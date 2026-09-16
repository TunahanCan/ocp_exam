#!/usr/bin/env python3
"""Apply source-aware terminology repairs and reviewed overrides to EN/TR JSONL.

This edits a separate edition of the cache; it never modifies a running worker's
append-only input. It does not claim to replace sentence-by-sentence review.
"""
from __future__ import annotations
import argparse,json,re
from pathlib import Path

def _case_like(original,replacement):
    if original and original[0].isupper():return replacement[0].upper()+replacement[1:]
    return replacement

def normalize_translation(english,turkish):
    source=english.lower();out=turkish;changes=[]
    def sub(rule,pattern,repl):
        nonlocal out
        def replace(m):
            value=repl(m) if callable(repl) else repl
            return _case_like(m.group(0),value)
        newer,n=re.subn(pattern,replace,out,flags=re.IGNORECASE)
        if n and newer!=out:changes.append(rule);out=newer
    if re.search(r'\bevents?\b',source):
        event_suffixes={'':'','ler':'lar','leri':'ları','lerin':'ların','lere':'lara','lerden':'lardan','lerle':'larla','lerinin':'larının','lerine':'larına','lerinde':'larında','lerinden':'larından','lerdir':'lardır','te':'da','ten':'dan','tir':'dır','le':'la','i':'ı','in':'ın','e':'a','inin':'ının','ine':'ına','ini':'ını','inde':'ında','inden':'ından','im':'ım','imiz':'ımız','iniz':'ınız','idir':'ıdır'}
        sub('event_to_olay',r'\betkinli(?:k|ğ)([a-zçğıöşü]*)\b',lambda m:'olay'+event_suffixes.get(m[1].lower(),m[1].lower()))
    if re.search(r'\bviews?\b',source):
        sub('view_to_gorunum',r'\bgörüş(?=[a-zçğıöşü]*\b)','görünüm')
    if re.search(r'\bapplications?\b',source):
        def application(m):
            suffix=m[1].lower()
            suffix=suffix.replace('su','sı').replace('nun','nın').replace('nu','nı').replace('yu','yı')
            return 'uygulama'+suffix
        sub('application_to_uygulama',r'\bbaşvuru([a-zçğıöşü]*)\b',application)
    if 'saga' in source:
        sub('sagah_to_saga',r'\bsagah','saga')
        sub('saga_not_legend',r'\b(?:destan|efsane)(?:lar|ler)?\b',lambda m:'saga’lar' if m[0].lower().endswith(('lar','ler')) else 'saga')
    if re.search(r'\bmap(?:s|ped|ping)?\b',source):
        sub('mapping_to_esleme',r'haritasını yapar|haritası yapar|haritalandırır|haritalar','eşler')
        sub('mapping_noun_to_esleme',r'haritalandırma|haritalama','eşleme')
    if re.search(r'\bjoin(?:s|ed|ing)?\b',source) and any(t in source for t in ('sql','query','queries','table','database','memory')):
        sub('sql_join',r'\bkatılımlar\b','JOIN işlemleri')
        sub('sql_join',r'\bkatılımı\b','JOIN işlemini')
        sub('sql_join',r'\bkatılım\b','JOIN işlemi')
    if 'maintainability' in source:
        sub('maintainability',r'sürdürülebilir','bakım yapılabilir')
        sub('maintainability',r'bakımlılı','bakım yapılabilirli')
    if 'hexagonal' in source:
        sub('hexagonal',r'sekizgen|altbuçlu|altıgenli','altıgen')
    if 'loose coupling' in source or 'loosely coupled' in source:
        sub('loose_coupling',r'boş eşleşme','gevşek bağlılık')
        sub('loosely_coupled',r'boş bir şekilde bağlantılı|gevşek bir şekilde bağlantılı|gevşek bir şekilde bağlanmış','gevşek bağlı')
    if 'state machine' in source:
        sub('state_machine',r'devlet makine','durum makine')
    if re.search(r'\bdecompos(?:e|es|ed|ing|ition)\b',source):
        sub('decomposition',r'bozunma','ayrıştırma')
        sub('decomposition',r'çürümenin','ayrıştırmanın')
        sub('decomposition',r'çürümeyi','ayrıştırmayı')
        sub('decomposition',r'çürümeye','ayrıştırmaya')
        sub('decomposition',r'çürüme','ayrıştırma')
    if 'coupling' in source or 'coupled' in source:
        sub('coupling_not_mating',r'çiftleşmenin','bağlılığın')
        sub('coupling_not_mating',r'çiftleşmeyi','bağlılığı')
        sub('coupling_not_mating',r'çiftleşmeye','bağlılığa')
        sub('coupling_not_mating',r'çiftleşmesi','bağlılığı')
        sub('coupling_not_mating',r'çiftleşme','bağlılık')
    if 'distributed system' in source:sub('distributed_system',r'paylaşılan sistem','dağıtık sistem')
    if 'distributed application' in source:sub('distributed_application',r'paylaşılan uygulama','dağıtık uygulama')
    if 'persistence' in source:
        sub('persistence_layer',r'sürdürme katman|süreklilik katman','kalıcılık katman')
    if re.search(r'\bports?\b',source):sub('port_not_harbor',r'liman','port')
    if 'inheritance' in source:sub('inheritance',r'miras','kalıtım')
    if 'object-oriented' in source:sub('object_oriented',r'nesne odaklı','nesne yönelimli')
    if re.search(r'\bclasses?\b',source):
        forms={'dersler':'sınıflar','dersleri':'sınıfları','derslerin':'sınıfların','derslere':'sınıflara','derslerde':'sınıflarda','derslerden':'sınıflardan','dersleriyle':'sınıflarıyla','derslerine':'sınıflarına','dersin':'sınıfın','dersi':'sınıfı','derse':'sınıfa','derste':'sınıfta','dersten':'sınıftan','dersine':'sınıfına','dersinin':'sınıfının','ders':'sınıf'}
        sub('class_not_lesson',r'\b(?:'+ '|'.join(sorted(forms,key=len,reverse=True))+r')\b',lambda m:forms[m[0].lower()])
    if re.search(r'\bpersist(?:s|ed|ing)?\b',source) and not re.search(r'\bmaintain\w*\b',source):
        sub('persist_not_sustain',r'sürdürmek','kalıcılaştırmak')
        sub('persist_not_sustain',r'sürdürür','kalıcılaştırır')
        sub('persist_not_sustain',r'sürdürül','kalıcılaştırıl')
    if 'out-of-order' in source or 'out of order' in source:
        sub('out_of_order',r'sipariş dışı|sıra dışı','sırası bozulmuş')
    if re.search(r'trade[- ]?offs?',source) and 'marketing' not in source:
        sub('trade_off',r'pazarlamaların','ödünleşimlerin')
        sub('trade_off',r'pazarlamalar','ödünleşimler')
        sub('trade_off',r'pazarlamanın','ödünleşimin')
        sub('trade_off',r'pazarlama','ödünleşim')
    if re.search(r'\bclients?\b',source) and not re.search(r'\b(?:customers?|consumers?)\b',source):sub('client',r'müşteri','istemci')
    if re.search(r'\bqueries\b',source) and 'question' not in source:sub('query',r'sorular','sorgular')
    if re.search(r'\bquery\b',source) and 'question' not in source:sub('query',r'\bsoru\b','sorgu')
    if 'pattern' in source and not re.search(r'\btemplates?\b',source):
        sub('pattern_language',r'örnek dili|örneği dili','örüntü dili')
        sub('pattern',r'\bşablonlar\b','örüntüler')
        sub('pattern',r'\bşablonların\b','örüntülerin')
        sub('pattern',r'\bşablonları\b','örüntüleri')
        sub('pattern',r'\bşablonun\b','örüntünün')
        sub('pattern',r'\bşablonu\b','örüntüsü')
        sub('pattern',r'\bşablon\b','örüntü')
        sub('pattern_suffix',r'örüntüun','örüntünün')
        sub('pattern_suffix',r'örüntülar','örüntüler')
    if re.search(r'\bservices?\b',source):sub('software_service',r'hizmet','servis')
    if re.search(r'\binvokes?\b',source):sub('invoke',r'çağrıştırır','çağırır')
    if 'asynchronous' in source:sub('asynchronous',r'asinkron','asenkron')
    if 'synchronous' in source:sub('synchronous',r'\bsinkron','senkron')
    sub('microservice_spelling',r'mikro servis','mikroservis')
    return out,list(dict.fromkeys(changes))

def read_cache(path):
    cache={}
    if path.suffix=='.json':
        records=json.loads(path.read_text())
    else:
        records=[]
        lines=path.read_text().splitlines()
        for i,line in enumerate(lines):
            try:records.append(json.loads(line))
            except json.JSONDecodeError:
                if i!=len(lines)-1:raise
    for r in records:
        if 'english' in r and 'turkish' in r:cache[r['english']]=r['turkish']
    return cache

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('cache',type=Path)
    ap.add_argument('output',type=Path)
    ap.add_argument('--overrides',type=Path,action='append',default=[])
    ap.add_argument('--report',type=Path)
    args=ap.parse_args()
    if args.cache.resolve()==args.output.resolve():raise SystemExit('Output must differ from input cache')
    cache=read_cache(args.cache);changes=[]
    for en,before in list(cache.items()):
        after,rules=normalize_translation(en,before)
        cache[en]=after
        if after!=before:changes.append({'english':en,'before':before,'after':after,'rules':rules})
    for path in args.overrides:
        for en,tr in read_cache(path).items():
            if en in cache and tr!=cache[en]:
                changes.append({'english':en,'before':cache[en],'after':tr,'rules':['reviewed_override']})
                cache[en]=tr
    args.output.write_text(''.join(json.dumps({'english':en,'turkish':tr},ensure_ascii=False)+'\n' for en,tr in cache.items()))
    report=args.report or args.output.with_suffix('.review.json')
    report.write_text(json.dumps({'entries':len(cache),'changes':changes,'unresolved_unknown_glyphs':[en for en,tr in cache.items() if '⁇' in tr],'unresolved_placeholders':[en for en,tr in cache.items() if re.search(r'Zxq|__TERM|<x\d',tr)]},ensure_ascii=False,indent=2)+'\n')
    print(f'{len(cache)} translations; {len(changes)} reviewed/normalized changes; {args.output}')
if __name__=='__main__':main()
