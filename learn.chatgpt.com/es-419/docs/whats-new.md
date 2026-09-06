<!-- source: https://learn.chatgpt.com/es-419/docs/whats-new -->

Este resumen semanal destaca las funciones de ChatGPT y Codex que pueden cambiar tu forma de
trabajar, con ejemplos y enlaces para obtener más información. Para ver todas las actualizaciones de cada versión, las correcciones de errores
y las mejoras menores, consulta el [registro de cambios de Codex](/codex/changelog).

## 31 de agosto–4 de septiembre de 2026

### Aborda tareas exigentes con GPT-6 Astra

[GPT-6 Astra](/es-419/codex/models#gpt-6-astra) combina razonamiento avanzado, uso de la computadora
y un mejor criterio para realizar tareas complejas con código, apps e investigación en
Codex y ChatGPT Work. Úsalo para ejecutar un flujo de trabajo, verificar el resultado y
crear un documento, una hoja de cálculo o una presentación que se ajuste a tus plantillas y
a tu tarea.

Cuando Astra esté disponible en tu cuenta, elígelo en el selector de modelos.
Consulta el [uso y los precios](/es-419/codex/pricing) antes de iniciar una tarea de gran alcance.
El acceso en Enterprise requiere tanto cumplir los requisitos del lanzamiento gradual como que un administrador
lo habilite.

## 24–28 de agosto de 2026

### Trabaja con más sitios web

- **Usa tu navegador:** trabaja en [Edge, Brave, Opera o Vivaldi](/es-419/codex/chrome-extension)
  además de Chrome desde la aplicación de escritorio de ChatGPT. Incorpora una pestaña abierta a un
  chat de ChatGPT Work o Codex y trabaja con el sitio web en el que ya tienes
  la sesión iniciada. Opera admite el control del navegador, pero no tiene chat lateral.

- **Usa las herramientas de un sitio web:** con las [herramientas del sitio (WebMCP)](/es-419/codex/webmcp),
  ChatGPT Work y Codex pueden usar acciones que ofrece un sitio web desde el navegador
  integrado de la aplicación de escritorio. Por ejemplo, un editor de documentos puede ofrecer herramientas para encontrar
  una sección o agregar un comentario. Actualiza la aplicación de escritorio y usa GPT-5.6 Sol o
  GPT-5.6 Terra. Las herramientas del sitio no están disponibles con GPT-5.6 Luna ni en espacios de trabajo Enterprise
  o Edu.

- **Inicia sesión a través del navegador en la nube:** en los planes elegibles, continúa una tarea
  que requiera una cuenta de un sitio web en ChatGPT Work en la web, iOS o Android.
  Sigue la [solicitud de inicio de sesión](/es-419/codex/browser?surface=web#web-sign-in-to-a-website)
  e ingresa tus datos en el flujo de inicio de sesión, no en el chat. Esto no
  conecta tu perfil de navegador local. El inicio de sesión en sitios web no está disponible para
  los espacios de trabajo Enterprise o Edu.

La disponibilidad depende del lanzamiento gradual y de la configuración del espacio de trabajo.

[Lee las notas de la versión del navegador del 25 de
agosto](/codex/changelog#codex-2026-08-25-browser).

### Ejecuta tareas programadas a partir de eventos de apps

Las [tareas programadas](/es-419/codex/automations?surface=web#web-trigger-tasks-from-app-events) ahora pueden
iniciarse cuando ocurre un evento compatible en Gmail, Slack o GitHub. Usa un disparador de
eventos para clasificar los correos nuevos, resumir la actividad de un canal o atender los comentarios de los pull requests
sin hacer consultas a intervalos fijos.

Las tareas activadas por eventos están disponibles en ChatGPT en la web y en dispositivos móviles para
los planes elegibles. Primero, conecta la app correspondiente y aprueba el acceso que solicita. En los espacios de trabajo
administrados, los administradores pueden controlar el acceso.

<PromptComponent
  prompt={`Cuando uno de mis pull requests en <owner>/<repository> reciba nuevos comentarios de revisión, resume los comentarios y prepara un plan de cambios.`}
/>

[Lee las notas de la versión del 25 de
agosto](/codex/changelog#codex-2026-08-25-event-triggers).

## 17–21 de agosto de 2026

### Trabaja con más de tus apps y contenido

- **Apple Messages:** [busca chats, resume mensajes, prepara respuestas y envíalas a través de Messages en tu Mac](/es-419/codex/plugins?surface=app#app-use-apple-messages-from-codex). El complemento está disponible en todos los planes en la aplicación de escritorio de ChatGPT para macOS. Úsalo en ChatGPT Work y Codex, no en los chats habituales de ChatGPT. De forma predeterminada, ChatGPT solo envía mensajes después de que apruebes el mensaje y sus destinatarios.

- **Coedición de Sites:** cuando esté disponible, [invita como editores a miembros activos de tu espacio de trabajo](/es-419/codex/sites#collaborate-on-a-site). Los editores pueden mejorar el Site y publicar actualizaciones después de que su propietario lo publique por primera vez. Los editores invitados pueden leer los datos de la base de datos activa del Site; los propietarios mantienen el control de las opciones para compartir y la configuración.

- **URL editables de Sites:** cuando esté disponible, [elige una nueva dirección alojada en ChatGPT para un Site existente](/es-419/codex/sites#change-a-site-url) sin volver a desplegarlo. La dirección anterior redirige a la nueva.

- **Historial de la computadora en Europa:** usa el [Historial de la computadora](/es-419/codex/customization/computer-history) en el EEE, Suiza y el Reino Unido. Permanece desactivado de forma predeterminada para los usuarios de ChatGPT Pro, Business y Enterprise en macOS. Los administradores de Business y Enterprise primero deben habilitar el acceso.

- **Instantáneas compartidas de hilos:** [comparte una instantánea de solo lectura de un hilo local de Codex](/es-419/codex/use-chatgpt#share-a-read-only-snapshot-of-a-codex-thread) desde la aplicación de escritorio de ChatGPT para macOS. Cualquier persona que tenga un enlace de una cuenta personal puede ver la instantánea; los enlaces de cuentas de espacios de trabajo se limitan al espacio de trabajo de origen. Codex oculta los secretos que coinciden con patrones conocidos, pero revisa la instantánea antes de compartirla porque aún puede contener información confidencial.

- **Hilos fijados unificados:** mantén tus [chats fijados](/es-419/codex/projects?surface=app#app-organize-projects-and-chats) sincronizados entre la app de escritorio y iOS.

[Lee las notas de la versión del 20 de agosto](/codex/changelog#codex-2026-08-20-app).

### Trabaja con proyectos de GitLab en Codex Cloud

La [compatibilidad con GitLab](/es-419/codex/third-party/gitlab) está disponible en versión beta en todos los planes de ChatGPT.
Conecta un proyecto, crea un entorno en la nube, inicia tareas desde incidencias
o solicitudes de fusión con `@codex` y solicita revisiones puntuales o automáticas de solicitudes
de fusión.

La integración se ejecuta en Codex Cloud y un administrador de un espacio de trabajo administrado puede
desactivarla. La actividad iniciada desde GitLab requiere permiso para configurar el webhook
correspondiente. Las conexiones de GitLab Self-Managed y GitLab Dedicated deben ser configuradas por
un administrador del espacio de trabajo; la actividad de los webhooks requiere GitLab 19.0 o una versión posterior.

[Lee las notas de la versión de GitLab del 19 de
agosto](/codex/changelog#codex-2026-08-19-gitlab).

### Exporta metadatos de complementos públicos para revisarlos

Los propietarios y administradores elegibles de espacios de trabajo de ChatGPT Enterprise pueden descargar un CSV de
los complementos públicos visibles en su espacio de trabajo. En
[Administración \> Complementos](https://chatgpt.com/admin/plugins), selecciona **Públicos** y luego
selecciona el ícono de descarga (**Exportar CSV**).

La exportación incluye los nombres y las descripciones de complementos, apps y habilidades de Chat,
así como el desarrollador, la versión, la fecha de incorporación en UTC y los metadatos de verificación de OpenAI.
Usa una instantánea del catálogo público que puede tener hasta 48 horas de antigüedad y excluye
los complementos creados para el espacio de trabajo. La exportación no está disponible en espacios
de trabajo FedRAMP.

[Lee las notas de la versión de la exportación para administradores del 17 de
agosto](/codex/changelog#codex-2026-08-17-admin-csv).

## 10–14 de agosto de 2026

### Encuentra trabajos anteriores con el Historial de la computadora

El [Historial de la computadora](/es-419/codex/customization/computer-history) convierte la actividad en
tus apps y sitios web en una cronología con función de búsqueda y en memorias que ChatGPT
y Codex pueden usar. Actívalo solo si quieres compartir ese contexto; después,
elige qué apps y sitios web aportan información, pausa la recopilación y revisa o
elimina tu historial en cualquier momento.

El Historial de la computadora está disponible en la aplicación de escritorio de ChatGPT en macOS para clientes
de ChatGPT Pro, Business y Enterprise. Los administradores de Business y Enterprise primero deben
habilitar el acceso. La disponibilidad inicial excluye a la Unión Europea, Suiza y el Reino
Unido.

### Usa la aplicación de escritorio de ChatGPT en Linux

La [aplicación de escritorio de ChatGPT para Linux](/es-419/codex/linux/linux-app) ya está disponible en
versión preliminar. Instala un paquete `.deb` en las distribuciones compatibles de Ubuntu o Debian,
o un paquete `.rpm` en Fedora. Los paquetes están disponibles para procesadores x64 y
ARM64.

Inicia sesión con tu cuenta de ChatGPT para trabajar con proyectos, archivos locales y
Codex. Algunas funciones, como el Uso de la computadora, aún no están disponibles en la
versión preliminar para Linux.

### Lleva contigo tu configuración actual de agentes y tu trabajo

[Importa instrucciones, configuración, habilidades, complementos, proyectos y trabajo
reciente](/codex/import) de **Claude Code**, <strong>Claude Cowork</strong> o
**Cursor** a la aplicación de escritorio de ChatGPT. Activa las actualizaciones automáticas en
**Configuración \> Importar** para mantener sincronizado el trabajo importado.

En Codex CLI, usa `/import` para importar a tu sesión local la configuración compatible y los chats recientes de
Claude Code o Cursor.

[Lee las notas de la versión del 11 de agosto para la aplicación de escritorio
y la CLI](/codex/changelog#codex-2026-08-11-app).

### Elige el acceso adecuado para tareas de seguridad defensiva

Daybreak ahora ofrece dos niveles para profesionales de ciberdefensa aprobados. **Daybreak Blue** permite realizar
tareas generales de defensa, como la revisión de seguridad del código, la respuesta a incidentes y
la validación de parches. **Daybreak Red** requiere una aprobación independiente y ofrece
acceso a modelos entrenados específicamente para evaluaciones de seguridad autorizadas.

El acceso requiere [Trusted Access for
Cyber](/es-419/codex/cyber-safety#trusted-access-for-cyber) y solo es válido para
la identidad, el espacio de trabajo o la organización, el modelo y la interfaz del producto aprobados.

[Lee el anuncio de Daybreak del 10
de agosto](/codex/changelog#codex-2026-08-10-daybreak).

## 3–7 de agosto de 2026

### Habla sobre archivos y proyectos con ChatGPT Voz

[ChatGPT Voz](/es-419/codex/features/voice) ahora admite archivos cargados y
[Proyectos de ChatGPT](/es-419/codex/projects). Haz preguntas sobre un documento durante una
conversación de voz o continúa un proyecto usando sus chats recientes, fuentes e
instrucciones.

### Estudia y enseña con complementos especializados en educación

Tres nuevos [complementos](/es-419/codex/plugins) incorporan flujos de trabajo específicos para el aula a
ChatGPT Work y Codex. **College Student** crea guías de estudio, cuestionarios
de práctica, tarjetas de estudio y explicaciones interactivas. **College Educator** ayuda a
crear planes de curso, materiales y evaluaciones. **K–12 Educator** ayuda con
la planificación de clases, los recursos para el aula y los materiales adaptados a distintos
estudiantes.

Los complementos están disponibles a través de ChatGPT Edu y las implementaciones de ChatGPT for Teachers en distritos
escolares. Las instituciones educativas controlan qué herramientas y permisos están disponibles. Lee
el [anuncio de los complementos
educativos](https://openai.com/index/learn-teach-chatgpt-work-codex/).

### Reutiliza archivos guardados y encuentra trabajos anteriores más rápido

En la web, agrega a una conversación un archivo guardado en la Biblioteca sin volver a subirlo,
busca en la Biblioteca y pega texto con formato sin perder encabezados,
enlaces ni listas. La búsqueda también encuentra carpetas y títulos de conversaciones en la
web, iOS y Android.

El texto pegado de más de 10 000 caracteres ahora se convierte en un archivo adjunto en todos los planes de ChatGPT,
incluidos Enterprise y Edu. Selecciona **Mostrar en el campo de texto** si quieres
volver a incluir el contenido en tu mensaje.

Lee las [notas de la versión
de ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

### Consulta tu uso restante de ChatGPT Work

Los usuarios elegibles de planes personales y ChatGPT Business pueden consultar su uso restante de
ChatGPT Work directamente en la barra lateral de la versión web. Las opciones de créditos disponibles dependen
de tu cuenta y de los permisos del espacio de trabajo. ChatGPT Work y Codex siguen
compartiendo los mismos [límites de uso y créditos](/es-419/codex/pricing).

### Elige cómo responde GPT-5.6 en ChatGPT

Los usuarios de ChatGPT Plus y Pro pueden ajustar cuánto razona GPT-5.6 Sol al preparar una
respuesta con un nuevo control deslizante. El modelo actualizado también ofrece datos más confiables
y respuestas más centradas en la consulta. GPT-5.6 Luna pasa a ser el modelo predeterminado de ChatGPT en los planes Gratis
y Go.

Estos cambios se aplican a las conversaciones de ChatGPT. No cambian el comportamiento del modelo
en ChatGPT Work ni en Codex. Lee las [notas de la versión
de ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

### Organiza el trabajo y cambia de agente en Codex CLI 0.147.0

[Codex CLI 0.147.0](https://github.com/openai/codex/releases/tag/rust-v0.147.0)
agrega secciones de chat persistentes que puedes ordenar manualmente y complementos portables para agentes.
Busca en catálogos de complementos locales, personales, del espacio de trabajo y remotos, o
[importa la configuración de Cursor y Claude Code](/es-419/codex/import) sin duplicar
las conversaciones sincronizadas.

Usa `--approve-for-me` para habilitar la [revisión automática de
aprobaciones](/es-419/codex/sandboxing/auto-review) para las solicitudes elegibles sin ampliar
los permisos del sistema de archivos o de la red. Las sesiones de Amazon Bedrock también incorporan
búsqueda web con caché y compactación remota de conversaciones.

### Supervisa y reanuda análisis de seguridad más profundos

Las versiones `0.1.16` a `0.1.18` del plugin de Codex Security alojado en la nube agregan seguimiento del progreso de los análisis en tiempo real,
medición del uso de tokens, análisis profundos que se pueden reanudar y límites
de descubrimiento configurables. La versión más reciente también admite la autenticación de Amazon Bedrock
para los análisis de repositorios y sus agentes delegados.

Usa el [panel de trabajo de Codex Security](/es-419/codex/security/plugin/workbench) para revisar
el progreso de los análisis y los hallazgos, o [configura un análisis
profundo](/es-419/codex/security/plugin/deep-scans) cuando necesites una evaluación más
exhaustiva. Consulta el [registro de cambios del complemento](/es-419/codex/security/plugin/changelog) para
confirmar qué funciones admite la versión que tienes instalada.

### Revisa los pull requests de GitHub para detectar riesgos de seguridad

[Codex Security Review](/es-419/codex/security/security-review) analiza los cambios de los pull requests
junto con el contexto del repositorio, los modelos de amenazas y las pautas de seguridad.
Configura revisiones automáticas cuando se abra un pull request o reciba nuevos
commits, o solicita una directamente con `@codex security review`.

La función está disponible en versión preliminar de investigación para los clientes elegibles de ChatGPT Enterprise,
Business, Edu y Pro. No está disponible en Plus y pueden aplicarse límites
de uso.

## 27–31 de julio de 2026

### Usa GPT-5.6 Terra y Luna con tarifas más bajas

GPT-5.6 Terra ahora cuesta un 20 % menos y GPT-5.6 Luna cuesta un 80 % menos. Las tarifas de entrada,
entrada en caché y salida se redujeron en las mismas proporciones. Los nuevos
[límites de uso y tarifas](/es-419/codex/pricing) hacen que Terra sea una mejor opción para el trabajo
cotidiano y que Luna sea especialmente útil para tareas de programación específicas y tareas de gran volumen.

### Encuentra contexto útil en tu navegador y en las pestañas abiertas

En la aplicación de escritorio de ChatGPT, el [navegador integrado](/es-419/codex/browser) puede encontrar
páginas en tu historial de navegación o buscar en Google directamente desde su barra
de direcciones. ChatGPT también puede buscar en tu historial de navegación cuando una tarea necesita
contexto anterior.

La [extensión de Chrome](/es-419/codex/chrome-extension) te permite mencionar pestañas abiertas,
llevar el texto seleccionado de una página a un chat lateral, hacer preguntas sobre videos de YouTube
o seleccionar **Preguntar a ChatGPT** en el menú contextual de una página. Revisa y aprueba
las solicitudes de uso del historial de navegación antes de que ChatGPT incluya esa información en una
tarea.

### Revisa cambios en varios repositorios

Cuando un [proyecto local contiene más de una
carpeta](/es-419/codex/projects#use-local-projects-for-folders-and-codebases), la
aplicación de escritorio muestra todos los repositorios y las líneas modificadas en cada uno. Selecciona
**Revisión** para inspeccionar sus diffs juntos sin alternar entre distintas vistas
de revisión.

### Perfecciona las imágenes generadas en tu conversación

Abre una imagen generada en el visor ampliado y luego alterna entre
**Vista enfocada** y **Vista de canvas**. Agrega comentarios en las imágenes, selecciona las
versiones que quieras conservar y solicita cambios específicos sin salir del chat.
Obtén más información sobre la [generación de imágenes](/es-419/codex/image-generation).

### Encuentra chats que necesitan tu atención

La nueva **Vista de actividad** de la aplicación de escritorio reúne los chats en los que participaste
recientemente y el trabajo que necesita tu atención. Selecciona la campana en la barra lateral
para abrir la vista.

[Lee las notas de la versión de escritorio
del 30 de julio](/codex/changelog#codex-2026-07-30-app).

### Conecta herramientas de socios con Iniciar sesión con ChatGPT

La opción **Iniciar sesión con ChatGPT** se está implementando en versión beta en complementos compatibles y
sitios de socios, comenzando por Airtable, GitLab, HubSpot, Notion, Supabase y
Vercel. Úsala para crear o vincular una cuenta de un servicio asociado en menos pasos y luego empieza
a trabajar con ese servicio en ChatGPT o Codex.

Los socios reciben únicamente tu nombre, dirección de correo electrónico y foto de perfil cuando
esté disponible. El acceso que solicita cada complemento sigue requiriendo revisión
y aprobación por separado. Lee el [anuncio sobre el inicio de sesión
del 29 de julio](/codex/changelog#codex-2026-07-29).

### Colabora en un espacio de trabajo dedicado a la investigación académica

[ChatGPT for Academic Researchers](https://openai.com/index/chatgpt-for-academic-researchers/)
ofrece a docentes e investigadores posdoctorales que cumplan los requisitos 12 meses de acceso gratuito
a un espacio de trabajo dedicado de ChatGPT. Los equipos aprobados pueden incluir hasta cinco
investigadores verificados de la misma institución y reciben protecciones de datos
empresariales y límites de uso de nivel ChatGPT Pro. Los participantes pueden usar GPT-5.6
en ChatGPT, ChatGPT Work y Codex para flujos de trabajo de investigación y programación.

El programa cubre el acceso a ChatGPT, no los créditos de la API de OpenAI. Para participar, se requiere
[verificación institucional y un artículo de investigación
que cumpla los requisitos](https://help.openai.com/en/articles/20001406).

### Continúa las tareas de Codex con mayor confiabilidad en iOS

ChatGPT para iOS 1.2026.202 se reconecta a las tareas de forma más confiable cuando vuelves a
la aplicación o desbloqueas tu dispositivo con Face ID. Las conversaciones de voz usan la voz de
ChatGPT que elegiste y muestran advertencias sobre los límites de uso, mientras que el editor ahora sugiere
complementos instalados y sus habilidades de la misma manera que la aplicación de escritorio.

Esta versión también mejora los controles para pausar y reanudar objetivos, las tablas integradas
y los temas visuales, los diffs extensos del espacio de trabajo, las referencias al texto seleccionado y la restauración
del modelo. Lee las [notas de la versión de iOS
del 27 de julio](/codex/changelog#codex-2026-07-27-mobile).

### Compara análisis de seguridad y administra hallazgos

Las versiones `0.1.14` y `0.1.15` del plugin alojado de Codex Security agregan comparaciones de análisis,
comentarios sobre falsos positivos, políticas de `SECURITY.md` con alcance definido e historiales de repositorios
y hallazgos más claros. Puedes seleccionar hallazgos para darles seguimiento en Linear o en
Issues de GitHub, y Codex revisa la acción propuesta antes de que la apruebes.

Usa el [panel de trabajo de
Codex Security](/es-419/codex/security/plugin/workbench) existente para revisar los análisis guardados, los hallazgos,
el historial del repositorio y las correcciones en la aplicación de escritorio. El catálogo de complementos alojados
ofrece la versión `0.1.15`, mientras que el marketplace público de complementos de la CLI
ofrece la versión `0.1.11`. Consulta el [registro de cambios del
plugin de Codex Security](/es-419/codex/security/plugin/changelog) antes de depender de una función nueva.

### Ejecuta análisis de seguridad desde la terminal, CI o TypeScript

La CLI pública y el SDK de TypeScript de `@openai/codex-security` llegaron a la versión
`0.1.5`, con una numeración de versiones independiente de la del plugin de Codex Security. Usa el
paquete para [ejecutar análisis desde la CLI](/es-419/codex/security/cli), revisar los cambios de los pull requests
y cargar resultados SARIF en [CI](/es-419/codex/security/cli/ci), o ejecutar
[análisis masivos](/es-419/codex/security/cli/bulk-scans) que se pueden reanudar en repositorios de GitHub
o a partir de un inventario CSV fijado.

El [SDK de TypeScript de Codex Security](/es-419/codex/security/sdk) también te permite incorporar
análisis, informes de progreso, controles de costos y cancelación a tus propias
herramientas. El paquete es público, pero ejecutar análisis sigue requiriendo acceso a
Codex Security. Algunos análisis de repositorios completos también requieren Trusted Access for Cyber.

### Organiza sesiones y amplía Codex CLI 0.146.0

[Codex CLI 0.146.0](https://github.com/openai/codex/releases/tag/rust-v0.146.0)
te permite asignar un nombre a un chat nuevo con `/new release prep` o `/clear bug bash`, fijar
hilos importantes y alternar entre conversaciones secundarias sin cerrarlas.
También agrega forks temporales de conversaciones, búsqueda web independiente para proveedores
de modelos personalizados compatibles, habilidades proporcionadas por el ejecutor y compatibilidad con archivos de manifiesto
de Agent Plugins, publicación de complementos en el espacio de trabajo y otros marketplaces de complementos.

Para clientes personalizados, [App Server](/es-419/codex/app-server) puede filtrar hilos
fijados, crear forks en memoria, inspeccionar el estado de los conectores instalados y leer
sus metadatos. La compatibilidad experimental con WebSocket también conecta app-server con
hosts remotos de Code Mode. Revisa los
[requisitos de seguridad de app-server](/es-419/codex/app-server#connect-the-cli-terminal-ui)
antes de exponer una conexión remota. Esta versión también mejora la compatibilidad con proxies,
la reconexión de MCP, la capacidad de respuesta de la terminal y la confiabilidad del sandbox de Windows.

### Usa GPT-5.6 Sol para trabajar con Codex en la nube

[GPT-5.6 Sol](/es-419/codex/models#recommended-models) ahora es el modelo que usa Codex Cloud para la revisión
de código y el aseguramiento de la calidad para los clientes que cumplen los requisitos. Sol es el modelo insignia
de GPT-5.6 para tareas complejas de programación, investigación, uso de la computadora y seguridad.
Codex Cloud selecciona su modelo automáticamente; Terra y Luna siguen disponibles en las
interfaces locales y web compatibles.

### Prepárate para el retiro de los modelos GPT-5.4

El 31 de agosto, GPT-5.4 y GPT-5.4 mini se retirarán de Codex para los usuarios que hayan iniciado
sesión con ChatGPT. Reemplaza `gpt-5.4` por `gpt-5.6-terra` y `gpt-5.4-mini`
por `gpt-5.6-luna` en los valores predeterminados del espacio de trabajo, la configuración de modelos guardada, las
configuraciones administradas, los agentes personalizados y las tareas programadas.

La API de OpenAI y las sesiones de Codex autenticadas con una clave de API no se ven
afectadas. Revisa los [modelos de Codex en desuso](/es-419/codex/models#deprecated-codex-models)
y la [disponibilidad de modelos en el
espacio de trabajo](/es-419/codex/enterprise/workspace-model-availability) antes de la
fecha límite.

## 20–24 de julio de 2026

### Habla sobre tu trabajo con ChatGPT Voz

[ChatGPT Voz](/es-419/codex/features/voice), que funciona con GPT-Live, te permite hablar
sobre tu trabajo y coordinar tareas en Chat, Work y Codex en la aplicación de escritorio
de ChatGPT. Inicia un chat o una tarea en modo de voz y luego pídele a ChatGPT que inicie, revise o
dirija el trabajo en otros hilos.

En macOS, di “Mira esto” para compartir una [captura de la aplicación](/es-419/codex/appshots) de
la ventana que está en primer plano cuando **Contexto de pantalla** esté activado.

Voz está disponible con los planes Plus, Pro, Business, Edu y Enterprise en la
app de escritorio y a través de [Remoto en iOS](/es-419/codex/remote-connections#set-up-mobile-access).

### Trabaja en varias carpetas dentro de un proyecto local

Los proyectos locales de la aplicación de escritorio de ChatGPT ahora pueden incluir varias carpetas
relacionadas. Elige una carpeta principal para los chats nuevos, las operaciones de Git y la detección
automática de `AGENTS.md`, habilidades y `config.toml`. Las carpetas secundarias siguen
disponibles para buscar, leer y editar archivos.

Abre **Editar proyecto** para [agregar carpetas y elegir la carpeta
principal](/es-419/codex/projects#use-local-projects-for-folders-and-codebases).

[Lee las notas de la versión del 23 de julio](/codex/changelog#codex-2026-07-23-app).

## Del 13 al 17 de julio de 2026

### Mantén juntas las conversaciones de Work y los proyectos en la app de escritorio

La aplicación de escritorio de ChatGPT ahora reúne las conversaciones de Chat y Work en la
vista de ChatGPT. Las conversaciones de Work en la nube se sincronizan entre la web, los dispositivos móviles y la app de escritorio;
las conversaciones locales de Work permanecen en tu computadora. Los proyectos de ChatGPT están disponibles
en la app de escritorio. Codex conserva su vista dedicada y un historial separado para
los flujos de trabajo de desarrollo.

[Compara ChatGPT Work y Codex en la app de
escritorio](/es-419/codex/use-chatgpt#compare-chatgpt-work-and-codex-on-desktop) para elegir la
vista que se adapte a tu tarea.

### Controla el trabajo en paralelo de Codex con Codex Micro

El 15 de julio, OpenAI y Work Louder lanzaron
[Codex Micro](/es-419/codex/features/codex-micro), un panel de control físico de edición
limitada para Codex en la aplicación de escritorio de ChatGPT. Sus teclas de agente muestran el estado de
hasta seis chats y permiten alternar entre ellos. Las teclas de comando personalizables, una palanca
analógica y un dial permiten ejecutar acciones comunes o habilidades, activar la función de presionar para hablar y
ajustar el esfuerzo de razonamiento sin dejar el teclado.

### Usa GPT-5.6 a través de Amazon Bedrock

GPT-5.6 Sol, Terra y Luna alcanzaron la disponibilidad general a través de Amazon Bedrock.
Las interfaces locales de ChatGPT Work y Codex pueden usar el
[proveedor `amazon-bedrock`](/es-419/codex/amazon-bedrock) integrado con una clave de API de Bedrock o la
cadena de credenciales del SDK de AWS. Esto incluye Work y Codex en la aplicación de escritorio de ChatGPT,
Codex CLI, la extensión para IDE y el SDK de Codex.

### Inspecciona las visualizaciones de las tareas de Codex en iOS

ChatGPT para iOS 1.2026.188 incorporó visualizaciones integradas en las tareas de Codex y
mejoró la creación y gestión de tareas desde las conversaciones, con enlaces confiables
a las tareas recién creadas. Lee las
[notas de la versión para iOS del 13 de julio](/codex/changelog#codex-2026-07-13-mobile).

## Del 6 al 10 de julio de 2026

<a id="take-on-ambitious-work-with-chatgpt-work"></a>

### Aborda trabajos ambiciosos en ChatGPT

[ChatGPT Work](/es-419/codex/get-started-with-work) en ChatGPT puede recopilar contexto de
tus archivos y [complementos](/es-419/codex/plugins),
realizar acciones en distintos flujos de trabajo y crear documentos, presentaciones,
hojas de cálculo, Sites y otros trabajos terminados que puedes revisar. Con
[GPT-5.6](/es-419/codex/models), puede dividir un objetivo en pasos y trabajar durante horas mientras
sigues su progreso, respondes preguntas, cambias de rumbo y apruebas
acciones importantes.

Las [tareas programadas](/es-419/codex/automations) pueden mantener ese trabajo en marcha cuando no estás
al ejecutarse una vez, según un horario, cuando ocurre un evento o mientras monitorean
cambios.

### Elige el modelo GPT-5.6 adecuado

La [familia GPT-5.6](/es-419/codex/models#recommended-models) ofrece tres modelos
recomendados en ChatGPT Work, la aplicación de escritorio de ChatGPT, Codex CLI y la extensión de Codex
para IDE. Sol es el modelo insignia para tareas complejas de programación, uso de la computadora, investigación y
seguridad. Terra equilibra capacidad y costo para el trabajo cotidiano, mientras que Luna
es la opción más rápida y de menor costo. La configuración predeterminada **Potencia** usa Sol con
un nivel medio de razonamiento.

### Usa Codex en la aplicación de escritorio de ChatGPT

El 9 de julio, la app de Codex se integró en la
[aplicación de escritorio de ChatGPT](/es-419/codex/app) para macOS y Windows. Codex conserva su
experiencia dedicada a la programación junto con Chat y Work de ChatGPT. La experiencia de
Codex incluye edición directamente en los diffs, revisión de Pull Requests en el panel lateral,
[Uso de la computadora](/es-419/codex/computer-use) más rápido gracias a GPT-5.6 y proyectos con varios
repositorios.

Quienes ya usan la app de Codex pueden actualizarla como de costumbre. Puedes establecer Codex como la vista
predeterminada, usar el logo de Codex como ícono de la app y acceder a los proyectos de Codex de escritorio desde
la app móvil de ChatGPT. La app de escritorio actualizada está disponible en todo el mundo con todos los
planes de ChatGPT, incluido Gratis.

## Del 15 al 19 de junio de 2026

### Convierte demostraciones de flujos de trabajo en habilidades reutilizables

[Grabar y reproducir](/es-419/codex/extend/record-and-replay) te permite mostrarle a ChatGPT o
Codex un flujo de trabajo en macOS y convertir la demostración en una habilidad reutilizable.
Úsalo para tareas repetitivas que sean más fáciles de mostrar que de describir; luego perfecciona la
habilidad generada y vuelve a ejecutarla con nuevas entradas. Inicialmente, no está disponible en
el EEE, el Reino Unido ni Suiza y requiere Uso de la computadora.

<a id="continue-a-task-on-another-host"></a>

### Continúa un chat en otro host

La [transferencia de chats](/es-419/codex/remote-connections#hand-off-a-chat-between-hosts)
mueve un chat y su estado de Git entre tu computadora local y un host remoto
conectado. Codex puede crear o reutilizar un worktree en el destino, transferir
el chat y continuar desde el proyecto correspondiente.

La misma versión de escritorio incorpora acciones en lote al historial de ejecuciones programadas, de modo que
puedes marcar todas las ejecuciones como leídas o archivar juntas las que cumplan los requisitos.

### Explora y revisa espacios de trabajo desde iOS

En la app móvil de ChatGPT, **Remoto** incorporó en iOS un explorador de archivos del espacio de trabajo, un
selector de directorios para chats nuevos, controles para expandir y contraer diffs y
opciones de aprobación de MCP para un solo chat o varios chats.

Uso de la computadora, la extensión de Chrome, Memorias y Chronicle también comenzaron
a habilitarse en el EEE, el Reino Unido y Suiza. Las Memorias siguen
desactivadas de forma predeterminada en esas regiones, y Chronicle es una versión preliminar de investigación de activación voluntaria
para suscriptores de ChatGPT Pro en macOS.

Lee las notas de la versión de [iOS del 15 de junio](/codex/changelog#codex-2026-06-15-mobile),
las de [disponibilidad del 16 de junio](/codex/changelog#codex-2026-06-16-app) y
las de la [app del 18 de junio](/codex/changelog#codex-2026-06-18-app).

## Del 8 al 12 de junio de 2026

### Depura apps web con el modo de desarrollador del navegador

El [modo de desarrollador](/es-419/codex/browser?surface=app#app-developer-mode) le da a Codex acceso
controlado a las capacidades de Chrome DevTools Protocol en Chrome y el navegador
integrado. Codex puede inspeccionar el tráfico de red, la salida de la consola, los errores de ejecución y
el estado de la página mientras analiza el rendimiento o depura tu app. En **Modo de desarrollador** , dentro de
**Configuración** \> **Navegador**, activa **Habilitar acceso completo a CDP**. Codex solicita
aprobación explícita antes de usar ese acceso en un sitio web.

El uso del navegador también es hasta el doble de rápido porque las optimizaciones de CDP y de las instantáneas del DOM
reducen los intercambios de ida y vuelta con el navegador.

  
    
  

### Lleva tu configuración a Codex

Los nuevos flujos de migración pueden importar los elementos de configuración compatibles de otros agentes de programación durante
la configuración inicial. La app de Codex también incorporó `/init` para crear instrucciones del proyecto,
además de mejoras en la administración de complementos, el diagnóstico del navegador y los resúmenes de chats
finalizados.

<a id="set-up-codex-tasks-from-ios"></a>

### Configura chats de Codex desde iOS

Remoto en iOS ahora permite elegir una rama, crear un worktree, ejecutar un script de
configuración del entorno, gestionar objetivos y agregar comentarios de revisión en línea.

Lee las notas de la versión de la [app del 9 de junio](/codex/changelog#codex-2026-06-09-app),
de [iOS del 9 de junio](/codex/changelog#codex-2026-06-09-mobile) y
de la [app del 11 de junio](/codex/changelog#codex-2026-06-11-app).

## Del 1 al 5 de junio de 2026

### Crea y despliega sitios web con Sites

[Sites](/es-419/codex/sites) permite que ChatGPT cree, guarde, despliegue e inspeccione sitios web,
paneles, herramientas internas, aplicaciones web y juegos alojados por OpenAI. Sites tiene un
acceso dedicado en ChatGPT en la web y en la aplicación de escritorio, donde puedes volver a tus
proyectos y administrar los valores y secretos del entorno alojado sin configurar una
infraestructura de despliegue aparte.

### Usa Codex con Amazon Bedrock

Puedes [usar Codex con Amazon Bedrock](/es-419/codex/amazon-bedrock) para flujos de trabajo locales
con autenticación, controles de cuenta y facturación administrados por AWS.
Remoto en iOS también incorporó un bloqueo opcional dentro de la aplicación, opciones para configurar el comportamiento de seguimiento,
ajuste de línea para las diferencias y conexiones SSH a equipos con Windows. La aplicación de escritorio
incorporó controles para ubicar la terminal e información sobre la actividad en la vista
de perfil.

[Lee todas las notas de lanzamiento de junio de 2026](/codex/changelog#month-2026-06).

## 25–29 de mayo de 2026

### Usa aplicaciones de Windows y controla Codex de forma remota

La función [Uso de la computadora](/es-419/codex/computer-use#windows-foreground-use) ahora permite
ver, hacer clic y escribir en aplicaciones de escritorio de Windows. Instala el complemento de Uso de la computadora
antes de comenzar. En Windows, Codex usa el escritorio activo y toma
el control en primer plano mientras se ejecuta la tarea. Las conexiones remotas también son compatibles con
Windows. En la aplicación móvil de ChatGPT, abre **Remoto** para empezar a trabajar en un dispositivo con Windows
o usa una Mac que ejecute la aplicación de escritorio de ChatGPT y revisa el progreso desde
otro lugar.

Remoto en iOS también incorporó accesos desde Spotlight y Atajos, navegación por chats
archivados, `/side` y opciones para guardar o copiar imágenes renderizadas. La aplicación de escritorio
incorporó la coordinación de chats para proyectos locales y worktrees, la búsqueda por contenido y
nombre de rama en chats anteriores e identificadores visuales coherentes para los
subagentes en segundo plano.

Lee las notas de lanzamiento de [iOS del 25 de mayo](/codex/changelog#codex-2026-05-25-mobile) y
[la aplicación del 29 de mayo](/codex/changelog#codex-2026-05-28-app).

## 18–22 de mayo de 2026

### Dale a Codex contexto de cualquier aplicación de Mac con Capturas de la aplicación

Las [Capturas de la aplicación](/es-419/codex/appshots) envían a Codex la ventana de la aplicación que está en primer plano con una
captura de pantalla y el texto disponible cuando presionas ambas teclas Command. Codex obtiene
contexto de trabajo de herramientas de diseño, paneles, documentos y otras aplicaciones
sin que tengas que copiar, pegar ni describir lo que aparece en pantalla.

### Da seguimiento a objetivos de larga duración

El [modo de objetivos](/es-419/codex/prompting#goal-mode) dejó de ser experimental y está
disponible en Codex App, la extensión para IDE y la CLI para objetivos que pueden llevar
horas o días. El [uso con bloqueo](/es-419/codex/computer-use#locked-use) permite que Codex
continúe las tareas aprobadas de uso de la computadora después de que se bloquee una Mac, incluso a través de
**Remoto** en la aplicación móvil de ChatGPT. Los espacios de trabajo de ChatGPT Business también pueden
[compartir paquetes reutilizables de complementos con los miembros del espacio de trabajo](https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace).

[Lee las notas de lanzamiento del 21 de mayo](/codex/changelog#codex-2026-05-21).

## 11–15 de mayo de 2026

### Continúa el trabajo de escritorio desde un dispositivo móvil

En la aplicación móvil de ChatGPT, **Remoto** se conecta a una Mac que ejecuta la aplicación de escritorio
de ChatGPT. Como el trabajo se ejecuta en el host conectado, tus proyectos, archivos,
credenciales, complementos, habilidades y configuración siguen disponibles cuando
continúas desde tu teléfono. Consulta [Conexiones remotas](/es-419/codex/remote-connections)
para configurar un host y retomar el trabajo desde otro dispositivo.

### Automatiza flujos de trabajo de confianza

Los hooks pasaron a estar disponibles de forma general para ejecutar comandos personalizados en puntos clave del
ciclo de vida del agente. Los administradores de ChatGPT Enterprise también pueden habilitar
[tokens de acceso de Codex](/es-419/codex/enterprise/access-tokens) para scripts de confianza,
programadores de tareas y ejecutores privados de CI. La documentación para empresas se amplió para incluir
la configuración administrada y los controles de Codex.

[Lee las notas de lanzamiento del 14 de mayo](/codex/changelog#codex-2026-05-13-app).

## 4–8 de mayo de 2026

### Trabaja en varias pestañas del navegador con la extensión de Chrome

La [extensión de Chrome](/es-419/codex/chrome-extension) puede trabajar en
paralelo en distintas pestañas en segundo plano sin tomar el control de tu navegador. Tú
controlas qué sitios web puede usar Codex, lo que facilita combinar investigación,
ingreso de datos y verificación en distintas aplicaciones web dentro de una misma tarea.

Codex App también incorporó la corrección del texto dictado y un diccionario personalizado para nombres,
rutas de archivos y símbolos de código. Los propietarios de espacios de trabajo de ChatGPT Enterprise pueden permitir
que los miembros creen [tokens de acceso de Codex](/es-419/codex/enterprise/access-tokens) para
flujos de trabajo locales de confianza y no interactivos.

Lee las notas de lanzamiento de [la aplicación del 5 de mayo](/codex/changelog#codex-2026-05-05-app),
[los tokens de acceso del 5 de mayo](/codex/changelog#codex-2026-05-05) y
[Codex para Chrome](/codex/changelog#codex-2026-05-07).

## 20–24 de abril de 2026

### Usa GPT-5.5 para tareas complejas

[GPT-5.5](/es-419/codex/models) llegó a Codex como el modelo recomendado para la mayoría de las
tareas, con fortalezas en implementación, depuración, pruebas, uso de la computadora,
investigación y elaboración de entregables completos de trabajo intelectual.

### Deja que Codex maneje el navegador y revise las aprobaciones

La función [Uso de la computadora en el navegador integrado](/es-419/codex/browser?surface=app#app-computer-use-in-the-browser)
permite que Codex navegue haciendo clic en servidores de desarrollo locales y páginas basadas en archivos para
reproducir problemas y verificar correcciones. Las solicitudes de aprobación que cumplen los requisitos también pueden pasar
por una [revisión automática de aprobaciones](/es-419/codex/sandboxing/auto-review),
que muestra el estado de la revisión y el riesgo antes de ejecutar la acción.

[Lee las notas de lanzamiento del 23 de abril](/codex/changelog#codex-2026-04-23).

## 13–17 de abril de 2026

### Previsualiza tu trabajo e interactúa con él en un solo lugar

El [navegador integrado](/es-419/codex/browser?surface=app) incorporó vistas previas en tiempo real y comentarios en las
páginas, mientras que [Uso de la computadora](/es-419/codex/computer-use) permitió que Codex viera y
manejara aplicaciones de macOS. En conjunto, estas funciones integraron la implementación visual y la verificación de extremo a extremo
en la misma tarea que el cambio de código.

  
    
  

<a id="start-with-a-task-and-keep-it-moving"></a>

### Empieza con un chat y sigue avanzando

Los [chats independientes](/es-419/codex/projects#start-without-a-project) permitieron
empezar sin elegir una carpeta de proyecto. La misma versión incorporó
[tareas programadas dentro de un chat](/es-419/codex/automations#schedule-a-task-inside-a-chat),
contexto de pull requests, vistas previas de archivos más completas y [Memorias](/es-419/codex/customization/memories) para
el trabajo que abarca varios chats.

[Lee las notas de la versión de Codex App del 16 de abril](/codex/changelog#codex-2026-04-16-app).

## 6–10 de abril de 2026

### Revisa y envía pull requests desde la app

La experiencia de revisión incorporó comentarios en línea que se pueden contraer, modos de revisión en línea y en una vista independiente,
y un contexto más claro de Git y del código fuente. Después, la actividad de los pull requests,
los comentarios y las opciones para hacer push se integraron en la app junto con las pestañas de archivos del
espacio de trabajo, para que pudieras inspeccionar un cambio y responder sin cambiar de herramienta.

Lee las notas de la versión de Codex App del [9 de abril](/codex/changelog#codex-2026-04-09-app) y del
[10 de abril](/codex/changelog#codex-2026-04-10-app), o
aprende a [revisar cambios en la app](/es-419/codex/code-review?surface=app).

## 23–27 de marzo de 2026

### Empaqueta flujos de trabajo como complementos

Los [complementos](/es-419/codex/plugins) se lanzaron como paquetes instalables de habilidades,
conectores y servidores MCP. Facilitaron encontrar,
instalar y compartir flujos de trabajo completos, mientras que las páginas rediseñadas de complementos y habilidades mostraban con más claridad su contenido
y estado. Esa semana también llegó la búsqueda de chats anteriores.

Lee las notas de la versión sobre la [búsqueda de tareas](/codex/changelog#codex-2026-03-24-app),
el [lanzamiento de complementos](/codex/changelog#codex-2026-03-25) y
[Codex App](/codex/changelog#codex-2026-03-25-app).

## 16–20 de marzo de 2026

### Crea un fork desde un mensaje anterior y elige herramientas desde el editor

Podías crear un fork de un chat a partir de un mensaje anterior, lo que facilitaba probar un nuevo
enfoque sin perder el hilo original. Los comandos de modelo y razonamiento pasaron a estar
disponibles mientras redactabas, las habilidades activadas aparecían en el menú `@` y GPT-5.4
mini ofrecía una opción más rápida para tareas más ligeras y subagentes.

Lee las notas de la versión sobre [GPT-5.4 mini](/codex/changelog#codex-2026-03-17),
el [control de chats](/codex/changelog#codex-2026-03-18-app) y
el [menú de habilidades](/codex/changelog#codex-2026-03-19-app).

## 9–13 de marzo de 2026

### Programa trabajo en el entorno adecuado

Las [tareas programadas](/es-419/codex/automations) podían ejecutarse localmente o en un worktree
con un modelo y un nivel de razonamiento definidos explícitamente. Las plantillas reutilizables permitían configurar más rápido las tareas
comunes, y los temas personalizados facilitaban la
personalización del espacio de trabajo.

  
    
  

### Deja que Codex inspeccione la salida de la terminal

Codex también aprendió a leer la [terminal integrada](/es-419/codex/integrated-terminal#run-and-validate-your-project)
del chat actual. Podía inspeccionar directamente un servidor de desarrollo en ejecución o la salida de una
compilación, en lugar de pedirte que la pegaras.

Lee las notas de la versión de Codex App del [11 de marzo](/codex/changelog#codex-2026-03-11-app) y del
[12 de marzo](/codex/changelog#codex-2026-03-12-app).

## 2–6 de marzo de 2026

### Ejecuta Codex de forma nativa en Windows

Codex App se lanzó en [Windows](/es-419/codex/windows/windows-app) con compatibilidad nativa con PowerShell
y sandbox, además de worktrees, tareas programadas y habilidades. WSL siguió
disponible para los desarrolladores que preferían un entorno Linux.

  
    
  

<a id="move-tasks-between-local-and-worktree"></a>

### Mueve chats entre Local y Worktree

[La transferencia entre Local y Worktree](/es-419/codex/environments/git-worktrees#working-between-local-and-worktree)
permitió mover un chat activo sin perder su contexto. GPT-5.4
también llegó a Codex esa semana para programación, uso de la computadora y flujos de trabajo
con contextos más extensos.

Lee las notas de la versión sobre el [lanzamiento en Windows](/codex/changelog#codex-2026-03-04-app),
la [transferencia entre worktrees](/codex/changelog#codex-2026-03-03-app) y
[GPT-5.4](/codex/changelog#codex-2026-03-05).

## 9–13 de febrero de 2026

### Itera en tiempo real y crea una variante de tu enfoque

GPT-5.3-Codex-Spark entró en vista previa de investigación como un modelo de respuesta casi instantánea para
iterar sobre código en tiempo real. La aplicación también incorporó la creación de forks de chats y una
ventana de chat flotante que siempre permanece en primer plano, para que pudieras explorar otro enfoque o
mantener Codex junto a un editor o navegador.

Lee las notas de la versión de [Spark](/codex/changelog#codex-2026-02-12) y
[Codex App](/codex/changelog#codex-2026-02-12-app), o consulta la
[guía de modelos](/es-419/codex/models) actual.

## 2–6 de febrero de 2026

### Codex App llega a macOS

Codex App se lanzó como un espacio de trabajo de escritorio para chats de proyectos en paralelo,
con revisión integrada de cambios en Git, worktrees, habilidades, tareas programadas y dictado por voz.
Estas capacidades ahora están en Codex dentro de la [aplicación de escritorio de ChatGPT](/es-419/codex/app).

  
    
  

### Redirige el trabajo en curso y agrega archivos

Dar nuevas indicaciones durante un turno permitió redirigir Codex sin detener una
respuesta en curso, y los archivos adjuntos dejaron de limitarse a imágenes. Estas formas de interacción
sentaron las bases para [dar nuevas indicaciones y poner en cola](/es-419/codex/prompting#steering-and-queuing)
mensajes de seguimiento con el contexto que Codex necesita.

Lee las [notas del lanzamiento de Codex App](/codex/changelog#codex-2026-02-02) y
las [notas de la versión de la aplicación del 5 de febrero](/codex/changelog#codex-2026-02-05-app).
