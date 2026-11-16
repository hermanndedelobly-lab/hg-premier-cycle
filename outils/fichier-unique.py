#!/usr/bin/env python3
"""Fabrique la page unique (index.html autonome) de l'application Android à partir des
fichiers de la version web : app.css (polices intégrées en base64), app.js et data/contenu.json
sont insérés dans la page. Les bibliothèques PDF (lib/) restent des fichiers à côté.

Usage : python3 outils/fichier-unique.py SORTIE.html [--mode apk|single] [--racine DOSSIER]
"""
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
    ap.add_argument('--mode', default='apk', choices=['apk', 'single'])
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
    scripts = ('<script>window.HG_MODE="' + a.mode + '";window.HG_VERSION="' + version + '";window.HG_DATA=' + donnees + ';</script>\n'
               '<script>' + js + '</script>\n')
    page = page[:mode.start()] + page[mode.end():]
    page = page.replace('</body>', scripts + '</body>', 1)

    with open(a.sortie, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'{a.sortie} : {len(page.encode()) / 1e6:.2f} Mo, version {version}, mode {a.mode}')


if __name__ == '__main__':
    main()
