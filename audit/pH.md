---

# PARTIE H — Troisième passe : contrôles d'identité arithmétique et de cohérence des intervalles

*Cette partie poursuit la logique des précédentes : elle ne répète rien, elle vérifie ce qui ne l'avait pas été. Trois des contrôles ont infirmé un soupçon antérieur, quatre ont produit des constats nouveaux. Tous sont reproductibles à partir des onglets cités.*

## H.1 La divergence des tableaux de zone est localisée : elle porte sur l'ajustement, non sur l'écart

Les tableaux 21, 22, 54 et 55 présentent, pour chaque zone, une « évolution ajustée » et un « écart à la moyenne provinciale ». La partie B avait établi que l'évolution ajustée diverge du classeur dans 10 zones sur 16 (P1) et 9 sur 16 (P2), sans que l'écart à la moyenne provinciale soit testé. Le contrôle d'identité règle la question.

**L'identité « écart = évolution ajustée − moyenne provinciale » est respectée dans les deux fichiers.** Sur les 128 cellules concernées (4 tableaux × 16 zones × 2 colonnes), la règle de calcul est vérifiée 64 fois sur 64 dans le classeur et 64 fois sur 64 dans le rapport (tolérance 0,15 point, qui couvre l'arrondi d'affichage et le fait que la moyenne provinciale est recalculée sur les zones du tableau).

**Conséquence : la divergence n'est pas une faute de recopie, c'est un changement de méthode d'ajustement.** Si le rapport avait recopié l'évolution ajustée du classeur et recalculé l'écart, l'identité serait rompue dans un des deux documents. Elle ne l'est nulle part. Le rapport a donc recalculé **les deux** colonnes à partir d'un ajustement différent, ce qui déplace mécaniquement l'écart à la moyenne provinciale.

| Tableau | Colonne « évolution ajustée » | Colonne « écart à la moyenne » |
|---|---|---|
| 21 (P1, corps) | 10 zones sur 16 divergent | 11 zones sur 16 divergent |
| 54 (P2, annexe D) | 9 zones sur 16 divergent | 8 zones sur 16 divergent |
| 22 (P3, corps) | 0 | 0 |
| 55 (P4, annexe D) | 0 | 0 |
| **Total** | **19 / 64** | **19 / 64** |

**Ce que cela change pour la correction.** La recommandation REC-006 n'a pas à « corriger des valeurs » : elle doit **écrire la règle d'ajustement et la publier en note** des tableaux 21 et 54, puis régénérer les deux colonnes. Une note de trois lignes — modèle utilisé, covariables, niveau d'ajustement — suffit à rendre les 38 cellules reproductibles. C'est la correction la moins coûteuse du dossier et l'une des plus rentables : elle concerne les deux seuls tableaux où le lecteur peut situer une zone par rapport à sa province.

> **REC-023 — Écrire la règle d'ajustement des tableaux de zone et régénérer les deux colonnes** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-023 |
| 2. Constat | Les colonnes « évolution ajustée » et « écart à la moyenne provinciale » divergent du classeur dans 19 zones sur 64 chacune, alors que l'identité arithmétique qui les lie est respectée dans les deux fichiers : l'ajustement a été recalculé, non recopié. |
| 3. Preuve | Tableaux 28, 71, 29 et 72 du document Word ; `T19_16_zones_P1` à `P4` colonnes H, I, J ; test d'identité J = I − moyenne provinciale (64/64 dans chaque fichier). |
| 4. Axe | 3 — réconciliation |
| 5. Criticité | Bloquant |
| 6. Cause probable | Un modèle d'ajustement différent entre l'export du 15 octobre et la rédaction du 19 octobre, sans note de méthode. |
| 7. Effet | 38 cellules publiées ne peuvent pas être reproduites ; le lecteur ne peut pas situer une zone dans sa province. |
| 8. Recommandation | Ajouter en note des tableaux 21, 22, 54 et 55 : modèle, covariables, niveau d'ajustement, et la règle de calcul de l'écart ; régénérer les deux colonnes depuis la sortie unique. Ne pas modifier les valeurs à la main. |
| 9. Modalité | Producteur ; note de tableau + régénération. |
| 10. Livrable | 4 tableaux v2 + note d'ajustement. |
| 11. Effort | 1 jour-personne. |
| 12. Dépendance | REC-006 (même exécution). |
| 13. Clôture | 128/128 cellules identiques au classeur ; note présente en bas des 4 tableaux. |
| 14. Statut | Ouvert. |

## H.2 Les tableaux d'unités appariées se réconcilient exactement — et cela précise ce qu'est le tableau 22

Trois contrôles de cohérence, tous concluants, qui n'avaient pas été faits.

**Le tableau 11 (mouvements) se réconcilie avec le tableau 4 (appariement).** Les effectifs se somment à 306 CAC appariés (159 dans le bras témoin, 147 dans le bras intervention) et 91 aires CODESA (46 et 45). Ce sont exactement les chiffres du bilan d'appariement. Les pourcentages somment à 100 (à 0,1 point près pour les CODESA témoins, arrondi). Aucune unité perdue, aucun double comptage.

**Le tableau 12 (unités en progression et régression) contient exactement les unités qui ont bougé.** Ses 249 lignes se décomposent en 189 CAC et 60 CODESA. Or 189 = 52 + 53 (CAC témoins) + 33 + 51 (CAC intervention) et 60 = 9 + 20 (CODESA témoins) + 12 + 19 (CODESA intervention) : la somme exacte des dégradations et améliorations du tableau 11. **Le tableau 12 n'omet aucune unité stable : il ne prétend pas les lister.** Le libellé du tableau devrait le dire (« unités ayant changé de catégorie »), car le lecteur qui compare 249 à 397 unités appariées conclut à un manque.

**Aucun doublon, aucune incohérence de calcul dans la liste nominative.** Les 249 unités sont uniques, et la colonne de mouvement égale exactement la différence entre les deux passages dans les 249 cas.

> **REC-024 — Nommer le tableau 12 pour ce qu'il est** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-024 |
| 2. Constat | Le tableau 12 liste 249 unités (189 CAC, 60 CODESA), soit exactement les unités ayant changé de catégorie ; son intitulé ne le dit pas et 148 unités stables du tableau 11 n'y figurent pas. |
| 3. Preuve | `T22_unites_progression_regressi` (249 lignes, 0 doublon, delta exact 249/249) ; `T21_mouvements_unites` (306 CAC et 91 CODESA, total 397). |
| 4. Axe | 2 — définition |
| 5. Criticité | Majeur |
| 6. Cause probable | Intitulé hérité du script de sélection (les unités stables sont filtrées en amont). |
| 7. Effet | Le lecteur croit à une liste incomplète ou à une perte d'unités. |
| 8. Recommandation | Renommer : « Unités appariées ayant changé de catégorie entre T0 et T1 (les 148 unités stables ne figurent pas dans cette liste) » ; publier l'agrégat par bras et par organe dans le corps, la liste nominative en annexe. |
| 9. Modalité | Auteur ; deux lignes de titre et de note. |
| 10. Livrable | Tableau 12 v2 + renvoi au tableau 11. |
| 11. Effort | 0,25 jour-personne. |
| 12. Dépendance | Aucune. |
| 13. Clôture | L'intitulé et la note mentionnent les unités stables ; 249 + 148 = 397. |
| 14. Statut | Ouvert. |

## H.3 La règle de progression n'est pas uniforme : cinq CAC sortent de la grille des neuf critères

Le rapport énonce une règle simple : une unité progresse si son évolution atteint un critère, soit 11,1 points pour les CAC (9 critères) et 14,3 pour les CODESA (7 critères). La vérification confirme la règle pour les CODESA — **60 évolutions sur 60 sont des multiples exacts de 14,3** — et pour l'essentiel des CAC (184 sur 189 sont des multiples de 11,1). Mais cinq CAC font exception, tous dans le bras témoin :

| Zone | s0 | s1 | Évolution | Mouvement attribué |
|---|---:|---:|---:|---|
| Tunda | 44,4 | 27,8 | −16,7 | Dégradation |
| Lodja | 72,2 | 100,0 | +27,8 | Amélioration |
| Minga | 22,2 | 50,0 | +27,8 | Amélioration |
| Nyantende | 61,1 | 77,8 | +16,7 | Amélioration |
| Nyantende | 50,0 | 69,4 | +19,4 | Amélioration |

Les valeurs 27,8 ; 50,0 ; 69,4 et 72,2 ne sont pas des multiples de 11,1. Elles sont en revanche toutes des multiples de 2,78, soit un trente-sixième : la grille réelle de l'indice est donc plus fine qu'un critère, ou le nombre de critères applicables varie d'une unité à l'autre. Dans les deux cas, **l'affirmation « un critère = 11,1 points » est fausse pour ces cinq unités**, et leur classement est fragile : une évolution de 16,7 points est comptée comme une amélioration au même titre qu'une évolution de 33,3.

L'incidence est faible (5 unités sur 189, soit 2,6 %) et ne déplace aucun résultat agrégé. Elle intéresse néanmoins la reproductibilité : un lecteur qui recalcule le tableau 11 à partir des scores individuels ne retrouvera pas les mêmes effectifs, et un évaluateur qui applique la règle littéralement classera la zone de Tunda différemment.

> **REC-025 — Décrire la grille réelle de l'indice de fonctionnalité des CAC** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-025 |
| 2. Constat | 5 CAC sur 189 présentent des scores qui ne sont pas des multiples de 11,1 (27,8 ; 50,0 ; 69,4 ; 72,2) et des évolutions de 16,7 et 19,4 points, incompatibles avec la règle « un critère = 11,1 points ». |
| 3. Preuve | `T22_unites_progression_regressi` (5 unités, toutes dans le bras témoin) ; `T21_mouvements_unites` (effectifs) ; § 1.3 du rapport. |
| 4. Axe | 2 — définition |
| 5. Criticité | Majeur |
| 6. Cause probable | Indice construit sur 36 unités élémentaires (2,78 points chacune) ou nombre de critères applicables variable selon l'unité. |
| 7. Effet | La règle de progression est appliquée avec un pas qui n'est pas celui de l'indice pour 2,6 % des CAC ; le tableau 11 n'est pas recalculable à l'identique. |
| 8. Recommandation | Décrire la grille élémentaire de l'indice (nombre d'items, pondération, traitement des items manquants) ; exprimer la règle de progression dans cette grille (« au moins quatre unités élémentaires ») plutôt qu'en points ; signaler le cas de Tunda si le classement change. |
| 9. Modalité | Producteur + auteur ; une note de méthode de cinq lignes. |
| 10. Livrable | § 1.3 v2 + note du tableau 11. |
| 11. Effort | 0,5 jour-personne. |
| 12. Dépendance | REC-007 (dictionnaire). |
| 13. Clôture | La grille élémentaire est décrite et la règle exprimée dans cette grille ; les 5 unités sont classées conformément à la règle écrite. |
| 14. Statut | Ouvert. |

## H.4 Le chapitre de l'équité ne peut pas conclure : gradient non monotone et intervalles contenant zéro

Deux constats, tirés de deux onglets que le rapport publie comme figures (14 et 15 du dossier d'images, tableaux sources `T37_gradient_quintiles` et `T36_concentration_erreygers`).

**Le « gradient » par quintile n'est monotone que dans 9 séries sur 32.** Sur les 32 séries (8 indicateurs × 2 bras × 2 passages), 23 présentent au moins un changement de sens, avec des amplitudes qui atteignent 20,9 points. Les trois plus fortes ruptures sont :

| Indicateur | Bras | Passage | Profil par quintile (Q1 → Q5) | Amplitude maximale d'un segment |
|---|---|---|---:|---:|
| Au moins quatre CPN (%) | Intervention | T0 | voir figure 14 | **20,9 points** |
| Accouchement en structure (%) | Intervention | T0 | — | 18,2 points |
| Enfant vacciné déclaré (%) | Intervention | T1 | — | 17,3 points |

Une série qui monte puis redescend n'est pas un gradient : c'est une relation non monotone, qui demande une autre lecture (seuil, effet de composition, ou absence de relation). Intituler la figure « Gradient par quintile de niveau de vie » engage une conclusion que 72 % des séries n'autorisent pas. Le titre doit être neutre (« Niveau des indicateurs par quintile de niveau de vie ») et le commentaire doit dire ce que ces ruptures impliquent.

**La moitié des indices de concentration ne se distinguent pas de zéro.** Sur les 24 indices d'Erreygers (6 indicateurs × 2 bras × 2 passages), **12 ont un intervalle de confiance qui contient zéro**. Le rapport ne peut donc pas affirmer qu'une inégalité existait, ni qu'elle a diminué, pour la moitié des indicateurs examinés. Et lorsque les intervalles excluent zéro, les évolutions vont dans le même sens dans les deux bras :

| Indicateur | Témoin T0 → T1 | Intervention T0 → T1 | Lecture |
|---|---|---|---|
| Exposition aux agents | +0,107 → +0,013 | +0,180 → +0,054 | baisse dans les deux bras |
| Connaissances | +0,091 → +0,112 | +0,233 → +0,133 | hausse chez les témoins, baisse chez les intervention |
| Enfant vacciné déclaré | +0,138 → −0,005 | +0,309 → +0,158 | baisse dans les deux bras |
| Carnet vu | +0,035 → −0,058 | +0,255 → +0,075 | baisse dans les deux bras |
| Amène les enfants à la pesée | +0,170 → +0,066 | +0,348 → +0,269 | baisse dans les deux bras |
| Accouchement en structure | +0,163 → +0,191 | +0,207 → +0,145 | hausse chez les témoins, baisse chez les intervention |

Onze des douze séries diminuent, dans les deux bras, avec des amplitudes comparables. La lecture honnête est celle d'une **réduction générale de l'inégalité entre les deux passages, commune aux zones d'intervention et aux zones témoins** — donc non attribuable au programme. Le seul indicateur où le bras intervention se distingue nettement est l'exposition aux agents (−0,126 contre −0,094), mais l'écart entre les deux bras est inférieur à la largeur des intervalles.

> **REC-026 — Réécrire le chapitre 8 : pas de gradient, pas d'effet sur l'équité** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-026 |
| 2. Constat | 23 séries de quintiles sur 32 ne sont pas monotones (jusqu'à 20,9 points de rupture) ; 12 indices d'Erreygers sur 24 ont un IC contenant zéro ; 11 des 12 séries évoluent dans le même sens dans les deux bras. |
| 3. Preuve | `T37_gradient_quintiles` (160 lignes → 32 séries) ; `T36_concentration_erreygers` (24 lignes) ; figure 14 et tableau 32. |
| 4. Axe | 2 — définition ; axe 5 |
| 5. Criticité | Bloquant |
| 6. Cause probable | Titre de figure choisi avant lecture des séries ; chapitre non rédigé. |
| 7. Effet | Le rapport s'apprête à affirmer un gradient social et un effet du programme sur l'équité que les données ne soutiennent pas. |
| 8. Recommandation | Renommer la figure 14 ; publier les séries avec leurs intervalles et le n par quintile ; conclure, au chapitre 8, à une réduction générale de l'inégalité commune aux deux bras et à l'absence d'effet différentiel démontrable ; signaler explicitement les 12 indices dont l'IC contient zéro. |
| 9. Modalité | Auteur ; rédaction du chapitre 8 à partir des deux onglets. |
| 10. Livrable | Chapitre 8 rédigé + figure 14 renommée et complétée. |
| 11. Effort | 2 jours-personne. |
| 12. Dépendance | REC-012 (figure 14), REC-017 (rédaction). |
| 13. Clôture | 0 emploi du mot « gradient » sans mention de la non-monotonie ; les 12 IC contenant zéro sont signalés. |
| 14. Statut | Ouvert. |

## H.5 Un constat qui n'en est pas un : les effectifs du tableau 31

La partie B signalait un écart d'effectifs entre le rapport et le classeur pour le tableau 31 (hétérogénéité) : 1 900 et 3 091 dans le rapport, 2 285 et 3 428 dans le classeur. La vérification des sommes explique l'écart et **le retire du passif**.

| Sous-groupe | n — rapport | n — classeur |
|---|---:|---:|
| Niveau de vie : quintiles 1-2 | 1 900 | 2 285 |
| Niveau de vie : quintiles 3-5 | 3 091 | 3 428 |
| **Somme** | **4 991** | **5 713** |

La somme des effectifs du rapport vaut exactement 4 991, l'échantillon d'analyse du tableau 20 ; celle du classeur vaut exactement 5 713, l'ensemble des observations des deux passages. Les deux sont justes, mais ils ne comptent pas la même population. Le rapport est donc cohérent avec lui-même ; c'est l'onglet qui calcule ses effectifs sur la base complète. La correction n'est pas de changer les chiffres, mais de nommer la base dans la note du tableau — ce qui rejoint REC-008 (distinguer base, enquêtés, analysés) et doit être ajouté à sa clôture.

## H.6 Un défaut de forme confirmé : les libellés de catégories du tableau 9

L'onglet `T16_categories_organes` emploie deux genres pour les mêmes catégories : « Non fonctionnel / Partiellement fonctionnel / Fonctionnel » pour les CODESA, « Non fonctionnelle / Partiellement fonctionnelle / Fonctionnelle » pour les CAC. Le tableau 9 du rapport reprend les deux séries telles quelles. Ce n'est pas une erreur de fond, mais dans un tableau qui compte 24 lignes et dont la lecture repose entièrement sur la comparaison des catégories, deux orthographes pour une même catégorie suffisent à faire douter de l'homogénéité du codage. À corriger lors de la passe de normalisation des libellés (REC-007).

## H.7 Ce que la troisième passe change au décompte

| Élément | Effet |
|---|---|
| Écarts chiffrés | 33 → **35** (deux constats nouveaux : grille de progression, écarts de zone localisés) |
| Griefs retirés | **2** (effectifs du tableau 31 ; 38 cellules de zone expliquées par un changement de méthode et non par une erreur) |
| Constats nouveaux | 6 (localisation de la divergence de zone ; réconciliation exacte des tableaux 11, 12 et 4 ; grille de progression ; non-monotonie du gradient ; indices d'Erreygers ; libellés de catégories) |
| Recommandations | 22 → **25** |
| Charge chiffrée hors rédaction | 29 → **32,5 jours-personne** |

**Le verdict de fond ne change pas** : le rapport n'est pas diffusable en l'état. Mais la nature du travail restant se précise. Sur les six conditions posées en partie F, trois sont désormais documentées au point de devenir des tâches d'écriture plutôt que des enquêtes : l'ajustement des zones (une note de trois lignes), la grille de progression (une note de cinq lignes), la réconciliation des effectifs (une mention de base de calcul). Le dossier n'est plus dans une phase de diagnostic : il est dans une phase de correction, et la liste des corrections est close pour l'essentiel.

Deux points restent ouverts et ne peuvent pas être clos par l'audit : la **reproductibilité** (les scripts ne sont pas livrés, REC-014) et la **rédaction** (douze chapitres sans texte, REC-017). Ce sont les deux seules conditions qui exigent un travail de fond, et ce sont elles qui déterminent la date de diffusion.
