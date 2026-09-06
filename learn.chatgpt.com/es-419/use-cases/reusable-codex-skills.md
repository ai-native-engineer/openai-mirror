<!-- source: https://learn.chatgpt.com/es-419/use-cases/reusable-codex-skills -->

## Crea una habilidad que Codex pueda tener disponible

Usa habilidades para darle a Codex instrucciones, recursos y scripts reutilizables para las tareas que repites. Una [habilidad](/es-419/codex/build-skills) puede conservar la tarea, el documento, el comando o el ejemplo que hizo que Codex fuera útil la primera vez.

Empieza con un ejemplo que haya funcionado: un chat de Codex en el que se hizo cherry-pick de un PR, una lista de verificación de lanzamiento de Notion, un conjunto de comentarios útiles en un PR o un hilo de Slack que explique un proceso de lanzamiento.

## Cómo usarlo

1. Agrega el contexto que quieres que use Codex.

   Quédate en el chat de Codex que quieres conservar, pega el hilo de Slack o el enlace a la documentación y agrega la regla, el comando o el ejemplo que Codex debe recordar.

2. Ejecuta el prompt inicial.

   El prompt asigna un nombre a la habilidad que quieres crear y luego proporciona a `$skill-creator` la tarea, el documento, el PR, el comando o el resultado que debe conservar.

3. Deja que Codex cree y valide la habilidad.

   El resultado debe definir `$skill-name`, describir cuándo debe activarse y guardar las instrucciones reutilizables en el lugar correcto.

   Las habilidades que están en `~/.codex/skills` se pueden usar desde cualquier repositorio. Las habilidades del repositorio actual pueden incluirse en un commit para que tus compañeros de equipo también las usen.

4. Usa la habilidad y luego actualízala desde el chat.

   Invoca la nueva habilidad `$skill-name` en el próximo PR, alerta, revisión, nota de lanzamiento o tarea de diseño. Si usa un comando de prueba incorrecto, pasa por alto una regla de revisión, omite un paso del runbook o redacta un borrador que no enviarías, pídele a Codex que agregue esa corrección a la habilidad.

## Proporciona material de referencia

Dale a `$skill-creator` el material que explica cómo debe funcionar la habilidad.

| Lo que tienes                                              | Qué agregar                                                                                                                                                             |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Un flujo de trabajo de un chat de Codex que quieres conservar** | Quédate en ese chat y escribe `use this chat`. Codex puede usar el contexto, los comandos, los cambios y los comentarios del chat como punto de partida.                                         |
| **Documentación o un runbook**                                      | Pega la lista de verificación de lanzamiento, incluye un enlace al runbook de respuesta a incidentes, adjunta el PDF de la API o indícale a Codex dónde está la guía de Markdown en tu repositorio.                                 |
| **Conversación del equipo**                                      | Pega el hilo de Slack en el que alguien explicó una alerta, incluye el enlace a la revisión del PR con las reglas de frontend o adjunta la conversación de soporte que explica el problema del cliente. |
| **Scripts o comandos que la habilidad debe reutilizar**             | Agrega el comando de prueba, el comando de vista previa, el script de lanzamiento, el script para obtener registros o el comando auxiliar local que quieres que Codex ejecute en tareas futuras.                                    |
| **Un buen resultado**                                          | Agrega el PR fusionado, la entrada final del registro de cambios, la nota de lanzamiento aprobada, el ticket resuelto, la captura de pantalla del antes y el después o la respuesta final de Codex que quieres que las tareas futuras imiten.         |

Si la fuente está en Slack, Linear, GitHub, Notion o Sentry, conecta esa herramienta a Codex mediante un [complemento](/es-419/codex/plugins), menciónala en el prompt inicial o pega la parte relevante en el chat.

## Lo que crea Codex

La mayoría de las habilidades comienzan con un archivo `SKILL.md`. `$skill-creator` puede agregar material de referencia más extenso, scripts o recursos cuando el flujo de trabajo los necesite.

## Habilidades que podrías crear

Usa el mismo patrón cuando las tareas futuras deban consultar el mismo runbook, ejecutar la misma CLI, seguir los mismos criterios de revisión, redactar la misma actualización para el equipo o realizar el control de calidad del mismo flujo en el navegador. Por ejemplo:

- **`$buildkite-fix-ci`** descarga los registros de las tareas fallidas, diagnostica el error y propone la corrección mínima en el código.
- **`$fix-merge-conflicts`** hace checkout de un PR de GitHub, lo pone al día con la rama base, resuelve los conflictos y devuelve el comando exacto para hacer push.
- **`$frontend-skill`** mantiene a Codex alineado con tus preferencias de UI, los componentes existentes, el ciclo de control de calidad con capturas de pantalla, la selección de recursos y la etapa de pulido en el navegador.
- **`$pr-review-comments`** convierte las notas de revisión en comentarios concisos en línea con el tono adecuado y enlaces de GitHub.
- **`$web-game-prototyper`** define el alcance del primer ciclo jugable, selecciona recursos, ajusta la sensación de juego, toma capturas de pantalla y pule el resultado en el navegador.
