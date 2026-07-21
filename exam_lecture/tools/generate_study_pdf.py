#!/usr/bin/env python3
"""Render the unit vocabulary/grammar Markdown sources as styled study PDFs."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)


NAVY = colors.HexColor("#17324D")
TEAL = colors.HexColor("#087E8B")
MINT = colors.HexColor("#E8F5F3")
AMBER = colors.HexColor("#F4A261")
CREAM = colors.HexColor("#FFF7E8")
INK = colors.HexColor("#23313D")
MUTED = colors.HexColor("#5D6B78")
LINE = colors.HexColor("#D8E2E8")
PAPER = colors.HexColor("#FCFDFE")


def register_fonts() -> None:
    font_dir = Path("/System/Library/Fonts/Supplemental")
    fonts = {
        "StudySans": font_dir / "Arial.ttf",
        "StudySans-Bold": font_dir / "Arial Bold.ttf",
        "StudySans-Italic": font_dir / "Arial Italic.ttf",
        "StudyMono": font_dir / "Courier New.ttf",
        "StudyMono-Bold": font_dir / "Courier New Bold.ttf",
    }
    missing = [str(path) for path in fonts.values() if not path.exists()]
    if missing:
        raise SystemExit(f"Required fonts not found: {', '.join(missing)}")
    for name, path in fonts.items():
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily(
        "StudySans",
        normal="StudySans",
        bold="StudySans-Bold",
        italic="StudySans-Italic",
        boldItalic="StudySans-Bold",
    )


def inline_markup(value: str) -> str:
    """Convert the small inline-Markdown subset used by the study notes."""
    value = escape(value.strip())
    value = re.sub(
        r"\[([^]]+)]\(([^)]+)\)",
        r'<font color="#087E8B"><u>\1</u></font>',
        value,
    )
    value = re.sub(
        r"`([^`]+)`",
        r'<font name="StudyMono" color="#A23E48">\1</font>',
        value,
    )
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    return value


def paragraph_markup(lines: list[str]) -> str:
    parts: list[str] = []
    for line in lines:
        hard_break = line.endswith("  ") or line.endswith("\\")
        clean_line = line[:-1] if line.endswith("\\") else line.rstrip()
        parts.append(inline_markup(clean_line))
        if hard_break:
            parts.append("<br/>")
        else:
            parts.append(" ")
    return "".join(parts).strip()


def build_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "body": ParagraphStyle(
            "StudyBody",
            parent=base["BodyText"],
            fontName="StudySans",
            fontSize=10.2,
            leading=15,
            textColor=INK,
            spaceAfter=7,
        ),
        "h2": ParagraphStyle(
            "StudyH2",
            parent=base["Heading2"],
            fontName="StudySans-Bold",
            fontSize=16,
            leading=19,
            textColor=NAVY,
            spaceBefore=13,
            spaceAfter=8,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "StudyH3",
            parent=base["Heading3"],
            fontName="StudySans-Bold",
            fontSize=11.2,
            leading=14,
            textColor=NAVY,
            backColor=MINT,
            borderColor=TEAL,
            borderWidth=0.8,
            borderPadding=(5, 7, 5, 7),
            borderRadius=3,
            spaceBefore=9,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "callout": ParagraphStyle(
            "StudyCallout",
            parent=base["BodyText"],
            fontName="StudySans",
            fontSize=9.6,
            leading=14,
            textColor=INK,
        ),
        "table": ParagraphStyle(
            "StudyTable",
            parent=base["BodyText"],
            fontName="StudySans",
            fontSize=8.5,
            leading=11,
            textColor=INK,
        ),
        "table_head": ParagraphStyle(
            "StudyTableHead",
            parent=base["BodyText"],
            fontName="StudySans-Bold",
            fontSize=8.7,
            leading=11,
            textColor=colors.white,
            alignment=TA_CENTER,
        ),
        "code": ParagraphStyle(
            "StudyCode",
            parent=base["Code"],
            fontName="StudyMono",
            fontSize=8.2,
            leading=11,
            textColor=colors.HexColor("#EAF2F8"),
            leftIndent=0,
        ),
        "cover_tag": ParagraphStyle(
            "CoverTag",
            parent=base["BodyText"],
            fontName="StudySans-Bold",
            fontSize=10,
            leading=13,
            textColor=TEAL,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "cover_title": ParagraphStyle(
            "CoverTitle",
            parent=base["Title"],
            fontName="StudySans-Bold",
            fontSize=25,
            leading=30,
            textColor=colors.white,
            alignment=TA_CENTER,
        ),
        "cover_sub": ParagraphStyle(
            "CoverSub",
            parent=base["BodyText"],
            fontName="StudySans",
            fontSize=10.5,
            leading=15,
            textColor=MUTED,
            alignment=TA_CENTER,
        ),
    }


def make_cover(title: str, styles: dict[str, ParagraphStyle]):
    banner = Table(
        [[Paragraph(inline_markup(title), styles["cover_title"])]],
        colWidths=[165 * mm],
    )
    banner.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("BOX", (0, 0), (-1, -1), 1.2, TEAL),
                ("LEFTPADDING", (0, 0), (-1, -1), 12 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 16 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 16 * mm),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return [
        Spacer(1, 5 * mm),
        Paragraph("JAVA 17 OCP · YDS STUDY SERIES", styles["cover_tag"]),
        banner,
        Spacer(1, 5 * mm),
        Paragraph(
            "Teknik İngilizceyi bağlam içinde öğren · kısa tekrarlarla kalıcılaştır",
            styles["cover_sub"],
        ),
        Spacer(1, 7 * mm),
    ]


def make_callout(lines: list[str], styles: dict[str, ParagraphStyle]):
    content = Paragraph(paragraph_markup(lines), styles["callout"])
    table = Table([[content]], colWidths=[165 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CREAM),
                ("LINEBEFORE", (0, 0), (0, -1), 4, AMBER),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#F2D6A2")),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def make_code(code: list[str], styles: dict[str, ParagraphStyle]):
    pre = Preformatted("\n".join(code).rstrip(), styles["code"])
    table = Table([[pre]], colWidths=[165 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#1E2933")),
                ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#405363")),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def make_table(rows: list[list[str]], styles: dict[str, ParagraphStyle]):
    count = max(len(row) for row in rows)
    normalized = [row + [""] * (count - len(row)) for row in rows]
    rendered = []
    for row_number, row in enumerate(normalized):
        style = styles["table_head"] if row_number == 0 else styles["table"]
        rendered.append([Paragraph(inline_markup(cell), style) for cell in row])
    widths = [165 * mm / count] * count
    table = Table(rendered, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), TEAL),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, MINT]),
                ("GRID", (0, 0), (-1, -1), 0.45, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def parse_table(lines: list[str], start: int) -> tuple[list[list[str]], int] | None:
    if start + 1 >= len(lines) or not lines[start].lstrip().startswith("|"):
        return None
    separator = lines[start + 1]
    if not re.match(r"^\s*\|?\s*:?-{3,}", separator):
        return None
    rows: list[list[str]] = []
    index = start
    while index < len(lines) and lines[index].lstrip().startswith("|"):
        if index != start + 1:
            rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
        index += 1
    return rows, index


def markdown_to_story(markdown: str, styles: dict[str, ParagraphStyle]):
    lines = markdown.splitlines()
    story = []
    paragraph_lines: list[str] = []
    list_items: list[str] = []
    list_ordered = False

    def flush_paragraph() -> None:
        if paragraph_lines:
            story.append(Paragraph(paragraph_markup(paragraph_lines), styles["body"]))
            paragraph_lines.clear()

    def flush_list() -> None:
        nonlocal list_ordered
        if not list_items:
            return
        items = [
            ListItem(Paragraph(inline_markup(item), styles["body"]), leftIndent=9)
            for item in list_items
        ]
        list_flowable = ListFlowable(
            items,
            bulletType="1" if list_ordered else "bullet",
            start="1" if list_ordered else None,
            leftIndent=17,
            bulletFontName="StudySans-Bold",
            bulletFontSize=8,
            bulletColor=TEAL,
            spaceAfter=6,
        )
        if (
            story
            and isinstance(story[-1], Paragraph)
            and story[-1].style.name == "StudyH3"
        ):
            heading = story.pop()
            story.append(KeepTogether([heading, list_flowable]))
        else:
            story.append(list_flowable)
        list_items.clear()
        list_ordered = False

    index = 0
    seen_title = False
    while index < len(lines):
        line = lines[index]

        if line.startswith("```"):
            flush_paragraph()
            flush_list()
            index += 1
            code: list[str] = []
            while index < len(lines) and not lines[index].startswith("```"):
                code.append(lines[index])
                index += 1
            story.extend([make_code(code, styles), Spacer(1, 3 * mm)])
            index += 1
            continue

        table_result = parse_table(lines, index)
        if table_result:
            flush_paragraph()
            flush_list()
            rows, index = table_result
            story.extend([make_table(rows, styles), Spacer(1, 3 * mm)])
            continue

        if line.startswith(">"):
            flush_paragraph()
            flush_list()
            quote: list[str] = []
            while index < len(lines) and lines[index].startswith(">"):
                quote.append(lines[index][1:].lstrip())
                index += 1
            story.extend([make_callout(quote, styles), Spacer(1, 3 * mm)])
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            flush_list()
            level = len(heading.group(1))
            title = heading.group(2)
            if level == 1 and not seen_title:
                story.extend(make_cover(title, styles))
                seen_title = True
            else:
                story.append(Paragraph(inline_markup(title), styles[f"h{min(level, 3)}"]))
            index += 1
            continue

        unordered = re.match(r"^\s*-\s+(.+)$", line)
        ordered = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if unordered or ordered:
            flush_paragraph()
            current_ordered = bool(ordered)
            if list_items and current_ordered != list_ordered:
                flush_list()
            list_ordered = current_ordered
            list_items.append((ordered or unordered).group(1))
            index += 1
            continue

        if not line.strip() or line.strip() == "---":
            flush_paragraph()
            flush_list()
            if line.strip() == "---":
                story.append(Spacer(1, 2 * mm))
            index += 1
            continue

        if list_items and line.startswith("  "):
            list_items[-1] += " " + line.strip()
        else:
            flush_list()
            paragraph_lines.append(line)
        index += 1

    flush_paragraph()
    flush_list()
    return story


class StudyDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, title: str):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=22 * mm,
            rightMargin=23 * mm,
            topMargin=20 * mm,
            bottomMargin=19 * mm,
            title=title,
            author="OCP Java 17 & YDS Study Project",
        )
        self.study_title = title
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="study-frame",
        )
        self.addPageTemplates(PageTemplate(id="study", frames=[frame], onPage=self.decorate_page))

    def decorate_page(self, canvas, doc) -> None:
        canvas.saveState()
        width, height = A4
        canvas.setFillColor(PAPER)
        canvas.rect(0, 0, width, height, stroke=0, fill=1)

        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(22 * mm, height - 13 * mm, width - 23 * mm, height - 13 * mm)
        canvas.line(22 * mm, 12 * mm, width - 23 * mm, 12 * mm)

        canvas.setFont("StudySans-Bold", 7.5)
        canvas.setFillColor(TEAL)
        canvas.drawString(22 * mm, height - 10 * mm, "UNIT 01 · BUILDING BLOCKS")

        canvas.setFont("StudySans", 7.5)
        canvas.setFillColor(MUTED)
        short_title = self.study_title
        if len(short_title) > 55:
            short_title = short_title[:52] + "..."
        canvas.drawRightString(width - 23 * mm, height - 10 * mm, short_title)
        canvas.drawString(22 * mm, 8 * mm, "Java 17 OCP + Teknik İngilizce")
        canvas.drawRightString(width - 23 * mm, 8 * mm, f"{doc.page}")
        canvas.restoreState()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    register_fonts()
    markdown = args.input.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", markdown, flags=re.MULTILINE)
    if not title_match:
        raise SystemExit("Markdown source must contain a level-one title")
    title = title_match.group(1).strip()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    document = StudyDocTemplate(str(args.output), title)
    document.build(markdown_to_story(markdown, build_styles()))
    print(f"Generated {args.output}")


if __name__ == "__main__":
    main()
