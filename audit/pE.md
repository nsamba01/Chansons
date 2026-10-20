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
