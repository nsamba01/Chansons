# Audit indépendant du rapport de résultats quantitatifs

## Programme SACO — Phase 2, riposte Mpox en République démocratique du Congo

**Rapport audité :** `Rapport_resultats_quantitatifs_Phase2_SACO_Mpox_maquette_2026-10-19 (1).docx` — 7 470 917 octets — empreinte SHA-256 (24 premiers caractères) `31c0f40739baa5d84626016a`.

**Source de données auditée :** `SACO_Phase2_Tableaux_2026-10-15 (2).xlsx` — 546 861 octets — empreinte SHA-256 `3ee1133d013fbd07b7373832`.

**Date de l'audit :** 20 octobre 2026. **Version :** seconde passe (partie G ajoutée).

**Nature du livrable audité :** maquette de rapport (le titre du fichier porte « maquette » et la date du 19 octobre 2026), accompagnée du classeur de sorties du 15 octobre 2026. L'audit porte donc sur un état de production intermédiaire : il ne juge pas une version diffusable, il mesure ce qui reste à faire pour qu'elle le devienne.

---

## Sommaire

- Avertissement de lecture
- 1. Synthèse de l'audit (onze constats, ce qui n'est pas mis en cause, six décisions, chiffres clés)
- 2. Méthode d'audit (sept étapes, conventions, limites)
- **Partie A** — Inventaire, architecture documentaire et complétude
- **Partie B** — Réconciliation numérique entre la maquette et le classeur
- **Partie C** — Décision par onglet : ce qui entre dans le rapport, ce qui reste en annexe
- **Partie D** — Cohérence scientifique interne
- **Partie E** — Appareil graphique et fiches de zone
- **Partie F** — Traçabilité, reproductibilité et plan de correction
- **Partie G** — Seconde passe de contrôles : ce que la reprise a établi
- Annexes de l'audit (artefacts, convention des blocs, récapitulatif des recommandations, empreintes)

---

## Avertissement de lecture

Trois conséquences découlent de la nature du livrable, et elles commandent l'interprétation de tout ce qui suit.

**Première conséquence — l'argumentation n'existe pas encore.** Douze chapitres sur treize ne contiennent, en lieu et place du texte, qu'un encadré « À rédiger — contenu attendu » qui décrit ce qu'il faudra écrire. L'ensemble des paragraphes rédigés représente environ 5 175 mots pour treize chapitres et sept annexes, soit moins de 400 mots par chapitre, essentiellement des notes de lecture de tableaux et des définitions de méthode. Aucun paragraphe de discussion, aucune interprétation causale, aucune recommandation n'est rédigé : l'annexe A « Note de correction des valeurs de T0 » et l'annexe F « Listes de contrôle » ne contiennent que le mot « à rédiger ».

**Deuxième conséquence — l'audit ne peut porter que sur l'infrastructure probante.** Il est impossible de contester un raisonnement qui n'est pas écrit, ni de vérifier si une conclusion excède ses données. Ce qui est vérifiable, en revanche, est considérable : la cohérence des 60 tableaux et des 20 figures avec les 77 sorties du classeur, la définition des indicateurs, les effectifs, l'inférence, les encodages graphiques, la traçabilité. C'est l'objet des parties A à F. Chaque constat est daté, localisé et chiffré ; aucun ne repose sur une impression de lecture.

**Troisième conséquence — les défauts relevés ne sont pas des erreurs de plume.** Ils sont de nature industrielle : deux passages d'estimation différents alimentent le même rapport, la numérotation des sorties ne permet aucun rapprochement automatique, les légendes ne sont pas liées aux objets qu'elles décrivent, une figure est vide, deux titres sont coupés par le cadre. Ces défauts se reproduiront à chaque nouvelle version si la chaîne de production n'est pas corrigée. C'est pourquoi le plan de correction de la partie F traite la chaîne avant les tableaux.

---

## 1. Synthèse de l'audit

### 1.1 Les onze constats majeurs

| N° | Constat | Criticité | Partie |
|---|---|---|---|
| 1 | Le rapport est une maquette : douze encadrés « À rédiger », annexes A et F vides, seize fiches de zone sans contexte qualitatif. Aucune interprétation n'est vérifiable. | Bloquant | A.4 |
| 2 | Deux jeux d'estimations coexistent. Le tableau 20 et les figures 1 et 7 donnent 2,9 ; −3,6 ; 0,1 ; −3,2 pour les quatre primaires ; le classeur (T25) donne 3,1 [−4,2 ; 10,5] ; −3,1 ; 0,1 ; −3,2 pour le modèle à effets fixes et 1,9 ; −1,9 ; 0,3 ; −2,4 pour la DiD à 16 points. Aucune colonne du classeur ne reproduit les quatre valeurs du rapport. | Bloquant | B.2 |
| 3 | La réconciliation numérique n'est ni faite ni documentée : trente-trois écarts chiffrés sont établis, dont des intervalles de confiance systématiquement plus étroits dans quatre tableaux « trois volets », et des colonnes « évolution ajustée » qui ne se reproduisent pas (10 zones sur 16 au tableau 21, 9 sur 16 au tableau 54). | Bloquant | B.3–B.5 |
| 4 | Les totaux du résumé exécutif sont des observations et non des unités : « 5 713 ménages » = 2 857 + 2 856, « 1 148 RECO » = 576 + 572. Le lecteur comprend un effectif de personnes là où le rapport compte des passages. | Majeur | D.2 |
| 5 | Aucune correspondance entre les sorties du classeur et les tableaux du rapport : le classeur numérote T01 à T55 (T24 absent), le rapport numérote 1 à 60 ; deux tableaux du rapport (58 et 60) n'ont aucun onglet source. | Bloquant | A.3 |
| 6 | Les codes du catalogue ne sont pas les noms des onglets (`T19_P1` contre `T19_16_zones_P1`, `T53_P1` contre `T53_sensibilite_P1`) : le rapprochement ne peut pas être automatisé, et un onglet n'est pas catalogué. | Majeur | A.2 |
| 7 | Le document contient 126 objets tabulaires : 49 encadrés d'une seule cellule (dont les douze consignes « À rédiger », seize en-têtes de fiche et seize encadrés « Contexte ») et 77 tableaux de données pour 60 légendes numérotées. Les seize tableaux des fiches de zone n'ont aucune légende et ne peuvent donc pas être cités ; le tableau 45 est en deux fragments. | Majeur | A.4 |
| 8 | L'appareil graphique comporte des défauts certains : figure 15 vide (axes tracés, aucune donnée), quatre titres tronqués par le bord du canevas (figures 2, 5, 7 et 8), une note de figure annonçant des intervalles de confiance non tracés (figure 17), une légende désignant un estimateur autre que celui tracé (figure 1), et une figure 7 dont le titre (« les pentes sont parallèles ») est contredit par ses propres valeurs (+7,0 points dans le bras intervention contre +3,9 dans le bras témoin pour P1). | Bloquant | E.2 |
| 9 | Deux définitions cohabitent pour un même indicateur : « carnet vu » tous ménages ou parmi les vaccinés, « connaissances » ou « connaissances déclarées (citations) », indice D3 à cinq ou six composantes, poids d'indice 0,218 ou 0,177. | Bloquant | D.1 |
| 10 | L'inférence est correctement bornée (16 grappes, CR2, Satterthwaite, Holm à 1,000) mais l'appareil de décision — grille des cas A à E, seuils de 5, 11, 8 et 0,25 point, EMD — n'est défini qu'en note de figure, jamais rappelé là où il sert, et l'EMD dépasse le seuil pour trois des quatre indicateurs primaires, ce qui interdit toute conclusion de pertinence. La grille ne se reproduit pas : la lettre de P2 diffère entre le rapport et le classeur, quatre EMD sur neuf diffèrent de 20 à 80 %, et aucune règle unique ne restitue les neuf lettres. | Majeur | D.3, G.4 |
| 11 | Deux indicateurs primaires sur quatre sont déséquilibrés à l'inclusion bien au-delà de la bande de ± 0,10 de la figure 4 (P3 : 0,376 ; P4 : 0,275), et deux covariables également (instruction : 0,35 ; taille du ménage : −0,32) ; le déséquilibre de P3 s'aggrave à T1 (0,431) par réduction de variance. Ni la figure 4 ni le texte ne le signalent. | Majeur | D.5 |

### 1.2 Ce que l'audit ne met pas en cause

Il faut le dire avec la même netteté, sous peine de rendre l'audit inutilisable. Le dispositif est, sur plusieurs points, d'un niveau méthodologique supérieur à ce que ce type d'enquête produit habituellement.

Le devis est correctement décrit : seize zones de santé, huit par bras, deux passages, appariement territorial documenté, et le rapport énonce lui-même, au § 11.1, les écarts au protocole (passage de R à un autre environnement de calcul, affectation programmatique des zones, absence de panel individuel, absence de pondération en deçà du niveau provincial). Les indicateurs primaires ont été choisis **avant** la lecture des effets et l'EMD est recalculée après observation, ce qui est la bonne séquence. L'inférence à seize grappes est traitée pour ce qu'elle est : les degrés de liberté de Satterthwaite descendent à 10,8–11, les p ajustées Holm valent 1,000 pour les quatre primaires, et le rapport ne revendique aucun effet. La correction de Benjamini-Hochberg est appliquée aux indicateurs secondaires, et aucun ne survit (p ajustée minimale 0,607) — le rapport le dit. Le dossier de plausibilité des tendances parallèles est présent (placebos, divergence ± 2 et ± 5 points, retrait d'une zone à tour de rôle, courbes de spécification).

Autrement dit : le problème n'est pas la science, c'est la chaîne de production et l'absence de rédaction. Cette distinction est le fil directeur des recommandations.

### 1.3 Les six décisions qui conditionnent la diffusion

1. **Recalculer les quatre primaires sur une base unique** et déclarer une seule estimation principale — le modèle conjoint à effets fixes d'aire tel que défini au § 1.4 —, en publiant la DiD à 16 points comme complément et non comme colonne concurrente. Tant que deux jeux de valeurs circulent, aucune phrase du rapport ne peut être validée.
2. **Écrire la note de l'annexe A** avant toute autre rédaction : elle doit expliquer chaque valeur de T0 modifiée entre le classeur et le rapport (Kibombo P2 : 20,4 au classeur, 23,7 dans la fiche et au tableau 54 ; Tunda P2 : 14,4 contre 15,0).
3. **Établir la table de correspondance sortie → tableau** et l'insérer dans l'annexe G, avec le nom exact de l'onglet. C'est la condition de l'auditabilité par un tiers.
4. **Reconstruire la figure 15** à partir du tableau 34 et du tableau 56, et supprimer les figures en doublon.
5. **Décider du format de chaque sortie** : 78 onglets ne peuvent pas devenir 60 tableaux. La partie C tranche, onglet par onglet, entre corps du rapport (A), simplification (B), figure (C), tableau de synthèse (D) et annexe (E).
6. **Publier la table de décision de la grille des cas** et l'appliquer par script (REC-022) : c'est l'appareil qui fonde chaque conclusion de pertinence, et il n'est aujourd'hui ni reproductible ni cohérent d'un document à l'autre.
7. **Corriger le vocabulaire des effectifs** : parler d'observations quand il s'agit de passages, d'unités quand il s'agit de personnes ou d'établissements, et donner systématiquement le n par passage.

### 1.4 Chiffres clés de l'inventaire

| Objet | Mesure |
|---|---|
| Onglets du classeur | 78 (1 catalogue + 77 sorties) |
| Entrées du catalogue | 92 (71 « tableau », 20 « figure », 1 « fiche ») |
| Onglets avec code T | 77, numérotés T01 à T55, **T24 absent**, quatre numéros éclatés en 21 sous-codes |
| Paragraphes du rapport | 342 (263 non vides), dont 80 légendes |
| Objets tabulaires | 126, dont 49 encadrés d'une cellule et 77 tableaux de données |
| Figures légendées | 20, portées par 24 images de graphique distinctes |
| Tableaux légendés | 60 légendes pour 77 tableaux de données |
| Images PNG embarquées | 44, dont 4 non référencées par une légende |
| Encadrés « À rédiger » | 12 (un par chapitre sans texte) |
| Fiches de zone | 16, de 22 indicateurs chacune |
| Prose rédigée | ≈ 5 175 mots pour 13 chapitres et 7 annexes |
| Écarts chiffrés documentés | 33, dont 31 engageant la reproductibilité |

---

## 2. Méthode d'audit

### 2.1 Les sept étapes

L'audit a été conduit en sept étapes séquentielles, chacune produisant un artefact vérifiable.

**Étape 1 — Inventaire et dénombrement.** Ouverture des deux fichiers au niveau du format (archive OOXML), extraction de la liste des onglets, de leurs dimensions réelles, de leurs en-têtes et de leurs effectifs de lignes ; extraction de la liste ordonnée des paragraphes, des objets tabulaires et des images du document Word, avec leur position dans le flux. Cette étape a produit la matière brute des parties A et C.

**Étape 2 — Cartographie des sorties et des légendes.** Rapprochement de chaque légende « Tableau N » et « Figure N » avec l'objet qu'elle précède ou qu'elle suit dans le flux XML, puis avec l'onglet du classeur qui porte la même sémantique. Cette étape a révélé que 126 objets tabulaires se partagent 60 légendes et que la numérotation du classeur est indépendante de celle du rapport.

**Étape 3 — Réconciliation numérique.** Comparaison, pour 61 appariements possibles, des valeurs ponctuelles et des intervalles, après normalisation des décimales (virgule décimale, espaces insécables, signe moins typographique) et alignement des lignes sur les libellés. Chaque divergence retenue a été relue manuellement dans les deux fichiers avant d'être inscrite : les divergences issues d'un simple décalage d'alignement — notamment dans les tableaux Word fragmentés — ont été écartées. Les résultats figurent en partie B et dans `audit/reconciliation.csv`.

**Étape 4 — Contrôle de cohérence interne.** Vérification des identités arithmétiques que le rapport doit respecter : sommes des effectifs par zone égales aux totaux annoncés ; évolution égale à T1 − T0 ; écart à la moyenne provinciale égal à l'évolution ajustée moins la moyenne de province ; cohérence des dénominateurs entre indicateurs ; cohérence des pondérations et des poids d'indice entre le corps du rapport et les annexes.

**Étape 5 — Audit des productions graphiques.** Pour chacune des 44 images : dimensions, densité d'encre hors bandeau de titre, test de débordement du dessin sur les bords gauche et droit du canevas, corrélation deux à deux des images en niveaux de gris pour détecter les doublons, puis lecture visuelle des figures litigieuses. Les résultats figurent dans `audit/figures.csv` et en partie E.

**Étape 6 — Audit des fiches de zone.** Comparaison des 16 fiches (22 indicateurs chacune, soit 352 cellules) avec les onglets `T19_16_zones_P1` à `P4`, colonne par colonne, et contrôle de la structure de référence proposée au lecteur.

**Étape 7 — Revue de robustesse et de reproductibilité.** Lecture des matrices de sensibilité, des placebos, des courbes de spécification et des analyses de variance ; vérification que la ligne « estimation principale » de chaque matrice correspond bien à l'estimation déclarée principale dans le corps du rapport ; examen du catalogue et des annexes au regard de leur fonction de traçabilité.

**Étape 8 — Seconde passe de vérification.** Les constats de la première passe ont été repris un par un, avec trois objets : vérifier les affirmations qui reposaient sur une lecture unique, chercher ce qui n'avait pas été regardé (colonne `n` du tableau 60, lignes de synthèse du tableau 57, identité de la cascade maternelle, lettres de cas), et retirer les soupçons non confirmés. Cette passe a ajouté cinq constats, corrigé deux affirmations et retiré un grief ; elle fait l'objet de la partie G. Elle a aussi nécessité de reconstruire l'accès au classeur, celui-ci ne s'ouvrant pas avec une bibliothèque standard (voir REC-014).

### 2.2 Conventions de comparaison

**Unités.** Les indicateurs de type indice sont exprimés sur une échelle 0–100 et les écarts en **points de pourcentage** de cette échelle, notés « pts ». Les indices de domaine sont exprimés en **écarts-types** de la référence témoin à T0, notés « écart-type ». Aucune confusion entre points de pourcentage et pourcentage relatif n'est admise dans les recommandations : un passage de 30,3 % à 38,9 % est une hausse de 8,6 pts, soit +28,4 % en relatif, et les deux formulations ne sont jamais interchangeables.

**Tolérance.** Une valeur est déclarée divergente lorsque l'écart excède 0,05 dans l'unité de la colonne, ce qui couvre l'arrondi d'affichage à une décimale mais exclut les écarts d'arrondi de second ordre (0,01 à 0,02), lesquels sont signalés séparément comme « dérive d'arrondi » sans être portés au passif.

**Progression.** La règle de progression est celle du rapport : une unité progresse si son évolution atteint au moins un critère, soit 11,1 pts pour les CAC (9 critères) et 14,3 pts pour les CODESA (7 critères). L'audit a vérifié que cette règle est appliquée avec le pas de chaque organe, et non avec un pas unique.

**Criticité.** Trois niveaux seulement. *Bloquant* : le défaut empêche la validation du document par un tiers ou contredit une valeur publiée. *Majeur* : le défaut altère la lecture ou la traçabilité sans invalider le résultat. *Mineur* : le défaut de forme, à corriger en passe finale.

### 2.3 Limites de l'audit

Quatre limites doivent être explicitées.

**L'audit ne remonte pas aux données individuelles.** Aucune base de microdonnées n'était disponible. L'audit vérifie la cohérence entre le classeur de sorties et le rapport, non la validité des calculs qui ont produit le classeur. Un écart entre le classeur et les données brutes resterait invisible. C'est une raison supplémentaire, et non accessoire, d'exiger que les scripts soient joints et exécutables.

**L'audit ne vérifie pas la conformité au protocole.** Le protocole d'enquête n'était pas fourni. Les écarts assumés au protocole sont donc pris tels que le § 11.1 les déclare, sans vérification indépendante.

**L'audit ne porte pas sur le volet qualitatif.** Les encadrés « Contexte (volet qualitatif) » des fiches de zone renvoient à une source non fournie ; ils ont été constatés vides, non jugés.

**Le dénombrement des divergences est un dénombrement de cas établis, non une estimation d'exhaustivité.** Trente-trois écarts chiffrés sont documentés dans les parties B (tableau B.3) et G (tableau G.6). Ils sont certains. Ils ne prétendent pas couvrir toutes les cellules des 61 appariements : la fragmentation des objets Word (jusqu'à 17 objets sous une même légende) rend une comparaison automatique intégrale non fiable, et l'audit a préféré publier peu de cas certains plutôt qu'un compte global qu'il n'aurait pas pu défendre ligne à ligne. Ce choix est lui-même un constat : un rapport dont les tableaux ne peuvent pas être comparés automatiquement n'est pas auditable en routine.
---

# PARTIE A — Inventaire, architecture documentaire et complétude

*Axes 1 (conformité au devis), 8 (traçabilité) et 9 (complétude).*

## A.1 Le classeur : 78 onglets pour 71 codes

Le classeur `SACO_Phase2_Tableaux_2026-10-15 (2).xlsx` contient 78 onglets : un onglet `Catalogue` et 77 onglets de sorties.

Le catalogue recense 92 entrées : 71 « tableau », 20 « figure » et 1 « fiche ». Il porte, pour chaque entrée, un code, un type, un titre, le script producteur, le registre, la population et une note. C'est un bon instrument, et il est renseigné de façon homogène.

Mais il ne décrit pas le classeur, et c'est le premier défaut structurel.

**71 codes pour 77 onglets.** Quatre numéros sont éclatés en sous-codes : T14 (cinq sous-codes : `T14_men`, `T14_cac`, `T14_cod`, `T14_reco`, `T14_asc`), T15 (cinq sous-codes), T19 (quatre : `T19_P1` à `T19_P4`), T53 (sept : `T53_P1` à `P53_P4` et `T53_D1` à `T53_D3`). Ces 21 sous-codes occupent 21 onglets. Restent 50 numéros simples, occupés par 56 onglets : l'écart de six s'explique par des onglets supplémentaires non catalogués et par des versions longues.

**T24 manque.** La numérotation va de T01 à T55 sans interruption sauf T24, absent du catalogue comme du classeur. Cette lacune n'est signalée nulle part et suggère une sortie supprimée sans trace.

**Le catalogue s'arrête à T55, le rapport va jusqu'à 60.** Les deux numérotations sont indépendantes : `T39_continuum_maternel` est publié comme tableau 56, `T45_mpox_cap` comme tableau 57. Aucune table de correspondance n'est fournie, ni dans le classeur, ni dans l'annexe G (« Catalogue des sorties ») du rapport qui se contente de reproduire les codes du classeur. Un lecteur ne peut donc pas savoir quel onglet produit quel tableau, et un auditeur ne peut pas reconstituer un tableau à partir de sa source.

**Les codes ne sont pas les noms d'onglets.** Le catalogue déclare `T19_P1` ; l'onglet s'appelle `T19_16_zones_P1`. Le catalogue déclare `T53_P1` ; l'onglet s'appelle `T53_sensibilite_P1`. Douze onglets sont dans ce cas. Le rapprochement ne peut pas être automatisé par jointure sur le code, ce qui prive le catalogue de sa fonction principale. Un onglet — `T19_16_zones_complet` — n'a aucun code au catalogue.

**Deux tableaux du rapport n'ont aucune source dans le classeur.** Le tableau 58 (« UCODESA : fonctions et pièces déclarées », 53 lignes, 5 colonnes) et le tableau 60 (« Repondération de T1 : taille effective de Kish et étendue des poids ») ne correspondent à aucun onglet : aucune cellule du classeur ne contient les valeurs de Kish, et l'onglet `T23_repondération_T1` ne porte que les évolutions brutes et repondérées. Ces deux tableaux sont donc invérifiables dans le classeur — avec une nuance pour le second : sa colonne d'effectifs se reproduit exactement à partir du tableau 3 (voir G.1), seules les colonnes de poids échappent à la vérification.

> **REC-001 — Rétablir une correspondance unique entre sorties et tableaux** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-001 |
| 2. Constat | 77 onglets, 71 codes, 60 tableaux : trois numérotations sans table de correspondance ; 12 onglets dont le nom diffère du code ; 1 onglet hors catalogue ; 2 tableaux sans onglet source. |
| 3. Preuve | `Catalogue` colonnes A–G ; onglets `T19_16_zones_P1`, `T53_sensibilite_P1` ; rapport tableaux 58 et 60 ; aucune occurrence de « Kish » dans les 78 onglets. |
| 4. Axe | 8 — traçabilité |
| 5. Criticité | Bloquant |
| 6. Cause probable | Le catalogue est un inventaire de scripts, non une table de publication ; les renommages d'onglets n'ont pas été répercutés. |
| 7. Effet | Aucun tableau du rapport ne peut être rejoué ni vérifié par un tiers ; l'annexe G est décorative. |
| 8. Recommandation | Ajouter au catalogue trois colonnes obligatoires : `n_tableau_rapport`, `nom_onglet`, `version_classeur` ; renseigner les 60 lignes ; déclarer explicitement les deux tableaux sans source et les produire ou les retirer. |
| 9. Modalité | Producteur des sorties ; une passe de saisie, contrôle par l'auditeur sur les 60 lignes. |
| 10. Livrable | Catalogue v2 avec 60 lignes renseignées, exporté en annexe G du rapport. |
| 11. Effort | 2 jours-personne. |
| 12. Dépendance | REC-002 (nommage) doit être traité dans la même passe. |
| 13. Clôture | 60/60 tableaux du rapport reliés à un onglet existant ; 0 onglet hors catalogue ; jointure automatique possible sur `nom_onglet`. |
| 14. Statut | Ouvert — non instruit à la date de l'audit. |

> **REC-002 — Normaliser le nommage des onglets et supprimer T24 sans laisser de trou** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-002 |
| 2. Constat | Douze onglets portent un nom différent de leur code ; T24 est absent sans mention. |
| 3. Preuve | `Catalogue` A ; noms d'onglets, feuille 1 du classeur. |
| 4. Axe | 8 — traçabilité |
| 5. Criticité | Majeur |
| 6. Cause probable | Renommage tardif des onglets lors d'une réorganisation des sorties. |
| 7. Effet | Toute jointure sur le code échoue silencieusement ; un script de contrôle produirait des faux négatifs. |
| 8. Recommandation | Aligner le code du catalogue sur le nom d'onglet (ou l'inverse), et documenter l'absence de T24 par une ligne « supprimé, motif, date, remplacé par ». |
| 9. Modalité | Producteur ; renommage en une passe, avec vérification que les scripts pointent toujours le bon onglet. |
| 10. Livrable | Classeur v2 + note de version. |
| 11. Effort | 0,5 jour-personne. |
| 12. Dépendance | Aucune. |
| 13. Clôture | 0 divergence code/onglet ; T24 documenté. |
| 14. Statut | Ouvert. |

## A.2 Le rapport : 342 paragraphes, 126 objets tabulaires, 44 images

Le document compte 13 chapitres, 7 annexes (A à G) et 16 fiches de zone. Sa structure éditoriale est solide : résumé exécutif, méthodologie en six sections, profil des échantillons, trois chapitres de résultats par acteur (gouvernance, acteurs communautaires, ménages), un chapitre d'effet, un chapitre de mécanismes, un chapitre d'équité, un chapitre thématique en quatre sections, un chapitre d'alignement avec la stratégie nationale, un chapitre de robustesse et de limites, une synthèse par dynamique, une discussion et des recommandations.

Cette architecture appelle deux observations.

**Elle est complète et bien ordonnée.** L'ordre suit la logique attendue d'un rapport d'évaluation : méthode, comparabilité, résultats descriptifs, effet, mécanismes, équité, thèmes, alignement programmatique, robustesse, synthèse. La place de la robustesse avant la synthèse est un bon choix, souvent inversé dans les rapports d'enquête.

**Elle est vide.** Douze encadrés « À rédiger — contenu attendu » occupent la place du texte dans les chapitres 1 à 13. Ces encadrés sont des cellules de tableau, ce qui explique qu'ils n'apparaissent pas dans le décompte des paragraphes. Ils décrivent avec précision ce qu'il faudra écrire (« Trois messages pour le résumé », « Décrire la réalisation par zone, le déficit d'ASC à T1 ») — ce qui est une bonne pratique de maquette, mais qui interdit toute évaluation du raisonnement.

**126 objets tabulaires, dont 49 encadrés d'une cellule.** Le décompte exact est le suivant : 49 objets sont des tableaux d'une seule cellule, utilisés comme conteneurs de texte — c'est le cas des douze consignes « À rédiger », des seize en-têtes de fiche (« Province : Maniema · Bras : intervention »), des seize encadrés « Contexte (volet qualitatif) » et d'un encadré d'usage en tête de document. Les 77 autres sont de vrais tableaux de données.

**77 tableaux de données pour 60 légendes numérotées.** L'écart de dix-sept s'explique par deux causes distinctes :

| Cause | Écart | Observation |
|---|---:|---|
| Tableaux des fiches de zone | +16 | Aucune légende « Tableau », aucune numérotation : ils ne peuvent pas être cités par renvoi |
| Tableau 45 (sensibilité P4) | +1 | Deux fragments sous une même légende |
| **Total** | **+17** | 60 légendes, 77 tableaux de données |

Le point important n'est pas le fragment du tableau 45, qui se corrige en une passe. C'est que **les seize tableaux de fiche, soit 368 lignes, échappent à la numérotation du rapport**. Un lecteur ne peut pas écrire « voir le tableau de la fiche de Kibombo » ; un auditeur ne peut pas les citer ; un correcteur ne peut pas les suivre. Ils existent visuellement et n'existent pas documentairement.

**Le recours massif aux encadrés d'une cellule est un défaut de structure, non de style.** Tout le texte de consigne du document — les douze « À rédiger » — se trouve dans des tableaux d'une cellule. Conséquence immédiate : une extraction du texte par paragraphe ne le voit pas. L'audit l'a constaté à ses dépens, en cherchant d'abord les consignes dans les paragraphes et en n'en trouvant aucune. Conséquence plus grave : ces consignes sont invisibles pour un lecteur d'écran, pour un moteur d'indexation et pour tout contrôle automatique de complétude. Les encadrés doivent devenir des paragraphes avec un style dédié.

## A.3 Les figures : 20 légendes, 24 images de graphique, 44 fichiers

Le dossier `word/media/` contient 44 fichiers PNG. Leur nature est hétérogène :

- **24 images de graphique** (largeur 1 889 à 2 191 px, densité d'encre modérée), qui portent effectivement les figures ;
- **15 barres de titre décoratives** de 2 079 × 284 px, densité d'encre ≈ 0,97, bandeaux de chapitre répétés et non figures ;
- **1 image de couverture** (1 819 × 2 573 px) ;
- **4 fichiers non référencés** par un appel du document : une barre de titre supplémentaire, un filet de séparation de 2 000 × 16 px et deux images inutilisées.

Le total est de 44 fichiers, dont 40 référencés.

Les 20 légendes « Figure » sont numérotées sans trou ni doublon, ce qui est un point positif. Mais plusieurs figures sont des assemblages de plusieurs PNG : la figure 3 est portée par un bloc de sept images (dont des panneaux de légende), la figure 1 par deux images de graphique distinctes. Un assemblage n'est pas un défaut en soi ; il en devient un quand aucune des images composantes ne porte de titre propre, car le contrôle visuel devient impossible sans reconstituer l'ordre.

## A.4 Complétude : ce qui manque au document

| Zone du document | État | Conséquence |
|---|---|---|
| Résumé exécutif | Encadré « À rédiger — une page, après validation des effets » ; 4 sous-titres de résultats confirmatoires présents, texte absent | Aucune conclusion vérifiable |
| Chapitres 1 à 11 | Encadrés « À rédiger — contenu attendu » (sauf § 1.1 à 1.6 et § 11.1, rédigés) | Seule la méthode est écrite |
| Chapitre 12 (synthèse par dynamique) | Encadré | — |
| Chapitre 13.1 (discussion), 13.2 (recommandations) | Encadrés | Aucune recommandation pour le commanditaire |
| Annexe A (note de correction des valeurs de T0) | « à rédiger » | **Les corrections de T0 sont visibles mais non expliquées** (voir B.5) |
| Annexe B (indicateurs, indices, EMD) | Tableaux 46 à 49 présents | Complet sur le fond |
| Annexe C (qualité des données) | Tableaux 50 à 52 présents | Complet |
| Annexe D (tableaux complémentaires) | Tableaux 53 à 57 présents | Complet |
| Annexe E (fiches de zone) | 16 fiches, 22 indicateurs | Voir partie E.3 |
| Annexe F (listes de contrôle) | « à rédiger » | Aucun contrôle de qualité publié |
| Annexe G (catalogue des sorties) | Reprise des codes du classeur | Sans correspondance avec les tableaux |

Le cas de l'annexe A est le plus préoccupant, et il faut le dire sans détour : **le rapport contient des valeurs de T0 corrigées sans la note qui devait les justifier.** Kibombo (P2) passe de 20,4 dans le classeur à 23,7 dans la fiche de zone et au tableau 54 ; Tunda passe de 14,4 à 15,0. Ces deux corrections déplacent les évolutions de 3,3 points et 0,6 point, et la première change le signe de l'évolution ajustée (−4,5 dans le classeur, −6,4 au tableau 54). Une correction de cette nature, dans un rapport qui revendique la traçabilité, ne peut pas rester sans note.

> **REC-003 — Rédiger la note de l'annexe A avant toute autre rédaction** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-003 |
| 2. Constat | Deux valeurs de T0 divergent entre le classeur et le rapport (Kibombo P2 : 20,4 contre 23,7 ; Tunda P2 : 14,4 contre 15,0), et la note qui devait les expliquer est vide. |
| 3. Preuve | `T19_16_zones_P2` colonnes D/H ; fiche de zone Kibombo (ligne « P2 Connaissances ») ; tableau 54 ; annexe A (« à rédiger »). |
| 4. Axe | 3 — réconciliation |
| 5. Criticité | Bloquant |
| 6. Cause probable | Correction des indices de connaissances après recalcul du dénominateur d'items, non répercutée dans l'export du 15 octobre. |
| 7. Effet | Le lecteur ne peut pas savoir quelle valeur fait foi ; l'évolution ajustée de Kibombo change de sens (−4,5 contre −6,4). |
| 8. Recommandation | Décrire, pour chaque valeur modifiée : variable, zone, valeur du 15 octobre, valeur du 19 octobre, cause, nombre de lignes concernées, effet sur les estimations publiées. Si d'autres corrections existent, les lister exhaustivement (comparer les 16 zones × 4 primaires, soit 64 cellules — l'audit en a trouvé exactement 2 divergentes dans les fiches). |
| 9. Modalité | Auteur du rapport, avec le producteur des sorties ; validation par l'auditeur cellule par cellule. |
| 10. Livrable | Annexe A rédigée (1 à 2 pages) + journal des modifications daté. |
| 11. Effort | 1 jour-personne. |
| 12. Dépendance | REC-004 (choix de l'estimation principale) pour la phrase finale sur l'effet. |
| 13. Clôture | 64/64 cellules des fiches justifiées ; 0 valeur modifiée sans mention. |
| 14. Statut | Ouvert. |

> **REC-004 — Réduire les objets tabulaires au nombre de légendes** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-004 |
| 2. Constat | 77 tableaux de données pour 60 légendes ; seize tableaux de fiche sans légende ni numéro ; tableau 45 en deux fragments ; 49 encadrés d'une cellule porteurs d'un texte invisible à l'extraction. |
| 3. Preuve | Décompte des `w:tbl` du corps de document et des paragraphes « Tableau N. » ; 49 tableaux 1 × 1 ; fiches de zone (tableaux de 23 lignes non légendés). |
| 4. Axe | 1 — conformité au devis |
| 5. Criticité | Majeur |
| 6. Cause probable | Génération automatique par province ou par bras sans agrégation. |
| 7. Effet | Le document n'est ni paginable ni indexable ; un tableau ne peut pas être cité de façon univoque. |
| 8. Recommandation | Une légende = un objet. Fusionner les fragments ; à défaut, numéroter 60a, 60b… et titrer chaque fragment. Retirer ou légender l'objet orphelin. |
| 9. Modalité | Mise en forme ; contrôle par extraction automatique du nombre d'objets par légende. |
| 10. Livrable | Rapport v2 avec 60 objets tabulaires. |
| 11. Effort | 2 jours-personne. |
| 12. Dépendance | REC-001. |
| 13. Clôture | 77 tableaux légendés et numérotés ; 0 tableau de données sans légende ; 0 encadré d'une cellule. |
| 14. Statut | Ouvert. |
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
| 24 | Tableau 31, effectifs | 1 900 / 3 091 | 2 285 / 3 428 (T35) | 385 / 337 | **Effectifs divergents** |
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
---

# PARTIE C — Décision par onglet : ce qui entre dans le rapport, ce qui reste en annexe

*Axe 2 — définition et stabilité des indicateurs ; axe 6 — lisibilité. Cette partie répond à une question que le classeur laisse ouverte : 77 sorties ne peuvent pas devenir 60 tableaux, et 60 tableaux ne peuvent pas être lus.*

## C.1 La règle de décision

Cinq décisions seulement, appliquées à chaque onglet.

| Code | Décision | Signification |
|---|---|---|
| **A** | Conserver | L'onglet devient un tableau du corps, tel quel ou après correction d'une valeur. Format court, message unique, lisible en une page. |
| **B** | Simplifier | Le contenu est nécessaire mais le format ne l'est pas : réduction du nombre de colonnes, transposition lignes/colonnes, sélection des indicateurs prioritaires, renvoi du détail en annexe. |
| **C** | Remplacer par une figure | Le message est un profil, une composition, une comparaison de deux points, une distribution : le tableau ne peut pas le porter. La figure est à produire. |
| **D** | Remplacer par un tableau de synthèse | Le contenu est un diagnostic exhaustif dont seules quelques lignes portent le message ; le corps reçoit une synthèse de 4 à 8 lignes, le détail va en annexe. |
| **E** | Déplacer en annexe | Le contenu est une pièce justificative : il doit rester disponible, il n'a pas à être lu. |
| **H** | Hors rapport | Document de travail, à ne pas publier. |

Trois principes gouvernent l'application.

**Un tableau du corps porte un message, pas une matrice.** Si l'on ne peut pas énoncer en une phrase ce que le tableau démontre, il va en annexe. Ce critère suffit à déplacer 23 onglets.

**Une composition ne se lit pas en lignes.** Dès qu'un tableau décrit une répartition entre catégories (catégories de fonctionnalité, transitions, quintiles, motifs de recours), la figure est la forme correcte et le tableau la forme fautive. Quinze onglets sont dans ce cas, dont le tableau 9 (24 lignes pour une composition en trois catégories) et le tableau 23 (20 lignes pour une sensibilité continue).

**Le corps du rapport doit tenir en 18 à 22 tableaux.** C'est la contrainte de lecture : au-delà, le lecteur cesse de lire et commence à feuilleter. Le corps actuel en compte 60, dont un fragmenté et seize non numérotés, et 96 lignes pour le seul tableau 18.

## C.2 Résultat du tri

| Décision | Nombre d'onglets | Effet |
|---|---:|---|
| A — conserver dans le corps | 15 | 15 tableaux courts |
| B — simplifier | 19 | 19 tableaux ramenés à 6–12 lignes |
| C — remplacer par une figure | 15 | 15 figures à produire (dont 6 se substituent à des figures existantes) |
| D — remplacer par une synthèse | 5 | 5 tableaux de 4 à 8 lignes + 5 pièces en annexe |
| E — déplacer en annexe | 23 | 23 pièces justificatives |
| H — hors rapport | 1 | Catalogue, remplacé par l'annexe G corrigée |

Le corps du rapport passerait ainsi de 60 à **39 tableaux** (15 conservés, 19 simplifiés, 5 synthèses) et 15 figures nouvelles, ce qui reste supérieur à la cible de 22. La réduction complémentaire ne peut venir que d'une décision éditoriale — quel chapitre mérite d'être lu en premier — qui n'appartient pas à l'auditeur. L'audit signale seulement que les chapitres 4 (acteurs) et 10 (alignement PSN) concentrent à eux seuls 11 tableaux dont 6 relèvent de la synthèse.

## C.3 Les cinq décisions les plus lourdes

**Le tableau 60 (repondération, taille de Kish) doit être produit proprement ou retiré.** Il compte 23 lignes, dont 8 de données. Sa colonne `n` se reproduit exactement à partir du tableau 3 (8 lignes sur 8) ; ses deux colonnes de poids et de taille effective ne sont pas recalculables faute de table de poids. Le tableau doit donc être conservé, mais rattaché à un onglet et complété d'une colonne d'effet de plan (REC-020).

**Le tableau 9 (composition des catégories de fonctionnalité) doit devenir une figure.** 24 lignes pour dire que la part d'unités non fonctionnelles a été divisée par deux dans le bras intervention : c'est une composition à trois modalités, donc des barres empilées à 100 %, avec l'effectif en étiquette.

**Le tableau 18 (96 lignes) doit être scindé.** Douze indicateurs prioritaires au corps, en figure appariée (T0–T1 par bras), et les 96 lignes en annexe D. Aucune information n'est perdue ; la lisibilité est multipliée.

**Le tableau 23 (divergence de tendance) doit devenir quatre courbes.** Vingt lignes pour une sensibilité continue à une hypothèse : la figure montre que la conclusion ne bascule qu'entre 2 et 5 points de divergence, ce que le tableau de 20 lignes ne fait pas voir.

**Le tableau 40 (indice de conformité) doit rester dans le corps.** C'est un des rares tableaux qui porte un message clair (la part des normes applicables respectées) avec un format court. Il manque seulement la liste des six normes qui composent l'indice : une note de bas de tableau suffit.

## C.4 Décision, onglet par onglet

La colonne « Tableau du rapport » donne le numéro de la légende sous laquelle la sortie est publiée (ou « — » si elle n'est pas publiée). La colonne « Diagnostic » est le motif de la décision ; elle est rédigée pour être reprise telle quelle dans le journal de correction.

| Onglet | Lignes | Tableau du rapport | Déc. | Diagnostic | Destination |
|---|---:|---|---|---|---|
| `Catalogue` | 92 | — | **H** | Métadonnée de production, non publiable telle quelle ; 71 entrées « tableau », 20 « figure », 1 « fiche » alors que le rapport numérote 60 tableaux et 20 figures. | Annexe G — complétée par la correspondance onglet → tableau du rapport |
| `T01_bilan_appariement` | 7 | Tableau 4 | **B** | 7 lignes utiles, mais deux bases différentes (villages et aires) cohabitent sous le même libellé « ménages » (688 villages, taux 56 %) sans que le mot « villages » apparaisse ; le contraste 56 % / 97,8 % n'est pas expliqué. | Corps, chapitre 2 — tableau 4 conservé et scindé en deux blocs (villages / aires) |
| `T02_realisation_zs` | 17 | Tableau 3 | **B** | 15 colonnes pour 17 lignes ; contient une ligne fantôme (province Kasaï-Oriental, ZS vide, CAC T1 = 1) reprise telle quelle dans le rapport ; colonne UCODESA presque vide (0 ou 1). | Corps, chapitre 2 — 6 colonnes (ménages, RECO, ASC, CAC, CODESA) + ligne fantôme supprimée ; UCODESA en note |
| `T03_asc_couverture` | 4 | Tableau 50 (annexe C) | **D** | Quatre lignes mais un dénominateur absent (48 %, 43 %, 60 %, 26 % de quoi ?) ; baisse de 14 points au Sankuru et de 11 au Maniema non commentée. | Corps, chapitre 2 (3 lignes commentées) + annexe C pour la version détaillée |
| `T04_qualite_manquants` | 58 | Tableau 51 (annexe C) | **E** | 58 lignes de codes de variables (L1, L7, S01Q07…) sans libellé d'indicateur ; les manquants structurels (W2 : 29,8 % / 22,2 %) ne sont pas distingués des manquants réels. | Annexe C — ajout d'une colonne « libellé » et d'une colonne « nature du manquant » |
| `T05_dates_collecte` | 10 | Tableau 2 | **B** | Dates exportées en numéros de série Excel (44828, 46305) : illisibles ; 10 lignes pour 5 bases × 2 passages. | Corps, chapitre 1 — 5 lignes (une par base), dates formatées, colonne « hors fenêtre » conservée |
| `T06_fiches_indicateurs` | 88 | Tableau 46 (annexe B) | **E** | 88 indicateurs, indispensable, mais trois libellés coexistent pour un même indice (P2 : « connaissances » dans le corps, « connaissances déclarées (citations) » dans la maquette) ; les dénominateurs ne figurent pas dans une colonne dédiée. | Annexe B — ajout des colonnes « dénominateur », « unité », « libellé court normalisé » |
| `T07_poids_indices_domaine` | 23 | Tableau 47 (annexe B) | **D** | La composition de D3 diffère entre le classeur (6 composantes, dont recours formel) et le rapport (5 composantes) ; les poids ne sont pas les mêmes (P1 0,177 vs 0,218). | Annexe B — tableau de synthèse 4 lignes (indice, nombre de composantes, poids minimal/maximal) + composition détaillée en annexe |
| `T08_fiabilite_indices` | 8 | Tableau 48 (annexe B) | **B** | 8 lignes, deux populations mélangées (L10 global n = 5713 et L10 par bras/passage n ≈ 1 428). | Annexe B — 4 lignes principales (alpha, oméga) + 4 lignes de contrôle d'invariance |
| `T09_irt_signes_danger` | 18 | Tableau 49 (annexe B) | **E** | Discrimination jusqu'à 3,41 et difficulté jusqu'à 4,51 (item 16) sans commentaire sur les items extrêmes ni sur les items non informatifs. | Annexe B — tri par difficulté, items extrêmes signalés |
| `T10_emd_par_bras` | 23 | Tableau 1 | **C** | 23 lignes × 11 colonnes pour dire qu'aucun effet inférieur à 9-38 points n'est détectable ; deux lignes portent le même libellé (« CODESA : indice de riposte Mpox ») avec des effectifs incompatibles (6 et 36 unités par ZS). | Corps, chapitre 1 — figure « EMD et seuil de pertinence par indicateur » (barres appariées) + tableau 6 lignes |
| `T11_profil_menages` | 21 | Tableau 5 | **B** | Mélange d'unités dans une même colonne : « Milieu urbain (%) » vaut 0,42 / 2,16 (proportions) alors que « Enfant malade (%) » vaut 36,06 (pourcentage) ; âge et DS différents du classeur (30,13 vs 30,11 ; DS 0,18 vs 0,13). | Corps, chapitre 2 — 12 lignes (âge, instruction, taille, quintiles, distance, morbidité) ; religion en annexe |
| `T12_profil_acteurs` | 12 | Tableau 6 | **B** | 12 lignes, colonnes T1 vides pour les CAC (H = 0, F/G absents) : la structure du tableau laisse croire à une absence de mesure alors qu'il s'agit de coupes répétées. | Corps, chapitre 2 — 8 lignes ; cellules vides remplacées par « nd » motivé |
| `T13_equilibre_T0` | 26 | Figure 4 (source) | **C** | Contient le résultat le plus lourd du chapitre 2 : P3 DS = 0,376 et P4 DS = 0,275 à T0, au-delà du seuil de 0,25 que le rapport définit lui-même comme « déséquilibre à ajuster » ; non repris dans le texte ni dans le titre de la figure. | Corps, chapitre 2 — figure 4 recadrée (5 indicateurs primaires en tête) + encadré « déséquilibres à T0 » |
| `T14_asc_3volets_complet` | 120 | — | **E** | Version longue (Ensemble, bras, provinces, bras × province) non utilisée par le rapport. | Annexe D — réservé aux besoins de vérification |
| `T14_asc_3volets` | 24 | Tableau 15 | **B** | 24 lignes = 8 indicateurs × 3 volets ; les IC de l'écart diffèrent systématiquement du classeur (ex. supervision : [-7,6 ; 23,2] dans le classeur, [-6,4 ; 22,0] dans le rapport) sans que la méthode soit documentée. | Corps, chapitre 4 — 8 lignes (un indicateur par ligne, trois colonnes de groupes) + note d'IC |
| `T14_cac_3volets_complet` | 225 | — | **E** | Version longue non utilisée ; sert de base à la figure 6 et aux fiches. | Annexe D |
| `T14_cac_3volets` | 45 | Tableau 7 | **B** | 45 lignes = 15 indicateurs × 3 volets ; les IC de l'écart du rapport sont plus étroits que ceux du classeur pour 42 des 45 lignes (ex. indice de riposte : [-16,2 ; 20,9] vs [-14,7 ; 19,4]). | Corps, chapitre 3 — 10 indicateurs en lignes, 3 groupes en colonnes ; 5 indicateurs secondaires en annexe |
| `T14_cod_3volets_complet` | 165 | — | **E** | Version longue non utilisée. | Annexe D |
| `T14_cod_3volets` | 33 | Tableau 8 | **B** | 33 lignes = 11 indicateurs × 3 volets ; n très faibles (96 CODESA, 48 par bras) et IC de ±20 à ±30 points : les écarts ne sont pas interprétables, ce que le tableau ne dit pas. | Corps, chapitre 3 — 8 lignes + bandeau « n = 96, IC de ±20 points : aucune conclusion d'écart » |
| `T14_men_3volets_complet` | 480 | — | **E** | 480 lignes (32 indicateurs × 15 groupes) : c'est la matrice la plus riche du classeur, non publiée. | Annexe D + source des figures de synthèse |
| `T14_men_3volets` | 96 | Tableau 18 | **D** | 96 lignes = 32 indicateurs × 3 volets ; doublon partiel du tableau 53 (129 lignes) ; c'est le tableau le plus long du corps du rapport. | Corps, chapitre 5 — tableau de synthèse 12 lignes (indicateurs prioritaires) + figure dumbbell ; 96 lignes en annexe D |
| `T14_reco_3volets_complet` | 285 | — | **E** | Version longue non utilisée ; contient les composantes utiles aux fiches. | Annexe D |
| `T14_reco_3volets` | 57 | Tableau 12 | **B** | 57 lignes = 19 indicateurs × 3 volets ; IC de l'écart plus étroits que le classeur pour 51 des 57 lignes. | Corps, chapitre 4 — 10 lignes ; 9 indicateurs en annexe D |
| `T15_asc_3volets_province` | 32 | — | **E** | 32 lignes non publiées ; nécessaire pour situer une zone dans sa province (fiches). | Annexe D + alimentation des fiches |
| `T15_cac_3volets_province` | 60 | — | **E** | 60 lignes non publiées ; les IC par province atteignent ±40 points (n ≈ 143 par province). | Annexe D — avec avertissement de puissance |
| `T15_cod_3volets_province` | 44 | — | **E** | 44 lignes non publiées ; n ≈ 24 CODESA par province. | Annexe D |
| `T15_men_3volets_province` | 128 | Tableau 53 (annexe D) | **E** | 128 lignes = 32 indicateurs × 4 provinces ; doublon de structure avec le tableau 18. | Annexe D — conservé tel quel mais avec en-tête de colonnes explicite |
| `T15_reco_3volets_province` | 76 | — | **E** | 76 lignes non publiées ; n = 144 RECO par province. | Annexe D |
| `T16_categories_organes` | 24 | Tableau 9 | **C** | 24 lignes = 2 organes × 2 bras × 2 passages × 3 catégories : trois dimensions en lignes pour une information qui est une composition. | Corps, chapitre 3 — barres empilées 100 % (organe × bras × passage) + tableau 4 lignes |
| `T17_ucodesa` | 30 | Tableau 59 (annexe D) | **C** | 30 lignes (15 UCODESA × 2 passages) pour une seule variable (part de femmes), avec des effectifs de 2 à 8 membres. | Annexe D + micro-figure en fiche de zone |
| `T18_evolutions_longues` | 330 | — | **E** | Tableau de travail (22 indicateurs × 15 groupes) destiné aux figures ; non publiable. | Annexe D ou hors rapport (document de production) |
| `T19_16_zones_complet` | 208 | — | **E** | 13 variables × 16 zones, avec valeurs brutes (y) et résidualisées (r) : seul endroit où les deux définitions coexistent. | Annexe D + source unique des fiches et de la figure des pentes |
| `T19_16_zones_P1` | 16 | Tableau 21 | **B** | 16 lignes, 10 colonnes ; l'« évolution ajustée » diffère pour 10 des 16 zones de celle du rapport (Kibombo 4,7 vs 4,8 ; Pangi -0,6 vs -0,8). | Corps, chapitre 6 — 6 colonnes (T0, T1, n, évolution brute, évolution ajustée, écart) + figure des pentes |
| `T19_16_zones_P2` | 16 | Tableau 54 (annexe D) | **B** | « Évolution ajustée » différente pour 9 des 16 zones ; T0 révisé pour Kibombo (20,4 vs 23,7) et Tunda (14,4 vs 15,0). | Annexe D — avec renvoi à l'annexe A pour les valeurs de T0 révisées |
| `T19_16_zones_P3` | 16 | Tableau 22 | **B** | Reproductible (aucun écart) ; 16 lignes, 10 colonnes. | Corps, chapitre 6 — 6 colonnes ; figure commune avec P1 |
| `T19_16_zones_P4` | 16 | Tableau 55 (annexe D) | **A** | Reproductible ; en annexe alors qu'il porte la dispersion la plus forte (-13,5 à +22,1 points). | Corps, chapitre 6 — déplacé de l'annexe vers le corps, en figure |
| `T20_transitions_matrices` | 36 | Tableau 10 | **E** | 36 lignes = 2 organes × 2 bras × 9 transitions ; les 9 transitions sont déjà représentées par les figures 5 et 6. | Annexe D — tableau conservé comme source chiffrée des figures 5 et 6 |
| `T21_mouvements_unites` | 4 | Tableau 11 | **A** | 4 lignes, parfait pour un tableau de synthèse ; mais le seuil affiché (± 11,1 points = un critère sur neuf pour les CAC) est appliqué aussi aux CODESA, dont le pas est de 14,3 points (un critère sur sept). | Corps, chapitre 3 — conservé, seuil corrigé par organe |
| `T22_unites_progression_regressi` | 249 | — | **C** | 249 unités (189 CAC, 60 CODESA) ; aucune unité stable alors que le tableau 11 en compte 148 : la liste ne contient que les unités ayant bougé, ce qui n'est pas dit ; les écarts sont des multiples exacts du pas (11,1 ou 14,3). | Corps, chapitre 3 — figure « unités en progression, stables, en régression » ; liste nominative en annexe D |
| `T23_repondération_T1` | 16 | Tableau 19 | **C** | 16 lignes = 8 indicateurs × 2 bras ; les valeurs repondérées du rapport diffèrent du classeur (69,5 vs 70,0 ; évolution 4,2 vs 4,8). | Corps, chapitre 5 — dumbbell « évolution brute vs repondérée » par bras (8 indicateurs) + tableau 4 lignes |
| `T25_tableau_des_effets` | 9 | Tableau 20 | **B** | 17 colonnes pour 9 lignes ; trois sources donnent trois estimations principales différentes pour P1 : 1,9 (T25, DiD 16 points), 2,9 (rapport), 3,1 (T25, modèle conjoint) ; la colonne « p ajustée » mêle Holm et BH. | Corps, chapitre 6 — 8 colonnes (T0/T1 par bras, DiD principale, IC, p ajustée, EMD, seuil, cas) ; colonnes de sensibilité en annexe |
| `T26_unites_appariees` | 2 | Tableau 25 | **A** | 2 lignes, très lisible ; mais l'EMD de 23 points annoncée en note n'est pas calculée dans le classeur. | Corps, chapitre 6.1 — conservé |
| `T27_divergence_tendances` | 20 | Tableau 24 | **C** | 20 lignes = 4 indicateurs × 5 divergences ; les valeurs du rapport (7,9 [-0,6 ; 15,3]) ne se déduisent pas du classeur (6,9 [-0,6 ; 13,3]) ; colonne « Cas » codée A-E sans grille sous les yeux du lecteur. | Corps, chapitre 6.1 — figure « effet corrigé selon la divergence supposée » (4 courbes, bande IC) + 4 lignes de tableau |
| `T28_placebos` | 6 | Tableau 23 | **A** | 6 lignes, bien construit ; une ligne diffère du classeur (âge : 31,6 vs 31,2 ; DiD -0,6 vs -0,3). | Corps, chapitre 6.1 — conservé |
| `T29_effets_secondaires` | 70 | Tableau 26 | **E** | 70 lignes ; aucun indicateur ne survit à la correction BH (p ajustée minimale 0,607) ; le tableau occupe plusieurs pages pour un résultat nul. | Annexe D + corps : figure forêt BH (10 indicateurs à p brut < 0,15) et 3 lignes de commentaire |
| `T30_differences_premieres_aires` | 17 | Tableau 27 | **D** | 17 lignes = 8 modèles ; le coefficient D1 de D3 vaut 0,2 [0,08 ; 0,31] dans le rapport et 0,11 [0,01 ; 0,21] dans le classeur (facteur 2) ; la variable « dD1 » n'est pas définie dans le tableau. | Corps, chapitre 7 — tableau de synthèse 5 lignes (un modèle, un coefficient clé, IC, p) + détail en annexe |
| `T31_associations_transversales` | 9 | Tableau 28 | **A** | 9 lignes ; n différent (4 984 vs 4 954) ; le coefficient D3 ~ P3 vaut 0,1 dans le rapport et 0,05 dans le classeur ; la colonne « Valeur E, borne proche de 0 » du rapport n'existe pas dans le classeur. | Corps, chapitre 7 — conservé après correction, avec la valeur E et sa borne |
| `T32_variance_niveaux` | 8 | Tableau 29 | **C** | 8 lignes ; pour D3, les variances du rapport (0,321 / 0,075 / 0,458) ne correspondent pas au classeur (0,109 / 0,029 / 0,169) ; la part d'aire du rapport (0,376) est présentée comme un résultat alors qu'elle dépend de composantes divergentes. | Corps, chapitre 7 — barres empilées de décomposition (aire / ZS / résiduel) par indicateur et passage |
| `T33_effets_aires` | 776 | Figure 12 (source) | **E** | 776 lignes (4 résultats × 2 passages × ~97 aires) : données de figure, pas tableau ; contient la variable « hors_ic » qui fonde les « signalements » des fiches. | Annexe D (extrait : 10 aires les plus atypiques) + source de la figure 12 |
| `T34_capacites_extrants_reco` | 3 | Tableau 30 | **A** | 3 lignes, très clair ; rapport de taux 1,84 pour la prime, non commenté dans le rapport. | Corps, chapitre 7 — conservé |
| `T35_heterogeneite` | 20 | Tableau 31 | **C** | 20 lignes ; les effectifs du rapport (1 900 / 3 091) diffèrent du classeur (2 285 / 3 428) et les DiD aussi (4,0 vs 3,2) ; les lignes « Province » n'ont ni n ni IC. | Corps, chapitre 8 — figure forêt par sous-groupe (déjà figure 13) + 8 lignes de tableau |
| `T36_concentration_erreygers` | 24 | Tableau 32 | **C** | 24 lignes = 6 indicateurs × 2 bras × 2 passages ; les différences avec le classeur sont des arrondis (0,093 vs 0,091). | Corps, chapitre 8 — dumbbell T0 → T1 par indicateur et par bras (12 paires) + annexe |
| `T37_gradient_quintiles` | 160 | Figure 14 (source) | **E** | 160 lignes = 8 indicateurs × 4 groupes × 5 quintiles : données de figure. | Annexe D (source) + figure 14 dans le corps |
| `T38_genre` | 25 | Tableau 33 | **C** | 25 lignes = 9 populations × bras × passage ; deux lignes à n = 2 (« RECO désignés depuis moins d'un an ») : pourcentages non interprétables. | Corps, chapitre 8 — barres groupées « part de femmes » par acteur et passage, ligne de repère 50 % |
| `T39_continuum_maternel` | 32 | Tableau 56 (annexe D) | **A** | 32 lignes, deux populations (toutes les femmes / naissances < 6 mois) ; les n du rapport diffèrent du classeur (172 vs 252 pour la CPoN) ; le tableau est en annexe alors que la figure 15 du corps en dépend. | Corps, chapitre 9.1 — remonté en tableau 34 (2 populations × 4 étapes, 8 lignes) ; figure 15 reconstruite à partir de T40 |
| `T40_continuum_conditionnel` | 4 | Tableau 34 | **A** | 4 lignes ; la « co-couverture des 4 étapes » (16,7 % à 24,2 %) n'est pas le produit des probabilités conditionnelles affichées (0,415 × 0,943 × 0,35 ≈ 13,7 %) : la règle de calcul n'est pas documentée. | Corps, chapitre 9.1 — conservé avec une note de calcul explicite |
| `T41_enfant_malade_distributions` | 12 | Figure 16 (source) | **C** | 12 lignes × 17 colonnes : deux questions différentes (première réaction / lieu / délai) dans une même matrice, avec des colonnes vides pour chaque bloc. | Corps, chapitre 9.2 — figure 16 conservée ; trois petits tableaux de 4 lignes si chiffres nécessaires |
| `T42_enfant_malade_multinomial` | 4 | Tableau 35 | **A** | 4 lignes, très lisible ; écarts d'arrondi avec le classeur (58,9 vs 58,6). | Corps, chapitre 9.2 — conservé |
| `T43_enfant_malade_deux_parties` | 20 | Tableau 36 | **B** | 20 lignes dont 18 coefficients : le lecteur ne peut pas distinguer les termes d'intérêt (bras, passage, interaction) des covariables d'ajustement. | Corps, chapitre 9.2 — 6 lignes (bras, passage, interaction, J2, quintile 5, marche) + renvoi en annexe |
| `T44_vaccination_declare_vu` | 20 | Tableau 37 | **A** | 20 lignes ; l'écart est calculé entre deux indicateurs de dénominateur identique (tous ménages), ce qui est correct, mais la colonne « Carnet vu (%) » porte le même libellé que l'indicateur W2 (parmi les vaccinés) utilisé ailleurs : deux indicateurs, un seul nom. | Corps, chapitre 9.3 — conservé, libellés explicites (« carnet vu, tous ménages » / « carnet vu parmi les vaccinés ») + figure 17 |
| `T45_mpox_cap` | 120 | Tableau 57 (annexe D) | **E** | 120 lignes ; 8 lignes « Synthèse » sans aucun libellé d'item, qui portent deux valeurs distinctes pour un même bras × passage (55,5 et 61,5 chez les témoins à T0) : les deux séries sont indiscernables ; les dénominateurs diffèrent entre blocs sans explication. | Annexe D + corps : figure 18 (12 items) et 8 lignes de synthèse nommées |
| `T46_mpox_acceptabilite` | 14 | Tableau 38 | **A** | 14 lignes ; les p « < 0,001 » sont correctement rendus ; les rapports de cotes diffèrent légèrement du classeur (4,35 contre 4,38 ; 0,97 contre 0,98) comme les p intermédiaires (0,894 contre 0,945 ; 0,717 contre 0,723) — dérive de recalcul, sans effet sur la lecture. | Corps, chapitre 9.4 — conservé |
| `T47_reco_professionnalisation_c` | 36 | Tableau 13 | **C** | 36 lignes = 9 composantes × 2 bras × 2 passages ; P4 et P4 hors intrants figurent dans le même tableau que leurs composantes (redondance), et le total P4 n'est pas la moyenne simple des 6 items affichés. | Corps, chapitre 4 — dumbbell des 9 composantes (4 points par composante) + 6 lignes |
| `T48_asc_prime_montant` | 4 | Tableau 16 | **A** | 4 lignes, effectifs 28 / 16 / 23 / 19 : les médianes (10 vs 30 USD) sont robustes mais les IC ne sont pas calculés et la période de versement n'est pas connue. | Corps, chapitre 4 — conservé avec effectifs rappelés en tête et note sur la période |
| `T49_reco_charge_menages` | 4 | Tableau 14 | **A** | 4 lignes ; Gini intra-ZS (0,45 à 0,55) et part > 100 ménages (16,7 % à 24,4 %) sont deux mesures de la même dispersion, présentées sans hiérarchie. | Corps, chapitre 4 — conservé |
| `T50_logistique` | 28 | Tableau 17 | **B** | 28 lignes = 7 indicateurs × 2 bases × 2 bras × 2 passages ; les IC de ±25 à ±30 points (RECO) ne sont pas signalés. | Corps, chapitre 4 — 8 lignes (ruptures de stock, information, transport, équipement) + annexe |
| `T51_normes_psn` | 20 | Tableau 39 | **D** | 20 normes, dont 2 seulement portent une cible chiffrée (« 50 % de femmes ») et une une norme structurelle (« ≤ 50 ménages ») ; les autres sont des niveaux descriptifs présentés comme des normes ; « ASC formé et certifié » n'est traçable dans aucun autre onglet. | Corps, chapitre 10 — tableau de synthèse 8 normes (cible documentée, valeur T0/T1, écart) + figure d'écart à la cible |
| `T52_indice_conformite` | 8 | Tableau 40 | **A** | 8 lignes, lisible ; les 6 normes composant l'indice ne sont pas listées dans le tableau ni dans sa note. | Corps, chapitre 10 — conservé + liste des 6 normes en note |
| `T53_sensibilite_D1` | 7 | — | **E** | 7 variantes, absente du rapport alors que D1 est commenté dans le résumé exécutif. | Annexe D — ajoutée |
| `T53_sensibilite_D2` | 7 | — | **E** | 7 variantes, absente du rapport. | Annexe D — ajoutée |
| `T53_sensibilite_D3` | 14 | — | **E** | 14 variantes, absente du rapport alors que D3 est un indice de résultat. | Annexe D — ajoutée |
| `T53_sensibilite_P1` | 22 | Tableau 42 | **C** | 22 variantes ; la ligne « Principale » du classeur porte 1,9 (16 points) alors que le rapport retient 2,9 (modèle conjoint) : la matrice est calculée sur l'ancienne estimation principale, ce qui invalide la comparaison « conclusion inchangée ». | Corps, chapitre 11 — courbe de spécification (figure 19) + 6 lignes ; matrice complète en annexe D |
| `T53_sensibilite_P2` | 21 | Tableau 43 | **C** | 21 variantes, même décalage d'estimation principale (-1,9 vs -3,6). | Corps, chapitre 11 — courbe de spécification + annexe D |
| `T53_sensibilite_P3` | 23 | Tableau 44 | **B** | 23 variantes : ici les valeurs coïncident, seuls les libellés de la ligne « Principale » sont inversés (16 points vs modèle conjoint). | Annexe D — matrice conservée ; corps : 6 lignes |
| `T53_sensibilite_P4` | 18 | Tableau 45 | **B** | 18 variantes, même défaut d'étiquetage que P3. | Annexe D — matrice conservée ; corps : 6 lignes |
| `T54_synthese_sensibilite` | 7 | Tableau 41 | **A** | 7 lignes ; la part de variantes de même conclusion diffère fortement du rapport pour P2 (76 % au classeur, 44 % au rapport) et le nombre de variantes aussi (17 vs 16). | Corps, chapitre 11 — conservé, recalculé |
| `T55_manquants_primaires` | 20 | Tableau 52 (annexe C) | **B** | 20 lignes, mais « Manquants (%) = 0 » partout alors que le tableau 51 montre 29,8 % de manquants sur W2 : la différence (règle du minimum d'items) n'est pas expliquée ; valeurs différentes du rapport (12,3 vs 12,4 ; 11,7 vs 11,9 ; 13,6 vs 14,8). | Annexe C — conservé avec colonne « règle de calcul de l'indice » |
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
---

# PARTIE E — Appareil graphique et fiches de zone

*Axe 6 — lisibilité et encodage ; axe 7 — fiches de zone.*

## E.1 Ce que contient réellement le dossier d'images

Le document embarque 44 fichiers PNG. Leur répartition est instructive :

| Nature | Nombre | Référencés | Dimensions typiques | Rôle |
|---|---:|---:|---|---|
| Images de graphique | 24 | 24 | 1 889 à 2 191 px de large | Portent les 20 figures |
| Barres de titre décoratives | 16 | 15 | 2 079 × 284 px | Bandeaux de chapitre |
| Image de couverture | 1 | 1 | 1 819 × 2 573 px | Page de titre |
| Filet de séparation | 1 | 0 | 2 000 × 16 px | Séparateur |
| Autres images inutilisées | 2 | 0 | — | Résidus de versions antérieures |
| **Total** | **44** | **40** | — | **4 non référencés** |

Deux observations. D'une part, les 16 barres décoratives représentent 36 % des fichiers images : elles alourdissent le document et rendent tout contrôle automatique des figures impossible sans les écarter par un test de densité. D'autre part, quatre PNG ne sont appelés nulle part : ils proviennent de versions antérieures et devraient être purgés, car ils empêchent de répondre à la question simple « combien de figures ce document contient-il ? » autrement qu'en analysant le XML.

## E.2 Les défauts certains

Sept défauts sont établis par examen direct des images et du texte. Ils sont présentés par ordre de gravité.

**1. La figure 15 est vide.** L'image `414f5c73` (1 889 × 1 122 px) porte la légende « Cascade CPN1 → CPN4+ → accouchement en structure → consultation postnatale ». Les axes sont tracés, l'échelle verticale va de 0 à 100, les étiquettes d'étapes sont en place. Aucune donnée n'est dessinée : la densité d'encre hors bandeau de titre est de 0,007, contre 0,06 à 0,27 pour les autres figures, et l'écart est d'un facteur dix. Une figure vide dans un rapport de résultats n'est pas un détail de mise en forme : c'est une affirmation implicite — « la cascade n'a pas pu être produite » — que le texte ne porte pas.

**2. Quatre titres sont coupés par le bord du canevas.** Figures 2 (« …la conformité progresse sur la désignation et les réunion**s** »), 5 (« …les mouvements von**t** dans les deux sens »), 7 (quatrième panneau : « Professionnalisation »), 8 (« D4 lu en évolution seulemen**t** »). Le défaut est mécanique — la zone de titre n'a pas été dimensionnée pour la longueur du texte — et il est systématique : une phrase de titre trop longue est tronquée silencieusement, sans avertissement du producteur.

**3. La note de la figure 17 annonce des intervalles de confiance qui ne sont pas tracés.** La note se termine par « pondération égale des provinces ; IC à 95 % ». L'image ne contient aucune barre d'erreur, aucun intervalle, aucun chiffre d'incertitude : quatre points par panneau, reliés par un segment. Une note de figure qui décrit un élément absent est plus grave qu'une note absente, parce qu'elle empêche le lecteur de douter.

**4. La figure 1 annonce une chose et en montre une autre.** La légende dit « Forêt des effets sur les quatre indicateurs primaires : DiD à 16 points ». La forêt trace deux séries : « estimation principale, modèle conjoint à effets fixes d'aire, IC CR2 » (point marine) et « DiD brute à 16 points » (carré cyan). La série mise en avant est donc celle du modèle conjoint, et les valeurs affichées (2,9 ; −3,6 ; 0,1 ; −3,2) sont celles du modèle conjoint, non celles de la DiD à 16 points (3,0 ; −2,1 ; 0,3 ; −2,4). La légende et le contenu désignent deux estimateurs différents.

**5. Le titre de la figure 7 est contredit par les valeurs de la figure 7.** Le titre affirme : « Les quatre indicateurs primaires progressent dans les deux bras ; les pentes sont parallèles ». Les pentes ne sont pas parallèles : pour P1, le bras intervention passe de 62,2 à 69,2 (+7,0 points) tandis que le bras témoin passe de 65,3 à 69,2 (+3,9 points), soit un écart de pente de 3,1 points — c'est précisément cet écart que le rapport estime ensuite. Pour P2, le bras intervention progresse de 6,5 points et le bras témoin de 8,6 points, dans l'autre sens. Une figure dont le titre contredit les données qu'elle affiche est un défaut de rédaction, mais il porte ici sur l'hypothèse centrale du devis : l'égalité des tendances. Le titre doit dire « les pentes divergent de 3,1 points sur P1, ce qui est l'objet du test », ou ne rien dire.

**6. Deux figures invitent à une lecture causale qu'elles ne peuvent pas soutenir.** La figure 2 compare, pour 19 normes, les niveaux de conformité des deux bras à T0 et à T1, avec un titre assertif (« la conformité progresse sur la désignation et les réunions, stagne sur la prime et le contrat »). Or une comparaison de niveaux entre bras n'est pas un effet : à T1, le bras intervention est à 18 % de RECO avec contrat contre 33 % dans le bras témoin, et cette différence de niveau n'autorise aucune conclusion sur l'effet du programme. Le titre transforme une lecture descriptive en jugement d'efficacité. De plus, deux normes s'intitulent « (cible 50 %) » — la part de femmes parmi les RECO et parmi les ASC — sans qu'aucun repère à 50 % ne soit tracé : la figure nomme une cible et ne la montre pas.

**7. Le double codage « évité / plein » est illisible sur les séries orange.** Aux figures 2, 5, 6 et 17, le passage T0 → T1 est encodé par un marqueur évidé puis plein. Pour la série orange (témoin, marqueur en losange), le losange évidé et le losange plein sont visuellement confondus à la taille d'impression, alors qu'ils se distinguent bien pour la série bleue (cercle). Le lecteur ne peut pas suivre la série témoin. À la figure 1 (panneaux), le problème s'aggrave : à T1, les deux bras de P1 convergent exactement sur 69,2, les marqueurs se superposent et une seule étiquette subsiste.

**Un défaut d'encodage qui n'est pas seulement esthétique.** Dans la figure 1 (panneaux) et la figure 8, les étiquettes de cas utilisent l'orange pour « cas D » (couleur qui, dans la même figure, désigne le bras témoin) et le gris foncé pour « cas E ». Une couleur ne peut pas porter deux variables dans la même figure : le lecteur croit que « cas D » qualifie le bras témoin. Par ailleurs, le seuil de pertinence est tracé par un tiret rouge non étiqueté : comme il vaut 5 points pour P1 et P2, 11 pour P3 et 8 pour P4, et que les quatre panneaux partagent une échelle, le lecteur ne peut pas savoir à quel seuil se rapporte chaque tiret sans consulter le tableau 20.

## E.3 Points examinés et écartés

**Aucune figure n'est un doublon.** La corrélation deux à deux des 44 images en niveaux de gris fait apparaître des coefficients élevés (0,96) entre la figure 5 (transitions des CODESA) et la figure 6 (transitions des CAC), ainsi qu'entre plusieurs barres de titre. Après examen, ces ressemblances s'expliquent par un gabarit commun — même mise en page, mêmes palettes — et non par une duplication : les données sont différentes et les deux figures sont légitimes. La suspicion de doublon est levée.

**Le décompte des aires de la figure 5 est exact.** La figure montre 46 aires dans le bras témoin (22 + 15 + 9) et 45 dans le bras intervention (26 + 11 + 8), soit 91 aires. Le tableau 4 donne 91 aires appariées. La cohérence est parfaite ; ce sont les 98 aires du résumé exécutif qui nécessitent une précision de vocabulaire (base de sondage, non unités enquêtées), traitée en D.2.

**La figure 4 est lisible et utile.** La comparaison des différences standardisées des covariables entre bras à T0 et T1 est correctement construite, avec une bande de ± 0,10 visible. Deux covariables sortent de cette bande (instruction : « aucune », 0,35 ; taille du ménage, −0,32), ce qui est un résultat à commenter. Mais surtout, deux indicateurs primaires en sortent très largement : P3 (fonctionnalité des CAC) à 0,376 et P4 (professionnalisation des RECO) à 0,275 à T0, selon l'onglet `T13_equilibre_T0` qui alimente la figure 4. La figure 4 ne les met pas en évidence et le texte, non rédigé, ne les commente pas. **C'est le point analytique le plus important de cette partie** : les deux indicateurs d'offre présentent, à l'inclusion, un déséquilibre entre bras supérieur au seuil d'alerte du rapport, et c'est sur eux que porte la seule conclusion conclusive du dispositif (D.3). Le lecteur doit être conduit de l'un à l'autre explicitement.

> **REC-012 — Reprendre l'appareil graphique** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-012 |
| 2. Constat | Figure 15 vide ; quatre titres tronqués (2, 5, 7, 8) ; note de la figure 17 annonçant des IC non tracés ; légende de la figure 1 désignant un autre estimateur que celui tracé ; titre de la figure 7 contredit par ses valeurs ; double codage illisible sur les séries orange ; couleur de cas confondue avec la couleur de bras. |
| 3. Preuve | Images `414f5c73` (densité 0,007), `03416a46`, `767a698a`, `a3366995`, `4503ad41` ; figure 17 et sa note ; figures 1 et 2. |
| 4. Axe | 6 — lisibilité |
| 5. Criticité | Bloquant |
| 6. Cause probable | Production automatique avec une largeur de canevas fixe et des titres variables ; absence de relecture visuelle avant export. |
| 7. Effet | Une figure vide, des titres incomplets et une note fausse suffisent à discréditer l'ensemble du document auprès d'un lecteur attentif. |
| 8. Recommandation | Régénérer les figures 1, 2, 5, 7, 8, 15 et 17 : titres sur deux lignes avec largeur ajustée, marqueurs différenciés par forme pour T0/T1, seuils étiquetés avec leur valeur, cas codés dans une couleur neutre, note de la figure 17 corrigée ou IC effectivement tracés, figure 15 reconstruite depuis les tableaux 34 et 56. |
| 9. Modalité | Producteur des figures ; contrôle par un test automatique de débordement (encre sur les deux colonnes de bord) et par relecture des 20 figures. |
| 10. Livrable | 20 figures v2 + rapport v2. |
| 11. Effort | 3 jours-personne. |
| 12. Dépendance | REC-004 (la figure 1 doit suivre l'estimation principale déclarée). |
| 13. Clôture | 0 figure vide ; 0 titre tronqué (test automatique) ; 0 note décrivant un élément absent. |
| 14. Statut | Ouvert. |

## E.4 Justification analytique, figure par figure

Chaque figure est jugée sur une seule question : apporte-t-elle ce qu'aucun tableau ne peut apporter ? La colonne « Verdict » distingue *conserver*, *reprendre* (contenu juste, exécution à corriger) et *reconstruire* (contenu manquant).

| Fig. | Ce qu'elle montre | Question analytique servie | Verdict | Motif |
|---:|---|---|---|---|
| 1 | Forêt des 5 effets (4 primaires + hors intrants) et 4 panneaux T0→T1 par bras | Situer les quatre effets sur une échelle commune avec leur incertitude | **Reprendre** | Légende « DiD à 16 points » contre série « modèle conjoint » ; cas colorés comme les bras ; seuils non étiquetés ; panneaux redondants avec la forêt |
| 2 | 19 normes du PSN, niveaux T0/T1 par bras | Mesurer l'écart à la norme, norme par norme | **Reprendre** | Titre assertif sur un effet non testé ; cibles à 50 % non tracées ; T0/T1 illisible sur la série orange |
| 3 | Effectifs d'ASC enquêtés par zone à T0 et T1 | Documenter le déficit d'ASC et sa géographie | **Conserver** | Figure adaptée ; le commentaire devra distinguer zones déficitaires et zones à effectif élevé (Ototo dépasse 20 ASC à T1) |
| 4 | Différences standardisées des covariables, T0 et T1 | Établir la comparabilité initiale des bras | **Reprendre** | Ne signale pas les deux primaires hors bande (P3 : 0,376 ; P4 : 0,275), alors qu'ils conditionnent l'interprétation (voir D.5) |
| 5 | Transitions des CODESA entre 3 catégories, 91 aires | Montrer l'ampleur des mouvements entre catégories | **Reprendre** | Titre tronqué ; effectifs lisibles mais T0/T1 confondus sur l'orange |
| 6 | Transitions des CAC, villages appariés | Idem pour les CAC (306 appariés) | **Conserver** | Gabarit éprouvé ; préciser en titre la population (306 CAC appariés, non 1 143 observations) |
| 7 | Évolution T0→T1 des 4 primaires, moyennes de zone | Montrer que les deux bras progressent | **Reprendre** | Titre contredit par les pentes ; échelles libres empêchant la lecture de l'écart initial ; étiquette 62,2 masquée |
| 8 | Forêt des 4 indices de domaine | Situer les effets sur les indices composites | **Reprendre** | Titre tronqué ; « cas D » non défini ; série principale étiquetée différemment du tableau 20 |
| 9 | Distributions de permutation des 4 primaires (1 296 attributions) | Fonder la p de permutation | **Conserver** | Figure rare et utile ; ajouter la valeur observée sur chaque histogramme |
| 10 | Évolutions ajustées par zone, province et bras | Montrer la dispersion inter-zones | **Conserver** | Seule figure qui donne la dispersion ; vérifier la cohérence avec les tableaux 21/22/54/55 (colonne ajustée divergente) |
| 11 | Forêt DiD des indicateurs secondaires, après BH | Montrer qu'aucun résultat secondaire ne survit | **Conserver** | Bien construite ; indiquer combien des 70 indicateurs secondaires sont représentés |
| 12 | Effets aléatoires d'aire sur P1 | Identifier les aires atypiques | **Conserver** | Utile au volet qualitatif ; la variable « hors IC » qui fonde les signalements doit être définie en note |
| 13 | Forêt par sous-groupe et test global | Établir l'absence d'hétérogénéité détectable | **Conserver** | Bonne figure ; ajouter les effectifs par sous-groupe |
| 14 | Gradient par quintile de niveau de vie | Documenter le gradient social | **Conserver** | Figure adaptée ; préciser l'indicateur de niveau de vie et le nombre d'observations par quintile |
| 15 | Cascade CPN1 → CPN4+ → accouchement → postnatal | Mesurer l'abandon entre étapes | **Reconstruire** | **Figure vide** ; à produire depuis les tableaux 34 (probabilités conditionnelles) et 56 (étapes) |
| 16 | Première réaction devant l'enfant malade | Comparer les recours par bras et passage | **Conserver** | Figure adaptée à une question à modalités multiples |
| 17 | Vaccination déclarée et carnet vu, par province | Mesurer l'écart déclaratif | **Reprendre** | Note annonçant des IC absents ; ajouter les dénominateurs (enfants vaccinés) par panneau |
| 18 | Connaissances et attitudes Mpox par item | Situer les items les plus faibles | **Conserver** | Figure adaptée ; l'ordre des items doit être stable entre T0 et T1 |
| 19 | Courbes de spécification des 4 primaires | Montrer la stabilité de l'estimation selon les spécifications | **Conserver** | Excellente figure ; elle doit être calculée sur l'estimation principale déclarée |
| 20 | Estimations en retirant chaque zone | Tester l'influence d'une zone | **Conserver** | Figure adaptée ; nommer la zone la plus influente |

Bilan : **11 figures conservées, 7 à reprendre, 1 à reconstruire, 1 à vérifier** (figure 10). Aucune figure n'est superflue, ce qui est remarquable pour un document de cette taille ; le problème est l'exécution, non le choix.

## E.5 Les fiches de zone

Les seize fiches suivent un modèle unique : un en-tête (province, bras), un tableau de 22 indicateurs en six colonnes (T0, T1, évolution, valeur provinciale à T1, valeur bras × province à T1), puis un encadré « Contexte (volet qualitatif) » vide. Les zones couvrent quatre provinces (Maniema, Kasaï-Oriental, Sankuru, Sud-Kivu) et huit zones par bras.

**Ce qui fonctionne.** Les 22 indicateurs sont organisés en trois blocs (ménages, organes, agents) qui correspondent aux trois registres du rapport, et les valeurs sont exactes : sur 64 cellules de primaires contrôlées, deux divergent du classeur, et ce sont les deux valeurs de T0 que l'annexe A doit expliquer. La fiche est donc fiable à 97 %.

**Ce qui ne fonctionne pas.**

*Les colonnes de référence ne sont données qu'à T1.* La fiche indique la valeur de la province à T1 et celle du croisement bras × province à T1, mais pas leurs valeurs à T0. Le lecteur peut donc comparer un niveau, pas une évolution : il ne peut pas savoir si la zone a progressé plus ou moins que sa province, puisque l'évolution provinciale n'est pas affichée. Pour une fiche destinée à un usage décentralisé — ce qui est manifestement son objet — c'est la comparaison la plus utile qui manque.

*Le choix des 22 indicateurs n'est pas justifié et n'est pas adapté à la zone.* Les mêmes 22 lignes sont servies à une zone de Maniema et à une zone du Sud-Kivu, quelle que soit la taille de la zone. Une ligne comme « ASC enquêtés (nombre) » (8 à T0, 7 à T1 pour Kibombo) n'a aucun intérêt analytique dans une fiche de résultats ; à l'inverse, la fiche ne donne ni la taille de la population couverte, ni le nombre d'aires, qui sont les premiers éléments de contexte dont un lecteur local a besoin.

*Le contexte qualitatif est vide dans les seize fiches.* Chaque fiche se termine par « Contexte (volet qualitatif) : événements, note de mise en œuvre, mode de paiement… » : seize fois la même phrase, seize fois sans contenu. Une fiche sans son contexte est un tableau de chiffres, pas une fiche.

*Une valeur mérite un contrôle avant publication.* La fiche de Kibombo indique « RECO en riposte (%) : 100,0 à T0, 45,7 à T1, soit −54,3 points ». Une chute de 54 points en un an sur un indicateur de mobilisation est un signal fort ; elle doit être vérifiée (effectif de base, formulation de la question, possible changement de période de référence) avant d'être publiée, et commentée si elle est exacte.

> **REC-013 — Refondre le modèle de fiche de zone** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-013 |
| 2. Constat | Les colonnes de référence ne sont fournies qu'à T1, ce qui interdit toute comparaison d'évolution ; les 22 indicateurs ne sont pas hiérarchisés ; le contexte qualitatif est vide dans 16 fiches sur 16 ; une valeur (RECO en riposte, −54,3 pts) n'est pas contrôlée. |
| 3. Preuve | Fiches de zone, tableaux 79, 82, 85… (22 lignes × 6 colonnes) ; encadré « Contexte (volet qualitatif) ». |
| 4. Axe | 7 — fiches de zone |
| 5. Criticité | Majeur |
| 6. Cause probable | Modèle conçu comme une extraction automatique d'indicateurs, non comme un support de dialogue avec la zone. |
| 7. Effet | La fiche ne permet pas de répondre à la question qu'elle doit servir : « notre zone a-t-elle progressé plus ou moins que les autres ? » |
| 8. Recommandation | Ajouter trois colonnes (province T0, bras × province T0, écart d'évolution) ; réduire à 12 indicateurs hiérarchisés (4 primaires + 8 indicateurs d'action) ; ajouter en tête la population, le nombre d'aires et d'unités ; remplir le contexte qualitatif ou supprimer l'encadré ; contrôler la ligne « RECO en riposte ». |
| 9. Modalité | Auteur + chargé du volet qualitatif ; régénération des 16 fiches depuis un modèle unique. |
| 10. Livrable | 16 fiches v2. |
| 11. Effort | 2 jours-personne + apport qualitatif. |
| 12. Dépendance | REC-003 (les valeurs de T0 doivent être arrêtées avant régénération). |
| 13. Clôture | 16/16 fiches avec écarts d'évolution ; 0 encadré vide ; 64/64 cellules de primaires conformes au classeur. |
| 14. Statut | Ouvert. |
---

# PARTIE F — Traçabilité, reproductibilité et plan de correction

*Axe 8 — reproductibilité ; axe 9 — complétude ; axe 10 — registre.*

## F.1 Reproductibilité : ce qui est déclaré et ce qui est fourni

Le rapport a l'honnêteté de déclarer ses écarts au protocole au § 11.1 : passage de l'environnement R prévu à un autre environnement de calcul, affectation programmatique des seize zones (et non par tirage), absence de données de panel individuelles, absence de pondération en deçà du niveau provincial, seize grappes seulement, données déclaratives. Cette déclaration est un acte de probité et elle doit être conservée mot pour mot dans la version finale.

Elle ne suffit pas, pour une raison simple : **aucun script n'est fourni**. Le catalogue du classeur renseigne pourtant, pour chaque sortie, un script producteur (`01_nettoyage.R`, puis les scripts d'analyse) et une population. Ces mentions sont l'amorce d'une chaîne reproductible, mais les scripts eux-mêmes ne sont pas joints, et rien n'indique quelle version du code a produit quelle version du classeur.

Il en résulte une conséquence que l'audit a rencontrée à chaque étape : l'écart entre le classeur et le rapport ne peut pas être attribué. Est-ce un recalcul volontaire ? Une correction d'erreur ? Un changement de covariable ? L'audit peut constater l'écart, il ne peut pas en établir la cause. C'est exactement la situation que la reproductibilité est censée éviter.

**Un point technique à corriger, indépendamment des scripts.** Le classeur contient des anomalies de structure qui empêchent son ouverture par les bibliothèques standard : une dimension déclarée `A1` pour toutes les feuilles, et l'absence du fichier `xl/drawings/drawing1.xml` référencé par une feuille. Un lecteur — humain ou machine — qui ouvre ce fichier avec un outil autre qu'Excel obtient une erreur. Un classeur de sorties qui n'est pas lisible par un outil standard n'est pas un classeur de sorties : c'est un document privé.

> **REC-014 — Joindre les scripts, leur version et un journal d'exécution** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-014 |
| 2. Constat | Aucun script n'est fourni ; le catalogue en mentionne pourtant un par sortie ; le classeur présente des anomalies de structure (dimension `A1`, partie de dessin manquante) qui le rendent illisible hors Excel. |
| 3. Preuve | Colonne D du `Catalogue` (`01_nettoyage.R`, etc.) ; absence de répertoire de code ; erreur d'ouverture par une bibliothèque standard ; `xl/drawings/drawing1.xml` absent de l'archive. |
| 4. Axe | 8 — reproductibilité |
| 5. Criticité | Bloquant |
| 6. Cause probable | Livraison limitée aux sorties, sans le code qui les produit. |
| 7. Effet | Aucun écart entre le classeur et le rapport ne peut être expliqué ; l'auditabilité est nulle. |
| 8. Recommandation | Livrer l'archive de code (scripts de nettoyage et d'analyse) avec un fichier `sessionInfo()` ; ajouter un journal d'exécution horodaté ; régénérer le classeur avec un export propre (dimensions correctes, aucune partie manquante) et vérifier l'ouverture par un outil non-Excel. |
| 9. Modalité | Producteur ; constitution de l'archive et test d'ouverture. |
| 10. Livrable | Archive de code versionnée + classeur v2 lisible + journal d'exécution. |
| 11. Effort | 2 jours-personne. |
| 12. Dépendance | REC-005. |
| 13. Clôture | Le classeur s'ouvre avec deux outils indépendants ; chaque tableau du rapport est reproductible par exécution du script déclaré. |
| 14. Statut | Ouvert. |

> **REC-015 — Mettre en place un contrôle automatique avant chaque diffusion** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-015 |
| 2. Constat | Les défauts relevés (figure vide, titres tronqués, note annonçant des IC absents, deux numérotations, 77 tableaux pour 60 légendes, 16 tableaux de fiche non numérotés) sont tous détectables par un contrôle automatique et aucun n'a été détecté. |
| 3. Preuve | Parties A, B et E. |
| 4. Axe | 8 — reproductibilité ; axe 6 |
| 5. Criticité | Majeur |
| 6. Cause probable | Relecture exclusivement humaine, sur un document de 7,4 Mo. |
| 7. Effet | Les défauts se reproduiront à chaque version ; le coût de correction croît avec la taille du document. |
| 8. Recommandation | Écrire une liste de contrôle exécutable en six points : (1) nombre d'objets tabulaires = nombre de légendes ; (2) 0 image de densité d'encre < 0,02 hors bandeau ; (3) 0 image avec encre sur les colonnes de bord ; (4) numérotation des tableaux et figures sans trou ni doublon ; (5) 0 occurrence de « à rédiger » ; (6) 0 écart entre les valeurs des tableaux d'estimation et le classeur. Publier le résultat en annexe F. |
| 9. Modalité | Producteur ; script de contrôle exécuté à chaque export ; résultat joint au document. |
| 10. Livrable | Script `controle_diffusion` + annexe F renseignée par sa sortie. |
| 11. Effort | 2 jours-personne (une fois), puis automatisé. |
| 12. Dépendance | REC-001 (pour le contrôle 6). |
| 13. Clôture | Les six contrôles passent au vert sur la version diffusée. |
| 14. Statut | Ouvert. |

## F.2 Plan de correction

La correction ne peut pas être conduite chapitre par chapitre : elle dépend d'une décision unique, prise en amont, qui commande tout le reste. Le plan est donc séquencé en trois vagues.

### Vague 1 — Décider (2 à 3 jours)

| Ordre | Action | Recommandation | Effet |
|---:|---|---|---|
| 1 | Arrêter l'estimation principale (modèle conjoint, CR2) et l'appliquer partout | REC-004 | Débloque tout le reste |
| 2 | Décider du sort de chaque onglet selon la partie C | REC-016 | Fixe le périmètre du corps et des annexes |
| 3 | Rédiger la note de l'annexe A sur les deux valeurs de T0 | REC-003 | Rend les fiches publiables |
| 4 | Publier la table de décision de la grille et aligner les EMD | REC-022 | Rend les cas reproductibles |

### Vague 2 — Recalculer (5 à 6 jours)

| Ordre | Action | Recommandation | Effet |
|---:|---|---|---|
| 5 | Régénérer les sorties d'estimation avec version et journal | REC-005, REC-014 | Traçabilité |
| 6 | Recalculer les 5 tableaux « trois volets », les 7 matrices de sensibilité et le tableau 41 | REC-006 | Supprime 4 modes de défaillance |
| 7 | Recalculer les colonnes « évolution ajustée » des tableaux 21 et 54 | REC-006 | Supprime 19 zones divergentes |
| 8 | Décrire la repondération de second niveau et livrer la table de poids | REC-020 | Explique un rapport de poids de 11 |
| 9 | Documenter la co-couverture, puis reconstruire la figure 15 et reprendre 7 figures | REC-012, REC-021 | Appareil graphique fiable et cascade vérifiable |
| 10 | Régénérer les 16 fiches de zone sur le modèle refondu | REC-013 | Support décentralisé utilisable |

### Vague 3 — Écrire et contrôler (10 à 15 jours)

| Ordre | Action | Recommandation | Effet |
|---:|---|---|---|
| 11 | Rédiger les 12 encadrés « à rédiger » et les annexes A et F | REC-017 | Le document devient un rapport |
| 12 | Homogénéiser les libellés d'indicateurs sur la base du tableau 46 | REC-007 | Supprime les doubles définitions |
| 13 | Reprendre le résumé exécutif avec les quatre effectifs | REC-008 | Supprime l'ambiguïté majeure |
| 14 | Sourcer les seuils et rendre la grille des cas autoportante | REC-009 | Décisions de pertinence justifiées |
| 15 | Écrire le paragraphe sur le seul primaire conclusif (P3) | REC-010 | Restitue le résultat le plus fort |
| 16 | Commenter la variante « sans L6_recent » | REC-011 | Honnêteté de la sensibilité |
| 17 | Passer les six contrôles automatiques | REC-015 | Zéro défaut mécanique |

Le total des charges chiffrées dans les blocs de recommandation s'élève à **29 jours-personne** hors rédaction des chapitres, laquelle représente l'essentiel du reste à faire et ne peut pas être estimée par l'auditeur sans connaître l'ambition éditoriale du commanditaire. À titre indicatif, un rapport de 40 à 60 pages rédigé à partir de ce matériau demande 15 à 25 jours d'auteur.

> **REC-016 — Exécuter le tri des 78 onglets** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-016 |
| 2. Constat | 77 sorties pour 60 tableaux : le corps du rapport ne peut pas toutes les accueillir, et aucune règle de tri n'est écrite. |
| 3. Preuve | Partie C (78 décisions) ; 15 conserver, 19 simplifier, 15 figures, 5 synthèses, 23 annexes, 1 hors rapport. |
| 4. Axe | 2 — définition ; axe 6 |
| 5. Criticité | Majeur |
| 6. Cause probable | Le classeur a été construit comme un inventaire exhaustif, non comme un plan de publication. |
| 7. Effet | Le rapport contient 96 lignes pour un tableau, 24 lignes pour une composition à trois catégories et seize tableaux de fiche non numérotés. |
| 8. Recommandation | Appliquer les décisions A à E de la partie C ; ouvrir un journal de tri (onglet, décision, destination, motif) et le joindre en annexe G. |
| 9. Modalité | Auteur + producteur ; une passe de tri, puis contrôle du nombre d'objets par chapitre. |
| 10. Livrable | Plan de publication (60 → 39 tableaux, 15 figures nouvelles) + journal de tri. |
| 11. Effort | 2 jours-personne. |
| 12. Dépendance | REC-001. |
| 13. Clôture | 77/77 onglets affectés ; corps ≤ 40 tableaux ; 0 tableau de plus de 15 lignes dans le corps hors exceptions motivées. |
| 14. Statut | Ouvert. |

> **REC-017 — Rédiger le rapport, chapitre par chapitre, à partir d'une trame imposée** *(bloquant)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-017 |
| 2. Constat | Douze chapitres sur treize ne contiennent qu'un encadré « À rédiger — contenu attendu » ; l'annexe A et l'annexe F sont vides ; le résumé exécutif est vide. |
| 3. Preuve | Encadrés des tableaux 2, 5, 10, 16, 23, 26, 34, 39, 43, 49, 52, 59, 60, 61, 62 ; annexes A et F. |
| 4. Axe | 9 — complétude |
| 5. Criticité | Bloquant |
| 6. Cause probable | Maquette produite avant rédaction, avec un remplissage différé prévu. |
| 7. Effet | Le document n'est pas un rapport : c'est un recueil de tableaux commentés par leur légende. |
| 8. Recommandation | Imposer pour chaque chapitre une trame en quatre paragraphes : (1) ce que montre le tableau, en une phrase et avec les chiffres ; (2) ce que cela ne montre pas (limite, incertitude) ; (3) ce que cela implique pour l'action ; (4) ce qu'il faut vérifier. Interdire toute phrase d'effet sans intervalle de confiance. |
| 9. Modalité | Auteur ; rédaction chapitre par chapitre avec revue par l'auditeur sur les chapitres 6, 11 et 13 (les plus sensibles). |
| 10. Livrable | Rapport rédigé (40 à 60 pages) + résumé exécutif de 2 pages. |
| 11. Effort | 15 à 25 jours-auteur. |
| 12. Dépendance | Vagues 1 et 2 achevées (les chiffres doivent être arrêtés avant d'être commentés). |
| 13. Clôture | 0 occurrence de « à rédiger » ; chaque chapitre contient les quatre paragraphes ; chaque effet commenté est accompagné de son intervalle. |
| 14. Statut | Ouvert. |

> **REC-018 — Instituer une revue de validation avant diffusion** *(majeur)*

| Champ | Contenu |
|---|---|
| 1. Identifiant | REC-018 |
| 2. Constat | Aucune trace de revue interne : ni liste de contrôle, ni version validée, ni signature. |
| 3. Preuve | Absence d'annexe F renseignée ; absence de page de validation ; statut « maquette » du fichier. |
| 4. Axe | 1 — conformité |
| 5. Criticité | Majeur |
| 6. Cause probable | Chaîne de production individuelle sans point de contrôle formel. |
| 7. Effet | Les défauts détectés par cet audit l'ont été par un tiers externe, après dix jours de production. |
| 8. Recommandation | Trois signatures avant diffusion : producteur des données (exactitude), auteur (interprétation), commanditaire (périmètre). Chaque signature s'appuie sur la sortie des six contrôles automatiques. |
| 9. Modalité | Direction du programme ; procédure d'une page. |
| 10. Livrable | Page de validation + procédure de diffusion. |
| 11. Effort | 0,5 jour-personne. |
| 12. Dépendance | REC-015. |
| 13. Clôture | La version diffusée porte les trois signatures et la sortie de contrôle. |
| 14. Statut | Ouvert. |

## F.3 Verdict de l'audit

**Le rapport n'est pas diffusable en l'état.** Ce verdict ne porte pas sur la qualité du travail analytique, qui est élevée, mais sur cinq conditions non remplies.

1. **Une seule estimation principale**, retrouvée à l'identique dans le classeur (REC-004, REC-006).
2. **Une note de correction de T0** qui explique les deux valeurs modifiées (REC-003).
3. **Une correspondance traçable** entre chaque tableau et un onglet existant (REC-001, REC-014).
4. **Un appareil graphique sans figure vide ni titre tronqué** (REC-012).
5. **Une grille des cas reproductible** — lettre identique dans le rapport et dans le classeur, EMD identiques, table de décision publiée (REC-022).
6. **Un texte rédigé** — au minimum le résumé exécutif, les chapitres 6, 11 et 13, et l'annexe A (REC-017).

Les conditions 1 à 5 sont mécaniques et peuvent être levées en une douzaine de jours. La sixième est un travail éditorial de trois semaines. Rien dans cet audit ne suggère que les résultats eux-mêmes soient fragiles : les quatre intervalles de confiance contiennent zéro, aucune correction pour tests multiples ne laisse survivre un résultat, et le rapport le dit. Ce qui manque n'est pas la rigueur, c'est la finition — et, pour un document destiné à orienter une politique publique, la finition fait partie de la rigueur.

## F.4 Ce que l'audit recommande de ne pas faire

Trois tentations doivent être écartées.

**Ne pas « corriger » les valeurs divergentes en choisissant la plus favorable.** Les écarts entre 2,9 et 3,1 ou entre −3,6 et −3,1 ne changent aucune conclusion. Les aligner sur la valeur la plus flatteuse serait une faute, et l'aligner sur la plus défavorable serait une faute symétrique. Il faut trancher par la spécification, pas par le résultat.

**Ne pas supprimer les tableaux gênants.** Le tableau 41 dit que 57 % des variantes de l'indice de résultats ménages changent la conclusion ; la figure 11 dit qu'aucun indicateur secondaire ne survit à la correction de Benjamini-Hochberg ; la variante « sans L6_recent » triple l'effet sur P1. Ces trois éléments doivent rester et être commentés : ce sont eux qui donneront au rapport sa crédibilité.

**Ne pas attendre la version finale pour écrire l'annexe A.** C'est la seule pièce dont l'absence rend toutes les autres suspectes, parce qu'elle documente une correction qui, sans elle, ressemble à un ajustement des chiffres au résultat attendu.

---

# Annexes de l'audit

## Annexe 1 — Artefacts produits

| Fichier | Contenu |
|---|---|
| `Audit_rapport_quantitatif_SACO_Phase2_2026-10-20.docx` | Le présent rapport, en format bureautique (version de diffusion) |
| `Audit_SACO_Phase2_annexes_2026-10-20.xlsx` | Annexes techniques : synthèse chiffrée, 78 décisions, 66 appariements, 40 images, 22 recommandations |
| `audit/reconciliation.csv` | 66 appariements testés automatiquement : onglet, légende, nombre de lignes, nombre de valeurs comparées, nombre de divergences, premiers exemples |
| `audit/figures.csv` | Inventaire des figures : légende, image, dimensions, densité d'encre, encre sur les bords gauche et droit, nombre d'images par figure |
| `audit/data_partC.py` | Les 78 décisions de tri, avec diagnostic, destination et justification |
| `audit/reconcile.py`, `audit/figures.py` | Scripts de production des deux tableaux ci-dessus, réexécutables sur les fichiers audités |
| `audit/build_dump.py` | Reconstruction de l'accès aux 78 onglets (contournement d'une partie de dessin manquante) |
| `audit/make_docx.py` | Conversion du rapport en format bureautique |
| `README_AUDIT.md` | Mode d'emploi des livrables et procédure de reproduction |

## Annexe 2 — Convention des blocs de recommandation

Chaque recommandation comporte quatorze champs obligatoires : (1) identifiant ; (2) constat ; (3) preuve et localisation ; (4) axe d'audit ; (5) criticité ; (6) cause probable ; (7) effet sur la lecture ou le risque ; (8) recommandation ; (9) modalité de mise en œuvre ; (10) livrable attendu ; (11) charge ; (12) dépendances ; (13) critère de clôture vérifiable ; (14) statut.

## Annexe 3 — Récapitulatif des recommandations

| Réf. | Objet | Criticité | Charge (j-h) | Vague |
|---|---|---|---:|---:|
| REC-001 | Correspondance sorties ↔ tableaux | Bloquant | 2 | 1 |
| REC-002 | Nommage des onglets, sort de T24 | Majeur | 0,5 | 1 |
| REC-003 | Note de correction des valeurs de T0 | Bloquant | 1 | 1 |
| REC-004 | Estimation principale unique | Bloquant | 3 | 1 |
| REC-005 | Versionnage et horodatage des sorties | Majeur | 1 | 2 |
| REC-006 | Recalcul des tableaux dérivés | Bloquant | 3 | 2 |
| REC-007 | Dictionnaire d'indicateurs unique | Bloquant | 3 | 3 |
| REC-008 | Trois effectifs distingués | Majeur | 1 | 3 |
| REC-009 | Seuils sourcés, grille des cas autoportante | Majeur | 0,5 | 3 |
| REC-010 | Identifier le seul primaire conclusif | Bloquant | 0,5 | 3 |
| REC-011 | Traiter la variante « sans L6_recent » | Majeur | 0,5 | 3 |
| REC-012 | Reprise de l'appareil graphique | Bloquant | 3 | 2 |
| REC-013 | Refonte des fiches de zone | Majeur | 2 | 2 |
| REC-014 | Scripts, version, journal d'exécution | Bloquant | 2 | 2 |
| REC-015 | Contrôles automatiques de diffusion | Majeur | 2 | 3 |
| REC-016 | Exécution du tri des 78 onglets | Majeur | 2 | 1 |
| REC-017 | Rédaction du rapport | Bloquant | 15–25 | 3 |
| REC-018 | Revue de validation | Majeur | 0,5 | 3 |
| REC-019 | Déséquilibre initial et effet plafond des primaires d'offre | Majeur | 1 | 3 |
| REC-020 | Repondération de second niveau et publication des poids | Majeur | 1,5 | 2 |
| REC-021 | Règle de calcul de la co-couverture de la cascade | Majeur | 0,5 | 2 |
| REC-022 | Table de décision de la grille des cas, EMD alignées | Bloquant | 1 | 1 |

**Répartition :** 9 recommandations bloquantes, 13 majeures, 0 mineure. Charge totale chiffrée hors rédaction : 29 jours-personne.

## Annexe 4 — Fichiers audités et empreintes

| Fichier | Taille (octets) | SHA-256 (24 premiers caractères) |
|---|---:|---|
| `Rapport_resultats_quantitatifs_Phase2_SACO_Mpox_maquette_2026-10-19 (1).docx` | 7 470 917 | `31c0f40739baa5d84626016a` |
| `SACO_Phase2_Tableaux_2026-10-15 (2).xlsx` | 546 861 | `3ee1133d013fbd07b7373832` |

Toute version postérieure à ces empreintes doit être considérée comme non auditée. Les constats de la partie B sont attachés à l'état du 19 octobre 2026 ; ils n'ont pas vocation à être reportés sur une version ultérieure sans nouvelle vérification.
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
