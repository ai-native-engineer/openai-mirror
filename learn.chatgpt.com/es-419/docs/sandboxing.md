<!-- source: https://learn.chatgpt.com/es-419/docs/sandboxing -->

El sandbox es el límite que permite al agente actuar de forma autónoma sin darle
acceso sin restricciones a tu equipo. Cuando un chat local ejecuta comandos en la
**Aplicación de escritorio de ChatGPT**, en **Codex CLI** o en la **Extensión para IDE**, esos comandos se ejecutan en un
entorno restringido en lugar de ejecutarse con acceso completo de forma predeterminada.

Ese entorno determina qué puede hacer el agente por su cuenta, como qué archivos
puede modificar y si los comandos pueden usar la red. Cuando una tarea permanece dentro
de esos límites, el agente puede seguir avanzando sin detenerse para pedir confirmación. Cuando
necesita superarlos, entra en acción el flujo de aprobación.

  El entorno aislado y las aprobaciones son controles distintos que funcionan en conjunto. El
sandbox define los límites técnicos. La política de aprobación determina cuándo el
agente debe detenerse y solicitar aprobación antes de cruzarlos.

## Qué hace el sandbox

El sandbox se aplica a los comandos que se inician, no solo a las operaciones
integradas sobre archivos. Si el agente ejecuta herramientas como `git`, administradores de paquetes o ejecutores de pruebas,
esos comandos heredan los mismos límites del sandbox.

Codex aplica controles nativos de la plataforma en cada sistema operativo. La implementación varía
entre macOS, Linux, WSL2 y Windows nativo, pero la idea es la misma en todas las
interfaces: proporcionar al agente un espacio de trabajo delimitado para que las tareas habituales puedan ejecutarse
de forma autónoma dentro de límites claros.

## Por qué es importante

El sandbox reduce la fatiga por las aprobaciones. En lugar de pedirte que confirmes cada
comando de bajo riesgo, el agente puede leer archivos, hacer cambios y ejecutar comandos habituales del
proyecto dentro del límite que ya aprobaste.

También ofrece un modelo de confianza más claro para el trabajo con agentes. No solo
confías en las intenciones del agente, sino también en que opera
dentro de límites impuestos por el sistema. Esto facilita que el agente trabaje de forma independiente
y, al mismo tiempo, te permite saber cuándo se detendrá para pedir ayuda.

## Primeros pasos

El modo de permisos predeterminado aplica automáticamente el entorno aislado.

### Requisitos previos

En **macOS**, el entorno aislado funciona sin configuración adicional con el framework Seatbelt
integrado.

En **Windows**, Codex usa la implementación nativa del [sandbox de
Windows](/es-419/codex/windows/windows-sandbox#windows-sandbox) cuando se ejecuta en PowerShell y la
implementación del sandbox de Linux cuando se ejecuta en WSL2.

En **Linux y WSL2**, instala primero `bubblewrap` con tu administrador de paquetes:

  <div slot="ubuntu-debian">

```bash
sudo apt install bubblewrap

  </div>

  <div slot="fedora">

```bash
sudo dnf install bubblewrap

  </div>

Codex usa el primer ejecutable de `bwrap` que encuentra en `PATH`. Si no hay ningún ejecutable de `bwrap`
disponible, Codex recurre a una herramienta auxiliar incluida, pero esta
requiere compatibilidad con la creación de espacios de nombres de usuario sin privilegios. Instalar el
paquete de la distribución que proporciona `bwrap` hace que esta configuración sea confiable.

Codex muestra una advertencia al iniciar cuando falta `bwrap` o cuando la herramienta auxiliar
no puede crear el espacio de nombres de usuario necesario. En las distribuciones que restringen esta
configuración de AppArmor, opta por cargar el perfil de AppArmor de `bwrap` para que `bwrap`
siga funcionando sin desactivar la restricción de forma global.

  **Nota sobre AppArmor en Ubuntu:** en Ubuntu 25.04, instalar `bubblewrap` desde el
  repositorio de paquetes de Ubuntu debería funcionar sin configuración adicional de AppArmor. El
perfil `bwrap-userns-restrict` se incluye en el paquete `apparmor`, en la ruta
`/etc/apparmor.d/bwrap-userns-restrict`.

En Ubuntu 24.04, es posible que Codex siga advirtiendo que no puede crear el espacio de nombres de usuario
necesario después de instalar `bubblewrap`. Copia y carga el perfil adicional:

```bash
sudo apt update
sudo apt install apparmor-profiles apparmor-utils
sudo install -m 0644 \
  /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
  /etc/apparmor.d/bwrap-userns-restrict
sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict

`apparmor_parser -r` carga el perfil en el kernel sin necesidad de reiniciar. También
puedes volver a cargar todos los perfiles de AppArmor:

```bash
sudo systemctl reload apparmor.service

Si ese perfil no está disponible o no resuelve el problema, puedes desactivar
la restricción de AppArmor sobre los espacios de nombres de usuario sin privilegios con:

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

## Cómo funcionan los permisos

Usa el control de permisos de tu interfaz para cambiar cómo Codex gestiona las
acciones locales.

Las aprobaciones determinan cuándo Codex se detiene antes de una acción, mientras que el sandbox
determina a qué archivos y recursos de red pueden acceder los comandos. Cuando una
aprobación ofrece distintos alcances, como aprobarla una vez o durante la sesión,
elige el alcance más limitado que permita continuar la tarea. Mantén el límite del proyecto
como opción predeterminada; usa proyectos o worktrees independientes en vez de
ampliar el acceso a repositorios no relacionados.

ChatGPT Work ejecuta código y comandos de shell en un entorno administrado y aislado.
La política del espacio de trabajo y los controles específicos de cada herramienta determinan qué capacidades están
disponibles. Cuando la opción esté disponible, ve a **Configuración \> Controles de datos \> Acceso
a la red de Work** para administrar el acceso a la red del código y de los comandos de shell. Activa
**Permitir el acceso a la Internet pública** para que esos comandos puedan acceder a la Internet
pública. Cuando esta opción está desactivada, los comandos solo pueden acceder a los nombres de host necesarios incluidos en una
lista de permitidos administrada.

La búsqueda web, los complementos y el navegador remoto tienen controles independientes.
Los cambios entran en vigor cuando finaliza la ejecución actual de código o shell y Work
actualiza su entorno de ejecución. La versión web de ChatGPT no ofrece el sandbox local de
Codex ni el selector del modo de aprobación.

En la aplicación de escritorio de ChatGPT, usa el control de permisos debajo del editor.
Según tu configuración, el menú puede incluir **Solicitar aprobación**,
**Aprobar por mí** para las solicitudes de aprobación elegibles, **Acceso completo** y perfiles de permisos con nombre o
personalizados.

En la CLI, ingresa
[`/permissions`](/codex/developer-commands?surface=cli#cli-update-permissions-with-permissions)
para abrir el selector de permisos y cambiar el perfil de permisos activo.

En la extensión para IDE, usa el control de permisos debajo del editor.
Según tu configuración, el menú puede incluir **Solicitar aprobación**,
**Aprobar por mí** para las solicitudes de aprobación elegibles, **Acceso completo** y perfiles de permisos con nombre o
personalizados.

<div class="not-prose my-8 max-w-[18rem] mr-auto">
  
    
      
    
  
</div>

<a id="configure-defaults"></a>

## Configurar los valores predeterminados

Para comenzar siempre con el mismo comportamiento, establece los valores predeterminados en `config.toml`.
[Configuración básica](/es-419/codex/config-file/config-basic) explica cómo funciona y la
[Referencia de configuración](/es-419/codex/config-file/config-reference) documenta las claves exactas
`sandbox_mode`, `approval_policy`, `approvals_reviewer` y
`sandbox_workspace_write.writable_roots`. Usa estos ajustes para decidir cuánta
autonomía tiene el agente de forma predeterminada, en qué directorios puede escribir, cuándo
debe detenerse para solicitar aprobación y quién revisa las solicitudes de aprobación elegibles.

En términos generales, los modos de sandbox más comunes son:

- `read-only`: el agente puede inspeccionar archivos, pero no puede editarlos ni ejecutar
  comandos sin aprobación.
- `workspace-write`: el agente puede leer archivos, hacer cambios dentro del espacio de trabajo y ejecutar
  comandos locales habituales dentro de ese límite. Este es el modo predeterminado con menos
  interrupciones para el trabajo local.
- `danger-full-access`: el agente funciona sin restricciones del sandbox. Esto elimina
  los límites del sistema de archivos y de la red, y solo debe usarse cuando quieras
  que el agente actúe con acceso completo.

Las políticas de aprobación más comunes son:

- `untrusted`: el agente solicita aprobación antes de ejecutar comandos que no forman parte de su conjunto
  de confianza.
- `on-request`: el agente trabaja dentro del sandbox de forma predeterminada y solicita aprobación cuando
  necesita superar ese límite.
- `never`: el agente no se detiene para solicitar aprobación.

Cuando las aprobaciones son interactivas, también puedes elegir quién las revisa con
`approvals_reviewer`:

- `user`: las solicitudes de aprobación se muestran al usuario. Este es el valor predeterminado.
- `auto_review`: las solicitudes de aprobación elegibles se envían a un agente revisor (consulta la
[revisión automática](/es-419/codex/sandboxing/auto-review)).

El acceso completo implica usar `sandbox_mode = "danger-full-access"` junto con
`approval_policy = "never"`. En cambio, la configuración predefinida de automatización
local de menor riesgo usa `sandbox_mode = "workspace-write"` junto con
`approval_policy = "on-request"`, o los flags equivalentes de la CLI
`--sandbox workspace-write --ask-for-approval on-request`. Luego puedes mantener
`approvals_reviewer = "user"` para las aprobaciones manuales o establecer
`approvals_reviewer = "auto_review"` para la revisión automática de aprobaciones.

Si necesitas que el agente trabaje en más de un directorio, las raíces con permiso de escritura te permiten
ampliar las ubicaciones que puede modificar sin eliminar por completo el sandbox. Si
necesitas un límite de confianza más amplio o más restringido, ajusta el modo de sandbox predeterminado
y la política de aprobación en lugar de depender de excepciones puntuales.

Cuando un flujo de trabajo necesite una excepción específica, usa las [reglas](/es-419/codex/agent-configuration/rules). Las reglas
permiten autorizar prefijos de comandos fuera del sandbox, solicitar aprobación para ellos o prohibirlos, lo que
suele ser mejor que ampliar el acceso de forma general. Para saber dónde encontrar la configuración específica del IDE,
consulta [Configuración de la extensión de Codex para IDE](/codex/developer-settings?surface=ide).

La revisión automática, cuando está disponible, no cambia el límite del sandbox. Es
uno de los valores posibles de `approvals_reviewer` para las solicitudes de aprobación en ese límite, por ejemplo,
solicitudes para exceder el sandbox, accesos a la red bloqueados o llamadas a herramientas con efectos secundarios
que aún requieren aprobación. Las acciones que ya están permitidas dentro del sandbox se ejecutan
sin revisión adicional. Para obtener información sobre el ciclo de vida del revisor, los tipos de activadores, el comportamiento de las
denegaciones y los detalles de configuración, consulta la
[revisión automática](/es-419/codex/sandboxing/auto-review).

Los detalles de cada plataforma se encuentran en su documentación específica. Para conocer la configuración de Windows nativo,
su comportamiento y la solución de problemas, consulta [Windows](/es-419/codex/windows/windows-sandbox). Para conocer los requisitos para administradores
y las restricciones a nivel de organización sobre el entorno aislado y las aprobaciones, consulta
[Aprobaciones del agente y seguridad](/es-419/codex/agent-approvals-security).
