<!-- source: https://learn.chatgpt.com/es-419/docs/security/cli/faq -->

Encuentra respuestas a preguntas frecuentes sobre cómo analizar repositorios y gestionar
hallazgos de seguridad desde la terminal. Para la instalación y un primer análisis, comienza
con el [inicio rápido de la CLI](/es-419/codex/security/cli).

## Análisis de repositorios

### Quién puede usar la CLI

El paquete `@openai/codex-security` es público.

Para ejecutar análisis, se requiere acceso a Codex Security. Para obtener mejores resultados, usa una cuenta
verificada para [Trusted Access for Cyber](https://chatgpt.com/cyber).

### Por qué un análisis usa una clave de API después de iniciar sesión

Cuando tu entorno incluye `OPENAI_API_KEY` o `CODEX_API_KEY`, los análisis
sin una terminal interactiva y los análisis JSON y JSONL usan de forma predeterminada la clave de API
del entorno, incluso después de iniciar sesión correctamente con ChatGPT o con un token de acceso.
Los análisis interactivos con salida de texto te piden que elijas cuando también está disponible
el inicio de sesión con ChatGPT. Las ejecuciones de prueba no muestran solicitudes ni cargan credenciales.

Para usar tus credenciales almacenadas en un análisis, selecciónalas explícitamente:

```bash
npx @openai/codex-security scan . --auth chatgpt

Para exigir una clave de API de `OPENAI_API_KEY` o `CODEX_API_KEY`:

```bash
npx @openai/codex-security scan . --auth api-key

Para que tus credenciales almacenadas se usen automáticamente de forma predeterminada, ejecuta
`unset OPENAI_API_KEY CODEX_API_KEY`. Para conocer todos los modos de autenticación compatibles,
consulta la [referencia de la CLI](/es-419/codex/security/cli/reference#select-scan-authentication).

### Cómo funciona el análisis de repositorios en lote

Inicia sesión con GitHub CLI:

```bash
gh auth login

Busca y selecciona repositorios de una cuenta u organización de GitHub:

```bash
npx @openai/codex-security bulk-scan

Si ya tienes una lista preparada, proporciona un archivo CSV de repositorios y un directorio de salida:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Consulta [Ejecutar análisis de seguridad en lote](/es-419/codex/security/cli/bulk-scans) para obtener información sobre la detección de repositorios en GitHub,
el formato CSV, los resultados de la campaña y las opciones disponibles.

### Se puede reanudar un análisis en lote interrumpido

Sí. Ejecuta el mismo comando de análisis en lote con el CSV y el directorio de salida originales.
Codex Security omite los repositorios cuyo análisis ya finalizó.

Agrega `--max-attempts 3` para reintentar ante errores temporales del repositorio o del análisis:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

Un análisis completado con cobertura `partial` o `unknown` conserva sus resultados y
hace que la campaña finalice con el código de salida `2`. No se vuelve a intentar, ni siquiera con
`--max-attempts`.

### Cómo puede un análisis usar la arquitectura y las políticas de seguridad

Proporciona documentos de arquitectura, modelos de amenazas o políticas de seguridad con
`--knowledge-base`:

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Codex Security usa estos documentos como contexto para el análisis actual. Para conocer
los tipos de archivos compatibles y el comportamiento de los directorios, consulta [Agregar contexto
de seguridad](/es-419/codex/security/cli/reference#add-security-context).

## Hallazgos y cobertura

### Dónde pueden los equipos encontrar los resultados de análisis anteriores

Muestra los análisis guardados de tu repositorio:

```bash
npx @openai/codex-security scans list /path/to/repository

Usa un ID de análisis incluido en los resultados para inspeccionar sus hallazgos:

```bash
npx @openai/codex-security scans show SCAN_ID

Cada análisis completado conserva en un mismo lugar el informe, los hallazgos, la cobertura y los artefactos
de respaldo. Consulta [Artefactos
del análisis](/es-419/codex/security/cli/reference#scan-artifacts) para ver la estructura completa.

Para inspeccionar los eventos guardados del análisis y de los procesos de trabajo, ejecuta `scans logs SCAN_ID`. Estos registros
no ocultan datos confidenciales y pueden contener código fuente o credenciales.

### Qué ocurre si la CLI no puede guardar el historial de análisis

Codex Security guarda el historial de análisis en una base de datos de trabajo. Si el directorio de estado
predeterminado no tiene permisos de escritura, elige un directorio privado fuera del
repositorio:

```bash

### Cómo distinguen los análisis los hallazgos nuevos de los conocidos

Muestra los hallazgos abiertos de todos los análisis de un repositorio:

```bash
npx @openai/codex-security findings list /path/to/repository

La lista identifica los hallazgos confirmados en el análisis más reciente y los hallazgos abiertos
anteriores que ese análisis no confirmó.

Compara los hallazgos de ambos análisis:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

La comparación asocia automáticamente los hallazgos según su causa raíz, reutiliza las coincidencias guardadas
e identifica hallazgos nuevos, persistentes, reabiertos, resueltos y desconocidos.
Un hallazgo se considera resuelto solo cuando el análisis posterior cubre su objetivo original
y la ruta afectada sin brechas de cobertura.

### Cómo funciona la retroalimentación sobre falsos positivos

Inspecciona el análisis guardado para encontrar el ID de ocurrencia:

```bash
npx @openai/codex-security scans show SCAN_ID

Registra por qué ese hallazgo no corresponde:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

Los análisis futuros del mismo repositorio reciben esa explicación como contexto. Estos
siguen comprobando de forma independiente el código fuente, los controles y la alcanzabilidad actuales. Descartar un
hallazgo no suprime ninguna regla, ruta ni clase de vulnerabilidad.

Para conocer los detalles del comando, consulta la [referencia de
hallazgos](/es-419/codex/security/cli/reference#codex-security-findings).

### Por qué los análisis repetidos pueden devolver hallazgos diferentes

Los análisis asistidos por IA pueden variar, incluso con la misma configuración de análisis. Comienza
por volver a ejecutar el análisis de referencia:

```bash
npx @openai/codex-security scans rerun BASELINE_SCAN_ID

La nueva ejecución conserva la configuración original del análisis y requiere la misma versión del
complemento. Si el complemento instalado cambió, el comando se detiene.

Compara el análisis de referencia con el nuevo análisis:

```bash
npx @openai/codex-security scans compare BASELINE_SCAN_ID REPEAT_SCAN_ID

Proporciona lineamientos comunes de arquitectura y seguridad cuando la falta de contexto pueda
contribuir a la variación. La asociación puede identificar el mismo hallazgo subyacente
en distintas ejecuciones, pero no hace que los análisis sean deterministas. Vuelve a comprobar directamente cualquier
hallazgo importante que desaparezca.

### Cómo puede un equipo confirmar que una corrección funcionó

Después de aplicar una corrección, vuelve a ejecutar el análisis original:

```bash
npx @openai/codex-security scans rerun BEFORE_SCAN_ID

Compara los hallazgos originales con el nuevo análisis:

```bash
npx @openai/codex-security scans compare BEFORE_SCAN_ID AFTER_SCAN_ID

Confirma que el nuevo análisis cubra el objetivo original y la ruta afectada sin
brechas de cobertura. Luego, vuelve a comprobar directamente el hallazgo original en la copia de trabajo
actual:

```bash
npx @openai/codex-security validate /path/to/original/findings.json \
  "Recheck the SQL injection in src/orders.ts:42 against the current code"

Ni la ausencia de un hallazgo ni una comparación de análisis bastan por sí solas para demostrar que una corrección funcionó.

### Qué significa una cobertura incompleta

La cobertura puede ser `complete`, `partial` o `unknown`. Revisa `coverage.json`
para conocer las rutas excluidas, las superficies pendientes y las preguntas abiertas antes de considerar un
análisis como evidencia de una revisión.

Los análisis con cobertura parcial o desconocida devuelven el código de salida `2`, incluso sin una
política de gravedad. Aun así, conservan los hallazgos y la cobertura disponibles. Un análisis posterior
no puede determinar que un hallazgo anterior ya no existe si no
cubre la ruta original de ese hallazgo.

## Automatización y costo

### Cómo funcionan los límites de tiempo de los análisis profundos

Establece un plazo para los procesos de trabajo al iniciar un análisis profundo:

```bash
npx @openai/codex-security scan . --mode deep --max-time-hours 1.5

El valor predeterminado es de `96` horas. Usa cualquier valor positivo de hasta `96`, incluidas
las fracciones. Al cumplirse el plazo, Codex Security detiene los procesos de trabajo que no hayan finalizado, conserva
los resultados de los análisis estándar completados y los incorpora al informe final. Si
ningún proceso de trabajo finaliza la revisión del código fuente, el informe registra una cobertura parcial y la
CLI devuelve el código de salida `2`.

Para configuraciones persistentes o campañas en lote, establece `max_time_hours` en
`[deep_scan]` dentro de la [configuración de análisis
profundos](/es-419/codex/security/cli/reference#configure-deep-scans).

### Cómo funcionan los límites de costo de los análisis

Establece un límite de costo estimado en USD antes de iniciar el análisis:

```bash
npx @openai/codex-security scan . --max-cost 5

El límite es una estimación, no un tope estricto de gasto. Las solicitudes que ya están en
curso pueden finalizar por encima de ese límite. Si un análisis profundo alcanza el límite después
de que Codex Security consolida los resultados de los procesos de trabajo finalizados, la CLI guarda el informe
finalizado con cobertura parcial y termina con el código de salida `2`. De lo contrario, conserva
cualquier resultado parcial disponible.

### Pueden los análisis revisar commits y pull requests

Instala una verificación de seguridad previa al commit para los cambios preparados y sin preparar:

```bash
npx @openai/codex-security install-hook

Para las verificaciones de pull requests, analiza los cambios incluidos en commits y establece un umbral de
gravedad:

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --fail-on-severity high

Un análisis completo devuelve el código de salida `1` cuando detecta un problema de gravedad igual o superior a la
seleccionada. Consulta [Ejecuta análisis en CI](/es-419/codex/security/cli/ci) para conocer el
flujo de trabajo completo de GitHub Actions, el manejo de artefactos y la exportación de SARIF.

### ¿Puede otra aplicación ejecutar análisis directamente?

Sí. Usa el [SDK de TypeScript](/es-419/codex/security/sdk) para iniciar análisis, seleccionar
objetivos, inspeccionar los hallazgos y la cobertura, seguir el progreso y aplicar controles de costos
desde una aplicación o herramienta para desarrolladores.
