# -*- coding: utf-8 -*-
"""Carte de pagination estimée et inventaire par chapitre de la maquette.

La maquette ne conserve aucune pagination (aucun w:lastRenderedPageBreak), et
seuls 31 sauts de page explicites marquent les ouvertures de chapitre. La page
de chaque objet est donc estimée par une règle documentée et reproductible :
  - une page « ouvre » sur un saut explicite ;
  - un paragraphe de longueur L consomme L/2900 page (10 pt, interligne 1,08,
    marges 2 cm) ;
  - un tableau consomme (nb lignes)/26 page, minimum 0,25 ;
  - une figure (image) consomme 0,55 page.
Les valeurs sont des estimations d'occupation, pas une pagination Word.
"""
import json, re
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table

DOCX = '/home/user/Chansons/Rapport_resultats_quantitatifs_Phase2_SACO_Mpox_maquette_2026-10-19 (1).docx'
CHARS_PER_PAGE = 2900.0
ROWS_PER_PAGE = 26.0

d = Document(DOCX)
body = d.element.body
page = 1.0
chapter = '(avant-propos)'
tables_total = 0
items = []

def has_page_break(el):
    for br in el.iter(qn('w:br')):
        if br.get(qn('w:type')) == 'page':
            return True
    return False

def has_image(el):
    return any(True for _ in el.iter(qn('a:blip')))

for ch in body.iterchildren():
    tag = ch.tag.split('}')[1]
    if has_page_break(ch):
        page = float(int(page) + 1)

    if tag == 'p':
        p = Paragraph(ch, d)
        txt = p.text.strip()
        style = p.style.name if p.style is not None else ''
        if txt.startswith('Tableau ') and re.match(r'^Tableau\s+\d+\.', txt):
            items.append(dict(kind='tableau', label=txt[:70], page=round(page), chapter=chapter))
        elif txt.startswith('Figure ') and re.match(r'^Figure\s+\d+\.', txt):
            items.append(dict(kind='figure', label=txt[:70], page=round(page), chapter=chapter))
        elif style.startswith('Heading 1'):
            chapter = txt
            items.append(dict(kind='chapitre', label=txt, page=round(page), chapter=txt))
        elif style.startswith('Heading 2'):
            items.append(dict(kind='section', label=txt, page=round(page), chapter=chapter))
        if has_image(ch):
            page += 0.55
        page += len(txt) / CHARS_PER_PAGE
    elif tag == 'tbl':
        t = Table(ch, d)
        rows = len(t.rows)
        page += max(0.25, rows / ROWS_PER_PAGE)
        tables_total += 1

json.dump(items, open('/home/user/Chansons/audit/layout_map.json', 'w'), ensure_ascii=False, indent=1)
print(f'{len(items)} objets repérés, {tables_total} tableaux Word, ~{round(page)} pages estimées')
for it in items:
    if it['kind'] in ('chapitre',):
        print(f"  p.{it['page']:>3}  {it['label'][:70]}")
