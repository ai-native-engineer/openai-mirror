<!-- source: https://learn.chatgpt.com/es-419/use-cases/use-your-computer-with-codex -->

## Introducción

Utiliza [Uso de la computadora](/es-419/docs/computer-use) cuando una tarea abarque apps de escritorio, ventanas o archivos locales. ChatGPT puede hacer clic, escribir y navegar por las apps que autorices, y luego entregarte el resultado para que lo revises. Para trabajar en un sitio web o en un navegador donde hayas iniciado sesión, inicia una tarea independiente en el navegador con `@Chrome`.

**Uso de la computadora requiere la aplicación de escritorio de ChatGPT.** En las regiones compatibles, Uso de la computadora está disponible en ChatGPT Work y Codex para macOS y Windows. Las tareas de Work en la nube que se ejecutan en la web o en dispositivos móviles no pueden acceder directamente a tus apps o archivos locales ni a las sesiones del navegador de escritorio en las que hayas iniciado sesión. Puedes iniciar o dirigir una tarea de escritorio desde [Remoto en dispositivos móviles](/es-419/codex/remote-connections) cuando conectes un host Mac o Windows.

Algunos buenos ejemplos son pasar notas a un sistema de registro, consultar el contexto en varias apps antes de redactar una respuesta o copiar información aprobada entre herramientas que no tienen un complemento específico.

Así puede verse la delegación segura de una tarea de escritorio cuando Mensajes y Notas contienen tus planes para una escapada de fin de semana a una cabaña:

<div data-use-case-export-only>

**Tarea de escritorio:** reúne ideas para una escapada de fin de semana a una cabaña a partir de Mensajes y de una lista de opciones preseleccionadas en Notas, crea una nota local y redacta una respuesta.

**Resultado:** Pine Lodge tiene acceso sin escalones, está a no más de dos horas y cuesta $690 en total. Lake House podría ser una opción, pero aún falta confirmar el tiempo de viaje y la accesibilidad. Cedar Ridge se descarta porque tiene escaleras. No se conoce el tamaño del grupo, por lo que el precio por persona sigue sujeto a confirmación.

La nota local y el borrador de la respuesta están listos para su revisión. No se reservó ni se envió nada.

</div>

## Cómo usarlo

1. Abre la aplicación de escritorio de ChatGPT e instala el [complemento de Uso de la computadora](/es-419/docs/computer-use).
2. Inicia tu solicitud con `@Computer` para las apps de escritorio o con `@Chrome` para las tareas del navegador.
3. Describe la tarea, las apps o los archivos involucrados y el resultado que quieres obtener.
4. Revisa las solicitudes de acceso y haz una pausa antes de realizar acciones que impliquen enviar, presentar o modificar datos importantes.
5. En Windows, mantén visible la app de destino mientras se ejecuta Uso de la computadora.

Si existe un complemento para una app, ChatGPT puede usarlo para realizar la acción estructurada. Uso de la computadora es útil cuando la tarea depende de la interfaz de la app o no hay ningún complemento disponible.

## Qué puedes probar

Comienza con una sola herramienta: usa `@Computer` para las apps de escritorio y los archivos locales, o `@Chrome` para tu navegador. ChatGPT puede elegir otras herramientas según sea necesario.

**Convierte mensajes en un plan**

**Busca lugares donde hospedarte**

**Ponte al día con un proyecto**

**Actualiza un sistema de seguimiento a partir de las notas de una reunión**

**Trabaja en tu navegador con la sesión iniciada**

**Prueba un sitio web**

**Ordena los archivos locales**

**Muéstrale lo que estás viendo**

En macOS, usa una [captura de la aplicación](/es-419/codex/appshots) para compartir la ventana de la app que tienes en primer plano. Las capturas de la aplicación proporcionan contexto visual; luego, Uso de la computadora puede abrir la app, inspeccionarla e interactuar con ella si lo permites.

## Consejos prácticos

### Entiende cómo se ejecuta la tarea en cada computadora

En macOS, Uso de la computadora puede funcionar en segundo plano mientras usas otras apps. Una vista previa de imagen en imagen muestra la app activa; ábrela para seguir el progreso o muévela para que no estorbe. Si usas una Mascota, puedes mover la vista previa allí.

En Windows, Uso de la computadora se ejecuta en el escritorio activo y toma el control en primer plano. Mientras se ejecuta la tarea, verás movimientos del puntero y actividad del teclado. Mantén el dispositivo desbloqueado y conectado, o ejecuta la app de escritorio en una máquina virtual de Windows si necesitas seguir usando tu escritorio principal.

### Elige el navegador adecuado

Las tareas en el navegador suelen formar parte de Uso de la computadora. Elige el navegador que tenga el contexto que necesitas:

- **[Extensión de Chrome](/es-419/codex/chrome-extension):** usa `@Chrome` para tareas en el navegador, como buscar anuncios, consultar sitios web y usar tu perfil actual de Chrome con la sesión iniciada, tus pestañas o tus extensiones.
- **[Navegador integrado](/es-419/codex/browser?surface=app):** úsalo cuando quieras una sesión de navegador independiente para localhost o sitios públicos. Tiene su propio estado de navegación y puede esperar mientras inicias sesión.
- **Navegador en la nube de ChatGPT Work en la web o dispositivos móviles:** úsalo con sitios públicos compatibles sin iniciar sesión. No puede acceder a archivos locales, pestañas abiertas, extensiones ni contraseñas guardadas; tampoco puede iniciar sesión en sitios ni completar pagos.

Especifica el navegador en el prompt cuando sea importante y usa la [personalización](/es-419/docs/customization/overview) para definir una preferencia de escritorio recurrente.

### Evita ejecutar tareas en paralelo en la misma app

No ejecutes dos tareas de Uso de la computadora en la misma app al mismo tiempo. Las acciones en conflicto pueden cambiar la ventana o el estado actuales y hacer que el resultado no sea confiable.

### Prepara las apps con sesión iniciada y el uso con la pantalla bloqueada

Antes de iniciar una tarea de escritorio, inicia sesión en las apps y los servicios que necesite. En macOS, puedes habilitar el [uso con la pantalla bloqueada](/es-419/docs/computer-use#locked-use) si la tarea debe continuar después de que la Mac se bloquee. El uso con la pantalla bloqueada no está disponible para Uso de la computadora en Windows.
