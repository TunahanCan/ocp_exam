#!/usr/bin/env python3
"""Lossless special-block extraction for the supplied Microservices Patterns PDF.

Public API: extract_special_blocks(spans, page) -> (records, remaining_spans).
Call after removing page furniture and the visually checked figure regions, but
before grouping prose. Span dictionaries are those produced by extract_book.py.

This is deliberately source-specific. Table geometry was checked against the
supplied PDF, including its two unnumbered operation-specification tables. Only
coordinates are fixed below: every caption, heading and cell comes from source
spans. No external packages are required.
"""
from __future__ import annotations

from bisect import bisect_right
import re
from statistics import median

# (table ID, caption top, header top, end, column starts, logical row starts).
# A None caption/header denotes an unnumbered, headerless specification table.
TABLES = {
    48: [('2.1', 516, 537, 603, [99, 150, 206, 337], [556, 573])],
    49: [
        ('2.1', 54, 75, 196, [108, 159, 215, 346], [94, 121, 148, 175]),
        ('operation_createOrder', None, None, 399, [108, 189], [292, 319, 336, 375]),
        ('operation_acceptOrder', None, None, 593, [108, 189], [497, 514, 531, 559]),
    ],
    62: [('2.2', 117, 138, 270, [99, 216], [157, 174, 191, 208, 237])],
    63: [('2.3', 54, 75, 343, [108, 196, 344], [94, 111, 203, 232, 271, 321])],
    67: [('3.1', 390, 421, 480, [108, 220, 363], [440, 457])],
    93: [('3.2', 153, 174, 283, [108, 244, 338], [193, 210, 227, 254, 271])],
    117: [('4.1', 54, 75, 190, [108, 147, 252, 372], [94, 111, 128, 145, 162, 179])],
    198: [('6.1', 323, 344, 528, [99, 190, 367], list(range(363, 517, 17)))],
    238: [('7.1', 322, 343, 524, [99, 209, 346], [362, 399, 426, 463, 500])],
    320: [('10.1', 499, 520, 605, [99, 185, 300, 389], [539, 566, 583])],
}

# These four mathematical paragraphs are the only body-text occurrences of
# Baskerville superscript/subscript fonts in the supplied chapter pages. Keep
# plain-text notation explicit so PDF/Markdown renderers cannot lose it again.
# Keys are immutable source-run anchors, not generated paragraph IDs.
ENGLISH_OVERRIDES = {
    '116:9': {
        'source_runs': {f'116:{i}' for i in range(9, 43)},
        'english': (
            'Suppose that the (n + 1)th transaction of a saga fails. The effects of the previous n '
            'transactions must be undone. Conceptually, each of those steps, T_i, has a corresponding '
            'compensating transaction, C_i, which undoes the effects of the T_i. To undo the effects '
            'of those first n steps, the saga must execute each C_i in reverse order. The sequence '
            'of steps is T_1 … T_n, C_n … C_1, as shown in figure 4.3. In this example, T_(n+1) '
            'fails, which requires steps T_1 … T_n to be undone.'),
    },
    '116:43': {
        'source_runs': {f'116:{i}' for i in range(43, 58)},
        'english': (
            'The saga executes the compensation transactions in reverse order of the forward '
            'transactions: C_n … C_1. The mechanics of sequencing the C_i transactions aren’t any '
            'different than sequencing the T_i transactions. The completion of C_i must trigger '
            'the execution of C_(i−1).'),
    },
    '227:87': {'replace': ('99.5%(4+1)', '(99.5%)^(4+1)')},
    '104:68': {'replace': ('99.5%3', '(99.5%)^3')},
}


def apply_english_overrides(records):
    """Repair verified mathematical layout damage while preserving source runs.

    Call after paragraph/continuation grouping and before translation. Every
    changed record retains its extracted text and a correction note for audit.
    A changed paragraph boundary raises instead of replacing unrelated prose.
    """
    result = []
    for original in records:
        record = dict(original)
        for anchor, override in ENGLISH_OVERRIDES.items():
            if anchor not in record.get('source_runs', []):
                continue
            extracted = record['english']
            if 'source_runs' in override:
                if set(record['source_runs']) != override['source_runs']:
                    raise ValueError(f'Mathematical correction {anchor}: paragraph boundary changed')
                corrected = override['english']
            else:
                before, after = override['replace']
                if before not in extracted and after not in extracted:
                    raise ValueError(f'Mathematical correction {anchor}: expected expression missing')
                corrected = extracted.replace(before, after)
            if corrected != extracted:
                record['english_extracted'] = extracted
                record['english'] = corrected
                record['source_correction'] = (
                    'Verified against the source PDF: restored mathematical subscript/superscript '
                    'using explicit plain-text notation; all source text runs retained.')
        result.append(record)
    return result


def _clean_prose(s):
    s = s.replace('\u00ad', '').replace('\ufb01', 'fi').replace('\ufb02', 'fl')
    # Verified compound words in wrapped table/callout text; other wraps are
    # typesetting hyphens, including split identifiers such as Order-Created.
    s = re.sub(r'(\w+)-\s*\n\s*(\w+)',
               lambda m: m[1] + ('-' if (m[1] + '-' + m[2]).lower()
                                 in {'code-generated', 'cluster-wide'} else '') + m[2], s)
    s = re.sub(r'\s+', ' ', s).strip()
    return re.sub(r'\s+([,.;:!?])', r'\1', s)


def _lines(spans):
    groups = []
    for t in sorted(spans, key=lambda t: (t['y'], t['x'])):
        if not groups or t['y'] - groups[-1]['y'] > 2:
            groups.append({'y': t['y'], 'spans': []})
        groups[-1]['spans'].append(t)
    for g in groups:
        g['spans'].sort(key=lambda t: t['x'])
        g['x'] = min(t['x'] for t in g['spans'])
        g['bottom'] = max(t['y'] + t['h'] for t in g['spans'])
    return groups


def _join(spans, *, code=False, advance=4.8):
    result = ''
    right = None
    for t in sorted(spans, key=lambda t: t['x']):
        s = t['s'].replace('\ufb01', 'fi').replace('\ufb02', 'fl')
        gap = t['x'] - right if right is not None else 0
        if result and s and gap > 1.5 and not result[-1].isspace() and not s[0].isspace():
            result += ' ' * (max(1, round(gap / advance)) if code else 1)
        result += s
        right = t['x'] + t['w']
    return result.rstrip() if code else result.strip()


def _cell(spans):
    """Retain per-line text so bullets and wrapped words stay recoverable."""
    lines = [_join(g['spans']).replace('\uf0a1', '•') for g in _lines(spans)]
    raw = '\n'.join(lines)
    return _clean_prose(raw), raw


def extract_tables(spans, page):
    records = []
    used = set()
    for table_id, caption_y, header_y, end, starts, row_starts in TABLES.get(page, []):
        start = caption_y if caption_y is not None else row_starts[0] - 2
        members = [t for t in spans if start - 1 <= t['y'] < end]
        if not members:
            continue
        # A wrong source PDF should fail conspicuously instead of silently
        # deleting prose. All tables here have small-font cells.
        if any('Baskerville' in t['family'] and t['size'] >= 9.5 for t in members):
            raise ValueError(f'Table {table_id}, page {page}: geometry intersects body prose')
        ncols = len(starts)
        captions = [t for t in members if header_y is not None and t['y'] < header_y - 3]
        headers = [t for t in members if t['color'].lower() == '#ffffff']
        body = [t for t in members if t not in captions and t not in headers]
        if header_y is not None:
            body = [t for t in body if t['y'] >= row_starts[0] - 2]
        header_cells = [[] for _ in starts]
        cell_spans = [[[] for _ in starts] for _ in row_starts]
        for t in headers:
            col = max(0, min(ncols - 1, bisect_right(starts, t['x'] + 2) - 1))
            header_cells[col].append(t)
        for t in body:
            col = max(0, min(ncols - 1, bisect_right(starts, t['x'] + 2) - 1))
            row = max(0, min(len(row_starts) - 1, bisect_right(row_starts, t['y'] + 2) - 1))
            cell_spans[row][col].append(t)
        rows = [[_cell(c)[0] for c in row] for row in cell_spans]
        rows_source_lines = [[_cell(c)[1] for c in row] for row in cell_spans]
        if not all(any(cell for cell in row) for row in rows):
            raise ValueError(f'Table {table_id}, page {page}: an expected logical row is empty')
        record = {
            'type': 'table', 'table': table_id, 'english': _cell(captions)[0],
            'columns': [_cell(c)[0] for c in header_cells], 'rows': rows,
            'rows_source_lines': rows_source_lines,
            'page': page, 'y': start, 'bottom': end,
            'source_runs': [t['run'] for t in members],
            'source_cell_runs': [[[t['run'] for t in cell] for cell in row] for row in cell_spans],
            'source_box_pt': [min(t['x'] for t in members) - 6, start - 3,
                              max(t['x'] + t['w'] for t in members) + 4, end],
            'uncaptioned': caption_y is None, 'headerless': header_y is None,
            'continued': bool(caption_y is not None and 'continued' in _cell(captions)[0]),
        }
        records.append(record)
        used.update(record['source_runs'])
    return records, [t for t in spans if t['run'] not in used]


def is_code_span(t):
    return 'Courier' in t['family'] and t['size'] <= 8 and t['color'].lower() != '#ffffff'


def is_annotation_span(t):
    return ('Humanist' in t['family'] or 'Arial' in t['family']
            or ('Helvetica' in t['family'] and t['color'] == '#656565' and t['size'] <= 9))


def _code_boundary(t):
    if is_code_span(t) or is_annotation_span(t):
        return False
    return ('Baskerville' in t['family'] or 'FranklinGothic' in t['family']) and bool(t['s'].strip())


def infer_language(code):
    if re.search(r'^(?:\s*\$ |\s*(?:curl|docker|kubectl|istioctl|export|java|mvn|npm|aws|git|gradle|yarn|cd|ls|\./gradlew)\s)', code, re.M):
        return 'bash'
    if re.search(r'^\s*(?:syntax\s*=\s*"proto|message\s+\w+\s*\{|rpc\s+\w+\s*\()', code, re.M):
        return 'protobuf'
    if re.search(r'^\s*(?:apiVersion|kind|service|services|server|spring|metadata|spec|Resources|AWSTemplateFormatVersion)\s*:', code, re.M):
        return 'yaml'
    if re.match(r'\s*[\[{]', code) and re.search(r'"[^"\n]+"\s*:', code):
        return 'json'
    if re.match(r'\s*(?:SELECT|UPDATE|CREATE TABLE|DELETE|INSERT|ROLLBACK|BEGIN|COMMIT)\b', code, re.I):
        return 'sql'
    if re.search(r'^\s*(?:GET|POST|PUT|DELETE|PATCH|HTTP/\d)\s*[/ ]', code, re.M):
        return 'http'
    if re.search(r'^\s*(?:Feature|Scenario|Given|When|Then|And|As a)\b', code, re.M):
        return 'gherkin'
    if re.search(r'^\s*(?:(?:const|let|var)\s+|(?:async\s+)?function\s+|module\.exports|constructor\s*\(|app\.(?:get|post)\()', code, re.M):
        return 'javascript'
    if re.search(r'^\s*(?:type\s+\w+\s*\{|query\s*(?:\w+\s*)?\{|schema\s*\{)', code, re.M):
        return 'graphql'
    if re.search(r'^\s*(?:(?:org\.springframework\.cloud\.contract\.spec\.)?Contract\.make|dependencies\s*\{|apply plugin:|buildscript\s*\{|task\s+\w+)', code, re.M):
        return 'groovy'
    if re.match(r'\s*(?:FROM|RUN|COPY|ENTRYPOINT|CMD|EXPOSE|ENV)\s', code):
        return 'dockerfile'
    if re.match(r'\s*(?:\d{4}-\d{2}-\d{2} |Consumer - |attribute_not_exists\()', code):
        return 'text'
    return 'java'


def extract_code(spans, page):
    """Group code independently of adjacent callout annotations.

    Physical line coordinates and untouched per-span text remain in the record.
    The smallest left edge is used as a local baseline; page continuation merging
    can instead use ``source_baseline_x`` to preserve a chapter-wide baseline.
    """
    code_spans = [t for t in spans if is_code_span(t)]
    code_lines = _lines(code_spans)
    boundaries = [t for t in spans if _code_boundary(t)]
    groups = []
    for g in code_lines:
        prev = groups[-1][-1] if groups else None
        interrupted = prev and any(prev['bottom'] - 1 < t['y'] < g['y'] - 2 for t in boundaries)
        if prev is None or g['y'] - prev['y'] > 42 or interrupted:
            groups.append([])
        groups[-1].append(g)
    records = []
    used = set()
    for lines in groups:
        members = [t for g in lines for t in g['spans']]
        # Figure captions may contain 8-point Courier; manifests normally remove
        # them. Do not swallow a remaining inline code name beside prose.
        overlaps_prose = any(abs(t['y'] - g['y']) <= 2 for t in boundaries for g in lines)
        if overlaps_prose and len(lines) == 1:
            continue
        advances = [t['w'] / len(t['s']) for t in members if len(t['s']) >= 8 and t['w'] > 0]
        advance = median(advances) if advances else 4.8
        if not 3.5 <= advance <= 6:
            advance = 4.8
        x0 = min(g['x'] for g in lines)
        rendered = []
        previous_y = None
        for g in lines:
            if previous_y is not None and g['y'] - previous_y >= 17:
                rendered.append('')
            rendered.append(' ' * max(0, round((g['x'] - x0) / advance)) +
                            _join(g['spans'], code=True, advance=advance))
            previous_y = g['y']
        code = '\n'.join(rendered)
        records.append({
            'type': 'code', 'english': code, 'code': code, 'language': infer_language(code),
            'page': page, 'y': lines[0]['y'], 'bottom': lines[-1]['bottom'],
            'source_runs': [t['run'] for t in members],
            'source_baseline_x': x0, 'source_character_advance': round(advance, 4),
            'source_code_lines': [{'y': g['y'], 'x': g['x'],
                                   'text': _join(g['spans'], code=True, advance=advance),
                                   'source_runs': [t['run'] for t in g['spans']]} for g in lines],
            'continues_from_previous_page': lines[0]['y'] <= 65,
            'continues_on_next_page': lines[-1]['bottom'] >= 575,
        })
        used.update(t['run'] for t in members)
    return records, [t for t in spans if t['run'] not in used]


def extract_annotations(spans, page):
    """Keep adjacent code callout columns in independent reading order.

    The PDF uses separate Humanist text runs for every physical callout line.
    Full-page baseline grouping interleaves neighboring callouts. Connect only
    nearby lines whose horizontal intervals overlap or share a text edge.
    """
    candidates = sorted((t for t in spans if is_annotation_span(t)),
                        key=lambda t: (t['y'], t['x']))
    groups = []
    for t in candidates:
        eligible = []
        for n, group in enumerate(groups):
            last = group['last']
            dy = t['y'] - last['y']
            if not 0 <= dy <= 13:
                continue
            left, right = last['x'], last['x'] + last['w']
            t_right = t['x'] + t['w']
            overlap = min(right, t_right) - max(left, t['x'])
            gap = max(left - t_right, t['x'] - right, 0)
            if dy <= 2:
                # Inline font changes can split one callout line into runs.
                compatible = gap <= 5
            else:
                compatible = overlap >= min(3, min(last['w'], t['w']) * .2)
                compatible |= min(abs(t['x'] - left), abs(t_right - right)) <= 4
            if compatible:
                score = dy + abs((left + right) - (t['x'] + t_right)) * .1
                eligible.append((score, n))
        if eligible:
            _, n = min(eligible)
            group = groups[n]
            group['spans'].append(t)
            if abs(t['y'] - group['last']['y']) <= 2:
                left = min(t['x'], group['last']['x'])
                right = max(t['x'] + t['w'], group['last']['x'] + group['last']['w'])
                group['last'] = dict(t, x=left, w=right-left)
            else:
                group['last'] = t
        else:
            groups.append({'spans': [t], 'last': t})
    records = []
    for group in groups:
        members = group['spans']
        english, raw = _cell(members)
        records.append({
            'type': 'annotation', 'english': english, 'page': page,
            'y': min(t['y'] for t in members),
            'bottom': max(t['y'] + t['h'] for t in members),
            'source_runs': [t['run'] for t in members],
            'source_lines': raw,
            'source_box_pt': [min(t['x'] for t in members), min(t['y'] for t in members),
                              max(t['x'] + t['w'] for t in members),
                              max(t['y'] + t['h'] for t in members)],
        })
    used = {t['run'] for t in candidates}
    return records, [t for t in spans if t['run'] not in used]


def extract_special_blocks(spans, page):
    """Extract tables, intact code and independent callouts; leave prose."""
    tables, remaining = extract_tables(spans, page)
    code, remaining = extract_code(remaining, page)
    annotations, remaining = extract_annotations(remaining, page)
    return sorted(tables + code + annotations, key=lambda r: r['y']), remaining


def merge_code_continuations(records):
    """Join a listing split at a page turn, allowing intervening callout records.

    Coordinates are normalized by the book's alternating 93/102 pt text margin.
    Thus an indented first line on the next page keeps its original indentation.
    Explicit prose, tables or headings between fragments prevent a merge.
    """
    result = []
    for original in records:
        r = dict(original)
        if r.get('type') != 'code' or not r.get('continues_from_previous_page'):
            result.append(r)
            continue
        j = len(result) - 1
        while j >= 0 and result[j].get('type') == 'annotation':
            j -= 1
        previous = result[j] if j >= 0 else None
        last_page = previous.get('pages', [previous.get('page')])[-1] if previous else None
        if not (previous and previous.get('type') == 'code'
                and previous.get('continues_on_next_page')
                and last_page == r['page'] - 1):
            result.append(r)
            continue
        # Materialize physical page numbers before combining the line lists.
        old_lines = [dict(g, page=g.get('page', previous['page']))
                     for g in previous['source_code_lines']]
        new_lines = [dict(g, page=g.get('page', r['page']))
                     for g in r['source_code_lines']]
        combined = old_lines + new_lines
        relative_left = min(g['x'] - (93 if g['page'] % 2 == 0 else 102) for g in combined)
        advance = previous.get('source_character_advance', 4.8)
        code_lines = []
        preceding = None
        for line in combined:
            if preceding and line['page'] == preceding['page'] and line['y'] - preceding['y'] >= 17:
                code_lines.append('')
            left = line['x'] - (93 if line['page'] % 2 == 0 else 102) - relative_left
            code_lines.append(' ' * max(0, round(left / advance)) + line['text'])
            preceding = line
        previous['source_code_lines'] = combined
        previous['source_runs'] = previous['source_runs'] + r['source_runs']
        previous['code'] = '\n'.join(code_lines)
        previous['english'] = previous['code']
        previous['pages'] = previous.get('pages', [previous['page']]) + [r['page']]
        previous['bottom'] = r['bottom']
        previous['continues_on_next_page'] = r['continues_on_next_page']
        previous['merged_page_continuation'] = True
    return result
