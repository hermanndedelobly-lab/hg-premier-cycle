#!/usr/bin/env python3
"""Télécharge des photographies candidates libres de droits depuis Wikimedia Commons.

Lancé par le workflow « Illustrations libres (Commons) » (le réseau des sessions de développement
n'atteint pas Commons). Lit illustrations/demande.json et écrit dans illustrations/candidats/ :
  - les images (miniatures Commons à la largeur demandée) ;
  - candidats.json : titre, page Commons, licence, auteur, crédit, description, dimensions.
Seules les licences libres sont retenues (domaine public, CC0, CC BY, CC BY-SA) ; aucune image
n'est intégrée à l'application par ce script : le choix est fait après vérification humaine.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORTIE = os.path.join(RACINE, 'illustrations', 'candidats')
API = 'https://commons.wikimedia.org/w/api.php'
UA = 'illustrations-scolaires/1.0 (outil pedagogique; GitHub Actions)'
LIBRE = re.compile(r'^(public domain|pd\b|pd-|cc0|cc by(-sa)? ?\d|cc-by(-sa)?-\d)', re.I)


def lire(url, essais=6):
    # Wikimedia limite le débit (erreur 429) : on attend de plus en plus longtemps avant de réessayer.
    for k in range(essais):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or k == essais - 1:
                raise
            attente = int(e.headers.get('Retry-After') or 0) or 10 * (k + 1)
            print(f'  limite de débit ({e.code}), nouvelle tentative dans {attente} s', file=sys.stderr)
            time.sleep(attente)


def appel(params):
    url = API + '?' + urllib.parse.urlencode(dict(params, format='json', formatversion='2'))
    return json.loads(lire(url))


def texte(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h or '')).strip()


def chercher(q, largeur):
    d = appel({'action': 'query', 'generator': 'search', 'gsrsearch': q + ' filetype:bitmap', 'gsrnamespace': 6,
               'gsrlimit': 15, 'prop': 'imageinfo', 'iiprop': 'url|size|extmetadata|mime', 'iiurlwidth': largeur,
               'iiextmetadatafilter': 'LicenseShortName|LicenseUrl|Artist|Credit|ImageDescription|DateTimeOriginal|UsageTerms|AttributionRequired'})
    pages = sorted(d.get('query', {}).get('pages', []), key=lambda p: p.get('index', 99))
    res = []
    for p in pages:
        ii = (p.get('imageinfo') or [{}])[0]
        m = ii.get('extmetadata', {})
        lic = texte(m.get('LicenseShortName', {}).get('value'))
        if not LIBRE.search(lic) or ii.get('mime') not in ('image/jpeg', 'image/png'):
            continue
        if min(ii.get('width', 0), ii.get('height', 0)) < 400:
            continue
        res.append({'fichier': p['title'], 'page': ii.get('descriptionurl'), 'miniature': ii.get('thumburl'),
                    'largeur_originale': ii.get('width'), 'hauteur_originale': ii.get('height'),
                    'licence': lic, 'licence_url': m.get('LicenseUrl', {}).get('value', ''),
                    'auteur': texte(m.get('Artist', {}).get('value')), 'credit': texte(m.get('Credit', {}).get('value')),
                    'description': texte(m.get('ImageDescription', {}).get('value'))[:400],
                    'date': texte(m.get('DateTimeOriginal', {}).get('value')),
                    'attribution_requise': m.get('AttributionRequired', {}).get('value', '')})
    return res


def main():
    dem = json.load(open(os.path.join(RACINE, 'illustrations', 'demande.json'), encoding='utf-8'))
    os.makedirs(SORTIE, exist_ok=True)
    tout, n = [], dem.get('candidats_par_theme', 3)
    for th in dem['themes']:
        vus, retenus = set(), []
        for q in th['recherches']:
            try:
                for c in chercher(q, dem.get('largeur', 800)):
                    if c['fichier'] not in vus and len(retenus) < n:
                        vus.add(c['fichier']); retenus.append(c)
            except Exception as e:
                print(f'{th["id"]} : recherche « {q} » en échec : {e}', file=sys.stderr)
            time.sleep(3)
            if len(retenus) >= n:
                break
        for k, c in enumerate(retenus, 1):
            ext = '.png' if c['miniature'].lower().endswith('.png') else '.jpg'
            nom = f'{th["id"]}-{k}{ext}'
            try:
                data = lire(c['miniature'])
            except Exception as e:
                print(f'{nom} : téléchargement impossible ({e}), image ignorée', file=sys.stderr)
                continue
            with open(os.path.join(SORTIE, nom), 'wb') as f:
                f.write(data)
            c.update({'theme': th['id'], 'titre_theme': th['titre'], 'image': nom})
            tout.append(c)
            time.sleep(4)
        print(f'{th["id"]} : {len(retenus)} candidat(s)')
    with open(os.path.join(SORTIE, 'candidats.json'), 'w', encoding='utf-8') as f:
        json.dump({'demande': dem.get('numero'), 'candidats': tout}, f, ensure_ascii=False, indent=1)
    print(f'{len(tout)} images téléchargées.')


if __name__ == '__main__':
    main()
