#!/usr/bin/env python3
"""Audit the completeness and navigation of the unit study materials."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


REQUIRED_MARKDOWN = (
    "README.md",
    "bilingual_notes.md",
    "technical_memory_notes.md",
    "vocabulary.md",
    "grammar_notes.md",
    "practice_quiz.md",
)
PDF_STEMS = (
    "bilingual_notes",
    "technical_memory_notes",
    "vocabulary",
    "grammar_notes",
    "practice_quiz",
)
REVIEW_QUESTION_COUNTS = {
    "unit_01_building_blocks": 23,
    "unit_02_operators": 21,
    "unit_03_making_decisions": 29,
    "unit_04_core_apis": 22,
    "unit_05_methods": 21,
    "unit_06_class_design": 26,
    "unit_07_beyond_classes": 30,
    "unit_08_lambdas_and_functional_interfaces": 21,
    "unit_09_collections_and_generics": 20,
    "unit_10_streams": 21,
    "unit_11_exceptions_and_localization": 26,
    "unit_12_modules": 25,
    "unit_13_concurrency": 25,
    "unit_14_i_o": 25,
    "unit_15_jdbc": 21,
}
FORBIDDEN_TEXT = (
    "\ufffd",
    "■",
    "TODO_TRANSLATION",
    "TRANSLATION_PENDING",
    "<placeholder>",
    "<<<<<<<",
    "=======",
    ">>>>>>>",
)
FORBIDDEN_PATTERNS = (
    re.compile(
        r"^[ \t]*>[ \t]*\*\*English:\*\*[ \t]*(?:\.\.\.|…)[ \t]*$",
        re.MULTILINE,
    ),
    re.compile(
        r"^[ \t]*>[ \t]*\*\*Türkçe:\*\*[ \t]*(?:\.\.\.|…)[ \t]*$",
        re.MULTILINE,
    ),
)


def github_slug(title: str) -> str:
    """Return the GitHub-style base slug used by this repository's headings."""
    title = re.sub(r"`([^`]*)`", r"\1", title)
    title = re.sub(r"<[^>]+>", "", title).strip().lower()
    title = "".join(
        character
        for character in title
        if character.isalnum() or character in " _-"
    )
    return re.sub(r"\s", "-", title)


def prose_lines(text: str) -> list[str]:
    """Return Markdown lines outside fenced code blocks."""
    lines: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append(line)
    return lines


def heading_anchors(path: Path) -> set[str]:
    """Collect heading anchors, including duplicate-heading suffixes."""
    seen: dict[str, int] = {}
    anchors: set[str] = set()
    for line in prose_lines(path.read_text(encoding="utf-8")):
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line)
        if not match:
            continue
        base = github_slug(match.group(1))
        duplicate_index = seen.get(base, 0)
        seen[base] = duplicate_index + 1
        anchors.add(base if duplicate_index == 0 else f"{base}-{duplicate_index}")
    return anchors


def markdown_links(path: Path) -> list[str]:
    """Return normal Markdown link targets, excluding image links."""
    text = "\n".join(prose_lines(path.read_text(encoding="utf-8")))
    return re.findall(r"(?<!!)\[[^]]+]\(([^)]+)\)", text)


def audit_markdown(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    lines = prose_lines(text)
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.endswith((" ", "\t")):
            errors.append(f"{path}:{line_number}: trailing whitespace")
    h1_count = sum(bool(re.match(r"^#\s+", line)) for line in lines)
    if h1_count != 1:
        errors.append(f"{path}: expected one H1, found {h1_count}")
    heading_levels = [
        len(match.group(1))
        for line in lines
        if (match := re.match(r"^(#{1,6})\s+", line))
    ]
    for current, following in zip(heading_levels, heading_levels[1:]):
        if following > current + 1:
            errors.append(
                f"{path}: heading level jumps from H{current} to H{following}"
            )
    if text.count("```") % 2:
        errors.append(f"{path}: unbalanced code fences")
    for forbidden in FORBIDDEN_TEXT:
        if forbidden in text:
            errors.append(f"{path}: forbidden marker {forbidden!r}")
    for forbidden_pattern in FORBIDDEN_PATTERNS:
        if forbidden_pattern.search(text):
            errors.append(
                f"{path}: forbidden placeholder matching "
                f"{forbidden_pattern.pattern!r}"
            )

    for raw_target in markdown_links(path):
        target = raw_target.strip().split()[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        file_part, separator, fragment = target.partition("#")
        resolved = (
            (path.parent / unquote(file_part)).resolve()
            if file_part
            else path.resolve()
        )
        if not resolved.exists():
            errors.append(f"{path}: missing link target {target}")
            continue
        if separator and resolved.suffix.lower() == ".md":
            if unquote(fragment) not in heading_anchors(resolved):
                errors.append(f"{path}: missing heading target {target}")


def practice_question_count(path: Path) -> int:
    """Count numbered question headings before the answer section."""
    text = path.read_text(encoding="utf-8")
    question_part = re.split(
        r"^##\s+(?:Cevap|Answers?)",
        text,
        maxsplit=1,
        flags=re.MULTILINE | re.IGNORECASE,
    )[0]
    headings = re.findall(
        r"^#{2,4}\s+(?:Soru|Question)\s+(\d+)\b",
        question_part,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    return len(set(headings))


def review_question_section(path: Path) -> str | None:
    """Return the source-book review-question section from bilingual notes."""
    text = path.read_text(encoding="utf-8")
    start = re.search(
        r"^#{2,3}\s+Review Questions"
        r"(?:\s*/\s*Gözden Geçirme Soruları)?\s*$",
        text,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    if not start:
        return None
    remainder = text[start.end() :]
    end = re.search(
        r"^##\s+(?:"
        r"Appendix|Kapsam|Kaynak ve kapsam|Bölüm sonu|Cevaplar|Kaynak dışı"
        r")",
        remainder,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    return remainder[: end.start() if end else len(remainder)]


def audit_review_questions(path: Path, expected: int, errors: list[str]) -> int:
    """Validate clear boundaries and bilingual coverage for source questions."""
    section = review_question_section(path)
    if section is None:
        errors.append(f"{path}: missing Review Questions section")
        return 0

    headings = [
        int(number)
        for number in re.findall(
            r"^###\s+Question\s+(\d+)\s*/\s*Soru\s+\1\s*$",
            section,
            flags=re.MULTILINE | re.IGNORECASE,
        )
    ]
    wanted = list(range(1, expected + 1))
    if headings != wanted:
        errors.append(
            f"{path}: expected review headings 1..{expected}, found {headings}"
        )

    heading_matches = list(
        re.finditer(
            r"^###\s+Question\s+(\d+)\s*/\s*Soru\s+\1\s*$",
            section,
            flags=re.MULTILINE | re.IGNORECASE,
        )
    )
    for index, heading in enumerate(heading_matches):
        number = int(heading.group(1))
        chunk_end = (
            heading_matches[index + 1].start()
            if index + 1 < len(heading_matches)
            else len(section)
        )
        chunk = section[heading.end() : chunk_end]
        if not re.search(r"\*\*English(?:\s+—\s+[A-Z])?:\*\*", chunk):
            errors.append(f"{path}: review question {number} missing English")
        if not re.search(r"\*\*Türkçe(?:\s+—\s+[A-Z])?:\*\*", chunk):
            errors.append(f"{path}: review question {number} missing Turkish")
        english_blocks = re.findall(
            r"^>\s*\*\*English(?:\s+—\s+([A-Z]))?:\*\*\s*(.*)$",
            chunk,
            flags=re.MULTILINE,
        )
        if english_blocks:
            first_option, first_text = english_blocks[0]
            wrong_number = re.match(r"(\d+)\.\s+", first_text)
            if first_option or (
                wrong_number and int(wrong_number.group(1)) != number
            ):
                errors.append(
                    f"{path}: review question {number} has a malformed prompt"
                )
            if re.search(
                r"(?:fill\s+in|insert(?:ed)?\s+(?:in|into))\s+"
                r"(?:the\s+)?blank|blank\s+line",
                first_text,
                flags=re.IGNORECASE,
            ) and not re.search(
                r"_{3,}|INSERT\s+(?:CODE|OPTION)|//\s*LINE\b",
                chunk,
                flags=re.IGNORECASE,
            ):
                errors.append(
                    f"{path}: review question {number} describes a blank "
                    f"but has no visible placeholder"
                )
            for option, text in english_blocks[1:]:
                if not option and not re.match(r"[A-Z]\.(?:\s+.*)?$", text):
                    errors.append(
                        f"{path}: review question {number} has a fragmented "
                        f"English block {text!r}"
                    )
        option_letters: set[str] = set()
        for option, text in english_blocks[1:]:
            if option:
                option_letters.add(option)
                continue
            text_option = re.match(r"([A-Z])\.(?:\s+.*)?$", text)
            if text_option:
                option_letters.add(text_option.group(1))
        for option_fence in re.findall(
            r"^```(?:java|text)\s*\n(.*?)^```",
            chunk,
            flags=re.MULTILINE | re.DOTALL,
        ):
            option_letters.update(
                re.findall(
                    r"^\s*([A-Z])\.\s+",
                    option_fence,
                    flags=re.MULTILINE,
                )
            )
        if not option_letters:
            errors.append(f"{path}: review question {number} has no answer options")
        else:
            final_letter = max(option_letters)
            wanted_letters = {
                chr(code)
                for code in range(ord("A"), ord(final_letter) + 1)
            }
            if option_letters != wanted_letters:
                errors.append(
                    f"{path}: review question {number} has non-contiguous "
                    f"options {sorted(option_letters)}"
                )
        if re.search(
            r"^```\s*"
            r"(?:"
            r"<!--\s*source-page:[^>]+-->\s*"
            r"(?:##\s+(?:Source page|Kaynak PDF sayfası)[^\n]*\s*)?"
            r"|"
            r"##\s+(?:Source page|Kaynak PDF sayfası)[^\n]*\s*"
            r")"
            r"```(?:java|text)\s*$",
            chunk,
            flags=re.MULTILINE,
        ):
            errors.append(
                f"{path}: review question {number} has a page-split code block"
            )
        referenced_lines: set[str] = set()
        for first, second in re.findall(
            r"\blines?\s+(\d+)(?:\s+and\s+(\d+))?",
            chunk,
            flags=re.IGNORECASE,
        ):
            referenced_lines.add(first)
            if second:
                referenced_lines.add(second)
        for line_number in sorted(referenced_lines, key=int):
            if not re.search(
                rf"^\s*(?:{re.escape(line_number)}:|"
                rf"//\s*LINE\s+{re.escape(line_number)}\b)",
                chunk,
                flags=re.MULTILINE | re.IGNORECASE,
            ):
                errors.append(
                    f"{path}: review question {number} refers to line "
                    f"{line_number} but the code has no matching line number"
                )

    if "<!-- source-page:" not in section:
        errors.append(f"{path}: review questions missing source-page markers")
    if re.search(
        r"^##\s+(?:Source page|Kaynak PDF sayfası)\b",
        section,
        flags=re.MULTILINE | re.IGNORECASE,
    ):
        errors.append(
            f"{path}: review questions expose internal source-page headings"
        )
    if re.search(r"!\[[^]]*]\([^)]+\)", section):
        errors.append(
            f"{path}: review questions contain an image; transcribe code as text"
        )
    if re.search(
        r"\b(?:CODE|QUESTION|IMAGE)[ _-]?(?:MISSING|PLACEHOLDER)\b",
        section,
        flags=re.IGNORECASE,
    ):
        errors.append(f"{path}: review questions contain a missing-content marker")

    for language, content in re.findall(
        r"^```([^\n]*)\n(.*?)^```",
        section,
        flags=re.MULTILINE | re.DOTALL,
    ):
        if language.strip() not in {"java", "text", "bash"}:
            errors.append(
                f"{path}: review code fence has unsupported language "
                f"{language.strip()!r}"
            )
        if not content.strip():
            errors.append(f"{path}: review questions contain an empty code fence")

    return len(headings)


def audit_unit(unit: Path) -> tuple[int, int, list[str]]:
    errors: list[str] = []
    for filename in REQUIRED_MARKDOWN:
        path = unit / filename
        if not path.exists():
            errors.append(f"{unit}: missing {filename}")
            continue
        audit_markdown(path, errors)

    readme = unit / "README.md"
    if readme.exists():
        readme_text = readme.read_text(encoding="utf-8")
        normalized_readme = readme_text.lower()
        for phrase in ("hangi belge", "çalışma rotası", "hazır mıyım"):
            if phrase not in normalized_readme:
                errors.append(f"{readme}: missing user-guide phrase {phrase!r}")
        for stem in PDF_STEMS:
            for suffix in (".md", ".pdf"):
                target = f"{stem}{suffix}"
                if f"]({target})" not in readme_text:
                    errors.append(f"{readme}: missing direct link to {target}")
        if "](bilingual_notes.md#review-questions" not in readme_text:
            errors.append(f"{readme}: missing direct link to Review Questions")

    for stem in PDF_STEMS:
        markdown = unit / f"{stem}.md"
        pdf = unit / f"{stem}.pdf"
        if not pdf.exists():
            errors.append(f"{unit}: missing {pdf.name}")
        elif markdown.exists() and pdf.stat().st_mtime_ns < markdown.stat().st_mtime_ns:
            errors.append(f"{unit}: stale {pdf.name}")

    quiz = unit / "practice_quiz.md"
    question_count = practice_question_count(quiz) if quiz.exists() else 0
    if quiz.exists():
        quiz_text = quiz.read_text(encoding="utf-8").lower()
        if "özgün" not in quiz_text:
            errors.append(f"{quiz}: must identify questions as original study material")
        if question_count < 6:
            errors.append(f"{quiz}: expected at least 6 questions, found {question_count}")
        answers = re.split(r"^##\s+Cevap[^\n]*", quiz_text, maxsplit=1,
                           flags=re.MULTILINE | re.IGNORECASE)
        question_numbers = [int(number) for number in re.findall(
            r"^###\s+Soru\s+(\d+)\b", answers[0], re.MULTILINE | re.IGNORECASE
        )]
        if question_numbers != list(range(1, question_count + 1)):
            errors.append(f"{quiz}: non-sequential question numbers {question_numbers}")
        if len(answers) == 2:
            answer_numbers = [int(number) for number in re.findall(
                r"^###\s+(?:soru\s+)?(\d+)\b", answers[1], re.MULTILINE
            )]
            if answer_numbers != question_numbers:
                errors.append(f"{quiz}: answer headings do not match questions")
        if not re.search(
            r"^##\s+(?:Cevap|Answers?)",
            quiz_text,
            re.MULTILINE | re.IGNORECASE,
        ):
            errors.append(f"{quiz}: missing answer section")

    review_count = 0
    bilingual_notes = unit / "bilingual_notes.md"
    expected_review_count = REVIEW_QUESTION_COUNTS.get(unit.name)
    if bilingual_notes.exists() and expected_review_count is not None:
        review_count = audit_review_questions(
            bilingual_notes,
            expected_review_count,
            errors,
        )
        answer_numbers = [int(number) for number in re.findall(
            r"^###\s+Official Answer\s+(\d+)\b",
            bilingual_notes.read_text(encoding="utf-8"), re.MULTILINE
        )]
        if answer_numbers != list(range(1, expected_review_count + 1)):
            errors.append(f"{bilingual_notes}: source answer key incomplete; "
                          f"expected 1..{expected_review_count}, found {answer_numbers}")

    return question_count, review_count, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "units_root",
        nargs="?",
        type=Path,
        default=Path("exam_lecture/units"),
    )
    args = parser.parse_args()

    units = sorted(path for path in args.units_root.glob("unit_*") if path.is_dir())
    if not units:
        raise SystemExit(f"No unit directories found under {args.units_root}")

    all_errors: list[str] = []
    index = args.units_root / "README.md"
    if not index.exists():
        all_errors.append(f"{args.units_root}: missing README.md")
    shared_markdown = sorted(args.units_root.glob("*.md"))
    for path in shared_markdown:
        audit_markdown(path, all_errors)
    plan = args.units_root / "study_plan.md"
    plan_pdf = plan.with_suffix(".pdf")
    if plan.exists():
        if not plan_pdf.exists():
            all_errors.append(f"{plan}: missing PDF")
        elif plan_pdf.stat().st_mtime_ns < plan.stat().st_mtime_ns:
            all_errors.append(f"{plan}: stale PDF")

    for unit in units:
        question_count, review_count, errors = audit_unit(unit)
        all_errors.extend(errors)
        state = "PASS" if not errors else f"FAIL ({len(errors)})"
        print(
            f"{unit.name}: {state}; practice questions={question_count}; "
            f"review questions={review_count}"
        )

    if all_errors:
        print("\nErrors:", file=sys.stderr)
        for error in all_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"PASS: {len(units)} units; "
        f"{len(units) * len(REQUIRED_MARKDOWN) + len(shared_markdown)} Markdown files; "
        f"{len(units) * len(PDF_STEMS) + int(plan_pdf.exists())} PDFs; "
        f"{sum(REVIEW_QUESTION_COUNTS.values())} source review questions"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
