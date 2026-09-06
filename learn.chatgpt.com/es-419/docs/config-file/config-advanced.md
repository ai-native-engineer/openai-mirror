<!-- source: https://learn.chatgpt.com/es-419/docs/config-file/config-advanced -->

Usa estas opciones cuando necesites más control sobre los proveedores, las políticas y las integraciones. Para comenzar rápidamente, consulta [Configuración básica](/es-419/codex/config-file/config-basic).

Para obtener más información sobre las instrucciones del proyecto, las capacidades reutilizables, los comandos slash personalizados, los flujos de trabajo de subagentes y las integraciones, consulta [Personalización](/es-419/codex/customization/overview). Para conocer las claves de configuración, consulta [Referencia de configuración](/es-419/codex/config-file/config-reference).

## Perfiles

Los perfiles te permiten guardar capas de configuración con nombre y cambiar entre ellas desde
la CLI. Cuando pasas `--profile profile-name`, Codex carga
`~/.codex/config.toml` y luego superpone `~/.codex/profile-name.config.toml`.
Los nombres de perfil pueden contener letras, números, guiones y guiones bajos.

Crea un archivo TOML distinto para cada perfil. Usa claves de configuración de nivel superior en el
archivo del perfil; no las anides en `[profiles.profile-name]`.

```toml
# ~/.codex/deep-review.config.toml
model = "gpt-5.5"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
model_catalog_json = "/Users/me/.codex/model-catalogs/deep-review.json"

```shell
codex --profile deep-review
codex exec --profile deep-review "review this change"

Como el archivo del perfil es una capa situada por encima de tu configuración base de usuario y por debajo de la
configuración del proyecto y de la CLI, solo necesita los valores que difieren de tu
configuración base. Los archivos de perfil también pueden anular `model_catalog_json`; Codex usa el
valor del perfil cuando ambos archivos lo establecen.

En Codex 0.134.0 y versiones posteriores, `--profile` ya no lee `[profiles.profile-name]`
de `config.toml`, y el selector de nivel superior `profile = "profile-name"` ya no
se admite. Mueve la configuración heredada de los perfiles a
`~/.codex/profile-name.config.toml` y luego elimina la tabla
`[profiles.profile-name]` correspondiente y el selector `profile = "profile-name"` de
`config.toml`.

## Anulaciones puntuales desde la CLI

Además de editar `~/.codex/config.toml`, puedes anular valores de configuración para una sola ejecución desde la CLI:

- Prioriza las opciones específicas cuando estén disponibles; por ejemplo, `--model`.
- Usa `-c` / `--config` cuando necesites anular el valor de cualquier clave.

Ejemplos:

```shell
# Dedicated flag
codex --model gpt-5.6-terra

# Generic key/value override (value is TOML, not JSON)
codex --config model='"gpt-5.6-terra"'
codex --config sandbox_workspace_write.network_access=true
codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'

Notas:

- Las claves pueden usar la notación de puntos para establecer valores anidados; por ejemplo, `mcp_servers.context7.enabled=false`.
- Los valores de `--config` se analizan como TOML. Cuando tengas dudas, coloca el valor entre comillas para evitar que el shell lo divida en los espacios.
- Si el valor no se puede analizar como TOML, Codex lo trata como una cadena.

## Ubicaciones de la configuración y del estado

Codex almacena su estado local en `CODEX_HOME`; el valor predeterminado es `~/.codex`.

Archivos comunes que puedes encontrar allí:

- `config.toml` (tu configuración local)
- `auth.json` (si usas almacenamiento de credenciales basado en archivos) o el llavero/gestor de claves de tu sistema operativo
- `history.jsonl` (si la persistencia del historial está habilitada)
- Otros datos de estado por usuario, como registros y cachés

Para obtener detalles sobre la autenticación, incluidos los modos de almacenamiento de credenciales, consulta [Autenticación](/es-419/codex/auth). Para ver la lista completa de claves de configuración, consulta [Referencia de configuración](/es-419/codex/config-file/config-reference).

Para conocer los valores predeterminados, las reglas y las habilidades compartidos que se incluyen en repositorios o rutas del sistema, consulta [Configuración del equipo](/es-419/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config).

Si solo necesitas dirigir el proveedor de OpenAI integrado a un proxy de LLM, un enrutador o un proyecto con residencia de datos habilitada, establece `openai_base_url` en `config.toml` en lugar de definir un proveedor nuevo. Esto cambia la URL base del proveedor integrado `openai` sin requerir una entrada `model_providers.<id>` independiente.

```toml
openai_base_url = "https://us.api.openai.com/v1"

## Archivos de configuración del proyecto (`.codex/config.toml`)

Además de tu configuración de usuario, Codex lee las anulaciones específicas del proyecto desde archivos `.codex/config.toml` dentro de tu repositorio. Codex recorre la ruta desde la raíz del proyecto hasta tu directorio de trabajo actual y carga cada archivo `.codex/config.toml` que encuentra. Si varios archivos definen la misma clave, tiene prioridad el que esté más cerca de tu directorio de trabajo.

Por seguridad, Codex carga los archivos de configuración específicos del proyecto solo cuando este es de confianza. Si el proyecto no es de confianza, Codex ignora sus capas `.codex/`, incluidos `.codex/config.toml`, los hooks locales del proyecto y las reglas locales del proyecto. Las capas de usuario y del sistema permanecen separadas y se siguen cargando.

Las rutas relativas dentro de la configuración de un proyecto; por ejemplo, `model_instructions_file`, se resuelven en relación con la carpeta `.codex/` que contiene el archivo `config.toml`.

Los archivos de configuración del proyecto no pueden anular opciones que redirijan credenciales, alteren
los metadatos de las solicitudes de la app controlados por el host, cambien la autenticación del proveedor, seleccionen perfiles de configuración
ni ejecuten comandos de notificación o telemetría locales en la máquina. Codex ignora las
siguientes claves en el archivo local del proyecto `.codex/config.toml` y muestra una advertencia
al iniciar cuando las encuentra: `openai_base_url`, `chatgpt_base_url`,
`apps_mcp_product_sku`, `model_provider`, `model_providers`, `notify`,
`profile`, `profiles`, `experimental_realtime_ws_base_url` y `otel`. Configura
las claves de proveedor, notificación y telemetría en tu archivo de nivel de usuario
`~/.codex/config.toml`; selecciona perfiles de configuración con `--profile profile-name`
y `~/.codex/profile-name.config.toml`.

## Hooks

Codex también puede cargar hooks del ciclo de vida desde archivos `hooks.json` o desde tablas
`[hooks]` en línea en archivos `config.toml` ubicados junto a las capas de configuración activas.

En la práctica, estas son las cuatro ubicaciones más útiles:

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

Los hooks locales del proyecto solo se cargan cuando la capa `.codex/` del proyecto es de confianza.
Los hooks de nivel de usuario no dependen de la confianza del proyecto.

Los hooks TOML en línea usan la misma estructura de eventos que `hooks.json`:

```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

Si una misma capa contiene tanto `hooks.json` como `[hooks]` en línea, Codex carga
ambos y muestra una advertencia. Usa una sola representación por capa.

Para conocer la lista actual de eventos, los campos de entrada, el comportamiento de salida y las limitaciones, consulta
[Hooks](/es-419/codex/hooks).

## Roles de los agentes (`[agents]` en `config.toml`)

Para configurar los roles de subagentes (`[agents]` en `config.toml`), consulta [Subagentes](/es-419/codex/agent-configuration/subagents).

## Detección de la raíz del proyecto

Codex detecta la configuración del proyecto; por ejemplo, las capas `.codex/` y `AGENTS.md`, recorriendo los directorios superiores desde el directorio de trabajo hasta encontrar la raíz del proyecto.

De forma predeterminada, Codex considera que un directorio que contiene `.git` es la raíz del proyecto. Para personalizar este comportamiento, establece `project_root_markers` en `config.toml`:

```toml
# Treat a directory as the project root when it contains any of these markers.
project_root_markers = [".git", ".hg", ".sl"]

Establece `project_root_markers = []` para omitir la búsqueda en directorios superiores y considerar el directorio de trabajo actual como la raíz del proyecto.

## Proveedores de modelos personalizados

Un proveedor de modelos define cómo se conecta Codex a un modelo: URL base, API de comunicación, autenticación y encabezados HTTP opcionales. Los proveedores personalizados no pueden reutilizar los identificadores reservados de los proveedores integrados: `openai`, `ollama` y `lmstudio`.

Define proveedores adicionales y haz que `model_provider` apunte a ellos:

```toml
model = "gpt-5.6-terra"
model_provider = "proxy"

[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "http://proxy.example.com"
env_key = "OPENAI_API_KEY"

[model_providers.local_ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"

[model_providers.mistral]
name = "Mistral"
base_url = "https://api.mistral.ai/v1"
env_key = "MISTRAL_API_KEY"

Si un proveedor personalizado admite el punto de acceso para la búsqueda web independiente, declara
esa capacidad en la configuración del proveedor:

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
env_key = "OPENAI_API_KEY"
supports_standalone_web_search = true

En los proveedores personalizados, el valor predeterminado de esta opción es `false`. La búsqueda web independiente está
en desarrollo y desactivada de forma predeterminada. Establecer la capacidad del proveedor en `true`
no la habilita: el proveedor debe admitir un punto de acceso compatible
y el modelo y el entorno de ejecución seleccionados deben admitir la búsqueda independiente. El
[modo `web_search`](/es-419/codex/web-search) configurado y
las restricciones de búsqueda administradas siguen aplicándose.

Agrega encabezados de solicitud cuando sea necesario:

```toml
[model_providers.example]
http_headers = { "X-Example-Header" = "example-value" }
env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }

Usa autenticación mediante comandos cuando un proveedor necesite que Codex obtenga tokens de portador de un asistente externo de credenciales:

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
wire_api = "responses"

[model_providers.proxy.auth]
command = "/usr/local/bin/fetch-codex-token"
args = ["--audience", "codex"]
timeout_ms = 5000
refresh_interval_ms = 300000

El comando de autenticación no recibe ninguna entrada por `stdin` y debe imprimir el token en stdout. Codex elimina los espacios en blanco iniciales y finales, considera que un token vacío es un error y lo actualiza de forma proactiva según `refresh_interval_ms`; establece `refresh_interval_ms = 0` para actualizarlo solo después de un reintento de autenticación. No combines `[model_providers.<id>.auth]` con `env_key`, `experimental_bearer_token` ni `requires_openai_auth`.

### Proveedor de Amazon Bedrock

Codex incluye un proveedor de modelos `amazon-bedrock` integrado. Establécelo directamente como
`model_provider`; a diferencia de los proveedores personalizados, este proveedor integrado solo admite
las anulaciones anidadas del perfil y la región de AWS.

```toml
model_provider = "amazon-bedrock"
model = "<bedrock-model-id>"

[model_providers.amazon-bedrock.aws]
profile = "default"
region = "eu-central-1"

Si omites `profile`, Codex usa la cadena estándar de credenciales de AWS. Establece
`region` en la región compatible de Bedrock que debe procesar las solicitudes.

Para consultar el flujo de configuración completo, las opciones de autenticación, los modelos compatibles y la
disponibilidad de las funciones, consulta [Usa ChatGPT Work y Codex con Amazon
Bedrock](/es-419/codex/amazon-bedrock).

## Modo OSS (proveedores locales)

Codex puede ejecutarse con un proveedor local de “código abierto”, como Ollama o LM
Studio, cuando incluyes `--oss`. Elige uno para una sola ejecución con
`--local-provider`, o establece `oss_provider` como predeterminado. Si no estableces ninguno, la
CLI interactiva te pide que elijas; `codex exec` finaliza con un error.

```toml
# Default local provider used with `--oss`
oss_provider = "ollama" # or "lmstudio"

## Proveedor de Azure y ajustes específicos de cada proveedor

```toml
[model_providers.azure]
name = "Azure"
base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
env_key = "AZURE_OPENAI_API_KEY"
query_params = { api-version = "2025-04-01-preview" }
wire_api = "responses"
request_max_retries = 4
stream_max_retries = 10
stream_idle_timeout_ms = 300000

Para cambiar la URL base del proveedor de OpenAI integrado, usa `openai_base_url`; no crees `[model_providers.openai]`, porque no puedes anular los identificadores de los proveedores integrados.

## Organizaciones de la API que usan residencia de datos

Los proyectos creados con la [residencia de datos](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt) habilitada pueden crear un proveedor de modelos para actualizar `base_url` con el [prefijo correcto](/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency). Los espacios de trabajo de ChatGPT con residencia de datos no requieren un proveedor personalizado; cuando inicias sesión con ChatGPT, Codex respeta la configuración de residencia del espacio de trabajo.

```toml
model_provider = "openaidr"
[model_providers.openaidr]
name = "OpenAI Data Residency"
base_url = "https://us.api.openai.com/v1" # Replace 'us' with domain prefix

## Razonamiento, nivel de detalle y límites del modelo

```toml
model_reasoning_summary = "none"          # Disable summaries
model_verbosity = "low"                   # Shorten responses
model_supports_reasoning_summaries = true # Force reasoning
model_context_window = 128000             # Context window size

`model_verbosity` solo se aplica a los proveedores que usan Responses API. Los proveedores de Chat Completions ignorarán esta configuración.

## Políticas de aprobación y modos de sandbox

Elige el nivel de rigor de las aprobaciones (afecta cuándo Codex hace una pausa) y el nivel del sandbox (afecta el acceso a los archivos y a la red).

Para conocer los detalles operativos que debes tener en cuenta al editar `config.toml`, consulta [Combinaciones comunes de sandbox y aprobación](/es-419/codex/agent-approvals-security#common-sandbox-and-approval-combinations), [Rutas protegidas en directorios raíz con permisos de escritura](/es-419/codex/agent-approvals-security#protected-paths-in-writable-roots) y [Acceso a la red](/es-419/codex/agent-approvals-security#network-access).

Para conocer los perfiles de permisos en fase beta que configuran en conjunto el acceso al sistema de archivos y a la red, consulta [Permisos](/es-419/codex/permissions).

También puedes usar una política de aprobación granular (`approval_policy = { granular = { ... } }`) para permitir o rechazar automáticamente categorías específicas de prompts. Esto es útil cuando quieres aprobaciones interactivas habituales para algunos casos, pero que otros, como `request_permissions` o los prompts de scripts de habilidades, se rechacen automáticamente.

Configura `approvals_reviewer = "auto_review"` para enviar a revisión automática las solicitudes de aprobación
interactivas que cumplan los requisitos. Esto cambia quién revisa, no
el límite del sandbox.

Usa `[auto_review].policy` para las instrucciones locales de la política del revisor. La configuración administrada
`guardian_policy_config` tiene prioridad.

```toml
approval_policy = "untrusted"   # Other options: on-request, never, or { granular = { ... } }
approvals_reviewer = "user"     # Or "auto_review" for automatic review
sandbox_mode = "workspace-write"
allow_login_shell = false       # Optional hardening: disallow login shells for shell tools

# Example granular approval policy:
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

[sandbox_workspace_write]
exclude_tmpdir_env_var = false  # Allow $TMPDIR
exclude_slash_tmp = false       # Allow /tmp
writable_roots = ["/Users/YOU/.pyenv/shims"]
network_access = false          # Opt in to outbound network

[auto_review]
policy = """
Use your organization's automatic review policy.
"""

### Perfiles de permisos con nombre

Para conocer los perfiles integrados, la sintaxis de los perfiles personalizados y el modelo completo de configuración del sistema de archivos y
de la red, consulta [Permisos](/es-419/codex/permissions).

Para ver la lista completa de claves y las restricciones de los requisitos, consulta
[Referencia de configuración](/es-419/codex/config-file/config-reference) y
[Configuración administrada](/es-419/codex/enterprise/managed-configuration).

  En el modo workspace-write, algunos entornos mantienen `.git/` y `.codex/`
  en modo de solo lectura, aunque se pueda escribir en el resto del espacio de trabajo. Por eso,
  es posible que comandos como `git commit` todavía requieran aprobación para ejecutarse fuera del
  sandbox. Si quieres que Codex omita comandos específicos (por ejemplo, bloquear `git
  commit` fuera del sandbox), usa
<a href="/codex/agent-configuration/rules">reglas</a>.

Desactiva por completo el entorno aislado (úsalo solo si tu entorno ya aísla los procesos):

```toml
sandbox_mode = "danger-full-access"

## Política del entorno de shell

`shell_environment_policy` controla qué variables de entorno pasa Codex a los
comandos que inicia. Comienza con un entorno vacío mediante `inherit = "none"` o
hereda un conjunto reducido mediante `inherit = "core"`. Agrega valores explícitos y filtros
por clave para evitar pasar secretos innecesarios a los comandos iniciados.

```toml
[shell_environment_policy]
inherit = "core"
set = { MY_FLAG = "1" }
ignore_default_excludes = false

[shell_environment_policy.filters]
"AWS_*" = "exclude"
"AZURE_*" = "exclude"

Los patrones de filtro no distinguen entre mayúsculas y minúsculas y admiten `*` y `?`. Usa `"exclude"`
para eliminar las variables que coincidan. Cuando algún patrón usa `"include"`, Codex conserva
solo las variables que coinciden con un patrón de inclusión. Los patrones de inclusión no restauran las variables
que ya se excluyeron. Las claves de filtro se combinan sin distinguir entre mayúsculas y minúsculas en todas las
capas de configuración.

`ignore_default_excludes` tiene como valor predeterminado `true`, por lo que Codex no elimina automáticamente
los nombres de variables que contienen `KEY`, `SECRET` o `TOKEN`. Configúralo como `false`
para aplicar esas exclusiones automáticas antes de que se ejecuten tus filtros explícitos.

Codex aplica primero las exclusiones automáticas, luego las personalizadas, después los valores de
`set` y, por último, la lista de elementos permitidos basada en patrones de inclusión. Como `set` se ejecuta después de las
exclusiones, puede restaurar una variable excluida. Una lista de elementos permitidos basada en patrones de inclusión
aun así puede eliminar ese valor restaurado.

Los arreglos anteriores `exclude` y `include_only` siguen siendo compatibles con las configuraciones
existentes. No combines ninguno de los dos arreglos con
`[shell_environment_policy.filters]` en la misma capa de configuración; Codex
rechaza esa combinación.

## Servidores MCP

Consulta la [documentación específica de MCP](/es-419/codex/extend/mcp) para conocer los detalles de configuración.

## Observabilidad y telemetría

Habilita la exportación de registros de OpenTelemetry (OTel) para hacer un seguimiento de las ejecuciones de Codex (solicitudes a la API, eventos SSE, prompts, aprobaciones y resultados de herramientas). Está deshabilitada de forma predeterminada; habilítala mediante `[otel]`:

```toml
[otel]
environment = "staging"   # defaults to "dev"
exporter = "none"         # set to otlp-http or otlp-grpc to send events
log_user_prompt = false   # redact user prompts unless explicitly enabled

Elige un exportador:

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}

Si `exporter = "none"`, Codex registra los eventos, pero no envía nada. Los exportadores agrupan los eventos en lotes de forma asíncrona y vacían el búfer al cerrarse. Los metadatos de los eventos incluyen el nombre del servicio, la versión de la CLI, la etiqueta del entorno, el ID de la conversación, el modelo, la configuración del sandbox y de las aprobaciones, y los campos específicos de cada evento (consulta [Referencia de configuración](/es-419/codex/config-file/config-reference)).

### Qué se emite

Codex emite eventos de registro estructurados sobre las ejecuciones y el uso de herramientas. Estos son algunos tipos de eventos representativos:

- `codex.conversation_starts` (modelo, configuración de razonamiento, política de sandbox y aprobación)
- `codex.api_request` (intento, estado/éxito, duración y detalles del error)
- `codex.sse_event` (tipo de evento de transmisión, éxito/falla, duración y recuentos de tokens en `response.completed`)
- `codex.websocket_request` y `codex.websocket_event` (duración de la solicitud, además del tipo, éxito o error de cada mensaje)
- `codex.user_prompt` (longitud; contenido oculto salvo que se habilite explícitamente)
- `codex.tool_decision` (si se aprobó o denegó y si la decisión provino de la configuración o del usuario)
- `codex.tool_result` (duración, éxito, fragmento de salida)

### Métricas de OTel emitidas

Cuando la canalización de métricas de OTel está habilitada, Codex emite contadores e histogramas de duración correspondientes a la actividad de la API, las transmisiones y las herramientas.

Cada una de las siguientes métricas también incluye etiquetas de metadatos predeterminadas: `auth_mode`, `originator`, `session_source`, `model` y `app.version`.

| Métrica                                | Tipo      | Campos              | Descripción                                                       |
| ------------------------------------- | --------- | ------------------- | ----------------------------------------------------------------- |
| `codex.api_request`                   | contador   | `status`, `success` | Recuento de solicitudes a la API por estado HTTP y éxito/falla.             |
| `codex.api_request.duration_ms`       | histograma | `status`, `success` | Duración de las solicitudes a la API en milisegundos.                             |
| `codex.sse_event`                     | contador   | `kind`, `success`   | Recuento de eventos SSE por tipo de evento y éxito/falla.                |
| `codex.sse_event.duration_ms`         | histograma | `kind`, `success`   | Duración del procesamiento de eventos SSE en milisegundos.                    |
| `codex.websocket.request`             | contador   | `success`           | Recuento de solicitudes WebSocket por éxito/falla.                       |
| `codex.websocket.request.duration_ms` | histograma | `success`           | Duración de las solicitudes WebSocket en milisegundos.                       |
| `codex.websocket.event`               | contador   | `kind`, `success`   | Recuento de mensajes/eventos de WebSocket por tipo y éxito/falla.        |
| `codex.websocket.event.duration_ms`   | histograma | `kind`, `success`   | Duración del procesamiento de mensajes/eventos de WebSocket en milisegundos.      |
| `codex.tool.call`                     | contador   | `tool`, `success`   | Cantidad de invocaciones de herramientas por nombre de la herramienta y resultado (éxito o error).           |
| `codex.tool.call.duration_ms`         | histograma | `tool`, `success`   | Duración de la ejecución de herramientas en milisegundos, por nombre de la herramienta y resultado. |

Para obtener más recomendaciones sobre seguridad y privacidad relacionadas con la telemetría, consulta [Seguridad](/es-419/codex/agent-approvals-security#monitoring-and-telemetry).

### Métricas

De forma predeterminada, Codex envía periódicamente a OpenAI una pequeña cantidad de datos anónimos sobre uso y estado. Esto ayuda a detectar cuándo Codex no funciona correctamente y permite saber qué funciones y opciones de configuración se usan, para que el equipo de Codex pueda enfocarse en lo que más importa. Estas métricas no contienen información de identificación personal (PII). La recopilación de métricas es independiente de la exportación de registros y trazas de OTel.

Si quieres desactivar por completo la recopilación de métricas de la aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE en una computadora, establece el indicador de análisis en tu configuración:

```toml
[analytics]
enabled = false

Cada métrica incluye sus propios campos, además de los campos de contexto predeterminados que aparecen a continuación.

#### Campos de contexto predeterminados (se aplican a cada evento o métrica)

- `auth_mode`: `swic` | `api` | `unknown`.
- `model`: nombre del modelo utilizado.
- `app.version`: versión de Codex.

#### Catálogo de métricas

Cada métrica incluye los campos obligatorios, además de los campos de contexto predeterminados anteriores. Los nombres de las métricas que aparecen a continuación omiten el prefijo `codex.`.
La mayoría de los nombres de métricas se definen de forma centralizada en `codex-rs/otel/src/metrics/names.rs`; también se incluyen aquí las métricas específicas de funciones emitidas fuera de ese archivo.
Si una métrica incluye el campo `tool`, este refleja la herramienta interna utilizada (por ejemplo, `apply_patch` o `shell`) y no contiene el comando de shell real ni el parche real que `codex` intenta aplicar.

#### Entorno de ejecución y transporte del modelo

| Métrica                                          | Tipo      | Campos               | Descripción                                                  |
| ----------------------------------------------- | --------- | -------------------- | ------------------------------------------------------------ |
| `api_request`                                   | contador   | `status`, `success`  | Cantidad de solicitudes a la API por estado HTTP y resultado (éxito o error).        |
| `api_request.duration_ms`                       | histograma | `status`, `success`  | Duración de las solicitudes a la API en milisegundos.                        |
| `sse_event`                                     | contador   | `kind`, `success`    | Cantidad de eventos SSE por tipo de evento y resultado (éxito o error).           |
| `sse_event.duration_ms`                         | histograma | `kind`, `success`    | Duración del procesamiento de eventos SSE en milisegundos.               |
| `websocket.request`                             | contador   | `success`            | Cantidad de solicitudes WebSocket por resultado (éxito o error).                  |
| `websocket.request.duration_ms`                 | histograma | `success`            | Duración de las solicitudes WebSocket en milisegundos.                  |
| `websocket.event`                               | contador   | `kind`, `success`    | Cantidad de mensajes/eventos de WebSocket por tipo y resultado (éxito o error).   |
| `websocket.event.duration_ms`                   | histograma | `kind`, `success`    | Duración del procesamiento de mensajes/eventos de WebSocket en milisegundos. |
| `responses_api_overhead.duration_ms`            | histograma |                      | Medición del tiempo de sobrecarga de Responses API a partir de las respuestas de WebSocket.      |
| `responses_api_inference_time.duration_ms`      | histograma |                      | Medición del tiempo de inferencia de Responses API a partir de las respuestas de WebSocket.     |
| `responses_api_engine_iapi_ttft.duration_ms`    | histograma |                      | Medición del tiempo hasta el primer token en la IAPI del motor de Responses API.        |
| `responses_api_engine_service_ttft.duration_ms` | histograma |                      | Medición del tiempo hasta el primer token en el servicio del motor de Responses API.     |
| `responses_api_engine_iapi_tbt.duration_ms`     | histograma |                      | Medición del tiempo entre tokens en la IAPI del motor de Responses API.         |
| `responses_api_engine_service_tbt.duration_ms`  | histograma |                      | Medición del tiempo entre tokens en el servicio del motor de Responses API.      |
| `transport.fallback_to_http`                    | contador   | `from_wire_api`      | Cantidad de veces que se recurrió a HTTP como alternativa a WebSocket.                            |
| `remote_models.fetch_update.duration_ms`        | histograma |                      | Tiempo para obtener definiciones de modelos remotos.                      |
| `remote_models.load_cache.duration_ms`          | histograma |                      | Tiempo para cargar la caché de modelos remotos.                         |
| `startup_prewarm.duration_ms`                   | histograma | `status`             | Duración del precalentamiento al inicio por resultado.                         |
| `startup_prewarm.age_at_first_turn_ms`          | histograma | `status`             | Antigüedad del precalentamiento inicial cuando lo resuelve el primer turno real.    |
| `cloud_requirements.fetch.duration_ms`          | histograma |                      | Duración de la obtención de los requisitos de la nube administrados por el espacio de trabajo.         |
| `cloud_requirements.fetch_attempt`              | contador   | Ver nota             | Intentos de obtención de los requisitos de la nube administrados por el espacio de trabajo.         |
| `cloud_requirements.fetch_final`                | contador   | Ver nota             | Resultado final de la obtención de los requisitos de la nube administrados por el espacio de trabajo.    |
| `cloud_requirements.load`                       | contador   | `trigger`, `outcome` | Resultado de la carga de los requisitos de la nube administrados por el espacio de trabajo.           |

La métrica `cloud_requirements.fetch_attempt` incluye los campos `trigger`, `attempt`, `outcome` y `status_code`. La métrica `cloud_requirements.fetch_final` incluye los campos `trigger`, `outcome`, `reason`, `attempt_count` y `status_code`.

#### Actividad de turnos y herramientas

| Métrica                                 | Tipo      | Campos                                                                    | Descripción                                                                                                      |
| -------------------------------------- | --------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `turn.e2e_duration_ms`                 | histograma |                                                                           | Tiempo de extremo a extremo de un turno completo.                                                                                 |
| `turn.ttft.duration_ms`                | histograma |                                                                           | Tiempo hasta el primer token en un turno.                                                                                  |
| `turn.ttfm.duration_ms`                | histograma |                                                                           | Tiempo hasta el primer elemento de salida del modelo en un turno.                                                                      |
| `turn.network_proxy`                   | contador   | `active`, `tmp_mem_enabled`                                               | Indica si el proxy de red administrado estuvo activo durante el turno.                                                       |
| `turn.memory`                          | contador   | `read_allowed`, `feature_enabled`, `config_use_memories`, `has_citations` | Disponibilidad de lectura de memoria y uso de citas de memoria por turno.                                                     |
| `turn.tool.call`                       | histograma | `tmp_mem_enabled`                                                         | Cantidad de llamadas a herramientas durante el turno.                                                                                |
| `turn.token_usage`                     | histograma | `token_type`, `tmp_mem_enabled`                                           | Uso de tokens por turno según el tipo de token (`total`, `input`, `cached_input`, `output` o `reasoning_output`).          |
| `tool.call`                            | contador   | `tool`, `success`                                                         | Cantidad de invocaciones de herramientas por nombre de herramienta y resultado (éxito o error).                                                          |
| `tool.call.duration_ms`                | histograma | `tool`, `success`                                                         | Duración de la ejecución de herramientas en milisegundos por nombre de herramienta y resultado.                                                |
| `tool.unified_exec`                    | contador   | `tty`                                                                     | Llamadas a la herramienta exec unificada según el modo TTY.                                                                             |
| `approval.requested`                   | contador   | `tool`, `approved`                                                        | Resultado de la solicitud de aprobación de una herramienta (`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`). |
| `mcp.call`                             | contador   | Ver nota                                                                  | Resultado de la invocación de una herramienta de MCP.                                                                                      |
| `mcp.call.duration_ms`                 | histograma | Ver nota                                                                  | Duración de la invocación de una herramienta de MCP.                                                                                    |
| `mcp.tools.list.duration_ms`           | histograma | `cache`                                                                   | Duración del listado de herramientas de MCP, incluido el estado de acierto o fallo de caché.                                                          |
| `mcp.tools.fetch_uncached.duration_ms` | histograma |                                                                           | Duración de las obtenciones de herramientas de MCP con fallo de caché.                                                                |
| `mcp.tools.cache_write.duration_ms`    | histograma |                                                                           | Duración de las escrituras en la caché de herramientas MCP de Codex Apps.                                                                    |
| `hooks.run`                            | contador   | `hook_name`, `source`, `status`                                           | Cantidad de ejecuciones de hooks por nombre, origen y estado.                                                                 |
| `hooks.run.duration_ms`                | histograma | `hook_name`, `source`, `status`                                           | Duración de la ejecución del hook en milisegundos.                                                                               |

Las métricas `mcp.call` y `mcp.call.duration_ms` incluyen `status`; las emisiones normales de llamadas a herramientas también incluyen `tool`, además de `connector_id` y `connector_name` cuando están disponibles. Las llamadas MCP bloqueadas de Codex Apps pueden emitir `mcp.call` solo con `status`.

#### Hilos, tareas y funciones

| Métrica                            | Tipo      | Campos                | Descripción                                                                      |
| --------------------------------- | --------- | --------------------- | -------------------------------------------------------------------------------- |
| `feature.state`                   | contador   | `feature`, `value`    | Valores de las funciones que difieren de los predeterminados (se emite una fila por cada valor no predeterminado).         |
| `status_line`                     | contador   |                       | Sesión iniciada con una línea de estado configurada.                                   |
| `model_warning`                   | contador   |                       | Advertencia enviada al modelo.                                                       |
| `thread.started`                  | contador   | `is_git`              | Nuevo hilo creado, con una etiqueta que indica si el directorio de trabajo está en un repositorio de Git.    |
| `conversation.turn.count`         | contador   |                       | Turnos de usuario/asistente por hilo, registrados al finalizar el hilo.              |
| `thread.fork`                     | contador   | `source`              | Nuevo hilo creado mediante un fork de un hilo existente.                                |
| `thread.rename`                   | contador   |                       | Hilo renombrado.                                                                  |
| `thread.side`                     | contador   | `source`              | Conversación paralela creada.                                                       |
| `thread.skills.enabled_total`     | histograma |                       | Cantidad de habilidades habilitadas para un hilo nuevo.                                       |
| `thread.skills.kept_total`        | histograma |                       | Cantidad de habilidades habilitadas que se conservaron después de renderizar el prompt.                            |
| `thread.skills.truncated`         | histograma |                       | Si al renderizar las habilidades se truncó la lista de habilidades habilitadas (`1` o `0`).          |
| `task.compact`                    | contador   | `type`                | Cantidad de compactaciones por tipo (`remote` o `local`), incluidas las manuales y las automáticas. |
| `task.review`                     | contador   |                       | Cantidad de revisiones activadas.                                                     |
| `task.undo`                       | contador   |                       | Cantidad de acciones de deshacer activadas.                                                |
| `task.user_shell`                 | contador   |                       | Cantidad de acciones de shell realizadas por el usuario (`!` en la TUI, por ejemplo).                       |
| `shell_snapshot`                  | contador   | Ver nota              | Si se pudo tomar una instantánea del shell.                                       |
| `shell_snapshot.duration_ms`      | histograma | `success`             | Tiempo necesario para tomar una instantánea del shell.                                                   |
| `skill.injected`                  | contador   | `status`, `skill`     | Resultados de la inyección de habilidades por habilidad.                                               |
| `plugins.startup_sync`            | contador   | `transport`, `status` | Intentos de sincronización de complementos seleccionados durante el inicio.                                            |
| `plugins.startup_sync.final`      | contador   | `transport`, `status` | Resultado final de la sincronización de complementos seleccionados durante el inicio.                                       |
| `multi_agent.spawn`               | contador   | `role`                | Creaciones de agentes por rol.                                                            |
| `multi_agent.resume`              | contador   |                       | Reanudaciones de agentes.                                                                   |
| `multi_agent.nickname_pool_reset` | contador   |                       | Restablecimientos del conjunto de apodos de agentes.                                                      |

La métrica `shell_snapshot` incluye `success` y, en caso de error, `failure_reason`.

#### Memoria y estado local

| Métrica                         | Tipo      | Campos                    | Descripción                                               |
| ------------------------------ | --------- | ------------------------- | --------------------------------------------------------- |
| `memory.phase1`                | contador   | `status`                  | Cantidad de trabajos de la fase 1 de memoria por estado.                      |
| `memory.phase1.e2e_ms`         | histograma |                           | Duración de extremo a extremo de la fase 1 de memoria.                   |
| `memory.phase1.output`         | contador   |                           | Resultados escritos durante la fase 1 de memoria.                           |
| `memory.phase1.token_usage`    | histograma | `token_type`              | Uso de tokens durante la fase 1 de memoria por tipo de token.                 |
| `memory.phase2`                | contador   | `status`                  | Cantidad de trabajos de la fase 2 de memoria por estado.                      |
| `memory.phase2.e2e_ms`         | histograma |                           | Duración de extremo a extremo de la fase 2 de memoria.                   |
| `memory.phase2.input`          | contador   |                           | Cantidad de entradas de la fase 2 de memoria.                               |
| `memory.phase2.token_usage`    | histograma | `token_type`              | Uso de tokens durante la fase 2 de memoria por tipo de token.                 |
| `memories.usage`               | contador   | `kind`, `tool`, `success` | Uso de la memoria según el tipo, la herramienta y si hubo éxito o error.          |
| `external_agent_config.detect` | contador   | Ver nota                  | Detecciones de configuración de agentes externos por tipo de elemento de migración.  |
| `external_agent_config.import` | contador   | Ver nota                  | Importaciones de configuración de agentes externos por tipo de elemento de migración.     |
| `db.backfill`                  | contador   | `status`                  | Resultados de la carga retroactiva inicial de la base de datos de estado (`upserted`, `failed`). |
| `db.backfill.duration_ms`      | histograma | `status`                  | Duración de la carga retroactiva inicial de la base de datos de estado.                |
| `db.error`                     | contador   | `stage`                   | Errores durante las operaciones de la base de datos de estado.                        |

Las métricas `external_agent_config.detect` y `external_agent_config.import` incluyen `migration_type`; las migraciones de habilidades también incluyen `skills_count`.

#### Sandbox de Windows

| Métrica                                           | Tipo      | Campos                                    | Descripción                                           |
| ------------------------------------------------ | --------- | ----------------------------------------- | ----------------------------------------------------- |
| `windows_sandbox.setup_success`                  | contador   | `originator`, `mode`                      | Configuraciones del sandbox de Windows completadas correctamente.                      |
| `windows_sandbox.setup_failure`                  | contador   | `originator`, `mode`                      | Errores en la configuración del sandbox de Windows.                       |
| `windows_sandbox.setup_duration_ms`              | histograma | `result`, `originator`, `mode`            | Duración de la configuración del sandbox de Windows.                       |
| `windows_sandbox.elevated_setup_success`         | contador   |                                           | Configuraciones del sandbox de Windows con privilegios elevados completadas correctamente.             |
| `windows_sandbox.elevated_setup_failure`         | contador   | Ver nota                                  | Errores en la configuración del sandbox de Windows con privilegios elevados.              |
| `windows_sandbox.elevated_setup_canceled`        | contador   | Ver nota                                  | Intentos cancelados de configurar el sandbox de Windows con privilegios elevados.     |
| `windows_sandbox.elevated_setup_duration_ms`     | histograma | `result`                                  | Duración de la configuración del sandbox de Windows con privilegios elevados.              |
| `windows_sandbox.elevated_prompt_shown`          | contador   |                                           | Se mostró el prompt para configurar el sandbox con privilegios elevados.                  |
| `windows_sandbox.elevated_prompt_accept`         | contador   |                                           | Se aceptó el prompt para configurar el sandbox con privilegios elevados.               |
| `windows_sandbox.elevated_prompt_use_legacy`     | contador   |                                           | El usuario eligió el sandbox heredado en el prompt de configuración con privilegios elevados.   |
| `windows_sandbox.elevated_prompt_quit`           | contador   |                                           | El usuario eligió salir en el prompt de configuración con privilegios elevados.                   |
| `windows_sandbox.fallback_prompt_shown`          | contador   |                                           | Se mostró el prompt alternativo del sandbox.                        |
| `windows_sandbox.fallback_retry_elevated`        | contador   |                                           | El usuario volvió a intentar la configuración con privilegios elevados desde el prompt alternativo. |
| `windows_sandbox.fallback_use_legacy`            | contador   |                                           | El usuario eligió el sandbox heredado desde el prompt alternativo.   |
| `windows_sandbox.fallback_prompt_quit`           | contador   |                                           | El usuario salió desde el prompt alternativo.                   |
| `windows_sandbox.legacy_setup_preflight_failed`  | contador   | Ver nota                                  | Error en la comprobación previa de la configuración del sandbox heredado de Windows.       |
| `windows_sandbox.setup_elevated_sandbox_command` | contador   |                                           | Se invocó el comando de configuración del sandbox con privilegios elevados.               |
| `windows_sandbox.createprocessasuserw_failed`    | contador   | `error_code`, `path_kind`, `exe`, `level` | Errores de `CreateProcessAsUserW` en Windows.              |

Las métricas de errores de configuración con privilegios elevados incluyen `code` y `message` cuando están disponibles los detalles de los errores de configuración de Windows, y pueden incluir `originator` cuando se emiten desde la ruta de configuración compartida. La métrica `windows_sandbox.legacy_setup_preflight_failed` incluye `originator` cuando se emite desde la ruta de configuración compartida, pero es posible que los errores de comprobación previa del prompt alternativo no incluyan ningún campo.

### Controles de comentarios

De forma predeterminada, los clientes locales permiten a los usuarios enviar comentarios mediante `/feedback`. Para desactivar la recopilación de comentarios en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE en una máquina, actualiza tu configuración:

```toml
[feedback]
enabled = false

Cuando la recopilación está desactivada, `/feedback` muestra un mensaje que indica que está desactivada y Codex rechaza los envíos de comentarios.

### Ocultar o mostrar eventos de razonamiento

Si quieres reducir el ruido de la salida de “razonamiento” (por ejemplo, en los registros de CI), puedes suprimirla:

```toml
hide_agent_reasoning = true

Si quieres mostrar el contenido de razonamiento sin procesar cuando un modelo lo emita:

```toml
show_raw_agent_reasoning = true

Activa el razonamiento sin procesar solo si es aceptable para tu flujo de trabajo. Algunos modelos o proveedores (como `gpt-oss`) no emiten razonamiento sin procesar; en ese caso, esta configuración no tiene ningún efecto visible.

## Notificaciones

Usa `notify` para ejecutar un programa externo cada vez que Codex emita eventos compatibles (actualmente, solo `agent-turn-complete`). Esto es útil para las notificaciones emergentes de escritorio, los webhooks de chat, las actualizaciones de CI o cualquier alerta por un canal secundario que las notificaciones integradas de la TUI no cubran.

```toml
notify = ["python3", "/path/to/notify.py"]

Ejemplo de `notify.py` (truncado) que reacciona a `agent-turn-complete`:

```python
#!/usr/bin/env python3

def main() -> int:
    notification = json.loads(sys.argv[1])
    if notification.get("type") != "agent-turn-complete":
        return 0
    title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
    message = " ".join(notification.get("input-messages", []))
    subprocess.check_output([
        "terminal-notifier",
        "-title", title,
        "-message", message,
        "-group", "codex-" + notification.get("thread-id", ""),
        "-activate", "com.googlecode.iterm2",
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())

El script recibe un único argumento JSON. Entre los campos comunes se incluyen:

- `type` (actualmente, `agent-turn-complete`)
- `thread-id` (identificador de sesión)
- `turn-id` (identificador de turno)
- `cwd` (directorio de trabajo)
- `input-messages` (mensajes del usuario que dieron lugar al turno)
- `last-assistant-message` (texto del último mensaje del asistente)

Guarda el script en alguna ubicación del disco y configura `notify` para que apunte a él.

#### `notify` frente a `tui.notifications`

- `notify` ejecuta un programa externo (útil para webhooks, notificadores de escritorio y hooks de CI).
- `tui.notifications` está integrado en la TUI y puede filtrar opcionalmente por tipo de evento (por ejemplo, `agent-turn-complete` y `approval-requested`).
- `tui.notification_method` controla cómo la TUI emite notificaciones de la terminal (`auto`, `osc9` o `bel`).
- `tui.notification_condition` controla si las notificaciones de la TUI se activan solo cuando
  la terminal no tiene el foco (`unfocused`) o siempre (`always`).

En el modo `auto`, Codex prefiere las notificaciones OSC 9 (una secuencia de escape de terminal que algunas terminales interpretan como una notificación de escritorio) y, de lo contrario, recurre a BEL (`\x07`).

Consulta [Referencia de configuración](/es-419/codex/config-file/config-reference) para ver las claves exactas.

## Persistencia del historial

De forma predeterminada, Codex guarda las transcripciones de las sesiones locales en `CODEX_HOME` (por ejemplo, `~/.codex/history.jsonl`). Para desactivar la persistencia del historial local:

```toml
[history]
persistence = "none"

Para limitar el tamaño del archivo de historial, establece `history.max_bytes`. Cuando el archivo supera el límite, Codex elimina las entradas más antiguas y compacta el archivo mientras conserva los registros más recientes.

```toml
[history]
max_bytes = 104857600 # 100 MiB

## Citas con enlaces

Si usas una integración de terminal o editor que admita esta función, Codex puede mostrar las citas de archivos como enlaces en los que se puede hacer clic. Configura `file_opener` para elegir el esquema de URI que usa Codex:

```toml
file_opener = "vscode" # or cursor, windsurf, vscode-insiders, none

Ejemplo: una cita como `/home/user/project/main.py:42` puede reescribirse como un enlace `vscode://file/...:42` en el que se puede hacer clic.

## Detección de instrucciones del proyecto

Codex lee `AGENTS.md` (y los archivos relacionados) e incluye una cantidad limitada de instrucciones del proyecto en el primer turno de una sesión. Dos opciones controlan este comportamiento:

- `project_doc_max_bytes`: cuánto se debe leer de cada archivo `AGENTS.md`
- `project_doc_fallback_filenames`: nombres de archivo adicionales que se deben probar cuando falta `AGENTS.md` en algún nivel del directorio

Para ver una guía detallada, consulta [Instrucciones personalizadas con AGENTS.md](/es-419/codex/agent-configuration/agents-md).

## Escritorio

Las opciones de esta sección se aplican únicamente a la aplicación de escritorio de ChatGPT.

### Agregar controladores de archivos personalizados

En tu archivo `~/.codex/config.toml` de usuario, agrega entradas en
`desktop.custom_file_handlers` para abrir archivos en editores o iniciadores internos
que la aplicación de escritorio de ChatGPT no admite de forma predeterminada. Cada entrada agrega una
opción de editor a los menús **Abrir en** de la aplicación. La aplicación muestra esta opción cuando
`command` es una ruta absoluta existente o se puede resolver mediante el `PATH` de la aplicación.

El siguiente ejemplo muestra tres formas de pasar un archivo a un controlador:

```toml
# Append the opened path directly after the command.
[desktop.custom_file_handlers.vscodium]
label = "VSCodium"
icon = "/Users/you/.codex/icons/vscodium.png"
command = "codium"

# Place fixed arguments before the opened path.
[desktop.custom_file_handlers.textedit]
label = "TextEdit"
icon = "/Users/you/.codex/icons/textedit.png"
command = "/usr/bin/open"
args = ["-a", "TextEdit"]

# Append one JSON argument with the path and editor context.
[desktop.custom_file_handlers.company_editor]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"
input = "json_argument"

Guarda `config.toml` y luego reinicia la aplicación de escritorio de ChatGPT.

El ID del controlador es el segmento final del encabezado de la tabla TOML. Debe tener
entre 1 y 64 caracteres, comenzar con una letra o un número ASCII y contener
solo letras y números ASCII, puntos, guiones bajos o guiones. La aplicación expone
el ID con el prefijo `custom:`; por ejemplo, `company_editor` se convierte en
`custom:company_editor`. Escribe entre comillas cualquier ID que contenga un punto para que TOML no lo
interprete como una tabla anidada. Por ejemplo:

```toml
[desktop.custom_file_handlers."company.editor"]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"

Cada controlador admite los siguientes campos:

| Campo          | Obligatorio | Descripción                                                                                                                                                              |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `label`        | Sí      | Nombre para mostrar en la app.                                                                                                                                                 |
| `icon`         | Sí      | Ícono incluido con la app, como `apps/vscode.png`, una URL `data:image/...` en base64, un URI `file:` o una ruta local absoluta a una imagen. Si el origen no es compatible, se usa el ícono predeterminado de VS Code. |
| `command`      | Sí      | Ruta del ejecutable o nombre del comando que se debe detectar y ejecutar.                                                                                                                    |
| `args`         | No       | Arreglo de cadenas que se inserta entre `command` y la entrada del archivo. El valor predeterminado es `[]`.                                                                                            |
| `input`        | No       | Cómo envía la app la entrada del archivo: `path`, `json_argument` o `json_stdin`. El valor predeterminado es `path`.                                                                              |
| `supports_ssh` | No       | Indica si se debe ofrecer el controlador para los archivos de espacios de trabajo SSH. El valor predeterminado es `false`. Usa `json_stdin` cuando el controlador necesite los detalles del host remoto y de la ruta.                     |

El valor `input` controla lo que aparece después de `args`:

- `path` agrega la ruta como último argumento del comando.
- `json_argument` agrega un objeto JSON con `target`, `path`, `appPath` y
`location`. El valor de `location` es un objeto con los valores `line` y
`column`, que comienzan en 1, o `null`.
- `json_stdin` escribe el objeto JSON en la entrada estándar en lugar de agregar un
  argumento. También incluye `hostConfig`, `remoteWorkspaceRoot` y
`remotePath`; estos campos tienen el valor `null` cuando no corresponden.

Por ejemplo, `company_editor` puede recibir este argumento cuando el usuario abre una
ubicación específica en el código fuente:

```json
{
  "target": "custom:company_editor",
  "path": "/repo/src/index.ts",
  "appPath": null,
  "location": { "line": 12, "column": 3 }
}

Al seleccionar un controlador personalizado como editor preferido, esa elección se conserva de la misma
manera que al seleccionar un editor integrado, incluidas las preferencias por proyecto.

## Opciones de la TUI

Ejecutar `codex` sin ningún subcomando inicia la interfaz de usuario interactiva de la terminal (TUI). Codex ofrece algunas opciones de configuración específicas de la TUI en `[tui]`, entre ellas:

- `tui.notifications`: habilitar o deshabilitar las notificaciones (o restringirlas a tipos específicos)
- `tui.notification_method`: elegir `auto`, `osc9` o `bel` para las notificaciones de la terminal
- `tui.notification_condition`: elegir `unfocused` o `always` para definir cuándo
  se activan las notificaciones
- `tui.animations`: habilitar o deshabilitar las animaciones ASCII y los efectos de brillo
- `tui.alternate_screen`: controlar el uso de la pantalla alternativa (establecer en `never` para conservar el historial de desplazamiento de la terminal)
- `tui.show_tooltips`: mostrar u ocultar las sugerencias de introducción en la pantalla de bienvenida

El valor predeterminado de `tui.notification_method` es `auto`. En el modo `auto`, Codex prefiere las notificaciones OSC 9 (una secuencia de escape de terminal que algunas terminales interpretan como una notificación de escritorio) cuando parece que la terminal las admite; de lo contrario, recurre a BEL (`\x07`).

Consulta [Referencia de configuración](/es-419/codex/config-file/config-reference) para ver la lista completa de claves.
