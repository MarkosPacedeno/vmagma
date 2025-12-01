const CACHE_NAME = "vmagma-cache-v1";
const urlsToCache = [
  "/",                // página principal
  "/acerca.html",     // tu historia
  "/static/css/styles.css", // tus estilos
  "/static/js/app.js",      // tu lógica JS
  "/static/icons/icon-192.png",
  "/static/icons/icon-512.png"
];

// ✅ Se instala y guarda en caché los archivos iniciales
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

// ✅ Activa y limpia cachés viejas si cambias versión
self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      );
    })
  );
});

// ✅ Intercepta peticiones y responde desde caché o red
self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      // Si está en caché, lo devuelve; si no, lo pide a la red
      return response || fetch(event.request);
    })
  );
});
