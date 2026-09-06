<!-- source: https://learn.chatgpt.com/es-419/docs/auth -->

## Autenticación de OpenAI

<a id="sign-in-with-chatgpt"></a>

Codex admite dos formas de iniciar sesión al usar modelos de OpenAI:

- Iniciar sesión con ChatGPT para acceder mediante una suscripción
- Iniciar sesión con una clave de API para acceder según el uso

La aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE admiten ambos métodos de inicio de sesión
para trabajar de forma local. Codex Cloud requiere iniciar sesión con ChatGPT.

El método de inicio de sesión también determina qué controles administrativos y políticas de tratamiento de datos se aplican.

- Cuando inicias sesión con ChatGPT, el uso de Codex se rige por los permisos de tu espacio de trabajo
de ChatGPT, el control de acceso basado en roles (RBAC) y la configuración de retención y residencia
de datos de ChatGPT Enterprise.
- En cambio, con una clave de API, el uso se rige por la configuración de retención y
uso compartido de datos de tu organización de la API.

En los espacios de trabajo administrados, la autenticación es solo una capa de acceso. La
pertenencia al espacio de trabajo y el aprovisionamiento determinan quién puede iniciar sesión, mientras que los puestos y
roles del espacio de trabajo determinan qué interfaces y funciones del producto pueden usar.
Para el trabajo local en la aplicación de escritorio de ChatGPT, Codex CLI o la extensión para IDE,
los perfiles de permisos limitan lo que el agente puede hacer en el dispositivo. Consulta
[Grupos y aprovisionamiento](/es-419/codex/enterprise/groups-and-provisioning)
y [Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions)
para planificar esos controles.

### Iniciar sesión con ChatGPT

Cuando inicias sesión con ChatGPT desde la aplicación de escritorio de ChatGPT, Codex CLI o la extensión para IDE, el flujo de inicio de sesión abre una ventana del navegador. Después de iniciar sesión, el navegador devuelve tus credenciales a Codex.

### ChatGPT en la web

Abre [ChatGPT](https://chatgpt.com), inicia sesión y elige el espacio de trabajo en el que
quieras trabajar. ChatGPT en la web mantiene la sesión autenticada en tu navegador.

#### Aplicación de escritorio de ChatGPT

En la pantalla sin sesión iniciada, selecciona **Continuar para iniciar sesión** y luego completa el
flujo en el navegador.

#### Codex CLI

Ejecuta `codex login` y luego completa el flujo en el navegador. Esta es la ruta de
autenticación predeterminada cuando no hay una sesión válida disponible.

#### Extensión para IDE

En la pantalla sin sesión iniciada, selecciona **Iniciar sesión con ChatGPT** y luego completa el
flujo en el navegador.

<a id="sign-in-with-an-api-key"></a>

### Iniciar sesión con una clave de API

También puedes iniciar sesión en la aplicación de escritorio de ChatGPT, Codex CLI o la extensión para IDE con una clave de API. Obtén tu clave de API en el [panel de OpenAI](https://platform.openai.com/api-keys).

#### Aplicación de escritorio de ChatGPT

En la pantalla sin sesión iniciada, selecciona **Iniciar sesión de otra forma**, ingresa tu clave y luego
selecciona **Continuar**.

#### Codex CLI

Canaliza la clave hacia `codex login` mediante stdin:

```shell
printenv OPENAI_API_KEY | codex login --with-api-key

#### Extensión para IDE

En la pantalla sin sesión iniciada, selecciona **Usar clave de API**, ingresa tu clave y luego
selecciona **Aceptar**.

OpenAI factura el uso de la clave de API a través de tu cuenta de la Plataforma de OpenAI según las tarifas estándar de la API. Consulta la [página de precios de la API](https://openai.com/api/pricing/).

La autenticación con clave de API admite flujos de trabajo locales de Codex, pero algunas funciones que
dependen del acceso al espacio de trabajo de ChatGPT o de servicios en la nube tienen limitaciones o no están disponibles.
Compara la compatibilidad según el plan en
[Disponibilidad de funciones](/es-419/codex/pricing#feature-availability).

En Codex CLI y Codex en la aplicación de escritorio de ChatGPT, la autenticación con clave de API
incluye acceso a los complementos compatibles seleccionados por OpenAI. Algunos complementos no están
disponibles porque sus flujos de conexión requieren funciones de OAuth
que no son compatibles. Consulta [Usar complementos](/es-419/codex/plugins#api-key-availability).

Cuando inicias sesión con una clave de API, Codex aplica los precios estándar de la API en lugar de
los créditos incluidos en el plan de ChatGPT.

Usa la autenticación con clave de API para flujos de trabajo programáticos de Codex CLI, como las tareas de
CI/CD. No expongas la ejecución de Codex en entornos públicos o que no sean de confianza.

### Comprobar la autenticación o cerrar sesión

Abre el menú del perfil para confirmar la cuenta y el espacio de trabajo activos. Para finalizar la
sesión de ChatGPT en la web en ese navegador, selecciona **Cerrar sesión**.

Abre el menú del perfil para ver la cuenta activa o el estado de la clave de API. Selecciona
**Cerrar sesión** para borrar las credenciales actuales.

Ejecuta `codex login status` para ver el método de autenticación activo. Para la autenticación
almacenada, ejecuta `codex logout` para borrar las credenciales actuales. Cuando
el proceso selecciona la identidad de carga de trabajo, Codex rechaza `codex login` y
`codex logout` porque el entorno del proceso controla la autenticación.

Abre el menú del perfil para ver la cuenta activa o el estado de la clave de API. Selecciona
**Cerrar sesión** para borrar las credenciales actuales.

### Usar tokens de acceso de Codex para la automatización empresarial

En los espacios de trabajo de ChatGPT Enterprise, los administradores pueden otorgar el permiso para tokens de acceso
para que los miembros autorizados creen tokens de acceso de Codex destinados a flujos de trabajo locales de Codex de confianza,
que no requieren interacción. Usa un token de acceso cuando la automatización
necesite acceder al espacio de trabajo de ChatGPT, a los derechos de uso de Codex administrados por ChatGPT o
a los controles empresariales del espacio de trabajo sin iniciar sesión en un navegador.

Los tokens de acceso están destinados a scripts, planificadores y ejecutores privados de CI que sean de confianza.
Para las llamadas generales a la API de OpenAI, sigue usando claves de API de la Plataforma.

Para conocer los pasos de configuración y la guía sobre permisos, rotación y revocación, consulta
[Tokens de acceso](/es-419/codex/enterprise/access-tokens).

Si tu plataforma en la nube, sistema de CI o clúster ya emite tokens de corta duración
para cargas de trabajo, usa la
[federación de identidades de cargas de trabajo](/es-419/codex/enterprise/workload-identity)
en lugar de almacenar una credencial de OpenAI.

Si tu entorno ya proporciona un token de acceso de Codex, canalízalo a la CLI:

```shell
printenv CODEX_ACCESS_TOKEN | codex login --with-access-token

## Proteger tu cuenta de Codex Cloud

Codex Cloud interactúa directamente con tu base de código, por lo que necesita mayor seguridad que muchas otras funciones de ChatGPT. Habilita la autenticación multifactor (MFA).

Si usas un proveedor de inicio de sesión social (Google, Microsoft o Apple), no es obligatorio habilitar la MFA en tu cuenta de ChatGPT, pero puedes configurarla con tu proveedor de inicio de sesión social.

Para ver las instrucciones de configuración, consulta:

- [Google](https://support.google.com/accounts/answer/185839)
- [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661)
- [Apple](https://support.apple.com/en-us/102660)

Si accedes a ChatGPT mediante inicio de sesión único (SSO), el administrador de SSO de tu organización debería exigir la MFA a todos los usuarios.

Si inicias sesión con un correo electrónico y una contraseña, debes configurar la MFA en tu cuenta antes de acceder a Codex Cloud.

Si tu cuenta admite más de un método de inicio de sesión y uno de ellos es el correo electrónico y la contraseña, debes configurar la MFA antes de acceder a Codex, incluso si inicias sesión de otra forma.

<a id="login-caching"></a>

## Almacenamiento en caché del inicio de sesión

Cuando inicias sesión en la aplicación de escritorio de ChatGPT, Codex CLI o la extensión para IDE con ChatGPT o una clave de API, tus datos de inicio de sesión se almacenan en caché y se reutilizan. La CLI y la extensión comparten los mismos datos de inicio de sesión almacenados en caché. Si cierras sesión en cualquiera de las dos, tendrás que volver a iniciar sesión la próxima vez que inicies la CLI o la extensión.

Codex almacena los datos de inicio de sesión en la caché local, ya sea en un archivo de texto sin formato ubicado en `~/.codex/auth.json` o en el almacén de credenciales específico de tu sistema operativo.

En las sesiones iniciadas con ChatGPT, Codex actualiza automáticamente los tokens durante el uso antes de que caduquen, por lo que las sesiones activas suelen continuar sin requerir otro inicio de sesión en el navegador.

<a id="credential-storage"></a>
<a id="enforce-a-login-method-or-workspace"></a>

## Almacenamiento de credenciales

Usa `cli_auth_credentials_store` para controlar dónde almacena Codex CLI las credenciales en caché:

```toml
# file | keyring | auto
cli_auth_credentials_store = "keyring"

- `file` almacena las credenciales en `auth.json`, dentro de `CODEX_HOME` (el valor predeterminado es `~/.codex`).
- `keyring` almacena las credenciales en el almacén de credenciales de tu sistema operativo.
- `auto` usa el almacén de credenciales del sistema operativo cuando está disponible; de lo contrario, recurre a `auth.json`.

Consulta la [referencia de configuración](/es-419/codex/config-file/config-reference) para conocer el esquema completo de
`config.toml`.

  Si usas almacenamiento basado en archivos, trata `~/.codex/auth.json` como una contraseña: el archivo
  contiene tokens de acceso. No lo incluyas en ningún commit, no lo pegues en tickets ni lo compartas en el
  chat.

## Exigir un método de inicio de sesión o un espacio de trabajo

En entornos administrados, los administradores pueden restringir cómo pueden autenticarse los usuarios:

```toml
# Only allow ChatGPT login or only allow API key login.
forced_login_method = "chatgpt" # or "api"

# When using ChatGPT login, restrict users to a specific workspace.
forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"

Si las credenciales activas no coinciden con las restricciones configuradas, Codex cierra la sesión del usuario y se cierra.

Por lo general, estos ajustes se aplican mediante la configuración administrada, no mediante la configuración individual de cada usuario. Consulta [Configuración administrada](/es-419/codex/enterprise/managed-configuration).

## Diagnóstico de inicio de sesión

Las ejecuciones directas de `codex login` crean un archivo específico `codex-login.log` en
el directorio de registros configurado. Úsalo cuando necesites depurar fallas del inicio de sesión en el navegador o
del código de dispositivo, o cuando el equipo de soporte solicite registros específicos del inicio de sesión.

## Paquetes personalizados de CA

Si tu red usa un proxy TLS corporativo o una CA raíz privada, configura
`CODEX_CA_CERTIFICATE` con un paquete PEM antes de iniciar sesión. Cuando
`CODEX_CA_CERTIFICATE` no está configurado, Codex usa `SSL_CERT_FILE` como alternativa. La misma
configuración de CA personalizada se aplica al inicio de sesión, a las solicitudes HTTPS normales y a las conexiones WebSocket
seguras.

```shell

codex login

## Inicio de sesión en dispositivos sin interfaz gráfica

Si inicias sesión en ChatGPT con Codex CLI, es posible que la interfaz de inicio de sesión basada en el navegador no funcione en ciertas situaciones:

- Estás ejecutando la CLI en un entorno remoto o sin interfaz gráfica.
- Tu configuración de red local bloquea el callback de localhost que Codex usa para devolver el token de OAuth a la CLI después de que inicias sesión.

En estas situaciones, es preferible usar la autenticación mediante código de dispositivo (beta). En la interfaz interactiva de inicio de sesión, elige **Iniciar sesión con código de dispositivo** o ejecuta directamente `codex login --device-auth`. Si la autenticación mediante código de dispositivo no funciona en tu entorno, usa uno de los métodos alternativos.

### Opción preferida: autenticación mediante código de dispositivo (beta)

1. Habilita el inicio de sesión con código de dispositivo en la configuración de seguridad de ChatGPT (cuenta personal) o en los permisos del espacio de trabajo de ChatGPT (administrador del espacio de trabajo).
2. En la terminal donde ejecutas Codex, elige una de estas opciones:
   - En la interfaz interactiva de inicio de sesión, selecciona **Iniciar sesión con código de dispositivo**.
   - Ejecuta `codex login --device-auth`.
3. Abre el enlace en tu navegador, inicia sesión y luego ingresa el código de un solo uso.

Si el inicio de sesión con código de dispositivo no está disponible en tu entorno, usa uno de los
métodos alternativos que se indican a continuación.

### Alternativa: iniciar sesión localmente y copiar la caché de autenticación

Si puedes completar el flujo de inicio de sesión en una máquina con navegador, puedes copiar tus credenciales almacenadas en caché a la máquina sin interfaz gráfica.

1. En una máquina donde puedas usar el flujo de inicio de sesión basado en el navegador, ejecuta `codex login`.
2. Confirma que la caché de inicio de sesión exista en `~/.codex/auth.json`.
3. En la máquina sin interfaz gráfica, copia `~/.codex/auth.json` en `~/.codex/auth.json`.

Trata `~/.codex/auth.json` como una contraseña: contiene tokens de acceso. No lo incluyas en ningún commit, no lo pegues en tickets ni lo compartas en el chat.

Si tu sistema operativo almacena las credenciales en un almacén de credenciales en lugar de `~/.codex/auth.json`, es posible que este método no sea aplicable. Consulta
[Almacenamiento de credenciales](/es-419/codex/auth#credential-storage) para saber cómo configurar el almacenamiento basado en archivos.

Cópialo a una máquina remota mediante SSH:

```shell
ssh user@remote 'mkdir -p ~/.codex'
scp ~/.codex/auth.json user@remote:~/.codex/auth.json

O usa un comando de una sola línea que evita usar `scp`:

```shell
ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json

Cópialo en un contenedor de Docker:

```shell
# Replace MY_CONTAINER with the name or ID of your container.
CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"

Para ver una versión más avanzada de este mismo patrón en ejecutores de CI/CD de confianza, consulta
[Mantener la autenticación de la cuenta de Codex en CI/CD (avanzado)](/codex/auth/ci-cd-auth).
Esa guía explica cómo permitir que Codex actualice `auth.json` durante las ejecuciones normales y
cómo conservar después el archivo actualizado para la siguiente tarea. Las claves de API siguen siendo la opción predeterminada
recomendada para la automatización.

### Alternativa: reenviar el callback de localhost mediante SSH

Si puedes reenviar puertos entre tu máquina local y el host remoto, puedes usar el flujo estándar basado en el navegador mediante un túnel hacia el servidor local de callback de Codex (el valor predeterminado es `localhost:1455`).

1. Desde tu máquina local, inicia el reenvío de puertos:

```shell
ssh -L 1455:localhost:1455 user@remote

2. En esa sesión SSH, ejecuta `codex login` y abre en tu máquina local la dirección que se muestra.

## Proveedores de modelos alternativos

Cuando defines un [proveedor de modelos personalizado](/es-419/codex/config-file/config-advanced#custom-model-providers) en tu archivo de configuración, puedes elegir uno de estos métodos de autenticación:

- **Autenticación de OpenAI**: configura `requires_openai_auth = true` para usar la autenticación de OpenAI. Luego puedes iniciar sesión con ChatGPT o una clave de API. Esto es útil cuando accedes a modelos de OpenAI mediante un servidor proxy de LLM. Cuando `requires_openai_auth = true`, Codex ignora `env_key`.
- **Autenticación mediante variable de entorno**: configura `env_key = "<ENV_VARIABLE_NAME>"` para usar una clave de API específica del proveedor desde la variable de entorno local llamada `<ENV_VARIABLE_NAME>`.
- **Sin autenticación**: si no defines `requires_openai_auth` (o lo defines como `false`) y tampoco defines `env_key`, Codex supone que el proveedor no requiere autenticación. Esto es útil para modelos locales.
