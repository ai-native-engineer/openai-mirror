<!-- source: https://learn.chatgpt.com/es-419/use-cases/macos-sidebar-detail-inspector -->

## Comienza con el modelo de escenas de Mac

Este caso de uso permite convertir una idea de app en la estructura base de una app para Mac que parezca diseñada para el escritorio, no como una adaptación de una pila pensada primero para interfaces táctiles. Pídele a Codex que elija primero el modelo de escenas y luego diseñe la ventana principal en torno a una selección estable de la barra lateral, un área de detalles y un inspector para controles o metadatos secundarios.

![Estructura base de una app nativa para Mac con barra lateral y panel de detalles, un elemento seleccionado en la barra lateral y contenido en el panel de detalles](/images/codex/use-cases/macos-sidebar-detail-inspector.png)

Usa el [complemento Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) cuando quieras que Codex aplique esa estructura de escritorio y mantenga el ciclo de compilación y ejecución centrado en la línea de comandos. Su habilidad de patrones de SwiftUI para macOS es adecuada para diseñar escenas, barras laterales, inspectores, comandos y opciones de configuración, además de pequeños puentes de AppKit cuando SwiftUI no puede expresar claramente un comportamiento específico de Mac.

## Crea una barra lateral, un panel de detalles y un inspector

Prefiere `NavigationSplitView` cuando la función se beneficie de una navegación persistente y una selección estable. Mantén las filas de la barra lateral nativas y ligeras, usa fondos del sistema para la barra lateral y reserva las tarjetas personalizadas o los metadatos densos para el panel de detalles o el inspector.

```swift
struct LibraryRootView: View {
  @SceneStorage("LibraryRootView.selection") private var selection: Item.ID?
  @SceneStorage("LibraryRootView.showInspector") private var showInspector = true

  var body: some View {
    NavigationSplitView {
      List(selection: $selection) {
        ForEach(items) { item in
          Label(item.title, systemImage: item.systemImage)
            .tag(item.id)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Library")
    } detail: {
      ItemDetailView(selection: selection)
        .inspector(isPresented: $showInspector) {
          ItemInspectorView(selection: selection)
        }
    }
  }
}

Si la app necesita dimensiones inusuales en la vista dividida, coordinación de ventanas a bajo nivel o un comportamiento personalizado de la cadena de respondedores, pídele a Codex que mantenga intacta la estructura de SwiftUI y agregue solo el puente de AppKit más pequeño necesario para resolver esa limitación.

## Coloca los comandos, las barras de herramientas y los atajos en la capa de escritorio

Los usuarios de Mac deben poder encontrar acciones importantes en la barra de menús, la barra de herramientas y los atajos de teclado. Pídele a Codex que vincule los `commands` a nivel de escena, los elementos de menú sensibles al contexto y los botones de la barra de herramientas con las mismas acciones de la app, para que los usuarios de escritorio no tengan que buscar controles disponibles solo mediante gestos.

```swift
@main
struct LibraryApp: App {
  var body: some Scene {
    WindowGroup {
      LibraryRootView()
    }
    .commands {
      CommandMenu("Library") {
        Button("New Item") {
          // Create a new item.
        }
        .keyboardShortcut("n")

        Button("Toggle Inspector") {
          // Route this command to the focused window or selected item state.
        }
        .keyboardShortcut("i", modifiers: [.command, .option])
      }
    }

    Settings {
      LibrarySettingsView()
    }
  }
}

Usa `FocusedValue`, el estado de la escena o un estado de selección explícito cuando un comando deba aplicarse al elemento que se muestra actualmente en el panel de detalles. Si un atajo fuera a registrarse en varios lugares, pídele a Codex que centralice su administración para que la app tenga una única ruta clara para el comando.

## Mantén las preferencias en `Settings`

Para las preferencias de la app, usa una escena dedicada de `Settings` y conserva con `@AppStorage` las opciones del usuario que deban persistir. Esto suele ser más adecuado en Mac que insertar una pantalla de configuración en la pila de navegación de la ventana de contenido principal.

```swift
struct LibrarySettingsView: View {
  @AppStorage("showItemMetadata") private var showItemMetadata = true

  var body: some View {
    TabView {
      Form {
        Toggle("Show Item Metadata", isOn: $showItemMetadata)
      }
      .tabItem { Label("General", systemImage: "gearshape") }
    }
    .frame(width: 460, height: 260)
    .scenePadding()
  }
}

## Describe el concepto de la app en el prompt y luego valida la estructura base

Esta página funciona mejor cuando tu prompt especifica el concepto de la app, los objetos de contenido principales y las acciones principales, y luego le pide a Codex que primero cree la estructura de escritorio en torno a ese flujo de trabajo. Haz que el agente ejecute una comprobación breve de compilación y ejecución y resuma la estructura de escenas, la conexión de comandos, la propiedad del estado y cualquier caso especial que haya tenido que resolver con un puente de AppKit.

## Consejos prácticos

### Mantén nativa la barra lateral

Usa un ícono, una línea de título y, como máximo, una línea secundaria breve en las filas de la barra lateral. Traslada las tarjetas con más información, los contadores y los metadatos al panel de detalles o al inspector para que la lista de origen siga siendo fácil de revisar de un vistazo.

### Evita ocultar la configuración en la pila principal

Si una preferencia de usuario afecta a toda la app, pídele a Codex que coloque ese control en `Settings` con `@AppStorage` y que proporcione un punto de acceso desde el menú de la app, en vez de crear otra pantalla de configuración en la pila de navegación.

### Reserva AppKit para necesidades puntuales del escritorio

Si la función necesita paneles para abrir o guardar archivos, control del primer respondedor o una `NSView` personalizada, usa AppKit solo como una pequeña capa alrededor de un modelo de estado administrado por SwiftUI, en vez de reescribir toda la ventana con AppKit.
