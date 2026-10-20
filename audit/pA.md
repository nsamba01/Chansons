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
