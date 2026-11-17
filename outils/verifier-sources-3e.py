#!/usr/bin/env python3
"""Lot 4 (3e) : vérification des références et des faits récents (exécuté par GitHub Actions).
Écrit dans sources/verification/lot4/ ; rien n'est modifié dans l'application.
  1. Open Library (recherche par titre) : ouvrages cités dans les espaces Culture générale de 3e.
  2. Wikipédia (API, source secondaire) : faits historiques, institutions (ONU, UA, OMC), données ivoiriennes.
  3. Wikipédia, texte complet de quelques articles (UA, CADHP, membres de l'ONU, Secrétaire général, Rwanda, Biafra, AOF).
  4. Sites officiels : ONU, UA, Commission africaine, Direction générale de l'économie, ONUSIDA.
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request

OUT = os.path.join('sources', 'verification', 'lot4')
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
    ('weiskel-1980', 'French Colonial Rule and the Baule Peoples'),
    ('brunschwig-1971', "Le partage de l'Afrique noire Brunschwig"),
    ('grah-mel', 'Félix Houphouët-Boigny biographie Grah Mel'),
    ('morgenthau-1964', 'Political Parties in French-Speaking West Africa'),
    ('stremlau-1977', 'The International Politics of the Nigerian Civil War'),
    ('achebe-2012', 'There Was a Country Achebe'),
    ('des-forges-1999', 'Leave None to Tell the Story Des Forges'),
    ('prunier-1995', 'The Rwanda Crisis History of a Genocide'),
    ('wieviorka-2023', 'Histoire totale de la Seconde Guerre mondiale'),
    ('hilberg', 'La destruction des Juifs d\'Europe Hilberg'),
    ('echenberg-1991', 'Colonial Conscripts Tirailleurs'),
    ('maurel-2015', 'Histoire des idées des Nations unies'),
    ('ruf-1995', 'Booms et crises du cacao'),
    ('carroue', 'Atlas de la mondialisation Carroué'),
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
    ('aof', 'Afrique-Occidentale française création 1895 organisation 1904'),
    ('abidjan-niger', 'Chemin de fer Abidjan-Niger construction 1904 Bouaké 1912'),
    ('biafra-reconnaissance', 'Biafra reconnaissance Côte d\'Ivoire 1968 Tanzanie Gabon Zambie Haïti'),
    ('msf', 'Médecins sans frontières fondation décembre 1971 Biafra'),
    ('rwanda-carte', 'Rwanda carte d\'identité mention ethnique 1931 1933 Belges'),
    ('rwanda-victimes', 'génocide des Tutsi nombre de victimes recensement 2002 1 074 017'),
    ('thiaroye', 'massacre de Thiaroye 1er décembre 1944'),
    ('charte-onu', 'Charte des Nations unies signature 26 juin 1945 50 États Pologne'),
    ('sg-onu-2027', 'Secrétaire général des Nations unies 2027 élu 2026'),
    ('cadhp', 'Charte africaine des droits de l\'homme et des peuples adoptée 27 juin 1981 Nairobi'),
    ('zlecaf', 'Zone de libre-échange continentale africaine entrée en vigueur 2019 échanges 2021'),
    ('cua-2025', 'Mahmoud Ali Youssouf président de la Commission de l\'Union africaine 2025'),
    ('ua-g20', 'Union africaine membre du G20 2023'),
    ('baleine', 'gisement Baleine Côte d\'Ivoire découverte 2021 production 2023'),
    ('rgph-2021', 'Recensement général de la population Côte d\'Ivoire 2021 29 389 150'),
    ('foret-ci', 'forêt Côte d\'Ivoire 16 millions hectares 1900 2,97 millions 2021'),
    ('vih-ci', 'VIH sida Côte d\'Ivoire prévalence adultes'),
    ('soubre', 'barrage de Soubré mise en service 2017'),
    ('brvm', 'Bourse régionale des valeurs mobilières 1996 1998 Abidjan'),
    ('omc-okonjo', 'Ngozi Okonjo-Iweala directrice générale OMC 2021'),
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
    ('fr', 'Union africaine'), ('fr', 'Charte africaine des droits de l\'homme et des peuples'), ('en', 'Member states of the United Nations'),
    ('fr', 'Secrétaire général des Nations unies'), ('en', '2026 United Nations Secretary-General selection'), ('fr', 'Génocide des Tutsi au Rwanda'),
    ('fr', 'Guerre du Biafra'), ('fr', 'Afrique-Occidentale française'), ('en', 'Demographics of Africa'), ('fr', 'Gisement Baleine'),
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

for cle, url in [('onu-membres', 'https://www.un.org/en/about-us/growth-in-un-membership'), ('ua-membres', 'https://au.int/en/member_states/countryprofiles2'),
                 ('cadhp', 'https://achpr.au.int/en/charter/african-charter-human-and-peoples-rights'), ('dge', 'https://www.dge.gouv.ci/'),
                 ('onusida-ci', 'https://www.unaids.org/fr/regionscountries/countries/cotedivoire')]:
    try:
        t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', get(url)))
        open(os.path.join(OUT, 'site-' + cle + '.txt'), 'w').write(t[:200000])
        noter('Site ' + cle, True, t[:300])
    except Exception as e:
        noter('Site ' + cle, False, repr(e))

json.dump(journal, open(os.path.join(OUT, 'journal.json'), 'w'), ensure_ascii=False, indent=1)
print('Terminé :', sum(1 for j in journal if j['ok']), '/', len(journal))
