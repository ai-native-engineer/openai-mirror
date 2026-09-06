<!-- source: https://learn.chatgpt.com/es-419/docs/computer-use -->

En las regiones compatibles, Uso de la computadora en la aplicación de escritorio de ChatGPT está disponible en
macOS y Windows con ChatGPT Work y Codex. Instala el complemento Uso de la
computadora. En macOS, otorga los permisos de Grabación de pantalla y Accesibilidad cuando
se te soliciten.

Con Uso de la computadora, ChatGPT puede ver y controlar interfaces gráficas de usuario en macOS
o Windows. Úsalo para tareas en las que las herramientas de línea de comandos o las integraciones estructuradas
no sean suficientes, como revisar una app de escritorio, usar un navegador, cambiar la
configuración de una app, trabajar con una fuente de datos que no esté disponible como complemento o
reproducir un error que solo ocurra en una interfaz gráfica de usuario.

Como Uso de la computadora puede afectar el estado de las apps y del sistema fuera del espacio de trabajo de tu
proyecto, úsalo para tareas de alcance limitado y revisa las solicitudes de permiso antes de
continuar.

## Configurar Uso de la computadora

En la aplicación de escritorio de ChatGPT, selecciona ChatGPT y cambia a Work en el selector, o selecciona
Codex. Abre **Complementos \> Uso de la
computadora** y selecciona **Instalar complemento** si se te solicita. Si ChatGPT muestra **Activar**,
selecciónalo. Activa los interruptores del servidor y de la habilidad de Uso de la computadora y, luego, selecciona **Probar
ahora** para comenzar.

  

Luego, abre **Configuración \> Uso de la computadora** para revisar el acceso a las apps. Los controles del navegador conectado
muestran la acción **Administrar** . Las apps que apruebes para tareas futuras aparecen en
la sección **Apps siempre permitidas** .

  

En Windows, mantén la app de destino visible en el escritorio activo mientras se ejecuta la
tarea. En macOS, otorga los permisos de Grabación de pantalla y Accesibilidad cuando
se te soliciten para que ChatGPT pueda ver la app de destino e interactuar con ella.

En macOS, otorga:

- el permiso de **Grabación de pantalla** para que ChatGPT pueda ver la app de destino.
- el permiso de **Accesibilidad** para que ChatGPT pueda hacer clic, escribir y navegar.

## Cuándo usar Uso de la computadora

Para tareas difíciles que dependan de capturas de pantalla o del criterio visual, elige
[GPT-6 Astra](/es-419/codex/models#gpt-6-astra) cuando esté disponible en tu selector de
modelos. Se aplican la misma configuración del complemento, los mismos permisos del sistema operativo y los mismos controles
de acceso a las apps.

Elige Uso de la computadora cuando la tarea dependa de una interfaz gráfica de usuario que sea
difícil de verificar solo mediante archivos o la salida de comandos.

Es una buena opción para:

- probar una app de macOS, una app de Windows, un flujo en el simulador de iOS u otra app de escritorio
que ChatGPT esté creando.
- realizar una tarea que requiera tu navegador web.
- reproducir un error que solo aparezca en una interfaz gráfica.
- cambiar la configuración de una app cuando sea necesario navegar por una interfaz mediante clics.
- inspeccionar información en una app o fuente de datos que no esté disponible mediante un
complemento.
- en macOS, ejecutar una tarea de alcance limitado en segundo plano mientras sigues trabajando
en otras cosas.
- ejecutar un flujo de trabajo que abarque más de una app.

Para las apps web que desarrolles localmente, usa primero el
[navegador integrado](/es-419/codex/browser?surface=app).

### Uso en primer plano en Windows

En Windows, Uso de la computadora funciona en el escritorio activo. No puede ejecutarse en
segundo plano mientras sigues usando la misma sesión de Windows, así que ten en cuenta que ChatGPT
moverá el puntero, escribirá y tomará el control de la interacción en primer plano mientras se ejecuta la tarea.

Para las tareas de Windows que deban continuar mientras estás ausente, mantén el dispositivo con Windows
desbloqueado y conectado a internet. Usa el
[control remoto](/es-419/codex/remote-connections) desde tu teléfono para revisar el progreso
o enviar instrucciones de seguimiento, o ejecuta la aplicación de escritorio de ChatGPT en una máquina virtual de Windows
para que Uso de la computadora tome el control de la VM en lugar de tu escritorio principal.

## Iniciar una tarea con Uso de la computadora

Menciona `@Computer` o `@AppName` en tu prompt, o pídele a ChatGPT que use Uso de la
computadora. Describe exactamente la app, la ventana o el flujo que ChatGPT debe controlar.

```text
Open the app with Computer Use, reproduce the onboarding bug, and fix the
smallest code path that causes it. After each change, run the same UI flow
again.

```text
Open @Chrome and verify the checkout page still works after the latest changes.

Si la app de destino ofrece un complemento o servidor MCP específico, da preferencia a esa
integración estructurada para acceder a los datos y realizar operaciones repetibles. Elige
Uso de la computadora cuando ChatGPT necesite inspeccionar o controlar visualmente la app.

## Permisos y aprobaciones

Los administradores del espacio de trabajo pueden restringir a qué apps puede acceder Uso de la computadora y
si se pueden guardar las aprobaciones. Consulta los
[controles administrados del navegador y de Uso de la computadora](/es-419/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Los permisos del sistema para Uso de la computadora son independientes de las aprobaciones de apps en ChatGPT.
En macOS, los permisos de Grabación de pantalla y Accesibilidad permiten que ChatGPT vea y
controle las apps. Las aprobaciones de apps determinan qué apps permites que use ChatGPT. La
lectura y edición de archivos, así como los comandos de shell, siguen sujetos a la configuración de sandbox y aprobación
de la tarea.

Con Uso de la computadora, ChatGPT solo puede ver las apps que permites y realizar acciones en ellas.
Durante una tarea, ChatGPT te pide permiso antes de poder usar una app de tu
computadora. Puedes elegir **Permitir siempre** para que ChatGPT pueda usar esa app en el futuro
sin volver a preguntar. Puedes quitar apps de la lista **Permitir siempre** en la sección
**Uso de la computadora** de la configuración de la aplicación de escritorio de ChatGPT.

  
    
  

ChatGPT también puede pedir permiso antes de realizar acciones sensibles o que puedan causar interrupciones.

Si ChatGPT no puede ver o controlar una app, abre **Configuración del Sistema \> Privacidad y
seguridad** y revisa los permisos de **Grabación de pantalla** y **Accesibilidad** para **Uso de la computadora de
Codex** en macOS. En Windows, asegúrate de que la app de destino esté visible en la
sesión de escritorio activa.

En Windows, Uso de la computadora almacena las decisiones persistentes sobre apps en
`$CODEX_HOME/config.toml`. Enumera las apps que Uso de la computadora puede abrir sin
solicitar permiso:

```toml
[computer_use.windows]
always_allowed_app_ids = ["mspaint.exe"]

Usa el identificador de app que indica Uso de la computadora en Windows, como el nombre de un ejecutable
para una app de escritorio o un ID de modelo de usuario de aplicación para una app empaquetada. ChatGPT
solicita permiso para usar las apps que no estén en la lista. Para revocar una decisión guardada, quita
la app de **Configuración \> Uso de la computadora \> Permitir siempre**.

Esta tabla almacena las decisiones locales de Uso de la computadora. Es independiente del archivo
`requirements.toml` que aplican los administradores, donde pueden desactivar Uso de la
computadora con `[features].computer_use = false`. Las entradas antiguas de la lista de apps permitidas de
`$CODEX_HOME/computer-use/config.toml` se migran a la
configuración actual; su lista `denied` no forma parte del esquema de políticas actual.

## Uso con la pantalla bloqueada

  El uso con la pantalla bloqueada es para macOS. En Windows, Uso de la computadora funciona en primer plano.

El uso con la pantalla bloqueada permite que ChatGPT utilice Uso de la computadora después de que tu Mac se bloquee, pero solo después de
que lo actives. Úsalo cuando una tarea de ChatGPT necesite usar apps de escritorio desde un
dispositivo conectado después de que la Mac se bloquee.

Cuando activas el uso con la pantalla bloqueada, ChatGPT instala un
[complemento de autorización](https://developer.apple.com/documentation/security/authorization-plug-ins) de Apple
que participa en el flujo de desbloqueo de macOS.

El uso con la pantalla bloqueada tiene un alcance limitado por diseño. No es un mecanismo de uso general para desbloquear
tu Mac de forma remota y no permite que otras apps ni procesos locales desbloqueen la
computadora.

Para usar la función con la pantalla bloqueada:

1. en la app, abre **Configuración \> Uso de la computadora** .
2. activa el uso con la pantalla bloqueada.
3. inicia una tarea que use Uso de la computadora desde un dispositivo conectado después de que la pantalla de tu Mac
se haya bloqueado.

Cuando una tarea de ChatGPT accede a una app mediante Uso de la computadora después de que tu Mac se bloquea, ChatGPT
desbloquea temporalmente la Mac mientras impide el uso local y mantiene las protecciones de la pantalla
bloqueada. Antes de desbloquearla, ChatGPT comprueba si el intento de desbloqueo corresponde
a un turno activo y de confianza de Uso de la computadora. Fuera de ese breve período, ChatGPT
rechaza el desbloqueo y te pide que lo hagas manualmente si es necesario.

El uso con la pantalla bloqueada incluye medidas de protección:

- el período de autorización es breve y se limita al intento de desbloqueo
actual.
- el desbloqueo automático solo está disponible para ChatGPT durante los turnos activos de Uso de la computadora.
- ChatGPT cubre todas las pantallas mientras el escritorio está desbloqueado temporalmente.
- si ChatGPT detecta una entrada local del teclado o del puntero, vuelve a bloquear la Mac y
pausa el desbloqueo automático hasta que la desbloquees manualmente.

## Recomendaciones de seguridad

Con Uso de la computadora, ChatGPT puede ver el contenido de la pantalla, tomar capturas de pantalla e interactuar
con las ventanas, los menús, la entrada del teclado y el estado del portapapeles en la app de destino.
Considera el contenido visible de la app, las páginas del navegador, las capturas de pantalla y los archivos abiertos en la
app de destino como contexto que ChatGPT puede procesar mientras se ejecuta la tarea.

Limita el alcance de las tareas y mantente presente durante los flujos sensibles:

- Indícale a ChatGPT una app o un flujo concreto a la vez.
- Puedes detener la tarea o retomar el control de tu computadora en cualquier momento.
- Mantén cerradas las apps sensibles, a menos que sean necesarias para la tarea.
- En Windows, ten en cuenta que ChatGPT tomará el control de la interacción en primer plano mientras trabaja; usa un
dispositivo secundario o una VM, o detén la tarea antes de usar ese escritorio tú mismo.
- Evita las tareas que requieran secretos a menos que estés presente y puedas aprobar cada
paso.
- Revisa las solicitudes de permisos de las apps antes de permitir que ChatGPT use una app.
- Usa **Permitir siempre** solo para apps cuyo uso automático por parte de ChatGPT consideres seguro en
  tareas futuras.
- Mantente presente cuando se modifiquen ajustes relacionados con la cuenta, la seguridad, la privacidad, la red, los pagos o las
credenciales.
- Cancela la tarea si ChatGPT empieza a interactuar con la ventana equivocada.

Si ChatGPT usa tu navegador, puede interactuar con páginas en las que ya
iniciaste sesión. Revisa las acciones en los sitios web como si las realizaras tú mismo: las páginas web
pueden contener contenido malicioso o engañoso, y los sitios pueden considerar que los clics aprobados,
los envíos de formularios y las acciones realizadas con la sesión iniciada provienen de tu cuenta. Para seguir
usando tu navegador mientras ChatGPT trabaja, pídele a ChatGPT que use otro navegador.

La función no puede automatizar apps de terminal ni el propio ChatGPT, ya que hacerlo
podría eludir las políticas de seguridad de ChatGPT. Tampoco puede autenticarse como
administrador ni aprobar solicitudes de permisos de seguridad y privacidad en tu
computadora.

Los cambios en archivos y los comandos de shell siguen sujetos a la configuración de aprobación y de sandbox de ChatGPT
cuando corresponda. Es posible que los cambios realizados mediante apps de escritorio no aparezcan en el panel de revisión
hasta que se guarden en el disco y queden bajo seguimiento del proyecto. Tus controles de datos de ChatGPT
se aplican al contenido procesado mediante ChatGPT, incluidas las capturas de pantalla tomadas
con Uso de la computadora.
