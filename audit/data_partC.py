# -*- coding: utf-8 -*-
"""Données de la Partie C : décision sur les onglets du classeur SACO Phase 2.
Colonnes : onglet, objet, lignes de données, n° tableau du rapport (maquette 2026-10-19),
diagnostic, décision (A/B/C/D/E), emplacement recommandé, justification.
A = conserver dans le corps ; B = simplifier ; C = remplacer par une figure ;
D = remplacer par un tableau de synthèse ; E = déplacer en annexe.
"""

DECISIONS = [
("Catalogue", "Catalogue des sorties (code, type, titre, script, registre, population, note)", 92, "—",
 "Métadonnée de production, non publiable telle quelle ; 71 entrées « tableau », 20 « figure », 1 « fiche » alors que le rapport numérote 60 tableaux et 20 figures.",
 "Hors rapport (document de travail)",
 "Annexe G — complétée par la correspondance onglet → tableau du rapport",
 "Aucune entrée ne renvoie au numéro du rapport : la traçabilité annoncée en annexe G est rompue."),

("T01_bilan_appariement", "Bilan de l'appariement territorial T0/T1", 7, "Tableau 4",
 "7 lignes utiles, mais deux bases différentes (villages et aires) cohabitent sous le même libellé « ménages » (688 villages, taux 56 %) sans que le mot « villages » apparaisse ; le contraste 56 % / 97,8 % n'est pas expliqué.",
 "B", "Corps, chapitre 2 — tableau 4 conservé et scindé en deux blocs (villages / aires)",
 "Le taux d'appariement est un résultat en soi et conditionne l'annexe des unités appariées : il doit rester visible, mais l'unité d'analyse doit être nommée."),

("T02_realisation_zs", "Réalisation par ZS, questionnaire et passage", 17, "Tableau 3",
 "15 colonnes pour 17 lignes ; contient une ligne fantôme (province Kasaï-Oriental, ZS vide, CAC T1 = 1) reprise telle quelle dans le rapport ; colonne UCODESA presque vide (0 ou 1).",
 "B", "Corps, chapitre 2 — 6 colonnes (ménages, RECO, ASC, CAC, CODESA) + ligne fantôme supprimée ; UCODESA en note",
 "Tableau de contrôle qualité : il doit rester dans le corps car il porte l'argument de comparabilité, mais sa lisibilité est atteinte par la largeur et par l'artefact."),

("T03_asc_couverture", "Couverture ASC par province", 4, "Tableau 50 (annexe C)",
 "Quatre lignes mais un dénominateur absent (48 %, 43 %, 60 %, 26 % de quoi ?) ; baisse de 14 points au Sankuru et de 11 au Maniema non commentée.",
 "D", "Corps, chapitre 2 (3 lignes commentées) + annexe C pour la version détaillée",
 "Le déficit d'ASC à T1 est une limite explicite du rapport (chapitre 4) : il ne peut pas rester une annexe muette sans dénominateur."),

("T04_qualite_manquants", "Qualité : valeurs manquantes par variable", 58, "Tableau 51 (annexe C)",
 "58 lignes de codes de variables (L1, L7, S01Q07…) sans libellé d'indicateur ; les manquants structurels (W2 : 29,8 % / 22,2 %) ne sont pas distingués des manquants réels.",
 "E", "Annexe C — ajout d'une colonne « libellé » et d'une colonne « nature du manquant »",
 "Tableau de diagnostic exhaustif : sa place est en annexe, à condition d'être lisible et relié au dictionnaire (tableau 46)."),

("T05_dates_collecte", "Dates de collecte et entretiens hors fenêtre", 10, "Tableau 2",
 "Dates exportées en numéros de série Excel (44828, 46305) : illisibles ; 10 lignes pour 5 bases × 2 passages.",
 "B", "Corps, chapitre 1 — 5 lignes (une par base), dates formatées, colonne « hors fenêtre » conservée",
 "Preuve de la fenêtre de collecte et du contrôle qualité : utile au lecteur méthodologique, inutile en dix lignes."),

("T06_fiches_indicateurs", "Dictionnaire des indicateurs", 88, "Tableau 46 (annexe B)",
 "88 indicateurs, indispensable, mais trois libellés coexistent pour un même indice (P2 : « connaissances » dans le corps, « connaissances déclarées (citations) » dans la maquette) ; les dénominateurs ne figurent pas dans une colonne dédiée.",
 "E", "Annexe B — ajout des colonnes « dénominateur », « unité », « libellé court normalisé »",
 "Référentiel de lecture : il doit rester en annexe mais devenir la source unique des libellés employés dans tout le rapport."),

("T07_poids_indices_domaine", "Poids des composantes des indices de domaine", 23, "Tableau 47 (annexe B)",
 "La composition de D3 diffère entre le classeur (6 composantes, dont recours formel) et le rapport (5 composantes) ; les poids ne sont pas les mêmes (P1 0,177 vs 0,218).",
 "D", "Annexe B — tableau de synthèse 4 lignes (indice, nombre de composantes, poids minimal/maximal) + composition détaillée en annexe",
 "Une divergence de composition d'indice est une erreur de définition, pas un détail de présentation : elle doit être visible en synthèse."),

("T08_fiabilite_indices", "Fiabilité des indices réflexifs", 8, "Tableau 48 (annexe B)",
 "8 lignes, deux populations mélangées (L10 global n = 5713 et L10 par bras/passage n ≈ 1 428).",
 "B", "Annexe B — 4 lignes principales (alpha, oméga) + 4 lignes de contrôle d'invariance",
 "Bon tableau, mal hiérarchisé : le lecteur doit voir d'abord la fiabilité de l'indice, ensuite le contrôle par sous-groupe."),

("T09_irt_signes_danger", "Paramètres IRT des 18 signes de danger", 18, "Tableau 49 (annexe B)",
 "Discrimination jusqu'à 3,41 et difficulté jusqu'à 4,51 (item 16) sans commentaire sur les items extrêmes ni sur les items non informatifs.",
 "E", "Annexe B — tri par difficulté, items extrêmes signalés",
 "Tableau technique de validation ; en annexe, mais il doit porter une phrase d'interprétation."),

("T10_emd_par_bras", "EMD par indicateur, sans et avec bras", 23, "Tableau 1",
 "23 lignes × 11 colonnes pour dire qu'aucun effet inférieur à 9-38 points n'est détectable ; deux lignes portent le même libellé (« CODESA : indice de riposte Mpox ») avec des effectifs incompatibles (6 et 36 unités par ZS).",
 "C", "Corps, chapitre 1 — figure « EMD et seuil de pertinence par indicateur » (barres appariées) + tableau 6 lignes",
 "Le message du tableau est un classement de précision, pas une lecture ligne à ligne : c'est un cas d'école de remplacement par une figure."),

("T11_profil_menages", "Profil des ménages et équilibre (DS)", 21, "Tableau 5",
 "Mélange d'unités dans une même colonne : « Milieu urbain (%) » vaut 0,42 / 2,16 (proportions) alors que « Enfant malade (%) » vaut 36,06 (pourcentage) ; âge et DS différents du classeur (30,13 vs 30,11 ; DS 0,18 vs 0,13).",
 "B", "Corps, chapitre 2 — 12 lignes (âge, instruction, taille, quintiles, distance, morbidité) ; religion en annexe",
 "Tableau de comparabilité : il doit rester dans le corps mais ne peut pas mélanger deux échelles dans une colonne étiquetée %."),

("T12_profil_acteurs", "Profil des agents et des organes (DS)", 12, "Tableau 6",
 "12 lignes, colonnes T1 vides pour les CAC (H = 0, F/G absents) : la structure du tableau laisse croire à une absence de mesure alors qu'il s'agit de coupes répétées.",
 "B", "Corps, chapitre 2 — 8 lignes ; cellules vides remplacées par « nd » motivé",
 "Utile à la comparabilité des agents, mais la vacuité des cellules CAC est une source de contresens."),

("T13_equilibre_T0", "Équilibre à T0 (différences standardisées)", 26, "Figure 4 (source)",
 "Contient le résultat le plus lourd du chapitre 2 : P3 DS = 0,376 et P4 DS = 0,275 à T0, au-delà du seuil de 0,25 que le rapport définit lui-même comme « déséquilibre à ajuster » ; non repris dans le texte ni dans le titre de la figure.",
 "C", "Corps, chapitre 2 — figure 4 recadrée (5 indicateurs primaires en tête) + encadré « déséquilibres à T0 »",
 "Le déséquilibre des deux indicateurs primaires d'offre est une objection majeure à l'interprétation des DiD : il doit être visible, pas enfoui dans une figure de 22 lignes."),

("T14_asc_3volets_complet", "Trois volets ASC — version complète (15 groupes)", 120, "—",
 "Version longue (Ensemble, bras, provinces, bras × province) non utilisée par le rapport.",
 "E", "Annexe D — réservé aux besoins de vérification",
 "Conserver pour la traçabilité, sans publication."),

("T14_asc_3volets", "Trois volets ASC (ensemble et bras)", 24, "Tableau 15",
 "24 lignes = 8 indicateurs × 3 volets ; les IC de l'écart diffèrent systématiquement du classeur (ex. supervision : [-7,6 ; 23,2] dans le classeur, [-6,4 ; 22,0] dans le rapport) sans que la méthode soit documentée.",
 "B", "Corps, chapitre 4 — 8 lignes (un indicateur par ligne, trois colonnes de groupes) + note d'IC",
 "La structure « trois volets » est le principal obstacle de lecture du rapport : elle doit être transposée en colonnes, pas en lignes répétées."),

("T14_cac_3volets_complet", "Trois volets CAC — version complète", 225, "—",
 "Version longue non utilisée ; sert de base à la figure 6 et aux fiches.",
 "E", "Annexe D",
 "Traçabilité."),

("T14_cac_3volets", "Trois volets CAC (ensemble et bras)", 45, "Tableau 7",
 "45 lignes = 15 indicateurs × 3 volets ; les IC de l'écart du rapport sont plus étroits que ceux du classeur pour 42 des 45 lignes (ex. indice de riposte : [-16,2 ; 20,9] vs [-14,7 ; 19,4]).",
 "B", "Corps, chapitre 3 — 10 indicateurs en lignes, 3 groupes en colonnes ; 5 indicateurs secondaires en annexe",
 "Tableau central du chapitre 3 mais illisible en l'état et non reproductible."),

("T14_cod_3volets_complet", "Trois volets CODESA — version complète", 165, "—",
 "Version longue non utilisée.",
 "E", "Annexe D",
 "Traçabilité."),

("T14_cod_3volets", "Trois volets CODESA (ensemble et bras)", 33, "Tableau 8",
 "33 lignes = 11 indicateurs × 3 volets ; n très faibles (96 CODESA, 48 par bras) et IC de ±20 à ±30 points : les écarts ne sont pas interprétables, ce que le tableau ne dit pas.",
 "B", "Corps, chapitre 3 — 8 lignes + bandeau « n = 96, IC de ±20 points : aucune conclusion d'écart »",
 "Le tableau doit rester, mais avec un avertissement de puissance visible plutôt qu'en note de bas de tableau."),

("T14_men_3volets_complet", "Trois volets ménages — version complète", 480, "—",
 "480 lignes (32 indicateurs × 15 groupes) : c'est la matrice la plus riche du classeur, non publiée.",
 "E", "Annexe D + source des figures de synthèse",
 "Doit devenir la source des figures du chapitre 5 et des fiches, pour éviter les recalculs divergents."),

("T14_men_3volets", "Trois volets ménages (ensemble et bras)", 96, "Tableau 18",
 "96 lignes = 32 indicateurs × 3 volets ; doublon partiel du tableau 53 (129 lignes) ; c'est le tableau le plus long du corps du rapport.",
 "D", "Corps, chapitre 5 — tableau de synthèse 12 lignes (indicateurs prioritaires) + figure dumbbell ; 96 lignes en annexe D",
 "Un tableau de 96 lignes ne peut pas porter un message : il faut choisir 12 indicateurs et renvoyer le reste en annexe, sans perte d'information."),

("T14_reco_3volets_complet", "Trois volets RECO — version complète", 285, "—",
 "Version longue non utilisée ; contient les composantes utiles aux fiches.",
 "E", "Annexe D",
 "Traçabilité."),

("T14_reco_3volets", "Trois volets RECO (ensemble et bras)", 57, "Tableau 12",
 "57 lignes = 19 indicateurs × 3 volets ; IC de l'écart plus étroits que le classeur pour 51 des 57 lignes.",
 "B", "Corps, chapitre 4 — 10 lignes ; 9 indicateurs en annexe D",
 "Même diagnostic que les tableaux 7 et 15 : mise en colonnes et sélection."),

("T15_asc_3volets_province", "Trois volets ASC par province", 32, "—",
 "32 lignes non publiées ; nécessaire pour situer une zone dans sa province (fiches).",
 "E", "Annexe D + alimentation des fiches",
 "Support des fiches, pas du corps."),

("T15_cac_3volets_province", "Trois volets CAC par province", 60, "—",
 "60 lignes non publiées ; les IC par province atteignent ±40 points (n ≈ 143 par province).",
 "E", "Annexe D — avec avertissement de puissance",
 "Ne pas publier au corps : les IC y sont trop larges pour être comparés."),

("T15_cod_3volets_province", "Trois volets CODESA par province", 44, "—",
 "44 lignes non publiées ; n ≈ 24 CODESA par province.",
 "E", "Annexe D",
 "Effectifs trop faibles pour une lecture par province."),

("T15_men_3volets_province", "Trois volets ménages par province", 128, "Tableau 53 (annexe D)",
 "128 lignes = 32 indicateurs × 4 provinces ; doublon de structure avec le tableau 18.",
 "E", "Annexe D — conservé tel quel mais avec en-tête de colonnes explicite",
 "Le passage « par bras » puis « par province » est la bonne logique ; c'est le volume qui impose l'annexe."),

("T15_reco_3volets_province", "Trois volets RECO par province", 76, "—",
 "76 lignes non publiées ; n = 144 RECO par province.",
 "E", "Annexe D",
 "Traçabilité."),

("T16_categories_organes", "Catégories de fonctionnalité des organes", 24, "Tableau 9",
 "24 lignes = 2 organes × 2 bras × 2 passages × 3 catégories : trois dimensions en lignes pour une information qui est une composition.",
 "C", "Corps, chapitre 3 — barres empilées 100 % (organe × bras × passage) + tableau 4 lignes",
 "Une composition se lit en barres empilées, pas en 24 lignes ; le message (part de non-fonctionnels divisée par deux dans le bras intervention) est perdu."),

("T17_ucodesa", "UCODESA : composition", 30, "Tableau 59 (annexe D)",
 "30 lignes (15 UCODESA × 2 passages) pour une seule variable (part de femmes), avec des effectifs de 2 à 8 membres.",
 "C", "Annexe D + micro-figure en fiche de zone",
 "La variable est trop instable (0 % à 50 % sur 3 à 8 membres) pour un tableau : une figure par zone suffit."),

("T18_evolutions_longues", "Évolutions par bras et province (format long)", 330, "—",
 "Tableau de travail (22 indicateurs × 15 groupes) destiné aux figures ; non publiable.",
 "E", "Annexe D ou hors rapport (document de production)",
 "Ce n'est pas un tableau de rapport : c'est la matière première des figures 7, 10 et 13."),

("T19_16_zones_complet", "16 zones — version complète (13 variables)", 208, "—",
 "13 variables × 16 zones, avec valeurs brutes (y) et résidualisées (r) : seul endroit où les deux définitions coexistent.",
 "E", "Annexe D + source unique des fiches et de la figure des pentes",
 "Doit devenir la source officielle des colonnes « évolution ajustée » aujourd'hui non reproductibles."),

("T19_16_zones_P1", "16 zones — P1 exposition", 16, "Tableau 21",
 "16 lignes, 10 colonnes ; l'« évolution ajustée » diffère pour 10 des 16 zones de celle du rapport (Kibombo 4,7 vs 4,8 ; Pangi -0,6 vs -0,8).",
 "B", "Corps, chapitre 6 — 6 colonnes (T0, T1, n, évolution brute, évolution ajustée, écart) + figure des pentes",
 "Le tableau est bon ; c'est la reproductibilité de la colonne ajustée qui doit être rétablie."),

("T19_16_zones_P2", "16 zones — P2 connaissances", 16, "Tableau 54 (annexe D)",
 "« Évolution ajustée » différente pour 9 des 16 zones ; T0 révisé pour Kibombo (20,4 vs 23,7) et Tunda (14,4 vs 15,0).",
 "B", "Annexe D — avec renvoi à l'annexe A pour les valeurs de T0 révisées",
 "Tableau correct en annexe, mais les valeurs de T0 doivent être expliquées : c'est l'objet de l'annexe A, aujourd'hui vide."),

("T19_16_zones_P3", "16 zones — P3 fonctionnalité CAC", 16, "Tableau 22",
 "Reproductible (aucun écart) ; 16 lignes, 10 colonnes.",
 "B", "Corps, chapitre 6 — 6 colonnes ; figure commune avec P1",
 "Seul tableau de zone entièrement cohérent avec le classeur : il peut servir de modèle de mise en forme."),

("T19_16_zones_P4", "16 zones — P4 professionnalisation RECO", 16, "Tableau 55 (annexe D)",
 "Reproductible ; en annexe alors qu'il porte la dispersion la plus forte (-13,5 à +22,1 points).",
 "A", "Corps, chapitre 6 — déplacé de l'annexe vers le corps, en figure",
 "L'indicateur le plus dispersé est le plus informatif pour l'action : sa place est dans le corps."),

("T20_transitions_matrices", "Matrices de transition (unités appariées)", 36, "Tableau 10",
 "36 lignes = 2 organes × 2 bras × 9 transitions ; les 9 transitions sont déjà représentées par les figures 5 et 6.",
 "E", "Annexe D — tableau conservé comme source chiffrée des figures 5 et 6",
 "Double emploi avec les figures ; le corps n'a besoin que des effectifs de mouvement."),

("T21_mouvements_unites", "Mouvements des unités appariées", 4, "Tableau 11",
 "4 lignes, parfait pour un tableau de synthèse ; mais le seuil affiché (± 11,1 points = un critère sur neuf pour les CAC) est appliqué aussi aux CODESA, dont le pas est de 14,3 points (un critère sur sept).",
 "A", "Corps, chapitre 3 — conservé, seuil corrigé par organe",
 "Le tableau est le bon format ; l'erreur est dans la définition du seuil, pas dans la structure."),

("T22_unites_progression_regressi", "Unités en progression / régression (nominatif)", 249, "—",
 "249 unités (189 CAC, 60 CODESA) ; aucune unité stable alors que le tableau 11 en compte 148 : la liste ne contient que les unités ayant bougé, ce qui n'est pas dit ; les écarts sont des multiples exacts du pas (11,1 ou 14,3).",
 "C", "Corps, chapitre 3 — figure « unités en progression, stables, en régression » ; liste nominative en annexe D",
 "C'est le seul tableau nominatif du dispositif : il ne peut pas être publié en l'état (risque de réidentification) mais son agrégation manque au rapport."),

("T23_repondération_T1", "Repondération de T1 sur T0", 16, "Tableau 19",
 "16 lignes = 8 indicateurs × 2 bras ; les valeurs repondérées du rapport diffèrent du classeur (69,5 vs 70,0 ; évolution 4,2 vs 4,8).",
 "C", "Corps, chapitre 5 — dumbbell « évolution brute vs repondérée » par bras (8 indicateurs) + tableau 4 lignes",
 "Le message est un écart entre deux estimations, ce qui est exactement ce qu'une figure appariée montre le mieux."),

("T25_tableau_des_effets", "Tableau des effets (primaires et indices)", 9, "Tableau 20",
 "17 colonnes pour 9 lignes ; trois sources donnent trois estimations principales différentes pour P1 : 1,9 (T25, DiD 16 points), 2,9 (rapport), 3,1 (T25, modèle conjoint) ; la colonne « p ajustée » mêle Holm et BH.",
 "B", "Corps, chapitre 6 — 8 colonnes (T0/T1 par bras, DiD principale, IC, p ajustée, EMD, seuil, cas) ; colonnes de sensibilité en annexe",
 "Tableau le plus important du rapport, donc celui dont la lisibilité et la cohérence priment ; 17 colonnes détruisent le message."),

("T26_unites_appariees", "Unités appariées : DiD et ANCOVA", 2, "Tableau 25",
 "2 lignes, très lisible ; mais l'EMD de 23 points annoncée en note n'est pas calculée dans le classeur.",
 "A", "Corps, chapitre 6.1 — conservé",
 "Tableau court et honnête : il documente l'impossibilité de conclure sur les organes."),

("T27_divergence_tendances", "Divergence de tendance ± 2 / ± 5 points", 20, "Tableau 24",
 "20 lignes = 4 indicateurs × 5 divergences ; les valeurs du rapport (7,9 [-0,6 ; 15,3]) ne se déduisent pas du classeur (6,9 [-0,6 ; 13,3]) ; colonne « Cas » codée A-E sans grille sous les yeux du lecteur.",
 "C", "Corps, chapitre 6.1 — figure « effet corrigé selon la divergence supposée » (4 courbes, bande IC) + 4 lignes de tableau",
 "Le message est une sensibilité continue à une hypothèse, pas une grille de 20 cellules."),

("T28_placebos", "Placebos (indicateurs non ciblés)", 6, "Tableau 23",
 "6 lignes, bien construit ; une ligne diffère du classeur (âge : 31,6 vs 31,2 ; DiD -0,6 vs -0,3).",
 "A", "Corps, chapitre 6.1 — conservé",
 "Court, pertinent, directement lisible : modèle de tableau à conserver."),

("T29_effets_secondaires", "Effets secondaires (exploratoire, BH)", 70, "Tableau 26",
 "70 lignes ; aucun indicateur ne survit à la correction BH (p ajustée minimale 0,607) ; le tableau occupe plusieurs pages pour un résultat nul.",
 "E", "Annexe D + corps : figure forêt BH (10 indicateurs à p brut < 0,15) et 3 lignes de commentaire",
 "Résultat négatif et non confirmatoire : il doit être résumé, pas déroulé."),

("T30_differences_premieres_aires", "Différences premières au niveau de l'aire", 17, "Tableau 27",
 "17 lignes = 8 modèles ; le coefficient D1 de D3 vaut 0,2 [0,08 ; 0,31] dans le rapport et 0,11 [0,01 ; 0,21] dans le classeur (facteur 2) ; la variable « dD1 » n'est pas définie dans le tableau.",
 "D", "Corps, chapitre 7 — tableau de synthèse 5 lignes (un modèle, un coefficient clé, IC, p) + détail en annexe",
 "Le chapitre 7 est un chapitre de mécanismes : cinq coefficients suffisent, à condition qu'ils soient exacts."),

("T31_associations_transversales", "Associations transversales et valeurs E", 9, "Tableau 28",
 "9 lignes ; n différent (4 984 vs 4 954) ; le coefficient D3 ~ P3 vaut 0,1 dans le rapport et 0,05 dans le classeur ; la colonne « Valeur E, borne proche de 0 » du rapport n'existe pas dans le classeur.",
 "A", "Corps, chapitre 7 — conservé après correction, avec la valeur E et sa borne",
 "Tableau court et porteur d'un message prudent (association, pas causalité) : à conserver tel quel, une fois corrigé."),

("T32_variance_niveaux", "Décomposition de la variance par niveau", 8, "Tableau 29",
 "8 lignes ; pour D3, les variances du rapport (0,321 / 0,075 / 0,458) ne correspondent pas au classeur (0,109 / 0,029 / 0,169) ; la part d'aire du rapport (0,376) est présentée comme un résultat alors qu'elle dépend de composantes divergentes.",
 "C", "Corps, chapitre 7 — barres empilées de décomposition (aire / ZS / résiduel) par indicateur et passage",
 "Une décomposition de variance se lit en barres empilées ; en tableau, le lecteur ne voit ni l'ordre de grandeur ni la progression."),

("T33_effets_aires", "Effets aléatoires d'aire (données de la chenille)", 776, "Figure 12 (source)",
 "776 lignes (4 résultats × 2 passages × ~97 aires) : données de figure, pas tableau ; contient la variable « hors_ic » qui fonde les « signalements » des fiches.",
 "E", "Annexe D (extrait : 10 aires les plus atypiques) + source de la figure 12",
 "Le passage de 776 lignes à un extrait de 10 est le seul moyen de rendre les aires atypiques utilisables par le volet qualitatif."),

("T34_capacites_extrants_reco", "Capacités → extrants (RECO)", 3, "Tableau 30",
 "3 lignes, très clair ; rapport de taux 1,84 pour la prime, non commenté dans le rapport.",
 "A", "Corps, chapitre 7 — conservé",
 "Tableau court dont le résultat (prime associée à 84 % de visites en plus) mérite d'être commenté."),

("T35_heterogeneite", "Hétérogénéité pré-spécifiée", 20, "Tableau 31",
 "20 lignes ; les effectifs du rapport (1 900 / 3 091) diffèrent du classeur (2 285 / 3 428) et les DiD aussi (4,0 vs 3,2) ; les lignes « Province » n'ont ni n ni IC.",
 "C", "Corps, chapitre 8 — figure forêt par sous-groupe (déjà figure 13) + 8 lignes de tableau",
 "Le message est l'absence d'hétérogénéité détectable : une forêt le montre d'un regard, 20 lignes non."),

("T36_concentration_erreygers", "Indices de concentration d'Erreygers", 24, "Tableau 32",
 "24 lignes = 6 indicateurs × 2 bras × 2 passages ; les différences avec le classeur sont des arrondis (0,093 vs 0,091).",
 "C", "Corps, chapitre 8 — dumbbell T0 → T1 par indicateur et par bras (12 paires) + annexe",
 "La question est « l'inégalité a-t-elle diminué ? » : c'est une comparaison appariée, donc une figure à deux points reliés."),

("T37_gradient_quintiles", "Gradient par quintile (données de figure)", 160, "Figure 14 (source)",
 "160 lignes = 8 indicateurs × 4 groupes × 5 quintiles : données de figure.",
 "E", "Annexe D (source) + figure 14 dans le corps",
 "Aucune valeur ajoutée à publier la matrice complète."),

("T38_genre", "Genre dans la gouvernance et parmi les agents", 25, "Tableau 33",
 "25 lignes = 9 populations × bras × passage ; deux lignes à n = 2 (« RECO désignés depuis moins d'un an ») : pourcentages non interprétables.",
 "C", "Corps, chapitre 8 — barres groupées « part de femmes » par acteur et passage, ligne de repère 50 %",
 "La comparaison à la cible de 50 % est le message : elle doit être tracée sur la figure, pas laissée au lecteur."),

("T39_continuum_maternel", "Continuum maternel (cascade)", 32, "Tableau 56 (annexe D)",
 "32 lignes, deux populations (toutes les femmes / naissances < 6 mois) ; les n du rapport diffèrent du classeur (172 vs 252 pour la CPoN) ; le tableau est en annexe alors que la figure 15 du corps en dépend.",
 "A", "Corps, chapitre 9.1 — remonté en tableau 34 (2 populations × 4 étapes, 8 lignes) ; figure 15 reconstruite à partir de T40",
 "C'est la source du seul graphique vide du rapport : il faut remonter la source dans le corps et la rendre minimale."),

("T40_continuum_conditionnel", "Continuum maternel conditionnel", 4, "Tableau 34",
 "4 lignes ; la « co-couverture des 4 étapes » (16,7 % à 24,2 %) n'est pas le produit des probabilités conditionnelles affichées (0,415 × 0,943 × 0,35 ≈ 13,7 %) : la règle de calcul n'est pas documentée.",
 "A", "Corps, chapitre 9.1 — conservé avec une note de calcul explicite",
 "Seul tableau qui permet une vraie cascade (étapes conditionnelles) : sa définition doit être verrouillée."),

("T41_enfant_malade_distributions", "Enfant malade : distributions", 12, "Figure 16 (source)",
 "12 lignes × 17 colonnes : deux questions différentes (première réaction / lieu / délai) dans une même matrice, avec des colonnes vides pour chaque bloc.",
 "C", "Corps, chapitre 9.2 — figure 16 conservée ; trois petits tableaux de 4 lignes si chiffres nécessaires",
 "Tableau à trois volets au sens strict (trois questions, trois jeux de modalités) : la figure est la seule forme lisible."),

("T42_enfant_malade_multinomial", "Enfant malade : multinomial", 4, "Tableau 35",
 "4 lignes, très lisible ; écarts d'arrondi avec le classeur (58,9 vs 58,6).",
 "A", "Corps, chapitre 9.2 — conservé",
 "Bon format."),

("T43_enfant_malade_deux_parties", "Enfant malade : modèle en deux parties", 20, "Tableau 36",
 "20 lignes dont 18 coefficients : le lecteur ne peut pas distinguer les termes d'intérêt (bras, passage, interaction) des covariables d'ajustement.",
 "B", "Corps, chapitre 9.2 — 6 lignes (bras, passage, interaction, J2, quintile 5, marche) + renvoi en annexe",
 "Hiérarchiser les coefficients est la condition pour que le tableau soit lu."),

("T44_vaccination_declare_vu", "Vaccination : déclaré contre carnet vu", 20, "Tableau 37",
 "20 lignes ; l'écart est calculé entre deux indicateurs de dénominateur identique (tous ménages), ce qui est correct, mais la colonne « Carnet vu (%) » porte le même libellé que l'indicateur W2 (parmi les vaccinés) utilisé ailleurs : deux indicateurs, un seul nom.",
 "A", "Corps, chapitre 9.3 — conservé, libellés explicites (« carnet vu, tous ménages » / « carnet vu parmi les vaccinés ») + figure 17",
 "Tableau central du chapitre 9.3 ; le risque est le libellé, pas la structure."),

("T45_mpox_cap", "Mpox : CAP par bras et passage", 120, "Tableau 57 (annexe D)",
 "120 lignes ; 8 lignes « Synthèse » sans aucun libellé d'item, qui portent deux valeurs distinctes pour un même bras × passage (55,5 et 61,5 chez les témoins à T0) : les deux séries sont indiscernables ; les dénominateurs diffèrent entre blocs sans explication.",
 "E", "Annexe D + corps : figure 18 (12 items) et 8 lignes de synthèse nommées",
 "Seul tableau du rapport avec des lignes sans intitulé : défaut bloquant pour la publication, même en annexe."),

("T46_mpox_acceptabilite", "Mpox : acceptabilité (logistique)", 14, "Tableau 38",
 "14 lignes ; les p « < 0,001 » sont correctement rendus ; les rapports de cotes diffèrent légèrement du classeur (4,35 contre 4,38 ; 0,97 contre 0,98) comme les p intermédiaires (0,894 contre 0,945 ; 0,717 contre 0,723) — dérive de recalcul, sans effet sur la lecture.",
 "A", "Corps, chapitre 9.4 — conservé",
 "Tableau court et interprétable ; l'erreur de p est certaine et se corrige en une passe."),

("T47_reco_professionnalisation_c", "RECO : composantes de P4", 36, "Tableau 13",
 "36 lignes = 9 composantes × 2 bras × 2 passages ; P4 et P4 hors intrants figurent dans le même tableau que leurs composantes (redondance), et le total P4 n'est pas la moyenne simple des 6 items affichés.",
 "C", "Corps, chapitre 4 — dumbbell des 9 composantes (4 points par composante) + 6 lignes",
 "Le message est la stagnation de la prime et du contrat : quatre points reliés le montrent mieux que 36 cellules."),

("T48_asc_prime_montant", "ASC : montant de la prime", 4, "Tableau 16",
 "4 lignes, effectifs 28 / 16 / 23 / 19 : les médianes (10 vs 30 USD) sont robustes mais les IC ne sont pas calculés et la période de versement n'est pas connue.",
 "A", "Corps, chapitre 4 — conservé avec effectifs rappelés en tête et note sur la période",
 "Tableau honnête, à condition que le lecteur voie que n < 30."),

("T49_reco_charge_menages", "RECO : charge de ménages", 4, "Tableau 14",
 "4 lignes ; Gini intra-ZS (0,45 à 0,55) et part > 100 ménages (16,7 % à 24,4 %) sont deux mesures de la même dispersion, présentées sans hiérarchie.",
 "A", "Corps, chapitre 4 — conservé",
 "Bon format, message clair (la moitié des RECO dépassent la norme de 50 ménages)."),

("T50_logistique", "Logistique et intrants", 28, "Tableau 17",
 "28 lignes = 7 indicateurs × 2 bases × 2 bras × 2 passages ; les IC de ±25 à ±30 points (RECO) ne sont pas signalés.",
 "B", "Corps, chapitre 4 — 8 lignes (ruptures de stock, information, transport, équipement) + annexe",
 "Sélection nécessaire : la logistique est un chapitre secondaire du rapport."),

("T51_normes_psn", "Conformité aux normes du PSN SACO", 20, "Tableau 39",
 "20 normes, dont 2 seulement portent une cible chiffrée (« 50 % de femmes ») et une une norme structurelle (« ≤ 50 ménages ») ; les autres sont des niveaux descriptifs présentés comme des normes ; « ASC formé et certifié » n'est traçable dans aucun autre onglet.",
 "D", "Corps, chapitre 10 — tableau de synthèse 8 normes (cible documentée, valeur T0/T1, écart) + figure d'écart à la cible",
 "Confondre un niveau observé et une norme est une erreur d'interprétation : la synthèse doit séparer les deux."),

("T52_indice_conformite", "Indice de conformité des agents", 8, "Tableau 40",
 "8 lignes, lisible ; les 6 normes composant l'indice ne sont pas listées dans le tableau ni dans sa note.",
 "A", "Corps, chapitre 10 — conservé + liste des 6 normes en note",
 "Bon format ; il manque la composition de l'indice."),

("T53_sensibilite_D1", "Matrice de sensibilité D1", 7, "—",
 "7 variantes, absente du rapport alors que D1 est commenté dans le résumé exécutif.",
 "E", "Annexe D — ajoutée",
 "Un indicateur commenté sans matrice de sensibilité crée une asymétrie de traitement."),

("T53_sensibilite_D2", "Matrice de sensibilité D2", 7, "—",
 "7 variantes, absente du rapport.",
 "E", "Annexe D — ajoutée",
 "Même raison que D1."),

("T53_sensibilite_D3", "Matrice de sensibilité D3", 14, "—",
 "14 variantes, absente du rapport alors que D3 est un indice de résultat.",
 "E", "Annexe D — ajoutée",
 "Même raison ; D3 est l'indice le plus proche des résultats ménages."),

("T53_sensibilite_P1", "Matrice de sensibilité P1", 22, "Tableau 42",
 "22 variantes ; la ligne « Principale » du classeur porte 1,9 (16 points) alors que le rapport retient 2,9 (modèle conjoint) : la matrice est calculée sur l'ancienne estimation principale, ce qui invalide la comparaison « conclusion inchangée ».",
 "C", "Corps, chapitre 11 — courbe de spécification (figure 19) + 6 lignes ; matrice complète en annexe D",
 "La matrice est le bon outil, mais elle doit être recalculée sur l'estimation déclarée principale ; sinon elle documente une autre étude."),

("T53_sensibilite_P2", "Matrice de sensibilité P2", 21, "Tableau 43",
 "21 variantes, même décalage d'estimation principale (-1,9 vs -3,6).",
 "C", "Corps, chapitre 11 — courbe de spécification + annexe D",
 "Idem P1."),

("T53_sensibilite_P3", "Matrice de sensibilité P3", 23, "Tableau 44",
 "23 variantes : ici les valeurs coïncident, seuls les libellés de la ligne « Principale » sont inversés (16 points vs modèle conjoint).",
 "B", "Annexe D — matrice conservée ; corps : 6 lignes",
 "Cas intermédiaire : le recalcul est inutile, seule la ligne de référence est mal étiquetée."),

("T53_sensibilite_P4", "Matrice de sensibilité P4", 18, "Tableau 45",
 "18 variantes, même défaut d'étiquetage que P3.",
 "B", "Annexe D — matrice conservée ; corps : 6 lignes",
 "Idem P3."),

("T54_synthese_sensibilite", "Synthèse des sensibilités", 7, "Tableau 41",
 "7 lignes ; la part de variantes de même conclusion diffère fortement du rapport pour P2 (76 % au classeur, 44 % au rapport) et le nombre de variantes aussi (17 vs 16).",
 "A", "Corps, chapitre 11 — conservé, recalculé",
 "Tableau de synthèse réussi : c'est la valeur qui est fausse, pas la structure."),

("T55_manquants_primaires", "Manquants des indicateurs primaires", 20, "Tableau 52 (annexe C)",
 "20 lignes, mais « Manquants (%) = 0 » partout alors que le tableau 51 montre 29,8 % de manquants sur W2 : la différence (règle du minimum d'items) n'est pas expliquée ; valeurs différentes du rapport (12,3 vs 12,4 ; 11,7 vs 11,9 ; 13,6 vs 14,8).",
 "B", "Annexe C — conservé avec colonne « règle de calcul de l'indice »",
 "Un zéro de manquants non expliqué est plus dangereux qu'un taux élevé : il donne l'illusion d'une base complète."),
]
