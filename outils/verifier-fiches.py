#!/usr/bin/env python3
"""Contrôle des fiches de l'onglet Enseignant (depuis la 1.19.0) : le HTML reconstitué par l'application
(app.js, completerFiches, exécuté avec Node) doit être identique, caractère pour caractère, au HTML produit par
outils/espace-enseignant/construire.py. Usage : python3 outils/verifier-fiches.py [data/contenu.json]"""
import json, os, subprocess, sys, tempfile
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, 'outils', 'espace-enseignant'))
import construire  # noqa: E402

chemin = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RACINE, 'data', 'contenu.json')
with tempfile.TemporaryDirectory() as tmp:
    copie = os.path.join(tmp, 'contenu.json')
    D = json.load(open(chemin, encoding='utf-8'))
    json.dump(D, open(copie, 'w', encoding='utf-8'), ensure_ascii=False)
    construire.COMPLET.clear()
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):
        construire.main(copie)
    ref = os.path.join(tmp, 'ref.json')
    json.dump(construire.COMPLET, open(ref, 'w', encoding='utf-8'), ensure_ascii=False)
    js = r'''
const fs = require('fs');
const app = fs.readFileSync(process.argv[2], 'utf8');
const D = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')), REF = JSON.parse(fs.readFileSync(process.argv[4], 'utf8'));
new Function('D', app.slice(app.indexOf('  function ulF('), app.indexOf('  function completerTextes()')) + '\ncompleterFiches();')(D);
let n = 0, ok = 0, ecarts = [];
D.classes.forEach(c => (c.annexes || []).forEach(a => { if (!a.fiche) return; n++; if (a.html === REF[a.id]) ok++; else ecarts.push(a.id); }));
console.log(JSON.stringify({ n, ok, ecarts, attendues: Object.keys(REF).length }));
'''
    f = os.path.join(tmp, 'c.js'); open(f, 'w').write(js)
    r = json.loads(subprocess.run(['node', f, os.path.join(RACINE, 'app.js'), chemin, ref], capture_output=True, text=True, check=True).stdout)
print(f"fiches reconstituées identiques : {r['ok']} / {r['n']} (attendues : {r['attendues']})" + (f" ; écarts : {r['ecarts'][:10]}" if r['ecarts'] else ''))
sys.exit(0 if r['ok'] == r['n'] == r['attendues'] and r['n'] > 0 else 1)
