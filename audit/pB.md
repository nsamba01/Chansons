---

# PARTIE B — Réconciliation numérique entre la maquette et le classeur

*Axe 3 — réconciliation. Cette partie est le cœur de l'audit : elle établit, valeur par valeur, si le rapport dit ce que disent ses données.*

## B.1 Ce qui a été comparé

Soixante et un appariements ont été testés entre un tableau du rapport et un onglet du classeur. Chaque appariement a été construit sur la sémantique (même indicateur, même population, même registre), puis vérifié sur la structure (même nombre de lignes de données, mêmes libellés de lignes, même ordre de colonnes). Les valeurs ont été comparées après normalisation des décimales et du signe moins, avec une tolérance de 0,05 dans l'unité de la colonne.

Le résultat tient en une phrase : **les tableaux descriptifs se reproduisent, les tableaux d'estimation ne se reproduisent pas.**

Les 33 tableaux descriptifs (profils, distributions, effectifs, trois volets, catégories, transitions, UCODESA, qualité des données) se reproduisent à l'arrondi près, sauf quatre exceptions documentées ci-dessous. Les tableaux d'estimation — effets, variance, associations, hétérogénéité, sensibilité — présentent des écarts qui ne sont pas des arrondis.

La raison de cette asymétrie est simple et c'est le principal constat de cette partie : **le rapport a été rédigé sur un second passage d'estimation, postérieur à l'export du classeur du 15 octobre**, et rien ne signale ce changement de version. Le motif des écarts le confirme : ils affectent les indicateurs ménages (P1, P2, indice de résultats D3) et épargnent les indicateurs d'offre (P3, P4), ce qui est compatible avec une modification du traitement des pondérations ou du dénominateur des items de connaissances — hypothèse qui ne peut pas être vérifiée sans les scripts, et qui est donc présentée comme telle.

## B.2 Le cas central : les quatre indicateurs primaires

C'est le tableau que tout le rapport attend. Le tableau 20 s'intitule « Tableau des effets : indicateurs primaires et indices de domaine (registre attributionnel) ». Il comporte 17 colonnes pour 9 lignes, dont deux colonnes d'effet : « DiD modèle conjoint [IC CR2] » et « DiD 16 points brute [IC t11] ».

| Primaire | Rapport — modèle conjoint | Classeur T25 — modèle à effets fixes | Rapport — DiD 16 points | Classeur T25 — DiD 16 points |
|---|---|---|---|---|
| P1 Exposition | **2,9** [−4,4 ; 10,3] — p 0,399 | **3,1** [−4,2 ; 10,5] — p 0,371 | **3,0** [−4,2 ; 10,3] | **1,9** [−4,4 ; 8,3] |
| P2 Connaissances | **−3,6** [−10,8 ; 3,7] — p 0,305 | **−3,1** [−10,3 ; 4,1] — p 0,364 | **−2,1** [−9,3 ; 5,1] | **−1,9** [−8,8 ; 5,1] |
| P3 Fonctionnalité CAC | 0,1 [−6,2 ; 6,4] — p 0,966 | 0,1 [−6,2 ; 6,4] — p 0,966 | 0,3 [−6,0 ; 6,6] | 0,3 [−6,0 ; 6,6] |
| P4 Professionnalisation RECO | −3,2 [−12,9 ; 6,6] — p 0,488 | −3,2 [−12,9 ; 6,6] — p 0,488 | −2,4 [−11,9 ; 7,1] | −2,4 [−11,9 ; 7,1] |

Trois observations.

**Aucune colonne du classeur ne reproduit les quatre valeurs du rapport.** Ni la colonne « DiD 16 points », ni la colonne « Modèle EF » de `T25_tableau_des_effets` ne donne 2,9 ; −3,6 ; 0,1 ; −3,2. Les deux dernières valeurs viennent de la colonne « Modèle EF » ; les deux premières ne viennent d'aucune colonne.

**Les écarts ne sont pas des arrondis.** P1 : 2,9 contre 3,1 (0,2) mais aussi 3,0 contre 1,9 (1,1) pour la DiD à 16 points. P2 : −3,6 contre −3,1 (0,5) et −2,1 contre −1,9 (0,2). Un arrondi ne produit pas un écart de 1,1 point sur un coefficient dont l'intervalle est de largeur 14,7.

**La largeur des intervalles est stable, leur centre se déplace.** Pour P1, l'intervalle du modèle à effets fixes fait 14,7 points d'amplitude dans les deux fichiers ([−4,2 ; 10,5] et [−4,4 ; 10,3]) mais n'est pas centré sur le même point. Cela indique un changement d'estimation ponctuelle, non un changement de variance : le second passage a probablement modifié une covariable ou une pondération, pas le calcul de l'erreur-type.

Les figures amplifient le problème au lieu de le résoudre. La figure 1 affiche, dans chaque panneau, « DiD modèle conjoint (IC 95 % CR2) » avec les valeurs du tableau 20, alors que sa légende annonce une **forêt des effets « DiD à 16 points »**. Le graphique montre une chose et la légende en annonce une autre. La figure 7 reprend les mêmes valeurs (P1 : T1 témoin 69,2 et T1 intervention 69,2 ; P2 : T0 30,3 et 33,8) là où le tableau 20 donne 69,3 pour P1 et 33,8 pour P2 mais où le classeur donne 33,4 pour P2 à T0 : la figure 1, la figure 7 et le tableau 20 ne s'accordent pas entre eux, et aucun des trois ne s'accorde intégralement avec le classeur.

## B.3 Les écarts vérifiés, cas par cas

Le tableau suivant ne contient que des écarts relus dans les deux fichiers. Chaque ligne est reproductible à partir des références indiquées. Les lignes 30 à 34 ont été ajoutées lors de la seconde passe (partie G) ; la ligne 29 a été corrigée : les p « < 0,001 » sont bien rendus dans le rapport, seul le tableau 58 reste sans source certaine.

| # | Objet | Valeur du rapport | Valeur du classeur | Écart | Nature |
|---|---|---|---|---|---|
| 1 | P1, modèle conjoint | 2,9 [−4,4 ; 10,3] | 3,1 [−4,2 ; 10,5] (T25, « Modèle EF ») | 0,2 pt | Deux passages |
| 2 | P1, DiD 16 points | 3,0 [−4,2 ; 10,3] | 1,9 [−4,4 ; 8,3] (T25) | 1,1 pt | Deux passages |
| 3 | P2, modèle conjoint | −3,6 [−10,8 ; 3,7] | −3,1 [−10,3 ; 4,1] (T25) | 0,5 pt | Deux passages |
| 4 | P2, DiD 16 points | −2,1 [−9,3 ; 5,1] | −1,9 [−8,8 ; 5,1] (T25) | 0,2 pt | Deux passages |
| 5 | P2, T0 bras intervention | 33,8 | 33,4 (T25) | 0,4 pt | Deux passages |
| 6 | P1, T1 bras témoin | 69,2 (figures 1 et 7) | 69,3 (T25) | 0,1 pt | Dérive d'arrondi |
| 7 | Tableau 21, évolution ajustée (P1) | 4,8 (Kibombo) ; −8,3 (Kalima) | 4,7 ; −8,4 (T19_P1 col. I) | 0,1 | Recalcul de l'ajustement — **10 zones sur 16** |
| 8 | Tableau 21, écart à la moyenne provinciale | 4,9 (Kibombo) | 4,7 (col. J) | 0,2 | Recalcul — **11 zones sur 16** |
| 9 | Tableau 54, évolution ajustée (P2) | −6,4 (Kibombo) ; −5,6 (Kalima) | −4,5 ; −7,0 (T19_P2 col. I) | 1,9 ; 1,4 | Recalcul — **9 zones sur 16** |
| 10 | Tableau 54, écart à la moyenne (P2) | −6,5 (Kibombo) | −4,5 (col. J) | 2,0 | Recalcul — **8 zones sur 16** |
| 11 | Tableaux 22 et 55 (P3, P4) | identiques | identiques | 0 | **Reproductibles 16/16** |
| 12 | Tableau 41, part de variantes concordantes | 44 % pour P2 ; 16 variantes | 76 % ; 17 variantes (T54) | 32 pts | Recalcul de la sensibilité |
| 13 | Tableau 41, gouvernance | 100 % | 86 % (T54) | 14 pts | Recalcul |
| 14 | Tableau 41, connaissances, estimation extrême | −5,8 | −4,9 (T54) | 0,9 pt | Recalcul |
| 15 | Tableaux 42–45, ligne « principale » | « modèle conjoint à effets fixes d'aire (CR2) » | « Estimation principale (16 points) » | — | **Étiquetage inversé** |
| 16 | Tableau 42 (P1), ligne principale | 2,9 | 1,9 [−4,4 ; 8,3] | 1,0 pt | Matrice calculée sur l'ancienne estimation |
| 17 | Tableau 43 (P2), ligne principale | −3,6 | −1,9 | 1,7 pt | Idem |
| 18 | Tableau 47, poids des indices | 0,218 et 0,191 | 0,177 et 0,139 (T07) | 0,041 ; 0,052 | Divergence de définition |
| 19 | Tableau 29, variance P1 (aire / ZS / résiduel) | 289,176 / 26,567 / 689,029 | 289,38 / 26,317 / 685,475 (T32) | 0,2 / 0,25 / 3,55 | Deux passages |
| 20 | Tableau 29, variance D3 | 0,321 / 0,075 / 0,458 | 0,109 / 0,029 / 0,169 (T32) | facteur ≈ 3 | Divergence majeure de décomposition |
| 21 | Tableau 28, association P1 ~ P3 | 2,89 [0,97 ; 4,81] p 0,007 | 2,89 [0,98 ; 4,80] p 0,006 (T31) | 0,01 | Recalcul d'IC |
| 22 | Tableau 28, colonne « valeur E » | présente | **absente du classeur** (T31) | — | Sortie non traçable |
| 23 | Tableau 31, hétérogénéité | 0,31 ; 0,13 p 0,078 | 0,30 ; 0,12 p 0,091 (T35) | 0,01 | Recalcul |
| 24 | Tableau 31, effectifs | 1 900 / 3 091 (somme 4 991) | 2 285 / 3 428 (T35, somme 5 713) | 385 / 337 | **Bases différentes — grief retiré (H.5)** |
| 25 | Tableau 24, divergence ± 5 | 7,9 [0,6 ; 15,3] | 6,9 [0,6 ; 13,3] (T27) | 1,0 | Recalcul |
| 26 | Tableau 19, repondération P1 | 69,5 ; évolution 4,2 | 70,0 ; 4,8 (T23) | 0,5 ; 0,6 | Recalcul |
| 27 | Tableau 23, placebo « âge » | 31,6 ; −0,6 [−3,1 ; 2,0] p 0,622 | 31,2 ; −0,3 [−2,7 ; 2,2] p 0,799 (T28) | 0,4 ; 0,3 | Deux passages |
| 28 | Tableaux 7, 8, 12, 15 (trois volets) | IC systématiquement plus étroits | IC du classeur | ex. supervision ASC : [−6,4 ; 22,0] contre [−7,6 ; 23,2] | **Recalcul d'IC, quasi toutes les lignes** |
| 29 | Tableaux 58 et 60 | présents | **aucun onglet** | — | Sans source |
| 30 | Tableau 20, EMD — hors intrants | 15,1 | 13,3 (T25) | 1,8 | **EMD recalculée** |
| 31 | Tableau 20, EMD — capacités des acteurs | 0,9 | 0,5 (T25) | 0,4 (80 %) | **EMD recalculée** |
| 32 | Tableau 20, EMD — résultats ménages | 0,4 | 0,3 (T25) | 0,1 (33 %) | **EMD recalculée** |
| 33 | Tableau 20, EMD — riposte Mpox | 0,8 | 0,6 (T25) | 0,2 (33 %) | **EMD recalculée** |
| 34 | Tableau 20, lettre de cas — P2 | E | D (T25 et T27 à divergence 0) | — | **Divergence de grille** |
| 35 | Dérives d'arrondi | 30,13 / 0,093 / 26,6 / 58,9 / 12,3 / 26,6 | 30,11 / 0,091 / 26,5 / 58,6 / 12,4 / 26,8 | ≤ 0,3 | Sans conséquence |

Le cas 20 mérite d'être isolé parce qu'il porte sur un indice de résultat, donc sur la conclusion. Dans le tableau 29, la décomposition de la variance de l'indice de résultats ménages (D3) donne une variance d'aire de 0,321, une variance de zone de 0,075 et une variance résiduelle de 0,458. Le classeur donne 0,109 ; 0,029 ; 0,169, soit des valeurs trois à quatre fois plus faibles. Les rapports internes sont différents : la part d'aire est de 38 % dans le rapport et de 36 % dans le classeur, mais les niveaux absolus ne sont pas comparables. Or c'est le niveau absolu qui détermine la part de variance attribuable au niveau d'analyse et, par conséquent, l'interprétation des effets d'aire de la figure 12. Un facteur trois sur une variance n'est pas un arrondi : il faut trancher.

## B.4 Les quatre modes de défaillance

Les trente écarts ci-dessus ne sont pas trente accidents. Ils se ramènent à quatre mécanismes, ce qui est une bonne nouvelle pour la correction : quatre corrections de chaîne suffisent.

**Mode 1 — Deux passages d'estimation, sans numéro de version.** Le classeur du 15 octobre et le rapport du 19 octobre ne sortent pas du même calcul. Le motif (P1, P2 et D3 affectés ; P3 et P4 épargnés) suggère un changement dans les pondérations ou les covariables individuelles des ménages. Correction : un identifiant de version dans chaque sortie et dans chaque tableau, et une seule version de référence par diffusion.

**Mode 2 — Recalcul des intervalles de confiance dans les tableaux « trois volets ».** Les tableaux 7, 8, 12 et 15 présentent des intervalles plus étroits que le classeur dans la quasi-totalité de leurs lignes, avec un centre décalé de 1 à 1,5 point : pour la supervision des ASC (tableau 15), l'écart est de [−6,4 ; 22,0] dans le rapport contre [−7,6 ; 23,2] dans le classeur, soit un intervalle de 28,4 points au lieu de 30,8. L'étroitesse systématique de l'intervalle, sans réduction de l'effectif, indique un changement de méthode d'inférence (degrés de liberté ou type de bootstrap) non documenté. Correction : indiquer en note de chaque tableau le nombre de degrés de liberté et la méthode de bootstrap, et recalculer depuis une source unique.

**Mode 3 — Colonnes « évolution ajustée » recalculées, non reproduites.** Les tableaux 21 et 54 donnent une évolution ajustée qui ne se reproduit pas (10/16 et 9/16 zones), alors que les tableaux 22 et 55 se reproduisent parfaitement. L'ajustement est donc, pour les indicateurs ménages, recalculé avec un modèle différent de celui du classeur. Correction : publier la formule d'ajustement en note et joindre le script.

**Mode 4 — Étiquetage inversé des lignes de référence.** Dans les matrices de sensibilité (tableaux 42 à 45), la ligne de référence est étiquetée « modèle conjoint à effets fixes d'aire (CR2) » alors que le classeur l'étiquette « Estimation principale (16 points) » et qu'elle porte les valeurs de la DiD à 16 points. Le lecteur croit donc lire la sensibilité de l'estimation principale alors qu'il lit celle de l'estimation complémentaire.

## B.5 Le cas des fiches de zone et de l'annexe A

Les fiches de zone sont, paradoxalement, la partie la mieux contrôlée du document : sur 64 cellules (16 zones × 4 primaires), **deux seulement divergent** du classeur, et ce sont exactement les deux valeurs que l'annexe A aurait dû expliquer.

| Zone | Primaire | T0 fiche | T0 classeur | Évolution fiche | Évolution classeur |
|---|---|---|---|---|---|
| Kibombo | P2 Connaissances | 23,7 | 20,4 | 7,0 | 10,3 |
| Tunda | P2 Connaissances | 15,0 | 14,4 | 26,0 | 26,6 |

Tout le reste des fiches est exact : T1, évolutions, indicateurs secondaires, effectifs. C'est un point à porter au crédit du producteur, et cela renforce la recommandation : puisque deux cellules font exception, la note qui les explique est courte et doit être écrite immédiatement.

En revanche, les tableaux de zone de l'annexe D (tableaux 54 et 55) présentent l'écart décrit au cas 9 : la colonne « évolution ajustée » du tableau 54 s'écarte du classeur dans 9 zones sur 16, dont Kibombo (−6,4 contre −4,5). La fiche de zone et le tableau d'annexe donnent donc, pour la même zone et le même indicateur, deux évolutions différentes (7,0 dans la fiche, 7,0 au tableau 54 : la colonne brute est cohérente ; mais l'évolution *ajustée* du tableau 54 ne peut pas être recalculée à partir de la fiche, qui ne la publie pas). Le lecteur qui veut comprendre la différence entre évolution brute et évolution ajustée d'une zone n'a aucun moyen de la reconstituer.

## B.6 Conséquence : le rapport ne peut pas être validé en l'état

Il faut être précis sur ce que cela signifie, car la formulation « les chiffres ne sont pas reproductibles » serait excessive et fausse.

**Ce qui est établi :** les tableaux descriptifs sont exacts ; les tableaux d'estimation ne proviennent pas du classeur livré ; les intervalles de confiance de quatre tableaux descriptifs ont été recalculés ; deux tableaux n'ont pas de source ; deux valeurs de T0 ont été corrigées sans note.

**Ce qui en découle :** aucune phrase du rapport ne peut être validée tant que l'estimation principale n'est pas arrêtée, parce qu'on ne sait pas si elle portera sur 2,9 ou 3,1 (P1) et sur −3,6 ou −3,1 (P2). Or ces deux indicateurs sont, avec P3 et P4, les quatre résultats confirmatoires. La différence entre 2,9 et 3,1 ne change pas la conclusion — les quatre intervalles contiennent zéro — mais elle rend le rapport attaquable sur la forme, et dans un document qui revendique une inférence à seize grappes et une correction de Holm, l'attaquabilité formelle suffit à disqualifier la diffusion.

**Ce qui est à faire, dans l'ordre :** arrêter l'estimation principale (REC-004) ; régénérer toutes les sorties d'estimation avec cette spécification et un identifiant de version (REC-005) ; recalculer les quatre tableaux « trois volets » et les matrices de sensibilité depuis cette même sortie (REC-006) ; rédiger l'annexe A (REC-003).

> **REC-004 — Arrêter une estimation principale unique et la déclarer** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-004 |
| 2. Constat | Deux spécifications sont présentées simultanément (modèle conjoint à effets fixes d'aire et DiD à 16 points), avec des valeurs différentes pour P1 et P2, et les figures étiquettent l'une en montrant l'autre. |
| 3. Preuve | Tableau 20, colonnes F et K ; `T25_tableau_des_effets`, colonnes F et I ; figures 1 et 7 ; légendes des figures 1 et 8. |
| 4. Axe | 5 — inférence ; axe 3 |
| 5. Criticité | Bloquant |
| 6. Cause probable | Le § 1.4 définit le modèle conjoint comme estimation principale ; le § 6 et les figures héritent d'un état antérieur où la DiD à 16 points l'était. |
| 7. Effet | Le lecteur ne sait pas quel coefficient commenter ; les matrices de sensibilité portent sur l'autre spécification. |
| 8. Recommandation | Déclarer le modèle conjoint à effets fixes d'aire (CR2, Satterthwaite) comme estimation principale unique ; présenter la DiD à 16 points comme sensibilité ; aligner les légendes des figures 1 et 8 ; recalculer les matrices sur la spécification déclarée. |
| 9. Modalité | Auteur du rapport et producteur des sorties, en une passe unique ; contrôle : les quatre valeurs du tableau 20 doivent figurer dans un onglet du classeur. |
| 10. Livrable | Tableau 20 v2 + figures 1 et 7 v2 + note de version. |
| 11. Effort | 3 jours-personne (dont recalcul). |
| 12. Dépendance | Aucune — c'est le point de départ. |
| 13. Clôture | 8/8 valeurs (4 primaires × 2 spécifications) retrouvées à l'identique dans le classeur. |
| 14. Statut | Ouvert. |

> **REC-005 — Horodater et versionner chaque sortie** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-005 |
| 2. Constat | Les écarts entre le classeur du 15 octobre et le rapport du 19 octobre ne sont signalés nulle part ; aucune sortie ne porte de version. |
| 3. Preuve | Partie B, cas 1 à 5, 19 à 27 ; en-têtes des 78 onglets. |
| 4. Axe | 8 — traçabilité |
| 5. Criticité | Majeur |
| 6. Cause probable | Absence de convention de version dans la chaîne de production. |
| 7. Effet | Tout écart devient indétectable ; la charge d'audit croît avec chaque version. |
| 8. Recommandation | Inscrire en première ligne de chaque onglet : `version / date / script / commit` ; reporter la même mention en note de chaque tableau du rapport. |
| 9. Modalité | Producteur ; ajout automatisé dans le script d'export. |
| 10. Livrable | Classeur v2 + modèle de note de tableau. |
| 11. Effort | 1 jour-personne. |
| 12. Dépendance | REC-004. |
| 13. Clôture | 78/78 onglets horodatés ; 60/60 tableaux porteurs d'une mention de version. |
| 14. Statut | Ouvert. |

> **REC-006 — Recalculer les tableaux « trois volets » et les matrices de sensibilité depuis la sortie unique** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-006 |
| 2. Constat | Les intervalles des tableaux 7, 8, 12 et 15 sont systématiquement plus étroits que ceux du classeur (42/45 et 51/57 lignes) ; les matrices 42 à 45 sont calculées sur l'ancienne estimation principale. |
| 3. Preuve | Partie B, cas 15 à 17 et 28 ; `T14_cac_3volets`, `T14_reco_3volets`, `T53_sensibilite_P1` à `P4`. |
| 4. Axe | 3 — réconciliation ; axe 5 |
| 5. Criticité | Bloquant |
| 6. Cause probable | Recalcul partiel lors du second passage, sans régénération des tableaux dérivés. |
| 7. Effet | Les intervalles publiés sont plus favorables que les intervalles réels ; la sensibilité documente une autre estimation que celle annoncée. |
| 8. Recommandation | Régénérer d'un bloc les 5 tableaux « trois volets », les 7 matrices de sensibilité et le tableau 41 ; publier en note la méthode d'inférence (ddl, bootstrap) de chaque tableau. |
| 9. Modalité | Producteur ; exécution unique du script, puis contrôle des 4 primaires et de 20 lignes tirées au hasard. |
| 10. Livrable | 13 tableaux v2 + journal d'exécution. |
| 11. Effort | 3 jours-personne. |
| 12. Dépendance | REC-004, REC-005. |
| 13. Clôture | 0 écart d'intervalle entre le rapport et le classeur sur les 13 tableaux. |
| 14. Statut | Ouvert. |

## B.7 Points examinés et écartés

Un audit qui ne dit que ce qu'il trouve est incomplet : il doit dire aussi ce qu'il a soupçonné et infirmé. Quatre suspicions ont été levées.

**Les « désalignements structurels » de quatre tableaux n'existent pas.** Les tableaux 3, 4, 6 et 9 comptaient 18, 8, 13 et 25 lignes là où les onglets `T02_realisation_zs`, `T01_bilan_appariement`, `T12_profil_acteurs` et `T16_categories_organes` en comptent 17, 7, 12 et 24. La vérification, ligne à ligne, montre que l'écart est exactement d'une ligne : la ligne d'en-tête, comptée dans le tableau Word et exclue du décompte de données du classeur. **Aucun désalignement structurel n'est retenu.** Les quatre tableaux sont appariables 1:1.

**Le tableau 3 ne contient pas de colonnes « évolution ajustée » absentes de sa source.** La colonne existe dans l'onglet, en position 9. La suspicion venait d'une lecture de l'en-tête sur deux lignes.

**Les totaux du résumé exécutif sont arithmétiquement exacts.** 5 713 ménages = 2 857 + 2 856 ; 1 148 RECO = 576 + 572 ; 1 144 CAC = 573 + 571 ; 192 CODESA = 96 + 96 ; 326 ASC = 177 + 149. Ces totaux se réconcilient au centime avec le tableau 3. Le problème n'est donc pas arithmétique, il est sémantique — il est traité en D.2 : ce sont des observations, non des unités.

**La progression des unités est correctement calculée.** Le contrôle des seuils par organe (11,1 pts pour les CAC, 14,3 pour les CODESA) confirme que les évolutions sont des multiples exacts du pas ; aucune unité ne présente d'évolution intermédiaire, ce qui valide la construction de l'indicateur. Le décompte (CAC : 51 progressions et 33 régressions dans le bras intervention, 53 et 52 dans le bras témoin ; CODESA : 19 et 12 contre 20 et 9) est exact. En revanche, la phrase du rapport selon laquelle il y aurait « autant de dégradations que d'améliorations » n'est vraie que pour le bras témoin des CAC : dans le bras intervention des CAC, les progressions sont plus nombreuses que les régressions (51 contre 33).
