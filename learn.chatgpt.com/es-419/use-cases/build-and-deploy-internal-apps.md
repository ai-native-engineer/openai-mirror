<!-- source: https://learn.chatgpt.com/es-419/use-cases/build-and-deploy-internal-apps -->

## Crea e implementa con una sola tarea

Sites es un servicio de alojamiento administrado en ChatGPT. Pídele a ChatGPT que cree una aplicación; podrá crear el proyecto, ejecutarlo para probarlo, implementarlo y proporcionarte una URL que puedes compartir.

Sites está en versión beta pública para los planes de pago que cumplen los requisitos. No está disponible para los planes Free ni Go, ni en el EEE, Suiza o el Reino Unido al momento del lanzamiento; además, el lanzamiento gradual o la configuración del espacio de trabajo pueden afectar el acceso.

Abarca desde sitios estáticos hasta aplicaciones web full-stack en JavaScript o TypeScript. Esto hace que Sites sea una buena opción para herramientas internas específicas: paneles de incorporación, centros de capacitación, bibliotecas de recursos con búsqueda, aplicaciones ligeras para flujos de trabajo y vistas de informes.

Consulta la [documentación de Sites](/es-419/codex/sites) para obtener orientación sobre la configuración, el almacenamiento, la implementación y el acceso.

Comienza con un solo flujo de trabajo útil. Una primera versión clara es más fácil de revisar, implementar y mejorar que una solicitud amplia que pretenda recrear todo un sistema interno.

## Qué esperar

Este es un ejemplo ficticio que usa un resumen de lanzamiento adjunto y cinco solicitudes de ejemplo. En la primera iteración, se crea y comprueba un gestor enfocado en las solicitudes de lanzamiento; en una solicitud posterior, se agrega un filtro por responsable y se facilita la identificación de las solicitudes vencidas.

<div data-use-case-export-only>

El gestor de solicitudes de lanzamiento se abre con **cinco solicitudes de ejemplo**, entre ellas una bloqueada, dos en revisión y una vencida. El equipo puede consultarlas por lanzamiento y estado, filtrar las solicitudes bloqueadas, agregar una solicitud y actualizar su estado. El flujo principal y el estado guardado se comprobaron con anchos de pantalla de computadoras de escritorio y dispositivos móviles.

Tras una solicitud adicional, el gestor incluye un filtro por responsable y resalta el trabajo vencido; **las solicitudes bloqueadas permanecen en la parte superior y ninguna solicitud puede marcarse como lista si no tiene responsable**. La vista previa sigue siendo privada; no se publicó ningún sitio ni se modificó el acceso.

</div>

## Proporciona a ChatGPT el contexto del flujo de trabajo

Indícale a ChatGPT para quién es la aplicación, qué deben hacer las personas, qué material de referencia debe revisar y qué debe conservarse entre sesiones. Especifica el alcance previsto para compartirla y pídele a ChatGPT que pruebe el flujo principal antes de implementarla.

Usa [complementos](/es-419/codex/plugins) para obtener o actualizar datos de fuentes internas conectadas. Inicia una tarea de Sites que use aplicaciones conectadas o archivos en la nube desde Work en la Web, o desde Work o Codex en la App de escritorio. Usa la App de escritorio para un archivo local, el navegador integrado para un sitio donde hayas iniciado sesión o la Extensión de Chrome de Codex para una sesión existente de Chrome.

  Si necesitas obtener datos en tiempo real, puedes conectarte a una herramienta de terceros mediante una
  clave de API definida en la configuración del sitio. No incluyas valores secretos en prompts
  ni archivos. Si quieres usar conexiones de complementos, puedes [programar trabajo desde
  la tarea actual](/es-419/codex/automations#schedule-work-from-a-task) para obtener datos
  con complementos según un cronograma establecido, actualizar la aplicación y guardar una versión para revisión.
  Implementa la versión revisada solo después de recibir aprobación.

## Elige el almacenamiento de la aplicación

Muchas aplicaciones internas necesitan persistencia. Sites admite dos primitivas de almacenamiento:

- Usa D1, una base de datos compatible con SQLite, para datos estructurados como el estado de las listas de verificación, los marcadores, los filtros, las anotaciones, la configuración y los metadatos de archivos.
- Usa el almacenamiento de objetos R2 para guardar los bytes de documentos cargados, imágenes u otros recursos que deban conservarse.

Guarda los metadatos estructurados en D1 y los objetos de archivo de mayor tamaño en R2. Es posible que una página de recursos de solo lectura o un sitio estático pequeño no necesiten ninguno de los dos.

Sites no admite la residencia de datos ni la de inferencia. No lo uses para procesar información de salud protegida o datos de tarjetas de pago, ni para habilitar transacciones financieras. Revisa las [restricciones de Sites sobre datos y uso](https://help.openai.com/en/articles/20001339-creating-and-managing-chatgpt-sites) antes de almacenar información confidencial.

## Administra y comparte tus proyectos

Puedes administrar quién puede visitar tus proyectos implementados.

Mantén privado un proyecto nuevo mientras revisas su contenido, el manejo de datos y el público al que va dirigido.

Según la configuración de tu cuenta y de tu espacio de trabajo, puedes compartirlo con:

- Las personas que invites.
- Todas las personas de tu espacio de trabajo.
- Cualquier persona en Internet.

Compartir un proyecto permite que otras personas lo visiten, pero no que lo editen. Para cambiar el acceso, abre [Sites en ChatGPT](https://chatgpt.com/sites) o pídeselo directamente a ChatGPT:

Compartir públicamente también es útil para una guía sencilla de un evento, una página de recursos de un club u otro sitio destinado a personas ajenas a un espacio de trabajo. En los espacios de trabajo para Empresas, la publicación pública está desactivada de forma predeterminada y un administrador debe habilitarla. Mantén privados los datos internos incluso cuando haya un enlace público disponible.

## Ejemplos

La [galería de Sites](/showcase/sites) incluye ejemplos de sitios con prompts completos.

{/* vale Vale.Spelling = NO */}
{/* vale Vale.Terms = NO */}

- **[Onboarding Hub](/showcase/onboarding-hub)** combina una lista de verificación de la primera semana, recursos, notas y documentos cargados. Usa D1 para el estado del usuario y los metadatos de archivos, y R2 para los bytes de los archivos cargados.
- **[Enablement Hub](/showcase/enablement-hub)** ofrece una biblioteca de capacitación con búsqueda, filtros y marcadores guardados en D1.
- **[Pulse Dashboard](/showcase/pulse-dashboard)** presenta métricas, tendencias y detalles de linaje, y usa D1 para la configuración y las instantáneas en caché.
- **[Sparkboard](/showcase/idea-intake)** convierte la recepción de ideas de los empleados en un flujo de trabajo con envíos autenticados, votaciones, comentarios, tableros de estado y clasificaciones de colaboradores.
- **[Launch Cal](/showcase/launch-cal)** organiza los próximos lanzamientos de productos en un calendario mensual con filtros, indicadores de riesgo, listas de verificación y referencias a fuentes conectadas.
- **[Event Planning Hub](/showcase/event-planning-hub)** combina solicitudes de eventos, aprobaciones, plantillas, hitos, preparación para el cumplimiento de políticas y recursos de planificación conectados.

{/* vale Vale.Terms = YES */}
{/* vale Vale.Spelling = YES */}

Usa esos ejemplos como punto de partida y, luego, acota el prompt al flujo de trabajo y al material de referencia de tu equipo.
