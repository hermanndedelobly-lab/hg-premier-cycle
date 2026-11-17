#!/usr/bin/env python3
"""Passerelle APK 1.10.0 → GNOMBLESSON, sans désinstallation ni nouvel APK.

L'APK 1.10.0 (clé de signature perdue) ne peut plus recevoir de nouvel APK, mais elle sait télécharger un contenu
corrigé depuis l'« Adresse du site des mises à jour » saisie dans ses Réglages. Ce script produit le dossier servi à
cette adresse (par défaut « pont/ ») :
  pont/version.json        même fichier que la racine ;
  pont/data/contenu.json   contenu GNOMBLESSON + lanceur (champ « pont ») ;
  pont/maj/page.html       page GNOMBLESSON (copie de maj/page.html, à régénérer avant).

La 1.10.0 affiche certains champs du contenu sans les neutraliser (nombre de leçons de l'accueil, durée d'une leçon
dans chaque page de classe) : on y place une image dont l'erreur de chargement exécute le lanceur. Le lanceur
nettoie les données (durées numériques, nombre de leçons, lanceur retiré), puis remplace la page par GNOMBLESSON,
avec les mêmes données locales (progression, scores, réglages). Mêmes sécurités que la mise à jour sans APK :
une version qui ne confirme pas son démarrage est écartée (code-essai / code-ok / code-echec) et « Revenir à la
version d'origine » rend la 1.10.0 normale.

Usage : python3 outils/fichier-unique.py maj/page.html --mode maj && python3 outils/fabriquer-pont.py [pont]
"""
import json
import os
import shutil
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORTIE = os.path.join(R, sys.argv[1] if len(sys.argv) > 1 else 'pont')

LANCEUR_CORPS = r"""
(function () {
  if (window.HG_PONT_FAIT || window.HG_MAJ) return;            // déjà lancé, ou déjà dans GNOMBLESSON
  window.HG_PONT_FAIT = true;
  function lire(k) { try { return localStorage.getItem('hg1c.' + k); } catch (e) { return null; } }
  function ecrire(k, v) { try { localStorage.setItem('hg1c.' + k, v); } catch (e) {} }
  function retablir(r) {   // la 1.10.0 d'origine redémarre (progression intacte) ; on peut revérifier plus tard
    try { localStorage.setItem('hg1c.maj-incident', JSON.stringify({ quand: Date.now(), raison: 'passerelle : ' + r }));
      localStorage.removeItem('hg1c.contenu-maj'); } catch (e) {}
    location.replace(location.href.split('#')[0]);
  }
  var d; try { d = JSON.parse(lire('contenu-maj')); } catch (e) { return; }
  if (!d || !d.classes) return;
  var V = d.version;
  // sécurité : une version qui n'a pas confirmé son démarrage au lancement précédent est écartée
  if (lire('code-echec') === V) return;
  if (lire('code-essai') === V && lire('code-ok') !== V) { ecrire('code-echec', V); return; }
  var base = ''; try { base = (JSON.parse(lire('reglages')) || {}).adresse || ''; } catch (e) {}
  base = base.replace(/\/+$/, '');
  function propre(x) {     // ancien format : données complètes salies par les déclencheurs
    var n = 0;
    x.classes.forEach(function (c) { c.disciplines.forEach(function (di) { di.themes.forEach(function (t) { t.lecons.forEach(function (l) {
      n++; if (typeof l.duree === 'string') l.duree = parseInt(l.duree, 10) || 0; }); }); }); });
    x.nbLecons = n; delete x.pont; return x;
  }
  function donnees() {
    if (!d.stub) return Promise.resolve(propre(d));
    return window.HGStock.lire(V).catch(function () {
      if (!base || !d.source) throw new Error('contenu complet introuvable');
      return fetch(new URL(d.source, base + '/').href, { cache: 'no-store' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })
        .then(function (t) { var x = JSON.parse(t); if (!x.classes || x.version !== V) throw new Error('contenu invalide');
          return window.HGStock.enregistrer(x, t, null, d).then(function () { return x; }); });
    });
  }
  function page() {
    var c = null; try { c = JSON.parse(lire('code-maj')); } catch (e) {}
    if (c && c.version === V && c.page) return Promise.resolve(c.page);
    if (!base) return Promise.reject(new Error('adresse absente'));
    return fetch(base + '/maj/page.html', { cache: 'no-store' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); }).then(function (p) {
      if (p.indexOf('window.HG_VERSION="' + V + '"') < 0) throw new Error('page invalide');
      ecrire('code-maj', JSON.stringify({ version: V, page: p })); return p;
    });
  }
  Promise.all([donnees(), page()]).then(function (r) {
    ecrire('code-essai', V);
    window.HG_DATA_PROPRE = r[0]; window.HG_VERSION_EMBARQUEE = '1.10.0';
    document.open(); document.write(r[1]); document.close();
  }).catch(function (e) { if (d.stub) retablir(e && e.message); });
})();
"""

DECLENCHEUR = ("<img src=\"pont-declencheur\" alt=\"\" style=\"display:none\" onerror=\"try{(new Function("
               "JSON.parse(localStorage.getItem('hg1c.contenu-maj')).pont))()}catch(e){}\">")

d = json.load(open(os.path.join(R, 'data', 'contenu.json'), encoding='utf-8'))
v = json.load(open(os.path.join(R, 'version.json'), encoding='utf-8'))
page = open(os.path.join(R, 'maj', 'page.html'), encoding='utf-8').read()
if v['version'] != d['version'] or ('window.HG_VERSION="%s"' % d['version']) not in page:
    sys.exit('versions différentes : version.json, data/contenu.json et maj/page.html doivent être identiques')
if "W.HG_DATA_PROPRE" not in page or "HGStock" not in page:
    sys.exit('maj/page.html sans chargeur v2 (HG_DATA_PROPRE, HGStock) : régénérer avec outils/fichier-unique.py --mode maj')

LANCEUR = open(os.path.join(R, 'outils', 'stockage-maj.js'), encoding='utf-8').read() + LANCEUR_CORPS
d['pont'] = LANCEUR
d['nbLecons'] = str(d['nbLecons']) + DECLENCHEUR
for c in d['classes']:          # une leçon par classe : chaque page de classe déclenche aussi
    l = c['disciplines'][0]['themes'][0]['lecons'][0]
    l['duree'] = str(l['duree']) + DECLENCHEUR

# stockage v2 : la 1.10.0 ne range plus que ce squelette (structure complète, textes longs vidés, lanceur et déclencheurs
# conservés) ; le contenu complet est lu à l'adresse « source » (relative à l'adresse de la passerelle) puis compressé.
def squelette(x, cle=''):
    if isinstance(x, str):
        return '' if (len(x) > 300 and cle != 'pont' and 'pont-declencheur' not in x) else x
    if isinstance(x, list):
        return [] if cle == 'quiz' else [squelette(y) for y in x]
    if isinstance(x, dict):   # données compactes des fiches enseignant (1.19.0) : inutiles dans le squelette
        return {k: squelette(v, k) for k, v in x.items() if k != 'fiche'}
    return x
d = squelette(d)
d['stub'] = True
d['stockage'] = 'compresse'
d['source'] = '../data/contenu.json'
os.makedirs(os.path.join(SORTIE, 'data'), exist_ok=True)
os.makedirs(os.path.join(SORTIE, 'maj'), exist_ok=True)
with open(os.path.join(SORTIE, 'data', 'contenu.json'), 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, separators=(',', ':'))
shutil.copyfile(os.path.join(R, 'version.json'), os.path.join(SORTIE, 'version.json'))
shutil.copyfile(os.path.join(R, 'maj', 'page.html'), os.path.join(SORTIE, 'maj', 'page.html'))
print('passerelle prête :', os.path.relpath(SORTIE, R), '| version', d['version'], '| squelette', os.path.getsize(os.path.join(SORTIE, 'data', 'contenu.json')), 'octets')
