<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/service-accounts -->

Las cuentas de servicio te permiten ejecutar y escalar flujos de trabajo de Codex sin interfaz gráfica en toda tu organización sin depender de la cuenta de un empleado. Cada ejecutor de integración continua (CI), tarea programada o integración compartida obtiene su propia identidad en el espacio de trabajo de ChatGPT, con los mismos grupos, roles, controles de acceso y capacidad de auditoría que esperarías para las personas.

Solo los propietarios y administradores del espacio de trabajo pueden crear cuentas de servicio. Pueden permitir que otras personas o grupos administren una cuenta, configuren complementos o creen tokens de acceso.

Las cuentas de servicio solo están disponibles en los planes de pago por uso.

Una cuenta de servicio representa una identidad no humana del espacio de trabajo. Un [token de acceso personal](/es-419/codex/enterprise/access-tokens) representa al miembro del espacio de trabajo que lo crea. Las cuentas de servicio de proyectos de la Plataforma API y las claves de API usan un acceso a proyectos y una facturación independientes.

## Crear y configurar una cuenta de servicio

Este recorrido interactivo usa GitHub como ejemplo: crea una cuenta, configura un complemento, crea un token y asigna grupos y roles.

1. Abre [Cuentas de servicio](https://chatgpt.com/admin/service-accounts) en la configuración de tu espacio de trabajo.
2. Selecciona el botón con el signo más (**+**) e ingresa un nombre descriptivo, como `release-automation`.
3. Selecciona **Crear**.

## Conectar un complemento

Configura los complementos de la propia cuenta de servicio. Esta no hereda los complementos ni las apps conectadas de la persona que la creó.

1. Abre la sección **Complementos** de la cuenta y selecciona **Agregar complemento**.
2. Elige un complemento y comprueba que aparezca como configurado o habilitado.

Los roles **Configurar** y **Administrador** permiten configurar complementos. El rol **Usuario** no lo permite.

## Crear un token de acceso

Crea un token desde la página de detalles de la cuenta de servicio. El token representa a la cuenta de servicio, no a la persona que lo crea.

1. Abre la cuenta y selecciona **Crear token** en **Tokens de acceso**.
2. Asigna un nombre al token, confirma el alcance **Codex** y elige una opción de vencimiento.
3. Selecciona **Crear** y guarda el token en tu gestor de secretos.

El token completo se muestra una sola vez. Las políticas del espacio de trabajo determinan qué opciones de vencimiento están disponibles.

## Asignar roles y grupos

Una cuenta de servicio puede recibir roles del espacio de trabajo y unirse a grupos igual que un miembro humano del espacio de trabajo. Asígnale acceso directamente; no hereda los permisos de la persona que la creó.

Para permitir que personas o grupos administren la cuenta, selecciona **Compartir**, luego **Agregar personas o grupos** y asigna un rol:

| Rol en la cuenta compartida | Configurar la cuenta y sus complementos | Crear tokens de acceso para la cuenta de servicio |
| ------------------- | ------------------------------------- | ------------------------------------ |
| **Usuario**            | No                                    | Sí                                  |
| **Configurar**       | Sí                                   | No                                   |
| **Administrador**         | Sí                                   | Sí                                  |

Estos roles se aplican a quienes administran la cuenta. Son independientes de los roles del espacio de trabajo y los grupos asignados a la cuenta de servicio.

Los roles **Configurar** y **Administrador** permiten habilitar o deshabilitar la cuenta. Solo los propietarios y administradores del espacio de trabajo pueden crear, eliminar o compartir cuentas. Los operadores administran las cuentas compartidas mientras tienen iniciada la sesión en sus propias cuentas de ChatGPT.

Para obtener más información sobre los permisos del espacio de trabajo, consulta [Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions).

## Ejecutar Codex sin iniciar sesión

Los tokens de acceso de cuentas de servicio requieren la versión `0.142.0` o posterior de Codex CLI. Configura `CODEX_ACCESS_TOKEN` y ejecuta Codex sin abrir un navegador:

```bash

codex exec --json "Inspect this repository and summarize its current state."

En CI, proporciona el token mediante un gestor de secretos o un secreto del runner.

Para guardar un inicio de sesión en una máquina de confianza, pasa el token a través de la entrada estándar:

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "Summarize the changes in the current branch."

Esto guarda la credencial de forma local. En runners compartidos o temporales, usa `CODEX_ACCESS_TOKEN` sin guardar un inicio de sesión.

## Aprovisionar cuentas de servicio con SCIM

Si tu espacio de trabajo admite el aprovisionamiento de cuentas de servicio mediante el protocolo System for Cross-domain Identity Management (SCIM), configura `userType` con el valor `ServiceAccount` en tu proveedor de identidad:

```json
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "userName": "svc-codex-release@company.example",
  "displayName": "Codex release automation",
  "active": true,
  "userType": "ServiceAccount"
}

Asigna la identidad al espacio de trabajo y a los grupos necesarios, y luego sincronízala. El proveedor de identidad administra el nombre de la cuenta, su pertenencia a grupos y su ciclo de vida. Las cuentas administradas mediante SCIM no se pueden renombrar ni eliminar en ChatGPT. Consulta [Grupos y aprovisionamiento](/es-419/codex/enterprise/groups-and-provisioning).

## Administrar cuentas de servicio con la Admin API

Si tu espacio de trabajo tiene acceso, usa una clave de la Admin API de ChatGPT para administrar cuentas, tokens y el uso compartido. Las operaciones de lectura requieren `chatgpt.enterprise.service_account.read`; los cambios requieren `chatgpt.enterprise.service_account.write`. Un token de cuenta de servicio no puede autenticar solicitudes a la Admin API.

Consulta la [referencia de la Admin API](https://chatgpt.com/public/admin/api-reference) para conocer las operaciones disponibles y las rutas de solicitud actuales.

### Cuentas

| Operación                    | Método   | Qué hace                               |
| ---------------------------- | -------- | ------------------------------------------ |
| Listar cuentas                | `GET`    | Devuelve las cuentas de servicio del espacio de trabajo         |
| Crear una cuenta            | `POST`   | Crea una cuenta de servicio con nombre            |
| Obtener una cuenta               | `GET`    | Devuelve una cuenta de servicio                |
| Habilitar o deshabilitar una cuenta | `PATCH`  | Actualiza el valor `enabled` de la cuenta      |
| Eliminar una cuenta            | `DELETE` | Elimina la cuenta y revoca sus tokens |

Crea cuentas con `POST /v1/manage/workspaces/{workspace_id}/service-accounts`. Las actualizaciones de la cuenta solo modifican `enabled`.

### Tokens

| Operación      | Método   | Qué hace                         |
| -------------- | -------- | ------------------------------------ |
| Listar tokens    | `GET`    | Devuelve los metadatos de los tokens de la cuenta |
| Crear un token | `POST`   | Crea un token de acceso con un alcance definido        |
| Revocar un token | `DELETE` | Revoca un token de forma permanente        |

Por ejemplo, crea un token de Codex que vence después de 30 días:

```json
{
  "name": "production-release-runner",
  "ttl": 2592000,
  "scopes": ["chatgpt.workspace.feature.allow-codex-local-access.access"]
}

`ttl` es la duración del token en segundos. Una duración limitada debe ser inferior a un año y respetar la política de vencimiento de tu espacio de trabajo. El `access_token` completo solo se devuelve cuando se crea el token.

La Admin API también permite listar, agregar, actualizar y eliminar accesos a cuentas compartidas. Sus valores de rol son `manager`, `configurer` y `user`; `configurer` aparece como **Configurar** en ChatGPT.

## Proteger y administrar cuentas de servicio

- Concede solo los roles, grupos, complementos y conexiones que necesita el flujo de trabajo.
- Guarda los tokens en un administrador de secretos y usa ejecutores confiables.
- Mantén las credenciales fuera de los registros, los mensajes de chat y el control de versiones.
- Establece fechas de vencimiento definidas y revisa periódicamente el acceso y la actividad de la cuenta.
- Para rotar un token, crea uno de reemplazo, actualiza el flujo de trabajo, verifica el acceso y revoca el token anterior desde el espacio de trabajo o la Admin API.
- Revoca inmediatamente los tokens expuestos e investiga la actividad reciente de la cuenta.
- Deshabilita o elimina las cuentas que no se usen desde el espacio de trabajo o la Admin API. Ambas acciones revocan todos los tokens activos. Las cuentas deshabilitadas se pueden volver a habilitar con tokens nuevos; la eliminación no se puede deshacer.

Las ejecuciones se atribuyen a la cuenta de servicio. La analítica del espacio de trabajo y los registros de auditoría disponibles también pueden identificar quién creó tokens o cambió la configuración de la cuenta. Confirma la cobertura de eventos en la [referencia de la Admin API](https://chatgpt.com/public/admin/api-reference).

## Documentación relacionada

- [Autenticación](/es-419/codex/auth)
- [Tokens de acceso personal](/es-419/codex/enterprise/access-tokens)
- [Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions)
- [Grupos y aprovisionamiento](/es-419/codex/enterprise/groups-and-provisioning)
- [Gobernanza](/es-419/codex/enterprise/governance)
- [API de Cumplimiento y eventos de auditoría](/es-419/codex/enterprise/compliance-api)
- [Modo no interactivo](/es-419/codex/non-interactive-mode)
