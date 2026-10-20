# -*- coding: utf-8 -*-
"""Croquis des figures proposées, tracés avec les valeurs réelles du classeur.

Aucune donnée n'est inventée : chaque croquis porte la source de ses valeurs et
signale en rouge ce que le classeur ne contient pas.
"""
import json, textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

X = json.load(open('/home/user/dump.json'))
OUT = '/home/user/Chansons/audit/croquis'

NAVY='#1F3A5F'; BLEU='#2E6DA4'; ORANGE='#D97B36'; GRIS='#9A9A9A'; ROUGE='#B03A2E'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,
                     'axes.edgecolor':'#CCCCCC','xtick.color':'#333333','ytick.color':'#333333'})

def entete(fig, surtitre, constat, sous_titre=None, width=78):
    fig.text(0.012, 0.965, surtitre, fontsize=8.6, color='#6B6B6B', va='top')
    fig.text(0.012, 0.935, '\n'.join(textwrap.wrap(constat, width)), fontsize=11.5,
             fontweight='bold', color=NAVY, va='top', linespacing=1.25)
    if sous_titre:
        fig.text(0.012, 0.845, '\n'.join(textwrap.wrap(sous_titre, 110)), fontsize=7.8,
                 color=ROUGE, style='italic', va='top', linespacing=1.3)

def source(fig, txt):
    fig.text(0.012, 0.015, '\n'.join(textwrap.wrap(txt, 118)), fontsize=6.9, color='#6B6B6B', va='bottom')

def style(ax):
    for s in ('top','right'): ax.spines[s].set_visible(False)
    ax.grid(axis='x', color='#EDEDED'); ax.set_axisbelow(True)


# ---------------------------------------------------------------- 1. cascade conditionnelle
def cascade():
    # T40 : probabilités conditionnelles, bras témoin T0
    p = [100.0, 41.5, 39.1, 13.7]           # CPN1, CPN4+|CPN1, structure|CPN4+, CPoN|structure
    etapes = ['CPN1\nau moins une visite', 'CPN4+\nau moins quatre visites',
              'Accouchement\nen structure', 'CPoN\nà six semaines']
    fig = plt.figure(figsize=(7.6, 4.1))
    ax = fig.add_axes([0.24, 0.24, 0.52, 0.55])
    y = np.arange(4)[::-1]
    ax.barh(y, p, height=0.58, color=[NAVY, BLEU, BLEU, '#6FA8DC'])
    for k, v in enumerate(p):
        ax.text(v + 1.6, y[k], f'{v:.1f} %', va='center', fontsize=9, color='#333333', fontweight='bold')
    for k in range(3):
        perte = p[k] - p[k+1]
        ax.text(p[k+1] + 1.6, y[k] - 0.5, f'−{perte:.1f} pts', va='center', fontsize=7.4, color=ROUGE)
    ax.set_yticks(y); ax.set_yticklabels(etapes, fontsize=8)
    ax.set_xlim(0, 112); ax.set_xlabel('% des femmes encore présentes dans la cascade')
    style(ax)
    entete(fig, 'Figure 15 (proposition) — cascade maternelle conditionnelle, bras témoin à T0',
           "De la première consultation à la visite postnatale, la cascade perd 86 % de son effectif",
           "Écart à documenter : la co-couverture publiée (16,7 %) ne se déduit pas du produit des trois conditionnelles (13,7 %).")
    source(fig, "Source : T40_continuum_conditionnel (bras témoin, T0) : 41,5 % × 94,3 % × 35,0 %. Les cascade par bras, passage et province restent à produire (T39 ne fournit que 4 étapes marginales, non emboîtées).")
    fig.savefig(f'{OUT}/fig15_cascade.png', dpi=200, bbox_inches=None); plt.close(fig)


# ---------------------------------------------------------------- 2. normes PSN
def normes():
    rows=[r['cells'] for r in X['T51_normes_psn']['rows'][1:]]
    lab=[c['A'].replace(' (cible 50 %)','') for c in rows]
    t0=[c['E'] for c in rows]; t1=[c['F'] for c in rows]
    order=sorted(range(len(rows)), key=lambda k: -(t1[k]-t0[k]))
    n=len(rows); ypos={k: n-1-i for i,k in enumerate(order)}
    fig=plt.figure(figsize=(7.8,6.0))
    ax=fig.add_axes([0.40,0.16,0.56,0.62])
    for k in order:
        y=ypos[k]
        ax.plot([t0[k],t1[k]],[y,y], color='#DEDEDE', lw=3.6, zorder=1, solid_capstyle='round')
    ax.scatter([t0[k] for k in order],[ypos[k] for k in order], s=32, facecolor='white',
               edgecolor=BLEU, lw=1.4, zorder=3, label='T0')
    ax.scatter([t1[k] for k in order],[ypos[k] for k in order], s=32, color=BLEU, zorder=3, label='T1')
    ax.axvline(50, color=ROUGE, lw=0.9, ls=(0,(4,3)), zorder=2)
    ax.set_yticks([ypos[k] for k in order]); ax.set_yticklabels([lab[k] for k in order], fontsize=7.0)
    ax.set_xlim(0,100); ax.set_ylim(-0.8, n-0.2); ax.set_xlabel("% d'unités conformes", labelpad=14)
    style(ax)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([],[],marker='o',ls='',mfc='white',mec=BLEU,label='T0'),
                       Line2D([],[],marker='o',ls='',color=BLEU,label='T1'),
                       Line2D([],[],color=ROUGE,ls=(0,(4,3)),label='Cible 50 % (2 normes)')],
              ncol=1,fontsize=7.2,frameon=False,loc='lower right',bbox_to_anchor=(1.0,0.02))
    entete(fig,'Figure 2 (proposition) — normes du PSN SACO, bras intervention',
           "La conformité progresse sur la désignation et les réunions, stagne sur la prime, le contrat et les dotations",
           "18 normes sur 20 n'ont aucune cible chiffrée : elles décrivent un niveau sans imposer de seuil.")
    source(fig,"Source : T51_normes_psn (20 normes, bras intervention T0 → T1), classées par progression de T0 à T1. La série témoin, présente dans la figure 2 de la maquette, n'est pas retracée ici.")
    fig.savefig(f'{OUT}/fig02_normes.png', dpi=200); plt.close(fig)


# ---------------------------------------------------------------- 3. unités par zone
def unites():
    rows=[r['cells'] for r in X['T22_unites_progression_regressi']['rows'][1:]]
    prov={c['C']:c['B'] for c in rows}
    agg={}
    for c in rows:
        d=agg.setdefault(c['C'],{'Amélioration':0,'Dégradation':0}); d[c['I']]+=1
    zones=sorted(agg, key=lambda z:(prov[z], z))
    n=len(zones)
    fig=plt.figure(figsize=(7.8,5.3))
    ax=fig.add_axes([0.30,0.20,0.62,0.60])
    y=np.arange(n)[::-1]
    prog=np.array([agg[z]['Amélioration'] for z in zones], dtype=float)
    reg=-np.array([agg[z]['Dégradation'] for z in zones], dtype=float)
    ax.barh(y,prog,color=BLEU,height=0.6,label='Progressions')
    ax.barh(y,reg,color=ORANGE,height=0.6,label='Régressions')
    xmax=max(prog.max(), -reg.min())+3.2
    for k,z in enumerate(zones):
        net=int(prog[k]+reg[k])
        ax.text(prog[k]+0.35, y[k], f'{net:+d}', va='center', fontsize=7.4,
                color=BLEU if net>0 else (ORANGE if net<0 else '#666666'), fontweight='bold')
    ax.axvline(0,color='#555555',lw=0.9)
    ax.set_yticks(y); ax.set_yticklabels([f'{z} ({prov[z]})' for z in zones],fontsize=6.8)
    ax.set_xlim(-xmax, xmax); ax.set_ylim(-0.7, n-0.3)
    ax.set_xlabel("Nombre d'unités appariées", labelpad=6)
    ax.tick_params(axis='x', labelsize=7.5)
    style(ax)
    ax.legend(ncol=2,fontsize=7.2,frameon=False,loc='upper center',bbox_to_anchor=(0.42,-0.10))
    entete(fig,'Figure 6 bis (proposition) — mouvements des unités appariées par zone',
           "Neuf zones progressent, cinq reculent, deux stagnent : le solde est positif de 37 unités sur 249",
           "Six zones d'intervention sur huit progressent, contre trois sur huit côté témoin — écart non testé. 5 CAC sur 189 sortent de la grille déclarée.")
    source(fig,"Source : T22_unites_progression_regressi (249 unités : 189 CAC, 60 CODESA). Seuil : un critère = 11,1 pts (CAC, 9 critères) ou 14,3 pts (CODESA).")
    fig.savefig(f'{OUT}/fig06bis_unites.png', dpi=200); plt.close(fig)


# ---------------------------------------------------------------- 4. ménages
def menages():
    rows=[r['cells'] for r in X['T14_men_3volets']['rows'][1:]]
    def get(pref,grp):
        for c in rows:
            if c.get('B','').startswith(pref) and c.get('C')==grp:
                return (float(str(c['D']).split()[0].replace(',','.')),
                        float(str(c['F']).split()[0].replace(',','.')))
        return None
    inds=[("Indice d'exposition",'Exposition aux agents'),('Indice de connaissances des ménages','Connaissances'),
          ('Connaît le COSA','Connaît le COSA'),('A reçu une visite','Visite à domicile'),
          ('Enfant vacciné déclaré','Enfant vacciné'),('Carnet de vaccination vu','Carnet vu'),
          ('Amène les enfants à la pesée','Pesée'),('Se lave les mains','Lavage des mains'),
          ('Connaît la Mpox','Connaît la Mpox'),('Accepterait le vaccin','Accepterait le vaccin'),
          ('Au moins quatre CPN','Au moins 4 CPN'),('Accouchement en structure','Accouchement struct.')]
    fig=plt.figure(figsize=(7.6,4.7))
    ax=fig.add_axes([0.26,0.22,0.70,0.58])
    y=np.arange(len(inds))[::-1]
    for k,(pref,lab) in enumerate(inds):
        a=get(pref,'Témoin'); b=get(pref,'Intervention')
        if not a or not b: continue
        ax.plot([a[0],a[1]],[y[k]+0.17]*2,color=ORANGE,lw=1.7,solid_capstyle='round')
        ax.scatter([a[0],a[1]],[y[k]+0.17]*2,s=20,facecolor='none',edgecolor=ORANGE,lw=1.2,zorder=3)
        ax.plot([b[0],b[1]],[y[k]-0.17]*2,color=BLEU,lw=1.7,solid_capstyle='round')
        ax.scatter([b[0],b[1]],[y[k]-0.17]*2,s=20,color=BLEU,zorder=3)
    ax.set_yticks(y); ax.set_yticklabels([l for _,l in inds],fontsize=7.6)
    ax.set_xlabel('Valeur (%) — T0 (évidé, à gauche) → T1 (plein, à droite)', labelpad=6); ax.set_xlim(0,100); ax.set_ylim(-1.2, len(inds)-0.4)
    style(ax)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([],[],color=ORANGE,label='Témoin'),Line2D([],[],color=BLEU,label='Intervention')],
              ncol=2,fontsize=7.4,frameon=False,loc='upper center',bbox_to_anchor=(0.5,-0.13))
    entete(fig,'Figure 7 bis (proposition) — douze indicateurs ménages, T0 → T1 par bras',
           "Les deux bras progressent sur presque tous les indicateurs ; aucun écart ne se détache",
           "Le tableau 18 publie 96 lignes : ces douze indicateurs suffisent à porter le message du chapitre.")
    source(fig,"Source : T14_men_3volets (96 lignes → 12 indicateurs retenus ; les 20 autres vont en annexe D). Aucune valeur modifiée.")
    fig.savefig(f'{OUT}/fig07bis_menages.png', dpi=200); plt.close(fig)


# ---------------------------------------------------------------- 5. matrice zones
def matrice():
    sheets=['T19_16_zones_P1','T19_16_zones_P2','T19_16_zones_P3','T19_16_zones_P4']
    cols=['P1\nExposition','P2\nConnaissances','P3\nCAC','P4\nRECO']
    data=[]; zones=None
    for sh in sheets:
        rows=[r['cells'] for r in X[sh]['rows'][1:]]
        if zones is None: zones=[(c['B'],c['C'],c['A']) for c in rows]
        data.append([float(c['H']) for c in rows])
    M=np.array(data).T
    fig=plt.figure(figsize=(6.6,5.2))
    ax=fig.add_axes([0.30,0.16,0.58,0.62])
    im=ax.imshow(M,cmap='RdBu_r',vmin=-18,vmax=18,aspect='auto')
    ax.set_xticks(range(4)); ax.set_xticklabels(cols,fontsize=7.8)
    ax.set_yticks(range(len(zones))); ax.set_yticklabels([f'{z[0]} · {z[2][:9]}' for z in zones],fontsize=7.0)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(j,i,f'{M[i,j]:+.0f}',ha='center',va='center',fontsize=6.6,
                    color='white' if abs(M[i,j])>11 else '#333333')
    cb=fig.colorbar(im,ax=ax,fraction=0.036,pad=0.02); cb.set_label('Évolution brute (points)',fontsize=7.4)
    cb.ax.tick_params(labelsize=7)
    entete(fig,'Figure 10 bis (proposition) — matrice des seize zones, quatre primaires',
           "Deux zones progressent sur les quatre primaires, aucune ne recule sur les quatre",
           "La dispersion est inter-zone, non inter-bras. Cette matrice remplace les deux tableaux de zone du corps (T 21 et T 22) et sert de sommaire aux seize fiches.",
           width=64)
    source(fig,"Source : T19_16_zones_P1 à P4, colonne « évolution brute ». Le détail chiffré reste en annexe D ; les fiches de zone conservent le détail local.")
    fig.savefig(f'{OUT}/fig10bis_matrice.png', dpi=200); plt.close(fig)


# ---------------------------------------------------------------- 6. écart déclaré - carnet vu
def ecart_vacc():
    rows=[r['cells'] for r in X['T44_vaccination_declare_vu']['rows'][1:]]
    prov=['Maniema','Kasaï-Oriental','Sankuru','Sud-Kivu']
    def val(pv,br,ps):
        for c in rows:
            if c['A']==pv and c['B']==br and c['C']==ps: return float(c['F'])
    fig=plt.figure(figsize=(7.4,4.6))
    ax=fig.add_axes([0.16,0.18,0.74,0.46])
    y=np.arange(4)[::-1]
    serie=[('Témoin',ORANGE,ROUGE,0.16),('Intervention','#7FA8C9',NAVY,-0.16)]
    for lbl,c0,c1,off in serie:
        for k in range(4):
            v0=val(prov[k],lbl,'T0'); v1=val(prov[k],lbl,'T1')
            ax.annotate('',xy=(v1,y[k]+off),xytext=(v0,y[k]+off),
                        arrowprops=dict(arrowstyle='-|>',color=c1,lw=1.1,alpha=.8,shrinkA=4,shrinkB=4))
            ax.scatter([v0],[y[k]+off],s=30,color=c0,zorder=3)
            ax.scatter([v1],[y[k]+off],s=34,color=c1,zorder=3)
            ax.text(v0-0.9,y[k]+off+0.10,f'{v0:.1f}',ha='right',va='bottom',fontsize=6.7,color='#555555')
            ax.text(v1+0.9,y[k]+off-0.10,f'{v1:.1f}',ha='left',va='top',fontsize=6.7,color=c1,fontweight='bold')
    ax.set_yticks(y); ax.set_yticklabels(prov,fontsize=8.4)
    ax.set_xlim(-3,63); ax.set_xticks([0,10,20,30,40,50,60])
    ax.set_xlabel("Écart « déclaré − carnet vu » (points de %) ; la flèche va de T0 à T1")
    style(ax)
    from matplotlib.lines import Line2D
    fig.legend(handles=[Line2D([],[],marker='o',ls='',color=ORANGE,label='Témoin, T0'),
                        Line2D([],[],marker='o',ls='',color=ROUGE,label='Témoin, T1'),
                        Line2D([],[],marker='o',ls='',color='#7FA8C9',label='Intervention, T0'),
                        Line2D([],[],marker='o',ls='',color=NAVY,label='Intervention, T1')],
               loc='upper left',bbox_to_anchor=(0.16,0.735),ncol=4,frameon=False,fontsize=7.2,
               handletextpad=0.2,columnspacing=1.4)
    entete(fig,"Figure 17 bis (proposition) — écart entre vaccination déclarée et carnet vu, par province",
           "La déclaration progresse plus vite que la preuve documentaire, dans les deux bras",
           "Ensemble : l'écart passe de 31,4 à 38,9 pts (témoin) et de 26,2 à 32,6 pts (intervention). Au Sud-Kivu témoin, 54,7 pts à T1.",
           width=70)
    source(fig,"Source : T44_vaccination_declare_vu, colonne « écart déclaré - vu » (4 provinces × 2 bras × 2 passages). Cinq lignes présentent un écart d'arrondi de 0,1 pt : l'écart est calculé avant arrondi des composantes.")
    fig.savefig(f'{OUT}/fig17bis_ecart_vacc.png',dpi=200); plt.close(fig)


for f in (cascade,normes,unites,menages,matrice,ecart_vacc):
    f(); print('ok',f.__name__)
