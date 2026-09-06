<!-- source: https://learn.chatgpt.com/es-419/use-cases/ios-app-intents -->

## Haz visibles para el sistema las partes adecuadas de tu app

App Intents es una de las formas más claras de hacer que una app de iOS sea más útil fuera de su propia UI. En lugar de tratar tu app como un espacio cerrado que solo funciona cuando alguien la abre y navega por ella, usa Codex para exponer las acciones y los objetos que deben estar disponibles en Shortcuts, Siri, Spotlight, widgets, controles y las experiencias más recientes del sistema basadas en asistentes.

Esto resulta útil hoy para la visibilidad y la automatización, y es un paso sólido de preparación para un futuro en el que los asistentes tengan un papel más central. Si tu app ya sabe cómo redactar, abrir, filtrar, enrutar o resumir algo útil, App Intents le ofrece al sistema una forma estructurada de solicitar esa capacidad.

## Comienza por las acciones y entidades, no por todas las pantallas

En una primera implementación de App Intents, lo mejor no suele ser “reflejar toda la app”. Pídele a Codex que identifique:

- las pocas acciones que un usuario querría activar sin navegar por toda la interfaz
- los objetos de la app que el sistema debe comprender para dirigir correctamente esas acciones
- qué flujos de trabajo deben abrir la app en un estado específico y cuáles deben completarse directamente desde una superficie del sistema

Las recomendaciones de Apple sobre App Intents ofrecen un buen marco para hacerlo: define la acción, define la capa de entidades que necesita el sistema y luego haz que esas acciones sean fáciles de encontrar y reutilizar en distintas experiencias del sistema. Las referencias más útiles son [Hacer que las acciones y el contenido se puedan descubrir y estén ampliamente disponibles](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-and-widely-available), [Crear tu primera intención de app](https://developer.apple.com/documentation/appintents/creating-your-first-app-intent) y el ejemplo de experiencias del sistema [Adoptar App Intents para admitir experiencias del sistema](https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences).

## Piensa en las superficies del sistema, no solo en Shortcuts

La oportunidad va más allá de “agregar un atajo”. Una buena capa de App Intents puede hacer que tu app sea útil en varios lugares:

- Shortcuts, donde los usuarios pueden ejecutar acciones directamente o integrarlas en automatizaciones más amplias
- Siri, donde la app puede exponer verbos significativos y enlaces profundos, en lugar de limitarse a abrirse de forma genérica
- Spotlight, donde las entidades de la app y los App Shortcuts se convierten en puntos de entrada del sistema fáciles de encontrar
- widgets, Live Activities, controles y otras superficies de UI basadas en intenciones
- experiencias más recientes orientadas a asistentes, donde las acciones y entidades estructuradas le resultan al sistema mucho más fáciles de entender que los flujos arbitrarios de la UI

## Sigue un patrón de app real

Esto suele funcionar mejor cuando la app adopta una estructura como la siguiente:

- un target dedicado a App Intents, en lugar de dispersar tipos de intenciones entre archivos de la app que no guardan relación
- entradas de `AppShortcutsProvider` para acciones valiosas para el usuario, como redactar una publicación o abrir la app en una pestaña específica
- tipos `AppEntity` pequeños para elementos sobre los que el sistema necesita razonar, como cuentas, listas y filtros de cronología
- un manejo de intenciones que redirija correctamente a la escena principal de la app, de modo que una intención invocada pueda abrir el flujo de redacción correcto o cambiar la app a la pestaña adecuada

Para la mayoría de las apps, le pediría a Codex que siguiera este patrón: comenzar con una pequeña capa de acciones orientada al sistema, mantener acotada la capa de entidades y configurar un retorno predecible a la app en tiempo de ejecución cuando la intención necesite la UI principal.

## Pídele a Codex que diseñe la primera capa de intenciones

El prompt más eficaz en este caso le proporciona a Codex los objetos principales y las acciones más importantes de tu app; luego le pide que elija la capa inicial de App Intents más pequeña que resulte útil, en lugar de exponerlo todo indiscriminadamente.

## Consejos prácticos

### Expón los verbos que los usuarios realmente quieren usar fuera de la app

Las primeras intenciones más adecuadas suelen ser acciones como redactar, abrir, buscar, filtrar, iniciar, continuar o inspeccionar. Si una acción solo resulta útil después de un largo flujo de configuración dentro de la app, quizá no deba incluirse en la primera implementación de App Intents.

### Mantén las entidades más acotadas que la capa de modelos

Por lo general, el sistema no necesita todo tu modelo de persistencia. Pídele a Codex que defina la capa más pequeña de entidades de la app que aun así les brinde a Siri, Shortcuts y Spotlight contexto suficiente para enrutar y mostrar correctamente la acción.

### Considéralo infraestructura para asistentes, no solo una función de Shortcuts

Aunque tu primera versión solo aporte mejoras visibles a Shortcuts o Siri, la ventaja de fondo es que tu app empieza a expresarse mediante acciones y entidades estructuradas. Eso le facilita participar en futuros puntos de entrada del sistema e impulsados por IA, en comparación con una app cuyas capacidades solo están codificadas en toques y jerarquías de vistas.
