<!-- source: https://learn.chatgpt.com/es-419/docs/security/cli/ci/gitlab -->

Ejecuta Codex Security en GitLab CI/CD para analizar cambios registrados en commits y ramas
protegidas, publicar hallazgos en GitLab Security y, de forma opcional, proponer correcciones
verificadas en borradores de solicitudes de fusión.

El flujo de trabajo mantiene las credenciales de análisis separadas del acceso de escritura al repositorio.
Los cambios generados siempre requieren revisión humana antes de fusionarse.

Empieza solo con informes de análisis. Habilita la remediación únicamente después de comprobar el
runner, los hallazgos y los límites de acceso de las credenciales de tu proyecto.

## Antes de empezar

Necesitas:

- Un proyecto de GitLab con un runner de confianza compatible con el espacio de nombres
de usuario del sandbox de Codex.
- El rol Maintainer u Owner en el proyecto de GitLab para poder configurar
[las variables de CI/CD del proyecto](https://docs.gitlab.com/ci/variables/) y los recursos
  protegidos.
- Una clave de API de OpenAI con acceso a Codex Security. Las organizaciones que usan claves de API de la plataforma
  pueden [solicitar Trusted Access for
  Cyber](https://openai.com/form/enterprise-trusted-access-for-cyber/).
  Las personas que usan la autenticación de ChatGPT pueden usar el [flujo personal
  de Trusted Access](https://chatgpt.com/cyber). Algunas cuentas o repositorios requieren este
  acceso para los análisis del repositorio completo.
- GitLab Ultimate 19.2 o posterior para la [ingesta de
  SARIF 2.1.0](https://docs.gitlab.com/user/application_security/detect/sarif/).
- El historial completo de Git para que los trabajos de las solicitudes de fusión puedan calcular la base de fusión.

La imagen del pipeline instala Node.js 26, Python 3, Git, `rg` y la versión fijada de la
CLI de Codex Security. La remediación automatizada también requiere una prueba de
regresión existente y un runner que pueda ejecutar comandos controlados por el repositorio
sin credenciales protegidas.

## Empieza con un pipeline solo de análisis

Crea una variable de CI/CD de GitLab enmascarada, oculta y protegida llamada
`CODEX_SECURITY_API_KEY`. Usa una clave de API de la plataforma de OpenAI con acceso a Codex Security
y establece su ámbito de entorno en `codex-security/openai`. Consulta
[las variables de CI/CD con ámbito de entorno](https://docs.gitlab.com/ci/environments/#limit-the-environment-scope-of-a-cicd-variable).

Primero agrega este pipeline mínimo a un proyecto de prueba. Analiza los cambios registrados en commits
en las solicitudes de fusión protegidas que cumplen los requisitos, publica SARIF desde un trabajo de informes
completado correctamente y restablece el resultado del analizador en un control independiente:

```yaml
stages:
  - security_scan
  - security_gate

.codex-security-merge-request:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID && $CI_MERGE_REQUEST_SOURCE_BRANCH_PROTECTED == "true" && $CI_MERGE_REQUEST_TARGET_BRANCH_PROTECTED == "true"'

codex-security:
  extends: .codex-security-merge-request
  stage: security_scan
  image: node:26-bookworm-slim
  environment:
    name: codex-security/openai
    action: access
  variables:
    GIT_DEPTH: "0"
  before_script:
    - npm install --prefix /tmp/codex-security-cli --ignore-scripts --no-audit --no-fund @openai/codex-security@0.1.20
  script:
    - |
      set -eu
      test -n "${CODEX_SECURITY_API_KEY:-}"

      CODEX_SECURITY_BIN="/tmp/codex-security-cli/node_modules/.bin/codex-security"
      RESULTS_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      ARTIFACT_DIR="codex-security-artifacts"
      BASE_REVISION="$(git merge-base \
        "$CI_MERGE_REQUEST_DIFF_BASE_SHA" "$CI_COMMIT_SHA")"
      install -d -m 700 "$RESULTS_DIR" "$ARTIFACT_DIR/results"

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY
      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          --diff "$BASE_REVISION" \
          --head "$CI_COMMIT_SHA" \
          --auth api-key \
          --output-dir "$RESULTS_DIR" \
          --json
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      case "$scan_exit" in
        0|1|2) ;;
        *) exit "$scan_exit" ;;
      esac

      "$CODEX_SECURITY_BIN" export "$RESULTS_DIR" \
        --export-format sarif \
        --source-root "$CI_PROJECT_DIR" \
        --output "$ARTIFACT_DIR/results.sarif"
      test -s "$ARTIFACT_DIR/results.sarif"
      cp -R "$RESULTS_DIR"/. "$ARTIFACT_DIR/results/"
      printf '%s\n' "$scan_exit" > "$ARTIFACT_DIR/scan-exit-code.txt"
      exit 0
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/results.sarif

codex-security-gate:
  extends: .codex-security-merge-request
  stage: security_gate
  image: alpine:3.20
  needs:
    - job: codex-security
      artifacts: true
  script:
    - exit "$(cat codex-security-artifacts/scan-exit-code.txt)"

  

Revisa cada cambio en `.gitlab-ci.yml` antes de ejecutar un trabajo que tenga acceso a secretos.
El ejemplo mínimo omite intencionalmente los análisis completos y la remediación.

## Adopta el pipeline para producción

1. [Descarga el pipeline completo de GitLab](/codex/security/cli/ci/gitlab.yml)
   y guárdalo como `.gitlab-ci.yml` en la raíz del repositorio. Si tu repositorio
   ya tiene un pipeline, integra las etapas, las plantillas ocultas y los
   trabajos del ejemplo en el archivo existente.
2. Conserva las etapas existentes de compilación, pruebas y despliegue. Si el proyecto usa
`workflow: rules`, confirma que permita los eventos del pipeline que quieres
   analizar.

El ejemplo agrega las etapas `security_scan`, `security_remediation`, `security_publish`
y `security_gate`. Para generar solo informes de análisis, se requiere únicamente
`CODEX_SECURITY_API_KEY`.

El trabajo de análisis se ejecuta de forma predeterminada solo para solicitudes de fusión del mismo proyecto entre
ramas protegidas. Establece `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH=true` para analizar
los envíos de cambios a la rama predeterminada protegida y los pipelines manuales. Establece
`CODEX_SECURITY_SCHEDULED_DEEP_SCAN=true` y configura presupuestos explícitos de tiempo y costo
para habilitar análisis profundos programados en la rama predeterminada protegida.

Un pipeline de solicitud de fusión puede acceder a variables y runners protegidos solo cuando:

- Proteges las ramas de origen y destino en el mismo proyecto.
- El proyecto [permite que los pipelines de solicitudes de fusión accedan a variables y
  runners protegidos](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners).
- El usuario que inicia el pipeline puede enviar cambios a la rama de destino o fusionarlos en ella.

Los pipelines de forks y las solicitudes de fusión sin protección no reciben la credencial
de análisis. Revisa cada cambio en `.gitlab-ci.yml` antes de ejecutar un trabajo
que tenga acceso a secretos. Enmascarar y ocultar una variable no hace seguro el código de CI
que no es de confianza.

## Ejecuta un análisis y revisa los hallazgos

Crea una solicitud de fusión protegida que cumpla los requisitos o ejecuta el pipeline en la
rama predeterminada protegida. Empieza con un diff pequeño antes de ejecutar un análisis con costo
del repositorio completo.

Abre el trabajo `codex-security` y confirma que sus artefactos incluyan:

- `scan-manifest.json`
- `findings.json`
- `coverage.json`
- `results.sarif`
- `scan-exit-code.txt`

Luego abre la pestaña **Seguridad** del pipeline, revisa las advertencias de ingesta y confirma
los identificadores de los hallazgos, los niveles de gravedad y las ubicaciones en el código fuente. Los análisis de la rama predeterminada
también crean registros de vulnerabilidades del proyecto. Los hallazgos de las solicitudes de fusión aparecen en
la pestaña Seguridad del pipeline o en el widget de seguridad de la solicitud de fusión, pero no crean
registros de vulnerabilidades a nivel de proyecto.

Restringe el acceso a los artefactos, ya que los resultados del análisis pueden contener fragmentos de código fuente
vulnerable, evidencia y detalles de remediación.

## Elige un perfil de análisis

El pipeline selecciona un perfil según el evento que lo activa:

| Evento desencadenante                                        | Objetivo          | Modo       | Esfuerzo  |
| ---------------------------------------------- | --------------- | ---------- | ------- |
| Solicitud de fusión protegida del mismo proyecto           | Diff registrado en commits  | `standard` | `low`   |
| Envío de cambios a la rama predeterminada protegida o ejecución manual, con activación explícita | Repositorio completo | `standard` | `high`  |
| Ejecución programada en la rama predeterminada protegida, con activación explícita    | Repositorio completo | `deep`     | `xhigh` |

Los análisis de solicitudes de fusión centran los comentarios en el cambio registrado en commits.
Los análisis de la rama predeterminada revisan el repositorio integrado. Los análisis profundos programados
ofrecen una cobertura periódica más amplia. Un análisis de diff completado se aplica solo a ese
cambio y no demuestra que todo el repositorio esté libre de problemas.

El flujo de trabajo instala la CLI fuera del repositorio y la ejecuta mediante una ruta
absoluta. Su comprobación previa en modo de simulación usa la clave de API limitada al proceso, pero no inicia
un análisis con costo ni verifica la autenticación de la API, el acceso a Codex Security, la cuota ni la
disponibilidad del modelo.

El flujo de trabajo escribe el estado y los resultados del análisis fuera del worktree y limita
`OPENAI_API_KEY` al proceso de análisis. La CLI recibe un entorno reducido y definido explícitamente
en lugar de heredar todas las variables de GitLab. Para los análisis de diff, el
flujo de trabajo calcula la base de fusión y vincula el análisis a las revisiones base y
head revisadas.

El ejemplo fija `@openai/codex-security` en la versión `0.1.20`. Vuelve a probar la autenticación,
los artefactos, la ingesta de SARIF y el control de políticas antes de cambiar la versión fijada.

## Separa la generación de informes de la aplicación de políticas

GitLab ingiere SARIF desde un trabajo de informes completado correctamente. El pipeline publica el
informe primero y restablece el estado de salida del analizador en el trabajo independiente
`codex-security-gate`.

El trabajo de informes acepta hallazgos con los códigos de salida `0` y `1`. Acepta el código de salida
`2` solo cuando el archivo de manifiesto del análisis demuestra que el análisis se completó, la cobertura es
explícitamente `partial` y existe un informe SARIF no vacío. Los demás errores de ejecución,
configuración o exportación siguen bloqueando el proceso.

El control final conserva estos códigos de salida del analizador:

| Salida | Significado                                                                     |
| ---- | --------------------------------------------------------------------------- |
| `0`  | El escaneo finalizó con cobertura completa y cumplió su política.            |
| `1`  | El escaneo finalizó y encontró un problema que alcanza o supera el umbral configurado. |
| `2`  | El escaneo tuvo cobertura incompleta o un error de entrada o de ejecución.              |

El ejemplo permite temporalmente el código de salida `2` mientras calibras la cobertura parcial.
Elimina esa excepción cuando la cobertura incompleta deba bloquear el pipeline.

La remediación y la publicación se ejecutan antes del control final de políticas. Un hallazgo que cumple los requisitos
puede generar una solicitud de fusión en borrador verificada, incluso si el control después
hace que el pipeline falle.

## Habilitar la remediación verificada

La remediación automatizada es opcional y solo se ejecuta en pipelines de la rama predeterminada
protegida. El proceso de remediación de Codex y los comandos de verificación controlados
por el repositorio no reciben el token de acceso al proyecto de GitLab ni las credenciales
inyectadas por el runner.

El contrato de seguridad tiene tres partes: los comandos controlados por el repositorio nunca
reciben credenciales de OpenAI ni de GitLab, solo el trabajo de publicación recibe
acceso de escritura al repositorio y cada cambio generado permanece en borrador hasta que
una persona lo revisa y lo fusiona.

El flujo de trabajo:

1. Requiere cobertura completa del escaneo y un hallazgo de gravedad `high` o
   `critical`.
2. Confirma que la prueba de regresión configurada falle antes de aplicar el parche.
3. Genera un parche específico y rechaza cambios en archivos de CI, de credenciales, binarios u
otros archivos protegidos.
4. Ejecuta la prueba de regresión sin credenciales de OpenAI, de GitLab, del registro, de despliegue ni
de tokens de trabajo.
5. Usa `verify-fix` para devolver `fixed`, `still_vulnerable` o `inconclusive`.
   El trabajo publica un parche solo cuando `verify-fix` devuelve `fixed` y el
   proceso de verificación deja el parche sin cambios.

Configura estas variables protegidas para habilitar la remediación:

- Establece `CODEX_SECURITY_ENABLE_REMEDIATION` en `true`.
- Configura `CODEX_SECURITY_VERIFICATION_COMMAND` con una prueba de regresión existente que
  termine con el código de salida `1` antes de la corrección y `0` después.
- De manera opcional, configura `CODEX_SECURITY_SETUP_COMMAND` con un comando no interactivo
  de configuración de dependencias.

Elige una prueba de regresión que compruebe la invariante de seguridad subyacente, no
una implementación particular. Revisa con el mismo rigor los cambios generados en las pruebas y
en el código fuente.

<details>
  <summary>Avanzado: aislamiento de comandos del repositorio</summary>

Los comandos `validate`, `patch` y `verify-fix` reciben una
`CODEX_API_KEY` limitada al proceso. Los comandos de configuración y pruebas controlados por el repositorio se ejecutan como
un usuario distinto sin privilegios en una copia con permisos de escritura de los archivos fuente bajo control de versiones.
La copia excluye intencionalmente los metadatos de Git, el contenido de los submódulos y
los artefactos descargados. Los comandos de configuración y pruebas que requieren `.git` o
submódulos deben ejecutarse en un trabajo sin credenciales diseñado por separado.

Solo los pasos de Codex cuyo propietario es root pueden acceder a la copia de trabajo canónica o al
directorio adyacente de variables de tipo archivo de GitLab. El entorno limpio de la copia contiene únicamente
`PATH`, `HOME`, `LANG`, `CI` y `CI_PROJECT_DIR`. Si un comando necesita otro
valor que no sea secreto, agrégalo a la lista de permitidos después de revisar el comando. Si tu
runner no puede cambiar de usuario, traslada la verificación a un trabajo independiente
sin credenciales antes de habilitar la remediación.

</details>

## Publicar una solicitud de fusión en borrador

Crea un [token de acceso a un proyecto
de GitLab](https://docs.gitlab.com/user/project/settings/project_access_tokens/#create-a-project-access-token)
con el rol Developer y los alcances `api` y `write_repository`. Guárdalo como
una variable `GITLAB_REMEDIATION_TOKEN` protegida, enmascarada y oculta, con alcance limitado
al entorno `codex-security/publish`.

Establece `CODEX_SECURITY_CREATE_MR=true` para habilitar la publicación. Configura también la variable no secreta
`CODEX_SECURITY_MR_TEST_COMMAND` con la prueba de regresión de seguridad específica del proyecto
que debe superar cada rama de remediación generada. Mantén esta variable
sin protección para que la solicitud de fusión generada sin protección pueda leer el comando.
El flujo de trabajo de publicación:

- Recibe el token de escritura en el repositorio, pero ninguna credencial de OpenAI.
- Crea una rama `codex-security/fix-<finding-hash>`.
- Abre una solicitud de fusión en borrador y reutiliza un borrador abierto existente en lugar de
crear un duplicado.
- Ejecuta la prueba de regresión de la rama de remediación sin protección como un usuario sin privilegios
en una copia que solo contiene archivos bajo control de versiones, sin credenciales protegidas.
- Nunca fusiona automáticamente el cambio generado.

No uses `CI_JOB_TOKEN` en lugar del token de acceso al proyecto. No puede realizar
la operación necesaria para crear la solicitud de fusión. Revisa el parche propuesto,
la evidencia de verificación y el hallazgo antes de fusionar.

## Configurar variables opcionales

Configura solo las variables necesarias para las funciones que habilites:

| Variable                                  | Cuándo se necesita                       | Valor predeterminado o propósito                                          |
| ----------------------------------------- | --------------------------------- | ----------------------------------------------------------- |
| `CODEX_SECURITY_API_KEY`                  | Cada escaneo                        | Protegida, enmascarada y oculta; limita su alcance a `codex-security/openai` |
| `CODEX_SECURITY_VERSION`                  | Actualización de la CLI                       | Fijado en `0.1.20`; vuelve a realizar las pruebas antes de cambiarlo                  |
| `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` | Escaneos completos de la rama predeterminada         | Activación explícita; desactivada por defecto                             |
| `CODEX_SECURITY_SCHEDULED_DEEP_SCAN`      | Escaneos profundos programados              | Activación explícita; desactivada por defecto                             |
| `CODEX_SECURITY_DEEP_MAX_TIME_HOURS`      | Escaneos profundos programados              | Presupuesto de tiempo obligatorio mayor que `0` y menor que `8`     |
| `CODEX_SECURITY_DEEP_MAX_COST`            | Escaneos profundos programados              | Límite obligatorio de costo estimado en USD mayor que `0`      |
| `CODEX_SECURITY_ENABLE_REMEDIATION`       | Generación de parches                  | Activación explícita con variable protegida; desactivada por defecto                            |
| `CODEX_SECURITY_VERIFICATION_COMMAND`     | Generación de parches                  | Prueba de regresión protegida                                   |
| `CODEX_SECURITY_SETUP_COMMAND`            | Configuración opcional de la remediación        | Instalación protegida de dependencias                           |
| `CODEX_SECURITY_REMEDIATION_EFFORT`       | Ajustes opcionales de la remediación       | `high`                                                      |
| `CODEX_SECURITY_MAX_CHANGED_FILES`        | Límite opcional del tamaño del parche         | `8`; rango permitido de `1` a `20`                         |
| `CODEX_SECURITY_CREATE_MR`                | Creación de solicitudes de fusión en borrador      | Activación explícita con variable protegida; desactivada por defecto                            |
| `GITLAB_REMEDIATION_TOKEN`                | Creación de solicitudes de fusión en borrador      | Token de proyecto con el rol Developer y alcance limitado a `codex-security/publish`  |
| `CODEX_SECURITY_GITLAB_INTERNAL_URL`      | Publicación opcional en una instancia autoalojada   | Origen de GitLab accesible desde el runner                     |
| `CODEX_SECURITY_MR_TEST_COMMAND`          | Publicación de solicitudes de fusión en borrador    | Prueba de regresión obligatoria, específica del proyecto y sin secretos       |
| `CODEX_SECURITY_MR_SETUP_COMMAND`         | Configuración opcional de la rama de remediación | Configuración de dependencias sin secretos                                 |

GitLab proporciona las variables `CI_*`. El pipeline administra
`CODEX_SECURITY_BIN`, `CODEX_SECURITY_EFFORT`, `CODEX_SECURITY_MODE`,
`CODEX_SECURITY_STATE_DIR` y `CODEX_SECURITY_TARGET`; no las configures
como variables del proyecto. Para los análisis de diferencias, la CLI deriva la identidad canónica
del objetivo a partir de las revisiones base y head normalizadas.

## Ajusta la aplicación de políticas y el costo

Usa análisis centrados en las diferencias para obtener comentarios sobre las solicitudes de fusión, análisis estándar del repositorio
para la rama predeterminada y análisis profundos programados para una cobertura más amplia. Ambos
perfiles de análisis de todo el repositorio están desactivados de forma predeterminada. Un análisis profundo programado también requiere
`CODEX_SECURITY_DEEP_MAX_TIME_HOURS` y `CODEX_SECURITY_DEEP_MAX_COST`; mantén el
tiempo asignado a la CLI por debajo del límite de ocho horas del trabajo. Mide ejecuciones representativas
antes de establecer un presupuesto. Considera `--max-cost` un límite para el costo estimado, no
un tope estricto de facturación.

Empieza con análisis que solo generen informes. Agrega `--fail-on-severity` después de que tu equipo haya
revisado hallazgos representativos, la cobertura, el costo y el tiempo de ejecución. Consulta [Ejecutar Codex Security
en CI](/es-419/codex/security/cli/ci) para conocer las políticas de gravedad y los detalles
de los códigos de salida.

Cuando falla un trabajo:

- La falta de artefactos del análisis indica un problema de configuración o del runner.
- Si hay artefactos con cobertura parcial, debes revisar `coverage.json`.
- Si faltan hallazgos en GitLab, verifica si el trabajo del informe SARIF
se completó correctamente y si GitLab aceptó el informe.
- Si se omite la remediación, verifica la rama protegida, la cobertura
completa, la gravedad del hallazgo, el comando de verificación y las variables de activación explícita.
- Si hay errores de publicación, verifica el rol, los ámbitos y
la restricción de entorno del token del proyecto.

Para obtener información sobre cada comando, opción y artefacto, consulta la [referencia de la
CLI de Codex Security](/es-419/codex/security/cli/reference).
