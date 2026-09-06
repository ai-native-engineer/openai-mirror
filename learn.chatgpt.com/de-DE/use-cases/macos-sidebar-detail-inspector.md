<!-- source: https://learn.chatgpt.com/de-DE/use-cases/macos-sidebar-detail-inspector -->

## Mit dem Szenenmodell für den Mac beginnen

Dieser Anwendungsfall zeigt, wie du aus einer App-Idee ein Grundgerüst für eine Mac-App machst, das sich wie für den Desktop entwickelt anfühlt und nicht wie ein vergrößerter, für Touch-Bedienung konzipierter Stack. Lass Codex zuerst das Szenenmodell auswählen und dann das Hauptfenster mit einer stabilen Auswahl in der Seitenleiste, einem Detailbereich und einem Inspektor für zusätzliche Steuerelemente oder Metadaten gestalten.

![Natives Mac-App-Grundgerüst mit Seitenleiste und Detailbereich; in der Seitenleiste ist ein Element ausgewählt und sein Inhalt wird im Detailbereich angezeigt](/images/codex/use-cases/macos-sidebar-detail-inspector.png)

Nutze das [Plug-in Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps), wenn Codex diese Desktop-Struktur umsetzen und die Build-/Run-Schleife weiterhin vorrangig über die Shell abwickeln soll. Der zugehörige Skill für SwiftUI-Muster unter macOS eignet sich für Szenendesign, Seitenleisten, Inspektoren, Befehle, Einstellungen und kleine AppKit-Bridges, wenn SwiftUI ein bestimmtes Mac-spezifisches Verhalten nicht ganz abbilden kann.

## Seitenleiste, Detailbereich und Inspektor erstellen

Bevorzuge `NavigationSplitView`, wenn die Funktion von einer dauerhaften Navigation und einem stabil ausgewählten Element profitiert. Halte die Zeilen der Seitenleiste nativ und schlank, nutze für die Seitenleiste Systemhintergründe und verwende eigene Karten oder umfangreiche Metadaten nur im Detailbereich oder Inspektor.

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

Wenn die App ungewöhnliche Größenverhältnisse in der geteilten Ansicht, eine systemnahe Fensterkoordination oder ein angepasstes Verhalten der Responder Chain benötigt, lass Codex das SwiftUI-Grundgerüst beibehalten und nur die kleinstmögliche AppKit-Bridge ergänzen, die diese konkrete Lücke schließt.

## Befehle, Symbolleisten und Tastaturkurzbefehle in die Desktop-Ebene integrieren

Auf dem Mac sollten wichtige Aktionen in der Menüleiste und der Symbolleiste sowie über Tastaturkurzbefehle auffindbar sein. Lass Codex `commands` auf Szenenebene, kontextsensitive Menüeinträge und Schaltflächen in der Symbolleiste so einbinden, dass sie dieselben App-Aktionen auslösen. So muss niemand nach Bedienelementen suchen, die sich nur per Geste bedienen lassen.

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

Verwende `FocusedValue`, den Szenenzustand oder einen expliziten Auswahlzustand, wenn ein Befehl für das aktuell im Detailbereich angezeigte Element gelten soll. Falls ein Tastaturkurzbefehl an mehreren Stellen registriert würde, lass Codex die Zuständigkeit bündeln, damit es in der App nur einen eindeutigen Weg für diesen Befehl gibt.

## Einstellungen in `Settings` verwalten

Verwende für App-Einstellungen eine eigene Szene vom Typ `Settings` und speichere dauerhafte Nutzereinstellungen mit `@AppStorage`. Das passt in der Regel besser zum Mac, als einen Einstellungs-Screen über die Navigation des Hauptfensters aufzurufen.

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

## App-Konzept im Prompt beschreiben, dann das Grundgerüst validieren

Die besten Ergebnisse erzielst du, wenn du im Prompt das App-Konzept, die zentralen Inhaltsobjekte und die wichtigsten Aktionen nennst und Codex anschließend bittest, zuerst das Desktop-Grundgerüst für diesen Workflow zu entwickeln. Lass den Agenten einen kleinen Build-/Run-Test ausführen und die Szenenstruktur, die Einbindung der Befehle, die Zustandsverwaltung sowie alle Stellen zusammenfassen, an denen AppKit eingebunden werden musste.

## Praktische Tipps

### Seitenleiste nativ halten

Verwende in den Zeilen der Seitenleiste ein Symbol, eine Titelzeile und höchstens eine kurze Zusatzzeile. Verschiebe umfangreichere Karten, Zähler und Metadaten in den Detailbereich oder Inspektor, damit die Liste in der Seitenleiste leicht zu überblicken bleibt.

### Einstellungen nicht im Haupt-Stack verstecken

Wenn eine Einstellung für die gesamte App gilt, lass Codex das entsprechende Steuerelement unter `Settings` platzieren, den Wert mit `@AppStorage` speichern und einen Einstieg über das App-Menü bereitstellen, statt einen weiteren Einstellungs-Screen über die Navigation aufzurufen.

### AppKit nur für klar begrenzte Desktop-Lücken verwenden

Wenn die Funktion Dialoge zum Öffnen und Speichern, die Steuerung des First Responders oder eine eigene `NSView` benötigt, setze AppKit nur als kleine Ergänzung zu einem von SwiftUI verwalteten Zustandsmodell ein, statt das gesamte Fenster in AppKit neu zu schreiben.
