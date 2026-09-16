#!/usr/bin/env python3
"""Offline EN->TR translation. Models and text remain local during inference."""
from __future__ import annotations
import argparse, hashlib, json, os, re, sys, time
from pathlib import Path
os.environ.setdefault('HF_HUB_OFFLINE','1')
os.environ.setdefault('TRANSFORMERS_OFFLINE','1')
import ctranslate2
import sentencepiece as spm
ROOT=Path(__file__).resolve().parent
DEFAULT_MODEL=Path('/tmp/microservices_translation_runtime/models/nllb600m')
DEFAULT_CACHE=Path('/tmp/microservices_translation_runtime/translation_cache.jsonl')

# English identifiers remain literal. Descriptive architectural terms are
# translated with a small explicit glossary, because raw NLLB sometimes changes
# their technical meaning (e.g. maintainability -> sustainability).
GLOSSARY={
    'loosely coupled': 'gevşek bağlı',
    'tightly coupled': 'sıkı bağlı',
    'loose coupling': 'gevşek bağlılık',
    'tight coupling': 'sıkı bağlılık',
    'maintainability': 'bakım yapılabilirlik',
    'testability': 'test edilebilirlik',
    'deployability': 'dağıtılabilirlik',
    'scalability': 'ölçeklenebilirlik',
    'reliability': 'güvenilirlik',
    'availability': 'kullanılabilirlik',
    'throughput': 'işlem hacmi',
    'latency': 'gecikme',
    'bounded context': 'bounded context (sınırlı bağlam)',
    'bounded contexts': 'bounded context’ler (sınırlı bağlamlar)',
    'domain-driven design': 'domain-driven design (alan odaklı tasarım)',
    'business capability': 'iş yetkinliği',
    'business capabilities': 'iş yetkinlikleri',
    'business logic': 'iş mantığı',
    'domain model': 'alan modeli',
    'domain models': 'alan modelleri',
    'god class': 'god class (aşırı sorumluluk yüklenmiş merkezî sınıf)',
    'god classes': 'god class’lar (aşırı sorumluluk yüklenmiş merkezî sınıflar)',
    'data consistency': 'veri tutarlılığı',
    'eventual consistency': 'nihai tutarlılık',
    'event sourcing': 'event sourcing (olay kaynaklı durum yönetimi)',
    'distributed transaction': 'dağıtık işlem',
    'distributed transactions': 'dağıtık işlemler',
    'inbound adapter': 'inbound adapter (giriş uyarlayıcısı)',
    'outbound adapter': 'outbound adapter (çıkış uyarlayıcısı)',
    'inbound adapters': 'inbound adapter’lar (giriş uyarlayıcıları)',
    'outbound adapters': 'outbound adapter’lar (çıkış uyarlayıcıları)',
    'inbound port': 'inbound port (giriş bağlantı noktası)',
    'outbound port': 'outbound port (çıkış bağlantı noktası)',
    'implementation details': 'gerçekleştirim ayrıntıları',
    'asynchronous messaging': 'asenkron mesajlaşma',
    'synchronous communication': 'senkron iletişim',
    'interprocess communication': 'süreçler arası iletişim',
    'code duplication': 'kod tekrarı',
    'encapsulates': 'kapsüller',
    'invokes': 'çağırır',
    'invoke': 'çağırmak',
    'clients': 'istemciler',
    'client': 'istemci',
}
_GLOSSARY_PATTERN=r'(?i:\b(?:'+ '|'.join(re.escape(t) for t in sorted(GLOSSARY,key=len,reverse=True))+r')\b)'
_IDENTIFIER_PATTERNS=[
    r'\b[A-Z][A-Za-z0-9_]*<[^<>\n]{1,100}>',
    r'\b(?!(?:The|This|That|An|A|When|If|For|In|As|Once|After|Before|During|Finally|Similarly|Likewise|Each|Another|First|Second)\b)(?:[A-Z][a-zA-Z]+\s+){1,5}Saga\b',
    r'`[^`\n]+`',
    r'https?://[^\s<>]+|www\.[^\s<>]+',
    r'@[A-Za-z_][A-Za-z0-9_]*',
    r'\b(?!(?:The|This|That|An|A|When|If|For|In|As|Once|After|Before|During|Finally|Similarly|Likewise|Each|Another|First|Second)\b)(?:[A-Z][a-zA-Z]+\s+){1,3}(?:Service|service)\b',
    r'\b(?:[A-Z][a-z0-9]+(?:[A-Z][A-Za-z0-9]*)+|[a-z]+(?:[A-Z][A-Za-z0-9]*)+)(?:<[^<>\n]{1,100}>)?(?:\([^()\n]{0,80}\))?',
    r'\b[A-Za-z_][A-Za-z0-9_]*\(\)',
    r'\b[A-Z][A-Z0-9_]{1,}\b',
    r'\b(?:Order|Consumer|Restaurant|Delivery|Courier|Money|Ticket|Address|Location|Customer|Product|Account|Payment|Saga|Aggregate|Entity)\b',
]
GLOSSARY.update({'saga':'saga','sagas':'saga’lar','aggregate':'aggregate','aggregates':'aggregate’ler','entity':'entity','entities':'entity’ler','compensation':'telafi','compensating transaction':'telafi işlemi','compensating transactions':'telafi işlemleri','orchestration':'orkestrasyon','choreography':'koreografi','stub':'stub','stubs':'stub’lar','mock':'mock','mocks':'mock’lar','commit':'commit','rollback':'geri alma','hexagonal':'altıgen'})
_CORE_TERMS=('saga','sagas','aggregate','aggregates','entity','entities','compensation','compensating transaction','compensating transactions','orchestration','choreography','stub','stubs','mock','mocks','commit','rollback','hexagonal','inbound adapter','inbound adapters','outbound adapter','outbound adapters','inbound port','inbound ports','outbound port','outbound ports','bounded context','bounded contexts','god class','god classes','event sourcing','domain-driven design')
PROTECTED_PATTERN=re.compile('|'.join(_IDENTIFIER_PATTERNS+[r'(?i:\b(?:'+'|'.join(re.escape(t) for t in sorted(_CORE_TERMS,key=len,reverse=True))+r')\b)']))
STABLE_ACRONYMS=set('API REST HTTP HTTPS SQL JSON XML HTML JDBC JPA SOAP RPC JVM JDK TCP IP UDP DNS AMQP DDD CQRS ACID CAP OSGI UI UML URI URL FTGO'.split())
def semantic_key(word,i):
    if word.startswith(('http://','https://','www.')):name='Url'
    else:
        words=re.findall('[A-Za-z0-9]+',word)
        name=''.join(w[0].upper()+w[1:] for w in words)[:48] or 'Value'
    return f'Zxq{name}Q{i}Z'


def protect_terms(text,style='semantic'):
    replacements=[]
    def sub(m):
        word=m.group(0)
        if word in STABLE_ACRONYMS:return word
        if word.lower() in ('aggregate','aggregates') and re.match(r'\s+(?:data|information|the|these|those|results|all)\b',text[m.end():],flags=re.IGNORECASE):return word
        suffix=''
        if word.startswith(('http://','https://','www.')):
            stripped=word.rstrip('.,;:)')
            suffix=word[len(stripped):];word=stripped
        value=GLOSSARY.get(word.lower(),word) if word.lower() in _CORE_TERMS and word not in ('Saga','Aggregate','Entity') else word
        i=len(replacements)
        replacements.append((word,value))
        key=semantic_key(word,i) if style=='semantic' else (f'__TERM{i}__' if style=='term' else f'<x{i}>')
        return key+suffix
    return PROTECTED_PATTERN.sub(sub,text),replacements

def restore_terms(text,replacements,style='semantic'):
    missing=[]
    for i,(original,value) in enumerate(replacements):
        if style=='semantic':pattern=re.escape(semantic_key(original,i))
        elif style=='term':pattern=rf'_{{0,2}}\s*TERM\s*0*{i}(?!\d)\s*_{{0,2}}'
        else:pattern=rf'<?\s*x\s*0*{i}(?!\d)\s*>?'
        text,n=re.subn(pattern,lambda _:value,text,flags=re.IGNORECASE)
        if not n:missing.append(original)
    return text,missing

class LocalTranslator:
    def __init__(self, model_dir=DEFAULT_MODEL, *, beam_size=2, intra_threads=6, inter_threads=2, batch_size=48, protect=True):
        self.model_dir=Path(model_dir)
        self.sp=spm.SentencePieceProcessor(model_file=str(self.model_dir/'sentencepiece.bpe.model'))
        self.translator=ctranslate2.Translator(str(self.model_dir),device='cpu',compute_type='int8',intra_threads=intra_threads,inter_threads=inter_threads)
        self.beam_size=beam_size
        self.batch_size=batch_size
        self.protect=protect
        self.warnings=[]

    def split(self,text):
        """Translate each sentence explicitly; split only oversized sentences at words."""
        sentences=re.split(r'(?<=[.!?])\s+(?=[A-Z“"(])', text.strip())
        chunks=[]
        for sentence in sentences:
            if not sentence.strip():continue
            if len(self.sp.encode(sentence))<=240:
                chunks.append(sentence)
            else:
                words=sentence.split();acc=[]
                for word in words:
                    trial=' '.join(acc+[word])
                    if acc and len(self.sp.encode(trial))>240:
                        chunks.append(' '.join(acc));acc=[word]
                    else:acc.append(word)
                if acc:chunks.append(' '.join(acc))
        return chunks or ['']

    def _translate_raw(self,chunks, *, beam_size=None):
        normalized=[s.translate(str.maketrans({'’': chr(39), '‘': chr(39), '“': chr(34), '”': chr(34), '—': ' - ', '–': '-', '…': '...', '': ' - ', '•': ' - ', '«': chr(34), '»': chr(34)})) for s in chunks]
        source=[['eng_Latn']+self.sp.encode_as_pieces(s)+['</s>'] for s in normalized]
        results=self.translator.translate_batch(source,target_prefix=[['tur_Latn'] for _ in chunks],beam_size=self.beam_size if beam_size is None else beam_size,max_decoding_length=512,max_input_length=512,batch_type='tokens',max_batch_size=2048,repetition_penalty=1.0)
        outputs=[]
        for s,r in zip(chunks,results,strict=True):
            tokens=r.hypotheses[0]
            if tokens and tokens[0]=='tur_Latn':tokens=tokens[1:]
            text=self.sp.decode(tokens).strip()
            if s.strip() and not text:raise RuntimeError('Empty translation for nonempty source')
            outputs.append(text)
        return outputs

    def translate_chunks(self,chunks):
        if not self.protect:return self._translate_raw(chunks)
        prepared=[s.lower() if s.isupper() and '_' not in s and s.strip() not in STABLE_ACRONYMS else s for s in chunks]
        protected=[protect_terms(s) for s in prepared]
        raw=self._translate_raw([p for p,r in protected])
        outputs=[]
        for source,translated,(p,replacements) in zip(prepared,raw,protected,strict=True):
            for i,(original,value) in enumerate(replacements):
                key=semantic_key(original,i)
                if translated.count(key)>1:
                    self.warnings.append({'kind':'duplicate_protected_token_removed','source':source,'token':original})
                    while translated.count(key)>1:translated=translated.replace(key,'',1)
            restored,missing=restore_terms(translated,replacements)
            unresolved=bool(re.search(r'Zxq|__TERM|<x\d',restored))
            if missing or unresolved:
                # Retry only this sentence using another placeholder syntax.
                alternate,alt_replacements=protect_terms(source,'xml')
                alternate_out=self._translate_raw([alternate],beam_size=max(4,self.beam_size))[0]
                restored,still_missing=restore_terms(alternate_out,alt_replacements,'xml')
                alternate_unresolved=bool(re.search(r'Zxq|__TERM|<x\d',restored))
                if still_missing or alternate_unresolved:
                    # Last-resort repair preserves every technical token and
                    # translates all intervening prose. Flag for editorial review.
                    fragment_source,_=protect_terms(source,'term')
                    pieces=re.split(r'(__TERM\d+__)',fragment_source)
                    prose=[v for v in pieces if v.strip() and not re.fullmatch(r'__TERM\d+__',v)]
                    prosetr=iter(self._translate_raw(prose)) if prose else iter([])
                    result=[]
                    for piece in pieces:
                        m=re.fullmatch(r'__TERM(\d+)__',piece)
                        if m:result.append(replacements[int(m.group(1))][1])
                        elif piece.strip():result.append(next(prosetr))
                    restored=' '.join(result)
                self.warnings.append({'kind':'protected_terms_repaired','source':source,'missing':missing,'fallback_fragment_translation':bool(still_missing or alternate_unresolved),'translation':restored})
            # Technical context: services are software services, not benefits.
            restored=re.sub(r'\bhizmet', 'servis',restored,flags=re.IGNORECASE)
            restored=restored.replace('çağrıştırır','çağırır').replace('asinkron','asenkron')
            lower_source=source.lower()
            if 'maintainability' in lower_source:
                restored=re.sub(r'sürdürülebilir', 'bakım yapılabilir', restored, flags=re.IGNORECASE)
            if 'loosely coupled' in lower_source or 'loose coupling' in lower_source:
                restored=re.sub(r'boş bir şekilde bağlantılı|boşlukla bağlantılı|gevşek bir şekilde bağlantılı|gevşek bir şekilde bağlanmış', 'gevşek bağlı', restored, flags=re.IGNORECASE)
            if re.search(r'\bclients?\b',lower_source) and not re.search(r'\b(?:customers?|consumers?)\b',lower_source):
                restored=re.sub(r'müşteri','istemci',restored,flags=re.IGNORECASE)
            if 'throughput' in lower_source:
                restored=re.sub(r'\bverimlilik\b','işlem hacmi',restored,flags=re.IGNORECASE)

            if 'hexagonal' in lower_source:
                restored=re.sub(r'sekizgen|altıgenli','altıgen',restored,flags=re.IGNORECASE)
            if 'persistence' in lower_source:
                restored=re.sub(r'sürdürme katman|süreklilik katman','kalıcılık katman',restored,flags=re.IGNORECASE)
            if re.search(r'\bports?\b',lower_source):
                restored=re.sub(r'liman','port',restored,flags=re.IGNORECASE)
            if 'inheritance' in lower_source:
                restored=re.sub(r'miras','kalıtım',restored,flags=re.IGNORECASE)
            if 'object-oriented' in lower_source:
                restored=restored.replace('nesne odaklı','nesne yönelimli').replace('Nesne odaklı','Nesne yönelimli')
            if 'pattern' in lower_source and not re.search(r'\btemplates?\b',lower_source):
                restored=re.sub(r'şablon','örüntü',restored,flags=re.IGNORECASE)
                restored=restored.replace('örnek dili','örüntü dili').replace('örneği dili','örüntü dili')
            restored=restored.replace('mikro servis','mikroservis')
            outputs.append(restored.strip())
        return outputs

    def translate_many(self,texts, *, progress=None):
        groups=[self.split(s) for s in texts]
        chunks=[s for group in groups for s in group]
        translations=[]
        for start in range(0,len(chunks),self.batch_size):
            batch=chunks[start:start+self.batch_size]
            translations.extend(self.translate_chunks(batch))
            if progress:progress(min(start+len(batch),len(chunks)),len(chunks))
        out=[];i=0
        for group in groups:
            out.append(' '.join(translations[i:i+len(group)]));i+=len(group)
        return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('input',type=Path,help='JSON list of strings or records')
    ap.add_argument('output',type=Path)
    ap.add_argument('--source-field',default='english')
    ap.add_argument('--target-field',default='turkish')
    ap.add_argument('--cache',type=Path,default=DEFAULT_CACHE)
    ap.add_argument('--priority-jobs',type=Path)
    ap.add_argument('--no-protect',action='store_true')
    ap.add_argument('--warnings',type=Path)
    ap.add_argument('--model',type=Path,default=DEFAULT_MODEL)
    ap.add_argument('--beam-size',type=int,default=2)
    ap.add_argument('--batch-size',type=int,default=48)
    ap.add_argument('--intra-threads',type=int,default=6)
    ap.add_argument('--inter-threads',type=int,default=2)
    args=ap.parse_args()
    records=json.loads(args.input.read_text())
    if not isinstance(records,list):raise SystemExit('Input must be a JSON list')
    texts=[r if isinstance(r,str) else r[args.source_field] for r in records]
    cache={}
    if args.cache.exists():
        for line in args.cache.read_text().splitlines():
            try:
                r=json.loads(line);cache[r['english']]=r['turkish']
            except (ValueError,KeyError):pass
    pending=list(dict.fromkeys(t for t in texts if t not in cache))
    if args.priority_jobs:
        priority={r if isinstance(r,str) else r[args.source_field] for r in json.loads(args.priority_jobs.read_text())}
        pending.sort(key=lambda text: text not in priority)
    print(f'{len(texts)} input paragraphs, {len(pending)} untranslated',flush=True)
    translator=LocalTranslator(args.model,beam_size=args.beam_size,batch_size=args.batch_size,intra_threads=args.intra_threads,inter_threads=args.inter_threads,protect=not args.no_protect)
    started=time.monotonic()
    args.cache.parent.mkdir(parents=True,exist_ok=True)
    with args.cache.open('a') as cf:
        for start in range(0,len(pending),32):
            batch=pending[start:start+32]
            results=translator.translate_many(batch)
            for english,turkish in zip(batch,results,strict=True):
                cache[english]=turkish
                cf.write(json.dumps({'english':english,'turkish':turkish},ensure_ascii=False)+'\n')
            cf.flush()
            warnings_path=args.warnings or args.output.with_suffix('.warnings.json')
            warnings_path.write_text(json.dumps(translator.warnings,ensure_ascii=False,indent=2)+'\n')
            print(f'{min(start+len(batch),len(pending))}/{len(pending)} paragraphs; elapsed {time.monotonic()-started:.1f}s',flush=True)
    output=[{'english':r,'turkish':cache[r]} if isinstance(r,str) else dict(r,**{args.target_field:cache[r[args.source_field]]}) for r in records]
    warnings_path=args.warnings or args.output.with_suffix('.warnings.json')
    warnings_path.write_text(json.dumps(translator.warnings,ensure_ascii=False,indent=2)+'\n')
    args.output.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(f'Wrote {args.output}',flush=True)
if __name__=='__main__':main()
