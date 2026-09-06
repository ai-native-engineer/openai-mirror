<!-- source: https://learn.chatgpt.com/es-419/docs/plugins -->

## Descripción general

Los complementos agrupan capacidades en flujos de trabajo reutilizables en ChatGPT y Codex. Pueden
incluir habilidades, conectores o ambos. Ambos productos usan un único directorio universal de
complementos, por lo que los mismos complementos públicos se pueden encontrar en sus interfaces
compatibles.

Los complementos funcionan en Chat y Work en ChatGPT en la web, en computadoras de escritorio y en dispositivos móviles,
y en Codex dentro de la aplicación de escritorio de ChatGPT. Codex CLI también tiene un navegador de complementos
para los entornos de Codex. La extensión para IDE no admite complementos.

En dispositivos móviles, puedes usar en Chat o Work los complementos disponibles para tu cuenta.

Abre la pestaña **Complementos** para explorar e instalar complementos. Una vez instalados, puedes
usarlos en Chat o Work en ChatGPT, o en Codex. Los complementos instalados pueden
agregar habilidades, conectores y herramientas MCP a los chats nuevos.

Abre la pestaña **Complementos** para explorar e instalar complementos. Una vez instalados, puedes
usarlos en Chat o Work. Un complemento puede solicitarte que conectes un servicio
externo antes de que sus herramientas estén disponibles.

En Codex CLI, ingresa `/plugins` para abrir el navegador de complementos. Instala un complemento desde
un Marketplace configurado y luego inicia una sesión nueva antes de usar las habilidades
o herramientas que incluye.

<a id="plugin-directory-in-the-ide-extension"></a>

### Usar complementos desde una interfaz compatible

Los complementos no están disponibles en la extensión para IDE. Para explorar e instalar complementos
para Codex, usa la aplicación de escritorio de ChatGPT o Codex CLI.

Amplía lo que ChatGPT y Codex pueden hacer, por ejemplo:

- Instala el plugin de Codex Security para analizar código autorizado y confirmar
hallazgos de posibles vulnerabilidades.
- Instala el complemento de Gmail para trabajar con Gmail.
- Instala el complemento de Google Drive para trabajar en Drive, Docs, Sheets y
Slides.
- Instala el complemento de Slack para resumir canales o redactar respuestas.

Un complemento puede contener una o más de estas partes:

- **Habilidades:** instrucciones reutilizables para tipos específicos de trabajo. ChatGPT y
  Codex pueden cargarlas cuando sea necesario para seguir los pasos adecuados y usar las
  referencias o los scripts auxiliares apropiados para una tarea.
- **Conectores:** conexiones a herramientas como GitHub, Slack o Google Drive, para que
  ChatGPT y Codex puedan leer información de esas herramientas y realizar acciones en
  ellas. Los conectores exponen herramientas y pueden incluir una interfaz de usuario personalizada.
- **Servidores MCP:** servicios que dan a ChatGPT y Codex acceso a más herramientas o
  información compartida, a menudo proveniente de sistemas externos a tu proyecto local. También
  son los servicios en los que se basan los conectores. Definen herramientas, exigen autenticación, devuelven
  datos estructurados y realizan acciones en sistemas externos.
- **Extensiones del navegador:** capacidades del navegador que un complemento necesita para su
  flujo de trabajo.
- **Hooks:** comandos que se ejecutan en puntos configurados del ciclo de vida. Revisa los hooks
  de los complementos y asegúrate de que sean confiables antes de habilitarlos.
- **Plantillas de tareas programadas:** puntos de partida reutilizables para tareas recurrentes
  donde las tareas programadas estén disponibles.

Puedes compartir complementos publicándolos mediante una fuente de Marketplace, como un
Marketplace basado en un repositorio para un proyecto o equipo. Consulta [Crear plugins](https://developers.openai.com/plugins/build/plugins)
para obtener orientación sobre la configuración del Marketplace, el empaquetado y la distribución.

Si estás creando una integración, comienza con
[Crear un servidor MCP](https://developers.openai.com/plugins/build/mcp-server).
Si el complemento necesita una interfaz de usuario personalizada, usa la
[guía opcional de la interfaz de usuario](https://developers.openai.com/plugins/build/chatgpt-ui).

## Usar e instalar complementos

<a id="plugin-directory-in-the-codex-app"></a>

### Directorio universal de complementos

ChatGPT y Codex usan el mismo catálogo público de complementos. En la web o en la
aplicación de escritorio de ChatGPT, abre la pestaña **Complementos** para explorar e instalar complementos.

  
    
  

El Directorio de complementos organiza los complementos en pestañas:

- **OpenAI:** complementos creados por OpenAI.
- **Nombre de tu espacio de trabajo:** complementos proporcionados por tu espacio de trabajo.
- **Personal:** complementos de tu Marketplace personal, incluidas las secciones **Creados por mí** y
**Compartidos conmigo** cuando esos complementos estén disponibles.

Usa la fila independiente **Instalados** para revisar los complementos que ya instalaste.

Los administradores del espacio de trabajo pueden importar y sincronizar un Marketplace de GitHub para su equipo. Consulta
[Administración de complementos](/es-419/codex/enterprise/plugin-management) para conocer los requisitos de configuración y
acceso.

### Instalar y usar un complemento

Después de abrir el Directorio de complementos:

1. Busca un complemento o explora el directorio y luego abre sus detalles.
2. Selecciona el botón con el signo más para instalar el complemento.
3. Si el complemento necesita un conector, conéctalo cuando se te solicite. Algunos complementos
te piden que te autentiques durante la instalación. Otros esperan hasta la primera vez que
los uses.
4. Después de instalarlo, inicia un chat nuevo y pide a ChatGPT o Codex que use el
complemento.

### Conectarse con socios compatibles mediante Iniciar sesión con ChatGPT

**Iniciar sesión con ChatGPT** se está implementando en versión beta para complementos y
sitios de socios compatibles, incluidos Airtable, GitLab, HubSpot, Notion, Supabase y
Vercel. Cuando la opción esté disponible, selecciona **Iniciar sesión con ChatGPT** al
conectar el complemento para crear o vincular tu cuenta con ese servicio.

Al iniciar sesión, solo se comparten con el socio tu nombre, dirección de correo electrónico y foto de perfil, cuando
estén disponibles. Esto no le otorga al complemento acceso a tus datos ni
aprueba acciones automáticamente. Como paso independiente, revisa y aprueba los
permisos que solicita el complemento antes de usar la conexión.

Después de instalar un complemento, puedes usarlo directamente en la ventana del prompt:

  
    
  

<div class="not-prose mt-4 grid gap-4 md:grid-cols-2">
  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">Describe la tarea directamente</p>
    <p class="mt-2 text-sm text-secondary">
      Pide el resultado que buscas, por ejemplo, “Resume los hilos no leídos de Gmail
de hoy” u “Obtén las notas de lanzamiento más recientes de Google Drive”.
    </p>
    <p class="mt-3 text-sm text-secondary">
      Usa esta opción cuando quieras que ChatGPT elija las herramientas instaladas adecuadas para la
tarea.
    </p>
  </div>

  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">Elige un complemento específico</p>
    <p class="mt-2 text-sm text-secondary">
      Escribe <code>@</code> para invocar explícitamente el complemento o una de las habilidades
      que incluye.
    </p>
    <p class="mt-3 text-sm text-secondary">
      Usa esta opción cuando quieras especificar qué complemento o habilidad debe usar ChatGPT.
      Consulta <a href="/codex/skills-and-plugins">Habilidades y complementos</a>.
    </p>
  </div>
</div>

### Usar Apple Messages desde Codex

El complemento de Apple Messages está disponible en todos los planes en la aplicación de escritorio de ChatGPT
para macOS. En Codex y ChatGPT Work, puede leer y buscar chats de iMessage, SMS y
RCS en tu Mac y enviar mensajes en tu nombre a través de la aplicación Messages.
No te permite interactuar con ChatGPT de forma remota a través de Messages y
no funciona en los chats normales de ChatGPT.

En esta versión, el complemento de Messages solo está incluido en la compilación para Apple Silicon
(arm64) de la aplicación de escritorio de ChatGPT.

1. Abre **Complementos**, busca el complemento de Apple Messages e instálalo.
2. Inicia un chat nuevo en Codex o ChatGPT Work y pídele que busque, resuma, redacte
o envíe un mensaje.
3. Concede los permisos de macOS solicitados antes de que ChatGPT lea el contenido de Messages.
4. Revisa el mensaje y sus destinatarios antes de permitir su envío.

De forma predeterminada, ChatGPT solo envía mensajes después de que apruebes el mensaje y sus
destinatarios. Selecciona **Permitir una vez** para aprobar únicamente ese envío. Si seleccionas
**Permitir siempre los envíos a este chat**, ChatGPT podrá enviar mensajes futuros a ese
chat de Messages sin solicitar otra aprobación de envío.

Mantén la aprobación para cada envío en los chats que puedan contener instrucciones no confiables o
engañosas. La aprobación persistente elimina tu última oportunidad de revisar un mensaje
antes de que ChatGPT lo envíe en tu nombre. Úsala solo si aceptas ese riesgo.

Para restablecer la aprobación para cada envío, abre **Configuración** \> **Uso de la computadora** y selecciona
**Administrar** junto a **Messages**. En **Envío siempre permitido**, selecciona el
ícono de la papelera junto al chat y luego confirma con **Eliminar**. ChatGPT volverá a solicitar aprobación
antes de enviar mensajes a ese chat.

**Problema conocido:** si tu tarea está configurada en **Acceso completo** o desactiva de otro modo
las solicitudes de aprobación, es posible que Apple Messages no pueda mostrar la confirmación necesaria
para enviar mensajes. Cambia a **Solicitar aprobación** o **Aprobar por mí** y vuelve a intentarlo.

Apple Messages funciona en tu Mac. No está disponible directamente en ChatGPT en la
web ni en dispositivos móviles, en Codex CLI ni en la extensión para IDE.

En los espacios de trabajo administrados, los administradores pueden desactivar Apple Messages mediante el
control existente de Uso de la computadora.

<a id="plugin-directory-in-codex-cli"></a>

### Navegador de complementos en Codex CLI

En Codex CLI, ejecuta el siguiente comando para abrir el navegador de complementos:

```text
codex
/plugins

  
    
  

El navegador de complementos de la CLI agrupa los complementos por Marketplace. Usa las pestañas del Marketplace
para cambiar de fuente, abre un complemento para consultar sus detalles, instala o desinstala
elementos del Marketplace y presiona <kbd>Espacio</kbd> en un complemento instalado para activarlo
o desactivarlo.

<a id="api-key-availability"></a>

### Disponibilidad con claves de API

Si [inicias sesión en Codex con una clave
de API de OpenAI](/es-419/codex/auth#sign-in-with-an-api-key), puedes explorar, instalar y administrar
complementos compatibles seleccionados por OpenAI en Codex CLI y en Codex dentro de la aplicación
de escritorio de ChatGPT. Algunos complementos no están disponibles con la autenticación mediante claves de API porque sus
flujos de conexión requieren capacidades de OAuth no compatibles. Consulta el uso de los complementos
en la [página de uso de la plataforma](https://platform.openai.com/usage).

### Cómo funcionan los permisos y el uso compartido de datos

En ChatGPT en la web, Chat y Work usan los permisos del espacio de trabajo y las herramientas
disponibles para ese chat. Los conectores siguen necesitando su propio inicio de sesión y acceso.

Cuando una capacidad de un complemento se ejecuta a través de un host de Codex, se aplican el [sandbox y la
política de aprobación](/es-419/codex/agent-approvals-security) de ese host.
Las conexiones a servicios externos usan la autenticación y los
controles de acceso propios de cada servicio.

- Las habilidades incluidas están disponibles cuando inicias un chat nuevo o una nueva sesión de CLI
después de la instalación.
- Si un complemento incluye conectores, el producto activo puede pedirte que los instales
o que inicies sesión en ellos durante la configuración o la primera vez que los uses.
- Si un complemento incluye servidores MCP, es posible que requieran una configuración adicional o
autenticación antes de que puedas usarlos.
- Cuando ChatGPT envía datos a través de un conector incluido, se aplican los términos y la política de privacidad
de ese servicio.

### Eliminar un complemento

Para eliminar un complemento, ábrelo en un navegador de complementos compatible y selecciona
**Desinstalar complemento** cuando esa acción esté disponible. Es posible que los complementos instalados en el espacio de trabajo o
los predeterminados no ofrezcan esa acción; en ese caso, los controla
el administrador de tu espacio de trabajo.

Al desinstalar un complemento, se elimina su paquete de ese entorno de ChatGPT o Codex,
pero los conectores incluidos permanecen conectados hasta que los administres en
ChatGPT.

## Crear tu propio complemento

Si quieres crear, probar o distribuir tu propio complemento, consulta
[Crear plugins](https://developers.openai.com/plugins/build/plugins). En esa página se abordan la creación local de la estructura inicial,
la configuración manual del Marketplace, el uso compartido en el espacio de trabajo, los archivos de manifiesto de los complementos y las pautas
de empaquetado.

Si tu complemento incluye capacidades basadas en un servidor, consulta
[Crear un servidor MCP](https://developers.openai.com/plugins/build/mcp-server).
Las herramientas MCP pueden funcionar sin una interfaz de usuario personalizada o devolver una interfaz de usuario cuando una presentación visual facilita
el flujo de trabajo.

Cuando tu complemento esté listo para su revisión, consulta
[Enviar complementos](https://developers.openai.com/plugins/deploy/submission) para conocer el proceso de envío
en la plataforma de OpenAI, los permisos necesarios, los materiales de revisión, las comprobaciones de MCP y los requisitos
de los casos de prueba.

## Guías de complementos

- [Grabar y reproducir](/es-419/codex/extend/record-and-replay): muéstrale a ChatGPT un flujo de trabajo
  una sola vez y conviértelo en una habilidad reutilizable.
- [Plugin de Codex Security](/es-419/codex/security/plugin): analiza código autorizado,
  confirma los hallazgos y prepara correcciones revisadas.
