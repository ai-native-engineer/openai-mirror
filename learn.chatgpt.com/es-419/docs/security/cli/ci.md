<!-- source: https://learn.chatgpt.com/es-419/docs/security/cli/ci -->

Ejecuta la CLI de Codex Security en CI para revisar los cambios exactos de un Pull Request
o una solicitud de fusión, conservar los hallazgos y la cobertura y, si lo deseas, hacer que la verificación falle ante
un nivel de gravedad determinado. Comienza con resultados informativos, revisa la calidad y el
tiempo de ejecución del análisis y luego agrega una política de gravedad adecuada para tu repositorio.

  Instala el paquete público `@openai/codex-security`. Para ejecutar análisis, aún
  se requiere acceso a Codex Security.

Esta guía incluye ejemplos para GitHub Actions y GitLab CI/CD. Los mismos comandos de análisis
y exportación funcionan en otros sistemas de CI.

## Preparar el flujo de trabajo

Guarda una clave de API de OpenAI en el almacén de secretos de tu proveedor de CI con el nombre
`CODEX_SECURITY_API_KEY`.

Asigna este secreto directamente a la variable de entorno `OPENAI_API_KEY`
del paso de análisis. Limita el alcance de la credencial al proceso de análisis y usa
`--auth api-key` para seleccionarla explícitamente.

Ejecuta el flujo de trabajo solo para repositorios y Pull Requests en los que confíes. Los análisis usan
los permisos locales del ejecutor y no se detienen para solicitar aprobación. Los procesos de análisis
pueden heredar el entorno del job, así que mantén fuera de él los tokens y las credenciales de la
nube que no estén relacionados con el análisis.

El ejecutor necesita:

- Node.js 22 (22.13.0 o posterior), 24 o 26.
- Python 3.10 o posterior.
- El paquete publicado `@openai/codex-security`, instalado fuera del checkout del
  repositorio.
- El historial de las revisiones de origen y base del Pull Request o de la solicitud de fusión para que Git pueda calcular
la base de fusión.

## Agregar el flujo de trabajo de GitHub Actions

En repositorios privados o internos, activa
[GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)
antes de cargar SARIF.

Crea `.github/workflows/codex-security.yml`. Antes de hacer checkout del
Pull Request, instala `@openai/codex-security` en
`$RUNNER_TEMP/codex-security` para que el ejecutable de confianza esté disponible en
`$RUNNER_TEMP/codex-security/node_modules/.bin/codex-security`:

```yaml
name: Codex Security scan

on:
  pull_request:

jobs:
  codex-security:
    if: github.event.pull_request.head.repo.full_name == github.repository && github.actor != 'dependabot[bot]'
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    steps:
      - name: Set up Node.js
        uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7
        with:
          node-version: "26"

      - name: Set up Python
        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7
        with:
          python-version: "3.14"

      - name: Install Codex Security
        run: |
          set -euo pipefail
          npm install \
            --prefix "$RUNNER_TEMP/codex-security" \
            --ignore-scripts \
            --no-audit \
            --no-fund \
            @openai/codex-security

      - name: Verify Codex Security
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
        run: |
          set -euo pipefail
          test -x "$CODEX_SECURITY_BIN"
          "$CODEX_SECURITY_BIN" --version

      - name: Check out the pull request
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Scan the pull request
        env:
          OPENAI_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          CODEX_SECURITY_STATE_DIR: ${{ runner.temp }}/codex-security-state
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
        run: |
          set -euo pipefail
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          "$CODEX_SECURITY_BIN" scan . \
            --diff "$BASE_REVISION" \
            --head "$HEAD_SHA" \
            --auth api-key \
            --output-dir "$SCAN_DIR" \
            --json > "$RUNNER_TEMP/codex-security.json"

      - name: Export SARIF
        id: export-sarif
        if: always()
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
          SARIF_FILE: ${{ runner.temp }}/codex-security.sarif
        run: |
          set -euo pipefail
          if test -f "$SCAN_DIR/scan-manifest.json"; then
            "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
              --export-format sarif \
              --source-root "$GITHUB_WORKSPACE" \
              --output "$SARIF_FILE"
            echo "available=true" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload SARIF
        if: always() && steps.export-sarif.outputs.available == 'true'
        uses: github/codeql-action/upload-sarif@e4fba868fa4b1b91e1fdab776edc8cfbe6e9fb81 # v4
        with:
          sarif_file: ${{ runner.temp }}/codex-security.sarif
          ref: refs/pull/${{ github.event.pull_request.number }}/head
          sha: ${{ github.event.pull_request.head.sha }}
          category: codex-security

      - name: Preserve scan results
        if: always()
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7
        with:
          name: codex-security-results
          path: |
            ${{ runner.temp }}/codex-security-results
            ${{ runner.temp }}/codex-security.json
          if-no-files-found: warn
          retention-days: 7

El flujo de trabajo hace checkout de la revisión de origen del Pull Request, calcula su base de fusión y
analiza los cambios confirmados entre esas revisiones. El historial completo permite delimitar con exactitud
qué se analiza. `persist-credentials: false` evita que el token del repositorio se incluya en
la configuración de Git de la copia obtenida. Instalar la CLI antes del checkout y
ejecutarla mediante su ruta absoluta impide que los ejecutables controlados por el repositorio accedan a
la credencial del análisis. `--auth api-key` selecciona explícitamente la clave de API con alcance limitado.
El análisis guarda su historial en un directorio de estado con permisos de escritura fuera del
repositorio.

`--json` escribe un único documento JSON completo en stdout, por lo que el flujo de trabajo puede guardarlo
directamente. El progreso, los resúmenes de finalización y los errores siguen enviándose a stderr. Esto
difiere de `codex exec --json`, que emite un flujo de eventos JSON Lines.

El paso de exportación lee un análisis completado y sellado, y genera SARIF. No modifica el
entorno de ejecución ni las credenciales de Codex. Los artefactos del análisis pueden contener fragmentos de
código fuente vulnerable, evidencia y detalles de corrección. Elige controles de acceso y un
periodo de retención breve que sean adecuados para tu repositorio.

## Agregar el pipeline de GitLab CI/CD

Para un flujo de trabajo de producción con análisis protegidos de la rama predeterminada, análisis profundos
programados de activación opcional, un control independiente basado en políticas SARIF y, opcionalmente,
solicitudes de fusión verificadas en borrador, consulta [Ejecutar Codex Security en GitLab
CI/CD](/es-419/codex/security/cli/ci/gitlab).

GitLab puede importar
[informes SARIF 2.1.0](https://docs.gitlab.com/ci/yaml/artifacts_reports/#artifactsreportssarif)
en GitLab Ultimate 19.2 o posterior. Agrega la variable de CI/CD enmascarada y oculta
`CODEX_SECURITY_API_KEY` antes de ejecutar el pipeline.

El siguiente ejemplo mínimo agrega un job `security` dedicado únicamente al análisis al archivo
`.gitlab-ci.yml` de la raíz. Conserva las etapas y los jobs que ya existan en el archivo. De forma predeterminada, analiza
los cambios de las solicitudes de fusión. Configura `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH`
con el valor `"true"` para analizar también toda la rama predeterminada:

```yaml
variables:
  CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH: "false"

stages:
  - test
  - security

codex-security:
  stage: security
  image: node:26-bookworm-slim
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "diff"
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH && $CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH == "true"'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "full"
  variables:
    GIT_DEPTH: "0"
    CODEX_SECURITY_CLI_DIR: "/tmp/codex-security-cli"
  before_script:
    - |
      set -eu
      apt-get update -qq
      apt-get install -y -qq --no-install-recommends \
        ca-certificates \
        git \
        python3 \
        ripgrep
      npm install \
        --prefix "$CODEX_SECURITY_CLI_DIR" \
        --ignore-scripts \
        --no-audit \
        --no-fund \
        @openai/codex-security@0.1.20

      test -x "$CODEX_SECURITY_BIN"
      "$CODEX_SECURITY_BIN" --version
  script:
    - |
      set -eu
      if test -z "${CODEX_SECURITY_API_KEY:-}"; then
        echo "Set the CODEX_SECURITY_API_KEY CI/CD variable." >&2
        exit 2
      fi

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      case "${CODEX_SECURITY_SCAN_SCOPE:-}" in
        diff)
          BASE_SHA="$CI_MERGE_REQUEST_DIFF_BASE_SHA"
          HEAD_SHA="$CI_COMMIT_SHA"
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          set -- --diff "$BASE_REVISION" --head "$HEAD_SHA"
          echo "Scanning committed changes from $BASE_REVISION to $HEAD_SHA."
          ;;
        full)
          set -- --mode standard
          echo "Scanning the complete default branch at $CI_COMMIT_SHA."
          ;;
        *)
          echo "Unsupported Codex Security scan scope: ${CODEX_SECURITY_SCAN_SCOPE:-unset}" >&2
          exit 2
          ;;
      esac

      SCAN_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      JSON_FILE="/tmp/codex-security-$CI_JOB_ID.json"
      SARIF_FILE="/tmp/codex-security-$CI_JOB_ID.sarif"

      install -d -m 700 "$CODEX_SECURITY_STATE_DIR" "$SCAN_DIR"

      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          "$@" \
          --auth api-key \
          --output-dir "$SCAN_DIR" \
          --json > "$JSON_FILE"
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      install -d -m 700 codex-security-artifacts/results
      cp -R "$SCAN_DIR"/. codex-security-artifacts/results/
      if test -s "$JSON_FILE"; then
        cp "$JSON_FILE" codex-security-artifacts/codex-security.json
      fi
      printf '%s\n' "$scan_exit" > codex-security-artifacts/scan-exit-code.txt

      export_exit=0
      if test -f "$SCAN_DIR/scan-manifest.json"; then
        set +e
        "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
          --export-format sarif \
          --source-root "$CI_PROJECT_DIR" \
          --output "$SARIF_FILE"
        export_exit="$?"
        set -e
        if test -s "$SARIF_FILE"; then
          cp "$SARIF_FILE" codex-security-artifacts/codex-security.sarif
        fi
      fi

      if test "$scan_exit" -ne 0; then
        exit "$scan_exit"
      fi
      exit "$export_exit"
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/codex-security.sarif

De forma predeterminada, el job solo se ejecuta para solicitudes de fusión provenientes de ramas del mismo
proyecto, por lo que los pipelines de forks no reciben la credencial del análisis. Configura
`CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` con el valor `"true"` a nivel de grupo, proyecto o
pipeline para ejecutar también un análisis completo estándar en la rama predeterminada. Los análisis
completos tardan más y cuestan más que los análisis de diferencias.

`GIT_DEPTH: "0"` proporciona el historial necesario para calcular la base de fusión a partir de
`CI_MERGE_REQUEST_DIFF_BASE_SHA` y `CI_COMMIT_SHA` en los análisis de solicitudes de fusión.

El job instala la CLI en `/tmp`, la ejecuta mediante su ruta absoluta y expone la
clave de API únicamente al proceso de análisis. `artifacts: when: always` conserva el informe SARIF
cuando falla el análisis, mientras que `artifacts:access: maintainer` limita el acceso
a los resultados detallados del análisis.

Los cambios en `.gitlab-ci.yml` pueden exponer variables de CI/CD, así que revisa los cambios del pipeline
antes de ejecutar el job. Si
[proteges `CODEX_SECURITY_API_KEY`](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners),
GitLab solo la pone a disposición de las solicitudes de fusión del mismo proyecto entre
ramas protegidas y solo cuando el usuario puede acceder a la rama de destino.

La guía específica de GitLab amplía este job básico para obtener el flujo de trabajo de producción
cuyo enlace aparece al inicio de esta sección.

## Elegir una política de gravedad

Ambos ejemplos solo generan informes porque omiten `--fail-on-severity`. Cuando
quieras que los hallazgos afecten la verificación, agrega un umbral al comando de
análisis:

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --fail-on-severity high

Los umbrales admitidos son `critical`, `high`, `medium` y `low`. Un
umbral incluye los hallazgos del análisis actual con esa gravedad o una superior.
Los hallazgos anteriores que siguen abiertos y aparecen en el resumen del repositorio no afectan la política.

El paso de análisis usa estos códigos de salida:

| Código de salida  | Significado                                                                                 |
| ----- | --------------------------------------------------------------------------------------- |
| `0`   | El análisis finalizó con cobertura completa y se cumplieron todas las políticas configuradas.            |
| `1`   | El análisis completado contiene un hallazgo con una gravedad igual o superior al umbral.                        |
| `2`   | La CLI detectó un error de entrada o de ejecución, o el análisis completado tiene cobertura incompleta. |
| `130` | Ctrl-C interrumpió el análisis.                                                            |
| `143` | SIGTERM finalizó el análisis.                                                            |

Un análisis con cobertura `partial` o `unknown` devuelve `2`, incluso sin una política de
gravedad. La CLI aun así guarda los hallazgos y la cobertura disponibles. Revisa en
`coverage.json` las áreas cuyo análisis se pospuso antes de considerar concluyente la verificación.

## Reintentar con un directorio de resultados existente

Usa un directorio nuevo en el ejecutor para cada job de CI. En un ejecutor persistente o autohospedado,
conserva un resultado anterior con `--archive-existing`:

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --archive-existing

El comando archiva los resultados anteriores y comienza con un directorio de análisis vacío.

## Solucionar problemas de un análisis de CI

- **Referencia de Git desconocida o diferencia inesperada:** recupera el historial de las revisiones base y de origen,
  calcula la base de fusión y pasa ambas revisiones de forma explícita.
- **Directorio de salida protegido o no vacío:** elige un directorio privado
  fuera del Worktree de Git que lo contiene. Usa `--archive-existing` si el
  directorio ya contiene resultados.
- **Faltan credenciales:** confirma que `CODEX_SECURITY_API_KEY` esté disponible para
  el flujo de trabajo o pipeline de confianza y se asigne directamente a la variable de entorno
`OPENAI_API_KEY` del proceso de análisis.
- **Error en el historial del análisis:** asigna a `CODEX_SECURITY_STATE_DIR` un directorio con permisos de escritura
  fuera del repositorio.
- **Error de configuración de Python:** confirma que el ejecutor use Python 3.10 o posterior.
- **Cobertura incompleta:** revisa `coverage.json`, incluidas las superficies cuyo análisis se pospuso
  y las preguntas pendientes, y luego vuelve a ejecutar el análisis con un objetivo o entorno adecuados.
- **Error al exportar SARIF:** confirma que el análisis haya finalizado y que el directorio completo
  del análisis esté disponible. La exportación valida los artefactos sellados antes de generar
  SARIF.
- **Error al cargar SARIF:** para GitHub Actions, confirma que tu organización
  haya activado GitHub Code Security para el repositorio y que el flujo de trabajo conceda
`actions: read`, `contents: read` y `security-events: write`. Para GitLab
  CI/CD, confirma que el proyecto use GitLab Ultimate 19.2 o posterior y que
  el job cargue un archivo SARIF 2.1.0 mediante `artifacts:reports:sarif`.

Para conocer todos los comandos, opciones, artefactos y campos de salida, consulta la [referencia
de la CLI](/es-419/codex/security/cli/reference). Para una revisión interactiva de CI
basada en complementos, consulta [Revisar la seguridad de los cambios en el código](/es-419/codex/security/plugin/code-changes#automate-reviews-in-cicd).
