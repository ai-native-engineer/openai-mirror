<!-- source: https://learn.chatgpt.com/es-419/use-cases/github-code-reviews -->

## Cómo usarlo

Comienza por agregar la revisión de código de Codex a tu organización o repositorio de GitHub.
Consulta [Revisión de código de Codex en GitHub](/es-419/codex/third-party/github) para obtener más información.

Puedes configurar Codex para que revise automáticamente cada Pull Request, o puedes solicitar una revisión escribiendo `@codex review` en un comentario de un Pull Request.

Si Codex señala una regresión o un posible problema, puedes pedirle que lo corrija mediante un comentario en el Pull Request con un prompt de seguimiento como `@codex fix it`.

Esto iniciará un nuevo chat en la nube que corregirá el problema y actualizará el Pull Request.

## Definir pautas de revisión

Para personalizar lo que revisa Codex, agrega una sección `## Code Review Rules` en el archivo
`AGENTS.md` más cercano al código al que se aplican las reglas. Por ejemplo:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Coloca las reglas de todo el repositorio en el archivo `AGENTS.md` de la raíz y las reglas específicas de cada servicio
en un archivo anidado. Mantén las reglas concisas, describe el comportamiento que se debe señalar y cualquier
alternativa segura o excepción, y deja las comprobaciones de formato y lint en CI. Consulta
[Personalizar lo que revisa Codex](/es-419/codex/third-party/github#customize-what-codex-reviews)
para obtener orientación sobre la configuración y la redacción de reglas.
