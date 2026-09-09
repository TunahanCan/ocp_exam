#!/usr/bin/env python3
"""Render a unit Markdown source as a styled study PDF."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote
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
    PageBreak,
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


def heading_slug(title: str) -> str:
    title = re.sub(r"`([^`]*)`", r"\1", title)
    title = re.sub(r"<[^>]+>", "", title).strip().lower()
    title = "".join(char for char in title if char.isalnum() or char in " _-")
    return re.sub(r"\s", "-", title)


def compact_running_title(title: str) -> str:
    """Return a short, meaningful title for the page header."""
    if " — " in title:
        return title.rsplit(" — ", maxsplit=1)[-1].strip()
    parts = title.split(" · ")
    if len(parts) >= 3:
        return parts[-1].strip()
    return title


def register_fonts() -> None:
    font_sets = (
        {
            "StudySans": Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
            "StudySans-Bold": Path(
                "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
            ),
            "StudySans-Italic": Path(
                "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
            ),
            "StudyMono": Path(
                "/System/Library/Fonts/Supplemental/Courier New.ttf"
            ),
            "StudyMono-Bold": Path(
                "/System/Library/Fonts/Supplemental/Courier New Bold.ttf"
            ),
        },
        {
            "StudySans": Path(
                "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
            ),
            "StudySans-Bold": Path(
                "/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf"
            ),
            "StudySans-Italic": Path(
                "/usr/share/fonts/truetype/msttcorefonts/Arial_Italic.ttf"
            ),
            "StudyMono": Path(
                "/usr/share/fonts/truetype/msttcorefonts/Courier_New.ttf"
            ),
            "StudyMono-Bold": Path(
                "/usr/share/fonts/truetype/msttcorefonts/Courier_New_Bold.ttf"
            ),
        },
        {
            "StudySans": Path(
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
            ),
            "StudySans-Bold": Path(
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
            ),
            "StudySans-Italic": Path(
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"
            ),
            "StudyMono": Path(
                "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
            ),
            "StudyMono-Bold": Path(
                "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
            ),
        },
    )
    fonts = next(
        (
            candidate
            for candidate in font_sets
            if all(path.exists() for path in candidate.values())
        ),
        None,
    )
    if fonts is None:
        searched = sorted(
            {str(path) for candidate in font_sets for path in candidate.values()}
        )
        raise SystemExit(
            "Required Unicode font set not found. Searched: "
            + ", ".join(searched)
        )
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
    # Protect inline-code contents before applying emphasis substitutions.
    # Otherwise operators/comment delimiters such as `*`, `*/`, and `<` can be
    # mistaken for Markdown or ReportLab markup after the <font> tag is added.
    code_spans: list[str] = []

    def stash_code(match: re.Match[str]) -> str:
        index = len(code_spans)
        code_spans.append(match.group(1))
        return f"@@CODE_SPAN_{index}@@"

    value = re.sub(r"`([^`]+)`", stash_code, value.strip())
    # The study notes use HTML-style breaks inside compact bilingual question
    # and answer blocks. Preserve them through XML escaping so ReportLab
    # renders an actual line break instead of the literal ``<br>`` text.
    value = re.sub(r"<br\s*/?>", "@@HTML_BREAK@@", value, flags=re.IGNORECASE)
    value = escape(value)
    def render_link(match: re.Match[str]) -> str:
        label, target = match.groups()
        # Internal contents links are actual PDF destinations. Relative files
        # remain visual references; their Markdown links remain available in
        # the editable source. Do not invent PDF destinations in other files.
        if target.startswith("#"):
            return f'<link href="{unquote(target)}" color="#087E8B"><u>{label}</u></link>'
        if target.startswith(("https://", "http://", "mailto:")):
            return f'<link href="{target}" color="#087E8B"><u>{label}</u></link>'
        return f'<font color="#087E8B"><u>{label}</u></font>'

    value = re.sub(r"\[([^]]+)]\(([^)]+)\)", render_link, value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    # Do not interpret comment delimiters such as /* and */ (often shown in
    # inline code) as emphasis markers.
    value = re.sub(
        r"(?<![*/`])\*([^*`]+)\*(?![*/`])",
        r"<i>\1</i>",
        value,
    )
    for index, code in enumerate(code_spans):
        value = value.replace(
            f"@@CODE_SPAN_{index}@@",
            f'<font name="StudyMono" color="#A23E48">{escape(code)}</font>',
        )
    value = value.replace("@@HTML_BREAK@@", "<br/>")
    return value


def paragraph_markup(lines: list[str]) -> str:
    parts: list[str] = []
    for line in lines:
        hard_break = line.endswith("  ") or line.endswith("\\")
        clean_line = line[:-1] if line.endswith("\\") else line.rstrip()
        parts.append(clean_line)
        if hard_break:
            parts.append("<br/>")
        else:
            parts.append(" ")
    # Markdown emphasis, inline code and links may span source lines. Parse
    # the complete paragraph, after preserving explicit Markdown line breaks.
    return inline_markup("".join(parts).strip())


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
            allowWidows=0,
            allowOrphans=0,
        ),
        "body_keep": ParagraphStyle(
            "StudyBodyKeep",
            parent=base["BodyText"],
            fontName="StudySans",
            fontSize=10.2,
            leading=15,
            textColor=INK,
            spaceAfter=7,
            keepWithNext=True,
            allowWidows=0,
            allowOrphans=0,
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
        "h4": ParagraphStyle(
            "StudyH4",
            parent=base["Heading4"],
            fontName="StudySans-Bold",
            fontSize=10.4,
            leading=13,
            textColor=TEAL,
            borderColor=LINE,
            borderWidth=0,
            borderPadding=(2, 0, 2, 0),
            spaceBefore=8,
            spaceAfter=5,
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
        PageBreak(),
    ]


def make_callout(lines: list[str], styles: dict[str, ParagraphStyle]):
    # GitHub-style admonitions are already visually rendered as callout cards in
    # this PDF theme.  Suppress the raw ``[!IMPORTANT]``/``[!NOTE]`` marker while
    # preserving any heading text that follows it on the same line.
    if lines:
        admonition = re.match(
            r"^\[!(?:IMPORTANT|WARNING|NOTE|TIP|CAUTION)\]\s*(.*)$",
            lines[0],
            re.IGNORECASE,
        )
        if admonition:
            remainder = admonition.group(1).strip()
            lines = ([remainder] if remainder else []) + lines[1:]
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


def split_table_row(line: str) -> list[str]:
    """Split a Markdown table row without treating code-span pipes as columns."""
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|") and not body.endswith(r"\|"):
        body = body[:-1]

    cells: list[str] = []
    cell: list[str] = []
    in_code = False
    escaped = False
    for char in body:
        if escaped:
            cell.append(char)
            escaped = False
            continue
        if char == "\\":
            escaped = True
            cell.append(char)
            continue
        if char == "`":
            in_code = not in_code
            cell.append(char)
            continue
        if char == "|" and not in_code:
            cells.append("".join(cell).strip())
            cell.clear()
            continue
        cell.append(char)
    cells.append("".join(cell).strip())
    return cells


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
            rows.append(split_table_row(lines[index]))
        index += 1
    return rows, index


def structured_quote_to_story(
    lines: list[str], styles: dict[str, ParagraphStyle]
):
    """Render code/tables nested inside a blockquote as real flowables.

    The bilingual source sometimes keeps a figure or table and both language
    captions inside one Markdown blockquote. Flattening that whole block into a
    Paragraph destroys diagram whitespace and displays table pipes literally.
    Split only these structured quotes into caption cards plus native code/table
    flowables; ordinary bilingual paragraph pairs remain a single callout card.
    """

    story = []
    prose: list[str] = []

    def flush_prose() -> None:
        while prose and not prose[-1].strip():
            prose.pop()
        if prose:
            story.extend([make_callout(prose.copy(), styles), Spacer(1, 3 * mm)])
            prose.clear()

    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            flush_prose()
            index += 1
            code: list[str] = []
            while index < len(lines) and not lines[index].startswith("```"):
                code.append(lines[index])
                index += 1
            story.extend([make_code(code, styles), Spacer(1, 3 * mm)])
            if index < len(lines):
                index += 1
            continue

        table_result = parse_table(lines, index)
        if table_result:
            flush_prose()
            rows, index = table_result
            story.extend([make_table(rows, styles), Spacer(1, 3 * mm)])
            continue

        # ``\`` is inserted between English and Turkish prose in an ordinary
        # bilingual card.  Once a structured element separates the captions,
        # it is just a segment boundary and should not render visibly.
        if line == "\\":
            flush_prose()
        elif not line.strip():
            flush_prose()
        else:
            prose.append(line)
        index += 1

    flush_prose()
    return story


def markdown_to_story(markdown: str, styles: dict[str, ParagraphStyle]):
    lines = markdown.splitlines()
    story = []
    paragraph_lines: list[str] = []
    list_items: list[str] = []
    list_ordered = False
    heading_counts: dict[str, int] = {}

    def flush_paragraph() -> None:
        if paragraph_lines:
            follows_heading = (
                story
                and isinstance(story[-1], Paragraph)
                and story[-1].style.name in {"StudyH2", "StudyH3", "StudyH4"}
            )
            is_translated_heading = paragraph_lines[0].startswith(
                "**Türkçe başlık:**"
            )
            style = (
                styles["body_keep"]
                if follows_heading and is_translated_heading
                else styles["body"]
            )
            story.append(Paragraph(paragraph_markup(paragraph_lines), style))
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
        heading_chain = []
        while (
            story
            and isinstance(story[-1], Paragraph)
            and story[-1].style.name
            in {"StudyH2", "StudyH3", "StudyH4", "StudyBodyKeep"}
        ):
            heading_chain.insert(0, story.pop())
        if heading_chain:
            # Keep a section heading (and, when present, its translated
            # heading) with the first list that gives the section meaning.
            # This also handles H2 alphabet bands followed by an H3 word card.
            story.append(KeepTogether([*heading_chain, list_flowable]))
        else:
            story.append(list_flowable)
        list_items.clear()
        list_ordered = False

    index = 0
    seen_title = False
    while index < len(lines):
        line = lines[index]

        if line.strip() == "<!-- page-break -->":
            flush_paragraph()
            flush_list()
            story.append(PageBreak())
            index += 1
            continue

        if line.lstrip().startswith("<!--"):
            flush_paragraph()
            flush_list()
            while index < len(lines):
                finished = "-->" in lines[index]
                index += 1
                if finished:
                    break
            continue

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
            bilingual_pair = lines[index].startswith("> **English:**")
            seen_turkish = False
            while index < len(lines) and lines[index].startswith(">"):
                quote_line = lines[index][1:].lstrip()
                # A note/link card and a following bilingual paragraph are
                # separate semantic blocks even if an unquoted blank line was
                # accidentally omitted in the Markdown source.
                if (
                    not bilingual_pair
                    and quote
                    and quote_line.startswith("**English:**")
                ):
                    break
                # Some generated bilingual Markdown keeps consecutive paragraph
                # pairs inside one continuous blockquote.  Stop before the next
                # English label once this pair's Turkish block has been read so
                # each source paragraph and translation gets its own card.
                if (
                    bilingual_pair
                    and seen_turkish
                    and quote_line.startswith("**English:**")
                ):
                    break
                if bilingual_pair and quote_line.startswith("**Türkçe:**"):
                    while quote and not quote[-1].strip():
                        quote.pop()
                    if quote and quote[-1] != "\\":
                        quote.append("\\")
                quote.append(quote_line)
                if quote_line.startswith("**Türkçe:**"):
                    seen_turkish = True
                index += 1
            # In bilingual notes, keep the immediately following Turkish block
            # in the same card so the source paragraph and its translation do
            # not become detached across pages.
            if (
                bilingual_pair
                and not seen_turkish
                and index + 1 < len(lines)
                and not lines[index].strip()
                and lines[index + 1].startswith("> **Türkçe")
            ):
                index += 1
                quote.append("\\")
                while index < len(lines) and lines[index].startswith(">"):
                    quote_line = lines[index][1:].lstrip()
                    if quote_line.startswith("**English:**"):
                        break
                    quote.append(quote_line)
                    index += 1
            has_structured_content = any(
                item.startswith("```") or item.lstrip().startswith("|")
                for item in quote
            )
            follows_heading = (
                story
                and isinstance(story[-1], Paragraph)
                and story[-1].style.name in {"StudyH2", "StudyH3", "StudyH4"}
            )
            is_translated_heading = (
                len(quote) == 1
                and quote[0].startswith("**Türkçe başlık:**")
            )
            if follows_heading and is_translated_heading:
                # Treat a translated heading as part of the heading hierarchy,
                # not as a standalone callout.  The keep chain also carries the
                # first explanatory block to the same page.
                story.append(
                    Paragraph(paragraph_markup(quote), styles["body_keep"])
                )
            elif has_structured_content:
                story.extend(structured_quote_to_story(quote, styles))
            else:
                story.extend([make_callout(quote, styles), Spacer(1, 3 * mm)])
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            flush_list()
            level = len(heading.group(1))
            title = heading.group(2)
            slug = heading_slug(title)
            duplicate = heading_counts.get(slug, 0)
            heading_counts[slug] = duplicate + 1
            anchor = slug if duplicate == 0 else f"{slug}-{duplicate}"
            if level == 1 and not seen_title:
                story.extend(make_cover(title, styles))
                seen_title = True
            else:
                paragraph = Paragraph(
                    f'<a name="{anchor}"/>' + inline_markup(title),
                    styles[f"h{min(level, 4)}"],
                )
                paragraph.study_heading = (level, title, anchor)
                story.append(paragraph)
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
    # A trailing layout spacer can overflow onto a header/footer-only page when
    # the final card exactly fills the preceding frame.
    while story and isinstance(story[-1], Spacer):
        story.pop()
    return keep_exercises_together(story)


def keep_exercises_together(story):
    """Keep short exercises and their separate answer explanations intact.

    KeepTogether still permits a genuinely long exercise to span pages. Explicit
    answer-section page breaks retain their role of hiding answers from view.
    """
    output = []
    group = []
    in_answers = False

    def flush():
        if group:
            output.append(KeepTogether(group.copy()))
            group.clear()

    for item in story:
        heading = getattr(item, "study_heading", None)
        if isinstance(item, PageBreak):
            flush()
            output.append(item)
            continue
        if heading:
            level, title, _ = heading
            if level <= 3:
                flush()
            if level == 2:
                in_answers = bool(re.match(r"Cevap|Answers", title, re.IGNORECASE))
            if level == 3 and (
                re.match(r"Official Answer\s+\d+", title)
                or re.fullmatch(r"Soru\s+\d+", title)
                or (in_answers and re.match(r"(?:Soru\s+)?\d+\b", title))
            ):
                group.append(item)
                continue
        if group:
            group.append(item)
        else:
            output.append(item)
    flush()
    return output


class StudyDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, title: str, unit_label: str):
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
        self.unit_label = unit_label
        self.outline_levels: list[int] = []
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="study-frame",
        )
        self.addPageTemplates(PageTemplate(id="study", frames=[frame], onPage=self.decorate_page))

    def afterFlowable(self, flowable) -> None:
        heading = getattr(flowable, "study_heading", None)
        if heading is None:
            return
        level, title, anchor = heading
        # Source-page labels preserve traceability in the body, but the PDF
        # sidebar should help the reader find topics, exercises and answers.
        if re.match(r"(?:Kaynak PDF sayfası|Source page)\s+\d+", title):
            self.outline_levels.clear()
            return
        while self.outline_levels and self.outline_levels[-1] >= level:
            self.outline_levels.pop()
        self.canv.addOutlineEntry(
            re.sub(r"[*`]", "", title), anchor,
            level=len(self.outline_levels), closed=True,
        )
        self.outline_levels.append(level)

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
        canvas.drawString(22 * mm, height - 10 * mm, self.unit_label)

        canvas.setFont("StudySans", 7.5)
        canvas.setFillColor(MUTED)
        short_title = compact_running_title(self.study_title)
        left_edge = 22 * mm + canvas.stringWidth(
            self.unit_label, "StudySans-Bold", 7.5
        ) + 8 * mm
        right_edge = width - 23 * mm
        available_width = max(0, right_edge - left_edge)
        while (
            len(short_title) > 4
            and canvas.stringWidth(short_title, "StudySans", 7.5)
            > available_width
        ):
            short_title = short_title[:-4].rstrip(". ") + "..."
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
    unit_match = re.match(r"Unit\s+(\d+)\s*·\s*([^·]+)", title, re.IGNORECASE)
    unit_label = (
        f"UNIT {unit_match.group(1)} · {unit_match.group(2).strip().upper()}"
        if unit_match
        else "JAVA 17 OCP · YDS"
    )
    document = StudyDocTemplate(str(args.output), title, unit_label)
    document.build(markdown_to_story(markdown, build_styles()))
    print(f"Generated {args.output}")


if __name__ == "__main__":
    main()
