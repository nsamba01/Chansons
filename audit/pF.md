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
