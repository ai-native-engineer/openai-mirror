<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/chatgpt-work-cloud-security -->

ChatGPT Work forma parte de tu espacio de trabajo de ChatGPT existente y sigue sus
políticas aplicables de privacidad, seguridad y manejo de datos. Para los espacios de trabajo Business,
Enterprise y Edu, las protecciones existentes incluyen el cifrado en tránsito
y en reposo. De forma predeterminada, OpenAI no usa los datos empresariales para entrenar
sus modelos.

Work en la nube también incorpora la ejecución alojada de tareas y herramientas opcionales que pueden
acceder a sistemas conectados o realizar acciones autorizadas. Revisa los permisos,
la configuración de retención y los registros de auditoría disponibles para las capacidades que
habilita tu organización.

Las capacidades y los controles dependen del plan, el despliegue y la configuración del espacio de trabajo,
así como de la integración conectada. Para conocer el modelo de ejecución general, consulta la
[Descripción general de ChatGPT Work](/es-419/codex/enterprise/chatgpt-work-overview).

## Seguridad de un vistazo

- Las tareas en la nube se ejecutan en infraestructura administrada por OpenAI, no en el dispositivo
del usuario.
- Una tarea en la nube no hereda de ese dispositivo archivos locales, aplicaciones de escritorio,
sesiones del navegador ni acceso a redes privadas.
- Las apps conectadas usan los permisos de la cuenta autorizada, que puede ser
individual, compartida o propiedad de un agente.
- Los controles del espacio de trabajo y los específicos de cada función regulan el acceso a Work, la ejecución
local, la navegación en la nube, las apps conectadas y el acceso a la red desde código o el shell.
- Los datos de los espacios de trabajo Business, Enterprise y Edu se cifran en tránsito y en
reposo y, de forma predeterminada, no se usan para entrenar modelos de OpenAI.
- La retención y la visibilidad para auditorías dependen de la categoría de datos, la ubicación de almacenamiento,
el evento y la configuración del producto que corresponda.

## Dónde se ejecutan las tareas en la nube

Las personas pueden iniciar tareas en la nube desde las versiones compatibles de ChatGPT para la web, dispositivos móviles o
escritorio. Work en la web y en dispositivos móviles se ejecuta en la nube. La app de escritorio puede
ejecutar tareas en la nube o locales cuando los permisos correspondientes están disponibles y
habilitados.

El dispositivo del usuario se encuentra dentro del perímetro de confianza que administra el equipo de TI
de la propia organización, fuera de los sistemas operados por OpenAI. Iniciar una tarea en la nube desde
la app de escritorio no le da a la tarea acceso directo a la computadora del usuario.
La ejecución permanece en el entorno administrado por OpenAI, independientemente de la interfaz
utilizada para iniciarla.

Work en la nube usa el arnés de ejecución de tareas de Codex. Work y Codex comparten mecanismos
básicos de ejecución y aislamiento, pero sus herramientas disponibles, permisos y
controles administrativos no son idénticos. El cliente controla el acceso al espacio de trabajo,
las conexiones aprobadas y la información proporcionada intencionalmente a una tarea;
OpenAI administra el entorno de ejecución alojado.

Work en la nube se ejecuta en infraestructura compartida y administrada por OpenAI. En la ruta de ejecución
compatible actual, las tareas se ejecutan en sandboxes basados en VM, con el estado de ejecución
asociado al usuario autenticado de la cuenta en el espacio de trabajo. Work puede reutilizar
un entorno entre tareas o reemplazarlo y conservar el estado que cumpla los requisitos. Esto
no significa que cada tarea reciba un contenedor nuevo ni que cada cliente tenga un
host físico dedicado. Los clientes no proporcionan, alojan ni administran los contenedores de
Work en la nube.

## A qué puede acceder una tarea en la nube

Una tarea en la nube puede usar información disponible a través de una vía autorizada:

- Información que una persona ingresa en una conversación.
- Archivos cargados intencionalmente, adjuntados desde la Biblioteca o puestos a disposición
a través de un proyecto.
- Contenido obtenido a través de una app habilitada y una conexión de cuenta
autorizada.
- Contenido de sitios web al que se accede a través de un navegador en la nube habilitado u otra
capacidad web permitida, sujeto a los controles de acceso aplicables.

Una tarea en la nube no hereda directamente el acceso a archivos locales, aplicaciones
instaladas ni a la sesión del navegador del usuario. Que un dispositivo tenga acceso a una VPN
corporativa, un sitio web interno o una red privada no le otorga ese acceso a la tarea en la
nube.

Una conexión autorizada puede poner a disposición información de un sistema interno
a través de su propia vía de acceso. Esa conexión no le da a la tarea en la nube
acceso sin restricciones al dispositivo ni a la red del empleado.

## Apps, complementos y cuentas conectadas

Una app puede darle a Work acceso a información o acciones en otro sistema. Un
complemento puede usar una app como una de sus herramientas subyacentes. Hacer que un complemento esté disponible
no habilita automáticamente la app subyacente, ni autoriza una cuenta, ni
aprueba todas las acciones que la integración puede realizar.

Una tarea que usa una app conectada, directamente o a través de un complemento, solo puede continuar
cuando:

- La app y cualquier complemento que la requiera están habilitados en el espacio de trabajo.
- La persona tiene el acceso necesario en el espacio de trabajo o a través de su rol.
- La conexión usa una cuenta autorizada individual, compartida o propiedad de
un agente.
- La cuenta conectada, los alcances aprobados y la configuración disponible de las acciones de la app
permiten acceder a la información o realizar la operación solicitada.

En las apps que admiten **Control de acciones**, los administradores pueden permitir acciones de solo lectura,
todas las acciones o un conjunto personalizado. Los **Permisos de las apps** controlan cuándo
ChatGPT pide confirmación para trabajar con una app. Según la app y el
espacio de trabajo, las opciones pueden incluir **Preguntar siempre**, **Cualquier cambio**, **Acciones
importantes** y **No preguntar nunca**. Con **Cualquier cambio**, las operaciones de lectura compatibles pueden realizarse
sin solicitar confirmación, mientras que los cambios sí la requieren.

Una operación de escritura autorizada puede ejecutarse sin solicitar confirmación cuando la política configurada
lo permite. Esto no amplía las acciones permitidas de la app, el acceso al espacio de trabajo ni los
permisos de la cuenta conectada. ChatGPT aún puede bloquear algunas acciones de alto
riesgo.

Confirma que el complemento y cada app subyacente estén disponibles en el espacio de trabajo.
Revisa el acceso por rol, la autorización de la cuenta conectada y los permisos de las acciones como
decisiones independientes. Consulta
[Controles de complementos](/es-419/codex/enterprise/apps-and-connectors).

### Conexiones personales y compartidas

Una conexión personal usa los permisos que tiene el empleado conectado en el sistema de
origen. Una conexión compartida o propiedad de un agente, en cambio, usa los permisos de
su cuenta conectada. Esa cuenta podría acceder a información o realizar
acciones a las que la persona solicitante no tendría acceso con una cuenta personal.

Antes de habilitar una conexión compartida, limita los permisos y los
alcances de la cuenta, elige quién puede usarla y revisa las acciones que puede realizar. Consulta
[Conexiones y permisos de los agentes del espacio de trabajo](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business).

El contenido obtenido de una app conectada no se guarda automáticamente como un archivo de la Biblioteca.
Si más adelante se guarda en una conversación, un proyecto, la Biblioteca o un
índice sincronizado, esa copia se rige por las reglas de la ubicación donde se guardó.

## Navegador en la nube y acceso a la red

El navegador en la nube, la búsqueda web, las apps conectadas y el acceso a la red desde código o el shell son
capacidades independientes. Restringir una no deshabilita automáticamente las
demás.

### Navegador en la nube

El navegador en la nube es una herramienta alojada que una tarea de Work puede usar para interactuar con
sitios web. Abrir ChatGPT en un navegador web o en la app de escritorio no habilita la navegación
en la nube; una tarea en la nube puede ejecutarse sin ella.

El navegador alojado no hereda el perfil del navegador local del usuario, las pestañas abiertas,
las sesiones iniciadas, las contraseñas guardadas, el administrador de contraseñas ni el historial de navegación.
Cuando esta función está disponible, los usuarios pueden iniciar sesión por separado mediante un flujo seguro de inicio de sesión
en el entorno alojado. Esto no otorga acceso a su sesión del navegador local.

Las interacciones compatibles con sitios web pueden incluir formularios públicos y combinar
información de una app autorizada con una tarea en un sitio web. Cuando están disponibles,
los permisos de sitios web incluyen **Preguntar siempre**, **Aprobar automáticamente** y **Permitir
siempre**. **Aprobar automáticamente** aplica verificaciones automatizadas de riesgo; **Permitir siempre**
elimina la revisión interactiva del acceso al sitio web. Ninguna de las dos opciones otorga nuevos permisos
a las apps ni aprueba todas las acciones en un sitio web. Las acciones con consecuencias importantes
pueden seguir requiriendo una confirmación por separado.

Para que una tarea de Work use el navegador en la nube en un espacio de trabajo Enterprise,
los administradores deben habilitar tanto el acceso a Work como al navegador en la nube. Consulta
[Uso del navegador en la nube en ChatGPT](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt).

### Acceso a la red desde código y el shell

El acceso a Internet público para la ejecución de código o del shell se rige por su propia política de
red. Cuando el acceso a Internet público está desactivado, los destinos de red necesarios para
ChatGPT Work pueden seguir siendo accesibles a través de una lista administrada de destinos permitidos.

La lista de destinos permitidos regula los destinos de red, no los comandos del shell. Deshabilitar
el acceso a Internet público para la ejecución de código o del shell no deshabilita, por sí solo,
el navegador en la nube, la búsqueda web ni las apps conectadas. Los cambios en la configuración de
red se aplican después de que finaliza la ejecución de código o el comando del shell en curso y se
actualiza el entorno de ejecución.

Consulta [Entorno aislado para código y el shell](/es-419/codex/sandboxing?surface=web).

## Manejo y retención de datos

Work en la nube aplica las protecciones de privacidad y seguridad correspondientes al espacio de trabajo de ChatGPT
descritas anteriormente. Consulta
[Privacidad para empresas](https://openai.com/enterprise-privacy/).

La información asociada con una tarea en la nube no se rige por un único
plazo de retención universal:

| Categoría de datos                        | Comportamiento de retención y eliminación                                                                                                                                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conversaciones de Work                   | Se rigen por la configuración de retención de conversaciones del espacio de trabajo. Por lo general, los chats eliminados se programan para su eliminación permanente en un plazo de 30 días, con las excepciones publicadas de seguridad, legales y de desidentificación.                                                                                |
| Estado e instantáneas de la ejecución alojada | Tienen un ciclo de vida distinto al de las conversaciones y los archivos. El acceso al estado de ejecución se limita al usuario de la cuenta, y la configuración de retención de conversaciones del espacio de trabajo sirve de referencia para las instantáneas almacenadas que cumplen los requisitos. Finalizar una tarea o eliminar un chat no elimina de inmediato todos los artefactos relacionados. |
| Archivos guardados en la Biblioteca               | Los archivos cargados o generados se rigen por las reglas de retención aplicables de la Biblioteca y del espacio de trabajo. Eliminar una conversación no elimina un archivo guardado en la Biblioteca.                                                                                                                                      |
| Archivos del proyecto                        | Permanecen asociados a su proyecto hasta que se quitan o se elimina el proyecto, sujetos a las reglas de eliminación aplicables.                                                                                                                                                                       |
| Memorias guardadas, cuando están habilitadas         | Se rigen por controles de memoria independientes. Eliminar una conversación no necesariamente elimina una memoria guardada existente.                                                                                                                                                                             |
| Cargas temporales                    | Las cargas temporales de Enterprise fuera de la Biblioteca que cumplan los requisitos pueden vencer después de 48 horas, a menos que se aplique otra configuración de retención.                                                                                                                                                      |
| Contenido de apps conectadas                | Los registros del sistema de origen se rigen por las políticas de ese sistema. Las copias guardadas en una conversación, un proyecto, la Biblioteca o un índice sincronizado se rigen por las reglas de la ubicación donde se guardaron.                                                                                                                         |
| Datos del navegador en la nube                   | Los datos del navegador alojado son independientes de los datos del navegador local. Los usuarios pueden eliminar las cookies guardadas del navegador en la nube mediante la configuración correspondiente.                                                                                                                                                    |
| Registros de cumplimiento                   | Los registros de la Plataforma de registros de cumplimiento están disponibles durante 30 días. Las copias exportadas se rigen por la política de retención del sistema receptor.                                                                                                                                                               |

Eliminar una conversación, eliminar un archivo de la Biblioteca o una memoria guardada,
desconectar una app y borrar los datos del navegador alojado son acciones distintas.
Revisa la ubicación de almacenamiento correspondiente en lugar de suponer que una sola acción elimina
todas las copias. Consulta
[Políticas de retención de chats y archivos](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt).

Conservar el contexto adecuado de la conversación y la ejecución puede ayudar a Work a reanudar
tareas interrumpidas, consultar pasos anteriores y producir resultados más consistentes.
Una retención más breve o la eliminación pueden reducir esa continuidad, así que elige una configuración
que equilibre los requisitos de seguridad con la utilidad del flujo de trabajo.

Los espacios de trabajo Enterprise y Edu que cumplan los requisitos pueden usar Enterprise Key Management para
el contenido almacenado compatible, incluidas las instantáneas de ejecución alojada compatibles cuando
se requiera cifrado administrado por el cliente. La cobertura varía según la categoría de datos y la
implementación. La rotación de una clave no elimina los datos existentes ni, por sí sola, impide
el acceso al contenido cifrado anteriormente. Revocar o deshabilitar el acceso a la clave es una
acción independiente que puede interrumpir los flujos de trabajo compatibles. Ninguna de estas acciones sustituye una
política de retención o eliminación.

La residencia de datos y la residencia de inferencia se aplican solo al contenido que cumpla los requisitos y a
las cargas de trabajo compatibles, según el acuerdo, la región y la
configuración de la organización. Las apps conectadas, los proveedores externos y algunos procesos o
índices sincronizados pueden regirse por reglas de ubicación independientes. Verifica la compatibilidad del
producto, la integración y la región. Consulta
[Residencia de datos y residencia de inferencia](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt).

La [retención cero de datos](/api/docs/guides/your-data#zero-data-retention) de la API de OpenAI
es un control específico de la API y no define la retención de ChatGPT Work.

## Controles de acceso para administradores

Revisa los controles que se aplican a cada parte de una tarea en la nube:

- **Work en la nube y Work local:** cuando haya controles independientes disponibles,
  administra Work en la nube y Work local con controles distintos en **Configuración del espacio de trabajo** \>
**Permisos y roles**. En otros espacios de trabajo, Work local puede compartir un control
  con Codex Local.
- **Apps y complementos:** elige qué integraciones están disponibles y qué
  personas o roles pueden usarlas.
- **Acciones de cuentas conectadas:** revisa los permisos de la cuenta, los alcances de la aplicación
  y los controles de acciones o confirmaciones disponibles.
- **Navegador y acceso a la red:** evalúa por separado el acceso al navegador en la nube y el acceso a la red pública
  para la ejecución de código o comandos de shell.

Habilita **Work en la nube** solo para usuarios o grupos aprobados. Cuando haya controles separados para
**Work en la nube** y **Work local** , habilita **Work en la nube**
y deshabilita **Work local** para el rol correspondiente, a fin de permitir el uso de Work en la nube sin
ejecución local. Cuando Work local y Codex compartan un control, revisa el efecto
en ambos antes de deshabilitar la ejecución local. Estos controles no impiden que una
persona autorizada cargue intencionalmente un archivo en una tarea en la nube.

En los permisos de rol que admiten los estados **Predeterminado**, **Activado** y **Desactivado** ,
**Predeterminado** hereda la configuración del espacio de trabajo, **Activado** otorga acceso y **Desactivado**
elimina el acceso a través de ese rol. Si un usuario tiene varios roles personalizados, otro
rol aún puede otorgarle acceso. Algunas configuraciones de Work y de los complementos usan controles distintos,
de dos estados. Verifica el acceso efectivo considerando todos los roles asignados. Consulta
[Control de acceso basado en roles](https://help.openai.com/en/articles/11750701-rbac).

Cuando esté disponible, el permiso **Work en la nube** se aplica a las experiencias web,
móviles y de escritorio compatibles. No permite seleccionar de forma independiente cuáles de esas
interfaces pueden ejecutar tareas en la nube. Considera la administración de dispositivos u otros controles
de acceso si una implementación debe excluir una interfaz específica.

## Visibilidad para auditoría y cumplimiento

En los espacios de trabajo Enterprise y Edu que cumplan los requisitos, la Plataforma de registros de cumplimiento puede
incluir los prompts y las respuestas de Work admitidos. Las llamadas a apps conectadas tienen registros
independientes, y los registros de auditoría disponibles en el sistema de origen varían según la integración.
Los puntos de acceso de cumplimiento compatibles pueden dar acceso a los archivos de la Biblioteca que cumplan los requisitos.

La cobertura depende del evento y del sistema donde ocurre. No supongas
que cada comando de shell, interacción con el navegador, llamada a una app, operación con archivos o
aprobación aparece en una exportación de cumplimiento visible para el cliente.

El monitoreo de puntos de acceso puede observar el cliente de ChatGPT o el tráfico de red en dispositivos administrados,
pero no puede inspeccionar las acciones dentro del entorno de ejecución alojado. En su lugar, usa
los registros compatibles de Work, de cumplimiento y de los sistemas conectados.

Revisa la cobertura actual de eventos de cumplimiento junto con los informes del espacio de trabajo,
los registros de auditoría de los sistemas conectados y las políticas de retención de los sistemas que reciben
los registros exportados. Consulta la
[Plataforma de cumplimiento de OpenAI](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

## Empieza con una prueba piloto a pequeña escala

Elige una tarea práctica para un grupo pequeño. Por ejemplo, un equipo de seguridad podría
comparar un aviso aprobado de un proveedor con un inventario autorizado y revisar un
borrador de evaluación de la exposición antes de decidir qué hacer. Si la navegación en la nube o
las apps conectadas no están disponibles, proporciona directamente el aviso y un extracto aprobado
del inventario.

Habilita solo el acceso que requiere la tarea. Confirma los permisos de las cuentas
conectadas, la configuración de retención, los registros de auditoría disponibles y en qué punto una persona
debe revisar el resultado antes de ampliar el acceso. Para planificar la implementación, consulta la
[Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup).
