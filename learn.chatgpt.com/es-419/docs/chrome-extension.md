<!-- source: https://learn.chatgpt.com/es-419/docs/chrome-extension -->

Usa la extensión de ChatGPT para el navegador para trabajar en Google Chrome, Microsoft Edge,
Brave, Opera o Vivaldi desde la aplicación de escritorio de ChatGPT. ChatGPT puede leer contenido o realizar acciones
en sitios donde ya iniciaste sesión, como LinkedIn, Salesforce, Gmail
o herramientas internas.

Los cinco navegadores permiten mencionar pestañas y controlar el navegador desde la aplicación
de escritorio. Chrome, Edge, Brave y Vivaldi también permiten usar el chat lateral. **Opera no admite
el chat lateral**; inicia sus tareas desde la aplicación de escritorio.

Actualiza la aplicación de escritorio de ChatGPT antes de configurar otro navegador. La disponibilidad
de los navegadores puede depender del despliegue y de la configuración de tu espacio de trabajo.

Si prefieres que ChatGPT controle su navegador integrado, usa `@Browser`. El
[navegador integrado](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app)
permite iniciar sesión y mantiene las tareas de navegación dentro de ChatGPT sin usar tu
perfil de navegador habitual.

ChatGPT también puede cambiar de herramienta según lo requiera la tarea: usa complementos cuando hay una
integración específica disponible; tu navegador, cuando necesita el contexto de un navegador
con una sesión iniciada; y el navegador integrado para localhost.

<div className="not-prose my-4">
  
</div>

<a id="use-chatgpt-from-chrome"></a>

## Usar el chat lateral en tu navegador

El chat lateral está disponible en Chrome, Edge, Brave y Vivaldi.

Abre ChatGPT junto a la página que estás viendo para hacer preguntas sobre ella o continuar
con tareas que puedan usar su contexto junto con archivos locales y Apps conectadas.
ChatGPT puede usar el contexto de las pestañas abiertas cuando una tarea lo requiera.

1. Abre la página con la que quieras trabajar.
2. Selecciona ChatGPT en la barra de herramientas del navegador o en el menú **Extensiones** . En macOS, también
   puedes presionar <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd>.
3. Haz una pregunta sobre la página o asigna una tarea a ChatGPT.

El panel permanece en la pestaña donde lo abriste. Los chats que inicies en el chat lateral
están disponibles en la aplicación de ChatGPT, y puedes abrir chats recientes de ChatGPT en
el chat lateral para continuar tu trabajo en cualquiera de los dos lugares.

  

## Agregar pestañas y texto seleccionado a un chat

Menciona una pestaña abierta del navegador en la aplicación de escritorio cuando quieras que ChatGPT use
esa página como contexto. En los navegadores con chat lateral, también puedes mencionar pestañas
en ese chat o seleccionar texto en una página y agregar la selección a tu chat para
preguntar sobre un fragmento específico sin copiar toda la página.

En los navegadores con chat lateral, también puedes hacer clic con el botón derecho en la página y seleccionar
**Preguntar a ChatGPT**. El chat lateral se abre con el contexto pertinente de la página para que puedas
continuar la solicitud en tu navegador.

### Preguntar sobre un video de YouTube

Abre un video de YouTube y haz una pregunta sobre él en el chat lateral de un navegador compatible.
Cuando haya subtítulos disponibles, ChatGPT podrá usar la transcripción del video con marcas de tiempo
para explicar, resumir o responder preguntas sobre el contenido.

Considera el contenido de las páginas web, el texto seleccionado y las transcripciones de videos como
contexto no confiable. Revisa la página y todos los permisos solicitados antes de pedirle a ChatGPT que
use esa información o realice acciones basadas en ella.

<a id="set-up-the-chrome-extension"></a>

## Configurar tu navegador

Instala el navegador en tu computadora y abre **Configuración \> Uso de la computadora** en
la aplicación de escritorio de ChatGPT. Expande **Más navegadores** si tu navegador no aparece
en la lista principal.

1. Selecciona tu navegador y sigue las indicaciones que aparezcan para instalar el complemento necesario.
2. Selecciona **Instalar** junto al navegador para abrir su página en la tienda de extensiones.
   Instala la extensión de ChatGPT y revisa las solicitudes de permisos del navegador.
3. Vuelve a **Uso de la computadora** y confirma que el navegador muestre **Administrar**.
4. Inicia un chat de ChatGPT Work o Codex y selecciona tu navegador mediante
una mención con `@`. Usa el perfil del navegador donde instalaste la extensión.

El interruptor del navegador en **Uso de la computadora** determina si este aparece en el
menú de menciones con `@`. Para cambiar los permisos de los sitios web, selecciona **Administrar** .

  

<a id="start-a-chrome-task-from-chatgpt"></a>

## Iniciar una tarea en el navegador desde ChatGPT

Después de la configuración, inicia un chat nuevo de ChatGPT Work o Codex. Selecciona **Chrome**, **Edge**,
**Brave Browser**, **Opera** o **Vivaldi** en el menú de menciones con `@` para elegir
qué navegador usa ChatGPT. Por ejemplo:

```text
@Edge open Salesforce and update the account from these call notes.

También puedes mencionar una pestaña abierta para darle a ChatGPT el contexto de esa página.
Opera admite estos flujos de trabajo desde la aplicación de escritorio, aunque no tiene chat lateral.

## Controlar el acceso a sitios web

De forma predeterminada, ChatGPT solicita permiso antes de interactuar con cada sitio web nuevo. ChatGPT basa
la solicitud en el host del sitio web, por ejemplo, `example.com`.

Cuando ChatGPT solicite usar un sitio web, puedes elegir la opción que corresponda a la
tarea y a tu tolerancia al riesgo:

- **Permitir una vez** para que ChatGPT use el sitio web una sola vez.
- **Permitir para este sitio** para que ChatGPT pueda volver a usar el sitio web sin pedir permiso.
- **Permitir para todos los sitios** para que ChatGPT pueda usar sitios web sin pedir permiso.
- **Rechazar** para impedir que ChatGPT use el sitio web.

### Administrar sitios web permitidos y bloqueados

En la aplicación de escritorio de ChatGPT, ve a **Configuración** \> **Uso de la computadora** y selecciona
**Administrar** junto a tu navegador para administrar una lista de dominios permitidos y otra de
dominios bloqueados. La lista de dominios permitidos contiene los que ChatGPT puede usar sin volver a pedir permiso.
La lista de dominios bloqueados contiene los que ChatGPT no debe usar. Los navegadores compatibles
comparten estos permisos de sitios web.

Si quitas un dominio de la lista de dominios permitidos, ChatGPT volverá a pedir permiso antes de usarlo.
Si quitas un dominio de la lista de dominios bloqueados, ChatGPT podrá volver a pedir permiso en lugar de
tratarlo como bloqueado.

#### Permitir para todos los sitios 

Si seleccionas **Permitir para todos los sitios**, ChatGPT deja de pedir confirmación
antes de usar sitios web. Elige esta opción solo si confías en que ChatGPT use cualquier
sitio web abierto en el navegador.

#### Historial de navegación 

El historial de navegación puede incluir datos de telemetría sensibles, URLs internas, términos de búsqueda
y actividad de sesiones del navegador en dispositivos donde hayas iniciado sesión. Si permites que ChatGPT
acceda al historial de navegación, las entradas pertinentes pueden pasar a formar parte del contexto que
ChatGPT usa para la tarea. El contenido malicioso o engañoso de una página puede aumentar el
riesgo de que ChatGPT copie estos datos en un lugar no previsto.

ChatGPT solicita permiso cuando quiere usar el historial de navegación. ChatGPT limita el acceso al historial al ámbito de
la solicitud, y el historial no ofrece una opción para permitir siempre el acceso.

## Datos y seguridad

<a id="chrome-extension-permissions"></a>

### Permisos de la extensión del navegador

Tu navegador te pide que aceptes los permisos cuando instalas la extensión.
Por ejemplo, la solicitud de permisos de Chrome puede incluir:

- Acceder al depurador de la página
- Leer y modificar todos tus datos en todos los sitios web
- Leer y modificar tu historial de navegación en todos los dispositivos en los que hayas iniciado sesión
- Mostrar notificaciones
- Leer y modificar tus marcadores
- Administrar tus descargas
- Comunicarse con aplicaciones nativas que colaboran con la extensión
- Ver y administrar tus grupos de pestañas

Estos permisos permiten que la extensión ejecute flujos de trabajo en el
navegador. ChatGPT sigue aplicando sus propias confirmaciones, opciones de configuración, listas de sitios permitidos y
listas de sitios bloqueados antes de usar sitios web o el historial del navegador durante una tarea.

### Memorias

Uso de la computadora respeta tu configuración de Memorias. Si la función Memorias está activada, ChatGPT puede
usar memorias guardadas relevantes mientras trabaja en tu navegador. Si está desactivada,
el control del navegador no usa memorias.

### Qué guarda OpenAI de tu navegación

OpenAI no guarda por separado un registro completo de tus acciones en el navegador realizadas a través de la
extensión. OpenAI solo guarda la actividad del navegador cuando pasa a formar parte del contexto de ChatGPT,
como el texto que ChatGPT lee en una página, capturas de pantalla, llamadas a herramientas,
resúmenes, mensajes u otro contenido incluido en el chat.

Tus controles de datos de ChatGPT se aplican al contenido procesado en el contexto.
Evita enviar secretos o datos muy sensibles mediante tareas del navegador, a menos que
sean necesarios y estés presente para revisar cada prompt.

## Solución de problemas

Si ChatGPT no puede conectarse a tu navegador, primero confirma que el sitio web al que intenta
acceder no esté en la lista de sitios bloqueados de Configuración. Si el sitio web no está bloqueado, realiza
estas comprobaciones:

1. Actualiza la aplicación de escritorio de ChatGPT. Si tienes instalada más de una aplicación de escritorio de ChatGPT o Codex,
actualiza cada una o elimina las copias que ya no uses.
2. Reinicia tu navegador. En Chrome, Edge, Brave o Vivaldi, vuelve a abrir ChatGPT desde
   la barra de herramientas o el menú **Extensiones** y confirma que se cargue el chat lateral. Opera
   no tiene chat lateral; comprueba su conexión desde la aplicación de escritorio.
3. En **Configuración \> Uso de la computadora**, confirma que tu navegador aparezca y muestre
**Administrar**. Si todavía muestra **Instalar**, vuelve a seguir el proceso de configuración.
   Activa su interruptor si el navegador no aparece en el menú de menciones con `@`.
4. Asegúrate de usar el perfil del navegador en el que está instalada la
extensión. Si usas más de un perfil, instala y activa la
extensión en el perfil activo.
5. Inicia un chat nuevo de ChatGPT Work o Codex y vuelve a intentar la tarea del navegador. Esto puede
borrar el estado de conexión específico del chat.
6. Reinicia la aplicación de escritorio de ChatGPT y vuelve a intentarlo. Si la extensión aún
   no se conecta, vuelve a instalarla desde **Configuración \> Uso de la computadora**.
7. Si ChatGPT aún no puede usar el navegador, ejecuta `/feedback`
   en la aplicación e incluye el ID del chat cuando te comuniques con soporte.

### Subir archivos

Si una tarea de Chrome necesita subir un archivo desde tu computadora, permite que la Extensión de Chrome
acceda a URLs de archivo en Chrome:

1. En Chrome, selecciona el ícono de extensiones de la barra de herramientas y luego haz clic en **Administrar
   extensiones**.
2. En la tarjeta de la extensión, haz clic en **Detalles**.
3. Activa **Permitir acceso a URLs de archivo**.

Después de cambiar la configuración, vuelve a iniciar la tarea de Chrome.
