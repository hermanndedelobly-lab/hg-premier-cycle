#!/usr/bin/env python3
"""Récupère des sources officielles pour vérifier les contenus (exécuté par GitHub Actions, qui a accès à Internet).
Écrit dans sources/verification/ : rien n'est modifié dans l'application.
  1. Normales climatologiques OMM 1991-2020 (archive NOAA/NCEI, transmises par les services météorologiques
     nationaux, pour la Côte d'Ivoire la SODEXAM) : liste des fichiers, extraits des stations ivoiriennes.
  2. Notice bibliographique Crossref de l'étude publiée dans Nature (2025) sur Anyama / Bété I.
  3. Fiche de la liste indicative UNESCO « Parc archéologique d'Ahouakro » (5087).
  4. Décret n° 2017-322 (FAOLEX).
"""
import json
import os
import re
import subprocess
import urllib.parse
import urllib.request

OUT = os.path.join('sources', 'verification')
os.makedirs(OUT, exist_ok=True)
UA = {'User-Agent': 'gnomblesson-verification/1.0 (outil pedagogique)'}
journal = []


def get(url, binaire=False, timeout=120):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    return data if binaire else data.decode('utf-8', 'replace')


def noter(etape, ok, detail):
    journal.append({'etape': etape, 'ok': ok, 'detail': detail})
    print(('OK  ' if ok else 'ERR ') + etape + ' : ' + str(detail)[:300])


# 1. Normales OMM 1991-2020 (liste déjà établie : demande 2)
if os.environ.get('LISTE_OMM'):
  pass
BASE = 'https://www.ncei.noaa.gov/data/oceans/archive/arc0216/0253808/6.6/data/0-data/'
STATIONS = {'65578': 'Abidjan', '65555': 'Bouaké', '65536': 'Korhogo', '65562': 'Daloa', '65560': 'Man',
            '65548': 'Odienné', '65585': 'Sassandra', '65594': 'San-Pédro', '65599': 'Tabou', '65563': 'Dimbokro',
            '65545': 'Séguéla', '65557': 'Bondoukou', '65559': 'Gagnoa', '65556': 'Yamoussoukro'}
try:
    visites, a_voir, fichiers = set(), [BASE], []
    while a_voir and len(visites) < 60:
        u = a_voir.pop(0)
        if u in visites:
            continue
        visites.add(u)
        page = get(u, timeout=60)
        for lien in re.findall(r'href="([^"?#]+)"', page):
            if lien.startswith('/') or lien.startswith('..') or lien.startswith('http'):
                continue
            plein = urllib.parse.urljoin(u, lien)
            if lien.endswith('/'):
                if plein.startswith(BASE) and plein.count('/') - BASE.count('/') <= 3:
                    a_voir.append(plein)
            else:
                fichiers.append(plein)
    open(os.path.join(OUT, 'omm-normales-liste.txt'), 'w').write('\n'.join(fichiers))
    noter('OMM liste', True, f'{len(fichiers)} fichiers dans {len(visites)} répertoires')
    cibles = [f for f in fichiers if re.search(r'(Ivoire|Cote|COTE|IVORY|Ivory|CIV|_IV_|Region[-_ ]?1|Region_I\b|RA[-_ ]?I\b|Africa)', f)]
    noter('OMM fichiers Côte d\'Ivoire', bool(cibles), cibles[:20])
    for f in cibles[:40]:
        nom = os.path.basename(urllib.parse.unquote(f))
        try:
            data = get(f, binaire=True, timeout=300)
            chemin = os.path.join(OUT, 'omm-' + re.sub(r'[^A-Za-z0-9._-]', '_', nom))
            open(chemin, 'wb').write(data)
            noter('OMM téléchargement', True, nom + f' ({len(data)} octets)')
        except Exception as e:  # noqa: BLE001
            noter('OMM téléchargement', False, f'{nom} : {e}')
    # recherche des stations dans les fichiers texte téléchargés (CSV) et dans les archives zip
    extraits = []
    for nom in os.listdir(OUT):
        p = os.path.join(OUT, nom)
        if nom.endswith('.zip'):
            subprocess.run(['unzip', '-o', '-q', p, '-d', os.path.join(OUT, 'omm-zip')], check=False)
    for racine, _, noms in os.walk(OUT):
        for nom in noms:
            if not nom.lower().endswith(('.csv', '.txt')) or nom == 'omm-normales-liste.txt':
                continue
            p = os.path.join(racine, nom)
            try:
                lignes = open(p, encoding='utf-8', errors='replace').read().splitlines()
            except Exception:  # noqa: BLE001
                continue
            for i, l in enumerate(lignes):
                if any(s in l for s in STATIONS) or re.search(r'ABIDJAN|Abidjan', l):
                    extraits.append(os.path.relpath(p, OUT) + ' | ' + (lignes[0] if i else '') + ' | ' + l)
    open(os.path.join(OUT, 'omm-extraits-cote-divoire.txt'), 'w').write('\n'.join(extraits))
    noter('OMM extraits', bool(extraits), f'{len(extraits)} lignes')
except Exception as e:  # noqa: BLE001
    noter('OMM', False, str(e))

# 1 bis. Fichiers composites OMM : lignes des stations ivoiriennes (identifiants 655xx) et métadonnées
try:
    D = BASE
    pays = get(D + 'metadata/country_station_counts.csv')
    open(os.path.join(OUT, 'omm-pays-stations.csv'), 'w').write(pays)
    noter('OMM pays', True, [l for l in pays.splitlines() if re.search(r'Ivoire|IVOIRE|Ivory|IVORY', l)] or 'Côte d\'Ivoire absente de la liste des pays')
    for nom in ('metadata/wmo_normals_9120_8param_meta.csv', 'data-composite-primary-parameters/wmo_normals_9120_PRCP.csv',
                'data-composite-primary-parameters/wmo_normals_9120_TAVG.csv', 'data-composite-primary-parameters/wmo_normals_9120_TMAX.csv',
                'data-composite-primary-parameters/wmo_normals_9120_TMIN.csv', 'data-composite-primary-parameters/wmo_normals_9120_DP01.csv'):
        t = get(D + nom, timeout=600)
        lignes = t.splitlines()
        garde = [lignes[0]] + [l for l in lignes[1:] if re.search(r'(^|[,;"])655\d\d([,;"]|$)|Ivoire|IVOIRE|Ivory|IVORY|ABIDJAN|Abidjan', l)]
        open(os.path.join(OUT, 'omm-' + os.path.basename(nom).replace('.csv', '-cote-divoire.csv')), 'w').write('\n'.join(garde))
        noter('OMM ' + os.path.basename(nom), len(garde) > 1, f'{len(garde) - 1} lignes ivoiriennes sur {len(lignes) - 1}')
except Exception as e:  # noqa: BLE001
    noter('OMM composites', False, str(e))

# 1 ter. UNESCO : sites de métallurgie ancienne du fer du Burkina Faso (vocabulaire « bas fourneau »)
try:
    h = get('https://whc.unesco.org/fr/list/1602/')
    texte = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'(?s)<(script|style).*?</\1>', ' ', h)))
    open(os.path.join(OUT, 'unesco-1602-fr.txt'), 'w').write(texte)
    noter('UNESCO 1602', 'fourneau' in texte, [texte[m.start() - 150:m.start() + 250] for m in re.finditer('fourneau', texte)][:4])
except Exception as e:  # noqa: BLE001
    noter('UNESCO 1602', False, str(e))

# 2. Crossref : étude Nature 2025 sur Anyama (par son DOI)
try:
    r = json.loads(get('https://api.crossref.org/works/10.1038/s41586-025-08613-y'))['message']
    notice = {'titre': (r.get('title') or [''])[0], 'revue': (r.get('container-title') or [''])[0], 'doi': r.get('DOI'),
              'volume': r.get('volume'), 'numero': r.get('issue'), 'pages': r.get('page'),
              'en_ligne': (r.get('published-online') or {}).get('date-parts'), 'imprime': (r.get('published-print') or {}).get('date-parts'),
              'auteurs': [{'nom': ((a.get('given') or '') + ' ' + (a.get('family') or '')).strip(),
                           'affiliations': [x.get('name') for x in a.get('affiliation', [])]} for a in r.get('author', [])]}
    json.dump(notice, open(os.path.join(OUT, 'crossref-nature-anyama-doi.json'), 'w'), ensure_ascii=False, indent=1)
    noter('Crossref DOI', True, notice['titre'] + ' — ' + str(notice['volume']) + ' ' + str(notice['pages']))
except Exception as e:  # noqa: BLE001
    noter('Crossref DOI', False, str(e))
try:
    q = urllib.parse.urlencode({'query.bibliographic': 'rainforest human occupation 150,000 years Côte d\'Ivoire Anyama Bété',
                                'filter': 'from-pub-date:2024-06-01,until-pub-date:2025-12-31', 'rows': 10})
    r = json.loads(get('https://api.crossref.org/works?' + q))
    items = [{'titre': (i.get('title') or [''])[0], 'revue': (i.get('container-title') or [''])[0], 'doi': i.get('DOI'),
              'volume': i.get('volume'), 'pages': i.get('page'), 'numero': i.get('issue'),
              'date': (i.get('published') or i.get('issued') or {}).get('date-parts'),
              'auteurs': [((a.get('given') or '') + ' ' + (a.get('family') or '')).strip() for a in i.get('author', [])]}
             for i in r['message']['items']]
    json.dump(items, open(os.path.join(OUT, 'crossref-anyama.json'), 'w'), ensure_ascii=False, indent=1)
    noter('Crossref', True, [x['titre'][:90] + ' — ' + str(x['revue']) for x in items[:5]])
except Exception as e:  # noqa: BLE001
    noter('Crossref', False, str(e))

# 3. UNESCO, liste indicative 5087
for url, nom in (('https://whc.unesco.org/fr/listesindicatives/5087/', 'unesco-5087-fr.html'),
                 ('https://whc.unesco.org/en/tentativelists/5087/', 'unesco-5087-en.html')):
    try:
        h = get(url)
        texte = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'(?s)<(script|style).*?</\1>', ' ', h)))
        open(os.path.join(OUT, nom.replace('.html', '.txt')), 'w').write(texte)
        noter('UNESCO ' + nom, 'Ahouakro' in texte, texte[texte.find('Ahouakro') - 200: texte.find('Ahouakro') + 900] if 'Ahouakro' in texte else 'Ahouakro absent')
    except Exception as e:  # noqa: BLE001
        noter('UNESCO ' + nom, False, str(e))

# 4. Décret 2017-322 (FAOLEX)
try:
    pdf = get('https://faolex.fao.org/docs/pdf/IVC187426.pdf', binaire=True)
    open(os.path.join(OUT, 'decret-2017-322.pdf'), 'wb').write(pdf)
    subprocess.run(['pdftotext', '-layout', os.path.join(OUT, 'decret-2017-322.pdf'), os.path.join(OUT, 'decret-2017-322.txt')], check=False)
    t = open(os.path.join(OUT, 'decret-2017-322.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(os.path.join(OUT, 'decret-2017-322.txt')) else ''
    noter('Décret 2017-322', 'Ahouakro' in t, t[:600])
except Exception as e:  # noqa: BLE001
    noter('Décret 2017-322', False, str(e))

json.dump(journal, open(os.path.join(OUT, 'journal.json'), 'w'), ensure_ascii=False, indent=1)
