<!-- source: https://learn.chatgpt.com/es-419/docs/code-review -->

Usa ChatGPT o Codex para inspeccionar los cambios en el código antes de incluirlos en un commit o enviarlos.

## Iniciar una revisión

En ChatGPT Work, sube el código que quieres revisar o ponlo a disposición mediante
un [complemento](/es-419/codex/plugins) de código fuente instalado. En tu prompt, identifica
el Pull Request, la rama, el commit, los archivos y los criterios de revisión.

### Revisar en la App

Abre el panel de revisión para comprender qué cambió, dar comentarios sobre líneas específicas
y decidir qué cambios preparar, revertir, incluir en un commit o enviar.

Para pedirle a Codex que revise los cambios, escribe `/review` en el Editor. Elige
**Revisar en comparación con una rama base** o **Revisar cambios sin commit**. Codex informa
hallazgos priorizados sin modificar tu árbol de trabajo.

El panel de revisión requiere un proyecto dentro de un repositorio de Git. Si tu proyecto
aún no es un repositorio de Git, la App te pide que crees uno.

Escribe `/review` para abrir las opciones predefinidas de revisión de la CLI. Codex inicia un revisor dedicado
que lee el diff seleccionado e informa hallazgos priorizados que puedes atender
sin modificar tu árbol de trabajo.

Escribe `/review` en el Editor de la Extensión para IDE. Elige **Revisar en comparación con una rama
base** o **Revisar cambios sin commit**. Codex informa hallazgos priorizados
sin modificar tu árbol de trabajo.

El comando `/review` solo aparece cuando el proyecto abierto se encuentra dentro de un repositorio
de Git.

## Elegir el alcance de la revisión

Indica en tu prompt el Pull Request, la rama, el commit o los archivos que quieres inspeccionar. Para
revisar archivos locales que no estén disponibles mediante un complemento de código fuente instalado,
súbelos al chat.

### Qué cambios muestra

El panel de revisión refleja el estado de tu repositorio de Git, no solo lo que editó Codex.
Incluye los cambios hechos por Codex, los que hiciste tú y cualquier
otro cambio sin commit en el repositorio.

De forma predeterminada, el panel de revisión muestra los cambios **Sin preparar** . Usa **Preparados** para el
índice de Git, **Commit** para un commit seleccionado, **Rama** para el diff con respecto a tu
rama base o **Último turno** para el turno más reciente del asistente.

### Revisar varios repositorios

Cuando un [proyecto local incluye varias carpetas](/es-419/codex/projects#use-local-projects-for-folders-and-codebases)
asociadas a distintos repositorios de Git, el panel de revisión puede mostrar los cambios de cada
repositorio. Abre el selector de repositorios en el encabezado de la revisión para inspeccionar
otro repositorio y ver las líneas agregadas o eliminadas sin salir del
panel de revisión actual.

Elige **Último turno** para ver los cambios más recientes del asistente en todos los repositorios
adjuntos. Para esta vista, el selector de repositorios muestra **Todos los repositorios** . Los demás
alcances de revisión, como **Sin preparar**, **Preparados** y **Rama**, se aplican al
repositorio que selecciones.

Elige uno de estos alcances de `/review`:

- **Revisar en comparación con una rama base** determina la base de fusión y revisa el diff de tu rama.
- **Revisar cambios sin commit** incluye archivos preparados, sin preparar y sin seguimiento.
- **Revisar un commit** examina el conjunto exacto de cambios de un commit seleccionado.
- **Instrucciones de revisión personalizadas** centran la revisión en los criterios que proporciones.

Elige uno de estos alcances de `/review`:

- **Revisar en comparación con una rama base** compara tu rama actual con la rama que selecciones.
- **Revisar cambios sin commit** revisa los cambios de tu árbol de trabajo.

## Trabajar con los resultados de la revisión

Los hallazgos de la revisión aparecen en el chat web. Pide evidencia, solicita una
revisión de seguimiento más acotada o pídele a ChatGPT que prepare versiones revisadas de los archivos.

### Resultados de la revisión de código

Los hallazgos de la revisión aparecen como comentarios en línea en el panel de revisión.

De forma predeterminada, las revisiones se ejecutan en el chat actual. En **Configuración** \> **General** \>
**Revisión de código**, elige **Separada** para iniciar un chat de revisión independiente. Consulta la
[configuración para desarrolladores](/codex/developer-settings?surface=app#app-code-review).

  
    
  

La revisión aparece como un turno en la transcripción. Configura `review_model` en
`config.toml` si quieres que las revisiones usen un modelo distinto del de la
sesión actual.

De forma predeterminada, la revisión se ejecuta en el chat actual. Configura `chatgpt.reviewDelivery` como
`detached` si quieres que `/review` inicie un chat de revisión independiente. Consulta la
[referencia de configuración de la Extensión para IDE](/codex/developer-settings?surface=ide#ide-editor-settings-reference).

Si le pides a ChatGPT que prepare versiones revisadas de los archivos, las herramientas y los permisos del espacio de trabajo
disponibles para el chat siguen aplicándose.

Si le pides a Codex que aplique las correcciones que encuentre, se aplicará tu [configuración habitual de sandbox y
aprobación](/es-419/codex/sandboxing).

## Navegar por el panel de revisión

- Al hacer clic en el nombre de un archivo, normalmente se abre ese archivo en el editor que elegiste. Puedes
  elegir el editor predeterminado en la [configuración para desarrolladores](/codex/developer-settings?surface=app#app-project-and-terminal-behavior).
- Al hacer clic en el fondo del nombre del archivo, se expande o contrae el diff.
- Al hacer clic en una línea mientras mantienes presionada la tecla <kbd>Cmd</kbd>, se abre esa línea en el editor que elegiste.
- Si estás conforme con un cambio, puedes [prepararlo o revertir los cambios](#staging-and-reverting-files) que no quieras.

## Comentarios en línea para dar retroalimentación

Los comentarios en línea te permiten dar retroalimentación directamente sobre líneas específicas del diff.
Esta suele ser la forma más rápida de orientar a Codex hacia la corrección adecuada.

Para dejar un comentario en línea:

1. Abre el panel de revisión.
2. Coloca el cursor sobre la línea que quieras comentar.
3. Selecciona el botón **+** que aparece.
4. Escribe tu comentario y envíalo.
5. Cuando termines de dejar comentarios, envía un mensaje al chat.

Como los comentarios corresponden a líneas específicas, Codex puede responder con más precisión que con
una instrucción general.

Codex considera los comentarios en línea como indicaciones para la revisión. Después de dejar comentarios, envía un
mensaje de seguimiento que exprese claramente tu intención, por ejemplo: “Atiende los
comentarios en línea y mantén el alcance al mínimo”.

## Revisiones de Pull Request

Cuando Codex tiene acceso a tu repositorio en GitHub y el proyecto actual está en
la rama del Pull Request, la aplicación de escritorio de ChatGPT puede ayudarte a gestionar los comentarios
del Pull Request sin salir de la App. La barra lateral muestra el contexto del Pull Request
y los comentarios de los revisores, mientras que el panel de revisión muestra los comentarios
junto al diff para que puedas pedirle a Codex que resuelva los problemas en el mismo chat.

Instala la CLI de GitHub (`gh`) y autentícala con `gh auth login` para que Codex
pueda cargar el contexto del Pull Request, los comentarios de revisión y los archivos modificados. Si `gh` no está
instalado o autenticado, es posible que los detalles del Pull Request no aparezcan en la barra lateral
ni en el panel de revisión.

Usa este flujo cuando quieras mantener todo el ciclo de corrección en un solo lugar:

1. Abre el panel de revisión en la rama del Pull Request.
2. Revisa el contexto del Pull Request, los comentarios y los archivos modificados.
3. Pídele a Codex que atienda los comentarios específicos que elijas.
4. Inspecciona el diff resultante en el panel de revisión.
5. Prepara los cambios, haz un commit y envíalos a la rama del Pull Request cuando estés listo.

Para las revisiones iniciadas desde GitHub, consulta [Usar Codex en GitHub](/es-419/codex/third-party/github).

## Preparar y revertir archivos

El panel de revisión incluye acciones de Git para que puedas ajustar el diff antes de
hacer commit.

Puedes preparar cambios, quitarlos del área de preparación o revertirlos en estos niveles:

- **Diff completo**: usa los botones de acción del encabezado de revisión, como **Preparar todo** o **Revertir todo**.
- **Por archivo**: prepara un archivo individual, quítalo del área de preparación o reviértelo.
- **Por bloque**: prepara un solo bloque de cambios, quítalo del área de preparación o reviértelo.

Usa el área de preparación cuando quieras aceptar parte del trabajo y revierte los cambios cuando quieras
descartarlos.

### Estados de cambios preparados y sin preparar

Git puede representar cambios preparados y sin preparar en un mismo archivo. Cuando eso
sucede, el panel puede mostrar el mismo archivo en ambas vistas. Este es el comportamiento
normal de Git.
