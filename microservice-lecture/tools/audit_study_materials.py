#!/usr/bin/env python3
"""Check local study links, bilingual pairs, figure inventory and PDF bounds.

Uses only Python's standard library and the existing Poppler commands. This
structural audit does not replace translation review or visual page inspection.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_unit(unit):
    errors, documents = [], []
    for name in ("README.md", "bilingual_notes.md", "bilingual_notes.pdf",
                 "vocabulary.md", "vocabulary.pdf", "grammar_notes.md", "grammar_notes.pdf"):
        if not (unit / name).exists():
            errors.append(f"missing {name}")
    for source in sorted(unit.glob("*.md")):
        text = source.read_text()
        if text.count("```") % 2:
            errors.append(f"{source.name}: unmatched code fence")
        without_code = re.sub(r"```.*?```", "", text, flags=re.S)
        if len(re.findall(r"^# ", without_code, re.M)) != 1:
            errors.append(f"{source.name}: expected one H1")
        for target in re.findall(r"\]\(([^\s)]+)\)", without_code):
            if re.match(r"[a-z]+://|mailto:|#", target):
                continue
            local = target.split("#")[0].strip("<>")
            if local and not (source.parent / local).exists():
                errors.append(f"{source.name}: missing link {local}")
        if source.stem == "bilingual_notes":
            labels = re.findall(r"^> \*\*(English|Türkçe):\*\*", without_code, re.M)
            if any(label != ("English" if i % 2 == 0 else "Türkçe") for i, label in enumerate(labels)) or len(labels) % 2:
                errors.append(f"{source.name}: nonalternating language labels")
            ids = re.findall(r"<!-- source-record: (.*?) -->", text)
            if len(ids) != len(set(ids)):
                errors.append(f"{source.name}: duplicate source record IDs")
            if ids and ids != sorted(ids):
                errors.append(f"{source.name}: source record order changed")
            manifest = json.loads((unit / "assets/manifest.json").read_text())
            expected = ["assets/" + f["file"] for f in manifest["figures"]]
            actual = re.findall(r"^!\[[^\]]*\]\((assets/[^)]+)\)", text, re.M)
            if actual != expected:
                errors.append(f"{source.name}: figure order/inventory differs from manifest")
        pdf = source.with_suffix(".pdf")
        if not pdf.exists():
            continue
        result = subprocess.run(["pdftotext", "-bbox-layout", str(pdf), "-"],
                                capture_output=True, check=True)
        xml = ET.fromstring(result.stdout)
        pages = xml.findall(".//{*}page")
        pair_counts, blank_pages, overflow = [], [], []
        for page_no, page in enumerate(pages, 1):
            words = page.findall(".//{*}word")
            body = [w for w in words if 42 < float(w.attrib["yMin"]) < 798]
            if not body:
                blank_pages.append(page_no)
            width, height = float(page.attrib["width"]), float(page.attrib["height"])
            for w in words:
                a = w.attrib
                if (float(a["xMin"]) < -0.5 or float(a["yMin"]) < -0.5 or
                    float(a["xMax"]) > width + 0.5 or float(a["yMax"]) > height + 0.5):
                    overflow.append({"page": page_no, "word": w.text})
            en = sum(w.text == "English:" for w in words)
            tr = sum(w.text == "Türkçe:" for w in words)
            if source.stem == "bilingual_notes" and en != tr:
                pair_counts.append({"page": page_no, "english": en, "turkish": tr})
        if blank_pages:
            errors.append(f"{pdf.name}: empty content pages {blank_pages}")
        if overflow:
            errors.append(f"{pdf.name}: {len(overflow)} words beyond page bounds")
        documents.append({"source": source.name, "pdf": pdf.name, "pages": len(pages),
                          "source_sha256": sha256(source), "pdf_sha256": sha256(pdf),
                          "page_pair_count_differences": pair_counts,
                          "overflow": overflow, "empty_content_pages": blank_pages})
    return {"unit": unit.name, "documents": documents, "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--units", help="Comma-separated unit numbers; default all")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    selected = {int(n) for n in args.units.split(",")} if args.units else None
    units = [p for p in sorted((ROOT / "units").glob("unit_*"))
             if selected is None or int(p.name.split("_")[1]) in selected]
    source_map = json.loads((ROOT / "source_map.json").read_text())
    source_pdf = ROOT / Path(source_map["source_pdf"]).name
    report = {"source_pdf_unchanged": sha256(source_pdf) == source_map["source_sha256"],
              "units": [audit_unit(u) for u in units],
              "scope": "Structural checks only; visual and semantic review reported separately."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    errors = sum(len(u["errors"]) for u in report["units"])
    docs = [d for u in report["units"] for d in u["documents"]]
    print(f"{len(units)} units, {len(docs)} PDFs, {sum(d['pages'] for d in docs)} pages, {errors} errors")
    for unit in report["units"]:
        for error in unit["errors"]:
            print(unit["unit"], error)
    if errors or not report["source_pdf_unchanged"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
