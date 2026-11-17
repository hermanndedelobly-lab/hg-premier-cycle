#!/usr/bin/env python3
"""Lot 2 (5e), seconde demande : compléments de vérification (exécuté par GitHub Actions).
Écrit dans sources/verification/lot2/ (fichiers « b-… ») ; rien n'est modifié dans l'application.
  1. Open Library (recherche par titre) : Vogel 1997, Niane 1960.
  2. Crossref : chapitre de J.-P. Chauveau (2006) sur le tutorat en pays gban.
  3. Wikipédia (API, source secondaire) : textes de loi, Probo Koala, recensement 2021, ANAGED, barrages.
  4. Sites officiels : page d'accueil de l'INS ; indicateurs de la Banque mondiale (population, part urbaine).
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request

OUT = os.path.join('sources', 'verification', 'lot2')
os.makedirs(OUT, exist_ok=True)
UA = {'User-Agent': 'gnomblesson-verification/1.0 (outil pedagogique)'}
journal = []


def get(url, timeout=90):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode('utf-8', 'replace')


def noter(etape, ok, detail):
    journal.append({'etape': etape, 'ok': ok, 'detail': detail})
    print(('OK  ' if ok else 'ERR ') + etape + ' : ' + str(detail)[:400])


for cle, titre in [('vogel-1997', 'Baule: African Art, Western Eyes'), ('niane-1960', "Soundjata ou l'épopée mandingue")]:
    try:
        d = json.loads(get('https://openlibrary.org/search.json?' + urllib.parse.urlencode(
            {'title': titre, 'limit': 5, 'fields': 'title,author_name,first_publish_year,publisher'})))
        noter('Open Library ' + cle, bool(d.get('docs')), d.get('docs', [])[:3])
    except Exception as e:
        noter('Open Library ' + cle, False, repr(e))

time.sleep(5)
try:
    d = json.loads(get('https://api.crossref.org/works?' + urllib.parse.urlencode(
        {'query.bibliographic': 'Chauveau How does an institution evolve? Land, politics, intergenerational relations and the institution of the tutorat', 'rows': 3})))
    items = d['message']['items']
    noter('Crossref chauveau-2006', bool(items), [{'titre': (x.get('title') or [''])[0], 'auteurs': [a.get('family') for a in x.get('author', [])],
                                                   'ouvrage': (x.get('container-title') or [''])[0], 'editeur': x.get('publisher'),
                                                   'annee': (x.get('issued', {}).get('date-parts') or [[None]])[0][0], 'doi': x.get('DOI')} for x in items])
except Exception as e:
    noter('Crossref chauveau-2006', False, repr(e))

WIKI = [('code-environnement', 'Code de l\'environnement Côte d\'Ivoire loi 96-766'), ('probo-koala', 'Probo Koala déchets toxiques Abidjan 2006'),
        ('rgph-2021', 'Recensement général de la population 2021 Côte d\'Ivoire'), ('demographie', 'Démographie de la Côte d\'Ivoire'),
        ('code-eau', 'Code de l\'eau Côte d\'Ivoire 1998'), ('foncier', 'loi 98-750 domaine foncier rural Côte d\'Ivoire'),
        ('anaged', 'Agence nationale de gestion des déchets Côte d\'Ivoire'), ('soubre', 'barrage de Soubré'), ('kossou', 'barrage de Kossou'),
        ('sachets', 'interdiction sachets plastiques Côte d\'Ivoire 2013'), ('code-forestier', 'Code forestier Côte d\'Ivoire 2019'),
        ('niani', 'Niani capitale empire du Mali')]
for cle, q in WIKI:
    try:
        d = json.loads(get('https://fr.wikipedia.org/w/api.php?' + urllib.parse.urlencode(
            {'action': 'query', 'list': 'search', 'srsearch': q, 'srlimit': 5, 'format': 'json'})))
        res = [{'titre': x['title'], 'extrait': re.sub(r'<[^>]+>', '', x['snippet'])} for x in d['query']['search']]
        json.dump(res, open(os.path.join(OUT, 'b-wiki-' + cle + '.json'), 'w'), ensure_ascii=False, indent=1)
        noter('Wikipédia ' + cle, bool(res), res[:3])
    except Exception as e:
        noter('Wikipédia ' + cle, False, repr(e))

for cle, url in [('ins-accueil', 'https://www.ins.ci/'), ('ins-rgph', 'https://www.ins.ci/RGPH2021/')]:
    try:
        t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', get(url)))
        open(os.path.join(OUT, 'b-' + cle + '.txt'), 'w').write(t)
        noter('INS ' + cle, True, [t[max(0, m.start() - 200):m.end() + 200] for m in re.finditer(r'29 ?389 ?150|RGPH ?2021|moins de 35|urbain', t)][:6])
    except Exception as e:
        noter('INS ' + cle, False, repr(e))

for cle, ind in [('population', 'SP.POP.TOTL'), ('urbain', 'SP.URB.TOTL.IN.ZS')]:
    try:
        d = json.loads(get(f'https://api.worldbank.org/v2/country/CIV/indicator/{ind}?format=json&date=2014:2023'))
        noter('Banque mondiale ' + cle, True, [(x['date'], x['value']) for x in d[1]])
    except Exception as e:
        noter('Banque mondiale ' + cle, False, repr(e))

json.dump(journal, open(os.path.join(OUT, 'b-journal.json'), 'w'), ensure_ascii=False, indent=1)
print('Terminé :', sum(1 for j in journal if j['ok']), '/', len(journal))
