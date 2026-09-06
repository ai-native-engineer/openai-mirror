<!-- source: https://learn.chatgpt.com/de-DE/docs/extend/record-and-replay -->

„Aufzeichnen und Wiedergeben“ ist unter macOS verfügbar. Die Computernutzung muss ebenfalls verfügbar und aktiviert sein.

Mit „Aufzeichnen und Wiedergeben“ kannst du auf deinem Mac einen Ablauf vorführen und daraus einen wiederverwendbaren Skill erstellen. Nutze die Funktion, wenn sich der Ablauf wiederholt, von deinen Präferenzen abhängt oder sich leichter vorführen als in einem Prompt beschreiben lässt.

Du kannst beispielsweise aufzeichnen, wie du eine Spesenabrechnung einreichst, einen Parkplatz buchst, ein korrekt konfiguriertes Issue erstellst, ein Video veröffentlichst oder einen wiederkehrenden Bericht herunterlädst. ChatGPT oder Codex kann aus diesem Muster einen Skill erstellen, den du mit Computernutzung, Browseraktionen, verbundenen Plug-ins oder einer Kombination daraus wiederverwenden kannst.

## Bevor du beginnst

Wähle einen Ablauf, den du bereits sicher ausführen kannst. „Aufzeichnen und Wiedergeben“ funktioniert am besten, wenn die Schritte gleich bleiben und die Erfolgskriterien klar sind.

## Aufzeichnung starten

1. Wähle in der ChatGPT-Desktop-App ChatGPT aus und aktiviere Work über den Umschalter, oder wähle Codex aus. Öffne anschließend **Plug-ins**.
2. Öffne das Menü **+** .
3. Wähle **Skill aufzeichnen** aus.
4. Prüfe den vorgeschlagenen Prompt, ergänze hilfreichen Kontext und sende ihn ab.
5. Wenn der Chat eine Berechtigung zum Aufzeichnen deiner Aktionen anfordert, genehmige die Anfrage, sobald du bereit bist, den Ablauf vorzuführen.
6. Führe den Ablauf auf deinem Mac aus.
7. Wenn du fertig bist, beende die Aufzeichnung über die Menüleiste oder das Overlay. Du kannst dem Chat auch mitteilen, dass du fertig bist.

Während der Aufzeichnung beobachtet ChatGPT oder Codex die Aktionen und Fensterinhalte, die zum Erlernen des Ablaufs erforderlich sind. Die Aufzeichnung läuft weiter, bis du sie beendest. Beschränke die Aufzeichnung auf die Aufgabe, die der Skill vermitteln soll.

Nachdem du die Aufzeichnung beendet hast, analysiert ChatGPT oder Codex den aufgezeichneten Ablauf und entwirft einen Skill. Der Skill erklärt, wann der Ablauf verwendet werden soll, welche Eingaben er benötigt, welche Schritte auszuführen sind und wie sich das Ergebnis überprüfen lässt. Du kannst auch um weitere Anpassungen bitten.

## Ablauf wiedergeben

Starte einen neuen Chat in ChatGPT oder Codex und bitte darum, den erstellten Skill zu verwenden. Gib die Werte an, die diesmal anders sind, etwa die hochzuladende Datei, das zu erstellende Issue oder den Datumsbereich für den Bericht.

Das Produkt verwendet den Skill als wiederverwendbaren Kontext für die Aufgabe. Anschließend kann es den Ablauf mit den Werkzeugen ausführen, die in der aktuellen Umgebung verfügbar sind, darunter Computernutzung, Browseraktionen und installierte Plug-ins.

## Tipps für bessere Aufzeichnungen

- Halte die Vorführung kurz, aber vollständig.
- Nenne vor Beginn der Aufzeichnung dein Ziel und alle konkreten Eingaben, die bei unterschiedlichen Einsätzen des Skills variieren können.
- Verwende realistische Eingaben, aber keine geheimen Informationen oder sensiblen Daten.
- Ergänze den Skill nach der Aufzeichnung um wichtige, nicht offensichtliche Präferenzen, etwa Namenskonventionen, Standardwerte für Felder oder Entscheidungspunkte.
- Beende die Aufzeichnung, sobald der Ablauf abgeschlossen ist, statt danach noch Aufräumarbeiten aufzuzeichnen, die nichts mit dem Ablauf zu tun haben.

## Wann du ein weiteres Plug-in erstellen solltest

Mit „Aufzeichnen und Wiedergeben“ kannst du aus einem vorgeführten Ablauf schnell einen Skill erstellen.
Wenn du ein eigenständiges, stabiles Paket im Team verteilen,
mehrere Skills bündeln, Konnektoren einbinden, MCP-Server hinzufügen oder
Installationsmetadaten verwalten möchtest, erstelle aus dem Ablauf ein eigenes Plug-in. Weitere Informationen findest du unter
[Plug-ins erstellen](https://developers.openai.com/plugins/build/plugins).

## Fehlerbehebung

### Ich sehe „Aufzeichnen und Wiedergeben“ nicht

Wenn deine Organisation Codex mit `requirements.toml` verwaltet, regelt die Vorgabe
`[features].computer_use` auch die Verfügbarkeit von „Aufzeichnen und Wiedergeben“. Mit der Einstellung
`computer_use = false` sind beide Funktionen nicht verfügbar.
