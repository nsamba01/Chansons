# -*- coding: utf-8 -*-
"""Convertit les fichiers Markdown de recommandations éditoriales en DOCX.

Reprend la mise en forme de la maquette du rapport (A4, marges 2 cm,
Calibri 10 pt, interligne 1,08, titres bleu nuit) et ajoute la gestion des
images insérées en pleine largeur.
"""
import re, os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = '/home/user/Chansons'
PARTS = [f'{ROOT}/audit/editorial/doc_p{i}.md' for i in range(6)]
OUT = f'{ROOT}/Propositions_editoriales_rapport_SACO_Phase2_2026-10-20.docx'

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2.0)
sec.top_margin = sec.bottom_margin = Cm(2.0)

st = doc.styles['Normal']
st.font.name = 'Calibri'; st.font.size = Pt(10)
st.paragraph_format.space_after = Pt(4)
st.paragraph_format.line_spacing = 1.08

for name, size, color in (('Heading 1', 17, (0x1F, 0x3A, 0x5F)),
                          ('Heading 2', 13, (0x1F, 0x3A, 0x5F)),
                          ('Heading 3', 11.5, (0x2E, 0x4E, 0x73))):
    s = doc.styles[name]
    s.font.name = 'Calibri'; s.font.size = Pt(size); s.font.bold = True
    s.font.color.rgb = RGBColor(*color)
    s.paragraph_format.space_before = Pt(14); s.paragraph_format.space_after = Pt(6)
    s.paragraph_format.keep_with_next = True

# pied de page : titre court + numéro
footer = sec.footer.paragraphs[0]
footer.text = 'Propositions éditoriales — rapport quantitatif SACO Phase 2 — 20 octobre 2026'
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
for r in footer.runs:
    r.font.size = Pt(8); r.font.color.rgb = RGBColor(0x6B, 0x6B, 0x6B)

INLINE = re.compile(r'(\*\*[^*]+\*\*|`[^`]+`|(?<!\*)\*[^*]+\*(?!\*))')


def add_runs(par, text):
    for tok in INLINE.split(text):
        if not tok:
            continue
        if tok.startswith('**') and tok.endswith('**'):
            r = par.add_run(tok[2:-2]); r.bold = True
        elif tok.startswith('`') and tok.endswith('`'):
            r = par.add_run(tok[1:-1]); r.font.name = 'Consolas'; r.font.size = Pt(8.5)
        elif tok.startswith('*') and tok.endswith('*') and len(tok) > 2:
            r = par.add_run(tok[1:-1]); r.italic = True
        else:
            par.add_run(tok)


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hexcolor)
    tcPr.append(shd)


def add_table(rows):
    header = [c.strip() for c in rows[0].strip('|').split('|')]
    body = [[c.strip() for c in line.strip('|').split('|')] for line in rows[2:]]
    ncol = len(header)
    t = doc.add_table(rows=1, cols=ncol)
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.rows[0].cells
    for i, h in enumerate(header):
        hdr[i].text = ''
        p = hdr[i].paragraphs[0]
        r = p.add_run(h.replace('**', '')); r.bold = True; r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        p.paragraph_format.space_after = Pt(1)
        shade(hdr[i], '1F3A5F')
    for j, row in enumerate(body):
        cells = t.add_row().cells
        for i in range(ncol):
            val = row[i] if i < len(row) else ''
            cells[i].text = ''
            p = cells[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(1)
            add_runs(p, val)
            for r in p.runs:
                if r.font.size is None:
                    r.font.size = Pt(8)
            if j % 2 == 1:
                shade(cells[i], 'F2F5F9')
    doc.add_paragraph()


def add_figure(cap, path):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(path, width=Cm(16.4))
    c = doc.add_paragraph()
    c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c.paragraph_format.space_after = Pt(10)
    r = c.add_run(cap)
    r.italic = True; r.font.size = Pt(8.5); r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)


IMG = re.compile(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$')
first_h1 = True
for path in PARTS:
    lines = open(path, encoding='utf-8').read().split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1; continue
        m = IMG.match(line.strip())
        if m:
            img = m.group(2)
            img = img if os.path.isabs(img) else os.path.join(ROOT, img)
            add_figure(m.group(1), img)
            i += 1; continue
        if line.startswith('|'):
            block = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                block.append(lines[i].strip()); i += 1
            if len(block) >= 2:
                add_table(block)
            continue
        if line.startswith('### '):
            doc.add_heading(re.sub(r'\*\*', '', line[4:].strip()), level=3)
        elif line.startswith('## '):
            doc.add_heading(re.sub(r'\*\*', '', line[3:].strip()), level=2)
        elif line.startswith('# '):
            if not first_h1:
                doc.add_page_break()
            first_h1 = False
            doc.add_heading(re.sub(r'\*\*', '', line[2:].strip()), level=1)
        elif line.startswith('---'):
            pass
        elif line.startswith('> '):
            txt = line[2:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.4)
            p.paragraph_format.space_before = Pt(8)
            add_runs(p, txt)
            for r in p.runs:
                r.bold = True; r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)
        elif line.startswith('- '):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(2)
            add_runs(p, line[2:].strip())
        elif re.match(r'^\d+\.\s', line):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6)
            p.paragraph_format.first_line_indent = Cm(-0.6)
            p.paragraph_format.space_after = Pt(3)
            add_runs(p, line.strip().replace('. ', '.  ', 1))
        else:
            p = doc.add_paragraph()
            if line.startswith('*') and line.endswith('*') and not line.startswith('**'):
                p.paragraph_format.left_indent = Cm(0.3)
            add_runs(p, line)
        i += 1

doc.save(OUT)
print('écrit', OUT)
