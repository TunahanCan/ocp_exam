#!/usr/bin/env python3
"""Extract source-ordered prose, tables, code and figure references from the supplied PDF.

Uses Poppler's XML coordinates and the visually checked figure manifests. The
JSON is an intermediate build artifact; editable study material lives in Markdown.
"""
from __future__ import annotations
import argparse, collections, json, re, subprocess, xml.etree.ElementTree as ET
from pathlib import Path

from extract_special_blocks import extract_special_blocks, merge_code_continuations, apply_english_overrides

HYPHEN_WORDS=set()

ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'Microservices_Patterns_1_Bolumden_Itibaren.pdf'

def unit_slug(c):
 return 'unit_%02d_'%c['number']+re.sub(r'[^a-z0-9]+','_',c['title_english'].lower()).strip('_')

def clean(s):
 s=s.replace('\uf0a1','•').replace('\u00ad','').replace('\ufb01','fi').replace('\ufb02','fl')
 s=re.sub(r'([A-Za-z]+)-\s*\n\s*([A-Za-z]+)',lambda m: m[1]+'-'+m[2] if (m[1]+'-'+m[2]).lower() in HYPHEN_WORDS else m[1]+m[2],s)
 s=re.sub(r'\s+',' ',s).strip()
 s=re.sub(r'\s+([,.;:!?])',r'\1',s)
 s=s.replace('CREATE _PENDING','CREATE_PENDING')
 s=re.sub(r'(https?://)\s+',r'\1',s)
 s=re.sub(r'([A-Z])\s+(_[A-Z])',r'\1\2',s)
 return s

def line_text(spans,code=False):
 spans=sorted(spans,key=lambda t:t['x']);out='';right=None
 for t in spans:
  text=t['s']
  if right is not None and t['x']-right>1.5 and out and not out[-1].isspace() and text and not text[0].isspace():
   out+=' ' if not code else ' '*max(1,round((t['x']-right)/4.8))
  out+=text;right=t['x']+t['w']
 return out.rstrip() if code else re.sub(r'\s+',' ',out).strip()

def lines_for(spans):
 groups=[]
 for t in sorted(spans,key=lambda t:(t['y'],t['x'])):
  if not groups or abs(t['y']-groups[-1]['y'])>2:
   groups.append({'y':t['y'],'spans':[t]})
  else:groups[-1]['spans'].append(t)
 for g in groups:
  g['x']=min(t['x'] for t in g['spans']);g['bottom']=max(t['y']+t['h'] for t in g['spans']);g['s']=line_text(g['spans'])
 return groups

def in_box(t,box):
 x,y=t['x']+t['w']/2,t['y']+t['h']/2
 return box[0]-0.6<=x<=box[2]+0.6 and box[1]-0.6<=y<=box[3]+0.6

def kind(g):
 ss=g['spans'];families=' '.join(t['family'] for t in ss)
 if all('Courier' in t['family'] and t['size']<=8 for t in ss):return 'code'
 if any(('FranklinGothic-Demi' in t['family'] or 'Courier' in t['family']) and t['color']=='#ffffff' for t in ss):return 'listing'
 if any('FranklinGothic-Demi' in t['family'] and t['color']=='#466a85' and t['size']>=11 for t in ss):return 'heading'
 if all(t['color']=='#466a85' and 'FranklinGothic' in t['family'] for t in ss) and not any('Book' in t['family'] for t in ss):return 'subheading'
 if any('Humanist' in t['family'] or 'Arial' in t['family'] for t in ss):return 'annotation'
 return 'prose'

def extract_chapter(c,pages,fonts):
 unit=ROOT/'units'/unit_slug(c)
 manifest_path=unit/'assets/manifest.json'
 manifest=json.loads(manifest_path.read_text())
 figures=collections.defaultdict(list)
 for f in manifest['figures']:figures[f['source_pdf_page']].append(f)
 records=[];stats=collections.Counter();all_runs=[]
 for pn in range(c['pdf_start_page'],c['pdf_end_page']+1):
  page=pages[pn];spans=[]
  for n,t in enumerate(page.findall('text')):
   s=''.join(t.itertext());font=fonts[t.get('font')]
   if not s.strip():continue
   a={'s':s,'x':float(t.get('left')),'y':float(t.get('top')),'w':float(t.get('width')),'h':float(t.get('height')),'size':float(font['size']),'family':font['family'],'color':font['color'],'run':f'{pn}:{n}'}
   stats['runs_total']+=1
   if a['y']<45 or a['y']>630 or (pn==c['pdf_start_page'] and (a['size']>=25 or (a['y']>=595 and re.fullmatch(r'\d+',s.strip())))):
    stats['runs_header_footer_title']+=1;continue
   reason=None
   for f in figures[pn]:
    if in_box(a,f['crop_box_pt']):reason='runs_figure';break
    if 'caption_box_pt' in f and in_box(a,f['caption_box_pt']):reason='runs_caption';break
   if reason:stats[reason]+=1;continue
   spans.append(a);all_runs.append(a['run'])
  special_records,spans=extract_special_blocks(spans,pn)
  lines=lines_for(spans)
  # Separate callout annotations from the code runs they sit beside.
  expanded=[]
  for g in lines:
   code=[t for t in g['spans'] if 'Courier' in t['family'] and t['size']<=8]
   ann=[t for t in g['spans'] if 'Humanist' in t['family'] or 'Arial' in t['family']]
   if code and ann:
    for subset in (code,ann,[t for t in g['spans'] if t not in code and t not in ann]):
     if subset:expanded+=lines_for(subset)
   else:expanded.append(g)
  expanded.sort(key=lambda g:(g['y'],g['x']))
  blocks=[];current=None
  for g in expanded:
   s=g['s'];k=kind(g)
   if not s:continue
   bullet=bool(re.match(r'^[\uf0a1\u2022]|^\d+\s',s)) and any('Wingdings' in t['family'] or t['color']=='#cca658' for t in g['spans'])
   if bullet:s=re.sub(r'^[\uf0a1\u2022]\s*','• ',s)
   g['s']=s
   # The first-line indentation (12 pt) marks a new paragraph even without
   # extra vertical whitespace. It is not confused with a bullet continuation.
   base=93 if pn%2==0 else 102
   first_span=min(g['spans'],key=lambda t:t['x'])
   is_indent=first_span['s'].startswith(' ') and any('Baskerville' in t['family'] for t in g['spans'])
   new=current is None or k!=current['kind'] or bullet
   if current and current['bullet'] and not bullet and g['x']<=current['x']+3:
    new=True
   if current and not new:
    gap=g['y']-current['last_y']
    if k in ('heading','subheading','listing'):new=gap>17
    elif k=='code':new=gap>42
    elif k=='annotation':new=gap>13 or abs(g['x']-current['x'])>65
    else:new=gap>17 or is_indent
   if new:
    current={'kind':k,'lines':[],'y':g['y'],'x':g['x'],'last_y':g['y'],'bullet':bullet,'indent':is_indent};blocks.append(current)
   current['lines'].append(g);current['last_y']=g['y']
  page_records=[]
  for b in blocks:
   k=b['kind'];text=clean('\n'.join(g['s'] for g in b['lines']))
   record={'type':k,'english':text,'page':pn,'y':b['y'],'indent':b['indent'],'source_runs':[t['run'] for g in b['lines'] for t in g['spans']]}
   if k=='code':
    x0=min(g['x'] for g in b['lines']);code=[]
    for g in b['lines']:
     code.append(' '*max(0,round((g['x']-x0)/4.8))+line_text(g['spans'],True))
    record['code']='\n'.join(code);record['language']='java'
    if re.search(r'^(?:\$ |curl |docker |kubectl |export |java |mvn |npm )',record['code'],re.M):record['language']='bash'
    elif re.match(r'\s*[\[{]',record['code']) and re.search(r'"[^"\n]+"\s*:',record['code']):record['language']='json'
    elif re.match(r'\s*(?:SELECT|UPDATE|CREATE TABLE|DELETE|INSERT|ROLLBACK)\b',record['code']):record['language']='sql'
   elif k=='heading':
    match=re.match(r'^(\d+(?:\.\d+)+)\b',text)
    record['level']=min(3,len(match[1].split('.'))) if match else 3
   elif k in ('subheading','listing'):record['type']='heading';record['level']=4
   if b['bullet']:record['type']='item'
   page_records.append(record)
  for f in figures[pn]:
   page_records.append({'type':'figure','english':'Figure '+f['figure']+' '+f['caption_english'],'figure':f['figure'],'file':'assets/'+f['file'],'page':pn,'y':f['crop_box_pt'][1]})
  page_records+=special_records
  page_records.sort(key=lambda r:(r['y'],0 if r['type']=='figure' else 1))
  records+=page_records
 # Merge page-split prose while leaving figures directly after the completed
 # paragraph. All source text remains represented in source_runs.
 i=1
 while i<len(records):
  r=records[i]
  if r['type']=='prose' and not r.get('indent'):
   j=i-1
   while j>=0 and records[j]['type'] in ('figure','table'):j-=1
   if j>=0 and records[j]['type'] in ('prose','item') and r['page']>max(records[j].get('pages',[records[j]['page']])) and not any(q['page']==r['page'] and q['type'] not in ('figure','table','annotation') for q in records[j+1:i]):
    prev=records[j]
    if records[j+1:i] and re.search(r'[.!?:][”\"]?$',prev['english']):
     i+=1;continue
    prev['english']=clean(prev['english']+'\n'+r['english']);prev.setdefault('pages',[prev['page']]).append(r['page']);prev['source_runs']+=r['source_runs'];records.pop(i);continue
  i+=1
 records=merge_code_continuations(records)
 records=apply_english_overrides(records)
 for i,r in enumerate(records):r['id']=f"u{c['number']:02d}_{i:04d}"
 stats['text_runs_retained']=len(all_runs);stats['records']=len(records)
 return {'chapter':c,'slug':unit_slug(c),'records':records,'statistics':dict(stats)}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--xml',type=Path,default=Path('/tmp/ms_fig_source.xml'));ap.add_argument('--units',default='2,3,4,5,6,7,8,9,10,11,12,13');ap.add_argument('--output',type=Path,default=Path('/tmp/ms_structured'));a=ap.parse_args()
 if not a.xml.exists():
  subprocess.run(['pdftohtml','-xml','-zoom','1','-i','-hidden',str(PDF),str(a.xml)],check=True)
 root=ET.parse(a.xml).getroot()
 global HYPHEN_WORDS
 HYPHEN_WORDS={w.lower() for t in root.iter('text') for w in re.findall(r'[A-Za-z]+(?:-[A-Za-z]+)+',''.join(t.itertext()))}
 pages={int(p.get('number')):p for p in root.findall('page')};fonts={f.get('id'):f.attrib for f in root.iter('fontspec')}
 a.output.mkdir(parents=True,exist_ok=True)
 requested={int(n) for n in a.units.split(',')}
 for c in json.loads((ROOT/'source_map.json').read_text())['chapters']:
  if c['number'] not in requested:continue
  data=extract_chapter(c,pages,fonts);out=a.output/f"unit_{c['number']:02d}.json";out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
  print(c['number'],len(data['records']),collections.Counter(r['type'] for r in data['records']))
if __name__=='__main__':main()
