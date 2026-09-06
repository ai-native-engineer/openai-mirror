<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/workload-identity -->

La federación de identidades de cargas de trabajo permite que las automatizaciones de confianza usen Codex sin almacenar un token de acceso personal ni otra credencial de OpenAI de larga duración. Tu carga de trabajo presenta un token de identidad de corta duración de un proveedor que ya administras. OpenAI verifica ese token y devuelve un token de acceso de corta duración para un usuario o una cuenta de servicio de tu espacio de trabajo administrado de ChatGPT.

Usa identidades de cargas de trabajo para procesos de Codex sin supervisión en plataformas en la nube,
Kubernetes, sistemas de CI y otros entornos que puedan emitir tokens OIDC o
JWT-SVID de SPIFFE. Para conocer el modelo de confianza compartido y el flujo independiente de la API de OpenAI,
consulta la [descripción general de las identidades de cargas de trabajo](/api/docs/guides/workload-identity-federation).

  La federación de identidades de cargas de trabajo de Codex está en versión beta y debe habilitarse para tu
  espacio de trabajo. Para solicitar acceso, comunícate con tu representante de OpenAI o con el [Soporte de
  OpenAI](https://help.openai.com/en/articles/6614161-how-can-i-contact-support).

## Antes de comenzar

Necesitas:

- Permiso para administrar identidades de cargas de trabajo en el OpenAI Admin Portal.
- Un espacio de trabajo administrado de ChatGPT.
- Un usuario de ChatGPT o una cuenta de servicio con membresía activa en ese espacio de trabajo, o permiso para crear el usuario o la cuenta durante la configuración.
- Un token OIDC o un JWT-SVID de SPIFFE del que conozcas el emisor, la audiencia y las declaraciones identificativas.
- Un entorno de ejecución que pueda mantener ese token vigente en un archivo protegido ubicado en una ruta absoluta.
- Codex 0.148.0 o una versión posterior.
- Una política de autenticación vigente de Codex que permita la autenticación con ChatGPT
  y el espacio de trabajo seleccionado por la regla de federación. Consulta [Exigir un método de inicio de sesión
  o un espacio de trabajo](/es-419/codex/auth#enforce-a-login-method-or-workspace).

OpenAI no crea una entidad de seguridad ni asigna membresías en un espacio de trabajo durante el intercambio de tokens. Un administrador selecciona o crea la entidad de seguridad antes de que se conecte la carga de trabajo. Crear un usuario humano ocupa un puesto en el espacio de trabajo y está sujeto a las reglas de membresía de ese espacio de trabajo.

En Windows nativo, usa el modo **elevado** del
[Sandbox de Windows](/es-419/codex/windows/windows-sandbox). Otros modos del sandbox de Windows
no pueden proteger el archivo del token de identidad de los comandos controlados por el modelo.

## Obtener un token de identidad

El entorno de ejecución de tu carga de trabajo obtiene y renueva el token de identidad de origen. Codex no invoca servicios de metadatos en la nube ni bibliotecas cliente de proveedores de identidad en tu nombre.

| Entorno de ejecución                          | Origen recomendado del archivo de token                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes, AKS, EKS o GKE     | Monta un token proyectado de una cuenta de servicio y configura Codex para que apunte a ese archivo. La plataforma se encarga de rotarlo.                                  |
| Identidad administrada de Microsoft Entra | Ejecuta un proceso de confianza en el host o un sidecar que solicite un token a Azure IMDS y reemplace el archivo antes de que venza.                |
| Federación saliente de identidades de AWS | Ejecuta un proceso de confianza en el host que invoque `GetWebIdentityToken` en el STS regional y reemplace el archivo antes de que venza.                   |
| Google Cloud                     | Ejecuta un proceso de confianza en el host que solicite un token de identidad al servidor de metadatos y reemplace el archivo antes de que venza.        |
| Oracle Cloud Infrastructure      | Ejecuta un proceso de confianza en el host que use una entidad de seguridad de instancia para solicitar un token de acceso de IDCS y reemplace el archivo antes de que venza. |
| GitHub Actions                   | Solicita el token OIDC del trabajo, escríbelo en un archivo protegido y solicita un token nuevo antes de un intercambio posterior.                    |
| SPIFFE                           | Usa la SPIFFE Workload API o una herramienta auxiliar aprobada para escribir un JWT-SVID vigente en el archivo.                                      |
| Proveedor OIDC personalizado             | Usa el flujo de cargas de trabajo del emisor para obtener un JWT y actualiza el archivo protegido antes de que venza el JWT.                            |

Sigue la guía de tu proveedor para configurar la emisión de tokens e inspeccionar un token de ejemplo:

- [Microsoft Azure](/api/docs/guides/workload-identity-federation/microsoft-azure)
- [AWS](/api/docs/guides/workload-identity-federation/aws)
- [Google Cloud](/api/docs/guides/workload-identity-federation/google-cloud)
- [Oracle Cloud Infrastructure](/api/docs/guides/workload-identity-federation/oracle-cloud)
- [GitHub Actions](/api/docs/guides/workload-identity-federation/github-actions)
- [Kubernetes](/api/docs/guides/workload-identity-federation/kubernetes)
- [SPIFFE](/api/docs/guides/workload-identity-federation/spiffe)

Decodifica un token de ejemplo de forma local y registra sus valores `iss`, `aud`, `sub` y cualquier otra
declaración en la que tengas previsto confiar. La decodificación no verifica la firma. No pegues un
token de producción en un sitio web ni lo escribas en los registros.

## Conectar la carga de trabajo

Un administrador crea el proveedor y la regla de federación antes de iniciar Codex.

1. Abre [Identidad de carga de trabajo](https://admin.openai.com/workload-identity) en el
   OpenAI Admin Portal y selecciona **Conectar carga de trabajo**.
2. Reutiliza un proveedor configurado para Codex o crea uno. Las configuraciones preestablecidas de proveedores completan los ajustes comunes para GitHub Actions, Microsoft Entra ID, Google Cloud, AWS, Kubernetes, SPIFFE y proveedores OIDC personalizados.
3. Selecciona **Codex** y el espacio de trabajo administrado que puede usar la carga de trabajo.
4. Agrega las condiciones más restrictivas que identifiquen la carga de trabajo. Configura coincidencias por sujeto, declaraciones exactas, una condición CEL o una combinación de estos elementos. Agrega audiencias aceptadas para limitar los tokens que admite la regla. Cada criterio de coincidencia configurado debe cumplirse.
5. Asocia la regla con un solo usuario de ChatGPT o una sola cuenta de servicio existentes, o crea el usuario o la cuenta durante la configuración.
6. Revisa el proveedor, las condiciones, el espacio de trabajo, la entidad de seguridad, los alcances y la vigencia del token
   de acceso. Selecciona **Conectar carga de trabajo** y, luego, **Descargar configuración**.

El archivo descargado contiene el ID no secreto de una regla de federación y la ruta desde la que Codex leerá el token de identidad. No contiene ninguna credencial.

Para automatizar la configuración, usa la [Admin API de identidades
de cargas de trabajo](/api/docs/guides/workload-identity-federation/admin-api). Para conocer el comportamiento
de los criterios de coincidencia y ver ejemplos, consulta la [referencia de reglas
de federación](/api/docs/guides/workload-identity-federation/federation-rules).

## Configurar el proceso de Codex

El proceso que inicia Codex requiere estas dos variables de identidad de carga de trabajo:

```bash

`OPENAI_FEDERATION_RULE_ID` no es un secreto. El archivo del token sí lo es. Usa una ruta
absoluta en un directorio dedicado, como `/var/run/secrets/openai.com`, que sea propiedad
de la cuenta de la carga de trabajo y tenga el modo `0700`. Solo los procesos de confianza en el host deben escribir
allí. Mantén el directorio fuera de los repositorios y de otras rutas disponibles para las
herramientas de Codex. Mantén las credenciales fuera de los registros, del historial del shell y de los artefactos de compilación.

### Agregar atribución de auditoría

Cuando varias instancias del entorno de ejecución comparten una regla de federación, puedes identificar cada instancia
en los eventos de auditoría de emisión de tokens. Configura la variable opcional
`OPENAI_WORKLOAD_IDENTITY_CONTEXT` con un objeto JSON codificado como una
cadena de texto:

```bash

  "instance_id": "runner-42",
  "display_name": "payments-prod",
  "labels": {
    "environment": "production",
    "region": "us-west-2"
  }
}'

El objeto requiere `instance_id`. También puede contener `display_name` y hasta
ocho etiquetas. El objeto codificado puede tener un tamaño máximo de 1024 bytes. `instance_id` y
`display_name` pueden tener hasta 128 caracteres. Las claves de las etiquetas pueden tener hasta 64
caracteres y sus valores, hasta 256 caracteres.

Los identificadores deben comenzar con una letra o un número ASCII. A continuación, los valores pueden incluir
letras, números, `.`, `_`, `:`, `/`, `@` y `-`. Las claves de las etiquetas admiten letras,
números, `.`, `_` y `-`.

OpenAI trata este contexto como una atribución de auditoría informada por el cliente, no como una identidad de carga de trabajo verificada. No afecta la autenticación, la autorización, la coincidencia de reglas, los alcances, los límites de solicitudes, la revocación, los controles de habilitación de funciones ni las métricas. No incluyas credenciales, secretos, datos personales, prompts, resultados del modelo ni ningún otro contenido del cliente.

Cuando el contexto es válido, OpenAI genera un ID de atribución estable cuyo alcance se limita al inquilino,
al proveedor, a la regla de federación y a `instance_id`. Para la atribución, el token de acceso
contiene el ID, pero no el contexto. El evento de auditoría de emisión correcta del token
contiene el ID y el contexto normalizado. Si el contexto supera un límite o
incumple este esquema, el intercambio falla con `invalid_grant`.

Codex lee el contexto cuando se inicia el proceso y no transmite ni el contexto ni el ID de la regla ni la ruta del archivo del token a shells, hooks o servidores MCP controlados por el modelo. Reinicia Codex después de cambiar el contexto.

### Proteger y rotar el archivo del token

En las implementaciones administradas de Linux, macOS y WSL, agrega todo el directorio del token a
[`permissions.filesystem.deny_read`](/es-419/codex/enterprise/managed-configuration#enforce-deny-read-requirements)
en los requisitos administrados:

```toml
[permissions.filesystem]
deny_read = ["/var/run/secrets/openai.com"]

Esto impide que los comandos controlados por el modelo lean el token activo o un reemplazo temporal, mientras que el proceso del host de Codex todavía puede usar el token para el intercambio. En los volúmenes de tokens proyectados, deniega el acceso a todo el montaje del token y a cualquier ruta subyacente o de destino resuelta que esté fuera de él. Los modos de archivo y la limpieza de variables de entorno, por sí solos, no protegen las credenciales de otro proceso que se ejecuta como el mismo usuario. En Windows nativo, usa el sandbox con privilegios elevados descrito anteriormente.

Para las fuentes de tokens que no proyectan un archivo, encarga a un proceso de confianza del host que escriba cada reemplazo dentro de ese directorio protegido y le cambie el nombre para colocarlo en su ubicación definitiva. Un cambio de nombre atómico evita que Codex lea un token incompleto. Por ejemplo, adapta este script de actualización del host al comando de tokens de tu proveedor. Aprovisiona el directorio antes de ejecutar el script:

```bash
set -eu
TOKEN_DIR="/var/run/secrets/openai.com"
TOKEN_FILE="$TOKEN_DIR/identity-token"
umask 077
TOKEN_TEMP="$(mktemp "$TOKEN_DIR/.identity-token.XXXXXX")"
trap 'rm -f -- "$TOKEN_TEMP"' EXIT
trap 'exit 1' HUP INT TERM
your-identity-provider-command > "$TOKEN_TEMP"
test -s "$TOKEN_TEMP"
mv -f -- "$TOKEN_TEMP" "$TOKEN_FILE"

Ejecuta el proceso de actualización fuera de cualquier shell o herramienta que Codex pueda controlar. Mantén
activa la denegación de lectura durante la actualización y la limpieza. Incluso si una detención forzada
deja un archivo temporal, este debe permanecer dentro del directorio con lectura
denegada. No incluyas la configuración de identidad de la carga de trabajo en `config.toml`.

## Verificar la conexión

Carga el entorno descargado e inspecciona el método de autenticación seleccionado:

```bash
. ./workload-identity-idpm_example.env
codex login status

En PowerShell:

```powershell
$env:OPENAI_FEDERATION_RULE_ID = "idpm_..."
$env:OPENAI_IDENTITY_TOKEN_FILE = "C:\run\openai\identity-token"
codex login status

Una comprobación correcta imprime `Logged in using workload identity`. Esto confirma
que Codex intercambió un token mediante la regla de federación configurada. El comando
no imprime el espacio de trabajo, la entidad de seguridad ni la regla correspondientes. Confirma estos valores
en el portal de administración antes de iniciar la carga de trabajo. Si Codex informa otro
método de autenticación, las dos variables WIF obligatorias no llegaron al proceso.

Si el proveedor usa **Evitar la reutilización de aserciones** y la aserción incluye `jti`
como declaración, esta comprobación consume ese `jti`. Escribe una aserción recién emitida con un nuevo
`jti` antes de iniciar otro proceso de Codex.

Ejecuta una solicitud pequeña desde el mismo entorno:

```bash
codex exec "Reply with only: workload identity is working"

Codex intercambia el token de origen y conserva en memoria el token de acceso de OpenAI.
No escribe ninguna de las dos credenciales en `auth.json`, en el llavero del sistema ni en
`config.toml`.

## Mantener el token actualizado

Actualiza el archivo del token de identidad antes de que venza el token de origen. Codex vuelve a leer el archivo cuando necesita otro token de acceso de OpenAI. El token de OpenAI vence cuando ocurra primero una de estas dos situaciones: que venza el token de origen o que se cumpla el período de vigencia de la regla de federación; nunca dura más de una hora.

Cuando un administrador activa la protección contra la reutilización, cada JWT de origen debe tener un
`jti` único. Escribe una aserción recién emitida con un `jti` nuevo antes de cada
intercambio, incluidas las actualizaciones en un proceso de larga duración. Las aserciones sin
`jti` no cuentan con protección contra la reutilización.

Codex comparte una sesión de intercambio en memoria dentro de cada proceso del host. Las solicitudes simultáneas de ese proceso reutilizan un token de acceso de OpenAI válido y comparten una sola actualización cuando vence. Los procesos independientes realizan intercambios separados, por lo que necesitan aserciones que el proveedor les permita usar.

## Prioridad de las credenciales

Las dos variables obligatorias de identidad de la carga de trabajo tienen prioridad sobre cualquier otra fuente de credenciales:

1. Si está presente `OPENAI_FEDERATION_RULE_ID` o
`OPENAI_IDENTITY_TOKEN_FILE`, Codex selecciona la identidad de la carga de trabajo.
2. Si solo está presente una de las variables obligatorias, Codex devuelve un error. No recurre a una clave de API, un token de acceso ni un inicio de sesión almacenado.
3. La variable `OPENAI_WORKLOAD_IDENTITY_CONTEXT`, por sí sola, no selecciona la identidad de la carga de trabajo.
4. Cuando no está presente ninguna de las variables WIF obligatorias, Codex aplica las reglas
   habituales de credenciales para esa interfaz. En las interfaces que permiten la
   autenticación mediante una clave de API, `CODEX_API_KEY` tiene prioridad en `codex exec`,
`codex review`, el SDK de TypeScript y `codex exec-server --remote`. Otras
   interfaces pueden usar `CODEX_ACCESS_TOKEN` o un inicio de sesión almacenado.

La opción `apiKey` de un SDK se convierte en `CODEX_API_KEY`, pero WIF sigue teniendo prioridad
cuando está presente cualquiera de las variables WIF obligatorias. Omite esta opción al usar WIF para
que la carga de trabajo no incluya una credencial de larga duración que no se utiliza.

Para migrar una carga de trabajo existente sin interrupciones, configura WIF mientras su credencial actual siga disponible. Inicia un proceso nuevo con las dos variables WIF obligatorias; WIF tiene prioridad, incluso si la credencial anterior todavía está presente. Una vez que la carga de trabajo funcione correctamente con WIF, elimina la credencial anterior de su entorno de ejecución y de su almacén de secretos y, a continuación, revócala. Antes de revocarla, puedes revertir el cambio si eliminas ambas variables WIF obligatorias e inicias un proceso nuevo.

## Interfaces de Codex compatibles

Configura la identidad de la carga de trabajo en la máquina que aloja el proceso de Codex.

| Interfaz                                         | Compatibilidad y límite del host                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Uso interactivo de `codex`, `resume` y `fork`       | Compatible. Inicia la CLI en el entorno configurado.                                                 |
| `codex exec`, `exec resume` y `codex review` | Compatible. Cualquiera de las variables WIF obligatorias hace que WIF tenga prioridad.                                      |
| SDK de TypeScript                                  | Compatible. El proceso padre proporciona las variables WIF obligatorias y cualquier contexto de atribución opcional. |
| `codex app-server`                              | Compatible. Configura WIF en el host de app-server, no en un cliente remoto.                                |
| `codex exec-server --remote`                    | Compatible con la autenticación en el registro de entornos remotos. Configura WIF en el host de exec-server. |
| Operaciones locales de procesos de exec-server            | No utilizan autenticación WIF. Se ejecutan mediante el protocolo local de exec-server.                         |
| `codex mcp-server`                              | No compatible.                                                                                          |

Los clientes remotos de app-server y exec-server nunca envían el token de identidad de origen a través de sus protocolos.

## Modificar o eliminar el acceso

Los cambios en una regla relacionados con sus sujetos, audiencias, declaraciones, condición CEL, ámbitos o la vigencia del token se aplican a los nuevos intercambios. Un token emitido antes del cambio puede seguir siendo válido hasta que finalice su período de vigencia.

Desactiva un proveedor o una regla para detener el acceso de inmediato. La desactivación bloquea los nuevos intercambios y revoca los tokens de acceso de OpenAI ya emitidos a través de ese recurso. Archivar el recurso tiene el mismo efecto sobre el acceso y no se puede deshacer. Modificar la relación de confianza del proveedor también revoca los tokens emitidos antes de que entre en vigor la nueva relación de confianza.

## Auditar los cambios

La creación, la actualización y el archivado de proveedores y reglas de federación generan eventos
de auditoría. Usa la [guía de la API de Cumplimiento y de los eventos de
auditoría](/es-419/codex/enterprise/compliance-api) para exportar los eventos que tu espacio de trabajo
admite. Correlaciónalos con los registros de emisión de tu proveedor de identidad y no
registres aserciones de origen ni tokens de acceso de OpenAI en ninguno de los dos sistemas.

Cuando el proceso proporciona `OPENAI_WORKLOAD_IDENTITY_CONTEXT`, los eventos de auditoría de emisión
correcta de tokens también contienen el ID de atribución estable y el
contexto normalizado descritos anteriormente.

## Solucionar problemas

| Síntoma                                                               | Comprobación                                                                                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Codex informa que la configuración de identidad de la carga de trabajo está incompleta              | Configura ambas variables obligatorias en el mismo proceso y usa una ruta absoluta para el archivo del token.                               |
| Codex informa que su política de inicio de sesión no permite la identidad de la carga de trabajo | Permite la autenticación de ChatGPT en la política efectiva e incluye el espacio de trabajo de la regla entre los espacios de trabajo permitidos. |
| Codex muestra otra credencial                                      | Carga las dos variables WIF obligatorias en el proceso de Codex; luego, inicia un proceso nuevo y vuelve a ejecutar `codex login status`.  |
| OpenAI rechaza el contexto de la carga de trabajo                                       | Revisa su estructura JSON, tamaño, caracteres permitidos y límites de los campos. Elimina el contenido confidencial o el contenido del cliente.            |
| OpenAI rechaza el token                                              | Compara `iss`, `aud`, el vencimiento, la clave de firma y el período de vigencia de la aserción con la configuración del proveedor.               |
| La regla no coincide                                               | Confirma que el cliente usa el ID de regla previsto y que se superan todas las comprobaciones de sujeto, audiencia, declaración exacta y CEL.  |
| OpenAI rechaza la entidad de seguridad                                          | Confirma que el usuario o la cuenta de servicio estén activos y sean miembros activos del espacio de trabajo seleccionado.                   |
| OpenAI rechaza una aserción repetida                                   | Obtén un nuevo JWT con un nuevo `jti`; no vuelvas a intentar usar la misma aserción protegida contra repeticiones.                                  |
| Un proceso de larga duración deja de realizar renovaciones                               | Confirma que el proceso de renovación del host sigue reemplazando el archivo del token antes de que venza.                                  |

Para obtener información sobre la verificación del proveedor, los límites y CEL, consulta la [referencia de las reglas
de federación](/api/docs/guides/workload-identity-federation/federation-rules).
