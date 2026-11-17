#!/usr/bin/env python3
"""Lot 3 (4e) : vérification des références et des faits récents (exécuté par GitHub Actions).
Écrit dans sources/verification/lot3/ ; rien n'est modifié dans l'application.
  1. Open Library (recherche par titre) : ouvrages cités dans les espaces Culture générale de 4e.
  2. Wikipédia (API, source secondaire) : institutions ivoiriennes, CEDEAO, UE, faits historiques.
  3. Wikipédia, texte complet de quelques articles (listes : districts, membres, présidences).
  4. Sites officiels : CEDEAO, Union européenne, Slave Voyages (accessibilité et extraits).
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request

OUT = os.path.join('sources', 'verification', 'lot3')
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


LIVRES = [
    ('wilks-1975', 'Asante in the Nineteenth Century'),
    ('memel-fote-1980', 'Le système politique de Lodjoukrou'),
    ('fortes-1940', 'African Political Systems'),
    ('roussier-1935', "L'établissement d'Issiny"),
    ('petre-grenouilleau-2004', 'Les traites négrières essai d\'histoire globale'),
    ('eltis-richardson-2010', 'Atlas of the Transatlantic Slave Trade'),
    ('soboul', 'La Révolution française Soboul'),
    ('martin-2012', 'Nouvelle histoire de la Révolution française'),
    ('verley-1997', 'La Révolution industrielle Verley'),
    ('allen-2009', 'The British Industrial Revolution in Global Perspective'),
    ('pomeranz-2000', 'The Great Divergence'),
]
ol = {}
for cle, titre in LIVRES:
    try:
        d = json.loads(get('https://openlibrary.org/search.json?' + urllib.parse.urlencode(
            {'q': titre, 'limit': 5, 'fields': 'title,author_name,first_publish_year,publisher'})))
        ol[cle] = d.get('docs', [])[:5]
        noter('Open Library ' + cle, bool(d.get('docs')), ol[cle][:2])
    except Exception as e:
        noter('Open Library ' + cle, False, repr(e))
    time.sleep(2)
json.dump(ol, open(os.path.join(OUT, 'openlibrary.json'), 'w'), ensure_ascii=False, indent=1)

RECH = [
    ('cdvr', 'Commission Dialogue Vérité et Réconciliation Côte d\'Ivoire 2011'),
    ('conariv', 'Commission nationale pour la réconciliation et l\'indemnisation des victimes'),
    ('cnrct', 'Chambre nationale des rois et chefs traditionnels Côte d\'Ivoire'),
    ('aniaba', 'Aniaba Assinie Louis XIV'),
    ('assinie-fort', 'Assinie fort Saint-Louis 1701'),
    ('bouet-willaumez', 'Bouët-Willaumez traités Grand-Bassam 1842'),
    ('toussaint', 'Toussaint Louverture insurrection 1791 Saint-Domingue'),
    ('trevithick', 'Richard Trevithick locomotive 1804'),
    ('loi-2014-451', 'loi 2014-451 administration territoriale Côte d\'Ivoire'),
    ('districts', 'Districts autonomes de Côte d\'Ivoire 2021 ministre-gouverneur'),
    ('communes', 'Communes de Côte d\'Ivoire 1980 communalisation'),
    ('elections-2023', 'Élections municipales ivoiriennes de 2023'),
    ('habg', 'Haute Autorité pour la bonne gouvernance Côte d\'Ivoire'),
    ('cedeao-aes', 'Alliance des États du Sahel retrait CEDEAO janvier 2025'),
    ('cedeao-president', 'président de la Commission de la CEDEAO 2026'),
    ('zone-euro-bulgarie', 'Bulgarie zone euro 2026'),
    ('ape-ci', 'accord de partenariat économique Côte d\'Ivoire Union européenne 2016'),
]
for cle, q in RECH:
    try:
        d = json.loads(get('https://fr.wikipedia.org/w/api.php?' + urllib.parse.urlencode(
            {'action': 'query', 'list': 'search', 'srsearch': q, 'srlimit': 5, 'format': 'json'})))
        res = [{'titre': x['title'], 'extrait': re.sub(r'<[^>]+>', '', x['snippet'])} for x in d['query']['search']]
        json.dump(res, open(os.path.join(OUT, 'wiki-' + cle + '.json'), 'w'), ensure_ascii=False, indent=1)
        noter('Wikipédia ' + cle, bool(res), res[:3])
    except Exception as e:
        noter('Wikipédia ' + cle, False, repr(e))
    time.sleep(3)

# Textes complets (listes et présidences), en français puis en anglais
PAGES = [
    ('fr', 'Districts de Côte d\'Ivoire'), ('fr', 'Communauté économique des États de l\'Afrique de l\'Ouest'),
    ('en', 'ECOWAS Commission'), ('en', 'Economic Community of West African States'),
    ('fr', 'Zone euro'), ('fr', 'Alliance des États du Sahel'), ('en', 'Trans-Atlantic Slave Trade Database'),
]
for lang, titre in PAGES:
    cle = re.sub(r'[^a-z0-9]+', '-', titre.lower()).strip('-')
    try:
        d = json.loads(get(f'https://{lang}.wikipedia.org/w/api.php?' + urllib.parse.urlencode(
            {'action': 'query', 'prop': 'extracts', 'explaintext': 1, 'titles': titre, 'format': 'json', 'redirects': 1})))
        txt = next(iter(d['query']['pages'].values())).get('extract', '')
        open(os.path.join(OUT, f'page-{lang}-{cle}.txt'), 'w').write(txt)
        noter(f'Wikipédia page {lang} {titre}', len(txt) > 500, len(txt))
    except Exception as e:
        noter(f'Wikipédia page {lang} {titre}', False, repr(e))
    time.sleep(3)

for cle, url in [('ecowas', 'https://www.ecowas.int/'), ('ue-pays', 'https://european-union.europa.eu/principles-countries-history/eu-countries_fr'),
                 ('slavevoyages', 'https://www.slavevoyages.org/assessment/estimates')]:
    try:
        t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', get(url)))
        open(os.path.join(OUT, 'site-' + cle + '.txt'), 'w').write(t[:200000])
        noter('Site ' + cle, True, t[:300])
    except Exception as e:
        noter('Site ' + cle, False, repr(e))

json.dump(journal, open(os.path.join(OUT, 'journal.json'), 'w'), ensure_ascii=False, indent=1)
print('Terminé :', sum(1 for j in journal if j['ok']), '/', len(journal))
