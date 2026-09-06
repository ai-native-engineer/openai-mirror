<!-- source: https://learn.chatgpt.com/es-419/use-cases/native-macos-apps -->

## Crear la estructura inicial de la app y el ciclo de compilación

Para una nueva app para Mac, pídele a Codex que primero elija el modelo de escena adecuado: `WindowGroup`, `Window`, `Settings`, `MenuBarExtra` o `DocumentGroup`. De este modo, la app será nativa de escritorio desde la primera iteración, en lugar de crecer a partir de una `ContentView` al estilo de iOS.

Mantén el ciclo de ejecución con la shell como punto de partida. Para proyectos de Xcode, usa `xcodebuild`. Para las apps cuyo punto de partida sea un paquete, usa `swift build` y un script contenedor local del proyecto en `script/build_and_run.sh` que detenga el proceso anterior, compile la app, inicie el nuevo artefacto y, de forma opcional, proporcione logs o telemetría.

Si una app hecha solo con SwiftPM tiene interfaz gráfica, empaquétala e iníciala como una `.app` en lugar de ejecutar directamente el ejecutable sin empaquetar. Así evitas, durante la validación local, problemas por la ausencia de la app en el Dock, la falta de activación o la falta de identidad del paquete.

## Aprovechar las habilidades

Agrega el [complemento Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) cuando el trabajo se vuelva más específico de escritorio. Incluye ciclos de compilación y depuración con la shell como punto de partida, empaquetado de apps con SwiftPM, patrones nativos de SwiftUI para escenas y ventanas, integración con AppKit, registro unificado, diagnóstico de pruebas y flujos de firma y notarización.

Para obtener más información sobre cómo instalar y usar complementos y habilidades, consulta la [documentación de complementos](/es-419/codex/plugins) y la [documentación de habilidades](/es-419/codex/build-skills).

## Crear una interfaz nativa de escritorio

Prefiere las convenciones de Mac a los patrones de navegación de iOS. Usa `NavigationSplitView` para diseños de barra lateral y panel de detalles, escenas `Settings` explícitas para las preferencias, barras de herramientas y comandos para que las acciones sean fáciles de encontrar, y elementos adicionales de la barra de menús para utilidades ligeras que deban estar siempre disponibles.

Usa primero materiales del sistema, colores semánticos y controles estándar. Agrega estilos de ventana personalizados, regiones de arrastre o superficies de Liquid Glass solo cuando el producto necesite una apariencia de escritorio diferenciada.

Si SwiftUI casi logra el comportamiento que necesitas, pero no del todo, agrega la integración más pequeña posible con AppKit. Algunos buenos ejemplos son los paneles de abrir y guardar, el control del primer respondedor, la validación de menús, los casos límite de arrastrar y soltar y una `NSView` encapsulada para un control especializado.

## Depurar, probar y preparar la distribución

Para observar el comportamiento en tiempo de ejecución, pídele a Codex que agregue algunos eventos de `Logger` al abrir ventanas, seleccionar elementos en la barra lateral, ejecutar comandos de menú o sincronizar en segundo plano; luego, verifica esos eventos con `log stream` después de iniciar la app.

En caso de pruebas fallidas, haz que Codex ejecute primero el alcance útil más limitado de `xcodebuild test` o `swift test` y determine si se trata de un error de compilación, una aserción fallida, un bloqueo, una falla intermitente o un problema del entorno o la configuración.

Cuando el trabajo pase de la iteración local a la distribución, pídele a Codex que prepare tanto un proceso de archivado manual en Xcode como uno de archivado y notarización mediante scripts para distribuir de forma repetible. Haz que inspeccione el paquete de la app, las autorizaciones y el entorno de ejecución reforzado con `codesign` y `plutil`, y usa [App Store Connect CLI](https://asccli.sh/) cuando también quieras mantener las cargas en la terminal.

## Prompt de ejemplo

## Consejos prácticos

### Mantener las escenas explícitas

Modela la ventana principal, la ventana de configuración, las ventanas de utilidades y los elementos adicionales de la barra de menús como raíces de escenas independientes, en lugar de ocultar toda la app dentro de una única vista enorme.

### Aprovechar más los componentes del sistema

Antes de crear barras laterales, barras de herramientas o materiales personalizados, comprueba si las API estándar de escenas y ventanas de SwiftUI ya proporcionan el comportamiento de Mac que buscas.

### Limitar AppKit a casos puntuales

Usa `NSViewRepresentable`, `NSViewControllerRepresentable` o un componente auxiliar específico basado en `NSWindow` para cubrir una capacidad de escritorio faltante, pero mantén SwiftUI como la fuente de verdad para la selección y el estado de la app.

### Validar la firma y la notarización por separado del éxito de la compilación local

Que la app se inicie correctamente de forma local no demuestra que esté firmada ni lista para notarizarse. Mantén un flujo de archivado manual en Xcode para comprobaciones puntuales previas al lanzamiento, agrega un flujo de archivado y notarización mediante scripts para una distribución repetible y ejecuta comprobaciones con `codesign` y `plutil` cuando la tarea consista en distribuir, no solo en iterar localmente.
