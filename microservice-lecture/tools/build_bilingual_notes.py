#!/usr/bin/env python3
"""Assemble source-ordered bilingual Markdown from extraction and translation JSON.

Markdown is the editable final source. This assembler never changes code or
figure assets. Run the PDF renderer separately after editorial corrections.
"""
from pathlib import Path
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def translations(paths):
    result = {}
    for path in paths:
        if path.suffix == '.jsonl':
            rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        else:
            rows = json.loads(path.read_text())
        for row in rows:
            result[row['english']] = row['turkish']
    return result


def source_text(text):
    text = text.replace('\uf0a1', '•').replace('\u00ad', '')
    text = re.sub(r'(https?://[^\s]+/)\s+(?=[\w.~])', r'\1', text)
    text = re.sub(r'(https?://[^\s]+)\s+(?=/)', r'\1', text)
    fixes = {
        'applications’s': 'application’s',
        'also constraints the dependencies': 'also constrains the dependencies',
        'which handled requests from external systems': 'which handle requests from external systems',
        'how to identity an application': 'how to identify an application',
        'A courier who deliver orders': 'A courier who delivers orders',
        'On interesting aspect': 'An interesting aspect',
        'restaurantrelated': 'restaurant-related',
        'A domain mode captures': 'A domain model captures',
        'to map to services, because is somewhat subjective': 'to map to services is somewhat subjective',
        'access the access database': 'access the database',
        'a Ticket simply consist of': 'a Ticket simply consists of',
        'Order Service service': 'Order Service',
        'a list of a potential services': 'a list of potential services',
        'Transcription script': 'Transaction script',
        'such \uf0ae \uf0ae as Order Service Accounting Service Order Service.':
            'such as Order Service → Accounting Service → Order Service.',
        '• \uf0ae REST client service—': '• REST client → service—',
        '• Domain event consumer publisher—': '• Domain event consumer → publisher—',
        '• \uf0ae Command message requestor replier—': '• Command message requestor → replier—',
        'the \uf0ae routing rules': 'the routing rules',
        'direct Service Service \uf0ae \uf0ae \uf0ae communication becomes Service Source Envoy Destination Envoy Service.':
            'direct Service → Service communication becomes Service → Source Envoy → Destination Envoy → Service.',
    }
    for before, after in fixes.items():
        text = text.replace(before, after)
    return text.removesuffix(' \uf0ae')


def pair(en, tr):
    return f'> **English:** {source_text(en)}\n>\n> **Türkçe:** {source_text(tr)}\n'


def chapter_markdown(data, cache, splits=None):
    c = data['chapter']
    number = c['number']
    out = [
        f"# Ünite {number:02} · {c['title_english']} — {c['title_turkish']}\n",
        f"**Amaç:** {c['title_turkish']} konusunu İngilizce–Türkçe karşılaştırmalı çalışmak; teknik açıklamaları özgün şekiller, tablolar ve kod örnekleriyle birlikte okumak.\n",
        f"**Kaynak:** Kullanıcının sağladığı *Microservices Patterns*, bölüm {number}; `Microservices_Patterns_1_Bolumden_Itibaren.pdf`, kaynak PDF sayfaları **{c['pdf_start_page']}–{c['pdf_end_page']}**. Başlık ve metin sırası korunmuş, sayfa sonlarında bölünen paragraflar birleştirilmiştir. Şekiller, üzerlerindeki yazılar korunarak kaynak PDF'den alınmıştır.\n",
        '**Okuma notu:** Teknoloji ve şirket örnekleri kitabın yazıldığı dönemin anlatımıdır. Kodlar kaynakta verilen bağlama bağlı örneklerdir; bağımsız Java 17 programları olarak sunulmaz. İngilizce kaynak ve Türkçe çeviri ardışık bloklardadır. Çeviri hazırlığında yerel bir çeviri modeli kullanılmış; teknik terimler ve metin aktarımı ayrıca kontrol edilmiştir.\n',
        '**Dil çalışması:** [Ünite sözlüğü](vocabulary.md) · [Vocabulary PDF](vocabulary.pdf) · [Grammar notları](grammar_notes.md) · [Grammar PDF](grammar_notes.pdf). Kelime anlamları ve cümle yapılarının ayrıntıları bu iki eşlikçi kaynaktadır.\n',
    ]
    previous_page = None
    for r in data['records']:
        en = r['english']
        if r['page'] != previous_page:
            out.append(f"<!-- source-pages: {','.join(map(str,r.get('pages',[r['page']])))} -->\n")
            previous_page = r['page']
        out.append(f"<!-- source-record: {r['id']} -->\n")
        if splits and en in splits:
            for part in splits[en]:
                out.append(pair(part['english'], part['turkish']))
            continue
        kind = r['type']
        if kind == 'code':
            out.append(f"```{r['language']}\n{r['code']}\n```\n")
            continue
        if en and en not in cache:
            raise ValueError(f"Missing translation {r['id']}: {en[:100]}")
        tr = cache.get(en, '')
        if kind == 'heading':
            level = r.get('level', 3)
            if en == 'This chapter covers':
                level, tr = 2, 'Bu bölümün kapsamı'
            if en == 'Summary':
                level, tr = 2, 'Bölüm özeti'
            # Display a section number once, even if the model repeats it.
            match = re.match(r'^(\d+(?:\.\d+)+)\s+', en)
            if match:
                tr = re.sub(r'^' + re.escape(match[1]) + r'\s*', '', tr)
            out.append('#' * level + f' {source_text(en)} — {source_text(tr)}\n')
        elif kind == 'figure':
            out.append(f"![Figure {r['figure']}]({r['file']})\n")
            out.append(pair(en, tr))
        elif kind == 'table':
            if en:
                out.append(pair(en, tr))
            def cell(value):
                if not value:
                    return ''
                if value not in cache:
                    raise ValueError(f"Missing table translation {r['id']}: {value}")
                english = source_text(value).replace('|', '\\|')
                turkish = source_text(cache[value]).replace('|', '\\|')
                return f'**EN:** {english}<br/>**TR:** {turkish}'
            out.append('| ' + ' | '.join(cell(v) for v in r['columns']) + ' |')
            out.append('| ' + ' | '.join('---' for _ in r['columns']) + ' |')
            for row in r['rows']:
                out.append('| ' + ' | '.join(cell(v) for v in row) + ' |')
            out.append('')
        else:
            if kind == 'annotation':
                out.append('**Kod açıklaması:**\n')
            out.append(pair(en, tr))
        if r['id'] == 'u06_0168':
            out.append('> **Editör notu — kaynakta eksik ifade:** Kaynakta “implement a new requirement to customers” ifadesinin fiili eksiktir. İzleyen iki cümledeki “market to customers” açıklamasına dayanarak Türkçede müşterilere yönelik pazarlama gereksinimi anlamı kullanılmıştır.\n')
        if r['id'] == 'u07_0254':
            out.append('> **Editör notu — karşılaştırma yönü:** Kaynağın yinelenen olay tanımı, hemen altındaki koşulla çelişir. Kod güncellemeyi yalnızca kayıt yoksa veya **saklanan son ID < gelen eventId** ise kabul eder. Dolayısıyla kayıt varsa **gelen eventId ≤ saklanan son ID** durumundaki olay yinelenmiş/eski kabul edilir. İngilizce cümle ve çevirisi kaynakta söylendiği biçimde bırakılmıştır; uygulamada alttaki kodun karşılaştırma yönünü esas alın.\n')
        if r['id'] == 'u07_0228':
            out.append('> **Editör notu — kaynak sözcük sırası:** “One map per time line” ifadesi, aynı paragraftaki lineItems alanı ve Şekil 7.13 bağlamında **her sipariş kalemi için bir map** anlamında çevrilmiştir.\n')
        if r['id'] == 'u07_0291':
            out.append('> **Editör notu — serialize / deserialize:** Kaynak ikinci cümlede de “serializes” der. Ancak başlangıç token’ı JSON’dan anahtar nesnesine geri çevrilir; bu adım **deserialize** işlemidir. İlk cümledeki sonuç anahtarını JSON token’a çevirme ise **serialize** işlemidir.\n')
        if r['id'] == 'u06_0244':
            out.append('> **Java terim notu:** Kaynak “extends” sözcüğünü üst türe bağlı olma anlamında kullanır. Java kodunda bir sınıf arayüzü **implements** ile uygular; arayüz başka bir arayüzü **extends** ile genişletir.\n')
        if r['id'] == 'u06_0166':
            out.append('> **Editör notu — kaynak ifadesi:** İlk cümlede “rather than aggregating them” yazılıdır. Bölümün teknik vurgusu, karmaşık aggregate nesne grafı yerine genellikle daha basit olayların saklanması ve gerektiğinde Memento ile snapshot alınmasıdır.\n')
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('structured', nargs='+', type=Path)
    ap.add_argument('--translations', nargs='+', type=Path, required=True,
                    help='JSON/JSONL sources in precedence order; last file wins')
    ap.add_argument('--output-root', type=Path, default=ROOT/'units')
    ap.add_argument('--splits', nargs='*', type=Path, default=[],
                    help='Reviewed EN/TR splits for paragraphs joined in extraction')
    ap.add_argument('--jobs-output', type=Path,
                    help='Only export translation requests, without writing Markdown')
    a = ap.parse_args()
    datasets = [json.loads(p.read_text()) for p in a.structured]
    if a.jobs_output:
        jobs = []
        for data in datasets:
            for r in data['records']:
                if r['type'] == 'code':
                    continue
                if r['english']:
                    jobs.append({'id':r['id'], 'english':r['english']})
                if r['type'] == 'table':
                    for i, row in enumerate([r['columns']] + r['rows']):
                        for j, value in enumerate(row):
                            if value:
                                jobs.append({'id':f"{r['id']}_t{i}_{j}", 'english':value})
        a.jobs_output.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n')
        print(f'Exported {len(jobs)} requests to {a.jobs_output}')
        return
    cache = translations(a.translations)
    splits = {r['english']:r['pairs'] for path in a.splits for r in json.loads(path.read_text())}
    for data in datasets:
        target = a.output_root / data['slug'] / 'bilingual_notes.md'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(chapter_markdown(data, cache, splits))
        print(target)


if __name__ == '__main__':
    main()
