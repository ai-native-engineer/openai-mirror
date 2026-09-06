<!-- source: https://learn.chatgpt.com/es-419/use-cases/ai-app-evals -->

## Introducción

Cuando creas una aplicación de IA o modificas una existente, quieres asegurarte de que se comporte como esperas. Las evaluaciones permiten probar sistemáticamente un conjunto de situaciones y detectar regresiones antes del lanzamiento.

Puedes usar Promptfoo para ejecutar evaluaciones en tu aplicación de IA y Codex para ayudarte a crearlas y mantenerlas.

## Cómo usarlo

Usa Codex junto con la habilidad `$promptfoo-evals` del complemento de Promptfoo para convertir un comportamiento de la aplicación de IA en un conjunto de evaluaciones repetible. Si la aplicación aún no tiene un destino de Promptfoo que funcione, `$promptfoo-provider-setup` ayuda a conectar el conjunto con la ruta de la aplicación que quieres probar.

Codex puede inspeccionar la aplicación, proponer casos que aporten señales claras, agregar la configuración de Promptfoo y los datos de prueba, ejecutar el conjunto localmente y darte un comando que puedas seguir usando.

Este caso de uso funciona mejor cuando el comportamiento es concreto: calidad de las respuestas de soporte, anclaje en la información recuperada, etiquetas del clasificador, llamadas a herramientas, estructura JSON, reglas de negocio o confianza al migrar prompts y modelos.

Una buena primera versión debe incluir código y datos de prueba fáciles de revisar: un archivo `promptfooconfig.yaml` o una configuración equivalente, un pequeño directorio `evals/`, casos de prueba, cualquier adaptador de destino necesario para llamar a la aplicación y un comando local como `npm run evals`.

## Elige qué evaluar

Comienza con una promesa visible para los usuarios. Evita pedirle a Codex que evalúe todo el sistema de IA de una sola vez. Es más fácil confiar en un conjunto más pequeño, revisarlo y seguir ejecutándolo.

Algunos buenos objetivos iniciales son:

- **Corrección:** clasificación, extracción, resumen, enrutamiento o transformación.
- **Anclaje:** respuestas que deben mantenerse vinculadas a los documentos recuperados o las fuentes citadas.
- **Uso de herramientas:** elegir la herramienta adecuada, pasar argumentos válidos y gestionar los errores de las herramientas.
- **Formato o reglas de negocio:** esquemas JSON, nombres de campos, límites impuestos por reglas de negocio o contratos para el texto de la interfaz de usuario.
- **Migración de prompts o modelos:** asegurarse de que un cambio de prompt, modelo, mensaje del sistema o configuración de recuperación no provoque fallas en casos importantes.

Parte de los requisitos del producto, informes de errores, casos que el equipo de soporte haya escalado o ejemplos depurados que tu equipo no tenga inconveniente en incorporar al repositorio.

## Pide un plan de evaluación

Codex debe inspeccionar la aplicación antes de editarla. Pide un plan que indique la ruta de destino, los datos de prueba, las aserciones, el adaptador y los comandos. Así podrás detectar si se eligió un destino incorrecto o si los casos de prueba son deficientes antes de agregar los archivos.

Revisa el plan antes de implementarlo. Debe indicar la ruta de la aplicación o el punto de acceso al que llamará Promptfoo, los casos iniciales, las aserciones, los archivos que creará Codex, el comando local y los secretos o servicios necesarios. Si el plan prueba directamente el modelo en lugar de la ruta de la aplicación que usan los usuarios, pregúntale a Codex si eso es intencional.

## Implementa, ejecuta e itera

Cuando el plan sea correcto, pídele a Codex que lo implemente. La primera implementación debe ser sencilla: configuración, casos, datos de prueba, un adaptador de destino si es necesario, un comando y evidencia de que el comando se ejecutó.

Un conjunto pequeño de evaluaciones de la aplicación podría verse así:

```text
evals/
  promptfooconfig.yaml
  tests/
    cases.yaml
  providers/
    provider.js  # only if the built-in provider cannot call the app directly

Ejecuta el conjunto antes de cambiar el comportamiento. La evaluación de referencia te indica si la aplicación ya falla en esos casos, si es necesario ajustar las aserciones o si el adaptador de destino no es el correcto. Ajusta las aserciones cuando sean demasiado frágiles o vagas, pero mantén visibles las fallas reales del producto.

Después de la primera ejecución, usa el conjunto para comparar los cambios en la aplicación antes de lanzarlos. Agrega nuevos casos cada vez que un error, un requisito de lanzamiento o una revisión del producto revele un comportamiento que quieras mantener estable. Cuando el comando local sea estable, pídele a Codex que lo agregue a CI o a tu lista de verificación para lanzamientos.
