<!-- source: https://learn.chatgpt.com/es-419/docs/non-interactive-mode -->

El modo no interactivo te permite ejecutar Codex desde scripts (por ejemplo, trabajos de integración continua (CI)) sin abrir la TUI interactiva.
Se invoca con `codex exec`.

Para obtener información detallada sobre las opciones, consulta [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec).

## Cuándo usar `codex exec`

Usa `codex exec` cuando quieras que Codex:

- Se ejecute como parte de una canalización (CI, comprobaciones previas a la fusión y trabajos programados).
- Genere una salida que puedas pasar a otras herramientas (por ejemplo, para generar notas de la versión o resúmenes).
- Se integre de forma natural en flujos de trabajo de la CLI que encadenan comandos para pasar su salida a Codex y la salida de Codex a otras herramientas.
- Se ejecute con opciones explícitas y preestablecidas de sandbox y aprobación.

## Uso básico

Pasa un prompt de tarea como un único argumento:

```bash
codex exec "summarize the repository structure and list the top 5 risky areas"

Mientras se ejecuta `codex exec`, Codex transmite el progreso a `stderr` y solo imprime el mensaje final del agente en `stdout`. Esto facilita redirigir o canalizar el resultado final:

```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md

Usa `--ephemeral` cuando no quieras conservar en el disco los archivos de ejecución de la sesión:

```bash
codex exec --ephemeral "triage this repository and suggest next steps"

Si canalizas datos a stdin y también proporcionas un argumento de prompt, Codex trata el prompt como la instrucción y el contenido canalizado como contexto adicional.

Así puedes generar datos de entrada con un comando y pasarlos directamente a Codex:

```bash
curl -s https://jsonplaceholder.typicode.com/comments \
  | codex exec "format the top 20 items into a markdown table" \
  > table.md

Para conocer patrones más avanzados de canalización de stdin, consulta [Canalización avanzada de stdin](#advanced-stdin-piping).

## Permisos y seguridad

De forma predeterminada, `codex exec` se ejecuta en un sandbox de solo lectura. En las automatizaciones, configura los permisos mínimos necesarios para el flujo de trabajo:

- Permitir ediciones: `codex exec --sandbox workspace-write "<task>"`
- Permitir un acceso más amplio: `codex exec --sandbox danger-full-access "<task>"`

Usa `danger-full-access` solo en un entorno controlado (por ejemplo, un ejecutor de CI aislado o un contenedor).

Codex conserva `codex exec --full-auto` como una opción de compatibilidad obsoleta y muestra una advertencia. En los scripts nuevos, usa la opción explícita `--sandbox workspace-write` en su lugar.

Usa `--ignore-user-config` cuando necesites una ejecución que no cargue `$CODEX_HOME/config.toml` y `--ignore-rules` cuando necesites omitir los archivos `.rules` de execpolicy del usuario y del proyecto en un entorno de automatización controlado.

Si configuras un servidor MCP habilitado con `required = true` y este no se inicializa, `codex exec` finaliza con un error en lugar de continuar sin ese servidor.

## Hacer que la salida sea legible por máquina

Para procesar la salida de Codex en scripts, usa el formato JSON Lines:

```bash
codex exec --json "summarize the repo structure" | jq

Cuando habilitas `--json`, `stdout` se convierte en un flujo de JSON Lines (JSONL) para que puedas capturar todos los eventos que Codex emite mientras se ejecuta. Los tipos de eventos incluyen `thread.started`, `turn.started`, `turn.completed`, `turn.failed`, `item.*` y `error`.

Los tipos de elementos incluyen mensajes del agente, razonamiento, ejecuciones de comandos, cambios en archivos, llamadas a herramientas de MCP, búsquedas web y actualizaciones del plan.

Ejemplo de flujo JSON (cada línea es un objeto JSON):

```jsonl
{"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122,"reasoning_output_tokens":0}}

Si solo necesitas el mensaje final, escríbelo en un archivo con `-o <path>`/`--output-last-message <path>`. Esto guarda el mensaje final en el archivo y aun así lo imprime en `stdout` (consulta [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec) para obtener más detalles).

## Crear resultados estructurados con un esquema

Si necesitas datos estructurados para pasos posteriores, usa `--output-schema` para solicitar una respuesta final que se ajuste a un JSON Schema.
Esto resulta útil en flujos de trabajo automatizados que necesitan campos estables (por ejemplo, resúmenes de trabajos, informes de riesgos o metadatos de versiones).

`schema.json`

```json
{
  "type": "object",
  "properties": {
    "project_name": { "type": "string" },
    "programming_languages": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["project_name", "programming_languages"],
  "additionalProperties": false
}

Ejecuta Codex con el esquema y escribe la respuesta JSON final en el disco:

```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json

Ejemplo de salida final (stdout):

```json
{
  "project_name": "Codex CLI",
  "programming_languages": ["Rust", "TypeScript", "Shell"]
}

## Autenticación en automatizaciones

`codex exec` reutiliza de forma predeterminada la autenticación guardada de la CLI. En CI, es habitual proporcionar las credenciales de forma explícita:

Si tu entorno de ejecución de confianza en la nube o de CI ya recibe tokens de cargas de trabajo
de corta duración, usa la
[federación de identidades de cargas de trabajo](/es-419/codex/enterprise/workload-identity)
en lugar de almacenar una credencial de OpenAI.

### Usar la autenticación con clave de API

Para GitHub Actions, usa la [GitHub Action de Codex](/es-419/codex/github-action) en lugar de instalar y autenticar la CLI por tu cuenta. La acción está diseñada para reducir la exposición de la clave de API: instala Codex, inicia un proxy de Responses API y ejecuta Codex con una estrategia de seguridad configurable.

No configures `OPENAI_API_KEY` ni `CODEX_API_KEY` como variables de entorno a nivel de trabajo en flujos de trabajo que hagan checkout de código controlado por el repositorio o lo ejecuten. Los scripts de compilación, las pruebas, los hooks del ciclo de vida de las dependencias o una acción comprometida en el mismo trabajo pueden leer esas variables de entorno.

En otros entornos de automatización, configura `CODEX_API_KEY` solo para la invocación de Codex
que la necesite y asegúrate de que no se ejecute código que no sea de confianza en el mismo
entorno del proceso.

Para usar una clave de API diferente en una sola ejecución, configura `CODEX_API_KEY` en línea:

```bash
CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"

Puedes usar `CODEX_API_KEY` con `codex exec`, `codex review`, el SDK
de TypeScript y `codex exec-server --remote`.

Lee esta sección si necesitas ejecutar trabajos de CI/CD con una cuenta de usuario de Codex en lugar de una
clave de API, como los equipos empresariales que usan el acceso a Codex administrado por ChatGPT en ejecutores de confianza
o los usuarios que necesitan los límites de solicitudes de ChatGPT/Codex en lugar de usar una clave de API.

Las claves de API son la opción predeterminada adecuada para la automatización porque son más fáciles de
aprovisionar y rotar. Usa esta opción solo si necesitas específicamente ejecutar tareas con
tu cuenta de Codex.

Trata `~/.codex/auth.json` como una contraseña: contiene tokens de acceso. No
lo incluyas en ningún commit, lo pegues en tickets ni lo compartas en el chat.

No uses este flujo de trabajo para repositorios públicos o de código abierto. Si `codex login`
no es una opción en el ejecutor, carga `auth.json` desde un almacenamiento seguro, ejecuta
Codex en el ejecutor para que Codex lo actualice en la misma ubicación y conserva el archivo actualizado
entre ejecuciones.

Consulta [Mantener la autenticación de la cuenta de Codex en CI/CD (avanzado)](/codex/auth/ci-cd-auth).

## Reanudar una sesión no interactiva

Si necesitas continuar una ejecución anterior (por ejemplo, una canalización de dos etapas), usa el subcomando `resume`:

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"

También puedes especificar un ID de sesión concreto con `codex exec resume <SESSION_ID>`.

## Se requiere un repositorio de Git

Codex exige que los comandos se ejecuten dentro de un repositorio de Git para evitar cambios destructivos. Omite esta comprobación con `codex exec --skip-git-repo-check` si tienes la certeza de que el entorno es seguro.

## Patrones comunes de automatización

### Ejemplo: corregir automáticamente errores de CI en GitHub Actions

En los flujos de trabajo de GitHub Actions, usa [`openai/codex-action`](https://github.com/openai/codex-action) en lugar de instalar Codex y pasar la clave de API a un paso de shell. La acción inicia un proxy seguro para la clave de API de OpenAI.

Puedes usar Codex para proponer correcciones automáticamente cuando falla un flujo de trabajo de CI. El patrón es el siguiente:

1. Activa un flujo de trabajo de seguimiento cuando tu flujo de trabajo principal de CI finalice con un error.
2. Haz checkout del commit con errores usando únicamente permisos de lectura del repositorio.
3. Ejecuta los comandos de configuración antes de Codex, sin exponer tu clave de API de OpenAI a esos pasos.
4. Ejecuta la GitHub Action de Codex.
5. Guarda los cambios locales de Codex como un artefacto de parche.
6. En un trabajo independiente, aplica el parche y abre un Pull Request.

El trabajo de Codex que aparece a continuación solo tiene `contents: read`. Una vez que Codex termina, el trabajo solo serializa el diff como artefacto. El trabajo `open_pr` recibe permisos de escritura en el repositorio, pero no recibe `OPENAI_API_KEY`.

El ejemplo presupone un proyecto de Node.js. Ajusta los comandos de configuración y pruebas según tu stack tecnológico.

Para obtener una lista de verificación de seguridad más detallada, consulta la [guía de seguridad de Codex GitHub Action](https://github.com/openai/codex-action/blob/main/docs/security.md).

```yaml
name: Codex auto-fix on CI failure

on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

jobs:
  generate_fix:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      has_patch: ${{ steps.diff.outputs.has_patch }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0
          persist-credentials: false

      - uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install dependencies
        run: |
          if [ -f package-lock.json ]; then npm ci; fi

      - name: Run Codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt: |
            The CI workflow "${{ github.event.workflow_run.name }}" failed for commit
            ${{ github.event.workflow_run.head_sha }}.

            Run `npm test --silent` to reproduce the failure. Identify the minimal
            change needed to make the tests pass, implement only that change, and
            run `npm test --silent` again.

            Do not refactor unrelated files.

      - name: Create patch artifact
        id: diff
        run: |
          git add -N .
          git diff --binary HEAD > codex.patch
          if [ -s codex.patch ]; then
            echo "has_patch=true" >> "$GITHUB_OUTPUT"
          else
            echo "has_patch=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload patch artifact
        if: steps.diff.outputs.has_patch == 'true'
        uses: actions/upload-artifact@v4
        with:
          name: codex-fix-patch
          path: codex.patch
          if-no-files-found: error

  open_pr:
    runs-on: ubuntu-latest
    needs: generate_fix
    if: needs.generate_fix.outputs.has_patch == 'true'
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0

      - uses: actions/download-artifact@v4
        with:
          name: codex-fix-patch

      - name: Apply Codex patch
        run: git apply --index codex.patch

      - name: Open pull request
        env:
          GH_TOKEN: ${{ github.token }}
          FAILED_HEAD_BRANCH: ${{ github.event.workflow_run.head_branch }}
          FAILED_HEAD_SHA: ${{ github.event.workflow_run.head_sha }}
          RUN_ID: ${{ github.event.workflow_run.run_id }}
        run: |
          branch="codex/auto-fix-$RUN_ID"

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git switch -c "$branch"
          git commit -m "Auto-fix failing CI via Codex"
          git push origin "$branch"

          {
            echo "Codex generated this patch after CI failed for \`$FAILED_HEAD_SHA\`."
            echo
            echo "Review the changes before merging."
          } > pr-body.md

          gh pr create \
            --base "$FAILED_HEAD_BRANCH" \
            --head "$branch" \
            --title "Auto-fix failing CI via Codex" \
            --body-file pr-body.md

## Canalización avanzada de stdin

Cuando otro comando genere la entrada para Codex, elige el patrón de stdin según el origen de la instrucción. Usa el patrón de prompt más stdin cuando ya conozcas la instrucción y quieras enviar la salida canalizada como contexto. Usa `codex exec -` cuando stdin deba ser el prompt completo.

### Usar el patrón de prompt más stdin

El patrón de prompt más stdin resulta útil cuando otro comando ya genera los datos que quieres que Codex examine. En este modo, tú escribes la instrucción y canalizas la salida como contexto, por lo que encaja de forma natural en los flujos de trabajo de CLI basados en salidas de comandos, registros y datos generados.

```bash
npm test 2>&1 \
  | codex exec "summarize the failing tests and propose the smallest likely fix" \
  | tee test-summary.md

### Resumir registros

```bash
tail -n 200 app.log \
  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
  > log-triage.md

### Inspeccionar problemas de TLS o HTTP

```bash
curl -vv https://api.example.com/health 2>&1 \
  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
  > tls-debug.md

### Preparar una actualización lista para Slack

```bash
gh run view 123456 --log \
  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
  | pbcopy

### Redactar un comentario para un Pull Request a partir de registros de CI

```bash
gh run view 123456 --log \
  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
  | gh pr comment 789 --body-file -

### Usar `codex exec -` cuando stdin sea el prompt

Si omites el argumento del prompt, Codex lee el prompt desde stdin. Usa `codex exec -` cuando quieras forzar ese comportamiento de forma explícita.

El valor centinela `-` resulta útil cuando otro comando o script genera dinámicamente el prompt completo. Es una buena opción si almacenas prompts en archivos, los construyes con scripts de shell o combinas la salida de comandos en tiempo real con instrucciones antes de enviar el prompt completo a Codex.

```bash
cat prompt.txt | codex exec -

```bash
printf "Summarize this error log in 3 bullets:\n\n%s\n" "$(tail -n 200 app.log)" \
  | codex exec -

```bash
generate_prompt.sh | codex exec - --json > result.jsonl
