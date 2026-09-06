<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/work-admin-faq -->

ChatGPT Work incorpora a ChatGPT la tecnología en la que se basa Codex para realizar tareas más largas y
de varios pasos. Puede recopilar contexto de chats, archivos, recursos del espacio de trabajo
y sistemas conectados; usar herramientas aprobadas; y crear resultados listos para su
revisión. El acceso, el contexto, las acciones, el comportamiento de la red y el uso de créditos varían según el
plan, la configuración del espacio de trabajo, los permisos de las fuentes y la plataforma.

## Descripción general

ChatGPT Work permite que los usuarios deleguen a ChatGPT tareas más largas y de varios pasos. Puede recopilar
información de fuentes conectadas, razonar en varios pasos, crear documentos,
presentaciones o análisis, y devolver resultados para su revisión.

ChatGPT Work está disponible en las plataformas web, móviles y de escritorio compatibles para
los planes y espacios de trabajo que reúnen los requisitos. Cuando se admite, los propietarios del espacio de trabajo o los
administradores autorizados pueden administrar Work en la nube, Work local y Codex local mediante
permisos independientes. En los espacios de trabajo Enterprise y Edu que reúnen los requisitos, el rol
predeterminado del espacio de trabajo incluye Work, salvo que un administrador autorizado lo desactive. Los controles del navegador y
de la red restringen aún más Work en la nube, y la disponibilidad depende del rol,
el plan, el espacio de trabajo y la región. Consulta
[ChatGPT Work y Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Estas preguntas frecuentes explican cómo los administradores gestionan ChatGPT Work: controles de acceso y datos,
cumplimiento y visibilidad, uso y gastos, respuesta a incidentes y prácticas de
implementación. Para conocer el modelo de ejecución alojada y los límites de seguridad, consulta
[Descripción general de ChatGPT Work](/es-419/codex/enterprise/chatgpt-work-overview).

## Controles administrativos principales

Los administradores gestionan ChatGPT Work mediante estas capas de control:

- **Acceso al espacio de trabajo empresarial:** los controles de identidad y acceso gestionan la
  autenticación y el acceso al espacio de trabajo. Según el plan y la
  configuración, las funciones de identidad controladas por los administradores pueden incluir SSO,
  verificación de dominios, aprovisionamiento mediante SCIM, gestión del ciclo de vida de los usuarios y
  sincronización de grupos de identidad. SCIM y los grupos de identidad sincronizados no se
  incluyen en ChatGPT Business. Los usuarios pueden habilitar la MFA de OpenAI en sus cuentas.
  ChatGPT no permite exigir la MFA en todo el espacio de trabajo; las organizaciones que
  la requieran deben exigir SSO y MFA a través de su proveedor de identidad. Administra el
  SSO y la configuración de identidad relacionada en la
[Consola de administración global](https://help.openai.com/en/articles/12289294-admin-portal).
  Consulta [Autenticación multifactor](https://help.openai.com/en/articles/7967234-enabling-or-disabling-multi-factor-authentication-mfa).
- **Acceso a ChatGPT Work dentro del espacio de trabajo:** cuando está disponible, Work en la nube
  rige el uso de Work alojado en las plataformas web, móviles y de escritorio compatibles.
  Work local rige el uso local de Work en la aplicación de escritorio, mientras que Codex local controla el acceso local a
  Codex en los clientes de escritorio, CLI e IDE compatibles. La configuración del navegador y de la red en la nube
  restringe aún más Work en la nube. El control de acceso basado en roles (RBAC) personalizado
  y los permisos disponibles dependen del plan y del espacio de trabajo.
- **Pertenencia a grupos:** en los planes compatibles con SCIM, sincroniza los grupos mediante
  un proveedor de identidad para que el acceso se actualice cuando los empleados se incorporen a la organización,
  cambien de rol o se vayan. Consulta
[Grupos y aprovisionamiento](/es-419/codex/enterprise/groups-and-provisioning).
- **Roles del espacio de trabajo y de los miembros:** los roles integrados de Enterprise incluyen Propietario,
  Administrador, Miembro y Visualizador de analítica. En los planes compatibles, los roles personalizados y
  el RBAC para miembros controlan el acceso a ChatGPT Work, los complementos y otras capacidades.
  Cuando se aplican distintos tipos de licencia, los miembros también necesitan una que incluya ChatGPT; una
  licencia exclusiva de Codex no concede acceso a Work. Consulta
[Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions).
- **Complementos y apps:** la política de complementos rige su disponibilidad e
  instalación. El acceso a las apps, los controles de acciones y el funcionamiento de las aprobaciones se
  configuran por separado. Cuando están disponibles, los agentes del espacio de trabajo tienen sus propios
  controles. Consulta [Controles de complementos](/es-419/codex/enterprise/apps-and-connectors),
[Complementos](/es-419/codex/plugins) y el
[documento técnico sobre la seguridad de App](https://cdn.openai.com/business-guides-and-resources/app-security-whitepaper.pdf).
- **Permisos de los sistemas de origen:** un usuario solo puede acceder al contenido y las acciones
  que la cuenta o la conexión compartida permiten en la aplicación nativa. Consulta
[Controles de administración, seguridad y cumplimiento en apps](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business).
- **Restricciones de aprobación y de acciones:** en las apps que admiten el control de acciones,
  los administradores pueden permitir todas las acciones, acciones de solo lectura o un conjunto personalizado, y decidir
  cómo se gestionan las acciones recién agregadas. Los permisos de las apps determinan por separado
  cuándo ChatGPT solicita confirmación antes de usar una app.
- **Créditos:** ChatGPT Work y Codex comparten precios, créditos y límites de uso.
  Los administradores de Enterprise y Edu que reúnen los requisitos pueden establecer límites mensuales por usuario mediante un
  valor predeterminado para el espacio de trabajo, valores predeterminados para grupos y excepciones individuales. Los usuarios pueden
  solicitar aumentos cuando el espacio de trabajo lo permite. Business sigue un modelo independiente
  de créditos y control de gastos. Consulta
[Límites de uso y controles de gastos de ChatGPT](/es-419/codex/enterprise/usage-limits).
- **Analítica e informes:** la Consola de administración global y la analítica del espacio de trabajo
  permiten analizar la adopción y el uso de créditos. Usa la API de Cumplimiento y las plataformas de
  informes de Codex para los eventos y productos que cubren según su documentación; revisa los
  esquemas actuales antes de afirmar que cubren determinados prompts, archivos,
  aprobaciones, acciones, errores o llamadas a herramientas. Consulta
[Gobernanza](/es-419/codex/enterprise/governance).

## Acceso, datos, sistemas y acciones de los usuarios

### ¿Cómo se protegen el acceso a los datos y sistemas, así como las acciones de los usuarios?

ChatGPT Work se rige por los controles de identidad, acceso y permisos ya
establecidos en tu espacio de trabajo de ChatGPT. Los administradores usan la gestión de identidades,
los roles del espacio de trabajo y, en los planes que reúnen los requisitos, el
[RBAC](https://help.openai.com/en/articles/11750701-rbac) para determinar quién puede
usar ChatGPT Work.

Cuando se admite, el acceso puede sincronizarse con tu proveedor de identidad mediante
[SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
y la sincronización de grupos. Así puedes gestionar el acceso y los permisos de forma centralizada
a medida que los empleados se incorporan a la organización, cambian de rol o se van.

Los sistemas de origen subyacentes aplican los permisos de la cuenta o de la conexión
compartida aprobada que se utiliza para la operación. Una conexión individual usa los
permisos de acceso de esa persona al sistema de origen. Una conexión compartida o perteneciente a un agente puede conceder
a los usuarios autorizados del agente acceso mediante la cuenta conectada, incluso a datos o
acciones a los que no podrían acceder desde sus propias cuentas. Limita los alcances de la conexión,
las acciones disponibles y el público del agente a lo que requiera el uso empresarial previsto. Consulta
[Conexiones y permisos de los agentes del espacio de trabajo](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business).

<a id="how-does-work-access-data-and-context"></a>
<a id="how-does-work-mode-access-data-and-context"></a>

### ¿Cómo accede ChatGPT Work a los datos y al contexto?

ChatGPT Work puede usar el chat actual, los archivos cargados, los recursos del espacio de trabajo y los
sistemas conectados mediante apps aprobadas y, cuando corresponda, complementos.
Según las capacidades y los permisos habilitados, esto puede incluir documentos,
repositorios, tickets, canales, correo electrónico y calendarios. Los archivos anteriores pueden estar
disponibles a través del chat actual, los proyectos compatibles, el acceso autorizado a la Biblioteca
o las referencias automáticas a la Biblioteca, si están habilitadas. Las memorias guardadas se rigen por sus propios
controles del espacio de trabajo y del usuario.

Cada fuente de contexto conserva sus propios controles: los usuarios aportan el contexto del chat,
los administradores gestionan los recursos del espacio de trabajo y los sistemas conectados aplican la autenticación
y los permisos. ChatGPT Work solo puede acceder a la información autorizada para el usuario o para una
conexión compartida aprobada.

ChatGPT Work hereda las protecciones aplicables del espacio de trabajo de ChatGPT. La residencia, la retención,
el registro y la disponibilidad de funciones varían según el plan, la región, la plataforma y el sistema
conectado, así que confirma la cobertura de tu configuración.

### ¿Qué acciones de alto impacto están restringidas o requieren revisión?

El riesgo varía según la acción. Por lo general, leer o preparar borradores tiene menos impacto que modificar
datos, compartir información o actuar en sistemas externos. Combina roles, permisos y credenciales de
alcance restringido, y los mecanismos de aprobación disponibles para limitar las acciones de mayor impacto
a usos confiables y sujetos a revisión.

Las categorías habituales de acciones incluyen:

- **Lectura:** acceder, buscar o resumir información de fuentes aprobadas
  sin modificar los datos subyacentes.
- **Creación de borradores:** preparar documentos, correos electrónicos, informes, código u otro contenido para que una
  persona lo revise antes de usarlo.
- **Escritura:** crear, actualizar o eliminar registros en sistemas conectados, como
  documentos, tickets, repositorios o herramientas de gestión de proyectos.
- **Uso compartido:** enviar, publicar o poner información a disposición de más
  personas, sistemas o destinos externos de cualquier otra forma.
- **Programación:** iniciar una tarea en el futuro o según una programación recurrente
  sin que un usuario tenga que iniciar cada ejecución.
- **Ejecución:** ejecutar código, comandos de shell, automatización del navegador u otras
  tareas controladas por herramientas que interactúen directamente con entornos externos.

Para las acciones de mayor impacto, usa revisión humana, credenciales restringidas, alcances
limitados y los mecanismos de aprobación disponibles. Las acciones de los complementos siguen sujetas a los permisos
y controles de seguridad de cada integración.

## Cumplimiento

<a id="how-does-work-support-enterprise-privacy-and-data-commitments"></a>
<a id="how-does-work-mode-support-enterprise-privacy-and-data-commitments"></a>

### ¿Cómo respalda ChatGPT Work los compromisos de privacidad y datos para empresas?

ChatGPT Work se rige por los compromisos de privacidad, seguridad y datos aplicables al
espacio de trabajo de ChatGPT del cliente, según el plan, la configuración, la plataforma, la función
y la región. Para ChatGPT Enterprise, esto incluye
[no usar datos empresariales para el entrenamiento de forma predeterminada](https://help.openai.com/en/articles/8983130-what-if-i-want-to-keep-my-history-on-but-disable-model-training),
cifrado en tránsito y en reposo, controles de acceso a nivel del espacio de trabajo y
las funciones de registro de auditoría disponibles.

La cobertura de la residencia de datos, la residencia de inferencia, HIPAA o un acuerdo de
asociado comercial no es universal. Confirma la
[guía vigente sobre residencia de datos y de inferencia](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)
y el acuerdo del cliente para las funciones y regiones en uso.

Los servicios conectados tienen sus propios requisitos de retención, registro, acceso, residencia y
cumplimiento. Cuando ChatGPT Work usa complementos, repositorios o sistemas de terceros,
evalúa tanto los controles del espacio de trabajo de ChatGPT como los del sistema
conectado.

Para la actividad de Codex, los controles empresariales pueden extenderse a los entornos de desarrollo,
los repositorios, las herramientas configuradas y la actividad relacionada. Revisa la
[Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup) y
[Gobernanza](/es-419/codex/enterprise/governance) junto con los controles del espacio de trabajo.

### ¿Qué datos se almacenan, se conservan o se eliminan?

La retención y eliminación de datos de ChatGPT Work se rigen por el plan del espacio de trabajo
de ChatGPT, la configuración administrativa y las capacidades en uso. La retención puede variar
según la información a la que accede ChatGPT Work. Las conversaciones y los archivos de la Biblioteca
que reúnen los requisitos siguen la configuración aplicable del espacio de trabajo. Los archivos de proyectos, las
cargas temporales, las memorias guardadas, los eventos de cumplimiento, los datos sincronizados de apps y los
registros de terceros pueden tener reglas independientes de retención y eliminación. Consulta
[Políticas de retención de chats y archivos](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt).

ChatGPT Work puede crear contenido de chats, archivos cargados o generados, artefactos
y metadatos de ejecución. Los chats de Codex también pueden crear metadatos del repositorio o del entorno,
salidas de comandos, diffs y registros. Consulta la documentación actual del producto y de la
[API de Cumplimiento](/es-419/codex/enterprise/compliance-api) para conocer con exactitud las
clases de datos, los periodos de retención y las vías de eliminación.

Revisa los requisitos de retención tanto del espacio de trabajo de ChatGPT como de los sistemas empresariales
conectados para que las políticas de gobernanza de datos, cumplimiento y
retención de registros de tu organización se apliquen a cada sistema.

## Observabilidad

### ¿Qué datos de uso están disponibles para administradores o propietarios?

Los administradores y propietarios pueden usar la analítica de productos y los registros de cumplimiento para obtener visibilidad sobre distintos
aspectos. La Consola de administración global ofrece las vistas disponibles de adopción y uso de créditos de ChatGPT y
Codex; los desgloses disponibles por usuario, producto, agente y modelo
dependen de la plataforma de analítica y del espacio de trabajo. Para los espacios de trabajo que reúnen los
requisitos, la API de Cumplimiento proporciona registros de conversaciones de ChatGPT dentro de su cobertura,
incluida la actividad de Work en la nube que admite. La cobertura depende del producto,
la plataforma, los permisos, el punto de acceso disponible y el esquema de eventos documentado. Consulta
[Analítica del espacio de trabajo](/es-419/codex/enterprise/workspace-analytics) y la
[API de Cumplimiento](/es-419/codex/enterprise/compliance-api).

### ¿Se registran los prompts, los resultados, los archivos, las acciones o las llamadas a herramientas?

Para los espacios de trabajo Enterprise y Edu que reúnen los requisitos, la Plataforma de registros de cumplimiento
proporciona los prompts de los usuarios de Work y las respuestas de los agentes.
[Las llamadas a las apps conectadas se registran por separado](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business),
y los espacios de trabajo que reúnen los requisitos pueden acceder a archivos activos de la Biblioteca mediante los
[puntos de acceso disponibles de la API de Cumplimiento específicos de la Biblioteca](https://help.openai.com/en/articles/20001052-library-for-chatgpt).
Estos registros no constituyen una pista de auditoría completa de cada operación con archivos en el entorno alojado,
comando de shell, interacción con el navegador, invocación de herramientas o aprobación.
Confirma la cobertura actual de eventos y productos en la documentación de la API de Cumplimiento
que requiere autenticación.

La Plataforma de registros de cumplimiento conserva los datos durante 30 días. Exporta los registros
de forma continua a un sistema aprobado de descubrimiento electrónico, prevención de pérdida de datos, SIEM
o lago de datos cuando tu organización requiera una retención más prolongada. Consulta la
[guía de la Plataforma de cumplimiento de OpenAI](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

### ¿Es posible detectar rápidamente comportamientos inusuales, fallas o picos de uso?

La analítica del espacio de trabajo, los registros de cumplimiento y las herramientas de monitoreo conectadas ayudan a
los administradores a revisar el uso e investigar la actividad de ChatGPT, Work y Codex incluida en su cobertura.
Según la plataforma de informes seleccionada, las señales pueden incluir usuarios activos,
mensajes incluidos en la cobertura, actividad de apps, uso de agentes, eventos de autenticación o
administrativos y consumo de créditos. Los registros exportados pueden facilitar el
descubrimiento electrónico, la prevención de pérdida de datos, los sistemas SIEM, las auditorías y las investigaciones.
La calidad de la detección depende del plan, la cobertura de eventos, la atribución, la actualidad de los datos y
las reglas configuradas.

Entre las señales que pueden ameritar una revisión se incluyen aumentos inesperados del uso o del consumo de
créditos, actividad inusual de usuarios o agentes, errores operativos recurrentes y
eventos de autenticación o administrativos relevantes. Verifica las señales exactas
con los esquemas aplicables de analítica, cumplimiento y registros de auditoría.

Para la actividad de Codex, la analítica de Codex y la Analytics API proporcionan las métricas disponibles
de adopción y actividad. Las organizaciones que usan clientes locales de Codex pueden optar
por habilitar las exportaciones de OpenTelemetry para eventos como solicitudes a la API, errores, metadatos de prompts,
decisiones de aprobación de herramientas y resultados de herramientas. El contenido de los prompts se
oculta, salvo que `otel.log_user_prompt = true` se habilite de forma explícita
e independiente. Consulta
[Monitoreo y telemetría](/es-419/codex/agent-approvals-security#monitoring-and-telemetry).
Esta telemetría local de Codex no ofrece una exportación de OpenTelemetry para ChatGPT Work
en la web.

## Gobernanza

### ¿Cómo pueden los administradores controlar el acceso, los permisos y las políticas?

La gobernanza abarca tres capas relacionadas, pero independientes:

- **Los controles de acceso de ChatGPT Work** determinan quién puede usar ChatGPT Work en
  cada plataforma.
- **Los controles de los agentes del espacio de trabajo** determinan quién puede crear, publicar, compartir,
  programar o configurar agentes reutilizables y conexiones compartidas, cuando
  los agentes del espacio de trabajo están disponibles.
- **La configuración administrada de Codex** rige el comportamiento del entorno de ejecución local de Codex dentro de su alcance
  y no configura la versión alojada de ChatGPT Work.

La configuración administrada impone límites al comportamiento del entorno de ejecución en los aspectos que admite. No concede acceso al
espacio de trabajo, no sustituye el RBAC ni revoca el acceso de un usuario al espacio de trabajo. Estas
capas no constituyen una interfaz uniforme de políticas de ChatGPT Work. La analítica y los registros de cumplimiento
ofrecen visibilidad adicional dentro de los alcances documentados de productos y
eventos.

Para los clientes locales compatibles de Codex, los administradores empresariales pueden aplicar
[configuración administrada](/es-419/codex/enterprise/managed-configuration) y
[perfiles de permisos](/es-419/codex/permissions). Estos controles de los clientes locales no
otorgan acceso a ChatGPT Work alojado ni reemplazan los permisos del espacio de trabajo que lo rigen.

### ¿Se puede limitar el acceso por grupo, rol, espacio de trabajo o capacidad?

Sí. En los planes Enterprise y Edu elegibles que admiten RBAC personalizado para miembros,
las capacidades de ChatGPT Work pueden limitarse mediante roles del espacio de trabajo, grupos de identidad
y permisos definidos por los administradores. ChatGPT Business utiliza los controles
aplicables al espacio de trabajo, pero no incluye RBAC personalizado para miembros ni sincronización
de grupos mediante SCIM. Asigna las capacidades compatibles según las necesidades empresariales
y la política de la organización. Consulta la
[guía de RBAC](https://help.openai.com/en/articles/11750701-rbac) y esta
[guía paso a paso de RBAC](https://vimeo.com/1207482321/d1286e4467?share=copy&fl=sv&fe=ci).

Cuando el RBAC personalizado está disponible, las organizaciones pueden usarlo para determinar qué
usuarios pueden acceder a ChatGPT Work, administrar la configuración del espacio de trabajo, configurar
complementos aprobados o usar funciones compatibles de los agentes del espacio de trabajo. En los espacios
de trabajo Enterprise y Edu elegibles, los límites mensuales de uso pueden facilitar una implementación
gradual mediante un límite predeterminado para el espacio de trabajo, límites predeterminados para los grupos y excepciones por usuario.

El acceso a los sistemas conectados se rige de forma independiente. Limita el acceso a los complementos, las credenciales
compartidas, los repositorios y las acciones con capacidad de escritura al conjunto mínimo necesario
de usuarios mediante los permisos del espacio de trabajo, la configuración de los complementos y los controles
del sistema de origen. En los clientes locales compatibles de Codex, la configuración administrada puede
restringir aún más las capacidades del entorno de ejecución local. Work alojado se rige por sus propios controles
del espacio de trabajo y específicos del producto.

### ¿Cómo se controlan los límites del entorno de ejecución y de la red?

Los límites de seguridad de ChatGPT Work dependen de la tarea. Una conversación estándar de Chat, un
flujo de trabajo conectado, una tarea programada y un chat de Codex pueden ejecutarse en distintos
entornos, con diferentes permisos, herramientas y acceso a la red.

Administra cada entorno de ejecución mediante los controles que le correspondan. Work Cloud
rige Work alojado en las plataformas web, móviles y de escritorio compatibles. Work Local
rige Work local en la aplicación de escritorio, y Codex Local controla el acceso local compatible
a Codex en los clientes de escritorio, CLI e IDE. Los permisos de red del navegador y del shell
restringen aún más Work Cloud. La búsqueda, las apps, los complementos, los agentes del espacio
de trabajo disponibles y los permisos del sistema de origen siguen siendo controles independientes.
La configuración administrada y las políticas de ejecución local aplicables solo rigen
las experiencias locales compatibles. Estos controles no son intercambiables.

Para la actividad de Codex, las ejecuciones locales en la aplicación de escritorio de ChatGPT, la CLI y el IDE se realizan
en el equipo del usuario con aislamiento mediante el sandbox del sistema operativo y políticas de aprobación.
Codex Cloud ejecuta chats en entornos aislados administrados por OpenAI. En los clientes locales
compatibles, los administradores empresariales pueden usar requisitos administrados para restringir
los perfiles de permisos, las aprobaciones, el acceso al sistema de archivos y a la red, los servidores MCP,
los hooks, las reglas de comandos y otros comportamientos compatibles del entorno de ejecución.

## Uso y costos

<a id="how-does-work-usage-translate-into-spend-over-time"></a>
<a id="how-does-work-mode-usage-translate-into-spend-over-time"></a>

### ¿Cómo se refleja el uso de ChatGPT Work en el gasto a lo largo del tiempo?

[ChatGPT Work y Codex comparten los precios, los créditos y los límites de uso](/es-419/codex/pricing).
En los acuerdos basados en créditos que cumplan los requisitos, compara el uso combinado de Chat y Work
de los empleados con los créditos compartidos asignados al espacio de trabajo. El consumo varía según
el modelo, la configuración de razonamiento o velocidad que corresponda, las entradas y salidas procesadas
y las herramientas o funciones elegibles.

Usar los créditos contratados no aumenta automáticamente el importe de tu factura. Los cargos reales
dependen del saldo de créditos restante, las tarifas contratadas, si la cuenta admite
consumo excedente y el límite de excedentes configurado para el espacio de trabajo. Consulta ejemplos de planificación,
los límites efectivos por usuario, el alcance de los informes y los detalles de facturación
en [ChatGPT Work: uso y costos](/es-419/codex/enterprise/chatgpt-work-usage-and-cost).

Los patrones con mayor variación suelen corresponder a flujos de trabajo que se ejecutan con frecuencia,
recuperan o procesan grandes cantidades de información, llaman a varias herramientas o apps,
vuelven a intentarlo tras una falla o generan artefactos de gran tamaño. Entre los casos que requieren
especial atención a los costos se incluyen las tareas programadas o recurrentes, los archivos grandes,
la recuperación amplia de información de fuentes empresariales, las llamadas repetidas a apps y los chats
de Codex que procesan repositorios, ejecutan comandos o usan entornos en la nube. Cuando están disponibles,
los activadores de la API de los agentes del espacio de trabajo también pueden aumentar el consumo.

Usa controles de gasto, analítica de uso e informes para supervisar estos patrones
a lo largo del tiempo. Revisa el uso según las dimensiones disponibles en la interfaz actual de analítica
y ajusta los límites o el alcance de la implementación según el valor para la empresa. No interpretes
la analítica agregada como una atribución exacta de costos por flujo de trabajo.

La analítica del espacio de trabajo, los registros de cumplimiento y las herramientas de supervisión conectadas pueden ayudar
a los administradores a revisar el uso e investigar la actividad que cubren. La capacidad de
detectar comportamientos riesgosos o inusuales depende del plan, la cobertura de los registros, la atribución,
la actualidad de los datos y las reglas configuradas en tus sistemas de supervisión.

### ¿Qué límites de uso, alertas o topes están disponibles?

Los espacios de trabajo Enterprise y Edu elegibles pueden usar límites mensuales por usuario y
controles de gasto para todo el espacio de trabajo para el uso basado en créditos:

- **Supervisa el consumo de créditos:** revisa los informes disponibles sobre el uso de créditos en la
  Consola de administración global y en la configuración del espacio de trabajo.
- **Establece un límite mensual predeterminado:** define un límite de créditos predeterminado por usuario
  para el espacio de trabajo.
- **Aplica límites específicos para cada grupo:** asigna a los grupos límites mensuales predeterminados por usuario que
  reflejen sus flujos de trabajo, responsabilidades o etapa de implementación.
- **Crea excepciones por usuario:** asigna un límite diferente a un usuario específico sin
  cambiar el límite predeterminado de todo el grupo.
- **Revisa las solicitudes de aumento:** si las solicitudes están habilitadas, los usuarios pueden pedir un
  límite mensual mayor. La aprobación crea una excepción para ese usuario.
- **Controla la exposición financiera total del espacio de trabajo:** configura por separado las alertas de créditos del espacio de trabajo y
  el límite de excedentes en la Consola de administración global. Las alertas notifican a
  los destinatarios; el límite de excedentes controla el uso elegible una vez que se agota
  la reserva de créditos contratados.
- **Exporta los datos de uso:** los administradores de Enterprise que cumplen los requisitos pueden acceder
  a los datos sobre el uso de créditos mediante la Cost API unificada para generar informes internos o realizar tareas de
  supervisión.

Los usuarios pueden ver su propio uso y, si esta opción está habilitada, solicitar más créditos, pero
no pueden cambiar los límites asignados. Consulta
[Administrar los límites de uso y los excedentes](https://help.openai.com/en/articles/20001001-manage-usage-limits-and-overages-in-chatgpt-enterprise-and-edu)
y la
[guía paso a paso de los controles de gasto](https://vimeo.com/1207484127/0f2029dd01?share=copy&fl=sv&fe=ci).

## Controles de incidentes y revocación

### ¿Cómo pueden los administradores interrumpir el acceso o la actividad?

Durante la baja de un usuario o la revisión de un incidente, es posible que los administradores deban interrumpir el acceso,
deshabilitar apps, revocar credenciales compartidas, pausar tareas programadas o revocar credenciales
de Codex.

Las opciones de revocación incluyen:

- Quita a un usuario el acceso al espacio de trabajo o al grupo. Para los usuarios administrados mediante SCIM, quita
el acceso en el proveedor de identidad; de lo contrario, una sincronización posterior puede
volver a aprovisionar al usuario.
- Deshabilita o restringe el complemento o la app correspondiente.
- Revoca una conexión compartida, un bot o una cuenta de servicio desde la interfaz
que los administra. Los propietarios y administradores del espacio de trabajo pueden revocar por separado
los tokens de acceso de Codex al espacio de trabajo.
- Anula la publicación de un agente del espacio de trabajo o elimínalo a través de su propietario
o del administrador del espacio de trabajo.
- Deshabilita la tarea programada correspondiente o, cuando esté disponible, el activador de la API
de los agentes del espacio de trabajo.
- Para el acceso a Codex, revoca por separado el token de acceso, la conexión al repositorio
y el acceso al entorno en la nube correspondientes. La configuración administrada no es un
mecanismo de revocación del acceso.

## Recursos adicionales para tus equipos

| Tema                    | Úsalo para explicar                                                      | Página de aprendizaje de ChatGPT                                               |
| ------------------------ | ----------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Descripción general de Work            | Cómo funcionan la ejecución en la nube, el acceso al navegador, la política de red y los límites aplicables a los datos | [Descripción general de ChatGPT Work](/es-419/codex/enterprise/chatgpt-work-overview) |
| Configuración del espacio de trabajo y RBAC | Quién puede usar y administrar Codex                                              | [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)             |
| Autenticación           | En qué se diferencian el inicio de sesión con ChatGPT, el inicio de sesión con una clave de API y la política del espacio de trabajo             | [Autenticación](/es-419/codex/auth)                                    |
| Aprobaciones y entorno aislado | Cómo controla Codex las operaciones con archivos, la ejecución de comandos, el acceso a la red y las acciones de herramientas con efectos secundarios    | [Aprobaciones y seguridad del agente](/es-419/codex/agent-approvals-security)  |
| Política administrada           | Cómo aplican los administradores configuraciones de Codex que los usuarios no pueden anular                        | [Configuración administrada](/es-419/codex/enterprise/managed-configuration) |
| Entornos de ejecución     | Cómo funcionan la configuración de Codex Cloud, los secretos, las cachés y las fases de las tareas                  | [Entornos en la nube](/es-419/codex/environments/cloud-environment)      |
| Acceso a Internet          | Cómo funcionan las listas de dominios permitidos y los métodos HTTP de Codex Cloud                       | [Acceso del agente a Internet](/es-419/codex/cloud/internet-access)            |
| Permisos              | Cómo funcionan los controles del sistema de archivos, de red y de denegación de lectura                          | [Permisos](/es-419/codex/permissions)                                |
| Observabilidad            | Cómo funcionan los análisis, los informes y las exportaciones de cumplimiento                         | [Gobernanza](/es-419/codex/enterprise/governance)                       |
| Credenciales de automatización   | Cómo se crean, limitan, revocan y auditan los tokens de acceso                  | [Tokens de acceso](/es-419/codex/enterprise/access-tokens)                 |

## Acciones recomendadas para administradores

- **Confirma quién debe tener acceso primero.** Decide si restringir el acceso a
  ChatGPT Work, realizar una prueba piloto o implementarlo de forma generalizada. Muchas organizaciones comienzan
  con usuarios avanzados, embajadores o equipos con casos de uso claros.
- **Revisa los roles y permisos.** En **Permisos y roles**, confirma qué
  usuarios o grupos pueden acceder a ChatGPT Work. Ajusta el acceso a las necesidades del negocio, al nivel de preparación
  y a las expectativas de gobernanza.
- **Revisa los complementos y las fuentes de datos.** ChatGPT Work resulta más útil con
  contexto empresarial aprobado, como archivos, correo electrónico, calendarios, Slack o CRM. Revisa
  los complementos habilitados, a quiénes están dirigidos y si las políticas de las aplicaciones siguen ajustándose a la forma en que los usuarios
  deben delegar el trabajo.
- **Establece expectativas sobre los casos de uso adecuados.** Orienta el uso de ChatGPT Work hacia tareas de varios pasos y
  de mayor valor, como investigación, síntesis, análisis, creación de archivos,
  actualizaciones de flujos de trabajo y resultados reutilizables. Usa Chat para preguntas rápidas,
  pequeños ajustes de redacción o lluvias de ideas.
- **Revisa los controles de créditos y uso.** Como ChatGPT Work puede realizar
  tareas de mayor duración, puede consumir más créditos que una conversación estándar de Chat. Revisa
  los valores predeterminados generales y por grupo, las excepciones por usuario y las pautas internas para
  ajustar el esfuerzo al valor para el negocio.
- **Identifica tus primeros flujos de trabajo de alto valor.** Comienza con resultados claros y revisables,
  como presentaciones informativas para clientes, informes periódicos, síntesis de investigaciones,
  actualizaciones de herramientas de seguimiento o documentos y diapositivas bien elaborados.
- **Prepara a los embajadores y a los equipos de soporte.** Proporciona primero los recursos de implementación a los embajadores, a los responsables de capacitación
  y a los equipos de soporte para que puedan responder preguntas,
  recopilar comentarios y mostrar cómo delegar de forma eficaz.
- **Comunica las expectativas de revisión y aprobación.** Recuerda a los usuarios que las personas
  siguen siendo responsables de revisar los resultados, validar las afirmaciones importantes y
  aprobar las acciones de gran impacto antes de que los resultados se compartan o utilicen.
- **Supervisa la adopción y realiza ajustes.** Revisa el uso, los comentarios, el consumo de créditos
  y el trabajo delegado después de la implementación. Usa la información obtenida para ajustar el acceso,
  las pautas, la capacitación y la ampliación.
