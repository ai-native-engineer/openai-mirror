<!-- source: https://learn.chatgpt.com/es-419/docs/config-file/config-basic -->

Codex lee los detalles de configuración desde varias ubicaciones. Tus valores predeterminados personales están en `~/.codex/config.toml` y puedes usar archivos `.codex/config.toml` para reemplazarlos en proyectos específicos. Por seguridad, Codex solo carga las capas `.codex/` de un proyecto si confías en él.

## Archivo de configuración de Codex

Codex almacena la configuración del usuario en `~/.codex/config.toml`. Para que los ajustes se apliquen a un proyecto o una subcarpeta específicos, agrega un archivo `.codex/config.toml` en tu repositorio.

Para abrir el archivo de configuración desde la extensión de Codex para IDE, selecciona el ícono de engranaje en la esquina superior derecha y luego selecciona **Configuración de Codex \> Abrir config.toml**.

La CLI y la extensión para IDE comparten las mismas capas de configuración. Puedes usarlas para:

- Establecer el modelo y el proveedor predeterminados.
- Configurar [políticas de aprobación y ajustes del sandbox](/es-419/codex/agent-approvals-security#sandbox-and-approvals).
- Configurar [servidores MCP](/es-419/codex/extend/mcp).

## Prioridad de la configuración

Codex resuelve los valores en este orden (primero los de mayor prioridad):

1. Flags de la CLI y valores definidos mediante `--config`
2. Archivos de configuración del proyecto: `.codex/config.toml`, ordenados desde la raíz del proyecto hasta tu directorio de trabajo actual (el más cercano tiene prioridad; solo para proyectos de confianza)
3. Archivos de [perfil](/es-419/codex/config-file/config-advanced#profiles) seleccionados con `--profile profile-name` (`~/.codex/profile-name.config.toml`)
4. Configuración del usuario: `~/.codex/config.toml`
5. Configuración del sistema (si existe): `/etc/codex/config.toml` en Unix
6. Valores predeterminados integrados

Usa ese orden de prioridad para establecer valores predeterminados compartidos en `config.toml` y reserva los [archivos de perfil](/es-419/codex/config-file/config-advanced#profiles) para los valores que difieren.

Si marcas un proyecto como no confiable, Codex omite las capas `.codex/` específicas del proyecto, lo que incluye la configuración local del proyecto, los hooks y las reglas. La configuración del usuario y del sistema se sigue cargando, incluidos los hooks y las reglas de alcance global o del usuario.

Para reemplazar valores de forma puntual mediante `-c`/`--config` (incluidas las reglas de uso de comillas de TOML), consulta [Configuración avanzada](/es-419/codex/config-file/config-advanced#one-off-overrides-from-the-cli).

  En equipos administrados, tu organización también puede imponer restricciones mediante
`requirements.toml` (por ejemplo, prohibir `approval_policy = "never"` o
`sandbox_mode = "danger-full-access"`). Consulta [Configuración
  administrada](/es-419/codex/enterprise/managed-configuration) y [Requisitos
  impuestos por el administrador](/es-419/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

## Opciones de configuración comunes

Estas son algunas de las opciones que se modifican con más frecuencia:

#### Modelo predeterminado

Elige el modelo que Codex usa de forma predeterminada en la CLI y el IDE.

#### Solicitudes de aprobación

Controla cuándo Codex se detiene para solicitar aprobación antes de ejecutar los comandos generados.

```toml
approval_policy = "on-request"

Para conocer las diferencias de comportamiento entre `untrusted`, `on-request` y `never`, consulta [Ejecutar sin solicitudes de aprobación](/es-419/codex/agent-approvals-security#run-without-approval-prompts) y [Combinaciones comunes de sandbox y aprobación](/es-419/codex/agent-approvals-security#common-sandbox-and-approval-combinations).

#### Nivel de sandbox

Ajusta el nivel de acceso al sistema de archivos y a la red que tiene Codex mientras ejecuta comandos.

```toml
sandbox_mode = "workspace-write"

Para conocer el comportamiento de cada modo (incluidas las rutas protegidas `.git`/`.codex` y los valores predeterminados de red), consulta [Sandbox y aprobaciones](/es-419/codex/agent-approvals-security#sandbox-and-approvals), [Rutas protegidas en directorios raíz con permisos de escritura](/es-419/codex/agent-approvals-security#protected-paths-in-writable-roots) y [Acceso a la red](/es-419/codex/agent-approvals-security#network-access).

#### Perfiles de permisos

Codex también admite perfiles de permisos con nombre para reutilizar políticas del sistema de archivos y
de red. Los perfiles integrados son `:read-only`, `:workspace` y
`:danger-full-access`. Los perfiles personalizados usan tablas `[permissions.<name>]` y un
valor de `default_permissions` que coincida con el nombre del perfil. Consulta [Permisos](/es-419/codex/permissions).

#### Modo del sandbox de Windows

Cuando ejecutes Codex de forma nativa en Windows, establece el modo del sandbox nativo en `elevated` dentro de la tabla `windows`. Usa `unelevated` solo si no tienes permisos de administrador o si falla la configuración con privilegios elevados.

```toml
[windows]
sandbox = "elevated"   # Recommended
# sandbox = "unelevated" # Fallback if admin permissions/setup are unavailable

#### Modo de búsqueda web

Codex habilita la búsqueda web de forma predeterminada para los chats locales y proporciona los resultados desde una caché de búsqueda web. Esta caché es un índice de resultados web que mantiene OpenAI, por lo que el modo en caché devuelve resultados preindexados en lugar de consultar páginas en tiempo real. Esto reduce la exposición a la inyección de prompts proveniente de contenido web arbitrario obtenido en tiempo real, pero aun así debes tratar los resultados web como no confiables. Si usas `--yolo` u otra [configuración del sandbox con acceso completo](/es-419/codex/agent-approvals-security#common-sandbox-and-approval-combinations), la búsqueda web usa resultados en tiempo real de forma predeterminada. Elige un modo con `web_search`:

- `"cached"` (opción predeterminada) devuelve resultados de la caché de búsqueda web.
- `"indexed"` permite el acceso externo a la web solo cuando el índice de búsqueda autoriza la solicitud.
- `"live"` obtiene los datos más recientes de la web (equivale a `--search`).
- `"disabled"` desactiva la herramienta de búsqueda web.

```toml
web_search = "cached"  # default; serves results from the web search cache
# web_search = "indexed" # gate external web access through the search index
# web_search = "live"  # fetch the most recent data from the web (same as --search)
# web_search = "disabled"

#### Esfuerzo de razonamiento

Ajusta el esfuerzo de razonamiento que aplica el modelo, si este lo admite.

```toml
model_reasoning_effort = "high"

#### Estilo de comunicación

Establece un estilo de comunicación predeterminado para los modelos compatibles.

```toml
personality = "friendly" # or "pragmatic" or "none"

Puedes cambiar esta opción más adelante en una sesión activa mediante `/personality`, o para cada hilo o turno cuando uses las API de App Server.

#### Asignación de teclas de la TUI

Personaliza los atajos del terminal en `tui.keymap`. Algunas acciones del editor usan como alternativa las asignaciones correspondientes de `tui.keymap.global`; las asignaciones específicas del contexto tienen prioridad cuando se admiten. Una lista vacía elimina las asignaciones de teclas de la acción.

```toml
[tui.keymap.global]
open_transcript = "ctrl-t"

[tui.keymap.composer]
submit = ["enter", "ctrl-m"]

[tui.keymap.chat]
interrupt_turn = "f12"

#### Entorno de los comandos

Controla qué variables de entorno pasa Codex a los comandos que inicia. Usa
filtros por clave para conservar solo las variables que necesitas:

```toml
[shell_environment_policy]
ignore_default_excludes = false

[shell_environment_policy.filters]
"PATH" = "include"
"HOME" = "include"

`ignore_default_excludes` tiene `true` como valor predeterminado, lo que omite el filtrado automático
de los nombres de variables que contienen `KEY`, `SECRET` o `TOKEN`. Establécelo en `false`
si quieres aplicar ese filtrado automático. Para conocer las reglas de exclusión, el orden de prioridad y la
configuración heredada, consulta [Política del entorno de
shell](/es-419/codex/config-file/config-advanced#shell-environment-policy).

#### Directorio de registros

Cambia la ubicación en la que Codex escribe los archivos de registro locales. Establecer `log_dir` explícitamente también
habilita en ese directorio el registro opcional de la TUI en texto sin formato, `codex-tui.log`.

```toml
log_dir = "/absolute/path/to/codex-logs"

Para ejecuciones puntuales, también puedes establecerlo desde la CLI:

```bash
codex -c log_dir=./.codex-log

## Flags de funciones

Usa la tabla `[features]` de `config.toml` para activar o desactivar capacidades opcionales y experimentales.

### Flags de funciones comunes

| Clave                  |        Valor predeterminado        | Madurez     | Descripción                                                                              |
| -------------------- | :-------------------: | ------------ | ---------------------------------------------------------------------------------------- |
| `apps`               |         true          | Estable       | Habilita las integraciones con apps (conectores)                                                      |
| `goals`              |         true          | Estable       | Habilita los objetivos persistentes y la continuación automática                                        |
| `hooks`              |         true          | Estable       | Habilita los hooks del ciclo de vida desde `hooks.json` o mediante `[hooks]` en línea. Consulta [Hooks](/es-419/codex/hooks). |
| `fast_mode`          |         true          | Estable       | Habilita la selección del Modo rápido y su uso mediante `service_tier = "fast"`                          |
| `memories`           |         false         | Experimental | Habilita [Memorias](/es-419/codex/customization/memories)                                         |
| `multi_agent`        |         true          | Estable       | Habilita las herramientas de colaboración entre subagentes                                                      |
| `personality`        |         true          | Estable       | Habilita los controles para seleccionar la personalidad                                                    |
| `remote_plugin`      |         true          | Estable       | Habilita el catálogo remoto de complementos                                                         |
| `shell_snapshot`     |         true          | Estable       | Guarda una instantánea de tu entorno de shell para acelerar la ejecución de comandos repetidos                            |
| `shell_tool`         |         true          | Estable       | Habilita la herramienta `shell` predeterminada                                                          |
| `unified_exec`       | `true` excepto en Windows | Estable       | Usa la herramienta exec unificada basada en PTY                                                     |
| `web_search`         |         true          | En desuso   | Opción heredada; se recomienda usar el ajuste `web_search` de nivel superior                                 |
| `web_search_cached`  |         false         | En desuso   | Opción heredada que se asigna a `web_search = "cached"` cuando no está definida                            |
| `web_search_request` |         false         | En desuso   | Opción heredada que se asigna a `web_search = "live"` cuando no está definida                              |

  Esta tabla enumera los flags comunes disponibles para los usuarios, no todas las funciones internas o
  en desarrollo. La columna Madurez usa etiquetas como
  Experimental, Beta y Estable. Consulta [Madurez de las
  funciones](/es-419/codex/feature-maturity) para saber cómo interpretar estas etiquetas.

Omite las claves de las funciones para conservar sus valores predeterminados.

Para configurar los hooks del ciclo de vida, consulta [Hooks](/es-419/codex/hooks).

### Habilitar funciones

- En `config.toml`, agrega `feature_name = true` en la sección `[features]`.
- Desde la CLI, ejecuta `codex --enable feature_name`.
- Para habilitar más de una función, ejecuta `codex --enable feature_a --enable feature_b`.
- Para deshabilitar una función, establece su clave en `false` dentro de `config.toml`.
