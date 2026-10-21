# -*- coding: utf-8 -*-
"""Résumé exécutif, chapitres 1 et 2."""
from base import *
from docx.shared import Pt, Cm


def resume(doc):
    h1(doc, '', 'Résumé exécutif', band=f'{FIG}/bands/b00_resume.png')
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    run(p, "Rapport de résultats quantitatifs · Phase 2 · SACO / Mpox · République démocratique du Congo",
        size=9, color=GREY, italic=True)

    para(doc, "Ce rapport présente les résultats quantitatifs de la phase 2 du projet SACO sur la riposte "
              "à la Mpox dans quatre provinces de la République démocratique du Congo : Maniema, "
              "Kasaï-Oriental, Sankuru et Sud-Kivu. Il compare seize zones de santé, huit dans lesquelles "
              "l'appui a été déployé et huit zones témoins, à deux passages espacés de cinq mois et demi, "
              "auprès de 5 713 ménages, 576 RECO, 177 ASC, 573 CAC et 96 CODESA. Il répond à une question "
              "simple : ce que l'appui a apporté peut-il être distingué de ce qui serait advenu sans lui ?")

    para(doc, "La réponse est non, pour les quatre indicateurs primaires retenus avant l'analyse. Les quatre "
              "indicateurs progressent dans les deux bras. Aucun écart entre bras n'est établi : les estimations "
              "de différence de différences vont de −2,4 à +1,9 point, leurs intervalles de confiance contiennent "
              "tous zéro et tous chevauchent le seuil de pertinence de 10 à 13 points fixé a priori. Les quatre "
              "conclusions résistent à 14 à 19 variantes selon l'indicateur, sans qu'aucune ne fasse apparaître "
              "d'effet établi. Ce résultat négatif n'est pas un échec de "
              "l'intervention : c'est le constat d'un dispositif de mesure à seize grappes, dimensionné pour "
              "détecter des effets d'au moins 9 à 13 points, sur une intervention dont les effets attendus étaient "
              "plus modestes.")

    h2(doc, "Les quatre résultats confirmatoires", number=None)
    bullets(doc, [
        "**P1 — Exposition des ménages aux agents.** 65,3 → 69,3 en zone témoin, 62,2 → 69,2 en zone "
        "d'intervention ; DiD 1,9 [−4,4 ; 8,3], p = 0,506 ; modèle à effets fixes d'aire 3,1 [−4,2 ; 10,5]. "
        "EMD : 10,1 points.",
        "**P2 — Connaissances des ménages.** 30,3 → 38,9 (témoin), 33,4 → 40,3 (intervention) ; DiD −1,9 "
        "[−8,8 ; 5,1], p = 0,628. EMD : 10,0 points.",
        "**P3 — Fonctionnalité des CAC.** 66,9 → 70,4 (témoin), 75,6 → 79,4 (intervention) ; DiD 0,3 "
        "[−6,0 ; 6,6], p = 0,915. EMD : 8,8 points.",
        "**P4 — Professionnalisation des RECO.** 35,6 → 38,7 (témoin), 41,6 → 42,3 (intervention) ; DiD −2,4 "
        "[−11,9 ; 7,1], p = 0,690. EMD : 13,3 points.",
    ])
    para(doc, "Après correction de Holm sur les quatre tests, toutes les valeurs de p ajustées valent 1,000. "
              "Sur les 32 indicateurs secondaires, la plus petite valeur de p corrigée par Benjamini-Hochberg "
              "est de 0,897. Aucun effet n'est établi à quelque niveau que ce soit.")

    figure(doc, f'{FIG}/f01.png', "Figure 1. Forêt des effets sur les quatre indicateurs primaires : "
           "différence de différences à seize points (bleu marine), modèle à effets fixes d'aire (cyan), "
           "intervalle de confiance à 95 %, seuil de pertinence (tiret) et EMD (bande).", width=16.4,
           note_txt="Lecture : un intervalle qui traverse zéro et le seuil ne permet ni d'établir un effet ni "
                    "d'exclure un effet pertinent. Source : T25_tableau_des_effets, T10_emd_par_bras.")

    callout(doc, "CE QU'IL FAUT RETENIR",
            ["Les quatre primaires progressent, dans les deux bras, de 3 à 8 points en cinq mois et demi. "
             "L'appui n'ajoute rien de mesurable à cette progression, mais le rapport ne peut pas non plus "
             "affirmer qu'il n'ajoute rien : l'effectif de seize zones ne permet pas de trancher en dessous "
             "de 9 à 13 points.",
             "Trois mécanismes ressortent néanmoins, sur les registres association et attribution partielle : "
             "la fonctionnalité des CAC est associée à l'exposition des ménages et à leurs connaissances "
             "(+2,9 et +3,0 points par 10 points de fonctionnalité), la supervision des RECO est associée à "
             "leurs visites à domicile (rapport de taux 1,76), et la prime est associée à un doublement des "
             "visites (1,84 [1,51 ; 2,24]). Ces associations ne sont pas des effets de l'appui : elles "
             "décrivent ce qui, dans le dispositif, va de pair avec les résultats."])

    h2(doc, "Ce que le rapport apporte de neuf")
    bullets(doc, [
        "**Un tableau des effets unique et traçable.** Les valeurs publiées ici sont celles du classeur "
        "d'analyse, vérifiées ligne à ligne ; les chiffres du résumé de la maquette antérieure étaient, sur "
        "trois des quatre primaires, issus d'une autre spécification (voir annexe A).",
        "**Trois figures qui manquaient ou qui étaient vides** : la cascade maternelle par étape et par "
        "province, la synthèse des normes du PSN SACO, les unités en progression et en régression par zone.",
        "**Un principe de lecture explicite** : chaque tableau porte son registre (évolution, association, "
        "attribution) et la population sur laquelle il est calculé. Aucune valeur n'est présentée sans son "
        "intervalle ni son effectif.",
        "**Un volume resserré** : les tableaux de détail par zone, les matrices de sensibilité et les "
        "fiches sont renvoyés en annexe, et plusieurs tableaux de séries sont remplacés par des figures. "
        "Aucun résultat n'est retiré du corps du rapport.",
    ])

    h2(doc, "Les cinq recommandations qui découlent des chiffres")
    bullets(doc, [
        "**Redimensionner le devis avant la phase 3.** Pour détecter un effet de 5 points sur P1 avec la "
        "variabilité observée, il faudrait environ 60 zones par bras. À défaut, mesurer les effets là où ils "
        "sont attendus : sur les unités effectivement exposées, avec un devis apparié à une seule grappe.",
        "**Traiter la prime et le contrat comme le levier principal.** La prime est le seul intrant associé "
        "de façon forte et cohérente aux visites à domicile ; elle reste versée à 24 % des ASC et son montant "
        "médian est de 30 USD en intervention contre 10 USD en zone témoin.",
        "**Ne pas conditionner l'appui aux indicateurs de volume.** Les zones d'intervention partaient d'un "
        "niveau plus élevé sur P3 et P4 : conditionner l'appui à leur progression relative pénaliserait les "
        "zones les mieux dotées.",
        "**Sécuriser le carnet de vaccination.** L'écart entre vaccination déclarée et carnet vu atteint "
        "54,7 points au Sud-Kivu témoin à T1 : la déclaration ne peut pas servir d'indicateur de résultat "
        "sans contrôle documentaire.",
        "**Publier les résultats négatifs.** Le rapport est diffusable comme description d'une progression "
        "collective et comme analyse des mécanismes ; il ne peut pas être présenté comme la démonstration de "
        "l'efficacité de l'appui.",
    ])


def ch1(doc):
    page_break(doc)
    h1(doc, 1, 'Méthodologie', band=f'{FIG}/bands/b01.png')
    para(doc, "Ce chapitre expose le devis, les bases, la construction des indicateurs et les règles "
              "d'inférence. Il indique aussi, dès l'ouverture, ce que le dispositif permet de conclure et ce "
              "qu'il ne permet pas : c'est la condition de lecture de tout ce qui suit.")

    h2(doc, "1.1 Le devis et ce qu'il permet d'établir", number=None)
    para(doc, "L'étude compare seize zones de santé réparties dans quatre provinces, à deux passages. Huit "
              "zones ont reçu l'appui, huit ont été suivies sans appui. Les deux passages sont espacés de "
              "cinq mois et demi : le premier de mars à avril 2026, le second de fin août à septembre 2026. "
              "Chaque zone est documentée par cinq questionnaires : ménages, RECO, ASC, CAC et CODESA.")
    figure(doc, f'{FIG}/devis.png', "Figure 2. Chronologie du devis, appariement des zones et logique "
           "d'inférence.", width=16.4,
           note_txt="Source : protocole d'enquête, passage T0 (mars–avril 2026) et T1 (août–septembre 2026).")
    para(doc, "Le devis est un avant-après avec comparaison. Il identifie l'effet de l'appui sous l'hypothèse "
              "que, sans l'appui, les zones d'intervention auraient suivi la même évolution que les zones "
              "témoins. Cette hypothèse n'est pas testable directement ; le chapitre 11 la met à l'épreuve en "
              "simulant des divergences de tendance préexistantes de ± 2 et ± 5 points. Trois registres de "
              "lecture en découlent, et chaque tableau du rapport porte le sien.")

    h3(doc, "Trois registres, trois portées")
    table(doc, "Tableau 1. Les trois registres de lecture et ce qu'ils autorisent à écrire",
          ['Registre', 'Question posée', 'Ce qui est calculé', 'Ce que l\'on peut écrire'],
          [["Évolution", "Qu'est-ce qui a changé, dans un bras, une province, une zone ?",
            "Comparaison T0 → T1, avec intervalle de confiance", "« a progressé de x points »"],
           ["Association", "Qu'est-ce qui va ensemble, au même moment ou entre deux variations ?",
            "Effets d'aire, différences premières, coefficients transversaux",
            "« est associé à », jamais « entraîne »"],
           ["Attribution", "Qu'est-ce que l'appui a changé en plus de ce qui serait advenu ?",
            "Différence de différences à seize points, réservée aux primaires et aux indices D1–D3",
            "« effet estimé », avec son intervalle et son EMD"]],
          widths=[2.6, 5.4, 4.6, 4.4],
          note_txt="La règle est appliquée sans exception : un résultat d'association n'est jamais présenté "
                   "comme un effet, et un résultat d'évolution n'est jamais présenté comme une attribution.")

    h2(doc, "1.2 Les bases, les passages et l'appariement", number=None)
    para(doc, "Les cinq bases ne se lisent pas au même niveau. Les ménages sont échantillonnés en grappes "
              "dans les villages ; les RECO, ASC et CAC sont enquêtés individuellement ; les CODESA sont "
              "documentés au niveau de l'aire de santé. Les effectifs effectivement analysés diffèrent donc "
              "des effectifs enquêtés, et le rapport donne toujours le dénominateur utilisé.")
    table(doc, "Tableau 2. Entretiens réalisés et appariement entre les deux passages",
          ['Base', 'Unités à T0', 'Unités à T1', 'Unités appariées', "Taux d'appariement (% de T0)"],
          sheet_rows('T01_bilan_appariement', 'ABCDE'),
          widths=[4.6, 2.8, 2.8, 3.0, 3.8],
          note_txt="Lecture : les villages ne sont pas des unités appariables une à une (les grappes de "
                   "ménages changent) ; les aires de santé, elles, le sont à plus de 95 %. "
                   "Source : T01_bilan_appariement.")
    para(doc, "Deux constats de qualité doivent être posés d'entrée. Les dates de collecte comportent des "
              "valeurs aberrantes : treize entretiens ménages à T0 et onze à T1 sont hors de la fenêtre "
              "prévue, dont quelques-uns remontent à 2022 et 2023. Ces entretiens sont conservés dans "
              "l'analyse principale, et retirés dans une variante de sensibilité (chapitre 11) : la conclusion "
              "ne change pas. Les bases agents, elles, sont propres : une seule date hors fenêtre, côté RECO "
              "à T0.")
    table(doc, "Tableau 3. Fenêtres de collecte et entretiens hors fenêtre, par base et par passage",
          ['Base', 'Passage', 'n', 'Première date', 'Dernière date', 'Hors fenêtre'],
          [[r[0], r[1], r[2], str(r[3])[:10], str(r[4])[:10], r[5]]
           for r in sheet_rows('T05_dates_collecte', 'ABCDEF')],
          widths=[3.4, 2.0, 2.0, 3.2, 3.2, 3.2],
          note_txt="Source : T05_dates_collecte. Les dates sont celles de l'entretien, non celles de la "
                   "saisie ; la fenêtre contractuelle est de six semaines par passage.")

    h2(doc, "1.3 La construction des indicateurs", number=None)
    para(doc, "Les quatre indicateurs primaires ont été fixés avant l'analyse. P1 mesure l'exposition des "
              "ménages aux agents sur une échelle 0–100, construite à partir de la visite à domicile, de la "
              "participation aux animations et de la connaissance des agents. P2 mesure les connaissances "
              "déclarées, sur 24 items, également ramenées sur 0–100. P3 note la fonctionnalité des CAC sur "
              "neuf critères et P4 la professionnalisation des RECO sur six items, dont quatre hors intrants.")
    para(doc, "Trois indices de domaine complètent le dispositif : D1 gouvernance communautaire, D2 capacités "
              "des acteurs, D3 résultats des ménages, tous exprimés en écarts-types. Ils sont lus en "
              "attribution, mais avec une réserve : leurs composantes sont aussi des résultats de l'appui, ce "
              "qui rend l'interprétation circulaire. Le rapport les traite donc comme des indices de "
              "description, jamais comme des preuves.")
    table(doc, "Tableau 4. Qualité des indices composites : cohérence interne et structure",
          ['Indice', 'Items', 'n', 'Alpha (KR-20)', 'Oméga', 'Corrélation inter-items'],
          sheet_rows('T08_fiabilite_indices', 'ABCDEF'),
          widths=[6.6, 1.8, 1.8, 2.6, 1.8, 2.4],
          note_txt="Lecture : les indices principaux dépassent 0,90 ; l'indice de connaissances Mpox, plus "
                   "court, reste au-dessus de 0,69. Source : T08_fiabilite_indices.")
    para(doc, "La fiabilité n'est pas uniforme entre les bras : l'alpha du score de signes de danger vaut 0,841 "
              "à T0 en zone d'intervention contre 0,901 en zone témoin, puis 0,927 contre 0,916 à T1. Cette "
              "asymétrie initiale, corrigée à T1, invite à ne pas lire les évolutions de cet indice au point "
              "près.")

    h2(doc, "1.4 Effet minimal détectable et seuils de pertinence", number=None)
    para(doc, "Un résultat non significatif n'est pas un résultat nul. Pour distinguer les deux, l'effet "
              "minimal détectable (EMD) a été calculé pour chaque indicateur, à partir de la variabilité "
              "intra-province des seize évolutions de zone. Il indique la taille d'effet que le devis aurait "
              "pu détecter avec une puissance de 80 %.")
    table(doc, "Tableau 5. Effet minimal détectable par indicateur, sur les seize zones, sans et avec le bras",
          ['Indicateur', 'ZS', 'Unités / ZS', 'T0', 'T1', 'Écart brut', 'EMD sans bras', 'EMD avec bras', 'r T0–T1'],
          [[r[0], r[1], r[2], r[3], r[4], r[5], r[7], r[9], r[10]]
           for r in sheet_rows('T10_emd_par_bras', 'ABCDEFGHIJK')[:10]],
          widths=[5.6, 1.0, 1.5, 1.1, 1.1, 1.6, 1.7, 1.7, 1.5],
          size=7.0,
          note_txt="EMD = (t₀,₉₇₅;₁₁ + t₀,₈₀;₁₁) × σΔ × √(1/8 + 1/8), où σΔ est l'écart-type intra-province "
                   "des seize évolutions de zone. Source : T10_emd_par_bras. Les dix premiers indicateurs "
                   "sont publiés ici ; la liste complète figure en annexe D.")
    para(doc, "Le résultat est net : l'EMD va de 8,8 points pour la fonctionnalité des CAC à 13,3 points pour "
              "la professionnalisation des RECO. Les écarts bruts observés sur les quatre primaires vont de "
              "1,9 à 7,7 points, tous inférieurs à l'EMD de leur indicateur. Le devis ne pouvait donc pas "
              "mettre en évidence des effets de l'ordre de grandeur de ceux que l'appui pouvait "
              "raisonnablement produire.")

    h2(doc, "1.5 Estimation et inférence à seize grappes", number=None)
    para(doc, "L'estimation principale est un modèle conjoint avec interaction bras × passage, la différence "
              "de différences portant sur seize points (huit zones par bras). Trois précautions gouvernent "
              "l'inférence. D'abord, la valeur de p est calculée par permutation des seize étiquettes de "
              "zone, et non par un test asymptotique : avec huit grappes par bras, les approximations "
              "normales sont fragiles. Ensuite, un modèle à effets fixes d'aire avec erreurs robustes en "
              "grappes (CR2) sert de contrôle, parce qu'il absorbe l'hétérogénéité fixe des aires. Enfin, "
              "une correction de Holm est appliquée aux quatre tests primaires, et une correction de "
              "Benjamini-Hochberg aux 32 indicateurs secondaires.")
    table(doc, "Tableau 6. Grille de lecture des effets (cas A à E)",
          ['Cas', 'Configuration de l\'intervalle à 95 %', 'Lecture'],
          [["A", "Entièrement au-dessus du seuil de pertinence", "effet établi et pertinent"],
           ["B", "Au-dessus de zéro, mais traversant le seuil", "établi, pertinence incertaine"],
           ["C", "Au-dessus de zéro, entièrement sous le seuil", "établi, sous le seuil"],
           ["D", "Traversant zéro", "indéterminé"],
           ["E", "Entièrement au-dessous du seuil, y compris négatif", "gain ≥ seuil non soutenu ; "
                 "baisse non exclue si l'intervalle est négatif"]],
          widths=[1.2, 8.2, 7.6],
          note_txt="Seuils de pertinence : 10 points pour P1 et P2, 5 points pour P3, 11 points pour P4. "
                   "La grille est appliquée telle quelle dans tous les chapitres.")
    para(doc, "Les quatre primaires relèvent du cas D ou E. Aucune ne relève de A, B ou C. Une divergence de "
              "tendance de −5 points ferait passer P1 au cas B (6,9 [0,6 ; 13,3]) et une divergence de "
              "+5 points la ferait passer au cas E (−3,1 [−9,4 ; 3,3]) : la conclusion est donc sensible au "
              "signe et à l'ampleur de la divergence préexistante, ce que le chapitre 11 documente "
              "précisément.")

    h2(doc, "1.6 Ce que le rapport ne fait pas", number=None)
    bullets(doc, [
        "Il ne mesure pas l'effet de l'appui sur l'incidence de la Mpox : les cas déclarés par zone ne sont "
        "pas disponibles à une granularité compatible avec le devis.",
        "Il ne compare pas les zones d'intervention aux zones témoins sur des indicateurs de santé "
        "biologiques : aucune mesure biologique n'a été collectée.",
        "Il ne restitue pas de données individuelles : toutes les analyses sont agrégées au niveau de la "
        "zone, de l'aire ou du bras, et les tableaux publient des effectifs, jamais des identifiants.",
        "Il ne tranche pas entre les effets de l'appui et ceux d'autres interventions simultanées dans les "
        "mêmes provinces ; le chapitre 11 montre l'ampleur de cette incertitude.",
        "Il ne fournit pas de pagination définitive : la maquette ne conserve pas de pagination, et les "
        "renvois de page du sommaire sont à recalculer après mise en page.",
    ])
    para(doc, "Les conditions de production sont réunies pour un usage interne et pour la discussion avec "
              "les partenaires. Elles ne le sont pas pour une communication publique présentant l'appui "
              "comme ayant produit les progressions observées : le chapitre 13 détaille les formulations "
              "autorisées.")


def _ds(v):
    try:
        return f'{float(str(v).replace(",", ".")):.2f}'.replace('.', ',')
    except Exception:
        return ''


def ch2(doc):
    page_break(doc)
    h1(doc, 2, 'Profil des échantillons et comparabilité', band=f'{FIG}/bands/b02.png')
    para(doc, "Avant de comparer des évolutions, il faut établir que les deux bras étaient comparables au "
              "départ et que la composition des échantillons n'a pas changé entre les passages. Ce chapitre "
              "présente les profils, les différences standardisées et l'effet de la repondération.")

    h2(doc, "2.1 Les ménages", number=None)
    para(doc, "Les 5 713 ménages enquêtés se répartissent en 2 857 à T0 et 2 856 à T1, à parts égales entre "
              "les deux bras. La répondante a en moyenne 30 à 31 ans ; le ménage compte 7,1 personnes en zone "
              "témoin et 6,1 en zone d'intervention. Une différence de niveau d'instruction apparaît d'emblée : "
              "16,4 % des répondantes n'ont aucune instruction en zone témoin contre 31,0 % en zone "
              "d'intervention (différence standardisée 0,35).")
    table(doc, "Tableau 7. Profil des ménages par bras et par passage",
          ['Caractéristique', 'T0 témoin', 'T0 intervention', 'DS T0', 'T1 témoin', 'T1 intervention',
           'DS T1'],
          [[r[0], r[1], r[2], r[3], r[4], r[5], r[6]]
           for r in sheet_rows('T11_profil_menages', 'ABCDEFG')],
          widths=[6.2, 1.8, 2.0, 1.4, 1.8, 2.0, 1.4],
          size=7.0,
          note_txt="DS : différence standardisée entre bras (témoin moins intervention), en unités d'écart-type. "
                   "Une valeur supérieure à 0,20 en valeur absolue signale un déséquilibre. Les effectifs sont "
                   "de 1 428 et 1 429 ménages à T0, 1 433 et 1 423 à T1. Source : T11_profil_menages.")
    para(doc, "Quatre variables dépassent le seuil conventionnel de 0,20 : l'instruction, la taille du ménage, "
              "le milieu urbain et le temps de marche vers la formation sanitaire. Ces écarts ne sont pas "
              "corrigés par appariement, faute d'unités appariables au niveau des ménages ; ils sont traités "
              "par ajustement dans les modèles et par une variante de repondération. Ils n'expliquent pas les "
              "résultats du chapitre 6, mais ils interdisent de lire les niveaux bruts comme des niveaux "
              "comparables.")

    h2(doc, "2.2 Les acteurs et les organes", number=None)
    para(doc, "Les acteurs communautaires présentent des profils contrastés. Les ASC sont plus âgés en zone "
              "témoin (44,5 ans contre 39,5) et plus souvent titulaires d'un diplôme d'État (40,7 % contre "
              "26,6 %), deux différences standardisées de −0,40 et −0,30 à T0. Les CODESA sont présidés par "
              "des hommes dans plus de neuf cas sur dix, et la part des femmes parmi les membres progresse "
              "dans les deux bras (25,9 → 29,0 % en témoin, 26,4 → 30,1 % en intervention).")
    table(doc, "Tableau 8. Profil des agents et des organes par bras et par passage",
          ['Base', 'Caractéristique', 'T0 témoin', 'T0 intervention', 'DS T0', 'T1 témoin',
           'T1 intervention', 'DS T1'],
          [[r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]]
           for r in sheet_rows('T12_profil_acteurs', 'ABCDEFGH')],
          widths=[1.8, 5.2, 1.7, 1.9, 1.2, 1.7, 1.9, 1.2],
          size=7.0,
          note_txt="Source : T12_profil_acteurs. Les RECO sont 288 par bras et par passage, les ASC 90 et 87 "
                   "à T0, 71 et 78 à T1, les CAC 290 et 288, les CODESA 48 par bras et par passage.")

    h2(doc, "2.3 L'équilibre à T0 et son évolution", number=None)
    para(doc, "Les différences standardisées se réduisent entre les passages pour la plupart des covariables "
              "ménages : la composition des échantillons devient plus proche. Deux exceptions notables : le "
              "milieu urbain, dont la différence standardisée passe de −0,05 à 0,18 du fait de l'arrivée de "
              "ménages urbains dans l'échantillon d'intervention à T1, et P3, dont la différence "
              "standardisée reste élevée (0,38 à T0, 0,43 à T1).")
    table(doc, "Tableau 9. Différences standardisées entre bras à T0 et à T1, covariables et primaires",
          ['Caractéristique', 'DS T0', 'DS T1', 'Groupe'],
          [[r[0], _ds(r[1]), _ds(r[2]), r[3]] for r in sheet_rows('T13_equilibre_T0', 'ABCD')],
          widths=[9.0, 2.4, 2.4, 3.2],
          size=7.2,
          note_txt="Source : T13_equilibre_T0. P3 et P4 sont structurellement déséquilibrés : les zones "
                   "d'intervention étaient mieux dotées au départ, ce qui borne à la baisse ce que l'appui "
                   "pouvait ajouter.")

    h2(doc, "2.4 Attrition, repondération et ce que cela change", number=None)
    para(doc, "L'attrition est nulle au niveau des zones : aucune zone perdue, aucun bras modifié en cours "
              "de route. Elle est forte au niveau des grappes de ménages, avec un taux d'appariement de "
              "56 % entre les deux passages, mais les grappes ne sont pas l'unité d'analyse : les ménages "
              "sont renouvelés à chaque passage dans les mêmes zones, et le rapport ne suit pas de cohorte "
              "de ménages. Les aires de santé, en revanche, sont appariables à plus de 95 %.")
    para(doc, "Une repondération de T1 sur la composition de T0 (province × instruction × quintile) a été "
              "appliquée aux primaires. Elle déplace les évolutions de 0,1 à 1,5 point (P1 témoin : 4,0 → 4,8 ; "
              "P2 témoin : 8,8 → 7,3) et ne modifie aucune conclusion ; le détail figure dans la matrice de "
              "sensibilité du chapitre 11. La conclusion "
              "générale de ce chapitre est donc que la comparabilité est suffisante pour comparer des "
              "évolutions avec ajustement, mais insuffisante pour comparer des niveaux sans ajustement.")


def ch3(doc):
    page_break(doc)
    h1(doc, 3, 'Gouvernance communautaire', band=f'{FIG}/bands/b03.png')
    para(doc, "Les CODESA sont l'organe de gouvernance de l'aire de santé. Leur fonctionnalité conditionne "
              "la reconnaissance des agents, la tenue des réunions de monitorage et l'accès aux dotations. "
              "Ce chapitre décrit leur état, leurs transitions entre les deux passages et leur conformité aux "
              "normes du plan national.")

    h2(doc, "3.1 Un niveau élevé, qui progresse dans les deux bras", number=None)
    para(doc, "La fonctionnalité moyenne des CODESA progresse de 71,1 à 75,9 sur 100 dans le bras témoin "
              "et de 76,2 à 81,0 dans le bras intervention : +4,8 points dans un bras comme dans l'autre. "
              "La différence de différences est donc nulle, au point près, et les intervalles des deux "
              "évolutions sont très larges (−19,1 à 28,6 en témoin, −16,8 à 26,3 en intervention). "
              "L'appui n'ajoute rien à une progression qui est celle des deux bras.")
    table(doc, "Tableau 10. Indicateurs CODESA : valeurs à T0 et à T1, écart, ensemble et par bras",
          ['Indicateur', 'Groupe', 'T0 [IC 95 %]', 'n T0', 'T1 [IC 95 %]', 'n T1', 'Écart [IC 95 %]'],
          [[r[0], r[1], r[2], r[3], r[4], r[5], r[6]]
           for r in sheet_rows('T14_cod_3volets', 'ABCDEFG')[1:]],
          widths=[5.4, 1.7, 2.5, 1.0, 2.5, 1.0, 2.9],
          size=6.9,
          note_txt="Source : T14_cod_3volets. Les intervalles sont à 95 %, calculés par bootstrap en "
                   "grappes ; les effectifs sont ceux des CODESA documentés, 96 par passage.")
    para(doc, "La lecture par catégorie précise le mouvement : les CODESA non fonctionnels reculent de 16,7 "
              "à 10,4 % en zone d'intervention et de 18,8 à 22,9 % en zone témoin. Autrement dit, la "
              "progression n'est pas un déplacement homogène : elle correspond à la sortie de la catégorie "
              "basse dans un bras, et à une entrée dans cette catégorie dans l'autre.")
    table(doc, "Tableau 11. Répartition des CODESA et des CAC par catégorie de fonctionnalité",
          ['Organe', 'Bras', 'Passage', 'Catégorie', 'Effectif', '%'],
          [[r[0], r[1], r[2], r[3], r[4], r[5]] for r in sheet_rows('T16_categories_organes', 'ABCDEF')],
          widths=[2.2, 2.6, 2.0, 6.4, 2.0, 1.8],
          size=7.2,
          note_txt="Catégories : moins de 50 % des critères (non fonctionnel), 50 à 79 % (partiellement), "
                   "80 % et plus (fonctionnel). Source : T16_categories_organes.")

    h2(doc, "3.2 Les transitions : ce qui bouge et ce qui ne bouge pas", number=None)
    para(doc, "Les matrices de transition portent sur les aires appariées, 45 en témoin et 45 en "
              "intervention pour les CODESA. Dans le bras intervention, six aires non fonctionnelles sur huit "
              "quittent cette catégorie, dont quatre deviennent fonctionnelles ; dans le bras témoin, sept "
              "des neuf aires non fonctionnelles le restent. À l'autre extrémité, vingt et une aires "
              "fonctionnelles sur vingt-six le demeurent en intervention, seize sur vingt-deux en témoin.")
    figure(doc, f'{FIG}/fig05_codesa.png', "Figure 3. Transitions des CODESA entre catégories de "
           "fonctionnalité, aires appariées, de T0 à T1.", width=16.4,
           note_txt="Les catégories sont définies sur le pourcentage de critères satisfaits (moins de 50 %, "
                    "50 à 79 %, 80 % et plus). Les effectifs par case figurent dans le tableau 12. "
                    "Source : T20_transitions_matrices.")
    table(doc, "Tableau 12. Unités appariées en dégradation, stabilité et amélioration, par bras",
          ['Organe', 'Bras', 'Dégradation', 'Stabilité', 'Amélioration', '% dégradation', '% stabilité',
           '% amélioration'],
          sheet_rows('T21_mouvements_unites', 'ABCDEFGH'),
          widths=[2.4, 2.4, 2.2, 2.0, 2.4, 2.2, 2.0, 2.4],
          size=7.2,
          note_txt="Lecture : la dégradation est plus fréquente en zone témoin pour les CAC (32,7 % contre "
                   "22,4 %), mais l'amélioration est presque aussi fréquente dans les deux bras (33,3 % "
                   "contre 34,7 %). Source : T21_mouvements_unites.")
    para(doc, "Le résultat mérite d'être souligné parce qu'il contredit une lecture linéaire de l'appui : "
              "dans les deux bras, un tiers des CAC progressent et un quart à un tiers régressent. Le solde "
              "est légèrement favorable au bras intervention, de 12,3 points de pourcentage contre 0,6 en "
              "témoin, mais l'écart n'est pas testé au niveau des unités, faute de puissance.")

    h2(doc, "3.3 La conformité aux normes du plan national", number=None)
    para(doc, "Le PSN SACO 2025-2030 fixe vingt normes opposables aux organes et aux agents. Sur ces vingt "
              "normes, deux seulement sont assorties d'une cible chiffrée dans le plan, et dix-huit ne le "
              "sont pas : la conformité se lit donc en niveau et en évolution, pas en atteinte d'une cible.")
    figure(doc, f'{FIG}/fig02_normes.png', "Figure 4. Conformité aux normes du PSN SACO à T0 (évidé) et à "
           "T1 (plein), par bras.", width=16.4,
           note_txt="Source : T51_normes_psn. La figure reprend les vingt normes ; les valeurs chiffrées "
                    "figurent au chapitre 10, tableau 39.")
    para(doc, "Trois familles de normes se comportent différemment. La désignation et la tenue des réunions "
              "progressent partout : RECO élu en assemblée de 47,9 à 56,4 % en témoin et de 64,6 à 77,9 % en "
              "intervention ; réunions mensuelles des CODESA de 83,3 à 93,8 % et de 87,5 à 95,8 %. Les "
              "dotations d'intrants stagnent ou reculent : la part des ASC percevant une prime passe de 31,1 "
              "à 22,5 % en témoin et de 26,4 à 24,4 % en intervention. Les contrats restent marginaux : 9,4 % "
              "des RECO témoins et 13,0 % des RECO d'intervention en ont un à T1.")

    h2(doc, "3.4 L'indice de conformité : un niveau bas, une pente faible", number=None)
    para(doc, "L'indice de conformité rapporte le nombre de normes respectées au nombre de normes "
              "applicables. Il vaut 41,7 à T0 et 45,0 à T1 pour les RECO témoins, 47,6 et 50,0 pour les RECO "
              "d'intervention ; pour les ASC, 33,4 et 38,0 contre 39,4 et 40,5. Les intervalles se recouvrent "
              "dans les deux cas.")
    table(doc, "Tableau 13. Indice de conformité des agents aux normes du PSN SACO (0–100)",
          ['Agent', 'Bras', 'Passage', 'Indice de conformité [IC 95 %]', 'n'],
          sheet_rows('T52_indice_conformite', 'ABCDE'),
          widths=[4.2, 3.0, 2.4, 5.4, 2.0],
          note_txt="L'indice rapporte les normes respectées aux normes applicables à l'agent. Être conforme "
                   "n'est pas être efficace : le chapitre 7 montre que l'indice n'est pas associé aux "
                   "extrants. Source : T52_indice_conformite.")
    para(doc, "Un agent sur deux respecte donc la moitié des normes qui le concernent. Ce niveau n'est pas "
              "une mesure de qualité du travail : il mesure l'écart entre un référentiel national ambitieux "
              "et les conditions matérielles dans lesquelles les agents exercent. Le chapitre 10 discute "
              "cette distinction, essentielle pour l'usage du tableau de bord national.")


def ch4(doc):
    page_break(doc)
    h1(doc, 4, 'Acteurs communautaires', band=f'{FIG}/bands/b04.png')
    para(doc, "Les CAC, les RECO et les ASC sont les trois maillons de l'appui. Ce chapitre décrit leur "
              "fonctionnement, leurs moyens et leur reconnaissance, en distinguant systématiquement ce qui "
              "relève de l'évolution et ce qui relève de l'association.")

    h2(doc, "4.1 Les CAC : une progression réelle, un écart non établi", number=None)
    para(doc, "La fonctionnalité des CAC progresse de 66,9 à 70,4 en zone témoin et de 75,6 à 79,5 en zone "
              "d'intervention. Les deux bras partaient de niveaux différents — la différence standardisée "
              "initiale est de 0,38 — et l'écart d'évolution n'est pas établi (0,3 [−6,0 ; 6,6]).")
    table(doc, "Tableau 14. Indicateurs CAC : valeurs à T0 et à T1, écart, ensemble et par bras",
          ['Indicateur', 'Groupe', 'T0 [IC 95 %]', 'n T0', 'T1 [IC 95 %]', 'n T1', 'Écart [IC 95 %]'],
          [[r[0], r[1], r[2], r[3], r[4], r[5], r[6]]
           for r in sheet_rows('T14_cac_3volets', 'ABCDEFG')[1:]],
          widths=[5.4, 1.7, 2.5, 1.0, 2.5, 1.0, 2.9],
          size=6.9,
          note_txt="Source : T14_cac_3volets. Neuf critères composent l'indice ; les effectifs sont de 290 "
                   "CAC à T0 et 288 à T1.")
    para(doc, "Deux composantes portent la progression : la tenue de réunions de monitorage (80,4 → 86,0 % "
              "en témoin, 89,2 → 92,6 % en intervention) et la disposition d'un plan d'action (58,2 → 57,3 % "
              "et 75,0 → 80,3 %). Les critères qui supposent des ressources — subsides de fonctionnement, "
              "équipements — ne progressent pas, et reculent même en zone témoin (44,2 → 36,7 %).")
    figure(doc, f'{FIG}/f06.png', "Figure 5. Transitions des CAC entre catégories de fonctionnalité, "
           "villages appariés, de T0 à T1.", width=16.4,
           note_txt="Source : T20_transitions_matrices, 306 villages appariés. Les cases décrivent des "
                    "trajectoires, non des effets.")
    para(doc, "La lecture des trajectoires confirme que le mouvement est général : 33,3 % des CAC témoins "
              "s'améliorent et 32,7 % se dégradent ; 34,7 % des CAC d'intervention s'améliorent et 22,4 % se "
              "dégradent. Le brassage est donc intense dans les deux bras, ce qui rend les comparaisons de "
              "moyennes fragiles et plaide pour une lecture par unité, comme au chapitre 12.")

    h2(doc, "4.2 Les RECO : une professionnalisation qui plafonne", number=None)
    para(doc, "La professionnalisation des RECO progresse de 35,6 à 38,7 en témoin et de 41,6 à 42,3 en "
              "intervention. L'écart d'évolution est de −2,4 [−11,9 ; 7,1] : aucune conclusion d'attribution "
              "n'est possible.")
    figure(doc, f'{FIG}/f03.png', "Figure 6. RECO enquêtés par zone de santé à T0 et à T1.", width=16.4,
           note_txt="Les effectifs varient de 6 à 28 RECO par zone selon les zones et les passages ; aucune "
                    "zone n'est perdue. Source : T02_realisation_zs.")
    table(doc, "Tableau 15. Composantes de la professionnalisation des RECO, par bras et par passage",
          ['Composante', 'Bras', 'Passage', 'Valeur [IC 95 %]', 'n'],
          [[r[0], r[1], r[2], r[3], r[4]] for r in sheet_rows('T47_reco_professionnalisation_c', 'ABCDE')],
          widths=[5.0, 3.0, 2.2, 4.8, 1.6],
          size=7.0,
          note_txt="Chaque composante est notée sur 0–100. La formation initiale recule en intervention "
                   "(83,0 → 73,0), du fait du renouvellement des RECO. Source : "
                   "T47_reco_professionnalisation_components.")
    para(doc, "Trois composantes expliquent le plafonnement. La certification reste rare : 10,8 % des RECO "
              "témoins et 13,3 % des RECO d'intervention déclarent un certificat de formation à T1. Le "
              "contrat avec le ministère reste marginal : 9,4 et 13,0 %. La prime de motivation, enfin, est "
              "déclarée par 13,9 et 13,0 % des RECO. La formation sur le paquet, elle, progresse dans les "
              "deux bras (47,9 et 59,7 %).")

    h2(doc, "4.3 La charge des RECO et la prime des ASC", number=None)
    para(doc, "La charge en ménages est stable : la médiane du nombre de ménages couverts par un RECO passe "
              "de 35 à 40 en zone témoin et reste à 50 en zone d'intervention. La part des RECO couvrant plus "
              "de 100 ménages augmente dans les deux bras (22,9 → 24,4 % et 16,7 → 23,9 %), ce qui éloigne "
              "durablement de la norme d'un RECO pour cinquante ménages.")
    table(doc, "Tableau 16. RECO : nombre de ménages couverts et concentration intra-zone",
          ['Bras', 'Passage', 'n', 'Médiane', 'Q1', 'Q3', '≤ 50 ménages (%)', '> 100 ménages (%)',
           'Gini intra-ZS'],
          sheet_rows('T49_reco_charge_menages', 'ABCDEFGHI'),
          widths=[2.2, 1.8, 1.2, 1.8, 1.4, 1.4, 2.6, 2.6, 2.0],
          size=7.0,
          note_txt="Source : T49_reco_charge_menages. Le Gini intra-zone mesure l'inégalité de répartition "
                   "des ménages entre RECO d'une même zone.")
    para(doc, "La prime des ASC est le point le plus discriminant du dispositif. Le montant médian déclaré "
              "est de 30 USD en zone d'intervention, contre 10 USD en zone témoin, et 73,7 % des ASC "
              "d'intervention perçoivent au moins 30 USD à T1, contre 25,0 % des ASC témoins. Cette "
              "différence est le seul écart d'intrants franc du dispositif, et c'est aussi celui qui "
              "s'accompagne des associations les plus fortes avec les visites à domicile (chapitre 7).")
    table(doc, "Tableau 17. ASC : montant déclaré de la prime de motivation (USD), parmi ceux qui en perçoivent",
          ['Bras', 'Passage', 'n', 'Médiane', 'Q1', 'Q3', '≥ 30 USD (%)'],
          sheet_rows('T48_asc_prime_montant', 'ABCDEFG'),
          widths=[2.6, 2.2, 1.6, 2.4, 2.0, 2.0, 4.2],
          note_txt="Les effectifs sont faibles (16 à 28 ASC par bras et par passage) : les montants sont des "
                   "ordres de grandeur déclarés, non des montants versés. Source : T48_asc_prime_montant.")

    h2(doc, "4.4 Logistique, intrants et ruptures", number=None)
    para(doc, "Les ruptures de stock au centre de santé touchent une majorité d'aires dans les deux bras. "
              "Elles sont déclarées par 61,5 % des RECO témoins et 54,8 % des RECO d'intervention à T1, et "
              "par 66,7 % des ASC témoins et 63,2 % des ASC d'intervention. Aucune tendance nette ne se "
              "dégage : les écarts entre passages sont du même ordre que les écarts entre bras.")
    table(doc, "Tableau 18. Logistique et intrants des agents et des CAC, par bras et par passage",
          ['Base', 'Indicateur', 'Bras', 'Passage', 'Valeur [IC 95 %]', 'n'],
          [[r[0], r[1], r[2], r[3], r[4], r[5]] for r in sheet_rows('T50_logistique', 'ABCDEF')],
          widths=[1.8, 5.8, 2.4, 2.0, 3.8, 1.2],
          size=6.9,
          note_txt="Source : T50_logistique. Les intervalles très larges traduisent la faible taille des "
                   "effectifs d'ASC et l'hétérogénéité entre aires.")
    para(doc, "Le tableau appelle une remarque de méthode : les pourcentages de ruptures de stock ne sont pas "
              "comparables entre RECO et ASC, car les premiers répondent pour leur centre de santé de "
              "rattachement, les seconds pour l'aire entière. Le rapport publie les deux, mais ne les "
              "agrège pas.")

    h2(doc, "4.5 La place des femmes", number=None)
    para(doc, "La part des femmes parmi les agents reste minoritaire et stable : 28,5 → 30,3 % parmi les RECO "
              "témoins, 27,8 → 29,5 % parmi les RECO d'intervention ; 20,0 → 16,9 % et 19,5 → 16,7 % parmi les "
              "ASC. La cible de parité du plan national n'est donc atteinte par aucun bras, et l'écart ne se "
              "referme pas.")
    table(doc, "Tableau 19. Part des femmes parmi les agents, les membres et les répondants des organes",
          ['Acteur', 'Bras', 'Passage', 'Part des femmes (%)', 'n'],
          sheet_rows('T38_genre', 'ABCDE'),
          widths=[5.0, 3.0, 2.2, 4.4, 1.8],
          size=7.0,
          note_txt="Source : T38_genre. Les organes sont représentés par leur répondant, généralement le "
                   "président ; la part des femmes parmi les membres figure séparément pour les CODESA.")
    para(doc, "L'analyse de genre du chapitre 8 montre que cette sous-représentation ne s'accompagne pas d'un "
              "écart d'accès aux services pour les ménages : les effets estimés ne diffèrent pas selon le "
              "sexe de la répondante. Elle reste néanmoins un enjeu de conformité au plan national.")
