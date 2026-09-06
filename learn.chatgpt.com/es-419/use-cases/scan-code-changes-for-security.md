<!-- source: https://learn.chatgpt.com/es-419/use-cases/scan-code-changes-for-security -->

## Revisar el cambio en lugar de todo el repositorio

Usa un análisis de seguridad del diff cuando un Pull Request, un Commit, una rama o un parche local
modifique una ruta sensible del código. El Plugin de Codex Security usa el contexto del repositorio
para comprender el cambio y, luego, centra la detección y validación de hallazgos
en el diff y en el código directamente relacionado.

Este flujo de trabajo complementa la revisión de código habitual. Úsalo cuando busques evidencia
sobre regresiones de seguridad, no una revisión general de estilo o de pruebas.

## Realizar una revisión enfocada

1. Abre el repositorio y haz checkout del conjunto exacto de cambios del repositorio Git que quieres revisar, o descríbelo.
2. Completa el [Inicio rápido del Plugin de Codex Security](/es-419/codex/security/plugin) y especifica en el prompt inicial el Pull Request, el Commit, el diff de rama o el parche del árbol de trabajo.
3. Indica las superficies de alto riesgo del cambio, como la autenticación, los analizadores sintácticos, las rutas de archivos, las solicitudes de red o el manejo de credenciales.
4. Ejecuta el prompt sin solicitar una corrección para que el primer resultado siga siendo un artefacto de revisión.
5. Verifica cada línea que el informe señale como afectada, cada resultado de validación y cada falta de pruebas indicada antes de decidir si es necesario tomar medidas correctivas.

## Dar seguimiento a un hallazgo

Un informe útil distingue entre un hallazgo de seguridad alcanzable, sustentado por evidencia, y una
sospecha que aún requiere confirmación, y puede incluir comentarios de código en línea
para las líneas afectadas. Para actuar sobre el resultado, abre una nueva tarea acotada
de corrección con el identificador del hallazgo o la sección pertinente del informe.
Consulta [Corregir una lista de vulnerabilidades pendientes](/es-419/codex/use-cases/remediate-vulnerability-backlog)
para conocer el ciclo de corrección y validación.

Para obtener detalles sobre los selectores de cambios, el alcance del diff y la revisión de resultados, consulta [Revisar cambios de código
para detectar problemas de seguridad](/es-419/codex/security/plugin/code-changes).
