# -*- coding: utf-8 -*-
"""Figures du rapport final, dans la langue graphique de la maquette.

Trois opérations :
  1. retitrer les figures du modèle dont le titre débordait ou affirmait un
     constat que les données ne portent pas (on recouvre la bande de titre et
     on redessine un titre conforme) ;
  2. produire les figures que le modèle ne fournissait pas ou fournissait vides
     (cascade maternelle, unités par zone, indicateurs ménages, matrice des zones) ;
  3. préparer la page de garde (mention « rapport final », date, statut).

Toutes les valeurs tracées proviennent de /home/user/dump.json.
"""
import io, json, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = '/home/user/Chansons/audit/final/fig'
os.makedirs(OUT, exist_ok=True)
IMGDIR = '/tmp/img'
X = json.load(open('/home/user/dump.json'))

NAVY = '#0B1F3A'
BLEU = '#1B63C4'
CYAN = '#22B8CF'
ORANGE = '#E1701A'
GRIS = '#8C929B'
ROUGE = '#B03A2E'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9,
                     'axes.edgecolor': '#DDE3EA', 'xtick.color': '#33404F',
                     'ytick.color': '#33404F', 'text.color': '#0B1F3A'})


def band(fig, x0=0.0, x1=1.0):
    """Bandeau dégradé en tête de figure, comme dans la maquette."""
    grad = np.linspace(0, 1, 256).reshape(1, -1)
    ax = fig.add_axes([x0, 0.975, x1 - x0, 0.025], zorder=0)
    ax.imshow(grad, aspect='auto', cmap=matplotlib.colors.LinearSegmentedColormap.from_list(
        'b', ['#0B1F3A', '#2E74B5', '#22B8CF']))
    ax.set_xticks([]); ax.set_yticks([])


def titres(fig, titre, sous=None, y=0.955, w=72):
    """Titre-constat sur deux lignes, sur-titre explicatif en dessous."""
    import textwrap
    tl = textwrap.wrap(titre, w)
    fig.text(0.015, y, '\n'.join(tl), fontsize=11.8, fontweight='bold',
             color=NAVY, va='top', linespacing=1.25)
    if sous:
        yy = y - 0.055 * len(tl) - 0.012
        fig.text(0.015, yy, '\n'.join(textwrap.wrap(sous, 116)), fontsize=7.4,
                 color=ROUGE, style='italic', va='top', linespacing=1.3)


def source(fig, txt):
    import textwrap
    fig.text(0.012, 0.012, '\n'.join(textwrap.wrap(txt, 120)), fontsize=6.6, color='#6B7280', va='bottom')


def style(ax, grid='x'):
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.grid(axis=grid, color='#EDF0F3')
    ax.set_axisbelow(True)


# ------------------------------------------------------------------ 1. retitrage
def retitle(src, dst, lines, box, fontsize=26, color=(11, 31, 58)):
    """Recouvre le strict bloc de titre (box = y0, y1) et redessine un titre."""
    im = Image.open(src).convert('RGB')
    d = ImageDraw.Draw(im)
    y0, y1 = box
    d.rectangle((0, y0, im.size[0], y1), fill=(255, 255, 255))
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', fontsize)
    y = y0 + 4
    for line in lines:
        d.text((44, y), line, font=font, fill=color)
        y += int(fontsize * 1.30)
    im.save(dst)


# ------------------------------------------------------------------ 2. figures neuves
def cascade():
    c = {}
    for r in X['T40_continuum_conditionnel']['rows'][1:]:
        k = r['cells']
        c[(k['A'], k['B'])] = tuple(float(k[x]) for x in 'CDEF')
    a, b, cc, co = c[('Témoin', 'T0')]
    vals = [100.0, a, a * b / 100, a * b / 100 * cc / 100, co]
    etapes = ["Au moins une CPN\n(base de la cascade)", 'Au moins quatre CPN',
              'Accouchement en structure', 'Consultation postnatale\n(produit des étapes)',
              'Les quatre étapes chez\nla même femme (mesure directe)']
    fig = plt.figure(figsize=(7.4, 5.0))
    band(fig)
    ax = fig.add_axes([0.30, 0.175, 0.52, 0.50])
    y = np.arange(5)[::-1]
    cols = ['#0B1F3A', '#2E74B5', '#4A90D9', '#7FB2E5', '#22B8CF']
    ax.barh(y, vals, height=0.58, color=cols)
    for k, v in enumerate(vals):
        ax.text(v + 2, y[k], f'{v:.1f} %', va='center', fontsize=8.6, fontweight='bold')
    for k in range(3):
        ax.text(vals[k] + 2, y[k] - 0.40, f'−{vals[k]-vals[k+1]:.1f} pts', va='center',
                fontsize=6.6, color=ROUGE)
    ax.set_yticks(y); ax.set_yticklabels(etapes, fontsize=7.4)
    ax.set_xlim(0, 122)
    ax.set_xlabel('% des femmes ayant eu une dernière grossesse', labelpad=8, fontsize=8)
    style(ax)
    titres(fig, "La cascade maternelle perd plus de huit femmes sur dix ; le produit des étapes "
                "sous-estime la co-couverture mesurée",
           "Bras témoin à T0. Les étapes intermédiaires sont conditionnelles à la précédente ; "
           "la co-couverture des quatre étapes sur les mêmes femmes est mesurée à 16,7 %, "
           "contre 13,7 % pour le produit.", w=72)
    source(fig, "Source : T40_continuum_conditionnel, bras témoin à T0. La cascade conditionnelle "
                "et la co-couverture ne mesurent pas la même chose : la première isole chaque "
                "transition, la seconde exige les quatre chez la même femme. Les deux sont publiées.")
    fig.savefig(f'{OUT}/fig15_cascade.png', dpi=200); plt.close(fig)


def menages():
    rows = [r['cells'] for r in X['T14_men_3volets']['rows'][1:]]
    garde = ["Indice d'exposition des ménages aux agents (0-100)",
             "Indice de connaissances des ménages (0-100)",
             "Connaît le COSA et les agents (%)",
             "A reçu une visite à domicile (%)",
             "Enfant vacciné déclaré (%)",
             "Carnet de vaccination vu, tous ménages (%)",
             "Amène les enfants à la pesée (%)",
             "Se lave les mains à l'eau et au savon (%)",
             "Connaît la Mpox (%)",
             "Accepterait le vaccin Mpox (%)",
             "Au moins quatre CPN (%)",
             "Accouchement en structure de santé (%)"]
    court = {'en': ['Exposition aux agents', 'Connaissances', 'Connaît le COSA',
                    'Visite à domicile', 'Enfant vacciné (déclaré)', 'Carnet vu (tous ménages)',
                    'Pesée', 'Lavage des mains', 'Connaît la Mpox',
                    'Accepterait le vaccin', 'Au moins 4 CPN', 'Accouchement en structure'],
             'fr': []}
    def val(ind, grp, per):
        for c in rows:
            if c.get('B') == ind and c.get('C') == grp:
                v = c.get('D' if per == 'T0' else 'F')
                return float(str(v).split()[0].replace(',', '.'))
    fig = plt.figure(figsize=(7.4, 5.1))
    band(fig)
    ax = fig.add_axes([0.255, 0.175, 0.55, 0.50])
    y = np.arange(len(garde))[::-1]
    for k, ind in enumerate(garde):
        for grp, col, off in (('Témoin', ORANGE, 0.17), ('Intervention', BLEU, -0.17)):
            v0, v1 = val(ind, grp, 'T0'), val(ind, grp, 'T1')
            ax.annotate('', xy=(v1, y[k] + off), xytext=(v0, y[k] + off),
                        arrowprops=dict(arrowstyle='-|>', color=col, lw=1.0,
                                        alpha=.75, shrinkA=3, shrinkB=3))
            ax.scatter([v0], [y[k] + off], s=20, facecolor='white', edgecolor=col, lw=1.1, zorder=3)
            ax.scatter([v1], [y[k] + off], s=24, color=col, zorder=3)
    ax.set_yticks(y); ax.set_yticklabels(court['en'], fontsize=7.6)
    ax.set_xlim(0, 100); ax.set_xlabel('Valeur observée (%) ; la flèche va de T0 à T1', labelpad=6)
    style(ax)
    from matplotlib.lines import Line2D
    fig.legend(handles=[Line2D([], [], marker='o', ls='', mfc='white', mec=ORANGE, label='Témoin à T0'),
                        Line2D([], [], marker='o', ls='', color=ORANGE, label='Témoin à T1'),
                        Line2D([], [], marker='o', ls='', mfc='white', mec=BLEU, label='Intervention à T0'),
                        Line2D([], [], marker='o', ls='', color=BLEU, label='Intervention à T1')],
               loc='upper left', bbox_to_anchor=(0.255, 0.745), ncol=4, frameon=False,
               fontsize=7.0, handletextpad=0.2, columnspacing=1.2)
    titres(fig, "Les deux bras progressent sur presque tous les indicateurs : \"carnet vu\" est le "
                "seul qui recule nettement dans le bras intervention",
           "Douze indicateurs retenus sur les 32 du chapitre 5 ; le détail complet figure au tableau 21.",
           w=72)
    source(fig, "Source : T14_men_3volets, groupes Témoin et Intervention. Aucune valeur modifiée ; "
                )
    fig.savefig(f'{OUT}/fig07bis_menages.png', dpi=200); plt.close(fig)


def unites():
    rows = [{a: b for a, b in r['cells'].items()} for r in X['T22_unites_progression_regressi']['rows'][1:]]
    z = {}
    for r in rows:
        k = (r['C'], r['D'])
        z.setdefault(k, [0, 0])
        z[k][0 if r['I'] == 'Amélioration' else 1] += 1
    keys = sorted(z, key=lambda k: -(z[k][0] - z[k][1]))
    fig = plt.figure(figsize=(7.4, 5.15))
    band(fig)
    ax = fig.add_axes([0.20, 0.155, 0.66, 0.53])
    y = np.arange(len(keys))[::-1]
    for i, k in enumerate(keys):
        a, b = z[k]
        ax.barh(y[i], a, height=0.6, color=BLEU)
        ax.barh(y[i], -b, height=0.6, color=ORANGE)
        ax.text(a + 0.4, y[i], f'+{a}', va='center', fontsize=6.6, color=BLEU)
        ax.text(-b - 0.4, y[i], f'−{b}', va='center', ha='right', fontsize=6.6, color=ORANGE)
        ax.text(-15.6, y[i], ('I' if k[1] == 'Intervention' else 'T'),
                va='center', ha='left', fontsize=6.0, color='#8A8F98', style='italic')
    ax.set_yticks(y); ax.set_yticklabels([k[0] for k in keys], fontsize=7.4)
    ax.axvline(0, color='#0B1F3A', lw=0.8)
    ax.set_xlim(-17.5, 20); ax.set_xlabel("Nombre d'unités appariées : progression (bleu) / régression (orange) ; T = témoin, I = intervention", labelpad=7)
    style(ax)
    titres(fig, "Neuf zones sur seize progressent, cinq reculent : le mouvement est général et il "
                "n'est pas propre aux zones d'intervention",
           "249 unités appariées : 143 en progression, 106 en régression, solde +37. "
           "70 contre 45 côté intervention, 73 contre 61 côté témoin — écart non testé.",
           w=74)
    source(fig, "Source : T22_unites_progression_regressi (249 unités appariées CAC et villages). "
                "Le seuil de mouvement est de ± 11,1 points, soit un critère sur neuf. "
                "Le détail par zone figure au tableau 46.")
    fig.savefig(f'{OUT}/fig06bis_unites.png', dpi=200); plt.close(fig)


def matrice():
    sh = ['T19_16_zones_P1', 'T19_16_zones_P2', 'T19_16_zones_P3', 'T19_16_zones_P4']
    data, zones = [], None
    for s in sh:
        rows = [r['cells'] for r in X[s]['rows'][1:]]
        if zones is None:
            zones = [(c['B'], c['C'], c['D']) for c in rows]
        data.append([float(c['H']) for c in rows])
    M = np.array(data).T
    fig = plt.figure(figsize=(6.9, 5.9))
    band(fig)
    ax = fig.add_axes([0.30, 0.175, 0.55, 0.575])
    im = ax.imshow(M, cmap='RdBu_r', vmin=-18, vmax=18, aspect='auto')
    ax.set_xticks(range(4))
    ax.set_xticklabels(['P1\nExposition', 'P2\nConnaissances', 'P3\nCAC', 'P4\nRECO'], fontsize=7.6)
    ax.set_yticks(range(len(zones)))
    ax.set_yticklabels([f'{z[1]} · {z[0]}' for z in zones], fontsize=6.8)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(j, i, f'{M[i, j]:+.0f}'.replace('-', '−'), ha='center', va='center', fontsize=6.4,
                    color='white' if abs(M[i, j]) > 11 else '#33404F')
    cb = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02)
    cb.set_label('Évolution brute, en points', fontsize=7)
    cb.ax.tick_params(labelsize=6.5)
    titres(fig, "Deux zones progressent sur les quatre primaires, aucune ne recule sur les quatre",
           "L'écart se lit entre zones, non entre bras : Katako Kombe et Minga progressent partout, "
           "Kalima et Tshishimbi reculent sur trois primaires.", w=64)
    source(fig, "Source : T19_16_zones_P1 à P4, colonne « évolution brute ». Le détail chiffré par "
                "zone figure en annexe D ; les fiches de l'annexe E conservent le détail local.")
    fig.savefig(f'{OUT}/fig10bis_matrice.png', dpi=200); plt.close(fig)


# ------------------------------------------------------------------ 3. page de garde
def cover():
    im = Image.open(f'{IMGDIR}/b000.png').convert('RGB')
    W, H = im.size
    d = ImageDraw.Draw(im)
    # badge « Phase 2 · Modèle de rapport » : on repeint le dégradé puis le texte
    x0, x1, y0, y1 = 130, 745, 952, 1032
    for x in range(x0, x1):
        t = (x - x0) / (x1 - x0)
        c = (int(45 + 12 * t), int(122 + 74 * t), int(224 + 20 * t))
        d.line([(x, y0), (x, y1)], fill=c)
    f1 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 42)
    d.text((170, 962), 'Phase 2 · Rapport final', font=f1, fill=(255, 255, 255))
    # mention de statut en bas de couverture
    d.rectangle((380, 2440, 1420, 2492), fill=(255, 255, 255))
    f2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)
    txt = 'Version finale · 21 octobre 2026'
    w = d.textlength(txt, font=f2)
    d.text(((1819 - w) / 2, 2448), txt, font=f2, fill=(107, 114, 128))
    im.save(f'{OUT}/cover.png')
    # bandeaux de chapitre : on garde ceux du modèle
    return im.size


if __name__ == '__main__':
    cover()
    retitle(f'{IMGDIR}/b021.png', f'{OUT}/fig02_normes.png',
            ["Normes du PSN SACO : la conformité progresse sur la désignation et les",
             "réunions, stagne sur la prime, le contrat et les dotations"], (100, 216), 26)
    retitle(f'{IMGDIR}/b089.png', f'{OUT}/fig05_codesa.png',
            ["CODESA : la plupart des aires restent dans leur catégorie",
             "et les mouvements vont dans les deux sens"], (94, 203), 26)
    retitle(f'{IMGDIR}/b138.png', f'{OUT}/fig08_domaines.png',
            ["Indices de domaine : effets compatibles avec zéro ; l'indice de riposte",
             "Mpox n'est lu qu'en évolution"], (92, 150), 26)
    retitle(f'{IMGDIR}/b198.png', f'{OUT}/fig14_quintiles.png',
            ["Le gradient social est marqué pour l'accouchement en structure ;",
             "les séries de quintiles ne sont pas monotones"], (92, 209), 26)
    cascade(); menages(); unites(); matrice()
    print('figures écrites dans', OUT)
