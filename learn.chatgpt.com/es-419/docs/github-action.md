<!-- source: https://learn.chatgpt.com/es-419/docs/github-action -->

Usa la GitHub Action de Codex (`openai/codex-action@v1`) para ejecutar Codex en trabajos de CI/CD, aplicar parches o publicar revisiones desde un flujo de trabajo de GitHub Actions.
La acción instala la CLI de Codex, inicia el proxy de Responses API cuando proporcionas una clave de API y ejecuta `codex exec` con los permisos que especifiques.

Usa esta acción cuando quieras:

- Automatizar los comentarios de Codex sobre pull requests o versiones sin tener que administrar la CLI.
- Supeditar los cambios a controles de calidad realizados por Codex como parte de tu pipeline de CI.
- Ejecutar tareas repetibles de Codex (revisión de código, preparación de versiones y migraciones) desde un archivo de flujo de trabajo.

Para ver un ejemplo de CI, consulta el [Modo no interactivo](/es-419/codex/non-interactive-mode) y explora el código fuente en el [repositorio openai/codex-action](https://github.com/openai/codex-action).

## Requisitos previos

- Guarda tu clave de OpenAI como un secreto de GitHub (por ejemplo, `OPENAI_API_KEY`) y haz referencia a ella en el flujo de trabajo.
- Ejecuta el trabajo en un ejecutor de Linux o macOS. En Windows, establece `safety-strategy: unsafe`.
- Haz checkout de tu código antes de invocar la acción para que Codex pueda leer el contenido del repositorio.
- Decide qué prompts quieres ejecutar. Puedes proporcionar texto en línea mediante `prompt` o usar `prompt-file` para indicar la ruta de un archivo versionado en el repositorio.

## Flujo de trabajo de ejemplo

El flujo de trabajo de ejemplo que aparece a continuación revisa los pull requests nuevos, captura la respuesta de Codex y la publica en el PR.

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge
          fetch-depth: 0
          persist-credentials: false

      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    permissions:
      issues: write
      pull-requests: write
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}

Reemplaza `.github/codex/prompts/review.md` por tu propio archivo de prompt o usa la entrada `prompt` para proporcionar texto en línea. El ejemplo también escribe el mensaje final de Codex en `codex-output.md` para inspeccionarlo más adelante o subirlo como artefacto.

## Configurar `codex exec`

Ajusta cómo se ejecuta Codex configurando las entradas de la acción que corresponden a las opciones de `codex exec`:

- `prompt` o `prompt-file` (elige una opción): instrucciones en línea o una ruta dentro del repositorio que apunte a un archivo Markdown o de texto con tu tarea. Considera guardar los prompts en `.github/codex/prompts/`.
- `codex-args`: flags adicionales de la CLI. Proporciona un arreglo JSON (por ejemplo, `["--ephemeral"]`) o una cadena de shell (`--profile ci`) para configurar sesiones, perfiles o ajustes de MCP.
- `model` y `effort`: elige la configuración del agente de Codex que quieras; deja ambos campos vacíos para usar los valores predeterminados.
- `sandbox`: configura el modo de sandbox (`workspace-write`, `read-only`, `danger-full-access`) de acuerdo con los permisos que Codex necesite durante la ejecución.
- `output-file`: guarda el mensaje final de Codex en el disco para que los pasos posteriores puedan subirlo o compararlo.
- `codex-version`: fija una versión específica de la CLI. Déjalo en blanco para usar la última versión publicada.
- `codex-home`: indica un directorio de inicio compartido de Codex si quieres reutilizar archivos de configuración o configuraciones de MCP entre pasos.

## Administrar privilegios

En los ejecutores alojados en GitHub, Codex tiene acceso amplio a menos que lo restrinjas. Usa estas entradas para controlar la exposición:

- `safety-strategy` (valor predeterminado: `drop-sudo`) elimina `sudo` antes de ejecutar Codex. Este cambio no puede revertirse durante el trabajo y protege los secretos almacenados en la memoria. En Windows, debes establecer `safety-strategy: unsafe`.
- `unprivileged-user` combina `safety-strategy: unprivileged-user` con `codex-user` para ejecutar Codex con una cuenta específica. Asegúrate de que el usuario tenga permisos de lectura y escritura en la copia local del repositorio (consulta el [ejemplo de `unprivileged-user`](https://github.com/openai/codex-action/blob/main/examples/unprivileged-user.yml) para corregir la propiedad).
- `read-only` impide que Codex cambie archivos o use la red, pero se sigue ejecutando con privilegios elevados. No confíes únicamente en `read-only` para proteger los secretos.
- `sandbox` limita, dentro del propio Codex, el acceso al sistema de archivos y a la red. Elige la opción más restrictiva que permita completar la tarea.
- `allow-users` y `allow-bots` restringen quién puede activar el flujo de trabajo. De manera predeterminada, solo los usuarios con acceso de escritura pueden ejecutar la acción; agrega explícitamente las cuentas de confianza adicionales o deja el campo vacío para mantener el comportamiento predeterminado.

## Capturar resultados

La acción emite el último mensaje de Codex mediante la salida `final-message`. Asígnalo a una salida del trabajo (como se muestra arriba) o procésalo directamente en pasos posteriores. Combina `output-file` con la función para subir artefactos si prefieres recopilar la transcripción completa del ejecutor. Cuando necesites datos estructurados, pasa `--output-schema` mediante `codex-args` para aplicar un esquema JSON.

## Lista de verificación de seguridad

- Limita quién puede iniciar el flujo de trabajo. Prioriza los eventos de confianza o las aprobaciones explícitas en lugar de permitir que cualquiera ejecute Codex en tu repositorio.
- Sanea las entradas de prompts procedentes de pull requests, mensajes de commit o contenido de issues para evitar la inyección de prompts. Revisa los comentarios HTML o el texto oculto antes de proporcionarlos a Codex.
- Protege tu `OPENAI_API_KEY`: conserva `safety-strategy` en `drop-sudo` o ejecuta Codex con un usuario sin privilegios. Nunca dejes la acción en modo `unsafe` en ejecutores compartidos entre varios usuarios.
- Ejecuta Codex como el último paso de un trabajo para que los pasos posteriores no hereden cambios de estado inesperados.
- Rota las claves de inmediato si sospechas que los registros del proxy o la salida de la acción expusieron datos secretos.

## Solución de problemas

- **Configuraste tanto prompt como prompt-file**: quita la entrada duplicada para proporcionar una sola fuente.
- **responses-api-proxy no escribió la información del servidor**: confirma que la clave de API esté presente y sea válida; el proxy solo se inicia cuando proporcionas `openai-api-key`.
- **Se esperaba que se eliminara `sudo`, pero `sudo` se ejecutó correctamente**: asegúrate de que ningún paso anterior haya restaurado `sudo` y de que el sistema operativo del ejecutor sea Linux o macOS. Vuelve a ejecutarlo con un trabajo nuevo.
- **Errores de permisos después de `drop-sudo`**: otorga acceso de escritura antes de que se ejecute la acción (por ejemplo, con `chmod -R g+rwX "$GITHUB_WORKSPACE"` o mediante el patrón unprivileged-user).
- **Se bloqueó una activación no autorizada**: ajusta las entradas `allow-users` o `allow-bots` si necesitas permitir cuentas de servicio además de los colaboradores con acceso de escritura incluidos de forma predeterminada.
