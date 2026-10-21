# -*- coding: utf-8 -*-
"""Chapitres 9 à 13 : thématiques, PSN, robustesse, synthèse par dynamique, discussion."""
from base import *
from docx.shared import Pt, Cm


def _mpox(bloc, items):
    out = []
    for r in X['T45_mpox_cap']['rows'][1:]:
        c = r['cells']
        if c.get('A') == bloc and c.get('B') in items:
            out.append([c.get('B'), c.get('C'), c.get('D'), c.get('E'), c.get('F')])
    return out


def _zones_mouvement():
    z = {}
    for r in X['T22_unites_progression_regressi']['rows'][1:]:
        c = r['cells']
        k = (c.get('C'), c.get('D'))
        z.setdefault(k, [0, 0])
        z[k][0 if c.get('I') == 'Amélioration' else 1] += 1
    out = [[k[0], 'Intervention' if k[1] == 'Intervention' else 'Témoin', str(v[0]), str(v[1]),
            f'{v[0]-v[1]:+d}'.replace('+', '+').replace('-', '−')] for k, v in z.items()]
    out.sort(key=lambda r: -int(r[4].replace('−', '-')))
    return out


def ch9(doc):
    page_break(doc)
    h1(doc, 9, 'Thématiques', band=f'{FIG}/bands/b09.png')
    para(doc, "Trois dossiers méritent un traitement séparé, parce qu'ils portent des enjeux de santé "
              "publique qui dépassent la question de l'effet : la Mpox, le recours aux soins de l'enfant "
              "malade et la santé maternelle. Le chapitre reprend les données du chapitre 5, mais les "
              "travaille au niveau des mécanismes et des sous-populations.")

    h2(doc, "9.1 La Mpox : des connaissances qui progressent, une prévention qui stagne", number=None)
    para(doc, "Les connaissances sur la Mpox progressent dans les deux bras, mais la structure des "
              "connaissances est asymétrique : les ménages savent mieux que la maladie existe et comment "
              "elle se transmet, mais les gestes de prévention restent partiels. La radio reste la "
              "première source d'information (52,7 % en témoin à T1, 50,0 % en intervention), devant "
              "l'agent communautaire lors d'une visite à domicile (51,8 et 56,4 %).")
    table(doc, "Tableau 38. Sources d'information sur la Mpox, par bras et par passage (%)",
          ['Source', 'Bras', 'Passage', '% [IC 95 %]', 'n'],
          _mpox('K2', ['ASC / COSA lors d\'une VAD', 'Amis, famille', 'Centre ou poste de santé',
                       'Radio', 'Télévision', 'Église', 'Lecture']),
          widths=[5.6, 2.8, 2.2, 4.6, 1.8],
          size=7.2,
          note_txt="Question posée aux ménages connaissant la Mpox ; n = 637 à 823 selon le bras et le "
                   "passage. Source : T45_mpox_cap.")
    para(doc, "Les modes de transmission cités sont dominés par le contact avec une personne infectée et par "
              "le contact avec les animaux ; les items relatifs aux rapports sexuels et au linge du malade "
              "restent minoritaires, alors qu'ils figurent dans les messages nationaux. La prévention, "
              "enfin, se concentre sur quatre gestes — isoler la personne suspecte, informer les autorités "
              "sanitaires, éviter tout contact direct et sensibiliser l'entourage, cités par 40 à 60 % des "
              "répondants — et beaucoup moins sur les équipements de protection (18 à 36 %).")
    table(doc, "Tableau 39. Modes de transmission et gestes de prévention cités, par bras et par passage (%)",
          ['Item', 'Bras', 'Passage', '% [IC 95 %]', 'n'],
          _mpox('K3', ['Contact avec une personne infectée', 'Contact avec les animaux', 'Habits du malade',
                       'Manger avec le malade', 'Rapports sexuels']) +
          _mpox('K5', ['Informer les autorités sanitaires', 'Isoler la personne suspecte',
                       'Porter des équipements de protection', 'Sensibiliser l\'entourage',
                       'Éviter tout contact direct']),
          widths=[6.4, 2.8, 2.2, 4.4, 1.4],
          size=6.9,
          note_txt="Source : T45_mpox_cap, blocs K3 (transmission) et K5 (conduite à tenir).")
    para(doc, "L'acceptabilité déclarée du vaccin est élevée — 79,5 % en intervention à T1 — mais elle "
              "diminue avec le niveau de vie et la distance, comme le montre le chapitre 5. Le rapprochement "
              "des deux constats suggère que le frein n'est pas l'acceptabilité mais l'accessibilité : les "
              "ménages les plus éloignés acceptent moins un vaccin qu'ils auraient plus de mal à recevoir.")

    h2(doc, "9.2 L'enfant malade : qui consulte, et en combien de temps", number=None)
    para(doc, "Le recours aux soins de l'enfant malade a été modélisé en deux parties : d'abord la décision "
              "de consulter, ensuite le délai parmi ceux qui consultent. La première est fortement liée au "
              "bras — le rapport de cotes est de 2,12 [1,31 ; 3,43] en faveur de l'intervention — et à la "
              "connaissance des facilités de gratuité (2,00 [1,44 ; 2,77]). La seconde dépend surtout du "
              "niveau de vie.")
    table(doc, "Tableau 40. Recours pour l'enfant malade en deux parties : consultation, puis délai",
          ['Partie', 'Terme', 'Rapport de cotes', 'IC 95 %', 'p'],
          sheet_rows('T43_enfant_malade_deux_parties', 'ABCDE'),
          widths=[4.6, 5.2, 2.8, 3.0, 1.8],
          size=7.0,
          note_txt="Partie 1 : modèle logistique de la consultation. Partie 2 : modèle du délai parmi les "
                   "consultants. Le rapport de cotes du bras mesure une association, non un effet : les "
                   "zones d'intervention recourent déjà davantage au départ. "
                   "Source : T43_enfant_malade_deux_parties.")
    para(doc, "Ce résultat illustre la difficulté centrale du rapport : la variable « bras » est associée à "
              "presque tous les résultats, y compris à ceux sur lesquels l'appui n'a pas d'action directe. "
              "C'est cette association, et non un effet, que la différence de différences neutralise — et "
              "c'est pourquoi les deux lectures doivent être présentées ensemble.")

    h2(doc, "9.3 La santé maternelle : une cascade qui fuit par le milieu", number=None)
    para(doc, "La cascade maternelle perd l'essentiel de son effectif entre la première et la quatrième "
              "consultation prénatale : 58,5 points sur 100. Les pertes suivantes, plus faibles, sont "
              "concentrées sur la période postnatale, où seuls 35 % des femmes accouchées en structure "
              "reviennent six semaines après. Le point d'entrée est donc bon — neuf femmes sur dix font au "
              "moins une consultation — et c'est le maintien dans le parcours qui pose problème.")
    para(doc, "L'évolution entre les deux passages ne va pas dans le sens attendu : la quatrième "
              "consultation recule en zone d'intervention (42,5 → 38,6 %) et la consultation postnatale "
              "progresse moins vite qu'en zone témoin (31,4 → 38,8 % contre 31,4 → 45,4 %). Deux explications "
              "sont possibles et non départageables avec ces données : une différence de calendrier de "
              "grossesse entre les passages, ou un effet de saturation des structures dans les zones où "
              "l'appui a mobilisé les agents.")
    table(doc, "Tableau 41. Probabilités conditionnelles de franchir chaque étape du continuum maternel",
          ['Bras', 'Passage', 'P(CPN4+ | CPN1)', 'P(structure | CPN4+)', 'P(CPoN | structure)',
           'Co-couverture des 4 étapes (%)'],
          sheet_rows('T40_continuum_conditionnel', 'ABCDEF'),
          widths=[3.0, 2.2, 3.0, 3.0, 3.0, 3.4],
          note_txt="La co-couverture est mesurée directement sur les quatre réponses individuelles ; elle "
                   "n'est pas le produit des trois probabilités conditionnelles. "
                   "Source : T40_continuum_conditionnel.")

    h2(doc, "9.4 Ce que les thèmes changent à la lecture d'ensemble", number=None)
    para(doc, "Les trois dossiers convergent vers une même conclusion : le dispositif a touché les ménages, "
              "mais pas les points où se joue la santé. L'exposition progresse, les connaissances "
              "progressent, la demande de soins progresse ; la prévention de la Mpox, le retour postnatal et "
              "la vérification vaccinale ne suivent pas. Autrement dit, l'appui a agi sur le premier maillon "
              "de la chaîne — la mise en relation — et beaucoup moins sur les suivants.")
    para(doc, "Cette lecture est cohérente avec l'analyse des mécanismes du chapitre 7 : ce qui est associé "
              "aux résultats, c'est le fonctionnement des organes et la prime, c'est-à-dire les conditions "
              "matérielles de l'activité, non la formation ou la conformité aux normes.")


def ch10(doc):
    page_break(doc)
    h1(doc, 10, 'Alignement avec le PSN SACO 2025-2030', band=f'{FIG}/bands/b10.png')
    para(doc, "Le plan national de développement sanitaire fixe vingt normes opposables aux organes et aux "
              "agents communautaires. Ce chapitre mesure l'écart à ces normes, son évolution et sa "
              "signification. Il distingue trois questions que l'on confond souvent : être conforme, être "
              "efficace et être financé.")

    h2(doc, "10.1 Les vingt normes, une par une", number=None)
    para(doc, "Deux normes seulement sont assorties d'une cible chiffrée dans le plan : la parité parmi les "
              "RECO (50 %) et le nombre de ménages par RECO (50). Les dix-huit autres sont des obligations de "
              "moyens, sans niveau cible. La conformité se lit donc en niveau et en évolution, non en "
              "atteinte d'une cible.")
    table(doc, "Tableau 42. Conformité aux normes du PSN SACO (% d'unités conformes), par bras et par passage",
          ['Norme', 'Unité', 'Témoin T0', 'Témoin T1', 'Intervention T0', 'Intervention T1',
           "Contenu de l'appui"],
          [[r[0], r[1], r[2], r[3], r[4], r[5], r[6]]
           for r in sheet_rows('T51_normes_psn', 'ABCDEFG')],
          widths=[6.4, 1.6, 1.8, 1.8, 2.2, 2.2, 1.8],
          size=6.9,
          note_txt="Lecture : la colonne « contenu de l'appui » signale les normes que l'appui finançait "
                   "directement. Source : T51_normes_psn.")
    para(doc, "Le tableau met en évidence trois régimes. Les normes de désignation et de réunion progressent "
              "partout, souvent de plus de 10 points. Les normes de dotation stagnent : la prime recule, les "
              "subsides de fonctionnement des CAC reculent en témoin et progressent peu en intervention, et "
              "les membres de CODESA rémunérés restent une minorité. Les normes de statut, enfin, sont "
              "bloquées : contrat et certification concernent moins de 15 % des agents dans les deux bras.")

    h2(doc, "10.2 La conformité est-elle associée à l'efficacité ?", number=None)
    para(doc, "Non. L'indice de conformité des RECO aux six normes qui les concernent n'est pas associé à "
              "leurs extrants : le rapport de taux est de 1,00 [0,95 ; 1,06] par 10 points de conformité. "
              "La prime, elle, l'est fortement (1,84). La conformité mesure donc le respect d'un "
              "référentiel, pas la production de services.")
    para(doc, "Cette conclusion a une conséquence pratique importante pour le tableau de bord national : "
              "utiliser l'indice de conformité comme indicateur de performance conduirait à valoriser des "
              "agents qui remplissent des conditions formelles sans que leur activité change. Le rapport "
              "recommande de conserver l'indice comme mesure de conformité et d'y adjoindre un indicateur "
              "d'activité — visites, animations, référencements.")

    h2(doc, "10.3 Ce que l'appui a financé, et ce qu'il n'a pas changé", number=None)
    para(doc, "Quatre normes correspondent à des intrants que l'appui finançait : la prime des ASC, le "
              "contrat des RECO, le contrat des ASC et les subsides de fonctionnement des CAC. Sur ces "
              "quatre, une seule s'améliore franchement en zone d'intervention : la prime, dont la part des "
              "ASC concernés progresse de 26,4 à 24,4 % — autrement dit, elle recule légèrement. Le contrat "
              "des ASC recule de 26,4 à 10,3 %. Les subsides des CAC progressent de 57,3 à 60,2 %.")
    figure(doc, f'{FIG}/fig02_normes.png', "Figure 16. Conformité aux vingt normes du PSN SACO à T0 et à "
           "T1, par bras : synthèse graphique.", width=16.4,
           note_txt="La figure reprend le tableau 42. Les normes sont ordonnées du plus au moins conforme à "
                    "T0 ; les points évides sont T0, les points pleins T1.")
    para(doc, "Le décalage entre ce qui est financé et ce qui progresse est l'un des résultats les plus "
              "solides du rapport, et l'un des plus gênants : il suggère que les intrants de l'appui ont "
              "été insuffisants ou irréguliers pour modifier durablement les pratiques, alors que les "
              "normes de gouvernance — qui ne coûtent presque rien — ont continué de progresser.")

    h2(doc, "10.4 Recommandations d'alignement", number=None)
    bullets(doc, [
        "**Fixer des cibles sur les normes qui n'en ont pas**, en particulier sur la supervision mensuelle "
        "et sur la tenue des réunions de monitorage, déjà proches de 90 %.",
        "**Séparer dans le tableau de bord la conformité et l'activité** : deux indices, deux usages.",
        "**Rendre la prime prévisible** : sa variabilité est le principal facteur associé à l'activité des "
        "agents.",
        "**Traiter le contrat comme un préalable administratif**, non comme un levier de performance : "
        "il n'est associé à aucun extrant dans les données.",
        "**Publier les normes non atteintes** : la part des femmes parmi les ASC recule, et la cible de "
        "parité n'est approchée par aucun bras.",
    ])


def ch11(doc):
    page_break(doc)
    h1(doc, 11, 'Robustesse et limites', band=f'{FIG}/bands/b11.png')
    para(doc, "Un résultat négatif n'a de valeur que s'il est robuste. Ce chapitre passe les quatre primaires "
              "au crible de dix-huit familles de variantes, retire une zone à la fois, examine les données "
              "manquantes et discute les limites de validité.")

    h2(doc, "11.1 Les matrices de sensibilité", number=None)
    para(doc, "Pour chaque primaire, l'estimation a été recalculée en variant la spécification (covariables, "
              "pondération, repondération), la qualité des données (entretiens hors fenêtre, sexe corrigé), "
              "l'échantillon (retrait d'une province, d'une zone à tour de rôle), la construction de "
              "l'indice (retrait d'un item), la version de l'indicateur, l'imputation, l'estimateur et "
              "l'hypothèse de tendance. Dix-huit variantes ont été produites pour P1.")
    table(doc, "Tableau 43. Matrice de sensibilité : indice d'exposition des ménages aux agents (P1)",
          ['Famille', 'Variante', 'DiD [IC 95 %]', 'p', 'Conclusion inchangée'],
          [[r[0], r[1], r[2], r[3], r[4]]
           for r in sheet_rows('T53_sensibilite_P1', 'ABCDE')],
          widths=[3.4, 8.4, 3.4, 1.6, 2.4],
          size=6.8,
          note_txt="« Conclusion inchangée » signifie que l'estimation reste dans le cas D ou E de la grille "
                   "du tableau 6. Source : T53_sensibilite_P1.")
    para(doc, "La conclusion ne change que dans deux cas, tous deux construits : une divergence de tendance "
              "de −5 points fait passer P1 au cas B (6,9 [0,6 ; 13,3]) et une divergence de +5 points la fait "
              "passer au cas E (−3,1 [−9,4 ; 3,3]). Ces deux cas encadrent l'hypothèse des tendances "
              "parallèles ; ils ne l'infirment pas, ils en mesurent l'enjeu.")
    table(doc, "Tableau 44. Synthèse des matrices de sensibilité : variantes, étendue et part des variantes "
          "concluantes",
          ['Indicateur', 'Variantes', 'Conclusion inchangée', 'Part (%)', 'Min DiD', 'Max DiD',
           'IC le plus large'],
          [[r[0], r[1], r[2], r[3], r[4], r[5], r[6]]
           for r in sheet_rows('T54_synthese_sensibilite', 'ABCDEFG')],
          widths=[5.8, 1.8, 2.8, 1.6, 1.6, 1.6, 2.2],
          size=7.2,
          note_txt="Source : T54_synthese_sensibilite. La part des variantes concluantes est la part des "
                   "spécifications qui laissent la conclusion inchangée.")
    para(doc, "Un point doit être précisé, car il conditionne la lecture du tableau précédent : les "
              "changements de conclusion répertoriés sont, à deux exceptions près, des passages entre le cas "
              "D et le cas E, c'est-à-dire entre « effet indéterminé » et « gain non soutenu, baisse non "
              "exclue ». Les deux exceptions sont les divergences de tendance simulées de −5 points sur P1, "
              "qui font passer l'estimation au cas B. Aucune variante ne fait apparaître d'effet établi.")
    figure(doc, f'{FIG}/f19.png', "Figure 17. Courbes de spécification des quatre primaires.", width=16.4,
           note_txt="Chaque point est une variante ; la ligne verticale marque le zéro, la bande l'EMD. "
                    "Source : T53_sensibilite_P1 à P4.")

    h2(doc, "11.2 Le retrait d'une zone", number=None)
    para(doc, "Retirer une zone de santé à tour de rôle modifie les estimations de P1 dans une fourchette de "
              "0,6 à 3,3 points, sans faire sortir l'intervalle du cas D. Aucune zone n'est donc "
              "déterminante — ce qui est attendu avec huit zones par bras, et rassurant sur l'absence de "
              "valeur aberrante.")
    figure(doc, f'{FIG}/f20.png', "Figure 18. Estimations en retirant chaque zone de santé à tour de rôle.",
           width=16.4,
           note_txt="Source : T53_sensibilite_P1 à P4, variante « sans une zone à tour de rôle ». "
                    "Les quinze estimations sont présentées par indicateur, avec leur intervalle.")

    h2(doc, "11.3 Les données manquantes", number=None)
    para(doc, "Les indicateurs primaires ne comportent aucune valeur manquante : les 5 713 ménages répondent "
              "aux items qui les composent. Les covariables, en revanche, sont incomplètes pour 12 à 15 % "
              "des ménages. Ces manquants ont été traités par imputation multiple (m = 5) dans une variante "
              "dédiée, qui déplace l'estimation de P1 de 1,9 à 2,9 points sans changer la conclusion.")
    table(doc, "Tableau 45. Données manquantes sur les indicateurs primaires et les covariables, par bras et "
          "passage",
          ['Indicateur', 'Bras', 'Passage', 'Manquants (%)', 'Covariables incomplètes (%)'],
          sheet_rows('T55_manquants_primaires', 'ABCDE'),
          widths=[3.6, 3.0, 2.4, 3.4, 4.6],
          size=7.2,
          note_txt="Source : T55_manquants_primaires. Aucun indicateur primaire ne comporte de valeur "
                   "manquante ; les manquants portent sur les covariables d'ajustement.")

    h2(doc, "11.4 Les limites de validité", number=None)
    bullets(doc, [
        "**Puissance** : avec huit zones par bras, l'EMD est de 9 à 13 points ; un effet de 3 à 5 points, "
        "plausible pour ce type d'appui, n'aurait pas été détecté.",
        "**Tendances parallèles** : l'hypothèse n'est pas testable. Une divergence de 5 points suffit à "
        "faire basculer la conclusion sur P1.",
        "**Contamination** : les zones témoins sont dans les mêmes provinces et bénéficient des mêmes "
        "campagnes nationales ; la progression des témoins en est probablement accrue, ce qui réduit "
        "l'écart observable.",
        "**Mesure déclarative** : la plupart des indicateurs sont déclarés. L'écart entre vaccination "
        "déclarée et carnet vu montre l'ampleur du biais possible.",
        "**Saisonnalité** : T0 a lieu en saison des pluies, T1 en saison sèche ; les recours aux soins et "
        "les épidémies saisonnières en dépendent.",
        "**Attrition des grappes** : 44 % des grappes de ménages ne sont pas retrouvées, ce qui interdit "
        "toute analyse de cohorte au niveau des ménages.",
        "**Données Mpox** : les cas par zone ne sont pas disponibles à la granularité du devis ; l'effet sur "
        "l'incidence n'est pas mesuré.",
    ])
    para(doc, "Prises ensemble, ces limites dessinent un devis adapté à la description et à l'analyse des "
              "mécanismes, inadapté à la démonstration d'efficacité. C'est la conclusion méthodologique "
              "centrale du rapport, et elle conditionne les recommandations du chapitre 13.")


def ch12(doc):
    page_break(doc)
    h1(doc, 12, 'Synthèse conjointe par dynamique', band=f'{FIG}/bands/b12.png')
    para(doc, "Les chapitres précédents raisonnent en moyenne de bras. Ce chapitre change d'unité d'analyse : "
              "il suit les zones et les unités appariées, pour montrer où le mouvement se produit et ce que "
              "les moyennes masquent.")

    h2(doc, "12.1 Neuf zones sur seize progressent", number=None)
    para(doc, "Sur 249 unités appariées — CAC et villages — 143 progressent et 106 régressent, soit un solde "
              "de +37. Le mouvement est donc majoritaire mais loin d'être général. Il n'est pas propre aux "
              "zones d'intervention : 70 unités progressent contre 45 côté intervention, 73 contre 61 côté "
              "témoin. L'écart n'est pas testé, faute de puissance au niveau des unités.")
    figure(doc, f'{FIG}/fig06bis_unites.png', "Figure 19. Unités appariées en progression et en régression, "
           "par zone de santé.", width=16.4,
           note_txt="T = zone témoin, I = zone d'intervention. Le seuil de mouvement est de ± 11,1 points, "
                    "soit un critère sur neuf. Source : T22_unites_progression_regressi.")
    table(doc, "Tableau 46. Mouvements des unités appariées par zone de santé et par bras",
          ['Zone de santé', 'Bras', 'Progression', 'Régression', 'Solde'],
          _zones_mouvement(),
          widths=[5.4, 3.4, 3.2, 3.0, 2.0],
          note_txt="Source : T22_unites_progression_regressi, agrégation des unités CAC et villages. "
                   "Les neuf zones en progression et les cinq en récession sont classées par solde.")

    h2(doc, "12.2 Les profils de zone", number=None)
    para(doc, "La matrice des évolutions brutes sur les quatre primaires montre des profils très contrastés. "
              "Deux zones progressent sur les quatre indicateurs — Katako Kombe (intervention) et Minga "
              "(témoin) —, aucune ne recule sur les quatre. Quatre zones reculent sur trois indicateurs : "
              "Kalima, Tshishimbi, Walungu et Tunda, toutes témoins.")
    figure(doc, f'{FIG}/fig10bis_matrice.png', "Figure 20. Évolutions brutes des quatre primaires, par zone "
           "de santé.", width=15.4,
           note_txt="Lecture : chaque case donne l'évolution brute en points entre T0 et T1 pour la zone et "
                    "l'indicateur. Ce sont des évolutions, non des effets. Source : T19_16_zones_P1 à P4.")
    para(doc, "Le contraste le plus net oppose Katako Kombe (+12, +17, +15, +22) à Tunda (+7, +27, +2, +0) : "
              "la première progresse partout, sans être la mieux dotée au départ ; la seconde progresse "
              "fortement sur les connaissances mais ne bouge pas sur les autres indicateurs. Ces profils "
              "rappellent qu'une moyenne de bras agrège des trajectoires qui n'ont pas grand-chose en commun.")

    h2(doc, "12.3 Les cas contrastés", number=None)
    para(doc, "Trois cas méritent une fiche détaillée, reproduite en annexe E. Katako Kombe est la zone où "
              "tout progresse, y compris la fonctionnalité des CAC et la professionnalisation des RECO. "
              "Kalima est la zone où tout recule sauf les connaissances, alors qu'elle est témoin et "
              "relativement bien dotée. Nyangezi est stable sur les quatre indicateurs, avec des effectifs "
              "pourtant complets aux deux passages.")
    para(doc, "Ces cas ne permettent pas de conclusion causale — une zone n'est pas une observation "
              "indépendante, et les écarts peuvent relever du hasard — mais ils orientent l'analyse "
              "qualitative : ce qui distingue Katako Kombe, c'est la conjonction d'un CODESA actif et d'un "
              "fonctionnement retrouvé des CAC après une période difficile, non un intrant supplémentaire.")

    h2(doc, "12.4 Ce que la dynamique de zone change à la lecture d'ensemble", number=None)
    para(doc, "Deux conséquences. D'abord, la progression des moyennes n'est pas un phénomène uniforme : elle "
              "résulte de mouvements opposés qui se compensent partiellement, ce qui justifie un suivi par "
              "zone plutôt que par bras. Ensuite, l'absence d'écart entre bras au niveau des moyennes ne "
              "signifie pas l'absence de dynamique : certaines zones d'intervention progressent fortement et "
              "d'autres reculent, comme dans le bras témoin.")
    para(doc, "Pour la phase 3, la recommandation est de raisonner en portefeuille de zones plutôt qu'en "
              "bras : identifier les zones où le dispositif fonctionne, comprendre pourquoi, et concentrer "
              "l'appui là où il produit du mouvement.")


def ch13(doc):
    page_break(doc)
    h1(doc, 13, 'Discussion et recommandations', band=f'{FIG}/bands/b13.png')
    para(doc, "Ce chapitre discute la portée des résultats, propose des formulations utilisables en "
              "communication et formule douze recommandations, avec leur délai et leur responsable.")

    h2(doc, "13.1 Ce que les résultats permettent d'affirmer", number=None)
    para(doc, "Le dispositif a accompagné une progression réelle dans les zones d'intervention : "
              "l'exposition des ménages aux agents passe de 62,2 à 69,2, les connaissances de 33,4 à 40,3, "
              "la fonctionnalité des CAC de 75,6 à 79,5, la professionnalisation des RECO de 41,6 à 42,3. "
              "Les mêmes progressions s'observent dans les zones témoins, à des niveaux légèrement "
              "différents. C'est ce que le rapport peut affirmer sans réserve.")
    para(doc, "Il ne peut pas affirmer que ces progressions sont dues à l'appui. Il ne peut pas non plus "
              "affirmer le contraire. La formulation exacte est : « dans un dispositif capable de détecter "
              "des effets d'au moins 9 à 13 points, aucun effet de l'appui n'a été mis en évidence sur les "
              "quatre indicateurs retenus ; les estimations sont compatibles avec un effet modeste comme "
              "avec une absence d'effet ».")

    h2(doc, "13.2 Trois registres de formulation", number=None)
    table(doc, "Tableau 47. Formulations autorisées et formulations à éviter",
          ['Registre', 'Formulation autorisée', 'Formulation à éviter'],
          [["Évolution", "« L'exposition des ménages aux agents a progressé de 7 points en zone "
                         "d'intervention entre mars et septembre 2026. »",
            "« L'appui a fait progresser l'exposition de 7 points. »"],
           ["Attribution", "« Aucun effet de l'appui n'a été mis en évidence ; l'intervalle de confiance "
                           "va de −4,4 à +8,3 points. »",
            "« L'appui n'a pas eu d'effet. »"],
           ["Association", "« La fonctionnalité des CAC est associée à l'exposition des ménages : "
                           "+2,9 points par 10 points de fonctionnalité. »",
            "« Des CAC fonctionnels améliorent l'exposition des ménages. »"],
           ["Conformité", "« Un agent sur deux respecte la moitié des normes qui le concernent. »",
            "« La qualité des agents est insuffisante. »"],
           ["Prospective", "« Un devis à soixante zones par bras permettrait de détecter un effet de "
                           "5 points. »",
            "« Il suffit d'étendre l'appui pour obtenir des résultats. »"]],
          widths=[2.6, 8.2, 6.2],
          note_txt="Ces formulations sont reprises dans la note de communication qui accompagne le rapport.")

    h2(doc, "13.3 Les douze recommandations", number=None)
    para(doc, "Les recommandations sont classées par destinataire et par horizon. Elles découlent directement "
              "des chiffres du rapport ; le délai indique l'échéance proposée à compter de la validation du "
              "rapport.")
    table(doc, "Tableau 48. Recommandations, responsables et délais",
          ['N°', 'Recommandation', 'Fondement chiffré', 'Responsable', 'Délai'],
          [["R1", "Redimensionner le devis de la phase 3 : 60 zones par bras pour un effet de 5 points, ou "
                  "devis apparié au niveau de l'aire",
            "EMD de 8,8 à 13,3 points ; ICC d'aire de 0,29 à 0,57", "Unité de suivi-évaluation", "30 j"],
           ["R2", "Faire de la prime un engagement pluriannuel et prévisible",
            "prime associée aux visites : RT 1,84 [1,51 ; 2,24]", "Direction du projet, UNICEF", "60 j"],
           ["R3", "Relever la prime des ASC au niveau de 30 USD dans les huit zones d'intervention",
            "73,7 % des ASC d'intervention perçoivent ≥ 30 USD contre 25,0 % en témoin", "Direction du projet",
            "60 j"],
           ["R4", "Ne pas conditionner l'appui aux indicateurs de volume",
            "P3 et P4 partaient plus haut en intervention (DS 0,38 et 0,27)", "Bailleur, coordination PSN",
            "90 j"],
           ["R5", "Séparer conformité et activité dans le tableau de bord national",
            "indice de conformité sans effet sur les extrants : RT 1,00 [0,95 ; 1,06]", "Ministère de la Santé",
            "120 j"],
           ["R6", "Instituer un contrôle documentaire de la vaccination",
            "écart déclaré − vu de 26,2 à 54,7 points selon la province", "Programme élargi de vaccination",
            "120 j"],
           ["R7", "Cibler les ménages éloignés pour la vaccination Mpox",
            "acceptabilité 0,72 [0,62 ; 0,83] entre 30 et 60 min de marche", "Programme Mpox", "90 j"],
           ["R8", "Renforcer le maintien dans le parcours postnatal",
            "35 % de retour postnatal après accouchement en structure", "Santé maternelle, zones de santé",
            "180 j"],
           ["R9", "Documenter les ruptures de stock par aire et par mois",
            "61,5 % des RECO témoins déclarent des ruptures", "Pharmacie, zones de santé", "90 j"],
           ["R10", "Publier les résultats négatifs et la note de formulation",
            "verdict de non-démonstration ; formulations du tableau 47", "Direction du projet", "15 j"],
           ["R11", "Suivre les zones, non les bras, dans le pilotage",
            "9 zones en progression, 5 en régression, 2 stables", "Unité de suivi-évaluation", "30 j"],
           ["R12", "Programmer une enquête qualitative sur les cas contrastés",
            "Katako Kombe, Kalima, Nyangezi : profils opposés", "Unité de recherche", "150 j"]],
          widths=[1.0, 6.6, 5.0, 2.8, 1.6],
          size=6.8,
          note_txt="Les délais sont exprimés en jours à compter de la validation du rapport. Les responsables "
                   "sont désignés par fonction, non par personne.")

    h2(doc, "13.4 Ce qu'il faudrait pour conclure", number=None)
    para(doc, "Trois conditions permettraient de transformer ce rapport descriptif en évaluation d'efficacité. "
              "Un devis dimensionné pour l'effet attendu, soit environ soixante zones par bras pour un effet "
              "de 5 points sur P1. Une mesure au niveau des unités effectivement exposées, avec appariement à "
              "l'aire, pour exploiter la variance intra-zone. Une mesure non déclarative des résultats "
              "— carnet vu, observation des séances, données de fréquentation des structures — pour réduire "
              "le biais de déclaration, dont l'ampleur atteint 55 points au Sud-Kivu.")
    para(doc, "À défaut, le dispositif actuel reste utile : il documente une progression collective, il "
              "identifie les mécanismes sur lesquels agir et il fournit un tableau de bord de zone utilisable "
              "par les équipes. Ce n'est pas une évaluation d'impact, et le rapport ne le présente pas comme "
              "telle.")

    h2(doc, "13.5 Conclusion", number=None)
    para(doc, "La phase 2 du projet SACO a accompagné, sans les produire de façon démontrable, des "
              "progressions sensibles dans seize zones de santé de quatre provinces. Les ménages voient "
              "davantage les agents, connaissent mieux la Mpox et recourent plus souvent au centre de santé. "
              "Les organes communautaires fonctionnent un peu mieux, les agents un peu plus souvent formés. "
              "Rien de cela ne se distingue nettement de ce qui s'est produit dans les zones sans appui.")
    para(doc, "Le rapport propose de lire ce résultat comme un enseignement, non comme un échec : à cette "
              "échelle et avec ces instruments, l'appui communautaire ne produit pas d'effet mesurable sur "
              "des indicateurs agrégés de zone. Il produit en revanche des conditions — prime, "
              "fonctionnement des organes, supervision — dont l'analyse montre qu'elles sont associées aux "
              "résultats. C'est là que la phase 3 a le plus à gagner, et c'est là que le dispositif de mesure "
              "doit être reconstruit.")
