<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/governance -->

La gobernanza de la actividad de Codex abarca analítica interactiva, generación programática
de informes, controles relacionados con el uso de ChatGPT y registros de auditoría. Elige la
herramienta que corresponda a cada cuestión; los datos de analítica y cumplimiento tienen
finalidades distintas.

<a id="governance-and-observability"></a>
<a id="ways-to-track-codex-usage"></a>

| Si necesitas                                          | Empieza por                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------- |
| Comprender la adopción en ChatGPT                      | [Analítica del espacio de trabajo](/es-419/codex/enterprise/workspace-analytics)              |
| Revisar de forma interactiva la adopción y la actividad de Codex        | [Analítica de Codex](#analytics-dashboard)                                   |
| Cargar informes agregados de Codex en otro sistema     | [Analytics API](/es-419/codex/enterprise/analytics-api)                          |
| Exportar registros para auditorías o investigaciones               | [API de Cumplimiento](/es-419/codex/enterprise/compliance-api)                        |
| Revisar los controles de créditos del espacio de trabajo de ChatGPT según el plan | [Límites de uso y controles de gasto de ChatGPT](/es-419/codex/enterprise/usage-limits) |

## Abrir las herramientas de administración

- Abre [Analítica del espacio de trabajo](https://chatgpt.com/admin/usage) para consultar de forma interactiva
  los informes del espacio de trabajo. La [guía de analítica del espacio de trabajo](https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu)
  describe los roles y las vistas actuales.
- Abre la [referencia de la Analytics API de Codex](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)
  cuando necesites programar la generación de informes mediante código.
- Abre la [referencia de la API de administración](https://chatgpt.com/public/admin/api-reference)
  y la [guía de la Plataforma de cumplimiento](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)
  para las integraciones de auditoría e investigación.

Por ejemplo, usa la analítica del espacio de trabajo para comprobar rápidamente la adopción, la Analytics API
para cargar informes agregados de Codex en un sistema de inteligencia empresarial,
y la API de Cumplimiento para enviar registros auditables a un SIEM o a un flujo de trabajo
de descubrimiento electrónico.

## Panel de analítica

<a id="dashboard-views"></a>
<a id="data-export"></a>

ChatGPT ofrece analítica de todo el espacio de trabajo para obtener una visión general de la adopción y la participación.
La analítica de Codex se centra en la actividad de Codex. Ambas son herramientas interactivas de
informes, no registros de auditoría sin procesar.

Usa [Analítica del espacio de trabajo](/es-419/codex/enterprise/workspace-analytics) para comparar las
dos experiencias y encontrar las fuentes actuales que mantienen sus responsables. También puedes
abrir [Analítica del espacio de trabajo](https://chatgpt.com/admin/usage) directamente. No
definas un contrato estable de generación de informes a partir de las etiquetas del panel ni de los
campos de los informes descargados; estos pueden cambiar a medida que evoluciona el producto.

## Controles relacionados con el uso de ChatGPT

Los controles de uso del espacio de trabajo de ChatGPT son independientes de la analítica y no
configuran los derechos de acceso a las funciones. Según el plan, la actividad elegible de Codex
puede consumir créditos del espacio de trabajo de ChatGPT y, si se alcanzan los límites, puede pausarse el acceso a
las funciones elegibles. Estos controles no establecen un límite universal de Codex ni rigen
la facturación de la Plataforma API.

Consulta [Límites de uso y controles de gasto de ChatGPT](/es-419/codex/enterprise/usage-limits)
para conocer el alcance que se mantiene estable y consultar las fuentes actuales del Centro de ayuda.

## Analytics API

<a id="what-it-measures"></a>
<a id="endpoints"></a>
<a id="usage"></a>
<a id="code-review-activity"></a>
<a id="user-engagement-with-code-review"></a>
<a id="how-it-works"></a>
<a id="common-use-cases"></a>

Usa la Analytics API para generar de forma programática informes agregados de Codex. Es
adecuada para almacenes de datos, sistemas de inteligencia empresarial y procesos internos
de generación de informes que no deban depender de un panel interactivo.

La referencia de la API es la fuente oficial sobre los requisitos de acceso, las rutas, los esquemas,
los campos, los períodos de los informes y la paginación. Consulta
[Analytics API](/es-419/codex/enterprise/analytics-api) para conocer el alcance conceptual de la integración
y encontrar el enlace a la referencia canónica.

## API de Cumplimiento

<a id="what-it-measures-1"></a>
<a id="what-you-can-export"></a>
<a id="activity-logs"></a>
<a id="metadata-for-audit-and-investigation"></a>
<a id="common-use-cases-1"></a>
<a id="what-it-does-not-provide"></a>

Usa la API de Cumplimiento para flujos de trabajo de seguridad, legales y de gobernanza que requieran
registros auditables. No es un panel de adopción ni de productividad.

La referencia de la API es la fuente oficial sobre la cobertura de eventos, los esquemas, los permisos,
los filtros, la retención y el comportamiento de las solicitudes. Consulta
[API de Cumplimiento](/es-419/codex/enterprise/compliance-api) para conocer el alcance conceptual
de la integración y encontrar el enlace a la referencia canónica.

<a id="recommended-pattern"></a>

Para definir la secuencia de implementación y realizar verificaciones en estas herramientas, usa la
[Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup).

## Documentación relacionada

- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
- [Analítica del espacio de trabajo](/es-419/codex/enterprise/workspace-analytics)
- [Analytics API](/es-419/codex/enterprise/analytics-api)
- [API de Cumplimiento](/es-419/codex/enterprise/compliance-api)
