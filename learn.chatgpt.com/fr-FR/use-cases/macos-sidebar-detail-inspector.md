<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/macos-sidebar-detail-inspector -->

## Commencez par définir le modèle de scènes Mac

Ce cas d’usage permet de transformer une idée en ossature d’application Mac conçue pour un usage sur ordinateur, et non dérivée d’une pile pensée d’abord pour le tactile. Demandez à Codex de commencer par choisir le modèle de scènes, puis de concevoir la fenêtre principale autour d’une sélection stable dans la barre latérale, d’une zone de détail et d’un inspecteur pour les contrôles ou métadonnées secondaires.

![Ossature d’une application Mac native, avec un élément sélectionné dans la barre latérale et son contenu dans le volet de détail](/images/codex/use-cases/macos-sidebar-detail-inspector.png)

Utilisez le [plugin Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) lorsque vous voulez que Codex applique cette structure de bureau et conserve une boucle de compilation/exécution pilotée depuis le shell. Son Skill consacré aux modèles SwiftUI pour macOS convient bien à la conception des scènes, des barres latérales, des inspecteurs, des commandes et des paramètres, ainsi qu’aux petites passerelles AppKit nécessaires lorsque SwiftUI ne couvre pas tout à fait un comportement propre au Mac.

## Créez une barre latérale, un volet de détail et un inspecteur

Privilégiez `NavigationSplitView` lorsque la fonctionnalité bénéficie d’une navigation persistante et d’une sélection stable. Conservez des lignes natives et légères dans la barre latérale, utilisez les arrière-plans système pour celle-ci et réservez les cartes personnalisées ou les métadonnées denses au volet de détail ou à l’inspecteur.

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

Si l’application nécessite un dimensionnement inhabituel des volets, une coordination des fenêtres à bas niveau ou un comportement personnalisé de la chaîne de répondeurs, demandez à Codex de conserver l’ossature SwiftUI intacte et d’ajouter uniquement la plus petite passerelle AppKit nécessaire pour combler cette lacune.

## Placez les commandes, les barres d’outils et les raccourcis dans la couche propre à l’application de bureau

Pour les utilisateurs de Mac, les actions importantes doivent être faciles à repérer dans la barre de menus et la barre d’outils, et accessibles avec des raccourcis clavier. Demandez à Codex de relier aux mêmes actions de l’application les `commands` définies au niveau de la scène, les éléments de menu contextuels et les boutons de la barre d’outils, afin que les utilisateurs n’aient pas à rechercher des contrôles accessibles uniquement par des gestes.

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

Utilisez `FocusedValue`, l’état de la scène ou un état de sélection explicite lorsqu’une commande doit s’appliquer à l’élément actuellement affiché dans le volet de détail. Si un raccourci risque d’être enregistré à plusieurs endroits, demandez à Codex de centraliser sa gestion afin que l’application dispose d’un chemin de commande unique et clairement défini.

## Conservez les préférences dans `Settings`

Pour les préférences de l’application, utilisez une scène `Settings` dédiée et conservez durablement les choix utilisateur avec `@AppStorage`. Cette approche est généralement mieux adaptée à une application Mac que l’ajout d’un écran de paramètres dans la pile de navigation de la fenêtre de contenu principale.

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

## Décrivez le concept de l’application dans le prompt, puis validez son ossature

Cette page donne les meilleurs résultats lorsque votre prompt décrit le concept de l’application, les principaux objets de contenu et les actions essentielles, puis demande à Codex de commencer par bâtir l’ossature de bureau autour de ce workflow. Demandez à l’agent d’effectuer une vérification simple de compilation/exécution et de résumer la structure des scènes, le câblage des commandes, la répartition de la gestion de l’état et les éventuels points nécessitant une passerelle AppKit.

## Conseils pratiques

### Conservez une barre latérale native

Dans les lignes de la barre latérale, utilisez une icône, une ligne de titre et, au maximum, une courte ligne secondaire. Déplacez les cartes plus riches, les compteurs et les métadonnées vers le volet de détail ou l’inspecteur, afin que la liste source reste facile à lire d’un coup d’œil.

### Évitez de placer les paramètres dans la pile principale

Si une préférence utilisateur s’applique à toute l’application, demandez à Codex de placer ce réglage dans `Settings` avec `@AppStorage` et de prévoir un point d’accès depuis le menu de l’application, au lieu de créer un nouvel écran de paramètres dans la pile de navigation.

### Réservez AppKit aux quelques lacunes de SwiftUI sur Mac

Si la fonctionnalité nécessite des panneaux d’ouverture et d’enregistrement, le contrôle du premier répondant ou une `NSView` personnalisée, utilisez AppKit uniquement comme une fine couche d’adaptation autour d’un modèle d’état dont SwiftUI reste responsable, plutôt que de réécrire toute la fenêtre avec AppKit.
