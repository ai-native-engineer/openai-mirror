<!-- source: https://learn.chatgpt.com/es-419/docs/agent-approvals-security -->

Codex ayuda a proteger tu código y tus datos, y reduce el riesgo de uso indebido.

  Esta página explica cómo operar Codex de forma segura, incluido el entorno aislado, las aprobaciones
  y el acceso a la red. Si buscas Codex Security, el producto para
  analizar repositorios de GitHub conectados, consulta [Codex Security](/es-419/codex/security).

De forma predeterminada, el agente se ejecuta con el acceso a la red desactivado. De manera local, Codex usa un sandbox cuyas restricciones aplica el sistema operativo para limitar aquello a lo que puede acceder (normalmente, al espacio de trabajo actual), además de una política de aprobación que determina cuándo debe detenerse y consultarte antes de actuar.

Para obtener una explicación general de cómo funciona el entorno aislado en la aplicación de escritorio de ChatGPT,
Codex CLI y la extensión para IDE, consulta [entorno aislado](/es-419/codex/sandboxing).
Para obtener una descripción más amplia de la seguridad empresarial, consulta el [informe técnico de seguridad de Codex](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).

## Sandbox y aprobaciones

Los controles de seguridad de Codex se basan en dos capas que funcionan en conjunto:

- **Modo sandbox**: lo que Codex puede hacer técnicamente (por ejemplo, dónde puede escribir y si puede acceder a la red) cuando ejecuta comandos generados por el modelo.
- **Política de aprobación**: cuándo Codex debe consultarte antes de ejecutar una acción (por ejemplo, salir del sandbox, usar la red o ejecutar comandos que no pertenezcan a un conjunto de confianza).

Codex usa distintos modos de sandbox según dónde lo ejecutes:

- **Codex Cloud**: se ejecuta en contenedores aislados administrados por OpenAI, lo que impide el acceso a tu sistema host o a datos no relacionados. Usa un modelo de ejecución de dos fases: la configuración se ejecuta antes de la fase del agente y puede acceder a la red para instalar las dependencias especificadas; luego, la fase del agente se ejecuta sin conexión de forma predeterminada, salvo que habilites el acceso a Internet para ese entorno. Los secretos configurados para entornos en la nube solo están disponibles durante la configuración y se eliminan antes de que comience la fase del agente.
- **Codex CLI / extensión para IDE**: los mecanismos del sistema operativo aplican las políticas de sandbox. De forma predeterminada, no hay acceso a la red y los permisos de escritura se limitan al espacio de trabajo activo. Puedes configurar el sandbox, la política de aprobación y los ajustes de red según tu tolerancia al riesgo.

En el ajuste preestablecido `Auto` (por ejemplo, `--sandbox workspace-write --ask-for-approval on-request`), Codex puede leer archivos, hacer cambios y ejecutar comandos automáticamente en el directorio de trabajo.

Codex solicita aprobación para editar archivos fuera del espacio de trabajo o ejecutar comandos que requieren acceso a la red. Si quieres chatear o planificar sin hacer cambios, cambia al modo `read-only` con el comando `/permissions`.

Codex también puede solicitar aprobación para llamadas a herramientas de apps (conectores) que declaran efectos secundarios, aunque la acción no sea un comando de shell ni un cambio en un archivo. Las llamadas destructivas a herramientas de apps o MCP siempre requieren aprobación cuando la herramienta declara una anotación destructiva (salvo que declare una anotación de lectura, que tiene prioridad).

## Monitoreo de seguridad y tareas en pausa

GPT-6 Astra incluye monitoreo de seguridad en Codex y ChatGPT Work. El monitoreo
se ejecuta de forma asíncrona y puede pausar una tarea si detecta un comportamiento potencialmente inseguro del
modelo. La pausa puede ocurrir después de la actividad que la desencadenó; el monitoreo
no reemplaza el entorno aislado, los permisos ni la revisión del resultado.

Si una tarea se pausa, lee el aviso y revisa los hallazgos cuando estén disponibles. Reanúdala
solo después de comprobar que puede continuar de forma segura. Si el aviso indica que la
tarea terminó o no ofrece una opción para reanudarla, no puedes hacerlo desde esa
interfaz.

| Interfaz y controles de datos                                                                               | Hallazgos y reanudación                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Clientes de Codex y ChatGPT Work con el flujo de hallazgos y reanudación, sin los controles de datos enumerados aquí | Revisa los hallazgos antes de reanudar la tarea.                      |
| Codex CLI y Codex para dispositivos móviles                                                                                    | Los hallazgos completos y la reanudación no están disponibles. La tarea termina. |
| Retención cero de datos, monitoreo de abusos modificado o residencia de almacenamiento de datos fuera de EE. UU.                        | Los hallazgos completos y la reanudación no están disponibles. La tarea termina. |

El monitoreo de seguridad evalúa el comportamiento del modelo durante una tarea.
La [revisión automática de aprobaciones](/es-419/codex/sandboxing/auto-review) evalúa acciones individuales que
ya requieren aprobación antes de que se ejecuten. Una acción aprobada mediante
la revisión automática de aprobaciones puede formar parte de una tarea que el monitoreo pause más adelante.

## Acceso a la red 

Para Codex Cloud, consulta [acceso a Internet del agente](/es-419/codex/cloud/internet-access) para habilitar el acceso completo a Internet o una lista de dominios permitidos.

En la aplicación de escritorio de ChatGPT, Codex CLI o la extensión para IDE, el modo de sandbox predeterminado `workspace-write` mantiene desactivado el acceso a la red, salvo que lo habilites en tu configuración:

```toml
[sandbox_workspace_write]
network_access = true

### Aislamiento de red

El acceso a la red se controla mediante reglas de destino que se aplican a scripts,
programas y subprocesos generados por comandos. Cuando el acceso a la red de los comandos
ya está habilitado, activa la función `network_proxy` para restringir ese tráfico
a la política de red que configures. Agregar reglas de dominio no activa el
proxy por sí solo.

```toml
[features.network_proxy]
enabled = true
domains = { "api.openai.com" = "allow", "example.com" = "deny" }

Para una sesión puntual de la CLI, usa la forma booleana abreviada cuando solo necesites
activar o desactivar la función, y el formato de tabla cuando también configures opciones de política:

```bash
codex \
  -c 'features.network_proxy=true' \
  -c 'sandbox_workspace_write.network_access=true'

codex \
  -c 'features.network_proxy.enabled=true' \
  -c 'features.network_proxy.domains={ "api.openai.com" = "allow", "example.com" = "deny" }' \
  -c 'sandbox_workspace_write.network_access=true'

Esta función cambia la manera en que se aplica el acceso a la red ya habilitado, pero no concede
acceso a la red por sí sola. Usa `sandbox_workspace_write.network_access` con la configuración
`workspace-write` para decidir si los comandos tienen acceso a la red:

- Red desactivada + `network_proxy` activado: la red permanece desactivada y la función no tiene efecto.
- Red activada + `network_proxy` desactivado: la red permanece activada con acceso de salida directo
  sin restricciones.
- Red activada + `network_proxy` activado: la red permanece activada y el tráfico de salida queda
  restringido por la política de red configurada.

La función de proxy también se aplica a los [perfiles de permisos](/es-419/codex/permissions#network-permissions).
En un perfil, `network.enabled = true` concede acceso a la red a los comandos, mientras que
`features.network_proxy = true` hace que se apliquen las reglas de dominio
de ese perfil:

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
extends = ":workspace"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

Si omites la función de proxy en este ejemplo, los comandos tienen acceso directo a la
red y la regla de permiso para `api.openai.com` no restringe sus destinos.

Los requisitos `experimental_network` administrados por administradores son independientes del control
con el que el usuario activa la función. Permiten configurar e iniciar la red en el sandbox sin
`features.network_proxy`, pero no activan el acceso a la red cuando el
sandbox activo lo mantiene desactivado. Consulta [Configuración administrada](/es-419/codex/enterprise/managed-configuration#configure-network-access-requirements)
para conocer el formato de `requirements.toml` para administradores.

#### Política de red

Las reglas de dominio se basan en una lista de permitidos:

- Los hosts exactos solo coinciden consigo mismos.
- `*.example.com` coincide con subdominios como `api.example.com`, pero no con
`example.com`.
- `**.example.com` coincide tanto con el dominio raíz como con los subdominios.
- Una regla de permiso global con `*` coincide con cualquier host público que no esté denegado. Considera `*`
  como acceso amplio a la red y, cuando sea posible, prefiere reglas de alcance limitado.
- `deny` siempre tiene prioridad sobre `allow`, y el valor global `*` solo es válido para reglas de permiso.

#### Destinos locales y privados

De forma predeterminada, `allow_local_binding = false` bloquea destinos de loopback, de enlace local y
privados:

- Excepciones específicas: agrega una regla que permita un literal exacto de IP local o `localhost`
  cuando un comando necesite un destino local.
- Acceso más amplio: establece `allow_local_binding = true` solo cuando quieras ampliar deliberadamente
  el acceso local o privado.
- Comodines: las reglas con comodines no se consideran excepciones locales explícitas.
- Direcciones resueltas: los nombres de host que se resuelven en IP locales o privadas permanecen bloqueados
aunque coincidan con la lista de permitidos.

#### Protecciones contra la revinculación de DNS

Antes de permitir un nombre de host, Codex realiza, en la medida de lo posible, una comprobación de DNS y de clasificación de
IP:

- Las consultas que fallan o exceden el tiempo de espera se bloquean.
- Se bloquean los nombres de host que se resuelven en direcciones no públicas.
- La comprobación reduce el riesgo de revinculación de DNS, pero no lo elimina. Para impedirla
por completo, habría que mantener fijas las IP resueltas hasta la capa de
transporte.

Si contemplas la posibilidad de DNS hostiles, aplica también controles de salida en una capa inferior.

#### Configuraciones peligrosas

Dos configuraciones amplían deliberadamente el límite de confianza:

- `dangerously_allow_non_loopback_proxy = true` puede exponer los puntos de escucha del proxy más allá de
  loopback.
- `dangerously_allow_all_unix_sockets = true` omite la lista de sockets Unix permitidos.

Úsalos solo en entornos estrictamente controlados. Cuando se habilita el proxy de sockets Unix,
los puntos de escucha se mantienen exclusivamente en loopback, incluso si se solicitó vincularlos a otras interfaces,
por lo que la red del sandbox no se convierte en un puente remoto hacia los daemons locales.

`network_proxy` está desactivado de forma predeterminada. Cuando lo habilitas:

| Ajuste                                | Valor predeterminado | Comportamiento                                                                                                                                                                              |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                              | `false` | Inicia la red del sandbox solo cuando el acceso de los comandos a la red ya está habilitado.                                                                                                           |
| `domains`                              | sin definir   | Usa una lista de permitidos, por lo que no se permite ningún destino externo hasta que agregues reglas `allow`. Admite hosts exactos, comodines de alcance limitado y reglas de permiso globales `*`; `deny` siempre tiene prioridad. |
| `unix_sockets`                         | sin definir   | No se permite ningún destino de sockets Unix hasta que agregues reglas `allow` explícitas.                                                                                                         |
| `allow_local_binding`                  | `false` | Bloquea los destinos locales y de redes privadas, a menos que agregues una regla de permiso para una dirección IP local literal exacta o para `localhost`, o que habilites explícitamente un acceso más amplio a destinos locales y privados.                |
| `enable_socks5`                        | `true`  | Ofrece compatibilidad con SOCKS5 cuando la política lo permite.                                                                                                                                         |
| `enable_socks5_udp`                    | `true`  | Permite UDP a través de SOCKS5 cuando SOCKS5 está disponible.                                                                                                                                      |
| `allow_upstream_proxy`                 | `true`  | Permite que la red del sandbox use un proxy ascendente definido en el entorno.                                                                                                               |
| `dangerously_allow_non_loopback_proxy` | `false` | Mantiene los puntos de acceso de escucha en loopback, a menos que los expongas deliberadamente más allá de localhost.                                                                                            |
| `dangerously_allow_all_unix_sockets`   | `false` | Mantiene el acceso a sockets Unix basado en una lista de permitidos, a menos que eludas deliberadamente esa protección.                                                                                              |

### Tráfico fuera del proxy de red de comandos

El proxy de red filtra scripts, programas y procesos secundarios que se ejecutan
dentro del sandbox local de comandos. No filtra la búsqueda web, las llamadas a herramientas de apps o
conectores, las conexiones a servidores MCP, la actividad del navegador o de Uso de la computadora,
las tareas de Codex Cloud ni las solicitudes del cliente relacionadas con el modelo y la autenticación. Estas
funciones usan conexiones de servicio, ajustes de funciones, políticas del espacio de trabajo
o controles del entorno independientes.

Las herramientas del navegador verifican por separado las reglas administradas de denegación de red y las listas exclusivas de permitidos
antes de acceder a un origen. Las políticas de origen del navegador pueden restringir aún más el acceso a sitios,
las cargas, las descargas y las herramientas para desarrolladores. Consulta
[controles administrados del navegador](/es-419/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Para usuarios administrados, combina la política de red de comandos con controles como
`allowed_web_search_modes`, `mcp_servers` aprobados y requisitos de funciones
para apps, complementos, navegadores o Uso de la computadora. Consulta
[Configuración administrada](/es-419/codex/enterprise/managed-configuration).

También puedes controlar la [herramienta de búsqueda web](https://platform.openai.com/docs/guides/tools-web-search) sin conceder acceso completo a la red a los comandos que se ejecutan. De forma predeterminada, Codex usa una caché de búsqueda web para acceder a los resultados. La caché es un índice de resultados web mantenido por OpenAI, por lo que el modo en caché devuelve resultados preindexados en lugar de obtener páginas en vivo. Esto reduce la exposición a la inyección de prompts desde contenido arbitrario en vivo, pero aun así debes tratar los resultados web como contenido no confiable. Si usas `--yolo` u otra [configuración de sandbox con acceso completo](#common-sandbox-and-approval-combinations), la búsqueda web usa resultados en vivo de forma predeterminada. Usa `--search` o establece `web_search = "live"` para permitir la navegación en vivo, o establece el valor en `"disabled"` para desactivar la herramienta:

```toml
web_search = "cached"  # default
# web_search = "disabled"
# web_search = "live"  # same as --search

Establece `web_search = "indexed"` cuando el acceso web externo deba controlarse mediante el
índice de búsqueda. Ten cuidado al habilitar el acceso a la red o la búsqueda web en Codex.
La inyección de prompts puede hacer que el agente obtenga y siga instrucciones no confiables.

## Valores predeterminados y recomendaciones

- Al iniciarse, Codex detecta si la carpeta tiene control de versiones y recomienda:
  - Carpetas con control de versiones: `Auto` (escritura en el espacio de trabajo + aprobaciones cuando se soliciten)
  - Carpetas sin control de versiones: `read-only`
- Según tu configuración, Codex también puede iniciarse en modo `read-only` hasta que marques explícitamente el directorio de trabajo como confiable (por ejemplo, mediante un prompt de configuración inicial o `/permissions`).
- El espacio de trabajo incluye el directorio actual y directorios temporales como `/tmp`. Usa el comando `/status` para ver qué directorios pertenecen al espacio de trabajo.
- Para aceptar los valores predeterminados, ejecuta `codex`.
- Puedes configurarlos explícitamente:
  - `codex --sandbox workspace-write --ask-for-approval on-request`
  - `codex --sandbox read-only --ask-for-approval on-request`

### Rutas protegidas en raíces con permiso de escritura

En la política predeterminada de sandbox `workspace-write`, las raíces con permiso de escritura siguen incluyendo rutas protegidas:

- `<writable_root>/.git` tiene protección de solo lectura, ya sea que aparezca como directorio o archivo.
- Si `<writable_root>/.git` es un archivo de puntero (`gitdir: ...`), la ruta resuelta del directorio de Git también queda protegida con acceso de solo lectura.
- `<writable_root>/.agents` tiene protección de solo lectura cuando existe como directorio.
- `<writable_root>/.codex` tiene protección de solo lectura cuando existe como directorio.
- La protección es recursiva, por lo que todo el contenido de esas rutas es de solo lectura.

### Ejecutar sin solicitudes de aprobación

Puedes desactivar las solicitudes de aprobación con `--ask-for-approval never` o `-a never` (forma abreviada).

Esta opción funciona con todos los modos `--sandbox`, por lo que sigues controlando el nivel de autonomía de Codex. Codex hace todo lo posible dentro de las restricciones que establezcas.

Si necesitas que Codex lea archivos, haga cambios y ejecute comandos con acceso a la red sin solicitudes de aprobación, usa `--sandbox danger-full-access` (o el flag `--dangerously-bypass-approvals-and-sandbox`). Ten cuidado antes de hacerlo.

Como opción intermedia, `approval_policy = { granular = { ... } }` te permite mantener interactivas categorías específicas de solicitudes de aprobación y rechazar automáticamente las demás. La política granular abarca aprobaciones del sandbox, solicitudes de reglas de execpolicy, solicitudes de MCP, solicitudes de `request_permissions` y aprobaciones de scripts de habilidades.

### Revisiones automáticas de aprobaciones

De forma predeterminada, las solicitudes de aprobación se dirigen a ti:

```toml
approvals_reviewer = "user"

Las revisiones automáticas de aprobaciones se aplican cuando las aprobaciones son interactivas, como con
`approval_policy = "on-request"` o una política de aprobación granular. Establece
`approvals_reviewer = "auto_review"` para enviar las solicitudes de aprobación que cumplan los requisitos
a un agente revisor antes de que Codex ejecute la acción solicitada:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"

Para conocer el ciclo de vida completo del revisor, las condiciones de activación, la prioridad de configuración
y el comportamiento ante fallos, consulta
[Revisión automática](/es-419/codex/sandboxing/auto-review).

El revisor evalúa únicamente acciones que ya requieren aprobación, como elevaciones de permisos del sandbox,
solicitudes de red bloqueadas, solicitudes de `request_permissions` o
llamadas a herramientas de apps y MCP con efectos secundarios. Las acciones que permanecen dentro del sandbox
continúan sin un paso adicional de revisión.

La política del revisor comprueba si hay exfiltración de datos, sondeo de credenciales, debilitamiento persistente
de la seguridad y acciones destructivas. Las acciones de riesgo bajo y medio
pueden continuar cuando la política lo permite. La política deniega las acciones de riesgo crítico.
Las acciones de riesgo alto requieren autorización suficiente del usuario y que no se aplique ninguna regla de denegación.
Los fallos al crear el prompt, en la sesión de revisión o en el análisis sintáctico bloquean la ejecución por seguridad. Los tiempos de espera agotados
se notifican por separado, pero la acción tampoco se ejecuta.

La [política predeterminada del revisor](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)
está en el repositorio de código abierto de Codex. Las empresas pueden reemplazar su
sección específica del tenant mediante `guardian_policy_config` en los requisitos administrados.
También se admite el texto local de `[auto_review].policy`, pero los requisitos administrados
tienen prioridad. Para obtener detalles de configuración, consulta
[Configuración administrada](/es-419/codex/enterprise/managed-configuration#configure-automatic-review-policy).

En la aplicación de escritorio de ChatGPT, estas revisiones aparecen como elementos de revisión automática con un estado
como En revisión, Aprobada, Denegada, Cancelada o Tiempo de espera agotado. También pueden
incluir un nivel de riesgo y una evaluación de la autorización del usuario para la solicitud
revisada.

La revisión automática usa llamadas adicionales al modelo, por lo que puede aumentar el uso de Codex. Los administradores
pueden restringirla con `allowed_approvals_reviewers`.

### Combinaciones comunes de sandbox y aprobaciones

| Objetivo                                                            | Flags / configuración                                                                                                                      | Efecto                                                                                                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Auto (ajuste preestablecido)                                                     | _no se necesitan flags_ o `--sandbox workspace-write --ask-for-approval on-request`                                                      | Codex puede leer archivos, hacer cambios y ejecutar comandos en el espacio de trabajo. Codex requiere aprobación para editar fuera del espacio de trabajo o acceder a la red. |
| Exploración segura de solo lectura                                           | `--sandbox read-only --ask-for-approval on-request`                                                                                 | Codex puede leer archivos y responder preguntas. Codex requiere aprobación para hacer cambios, ejecutar comandos o acceder a la red.                               |
| Solo lectura no interactiva (CI)                                    | `--sandbox read-only --ask-for-approval never`                                                                                      | Codex solo puede leer archivos; nunca solicita aprobación.                                                                                              |
| Editar automáticamente, pero solicitar aprobación para ejecutar comandos no confiables | `--sandbox workspace-write --ask-for-approval untrusted`                                                                            | Codex puede leer y editar archivos, pero solicita aprobación antes de ejecutar comandos no confiables.                                                           |
| Modo de revisión automática                                                  | `--sandbox workspace-write --ask-for-approval on-request -c approvals_reviewer=auto_review` o `approvals_reviewer = "auto_review"` | Mantiene el mismo límite del sandbox que el modo estándar de aprobación a solicitud, pero Revisión automática evalúa las solicitudes de aprobación que cumplen los requisitos en lugar de mostrarlas al usuario.  |
| Acceso completo peligroso                                             | `--dangerously-bypass-approvals-and-sandbox` (alias: `--yolo`)                                                                      |  Sin sandbox; sin aprobaciones _(no recomendado)_                                                                               |

Para ejecuciones no interactivas, usa `codex exec --sandbox workspace-write`; Codex conserva las invocaciones anteriores de `codex exec --full-auto` como una opción de compatibilidad obsoleta y muestra una advertencia.

Con `--ask-for-approval untrusted`, Codex solo ejecuta automáticamente operaciones de lectura que se sabe que son seguras. Los comandos que pueden modificar el estado o activar vías de ejecución externas (por ejemplo, operaciones destructivas de Git o flags de Git que controlan la salida o sobrescriben la configuración) requieren aprobación.

#### Configuración en `config.toml`

Para conocer el flujo de configuración más amplio, consulta [Configuración básica](/es-419/codex/config-file/config-basic), [Configuración avanzada](/es-419/codex/config-file/config-advanced#approval-policies-and-sandbox-modes) y la [Referencia de configuración](/es-419/codex/config-file/config-reference).

```toml
# Always ask for approval mode
approval_policy = "untrusted"
sandbox_mode    = "read-only"
allow_login_shell = false # optional hardening: disallow login shells for shell-based tools

# Optional: Allow network in workspace-write mode
[sandbox_workspace_write]
network_access = true

# Optional: granular approval policy
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

También puedes guardar configuraciones preestablecidas como [archivos de perfil](/es-419/codex/config-file/config-advanced#profiles) y luego seleccionarlas con `codex --profile profile-name`:

```toml
# ~/.codex/full_auto.config.toml
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

```toml
# ~/.codex/readonly_quiet.config.toml
approval_policy = "never"
sandbox_mode    = "read-only"

### Probar el sandbox localmente

Para ver qué sucede cuando un comando se ejecuta dentro del sandbox de Codex, usa estos comandos de Codex CLI:

```bash
# macOS
codex sandbox macos [--permissions-profile <name>] [--log-denials] [COMMAND]...
# Linux
codex sandbox linux [--permissions-profile <name>] [COMMAND]...
# Windows
codex sandbox windows [--permissions-profile <name>] [COMMAND]...

El comando `sandbox` también está disponible como `codex debug`, y las herramientas auxiliares de cada plataforma tienen alias (por ejemplo, `codex sandbox seatbelt` y `codex sandbox landlock`).

## Sandbox a nivel del sistema operativo

Codex aplica el sandbox de distintas maneras según tu sistema operativo:

- **macOS** usa políticas de Seatbelt y ejecuta comandos mediante `sandbox-exec` con un perfil (`-p`) que corresponde al modo `--sandbox` que seleccionaste. Cuando el acceso de lectura restringido habilita los valores predeterminados de la plataforma, Codex agrega una política de macOS cuidadosamente seleccionada (en lugar de permitir un acceso amplio a `/System`) para preservar la compatibilidad con herramientas comunes.
- **Linux** usa `bwrap` junto con `seccomp` de forma predeterminada.
- **Windows** usa la implementación del sandbox de Linux cuando Codex se ejecuta en [Windows Subsystem for Linux 2 (WSL2)](/es-419/codex/windows/wsl). WSL1 se admitía hasta Codex `0.114`; a partir de `0.115`, el sandbox de Linux pasó a usar `bwrap`, por lo que WSL1 ya no se admite. Cuando se ejecuta de forma nativa en Windows, Codex usa una implementación de [Sandbox de Windows](/es-419/codex/windows/windows-sandbox#windows-sandbox).

Si usas la extensión de Codex para IDE en Windows, esta admite WSL2 directamente. Establece lo siguiente en la configuración de VS Code para mantener al agente dentro de WSL2 siempre que esté disponible:

```json
{
  "chatgpt.runCodexInWindowsSubsystemForLinux": true
}

Esto garantiza que la extensión para IDE herede la semántica del sandbox de Linux para los comandos, las aprobaciones y el acceso al sistema de archivos, incluso cuando el sistema operativo del host sea Windows. Obtén más información en la [guía de WSL](/es-419/codex/windows/wsl).

Cuando ejecutes Codex de forma nativa en Windows, configura el modo de sandbox nativo en `config.toml`:

```toml
[windows]
sandbox = "unelevated" # or "elevated"
# sandbox_private_desktop = true  # default; set false only for compatibility

Consulta la [guía de configuración de Windows](/es-419/codex/windows/windows-sandbox#windows-sandbox) para obtener más información.

Cuando ejecutas Linux en un entorno en contenedores como Docker, es posible que el sandbox no funcione si la configuración del host o del contenedor bloquea las operaciones de espacios de nombres, de `bwrap` con setuid o de `seccomp` que Codex necesita.

En ese caso, configura tu contenedor de Docker para proporcionar el aislamiento que necesitas y luego ejecuta `codex` con `--sandbox danger-full-access` (o con el flag `--dangerously-bypass-approvals-and-sandbox`) dentro del contenedor.

### Ejecutar Codex en Dev Containers

Si tu host no puede ejecutar directamente el sandbox de Linux o si tu organización ya usa el desarrollo en contenedores como estándar, ejecuta Codex con Dev Containers y deja que Docker proporcione el límite externo de aislamiento. Esto funciona con Visual Studio Code Dev Containers y herramientas compatibles.

Usa el [ejemplo de devcontainer seguro de Codex](https://github.com/openai/codex/tree/main/.devcontainer) como implementación de referencia. El ejemplo instala Codex, herramientas de desarrollo comunes, `bubblewrap` y controles de tráfico saliente basados en un firewall.

  Los devcontainers ofrecen una protección considerable, pero no evitan todos los
  ataques. Si ejecutas Codex con `--sandbox danger-full-access` o
`--dangerously-bypass-approvals-and-sandbox` dentro del contenedor, un proyecto
  malicioso puede exfiltrar todo lo disponible en el devcontainer, incluidas las
  credenciales de Codex. Usa este patrón solo con repositorios de confianza y
  monitorea la actividad de Codex como lo harías en cualquier otro entorno con privilegios elevados.

La implementación de referencia incluye:

- una imagen base de Ubuntu 24.04 con Codex y herramientas de desarrollo comunes instaladas;
- un perfil de firewall basado en una lista de permitidos para el acceso de salida;
- configuración de VS Code y recomendaciones de extensiones para volver a abrir el espacio de trabajo en un contenedor;
- montajes persistentes para el historial de comandos y la configuración de Codex;
- `bubblewrap`, para que Codex pueda seguir usando su sandbox de Linux cuando el contenedor conceda las capacidades necesarias.

Para probarlo:

1. Instala Visual Studio Code y la [extensión Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2. Copia la configuración de ejemplo de `.devcontainer` de Codex en tu repositorio o comienza directamente desde el repositorio de Codex.
3. En VS Code, ejecuta **Dev Containers: Open Folder in Container...** y selecciona `.devcontainer/devcontainer.secure.json`.
4. Después de que se inicie el contenedor, abre una terminal y ejecuta `codex`.

También puedes iniciar el contenedor desde la CLI:

```bash
devcontainer up --workspace-folder . --config .devcontainer/devcontainer.secure.json

El ejemplo tiene tres componentes principales:

- `.devcontainer/devcontainer.secure.json` controla la configuración del contenedor, las capacidades, los montajes, las variables de entorno y las extensiones de VS Code.
- `.devcontainer/Dockerfile.secure` define la imagen basada en Ubuntu y las herramientas instaladas.
- `.devcontainer/init-firewall.sh` aplica la política de tráfico de red saliente.

El firewall de referencia está pensado como un punto de partida. Si dependes de una lista de dominios permitidos para el aislamiento, implementa protecciones contra la revinculación de DNS y medidas de actualización de DNS adecuadas para tu entorno, como actualizaciones que tengan en cuenta el TTL o un firewall con reconocimiento de DNS.

Dentro del contenedor, elige uno de estos modos:

- Mantén habilitado el sandbox de Linux de Codex si el perfil de Dev Container concede las capacidades que `bwrap` necesita para crear el sandbox interno.
- Si quieres usar el contenedor como límite de seguridad, ejecuta Codex con `--sandbox danger-full-access` dentro del contenedor para que Codex no intente crear una segunda capa de sandbox.

## Control de versiones

Codex funciona mejor con un flujo de trabajo de control de versiones:

- Trabaja en una rama de funcionalidad y asegúrate de que `git status` no muestre cambios pendientes antes de delegar. Esto facilita aislar y revertir los parches de Codex.
- Prefiere los flujos de trabajo basados en parches (por ejemplo, `git diff`/`git apply`) en lugar de editar directamente los archivos con seguimiento. Crea commits con frecuencia para poder revertir los cambios en pasos pequeños.
- Trata las sugerencias de Codex como cualquier otro PR: ejecuta verificaciones específicas, revisa las diferencias y documenta las decisiones en los mensajes de commit para fines de auditoría.

## Monitoreo y telemetría

Codex admite el monitoreo opcional mediante OpenTelemetry (OTel) para ayudar a los equipos a auditar el uso, investigar problemas y cumplir los requisitos de cumplimiento sin debilitar la configuración de seguridad local predeterminada. La telemetría está desactivada de forma predeterminada; habilítala explícitamente en tu configuración.

### Descripción general

- Codex desactiva la exportación de OTel de forma predeterminada para mantener las ejecuciones locales autocontenidas.
- Cuando se habilita, Codex emite eventos de registro estructurados que abarcan chats, solicitudes de API, actividad de flujos SSE/WebSocket, prompts del usuario (con su contenido oculto de forma predeterminada), decisiones de aprobación de herramientas y resultados de herramientas.
- Codex etiqueta los eventos exportados con `service.name` (origen), la versión de la CLI y una etiqueta de entorno para separar el tráfico de dev/staging/prod.

### Habilitar OTel (opcional)

Agrega un bloque `[otel]` a tu configuración de Codex (por lo general, `~/.codex/config.toml`), elige un exportador y define si se debe registrar el texto de los prompts.

```toml
[otel]
environment = "staging"   # dev | staging | prod
exporter = "none"          # none | otlp-http | otlp-grpc
log_user_prompt = false     # redact prompt text unless policy allows

- `exporter = "none"` mantiene activa la instrumentación, pero no envía datos a ningún destino.
- Para enviar eventos a tu propio recopilador, elige una de estas opciones:

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

Codex agrupa los eventos en lotes y los envía al cerrarse. Codex exporta únicamente la telemetría generada por su módulo OTel.

### Categorías de eventos

Algunos tipos de eventos representativos son:

- `codex.conversation_starts` (modelo, ajustes de razonamiento, política de sandbox/aprobación)
- `codex.api_request` (intento, estado/éxito, duración y detalles del error)
- `codex.sse_event` (tipo de evento de transmisión, éxito/fallo, duración y recuentos de tokens en `response.completed`)
- `codex.websocket_request` y `codex.websocket_event` (duración de la solicitud y tipo/éxito/error de cada mensaje)
- `codex.user_prompt` (longitud; el contenido se oculta a menos que se habilite explícitamente su registro)
- `codex.tool_decision` (aprobado/denegado, origen: configuración o usuario)
- `codex.tool_result` (duración, éxito, fragmento del resultado)

Las métricas de OTel asociadas (pares de contador e histograma de duración) incluyen `codex.api_request`, `codex.sse_event`, `codex.websocket.request`, `codex.websocket.event` y `codex.tool.call` (con sus correspondientes instrumentos `.duration_ms`).

Para consultar el catálogo completo de eventos y la referencia de configuración, consulta la [documentación de configuración de Codex en GitHub](https://github.com/openai/codex/blob/main/docs/config.md#otel).

### Recomendaciones de seguridad y privacidad

- Mantén `log_user_prompt = false` a menos que la política permita explícitamente almacenar el contenido de los prompts. Los prompts pueden incluir código fuente y datos confidenciales.
- Dirige la telemetría únicamente a colectores bajo tu control; aplica límites de retención y controles de acceso acordes con tus requisitos de cumplimiento.
- Trata los argumentos y los resultados de las herramientas como información confidencial. Prioriza el ocultamiento de datos en el colector o en el SIEM cuando sea posible.
- Revisa la configuración local de retención de datos (por ejemplo, `history.persistence` / `history.max_bytes`) si no quieres que Codex guarde transcripciones de las sesiones en `CODEX_HOME`. Consulta [Configuración avanzada](/es-419/codex/config-file/config-advanced#history-persistence) y [Referencia de configuración](/es-419/codex/config-file/config-reference).
- Si ejecutas la CLI con el acceso a la red desactivado, la exportación de OTel no podrá llegar a tu colector. Para exportar, permite el acceso a la red en el modo `workspace-write` para el punto de acceso de OTel o exporta desde Codex Cloud con el dominio del colector en tu lista de dominios aprobados.
- Revisa periódicamente los eventos para detectar cambios en las aprobaciones o el sandbox y ejecuciones inesperadas de herramientas.

OTel es opcional y está diseñado para complementar, no reemplazar, las protecciones de sandbox y aprobación descritas anteriormente.

## Configuración administrada

Los administradores de empresas pueden configurar los ajustes de seguridad de Codex para su espacio de trabajo en [Configuración administrada](/es-419/codex/enterprise/managed-configuration). Consulta esa página para obtener detalles sobre la configuración y las políticas.
