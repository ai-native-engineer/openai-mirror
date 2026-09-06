<!-- source: https://learn.chatgpt.com/es-419/use-cases/api-integration-migrations -->

## Introducción

A medida que lanzamos nuevos modelos y funciones de la API, te recomendamos actualizar tu integración para aprovechar las mejoras más recientes.
Cambiar de un modelo a otro no suele ser tan sencillo como actualizar solo el nombre del modelo.

Puede haber cambios en la API. Por ejemplo, para el modelo GPT-5.4, agregamos un nuevo parámetro `phase` al mensaje del asistente que es importante incluir en tu integración. Pero lo más importante es que el comportamiento del modelo puede ser diferente y requerir cambios en tus prompts existentes.

Al migrar a un modelo nuevo, debes asegurarte no solo de hacer los cambios necesarios en el código, sino también de evaluar el impacto en tus flujos de trabajo.

## Aprovecha la habilidad de documentación de OpenAI

La página [Guía de modelos](/api/docs/guides/latest-model) reúne las recomendaciones sobre las funciones de la API, el comportamiento de los modelos, la migración y el diseño de prompts para cada generación de modelos.

La habilidad de documentación de OpenAI también incluye [recomendaciones específicas](https://github.com/openai/codex/blob/6323f0104d17d211029faab149231ba787f7da37/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-5p4.md) que sirven como referencia concreta para la migración. Para el modelo al que se recomienda actualizar actualmente, consulta la página [Guía de modelos](/api/docs/guides/latest-model).

Codex ahora incluye de forma automática la habilidad de documentación de OpenAI, así que asegúrate de mencionarla en tu prompt para acceder a toda la documentación y las recomendaciones más recientes al desarrollar con la API de OpenAI.

## Crea un flujo de evaluaciones sólido

Codex puede actualizar automáticamente tus prompts según las recomendaciones más recientes sobre el diseño de prompts, pero debes contar con una forma de automatizar la verificación de que tu integración funciona según lo previsto.

Asegúrate de crear un flujo de evaluaciones que puedas ejecutar cada vez que hagas cambios en tu integración para verificar que no haya regresiones en el comportamiento.

Esta [guía del Cookbook](/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel) explica en detalle cómo hacerlo mediante nuestra [Evals API](/api/docs/guides/evals).
