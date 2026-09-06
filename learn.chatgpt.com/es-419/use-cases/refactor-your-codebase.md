<!-- source: https://learn.chatgpt.com/es-419/use-cases/refactor-your-codebase -->

## Introducción

Cuando tu base de código ha acumulado código sin usar, lógica duplicada, abstracciones obsoletas, archivos grandes o patrones heredados que encarecen cada cambio más de lo necesario, considera reducir la deuda de ingeniería mediante una refactorización. La refactorización consiste en mejorar la estructura del sistema existente sin convertir el trabajo en una migración del stack tecnológico.

Codex resulta útil en este caso porque primero puede analizar el área problemática y luego aplicar la limpieza en iteraciones pequeñas y fáciles de revisar: eliminar rutas sin usar, simplificar módulos grandes, consolidar rutas duplicadas, modernizar patrones obsoletos del framework y reforzar la validación de cada iteración.

El objetivo es mejorar la base de código existente sin migrarla:

1. Elimina el código sin usar, las funciones auxiliares obsoletas, los flags antiguos y las capas de compatibilidad que ya no sean necesarias.
2. Reduce el tamaño de los módulos sobrecargados al extraer funciones auxiliares, dividir componentes o trasladar los efectos secundarios a límites más claros.
3. Reemplaza los patrones heredados por las convenciones actuales del repositorio: primitivas más recientes del framework, tipos más claros, un flujo de estado más simple o utilidades de la biblioteca estándar.
4. Mantén estable el comportamiento público y reduce el costo del siguiente cambio.

## Cómo usarlo

1. Pídele a Codex que analice el área antes de editarla: módulos sobrecargados, lógica duplicada, código sin usar, pruebas, contratos públicos y cualquier patrón antiguo que ya no sea adecuado para el repositorio.
2. Elige un tipo de limpieza a la vez: elimina el código sin usar, simplifica el flujo de control, moderniza un patrón obsoleto o divide un archivo grande en partes más pequeñas con responsables claros.
3. Antes de que Codex aplique parches a los archivos, pídele que indique el comportamiento actual, la mejora estructural que quiere realizar y la comprobación mínima que permita demostrar que el comportamiento se mantuvo estable.
4. Revisa y ejecuta la comprobación mínima que resulte útil después de cada iteración, en lugar de agrupar toda la limpieza en un único diff.
5. Mantén los cambios en el stack, las migraciones de dependencias y los cambios de arquitectura como tareas separadas, a menos que sean necesarios para completar la limpieza.

  Puedes usar el Modo plan para crear un plan de refactorización antes de comenzar el
trabajo.

## Aprovechar los ExecPlans

La [guía práctica para modernizar código](/cookbook/examples/codex/code_modernization) presenta los ExecPlans: documentos que le permiten a Codex mantener una visión general de la limpieza, detallar el estado final previsto y registrar la validación después de cada iteración.
Son útiles cuando la refactorización abarca más de un módulo o requiere más de una sesión. Úsalos para registrar eliminaciones, actualizaciones de patrones, contratos que debieron mantenerse estables y lo que siga pendiente.

## Usar habilidades para patrones recurrentes

Las [habilidades](/es-419/codex/build-skills) son útiles cuando las mismas reglas de limpieza se repiten en varios repositorios, servicios o equipos. Usa habilidades específicas del framework cuando estén disponibles, complementa las limpiezas riesgosas con habilidades de seguridad y CI, y crea una habilidad para el equipo cuando tengas una lista de verificación comprobada para eliminar código sin usar, extraer módulos o modernizar patrones heredados.
Si terminas aplicando la misma modernización a más de una base de código, Codex puede ayudarte a convertir el primer proceso exitoso en una habilidad reutilizable.
