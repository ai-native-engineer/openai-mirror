<!-- source: https://learn.chatgpt.com/es-419/use-cases/frontend-designs -->

## Introducción

Cuando tengas capturas de pantalla, un breve documento de diseño o algunas referencias que sirvan de inspiración, Codex puede convertir todo eso en una UI responsiva sin dejar de respetar los patrones ya establecidos en tu proyecto.

Con la habilidad de Playwright, Codex puede abrir la aplicación en un navegador real, comparar la implementación con tus capturas de pantalla en distintos tamaños de pantalla y ajustar la disposición o el comportamiento hasta que el resultado se acerque al objetivo.

## Comienza con referencias

Proporciona a Codex las referencias más claras que tengas sobre la UI que buscas. Una sola captura de pantalla puede bastar para una tarea acotada, pero podrás comunicar mejor el diseño si incluyes varios estados, como diseños para computadoras de escritorio y dispositivos móviles, estados al pasar el cursor o de selección, y vistas vacías o de carga relevantes.

No es necesario que las referencias sean entregables de diseño perfectos. Solo deben comunicar con suficiente claridad la jerarquía, el espaciado y la intención visual para que Codex no tenga que adivinar.

## Sé específico

Cuanto más específicas sean tus indicaciones sobre los patrones de interacción esperados y el estilo que buscas, mejor será el resultado.
El modelo tiende a usar de forma predeterminada los patrones y estilos más comunes, por lo que, si tus referencias no dejan claro que buscas algo diferente, la UI puede verse genérica.
Cuanta más información proporciones, ya sea en forma de otras referencias visuales o de instrucciones más específicas, más probabilidades tendrás de obtener una UI que se destaque.

## Prepara el sistema de diseño

Codex funciona mejor cuando el repositorio de destino ya tiene una capa de componentes bien definida. Codex puede usar automáticamente los componentes y el sistema de diseño que ya tienes, en lugar de recrearlos desde cero.

Si es necesario, por ejemplo, cuando no usas una pila tecnológica estándar, indícale a Codex qué primitivas reutilizar, dónde están tus tokens y qué establece el repositorio como estándar para botones, campos de entrada, tarjetas, tipografía e íconos.

Si partes de una base de código existente, es muy probable que Codex entienda por su cuenta cómo usar tus componentes y tu sistema de diseño. Sin embargo, si comienzas desde cero, conviene darle instrucciones explícitas.

Pídele a Codex que tome las capturas de pantalla como objetivo visual, pero que adapte ese objetivo a las utilidades, los wrappers de componentes, el sistema de colores, la escala tipográfica, los tokens de espaciado, el enrutamiento, la gestión del estado y los patrones de obtención de datos que realmente usa el proyecto.

## Aprovecha Playwright

Playwright es una excelente herramienta para ayudar a Codex a perfeccionar la UI mediante iteraciones. Con esta herramienta, Codex puede abrir la aplicación en un navegador real, comparar la implementación con las capturas de pantalla que proporcionaste y ajustar la disposición o el comportamiento.

Codex puede cambiar el tamaño de la ventana del navegador para probar distintos tamaños de pantalla y comprobar la disposición en diferentes puntos de quiebre.

Asegúrate de que la habilidad interactiva de Playwright esté habilitada en Codex. Para obtener más información, consulta la [documentación sobre Habilidades](/es-419/docs/build-skills).

## Itera

La primera versión ya debería acercarse en líneas generales a las capturas de pantalla. Si se trata de un diseño complejo, de interacciones complejas o de una UI con muchas animaciones, probablemente necesitarás varias rondas de ajustes.

Pídele a Codex que compare la implementación con las capturas de pantalla en vez de limitarse a comprobar si la página se compila correctamente. Cuando surjan conflictos, debe dar prioridad a los tokens del sistema de diseño del repositorio y limitarse a los ajustes mínimos de espaciado o tamaño necesarios para conservar la apariencia general del diseño.

Usa capturas de pantalla adicionales o notas breves si ayudan a aclarar estados que no sean evidentes en una sola imagen.

### Prompt de seguimiento sugerido
