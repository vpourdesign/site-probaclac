# -*- coding: utf-8 -*-
import re,os,json
def g(s,pat):
    m=re.search(pat,s,re.S); return m.group(1).strip() if m else None
def gall(s,pat):
    return [m.strip() for m in re.findall(pat,s,re.S)]
files=sorted(f for f in os.listdir('.') if f.startswith('probiotique-') and f.endswith('.html') and f!='probiotique-adulte.html')
out={}
for f in files:
    s=open(f,encoding='utf-8').read()
    out[f]={
     'h1':g(s,r'<h1>(.*?)</h1>'),
     'formula':g(s,r'<dt>Formule</dt>\s*<dd>(.*?)</dd>'),
     'formats':g(s,r'<dt>Formats disponibles</dt>\s*<dd>(.*?)</dd>'),
     'desc':g(s,r'<p class="pbl-desc">(.*?)</p>'),
     'nonmed':g(s,r'<p class="nonmed">(.*?)</p>'),
     'posology':g(s,r'<h3>Posologie</h3>(.*?)</div>'),
     'studyband':g(s,r'<p class="studyband__txt">(.*?)</p>'),
     'forwhom_title':g(s,r'shead__title" style="margin:0 0 1\.1rem;">(.*?)</h2>'),
     'forwhom_paras':gall(s,r'<p class="mute">(.*?)</p>'),
     'final_h2':g(s,r'font-size:var\(--t-h2\);line-height:1;margin:0 0 1\.2rem;">(.*?)</h2>'),
     'comp_extra':g(s,r'<p class="caphdr-note">(.*?)</p>'),
    }
open('_fr_blocks.json','w',encoding='utf-8').write(json.dumps(out,ensure_ascii=False,indent=1))
print("written",len(files),"files")
# print compact preview
for f,d in out.items():
    print("\n###",f)
    for k,v in d.items():
        if isinstance(v,list): v='|| '.join(v)
        print(f"  [{k}] {str(v)[:160]}")
