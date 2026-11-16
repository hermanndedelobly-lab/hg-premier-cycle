#!/usr/bin/env python3
"""Intègre les contenus enrichis (pedagogie/<identifiant>/) dans data/contenu.json.

Pour chaque leçon : cours <- eleve.html ; nouveaux champs enseignant, preparation, culture,
evaluation, v11 (statut) ; textes de recherche recalculés. Contrôles bloquants :
  - identifiant de leçon existant, les cinq fichiers présents et non vides ;
  - HTML bien formé (balises ouvertes et fermées dans le bon ordre) ;
  - trace écrite : Introduction, au moins deux parties « I. » « II. », des sous-parties, Conclusion ;
  - mode enseignant : rubriques 1 à 10 et « 11 et 12 » ; culture : rubriques 1 à 9 ;
  - évaluation : compréhension, activités d'application, situation d'évaluation, corrigés, barème ;
  - préparation : compétence, habiletés, situation, matériel, stratégie, déroulement, vérification,
    synthèse, évaluation, remédiation ;
  - exercices.html, banque.html (facultatifs) : jamais moins d'exercices que dans la version précédente ;
  - illustrations : chaque <figure> a un <svg aria-label>, une <figcaption> avec titre en gras,
    puis une explication <p class="illus-expl">.
Usage : python3 outils/integrer-pedagogie.py [--verifier]
"""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENU = os.path.join(RACINE, 'data', 'contenu.json')
PEDA = os.path.join(RACINE, 'pedagogie')
FICHIERS = ['eleve', 'evaluation', 'enseignant', 'preparation', 'culture']
VIDES = {'br', 'img', 'hr', 'input', 'meta', 'link', 'col', 'area', 'source', 'wbr'}


class Verif(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pile, self.erreurs = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VIDES:
            self.pile.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VIDES:
            return
        if not self.pile or self.pile[-1][0] != tag:
            attendu = self.pile[-1] if self.pile else ('rien', 0)
            self.erreurs.append(f'ligne {self.getpos()[0]} : </{tag}> alors que <{attendu[0]}> (ligne {attendu[1]}) est ouvert')
            if any(t == tag for t, _ in self.pile):
                while self.pile and self.pile[-1][0] != tag:
                    self.pile.pop()
                self.pile.pop()
        else:
            self.pile.pop()


def texte(h):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()


def controler(lid, f, h, err):
    v = Verif()
    v.feed(h)
    v.close()
    err += [f'{lid}/{f}.html : {e}' for e in v.erreurs]
    if v.pile:
        err.append(f'{lid}/{f}.html : balises non fermées : ' + ', '.join(f'<{t}> l.{n}' for t, n in v.pile))
    for fig in re.findall(r'<figure.*?</figure>', h, re.S):
        if not re.search(r'<svg[^>]*aria-label="[^"]+"', fig):
            err.append(f'{lid}/{f}.html : illustration sans svg ni aria-label')
        if not re.search(r'<figcaption><b>[^<]+</b>', fig):
            err.append(f'{lid}/{f}.html : illustration sans légende commençant par un titre en gras')
    n_fig = len(re.findall(r'</figure>', h))
    if n_fig != len(re.findall(r'</figure>\s*<p class="illus-expl">', h)):
        err.append(f'{lid}/{f}.html : chaque illustration doit être suivie de son explication (p.illus-expl)')
    t = texte(h).lower()

    def exiger(motifs, quoi):
        for m in motifs:
            if not re.search(m, h if m.startswith('<') else t):
                err.append(f'{lid}/{f}.html : {quoi} manquant : {m}')
    if f == 'eleve':
        exiger([r'<h3>Introduction</h3>', r'<h4>I\. ', r'<h4>II\. ', r'<h5>1\. ', r'<h5>2\. ', r'<h3>Conclusion</h3>', r'<aside class="appli"'], 'élément de trace écrite')
    elif f == 'enseignant':
        exiger([rf'<h4>{i}\. ' for i in range(1, 11)] + [r'<h4>11 et 12\. '], 'rubrique du mode enseignant')
    elif f == 'culture':
        exiger([rf'<h4>{i}\. ' for i in range(1, 10)], 'rubrique de culture générale')
    elif f == 'evaluation':
        exiger(['compréhension', "activités d'application", "situation d'évaluation", 'corrigé', 'barème'], 'élément d\'évaluation')
    elif f == 'preparation':
        exiger(['compétence', 'habiletés', "situation d'apprentissage", 'matériel', 'stratégie', 'déroulement',
                'vérification', 'synthèse', 'évaluation', 'remédiation'], 'élément de préparation')


def main():
    verifier = '--verifier' in sys.argv
    with open(CONTENU, encoding='utf-8') as fh:
        d = json.load(fh)
    lecons = {l['id']: l for c in d['classes'] for di in c['disciplines'] for t in di['themes'] for l in t['lecons']}
    err, lots = [], {}
    for lid in sorted(os.listdir(PEDA)):
        dossier = os.path.join(PEDA, lid)
        if not os.path.isdir(dossier):
            continue
        if lid not in lecons:
            err.append(f'{lid} : identifiant de leçon inconnu')
            continue
        lot = {}
        for f in FICHIERS:
            p = os.path.join(dossier, f + '.html')
            if not os.path.isfile(p) or not open(p, encoding='utf-8').read().strip():
                err.append(f'{lid} : fichier {f}.html absent ou vide')
                continue
            lot[f] = open(p, encoding='utf-8').read().strip() + '\n'
            controler(lid, f, lot[f], err)
        # exercices.html (facultatif) : version corrigée des exercices traités de la leçon (champ « exercices »).
        # Garde-fou : aucun exercice existant ne peut disparaître.
        # banque.html (facultatif) : idem pour la banque d'exercices de la leçon (champ « banque »).
        for opt in ('exercices', 'banque'):
            p = os.path.join(dossier, opt + '.html')
            if not os.path.isfile(p):
                continue
            lot[opt] = open(p, encoding='utf-8').read().strip() + '\n'
            controler(lid, opt, lot[opt], err)
            avant = (lecons[lid].get(opt) or '').count('<section class="exo">')
            apres = lot[opt].count('<section class="exo">')
            if apres < avant:
                err.append(f'{lid}/{opt}.html : {apres} exercices au lieu de {avant} (suppression interdite)')
        meta = os.path.join(dossier, 'meta.json')
        lot['meta'] = json.load(open(meta, encoding='utf-8')) if os.path.isfile(meta) else {'statut': 'brouillon'}
        if lot['meta'].get('statut') not in ('brouillon', 'pilote', 'validee'):
            err.append(f'{lid} : statut inconnu dans meta.json')
        lots[lid] = lot
    if err:
        print('\n'.join(err))
        sys.exit(1)
    print(f'{len(lots)} leçon(s) enrichie(s) : contrôles réussis ({", ".join(lots)}).')
    if verifier:
        return
    for lid, lot in lots.items():
        l = lecons[lid]
        l['cours'] = lot['eleve']
        for f in ('enseignant', 'preparation', 'culture', 'evaluation', 'exercices', 'banque'):
            if f in lot:
                l[f] = lot[f]
        if 'banque' in lot:
            l['texteBanque'] = texte(l['banque'])
            l['nbBanque'] = l['banque'].count('<section class="exo">')
        l['v11'] = lot['meta']
        l['texte'] = texte(l['situation'] + ' ' + l['cours'] + ' ' + l['evaluation'])
        l['texteEns'] = texte(l['enseignant'] + ' ' + l['preparation'])
        l['texteCult'] = texte(l['culture'])
    with open(CONTENU, 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print('data/contenu.json mis à jour.')


if __name__ == '__main__':
    main()
