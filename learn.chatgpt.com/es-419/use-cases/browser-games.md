<!-- source: https://learn.chatgpt.com/es-419/use-cases/browser-games -->

## Introducción

Crear un juego es uno de los ejemplos más claros de cómo Codex ayuda en mucho más que generar código. Un juego real suele necesitar un concepto escrito, una capa de renderizado, trabajo en la estructura del frontend, estado del backend, producción de recursos y ajustes visuales constantes

Este caso de uso funciona mejor cuando Codex comienza por documentar exactamente lo que debe hacer el juego y luego hace iteraciones con Playwright interactive para probarlo en un navegador en ejecución.

## Comenzar por el plan del juego

Antes de que Codex prepare estructura alguna, pídele que cree un archivo `PLAN.md` que defina el juego en términos concretos:

- el objetivo del jugador
- el bucle principal
- los métodos de entrada y los controles
- las condiciones de victoria y derrota
- la progresión o la dificultad
- la dirección visual
- los supuestos sobre el stack tecnológico y el alojamiento
- el orden de los hitos

Ese plan es importante porque “crear un juego” por sí solo es demasiado impreciso. Codex necesita saber cómo implementar cada parte del juego y consultar a menudo los detalles de implementación durante el desarrollo.

Puedes activar el modo plan con el comando slash `/plan`.
Toma el resultado y guárdalo en un archivo `PLAN.md`.

## Guiar el comportamiento de Codex con AGENTS.md

Para asegurarte de que Codex siga el plan, verifique su trabajo y use las herramientas adecuadas, crea un archivo `AGENTS.md` como este:

```text
# Game name

Tech Stack:

- NextJS for frontend (hosted on Vercel)
- <insert technology> for rendering
- Fastify for backend, websockets (hosted on <hosting platform>)
- Postgres for database (hosted on <hosting platform>)
- Redis for caching and pub/sub (hosted on <hosting platform>)
- OpenAI for generative AI features

Tips:

- Use build and test commands to verify your work as soon as you complete a feature or task
- Use the PLAN.md file to guide your work when building new features
- Log your work under .logs (create new log files as you see fit) to record your thought process and decisions, and reference them when iterating on features
- Use playwright to test the visual output of your work, and iterate if it doesn't look right or fit the vibe
- Use imagegen to generate visual assets for your work, and every time you generate a collection of assets, save the prompts you used to be able to continue generating more of the same assets later (create files in .prompts)
- Use Context7 MCP to fetch <rendering framework> docs

Esto permite que Codex trabaje de forma independiente durante mucho tiempo y use las habilidades pertinentes cuando sea necesario.

## Aprovechar las habilidades

Agrega las habilidades mencionadas en el archivo AGENTS.md:

- Imagegen, para que Codex genere recursos visuales para el juego según sea necesario
- Playwright interactive, para que Codex pueda probar el juego en un navegador en ejecución
- Documentación de OpenAI, para que Codex pueda obtener la documentación más reciente de la API de OpenAI
- Si lo deseas, puedes agregar el servidor MCP Context7 para obtener la documentación más reciente del framework de renderizado

Obtén más información sobre cómo agregar habilidades en la [documentación sobre habilidades](/es-419/codex/build-skills).

  **Consejo**: Pídele a Codex que guarde en un archivo los prompts para generar imágenes, de modo que
  todos los recursos visuales sean coherentes entre sí. Dale indicaciones sobre el estilo de los recursos que
  quieres generar y permite que Codex cree prompts detallados y reutilizables.

## Dejar que Codex trabaje e itere

Codex generará una primera versión del juego basada en el plan inicial.

Si tienes muchos recursos de imagen que generar, esta primera versión puede tardar bastante, a veces varias horas. Como Codex puede verificar su trabajo y probar el juego en un navegador en ejecución, puede seguir trabajando durante mucho tiempo sin que intervengas.

Cuanto más definido esté el plan, mejor será el resultado final después de la primera iteración.

A medida que lo pruebes, itera según sea necesario: proporciona capturas de pantalla y solicita cambios en la jugabilidad o actualizaciones de los recursos visuales hasta que el resultado te satisfaga.
