#!/usr/bin/env python3
"""Build a paragraph-paired bilingual draft from page-layout extractions.

The input directory can be produced by ``extract_pdf_pages.swift`` or an
equivalent extractor that writes the same JSON schema. Translation is performed
locally with Argos, or deferred with ``--translation-mode placeholder`` for a
later neural translation pass. Java source, output, API identifiers, and a
protected OCP glossary are kept unchanged.
"""

from __future__ import annotations

import argparse
import json
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path


TRANSLATION_MODE = "argos"


UNIT_TOPICS = {
    10: [
        "Returning an Optional",
        "Using Streams",
        "Using Common Terminal Operations",
        "Using Common Intermediate Operations",
        "Working with Primitive Streams",
        "Working with Advanced Stream Pipeline Concepts",
        "Summary",
        "Exam Essentials",
        "Review Questions",
    ],
    11: [
        "Understanding Exceptions",
        "Recognizing Exception Classes",
        "Handling Exceptions",
        "Automating Resource Management",
        "Formatting Values",
        "Supporting Internationalization and Localization",
        "Summary",
        "Exam Essentials",
        "Review Questions",
    ],
    12: [
        "Introducing Modules",
        "Creating and Running a Modular Program",
        "Updating Our Example for Multiple Modules",
        "Diving into the Module Declaration",
        "Creating a Service",
        "Discovering Modules",
        "Comparing Types of Modules",
        "Migrating an Application",
        "Summary",
        "Exam Essentials",
        "Review Questions",
    ],
    13: [
        "Introducing Threads",
        "Creating Threads with the Concurrency API",
        "Writing Thread-Safe Code",
        "Using Concurrent Collections",
        "Identifying Threading Problems",
        "Working with Parallel Streams",
        "Summary",
        "Exam Essentials",
        "Review Questions",
    ],
}

PROTECTED_TERMS = [
    # Java 9+ module-system syntax and command-line vocabulary. These tokens
    # must survive translation exactly; changing even one hyphen can alter the
    # answer to an OCP command/syntax question.
    "requires transitive",
    "open module",
    "module-info.class",
    "module-info.java",
    "ServiceLoader.Provider",
    "runtime image",
    "module graph",
    "module descriptor",
    "module declaration",
    "module directive",
    "module name",
    "module path",
    "classpath",
    "named module",
    "automatic module",
    "unnamed module",
    "service provider interface",
    "service provider",
    "service locator",
    "qualified export",
    "transitive dependency",
    "strong encapsulation",
    "reflection",
    "migration",
    "directive",
    "requires",
    "exports",
    "opens",
    "provides",
    "uses",
    # Concurrency vocabulary is intentionally retained in English, matching
    # the Java API and the terminology candidates see on the exam.
    "platform thread",
    "daemon thread",
    "worker thread",
    "thread pool",
    "thread state",
    "thread lifecycle",
    "thread scheduler",
    "context switch",
    "shared mutable state",
    "lost update",
    "intrinsic monitor",
    "mutual exclusion",
    "visibility",
    "atomicity",
    "synchronization",
    "public",
    "private",
    "protected",
    "static",
    "abstract",
    "synchronized",
    "volatile",
    "ScheduledExecutorService",
    "ConcurrentModificationException",
    "IllegalMonitorStateException",
    "ConcurrentSkipListMap",
    "ConcurrentSkipListSet",
    "ConcurrentLinkedQueue",
    "CopyOnWriteArrayList",
    "CopyOnWriteArraySet",
    "LinkedBlockingQueue",
    "ConcurrentHashMap",
    "AtomicBoolean",
    "AtomicInteger",
    "AtomicLong",
    "ExecutorService",
    "ExecutionException",
    "TimeoutException",
    "BrokenBarrierException",
    "InterruptedException",
    "ReentrantLock",
    "CyclicBarrier",
    "ForkJoinPool",
    "ServiceLoader",
    "Automatic-Module-Name",
    "Runnable",
    "Callable",
    "Executors",
    "Future",
    "TimeUnit",
    "Thread",
    "Lock",
    "jlink",
    "jdeps",
    "jmod",
    "OptionalDouble",
    "OptionalInt",
    "OptionalLong",
    "DoubleSummaryStatistics",
    "IntSummaryStatistics",
    "LongSummaryStatistics",
    "DateTimeFormatter",
    "DecimalFormat",
    "MessageFormat",
    "NumberFormat",
    "ResourceBundle",
    "AutoCloseable",
    "FileInputStream",
    "FileNotFoundException",
    "NoSuchElementException",
    "IllegalStateException",
    "IllegalArgumentException",
    "NullPointerException",
    "RuntimeException",
    "IOException",
    "SQLException",
    "ParseException",
    "DateTimeException",
    "MissingResourceException",
    "IntStream",
    "LongStream",
    "DoubleStream",
    "Spliterator",
    "Collectors",
    "Comparator",
    "Supplier",
    "Consumer",
    "Predicate",
    "Function",
    "BiFunction",
    "BinaryOperator",
    "BiConsumer",
    "Collection",
    "ArrayList",
    "TreeSet",
    "Optional",
    "Stream",
    "String",
    "Integer",
    "Boolean",
    "Throwable",
    "Properties",
    "Locale",
    "LocalDate",
    "List",
    "Set",
    "Map",
    "Java",
    "JVM",
    "OCP",
    "null",
    "void",
    "boolean",
    "byte",
    "short",
    "int",
    "long",
    "float",
    "double",
    "char",
    "var",
    "try/catch/finally",
    "try-with-resources statement",
    "try-with-resources",
    "resource bundle",
    "method reference",
    "functional interface",
    "primitive stream",
    "stream pipeline",
    "intermediate operation",
    "terminal operation",
    "stateful operation",
    "stateless operation",
    "short-circuiting operation",
    "checked exception",
    "unchecked exception",
    "suppressed exception",
    "primary exception",
    "multi-catch block",
    "catch block",
    "finally block",
    "try block",
    "handle or declare rule",
    "effectively final",
    "factory method",
    "method signature",
    "return type",
    "runtime exception",
    "date/time formatter",
    "default locale",
    "locale category",
    "properties file",
    "parallel stream",
    "sequential stream",
    "infinite stream",
    "finite stream",
    "race condition",
    "deadlock",
    "starvation",
    "livelock",
    "thread-safe",
    "memory consistency",
    "atomic operation",
    "critical section",
    "parallel decomposition",
    "stateful lambda",
    "module path",
    "classpath",
    "named module",
    "automatic module",
    "unnamed module",
    "service provider interface",
    "service provider",
    "service locator",
    "qualified export",
    "transitive dependency",
    "lazy evaluation",
    "reduction",
    "identity",
    "accumulator",
    "combiner",
    "collector",
    "partitioning",
    "grouping",
    "mapping",
    "flat mapping",
    "stream",
    "pipeline",
    "lambda",
]

@dataclass
class Line:
    text: str
    x: float
    y: float
    width: float
    height: float
    font: float


@dataclass
class Block:
    kind: str
    text: str
    level: int = 0


TITLE_PAGE_CONTENT = {
    10: [
        Block("heading", "Chapter 10 · Streams", 2),
        Block(
            "prose",
            "OCP exam objectives covered in this chapter: Working with Streams and "
            "Lambda expressions.",
        ),
        Block(
            "prose",
            "Use Java object and primitive Streams, including lambda expressions "
            "implementing functional interfaces, to supply, filter, map, consume, "
            "and sort data.",
        ),
        Block(
            "prose",
            "Perform decomposition, concatenation and reduction, and grouping and "
            "partitioning on sequential and parallel streams.",
        ),
    ],
    11: [
        Block("heading", "Chapter 11 · Exceptions and Localization", 2),
        Block(
            "prose",
            "OCP exam objectives covered in this chapter: Handling Exceptions and "
            "Implementing Localization.",
        ),
        Block(
            "prose",
            "Handle exceptions using try/catch/finally, try-with-resources, and "
            "multi-catch blocks, including custom exceptions.",
        ),
        Block(
            "prose",
            "Implement localization using locales, resource bundles, parse and "
            "format messages, dates, times, and numbers including currency and "
            "percentage values.",
        ),
    ],
    12: [
        Block("heading", "Chapter 12 · Modules", 2),
        Block(
            "prose",
            "OCP exam objectives covered in this chapter: Packaging and "
            "deploying Java code and using the Java Platform Module System.",
        ),
        Block(
            "prose",
            "Define modules and their dependencies, and expose module content, "
            "including content used through reflection. Define services, "
            "producers, and consumers.",
        ),
        Block(
            "prose",
            "Compile Java code; produce modular and non-modular JARs and runtime "
            "images; and implement migration using unnamed and automatic modules.",
        ),
    ],
    13: [
        Block("heading", "Chapter 13 · Concurrency", 2),
        Block(
            "prose",
            "OCP exam objectives covered in this chapter: Managing concurrent "
            "code execution and working with Streams and lambda expressions.",
        ),
        Block(
            "prose",
            "Create worker threads with Runnable and Callable, and manage the "
            "thread life cycle using Executor services and the Concurrency API.",
        ),
        Block(
            "prose",
            "Develop thread-safe code using locking mechanisms and concurrent "
            "APIs, and process Java collections concurrently with parallel streams.",
        ),
        Block(
            "prose",
            "Perform decomposition, concatenation, reduction, grouping, and "
            "partitioning on sequential and parallel streams.",
        ),
    ],
}


def normalize_ocr(text: str) -> str:
    text = (
        text.replace("\u00ad", "")
        .replace("\u00a0", " ")
        .replace("\u2002", " ")
        .replace("\u2003", " ")
        .replace("‐", "-")
        .replace("‑", "-")
        .replace("–", "–")
        .replace("\t", " ")
    )
    text = re.sub(r"-\s+>", "->", text)
    text = re.sub(r"<\s+-", "<-", text)
    text = re.sub(r"(?<=\w)-\s+(?=\w)", "-", text)
    text = re.sub(r"\s+([,.;:?!])", r"\1", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def load_page(path: Path, page_number: int) -> list[Line]:
    raw = json.loads(
        (path / f"page-{page_number:04d}.layout.json").read_text(encoding="utf-8")
    )
    lines = [
        Line(
            text=normalize_ocr(item["text"]),
            x=float(item["x"]),
            y=float(item["y"]),
            width=float(item["width"]),
            height=float(item["height"]),
            font=float(item["dominantFontSize"]),
        )
        for item in raw
        if normalize_ocr(item["text"])
    ]
    # PDF extractors may report slightly different baselines for font runs on
    # the same visual line. Integer baseline grouping keeps page numbers,
    # question numbers, and answer text in their intended left-to-right order.
    lines.sort(key=lambda line: (-round(line.y / 2.0), line.x))

    merged: list[Line] = []
    for line in lines:
        if merged and abs(merged[-1].y - line.y) < 2.0:
            previous = merged[-1]
            gap = line.x - (previous.x + previous.width)
            if gap < 45:
                separator = ""
                if (
                    previous.text
                    and line.text
                    and not previous.text.endswith((" ", ".", "/", "(", "<", "["))
                    and not line.text.startswith((".", ",", ";", ":", ")", "]", ">"))
                    and gap > 1.5
                ):
                    separator = " "
                previous.text = normalize_ocr(previous.text + separator + line.text)
                previous.width = max(previous.width, line.x + line.width - previous.x)
                previous.font = max(previous.font, line.font)
                continue
        merged.append(line)
    return merged


def is_running_header(line: Line, page_number: int, chapter: int) -> bool:
    if line.y < 605:
        return False
    text = line.text
    patterns = [
        rf"^{page_number}\s+Chapter\s+{chapter}\b",
        rf"^Chapter\s+{chapter}\b.*\s{page_number}$",
        rf"^(?:Streams|Exceptions and Localization|Modules|Concurrency)\s+{page_number}$",
        rf"^Review Questions\s+{page_number}$",
        rf"^{page_number}\s+Appendix\b",
        rf"^Chapter\s+(?:10:\s+Streams|11:\s+Exceptions and Localization|12:\s+Modules|13:\s+Concurrency)\s+{page_number}$",
        rf"^.+\s+{page_number}$",
        rf"^{page_number}\s+.+$",
    ]
    return any(re.match(pattern, text) for pattern in patterns)


def looks_like_code(text: str, font: float) -> bool:
    stripped = re.sub(r"^\d+:\s*", "", text.strip())
    if not stripped:
        return False
    if font > 8.8:
        return False
    if re.match(r"^(?:java\.[\w.]+(?:Exception|Error)|Caused by:)", stripped):
        return True
    code_signals = (
        ";",
        "{",
        "}",
        "->",
        "::",
        "System.out",
        "Collectors.",
        "IntStream.",
        "LongStream.",
        "DoubleStream.",
        ".stream()",
        ".parallelStream()",
        " = ",
        "++",
        "--",
        "//",
    )
    if any(signal in stripped for signal in code_signals):
        return True
    if stripped in {
        "try",
        "else",
        "finally",
        "default:",
        "break;",
        "continue;",
        "{",
        "}",
    }:
        return True
    # A method name embedded in an explanatory sentence (for example,
    # "The isParallel() method returns ...") is prose, not source code.
    # Treat call-shaped text as code only when the line itself starts with a
    # call/expression and contains little or no surrounding prose.
    if re.match(
        r"^(?:(?:return|throw|new)\s+)?"
        r"(?:[A-Za-z_$][\w$]*\.)*[A-Za-z_$][\w$]*"
        r"\([^)]*\)(?:[.;,{)]|$)",
        stripped,
    ):
        return True
    return False


def join_text_lines(lines: list[Line]) -> str:
    output = ""
    for line in lines:
        text = line.text
        if not output:
            output = text
        elif output.endswith("-") and text[:1].islower():
            output = output[:-1] + text
        else:
            output += " " + text
    return normalize_ocr(output)


def page_to_blocks(
    lines: list[Line],
    page_number: int,
    chapter: int,
    *,
    appendix: bool = False,
) -> list[Block]:
    filtered = [
        line
        for line in lines
        if not is_running_header(line, page_number, chapter)
        and line.text not in {"■", "■ ■", "✓", "✓ ✓"}
    ]
    if not filtered:
        return []

    prose_x_values = [
        line.x
        for line in filtered
        if 8.9 <= line.font <= 10.1 and line.x < 160
    ]
    base_x = min(prose_x_values) if prose_x_values else 72.0
    blocks: list[Block] = []
    current: list[Line] = []
    current_kind = ""
    previous_y: float | None = None

    def flush() -> None:
        nonlocal current, current_kind
        if not current:
            return
        if current_kind == "code":
            code_lines = []
            for item in current:
                code_lines.append(re.sub(r"^\d+:\s?", "", item.text))
            blocks.append(Block("code", "\n".join(code_lines).rstrip()))
        else:
            blocks.append(Block("prose", join_text_lines(current)))
        current = []
        current_kind = ""

    for line in filtered:
        text = line.text
        if line.font >= 11.5 and not looks_like_code(text, line.font):
            flush()
            if line.font >= 19:
                level = 2
            elif line.font >= 13:
                level = 3
            else:
                level = 4
            blocks.append(Block("heading", text, level))
            previous_y = line.y
            continue

        code = looks_like_code(text, line.font)
        kind = "code" if code else "prose"
        y_gap = (previous_y - line.y) if previous_y is not None else 0
        starts_paragraph = (
            kind == "prose"
            and current_kind == "prose"
            and (
                line.x >= base_x + 8
                or y_gap > max(15.5, line.height + 4)
                or text.startswith(("FIGURE ", "TABLE ", "Note:", "Remember:"))
                or re.match(r"^(?:Summary|Exam Essentials|Review Questions)$", text)
            )
        )
        if current and (kind != current_kind or starts_paragraph):
            flush()

        if not current:
            current_kind = kind
        current.append(line)
        previous_y = line.y

    flush()

    # Merge fragments that PDFKit split inside the same prose sentence. The
    # source PDF occasionally changes font runs or indentation in the middle of
    # a sentence, so limiting this repair to short fragments loses context for
    # translation.
    repaired: list[Block] = []
    for block in blocks:
        if (
            repaired
            and block.kind == repaired[-1].kind == "prose"
            and not re.search(r"[.!?:)]$", repaired[-1].text)
            # A question or option may continue in the next PDF text block.
            # Only a *new* numbered/lettered block starts a fresh item.
            and not re.match(r"^[A-H]\.", block.text)
            and not re.match(r"^\d+\.", block.text)
        ):
            repaired[-1].text = normalize_ocr(repaired[-1].text + " " + block.text)
        else:
            repaired.append(block)
    return repaired


def protect_terms(text: str) -> tuple[str, dict[str, str]]:
    replacements: dict[str, str] = {}

    def stash(value: str) -> str:
        key = f"<x{len(replacements)}>"
        replacements[key] = value
        return key

    # Protect command-line flags, paths, archives, and module/class names
    # before ordinary prose. OCR often leaves commands inside a prose block,
    # so relying only on code-fence detection is not sufficient.
    syntax_pattern = re.compile(
        r"(?<![\w-])--[a-z][a-z0-9-]*"
        r"|(?<!\w)-[A-Za-z](?![\w-])"
        r"|(?<!\w)(?:[A-Za-z0-9_$.*-]+/)+[A-Za-z0-9_$.*-]+"
        r"|(?<!\w)[A-Za-z0-9_$.-]+\.(?:jar|jmod|java|class)\b"
    )
    text = syntax_pattern.sub(lambda match: stash(match.group(0)), text)

    # Protect Java-looking tokens and calls next.
    token_pattern = re.compile(
        r"\b(?:[a-zA-Z_$][\w$]*\.)+[a-zA-Z_$][\w$]*(?:\([^)]*\))?"
        r"|\b[a-zA-Z_$][\w$]*(?:<[^>\n]+>)?\([^)]*\)"
        r"|\b[a-zA-Z_$][\w$]*<[^>\n]+>"
        r"|\b[A-Z][A-Za-z0-9_$]*(?:Exception|Error)\b"
        r"|\b(?:Exception|Error)\b"
        r"|\b[a-z]+[A-Z][A-Za-z0-9_$]*\b"
        r"|\b[A-Z][A-Z0-9_]{2,}\b"
    )
    text = token_pattern.sub(lambda match: stash(match.group(0)), text)

    for term in sorted(PROTECTED_TERMS, key=len, reverse=True):
        pattern = re.compile(rf"\b{re.escape(term)}(?:s)?\b", re.IGNORECASE)
        text = pattern.sub(lambda match: stash(match.group(0)), text)

    return text, replacements


def translate_text(text: str, cache: dict[str, str]) -> str:
    if text in cache:
        return cache[text]
    if TRANSLATION_MODE == "placeholder":
        translated = "[Yerel çeviri kalite geçişinde doldurulacak.]"
        cache[text] = translated
        return translated
    try:
        import argostranslate.translate as argos_translate
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Argos Translate is required to build bilingual drafts. "
            "Install the English→Turkish model before running this command."
        ) from exc
    protected, replacements = protect_terms(text)
    translated = argos_translate.translate(protected, "en", "tr")
    for key, value in replacements.items():
        translated = translated.replace(key, value)
    translated = normalize_ocr(translated)
    translated = (
        translated.replace("Seçmeli", "Optional")
        .replace("seçmeli", "Optional")
        .replace("akış boru hattı", "stream pipeline")
        .replace("Akış boru hattı", "Stream pipeline")
        .replace("terminal operasyonu", "terminal operation")
        .replace("orta operasyon", "intermediate operation")
    )
    cache[text] = translated
    return translated


def quote_pair(english: str, turkish: str) -> str:
    english_lines = textwrap.wrap(
        english, width=88, break_long_words=False, break_on_hyphens=False
    ) or [""]
    turkish_lines = textwrap.wrap(
        turkish, width=88, break_long_words=False, break_on_hyphens=False
    ) or [""]
    output = [f"> **English:** {english_lines[0]}"]
    output.extend(f"> {line}" for line in english_lines[1:])
    output.append(">")
    output.append(f"> **Türkçe:** {turkish_lines[0]}")
    output.extend(f"> {line}" for line in turkish_lines[1:])
    return "\n".join(output)


def render_blocks(
    blocks: list[Block],
    cache: dict[str, str],
    *,
    official_answer_state: list[int] | None = None,
) -> list[str]:
    output: list[str] = []
    for block in blocks:
        text = block.text.strip()
        if not text:
            continue
        if official_answer_state is not None and block.kind == "prose":
            match = re.match(r"^(\d+)\.\s*", text)
            if match and int(match.group(1)) == official_answer_state[0]:
                output.append(f"### Official Answer {official_answer_state[0]}")
                official_answer_state[0] += 1
        if block.kind == "heading":
            clean_heading = re.sub(r"\s+\d+$", "", text)
            output.append(f"{'#' * block.level} {clean_heading}")
        elif block.kind == "code":
            code_lines = text.splitlines()
            for offset in range(0, len(code_lines), 42):
                code_chunk = "\n".join(code_lines[offset : offset + 42])
                output.append(f"```java\n{code_chunk}\n```")
        else:
            output.append(quote_pair(text, translate_text(text, cache)))
    return output


def appendix_blocks(
    source_directory: Path,
    chapter: int,
    start_page: int,
    end_page: int,
    start_heading: str,
    stop_heading: str | None,
) -> list[tuple[int, list[Block]]]:
    active = False
    pages: list[tuple[int, list[Block]]] = []
    for page_number in range(start_page, end_page + 1):
        blocks = page_to_blocks(
            load_page(source_directory, page_number),
            page_number,
            chapter,
            appendix=True,
        )
        selected: list[Block] = []
        for block in blocks:
            normalized = re.sub(r"\s+\d+$", "", block.text.strip())
            if not active and start_heading in normalized:
                active = True
                continue
            if active and stop_heading and stop_heading in normalized:
                active = False
                break
            if active:
                selected.append(block)
        if selected:
            pages.append((page_number, selected))
    return pages


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_directory", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--unit", type=int, required=True, choices=(10, 11, 12, 13))
    parser.add_argument("--title", required=True)
    parser.add_argument("--start-page", type=int, required=True)
    parser.add_argument("--end-page", type=int, required=True)
    parser.add_argument("--appendix-start-page", type=int, required=True)
    parser.add_argument("--appendix-end-page", type=int, required=True)
    parser.add_argument("--appendix-start-heading", required=True)
    parser.add_argument("--appendix-stop-heading")
    parser.add_argument("--official-count", type=int, required=True)
    parser.add_argument(
        "--translation-mode",
        choices=("argos", "placeholder"),
        default="argos",
        help=(
            "Use placeholder to build the source structure before a separate "
            "local retranslation quality pass."
        ),
    )
    args = parser.parse_args()

    global TRANSLATION_MODE
    TRANSLATION_MODE = args.translation_mode

    topics = UNIT_TOPICS[args.unit]
    front = [
        f"# Unit {args.unit:02d} · {args.title} · Bilingual Notes",
        "",
        "Bu ana kaynak, `OCP_Java_SE17_Chapter1den_Itibaren.pdf` içindeki ilgili",
        "chapter gövdesini ve Appendix resmî cevaplarını kaynak sırasını koruyan",
        "English → Türkçe paragraf çiftleriyle bir araya getirir. Kod ve terminal",
        "çıktıları çevrilmeden, bir kez ve kaynak konumunda gösterilir.",
        "",
        "[Vocabulary](vocabulary.md) · [Grammar notes](grammar_notes.md) ·",
        "[Teknik hafıza notu](technical_memory_notes.md)",
        "",
        "## Kaynak kapsam manifesti",
        "",
        "- Kaynak: `exam_lecture/OCP_Java_SE17_Chapter1den_Itibaren.pdf`",
        f"- Chapter: {args.unit} · {args.title}",
        f"- Chapter PDF sayfaları: {args.start_page}–{args.end_page}",
        (
            "- Appendix cevap sayfaları: "
            f"{args.appendix_start_page}–{args.appendix_end_page}"
        ),
        f"- Beklenen sayfa marker'ı: {args.end_page - args.start_page + 1}",
        f"- Beklenen resmî cevap: {args.official_count}",
        "- Eşleme biçimi: English paragraf → Türkçe çeviri → varsa kod",
        "",
        "## İçindekiler",
        "",
    ]
    front.extend(f"{index}. [{topic}](#{topic.lower().replace(' ', '-')})" for index, topic in enumerate(topics, 1))
    front.extend(
        [
            f"{len(topics) + 1}. [Official Review Question Answers / Resmî Cevaplar](#appendix--official-review-question-answers--resmî-cevaplar)",
            "",
            f"## Chapter {args.unit} · {args.title} · Eksiksiz çift dilli kaynak",
            "",
        ]
    )

    cache: dict[str, str] = {}
    body: list[str] = []
    total_pages = args.end_page - args.start_page + 1
    for index, page_number in enumerate(
        range(args.start_page, args.end_page + 1), start=1
    ):
        print(f"chapter page {index}/{total_pages}: {page_number}", flush=True)
        body.append(f"<!-- source-page: {page_number:04d} -->")
        blocks = (
            TITLE_PAGE_CONTENT[args.unit]
            if page_number == args.start_page
            else page_to_blocks(
                load_page(args.source_directory, page_number),
                page_number,
                args.unit,
            )
        )
        body.extend(render_blocks(blocks, cache))
        body.append("")

    appendix = [
        "## Appendix · Official Review Question Answers / Resmî Cevaplar",
        "",
        (
            "Aşağıdaki cevaplar kaynak Appendix bölümündeki sıra ve gerekçeleri "
            "korur. Türkçe bloklar doğal teknik çeviridir."
        ),
        "",
    ]
    official_state = [1]
    for page_number, blocks in appendix_blocks(
        args.source_directory,
        args.unit,
        args.appendix_start_page,
        args.appendix_end_page,
        args.appendix_start_heading,
        args.appendix_stop_heading,
    ):
        print(f"appendix page: {page_number}", flush=True)
        appendix.append(f"<!-- appendix-source-page: {page_number:04d} -->")
        appendix.extend(
            render_blocks(blocks, cache, official_answer_state=official_state)
        )
        appendix.append("")

    appendix.extend(
        [
            "## Coverage ledger",
            "",
            f"- Chapter body marker'ları: {args.start_page}–{args.end_page}",
            (
                "- Appendix answer marker'ları: "
                f"{args.appendix_start_page}–{args.appendix_end_page}"
            ),
            f"- Resmî cevap hedefi: 1–{args.official_count}",
            "- Kod blokları özgün dilinde tutulmuştur.",
            "- Çeviri ayrıntıları ünite vocabulary ve grammar kaynaklarıyla desteklenir.",
            "",
        ]
    )
    args.output.write_text(
        "\n".join(front + body + appendix).rstrip() + "\n",
        encoding="utf-8",
    )
    print(
        f"Generated {args.output} with {len(cache)} translated prose blocks",
        flush=True,
    )


if __name__ == "__main__":
    main()
