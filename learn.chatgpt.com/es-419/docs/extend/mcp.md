<!-- source: https://learn.chatgpt.com/es-419/docs/extend/mcp -->

El protocolo de contexto de modelos (MCP) conecta los modelos con herramientas y contexto. Úsalo para
dar a ChatGPT o Codex acceso a documentación de terceros, o para permitirles
interactuar con herramientas de desarrollo como tu navegador o Figma.

ChatGPT en la web puede usar herramientas remotas basadas en MCP que proporcionan los complementos. Los clientes locales de Codex
también pueden conectarse directamente a servidores MCP y compartir su configuración.

<a id="supported-mcp-features"></a>

La aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE admiten servidores MCP y
comparten la configuración de MCP para el mismo host de Codex.

Las funciones compatibles que se describen a continuación se aplican a los servidores MCP configurados en un
host de Codex. Las herramientas alojadas de los complementos pueden tener capacidades diferentes.

## Funciones de MCP compatibles

- **Servidores STDIO**: servidores que se ejecutan como un proceso local (iniciado mediante un comando).
  - Variables de entorno
- **Servidores Streamable HTTP**: servidores a los que accedes mediante una dirección.
  - Autenticación mediante token portador
  - Autenticación OAuth, incluidos los documentos de metadatos del ID de cliente (CIMD) y
el registro dinámico de clientes (DCR)
  - Autenticación con la sesión de ChatGPT para servidores propios de confianza
- **Instrucciones del servidor**: Codex lee el campo `instructions` de MCP que se devuelve durante la inicialización y lo usa como guía para todo el servidor, junto con las herramientas del servidor.

Si desarrollas o mantienes un servidor MCP para Codex, usa `instructions` para los flujos de trabajo entre herramientas, las restricciones y los límites de solicitudes aplicables a todo el servidor. Asegúrate de que los primeros 512 caracteres sean comprensibles por sí solos para que Codex tenga disponibles las indicaciones más importantes cuando decida cómo usar el servidor.

## Conectar Codex a un servidor MCP

Codex almacena la configuración de MCP en `config.toml`, junto con otras opciones de configuración de Codex. De forma predeterminada, este archivo se encuentra en `~/.codex/config.toml`, pero también puedes configurar servidores MCP para un proyecto específico con `.codex/config.toml` (solo en proyectos de confianza).

La aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE comparten esta configuración.
Una vez que configures tus servidores MCP, puedes alternar entre esos clientes sin
tener que repetir la configuración.

### Configurar en la aplicación de escritorio de ChatGPT

1. Abre **Configuración** y luego selecciona **Servidores MCP**.
2. Selecciona **Agregar servidor**.
3. Ingresa un nombre, elige **STDIO** o **Streamable HTTP** y proporciona el
   comando o la URL del servidor.
4. Guarda el servidor y luego selecciona **Reiniciar**.

La lista de servidores muestra cuáles están habilitados y cuáles requieren OAuth. Selecciona
**Autenticar** cuando un servidor OAuth requiera iniciar sesión. En el editor, escribe `/mcp`
para ver los servidores conectados.

## Usar herramientas basadas en MCP en ChatGPT en la web

En un chat alojado de ChatGPT Work, instala un [complemento](/es-419/codex/plugins) para usar los
conectores y las herramientas MCP remotas que incluye. Después de la instalación, Chat y Work pueden
usar esas herramientas. Los administradores del espacio de trabajo pueden controlar qué complementos y herramientas
están disponibles.

ChatGPT en la web no lee los archivos locales de configuración de Codex ni muestra el menú local
de comandos de Codex. Abre la pestaña **Complementos** para explorar y administrar las
herramientas disponibles.

### Configurar con la CLI

#### Agregar un servidor MCP

```bash
codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>

Por ejemplo, para agregar Context7 (un servidor MCP gratuito de documentación para desarrolladores), puedes ejecutar el siguiente comando:

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp

#### Otros comandos de la CLI

Ejecuta `codex mcp list` para ver los servidores configurados. Para ver todos los comandos de MCP
disponibles, ejecuta `codex mcp --help`. Si un servidor admite OAuth, ejecuta
`codex mcp login <server-name>`.

#### Interfaz de usuario en la terminal (TUI)

En la TUI de `codex`, usa `/mcp` para ver tus servidores MCP activos.

### Configurar en la extensión para IDE

1. Abre el menú del ícono de engranaje y luego selecciona **Servidores MCP**.
2. Selecciona **Agregar servidor**.
3. Ingresa un nombre, elige **STDIO** o **Streamable HTTP** y proporciona el
   comando o la URL del servidor.
4. Guarda el servidor y luego selecciona **Reiniciar extensión**.

La lista de servidores MCP muestra cuáles están habilitados y cuáles requieren OAuth.
Selecciona **Autenticar** cuando un servidor OAuth requiera iniciar sesión.

### Configurar con config.toml

Para tener un control más preciso, edita `~/.codex/config.toml` o un archivo
`.codex/config.toml` específico del proyecto. Consulta la [referencia de configuración](/es-419/codex/config-file/config-reference)
para acceder a una lista con función de búsqueda de todas las opciones de MCP compatibles.

Configura cada servidor MCP con una tabla `[mcp_servers.<server-name>]` en el archivo de configuración.

<a id="stdio-servers"></a>

#### Servidores STDIO

- `command` (obligatorio): el comando que inicia el servidor.
- `args` (opcional): argumentos que se pasarán al servidor.
- `env` (opcional): variables de entorno que se establecerán para el servidor.
- `env_vars` (opcional): variables de entorno que se permitirán y reenviarán.
- `cwd` (opcional): directorio de trabajo desde el que se iniciará el servidor.
- `experimental_environment` (opcional): establece el valor en `remote` para iniciar el servidor stdio
  mediante el entorno de un ejecutor remoto cuando haya uno disponible.

`env_vars` puede contener nombres de variables u objetos que indiquen un origen:

```toml
env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]

Las entradas de tipo cadena y `source = "local"` obtienen valores del entorno local de Codex.
`source = "remote"` obtiene valores del entorno del ejecutor remoto y requiere
stdio remoto de MCP.

<a id="streamable-http-servers"></a>

#### Servidores Streamable HTTP

- `url` (obligatorio): la dirección del servidor.
- `auth` (opcional): autenticación que se intentará después de probar los tokens portadores y los
  encabezados de autorización configurados. Usa `oauth` (valor predeterminado) para las credenciales OAuth
  de MCP almacenadas. Usa `chatgpt` para emplear la sesión actual de ChatGPT con el origen
  propio de confianza de ChatGPT, con las credenciales OAuth almacenadas como alternativa.
- `bearer_token_env_var` (opcional): nombre de la variable de entorno que contiene un token portador para enviar en `Authorization`.
- `http_headers` (opcional): mapa que asocia nombres de encabezados con valores estáticos.
- `env_http_headers` (opcional): mapa que asocia nombres de encabezados con nombres de variables de entorno (los valores se obtienen del entorno).
- `http_headers_helper` (opcional): comando local que imprime un objeto JSON con
  nombres de encabezados y valores de tipo cadena, como `{"X-Auth": "temporary-token"}`.
  Se admite para conexiones MCP por HTTP realizadas desde el entorno local, pero no para
  servidores stdio ni conexiones realizadas a través de un entorno de ejecución remoto.

Codex almacena en caché los encabezados proporcionados por el comando auxiliar para la conexión. Después de que una solicitud POST al mismo origen
devuelva `401` o `403`, actualiza los encabezados una vez y solo vuelve a intentarlo si el
comando auxiliar devuelve valores distintos. Los tokens portadores explícitos y las credenciales OAuth
tienen prioridad sobre el encabezado `Authorization` proporcionado por el comando auxiliar.
Una respuesta `403` de OAuth que indique un alcance insuficiente no activa la
actualización mediante el comando auxiliar.

Si ninguna fuente proporciona credenciales, Codex puede conectarse al servidor sin
autenticación. Ejecuta `codex mcp login <server-name>` por separado para iniciar la autenticación
OAuth de MCP.

#### Otras opciones de configuración

- `startup_timeout_sec` (opcional): tiempo de espera (en segundos) para que se inicie el servidor. Valor predeterminado: `10`.
- `tool_timeout_sec` (opcional): tiempo de espera (en segundos) para que el servidor ejecute una herramienta. Valor predeterminado: `60`.
- `enabled` (opcional): establece `false` para desactivar un servidor sin eliminarlo.
- `required` (opcional): establece `true` para que el inicio falle si este servidor habilitado no puede inicializarse.
- `enabled_tools` (opcional): lista de herramientas permitidas.
- `disabled_tools` (opcional): lista de herramientas denegadas (se aplica después de `enabled_tools`).
- `default_tools_approval_mode` (opcional): comportamiento predeterminado de aprobación para las
  herramientas de este servidor. Los valores admitidos son `auto`, `prompt`, `writes` y
`approve`. El modo `writes` solicita aprobación para las herramientas que no estén marcadas como de solo lectura.
- `tools.<tool>.approval_mode` (opcional): comportamiento de aprobación personalizado por herramienta.
- `tools.<tool>.output_token_limit` (opcional): presupuesto de tokens mayor que cero para la salida de una
  herramienta, antes de sumar el margen estándar del 20 % para la serialización. Reemplaza el
  presupuesto predeterminado del modelo para truncar la salida de esa herramienta.

La opción de nivel superior `mcp_optional_startup_grace_ms` controla cuánto tiempo espera Codex
a los servidores MCP opcionales al crear el catálogo inicial de herramientas. Su valor
predeterminado es `1000` milisegundos. Configúrala en `0` para usar en su lugar el tiempo de espera
`startup_timeout_sec` de cada servidor. Los servidores obligatorios siguen usando sus tiempos
de espera de inicio.

#### Registro de clientes OAuth y devoluciones de llamada

Cuando tu servidor de autorización requiera un cliente OAuth registrado previamente, proporciona
su ID de cliente al agregar el servidor MCP:

```bash
codex mcp add example --url https://mcp.example.com --oauth-client-id my-client

Codex muestra la URL completa de devolución de llamada para que la registres con tu proveedor:

```text
OAuth callback URL: http://127.0.0.1/callback

Codex guarda la devolución de llamada junto con el ID de cliente en `config.toml` para futuros
inicios de sesión:

```toml
[mcp_servers.example]
url = "https://mcp.example.com"

[mcp_servers.example.oauth]
client_id = "my-client"
callback_url = "http://127.0.0.1/callback"

Los clientes registrados previamente que se acaban de agregar usan una devolución de llamada estable solo cuando el
servidor de autorización anuncia
`authorization_response_iss_parameter_supported: true` y proporciona en sus metadatos un
`issuer`. Si no se anuncia compatibilidad con el emisor, Codex agrega al final un ID de devolución de llamada
específico del servidor, como `http://127.0.0.1/callback/XuuuHAzzHOni`. Los clientes existentes
sin una devolución de llamada guardada siguen usando la redirección específica de su ID de devolución de llamada.

Durante el inicio de sesión, la selección de la devolución de llamada depende de la configuración de OAuth y de
los metadatos del servidor de autorización:

| Configuración de OAuth                                                | Compatibilidad con el emisor           | Devolución de llamada utilizada                                                                                                                                      |
| ------------------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_url` sin `client_id`                                 | Compatible                | La devolución de llamada configurada se usa para registrar el cliente.                                                                                           |
| `callback_url` sin `client_id`                                 | No compatible              | Para registrar el cliente, se usa la devolución de llamada configurada con el ID de devolución de llamada específico del servidor agregado al final.                                             |
| `client_id` y `callback_url`                                     | Compatible                | Se reutiliza la devolución de llamada configurada; la respuesta de autorización debe contener un `iss` coincidente.                                                     |
| `client_id` y un valor de `callback_url` que termina con el ID de devolución de llamada correcto | No compatible              | Se reutiliza la devolución de llamada configurada sin cambios.                                                                                                       |
| `client_id` y un valor de `callback_url` que no incluye el ID de devolución de llamada correcto   | No compatible              | Se ignora la devolución de llamada configurada. Codex usa `mcp_oauth_callback_url` o, si no se ha configurado, `http://127.0.0.1/callback`, con el ID de devolución de llamada agregado al final. |
| `client_id` sin un valor de `callback_url` configurado                    | Compatible o no compatible | Codex usa la devolución de llamada global o predeterminada con el ID de devolución de llamada específico del servidor agregado al final.                                                           |

El uso de la alternativa no modifica la URL de devolución de llamada almacenada. Codex obtiene el ID de devolución de llamada
a partir de la URL del servidor MCP, incluidas su ruta y cadena de consulta. Las mismas
reglas de selección se aplican al inicio de sesión automático y al explícito.

Configura `mcp_oauth_callback_url` cuando necesites una ruta de devolución de llamada personalizada o una URL de entrada de un
Devbox remoto. Los clientes registrados previamente que se acaban de agregar usan esa URL sin cambios
si su proveedor admite la identificación del emisor. De lo contrario, usan la
URL configurada con el ID de devolución de llamada específico del servidor agregado al final. Registra siempre
la devolución de llamada exacta que muestra `codex mcp add`.

Para las devoluciones de llamada `http://127.0.0.1` sin puerto, Codex omite el puerto de escucha en
la URL que muestra y almacena, y luego inserta el puerto de escucha activo durante
la autorización. Esta sustitución no se aplica a `localhost`, a hosts IPv6,
a URL HTTPS ni a devoluciones de llamada que ya incluyan un puerto. Los servidores de autorización
deben aceptar puertos de loopback variables según
[RFC 8252, sección 7.3](https://www.rfc-editor.org/rfc/rfc8252#section-7.3).

Configura `mcp_oauth_callback_port` para elegir un puerto de escucha global fijo, o configura
`mcp_servers.<server-name>.oauth.callback_port` para reemplazarlo en un servidor específico.
Un puerto explícito en la URL de devolución de llamada no configura el proceso de escucha. Para una
devolución de llamada directa de loopback, usa `http://127.0.0.1` sin puerto o configura el mismo
puerto explícito tanto para la URL de devolución de llamada como para el proceso de escucha. Una devolución de llamada a través de un proxy puede
usar intencionalmente un puerto en la URL externa distinto del puerto
de escucha local. Las URL locales de devolución de llamada se enlazan a la interfaz local; las no locales
se enlazan a `0.0.0.0`.

Codex valida cualquier `iss` devuelto antes de intercambiar el código de autorización. Si
`iss` no coincide, siempre se rechaza la respuesta. Cuando se anuncia compatibilidad con el emisor,
también se rechaza si falta `iss`. Ante cualquiera de estos errores, no se intercambia el código ni se recurre
a otra devolución de llamada. Una URL de devolución de llamada mal formada o el anuncio de compatibilidad con el emisor
sin un emisor en los metadatos también siguen provocando un error que impide continuar. Consulta
[Autenticar usuarios](/plugins/build/auth).

Si el servidor MCP anuncia `scopes_supported`, Codex prefiere esos
alcances anunciados por el servidor durante el inicio de sesión con OAuth. De lo contrario, Codex recurre a los
alcances configurados en `config.toml`.

#### Registro de clientes OAuth

Codex admite los [documentos de metadatos de ID de cliente OAuth (CIMD)](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)
y el registro dinámico de clientes (DCR). De manera predeterminada, Codex elige automáticamente
CIMD cuando el servidor de autorización anuncia
`client_id_metadata_document_supported: true`, incluye `none` en
`token_endpoint_auth_methods_supported` y la devolución de llamada usa una URL de
loopback compatible. De lo contrario, Codex usa DCR cuando está disponible. Si hay un ID de cliente OAuth
configurado, este siempre tiene prioridad y se omite el registro del cliente.

Para CIMD, Codex usa un documento de metadatos alojado en ChatGPT y específico del
servidor MCP:

```text
https://chatgpt.com/oauth/codex/<callback_id>/client.json

Codex obtiene `<callback_id>` a partir de la URL del servidor MCP y lo incluye en la
URI de redirección de loopback, por ejemplo,
`http://127.0.0.1:<port>/callback/<callback_id>`. El documento de metadatos registra
la URI de loopback correspondiente sin puerto. Los servidores de autorización deben aceptar el
puerto seleccionado al iniciar sesión y verificar que el host y la ruta coincidan exactamente, como exige
[RFC 8252](https://www.rfc-editor.org/rfc/rfc8252.html#section-7.3). Los hosts, las rutas o los parámetros
de consulta personalizados para la devolución de llamada requieren DCR o un ID de cliente
OAuth configurado.

La compatibilidad con un documento CIMD estable y compartido está en desarrollo y estará disponible próximamente:

```text
https://chatgpt.com/oauth/codex/client.json

Codex usará el documento estable con la ruta compartida `/callback` cuando el
servidor de autorización anuncie
`authorization_response_iss_parameter_supported: true`, proporcione un
`issuer` válido en sus metadatos e incluya un `iss` coincidente en las
respuestas de autorización. Los servidores cuyas respuestas no estén vinculadas al emisor seguirán usando el
documento específico de la devolución de llamada.

Para elegir un método de registro para un inicio de sesión en la CLI, usa
`--oauth-client-registration`:

```bash
codex mcp login <server-name> --oauth-client-registration cimd
codex mcp login <server-name> --oauth-client-registration dcr

El valor predeterminado es `auto`. Las opciones de registro solo se aplican al inicio de sesión actual y
no se almacenan en `config.toml`.

#### Ejemplos de config.toml

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env_vars = ["LOCAL_TOKEN"]

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"

```toml
# Optional MCP OAuth callback overrides (used by `codex mcp login`)
mcp_oauth_callback_port = 5555
mcp_oauth_callback_url = "https://devbox.example.internal/callback"

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }

```toml
[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
enabled_tools = ["open", "screenshot"]
disabled_tools = ["screenshot"] # applied after enabled_tools
default_tools_approval_mode = "prompt"
startup_timeout_sec = 20
tool_timeout_sec = 45
enabled = true

[mcp_servers.chrome_devtools.tools.open]
approval_mode = "approve"
output_token_limit = 30000

### Servidores MCP proporcionados por complementos

Los complementos instalados pueden incluir servidores MCP en su archivo de manifiesto. Esos
servidores se inician desde el complemento, por lo que la configuración del usuario no establece su
comando de transporte. La configuración del usuario sí puede controlar el estado de activación y la política de herramientas
en `plugins.<plugin>.mcp_servers.<server>`.

```toml
[plugins."sample@test".mcp_servers.sample]
enabled = true
default_tools_approval_mode = "prompt"
enabled_tools = ["read", "search"]

[plugins."sample@test".mcp_servers.sample.tools.search]
approval_mode = "approve"

Los servidores MCP HTTP proporcionados por complementos también pueden declarar la configuración de OAuth en `.mcp.json`.
Los archivos de manifiesto de los complementos usan los nombres de campo en camelCase `clientId`, `callbackUrl` y
`callbackPort`:

```json
{
  "mcpServers": {
    "sample": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "clientId": "my-pre-registered-client",
        "callbackUrl": "http://127.0.0.1/callback/registered"
      }
    }
  }
}

Los servidores MCP proporcionados por complementos siguen las mismas reglas de selección de devolución de llamada que otros
servidores MCP. Si un complemento proporciona un `clientId`, su proveedor no admite
devoluciones de llamada vinculadas al emisor y `callbackUrl` no incluye el ID de devolución de llamada
específico del servidor, Codex ignora esa URL para el inicio de sesión y usa `mcp_oauth_callback_url` o,
si no se ha configurado, `http://127.0.0.1/callback`, con el ID de devolución de llamada agregado al final. El
valor de `callbackUrl` configurado no cambia.

El valor de `oauth.callbackPort` de un complemento prevalece sobre el valor global de
`mcp_oauth_callback_port`; si no se configura ninguno de los dos, Codex elige un puerto efímero.
El puerto incluido en `callbackUrl` no determina el puerto de escucha. Para una
devolución de llamada directa de loopback con un puerto fijo, configura ambos valores para que coincidan:

```json
{
  "callbackUrl": "http://127.0.0.1:4321/callback/registered",
  "callbackPort": 4321
}

Si usas una entrada remota u otro proxy, el puerto de la URL de devolución de llamada y el puerto de escucha
local pueden diferir intencionalmente cuando el proxy reenvía al proceso de escucha
configurado.

## Ejemplos de servidores MCP útiles

La lista de servidores MCP sigue creciendo. Estos son algunos ejemplos comunes:

- [MCP de la documentación de OpenAI](/learn/docs-mcp): busca y lee la documentación para desarrolladores de OpenAI.
- [Context7](https://github.com/upstash/context7): conéctate a documentación actualizada para desarrolladores.
- Figma [Local](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) y [Remoto](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/): accede a tus diseños de Figma.
- [Playwright](https://www.npmjs.com/package/@playwright/mcp): controla e inspecciona un navegador con Playwright.
- [Herramientas para desarrolladores de Chrome](https://github.com/ChromeDevTools/chrome-devtools-mcp/): controla e inspecciona Chrome.
- [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex): accede a los registros de Sentry.
- [GitHub](https://github.com/github/github-mcp-server): administra GitHub más allá de lo que permite `git` (por ejemplo, pull requests e issues).
