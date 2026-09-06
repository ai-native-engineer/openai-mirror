<!-- source: https://learn.chatgpt.com/es-419/use-cases/verified-operations-workflows -->

## Ejecuta operaciones que puedas auditar

Si tienes operaciones repetibles que debes ejecutar con regularidad, como dar acceso a un usuario, aplicar una actualización por lotes o ejecutar un script con distintos parámetros, puedes usar ChatGPT para automatizarlas y obtener un resultado auditable.

Usa este flujo de trabajo cuando ChatGPT deba ejecutar una operación repetible y mostrarte qué ocurrió mediante un artefacto que sirva como verificación.

## Describe la tarea y los datos de entrada

1. Proporciona a ChatGPT la tabla de entrada, los archivos, los tickets u otra lista de elementos que deba procesar por lotes.
2. Indícale la fuente de aprobación o la política que define el alcance permitido, si corresponde.
3. Indica a ChatGPT qué script, API, habilidad, CLI o flujo de trabajo de una app debe realizar el trabajo.
4. Si lo deseas, solicita una ejecución de prueba cuando el flujo de trabajo la admita.
5. Pídele a ChatGPT que ejecute la operación por lotes y registre una fila de éxito o falla por cada elemento.

Mantén acotado el alcance y agrega instrucciones para que ChatGPT ejecute la operación solo cuando tenga todos los datos de entrada obligatorios.
Si a una fila le falta un campo obligatorio, ChatGPT debe marcarla en lugar de adivinar.

Usa [complementos](/es-419/codex/plugins) para conectar las herramientas que utilizas para ejecutar la operación, como tu sistema de tickets o la hoja de cálculo con los elementos de la lista.

## Exige evidencia para verificar el resultado

Una ejecución útil de operaciones incluye un resultado que tú o un integrante de tu equipo puedan inspeccionar, como un CSV, un archivo de registro, un enlace a un panel, una captura de pantalla, una verificación de un PR u otra evidencia de que la operación se realizó correctamente. En la app de escritorio de ChatGPT, puedes [abrir e inspeccionar los archivos generados](/es-419/codex/artifacts-viewer) después de la ejecución para verificar el resultado.

## Convierte la ejecución en un flujo de trabajo reutilizable

Después de la primera ejecución correcta, pídele a ChatGPT que registre los elementos repetibles. Para los flujos de trabajo habituales, esto puede convertirse en una [habilidad](/es-419/codex/build-skills) o una [tarea programada](/es-419/codex/automations).

Para las operaciones programadas, crea una tarea programada solo después de que la ejecución manual produzca resultados confiables. Mantén permanentemente como borradores las acciones sensibles que podrían afectar el acceso o los datos, a menos que quieras explícitamente que ChatGPT las realice.
