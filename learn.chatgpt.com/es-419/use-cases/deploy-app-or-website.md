<!-- source: https://learn.chatgpt.com/es-419/use-cases/deploy-app-or-website -->

## Comienza con el sitio y el destino del despliegue

Codex puede crear o actualizar un sitio web o una aplicación, ejecutar las verificaciones del proyecto, realizar el despliegue en Vercel y devolver la URL.

Una entrega útil incluye material concreto: un repositorio, una captura de pantalla, un mapa, un brief de diseño, una nota de producto, documentación de una API o una fuente de datos. Codex debe inspeccionar el proyecto antes de modificarlo y luego usar el complemento de Vercel para desplegar una vista previa de forma predeterminada.

Usa `@build-web-apps` cuando Codex necesite crear o perfeccionar la aplicación. Usa `@vercel` cuando deba desplegarla, inspeccionar el despliegue o consultar los registros de compilación de Vercel.

## Verifica el resultado antes de compartirlo

Codex debe indicarte qué cambios hizo, qué comando usó para compilar el proyecto y si el despliegue en Vercel está listo. Si el despliegue requiere configurar una variable de entorno, elegir un equipo, configurar un dominio o iniciar sesión, Codex debe señalarlo en lugar de fingir que el sitio está terminado.

Haz explícitos los cambios en producción. Un despliegue de vista previa es la opción predeterminada; solicita un despliegue en producción solo cuando esa sea realmente tu intención.

## Itera a partir de la URL activa

Cuando tengas la vista previa, mantén abierto el mismo chat. Pídele a Codex que abra la URL, corrija problemas de diseño, actualice los textos, integre los datos que faltan o consulte los registros de Vercel si falla el despliegue. El chat ya tiene el contexto del repositorio, el despliegue y la compilación.

Conviene que las solicitudes de seguimiento sean específicas:

- “Hay muy poco espacio en el diseño para dispositivos móviles. Corrígelo y vuelve a desplegar la vista previa.”
- “Usa el mismo proyecto y agrega los datos más recientes de \[source\].”
- “Lee los registros de la compilación fallida y corrige el despliegue.”
