<!-- source: https://learn.chatgpt.com/es-419/docs/image-inputs -->

Agrega imágenes a un prompt cuando la tarea dependa del contexto visual, como una
captura de pantalla de un error, un diseño de interfaz, un diagrama de arquitectura o un recurso existente. Explica
qué debe inspeccionar ChatGPT y qué resultado quieres obtener; no confíes únicamente en la imagen
para comunicar la tarea.

Arrastra una imagen al editor de prompts mientras mantienes presionada <kbd>Mayús</kbd> para incluirla
como contexto. También puedes pedirle a ChatGPT que inspeccione una imagen en tu sistema o usar
una herramienta de captura de pantalla para verificar el trabajo en otra aplicación.

Adjunta, pega o arrastra una imagen al editor web de ChatGPT. En el prompt,
indícale a ChatGPT qué debe inspeccionar y qué resultado quieres obtener de la imagen.

Pega una imagen en el editor interactivo o especifica uno o más archivos en la
línea de comandos:

```bash
codex -i screenshot.png "Explain this error and suggest the smallest fix"
codex --image before.png,after.png "Compare these states and list the regressions"

Si usas varias imágenes, separa las rutas con comas o repite `--image`. Codex
admite formatos de imagen comunes, incluidos PNG y JPEG.

Arrastra una imagen al editor de prompts mientras mantienes presionada <kbd>Mayús</kbd> para que la
extensión reciba la imagen en lugar de pasarla al editor.

## Redacta el prompt en torno a la imagen

Indica qué muestra la imagen, señala el área relevante y especifica el resultado
y las restricciones. Si adjuntas más de una imagen, identifica cada una y explica
cómo debe compararlas ChatGPT.

Por ejemplo:

```text
Compare this checkout screen with the design. Fix spacing and typography only;
do not change behavior. Verify the result with a new screenshot.

## Usa la función adecuada para imágenes

Usa una entrada de imagen cuando quieras que ChatGPT inspeccione una referencia visual. Usa
la [generación de imágenes](/es-419/codex/image-generation) cuando quieras que ChatGPT
cree o edite una imagen.
