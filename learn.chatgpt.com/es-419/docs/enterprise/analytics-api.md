<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/analytics-api -->

La Analytics API de Codex proporciona métricas agregadas sobre el uso y la actividad de Codex para
un espacio de trabajo de ChatGPT.

La [referencia de la Analytics API de Codex](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)
es la fuente oficial de información vigente sobre los requisitos de acceso, las rutas, los esquemas de solicitud y
respuesta, las métricas, la semántica temporal y la paginación.

## Cuándo usar la Analytics API

La Analytics API es adecuada cuando necesitas:

- Automatizar la generación periódica de informes de Codex.
- Cruzar las métricas agregadas de Codex con datos internos de la organización.
- Crear una capa controlada de generación de informes para destinatarios autorizados.
- Evitar que una integración dependa de un panel interactivo.

No es una interfaz para registros de auditoría sin procesar. Usa la
[API de Cumplimiento](/es-419/codex/enterprise/compliance-api) cuando el flujo de trabajo requiera
registros de actividad auditables.

## Confirma los límites administrativos

Los resultados de la Analytics API se limitan a un espacio de trabajo de ChatGPT, pero las solicitudes
se autentican con una clave de API de una organización de la Plataforma. La organización a la que pertenece la clave debe
coincidir con la organización asociada al espacio de trabajo.

La referencia de la API es la fuente oficial de información vigente sobre el aprovisionamiento de claves, los requisitos de alcance,
las rutas, los esquemas, los campos, la semántica temporal y el comportamiento de la paginación. Esta página
no duplica ese contrato.

## Documentación relacionada

- [Analítica del espacio de trabajo](/es-419/codex/enterprise/workspace-analytics)
- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
- [Gobernanza](/es-419/codex/enterprise/governance)
- [API de Cumplimiento](/es-419/codex/enterprise/compliance-api)
