<!-- source: https://learn.chatgpt.com/es-419/use-cases/build-an-ai-tour-guide -->

## Introducción

Algunos flujos de trabajo son más fáciles de aprender cuando alguien te muestra adónde ir y qué seleccionar. Usa Codex para crear un recorrido que guíe a los usuarios por tu aplicación web mientras realizan las acciones por su cuenta.

Con herramientas de WebMCP para los controles, el estado y la documentación de tu aplicación, Codex puede elegir la siguiente instrucción según lo que ve el usuario. Un usuario que no ha conectado un servicio necesita un primer paso distinto al de alguien que ya completó la configuración.

## Cómo usarlo

1. Abre el repositorio de tu aplicación en Codex y elige un flujo de trabajo para guiar al usuario, como conectar un servicio o agregar una carpeta.
2. Proporciona la documentación pertinente y describe los estados iniciales que el recorrido debería contemplar.
3. Ejecuta el prompt inicial de esta página para agregar elementos del recorrido, herramientas para consultar el estado de la interfaz y acceso a las instrucciones de la aplicación.
4. Prueba el flujo en un entorno de navegador donde Codex pueda llamar a las herramientas de WebMCP de tu aplicación. Pídele a Codex que te guíe y luego completa cada paso por tu cuenta.

Limita el alcance del primer recorrido. Verifica que pueda guiar a un usuario desde la configuración hasta completar el flujo antes de agregar más flujos de trabajo.

## Ejemplo: agrega una carpeta de Google Drive en Runme

En <a href="https://web.runme.dev" target="_blank" rel="noopener noreferrer">Runme</a>, los usuarios editan cuadernos y usan un explorador de archivos para agregar carpetas de Google Drive y navegar por sus archivos. El recorrido ayuda a un nuevo usuario a encontrar esos controles y aprender el flujo.

Para conocer más sobre Runme, puedes leer <a href="https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex" target="_blank" rel="noopener noreferrer">Automatizar tareas repetitivas en OpenAI con Codex</a>.

Mira cómo Codex resalta los controles de Runme y explica para qué sirven. Las siguientes capturas de pantalla muestran un recorrido distinto, centrado en la tarea de agregar una carpeta de Google Drive.

<figure class="not-prose my-4">
  <video
    class="w-full rounded-lg border border-default"
    controls
    muted
    playsinline
    preload="metadata"
    poster="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/tour-demo-poster.webp"
    aria-label="Codex demonstrates an AI tour of Runme's controls"
  >
    <source
      src="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/runme-ai-tour-demo.webm"
      type="video/webm"
    />
    Tu navegador no admite la etiqueta de video.
  </video>
</figure>

El recorrido de Google Drive comienza con una solicitud:

### Conecta Google Drive

Codex comprueba si Google Drive está conectado. Si no lo está, Codex resalta **Conectar Google Drive** y le pide al usuario que lo seleccione y complete la conexión.

![Codex resalta Conectar Google Drive en Runme y explica cómo empezar.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/connect-google-drive.webp)

### Abre el explorador de archivos

Una vez completada la conexión, Codex guía al usuario al explorador de archivos. La siguiente instrucción se adapta al estado actualizado de la aplicación.

![Codex resalta el control para abrir el explorador de archivos de Runme.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/open-file-explorer.webp)

### Agrega la carpeta

Una vez que el usuario expande la barra de herramientas, Codex resalta el control para agregar una carpeta de Google Drive. El usuario mantiene el control de la interacción y aprende dónde encontrar ese control la próxima vez.

![Codex resalta el control para agregar una carpeta de Google Drive en Runme.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/add-google-drive-folder.webp)

## Dale a Codex el contexto para guiar a los usuarios

La implementación de Runme proporciona tres tipos de contexto: elementos del recorrido, estado de la aplicación y documentación. Los nombres de las herramientas que se muestran a continuación corresponden a Runme; adapta esas mismas funciones a tu aplicación.

### Permite detectar los controles

Asigna a los elementos del recorrido valores de `data-tour-id` estables y semánticos, con una etiqueta y una descripción para cada uno. Runme expone estos controles a través de tres herramientas de WebMCP:

- `listTargets` enumera los elementos registrados, sus IDs, etiquetas y descripciones.
- `showTourStep({ target, title?, message, placement? })` resalta un elemento y muestra una explicación.
- `dismiss` quita el resaltado.

Esto le permite a Codex identificar un control y explicar para qué sirve sin realizar su acción por el usuario.

### Lee el estado y espera al usuario

Runme mantiene el estado relacionado con el recorrido fuera de React y lo expone a través de un controlador. Su herramienta `getUiSnapshot` proporciona el estado actual de la interfaz, incluido el estado de inicio de sesión. `waitForUiChange(...)` permite que Codex espere un cambio, como que el usuario seleccione el control resaltado.

Pídele a Codex que vuelva a leer el estado después de cada interacción. El avance del recorrido debería depender de lo que ocurrió en la aplicación, no de si Codex ya mostró una instrucción.

### Incluye las instrucciones en la aplicación

Runme incluye documentación en Markdown junto con la aplicación y la pone a disposición a través de WebMCP:

- `readInstructionsForAIAgents` explica cómo debería interactuar Codex con la aplicación y sus herramientas.
- `listDocumentation()` enumera las páginas disponibles y sus descripciones.
- `getDocumentation({ name })` devuelve una página seleccionada en formato Markdown.

Las instrucciones y herramientas del recorrido se pueden distribuir junto con la aplicación, sin un complemento de Codex aparte para el recorrido.

## Revisa el recorrido

Prueba la misma solicitud desde distintos estados iniciales. Comprueba que el recorrido omita la configuración ya completada, espere al usuario y actualice sus indicaciones cuando cambie la interfaz.

También prueba un paso cancelado y un control que aún no sea visible. Codex debería explicar qué falta o elegir un siguiente paso válido. No debería afirmar que una acción se completó correctamente solo porque resaltó un botón.

Mantén la autenticación, las verificaciones de permisos y las acciones del usuario en el flujo existente de la aplicación. El recorrido debería ayudar a los usuarios a entender la interfaz sin eludir esos controles.

## Sugerencias para continuar

Una vez que funcione el primer flujo, continúa en el mismo chat:

- “Prueba este recorrido cuando Google Drive ya esté conectado y el explorador de archivos esté cerrado”.
- “Maneja el caso de un usuario que cancela un paso y luego pide continuar el recorrido”.
- “Agrega un recorrido para \[next workflow\], reutilizando los elementos de destino y las herramientas de estado existentes”.
