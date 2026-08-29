# Learn Dutch

updated: 2026-08-29

App nativa para aprender holandés desde 0. Una ficha, un uso: holandés. No web, no catálogo, no “plataforma de libros”.

Stukje fue el prototipo del formato (trozos, progreso, diálogos/vocab/reglas como bloques). El contenido era *Dutch For Dummies*: no se publica. Learn Dutch es el producto.

## Contenido

Coger de internet una fuente ya estructurada — libro abierto u otro material con licencia clara — que sea un **currículum desde 0**, y convertirla en la app.

No un dump de frases. No un PDF partido por páginas. Una secuencia de lecciones.

Criterios para elegir fuente (aún no está elegida; es el primer paso):

- Empieza en cero (A0 → A1/A2).
- Licencia que permita app en Play y uso en la UE. Gutenberg USA no basta (aquí es vida del autor + 70).
- Ya viene en piezas útiles: diálogos, vocabulario, reglas. Si solo hay prosa, no sirve.
- Se puede defender en un listing: “curso de holandés”, no “este PDF en un WebView”.

## Forma

Lo que Stukje ya demostró y se queda: leer de uno en uno, marcar, volver mañana. UI pequeña, con carácter.

Lo que se añade, y poco más:

- Audio de frases y diálogos **metido en la app**, generado en el build (TTS de calidad, una vez). El teléfono no llama a ninguna API al pulsar play.
- Se lee gratis. Oír se paga una vez (IAP, Play Billing). No suscripción.

Nada de cuentas, rachas, SRS, notas, buscador, chat, “escribe y óyela”. Si no cabe en ese párrafo, no va en esta versión.

## No es

- Stukje con otro nombre y el Dummies dentro.
- Una app por cada libro o idioma clonado con el mismo shell.
- Duolingo. El valor es el currículum bien cortado + oír holandés de verdad, offline.

Si más adelante hay recetas u otro idioma, es otro producto, otro nombre, otra UX.

## Dónde vive

`/root/LearnDutch` — este archivo es la brújula. Stukje (`/root/stukje`, repo `DKeAlvaro/stukje`) se queda como prototipo del formato, no como producto.
