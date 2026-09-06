<!-- source: https://learn.chatgpt.com/es-419/use-cases/user-stories-to-ui-mocks -->

## Introducción

Los equipos de producto suelen recopilar comentarios de diversas fuentes, como hilos de Slack, issues de Linear, documentos u hojas de cálculo de Google Drive, o notas de llamadas con clientes. En algunos casos, tienen historias de usuario claras que ilustran un problema que quieren resolver; en otros, el contexto se encuentra en esas fuentes.

ChatGPT puede recopilar este contexto y convertirlo en una maqueta de IU para una funcionalidad que resuelva el problema. Una vez que valides la propuesta, Codex puede implementarla en el producto.

## Genera una referencia visual fiel

Si tienes una historia de usuario clara, puedes comenzar por ella. De lo contrario, primero puedes conversar con ChatGPT para recopilar contexto de distintas fuentes y sintetizarlo en una historia de usuario.

Luego, puedes pedirle a ChatGPT que use la generación de imágenes para crear varias propuestas visuales de la maqueta. Las maquetas deben respetar la arquitectura de la información del producto y las restricciones del sistema de diseño.

Si te resulta útil, puedes proporcionar capturas de pantalla de la IU actual o un archivo de Figma como referencia.

Repite este proceso hasta que la maqueta te satisfaga. Cuanto más acotados sean los cambios, más probable será que Codex genere una maqueta que pueda implementarse directamente.

## Pasa de la maqueta al prototipo

Usa la imagen final de la maqueta que quieras que Codex implemente. Selecciona Codex, inicia un chat nuevo y vuelve a adjuntar la imagen, en lugar de continuar directamente en el chat de ChatGPT. Luego, pídele a Codex que implemente la maqueta —si estás creando una aplicación web, puedes usar el [complemento Build Web Apps](https://github.com/openai/plugins/tree/main/plugins/build-web-apps)— para convertirla en un prototipo funcional:
