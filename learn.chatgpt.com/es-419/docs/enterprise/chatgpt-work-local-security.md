<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/chatgpt-work-local-security -->

ChatGPT Work puede usar archivos, aplicaciones y sesiones de navegador aprobados en la computadora del usuario para completar tareas locales. El acceso depende de los permisos del espacio de trabajo, del acceso que ya tiene la cuenta del usuario, de los permisos del sistema operativo, de las aprobaciones de aplicaciones y de las políticas de dispositivo compatibles.

Las funciones locales dependen de la app de escritorio compatible, del sistema operativo, de los derechos de uso del espacio de trabajo, de los permisos de los roles, de la política del dispositivo y del despliegue del producto.

## Resumen de seguridad

- Las tareas locales se ejecutan a través de la aplicación de escritorio de ChatGPT. Abrir una tarea alojada en la nube desde la misma aplicación no la convierte en una tarea local.

- Los controles disponibles para Work local y alojado dependen de la configuración del espacio de trabajo y del despliegue.

- El acceso a archivos, Uso de la computadora, los navegadores y las apps conectadas usan distintos permisos y aprobaciones.

- Un navegador o una aplicación con una sesión ya iniciada en un sistema de la empresa puede dar acceso con los permisos de esa cuenta.

- Las políticas compatibles para dispositivos administrados pueden restringir las funciones locales sin reemplazar los controles de acceso del espacio de trabajo.

- Los datos de los espacios de trabajo Business, Enterprise y Edu que procesan los servicios de OpenAI cubiertos se cifran en tránsito y en reposo, y no se usan para entrenar los modelos de OpenAI de forma predeterminada.

- Los archivos locales, el contexto de la tarea, los datos del navegador, los registros de los sistemas conectados y los eventos de auditoría pueden estar sujetos a distintas reglas de almacenamiento y retención.

## Dónde se ejecutan las tareas locales

Work Local accede a los recursos aprobados a través de la app de escritorio en la computadora del usuario. Work en la nube se ejecuta en infraestructura administrada por OpenAI, incluso cuando se abre desde la misma app de escritorio.

Los archivos locales pueden permanecer en el dispositivo, pero los fragmentos de archivos relevantes, los prompts, las capturas de pantalla, el contenido del navegador o los resultados de herramientas pueden enviarse a los servicios de OpenAI para completar una tarea. La ejecución local no implica que la inferencia del modelo se realice sin conexión o exclusivamente en el dispositivo.

## Acceso a archivos y al dispositivo

Una tarea local puede trabajar con la información que el usuario proporciona o pone a disposición, incluidos archivos compatibles, contenido de aplicaciones, sesiones de navegador y sistemas conectados autorizados. El acceso depende de los privilegios que ya tiene el usuario y de los controles que rigen esa función específica.

Otorgar acceso a Work local no aprueba automáticamente todas las aplicaciones, no concede derechos de administrador ni elude los permisos de la cuenta usada para acceder a otro sistema. Una conexión compartida aprobada puede tener privilegios distintos de los de la cuenta personal del usuario.

## Uso de la computadora y aprobaciones de aplicaciones

[Uso de la computadora](/es-419/codex/computer-use) puede interactuar con aplicaciones de escritorio compatibles solo cuando la función está disponible, se han otorgado los permisos necesarios del sistema operativo y el usuario autoriza la aplicación. Según las opciones disponibles, la aprobación puede aplicarse a la sesión actual o a tareas futuras.

En macOS, Grabación de pantalla permite que Uso de la computadora vea el contenido de las aplicaciones, y Accesibilidad le permite hacer clic, escribir y navegar. Las tareas compatibles de macOS pueden ejecutarse en segundo plano. En Windows, Uso de la computadora opera en el escritorio activo y visible, y no puede ejecutarse en segundo plano mientras el usuario sigue usando esa misma sesión.

Los usuarios pueden detener una tarea en cualquier momento. Uso de la computadora no puede aprobar solicitudes de seguridad del sistema operativo, autenticarse como administrador ni automatizar aplicaciones de terminal o el propio ChatGPT.

### Dispositivos bloqueados

Las configuraciones compatibles de macOS pueden permitir, de forma opcional, que una tarea aprobada de Uso de la computadora continúe mientras el Mac está bloqueado. La disponibilidad depende de la versión de la app, del despliegue de la función, de los requisitos aplicables y de si se cumplen los criterios para el control remoto.

Los administradores pueden desactivar el funcionamiento con el dispositivo bloqueado mediante la configuración administrada compatible. Uso de la computadora en Windows requiere un escritorio activo y desbloqueado; el comportamiento de uso con el dispositivo bloqueado en macOS no implica una compatibilidad equivalente en Windows.

## Sesiones de navegador y sesiones ya iniciadas

Work Local no obtiene acceso automáticamente a todos los navegadores ni a todas las cuentas de la empresa. El acceso depende del navegador utilizado, de la cuenta con la sesión iniciada y de las aprobaciones requeridas para esa experiencia de navegación.

| Vía de acceso mediante el navegador                                | Sesión y límite de seguridad                                                                                                                                                                                                 |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Navegador integrado de la app de escritorio](/es-419/codex/browser)    | Usa un perfil de navegador separado del navegador habitual del usuario. El usuario puede iniciar sesión en ese perfil, y el acceso compatible a sitios web puede requerir aprobación. El navegador integrado no puede automatizar la carga de archivos.              |
| [Extensión de Chrome](/es-419/codex/chrome-extension) | Puede interactuar con las pestañas y cuentas existentes del navegador cuando se aprueban la extensión y el acceso a sitios web. Los usuarios pueden aprobar un sitio para una sola ocasión o permitir el acceso futuro; el acceso al historial del navegador y a los archivos locales requiere una revisión por separado. |
| Control de un navegador con Uso de la computadora            | Usa un navegador aprobado como aplicación de escritorio, incluidas las cuentas con sesiones ya iniciadas en ese navegador. Siguen aplicándose los permisos del sistema operativo, la aprobación de la aplicación y los permisos de la cuenta existente.               |

Las opciones de aprobación de sitios web y las confirmaciones de acciones sensibles varían según la experiencia de navegación. Permitir todos los sitios reduce las futuras solicitudes de aprobación, por lo que los usuarios deben revisar esa opción antes de habilitarla.

Un navegador alojado en la nube está separado de los navegadores locales del usuario y no hereda automáticamente sus sesiones ya iniciadas. Los flujos de trabajo compatibles en la nube pueden solicitar un inicio de sesión independiente, autorizado por el usuario.

## Apps, complementos y cuentas conectadas

Una app conectada puede proporcionar acceso a información o acciones en otro sistema. Un complemento puede usar una app como herramienta subyacente. Que un complemento esté disponible no habilita automáticamente la app requerida, no autoriza una cuenta ni permite todas las acciones.

La disponibilidad de complementos y apps depende del plan y de la configuración del espacio de trabajo. La [descripción general de ChatGPT Work](/es-419/codex/enterprise/chatgpt-work-overview) indica que los complementos y sus apps subyacentes están desactivados de forma predeterminada en los espacios de trabajo Enterprise y Edu, y activados de forma predeterminada en los espacios de trabajo Business. Verifica la configuración real del espacio de trabajo y de la experiencia del producto correspondientes.

Antes de que una tarea use un sistema conectado, confirma que el espacio de trabajo permite la app y cualquier complemento requerido, que la conexión está autorizada y que la cuenta conectada puede acceder a la información solicitada o realizar la acción solicitada. Los ajustes de solo lectura, las acciones permitidas y los requisitos de confirmación varían según la integración.

Los complementos exclusivos de escritorio, las herramientas locales y otras funciones proporcionadas localmente pueden seguir distintos procesos de instalación o aprobación. No supongas que todas las herramientas locales usan el mismo proceso de aprobación administrativa.

### Conexiones personales y compartidas

Una conexión personal usa los permisos del usuario conectado en el sistema de origen. Una conexión compartida o propiedad de un agente usa los permisos de la cuenta conectada, que pueden ser más amplios que el acceso propio del usuario.

Limita las cuentas compartidas a los datos y las acciones necesarios, restringe quién puede usarlas y aplica los controles compatibles de acciones o confirmación. Los registros del sistema conectado siguen sujetos a los permisos y las políticas de retención de ese sistema.

## Acceso de administradores y políticas de dispositivos administrados

Revisa los controles de Work disponibles en **Configuración del espacio de trabajo** \> **Permisos y roles**. Que Work local y Work alojado aparezcan como permisos distintos depende de la configuración del espacio de trabajo y del despliegue. Para obtener más orientación, consulta las [preguntas frecuentes para administradores de Work](/es-419/codex/enterprise/work-admin-faq).

Habilita solo los entornos de ejecución aprobados para cada usuario o grupo y verifica el acceso efectivo después de hacer cambios.

Los permisos del espacio de trabajo determinan quién puede usar Work. Los administradores también pueden restringir las funciones de escritorio compatibles mediante requisitos obligatorios definidos en `requirements.toml`. Según la implementación, estos requisitos pueden distribuirse mediante la configuración administrada del espacio de trabajo, un archivo de configuración a nivel del sistema o herramientas compatibles de administración de dispositivos móviles para macOS.

Los usuarios individuales no pueden anular los requisitos obligatorios. En cambio, los valores predeterminados administrados establecen ajustes iniciales que los usuarios podrían modificar. Ninguno de estos mecanismos reemplaza los roles del espacio de trabajo ni los permisos del sistema operativo.

| Ajuste administrado                                       | Objetivo de seguridad                                                             |
| ----------------------------------------------------- | ---------------------------------------------------------------------------- |
| `features.computer_use = false`                       | Desactiva las funciones compatibles de Uso de la computadora.                                 |
| `allow_appshots = false`                              | Impide la captura de Appshot donde sea compatible.                                           |
| `features.in_app_browser = false`                     | Desactiva el navegador integrado de la app de escritorio.                                  |
| `features.browser_use = false`                        | Desactiva la automatización compatible del navegador; revisa por separado otras vías de acceso mediante navegadores. |
| `features.apps = false` o `features.plugins = false` | Restringe las aplicaciones conectadas o los complementos compatibles.                        |
| `computer_use.allow_locked_computer_use = false`      | Impide el uso de las funciones compatibles de Uso de la computadora mientras un Mac está bloqueado.                        |

Los ajustes y métodos de distribución disponibles dependen del cliente, del sistema operativo, del espacio de trabajo y de la configuración de la implementación. Valida las restricciones en un dispositivo administrado representativo. Para conocer los ajustes de políticas compatibles, los ejemplos de configuración y las instrucciones de configuración de MDM, consulta [Configuración administrada](/es-419/codex/enterprise/managed-configuration).

## Conectividad de red local y recursos privados

Una tarea puede acceder a información de la empresa por vías como un navegador del dispositivo, una aplicación de escritorio aprobada o una app conectada. Los controles existentes del dispositivo, del proxy, de la VPN, del sistema de origen y del punto de acceso pueden aplicarse de forma distinta a cada vía.

El acceso a una VPN corporativa no autoriza automáticamente a todas las herramientas a usar todos los recursos internos. Del mismo modo, un navegador de Work en la nube o un control de red en la nube no constituye una restricción universal sobre la conectividad de red local del dispositivo. Revisa la conexión, la identidad, el destino y la acción que realmente requiere el flujo de trabajo.

## Manejo y retención de datos

Aplica al dispositivo y al flujo de trabajo específicos los controles de tu organización para puntos de acceso, acceso a archivos, proxies y prevención de pérdida de datos. Confirma si esos controles pueden impedir que la información sensible ingrese a la tarea antes de que se procese. Los registros de auditoría y las exportaciones de cumplimiento ayudan con el monitoreo y la investigación, pero no bloquean el procesamiento por sí solos.

El almacenamiento y la retención dependen de la categoría de información y de dónde se guarde.

| Categoría de información                            | Qué revisar                                                                                                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Registros locales de conversaciones                      | Cómo se almacenan, eliminan, respaldan o comparten los registros locales en la experiencia de escritorio. No supongas que la configuración de retención de las conversaciones alojadas se aplica a todos los artefactos locales. |
| Archivos locales y resultados generados               | El almacenamiento del dispositivo, la política de puntos de acceso, las cargas autorizadas por el usuario, el uso compartido externo y cualquier copia guardada por separado.                                                       |
| Prompts, fragmentos de archivos y contexto de la aplicación | El contenido proporcionado a un modelo o servicio, los términos aplicables al espacio de trabajo y el recorrido real de los datos en el flujo de trabajo.                                                           |
| Voz y capturas de la aplicación                              | La entrada del micrófono, las capturas de pantalla de la ventana en primer plano, el texto accesible de las aplicaciones, el almacenamiento local de la sesión y cualquier contenido enviado como contexto de la tarea.                          |
| Datos del navegador                                    | El perfil del navegador utilizado, las sesiones ya iniciadas, el historial de navegación, las descargas, las aprobaciones de sitios web y cualquier contenido de la tarea almacenado por separado.                           |
| Registros de sistemas conectados                        | Los permisos y la retención del sistema de origen, la identidad de la cuenta conectada y cualquier información guardada por separado en la conversación o en otro destino.              |
| Registros de cumplimiento y actividad                 | Qué eventos de Work Local están disponibles para el espacio de trabajo, la integración compatible y la política de retención del sistema receptor.                                   |

Para los espacios de trabajo Business, Enterprise y Edu compatibles, los datos empresariales procesados por los servicios de OpenAI cubiertos se cifran en tránsito y en reposo y, de forma predeterminada, no se usan para entrenar ni mejorar los modelos de OpenAI. Estas protecciones no significan que OpenAI controle cada archivo del dispositivo, aplicación de terceros, perfil de navegador o registro del sistema de origen.

No apliques a los registros locales un período de retención de conversaciones alojadas, cargas temporales o registros de cumplimiento sin confirmar que corresponde a la categoría de datos específica.

## Visibilidad para auditoría y cumplimiento

Los informes disponibles dependen del plan del espacio de trabajo, la experiencia del producto, el evento, la aplicación conectada y la configuración implementada. Verifica la cobertura de Work Local antes de basarte en una exportación del espacio de trabajo para responder a incidentes o realizar una revisión regulatoria.

Determina si los sistemas pertinentes registran la identidad de la tarea, los prompts y las respuestas admitidos, las llamadas a aplicaciones conectadas, las aprobaciones del navegador, las acciones en aplicaciones, la actividad con archivos locales o los eventos de puntos de acceso. Los registros del sistema de origen y del dispositivo pueden ofrecer una visibilidad distinta de la que ofrecen los registros del espacio de trabajo de ChatGPT.

OpenAI no almacena por separado un registro completo de las acciones de Chrome realizadas mediante la extensión. No supongas que todas las operaciones con archivos locales, capturas de pantalla, acciones del navegador, aprobaciones o actualizaciones externas aparecen en la API de Cumplimiento.

## Comienza con una tarea aprobada

Comienza con un grupo pequeño que use dispositivos administrados y elige una tarea aprobada, como comparar libros de cálculo financieros seleccionados. Confirma el acceso a Work de cada usuario y proporciona únicamente los archivos, las aplicaciones, las sesiones del navegador o las cuentas conectadas que la tarea requiera.

Verifica que las acciones aprobadas funcionen, que las acciones restringidas se bloqueen y que los registros disponibles satisfagan tus necesidades de monitoreo. Pide a un usuario que revise los resultados y cualquier cambio externo antes de ampliar el acceso.
