<!-- source: https://learn.chatgpt.com/es-419/use-cases/idea-to-proof-of-concept -->

## Comienza con una dirección visual

GPT Image 2 es excelente para generar maquetas de interfaz de usuario de alta calidad. En lugar de empezar desde cero al explorar ideas nuevas, puedes aprovechar la generación de imágenes para definir una dirección visual.

Puedes hacerlo de dos maneras:

- Itera sobre la dirección visual con la habilidad ImageGen y, una vez que estés conforme con la interfaz de usuario propuesta, puedes pedirle a Codex que cree un prototipo que reproduzca ese diseño. En ese caso, selecciona Codex, inicia un chat nuevo y adjunta la imagen final que quieres implementar, en lugar de continuar directamente en el chat de ChatGPT. Codex obtiene mejores resultados cuando puede tomar como referencia un archivo que adjuntó el usuario.
- Usa un complemento y simplemente describe tu idea: el complemento generará por ti la dirección visual y se encargará de los siguientes pasos.

## Aprovecha un complemento

Si no necesitas iterar sobre la dirección visual antes de comenzar la implementación, puedes usar un complemento y describir tu idea.

Usa el [complemento Build Web Apps](https://github.com/openai/plugins/tree/main/plugins/build-web-apps)
para aplicaciones web, paneles, sitios web creativos y herramientas centradas en el frontend. Su
flujo de trabajo hace que Codex genere primero un diseño, lo reproduzca en código y use el
navegador para comparar el resultado con el concepto.

Usa el [complemento Game Studio](https://github.com/openai/plugins/tree/main/plugins/game-studio)
cuando la prueba de concepto sea un juego para navegador. Este enfoque debe definir lo que el jugador
puede hacer, el primer ciclo jugable, el motor, el flujo de trabajo para los recursos, el HUD, los controles y cómo se probará en el navegador
antes de ampliar el juego.

## Flujo de trabajo para iterar

Una buena prueba de concepto se limita a un MVP que pueda implementarse rápidamente y validarse con el equipo.
Si quieres asegurarte de que el MVP funcione según lo esperado, puedes usar Playwright interactive para que Codex verifique su propio trabajo.

Una vez que tengas una primera versión en funcionamiento, puedes iterar sobre ella pidiendo cambios puntuales en el mismo chat:
