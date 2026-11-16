#!/usr/bin/env python3
"""Insère les 11 photographies validées le 16/11/2026 dans la leçon pilote 6e-h-t1-l1.
Exécution unique (le script refuse de s'appliquer deux fois). Statue d'Ibn Khaldoun exclue (suspendue).
"""
import html
import json
import os
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(R, 'pedagogie', '6e-h-t1-l1')
CR = {c['id']: c for c in json.load(open(os.path.join(R, 'illustrations', 'selection', 'credits.json'), encoding='utf-8'))}
e = html.escape

PHOTOS = {
    'herodote': ("Photo 1 – Buste d'Hérodote.", "Buste en marbre, copie romaine du IIe siècle après J.-C. d'une statue grecque ; le nom ΗΡΟΔΟΤΟΣ (Hérodote) est gravé sur le socle.",
                 "Crédit : Metropolitan Museum of Art, New York — CC0 (domaine public) — Wikimedia Commons.",
                 "Buste en marbre blanc d'un homme barbu aux cheveux bouclés, avec le nom Hérodote gravé en grec sur le socle.",
                 "Ce buste a été sculpté des siècles après la mort d'Hérodote : c'est une image imaginée, pas un portrait fait de son vivant. Même une statue doit être critiquée comme une source."),
    'pierre-palerme': ("Photo 2 – La pierre de Palerme.", "Fragment de pierre gravé de hiéroglyphes : annales des rois de l'Égypte ancienne (IIIe millénaire avant J.-C.), conservé au musée archéologique de Palerme (Italie).",
                       "Crédit : photo CvZ — CC BY-SA 4.0 — Wikimedia Commons (image redimensionnée).",
                       "Fragment de pierre noire couvert de lignes de hiéroglyphes égyptiens.",
                       "Bien avant Hérodote, les Égyptiens notaient les évènements de chaque année de règne de leurs rois : d'autres civilisations avaient leurs propres façons de conserver le passé."),
    'poids-akan': ("Photo 3 – Poids akan à peser l'or.", "Poids en laiton fabriqués par les Akan (Côte d'Ivoire et Ghana actuels) pour peser la poudre d'or ; muséum de Toulouse (France).",
                   "Crédit : photo Didier Descouens — CC BY-SA 4.0 — Wikimedia Commons (image redimensionnée).",
                   "Petits poids en métal doré en forme de têtes d'animaux à cornes, de masques et d'objets, présentés sur fond noir.",
                   "Ces objets servaient au commerce de l'or : ils témoignent de la vie économique des Akan. Leurs formes renseignent aussi sur leurs croyances et leurs proverbes."),
    'masque-dan': ("Photo 4 – Masque dan.", "Masque du peuple dan, dans l'ouest de la Côte d'Ivoire.",
                   "Crédit : photo Roman Bonnefoy — CC BY-SA 4.0 — Wikimedia Commons (image redimensionnée).",
                   "Masque sculpté au visage ovale et lisse, aux yeux étroits, orné de coquillages et de fibres.",
                   "Les masques appartiennent à la vie culturelle et religieuse : ils sont utilisés lors des cérémonies et renseignent l'historien sur les croyances et l'organisation de la société."),
    'manuscrits-tombouctou': ("Photo 5 – Manuscrits de Tombouctou.", "Pages de manuscrits anciens de Tombouctou (Mali), écrits en arabe, consacrées à l'astronomie et aux mathématiques.",
                              "Crédit : photo Elias Altmimi, 2007 — domaine public — Wikimedia Commons.",
                              "Deux pages de manuscrit jaunies, couvertes d'écriture arabe et de cercles dessinés à l'encre rouge et noire.",
                              "Source écrite : ces manuscrits prouvent que l'écrit existait en Afrique de l'Ouest bien avant la colonisation."),
    'griot-gravure': ("Photo 6 – Un griot au XIXe siècle.", "« Griot de Niantanso », gravure publiée en 1872 dans le récit de voyage de l'explorateur français Eugène Mage.",
                      "Crédit : gravure d'après Eugène Mage, 1872 — domaine public — New York Public Library, via Wikimedia Commons.",
                      "Gravure en noir et blanc d'un homme assis tenant un grand instrument de musique à cordes.",
                      "Le griot transmet le passé par la parole et la musique : c'est un détenteur de la tradition orale. La gravure est elle-même une source iconographique, réalisée d'après le regard d'un voyageur européen."),
    'fouille-yagala': ("Photo 7 – Une fouille archéologique.", "Fouille de l'abri sous roche de Yagala (Sierra Leone) en 1967 : l'archéologue dégage les objets laissés par les hommes de la préhistoire.",
                       "Crédit : photo John Atherton, 1967 — CC BY-SA 2.0 — Wikimedia Commons (image redimensionnée).",
                       "Photographie en noir et blanc d'un archéologue accroupi qui creuse le sol entre de gros rochers.",
                       "Les fouilles fournissent des sources matérielles (outils, poteries) pour les périodes sans écrits. En Côte d'Ivoire, le site d'Anyama a été étudié de la même manière."),
    'grand-bassam': ("Photo 8 – Grand-Bassam, ville historique.", "Maison de l'époque coloniale dans le quartier historique de Grand-Bassam, première capitale de la colonie de Côte d'Ivoire.",
                     "Crédit : photo Joker-x — CC BY-SA 3.0 — Wikimedia Commons (image redimensionnée).",
                     "Grande maison coloniale à arcades et à étage, entourée de palmiers.",
                     "Les bâtiments anciens sont des traces du passé. Grand-Bassam est inscrite au patrimoine mondial de l'UNESCO depuis 2012 : connaître son histoire aide à la protéger."),
    'mosquee-kong-1892': ("Document 3 a – « Une mosquée de Kong », 1892.", "Gravure d'Édouard Riou publiée en 1892 dans le récit de l'explorateur Louis-Gustave Binger, Du Niger au golfe de Guinée par le pays de Kong et le Mossi (voyage de 1887 – 1889).",
                          "Crédit : gravure d'Édouard Riou, 1892 — domaine public — New York Public Library, via Wikimedia Commons.",
                          "Gravure en noir et blanc d'une mosquée en terre hérissée de pieux, entourée d'arbres, avec quelques personnages au premier plan.",
                          "Le dessinateur, Édouard Riou, n'a pas fait le voyage : il a travaillé en France, d'après les croquis et le récit de Binger. L'image peut donc contenir des erreurs ou des embellissements."),
    'mosquee-kong': ("Document 3 b – La mosquée de Kong en 2002.", "Mosquée de style soudanais de Kong (nord de la Côte d'Ivoire), construite en terre crue et renforcée de pieux de bois.",
                     "Crédit : photo Ivoire8 — CC BY-SA 3.0 — Wikimedia Commons (image redimensionnée).",
                     "Photographie en couleur d'une mosquée en terre aux tours pointues hérissées de pieux, devant un palmier.",
                     "Les mosquées de style soudanais du nord ivoirien, dont celles de Kong, sont inscrites au patrimoine mondial de l'UNESCO depuis 2021."),
    'koras': ("Photo 9 – Koras mandingues.", "Koras, harpes-luths à 21 cordes des griots du monde mandingue, exposées dans un musée.",
              "Crédit : photo Mouha.ibs — CC BY-SA 4.0 — Wikimedia Commons (image redimensionnée).",
              "Trois instruments à cordes au long manche et à grosse caisse ronde, posés contre un mur blanc.",
              "La kora accompagne les récits des griots : généalogies, épopées comme celle de Soundiata, louanges. L'instrument lui-même est une source matérielle sur la culture mandingue."),
}


def fig(pid):
    titre, legende, credit, alt, expl = PHOTOS[pid]
    c = CR[pid]
    return (f'<figure class="photo"><img src="img/6e-h-t1-l1/{pid}.jpg" alt="{e(alt)}" width="{c["largeur"]}" height="{c["hauteur"]}" loading="lazy" decoding="async">'
            f'<figcaption><b>{e(titre)}</b> {e(legende)} <span class="credit">{e(credit)}</span></figcaption></figure>\n'
            f'<p class="illus-expl">{e(expl)}</p>\n')


def inserer(fichier, apres, ids, avant=False, bloc=None):
    p = os.path.join(P, fichier)
    s = open(p, encoding='utf-8').read()
    if 'img/6e-h-t1-l1/' + ids[0] + '.jpg' in s:
        sys.exit(f'{fichier} : photos déjà insérées ({ids[0]})')
    assert s.count(apres) == 1, (fichier, apres[:60])
    ajout = bloc if bloc is not None else ''.join(fig(i) for i in ids)
    s = s.replace(apres, (ajout + apres) if avant else (apres + '\n' + ajout))
    open(p, 'w', encoding='utf-8').write(s)


# --- Espace Élève (trace écrite) ---
inserer('eleve.html', "et en Afrique de l'Ouest les griots transmettaient les généalogies et les récits des royaumes.</p>", ['herodote', 'pierre-palerme'])
inserer('eleve.html', "sont tous des sujets d'histoire.</p>", ['poids-akan', 'masque-dan'])
inserer('eleve.html', "(peintures, photographies, cartes anciennes).</p>", ['manuscrits-tombouctou', 'griot-gravure', 'fouille-yagala'])
inserer('eleve.html', "les frontières actuelles du pays ont été tracées pendant la colonisation.</p>", ['grand-bassam'])

# --- Espace Enseignant : document 3 (comparaison des deux images de Kong) ---
doc3 = ('<p><strong>Document 3 – La mosquée de Kong, d\'hier à aujourd\'hui</strong> (comparaison de deux sources iconographiques).</p>\n'
        + fig('mosquee-kong-1892') + fig('mosquee-kong') +
        '<p><em>Commentaire.</em> La comparaison est un exercice simple de critique des sources, accessible en 6e. On fait identifier pour chaque image : '
        'sa nature (gravure / photographie), son auteur, sa date et le contexte de sa production (récit d\'exploration publié en France en 1892 ; photographie d\'un habitant en 2002). '
        'On fait ensuite relever les ressemblances (forme générale, pieux de bois, terre crue) et les différences. Conclusion attendue : une image n\'est pas une copie exacte de la réalité ; '
        'il faut savoir qui l\'a produite, quand et dans quel but, et la confronter à d\'autres sources. Prolongement : la mosquée de Kong a été détruite lors des guerres de la fin du XIXe siècle puis reconstruite, '
        'ce qui explique aussi certaines différences ; ce point peut être vérifié dans les ouvrages de la bibliographie avant d\'être présenté en classe.</p>\n'
        '<p><em>Questions possibles.</em> 1. Quelle image est la plus ancienne ? 2. Qui a produit chaque image ? 3. Relève deux ressemblances et une différence. 4. Peut-on se fier entièrement à la gravure ? Pourquoi ?</p>\n')
inserer('enseignant.html', '<p><strong>Schémas 1 et 2 de la trace écrite.</strong>', ['mosquee-kong-1892'], avant=True, bloc=doc3)

# --- Espace Culture générale : koras (rubrique 7) et crédits complets (rubrique 9) ---
inserer('culture.html', "il est plus juste de dire que beaucoup de sociétés transmettaient surtout leur passé par la parole.</p>", ['koras'])
ordre = ['herodote', 'pierre-palerme', 'poids-akan', 'masque-dan', 'manuscrits-tombouctou', 'griot-gravure', 'fouille-yagala', 'grand-bassam', 'mosquee-kong-1892', 'mosquee-kong', 'koras']
lignes = ''.join(
    f'<tr><td>{e(PHOTOS[i][0].rstrip("."))}</td><td>{e(CR[i]["fichier_commons"].replace("File:", ""))}</td><td>{e(PHOTOS[i][2].replace("Crédit : ", "").split(" — ")[0])}</td>'
    f'<td>{e(CR[i]["licence"])}{(" (" + e(CR[i]["licence_url"]) + ")") if CR[i]["licence_url"] else ""}</td><td>{e(CR[i]["page_commons"])}</td></tr>' for i in ordre)
credits = ('<h5>Crédits des illustrations</h5>\n<p>Photographies validées par le porteur du projet le 16/11/2026 ; licences contrôlées sur les fiches originales de Wikimedia Commons le même jour '
           '(aucune alerte). Les images sous licence CC BY-SA ont été redimensionnées pour les téléphones : ces versions modifiées sont diffusées sous la même licence.</p>\n'
           '<div class="tbl credits"><table><thead><tr><th>Illustration</th><th>Titre du fichier</th><th>Auteur</th><th>Licence</th><th>Source</th></tr></thead><tbody>'
           + lignes + '</tbody></table></div>\n')
inserer('culture.html', '<p class="conseil"><strong>Sources utilisées pour cette leçon :</strong>', ['__credits__'], avant=True, bloc=credits)
print('11 photographies insérées.')
