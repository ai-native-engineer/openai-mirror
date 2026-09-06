<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/user-lifecycle -->

Usa esta guía para dar a los empleados el acceso adecuado al espacio de trabajo de ChatGPT cuando
se incorporan, actualizar ese acceso cuando cambian sus responsabilidades y eliminarlo
cuando se van. El proceso también abarca las licencias del espacio de trabajo, los roles asignados por grupo,
los tokens de acceso de Codex y los sistemas conectados con sus propios controles de acceso.

El inicio de sesión único (SSO) verifica la identidad de un empleado. El aprovisionamiento agrega al
empleado a un espacio de trabajo. Ninguna de estas acciones determina por sí sola la licencia del empleado,
sus permisos de funciones, la política de ejecución local ni el acceso a un sistema externo.

Gestiona el acceso de los empleados en tres etapas del ciclo de vida:

- **Incorporación:** aprovisiona el acceso al espacio de trabajo, los grupos, los roles y la licencia correcta.
- **Cambio:** actualiza los grupos del empleado y elimina solo los roles directos obsoletos.
- **Salida:** elimina el acceso al espacio de trabajo, revoca los tokens y revisa los sistemas conectados.

## Verificar los requisitos previos y asignar responsables

Antes de incorporar empleados, identifica quién controla cada parte del ciclo de vida:

| Responsable                     | Responsabilidad                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| Propietario del espacio de trabajo           | Habilitar la sincronización de directorios, asignar roles del espacio de trabajo, aprobar tipos de licencia y revisar el acceso de auditoría |
| Administrador de identidades    | Configurar el proveedor de identidad, las asignaciones de aplicaciones, los grupos de aprovisionamiento y el estado de sincronización        |
| Administrador del espacio de trabajo   | Revisar los miembros del espacio de trabajo, la pertenencia a grupos y las opciones de administración disponibles                     |
| Responsable de seguridad o del servicio | Revisar los tokens de Codex, los sistemas conectados, la automatización compartida y las evidencias de auditoría requeridas                |

Confirma el espacio de trabajo de destino, verifica el dominio de correo electrónico de la organización cuando
sea necesario e identifica a un propietario del espacio de trabajo que pueda habilitar la sincronización
de directorios. Luego, comprueba qué controles admite el plan del espacio de trabajo:

| Capacidad                                 | Planes de espacio de trabajo compatibles                                                                                    |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Sincronización de directorios mediante SCIM     | ChatGPT Enterprise, Edu y Healthcare                                                                      |
| Roles personalizados y control de acceso basado en roles | ChatGPT Enterprise, Edu, Healthcare y Teachers                                                            |
| Tokens de acceso de Codex                        | ChatGPT Business y Enterprise                                                                              |
| Licencias solo de Codex                           | Espacios de trabajo Enterprise elegibles y espacios de trabajo Business existentes que cumplan los requisitos; no disponibles para Edu, Teachers ni Healthcare |

SCIM es la sigla de System for Cross-domain Identity Management. Un espacio de trabajo Business
puede admitir tokens de acceso de Codex sin SCIM, mientras que un espacio de trabajo Edu
puede admitir SCIM sin tokens de acceso de Codex ni licencias solo de Codex. Aplica únicamente
los controles disponibles para tu espacio de trabajo.

Un espacio de trabajo Business puede conservar y agregar licencias solo de Codex únicamente si tenía una licencia de Codex
antes del 24 de junio de 2026 o si, a esa fecha, tenía una invitación pendiente para una licencia de Codex
que cumpliera los requisitos. Los espacios de trabajo Business nuevos y los que no tengan una licencia o
invitación que cumpla los requisitos no pueden agregar su primera licencia solo de Codex. Consulta
[Gestionar el ciclo de vida y la migración de espacios de trabajo en ChatGPT Business](https://help.openai.com/en/articles/8801890-managing-workspace-lifecycle-and-migration-in-chatgpt-business).

Si el espacio de trabajo admite más de un tipo de licencia, revisa el tipo predeterminado en
**Configuración del espacio de trabajo \> Identidad y acceso** antes de habilitar el aprovisionamiento
automatizado. Los usuarios aprovisionados mediante SCIM heredan ese tipo predeterminado, y la licencia determina
qué interfaces del producto están disponibles. Un rol personalizado no puede otorgar un acceso que
la licencia no incluya.

Usa **Permisos y roles** para revisar los controles de acceso local, tokens de acceso,
duración de las credenciales y dispositivos remotos. Algunos espacios de trabajo combinan el acceso
local en **Codex y Work Local**, con el control **Permitir que los miembros usen Codex y
Work localmente** . Otros separan **Codex Local**, con **Permitir que los miembros
usen Codex localmente**, de **Work Local**, con **Usar Work localmente**.
Los controles separados de Codex y Work no otorgan acceso al otro producto. Los controles
de tokens aparecen en la sección de acceso local o en una sección independiente de **Tokens de
acceso** . Estas opciones son independientes de la pertenencia a grupos y
de los tipos de licencia asignados.

El siguiente ejemplo muestra los controles combinados de **Codex y Work Local** y una
sección independiente de **Tokens de acceso** :

  

Para conocer los requisitos previos actuales y los esquemas de identidad compatibles, consulta
[Identidad y aprovisionamiento](https://help.openai.com/en/articles/9672121)
y [Gestionar miembros, tipos de licencia, roles y acceso](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise).

## Elegir cómo se incorporan los empleados al espacio de trabajo

Elige un método principal de aprovisionamiento para cada conjunto de usuarios:

| Método                     | Cómo se obtiene el acceso                                                       | Dónde eliminar el acceso                                  |
| -------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------- |
| Invitación manual          | Un propietario o administrador del espacio de trabajo invita a un empleado                          | Administración de miembros del espacio de trabajo                         |
| Creación automática de cuentas | Un empleado con un dominio de correo electrónico elegible inicia sesión                      | Administración del espacio de trabajo y el flujo de identidad correspondiente |
| Sincronización de directorios con SCIM   | Un administrador de identidades asigna al empleado en el proveedor de identidad | La aplicación o el grupo de aprovisionamiento del proveedor de identidad |

Usa invitaciones manuales para una prueba piloto pequeña o un grupo que no se gestione mediante
sincronización de directorios. Usa SCIM cuando la pertenencia al espacio de trabajo deba reflejar
lo que indique el proveedor de identidad a medida que los empleados se incorporan, cambian de equipo o se van.

No habilites la creación automática de cuentas y SCIM al mismo tiempo. Es posible que los usuarios agregados mediante
la creación automática de cuentas no estén gestionados por SCIM, por lo que eliminarlos de
un grupo del proveedor de identidad podría no eliminar su acceso al espacio de trabajo. Consulta las
[Preguntas frecuentes sobre la integración con SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
para obtener orientación actualizada.

SCIM puede conectar un único espacio de trabajo de ChatGPT o el inquilino de una organización,
según la configuración de identidad aprobada. Mantén explícita cada asignación de espacio de trabajo
y producto. Una conexión de directorio compartida no otorga ni elimina automáticamente
el acceso en todos los espacios de trabajo u organizaciones de la Plataforma API.

## Conectar un grupo de aprovisionamiento al espacio de trabajo correcto

Configura la conexión antes de agregar al primer empleado de la prueba piloto. El propietario del espacio
de trabajo y el administrador de identidades tienen responsabilidades distintas:

1. Pide al propietario del espacio de trabajo que seleccione el espacio de trabajo de ChatGPT previsto y revise
**Configuración del espacio de trabajo \> Grupos**. Registra los nombres de los grupos existentes, sus miembros,
   las asignaciones de roles personalizados y los accesos compartidos pertinentes a proyectos o GPT.
2. Pide al administrador de identidades que identifique el grupo exacto del proveedor de identidad
que se va a sincronizar. Compara su nombre y sus miembros con los de cada
grupo existente en el espacio de trabajo.
3. Si un grupo sincronizado tiene el mismo nombre que un grupo existente en el espacio de trabajo,
resuelve las diferencias del grupo en conflicto o cámbiale el nombre antes de habilitar la sincronización.
Pide al propietario del espacio de trabajo que apruebe los miembros, los roles heredados y los
accesos compartidos resultantes. Un grupo existente con el mismo nombre pasa a ser gestionado por SCIM,
y el proveedor de identidad pasa a controlar sus miembros.
4. Selecciona un grupo piloto de alcance limitado y registra el espacio de trabajo aprobado,
los empleados previstos y las asignaciones de roles a grupos.
5. Pide al propietario del espacio de trabajo que abra **Configuración del espacio de trabajo \> Identidad y acceso**
   y seleccione **Habilitar la sincronización de directorios**. Si se le solicita, debe elegir **Usar SCIM solo
   para este espacio de trabajo** para el aprovisionamiento a nivel del espacio de trabajo, o **Mantener la opción
   de ampliar a otros productos** para el aprovisionamiento aprobado a nivel de inquilino. Si
   SCIM ya está activo a nivel de inquilino, gestiona esa conexión existente
   en lugar de crear una segunda conexión para el espacio de trabajo.
6. Pide al administrador de identidades que complete la conexión con el proveedor de identidad,
seleccione la aplicación de ChatGPT y asigne el grupo aprobado para aprovisionar
miembros en el espacio de trabajo previsto.
7. En **Configuración del espacio de trabajo \> Grupos**, confirma que el grupo seleccionado muestre
   su insignia de SCIM. Verifica el nombre del grupo, los miembros sincronizados y el espacio de trabajo
   de destino antes de usarlo para otorgar acceso.
8. Pide al propietario del espacio de trabajo que abra **Permisos y roles \> Roles personalizados**,
   cree o seleccione el rol aprobado y lo asigne al grupo sincronizado.
   La configuración de roles está disponible en la web y requiere acceso de propietario
   del espacio de trabajo.
9. Revisa los permisos efectivos del grupo y el tipo de licencia predeterminado del espacio de trabajo
antes de agregar a un empleado representativo para la prueba piloto.

El administrador del proveedor de identidad controla la asignación a aplicaciones y la pertenencia a grupos;
el propietario del espacio de trabajo controla la sincronización de directorios y la asignación de roles
del espacio de trabajo. Consulta las [Preguntas frecuentes sobre la integración con SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
y [Configurar el control de acceso basado en roles](https://help.openai.com/en/articles/11750701-rbac)
para conocer los pasos y la disponibilidad actuales de cada proveedor.

## Aprovisionar el acceso de un empleado nuevo

Para un empleado administrado mediante SCIM:

1. Confirma el espacio de trabajo previsto, la dirección de correo electrónico verificada, el tipo de licencia predeterminado
y el grupo del proveedor de identidad.
2. Asigna al empleado a la aplicación de ChatGPT o al grupo que otorga acceso en
el proveedor de identidad.
3. Espera a que se complete la sincronización de directorios. Revisa el estado actual
del proveedor de identidad si el empleado no aparece.
4. En **Configuración del espacio de trabajo \> Miembros**, verifica el correo electrónico del empleado,
   su pertenencia al espacio de trabajo o invitación pendiente, el tipo de licencia y la insignia de SCIM.
5. En **Configuración del espacio de trabajo \> Grupos**, confirma que el empleado pertenezca al
   grupo sincronizado previsto. Pide al propietario del espacio de trabajo que verifique el rol personalizado
   asignado a ese grupo.
6. Pide a un empleado representativo que inicie sesión en el espacio de trabajo correcto y verifique
las interfaces del producto, las funciones y los sistemas conectados específicos que necesita.
7. Registra al responsable del acceso y la verificación exitosa mediante
el proceso aprobado por tu organización.

Si agregas a un empleado manualmente, envía la invitación desde la administración de miembros del espacio de trabajo
y luego realiza las mismas comprobaciones de licencia, grupo, rol e inicio de sesión.

Un grupo organiza a los miembros, pero no otorga por sí solo acceso a todas las funciones.
Para conocer el procedimiento actual de asignación de roles, consulta
[Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions)
y [Configurar el control de acceso basado en roles](https://help.openai.com/en/articles/11750701-rbac).

## Actualizar el acceso cuando un empleado cambia de equipo

Un empleado que cambia de equipo puede conservar el acceso otorgado por asignaciones anteriores de grupos o roles.
Actualiza el sistema que administra su pertenencia antes de verificar
el nuevo nivel de acceso:

1. Identifica el nuevo equipo del empleado, el espacio de trabajo y la licencia que necesita,
los permisos de funciones aprobados y el grupo de destino.
2. Agrega al empleado al grupo de destino aprobado antes de quitarlo
de su grupo anterior si debe permanecer en el espacio de trabajo durante todo
el cambio. Actualiza la pertenencia administrada mediante SCIM en el proveedor de identidad;
actualiza la pertenencia administrada manualmente desde la administración del espacio de trabajo.
3. Confirma que el rol aprobado ya esté asignado al grupo de destino.
Conserva las asignaciones de roles existentes en los grupos compartidos para que los demás miembros
mantengan su acceso aprobado.
4. Pide a un propietario del espacio de trabajo que modifique la asignación de un rol a un grupo solo después de
aprobar, por separado, un cambio de política para todo el grupo y revisar su efecto en
cada miembro.
5. Pide a un propietario del espacio de trabajo que abra el perfil del empleado, revise **Roles directos**
   y quite los roles obsoletos asignados directamente a esa persona. Los roles personalizados usan **Predeterminado**,
**Activado** y **Desactivado**. Un valor explícito de **Desactivado** en cualquier rol asignado tiene prioridad sobre
**Activado** en otro rol.
6. Revisa los permisos efectivos del empleado en todos los roles asignados directamente y
mediante grupos antes de aprobar el cambio de equipo.
7. Si el espacio de trabajo admite más de un tipo de licencia, pide a un propietario del espacio de trabajo que abra
**Configuración del espacio de trabajo \> Miembros \> Cambiar tipo de licencia** y revise
   el acceso a productos previsto para el empleado.
8. Antes de convertir una licencia de ChatGPT en una licencia exclusiva de Codex, confirma que el
empleado deba perder el acceso a los chats, las memorias, los proyectos y otras
funciones de ChatGPT. Los datos subyacentes no se eliminan y vuelven a estar disponibles
si el empleado vuelve a tener una licencia de ChatGPT.
9. Una vez completadas la sincronización y las actualizaciones de permisos, verifica tanto las
acciones que ahora están permitidas como las que ya no deberían estar disponibles.

Si el empleado es propietario de un flujo de trabajo automatizado, revisa si su token de Codex,
la entrada del administrador de secretos o la autorización del servicio conectado deben transferirse a otro
propietario aprobado. Quitar el permiso de uso local de Codex del empleado suspende
sus tokens de Codex, pero no los revoca. Restablecer el permiso
reactiva esos tokens, así que revoca las credenciales que deban perder el acceso de forma permanente.

## Dar de baja a un empleado saliente

Comienza por el sistema que administra la pertenencia del empleado al espacio de trabajo:

1. Determina si el empleado se administra mediante SCIM o si un administrador lo agregó
manualmente.
2. Para un empleado administrado mediante SCIM, quita su asignación a la aplicación de ChatGPT
y quítalo de todos los grupos de aprovisionamiento que otorgan acceso
en el proveedor de identidad. No elimines los grupos compartidos.
3. Para un empleado que no se administra mediante SCIM, pide a un propietario o
   administrador del espacio de trabajo que quite al miembro desde **Configuración del espacio de trabajo \> Miembros**.
4. Confirma que el miembro ya no esté en el espacio de trabajo previsto.
Para el acceso administrado mediante SCIM, verifica que la sincronización haya finalizado y que ninguna
otra asignación del proveedor de identidad pueda restablecer su pertenencia.
5. Registra la baja completada y asigna a un responsable para revisar los tokens,
los sistemas conectados y los datos conservados.

No confíes únicamente en quitar al empleado desde el espacio de trabajo si el proveedor de identidad aún lo asigna
a un grupo administrado mediante SCIM. Una sincronización posterior puede volver a agregar
al empleado al espacio de trabajo.

### Revocar tokens de acceso de Codex y transferir automatizaciones

Quitar a una persona del espacio de trabajo no sustituye una revisión explícita de las
credenciales que usan las automatizaciones de confianza. Aplica este procedimiento solo cuando el
espacio de trabajo admita y tenga habilitados los tokens de acceso de Codex.

Quitar el permiso de uso local de Codex suspende los tokens existentes, pero no los revoca.
Esos tokens pueden volver a funcionar si un propietario del espacio de trabajo restablece el permiso,
así que revoca explícitamente las credenciales que deban perder el acceso de forma permanente.

La página **Tokens de acceso** identifica al creador y el estado de cada token. Usa
**Revocar** para quitar el acceso a los tokens activos:

  

1. Pide a un propietario o administrador del espacio de trabajo que abra
[Tokens de acceso](https://chatgpt.com/admin/access-tokens).
2. Identifica los tokens creados por el empleado saliente y los flujos de trabajo que usan
esos tokens.
3. Elige la identidad de reemplazo. Para un flujo de trabajo no humano de larga duración con un
   plan de pago por uso elegible, usa una [cuenta de
   servicio](/es-419/codex/enterprise/service-accounts) dedicada y aprobada. De lo contrario, identifica a un
   propietario activo y aprobado para el flujo de trabajo. Pide a un propietario del espacio de trabajo que le otorgue a esa persona
   permiso para crear tokens de acceso si es necesario y confirma que tenga
   permiso de uso local de Codex.
4. Crea el token de reemplazo. Un operador autorizado de la cuenta de servicio puede
   crear un token desde la página de detalles de esa cuenta. Para reemplazarlo por un token
   personal, pide al nuevo propietario del flujo de trabajo que cree un token para su propia
   identidad del espacio de trabajo de ChatGPT. Si el cuadro de diálogo muestra **Ámbitos**, selecciona
**Codex**. Selecciona otros ámbitos solo cuando el flujo de trabajo los requiera. Un
   cuadro de diálogo sin **Ámbitos** crea un token exclusivo de Codex. Un administrador no puede
   crear un token personal en nombre de otro usuario.
5. Actualiza el secreto almacenado del flujo de trabajo y luego verifica que el flujo se ejecute correctamente
con el token de reemplazo.
6. Pide al propietario o administrador del espacio de trabajo que revoque los tokens del empleado saliente
y todas las credenciales reemplazadas.
7. Confirma que los tokens revocados ya no puedan iniciar nuevas ejecuciones autenticadas.

Cuando un propietario de reemplazo aprobado cree un token, usa un nombre descriptivo del flujo de trabajo
y elige el período de vigencia más corto para la credencial que permita la política
de tu organización. Si aparece **Ámbitos** , selecciona **Codex** y evita los permisos que el
flujo de trabajo no requiera. El siguiente ejemplo muestra la interfaz con ámbitos:

  

Los propietarios y administradores del espacio de trabajo pueden revocar cualquier token de su espacio de trabajo. Un miembro
con permiso para usar tokens de acceso solo puede revocar los tokens que haya creado. Para conocer los permisos
actuales de los tokens y los pasos para rotarlos, consulta
[Tokens de acceso](/es-419/codex/enterprise/access-tokens#rotate-or-revoke-a-token).

### Revisar los sistemas conectados y los datos conservados

El aprovisionamiento del espacio de trabajo no administra todos los límites de autorización. Pide al
responsable del servicio correspondiente que revise el acceso a:

- Repositorios de código fuente y cuentas de GitHub conectadas.
- Google Drive, Slack y otras aplicaciones conectadas.
- Complementos instalados, habilidades incluidas y capacidades disponibles mediante conectores.
- Entornos alojados de Codex, automatizaciones compartidas y secretos almacenados.
- Dispositivos administrados, credenciales almacenadas localmente y sesiones remotas compatibles.
- Organizaciones, proyectos y claves de API independientes en la Plataforma API.

Aplica los controles propios de cada sistema en lugar de suponer que un cambio en un grupo del espacio de trabajo
o en SCIM actualiza los permisos en todas partes. Consulta
[Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions)
para conocer el modelo completo de límites y [Controles de complementos](/es-419/codex/enterprise/apps-and-connectors)
para conocer la disponibilidad de los complementos, las habilidades incluidas y los permisos de las aplicaciones conectadas.

Quitar el acceso al espacio de trabajo no es lo mismo que eliminar contenido. Cuando un miembro
se va, el espacio de trabajo reasigna automáticamente la propiedad de sus proyectos y GPT
personalizados a un propietario del espacio de trabajo. Esos elementos no se marcan para su eliminación.
Si el miembro vuelve a unirse, recupera la propiedad.

En los espacios de trabajo Enterprise y Edu, los chats, archivos y documentos de canvas siguen
la política de retención configurada para el espacio de trabajo. Los espacios de trabajo Business conservan los chats,
archivos y documentos de canvas de forma indefinida. Los espacios de trabajo Healthcare también ofrecen
controles de retención de datos; revisa la configuración correspondiente del espacio de trabajo y
[la guía de ChatGPT para el sector salud](https://help.openai.com/en/articles/20001046-chatgpt-for-healthcare).

Reasignar un proyecto o GPT no transfiere las conversaciones ni los archivos privados
del antiguo miembro, y el cambio de propietario no le permite al propietario del espacio de trabajo
ver ese contenido privado. Consulta
[Baja de miembros del espacio de trabajo y retención de datos](https://help.openai.com/en/articles/8266418)
para conocer el comportamiento actual de cada plan.

Si se necesita evidencia del cambio por motivos de seguridad o cumplimiento, registra el
espacio de trabajo afectado, el empleado, la asignación en el proveedor de identidad, la hora de finalización,
el responsable de la aprobación y la verificación de la revocación de tokens en el sistema aprobado.
Confirma los registros disponibles, los permisos de administrador y la retención en la
[Referencia de la API de administración](https://chatgpt.com/admin/api-reference), que requiere autenticación.
Los ámbitos sensibles de cumplimiento pueden requerir la intervención de un propietario del espacio de trabajo. Para obtener una descripción general
del producto, consulta [API de Cumplimiento y eventos de auditoría](/es-419/codex/enterprise/compliance-api).
No deduzcas a partir de esta guía qué eventos se cubren, qué campos están disponibles ni cuáles son los períodos de retención.

## Solucionar problemas por falta de acceso o acceso inesperado

| Síntoma                                               | Qué revisar                                                                             | Acción correctiva                                                                                                       |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Un empleado puede iniciar sesión, pero no encuentra el espacio de trabajo  | El espacio de trabajo de destino, la invitación, la asignación en el proveedor de identidad y la dirección de correo electrónico         | Corrige la asignación o el mapeo del correo electrónico y luego verifica la pertenencia al espacio de trabajo                                               |
| Un empleado sincronizado recibe una licencia incorrecta       | El tipo de licencia predeterminado del espacio de trabajo y el registro actual del miembro                     | Pide a un propietario del espacio de trabajo que revise el tipo de licencia predeterminado y las opciones de licencia disponibles para el empleado                                     |
| Un cambio de equipo no elimina el acceso a una función                | La pertenencia a otros grupos, los **Roles directos** y los permisos combinados del empleado        | Elimina al empleado de los grupos a los que ya no deba pertenecer y luego pide a un propietario del espacio de trabajo que revoque solo los roles directos de ese empleado que ya no correspondan |
| Un grupo manual pasa a administrarse mediante SCIM sin aprobación  | Los nombres de grupo coincidentes, los miembros en el proveedor de identidad, los roles heredados y la configuración de uso compartido existente    | Ajusta la pertenencia a los grupos en el proveedor de identidad según lo aprobado y revisa el acceso afectado                                 |
| Otros empleados pierden el acceso después de un cambio de equipo       | Los cambios recientes en las asignaciones de roles a grupos compartidos y el acceso aprobado del equipo anterior     | Pide a un propietario del espacio de trabajo que restablezca el rol aprobado del grupo compartido y luego actualiza solo la pertenencia a grupos del empleado que cambia de equipo        |
| Un token de automatización deja de funcionar después de un cambio de equipo | El permiso de acceso local a Codex del responsable del flujo de trabajo y el estado actual del token                      | Pide a un propietario del espacio de trabajo que restablezca el acceso local aprobado a Codex, o rota y revoca el token afectado                     |
| Un cambio de acceso no se refleja de inmediato           | El estado de sincronización del proveedor de identidad, el plazo de sincronización previsto y las actualizaciones recientes de roles          | Pide al administrador de identidad que verifique la sincronización antes de contactar al soporte de OpenAI                                        |
| Un empleado eliminado vuelve al espacio de trabajo           | La asignación a la aplicación en el proveedor de identidad y todos los grupos de aprovisionamiento que otorgan acceso | Elimina al empleado en el proveedor de identidad en lugar de hacerlo solo en la configuración del espacio de trabajo                                      |
| Un empleado que deja la organización aún tiene un token en la lista         | El creador del token, el responsable del flujo de trabajo y los permisos sobre tokens del administrador del espacio de trabajo        | Rota las credenciales necesarias para la automatización y luego revoca el token del empleado que deja la organización                                   |
| Una aplicación conectada sigue permitiendo el acceso           | La cuenta en el sistema de origen, la disponibilidad del complemento y la autorización de la aplicación                   | Pide al responsable del servicio correspondiente que elimine el acceso con los controles admitidos por ese sistema                                  |

La mayoría de los proveedores de identidad se sincronizan cada 30 a 40 minutos, aunque algunos
aplican las actualizaciones de inmediato. Los cambios en los roles personalizados pueden tardar unos cinco minutos en
reflejarse. No puedes forzar una sincronización de SCIM, así que no elimines y vuelvas a crear
un miembro del espacio de trabajo para solucionar el retraso de una actualización.

Si la eliminación de acceso o la actualización de un grupo aún no se ha completado tras el plazo previsto
para ese proveedor, pide al administrador de identidad que recopile:

- El espacio de trabajo afectado y la dirección de correo electrónico del empleado.
- El proveedor de identidad, la asignación a la aplicación y el grupo de aprovisionamiento.
- El cambio que se intentó realizar, su marca de tiempo y el estado de sincronización más reciente.
- Los roles directos, los roles de grupo o los tokens que aún necesitan revisión.

Contacta al [soporte de OpenAI](https://help.openai.com/) con esos datos a través
del Centro de ayuda. Trata el caso de un exempleado que conserva el acceso como una excepción de
seguridad y sigue el proceso de escalamiento de incidentes de tu organización.

Para conocer la configuración y el comportamiento de sincronización específicos de cada proveedor, consulta las
[Preguntas frecuentes sobre la integración de SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq) actualizadas.
Para los errores de inicio de sesión e identidad, consulta
[Solución de problemas de autenticación](https://help.openai.com/en/articles/10489721-login-and-authentication-faq-s-and-troubleshooting-sso-scim-and-domain-verification).

## Verificar el ciclo de vida completo del empleado

Usa un empleado de prueba representativo para verificar las tres transiciones antes de una
implementación más amplia:

| Etapa del ciclo de vida | Responsable principal                 | Resultado satisfactorio                                                                                                            |
| --------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Incorporación          | Administrador de identidad        | El empleado se incorpora al espacio de trabajo correcto con la licencia, el grupo y el acceso a funciones previstos                                    |
| Cambio de equipo           | Responsables de identidad y propietarios del espacio de trabajo | Los administradores actualizan la pertenencia a grupos y los propietarios del espacio de trabajo eliminan los roles directos que ya no correspondan, conservando los roles de los grupos compartidos |
| Salida          | Responsables de identidad y seguridad  | Los administradores eliminan el acceso al espacio de trabajo, revisan los tokens admitidos y revocan o reasignan el acceso externo                       |

Registra quién aprobó cada cambio, qué verificaste y quién es
responsable de resolver las excepciones de acceso pendientes. Programa revisiones periódicas
del acceso según las políticas de identidad y seguridad de tu organización.

## Documentación relacionada

- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
- [Grupos y aprovisionamiento](/es-419/codex/enterprise/groups-and-provisioning)
- [Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions)
- [Controles de complementos](/es-419/codex/enterprise/apps-and-connectors)
- [Tokens de acceso](/es-419/codex/enterprise/access-tokens)
- [Cuentas de servicio](/es-419/codex/enterprise/service-accounts)
- [Autenticación](/es-419/codex/auth)
- [Configuración administrada](/es-419/codex/enterprise/managed-configuration)
- [API de Cumplimiento y eventos de auditoría](/es-419/codex/enterprise/compliance-api)
