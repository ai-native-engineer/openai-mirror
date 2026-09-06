<!-- source: https://learn.chatgpt.com/es-419/use-cases/feedback-synthesis -->

## Antes de comenzar

Los comentarios sobre el producto pueden estar en Slack, exportaciones de encuestas, sistemas de seguimiento de issues, registros de soporte o notas de investigación. Proporciona a ChatGPT Work las fuentes, el área del producto y el intervalo de fechas que debe revisar. Puede agrupar los problemas recurrentes en una hoja de cálculo o un documento que el equipo pueda revisar antes de decidir qué hacer a continuación.

Inicia este flujo de trabajo en Work, ya sea en la web o en la app de escritorio, con apps conectadas y archivos en la nube. Si la fuente está en tu computadora, primero adjunta una exportación local o usa la app de escritorio.

## Qué esperar

Este ejemplo usa una exportación de encuesta, registros de soporte, un hilo de comentarios y notas de investigación para una cola de revisión de solicitudes. El primer análisis agrupa los problemas recurrentes; la solicitud de seguimiento divide un tema amplio en dos decisiones más claras.

<div data-use-case-export-only>

El primer análisis detectó tres problemas recurrentes en una encuesta, registros de soporte, un hilo de comentarios y notas de investigación:

- **Los conflictos están ocultos en la cola:** ocho menciones en cuatro fuentes. Muestra el estado de los conflictos en la lista y distingue `Ready` de `Needs attention`.
- **La aprobación masiva puede incluir solicitudes bloqueadas:** cuatro menciones en cuatro fuentes. Omite las solicitudes bloqueadas de forma predeterminada o muestra una advertencia antes de aprobarlas.
- **Los revisores pierden su posición en la cola y no pueden aislar el trabajo:** diez menciones en cuatro fuentes. Conserva la búsqueda y los filtros, y ofrece una vista de `Needs attention`.

Tras una solicitud adicional para separar el último tema, la tabla distingue **el restablecimiento de la búsqueda y los filtros al regresar** de **la dificultad para aislar el trabajo bloqueado y no revisado**. La tabla mantiene, junto a cada tema, los usuarios afectados, los ID de evidencia, el nivel de confianza, las implicaciones para el diseño, las preguntas abiertas y las acciones de seguimiento. Estas cifras corresponden a menciones repetidas en una muestra pequeña, no a tasas de incidencia de todo el producto.

</div>

## Cómo funciona

1. Proporciona a Work las fuentes de comentarios, el área del producto y el período de revisión.
2. Pídele que agrupe por temas los comentarios recurrentes y conserve junto a cada tema los enlaces o ID que los respaldan.
3. Crea una hoja de cálculo o un documento de Google con los usuarios afectados, el nivel de confianza, las preguntas abiertas y la decisión que se debe tomar o la acción de seguimiento necesaria.
4. Revisa el resumen antes de convertir cualquier tema en una actualización para Slack o en un borrador de issue.

Usa el prompt inicial de esta página para el primer análisis y luego ajusta cualquier tema que sea demasiado amplio, carezca de evidencia o mezcle problemas distintos.

## Convierte un tema revisado en el siguiente borrador

Una vez que exista el resumen, pídele a Work que divida un tema amplio, agregue la evidencia faltante, redacte una actualización para Slack o convierta un tema revisado en un borrador de issue. Especifica el público destinatario y la decisión para que quede claro el siguiente paso.

## Mantén actualizado un canal de comentarios

Para un canal de Slack o una cola de issues que sigue recibiendo reportes nuevos, pídele a Work que [lo revise de forma programada](/es-419/codex/automations#schedule-work-from-a-task). Mantén los mismos límites de revisión para que los nuevos comentarios no den lugar, sin aprobación previa, a una publicación, un issue o una asignación.
