<!-- source: https://learn.chatgpt.com/es-419/docs/config-file/environment-variables -->

Codex usa `config.toml` para la configuración persistente. Usa variables de entorno para
sobrescribir ajustes en el shell, definir secretos de automatización, configurar el comportamiento del instalador o realizar diagnósticos.

Esta página enumera las variables de entorno públicas y estables que Codex lee directamente.
No incluye variables internas de desarrollo, variables de prueba ni
nombres de secretos específicos de un proveedor que elijas con
[`env_key`](/es-419/codex/config-file/config-advanced#custom-model-providers).

## Ubicaciones principales

| Variable            | Usada por                                    | Valor predeterminado      | Descripción                                                                                                                                                      |
| ------------------- | ------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_HOME`        | CLI, extensión para IDE, app-server e instaladores | `~/.codex`   | Establece el directorio raíz del estado de Codex, que incluye la configuración, la autenticación, los registros, las sesiones, las habilidades y los metadatos del paquete independiente. Si defines esta variable, el directorio debe existir de antemano. |
| `CODEX_SQLITE_HOME` | Estado de la CLI y de app-server                   | `CODEX_HOME` | Establece dónde se almacena el estado basado en SQLite. La opción de configuración `sqlite_home` tiene prioridad. Las rutas relativas se resuelven a partir del directorio de trabajo actual.           |

Para obtener más información sobre los archivos almacenados en `CODEX_HOME`, consulta
[Ubicaciones de configuración y estado](/es-419/codex/config-file/config-advanced#config-and-state-locations).

## Variables del instalador

Estas variables se aplican a los scripts de instalación independientes que se ofrecen en
`https://chatgpt.com/codex/install.sh` y
`https://chatgpt.com/codex/install.ps1`.

| Variable                | Valor predeterminado                                                                              | Descripción                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_NON_INTERACTIVE` | `false`                                                                              | Establécela en `1`, `true` o `yes` para omitir los prompts del instalador. Los prompts usan la respuesta predeterminada, así que usa esta opción para instalaciones y actualizaciones mediante scripts, no para la configuración inicial. |
| `CODEX_INSTALL_DIR`     | `~/.local/bin` en macOS/Linux; `%LOCALAPPDATA%\Programs\OpenAI\Codex\bin` en Windows | Cambia la ubicación donde se instala el comando visible `codex`. La caché del paquete independiente sigue almacenada en `CODEX_HOME/packages/standalone`.                        |

Para realizar instalaciones desatendidas, establece `CODEX_NON_INTERACTIVE=1` en el shell que ejecuta
el instalador descargado:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh

```powershell
$env:CODEX_NON_INTERACTIVE=1; irm https://chatgpt.com/codex/install.ps1 | iex

## Autenticación y red

| Variable                           | Usada por                                          | Descripción                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_API_KEY`                    | Exec, revisión, SDK de TypeScript y exec-server remoto | Proporciona una clave de API a un proceso no interactivo de Codex. Cuando ejecutes código controlado por el repositorio, establécela directamente en el comando, no para todo el trabajo.             |
| `CODEX_ACCESS_TOKEN`               | CLI, app-server y automatización confiable              | Proporciona un token de acceso de ChatGPT o Codex para automatización confiable. Para conservar el inicio de sesión, canalízalo a `codex login --with-access-token`.             |
| `OPENAI_FEDERATION_RULE_ID`        | Identidad de la carga de trabajo                                | Selecciona la regla de federación configurada para la carga de trabajo.                                                                                        |
| `OPENAI_IDENTITY_TOKEN_FILE`       | Identidad de la carga de trabajo                                | Apunta a la ruta absoluta del archivo que contiene el token OIDC actual o el SPIFFE JWT-SVID.                                                |
| `OPENAI_WORKLOAD_IDENTITY_CONTEXT` | Identidad de la carga de trabajo                                | Opcionalmente, proporciona identificadores JSON acotados para la atribución de auditoría informada por el cliente. No afecta la autenticación ni la autorización.         |
| `CODEX_CA_CERTIFICATE`             | Clientes HTTPS, de inicio de sesión y de WebSocket              | Apunta a un paquete de certificados de CA en formato PEM para entornos con interceptación corporativa de TLS o certificados raíz privados. Tiene prioridad sobre `SSL_CERT_FILE`. |
| `SSL_CERT_FILE`                    | Clientes HTTPS, de inicio de sesión y de WebSocket              | Ruta alternativa para el paquete de certificados de CA en formato PEM cuando `CODEX_CA_CERTIFICATE` no está definida.                                                                               |

Para las claves de API del proveedor, establece
[`env_key`](/es-419/codex/config-file/config-advanced#custom-model-providers) en la configuración del proveedor
del modelo. Codex lee la variable cuyo nombre especifica esa configuración, por lo que el nombre de la variable
no es en sí una variable de entorno fija de Codex.

Para administrar secretos de automatización, consulta
[Usar la autenticación con clave de API](/es-419/codex/non-interactive-mode#use-api-key-auth).
Para configurar tokens de acceso, consulta [Tokens de acceso](/es-419/codex/enterprise/access-tokens).
Para configurar la identidad de la carga de trabajo, consulta
[Federación de identidades de cargas de trabajo](/es-419/codex/enterprise/workload-identity).

## Diagnósticos

| Variable   | Usada por            | Descripción                                                                                                             |
| ---------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `RUST_LOG` | CLI y app-server | Controla el filtrado y el nivel de detalle de los registros de Rust. De forma predeterminada, `codex exec` genera una salida con el nivel `error`, a menos que establezcas un valor que muestre más detalles. |

`RUST_LOG` acepta valores como `error`, `warn`, `info`, `debug` y
`trace`. También admite filtros de registro de Rust más específicos, como
`codex_core=debug,codex_tui=debug`.

De forma predeterminada, la CLI interactiva registra los diagnósticos en almacenes locales de capacidad limitada, pero
la generación del archivo de texto sin formato `codex-tui.log` debe habilitarse expresamente. Define `log_dir` de forma explícita cuando
necesites un registro de texto sin formato para solucionar problemas:

```bash
RUST_LOG=debug codex -c log_dir=./.codex-log
tail -F ./.codex-log/codex-tui.log

En el modo no interactivo, `codex exec` muestra los mensajes directamente en lugar de escribirlos
en un archivo de registro de TUI independiente.
