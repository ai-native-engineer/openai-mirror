<!-- source: https://learn.chatgpt.com/es-419/docs/webmcp -->

Las herramientas del sitio implementan en ChatGPT el
[estándar WebMCP](https://webmachinelearning.github.io/webmcp/) propuesto. Con WebMCP,
un sitio web puede ofrecer acciones útiles directamente a un agente de IA junto con la
interfaz que las personas ya usan. Tú y el agente pueden trabajar con la misma página en tiempo real
y la misma sesión iniciada.

En el [navegador integrado](/es-419/codex/browser) de la aplicación de escritorio de ChatGPT,
ChatGPT Work y Codex pueden descubrir y usar estas herramientas cuando están disponibles.

  Usa GPT-5.6 Sol o GPT-5.6 Terra para las herramientas del sitio. GPT-5.6 Luna tiene
WebMCP desactivado por el momento. Actualiza la aplicación de escritorio de ChatGPT a la última versión. Las herramientas
del sitio no están disponibles en espacios de trabajo de Empresas o Edu. Su disponibilidad también
depende del despliegue y de las herramientas que ofrece la página actual.

## WebMCP frente a MCP

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/learn/architecture)
conecta una aplicación de IA con un servidor local o remoto. Sus herramientas pueden funcionar
independientemente de una página web abierta, por ejemplo, para buscar en un servicio o administrar
registros a través de una API.

[WebMCP](https://github.com/webmachinelearning/webmcp) permite que un sitio web ponga sus
capacidades a disposición de un agente como un conjunto de herramientas predefinidas. El agente puede
descubrirlas al visitar el sitio, por lo que los usuarios no necesitan instalar un servidor MCP
independiente ni configurar otra conexión para usar esas capacidades.

Este enfoque es útil cuando tú y el agente necesitan ver lo mismo, por ejemplo,
al editar un lienzo o explorar un panel. Un
[complemento con un servidor MCP](/es-419/codex/build-plugins) puede ofrecer una integración
que funcione independientemente de una página abierta. Un sitio web puede admitir ambas opciones.

## Cómo funciona en el navegador

Abre un sitio web en el navegador integrado y pídele a ChatGPT Work o a Codex que te ayude
con una tarea. Si la página ofrece herramientas del sitio, el agente puede descubrir y usar las
acciones pertinentes en el sitio web que estás viendo. Por ejemplo, un editor de
documentos podría permitirle al agente encontrar una sección o dejar un comentario para que lo revises.

Selecciona **Herramientas del sitio** en la barra de direcciones del navegador para ver qué
ofrece el sitio web. Elige **Herramientas del sitio disponibles** para inspeccionar cada herramienta. El
navegador revisa cada solicitud antes de que el sitio web la ejecute, y el agente
puede inspeccionar la página para ver qué cambió. Cuando haya actividad reciente disponible,
elige **Usadas recientemente** para abrir **Fuentes** y revisar esas llamadas.

En este ejemplo, despliega **Herramientas del sitio disponibles** para inspeccionar las herramientas que ofrece
[Margin](https://margin-local-docs.openai.chatgpt.site).

  

Las herramientas pertenecen a la página que las ofrece. Al cerrar una página o navegar a otra,
sus herramientas pueden dejar de estar disponibles. Si no hay una herramienta adecuada disponible,
es posible que el agente aún pueda usar sus capacidades habituales de navegación.

## Ejemplo: explora la documentación de OpenAI

ChatGPT Learn y OpenAI Developers ofrecen herramientas del sitio para buscar y leer
documentación. Selecciona **Abrir en ChatGPT** en el editor para abrir Learn en el
navegador de la aplicación de escritorio junto a un chat nuevo con este prompt listo para enviar.

El agente puede usar estas herramientas para buscar, leer y abrir la página correspondiente:

| Herramienta                    | Qué hace                                                             |
| ----------------------- | ------------------------------------------------------------------------ |
| `search_openai_docs`    | Busca en la documentación de OpenAI.                                           |
| `lookup_page`           | Lee una página de documentación a partir de su ruta o URL.                               |
| `lookup_context`        | Lee la ruta actual de la documentación y el texto seleccionado.                          |
| `navigate_to_page`      | Abre una página coincidente en el sitio de documentación actual.                 |
| `generate_custom_guide` | Inicia la generación de una guía personalizada de desarrollo o aprendizaje y devuelve su estado y enlace. |

El Agente de documentación genera una guía personalizada de forma asíncrona. Recibir su enlace no
significa que la generación haya terminado.

## Seguridad y controles del usuario

Las definiciones y los resultados de las herramientas que proporciona un sitio web son contenido no confiable. El
nombre de una herramienta o la afirmación de que solo lee datos no demuestran lo que hace. Las instrucciones
del sitio web no le dan permiso al agente para compartir información no relacionada ni
realizar acciones sensibles.

En el navegador integrado, cada llamada a una herramienta pasa por una revisión de seguridad antes
de ejecutarse. Las políticas habituales de acceso a sitios web y de confirmación siguen vigentes, incluso
para acciones con consecuencias importantes, como enviar mensajes, hacer compras, eliminar
datos o cambiar permisos. El navegador vincula cada llamada con la
página que la originó y el registro de la herramienta. Estas comprobaciones reducen el riesgo; no
hacen que un sitio web o sus resultados sean confiables.

Puedes desactivar **Habilitar herramientas del sitio** en **Configuración \> Navegador \> Permisos**.
Revisa el sitio, la acción solicitada y el resultado antes de compartir información
sensible o confiar en un cambio.

Reporta las vulnerabilidades de seguridad a través del
[Programa de recompensas por la detección de errores de seguridad](https://bugcrowd.com/engagements/openai) de OpenAI. Para los riesgos
de seguridad de la IA, consulta el
[Programa de recompensas por la detección de errores de seguridad de la IA](https://openai.com/index/safety-bug-bounty/). Respeta
el alcance y las instrucciones de envío de cada programa.

## Limitaciones

Actualmente, el navegador integrado de ChatGPT admite un subconjunto de las API de WebMCP.
No admite las siguientes funciones:

- **API declarativa:** las herramientas definidas mediante atributos de formularios HTML no están
  disponibles como herramientas del sitio.
- **Herramientas en iframes:** el navegador no descubre herramientas registradas dentro de
  iframes, incluidos los del mismo origen y los de otros orígenes.

Usa JavaScript para registrar herramientas en la página de nivel superior, como se muestra en la
[siguiente sección](#add-webmcp-to-your-website). ChatGPT Work y Codex pueden seguir
interactuando con formularios mediante las funciones habituales del navegador, pero esas interacciones
no son llamadas a herramientas de WebMCP.

La especificación de WebMCP y la guía de Chrome para desarrolladores describen un conjunto más amplio de
API, incluidas funciones que el navegador integrado aún no admite.

## Agrega WebMCP a tu sitio web

Puedes pedirle a Codex que agregue compatibilidad con WebMCP a la aplicación web o al
[Site](/es-419/codex/sites) en el que estás trabajando. Describe lo que un agente debería poder
hacer y pídele a Codex que reutilice la lógica y los permisos existentes de la aplicación.

Comienza con una operación que tu aplicación ya permita realizar. Por ejemplo:

- Un panel que permita al agente establecer un rango de fechas y examinar los datos en los que se basa
un gráfico.
- Un editor de documentos que permita al agente encontrar una sección, sugerir una modificación o
dejar un comentario para que lo revises.
- Un planificador de viajes que permita al agente comparar opciones y actualizar un itinerario
mientras revisas el mapa.

También puedes escribir el código por tu cuenta. En el módulo JavaScript de tu página, verifica
la compatibilidad del navegador y registra una herramienta. Este ejemplo de solo lectura devuelve el
título de la página actual:

```javascript
if (typeof document.modelContext?.registerTool === "function") {
  await document.modelContext.registerTool({
    name: "get_page_title",
    description: "Read the title of the current page.",
    inputSchema: {
      type: "object",
      properties: {},
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true },
    execute: async () => ({ title: document.title }),
  });
}

Un agente compatible puede descubrir `get_page_title` y recibir el título
actual de la página. Si una herramienta acepta argumentos, descríbelos en el esquema
de entrada y úsalos en el controlador `execute` para invocar la lógica
existente de tu aplicación.

Limita el alcance de las entradas, describe los efectos secundarios y devuelve información suficiente para
verificar el resultado. Usa los mecanismos de autenticación,
autorización y validación de entradas que ya tiene tu aplicación. Conserva la interfaz habitual para las personas
y para los navegadores que no sean compatibles con WebMCP.

Para obtener detalles de la API y ejemplos, consulta la
[especificación de WebMCP](https://webmachinelearning.github.io/webmcp/) y la
[guía de Chrome para desarrolladores](https://developer.chrome.com/docs/ai/webmcp).
