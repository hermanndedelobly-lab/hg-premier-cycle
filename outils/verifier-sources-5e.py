#!/usr/bin/env python3
"""Lot 2 (5e) : récupère des sources publiques pour vérifier les références et chiffres cités
(exécuté par GitHub Actions, qui a accès à Internet). Écrit dans sources/verification/lot2/ :
rien n'est modifié dans l'application.
  1. UNESCO, patrimoine culturel immatériel : éléments de la Côte d'Ivoire et du Mali.
  2. UNESCO, patrimoine mondial : parcs de Taï et de la Comoé, mont Nimba.
  3. Open Library : notices des ouvrages cités.
  4. Crossref : notices des articles cités.
  5. Recherche publique (textes de loi, RGPH 2021) : premiers résultats, pour orienter la vérification.
"""
import html
import json
import os
import re
import urllib.parse
import urllib.request

OUT = os.path.join('sources', 'verification', 'lot2')
os.makedirs(OUT, exist_ok=True)
UA = {'User-Agent': 'gnomblesson-verification/1.0 (outil pedagogique)', 'Accept-Language': 'fr,en;q=0.8'}
journal = []


def get(url, timeout=90):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode('utf-8', 'replace')


def texte(page):
    page = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', page, flags=re.S | re.I)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', page))).strip()


def noter(etape, ok, detail):
    journal.append({'etape': etape, 'ok': ok, 'detail': detail})
    print(('OK  ' if ok else 'ERR ') + etape + ' : ' + str(detail)[:400])


def extraits(t, mots, largeur=220):
    res = []
    for m in mots:
        for x in re.finditer(re.escape(m), t, flags=re.I):
            res.append(t[max(0, x.start() - largeur):x.end() + largeur])
            if len(res) > 40:
                return res
    return res


# 1. Patrimoine culturel immatériel
for nom, url, mots in [
        ('pci-cote-divoire', 'https://ich.unesco.org/fr/etat/cote-d-ivoire-CI', ['Zaouli', 'Gbofe', 'balafon', 'attiéké', 'attieke']),
        ('pci-mali', 'https://ich.unesco.org/fr/etat/mali-ML', ['Manden', 'Kouroukan', 'balafon'])]:
    try:
        t = texte(get(url))
        open(os.path.join(OUT, nom + '.txt'), 'w').write(t)
        noter('UNESCO PCI ' + nom, True, extraits(t, mots)[:12])
    except Exception as e:
        noter('UNESCO PCI ' + nom, False, repr(e))

# 2. Patrimoine mondial
for num in ('195', '227', '155'):
    try:
        t = texte(get(f'https://whc.unesco.org/fr/list/{num}/'))
        open(os.path.join(OUT, f'whc-{num}.txt'), 'w').write(t)
        titre = re.search(r'(Parc national[^|.]{0,60}|Réserve naturelle intégrale[^|.]{0,60})', t)
        annee = re.findall(r'(?:Date d.inscription|inscrit[^0-9]{0,40})\s*:?\s*(1\d{3}|20\d{2})', t)
        noter(f'UNESCO WHC {num}', True, {'titre': titre.group(1) if titre else None, 'annees': annee[:5], 'debut': t[:300]})
    except Exception as e:
        noter(f'UNESCO WHC {num}', False, repr(e))

# 3. Ouvrages (Open Library)
LIVRES = [
    ('dozon-1985', 'Dozon', 'société bété'), ('dozon-2011', 'Dozon', 'clefs de la crise ivoirienne'),
    ('perrot-1982', 'Perrot', 'Anyi-Ndenye'), ('vogel-1997', 'Vogel', 'Baule African Art Western Eyes'),
    ('holas-1957', 'Holas', 'Les Sénoufo'), ('ruf-1995', 'Ruf', 'Booms et crises du cacao'),
    ('person-samori', 'Person', 'Samori une révolution dyula'), ('avenard-1971', 'Avenard', 'milieu naturel de la Côte d\'Ivoire'),
    ('vansina-1961', 'Vansina', 'De la tradition orale'), ('loucou-1984', 'Loucou', 'Histoire de la Côte d\'Ivoire'),
    ('niane-1960', 'Niane', 'Soundjata ou l\'épopée mandingue'), ('fauvelle-2013', 'Fauvelle', 'Le rhinocéros d\'or')]
notices = {}
for cle, auteur, titre in LIVRES:
    try:
        q = urllib.parse.urlencode({'author': auteur, 'title': titre, 'limit': 5,
                                    'fields': 'title,author_name,first_publish_year,publisher,publish_year,publish_place'})
        d = json.loads(get('https://openlibrary.org/search.json?' + q))
        docs = d.get('docs', [])
        notices[cle] = docs
        noter('Open Library ' + cle, bool(docs), [{k: x.get(k) for k in ('title', 'author_name', 'first_publish_year', 'publisher')} for x in docs[:3]])
    except Exception as e:
        noter('Open Library ' + cle, False, repr(e))
json.dump(notices, open(os.path.join(OUT, 'openlibrary.json'), 'w'), ensure_ascii=False, indent=1)

# 4. Articles (Crossref)
ARTICLES = [('griaule-1948', 'Griaule alliance cathartique Africa 1948'),
            ('radcliffe-brown-1940', 'Radcliffe-Brown On joking relationships Africa 1940'),
            ('chauveau-2006', 'Chauveau How does an institution evolve tutorat Gban Côte d\'Ivoire')]
cr = {}
for cle, q in ARTICLES:
    try:
        d = json.loads(get('https://api.crossref.org/works?' + urllib.parse.urlencode({'query.bibliographic': q, 'rows': 3})))
        items = d['message']['items']
        cr[cle] = items
        noter('Crossref ' + cle, bool(items), [{'titre': (x.get('title') or [''])[0], 'auteurs': [a.get('family') for a in x.get('author', [])],
                                               'revue': (x.get('container-title') or [''])[0], 'annee': (x.get('issued', {}).get('date-parts') or [[None]])[0][0],
                                               'volume': x.get('volume'), 'numero': x.get('issue'), 'doi': x.get('DOI')} for x in items])
    except Exception as e:
        noter('Crossref ' + cle, False, repr(e))
json.dump(cr, open(os.path.join(OUT, 'crossref.json'), 'w'), ensure_ascii=False, indent=1)

# 5. Recherche publique : textes de loi et RGPH 2021
RECHERCHES = [
    ('code-eau', 'loi n° 98-755 du 23 décembre 1998 portant Code de l\'eau Côte d\'Ivoire'),
    ('code-environnement', 'loi n° 96-766 du 3 octobre 1996 portant Code de l\'environnement Côte d\'Ivoire'),
    ('foncier-rural', 'loi n° 98-750 du 23 décembre 1998 relative au domaine foncier rural'),
    ('sachets-plastiques', 'Côte d\'Ivoire décret 2013 interdiction sachets plastiques'),
    ('anaged', 'ANAGED Agence nationale de gestion des déchets Côte d\'Ivoire création 2017'),
    ('code-forestier', 'Côte d\'Ivoire nouveau Code forestier 2019 loi'),
    ('rgph-2021', 'RGPH 2021 Côte d\'Ivoire résultats 29 389 150 habitants moins de 35 ans urbaine'),
    ('rgph-2021-etrangers', 'RGPH 2021 Côte d\'Ivoire population étrangère pourcentage non ivoiriens'),
    ('uemoa-pression-fiscale', 'UEMOA critère de convergence taux de pression fiscale 20 %'),
    ('kirina-niani', 'capitale de l\'empire du Mali Niani localisation débat archéologie')]
for cle, q in RECHERCHES:
    try:
        page = get('https://html.duckduckgo.com/html/?' + urllib.parse.urlencode({'q': q}))
        res = []
        for m in re.finditer(r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>.*?<a[^>]+class="result__snippet"[^>]*>(.*?)</a>', page, flags=re.S):
            lien = html.unescape(m.group(1))
            u = urllib.parse.parse_qs(urllib.parse.urlparse(lien).query).get('uddg', [lien])[0]
            res.append({'url': u, 'titre': texte(m.group(2)), 'extrait': texte(m.group(3))})
        json.dump(res, open(os.path.join(OUT, 'recherche-' + cle + '.json'), 'w'), ensure_ascii=False, indent=1)
        noter('Recherche ' + cle, bool(res), res[:3])
    except Exception as e:
        noter('Recherche ' + cle, False, repr(e))

json.dump(journal, open(os.path.join(OUT, 'journal.json'), 'w'), ensure_ascii=False, indent=1)
print('Terminé :', sum(1 for j in journal if j['ok']), '/', len(journal), 'étapes réussies')
