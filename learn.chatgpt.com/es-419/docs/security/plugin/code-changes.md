<!-- source: https://learn.chatgpt.com/es-419/docs/security/plugin/code-changes -->

Ejecuta una revisión de seguridad de los cambios para detectar regresiones en un único conjunto de cambios basado en Git.
Codex revisa cada archivo modificado que se asemeje a código fuente y el código que lo respalda directamente.
La revisión no se amplía hasta convertirse en una auditoría completa del repositorio.

Para analizar un repositorio completo en lugar de un cambio específico, consulta [Ejecutar un análisis de
seguridad](/es-419/codex/security/plugin/scans).

## Ejecutar una revisión manual

En la App de escritorio, abre **Seguridad**, selecciona **Análisis** y, luego, **+ Análisis**.
Elige el repositorio y selecciona **Cambios**. Revisa cambios sin confirmar,
un solo commit o una revisión base y otra de cabecera. El **Análisis profundo** no está disponible para un
análisis de cambios.

También puedes pedirle a Codex que revise los cambios sin confirmar en una conversación:

```text
Use $codex-security:security-diff-scan to review my current uncommitted changes for security regressions.

Para un rango de commits o ramas, especifica ambas revisiones cuando sea necesario:

```text
Use $codex-security:security-diff-scan to review the changes from origin/main to HEAD for security regressions. Focus on authentication, authorization, input handling, filesystem access, network requests, and secrets.

También puedes indicar un pull request cuando sus revisiones base y de cabecera estén disponibles
en el checkout local.

## Confirmar el cambio en la configuración

1. Selecciona **Cambios**.
2. Confirma el repositorio del checkout, la rama actual y el commit más reciente.
3. En **Cambios para revisar**, elige:
   - `Uncommitted changes` para el árbol de trabajo actual.
   - El commit más reciente para una revisión de un solo commit.
   - Una revisión base y otra de cabecera para el rango de una rama o un pull request.
4. Confirma que el resumen describa el cambio que querías revisar.
5. Selecciona **Iniciar análisis**.

Codex no hace checkout de otra rama ni cambia el árbol de trabajo seleccionado. Si
una revisión solicitada no está disponible localmente, obtenla antes de la revisión o
proporciona revisiones base y de cabecera disponibles localmente.

## Tomar medidas sobre los hallazgos

Después de revisar los resultados, [corrige y verifica un hallazgo
aceptado](/es-419/codex/security/plugin/fix-findings) o [exporta y da seguimiento a los
hallazgos](/es-419/codex/security/plugin/export-findings).

## Automatizar las revisiones en CI/CD

Si tienes acceso a la CLI independiente en versión beta, consulta [Ejecutar Codex Security en
CI](/es-419/codex/security/cli/ci) para obtener JSON estructurado, una política de severidad y la carga
de SARIF. Continúa con esta sección para invocar la habilidad del plugin instalado
mediante `codex exec`.

Ejecuta `$codex-security:security-diff-scan` en CI cuando el ejecutor pueda invocar
Codex CLI sin interacción. Primero, instala la CLI sin exponer la
credencial del análisis:

```bash
npm install --global @openai/codex

Instala el Plugin de Codex Security en la CLI:

```bash
codex plugin add codex-security@openai-curated

El comando de instalación usa el Marketplace público de plugins de Codex CLI. Consulta el
[registro de cambios del plugin](/es-419/codex/security/plugin/changelog) antes de depender de una
versión o función específica del plugin en CI.

A continuación, proporciona una clave de API de OpenAI del almacén de secretos de CI como
`CODEX_SECURITY_API_KEY`. Expón la credencial únicamente durante el análisis:

```bash
CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
  --sandbox workspace-write \
  "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

El sandbox con permisos de escritura permite que el análisis cree artefactos temporales. El prompt
sigue exigiendo que Codex deje sin cambios el checkout del código fuente.

El análisis guarda sus resultados en
`$TMPDIR/codex-security-scans/<repository>/<scan-id>/`:

| Archivo                 | Contenido                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `report.md`          | Punto de entrada principal en formato legible para todo el directorio del análisis.                                                                                              |
| `findings/<slug>/`   | Informes detallados de vulnerabilidades y archivos de prueba de concepto de respaldo, cuando se soliciten.                                                                     |
| `hardening/`         | Orientación para el fortalecimiento estructural y propuestas de respaldo, cuando se soliciten.                                                                                   |
| `findings.json`      | Hallazgos con identificadores estables, severidad, confianza, ubicaciones en el código fuente y medidas de corrección. Úsalos en flujos de trabajo internos de seguridad aprobados o herramientas posteriores. |
| `scan-manifest.json` | Recibo sellado del análisis con el objetivo revisado, las revisiones y los hashes de los artefactos.                                                                             |
| `coverage.json`      | Superficies revisadas y pospuestas, exclusiones y exhaustividad de la cobertura.                                                                                    |

El [esquema de `findings.json`](https://github.com/openai/plugins/blob/main/plugins/codex-security/schemas/findings.schema.json)
define la estructura completa. El esquema incluye estos campos:

| Campo                     | Tipo   | Descripción                                                            |
| ------------------------- | ------ | ---------------------------------------------------------------------- |
| `documentType`            | Cadena | Identifica el documento como `codex-security.findings`.                  |
| `schemaVersion`           | Cadena | Identifica la versión del esquema de hallazgos.                                |
| `scanId`                  | Cadena | Identifica el análisis que generó los hallazgos.                        |
| `findings`                | Arreglo  | Contiene cero o más objetos de hallazgo.                                 |
| `findings[].findingId`    | Cadena | Identificador estable del hallazgo derivado de su huella digital.        |
| `findings[].occurrenceId` | Cadena | Identifica esta aparición del hallazgo en un análisis específico.          |
| `findings[].ruleId`       | Cadena | Identifica la familia de la vulnerabilidad.                                   |
| `findings[].identity`     | Objeto | Contiene el ancla semántica y un identificador opcional de instancia hermana. |
| `findings[].fingerprints` | Objeto | Contiene el algoritmo de huella digital y la huella digital principal.            |
| `findings[].title`        | Cadena | Proporciona el título breve del hallazgo.                                      |
| `findings[].summary`      | Cadena | Resume la vulnerabilidad y su impacto.                           |
| `findings[].severity`     | Objeto | Contiene el nivel de gravedad y los detalles opcionales de la puntuación.              |
| `findings[].confidence`   | Objeto | Contiene el nivel de confianza y su justificación.                           |
| `findings[].taxonomy`     | Objeto | Contiene la categoría de vulnerabilidad y los identificadores CWE.               |
| `findings[].locations`    | Arreglo  | Enumera los archivos afectados, los números de línea y el rol de cada ubicación.                |
| `findings[].remediation`  | Cadena | Describe la corrección recomendada.                                         |
| `findings[].provenance`   | Objeto | Identifica el origen del hallazgo.                                  |

Por ejemplo, este comando imprime una fila separada por tabulaciones para cada hallazgo:

```bash
jq -r '
  .findings[] |
  [.findingId, .severity.level, .confidence.level, .locations[0].path, .locations[0].startLine, .title] |
  @tsv
' findings.json

Estos ejemplos suponen un runner de Linux de confianza con Node.js y `npm`, Git, Python
3, `jq` y las herramientas de línea de comandos del proveedor. El prefijo global de paquetes de `npm`
debe permitir la escritura.

Elige el ejemplo correspondiente a tu proveedor de CI:

Los resultados del análisis pueden incluir detalles confidenciales sobre vulnerabilidades. Mantén los artefactos
en privado y publica los hallazgos solo después de revisar los destinatarios, el contenido y
las aprobaciones requeridas.

  <div slot="github">

```yaml
name: Codex Security review

on:
  pull_request:

jobs:
  security-review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Install Codex Security
        env:
          CODEX_HOME: ${{ runner.temp }}/codex-home
        run: |
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated

      - name: Review code changes
        env:
          CODEX_SECURITY_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_HOME: ${{ runner.temp }}/codex-home
          TMPDIR: ${{ runner.temp }}/codex-security
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_REVISION: ${{ github.event.pull_request.head.sha }}
        run: |
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_REVISION")"
          CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
            --sandbox workspace-write \
            "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: codex-security-review
          path: ${{ runner.temp }}/codex-security/codex-security-scans

  </div>

  <div slot="gitlab">

Crea una variable de CI/CD enmascarada llamada `CODEX_SECURITY_API_KEY` y revisa los artefactos
del análisis en privado antes de compartir los hallazgos.

```yaml
codex-security-review:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
  variables:
    GIT_DEPTH: "0"
  script:
    - |
      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
      CODEX_API_KEY="$codex_security_api_key" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
  after_script:
    - |
      unset CODEX_SECURITY_API_KEY
      scan_root="/tmp/codex-security-$CI_JOB_ID/codex-security-scans"
      if [ -d "$scan_root" ]; then
        tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
      fi
  artifacts:
    when: always
    paths:
      - codex-security-artifacts.tar.gz

  </div>

  <div slot="azure">

```yaml
trigger: none

pool:
  vmImage: ubuntu-latest

steps:
  - checkout: self
    fetchDepth: 0

  - bash: |
      set -euo pipefail

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
    displayName: Install Codex Security

  - bash: |
      set -euo pipefail

      CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
    displayName: Review code changes
    condition: and(succeeded(), ne(variables['System.PullRequest.IsFork'], 'True'))
    env:
      CODEX_SECURITY_API_KEY: $(CODEX_SECURITY_API_KEY)

  - publish: $(Agent.TempDirectory)/codex-security/codex-security-scans
    artifact: codex-security-review
    condition: always()

Para Azure Repos, configura una directiva de rama de **Validación de compilación** para ejecutar la
canalización en los pull requests.

  </div>

  <div slot="jenkins">

```groovy
pipeline {
  agent { label 'linux' }
  stages {
    stage('Codex Security review') {
      when {
        allOf {
          changeRequest()
          expression { !env.CHANGE_FORK?.trim() }
        }
      }
      steps {
        sh '''#!/usr/bin/env bash
          set -euo pipefail

          mkdir -p "$TMPDIR"
          git fetch --no-tags origin "$CHANGE_TARGET"
          target="$(git rev-parse FETCH_HEAD)"
          git fetch --no-tags origin "$CHANGE_BRANCH"
          git rev-parse FETCH_HEAD > "$TMPDIR/head"
          git merge-base "$target" "$(cat "$TMPDIR/head")" > "$TMPDIR/base"
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated
        '''
        withCredentials([string(credentialsId: 'codex-security-api-key', variable: 'CODEX_SECURITY_API_KEY')]) {
          sh '''#!/usr/bin/env bash
            set +x
            set -euo pipefail

            CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
              --sandbox workspace-write \
              "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
          '''
        }
      }
      post {
        always {
          sh '''#!/usr/bin/env bash
            set -euo pipefail
            scan_root="/tmp/codex-security-$BUILD_TAG/codex-security-scans"
            if [ -d "$scan_root" ]; then
              tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
            fi
          '''
          archiveArtifacts artifacts: 'codex-security-artifacts.tar.gz', allowEmptyArchive: true
        }
      }
    }
  }
}

  </div>

Los ejemplos omiten los pull requests provenientes de forks. Ejecuta trabajos con credenciales solo desde una
definición de canalización protegida y solo para colaboradores a quienes se les confíe la credencial
del análisis. Archiva `codex-security-scans` para conservar juntos los hallazgos estructurados,
el archivo de manifiesto, la cobertura y `report.md`, junto con cualquier resultado solicitado de
`findings/` o `hardening/`. Comienza con resultados informativos y revisa
la cobertura y el tiempo de ejecución antes de convertir el trabajo en una verificación obligatoria.

Para el manejo de claves de API y los controles del sandbox, consulta [Modo no
interactivo](/es-419/codex/non-interactive-mode). Si tu organización permite usar [Codex
GitHub Action](/es-419/codex/github-action), esta puede instalar la CLI durante la ejecución, pero
aun así debes instalar primero el complemento y configurar la entrada `codex-home`
de la acción para que apunte al mismo `CODEX_HOME`.
