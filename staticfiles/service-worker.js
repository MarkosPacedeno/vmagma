const CACHE_NAME = "vmagma-cache-v1";
const urlsToCache = [
  "/",
  "/static/landing/css/styles.css",
  "/static/landing/images/fondo1.gif",
  "/static/landing/icons/icon-192.png",
  "/static/landing/icons/icon-512.png"
];

// Instalar y cachear recursos
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Activar y limpiar cachés viejos
self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== CACHE_NAME) {
            return caches.delete(cache);
          }
        })
      );
    })
  );
});

// Interceptar peticiones y servir desde cache
self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});
