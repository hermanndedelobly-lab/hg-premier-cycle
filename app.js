/* Histoire géographie premier cycle — application hors ligne */
(function () {
  'use strict';
  var MODE = window.HG_MODE || 'single';
  var VERSION = window.HG_VERSION || '?';
  var D = null;                 // contenu
  var INDEX = {};               // id -> {type, classe, disc, theme, lecon|annexe}
  var ORDRE = {}, ORDRE_X = {};               // classe -> [ids des leçons dans l'ordre]
  var RECH = [];                // index de recherche
  var vue = document.getElementById('vue');
  var swReg = null, majEnAttente = null;

  // ---------- Stockage local (protégé) ----------
  function lire(k, def) { try { var v = localStorage.getItem('hg1c.' + k); return v === null ? def : JSON.parse(v); } catch (e) { return def; } }
  function ecrire(k, v) { try { localStorage.setItem('hg1c.' + k, JSON.stringify(v)); return true; } catch (e) { return false; } }
  function effacer(k) { try { localStorage.removeItem('hg1c.' + k); } catch (e) { /* rien */ } }
  function plusRecent(a, b) {
    var x = String(a || '0').split('.').map(Number), y = String(b || '0').split('.').map(Number);
    for (var i = 0; i < 3; i++) { if ((x[i] || 0) !== (y[i] || 0)) return (x[i] || 0) > (y[i] || 0); }
    return false;
  }
  var VERSION_ORIGINE = window.HG_DATA ? window.HG_DATA.version : null;
  var faites = lire('faites', {});
  var reglages = lire('reglages', { theme: 'auto', taille: 1, corriges: false });

  function appliquerReglages() {
    var r = document.documentElement;
    if (reglages.theme === 'auto') r.removeAttribute('data-theme'); else r.setAttribute('data-theme', reglages.theme);
    r.style.setProperty('--fs', reglages.taille);
  }
  appliquerReglages();

  // ---------- Outils ----------
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function norm(s) { return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); }
  function nbLecons(c) { return ORDRE[c.id].length; }
  function nbFaites(c) { return ORDRE[c.id].filter(function (id) { return faites[id]; }).length; }
  function nomTheme(t) { return t.n ? 'Thème ' + t.n : 'Complément'; }
  function heures(n) { return n ? n + ' h' : ''; }

  // ---------- Chargement ----------
  function charger() {
    if (window.HG_DATA) {
      // application Android : une mise à jour du contenu téléchargée remplace le contenu d'origine
      if (MODE === 'apk') {
        var m = lire('contenu-maj', null);
        if (m && m.classes && plusRecent(m.version, window.HG_DATA.version)) return Promise.resolve(m);
      }
      return Promise.resolve(window.HG_DATA);
    }
    return fetch('data/contenu.json').then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); });
  }

  function indexer() {
    D.classes.forEach(function (c) {
      ORDRE[c.id] = []; ORDRE_X[c.id] = [];
      c.disciplines.forEach(function (d) {
        d.themes.forEach(function (t) {
          t.lecons.forEach(function (l) {
            INDEX[l.id] = { type: 'lecon', classe: c, disc: d, theme: t, lecon: l };
            ORDRE[c.id].push(l.id);
            RECH.push({ id: l.id, href: '#l-' + l.id, classe: c.id, disc: d.id, titre: l.titre, ctx: c.id + ' · ' + d.nom + ' · ' + nomTheme(t), t: norm(l.titre + ' ' + t.titre), x: l.texte, nx: norm(l.texte) });
            if (l.banque) { ORDRE_X[c.id].push(l.id); RECH.push({ id: l.id, href: '#e-' + l.id, classe: c.id, disc: d.id, titre: 'Exercices : ' + l.titre, ctx: c.id + ' · Banque d\'exercices', t: norm('exercices ' + l.titre), x: l.texteBanque, nx: norm(l.texteBanque) }); }
          });
        });
      });
      (c.schemas || []).forEach(function (sc) { RECH.push({ id: sc.id, href: '#s-' + c.id, classe: c.id, disc: 'g', titre: 'Schéma : ' + sc.titre, ctx: c.id + ' · Schémas', t: norm(sc.titre), x: sc.texte, nx: norm(sc.texte) }); });
      c.annexes.forEach(function (a) {
        INDEX[a.id] = { type: 'annexe', classe: c, annexe: a };
        RECH.push({ id: a.id, href: '#l-' + a.id, classe: c.id, disc: '', titre: a.titre, ctx: c.id + ' · Annexe', t: norm(a.titre), x: a.texte, nx: norm(a.texte) });
      });
    });
  }

  // ---------- Barre des classes ----------
  function barreClasses(actif) {
    document.getElementById('classes').innerHTML = D.classes.map(function (c) {
      return '<a href="#c-' + c.id + '"' + (c.id === actif ? ' aria-current="page"' : '') + '><b>' + c.id + '</b><span>' + esc(c.nom) + '</span></a>';
    }).join('');
  }

  // ---------- Vues ----------
  function vueAccueil() {
    barreClasses(null);
    var der = lire('derniere', null);
    var h = '<p class="eyebrow">Programme ivoirien · APC</p><h1 class="titre-vue">Choisis une classe</h1>' +
      '<p class="chapo">' + D.nbLecons + ' leçons de la 6e à la 3e, chacune avec sa situation d\'apprentissage, le cours et des exercices corrigés. Tout fonctionne sans connexion.</p>';
    if (der && INDEX[der]) h += carteReprendre(der);
    h += '<div class="accueil-grille">' + D.classes.map(function (c) {
      var n = nbLecons(c), f = nbFaites(c);
      return '<a class="carte-classe" href="#c-' + c.id + '"><b>' + c.id + '</b><span>' + esc(c.nom) + '</span><small>' + n + ' leçons · ' + f + ' traitée' + (f > 1 ? 's' : '') + '</small><span class="mini"><i style="width:' + Math.round(100 * f / n) + '%"></i></span></a>';
    }).join('') + '</div>';
    h += '<a class="lien-carte" href="#apropos"><small>Version ' + esc(VERSION) + '</small>Réglages, mises à jour et installation</a>';
    afficher(h, 'Histoire géographie premier cycle');
  }

  function carteReprendre(id) {
    var e = INDEX[id], titre = e.type === 'lecon' ? e.lecon.titre : e.annexe.titre;
    return '<a class="reprendre" href="#l-' + id + '"><div><small>Reprendre · ' + e.classe.id + '</small><strong>' + esc(titre) + '</strong></div><span class="fleche" aria-hidden="true">→</span></a>';
  }

  function ongletsClasse(c, actif) {
    var nbS = (c.schemas || []).length;
    return '<nav class="onglets-classe" aria-label="Espaces de la classe">' +
      '<a href="#c-' + c.id + '"' + (actif === 'c' ? ' aria-current="page"' : '') + '>Cours</a>' +
      '<a href="#x-' + c.id + '"' + (actif === 'x' ? ' aria-current="page"' : '') + '>Exercices' + (c.nbBanque ? ' <span>' + c.nbBanque + '</span>' : '') + '</a>' +
      '<a href="#s-' + c.id + '"' + (actif === 's' ? ' aria-current="page"' : '') + '>Schémas' + (nbS ? ' <span>' + nbS + '</span>' : '') + '</a></nav>';
  }
  function vueClasse(c) {
    barreClasses(c.id);
    var n = nbLecons(c), f = nbFaites(c), nbT = 0;
    c.disciplines.forEach(function (d) { nbT += d.themes.filter(function (t) { return t.n; }).length; });
    var h = '<p class="eyebrow">Classe de ' + c.id + '</p><h1 class="titre-vue">' + esc(c.nom) + '</h1>' +
      '<p class="chapo">' + n + ' leçons réparties en ' + nbT + ' thèmes.</p>' + ongletsClasse(c, 'c') +
      '<div class="barre-progres"><span>' + f + ' / ' + n + ' traitées</span><span class="piste"><i style="width:' + Math.round(100 * f / n) + '%"></i></span></div>';
    var der = lire('derniere', null);
    if (der && INDEX[der] && INDEX[der].classe === c) h += carteReprendre(der);
    c.disciplines.forEach(function (d) {
      var hd = d.themes.reduce(function (a, t) { return a + t.lecons.reduce(function (b, l) { return b + (l.duree || 0); }, 0); }, 0);
      h += '<section class="discipline d-' + d.id + '"><div class="discipline-tete"><h2>' + esc(d.nom) + '</h2><span>' + hd + ' h de cours</span></div>';
      d.themes.forEach(function (t) {
        h += '<div class="theme"><div class="theme-tete"><p class="eyebrow">' + nomTheme(t) + '</p><h3>' + esc(t.titre === 'Complément' ? 'Leçon complémentaire' : t.titre) + '</h3></div><ul class="lecons">' +
          t.lecons.map(function (l) {
            return '<li class="' + (faites[l.id] ? 'fait' : '') + '"><a href="#l-' + l.id + '"><span class="num">L' + l.n + '</span><span class="t">' + esc(l.titre) + '</span><span class="meta">' + heures(l.duree) + '<span class="coche" aria-label="' + (faites[l.id] ? 'traitée' : 'non traitée') + '">✓</span></span></a></li>';
          }).join('') + '</ul></div>';
      });
      h += '</section>';
    });
    h += '<section class="discipline"><div class="discipline-tete" style="--c:var(--ink)"><h2>Ressources</h2></div><div class="liens-annexes">' +
      '<a class="lien-carte" href="#p-' + c.id + '"><small>Présentation</small>Programme et progression annuelle de ' + c.id + '</a>' +
      c.annexes.map(function (a) { return '<a class="lien-carte" href="#l-' + a.id + '"><small>Annexe</small>' + esc(a.titre) + '</a>'; }).join('') +
      '</div></section>';
    afficher(h, c.nom + ' · Histoire géographie');
  }

  function vueProgramme(c) {
    barreClasses(c.id);
    var h = '<div class="d-h"><nav class="fil"><a href="#c-' + c.id + '">' + c.id + '</a><span>›</span><span>Programme</span></nav>' +
      '<h1 class="lecon-titre">Programme et progression de ' + c.id + '</h1>' + BOUTON_PDF + '<div class="texte">' + c.programme + '</div></div>';
    afficher(h, 'Programme ' + c.id, { titre: 'Programme et progression de ' + c.id, surtitre: 'CLASSE DE ' + c.id.toUpperCase(), disc: 'h', fichier: c.id + ' programme', sections: [{ html: c.programme }] });
  }

  function vueAnnexe(e) {
    barreClasses(e.classe.id);
    ecrire('derniere', e.annexe.id);
    var h = '<div class="d-h"><nav class="fil"><a href="#c-' + e.classe.id + '">' + e.classe.id + '</a><span>›</span><span>Annexe</span></nav>' +
      '<h1 class="lecon-titre">' + esc(e.annexe.titre) + '</h1>' + BOUTON_PDF + '<div class="texte">' + e.annexe.html + '</div></div>';
    afficher(h, e.annexe.titre, { titre: e.annexe.titre, surtitre: 'CLASSE DE ' + e.classe.id.toUpperCase(), disc: 'h', fichier: e.classe.id + ' ' + e.annexe.titre, sections: [{ html: e.annexe.html }] });
  }

  function vueLecon(e) {
    var c = e.classe, d = e.disc, t = e.theme, l = e.lecon;
    barreClasses(c.id);
    ecrire('derniere', l.id);
    var ord = ORDRE[c.id], i = ord.indexOf(l.id);
    var prev = i > 0 ? INDEX[ord[i - 1]].lecon : null, next = i < ord.length - 1 ? INDEX[ord[i + 1]].lecon : null;
    var h = '<article class="d-' + d.id + '">' +
      '<nav class="fil" aria-label="Emplacement"><a href="#c-' + c.id + '">' + c.id + '</a><span>›</span><span>' + esc(d.nom) + '</span><span>›</span><span>' + nomTheme(t) + (t.n ? ' · ' + esc(t.titre) : '') + '</span></nav>' +
      '<h1 class="lecon-titre">' + esc(l.titre) + '</h1>' +
      '<div class="puces"><span class="puce">Leçon ' + l.n + '</span>' + (l.duree ? '<span class="puce">' + l.duree + ' h</span>' : '') + '<span class="puce">' + esc(d.nom) + '</span></div>' + BOUTON_PDF +
      '<div class="sommaire" role="navigation" aria-label="Parties de la leçon"><button type="button" data-aller="b-sit">Situation</button><button type="button" data-aller="b-cours">Cours</button><button type="button" data-aller="b-exo">Exercices</button>' + (l.banque ? '<a class="chip-lien" href="#e-' + l.id + '">Banque : ' + l.nbBanque + ' exercices</a>' : '') + '</div>' +
      '<section class="bloc" id="b-sit"><h2>Compétence, situation et habiletés</h2><div class="situation"><div class="texte">' + l.situation + '</div></div></section>' +
      '<section class="bloc" id="b-cours"><h2>Cours · trace écrite</h2><div class="texte">' + l.cours + '</div></section>' +
      '<section class="bloc" id="b-exo"><h2>Exercices traités et corrigés</h2>' +
      '<div class="outils-exo"><button type="button" class="btn" id="tous-corriges" aria-pressed="' + (reglages.corriges ? 'true' : 'false') + '">' + (reglages.corriges ? 'Masquer les corrigés' : 'Afficher tous les corrigés') + '</button>' +
      '<button type="button" class="btn" id="marquer" aria-pressed="' + (faites[l.id] ? 'true' : 'false') + '">' + (faites[l.id] ? '✓ Leçon traitée' : 'Marquer comme traitée') + '</button></div>' +
      '<div class="texte">' + l.exercices + '</div></section>' +
      '<nav class="suivants" aria-label="Leçons voisines">' +
      (prev ? '<a class="avant" href="#l-' + prev.id + '"><small>← Précédente</small><span>' + esc(prev.titre) + '</span></a>' : '') +
      (next ? '<a class="apres" href="#l-' + next.id + '"><small>Suivante →</small><span>' + esc(next.titre) + '</span></a>' : '') +
      '</nav></article>';
    afficher(h, l.titre, { titre: l.titre, disc: d.id, fichier: c.id + ' ' + d.id + ' lecon ' + l.n + ' ' + l.titre,
      surtitre: ('Classe de ' + c.id + ' · ' + d.nom + ' · ' + nomTheme(t)).toUpperCase(),
      meta: (t.n ? nomTheme(t) + ' : ' + t.titre + ' · ' : '') + 'Leçon ' + l.n + (l.duree ? ' · ' + l.duree + ' h' : ''),
      sections: [{ titre: 'Compétence, situation et habiletés', html: l.situation }, { titre: 'Cours · trace écrite', html: l.cours }, { titre: 'Exercices traités et corrigés', html: l.exercices }] });
    if (reglages.corriges) ouvrirCorriges(true);
    vue.querySelectorAll('[data-aller]').forEach(function (b) {
      b.addEventListener('click', function () { var cible = document.getElementById(b.getAttribute('data-aller')); if (cible) cible.scrollIntoView({ behavior: 'smooth', block: 'start' }); });
    });
    document.getElementById('tous-corriges').addEventListener('click', function () {
      reglages.corriges = !reglages.corriges; ecrire('reglages', reglages);
      this.setAttribute('aria-pressed', reglages.corriges ? 'true' : 'false');
      this.textContent = reglages.corriges ? 'Masquer les corrigés' : 'Afficher tous les corrigés';
      ouvrirCorriges(reglages.corriges);
    });
    document.getElementById('marquer').addEventListener('click', function () {
      if (faites[l.id]) delete faites[l.id]; else faites[l.id] = Date.now();
      ecrire('faites', faites);
      this.setAttribute('aria-pressed', faites[l.id] ? 'true' : 'false');
      this.textContent = faites[l.id] ? '✓ Leçon traitée' : 'Marquer comme traitée';
    });
  }
  function ouvrirCorriges(o) { vue.querySelectorAll('details.corrige').forEach(function (x) { x.open = o; }); }

  function vueExercicesClasse(c) {
    barreClasses(c.id);
    var h = '<p class="eyebrow">Classe de ' + c.id + '</p><h1 class="titre-vue">' + esc(c.nom) + '</h1>' + ongletsClasse(c, 'x') +
      '<p class="chapo">' + (c.nbBanque || 0) + ' exercices classés par leçon, chacun avec son corrigé détaillé. Les corrigés restent masqués jusqu\'à ce qu\'on les ouvre.</p>';
    if (!c.nbBanque) h += '<p class="vide">La banque d\'exercices de cette classe est en préparation : elle arrivera avec une prochaine mise à jour.</p>';
    c.disciplines.forEach(function (d) {
      h += '<section class="discipline d-' + d.id + '"><div class="discipline-tete"><h2>' + esc(d.nom) + '</h2></div>';
      d.themes.forEach(function (t) {
        h += '<div class="theme"><div class="theme-tete"><p class="eyebrow">' + nomTheme(t) + '</p><h3>' + esc(t.titre) + '</h3></div><ul class="lecons">' +
          t.lecons.map(function (l) {
            return '<li><a href="' + (l.banque ? '#e-' + l.id : '#l-' + l.id) + '"><span class="num">L' + l.n + '</span><span class="t">' + esc(l.titre) + '</span><span class="meta">' + (l.nbBanque ? l.nbBanque + ' exercices' : '—') + '</span></a></li>';
          }).join('') + '</ul></div>';
      });
      h += '</section>';
    });
    afficher(h, 'Exercices ' + c.id);
  }

  function vueBanque(e) {
    var c = e.classe, d = e.disc, l = e.lecon;
    barreClasses(c.id);
    var ord = ORDRE_X[c.id], i = ord.indexOf(l.id);
    var prev = i > 0 ? INDEX[ord[i - 1]].lecon : null, next = i < ord.length - 1 ? INDEX[ord[i + 1]].lecon : null;
    var h = '<article class="d-' + d.id + '"><nav class="fil"><a href="#x-' + c.id + '">' + c.id + ' · Exercices</a><span>›</span><span>' + esc(d.nom) + '</span></nav>' +
      '<h1 class="lecon-titre">' + esc(l.titre) + '</h1>' +
      '<div class="puces"><span class="puce">' + l.nbBanque + ' exercices</span><a class="puce puce-lien" href="#l-' + l.id + '">Revoir le cours</a></div>' + BOUTON_PDF +
      '<div class="outils-exo"><button type="button" class="btn" id="tous-corriges" aria-pressed="' + (reglages.corriges ? 'true' : 'false') + '">' + (reglages.corriges ? 'Masquer les corrigés' : 'Afficher tous les corrigés') + '</button></div>' +
      '<div class="texte">' + l.banque + '</div>' +
      '<nav class="suivants" aria-label="Banques voisines">' +
      (prev ? '<a class="avant" href="#e-' + prev.id + '"><small>← Précédente</small><span>' + esc(prev.titre) + '</span></a>' : '') +
      (next ? '<a class="apres" href="#e-' + next.id + '"><small>Suivante →</small><span>' + esc(next.titre) + '</span></a>' : '') +
      '</nav></article>';
    afficher(h, 'Exercices · ' + l.titre, { titre: 'Exercices : ' + l.titre, disc: d.id, fichier: c.id + ' ' + d.id + ' exercices lecon ' + l.n + ' ' + l.titre,
      surtitre: ('Classe de ' + c.id + ' · ' + d.nom + ' · Banque d\'exercices').toUpperCase(), meta: l.nbBanque + ' exercices avec corrigés détaillés',
      sections: [{ html: l.banque }] });
    if (reglages.corriges) ouvrirCorriges(true);
    document.getElementById('tous-corriges').addEventListener('click', function () {
      reglages.corriges = !reglages.corriges; ecrire('reglages', reglages);
      this.setAttribute('aria-pressed', reglages.corriges ? 'true' : 'false');
      this.textContent = reglages.corriges ? 'Masquer les corrigés' : 'Afficher tous les corrigés';
      ouvrirCorriges(reglages.corriges);
    });
  }

  function vueSchemas(c) {
    barreClasses(c.id);
    var sch = c.schemas || [];
    var h = '<div class="d-g"><p class="eyebrow">Classe de ' + c.id + '</p><h1 class="titre-vue">' + esc(c.nom) + '</h1>' + ongletsClasse(c, 's') +
      '<p class="chapo">Les cartes, frises, diagrammes et schémas de l\'année, avec la méthode pas à pas sur papier millimétré ou sur feuille de dessin ordinaire.</p>' + (sch.length ? BOUTON_PDF : '');
    if ((D.methode || []).length) {
      h += '<section class="bloc"><h2>Méthode générale</h2>' + D.methode.map(function (m) {
        return '<details class="schema"><summary><span><b>' + esc(m.titre) + '</b></span></summary><div class="texte">' + m.html + '</div></details>';
      }).join('') + '</section>';
    }
    h += '<section class="bloc"><h2>Les schémas de la ' + c.id + '</h2>';
    if (!sch.length) h += '<p class="vide">Les schémas de cette classe sont en préparation : ils arriveront avec une prochaine mise à jour.</p>';
    h += sch.map(function (s, i) {
      return '<details class="schema" id="' + s.id + '"><summary><span class="sch-num">' + (i + 1) + '</span><span><b>' + esc(s.titre) + '</b>' + (s.lecon ? '<small>' + esc(s.lecon) + '</small>' : '') + '</span></summary><div class="texte">' + s.html + '</div></details>';
    }).join('') + '</section></div>';
    var secs = [];
    if ((D.methode || []).length) secs.push({ titre: 'Méthode générale', html: D.methode.map(function (m) { return '<h3>' + esc(m.titre) + '</h3>' + m.html; }).join('') });
    if (sch.length) secs.push({ titre: 'Les schémas de la ' + c.id, html: sch.map(function (s, i) { return '<h3>' + (i + 1) + '. ' + esc(s.titre) + '</h3>' + (s.lecon ? '<p><em>' + esc(s.lecon) + '</em></p>' : '') + s.html; }).join('') });
    afficher(h, 'Schémas ' + c.id, { titre: 'Schémas et méthodes de la ' + c.id, disc: 'g', fichier: c.id + ' schemas', surtitre: ('Classe de ' + c.id + ' · Schémas').toUpperCase(), sections: secs });
  }

  var rechEtat = { q: lire('recherche', ''), classe: '' };
  function vueRecherche() {
    barreClasses(null);
    var h = '<p class="eyebrow">Toutes les classes</p><h1 class="titre-vue">Rechercher</h1>' +
      '<label class="eyebrow" for="q" style="display:block;margin-bottom:6px">Mot, notion, date ou nom</label>' +
      '<input id="q" class="champ" type="search" autocomplete="off" placeholder="Ex. : néolithique, CEDEAO, 1960, décentralisation" value="' + esc(rechEtat.q) + '">' +
      '<div class="filtres" role="group" aria-label="Filtrer par classe"><button type="button" data-cl="" aria-pressed="' + (rechEtat.classe === '' ? 'true' : 'false') + '">Toutes</button>' +
      D.classes.map(function (c) { return '<button type="button" data-cl="' + c.id + '" aria-pressed="' + (rechEtat.classe === c.id ? 'true' : 'false') + '">' + c.id + '</button>'; }).join('') + '</div>' +
      '<ul class="resultats" id="res"></ul>';
    afficher(h, 'Rechercher');
    var q = document.getElementById('q');
    q.addEventListener('input', function () { rechEtat.q = q.value; ecrire('recherche', q.value); chercher(); });
    vue.querySelectorAll('[data-cl]').forEach(function (b) {
      b.addEventListener('click', function () {
        rechEtat.classe = b.getAttribute('data-cl');
        vue.querySelectorAll('[data-cl]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        chercher();
      });
    });
    chercher();
    if (!rechEtat.q) q.focus();
  }
  function chercher() {
    var res = document.getElementById('res'); if (!res) return;
    var mots = norm(rechEtat.q).split(/\s+/).filter(function (m) { return m.length > 1; });
    if (!mots.length) { res.innerHTML = '<li class="vide">Tape au moins un mot de deux lettres. La recherche porte sur les titres, les cours, les exercices et les annexes des quatre classes.</li>'; return; }
    var trouves = [];
    RECH.forEach(function (r) {
      if (rechEtat.classe && r.classe !== rechEtat.classe) return;
      var score = 0;
      for (var i = 0; i < mots.length; i++) {
        var inT = r.t.indexOf(mots[i]) >= 0, inX = r.nx.indexOf(mots[i]) >= 0;
        if (!inT && !inX) return;
        score += inT ? 10 : 1;
      }
      trouves.push({ r: r, s: score });
    });
    trouves.sort(function (a, b) { return b.s - a.s; });
    if (!trouves.length) { res.innerHTML = '<li class="vide">Aucun résultat pour « ' + esc(rechEtat.q) + ' ». Essaie un autre mot ou retire le filtre de classe.</li>'; return; }
    res.innerHTML = trouves.slice(0, 60).map(function (o) {
      var r = o.r, p = r.nx.indexOf(mots[0]), deb = Math.max(0, p - 70);
      var ext = (deb > 0 ? '… ' : '') + r.x.slice(deb, deb + 190) + ' …';
      return '<li class="d-' + (r.disc || 'h') + '"><a href="' + r.href + '"><span class="r-meta">' + esc(r.ctx) + '</span><span class="r-titre">' + surligner(r.titre, mots) + '</span><span class="r-extrait">' + surligner(ext, mots) + '</span></a></li>';
    }).join('') + (trouves.length > 60 ? '<li class="vide">' + (trouves.length - 60) + ' autres résultats : précise ta recherche.</li>' : '');
  }
  function surligner(txt, mots) {
    // surlignage insensible aux accents : on travaille sur la version normalisée (même longueur caractère par caractère)
    var n = norm(txt), marques = [];
    mots.forEach(function (m) { var i = 0; while ((i = n.indexOf(m, i)) >= 0) { marques.push([i, i + m.length]); i += m.length; } });
    if (n.length !== txt.length || !marques.length) return esc(txt);
    marques.sort(function (a, b) { return a[0] - b[0]; });
    var out = '', pos = 0;
    marques.forEach(function (mk) { if (mk[0] < pos) return; out += esc(txt.slice(pos, mk[0])) + '<mark>' + esc(txt.slice(mk[0], mk[1])) + '</mark>'; pos = mk[1]; });
    return out + esc(txt.slice(pos));
  }

  function vueReglages() {
    barreClasses(null);
    var enLigne = navigator.onLine;
    var installee = window.matchMedia && window.matchMedia('(display-mode: standalone)').matches;
    var h = '<p class="eyebrow">Application</p><h1 class="titre-vue">Réglages et mises à jour</h1><div class="reglages">' +
      '<section class="panneau"><h2>Version installée</h2><p><span class="version-num">' + esc(VERSION) + '</span> · contenu du ' + esc(dateFr(D.date)) + '</p>' +
      '<div class="ligne"><span class="etat' + (enLigne ? ' ok' : '') + '">' + (enLigne ? 'En ligne' : 'Hors ligne') + '</span>' +
      (MODE === 'pwa' ? '<span class="etat' + (navigator.serviceWorker && navigator.serviceWorker.controller ? ' ok' : '') + '">' + (navigator.serviceWorker && navigator.serviceWorker.controller ? 'Disponible hors ligne' : 'Préparation hors ligne…') + '</span>' : '<span class="etat ok">' + (MODE === 'apk' ? 'Application Android' : 'Fichier autonome') + '</span>') + '</div>' +
      '<p style="margin-top:12px"><button type="button" class="btn btn-plein" id="verifier">Vérifier les mises à jour</button></p><p class="msg" id="msg-maj" role="status"></p>' +
      (MODE === 'apk' ? panneauAdresse() : '') +
      '<h2 style="margin-top:14px">Journal des corrections</h2><ul class="notes">' + D.notes.map(function (n) { return '<li>' + esc(n) + '</li>'; }).join('') + '</ul></section>' +
      '<section class="panneau"><h2>Lecture</h2><p>Taille du texte des cours</p><div class="ligne" role="group" aria-label="Taille du texte">' +
      [[0.92, 'Petite'], [1, 'Normale'], [1.12, 'Grande'], [1.25, 'Très grande']].map(function (t) { return '<button type="button" class="btn" data-taille="' + t[0] + '" aria-pressed="' + (reglages.taille === t[0] ? 'true' : 'false') + '">' + t[1] + '</button>'; }).join('') + '</div>' +
      '<p style="margin-top:12px">Apparence</p><div class="ligne" role="group" aria-label="Apparence">' +
      [['auto', 'Comme le téléphone'], ['light', 'Claire'], ['dark', 'Sombre']].map(function (t) { return '<button type="button" class="btn" data-theme-choix="' + t[0] + '" aria-pressed="' + (reglages.theme === t[0] ? 'true' : 'false') + '">' + t[1] + '</button>'; }).join('') + '</div></section>' +
      '<section class="panneau"><h2>Suivi de progression</h2><p>' + Object.keys(faites).length + ' leçon(s) marquée(s) comme traitée(s) sur cet appareil.</p><div class="ligne"><button type="button" class="btn" id="raz">Remettre le suivi à zéro</button><span class="msg" id="msg-raz"></span></div></section>' +
      '<section class="panneau" id="install"><h2>Installer sur le téléphone</h2>' + aideInstall(installee) + '</section>' +
      '<section class="panneau"><h2>À propos</h2><p>Support pédagogique pour l\'enseignant, rédigé à partir des programmes éducatifs ivoiriens (APC) du premier cycle. Vérifiez la progression auprès de votre conseiller pédagogique ou de l\'antenne pédagogique.</p></section>' +
      '</div>';
    afficher(h, 'Réglages');
    document.getElementById('verifier').addEventListener('click', verifierMaj);
    vue.querySelectorAll('[data-taille]').forEach(function (b) { b.addEventListener('click', function () { reglages.taille = +b.getAttribute('data-taille'); ecrire('reglages', reglages); appliquerReglages(); vueReglages(); }); });
    vue.querySelectorAll('[data-theme-choix]').forEach(function (b) { b.addEventListener('click', function () { reglages.theme = b.getAttribute('data-theme-choix'); ecrire('reglages', reglages); appliquerReglages(); vueReglages(); }); });
    var raz = document.getElementById('raz'), arme = false;
    raz.addEventListener('click', function () {
      if (!arme) { arme = true; raz.textContent = 'Confirmer la remise à zéro'; document.getElementById('msg-raz').textContent = 'Appuie encore pour confirmer.'; return; }
      faites = {}; ecrire('faites', faites); vueReglages();
    });
    var fa = document.getElementById('form-adresse');
    if (fa) fa.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var v = document.getElementById('adresse').value.trim().replace(/\/+$/, '');
      if (v && !/^https:\/\/[^\s/]+\.[^\s]+$/.test(v)) { message('L\'adresse doit commencer par https:// (exemple : https://hg-premier-cycle.netlify.app).'); return; }
      reglages.adresse = v; ecrire('reglages', reglages);
      if (v) verifierMajApk(true); else message('Adresse effacée : les mises à jour en ligne sont désactivées.');
    });
    var ro = document.getElementById('retour-origine');
    if (ro) ro.addEventListener('click', function () { effacer('contenu-maj'); location.reload(); });
    var bi = document.getElementById('btn-installer');
    if (bi) bi.addEventListener('click', function () { if (!invite) return; invite.prompt(); invite.userChoice.then(function () { invite = null; vueReglages(); }); });
  }
  function panneauAdresse() {
    return '<form id="form-adresse" style="margin-top:12px"><label for="adresse" style="display:block;font-weight:700;margin-bottom:4px">Adresse du site des mises à jour</label>' +
      '<p class="msg" style="margin:0 0 8px">Le site où les versions corrigées sont publiées. À renseigner une seule fois.</p>' +
      '<div class="ligne"><input id="adresse" class="champ" style="flex:1 1 14rem;font-size:15px;padding:10px 12px" type="url" inputmode="url" autocomplete="off" placeholder="https://…" value="' + esc(reglages.adresse || '') + '">' +
      '<button type="submit" class="btn">Enregistrer</button></div></form>' +
      (VERSION_ORIGINE && VERSION !== VERSION_ORIGINE ? '<p class="msg" style="margin-top:10px">Contenu mis à jour (version d\'origine de l\'application : ' + esc(VERSION_ORIGINE) + '). <button type="button" class="btn" id="retour-origine">Revenir au contenu d\'origine</button></p>' : '');
  }
  function aideInstall(installee) {
    if (MODE === 'apk') return '<p>L\'application Android est installée : tous les cours sont dans le téléphone et fonctionnent sans connexion. Pour installer une nouvelle version de l\'application elle-même, ouvre le nouveau fichier .apk : tes réglages et ton suivi sont conservés.</p>';
    if (MODE !== 'pwa') return '<p>Tu utilises la version « fichier unique » : elle s\'ouvre dans le navigateur, sans connexion, mais ne se met pas à jour seule. Pour l\'installer comme une application avec les mises à jour automatiques, ouvre l\'adresse en ligne de l\'application dans Chrome puis choisis « Installer ».</p>';
    if (installee) return '<p>L\'application est installée sur cet appareil. Les cours restent disponibles sans connexion.</p>';
    return (invite ? '<p><button type="button" class="btn btn-plein" id="btn-installer">Installer l\'application</button></p>' : '') +
      '<ol class="etapes"><li><b>Android (Chrome)</b> : menu ⋮ puis « Installer l\'application » ou « Ajouter à l\'écran d\'accueil ».</li><li><b>iPhone (Safari)</b> : bouton Partager puis « Sur l\'écran d\'accueil ».</li><li><b>Ordinateur (Chrome, Edge)</b> : icône d\'installation à droite de la barre d\'adresse.</li></ol>' +
      '<p style="margin-top:10px">Ouvre chaque classe une fois après l\'installation : tout le contenu est déjà enregistré pour l\'usage hors ligne.</p>';
  }
  function dateFr(iso) {
    var m = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
    var p = (iso || '').split('-'); return p.length === 3 ? (+p[2]) + ' ' + m[+p[1] - 1] + ' ' + p[0] : iso;
  }

  var PDF_SPEC = null;
  var BOUTON_PDF = '<button type="button" class="btn btn-pdf" data-pdf><span aria-hidden="true">⤓</span> PDF · Partager · Imprimer</button>';
  function afficher(h, titre, spec) {
    PDF_SPEC = spec || null;
    vue.innerHTML = h;
    var bp = vue.querySelector('[data-pdf]');
    if (bp) bp.addEventListener('click', function () { if (window.HGPDF && PDF_SPEC) window.HGPDF.ouvrir(PDF_SPEC); });
    document.title = titre === 'Histoire géographie premier cycle' ? titre : titre + ' · HG premier cycle';
    window.scrollTo(0, 0);
    mesurerEntete();
  }
  function mesurerEntete() {
    var t = document.querySelector('.topbar'); if (t) document.documentElement.style.setProperty('--hdr', t.offsetHeight + 'px');
  }
  window.addEventListener('resize', mesurerEntete);

  // ---------- Routage ----------
  function route() {
    var h = (location.hash || '').slice(1), e, c;
    if (!h || h === 'accueil') {
      var dc = lire('classe', null);
      if (!h && dc && trouverClasse(dc)) return vueClasse(trouverClasse(dc));
      return vueAccueil();
    }
    if (h === 'recherche') return vueRecherche();
    if (h === 'apropos') return vueReglages();
    if (h.indexOf('c-') === 0 && (c = trouverClasse(h.slice(2)))) { ecrire('classe', c.id); return vueClasse(c); }
    if (h.indexOf('p-') === 0 && (c = trouverClasse(h.slice(2)))) return vueProgramme(c);
    if (h.indexOf('x-') === 0 && (c = trouverClasse(h.slice(2)))) return vueExercicesClasse(c);
    if (h.indexOf('s-') === 0 && (c = trouverClasse(h.slice(2)))) return vueSchemas(c);
    if (h.indexOf('e-') === 0 && (e = INDEX[h.slice(2)]) && e.lecon && e.lecon.banque) return vueBanque(e);
    if (h.indexOf('l-') === 0 && (e = INDEX[h.slice(2)])) return e.type === 'lecon' ? vueLecon(e) : vueAnnexe(e);
    vueAccueil();
  }
  function trouverClasse(id) { for (var i = 0; i < D.classes.length; i++) if (D.classes[i].id === id) return D.classes[i]; return null; }
  window.addEventListener('hashchange', route);

  // ---------- Installation et mises à jour (version application) ----------
  var invite = null;
  window.addEventListener('beforeinstallprompt', function (ev) { ev.preventDefault(); invite = ev; });

  function bandeau(texte, ok) {
    document.getElementById('bandeau-texte').textContent = texte;
    document.getElementById('bandeau').hidden = false;
    document.getElementById('maj-dot').hidden = false;
    document.getElementById('bandeau-ok').onclick = ok;
  }
  document.getElementById('bandeau-plus-tard').addEventListener('click', function () { document.getElementById('bandeau').hidden = true; });

  function annoncerMaj(worker) {
    majEnAttente = worker;
    fetch('version.json', { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (v) {
      bandeau('Version ' + v.version + ' disponible : ' + (v.notes && v.notes[0] ? v.notes[0] : 'corrections du contenu') , appliquerMaj);
    }).catch(function () { bandeau('Une nouvelle version des cours est prête.', appliquerMaj); });
  }
  function appliquerMaj() {
    var b = document.getElementById('bandeau-ok'); b.textContent = 'Mise à jour…'; b.disabled = true;
    if (majEnAttente) majEnAttente.postMessage({ type: 'SKIP_WAITING' }); else location.reload();
  }

  function message(t) { var m = document.getElementById('msg-maj'); if (m) m.textContent = t; }

  // Application Android : le contenu corrigé est téléchargé depuis le site des mises à jour
  // (mêmes fichiers version.json et data/contenu.json que la version web) puis gardé dans le téléphone.
  function verifierMajApk(manuel) {
    var base = (reglages.adresse || '').trim().replace(/\/+$/, '');
    if (!base) { if (manuel) message('Renseigne d\'abord l\'adresse du site des mises à jour, juste en dessous.'); return; }
    if (!navigator.onLine) { if (manuel) message('Pas de connexion. Réessaie quand le téléphone est connecté : tes cours restent disponibles en attendant.'); return; }
    if (manuel) message('Vérification en cours…');
    fetch(base + '/version.json', { cache: 'no-store' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (v) {
      if (!plusRecent(v.version, VERSION)) { if (manuel) message('Tu as la dernière version (' + VERSION + ').'); return; }
      var deja = lire('contenu-maj', null);
      if (deja && deja.version === v.version) { message('Version ' + v.version + ' prête.'); bandeau('Version ' + v.version + ' prête : redémarre pour l\'utiliser.', function () { location.reload(); }); return; }
      if (manuel) message('Version ' + v.version + ' trouvée. Téléchargement en cours…');
      return fetch(base + '/data/contenu.json', { cache: 'no-store' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (d) {
        if (!d || !d.classes || !d.classes.length || d.version !== v.version) throw new Error('contenu invalide');
        if (!ecrire('contenu-maj', d)) { message('Le téléphone manque de place pour enregistrer la mise à jour.'); return; }
        message('Version ' + v.version + ' téléchargée.');
        bandeau('Version ' + v.version + ' téléchargée : ' + (v.notes && v.notes[0] ? v.notes[0] : 'corrections du contenu'), function () { location.reload(); });
      });
    }).catch(function () { if (manuel) message('Le site des mises à jour ne répond pas. Vérifie l\'adresse ou réessaie plus tard.'); });
  }

  function verifierMaj() {
    var msg = document.getElementById('msg-maj');
    if (MODE === 'apk') return verifierMajApk(true);
    if (MODE !== 'pwa') { msg.textContent = 'La version fichier unique ne se met pas à jour seule : remplace le fichier par la nouvelle version quand elle est diffusée.'; return; }
    if (!navigator.onLine) { msg.textContent = 'Pas de connexion. Réessaie quand le téléphone est connecté : tes cours restent disponibles en attendant.'; return; }
    msg.textContent = 'Vérification en cours…';
    fetch('version.json', { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (v) {
      if (v.version === VERSION) { msg.textContent = 'Tu as la dernière version (' + VERSION + ').'; return; }
      msg.textContent = 'Version ' + v.version + ' trouvée. Téléchargement en cours…';
      if (swReg) swReg.update().then(function () { if (swReg.waiting) annoncerMaj(swReg.waiting); });
    }).catch(function () { msg.textContent = 'Le serveur des mises à jour ne répond pas. Réessaie plus tard.'; });
  }

  function initSW() {
    if (MODE !== 'pwa' || !('serviceWorker' in navigator)) return;
    var rechargement = false;
    navigator.serviceWorker.addEventListener('controllerchange', function () { if (rechargement) return; rechargement = true; location.reload(); });
    navigator.serviceWorker.register('sw.js').then(function (reg) {
      swReg = reg;
      if (reg.waiting && navigator.serviceWorker.controller) annoncerMaj(reg.waiting);
      reg.addEventListener('updatefound', function () {
        var w = reg.installing;
        w.addEventListener('statechange', function () {
          if (w.state === 'installed' && navigator.serviceWorker.controller) annoncerMaj(w);
        });
      });
      // vérification automatique au démarrage puis à chaque retour dans l'application
      if (navigator.onLine) reg.update().catch(function () {});
      document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'visible' && navigator.onLine) reg.update().catch(function () {}); });
    }).catch(function () { /* hors ligne au premier lancement */ });
  }

  // ---------- Démarrage ----------
  charger().then(function (data) {
    D = data; VERSION = data.version || VERSION;
    indexer(); route(); initSW();
    if (MODE === 'apk') {
      setTimeout(function () { verifierMajApk(false); }, 1500);
      document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'visible') verifierMajApk(false); });
    }
  }).catch(function () {
    vue.innerHTML = '<h1 class="titre-vue">Cours introuvables</h1><p>Le contenu n\'a pas pu être chargé. Connecte le téléphone une fois et rouvre l\'application pour enregistrer les cours.</p>';
  });
})();

/* Histoire géographie premier cycle — export PDF (télécharger, partager, imprimer)
   Chaque fiche est mise en page en PDF A4 avec le nom de l'auteur en filigrane discret.
   Bibliothèque : pdfmake (chargée à la demande depuis lib/). */
(function () {
  'use strict';
  var AUTEUR = 'Gnomblesson Hermann Vallès';
  var SITE = 'https://hermanndedelobly-lab.github.io/hg-premier-cycle/';
  var C = { ink: '#1c2522', muted: '#5b6660', line: '#d8d8cd', brand: '#1f3b33', hist: '#a9501c', histSoft: '#f7ece3', geo: '#1c6573', geoSoft: '#e4f0f2', ok: '#2f7a4a', bg: '#f3f2ec', surface: '#fbfaf6' };

  // ---------- chargement de pdfmake ----------
  var chargement = null;
  function script(src) {
    return new Promise(function (ok, ko) { var s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = function () { ko(new Error('chargement ' + src)); }; document.head.appendChild(s); });
  }
  function charger() {
    if (window.pdfMake && window.pdfMake.vfs) return Promise.resolve();
    if (chargement) return chargement;
    var base = (window.HG_MODE === 'single') ? SITE + 'lib/' : 'lib/';
    chargement = script(base + 'pdfmake.min.js').then(function () { return script(base + 'vfs_fonts.js'); })
      .catch(function (e) { chargement = null; throw e; });
    return chargement;
  }

  // ---------- conversion HTML -> pdfmake ----------
  var SVG_STYLE = {
    'g-mm': { stroke: '#d68034', 'stroke-opacity': '0.14', 'stroke-width': '0.6' },
    'g-cm': { 'stroke-opacity': '0.3', 'stroke-width': '0.9' },
    'g-axe': { stroke: C.ink, 'stroke-width': '1.6' },
    'g-fleche': { fill: C.ink },
    'g-rappel': { stroke: C.muted, 'stroke-width': '1', 'stroke-dasharray': '3 3', fill: 'none' },
    'g-point': { fill: C.hist },
    'g-txt': { fill: C.ink, 'font-size': '13' },
    'g-petit': { fill: C.ink, 'font-size': '11' },
    'g-pluie': { fill: C.geo }, 'g-temp': { fill: C.hist },
    'g-barre-pluie': { fill: C.geo, 'fill-opacity': '0.75' }, 'g-barre': { fill: C.geo, 'fill-opacity': '0.75' },
    'g-courbe-temp': { fill: 'none', stroke: C.hist, 'stroke-width': '2.4' }, 'g-courbe': { fill: 'none', stroke: C.hist, 'stroke-width': '2.4' },
    'g-point-temp': { fill: C.hist },
    'g-h': { fill: C.geo, 'fill-opacity': '0.8' }, 'g-f': { fill: C.hist, 'fill-opacity': '0.8' },
    'g-boite': { fill: C.surface, stroke: C.brand, 'stroke-width': '1.6' },
    'g-periode': { stroke: '#ffffff', 'stroke-width': '1', 'fill-opacity': '0.55' }, 'g-part': { stroke: '#ffffff', 'stroke-width': '1' },
    p0: { fill: C.geo }, p1: { fill: C.hist }, p2: { fill: '#d6a234' }, p3: { fill: '#6c8f4e' }, p4: { fill: '#8a6bb0' }, p5: { fill: '#9aa4a0' }
  };
  function svgPdf(svg) {
    var s = svg.cloneNode(true);
    s.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    s.querySelectorAll('*').forEach(function (el) {
      var cl = (el.getAttribute('class') || '').split(/\s+/);
      cl.forEach(function (k) { var st = SVG_STYLE[k]; if (st) Object.keys(st).forEach(function (a) { el.setAttribute(a, st[a]); }); });
      var style = el.getAttribute('style');
      if (style) { var m = style.match(/font-size:\s*([\d.]+)px/); if (m) el.setAttribute('font-size', m[1]); el.removeAttribute('style'); }
      if (el.tagName.toLowerCase() === 'text') el.setAttribute('font-family', 'Roboto');
      if (/^(text|tspan)$/i.test(el.tagName) && !el.children.length && FLECHE.test(el.textContent)) {
        var parts = el.textContent.split(FLECHE); el.textContent = '';
        parts.forEach(function (x) { if (!x) return; var ts = document.createElementNS('http://www.w3.org/2000/svg', 'tspan'); if (FLECHE.test(x)) ts.setAttribute('font-family', 'Fleches'); ts.textContent = x; el.appendChild(ts); });
      }
      el.removeAttribute('class');
    });
    s.removeAttribute('class'); s.removeAttribute('style');
    var vb = (s.getAttribute('viewBox') || '0 0 640 300').split(/\s+/).map(Number);
    s.setAttribute('width', vb[2]); s.setAttribute('height', vb[3]);
    return { svg: new XMLSerializer().serializeToString(s), width: Math.min(480, vb[2] * 0.75), alignment: 'center', margin: [0, 4, 0, 2] };
  }

  function nettoie(t) { return t.replace(/\s+/g, ' '); }
  // Les flèches (→ ↓ ↔…) absentes de Roboto sont écrites avec la petite police « Fleches ».
  var FLECHE = /([\u2190-\u21ff\u27f5\u27f6\u25b2\u25bc\u2713])/;
  function morceaux(t, st) {
    return t.split(FLECHE).filter(function (x) { return x !== ''; }).map(function (x) {
      var r = Object.assign({ text: x }, st); if (FLECHE.test(x)) r.font = 'Fleches'; return r;
    });
  }
  function enLigne(node, st) {
    // renvoie une liste de fragments de texte {text, bold, italics}
    st = st || {};
    var out = [];
    node.childNodes.forEach(function (n) {
      if (n.nodeType === 3) { var t = nettoie(n.nodeValue); if (t) out = out.concat(morceaux(t, st)); return; }
      if (n.nodeType !== 1) return;
      var tag = n.tagName.toLowerCase();
      if (tag === 'br') { out.push({ text: '\n' }); return; }
      if (tag === 'strong' || tag === 'b') { out = out.concat(enLigne(n, Object.assign({}, st, { bold: true }))); return; }
      if (tag === 'em' || tag === 'i') { out = out.concat(enLigne(n, Object.assign({}, st, { italics: true }))); return; }
      if (tag === 'mark') { out = out.concat(enLigne(n, st)); return; }
      if (tag === 'svg') return;
      out = out.concat(enLigne(n, st));
    });
    return out;
  }
  function rogne(frag) {
    while (frag.length && /^\s*$/.test(frag[0].text) && frag[0].text !== '\n') frag.shift();
    if (frag.length) frag[0].text = frag[0].text.replace(/^\s+/, '');
    while (frag.length && /^\s*$/.test(frag[frag.length - 1].text)) frag.pop();
    if (frag.length) frag[frag.length - 1].text = frag[frag.length - 1].text.replace(/\s+$/, '');
    return frag;
  }
  function aDesBlocs(n) {
    for (var i = 0; i < n.children.length; i++) if (/^(p|ul|ol|table|div|h[1-6]|figure|aside|section|details)$/i.test(n.children[i].tagName)) return true;
    return false;
  }

  function blocs(node, o) {
    var out = [];
    var tampon = [];
    function vider() { rogne(tampon); if (tampon.length) out.push({ text: tampon, margin: [0, 0, 0, 5] }); tampon = []; }
    node.childNodes.forEach(function (n) {
      if (n.nodeType === 3) { if (n.nodeValue.trim()) tampon = tampon.concat(morceaux(nettoie(n.nodeValue), {})); return; }
      if (n.nodeType !== 1) return;
      var tag = n.tagName.toLowerCase(), cls = n.getAttribute('class') || '';
      if (/^(strong|b|em|i|a|span|br|mark)$/.test(tag)) { tampon = tampon.concat(enLigne({ childNodes: [n] })); return; }
      vider();
      if (tag === 'p') {
        if (/appli-tete/.test(cls)) { out.push({ text: n.textContent.trim().toUpperCase(), style: 'appliTete' }); return; }
        var f = rogne(enLigne(n)); if (f.length) out.push({ text: f, margin: [0, 0, 0, 5] }); return;
      }
      if (/^h[1-6]$/.test(tag)) { out.push({ text: rogne(enLigne(n)), style: tag, headlineLevel: 1 }); return; }
      if (tag === 'ul' || tag === 'ol') {
        var items = [];
        Array.prototype.forEach.call(n.children, function (li) {
          if (aDesBlocs(li)) items.push({ stack: blocs(li, o) }); else items.push({ text: rogne(enLigne(li)), margin: [0, 0, 0, 2] });
        });
        var l = {}; l[tag] = items; l.margin = [0, 0, 0, 6]; out.push(l); return;
      }
      if (tag === 'table') { out.push(tableau(n)); return; }
      if (tag === 'figure') {
        var svg = n.querySelector('svg'); if (svg) out.push(svgPdf(svg));
        var cap = n.querySelector('figcaption'); if (cap) out.push({ text: cap.textContent.trim(), style: 'legende' });
        return;
      }
      if (tag === 'svg') { out.push(svgPdf(n)); return; }
      if (tag === 'details') {
        if (/corrige/.test(cls)) {
          if (!o.corriges) return;
          var corps = n.querySelector('.corrige-body') || n;
          out.push({ table: { widths: ['*'], body: [[{ stack: [{ text: 'Corrigé', style: 'corrigeTete' }].concat(blocs(corps, o)), margin: [6, 4, 6, 2] }]] }, layout: cadre(null, C.ok, true), margin: [0, 0, 0, 8] });
          return;
        }
        var sum = n.querySelector('summary');
        if (sum) out.push({ text: rogne(enLigne(sum)), style: 'h3' });
        var tmp = n.cloneNode(true); var s2 = tmp.querySelector('summary'); if (s2) s2.remove();
        out = out.concat(blocs(tmp, o)); return;
      }
      if (tag === 'summary') return;
      if (tag === 'aside' && /appli/.test(cls)) {
        out.push({ table: { widths: ['*'], body: [[{ stack: blocs(n, o), margin: [8, 6, 8, 2] }]] }, layout: cadre(o.soft, o.accent), margin: [0, 2, 0, 10] });
        return;
      }
      if (tag === 'section' && /exo/.test(cls)) { out.push({ stack: blocs(n, o), margin: [0, 0, 0, 6] }); return; }
      out = out.concat(blocs(n, o));
    });
    vider();
    return out;
  }
  function cadre(fond, trait, gauche) {
    return {
      hLineWidth: function () { return gauche ? 0 : 0.8; }, vLineWidth: function (i) { return gauche ? (i === 0 ? 2.5 : 0) : 0.8; },
      hLineColor: function () { return trait; }, vLineColor: function () { return trait; },
      fillColor: function () { return fond || null; }, paddingLeft: function () { return 0; }, paddingRight: function () { return 0; },
      paddingTop: function () { return 0; }, paddingBottom: function () { return 0; }
    };
  }
  function tableau(t) {
    var rows = [], max = 0, entete = 0;
    t.querySelectorAll('tr').forEach(function (tr) {
      var row = [];
      tr.querySelectorAll('th,td').forEach(function (c) {
        var th = c.tagName.toLowerCase() === 'th';
        row.push({ text: rogne(enLigne(c)), bold: th, fillColor: th ? '#e8ebe4' : null, fontSize: 9.5 });
      });
      if (tr.parentNode.tagName.toLowerCase() === 'thead') entete++;
      max = Math.max(max, row.length); rows.push(row);
    });
    rows.forEach(function (r) { while (r.length < max) r.push(''); });
    if (!rows.length) return { text: '' };
    return { table: { headerRows: entete, widths: Array(max).fill('*'), body: rows, dontBreakRows: true },
      layout: { hLineColor: function () { return C.line; }, vLineColor: function () { return C.line; }, hLineWidth: function () { return 0.6; }, vLineWidth: function () { return 0.6; },
        paddingLeft: function () { return 4; }, paddingRight: function () { return 4; }, paddingTop: function () { return 3; }, paddingBottom: function () { return 3; } },
      margin: [0, 2, 0, 8] };
  }

  // ---------- filigrane discret, répété en diagonale sur toute la page ----------
  function filigrane(w, h) {
    var lignes = '';
    for (var y = -h; y < h * 1.6; y += 120) {
      for (var x = -w; x < w * 1.6; x += 330) lignes += '<text x="' + x + '" y="' + y + '">' + AUTEUR + '</text>';
    }
    return '<svg xmlns="http://www.w3.org/2000/svg" width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + ' ' + h + '">' +
      '<g transform="rotate(-32 ' + (w / 2) + ' ' + (h / 2) + ')" font-family="Roboto" font-size="20" font-weight="bold" fill="' + C.brand + '" fill-opacity="0.055">' + lignes + '</g></svg>';
  }

  function documentPdf(spec, o) {
    var accent = spec.disc === 'h' ? C.hist : spec.disc === 'g' ? C.geo : C.brand;
    o.accent = accent; o.soft = spec.disc === 'g' ? C.geoSoft : C.histSoft;
    var parseur = new DOMParser();
    var contenu = [
      { text: spec.surtitre || '', style: 'surtitre' },
      { text: spec.titre, style: 'titre' }
    ];
    if (spec.meta) contenu.push({ text: spec.meta, style: 'meta' });
    contenu.push({ canvas: [{ type: 'line', x1: 0, y1: 0, x2: 515, y2: 0, lineWidth: 1.2, lineColor: accent }], margin: [0, 2, 0, 10] });
    spec.sections.forEach(function (s) {
      if (s.titre) contenu.push({ text: s.titre, style: 'section', color: accent, headlineLevel: 1 });
      var doc = parseur.parseFromString('<div id="r">' + s.html + '</div>', 'text/html');
      contenu = contenu.concat(blocs(doc.getElementById('r'), o));
    });
    return {
      pageSize: 'A4', pageMargins: [40, 46, 40, 50],
      info: { title: spec.titre, author: AUTEUR, subject: 'Histoire-Géographie, premier cycle', creator: 'Histoire géographie premier cycle' },
      background: function (page, size) { return { svg: filigrane(size.width, size.height), absolutePosition: { x: 0, y: 0 } }; },
      header: function (p) { if (p === 1) return null; return { text: 'Histoire-Géographie · ' + (spec.surtitre || ''), style: 'entete', margin: [40, 20, 40, 0] }; },
      footer: function (p, n) {
        return { columns: [{ text: 'Document de ' + AUTEUR, style: 'pied' }, { text: p + ' / ' + n, style: 'pied', alignment: 'right' }], margin: [40, 16, 40, 0] };
      },
      pageBreakBefore: function (node, suivants) { return node.headlineLevel === 1 && suivants.length === 0; },
      content: contenu,
      defaultStyle: { font: 'Roboto', fontSize: 10.5, lineHeight: 1.22, color: C.ink },
      styles: {
        surtitre: { fontSize: 9, color: C.muted, bold: true, characterSpacing: 0.6 },
        titre: { fontSize: 17, bold: true, color: C.brand, margin: [0, 2, 0, 4], lineHeight: 1.1 },
        meta: { fontSize: 9.5, color: C.muted, margin: [0, 0, 0, 2] },
        section: { fontSize: 13.5, bold: true, margin: [0, 10, 0, 6] },
        h1: { fontSize: 15, bold: true, color: C.brand, margin: [0, 10, 0, 5] },
        h2: { fontSize: 13, bold: true, color: C.brand, margin: [0, 10, 0, 5] },
        h3: { fontSize: 12, bold: true, color: C.brand, margin: [0, 8, 0, 4] },
        h4: { fontSize: 11.5, bold: true, color: accent, margin: [0, 9, 0, 4] },
        h5: { fontSize: 10.8, bold: true, margin: [0, 6, 0, 3] },
        h6: { fontSize: 10.5, bold: true, italics: true, margin: [0, 4, 0, 2] },
        appliTete: { fontSize: 8.5, bold: true, color: accent, characterSpacing: 0.8, margin: [0, 0, 0, 4] },
        corrigeTete: { fontSize: 9, bold: true, color: C.ok, margin: [0, 0, 0, 3] },
        legende: { fontSize: 8.5, italics: true, color: C.muted, alignment: 'center', margin: [0, 0, 0, 10] },
        entete: { fontSize: 8, color: C.muted },
        pied: { fontSize: 8, color: C.muted }
      }
    };
  }

  function nomFichier(spec) {
    var base = ('HG ' + (spec.fichier || spec.titre)).normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^A-Za-z0-9]+/g, '-').replace(/^-|-$/g, '');
    return base.slice(0, 80) + '.pdf';
  }

  // ---------- actions ----------
  var POLICES = {
    Roboto: { normal: 'Roboto-Regular.ttf', bold: 'Roboto-Medium.ttf', italics: 'Roboto-Italic.ttf', bolditalics: 'Roboto-MediumItalic.ttf' },
    Fleches: { normal: 'Fleches.ttf', bold: 'Fleches.ttf', italics: 'Fleches.ttf', bolditalics: 'Fleches.ttf' }
  };
  function fabriquer(spec, o) { return charger().then(function () { return window.pdfMake.createPdf(documentPdf(spec, o), null, POLICES); }); }
  function base64(pdf) { return new Promise(function (ok) { pdf.getBase64(ok); }); }
  function blob(pdf) { return new Promise(function (ok) { pdf.getBlob(ok); }); }
  var android = window.HGAndroid;

  function agir(action, spec, o, msg) {
    var nom = nomFichier(spec);
    msg('Préparation du PDF…');
    return fabriquer(spec, o).then(function (pdf) {
      if (android) {
        return base64(pdf).then(function (b) {
          var r;
          if (action === 'telecharger') {
            r = android.telecharger(nom, b);
            if (r === 'partager') { r = android.partager(nom, b); return msg(r === 'ok' ? 'Choisis « Enregistrer » ou une application pour garder le PDF.' : 'Erreur : ' + r); }
            return msg(r === 'ok' ? 'PDF enregistré dans Téléchargements › Histoire-geographie (' + nom + ').' : 'Erreur : ' + r);
          }
          r = action === 'partager' ? android.partager(nom, b) : android.imprimer(nom, b);
          msg(r === 'ok' ? (action === 'partager' ? 'Choisis l\'application de partage.' : 'Choisis l\'imprimante ou « Enregistrer au format PDF ».') : 'Erreur : ' + r);
        });
      }
      if (action === 'partager') {
        return blob(pdf).then(function (bl) {
          var f = null; try { f = new File([bl], nom, { type: 'application/pdf' }); } catch (e) { /* ancien navigateur */ }
          if (f && navigator.canShare && navigator.canShare({ files: [f] })) {
            return navigator.share({ files: [f], title: spec.titre }).then(function () { msg('PDF partagé.'); }, function () { msg(''); });
          }
          pdf.download(nom); msg('Le partage direct n\'est pas disponible ici : le PDF a été téléchargé, tu peux l\'envoyer depuis tes fichiers.');
        });
      }
      if (action === 'imprimer') { pdf.print(); return msg('Le PDF s\'ouvre pour l\'impression.'); }
      pdf.download(nom); msg('PDF téléchargé : ' + nom);
    }).catch(function (e) {
      msg(/chargement/.test(String(e)) ? 'Impossible de charger le module PDF. Connecte-toi une première fois à Internet puis réessaie.' : 'Erreur pendant la création du PDF : ' + e);
    });
  }

  // ---------- panneau ----------
  function ouvrir(spec) {
    window.HGPDF._dernier = spec;
    var ancien = document.getElementById('panneau-pdf'); if (ancien) ancien.remove();
    var avecCorr = /class="corrige"/.test(spec.sections.map(function (s) { return s.html; }).join(''));
    var p = document.createElement('div');
    p.id = 'panneau-pdf'; p.className = 'panneau-pdf'; p.setAttribute('role', 'dialog'); p.setAttribute('aria-label', 'Exporter en PDF');
    p.innerHTML = '<div class="pp-fond" data-fermer></div><div class="pp-boite">' +
      '<div class="pp-tete"><b>Exporter en PDF</b><button type="button" class="pp-x" data-fermer aria-label="Fermer">×</button></div>' +
      '<p class="pp-titre">' + spec.titre.replace(/[<&]/g, '') + '</p>' +
      (avecCorr ? '<label class="pp-case"><input type="checkbox" id="pp-corr" checked> Inclure les corrigés</label>' : '') +
      '<div class="pp-actions"><button type="button" class="btn btn-plein" data-act="telecharger">Télécharger</button>' +
      '<button type="button" class="btn" data-act="partager">Partager</button><button type="button" class="btn" data-act="imprimer">Imprimer</button></div>' +
      '<p class="pp-note">A4, nom « ' + AUTEUR + ' » en filigrane.</p><p class="pp-msg" role="status" id="pp-msg"></p></div>';
    document.body.appendChild(p);
    var occupe = false;
    function msg(t) { document.getElementById('pp-msg').textContent = t || ''; }
    p.addEventListener('click', function (ev) {
      if (ev.target.hasAttribute('data-fermer')) { p.remove(); return; }
      var b = ev.target.closest('[data-act]'); if (!b || occupe) return;
      occupe = true; p.classList.add('occupe');
      var c = document.getElementById('pp-corr');
      setTimeout(function () {
        agir(b.getAttribute('data-act'), spec, { corriges: c ? c.checked : true }, msg).then(function () { occupe = false; p.classList.remove('occupe'); });
      }, 30);
    });
  }

  window.addEventListener('hashchange', function () { var p = document.getElementById('panneau-pdf'); if (p) p.remove(); });
  window.HGPDF = { ouvrir: ouvrir, _fabriquer: fabriquer, _document: documentPdf, _charger: charger, _nom: nomFichier };
})();
