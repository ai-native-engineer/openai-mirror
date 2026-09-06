<!-- source: https://learn.chatgpt.com/es-419/docs/security/threat-model -->

Aprende qué es un modelo de amenazas y cómo mejoran las sugerencias de Codex Security cuando lo editas.

## Qué es un modelo de amenazas

Un modelo de amenazas es un breve resumen de seguridad sobre cómo funciona tu repositorio. En Codex Security, lo editas como `project overview`, y el sistema lo usa como contexto para futuros análisis, así como para priorizar y revisar los hallazgos.

Codex Security crea el primer borrador a partir del código. Si los hallazgos no parecen acertados, esto es lo primero que debes editar.

Un modelo de amenazas útil destaca:

- los puntos de entrada y los datos de entrada no confiables
- los límites de confianza y los supuestos sobre la autenticación
- las rutas de los datos confidenciales o las acciones privilegiadas
- las áreas que tu equipo quiere que se revisen primero

Por ejemplo:

> API pública para realizar cambios en cuentas. Acepta solicitudes JSON y cargas de archivos. Usa un servicio interno de autenticación para verificar la identidad y registra los cambios de facturación mediante un servicio interno. Centra la revisión en las comprobaciones de autenticación, el análisis de los archivos cargados y los límites de confianza entre servicios.

Esto le da a Codex Security un mejor punto de partida para futuros análisis y para priorizar los hallazgos.

## Mejorar y volver a revisar el modelo de amenazas

Si quieres mejorar los resultados, edita primero el modelo de amenazas. Úsalo cuando los hallazgos no abarquen las áreas que te interesan o aparezcan en lugares inesperados. El modelo de amenazas cambia el contexto de los análisis futuros.

  Algunos usuarios copian el modelo de amenazas actual en Codex y usan un chat para mejorarlo
según las áreas que quieren que se revisen con más detalle. Después, vuelven a pegar la versión actualizada
en la interfaz web.

### Dónde editarlo

Para revisar o actualizar el modelo de amenazas, ve a los [análisis de Codex Security](https://chatgpt.com/codex/security/scans), abre el repositorio y haz clic en **Editar**.

## Documentación relacionada

- [Configuración de Codex Security en la nube](/es-419/codex/security/setup) explica cómo configurar el repositorio y revisar los hallazgos.
- [Codex Security](/es-419/codex/security) presenta una descripción general del producto.
- [Preguntas frecuentes sobre Codex Security en la nube](/es-419/codex/security/faq) responde preguntas comunes sobre la nube.
