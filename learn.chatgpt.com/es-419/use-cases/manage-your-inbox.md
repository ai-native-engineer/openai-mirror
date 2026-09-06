<!-- source: https://learn.chatgpt.com/es-419/use-cases/manage-your-inbox -->

## Antes de comenzar

Puedes ejecutar este flujo en ChatGPT Work desde el navegador o la app de escritorio. Antes de comenzar:

- **Conecta tu correo electrónico.** Instala el [complemento de Gmail u Outlook Email](/es-419/docs/plugins). También puedes conectar Slack, Google Drive y tu calendario para darle a ChatGPT más contexto al redactar respuestas.
- **Elige dónde se ejecutarán las revisiones programadas.** Comienza en el navegador si quieres que las revisiones continúen cuando tu laptop esté apagada. En la app de escritorio, mantén encendida la computadora y abierta la aplicación de escritorio de ChatGPT. Los chats de voz no admiten [tareas programadas](/es-419/docs/automations), así que configúralas o adminístralas desde un chat.

## Qué puedes esperar

ChatGPT revisa los correos recientes, identifica los mensajes que requieren atención, propone una limpieza y prepara respuestas sin enviarlas. Una vez que apruebes la limpieza, puede aplicar esos cambios a los mensajes anteriores acumulados. Así podría verse esa conversación:

<div data-use-case-export-only>

Revisé tu bandeja de entrada laboral conectada, centrada en los lanzamientos de productos, la documentación y el trabajo de producción. Tiene **116 mensajes, 96 sin leer**; la mayoría de los mensajes sin leer corresponde a actividad de proyectos, actualizaciones del calendario, notificaciones de archivos compartidos y boletines.

### Qué requiere atención

- **Preparación de la grabación:** envía los temas solicitados para la demostración, una biografía breve y una foto antes de la sesión de mañana.
- **Revisión de la documentación:** atiende las observaciones sobre la exactitud de la información del producto antes de continuar con la guía.
- **Error en la implementación de la vista previa:** investiga la compilación fallida antes de basarte en los cambios actuales.
- **Tarea sobre beneficios:** completa el cambio pendiente en los beneficios.
- **Alerta de inicio de sesión:** confirma si el inicio de sesión reciente fue tuyo y, si no, sigue las instrucciones de la alerta.

### Limpieza

Etiquetaría y archivaría las notificaciones rutinarias de proyectos, calendario y documentos con las etiquetas `Project activity`, `Calendar` y `Docs`; el correo archivado seguirá disponible en las búsquedas. Las solicitudes directas, las revisiones activas, las compilaciones fallidas, las alertas de seguridad y cualquier asunto sin resolver seguirían visibles. Conviene revisar por separado los boletines y otras suscripciones recurrentes.

### Una respuesta para quien organiza la grabación

La persona que organiza la grabación está esperando los temas de la demostración, una biografía breve y una foto. Revisé la información más reciente sobre el horario y redacté una respuesta con tu estilo:

> Me entusiasma participar. Planeo mostrar los tres flujos de trabajo que comentamos y enviaré hoy la biografía y la foto. Vi la invitación actualizada del calendario, así que me ajustaré al nuevo horario.

De ahora en adelante, revisaré a las **8 a. m. y 4 p. m. de lunes a viernes**. Te mostraré cualquier correo nuevo o actualizado que requiera tu atención, consultaré fuentes conectadas, como la mensajería, los documentos o tu calendario, cuando corresponda, y prepararé respuestas con tu estilo. Puedes darme otras indicaciones en cualquier momento respondiendo aquí.

### ¿Qué te gustaría que hiciera?

1. **¿Aplico la limpieza?** Sí / no. Los mensajes rutinarios se etiquetarán y archivarán, no se eliminarán.
2. **¿Guardo la respuesta como borrador?** Sí / no.
3. **¿Mantengo el horario y las prioridades propuestos?** Sí / no.

Responde “1 sí, 2 sí, 3 no” e incluye cualquier cambio.

</div>

**Advertencia:** el complemento de Gmail puede mover correos a la Papelera cuando lo pides explícitamente. Primero revisa los grupos propuestos y algunos mensajes de muestra, y archiva cualquier mensaje que te genere dudas en lugar de eliminarlo. Las acciones disponibles pueden variar según el complemento de correo electrónico y la configuración del espacio de trabajo.

## Cómo funciona

Un flujo de trabajo de correo electrónico tiene varias partes:

- **Contexto de las herramientas conectadas:** los complementos permiten que ChatGPT lea tu correo electrónico y consulte otras herramientas conectadas cuando una respuesta requiere más contexto. Slack puede contener la conversación o decisión más reciente, Google Drive puede tener archivos o documentación del proyecto relevantes, y tu calendario puede aclarar fechas o reuniones.
- **Prioridades:** puedes indicarle a ChatGPT qué personas, solicitudes, alertas y mensajes recurrentes debe priorizar o ignorar. Las revisiones futuras pueden seguir esas instrucciones.
- **Límites de aprobación:** ChatGPT propone una limpieza y redacta borradores de respuestas, pero espera tu aprobación antes de actuar.
- **Tareas programadas:** en lugar de esperar a que regreses y vuelvas a pedirlo, ChatGPT puede buscar mensajes nuevos en la misma tarea según un horario.

## Crea tu propio flujo de trabajo de correo electrónico

Puedes ser más específico cuando ya sabes lo que quieres. Un prompt de **correo de trabajo**
podría dar prioridad a las conversaciones activas, las solicitudes, las aprobaciones y el contexto del
proyecto:

En cambio, un prompt de **correo personal** podría centrarse en personas que conoces, facturas,
paquetes, viajes, citas y alertas de la cuenta:

Ambos ejemplos siguen la misma estructura básica: qué revisar, qué es importante, qué hacer, cuándo hacerlo y qué requiere aprobación.

## Ir más allá

Una vez que el flujo de trabajo básico esté en marcha, puedes perfeccionarlo o pedirle a ChatGPT que se encargue de otras tareas útiles relacionadas con el correo electrónico.

**Consulta siempre el contexto adecuado**

**Redacta una actualización periódica**

**Haz seguimiento de los correos sin respuesta**

**Cambia el formato**

**Enséñale qué es importante**

**Ajusta cómo redacta las respuestas**

**Cambia el horario de revisión**

Mantén las acciones de limpieza y respuesta sujetas a aprobación hasta que confíes en las reglas.

Las acciones de Gmail y Outlook y las tareas programadas dependen de tu plan y de la configuración de tu espacio de trabajo.
