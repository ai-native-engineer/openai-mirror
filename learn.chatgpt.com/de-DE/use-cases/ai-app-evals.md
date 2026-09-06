<!-- source: https://learn.chatgpt.com/de-DE/use-cases/ai-app-evals -->

## Einführung

Wenn du eine KI-Anwendung entwickelst oder eine bestehende änderst, möchtest du sicherstellen, dass sie sich wie erwartet verhält. Mit Evals kannst du eine Reihe von Szenarien systematisch testen und Regressionen vor der Auslieferung erkennen.

Mit Promptfoo kannst du Evals für deine KI-Anwendung ausführen. Codex hilft dir dabei, diese Evals zu erstellen und zu pflegen.

## So gehst du vor

Verwende Codex zusammen mit dem Skill `$promptfoo-evals` aus dem Promptfoo-Plug-in, um aus einem bestimmten Verhalten einer KI-App eine wiederholt ausführbare Eval-Suite zu erstellen. Falls die App noch kein funktionierendes Promptfoo-Ziel hat, hilft `$promptfoo-provider-setup` dabei, die Suite mit dem App-Pfad zu verbinden, den du testen möchtest.

Codex kann die App untersuchen, aussagekräftige Fälle vorschlagen, die Promptfoo-Konfiguration und Testdaten hinzufügen, die Suite lokal ausführen und dir einen Befehl nennen, den du weiterverwenden kannst.

Dieser Anwendungsfall eignet sich am besten, wenn das Verhalten klar umrissen ist: Qualität von Supportantworten, Retrieval-Verankerung, Klassifizierungslabels, Tool-Aufrufe, JSON-Struktur, Geschäftsregeln oder die Absicherung von Prompt- und Modellmigrationen.

Ein guter erster Durchgang sollte Code und Testdaten liefern, die sich gut überprüfen lassen: eine Datei `promptfooconfig.yaml` oder eine gleichwertige Konfiguration, ein kleines Verzeichnis `evals/`, Testfälle, gegebenenfalls einen Zieladapter zum Aufrufen der App und einen lokalen Befehl wie `npm run evals`.

## Lege fest, was du evaluieren möchtest

Beginne mit einem einzigen Versprechen an die Nutzenden. Bitte Codex nicht, das gesamte KI-System in einem Durchgang zu evaluieren. Eine kleinere Suite lässt sich leichter überprüfen und dauerhaft ausführen, und du kannst ihren Ergebnissen eher vertrauen.

Gute erste Ziele sind:

- **Korrektheit:** Klassifizierung, Extraktion, Zusammenfassung, Routing oder Transformation.
- **Verankerung:** Antworten, die an abgerufene Dokumente oder zitierte Quellen gebunden bleiben sollen.
- **Tool-Einsatz:** das richtige Tool auswählen, gültige Argumente übergeben und Tool-Fehler behandeln.
- **Format oder Geschäftsregeln:** JSON-Schemata, Feldnamen, durch Geschäftsregeln vorgegebene Grenzwerte oder Vorgaben für UI-Texte.
- **Prompt- oder Modellmigration:** sicherstellen, dass ein neuer Prompt, ein neues Modell, eine neue Systemnachricht oder eine neue Retrieval-Einstellung keine wichtigen Fälle beeinträchtigt.

Nutze Produktanforderungen, Fehlerberichte, eskalierte Supportfälle oder bereinigte Beispiele als Ausgangspunkt, die dein Team bedenkenlos in das Repository einchecken kann.

## Eval-Plan anfordern

Codex sollte die App prüfen, bevor Codex Änderungen vornimmt. Bitte um einen Plan, der Zielpfad, Fixtures, Assertions, Adapter und Befehle nennt. So kannst du einen falschen Zielpfad oder schwache Testfälle erkennen, bevor Dateien hinzugefügt werden.

Prüfe den Plan vor der Implementierung. Er sollte den App-Pfad oder Endpunkt nennen, den Promptfoo aufruft, außerdem die ersten Testfälle, die Assertions, die von Codex zu erstellenden Dateien, den lokalen Befehl und alle erforderlichen Secrets oder Dienste. Wenn der Plan das Modell direkt statt über den von Nutzenden aufgerufenen App-Pfad testet, frage Codex, ob das beabsichtigt ist.

## Implementieren, ausführen und weiterentwickeln

Sobald der Plan stimmt, bitte Codex, ihn umzusetzen. Die erste Implementierung sollte bewusst schlicht bleiben: Konfiguration, Fälle, Fixtures, bei Bedarf ein Zieladapter, ein Befehl und ein Nachweis, dass der Befehl ausgeführt wurde.

Eine kleine Suite, die die App aufruft, könnte so aussehen:

```text
evals/
  promptfooconfig.yaml
  tests/
    cases.yaml
  providers/
    provider.js  # only if the built-in provider cannot call the app directly

Führe die Suite aus, bevor du das Verhalten änderst. Der Baseline-Lauf zeigt dir, ob die App bei diesen Fällen bereits fehlschlägt, die Assertions angepasst werden müssen oder der Zieladapter nicht korrekt ist. Passe Assertions an, wenn sie zu empfindlich oder zu vage sind, aber lass tatsächliche Produktfehler sichtbar.

Nutze die Suite nach dem ersten Lauf, um App-Änderungen vor ihrer Auslieferung zu vergleichen. Füge neue Fälle hinzu, sobald ein Fehler, eine Release-Anforderung oder eine Produktprüfung ein Verhalten erkennen lässt, das stabil bleiben soll. Sobald der lokale Befehl stabil ist, bitte Codex, ihn in CI oder deine Release-Checkliste aufzunehmen.
