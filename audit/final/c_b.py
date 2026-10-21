# -*- coding: utf-8 -*-
"""Chapitres 5 à 8 : ménages, effet, mécanismes, équité."""
from base import *
from docx.shared import Pt, Cm


def _men(codes):
    """Lignes du tableau à trois volets ménages, filtrées par code."""
    rows = []
    for r in X['T14_men_3volets']['rows'][1:]:
        c = r['cells']
        if c.get('A') in codes:
            rows.append([c.get('B', ''), c.get('C', ''), c.get('D', ''), c.get('E', ''),
                         c.get('F', ''), c.get('G', ''), c.get('H', '')])
    return rows


def _n(v, d=1):
    try:
        return f'{float(str(v).replace(",", ".")):.{d}f}'.replace('.', ',')
    except Exception:
        return str(v)


def ch5(doc):
    page_break(doc)
    h1(doc, 5, 'Ménages', band=f'{FIG}/bands/b05.png')
    para(doc, "Ce chapitre décrit les résultats du côté des ménages : exposition aux agents, connaissances, "
              "pratiques de vaccination, recours aux soins, santé maternelle et rapport à la Mpox. Les "
              "valeurs sont celles des 5 713 ménages enquêtés, sans pondération autre que celle des "
              "provinces.")

    h2(doc, "5.1 L'exposition aux agents (P1)", number=None)
    para(doc, "L'indice d'exposition combine trois faits : avoir reçu une visite à domicile, avoir vu un "
              "agent animer dans le mois écoulé, connaître le COSA et ses agents. Il progresse de 65,3 à "
              "69,3 en zone témoin, de 62,2 à 69,2 en zone d'intervention. La progression est donc plus "
              "forte en intervention (+7,0 contre +4,0), mais l'intervalle de l'écart d'évolution contient "
              "zéro : −3,5 à 11,5 en témoin, 0,5 à 13,6 en intervention.")
    table(doc, "Tableau 20. Exposition des ménages aux agents (P1) et composantes, à T0 et à T1",
          ['Indicateur', 'Groupe', 'T0 [IC 95 %]', 'n T0', 'T1 [IC 95 %]', 'n T1', 'Écart [IC 95 %]'],
          _men(['P1', 'L7', 'L6', 'L1', 'L5']),
          widths=[5.4, 1.7, 2.5, 1.0, 2.5, 1.0, 2.9],
          size=6.9,
          note_txt="Source : T14_men_3volets. Les effectifs diffèrent de 5 713 sur les items conditionnels "
                   "(L6 : a vu un agent animer récemment), d'où des n plus faibles.")
    para(doc, "La visite à domicile est le canal le plus dynamique : 68,6 → 71,9 % en témoin, 66,0 → 74,5 % "
              "en intervention. La participation au choix des agents progresse fortement dans les deux bras "
              "(30,0 → 41,2 % et 46,7 → 55,4 %), signe d'une dynamique communautaire qui dépasse le "
              "périmètre de l'appui. La satisfaction à l'égard des agents reste élevée et stable, autour de "
              "90 %.")

    h2(doc, "5.2 Les connaissances (P2)", number=None)
    para(doc, "L'indice de connaissances passe de 30,3 à 38,9 en témoin et de 33,4 à 40,3 en intervention : "
              "+8,7 et +6,8 points. Le niveau reste bas en valeur absolue — les ménages citent en moyenne six "
              "signes de danger sur dix-huit — mais la progression est la plus forte des quatre primaires.")
    table(doc, "Tableau 21. Connaissances des ménages (P2) et items de connaissance, à T0 et à T1",
          ['Indicateur', 'Groupe', 'T0 [IC 95 %]', 'n T0', 'T1 [IC 95 %]', 'n T1', 'Écart [IC 95 %]'],
          _men(['P2', 'SIG', 'K1', 'K8', 'K7', 'W3', 'J2']),
          widths=[5.4, 1.7, 2.5, 1.0, 2.5, 1.0, 2.9],
          size=6.9,
          note_txt="Source : T14_men_3volets. L'indice de connaissances (P2) agrège 24 items et est ramené "
                   "sur 0–100 ; les items isolés sont des pourcentages.")
    para(doc, "La connaissance de la Mpox progresse de 44,9 à 54,9 % en témoin et de 55,5 à 58,0 % en "
              "intervention : la progression est plus forte là où l'appui n'était pas déployé, ce qui "
              "interdit d'attribuer le mouvement au dispositif. La même inversion s'observe sur "
              "l'acceptabilité déclarée du vaccin : 66,9 → 77,4 % contre 76,8 → 79,5 %.")

    h2(doc, "5.3 La vaccination : ce qui est déclaré et ce qui est vu", number=None)
    para(doc, "La vaccination est le domaine où l'écart entre déclaration et vérification est le plus "
              "important. En zone témoin, 68,4 % des ménages déclarent leur enfant vacciné à T0, mais le "
              "carnet n'est vu que dans 37,0 % des cas : l'écart est de 31,4 points. À T1, il monte à 38,9 "
              "points. Au Sud-Kivu témoin, il atteint 54,7 points, avec 89,7 % de déclarations et 34,9 % de "
              "carnets vus.")
    figure(doc, f'{FIG}/f17.png', "Figure 7. Vaccination déclarée (évidé) et carnet vu (plein), par "
           "province, bras et passage.", width=16.4,
           note_txt="L'écart entre les deux séries n'est pas un taux de fausse déclaration : il mêle oubli "
                    "du carnet, perte, absence de mise à jour et déclaration approximative. "
                    "Source : T44_vaccination_declare_vu.")
    table(doc, "Tableau 22. Vaccination de l'enfant : déclaration et carnet vu, par province, bras et passage",
          ['Province', 'Bras', 'Passage', 'Vacciné déclaré (%)', 'Carnet vu (%)',
           'Écart déclaré − vu (points)'],
          sheet_rows('T44_vaccination_declare_vu', 'ABCDEF'),
          widths=[3.6, 2.8, 2.2, 3.2, 2.8, 3.4],
          size=7.2,
          note_txt="Source : T44_vaccination_declare_vu. L'écart est un écart de mesure, non un effet ; il "
                   "ne doit pas être lu comme une proportion de déclarations inexactes.")

    h2(doc, "5.4 Le continuum maternel", number=None)
    para(doc, "La cascade maternelle se lit en deux temps. Les niveaux d'abord : 89,9 % des femmes ayant eu "
              "une dernière grossesse ont fait au moins une consultation prénatale en zone témoin à T0, "
              "37,3 % au moins quatre, 88,0 % ont accouché en structure et 31,4 % sont revenues en "
              "consultation postnatale. Les transitions ensuite : parmi celles qui ont fait une "
              "consultation, 41,5 % en font quatre ; parmi celles qui en font quatre, 94,3 % accouchent en "
              "structure ; parmi celles qui accouchent en structure, 35,0 % reviennent six semaines après.")
    figure(doc, f'{FIG}/fig15_cascade.png', "Figure 8. Cascade maternelle du bras témoin à T0 : produit des "
           "étapes et co-couverture mesurée.", width=16.4,
           note_txt="Source : T40_continuum_conditionnel. Le produit des probabilités conditionnelles "
                    "(13,7 %) n'est pas la co-couverture (16,7 %) : la première isole chaque transition, la "
                    "seconde exige les quatre étapes chez la même femme.")
    table(doc, "Tableau 23. Continuum maternel : niveaux par étape, bras et passage",
          ['Population', 'Étape', 'Bras', 'Passage', '% [IC 95 %]', 'n'],
          [[r[0], r[1], r[2], r[3], r[4], r[5]]
           for r in sheet_rows('T39_continuum_maternel', 'ABCDEF')[:16]],
          widths=[4.4, 5.0, 2.2, 1.8, 3.2, 1.2],
          size=6.9,
          note_txt="Source : T39_continuum_maternel, population « toutes les femmes avec une dernière "
                   "grossesse ». Les naissances des six derniers mois sont publiées en annexe D.")
    para(doc, "L'évolution est contre-intuitive : la quatrième consultation prénatale recule en zone "
              "d'intervention (42,5 → 38,6 %) alors qu'elle progresse en zone témoin (37,3 → 41,5 %). La "
              "consultation postnatale, elle, progresse fortement en témoin (31,4 → 45,4 %) et modérément "
              "en intervention (31,4 → 38,8 %). Aucun de ces mouvements ne peut être attribué à l'appui : "
              "ils vont, sur ces deux étapes, dans le sens opposé à celui attendu.")

    h2(doc, "5.5 L'enfant malade : recours et délais", number=None)
    para(doc, "Devant un enfant malade dans les deux semaines précédentes, le centre de santé reste le "
              "premier recours dans les deux bras, à des niveaux différents : 48,5 % en témoin à T0, 60,7 % "
              "en intervention. L'automédication recule en intervention (19,1 → 14,1 %) et stagne en témoin "
              "(25,5 → 27,2 %). L'agent communautaire, enfin, progresse partout (8,9 → 16,4 % et 7,7 → "
              "13,1 %).")
    figure(doc, f'{FIG}/f16.png', "Figure 9. Première réaction devant l'enfant malade, par bras et par "
           "passage.", width=16.4,
           note_txt="Source : T41_enfant_malade_distributions, questionnaire ménages, enfants malades dans "
                    "les deux semaines. Les pourcentages sont calculés sur les enfants malades, non sur "
                    "l'ensemble des ménages.")
    table(doc, "Tableau 24. Première réaction devant l'enfant malade : distribution par bras et passage",
          ['Question', 'Bras', 'Passage', 'Agent communautaire', 'Attente', 'Automédication',
           'Centre de santé', 'Médecine traditionnelle'],
          [[r[0], r[1], r[2], r[3], r[4], r[5], r[8], r[9]]
           for r in sheet_rows('T41_enfant_malade_distributions', 'ABCDEFGHIJK')[:4]],
          widths=[2.8, 1.9, 1.7, 2.6, 1.9, 2.6, 2.6, 2.9],
          size=6.8,
          note_txt="Colonnes omises : « Autre » (moins de 1 %). Source : T41_enfant_malade_distributions. "
                   "Les effectifs varient de 637 à 823 enfants malades selon le bras et le passage.")
    para(doc, "Le modèle multinomial confirme la structure des recours sans établir de différence "
              "significative entre bras : le centre de santé capte 47,6 puis 40,5 % des recours en témoin, "
              "58,6 puis 61,1 % en intervention ; l'automédication, 26,5 puis 28,0 % contre 19,6 puis "
              "14,8 %. Les intervalles de confiance de ces probabilités se recouvrent.")

    h2(doc, "5.6 La Mpox : connaissances, sources et acceptabilité", number=None)
    para(doc, "Trois ménages sur quatre environ déclarent accepter le vaccin Mpox, et neuf sur dix parmi ceux "
              "qui connaissent la maladie. L'acceptabilité est donc moins un problème de refus qu'un "
              "problème de connaissance : connaître la Mpox multiplie par 4,4 les chances d'accepter le "
              "vaccin, savoir qu'un vaccin existe par 5,0.")
    table(doc, "Tableau 25. Déterminants de l'acceptation déclarée du vaccin Mpox (rapports de cotes ajustés)",
          ['Terme', 'Rapport de cotes', 'IC 95 %', 'p'],
          sheet_rows('T46_mpox_acceptabilite', 'ABCD'),
          widths=[6.6, 3.4, 3.6, 2.4],
          size=7.2,
          note_txt="Modèle logistique, n = 4 991. Les modalités de référence sont : ne connaît pas la Mpox, "
                   "ne sait pas qu'un vaccin existe, quintile 1, moins de 30 minutes de marche. "
                   "Source : T46_mpox_acceptabilite.")
    figure(doc, f'{FIG}/f18.png', "Figure 10. Connaissances et attitudes sur la Mpox, par item, bras et "
           "passage.", width=16.4,
           note_txt="Source : T45_mpox_cap. Les items sont regroupés en quatre blocs : connaissance de la "
                    "maladie, modes de transmission, prévention, sources d'information.")
    para(doc, "Deux effets de composition méritent attention. L'acceptabilité diminue avec le niveau de vie : "
              "0,47 [0,28 ; 0,77] pour le quintile le plus riche par rapport au plus pauvre. Elle diminue "
              "aussi avec la distance : 0,72 [0,62 ; 0,83] entre 30 et 60 minutes de marche. Autrement dit, "
              "les ménages les plus éloignés et les plus aisés sont les moins disposés à accepter un vaccin "
              "pourtant gratuit — un résultat à rapprocher de l'analyse d'équité du chapitre 8.")


def ch6(doc):
    page_break(doc)
    h1(doc, 6, 'Effet de l\'intervention', band=f'{FIG}/bands/b06.png')
    para(doc, "Ce chapitre est le cœur du rapport : il établit ce que l'appui a changé, en plus de ce qui "
              "serait advenu sans lui. Il présente le tableau des effets, les contrôles placebo et de "
              "tendance, l'estimation sur unités appariées, les 32 indicateurs secondaires et les indices de "
              "domaine. Toutes les estimations de ce chapitre relèvent du registre attribution.")

    h2(doc, "6.1 Le tableau des effets", number=None)
    para(doc, "Neuf indicateurs sont estimés : les quatre primaires et les cinq indices de domaine. Pour "
              "chacun, quatre estimateurs sont produits — différence de différences à seize points, "
              "permutation, modèle à effets fixes d'aire avec erreurs CR2, et bootstrap — afin de vérifier "
              "que la conclusion ne dépend pas de la méthode d'inférence.")
    table(doc, "Tableau 26. Tableau des effets : indicateurs primaires et indices de domaine",
          ['Indicateur', 'T0 T', 'T1 T', 'T0 I', 'T1 I', 'DiD 16 points [IC 95 %]', 'p perm.',
           'p t(11)', 'Modèle EF [IC CR2]', 'p Satt.'],
          [[r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]]
           for r in sheet_rows('T25_tableau_des_effets', 'ABCDEFGHIJ')],
          widths=[4.2, 1.1, 1.1, 1.1, 1.1, 3.2, 1.2, 1.2, 2.4, 1.2],
          size=6.4, head_size=6.0,
          note_txt="Lecture : T = bras témoin, I = bras intervention. Les quatre premières lignes sont les "
                   "primaires ; les cinq suivantes, les indices de domaine, exprimés en écarts-types. "
                   "Aucune estimation ne franchit le seuil de pertinence. Source : T25_tableau_des_effets.")
    para(doc, "Le résultat est homogène : les quatre primaires vont de −2,4 à +1,9 point, les intervalles "
              "contiennent tous zéro, et les estimations à effets fixes d'aire ne s'en écartent pas de plus "
              "de 1,4 point. La correction de Holm sur les quatre tests primaires donne 1,000. La conclusion "
              "n'est donc pas un artefact d'inférence.")
    figure(doc, f'{FIG}/f08.png', "Figure 11. Forêt des effets sur les indices de domaine et les quatre "
           "primaires, avec bande d'EMD et seuil de pertinence.", width=16.4,
           note_txt="Lecture : les carrés indiquent le point estimé, les traits l'intervalle à 95 % (CR2). "
                    "Le cas D est affiché lorsque l'intervalle traverse zéro ; les cas D et E ne "
                    "distinguent pas un effet nul d'un effet modeste non détectable. "
                    "Source : T25_tableau_des_effets.")

    h2(doc, "6.2 Les contrôles placebo", number=None)
    para(doc, "Six caractéristiques que l'appui ne visait pas ont été traitées comme des résultats "
              "placebos : taille du ménage, nombre d'enfants de moins de cinq ans, âge de la répondante, "
              "part des quintiles 1–2, part des ménages à plus d'une heure de marche, part des enfants "
              "malades. Aucune ne montre de différence établie, et les écarts vont dans les deux sens : "
              "c'est le comportement attendu si les bras sont comparables.")
    table(doc, "Tableau 27. Tests placebo : différence de différences sur des caractéristiques non ciblées",
          ['Caractéristique', 'T0 témoin', 'T0 intervention', 'DiD [IC 95 %]', 'p permutation'],
          sheet_rows('T28_placebos', 'ABCDE'),
          widths=[5.6, 2.6, 3.0, 3.6, 2.4],
          note_txt="Source : T28_placebos. Les écarts sur les variables continues sont exprimés dans leur "
                   "unité ; sur les variables dichotomiques, en points de pourcentage.")

    h2(doc, "6.3 La sensibilité à une divergence de tendance", number=None)
    para(doc, "L'hypothèse des tendances parallèles ne peut pas être testée : elle peut seulement être "
              "bornée. Le chapitre simule une divergence préexistante de ± 2 et ± 5 points — c'est-à-dire le "
              "cas où les zones d'intervention auraient progressé plus ou moins vite que les zones témoins, "
              "même sans appui.")
    table(doc, "Tableau 28. Effets corrigés d'une divergence de tendance préexistante, par indicateur",
          ['Indicateur', 'Divergence supposée (points)', 'DiD corrigée [IC 95 %]', 'Cas'],
          sheet_rows('T27_divergence_tendances', 'ABCD'),
          widths=[2.4, 4.2, 6.2, 2.0],
          size=7.2,
          note_txt="Lecture : une divergence de −5 points fait passer P1 au cas B (6,9 [0,6 ; 13,3]) ; une "
                   "divergence de +5 points fait passer les quatre primaires au cas E. La conclusion "
                   "« aucun effet établi » est donc robuste, mais la conclusion « aucun effet » ne l'est pas. "
                   "Source : T27_divergence_tendances.")

    h2(doc, "6.4 L'estimation sur unités appariées", number=None)
    para(doc, "Une seconde estimation restreint la comparaison aux unités présentes aux deux passages : 91 "
              "aires de santé pour les CODESA, 306 villages pour les CAC. L'estimation par ANCOVA, plus "
              "efficace, donne des valeurs plus élevées que la différence de différences simple, sans "
              "changer la conclusion.")
    table(doc, "Tableau 29. Effets estimés sur les unités territoriales appariées",
          ['Indicateur', 'Unités', 'DiD appariée [IC 95 %]', 'p', 'ANCOVA [IC 95 %]', 'p ANCOVA',
           'Coefficient de T0'],
          sheet_rows('T26_unites_appariees', 'ABCDEFG'),
          widths=[5.4, 1.4, 3.2, 1.2, 3.2, 1.4, 1.8],
          size=7.2,
          note_txt="Source : T26_unites_appariees. Le coefficient de T0 mesure la persistance du niveau "
                   "initial : 0,30 pour les CAC, 0,34 pour les CODESA.")

    h2(doc, "6.5 Les 32 indicateurs secondaires", number=None)
    para(doc, "Les indicateurs secondaires couvrent la connaissance du COSA, la visite à domicile, la "
              "participation au choix des agents, les signes de danger, la Mpox, la vaccination, le lavage "
              "des mains, le recours aux soins et le continuum maternel. Aucun ne résiste à la correction de "
              "Benjamini-Hochberg : la plus petite valeur corrigée est de 0,897.")
    figure(doc, f'{FIG}/f11.png', "Figure 12. Différences de différences sur les indicateurs secondaires, "
           "avec correction de Benjamini-Hochberg par famille.", width=16.4,
           note_txt="Lecture : les points pleins signalent les indicateurs dont la valeur de p brute est "
                    "inférieure à 0,05 ; aucun ne le reste après correction. "
                    "Source : T29_effets_secondaires.")
    table(doc, "Tableau 30. Indicateurs secondaires : différences de différences, valeurs de p brute et "
          "corrigée",
          ['Code', 'Indicateur', 'T0 T', 'T1 T', 'T0 I', 'T1 I', 'DiD [IC 95 %]', 'p perm.', 'p BH'],
          [[r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]]
           for r in sheet_rows('T29_effets_secondaires', 'ABCDEFGHI')],
          widths=[1.2, 5.0, 1.1, 1.1, 1.1, 1.1, 3.4, 1.3, 1.3],
          size=6.4, head_size=6.0,
          note_txt="Source : T29_effets_secondaires. Les 32 lignes sont publiées ici : ce sont elles qui "
                   "portent la démonstration d'absence d'effet secondaire, et les transférer en annexe "
                   "aurait affaibli le propos.")
    para(doc, "Trois résultats secondaires méritent d'être signalés parce qu'ils sont proches du seuil "
              "conventionnel sans l'atteindre : la consultation en moins de 24 heures parmi les consultants "
              "(−16,9 [−35,7 ; 1,8], p = 0,071), le recours formel en première réaction (+3,0 [−12,5 ; 18,5]) "
              "et la part des ménages consultant un service (+4,7 [−1,5 ; 10,8], p = 0,128). Aucun ne permet "
              "de conclure : les intervalles sont trop larges.")

    h2(doc, "6.6 Ce que le chapitre établit, et ce qu'il n'établit pas")
    bullets(doc, [
        "**Établi** : aucune différence d'évolution entre bras n'est détectable sur les quatre primaires ni "
        "sur les 32 secondaires, avec une puissance de 80 % pour des effets de 9 à 13 points.",
        "**Établi** : les deux bras progressent sur la quasi-totalité des indicateurs de ménages, et cette "
        "progression est de même ordre dans les deux bras.",
        "**Non établi** : l'absence d'effet. Le devis ne permet pas de distinguer un effet nul d'un effet "
        "de 5 points, qui serait pourtant pertinent pour la décision publique.",
        "**Non établi** : l'effet sur l'incidence de la Mpox, sur la couverture vaccinale réelle et sur la "
        "qualité des soins dispensés.",
    ])
    para(doc, "La formulation autorisée est donc : « l'appui n'a pas produit d'effet mesurable sur les "
              "indicateurs retenus, dans un dispositif capable de détecter des effets d'au moins 9 à 13 "
              "points ». La formulation interdite est : « l'appui n'a pas eu d'effet ».")


def ch7(doc):
    page_break(doc)
    h1(doc, 7, 'Mécanismes et analyse systémique', band=f'{FIG}/bands/b07.png')
    para(doc, "En l'absence d'effet établi, la question devient : par quoi les résultats passent-ils ? Ce "
              "chapitre relève du registre association. Il décrit ce qui va ensemble — fonctionnalité des "
              "organes et exposition des ménages, supervision et visites, prime et activité des agents — sans "
              "prétendre établir de causalité.")

    h2(doc, "7.1 Les associations transversales", number=None)
    para(doc, "Les associations les plus solides lient la fonctionnalité des CAC aux résultats des ménages : "
              "+2,9 points d'exposition et +3,0 points de connaissances par 10 points de fonctionnalité, avec "
              "des valeurs E de 1,62 et 1,64. La supervision des RECO est associée aux visites à domicile "
              "(+2,11 points par 10 points, valeur E 1,76), la prime n'étant pas associée.")
    table(doc, "Tableau 31. Associations entre fonctionnalité des organes, professionnalisation des agents "
          "et résultats des ménages",
          ['Résultat', 'Exposition', 'Coefficient / 10 points', 'IC 95 %', 'p', 'd standardisé',
           'Valeur E', 'n'],
          sheet_rows('T31_associations_transversales', 'ABCDEFGH'),
          widths=[4.2, 3.0, 2.6, 2.6, 1.3, 1.9, 1.6, 1.2],
          size=6.9,
          note_txt="La valeur E mesure la force de l'association qu'il faudrait pour qu'un facteur de "
                   "confusion non mesuré explique entièrement le résultat. Au-delà de 1,5, l'association "
                   "est considérée comme difficile à expliquer par un seul confondant. "
                   "Source : T31_associations_transversales.")
    para(doc, "Le résultat est cohérent avec la littérature sur les dispositifs communautaires : ce n'est pas "
              "l'intrant qui compte, mais le fonctionnement de l'organe qui le porte. Il ne prouve pas que "
              "rendre les CAC fonctionnels améliorerait l'exposition ; il indique où une intervention "
              "ultérieure aurait intérêt à agir et à mesurer.")

    h2(doc, "7.2 Les différences premières au niveau de l'aire", number=None)
    para(doc, "Une analyse plus exigeante compare, entre aires de santé, la variation d'un résultat à la "
              "variation d'un facteur. Les coefficients sont plus faibles, et deux seulement sont "
              "significatifs : la variation de fonctionnalité des CAC est associée à la variation de "
              "l'exposition (+0,40 [0,04 ; 0,76]) et à celle des connaissances (+0,30 [0,00 ; 0,60]).")
    table(doc, "Tableau 32. Différences premières : variation des résultats selon la variation des organes "
          "et des agents",
          ['Modèle', 'Variable', 'Coefficient', 'IC 95 %', 'p', 'Aires', 'R²'],
          sheet_rows('T30_differences_premieres_aires', 'ABCDEFG'),
          widths=[5.6, 1.6, 1.8, 2.4, 1.2, 1.2, 1.2],
          size=6.6,
          note_txt="Chaque ligne est un modèle estimé sur les aires appariées ; Δ désigne la variation entre "
                   "T0 et T1. Source : T30_differences_premieres_aires.")

    h2(doc, "7.3 Où se situe la variance ?", number=None)
    para(doc, "La décomposition de la variance indique que l'essentiel de la variation se situe au niveau "
              "des ménages et des aires, non des zones de santé : l'ICC d'aire va de 0,29 à 0,57, l'ICC de "
              "zone de 0,03 à 0,14. Autrement dit, deux aires d'une même zone se ressemblent moins que deux "
              "zones d'un même bras.")
    table(doc, "Tableau 33. Décomposition de la variance par niveau, par indicateur et par passage",
          ['Résultat', 'Passage', 'Variance aire', 'Variance ZS', 'Variance résiduelle', 'ICC aire',
           'ICC ZS'],
          [[r[0], r[1], _n(r[2], 1), _n(r[3], 1), _n(r[4], 1), _n(r[5], 2), _n(r[6], 2)]
           for r in sheet_rows('T32_variance_niveaux', 'ABCDEFG')],
          widths=[3.4, 2.0, 2.8, 2.6, 3.0, 1.8, 1.8],
          size=7.0,
          note_txt="ICC : part de la variance attribuable au niveau considéré. Source : "
                   "T32_variance_niveaux.")
    figure(doc, f'{FIG}/f12.png', "Figure 13. Effets aléatoires d'aire sur l'exposition des ménages (P1), "
           "par passage.", width=16.4,
           note_txt="Source : T33_effets_aires. Les effets d'aire sont centrés sur zéro ; leur dispersion "
                    "est plus large à T1 qu'à T0, ce qui traduit une divergence croissante entre aires.")
    para(doc, "Cette structure a une conséquence directe sur le devis : randomiser ou apparier au niveau des "
              "zones revient à ignorer l'essentiel de la variance. C'est la raison technique pour laquelle "
              "l'EMD est élevé, et l'argument principal en faveur d'un devis apparié au niveau de l'aire pour "
              "la phase 3.")

    h2(doc, "7.4 Ce qui produit des visites à domicile", number=None)
    para(doc, "Les visites déclarées par les RECO sur trois mois ont été modélisées en fonction de leur "
              "professionnalisation, de la prime et du contrat. La professionnalisation n'a pas d'effet "
              "(rapport de taux 1,00 [0,95 ; 1,06] par 10 points). La prime multiplie les visites par 1,84 "
              "[1,51 ; 2,24]. Le contrat, lui, n'est pas associé (0,85 [0,64 ; 1,11]).")
    table(doc, "Tableau 34. Visites à domicile déclarées selon la professionnalisation, la prime et le "
          "contrat (rapports de taux)",
          ['Variable', 'Rapport de taux', 'IC 95 %', 'p'],
          sheet_rows('T34_capacites_extrants_reco', 'ABCD'),
          widths=[8.0, 3.2, 3.2, 2.6],
          note_txt="Modèle de Poisson à effets fixes d'aire, période de référence de trois mois. "
                   "Source : T34_capacites_extrants_reco.")
    para(doc, "Ce résultat est le plus directement actionnable du rapport. Il ne dit pas que payer les "
              "agents suffit : il dit que, dans les données observées, la prime est le seul levier associé à "
              "l'activité, et que la formation, telle qu'elle est mesurée, ne l'est pas. Il rejoint le constat "
              "du chapitre 3 sur la stagnation des dotations.")


def ch8(doc):
    page_break(doc)
    h1(doc, 8, 'Équité', band=f'{FIG}/bands/b08.png')
    para(doc, "Un dispositif peut améliorer la moyenne et creuser les écarts. Ce chapitre examine la "
              "distribution des résultats selon le niveau de vie, le sexe, l'instruction et la distance, avec "
              "un double point de vue : les inégalités de niveau (concentration) et les inégalités d'effet "
              "(hétérogénéité).")

    h2(doc, "8.1 Les inégalités de niveau", number=None)
    para(doc, "L'indice de concentration d'Erreygers mesure si un indicateur est plus fréquent chez les "
              "riches (valeur positive) ou chez les pauvres (valeur négative). La vaccination déclarée est "
              "nettement concentrée chez les ménages aisés en zone d'intervention à T0 (0,309 [0,003 ; "
              "0,592]), et l'accouchement en structure l'est dans les deux bras (0,163 et 0,207).")
    table(doc, "Tableau 35. Concentration des indicateurs de résultats (indice d'Erreygers), par bras et "
          "passage",
          ['Indicateur', 'Bras', 'Passage', "Indice d'Erreygers", 'IC 95 %'],
          sheet_rows('T36_concentration_erreygers', 'ABCDE'),
          widths=[6.8, 2.4, 2.0, 3.0, 2.8],
          size=7.0,
          note_txt="Un indice positif indique une concentration chez les ménages les mieux classés. "
                   "Source : T36_concentration_erreygers.")
    para(doc, "La concentration recule en zone d'intervention entre les deux passages — de 0,180 à 0,054 "
              "pour l'exposition, de 0,233 à 0,133 pour les connaissances, de 0,309 à 0,158 pour la "
              "vaccination déclarée — et reste stable ou s'aggrave en zone témoin. C'est le seul domaine où "
              "le sens du mouvement diffère entre les bras, et il mérite d'être suivi dans la phase 3.")

    h2(doc, "8.2 Le gradient par quintile de niveau de vie", number=None)
    para(doc, "Les courbes par quintile montrent un gradient net pour l'accouchement en structure, plus "
              "faible pour la vaccination, et un gradient inverse pour l'exposition aux agents, plus élevée "
              "chez les ménages modestes. Les séries ne sont pas monotones : les ruptures d'un quintile à "
              "l'autre atteignent 10 points.")
    figure(doc, f'{FIG}/fig14_quintiles.png', "Figure 14. Gradient par quintile de niveau de vie, par bras "
           "et par passage.", width=16.4,
           note_txt="Source : T37_gradient_quintiles. Quintiles calculés sur la base regroupée, T0 et T1 "
                    "confondus ; pondération égale des provinces. Les échelles sont communes aux quatre "
                    "panneaux, sauf pour l'indice de connaissances (0–100).")
    table(doc, "Tableau 36. Accouchement en structure de santé par quintile de niveau de vie, bras et "
          "passage (%)",
          ['Bras', 'Passage', 'Q1 (plus bas)', 'Q2', 'Q3', 'Q4', 'Q5 (plus haut)'],
          _quint('Accouchement en structure de santé (%)'),
          widths=[3.0, 2.2, 2.6, 2.2, 2.2, 2.2, 2.8],
          note_txt="Source : T37_gradient_quintiles. Les effectifs par cellule vont de 240 à 330 ménages.")


def _quint(ind):
    d = {}
    for r in X['T37_gradient_quintiles']['rows'][1:]:
        c = r['cells']
        if c.get('F') == ind:
            d[(c['A'], c['B'], c['C'])] = round(float(c['D']), 1)
    out = []
    for bras in ('Témoin', 'Intervention'):
        for pas in ('T0', 'T1'):
            out.append([bras, pas] + [_n(d.get((bras, pas, q), float('nan')), 1)
                                      for q in (1, 2, 3, 4, 5)])
    return out


def ch8_suite(doc):
    h2(doc, "8.3 Les inégalités d'effet : l'hétérogénéité pré-spécifiée", number=None)
    para(doc, "Les sous-groupes ont été fixés avant l'analyse : quintiles 1–2 contre 3–5, instruites contre "
              "sans instruction, moins d'une heure de marche contre une heure et plus. Aucun test global "
              "d'hétérogénéité n'atteint le seuil conventionnel ; les valeurs de p vont de 0,121 à 0,979.")
    table(doc, "Tableau 37. Hétérogénéité pré-spécifiée de l'effet sur P1 et P2, par sous-groupe",
          ['Résultat', 'Sous-groupe', 'Niveau', 'n', 'DiD 16 points', 'IC 95 %', 'p hétérogénéité'],
          sheet_rows('T35_heterogeneite', 'ABCDEFG'),
          widths=[1.8, 2.0, 4.8, 1.4, 2.2, 2.8, 2.4],
          size=7.2,
          note_txt="Source : T35_heterogeneite. Les comparaisons par province ne sont pas testées : deux "
                   "zones par bras et par province, soit quatre unités, ne permettent aucune inférence.")
    figure(doc, f'{FIG}/f13.png', "Figure 15. Différences de différences par sous-groupe pré-spécifié et "
           "test global d'hétérogénéité.", width=16.4,
           note_txt="Source : T35_heterogeneite. Les intervalles des sous-groupes se recouvrent largement, "
                    "ce qui est cohérent avec l'absence d'effet moyen.")
    para(doc, "Deux signaux faibles méritent d'être notés sans être surinterprétés : l'effet estimé sur P1 "
              "est plus élevé chez les ménages sans instruction (+8,6) et chez ceux qui vivent à plus d'une "
              "heure de marche (+9,4). Si ces écarts étaient confirmés, ils indiqueraient un appui plus "
              "efficace auprès des ménages les plus éloignés — l'inverse d'un effet Matthieu. Le rapport ne "
              "les retient pas comme résultats : les intervalles contiennent zéro et les tests "
              "d'hétérogénéité ne sont pas significatifs.")

    h2(doc, "8.4 Genre et milieu", number=None)
    para(doc, "Les effets estimés ne diffèrent pas selon le sexe de la répondante, et les écarts entre "
              "milieu urbain et rural ne sont pas testables : la part de ménages urbains est inférieure à "
              "3 % dans les deux bras. La sous-représentation des femmes parmi les agents, documentée au "
              "chapitre 4, ne se traduit donc pas, dans ces données, par un accès différencié aux services.")
    para(doc, "Cette absence d'écart doit être lue avec prudence : elle porte sur des indicateurs de "
              "déclaration, non sur des indicateurs de qualité de prise en charge. Le rapport ne peut pas "
              "conclure à l'équité du dispositif ; il conclut à l'absence d'inégalité détectable sur les "
              "indicateurs mesurés.")
