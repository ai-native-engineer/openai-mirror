<!-- source: https://learn.chatgpt.com/es-419/use-cases/code-migrations -->

## Introducción

Al pasar de un stack a otro, puedes usar Codex para planificar y ejecutar una migración controlada que abarque el enrutamiento, los modelos de datos, la configuración, la autenticación, las tareas en segundo plano, las herramientas de compilación, el despliegue, las pruebas e incluso el propio lenguaje y las convenciones del framework.

Codex resulta útil aquí porque puede hacer un inventario del sistema heredado, establecer la correspondencia entre los conceptos heredados y los nuevos e implementar el cambio mediante puntos de control en vez de hacer una única reescritura enorme. Esto es importante cuando dejas atrás un framework heredado, migras a un entorno de ejecución nuevo o sustituyes gradualmente un stack por otro mientras el producto debe seguir funcionando.

## Cómo usarlo

1. Comienza por hacer un inventario de todo lo que abarca la migración: paquetes heredados, convenciones del framework, enrutamiento, acceso a datos, autenticación, configuración, herramientas de compilación, pruebas, supuestos sobre el despliegue y cualquier contrato externo que deba mantenerse durante la migración.
2. Pídele a Codex que establezca la correspondencia entre los conceptos del sistema heredado y el stack de destino, y que señale todo lo que no tenga un equivalente directo.
3. Elige una estrategia incremental: una capa de compatibilidad, una migración módulo por módulo, branch-by-abstraction o una sustitución con el patrón estrangulador aplicada a un límite a la vez.
4. Mantén estable el comportamiento hasta que la propia migración obligue a introducir un cambio visible e identifica explícitamente esas excepciones.
5. Después de cada hito, ejecuta la validación mínima que demuestre la paridad: análisis de lint, comprobación de tipos, pruebas específicas, pruebas de contrato, pruebas de humo o una comparación lado a lado con la ruta heredada.
6. Después de cada punto de control, revisa el diff y el riesgo de transición restante, en lugar de esperar a completar toda la reescritura.

## Aprovecha los ExecPlans

En nuestro [recetario para modernizar código](/cookbook/examples/codex/code_modernization), presentamos los ExecPlans: documentos que permiten que Codex mantenga una visión general de las tareas de limpieza, describa con claridad el estado final previsto y registre la validación después de cada iteración.
Cuando le pidas a Codex que ejecute una migración compleja, pídele que cree un ExecPlan para cada parte del sistema a fin de garantizar que cada decisión y cada elección del stack tecnológico queden registradas y puedan revisarse más adelante.

## Combínalo con un objetivo

Para los segmentos de migración de larga duración, usa un [objetivo](/es-419/codex/use-cases/follow-goals) para orientar a Codex durante el proceso. Define el objetivo con un estado final claro, comprobaciones de paridad, expectativas de reversión y una condición para detener el trabajo.
