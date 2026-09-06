<!-- source: https://learn.chatgpt.com/es-419/docs/features/codex-micro -->

<div class="grid gap-6 lg:grid-cols-2 lg:items-start lg:gap-10">
  <div class="min-w-0 [&_p]:!mt-0">

Codex Micro es una colaboración de edición limitada entre Codex y Work Louder.
Funciona con la app de escritorio de ChatGPT y te permite consultar rápidamente los chats,
cambiar de uno a otro, usar la entrada de voz y activar acciones o habilidades comunes sin
separarte del teclado.

  </div>
  <div class="min-w-0">
    
      
    
  </div>
</div>

## Configurar Codex Micro

1. Abre la app de escritorio de ChatGPT.
2. Presiona una vez el botón trasero para encender Codex Micro.
3. Conéctalo con un cable USB-C o [emparéjalo mediante Bluetooth](#pair-with-bluetooth);
   luego, sigue la configuración que aparece cuando ChatGPT lo detecta.
4. En macOS, cuando se te solicite, permite **Monitoreo de entrada** para que ChatGPT pueda responder a
   las pulsaciones de teclas.
5. Abre **Configuración \> Codex Micro** para elegir qué chats siguen las teclas de agente o
   qué acciones activan, personalizar las teclas de comando, la palanca analógica y la perilla, y ajustar
   la iluminación y los controles de voz.

De forma predeterminada, mantén presionada la perilla un momento para abrir esta configuración. También
puedes seleccionar el ícono de Micro junto al nombre de tu cuenta en la parte inferior de ChatGPT.
Una asignación personalizada de la perilla puede reemplazar el atajo de mantenerla presionada.

La configuración del dispositivo sigue disponible después de que ChatGPT detecta un Micro compatible por
primera vez. Work Louder Input no es necesario para la integración con ChatGPT.
Úsalo para personalizar los controles de otras apps o configurar más capas.

## Emparejar mediante Bluetooth

Codex Micro ofrece tres canales Bluetooth.

1. Presiona una vez el botón trasero para encender el Micro.
2. Mantén presionado durante tres segundos el control táctil del borde inferior izquierdo.
La iluminación debajo del Micro se vuelve azul cuando el modo Bluetooth está activo.
3. Toca el control táctil para elegir el canal Bluetooth 1, 2 o 3. Si la luz
del canal parpadea rápidamente, el Micro está listo para emparejarse.
4. Abre la configuración de Bluetooth de tu computadora y conecta el Micro cuando
aparezca.
5. Espera a que la luz del canal quede fija; eso indica que el emparejamiento se completó.

El selector de conexión se cierra tras cinco segundos sin interacción. Para cambiar a
otro canal emparejado, abre de nuevo el selector, elige el canal y espera
a que se cierre. Para volver a emparejar ese canal, mantén presionado el control táctil
durante tres segundos hasta que su luz comience a parpadear.

Para usar USB-C en su lugar, abre el selector de conexión y toca el control táctil
hasta que la iluminación debajo del Micro se vuelva blanca. Si conectas un cable USB-C mientras
el Micro sigue en modo Bluetooth, se cargará, pero no cambiará a la conexión
por cable.

Para ver los diagramas de hardware, consulta la [guía de configuración de Codex Micro
de Work Louder](https://worklouder.cc/openai-micro-setup).

<a id="read-and-switch-tasks-with-agent-keys"></a>

## Leer chats y cambiar entre ellos con las teclas de agente

Cada una de las seis teclas de agente esmeriladas puede seguir un chat e iluminarse para indicar su
estado actual. Presiona una tecla de agente una vez para cambiar a ese chat sin llevar
ChatGPT al primer plano. Presiónala dos veces en un intervalo de 350 milisegundos para cambiar de chat y
traer la ventana de ChatGPT al frente. Para traer ChatGPT al frente con la primera pulsación, activa
**Traer ChatGPT al frente con un solo toque** en la configuración del dispositivo.

| Luz | Estado           | Significado                                   |
| ----- | ---------------- | ----------------------------------------- |
| Blanca | Inactivo             | El chat está inactivo.                         |
| Azul  | Pensando         | ChatGPT está trabajando.                       |
| Verde | Completado         | El chat finalizó con una actualización sin leer. |
| Ámbar | Requiere intervención   | ChatGPT necesita tu aprobación o respuesta.  |
| Roja   | Error            | Algo salió mal.                     |
| Apagada   | Sin chat asignado | La tecla no sigue ningún chat.            |

La luz de estado de la tecla del chat seleccionado emite pulsos.

De forma predeterminada, las teclas siguen tus seis chats actualizados más recientemente, estén
fijados o no. Cambia **Teclas de agente** en la configuración del dispositivo para usar una
disposición diferente:

- **Chats más recientes**: sigue los seis chats actualizados más recientemente, estén fijados o
  no.
- **Chats fijados**: sigue los primeros seis chats de **Fijados**.
- **Chats prioritarios**: coloca primero los chats que esperan tu intervención, los chats no leídos y los chats
  activos.
- **Asignaciones personalizadas**: asigna a cada tecla de agente un chat, un atajo, la acción de una tecla física o una
  habilidad activada. Presiona una tecla de agente sin asignar para abrir un chat nuevo.
  Cuando inicies el chat, ChatGPT lo asignará a esa tecla.

Los colores de estado no cambian para las teclas que siguen chats. Con **Asignaciones
personalizadas**, una tecla de agente puede activar una acción en su lugar.

## Usar y personalizar las teclas de comando

Codex Micro incluye seis acciones en su disposición predeterminada:

<div class="grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-start">
  <div class="min-w-0 [&_table]:!mt-0 [&_td:first-child]:!px-2 [&_th:first-child]:!px-2 md:order-2">

|                            Tecla                            | Acción predeterminada                           |
| :-------------------------------------------------------: | ---------------------------------------- |
|     | Activa o desactiva el modo rápido.                |
|  | Aprueba la solicitud actual.             |
|   | Rechaza la solicitud actual.             |
|    | Continúa el chat actual en uno nuevo. |
|       | Inicia la función Pulsar para hablar.                      |
|   | Envía el mensaje del Editor.        |

  </div>
  <div class="min-w-0 md:order-1">

La tecla Micrófono usa el micrófono de tu computadora. Codex Micro no tiene
micrófono propio. De forma predeterminada, usa **Pulsar para hablar**: mantén presionada la tecla mientras
hablas y suéltala para detener la grabación. Para grabar sin usar las manos, presiónala dos veces
en un intervalo de 350 milisegundos para seguir grabando. Presiónala de nuevo para detener la grabación.

Una luz verde agua recorre el teclado mientras grabas. Se convierte en una
luz blanca en movimiento mientras ChatGPT procesa tu voz y luego queda fija en blanco
cuando el prompt está listo. Presiona la tecla Codex para enviarlo.

Si **Chat de voz** está disponible en **Tecla de micrófono**, selecciónalo para usar la
tecla Micrófono para iniciar un chat de voz o activar o desactivar tu micrófono; mantenla presionada para
finalizar el chat. Activa **Usar teclas de micrófono separadas** para asignar de forma independiente los dos interruptores
debajo de la tecla Micrófono ancha.

En la configuración del dispositivo, selecciona una tecla de comando en la vista previa de **Diseño** y luego
elige su tapa y su acción. Puedes abrir el navegador o la Terminal, administrar
chats, revisar cambios, ejecutar acciones de Git y Pull Request, adjuntar archivos o fotos,
abrir Complementos o Tareas programadas, cambiar el nivel de esfuerzo de razonamiento, ejecutar una habilidad habilitada
o asignar otro atajo. Si eliges una tapa de tecla que ya se usa
en otra parte, ChatGPT intercambia ambas tapas en lugar de usar una dos veces.

Después de reasignar una tecla, cambia su tapa física para que coincida con la nueva acción.
Selecciona **Restablecer diseño** para restaurar las asignaciones predeterminadas de las teclas de comando y de la palanca analógica
sin cambiar el modo de las teclas de agente ni las asignaciones personalizadas de chats.

  </div>
</div>

## Usar la palanca analógica y el dial

<div class="grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-start">
  <div class="min-w-0">

La palanca analógica se mueve libremente en cualquier dirección. Cuando la alejas lo suficiente
del centro, ChatGPT convierte el movimiento en una de cuatro acciones
direccionales. Codex Micro usa inicialmente las asignaciones que se muestran aquí.

En la configuración del dispositivo, elige cualquier comando disponible de la app de escritorio de ChatGPT o habilidad habilitada para cada
dirección.

  </div>
  <div class="min-w-0 [&_table]:!mt-0">

| Dirección | Acción predeterminada             |
| --------- | -------------------------- |
| Arriba        | Activa o desactiva el Modo plan.  |
| Derecha     | Avanza en el historial de la app. |
| Abajo      | Muestra u oculta la barra lateral.  |
| Izquierda      | Retrocede en el historial de la app.    |

  </div>
</div>

De forma predeterminada, el dial usa **Navegación del Editor**. Gíralo para recorrer los
controles y las opciones del Editor; luego, presiónalo para abrir o seleccionar el
control que tiene el foco. Cuando está abierto un control o menú del Editor, la tecla de agente ubicada justo a
la derecha del dial se ilumina en rojo. Presiona esa tecla para cancelar.

En la configuración del dispositivo, elige uno de los cuatro modos del dial:

| Modo                       | Comportamiento                                                                       |
| -------------------------- | ------------------------------------------------------------------------------ |
| **Navegación del Editor**    | Recorre los controles del Editor y selecciona el control que tiene el foco.                 |
| **Solo razonamiento**         | Ajusta el nivel de esfuerzo de razonamiento y abre el control deslizante correspondiente o las opciones avanzadas.               |
| **Desplazamiento por la conversación** | Desplázate por el chat activo; presiona el dial para ir al mensaje más reciente.          |
| **Asignaciones personalizadas**     | Asigna una acción o habilidad al giro a la izquierda, al giro a la derecha, a la pulsación y a la pulsación prolongada. |

Mantener presionado el dial abre la configuración del dispositivo en todos los modos, excepto
**Asignaciones personalizadas**, donde ejecuta la acción asignada a la pulsación prolongada.

## Ajustar la iluminación

{/* vale Microsoft.Auto = NO */}

En la configuración del dispositivo, ajusta el **Brillo** y elige un intervalo de **Atenuación automática**
de entre 30 segundos y una hora, o desactiva la atenuación automática. Las luces
vuelven a encenderse cuando usas el Micro o cuando cambia el estado de una tecla de agente. De forma predeterminada,
las luces se apagan después de tres minutos.

{/* vale Microsoft.Auto = YES */}

Cuando el Micro informa el estado de la batería, puedes verlo en la configuración del dispositivo
y junto al ícono de Micro en la barra lateral.

## Agregar más capas

ChatGPT usa la capa 1. Usa [Work Louder
Input](https://worklouder.cc/micro-setup) para configurar hasta cinco capas más
con atajos y acciones para otras apps.

## Solucionar problemas de Codex Micro

### Solucionar problemas de Monitoreo de entrada en macOS

Si la configuración del dispositivo indica que Monitoreo de entrada no está configurado, selecciona **Abrir
Configuración del Sistema** y sigue estos pasos:

1. Abre **Configuración del Sistema \> Privacidad y seguridad \> Monitoreo de entrada**.
2. Activa el acceso para ChatGPT si ya aparece en la lista. Si no aparece, arrastra
**ChatGPT** desde Aplicaciones hasta la lista, o selecciona **Agregar (+)** y elige
**ChatGPT**.
3. Sal de ChatGPT y vuelve a abrirlo; luego, confirma que ChatGPT detecte el Micro en la capa 1.

Para obtener más información sobre este permiso de macOS, consulta la [guía de Monitoreo de entrada
de Apple](https://support.apple.com/guide/mac-help/mchl4cedafb6/mac).

### Solucionar interferencias en la conexión

ChatGPT reintenta la conexión automáticamente cuando detecta un Micro, pero no puede conectarse o pierde la
comunicación. Si el problema continúa, vuelve a conectar el Micro y verifica si
una utilidad de teclado o una herramienta de seguridad bloquea el acceso al Micro.

{/* vale Vale.Spelling = NO */}

En macOS, Work Louder señala que Karabiner y Logitech Options+ pueden interferir
en la comunicación con el Micro cuando esas apps tienen permiso de Monitoreo de entrada. Para
comprobar si hay interferencias, sal de la utilidad de teclado o desactiva temporalmente su
acceso a Monitoreo de entrada; luego, vuelve a conectar el Micro. Si tu organización administra
tu computadora, pide al administrador de TI que revise las reglas del dispositivo.

{/* vale Vale.Spelling = YES */}

### Obtener más ayuda de Work Louder

Para obtener ayuda con Bluetooth, cables, alimentación o el restablecimiento del teclado, consulta la [guía de configuración de Work
Louder Codex Micro](https://worklouder.cc/openai-micro-setup). Para recibir
asistencia directa, escribe a
[hello@worklouder.cc](mailto:hello@worklouder.cc).

## Obtener un Micro compatible

Consulta la disponibilidad de Codex Micro en [OpenAI Supply
Co](https://openai.com/supply/co-lab/work-louder/). La app de escritorio de ChatGPT también
es compatible con [Creator Micro 2](https://worklouder.cc/creator-micro-2), disponible
directamente en Work Louder.
