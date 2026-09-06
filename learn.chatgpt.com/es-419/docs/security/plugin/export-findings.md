<!-- source: https://learn.chatgpt.com/es-419/docs/security/plugin/export-findings -->

Usa un análisis completado de Codex Security para cualquiera de estas transferencias:

- **Exportar** crea un archivo portátil en formato JSON, CSV o SARIF.
- **Dar seguimiento a los hallazgos** prepara los hallazgos seleccionados como issues de Linear, GitHub o Jira
  o como un único borrador privado de aviso de seguridad de GitHub. Codex comprueba si hay
  duplicados y espera tu aprobación antes de escribir.

Ninguno de los dos flujos de trabajo modifica el paquete sellado del análisis.

  Los enlaces disponibles a los artefactos y los formatos de exportación dependen de la interfaz de Codex que uses y
  de la versión instalada del complemento. Consulta el [registro de cambios del
  complemento](/es-419/codex/security/plugin/changelog) antes de usar un formato en una
  automatización.

## Exportar un artefacto portátil

En la App de escritorio, abre un análisis completado desde **Seguridad** \> **Análisis**. Usa los
enlaces disponibles a sus artefactos para inspeccionar `report.md`, `findings.json`,
`scan-manifest.json`, `coverage.json` o un informe SARIF, si está disponible.

Para crear otro formato compatible, pídele a Codex que exporte los hallazgos del
análisis completado sin modificar su paquete sellado:

```text
Export the findings from [completed scan directory] as [JSON, CSV, or SARIF]. Do not modify the sealed scan bundle or upload its contents.

Elige el formato que se adapte a tu destino:

| Formato | Úsalo para                                                        |
| ------ | ----------------------------------------------------------------- |
| JSON   | Conserva los hallazgos estructurados y sellados para usarlos con herramientas y scripts.    |
| CSV    | Revisa los hallazgos y el estado actual de la clasificación local en una hoja de cálculo.  |
| SARIF  | Envía los hallazgos a herramientas que admitan el formato de intercambio SARIF. |

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Abre el artefacto de cobertura, el de hallazgos, el archivo de manifiesto del análisis, el informe Markdown o el artefacto SARIF
de un análisis completado.
  </figcaption>
</figure>

Selecciona **Informe Markdown** para abrir `report.md` en el editor externo
que tengas configurado. El editor depende de la configuración del sistema; en el ejemplo siguiente se muestra el
contenido del informe generado.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Revisa el alcance del análisis, el modelo de amenazas, los hallazgos validados y los enlaces a informes
detallados en el informe Markdown generado.
  </figcaption>
</figure>

Usa la ruta devuelta del artefacto. Si otra herramienta necesita todo el contexto del
análisis, conserva juntos los archivos originales `scan-manifest.json`, `findings.json` y
`coverage.json`. La exportación no sube los hallazgos a un servicio de análisis de
código.

## Dar seguimiento a los hallazgos seleccionados

Ejecuta `$codex-security:track-findings` con un hallazgo validado o un
lote seleccionado explícitamente de hasta 25 hallazgos del mismo análisis sellado. Cada
ejecución usa un solo proveedor y un solo destino. Un borrador privado de aviso de seguridad
de GitHub solo acepta un hallazgo.

Para preparar un issue de Linear, envía:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for the Linear team [team] and project [project, if
any]. Check for duplicates and show me the exact issue title, body, metadata,
and destination. Do not create or update anything until I approve that payload.

Para preparar un Issue de GitHub, envía:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for GitHub repository [owner/repository]. Check open
and closed issues for duplicates and show me the exact issue title, body,
metadata, repository visibility, and authenticated transport. Do not create or
update anything until I approve that payload.

Para preparar un issue de Jira, envía:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for Jira project [project key] as [issue type].
Check for duplicates and show me the exact issue summary, description,
metadata, and destination. Do not create or update anything until I approve
that payload.

El seguimiento en Jira requiere el complemento Atlassian Rovo en Codex. Para reutilizar un issue
se necesita acceso de lectura; para crear o actualizar uno, se necesita acceso de lectura y escritura.

Para preparar un borrador privado de aviso de seguridad de GitHub, envía:

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] as a private draft GitHub Security Advisory in
[owner/repository]. Verify the sealed source revision, repository, affected
paths, package metadata, and duplicate state. Show me the exact advisory
payload, authenticated GitHub CLI identity, and disclosure warnings. Do not
create anything until I approve that payload.

  Los borradores de avisos requieren un hallazgo de un análisis `git_revision` sellado, el
  repositorio de origen canónico, público y verificado y acceso de administrador. El
  flujo de trabajo no procesa avisos en lote ni los actualiza, publica o cierra. Usa un destino privado aprobado
  para issues cuando el repositorio de origen no cumpla esos requisitos.

## Revisar la operación de escritura propuesta

1. Confirma que el ID y la huella digital del hallazgo provienen del análisis sellado previsto.
2. Confirma el proveedor, el equipo específico de Linear, el repositorio de GitHub, el proyecto de Jira o
el repositorio del aviso, así como la visibilidad actual del destino.
3. Revisa el resultado de la comprobación de duplicados: `create`, `reuse`, `update` o `blocked`.
4. Lee en su totalidad el título, el cuerpo, las ubicaciones en el código fuente y los metadatos del proveedor
propuestos. Quita los detalles del exploit o la evidencia interna que el destino
no deba exponer.
5. Aprueba únicamente esa carga útil exacta. Cualquier cambio en el destino, la visibilidad, el conjunto de hallazgos
o el cuerpo requiere una nueva vista previa.

Los hallazgos sensibles deben enviarse a un destino privado. Crear un Issue de GitHub en un
repositorio interno o público requiere una advertencia explícita sobre la visibilidad
y la aprobación de todo el contenido. Da por hecho que la descripción de un borrador de aviso
terminará siendo pública y elimina las credenciales, la evidencia privada y los detalles innecesarios
del exploit antes de dar tu aprobación.

Revisa y aprueba las acciones externas en la conversación de Codex. La aprobación
no crea una pantalla separada para el issue o el aviso en el área de trabajo de Seguridad.

## Verificar el elemento al que se da seguimiento

Después de que apruebes la operación de escritura propuesta, Codex vuelve a comprobar el origen sellado,
el destino, el acceso y el estado de los duplicados. En el caso de un lote, procesa los hallazgos
uno por uno y se detiene ante el primer resultado incierto. La creación, la actualización o
la reutilización solo se completa cuando Codex vuelve a leer el issue exacto y verifica sus
identificadores de vinculación y su contenido.

Conserva la URL canónica devuelta del issue o del aviso junto con tu registro de clasificación.
Continúa con [Corregir y verificar un hallazgo](/es-419/codex/security/plugin/fix-findings)
cuando el responsable acepte el elemento para su corrección.
