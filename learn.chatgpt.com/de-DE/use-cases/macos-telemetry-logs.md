<!-- source: https://learn.chatgpt.com/de-DE/use-cases/macos-telemetry-logs -->

## Einen Logger hinzufügen, wenn Debugging zu vage wird

Dieser Anwendungsfall eignet sich für Abläufe in Mac-Apps, bei denen „etwas ist passiert“ zu vage ist, um Fehler allein durch eine Codeüberprüfung zu finden. Lass Codex für ein bestimmtes Verhalten einige wenige aussagekräftige Einträge im Unified Logging ergänzen, die App ausführen und das Verhalten auslösen. Prüfe anschließend in der Konsole oder mit `log stream`, ob die erwarteten Ereignisse ausgelöst wurden.

Verwende für diese Schleife das [Plug-in „Build macOS Apps“](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps). Sein Skill für macOS-Telemetrie ist bewusst schlank gehalten: Verwende Apples `Logger`, wähle ein eindeutiges Paar aus Subsystem und Kategorie, protokolliere Aktionsgrenzen und Zustandsübergänge, vermeide sensible Nutzdaten und prüfe das Ereignis, nachdem du die App lokal gebaut und ausgeführt hast, statt davon auszugehen, dass die Instrumentierung korrekt eingebunden ist.

## Warum Telemetrie bei agentischer Softwareentwicklung nützlich ist

Aussagekräftige Logs bieten Codex nach jedem Patch eine reproduzierbare Feedbackschleife. Statt dass du jedes Fenster, jede Menüaktion oder jeden Synchronisierungsübergang manuell prüfen musst, kann der Agent die App ausführen, den Ablauf durchspielen, gefilterte Logs auswerten und anhand der Ergebnisse entscheiden, welche Codeänderung als Nächstes erforderlich ist.

Das ist besonders bei drei agentischen Schleifen nützlich:

- **Debugging-Schleife ohne manuelles Eingreifen:** Codex instrumentiert einen verdächtigen Ablauf, startet die App, klickt in der Seitenleiste oder löst einen Befehl aus, wertet die ausgegebene Log-Sequenz aus, korrigiert den Pfad für Zustandsaktualisierungen und führt denselben Ablauf erneut aus, bis Logs und UI-Verhalten übereinstimmen.
- **Schleife zur Erfassung von App-Sitzungen:** Codex fügt jeweils ein Ereignis für den App-Start, das Öffnen eines Fensters, die Auswahl in der Seitenleiste sowie Start, Abschluss und Fehlschlagen eines Imports hinzu. Anschließend führt Codex eine lokale App-Sitzung durch und fasst die resultierende Zeitleiste zusammen, sodass fehlende oder in der falschen Reihenfolge auftretende Übergänge sofort auffallen.
- **Manuell gesteuerte Erfassungsschleife:** Codex startet die App mit aktivierter Protokollierung und lässt einen gezielt gefilterten Log-Stream laufen, während du einen schwierigen Ablauf manuell durchspielst. Anschließend prüft Codex die erfasste Sitzung und schlägt anhand dieses Traces den nächsten Patch vor.

## Instrumentierung sparsam und filterbar halten

Lass Codex für jeden Funktionsbereich je einen Logger einrichten, statt für jede Zustandsänderung eine dauerhafte Log-Zeile anzulegen. Funktionskategorien wie `Windowing`, `Commands`, `MenuBar`, `Sidebar`, `Sync` oder `Import` erleichtern es erheblich, die Logs beim nächsten Debugging-Durchlauf zu filtern.

```swift

private let logger = Logger(
  subsystem: Bundle.main.bundleIdentifier ?? "SampleApp",
  category: "Sidebar"
)

@MainActor
func selectItem(_ item: SidebarItem) {
  logger.info("Selected sidebar item: \(item.id, privacy: .public)")
  selection = item.id
}

Verwende `info` für knappe Aktions- und Lebenszyklusereignisse, die langfristig nützlich bleiben sollen, und `debug` für umfangreichere lokale Zustandsdetails, die vor Abschluss der Aufgabe entfernt oder herabgestuft werden können. Füge Signposts nur hinzu, wenn du eine Zeitspanne misst, und nicht standardmäßig.

## Lass Codex das Ereignis anhand der Logs nachweisen

Es reicht nicht, nur Aufrufe von `Logger` hinzuzufügen. Lass Codex die App ausführen, den instrumentierten Ablauf auslösen und dir den genauen Filter für die Konsole oder das verwendete Prädikat für `log stream` sowie ein oder zwei repräsentative Log-Zeilen nennen.

```bash
log stream --style compact --predicate 'subsystem == "com.example.app" && category == "Sidebar"'

Wenn ein erwartetes Ereignis nicht erscheint, lass Codex die Protokollierung näher an den vermuteten Kontrollpfad verschieben, denselben Ablauf erneut ausführen und so lange weiterarbeiten, bis aus den Logs hervorgeht, was passiert ist. Wenn sich die Aufgabe zu einer Absturz- oder Backtrace-Analyse entwickelt, nutze stattdessen den Debugging-Workflow des Plug-ins zum Bauen und Ausführen und konzentriere die Telemetrie weiterhin auf die Aktionsgrenzen.

## Einen Sitzungs-Trace für einen späteren Codex-Durchlauf speichern

Lass Codex bei länger dauernden oder sporadischen Fehlern einen gezielt gefilterten Log-Stream in einer kleinen lokalen Trace-Datei speichern, die Zeitleiste zusammenfassen und dieses Artefakt im Workspace ablegen. So kann ein späterer Codex-Durchlauf dieselben Belege prüfen, ohne die gesamte Sitzung aus dem Gedächtnis rekonstruieren zu müssen. Das erleichtert das Debugging über mehrere Durchläufe hinweg, wenn ein Agenten-Durchlauf einen Trace erfassen und ein weiterer das Verhalten vor und nach einem Patch vergleichen soll.

Das funktioniert auch gut, wenn du einen Teil der Sitzung selbst steuern musst. Lass Codex die App in einer Debugging-Schleife mit geeigneter Protokollierung starten und eine gefilterte Erfassung beginnen. Codex wartet, während du das Problem manuell reproduzierst, und liest danach die gespeicherte Trace-Datei ein.

## Praxistipps

### Jeweils nur eine Funktion instrumentieren

Konzentriere dich zunächst auf eine Seitenleiste, ein Fenster, einen Befehl oder einen Synchronisierungspfad, damit die Log-Sequenz leicht zu prüfen bleibt. Sobald dieser Pfad zuverlässig funktioniert, kann Codex dasselbe Muster auf benachbarte Abläufe ausweiten.

### Datenschutz in den Prompt aufnehmen

Lass Codex jede protokollierte Kennung erklären und weder Geheimnisse noch personenbezogene Daten oder Rohinhalte im Unified Logging erfassen. Ein kleiner Ereigniswortschatz reicht für lokales Debugging meist aus.

### Beispielausgabe in die abschließende Zusammenfassung aufnehmen

Repräsentative Log-Zeilen schaffen deutlich mehr Vertrauen in die Änderung als die Aussage „Telemetrie wurde hinzugefügt“. Lass Codex das Filterprädikat und eine kurze Zeitleiste der Aktionen aufnehmen, damit der nächste Agenten-Durchlauf dieselbe Prüfschleife wiederverwenden kann.
