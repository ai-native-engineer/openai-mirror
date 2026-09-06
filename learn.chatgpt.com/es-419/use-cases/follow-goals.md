<!-- source: https://learn.chatgpt.com/es-419/use-cases/follow-goals -->

## Introducción

Usa `/goal` cuando quieras que Codex siga trabajando para alcanzar un objetivo duradero, en lugar de detenerse después de un solo turno normal. Resulta útil para trabajos con un objetivo claro, un ciclo de validación y suficiente margen para que Codex avance sin pedirte que dirijas cada paso. Cuando usas `/goal`, Codex puede trabajar de forma independiente durante varias horas sin necesitar tu intervención.

Establece un objetivo con `/goal <objective>`, consulta el objetivo actual con `/goal` y usa `/goal pause`, `/goal resume` o `/goal clear` cuando necesites controlar la ejecución.

Si `/goal` no aparece en la lista de comandos slash, habilita `features.goals`
en `config.toml`:

```toml
[features]
goals = true

También puedes ejecutar `codex features enable goals` desde la CLI o pedirle a Codex que lo ejecute.

## Elegir el trabajo adecuado

Un buen objetivo debe tener un alcance mayor que un solo prompt, pero menor que una lista de tareas pendientes sin límites definidos. Debe especificar qué debe lograr Codex, qué no debe cambiar, cómo debe validar el progreso y cuándo debe detenerse.

Esto funciona bien para:

- migraciones de código en las que estén claros el stack de destino, las comprobaciones de paridad y las restricciones
- refactorizaciones de gran alcance en las que Codex pueda ejecutar pruebas después de cada punto de control
- experimentos, juegos o prototipos en los que Codex pueda seguir mejorando un artefacto funcional

Evita usar un objetivo para una lista poco estructurada de tareas sin relación entre sí.

## Configurar el ciclo

1. Especifica un solo objetivo y una sola condición de detención.
2. Indícale a Codex los archivos, la documentación, el issue, los registros o el plan que debe leer primero.
3. Define los comandos o artefactos que permiten comprobar el progreso.
4. Indícale a Codex que trabaje con puntos de control y lleve un registro breve del progreso.
5. Usa `/goal` para consultar el estado mientras se ejecuta.
6. Pausa, reanuda o elimina el objetivo cuando la ejecución termine, se bloquee o cambie de rumbo.

Lo importante es el contrato. Codex debe saber qué significa “terminado” antes de empezar. Si el objetivo es una migración, “terminado” podría significar que la nueva ruta supera las pruebas de contrato y que la ruta heredada aún cuenta con un mecanismo de reversión. Si el objetivo es un juego o un prototipo, “terminado” podría significar que la aplicación se compila, se inicia y coincide con la referencia proporcionada o con el comportamiento esperado.

  Pídele ayuda a Codex: empieza por conversar sobre lo que quieres
crear y luego pídele que establezca directamente un objetivo y comience a trabajar.

## Dejar que Codex trabaje de forma independiente

Mientras Codex trabaja en un objetivo, pide informes de progreso concisos que te permitan confiar más en su ejecución. Un informe de estado útil indica el punto de control actual, qué se verificó, qué falta y si Codex está bloqueado.
Si el informe se vuelve impreciso, acota el objetivo en lugar de agregar más instrucciones puntuales. Indícale a Codex exactamente cuál es el próximo punto de control relevante, qué comando lo valida y qué condición debe llevarlo a pausar la ejecución.

Cuando Codex trabaja para alcanzar un objetivo, puede hacerlo de forma independiente durante muchas horas sin que tengas que estar pendiente. Se detendrá cuando esté seguro de haber alcanzado la condición de detención, por lo que debes considerar `/goal` una tarea en segundo plano que no necesitas supervisar.

## Ejemplos de objetivos

### Migraciones

Ya sea que migres juegos a un stack nuevo, aplicaciones móviles a una plataforma nueva o una base de código a un framework nuevo, puedes usar `/goal` para que Codex ejecute la migración:

### Creación de prototipos

Ya sea que estés creando una aplicación nueva desde cero, un juego nuevo o una funcionalidad nueva, puedes usar `/goal` para que Codex complete una primera versión pulida. Puedes usar un archivo PLAN.md para guiar la creación de la primera versión y describir allí con precisión lo que quieres crear.

### Optimización de prompts

Cuando tengas un conjunto de evaluaciones, puedes usar `/goal` para optimizar los prompts en función de los resultados de las evaluaciones. Codex puede revisar los fallos, actualizar el prompt, volver a ejecutar las evaluaciones y seguir iterando hasta que mejore la puntuación o se alcance tu condición de detención.
