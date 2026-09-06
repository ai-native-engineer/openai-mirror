<!-- source: https://learn.chatgpt.com/es-419/use-cases/automation-bug-triage -->

## Cómo usarlo

Pídele a Codex que revise los lugares donde ya aparecen los errores: alertas de Sentry, issues de Linear, Issues de GitHub, comprobaciones de PR, registros de despliegue, tickets de soporte e hilos de Slack. Comienza con una revisión manual, ajusta el informe en el chat y luego ejecútala de forma programada.

Usa un solo chat de Codex para todo el ciclo de triaje:

1. Ejecuta una revisión bajo demanda y obtén un borrador de la lista.
2. Revisa la lista y comparte tus comentarios en ese mismo chat.
3. Programa desde ese chat una tarea para el triaje.
4. Opcional: pídele a Codex que redacte issues de Linear, actualizaciones de Slack, comentarios de GitHub o notas para el traspaso cuando estés conforme con el informe.

Antes de comenzar, instala los [complementos](/es-419/codex/plugins) que Codex necesite, como Sentry, Slack, Linear o GitHub. En el prompt inicial, reemplaza la lista de complementos entre corchetes por chips reales de complementos con `@`. Luego, reemplaza cada fuente entre corchetes por la ubicación exacta en la que debe buscar: un proyecto de Sentry o una URL de alerta, un canal o hilo de Slack, un equipo, una vista o una consulta de Linear, un repositorio de GitHub, una consulta de issues o una comprobación de PR, un enlace de despliegue, un archivo de registro, una cola de soporte o un panel.

## Fase 1: ejecutar la revisión

Inicia Codex desde el repositorio al que corresponden los errores cuando resulte útil tener contexto local: pruebas, herramientas del repositorio, comprobaciones de compilación o fallas de CI. También puedes ejecutar la revisión desde cualquier repositorio si las fuentes de errores están disponibles mediante complementos, conectores, Servidores MCP, enlaces, exportaciones, registros pegados o archivos adjuntos.

Primero, ejecuta el prompt inicial anterior. Conserva solo los complementos y las fuentes que formen parte de la revisión.

Por ejemplo, un prompt completado puede indicar los complementos y las colas, los canales o los repositorios exactos que quieras incluir en la revisión.

<div class="not-prose mb-12 rounded-xl bg-[url('/images/codex/codex-wallpaper-1.webp')] bg-cover bg-center p-4 md:p-8">
  
</div>

## Fase 2: mejorar la utilidad del informe

Antes de automatizar la revisión, asegúrate de que el informe sea lo bastante útil como para leerlo todos los días.

Una primera ejecución útil incluye:

- Errores relevantes ordenados de P0 a P3.
- Los reportes duplicados se agrupan bajo un solo error.
- Cada error incluye evidencia enlazada o citas breves.
- Las suposiciones están separadas de los hechos observados.
- Cada error incluye una recomendación breve sobre la siguiente acción.

Ajusta el informe en el mismo chat antes de programarlo. Puedes pedirle a Codex que:

- Revise una fuente adicional antes de ordenar la lista por prioridad.
- Descarte las alertas irrelevantes que el equipo ya conoce.
- Devuelva solo los errores P0 y P1.
- Combine los reportes de Slack, las alertas de Sentry y las fallas de GitHub cuando se refieran al mismo error.
- Muestre únicamente el mejor enlace para cada error.
- Incluya evidencia suficiente para que otra persona pueda reproducir el error o derivarlo al equipo adecuado.

## Fase 3: automatizar el proceso

Cuando el informe bajo demanda sea útil, continúa en el mismo chat y [programa desde allí una tarea para el triaje](/es-419/codex/automations#schedule-a-task-inside-a-chat). Codex puede usar lo que ajustaste en el chat para redactar el prompt recurrente.

**Programa la tarea de triaje**

## Fase 4: canalizar las acciones de seguimiento

Una vez que el informe programado sea útil, decide a dónde enviar el trabajo después. Codex puede redactar una actualización para un canal del equipo en Slack, preparar issues de Linear para los errores a los que quieras dar seguimiento, escribir comentarios en GitHub para un PR con verificaciones fallidas o preparar una nota de traspaso para quien esté de guardia.
