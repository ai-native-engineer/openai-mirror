<!-- source: https://learn.chatgpt.com/de-DE/use-cases/idea-to-proof-of-concept -->

## Mit einer visuellen Richtung beginnen

GPT Image 2 eignet sich sehr gut, um hochwertige UI-Mockups zu erstellen. Du musst beim Ausloten neuer Ideen nicht bei null anfangen: Mit der Bildgenerierung kannst du eine visuelle Richtung entwickeln.

Dafür gibt es zwei Möglichkeiten:

- Entwickle die visuelle Richtung mithilfe des ImageGen-Skills weiter. Sobald du mit dem vorgeschlagenen UI zufrieden bist, kannst du Codex bitten, einen Prototyp nach der visuellen Vorlage zu entwickeln. Wähle dazu Codex aus, starte einen neuen Chat und hänge das endgültige Bild an, das du umsetzen möchtest, anstatt direkt im ChatGPT-Chat fortzufahren. Codex erzielt bessere Ergebnisse, wenn es auf eine von dir angehängte Datei zurückgreifen kann.
- Nutze ein Plug-in und beschreibe einfach deine Idee. Das Plug-in entwickelt für dich eine visuelle Richtung und übernimmt die nächsten Schritte.

## Ein Plug-in nutzen

Wenn du die visuelle Richtung nicht weiter ausarbeiten musst, bevor du mit der Implementierung beginnst, kannst du ein Plug-in verwenden und deine Idee beschreiben.

Nutze das [Build Web Apps-Plug-in](https://github.com/openai/plugins/tree/main/plugins/build-web-apps)
für Web-Apps, Dashboards, kreative Websites und Tools mit umfangreichem Frontend. Der
Workflow sorgt dafür, dass Codex zuerst ein Design erstellt, es im Code nachbildet und den
Browser nutzt, um das Ergebnis mit dem Konzept zu vergleichen.

Nutze das [Game Studio-Plug-in](https://github.com/openai/plugins/tree/main/plugins/game-studio),
wenn der Proof of Concept ein Browsergame ist. Dieser Ansatz sollte die
möglichen Spielaktionen, die erste spielbare Kernschleife, die Engine, den Asset-Workflow, das HUD, die Steuerung und den
Browsertest festlegen, bevor du das Spiel erweiterst.

## Iterativer Workflow

Ein guter Proof of Concept konzentriert sich auf ein MVP, das sich schnell implementieren und gemeinsam mit dem Team validieren lässt.
Wenn du sicherstellen möchtest, dass das MVP wie erwartet funktioniert, kannst du Playwright interactive verwenden, damit Codex seine Arbeit überprüft.

Sobald deine erste Version funktioniert, kannst du sie weiterentwickeln, indem du im selben Chat klar umrissene Änderungen anforderst:
