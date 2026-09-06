<!-- source: https://learn.chatgpt.com/es-419/use-cases/deep-security-scan -->

## Elige una revisión exhaustiva del repositorio

Usa un análisis exhaustivo cuando necesites una revisión de vulnerabilidades más completa en
un repositorio o una carpeta indicada explícitamente y puedas destinar recursos a una ejecución más prolongada. El Plugin de Codex
Security realiza varias iteraciones de detección antes de validar y priorizar los
hallazgos, por lo que este flujo de trabajo requiere más tiempo y recursos que un análisis convencional.

Un análisis exhaustivo puede revisar un repositorio completo o un paquete o
directorio indicado explícitamente. Para revisar un Pull Request, un Commit, las diferencias de una Rama o un parche del árbol de trabajo,
usa
[$codex-security:security-diff-scan](/es-419/codex/use-cases/scan-code-changes-for-security).

## Prepara un análisis con autorización

1. Abre el repositorio en Codex y completa el [Inicio rápido del Plugin de Codex Security](/es-419/codex/security/plugin).
2. Confirma que el repositorio sea de tu propiedad o que tengas autorización para evaluarlo.
3. Agrega directrices sobre la arquitectura, los límites de confianza, los invariantes de seguridad, los criterios para los hallazgos,
   las exclusiones y la severidad en `SECURITY.md`. Usa archivos `SECURITY.md`
   anidados para definir políticas específicas de cada directorio.
4. Mantén los comandos admitidos de compilación, pruebas y validación, así como las demás instrucciones
   del repositorio en `AGENTS.md`.
5. Ejecuta el prompt inicial y permite que el análisis complete sus etapas de detección iterativa,
validación, análisis de rutas de ataque y elaboración del informe final.
6. Revisa el Espacio de trabajo de los hallazgos, el informe y cualquier vacío de evidencia. Solicita informes detallados
sobre las vulnerabilidades u orientación para el fortalecimiento estructural cuando los necesites.

## Revisa la evidencia antes de iniciar la corrección

El resultado final debe identificar las ubicaciones afectadas, explicar por qué se puede
llegar a ese comportamiento, indicar qué validación realizó Codex, señalar los vacíos de evidencia restantes y proponer un
enfoque de corrección acotado. Distingue los hallazgos sin evidencia de validación
de los hallazgos validados.

Inicia la corrección solo de un hallazgo que hayas seleccionado y revisado. Usa
[Corregir una lista de vulnerabilidades pendientes](/es-419/codex/use-cases/remediate-vulnerability-backlog)
para corregir los hallazgos uno por uno con una validación de regresión específica.

Para obtener información sobre la configuración, las comprobaciones previas, los objetivos delimitados y la duración esperada de la ejecución, consulta [Ejecuta un análisis de
seguridad exhaustivo](/es-419/codex/security/plugin/deep-scans).
