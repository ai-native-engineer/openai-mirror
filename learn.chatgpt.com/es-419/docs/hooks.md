<!-- source: https://learn.chatgpt.com/es-419/docs/hooks -->

Los hooks son un marco de extensibilidad para Codex. Te permiten ejecutar scripts o herramientas MCP
durante el bucle del agente para habilitar funciones como:

- Enviar el chat a un motor personalizado de registro y análisis
- Analizar los prompts de tu equipo para impedir que se peguen claves de API por accidente
- Resumir chats para crear memorias persistentes automáticamente
- Ejecutar una comprobación de validación personalizada cuando se detiene un turno del chat para hacer cumplir los estándares
- Personalizar el diseño de prompts al trabajar en un directorio determinado

Comportamiento en tiempo de ejecución que debes tener en cuenta:

- Se ejecutan todos los hooks coincidentes de los distintos archivos.
- Los hooks de comando coincidentes para un mismo evento se inician de forma concurrente,
por lo que un hook no puede impedir que se inicie otro hook coincidente.
- Los hooks no administrados deben revisarse y marcarse como confiables antes de ejecutarse.

Los hooks se ejecutan en distintos momentos de una conversación:

| Cuándo                              | Hooks                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Durante un turno                     | `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `UserPromptSubmit`, `SubagentStop`, `Stop` |
| Cuando interrumpes un turno activo | `Interrupt` (no se ejecuta para los subagentes)                                                                                   |
| Cuando se inicia una sesión o un subagente | `SessionStart`, `SubagentStart`                                                                                           |
| Cuando finaliza el hilo principal         | `SessionEnd` (no se ejecuta para los subagentes)                                                                                  |

## Dónde busca Codex los hooks

Codex detecta hooks junto a las capas de configuración activas en cualquiera de estas formas:

- `hooks.json`
- tablas `[hooks]` definidas directamente en `config.toml`

Los complementos instalados también pueden incluir la configuración del ciclo de vida mediante su archivo de
manifiesto o un archivo `hooks/hooks.json` predeterminado. Consulta [Crear
complementos](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) para conocer las
reglas de empaquetado de complementos.

En la práctica, las cuatro ubicaciones más útiles son:

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

Si existe más de una fuente de hooks, Codex carga todos los hooks coincidentes.
Las capas de configuración con mayor precedencia no reemplazan los hooks de las capas con menor precedencia.
Si una misma capa contiene tanto `hooks.json` como tablas `[hooks]` definidas directamente en ella, Codex
los combina y muestra una advertencia al iniciar. Es preferible usar una sola representación por capa.

Codex también puede detectar hooks incluidos en complementos habilitados. Los hooks incluidos en complementos
se cargan junto con otras fuentes de hooks y siguen el mismo proceso para revisarlos y marcarlos como confiables que
los demás hooks no administrados.

Los hooks locales del proyecto solo se cargan cuando la capa `.codex/` del proyecto se considera confiable. En
los proyectos que no son de confianza, Codex sigue cargando los hooks de usuario y del sistema desde sus propias
capas de configuración activas.

## Revisar los hooks y marcarlos como confiables

Codex muestra los hooks configurados antes de decidir cuáles pueden ejecutarse. Antes de que
pueda ejecutarse un hook no administrado, Codex exige que revises la definición exacta del hook
y la marques como confiable. Codex vincula el registro de confianza al hash actual del hook, por lo que
los hooks nuevos o modificados se marcan para revisión y se omiten hasta que se marquen como confiables.

Usa `/hooks` en la CLI para inspeccionar las fuentes de hooks, revisar hooks nuevos o modificados,
marcarlos como confiables o deshabilitar hooks no administrados de forma individual. Si al iniciar hay hooks que necesitan
revisión, Codex muestra una advertencia que te indica que abras `/hooks`.

Los hooks administrados provenientes del sistema, MDM, la nube o `requirements.toml` se marcan
como administrados, se consideran confiables según la política y no pueden deshabilitarse desde el navegador de hooks del usuario.

Para una automatización puntual que ya valide las fuentes de hooks fuera de Codex, pasa
`--dangerously-bypass-hook-trust` para ejecutar los hooks habilitados sin exigir
un registro persistente de confianza en esos hooks para esa invocación.

## Estructura de la configuración

Los hooks se organizan en tres niveles:

- Un evento de hook como `PreToolUse`, `PostToolUse`, `PreCompact`,
`SubagentStart` o `Stop`
- Un grupo de condiciones que determina cuándo hay una coincidencia para ese evento
- Uno o más controladores de hooks que se ejecutan cuando se cumplen las condiciones del grupo

```json
{
  "description": "Optional lifecycle hooks for this workspace.",
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes",
            "additionalContextLimit": 5000
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_end.py",
            "timeout": 3
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/permission_request.py\"",
            "statusMessage": "Checking approval request"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
            "statusMessage": "Reviewing Bash output"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit_data_flywheel.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}

Notas:

- `description` es un metadato opcional de nivel superior para un archivo `hooks.json`. Esto
  no cambia qué hooks se ejecutan.
- `timeout` se especifica en segundos.
- Si se omite `timeout`, Codex usa `600` segundos para la mayoría de los hooks.
  - `SessionEnd` y `Interrupt` usan `1` segundo de forma predeterminada y admiten hasta `3` segundos.
- `statusMessage` es opcional.
- `additionalContextLimit` establece la cantidad de `additionalContext` que puede
  enviar un hook de comando al modelo antes de que Codex guarde el texto completo en disco y envíe una
  vista previa más breve en su lugar. Consulta [Salida extensa de hooks](#large-hook-output).
- `commandWindows` permite reemplazar opcionalmente el comando solo en Windows. En TOML, usa
`command_windows` o `commandWindows`.
- Establece `async` en `true` para [ejecutar un hook de comando en
  segundo plano](#run-hooks-in-the-background).
- Se admiten los controladores `command` y `mcp_tool`. Los controladores `prompt` y `agent`
  se analizan, pero se omiten.
- Los comandos se ejecutan con el `cwd` de la sesión como directorio de trabajo.
- Para los hooks locales del repositorio, es preferible resolver las rutas desde la raíz de Git en vez de usar una
  ruta relativa como `.codex/hooks/...`. Codex puede iniciarse desde un
  subdirectorio, y una ruta basada en la raíz de Git mantiene estable la ubicación del hook.

Configuración TOML equivalente definida directamente en `config.toml`:

```toml
[[hooks.SessionStart]]
matcher = "^compact$"

[[hooks.SessionStart.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/session_start.py"'
additionalContextLimit = 5000

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
timeout = 30
statusMessage = "Reviewing Bash output"

## Hooks de herramientas MCP

Un hook de herramienta MCP permite que un evento del ciclo de vida llame a una herramienta de un servidor MCP
que ya esté conectado. Envía argumentos estructurados directamente a la herramienta y usa el mismo
proceso de revisión de confianza y el mismo contrato de salida que un hook de comando.

### Configurar un hook de herramienta MCP

Este hook le pide al servidor MCP `scanner` que analice cada parche después de que Codex escriba o
edite archivos:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "mcp_tool",
            "server": "scanner",
            "tool": "scan_patch",
            "input": { "patch": "${tool_input.command}" },
            "timeout": 30,
            "statusMessage": "Scanning edited files"
          }
        ]
      }
    ]
  }
}

| Campo           | Significado                                                          |
| --------------- | ---------------------------------------------------------------- |
| `type`          | Debe ser `mcp_tool`.                                              |
| `server`        | Nombre obligatorio de un servidor MCP que ya esté conectado.                |
| `tool`          | Nombre obligatorio de una herramienta expuesta por ese servidor.                  |
| `input`         | Objeto JSON opcional con plantillas de argumentos. El valor predeterminado es `{}`.    |
| `timeout`       | Tiempo límite opcional de ejecución activa, en segundos. El valor predeterminado es `600`. |
| `statusMessage` | Mensaje opcional que se muestra mientras se ejecuta el hook.                      |

### Expandir argumentos a partir del evento del hook

Usa `${field.nested}` para leer un campo del evento del hook mediante notación de puntos. Un marcador de posición
que ocupa un valor completo conserva su tipo JSON. Un marcador de posición dentro de una cadena
más larga se representa como texto. Codex expande objetos y arreglos de forma recursiva.

Para un evento que contiene `{"tool_input":{"file_path":"src/main.rs","count":3}}`,
esta plantilla de argumentos:

```json
{
  "path": "${tool_input.file_path}",
  "count": "${tool_input.count}",
  "message": "Scanning ${tool_input.file_path}"
}

se convierte en:

```json
{
  "path": "src/main.rs",
  "count": 3,
  "message": "Scanning src/main.rs"
}

### Ejecución y ciclo de vida

- Los hooks usan una conexión MCP existente. No inician servidores ni los vuelven a conectar.
- Un hook puede bloquear una operación cuando la herramienta devuelve una decisión de bloqueo.
Los errores, los servidores ausentes y las herramientas no disponibles no bloquean la operación.
- Los hooks de herramientas MCP se ejecutan de forma síncrona. No solicitan aprobación para usar herramientas ni activan
otros hooks.
- Se aplica el menor de los tiempos de espera del hook y del servidor.
El tiempo dedicado a esperar una respuesta a una solicitud de información de MCP no se contabiliza para ese límite.
- Los hooks de `SessionStart` pueden ejecutarse antes de que un servidor MCP esté listo. Si eso ocurre,
  no bloquean la sesión.
- `SessionEnd` no admite hooks de herramientas MCP.

## Desactivar los hooks

Los hooks están habilitados de forma predeterminada. Para desactivarlos en `config.toml`, establece:

```toml
[features]
hooks = false

Usa `hooks` como clave canónica de la función. `codex_hooks` sigue funcionando como
alias obsoleto. Los administradores pueden forzar la desactivación de los hooks de la misma forma en
`requirements.toml` con `[features].hooks = false`.

## Hooks administrados desde `requirements.toml`

Los requisitos administrados por la empresa también pueden definir hooks directamente en `[hooks]`.
Esto es útil cuando los administradores quieren hacer cumplir la configuración de hooks y
distribuir los scripts mediante MDM u otro sistema de administración de dispositivos.
Para aplicar los hooks administrados incluso si los usuarios desactivaron los hooks localmente, fija
`[features].hooks = true` en `requirements.toml` junto con `[hooks]`. Para ignorar los hooks
de usuario, proyecto, sesión y complementos sin dejar de permitir los hooks
administrados por los administradores, establece `allow_managed_hooks_only = true`.

```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"

Notas sobre los hooks administrados:

- `managed_dir` se usa en macOS y Linux.
- `windows_managed_dir` se usa en Windows.
- Codex no distribuye los scripts de `managed_dir`; las herramientas de tu empresa
  deben instalarlos y actualizarlos por separado.
- Los comandos de los hooks administrados deberían usar rutas absolutas a los scripts dentro del
directorio administrado configurado.
- `allow_managed_hooks_only = true` omite los hooks de usuario, proyecto, sesión y
  complementos, pero sigue cargando los hooks administrados de `requirements.toml` y
  otras capas de configuración administradas.

## Hooks incluidos en complementos

Cuando se habilita un complemento, Codex puede cargar sus hooks de ciclo de vida
junto con los hooks de usuario, de proyecto y administrados.

De forma predeterminada, Codex busca `hooks/hooks.json` en la raíz del complemento. El archivo de manifiesto de un complemento
puede reemplazar esa opción predeterminada mediante una entrada `hooks` en
`.codex-plugin/plugin.json`. La entrada del archivo de manifiesto puede ser una ruta con el prefijo `./`, un
arreglo de rutas con el prefijo `./`, un objeto de hooks definido directamente o un arreglo de
objetos de hooks definidos directamente.

```json
{
  "name": "repo-policy",
  "hooks": "./hooks/hooks.json"
}

Las rutas de hooks del archivo de manifiesto se resuelven en relación con la raíz del complemento y deben permanecer
dentro de ella. Si un archivo de manifiesto define `hooks`, Codex usa esas entradas del archivo de manifiesto
en lugar del archivo predeterminado `hooks/hooks.json`.

Los comandos de los hooks de complementos reciben estas variables de entorno:

- `PLUGIN_ROOT` es una extensión específica de Codex que apunta a la raíz del
  complemento instalado.
- `PLUGIN_DATA` es una extensión específica de Codex que apunta al directorio de datos del complemento
  en el que se puede escribir.
- Codex también establece `CLAUDE_PLUGIN_ROOT` y `CLAUDE_PLUGIN_DATA` para
  mantener la compatibilidad con los hooks de complementos existentes.

Los hooks de los complementos usan el mismo esquema de eventos que los demás hooks. Instalar o habilitar un
complemento no hace que sus hooks se consideren automáticamente de confianza; Codex omite los hooks incluidos en el complemento
hasta que revises la definición actual del hook y la marques como de confianza.

## Patrones de coincidencia

El campo `matcher` es una cadena de expresión regular que filtra cuándo se activan los hooks. Usa `"*"`,
`""` u omite `matcher` por completo para que coincida con cada aparición de un evento
compatible.

Solo algunos eventos actuales de Codex tienen en cuenta `matcher`:

| Evento               | Qué filtra `matcher` | Notas                                                        |
| ------------------- | ---------------------- | ------------------------------------------------------------ |
| `PermissionRequest` | nombre de la herramienta              | Se admiten `Bash`, `apply_patch`\* y los nombres de herramientas MCP |
| `PostToolUse`       | nombre de la herramienta              | Consulta [Cobertura de herramientas](#tool-coverage)                          |
| `PostCompact`       | desencadenante de la compactación     | Los valores son `manual` o `auto`                                |
| `PreCompact`        | desencadenante de la compactación     | Los valores son `manual` o `auto`                                |
| `PreToolUse`        | nombre de la herramienta              | Consulta [Cobertura de herramientas](#tool-coverage)                          |
| `SessionEnd`        | motivo de finalización             | Actualmente, solo `other`                                       |
| `SessionStart`      | origen del inicio           | Los valores son `startup`, `resume`, `clear` y `compact`       |
| `SubagentStart`     | tipo de subagente          | Los valores dependen del subagente que se inicia                    |
| `SubagentStop`      | tipo de subagente          | Los valores dependen del subagente que se detiene                     |
| `UserPromptSubmit`  | no se admite          | Se ignora cualquier `matcher` configurado para este evento           |
| `Stop`              | no se admite          | Se ignora cualquier `matcher` configurado para este evento           |
| `Interrupt`         | no se admite          | Se ignora cualquier `matcher` configurado para este evento           |

\*Para `apply_patch`, los valores de `matcher` también pueden ser `Edit` o `Write`.

Ejemplos:

- `Bash`
- `^apply_patch$`
- `Edit|Write`
- `mcp__filesystem__read_file`
- `mcp__filesystem__.*`
- `startup|resume|clear|compact`
- `manual|auto`

### Cobertura de herramientas

`PreToolUse` y `PostToolUse` pueden observar otras llamadas además de las de shell y MCP. La mayoría de las
herramientas de función locales usan la misma ruta de hooks, por lo que puedes buscar coincidencias con su nombre,
inspeccionar sus argumentos JSON y, en el caso de `PreToolUse`, bloquear o reescribir la llamada.

| Ruta de la herramienta                         | `PreToolUse` | `PostToolUse` | Notas                                                                                                                    |
| --------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Comandos de shell                    | Sí          | Sí           | Usa `Bash` como patrón de coincidencia.                                                                                                         |
| Ejecución unificada (`exec_command`)     | Sí          | Sí           | Usa `Bash` como patrón de coincidencia. Una consulta posterior con `write_stdin` puede entregar el evento `PostToolUse` del comando original cuando ese comando termine. |
| `apply_patch`                     | Sí          | Sí           | Usa `apply_patch`, `Edit` o `Write` como patrón de coincidencia.                                                                              |
| Herramientas MCP                         | Sí          | Sí           | Busca coincidencias con el nombre de la herramienta MCP, por ejemplo, `mcp__filesystem__read_file`.                                                           |
| Otras herramientas de función locales        | Sí          | Sí           | Busca coincidencias con el nombre de la herramienta de función, por ejemplo, `update_plan`. `spawn_agent` también coincide con `Agent`.                                 |
| Herramientas alojadas, como `WebSearch` | No           | No            | Estas no usan la ruta de hooks para herramientas de función locales.                                                                       |

`write_stdin` sirve como mecanismo de transporte para una sesión existente de ejecución unificada. No vuelve a ejecutar
`PreToolUse` cuando envía datos de entrada o consulta el estado de un comando que ya pasó por
`PreToolUse`.

Algunas rutas de herramientas especializadas pueden omitir la ruta de hooks predeterminada. Considera los
hooks de herramientas como una medida de protección útil, no como un mecanismo de control completo.

## Campos de entrada comunes

Cada hook de comando recibe un objeto JSON mediante `stdin`.

Estos son los campos compartidos que usarás habitualmente:

| Campo             | Tipo             | Significado                                                             |
| ----------------- | ---------------- | ------------------------------------------------------------------- |
| `session_id`      | `string`         | ID de la sesión actual de Codex. Los hooks de subagentes usan el ID de la sesión padre. |
| `transcript_path` | `string \| null` | Ruta al archivo de transcripción de la sesión, si existe                         |
| `cwd`             | `string`         | Directorio de trabajo de la sesión                                   |
| `hook_event_name` | `string`         | Nombre del evento de hook actual                                             |
| `model`           | `string`         | Extensión específica de Codex. Slug del modelo activo                         |

Los hooks asociados a un turno incluyen `turn_id` como una extensión específica de Codex en sus
tablas específicas de cada evento.

`SessionStart`, `PreToolUse`, `PermissionRequest`, `PostToolUse`,
`UserPromptSubmit`, `SubagentStart`, `SubagentStop`, `Stop` y `Interrupt` también incluyen
`permission_mode`, que describe el modo de permisos actual con los valores `default`,
`acceptEdits`, `plan`, `dontAsk` o `bypassPermissions`.

`transcript_path` apunta a una transcripción del chat para mayor comodidad, pero el
formato de la transcripción no es una interfaz estable para los hooks y puede cambiar con el tiempo.

Si necesitas el formato de intercambio completo, consulta [Esquemas](#schemas).

## Campos de salida comunes

`SessionStart`, `PreCompact`, `PostCompact`, `UserPromptSubmit`,
`SubagentStop` y `Stop` admiten estos campos JSON compartidos. `SubagentStart`
acepta la misma estructura para `systemMessage` y el contexto específico del hook, pero
`continue: false` no detiene al subagente:

```json
{
  "continue": true,
  "stopReason": "optional",
  "systemMessage": "optional",
  "suppressOutput": false
}

| Campo            | Efecto                                          |
| ---------------- | ----------------------------------------------- |
| `continue`       | Si su valor es `false`, marca esa ejecución del hook como detenida      |
| `stopReason`     | Se registra como el motivo de la detención             |
| `systemMessage`  | Se muestra como advertencia en la interfaz de usuario o en el flujo de eventos |
| `suppressOutput` | Actualmente se analiza sintácticamente, pero aún no está implementado            |

Finalizar con el código `0` sin generar salida se considera un éxito y Codex continúa.

`PreToolUse` y `PermissionRequest` admiten `systemMessage`, pero `continue`,
`stopReason` y `suppressOutput` no se admiten actualmente para esos eventos.
Si un hook `PreToolUse` devuelve uno de esos campos no admitidos, Codex marca
esa ejecución del hook como fallida, informa el error y continúa con la llamada a la herramienta.

`PostToolUse` admite `systemMessage`, `continue: false` y `stopReason`.
`suppressOutput` se analiza sintácticamente, pero actualmente no se admite para ese evento.

### Salidas extensas de hooks

De forma predeterminada, Codex limita a aproximadamente
2500 tokens cada mensaje de salida de un hook visible para el modelo. Si un hook devuelve más contenido, Codex guarda el texto completo en
`<temp_dir>/hook_outputs/<session_id>/<uuid>.txt` y proporciona al modelo una
vista previa del inicio y del final que incluye la ruta del archivo guardado. Este comportamiento se denomina
**volcado a disco**: Codex almacena en disco las salidas demasiado extensas y las reemplaza por una
vista previa más breve y visible para el modelo. Si no se puede escribir el archivo, el modelo aun así
recibe una vista previa truncada.

  Mantén conciso el contexto de los hooks y complementos. El contexto de varios hooks y complementos
  se acumula y puede reducir el rendimiento del modelo. Aumentar `additionalContextLimit`
  incrementa ese riesgo. Evita establecer el límite en `0`, a menos que el hook aplique un
  límite de salida estricto; de lo contrario, un solo hook puede consumir toda la ventana de
  contexto.

Para cualquier hook de comando que devuelva `additionalContext`, establece
`additionalContextLimit` en el controlador para personalizar el umbral aproximado de
tokens:

```json
{
  "type": "command",
  "command": "python3 ~/.codex/hooks/session_start.py",
  "additionalContextLimit": 5000
}

Omite `additionalContextLimit` para usar el umbral predeterminado de `2500` tokens. Usa un
entero positivo para seleccionar un umbral diferente o `0` para pasar todo el contexto adicional del controlador
directamente al modelo. Codex evalúa cada
controlador coincidente de forma independiente. Para los eventos que no pueden generar
contexto adicional, Codex ignora `additionalContextLimit` y muestra una advertencia de
configuración.

La configuración se aplica solo a `additionalContext`. La retroalimentación de las herramientas y los prompts de
continuación conservan el límite predeterminado.

Como las salidas demasiado extensas pueden escribirse en disco, evita devolver secretos u
otros datos confidenciales en la salida del hook.

## Ejecutar hooks en segundo plano

De forma predeterminada, Codex espera a que finalice un hook de comando antes de continuar con la
operación que lo activó. Establece `async` en `true` para ejecutar un hook de comando en
segundo plano mientras Codex continúa.

### Configurar un hook en segundo plano

Agrega `"async": true` a un manejador de comandos en `hooks.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/post_tool_use.py",
            "async": true,
            "timeout": 120
          }
        ]
      }
    ]
  }
}

Para un hook definido directamente en `config.toml`, establece `async = true`:

```toml
[[hooks.PostToolUse]]
matcher = "Bash"

[[hooks.PostToolUse.hooks]]
type = "command"
command = "python3 ~/.codex/hooks/post_tool_use.py"
async = true
timeout = 120

En los hooks en segundo plano, la entrada, el criterio de coincidencia, la revisión de confianza, el tiempo de espera y el
[manejo de salidas extensas](#large-hook-output) son los mismos que en los hooks de comando síncronos. Al igual que
en otros hooks de comando, `timeout` se mide en segundos y su valor predeterminado es
`600`. Los hooks `Interrupt` usan un tiempo de espera predeterminado de un segundo y un máximo de tres segundos,
incluso cuando se ejecutan en segundo plano.

### Cómo se ejecutan los hooks en segundo plano

Cuando un hook en segundo plano finaliza, Codex entrega la salida informativa que admite
en el siguiente punto seguro de la conversación:

- Si hay un turno activo, Codex espera a que finalicen la solicitud actual al modelo y las llamadas a herramientas,
y luego pone la salida a disposición de la siguiente solicitud al modelo en ese
turno.
- Si no hay ningún turno activo, Codex espera hasta el siguiente turno del usuario. La finalización de un
hook en segundo plano no inicia un turno nuevo.

Usa la misma salida JSON específica del evento que usarías en un hook síncrono. Codex agrega
`additionalContext` al contexto del modelo y muestra `systemMessage` como una
advertencia.

  Los hooks en segundo plano no pueden bloquear, aprobar, reescribir ni controlar de ninguna otra forma la
operación que los activó. Usa hooks síncronos para las políticas de herramientas,
las decisiones sobre permisos, el rechazo de prompts o la continuación de turnos.

### Limitaciones

- Codex ejecuta hasta ocho hooks en segundo plano de forma concurrente por sesión. Los hooks adicionales
esperan hasta que finalice uno de los que están en ejecución.
- Cada invocación coincidente se ejecuta de forma independiente, y los hooks en segundo plano pueden finalizar
en un orden distinto al de inicio.
- Cuando finaliza la sesión, Codex cancela los hooks en segundo plano que no hayan terminado y descarta
la salida que no se haya entregado.
- Los hooks `SessionEnd` siempre se ejecutan de forma síncrona.

## Hooks

### SessionStart

`matcher` se aplica a `source` para este evento.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo    | Tipo     | Significado                                                             |
| -------- | -------- | ------------------------------------------------------------------- |
| `source` | `string` | Cómo se inició la sesión: `startup`, `resume`, `clear` o `compact` |

El texto sin formato en `stdout` se agrega como contexto adicional de desarrollador.

El JSON en `stdout` admite los [campos de salida comunes](#common-output-fields) y esta
estructura específica del hook:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Load the workspace conventions before editing."
  }
}

Ese texto de `additionalContext` se agrega como contexto adicional de desarrollador.

Después de que Codex compacta una sesión raíz, los hooks `SessionStart` que coinciden con
`source: "compact"` se ejecutan antes de la siguiente solicitud al modelo. Esto también se aplica cuando
la compactación automática ocurre a mitad de un turno: Codex entrega el contexto
adicional del hook a la continuación inmediata en vez de esperar a un
turno posterior del usuario. Si el hook devuelve `continue: false`, Codex finaliza el turno
sin enviar otra solicitud al modelo.

### SessionEnd

`SessionEnd` te permite ejecutar un comando cuando finaliza una sesión, por ejemplo, para guardar notas
finales o limpiar archivos. Se ejecuta en el hilo principal cuando archivas o
eliminas una conversación que sigue abierta, cuando Codex se cierra normalmente o después de que una
conversación haya permanecido inactiva y sin estar abierta en ningún cliente conectado durante 30
minutos. No se ejecuta para subagentes.

Cambiar de conversación o llamar a `thread/unsubscribe` no finaliza
la sesión de inmediato, por lo que `SessionEnd` tampoco se ejecuta de inmediato. Tu hook aún puede
leer la transcripción de la sesión mientras se ejecuta.

`matcher` filtra `reason` para este evento. Por ahora, `reason` siempre es `other`.
Puedes omitir `matcher` o usar `other` para que el hook se ejecute en todos los eventos `SessionEnd`.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo    | Tipo     | Significado                        |
| -------- | -------- | ------------------------------ |
| `reason` | `string` | Motivo por el que finalizó la sesión: `other` |

Por ejemplo, un comando `SessionEnd` recibe:

```json
{
  "session_id": "thr_123",
  "transcript_path": "/workspace/.codex/rollout.jsonl",
  "cwd": "/workspace",
  "hook_event_name": "SessionEnd",
  "reason": "other"
}

Los hooks `SessionEnd` siempre se ejecutan de forma síncrona, incluso cuando `async` es `true`. Son
de carácter informativo, por lo que su salida no influirá en el comportamiento de Codex ni mantendrá abierto el hilo. Si un
comando supera el tiempo de espera o finaliza con un error, Codex lo informa como una falla del hook.

### SubagentStart

`matcher` se aplica a `agent_type` para este evento.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo             | Tipo     | Significado                                        |
| ----------------- | -------- | ---------------------------------------------- |
| `turn_id`         | `string` | Extensión específica de Codex. Identificador del turno activo de Codex |
| `agent_id`        | `string` | Identificador del subagente                    |
| `agent_type`      | `string` | Tipo o perfil del subagente                       |
| `permission_mode` | `string` | Modo de permisos actual                        |

El texto sin formato en `stdout` se agrega como contexto adicional de desarrollador para el subagente.

El JSON en `stdout` admite `systemMessage` y esta estructura específica del hook:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Review the repository test conventions first."
  }
}

Ese texto de `additionalContext` se agrega como contexto adicional de desarrollador para el
subagente. `continue: false` se analiza por compatibilidad, pero no impide que el
subagente se inicie.

### PreToolUse

`PreToolUse` puede interceptar Bash, las ediciones de archivos realizadas mediante `apply_patch`,
las llamadas a herramientas MCP y otras herramientas de función locales. Consulta [Cobertura de
herramientas](#tool-coverage) para conocer las rutas compatibles y las excepciones.

`matcher` se aplica a `tool_name` y a los alias de coincidencia. Para las ediciones de archivos mediante
`apply_patch`, los valores de `matcher` pueden ser `apply_patch`, `Edit` o `Write`; la entrada del hook
sigue indicando `tool_name: "apply_patch"`.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo         | Tipo         | Significado                                                                                                                          |
| ------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`     | `string`     | Extensión específica de Codex. Identificador del turno activo de Codex                                                                                   |
| `tool_name`   | `string`     | Nombre canónico de la herramienta para el hook, como `Bash`, `apply_patch` o un nombre MCP como `mcp__fs__read`                                     |
| `tool_use_id` | `string`     | Identificador de la llamada a la herramienta para esta invocación                                                                                                 |
| `tool_input`  | `JSON value` | Entrada específica de la herramienta. `Bash` y `apply_patch` usan `tool_input.command`. Las herramientas MCP y otras herramientas de función locales envían sus argumentos. |

Se ignora el texto sin formato en `stdout`.

El JSON en `stdout` puede usar `systemMessage`. Para denegar una llamada a una herramienta compatible, devuelve
esta estructura específica del hook:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook."
  }
}

Codex también acepta esta estructura de bloqueo anterior:

```json
{
  "decision": "block",
  "reason": "Destructive command blocked by hook."
}

También puedes usar el código de salida `2` y escribir el motivo del bloqueo en `stderr`.

Para agregar contexto visible para el modelo sin bloquear, devuelve
`hookSpecificOutput.additionalContext`:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "The pending command touches generated files."
  }
}

Para reescribir una llamada a una herramienta compatible sin bloquearla, devuelve
`permissionDecision: "allow"` con `updatedInput`:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "echo rewritten"
    }
  }
}

Para los comandos de Bash y `apply_patch`, `updatedInput` debe incluir un campo
`command` de tipo cadena. Para MCP y otras herramientas de funciones locales, `updatedInput` es el
objeto de argumentos de reemplazo. Devuelve `updatedInput` solo con
`permissionDecision: "allow"`; las demás estructuras de `updatedInput` se reportan como
errores.

`permissionDecision: "ask"`, la forma heredada `decision: "approve"`, `continue: false`,
`stopReason` y `suppressOutput` se analizan, pero aún no se admiten. Codex marca
la ejecución del hook como fallida, informa el error y continúa con la llamada a la herramienta.

### PermissionRequest

`PermissionRequest` se ejecuta cuando Codex está por solicitar aprobación, por ejemplo, para una
elevación de permisos del shell o una aprobación de red administrada. Puede permitir o denegar
la solicitud, o abstenerse de decidir y dejar que continúe la solicitud de aprobación habitual.
No se ejecuta para los comandos que no necesitan aprobación.

`matcher` se aplica a `tool_name` y a los alias de coincidencia. Los valores canónicos actuales
incluyen `Bash`, `apply_patch` y nombres de herramientas de MCP como
`mcp__server__tool`; `apply_patch` también coincide con `Edit` y `Write`.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo                    | Tipo             | Significado                                                                                                        |
| ------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------- |
| `turn_id`                | `string`         | Extensión específica de Codex. ID del turno activo de Codex                                                                 |
| `tool_name`              | `string`         | Nombre canónico de la herramienta del hook, como `Bash`, `apply_patch` o un nombre de MCP como `mcp__fs__read`                   |
| `tool_input`             | `JSON value`     | Entrada específica de la herramienta. `Bash` y `apply_patch` usan `tool_input.command`, mientras que las herramientas de MCP envían todos los argumentos. |
| `tool_input.description` | `string \| null` | Motivo de aprobación en formato legible, cuando Codex dispone de uno                                                             |

Se ignora el texto sin formato en `stdout`.

Algunas entradas de herramientas pueden incluir una descripción legible, pero no supongas que existe un campo
`tool_input.description` para todas las herramientas.

Para aprobar la solicitud, devuelve:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow"
    }
  }
}

Para denegar la solicitud, devuelve:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "deny",
      "message": "Blocked by repository policy."
    }
  }
}

Si varios hooks coincidentes devuelven decisiones, cualquier `deny` tiene prioridad. En caso contrario, un
`allow` permite que la solicitud continúe sin mostrar la solicitud de aprobación. Si ningún
hook coincidente decide, Codex usa el flujo de aprobación habitual.

No devuelvas `updatedInput`, `updatedPermissions` ni `interrupt` para
`PermissionRequest`; esos campos están reservados para comportamientos futuros y actualmente bloquean
la solicitud.

### PostToolUse

`PostToolUse` se ejecuta después de que las herramientas compatibles generan una salida, incluidos Bash,
`apply_patch`, las llamadas a herramientas de MCP y otras herramientas de funciones locales. Para Bash,
también se ejecuta después de los comandos que terminan con un estado distinto de cero. No puede deshacer los efectos
secundarios de una herramienta que ya se ejecutó. Consulta [Cobertura de herramientas](#tool-coverage) para conocer
las rutas admitidas y las excepciones.

`matcher` se aplica a `tool_name` y a los alias de coincidencia. Para las ediciones de archivos mediante
`apply_patch`, los valores de `matcher` pueden ser `apply_patch`, `Edit` o `Write`; la entrada del hook
sigue indicando `tool_name: "apply_patch"`.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo           | Tipo         | Significado                                                                                                                          |
| --------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`       | `string`     | Extensión específica de Codex. ID del turno activo de Codex                                                                                   |
| `tool_name`     | `string`     | Nombre canónico de la herramienta del hook, como `Bash`, `apply_patch` o un nombre de MCP como `mcp__fs__read`                                     |
| `tool_use_id`   | `string`     | ID de la llamada a la herramienta para esta invocación                                                                                                 |
| `tool_input`    | `JSON value` | Entrada específica de la herramienta. `Bash` y `apply_patch` usan `tool_input.command`. Las herramientas de MCP y otras herramientas de funciones locales envían sus argumentos. |
| `tool_response` | `JSON value` | Salida específica de la herramienta. Las herramientas de MCP envían el resultado de la llamada de MCP. Otras herramientas de funciones locales normalmente envían su salida destinada al modelo.    |

Se ignora el texto sin formato en `stdout`.

El JSON en `stdout` puede usar `systemMessage` y esta estructura específica del hook:

```json
{
  "decision": "block",
  "reason": "The Bash output needs review before continuing.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command updated generated files."
  }
}

Ese texto de `additionalContext` se agrega como contexto adicional de desarrollador.

Para este evento, `decision: "block"` no revierte el comando de Bash ya ejecutado.
En cambio, Codex registra los comentarios, reemplaza el resultado de la herramienta con esos
comentarios y hace que el modelo continúe a partir del mensaje proporcionado por el hook.

También puedes usar el código de salida `2` y escribir el motivo de los comentarios en `stderr`.

Para detener el procesamiento normal del resultado original de la herramienta después de que el comando ya se haya
ejecutado, devuelve `continue: false`. Codex reemplazará el resultado de la herramienta con
tus comentarios o el texto de detención y continuará desde allí.

`updatedMCPToolOutput` y `suppressOutput` se analizan, pero aún no se admiten.
Codex marca la ejecución del hook como fallida, informa el error y continúa con el procesamiento
normal del resultado de la herramienta.

#### Llamadas a herramientas desde el modo de código

Cuando un modelo usa el modo de código para llamar a una herramienta desde JavaScript, las decisiones de los hooks se aplican
a esa llamada anidada. `PreToolUse` puede detener la herramienta antes de que se ejecute o reescribir
su entrada. Un `PostToolUse` que bloquea no puede deshacer los efectos secundarios de la herramienta, pero
puede impedir que el resultado original llegue al script en ejecución.

| Resultado del hook                                                      | Lo que ve el modo de código                                                                                    |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `PreToolUse` bloquea                                              | La promesa de la herramienta se rechaza antes de que esta se ejecute.                                                         |
| `PreToolUse` devuelve `updatedInput`                              | La herramienta se ejecuta con la entrada reescrita y la promesa se resuelve con ese resultado.                      |
| `PostToolUse` devuelve `decision: "block"` o termina con el código `2` | La herramienta se ejecuta y luego la promesa se rechaza con el motivo del hook.                                          |
| `PostToolUse` devuelve `continue: false`                          | Codex usa los comentarios del hook como resultado visible para el modelo, pero no rechaza la promesa de la llamada anidada a la herramienta. |

### PreCompact

`PreCompact` se ejecuta antes de que Codex compacte el chat. `matcher` se aplica
a `trigger`, cuyos valores son `manual` y `auto`.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo     | Tipo     | Significado                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Extensión específica de Codex. ID del turno activo de Codex |
| `trigger` | `string` | Qué activó la compactación: `manual` o `auto`  |

Se ignora el texto sin formato en `stdout`.

El JSON en `stdout` admite los [campos de salida comunes](#common-output-fields). Si un
hook `PreCompact` coincidente devuelve `continue: false`, Codex se detiene antes de
compactar.

### PostCompact

`PostCompact` se ejecuta después de que Codex compacta el chat. `matcher` se aplica
a `trigger`, cuyos valores son `manual` y `auto`.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo     | Tipo     | Significado                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Extensión específica de Codex. ID del turno activo de Codex |
| `trigger` | `string` | Qué desencadenó la compactación: `manual` o `auto`  |

Se ignora el texto sin formato en `stdout`.

El JSON en `stdout` admite los [campos de salida comunes](#common-output-fields). Si un
hook `PostCompact` coincidente devuelve `continue: false`, Codex se detiene después de
compactar.

### UserPromptSubmit

`matcher` no se usa actualmente para este evento.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo     | Tipo     | Significado                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Extensión específica de Codex. ID del turno activo de Codex |
| `prompt`  | `string` | Prompt del usuario que está a punto de enviarse            |

El texto sin formato en `stdout` se agrega como contexto adicional de desarrollador.

El JSON en `stdout` admite los [campos de salida comunes](#common-output-fields) y
esta estructura específica del hook:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Ask for a clearer reproduction before editing files."
  }
}

Ese texto de `additionalContext` se agrega como contexto adicional de desarrollador.

Para bloquear el prompt, devuelve:

```json
{
  "decision": "block",
  "reason": "Ask for confirmation before doing that."
}

También puedes usar el código de salida `2` y escribir el motivo del bloqueo en `stderr`.

### SubagentStop

`matcher` se aplica a `agent_type` para este evento.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo                    | Tipo             | Significado                                         |
| ------------------------ | ---------------- | ----------------------------------------------- |
| `turn_id`                | `string`         | Extensión específica de Codex. ID del turno activo de Codex  |
| `agent_id`               | `string`         | Identificador del subagente                     |
| `agent_type`             | `string`         | Tipo o perfil del subagente                        |
| `agent_transcript_path`  | `string \| null` | Ruta del archivo de transcripción del subagente, si existe    |
| `stop_hook_active`       | `boolean`        | Si este subagente ya continuó     |
| `last_assistant_message` | `string \| null` | Mensaje más reciente del subagente como asistente, si está disponible |

`SubagentStop` espera datos JSON en `stdout` cuando finaliza con el código `0`. La salida en texto sin formato no es
válida para este evento.

El JSON en `stdout` admite los [campos de salida comunes](#common-output-fields). Para pedirle
a Codex que continúe el flujo del subagente, devuelve:

```json
{
  "decision": "block",
  "reason": "Run one more focused pass inside the subagent."
}

También puedes usar el código de salida `2` y escribir el motivo para continuar en `stderr`.

Si algún hook `SubagentStop` coincidente devuelve `continue: false`, esa decisión tiene
prioridad sobre las decisiones de continuación de otros hooks `SubagentStop`
coincidentes.

### Stop

`matcher` no se usa actualmente para este evento.

Campos adicionales a los [campos de entrada comunes](#common-input-fields):

| Campo                    | Tipo             | Significado                                           |
| ------------------------ | ---------------- | ------------------------------------------------- |
| `turn_id`                | `string`         | Extensión específica de Codex. ID del turno activo de Codex    |
| `stop_hook_active`       | `boolean`        | Si `Stop` ya hizo que este turno continuara |
| `last_assistant_message` | `string \| null` | Texto del mensaje más reciente del asistente, si está disponible       |

`Stop` espera datos JSON en `stdout` cuando finaliza con el código `0`. La salida en texto sin formato no es válida
para este evento.

El JSON en `stdout` admite los [campos de salida comunes](#common-output-fields). Para que
Codex continúe, devuelve:

```json
{
  "decision": "block",
  "reason": "Run one more pass over the failing tests."
}

También puedes usar el código de salida `2` y escribir el motivo para continuar en `stderr`.

Para este evento, `decision: "block"` no rechaza el turno. En su lugar, le indica
a Codex que continúe y crea automáticamente un nuevo prompt de continuación que funciona
como un nuevo prompt del usuario, con el valor de `reason` que proporcionaste como texto.

Si algún hook `Stop` coincidente devuelve `continue: false`, esa decisión tiene prioridad
sobre las decisiones de continuación de otros hooks `Stop` coincidentes.

### Interrupt

`Interrupt` se ejecuta cuando interrumpes un turno activo en el hilo principal. Úsalo
para registrar la interrupción o hacer la limpieza del trabajo iniciado por un hook. No se ejecuta
para hilos inactivos ni subagentes, y se ignora cualquier `matcher` configurado.

Además de los [campos de entrada comunes](#common-input-fields), el evento incluye
`turn_id`, el ID del turno interrumpido, y `permission_mode`.

Los hooks de comando tienen un tiempo de espera predeterminado de un segundo. Los tiempos de espera configurados
deben ser de entre uno y tres segundos. La salida del hook no puede impedir la
interrupción ni reiniciar el turno. Finaliza con el código `0` sin generar salida o devuelve JSON con
un `systemMessage` opcional para mostrar una advertencia. La salida en texto sin formato no es válida
para este evento.

```json
{ "systemMessage": "Saved the interrupted turn to the local audit log." }

## Esquemas

  Los esquemas enlazados de la rama `main` pueden incluir campos de hooks que no están en la
  versión actual. Usa esta página como referencia del comportamiento de la versión actual.

Si necesitas el formato de transmisión exacto que se usa actualmente, consulta los esquemas generados en el
[repositorio de Codex en GitHub](https://github.com/openai/codex/tree/main/codex-rs/hooks/schema/generated).
