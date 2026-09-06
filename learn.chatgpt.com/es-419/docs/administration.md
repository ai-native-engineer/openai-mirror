<!-- source: https://learn.chatgpt.com/es-419/docs/administration -->

# Administración

Define los límites de acceso y el alcance de las políticas para ChatGPT, las herramientas para desarrolladores de Codex, las API, los complementos y los sistemas conectados

Define los límites de acceso y el alcance de las políticas para ChatGPT, las herramientas para desarrolladores de Codex, las API, los complementos y los sistemas conectados.

La administración abarca seis ámbitos de control relacionados: el acceso al espacio de trabajo de ChatGPT; la política del entorno de ejecución local para las capacidades contempladas en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE; la elegibilidad para usar Codex Cloud; el acceso a la API de la plataforma; la disponibilidad de complementos y los permisos de los conectores; y los permisos en los sistemas conectados. Comienza por la identidad y el acceso en el espacio de trabajo y luego aplica los controles del entorno de ejecución y de los sistemas de origen necesarios para cada implementación.

Explorar la autenticación

Miembros, grupos, tokens de acceso y controles de roles del espacio de trabajo de ChatGPT

Primeros pasos

Comienza con la guía de implementación y luego consulta las páginas de referencia de cada ámbito de control.

Guía de implementación para administradores

Planifica el acceso, asigna responsables, configura los controles y verifica la implementación.

ChatGPT Work

Revisa la descripción general de ChatGPT Work y la documentación de referencia sobre su administración.

Descripción general de ChatGPT Work

Comprende la ejecución en entornos alojados, los controles de red, los límites aplicables a los datos y la visibilidad para auditorías.

Seguridad de ChatGPT Work en la nube

Revisa la ejecución en entornos alojados, las cuentas conectadas, los controles de acceso, la retención y la visibilidad para auditorías.

Seguridad local de ChatGPT Work

Revisa la ejecución local, el acceso al dispositivo y al navegador, las políticas administradas, el manejo de datos y las limitaciones de auditoría.

Preguntas frecuentes sobre la administración de ChatGPT Work

Revisa los controles de ChatGPT Work relacionados con el acceso, los datos, la gobernanza, el uso y los incidentes.

ChatGPT Work: uso y costo

Comprende los créditos compartidos, el impacto en la facturación, los controles de gasto y la planificación de la adopción.

Identidad y autenticación

Elige cómo iniciarán sesión las personas y emite credenciales para flujos de trabajo programáticos.

Descripción general de la autenticación

Compara los métodos de inicio de sesión, el almacenamiento de credenciales y los controles de aplicación de políticas.

Identidad de carga de trabajo

Permite que las cargas de trabajo de confianza usen Codex sin credenciales de larga duración.

Tokens de acceso personal

Crea y administra tokens para el acceso programático.

Cuentas de servicio

Crea y administra identidades del espacio de trabajo para flujos de trabajo automatizados.

Acceso, políticas y modelos del espacio de trabajo

Asigna el acceso al espacio de trabajo de ChatGPT y mantenlo separado de la política del entorno de ejecución local, del acceso a Codex Cloud y del acceso a la API de la plataforma.

Grupos y aprovisionamiento

Administra los grupos gestionados manualmente y mediante SCIM, el aprovisionamiento y las cohortes de implementación.

Gestión del ciclo de vida de los usuarios

Da de alta a los empleados, actualiza el acceso de los grupos y revoca las credenciales de los usuarios que dejen la organización.

Roles y permisos del espacio de trabajo

Usa el mapa de referencia de los controles del espacio de trabajo, del entorno de ejecución, de la API, de los complementos y de los sistemas de origen.

GPTs y uso compartido

Administra el uso compartido y la propiedad de los GPT, las apps conectadas y las acciones de terceros en todo tu espacio de trabajo.

Configuración administrada

Distribuye la configuración administrada donde se admita y exige el cumplimiento de los requisitos del entorno de ejecución para las capacidades contempladas en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE.

Prisma AIRS

Aplica a los prompts de Codex políticas de seguridad para todo el espacio de trabajo.

Configuración para HIPAA

Configura medidas de protección del entorno de ejecución local para flujos de trabajo que puedan manejar información médica protegida.

Disponibilidad de modelos en el espacio de trabajo

Administra por separado el acceso a los modelos en ChatGPT, en Codex dentro de la aplicación de escritorio de ChatGPT, en Codex CLI, en la extensión para IDE, en Codex Cloud y en la API de la plataforma.

Controles de complementos y conectores

Controla la instalación de complementos, las habilidades incluidas, las capacidades basadas en conectores y el acceso a los servicios conectados.

Controles de complementos

Administra la disponibilidad de los complementos, el acceso y las acciones de los conectores, así como los permisos de los sistemas de origen.

Administración de complementos

Importa y sincroniza complementos del espacio de trabajo desde GitHub.

Controles de habilidades

Compara los controles de habilidades del espacio de trabajo de ChatGPT, del sistema de archivos local y de los complementos.

Uso, gobernanza y cumplimiento

Mide la adopción y dirige los datos de informes o auditorías al sistema responsable de gestionarlos.

Gobernanza

Elige el recurso de analítica, gastos o auditoría adecuado para cada pregunta.

Complemento de administración

Usa el complemento de administración para permisos, aprobaciones y flujos de trabajo administrativos compatibles.

Analítica del espacio de trabajo

Revisa la adopción de ChatGPT y el uso de Codex en el espacio de trabajo.

API de análisis

Automatiza la generación de informes sobre la actividad de los desarrolladores y la revisión de código con la API de análisis de Codex.

API de Cumplimiento y eventos de auditoría

Exporta registros de actividad para flujos de trabajo de auditoría e investigación.

Implementación y proveedores de modelos

Implementa y actualiza apps de escritorio, conecta hosts administrados o configura un proveedor externo de modelos compatible.

Administrar las actualizaciones de la aplicación

Controla las actualizaciones de la app de escritorio e implementa versiones aprobadas a través de tu plataforma de administración de dispositivos.

Implementación de la aplicación de Windows

Elige un método de instalación y actualización para dispositivos Windows administrados.

Conexiones remotas

Inicia y controla el trabajo en computadoras conectadas.

Amazon Bedrock

Configura los clientes locales compatibles para usar los modelos disponibles a través de Bedrock.
