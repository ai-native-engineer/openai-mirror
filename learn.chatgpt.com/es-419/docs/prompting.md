<!-- source: https://learn.chatgpt.com/es-419/docs/prompting -->

<a id="prompts"></a>

## Descripción general del diseño de prompts

El diseño de prompts es la forma en que le indicas a ChatGPT lo que quieres saber, crear o cambiar. Un prompt
puede ser una pregunta, una instrucción o un objetivo. No necesitas sintaxis técnica ni
una fórmula rígida. Empieza con tus propias palabras, revisa la respuesta y usa mensajes de seguimiento
para dar forma al resultado.

Un prompt breve suele bastar. Para tareas más extensas o importantes, incluye los
aspectos relevantes:

- **Objetivo:** ¿qué debe hacer ChatGPT?
- **Contexto:** ¿qué información o fuentes serán útiles?
- **Resultado:** ¿qué formato, extensión o nivel de detalle necesitas?
- **Límites:** ¿qué debe permanecer sin cambios? ¿Qué debe evitar ChatGPT o consultarte
  antes de actuar?

Usa solo los elementos que sean útiles. No tienes que completar todos los puntos ni seguir un
formato obligatorio.

## Describe el resultado que necesitas

Empieza por el resultado, no por una lista detallada de pasos. Incluye el público o
el formato cuando esos detalles cambien lo que ChatGPT debe generar.

```text
Turn these meeting notes into a short update for the project team.
Put the decisions and next steps first.

Este prompt explica qué crear y quién lo leerá. Describe un proceso cuando
el proceso en sí sea importante. De lo contrario, dale margen a ChatGPT para buscar y comparar
información y ajustar su enfoque.

<a id="context"></a>

## Agrega contexto útil

Comparte la información que podría cambiar el resultado. Agrega solo las fuentes
relevantes y explica qué debe obtener ChatGPT de cada una.

- Adjunta documentos, hojas de cálculo, presentaciones o archivos PDF cuando quieras que
  ChatGPT los resuma, compare o transforme, o que [cree archivos para revisión](/es-419/codex/artifacts-viewer).
- Agrega una captura de pantalla, un diagrama u otra [entrada de imagen](/es-419/codex/image-inputs) cuando la
  tarea dependa del contexto visual. Indica el área relevante en vez de
  depender únicamente de la imagen.
- Pídele a ChatGPT que use la [búsqueda web](/es-419/codex/web-search) cuando la respuesta dependa de
  información actualizada y que incluya las fuentes cuando necesites comprobar el resultado.
- Usa un [proyecto](/es-419/codex/projects) cuando los chats relacionados deban compartir archivos,
  fuentes o una carpeta local.

### Usa fuentes conectadas

Cuando ChatGPT tenga acceso a fuentes conectadas, indica dónde debe buscar y qué
debe encontrar. No necesitas describir cada búsqueda que debe realizar.

```text
Use the latest project plan in Drive and relevant decisions and updates from
the project's Slack channel to prepare a status update.

Las fuentes conectadas requieren el complemento correspondiente, y su disponibilidad puede depender de
tu plan y de la configuración del espacio de trabajo.

### Usa complementos

Los complementos brindan a ChatGPT y Codex instrucciones reutilizables y conexiones con herramientas
como Google Drive, Gmail, Slack y GitHub. Ambos productos obtienen complementos públicos
del mismo directorio universal. Pide el resultado que necesitas y deja que
la interfaz activa elija entre las herramientas disponibles. En ChatGPT, escribe `@`
en el editor para elegir un complemento específico.

  
    <span slot="icon">
      
    </span>
    Busca, instala y usa complementos en ChatGPT y Codex.
  

### Personaliza ChatGPT

Configura en **Configuración \> Personalización**
las preferencias que deban aplicarse a todos los chats como instrucciones personalizadas. Mantén en el
prompt los detalles que solo sean relevantes para el chat actual.

  
    <span slot="icon">
      
    </span>
    Configura una personalidad predeterminada, instrucciones personalizadas y otras preferencias de la aplicación.
  

## Establece límites para evitar problemas reales

Los límites son unas cuantas instrucciones que ChatGPT necesita para evitar generar trabajo adicional
o realizar una acción que no pretendías. Agrega uno cuando modificar el detalle equivocado
vuelva inutilizable el resultado o cuando quieras revisar algo antes de que
afecte a otras personas.

- Mantén sin cambios las fechas aprobadas y las cifras del presupuesto.
- Usa solo las fuentes proporcionadas. Indica qué información falta en lugar de hacer suposiciones.
- Mantén las recomendaciones dentro del presupuesto indicado.
- Prepara el mensaje como borrador. No lo envíes.

Concéntrate en uno o dos de los límites más importantes. No necesitas controlar
cada paso que dé ChatGPT.

## Deja el resultado listo para usar

Indícale a ChatGPT cómo planeas usar el resultado. Esto le ayuda a elegir la
extensión, el nivel de detalle y la organización adecuados.

- Convierte esto en un resumen de una página que un director pueda revisar rápidamente antes de la reunión. Coloca primero la
decisión y los próximos pasos.
- Convierte estas notas en un correo electrónico de seguimiento que incluya las decisiones, las personas responsables y las fechas
de entrega.
- Crea una tabla clara que compare el gasto planificado con el real y resalta cualquier
diferencia superior al 10 %.

Para trabajos importantes, pídele a ChatGPT una revisión final, como confirmar que cada
tarea pendiente tenga una persona responsable y una fecha de entrega, o señalar la información que no pudo
verificar. Luego revisa tú mismo el resultado antes de usarlo o compartirlo.

## Mejora el resultado con mensajes de seguimiento

El primer prompt no tiene que ser perfecto. Revisa el resultado y luego pide
el cambio específico que quieres.

```text
Make the opening more direct, keep the evidence, and move the recommendation
above the background section.

Puedes agregar una fuente faltante, corregir el rumbo, pedir otra opción o
cambiar el nivel de detalle sin empezar de nuevo.

### Orientar y poner en cola

Cuando Codex ya esté trabajando, puedes enviar otro mensaje sin esperar a que
termine la ejecución actual:

- **Orientar** agrega el mensaje a la ejecución actual. Úsalo para cambiar el rumbo, agregar
  un detalle faltante o compartir información nueva.
- **Poner en cola** guarda el mensaje para la siguiente ejecución. Úsalo para un seguimiento que deba
  esperar hasta que termine el trabajo actual.

En la aplicación de escritorio de ChatGPT, elige la opción predeterminada en
[**Configuración \> General \> Comportamiento de seguimiento**](/es-419/codex/app/settings#general).
Los mensajes en cola aparecen encima del editor, donde puedes editarlos, reordenarlos, enviarlos o
eliminarlos. Esta configuración también muestra el atajo para usar el otro comportamiento
en un solo mensaje sin cambiar tu opción predeterminada.

En Codex CLI, presiona <kbd>Enter</kbd> mientras Codex trabaja para orientar el turno
actual, o presiona <kbd>Tab</kbd> para poner el mensaje en cola para el siguiente turno. Consulta los
[atajos interactivos](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)
para obtener más información.

## Combina todos los elementos

Para una actualización de proyecto basada en fuentes conectadas, un prompt completo podría ser
así:

```text
Prepare a one-page project status update for Monday's leadership meeting. Use
the latest project plan in Drive and relevant decisions and updates from the
project's Slack channel.

Lead with the decisions leadership needs to make and the next steps. Summarize
progress, risks, owners, and due dates. Keep approved dates and budget figures
unchanged. Flag any conflicting or missing information, and don't send or
publish anything.

Before you finish, check that every next step has an owner and due date.

Este prompt abarca el **Objetivo**, el **Contexto**, el **Resultado** y los **Límites**, y luego
solicita una revisión final sin detallar cada paso.

## Usa el dictado por voz

En la aplicación de escritorio de ChatGPT, presiona <kbd>Ctrl+Shift+D</kbd> mientras el editor esté
visible y luego comienza a hablar. ChatGPT transcribe lo que dices en el editor
para que puedas revisarlo y editarlo antes de enviar el prompt.

  
    
  

<a id="threads"></a>
<a id="chats"></a>

## Ejemplos de diseño de prompts para Chat

Usa Chat para preguntas, ideas, borradores y decisiones cotidianas. Empieza por el
resultado que quieres y agrega detalles solo si cambian la respuesta.

### Comprender un tema

```text
Explain how compound interest works for someone who has never invested.
Use one concrete example and define any financial terms you introduce.

### Redactar y perfeccionar textos

```text
Draft a friendly email declining this invitation because I will be traveling.
Keep it under 120 words and leave the door open for a future event.

### Comparar opciones

```text
Compare these two phone plans for one person who travels internationally twice
a year. Show the important differences in a table, then recommend one and explain
the tradeoff.

### Elaborar un plan práctico

```text
Plan five weekday dinners that take less than 30 minutes. Avoid peanuts, reuse
ingredients across meals, and finish with one consolidated shopping list.

<a id="prompting-for-work"></a>
<a id="prompting-in-work-mode"></a>

## Diseño de prompts para ChatGPT Work

Usa Chat para preguntas rápidas, reescrituras breves, lluvia de ideas y borradores
sencillos. Usa ChatGPT Work para tareas que recurren a distintas fuentes o herramientas, implican una
secuencia de pasos, requieren hacer cambios o generan un entregable de mayor alcance.

En ChatGPT Work, describe el resultado que necesitas, proporciona el material de referencia e indica
el público y cómo revisarás el trabajo. Pídele a ChatGPT que elabore un plan,
recopile la información necesaria, cree archivos y los revise antes de terminar.

<a id="use-work-efficiently"></a>
<a id="use-work-mode-efficiently"></a>

### Usar ChatGPT Work de manera eficiente

ChatGPT Work es útil para tareas que requieren mucho tiempo o son recurrentes, o para crear archivos finales que
puedas reutilizar. Una tarea que consume más créditos puede seguir valiendo la pena si ahorra
tiempo, mejora la calidad o te ayuda a tomar una decisión importante.

Comienza con un solo resultado que puedas revisar:

- Incluye solo fuentes relevantes y limita el rango de fechas cuando corresponda.
- Define el público, el formato de salida y la extensión deseada.
- Separa el trabajo obligatorio de las mejoras o los retoques opcionales.
- Pide un plan cuando el enfoque sea importante. Exige que ChatGPT solicite tu aprobación
antes de enviar, publicar o modificar información de la que dependen otras personas.
- Reduce el alcance de la tarea o detenla si empieza a realizar trabajo que ya no necesitas.

Revisa el primer resultado, perfecciona las instrucciones y reutiliza el flujo de trabajo cuando
funcione.

### Convertir material de referencia en archivos finales

```text
Use the attached quarterly reports to create a leadership brief and a six-slide
presentation.

The audience is the executive team. Lead with the three decisions they need to
make, distinguish reported facts from your analysis, cite each number to its
source file, and check that the brief and slides agree before you finish.

### Investigar para tomar una decisión

```text
Research three customer-support platforms for a 50-person company. Compare
pricing, security, integrations, and migration effort using current sources.
Deliver a recommendation memo with links, assumptions, and the questions we
should answer before signing a contract.

### Coordinar un lanzamiento

```text
Create a launch plan for the attached product brief. Include the timeline,
owners, dependencies, risks, announcement draft, customer FAQ, and a checklist
for launch day. Flag any missing decisions before producing the final files.

Para las tareas recurrentes, primero perfecciona el prompt en un chat normal. Cuando el resultado sea
confiable, [programa una tarea dentro de ese chat](/es-419/codex/automations#schedule-a-task-inside-a-chat).
En cambio, crea una tarea programada independiente cuando cada ejecución programada deba iniciar
un chat nuevo.

<a id="use-editor-context"></a>

## Diseño de prompts para Codex

Usa Codex cuando quieras que ChatGPT trabaje con código, una base de código o herramientas de desarrollo.
Un prompt útil para Codex indica el comportamiento que buscas y señala el código relevante o
los pasos para reproducir el problema, conserva las restricciones importantes y explica cómo verificar el
cambio.

<a id="goal-mode"></a>

Para una tarea de varios pasos, ingresa `/plan` en el editor de la App si quieres que Codex
investigue y proponga un enfoque antes de editar. Cuando el [modo Objetivo](/es-419/codex/long-running-work)
esté disponible, usa `/goal` después del plan para establecer un objetivo persistente. Consulta los [comandos slash
de la App](/codex/reference/slash-commands)
para ver la lista actual de comandos.

### Cómo leer estos ejemplos

Cada flujo de trabajo incluye:

- **Cuándo usarlo** y qué interfaz de Codex es la más adecuada (IDE, CLI o nube).
- **Pasos** con ejemplos de prompts del usuario.
- **Notas sobre el contexto**: qué ve Codex automáticamente y qué debes adjuntar.
- **Verificación**: cómo comprobar el resultado.

> **Nota:** la extensión para IDE incluye automáticamente los archivos abiertos como contexto. En la CLI, menciona las rutas de forma explícita o adjunta archivos mediante `/mention` y el autocompletado de rutas con `@`.

Codex ejecuta comandos locales dentro de un [sandbox](/es-419/codex/sandboxing)
que limita el acceso a archivos y a la red. Si una tarea necesita cruzar ese límite,
Codex sigue tu política de aprobación antes de continuar.

### Explicar una base de código

Usa esto durante tu incorporación, cuando heredes un servicio o cuando intentes comprender un protocolo, un modelo de datos o un flujo de solicitudes.

#### Flujo de trabajo de la extensión para IDE (la opción más rápida para explorar localmente)

1. Abre los archivos más relevantes.
2. Selecciona el código que te interesa (opcional, pero recomendado).
3. Escribe un prompt para Codex:

   ```text
   Explain how the request flows through the selected code.

   Include:
   - a short summary of the responsibilities of each module involved
   - what data is validated and where
   - one or two "gotchas" to watch for when changing this

Verificación:

- Pide un diagrama o una lista de verificación que puedas comprobar:

```text
Summarize the request flow as a numbered list of steps. Then list the files involved.

#### Flujo de trabajo de la CLI (útil si quieres una transcripción y comandos de shell)

1. Inicia una sesión interactiva:

   ```bash
   codex

2. Adjunta los archivos (opcional) y escribe el prompt:

   ```text
   I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.

Notas sobre el contexto:

- Puedes usar `@` en el editor para insertar rutas de archivos del espacio de trabajo, o `/mention` para adjuntar un archivo específico.

### Corregir un error

Usa esto cuando observes un comportamiento incorrecto que puedas reproducir localmente.

#### Flujo de trabajo de la CLI (ciclo rápido de reproducción y verificación)

1. Inicia Codex en la raíz del repositorio:

   ```bash
   codex

2. Proporciona a Codex los pasos para reproducir el problema y los archivos donde sospechas que está el error:

   ```text
   Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.

   Repro:
   1) Start the app: npm run dev
   2) Go to /settings
   3) Toggle "Enable alerts"
   4) Click Save
   5) Refresh the page: the toggle resets

   Constraints:
   - Do not change the API shape.
   - Keep the fix minimal and add a regression test if feasible.

   Start by reproducing the bug locally, then propose a patch and run checks.

Notas sobre el contexto:

- Tú proporcionas: los pasos para reproducir el problema y las restricciones (son más importantes que una descripción general).
- Codex proporciona: la salida de los comandos, los sitios de llamada detectados y las trazas de pila que genere.

Verificación:

- Codex debe volver a ejecutar los pasos para reproducir el problema después de corregir el error.
- Si tienes un flujo de verificación estándar, pídele que lo ejecute:

```text
After the fix, run lint + the smallest relevant test suite. Report the commands and results.

#### Flujo de trabajo de la extensión para IDE

1. Abre el archivo donde crees que está el error y el archivo que contiene la llamada más cercana.
2. Escribe un prompt para Codex:

   ```text
   Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.

### Escribir una prueba

Usa esto cuando quieras definir exactamente qué se debe probar.

#### Flujo de trabajo de la extensión para IDE (basado en la selección)

1. Abre el archivo que contiene la función.
2. Selecciona las líneas que definen la función. En la paleta de comandos, elige “Add to Codex Thread” para agregarlas al contexto.
3. Escribe un prompt para Codex:

   ```text
   Write a unit test for this function. Follow conventions used in other tests.

Notas sobre el contexto:

- Contenido proporcionado por el comando “Add to Codex Thread”: las líneas seleccionadas (lo que delimita el alcance por “número de línea”), además de los archivos abiertos.

#### Flujo de trabajo de la CLI (ruta e intervalo de líneas indicados en el prompt)

1. Inicia Codex:

   ```bash
   codex

2. Escribe un prompt con el nombre de una función:

   ```text
   Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.

### Crear un prototipo a partir de una captura de pantalla

Usa esto cuando quieras convertir una maqueta de diseño, una captura de pantalla o una referencia de interfaz de usuario en un prototipo funcional.

#### Flujo de trabajo en la CLI (imagen + prompt)

1. Guarda la captura de pantalla localmente (por ejemplo, `./specs/ui.png`).
2. Ejecuta Codex:

   ```bash
   codex

3. Arrastra el archivo de imagen a la terminal para adjuntarlo al prompt.

4. Continúa con las restricciones y la estructura:

   ```text
   Create a new dashboard based on this image.

   Constraints:
   - Use react, vite, and tailwind. Write the code in typescript.
   - Match spacing, typography, and layout as closely as possible.

   Outputs:
   - A new route/page that renders the UI
   - Any small components needed
   - README.md with instructions to run it locally

Notas de contexto:

- La imagen proporciona los requisitos visuales, pero aun así debes especificar las restricciones de implementación (framework, enrutamiento y estilo de los componentes).
- Describe por escrito los comportamientos que la imagen no muestra, como los estados al pasar el cursor, las reglas de validación o las interacciones con el teclado.

Verificación:

- Pídele a Codex que ejecute el servidor de desarrollo (si está permitido) y te indique exactamente dónde verlo:

```text
Start the dev server and tell me the local URL/route to view the prototype.

#### Flujo de trabajo de la extensión para IDE (imagen + archivos existentes)

1. Adjunta la imagen al chat de Codex (arrástrala y suéltala o pégala).
2. Escribe un prompt para Codex:

   ```text
   Create a new settings page. Use the attached screenshot as the target UI.
   Follow design and visual patterns from other files in this project.

### Iterar en la interfaz de usuario con actualizaciones en tiempo real

Usa esto cuando quieras un ciclo ágil de “diseñar → ajustar → recargar → ajustar” mientras Codex edita el código.

#### Flujo de trabajo en la CLI (ejecutar Vite y luego iterar con prompts breves)

1. Inicia Codex:

   ```bash
   codex

2. Inicia el servidor de desarrollo en otra ventana de la terminal:

   ```bash
   npm run dev

3. Pídele a Codex que haga cambios:

   ```text
   Propose 2-3 styling improvements for the landing page.

4. Elige un enfoque e itera con prompts breves y específicos:

   ```text
   Go with option 2.

   Change only the header:
   - make the typography more editorial
   - increase whitespace
   - ensure it still looks good on mobile

5. Repite el proceso con solicitudes concretas:

   ```text
   Next iteration: reduce visual noise.
   Keep the layout, but simplify colors and remove any redundant borders.

Verificación:

- Revisa los cambios en el navegador a medida que Codex actualiza el código.
- Haz commit de los cambios que te gusten y revierte los que no.
- Si reviertes o modificas un cambio, avísale a Codex para que no lo sobrescriba cuando trabaje en el siguiente prompt.

### Delegar la refactorización a la nube

Usa esto cuando quieras definir un enfoque a partir del contexto local y luego delegar la implementación extensa a un chat en la nube que pueda ejecutarse en paralelo.

#### Planificación local (IDE)

1. Asegúrate de haber hecho commit de tu trabajo actual o, al menos, de haberlo guardado en un stash para poder comparar los cambios con claridad.
2. Pídele a Codex que genere un plan de refactorización. Si tienes disponible la habilidad `$plan`, invócala explícitamente:

   ```text
   $plan

   We need to refactor the auth subsystem to:
   - split responsibilities (token parsing vs session loading vs permissions)
   - reduce circular imports
   - improve testability

   Constraints:
   - No user-visible behavior changes
   - Keep public APIs stable
   - Include a step-by-step migration plan

3. Revisa el plan y acuerda los cambios:

   ```text
   Revise the plan to:
   - specify exactly which files move in each milestone
   - include a rollback strategy

Notas de contexto:

- La planificación funciona mejor cuando Codex puede analizar localmente el código actual (puntos de entrada, límites entre módulos e indicios sobre el grafo de dependencias).

#### Delegación a la nube (IDE → Nube)

1. Si aún no lo hiciste, configura un [entorno en la nube de Codex](/es-419/codex/environments/cloud-environment).
2. Haz clic en el ícono de la nube debajo del editor de prompts y selecciona tu entorno en la nube.
3. Cuando ingresas el siguiente prompt, Codex crea un nuevo chat en la nube y transfiere el contexto del chat existente (incluidos el plan y cualquier cambio local en el código fuente).

   ```text
   Implement Milestone 1 from the plan.

4. Revisa el diff en la nube e itera si es necesario.

5. Crea un PR directamente desde la nube o trae los cambios a tu entorno local para probarlos y terminar el trabajo.

6. Itera sobre otros hitos del plan.

Las tareas delegadas a la nube se ejecutan en entornos aislados. El acceso a Internet está
desactivado durante la fase del agente, a menos que lo habilites para el entorno. Obtén más información
sobre el [acceso a Internet en la nube](/es-419/codex/cloud/internet-access).

### Realizar una revisión local del código

Usa esto cuando quieras una segunda opinión antes de hacer commit o crear un PR.

#### Flujo de trabajo en la CLI (revisar tu árbol de trabajo)

1. Inicia Codex:

   ```bash
   codex

2. Ejecuta el comando de revisión:

   ```text
   /review

3. Opcional: proporciona instrucciones personalizadas para enfocar la revisión:

   ```text
   /review Focus on edge cases and security issues

Verificación:

- Aplica correcciones a partir de los comentarios de la revisión y luego vuelve a ejecutar `/review` para confirmar que resolviste los problemas.

### Revisar un Pull Request de GitHub

Usa esto cuando quieras recibir comentarios de revisión sin traer la rama a tu entorno local.

Antes de usar esta función, habilita la **Revisión de código** de Codex en tu repositorio. Consulta [Revisión de código](/es-419/codex/third-party/github).

#### Flujo de trabajo en GitHub (basado en comentarios)

1. Abre el Pull Request en GitHub.
2. Deja un comentario en el que menciones a Codex y especifiques las áreas en las que debe enfocarse:

   ```text
   @codex review

3. Opcional: proporciona instrucciones más explícitas.

   ```text
   @codex review for security vulnerabilities and security concerns

### Actualizar la documentación

Usa esto cuando necesites hacer un cambio preciso y claro en la documentación.

#### Flujo de trabajo en el IDE o la CLI (cambios locales + validación local)

1. Identifica los archivos de documentación que debes modificar y ábrelos (IDE), o menciónalos con `@` (IDE o CLI).
2. Envía a Codex un prompt con el alcance y los requisitos de validación:

   ```text
   Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.

3. Después de que Codex prepare un borrador de los cambios, revisa la documentación e itera según sea necesario.

Verificación:

- Lee la página renderizada.
