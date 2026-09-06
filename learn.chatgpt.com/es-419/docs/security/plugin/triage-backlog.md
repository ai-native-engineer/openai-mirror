<!-- source: https://learn.chatgpt.com/es-419/docs/security/plugin/triage-backlog -->

Usa `$codex-security:triage-finding` para revisar los hallazgos de seguridad existentes
con respecto al repositorio actual. Este flujo de trabajo realiza un análisis estático
de solo lectura: Codex considera cada hallazgo una afirmación aún no demostrada e inspecciona
la evidencia del repositorio sin ejecutar el código.

Ejecuta este flujo de trabajo desde un proyecto de Codex asociado al repositorio que quieras
evaluar. Codex debe poder leer el código fuente del repositorio. Los conectores de Jira y Linear
pueden proporcionar datos de los hallazgos, mientras que los hallazgos de GitHub requieren acceso REST autenticado
a GitHub. Ninguna de estas opciones sustituye el acceso al código fuente.

Internamente, Codex comienza por el código citado o la información de versión indicada.
Rastrea la fuente presuntamente controlada por un atacante, los controles de seguridad pertinentes,
el sumidero peligroso y la ruta alcanzable. También comprueba la superficie del producto y el límite de
confianza, busca evidencia contradictoria y registra los vacíos de prueba. Luego, Codex devuelve
un veredicto por hallazgo y ordena por prioridad los hallazgos que requieren alguna medida o una
revisión adicional.

Esto difiere de `$codex-security:validation`, que puede compilar o ejecutar código,
crear una prueba específica o una prueba de concepto, o interactuar con una interfaz real para
reproducir o refutar un hallazgo. Usa este proceso para clasificar y priorizar
un backlog existente. Usa la validación cuando la evidencia obtenida en tiempo de ejecución pueda resolver un hallazgo
que la evidencia estática no permite aclarar.

  El proceso de clasificación y priorización del backlog parte de hallazgos existentes. Para buscar nuevas
  vulnerabilidades en el repositorio, [ejecuta un análisis de seguridad](/es-419/codex/security/plugin/scans). Este proceso
  no modifica el repositorio ni implementa correcciones.

## Elegir los hallazgos que se clasificarán y priorizarán

Puedes proporcionar un hallazgo o un conjunto de hallazgos de estas fuentes:

| Fuente                   | Qué proporcionar                                                                                                                                                                                                                                                                                                                                                                                                                                        | Requisitos                                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Hallazgos pegados o locales | Resultados SARIF, un CVE o GHSA, un aviso, un ticket de un escáner, un informe de un programa de recompensas por la detección de errores, un artefacto de un hallazgo de Codex Security o una afirmación sobre una vulnerabilidad en lenguaje claro.                                                                                                                                                                                                                                                                                          | No se requiere ningún conector.                                                                                                                                                                           |
| Jira o Linear           | URL o identificadores exactos de incidencias de seguridad o vulnerabilidades, una consulta JQL de Jira, o un equipo, proyecto o frase de búsqueda de Linear. Codex recupera el contenido de las incidencias seleccionadas antes de clasificarlas y priorizarlas.                                                                                                                                                                                                                                                                            | [Jira mediante Atlassian Rovo](codex://plugins/plugin_connector_692de805e3ec8191834719067174a384) o [Linear](codex://plugins/plugin_asdk_app_69a089a326dc8191b32a3f2553f5be2c) con permiso de lectura. |
| GitHub                   | Un repositorio y una fuente de hallazgos: análisis de código, vulnerabilidades y malware de `Dependabot`, avisos de seguridad e informes privados de vulnerabilidades, o todas las fuentes. Si no especificas un repositorio, Codex usa, cuando está disponible, el repositorio de GitHub adjunto al proyecto actual de Codex. Los Issues de GitHub no se incluyen entre las fuentes predeterminadas de GitHub; proporciona un Issue de GitHub específico o solicita explícitamente los Issues de GitHub cuando quieras clasificarlos y priorizarlos. | Acceso REST autenticado a GitHub, como `gh auth token`, `GH_TOKEN` o `GITHUB_TOKEN`, con permiso para leer el repositorio y el tipo de hallazgo seleccionados.                                      |

Codex conserva un resultado por cada hallazgo proporcionado, en el orden de entrada, para que cada
hallazgo se pueda rastrear hasta su fuente. No combina ni descarta hallazgos que parezcan
duplicados.

## Ejecutar el proceso de clasificación y priorización de solo lectura

Para hallazgos pegados o artefactos locales, envía un prompt como este:

```text
Use $codex-security:triage-finding to triage these existing security findings against this repository:

[Paste the findings or provide the artifact path.]

Para incidencias de Jira o Linear, identifica el conjunto de incidencias y mantén el sistema de origen
en modo de solo lectura:

```text
Use $codex-security:triage-finding to import and triage the security findings from [Jira or Linear issue URLs, identifiers, or query] against this repository.
Do not change the source issues.

Para los hallazgos de GitHub, indica el repositorio y la fuente:

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from [owner/repository] against this repository.

Para usar el repositorio de GitHub adjunto al proyecto actual de Codex, especifica
solo la fuente de los hallazgos:

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from GitHub against this repository. Use the GitHub repository attached to the current Codex project.

El flujo de trabajo sigue este orden:

1. Recopilar y organizar los hallazgos

   Codex recupera el contenido solicitado de las incidencias o de GitHub, conserva los
identificadores y las referencias de origen, y crea un elemento de clasificación y priorización por cada entrada. Genera
la lista completa de elementos antes de asignar los veredictos.

2. Confirmar el contexto del repositorio

   Codex determina el repositorio y la revisión actuales cuando están disponibles. Lee
`SECURITY.md`, si existe, para que las versiones compatibles, las entradas de confianza y los
   límites del producto y las superficies fuera del alcance se tengan en cuenta en la evaluación.

3. Inspeccionar la evidencia estática

   Para cada hallazgo, Codex rastrea la fuente presuntamente controlada por un atacante,
el control de seguridad pertinente, el sumidero vulnerable, la ruta alcanzable y el límite
de seguridad contemplado. Registra la evidencia que respalda la afirmación, la que la
contradice y los vacíos de prueba.

4. Asignar veredictos y posiciones

   Codex asigna un veredicto y un nivel de confianza a cada hallazgo. Ordena
por explotabilidad, en colas separadas, los hallazgos con veredicto `confirmed` y `needs_review`.

## Revisar los resultados

| Veredicto          | Qué significa                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `confirmed`      | La evidencia del repositorio muestra que la ruta vulnerable es alcanzable cuando se cumplen las precondiciones indicadas y que cruza un límite de seguridad contemplado.                     |
| `not_actionable` | La evidencia del repositorio descarta la afirmación; por ejemplo, al mostrar una versión no afectada, una ruta inalcanzable, una protección eficaz o una superficie que no se distribuye.                 |
| `needs_review`   | La evidencia del repositorio no basta para decidir porque la información necesaria no está disponible, es ambigua o depende del tiempo de ejecución, del entorno o de las políticas. |

  Las posiciones de explotabilidad usan números enteros positivos a partir de `1`, de forma independiente
  en cada cola de veredictos. Esto mantiene las prioridades de corrección separadas del
  trabajo de revisión pendiente. La posición `1` corresponde al hallazgo con veredicto `confirmed` más explotable
  o al hallazgo con veredicto `needs_review` de mayor prioridad en ese conjunto de resultados. La posición
  no es una puntuación de gravedad del escáner, y los hallazgos con veredicto `not_actionable` no reciben una posición.

Para cada hallazgo, revisa:

- la justificación del veredicto y la posición
- la evidencia que respalda la afirmación y la que la contradice
- las preguntas abiertas y los vacíos de prueba restantes
- la ubicación y el componente afectados
- la superficie del producto y el nivel de confianza de la fuente
- el siguiente paso recomendado
- la transferencia a [`$codex-security:fix-finding`](/es-419/codex/security/plugin/fix-findings),
  cuando el hallazgo tenga el veredicto `confirmed`

El proceso se completa cuando cada hallazgo proporcionado tiene un único resultado, Codex conserva
su identificador de origen y toda incertidumbre queda explícita. Los registros del backlog en Jira, Linear y otros
sistemas permanecen sin cambios, a menos que le pidas a Codex que los actualice después de
revisar los resultados de la clasificación y priorización.

## Siguientes pasos

- `confirmed`: después de que una persona acepte corregir el hallazgo, usa
[`$codex-security:fix-finding`](/es-419/codex/security/plugin/fix-findings) para corregirlo y
  verificarlo. El proceso de clasificación y priorización prepara una transferencia lista para usarse en un prompt, pero no invoca la habilidad
  automáticamente.
- `needs_review`: si ejecutar código puede resolver el vacío de prueba, usa
`$codex-security:validation` para realizar una validación dinámica acotada. Proporciona
  la afirmación del hallazgo, las ubicaciones afectadas, las precondiciones, la evidencia estática y los
  vacíos de prueba que aparecen en el resultado de la clasificación y priorización:

  ```text
  Use $codex-security:validation to dynamically validate finding [triage item ID or source ID] from the backlog triage result. Use the strongest realistic, bounded method, record exactly what was tested, and preserve any remaining proof gaps.

  A diferencia de la clasificación y priorización, la validación puede compilar o ejecutar código, crear una prueba específica o una
  prueba de concepto, o interactuar con una interfaz real. Revisa los comandos propuestos
  antes de aprobarlos y mantén vigentes las [políticas de aprobación y seguridad
  de Codex](/es-419/codex/agent-approvals-security).

- `needs_review`: si el hallazgo depende de la política del producto o del contexto de
  implementación, responde las preguntas abiertas indicadas antes de cambiar el código.
- `not_actionable`: conserva la evidencia junto con el registro del proceso de clasificación y priorización. Codex no cierra
  ni actualiza automáticamente el ticket de origen.
- Para buscar vulnerabilidades que no figuren en el backlog proporcionado, [ejecuta un análisis de
  seguridad](/es-419/codex/security/plugin/scans).
