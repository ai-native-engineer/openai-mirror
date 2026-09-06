<!-- source: https://learn.chatgpt.com/de-DE/use-cases/qa-your-app-with-computer-use -->

## Einführung

Die Computernutzung eignet sich besonders gut für QA-Durchläufe, da sie die Benutzeroberfläche erfassen, Abläufe durchklicken, Text in Felder eingeben und protokollieren kann, was fehlschlägt. So lassen sich sowohl Funktionsfehler als auch UI-Probleme in realistischen Nutzerabläufen erkennen.

Entscheidend ist, dass du Codex mitteilst, welche Umgebung getestet werden soll, welche Abläufe am wichtigsten sind und welche Art von Bericht du erhalten möchtest.

## So gehst du vor

1. Installiere das [Plug-in für die Computernutzung](/de-DE/codex/computer-use).
2. Gib an, welche App, welchen Build oder welche Umgebung Codex testen soll.
3. Nenne die Abläufe oder zentralen Anwendungsfälle, die dir besonders wichtig sind.
4. Fordere einen strukturierten Bericht an, damit du die Ergebnisse leicht einordnen oder weitergeben kannst.

Du kannst die Anweisung allgemein halten:

- `@Computer Test my app. Find any major issues and give me a report.`

Oder du formulierst sie konkreter:

- `@Computer Test my app in staging. Cover signup, invite a teammate, and upgrade billing. Log every bug with repro steps, expected result, actual result, and severity.`

Wenn du bereits eine Testplandatei im Repository pflegst, hänge sie an den Chat an oder verweise Codex darauf, damit der QA-Durchlauf deinen bestehenden Abläufen folgt.

## Praxistipps

### Beschreibe das Setup genau

Wenn der Status des Kontos, Testdaten, Feature-Flags oder die gewählte Umgebung den Ablauf beeinflussen, gib diese Informationen gleich zu Beginn an. Codex liefert deutlich bessere Ergebnisse, wenn klar ist, ob der Test lokal, in einer Staging-Umgebung oder unter produktionsnahen Bedingungen stattfindet.

### Nenne die relevanten Problemarten

Gib an, ob Codex sich auf Funktionsfehler, Layoutprobleme, missverständliche Texte, visuelle Regressionen oder all diese Punkte konzentrieren soll.

### Lege fest, ob der Durchlauf beendet oder fortgesetzt werden soll

Wenn ein blockierendes Problem den Durchlauf beenden soll, gib das an. Andernfalls weise Codex an, den übrigen Ablauf weiter zu testen und vor der abschließenden Zusammenfassung alle nicht blockierenden Probleme zu erfassen.

## Sinnvolle nächste Schritte

Lass nach dem QA-Durchlauf denselben Chat offen und bitte Codex, einen der gefundenen Fehler zu beheben, aus den Ergebnissen Entwürfe für Linear oder GitHub zu erstellen oder beim nächsten Durchlauf nur einen bestimmten Ablauf zu testen, der fehlschlägt.

## Prompt-Vorschlag

**Strukturierten QA-Durchlauf durchführen**
