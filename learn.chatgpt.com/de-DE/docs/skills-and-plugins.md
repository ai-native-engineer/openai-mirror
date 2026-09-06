<!-- source: https://learn.chatgpt.com/de-DE/docs/skills-and-plugins -->

Skills und Plug-ins helfen ChatGPT und Codex, wiederkehrende Aufgaben mit den
passenden Anweisungen, Ressourcen und Tools zu erledigen. Dadurch entfällt häufig die Notwendigkeit,
denselben Prompt, dieselbe Vorlage, dieselben Anforderungen oder denselben Prozess in jeden Chat einzufügen.

- Ein **Skill** bündelt Anweisungen und ergänzende Ressourcen für eine bestimmte
  Aufgabe oder einen bestimmten Arbeitsablauf.
- Ein **Plug-in** ist ein installierbares Paket, das Skills, Konnektoren oder
  beides enthalten kann. Konnektoren basieren auf Servern für das Model Context Protocol (MCP) und können
  optional eine angepasste ChatGPT-Benutzeroberfläche enthalten.

## Skills für wiederkehrende Aufgaben nutzen

Ein Skill ist ein wiederverwendbarer Arbeitsablauf mit aufgabenspezifischen
Anweisungen für ChatGPT oder Codex. Darin kannst du festhalten, wie du wiederkehrende Aufgaben bislang erledigst, damit das jeweilige
Produkt bei jeder solchen Aufgabe demselben Prozess folgt.

Ein Skill kann Folgendes kombinieren:

- Einen Namen und eine Beschreibung, anhand derer ChatGPT und Codex erkennen, wann der Skill
eingesetzt werden soll.
- Anweisungen für den Arbeitsablauf, die den Prozess und das erwartete Ergebnis festlegen.
- Ergänzende Ressourcen wie Vorlagen, Beispiele, Markenrichtlinien, Schemas
oder angebundene Tools.

Skills sind besonders nützlich, wenn gute Ergebnisse einen wiederholbaren Ansatz erfordern. Ein
Skill kann zum Beispiel ein tägliches Briefing vorbereiten, Dokumentation überprüfen, eine
Präsentation erstellen, den Schreibstandard eines Teams anwenden oder jede Woche Informationen aus denselben
angebundenen Tools zusammentragen.

Nutze Skills, um konsistentere Ergebnisse zu erzielen, bewährte Methoden deines Teams im
Arbeitsablauf bereitzustellen und einen einheitlichen Prozess weiterzugeben, statt dich auf undokumentiertes
Wissen zu verlassen.

ChatGPT und Codex können einen Skill auswählen, wenn deine Anfrage zu seinem Einsatzzweck passt. Du
kannst ihn auch gezielt auswählen. In ChatGPT erwähnst du Skills mit `@`, in Codex
mit `$`.

## Skills erstellen

Du kannst zunächst eine Aufgabe, die du regelmäßig erledigst, in einen klar umrissenen Leitfaden für
ChatGPT und Codex umwandeln. Gute erste Skills sind etwa ein wöchentliches Update, ein Kampagnenbriefing,
die Nachbereitung eines Meetings oder eine andere Aufgabe, bei der Schritte und Format
konsistent bleiben sollen.

So erstellst du einen nützlichen Skill:

1. **Wähle eine klar umrissene Aufgabe aus.** Halte fest, womit du normalerweise beginnst, etwa
   mit Dateien, Links oder Notizen, und wie das fertige Ergebnis aussehen soll.
2. **Beschreibe den Arbeitsablauf.** Beginne in ChatGPT mit `@skill-creator`; in Codex
   verwendest du `$skill-creator`. Erläutere das Ziel, die einzelnen Schritte, das erwartete
   Format sowie alles, was der Skill immer enthalten oder vermeiden soll. Füge, falls vorhanden, eine Vorlage
   oder ein gutes Beispiel hinzu.
3. **Prüfe den Entwurf und probiere ihn aus.** Kontrolliere die Anweisungen und teste den Skill mit einer
   realistischen Anfrage. Überarbeite ihn, wenn im Ergebnis ein Schritt fehlt oder es vom gewünschten
   Format abweicht.
4. **Installiere den Skill und verwende ihn erneut.** Sobald der Skill aktiviert ist, kann ChatGPT oder Codex ihn
   für passende Anfragen verwenden, oder du kannst ihn gezielt auswählen. Du kannst ihn auch
   mit deinem Team teilen, sofern deine Workspace-Einstellungen dies zulassen.

Weitere Informationen zum Erstellen von Skills findest du im folgenden Leitfaden.

  
    <span slot="icon">
      
    </span>
    Erstelle, teste und teile wiederverwendbare Skills mit ChatGPT und Codex.
  

## Plug-ins für Tools und gemeinsame Arbeitsabläufe nutzen

Mit Plug-ins lassen sich wiederverwendbare Funktionen leichter installieren und weitergeben. Ein Plug-in kann
Skills mit Konnektoren für Dienste wie GitHub, Google Drive oder
Slack kombinieren und MCP-Server für zusätzliche Tools und weiteren Kontext enthalten.

ChatGPT und Codex greifen auf dasselbe universelle Plug-in-Verzeichnis zu. Durchsuche es, wenn du
einen vorhandenen Arbeitsablauf hinzufügen möchtest, statt selbst einen zu erstellen. Beschreibe nach der Installation
eines Plug-ins die Aufgabe direkt oder wähle mit der Aufrufsyntax der jeweiligen Oberfläche gezielt ein Plug-in oder einen enthaltenen
Skill aus.

[Hier erfährst du, wie du Plug-ins installierst und verwendest](/de-DE/codex/plugins).

## Zwischen Skill und Plug-in wählen

Nutze einen Skill, wenn du wiederverwendbare Anweisungen für eine klar umrissene Aufgabe benötigst. Nutze ein
Plug-in, wenn du ein installierbares Paket benötigst, das Anweisungen mit
angebundenen Diensten oder anderen Tools kombinieren kann.

Mit
[„Aufzeichnen und Wiedergeben“](/de-DE/codex/extend/record-and-replay) kannst du auch einen Arbeitsablauf demonstrieren. Die Aufzeichnung wird dabei in einen
wiederverwendbaren Skill umgewandelt. Wie du dein eigenes Paket zusammenstellst und verteilst, erfährst du unter
[Plug-ins erstellen](https://developers.openai.com/plugins/build/plugins).

Wenn dein Plug-in eine Verbindung zu einem Dienst herstellen oder MCP-Tools bereitstellen muss, findest du weitere Informationen unter
[MCP-Server erstellen](https://developers.openai.com/plugins/build/mcp-server). Sobald dein Plug-in für den öffentlichen Review bereit ist,
findest du unter [Plug-ins einreichen](https://developers.openai.com/plugins/deploy/submission) weitere Informationen.

Weitere Beispiele für wiederverwendbare Arbeitsabläufe findest du unter [Skills in der OpenAI
Academy verwenden](https://openai.com/academy/skills/).
