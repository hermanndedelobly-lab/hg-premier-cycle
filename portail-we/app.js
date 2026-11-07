/* MW+ · Portail culturel wê — navigation et rendu des pages (sans dépendance). */
(function () {
  "use strict";
  var S = window.SITE;
  var main = document.getElementById("main");
  var nav = document.getElementById("nav");
  var menuBtn = document.querySelector(".menu-btn");
  var MOIS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."];

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function norm(s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function section(id) { return S.sections.find(function (s) { return s.id === id; }); }
  function href(sec, page) { return "#/" + sec + (page ? "/" + page : ""); }
  var rubriques = S.sections.filter(function (s) { return s.pages.length; });

  /* ---------- Menu ---------- */
  function buildNav() {
    var html = "<ul>";
    S.sections.forEach(function (s) {
      if (!s.pages.length) {
        html += '<li><a class="nav__top" data-sec="' + s.id + '" href="#/">' + esc(s.label) + "</a></li>";
        return;
      }
      html += '<li><button class="nav__top" type="button" data-sec="' + s.id + '" aria-expanded="false">' +
        esc(s.court || s.label) + '<span class="nav__caret" aria-hidden="true"></span></button><ul class="nav__sub">' +
        '<li><a href="' + href(s.id) + '"><strong>' + esc(s.label) + "</strong></a></li>" +
        s.pages.map(function (p) {
          return '<li><a data-page="' + s.id + "/" + p.id + '" href="' + href(s.id, p.id) + '">' + esc(p.titre) + "</a></li>";
        }).join("") + "</ul></li>";
    });
    nav.innerHTML = html + "</ul>";

    nav.addEventListener("click", function (e) {
      var btn = e.target.closest("button.nav__top");
      if (btn) {
        var li = btn.parentNode, open = !li.classList.contains("open");
        nav.querySelectorAll("li.open").forEach(function (o) { o.classList.remove("open"); o.firstChild.setAttribute("aria-expanded", "false"); });
        if (open) { li.classList.add("open"); btn.setAttribute("aria-expanded", "true"); }
        return;
      }
      if (e.target.closest("a")) closeMenu();
    });
    document.addEventListener("click", function (e) {
      if (!nav.contains(e.target) && !menuBtn.contains(e.target))
        nav.querySelectorAll("li.open").forEach(function (o) { o.classList.remove("open"); });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { nav.querySelectorAll("li.open").forEach(function (o) { o.classList.remove("open"); }); closeMenu(); }
    });
    menuBtn.addEventListener("click", function () {
      var open = !nav.classList.contains("is-open");
      nav.classList.toggle("is-open", open);
      document.body.classList.toggle("nav-open", open);
      menuBtn.setAttribute("aria-expanded", String(open));
    });
  }
  function closeMenu() {
    nav.classList.remove("is-open");
    document.body.classList.remove("nav-open");
    menuBtn.setAttribute("aria-expanded", "false");
    nav.querySelectorAll("li.open").forEach(function (o) { o.classList.remove("open"); });
  }

  function buildFooter() {
    document.getElementById("year").textContent = new Date().getFullYear();
    document.getElementById("footer-links").innerHTML = S.sections.map(function (s) {
      return '<a href="' + href(s.pages.length ? s.id : "") + '">' + esc(s.label) + "</a>";
    }).join("");
  }

  /* ---------- Briques ---------- */
  function sectionCard(s, i) {
    return '<a class="card" href="' + href(s.id) + '"><span class="card__num">' + (i + 2) + "</span><h3>" + esc(s.label) +
      "</h3><p>" + esc(s.intro) + '</p><div class="chips">' +
      s.pages.slice(0, 4).map(function (p) { return '<span class="chip">' + esc(p.titre) + "</span>"; }).join("") +
      (s.pages.length > 4 ? '<span class="chip">+' + (s.pages.length - 4) + "</span>" : "") +
      '</div><span class="card__more">Explorer →</span></a>';
  }
  function newsItem(n) {
    var d = new Date(n.date + "T12:00:00");
    return '<article class="news__item"><div class="news__date"><b>' + d.getDate() + "</b><span>" + MOIS[d.getMonth()] + " " + d.getFullYear() +
      '</span></div><div><span class="tag">' + esc(n.categorie) + (n.lieu ? " · " + esc(n.lieu) : "") + "</span><h3>" + esc(n.titre) +
      "</h3><p>" + esc(n.resume) + "</p></div></article>";
  }
  function newsSorted() { return S.actualites.slice().sort(function (a, b) { return b.date.localeCompare(a.date); }); }
  function pageHead(eyebrow, title, intro, crumbs) {
    return '<header class="pagehead"><div class="wrap">' + (crumbs ? '<nav class="crumbs" aria-label="Fil d’Ariane">' + crumbs + "</nav>" : "") +
      '<p class="eyebrow">' + esc(eyebrow) + "</p><h1>" + esc(title) + "</h1>" + (intro ? "<p>" + esc(intro) + "</p>" : "") + "</div></header>";
  }
  var aCompleter = '<div class="notice"><p><strong>Rubrique en construction</strong>Cette page attend vos contributions : textes, photos, enregistrements, corrections. ' +
    '<a href="#/contact/proposer">Proposer un contenu</a></p></div>';

  /* ---------- Pages ---------- */
  function renderHome() {
    document.title = "MW+ · Portail culturel wê";
    var news = newsSorted().slice(0, 3);
    main.innerHTML =
      '<section class="hero"><div class="hero__inner"><div><p class="eyebrow" style="color:var(--gold-2)">Portail culturel du peuple wê</p>' +
      "<h1>La Culture Wê,<br><em>notre fierté</em></h1>" +
      '<p class="lead">Histoire, langue, traditions, musique, villages et forces vives du pays wê, dans l’ouest de la Côte d’Ivoire — réunis en un seul lieu pour les transmettre aux générations futures.</p>' +
      '<div class="hero__actions"><a class="btn btn--gold" href="#/histoire">Découvrir notre histoire</a><a class="btn btn--ghost" href="#/langue/apprendre">Apprendre le wê</a></div></div>' +
      '<img class="hero__logo" src="assets/logo.webp" alt="Logo MW+ : statue wê sculptée devant une montagne boisée, avec la devise La Culture Wê, notre fierté" width="720" height="720"></div></section>' +

      '<section class="section"><div class="wrap"><div class="section__head"><div><p class="eyebrow">Explorer le portail</p><h2>Toutes les rubriques du portail</h2></div></div>' +
      '<div class="grid">' + rubriques.map(sectionCard).join("") + "</div></div></section>" +

      '<section class="section" style="padding-top:0"><div class="wrap split"><div><div class="section__head"><div><p class="eyebrow">Actualités</p><h2>À la une</h2></div>' +
      '<a class="btn btn--line" href="#/actualites">Toutes les actualités</a></div><div class="news">' +
      (news.length ? news.map(newsItem).join("") : '<div class="empty">Aucune actualité pour le moment.</div>') + "</div></div>" +
      '<div><div class="section__head"><div><p class="eyebrow">Accès rapides</p><h2>Commencer ici</h2></div></div><div class="grid" style="grid-template-columns:1fr 1fr">' +
      [["langue", "dictionnaire", "Dictionnaire français-wê"], ["langue", "proverbes", "Proverbes et expressions"], ["tourisme", "villages", "Nos villages"],
        ["culture", "danses", "Danses traditionnelles"], ["musique", "artistes", "Artistes wê"], ["business", "annuaire", "Annuaire des entreprises"]]
        .map(function (q) { return '<a class="card" href="' + href(q[0], q[1]) + '"><h3 style="font-size:1.02rem">' + esc(q[2]) + '</h3><span class="card__more">Ouvrir →</span></a>'; }).join("") +
      "</div></div></div></section>" +

      '<section class="section" style="padding-top:0"><div class="wrap"><div class="cta"><div><h2>Gardiens de la mémoire, à vous la parole</h2>' +
      "<p>Un conte, un proverbe, une photo d’archive, un mot wê, l’histoire de votre village : chaque contribution enrichit le patrimoine commun.</p></div>" +
      '<a class="btn btn--gold" href="#/contact/proposer">Proposer un contenu</a></div></div></section>';
  }

  function renderSection(s) {
    document.title = s.label + " · MW+";
    main.innerHTML = pageHead("Rubrique", s.label, s.intro, '<a href="#/">Accueil</a> › ' + esc(s.label)) +
      '<section class="section"><div class="wrap"><div class="grid">' +
      s.pages.map(function (p, i) {
        return '<a class="card" href="' + href(s.id, p.id) + '"><span class="card__num">' + (i + 1) + "</span><h3>" + esc(p.titre) + "</h3><p>" +
          esc(p.chapo) + '</p><span class="card__more">Lire →</span></a>';
      }).join("") + "</div></div></section>";
  }

  function renderPage(s, p) {
    document.title = p.titre + " · MW+";
    var body = "";
    switch (p.type) {
      case "dictionnaire": body = dictionnaire(p); break;
      case "actualites": body = actualites(p); break;
      case "annuaire": body = annuaire(p); break;
      case "formulaire": body = formulaire(p); break;
      default:
        body = (p.texte || []).map(function (t) { return "<p>" + esc(t) + "</p>"; }).join("") + (p.aCompleter ? aCompleter : "");
    }
    main.innerHTML = pageHead(s.label, p.titre, p.chapo,
      '<a href="#/">Accueil</a> › <a href="' + href(s.id) + '">' + esc(s.label) + "</a> › " + esc(p.titre)) +
      '<div class="layout"><aside class="sidenav" aria-label="' + esc(s.label) + '"><h2>' + esc(s.court || s.label) + "</h2><ul>" +
      s.pages.map(function (q) {
        return '<li><a href="' + href(s.id, q.id) + '"' + (q.id === p.id ? ' aria-current="page"' : "") + ">" + esc(q.titre) + "</a></li>";
      }).join("") + '</ul></aside><article class="article">' + body + "</article></div>";
    var cur = main.querySelector('.sidenav a[aria-current="page"]');
    if (cur && cur.scrollIntoView && window.innerWidth <= 860) cur.scrollIntoView({ block: "nearest", inline: "center" });
    if (p.type && hooks[p.type]) hooks[p.type](p);
  }

  /* Dictionnaire */
  function dictionnaire(p) {
    return (p.texte || []).map(function (t) { return "<p>" + esc(t) + "</p>"; }).join("") +
      '<div class="search" role="search"><input class="input" id="q" type="search" placeholder="Rechercher un mot (français ou wê)…" aria-label="Rechercher un mot">' +
      '<select class="select" id="cat" aria-label="Catégorie"><option value="">Toutes les catégories</option>' +
      uniq(S.dictionnaire.map(function (e) { return e.categorie; })).map(function (c) { return "<option>" + esc(c) + "</option>"; }).join("") +
      '</select></div><div id="results"></div>';
  }
  function uniq(a) { return a.filter(function (x, i) { return x && a.indexOf(x) === i; }).sort(); }

  /* Actualités */
  function actualites(p) {
    var list = newsSorted().filter(function (n) { return !p.filtre || n.categorie === p.filtre; });
    return list.length ? '<div class="news">' + list.map(newsItem).join("") + "</div>"
      : '<div class="empty"><strong>Rien à afficher pour le moment</strong>Une information à partager ? <a href="#/contact/proposer">Envoyez-la-nous</a>.</div>';
  }

  /* Annuaire */
  function annuaire(p) {
    return '<div class="search" role="search"><input class="input" id="q" type="search" placeholder="Nom, activité, ville…" aria-label="Rechercher dans l’annuaire">' +
      '<select class="select" id="ville" aria-label="Ville"><option value="">Toutes les villes</option>' +
      uniq(S.annuaire.map(function (e) { return e.ville; })).map(function (c) { return "<option>" + esc(c) + "</option>"; }).join("") +
      '</select></div><div id="results"></div>';
  }

  var hooks = {
    dictionnaire: function () {
      var q = document.getElementById("q"), cat = document.getElementById("cat"), out = document.getElementById("results");
      function run() {
        var t = norm(q.value), c = cat.value;
        var r = S.dictionnaire.filter(function (e) {
          return (!c || e.categorie === c) && (!t || norm(e.fr).indexOf(t) > -1 || norm(e.we).indexOf(t) > -1);
        }).sort(function (a, b) { return a.fr.localeCompare(b.fr, "fr"); });
        if (!S.dictionnaire.length) {
          out.innerHTML = '<div class="empty"><strong>Le dictionnaire est en cours de constitution</strong>Locuteurs du wê, proposez vos premiers mots : ' +
            'le mot en français, sa traduction, la variante (guéré, wobé, canton) et un exemple.<br><br><a class="btn btn--gold" href="#/contact/proposer">Proposer un mot</a></div>';
          return;
        }
        out.innerHTML = r.length ? '<p class="muted">' + r.length + " mot" + (r.length > 1 ? "s" : "") + '</p><div class="table-scroll"><table class="dict"><thead><tr><th>Français</th><th>Wê</th><th>Catégorie</th><th>Exemple</th></tr></thead><tbody>' +
          r.map(function (e) {
            return "<tr><td>" + esc(e.fr) + '</td><td class="we">' + esc(e.we) + (e.variante ? ' <span class="chip">' + esc(e.variante) + "</span>" : "") +
              "</td><td>" + esc(e.categorie) + "</td><td>" + esc(e.exemple) + "</td></tr>";
          }).join("") + "</tbody></table></div>"
          : '<div class="empty">Aucun résultat. <a href="#/contact/proposer">Proposer ce mot</a></div>';
      }
      q.addEventListener("input", run); cat.addEventListener("change", run); run();
    },
    annuaire: function (p) {
      var q = document.getElementById("q"), ville = document.getElementById("ville"), out = document.getElementById("results");
      function run() {
        var t = norm(q.value), v = ville.value;
        var r = S.annuaire.filter(function (e) {
          return (!p.filtre || e.categorie === p.filtre) && (!v || e.ville === v) &&
            (!t || norm([e.nom, e.activite, e.ville, e.description].join(" ")).indexOf(t) > -1);
        });
        out.innerHTML = r.length ? '<div class="grid">' + r.map(function (e) {
          return '<div class="card"><span class="tag">' + esc(e.categorie) + "</span><h3>" + esc(e.nom) + "</h3><p>" + esc(e.activite) + " · " + esc(e.ville) +
            "</p>" + (e.description ? "<p>" + esc(e.description) + "</p>" : "") +
            (e.telephone ? '<a class="card__more" href="tel:' + esc(e.telephone.replace(/\s/g, "")) + '">' + esc(e.telephone) + "</a>" : "") + "</div>";
        }).join("") + "</div>"
          : '<div class="empty"><strong>' + (S.annuaire.length ? "Aucun résultat" : "L’annuaire ouvre ses inscriptions") + "</strong>" +
            "Entreprises, commerçants, artisans et entrepreneurs wê : inscrivez gratuitement votre activité.<br><br>" +
            '<a class="btn btn--gold" href="#/contact/partenaire">Inscrire mon activité</a></div>';
      }
      q.addEventListener("input", run); ville.addEventListener("change", run); run();
    },
    formulaire: function (p) {
      var f = document.getElementById("form");
      f.addEventListener("submit", function (e) {
        e.preventDefault();
        if (!f.reportValidity()) return;
        var d = new FormData(f), lignes = [];
        d.forEach(function (v, k) { if (k !== "sujet" && v) lignes.push(k.charAt(0).toUpperCase() + k.slice(1) + " : " + v); });
        var sujet = "[MW+] " + (d.get("sujet") || p.titre);
        location.href = "mailto:" + S.emailContact + "?subject=" + encodeURIComponent(sujet) + "&body=" + encodeURIComponent(lignes.join("\n\n"));
        document.getElementById("form-ok").hidden = false;
      });
    }
  };

  /* Formulaires (envoi par la messagerie de l'utilisateur) */
  function formulaire(p) {
    var champs = {
      contact:
        '<div class="row"><label>Nom<input class="input" name="nom" required autocomplete="name"></label>' +
        '<label>E-mail<input class="input" name="email" type="email" required autocomplete="email"></label></div>' +
        '<label>Sujet<input class="input" name="sujet" required></label>' +
        '<label>Message<textarea class="input" name="message" rows="6" required></textarea></label>',
      partenaire:
        '<div class="row"><label>Structure<input class="input" name="structure" required></label>' +
        '<label>Personne à contacter<input class="input" name="contact" required autocomplete="name"></label></div>' +
        '<div class="row"><label>E-mail<input class="input" name="email" type="email" required autocomplete="email"></label>' +
        '<label>Téléphone<input class="input" name="telephone" type="tel" autocomplete="tel"></label></div>' +
        '<div class="row"><label>Type de partenariat<select class="select input" name="partenariat"><option>Inscription à l’annuaire</option><option>Publicité</option><option>Sponsoring d’événement</option><option>Partenariat institutionnel</option><option>Autre</option></select></label>' +
        '<label>Ville<input class="input" name="ville"></label></div>' +
        '<label>Présentation et projet<textarea class="input" name="projet" rows="5" required></textarea></label>',
      contenu:
        '<div class="row"><label>Nom<input class="input" name="nom" required autocomplete="name"></label>' +
        '<label>E-mail ou téléphone<input class="input" name="contact" required></label></div>' +
        '<div class="row"><label>Type de contenu<select class="select input" name="sujet"><option>Mot pour le dictionnaire</option><option>Proverbe ou expression</option><option>Conte ou légende</option><option>Histoire d’un village</option><option>Personnalité</option><option>Photo, vidéo ou audio</option><option>Archive</option><option>Actualité ou événement</option><option>Correction</option><option>Autre</option></select></label>' +
        '<label>Rubrique concernée<select class="select input" name="rubrique">' + rubriques.map(function (s) { return "<option>" + esc(s.label) + "</option>"; }).join("") + "</select></label></div>" +
        '<div class="row"><label>Village / canton<input class="input" name="village"></label><label>Source <span class="hint">(qui vous l’a transmis ?)</span><input class="input" name="source"></label></div>' +
        '<label>Votre contribution <span class="hint">Pour un mot : français, wê, variante, exemple. Pour un fichier, nous vous répondrons avec un lien d’envoi.</span><textarea class="input" name="contribution" rows="7" required></textarea></label>' +
        '<label style="display:flex;gap:8px;align-items:flex-start;font-weight:400"><input type="checkbox" name="accord" value="oui" required> J’accepte que ce contenu soit publié sur le portail, avec mention de son auteur.</label>'
    }[p.formulaire];
    return '<form class="form" id="form" novalidate>' + champs +
      '<div><button class="btn btn--gold" type="submit">Envoyer</button></div>' +
      '<p class="form__ok" id="form-ok" hidden>Votre messagerie s’est ouverte avec le message prêt à partir. Si rien ne s’est passé, écrivez-nous à <a href="mailto:' +
      esc(S.emailContact) + '">' + esc(S.emailContact) + "</a>.</p></form>";
  }

  function renderNotFound() {
    document.title = "Page introuvable · MW+";
    main.innerHTML = pageHead("Erreur", "Page introuvable", "Cette page n’existe pas ou a été déplacée.") +
      '<section class="section"><div class="wrap"><a class="btn btn--gold" href="#/">Retour à l’accueil</a></div></section>';
  }

  /* ---------- Routeur ---------- */
  function route() {
    var parts = location.hash.replace(/^#\/?/, "").split("/").filter(Boolean);
    var s = parts[0] ? section(parts[0]) : null;
    if (!parts.length || (s && s.id === "accueil")) renderHome();
    else if (!s) renderNotFound();
    else if (!parts[1]) renderSection(s);
    else {
      var p = s.pages.find(function (x) { return x.id === parts[1]; });
      p ? renderPage(s, p) : renderNotFound();
    }
    var cur = s && s.pages.length ? s.id : "accueil";
    nav.querySelectorAll(".nav__top").forEach(function (a) { a.setAttribute("aria-current", String(a.dataset.sec === cur)); });
    nav.querySelectorAll("[data-page]").forEach(function (a) {
      a.toggleAttribute("aria-current", a.dataset.page === parts.slice(0, 2).join("/"));
      if (a.hasAttribute("aria-current")) a.setAttribute("aria-current", "page");
    });
    closeMenu();
    window.scrollTo(0, 0);
    main.focus({ preventScroll: true });
  }

  buildNav();
  buildFooter();
  window.addEventListener("hashchange", route);
  route();
})();
