<!-- source: https://learn.chatgpt.com/es-419/use-cases/ios-liquid-glass -->

## Partir de iOS 26 como base

Aborda primero Liquid Glass como un proyecto de migración a iOS 26 y Xcode 26. Vuelve a compilar la app con el SDK de iOS 26, revisa qué obtienes automáticamente de los controles estándar de SwiftUI y, solo entonces, pídele a Codex que rediseñe las partes personalizadas que todavía se vean demasiado planas, pesadas o desconectadas de la interfaz del sistema.

Si la app aún admite versiones anteriores de iOS, deja clara esa restricción desde el principio. La habilidad de Liquid Glass para SwiftUI del [complemento Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) debe condicionar el uso de las nuevas API exclusivas de Liquid Glass con `#available(iOS 26, *)` y conservar una alternativa que siga viéndose bien en dispositivos anteriores.

## Aprovechar el complemento para iOS

Usa el [complemento Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) cuando quieras que Codex combine cambios en la IU de SwiftUI con una verificación en el simulador. Para trabajar con Liquid Glass, conviene pedirle a Codex que audite un flujo, migre un conjunto pequeño de superficies, ejecute la versión resultante en un simulador de iOS 26 y tome capturas de pantalla antes de ampliar el alcance.

Ese complemento incluye una habilidad de Liquid Glass para SwiftUI con un conjunto sencillo de valores predeterminados que conviene incorporar a tu prompt:

- Prioriza las API nativas `glassEffect` y `GlassEffectContainer`, los estilos de botones de Liquid Glass y las transiciones de `glassEffectID`, en lugar de las vistas de desenfoque personalizadas.
- Aplica `.glassEffect(...)` después de los modificadores de diseño y visuales para que el material se ajuste a la forma final que realmente quieres.
- Agrupa los elementos relacionados de Liquid Glass dentro de `GlassEffectContainer` cuando aparezcan juntas varias superficies.
- Usa `.interactive()` solo en botones, chips y controles que realmente respondan al tacto.
- Mantén uniformes la forma de las esquinas, los tintes y el espaciado en toda la funcionalidad, en lugar de mezclar tratamientos puntuales de Liquid Glass.
- Conserva una alternativa sin Liquid Glass para destinos de implementación anteriores a iOS 26.

Para obtener más información sobre cómo instalar complementos y habilidades, consulta nuestra documentación sobre [complementos](/es-419/codex/plugins) y [habilidades](/es-419/codex/build-skills).

## Ver las sesiones de la WWDC

Estas sesiones de WWDC25 son un buen material de referencia antes de pedirle a Codex que refactorice un flujo real de producción:

- [Conoce Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/)
- [Conoce el nuevo sistema de diseño](https://developer.apple.com/videos/play/wwdc2025/356/)
- [Crea una app de SwiftUI con el nuevo diseño](https://developer.apple.com/videos/play/wwdc2025/323/)
- [Crea una app de UIKit con el nuevo diseño](https://developer.apple.com/videos/play/wwdc2025/284/)
- [Novedades en SwiftUI](https://developer.apple.com/videos/play/wwdc2025/256/)

## Pedir un plan de migración y luego una parte acotada

Las migraciones a Liquid Glass dan mejores resultados cuando Codex separa “¿dónde debería aparecer Liquid Glass?” de “escribe todo el código ahora”. Primero pide una auditoría rápida y luego deja que el agente implemente una parte independiente con verificación en el simulador.

## Consejos prácticos

### No apliques Liquid Glass a todo

Liquid Glass debería crear una capa de controles bien definida sobre el contenido, no convertir cada tarjeta en un panel brillante. Pide a Codex que elimine los fondos decorativos que entran en conflicto con los materiales del sistema, conserve el contenido sin efectos donde la legibilidad sea más importante y reserve los tintes para dar énfasis semántico o destacar acciones principales.

### Comienza con un flujo muy utilizado

La pantalla raíz de una pestaña, una pantalla de detalles, una hoja modal, una interfaz de búsqueda o un flujo de incorporación suele ser un mejor primer objetivo de migración que una migración integral de toda la app. Esto facilita la revisión y deja claro qué decisiones sobre Liquid Glass deberían convertirse en patrones reutilizables de componentes.

### Revisar detenidamente el comportamiento alternativo

Si el destino de implementación de tu app es una versión anterior a iOS 26, pide a Codex que muestre la implementación alternativa junto a la versión de Liquid Glass. Este paso de revisión permite detectar regresiones accidentales en la disponibilidad de las API y evita publicar una migración que solo funciona en el simulador más reciente.
