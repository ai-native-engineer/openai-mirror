<!-- source: https://learn.chatgpt.com/es-419/docs/security/plugin -->

Codex Security analiza tu código en busca de vulnerabilidades y valida los
hallazgos plausibles. Para cada problema que se pueda reportar, te proporciona la evidencia y las recomendaciones de
corrección necesarias para revisar el resultado. Analiza solo código propio o que tengas
permiso para evaluar.

Sigue esta guía de inicio rápido para instalar el complemento y ejecutar un análisis estándar de solo lectura
de un repositorio local en Codex.

  Esta página describe el plugin de Codex Security en la app de escritorio o Codex CLI. Para
  analizar un repositorio de GitHub conectado en Codex Cloud, consulta la [configuración de Codex Security
  en la nube](/es-419/codex/security/setup).

## Instala el complemento

1. Abre [Codex en la aplicación de escritorio de ChatGPT](/es-419/codex/app).
2. Abre **Complementos**, busca **Codex Security** o usa el botón que aparece a continuación:

   <div className="not-prose my-6">
     
       Instalar el plugin de Codex Security
     
   </div>

3. Confirma que el complemento esté habilitado y luego abre **Seguridad** en la barra lateral.

1. En tu terminal, ve al repositorio que quieres evaluar e inicia Codex:

   ```bash
   codex

2. Ingresa `/plugins`, busca **Codex Security** y selecciona **Instalar
   complemento**.
3. Ingresa `/new` para iniciar un chat nuevo para el repositorio.

Para instalar Codex Security en un repositorio local, usa la aplicación de escritorio de ChatGPT
o Codex CLI.

  Consulta el [registro de cambios del complemento](/es-419/codex/security/plugin/changelog) antes de depender
  de una función o iniciar un análisis de larga duración. Si **Seguridad** no aparece en
  la barra lateral de la app de escritorio, actualiza la app y el complemento y confirma que el complemento
  esté habilitado.

## Ejecuta tu primer análisis

Para obtener la mejor calidad de análisis, usa <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
con un esfuerzo de razonamiento `xhigh`.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Elige un repositorio y configura un análisis de seguridad nuevo antes de iniciarlo.
  </figcaption>
</figure>

1. Abre la configuración del análisis

   Selecciona **Seguridad** en la barra lateral, abre **Análisis** y selecciona **+ Análisis**.

2. Elige la base de código y el área de análisis

   Selecciona un repositorio existente o usa otra carpeta. Elige **Base de código**,
   deja **Análisis profundo** desactivado y selecciona todo el repositorio o una carpeta.
   Confirma que la rama y la revisión correspondan al código que querías analizar.

3. Agrega contexto relevante

   Elige el modelo y el esfuerzo de razonamiento. Abre **Contexto adicional** solo cuando
   necesites describir un vector de ataque específico, un área sensible en materia de seguridad o un
   detalle del repositorio que deba orientar la revisión.

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       Activa el contexto adicional para describir vectores de ataque, áreas en las que centrarse y
pautas de seguridad relevantes.
     </figcaption>
   </figure>

4. Inicia el análisis

   Selecciona **Iniciar análisis** y sigue las fases del análisis en el entorno de trabajo de Seguridad.
   Selecciona **Ver actividad** para examinar la tarea de Codex que ejecuta el análisis.

5. Revisa el resultado

   Abre el análisis completado para examinar los hallazgos, la cobertura y los artefactos
   de informe disponibles. Usa **Hallazgos** para revisar problemas de distintos análisis o **Repositorios**
   para consultar el historial de análisis de un repositorio.

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       Revisa los resultados, los hallazgos y la cobertura del análisis en el entorno de trabajo de Seguridad.
     </figcaption>
   </figure>

1. Solicita un análisis estándar

   Envía este prompt en el chat nuevo:

   ```text
   Run a Codex Security scan on this repository.

2. Deja que finalice el análisis

   Codex ejecuta el análisis en la terminal sin abrir un espacio de trabajo de configuración. Mantén
la tarea en ejecución hasta que Codex informe que finalizó. Si Codex identifica
una limitación de configuración, revisa esa limitación y el cambio exacto propuesto
antes de aprobar una actualización de la configuración.

3. Revisa el resultado

   Revisa el resumen en la terminal y luego abre el archivo `report.md` generado para
   ver el resultado completo.

Ejecuta este flujo de trabajo local del complemento en la aplicación de escritorio de ChatGPT o Codex CLI.

## Qué crea el análisis

Los análisis completados siguen disponibles en **Análisis**. Revisa sus hallazgos y
su cobertura en el entorno de trabajo de Seguridad, o consulta los hallazgos relacionados y el historial del repositorio
en **Hallazgos** y **Repositorios**. El análisis también crea los archivos
que se indican a continuación.

Cada análisis completado muestra un resumen en la terminal y crea los archivos
que se indican a continuación.

Ejecuta este flujo de trabajo local del complemento en la aplicación de escritorio de ChatGPT o Codex CLI.

- `report.md`, el archivo principal para consultar los resultados del análisis.
- `findings/<slug>/`, cuando haya informes detallados de vulnerabilidades y archivos
  de prueba de concepto que los respalden.
- `hardening/`, cuando haya recomendaciones de refuerzo de seguridad a nivel estructural y propuestas o
  diagramas de apoyo.
- Datos estructurados del análisis en `scan-manifest.json`, `findings.json` y
`coverage.json` para la automatización y las integraciones. Puedes revisar los resultados del análisis
  sin abrir estos archivos.

Conserva completo el directorio del análisis cuando compartas o archives los resultados para que
los enlaces de `report.md` sigan funcionando.

## Elige tu siguiente flujo de trabajo

- [Usa el entorno de trabajo de Seguridad](/es-419/codex/security/plugin/workbench) para administrar
  los análisis guardados, los hallazgos, los repositorios y la actividad de análisis en la app de escritorio.
- [Ejecuta un análisis desde la CLI](/es-419/codex/security/cli) si tienes acceso a la beta y
  necesitas un flujo de trabajo repetible en la terminal con resultados estructurados.
- [Ejecuta un análisis estándar o de alcance limitado](/es-419/codex/security/plugin/scans) para revisar un
  repositorio o una carpeta con el flujo de trabajo predeterminado.
- [Evalúa un primer análisis](/es-419/codex/security/plugin/scans#assess-a-first-scan)
  para comparar los resultados con problemas conocidos y decidir cuándo volver a analizar.
- [Ejecuta un análisis profundo](/es-419/codex/security/plugin/deep-scans) para realizar un análisis más exhaustivo
  cuando puedas permitir un tiempo de ejecución más prolongado.
- [Revisa los cambios en el código](/es-419/codex/security/plugin/code-changes) para evaluar un Pull Request,
  un commit, un rango de ramas o un parche del árbol de trabajo.
- [Clasifica y prioriza un backlog](/es-419/codex/security/plugin/triage-backlog) para revisar los hallazgos
  de seguridad existentes.
- [Corrige y verifica un hallazgo](/es-419/codex/security/plugin/fix-findings) después de
  aceptar un hallazgo para su corrección.
- [Exporta hallazgos o dales seguimiento](/es-419/codex/security/plugin/export-findings) para crear
  JSON, CSV, SARIF, un issue en Linear, GitHub o Jira con aprobación previa, o un borrador
  privado de GitHub Security Advisory.
- [Crea informes de vulnerabilidades](/es-419/codex/security/plugin/vulnerability-reports)
  para convertir los hallazgos, las notas de divulgación, el código fuente y las PoCs proporcionados en
  informes autocontenidos.
- [Propón medidas de refuerzo de seguridad](/es-419/codex/security/plugin/security-hardening) para
  considerar opciones estructurales o arquitectónicas a partir de los resultados del análisis u otras
  evidencias de seguridad.
