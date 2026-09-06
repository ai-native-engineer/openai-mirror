<!-- source: https://learn.chatgpt.com/de-DE/use-cases/native-macos-apps -->

## App-Grundstruktur anlegen und Build-Ablauf einrichten

Wenn du eine neue Mac-App entwickelst, bitte Codex, zuerst das passende Szenenmodell auszuwählen: `WindowGroup`, `Window`, `Settings`, `MenuBarExtra` oder `DocumentGroup`. So ist die App von Anfang an nativ für den Desktop ausgelegt, statt auf einer `ContentView` im Stil von iOS aufzubauen.

Führe den Ausführungszyklus primär über die Shell aus. Verwende für Projekte in Xcode `xcodebuild`. Nutze für paketbasierte Apps `swift build` und das projektlokale Wrapper-Skript `script/build_and_run.sh`, das den alten Prozess beendet, die App erstellt, das neue Artefakt startet und optional Logs oder Telemetriedaten bereitstellt.

Wenn es sich bei einer reinen SwiftPM-App um eine GUI-App handelt, bündele und starte sie als `.app`, statt die unverpackte ausführbare Datei direkt auszuführen. So vermeidest du bei der lokalen Validierung Probleme mit der Dock-Integration, der Aktivierung und der Bundle-Identität.

## Skills nutzen

Füge das [Plug-in Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) hinzu, sobald speziellere Desktop-Aufgaben anstehen. Es deckt Build- und Debugging-Abläufe über die Shell, die Paketierung von SwiftPM-Apps, native SwiftUI-Muster für Szenen und Fenster, die Interoperabilität mit AppKit, einheitliches Logging, die Einordnung von Testfehlern sowie Arbeitsabläufe für Codesignierung und Notarisierung ab.

Weitere Informationen dazu, wie du Plug-ins und Skills installierst und verwendest, findest du in der [Dokumentation zu Plug-ins](/de-DE/codex/plugins) und der [Dokumentation zu Skills](/de-DE/codex/build-skills).

## Native Desktop-UI entwickeln

Bevorzuge Mac-Konventionen gegenüber iOS-Navigationsmustern. Verwende `NavigationSplitView` für Layouts mit Seitenleiste und Detailansicht, für Einstellungen explizite Szenen vom Typ `Settings`, Symbolleisten und Befehle für leicht auffindbare Aktionen sowie Menüleisten-Extras für schlanke, jederzeit verfügbare Dienstprogramme.

Verwende zunächst Systemmaterialien, semantische Farben und Standardsteuerelemente. Füge benutzerdefinierte Fensterstile, Ziehbereiche oder Oberflächen mit Liquid Glass nur hinzu, wenn das Produkt eine unverwechselbare Desktop-Oberfläche erfordert.

Wenn SwiftUI die Anforderungen fast, aber nicht vollständig abdeckt, füge eine möglichst kleine AppKit-Bridge hinzu. Gute Beispiele sind Dialoge zum Öffnen und Sichern, die Steuerung des First Responders, die Validierung von Menüs, Sonderfälle beim Drag-and-drop und eine in SwiftUI eingebundene Instanz von `NSView` für ein spezialisiertes Steuerelement.

## Debuggen, testen und die Veröffentlichung vorbereiten

Bitte Codex, für das Laufzeitverhalten einige Vorgänge mit `Logger` zu protokollieren, etwa das Öffnen von Fenstern, die Auswahl in der Seitenleiste, Menübefehle oder die Hintergrundsynchronisierung, und die Ereignisse nach dem Start der App mit `log stream` zu überprüfen.

Lass Codex bei fehlgeschlagenen Tests zuerst den kleinsten sinnvollen Testumfang mit `xcodebuild test` oder `swift test` ausführen und einordnen, ob es sich um einen Kompilierungsfehler, einen Assertion-Fehler, einen Absturz, einen sporadischen Testfehler oder ein Problem mit Umgebung oder Setup handelt.

Wenn sich die Arbeit von lokalen Iterationen auf die Verteilung verlagert, bitte Codex, sowohl einen Ablauf für die manuelle Archivierung in Xcode als auch einen skriptgestützten Ablauf für Archivierung und Notarisierung vorzubereiten, damit sich Veröffentlichungen zuverlässig wiederholen lassen. Lass Codex das App-Bundle, die Berechtigungen und die gehärtete Laufzeitumgebung mit `codesign` und `plutil` prüfen und [App Store Connect CLI](https://asccli.sh/) verwenden, wenn auch die Uploads über das Terminal erfolgen sollen.

## Beispiel-Prompt

## Praktische Tipps

### Szenen explizit modellieren

Modelliere das Hauptfenster, das Einstellungsfenster, die Dienstprogrammfenster und die Menüleisten-Extras jeweils als eigenständige Szenen, statt die gesamte App in einer einzigen riesigen Ansicht zu verstecken.

### Die Systemoberfläche stärker nutzen

Bevor du benutzerdefinierte Seitenleisten, Symbolleisten oder Materialien erstellst, prüfe, ob die standardmäßigen Szenen- und Fenster-APIs von SwiftUI das gewünschte Mac-Verhalten bereits bieten.

### AppKit nur gezielt einsetzen

Verwende `NSViewRepresentable`, `NSViewControllerRepresentable` oder eine gezielte Hilfskomponente auf Basis von `NSWindow`, um genau eine fehlende Desktop-Funktion abzudecken. SwiftUI sollte jedoch die maßgebliche Quelle für Auswahl und App-Zustand bleiben.

### Codesignierung und Notarisierung unabhängig vom lokalen Build-Erfolg prüfen

Ein erfolgreicher lokaler Start beweist nicht, dass die App signiert oder zur Notarisierung bereit ist. Behalte für einmalige Prüfungen vor der Veröffentlichung einen Ablauf für die manuelle Archivierung in Xcode bei, ergänze für die wiederholbare Verteilung einen skriptgestützten Ablauf für Archivierung und Notarisierung und führe Prüfungen mit `codesign` und `plutil` aus, wenn es um die Veröffentlichung und nicht nur um lokale Iterationen geht.
