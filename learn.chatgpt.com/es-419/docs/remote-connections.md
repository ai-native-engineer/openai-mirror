<!-- source: https://learn.chatgpt.com/es-419/docs/remote-connections -->

Desktop,
  Storage,
  Terminal,
} from "@components/react/oai/platform/ui/Icon.react";

Las conexiones remotas te permiten acceder al trabajo en curso en otro dispositivo o equipo.
En la app móvil de ChatGPT, abre **Remoto** para trabajar con chats de ChatGPT o Codex en
un dispositivo Mac o Windows conectado. También puedes continuar el trabajo desde otro
dispositivo compatible que ejecute la aplicación de escritorio de ChatGPT o conectar la app a proyectos
en un host SSH.

El acceso remoto utiliza los proyectos, los chats, los archivos, las credenciales,
los permisos, los complementos, el Uso de la computadora, la configuración del navegador y las herramientas locales del host conectado.

## Qué puedes hacer de forma remota

- Inicia chats nuevos en proyectos del host o continúa los existentes.
- Envía instrucciones de seguimiento, responde preguntas y orienta el trabajo en curso.
- Aprueba comandos y otras acciones.
- Revisa los resultados generados, las diferencias, los resultados de las pruebas, la salida de la terminal y las capturas de pantalla.
- Recibe una notificación cuando ChatGPT complete una tarea o necesite tu atención.
- Cambia entre hosts conectados y chats.

Las siguientes secciones explican cómo abrir **Remoto** en la app móvil de ChatGPT para acceder a un
host con la app de escritorio. Para conectar Codex a un proyecto en un host SSH, consulta
[conectarse a un host SSH](#connect-to-an-ssh-host).

<div class="not-prose my-6 max-w-4xl rounded-xl bg-[url('/images/codex/codex-wallpaper-1.webp')] bg-cover bg-center p-4 md:p-8">
  
    
      
    
  
</div>

<a id="before-you-set-up-mobile-access"></a>

## Antes de configurar Remoto

  Remoto admite hosts que ejecutan la aplicación de escritorio de ChatGPT en macOS y Windows.
  Puedes controlar un host desde ChatGPT en iOS o Android, o desde otro dispositivo Mac o
  Windows cuando esté disponible **Controlar otros dispositivos** . La disponibilidad puede
  variar según el despliegue.

Asegúrate de tener:

- Acceso a Codex en la cuenta y el espacio de trabajo de ChatGPT que quieras usar.
- La versión más reciente de la app móvil de ChatGPT en un dispositivo iOS o Android. Si **Remoto**
  no aparece en la app, primero actualiza ChatGPT.
- La versión más reciente de la aplicación de escritorio de ChatGPT para macOS o Windows, en ejecución en un host activo,
en línea y con sesión iniciada en la misma cuenta y el mismo espacio de trabajo. La configuración móvil se inicia
desde la app; no puedes realizarla desde Codex CLI ni desde la extensión para IDE.
- Cualquier configuración requerida de autenticación multifactor, SSO o llave de acceso para
esa cuenta o ese espacio de trabajo.

Si usas Codex mediante un espacio de trabajo de ChatGPT, es posible que tu administrador deba habilitar
el acceso a Control remoto antes de que puedas conectarte desde tu teléfono.

<a id="set-up-mobile-access"></a>

## Configurar Remoto

Comienza en la aplicación de escritorio de ChatGPT en el host que quieras conectar. El flujo de configuración
habilita el acceso remoto para ese host y luego muestra un código QR que puedes escanear desde tu
teléfono.
El código QR vincula ese teléfono con ese host. Vincula cada teléfono o dispositivo compatible con la
app de escritorio con cada host que quieras controlar.

  Las conexiones existentes que se hayan usado desde el 8 de junio de 2026 permanecen vinculadas. Si no has
usado una conexión existente desde el 8 de junio de 2026, actualiza ambas apps y vuelve a vincular los
dispositivos.

1. Inicia la configuración de Remoto.

   Abre la aplicación de escritorio de ChatGPT en el host. Ve a **Configuración** \>
**Conexiones** \> **Controlar esta Mac o PC** y luego selecciona **Configurar** o
**Agregar**. Aprueba el acceso remoto y completa cualquier verificación solicitada.

2. Escanea el código QR.

   Usa tu teléfono para escanear el código QR que muestra la app. El código abre ChatGPT
para que puedas terminar de conectar la app móvil al host.

3. Completa la configuración en ChatGPT.

   ChatGPT abre el flujo de configuración de Remoto. Confirma que estás usando la misma cuenta de ChatGPT
y el mismo espacio de trabajo; luego, completa los pasos requeridos de autenticación multifactor, SSO
o llave de acceso. Cuando la configuración se complete correctamente, el host aparecerá en Remoto en tu
teléfono.

4. Revisa la configuración del host.

   En la app del host, usa **Configuración** \> **Conexiones** para administrar los
   dispositivos conectados. También puedes elegir si quieres mantener la computadora activa, habilitar
   el Uso de la computadora o instalar la Extensión de Chrome.

  

## Elegir qué conectar

Comienza con la laptop o computadora de escritorio donde ya usas ChatGPT. Agrega una computadora siempre
encendida o un host SSH cuando necesites acceso continuo o un entorno diferente.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Tu laptop o computadora de escritorio</span></span>

Conecta la Mac o PC con Windows donde ya esté instalada la app de escritorio. Esto
te da acceso remoto a los mismos proyectos, chats, credenciales, complementos y configuración
local que ya usas.

Si esa computadora entra en reposo, pierde acceso a la red o se cierra la app, el acceso remoto
se interrumpe hasta que vuelva a estar disponible. Si usas esta computadora como dispositivo host,
mantenla conectada a la corriente y usa la configuración de conexión del host para evitar que entre en reposo cuando
esa opción esté disponible.

En una laptop Mac, el acceso remoto puede seguir disponible si la tapa está abierta y el equipo está
conectado a la corriente. Con la tapa cerrada, conecta también una pantalla externa. Si seleccionas
**Reposo** , el acceso remoto se interrumpe de todos modos.

En un host con Windows, mantén la sesión desbloqueada y disponible para las tareas que usan
[Uso de la computadora](/es-419/codex/computer-use). El Uso de la computadora en Windows se ejecuta en
primer plano, por lo que el control remoto es ideal para iniciar o revisar el trabajo mientras
dedicas el escritorio del host a la tarea.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Una computadora dedicada siempre encendida</span></span>

Usa una Mac o una PC con Windows dedicada y siempre encendida cuando quieras que ChatGPT permanezca
disponible para trabajos de larga duración.

Instala en esa máquina los proyectos, las credenciales, los servidores MCP, las habilidades y las herramientas que ChatGPT o
Codex deban usar.

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>Un entorno de desarrollo remoto</span></span>

Usa un host SSH o un entorno de desarrollo remoto administrado cuando el proyecto
ya se encuentre en un entorno remoto. Primero, conecta el host de la app de escritorio a ese
entorno; tu teléfono seguirá conectándose al mismo host y ChatGPT trabajará
en el entorno remoto con sus dependencias, políticas de seguridad y recursos de
cómputo.

Para obtener detalles sobre la configuración de SSH, consulta [conectarse a un host SSH](#connect-to-an-ssh-host).

  Para realizar tareas en el navegador o el escritorio de una computadora siempre encendida o un host remoto, habilita
el Uso de la computadora e instala la Extensión de Chrome en ese host.

## Qué proporciona el host conectado

Tu teléfono envía prompts, aprobaciones y mensajes de seguimiento a ChatGPT. El
host conectado proporciona el entorno que usa ChatGPT.

Esto significa lo siguiente:

- Los archivos del repositorio y los documentos locales provienen del host conectado.
- Los comandos de shell se ejecutan en ese host o entorno remoto.
- Los servidores MCP, las habilidades, el acceso al navegador y el Uso de la computadora provienen de la
configuración de ese host.
- Los sitios web con sesión iniciada y las apps de escritorio solo están disponibles cuando el host puede
acceder a ellos.
- La configuración del entorno aislado, los controles de seguridad y las aprobaciones de acciones siguen aplicándose
a la sesión conectada.

Una capa segura de retransmisión mantiene las máquinas de confianza accesibles desde tus dispositivos autorizados
de ChatGPT sin exponerlas directamente a la internet pública.

## Retomar el trabajo desde otro dispositivo

Puedes continuar el trabajo desde otro dispositivo con sesión iniciada que ejecute la aplicación de escritorio
de ChatGPT y admita el control remoto. Por ejemplo, si tu laptop no está disponible, puedes
iniciar un chat desde tu teléfono en un host siempre encendido y después abrir la app en
tu laptop para continuar allí el mismo chat.

En un dispositivo Mac o Windows donde la función esté disponible, usa **Configuración \>
Conexiones \> Controlar otros dispositivos** para agregar el otro host. Un dispositivo puede permitir el
acceso remoto y controlar otro dispositivo al mismo tiempo.

  

## Conectarse a un host SSH

En la aplicación de escritorio de ChatGPT, agrega proyectos remotos de un host SSH y ejecuta chats
que usen el sistema de archivos y el shell remotos. Los chats de proyectos remotos ejecutan comandos,
leen archivos y escriben cambios en el host remoto.

Mantén el host remoto configurado según los mismos criterios de seguridad que aplicas al
acceso SSH habitual: claves de confianza, cuentas con privilegios mínimos y ningún
servicio de escucha público sin autenticación.

1. Agrega el host a tu configuración de SSH para que Codex pueda detectarlo automáticamente.

   ```text
   Host devbox
     HostName devbox.example.com
     User you
     IdentityFile ~/.ssh/id_ed25519

   Codex lee de `~/.ssh/config` los alias explícitos de hosts, los resuelve con
   OpenSSH e ignora los hosts definidos solo mediante patrones.

2. Confirma que puedes conectarte por SSH al host desde la máquina en la que se ejecuta la app.

   ```bash
   ssh devbox

3. Instala Codex en el host remoto y autentícate.

   La app inicia el App Server remoto de Codex mediante SSH con el shell de inicio de sesión del
   usuario remoto. Asegúrate de que, en el host remoto, el comando `codex` esté disponible en la
   variable `PATH` de ese shell.

4. En la app, abre **Configuración \> Conexiones**, agrega o habilita el host SSH y luego
   elige una carpeta de proyecto remoto.

  

<a id="hand-off-a-thread-between-hosts"></a>
<a id="hand-off-a-chat-between-hosts"></a>
<a id="hand-off-a-task-between-hosts"></a>

## Transferir un chat entre hosts

La transferencia mueve un chat existente y su estado de Git entre tu computadora local
y un host remoto conectado. Úsala para comenzar a trabajar localmente, continuar en un
worktree de una computadora remota y traer el chat de vuelta más adelante.

Antes de transferir un chat, conecta el host de destino y guarda un proyecto
para el mismo repositorio de Git en ese host. Si el proyecto es un subdirectorio del
repositorio, guarda el mismo subdirectorio en ambos hosts. Codex solo muestra
los destinos donde haya un proyecto guardado que coincida.

Para transferir un chat:

1. Abre el chat en la app de escritorio.
2. En la parte inferior del chat, selecciona la ubicación de ejecución actual y luego el
   host de destino. Selecciona **Esta computadora** cuando transfieras un chat remoto de vuelta
   a tu computadora local.
3. Revisa el destino y la rama, y luego selecciona **Transferir**.

Codex crea o reutiliza un worktree en el host de destino, transfiere el
chat y el estado de Git, y pasa el chat a ese host. Si el chat está
en ejecución, la transferencia interrumpe la respuesta actual antes de transferirlo.

También puedes pedirle a Codex desde otro chat que transfiera a un
host conectado un chat que indiques por su nombre. Codex no puede transferir el chat desde el que se hace la solicitud y no se admite la transferencia
a un entorno de Codex Cloud.

## Autenticación y exposición a la red

Las conexiones remotas usan SSH para iniciar y administrar el App Server remoto de Codex.
No expongas los transportes del App Server directamente en una red compartida o pública.

Si necesitas acceder a una máquina remota fuera de tu red actual, usa una VPN
o una herramienta de red en malla en lugar de exponer el App Server directamente
a internet.

## Solución de problemas

### El host no aparece en tu teléfono

Confirma que la app de escritorio se esté ejecutando en el host, que hayas habilitado **Permitir
que otros dispositivos se conecten** y que ambos dispositivos usen la misma cuenta de ChatGPT y
el mismo espacio de trabajo. Si no has usado la conexión desde el 8 de junio de 2026, actualiza ambas
aplicaciones y vuelve a vincular los dispositivos.

### El control remoto está desactivado después de volver a iniciar sesión

Al cerrar sesión en ChatGPT, se desactiva **Control remoto**, pero no se eliminan las
vinculaciones existentes entre tus dispositivos. Cuando vuelvas a iniciar sesión, activa **Control remoto** para
restablecer el estado anterior de la conexión.

Si ves un error después de activar **Control remoto** y seleccionar **Agregar**,
reinicia la aplicación de escritorio de ChatGPT en el host y vuelve a intentarlo.

### La solicitud de aprobación no aparece

En la app móvil de ChatGPT, abre **Remoto**. Confirma que el teléfono y el host usen
la misma cuenta de ChatGPT y el mismo espacio de trabajo; luego, vuelve a escanear el código QR o reinicia
la configuración desde el host. Si usas un espacio de trabajo de ChatGPT, pídele al administrador que confirme
que habilitó el acceso a Control remoto.

### La sesión remota se desconecta

Comprueba si el host entró en suspensión, perdió el acceso a la red o si se cerró la app.
Mantén el host activo y conectado mientras ChatGPT trabaja.

### La autenticación impide completar la configuración

Completa el prompt de autenticación de la cuenta o del espacio de trabajo que aparece durante la configuración. Si
tu organización requiere SSO, autenticación multifactor o una clave de acceso,
completa ese proceso antes de volver a intentarlo. Si la configuración sigue fallando, pídele al
administrador de tu espacio de trabajo que confirme que habilitó el acceso a Control remoto.

## Consulta también

- [Aplicación de escritorio de ChatGPT](/es-419/codex/app)
- [Funciones](/es-419/codex/features)
- [Configuración de la aplicación de escritorio de ChatGPT](/codex/reference/settings)
- [Uso de la computadora](/es-419/codex/computer-use)
- [Extensión de Chrome](/es-419/codex/chrome-extension)
- [Opciones de línea de comandos](/codex/developer-commands?surface=cli)
- [Autenticación](/es-419/codex/auth)
