<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/access-tokens -->

Los tokens de acceso de Codex son credenciales del espacio de trabajo de ChatGPT cuyo alcance se limita a los permisos de Codex. Autentican flujos de trabajo locales no interactivos de confianza, incluidos Codex CLI y la automatización basada en App Server, con una identidad del espacio de trabajo de ChatGPT. Úsalos cuando un script, una tarea programada o un ejecutor de CI necesite acceso local repetible.

  Actualmente, los tokens de acceso de Codex son compatibles con los espacios de trabajo de ChatGPT Business y
ChatGPT Enterprise.

Crea tokens de acceso personal en [Tokens de acceso](https://chatgpt.com/admin/access-tokens), en la consola de administración de ChatGPT. Cada token pertenece a su creador y al espacio de trabajo de ChatGPT de ese usuario. Los tokens funcionan como identidades de agente para los flujos de trabajo locales programáticos. Para obtener información sobre los tokens creados desde la página de detalles de una identidad no humana dedicada del espacio de trabajo, consulta [Cuentas de servicio](/es-419/codex/enterprise/service-accounts).

  Si una clave de API de la plataforma funciona con tu automatización, sigue usando la autenticación con clave de API. Usa
los tokens de acceso de Codex cuando un flujo de trabajo local de confianza necesite específicamente acceso al espacio de trabajo de ChatGPT,
derechos de acceso administrados por el espacio de trabajo o controles empresariales.

  ¿Necesitas activar un agente publicado del espacio de trabajo de ChatGPT desde tu propio sistema? Ese
  flujo de trabajo requiere acceso a **Agentes del espacio de trabajo** . Un token exclusivo de Codex no puede
  autenticar llamadas para activar agentes del espacio de trabajo. Si el cuadro de diálogo del token ofrece
**Ámbitos**, selecciona **Agentes del espacio de trabajo** para activar un agente y **Codex** para
  automatizar con Codex. Otorga varios ámbitos solo cuando el flujo de trabajo requiera cada
  uno de ellos. Consulta [Autenticarse con tokens de acceso
  de agentes del espacio de trabajo](/workspace-agents/authentication).

## Cómo funcionan los tokens de acceso

Usa un token de acceso cuando Codex CLI o un cliente de App Server necesiten ejecutarse sin que un usuario complete el inicio de sesión en el navegador. El token representa al usuario del espacio de trabajo de ChatGPT que lo creó, por lo que las ejecuciones pueden usar el acceso de ese usuario y figurar en los datos de gobernanza del espacio de trabajo.

El cliente verifica el token cuando comienza una ejecución y la vincula con esa identidad del espacio de trabajo. Trata el token como cualquier otro secreto de automatización: guárdalo en un gestor de secretos, evita que aparezca en los registros y rótalo según la política de tu organización.

Usa tokens de acceso para:

- Tareas de `codex exec` que se ejecutan desde una automatización de confianza.
- Scripts locales que necesitan ejecuciones repetibles y no interactivas de Codex CLI.
- Automatización de confianza basada en App Server.
- Flujos de trabajo empresariales que asocian el uso con un usuario del espacio de trabajo de ChatGPT en lugar de con una clave de API de una organización.

Principales riesgos que debes evitar:

- **Secretos filtrados:** cualquier persona que tenga el token puede iniciar ejecuciones locales mediante Codex CLI o un cliente de App Server con la identidad de quien creó el token. Guarda los tokens en un gestor de secretos, evita que aparezcan en los registros y rótalos según la política de tu organización.
- **Confianza en el ejecutor:** los sistemas de CI públicos, los pull requests provenientes de forks o las máquinas compartidas pueden exponer los tokens a personas ajenas a tu espacio de trabajo. Usa tokens de acceso únicamente en ejecutores de confianza.
- **Identidades compartidas:** reutilizar el token de una persona en equipos no relacionados dificulta identificar a los responsables e interpretar los registros de auditoría. Crea tokens para un responsable específico del flujo de trabajo.
- **Credenciales obsoletas:** los tokens de larga duración pueden seguir activos después de que cambie el flujo de trabajo. Prefiere tokens con vigencia limitada y revoca los que ya no se usen.
- **Ámbito o tipo de credencial incorrecto:** la automatización de Codex requiere acceso a Codex,
  la activación de agentes del espacio de trabajo requiere acceso a Agentes del espacio de trabajo y las llamadas generales a la API de OpenAI
  requieren claves de API de la plataforma. Si aparece **Ámbitos** , otorga solo los
  permisos que requiera el flujo de trabajo.

## Habilitar la creación de tokens de acceso

Usa el permiso de tokens de acceso en la configuración del espacio de trabajo para permitir que los miembros autorizados creen tokens de acceso.

El permiso de tokens de acceso controla la creación de tokens. No otorga acceso a
la aplicación de escritorio de ChatGPT, Codex CLI ni la extensión para IDE, y tampoco cambia el
tipo de licencia de un miembro, su rol integrado en el espacio de trabajo ni su perfil de permisos
del entorno de ejecución local. Los flujos de trabajo de Codex CLI y App Server autenticados con tokens también requieren
que el usuario tenga permiso para usar Codex localmente.

Para conocer la relación entre estos controles, consulta
[Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions).

  
    
  

1. Pídele a un propietario del espacio de trabajo que abra
[Configuración del espacio de trabajo \> Permisos y roles](https://chatgpt.com/admin/permissions).
2. Si aparece la sección **Tokens de acceso** , activa **Permitir que los usuarios creen
   tokens de acceso personal**. Si esa sección no está disponible, activa **Permitir que
   los miembros usen tokens de acceso de Codex** en **Codex y Work Local** o
**Codex Local**.
3. Habilita el permiso local de Codex correspondiente para el responsable del flujo de trabajo:
**permitir que los miembros usen Codex y Work localmente** en **Codex y Work Local**,
   o **Permitir que los miembros usen Codex localmente** en **Codex Local**. Cuando **Work
   Local** tiene su propia sección, **Usar Work localmente** controla Work y no es
   necesario para los tokens de Codex.

Permite crear tokens de acceso solo a personas o responsables de servicios que sepan dónde se almacena el token, para qué automatización se usará y cuál es su calendario de rotación.

Deshabilitar el permiso local de Codex suspende los tokens de Codex activos de los miembros
afectados; no los revoca. Restablecer el acceso local a Codex reactiva esos
tokens. Revoca los tokens cuando su acceso deba terminar de forma permanente.

## Establecer un límite de vencimiento para los tokens de acceso

Un propietario del espacio de trabajo puede establecer el plazo de validez máximo que los miembros pueden elegir
para los tokens de acceso nuevos. Abre
[Configuración del espacio de trabajo \> Permisos y roles](https://chatgpt.com/admin/permissions).
Si aparece la sección **Tokens de acceso** , configura allí el **Límite de vencimiento del token de acceso**.
De lo contrario, busca esa opción en **Codex y Work Local** o
**Codex Local**.

  
    
  

El límite se aplica a los tokens de acceso nuevos. Los tokens existentes conservan su plazo de validez actual.

## Crear un token de acceso

Usa la página Tokens de acceso para asignarle un nombre al token, revisar los ámbitos de producto
disponibles y elegir un plazo de validez adecuado.

1. Ve a [Tokens de acceso](https://chatgpt.com/admin/access-tokens).
2. Selecciona **Crear**.

  
    
  

3. Ingresa un nombre descriptivo, como `release-ci` o `nightly-docs-check`.

  
    
  

4. Si el cuadro de diálogo muestra **Ámbitos**, selecciona **Codex**. Selecciona **Agentes del
   espacio de trabajo** solo si el mismo flujo de trabajo también necesita activar un agente del espacio de trabajo.
   Si el cuadro de diálogo no tiene un selector de ámbitos, crea un token exclusivo de Codex.
5. Elige un plazo de validez limitado, como 7, 30, 60 o 90 días. Los tokens de acceso personal
   con ámbitos definidos deben vencer. Una versión anterior del cuadro de diálogo para tokens exclusivos de Codex
   puede ofrecer **Sin vencimiento**; evita esa opción a menos que tu organización
   la apruebe y rote el token según un calendario definido.
6. Selecciona **Crear**.
7. Copia de inmediato el token de acceso generado. No podrás volver a verlo después de
cerrar el cuadro de diálogo.
8. Guarda el token en tu gestor de secretos o en el almacén de secretos de CI.

El plazo de validez personalizado mínimo es de un día. No puedes usar tokens revocados o vencidos para iniciar nuevas ejecuciones autenticadas.

## Usar un token de acceso con Codex CLI

Si el cuadro de diálogo de creación del token indica una versión requerida de Codex CLI, actualiza la CLI
a esa versión o a una posterior antes de usar el token.

Para una automatización efímera, guarda el token en `CODEX_ACCESS_TOKEN` y ejecuta Codex CLI de forma habitual:

```bash

codex exec --json "review this repository and summarize the top risks"

Para un inicio de sesión local persistente, pasa el token a `codex login --with-access-token` mediante una canalización:

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "summarize the last release diff"

`codex login --with-access-token` almacena una credencial de identidad de agente en el almacenamiento de autenticación de Codex CLI. Si prefieres no conservar las credenciales en la máquina, usa en su lugar la variable de entorno `CODEX_ACCESS_TOKEN`.

`codex app-server` puede usar la misma credencial mediante `CODEX_ACCESS_TOKEN` o
un inicio de sesión creado con `codex login --with-access-token` para autenticar sus
solicitudes a OpenAI. Esa credencial es independiente de la autenticación del transporte
entre el cliente y App Server. Para una conexión WebSocket remota, configura un
token de portador o de capacidad independiente como se describe en
[App Server](/es-419/codex/app-server); no reutilices el token de acceso de Codex como
token de transporte. Consulta
[Variables de entorno de autenticación y red](/es-419/codex/config-file/environment-variables#authentication-and-network).

## Rotar o revocar un token

Rota los tokens de acceso igual que los demás secretos de automatización:

1. Crea un token de reemplazo.
2. Actualiza el secreto en el ejecutor, el programador de tareas o el gestor de secretos.
3. Ejecuta una prueba de humo con el token nuevo.
4. Revoca el token anterior desde [Tokens de acceso](https://chatgpt.com/admin/access-tokens).

Desde la página Tokens de acceso, los propietarios y administradores del espacio de trabajo pueden revocar cualquier token del espacio de trabajo. Los miembros con permiso de tokens de acceso solo pueden revocar los tokens que crearon.

## Modelo de permisos

El permiso de tokens de acceso del espacio de trabajo controla la creación de tokens. Según
cómo esté organizada la interfaz del espacio de trabajo, **Permitir que los miembros usen Codex y Work localmente** en
**Codex y Work Local**, o **Permitir que los miembros usen Codex localmente** en **Codex
Local**, controla el acceso local a Codex. Si **Work Local** tiene su propia sección,
**Usar Work localmente** controla Work y no otorga acceso a Codex. Un miembro
necesita tanto acceso local a Codex como el permiso de tokens de acceso para los flujos de trabajo de Codex
autenticados con tokens. Un miembro puede tener acceso local a Codex sin permiso para
crear tokens de acceso.

| Capacidad                                                    | Propietarios y administradores del espacio de trabajo                      | Miembro con permiso de tokens de acceso           | Miembro sin permiso de tokens de acceso |
| ------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------- | -------------------------------------- |
| Abrir [Tokens de acceso](https://chatgpt.com/admin/access-tokens) | Sí                                              | Sí                                           | No                                     |
| Crear tokens de acceso                                          | Sí, para su propia identidad en el espacio de trabajo de ChatGPT    | Sí, para su propia identidad en el espacio de trabajo de ChatGPT | No                                     |
| Ver la lista de tokens de acceso                                            | Lista del espacio de trabajo, que incluye quién creó cada token | Solo los tokens que creó                      | No                                     |
| Revocar tokens de acceso desde la página Tokens de acceso              | Cualquier token del espacio de trabajo                       | Solo los tokens que creó                      | Sin acceso a la página                         |
| Otorgar o retirar el permiso de tokens de acceso                       | Solo el propietario del espacio de trabajo                             | No                                            | No                                     |
| Administrar otras opciones de configuración del cliente local o de Codex Cloud             | Sí, según los permisos de administración del espacio de trabajo        | No, a menos que un propietario otorgue acceso             | No                                     |

En resumen: los propietarios y administradores del espacio de trabajo gestionan el acceso a nivel del espacio de trabajo.
Los miembros necesitan el permiso de tokens de acceso para crear y administrar sus propios tokens,
pero ese permiso no les otorga derechos de administrador ni acceso a los tokens de otros
miembros.

## Solución de problemas

### La página Tokens de acceso devuelve un error 404 o indica que el acceso está prohibido

Pide a un propietario del espacio de trabajo que confirme que tu rol incluye **Permitir que los usuarios
creen tokens de acceso personal** o **Permitir que los miembros usen tokens de acceso
de Codex**, según la interfaz disponible. Para un flujo de trabajo de Codex
autenticado con tokens, confirma también que esté activa la opción **Permitir que los miembros usen Codex y Work
localmente** o **Permitir que los miembros usen Codex localmente** .

### `codex login --with-access-token` falla

Confirma que copiaste el token de acceso generado, no un token de sesión del navegador
ni una clave de API de la plataforma. Confirma también que el token esté activo, que no haya vencido
y que pertenezca a un usuario con el permiso necesario para usar Codex localmente.

## Documentación relacionada

- [Autenticación](/es-419/codex/auth)
- [Cuentas de servicio](/es-419/codex/enterprise/service-accounts)
- [Modo no interactivo](/es-419/codex/non-interactive-mode)
- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
- [Grupos y aprovisionamiento](/es-419/codex/enterprise/groups-and-provisioning)
- [Gestión del ciclo de vida de los usuarios](/es-419/codex/enterprise/user-lifecycle)
- [Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions)
- [Gobernanza](/es-419/codex/enterprise/governance)
