<!-- source: https://learn.chatgpt.com/es-419/docs/security/cli -->

Codex Security ayuda a los equipos de seguridad e ingeniería a detectar, confirmar y corregir
vulnerabilidades. Usa su interfaz de línea de comandos (CLI) para analizar
repositorios que te pertenezcan o que tengas permiso para evaluar, revisar los hallazgos a lo largo del tiempo
y comprobar los cambios antes de que se integren.

  El paquete `@openai/codex-security` es público. Para ejecutar análisis, necesitas acceso a Codex
  Security. Para realizar un análisis interactivo en Codex, comienza con el [inicio rápido del complemento de Codex
  Security](/es-419/codex/security/plugin). Para los repositorios de GitHub
  conectados, consulta la [configuración de Codex Security en la nube](/es-419/codex/security/setup).

## Comprobar los requisitos previos

La CLI requiere Node.js 22 (22.13.0 o una versión posterior), 24 o 26. Los análisis, los análisis en lote,
las exportaciones, el historial de análisis y los hallazgos guardados también requieren Python 3.10 o una versión posterior.
Para obtener más detalles, consulta [Autenticación y
requisitos previos](/es-419/codex/security/cli/reference#authentication-and-prerequisites).

## Configurar y verificar la CLI

Ejecuta la CLI con `npx` y comprueba su versión:

```bash
npx @openai/codex-security --version

Para consultar tanto la versión del paquete como la del complemento incluido, ejecuta:

```bash
npx @openai/codex-security info --json

Consulta las [versiones de la CLI y el SDK](https://github.com/openai/codex-security/releases)
para conocer los cambios del paquete.

Enumera los comandos disponibles:

```bash
npx @openai/codex-security --help

Consulta también la [referencia de la CLI](/es-419/codex/security/cli/reference).

## Iniciar sesión

Para uso local, inicia sesión con tu cuenta de ChatGPT:

```bash
npx @openai/codex-security login

En una máquina remota o sin interfaz gráfica, usa la autenticación mediante dispositivo:

```bash
npx @openai/codex-security login --device-auth

Para CI y otros flujos de trabajo automatizados, configura una clave de API de OpenAI:

```bash

Para las credenciales de AWS, consulta la [configuración
de Amazon Bedrock](/es-419/codex/security/cli/reference#use-amazon-bedrock). Para [OpenRouter o
Fireworks](/es-419/codex/security/cli/reference#use-openrouter-or-fireworks), configura la
clave de API del proveedor y selecciona un modelo con `--provider` y `--model`.

Para usar el inicio de sesión de ChatGPT cuando también haya una clave de API configurada, selecciónalo explícitamente:

```bash
npx @openai/codex-security scan . --auth chatgpt

Para exigir la clave de API del entorno, selecciona la autenticación con clave de API:

```bash
npx @openai/codex-security scan . --auth api-key

Según tu cuenta y tu repositorio, los análisis de todo el repositorio también pueden
requerir [Trusted Access for Cyber](https://chatgpt.com/cyber).

## Preparar un análisis

Elige un repositorio en el que confíes y que tengas permiso para evaluar. Los análisis usan tus
permisos locales del sistema operativo y no se detienen para solicitar aprobación. Los procesos
de análisis pueden heredar tu entorno, así que elimina las credenciales no relacionadas antes
de comenzar. Consulta [Permisos para análisis
locales](/es-419/codex/security/cli/reference#local-scan-permissions).

Elige un directorio fuera del repositorio para los resultados del análisis:

```bash
REPOSITORY=/path/to/repository
SCAN_DIR=/path/outside/repository/codex-security-results

Si omites `--output-dir`, Codex Security guarda los resultados en su propio directorio de estado
persistente. Los resultados pueden incluir fragmentos de código fuente y detalles de vulnerabilidades,
así que elige una ubicación privada y una política de retención adecuada.

Si el directorio de estado predeterminado no admite escritura, selecciona un directorio con permisos de escritura
fuera del repositorio analizado:

```bash

Verifica el repositorio, el objetivo y el directorio de salida antes de iniciar un análisis:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --dry-run

La ejecución de prueba verifica los datos de entrada locales, incluidas las rutas de `--knowledge-base`,
sin iniciar Codex, cargar credenciales ni comprobar el intérprete de Python
del complemento.

## Ejecutar tu primer análisis

Ejecuta un análisis estándar y conserva sus resultados en el directorio seleccionado:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR"

Las terminales interactivas muestran un panel del análisis en tiempo real. Agrega `--headless` para mostrar
líneas de progreso en texto sin formato en su lugar. CI y las terminales sin una sesión interactiva
usan automáticamente el progreso en texto sin formato.

El panel también muestra detalles de la sesión en tiempo real. Estos pueden contener código fuente
o credenciales, así que revísalos antes de compartirlos.

De forma predeterminada, la CLI escribe el progreso del análisis y su resumen de finalización en stderr.
No imprime el resultado completo del análisis en stdout. Cuando finaliza un análisis, se imprime un
resumen como este:

```text
  REPORT    /path/outside/repository/codex-security-results/report.md

  FINDINGS  2 (2 confirmed this scan; 0 previously found; 1 high, 1 medium)
  COVERAGE  complete
  ELAPSED   42s
  RESULTS   /path/outside/repository/codex-security-results

El uso de tokens y el costo estimado se muestran cuando están disponibles. Para imprimir el resultado
completo como JSON legible por máquinas, solicita explícitamente una salida estructurada:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --json

De forma predeterminada, los análisis solo generan informes, por lo que los hallazgos quedan disponibles para su revisión
local. Quizás te convenga agregar un umbral de gravedad cuando tengas todo listo para [ejecutar análisis en
CI](/es-419/codex/security/cli/ci).

## Elegir un modelo y un nivel de esfuerzo de razonamiento

De forma predeterminada, los análisis usan `gpt-5.6-sol` con un nivel de esfuerzo de razonamiento `xhigh`. Selecciona un
modelo y un nivel de esfuerzo diferentes cuando la tarea los requiera:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --model gpt-5.6-terra \
  --effort high

Los niveles de esfuerzo admitidos son `minimal`, `low`, `medium`, `high`, `xhigh` y
`max`.

## Revisar los resultados

Abre `report.md` para consultar el resultado en un formato legible. El directorio del análisis también contiene los
archivos estructurados que se usan en la automatización:

```text
codex-security-results/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

- `scan-manifest.json` registra el objetivo, el alcance, el productor y los artefactos
  sellados.
- `findings.json` registra la gravedad, el nivel de confianza, las ubicaciones, la evidencia y las medidas de
  remediación de cada hallazgo.
- `coverage.json` registra las superficies revisadas, las exclusiones, el trabajo postergado, las preguntas
  abiertas y la integridad de la cobertura.

La cobertura puede ser `complete`, `partial` o `unknown`. Revisa las áreas postergadas o las
preguntas abiertas antes de considerar el análisis como evidencia de una revisión.
La [referencia de la CLI](/es-419/codex/security/cli/reference#scan-artifacts) describe
el contrato completo de los artefactos y la salida.

## Revisar hallazgos y aplicar parches

Después de un análisis interactivo completo con hallazgos, la CLI ofrece un
explorador de hallazgos. Revisa la evidencia y elige qué hallazgos corregir. Puedes encontrar
las tareas guardadas en la App de escritorio de Codex.

Para aplicar parches a los hallazgos de gravedad alta y crítica sin el explorador:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --patch --patch-severity high --json

Agrega `--create-pr` para crear un commit con los parches verificados y abrir una Pull Request en GitHub.

También puedes aplicar parches a los hallazgos guardados o importar incidencias de Linear. Consulta la
[referencia de `validate` y `patch`](/es-419/codex/security/cli/reference#codex-security-validate-and-codex-security-patch).

## Elegir el siguiente análisis

Usa un análisis de ruta cuando un repositorio contenga servicios o paquetes independientes:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --path services/billing \
  --path packages/auth

Revisa los cambios incluidos en commits entre la revisión base y `HEAD`:

```bash
npx @openai/codex-security scan "$REPOSITORY" --diff origin/main --head HEAD

Revisa los cambios preparados y no preparados con respecto a `HEAD`:

```bash
npx @openai/codex-security scan "$REPOSITORY" --working-tree --base HEAD

Los análisis de diferencias y del árbol de trabajo requieren que el argumento del repositorio sea la raíz del
worktree de Git. Obtén las revisiones seleccionadas antes de iniciar un análisis de diferencias.

Usa el modo profundo cuando un repositorio o una ruta requieran una revisión más amplia:

```bash
npx @openai/codex-security scan "$REPOSITORY" --mode deep

Para controlar los procesos de trabajo, los subagentes y cuándo se detiene el análisis:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

Estas opciones requieren el modo profundo, que admite repositorios y rutas como objetivos,
pero no análisis de diferencias ni del árbol de trabajo. Aquí, `--workers` controla procesos independientes
de análisis estándar dentro de un mismo análisis; `bulk-scan --workers` controla análisis simultáneos
de repositorios. `--max-time-hours` acepta un número positivo de hasta `96`,
incluidas las fracciones de hora. Al llegar al límite, el análisis detiene los procesos que no finalizaron,
conserva los resultados de los análisis completados y los integra en el informe final.

## Agregar contexto de arquitectura y seguridad

Proporciona documentos de arquitectura, modelos de amenazas o políticas de seguridad como contexto
del análisis. Esto ayuda a Codex Security a evaluar los hallazgos según cómo funciona realmente
tu sistema:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

## Agregar instrucciones personalizadas al análisis

Agrega instrucciones que centren el análisis en tus prioridades de seguridad. Usa un
segundo archivo para las instrucciones de seguimiento:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --scan-prompt-file /path/to/scan.md \
  --post-scan-prompt-file /path/to/follow-up.md

El seguimiento se ejecuta en la misma sesión autenticada después de los análisis exitosos
y de los análisis con cobertura incompleta o errores. Si el seguimiento falla, la CLI
muestra una advertencia y conserva el análisis completado. No se ejecuta después de una
cancelación ni de un análisis que alcanza su límite de costo. Ambas opciones también funcionan
con `bulk-scan`; una columna `prompt` en el CSV agrega instrucciones específicas para cada repositorio.

## Establecer un presupuesto para el análisis

Usa `--max-cost` para detener un análisis cuando el costo estimado del modelo supere un límite
en USD:

```bash
npx @openai/codex-security scan "$REPOSITORY" --max-cost 5

Las solicitudes que ya están en curso pueden finalizar con un costo ligeramente superior al límite. Si un análisis
profundo alcanza el límite después de que Codex Security integra los resultados de los procesos de trabajo
completados, la CLI guarda el informe finalizado, marca su cobertura como `partial`
y devuelve el código de salida `2`. Si el análisis no puede generar un informe finalizado,
cualquier salida parcial disponible permanece en el disco.

## Analizar los cambios antes de cada commit

Instala una verificación de seguridad pre-commit de Git en tu repositorio:

```bash
npx @openai/codex-security install-hook

La verificación analiza los cambios preparados y no preparados antes de cada commit. Bloquea
los hallazgos de gravedad alta y los errores de análisis sin reemplazar un script
pre-commit existente.

## Analizar repositorios en lote

Inicia sesión en GitHub antes de descubrir repositorios:

```bash
gh auth login

Descubre y selecciona repositorios de tu cuenta u organización de GitHub:

```bash
npx @openai/codex-security bulk-scan

El flujo interactivo excluye los repositorios archivados y los forks. Te pide
confirmar los repositorios seleccionados antes de analizarlos.

Para analizar una lista preparada de repositorios, proporciona un archivo CSV y un directorio de salida:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Vuelve a ejecutar el mismo comando para reanudar un análisis en lote existente. Codex Security
omite los repositorios completados. Agrega `--max-attempts 3` para volver a intentarlo si ocurren
errores temporales en el repositorio o durante el análisis.

Para obtener información sobre el descubrimiento en GitHub, la preparación de archivos CSV, los resultados de campañas y la configuración de Docker, consulta
[Ejecuta análisis de seguridad en lote](/es-419/codex/security/cli/bulk-scans).

## Ejecutar análisis en lote en Docker

Si tu acceso incluye la imagen de Docker de Codex Security, usa la configuración
reforzada de Compose y el perfil de seguridad proporcionados en un host de Docker con Linux.
El host debe admitir la creación de espacios de nombres de usuario sin privilegios. Proporciona un archivo
CSV de repositorios, conserva los resultados y el estado de inicio de sesión en directorios montados persistentes y
proporciona las credenciales mediante tu entorno o un administrador de secretos:

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

El contenedor ejecuta análisis en lote sin prompts interactivos. Usa la CLI fuera de
Docker cuando quieras descubrir repositorios de forma interactiva. Para los repositorios
privados, proporciona `GH_TOKEN` o `GITHUB_TOKEN` mediante tu entorno o un
administrador de secretos. Los [requisitos de inicio de sesión](#sign-in), incluido el acceso a la cuenta y
al repositorio, también se aplican a los análisis en contenedores.

## Volver a consultar un análisis guardado

Muestra los análisis guardados de tu repositorio:

```bash
npx @openai/codex-security scans list "$REPOSITORY"

Copia el ID de un análisis de los resultados para inspeccionar sus hallazgos y su configuración:

```bash
npx @openai/codex-security scans show SCAN_ID

Para inspeccionar los eventos guardados de un análisis y de sus procesos de trabajo:

```bash
npx @openai/codex-security scans logs SCAN_ID

Los registros guardados no están censurados y pueden contener código fuente o credenciales.
Revísalos antes de compartirlos.

Muestra los hallazgos abiertos de los análisis del repositorio:

```bash
npx @openai/codex-security findings list "$REPOSITORY"

Un hallazgo anterior permanece abierto cuando el análisis más reciente no lo confirma.

Para marcar un hallazgo revisado como falso positivo, explica por qué el hallazgo no
es aplicable:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The route already checks permissions"

Los análisis posteriores tienen en cuenta esa explicación, pero aun así vuelven a revisar el código actual.

Ejecuta el mismo análisis sobre el checkout actual con su configuración original:

```bash
npx @openai/codex-security scans rerun SCAN_ID

Compara dos análisis para encontrar hallazgos nuevos, persistentes, reabiertos, resueltos o
desconocidos:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

La comparación empareja automáticamente los hallazgos según su causa raíz y reutiliza
las coincidencias guardadas.

Para conocer el formato CSV de los análisis en lote, los filtros del historial de análisis y las opciones de los comandos, consulta
la [referencia de la CLI](/es-419/codex/security/cli/reference).

Continúa con el flujo de trabajo que se adapte a tu objetivo:

- [Ejecuta análisis de seguridad en lote](/es-419/codex/security/cli/bulk-scans) para descubrir repositorios de GitHub
  o analizar un inventario CSV fijado.
- [Lee las preguntas frecuentes de la CLI](/es-419/codex/security/cli/faq) para obtener respuestas sobre el historial de análisis,
  los comentarios sobre falsos positivos, la cobertura y la verificación de correcciones.
- [Ejecuta análisis en CI](/es-419/codex/security/cli/ci) para revisar pull requests, conservar
  los resultados y establecer una política de gravedad.
- [Usa la referencia de la CLI](/es-419/codex/security/cli/reference) para consultar todas las opciones,
  los formatos de salida, los artefactos y los códigos de salida.
- [Integra el SDK de TypeScript](/es-419/codex/security/sdk) para ejecutar análisis desde una
  aplicación o una herramienta de desarrollo.
