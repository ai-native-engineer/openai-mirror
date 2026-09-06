<!-- source: https://learn.chatgpt.com/es-419/docs/customization/computer-history -->

El Historial de la computadora está **desactivado de forma predeterminada** para los usuarios de ChatGPT Pro, Business y
  Empresas en la aplicación de escritorio de ChatGPT en macOS. Los usuarios de Pro pueden
  elegir activarlo. En los espacios de trabajo de Business y Empresas, un administrador debe
  conceder acceso explícitamente antes de que cada miembro pueda elegir activarlo. El Historial
  de la computadora también requiere [Memorias](/es-419/codex/customization/memories) y no está
  disponible con una clave de API ni con Amazon Bedrock. Está disponible en regiones
  admitidas, incluidos el Espacio Económico Europeo (EEE), Suiza y el Reino
  Unido.

El Historial de la computadora convierte tu actividad en apps y sitios web en memorias y
una cronología que ChatGPT y Codex pueden consultar. Puedes preguntar de manera natural
por tu trabajo reciente, retomarlo donde lo dejaste, identificar patrones en tu forma de
trabajar y convertir los flujos de trabajo recurrentes en habilidades o automatizaciones.

Tu historial comienza solo cuando decides activarlo. Tú controlas qué apps y
sitios web contribuyen, puedes ver y pausar la recopilación desde la barra de menús de macOS y
consultar o eliminar tu historial en cualquier momento.

El Historial de la computadora reemplaza la anterior versión preliminar de investigación de Chronicle, pero es un
sistema reconstruido, no un simple cambio de nombre. Usa eventos de interacción, junto con texto y
otros datos contextuales disponibles a través de las funciones de accesibilidad de macOS, para
crear resúmenes que puedes revisar y eliminar. No incluye capturas de pantalla en tu historial ni
graba audio, y nunca incluye la actividad de navegación web en modo
privado.

  

## Cómo ayuda el Historial de la computadora

El Historial de la computadora ofrece contexto a partir de tu actividad reciente. Si un archivo, una
conversación de Slack, un documento de Google u otra fuente es más adecuada para la tarea, ChatGPT y
Codex pueden usar el historial para identificar esa fuente y después leerla directamente.

<section class="feature-grid mt-4">

<div>

### Retoma el trabajo donde lo dejaste

Pregunta qué estabas haciendo antes de una pausa sin tener que recordar cada app abierta,
cada documento ni el siguiente paso.

</div>

</section>

<section class="feature-grid inverse">

<div>

### Encuentra tu trabajo reciente

Menciona un documento, una conversación o una tarea según lo que recuerdes. El Historial de la
computadora puede usar la cronología de actividad para identificar la fuente a la que te refieres.

</div>

</section>

<section class="feature-grid">

<div>

### Reutiliza flujos de trabajo

Cuando el Historial de la computadora detecta tareas que se pueden repetir, una entrada de la cronología puede sugerir una
habilidad o automatización. Revisa la sugerencia y pídele a Codex que la cree a partir del
flujo de trabajo registrado.

</div>

</section>

## Cómo funciona el Historial de la computadora

El Historial de la computadora crea un flujo de eventos de interacción a partir de apps y
sitios web permitidos. Los eventos pueden incluir clics, escritura, atajos de teclado, cambios
entre apps y el contexto que macOS expone a través de su sistema de accesibilidad.
El Historial de la computadora convierte periódicamente estos eventos en resúmenes de texto
y archivos de memoria locales.

El Historial de la computadora no incluye capturas de pantalla en tu historial ni registra
la entrada del micrófono ni el audio del sistema. La actividad de navegación web
en modo privado nunca se incluye.

En **Configuración \> Historial de la computadora \> Historial**, la línea de tiempo agrupa los resúmenes por
día y hora. Cada elemento puede mostrar:

- Un título y un resumen escrito de la actividad.
- Las apps que contribuyeron al resumen.
- Una habilidad o automatización sugerida cuando ChatGPT identifica trabajo que puede repetirse.
- Acciones para mostrar el archivo de memoria en Finder o eliminar el elemento.

Selecciona **Preguntar sobre tu historial** para iniciar un chat con el Historial de la computadora o usa
prompts como:

- “¿En qué estaba trabajando antes de mi último descanso?”
- “¿Dónde puedo encontrar el documento de la propuesta que buscaba hoy más temprano?”
- “Dame una lista de las tareas en las que trabajé hoy y su estado”.
- “Prepara un resumen de lo que hice ayer para la reunión diaria”.

## Permisos y acceso

El Historial de la computadora usa controles independientes para el acceso al espacio de trabajo,
la activación voluntaria individual, las memorias y las apps o los sitios web incluidos en tu historial:

- **Acceso al espacio de trabajo:** el Historial de la computadora está desactivado de forma predeterminada en los espacios de trabajo de Business y
  Empresas, y no está disponible hasta que un administrador otorgue acceso
  de forma explícita. Los administradores de Empresas pueden usar **Habilitar el Historial
  de la computadora** en [**Configuración del espacio de trabajo \> Permisos y roles**](https://chatgpt.com/admin/settings)
  para conceder acceso a los roles correspondientes del espacio de trabajo.
- **Activación voluntaria individual:** conceder acceso al espacio de trabajo solo permite que un miembro decida
  activar el Historial de la computadora. Esto no activa la función para nadie. Cada
  persona debe decidir activarla de forma individual, incluidos los usuarios de ChatGPT Pro.
- **Memorias:** el Historial de la computadora también requiere [Memorias](/es-419/codex/customization/memories).
  Usa `/memories` para controlar si un chat individual puede usar memorias locales
  o contribuir a memorias futuras.
- **Apps y sitios web:** los permisos de tus apps y sitios web determinan qué
  fuentes pueden aportar eventos de interacción. Puedes permitir únicamente
  fuentes específicas o excluir las apps y las URL de sitios web que no quieras incluir.

Si tu rol en el espacio de trabajo no tiene acceso, modificar la configuración local no permite
activar el Historial de la computadora.

## Activar el Historial de la computadora

El Historial de la computadora está desactivado de forma predeterminada. Si usas un espacio de trabajo
de Business o Empresas, pídele a tu administrador que te conceda acceso antes de activarlo.
La aprobación del administrador no activa la función por ti.

1. Abre la aplicación de escritorio de ChatGPT en macOS.
2. En Configuración, en la sección **Integraciones**, selecciona **Historial de la computadora**.
3. Selecciona **Activar** y revisa la información sobre privacidad, permisos y almacenamiento
   local.
4. Si se te solicita, activa **Memorias**. El Historial de la computadora requiere Memorias para
   usar el contexto de la actividad en distintos chats y tareas.
5. Elige qué apps y sitios web pueden contribuir a tu historial y sigue las indicaciones
de permisos de macOS.

El Historial de la computadora no requiere el permiso de Grabación de pantalla. Si la opción
no aparece, confirma que tu plan sea compatible con el Historial de la computadora y que,
si corresponde, el administrador de tu espacio de trabajo lo haya habilitado.

## Controlar qué se incluye

Puedes controlar qué apps y sitios web contribuyen al historial futuro y si el Historial de la computadora
está recopilando eventos de interacción.

### Elegir apps y sitios web

En **Configuración \> Historial de la computadora \> Permisos**, elige qué apps y
sitios web puede incluir el Historial de la computadora:

- **Excluir estas apps** y **Excluir estos sitios web** bloquean las apps o las URL
  que indiques y permiten otras fuentes compatibles.
- **Incluir solo estas apps** e **Incluir solo estos sitios web** permiten únicamente las
  fuentes que elijas de forma explícita.

También puedes seleccionar el ícono de una app en un elemento de la línea de tiempo del historial
para excluirla del historial futuro. Puedes volver a incluirla más adelante.

La actividad de navegación web en modo privado nunca se incluye. Cambiar los permisos de apps
o sitios web afecta el historial futuro. Para quitar elementos existentes, elimínalos
o borra el historial.

### Pausar, reanudar o detener la recopilación

Usa la configuración del Historial de la computadora o la barra de menús de macOS para controlar
cuándo la función recopila actividad:

- Selecciona el ícono de ChatGPT en la barra de menús de macOS y despliega el menú del Historial
de la computadora para ver qué actividad registra y acceder a sus controles.
- Selecciona **Pausar** para detener la recopilación de nuevos eventos de interacción o selecciona
**Reanudar** cuando quieras volver a iniciarla.
- Desactiva el Historial de la computadora para detener la recopilación de actividad futura.

El Historial de la computadora puede incluir eventos de interacción de apps y sitios web
de comunicación. Desactívalo cuando te comuniques con otras personas, a menos que cuentes
con su consentimiento expreso previo. Considera pausarlo o excluir las apps que contengan
información sensible de salud, financiera o personal.

## Revisar y borrar el historial

Abre **Configuración \> Historial de la computadora \> Historial** para revisar lo que el Historial de la computadora
ha resumido. Puedes mostrar en Finder el archivo de memoria local de un resumen, eliminar
un elemento individual de la línea de tiempo o borrar los últimos 10 minutos, la última hora, el último día
o todo el historial. La barra de menús de macOS también permite borrar la última sesión de una app
reciente.

Borrar el historial elimina los eventos de interacción correspondientes y todas las memorias
creadas a partir de ellos. Esta acción no se puede deshacer.

## Privacidad y almacenamiento local

El Historial de la computadora almacena temporalmente el flujo de eventos de interacción en tu Mac para que
ChatGPT y Codex puedan generar memorias y crear flujos de trabajo sugeridos. El flujo
puede incluir actividades como clics y escritura, junto con texto y otro contexto
disponible a través de las funciones de accesibilidad de macOS. El Historial de la computadora
no incluye capturas de pantalla en tu historial ni registra la entrada del micrófono
ni el audio del sistema. La actividad de navegación web en modo privado nunca se incluye.

Los archivos temporales de eventos se conservan durante un máximo de 48 horas. Los archivos de memoria
generados permanecen en tu sistema de archivos hasta que los elimines o borres el historial,
y puedes mostrarlos desde la línea de tiempo del historial.

### ¿Dónde almacena mis datos el Historial de la computadora?

El Historial de la computadora guarda temporalmente los eventos de interacción en tu Mac. Los archivos
de eventos se mantienen aislados dentro del
[App Group](https://developer.apple.com/documentation/xcode/protecting-local-app-data-using-containers) de ChatGPT,
lo que impide que otras apps accedan a ellos sin permiso explícito.
ChatGPT y Codex eliminan estos archivos de eventos después de 48 horas.

El Historial de la computadora genera el mismo tipo de memorias locales que Codex: archivos Markdown
de texto sin formato que puedes leer y modificar. Estos archivos se almacenan
en `$CODEX_HOME/memories/extensions/skysight/`, que normalmente corresponde a
`~/.codex/memories/extensions/skysight/`.

<div className="not-prose my-4">
  
</div>

### ¿Qué datos se comparten con OpenAI?

El Historial de la computadora registra los eventos de interacción localmente y, de forma periódica,
inicia una sesión efímera de Codex con acceso al flujo de eventos de interacción para
resumir tu actividad en memorias.

OpenAI procesa los archivos temporales de eventos en sus servidores para generar memorias,
que luego se almacenan localmente en tu Mac. OpenAI no conserva esos archivos de eventos
después de procesarlos, a menos que lo exija la ley, y no los usa con fines de
entrenamiento.

Cuando ChatGPT o Codex usa una memoria en un chat futuro, el contenido relevante de la memoria
y los eventos de interacción pueden incluirse como contexto. El contenido de ese chat puede
usarse para mejorar los modelos de OpenAI si lo permiten tus
[controles de datos de ChatGPT](https://help.openai.com/en/articles/7730893-data-controls-faq).
Las memorias también están sujetas a los mismos
[controles por chat que las demás memorias de Codex](/es-419/codex/customization/memories#control-memories-per-chat).

### Riesgo de inyección de prompts

El Historial de la computadora aumenta el riesgo de inyección de prompts a partir del contenido
de apps y sitios web. Por ejemplo, si visitas un sitio web que contiene instrucciones maliciosas,
ChatGPT o Codex podrían seguirlas.

## Uso de tokens

El Historial de la computadora usa tokens al resumir la actividad y crear memorias.

## Solución de problemas

Si el Historial de la computadora está disponible, pero no se inicia:

1. Confirma que la función **Memorias** esté activada.
2. Abre **Configuración \> Historial de la computadora** y selecciona **Finalizar la configuración**, **Reanudar**
   o **Intentar de nuevo**, según el estado que aparezca.
3. Cierra y vuelve a abrir la aplicación de escritorio de ChatGPT si la configuración sigue sin estar disponible.
