# Registre des écarts non résolus — rapport SACO Phase 2 (Mpox)

Document de travail, **hors rapport**. Il consigne les incohérences détectées dans le classeur
d'analyse et dans la maquette qui n'ont **pas** été corrigées dans le rapport final, soit parce
qu'elles relèvent d'un arbitrage méthodologique, soit parce qu'elles nécessitent un retour au
producteur des données. Chaque ligne indique la source, l'écart, la décision prise dans le rapport
et l'action attendue.

| # | Source | Écart constaté | Décision dans le rapport | Action attendue |
|---|---|---|---|---|
| 1 | `T14_cac_3volets` vs `T25_tableau_des_effets` | Fonctionnalité des CAC à T1 en intervention : 79,5 dans T14, 79,4 dans T25 (0,1 point) | Valeur de T25 retenue (tableau des effets), écart consigné en annexe A | Harmoniser l'arrondi dans le classeur |
| 2 | `T14_men_3volets` vs `T25` | P1 témoin T0 : 65,3 (T14) et 65,3 (T25) mais T1 69,3 contre 69,3 ; P9 : écart de 0,1 sur deux cellules | Valeurs de T25 retenues pour les effets, T14 pour les niveaux | Recalculer T14 depuis la table de base |
| 3 | `T05_dates_collecte` | 13 entretiens ménages T0 et 11 à T1 hors fenêtre, dont des dates de 2022 et 2023 | Conservés dans l'analyse principale, retirés dans une variante | Vérifier la saisie des dates ; documenter la procédure de nettoyage |
| 4 | `T01_bilan_appariement` | Base « ménages » : 688 unités à T0, 385 appariées (56 %), alors que 5 713 ménages ont été enquêtés | L'unité appariée est la grappe, non le ménage ; le rapport le précise | Renommer la ligne « grappes de ménages » dans le classeur |
| 5 | `T41_enfant_malade_distributions` | Les quatre lignes « Délai de consultation » sont vides | Non publiées ; le délai est traité par `T43` | Compléter l'onglet ou le retirer |
| 6 | `T45_mpox_cap` | Effectifs variables selon les items (590 à 823), sans colonne de dénominateur commun | Effectifs publiés par item | Ajouter une colonne de dénominateur |
| 7 | `T48_asc_prime_montant` | 16 à 28 ASC par bras et par passage seulement | Publié avec avertissement sur la taille des effectifs | Élargir la base ASC ou signaler comme indicatif |
| 8 | `T51_normes_psn` | 18 normes sur 20 sans cible chiffrée dans le PSN ; la conformité ne peut pas être « atteinte » | Lecture en niveau et en évolution, jamais en taux d'atteinte | Faire préciser les cibles par le niveau national |
| 9 | Maquette, figure 15 | Cascade maternelle vide | Figure reconstruite depuis `T40`, produit et co-couverture distingués | — |
| 10 | Maquette, résumé exécutif | P1 2,9 [−4,4 ; 10,3] (variante d'imputation) ; P2 −3,6 (variante de tendance) ; P3 et P4 issues du modèle à effets fixes | Valeurs du tableau des effets rétablies, corrections listées en annexe A | — |
| 11 | Maquette, numérotation | Absence de tableau 25 ; tableau 45 en double ; 16 fiches non numérotées | Numérotation continue 1–48, annexes A1–D5 | — |
| 12 | Maquette, pagination | Aucune pagination conservée dans le fichier | Sommaire en champ automatique ; pagination à recalculer | Mettre à jour le sommaire dans Word |
| 13 | `T53` (toutes primaires) | Changements de conclusion D↔E dans 0 à 6 variantes selon l'indicateur | Signalés explicitement au chapitre 11 ; aucun effet établi dans aucune variante | Documenter la règle de classement D/E |
| 14 | `T39` vs `T40` | Les niveaux (37,3 % de CPN4+) et les probabilités conditionnelles (41,5 % parmi les CPN1) ne sont pas superposables | Les deux sont publiés, avec la base de chaque calcul | Ajouter la base dans le titre des colonnes |

## Points de méthode à trancher avant la phase 3

1. **Unité d'analyse** : l'aire de santé porte l'essentiel de la variance (ICC 0,29 à 0,57) ; le devis
   par zone sous-dimensionne la puissance.
2. **Indicateur de résultat vaccinal** : la déclaration surestime de 26 à 55 points selon la province ;
   seul le carnet vu est défendable.
3. **Conformité et activité** : l'indice de conformité n'est pas associé aux extrants (RT 1,00) ;
   il ne peut pas servir d'indicateur de performance.

## Fichiers

- `Rapport_final_resultats_quantitatifs_Phase2_SACO_Mpox_2026-10-21.docx` — rapport final.
- `audit/final/` — scripts d'assemblage (`build.py`, `base.py`, `c_a.py` à `c_d.py`, `figs.py`) et figures.
- `Audit_rapport_quantitatif_SACO_Phase2_2026-10-20.docx` — audit de référence (35 écarts, 25 REC).
