# -*- coding: utf-8 -*-
import os, sys, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *
from docx.shared import Pt, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import c_a, c_b, c_c, c_d


def cover(doc):
    """Page de garde : image pleine page, mention de statut refaite."""
    body = doc.element.body
    p0 = body[0]
    for r in p0.findall(qn('w:r')):
        p0.remove(r)
    from docx.text.paragraph import Paragraph
    par = Paragraph(p0, doc)
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.space_after = Pt(0)
    par.paragraph_format.line_spacing = 1.0
    par.add_run().add_picture(f'{FIG}/cover.png', width=Cm(20.98), height=Cm(29.4))
    # le paragraphe porteur du saut de section ne doit pas ajouter de ligne
    from docx.text.paragraph import Paragraph as _P
    brk = _P(body[1], doc)
    brk.paragraph_format.space_before = Pt(0)
    brk.paragraph_format.space_after = Pt(0)
    from docx.enum.text import WD_LINE_SPACING
    brk.paragraph_format.line_spacing_rule = WD_LINE_SPACING.EXACTLY
    brk.paragraph_format.line_spacing = Pt(1)


def sommaire(doc):
    page_break(doc)
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(14)
    run(p, 'Sommaire', size=26, bold=True, color=NAVY)
    hr(doc)
    # champ TOC réel : Word le calcule à l'ouverture (updateFields = true)
    p = doc.add_paragraph()
    r = p.add_run()
    fld = OxmlElement('w:fldChar'); fld.set(qn('w:fldCharType'), 'begin'); r._r.append(fld)
    r2 = p.add_run()
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve')
    it.text = 'TOC \\o "1-2" \\h \\z \\u'
    r2._r.append(it)
    r3 = p.add_run()
    fld2 = OxmlElement('w:fldChar'); fld2.set(qn('w:fldCharType'), 'separate'); r3._r.append(fld2)
    r4 = p.add_run('Table des matières générée par Word. Elle se remplit à l’ouverture du document ; '
                   'sinon, clic droit sur ce paragraphe puis « Mettre à jour les champs ».')
    r4.font.size = Pt(9); r4.font.color.rgb = RGBColor.from_string(GREY); r4.italic = True
    r5 = p.add_run()
    fld3 = OxmlElement('w:fldChar'); fld3.set(qn('w:fldCharType'), 'end'); r5._r.append(fld3)

    # liste des chapitres, en clair, pour la lecture sur écran et pour l'impression sans mise à jour
    para(doc, "Chapitres", size=10, bold=True, color=NAVY, before=240, after=60, align='left')
    chapters = [
        ('Résumé exécutif', ''),
        ('1. Méthodologie', 'devis, bases, indicateurs, EMD, inférence à seize grappes'),
        ('2. Profil des échantillons et comparabilité', 'ménages, acteurs, équilibre, attrition'),
        ('3. Gouvernance communautaire', 'CODESA, transitions, conformité au PSN'),
        ('4. Acteurs communautaires', 'CAC, RECO, ASC, prime, logistique, genre'),
        ('5. Ménages', 'exposition, connaissances, vaccination, continuum maternel, Mpox'),
        ('6. Effet de l’intervention', 'tableau des effets, placebos, sensibilité, secondaires'),
        ('7. Mécanismes et analyse systémique', 'associations, différences premières, variance'),
        ('8. Équité', 'concentration, quintiles, hétérogénéité, genre'),
        ('9. Thématiques', 'Mpox, vaccination, enfant malade, santé maternelle'),
        ('10. Alignement avec le PSN SACO 2025-2030', 'vingt normes, indice de conformité'),
        ('11. Robustesse et limites', 'matrices de sensibilité, retrait de zone, validité'),
        ('12. Synthèse conjointe par dynamique', 'unités, zones, cas contrastés'),
        ('13. Discussion et recommandations', 'portée, recommandations, plan d’action'),
        ('Annexes', 'A note de méthode · B catalogue · C dictionnaire · D tableaux par zone · E fiches'),
    ]
    for t, s in chapters:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = Pt(12)
        run(p, t, size=9.6, bold=True, color=NAVY)
        if s:
            run(p, '  —  ' + s, size=8.6, color=GREY)


def avant_propos(doc):
    page_break(doc)
    h2(doc, "Comment lire ce rapport", number=None)
    para(doc, "Le rapport est organisé autour de quatre questions : ce qui a changé (chapitres 3 à 5), ce "
              "que l'appui a ajouté (chapitre 6), par quels mécanismes (chapitre 7), et pour qui (chapitre 8). "
              "Les chapitres 9 à 12 approfondissent des thèmes, l'alignement avec le plan national, la "
              "robustesse et les dynamiques de zone. Le chapitre 13 discute la portée des résultats et "
              "formule les recommandations. L'annexe A documente les corrections apportées par rapport à la "
              "version antérieure du rapport.")
    bullets(doc, [
        "**Chaque tableau porte un registre** : évolution, association ou attribution. Le registre figure "
        "dans le titre ou dans la note.",
        "**Chaque valeur est accompagnée de son intervalle et de son effectif**, sauf mention contraire.",
        "**Les valeurs de p ne sont jamais seules** : elles sont lues avec la taille d'effet, l'EMD et le "
        "seuil de pertinence.",
        "**Les pourcentages et les points de pourcentage ne sont pas confondus** : « +4,8 points » désigne "
        "un écart absolu, « +12 % » un écart relatif.",
        "**Les tableaux de détail par zone et par sous-groupe figurent en annexe D**, pour ne pas rompre la "
        "lecture ; les tableaux du corps présentent les résultats nécessaires à l'argument.",
        "**Aucune valeur n'a été modifiée à la main** : toutes proviennent du classeur d'analyse, et les "
        "écarts constatés sont documentés en annexe A plutôt que corrigés en silence.",
    ])
    para(doc, "Une note sur la pagination : le document a été produit à partir de la maquette Word fournie, "
              "qui ne conserve pas de pagination fixe. Le sommaire est un champ automatique : il se met à "
              "jour à l'ouverture ou par un clic droit, et les renvois de page doivent être vérifiés après "
              "la première mise à jour.", size=8.6, color=GREY)


def main(out):
    doc = load_template()
    cover(doc)
    sommaire(doc)
    avant_propos(doc)
    c_a.resume(doc)
    c_a.ch1(doc)
    c_a.ch2(doc)
    c_a.ch3(doc)
    c_a.ch4(doc)
    c_b.ch5(doc)
    c_b.ch6(doc)
    c_b.ch7(doc)
    c_b.ch8(doc)
    c_b.ch8_suite(doc)
    c_c.ch9(doc)
    c_c.ch10(doc)
    c_c.ch11(doc)
    c_c.ch12(doc)
    c_c.ch13(doc)
    c_d.annexes(doc)
    set_update_fields(doc)
    doc.save(out)
    print('écrit :', out, os.path.getsize(out), 'octets')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'Rapport_final.docx'))
