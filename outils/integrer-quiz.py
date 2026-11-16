#!/usr/bin/env python3
"""Intègre les quiz (quiz/*.txt) dans data/contenu.json.

Format d'un fichier de quiz :
    @identifiant-de-la-lecon
    ? question
    + bonne réponse
    - mauvaise réponse      (une ou plusieurs)
    = explication           (facultative)
Les lignes vides et celles qui commencent par « # » sont ignorées.

Dans contenu.json, chaque leçon reçoit « quiz » : liste de {q, c, e?}, où c[0] est la bonne
réponse (l'application mélange les réponses à l'affichage), et « nbQuiz ».

Usage : python3 outils/integrer-quiz.py [--verifier]
  --verifier : contrôle seulement (n'écrit rien) ; code de sortie 1 en cas d'erreur.
"""
import glob
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENU = os.path.join(RACINE, 'data', 'contenu.json')


def lire_quiz(chemin, erreurs):
    quiz, lecon, q = {}, None, None

    def fermer():
        if q is None:
            return
        bonnes = [r for r in q['_r'] if r[0]]
        if len(bonnes) != 1:
            erreurs.append(f'{chemin}:{q["_l"]} : il faut exactement une bonne réponse (+), trouvé {len(bonnes)}')
        if len(q['_r']) < 2:
            erreurs.append(f'{chemin}:{q["_l"]} : il faut au moins deux réponses')
        textes = [r[1] for r in q['_r']]
        if len(set(textes)) != len(textes):
            erreurs.append(f'{chemin}:{q["_l"]} : réponses en double')
        item = {'q': q['q'], 'c': [r[1] for r in bonnes] + [r[1] for r in q['_r'] if not r[0]]}
        if q.get('e'):
            item['e'] = q['e']
        quiz[lecon].append(item)

    with open(chemin, encoding='utf-8') as f:
        for n, ligne in enumerate(f, 1):
            ligne = ligne.rstrip('\n').strip()
            if not ligne or ligne.startswith('#'):
                continue
            marque, texte = ligne[0], ligne[1:].strip()
            if marque == '@':
                fermer(); q = None
                lecon = texte
                if lecon in quiz:
                    erreurs.append(f'{chemin}:{n} : leçon {lecon} déjà présente')
                quiz[lecon] = []
            elif marque == '?':
                if lecon is None:
                    erreurs.append(f'{chemin}:{n} : question avant toute leçon (@)')
                    continue
                fermer()
                q = {'q': texte, '_r': [], '_l': n}
            elif marque in '+-':
                if q is None:
                    erreurs.append(f'{chemin}:{n} : réponse sans question')
                    continue
                q['_r'].append((marque == '+', texte))
            elif marque == '=':
                if q is None:
                    erreurs.append(f'{chemin}:{n} : explication sans question')
                    continue
                q['e'] = texte
            else:
                erreurs.append(f'{chemin}:{n} : ligne non reconnue : {ligne[:40]}')
        fermer()
    return quiz


def main():
    verifier = '--verifier' in sys.argv
    erreurs, tous = [], {}
    for chemin in sorted(glob.glob(os.path.join(RACINE, 'quiz', '*.txt'))):
        for k, v in lire_quiz(chemin, erreurs).items():
            if k in tous:
                erreurs.append(f'leçon {k} présente dans deux fichiers')
            tous[k] = v

    with open(CONTENU, encoding='utf-8') as f:
        d = json.load(f)
    lecons = {}
    for c in d['classes']:
        for di in c['disciplines']:
            for t in di['themes']:
                for l in t['lecons']:
                    lecons[l['id']] = l
    for k in tous:
        if k not in lecons:
            erreurs.append(f'leçon inconnue dans les quiz : {k}')
    for k in lecons:
        if k not in tous or not tous[k]:
            erreurs.append(f'leçon sans quiz : {k}')

    if erreurs:
        print('\n'.join(erreurs))
        sys.exit(1)

    total = sum(len(v) for v in tous.values())
    print(f'{len(tous)} leçons, {total} questions : correct.')
    if verifier:
        return
    for k, l in lecons.items():
        l['quiz'] = tous[k]
        l['nbQuiz'] = len(tous[k])
    d['nbQuiz'] = total
    with open(CONTENU, 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print('data/contenu.json mis à jour.')


if __name__ == '__main__':
    main()
