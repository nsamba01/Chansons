---

# PARTIE G — Seconde passe de contrôles : ce que la reprise a établi

*Cette partie a été ajoutée lors de la reprise de l'audit. Elle ne répète rien des parties A à F : elle apporte des vérifications nouvelles, corrige deux affirmations de la première passe (le tableau 60 n'est pas entièrement invérifiable ; les p du tableau 38 sont bien rendus) et en retire une (la prétendue perte du signe d'inégalité).*

*La reprise a nécessité de reconstruire l'accès au classeur : le fichier livré ne s'ouvre pas directement avec une bibliothèque standard, faute d'une partie de dessin référencée mais absente. Le script `audit/build_dump.py` documente et contourne ce défaut, ce qui constitue en soi une pièce du dossier (voir REC-014).*

## G.1 Tableau 60 : le seul tableau sans source — et ce qui est vérifiable

Le tableau 60 (« Repondération de T1 : taille effective de Kish et étendue des poids par province et par bras ») n'a aucun onglet d'origine. L'audit de première passe en concluait qu'aucune de ses valeurs ne pouvait être retrouvée. **Cette conclusion doit être nuancée** : la colonne `n` se reproduit exactement.

| Province | Bras | n (tableau 60) | n recalculé depuis le tableau 3 (T1) | Taille effective (Kish) | Poids max / min |
|---|---|---:|---:|---:|---:|
| Maniema | Témoin | 356 | **356** | 332 | 2,05 |
| Maniema | Intervention | 357 | **357** | 248 | 10,90 |
| Kasaï-Oriental | Témoin | 360 | **360** | 325 | 4,43 |
| Kasaï-Oriental | Intervention | 359 | **359** | 316 | 11,18 |
| Sankuru | Témoin | 359 | **359** | 331 | 7,57 |
| Sankuru | Intervention | 356 | **356** | 297 | 4,00 |
| Sud-Kivu | Témoin | 358 | **358** | 319 | 3,06 |
| Sud-Kivu | Intervention | 351 | **351** | 341 | 1,87 |

Huit lignes sur huit : la colonne `n` correspond exactement à la somme des ménages à T1 du tableau 3, province par province et bras par bras. C'est un point de cohérence interne à porter au crédit du producteur, et cela suffit à écarter l'hypothèse d'un tableau fabriqué.

En revanche, les deux colonnes de droite — taille effective de Kish et rapport poids maximal / poids minimal — ne sont **pas** recalculables : le classeur ne contient aucune table de poids, et aucun onglet ne porte de taille effective. Ces deux colonnes sont donc vérifiables seulement par le script qui les a produites, lequel n'est pas livré (REC-014).

**Un point d'analyse que ces chiffres soulèvent.** Le rapport indique, au § 1.4 et dans les notes du tableau 20, une « pondération égale des provinces ». Or, dans une même cellule province × bras, les poids varient d'un facteur **11,18** (Kasaï-Oriental, intervention) et **10,90** (Maniema, intervention). Sur deux zones de santé de 180 et 180 ménages, une pondération provinciale égale ne peut pas produire un tel écart : il faut qu'une repondération de second niveau — non-réponse, taille de ménage ou calibration sur des marges — intervienne à l'intérieur de la cellule. Cette repondération n'est décrite nulle part, alors qu'elle est la seule explication possible d'un rapport de 11 entre le poids le plus fort et le plus faible. Il en résulte des effets de plan de 1,03 à 1,44 (n / taille effective), cohérents avec un tel mécanisme, mais non documentés.

> **REC-020 — Décrire la repondération de second niveau et publier les poids** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-020 |
| 2. Constat | Les poids varient d'un facteur 11 dans une même cellule province × bras alors que le rapport annonce une pondération égale des provinces ; ni les poids ni la taille effective ne figurent dans le classeur. |
| 3. Preuve | Tableau 60, colonnes « Taille effective (Kish) » et « Poids max / min » (11,18 ; 10,90) ; § 1.4 ; absence de table de poids dans les 78 onglets. |
| 4. Axe | 4 — effectifs ; axe 8 |
| 5. Criticité | Majeur |
| 6. Cause probable | Une étape de calibration intra-provinciale ajoutée dans la chaîne de calcul sans être décrite dans la méthode. |
| 7. Effet | Le lecteur ne peut pas interpréter l'affirmation « pondération égale des provinces » ni juger de l'effet réel des poids sur les intervalles. |
| 8. Recommandation | Décrire l'étape (variable de calibration, source des marges, traitement de la non-réponse) ; livrer la table des poids en annexe ; ajouter une colonne « effet de plan » au tableau 60. Ne modifier aucune valeur. |
| 9. Modalité | Producteur + auteur ; une note de méthode de 10 lignes et un onglet supplémentaire. |
| 10. Livrable | § 1.5 v2 + onglet `P01_poids` + tableau 60 v2 (4 colonnes). |
| 11. Effort | 1,5 jour-personne. |
| 12. Dépendance | REC-014 (le script de pondération doit être fourni). |
| 13. Clôture | La repondération intra-cellulaire est décrite et la table de poids est livrée ; les 8 lignes du tableau 60 restent inchangées. |
| 14. Statut | Ouvert. |

## G.2 Tableau 57 (Mpox) : huit lignes sans intitulé, deux séries confondues

L'onglet `T45_mpox_cap` compte 120 lignes de données. Les huit dernières portent le bloc « Synthèse » **sans aucun libellé d'item** dans la colonne prévue, et se présentent par paires :

| Bloc | Item | Bras | Passage | % [IC 95 %] | n |
|---|---|---|---|---:|---:|
| Synthèse | *(vide)* | Témoin | T0 | 55,5 [46,7 ; 64,3] | 1 428 |
| Synthèse | *(vide)* | Témoin | T0 | 61,5 [52,5 ; 70,5] | 1 428 |
| Synthèse | *(vide)* | Témoin | T1 | 62,6 [53,8 ; 71,3] | 1 433 |
| Synthèse | *(vide)* | Témoin | T1 | 73,1 [65,4 ; 80,9] | 1 433 |
| Synthèse | *(vide)* | Intervention | T0 | 66,7 [59,2 ; 74,1] | 1 429 |
| Synthèse | *(vide)* | Intervention | T0 | 74,6 [67,1 ; 82,0] | 1 429 |
| Synthèse | *(vide)* | Intervention | T1 | 72,3 [63,5 ; 81,1] | 1 423 |
| Synthèse | *(vide)* | Intervention | T1 | 76,1 [67,8 ; 84,3] | 1 423 |

Deux séries de synthèse coexistent donc — vraisemblablement un indice de connaissances et un indice de prévention — et **rien ne permet de les distinguer**. Un lecteur qui lit les huit lignes voit deux pourcentages pour un même groupe et conclut à une erreur. La différence est pourtant substantielle : 55,5 contre 61,5 chez les témoins à T0, soit 6 points d'écart selon la série retenue.

C'est le seul endroit du rapport où des valeurs publiées n'ont aucun intitulé. En l'état, ces huit lignes sont inutilisables et doivent être nommées ou supprimées.

## G.3 Cascade maternelle : la co-couverture ne se déduit pas des probabilités conditionnelles affichées

L'onglet `T40_continuum_conditionnel` affiche, pour chaque bras et passage, trois probabilités conditionnelles et une « co-couverture des 4 étapes ». Ces quatre nombres devraient être liés par une identité : la co-couverture est le produit des trois conditionnelles (appliquées aux femmes ayant commencé la cascade). L'identité ne tient pas.

| Bras | Passage | CPN4+ sachant CPN1 | Structure sachant CPN4+ | CPoN sachant structure | Produit | Co-couverture publiée | Écart |
|---|---|---:|---:|---:|---:|---:|---:|
| Témoin | T0 | 41,5 | 94,3 | 35,0 | **13,70** | **16,7** | +3,0 |
| Témoin | T1 | 45,5 | 95,1 | 49,5 | **21,42** | **24,2** | +2,8 |
| Intervention | T0 | 47,8 | 96,0 | 36,6 | **16,80** | **19,9** | +3,1 |
| Intervention | T1 | 41,1 | 93,4 | 42,7 | **16,40** | **18,2** | +1,8 |

L'écart est systématique, toujours dans le même sens, et de 1,8 à 3,1 points. Trois explications sont possibles : les conditionnelles sont calculées sur des dénominateurs non emboîtés (par exemple la CPoN sur toutes les femmes accouchées et non sur celles ayant accouché en structure), la co-couverture est mesurée directement sur les quatre événements sans passer par les conditionnelles, ou l'une des deux séries est erronée. Le rapport ne tranche pas, et le tableau 34 ne porte aucune note de calcul.

**Un contrôle réussi, à porter au crédit du producteur.** La première conditionnelle se réconcilie exactement avec les taux marginaux : 37,3 % de femmes ayant eu au moins quatre CPN divisé par 89,9 % ayant eu au moins une CPN donne 41,5 %, soit la valeur affichée. Le chaînage des conditionnelles est donc correct à la première étape ; c'est la co-couverture qui est calculée autrement.

Ce point commande la reconstruction de la figure 15 (REC-012) : sans règle de calcul explicite, la cascade reconstruite ne correspondra pas aux chiffres publiés.

> **REC-021 — Documenter la règle de calcul de la co-couverture** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-021 |
| 2. Constat | La co-couverture des 4 étapes dépasse de 1,8 à 3,1 points le produit des trois probabilités conditionnelles affichées dans la même ligne. |
| 3. Preuve | `T40_continuum_conditionnel` (4 lignes) ; `T39_continuum_maternel` (contrôle de la première conditionnelle : 37,3 / 89,9 = 41,5). |
| 4. Axe | 2 — définition ; axe 3 |
| 5. Criticité | Majeur |
| 6. Cause probable | Dénominateurs non emboîtés ou mesure directe de la co-couverture. |
| 7. Effet | La cascade ne peut pas être reconstruite ; la figure 15 restera invérifiable. |
| 8. Recommandation | Ajouter au tableau 34 une note de trois lignes donnant la règle exacte (dénominateur de chaque étape, mode de calcul de la co-couverture) ; si la co-couverture est mesurée directement, le dire et cesser de la présenter comme un produit. |
| 9. Modalité | Auteur + producteur ; note de tableau. |
| 10. Livrable | Tableau 34 v2 + figure 15 reconstruite de façon cohérente. |
| 11. Effort | 0,5 jour-personne. |
| 12. Dépendance | REC-012. |
| 13. Clôture | La co-couverture est soit recalculée comme produit, soit expliquée ; l'écart est nul ou documenté. |
| 14. Statut | Ouvert. |

## G.4 La grille des cas : une lettre qui change selon le document

Le rapport affiche, pour chaque indicateur, une lettre de « cas » (A à E). La vérification systématique des neuf lignes du tableau 20 contre les deux onglets qui portent la même colonne (`T25_tableau_des_effets` et `T27_divergence_tendances`, cette dernière à divergence nulle) donne un désaccord sur un indicateur — et ce désaccord n'est pas un détail de présentation.

| Indicateur | Cas — tableau 20 (rapport) | Cas — T25 (classeur) | Cas — T27, divergence 0 | EMD (rapport / classeur) | Seuil |
|---|---|---|---:|---|---:|
| P1 Exposition | D | D | D | 10,1 / 10,1 | 5 |
| **P2 Connaissances** | **E** | **D** | **D** | 10,1 / 10,0 | 5 |
| P3 Fonctionnalité CAC | E | E | E | 8,8 / 8,8 | 11 |
| P4 Professionnalisation RECO | E | E | E | 13,3 / 13,3 | 8 |
| P4 hors intrants | E | E | — | **15,1 / 13,3** | 8 |
| D1 Gouvernance | D | D | — | 0,8 / 0,8 | 0,25 |
| D2 Capacités | D | D | — | **0,9 / 0,5** | 0,25 |
| D3 Résultats ménages | D | D | — | **0,4 / 0,3** | 0,25 |
| D4 Riposte Mpox | E | E | — | **0,8 / 0,6** | 0,25 |

Deux constats.

**La lettre de P2 n'est pas la même dans le rapport et dans le classeur.** Le rapport dit E, les deux onglets du classeur disent D. Or D et E ne veulent pas dire la même chose : D est l'indétermination, E est un gain au moins égal au seuil non soutenu par l'intervalle. Pour un effet estimé à −3,6 points avec un intervalle [−10,8 ; 3,7] et un seuil de 5 points, l'intervalle exclut tout gain atteignant le seuil : la lettre E du rapport est cohérente avec la définition, la lettre D du classeur ne l'est pas. Inversement, pour D3 (effet 0,1, intervalle [−0,1 ; 0,2], seuil 0,25), l'intervalle exclut également un gain atteignant le seuil, et le classeur code pourtant D. **Aucune règle unique ne reproduit les neuf lettres.** La grille est donc appliquée au jugement, indicateur par indicateur, sans table de décision — ce qui la rend non reproductible et, pour un lecteur, invérifiable.

**Quatre EMD sur neuf diffèrent entre le rapport et le classeur** : 15,1 contre 13,3 (hors intrants), 0,9 contre 0,5 (capacités), 0,4 contre 0,3 (résultats), 0,8 contre 0,6 (riposte). Ce sont des écarts de 20 à 80 % sur une quantité qui sert précisément à décider du cas. Un EMD recalculé change la conclusion de pertinence d'un indicateur ; quatre EMD recalculés sans mention changent la lecture de la moitié des indices composites.

Ces deux constats renforcent REC-009 (sourcer les seuils et rendre la grille autoportante) et y ajoutent une exigence : publier la **table de décision** de la grille, et non seulement la définition des cas.

> **REC-022 — Publier la table de décision de la grille des cas et aligner les EMD** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-022 |
| 2. Constat | La lettre de cas de P2 diffère entre le rapport (E) et le classeur (D) ; aucune règle unique ne reproduit les 9 lettres ; quatre EMD sur neuf diffèrent de 20 à 80 % entre le rapport et le classeur. |
| 3. Preuve | Tableau 20 colonnes L, M, N ; `T25_tableau_des_effets` colonnes L, M, N ; `T27_divergence_tendances`, lignes à divergence 0. |
| 4. Axe | 5 — inférence ; axe 3 |
| 5. Criticité | Bloquant |
| 6. Cause probable | Grille appliquée manuellement, indicateur par indicateur, sur deux jeux d'EMD issus de deux passages. |
| 7. Effet | Les lettres Codent des conclusions que le lecteur ne peut ni vérifier ni reproduire ; une même configuration reçoit deux lettres. |
| 8. Recommandation | Écrire la table de décision sous forme de conditions explicites (position de l'IC par rapport à 0 et au seuil), l'appliquer par script, aligner les EMD sur l'estimation principale, publier le tableau 20 avec un renvoi à la table. Pour P2, trancher et conserver la lettre correcte au vu de la règle. |
| 9. Modalité | Producteur ; script d'attribution des cas ; contrôle sur les 9 lignes. |
| 10. Livrable | Table de décision (5 lignes de conditions) + tableau 20 v2. |
| 11. Effort | 1 jour-personne. |
| 12. Dépendance | REC-004, REC-009. |
| 13. Clôture | Les 9 lettres sont reproduites par le script ; 0 divergence entre le rapport et le classeur ; EMD identiques. |
| 14. Statut | Ouvert. |

## G.5 Contrôles qui confirment ce que le rapport affirme

Quatre vérifications supplémentaires n'ont rien trouvé à redire, et il est utile de le dire.

**Les indicateurs secondaires ne résistent pas à la correction multiple, et c'est exact.** L'onglet `T29_effets_secondaires` contient 70 indicateurs ; aucune p ajustée par Benjamini-Hochberg n'est inférieure à 0,607, et la plus petite p brute (0,031, « CAC : a participé à une riposte ») devient 0,607 après correction. Le rapport ne revendique aucun résultat secondaire, ce qui est la bonne lecture. La figure 11 devrait toutefois indiquer combien des 70 indicateurs elle représente, faute de quoi le lecteur croit voir l'ensemble.

**Les totaux du tableau 3 se réconcilient au ménage près.** La somme des ménages par zone donne 2 857 à T0 et 2 856 à T1, soit exactement les 5 713 observations annoncées dans le résumé exécutif. Le décalage d'une unité entre les deux passages est cohérent avec l'appariement (688 villages à T0, 626 à T1). La ligne fantôme « Kasaï-Oriental » (province sans zone de santé, sans ménage, mais avec un unique CAC à T1) est confirmée : elle doit être supprimée du tableau 3 et du rapport.

**Vingt normes du PSN, dont deux seulement portent une cible chiffrée.** Le tableau 39 liste 20 normes ; seules « Femmes parmi les RECO (cible 50 %) » et « Femmes parmi les ASC (cible 50 %) » énoncent une cible numérique. Les dix-huit autres sont des niveaux descriptifs présentés comme des normes. Cette observation de la première passe est confirmée par lecture exhaustive de l'onglet : il n'existe aucune autre cible chiffrée. Elle renforce la recommandation de séparer, dans le tableau, ce qui est normé de ce qui est observé.

**Les p « < 0,001 » sont correctement rendus.** L'audit de première passe soupçonnait une perte du signe d'inégalité dans le tableau 38 (acceptabilité du vaccin Mpox), sur la base d'une lecture du classeur. La vérification dans le document Word montre que le tableau affiche bien « < 0,001 ». **Ce point est retiré du passif.** Les seules divergences du tableau 38 sont des dérives de recalcul (rapports de cotes 4,35 contre 4,38 et 4,99 contre 4,95 ; p intermédiaires 0,894 contre 0,945), sans effet sur la lecture.

## G.6 Ce que la reprise change dans le décompte des écarts

La première passe comptait trente écarts chiffrés. La reprise en ajoute quatre (les EMD du tableau 20) et en retire un (les p du tableau 38). Le décompte s'établit donc à **trente-trois écarts**, dont :

| Catégorie | Nombre | Exemples |
|---|---:|---|
| Deux passages d'estimation | 12 | P1 2,9 contre 3,1 ; P2 −3,6 contre −3,1 ; variance D3 (facteur 3) |
| Recalcul d'intervalles ou de p | 6 | IC des tableaux « trois volets » ; p du placebo « âge » |
| Recalcul de colonnes dérivées | 3 | évolution ajustée (10/16 et 9/16 zones) ; repondération |
| Divergences de définition | 2 | poids des indices ; composantes de D3 |
| Étiquetage | 2 | ligne « principale » des matrices ; cas de P2 |
| EMD recalculées | 4 | hors intrants, capacités, résultats, riposte |
| Sans source dans le classeur | 2 | tableaux 58 et 60 (Kish) |
| Dérives d'arrondi | 2 | 30,13 contre 30,11 ; 0,093 contre 0,091 |

Les dérives d'arrondi sont mentionnées pour mémoire et ne sont pas imputées. Les trente et un autres cas engagent la reproductibilité.

## G.7 Effet de la reprise sur le verdict

Le verdict ne change pas : **le rapport n'est pas diffusable en l'état.** Trois éléments le renforcent plutôt qu'ils ne l'allègent.

1. La grille des cas, présentée comme l'appareil de décision le plus abouti du document, ne se reproduit pas à partir de ses propres données (G.4), et son EMD — la quantité qui fonde chaque lettre — diffère entre le rapport et le classeur dans quatre cas sur neuf.
2. Le tableau 57 contient huit lignes publiées sans intitulé, qui portent deux séries distinctes (G.2) : c'est le seul endroit où une valeur n'est pas identifiable, et il se corrige en nommant les lignes.
3. La cascade maternelle, dont la figure 15 est vide, repose sur deux calculs qui ne s'accordent pas (G.3) : la reconstruction de la figure ne peut pas précéder la clarification du calcul.

Un élément l'allège en revanche, et il faut le dire : la colonne d'effectifs du tableau 60 se reproduit exactement, ce qui écarte l'hypothèse d'un tableau fabriqué et ramène le problème à une pièce non livrée (la table des poids). De même, le chaînage des conditionnelles de la cascade est exact à sa première étape, et les p du tableau 38 sont correctement rendus. L'audit retire donc un grief et en ajoute deux, dans la même mouvement : c'est ce que doit faire une seconde passe.

Le nombre de recommandations passe de dix-neuf à vingt-deux (une bloquante et deux majeures supplémentaires) ; la charge chiffrée hors rédaction, de vingt-cinq à vingt-neuf jours-personne. Le récapitulatif de l'annexe 3 et le plan de correction de la partie F.2 intègrent déjà ces ajouts.
