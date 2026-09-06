<!-- source: https://learn.chatgpt.com/es-419/docs/agent-configuration/subagents -->

ChatGPT Work y Codex pueden ejecutar flujos de trabajo con subagentes al crear
agentes especializados en paralelo y luego reunir sus resultados en una sola respuesta. Esto puede
ser especialmente útil para tareas complejas que permiten un alto grado de paralelismo, como
explorar una base de código o implementar un plan de varios pasos para una funcionalidad.

En los clientes locales de Codex, también puedes definir agentes personalizados con distintas configuraciones de modelo
e instrucciones para diferentes tareas.

## Disponibilidad

ChatGPT Work ofrece flujos de trabajo con subagentes y muestra su actividad a las cuentas que cumplen los requisitos.

<a id="custom-agents"></a>

Las versiones actuales de Codex activan los flujos de trabajo con subagentes de forma predeterminada. La actividad de los subagentes
aparece en la aplicación de escritorio de ChatGPT, Codex CLI y la extensión para IDE.

Como cada subagente realiza su propio trabajo con el modelo y las herramientas, los flujos de trabajo con subagentes
consumen más tokens que las ejecuciones comparables con un solo agente.

En ChatGPT Work, pídele a ChatGPT que delegue trabajo independiente a subagentes. Los
agentes se ejecutan en el entorno alojado de ChatGPT, y el chat muestra su
actividad y sus resultados. En la mayoría de los niveles de inteligencia, solicita la delegación
de forma explícita. Con Ultra, ChatGPT puede delegar trabajo de manera proactiva cuando los agentes en
paralelo mejorarían considerablemente la velocidad o la calidad.

Pídele a Codex en un chat de la app que delegue partes independientes del trabajo a
subagentes. Las versiones locales actuales de Codex delegan cuando se lo pides directamente o cuando
lo solicitan las instrucciones aplicables de `AGENTS.md` o de una habilidad. La app muestra cada
hilo de subagente para que puedas revisar su trabajo y el resumen que se devuelve al
chat principal.

Pídele a Codex que use subagentes en una sesión interactiva de la CLI. Codex también puede seguir
las instrucciones aplicables de `AGENTS.md` o de una habilidad que soliciten la delegación. Usa
`/agent` para revisar los hilos de agentes y cambiar de uno a otro mientras se ejecutan. El hilo
principal reúne los resultados de los subagentes en su respuesta final.

Pídele a Codex en un chat del IDE que delegue partes independientes del trabajo a subagentes.
Codex también puede seguir las instrucciones aplicables de `AGENTS.md` o de una habilidad que soliciten
la delegación. Cuando la interfaz de agentes en segundo plano está disponible, los subagentes activos aparecen
encima del editor. Expande el panel para ver su estado, detener todos los subagentes
activos o abrir el hilo de un subagente.

## Por qué son útiles los flujos de trabajo con subagentes

Incluso con ventanas de contexto grandes, los modelos tienen límites. Si saturas el chat principal (donde defines requisitos, restricciones y decisiones) con resultados intermedios que generan ruido, como notas de exploración, registros de pruebas, trazas de pila y resultados de comandos, la sesión puede volverse menos confiable con el tiempo.

Esto suele describirse como:

- **Contaminación del contexto**: la información útil queda oculta entre resultados intermedios que generan ruido.
- **Deterioro del contexto**: el rendimiento disminuye a medida que el chat se llena de detalles menos relevantes.

Para obtener más contexto, consulta el artículo de Chroma sobre el [deterioro del contexto](https://research.trychroma.com/context-rot).

Los flujos de trabajo con subagentes ayudan a sacar del hilo principal el trabajo que genera ruido:

- Mantén al **agente principal** enfocado en los requisitos, las decisiones y los resultados finales.
- Ejecuta **subagentes** especializados en paralelo para tareas de exploración, pruebas o análisis de registros.
- Devuelve **resúmenes** de los subagentes en lugar de resultados intermedios sin procesar.

También pueden ahorrar tiempo cuando el trabajo se puede ejecutar de forma independiente y en paralelo, y
permiten abordar tareas de mayor alcance al dividirlas en partes
acotadas. Por ejemplo, Codex puede dividir el análisis de un documento de
varios millones de tokens en problemas más pequeños y devolver las conclusiones principales al hilo
principal.

Como punto de partida, usa agentes en paralelo para tareas centradas en la lectura, como
exploración, pruebas, clasificación y priorización de problemas, y generación de resúmenes. Ten más cuidado con los flujos de trabajo en paralelo
que requieren mucha escritura, ya que, si varios agentes editan código al mismo tiempo, pueden surgir
conflictos y aumentar el trabajo de coordinación.

## Términos clave

Codex usa algunos términos relacionados en los flujos de trabajo con subagentes:

- **Flujo de trabajo con subagentes**: flujo de trabajo en el que Codex ejecuta agentes en paralelo y combina sus resultados.
- **Subagente**: agente delegado que Codex inicia para encargarse de una tarea específica.
- **Hilo de agente**: hilo en el que un subagente realiza su trabajo. Los clientes compatibles permiten abrir estos hilos para revisar el progreso o los resultados.

## Activar flujos de trabajo con subagentes

En la mayoría de los niveles de inteligencia, solicita directamente subagentes o que varios agentes trabajen
en paralelo. Ultra permite la delegación proactiva, por lo que ChatGPT puede delegar trabajo independiente adecuado
sin que se lo pidas por separado.

Solicita directamente subagentes o que varios agentes trabajen en paralelo. Codex también puede delegar cuando
lo solicitan las instrucciones aplicables del proyecto o de una habilidad.

En la práctica, la activación manual consiste en usar instrucciones directas como
“crea dos agentes”, “delega este trabajo en paralelo” o “usa un agente por
punto”. Los flujos de trabajo con subagentes consumen más tokens que las ejecuciones comparables con un solo agente
porque cada subagente realiza su propio trabajo con el modelo y las herramientas.

Un buen prompt para subagentes debe explicar cómo dividir el trabajo, si Codex
debe esperar a todos los agentes antes de continuar y qué resumen o resultado debe
devolver.

```text
Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.

## Elegir modelos y niveles de razonamiento

Los distintos agentes necesitan distintas configuraciones de modelo y razonamiento.

En ChatGPT Work, elige un modelo y un nivel de inteligencia en el editor.
Los niveles de inteligencia disponibles pueden incluir **Ligera**, **Media**, **Alta**,
**Muy alta** y **Max**, según el modelo seleccionado. **Ultra** solo está
disponible para las cuentas que cumplen los requisitos y los modelos compatibles. Usa el nivel máximo de
razonamiento y permite que ChatGPT delegue de forma proactiva trabajo adecuado a subagentes.

En los demás niveles de inteligencia, solicita subagentes de forma explícita cuando quieras que el trabajo
se delegue en paralelo.

Si no configuras un modelo para el subagente ni `model_reasoning_effort`, el
subagente hereda el modelo y el esfuerzo de razonamiento del agente que lo creó. Si una solicitud explícita
de creación o un valor predeterminado de `[agents]` selecciona un modelo sin un
esfuerzo de razonamiento explícito o configurado, el subagente usa el esfuerzo de
razonamiento predeterminado de ese modelo. Para equilibrar la inteligencia, la velocidad y el precio en cada tarea,
solicita un modelo o un esfuerzo de razonamiento específico en tu prompt,
configura los valores predeterminados de `[agents]` en `config.toml` o establece `model` y
`model_reasoning_effort` directamente en el archivo del agente personalizado.
Por ejemplo, usa <code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> para análisis rápidos o una configuración de <code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code> con mayor esfuerzo para tareas de razonamiento más exigentes.

  Para la mayoría de las tareas en Codex, comienza con{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>. Usa{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> cuando quieras
  una opción más rápida y económica para tareas menos exigentes de los subagentes.

### Elección del modelo

- **<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>**: comienza por este modelo para los agentes que se encarguen de tareas exigentes. Es la opción más sólida para trabajos ambiguos de varios pasos que requieren planificación, uso de herramientas, validación y seguimiento hasta completarlos dentro de un contexto más amplio.
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>**: úsalo para agentes que priorizan la velocidad y la eficiencia sobre la profundidad, por ejemplo, para tareas de exploración, análisis centrados en la lectura, revisión de archivos grandes o procesamiento de documentos de apoyo. Funciona bien para agentes en paralelo que devuelven resultados resumidos al agente principal.
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestNanoModel.slug}</code>**: úsalo para agentes rápidos y con un alcance acotado que se encarguen de trabajos claros, repetibles o de gran volumen.

### Esfuerzo de razonamiento (`model_reasoning_effort`)

- **`ultra`**: úsalo para el razonamiento más profundo cuando el modelo seleccionado sea compatible con
  este nivel.
- **`max`** y **`xhigh`**: úsalos para tareas de razonamiento especialmente exigentes cuando el
  modelo seleccionado sea compatible con estos niveles.
- **`high`**: úsalo cuando un agente necesite seguir una lógica compleja, comprobar supuestos o analizar casos extremos (por ejemplo, agentes de revisión o especializados en seguridad).
- **`medium`**: valor predeterminado equilibrado para la mayoría de los agentes.
- **`low`**: úsalo cuando la tarea sea sencilla y la velocidad sea la prioridad.

Un mayor esfuerzo de razonamiento aumenta el tiempo de respuesta y el uso de tokens, pero puede mejorar la calidad de los trabajos complejos. Para obtener más información, consulta [Modelos](/es-419/codex/models), [Configuración básica](/es-419/codex/config-file/config-basic) y [Referencia de configuración](/es-419/codex/config-file/config-reference).

## Orquestación y controles de hilos

ChatGPT o Codex se encarga de la orquestación entre los agentes, lo que incluye crear nuevos
subagentes, enviar instrucciones de seguimiento, esperar los resultados y cerrar los
hilos de los agentes.

Cuando se ejecutan muchos agentes, Codex espera hasta que todos los resultados solicitados estén
disponibles y luego devuelve una respuesta consolidada.

En la mayoría de los niveles de inteligencia, ChatGPT crea agentes después de una solicitud directa. Con
Ultra, ChatGPT también puede delegar de forma proactiva cuando resulta útil trabajar en paralelo.

Las versiones locales actuales de Codex crean agentes en respuesta a una solicitud directa o a instrucciones aplicables
del proyecto o de una habilidad.

Para verlo en acción, prueba el siguiente prompt en tu proyecto:

```text
I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race
5. Test flakiness
6. Maintainability of the code

## Administrar subagentes

Abre **Subagentes** para ver las listas de solo lectura **Activos** y **Finalizados** . Selecciona un
subagente finalizado para revisar sus detalles y su resultado. La barra lateral web muestra
la actividad de los subagentes, pero no ofrece controles para detener un subagente concreto ni darle nuevas
instrucciones.

- Abre un hilo de subagente desde la actividad que se muestra en el hilo principal para revisar
su trabajo.
- Pídele directamente a Codex que dé nuevas instrucciones a un subagente en ejecución, que lo detenga o que cierre los hilos de
subagentes finalizados.

  

  

- Usa `/agent` en la CLI para cambiar entre los hilos de agentes activos y revisar el hilo en curso.
- Pídele directamente a Codex que dé nuevas instrucciones a un subagente en ejecución, que lo detenga o que cierre los hilos de agentes completados.

- Cuando el panel de agentes en segundo plano esté disponible, expándelo para revisar el estado,
detener los subagentes activos o abrir el hilo de un subagente.
- Pídele directamente a Codex que dé nuevas instrucciones a un subagente en ejecución, que lo detenga o que cierre los hilos de
subagentes completados.

## Aprobaciones y controles del sandbox

Los subagentes heredan tu política actual del sandbox.

ChatGPT Work ejecuta los subagentes en su entorno alojado y no ofrece un
sandbox local de Codex ni un control del modo de aprobación. Los subagentes usan las herramientas disponibles
en el chat de origen. Los permisos de sitios web y conectores siguen siendo
específicos de cada herramienta.

Los subagentes heredan el modo de permisos seleccionado debajo del editor. Elige el
modo de permisos del turno de origen antes de pedirle a Codex que delegue el trabajo.

En las sesiones interactivas de la CLI, pueden aparecer solicitudes de aprobación de hilos de agentes
inactivos incluso mientras estás viendo el hilo principal. El panel superpuesto de aprobación
muestra la etiqueta del hilo de origen, y puedes presionar `o` para abrir ese hilo antes de
aprobar, rechazar o responder la solicitud.

En los flujos no interactivos, o cuando una ejecución no puede presentar una nueva solicitud de aprobación, una
acción que necesita una nueva aprobación falla y Codex devuelve el error al
flujo de trabajo de origen.

Codex también vuelve a aplicar los ajustes vigentes que modifican la configuración del turno de origen durante la ejecución cuando crea un
agente secundario. Esto incluye las opciones de sandbox y aprobación que defines de forma interactiva durante
la sesión, como los cambios en `/permissions` o `--yolo`, aunque el archivo del
agente personalizado seleccionado establezca otros valores predeterminados.

Los subagentes heredan el modo de permisos seleccionado debajo del editor. Elige
el modo de permisos del turno de origen antes de pedirle a Codex que delegue el trabajo.

También puedes modificar la configuración del sandbox para [agentes personalizados](#custom-agents) específicos; por ejemplo, puedes indicar explícitamente que uno debe trabajar en modo de solo lectura.

## Agentes personalizados

Codex incluye estos agentes integrados:

- `default`: agente de respaldo de propósito general.
- `worker`: agente enfocado en la ejecución para tareas de implementación y corrección.
- `explorer`: agente para explorar bases de código mediante tareas centradas en la lectura.

Para definir tus propios agentes personalizados, agrega archivos TOML independientes en
`~/.codex/agents/` para los agentes personales o en `.codex/agents/` para los agentes de un
proyecto específico.

Cada archivo define un agente personalizado. Codex carga estos archivos como capas de configuración
para las sesiones creadas, por lo que los agentes personalizados pueden sobrescribir los mismos ajustes que
la configuración de una sesión normal de Codex. Esto puede resultar más complejo que un archivo de manifiesto
específico para agentes, y el formato puede evolucionar a medida que maduren las opciones de creación y uso compartido.

Cada archivo independiente de agente personalizado debe definir lo siguiente:

- `name`
- `description`
- `developer_instructions`

Si un archivo de agente personalizado define `model` o `model_reasoning_effort`, prevalece el valor
del archivo. Antes de aplicar el archivo, Codex determina cada ajuste
a partir de un valor explícito indicado al crear el agente, luego del valor predeterminado correspondiente de `[agents]` y, por último,
del valor del agente de origen. Si una solicitud explícita de creación o un valor predeterminado de `[agents]`
selecciona un modelo y ninguno de los dos especifica un esfuerzo de razonamiento, Codex usa
el esfuerzo predeterminado de ese modelo. Un archivo de agente personalizado que solo define `model`
conserva el esfuerzo determinado previamente. Define también `model_reasoning_effort` en el
archivo si el modelo seleccionado no admite ese esfuerzo o si quieres uno
diferente. Otros ajustes de la sesión, como `sandbox_mode`, `mcp_servers`
y `skills.config`, se heredan del agente de origen cuando el archivo de agente personalizado
los omite.

### Configuración global

La configuración global de los subagentes sigue estando en `[agents]` dentro de tu [configuración](/es-419/codex/config-file/config-basic#configuration-precedence).

| Campo                                       | Tipo    | Obligatorio | Propósito                                                             |
| ------------------------------------------- | ------- | :------: | ------------------------------------------------------------------- |
| `agents.enabled`                            | booleano |    No    | Activa o desactiva las herramientas multiagente.                                |
| `agents.max_concurrent_threads_per_session` | número  |    No    | Limita la cantidad de hilos de agentes creados que pueden estar abiertos al mismo tiempo, sin contar el principal. |
| `agents.default_subagent_model`             | cadena  |    No    | Establece el modelo predeterminado de los agentes creados.                           |
| `agents.default_subagent_reasoning_effort`  | cadena  |    No    | Establece el esfuerzo de razonamiento predeterminado de los agentes creados.                |
| `agents.interrupt_message`                  | booleano |    No    | Registra un mensaje visible para el modelo cuando se interrumpe el turno de un agente.   |

**Notas:**

- El valor predeterminado de `agents.enabled` es `true`. Configúralo en `false` para desactivar las herramientas multiagente.
- Si dejas `agents.max_concurrent_threads_per_session` sin definir, Codex elige el valor predeterminado. Las configuraciones existentes pueden seguir usando `agents.max_threads` como alias heredado.
- Los valores explícitos usados al crear agentes tienen prioridad sobre `agents.default_subagent_model` y `agents.default_subagent_reasoning_effort`.
- El valor predeterminado de `agents.interrupt_message` es `true`. Configúralo en `false` para omitir del contexto del agente el mensaje de interrupción visible para el modelo.
- Si el nombre de un agente personalizado coincide con el de un agente integrado, como `explorer`, el agente personalizado tiene prioridad.

### Esquema del archivo de agente personalizado

| Campo                    | Tipo   | Obligatorio | Propósito                                                         |
| ------------------------ | ------ | :------: | --------------------------------------------------------------- |
| `name`                   | cadena |   Sí    | Nombre del agente que Codex usa al crearlo o hacer referencia a él. |
| `description`            | cadena |   Sí    | Indicaciones para el usuario sobre cuándo Codex debe usar este agente.     |
| `developer_instructions` | cadena |   Sí    | Instrucciones principales que definen el comportamiento del agente.             |

También puedes incluir otras claves compatibles de `config.toml` en un archivo de agente personalizado, como `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers` y `skills.config`.

Codex identifica el agente personalizado mediante su campo `name`. Hacer coincidir el nombre del archivo con
el nombre del agente es la convención más sencilla, pero el campo `name` es la referencia
definitiva.

### Ejemplos de agentes personalizados

Los mejores agentes personalizados tienen un alcance acotado y criterios definidos. Asigna a cada uno una tarea clara, un
conjunto de herramientas adecuado para esa tarea e instrucciones que eviten que se
desvíe hacia tareas relacionadas.

#### Ejemplo 1: revisión de un PR

Este patrón reparte la revisión entre tres agentes personalizados con enfoques específicos:

- `pr_explorer` traza un mapa de la base de código y recopila evidencia.
- `reviewer` busca riesgos relacionados con la corrección, la seguridad y las pruebas.
- `docs_researcher` consulta la documentación del framework o la API mediante un servidor MCP dedicado.

Configuración del proyecto (`.codex/config.toml`):

```toml
[agents]
max_concurrent_threads_per_session = 8

`.codex/agents/pr-explorer.toml`:

```toml
name = "pr_explorer"
description = "Read-only codebase explorer for gathering evidence before changes are proposed."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in exploration mode.
Trace the real execution path, cite files and symbols, and avoid proposing fixes unless the parent agent asks for them.
Prefer fast search and targeted file reads over broad scans.
"""

`.codex/agents/reviewer.toml`:

```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
Lead with concrete findings, include reproduction steps when possible, and avoid style-only comments unless they hide a real bug.
"""

`.codex/agents/docs-researcher.toml`:

```toml
name = "docs_researcher"
description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Use the docs MCP server to confirm APIs, options, and version-specific behavior.
Return concise answers with links or exact references when available.
Do not make code changes.
"""

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"

Esta configuración funciona bien con prompts como:

```text
Review this branch against main. Have pr_explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.

#### Ejemplo 2: depuración de la integración del frontend

Este patrón resulta útil para regresiones de la interfaz de usuario, flujos del navegador con fallas intermitentes o errores de integración que abarcan el código de la aplicación y el producto en ejecución.

Configuración del proyecto (`.codex/config.toml`):

```toml
[agents]
max_concurrent_threads_per_session = 6

`.codex/agents/code-mapper.toml`:

```toml
name = "code_mapper"
description = "Read-only codebase explorer for locating the relevant frontend and backend code paths."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Map the code that owns the failing UI flow.
Identify entry points, state transitions, and likely files before the worker starts editing.
"""

`.codex/agents/browser-debugger.toml`:

```toml
name = "browser_debugger"
description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"
developer_instructions = """
Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
Use browser tooling for screenshots, console output, and network evidence.
Do not edit application code.
"""

[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
startup_timeout_sec = 20

`.codex/agents/ui-fixer.toml`:

```toml
name = "ui_fixer"
description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
developer_instructions = """
Own the fix once the issue is reproduced.
Make the smallest defensible change, keep unrelated files untouched, and validate only the behavior you changed.
"""

[[skills.config]]
path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
enabled = false

Esta configuración funciona bien con prompts como:

```text
Investigate why the settings modal fails to save. Have browser_debugger reproduce it, code_mapper trace the responsible code path, and ui_fixer implement the smallest fix once the failure mode is clear.
