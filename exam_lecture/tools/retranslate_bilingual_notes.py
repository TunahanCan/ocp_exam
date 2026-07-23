#!/usr/bin/env python3
"""Replace Turkish quote blocks in bilingual notes with local NLLB output.

This optional quality pass keeps English source blocks and code unchanged. It
uses a locally cached Hugging Face model and protects Java/OCP terminology with
temporary XML-style placeholders before translation.
"""

from __future__ import annotations

import argparse
import re
import textwrap
from pathlib import Path

from build_bilingual_unit import normalize_ocr, protect_terms


ENGLISH_LABEL = re.compile(r"^> \*\*English(?:[^*]*)?:\*\*\s*(.*)$")
TURKISH_LABEL = re.compile(r"^> \*\*Türkçe(?:[^*]*)?:\*\*\s*(.*)$")
PLACEHOLDER = re.compile(r"<x\d+>")


def find_pairs(lines: list[str]) -> list[tuple[int, int, str]]:
    pairs: list[tuple[int, int, str]] = []
    index = 0
    while index < len(lines):
        match = ENGLISH_LABEL.match(lines[index])
        if not match:
            index += 1
            continue

        english_parts = [match.group(1)]
        cursor = index + 1
        while cursor < len(lines) and lines[cursor].startswith("> "):
            if ENGLISH_LABEL.match(lines[cursor]) or TURKISH_LABEL.match(lines[cursor]):
                break
            english_parts.append(lines[cursor][2:])
            cursor += 1

        if cursor >= len(lines) or lines[cursor] != ">":
            index += 1
            continue
        cursor += 1
        if cursor >= len(lines) or not TURKISH_LABEL.match(lines[cursor]):
            index += 1
            continue

        turkish_start = cursor
        cursor += 1
        while cursor < len(lines):
            if ENGLISH_LABEL.match(lines[cursor]):
                break
            if not lines[cursor].startswith(">"):
                break
            cursor += 1

        english = normalize_ocr(" ".join(english_parts))
        pairs.append((turkish_start, cursor, english))
        index = cursor
    return pairs


def chunk_text(text: str, limit: int = 650) -> list[str]:
    """Split prose into complete sentences before translation.

    NLLB sometimes omits a trailing rhetorical question when several sentences
    are translated as one long request. Keeping sentences separate gives every
    source sentence an explicit output while still wrapping unusually long
    sentences safely.
    """
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z<\"“])", text)
    chunks: list[str] = []
    for sentence in sentences:
        if len(sentence) > limit:
            chunks.extend(
                textwrap.wrap(
                    sentence,
                    width=limit,
                    break_long_words=False,
                    break_on_hyphens=False,
                )
            )
        else:
            chunks.append(sentence)
    return chunks or [text]


def restore_terms(text: str, replacements: dict[str, str]) -> str:
    for key, value in replacements.items():
        number = key[2:-1]
        variants = (
            key,
            key.replace("<", "< ").replace(">", " >"),
            f"x{number}>",
            f"x{number} >",
        )
        for variant in variants:
            text = text.replace(variant, value)
    return normalize_ocr(text)


def placeholder_present(text: str, key: str) -> bool:
    number = key[2:-1]
    variants = (
        key,
        key.replace("<", "< ").replace(">", " >"),
        f"x{number}>",
        f"x{number} >",
    )
    return any(variant in text for variant in variants)


def normalize_technical_translation(text: str) -> str:
    """Repair predictable literal translations of Java identifiers."""
    replacements = (
        (
            r"\b(?:Opsiyonel|Seçenek|Seçmeli|İsteğe bağlı)"
            r"(Double|Int|Long)?\b",
            r"Optional\1",
        ),
        (r"\bilkel (?:Akış|Akım)(?:lar|ları)?\b", "primitive Streams"),
        (r"\bdeney/çıkış/son olarak\b", "try/catch/finally"),
        (r"\bkaynaklarla deney\b", "try-with-resources"),
        (r"\bçoklu yakalama blo(?:ğu|kları)\b", "multi-catch block"),
        (r"\bJava['’]te\b", "Java'da"),
        (r"\bJava['’]nin\b", "Java'nın"),
        (r"\bJava['’]un\b", "Java'nın"),
        (r"\bJava['’]u\b", "Java'yı"),
    )
    for pattern, value in replacements:
        text = re.sub(pattern, value, text, flags=re.IGNORECASE)
    return normalize_ocr(text)


def turkish_quote(text: str) -> list[str]:
    wrapped = textwrap.wrap(
        text,
        width=88,
        break_long_words=False,
        break_on_hyphens=False,
    ) or [""]
    return [f"> **Türkçe:** {wrapped[0]}"] + [f"> {line}" for line in wrapped[1:]]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path, nargs="+")
    parser.add_argument(
        "--model",
        default="facebook/nllb-200-distilled-600M",
    )
    parser.add_argument("--ct2-model", type=Path)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument(
        "--architecture",
        choices=("nllb", "marian"),
        default="nllb",
    )
    parser.add_argument("--beam-size", type=int, default=1)
    args = parser.parse_args()

    documents: list[tuple[Path, list[str], list[tuple[int, int, str]]]] = []
    unique_english: list[str] = []
    seen: set[str] = set()
    for path in args.markdown:
        lines = path.read_text(encoding="utf-8").splitlines()
        pairs = find_pairs(lines)
        documents.append((path, lines, pairs))
        for _, _, english in pairs:
            if english not in seen:
                seen.add(english)
                unique_english.append(english)

    print(
        f"Loading {args.model} for {len(unique_english)} unique prose blocks",
        flush=True,
    )
    from transformers import AutoTokenizer

    tokenizer_options = {"local_files_only": True}
    if args.architecture == "nllb":
        tokenizer_options["src_lang"] = "eng_Latn"
    tokenizer = AutoTokenizer.from_pretrained(args.model, **tokenizer_options)

    chunk_records: list[tuple[str, dict[str, str], list[str]]] = []
    all_chunks: list[str] = []
    for english in unique_english:
        protected, replacements = protect_terms(english)
        chunks = chunk_text(protected)
        chunk_records.append((english, replacements, chunks))
        all_chunks.extend(chunks)

    translated_chunks: list[str] = []
    if args.ct2_model:
        import ctranslate2

        translator = ctranslate2.Translator(
            str(args.ct2_model),
            device="cpu",
            compute_type="int8",
            inter_threads=1,
            intra_threads=8,
        )
        for start in range(0, len(all_chunks), args.batch_size):
            batch = all_chunks[start : start + args.batch_size]
            source_tokens = [
                tokenizer.convert_ids_to_tokens(tokenizer.encode(text))
                for text in batch
            ]
            translate_options = {
                "beam_size": args.beam_size,
                "max_decoding_length": 512,
            }
            if args.architecture == "nllb":
                translate_options["target_prefix"] = [["tur_Latn"]] * len(batch)
            results = translator.translate_batch(source_tokens, **translate_options)
            for result in results:
                target_tokens = result.hypotheses[0]
                if args.architecture == "nllb":
                    target_tokens = target_tokens[1:]
                target_ids = tokenizer.convert_tokens_to_ids(target_tokens)
                translated_chunks.append(
                    tokenizer.decode(target_ids, skip_special_tokens=True)
                )
            print(
                f"translated {min(start + len(batch), len(all_chunks))}/"
                f"{len(all_chunks)} chunks",
                flush=True,
            )

        # A model can occasionally drop an XML-style placeholder. Re-run only
        # those individual sentences without placeholders instead of accepting
        # a truncated translation.
        fallback_indexes: list[int] = []
        fallback_sources: list[str] = []
        chunk_cursor = 0
        for _, replacements, chunks in chunk_records:
            for chunk in chunks:
                translated = translated_chunks[chunk_cursor]
                expected = PLACEHOLDER.findall(chunk)
                if any(
                    not placeholder_present(translated, key)
                    for key in expected
                ):
                    fallback_indexes.append(chunk_cursor)
                    fallback_sources.append(restore_terms(chunk, replacements))
                chunk_cursor += 1

        if fallback_sources:
            print(
                f"retranslating {len(fallback_sources)} chunks without placeholders",
                flush=True,
            )
            fallback_translations: list[str] = []
            for start in range(0, len(fallback_sources), args.batch_size):
                batch = fallback_sources[start : start + args.batch_size]
                source_tokens = [
                    tokenizer.convert_ids_to_tokens(tokenizer.encode(text))
                    for text in batch
                ]
                translate_options = {
                    "beam_size": args.beam_size,
                    "max_decoding_length": 512,
                }
                if args.architecture == "nllb":
                    translate_options["target_prefix"] = [
                        ["tur_Latn"]
                    ] * len(batch)
                results = translator.translate_batch(
                    source_tokens, **translate_options
                )
                for result in results:
                    target_tokens = result.hypotheses[0]
                    if args.architecture == "nllb":
                        target_tokens = target_tokens[1:]
                    target_ids = tokenizer.convert_tokens_to_ids(target_tokens)
                    fallback_translations.append(
                        tokenizer.decode(target_ids, skip_special_tokens=True)
                    )
            for index, translated in zip(
                fallback_indexes, fallback_translations, strict=True
            ):
                translated_chunks[index] = normalize_technical_translation(
                    translated
                )
    else:
        import torch
        from transformers import AutoModelForSeq2SeqLM

        model = AutoModelForSeq2SeqLM.from_pretrained(
            args.model,
            use_safetensors=False,
            local_files_only=True,
        )
        device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        model.to(device)
        model.eval()
        target_id = tokenizer.convert_tokens_to_ids("tur_Latn")
        with torch.inference_mode():
            for start in range(0, len(all_chunks), args.batch_size):
                batch = all_chunks[start : start + args.batch_size]
                encoded = tokenizer(
                    batch,
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                    max_length=512,
                ).to(device)
                generated = model.generate(
                    **encoded,
                    forced_bos_token_id=target_id,
                    max_length=512,
                    num_beams=1,
                )
                translated_chunks.extend(
                    tokenizer.batch_decode(generated, skip_special_tokens=True)
                )
                print(
                    f"translated {min(start + len(batch), len(all_chunks))}/"
                    f"{len(all_chunks)} chunks",
                    flush=True,
                )

    translation_map: dict[str, str] = {}
    cursor = 0
    for english, replacements, chunks in chunk_records:
        translated = " ".join(translated_chunks[cursor : cursor + len(chunks)])
        cursor += len(chunks)
        restored = restore_terms(translated, replacements)
        translation_map[english] = normalize_technical_translation(restored)

    for path, lines, pairs in documents:
        for start, end, english in reversed(pairs):
            lines[start:end] = turkish_quote(translation_map[english])
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        print(f"Updated {path} ({len(pairs)} paired blocks)", flush=True)


if __name__ == "__main__":
    main()
