<!-- source: https://learn.chatgpt.com/es-419/docs/windows/windows-sandbox -->

Usa Codex en Windows con la versión nativa de la [aplicación de escritorio de ChatGPT](/es-419/codex/windows/windows-app), la
[CLI](/es-419/codex/cli) o la [extensión para IDE](/es-419/codex/ide).

La aplicación de escritorio de ChatGPT para Windows admite flujos de trabajo esenciales, como chats paralelos,
worktrees, tareas programadas, funciones de Git, el navegador integrado, vistas previas de archivos,
complementos y habilidades.

La aplicación puede ejecutarse de forma nativa en PowerShell con un sandbox de Windows, sin
necesidad de WSL ni de una máquina virtual. Así, Codex conserva los flujos de trabajo nativos de
Windows mientras aplica permisos limitados para el sistema de archivos y la red.

  
    
  

<div class="mb-8">
  
</div>

El sandbox nativo de Windows tiene dos modos:

- de forma nativa en Windows con el sandbox reforzado `elevated`,
- de forma nativa en Windows con el sandbox de respaldo `unelevated`.

<span id="windows-sandbox"></span>

## Configurar el sandbox de Windows

Cuando ejecutas Codex de forma nativa en Windows, el modo de agente usa un sandbox de Windows para
bloquear la escritura en el sistema de archivos fuera de la carpeta de trabajo e impedir el acceso a la red
sin tu aprobación explícita.

La compatibilidad con el sandbox nativo de Windows incluye dos modos que puedes configurar en
`config.toml`:

```toml
[windows]
sandbox = "elevated" # or "unelevated"

`elevated` es el sandbox nativo de Windows recomendado. Usa usuarios dedicados del sandbox
con privilegios reducidos, límites de permisos del sistema de archivos, reglas de
firewall y los cambios necesarios en las políticas locales para ejecutar comandos en el sandbox.

`unelevated` es el sandbox nativo de Windows de respaldo. Ejecuta comandos con un
token restringido de Windows derivado de tu usuario actual, aplica límites del
sistema de archivos basados en ACL y usa controles sin conexión a nivel del entorno en lugar de
la regla de firewall dedicada al usuario sin conexión. Ofrece menos protección que `elevated`, pero
sigue siendo útil cuando una política local o
empresarial bloquea la configuración aprobada por el administrador.

Si ambos modos están disponibles, usa `elevated`. Si el sandbox nativo predeterminado
no funciona en tu entorno, usa `unelevated` como opción de respaldo mientras
solucionas los problemas de configuración.

Los administradores empresariales pueden restringir las implementaciones de sandbox nativo
que puede usar Codex mediante [`requirements.toml`](/es-419/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml):

```toml
[windows]
allowed_sandbox_implementations = ["elevated"]

Este ejemplo exige el sandbox `elevated` e impide que los usuarios recurran
a `unelevated`. Para permitir cualquiera de las dos implementaciones, incluye ambos valores;
Codex prefiere `elevated` cuando no se selecciona ningún modo. Consulta la
[referencia de `requirements.toml`](/es-419/codex/config-file/config-reference#requirementstoml) para conocer
los valores admitidos.

De forma predeterminada, ambos modos de sandbox también usan un escritorio privado para reforzar el
aislamiento de la interfaz de usuario. Establece `windows.sandbox_private_desktop = false` solo si necesitas el
comportamiento anterior de `Winsta0\\Default` por motivos de compatibilidad.

### Permisos del sandbox

  Ejecutar Codex en modo de acceso completo significa que Codex no se limita al directorio de tu proyecto
  y podría realizar acciones destructivas involuntarias que provoquen
  pérdida de datos. Para una automatización más segura, mantén los límites del sandbox y usa
[reglas](/es-419/codex/agent-configuration/rules) para excepciones específicas, o configura tu
[política de aprobación en
  nunca](/es-419/codex/agent-approvals-security#run-without-approval-prompts) para que
  Codex intente resolver problemas sin solicitar permisos elevados,
  según tu [configuración de aprobación y seguridad](/es-419/codex/agent-approvals-security).

### Matriz de versiones de Windows

| Versión de Windows                  | Nivel de compatibilidad   | Notas                                                                                                                                                                                 |
| -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows 11                       | Recomendado     | La mejor base para usar Codex en Windows. Úsala si estás estandarizando una implementación empresarial.                                                                                       |
| Windows 10 reciente y completamente actualizado | Compatibilidad limitada     | Puede funcionar, pero es menos confiable que Windows 11. En Windows 10, Codex depende de la compatibilidad con consolas modernas, incluido ConPTY. En la práctica, se requiere Windows 10 versión 1809 o posterior. |
| Compilaciones anteriores de Windows 10          | No recomendado | Es más probable que carezcan de componentes de consola necesarios, como ConPTY, y que presenten fallas en configuraciones empresariales.                                                                          |

Además, se presupone lo siguiente sobre el entorno:

- `winget` debe estar disponible. Si no lo está, actualiza Windows o instala
  el Administrador de paquetes de Windows antes de configurar Codex.
- El sandbox nativo recomendado depende de una configuración aprobada por el administrador.
- Algunos dispositivos administrados por empresas bloquean los pasos de configuración necesarios aunque la
versión del sistema operativo sea adecuada.

### Conceder acceso de lectura al sandbox

Si un comando falla porque el sandbox de Windows no puede leer un directorio, usa:

```text
/sandbox-add-read-dir C:\absolute\directory\path

La ruta debe ser absoluta y apuntar a un directorio existente. Una vez que el comando se ejecute correctamente, los comandos posteriores que se ejecuten en el sandbox podrán leer ese directorio durante la sesión actual.

<span id="windows-subsystem-for-linux"></span>

Usa el sandbox nativo de Windows de forma predeterminada. Elige [WSL](/es-419/codex/windows/wsl)
cuando necesites herramientas nativas de Linux, tu flujo de trabajo ya se ejecute en WSL2 o
ninguno de los modos de sandbox nativo de Windows satisfaga tus necesidades.

## Solución de problemas y preguntas frecuentes

Si estás solucionando problemas en un equipo Windows administrado, empieza por revisar el modo de
sandbox nativo, la versión de Windows y cualquier error de política que muestre Codex. La mayoría de los problemas de compatibilidad nativa con
Windows se deben a la configuración del sandbox, los derechos de inicio de sesión o los permisos del sistema de archivos,
no al editor en sí.

Si Codex no puede completar la configuración del sandbox `elevated`, las causas más comunes
son:

- se rechazó el aviso de UAC de Windows o del administrador,
- el equipo no permite crear usuarios o grupos locales,
- el equipo no permite modificar las reglas del firewall,
- el equipo bloquea los derechos de inicio de sesión necesarios para los usuarios del sandbox,
- u otra política empresarial bloquea parte del proceso de configuración.

Qué puedes intentar:

1. Vuelve a intentar configurar el sandbox `elevated` y aprueba el aviso del administrador
   si tu entorno lo permite.
2. Si la laptop de tu empresa lo bloquea, pregunta a tu equipo de TI si el equipo
permite una configuración aprobada por el administrador para crear usuarios o grupos locales, configurar el
firewall y conceder a los usuarios del sandbox los derechos de inicio de sesión necesarios.
3. Si la configuración predeterminada sigue fallando, usa el sandbox `unelevated` para poder
   seguir trabajando mientras se investiga el problema.

Esto significa que Codex no pudo completar la configuración del sandbox reforzado `elevated` en tu
equipo.

- Codex aún puede ejecutarse dentro de un sandbox.
- Sigue aplicando límites del sistema de archivos basados en ACL, pero no usa el
  límite independiente basado en el usuario del sandbox que usa `elevated` y ofrece un aislamiento de red
  más débil.
- Es una opción de respaldo útil, pero no es la configuración empresarial recomendada
a largo plazo.

Si usas una laptop empresarial administrada, la mejor solución a largo plazo suele ser
lograr que el sandbox `elevated` funcione con ayuda de tu equipo de TI.

Si los comandos ejecutados en el sandbox fallan con el error `1385`, Windows deniega el tipo de inicio de sesión
que el usuario del sandbox necesita para iniciar el comando.

En la práctica, esto suele significar que Codex creó correctamente los usuarios del sandbox,
pero la política de Windows aún impide que esos usuarios ejecuten
comandos en el sandbox.

Qué hacer:

1. Consulta con tu equipo de TI si la política del dispositivo otorga los derechos de inicio de sesión necesarios
a los usuarios del sandbox creados por Codex.
2. Compara las directivas de grupo o las OU para identificar diferencias si el problema afecta solo a algunas
máquinas o equipos.
3. Si necesitas seguir trabajando de inmediato, usa el sandbox `unelevated` mientras
   se investiga el problema con la política.
4. Envía `CODEX_HOME/.sandbox/sandbox.log` junto con tu versión de Windows y una
   breve descripción de la falla.

Codex puede advertir que `Everyone` tiene permisos de escritura en algunas carpetas.

Si ves esta advertencia, los permisos de Windows en esas carpetas son demasiado amplios para
que el sandbox pueda protegerlas por completo.

Qué hacer:

1. Revisa las carpetas que Codex enumera en la advertencia.
2. Revoca el acceso de escritura de `Everyone` a esas carpetas si corresponde en
   tu entorno.
3. Reinicia Codex o vuelve a ejecutar la configuración del sandbox después de corregir
esos permisos.

Si no sabes cómo cambiar esos permisos, pide ayuda a tu equipo de TI.

Algunos chats de Codex se ejecutan intencionalmente sin acceso saliente a la red,
según el modo de permisos en uso.

Si una tarea falla porque no puede acceder a la red:

1. Verifica si la tarea debía ejecutarse con la red deshabilitada.
2. Si esperabas tener acceso a la red, reinicia Codex y vuelve a intentarlo.
3. Si el problema persiste, recopila el registro del sandbox para que el equipo pueda verificar
si el sandbox de la máquina está en un estado incompleto o defectuoso.

Esto puede ocurrir después de:

- mover un repositorio o un espacio de trabajo,
- cambiar los permisos de la máquina,
- cambiar las políticas de Windows,
- u otros cambios en la configuración del sistema.

Qué puedes intentar:

1. Reinicia Codex.
2. Vuelve a intentar configurar el sandbox `elevated`.
3. Si eso no resuelve el problema, usa el sandbox `unelevated` como alternativa
   temporal.
4. Recopila el registro del sandbox para revisarlo.

Si sigues teniendo problemas, envía:

- `CODEX_HOME/.sandbox/sandbox.log`

También es útil incluir:

- una breve descripción de lo que intentabas hacer,
- si falló el sandbox `elevated` o se usó el sandbox `unelevated`,
- cualquier mensaje de error que aparezca en la aplicación,
- si viste el error `1385` u otro error de Windows o PowerShell,
- y si usas Windows 11 o Windows 10.

No envíes:

- el contenido de `CODEX_HOME/.sandbox-secrets/`

Es posible que a tu sistema le falten las herramientas de desarrollo de C++ que requieren algunas dependencias nativas:

- Visual Studio Build Tools (carga de trabajo de C++)
- Microsoft Visual C++ Redistributable (x64)
- Con `winget`, ejecuta `winget install --id Microsoft.VisualStudio.2022.BuildTools -e`

Después de la instalación, reinicia VS Code por completo.
