/* Service worker — Histoire géographie premier cycle
   Chaque nouvelle version publiée change VERSION : le navigateur télécharge alors
   le nouveau contenu en arrière-plan, puis l'application propose « Mettre à jour ». */
var VERSION = '1.10.0';
var CACHE = 'hg1c-' + VERSION;
var PRECACHE = ["./","index.html","app.css","app.js","data/contenu.json","manifest.webmanifest","fonts/literata-latin-400-normal.woff2","fonts/literata-latin-400-italic.woff2","fonts/literata-latin-700-normal.woff2","fonts/archivo-latin-500-normal.woff2","fonts/archivo-latin-700-normal.woff2","fonts/archivo-latin-800-normal.woff2","icons/icon-180.png","icons/icon-192.png","icons/icon-512.png","icons/icon-maskable-512.png","lib/pdfmake.min.js","lib/vfs_fonts.js"];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) {
    return c.addAll(PRECACHE.map(function (u) { return new Request(u, { cache: 'reload' }); }));
  }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k.indexOf('hg1c-') === 0 && k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener('message', function (e) {
  if (e.data && e.data.type === 'SKIP_WAITING') self.skipWaiting();
});

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
  var url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  // version.json : toujours demandé au serveur (pour savoir s'il existe une mise à jour)
  if (url.pathname.endsWith('/version.json')) {
    e.respondWith(fetch(req, { cache: 'no-store' }).catch(function () { return caches.match('version.json'); }));
    return;
  }
  // pages : l'application en cache, même sans connexion
  if (req.mode === 'navigate') {
    e.respondWith(caches.match('index.html', { cacheName: CACHE }).then(function (r) { return r || fetch(req); }));
    return;
  }
  // le reste : cache d'abord, réseau en secours
  e.respondWith(caches.match(req, { cacheName: CACHE, ignoreSearch: true }).then(function (r) {
    return r || fetch(req).then(function (res) {
      if (res.ok) { var copie = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copie); }); }
      return res;
    });
  }));
});
