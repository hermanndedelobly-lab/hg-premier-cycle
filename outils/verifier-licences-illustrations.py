#!/usr/bin/env python3
"""Contrôle final des licences des photographies retenues (illustrations/selection/credits.json).

Lancé par le workflow « Illustrations libres (Commons) » (le réseau des sessions de développement
n'atteint pas Commons). Pour chaque fichier non suspendu, relève sur la fiche Commons originale :
le texte source (modèles de licence et de permission), les catégories, les métadonnées
(licence, auteur, source, restrictions), et signale tout modèle de suppression ou de violation
de droits. Écrit illustrations/selection/verification-licences.json.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = 'https://commons.wikimedia.org/w/api.php'
UA = 'illustrations-scolaires/1.0 (outil pedagogique; GitHub Actions)'
ALERTES = re.compile(r'\{\{\s*(delete|speedy|copyvio|no permission|no license|no source|nsd|npd|nld|deletion request|dw no source|fop[- ]?[a-z]*|disputed)', re.I)


def lire(url, essais=6):
    for k in range(essais):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or k == essais - 1:
                raise
            time.sleep(int(e.headers.get('Retry-After') or 0) or 10 * (k + 1))


def texte(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h or '')).strip()


def main():
    sel = json.load(open(os.path.join(R, 'illustrations', 'selection.json'), encoding='utf-8'))
    statut = {p['id']: p.get('statut', '') for p in sel['photos']}
    credits = json.load(open(os.path.join(R, 'illustrations', 'selection', 'credits.json'), encoding='utf-8'))
    res = []
    for c in credits:
        if statut.get(c['id'], '').startswith('suspendue'):
            res.append({'id': c['id'], 'statut': 'suspendue : non vérifiée, non intégrée'})
            continue
        q = {'action': 'query', 'titles': c['fichier_commons'], 'prop': 'revisions|categories|imageinfo',
             'rvprop': 'content|timestamp', 'rvslots': 'main', 'cllimit': 'max', 'iiprop': 'extmetadata|url',
             'format': 'json', 'formatversion': '2'}
        d = json.loads(lire(API + '?' + urllib.parse.urlencode(q)))
        page = d['query']['pages'][0]
        if page.get('missing'):
            res.append({'id': c['id'], 'fichier': c['fichier_commons'], 'erreur': 'fichier introuvable sur Commons'})
            continue
        wt = page['revisions'][0]['slots']['main']['content']
        m = page['imageinfo'][0]['extmetadata']
        g = lambda k: texte(m.get(k, {}).get('value', ''))
        modeles = sorted(set(re.findall(r'\{\{\s*([^|}\n]+)', wt)))
        res.append({
            'id': c['id'], 'fichier': c['fichier_commons'], 'page': page['imageinfo'][0].get('descriptionurl'),
            'derniere_modification': page['revisions'][0]['timestamp'],
            'licence': g('LicenseShortName'), 'licence_url': g('LicenseUrl'), 'conditions': g('UsageTerms'),
            'auteur': g('Artist'), 'credit': g('Credit'), 'attribution': g('Attribution'),
            'restrictions': g('Restrictions'), 'protege': g('Copyrighted'), 'attribution_requise': g('AttributionRequired'),
            'modeles': modeles, 'alertes': sorted(set(a.group(0) for a in ALERTES.finditer(wt))),
            'categories': [x['title'] for x in page.get('categories', [])][:40],
            'licence_dans_texte': sorted(set(x for x in modeles if re.match(r'(?i)(cc-|cc0|pd-|public ?domain|self|licen[sc]e|met|nypl|flickrreview|lrr|metropolitan)', x.strip()))),
        })
        print(c['id'], '|', res[-1]['licence'], '| alertes :', res[-1]['alertes'] or 'aucune')
        time.sleep(3)
    out = os.path.join(R, 'illustrations', 'selection', 'verification-licences.json')
    json.dump({'date': time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()), 'fichiers': res}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('écrit :', out)


if __name__ == '__main__':
    sys.exit(main())
