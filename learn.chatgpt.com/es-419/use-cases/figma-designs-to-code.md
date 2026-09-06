<!-- source: https://learn.chatgpt.com/es-419/use-cases/figma-designs-to-code -->

## Introducción

Cuando tienes una selección exacta de Figma, Codex puede convertirla en una interfaz pulida sin ignorar los patrones ya establecidos en tu proyecto.

Con la habilidad de Figma, Codex puede usar el servidor MCP de Figma para obtener contexto de diseño estructurado, variables, recursos y la variante exacta que debe implementar.

Con la habilidad interactiva de Playwright, Codex puede abrir la aplicación en un navegador real, comparar la implementación con la referencia de Figma y hacer ajustes iterativos en la disposición o el comportamiento hasta acercar el resultado al objetivo.

## Configura tu proyecto de Figma

Cuanto más ordenado esté tu archivo de Figma, mejor será la primera implementación. Para facilitar el traspaso:

- Usa variables o tokens de diseño siempre que sea posible, en especial para colores, tipografía y espaciado
- Crea componentes para los elementos reutilizables de la interfaz en lugar de repetir capas sueltas
- Usa el diseño automático siempre que sea posible en lugar del posicionamiento manual
- Mantén los nombres de los frames y las capas lo suficientemente claros para que la pantalla principal, el estado y las variantes sean evidentes
- Conserva los íconos y las imágenes reales en el archivo cuando sea posible para que Codex no tenga que adivinar

Así, Codex tendrá una estructura más adecuada para convertirla en una interfaz sólida y lista para producción.

## Sé específico

Cuanto más específico seas sobre los patrones de interacción esperados y el estilo que buscas, mejor será el resultado.

Si un estado, breakpoint o interacción es importante, indícalo expresamente. Si el archivo contiene varias variantes muy similares, dile a Codex cuál debe tomar como referencia definitiva.

Cuanto más claramente indiques qué debe coincidir exactamente y en qué casos deben prevalecer las convenciones del repositorio, más fácil le resultará a Codex decidir qué priorizar.

## Prepara el sistema de diseño

Codex funciona mejor cuando el repositorio de destino ya cuenta con una capa de componentes bien definida. Codex puede usar automáticamente tus componentes y tu sistema de diseño existentes en lugar de recrearlos desde cero.

Si lo consideras necesario, indícale a Codex qué componentes base debe reutilizar, dónde están tus tokens y qué considera canónico el repositorio en cuanto a botones, campos de entrada, tarjetas, tipografía e íconos.

Trata el resultado del MCP de Figma, que suele tener el aspecto de código de React con Tailwind, como una referencia estructural y no como el estilo de código definitivo. Pídele a Codex que adapte ese resultado a la implementación real del proyecto: sus utilidades, wrappers de componentes, sistema de colores, escala tipográfica, tokens de espaciado, enrutamiento, gestión del estado y patrones de obtención de datos.

## Flujo de trabajo

### Comienza con una selección de Figma

Copia un enlace al frame, componente o variante exactos de Figma que quieres implementar. El flujo del MCP de Figma funciona mediante enlaces, por lo que el enlace debe apuntar al nodo exacto que quieres y no a un frame padre cercano.

### Pídele a Codex que use Figma

Figma debe guiar la primera iteración. Pídele a Codex que siga el flujo del MCP de Figma antes de comenzar a implementar.

Incluye lo siguiente en tu prompt:

Una vez lista la primera implementación, Codex usará Playwright para verificar la interfaz en un navegador real y corregir cualquier diferencia visual o de interacción que aún quede.
