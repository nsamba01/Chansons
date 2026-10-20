# Audit du rapport quantitatif SACO Phase 2 (Mpox) — livrables

Audit indépendant, en français, du rapport `Rapport_resultats_quantitatifs_Phase2_SACO_Mpox_maquette_2026-10-19 (1).docx`
confronté à son classeur de sorties `SACO_Phase2_Tableaux_2026-10-15 (2).xlsx`.
Seconde passe : 20 octobre 2026.

## Documents

| Fichier | Contenu |
|---|---|
| `Audit_rapport_quantitatif_SACO_Phase2_2026-10-20.md` | Rapport d'audit complet (source, ~29 000 mots, 48 tableaux) : synthèse, méthode en 8 étapes, parties A à G, 22 blocs de recommandation à 14 champs, plan de correction en 3 vagues |
| `Audit_rapport_quantitatif_SACO_Phase2_2026-10-20.docx` | Même rapport, mis en forme pour diffusion |
| `Audit_SACO_Phase2_annexes_2026-10-20.xlsx` | Annexes techniques : synthèse chiffrée, 78 décisions de tri par onglet, 66 appariements, 40 images, 22 recommandations |

## Pièces justificatives (`audit/`)

| Fichier | Rôle |
|---|---|
| `build_dump.py` | Reconstruit l'accès aux 78 onglets (le classeur livré ne s'ouvre pas directement : partie de dessin manquante). Produit `/home/user/dump.json` |
| `reconcile.py` | Compare 66 tableaux du rapport aux onglets du classeur ; produit `reconciliation.csv` |
| `figures.py` | Inventaire des figures (dimensions, densité d'encre, encre sur les bords, doublons) ; produit `figures.csv` |
| `data_partC.py` | Les 78 décisions de tri (diagnostic, destination, justification) |
| `make_docx.py` | Conversion Markdown → DOCX du rapport |
| `p0.md` … `pG.md` | Sources du rapport, section par section |

## Reproduire

```bash
python3 -m venv .venv && .venv/bin/pip install python-docx openpyxl pillow
.venv/bin/python audit/build_dump.py        # dump.json depuis le classeur
.venv/bin/python audit/reconcile.py         # audit/reconciliation.csv
.venv/bin/python audit/figures.py           # audit/figures.csv
cat audit/p0.md audit/pA.md audit/pB.md audit/pC.md audit/pC_table.md \
    audit/pD.md audit/pE.md audit/pF.md audit/pG.md > Audit_rapport_quantitatif_SACO_Phase2_2026-10-20.md
.venv/bin/python audit/make_docx.py         # version bureautique
```

Les empreintes des fichiers audités (SHA-256, 24 premiers caractères) sont consignées à l'annexe 4 du rapport :
`31c0f40739baa5d84626016a` (docx) et `3ee1133d013fbd07b7373832` (xlsx). Toute version postérieure doit être considérée comme non auditée.
