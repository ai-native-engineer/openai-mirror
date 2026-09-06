<!-- source: https://learn.chatgpt.com/es-419/use-cases/iterate-on-difficult-problems -->

## Introducción

Algunas tareas se verifican fácilmente en un solo intento: la compilación se completa correctamente, las pruebas pasan y listo. Sin embargo, algunos problemas de optimización son difíciles de resolver y requieren muchas iteraciones con un ciclo de evaluación riguroso. Para saber qué rumbo seguir, Codex debe inspeccionar el resultado actual, puntuarlo, decidir cuál será el siguiente cambio y repetir el proceso hasta obtener un resultado realmente bueno.

Este tipo de caso de uso funciona bien con una interfaz personalizada que permite inspeccionar visualmente el progreso a partir de los resultados y los artefactos generados que Codex registra en cada iteración.
Puedes observar cómo Codex sigue trabajando en la App mientras el artefacto objetivo, el resultado del modelo o el recurso generado siguen mejorando.
La clave es proporcionar a Codex los scripts necesarios para generar las métricas de evaluación y los artefactos que debe inspeccionar.

## Comenzar con las evaluaciones

Antes de comenzar la tarea, define cómo se medirá el éxito. La mejor configuración suele combinar:

- **Comprobaciones deterministas:** aspectos que los scripts pueden puntuar directamente, como incumplimientos de restricciones o métricas deterministas calculadas mediante código
- **Comprobaciones con un LLM como juez:** puntuaciones basadas en una rúbrica para cualidades difíciles de codificar con exactitud, como la similitud, la legibilidad, la utilidad o la calidad general; estas comprobaciones pueden basarse en resultados de texto o de imágenes

Si el aspecto subjetivo es importante, proporciona a Codex un script que pueda llamar a un modelo, por ejemplo, mediante la [Responses API](/api/reference/resources/responses/methods/create) y devolver puntuaciones estructuradas. La idea no es reemplazar las comprobaciones deterministas, sino complementarlas con un juez coherente para la parte que, de otro modo, las personas evaluarían a simple vista.

El ciclo funciona mejor cuando el resultado de la evaluación es legible por máquina, se guarda después de cada ejecución y puede compararse fácilmente a lo largo del tiempo.

  **Consejo**: pídele a Codex que genere el script de evaluación y describe las
  comprobaciones que quieres ejecutar.

## Definir una regla de detención para Codex

Las tareas difíciles suelen perder el rumbo porque el prompt dice “sigue mejorando”, pero no indica cuándo detenerse. Haz explícita la regla de detención.

Un patrón práctico es el siguiente:

1. Establece un objetivo para la puntuación general.
2. Establece un objetivo independiente para el promedio del LLM como juez.
3. Indícale a Codex que continúe hasta que ambos superen el umbral, no solo uno.

Por ejemplo, si el objetivo es obtener un artefacto de alta calidad, pídele a Codex que continúe hasta que tanto la puntuación general como el promedio del LLM superen el 90 %. Así, la tarea queda clara: Codex puede determinar si todavía está por debajo del objetivo, qué falta para alcanzarlo y si el último cambio ayudó.

## Mantener un registro continuo del ciclo

El trabajo de larga duración es mucho más confiable cuando Codex toma notas sobre el ciclo en lugar de depender únicamente del contexto del Chat.

Ese registro continuo debe incluir:

- las mejores puntuaciones actuales
- qué cambió en la última iteración
- qué aspectos mejoraron o empeoraron según la evaluación
- qué planea probar Codex a continuación

Esto es especialmente importante cuando la tarea se ejecuta durante mucho tiempo. El registro sirve como referencia al reanudar la tarea y como historial de autoevaluación de la ejecución actual.

## Inspeccionar el artefacto, no solo los registros

Para algunas tareas difíciles, el diff de código y los resultados de las métricas no son suficientes. Codex debe examinar el artefacto que produjo.

Si el resultado es visual, como una imagen generada, un diseño o un estado renderizado, permite que Codex inspeccione directamente ese artefacto —por ejemplo, cuando el resultado esté guardado en el disco como una imagen— y compare el resultado actual con el mejor resultado anterior o con la rúbrica prevista.

Esto refuerza el ciclo:

- el script de evaluación indica la puntuación
- el artefacto muestra lo que la puntuación pasó por alto
- el siguiente cambio se basa en ambos

Esta combinación es mucho más eficaz que hacer cambios en el código a ciegas entre ejecuciones.

## Hacer explícita cada iteración

Pídele a Codex que siga el mismo ciclo cada vez:

1. Ejecuta las evaluaciones sobre la línea base actual.
2. Identifica el modo de falla más importante a partir de las puntuaciones y los artefactos.
3. Haz un solo cambio específico para resolver ese cuello de botella.
4. Vuelve a ejecutar las evaluaciones.
5. Registra las nuevas puntuaciones y si el cambio ayudó.
6. Continúa hasta alcanzar los umbrales.

Esta disciplina es importante. Si en cada iteración se cambian demasiadas cosas a la vez, Codex no puede determinar qué idea mejoró la puntuación. Si Codex omite el registro, resulta difícil confiar en la tarea y reanudarla.
