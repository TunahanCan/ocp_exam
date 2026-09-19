#!/usr/bin/env python3
"""Build illustrated, bilingual study PDFs from their editable Markdown sources.

Usage (from the repository root)::

    python3 microservice-lecture/tools/generate_study_pdf.py \
        microservice-lecture/units/unit_01/bilingual_notes.md
    python3 microservice-lecture/tools/generate_study_pdf.py \
        microservice-lecture/units/unit_01/{bilingual_notes,vocabulary,grammar_notes}.md

Each input produces a sibling PDF with the same stem. ``--output PATH`` may be
used with one input. No dependency is installed by this script: it uses an
available ReportLab installation, including an existing uv package cache.

Markdown conventions:

* Start with one ``# Ünite 01 · ...`` title. H2/H3 headings become PDF bookmarks;
  a linked contents section is added if the source does not already contain one.
* Put each English/Turkish paragraph pair in one blockquote, or in two ordinary
  paragraphs labelled ``**English:**`` and ``**Türkçe:**``.
* Put ``![Şekil 1.1](assets/figure_01_01.png)`` on its own line. An immediately
  following labelled English/Turkish pair is its caption. Both remain together
  with the figure. Paths are relative to the Markdown file; images are embedded
  without changing their contents or aspect ratio.
* ``<!-- page-break -->`` and ``<!-- keep-with-next -->`` are supported, as are
  fenced code, simple Markdown tables, lists and inline links/emphasis.

The shared OCP renderer supplies typography and Markdown primitives read-only;
all microservices-specific changes are confined to this module.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


def load_existing_reportlab() -> None:
    if importlib.util.find_spec("reportlab") is not None:
        return
    cache = Path.home() / ".cache/uv/archive-v0"
    for package in sorted(cache.glob("*/reportlab/__init__.py")):
        sys.path.insert(0, str(package.parent.parent))
        return
    raise SystemExit(
        "ReportLab bulunamadı. Mevcut ReportLab ortamının Python yorumlayıcısını "
        "kullanın veya paket dizinini PYTHONPATH ile belirtin."
    )


load_existing_reportlab()

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)


THEME_PATH = (
    Path(__file__).resolve().parents[2]
    / "exam_lecture/tools/generate_study_pdf.py"
)
spec = importlib.util.spec_from_file_location("microservices_shared_theme", THEME_PATH)
if spec is None or spec.loader is None:
    raise SystemExit(f"Ortak PDF tasarımı yüklenemedi: {THEME_PATH}")
theme = importlib.util.module_from_spec(spec)
spec.loader.exec_module(theme)

WIDTH = 165 * mm
HEIGHT = A4[1] - 39 * mm
IMAGE_LINE = re.compile(r"^\s*(?:>\s*)?!\[([^\]]*)\]\((.+)\)\s*$")
CONTENTS_HEADING = re.compile(
    r"^##\s+(?:İçindekiler|Icindekiler|Contents|Table of Contents)\s*$",
    re.MULTILINE | re.IGNORECASE,
)
ORIGINAL_CALLOUT = theme.make_callout
ORIGINAL_TABLE = theme.make_table


def make_code(code, styles):
    """Allow long listings to continue across pages without reducing font size.

    Only the PDF view wraps long physical lines. The source Markdown retains
    the exact extracted code; a continuation arrow makes visual wrapping clear.
    """
    from reportlab.pdfbase.pdfmetrics import stringWidth
    style = styles['code']
    available = WIDTH - 18
    rows = []
    for original in code:
        remaining = original.expandtabs(4)
        first = True
        while remaining:
            # The bundled monospace fonts do not all contain U+21AA.
            prefix = '' if first else '-> '
            length = len(remaining)
            while length > 1 and stringWidth(prefix + remaining[:length], style.fontName, style.fontSize) > available:
                length -= 1
            # Prefer a space, while retaining every character and keeping
            # deeply indented lines from creating many tiny fragments.
            if length < len(remaining):
                boundary = remaining.rfind(' ', max(0,length//2), length)
                if boundary > 0:
                    length = boundary + 1
            rows.append([Preformatted(prefix + remaining[:length], style)])
            remaining = remaining[length:]
            first = False
        if not original:
            rows.append([Preformatted(' ', style)])
    if not rows:
        rows = [[Preformatted(' ', style)]]
    table = Table(rows, colWidths=[WIDTH], hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#1E2933')),
        ('BOX',(0,0),(-1,-1),0.6,colors.HexColor('#405363')),
        ('LEFTPADDING',(0,0),(-1,-1),9),
        ('RIGHTPADDING',(0,0),(-1,-1),9),
        ('TOPPADDING',(0,0),(-1,-1),1),
        ('BOTTOMPADDING',(0,0),(-1,-1),1),
        ('TOPPADDING',(0,0),(-1,0),7),
        ('BOTTOMPADDING',(0,-1),(-1,-1),7),
    ]))
    # A two-line condition or a short SQL statement is one reading unit.
    # Longer listings retain their normal row-by-row page splitting.
    return KeepTogether([table]) if len(rows) <= 10 else table


def make_table(rows, styles):
    table = ORIGINAL_TABLE(rows, styles)
    table.splitInRow = 1
    return table


@dataclass
class Figure:
    path: Path
    alt: str
    caption: list[str]


def normalize_language_paragraphs(markdown: str) -> str:
    """Give ordinary labelled language paragraphs the shared card formatting."""
    output: list[str] = []
    language_paragraph = False
    in_code = False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            language_paragraph = False
        if not in_code and theme.quote_language(line) and not line.startswith(">"):
            language_paragraph = True
        elif not line.strip() or line.startswith(("#", ">", "!", "<!--")):
            language_paragraph = False
        output.append("> " + line if language_paragraph else line)
    return "\n".join(output)


def add_contents(markdown: str) -> str:
    if CONTENTS_HEADING.search(markdown):
        return markdown
    headings: list[str] = []
    in_code = False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        match = re.match(r"^##\s+(.+)$", line)
        if match and not in_code:
            headings.append(match.group(1))
    if not headings:
        return markdown
    counts: dict[str, int] = {}
    links: list[str] = []
    for title in headings:
        slug = theme.heading_slug(title)
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchor = slug if count == 0 else f"{slug}-{count}"
        links.append(f"- [{title}](#{anchor})")
    contents = "\n\n## İçindekiler\n\n" + "\n".join(links) + "\n\n"
    title_match = re.search(r"^#\s+.+$", markdown, re.MULTILINE)
    assert title_match is not None
    return markdown[: title_match.end()] + contents + markdown[title_match.end() :]


def extract_figures(markdown: str, source: Path) -> tuple[str, dict[str, Figure]]:
    """Replace local images with card placeholders understood by the theme."""
    lines = markdown.splitlines()
    output: list[str] = []
    figures: dict[str, Figure] = {}
    index = 0
    in_code = False
    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            in_code = not in_code
        match = IMAGE_LINE.match(line) if not in_code else None
        if match is None:
            output.append(line)
            index += 1
            continue
        alt, target = match.groups()
        # Optional Markdown image titles do not form part of the file path.
        target = re.sub(r'\s+"[^\"]*"\s*$', "", target).strip().strip("<>")
        if re.match(r"^[a-z][a-z0-9+.-]*://", target, re.IGNORECASE):
            raise ValueError(f"Görsel önce yerel dosyaya kaydedilmeli: {target}")
        path = (source.parent / unquote(target)).resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Görsel bulunamadı: {path}")
        index += 1
        next_content = index
        while next_content < len(lines) and not lines[next_content].strip():
            next_content += 1
        caption: list[str] = []
        if (
            next_content < len(lines)
            and lines[next_content].startswith(">")
            and theme.quote_language(lines[next_content]) == "English"
        ):
            index = next_content
            seen_turkish = False
            while index < len(lines):
                caption_line = lines[index]
                if not caption_line.strip():
                    following = index + 1
                    while following < len(lines) and not lines[following].strip():
                        following += 1
                    if (
                        not seen_turkish
                        and following < len(lines)
                        and theme.quote_language(lines[following]) == "Türkçe"
                    ):
                        index = following
                        continue
                    break
                if not caption_line.startswith(">"):
                    break
                content = caption_line[1:].lstrip()
                language = theme.quote_language(content)
                if seen_turkish and language == "English":
                    break
                if IMAGE_LINE.match(caption_line):
                    break
                caption.append(content)
                seen_turkish = seen_turkish or language == "Türkçe"
                index += 1
        token = f"@@MICROSERVICE_FIGURE_{len(figures):04d}@@"
        figures[token] = Figure(path=path, alt=alt, caption=caption)
        output.extend(["", "> " + token, ""])
    return "\n".join(output), figures


def long_language_card(label: str, lines: list[str], styles, english: bool):
    """Repeat the language and pair number when a long paragraph spans pages."""
    color = theme.NAVY if english else theme.TEAL
    background = colors.HexColor("#EDF2FA") if english else theme.MINT
    label_style = ParagraphStyle(
        "ContinuationLabel", parent=styles["callout"],
        fontName="StudySans-Bold", fontSize=8.5, leading=11, textColor=color,
    )
    body = re.sub(r"^\*\*(?:English|Türkçe)[^*]*:\*\*\s*", "", " ".join(lines))
    table = Table(
        [[Paragraph(theme.inline_markup(label), label_style)],
         [Paragraph(theme.inline_markup(body), styles["callout"])]],
        colWidths=[WIDTH], repeatRows=1, splitByRow=1, splitInRow=1,
    )
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("LINEBEFORE", (0, 0), (-1, -1), 3, color),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return table


def make_figure(figure: Figure, styles):
    picture = Image(str(figure.path), lazy=2)
    if figure.caption:
        caption = ORIGINAL_CALLOUT(figure.caption.copy(), styles)
    else:
        caption = Paragraph(theme.inline_markup(figure.alt), styles["source_page"])
    _, caption_height = caption.wrap(WIDTH, HEIGHT)
    max_picture_height = HEIGHT - caption_height - 28 * mm
    if max_picture_height < 35 * mm:
        raise ValueError(f"Şekil açıklaması çok uzun; ayrı paragraf kullanın: {figure.path}")
    scale = min(WIDTH / picture.imageWidth, max_picture_height / picture.imageHeight)
    picture.drawWidth = picture.imageWidth * scale
    picture.drawHeight = picture.imageHeight * scale
    picture.hAlign = "CENTER"
    return KeepTogether([picture, Spacer(1, 3 * mm), caption])


def make_cover(title, styles):
    banner = Table(
        [[Paragraph(theme.inline_markup(title), styles["cover_title"])]],
        colWidths=[WIDTH],
    )
    banner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), theme.NAVY),
        ("BOX", (0, 0), (-1, -1), 1.2, theme.TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), 12 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 16 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 16 * mm),
    ]))
    return [
        Spacer(1, 10 * mm),
        Paragraph("MICROSERVICES · TEKNİK İNGİLİZCE · YDS", styles["cover_tag"]),
        banner,
        Spacer(1, 7 * mm),
        Paragraph(
            "Ünite bazlı çalışma kaynağı<br/>"
            "Kaynak sırasını izle · İngilizce ve Türkçeyi karşılaştır · görsellerle tekrar et",
            styles["cover_sub"],
        ),
        PageBreak(),
    ]


class MicroservicesDoc(theme.StudyDocTemplate):
    def __init__(self, filename: str, title: str, unit_label: str):
        BaseDocTemplate.__init__(
            self, filename, pagesize=A4,
            leftMargin=22 * mm, rightMargin=23 * mm,
            topMargin=20 * mm, bottomMargin=19 * mm,
            title=title, author="Microservices · Teknik İngilizce ve YDS Çalışması",
        )
        self.study_title = title
        self.unit_label = unit_label
        self.outline_levels = []
        frame = Frame(
            self.leftMargin, self.bottomMargin, self.width, self.height,
            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
            id="microservices-frame",
        )
        self.addPageTemplates(PageTemplate(
            id="microservices", frames=[frame], onPage=self.decorate_page,
        ))

    def decorate_page(self, canvas, doc):
        canvas.saveState()
        width, height = A4
        canvas.setFillColor(theme.PAPER)
        canvas.rect(0, 0, width, height, stroke=0, fill=1)
        canvas.setStrokeColor(theme.LINE)
        canvas.setLineWidth(0.5)
        canvas.line(22 * mm, height - 13 * mm, width - 23 * mm, height - 13 * mm)
        canvas.line(22 * mm, 12 * mm, width - 23 * mm, 12 * mm)
        canvas.setFont("StudySans-Bold", 7.5)
        canvas.setFillColor(theme.TEAL)
        canvas.drawString(22 * mm, height - 10 * mm, self.unit_label)
        canvas.setFont("StudySans", 7.5)
        canvas.setFillColor(theme.MUTED)
        short_title = theme.compact_running_title(self.study_title)
        available_width = WIDTH - canvas.stringWidth(self.unit_label, "StudySans-Bold", 7.5) - 8 * mm
        while len(short_title) > 4 and canvas.stringWidth(short_title, "StudySans", 7.5) > available_width:
            short_title = short_title[:-4].rstrip(". ") + "..."
        canvas.drawRightString(width - 23 * mm, height - 10 * mm, short_title)
        canvas.drawString(22 * mm, 8 * mm, "Microservices · Teknik İngilizce + YDS")
        canvas.drawRightString(width - 23 * mm, 8 * mm, str(doc.page))
        canvas.restoreState()


def render(source: Path, output: Path | None = None) -> Path:
    markdown = source.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    if title_match is None:
        raise ValueError(f"Markdown dosyasında # düzeyinde bir başlık olmalı: {source}")
    title = title_match.group(1).strip()
    markdown = add_contents(normalize_language_paragraphs(markdown))
    markdown, figures = extract_figures(markdown, source)
    styles = theme.build_styles()
    pair_number = 0

    def make_callout(lines, card_styles):
        nonlocal pair_number
        token = " ".join(line.strip() for line in lines).strip()
        if token in figures:
            return make_figure(figures[token], card_styles)
        card = ORIGINAL_CALLOUT(lines.copy(), card_styles)
        if lines and theme.quote_language(lines[0]) == "English":
            pair_number += 1
            boundary = next((i for i, line in enumerate(lines) if theme.quote_language(line) == "Türkçe"), None)
            if boundary is not None and card.wrap(WIDTH, HEIGHT)[1] > HEIGHT - 12 * mm:
                english = [line for line in lines[:boundary] if line.strip() not in {"", "\\"}]
                turkish = lines[boundary:]
                reference = f"Paragraf {pair_number:03d}"
                return KeepTogether([
                    long_language_card(f"English · {reference}", english, card_styles, True),
                    long_language_card(f"Türkçe · {reference}", turkish, card_styles, False),
                ], maxHeight=HEIGHT)
        return card

    theme.make_cover = make_cover
    theme.make_callout = make_callout
    theme.make_code = make_code
    theme.make_table = make_table
    unit = re.search(r"(?:Unit|Ünite|Unite)\s+(\d+)", title, re.IGNORECASE)
    unit_label = f"ÜNİTE {unit.group(1)} · MICROSERVICES" if unit else "MICROSERVICES · YDS"
    output = output or source.with_suffix(".pdf")
    output.parent.mkdir(parents=True, exist_ok=True)
    document = MicroservicesDoc(str(output), title, unit_label)
    story = theme.markdown_to_story(markdown, styles)
    # A standalone annotation label must travel with its bilingual explanation.
    for index, flowable in enumerate(story):
        if isinstance(flowable, Paragraph) and flowable.getPlainText().strip() == "Kod açıklaması:":
            flowable.keepWithNext = True
            for following in story[index + 1:]:
                if not isinstance(following, Spacer):
                    break
                following.keepWithNext = True
    if source.stem in {"vocabulary", "grammar_notes"}:
        story = keep_study_topics_together(story, source.stem)
    document.build(story)
    print(f"Generated {output} ({document.page} pages, {len(figures)} figures)")
    return output


def keep_study_topics_together(story, document_kind):
    """Keep short study cards whole; oversized topics may still split normally.

    Operate on the rendered flowables so Markdown remains the only content
    source. KeepTogether releases its children when a group cannot fit a page;
    headings and their PDF destinations remain ordinary child flowables.
    """
    result, pending = [], []
    level = 3 if document_kind == "vocabulary" else 2

    def flush():
        if pending:
            result.append(KeepTogether(pending.copy()))
            pending.clear()

    for item in story:
        heading = getattr(item, "study_heading", None)
        if heading and heading[0] <= level:
            flush()
            title = heading[1]
            is_topic = heading[0] == level and title.casefold() not in {
                "içindekiler", "contents", "table of contents"
            }
            if is_topic:
                if document_kind == "vocabulary" and result:
                    previous_heading = getattr(result[-1], "study_heading", None)
                    if previous_heading and previous_heading[0] == 2:
                        pending.append(result.pop())
                pending.append(item)
            else:
                result.append(item)
        elif isinstance(item, PageBreak):
            flush()
            result.append(item)
        elif pending:
            pending.append(item)
        else:
            result.append(item)
    flush()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", type=Path, nargs="+", help="Bir veya daha fazla Markdown kaynak dosyası")
    parser.add_argument("--output", type=Path, help="Tek girdi için isteğe bağlı PDF çıktı yolu")
    args = parser.parse_args()
    if args.output is not None and len(args.input) != 1:
        parser.error("--output yalnızca tek Markdown dosyasıyla kullanılabilir")
    theme.register_fonts()
    for source in args.input:
        render(source.resolve(), args.output)


if __name__ == "__main__":
    main()
