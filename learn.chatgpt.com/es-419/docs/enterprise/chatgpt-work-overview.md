<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/chatgpt-work-overview -->

ChatGPT Work y Codex comparten mecanismos fundamentales de ejecución, aislamiento
y permisos, y están sujetos a los mismos límites de seguridad contemplados en tu
acuerdo de ChatGPT Business o Enterprise. Las capacidades y los controles
disponibles en cada experiencia dependen de si una tarea se ejecuta localmente o en la
nube, de las herramientas disponibles y de las políticas aplicables al espacio de trabajo.

ChatGPT Work puede completar tareas de varios pasos con la información, los archivos,
las aplicaciones y las herramientas disponibles para un miembro autorizado del espacio de trabajo. En la web,
esas tareas se ejecutan en la nube, no en el dispositivo del miembro.

Esta descripción general explica el límite de ejecución, los controles de red y aplicaciones,
el manejo de datos y cómo se ejecutan las tareas de forma segura con ChatGPT Work en la
web. La disponibilidad y los controles administrativos dependen de tu plan y de la configuración
del espacio de trabajo.

Para una revisión específica de la ejecución en un entorno alojado, los permisos de las cuentas conectadas,
la configuración del navegador y de la red, la retención y la información disponible para auditorías, consulta
[Seguridad de ChatGPT Work en la nube](/es-419/codex/enterprise/chatgpt-work-cloud-security).

Para obtener información sobre el acceso al dispositivo, las sesiones del navegador local, las políticas administradas y el manejo
de datos locales, consulta
[Seguridad local de ChatGPT Work](/es-419/codex/enterprise/chatgpt-work-local-security).

## Aislamiento de la ejecución, archivos y acceso al dispositivo

Los archivos y las herramientas disponibles para ChatGPT Work dependen de dónde se ejecuta Work,
de los permisos del usuario y de la configuración administrativa.

### Work local

Work local ejecuta tareas a través de la aplicación de escritorio de ChatGPT en el dispositivo del usuario.
Puede acceder a archivos locales, aplicaciones y otros recursos puestos a su disposición,
de acuerdo con los permisos del usuario, los controles aplicables al espacio de trabajo y las políticas
de seguridad del dispositivo. A diferencia de Work en la Web, Work local puede utilizar recursos
que permanecen en tu computadora sin necesidad de cargar archivos en una conversación
en la nube.

### Work en la nube

Work en la nube está disponible en las interfaces web, móviles y de escritorio compatibles. Ejecuta
el arnés de ejecución de Codex en un entorno aislado sobre infraestructura administrada por OpenAI.
Las conversaciones en la nube pueden sincronizarse entre estas interfaces, y las tareas compatibles pueden
continuar mientras el usuario está ausente de la conversación.

Work en la web no puede acceder directamente a los archivos, las aplicaciones ni las pestañas abiertas
en el navegador de la computadora del usuario. El usuario puede proporcionar archivos cargándolos, agregándolos
a un proyecto compatible o mediante una aplicación conectada autorizada. La experiencia de escritorio
controla el acceso a los archivos y las aplicaciones locales mediante sus propios
permisos.

Cuando la
[Biblioteca](https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt)
está disponible, los archivos cargados o generados que cumplan los requisitos pueden guardarse allí.
Los administradores pueden controlar si ChatGPT hace referencia automáticamente a los archivos guardados
en la Biblioteca. Desactivar las referencias automáticas no impide que los usuarios accedan explícitamente
a los archivos que tienen autorización para usar ni que los adjunten.

Consulta [Entorno aislado para código y shell](/es-419/codex/sandboxing?surface=web),
[Creación y edición de documentos, hojas de cálculo y presentaciones](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work)
y
[Almacenamiento de archivos y Biblioteca en ChatGPT](https://help.openai.com/en/articles/20001052-library-for-chatgpt).

## Acceso a la red y destinos externos

Work usa herramientas como la ejecución de código y comandos de shell y el navegador en la nube para completar
tareas. Cada una de estas herramientas tiene permisos configurables.

- **Comandos de código y shell**: el acceso público a Internet depende de la política aplicable
  al espacio de trabajo y de la configuración de red individual de Work. Cuando no se permite el acceso
  público a Internet, los comandos aún pueden acceder a los destinos aprobados por OpenAI
  que son necesarios para que Work funcione. Esto controla los destinos de red, no los
  comandos que se pueden ejecutar.
- **Búsqueda web**: la búsqueda tiene controles independientes de la configuración
  de red para código y shell de Work.

Cuando está disponible, la configuración individual para código y shell se encuentra en
**Configuración** \> **Controles de datos** \> **Acceso de Work a la red**. Activar **Permitir el acceso
público a Internet** no anula ninguna restricción aplicable establecida por un
administrador. Desactivarla limita los comandos de código y shell a los destinos necesarios
de la lista administrada de destinos permitidos; no desactiva las aplicaciones conectadas, la búsqueda
web ni el navegador en la nube.

Los cambios en la configuración de red para código y shell surten efecto una vez que finaliza la ejecución actual
y Work actualiza su entorno de ejecución. Consulta
[Entorno aislado para código y shell](/es-419/codex/sandboxing?surface=web) y
[Controles de acceso de Work](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Los controles de las interacciones salientes son independientes de las
[restricciones de acceso por IP del espacio de trabajo](https://help.openai.com/en/articles/12111596-ip-allowlisting-for-chatgpt),
que limitan el acceso entrante al espacio de trabajo de ChatGPT o a la API de Cumplimiento.

## Navegador en la nube y acceso a sitios web

El
[Navegador en la nube](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
es una de las herramientas que puede usar ChatGPT Work y es distinto del
[Navegador integrado](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app).
Funciona de forma remota y usa una sesión de navegación independiente del navegador local
del usuario. No puede acceder a pestañas locales, extensiones, historial de navegación, contraseñas
guardadas ni sesiones locales autenticadas.

El navegador en la nube puede navegar por sitios web públicos, ingresar información en formularios
públicos compatibles y combinar información relevante de una aplicación aprobada con una tarea
en un sitio web. El inicio de sesión en sitios web a través del navegador en la nube no está disponible en
los espacios de trabajo Enterprise o Edu. La disponibilidad del navegador depende de tu plan,
región, despliegue y permisos del espacio de trabajo.
En los espacios de trabajo Enterprise, un administrador debe habilitar el acceso al navegador en la nube
además del acceso a Work.

El acceso a los sitios web y las acciones tienen controles independientes:

- De forma predeterminada, ChatGPT pregunta antes de visitar un sitio web nuevo. Cuando estas opciones están disponibles, los usuarios
  pueden seleccionar **Preguntar siempre**, **Aprobar automáticamente** o **Permitir siempre**, así como permitir o
  bloquear sitios web específicos. **Aprobar automáticamente** aplica verificaciones de riesgo automatizadas.
**Permitir siempre** elimina la revisión interactiva de acceso a los sitios web. Los administradores
  tienen la misma capacidad para limitar la configuración de aprobación de los usuarios (por ejemplo,
  desactivar **Permitir siempre** en todo el espacio de trabajo).
- Permitir un sitio web no implica aprobar todas las acciones que se realizan en él. ChatGPT puede
solicitar una confirmación adicional antes de realizar acciones que puedan generar un compromiso financiero,
legal, relacionado con una cuenta o de otro tipo con consecuencias importantes.

Los usuarios pueden consultar las capturas de pantalla disponibles de las páginas y la reproducción de la navegación en una conversación de Work.
Estos registros visibles para el usuario no implican que se puedan exportar mediante la API de Cumplimiento
ni que los administradores puedan ver un historial de ejecución completo.

Consulta
[Uso del navegador en la nube en ChatGPT](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
y [Navegador](/es-419/codex/browser?surface=web).

## Aplicaciones conectadas, credenciales y permisos

Una aplicación conectada o un complemento le proporciona a Work acceso únicamente a través de la integración que permite tu
espacio de trabajo y de los permisos otorgados para esa conexión. Los administradores pueden
controlar la disponibilidad de los complementos y las aplicaciones, el acceso según los roles del espacio de trabajo, la autorización
externa, la configuración de acciones y los permisos del sistema de origen desde el panel
de administración.

En los espacios de trabajo Enterprise y Edu, los complementos y sus aplicaciones subyacentes están desactivados de forma
predeterminada. En los espacios de trabajo Business, los complementos y las aplicaciones están activados de forma predeterminada. Poner un
complemento a disposición de los usuarios no habilita automáticamente la aplicación que requiere ni otorga acceso
a una cuenta. La conexión necesaria debe estar autorizada para una cuenta individual,
compartida o propiedad de un agente antes de que ChatGPT Work pueda acceder a ella. Una conexión compartida o
propiedad de un agente usa los permisos que tiene la cuenta conectada en el sistema de origen,
que pueden diferir de los permisos del usuario solicitante.

Cuando esta función está disponible, los administradores pueden limitar una aplicación a acciones de solo lectura o a un
conjunto de acciones aprobadas. La configuración de permisos de las aplicaciones también puede determinar si
ChatGPT pregunta antes de usar una aplicación, realizar cambios o ejecutar acciones
importantes. No todas las aplicaciones admiten los mismos controles de acciones, ni todas las acciones
requieren una confirmación individual de una persona.

En las aplicaciones sincronizadas, los cambios en el contenido de origen o en los permisos pueden tardar en
reflejarse. Desconectar una aplicación no elimina automáticamente la información que ya se guardó
en una conversación, un archivo generado o un registro que cuenta con su propia política de
retención.

Consulta
[Controles de administración, seguridad y cumplimiento para complementos y aplicaciones](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business),
[Controles de complementos](/es-419/codex/enterprise/apps-and-connectors),
[Configuración de Google Workspace a cargo de un administrador](https://help.openai.com/en/articles/10929079-google-workspace-admin-managed-setup)
y [Aplicaciones de ChatGPT con sincronización](https://help.openai.com/en/articles/10847137-chatgpt-apps-with-sync).

## Privacidad y manejo de datos

ChatGPT Work sigue las políticas de privacidad, seguridad y manejo de datos
aplicables a tu espacio de trabajo de ChatGPT. Las conversaciones, los archivos cargados, los archivos
generados, las aplicaciones conectadas y los datos del navegador pueden tener reglas diferentes de retención y
eliminación.

Para obtener más información, consulta [Privacidad empresarial](https://openai.com/enterprise-privacy/),
[Políticas de retención de chats y archivos](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt),
[Residencia de datos y residencia de inferencia](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)
y las [Preguntas frecuentes sobre la administración de ChatGPT Work](/es-419/codex/enterprise/work-admin-faq).

### La retención depende del tipo de datos

- **Conversaciones de Work:** se rigen por la configuración aplicable de retención y eliminación
  de conversaciones del espacio de trabajo de ChatGPT.
- **Archivos guardados en la Biblioteca:** se rigen por las reglas aplicables de retención de archivos y
  del espacio de trabajo. Eliminar una conversación no elimina los archivos almacenados en la
  Biblioteca.
- **Archivos del proyecto:** permanecen en el proyecto hasta que este se elimina, sujetos a las
  reglas y excepciones de eliminación aplicables.
- **Archivos cargados temporalmente fuera de la Biblioteca:** en Enterprise, los archivos cargados temporalmente pueden
  caducar después de 48 horas, a menos que se aplique una configuración de retención diferente.
- **Memorias guardadas, cuando están habilitadas:** se rigen por controles de memoria independientes.
- **Cookies del navegador en la nube:** se mantienen separadas de los datos del navegador local. Los usuarios pueden
  borrarlas desde la configuración del navegador en la nube.
- **Registros de la Plataforma de registros de cumplimiento:** permanecen disponibles en la plataforma durante 30
  días. Las copias exportadas se rigen por la política de retención del sistema receptor.
- **Datos de aplicaciones conectadas:** los registros de origen se rigen por las políticas de la aplicación
  conectada. Las copias guardadas en un chat, un archivo o un índice sincronizado también
  se rigen por las reglas aplicables de almacenamiento y retención de OpenAI.

Eliminar una conversación, finalizar una tarea de Work, borrar las cookies del navegador y
conservar registros de cumplimiento son operaciones diferentes. Eliminar un chat hace que deje de
estar visible y programa su eliminación permanente en un plazo de 30 días, sujeta a las
excepciones publicadas sobre seguridad, cuestiones legales y desidentificación.

Consulta
[Políticas de retención de chats y archivos](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt),
[Memoria en ChatGPT](https://help.openai.com/en/articles/8590148-memory-in-chatgpt-faq)
y la
[Plataforma de cumplimiento de OpenAI](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).
