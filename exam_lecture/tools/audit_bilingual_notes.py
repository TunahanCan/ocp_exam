#!/usr/bin/env python3
"""Audit page coverage and structural integrity of bilingual unit notes.

The source directory is expected to contain files named ``page-NNNN.txt``.
Those files can be produced from the project source PDF with PDFKit or another
text extractor. The comparison deliberately normalizes punctuation and OCR
line-break hyphenation, while retaining the source word order.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
import unicodedata
from pathlib import Path


PAGE_MARKER = re.compile(r"^<!-- source-page: (\d{4}) -->$", re.MULTILINE)
ENGLISH_LABEL = re.compile(r"^> \*\*English(?:[^*]*)?:\*\*\s*(.*)$")
TURKISH_LABEL = re.compile(r"^> \*\*Türkçe(?:[^*]*)?:\*\*")
PAIRED_ENGLISH_LABEL = re.compile(
    r"^> \*\*English(?::|\s+—\s+[^:]+:)\*\*",
    re.MULTILINE,
)
PAIRED_TURKISH_LABEL = re.compile(
    r"^> \*\*Türkçe(?::|\s+—\s+[^:]+:)\*\*",
    re.MULTILINE,
)
GROUPED_OPTION_LABEL = re.compile(
    r"^> \*\*English(?::|\s+—\s+[^:]+:)\*\*\s+"
    r"(?:\d+\.\s+)?[A-H]\.\s+[A-H]\.",
    re.MULTILINE,
)
MERGED_QUESTION_AND_CODE_LINE = re.compile(
    r"^> \*\*English(?::|\s+—\s+[^:]+:)\*\*\s+\d+\.\s+\d+:",
    re.MULTILINE,
)
KNOWN_OCR_WORD_BREAK = re.compile(
    r"\b(?:Object|String|Local|no|non|top|zero|pass|var|con|self|case|user|"
    r"built|stand|floating|package|pre|difficult|lowest)-\s+"
    r"(?:Oriented|Builder|Date|argument|abstract|sealed|level|based|by|"
    r"iable|iables|structor|explanatory|sensitive|defined|in|alone|point|"
    r"private|initialized|maintain|arg)",
    re.IGNORECASE,
)
KNOWN_BAD_TRANSLATIONS = re.compile(
    r"\bKAY\s+SIS\b|\bÖRÜŞ(?:ÜN)+\b|\bebeveynlik\b|"
    r"\bgenel\s+geçersiz\b|\btaklit\s+edilebilir\b|\boperacı\b|"
    r"\bmethodin\b|\bruntimena\b|\bruntimenda\b|\bJavada\b|"
    r"['\"](?:Java|object|class|reference|method|runtime)['\"]|"
    r"pattern\s+matchingyi['\"]|String\s*-\s*Builder",
)


def split_source_pages(markdown: str) -> dict[int, str]:
    parts = PAGE_MARKER.split(markdown)
    return {int(parts[index]): parts[index + 1] for index in range(1, len(parts), 2)}


def extract_english_source(markdown: str) -> str:
    """Return English, code, headings, and table rows from one page section."""
    output: list[str] = []
    in_english = False
    in_code = False

    for line in markdown.splitlines():
        if line.startswith("## Coverage ledger") or line.startswith("## Appendix"):
            break
        if line.startswith("```"):
            in_code = not in_code
            output.append(line)
            continue
        if in_code:
            output.append(line)
            continue
        if TURKISH_LABEL.match(line):
            in_english = False
            continue
        english = ENGLISH_LABEL.match(line)
        if english:
            in_english = True
            output.append(english.group(1))
            continue
        if in_english and line.startswith(">"):
            output.append(re.sub(r"^> ?", "", line))
            continue
        if in_english and not line.strip():
            continue
        in_english = False

        if re.match(r"^#{2,4}\s+", line):
            output.append(re.sub(r"^#+\s*", "", line))
        elif line.startswith("|"):
            output.append(line)

    return "\n".join(output)


def normalized_tokens(text: str) -> list[str]:
    text = (
        text.replace("\u00ad", "")
        .replace("‐", "-")
        .replace("‑", "-")
        .replace("–", "-")
        .replace("—", "-")
    )
    text = re.sub(r"(?<=[A-Za-z])-\s+(?=[a-z])", "", text)
    text = unicodedata.normalize("NFKD", text)
    return re.findall(r"[a-z0-9]+", text.lower())


def matched_source_ratio(source: str, notes: str) -> tuple[float, int, int, int]:
    source_tokens = normalized_tokens(source)
    note_tokens = normalized_tokens(notes)
    matcher = difflib.SequenceMatcher(
        None,
        source_tokens,
        note_tokens,
        autojunk=False,
    )
    matched = sum(block.size for block in matcher.get_matching_blocks())
    ratio = matched / len(source_tokens) if source_tokens else 1.0
    return ratio, matched, len(source_tokens), len(note_tokens)


def broken_translation_lines(markdown: str) -> list[int]:
    """Return bad-pattern line numbers, considering Turkish prose only."""
    hits: list[int] = []
    in_turkish = False
    for line_number, line in enumerate(markdown.splitlines(), start=1):
        if line.startswith("```"):
            in_turkish = False
            continue
        if re.match(r"^> \*\*English", line):
            in_turkish = False
            continue
        if re.match(r"^> \*\*Türkçe", line):
            in_turkish = True
        elif in_turkish and not line.startswith(">"):
            in_turkish = False
        if in_turkish and KNOWN_BAD_TRANSLATIONS.search(line):
            hits.append(line_number)
    return hits


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("source_pages", type=Path)
    parser.add_argument("start_page", type=int)
    parser.add_argument("end_page", type=int)
    parser.add_argument("--minimum-global-coverage", type=float, default=0.96)
    args = parser.parse_args()

    markdown = args.markdown.read_text(encoding="utf-8")
    pages = split_source_pages(markdown)
    expected_pages = list(range(args.start_page, args.end_page + 1))
    actual_pages = sorted(page for page in pages if page in expected_pages)
    structural_errors: list[str] = []

    if actual_pages != expected_pages:
        missing = sorted(set(expected_pages) - set(actual_pages))
        unexpected = sorted(set(actual_pages) - set(expected_pages))
        structural_errors.append(f"page marker mismatch; missing={missing}, unexpected={unexpected}")

    english_count = len(PAIRED_ENGLISH_LABEL.findall(markdown))
    turkish_count = len(PAIRED_TURKISH_LABEL.findall(markdown))
    if english_count != turkish_count:
        structural_errors.append(
            f"English/Türkçe label mismatch: {english_count}/{turkish_count}"
        )

    fence_count = len(re.findall(r"^```", markdown, re.MULTILINE))
    if fence_count % 2:
        structural_errors.append(f"unbalanced code fences: {fence_count}")
    if "FULL_SOURCE_INSERT" in markdown:
        structural_errors.append("FULL_SOURCE_INSERT placeholder remains")
    if "\u00ad" in markdown:
        structural_errors.append("soft-hyphen characters remain")
    if "\ufffd" in markdown:
        structural_errors.append("Unicode replacement characters remain")
    if not re.search(r"^## İçindekiler\s*$", markdown, re.MULTILINE):
        structural_errors.append("missing İçindekiler section")
    grouped_option_hits = [
        markdown.count("\n", 0, match.start()) + 1
        for match in GROUPED_OPTION_LABEL.finditer(markdown)
    ]
    if grouped_option_hits:
        structural_errors.append(
            f"grouped review-option labels at lines {grouped_option_hits[:10]}"
        )
    merged_question_hits = [
        markdown.count("\n", 0, match.start()) + 1
        for match in MERGED_QUESTION_AND_CODE_LINE.finditer(markdown)
    ]
    if merged_question_hits:
        structural_errors.append(
            "question numbers merged with code line numbers at lines "
            f"{merged_question_hits[:10]}"
        )
    broken_hyphen_hits = [
        markdown.count("\n", 0, match.start()) + 1
        for match in KNOWN_OCR_WORD_BREAK.finditer(markdown)
    ]
    if broken_hyphen_hits:
        structural_errors.append(
            f"known OCR word-break hyphens at lines {broken_hyphen_hits[:10]}"
        )

    bad_translation_hits = broken_translation_lines(markdown)
    if bad_translation_hits:
        structural_errors.append(
            f"known broken translation patterns at lines {bad_translation_hits[:10]}"
        )

    total_source: list[str] = []
    total_notes: list[str] = []
    page_results: list[tuple[float, int]] = []
    for page in expected_pages:
        source_path = args.source_pages / f"page-{page:04d}.txt"
        if not source_path.exists() or page not in pages:
            continue
        source = source_path.read_text(encoding="utf-8")
        source = re.sub(r"^===== PDF PAGE \d+ =====\n", "", source)
        notes = extract_english_source(pages[page])
        ratio, _, _, _ = matched_source_ratio(source, notes)
        page_results.append((ratio, page))
        total_source.append(source)
        total_notes.append(notes)

    global_ratio, matched, source_count, note_count = matched_source_ratio(
        "\n".join(total_source),
        "\n".join(total_notes),
    )
    if global_ratio < args.minimum_global_coverage:
        structural_errors.append(
            "global normalized source coverage "
            f"{global_ratio:.2%} is below {args.minimum_global_coverage:.2%}"
        )

    print(f"file: {args.markdown}")
    print(f"page markers: {len(actual_pages)}/{len(expected_pages)}")
    print(f"English/Türkçe labels: {english_count}/{turkish_count}")
    print(f"code fences: {fence_count} ({'balanced' if fence_count % 2 == 0 else 'unbalanced'})")
    print(
        "normalized source coverage: "
        f"{global_ratio:.2%} ({matched}/{source_count} source tokens; {note_count} note tokens)"
    )
    print("lowest page ratios:")
    for ratio, page in sorted(page_results)[:10]:
        print(f"  {page:04d}: {ratio:.2%}")

    if structural_errors:
        print("FAIL:")
        for error in structural_errors:
            print(f"  - {error}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
