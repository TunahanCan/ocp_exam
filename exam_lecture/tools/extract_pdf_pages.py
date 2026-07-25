#!/usr/bin/env python3
"""Extract positioned PDF text runs and font metadata with Poppler.

The output schema matches ``extract_pdf_pages.swift`` so the bilingual unit
builder works on Linux systems where PDFKit is unavailable.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path


def extract_page(pdf: Path, page_number: int) -> tuple[list[dict[str, object]], str]:
    result = subprocess.run(
        [
            "pdftohtml",
            "-f",
            str(page_number),
            "-l",
            str(page_number),
            "-xml",
            "-stdout",
            "-hidden",
            "-nodrm",
            "-i",
            str(pdf),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    root = ET.fromstring(result.stdout)
    page = root.find(".//page")
    if page is None:
        return [], ""

    # pdftohtml uses a 1.5x coordinate system for this source. Derive the
    # scale from the PDF's known page width rather than hard-coding it.
    rendered_width = float(page.attrib["width"])
    source_width = 531.0
    scale = rendered_width / source_width
    rendered_height = float(page.attrib["height"])
    fonts = {
        item.attrib["id"]: {
            "size": float(item.attrib.get("size", "0")) / scale,
            "family": item.attrib.get("family", ""),
        }
        for item in page.findall("fontspec")
    }
    records: list[dict[str, object]] = []
    plain_lines: list[str] = []
    for item in page.findall("text"):
        text = "".join(item.itertext()).strip()
        if not text:
            continue

        top = float(item.attrib["top"])
        height = float(item.attrib["height"])
        font = fonts.get(item.attrib.get("font", ""), {"size": 0.0, "family": ""})
        records.append(
            {
                "text": text,
                "x": float(item.attrib["left"]) / scale,
                # Use the text run's top baseline so inline monospace spans
                # merge with surrounding prose despite their taller box.
                "y": (rendered_height - top) / scale,
                "width": float(item.attrib["width"]) / scale,
                "height": height / scale,
                "dominantFontSize": round(float(font["size"]), 2),
                "fontFamily": str(font["family"]),
            }
        )
        plain_lines.append(text)
    return records, "\n".join(plain_lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("start_page", type=int)
    parser.add_argument("end_page", type=int)
    args = parser.parse_args()

    if args.start_page < 1 or args.end_page < args.start_page:
        parser.error("page numbers must define a positive inclusive range")
    args.output_directory.mkdir(parents=True, exist_ok=True)

    total = args.end_page - args.start_page + 1
    for index, page_number in enumerate(
        range(args.start_page, args.end_page + 1), start=1
    ):
        records, plain_text = extract_page(args.input, page_number)
        stem = f"page-{page_number:04d}"
        (args.output_directory / f"{stem}.layout.json").write_text(
            json.dumps(records, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (args.output_directory / f"{stem}.txt").write_text(
            f"===== PDF PAGE {page_number} =====\n{plain_text}\n",
            encoding="utf-8",
        )
        print(f"page {index}/{total}: {page_number}", flush=True)


if __name__ == "__main__":
    main()
