# -*- coding: utf-8 -*-
"""Réconciliation numérique maquette Word -> classeur Excel (appariement 1:1, un tableau Word par sortie)."""
import json, re, glob, csv
from docx import Document

MAP = [(3,'T10_emd_par_bras'),(4,'T05_dates_collecte'),(5,'T05_dates_collecte'),(6,'T02_realisation_zs'),
 (7,'T01_bilan_appariement'),(8,'T11_profil_menages'),(9,'T12_profil_acteurs'),(10,'T12_profil_acteurs'),
 (11,'T14_cac_3volets'),(12,'T14_cod_3volets'),(13,'T16_categories_organes'),(14,'T20_transitions_matrices'),
 (15,'T21_mouvements_unites'),(17,'T14_reco_3volets'),(18,'T47_reco_professionnalisation_c'),
 (19,'T49_reco_charge_menages'),(20,'T14_asc_3volets'),(21,'T48_asc_prime_montant'),(22,'T50_logistique'),
 (23,'T50_logistique'),(24,'T14_men_3volets'),(25,'T23_repondération_T1'),(26,'T23_repondération_T1'),
 (27,'T25_tableau_des_effets'),(28,'T19_16_zones_P1'),(29,'T19_16_zones_P3'),(30,'T28_placebos'),
 (31,'T27_divergence_tendances'),(32,'T26_unites_appariees'),(33,'T29_effets_secondaires'),
 (35,'T30_differences_premieres_aires'),(36,'T31_associations_transversales'),(37,'T32_variance_niveaux'),
 (38,'T34_capacites_extrants_reco'),(39,'T34_capacites_extrants_reco'),(40,'T35_heterogeneite'),
 (41,'T36_concentration_erreygers'),(42,'T38_genre'),(43,'T38_genre'),(44,'T40_continuum_conditionnel'),
 (45,'T42_enfant_malade_multinomial'),(46,'T43_enfant_malade_deux_parties'),(47,'T44_vaccination_declare_vu'),
 (48,'T46_mpox_acceptabilite'),(49,'T46_mpox_acceptabilite'),(50,'T51_normes_psn'),(51,'T52_indice_conformite'),
 (52,'T52_indice_conformite'),(53,'T54_synthese_sensibilite'),(54,'T53_sensibilite_P1'),
 (55,'T53_sensibilite_P2'),(56,'T53_sensibilite_P3'),(57,'T53_sensibilite_P4'),(63,'T06_fiches_indicateurs'),
 (64,'T07_poids_indices_domaine'),(65,'T08_fiabilite_indices'),(66,'T09_irt_signes_danger'),
 (67,'T03_asc_couverture'),(68,'T04_qualite_manquants'),(69,'T55_manquants_primaires'),
 (70,'T15_men_3volets_province'),(71,'T19_16_zones_P2'),(72,'T19_16_zones_P4'),
 (73,'T39_continuum_maternel'),(74,'T45_mpox_cap'),(76,'T17_ucodesa')]

NUM = re.compile(r'-?\d+(?:[.,]\d+)?')
def nums(cell):
    t = str(cell).replace('\u00a0',' ').replace('−','-').replace('–','-')
    out=[]
    for m in NUM.findall(t):
        try: out.append(float(m.replace(',','.')))
        except: pass
    return out

X = json.load(open('/home/user/dump.json'))
d = Document(glob.glob('/home/user/Chansons/*.docx')[0])

def caption_of(idx):
    # légende = dernier paragraphe "Tableau N." avant le tableau idx
    from docx.text.paragraph import Paragraph
    body=d.element.body; n=0; cap=''
    for ch in body.iterchildren():
        tag=ch.tag.split('}')[1]
        if tag=='p':
            t=Paragraph(ch,d).text.strip()
            if re.match(r'^Tableau\s+\d+',t): cap=t
        elif tag=='tbl':
            n+=1
            if n==idx: return cap
    return ''

rows=[]
for idx,sheet in MAP:
    t=d.tables[idx-1]
    wrows=[r for r in ([c.text for c in row.cells] for row in t.rows)]
    wnum=[v for r in wrows for v in nums(' | '.join(r))]
    snum=[]
    for r in X[sheet]['rows']:
        snum += nums(' | '.join(str(v) for v in r['cells'].values() if v is not None))
    mism=[]; n=min(len(wnum),len(snum))
    for i in range(n):
        if abs(wnum[i]-snum[i])>0.005: mism.append((i,wnum[i],snum[i]))
    rows.append(dict(idx=idx, sheet=sheet, caption=caption_of(idx)[:80],
        word_rows=len(t.rows), excel_rows=len(X[sheet]['rows']), word_nums=len(wnum), excel_nums=len(snum),
        compared=n, divergent=len(mism), first=mism[:3]))

with open('audit/reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)

bad=[r for r in rows if r['divergent']]
print(f"paires: {len(rows)} | paires divergentes: {len(bad)} | paires conformes: {len(rows)-len(bad)}")
print('désalignements de longueur:',[(r['sheet'],r['word_nums'],r['excel_nums']) for r in rows if r['word_nums']!=r['excel_nums']])
for r in sorted(bad,key=lambda r:-r['divergent'])[:30]:
    print(f"  {r['sheet']:34s} idx{r['idx']:3d} {r['divergent']:3d}/{r['compared']:3d}  {r['first'][:2]}")
