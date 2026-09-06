<!-- source: https://learn.chatgpt.com/es-419/docs/automations -->

Programa tareas recurrentes para que se ejecuten en segundo plano. En ChatGPT en la web y en dispositivos móviles,
los planes elegibles también permiten ejecutar tareas a partir de eventos compatibles de aplicaciones. Revisa las tareas activas,
pausadas y completadas, así como las ejecuciones recientes, en **Programadas**. Puedes combinar
las tareas programadas con [habilidades](/es-419/codex/build-skills) para realizar trabajos más complejos.

En la aplicación de escritorio de ChatGPT, las tareas programadas pueden trabajar con proyectos locales y
ejecutarse en el directorio del proyecto o en un worktree aislado. Mantén la computadora encendida y
la aplicación en ejecución cuando una tarea programada necesite archivos locales.

Cuando las tareas programadas estén habilitadas para tu espacio de trabajo, créalas desde Chat o
ChatGPT Work en la web y administra sus ejecuciones desde **Programadas**. Las tareas web
pueden usar el contexto cargado y las herramientas conectadas, pero no pueden trabajar directamente en
una carpeta de tu computadora.

Codex CLI no incluye la interfaz de administración de Programadas. Usa ChatGPT en la web
o la aplicación de escritorio para crear y administrar tareas programadas. La CLI puede ayudarte
a preparar y probar primero un prompt, una habilidad o un script.

La extensión para IDE no incluye la interfaz de administración de Programadas. Usa
ChatGPT en la web o la aplicación de escritorio para crear y administrar tareas programadas. La extensión para IDE
puede ayudarte a preparar y probar un prompt, una habilidad o un cambio en el espacio de trabajo
como primer paso.

<a id="managing-tasks"></a>
<a id="ask-codex-to-create-or-update-automations"></a>
<a id="ask-chatgpt-to-create-or-update-scheduled-tasks"></a>
<a id="thread-automations"></a>
<a id="scheduled-tasks-in-threads"></a>
<a id="scheduled-tasks-in-chats"></a>
<a id="schedule-work-from-a-task"></a>
<a id="schedule-a-task-inside-a-chat"></a>
<a id="test-automations"></a>
<a id="test-scheduled-tasks"></a>
<a id="worktree-cleanup-for-automations"></a>
<a id="worktree-cleanup-for-scheduled-tasks"></a>
<a id="permissions-and-security-model"></a>
<a id="examples"></a>
<a id="automatically-create-new-skills"></a>
<a id="stay-up-to-date-with-your-project"></a>
<a id="combining-automations-with-skills-to-fix-your-own-bugs"></a>
<a id="combining-scheduled-tasks-with-skills-to-fix-your-own-bugs"></a>

## Administrar tareas programadas en la web

Abre **Programadas** para revisar el estado de las tareas y las ejecuciones recientes. Usa una tarea programada independiente
cuando cada ejecución deba comenzar a partir del prompt guardado. Usa una tarea programada en un
chat cuando quieras que ChatGPT vuelva al mismo chat con su contexto
existente.

Las tareas programadas en la web pueden usar archivos cargados, herramientas conectadas, habilidades y
complementos disponibles para ese chat. No mantienen disponible una carpeta local ni
un worktree entre ejecuciones. Incluye las instrucciones que deban conservarse en el prompt de la tarea
o en una habilidad adjunta, y guarda el material de origen necesario en una ubicación accesible,
como un proyecto, un archivo cargado o un servicio conectado.

Antes de programar una tarea, prueba su prompt en un chat normal en la web.
Revisa las primeras ejecuciones y luego ajusta el prompt, las herramientas o la frecuencia si los
resultados son demasiado generales o necesitan contexto adicional.

## Activar tareas a partir de eventos de aplicaciones

En los planes elegibles, las tareas programadas pueden ejecutarse cuando ocurre un evento compatible de Gmail, Slack o
GitHub. Las tareas activadas por eventos están disponibles en ChatGPT en la web
y en dispositivos móviles. No están disponibles en la aplicación de escritorio de ChatGPT, Codex CLI ni en la
extensión para IDE.

Pídele a ChatGPT que cree la tarea y luego describe el evento que debe detectar y qué
hacer cuando ocurra. El disparador determina cuándo se ejecuta la tarea; el prompt
guardado determina qué hace cada ejecución. Una tarea puede usar varios disparadores de eventos,
pero no puede combinarlos con una programación basada en el tiempo.

Los disparadores de eventos compatibles incluyen:

- **Gmail:** nuevos mensajes entrantes, con filtros opcionales por remitente o asunto.
- **Slack:** mensajes nuevos en los canales seleccionados. Puedes filtrarlos por autor
  y elegir si se incluyen respuestas en hilos. No se admiten reacciones, ediciones, eliminaciones ni
  mensajes directos.
- **GitHub:** actividad de los Pull Requests en un repositorio. Filtra por Pull Request,
  autor, título o etiqueta, y elige si la tarea debe activarse con revisiones, comentarios, actualizaciones de commits
  o solo con fusiones.

Conecta y autoriza la aplicación antes de crear la tarea. Para Slack, agrega
`@ChatGPT` a cada canal que la tarea monitoree. Para GitHub, la aplicación conectada
debe tener acceso al repositorio.

Cuando llegan varios eventos coincidentes en poco tiempo, ChatGPT puede combinarlos
en una sola ejecución. Abre **Programadas** para revisar los eventos pendientes o elige **Ejecutar ahora**
para procesarlos.

La disponibilidad depende de tu plan y de la configuración del espacio de trabajo. En los
espacios de trabajo administrados, los administradores pueden controlar el acceso con el permiso **Permitir tareas programadas
activadas por eventos** .

Por ejemplo, programa una tarea para evaluar errores de telemetría y enviar correcciones,
o para crear informes sobre cambios recientes en el código base. Para trabajos continuos que
deban seguir usando el mismo contexto, [programa una tarea dentro de un chat existente](#schedule-a-task-inside-a-chat).

Para las tareas programadas asociadas a un proyecto, mantén la computadora encendida y la aplicación de escritorio de ChatGPT
en ejecución. El proyecto seleccionado debe seguir disponible en el disco cuando
llegue la hora programada de ejecutar la tarea.

En los repositorios Git, puedes elegir si una tarea programada se ejecuta en tu proyecto
local o en un [worktree](/es-419/codex/environments/git-worktrees) nuevo. En ambas opciones, la tarea se ejecuta en
segundo plano. Los worktrees mantienen los cambios de las tareas programadas separados del trabajo local
sin terminar, mientras que la ejecución en tu proyecto local puede modificar archivos en los que aún
estás trabajando. En proyectos sin control de versiones, las tareas programadas se ejecutan directamente en el
directorio del proyecto.

También puedes mantener la configuración predeterminada del modelo y del esfuerzo de razonamiento, o
elegirlos de forma explícita si quieres tener más control sobre cómo se ejecuta la tarea programada.

Si una tarea programada usa `gpt-5.4` o `gpt-5.4-mini` con el inicio de sesión de ChatGPT,
actualízala antes de que esos modelos se retiren el 31 de agosto de 2026. Sustituye `gpt-5.4` por
`gpt-5.6-terra` y `gpt-5.4-mini` por `gpt-5.6-luna`.

  

Las tareas programadas se ejecutan sin supervisión con la configuración predeterminada de tu sandbox. Comienza con el
nivel de acceso más limitado que permita completar la tarea y concede acceso a la red o un acceso más amplio a los archivos
solo cuando sea necesario. [Comprender el entorno aislado](/es-419/codex/sandboxing).

## Administrar tareas programadas

Encuentra todas las tareas programadas y sus ejecuciones en **Programadas** , en la barra lateral de la aplicación
de escritorio de ChatGPT.

La vista **Programadas** funciona como tu bandeja de entrada. Allí aparecen las ejecuciones de tareas programadas con hallazgos,
y un indicador de elementos no leídos señala cuándo una ejecución requiere tu atención.

  

Las tareas programadas independientes inician un chat nuevo en cada ejecución programada y muestran los
resultados en **Programadas**. Úsalas cuando cada ejecución deba ser independiente o cuando una
tarea programada deba ejecutarse en uno o más proyectos. Si necesitas una
frecuencia personalizada, usa los controles de programación personalizada. Para una programación avanzada, edita su
regla de recurrencia de RFC 5545 (RRULE), por ejemplo,
`RRULE:FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0`.

En los repositorios Git, cada tarea programada puede ejecutarse en tu proyecto local o
en un [worktree](/es-419/codex/environments/git-worktrees) dedicado en segundo plano. Usa
worktrees cuando quieras aislar los cambios de las tareas programadas del trabajo local
sin terminar. Usa el modo local cuando quieras que la tarea programada trabaje directamente en tu
copia de trabajo principal; ten en cuenta que puede modificar archivos que estés editando.
En proyectos sin control de versiones, las tareas programadas se ejecutan directamente en el directorio
del proyecto. Puedes ejecutar la misma tarea programada en más de un proyecto.

Las tareas programadas creadas con ChatGPT Work en la web, o con ChatGPT Work o
Codex en la aplicación de escritorio, pueden usar complementos. Las tareas programadas también pueden usar habilidades.
Para facilitar el mantenimiento de las tareas programadas y compartirlas entre equipos, usa
[habilidades](/es-419/codex/build-skills) para definir la acción y proporcionar herramientas y contexto.
Selecciona o invoca una habilidad específica en el prompt de la tarea cuando el flujo de trabajo no deba
depender de la selección automática de herramientas.

## Pedirle a ChatGPT que cree o actualice tareas programadas

Puedes crear y actualizar tareas programadas desde un chat de ChatGPT o Codex.
Describe el trabajo, cuándo debe ejecutarse y si cada ejecución debe volver al
chat actual o iniciar uno nuevo. ChatGPT puede redactar el prompt, elegir el
destino adecuado y actualizar la tarea cuando su alcance o frecuencia
cambien.

Por ejemplo, pídele a ChatGPT que programe un seguimiento desde el chat actual mientras finaliza un
despliegue, o que cree una tarea programada independiente que revise
un proyecto de forma recurrente.

Las habilidades también pueden crear o actualizar tareas programadas. Por ejemplo, una habilidad para
supervisar un Pull Request podría configurar una tarea programada que consulte el
estado del PR con el complemento de GitHub y aplique correcciones en respuesta a los nuevos comentarios de revisión.

## Programar una tarea dentro de un chat

Programa una tarea dentro de un chat existente cuando quieras que ChatGPT vuelva a ese chat
de forma programada. La tarea programada usa el contexto existente del chat en lugar de
comenzar con un prompt nuevo cada vez.

Las tareas programadas en un chat pueden usar intervalos de minutos para ciclos de seguimiento
activo, o programaciones diarias y semanales cuando necesites una comprobación a una hora
específica.

Programa una tarea dentro de un chat para:

- comprobar el estado de una operación de larga duración hasta que finalice
- consultar una fuente conectada con una frecuencia fija cuando necesites una instantánea
periódica en lugar de una respuesta a un evento compatible de una aplicación
- recordarle a ChatGPT que continúe un ciclo de revisión con una frecuencia fija
- ejecutar un flujo de trabajo basado en habilidades que use complementos, como consultar el estado de un PR
y atender nuevos comentarios
- continuar un chat de investigación o de clasificación y priorización en curso sin perder su contexto

Usa una tarea programada independiente cuando cada ejecución deba ser independiente o cuando
los hallazgos deban aparecer como ejecuciones separadas en **Programadas**.

Cuando programes una tarea dentro de un chat, redacta un prompt que pueda reutilizarse. Debe describir
qué debe hacer ChatGPT en cada ejecución programada, cómo decidir si hay
algo importante que informar y cuándo detenerse o pedirte información.

## Probar las tareas programadas

Antes de programar una tarea, prueba manualmente el prompt en un chat normal.
Esto te ayuda a confirmar lo siguiente:

- El prompt es claro y su alcance está definido correctamente.
- El modelo, el esfuerzo de razonamiento y las herramientas seleccionados o predeterminados se comportan según lo esperado.
- El resultado se puede revisar.

Cuando empieces a programar ejecuciones, revisa los primeros resultados y ajusta el
prompt o la frecuencia según sea necesario.

En la aplicación de escritorio de ChatGPT, puedes activar explícitamente una habilidad en el prompt de una
tarea programada mediante `$skill-name`.

## Limpieza de worktrees de tareas programadas

Si eliges worktrees para repositorios Git, programar ejecuciones frecuentes puede crear
muchos worktrees con el tiempo. Archiva las ejecuciones programadas que ya no necesites y evita
fijar ejecuciones, a menos que quieras conservar sus worktrees.

## Permisos y modelo de seguridad

Las tareas programadas se ejecutan sin supervisión y usan la configuración predeterminada de tu sandbox.

Para ver una explicación sencilla de estos límites, consulta la
[descripción general del entorno aislado](/es-419/codex/sandboxing). Para conocer las reglas del sistema de archivos y de la red,
consulta [Permisos](/es-419/codex/permissions).

- Si tu modo de sandbox es **de solo lectura**, las llamadas a herramientas fallan si requieren
  modificar archivos, acceder a la red o trabajar con apps en tu computadora.
  Considera cambiar la configuración del sandbox a escritura en el espacio de trabajo.
- Si tu modo de sandbox es **workspace-write**, las llamadas a herramientas fallan si requieren
  modificar archivos fuera del espacio de trabajo, acceder a la red o trabajar con apps
  en tu computadora. Puedes autorizar comandos específicos para que se ejecuten fuera del
  sandbox mediante [reglas](/es-419/codex/agent-configuration/rules).
- Si tu modo de sandbox es **acceso completo**, las tareas programadas en segundo plano conllevan un
  riesgo elevado, ya que ChatGPT puede modificar archivos, ejecutar comandos y acceder a la red
  sin preguntar. Considera cambiar la configuración del sandbox a escritura en el espacio de trabajo y
  usar [reglas](/es-419/codex/agent-configuration/rules) para definir qué comandos específicos puede ejecutar el agente
  con acceso completo.

Si estás en un entorno administrado, los administradores pueden restringir estos comportamientos mediante
requisitos impuestos por los administradores. Por ejemplo, pueden prohibir `approval_policy =
"never"` o limitar los modos de sandbox permitidos. Consulta
[Requisitos impuestos por los administradores (`requirements.toml`)](/es-419/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

Las tareas programadas usan `approval_policy = "never"` cuando la política de tu organización
lo permite. Si los requisitos de los administradores prohíben `approval_policy = "never"`,
las tareas programadas recurren al comportamiento de aprobación del modo de permisos
que seleccionaste.

## Ejemplos

### Crea nuevas habilidades automáticamente

```markdown
Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.

If there’s anything we’ve been doing often and struggle with that we should save as a skill to speed up future work, let’s do it.

Definitely don't feel like you need to update any- only if there's a good reason!

Let me know if you make any.

### Mantente al día con tu proyecto

```markdown
Look at the latest remote origin/master or origin/main . Then produce an exec briefing for the last 24 hours of commits that touch 

Formatting + structure:

- Use rich Markdown (H1 workstream sections, italics for the subtitle, horizontal rules as needed).
- Preamble can read something like “Here’s the last 24h brief for <directory>:”
- Subtitle should read: “Narrative walkthrough with owners; grouped by workstream.”
- Group by workstream rather than listing each commit. Workstream titles should be H1.
- Write a short narrative per workstream that explains the changes in plain language.
- Use bullet points and bolding when it makes things more readable
- Feel free to make bullets per person, but bold their name

Content requirements:

- Include PR links inline (e.g., [#123](...)) without a “PRs:” label.
- Do NOT include commit hashes or a “Key commits” section.
- It’s fine if multiple PRs appear under one workstream, but avoid per‑commit bullet lists.

Scope rules:

- Only include changes within the current cwd (or main checkout equivalent)
- Only include the last 24h of commits.
- Use `gh` to fetch PR titles and descriptions if it helps.
  Also feel free to pull PR reviews and comments

### Combinar tareas programadas con habilidades para corregir tus propios errores

Crea una habilidad nueva llamada `$recent-code-bugfix` que intente corregir un error introducido por tus propios commits y [guárdala en tus habilidades personales](/es-419/codex/build-skills#where-to-save-skills).

```markdown
---
name: recent-code-bugfix
description: Find and fix a bug introduced by the current author within the last week in the current working directory. Use when a user wants a proactive bugfix from their recent changes, when the prompt is empty, or when asked to triage/fix issues caused by their recent commits. Root cause must map directly to the author’s own changes.
---

# Recent Code Bugfix

## Overview

Find a bug introduced by the current author in the last week, implement a fix, and verify it when possible. Operate in the current working directory, assume the code is local, and ensure the root cause is tied directly to the author’s own edits.

## Workflow

### 1) Establish the recent-change scope

Use Git to identify the author and changed files from the last week.

- Determine the author from `git config user.name`/`user.email`. If unavailable, use the current user’s name from the environment or ask once.
- Use `git log --since=1.week --author=<author>` to list recent commits and files. Focus on files touched by those commits.
- If the user’s prompt is empty, proceed directly with this default scope.

### 2) Find a concrete failure tied to recent changes

Prioritize defects that are directly attributable to the author’s edits.

- Look for recent failures (tests, lint, runtime errors) if logs or CI outputs are available locally.
- If no failures are provided, run the smallest relevant verification (single test, file-level lint, or targeted repro) that touches the edited files.
- Confirm the root cause is directly connected to the author’s changes, not unrelated legacy issues. If only unrelated failures are found, stop and report that no qualifying bug was detected.

### 3) Implement the fix

Make a minimal fix that aligns with project conventions.

- Update only the files needed to resolve the issue.
- Avoid adding extra defensive checks or unrelated refactors.
- Keep changes consistent with local style and tests.

### 4) Verify

Attempt verification when possible.

- Prefer the smallest validation step (targeted test, focused lint, or direct repro command).
- If verification cannot be run, state what would be run and why it wasn’t executed.

### 5) Report

Summarize the root cause, the fix, and the verification performed. Make it explicit how the root cause ties to the author’s recent changes.

Después, crea una tarea programada nueva:

```markdown
Check my commits from the last 24h and submit a $recent-code-bugfix.
