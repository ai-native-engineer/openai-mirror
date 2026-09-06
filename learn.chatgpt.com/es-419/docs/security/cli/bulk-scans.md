<!-- source: https://learn.chatgpt.com/es-419/docs/security/cli/bulk-scans -->

Usa `npx @openai/codex-security bulk-scan` para revisar repositorios en una sola
campaña. Descubre repositorios de tu cuenta personal de GitHub o de una
organización, o proporciona un CSV que fije cada repositorio en una revisión
exacta de Git.

  El paquete `@openai/codex-security` es público. Para ejecutar análisis, necesitas
  acceso a Codex Security. Sigue el [inicio rápido de la CLI](/es-419/codex/security/cli) para instalar
  la CLI e iniciar sesión.

## Elegir el origen de los repositorios

| Origen           | Cuándo usarlo                                                                          |
| ---------------- | --------------------------------------------------------------------------------------- |
| Descubrimiento en GitHub | Elige de forma interactiva repositorios de tu cuenta personal de GitHub o de una organización. |
| Inventario CSV    | Ejecuta una campaña automatizada y repetible con revisiones exactas de los repositorios.                |

Ambos flujos de trabajo guardan el progreso, conservan los resultados de cada repositorio y te permiten
reanudar una campaña después de una interrupción.

## Descubrir repositorios de GitHub

Inicia sesión con GitHub CLI:

```bash
gh auth login

Inicia un análisis en lote interactivo:

```bash
npx @openai/codex-security bulk-scan

La CLI te guía por estos pasos:

1. Elige tu cuenta personal de GitHub o una organización.
2. Revisa los repositorios con actividad en los últimos 90 días.
3. Busca en la lista de repositorios y selecciona cuáles analizar.
4. Elige un directorio para los resultados de los análisis.
5. Revisa los repositorios seleccionados y confirma la campaña.

El descubrimiento excluye los repositorios archivados y los forks. La CLI registra el commit exacto
de la rama predeterminada de cada repositorio seleccionado en
`<output-directory>/repositories.csv`. Ningún análisis comienza hasta que confirmes
la selección.

Para usar GitHub Enterprise Server, primero inicia sesión en tu host de GitHub:

```bash
gh auth login --hostname github.example.com

Configura `GH_HOST` al iniciar el descubrimiento de repositorios:

```bash
GH_HOST=github.example.com npx @openai/codex-security bulk-scan

El descubrimiento interactivo requiere una terminal. Para CI, contenedores o una lista preparada de
repositorios, usa un inventario CSV.

## Crear un CSV de repositorios

Crea un CSV con una fila por cada repositorio y su revisión fijada:

```csv
id,repository,revision,scope,mode,prompt
payments,https://github.com/example/payments.git,0123456789abcdef0123456789abcdef01234567,services/api,standard,Review payment authorization and refunds.
identity,https://github.com/example/identity.git,fedcba9876543210fedcba9876543210fedcba98,,deep,Review session and identity boundaries.

El CSV admite estas columnas:

| Columna       | Obligatoria | Descripción                                                                                                |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------------- |
| `id`         | Sí      | Identificador único del repositorio. Usa letras, números, puntos, guiones o guiones bajos.                      |
| `repository` | Sí      | URL HTTPS, URL SSH o ruta de acceso a un repositorio local. Las rutas relativas se resuelven desde el directorio del CSV.               |
| `revision`   | Sí      | SHA completo del commit de Git, de 40 o 64 caracteres. No se admiten nombres de ramas, etiquetas ni hashes de commit abreviados. |
| `scope`      | No       | Directorio relativo al repositorio que se analizará. Omite el valor para analizar todo el repositorio.                       |
| `mode`       | No       | `standard` o `deep`. Omite el valor para usar el modo seleccionado en el comando.                                   |
| `prompt`     | No       | Instrucciones de análisis específicas para este repositorio.                                                             |

Para encontrar el SHA completo del commit de un repositorio local, ejecuta:

```bash
git -C /path/to/repository rev-parse HEAD

## Ejecutar una campaña desde un CSV

Proporciona el CSV y un directorio de salida privado ubicado fuera de los repositorios:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

`--workers` controla los análisis simultáneos de repositorios y su valor predeterminado es `4`. No
establece la cantidad de workers independientes de análisis estándar dentro de cada análisis profundo;
configura esos límites mediante
[`[deep_scan]`](/es-419/codex/security/cli/reference#configure-deep-scans). Usa `--mode
deep` para seleccionar el análisis profundo en las filas que no tengan su propio `mode`. Cada fila del CSV
puede elegir su propio modo de análisis y alcance dentro del repositorio.

Configura `[deep_scan].max_time_hours` para limitar la ejecución de los workers en cada análisis profundo de la
campaña. La opción `--max-time-hours` funciona con `scan`, no con `bulk-scan`.

La CLI hace checkout de cada revisión fijada, analiza el objetivo seleccionado, registra el
resultado y elimina el checkout temporal del repositorio. Un repositorio solo se considera
completo cuando el análisis tiene cobertura completa y existen todos los artefactos de
resultados requeridos.

## Compartir el contexto y las instrucciones de seguridad

Agrega documentos de arquitectura, modelos de amenazas o políticas de seguridad a cada análisis
con `--knowledge-base`. Repite la opción para agregar más archivos o directorios:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Para agregar instrucciones de análisis compartidas o ejecutar un seguimiento después de cada análisis,
proporciona archivos de prompts:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --scan-prompt-file scan-instructions.md \
  --post-scan-prompt-file follow-up.md

La CLI agrega el `prompt` del CSV de cada repositorio después de las instrucciones de análisis
compartidas. Las instrucciones de seguimiento se ejecutan en la misma sesión autenticada
después de los análisis exitosos y de aquellos con cobertura incompleta o errores, pero no
después de una cancelación ni de un análisis que alcance su límite de costo. Las rutas de los archivos de prompts
se resuelven desde el directorio actual.

## Elegir un modelo y un nivel de esfuerzo de razonamiento

De forma predeterminada, los análisis en lote usan `gpt-5.6-sol` con el nivel de esfuerzo de razonamiento `xhigh`. Para
elegir otro modelo y otro nivel de esfuerzo para una campaña con CSV:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --model gpt-5.6-terra \
  --effort high

Las mismas opciones funcionan durante el descubrimiento interactivo de repositorios:

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

Los niveles de esfuerzo admitidos son `minimal`, `low`, `medium`, `high` y `xhigh`.

Para usar OpenRouter o Fireworks, configura `OPENROUTER_API_KEY` o `FIREWORKS_API_KEY`,
respectivamente, y especifica `--provider` y `--model`. Para ver las credenciales y
ejemplos, consulta la [configuración de OpenRouter o
Fireworks](/es-419/codex/security/cli/reference#use-openrouter-or-fireworks) o la [configuración de
Amazon Bedrock](/es-419/codex/security/cli/reference#use-amazon-bedrock).

## Revisar los resultados de la campaña

El directorio de salida contiene la campaña fijada, un registro de resultados que solo permite agregar entradas
y artefactos separados para cada repositorio e intento:

```text
security-scans/
├── manifest.json
├── results.jsonl
├── checkouts/
└── artifacts/
    ├── payments/
    │   └── attempt-1/
    │       ├── scan-manifest.json
    │       ├── findings.json
    │       ├── coverage.json
    │       └── report.md
    └── identity/
        └── attempt-1/
            ├── scan-manifest.json
            ├── findings.json
            ├── coverage.json
            └── report.md

- `manifest.json` registra los repositorios, las revisiones fijadas, los alcances, los modos de análisis
  y las instrucciones compartidas o específicas de cada repositorio de la campaña.
- `results.jsonl` registra cada intento por repositorio, su estado, el directorio de
  artefactos y cualquier detalle disponible sobre costos o errores.
- `report.md` proporciona un informe legible correspondiente a un intento de análisis de un repositorio.
- `findings.json` y `coverage.json` registran los hallazgos de ese intento y el
  alcance revisado.

Exporta un análisis de repositorio finalizado cuando necesites un resultado portátil:

```bash
npx @openai/codex-security export \
  /path/outside/repositories/security-scans/artifacts/payments/attempt-1 \
  --export-format sarif \
  --output /path/outside/repositories/payments.sarif

Los resultados pueden contener fragmentos de código fuente y detalles de vulnerabilidades. Mantén el
directorio de salida privado, fuera de los repositorios analizados y sujeto a una
política de retención adecuada.

## Reanudar una campaña

Ejecuta el comando original con el mismo CSV y el mismo directorio de salida:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

La CLI reanuda los análisis de repositorios sin terminar y omite los que ya se completaron. Los análisis
con cobertura incompleta no se reintentan. Sus resultados siguen disponibles y
el comando finaliza con el código `2`.

No cambies el inventario de repositorios ni las instrucciones de análisis y seguimiento para
un directorio de salida existente. La CLI verifica el archivo de manifiesto fijado y rechaza una
campaña diferente. Usa un nuevo directorio de salida cuando cambies los repositorios,
las revisiones, los alcances, los modos de análisis o las instrucciones compartidas o específicas de cada repositorio.

## Reintentar repositorios con errores

Usa `--max-attempts` para reintentar un repositorio tras un error temporal de checkout o de
análisis:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

De forma predeterminada, se realiza un intento por repositorio. Cada intento tiene su propio
comprobante y directorio de artefactos. Los reintentos abarcan los errores de checkout, las fallas de análisis
y la falta de artefactos requeridos. Los análisis completados con cobertura incompleta
no se reintentan.

Los análisis en lote usan estos códigos de salida:

| Código de salida | Significado                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| `0`       | El análisis de cada repositorio se completó correctamente.                                                                              |
| `2`       | No se pudo completar el análisis de un repositorio, un análisis tuvo cobertura incompleta o el comando encontró un error de entrada o de ejecución. |
| `130`     | Ctrl-C interrumpió la campaña.                                                                                      |
| `143`     | SIGTERM finalizó la campaña.                                                                                      |

## Ejecuta análisis en lote en Docker

El [repositorio de
Codex Security](https://github.com/openai/codex-security) incluye una configuración reforzada de
Compose para campañas automatizadas con CSV en un host de Docker con Linux. El
host debe admitir la creación de espacios de nombres de usuario sin privilegios.

Mantén el CSV de repositorios, los resultados de los análisis y el estado de inicio de sesión montados en directorios
persistentes. Proporciona las credenciales de OpenAI mediante el entorno o un administrador de
secretos. Para los repositorios privados de GitHub, proporciona `GH_TOKEN` o `GITHUB_TOKEN`
de la misma manera.

Ejecuta la imagen con el CSV y el directorio de salida montados:

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

Usa el mismo CSV y el mismo directorio de salida montados para reanudar la campaña. Para
GitHub Enterprise Server, configura `CODEX_SECURITY_GIT_HOST` con tu host de GitHub.

Para conocer todos los flags disponibles, consulta la [referencia del comando
bulk-scan](/es-419/codex/security/cli/reference#codex-security-bulk-scan). Para resolver dudas frecuentes
sobre la cobertura de los análisis y sus hallazgos, consulta las [Preguntas frecuentes de la
CLI](/es-419/codex/security/cli/faq).
