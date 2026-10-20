---

# PARTIE D — Cohérence scientifique interne

*Axe 2 — définitions et indices ; axe 4 — effectifs et dénominateurs ; axe 5 — inférence et robustesse ; axe 10 — registre de communication.*

## D.1 Un indicateur, deux définitions

Le défaut le plus insidieux d'un rapport quantitatif n'est pas la valeur fausse : c'est le même nom porté par deux mesures. L'audit en a relevé quatre cas, tous corrigeables, tous susceptibles d'invalider une phrase du rapport le jour où elle sera écrite.

**« Carnet de vaccination vu ».** L'indicateur W2 est publié, au tableau 37, comme « carnet vu, tous ménages » (28,9 % à T0 à Kibombo, 46,4 % à T1). Il est utilisé ailleurs comme « carnet vu parmi les vaccinés ». Deux dénominateurs, un seul libellé. La fiche de zone de Kibombo affiche 28,9 → 46,4, ce qui correspond au dénominateur « tous ménages » ; le calcul de l'écart entre vaccination déclarée et carnet vu n'a de sens que si les deux portent sur le même dénominateur — ce qui est le cas ici, mais le lecteur ne peut pas le savoir. Correction : deux libellés distincts, et une note qui donne le dénominateur de chacun.

**« Connaissances des ménages ».** L'indicateur P2 est appelé « connaissances des ménages » au tableau 20, « connaissances déclarées des ménages (citations) » au tableau 21 et dans la figure 7, « connaissances déclarées (citations, 0-100) » ailleurs. Trois libellés pour un indice construit sur 24 items (L10, 18 items de signes de danger + K3/K6 pour la Mpox). La précision « déclarées (citations) » n'est pas cosmétique : elle indique que l'indice mesure ce que la répondante cite, non ce qu'elle reconnaît. Un lecteur qui commente « les connaissances ont progressé de 8,6 points » doit savoir laquelle des deux choses a progressé.

**Indice de résultats ménages (D3).** Le classeur (T07) le compose de six composantes, dont le recours formel ; le rapport en décrit cinq. Les poids publiés ne correspondent pas : 0,218 contre 0,177 pour la composante principale, 0,191 contre 0,139 pour la suivante. Une composante en plus, des poids différents, un même nom : l'indice D3 du rapport et l'indice D3 du classeur ne mesurent pas la même chose.

**Indice de riposte Mpox.** Le tableau 10 contient deux lignes portant ce libellé, avec des effectifs incompatibles (6 et 36 unités par zone). Deux lignes, un nom, deux populations.

> **REC-007 — Verrouiller le dictionnaire des indicateurs et l'imposer partout** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-007 |
| 2. Constat | Quatre indicateurs portent plusieurs définitions ou plusieurs libellés ; deux lignes du tableau 10 partagent un libellé avec des effectifs incompatibles ; les poids de D3 diffèrent entre le corps et l'annexe. |
| 3. Preuve | Tableaux 20, 21, 37, 47 ; `T07_poids_indices_domaine` (0,218 / 0,191) contre tableau 47 (0,177 / 0,139) ; `T10_emd_par_bras` (deux lignes « CODESA : indice de riposte Mpox »). |
| 4. Axe | 2 — définitions |
| 5. Criticité | Bloquant |
| 6. Cause probable | Le dictionnaire (tableau 46, 88 indicateurs) n'est pas la source unique des libellés : les tableaux ont été produits à des dates différentes. |
| 7. Effet | Un même mot désigne deux mesures ; toute phrase d'interprétation devient indécidable. |
| 8. Recommandation | Faire du tableau 46 la source unique : une ligne par indicateur, colonnes `code`, `libellé court`, `libellé long`, `dénominateur`, `unité`, `nombre d'items`, `composantes`, `poids`. Interdire toute variante dans les tableaux et figures ; faire vérifier automatiquement l'égalité des libellés. |
| 9. Modalité | Producteur + auteur ; passe de normalisation sur 60 tableaux et 20 figures. |
| 10. Livrable | Tableau 46 v2 + rapport v2 avec libellés homogènes. |
| 11. Effort | 3 jours-personne. |
| 12. Dépendance | REC-004 (les composantes de D3 doivent être figées avant d'être documentées). |
| 13. Clôture | 0 libellé divergent entre le dictionnaire, les tableaux et les figures ; 0 doublon de libellé dans une même table. |
| 14. Statut | Ouvert. |

**Sur la fiabilité, un point positif à ne pas perdre.** Les indices réflexifs sont correctement documentés (tableau 48) : alpha de KR-20 de 0,909 pour les 18 signes de danger sur 5 713 observations, 0,916 pour l'indice P2 à 24 items, avec un contrôle par bras et par passage (0,841 à 0,927). Les paramètres IRT (tableau 49) montrent des discriminations jusqu'à 3,41 et une difficulté de 4,51 pour l'item 16 : ces valeurs extrêmes mériteraient une phrase, car un item de difficulté 4,5 sur une échelle centrée sur zéro n'apporte presque aucune information dans la population étudiée. C'est un commentaire à écrire, pas une erreur à corriger.

## D.2 Effectifs : trois populations sous un même mot

C'est le point où le rapport risque la mauvaise foi involontaire — celle qui ne trompe personne exprès mais qui trompe tout le monde.

**Le cas des CAC.** Le chapitre 3 décrit les CAC enquêtés : 573 à T0, 571 à T1, 1 144 observations au total, et le modèle du tableau 20 porte sur 1 143 observations. La figure 6 et le tableau 14 décrivent les transitions des CAC **appariés** : 306 unités (56,5 % des 542 unités de T0). Entre 1 143 et 306, il y a un facteur 3,7. Les deux nombres sont justes ; ils ne mesurent pas la même population. Le rapport ne le dit pas au moment où il passe de l'un à l'autre, et le lecteur qui additionne les mouvements de la figure 6 pour en tirer une conclusion sur « les CAC » se trompe de population.

**Le cas des ménages.** 5 713 observations (2 857 à T0, 2 856 à T1), 4 991 observations dans les modèles (soit 87,4 %), 385 villages appariés sur 688 (56 %), 94 aires appariées sur 98 (95,9 %). Le résumé exécutif annonce « 5 713 ménages » : ce sont des observations, et le nombre de ménages distincts est inférieur, puisque le rapprochement territorial n'a retrouvé que 56 % des villages. La phrase doit dire « 5 713 observations ménages (2 857 à T0, 2 856 à T1, 4 991 dans les modèles) » et non « 5 713 ménages ».

**Le cas des aires.** Le résumé exécutif annonce 98 aires. Le tableau 4 en distingue 93 enquêtées à T0, 94 à T1, 91 appariées. La figure 5 (transitions des CODESA) repose sur 91 aires : 46 dans le bras témoin (22 + 15 + 9) et 45 dans le bras intervention (26 + 11 + 8). Les trois nombres — 98, 93 et 91 — sont cohérents si l'on comprend que 98 est la base de sondage, 93 les aires effectivement enquêtées et 91 les aires présentes aux deux passages. Encore faut-il l'écrire, sinon le lecteur conclut à sept aires perdues.

**Le cas des CODESA.** 96 à T0 et 96 à T1 (tableau 3), 91 appariées, mais le modèle du tableau 20 porte sur 186 observations et 185 pour l'indice de capacités. L'écart entre 96 × 2 = 192 et 186 s'explique par les manquants, mais il n'est pas commenté.

> **REC-008 — Distinguer systématiquement trois effectifs : base, enquêtés, analysés** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-008 |
| 2. Constat | « 5 713 ménages », « 1 148 RECO », « 1 144 CAC » sont des observations ; 306 CAC appariés cohabitent avec 1 143 observations ; 98 aires (base), 93 enquêtées et 91 appariées sont utilisées sans distinction. |
| 3. Preuve | Tableau 3 (sommes), tableau 4, tableau 20 colonne N, `T20_transitions_matrices` (effectifs 22/15/9 et 26/11/8), résumé exécutif. |
| 4. Axe | 4 — effectifs |
| 5. Criticité | Majeur |
| 6. Cause probable | Vocabulaire d'enquête (« ménages ») employé pour des unités d'observation. |
| 7. Effet | Le lecteur double ou triple mentalement les effectifs ; les taux de couverture sont mal interprétés. |
| 8. Recommandation | Adopter une convention unique et l'afficher en tête du tableau 3 : `base de sondage` / `unités enquêtées (T0, T1)` / `unités appariées` / `observations analysées`. Reprendre le résumé exécutif avec ces quatre colonnes. |
| 9. Modalité | Auteur ; reprise du tableau 3 et du résumé exécutif ; contrôle sur les 6 populations. |
| 10. Livrable | Tableau 3 v2 (6 lignes × 5 colonnes) + résumé exécutif corrigé. |
| 11. Effort | 1 jour-personne. |
| 12. Dépendance | Aucune. |
| 13. Clôture | 0 emploi du mot « ménages » pour des observations ; les 4 effectifs présents pour chacune des 6 populations. |
| 14. Statut | Ouvert. |

## D.3 L'appareil de décision : EMD, seuils et cas A à E

Le rapport dispose d'un appareil de décision à trois étages : l'effet minimal détectable (EMD), qui mesure la précision ; le seuil de pertinence, qui mesure l'intérêt programmatique ; la grille des cas A à E, qui croise les deux avec l'intervalle de confiance. Cet appareil est conceptuellement juste — c'est même la partie la plus avancée du document — mais il est appliqué de façon telle qu'il produit des conclusions que les données ne soutiennent pas.

**Les valeurs, telles que le classeur les donne.**

| Primaire | EMD | Seuil de pertinence | Effet estimé | IC 95 % | Cas |
|---|---:|---:|---|---|---|
| P1 Exposition | 10,1 | 5 | 2,9 | [−4,4 ; 10,3] | D |
| P2 Connaissances | 10,1 | 5 | −3,6 | [−10,8 ; 3,7] | E |
| P3 Fonctionnalité CAC | 8,8 | 11 | 0,1 | [−6,2 ; 6,4] | E |
| P4 Professionnalisation RECO | 13,3 | 8 | −3,2 | [−12,9 ; 6,6] | E |

**Le raisonnement que ces chiffres autorisent — et celui qu'ils n'autorisent pas.**

Pour P1 et P2, le seuil de pertinence (5 points) est inférieur à l'EMD (10,1 points). L'intervalle de confiance s'étend de part et d'autre du seuil : on ne peut donc ni établir un gain pertinent, ni exclure une perte pertinente. La conclusion correcte est « indéterminé », ce que la grille code D. C'est une conclusion négative, et elle doit être assumée comme telle.

Pour P4, le seuil (8 points) est également inférieur à l'EMD (13,3 points), et l'intervalle [−12,9 ; 6,6] contient le seuil dans les deux sens : même conclusion, indéterminé.

Pour P3, en revanche, le seuil (11 points) est **supérieur** à l'EMD (8,8 points). L'intervalle [−6,2 ; 6,4] est entièrement contenu entre −11 et +11. Cela signifie que, pour la fonctionnalité des CAC, le dispositif **permet de conclure** : aucun effet d'une ampleur programmatiquement pertinente n'est compatible avec les données. Ce n'est pas la même chose que « pas d'effet » — un effet de 5 points reste possible — mais c'est une conclusion forte, et c'est la seule des quatre qui soit établie par le dispositif.

Or le rapport traite les quatre primaires de la même manière, avec un cas E pour P3 et P4 et un cas D pour P1 et P2, comme si les quatre étaient également indéterminés. **Le seul résultat conclusif du rapport — l'absence d'effet pertinent sur la fonctionnalité des CAC — n'est pas identifié comme tel.** C'est un manque à gagner considérable : c'est précisément le type de conclusion qu'un bailleur peut utiliser.

**Le problème secondaire : les seuils ne sont pas sourcés.** Les valeurs de 5, 11, 8 points (et 0,25 écart-type pour les indices de domaine) apparaissent dans les tableaux et les notes de figure sans référence. Sont-elles issues du protocole, d'une norme du PSN SACO 2025-2030, d'un consensus d'experts ? Le lecteur ne peut pas le savoir, et un seuil de pertinence non sourcé est un seuil arbitraire — ce qui affaiblit l'argument au moment même où il deviendrait utile.

**La grille des cas n'est pas disponible là où elle sert.** Le tableau 20 comporte une colonne « Cas » avec les lettres A à E, et la figure 8 affiche « cas D » et « cas E » à côté de chaque estimation. La définition des cinq cas figure dans un panneau de légende (figure non légendée, image `a784ad`) et dans une note de bas de figure. Aucun renvoi, aucune note de tableau. Le lecteur qui rencontre « cas D » au tableau 20 pour la première fois n'a aucun moyen de savoir ce qu'il lit sans sortir du tableau. De plus, la note de la figure 8 ne définit que le cas E (« gain au moins égal au seuil non soutenu par l'IC ; une baisse n'est pas exclue ») et laisse A, B, C et D sans définition.

> **REC-009 — Sourcer les seuils et rendre la grille des cas autoportante** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-009 |
| 2. Constat | Les seuils de pertinence (5 ; 11 ; 8 points ; 0,25 écart-type) ne sont pas sourcés ; la grille des cas A à E n'est définie qu'en note de figure et de façon partielle (seul le cas E est défini). |
| 3. Preuve | Tableau 20 colonnes M et N ; figure 8 et sa note ; panneau de légende (image `a784ad`) ; § 1.3. |
| 4. Axe | 5 — inférence ; axe 10 |
| 5. Criticité | Majeur |
| 6. Cause probable | Les seuils proviennent du protocole, non reproduit dans le rapport ; la grille a été conçue pour un usage graphique. |
| 7. Effet | Les décisions de pertinence reposent sur des valeurs non justifiées ; la colonne « Cas » est illisible isolément. |
| 8. Recommandation | Insérer, au § 1.3, un tableau de 4 lignes (indicateur, seuil, source du seuil, EMD) et la définition complète des cinq cas ; ajouter en note du tableau 20 le renvoi au § 1.3. |
| 9. Modalité | Auteur ; rédaction d'une demi-page + note de tableau. |
| 10. Livrable | § 1.3 v2 + note du tableau 20. |
| 11. Effort | 0,5 jour-personne. |
| 12. Dépendance | REC-004. |
| 13. Clôture | 4/4 seuils sourcés ; 5/5 cas définis dans le corps, avant leur premier emploi. |
| 14. Statut | Ouvert. |

> **REC-010 — Identifier explicitement le seul primaire qui permet une conclusion** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-010 |
| 2. Constat | Pour P3, le seuil (11) dépasse l'EMD (8,8) et l'IC [−6,2 ; 6,4] est entièrement contenu dans la zone de non-pertinence : le dispositif conclut. Pour P1, P2 et P4, l'EMD dépasse le seuil : le dispositif ne conclut pas. Le rapport traite les quatre cas de la même façon. |
| 3. Preuve | Tableau 20, colonnes L, M, N ; `T25_tableau_des_effets` ; § 1.3. |
| 4. Axe | 5 — inférence |
| 5. Criticité | Bloquant (occasion manquée sur le seul résultat conclusif) |
| 6. Cause probable | Application uniforme de la grille sans examen de la relation EMD/seuil. |
| 7. Effet | Le rapport renonce à sa seule conclusion robuste et laisse croire que tout est indéterminé. |
| 8. Recommandation | Écrire, au chapitre 6 : « pour la fonctionnalité des CAC, l'intervalle de confiance est entièrement contenu dans la zone de non-pertinence (± 11 points), ce qui permet d'exclure un effet d'ampleur programmatique, sans exclure un effet modéré ; pour les trois autres primaires, l'EMD excède le seuil et aucune conclusion de pertinence n'est possible. » Ne pas modifier les valeurs. |
| 9. Modalité | Auteur ; rédaction d'un paragraphe ; validation par l'auditeur. |
| 10. Livrable | Paragraphe de conclusion du chapitre 6 + phrase correspondante du résumé exécutif. |
| 11. Effort | 0,5 jour-personne. |
| 12. Dépendance | REC-009. |
| 13. Clôture | La distinction « conclut / ne conclut pas » figure dans le résumé exécutif et dans le chapitre 6. |
| 14. Statut | Ouvert. |

## D.5 Le déséquilibre initial des indicateurs d'offre, et ce qu'il fait à la seule conclusion du rapport

L'onglet `T13_equilibre_T0`, qui alimente la figure 4, calcule les différences standardisées entre bras pour les covariables **et pour les indicateurs primaires**. Le résultat mérite d'être mis en avant, car il n'apparaît ni dans un tableau du corps ni dans le texte.

| Indicateur | DS à T0 | DS à T1 | Bande de la figure 4 |
|---|---:|---:|---:|
| P1 Exposition des ménages | −0,095 | −0,002 | ± 0,10 |
| P2 Connaissances des ménages | 0,110 | 0,039 | ± 0,10 |
| **P3 Fonctionnalité des CAC** | **0,376** | **0,431** | ± 0,10 |
| **P4 Professionnalisation des RECO** | **0,275** | 0,158 | ± 0,10 |
| D3 Résultats ménages | 0,060 | 0,204 | ± 0,10 |
| *Instruction : aucune* (covariable) | *0,35* | *0,29* | ± 0,10 |
| *Taille du ménage* (covariable) | *−0,32* | *−0,20* | ± 0,10 |

Précision de vocabulaire, pour éviter une confusion : la valeur 0,25 qui figure au tableau 20 est un **seuil de pertinence** pour les indices de domaine, non un seuil d'équilibre. Le seuil d'équilibre retenu par la figure 4 est de ± 0,10. C'est à cette bande qu'il faut se référer, et elle est franchie par P3 et P4 — respectivement 3,8 et 2,8 fois — comme par deux covariables (instruction « aucune » à 0,35 et taille du ménage à −0,32). Une phrase du rapport qui affirmerait l'équilibre des bras sur les covariables serait donc fausse pour ces deux variables.

Deux indicateurs primaires sur quatre présentent à l'inclusion un déséquilibre très supérieur à la bande de ± 0,10, et pour P3 ce déséquilibre **s'aggrave** au second passage (0,376 puis 0,431).

**Ce que cela ne fait pas.** Cela n'invalide pas la différence de différences : le devis ne suppose pas l'égalité des niveaux, seulement le parallélisme des tendances. Un écart de niveau de 8,7 points entre bras — 75,6 contre 66,9 à T0 sur la fonctionnalité des CAC — est compatible avec une identification valide du DiD.

**Ce que cela fait.** Cela impose deux précautions, dont une seule est prise.

*Première précaution, non prise : l'effet plafond.* L'indice de fonctionnalité des CAC est borné à 100. Le bras intervention part de 75,6 et dispose donc de 24,4 points de marge, le bras témoin de 66,9 et de 33,1 points. À supposer que les deux bras progressent d'une même quantité « vraie », le bras le plus haut plafonne plus tôt : le DiD est mécaniquement biaisé vers le bas. Autrement dit, **la conclusion « aucun effet pertinent sur P3 » est conservatrice** : elle sous-estime plutôt qu'elle ne surestime un éventuel effet. C'est une bonne nouvelle analytique, à condition d'être dite — car un lecteur qui constate l'écart de niveau sans lire cette explication conclura à l'inverse, que le programme a été testé sur des zones déjà bien dotées.

*Seconde précaution, partiellement prise : le test de tendance.* Le rapport produit des placebos (tableau 23) et une sensibilité à la divergence de tendance (tableau 24), ce qui couvre le risque de non-parallélisme. Mais il ne produit pas de test d'égalité des tendances avant traitement — ce qui est impossible avec deux passages — et ne discute donc pas le risque que les 0,376 → 0,431 signent une divergence de tendance plutôt qu'un simple décalage de niveau.

Il faut ajouter un élément qui renforce l'inquiétude : entre T0 et T1, le bras intervention gagne 3,8 points sur P3 (75,6 → 79,4) et le bras témoin 3,5 points (66,9 → 70,4). Les tendances sont donc quasi parallèles — c'est précisément pourquoi le DiD vaut 0,1 — mais la différence standardisée augmente parce que la variance inter-zones se réduit. Une hausse du DS avec des tendances parallèles est un artefact de dénominateur, non un signal de divergence : c'est une phrase à écrire, faute de quoi le DS de 0,431 sera lu comme une aggravation du déséquilibre.

> **REC-019 — Traiter le déséquilibre initial et l'effet plafond des indicateurs d'offre** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-019 |
| 2. Constat | P3 (0,376) et P4 (0,275) dépassent à T0 la bande d'équilibre de ± 0,10 de la figure 4 (3,8 et 2,8 fois) ; le DS de P3 monte à 0,431 à T1 ; deux covariables la dépassent aussi (0,35 et −0,32) ; ni la figure 4 ni le texte ne les signalent ; l'effet plafond de P3 n'est pas discuté. |
| 3. Preuve | `T13_equilibre_T0`, lignes « P3 fonctionnalité CAC » et « P4 professionnalisation RECO » ; tableau 20 (P3 : 75,6 → 79,4 contre 66,9 → 70,4). |
| 4. Axe | 4 — comparabilité ; axe 5 |
| 5. Criticité | Majeur |
| 6. Cause probable | La figure 4 a été conçue pour les covariables ; les primaires y ont été ajoutés sans traitement narratif. |
| 7. Effet | Le lecteur peut conclure soit à un déséquilibre rédhibitoire, soit à une aggravation, alors que le DiD reste valide et que son biais va dans le sens conservateur. |
| 8. Recommandation | Insérer au § 2 un paragraphe de dix lignes et un tableau de 4 lignes ; y expliquer (a) que le DiD n'exige pas l'égalité des niveaux, (b) que le plafond de 100 biaise P3 vers le bas, donc que la conclusion négative est conservatrice, (c) que la hausse du DS de P3 résulte d'une réduction de variance et non d'une divergence de tendance. Ne modifier aucune valeur. |
| 9. Modalité | Auteur ; rédaction d'un paragraphe + tableau 13 remonté au corps. |
| 10. Livrable | § 2.3 nouveau + tableau 13 publié. |
| 11. Effort | 1 jour-personne. |
| 12. Dépendance | REC-010. |
| 13. Clôture | Les trois points (a), (b), (c) figurent au corps du texte, avec les valeurs. |
| 14. Statut | Ouvert. |

## D.4 Robustesse : ce qui est fait, ce qui manque

**Ce qui est fait, et bien fait.** Le rapport ne cache aucun de ses résultats défavorables. Les p ajustées de Holm valent 1,000 pour les quatre primaires, et le tableau les affiche. La correction de Benjamini-Hochberg sur les indicateurs secondaires donne une p ajustée minimale de 0,607 : aucun ne survit, et le rapport le dit au lieu de commenter les p brutes. Les placebos (tableau 23) sont produits et montrent des DiD non significatives. La divergence de tendance est testée à ± 2 et ± 5 points (tableau 24) et le retrait d'une zone à tour de rôle est conduit (figure 20). Les courbes de spécification (figure 19) et les sept matrices de sensibilité (tableaux 42 à 45) complètent le dispositif. C'est un dossier de robustesse complet.

**Deux manques précis, et un point de méthode.**

*Le premier est une variante classée « inchangée » qui triple l'effet.* Dans la matrice de sensibilité de P1 (`T53_sensibilite_P1`), la variante « sans l'item L6_recent » donne 5,5 [−0,5 ; 11,5] avec p = 0,069, là où l'estimation principale vaut 1,9 [−4,4 ; 8,3] avec p = 0,506. L'effet est presque triplé, la p-value divisée par sept, et la borne supérieure de l'intervalle (11,5) franchit le seuil de pertinence de 5 points : la variante devient compatible avec un gain pertinent, ce que l'estimation principale n'était pas. Or la colonne « Conclusion inchangée » porte « oui », et le tableau 41 annonce 100 % de variantes concordantes pour cet indicateur. Le classement est défendable si la conclusion s'entend comme « aucun effet établi » — l'intervalle contient encore zéro et le seuil — mais il masque le fait que la seule variante portant sur la **définition même de l'indice** (retrait d'un item) est aussi celle qui déplace le plus le résultat. C'est le genre de sensibilité qu'un rapport doit commenter en corps de texte, pas laisser dans la seizième ligne d'une matrice.

**Un point de méthode à surveiller.** Les modèles multinomiaux (première réaction devant l'enfant malade, tableau 35) et les modèles en deux parties (tableau 36) sont estimés sur 4 991 observations avec 16 grappes. Le rapport applique CR2 et Satterthwaite, ce qui est la bonne réponse à la structure de grappes, mais il ne donne pas les degrés de liberté de ces modèles dans les notes de tableaux, alors qu'il les donne pour les primaires (10,8 à 11). L'ajout est trivial et il est nécessaire : sans lui, le lecteur ne peut pas apprécier la précision réelle des probabilités prédites.

*Le second concerne une ligne à effectif dérisoire, et une seule.* Le tableau 33 présente la part de femmes parmi les « RECO désignés depuis moins d'un an (T1) » avec un effectif de 2 et une valeur de 0 %. Un pourcentage calculé sur deux unités n'est pas un pourcentage : il vaut 0 %, 50 % ou 100 % selon un cas individuel. La ligne est de surcroît présente pour le seul bras témoin, ce qui la rend incomparable. Elle doit être supprimée ou fusionnée avec la ligne « RECO » qui porte, elle, sur 285 à 288 unités. À l'inverse, les lignes « Membres des CODESA » et « Répondant CODESA femme » reposent sur 48 unités chacune, ce qui est faible mais assumé et cohérent avec le tableau 3 : elles peuvent rester, à condition que le n figure dans le tableau — ce qui est le cas.

> **REC-011 — Traiter la sensibilité qui déplace le plus le résultat** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-011 |
| 2. Constat | La variante « sans l'item L6_recent » porte l'effet de P1 de 1,9 à 5,5 (p 0,069) et sa borne haute à 11,5, au-delà du seuil de 5 ; elle est classée « conclusion inchangée ». |
| 3. Preuve | `T53_sensibilite_P1`, ligne 16 ; `T54_synthese_sensibilite`, ligne « Indice d'exposition » (min −0,5 ; max 5,5 ; 18/18 concordantes) ; tableau 41. |
| 4. Axe | 5 — robustesse |
| 5. Criticité | Majeur |
| 6. Cause probable | Le critère de « conclusion inchangée » ne compare que la présence de zéro dans l'intervalle, non le déplacement vers la zone de pertinence. |
| 7. Effet | La sensibilité la plus structurante (définition de l'indice) apparaît comme une variante neutre. |
| 8. Recommandation | Commenter cette variante dans le corps du chapitre 6 ; préciser le critère de classement (position par rapport à 0 **et** au seuil) ; conserver la valeur telle quelle. |
| 9. Modalité | Auteur ; un paragraphe + une note de méthode sur le critère de classement. |
| 10. Livrable | Paragraphe du § 6.1 et note du tableau 41. |
| 11. Effort | 0,5 jour-personne. |
| 12. Dépendance | REC-009. |
| 13. Clôture | La variante figure au corps du texte avec ses deux bornes et son seuil. |
| 14. Statut | Ouvert. |
