<!-- source: https://learn.chatgpt.com/es-419/docs/projects -->

Usa un proyecto para organizar chats relacionados y darle a ChatGPT el contexto que necesita.
La vista **Proyectos** de la aplicación de escritorio de ChatGPT incluye proyectos de ChatGPT y
proyectos locales que se conectan a carpetas de tu computadora.

## Elegir un proyecto o empezar sin uno

Crea un proyecto cuando el trabajo se extienda en el tiempo, genere más de un
resultado o dependa de los mismos archivos y fuentes. Inicia un chat sin proyecto
cuando el trabajo sea independiente y no necesite contexto compartido de un proyecto.

Usa un proyecto para mantener juntos los chats, archivos, instrucciones y fuentes relacionados.
El mismo proyecto puede contener chats iniciados con Chat o ChatGPT Work.

## Elegir un proyecto o iniciar un chat sin proyecto

Crea un proyecto cuando el trabajo se extienda en el tiempo, genere más de un
resultado o dependa de los mismos archivos y fuentes. Inicia un chat sin proyecto
cuando el trabajo sea independiente y no necesite contexto compartido de un proyecto.

Cada proyecto tiene una sección **Chats** , donde se muestran sus chats, y una sección **Fuentes**
para los archivos subidos y el contexto conectado. Las instrucciones del proyecto se aplican
a todos sus chats. Un proyecto de ChatGPT no proporciona acceso directo a una carpeta de
tu computadora, así que sube o conecta las fuentes que quieras que ChatGPT use.

Con cualquiera de las dos opciones, inicia un chat nuevo desde el proyecto para usar sus archivos e
instrucciones compartidos; luego, vuelve a él desde **Chats**.

Codex CLI considera el directorio desde donde lo inicias como el proyecto del chat.
Ejecuta `codex` desde el directorio en el que quieras que trabaje Codex o usa
`--cd <directory>` (`-C`) para establecerlo de forma explícita. La CLI no muestra la
vista Proyectos de ChatGPT.

La extensión para IDE considera la carpeta o el espacio de trabajo abierto en tu IDE como el proyecto
local. En un espacio de trabajo con varias raíces, selecciona la raíz del espacio de trabajo para el chat. La
extensión no muestra la vista Proyectos de ChatGPT de la web ni de la aplicación de escritorio.

<a id="work-in-a-project"></a>

## Trabajar en un proyecto

La vista **Proyectos** reúne los proyectos de ChatGPT y los proyectos locales en un solo lugar.
Los proyectos de ChatGPT mantienen disponibles los archivos y el contexto del proyecto en los chats relacionados. Un
proyecto local permite que los chats accedan a una o más carpetas de tu computadora, como una
colección de archivos fuente o una base de código.

Inicia un chat distinto para cada resultado específico, de modo que sus mensajes y resultados se mantengan
enfocados mientras el proyecto mantiene organizado el trabajo relacionado.

  
    
  

## Trabajar en un proyecto

Un proyecto de ChatGPT permite que sus chats accedan a los mismos archivos subidos, a las instrucciones
del proyecto y a las fuentes conectadas. Usa Chat para una consulta breve o
ChatGPT Work para un entregable de mayor alcance; ambos aparecen como chats en la sección
**Chats** del proyecto. Inicia un chat distinto para cada resultado específico a fin de que sus
mensajes y resultados se mantengan enfocados mientras el proyecto conserva el contexto compartido.

## Trabajar en el directorio de un proyecto

Inicia Codex desde el directorio que deba proporcionar el contexto de archivos del chat. Usa
`/new` para iniciar un chat distinto para cada resultado específico. Usa `/resume` mientras
Codex esté abierto o ejecuta `codex resume` para continuar un chat guardado.

El chat conserva su transcripción y el directorio de trabajo registrado, mientras Codex lee
los archivos del árbol de trabajo actual. Conserva las instrucciones permanentes del proyecto en
`AGENTS.md` o en documentación registrada en el control de versiones para que estén disponibles en chats futuros.

## Trabajar en un espacio de trabajo

Abre la carpeta o el espacio de trabajo que deba proporcionar el contexto de archivos del chat. Inicia
un chat nuevo para cada resultado específico y, luego, selecciónalo en **Chats recientes** para
continuarlo. Los chats del mismo proyecto pueden trabajar con los mismos archivos, pero cada
chat conserva su propia transcripción.

La selección actual y los archivos abiertos proporcionan contexto para el turno actual. Conserva
las instrucciones permanentes del proyecto en `AGENTS.md` o en documentación registrada en el control de versiones para que estén
disponibles en chats futuros.

<a id="manage-project-threads"></a>
<a id="organize-projects-and-chats"></a>

<a id="organize-projects-and-tasks"></a>

## Organizar proyectos y chats

Mantén visible el trabajo activo y deja a un lado el que ya terminaste:

- **Fija un proyecto** para mantenerlo cerca de la parte superior de la barra lateral. También puedes fijarlo
  desde la vista Proyectos.
- **Fija un chat** si vuelves a él con frecuencia, aunque aparezcan chats más recientes en el
  proyecto.
- **Cambia el nombre de un chat** y usa un título breve que describa su resultado, como “Resumen del lanzamiento del
  tercer trimestre” o “Revisión de accesibilidad del proceso de pago”.
- **Busca proyectos** desde la vista Proyectos. Abre **Buscar chats** desde la
  barra lateral para encontrar un chat anterior cuando recuerdes una frase o el nombre de una rama,
  pero no el título. Buscar chats no tiene un atajo predeterminado, pero puedes asignar
  uno en **Configuración \> Atajos de teclado**.
- **Archiva un chat** cuando termines el trabajo. En el menú de un proyecto, selecciona
**Archivar chats** para archivar sus chats a la vez.

Fijar un proyecto o un chat no agrega contexto ni cambia a qué puede acceder ChatGPT. Solo cambia
el lugar donde aparece el proyecto o el chat en la barra lateral.

Restaura los chats archivados desde **Configuración \> Chats archivados**.

<a id="organize-projects-and-tasks-1"></a>

## Organizar proyectos y chats

Mantén visible el trabajo activo y deja a un lado el que ya terminaste:

- **Fija un proyecto** para mantenerlo cerca de la parte superior de la barra lateral. También puedes fijarlo
  desde la vista Proyectos.
- **Fija un chat** si vuelves a él con frecuencia, aunque aparezcan chats más recientes en el
  proyecto.
- **Cambia el nombre de un chat** y usa un título breve que describa su resultado, como “Resumen del lanzamiento del
  tercer trimestre” o “Revisión de accesibilidad del proceso de pago”.
- **Busca proyectos** desde la vista Proyectos. Busca chats anteriores con
<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>K</kbd> cuando recuerdes una frase o el
  nombre de una rama, pero no el título.
- **Archiva un chat** cuando termines el trabajo.

Fijar un proyecto o un chat no agrega contexto ni cambia a qué puede acceder ChatGPT. Solo cambia
el lugar donde aparece el proyecto o el chat en la barra lateral.

Restaura los chats archivados desde **Configuración \> Controles de datos \> Chats archivados**.

<a id="use-local-projects-for-folders-and-codebases"></a>

## Usar proyectos locales para carpetas y bases de código

Agrega un proyecto local cuando ChatGPT necesite leer o modificar archivos de tu computadora.
Los proyectos no necesitan una carpeta, pero puedes adjuntar carpetas según sea necesario.

Para agregar o cambiar carpetas, abre el menú del proyecto y selecciona **Editar proyecto**.
Selecciona **Agregar carpeta** para adjuntar varias carpetas. ChatGPT puede leer y modificar archivos
en todas las carpetas adjuntas. Para cambiar el directorio de trabajo predeterminado, coloca el cursor sobre una
carpeta y selecciona **Establecer como principal**.

Los chats nuevos se inician en la carpeta principal. Codex también usa esa carpeta de forma
predeterminada para las operaciones de Git y la detección automática de `AGENTS.md`, habilidades y
`config.toml`. Las carpetas secundarias siguen disponibles para buscar, leer y
editar archivos, pero Codex no detecta automáticamente esos archivos del proyecto en las
carpetas secundarias.

Usa varias carpetas cuando el trabajo relacionado se encuentre en distintos lugares, como una aplicación y
su documentación o un sitio web y su backend. Crea proyectos separados para
trabajos no relacionados o cuando cada chat deba acceder solo a una parte de un repositorio.
Esto mantiene enfocado el contexto de trabajo. Actualmente, los proyectos remotos admiten una sola
carpeta.

Usa [entornos locales](/es-419/codex/environments/local-environment) para definir acciones de configuración
y comandos comunes para un proyecto. El [panel de
revisión](/es-419/codex/code-review?surface=app) puede mostrar cambios en los repositorios
adjuntos al mismo proyecto. Las acciones de Pull Request y de
[worktree](/es-419/codex/environments/git-worktrees) se aplican al repositorio
principal. Cuando inicias un chat en un worktree, las demás carpetas permanecen
adjuntas.

Los proyectos y los worktrees organizan el trabajo, pero el [sandbox](/es-419/codex/sandboxing)
impone restricciones sobre lo que los comandos locales pueden leer o modificar y a qué pueden acceder por la red.

<a id="start-without-a-project"></a>

<a id="start-a-task-without-a-project"></a>

## Iniciar un chat sin proyecto

Selecciona **Chat nuevo** cuando el trabajo sea independiente y no requiera archivos
ni instrucciones compartidos del proyecto ni acceso a carpetas. Crea primero un proyecto cuando
varios chats vayan a depender del mismo contexto.

<a id="start-a-task-without-a-project-1"></a>

## Iniciar un chat sin proyecto

Inicia un chat desde Inicio de ChatGPT cuando no necesite archivos compartidos del proyecto,
instrucciones ni fuentes. Puedes usar Chat o ChatGPT Work; en la web,
ambos crean chats.

Si el trabajo se amplía, pásalo a un proyecto y usa nombres de chat claros para cada
resultado. Un proyecto puede contener chats en paralelo para investigación, redacción, revisión y
seguimiento sin mezclar todos los mensajes en un solo contexto.

<a id="start-a-chat"></a>
<a id="start-a-standalone-chat"></a>

<a id="use-quick-chat-for-a-quick-conversation"></a>

## Usar Chat rápido para una consulta breve

Chat rápido abre un chat normal de ChatGPT. Los chats de ChatGPT no aparecen en la
barra lateral de Codex, que contiene tus chats y proyectos de Codex.

Coloca el cursor sobre **Chat nuevo** y selecciona el ícono de **Chat rápido** que aparece a la derecha. También puedes
presionar

<kbd>Cmd+Option+N</kbd> en macOS o <kbd>Ctrl+Alt+N</kbd> en Windows y Linux.
Desde **Chat nuevo**, puedes abrir un chat existente de ChatGPT y agregarlo a un chat
de Codex.

## Incorporar otras herramientas y contexto

- Adjunta archivos o [imágenes de entrada](/es-419/codex/image-inputs) directamente a un chat
  cuando solo correspondan a esa solicitud.
- Instala [complementos](/es-419/codex/plugins) para incorporar contexto y acciones de otros
  servicios.
- Configura servidores [MCP](/es-419/codex/extend/mcp) cuando tu organización o configuración de desarrollo
  ofrezca herramientas mediante Model Context Protocol.
- Usa las [Memorias](/es-419/codex/customization/memories), cuando estén disponibles, para llevar el contexto útil de
  trabajos anteriores a chats futuros.

- Envía [imágenes de entrada](/es-419/codex/image-inputs) a un chat cuando el contexto visual solo sea relevante
  para esa solicitud.
- Instala [complementos](/es-419/codex/plugins) para incorporar contexto y acciones de otros
  servicios.
- Configura servidores [MCP](/es-419/codex/extend/mcp) cuando tu organización o tu configuración de desarrollo
  expongan herramientas mediante Model Context Protocol.
- Usa las [memorias](/es-419/codex/customization/memories), cuando estén disponibles, para incorporar contexto útil de
  trabajos anteriores en chats futuros.

- Haz referencia a archivos abiertos o selecciona código en el editor para agregar contexto al
turno actual.
- Configura servidores [MCP](/es-419/codex/extend/mcp) cuando tu organización o tu configuración de desarrollo
  expongan herramientas mediante Model Context Protocol.
- Usa las [memorias](/es-419/codex/customization/memories) del host de Codex conectado, cuando
  estén disponibles, para incorporar contexto útil en chats futuros.

- Agrega archivos y fuentes conectadas a la sección **Fuentes** del proyecto cuando
  deban estar disponibles en todos sus chats.
- Adjunta archivos o [imágenes de entrada](/es-419/codex/image-inputs) directamente a un chat cuando
  solo sean relevantes para ese chat.
- En ChatGPT Work, instala [complementos](/es-419/codex/plugins) para incorporar contexto y
  acciones de otros servicios.
- Usa las [memorias](/es-419/codex/customization/memories), cuando estén disponibles, para incorporar contexto útil de
  trabajos anteriores en chats futuros.

## Próximos pasos

- [Aprende a escribir y perfeccionar prompts](/es-419/codex/prompting)
- [Aprende a usar ChatGPT](/es-419/codex/use-chatgpt)
- [Continúa con el trabajo de larga duración](/es-419/codex/long-running-work)
