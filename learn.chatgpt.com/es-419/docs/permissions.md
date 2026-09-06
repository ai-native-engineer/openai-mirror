<!-- source: https://learn.chatgpt.com/es-419/docs/permissions -->

Versión beta. Los perfiles de permisos están en desarrollo activo y pueden cambiar.

  Los perfiles de permisos no se combinan con la configuración anterior del sandbox. Configura
  `default_permissions` y `[permissions]`, o bien `sandbox_mode` /
`sandbox_workspace_write`, pero no ambas opciones. Si `sandbox_mode` aparece en algún
  archivo de configuración cargado, pasas `--sandbox` o el perfil de configuración seleccionado establece
`sandbox_mode`, Codex usa esa configuración anterior del sandbox en lugar de
`default_permissions`.

La opción administrada `allowed_permission_profiles` es la excepción: hace que Codex use
perfiles de permisos. Quita opciones de configuración anteriores como
`sandbox_mode` y `[sandbox_workspace_write]` antes de implementar una lista administrada
de perfiles permitidos. Para una implementación empresarial con versiones mixtas, puedes mantener el
requisito administrado `allowed_sandbox_modes` como una restricción temporal de
compatibilidad hasta que todos los clientes ejecuten Codex 0.138.0 o una versión posterior.

Los perfiles de permisos te permiten aplicar límites basados en el principio de privilegio mínimo a los comandos locales
que Codex ejecuta en tu nombre. Un perfil es una política con nombre que combina reglas del sistema de archivos,
que definen qué pueden leer o escribir los comandos, con reglas de red,
que definen a qué destinos pueden acceder los comandos.

  La opción `network.enabled = true` de un perfil permite que los comandos accedan a la red, pero
  no inicia el proxy de red. Para aplicar las reglas de dominio del perfil, también establece
`features.network_proxy = true` en `config.toml` o usa requisitos de
  `[experimental_network]` habilitados y gestionados por un administrador. Sin un
  proxy activo, las reglas de dominio del perfil no restringen el acceso directo a la red.

Usa perfiles para dar a Codex acceso suficiente para el chat actual sin otorgarle
un acceso amplio a tu computadora o red. Por ejemplo, un perfil de solo lectura puede
permitir que Codex inspeccione un proyecto sin editarlo, mientras que un perfil con permisos de escritura
puede limitar las ediciones a las raíces seleccionadas del espacio de trabajo.

Los perfiles de permisos locales son compatibles con macOS, Linux, WSL y
Windows nativo. Consulta [Alcance y aplicación](#scope-and-enforcement) para obtener
detalles y salvedades específicos de cada plataforma.

Para la configuración de red de Codex Cloud, consulta [Acceso a Internet](/es-419/codex/cloud/internet-access).

## Definir y seleccionar un perfil

Codex incluye tres perfiles de permisos integrados:

- `:read-only` mantiene la ejecución de comandos locales en modo de solo lectura.
- `:workspace` permite escribir dentro de las raíces activas del espacio de trabajo y los directorios temporales del sistema.
- `:danger-full-access` elimina las restricciones locales del sandbox y debe usarse
  solo cuando ese acceso amplio sea intencional.

Crea un perfil con nombre en `[permissions.<name>]` y luego asigna a la clave de nivel superior
`default_permissions` el nombre de ese perfil o uno de los perfiles integrados anteriores.
En este ejemplo, `project-edit` es un nombre de perfil definido por el usuario, no un valor
integrado.

Los administradores empresariales pueden definir perfiles y restringir cuáles
pueden seleccionar los usuarios mediante el archivo `requirements.toml` administrado. Una vez que
`allowed_permission_profiles` está presente, se deniegan los perfiles omitidos,
incluidos los perfiles integrados omitidos y los que se agreguen en versiones futuras de Codex. Consulta
[Controlar los perfiles de permisos disponibles](/es-419/codex/enterprise/managed-configuration#control-available-permission-profiles)
para conocer la configuración administrada recomendada.

Los perfiles personalizados usan dos conceptos relacionados:

- `[permissions.<name>.workspace_roots]` agrega directorios concretos que deben
  considerarse raíces del espacio de trabajo para ese perfil.
- `[permissions.<name>.filesystem.":workspace_roots"]` define las reglas del sistema de archivos
  que Codex aplica dentro de cada raíz efectiva del espacio de trabajo: las raíces del espacio de trabajo
  en tiempo de ejecución de la sesión actual, junto con las raíces definidas anteriormente en el perfil.

Los perfiles también usan el modelo estándar de capas de configuración. Las capas con mayor precedencia pueden
agregar o reemplazar entradas con el mismo nombre de perfil sin tener que volver a declarar todo
el perfil.

Por ejemplo, una configuración a nivel de la organización y otra a nivel del usuario pueden extender
el mismo perfil de forma independiente:

```toml
# /etc/codex/config.toml
[permissions.server.workspace_roots]
"~/code/server" = true

```toml
# ~/.codex/config.toml
[permissions.server.workspace_roots]
"~/code/mobile-app" = true

Cuando `server` está activo, ambas raíces del espacio de trabajo forman parte del
perfil efectivo.

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"
"objects.githubusercontent.com" = "allow"
"*.github.com" = "allow"
"tracking.example.com" = "deny"

Este perfil:

- Lee las rutas mínimas en tiempo de ejecución que necesitan las herramientas de desarrollo comunes.
- Aplica las mismas reglas a las raíces del espacio de trabajo de la sesión actual y a las
raíces definidas en el perfil.
- Mantiene en modo de solo lectura la configuración relacionada con el IDE, como `.devcontainer/`, bajo cada
  raíz.
- Deniega el acceso a los archivos de entorno que coinciden con una regla glob.
- Permite el acceso a la red solo mediante la política de dominios configurada.

En un perfil activo, las reglas de denegación más específicas siguen vigentes aunque una ruta más general
sea legible o modificable. Por ejemplo, un perfil puede permitir escribir en las raíces del espacio de trabajo
y, aun así, configurar una ruta que coincida con `.env` como `deny`.

## Extender un perfil

Usa `extends` cuando un perfil sea prácticamente igual a uno integrado o a otro perfil con nombre.
Es preferible extender un perfil integrado en lugar de empezar desde cero para que se conserven
las protecciones básicas. Por ejemplo, extender `:workspace` mantiene
el directorio `.codex` de la raíz del espacio de trabajo en modo de solo lectura, a menos que
sobrescribas explícitamente esa regla. Define el perfil base una sola vez y luego agrega o sobrescribe solo las reglas que
sean diferentes.

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
description = "Project editing with OpenAI API access."
extends = ":workspace"

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

Este perfil parte de `:workspace`, mantiene denegado el acceso a los archivos que coinciden con `.env` y
permite solicitudes a `api.openai.com`. Un perfil puede extender `:read-only`,
`:workspace` u otro perfil con nombre. No puede extender
`:danger-full-access`; Codex también rechaza los perfiles base desconocidos y los ciclos de
herencia.

## Especificación de configuración

| Entrada                                                             | Tipo / valores              | Valor predeterminado                 | Detalles                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default_permissions`                                             | Cadena con el nombre del perfil        | Ninguno                    | Especifica el perfil de permisos que Codex aplica de forma predeterminada. Debe coincidir con un perfil definido en `[permissions]` o con uno integrado como `:workspace`. Configúralo explícitamente para obtener un comportamiento predecible; los requisitos administrados solo pueden omitirlo cuando tanto `:workspace` como `:read-only` estén permitidos explícitamente. Codex usa la configuración anterior del sandbox, a menos que la opción administrada `allowed_permission_profiles` le indique usar perfiles de permisos en este caso. |
| `[permissions.<name>]`                                            | Tabla                      | Ninguno                    | Define un perfil con nombre. `default_permissions` selecciona un perfil como predeterminado; las demás opciones de configuración de los perfiles de permisos también usan el nombre del perfil.                                                                                                                                                                                                                                                                               |
| `permissions.<name>.description`                                  | Cadena                     | Ninguno                    | Proporciona una descripción del perfil fácil de leer. Un perfil no hereda la descripción de su perfil base mediante `extends`.                                                                                                                                                                                                                                                                                                 |
| `permissions.<name>.extends`                                      | Cadena con el nombre del perfil        | Ninguno                    | Crea este perfil a partir de otro perfil con nombre o de uno de los perfiles integrados `:read-only` o `:workspace`. Codex rechaza `:danger-full-access`, los perfiles base desconocidos y los ciclos de herencia.                                                                                                                                                                                                                                            |
| `[permissions.<name>.workspace_roots]`                            | Tabla                      | Ninguno                    | Agrega raíces del espacio de trabajo definidas en el perfil a las que se aplican las reglas `:workspace_roots` del sistema de archivos, igual que a las raíces del espacio de trabajo en tiempo de ejecución de la sesión actual.                                                                                                                                                                                                                                                                                |
| `permissions.<name>.workspace_roots."<path>"`                     | Booleano                    | `false`                 | Agrega la ruta al conjunto de raíces del espacio de trabajo del perfil cuando su valor es `true`. Las entradas cuyo valor es `false` permanecen inactivas.                                                                                                                                                                                                                                                                                                                        |
| `[permissions.<name>.filesystem]`                                 | Tabla                      | Ninguno                    | Asocia rutas del sistema de archivos con valores de acceso o mapas de subrutas con ámbito definido. Si las tablas del sistema de archivos faltan o están vacías, el acceso al sistema de archivos permanece restringido y se emite una advertencia durante el inicio.                                                                                                                                                                                                                                                               |
| `permissions.<name>.filesystem.glob_scan_max_depth`               | Número                     | Ninguno                    | Limita la expansión de los patrones glob que deniegan la lectura en Linux, WSL y Windows nativo cuando Codex crea una instantánea de las coincidencias antes de iniciar el sandbox. Los valores más altos pueden aumentar el trabajo de análisis durante el inicio. Usa un valor de al menos `1` cuando un patrón `**` sin límites requiera una expansión previa acotada.                                                                                                                                                              |
| `[permissions.<name>.filesystem]."<path>"`                        | `read`, `write` o `deny` | Ninguno                    | Otorga acceso directo a una ruta admitida. `deny` deniega el acceso y prevalece sobre las entradas `write` o `read` con el mismo nivel de especificidad. Codex rechaza las reglas de escritura directa que el entorno de ejecución activo no puede aplicar.                                                                                                                                                                                                                            |
| `[permissions.<name>.filesystem."<path>"]."<subpath>"`            | `read`, `write` o `deny` | Ninguno                    | Otorga acceso a un elemento descendiente de `<path>`. Usa `.` para la ruta base. Las demás subrutas deben ser rutas descendientes relativas y no pueden contener los componentes `.` ni `..`.                                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network]`                                    | Tabla                      | Ninguno                    | Configura el acceso a la red de los comandos y la política que aplica un proxy de red activo. Habilita `features.network_proxy`, a menos que los requisitos de red gestionados por un administrador inicien el proxy.                                                                                                                                                                                                                                    |
| `permissions.<name>.network.enabled`                              | Booleano                    | `false`                 | Habilita el acceso a la red para los comandos del perfil. No inicia el proxy de red; sin un proxy activo, los comandos pueden conectarse directamente sin restricciones de dominio.                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network.domains]`                            | Tabla                      | Ninguno                    | Asocia patrones de host con `allow` o `deny`. Las reglas solo se aplican cuando el proxy de red está activo. Si no hay entradas de `allow`, el proxy activo bloquea las solicitudes a dominios, y las entradas de denegación prevalecen sobre las de permiso.                                                                                                                                                                                                                 |
| `permissions.<name>.network.domains."<pattern>"`                  | `allow` o `deny`          | Ninguno                    | Admite hosts exactos, `*.example.com` para subdominios, `**.example.com` para el dominio raíz y sus subdominios, y `*` como comodín global que solo puede usarse para permitir. Los patrones de host se normalizan al eliminar los espacios de los extremos, convertirlos a minúsculas y quitar el punto final, los puertos simples o los corchetes.                                                                                                                                                           |
| `[permissions.<name>.network.unix_sockets]`                       | Tabla                      | Ninguno                    | Configura excepciones a la lista de permitidos de sockets Unix. Úsalo solo para integraciones locales como Docker.                                                                                                                                                                                                                                                                                                                                         |
| `permissions.<name>.network.unix_sockets."<path>"`                | `allow` o `deny`          | Ninguno                    | Agrega una ruta absoluta de socket Unix a la lista de permitidos efectiva con `allow`, o la rechaza con `deny`. Las entradas denegadas se omiten de la lista de permitidos efectiva.                                                                                                                                                                                                                                                                |
| `permissions.<name>.network.proxy_url`                            | Cadena de URL                 | `http://127.0.0.1:3128` | Agente de escucha del proxy HTTP que se usa para `HTTP_PROXY`, `HTTPS_PROXY`, las variables de proxy de websocket y las variables de entorno de proxy de herramientas relacionadas.                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.enable_socks5`                        | Booleano                    | `true`                  | Habilita el agente de escucha SOCKS5 que se usa para `ALL_PROXY` y las variables de proxy FTP.                                                                                                                                                                                                                                                                                                                                                     |
| `permissions.<name>.network.socks_url`                            | Cadena de URL                 | `http://127.0.0.1:8081` | Dirección del agente de escucha SOCKS5.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `permissions.<name>.network.enable_socks5_udp`                    | Booleano                    | `true`                  | Habilita la compatibilidad de SOCKS5 con UDP cuando el agente de escucha SOCKS5 está habilitado.                                                                                                                                                                                                                                                                                                                                                               |
| `permissions.<name>.network.allow_upstream_proxy`                 | Booleano                    | `true`                  | Permite que el proxy de red del sandbox respete la configuración de proxy ascendente de `HTTP(S)_PROXY` y `ALL_PROXY` para las solicitudes salientes.                                                                                                                                                                                                                                                                                                          |
| `permissions.<name>.network.allow_local_binding`                  | Booleano                    | `false`                 | Desactiva la protección de redes locales y privadas cuando el valor es `true`. Cuando el valor es `false`, los literales locales exactos como `localhost` o `127.0.0.1` deben incluirse explícitamente en la lista de permitidos, y los nombres de host que se resuelven en direcciones IP locales o privadas permanecen bloqueados.                                                                                                                                                                                                |
| `permissions.<name>.network.dangerously_allow_non_loopback_proxy` | Booleano                    | `false`                 | Permite que los agentes de escucha del proxy se vinculen a direcciones que no sean de loopback. Déjalo sin configurar para el desarrollo local habitual.                                                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.dangerously_allow_all_unix_sockets`   | Booleano                    | `false`                 | Omite la lista de permitidos de sockets Unix cuando se admite el uso de proxy para sockets Unix. Esta es una vía de escape local de amplio alcance.                                                                                                                                                                                                                                                                                                               |

## Permisos del sistema de archivos

Las entradas del sistema de archivos usan `read`, `write` o `deny`:

| Acceso  | Significado                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `read`  | Permite que los comandos lean archivos y enumeren directorios dentro de la ruta. Los comandos no pueden crear, modificar, cambiar de nombre ni eliminar archivos allí. |
| `write` | Permite que los comandos lean y modifiquen archivos dentro de la ruta, incluida la creación, el cambio de nombre y la eliminación de archivos cuando lo permite el sistema operativo.  |
| `deny`  | Deniega tanto la lectura como la escritura dentro de la ruta. Úsalo para denegar una subruta dentro de un permiso más amplio de `read` o `write`.         |

Las entradas más específicas prevalecen sobre las más generales. Cuando dos entradas se aplican a la
misma ruta, `deny` prevalece sobre `write`, y `write` prevalece
sobre `read`.

Esta precedencia permite que un perfil describa primero un área de trabajo amplia y luego excluya
los archivos o directorios que deben permanecer inaccesibles para la lectura:

```toml
[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

En este ejemplo, la raíz del espacio de trabajo sigue permitiendo la escritura, `.devcontainer/` sigue
permitiendo la lectura, pero no la escritura, y los archivos de entorno coincidentes siguen
sin estar disponibles para los comandos ejecutados en el sandbox.

Una ruta más específica también puede volver a permitir el acceso a un subárbol más acotado dentro de una denegación más amplia:

```toml
[permissions.project-edit.filesystem]
"~/Documents" = "deny"
"~/Documents/codex" = "write"

Formatos de ruta compatibles:

| Ruta               | Significado                                                                                     | Subrutas delimitadas |
| ------------------ | ------------------------------------------------------------------------------------------- | --------------- |
| `:root`            | La raíz del sistema de archivos                                                                         | Solo `.`        |
| `:minimal`         | Rutas de la plataforma y del entorno de ejecución necesarias para las herramientas comunes                                           | Solo `.`        |
| `:workspace_roots` | Las raíces del espacio de trabajo de la sesión actual, junto con cualquier raíz del espacio de trabajo habilitada que se haya definido en el perfil      | Sí             |
| `:tmpdir`          | La ubicación de `$TMPDIR`, cuando esté disponible                                               | Solo `.`        |
| `:slash_tmp`       | La carpeta `/tmp`, si existe                                                             | Solo `.`        |
| `/absolute/path`   | Una ruta absoluta de la plataforma, como `/path` en macOS/Linux/WSL o `C:\path` en Windows nativo | Sí             |
| `~/path`           | Una ruta dentro del directorio de inicio del usuario actual                                              | Sí             |

En Windows nativo, las rutas relativas al directorio de inicio también pueden usar barras invertidas, como
`~\work`.

Usa `:root` solo cuando un perfil requiera intencionalmente acceso de lectura amplio:

```toml
[permissions.audit.filesystem]
":root" = "read"

Usa entradas anidadas en `:workspace_roots` para limitar el acceso a subrutas relativas a la raíz
del espacio de trabajo:

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"          # each workspace root
"docs" = "read"        # each workspace-root docs directory
"generated" = "deny"   # each workspace-root generated directory

Las subrutas anidadas deben permanecer dentro de la raíz de su espacio de trabajo. Se rechazan las referencias a directorios superiores, como
`../other-repo`.

### Denegar la lectura con rutas exactas o patrones glob

Usa `deny` para archivos o subárboles que Codex no deba leer, incluso cuando una regla más amplia
del perfil permita el acceso a ubicaciones cercanas. Las rutas exactas son adecuadas para ubicaciones estables,
como `~/.ssh`. Los patrones glob son más adecuados cuando un perfil debe abarcar una
familia de archivos sensibles cuyas ubicaciones exactas varían entre repositorios.

Cuando un patrón glob se encuentra en `:workspace_roots`, Codex lo interpreta en relación con cada
raíz efectiva del espacio de trabajo. Por ejemplo:

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

Esta regla deniega la lectura de los archivos `.env` coincidentes ubicados bajo cada raíz del espacio de trabajo del entorno de ejecución o
definida por el perfil. Úsala cuando quieras conservar las operaciones normales de escritura
en el espacio de trabajo e impedir la lectura de archivos de entorno, secretos generados u otros archivos similares
que contengan credenciales.

Los patrones glob `deny` se admiten como reglas de denegación de lectura. Los patrones glob `read` o `write`
son menos portables en el sandbox de Linux, WSL y Windows nativo, por lo que conviene usar rutas
exactas o reglas de subárbol como `"docs/**" = "read"`, siempre que sea posible.

En Linux, WSL y Windows nativo, un patrón `**` sin límites para denegar lecturas puede requerir
una expansión previa limitada antes de que se inicie el sandbox. Configura `glob_scan_max_depth` cuando
uses un patrón sin límites como `"**/*.env" = "deny"`:

```toml
[permissions.project-edit.filesystem]
glob_scan_max_depth = 3

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

`glob_scan_max_depth` debe ser al menos `1`. Con valores más altos, la exploración es más profunda antes
de iniciar el sandbox, lo que puede aumentar el trabajo de inicio en Linux, WSL y Windows nativo.
Si prefieres no usar una expansión limitada, enumera profundidades explícitas como
`*.env`, `*/*.env` y `*/*/*.env`.

Agrega al perfil raíces reutilizables del espacio de trabajo cuando las mismas reglas deban aplicarse a
otras raíces además de la raíz de la sesión actual:

```toml
[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

Cuando este perfil está activo, Codex aplica las reglas de `:workspace_roots` a las
raíces del espacio de trabajo del entorno de ejecución de la sesión actual y a cada raíz del espacio de trabajo definida en el perfil
que esté habilitada.

En Windows nativo, las rutas con letra de unidad, como `D:\work`, y las rutas UNC, como
`\\server\share`, se admiten como rutas absolutas.

## Permisos de red

El acceso a la red y el filtrado de red se configuran por separado. Configura
`permissions.<name>.network.enabled = true` para permitir que los comandos accedan a la red
y habilita `features.network_proxy` para aplicar las reglas de dominio del perfil:

```toml
[features]
network_proxy = true

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"example.com" = "allow"      # exact host
"*.example.com" = "allow"    # subdomains only
"**.example.com" = "allow"   # apex and subdomains
"ads.example.com" = "deny"   # deny wins over allow

El comportamiento resultante depende de ambas configuraciones:

- Red desactivada: los comandos no pueden acceder a la red, independientemente de la
función de proxy.
- Red activada, proxy desactivado: los comandos tienen acceso directo y sin restricciones a la
red. Las reglas de dominio del perfil de permisos no se aplican.
- Red activada, proxy activado: los comandos usan el proxy, que aplica las reglas de
dominio del perfil. Si el proxy activo no tiene dominios permitidos, bloquea los destinos
externos.

Agregar `[permissions.<name>.network.domains]` o configurar
`permissions.<name>.network.enabled = true` no habilita
`features.network_proxy`. Como alternativa, los administradores pueden habilitar el
proxy con `[experimental_network]` en `requirements.toml`. Consulta
[Configuración administrada](/es-419/codex/enterprise/managed-configuration#configure-network-access-requirements).

Cuando está activo, el proxy del sandbox de red se vincula de forma predeterminada a listeners locales:

```toml
[permissions.project-edit.network]
enabled = true
proxy_url = "http://127.0.0.1:3128"
enable_socks5 = true
socks_url = "http://127.0.0.1:8081"
enable_socks5_udp = true

Mantén la configuración predeterminada de estos listeners, salvo que necesites integrarlos con
un entorno de ejecución específico. Las claves de red `dangerously_*` son mecanismos de excepción para
entornos especializados y no deben usarse para el desarrollo local habitual.

### Redes locales y privadas

Cuando el proxy de red está activo, Codex aplica de forma predeterminada una protección para redes
locales y privadas frente al DNS rebinding y al acceso accidental a servicios locales.
Para permitir intencionalmente un destino local literal, agrega a la lista de permitidos
el host exacto o la dirección IP literal exacta:

```toml
[permissions.project-edit.network.domains]
"localhost" = "allow"
"127.0.0.1" = "allow"

Configura `allow_local_binding = true` solo cuando el perfil deba acceder a nombres de host incluidos en la lista de permitidos
que se resuelvan en direcciones locales o privadas:

```toml
[permissions.project-edit.network]
enabled = true
allow_local_binding = true

[permissions.project-edit.network.domains]
"localhost" = "allow"

### Sockets de Unix

El uso de proxy para sockets de Unix es un mecanismo de excepción local para herramientas como Docker. Úsalo
con moderación:

```toml
[permissions.project-edit.network.unix_sockets]
"/var/run/docker.sock" = "allow"
"/tmp/old.sock" = "deny"

Usa `deny` para rechazar una ruta de socket, incluso si una entrada heredada la permite. Las rutas
de socket rechazadas se excluyen de la lista efectiva de permitidos.

Cuando los sockets de Unix estén habilitados, mantén los listeners del proxy vinculados a direcciones de loopback.

## Migrar desde la configuración anterior del sandbox

Los perfiles de permisos sustituyen la combinación anterior de `sandbox_mode` y
`sandbox_workspace_write` cuando quieres que un solo perfil reutilizable describa el comportamiento
del sistema de archivos y de la red. Usa uno u otro sistema en una sesión, no
ambos.

Puntos de partida sugeridos:

- Para un flujo de trabajo de solo lectura, usa el perfil integrado `:read-only` o define un
  perfil personalizado con acceso de lectura únicamente donde sea necesario.
- Para editar el espacio de trabajo, usa el perfil integrado `:workspace` o define un
  perfil personalizado que escriba mediante `:workspace_roots` y agregue solo las rutas
  temporales o de caché adicionales que necesite el flujo de trabajo.
- Para la ejecución local sin restricciones, usa `:danger-full-access` solo cuando
  quieras intencionalmente el modelo de acceso local más amplio.

Los perfiles describen la postura local predeterminada de una sesión. Los requisitos administrados por la organización
pueden imponer restricciones adicionales que la configuración del usuario no debería
flexibilizar. Consulta [Configuración administrada](/es-419/codex/enterprise/managed-configuration)
para conocer las restricciones del sistema de archivos y de la red impuestas por los administradores.

## Alcance y aplicación

Los perfiles de permisos establecen los límites para la ejecución local de comandos dentro de un
sandbox. Úsalos junto con las políticas de aprobación y los controles independientes de la
búsqueda web, los conectores, los servidores MCP, el navegador integrado, el Uso de la computadora
y Codex Cloud.

### Qué controlan los perfiles

- **Ejecución local de comandos:** los perfiles de permisos regulan los comandos ejecutados dentro del sandbox
  de tu equipo. Los conectores, los servidores MCP, las interfaces del navegador o del
  Uso de la computadora, la configuración de los entornos de Codex Cloud y las
  escalaciones aprobadas cuentan con sus propios controles.
- **Escrituras en el sistema de archivos:** un perfil con permisos de escritura puede crear cambios persistentes.
  Considera sensibles las escrituras en scripts, pasos de compilación, hooks del gestor de paquetes, archivos de inicio
  del shell y directorios compartidos, porque posteriormente otras herramientas o usuarios pueden
  ejecutar esos archivos fuera del contexto original del sandbox.
- **Destinos de salida:** las reglas de dominio de red limitan los destinos del tráfico de los comandos ejecutados en el sandbox
  solo mientras el proxy de red está activo. No determinan
  si un destino permitido es confiable y las reglas de permiso con comodines
  mantienen un alcance amplio.
- **Servicios locales:** un proxy de red activo bloquea de forma predeterminada los destinos de redes locales y privadas.
  Agregar `localhost`, direcciones IP privadas o sockets de Unix a la lista de permitidos, o configurar
`allow_local_binding = true`, habilita explícitamente el acceso a servicios locales.

### Qué no controla el proxy de red

El proxy de red solo filtra el tráfico de los comandos locales que se ejecutan dentro del
sandbox. No aplica la lista de dominios permitidos del perfil a:

- **Búsqueda web:** la herramienta de búsqueda alojada usa su propia configuración de acceso. Usa
`web_search` y, en el caso de los clientes administrados, `allowed_web_search_modes` para
  controlarla. `tools.web_search.allowed_domains` filtra los resultados de búsqueda, no el acceso
  de los comandos a la red.
- **Apps y conectores:** las herramientas basadas en conectores usan sus propias conexiones del lado del servicio,
  los permisos del espacio de trabajo y la configuración de la app o la herramienta.
- **Servidores MCP:** los servidores MCP locales y remotos usan su propio proceso o
  transporte. Contrólalos mediante la configuración de `mcp_servers` y las listas administradas de servidores
  permitidos.
- **Navegador y Uso de la computadora:** la navegación en el navegador y las acciones de uso de la computadora
  usan sus propios controles de funciones y aprobación.
- **Tráfico de los servicios de Codex:** las solicitudes del modelo, de autenticación y de otros servicios del cliente
  usan la configuración independiente de HTTP y del proxy del sistema del cliente.
- **Codex Cloud:** estas tareas usan la propia
[configuración de acceso a Internet](/es-419/codex/cloud/internet-access) de su entorno.

Para limitar estas funciones, configura cada capacidad directamente. Una lista de destinos de red
permitidos para comandos no constituye una política de red global para todas las acciones que Codex puede realizar.

### Cómo se aplican las políticas

- En macOS, Codex usa perfiles de sandbox de Seatbelt. Si el sandbox de la plataforma no puede
aplicar la política seleccionada, Codex se niega a ejecutar el comando en lugar
de ejecutarlo sin avisar fuera del sandbox.
- En Linux y WSL, Codex usa [bubblewrap](https://github.com/containers/bubblewrap)
  y [seccomp](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html),
  mientras que Landlock está disponible para rutas alternativas de compatibilidad. El mecanismo
  de aplicación más sólido depende de los espacios de nombres de usuario y de la compatibilidad del kernel; los hosts de contenedores con restricciones
  pueden obligar a usar rutas de compatibilidad, y las políticas divididas no compatibles
  se rechazan.
- En Windows nativo, el [sandbox `elevated`](/es-419/codex/windows/windows-sandbox#windows-sandbox)
  es la opción más sólida porque puede usar usuarios dedicados del sandbox con menos privilegios,
  límites de permisos del sistema de archivos y reglas de firewall. El sandbox `unelevated`
  es una alternativa con un aislamiento de red más débil y no puede aplicar
  todas las excepciones que separan los permisos de lectura y escritura, por lo que se rechazan las políticas no compatibles. Usa WSL
  cuando necesites el modelo de sandbox de Linux.

### Recomendaciones operativas

Elige el perfil más restrictivo que permita completar la tarea, especialmente cuando
concedas permisos de escritura o acceso saliente a la red. Mantén la política de aprobación, la gestión de secretos
y las reglas de permiso en consonancia con ese nivel de acceso.

## Perfiles comunes

### Solo lectura con lista de destinos de red permitidos

```toml
default_permissions = "readonly-net"

[features]
network_proxy = true

[permissions.readonly-net.filesystem]
":minimal" = "read"

[permissions.readonly-net.filesystem.":workspace_roots"]
"." = "read"

[permissions.readonly-net.network]
enabled = true

[permissions.readonly-net.network.domains]
"api.openai.com" = "allow"

### Acceso a archivos limitado al espacio de trabajo

Este es un ejemplo de un perfil de permisos que permite a Codex escribir en las carpetas de tu espacio de trabajo y le deniega la lectura del resto del sistema de archivos (con excepciones limitadas, según lo determine `:minimal`).

```toml
default_permissions = "workspace-only"

[permissions.workspace-only]
# By extending the :workspace profile, you get Codex's safeguards to ensure
# subfolders such as .codex/ and .git/ within a workspace root are read-only
# while the rest of the folder is writable.
extends = ":workspace"

[permissions.workspace-only.filesystem]
# By default, deny read access to all files on disk.
":root" = "deny"

# Though in practice, a software agent needs to be able to read folders that
# contain common tools, such as `/usr/bin`, to get work done, so grant access
# to a "minimal" set of files and folders, as determined by Codex.
":minimal" = "read"

# By extending the :workspace profile, :tmpdir and :slash_tmp are "write" by
# default, though you can deny access to them altogether, if desired.
":tmpdir" = "deny"
":slash_tmp" = "deny"

### Escritura en el espacio de trabajo sin acceso a la red

```toml
default_permissions = "project-edit"

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"

[permissions.project-edit.network]
enabled = false

### Escritura en el espacio de trabajo con acceso a la web pública

```toml
default_permissions = "workspace-net"

[features]
network_proxy = true

[permissions.workspace-net.filesystem]
":minimal" = "read"

[permissions.workspace-net.filesystem.":workspace_roots"]
"." = "write"

[permissions.workspace-net.network]
enabled = true

[permissions.workspace-net.network.domains]
"*" = "allow"

Usa la regla global de autorización `"*"` solo cuando quieras permitir el
acceso a la red pública. Las reglas de denegación pueden restringir una lista de permitidos amplia.
