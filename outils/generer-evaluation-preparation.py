#!/usr/bin/env python3
"""Généralisation du modèle validé (leçon pilote 6e-h-t1-l1) : produit, pour une leçon, les fichiers
pedagogie/<id>/evaluation.html et pedagogie/<id>/preparation.html au format de la leçon pilote.

Sources :
  - la fiche de préparation de la leçon (outils/espace-enseignant/fiches_h.py et fiches_g.py pour la 6e,
    fiches_5e_h.py et fiches_5e_g.py pour la 5e) : situation analysée, séances, activités du professeur et réponses attendues,
    difficultés, différenciation, évaluation sur 20 avec corrigés et barèmes, valeurs ;
  - la leçon dans data/contenu.json (compétence, exemple de situation, habiletés et contenus) ;
  - pedagogie/<id>/questions.json : questions de compréhension et réponses attendues (rédigées pour la leçon) ;
  - pedagogie/<id>/eleve.html : plan de la trace écrite et conclusion (synthèse).
Les deux fichiers produits peuvent ensuite être retouchés à la main : le script refuse de les écraser
sans --forcer. Usage : python3 outils/generer-evaluation-preparation.py <id> [<id>…] [--forcer]
"""
import html as H
import json
import os
import re
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'outils', 'espace-enseignant'))
from fiches_h import FICHES as FH  # noqa: E402
from fiches_g import FICHES as FG  # noqa: E402
from fiches_5e_h import FICHES as F5H  # noqa: E402
from fiches_5e_g import FICHES as F5G  # noqa: E402

FICHES = dict(FH, **FG, **F5H, **F5G)


def pts(x):
    return ('%g' % x).replace('.', ',') + ' point' + ('s' if x >= 2 else '')


def ul(items):
    return '<ul>\n' + ''.join('<li>' + i + '</li>\n' for i in items) + '</ul>\n'


def tableau(entetes, lignes):
    return ('<div class="tbl"><table><thead><tr>' + ''.join('<th>' + e + '</th>' for e in entetes) + '</tr></thead><tbody>\n'
            + ''.join('<tr>' + ''.join('<td>' + c + '</td>' for c in l) + '</tr>\n' for l in lignes) + '</tbody></table></div>\n')


def corrige(contenu, titre='Corrigé et barème'):
    return '<details class="corrige"><summary>' + titre + '</summary><div class="corrige-body">' + contenu + '</div></details>'


def lecon(D, lid):
    for c in D['classes']:
        for d in c['disciplines']:
            for t in d['themes']:
                for l in t['lecons']:
                    if l['id'] == lid:
                        return c, d, t, l
    sys.exit('leçon inconnue : ' + lid)


def evaluation(l, F, Q):
    E = F['evaluation']
    h = ('<p class="chapo-bloc">Évaluation sur 20 points, conforme à la méthodologie APC : activités d\'application sur 8 points et '
         'situation d\'évaluation sur 12 points. Durée conseillée : 40 minutes. Les questions de compréhension servent à vérifier '
         'les acquis pendant ou après la séance et ne sont pas notées.</p>\n\n')
    h += '<h4>Questions de compréhension <span class="badge">non notées</span></h4>\n<ol>\n'
    h += ''.join('<li>' + q + '</li>\n' for q, _ in Q['comprehension']) + '</ol>\n'
    h += corrige('\n<ol>\n' + ''.join('<li>' + a + '</li>\n' for _, a in Q['comprehension']) + '</ol>', 'Réponses attendues') + '\n\n'
    h += '<h4>Activités d\'application <span class="badge">8 points</span></h4>\n'
    tot = 0
    for k, (enonce, p, cor) in enumerate(E['activites']):
        tot += p
        h += ('<section class="exo"><div class="enonce"><p><strong>Exercice ' + str(k + 1) + ' (' + pts(p) + ').</strong> ' + enonce + '</p></div>'
              + corrige('<p>' + cor + '</p>') + '</section>\n')
    assert tot == 8, (l['id'], 'activités', tot)
    h += '\n<h4>Situation d\'évaluation <span class="badge">12 points</span></h4>\n'
    h += '<div class="situation"><div class="texte"><p>' + E['situation'] + '</p></div></div>\n<p><strong>Consignes :</strong></p>\n<ol>\n'
    h += ''.join('<li>' + c + ' <em>(' + pts(p) + ')</em></li>\n' for c, p, _ in E['consignes']) + '</ol>\n'
    assert sum(p for _, p, _ in E['consignes']) == 10, (l['id'], 'consignes')
    h += corrige(''.join('<p><strong>Consigne ' + str(k + 1) + ' (' + pts(p) + ') :</strong> ' + c + '</p>' for k, (_, p, c) in enumerate(E['consignes'])),
                 'Corrigé de la situation d\'évaluation') + '\n'
    h += '<h5>Comment attribuer les points</h5>\n' + tableau(['Critère', 'Ce que l\'on vérifie', 'Points'], [
        ['CM1 – Pertinence', 'Chaque réponse correspond à la consigne posée.', 'compris dans les consignes'],
        ['CM2 – Utilisation correcte des outils de la discipline', 'Notions, dates, lieux, vocabulaire et calculs exacts.', 'compris dans les consignes'],
        ['CM3 – Cohérence de la production', 'Réponses logiques, ordonnées, sans contradiction.', '1'],
        ['CP – Critère de perfectionnement', 'Présentation soignée, orthographe correcte, originalité de la proposition.', '1'],
        ['<strong>Total</strong>', 'Consignes 10 points + cohérence 1 point + perfectionnement 1 point.', '<strong>12</strong>']])
    h += ('<p class="conseil">Barème : on accorde les points dès que l\'idée juste est exprimée, même maladroitement ; une réponse fausse ou '
          'absente vaut 0 (pas de point négatif). Les corrigés indiquent les réponses attendues, pas la seule formulation acceptée.</p>\n')
    return h


def preparation(c, d, t, l, F, Q, eleve):
    sit = l['situation']
    comp = re.search(r'<strong>(Compétence[^<]*?) ?:?</strong>\s*:?\s*(.*?)</p>', sit, re.S)
    exemple = re.search(r'<strong>Exemple de situation ?:</strong>\s*(.*?)</p>', sit, re.S)
    hab = re.findall(r'<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>', sit, re.S)
    nb = len(F['seances'])
    h = tableau([], [])[:0]
    h = '<div class="tbl"><table><tbody>\n' + ''.join('<tr><th>' + a + '</th><td>' + b + '</td></tr>\n' for a, b in [
        ('Discipline', 'Histoire-Géographie (' + d['nom'] + ')'), ('Classe', c['id']),
        ('Thème ' + str(t['n']) if t.get('n') else 'Thème', t['titre']), ('Leçon ' + str(l['n']), l['titre']),
        ('Durée', str(l['duree']) + ' heure' + ('s' if l['duree'] > 1 else '') + ' : ' + str(nb) + ' séance' + ('s' if nb > 1 else '') + ' de 1 heure (55 minutes utiles chacune)'),
        ('Compétence', (comp.group(1).strip() + ' : ' + comp.group(2).strip()) if comp else '—')]) + '</tbody></table></div>\n\n'
    h += '<h4>Habiletés et contenus</h4>\n' + tableau(['Habiletés', 'Contenus'], [[a.strip(), b.strip()] for a, b in hab]) + '\n'
    h += '<h4>Situation d\'apprentissage</h4>\n<p>' + (exemple.group(1).strip() if exemple else '') + '</p>\n'
    h += ('<p><strong>Analyse de la situation.</strong> Contexte : ' + F['contexte'] + ' Circonstance : ' + F['circonstance']
          + ' Tâches des élèves : ' + ' ; '.join(F['taches']) + '.</p>\n')
    h += '<p class="conseil"><strong>Adaptation conseillée :</strong> remplacer les noms de lieux et d\'établissement par ceux de votre localité ; la situation fonctionne mieux lorsque les élèves s\'y reconnaissent.</p>\n\n'
    h += '<h4>Prérequis à vérifier</h4>\n' + ul(F['prerequis'])
    h += '<h4>Matériel didactique</h4>\n' + ul([m[0].upper() + m[1:] + '.' for m in F['materiel']])
    strategies = []
    for s in F['seances']:
        for e in s['etapes']:
            x = e[2][0].lower() + e[2][1:]
            if x not in strategies:
                strategies.append(x)
    h += ('<h4>Stratégie pédagogique</h4>\n<p>Démarche active : les élèves découvrent les notions à partir de la situation, de documents et '
          'd\'exemples proches de leur vie, avant que l\'enseignant ne les formalise dans la trace écrite. Techniques utilisées : '
          + ' ; '.join(strategies) + '.</p>\n\n')
    # tableau synthétique du déroulement
    h += '<h4>Déroulement de la séance</h4>\n'
    h += ('<p class="conseil">' + str(nb) + ' séance' + ('s' if nb > 1 else '') + ' de 1 heure (55 minutes utiles). Le tableau donne la vue d\'ensemble ; '
          'le déroulé détaillé qui suit donne, étape par étape, les consignes de l\'enseignant et les réponses attendues des élèves.</p>\n')
    lignes = []
    for i, s in enumerate(F['seances']):
        assert sum(e[1] for e in s['etapes']) == 55, (l['id'], i)
        for (moment, duree, strat, prof, eleves, trace) in s['etapes']:
            lignes.append(['<strong>' + ('Séance ' + str(i + 1) + ' · ' if nb > 1 else '') + moment + '</strong><br>' + str(duree) + ' min',
                           strat[0].upper() + strat[1:] + '.', ' '.join(prof), trace or '—'])
    h += tableau(['Moment et durée', 'Stratégie', 'Activités de l\'enseignant', 'Trace écrite'], lignes) + '\n'
    h += '<h4>Déroulé détaillé, avec les réponses attendues</h4>\n'
    h += '<p class="conseil">Les réponses attendues sont des repères : on accepte toute formulation juste des élèves.</p>\n'
    for i, s in enumerate(F['seances']):
        h += '<h5>Séance ' + str(i + 1) + ' · ' + s['titre'] + ' (55 min)</h5>\n'
        h += tableau(['Étape et durée', 'Ce que fait l\'enseignant', 'Réponses attendues des élèves'], [
            ['<strong>' + m + '</strong><br>' + str(du) + ' min<br><small>' + st[0].upper() + st[1:] + '</small>', ' '.join(pr), ' '.join(el)]
            for (m, du, st, pr, el, tr) in s['etapes']])
    h += '\n<h4>Questions de vérification (au fil de la séance)</h4>\n<ol>\n' + ''.join('<li>' + q + '</li>\n' for q, _ in Q['comprehension']) + '</ol>\n'
    h += '<p class="conseil">Les réponses attendues sont données dans l\'espace Élève, rubrique « Évaluation », sous « Questions de compréhension ».</p>\n\n'
    concl = re.search(r'<h3>Conclusion</h3>\s*(<p>.*?</p>)', eleve, re.S)
    h += '<h4>Synthèse</h4>\n' + (concl.group(1) if concl else '') + '\n\n'
    h += ('<h4>Évaluation</h4>\n<p>Évaluation formative pendant la séance (activités d\'application de la trace écrite, questions de vérification) ; '
          'évaluation sommative sur 20 points proposée dans l\'espace Élève, rubrique « Évaluation » (activités d\'application sur 8 points, '
          'situation d\'évaluation sur 12 points, avec corrigés et barème). Le quiz de la leçon (8 questions) peut servir de révision.</p>\n\n')
    h += '<h4>Remédiation</h4>\n' + tableau(['Difficulté constatée', 'Activité de remédiation'], F['difficultes'])
    h += '<h4>Différenciation pédagogique</h4>\n<p><strong>Pour les élèves en difficulté :</strong></p>\n' + ul(F['soutien'])
    h += '<p><strong>Pour les élèves avancés :</strong></p>\n' + ul(F['approfondissement'])
    h += '<h4>Éducation aux valeurs et liens avec les autres disciplines</h4>\n' + ul(F['valeurs'])
    h += ('<p class="conseil"><strong>Source :</strong> déroulement, réponses attendues, remédiation et évaluation repris de la fiche de préparation '
          'de l\'espace enseignant de la ' + c['id'] + ' (2026) et harmonisés avec la trace écrite de la leçon.</p>\n')
    return h


def main():
    ids = [a for a in sys.argv[1:] if not a.startswith('--')]
    forcer = '--forcer' in sys.argv
    D = json.load(open(os.path.join(R, 'data', 'contenu.json'), encoding='utf-8'))
    for lid in ids:
        c, d, t, l = lecon(D, lid)
        dos = os.path.join(R, 'pedagogie', lid)
        Q = json.load(open(os.path.join(dos, 'questions.json'), encoding='utf-8'))
        eleve = open(os.path.join(dos, 'eleve.html'), encoding='utf-8').read()
        F = FICHES[lid]
        for nom, contenu in (('evaluation', evaluation(l, F, Q)), ('preparation', preparation(c, d, t, l, F, Q, eleve))):
            p = os.path.join(dos, nom + '.html')
            if os.path.exists(p) and not forcer:
                print('existe déjà (non écrasé, --forcer pour régénérer) :', os.path.relpath(p, R))
                continue
            open(p, 'w', encoding='utf-8').write(contenu)
            print('écrit :', os.path.relpath(p, R), len(contenu), 'caractères')


if __name__ == '__main__':
    main()
