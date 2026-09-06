<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/roles-and-workspace-permissions -->

Distintas configuraciones abarcan diferentes aspectos de la experiencia de tu organización con
ChatGPT. Dar acceso a alguien en un área no le concede automáticamente acceso en otra.
Usa esta página para ver cómo funcionan en conjunto los seis límites de control y, después,
consulta las guías vinculadas para conocer los pasos de configuración vigentes.

En la configuración del espacio de trabajo, **Codex y Work Local** reúne el acceso local a Codex y Work
en el permiso **Permitir que los miembros usen Codex y Work de forma local**. Otros espacios de trabajo
separan **Codex Local** y **Work Local** en secciones independientes. En esa
disposición, **Permitir que los miembros usen Codex de forma local** concede acceso local a Codex, y
**Usar Work de forma local** concede acceso local a Work. Habilitar uno no concede
acceso al otro. Estas etiquetas identifican permisos del espacio de trabajo, no
productos ni clientes independientes. Los permisos de los tokens y los límites de vigencia de las credenciales aparecen
en la sección **Tokens de acceso** o en la sección de acceso local, según
el espacio de trabajo. La configuración administrada es una capa independiente que restringe
el comportamiento compatible del entorno de ejecución para las capacidades incluidas en esos clientes. Las funciones
y los requisitos aplicables pueden variar según el cliente y la versión.

## Comprender los límites de control

| Límite          | Qué controla                                                                                                                                                                                      | Qué no controla                                                                          | Fuente actual                                                                                                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Espacio de trabajo de ChatGPT | Membresía, licencias, roles de administración integrados y acceso basado en roles a las funciones compatibles del espacio de trabajo                                                                                               | Permisos del agente local, acceso a la organización de la Plataforma API o permisos en un servicio conectado | [Acceso al espacio de trabajo de ChatGPT](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise) y [RBAC](https://help.openai.com/en/articles/11750701-rbac) |
| Clientes locales     | Comportamiento del entorno de ejecución para las capacidades incluidas en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE, lo que abarca aprobaciones, acceso al sistema de archivos y a la red, perfiles de permisos e integraciones permitidas | Una licencia de ChatGPT, el derecho de acceso a una función o un modelo, o el acceso a datos externos                         | [Configuración administrada](/es-419/codex/enterprise/managed-configuration) y [Permisos](/es-419/codex/permissions)                                                                                                   |
| Codex Cloud       | Elegibilidad para usar flujos de trabajo alojados de Codex y los entornos en la nube puestos a disposición del usuario                                                                                                       | Política del entorno de ejecución local o permisos del repositorio concedidos por un sistema de origen                    | [Entornos en la nube](/es-419/codex/environments/cloud-environment)                                                                                                                                              |
| Plataforma API      | Membresía en la organización y en el proyecto, claves de API, acceso a modelos, uso y facturación del trabajo autenticado mediante la API                                                                                            | Membresía en el espacio de trabajo de ChatGPT, acceso a clientes locales o acceso a Codex Cloud                         | [Plataforma API](https://platform.openai.com/docs/overview)                                                                                                                                         |
| Complementos           | Disponibilidad e instalación de complementos, habilidades incluidas, acceso a conectores y acciones admitidas de los conectores                                                                                               | Autorización en el servicio conectado o permisos más amplios del entorno de ejecución local y en la nube            | [Controles de complementos](/es-419/codex/enterprise/apps-and-connectors)                                                                                                                                                 |
| Sistemas conectados | Los repositorios, archivos, mensajes y acciones a los que puede acceder la cuenta autenticada en el sistema de origen                                                                                            | Derecho de acceso al espacio de trabajo de ChatGPT, a los complementos, a Codex Cloud o a la Plataforma API                              | Los controles de administración y acceso del servicio conectado                                                                                                                                               |

Una solicitud debe superar todos los límites que le correspondan. Por ejemplo, el acceso al espacio de trabajo
puede hacer que un complemento esté disponible, pero el servicio conectado sigue determinando qué datos
puede leer la cuenta que inició sesión. Un perfil de permisos local puede restringir una ejecución
en un cliente local compatible, pero no puede conceder acceso a una función ni a un modelo
del espacio de trabajo.

## Asignar acceso al espacio de trabajo

La administración del espacio de trabajo de ChatGPT separa el acceso al producto de las
facultades administrativas.

### Comprender la diferencia entre una licencia, un rol de administrador y un rol personalizado

Una licencia determina a qué áreas del producto puede acceder un miembro. Según el plan del
espacio de trabajo, los tipos de licencias disponibles pueden incluir licencias de ChatGPT y de Codex.

Los roles integrados del espacio de trabajo determinan las facultades administrativas. El rol de **Propietario** 
administra la configuración de todo el espacio de trabajo, el rol de **Administrador** administra las operaciones
y los grupos compatibles, el rol de **Miembro** no tiene derechos administrativos y el rol de
**Lector de analítica** puede acceder a la analítica del espacio de trabajo.

Los roles personalizados definen qué funciones compatibles puede usar un miembro. No
reemplazan la elegibilidad asociada a la licencia o al plan, no conceden permisos en un sistema conectado ni
modifican los requisitos del entorno de ejecución local.

<div class="not-prose my-4 aspect-video overflow-hidden rounded-md bg-gray-900">
  <iframe
    src="https://player.vimeo.com/video/1215495812"
    title="Guía paso a paso del control de acceso basado en roles"
    loading="lazy"
    allow="autoplay; fullscreen; picture-in-picture"
    allowFullScreen
    referrerPolicy="strict-origin-when-cross-origin"
    class="h-full w-full border-0"
  ></iframe>
</div>

### Configurar la opción predeterminada del espacio de trabajo y luego crear roles personalizados específicos

Solo los propietarios del espacio de trabajo pueden configurar el control de acceso basado en roles (RBAC) y crear
roles personalizados. La configuración del espacio de trabajo establece la base para los permisos
que admiten este control. Los propietarios pueden asignar roles personalizados mediante grupos o
directamente a miembros individuales cuando se admite esta opción. Los grupos pueden administrarse manualmente
o sincronizarse mediante SCIM, y un miembro puede recibir más de un rol personalizado.

Para los permisos que lo admiten, **Predeterminado** hereda la configuración del espacio de trabajo, **Activado**
concede acceso y **Desactivado** lo deniega de forma explícita. Si se selecciona explícitamente **Desactivado** en cualquier
rol aplicable, se bloquea el acceso, incluso si otro rol lo concede. Los estados de
permisos disponibles pueden variar según la función.

### Revisar los permisos de Work Local y Work en la nube

Cuando tu espacio de trabajo ofrezca **Work Local** y **Work en la nube**, revisa tanto la
configuración predeterminada del espacio de trabajo como cada rol personalizado aplicable. Work solo está disponible para
los espacios de trabajo que cumplen los requisitos, y los controles disponibles pueden variar según el plan, la configuración
del espacio de trabajo y la implementación. Un rol no puede ampliar el acceso permitido por la
licencia de un miembro.

**Work en la nube** regula las tareas compatibles de ChatGPT Work en la nube. Cuando los
controles son independientes, **Work Local** sin **Work en la nube** permite trabajar
de forma local en la aplicación de escritorio de ChatGPT, pero no permite que los miembros inicien tareas en la nube.
El acceso local a Codex se controla mediante **Permitir que los miembros usen Codex de forma local** en **Codex
Local**. Cambiar **Usar Work de forma local** no modifica el acceso local a Codex ni
reemplaza los requisitos del entorno de ejecución local.

Algunos espacios de trabajo muestran, en cambio, la sección combinada **Codex y Work Local** . En
esa disposición, **Permitir que los miembros usen Codex y Work de forma local** controla ambos
productos.

Para conocer los requisitos de elegibilidad y la configuración vigentes, consulta
[ChatGPT Work y Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Como las licencias, los roles y los permisos disponibles cambian con las actualizaciones del producto y del plan,
consulta el Centro de ayuda para conocer la lista actual de permisos y el procedimiento
de configuración:

- [Administrar miembros, tipos de licencia, roles y acceso](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Configurar el control de acceso basado en roles](https://help.openai.com/en/articles/11750701-rbac)
- [Administrar grupos](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)

### Controlar el acceso al Historial de la computadora

El [Historial de la computadora](/es-419/codex/customization/computer-history) está desactivado de forma predeterminada en los espacios de trabajo
Business y Enterprise. Los miembros no pueden activarlo hasta que un propietario
del espacio de trabajo conceda el acceso de forma explícita. Los propietarios de espacios de trabajo Enterprise pueden conceder acceso
según el rol:

1. Abre [**Configuración del espacio de trabajo \> Permisos y roles**](https://chatgpt.com/admin/settings).
2. Busca **Historial de la computadora** y elige el rol del espacio de trabajo que debe tener
   acceso.
3. Activa **Habilitar el Historial de la computadora** para ese rol.

Este permiso solo permite que los miembros a quienes se les asigne activen el Historial de la computadora;
no activa la función por ellos. Cada miembro debe activarla por su cuenta desde la aplicación de escritorio
de ChatGPT en macOS y puede elegir qué aplicaciones y sitios web contribuyen al historial. Los miembros
que no tengan el permiso necesario en el espacio de trabajo no pueden activar la función mediante
la configuración local.

## Aplicar la política del entorno de ejecución local

La política del entorno de ejecución local restringe las capacidades incluidas en la aplicación de escritorio
de ChatGPT, Codex CLI y la extensión para IDE. Además, los requisitos administrados desde la nube
dependen de un inicio de sesión compatible en ChatGPT y de la elegibilidad del plan. Los perfiles de permisos
y los requisitos administrados pueden restringir los comandos, el acceso al sistema de archivos y a la red,
las aprobaciones y otros comportamientos del entorno de ejecución local. No modifican la licencia,
el rol en el espacio de trabajo, el derecho de acceso a modelos ni los permisos del usuario en un
sistema externo.

Los usuarios pueden seleccionar un perfil de permisos integrado o personalizado cuando la política local
lo permita. Los administradores pueden distribuir valores predeterminados y requisitos mediante los
canales compatibles de configuración administrada. Consulta [Permisos](/es-419/codex/permissions)
para conocer el comportamiento de los perfiles y [Configuración administrada](/es-419/codex/enterprise/managed-configuration)
para conocer los requisitos, la distribución y el orden de precedencia.

## Documentación relacionada

- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
- [Grupos y aprovisionamiento](/es-419/codex/enterprise/groups-and-provisioning)
- [Gestión del ciclo de vida de los usuarios](/es-419/codex/enterprise/user-lifecycle)
- [Disponibilidad de modelos en el espacio de trabajo](/es-419/codex/enterprise/workspace-model-availability)
- [Tokens de acceso](/es-419/codex/enterprise/access-tokens)
- [Configuración administrada](/es-419/codex/enterprise/managed-configuration)
- [Autenticación](/es-419/codex/auth)
