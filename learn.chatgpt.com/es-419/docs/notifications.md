<!-- source: https://learn.chatgpt.com/es-419/docs/notifications -->

Las notificaciones te avisan cuando una tarea requiere tu atención. Sus controles y
canales de entrega varían según la interfaz.

## Configurar las notificaciones de escritorio

Abre [**Configuración**](codex://settings) para elegir si las alertas de finalización de turno
no aparecen nunca, solo cuando ChatGPT está en segundo plano o siempre. Hay controles
independientes para activar o desactivar las notificaciones de solicitudes de permiso y de preguntas. Tu
sistema operativo puede pedirte que otorgues permiso a la app de escritorio de ChatGPT
para enviar notificaciones.

### Seguir los chats en la vista Actividad

Cuando **Actividad** esté disponible, selecciona el ícono de campana en la barra lateral para ver los chats
que no has leído, que están en ejecución o que esperan tu respuesta. También puedes abrir o
cerrar la vista Actividad con <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>U</kbd> en macOS
o <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>U</kbd> en Windows.

Usa las opciones de la vista para elegir qué chats se muestran. Según la
interfaz que estés usando, las opciones pueden incluir **Work**, **Chat**, **Fijados** y
**Programados**. También puedes seleccionar **Marcar todo como leído** para quitar todos los elementos de la lista de no leídos.

<a id="follow-task-activity-with-a-pet"></a>

### Seguir la actividad del chat con una mascota

En la app de escritorio de ChatGPT, una mascota flotante es otra forma de seguir la
actividad del chat mientras trabajas en otras apps. Puede indicar estos estados de un chat: **En ejecución**,
**Necesita información**, **Listo** o **Bloqueado**.

Consulta [Mascotas](/es-419/codex/pets?surface=app) para elegir una mascota, entender su estado o
crear la tuya.

## Configurar las notificaciones web

Abre **Configuración \> Notificaciones** para administrar las categorías y los
canales de notificación disponibles para tu cuenta. Según la categoría y la cuenta,
los canales pueden incluir notificaciones push, correo electrónico o SMS. Usa **Administrar tareas** en la configuración de
notificaciones de tareas para abrir **Programadas**.

## Configurar las notificaciones de la CLI

Para las notificaciones del terminal y las externas, consulta
[Notificaciones](/es-419/codex/config-file/config-advanced#notifications) en la
guía de configuración avanzada. Puedes elegir cuándo la TUI emite una notificación
y si Codex ejecuta un programa externo cuando finaliza un turno.

<a id="follow-task-activity-in-the-ide"></a>

## Seguir la actividad del chat en el IDE

La extensión para IDE no ofrece controles de notificaciones independientes. Mantén el
chat abierto para seguir su actividad. Para ejecutar un programa externo cuando
finalice un turno, configura `notify` en el host de Codex conectado. Consulta
[Notificaciones](/es-419/codex/config-file/config-advanced#notifications) en la
guía de configuración avanzada.

## Documentación relacionada

- [Trabajo de larga duración](/es-419/codex/long-running-work)
- [Tareas programadas](/es-419/codex/automations)
- [Mascotas](/es-419/codex/pets)
