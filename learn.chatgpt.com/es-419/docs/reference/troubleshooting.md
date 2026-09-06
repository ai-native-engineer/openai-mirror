<!-- source: https://learn.chatgpt.com/es-419/docs/reference/troubleshooting -->

## Preguntas frecuentes

### En el panel lateral aparecen archivos que Codex no editó

Si tu proyecto está dentro de un repositorio Git, el panel de revisión muestra automáticamente
los cambios según el estado de Git de tu proyecto, incluidos los cambios que Codex
no realizó.

En el panel de revisión, puedes alternar entre los cambios preparados y los que aún no están
preparados, y comparar tu rama con main.

Si quieres ver solo los cambios del último turno de Codex, cambia el panel de
diferencias a la vista **Último turno**.

[Obtén más información sobre cómo usar el panel de revisión](/es-419/codex/code-review?surface=app).

### Eliminar un proyecto de la barra lateral

Para eliminar un proyecto de la barra lateral, coloca el cursor sobre el nombre del proyecto y haz clic
en los tres puntos y selecciona “Eliminar”. Para restaurarlo, vuelve a agregar el
proyecto con el botón **Agregar proyecto nuevo** junto a **Chats** o con

<kbd>Cmd</kbd>+<kbd>O</kbd>.

<a id="find-archived-threads"></a>
<a id="find-archived-tasks"></a>

### Buscar chats archivados

Los chats archivados se encuentran en [Configuración](codex://settings). Cuando desarchivas
un chat, vuelve a aparecer en su ubicación original de la barra lateral.

<a id="only-some-threads-appear-in-the-sidebar"></a>
<a id="only-some-tasks-appear-in-the-sidebar"></a>

### Solo algunos chats aparecen en la barra lateral

La barra lateral te permite filtrar los chats según el estado de un proyecto. Si te
faltan chats, selecciona el ícono de filtro junto a **Chats** y luego selecciona
**Cronológico**. Si aún no ves el chat, abre
[Configuración](codex://settings) y revisa **Chats archivados**.

### El código no se ejecuta en un Worktree

Los Worktrees se crean en un directorio diferente y, de forma predeterminada, heredan los archivos incluidos en
Git. Según cómo administres las dependencias y las herramientas de tu
proyecto, es posible que debas ejecutar scripts de configuración en tu Worktree mediante un
[entorno local](/es-419/codex/environments/local-environment) o copiar los archivos de configuración ignorados
con [`.worktreeinclude`](/es-419/codex/environments/git-worktrees#copy-ignored-local-files-into-managed-worktrees).
Como alternativa, puedes hacer checkout de los cambios en tu proyecto local habitual. Consulta
la [documentación sobre Worktrees](/es-419/codex/environments/git-worktrees) para obtener más información.

### La App no detecta el entorno local compartido de un compañero de equipo

La configuración del entorno local debe estar dentro de la carpeta `.codex`, en la
raíz de tu proyecto. Si trabajas en un monorepo con más de un
proyecto, asegúrate de abrir el proyecto en el directorio que contiene la carpeta
`.codex`.

### Codex solicita acceso a Apple Music

Según la tarea, es posible que Codex necesite navegar por el sistema de archivos. Algunos
directorios de macOS, como Música, Descargas o Escritorio, requieren
una aprobación adicional del usuario. Si Codex necesita leer tu directorio de inicio,
macOS te pide que apruebes el acceso a esas carpetas.

<a id="automations-create-many-worktrees"></a>

### Las tareas programadas crean muchos Worktrees

Con el tiempo, las tareas programadas que se ejecutan con frecuencia pueden crear muchos Worktrees. Archiva las ejecuciones
programadas que ya no necesites y evita fijarlas, salvo que quieras conservar sus
Worktrees.

### Recuperar un prompt después de seleccionar el destino incorrecto

Si iniciaste por accidente un chat con el destino incorrecto (**Local**, **Worktree** o **Nube**), puedes cancelar la ejecución actual y recuperar el prompt anterior presionando la tecla de flecha hacia arriba en el editor.

### Una función funciona en Codex CLI, pero no en la app de escritorio de ChatGPT

La app de escritorio de ChatGPT y Codex CLI pueden incluir versiones diferentes de Codex, por lo que
las funciones pueden estar disponibles en una interfaz antes que en la otra. Las funciones experimentales también podrían
llegar primero a Codex CLI.

Para consultar la versión de Codex CLI instalada en tu sistema, ejecuta:

```bash
codex --version

Para consultar la versión de Codex incluida en tu app de escritorio de ChatGPT, usa la
ruta que se conserva para el paquete de compatibilidad `Codex.app`:

```bash
/Applications/Codex.app/Contents/Resources/codex --version

## Comentarios y registros

Ingresa <kbd>/</kbd> en el espacio para escribir texto para enviar comentarios al equipo. Si
inicias el envío de comentarios en un chat existente, puedes optar por compartir la
sesión existente junto con tus comentarios. Después de enviar tus comentarios,
recibirás un ID de sesión que podrás compartir con el equipo.

Para informar un problema:

1. Busca [Issues existentes](https://github.com/openai/codex/issues) en el repositorio de Codex en GitHub.
2. [Abre un nuevo Issue de GitHub](https://github.com/openai/codex/issues/new?template=2-bug-report.yml&steps=Uploaded%20thread%3A%20019c0d37-d2b6-74c0-918f-0e64af9b6e14)

Hay más registros disponibles en las siguientes ubicaciones:

- Registros de la App (macOS): `~/Library/Logs/com.openai.codex/YYYY/MM/DD`
- Transcripciones de las sesiones: `$CODEX_HOME/sessions` (valor predeterminado: `~/.codex/sessions`)
- Sesiones archivadas: `$CODEX_HOME/archived_sessions` (valor predeterminado: `~/.codex/archived_sessions`)

Si compartes registros, revísalos primero para confirmar que no contengan información
confidencial.

## Bloqueos y métodos de recuperación

Si un chat parece estar bloqueado:

1. Verifica si Codex está esperando una aprobación.
2. Abre la Terminal y ejecuta un comando básico como `git status`.
3. Inicia un chat nuevo con un prompt más acotado y específico.

Si cancelas por error la creación del Worktree y pierdes el prompt, presiona la tecla de flecha hacia
arriba en el editor para recuperarlo.

## Problemas con la Terminal

**La Terminal parece estar bloqueada**

1. Cierra el panel de la Terminal.
2. Vuelve a abrirlo con <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
3. Vuelve a ejecutar un comando básico como `pwd` o `git status`.

Si los comandos se comportan de forma distinta a la esperada, primero verifica el directorio y la
rama actuales en la Terminal.

Si sigue bloqueada, espera a que terminen los chats activos y reinicia la App.

**Las fuentes no se muestran correctamente**

Codex usa la misma fuente para el panel de revisión, la Terminal integrada y cualquier otro código que se muestre en la App. Puedes configurar la fuente en el panel [Configuración](codex://settings) mediante la opción **Fuente del código**.
