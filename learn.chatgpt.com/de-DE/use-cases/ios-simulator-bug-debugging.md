<!-- source: https://learn.chatgpt.com/de-DE/use-cases/ios-simulator-bug-debugging -->

## Lass Codex den gesamten Simulator-Ablauf übernehmen

Dieser Anwendungsfall funktioniert am besten, wenn Codex den gesamten Ablauf übernimmt: das richtige App-Target auswählen, die App im Simulator starten, den aktuellen Bildschirm prüfen, die Reproduktionsschritte ausführen, Protokolle und Screenshots erfassen, bei Bedarf einen Stacktrace untersuchen, den Code korrigieren und denselben Ablauf erneut ausführen, um nachzuweisen, dass der Fehler behoben ist.

Wenn Codex diesen Ablauf weiterhin autonom ausführen soll, nutze das [Build iOS Apps-Plug-in](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps). Der iOS-Debugger-Arbeitsablauf des Plug-ins basiert auf XcodeBuildMCP. Dadurch kann Codex mit einem gestarteten Simulator interagieren und dieselben Belege sammeln, die sonst jemand manuell zusammentragen müsste.

Wenn XcodeBuildMCP mit Arbeitsabläufen für Simulator- und UI-Automatisierung, Debugging und Protokollierung konfiguriert ist, kann Codex den gesamten Zyklus aus Reproduktion, Fehlersuche und Verifizierung übernehmen. Falls Codex Projekt, Schema und Simulator noch nicht ausgewählt hat, lass Codex sie zuerst ermitteln und dieses Setup für den Rest der Sitzung wiederverwenden.

## Nutze die Möglichkeiten von XcodeBuildMCP

Fordere Codex auf, die folgenden praktischen Funktionsbereiche zu nutzen:

- Projekt und Simulator ermitteln: prüfen, ob Codex bereits weiß, welches App-Target und welchen Simulator es verwenden soll, das Xcode-Projekt oder den Workspace ermitteln, die Schemata auflisten, einen Simulator finden oder starten und dieses Setup für spätere Build- und Ausführungsschritte unverändert beibehalten.
- Build und Start steuern: einen Build für das aktive App-Target erstellen, den Simulator-Build installieren und starten, die App bei Bedarf mit Protokollerfassung neu starten und ihre Bundle-ID ermitteln, falls Codex app-spezifische Laufzeitprotokolle prüfen muss.
- UI prüfen und bedienen: die Accessibility-Hierarchie des aktuellen Bildschirms einlesen, Screenshots aufnehmen, Bedienelemente antippen, Text in Felder eingeben, durch Listen scrollen und Wischgesten vom Bildschirmrand oder andere Simulatorgesten ausführen.
- Protokolle und Debugger-Zustand: Simulator-Protokolle in Echtzeit abrufen, LLDB an den laufenden App-Prozess anhängen, Breakpoints setzen, Stackframes und lokale Variablen prüfen und Debugger-Befehle ausführen, wenn ein Absturz oder Hänger genauer untersucht werden muss.

Wichtig ist vor allem, dass Codex vor dem Tippen den View-Baum prüft. XcodeBuildMCP stellt die Accessibility-Hierarchie samt Koordinaten bereit. Dadurch kann Codex stabile Labels oder Element-IDs bevorzugen, statt Bildschirmpositionen zu erraten.

## Eine unklare Fehlerbeschreibung in ein reproduzierbares Skript verwandeln

Der iOS-Debugger-Skill liefert die besten Ergebnisse, wenn du in deinem Prompt einen konkreten Fehler und das erwartete Ergebnis nennst und Codex anschließend die App selbstständig steuern und Belege sammeln lässt. Falls eine Anmeldung, ein Deep Link oder eine Test-Fixture erforderlich ist, weise einmal darauf hin und bitte Codex, nur dann anzuhalten, wenn es ohne die fehlende Angabe nicht weitergehen kann.

## Praxistipps

### Fordere nicht nur eine Korrektur, sondern auch Belege an

Bitte Codex um Angaben zum genauen Simulator und zum verwendeten Schema sowie um die Screenshots, Protokollauszüge und Stackdetails, anhand derer der Fehler erklärt wurde. So lässt sich der endgültige Patch wesentlich leichter prüfen als mit der bloßen Aussage: „Ich glaube, das sollte den Fehler beheben.“

### Accessibility-Labels statt Koordinaten bevorzugen

Wenn Codex per Koordinaten tippen muss, weil ein Bedienelement weder ein stabiles Label noch eine Accessibility-ID hat, soll Codex darauf hinweisen. Das ist oft ein Hinweis darauf, dass die Fehlerbehebung auch eine kleine Verbesserung der UI-Testbarkeit umfassen sollte.

### Pro Durchlauf nur einen Fehler bearbeiten

Ein simulatorgestützter Debugging-Zyklus ist leistungsfähig. Seine Ergebnisse sind jedoch leichter einzuschätzen, wenn ein Prompt auf genau eine Fehlerart ausgerichtet ist. Bitte Codex, erst einen Zyklus aus Reproduktion, Fehlerbehebung und Verifizierung abzuschließen, bevor du den Auftrag auf verwandte Probleme ausweitest.
