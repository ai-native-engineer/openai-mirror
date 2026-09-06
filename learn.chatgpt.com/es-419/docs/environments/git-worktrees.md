<!-- source: https://learn.chatgpt.com/es-419/docs/environments/git-worktrees -->

Los worktrees permiten que Codex ejecute varios chats independientes en el mismo proyecto sin que interfieran entre sí. El repositorio, el worktree y los comandos permanecen en la computadora o en el entorno de desarrollo remoto donde se encuentra el proyecto. Puedes trabajar directamente en la aplicación de escritorio de ChatGPT o usar [Remoto](/es-419/codex/remote) en la aplicación móvil de ChatGPT para iniciar, guiar, aprobar y revisar chats de worktrees en una computadora conectada.

En los repositorios de Git, las [tareas programadas](/es-419/codex/automations) pueden ejecutarse en worktrees dedicados en segundo plano para que no entren en conflicto con el trabajo en curso. En los proyectos sin control de versiones, las tareas programadas se ejecutan directamente en el directorio del proyecto. También puedes iniciar chats manualmente en un worktree y usar Transferencia para mover un chat entre Local y Worktree.

  Los worktrees no se ejecutan localmente en tu teléfono. Con Remoto, la aplicación móvil
controla Codex en tu computadora conectada, donde permanecen el repositorio y el worktree,
o en el entorno de desarrollo remoto que usa esa computadora. Las siguientes
instrucciones específicas de escritorio se aplican a la computadora conectada.

## Qué es un worktree

Los worktrees solo funcionan en proyectos que forman parte de un repositorio de Git porque, internamente, usan [worktrees de Git](https://git-scm.com/docs/git-worktree). Un worktree te permite crear una segunda copia (“checkout”) de tu repositorio. Cada worktree tiene su propia copia de todos los archivos del repositorio, pero todos comparten los mismos metadatos (la carpeta `.git`) sobre commits, ramas, etc. Esto te permite hacer checkout de varias ramas y trabajar en ellas en paralelo.

## Terminología

- **Checkout local**: el repositorio que creaste. En la aplicación de escritorio de ChatGPT, a veces se denomina simplemente **Local** .
- **Worktree**: un [worktree de Git](https://git-scm.com/docs/git-worktree) creado a partir de tu checkout local en la aplicación de escritorio de ChatGPT.
- **Transferencia**: el flujo que mueve un chat entre Local y Worktree. Codex se encarga de las operaciones de Git necesarias para trasladar tu trabajo de forma segura entre ambos.

## Por qué usar un worktree

1. Trabaja en paralelo con Codex sin alterar la configuración que ya tienes en Local.
2. Pon trabajo en cola para que se ejecute en segundo plano mientras te concentras en lo que haces en primer plano.
3. Más adelante, cuando quieras inspeccionar, probar o colaborar de forma más directa, mueve el chat a Local.

## Primeros pasos

Los worktrees requieren un repositorio de Git. Asegúrate de que el proyecto seleccionado se encuentre en uno.

1.  Selecciona “Worktree”

    En la vista de chat nuevo, selecciona **Worktree** debajo del editor.
    Si quieres, elige un [entorno local](/es-419/codex/environments/local-environment) para ejecutar los scripts de configuración del worktree.

2.  Selecciona la rama inicial

    Debajo del editor, elige la rama de Git en la que se basará el worktree. Puede ser tu rama `main` / `master`, una rama de funcionalidad o tu rama actual con cambios locales que aún no agregaste al área de preparación.

3.  Envía tu prompt

    Envía tu prompt y Codex crea un worktree de Git basado en la rama que seleccionaste. De forma predeterminada, Codex trabaja con un [“HEAD desacoplado”](https://git-scm.com/docs/git-checkout#_detached_head).

4.  Elige dónde seguir trabajando

    Cuando estés listo, puedes seguir trabajando directamente en el worktree o transferir el chat a tu checkout local. Al transferirlo hacia o desde Local, se mueven el chat _y_ el código para que puedas continuar en el otro checkout.

## Trabajar entre Local y Worktree

El uso de los worktrees se parece mucho al de tu checkout local. La diferencia está en el lugar que ocupan en tu flujo de trabajo. Puedes pensar en Local como el primer plano y en Worktree como el segundo plano. Transferencia te permite mover un chat entre ambos.

Internamente, Transferencia se encarga de las operaciones de Git necesarias para mover el trabajo de forma segura entre dos checkouts. Esto es importante porque **Git solo permite que se haga checkout de una rama en un lugar a la vez**. Si haces checkout de una rama en un worktree, **no puedes** hacer checkout de esa misma rama en tu checkout local al mismo tiempo, y viceversa.

En la práctica, hay dos opciones habituales:

1. [Trabaja exclusivamente en el worktree](#option-1-working-on-the-worktree). Esta opción funciona mejor cuando puedes verificar los cambios directamente en el worktree, por ejemplo, porque tienes dependencias y herramientas instaladas mediante un [script de configuración del entorno local](/es-419/codex/environments/local-environment).
2. [Transfiere el chat a Local](#option-2-handing-a-chat-off-to-local). Usa esta opción cuando quieras llevar el chat a primer plano, por ejemplo, para inspeccionar los cambios en tu IDE habitual o porque solo puedes ejecutar una instancia de tu aplicación.

### Opción 1: trabajar en el worktree

<div class="feature-grid">

<div>

Si quieres mantener tus cambios exclusivamente en el worktree, conviértelo en una rama con el botón **Crear rama aquí** del encabezado del chat.

Desde aquí, puedes hacer commit de tus cambios, subir la rama a tu repositorio remoto y abrir un Pull Request en GitHub.

Puedes abrir tu IDE en el worktree con el botón “Abrir” del encabezado, usar la terminal integrada o hacer cualquier otra cosa que necesites desde el directorio del worktree.

</div>

  
    
  

</div>

Recuerda que, si creas una rama en un worktree, no puedes hacer checkout de ella en ningún otro worktree, incluido tu checkout local.

<a id="option-2-handing-a-thread-off-to-local"></a>
<a id="option-2-handing-a-chat-off-to-local"></a>
<a id="option-2-handing-a-task-off-to-local"></a>

### Opción 2: transferir un chat a Local

<div class="feature-grid">

<div>

Si quieres llevar un chat a primer plano, selecciona **Transferir** en el encabezado del chat y muévelo a **Local**.

Esta opción es útil cuando quieres revisar los cambios en la ventana habitual de tu IDE, ejecutar tu servidor de desarrollo actual o validar el trabajo en el mismo entorno que usas a diario.

Codex se encarga de los pasos de Git necesarios para mover el chat de forma segura entre el worktree y tu checkout local.

Cada chat conserva siempre el mismo worktree asociado. Si más adelante vuelves a transferir el chat a un worktree, Codex lo devuelve a ese mismo entorno en segundo plano para que puedas retomar donde lo dejaste.

</div>

  
    
  

</div>

También puedes hacerlo en sentido contrario. Si ya trabajas en Local y quieres liberar el primer plano, usa **Transferir** para mover el chat a un worktree. Esto resulta útil cuando quieres que Codex siga trabajando en segundo plano mientras vuelves a centrarte en otra tarea local.

Como Transferencia usa operaciones de Git, los archivos incluidos en tu archivo `.gitignore` no se moverán con el chat, a menos que Codex los copie a un worktree local administrado mediante `.worktreeinclude`.

## Detalles avanzados

### Worktrees administrados por Codex y worktrees permanentes

De forma predeterminada, los chats usan un worktree administrado por Codex. Estos worktrees están diseñados para ser ligeros y desechables. Por lo general, cada worktree administrado por Codex está dedicado a un solo chat, y Codex devuelve ese chat al mismo worktree si más adelante vuelves a transferirlo allí.

Si quieres un entorno de larga duración, crea un worktree permanente desde el menú de tres puntos de un proyecto en la barra lateral. Esto crea un nuevo worktree permanente que funciona como un proyecto independiente. Los worktrees permanentes no se eliminan automáticamente y puedes iniciar varios chats desde el mismo worktree.

### Cómo administra Codex tus worktrees

Codex crea worktrees en `$CODEX_HOME/worktrees`. El commit inicial es el commit `HEAD` de la rama seleccionada al iniciar el chat. Si elegiste una rama con cambios locales, Codex también aplica al worktree los cambios sin commit. El worktree no tiene ninguna rama en checkout. Está en un estado de [HEAD desacoplado](https://git-scm.com/docs/git-checkout#_detached_head). Esto permite que Codex cree varios worktrees sin generar ramas innecesarias.

### Copiar archivos locales ignorados a worktrees administrados

Los worktrees locales administrados por Codex parten de un checkout de Git, por lo que los archivos con seguimiento ya están presentes. Si tu repositorio ignora archivos de configuración local que necesita un worktree nuevo, agrega un archivo `.worktreeinclude` a la raíz del repositorio y enumera las rutas ignoradas o los patrones con el formato de `.gitignore` que se copiarán cuando Codex cree un worktree administrado.

Usa esta opción para los archivos que Git ignora intencionalmente, como `.env`, `.env.local` o `config/secrets.json`. Codex solo copia los archivos ignorados que coinciden con `.worktreeinclude`; no copia otros archivos locales que Git no tiene bajo seguimiento. No incluyas archivos con seguimiento.

Codex copia automáticamente un archivo `AGENTS.override.md` ignorado a los worktrees locales administrados, por lo que no necesitas incluirlo en `.worktreeinclude`.

```text
# .worktreeinclude
.env
.env.local
config/secrets.json

Codex omite los enlaces simbólicos de origen y no sobrescribe archivos que ya existan en el nuevo checkout. Este comportamiento se aplica a los worktrees locales administrados por la aplicación de escritorio de ChatGPT, pero no a los worktrees remotos ni a los worktrees de Git que crees por tu cuenta desde la línea de comandos.

### Limitaciones de las ramas

Supongamos que Codex completa una tarea en un worktree y decides crear allí una rama `feature/a` con **Crear rama aquí**. Ahora quieres probarla en tu checkout local. Si intentaras hacer checkout de esa rama, recibirías el siguiente error:

fatal: 'feature/a' is already used by worktree at '<WORKTREE_PATH>'

Para resolverlo, tendrías que hacer checkout de una rama distinta de `feature/a` en el worktree.

Si planeas hacer checkout de la rama en tu checkout local, usa Transferencia para mover el chat a Local, en lugar de intentar mantener la misma rama en checkout en ambos lugares al mismo tiempo.

Git impide que se haga checkout de la misma rama en más de un worktree a la vez porque una rama representa una sola referencia mutable (`refs/heads/<name>`), cuyo significado es “el estado que está actualmente en checkout” de un árbol de trabajo.

Cuando se hace checkout de una rama, Git considera que su HEAD pertenece a ese worktree y espera que operaciones como commits, resets, rebases y merges actualicen esa referencia de manera claramente definida y secuencial. Permitir que varios worktrees hagan checkout de la misma rama al mismo tiempo generaría ambigüedad y condiciones de carrera respecto de cuál de los worktrees actualiza la referencia de la rama con sus operaciones, lo que podría provocar la pérdida de commits, índices incoherentes o una resolución de conflictos poco clara.

Al aplicar la regla de una sola rama por worktree, Git garantiza que cada rama tenga una única copia de trabajo de referencia, a la vez que permite que otros worktrees hagan referencia de forma segura a los mismos commits mediante estados de HEAD desacoplado o ramas independientes.

### Limpieza de worktrees

Los worktrees pueden ocupar mucho espacio en disco. Cada uno tiene su propio conjunto de archivos del repositorio, dependencias, cachés de compilación, etc. Por eso, la aplicación de escritorio de ChatGPT intenta mantener la cantidad de worktrees dentro de un límite razonable.

De forma predeterminada, Codex conserva los 15 worktrees administrados por Codex más recientes. Puedes cambiar este límite o desactivar la eliminación automática en Configuración si prefieres administrar por tu cuenta el uso del disco.

Codex intenta no eliminar los worktrees que aún son importantes. Los worktrees administrados por Codex no se eliminan automáticamente si:

- Hay un chat fijado asociado al worktree
- El chat sigue en curso
- El worktree es permanente

Los worktrees administrados por Codex se eliminan automáticamente cuando:

- Archivas el chat asociado
- Codex necesita eliminar worktrees más antiguos para no superar el límite configurado

Antes de eliminar un worktree administrado por Codex, Codex guarda una instantánea del trabajo que contiene. Si abres un chat después de que se haya eliminado su worktree, verás la opción de restaurarlo.

## Preguntas frecuentes

  Sí. Codex crea los worktrees administrados en `$CODEX_HOME/worktrees` de
  forma predeterminada. Para elegir otra ubicación, abre **Configuración \> Worktrees** y cambia
**Directorio raíz de los worktrees**.

<a id="can-i-move-a-chat-between-local-and-worktree"></a>

  Sí. Usa **Transferir** en el encabezado del chat para mover un chat entre tu copia de trabajo local
  y un worktree. Codex se encarga de las operaciones de Git necesarias para mover el
  chat de forma segura entre entornos. Si más adelante vuelves a transferir un chat a un worktree,
  Codex lo devuelve al mismo worktree asociado.

<a id="what-happens-to-chats-if-a-worktree-is-deleted"></a>

  Los chats pueden permanecer en tu historial aunque el directorio subyacente del worktree se
elimine. En el caso de los worktrees administrados por Codex, Codex guarda una instantánea antes de eliminar
el worktree y ofrece restaurarlo si vuelves a abrir el chat asociado.
Los worktrees permanentes no se eliminan automáticamente cuando archivas sus
chats.
