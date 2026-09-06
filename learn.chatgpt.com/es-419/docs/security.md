<!-- source: https://learn.chatgpt.com/es-419/docs/security -->

Codex Security es un agente de seguridad de aplicaciones que ayuda a los equipos de seguridad y
de ingeniería a detectar, confirmar y corregir vulnerabilidades. Úsalo en
Codex, desde tu terminal, mediante el SDK de TypeScript o con repositorios de GitHub
conectados.

Para un primer análisis local guiado, comienza con el [inicio rápido
del Plugin de Codex Security](/es-419/codex/security/plugin).

## Usar Codex Security en la app de escritorio

En la aplicación de escritorio de ChatGPT, abre el menú desplegable de ChatGPT y selecciona **Codex**.
Instala y habilita el Plugin de Codex Security para abrir **Seguridad** en la
barra lateral. El entorno de trabajo de Seguridad reúne tus análisis, hallazgos y repositorios en
un solo lugar mientras Codex ejecuta cada análisis en una tarea.

- Usa **Análisis** para iniciar análisis, seguir su progreso y revisar los resultados guardados.
- Usa **Hallazgos** para examinar los problemas y la evidencia de los análisis completados.
- Usa **Repositorios** para revisar el historial de los repositorios y los hallazgos abiertos.

Consulta [Usa el entorno de trabajo de Seguridad](/es-419/codex/security/plugin/workbench) para conocer el
flujo de trabajo completo de la app de escritorio.

### Explorar los casos de uso del plugin

- [Ejecuta un análisis de seguridad](/es-419/codex/security/plugin/scans) en un repositorio o una carpeta específica.
- [Ejecuta un análisis de seguridad profundo](/es-419/codex/security/plugin/deep-scans) cuando necesites una revisión más amplia y puedas esperar más tiempo a que termine.
- [Revisa los cambios en el código](/es-419/codex/security/plugin/code-changes) antes de fusionar un Pull Request o una rama.
- [Clasificar y priorizar un backlog](/es-419/codex/security/plugin/triage-backlog) cuando ya tengas hallazgos de seguridad que revisar.
- [Corrige y verifica los hallazgos](/es-419/codex/security/plugin/fix-findings) con parches acotados para los hallazgos aprobados.
- [Exporta los hallazgos o hazles seguimiento](/es-419/codex/security/plugin/export-findings) como artefactos portátiles o en destinos de seguimiento sujetos a aprobación.
- [Crear informes de vulnerabilidades](/es-419/codex/security/plugin/vulnerability-reports) a partir de los hallazgos, las notas de divulgación, el código fuente y los PoCs proporcionados.
- [Proponer medidas de refuerzo de seguridad](/es-419/codex/security/plugin/security-hardening) a partir de los resultados de los análisis u otra evidencia de seguridad.
- [Consulta las novedades](/es-419/codex/security/plugin/changelog) del Plugin de Codex Security.

  El entorno de trabajo de Seguridad de la app de escritorio y Codex CLI usan el Plugin de Codex Security.
  Codex Security en la nube analiza repositorios de GitHub conectados mediante Codex Cloud.
  Para obtener información sobre el entorno aislado de Codex, las aprobaciones, los controles de red y la configuración para administradores, consulta
[Aprobaciones del agente y seguridad](/es-419/codex/agent-approvals-security).

## CLI y SDK de Codex Security

La CLI y el SDK de TypeScript están disponibles en el paquete público
[`@openai/codex-security`](https://github.com/openai/codex-security).
Ejecuta la CLI con `npx`:

```bash
npx @openai/codex-security --help

Para ejecutar análisis, necesitas acceso a Codex Security. Para obtener los mejores resultados, usa una cuenta
verificada para [Trusted Access for Cyber](https://chatgpt.com/cyber).

Usa el mismo analizador que el plugin en distintos repositorios y a lo largo del tiempo. La CLI
descubre repositorios de GitHub, reanuda análisis por lotes, hace un seguimiento de los hallazgos
entre análisis y registra comentarios sobre falsos positivos. Agrega tu arquitectura y tus políticas
de seguridad, establece un límite de costo estimado o ejecuta comprobaciones en CI y antes de los commits.
Usa el SDK de TypeScript para incorporar análisis, informes de progreso y controles de costos
en una aplicación o herramienta para desarrolladores.

- [Comienza con el inicio rápido de la CLI](/es-419/codex/security/cli) para configurar la CLI,
  realizar una comprobación previa de un repositorio y ejecutar un análisis local.
- [Ejecuta análisis de seguridad por lotes](/es-419/codex/security/cli/bulk-scans) para descubrir repositorios de GitHub
  o ejecutar una campaña reanudable a partir de un inventario CSV.
- [Ejecuta análisis en CI](/es-419/codex/security/cli/ci) para revisar los cambios en los Pull requests,
  conservar artefactos, cargar SARIF y establecer una política de gravedad.
- [Consulta las preguntas frecuentes sobre la CLI](/es-419/codex/security/cli/faq) para obtener respuestas sobre el historial de análisis,
  los comentarios sobre falsos positivos, la cobertura y la verificación de correcciones.
- [Usa la referencia de la CLI](/es-419/codex/security/cli/reference) para consultar los
  comandos, las opciones, los formatos de salida, los artefactos y los códigos de salida compatibles.
- [Integra el SDK de TypeScript](/es-419/codex/security/sdk) para seleccionar objetivos,
  examinar resultados, seguir el progreso y cancelar análisis desde el código.

## Codex Security en la nube

Codex Security en la nube se encuentra actualmente en versión preliminar de investigación. Analiza repositorios de
GitHub conectados para detectar posibles problemas de seguridad.

Ayuda a los equipos a:

1. **Detectar posibles vulnerabilidades** mediante un modelo de amenazas específico del repositorio y el contexto real del código.
2. **Reducir el ruido** al validar los hallazgos antes de que los revises.
3. **Avanzar hacia la corrección de los hallazgos** con resultados priorizados, evidencia y opciones de parches sugeridas.

## Cómo funciona Codex Security en la nube

Codex Security analiza los repositorios conectados commit por commit.
Crea el contexto del análisis a partir de tu repositorio, contrasta las posibles vulnerabilidades con ese contexto y valida los problemas con indicios sólidos en un entorno aislado antes de mostrarlos.

Obtienes un flujo de trabajo centrado en:

- el contexto específico del repositorio en lugar de firmas genéricas
- evidencia de validación que ayuda a reducir los falsos positivos
- correcciones sugeridas que puedes revisar en GitHub

## Acceso y requisitos previos de Codex Security en la nube

Codex Security en la nube funciona con repositorios de GitHub conectados mediante
Codex Cloud. Si un repositorio no aparece, confirma que esté disponible en tu
espacio de trabajo de Codex Cloud o comunícate con el equipo de OpenAI asignado a tu cuenta.

## Documentación relacionada

- En [Inicio rápido del Plugin de Codex Security](/es-419/codex/security/plugin) se explican paso a paso la instalación y un primer análisis local.
- En [Entorno de trabajo de Seguridad](/es-419/codex/security/plugin/workbench) se explican los análisis guardados, los hallazgos, los repositorios y la actividad de análisis en la app de escritorio.
- En [Inicio rápido de la CLI de Codex Security](/es-419/codex/security/cli) se explican paso a paso la configuración, la comprobación previa y un primer análisis desde la terminal.
- [Ejecuta análisis de seguridad por lotes](/es-419/codex/security/cli/bulk-scans) explica el descubrimiento de repositorios de GitHub, los inventarios CSV, los resultados de las campañas y el funcionamiento de la reanudación.
- En [Preguntas frecuentes sobre la CLI de Codex Security](/es-419/codex/security/cli/faq) encontrarás respuestas a preguntas comunes sobre análisis, hallazgos, cobertura y costos.
- En [SDK de TypeScript de Codex Security](/es-419/codex/security/sdk) se explica cómo ejecutar análisis desde una aplicación o herramienta para desarrolladores.
- En [Configuración de Codex Security en la nube](/es-419/codex/security/setup) se detallan la configuración, los análisis y la revisión de hallazgos.
- En [Revisión de seguridad](/es-419/codex/security/security-review) se explica cómo realizar revisiones de seguridad exhaustivas en Pull requests de GitHub.
- En [Mejorar el modelo de amenazas](/es-419/codex/security/threat-model) se explica cómo ajustar el alcance, los puntos de entrada y los supuestos de criticidad.
- En [Preguntas frecuentes sobre Codex Security en la nube](/es-419/codex/security/faq) se abordan preguntas comunes sobre el producto en la nube.
