<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/workspace-analytics -->

Usa la analítica del espacio de trabajo de ChatGPT para conocer la adopción general en el espacio de trabajo. Usa la analítica de Codex
para generar informes centrados en Codex. Usa la Analytics API para obtener datos agregados
mediante programación y la API de Cumplimiento para acceder a registros auditables.

Estas opciones para generar informes no otorgan acceso al producto ni establecen políticas en tiempo de ejecución. Consulta
[Roles y permisos del espacio de trabajo](/es-419/codex/enterprise/roles-and-workspace-permissions)
para conocer los límites administrativos.

## Elegir una opción para generar informes

| Opción                     | Úsala para                                                    | Responsable del contrato                                                                                                         |
| --------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Analítica del espacio de trabajo de ChatGPT | Informes interactivos sobre la adopción y la interacción en todo el espacio de trabajo | [Guía del Centro de ayuda sobre la analítica del espacio de trabajo](https://help.openai.com/en/articles/10875114)                               |
| Analítica de Codex             | Informes interactivos centrados en la adopción y la actividad de Codex  | El [panel de analítica de Codex](https://admin.openai.com/analytics/codex) con acceso autenticado                                |
| Analytics API               | Generación de informes agregados de Codex mediante programación                      | La [documentación de referencia de Codex Analytics API](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics) |
| API de Cumplimiento              | Registros de auditoría, de seguridad, legales y de investigación             | La [documentación de referencia de Admin API](https://chatgpt.com/public/admin/api-reference)                                              |

## Revisar la analítica del espacio de trabajo de ChatGPT

La analítica del espacio de trabajo de ChatGPT ofrece una vista interactiva de la adopción y
la interacción en las funciones compatibles del espacio de trabajo. La disponibilidad, los roles, las secciones
del panel, el grado de actualización de los datos, el tratamiento de la privacidad y los formatos de exportación pueden cambiar. Consulta
[Analítica del espacio de trabajo para ChatGPT Enterprise y Edu](https://help.openai.com/en/articles/10875114)
para conocer la cobertura y los procedimientos actuales.

Trata los informes descargados como datos identificables de la organización.
Aplica la política de acceso, almacenamiento y retención de la organización, en lugar de
suponer que una exportación tiene las mismas características de privacidad que un panel con datos
agregados.

## Revisar la analítica de Codex

El [panel de analítica de Codex](https://admin.openai.com/analytics/codex) con acceso autenticado
se centra en los informes de Codex. Úsalo para la exploración interactiva, no como un contrato
de esquema estable. Las categorías, los campos, los filtros y los formatos de exportación del panel pueden
cambiar independientemente de esta página.

Para automatizar la generación de informes, usa la [Analytics API](/es-419/codex/enterprise/analytics-api)
y sigue su documentación de referencia. Para obtener registros auditables, usa la
[API de Cumplimiento](/es-419/codex/enterprise/compliance-api).

## Interpretar los datos de los informes

Ten en cuenta estos límites:

- La analítica del espacio de trabajo de ChatGPT y la analítica de Codex abarcan ámbitos de producto
distintos.
- Los datos analíticos agregados y los registros de auditoría tienen fines distintos y se rigen por
contratos independientes.
- La analítica describe la actividad; no otorga acceso ni cambia los permisos en tiempo de
ejecución.
- [Los límites de uso y los controles de gasto de ChatGPT](/es-419/codex/enterprise/usage-limits) constituyen
  un límite independiente del espacio de trabajo que depende del plan.
