<!-- source: https://learn.chatgpt.com/es-419/docs/enterprise/compliance-api -->

Usa la API de Cumplimiento para flujos de trabajo de seguridad, asuntos legales, gobernanza e investigación
que requieran registros auditables. Usa la analítica, no los registros de cumplimiento,
para medir la adopción y las tendencias.

La [referencia de la API de administración](https://chatgpt.com/public/admin/api-reference)
es la fuente oficial sobre los requisitos de acceso vigentes, la cobertura de eventos, las rutas,
los esquemas, los filtros, la retención y el comportamiento de las solicitudes.

Para obtener una descripción general de las interfaces de cumplimiento disponibles y los patrones de integración
habituales, consulta la [guía de la Plataforma de cumplimiento](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

## Cuándo usar la API de Cumplimiento

La API de Cumplimiento es adecuada cuando necesitas:

- Exportar los registros admitidos a un sistema de auditoría o investigación.
- Aplicar los procesos de retención y conservación por motivos legales de la organización.
- Correlacionar la actividad de Codex con otros datos de seguridad o identidad.
- Respaldar investigaciones aprobadas de seguridad, asuntos legales o gobernanza.

No es un panel de productividad. No la uses para inferir la calidad del código ni
el desempeño individual. Usa la [Analítica del espacio de trabajo](/es-419/codex/enterprise/workspace-analytics)
o la [Analytics API](/es-419/codex/enterprise/analytics-api) para generar informes sobre la adopción.

## Primeros pasos

1. Abre la [referencia de la API de administración](https://chatgpt.com/public/admin/api-reference) y
   confirma que tu rol de administrador pueda acceder a los recursos de cumplimiento
   que necesitas.
2. Usa el flujo de registros de cumplimiento, que solo permite agregar entradas, para la recopilación continua. Consulta la
referencia de la API para conocer los recursos y los patrones de recuperación
admitidos actualmente.
3. [Descarga los archivos de registro](#download-logs) y prueba, fuera de producción, la ingesta en un sistema
   de gestión de información y eventos de seguridad (SIEM) o en un lago de datos.
4. Programa la recopilación continua y aplica los controles de acceso,
retención y conservación por motivos legales de tu organización a los registros exportados. No supongas que el
período de retención en origen sustituye la política de retención de tu organización.

Por ejemplo, un equipo de seguridad puede transmitir de forma continua eventos de cumplimiento inmutables a su
SIEM para realizar investigaciones o enviar esos eventos a un flujo de trabajo aprobado de descubrimiento
electrónico. Consulta la referencia de la API para conocer las rutas y los
esquemas vigentes, en lugar de copiar de esta guía el contrato de un punto de acceso.

### Descargar registros

Descarga el [script de Bash](/downloads/compliance-api/download_compliance_files.sh)
o el [script de PowerShell](/downloads/compliance-api/download_compliance_files.ps1).
Ambos enumeran y descargan todos los archivos de registro disponibles posteriores a una marca de tiempo determinada, siguen
la paginación y escriben JSONL en la salida estándar. Los errores se envían a la salida de error estándar.

Asigna a `COMPLIANCE_API_KEY` tu clave de la API de Cumplimiento para Empresas. Reemplaza
`<workspace_or_org_id>` por el ID de tu espacio de trabajo de ChatGPT o el ID de tu organización en la Plataforma API,
y `<after>` por una marca de tiempo ISO 8601 que incluya una zona
horaria. Este ejemplo recupera archivos `AUTH_LOG` en grupos de 100.

En macOS o Linux, instala Bash, `curl` y `jq` y luego ejecuta:

```bash
bash ./download_compliance_files.sh "<workspace_or_org_id>" AUTH_LOG 100 "<after>" > output.jsonl

El script para Windows es compatible con PowerShell 5.1 o posterior. Revisa el archivo descargado.
Si Windows lo bloquea y la política de ejecución de tu organización lo permite, ejecuta
`Unblock-File -Path .\download_compliance_files.ps1`. Este ejemplo usa
PowerShell 7 para guardar en UTF-8 sin marca de orden de bytes:

```powershell
.\download_compliance_files.ps1 "<workspace_or_org_id>" AUTH_LOG 100 "<after>" |
  Set-Content -Encoding utf8NoBOM output.jsonl

## Confirmar los límites administrativos

La cobertura de cumplimiento abarca el espacio de trabajo de ChatGPT y los productos incluidos
en la referencia vigente de la API. Los datos de la organización en la Plataforma API se rigen
por sus propios controles de datos y administración de la API.

La referencia de la API define las rutas vigentes, la cobertura de eventos, los esquemas,
los filtros, el comportamiento de retención, los requisitos de permisos y el funcionamiento de las solicitudes.
Esta página no reproduce ese contrato.

## Documentación relacionada

- [Analítica del espacio de trabajo](/es-419/codex/enterprise/workspace-analytics)
- [Guía de implementación para administradores](/es-419/codex/enterprise/admin-setup)
- [Gobernanza](/es-419/codex/enterprise/governance)
- [Analytics API](/es-419/codex/enterprise/analytics-api)
