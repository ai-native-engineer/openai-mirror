<!-- source: https://learn.chatgpt.com/es-419/use-cases/make-granular-ui-changes -->

## Introducción

Si ya tienes una aplicación y quieres iterar rápidamente sobre la UI, puedes usar `gpt-5.3-codex-spark` para realizar cambios pequeños y puntuales en la UI.
Codex-Spark es nuestro modelo más rápido, optimizado para iteraciones de código en tiempo real y prácticamente instantáneas.

Este enfoque funciona mejor con un ciclo bien acotado: un comentario visual, una edición puntual, una comprobación en el navegador y, después, el siguiente comentario.

  Puedes usar el [modelo Codex Spark](/es-419/codex/models) para esta tarea. Está
  disponible en los planes Pro.

## Elige tu modelo

Para iterar rápidamente sobre la UI, comienza con `gpt-5.3-codex-spark` si tienes acceso a este modelo. Es menos capaz que nuestros modelos de uso general, pero está diseñado para iteraciones de código en tiempo real. Si no tienes acceso a este modelo, usa <code>{RECOMMENDED_MODEL_REFERENCES.latestMainlineModel.slug}</code> con un nivel de esfuerzo de razonamiento `medium` o `low`.

Ese equilibrio entre velocidad y capacidad resulta útil para los cambios puntuales en la UI. Por lo general, no necesitas el modelo con el razonamiento más profundo para mover un botón, ajustar un breakpoint o cambiar el estado de un componente. Necesitas un modelo que responda rápido, entienda el código del área en cuestión, edite el archivo correcto y pueda repetir el ciclo sin que la iteración resulte engorrosa.

## Flujo de desarrollo

1. Abre la aplicación existente y deja a la vista la ruta o el componente relevante.
2. Abre el chat activo de Codex en una [ventana flotante](/codex/reference/settings#keep-a-chat-near-your-work) y mantenla cerca del navegador, el editor o la vista previa del diseño mientras trabajas.
3. Pídele a Codex que haga un cambio específico en la UI por vez. Incluye la ruta, el viewport, la captura de pantalla actual, la captura de pantalla objetivo o el comentario exacto sobre el producto, si los tienes.
4. Pídele a Codex que inspeccione la implementación actual, realice el cambio mínimo justificable y preserve los componentes, tokens, primitivas de layout y flujo de datos existentes de la aplicación.
5. Revisa el resultado y luego envía el siguiente pequeño ajuste en el mismo chat.

## Escribe prompts acotados

Los prompts para cambios puntuales en la UI deben ser directos y acotados. Un buen prompt especifica el área de la UI, el cambio deseado y la validación que esperas.

Si el resultado está cerca de lo esperado, pero no es del todo correcto, haz que el prompt de seguimiento sea igual de específico:

## Cuándo reducir el ritmo

No sigas usando el ciclo rápido si la tarea deja de ser puntual. Cambia a un modelo más capaz y formula un prompt con más detenimiento cuando el cambio requiera una refactorización amplia, una nueva primitiva del sistema de diseño, un comportamiento de accesibilidad no trivial o una decisión de producto que afecte a más de una pantalla.

La iteración rápida en la UI funciona mejor cuando Codex ajusta una parte de la UI que ya comprende, en lugar de rediseñar la aplicación desde cero.
