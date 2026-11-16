#!/usr/bin/env python3
"""Passerelle APK 1.10.0 → GNOMBLESSON, sans désinstallation ni nouvel APK.

L'APK 1.10.0 (clé de signature perdue) ne peut plus recevoir de nouvel APK, mais elle sait télécharger un contenu
corrigé depuis l'« Adresse du site des mises à jour » saisie dans ses Réglages. Ce script produit le dossier servi à
cette adresse (par défaut « pont/ ») :
  pont/version.json        même fichier que la racine ;
  pont/data/contenu.json   contenu GNOMBLESSON + lanceur (champ « pont ») ;
  pont/maj/page.html       page GNOMBLESSON (copie de maj/page.html, à régénérer avant).

La 1.10.0 affiche certains champs du contenu sans les neutraliser (nombre de leçons de l'accueil, durée d'une leçon
dans chaque page de classe) : on y place une image dont l'erreur de chargement exécute le lanceur. Le lanceur
nettoie les données (durées numériques, nombre de leçons, lanceur retiré), puis remplace la page par GNOMBLESSON,
avec les mêmes données locales (progression, scores, réglages). Mêmes sécurités que la mise à jour sans APK :
une version qui ne confirme pas son démarrage est écartée (code-essai / code-ok / code-echec) et « Revenir à la
version d'origine » rend la 1.10.0 normale.

Usage : python3 outils/fichier-unique.py maj/page.html --mode maj && python3 outils/fabriquer-pont.py [pont]
"""
import json
import os
import shutil
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORTIE = os.path.join(R, sys.argv[1] if len(sys.argv) > 1 else 'pont')

LANCEUR = r"""
(function () {
  if (window.HG_PONT_FAIT || window.HG_MAJ) return;
  window.HG_PONT_FAIT = true;
  function lire(k) { try { return localStorage.getItem('hg1c.' + k); } catch (e) { return null; } }
  function ecrire(k, v) { try { localStorage.setItem('hg1c.' + k, v); } catch (e) {} }
  var d; try { d = JSON.parse(lire('contenu-maj')); } catch (e) { return; }
  if (!d || !d.classes) return;
  var V = d.version;
  if (lire('code-echec') === V) return;
  if (lire('code-essai') === V && lire('code-ok') !== V) { ecrire('code-echec', V); return; }
  var n = 0;
  d.classes.forEach(function (c) { c.disciplines.forEach(function (di) { di.themes.forEach(function (t) { t.lecons.forEach(function (l) {
    n++; if (typeof l.duree === 'string') l.duree = parseInt(l.duree, 10) || 0; }); }); }); });
  d.nbLecons = n; delete d.pont;
  function lancer(page) {
    ecrire('code-essai', V);
    window.HG_DATA_PROPRE = d; window.HG_VERSION_EMBARQUEE = '1.10.0';
    document.open(); document.write(page); document.close();
  }
  var c = null; try { c = JSON.parse(lire('code-maj')); } catch (e) {}
  if (c && c.version === V && c.page) return lancer(c.page);
  var base = ''; try { base = (JSON.parse(lire('reglages')) || {}).adresse || ''; } catch (e) {}
  base = base.replace(/\/+$/, ''); if (!base) return;
  fetch(base + '/maj/page.html', { cache: 'no-store' }).then(function (r) { if (!r.ok) throw 0; return r.text(); }).then(function (p) {
    if (p.indexOf('window.HG_VERSION="' + V + '"') < 0) return;
    try { localStorage.setItem('hg1c.code-maj', JSON.stringify({ version: V, page: p })); } catch (e) { return; }
    lancer(p);
  }).catch(function () {});
})();
"""
DECLENCHEUR = ("<img src=\"pont-declencheur\" alt=\"\" style=\"display:none\" onerror=\"try{(new Function("
               "JSON.parse(localStorage.getItem('hg1c.contenu-maj')).pont))()}catch(e){}\">")

d = json.load(open(os.path.join(R, 'data', 'contenu.json'), encoding='utf-8'))
v = json.load(open(os.path.join(R, 'version.json'), encoding='utf-8'))
page = open(os.path.join(R, 'maj', 'page.html'), encoding='utf-8').read()
if v['version'] != d['version'] or ('window.HG_VERSION="%s"' % d['version']) not in page:
    sys.exit('versions différentes : version.json, data/contenu.json et maj/page.html doivent être identiques')
if "window.HG_DATA_PROPRE||" not in page:
    sys.exit('maj/page.html ne lit pas HG_DATA_PROPRE : régénérer avec outils/fichier-unique.py --mode maj')

d['pont'] = LANCEUR
d['nbLecons'] = str(d['nbLecons']) + DECLENCHEUR
for c in d['classes']:          # une leçon par classe : chaque page de classe déclenche aussi
    l = c['disciplines'][0]['themes'][0]['lecons'][0]
    l['duree'] = str(l['duree']) + DECLENCHEUR

os.makedirs(os.path.join(SORTIE, 'data'), exist_ok=True)
os.makedirs(os.path.join(SORTIE, 'maj'), exist_ok=True)
with open(os.path.join(SORTIE, 'data', 'contenu.json'), 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, separators=(',', ':'))
shutil.copyfile(os.path.join(R, 'version.json'), os.path.join(SORTIE, 'version.json'))
shutil.copyfile(os.path.join(R, 'maj', 'page.html'), os.path.join(SORTIE, 'maj', 'page.html'))
print('passerelle prête :', os.path.relpath(SORTIE, R), '| version', d['version'])
