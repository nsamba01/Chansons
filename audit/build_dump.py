# -*- coding: utf-8 -*-
"""Reconstruit dump.json (78 onglets) à partir du classeur SACO Phase 2.

Le classeur livré contient une dimension déclarée A1 sur toutes les feuilles et
référence une partie de dessin absente (xl/drawings/drawing1.xml), ce qui fait
échouer openpyxl en lecture directe. On reconstruit une copie propre dans un
répertoire temporaire, en retirant les références aux dessins manquants, puis on
extrait toutes les cellules.
"""
import json, os, re, shutil, sys, tempfile, zipfile
from openpyxl import load_workbook

SRC = '/home/user/Chansons/SACO_Phase2_Tableaux_2026-10-15 (2).xlsx'
OUT = '/home/user/dump.json'


def clean_copy(src, dst):
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(src) as z:
        names = z.namelist()
        z.extractall(tmp)
    # supprimer les relations vers des dessins absents
    rels = os.path.join(tmp, 'xl', '_rels', 'workbook.xml.rels')
    for root, _, files in os.walk(tmp):
        for f in files:
            if f.endswith('.rels'):
                p = os.path.join(root, f)
                txt = open(p, encoding='utf-8').read()
                new = re.sub(r'<Relationship[^>]*drawings/drawing\d+\.xml"[^>]*/>', '', txt)
                if new != txt:
                    open(p, 'w', encoding='utf-8').write(new)
    # retirer les balises de dessin dans les feuilles
    for name in names:
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            p = os.path.join(tmp, name)
            txt = open(p, encoding='utf-8').read()
            new = re.sub(r'<drawing[^>]*/>', '', txt)
            if new != txt:
                open(p, 'w', encoding='utf-8').write(new)
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(tmp):
            for f in files:
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, tmp))
    shutil.rmtree(tmp)


def main():
    dst = '/tmp/saco_clean.xlsx'
    clean_copy(SRC, dst)
    wb = load_workbook(dst, data_only=True)
    dump = {}
    for ws in wb.worksheets:
        rows = []
        for row in ws.iter_rows():
            cells = {}
            for c in row:
                if c.value is not None:
                    v = c.value
                    cells[c.column_letter] = v.isoformat() if hasattr(v, 'isoformat') else v
            if cells:
                rows.append({'row': row[0].row, 'cells': cells})
        dump[ws.title] = {'max_row': ws.max_row, 'max_col': ws.max_column, 'rows': rows}
    json.dump(dump, open(OUT, 'w'), ensure_ascii=False, default=str)
    print(f'{len(dump)} onglets -> {OUT}')


if __name__ == '__main__':
    main()
