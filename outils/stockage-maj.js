/* GNOMBLESSON — stockage v2 des mises à jour sans APK (depuis 1.17.0).
   Le contenu complet téléchargé est compressé (gzip) puis « emballé » en texte (15 bits par caractère, caractères
   U+0800 à U+87FF, jamais de demi-caractère UTF-16) et rangé dans localStorage sous la clé hg1c.contenu-gz :
   environ 6 fois moins de place qu'avant. La clé hg1c.contenu-maj ne contient plus qu'un petit descripteur
   (ou, pour la passerelle 1.10.0, un squelette porteur du lanceur). Une empreinte (FNV-1a) contrôle l'intégrité.
   Les clés de progression (faites, quiz, derniere, reglages…) ne sont jamais lues ni modifiées ici.
   Ce fichier est inclus tel quel dans la page de mise à jour (outils/fichier-unique.py, mode maj) et dans le
   lanceur de la passerelle (outils/fabriquer-pont.py). */
window.HGStock = window.HGStock || (function () {
  'use strict';
  var CLE = 'hg1c.contenu-gz', CLE_TMP = 'hg1c.contenu-gz-nouveau', ENTETE = 'GZ15';
  function dispo() { return typeof CompressionStream === 'function' && typeof DecompressionStream === 'function' && typeof TextEncoder === 'function'; }
  function empreinte(s) { var h = 0x811c9dc5; for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; } return ('0000000' + h.toString(16)).slice(-8); }
  function flux(octets, transfo) { return new Response(new Blob([octets]).stream().pipeThrough(transfo)).arrayBuffer().then(function (b) { return new Uint8Array(b); }); }
  function emballer(o) {   // octets → texte, 15 bits par caractère
    var t = [], acc = 0, n = 0;
    for (var i = 0; i < o.length; i++) {
      acc = (acc << 8) | o[i]; n += 8;
      if (n >= 15) { n -= 15; t.push(String.fromCharCode(0x0800 + ((acc >>> n) & 0x7fff))); acc &= (1 << n) - 1; }
      if (t.length >= 8192) { t = [t.join('')]; }
    }
    if (n > 0) t.push(String.fromCharCode(0x0800 + ((acc << (15 - n)) & 0x7fff)));
    return t.join('');
  }
  function deballer(s, longueur) {
    var o = new Uint8Array(longueur), acc = 0, n = 0, j = 0;
    for (var i = 0; i < s.length && j < longueur; i++) {
      var v = s.charCodeAt(i) - 0x0800; if (v < 0 || v > 0x7fff) throw new Error('caractère invalide');
      acc = (acc << 15) | v; n += 15;
      while (n >= 8 && j < longueur) { n -= 8; o[j++] = (acc >>> n) & 0xff; acc &= (1 << n) - 1; }
    }
    if (j !== longueur) throw new Error('données tronquées');
    return o;
  }
  // texte JSON → valeur à ranger : « GZ15:version:longueur:empreinte:données »
  function compresser(version, texte) {
    return flux(new TextEncoder().encode(texte), new CompressionStream('gzip')).then(function (o) {
      return [ENTETE, version, o.length, empreinte(texte), emballer(o)].join(':');
    });
  }
  function lireEntete(val) {
    if (!val || val.slice(0, 5) !== ENTETE + ':') return null;
    var p = val.split(':', 4), deb = p.join(':').length + 1;
    return { version: p[1], longueur: +p[2], empreinte: p[3], donnees: val.slice(deb) };
  }
  // valeur rangée → texte JSON vérifié
  function decompresser(val, versionAttendue) {
    var e = lireEntete(val);
    if (!e) return Promise.reject(new Error('stockage compressé absent'));
    if (versionAttendue && e.version !== versionAttendue) return Promise.reject(new Error('version ' + e.version + ' au lieu de ' + versionAttendue));
    var o; try { o = deballer(e.donnees, e.longueur); } catch (x) { return Promise.reject(x); }
    return flux(o, new DecompressionStream('gzip')).then(function (b) {
      var t = new TextDecoder().decode(b);
      if (empreinte(t) !== e.empreinte) throw new Error('empreinte incorrecte');
      return t;
    });
  }
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); return true; } catch (e) { return false; } }
  function lsDel(k) { try { localStorage.removeItem(k); } catch (e) { /* rien */ } }
  // contenu enregistré (version) → objet ; rejeté si absent, d'une autre version ou abîmé
  function lire(version) { return decompresser(lsGet(CLE), version).then(JSON.parse); }
  function versionRangee() { var e = lireEntete(lsGet(CLE)); return e ? e.version : null; }
  // squelette pour la passerelle 1.10.0 : structure complète, textes longs vidés, champs déclencheurs conservés
  function squelette(d) {
    function vide(x, cle) {
      if (typeof x === 'string') return (x.length > 300 && cle !== 'pont' && x.indexOf('pont-declencheur') < 0) ? '' : x;
      if (Array.isArray(x)) return cle === 'quiz' ? [] : x.map(function (y) { return vide(y, ''); });
      if (x && typeof x === 'object') { var r = {}; Object.keys(x).forEach(function (k) { r[k] = vide(x[k], k); }); return r; }
      return x;
    }
    var s = vide(d, ''); s.stub = true; s.stockage = 'compresse'; return s;
  }
  function descripteur(d) { return { version: d.version, date: d.date, stockage: 'compresse', notes: (d.notes || []).slice(0, 1) }; }
  /* Enregistre une version complète (objet d, texte JSON t) : contenu compressé vérifié, puis page de code éventuelle,
     puis descripteur (dernier, c'est lui qui « valide » la mise à jour). stub : squelette passerelle à garder.
     En cas d'échec, l'état précédent est conservé (ou, au pire, l'application revient à la version de l'APK). */
  function enregistrer(d, t, page, stub) {
    if (!dispo()) return Promise.reject(new Error('compression indisponible'));
    var V = d.version;
    return compresser(V, t).then(function (val) {
      // ancien contenu non compressé (format 1, plusieurs Mo) : remplacé d'abord par un descripteur provisoire
      // (version « 0 » : l'APK démarre sur sa propre version tant que la nouvelle n'est pas complète)
      var ancienDesc = lsGet('hg1c.contenu-maj');
      if (ancienDesc && ancienDesc.length > 200000) lsSet('hg1c.contenu-maj', JSON.stringify({ version: '0', stockage: 'en-cours' }));
      if (!lsSet(CLE_TMP, val)) {   // place insuffisante : on libère l'ancien contenu compressé avant de réessayer
        lsDel(CLE_TMP); lsDel(CLE);
        if (!lsSet(CLE_TMP, val)) { lsDel(CLE_TMP); throw new Error('place insuffisante'); }
      }
      return decompresser(lsGet(CLE_TMP), V).then(function (t2) {
        if (t2 !== t) throw new Error('relecture différente');
        if (page !== null && page !== undefined && !lsSet('hg1c.code-maj', JSON.stringify({ version: V, page: page }))) throw new Error('place insuffisante (code)');
        lsDel(CLE);
        if (!lsSet(CLE, val)) throw new Error('place insuffisante (contenu)');
        lsDel(CLE_TMP);
        if (!lsSet('hg1c.contenu-maj', JSON.stringify(stub || descripteur(d)))) throw new Error('place insuffisante (descripteur)');
        return true;
      });
    }).catch(function (e) { lsDel(CLE_TMP); throw e; });
  }
  function oublier() { lsDel(CLE); lsDel(CLE_TMP); }
  return { dispo: dispo, compresser: compresser, decompresser: decompresser, lire: lire, versionRangee: versionRangee,
    enregistrer: enregistrer, squelette: squelette, descripteur: descripteur, empreinte: empreinte, oublier: oublier,
    emballer: emballer, deballer: deballer, CLE: CLE };
})();
