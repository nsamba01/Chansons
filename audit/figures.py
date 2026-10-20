# -*- coding: utf-8 -*-
"""Inventaire des figures : chaque image est rattachée à la légende « Figure N. » qui la suit."""
import glob,re,zipfile,io,csv,xml.etree.ElementTree as ET
from docx import Document
from docx.text.paragraph import Paragraph
from PIL import Image
NS_A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
NS_R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
f=glob.glob('/home/user/Chansons/*.docx')[0]
d=Document(f); body=d.element.body; z=zipfile.ZipFile(f)
rels={r.get('Id'):r.get('Target').split('/')[-1] for r in ET.fromstring(z.read('word/_rels/document.xml.rels'))}
seq=[]
for ch in body.iterchildren():
    tag=ch.tag.split('}')[1]
    if tag=='p':
        imgs=[rels.get(e.get(NS_R+'embed')) for e in ch.iter(NS_A+'blip')]
        imgs=[i for i in imgs if i]
        t=Paragraph(ch,d).text.strip()
        if imgs: seq.append(('img',imgs))
        if re.match(r'^Figure\s+\d+\.',t): seq.append(('cap',t))
        if re.match(r'^Tableau\s+\d+\.',t): seq.append(('tab',t))
pending=[]; figures={}
for kind,val in seq:
    if kind=='img': pending+=val
    elif kind=='cap':
        n=int(re.match(r'^Figure\s+(\d+)',val).group(1))
        figures[n]=(val,pending); pending=[]
media=sorted(n.split('media/')[-1] for n in z.namelist() if n.startswith('word/media/') and n.lower().endswith('.png'))
used=set()
rows=[]
for n in sorted(figures):
    cap,imgs=figures[n]
    if not imgs:
        rows.append(dict(figure=n,caption=cap[:120],media='(aucune image)',wpx=0,hpx=0,dark='',left='',right='',refs=0))
        continue
    for im in imgs:
        used.add(im)
        im0=Image.open(io.BytesIO(z.read('word/media/'+im))); w,h=im0.size
        g=im0.convert('L').crop((0,int(h*0.18),w,h)); px=list(g.getdata())
        dark=sum(1 for p in px if p<128)/len(px)
        a=g.load(); H=g.size[1]
        left=sum(1 for y in range(H) if a[1,y]<160)/H
        right=sum(1 for y in range(H) if a[w-2,y]<160)/H
        rows.append(dict(figure=n,caption=cap[:120],media=im,wpx=w,hpx=h,dark=round(dark,4),
                         left=round(left,3),right=round(right,3),refs=len(imgs)))
with open('/home/user/Chansons/audit/figures.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows:
    print(f"F{r['figure']:>2} x{r['refs']} {r['media'][:16]:16s} {r['wpx']:>4}x{r['hpx']:<5} d={str(r['dark']):<7} l/r={r['left']}/{r['right']:<5} {r['caption'][:78]}")
print('\nimages non référencées:',[m for m in media if m not in used])
print('total PNG:',len(media),'| figures légendées:',len(figures),'| images utilisées dans une figure:',len(used))
