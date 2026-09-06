<!-- source: https://learn.chatgpt.com/de-DE/use-cases/browser-games -->

## Einführung

Die Spieleentwicklung zeigt besonders deutlich, dass Codex nicht nur bei der Codegenerierung hilft. Ein echtes Spiel erfordert meist ein schriftliches Konzept, eine Rendering-Schicht, ein Frontend-Grundgerüst, Zustandsverwaltung im Backend, die Erstellung von Assets und kontinuierliche visuelle Feinabstimmung

Dieser Anwendungsfall funktioniert am besten, wenn Codex zuerst genau festhält, was das Spiel leisten soll, und es danach mithilfe von Playwright interactive in einem Live-Browser testet und iterativ verbessert.

## Mit dem Spielplan beginnen

Bevor Codex überhaupt ein Grundgerüst erstellt, bitte Codex, eine Datei `PLAN.md` anzulegen, die das Spiel konkret definiert:

- das Spielziel
- die zentrale Spielschleife
- Eingaben und Steuerung
- Zustände für Sieg und Niederlage
- Fortschritt oder Schwierigkeitsgrad
- die visuelle Ausrichtung
- Annahmen zu Stack und Hosting
- die Reihenfolge der Meilensteine

Dieser Plan ist wichtig, weil „ein Spiel entwickeln“ für sich genommen zu vage ist. Codex muss wissen, wie die einzelnen Teile des Spiels umgesetzt werden sollen, und greift während der Entwicklung häufig auf die Implementierungsdetails zurück.

Du kannst den Planmodus mit dem Slash-Befehl `/plan` aktivieren.
Speichere die Ausgabe anschließend in der Datei `PLAN.md`.

## Das Verhalten von Codex mit AGENTS.md steuern

Damit Codex den Plan befolgt, seine Arbeit überprüft und die richtigen Tools verwendet, lege eine Datei `AGENTS.md` mit folgendem Inhalt an:

```text
# Game name

Tech Stack:

- NextJS for frontend (hosted on Vercel)
- <insert technology> for rendering
- Fastify for backend, websockets (hosted on <hosting platform>)
- Postgres for database (hosted on <hosting platform>)
- Redis for caching and pub/sub (hosted on <hosting platform>)
- OpenAI for generative AI features

Tips:

- Use build and test commands to verify your work as soon as you complete a feature or task
- Use the PLAN.md file to guide your work when building new features
- Log your work under .logs (create new log files as you see fit) to record your thought process and decisions, and reference them when iterating on features
- Use playwright to test the visual output of your work, and iterate if it doesn't look right or fit the vibe
- Use imagegen to generate visual assets for your work, and every time you generate a collection of assets, save the prompts you used to be able to continue generating more of the same assets later (create files in .prompts)
- Use Context7 MCP to fetch <rendering framework> docs

So kann Codex über längere Zeit selbstständig arbeiten und bei Bedarf die relevanten Skills verwenden.

## Skills nutzen

Füge die in der Datei AGENTS.md genannten Skills hinzu:

- Imagegen, damit Codex bei Bedarf visuelle Assets für das Spiel erstellen kann
- Playwright interactive, damit Codex das Spiel in einem Live-Browser testen kann
- OpenAI-Dokumentation, damit Codex die neueste OpenAI-API-Dokumentation abrufen kann
- Optional kannst du den MCP-Server von Context7 hinzufügen, um die neueste Dokumentation für das Rendering-Framework abzurufen

Weitere Informationen zum Hinzufügen von Skills findest du in der [Skills-Dokumentation](/de-DE/codex/build-skills).

  **Tipp**: Bitte Codex, Prompts für die Bildgenerierung in einer Datei zu speichern, damit
  alle visuellen Assets konsistent sind. Beschreibe den gewünschten Stil der Assets, die du
  erstellen möchtest, und lass Codex detaillierte, wiederverwendbare Prompts ausarbeiten.

## Codex arbeiten und das Spiel iterativ verbessern lassen

Codex erstellt auf Grundlage des ursprünglichen Plans eine erste Version des Spiels.

Wenn viele Bild-Assets generiert werden müssen, kann die Erstellung der ersten Version einige Zeit dauern, manchmal mehrere Stunden. Codex kann seine Arbeit testen und das Spiel in einem Live-Browser ausprobieren und deshalb lange ohne weitere Eingaben weiterarbeiten.

Je genauer der Plan ausgearbeitet ist, desto besser fällt das Endergebnis nach der ersten Iteration aus.

Beim Testen kannst du das Spiel nach Bedarf schrittweise verbessern: Stelle Screenshots bereit und bitte um Änderungen am Gameplay oder Aktualisierungen der visuellen Assets, bis du mit dem Ergebnis zufrieden bist.
