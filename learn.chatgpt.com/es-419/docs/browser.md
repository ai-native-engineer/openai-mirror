<!-- source: https://learn.chatgpt.com/es-419/docs/browser -->

El Navegador no está disponible en Codex CLI ni en la Extensión de Codex para IDE. Abre la
aplicación de escritorio de ChatGPT para usar el navegador integrado.

El Navegador permite que ChatGPT abra sitios web, recopile información actual y realice acciones
mientras tú mantienes el control. Úsalo para comparar opciones, completar una tarea de varios pasos
en un sitio web o revisar una página que estés creando.

El Navegador está disponible en ChatGPT en la web y en la aplicación de escritorio de ChatGPT.

[GPT-6 Astra](/es-419/codex/models#gpt-6-astra) mejora el criterio visual en tareas como
comparar una página con una captura de pantalla o completar un flujo de trabajo en varios sitios.
Elígelo cuando esté disponible en tu selector de modelos y describe cómo verificar
el resultado final.

En entornos de escritorio administrados, los administradores pueden restringir los orígenes del navegador,
las cargas, las descargas y el acceso para desarrolladores. Consulta los
[controles del navegador administrado](/es-419/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Trata el contenido de las páginas como contexto no confiable. Revisa el sitio y la acción propuesta
antes de compartir información confidencial o permitir que ChatGPT actúe.

El navegador integrado de la aplicación de escritorio de ChatGPT les ofrece a ChatGPT y a ti una vista compartida
de sitios web y aplicaciones web locales dentro de un chat. Úsalo para previsualizar una página,
dejar comentarios visuales o permitir que ChatGPT interactúe con un sitio en tu nombre.

El navegador integrado usa un perfil de navegador distinto del de tu navegador
habitual. No comparte automáticamente tus pestañas actuales ni tu sesión de navegación.
Puedes iniciar sesión directamente cuando una tarea requiera una cuenta. Abre **Configuración \>
Navegador** para administrar los datos del navegador y las funciones de importación de perfiles disponibles
en tu dispositivo.

De forma predeterminada, las descargas del navegador se guardan en la carpeta Descargas del sistema. En **Configuración \>
Navegador**, puedes elegir otra ubicación de descarga, restablecer la ubicación
predeterminada del sistema o activar **Preguntar dónde guardar las descargas**.

En su lugar, usa la [extensión del navegador](/es-419/codex/chrome-extension) cuando ChatGPT necesite
trabajar en una pestaña existente de Chrome, Edge, Brave, Opera o Vivaldi, o usar tu
perfil habitual del navegador.

Abre el navegador integrado desde la barra de herramientas, al hacer clic en una URL, al navegar
manualmente o al presionar <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>
(<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> en Windows).

  
    
  

## Buscar desde la barra de direcciones

Empieza a escribir en la barra de direcciones del navegador integrado para buscar páginas en su
historial de navegación. Selecciona una página coincidente para volver a abrirla o ingresa un término de búsqueda
para buscar en Google cuando no haya coincidencias en el historial.

El navegador integrado mantiene su propio perfil e historial de navegación. Los resultados no incluyen
automáticamente páginas de tu perfil habitual de Chrome ni de otros navegadores.

## Administrar el historial de navegación

Abre **Configuración \> Navegador** para buscar en el historial del navegador integrado, volver a abrir una
página visitada o eliminar entradas del historial cuando tu organización lo permita. Usa
**Borrar datos de navegación** para elegir un intervalo de tiempo y los tipos de datos de navegación
que quieras eliminar.

Cuando esta función esté disponible, ChatGPT puede pedir permiso para buscar en tu historial de navegación y encontrar una página
relevante para la tarea actual. Revisa la solicitud antes de permitir el acceso.
El historial de navegación puede incluir URL internas, términos de búsqueda y otra información
confidencial, así que permite el acceso solo cuando la tarea requiera ese contexto.

<a id="browser-use"></a>

## Uso de la computadora en el navegador

En la aplicación de escritorio, Uso de la computadora permite que ChatGPT Work o Codex controlen el
navegador integrado directamente. La experiencia seleccionada puede abrir páginas, hacer clic, escribir,
inspeccionar el estado renderizado, tomar capturas de pantalla y verificar el resultado de su trabajo en
la página.

El Navegador viene incluido en la aplicación de escritorio y se instala automáticamente. Pídele a ChatGPT
o a Codex que use el navegador integrado en tu tarea, o haz referencia a él directamente con
`@Browser`.

Por ejemplo:

```text
Use the browser to open http://localhost:3000/settings, reproduce the layout
bug, and fix only the overflowing controls.

ChatGPT pide permiso antes de usar un sitio web, a menos que ya hayas permitido ese
sitio. Administra los sitios permitidos y bloqueados en **Configuración \> Navegador**. ChatGPT también
pide confirmación antes de realizar acciones sensibles, como enviar información,
hacer una compra, cambiar permisos o eliminar datos. ChatGPT no puede
automatizar la carga de archivos en el navegador integrado.

  Las instrucciones de una página pueden ser engañosas o maliciosas. El permiso para un sitio web
permite que ChatGPT interactúe con ese sitio; no hace que su contenido sea
confiable ni implica que todas las acciones estén aprobadas.

## Previsualizar una página

1. Inicia el servidor de desarrollo de tu aplicación en la [terminal integrada](/es-419/codex/integrated-terminal) o con una [acción del entorno local](/es-419/codex/environments/local-environment#actions).
2. Abre la ruta local, la página basada en un archivo o la página pública haciendo clic en una URL o
navegando manualmente en el navegador.
3. Revisa el estado renderizado junto con el diff del código.
4. Deja comentarios del navegador en los elementos o las áreas que necesiten cambios.
5. Pídele a ChatGPT que atienda los comentarios y mantenga el alcance acotado.

Por ejemplo:

```text
I left comments on the pricing page in the built-in browser. Address the mobile
layout issues and keep the card structure unchanged.

## Comentar en la página

Cuando un error solo sea visible en la página renderizada, usa los comentarios del navegador para darle a
ChatGPT indicaciones precisas.

1. Activa el **Modo de anotación**.
2. Haz clic en un elemento o arrastra para seleccionar un área.
3. Escribe y guarda tu comentario.
4. Envía un mensaje en el chat para pedirle a ChatGPT que atienda los comentarios.

Los comentarios funcionan mejor si indicas el problema y el resultado que deseas:

```text
This button overflows on mobile. Keep the label on one line if it fits,
otherwise wrap it without changing the card height.

```text
This tooltip covers the data point under the cursor. Reposition the tooltip so
it stays inside the chart bounds.

<section class="feature-grid">

<div>

### Comentarios sobre el estilo

Cuando agregues una anotación a una sección de la página, selecciona **Ajustar** junto al
campo de texto para darle a ChatGPT comentarios más detallados sobre el estilo. Puedes cambiar
valores como la fuente, el texto, el espaciado y el color, previsualizar el resultado en la página
y luego enviar la anotación con un objetivo más claro.

</div>

  
    
  

</section>

## Limitar el alcance de las tareas del navegador

Acota cada tarea del navegador para poder revisarla de una sola vez.

- Indica la página, la ruta o la URL.
- Indica el estado que te interesa, como carga, vacío, error o éxito.
- Deja comentarios justo en los elementos o las áreas que necesiten cambios.
- Vuelve a revisar la página cuando ChatGPT termine.
- Pídele a ChatGPT que inicie o verifique el servidor de desarrollo antes de abrir una página
local.

Para los cambios en el repositorio, usa el [panel de revisión](/es-419/codex/code-review?surface=app) para
inspeccionar los cambios y dejar comentarios.

<section class="feature-grid">

<div>

## Modo de desarrollador

El Modo de desarrollador funciona con Uso de la computadora en Chrome y en el navegador integrado.
Proporciona a ChatGPT acceso controlado al Chrome DevTools Protocol (CDP). Úsalo para analizar el rendimiento de
JavaScript, inspeccionar la salida de la consola y el tráfico de red, examinar el DOM y los estilos
aplicados o diagnosticar un problema en el navegador activo.

Para habilitarlo, abre [**Configuración \> Navegador**](codex://settings/browser-use) y,
en **Modo de desarrollador**, activa **Habilitar acceso completo a CDP**. Si tu
organización deshabilitó esta configuración, no puedes habilitarla localmente. Los administradores pueden
establecer `browser_use_full_cdp_access = false` en la sección `[features]` de
[`requirements.toml`](/es-419/codex/enterprise/managed-configuration#pin-feature-flags)
para deshabilitar el acceso completo a CDP e impedir que los usuarios habiliten la configuración
correspondiente en la aplicación de escritorio de ChatGPT.

El acceso completo a CDP puede exponer componentes internos confidenciales del navegador. ChatGPT solicita
aprobación explícita antes de usar el acceso completo a CDP para inspeccionar un sitio web. Revisa el
sitio, la tarea y el acceso solicitado antes de aprobarlo.

Usa `@Browser` para el navegador integrado. Para usar el Modo de desarrollador en Chrome,
[configura la Extensión de Chrome](/es-419/codex/chrome-extension) e invoca `@Chrome`.

Por ejemplo:

```text
This app is slow. Use @Browser to capture a performance trace and inspect
network traffic, then identify the bottleneck.

</div>

  
    
  

</section>

## Usar ChatGPT Work para completar tareas en la web

ChatGPT Work puede completar tareas en distintos sitios web, incluidos aquellos en los que necesitas iniciar sesión.

Work usa su propio navegador, que se ejecuta en una computadora independiente en la nube, no el navegador de tu teléfono o computadora portátil.

Inicia una tarea desde ChatGPT Work en la web o en un dispositivo móvil, y ChatGPT podrá seguir trabajando aunque te alejes y cierres tu computadora. Con su computadora, Work puede realizar una gran variedad de tareas en internet al leer, hacer clic y escribir en páginas web. Según tu solicitud, puede usar un complemento, su navegador o ambos.

Por ejemplo, ChatGPT puede ayudarte a:

- Buscar y reservar una cita en el DMV.
- Iniciar sesión en tu cuenta de servicios públicos y comparar planes.
- Buscar y guardar departamentos que cumplan con tus criterios.
- Investigar a la competencia en redes sociales.
- Realizar el cierre contable en tu software de contabilidad.

Tú controlas a qué sitios web puede acceder ChatGPT, y está entrenado para pedir confirmación antes de realizar acciones con consecuencias importantes, como completar una reserva o un pago. Si ChatGPT no puede continuar por algún motivo, puedes tomar el control de su computadora y usarla desde un dispositivo móvil o una computadora.

La capacidad de ChatGPT Work para navegar por sitios web que requieren autenticación está disponible en la web y en dispositivos móviles con los planes Plus y Pro.

La disponibilidad depende del despliegue. El inicio de sesión en sitios web no está disponible para los espacios de trabajo de Empresas o Edu.

## Cómo funciona la computadora de ChatGPT Work

Cuando tu tarea requiere un sitio web, ChatGPT usa su propio navegador para recorrer páginas, recopilar información y completar pasos en línea.

De forma predeterminada, ChatGPT pregunta antes de acceder a un sitio web nuevo. Puedes aprobar las solicitudes individualmente o ajustar la configuración para que ChatGPT apruebe automáticamente los sitios web pertinentes para tu tarea. ChatGPT Work siempre pedirá confirmación antes de realizar acciones con consecuencias importantes, como enviar tu información para reservar una cita o completar un pago.

## Iniciar sesión en un sitio web

Si un sitio web requiere que inicies sesión, ChatGPT Work te pedirá que lo hagas. Una vez que te autentiques, continuará trabajando en el sitio web con la sesión iniciada. Tu sesión permanecerá activa para futuras tareas, así que no tendrás que iniciar sesión cada vez.

### Usar el formulario seguro de inicio de sesión

ChatGPT no puede ver tu nombre de usuario ni tu contraseña. El modelo nunca los ve y nunca se usan para entrenarlo. ChatGPT no almacena tu nombre de usuario ni tus contraseñas. Puedes eliminar en cualquier momento tu historial de navegación de todos los sitios o de un sitio individual desde **Configuración** \> **Navegador en la nube** \> **Datos del navegador**, lo que cerrará tu sesión en ese sitio.

Cuando ChatGPT encuentra una pantalla de inicio de sesión, hace una pausa y te pide que ingreses tus credenciales y los códigos de autenticación de dos factores que se necesiten. En iOS, puedes usar un administrador de contraseñas compatible para iniciar sesión sin complicaciones.

Usa el formulario de inicio de sesión que proporciona ChatGPT. No envíes contraseñas por el chat.

![ChatGPT Work en iOS con una tarea del DMV en pausa y un formulario seguro de inicio de sesión que muestra la dirección del sitio web y una contraseña enmascarada.](/images/codex/cloud-browser-auth/sign-in.webp)

### Iniciar sesión en la página web

Si la opción está disponible, selecciona **Iniciar sesión en la página web en su lugar** para iniciar sesión directamente en el navegador en la nube. La tarea se pausa mientras inicias sesión. Selecciona **Ya terminé** para devolverle el control a ChatGPT, o bien omite o cancela la solicitud.

<a id="start-a-browser-task"></a>
<a id="start-browser-work"></a>
<a id="web-start-browser-work"></a>

## Cómo iniciar una tarea en ChatGPT Work

1. Abre ChatGPT en la web o en un dispositivo móvil e inicia una tarea en Work.
2. Describe lo que quieres que haga ChatGPT.
3. Aprueba el acceso al sitio web si se te solicita.
4. Inicia sesión directamente si un sitio web lo requiere.
5. Sigue el progreso de la tarea en la conversación.
6. Revisa el resultado y aprueba las acciones que tengan consecuencias importantes.

No necesitas seleccionar el navegador por separado. ChatGPT decide cuándo usarlo según tu solicitud.

Algunos sitios web bloquean el acceso. Si eso sucede, ChatGPT te lo informará y, cuando sea posible, intentará completar la tarea de otra manera.

<a id="website-permissions-and-confirmations"></a>
<a id="web-website-permissions-and-confirmations"></a>

## Seguridad y controles del usuario

En la configuración de ChatGPT, abre **Navegador en la nube** para administrar los permisos de sitios web. Las opciones disponibles incluyen:

- **Preguntar siempre**: revisa manualmente cada solicitud de acceso a un sitio web.
- **Aprobar automáticamente**: permite que ChatGPT apruebe automáticamente el acceso después de comprobar si el sitio web es pertinente para tu tarea.
- **Permitir siempre**: permite el acceso a sitios web sin ese paso adicional de revisión. Ofrecemos esta opción para reducir al mínimo las interrupciones, pero no la recomendamos.

![Configuración del navegador en la nube que muestra las opciones de permisos de sitios web Preguntar siempre, Aprobar automáticamente y Permitir siempre.](/images/codex/cloud-browser-auth/website-permissions.webp)

También puedes permitir o bloquear sitios web específicos para establecer excepciones a tus permisos predeterminados.

Antes de que ChatGPT te pida iniciar sesión en cualquier sitio web, un modelo adicional de revisión comprueba la solicitud de inicio de sesión y el lugar donde se ingresará tu información para detectar indicios de phishing o engaño. Ponemos a prueba al agente frente a riesgos como la inyección de prompts, el phishing y las acciones no deseadas.

Para ofrecer total transparencia, verás la dirección del sitio web y una vista previa de su formulario de inicio de sesión, y podrás inspeccionar el sitio web en vivo antes de continuar. Las credenciales que ingreses en el formulario seguro de inicio de sesión van directamente al navegador y no son visibles para el modelo.

<a id="browser-data"></a>
<a id="web-browser-data"></a>

## Privacidad y datos del navegador

La computadora de ChatGPT Work funciona de manera independiente del navegador de tu dispositivo. Mantiene sus propias cookies, datos del navegador y sesiones iniciadas. La información que ChatGPT usa al completar una tarea se rige por la configuración de controles de datos que elijas en ChatGPT. Puedes revisar esta configuración en ChatGPT en la web y en dispositivos móviles, en **Configuración** \> **Controles de datos**.

No usa las pestañas abiertas, el historial de navegación, las contraseñas guardadas, las cookies, las extensiones ni las sesiones ya iniciadas de tu navegador personal.

Para borrar los datos del navegador, ve a **Configuración** \> **Navegador en la nube** \> **Datos del navegador** \> **Borrar todo**. Esto cierra tus sesiones en los sitios web del navegador de ChatGPT Work, por lo que tendrás que volver a iniciar sesión para futuras tareas.

![Configuración del navegador en la nube con una sección Datos del navegador y un control de Cookies para administrar las cookies guardadas por el navegador en la nube.](/images/codex/cloud-browser-auth/browser-data.webp)

## Limitaciones

- El inicio de sesión en sitios web no está disponible en todos los espacios de trabajo ni en todas las etapas del despliegue. Si una tarea requiere un método de inicio de sesión que no es compatible, completa ese paso por tu cuenta o usa otra herramienta disponible.
- Algunos sitios bloquean los navegadores automatizados o requieren un CAPTCHA. Es posible que ChatGPT no pueda completar una tarea en esos sitios.
- La disponibilidad de la navegación en la nube puede depender de tu plan, la configuración de tu espacio de trabajo y el despliegue. La navegación en la nube está disponible en todas las regiones con los planes de pago, excepto Gratis y Go. Los administradores de Empresas deben habilitar la navegación en la nube para su espacio de trabajo.

Durante el despliegue, es posible que el navegador no aparezca de inmediato aunque tu plan lo admita.
