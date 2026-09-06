<!-- source: https://learn.chatgpt.com/es-419/use-cases/update-documentation -->

## Introducción

Mantener la documentación al día es más fácil cuando se actualiza junto con los cambios en el código fuente, no semanas después. Codex puede revisar el código modificado, las pruebas, las notas de la versión, los issues vinculados y el contexto del Pull Request para luego preparar una actualización acotada de la documentación que se ajuste a la estructura existente.

Usa este flujo de trabajo para la documentación para desarrolladores, las actualizaciones de archivos README, los borradores del registro de cambios, las notas de migración, las guías operativas o cualquier otro contenido que deba reflejar comportamientos que cambian con frecuencia.

## Cómo usarlo

1. Empieza por el cambio que necesitas documentar.

   Comparte la rama, el Pull Request, el commit, el issue o los archivos. Si la documentación es pública, indica explícitamente que no deben incluirse hojas de ruta no publicadas, datos privados de clientes ni contexto de uso exclusivamente interno.

2. Pídele a Codex que identifique la documentación afectada.

   Antes de redactar, haz que busque en la documentación existente nombres de funcionalidades, claves de configuración, comandos, ejemplos y términos relacionados.

3. Actualiza solo la parte mínima necesaria de la documentación.

   Codex debe conservar la estructura actual de las páginas, la terminología, los enlaces cruzados y los metadatos de cabecera. Debe evitar reescrituras extensas cuando baste con una nota precisa, un ejemplo o la actualización de una sección.

4. Verifica los cambios.

   Pídele a Codex que ejecute las comprobaciones de formato y documentación adecuadas para el repositorio y que luego resuma la evidencia que respalda cada afirmación visible para los usuarios.

## Qué proporcionarle a Codex

| Fuente                               | Por qué resulta útil                                                               |
| ------------------------------------ | -------------------------------------------------------------------------- |
| Código y pruebas modificados               | Permite que Codex analice el comportamiento real para preparar actualizaciones específicas de la documentación. |
| Notas públicas de la versión o documentación del producto | Ayuda a Codex a respetar la terminología pública y reflejar correctamente la disponibilidad y el estado de la funcionalidad.    |
| Contexto del Pull Request o del issue        | Explica por qué se realizó el cambio y qué comportamiento visible para los usuarios es relevante.   |
| Comprobaciones locales de la documentación                    | Le da a Codex un criterio concreto de finalización antes de que se publique la documentación.   |

Agregar más contexto, como notas públicas de la versión, permite que Codex evite incluir contexto privado o actualizaciones que aún no se hayan hecho públicas.

## Hacer que el flujo de trabajo sea repetible

Para establecer una convención aplicable a todo el repositorio, agrega las expectativas de documentación a [AGENTS.md](/es-419/codex/agent-configuration/agents-md). Por ejemplo:

```md
## Documentation

- When user-facing behavior changes, check whether docs, examples, or changelogs need updates.
- Public docs must only include public information or behavior visible in this repo.
- Preserve existing terminology and frontmatter.
- Run the docs formatting and build checks before final handoff.

Si el proceso tiene más pasos, conviértelo en una [habilidad](/es-419/codex/build-skills) para que las futuras tareas de Codex puedan seguir el mismo ciclo de revisión de fuentes, redacción y verificación. Consulta [Guardar flujos de trabajo como habilidades](/es-419/codex/use-cases/reusable-codex-skills) para obtener más detalles sobre este patrón.

También puedes [programar una tarea para este flujo de trabajo desde el chat actual](/es-419/codex/automations#schedule-a-task-inside-a-chat). Por ejemplo, pídele a Codex que obtenga los Pull Requests recientes de GitHub y mantenga la documentación actualizada cada semana:
