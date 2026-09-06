<!-- source: https://learn.chatgpt.com/es-419/docs/pets -->

Las mascotas son compañeros animados opcionales que te ayudan a seguir el trabajo. El lugar donde aparece
una mascota y lo que muestra dependen de la interfaz que uses. Elegir una mascota cambia su
apariencia, pero no la forma en que ChatGPT completa las tareas.

<div class="flow-root">
  <div class="w-full md:float-right md:ml-6 md:w-64 xl:w-72">
    
  </div>

## Usar una mascota flotante

En la app de escritorio de ChatGPT, una mascota puede flotar sobre las ventanas de otras apps y ayudarte
a seguir la actividad de tus chats.

### Elegir y despertar una mascota

1. Abre el menú del perfil en la parte inferior de la app y selecciona **Mascotas**. También puedes
   abrir [**Configuración**](codex://settings) e ir a **Mascotas**.
2. Elige una mascota integrada o personalizada.
3. Ingresa `/pet` o abre el menú de comandos y selecciona **Despertar mascota**.

Selecciona **Guardar mascota** en **Configuración \> Mascotas** o en el menú de comandos, o vuelve a ingresar
`/pet` para ocultarla. Tu selección y la posición de la mascota se conservan
cuando vuelves a abrir la app.

Cuando seleccionas una mascota personalizada, también aparece en la vista **Perfil**.

### Entender el estado de la mascota

| Estado          | Significado                                                  |
| --------------- | -------------------------------------------------------- |
| **En curso**     | Un chat está procesando una tarea.                              |
| **Requiere intervención** | Un chat necesita tu aprobación, respuesta u otra decisión. |
| **Listo**       | Un chat finalizó y tiene actividad sin leer.            |
| **Bloqueado**     | Un chat falló o se produjo un error del sistema.             |

Cuando hay actividad en más de un chat, la mascota prioriza los chats que requieren
intervención, seguidos de los bloqueados, los listos y los que están en curso. Abre la bandeja de actividad para
elegir un chat.

Selecciona la mascota para volver a ChatGPT o selecciona una actividad para abrir el chat correspondiente.
La bandeja de actividad es independiente de las [notificaciones
del sistema](/es-419/codex/notifications?surface=app).

### Seguir el Uso de la computadora

En macOS, la ventana de imagen en imagen de [Uso de la computadora](/es-419/codex/computer-use) puede
acoplarse a una mascota despierta. Mueve la mascota y la ventana la seguirá.

### Crear una mascota personalizada

1. Abre **Configuración \> Mascotas** y selecciona **Crear tu propia mascota**.
2. La app instala la habilidad `hatch-pet` incluida, vuelve a cargar las habilidades y abre un
   chat nuevo.
3. Describe la mascota que quieres y envía el prompt.
4. Cuando termine la tarea, vuelve a **Configuración \> Mascotas**, selecciona **Actualizar**
   y elige tu nueva mascota.

Las mascotas personalizadas creadas en la app de escritorio se almacenan localmente en tu computadora.
No se sincronizan automáticamente con ChatGPT en la web.

### Reducir la animación

Las mascotas respetan la configuración de reducción de movimiento de tu sistema operativo. Cuando la reducción
de movimiento está activada, la mascota usa un fotograma estático en lugar de una animación de sprites.

## Elegir una mascota en la web

Si la función Mascotas está disponible para tu cuenta y espacio de trabajo, abre **Configuración \>
Personalización \> Mascota \> Seleccionar mascota**. Elige una mascota integrada o selecciona
**Predeterminado** para usar ChatGPT sin mascota.

Una mascota en la web aparece dentro de los chats compatibles de ChatGPT Work. No incluye la
superposición flotante, la bandeja de actividad ni el comando `/pet` de la app de escritorio.

### Subir una mascota personalizada

Selecciona **Subir mascota** para agregar una hoja de sprites personalizada. El archivo debe ser un
PNG o WebP transparente, de exactamente 1536 × 1872 píxeles y no superar los 20 MiB.
Desde la misma configuración, puedes editar, descargar, actualizar o eliminar las mascotas que subiste.

## Elegir una mascota de la terminal

En una sesión interactiva de la CLI de Codex:

- Ingresa `/pets` o `/pet` para abrir el selector de mascotas.
- Ingresa `/pets <name>` para elegir una mascota directamente.
- Ingresa `/pets off` para desactivar las mascotas de la terminal.

El selector incluye mascotas integradas y mascotas personalizadas compatibles instaladas en tu
computadora. Una mascota de la terminal muestra la actividad de la sesión actual de la CLI. Usa los estados
**En curso**, **Requiere intervención**, **Listo** y **Bloqueado**, pero no
ofrece la bandeja de actividad para varios chats de la app de escritorio.

Las mascotas de la terminal requieren iTerm2 3.6 o una versión posterior, o una terminal compatible con gráficos Kitty o
Sixel. No están disponibles en tmux ni Zellij.

## Mascotas en la extensión para IDE

La extensión para IDE de Codex no incluye un selector de mascotas ni una superposición flotante.
Usa la app de escritorio de ChatGPT o la CLI de Codex cuando quieras usar tu propia mascota.

</div>

## Documentación relacionada

- [Notificaciones](/es-419/codex/notifications)
- [Trabajo de larga duración](/es-419/codex/long-running-work)
- [Configuración de la app de escritorio de ChatGPT](/codex/reference/settings#pets)
