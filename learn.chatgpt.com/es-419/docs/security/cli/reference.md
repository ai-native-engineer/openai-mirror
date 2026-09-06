<!-- source: https://learn.chatgpt.com/es-419/docs/security/cli/reference -->

Usa esta referencia para consultar los comandos y las opciones que admite `codex-security`,
así como los formatos de salida y el comportamiento al finalizar. Para realizar un primer análisis guiado, comienza con el
[inicio rápido de la CLI](/es-419/codex/security/cli).

  El paquete `@openai/codex-security` es público. Para ejecutar análisis, necesitas acceso a Codex
  Security. Los análisis usan tus permisos locales y no se detienen para solicitar
  aprobación. Antes de comenzar, revisa [Permisos de análisis
  locales](#local-scan-permissions).

Ejecuta la CLI con `npx @openai/codex-security`.

## Descripción general de los comandos

```text
usage: codex-security [--version] <command> [options]

La CLI ofrece estos comandos:

| Comando                       | Función                                               |
| ----------------------------- | ----------------------------------------------------- |
| `codex-security scan`         | Ejecutar un análisis de Codex Security.                            |
| `codex-security install-hook` | Instalar un análisis de seguridad de Git previo al commit.               |
| `codex-security bulk-scan`    | Descubrir repositorios y ejecutar análisis en lote que se puedan reanudar.   |
| `codex-security scans`        | Enumerar, inspeccionar, comparar y recuperar registros de análisis guardados. |
| `codex-security findings`     | Revisar y actualizar los hallazgos de seguridad guardados.            |
| `codex-security export`       | Exportar hallazgos completados como CSV, JSON o SARIF.     |
| `codex-security publish`      | Publicar en Linear los hallazgos de análisis completados.            |
| `codex-security validate`     | Comprobar uno o más posibles hallazgos de seguridad.        |
| `codex-security patch`        | Aplicar parches a uno o más problemas de seguridad.                    |
| `codex-security login`        | Iniciar sesión, guardar credenciales o comprobar el estado del inicio de sesión.  |
| `codex-security logout`       | Eliminar los datos de inicio de sesión guardados.                            |
| `codex-security info`         | Mostrar metadatos de solo lectura del SDK y del complemento incluido.       |

La CLI también ofrece estos comandos de integración:

| Comando                      | Función                               |
| ---------------------------- | ------------------------------------- |
| `codex-security completions` | Generar scripts de autocompletado para el shell.    |
| `codex-security mcp`         | Registrar la CLI como servidor MCP.    |
| `codex-security skills`      | Sincronizar las habilidades de Codex Security con los agentes. |

Muestra todos los comandos disponibles:

```bash
npx @openai/codex-security --help

Agrega `--help` a un comando para consultar sus argumentos y opciones:

```bash
npx @openai/codex-security scan --help

`codex-security --version` muestra la versión instalada y finaliza.
`codex-security info --json` indica las versiones del SDK y del complemento incluido.
Ninguno de los dos comandos requiere Python.

### Descubrir comandos y conectar agentes

Imprime el archivo de manifiesto de comandos legible para los agentes:

```bash
npx @openai/codex-security --llms

Inspecciona el esquema de argumentos del análisis en formato JSON:

```bash
npx @openai/codex-security scan --schema --format json

Genera el autocompletado del shell para Bash:

```bash
npx @openai/codex-security completions bash

Reemplaza `bash` por `zsh` o `fish` si usas esos shells.

Los resultados del análisis admiten `--format toon|json|yaml|jsonl` y `--full-output`. La opción
`--format` a nivel del framework es independiente de `--export-format`, que selecciona
el formato de un artefacto exportado desde un análisis completado. La ayuda global del comando
también incluye `md`, pero los resultados del análisis no admiten la salida en formato Markdown.

Registra la CLI como servidor MCP:

```bash
npx @openai/codex-security mcp add

Sincroniza las habilidades de Codex Security con tus agentes:

```bash
npx @openai/codex-security skills add

MCP solo expone el comando de metadatos de solo lectura `info`. Los análisis, las exportaciones,
la autenticación, la validación y la aplicación de parches siguen siendo exclusivos de la CLI.

## `codex-security scan`

Ejecuta un análisis en un repositorio, en rutas seleccionadas, en cambios confirmados o en el
árbol de trabajo.

```text
usage: codex-security scan [-h] [--auth {auto,chatgpt,api-key}]
                           [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                           [--path PATH | --diff BASE | --working-tree]
                           [--head HEAD] [--base BASE]
                           [--knowledge-base PATH] [--scan-prompt-file FILE]
                           [--post-scan-prompt-file FILE]
                           [--mode {standard,deep}] [--workers N]
                           [--subagents N] [--stop-after-no-new N]
                           [--max-discovery-runs N] [--max-time-hours HOURS]
                           [--model MODEL]
                           [--effort {minimal,low,medium,high,xhigh,max}]
                           [--output-dir DIR]
                           [--archive-existing]
                           [--plugin-path PATH] [--python PATH]
                           [--codex KEY=VALUE] [--fail-on-severity LEVEL]
                           [--patch] [--patch-severity {critical,high,medium,low}]
                           [--create-pr]
                           [--max-cost USD] [--dry-run] [--headless] [--verbose]
                           [--json] [--format {toon,json,yaml,jsonl}]
                           [--full-output] [repository]

El valor predeterminado de `repository` es el directorio actual.

### Seleccionar la autenticación para el análisis

Usa `--auth auto`, la opción predeterminada, para seleccionar las credenciales automáticamente. Cuando están disponibles tanto
un inicio de sesión de ChatGPT como `OPENAI_API_KEY` o `CODEX_API_KEY`,
los análisis interactivos con salida de texto preguntan qué credencial usar. Los análisis de CI, JSON y
JSONL, así como los demás análisis sin una terminal interactiva, usan la
clave de API del entorno. Las ejecuciones de prueba no solicitan ni cargan credenciales.

Para usar tus credenciales guardadas, especifica `--auth chatgpt`:

```bash
npx @openai/codex-security scan . --auth chatgpt

Para usar una clave de API del entorno, especifica `--auth api-key`:

```bash
npx @openai/codex-security scan . --auth api-key

Para que la selección automática use de forma predeterminada las credenciales guardadas, ejecuta
`unset OPENAI_API_KEY CODEX_API_KEY`.

### Usar OpenRouter o Fireworks

Selecciona OpenRouter con su clave de API y un modelo explícito:

```bash

npx @openai/codex-security scan . \
  --provider openrouter \
  --model anthropic/claude-sonnet-4.5

Selecciona Fireworks con su clave de API y un modelo explícito:

```bash

npx @openai/codex-security scan . \
  --provider fireworks \
  --model accounts/fireworks/models/qwen3-235b-a22b

Ambos proveedores también admiten `bulk-scan`.

### Usar Amazon Bedrock

Selecciona Amazon Bedrock con `--provider amazon-bedrock` y especifica de forma explícita
un modelo de Bedrock con `--model`:

```bash
npx @openai/codex-security scan . \
  --provider amazon-bedrock \
  --model openai.gpt-5.6-sol

Configura `AWS_REGION` y autentícate mediante `AWS_BEARER_TOKEN_BEDROCK`, claves de acceso estándar
de AWS, un perfil de AWS, una identidad web, credenciales de contenedor o la
cadena de credenciales predeterminada de AWS. Los análisis de Bedrock usan credenciales de AWS en lugar de
`--auth`, un inicio de sesión de ChatGPT o una clave de API de OpenAI. Tanto `scan` como `bulk-scan`
admiten `--provider`.

### Seleccionar el objetivo del análisis

Elige un tipo de objetivo para cada análisis.

| Argumento                 | Descripción                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| `--path PATH`            | Analiza una ruta relativa al repositorio. Repite la opción para indicar más rutas.         |
| `--diff BASE`            | Analiza los cambios confirmados desde `BASE` hasta `--head`. La revisión de destino usa `HEAD` de forma predeterminada.    |
| `--head HEAD`            | Establece la revisión de destino para `--diff`.                                             |
| `--working-tree`         | Analiza los cambios preparados y sin preparar con respecto a `--base`. La revisión base usa `HEAD` de forma predeterminada. |
| `--base BASE`            | Establece la revisión base para `--working-tree`.                                     |
| `--mode {standard,deep}` | Selecciona el modo de análisis. El valor predeterminado es `standard`.                                |

`--path`, `--diff` y `--working-tree` son mutuamente excluyentes. `--head`
requiere `--diff` y `--base` requiere `--working-tree`. El modo profundo admite
repositorios y rutas como objetivos.

Los análisis de diferencias y del árbol de trabajo requieren que el argumento del repositorio sea la raíz del
worktree de Git. Las referencias seleccionadas deben existir en ese checkout.

Analiza todo el repositorio:

```bash
npx @openai/codex-security scan .

Analiza las rutas seleccionadas:

```bash
npx @openai/codex-security scan . --path src --path tests

Analiza los cambios incluidos en commits:

```bash
npx @openai/codex-security scan . --diff origin/main --head HEAD

Analiza los cambios preparados y no preparados:

```bash
npx @openai/codex-security scan . --working-tree --base HEAD

Ejecuta una revisión más profunda del repositorio:

```bash
npx @openai/codex-security scan . --mode deep

### Configurar los análisis profundos

Usa estas opciones con `--mode deep` para controlar la concurrencia y el tiempo de ejecución de los procesos de análisis:

| Argumento                 | Descripción                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `--workers N`            | Cantidad máxima de procesos independientes de análisis estándar que pueden ejecutarse simultáneamente. El valor predeterminado es `4`.                |
| `--subagents N`          | Subagentes disponibles para cada proceso de análisis. El valor predeterminado es `3`.                                   |
| `--stop-after-no-new N`  | Detén el análisis cuando `N` análisis consecutivos completados por los procesos no detecten problemas nuevos. El valor predeterminado es `4`. |
| `--max-discovery-runs N` | Límite total de ejecuciones independientes de análisis estándar. El valor predeterminado es `40`.                       |
| `--max-time-hours HOURS` | Límite de tiempo de ejecución de los procesos de análisis, en horas. El valor predeterminado es `96`; acepta valores fraccionarios.             |

`--subagents` acepta cero o un entero positivo. `--max-time-hours` acepta un
número positivo que no supere `96`. Las demás opciones requieren un entero
positivo. Estas opciones no están disponibles para los análisis estándar.

Por ejemplo, usa dos procesos de análisis, permite hasta diez ejecuciones y detén la ejecución de los procesos
después de 1,5 horas:

```bash
npx @openai/codex-security scan . \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

Cuando vence el límite de tiempo, el análisis detiene los procesos que no finalizaron, conserva los resultados de los análisis
completados y los incorpora al informe final. Si ningún proceso termina la revisión
del código fuente, el análisis registra una cobertura parcial y devuelve el código de salida `2`.

Establece valores predeterminados persistentes en `~/.codex/codex-security/config.toml`, o en
`$CODEX_HOME/codex-security/config.toml` cuando configures `CODEX_HOME`:

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

Las opciones de la línea de comandos tienen prioridad sobre estos valores predeterminados. `scan --workers` controla los procesos
independientes de análisis estándar dentro de un análisis profundo; `bulk-scan --workers`
controla los análisis simultáneos de repositorios. Configura `stop_after_consecutive_errors` solo
en el archivo TOML; su valor predeterminado es `3`.

### Agregar contexto de seguridad

Usa `--knowledge-base PATH` para proporcionar documentos de arquitectura, modelos de amenazas
o políticas de seguridad. Repite la opción para incluir más archivos o directorios:

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Los documentos compatibles incluyen archivos `.md`, `.markdown`, `.txt`, `.pdf` y `.docx`.
La CLI busca en los directorios de forma recursiva, rechaza las rutas de entrada que sean enlaces,
omite las entradas de directorio que sean enlaces y mantiene el contenido extraído de los documentos
fuera de los resultados guardados del análisis.

### Agregar instrucciones de análisis

Para agregar instrucciones al análisis, proporciona un archivo de texto o Markdown mediante
`--scan-prompt-file`. Usa `--post-scan-prompt-file` para ejecutar instrucciones de seguimiento
en la misma sesión autenticada después de análisis exitosos y de
análisis con cobertura incompleta o errores:

```bash
npx @openai/codex-security scan . \
  --scan-prompt-file security-focus.md \
  --post-scan-prompt-file follow-up.md

Por ejemplo, usa el prompt del análisis para centrarte en los límites de autorización y pide
en las instrucciones de seguimiento que se escriba un nuevo archivo `post-scan-summary.md` en el directorio del análisis.
Si las instrucciones de seguimiento fallan, la CLI emite una advertencia y conserva el análisis completado.
Las instrucciones de seguimiento no se ejecutan después de una cancelación ni cuando el análisis alcanza su límite de
costo.

### Configurar las opciones de salida y de políticas

Usa estas opciones para conservar artefactos, mantener resultados anteriores o crear un resultado
legible por máquina.

| Argumento                   | Descripción                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `--output-dir DIR`         | Escribe los artefactos del análisis en un directorio privado situado fuera del worktree de Git que contiene el repositorio. De forma predeterminada, se usa el estado persistente de Codex Security. |
| `--archive-existing`       | Mueve los resultados existentes a `DIR.previous-<timestamp>-<id>` y comienza con un directorio de salida vacío. Requiere `--output-dir`.  |
| `--fail-on-severity LEVEL` | Devuelve el código de salida `1` cuando un análisis completado informa un hallazgo con una gravedad igual o superior a `critical`, `high`, `medium` o `low`.                  |
| `--patch`                  | Corrige y verifica los hallazgos seleccionados después de un análisis completo.                                                                      |
| `--patch-severity LEVEL`   | Aplica parches a los hallazgos con una gravedad igual o superior a `critical`, `high`, `medium` o `low`. El valor predeterminado es `low`.                                        |
| `--create-pr`              | Crea un commit con los archivos de parche verificados y abre un Pull Request en GitHub. Requiere `--patch`.                                              |
| `--max-cost USD`           | Detén un análisis cuando el costo estimado del modelo supere el monto especificado en USD.                                                  |
| `--dry-run`                | Comprueba el repositorio, el objetivo, la base de conocimientos, el directorio de salida y la configuración de Codex sin iniciar un análisis.             |
| `--headless`               | Muestra el progreso en texto sin formato en lugar del panel interactivo del análisis.                                                          |
| `--verbose`                | Imprime en stderr diagnósticos con datos sensibles ocultos sobre el ciclo de vida, la autenticación, el progreso y el costo.                                          |
| `--json`                   | Imprime el archivo de manifiesto, los hallazgos, la cobertura, las rutas y los metadatos de los turnos en un único documento JSON.                                           |
| `--format FORMAT`          | Imprime el resultado completo del análisis como `toon`, `json`, `yaml` o `jsonl`.                                                        |
| `--full-output`            | Imprime el resultado completo con el formato predeterminado de salida estructurada.                                                        |

El límite de costo es una estimación, no un tope de gasto estricto. Las solicitudes que ya están en
curso pueden finalizar ligeramente por encima del límite. Si un análisis profundo alcanza el límite
después de que Codex Security consolida los resultados de los procesos completados, la CLI sella los
resultados disponibles, marca la cobertura como `partial` y devuelve el código de salida `2`.
De lo contrario, devuelve `2` y conserva en disco cualquier salida parcial disponible.

Cuando omitas `--output-dir`, los resultados se conservarán en
`$CODEX_HOME/state/plugins/codex-security/scans/<repository>`. El valor predeterminado de `CODEX_HOME`
es `~/.codex`. Configura `CODEX_SECURITY_STATE_DIR` para conservar los resultados en
`$CODEX_SECURITY_STATE_DIR/scans/<repository>` en su lugar. Estos directorios pueden
contener fragmentos de código fuente y detalles de vulnerabilidades, por lo que debes administrar sus permisos
y su retención según corresponda.

El entorno de trabajo guarda el historial de análisis en
`$CODEX_HOME/state/plugins/codex-security/workbench.sqlite3`. Configurar
`CODEX_SECURITY_STATE_DIR` también cambia la ubicación de la base de datos del entorno de trabajo.

El directorio de salida debe estar fuera del directorio analizado y de cualquier
worktree de Git que lo contenga. Un análisis puede reemplazar un directorio de resultados existente con
`--archive-existing`.

Para conservar resultados anteriores antes de reutilizar un directorio de salida:

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --archive-existing

De forma predeterminada, los análisis solo generan informes. Agrega `--fail-on-severity` para evaluar una
política de gravedad en CI:

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --json \
  --fail-on-severity high \
  > /path/outside/repository/codex-security.json

Una ejecución de prueba comprueba las entradas locales, incluidos los documentos de la base de conocimientos, sin
cargar credenciales, iniciar Codex ni comprobar el intérprete de Python
del plugin:

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --dry-run

### Configurar el entorno de ejecución

Usa las opciones del entorno de ejecución cuando necesites especificar un modelo, un intérprete, un plugin o
un valor de configuración de Codex.

| Argumento                                                  | Descripción                                                                                              |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `--auth {auto,chatgpt,api-key}`                           | Selecciona las credenciales para el análisis. El valor predeterminado es `auto`.                                                      |
| `--provider {openai,openrouter,fireworks,amazon-bedrock}` | Selecciona el proveedor de inferencia. El valor predeterminado es `openai`.                                                  |
| `--model MODEL`                                           | Selecciona el modelo. El valor predeterminado es `gpt-5.6-sol`. Es obligatorio especificarlo para OpenRouter, Fireworks y Amazon Bedrock.  |
| `--effort {minimal,low,medium,high,xhigh,max}`            | Selecciona el esfuerzo de razonamiento del modelo. El valor predeterminado es `xhigh`.                                             |
| `--plugin-path PATH`                                      | Usa un directorio o archivo ZIP del Plugin de Codex Security para reemplazar el plugin incluido.                             |
| `--python PATH`                                           | Selecciona el intérprete de Python para el entorno de ejecución del plugin.                                                    |
| `--codex KEY=VALUE`                                       | Sobrescribe un valor aislado de la configuración de Codex. Los valores usan la sintaxis TOML. Repite la opción para agregar más valores. |

Para seleccionar otro modelo y esfuerzo de razonamiento sin escribir TOML:

```bash
npx @openai/codex-security scan . --model gpt-5.6-terra --effort high

Coloca entre comillas los valores de tipo cadena que pases mediante `--codex` para que el analizador de TOML reciba una
cadena:

```bash
npx @openai/codex-security scan . --codex 'model="gpt-5.6-terra"'

## `codex-security install-hook`

Instala una comprobación de seguridad pre-commit de Git para el repositorio actual:

```bash
npx @openai/codex-security install-hook

La comprobación analiza los cambios preparados y no preparados antes de cada commit e impide continuar ante
hallazgos de gravedad alta o errores de análisis. Respeta `core.hooksPath` y no
reemplaza un script de pre-commit existente. Establece un umbral de gravedad diferente
cuando sea necesario:

```bash
npx @openai/codex-security install-hook . --fail-on-severity medium

## `codex-security bulk-scan`

Descubre y analiza repositorios de GitHub o ejecuta un análisis reanudable a partir de un
CSV de repositorios:

Para consultar una guía completa sobre la búsqueda en GitHub, los inventarios CSV, los resultados de campañas
y los análisis en contenedores, consulta [Ejecuta análisis de seguridad
en lote](/es-419/codex/security/cli/bulk-scans).

```text
usage: codex-security bulk-scan [input] [--output-dir DIR]
                                [--workers N] [--mode {standard,deep}]
                                [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                                [--model MODEL]
                                [--effort {minimal,low,medium,high,xhigh,max}]
                                [--knowledge-base PATH]
                                [--scan-prompt-file FILE]
                                [--post-scan-prompt-file FILE]
                                [--max-attempts N] [--plugin-path PATH]
                                [--python PATH] [--codex KEY=VALUE]

Ejecuta `npx @openai/codex-security bulk-scan` sin argumentos para seleccionar
repositorios de forma interactiva. Este flujo requiere iniciar sesión en GitHub CLI.

Para elegir un modelo y el esfuerzo de razonamiento durante la búsqueda interactiva:

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

Para usar una lista de repositorios preparada, proporciona un archivo CSV y `--output-dir`:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

El CSV requiere las columnas `id`, `repository` y `revision`. Las revisiones deben ser
hashes de commit completos. Las columnas opcionales `scope`, `mode` y `prompt` configuran
repositorios individuales:

```csv
id,repository,revision,scope,mode,prompt
service,https://github.com/example/service.git,0123456789abcdef0123456789abcdef01234567,src,standard,Review authorization boundaries.

Usa `--knowledge-base PATH` para compartir documentos de seguridad entre todos los
repositorios. Usa `--scan-prompt-file FILE` para agregar instrucciones de análisis compartidas; la
columna `prompt` del CSV agrega instrucciones específicas de cada repositorio después de ese
prompt compartido. `--post-scan-prompt-file FILE` ejecuta instrucciones de seguimiento después de cada
análisis, incluidos aquellos con cobertura incompleta o errores. No se ejecuta después de una
cancelación ni cuando un análisis alcanza su límite de costo.

`--workers` limita los análisis simultáneos de repositorios y su valor predeterminado es `4`. El valor predeterminado de `--mode`
es `standard` y el de `--max-attempts` es `1`. Configura
`--max-attempts` para reintentar cuando haya errores en el repositorio o en el análisis. Los análisis completados con
cobertura incompleta no se reintentan. Sus resultados siguen disponibles y el
comando devuelve el código de salida `2`.

Vuelve a ejecutar el mismo comando para reanudar desde un directorio de salida existente. La CLI
omite los análisis completados, incluidos aquellos con cobertura incompleta.

Para campañas en contenedores, consulta [Ejecuta análisis en lote en
Docker](/es-419/codex/security/cli/bulk-scans#run-bulk-scans-in-docker).

## `codex-security scans`

### Buscar análisis guardados

Enumera los análisis guardados del directorio actual:

```bash
npx @openai/codex-security scans

Enumera los análisis de otro repositorio:

```bash
npx @openai/codex-security scans list /path/to/repository

Busca análisis almacenados en un directorio de salida específico:

```bash
npx @openai/codex-security scans list --scan-root /path/outside/repository/results

### Inspeccionar o repetir un análisis

Muestra los resultados y la configuración de un análisis guardado:

```bash
npx @openai/codex-security scans show SCAN_ID

Agrega `--show-linked-findings` para incluir enlaces a hallazgos de análisis anteriores.

Vuelve a ejecutar el análisis en el checkout actual con su configuración original:

```bash
npx @openai/codex-security scans rerun SCAN_ID

La nueva ejecución requiere la versión del complemento registrada por el análisis original. Si la
versión instalada es diferente, el comando se detiene en lugar de ejecutarse con un
complemento distinto.

### Inspeccionar los registros de análisis guardados

Lee todos los eventos de sesión guardados de un análisis y sus procesos de trabajo. Estos registros
no ocultan datos confidenciales y pueden contener código fuente o credenciales, así que revísalos
antes de compartirlos:

```bash
npx @openai/codex-security scans logs SCAN_ID

Agrega `--json` para obtener un resultado en formato legible por máquinas con toda la información.

### Vincular y comparar hallazgos

Compara dos análisis para encontrar hallazgos nuevos, persistentes, reabiertos, resueltos y
desconocidos:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

La comparación vincula automáticamente los hallazgos que comparten la misma causa raíz
y reutiliza los vínculos guardados. Para guardar los vínculos explícitamente, usa `scans match`:

```bash
npx @openai/codex-security scans match PREVIOUS_SCAN_ID CURRENT_SCAN_ID

Un hallazgo se considera desconocido cuando el análisis posterior tiene cobertura incompleta o no
cubre la ubicación original del hallazgo. Agrega `--force` a `match` cuando necesites
volver a calcular un vínculo existente.

Para vincular todos los análisis completados del repositorio actual, incluidos los análisis de
otros checkouts:

```bash
npx @openai/codex-security scans match --all

Los resultados de los análisis pueden variar aunque vuelvas a ejecutar la misma configuración. La vinculación y
la comparación registran los cambios; no hacen que los resultados sean deterministas ni demuestran que una
vulnerabilidad haya dejado de existir. Usa `validate` para volver a comprobar un hallazgo crítico para la
seguridad en el código actual.

## `codex-security findings`

Enumera los hallazgos abiertos de los análisis del repositorio actual:

```bash
npx @openai/codex-security findings list

Pasa la ruta de un repositorio para inspeccionar otro checkout:

```bash
npx @openai/codex-security findings list /path/to/repository

Agrega `--json` para obtener una salida estructurada. La lista identifica los hallazgos detectados en el
último análisis y los hallazgos anteriores que no se confirmaron en ese análisis.

Ten en cuenta que los hallazgos anteriores permanecen abiertos hasta que se resuelvan o se descarten (su ausencia
en el último análisis no se interpreta como prueba de que se hayan corregido).

Para registrar un hallazgo revisado como falso positivo:

```text
usage: codex-security findings false-positive OCCURRENCE_ID
                       --reason REASON

Inspecciona el análisis guardado para identificar la aparición del hallazgo:

```bash
npx @openai/codex-security scans show SCAN_ID

Registra una explicación específica del falso positivo:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

El motivo no puede estar vacío. Codex Security guarda la decisión para el
repositorio y la proporciona como contexto para análisis futuros. Cada análisis vuelve a comprobar de forma independiente
el código fuente actual, los controles y la alcanzabilidad. Una decisión anterior
no suprime una regla, ruta ni clase de vulnerabilidad.

## `codex-security export`

Exporta CSV, JSON o SARIF desde un análisis completado y sellado. La exportación valida los
artefactos del análisis antes de escribir la salida y no modifica el entorno de ejecución de Codex ni las
credenciales.

```text
usage: codex-security export [--export-format {csv,json,sarif}]
                             [--output FILE|-] [--source-root PATH]
                             [--python PATH] scan_dir

`scan_dir` es el directorio del análisis completado.

| Argumento                           | Descripción                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| `--export-format {csv,json,sarif}` | Selecciona el formato de exportación. El valor predeterminado es `sarif`.                                           |
| `--output FILE\|-`                 | Escribe el formato seleccionado en un archivo o en stdout. De forma predeterminada, se escribe en un archivo del directorio actual. |
| `--source-root PATH`               | Agrega huellas digitales de las líneas de código fuente a SARIF mediante un checkout del repositorio.                          |
| `--python PATH`                    | Selecciona el intérprete de Python para el exportador incluido.                                     |

`--source-root` solo funciona con `--export-format sarif`. JSON conserva
el documento sellado de hallazgos. CSV contiene columnas transferibles de hallazgos y
no incluye el estado de clasificación del entorno de trabajo local.

Sin `--output`, la CLI escribe SARIF en `results.sarif`, JSON en
`findings.json` y CSV en `findings.csv` dentro del directorio de trabajo actual.
Las exportaciones pueden contener fragmentos del código fuente y detalles de vulnerabilidades. Ejecuta el comando
fuera del repositorio o pasa `--output` con una ruta privada fuera del
checkout analizado.

Escribe SARIF en un archivo:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root /path/to/repository \
  --output /path/outside/repository/exports/results.sarif

Escribe SARIF en stdout:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root . \
  --output -

Exporta los hallazgos como JSON:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format json \
  --output /path/outside/repository/exports/findings.json

Exporta los hallazgos como CSV:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format csv \
  --output /path/outside/repository/exports/findings.csv

## `codex-security publish scan`

Publica todos los hallazgos de un análisis completado en Linear:

```text
usage: codex-security publish scan [SCAN_DIR] --to linear
                                   [--linear-team TEAM_ID]
                                   [--project PROJECT_ID]
                                   [--linear-api-key KEY]
                                   [--linear-assignee EMAIL_OR_USER_ID]
                                   [--dry-run] [--json]

`SCAN_DIR` debe contener un análisis completado y sellado. Omítelo en una terminal
interactiva para seleccionar un análisis completado del historial local de análisis. Para crear incidencias,
el análisis y sus hallazgos también deben estar en el historial local de análisis. Una ejecución
de prueba valida los artefactos sellados sin esta comprobación de persistencia.

| Argumento                             | Descripción                                                                                                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--to linear`                        | Publica en Linear. Este argumento es obligatorio.                                                                                                                    |
| `--linear-team TEAM_ID`              | Selecciona el equipo de Linear. Si se omite, se usa `CODEX_SECURITY_LINEAR_TEAM`; una de las dos opciones es obligatoria.                                                                 |
| `--project PROJECT_ID`               | Selecciona un proyecto de Linear. Si se omite, se usa `CODEX_SECURITY_LINEAR_PROJECT`. Si no se configura ninguna de las dos opciones, las incidencias se crean directamente en el equipo.                          |
| `--linear-api-key KEY`               | Usa una clave de API personal de Linear para publicar directamente. Si se omite, se usa `CODEX_SECURITY_LINEAR_API_KEY`.                                                         |
| `--linear-assignee EMAIL_OR_USER_ID` | Asigna las incidencias creadas mediante una dirección de correo electrónico o un ID de usuario de Linear. Requiere `--linear-api-key` o `CODEX_SECURITY_LINEAR_API_KEY`. Si se omite, las incidencias quedan sin asignar. |
| `--dry-run`                          | Prepara las cargas útiles de las incidencias sin iniciar Codex, contactar a Linear, crear incidencias ni escribir el estado de publicación.                                                 |
| `--json`                             | Escribe los resultados estructurados de la publicación en stdout. El progreso permanece en stderr.                                                                                      |

  Las descripciones de las incidencias de Linear y la salida de la ejecución de prueba pueden incluir fragmentos de código fuente
y detalles de vulnerabilidades. Publica únicamente en un equipo o proyecto de Linear
autorizado y trata la salida guardada como información confidencial.

Cada ejecución que no sea de prueba intenta crear una incidencia nueva para cada hallazgo.
Volver a publicar el mismo análisis no vincula, actualiza ni reutiliza las incidencias existentes.
Si falla la publicación de algunos hallazgos, el comando conserva las incidencias creadas correctamente y
devuelve el código de salida `2`.
Con `--json`, revisa los resultados `created` y `failed` antes de reintentar para
evitar duplicados.

Previsualiza las cargas útiles de las incidencias antes de publicarlas:

```bash
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --dry-run \
  --json

### Publicar con la aplicación de Linear conectada

Sin una clave de API de Linear, el comando inicia Codex con tu configuración
actual y la aplicación de Linear conectada. Inicia sesión y conecta Linear a tu
cuenta de Codex antes de publicar:

```bash
npx @openai/codex-security login
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --project PROJECT_ID

### Publicar con una clave de API de Linear

Si proporcionas `--linear-api-key` o `CODEX_SECURITY_LINEAR_API_KEY`, la publicación se realiza
directamente mediante la API de Linear y Codex no se inicia. La publicación directa
deja las incidencias sin asignar, a menos que selecciones un responsable:

```bash

npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --linear-assignee teammate@example.com

Los valores de la línea de comandos tienen prioridad sobre las variables de entorno correspondientes. Para las claves de API,
usa `CODEX_SECURITY_LINEAR_API_KEY` en lugar de `--linear-api-key`, ya que los
argumentos de la línea de comandos pueden aparecer en el historial del shell y en las listas de procesos.

## `codex-security validate` y `codex-security patch`

Comprueba si un posible hallazgo es válido:

```bash
npx @openai/codex-security validate findings.json \
  "Possible SQL injection in src/query.ts:42"

Genera una corrección con la habilidad de remediación incluida:

```bash
npx @openai/codex-security patch findings.json \
  "Missing authorization check in src/routes.ts:18"

Cada argumento posicional acepta texto literal o la ruta de un archivo. Estas entradas usan
el directorio actual. Usa `validate` para volver a comprobar un hallazgo después de una corrección o cuando un
análisis posterior ya no lo reporte. La comparación de análisis por sí sola no demuestra que una corrección
haya funcionado.

Usa `--effort` para seleccionar el esfuerzo de razonamiento de cualquiera de los comandos:

```bash
npx @openai/codex-security validate "Possible SQL injection" --effort high

### Corregir hallazgos después de un análisis

Usa `scan --patch` para corregir hallazgos después de un análisis completo. Esto requiere
`@openai/codex-security` 0.1.15 o una versión posterior. El umbral de gravedad predeterminado es
`low`. Este comando selecciona hallazgos de gravedad alta y crítica:

```bash
npx @openai/codex-security scan . --patch --patch-severity high --json

Los hallazgos verificados y ya corregidos no activan `--fail-on-severity`.

### Corregir hallazgos guardados

Proporciona el ID de un hallazgo o de una ocurrencia para aplicar una corrección en su repositorio original, o selecciona
hallazgos de un análisis guardado:

```bash
npx @openai/codex-security patch OCCURRENCE_ID
npx @openai/codex-security patch --scan SCAN_ID --severity high --json
npx @openai/codex-security patch --scan latest --severity medium

`--scan latest` selecciona el último análisis completado del repositorio actual.
Los comandos para hallazgos guardados admiten `--json`; las entradas de texto literal y las de archivos no lo admiten.

Agrega `--create-pr` para crear un commit únicamente con los archivos de parche verificados y abrir un Pull Request
con la CLI de GitHub:

```bash
npx @openai/codex-security patch --scan SCAN_ID --severity high --create-pr

Si falla el push o el Pull Request, ejecuta el comando indicado `patch --resume-pr BRANCH`
desde el mismo repositorio para volver a intentarlo.

### Corregir incidencias de Linear

Configura `CODEX_SECURITY_LINEAR_API_KEY` o `LINEAR_API_KEY` para usar una clave de API personal,
o `LINEAR_ACCESS_TOKEN` para usar un token OAuth. Usa una variable de entorno en lugar de
`--linear-api-key KEY` para evitar que la clave aparezca en el historial del shell.

Importa una incidencia mediante su ID o URL. Repite `--linear-issue` para seleccionar más de una
incidencia:

```bash
npx @openai/codex-security patch --linear-issue SEC-123 --linear-issue SEC-124

Usa `--linear-project` para seleccionar las incidencias abiertas de un proyecto. Agrega `--linear-filter`
para acotar la selección:

```bash
npx @openai/codex-security patch --linear-project "Security backlog" \
  --linear-filter '{"labels":{"name":{"eq":"security"}}}'

La CLI excluye las incidencias completadas y canceladas, a menos que el filtro establezca `state`.
No modifica las incidencias de Linear.

## `codex-security login`, `logout` y `info`

Inicia sesión de forma interactiva:

```bash
npx @openai/codex-security login

Usa la autenticación de dispositivo en una máquina remota o sin interfaz gráfica:

```bash
npx @openai/codex-security login --device-auth

Comprueba el inicio de sesión actual:

```bash
npx @openai/codex-security login status

Elimina el inicio de sesión almacenado:

```bash
npx @openai/codex-security logout

Guarda una clave de API proporcionándola mediante stdin:

```bash
printenv OPENAI_API_KEY | npx @openai/codex-security login --with-api-key

Guarda un token de acceso empresarial:

```bash
printenv CODEX_ACCESS_TOKEN | npx @openai/codex-security login --with-access-token

Inspecciona los metadatos de solo lectura del SDK y del complemento incluido:

```bash
npx @openai/codex-security info --json

Al exponer la CLI como un servidor MCP, `info` es el único comando disponible.
Los análisis, las exportaciones, la publicación, el inicio de sesión, la validación y la aplicación de parches siguen disponibles únicamente en la CLI.

## Leer la salida del análisis

De forma predeterminada, los análisis envían a stderr el progreso, los resúmenes de finalización y los errores,
sin escribir el resultado completo del análisis en stdout. Especifica `--json`,
`--format` o `--full-output` para enviar los resultados estructurados del análisis a stdout.

Las terminales interactivas muestran un panel en tiempo real con la fase actual del análisis,
los archivos revisados, la actividad, el uso de tokens y el costo estimado. En CI y con la salida
redirigida, el progreso se muestra como texto sin formato. Agrega `--headless` para mostrar el progreso como texto sin formato en
una terminal interactiva:

```bash
npx @openai/codex-security scan . --headless

El panel también muestra detalles de la sesión en tiempo real. La información sensible no se oculta y los detalles pueden
contener código fuente o credenciales. Revísalos antes de compartirlos.

### Diagnósticos detallados

Agrega `--verbose` para imprimir en stderr diagnósticos del ciclo de vida, la autenticación, el progreso y el
costo con los datos sensibles ocultos:

```bash
npx @openai/codex-security scan . --verbose

Configura `CODEX_SECURITY_LOG_LEVEL=debug` para habilitar los mismos diagnósticos sin la
opción. `LOG_LEVEL=debug` también habilita los diagnósticos cuando
`CODEX_SECURITY_LOG_LEVEL` no está configurado.

### Resumen de finalización

Un análisis completado escribe en stderr la cantidad de hallazgos abiertos del repositorio, el desglose por gravedad,
la cobertura, el tiempo transcurrido, la ruta del informe y el directorio de resultados. También
incluye el uso de tokens y el costo estimado cuando están disponibles:

```text
  REPORT    /path/to/scan/report.md

  FINDINGS  4 (3 confirmed this scan; 1 previously found; 1 critical, 2 high, 1 informational)
  COVERAGE  complete
  ELAPSED   1s
  TOKENS    1,250 input, 200 cached, 30 output
  RESULTS   /path/to/scan

Los hallazgos informativos se incluyen en el total del resumen. Las políticas de gravedad
solo evalúan los hallazgos `critical`, `high`, `medium` y `low` del análisis
actual, no los hallazgos anteriores que aparecen en el total del repositorio.

### Salida JSON

`scan --json` escribe un documento JSON completo en stdout. Su estructura de nivel
superior es:

```text
manifest
repositoryFindings
findings
coverage
scanDir
threadId
reportPath
artifactsDir
sarifPath
cost
turn
  id
  status
  durationMs
  finalResponse
  usage

Al [aplicar parches](#patch-findings-after-a-scan), la salida JSON también incluye los
resultados de los parches y cualquier Pull Request creado.

El progreso, los resúmenes de finalización, los avisos de archivado y los errores permanecen en stderr.
Un análisis completado imprime igualmente el resultado JSON completo cuando una política de gravedad
devuelve el código de salida `1` o la cobertura incompleta devuelve el código de salida `2`.

  `codex-security scan --json` genera un documento JSON. `codex exec --json`
  genera un flujo de eventos JSON Lines. Usa el formato de salida que corresponda al
  comando que ejecutes.

## Artefactos del análisis

Un análisis completado conserva juntos el informe legible y los artefactos estructurados:

```text
<scan-directory>/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

Los archivos estructurados cumplen funciones diferentes:

| Archivo                    | Contenido                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `scan-manifest.json`    | Identidad, estado, objetivo, alcance y productor del análisis, además de registros de artefactos sellados.                                                    |
| `findings.json`         | Identificadores de hallazgos, gravedad, confianza, taxonomía, ubicaciones, evidencia, validación, flujo de datos, alcanzabilidad y remediación. |
| `coverage.json`         | Superficies revisadas, exclusiones, trabajo pospuesto, preguntas abiertas y exhaustividad de la cobertura.                                        |
| `report.md`             | Informe legible del análisis.                                                                                                           |
| `artifacts/`            | Artefactos complementarios del análisis.                                                                                                      |
| `exports/results.sarif` | SARIF generado durante el análisis, si está disponible.                                                                                  |

La exhaustividad de la cobertura tiene tres valores:

- `complete`: el análisis registra una cobertura completa del alcance seleccionado.
- `partial`: el análisis registra trabajo pospuesto u otras limitaciones de cobertura.
- `unknown`: el análisis indica que se desconoce la exhaustividad de la cobertura.

Revisa las superficies cuyo análisis se pospuso, las exclusiones explícitas y las preguntas abiertas antes de usar
la cobertura como evidencia para tomar una decisión de seguridad.

## Códigos de salida y señales

La CLI usa estos códigos de salida:

| Salida  | Condición                                                                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`   | Un análisis finalizó con cobertura completa y cumplió su política de gravedad, un análisis masivo o una publicación finalizó sin errores, u otro comando se ejecutó correctamente.                  |
| `1`   | Un análisis completado informa un hallazgo cuya gravedad es igual o superior a la configurada.                                                                                                       |
| `2`   | La CLI detectó un error de entrada, de ejecución o de exportación, un análisis tiene cobertura incompleta, un análisis masivo incluye repositorios con errores o una publicación presenta errores en uno o más hallazgos. |
| `130` | Ctrl-C interrumpió un análisis o una publicación.                                                                                                                                     |
| `143` | SIGTERM finalizó un análisis o una publicación.                                                                                                                                     |

Cualquier análisis con cobertura `partial` o `unknown` devuelve `2`, incluso sin una
política de gravedad. Cuando solicitas una salida estructurada, los análisis completados y las
publicaciones parciales igualmente escriben los resultados disponibles en stdout. La CLI
imprime la ubicación de cualquier salida parcial después de una interrupción o de un error
de ejecución.

## Permisos de los análisis locales

Los análisis de la CLI y el SDK se ejecutan con los permisos de tu sistema operativo local. Cada análisis
utiliza el perfil del sistema de archivos `codex_security_scan` y establece `approvalPolicy` en
`"never"`. El perfil permite leer el sistema de archivos local y escribir en las
raíces del espacio de trabajo y en el directorio seleccionado para el estado del análisis. Los análisis no se detienen para
solicitar una aprobación interactiva.

La configuración proporcionada mediante `--codex` en la CLI o `codexOverrides` en el SDK, incluidos
`approval_policy`, `sandbox_mode` y los permisos del sistema de archivos, no puede reemplazar
ni restringir estos controles de análisis. Las restricciones del Host y de la red siguen vigentes.

Los procesos de análisis y del entorno de trabajo pueden heredar tu entorno, incluidos tokens
de API y credenciales de la nube no relacionados. Analiza únicamente repositorios en los que
confíes y que tengas permiso para evaluar, y proporciona solo las credenciales que requiere el análisis.

## Autenticación y requisitos previos

Configura `OPENAI_API_KEY` o `CODEX_API_KEY`, inicia sesión con
`npx @openai/codex-security login` o usa un inicio de sesión de Codex existente almacenado en un
archivo. Para OpenRouter o Fireworks, configura la clave de API del proveedor y selecciona un
modelo. Para Amazon Bedrock, usa una clave de API de Bedrock o la cadena estándar de
credenciales de AWS.

Para seleccionar las credenciales, consulta [Seleccionar la autenticación del
análisis](#select-scan-authentication).

Para CI, limita el alcance de la clave de API al paso del análisis y usa un flujo de trabajo de confianza.

La CLI requiere Node.js 22 (22.13.0 o posterior), 24 o 26. Los análisis, los análisis masivos,
las exportaciones, el historial de análisis y los hallazgos guardados también requieren Python 3.10 o posterior.
Python 3.10 también requiere `tomli`. Usa `--python` con `scan`, `bulk-scan` o
`export`, o configura `PYTHON` para cualquier comando basado en Python.

Continúa con el [inicio rápido de la CLI](/es-419/codex/security/cli), la [guía de análisis
masivos](/es-419/codex/security/cli/bulk-scans), las [preguntas frecuentes sobre la CLI](/es-419/codex/security/cli/faq), la [guía de
CI](/es-419/codex/security/cli/ci) o la [guía del SDK de TypeScript](/es-419/codex/security/sdk).
