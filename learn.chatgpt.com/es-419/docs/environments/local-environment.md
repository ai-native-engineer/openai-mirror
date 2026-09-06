<!-- source: https://learn.chatgpt.com/es-419/docs/environments/local-environment -->

Los entornos locales permiten definir los pasos necesarios para configurar los worktrees, así como las acciones comunes de un proyecto.

  Los entornos locales solo están disponibles en Codex dentro de la aplicación de escritorio de ChatGPT.
  Selecciona **Codex** antes de configurar o usar un entorno local.

Configura tus entornos locales desde el panel de [configuración de la aplicación de escritorio de ChatGPT](codex://settings). Puedes agregar el archivo generado al repositorio Git de tu proyecto para compartirlo con otras personas.

Codex guarda esta configuración en la carpeta `.codex`, en la raíz de tu
proyecto. Si tu repositorio contiene más de un proyecto, abre el directorio
del proyecto que contiene la carpeta compartida `.codex`.

## Scripts de configuración

Como los worktrees se ejecutan en directorios distintos de los de tus chats locales, es posible que tu proyecto no esté completamente configurado y que le falten dependencias o archivos que no se hayan incluido en tu repositorio. Los scripts de configuración se ejecutan automáticamente cuando Codex crea un worktree nuevo al iniciar un chat nuevo.

Usa este script para ejecutar cualquier comando necesario para configurar tu entorno, como instalar dependencias o ejecutar un proceso de compilación.

Por ejemplo, en un proyecto de TypeScript, quizás quieras instalar las dependencias y realizar una compilación inicial mediante un script de configuración:

```bash
npm install
npm run build

Si tu configuración es específica de una plataforma, define scripts de configuración para macOS, Windows o Linux que reemplacen el script predeterminado.

## Acciones

<section class="feature-grid">

<div>
Usa acciones para definir tareas comunes, como iniciar el servidor de desarrollo de tu aplicación o ejecutar la suite de pruebas. Estas acciones aparecen en la barra superior de la aplicación de escritorio de ChatGPT para que puedas acceder rápidamente a ellas. Las acciones se ejecutan en la [terminal integrada](/es-419/codex/integrated-terminal) de la aplicación.

Las acciones te evitan tener que escribir comandos para tareas habituales, como ejecutar una compilación de tu proyecto o iniciar un servidor de desarrollo. Para realizar una depuración rápida y puntual, puedes usar directamente la terminal integrada.

</div>

  
    
  

</section>

Por ejemplo, para un proyecto de Node.js, podrías crear una acción “Ejecutar” que contenga el siguiente script:

```bash
npm start

Si los comandos de tu acción son específicos de una plataforma, define scripts específicos para macOS, Windows y Linux.

Para identificar tus acciones, elige un ícono asociado a cada acción.

## Usar las herramientas integradas de Git

<div class="my-8 grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-center">

<div>

En Codex, la aplicación de escritorio de ChatGPT proporciona controles habituales de Git junto a cada
proyecto local y worktree. El panel de diferencias muestra los cambios en el checkout actual
y te permite agregar comentarios en línea que Codex debe atender. Puedes preparar o revertir cada
fragmento, preparar o revertir archivos completos, hacer commit de los cambios, hacer push de una rama y crear
un Pull Request sin salir de la aplicación.

Usa la [terminal integrada](/es-419/codex/integrated-terminal) para las operaciones de Git
que la aplicación no ofrece. Para mantener los cambios simultáneos aislados de
tu checkout local, inicia la tarea en un [worktree](/es-419/codex/environments/git-worktrees).

</div>

  

</div>
