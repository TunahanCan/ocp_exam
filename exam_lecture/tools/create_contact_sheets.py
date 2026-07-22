#!/usr/bin/env python3
"""Create labeled contact sheets from rendered PDF page PNG files."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def natural_page_key(path: Path) -> tuple[int, str]:
    digits = "".join(character for character in path.stem if character.isdigit())
    return (int(digits) if digits else 0, path.name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_directory", type=Path)
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--rows", type=int, default=4)
    parser.add_argument("--thumbnail-width", type=int, default=420)
    args = parser.parse_args()

    page_paths = sorted(args.input_directory.glob("page-*.png"), key=natural_page_key)
    if not page_paths:
        raise SystemExit(f"No page PNG files found in {args.input_directory}")

    args.output_directory.mkdir(parents=True, exist_ok=True)
    label_height = 34
    gap = 18
    first_page = Image.open(page_paths[0])
    aspect_ratio = first_page.height / first_page.width
    thumbnail_height = round(args.thumbnail_width * aspect_ratio)
    cell_width = args.thumbnail_width + gap
    cell_height = thumbnail_height + label_height + gap
    sheet_width = args.columns * cell_width + gap
    sheet_height = args.rows * cell_height + gap
    per_sheet = args.columns * args.rows
    font = ImageFont.load_default(size=20)

    for sheet_index, offset in enumerate(range(0, len(page_paths), per_sheet), start=1):
        sheet = Image.new("RGB", (sheet_width, sheet_height), "#d9e2ea")
        draw = ImageDraw.Draw(sheet)
        for position, page_path in enumerate(page_paths[offset : offset + per_sheet]):
            row, column = divmod(position, args.columns)
            x = gap + column * cell_width
            y = gap + row * cell_height
            with Image.open(page_path) as page:
                thumbnail = page.convert("RGB")
                thumbnail.thumbnail((args.thumbnail_width, thumbnail_height), Image.Resampling.LANCZOS)
                sheet.paste(thumbnail, (x, y + label_height))
            draw.text((x, y + 5), page_path.stem, fill="#102a43", font=font)
        output_path = args.output_directory / f"sheet-{sheet_index:02d}.png"
        sheet.save(output_path, optimize=True)

    print(
        f"Created {(len(page_paths) + per_sheet - 1) // per_sheet} contact sheets "
        f"for {len(page_paths)} pages in {args.output_directory}"
    )


if __name__ == "__main__":
    main()
