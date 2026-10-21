# -*- coding: utf-8 -*-
"""Annexes A à E."""
from base import *
from docx.shared import Pt, Cm


def _f(v, d=1):
    try:
        return f'{float(str(v).replace(",", ".")):.{d}f}'.replace('.', ',')
    except Exception:
        return str(v)


def annexes(doc):
    page_break(doc)
    h1(doc, '', 'Annexes', band=f'{FIG}/bands/b14_annexes.png')
    para(doc, "Les annexes documentent la méthode, les sources et les tableaux de détail. Elles sont conçues "
              "pour être consultées, non pour être lues d'un bout à l'autre : le corps du rapport contient "
              "les résultats nécessaires à l'argument, les annexes contiennent ce qui permet de les vérifier.")

    h2(doc, "Annexe A. Note de méthode : corrections apportées à la version antérieure", number=None)
    para(doc, "Le rapport final reprend la maquette du 19 octobre 2026 et corrige les points relevés par "
              "l'audit du 20 octobre. Ces corrections sont documentées ici, parce qu'aucune valeur n'a été "
              "modifiée en silence : chaque écart entre la maquette et le rapport final est justifié par sa "
              "source.")
    table(doc, "Tableau A1. Corrections apportées et justification",
          ['Objet', 'Maquette', 'Rapport final', 'Justification'],
          [["P1, DiD", "2,9 [−4,4 ; 10,3], p = 0,399", "1,9 [−4,4 ; 8,3], p = 0,506",
            "La valeur de la maquette correspond à la variante d'imputation multiple (T53, ligne "
            "« imputation multiple »), non à l'estimation principale"],
           ["P2, DiD", "−3,6 [−10,8 ; 3,7]", "−1,9 [−8,8 ; 5,1]",
            "La maquette retenait la variante de divergence de tendance à +2 points ; l'estimation "
            "principale est celle du tableau des effets (T25)"],
           ["P3 et P4, DiD", "0,1 [−6,2 ; 6,4] et −3,2 [−12,9 ; 6,6]",
            "0,3 [−6,0 ; 6,6] et −2,4 [−11,9 ; 7,1]",
            "Les valeurs de la maquette étaient celles du modèle à effets fixes d'aire, non de "
            "l'estimation principale ; les deux sont désormais publiées côte à côte (tableau 26)"],
           ["Numérotation des tableaux", "Pas de tableau 25 ; tableau 45 en double ; 16 fiches non "
            "numérotées", "Numérotation continue de 1 à 48, annexes en A1–A5",
            "La numérotation a été reconstruite ; la correspondance avec le classeur figure en annexe B"],
           ["Figure 15", "Cascade maternelle vide", "Cascade avec produit des étapes et co-couverture",
            "La figure est reconstruite depuis T40 ; les deux mesures sont distinguées"],
           ["Résumé exécutif", "Trois valeurs issues de spécifications secondaires",
            "Valeurs du tableau des effets, avec EMD", "Cohérence entre le résumé et le chapitre 6"],
           ["Écart d'arrondi", "CAC à T1 en intervention : 79,5 (T14) et 79,4 (T25)",
            "79,4 partout", "Les deux onglets diffèrent de 0,1 point par arrondi ; le rapport retient la "
            "valeur du tableau des effets et l'écart est consigné au registre"],
           ["Titres de figures", "Titres tronqués à droite sur six figures",
            "Titres recalculés sur deux lignes", "Lisibilité ; aucun contenu graphique modifié"],
           ["Phrase de mise à jour des champs", "Présente dans le sommaire",
            "Remplacée par une mention discrète", "Le sommaire est un champ automatique documenté"]],
          widths=[2.8, 4.0, 4.4, 5.8],
          size=6.8,
          note_txt="Les écarts non résolus — incohérences internes du classeur, non corrigées ici — font "
                   "l'objet d'un registre séparé, remis avec le rapport et non intégré à celui-ci.")

    h2(doc, "Annexe B. Catalogue des tableaux du classeur et correspondance", number=None)
    para(doc, "Le classeur d'analyse compte 78 onglets. Le tableau ci-dessous donne, pour chaque onglet "
              "mobilisé dans le rapport, son objet et le numéro du tableau correspondant dans le corps du "
              "texte ou en annexe.")
    table(doc, "Tableau B1. Onglets du classeur mobilisés et correspondance avec les tableaux du rapport",
          ['Onglet', 'Objet', 'Tableau du rapport'],
          _catalogue(),
          widths=[5.6, 8.4, 3.0],
          size=6.6,
          note_txt="Les onglets non listés sont des onglets de construction (contrôles intermédiaires, "
                   "agrégats) qui ne sont pas publiés.")

    h2(doc, "Annexe C. Dictionnaire des indicateurs et pondération des indices", number=None)
    para(doc, "Chaque indicateur est défini par sa base, son type, son registre et sa population. Le "
              "dictionnaire est la référence pour toute relecture des tableaux : deux indicateurs de même "
              "nom peuvent différer par leur population.")
    table(doc, "Tableau C1. Dictionnaire des indicateurs : base, registre, population et définition abrégée",
          ['Code', 'Indicateur', 'Base', 'Type', 'Registre', 'Population'],
          [[r[0], r[1], r[2], r[3], r[4], r[5]]
           for r in sheet_rows('T06_fiches_indicateurs', 'ABCDEF')],
          widths=[1.4, 6.4, 1.4, 1.6, 2.0, 4.2],
          size=6.6,
          note_txt="La définition complète de chaque indicateur figure dans l'onglet T06 du classeur. "
                   "Source : T06_fiches_indicateurs.")
    table(doc, "Tableau C2. Composition et pondération des indices de domaine",
          ['Indice', 'Composante', 'Poids'],
          [[r[0], r[1], _f(r[2], 3)] for r in sheet_rows('T07_poids_indices_domaine', 'ABC')],
          widths=[6.0, 8.4, 2.6],
          size=7.0,
          note_txt="Les poids sont ceux de la variante d'Anderson ; une variante à poids égaux est testée "
                   "en sensibilité. Source : T07_poids_indices_domaine.")

    h2(doc, "Annexe D. Tableaux de détail par zone de santé", number=None)
    para(doc, "Les quatre tableaux suivants donnent, pour chaque zone, les valeurs observées à T0 et à T1 et "
              "l'évolution brute sur chaque indicateur primaire. Ils permettent de reconstituer les moyennes "
              "de bras et de vérifier la matrice de la figure 20.")
    for i, (nom, sh) in enumerate([('P1 — Exposition des ménages aux agents (0–100)', 'T19_16_zones_P1'),
                                   ('P2 — Connaissances des ménages (0–100)', 'T19_16_zones_P2'),
                                   ('P3 — Fonctionnalité des CAC (0–100)', 'T19_16_zones_P3'),
                                   ('P4 — Professionnalisation des RECO (0–100)', 'T19_16_zones_P4')]):
        table(doc, f"Tableau D{i+1}. {nom} : valeurs par zone, évolution brute et évolution ajustée",
              ['Province', 'Zone de santé', 'Bras', 'T0', 'n T0', 'T1', 'n T1', 'Évolution brute',
               'Évolution ajustée'],
              [[r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]]
               for r in sheet_rows(sh, 'ABCDEFGHI')],
              widths=[2.6, 3.0, 2.2, 1.4, 1.2, 1.4, 1.2, 2.2, 2.4],
              size=6.9,
              note_txt=f"Source : {sh}. L'évolution ajustée est obtenue par un modèle à effets fixes de "
                       "province ; l'écart à la moyenne provinciale figure dans le classeur.")
    table(doc, "Tableau D5. Synthèse par zone : valeurs initiales et finales des quatre primaires",
          ['Province', 'Zone', 'Bras', 'P1 T0', 'P1 T1', 'P2 T0', 'P2 T1', 'P3 T0', 'P3 T1', 'P4 T0',
           'P4 T1'],
          _synth_zones(),
          widths=[2.2, 2.6, 2.0, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2],
          size=6.6,
          note_txt="Source : T19_16_zones_P1 à P4, colonnes T0 et T1. Les valeurs sont arrondies à une "
                   "décimale.")

    h2(doc, "Annexe E. Fiches de zone", number=None)
    para(doc, "Les fiches rassemblent, pour chaque zone, les éléments utiles au dialogue avec l'équipe "
              "cadre : effectifs, évolution des quatre primaires, mouvements des unités, points "
              "d'attention. Elles sont établies à partir des tableaux D1 à D5 et du tableau 46.")

    h2(doc, "Annexe F. Sources, logiciels et reproductibilité", number=None)
    bullets(doc, [
        "**Sources** : classeur d'analyse `SACO_Phase2_Tableaux_2026-10-15.xlsx`, 78 onglets ; maquette "
        "Word du 19 octobre 2026 ; rapport d'audit du 20 octobre 2026.",
        "**Extraction** : reconstruction du classeur corrompu par retrait des objets graphiques manquants ; "
        "lecture des 78 onglets, 5 713 lignes ménages agrégées.",
        "**Figures** : figures de la maquette conservées, titres recomposés ; quatre figures produites "
        "(cascade, unités, ménages, matrice des zones).",
        "**Document** : assemblage par programme, styles de la maquette ; aucun contenu saisi à la main dans "
        "le fichier final.",
        "**Reproductibilité** : les scripts d'assemblage et de contrôle sont déposés avec le rapport ; "
        "toute valeur citée est retrouvable dans un onglet nommé.",
    ])
    para(doc, "Une limite de production doit être signalée : le document n'a pas pu être converti en PDF "
              "dans l'environnement de production, faute d'outil de conversion disponible. La version Word "
              "est la version de référence ; l'export PDF doit être fait depuis Word après mise à jour du "
              "sommaire.", size=8.4, color=GREY)


def _catalogue():
    mapping = {
        'T01_bilan_appariement': '2', 'T02_realisation_zs': '6', 'T05_dates_collecte': '3',
        'T08_fiabilite_indices': '4', 'T10_emd_par_bras': '5', 'T11_profil_menages': '7',
        'T12_profil_acteurs': '8', 'T13_equilibre_T0': '9', 'T14_cod_3volets': '10',
        'T16_categories_organes': '11', 'T20_transitions_matrices': '3 (figure)',
        'T21_mouvements_unites': '12', 'T22_unites_progression_regressi': '46',
        'T25_tableau_des_effets': '26', 'T26_unites_appariees': '29', 'T27_divergence_tendances': '28',
        'T28_placebos': '27', 'T29_effets_secondaires': '30', 'T30_differences_premieres_aires': '32',
        'T31_associations_transversales': '31', 'T32_variance_niveaux': '33',
        'T34_capacites_extrants_reco': '34', 'T35_heterogeneite': '37',
        'T36_concentration_erreygers': '35', 'T37_gradient_quintiles': '36',
        'T38_genre': '19', 'T39_continuum_maternel': '23', 'T40_continuum_conditionnel': '41',
        'T41_enfant_malade_distributions': '24', 'T43_enfant_malade_deux_parties': '40',
        'T44_vaccination_declare_vu': '22', 'T45_mpox_cap': '38–39',
        'T46_mpox_acceptabilite': '25', 'T47_reco_professionnalisation_c': '15',
        'T48_asc_prime_montant': '17', 'T49_reco_charge_menages': '16', 'T50_logistique': '18',
        'T51_normes_psn': '42', 'T52_indice_conformite': '13',
        'T53_sensibilite_P1': '43', 'T54_synthese_sensibilite': '44', 'T55_manquants_primaires': '45',
        'T06_fiches_indicateurs': 'C1', 'T07_poids_indices_domaine': 'C2',
        'T19_16_zones_P1': 'D1', 'T19_16_zones_P2': 'D2', 'T19_16_zones_P3': 'D3',
        'T19_16_zones_P4': 'D4 et D5',
    }
    obj = {
        'T01_bilan_appariement': 'Bilan de l\'appariement entre T0 et T1, par base',
        'T02_realisation_zs': 'Entretiens réalisés par zone, questionnaire et passage',
        'T05_dates_collecte': 'Fenêtres de collecte et entretiens hors fenêtre',
        'T08_fiabilite_indices': 'Cohérence interne des indices composites',
        'T10_emd_par_bras': 'Effet minimal détectable, sans et avec le bras',
        'T11_profil_menages': 'Profil des ménages par bras et par passage',
        'T12_profil_acteurs': 'Profil des agents et des organes',
        'T13_equilibre_T0': 'Différences standardisées entre bras',
        'T14_cod_3volets': 'Indicateurs CODESA à trois volets',
        'T16_categories_organes': 'Catégories de fonctionnalité des organes',
        'T20_transitions_matrices': 'Matrices de transition des catégories',
        'T21_mouvements_unites': 'Dégradation, stabilité, amélioration par organe',
        'T22_unites_progression_regressi': 'Mouvements des unités appariées',
        'T25_tableau_des_effets': 'Tableau des effets, neuf indicateurs',
        'T26_unites_appariees': 'DiD et ANCOVA sur unités appariées',
        'T27_divergence_tendances': 'Sensibilité à une divergence de tendance',
        'T28_placebos': 'Tests placebo sur caractéristiques non ciblées',
        'T29_effets_secondaires': '32 indicateurs secondaires, p brute et BH',
        'T30_differences_premieres_aires': 'Différences premières au niveau de l\'aire',
        'T31_associations_transversales': 'Associations transversales, valeur E',
        'T32_variance_niveaux': 'Décomposition de la variance et ICC',
        'T34_capacites_extrants_reco': 'Visites à domicile selon professionnalisation et prime',
        'T35_heterogeneite': 'Hétérogénéité pré-spécifiée par sous-groupe',
        'T36_concentration_erreygers': 'Indice de concentration d\'Erreygers',
        'T37_gradient_quintiles': 'Gradient par quintile de niveau de vie',
        'T38_genre': 'Part des femmes parmi les acteurs',
        'T39_continuum_maternel': 'Continuum maternel, niveaux par étape',
        'T40_continuum_conditionnel': 'Probabilités conditionnelles et co-couverture',
        'T41_enfant_malade_distributions': 'Première réaction devant l\'enfant malade',
        'T43_enfant_malade_deux_parties': 'Recours en deux parties : consultation puis délai',
        'T44_vaccination_declare_vu': 'Vaccination déclarée et carnet vu',
        'T45_mpox_cap': 'Connaissances et attitudes Mpox par item',
        'T46_mpox_acceptabilite': 'Déterminants de l\'acceptation du vaccin',
        'T47_reco_professionnalisation_c': 'Composantes de la professionnalisation des RECO',
        'T48_asc_prime_montant': 'Montant déclaré de la prime des ASC',
        'T49_reco_charge_menages': 'Charge en ménages des RECO',
        'T50_logistique': 'Ruptures de stock, transport, équipements',
        'T51_normes_psn': 'Conformité aux vingt normes du PSN',
        'T52_indice_conformite': 'Indice de conformité des agents',
        'T53_sensibilite_P1': 'Matrice de sensibilité, P1',
        'T54_synthese_sensibilite': 'Synthèse des matrices de sensibilité',
        'T55_manquants_primaires': 'Données manquantes et covariables incomplètes',
        'T06_fiches_indicateurs': 'Dictionnaire des indicateurs',
        'T07_poids_indices_domaine': 'Pondération des indices de domaine',
        'T19_16_zones_P1': 'P1 par zone : T0, T1, évolutions',
        'T19_16_zones_P2': 'P2 par zone : T0, T1, évolutions',
        'T19_16_zones_P3': 'P3 par zone : T0, T1, évolutions',
        'T19_16_zones_P4': 'P4 par zone : T0, T1, évolutions',
    }
    return [[k, obj[k], mapping[k]] for k in mapping]


def _synth_zones():
    import json
    X = json.load(open('/home/user/dump.json'))
    zones, vals = [], {}
    for i, sh in enumerate(['T19_16_zones_P1', 'T19_16_zones_P2', 'T19_16_zones_P3', 'T19_16_zones_P4']):
        for r in X[sh]['rows'][1:]:
            c = r['cells']
            key = c['B']
            if key not in vals:
                vals[key] = {'prov': c['A'], 'bras': c['C']}
                zones.append(key)
            vals[key][f'p{i+1}'] = (c['D'], c['F'])
    out = []
    for z in zones:
        v = vals[z]
        out.append([v['prov'], z, 'Int.' if v['bras'] == 'Intervention' else 'Tém.',
                    _f(v['p1'][0]), _f(v['p1'][1]), _f(v['p2'][0]), _f(v['p2'][1]),
                    _f(v['p3'][0]), _f(v['p3'][1]), _f(v['p4'][0]), _f(v['p4'][1])])
    return out
