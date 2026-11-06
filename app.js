/* Histoire géographie premier cycle — application hors ligne */
(function () {
  'use strict';
  var MODE = window.HG_MODE || 'single';
  var VERSION = window.HG_VERSION || '?';
  var D = null;                 // contenu
  var INDEX = {};               // id -> {type, classe, disc, theme, lecon|annexe}
  var ORDRE = {};               // classe -> [ids des leçons dans l'ordre]
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
      ORDRE[c.id] = [];
      c.disciplines.forEach(function (d) {
        d.themes.forEach(function (t) {
          t.lecons.forEach(function (l) {
            INDEX[l.id] = { type: 'lecon', classe: c, disc: d, theme: t, lecon: l };
            ORDRE[c.id].push(l.id);
            RECH.push({ id: l.id, classe: c.id, disc: d.id, titre: l.titre, ctx: c.id + ' · ' + d.nom + ' · ' + nomTheme(t), t: norm(l.titre + ' ' + t.titre), x: l.texte, nx: norm(l.texte) });
          });
        });
      });
      c.annexes.forEach(function (a) {
        INDEX[a.id] = { type: 'annexe', classe: c, annexe: a };
        RECH.push({ id: a.id, classe: c.id, disc: '', titre: a.titre, ctx: c.id + ' · Annexe', t: norm(a.titre), x: a.texte, nx: norm(a.texte) });
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

  function vueClasse(c) {
    barreClasses(c.id);
    var n = nbLecons(c), f = nbFaites(c), nbT = 0;
    c.disciplines.forEach(function (d) { nbT += d.themes.filter(function (t) { return t.n; }).length; });
    var h = '<p class="eyebrow">Classe de ' + c.id + '</p><h1 class="titre-vue">' + esc(c.nom) + '</h1>' +
      '<p class="chapo">' + n + ' leçons réparties en ' + nbT + ' thèmes.</p>' +
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
      '<h1 class="lecon-titre">Programme et progression de ' + c.id + '</h1><div class="texte">' + c.programme + '</div></div>';
    afficher(h, 'Programme ' + c.id);
  }

  function vueAnnexe(e) {
    barreClasses(e.classe.id);
    ecrire('derniere', e.annexe.id);
    var h = '<div class="d-h"><nav class="fil"><a href="#c-' + e.classe.id + '">' + e.classe.id + '</a><span>›</span><span>Annexe</span></nav>' +
      '<h1 class="lecon-titre">' + esc(e.annexe.titre) + '</h1><div class="texte">' + e.annexe.html + '</div></div>';
    afficher(h, e.annexe.titre);
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
      '<div class="puces"><span class="puce">Leçon ' + l.n + '</span>' + (l.duree ? '<span class="puce">' + l.duree + ' h</span>' : '') + '<span class="puce">' + esc(d.nom) + '</span></div>' +
      '<div class="sommaire" role="navigation" aria-label="Parties de la leçon"><button type="button" data-aller="b-sit">Situation</button><button type="button" data-aller="b-cours">Cours</button><button type="button" data-aller="b-exo">Exercices</button></div>' +
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
    afficher(h, l.titre);
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
      return '<li class="d-' + (r.disc || 'h') + '"><a href="#l-' + r.id + '"><span class="r-meta">' + esc(r.ctx) + '</span><span class="r-titre">' + surligner(r.titre, mots) + '</span><span class="r-extrait">' + surligner(ext, mots) + '</span></a></li>';
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

  function afficher(h, titre) {
    vue.innerHTML = h;
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
