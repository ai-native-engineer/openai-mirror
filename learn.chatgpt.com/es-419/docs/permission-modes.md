<!-- source: https://learn.chatgpt.com/es-419/docs/permission-modes -->

{/* vale Microsoft.FirstPerson = NO */}

## Modos de permisos

Los permisos controlan cómo ChatGPT (en la aplicación de escritorio) y Codex (en la CLI o el IDE) gestionan las acciones locales, como editar archivos, ejecutar comandos y usar internet. El modo que elijas define el límite
entre lo que ChatGPT puede hacer por su cuenta y lo que requiere revisión.

Para la mayoría de las tareas, comienza con **Solicitar aprobación**. Con este modo, ChatGPT puede trabajar dentro del
espacio de trabajo actual y se detiene antes de rebasar ese límite.

Selecciona distintos modos a continuación para saber cómo funciona cada uno.

## Habilitar los modos

Cuando uses por primera vez la aplicación de escritorio de ChatGPT, debes habilitar los modos en la configuración de la aplicación.

**Solicitar aprobación** está siempre disponible. Para agregar **Aprobar por mí** (que en la configuración se llama
**Revisión automática**) o **Acceso completo** al menú de permisos, abre
**Configuración \> General** en la aplicación de escritorio de ChatGPT y activa el modo en
**Permisos**. Habilitar un modo hace que esté disponible en el menú; no se
selecciona ese modo ni se modifica ningún chat existente.

  

  Los modos disponibles pueden depender de tu configuración local y de los
requisitos de tu organización. Un modo no permitido aparece deshabilitado.

## Cómo funcionan los permisos

Dos controles funcionan en conjunto:

- El **sandbox** define a qué archivos y recursos de red puede acceder ChatGPT.
- Las **aprobaciones** determinan cuándo ChatGPT se detiene antes de realizar una acción o envía la
  solicitud a revisión automática.

Cambiar quién revisa una solicitud no amplía el sandbox. Por ejemplo,
**Aprobar por mí** mantiene el mismo límite del espacio de trabajo que **Solicitar aprobación**;
envía a revisión automática las solicitudes para rebasar ese límite.

Usa el control de permisos que aparece debajo del Editor en la aplicación de escritorio de ChatGPT o en la
extensión para IDE.

En la CLI, ingresa `/permissions`. Para obtener detalles técnicos, consulta
[Sandbox](/es-419/codex/sandboxing), [revisión automática](/es-419/codex/sandboxing/auto-review) o
[perfiles de permisos](/es-419/codex/permissions).
