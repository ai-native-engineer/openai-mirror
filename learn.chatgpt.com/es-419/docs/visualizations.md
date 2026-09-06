<!-- source: https://learn.chatgpt.com/es-419/docs/visualizations -->

Las visualizaciones convierten preguntas, ideas e información en gráficos, mapas,
diagramas, calculadoras, simulaciones y explicaciones interactivas que puedes explorar
en un chat de ChatGPT. Usa una cuando ajustar las entradas o ver una
relación permita entender mejor una respuesta, compararla, practicar con ella o
actuar a partir de ella.

  La versión preliminar de Visualizaciones se habilita de forma gradual. La disponibilidad puede depender de tu
plan, plataforma, cuenta y configuración del espacio de trabajo.

La versión preliminar de Visualizaciones se habilita gradualmente en la aplicación de escritorio de ChatGPT. Cuando
**Visualizar** esté disponible, escribe `@` en el editor, comienza a escribir
`Visualize` y selecciona **Visualizar** en **Complementos**. El editor agrega la etiqueta
**Visualizar** antes de tu solicitud.

Si **Visualizar** no aparece, usa ChatGPT en la web o vuelve a intentarlo cuando la
versión preliminar llegue a tu cuenta.

En un chat compatible de Chat o ChatGPT Work, escribe `@` en el editor,
comienza a escribir `Visualize` y selecciona **Visualizar** en **Complementos**. Su
descripción es **Crear visualizaciones y herramientas interactivas**. El editor
agrega una etiqueta **Visualizar** antes de tu solicitud.

También puedes escribir `@Visualize` y seleccionar la sugerencia correspondiente.

Codex CLI no renderiza visualizaciones. Abre el mismo material de referencia en
ChatGPT en la web o en la aplicación de escritorio de ChatGPT y agrega allí la etiqueta `@Visualize`.

La extensión para IDE de Codex no renderiza visualizaciones. Usa ChatGPT en la web
o la aplicación de escritorio de ChatGPT para este flujo de trabajo.

## Consultar la disponibilidad

| Plataforma                     | Disponibilidad actual                                                          |
| --------------------------- | ----------------------------------------------------------------------------- |
| ChatGPT en la web          | Disponible para cuentas compatibles en Chat y ChatGPT Work                      |
| Aplicación de escritorio de ChatGPT         | Implementación gradual de la versión preliminar                                                        |
| Aplicaciones móviles de ChatGPT         | Implementación gradual para cuentas elegibles; los controles del editor pueden variar según la versión de la aplicación |
| Codex CLI y la extensión para IDE | No se admite el renderizado de visualizaciones                                       |

La sugerencia **Visualizar** es una señal confiable de que la versión preliminar está habilitada
en tu cuenta. Durante la implementación gradual, la disponibilidad puede variar entre cuentas,
espacios de trabajo y versiones de la aplicación, incluso dentro del mismo plan.

## Elegir cuándo conviene usar una visualización

ChatGPT puede elegir un formato visual cuando mejora sustancialmente la respuesta. También
puedes agregar la etiqueta `@Visualize` cuando quieras específicamente un resultado interactivo.

Pide el formato más sencillo que se adapte a la tarea:

- Usa un diagrama para mostrar relaciones con etiquetas o un proceso.
- Usa un gráfico o un trazado para datos numéricos identificados y comparaciones.
- Usa un mapa para la información geográfica.
- Usa una visualización interactiva cuando deban cambiar las entradas, el tiempo, el movimiento o las relaciones
espaciales.
- Usa un [Site](/es-419/codex/sites) cuando necesites una aplicación alojada y duradera con una
  URL que se pueda compartir, permisos o datos persistentes.

## Especificar el resultado y los controles en el prompt

Una solicitud bien formulada especifica el resultado, el material de referencia, la pregunta y las interacciones
útiles. Prueba este ejemplo:

Indícale a ChatGPT qué información debe usar, como el contenido que ya está en el
chat, los datos pegados, un archivo adjunto o una fuente conectada disponible.
Para solicitudes complejas, elige un nivel de razonamiento más alto cuando esté disponible.

## Explorar ejemplos interactivos

Estos ejemplos reproducen tres visualizaciones de la página de lanzamiento de GPT-5.6.
Usa sus controles para ver cómo un prompt bien definido puede convertirse en una
explicación interactiva, un laboratorio o una herramienta didáctica.

  

## Perfeccionar y continuar

Continúa en el mismo chat y describe el cambio que quieres. Entre las solicitudes de seguimiento útiles
se incluyen:

- Agrega o elimina un control, filtro, comparación o anotación.
- Corrige los datos de origen, las unidades, las etiquetas o los supuestos.
- Simplifica un resultado lento agregando los datos, agrupándolos en intervalos o tomando una muestra.
- Agrega un resumen de texto conciso y una tabla de datos.
- Haz que todos los controles sean accesibles con el teclado y agrega estados de foco visibles.
- Usa etiquetas o patrones, además del color, y elimina el movimiento en bucle.
- Convierte el resultado en un Site cuando deba alojarse y consultarse de nuevo.

Una solicitud de seguimiento puede crear una nueva visualización que reemplace a la anterior en vez de editar el
resultado original directamente. Revisa la versión nueva antes de confiar en ella.

## Compartir o reutilizar un resultado

Usa la acción estándar **Compartir** del chat cuando esté disponible. Antes, revisa
todo el chat compartido, incluidos sus datos de origen y los mensajes
anteriores. Por lo general, una visualización es una instantánea de la información disponible
cuando ChatGPT la creó y no un panel en vivo que se mantenga sincronizado con una
fuente conectada.

Los controles de descarga generados y los formatos de exportación pueden variar según el resultado. Si una exportación
no funciona, pídele a ChatGPT los datos subyacentes en un formato más simple o pídele
que convierta la visualización en un Site.

## Mejorar la accesibilidad

Las visualizaciones generadas procuran usar controles semánticos, indicadores de foco visibles y contraste
que facilite la lectura y movimiento reducido, pero el resultado puede variar. Revisa la visualización
antes de compartirla. Pídele a ChatGPT que agregue un resumen de texto y una tabla de datos, etiquete los ejes
y las unidades, evite depender solo del color y haga que los controles funcionen con el teclado.

## Qué hacer si falla un resultado

Las visualizaciones pueden tardar un minuto o más en generarse. Si el resultado está en blanco
o no aparece, espera a que termine la respuesta, recarga el chat una vez y
luego vuelve a intentarlo. Si sigue fallando:

- Pide una visualización más pequeña o más sencilla.
- Agrega los datos o agrúpalos en intervalos, toma una muestra con menos puntos o reduce la precisión de un conjunto de datos grande.
- Elimina cualquier control o biblioteca que se haya generado y no funcione.
- Verifica los valores importantes, los límites geográficos y los supuestos de las fuentes.
- Pide en su lugar un gráfico, un diagrama, una tabla o un Site.

Al manejar datos, aplica el mismo criterio que usarías en cualquier chat de ChatGPT. Solo
incluye información sensible cuando tu organización lo permita y revisa
el chat completo antes de compartirlo.

## Documentación relacionada

- [Sites](/es-419/codex/sites)
- [Proyectos y chats](/es-419/codex/projects)
- [Trabajar con archivos](/es-419/codex/artifacts-viewer)
- [Generación de imágenes](/es-419/codex/image-generation)
