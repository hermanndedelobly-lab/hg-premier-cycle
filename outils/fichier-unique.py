#!/usr/bin/env python3
"""Fabrique la page unique (index.html autonome) de l'application Android à partir des
fichiers de la version web : app.css (polices intégrées en base64), app.js et data/contenu.json
sont insérés dans la page. Les bibliothèques PDF (lib/) restent des fichiers à côté.

Usage : python3 outils/fichier-unique.py SORTIE.html [--mode apk|single|maj] [--racine DOSSIER]

Modes :
  apk    page de l'APK (données intégrées) + script de démarrage qui choisit la version la plus récente
         enregistrée dans le téléphone (mise à jour sans nouvel APK) ;
  maj    page de mise à jour téléchargée par l'application (maj/page.html) : code et styles, sans les
         données (lues dans le téléphone, clé hg1c.contenu-maj) ;
  single fichier autonome.
"""

# Script de démarrage de la page de l'APK. S'exécute avant tout le reste. Si le téléphone contient une version
# téléchargée plus récente (page « maj » + contenu de même version), la page d'origine ne démarre pas
# (window.HG_REMPLACER) et elle est remplacée par la version téléchargée une fois lue. Sécurité : si la version
# téléchargée n'a pas confirmé son démarrage (clé code-ok) au lancement précédent, elle est écartée (code-echec)
# et la version d'origine de l'APK démarre.
DEMARRAGE = '''<script>/* Démarrage GNOMBLESSON : version la plus récente enregistrée dans le téléphone */
(function () {
  var E = "%(version)s"; window.HG_VERSION_EMBARQUEE = E;
  function lire(k) { try { return localStorage.getItem('hg1c.' + k); } catch (e) { return null; } }
  function ecrire(k, v) { try { localStorage.setItem('hg1c.' + k, v); } catch (e) { /* rien */ } }
  function plus(a, b) { a = String(a || '0').split('.').map(Number); b = String(b || '0').split('.').map(Number);
    for (var i = 0; i < 3; i++) { if ((a[i] || 0) !== (b[i] || 0)) return (a[i] || 0) > (b[i] || 0); } return false; }
  var m = null, d = null;
  try { m = JSON.parse(lire('code-maj')); } catch (e) { m = null; }
  if (!m || !m.page || !plus(m.version, E)) return;
  try { d = JSON.parse(lire('contenu-maj')); } catch (e) { d = null; }
  if (!d || d.version !== m.version) return;
  if (lire('code-echec') === m.version) return;
  if (lire('code-essai') === m.version && lire('code-ok') !== m.version) { ecrire('code-echec', m.version); return; }
  ecrire('code-essai', m.version);
  window.HG_REMPLACER = m.page;
  document.addEventListener('DOMContentLoaded', function () {
    var page = window.HG_REMPLACER; window.HG_REMPLACER = null; window.HG_DATA = null;
    document.open(); document.write(page); document.close();
  });
})();</script>
'''
import argparse
import base64
import json
import os
import re
import sys


def lire(chemin):
    with open(chemin, encoding='utf-8') as f:
        return f.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sortie')
    ap.add_argument('--mode', default='apk', choices=['apk', 'single', 'maj'])
    ap.add_argument('--racine', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    a = ap.parse_args()
    R = a.racine

    page = lire(os.path.join(R, 'index.html'))
    css = lire(os.path.join(R, 'app.css'))
    js = lire(os.path.join(R, 'app.js'))
    contenu = lire(os.path.join(R, 'data', 'contenu.json'))
    version = json.loads(contenu)['version']

    def police(m):
        with open(os.path.join(R, m.group(1)), 'rb') as f:
            return 'url(data:font/woff2;base64,' + base64.b64encode(f.read()).decode() + ')'
    css = re.sub(r'url\((fonts/[^)]+\.woff2)\)', police, css)

    # liens inutiles dans la page autonome (manifeste, icônes), feuille de style intégrée
    page = re.sub(r'<link rel="(manifest|icon|apple-touch-icon)"[^>]*>\n', '', page)
    page, n = re.subn(r'<link rel="stylesheet" href="app.css">', lambda m: '<style>' + css + '</style>', page)
    if n != 1:
        sys.exit('feuille de style introuvable dans index.html')

    mode = re.search(r'<script>window.HG_MODE="pwa";window.HG_VERSION="([^"]+)";</script>\n<script src="app.js" defer></script>\n', page)
    if not mode:
        sys.exit('scripts de démarrage introuvables dans index.html')
    if mode.group(1) != version:
        sys.exit(f'versions différentes : index.html {mode.group(1)} / contenu.json {version}')
    # « </ » écrit « <\/ » : aucun « </script> » du contenu ne peut fermer la balise
    donnees = contenu.replace('</', '<\\/')
    if a.mode == 'maj':
        # surveillance : sans confirmation de démarrage (code-ok) en 12 s, la version téléchargée s'écarte
        # d'elle-même (code-echec) et l'application redémarre sur la version de l'APK
        garde = ('<script>(function(){var V="' + version + '";setTimeout(function(){try{if(localStorage.getItem("hg1c.code-ok")!==V)'
                 '{localStorage.setItem("hg1c.code-echec",V);location.reload();}}catch(e){}},12000);})();</script>\n')
        page = page.replace('<head>\n', '<head>\n' + garde, 1)
        donnees_js = "window.HG_MAJ=true;try{window.HG_DATA=JSON.parse(localStorage.getItem('hg1c.contenu-maj'))}catch(e){window.HG_DATA=null}"
        mode_js = 'apk'
    else:
        donnees_js = 'window.HG_DATA=' + donnees
        mode_js = a.mode
    scripts = ('<script>window.HG_MODE="' + mode_js + '";window.HG_VERSION="' + version + '";' + donnees_js + ';</script>\n'
               '<script>' + js.replace('</script', '<\\/script') + '</script>\n')
    page = page[:mode.start()] + page[mode.end():]
    page = page.replace('</body>', scripts + '</body>', 1)
    if a.mode == 'apk':
        page = page.replace('<head>\n', '<head>\n' + DEMARRAGE % {'version': version}, 1)

    with open(a.sortie, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'{a.sortie} : {len(page.encode()) / 1e6:.2f} Mo, version {version}, mode {a.mode}')


if __name__ == '__main__':
    main()
