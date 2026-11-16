# Construit l\'Espace enseignant de 6e et l\'ajoute à data/contenu.json
# Usage : python3 construire.py <chemin/contenu.json>
import json, re, sys, html as H
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiches_h import FICHES as FH
from fiches_g import FICHES as FG
from guide import guide_html

FICHES = {}
FICHES.update(FH); FICHES.update(FG)

def txt(s):
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()

def ul(items):
    return '<ul>\n' + ''.join('<li>' + i + '</li>\n' for i in items) + '</ul>\n'

def tableau(entetes, lignes):
    h = '<div class="tbl"><table>\n<thead><tr>' + ''.join('<th>' + e + '</th>' for e in entetes) + '</tr></thead>\n<tbody>'
    for l in lignes:
        h += '<tr>' + ''.join('<td>' + c + '</td>' for c in l) + '</tr>\n'
    return h + '</tbody></table></div>\n'

def corrige(contenu, titre='Corrigé'):
    return '<details class="corrige"><summary>' + titre + '</summary><div class="corrige-body">' + contenu + '</div></details>'

def pts(x):
    return (('%g' % x).replace('.', ',')) + ' pt' + ('s' if x >= 2 else '')

def min_fr(m):
    return str(m) + ' min'

def plan_trace(cours):
    c = re.sub(r'<aside class="appli">.*?</aside>', '', cours, flags=re.S)
    out, cur = [], None
    for m in re.finditer(r'<(h[345])>(.*?)</\1>', c, re.S):
        t = m.group(2)
        if m.group(1) == 'h4':
            cur = [t, []]; out.append(cur)
        elif m.group(1) == 'h5' and cur:
            cur[1].append(t)
    h = '<ul>\n<li>Introduction</li>\n'
    for t, subs in out:
        h += '<li><strong>' + t + '</strong>' + (ul(subs) if subs else '') + '</li>\n'
    return h + '<li>Conclusion</li>\n</ul>\n'

def habiletes(situation):
    rows = re.findall(r'<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>', situation, re.S)
    res = []
    for a, b in rows:
        b = b.strip()
        if b.startswith(('La ', 'Le ', 'Les ', 'L&#39;', "L'", 'Des ', 'Un ', 'Une ')):
            b = b[0].lower() + b[1:]
        res.append(a.strip().lower().capitalize() + ' ' + b + ' ;')
    if res:
        res[-1] = res[-1][:-2] + '.'
    return res

def fiche(classe, disc, theme, l, F):
    nb_s = len(F['seances'])
    assert nb_s == l['duree'], (l['id'], nb_s, l['duree'])
    h = '<p><em>Fiche de préparation détaillée, conforme à l\'approche par les compétences (APC), à adapter à votre classe. Elle accompagne la leçon de l\'élève : la trace écrite à faire copier se trouve dans le cours.</em></p>\n'
    h += '<p><a href="#l-' + l['id'] + '">→ Ouvrir la leçon de l\'élève (cours, activités, exercices)</a></p>\n'
    h += '<h3>Fiche d\'identification</h3>\n'
    h += tableau(['Rubrique', 'Renseignement'], [
        ['Classe', classe['nom'] + ' (' + classe['id'] + ')'],
        ['Discipline', disc['nom']],
        ['Thème', 'Thème ' + str(theme['n']) + ' : ' + theme['titre']],
        ['Leçon', 'Leçon ' + str(l['n']) + ' : ' + l['titre']],
        ['Volume horaire', str(l['duree']) + ' h, soit ' + str(nb_s) + ' séance' + ('s' if nb_s > 1 else '') + ' de 55 min'],
        ['Supports et matériel', ' ; '.join(F['materiel'])],
        ['Bibliographie', 'Programme éducatif et guide d\'exécution d\'Histoire-Géographie, classe de 6e (MENA, Côte d\'Ivoire) ; manuel d\'Histoire-Géographie de 6e en usage dans l\'établissement ; ' + F.get('biblio', 'cours de l\'application « Histoire géographie premier cycle »')],
    ])
    h += '<h3>1. Compétence, situation et habiletés</h3>\n' + l['situation']
    h += '<h4>Analyse de la situation d\'apprentissage</h4>\n'
    h += ul(['<strong>Contexte :</strong> ' + F['contexte'],
             '<strong>Circonstance :</strong> ' + F['circonstance'],
             '<strong>Tâches des élèves :</strong> ' + ' ; '.join(F['taches']) + '.'])
    h += '<h3>2. Objectifs de la leçon</h3>\n<p>À la fin de la leçon, l\'élève doit être capable de :</p>\n' + ul(habiletes(l['situation']))
    h += '<h3>3. Prérequis à vérifier</h3>\n' + ul(F['prerequis'])
    h += '<h3>4. Plan de la trace écrite</h3>\n' + plan_trace(l['cours'])
    h += '<h3>5. Déroulement détaillé</h3>\n'
    h += '<p>Repères : présentation 10 min environ, développement 35 min, évaluation 10 min par séance. Les réponses attendues guident la correction orale ; la trace écrite est dictée ou recopiée à la fin de chaque partie.</p>\n'
    for i, s in enumerate(F['seances']):
        assert sum(e[1] for e in s['etapes']) == 55, (l['id'], i, sum(e[1] for e in s['etapes']))
        h += '<h4>Séance ' + str(i + 1) + ' (55 min) : ' + s['titre'] + '</h4>\n'
        for (moment, duree, strat, prof, eleves, trace) in s['etapes']:
            h += '<h5>' + moment + ' · ' + min_fr(duree) + '</h5>\n'
            h += '<p><strong>Stratégie :</strong> ' + strat + '</p>\n'
            h += '<p><strong>Activités du professeur :</strong></p>\n' + ul(prof)
            h += '<p><strong>Activités des élèves et réponses attendues :</strong></p>\n' + ul(eleves)
            if trace:
                h += '<p><strong>Trace écrite :</strong> ' + trace + '</p>\n'
    h += '<h3>6. Éclairage scientifique pour le professeur</h3>\n<p>Connaissances d\'approfondissement, à ne pas dicter, pour répondre aux questions des élèves et enrichir les explications.</p>\n' + ul(F['eclairage'])
    h += '<h3>7. Difficultés prévisibles et remédiation</h3>\n' + tableau(['Difficulté ou erreur fréquente', 'Remédiation proposée'], F['difficultes'])
    h += '<h3>8. Différenciation pédagogique</h3>\n'
    h += '<p><strong>Pour les élèves en difficulté :</strong></p>\n' + ul(F['soutien'])
    h += '<p><strong>Pour les élèves avancés :</strong></p>\n' + ul(F['approfondissement'])
    # évaluation
    E = F['evaluation']
    h += '<h3>9. Évaluation de fin de leçon (20 points)</h3>\n'
    h += '<p><em>Durée conseillée : 30 à 40 min. Les corrigés sont masqués ; ouvrez-les pour la correction.</em></p>\n'
    h += '<h4>I. Activités d\'application (8 points)</h4>\n'
    tot = 0
    for k, (enonce, p_, cor) in enumerate(E['activites']):
        tot += p_
        h += '<aside class="appli"><p class="appli-tete">Activité ' + str(k + 1) + ' · ' + pts(p_) + '</p><div class="enonce"><p>' + enonce + '</p></div>' + corrige('<p>' + cor + '</p>', 'Corrigé et barème') + '</aside>\n'
    assert tot == 8, (l['id'], 'activités', tot)
    h += '<h4>II. Situation d\'évaluation (12 points)</h4>\n'
    h += '<div class="situation"><div class="texte"><p>' + E['situation'] + '</p></div></div>\n<p><strong>Consignes :</strong></p>\n<ol>\n'
    for (cons, p_, cor) in E['consignes']:
        h += '<li>' + cons + ' <em>(' + pts(p_) + ')</em></li>\n'
    h += '</ol>\n'
    cor = ''.join('<p><strong>Consigne ' + str(k + 1) + ' (' + pts(p) + ') :</strong> ' + c + '</p>' for k, (_, p, c) in enumerate(E['consignes']))
    h += corrige(cor, 'Corrigé de la situation d\'évaluation') + '\n'
    pc = sum(p for _, p, _ in E['consignes'])
    assert pc == 10, (l['id'], 'consignes', pc)
    h += '<p><strong>Grille de correction de la situation (12 pts)</strong></p>\n' + tableau(['Critère', 'Indicateur', 'Points'], [
        ['CM1 – Pertinence', 'Chaque réponse correspond à la consigne posée', 'compris dans les points des consignes'],
        ['CM2 – Utilisation correcte des outils de la discipline', 'Notions, dates, localisations et calculs exacts', 'compris dans les points des consignes'],
        ['CM3 – Cohérence', 'Réponses logiques, ordonnées, sans contradiction', '1'],
        ['CP – Perfectionnement', 'Présentation soignée, orthographe correcte, originalité de la proposition', '1'],
        ['Total', 'Consignes 10 pts + cohérence 1 pt + perfectionnement 1 pt', '12'],
    ])
    h += '<h3>10. Éducation aux valeurs et liens avec les autres disciplines</h3>\n' + ul(F['valeurs'])
    h += '<h3>11. Bilan de la séance (à remplir par le professeur)</h3>\n' + ul([
        'Les objectifs ont-ils été atteints ? Par quelle proportion d\'élèves (résultats de l\'évaluation) ?',
        'Quelles parties ont pris plus de temps que prévu ? Que faut-il ajuster pour la prochaine classe ?',
        'Quels élèves ont besoin d\'une remédiation, et laquelle ?',
        'Remarques sur les supports utilisés (à garder, à changer, à compléter).'])
    return h

def main(chemin):
    D = json.load(open(chemin, encoding='utf-8'))
    c = [x for x in D['classes'] if x['id'] == '6e'][0]
    c['annexes'] = [a for a in c['annexes'] if not a.get('enseignant')]
    nouvelles = []
    g = guide_html(c)
    nouvelles.append({'id': '6e-ens-guide', 'titre': 'Guide de l\'enseignant de 6e', 'enseignant': True, 'html': g, 'texte': txt(g)})
    manque = []
    for d in c['disciplines']:
        for t in d['themes']:
            for l in t['lecons']:
                F = FICHES.get(l['id'])
                if not F:
                    manque.append(l['id']); continue
                hh = fiche(c, d, t, l, F)
                nouvelles.append({'id': '6e-ens-' + l['id'][3:], 'titre': 'Fiche enseignant · ' + d['nom'] + ' T' + str(t['n']) + '-L' + str(l['n']) + ' · ' + l['titre'],
                                  'enseignant': True, 'lecon': l['id'], 'disc': d['id'], 'html': hh, 'texte': txt(hh)})
    if manque:
        print('Fiches manquantes :', manque)
    c['annexes'] = c['annexes'] + nouvelles
    json.dump(D, open(chemin, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print(len(nouvelles), 'éléments enseignant ajoutés ;', sum(len(n['html']) for n in nouvelles), 'caractères HTML')

if __name__ == '__main__':
    main(sys.argv[1])
