<!-- source: https://learn.chatgpt.com/es-419/docs/security/plugin/workbench -->

El área de trabajo de Seguridad reúne tus análisis, hallazgos y repositorios
en la App de escritorio de Codex. Codex realiza el análisis en una tarea normal, mientras que
el área de trabajo mantiene el análisis y sus resultados disponibles para cuando regreses.

En la Aplicación de escritorio de ChatGPT, abre el menú desplegable de ChatGPT y selecciona **Codex**.
Instala y habilita el [Plugin de Codex Security](/es-419/codex/security/plugin) y luego
selecciona **Seguridad** en la barra lateral.

  Si no aparece **Seguridad** , confirma que **Codex** esté seleccionado y que el
  plugin esté instalado y habilitado. Si es necesario, actualiza la App de escritorio y el plugin,
  y comprueba si el administrador de tu espacio de trabajo permite usar el plugin.

## Iniciar un análisis

Para obtener la mejor calidad de análisis, usa <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
con el nivel de razonamiento `xhigh`.

1. Abre **Análisis** y selecciona **+ Análisis**.
2. Selecciona un repositorio existente o elige otra carpeta.
3. Elige **Base de código** para analizar un repositorio o **Cambios** para revisar un
   cambio basado en Git.
4. Para un análisis estándar de la base de código, selecciona todo el repositorio o una carpeta.
5. Para realizar un análisis profundo, primero selecciona el repositorio o la carpeta como base de código y luego
   activa **Análisis profundo**. Los análisis profundos revisan toda la base de código seleccionada.
6. Para analizar cambios, selecciona cambios sin confirmar, un commit o un rango de
   revisiones. **Análisis profundo** no está disponible para los análisis de cambios.
7. Elige un modelo y un nivel de razonamiento. Abre **Contexto adicional** para describir
   vectores de ataque relevantes, áreas de interés u otro contexto de seguridad.
8. Selecciona **Iniciar análisis**.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Elige un repositorio y configura un análisis en el área de trabajo de Seguridad.
  </figcaption>
</figure>

Consulta [Ejecuta un análisis de seguridad](/es-419/codex/security/plugin/scans), [Ejecuta un análisis profundo de
seguridad](/es-419/codex/security/plugin/deep-scans) o [Revisa los cambios en el código por motivos de
seguridad](/es-419/codex/security/plugin/code-changes) para obtener detalles sobre cada tipo de
análisis.

## Seguir el progreso del análisis

La página del análisis muestra la fase actual y cualquier avance que informe el plugin.
En un análisis estándar, las fases incluyen el modelado de amenazas, el descubrimiento, la validación,
el análisis del impacto y de las rutas, la generación de informes y la finalización.

Selecciona **Ver actividad** para abrir la tarea de Codex que ejecuta el análisis. Puedes
salir del área de trabajo y volver a **Análisis** sin perder un análisis guardado. Para detener
el proceso de forma intencional, abre el análisis y selecciona **Detener análisis**.

Cuando finalice el análisis, abre sus resultados para revisar el objetivo, la revisión,
los hallazgos, la cobertura y los artefactos del informe disponibles.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Revisa los hallazgos, la gravedad, la cobertura del análisis y los artefactos cuando este
finalice.
  </figcaption>
</figure>

## Revisar los hallazgos de distintos análisis

Abre **Hallazgos** para inspeccionar los hallazgos guardados de distintos repositorios y análisis.
Busca en la lista o fíltrala; luego, selecciona un hallazgo para revisar su resumen, la evidencia
del código fuente, la validación y el impacto.

Usa **Resumen** para ver los detalles del hallazgo y **Parche** cuando quieras generar,
revisar, aplicar o verificar una corrección puntual. Consulta [Corregir y verificar hallazgos de
seguridad](/es-419/codex/security/plugin/fix-findings) para conocer el flujo de trabajo de remediación.

  La pestaña **Hallazgos** muestra los hallazgos de los análisis guardados de Codex Security. Los tickets
  importados y otros problemas de seguridad existentes siguen formando parte de un
[flujo de trabajo de clasificación del backlog](/es-419/codex/security/plugin/triage-backlog) independiente.

## Inspeccionar el historial del repositorio

Abre **Repositorios** para explorar los repositorios y las carpetas disponibles. Selecciona un
repositorio para inspeccionar su historial de análisis, la revisión analizada más reciente y los
hallazgos abiertos. Desde los detalles del repositorio, abre un análisis anterior o consulta los hallazgos
asociados con ese repositorio.

Si un repositorio no tiene análisis, inicia uno desde sus detalles o selecciona **+ Análisis**
en el área de trabajo.

## Iniciar un análisis desde una conversación

También puedes pedirle a Codex que ejecute el Plugin de Codex Security instalado en una conversación
normal. Los análisis que usan el área de trabajo compartida del plugin aparecen en **Análisis**,
por lo que puedes volver a consultar su progreso y sus resultados desde el área de trabajo de Seguridad.

Para los análisis y la automatización mediante la Terminal, consulta el [Inicio rápido
de la CLI de Codex Security](/es-419/codex/security/cli).
