#!/usr/bin/env python3
"""Prépare les photographies retenues (illustrations/selection.json) pour les téléphones :
redimensionnement (640 px au plus), JPEG optimisé de moins de 100 Ko, crédit complet.
Écrit illustrations/selection/<id>.jpg et illustrations/selection/credits.json, et une planche HTML
de validation (argument facultatif : chemin de la planche). N'intègre rien à l'application.
"""
import html
import json
import os
import sys

from PIL import Image

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAND = os.path.join(R, 'illustrations', 'candidats')
SEL = os.path.join(R, 'illustrations', 'selection')
MAX_OCTETS = 100 * 1024


def credit(c):
    auteur = c['auteur'] or ('Metropolitan Museum of Art' if 'Metropolitan' in c['credit'] else 'auteur non indiqué')
    if auteur.startswith('This photo was taken by Roman Bonnefoy'):
        auteur = 'Roman Bonnefoy'
    auteur = auteur.replace(' http://fr.wikipedia.org/wiki/User:Joker-x', '').replace('Unknown author Unknown author', 'auteur inconnu')
    return f"{auteur} — {c['licence']} — Wikimedia Commons"


def main():
    sel = json.load(open(os.path.join(R, 'illustrations', 'selection.json'), encoding='utf-8'))
    cand = {c['image']: c for c in json.load(open(os.path.join(CAND, 'candidats.json'), encoding='utf-8'))['candidats']}
    os.makedirs(SEL, exist_ok=True)
    sortie = []
    for p in sel['photos']:
        c = cand[p['source']]
        im = Image.open(os.path.join(CAND, p['source'])).convert('RGB')
        im.thumbnail((640, 640))
        chemin = os.path.join(SEL, p['id'] + '.jpg')
        for q in (78, 72, 66, 60, 54, 48):
            im.save(chemin, 'JPEG', quality=q, optimize=True, progressive=True)
            if os.path.getsize(chemin) <= MAX_OCTETS:
                break
        sortie.append(dict(p, fichier=p['id'] + '.jpg', largeur=im.width, hauteur=im.height, octets=os.path.getsize(chemin),
                           credit=credit(c), licence=c['licence'], licence_url=c['licence_url'], page_commons=c['page'],
                           fichier_commons=c['fichier']))
        print(f"{p['id']:<24} {im.width}x{im.height}  {os.path.getsize(chemin) // 1024} Ko  {c['licence']}")
    json.dump(sortie, open(os.path.join(SEL, 'credits.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if len(sys.argv) > 1:
        e = html.escape
        cartes = ''.join(f'''<figure><img src="{os.path.join(SEL, s['fichier'])}" alt="{e(s['titre'])}">
<figcaption><b>{i}. {e(s['titre'])}.</b> {e(s['legende'])}</figcaption>
<p class="expl">{e(s['explication'])}</p>
<p class="meta"><b>Emplacement prévu :</b> {e(s['emplacement'])}<br><b>Crédit :</b> {e(s['credit'])}<br>
<b>Fichier :</b> {e(s['fichier_commons'])} · {s['largeur']}×{s['hauteur']} px · {s['octets'] // 1024} Ko</p></figure>''' for i, s in enumerate(sortie, 1))
        total = sum(s['octets'] for s in sortie) // 1024
        page = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Photographies leçon pilote</title><style>
:root {{ --ink:#0f1a33; --muted:#55607a; --line:#d8deeb; --bg:#fff; --card:#f4f6fb; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --ink:#e9edf8; --muted:#9aa6c4; --line:#1f2f63; --bg:#060f2b; --card:#0c1a45; }} }}
:root[data-theme="dark"] {{ --ink:#e9edf8; --muted:#9aa6c4; --line:#1f2f63; --bg:#060f2b; --card:#0c1a45; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:15px/1.45 "Segoe UI",Roboto,Arial,sans-serif; }}
.doc {{ max-width:46rem; margin:0 auto; padding:18px 16px 40px; }} h1 {{ font-size:21px; margin:0 0 6px; }}
.chapo {{ color:var(--muted); }} figure {{ margin:0 0 22px; padding:12px; background:var(--card); border:1px solid var(--line); border-radius:12px; break-inside:avoid; }}
img {{ display:block; max-width:100%; max-height:360px; margin:0 auto 10px; border-radius:6px; }} figcaption {{ font-size:14.5px; }}
.expl {{ margin:8px 0 6px; }} .meta {{ margin:0; font-size:12.5px; color:var(--muted); word-break:break-word; }}
</style></head><body><div class="doc"><h1>Photographies proposées — leçon pilote « 6e – L'histoire et son objet »</h1>
<p class="chapo">{len(sortie)} photographies libres de droits (Wikimedia Commons), choisies parmi 30 candidates, optimisées pour les téléphones
(640 px au plus, {total} Ko au total). Proposition à valider : rien n'est encore intégré à l'application. Licences : domaine public,
CC0, CC BY-SA (le crédit doit alors être affiché sous l'image, ce qui est prévu).</p>{cartes}</div></body></html>'''
        open(sys.argv[1], 'w', encoding='utf-8').write(page)
        print('planche :', sys.argv[1])


if __name__ == '__main__':
    main()
