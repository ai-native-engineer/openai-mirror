<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/managed-configuration -->

La configuración administrada controla el comportamiento del entorno de ejecución local para las capacidades que admiten estos controles en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE. Los requisitos admitidos pueden variar según el cliente y la versión. La configuración administrada no otorga acceso al espacio de trabajo de ChatGPT, no asigna puestos ni reemplaza el control de acceso basado en roles (RBAC) del espacio de trabajo. Consulta [Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions) para gestionar el acceso a las funciones del espacio de trabajo y esta página para la política del entorno de ejecución local.

Los administradores empresariales pueden controlar el comportamiento de los clientes locales compatibles de dos maneras:

- **Requisitos**: restricciones impuestas por los administradores que los usuarios no pueden anular.
- **Valores predeterminados administrados**: valores iniciales que se aplican cuando se inicia un cliente compatible. Los usuarios pueden cambiar la configuración durante una ejecución; el cliente vuelve a aplicar los valores predeterminados administrados la próxima vez que se inicia.

## Requisitos impuestos por los administradores (requirements.toml)

Los requisitos restringen las opciones de configuración sensibles para la seguridad (la política de aprobación, el revisor de aprobaciones, la política de revisión automática, el modo sandbox, los perfiles de permisos, el modo de búsqueda web, los hooks administrados, qué servidores MCP pueden habilitar los usuarios y qué fuentes del Marketplace de complementos configuradas por los usuarios pueden agregar, usar para instalar complementos o actualizar). Al resolver la configuración (por ejemplo, a partir de `config.toml`, [archivos de perfil](/es-419/codex/config-file/config-advanced#profiles) o valores de configuración especificados mediante la CLI), si un valor entra en conflicto con una regla impuesta, el cliente local recurre a un valor compatible y notifica al usuario. Si configuras una lista de elementos permitidos en `mcp_servers`, el cliente solo habilita un servidor MCP cuando tanto su nombre como su identidad coinciden con una entrada aprobada; de lo contrario, lo deshabilita.

Los requisitos también pueden restringir las [marcas de funciones](/es-419/codex/config-file/config-basic/#feature-flags) mediante la tabla `[features]` de `requirements.toml`. Las funciones no siempre tienen implicaciones de seguridad, pero las empresas pueden fijar sus valores si lo desean. Las claves omitidas permanecen sin restricciones.

Para Codex 0.138.0 o posterior, usa preferentemente [perfiles de permisos](/es-419/codex/permissions)
con `allowed_permission_profiles` y un valor administrado de `default_permissions`. Usa
`allowed_sandbox_modes` solo en implementaciones heredadas que aún configuren
`sandbox_mode`.

Para conocer la lista exacta de claves, consulta la [sección de `requirements.toml` en la Referencia de configuración](/es-419/codex/config-file/config-reference#requirementstoml).

### Ubicaciones y precedencia

Cada cliente local compatible combina los requisitos en orden de menor a mayor precedencia:

1. Archivo `requirements.toml` del sistema (`/etc/codex/requirements.toml` en sistemas Unix,
   incluidos Linux y macOS, o `%ProgramData%\OpenAI\Codex\requirements.toml`
   en Windows).
2. Requisitos administrados por la empresa y distribuidos en el paquete de configuración en la nube.
3. Campos heredados de `managed_config.toml` que el cliente local reinterpreta como requisitos.
4. Preferencias administradas de macOS (MDM) distribuidas mediante
`com.openai.codex:requirements_toml_base64`.

Las capas de mayor precedencia reemplazan los valores escalares y de lista comunes de las
capas inferiores. Las tablas se combinan por clave, mientras que los requisitos como las reglas, los hooks y las
restricciones del sistema de archivos se combinan de una manera específica para cada campo. Consulta la
[referencia de `requirements.toml`](/es-419/codex/config-file/config-reference#requirementstoml)
para ver el esquema actual, en lugar de suponer que todos los campos se combinan de la
misma manera.

Por motivos de compatibilidad con versiones anteriores, los clientes locales compatibles reinterpretan los campos heredados
`approval_policy`, `approvals_reviewer` y `sandbox_mode` como
requisitos. Esta conversión agrega opciones de compatibilidad donde sea necesario; usa
`requirements.toml` para definir listas explícitas de elementos permitidos.

### Requisitos administrados desde la nube

Cuando un usuario inicia sesión con ChatGPT y tiene un plan compatible, los clientes locales compatibles
pueden recibir requisitos impuestos por los administradores y asociados al espacio de trabajo. Este es
un canal de distribución de políticas compatibles con `requirements.toml`. No otorga
acceso al espacio de trabajo ni reemplaza el RBAC del espacio de trabajo.

Abre [Configuración administrada](https://chatgpt.com/codex/settings/managed-configs)
para crear y asignar requisitos administrados desde la nube. Por ejemplo, esta política limita
las opciones de aprobación y de sandbox, y solicita confirmación antes de que
se ejecute un punto de entrada de shell compatible:

```toml
allowed_approval_policies = ["on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[rules]
prefix_rules = [
  { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entry points" },
]

Confirma que todas las versiones de los clientes administrados admitan las claves que selecciones y
prueba la política con un grupo pequeño antes de asignarla a toda la organización. Usa
la referencia de configuración para consultar el esquema actual y la interfaz de administración
para conocer el comportamiento actual de las asignaciones.

El servicio selecciona las capas de requisitos administrados por la empresa que se aplican a la
identidad con la que se inició sesión. El cliente local evalúa esas capas junto con las demás
fuentes de requisitos descritas en [Ubicaciones y precedencia](#locations-and-precedence).
Usa la interfaz de administración actual para crear y
asignar requisitos en el espacio de trabajo. No dependas de una copia del algoritmo de coincidencia de grupos; el servicio de administración
controla ese comportamiento y puede modificarlo independientemente del formato de los requisitos
locales.

Para conocer las claves admitidas y ver ejemplos, consulta
[Ejemplo de requirements.toml](#example-requirementstoml) y la
[referencia de `requirements.toml`](/es-419/codex/config-file/config-reference#requirementstoml).

#### Cómo aplican los clientes locales los requisitos administrados desde la nube

Cuando un usuario inicia un cliente local compatible e inicia sesión con ChatGPT con un
plan compatible, el cliente primero busca una entrada de caché válida que coincida con esa identidad.
Si no hay ninguna entrada válida disponible, el cliente obtiene el paquete aplicable
con reintentos y, si lo logra, escribe una entrada de caché firmada. Si la solicitud falla o
se agota el tiempo de espera y no hay una caché válida disponible, la carga del paquete de configuración en la nube devuelve
un error en lugar de iniciar silenciosamente sin la capa de requisitos administrados desde la
nube.

Después de resolver la caché, el cliente combina los requisitos de la nube con las
demás capas de requisitos descritas anteriormente. Una actualización en segundo plano puede renovar la
caché para un inicio posterior; no reemplaza los requisitos ya cargados
en el proceso actual.

### Verificar la experiencia de administradores y empleados

Designa a una persona responsable de cada política administrada, registra qué usuarios o grupos deben
recibirla y documenta la justificación empresarial de cualquier restricción del sistema de archivos, de red,
de aprobación o de perfiles de permisos.

Antes de ampliar la implementación, prueba un flujo de trabajo aprobado y otro
prohibido deliberadamente con un usuario representativo. Verifica la configuración efectiva
en el cliente compatible; no supongas que un rol o grupo del espacio de trabajo, por sí solo,
aplica la restricción local.

### Ejemplo de requirements.toml

Este ejemplo bloquea `--ask-for-approval never` y `--sandbox danger-full-access` (incluido `--yolo`):

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

### Desactivar las capturas de la aplicación

Para desactivar las capturas de la aplicación para los usuarios administrados, establece el requisito de nivel superior `allow_appshots`:

```toml
allow_appshots = false

Donde estén disponibles las capturas de la aplicación, `allow_appshots = false` las desactiva. Si
omites la clave, los requisitos no restringen las capturas de la aplicación y se aplican las comprobaciones normales de
disponibilidad del producto. Los clientes de App Server que leen los requisitos efectivos
mediante `configRequirements/read` reciben la misma restricción en
`allowAppshots`; si se omite `allowAppshots` o su valor es `null`, no se desactivan
las capturas de la aplicación.

### Desactivar el control remoto del dispositivo

Para desactivar el [control remoto del dispositivo](/es-419/codex/remote-connections#pick-up-work-from-another-device)
para los usuarios administrados, establece el requisito de nivel superior `allow_remote_control`:

```toml
allow_remote_control = false

Donde se admite el control remoto del dispositivo, `allow_remote_control = false`
lo desactiva. Si omites la clave, los requisitos no restringen el control remoto del
dispositivo y se aplican las comprobaciones normales de disponibilidad del producto. Este requisito no
desactiva las conexiones remotas SSH.

### Controlar los perfiles de permisos disponibles

Usa `allowed_permission_profiles` para controlar qué
[perfiles de permisos](/es-419/codex/permissions) integrados y personalizados pueden seleccionar los usuarios. Es el
equivalente de `allowed_sandbox_modes` para los perfiles de permisos; usa la lista de elementos permitidos que
corresponda a la forma en que tus usuarios seleccionan los permisos.

Las listas de perfiles de permisos permitidos requieren Codex 0.138.0 o posterior. Codex 0.137.0 y
versiones anteriores ignoran `allowed_permission_profiles` y el valor administrado de
`default_permissions`.

Usa los siguientes ejemplos de perfiles de permisos solo después de que todos los clientes administrados ejecuten una
versión compatible. No implementes perfiles personalizados administrados hasta que se complete la actualización
de todos los equipos.

Cuando está presente, la tabla contiene la lista completa de perfiles permitidos. Permite los
perfiles configurados con `true` y deniega los que se omiten o se configuran con `false`, incluidos los
perfiles integrados que se agreguen en versiones futuras de Codex.

#### Permitir los perfiles estándar

Esta política permite el acceso de solo lectura y el acceso al espacio de trabajo, pero no el acceso completo:

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

#### Agregar un valor predeterminado administrado con privilegios mínimos

Los administradores pueden definir un perfil personalizado en la misma fuente de requisitos. Usa
nombres de perfil específicos de la organización que no entren en conflicto con los nombres de la
configuración cargada de los usuarios. Los nombres personalizados no pueden comenzar con `:` ni usar
el nombre reservado `filesystem`.

No implementes perfiles personalizados administrados en clientes que ejecuten Codex 0.137.0 o
versiones anteriores. Esos clientes reconocen la tabla de perfiles, pero no el valor predeterminado administrado
que selecciona el perfil.

Por ejemplo:

```toml
default_permissions = "acme_review_only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
acme_review_only = true
# ":danger-full-access" is intentionally omitted, so it is denied.

[permissions.acme_review_only]
description = "Review code without modifying the workspace."
extends = ":read-only"

#### Permitir solo perfiles definidos por la empresa

Omite todos los perfiles integrados cuando los usuarios solo deban seleccionar perfiles definidos por los administradores:

```toml
default_permissions = "acme_workspace"

[allowed_permission_profiles]
acme_workspace = true

[permissions.acme_workspace]
description = "Workspace access with sensitive files denied."
extends = ":workspace"

[permissions.acme_workspace.filesystem]
glob_scan_max_depth = 3

[permissions.acme_workspace.filesystem.":workspace_roots"]
"**/*.env" = "deny"

El perfil personalizado puede extender `:workspace` aunque los usuarios no puedan seleccionar el
perfil integrado `:workspace` directamente.

#### Desactivar un perfil permitido por otra fuente

Las listas de permisos permitidos se combinan por nombre de perfil. Dado que los requisitos de la nube tienen
mayor precedencia que los requisitos del sistema, los requisitos de la nube pueden usar `false`
para desactivar un perfil permitido por el archivo del sistema.

Requisitos de la nube:

```toml
default_permissions = ":read-only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = false

Requisitos del sistema:

```toml
[allowed_permission_profiles]
":read-only" = true
":workspace" = true  # Not honored because cloud requirements set this to false.

Establece `default_permissions` explícitamente en un perfil permitido. Si se omite,
el entorno de ejecución local usa `:workspace` de forma predeterminada solo cuando se permiten explícitamente tanto `:workspace` como
`:read-only`. Cuando `allowed_permission_profiles`
no está presente, los requisitos administrados no restringen los nombres de perfil que pueden
seleccionar los usuarios. Cada entrada debe especificar un perfil integrado o uno personalizado definido en
una configuración cargada o una fuente de requisitos. Define los perfiles personalizados en los requisitos
administrados para controlar su comportamiento de forma centralizada.

### Sobrescribir los requisitos del sandbox según el host

Usa `[[remote_sandbox_config]]` cuando una misma política administrada deba aplicar distintos
requisitos de sandbox en diferentes hosts. Por ejemplo, puedes mantener una configuración predeterminada más estricta
para las computadoras portátiles y permitir la escritura en el espacio de trabajo en equipos de desarrollo o ejecutores de CI
que coincidan con los patrones. Actualmente, las entradas específicas de cada host solo sobrescriben `allowed_sandbox_modes`:

```toml
allowed_sandbox_modes = ["read-only"]

[[remote_sandbox_config]]
hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

El entorno de ejecución local compara cada entrada de `hostname_patterns` con el
nombre de host que logra resolver. Da preferencia al nombre de dominio completo cuando está
disponible y, de lo contrario, usa el nombre de host local. La comparación no distingue entre mayúsculas y minúsculas;
`*` coincide con cualquier secuencia de caracteres y `?`, con un carácter.

La primera entrada de `[[remote_sandbox_config]]` que coincida tiene prioridad dentro de la misma
fuente de requisitos. Si ninguna entrada coincide, el entorno de ejecución local conserva el valor de nivel superior de
`allowed_sandbox_modes`. La coincidencia del nombre de host solo sirve para seleccionar la política; no la
consideres una prueba autenticada de la identidad del dispositivo.

También puedes restringir el modo de búsqueda web:

```toml
allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed

`allowed_web_search_modes = []` solo permite `"disabled"`.
Por ejemplo, `allowed_web_search_modes = ["cached"]` impide la búsqueda web en tiempo real incluso en sesiones de `danger-full-access`.

### Configurar los requisitos de acceso a la red

  `[experimental_network]` es experimental y puede cambiar. No habilites estos
  requisitos de forma generalizada en un despliegue empresarial sin validarlos
  en las versiones de los clientes locales y los sistemas operativos que usan tus usuarios. La compatibilidad con Windows
  sigue siendo limitada; evita aplicar esta política a los usuarios de Windows a menos
  que la hayas probado en tu entorno.

Usa `[experimental_network]` en `requirements.toml` cuando los administradores deban
definir de manera centralizada los requisitos de acceso a la red. Estos requisitos son independientes
del interruptor `features.network_proxy` del usuario: permiten configurar el acceso a la red del sandbox
sin esa marca de función, pero no otorgan a los comandos acceso a la red
cuando el sandbox activo mantiene desactivado dicho acceso. Establece
`experimental_network.enabled = true` para activar el proxy administrado; las reglas de
dominios por sí solas no activan el proxy.

```toml
[experimental_network]
enabled = true
managed_allowed_domains_only = true

[experimental_network.domains]
"api.openai.com" = "allow"
"**.example.com" = "allow"
"blocked.example.com" = "deny"
"**.exfil.example.com" = "deny"

Usa `experimental_network.managed_allowed_domains_only = true` solo cuando
también definas entradas `"allow"` bajo control de los administradores en
`[experimental_network.domains]` y quieras que esas reglas sean exclusivas. Si el valor es
`true` y no hay reglas de autorización administradas, las reglas de autorización de dominios agregadas por los usuarios dejan de
tener efecto. No combines el mapa canónico `domains` con las listas heredadas
`allowed_domains` o `denied_domains`.

`*.example.com` solo coincide con subdominios. `**.example.com` coincide con el dominio
raíz y sus subdominios. Una regla de denegación coincidente prevalece sobre una regla de autorización.

La sintaxis de los dominios, las reglas para destinos locales o privados, la prioridad de la denegación sobre el permiso
y las limitaciones de la revinculación de DNS son iguales a las del comportamiento de red del sandbox
descrito en [Aprobaciones del agente y seguridad](/es-419/codex/agent-approvals-security#network-isolation).

El proxy enruta los comandos locales que se ejecutan dentro del sandbox. Las herramientas del navegador
también comprueban las denegaciones de red administradas y las listas exclusivas de dominios permitidos antes de acceder
a un origen; esta comprobación de políticas es independiente y no enruta el tráfico del navegador a través
del proxy de comandos. El proxy no filtra la búsqueda web, las apps y los conectores, los servidores
MCP, el tráfico de las aplicaciones nativas, las solicitudes al servicio de Codex ni el tráfico de Codex Cloud.
Usa los controles específicos de cada ámbito:

- Usa `allowed_web_search_modes` para restringir la búsqueda web.
- Usa `features.apps = false` para desactivar las integraciones de apps y conectores, y
`features.plugins = false` para desactivar los complementos donde sean compatibles.
- Usa la lista administrada de servidores aprobados en `mcp_servers` para restringir los servidores MCP.
- Usa requisitos de funciones como `browser_use`, `in_app_browser` y
`computer_use` para restringir las capacidades del navegador y del uso de la computadora.
- Configura el acceso a la red de Codex Cloud en la configuración de su entorno en la nube.

Una lista de dominios permitidos para comandos no sustituye estos controles específicos de
cada capacidad.

### Controlar el navegador y el Uso de la computadora

Usa las tablas `[browser_use]` y `[computer_use]` de `requirements.toml` para
restringir los clientes de escritorio compatibles. Valida la política en las versiones de los clientes
y los sistemas operativos de tu despliegue. Configurar una regla de autorización no
instala un complemento, no otorga un permiso del sistema operativo ni aprueba una acción
que aún requiere revisión.

Para el acceso del navegador, configura una política de orígenes. Un origen incluye el esquema,
el host y, de manera opcional, el puerto, como `https://example.com` o
`https://*.example.com:8443`. No incluyas una ruta, una consulta ni un fragmento. A diferencia de
las reglas de dominios para el acceso de comandos a la red, las reglas de orígenes del navegador distinguen HTTP de HTTPS
y verifican que el puerto coincida.

Este ejemplo restringe el acceso del navegador a un sitio aprobado e impide la carga de archivos
y el acceso completo a Chrome DevTools Protocol (CDP) en ese sitio:

```toml
[browser_use]
allow_history_access = false
allow_global_persistent_approval = false

[browser_use.default_origin_policy]
access = "deny"

[browser_use.origins."https://example.com"]
access = "allow"
uploads = "deny"
downloads = "allow"
full_cdp_access = "deny"
persistent_approval = false
access_approval_lifetime = "turn"

Las reglas de orígenes coincidentes se resuelven por campo. Una denegación coincidente prevalece; de lo contrario,
la política predeterminada de orígenes proporciona los campos que las reglas coincidentes no especifican.
La configuración local puede agregar restricciones, pero no puede flexibilizar una denegación administrada.
Las denegaciones de red y las listas administradas exclusivas de dominios permitidos siguen aplicándose.

Establece `browser_use.disable_auto_review = true` para desactivar la revisión automática de aprobaciones
para las acciones del navegador, o establece `auto_review = "deny"` en una política de orígenes
para restringirla en ese origen. Esto controla la gestión de aprobaciones; no
desactiva el monitoreo de seguridad del modelo.

Para las aplicaciones nativas, establece una política de acceso predeterminada e identifica las aplicaciones permitidas. Por
ejemplo, esta política de macOS permite Calculator e impide guardar aprobaciones:

```toml
[computer_use]
default_app_access = "deny"
allow_persistent_approval = false

[computer_use.macos.bundle_ids]
"com.apple.calculator" = "allow"

Las políticas de Windows pueden identificar aplicaciones empaquetadas mediante
`computer_use.windows.aumids` o ejecutables mediante
`computer_use.windows.exes`. Las reglas de ejecutables requieren `publisher_name`,
`product_name` y `access`; `binary_name` es opcional. Usa la identidad verificada
de la aplicación en lugar de basarte solo en su nombre visible.

Consulta la [referencia de configuración](/es-419/codex/config-file/config-reference#requirementstoml)
para conocer todos los campos y las [restricciones de uso con el equipo bloqueado](#restrict-locked-computer-use)
para dispositivos macOS administrados.

### Fijar marcas de funciones

También puedes fijar las [marcas de funciones](/es-419/codex/config-file/config-basic/#feature-flags) para los usuarios
que reciban un archivo `requirements.toml` administrado:

```toml
[features]
personality = true
unified_exec = false

# Disable surface-specific features when needed.
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
in_app_updates = false
computer_use = false

Usa las claves canónicas de funciones de `config.toml` que aparecen en la tabla `[features]` para las
funciones del entorno de ejecución. El entorno de ejecución local normaliza las funciones reconocidas para respetar estos
valores fijos y rechaza las escrituras incompatibles en `config.toml` o en la configuración de funciones de los archivos de
perfil.

<a id="disable-codex-feature-surfaces"></a>

- `in_app_browser = false` desactiva el panel del navegador integrado.
- `in_app_updates = false` desactiva el actualizador propio de la aplicación de escritorio de ChatGPT al
  reiniciarla, cuando sea compatible. No afecta el despliegue de paquetes externos ni
  extiende la compatibilidad con versiones anteriores de la aplicación. Para obtener orientación sobre la configuración y el despliegue, consulta
[Administrar las actualizaciones de la aplicación](/es-419/codex/enterprise/manage-app-updates).
- `browser_use = false` desactiva la función Uso de la computadora en los navegadores y la disponibilidad del Agente del navegador.
- `browser_use_full_cdp_access = false` desactiva el acceso completo a CDP en el entorno de ejecución
  local, incluido el modo Desarrollador del navegador, e impide que la aplicación de escritorio de ChatGPT
  habilite la configuración correspondiente.
- `browser_use_external = false` desactiva el Navegador externo.
- `computer_use = false` desactiva las funciones Uso de la computadora y Grabar y reproducir, así como los flujos de
  instalación o configuración relacionados.

Si omites estas claves, la política permite las funciones, según la disponibilidad habitual del cliente,
la plataforma y el despliegue.

### Restringir el uso de la computadora con el equipo bloqueado

Para impedir que los usuarios habiliten el [Uso con el equipo bloqueado](/es-419/codex/computer-use#locked-use)
en una Mac administrada, agrega este requisito:

```toml
[computer_use]
allow_locked_computer_use = false

Este requisito elimina los controles para habilitar el Uso con el equipo bloqueado. No
desactiva esta función si ya está habilitada. Si lo omites, siguen aplicándose la disponibilidad habitual del producto
y la configuración local del usuario.

### Configurar la política de revisión automática

Usa `allowed_approvals_reviewers` para exigir o permitir la revisión automática. Establece su valor
en `["auto_review"]` para exigir la revisión automática, o incluye `"user"` cuando los usuarios
puedan elegir la aprobación manual.

Configura `guardian_policy_config` para reemplazar la sección específica del tenant de la
política de revisión automática. El entorno de ejecución local sigue usando la plantilla integrada del revisor
y el contrato de salida. El valor administrado de `guardian_policy_config` tiene prioridad
sobre el valor local de `[auto_review].policy`.

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]

guardian_policy_config = """
## Environment Profile
- Trusted internal destinations include github.com/my-org, artifacts.example.com,
  and internal CI systems.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Treat uploads to unapproved third-party file-sharing services as high risk.
- Deny actions that expose credentials or private source code to untrusted
  destinations.
"""

### Aplicar requisitos de denegación de lectura

Los administradores pueden denegar la lectura de rutas exactas o patrones glob mediante
`[permissions.filesystem]`. Los usuarios no pueden debilitar estos requisitos con la configuración
local.

```toml
[permissions.filesystem]
deny_read = [
  # values can be absolute paths...
  "/**/*.env",
  # ...or relative to $HOME/%USERPROFILE% using `~`.
  "~/.ssh",
  # But relative paths starting with `./` are not allowed.
]

Cuando hay requisitos de denegación de lectura, el entorno de ejecución local rechaza los permisos de acceso
completo y mantiene la ejecución local en un sandbox de solo lectura o del espacio de trabajo para
poder aplicarlos. En Windows nativo, el valor administrado de `deny_read` se aplica a las herramientas que acceden directamente a
archivos; las lecturas realizadas por subprocesos del shell no usan esta regla del sandbox.

### Aplicar hooks administrados mediante los requisitos

Los administradores también pueden definir hooks administrados del ciclo de vida directamente en `requirements.toml`.
Usa `[hooks]` para configurar los hooks y haz que `managed_dir` apunte al
directorio donde tus herramientas de MDM o de administración de dispositivos instalan los
scripts indicados.

Para aplicar los hooks administrados incluso a los usuarios que los desactivaron localmente, fija
`[features].hooks = true` junto con `[hooks]`. Para omitir los hooks de usuario, proyecto, sesión
y complementos, pero seguir permitiendo los hooks administrados, establece
`allow_managed_hooks_only = true`.

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

Notas:

- El entorno de ejecución local aplica la configuración de hooks de `requirements.toml`,
  pero no distribuye los scripts de `managed_dir`.
- Distribuye esos scripts con tu solución de MDM o de administración de dispositivos.
- Los comandos de hooks administrados deben hacer referencia a rutas absolutas de scripts dentro del
directorio administrado configurado.
- `allow_managed_hooks_only = true` omite los hooks provenientes de fuentes de usuario, proyecto, sesión y
  complementos, pero sigue cargando los hooks de `requirements.toml` y otras
  capas de configuración administrada.

### Aplicar reglas de comandos mediante los requisitos

Los administradores también pueden aplicar reglas restrictivas para comandos desde `requirements.toml`
mediante una tabla `[rules]`. Estas reglas se combinan con los archivos `.rules` habituales y la
decisión más restrictiva sigue prevaleciendo.

A diferencia de `.rules`, las reglas de requisitos deben especificar `decision`, y esa decisión
debe ser `"prompt"` o `"forbidden"` (no `"allow"`).

```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
]

Para restringir qué servidores MCP puede habilitar un cliente local, agrega en `mcp_servers` una lista
de servidores aprobados. Para los servidores stdio, busca coincidencias por `command`; para los servidores HTTP
con streaming, por `url`:

```toml
[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }

Cuando `identity.command` es una cadena, solo se compara con el valor configurado de `command`.
No se inspeccionan `args`, `cwd`, `env` ni `env_vars`.

Para restringir una invocación stdio completa, busca coincidencias con el ejecutable y cada
argumento posicional:

```toml
[mcp_servers.internal.identity]
command = { executable = "/usr/local/bin/codex-mcp", args = [
  { match = "exact", value = "serve" },
  { match = "prefix", value = "--workspace=" },
] }

El ejecutable, la cantidad de argumentos y el orden de los argumentos deben coincidir. Las reglas de argumentos y URL
admiten coincidencias `exact` y `prefix`, además de coincidencias `regex` con el valor completo. Las reglas estructuradas
de comandos tampoco inspeccionan `cwd`, `env` ni `env_vars`. Los servidores MCP incluidos en complementos
usan las mismas estructuras de identidad en
`plugins.<plugin>.mcp_servers.<server>`.

Si `mcp_servers` está presente pero vacío, el cliente local desactiva todos los servidores MCP.

### Controlar la disponibilidad de los complementos

Para desactivar los complementos en los clientes locales compatibles, establece `features.plugins` en
`false` dentro de `requirements.toml`:

```toml
features.plugins = false

Esta configuración también se aplica cuando los usuarios inician sesión en Codex con una clave de API. Consulta la
[referencia de
`features.plugins`](/es-419/codex/config-file/config-reference#requirementstoml) para conocer la
configuración compatible.

### Restringir las fuentes del Marketplace de complementos

Para restringir las operaciones en las fuentes del Marketplace configuradas por los usuarios, establece
`restrict_to_allowed_sources = true` y define una o más reglas de fuentes:

```toml
[marketplaces]
restrict_to_allowed_sources = true

[marketplaces.allowed_sources.company_plugins]
source = "git"
url = "https://github.com/example/company-plugins.git"
ref = "main"

[marketplaces.allowed_sources.internal_git]
source = "host_pattern"
host_pattern = '^git\.example\.com$'

[marketplaces.allowed_sources.local_plugins]
source = "local"
path = "/opt/company/codex-plugins"

Las reglas de Git buscan coincidencias con la URL normalizada del repositorio y, cuando está presente, con un valor exacto de
`ref`. Los patrones de host son expresiones regulares que se comparan con el host de Git en minúsculas;
usa `^` y `$` para buscar una coincidencia con el host completo. Las reglas locales requieren una ruta absoluta
y normalizada. Consulta la [referencia de `requirements.toml`](/es-419/codex/config-file/config-reference#requirementstoml)
para ver el esquema completo y el comportamiento de combinación.

Para las fuentes configuradas por los usuarios, estos requisitos rechazan las operaciones de agregar un Marketplace, instalar complementos y
actualizar un Marketplace de Git configurado cuando no coinciden con las reglas.
Los Marketplace de OpenAI administrados por Codex siguen disponibles cuando coinciden su fuente y
su nombre reservado. Los requisitos no filtran los Marketplace de usuarios que ya estén configurados
ni sus complementos durante la ejecución.

Estas restricciones de fuentes se aplican solo donde el cliente local admite operaciones con marketplaces de complementos: ChatGPT y Codex en la app de escritorio, y Codex CLI.
No controlan el uso de complementos en ChatGPT en la web ni en dispositivos móviles, y no
agregan complementos a la extensión para IDE.

## Valores predeterminados administrados (`managed_config.toml`)

Los valores predeterminados administrados establecen la configuración con la que se inicia un cliente local compatible. Al
iniciarse, reemplazan la configuración del archivo `config.toml` local del usuario y cualquier valor
definido con `--config` en la CLI. Los usuarios pueden cambiar esos ajustes durante la ejecución actual, y los
valores predeterminados se vuelven a aplicar la próxima vez que se inicia el cliente.

Si un valor predeterminado administrado, un perfil de MDM de macOS o una configuración guardada fija `gpt-5.4`
o `gpt-5.4-mini` para usuarios que iniciaron sesión con ChatGPT, actualízalo antes del 31 de agosto de 2026. Reemplaza `gpt-5.4` por `gpt-5.6-terra` y `gpt-5.4-mini` por
`gpt-5.6-luna`. Esto no afecta a la API de OpenAI ni a Codex cuando se autentica con tu propia clave de API.
Consulta la [disponibilidad de modelos en el espacio de
trabajo](/es-419/codex/enterprise/workspace-model-availability#prepare-for-the-gpt-54-retirement).

Asegúrate de que los valores predeterminados administrados cumplan tus requisitos; el entorno de ejecución local
rechaza los valores no permitidos.

### Precedencia y capas

El entorno de ejecución local compone la configuración efectiva en este orden (las capas superiores
prevalecen sobre las inferiores):

- Preferencias administradas (MDM de macOS; máxima precedencia)
- `managed_config.toml` (archivo del sistema o administrado)
- `config.toml` (configuración base del usuario)

Los valores definidos con `--config key=value` en la CLI se aplican a la configuración base, pero las capas administradas los reemplazan. Esto significa que cada ejecución comienza con los valores predeterminados administrados, aunque proporciones opciones locales.

Los requisitos administrados en la nube afectan la capa de requisitos (no los valores predeterminados administrados). Para conocer su precedencia, consulta la sección anterior sobre requisitos impuestos por administradores.

### Ubicaciones

- Linux/macOS (Unix): `/etc/codex/managed_config.toml`
- Windows/sistemas que no son Unix: `~/.codex/managed_config.toml`

Si el archivo no existe, el entorno de ejecución local omite la capa administrada.

### Preferencias administradas de macOS (MDM)

En macOS, los administradores pueden distribuir un perfil de dispositivo que proporciona cargas útiles TOML codificadas en base64 en:

- Dominio de preferencias: `com.openai.codex`
- Claves:
  - `config_toml_base64` (valores predeterminados administrados)
  - `requirements_toml_base64` (requisitos)

El entorno de ejecución local interpreta estas cargas útiles de “preferencias administradas” como TOML. Para
los valores predeterminados administrados (`config_toml_base64`), las preferencias administradas tienen la máxima
precedencia. Para los requisitos (`requirements_toml_base64`), la precedencia sigue
el orden de los requisitos administrados en la nube descrito anteriormente. La misma
tabla `[features]` de requisitos funciona en `requirements_toml_base64`; usa
también allí las claves canónicas de funciones.

### Flujo de trabajo de configuración de MDM

El entorno de ejecución local respeta las cargas útiles estándar de MDM de macOS, por lo que puedes distribuir
la configuración con herramientas como `Jamf Pro`, `Fleet` o `Kandji`. Una implementación
sencilla se realiza de la siguiente manera:

1. Crea la carga útil TOML administrada y codifícala con `base64` (sin saltos de línea).
2. Agrega la cadena a tu perfil de MDM dentro del dominio `com.openai.codex`, en `config_toml_base64` (valores predeterminados administrados) o en `requirements_toml_base64` (requisitos).
3. Distribuye el perfil y luego pide a los usuarios que reinicien el cliente local compatible y
confirmen que el resumen de la configuración de inicio refleje los valores administrados.
4. Cuando revoques o cambies la política, actualiza la carga útil administrada; el cliente
leerá la preferencia actualizada la próxima vez que se inicie.

Evita incluir secretos o valores dinámicos que cambien con frecuencia en la carga útil. Trata el TOML administrado como cualquier otra configuración de MDM sujeta al control de cambios.

### Ejemplo de managed\_config.toml

```toml
# Set conservative defaults
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false             # keep network disabled unless explicitly allowed

[otel]
environment = "prod"
exporter = "otlp-http"            # point at your collector
log_user_prompt = false            # keep prompts redacted
# exporter details live under exporter tables; see Monitoring and telemetry above

### Medidas de protección recomendadas

- Usa preferentemente `workspace-write` con aprobaciones para la mayoría de los usuarios; reserva el acceso completo para contenedores controlados.
- Mantén `network_access = false` a menos que tu revisión de seguridad permita un recopilador o los dominios necesarios para tus flujos de trabajo.
- Usa la configuración administrada para fijar los ajustes de OTel (exportador, entorno), pero mantén `log_user_prompt = false` a menos que tu política permita explícitamente almacenar el contenido de los prompts.
- Audita periódicamente las diferencias entre el archivo `config.toml` local y la política administrada para detectar desviaciones; las capas administradas deben prevalecer sobre las opciones y los archivos locales.
