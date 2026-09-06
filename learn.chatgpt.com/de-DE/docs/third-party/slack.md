<!-- source: https://learn.chatgpt.com/de-DE/docs/third-party/slack -->

Nutze Codex in Slack, um Programmieraufgaben direkt in Kanälen und Threads anzustoßen. Erwähne `@Codex` zusammen mit einem Prompt. Codex erstellt daraufhin einen Cloud-Chat und antwortet mit den Ergebnissen.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>

<br />

## Slack-App einrichten

1. Richte [Cloud-Chats in Codex](/de-DE/codex/cloud) ein. Du brauchst einen Plus-, Pro-, Business-, Enterprise- oder Edu-Tarif (siehe [Preise für ChatGPT](https://chatgpt.com/pricing)), ein verknüpftes GitHub-Konto und mindestens eine [Umgebung](/de-DE/codex/environments/cloud-environment).
2. Öffne die [Codex-Einstellungen](https://chatgpt.com/codex/settings/connectors) und installiere die Slack-App für deinen Workspace. Je nach den Richtlinien deines Slack-Workspaces muss eine Person mit Adminrechten die Installation möglicherweise genehmigen.
3. Füge `@Codex` einem Kanal hinzu. Falls du die App noch nicht hinzugefügt hast, fordert Slack dich beim Erwähnen dazu auf.

<a id="start-a-task"></a>

## Chat starten

1. Erwähne in einem Kanal oder Thread `@Codex` und füge deinen Prompt hinzu. Codex kann auf frühere Nachrichten im Thread zurückgreifen. Daher musst du den Kontext oft nicht noch einmal angeben.
2. (Optional) Gib in deinem Prompt eine Umgebung oder ein Repository an, zum Beispiel: `@Codex fix the above in openai/codex`.
3. Warte, bis Codex reagiert (👀) und mit einem Link zum Chat antwortet. Nach Abschluss postet Codex das Ergebnis und je nach deinen Einstellungen auch eine Antwort im Thread.

### So wählt Codex eine Umgebung und ein Repository aus

- Codex prüft die Umgebungen, auf die du Zugriff hast, und wählt diejenige aus, die am besten zu deiner Anfrage passt. Ist deine Anfrage nicht eindeutig, verwendet Codex die zuletzt von dir genutzte Umgebung.
- Der Chat verwendet den Standard-Branch des ersten Repositorys, das in der Repository-Zuordnung dieser Umgebung aufgeführt ist. Wenn du ein anderes Repository als Standard oder weitere Repositorys brauchst, aktualisiere die Repository-Zuordnung in Codex.
- Wenn keine geeignete Umgebung oder kein geeignetes Repository verfügbar ist, antwortet Codex in Slack mit einer Anleitung, wie du das Problem vor einem erneuten Versuch behebst.

### Datenkontrollen für Unternehmen

Standardmäßig antwortet Codex im Thread. Diese Antwort kann Informationen aus der Umgebung enthalten, in der Codex die Aufgabe ausgeführt hat.
Um das zu verhindern, kann eine Person mit Adminrechten für das Unternehmen die Option **Zulassen, dass die Codex-Slack-App nach Abschluss einer Aufgabe Antworten postet** in den [ChatGPT-Workspace-Einstellungen](https://chatgpt.com/admin/settings) deaktivieren. Deaktiviert eine Person mit Adminrechten die Antworten, antwortet Codex nur noch mit einem Link zum Chat.

### Datennutzung, Datenschutz und Sicherheit

Wenn du `@Codex` erwähnst, erhält Codex deine Nachricht und den bisherigen Threadverlauf, um deine Anfrage zu verstehen und einen Chat zu erstellen.
Die Datenverarbeitung richtet sich nach der [Datenschutzrichtlinie](https://openai.com/privacy), den [Nutzungsbedingungen](https://openai.com/terms/) und anderen geltenden [Richtlinien](https://openai.com/policies) von OpenAI.
Weitere Informationen zur Sicherheit findest du in der [Sicherheitsdokumentation](/de-DE/codex/agent-approvals-security) von Codex.

Codex verwendet große Sprachmodelle, die Fehler machen können. Überprüfe Antworten und Diffs immer.

### Tipps und Fehlerbehebung

- **Fehlende Verbindungen**: Wenn Codex deine Slack- oder GitHub-Verbindung nicht bestätigen kann, antwortet Codex mit einem Link, über den du die Verbindung erneut herstellen kannst.
- **Unerwartet ausgewählte Umgebung**: Nenne in deiner Antwort im Thread die gewünschte Umgebung (zum Beispiel `Please run this in openai/openai (applied)`) und erwähne dann erneut `@Codex`.
- **Lange oder komplexe Threads**: Fasse die wichtigsten Details in deiner letzten Nachricht zusammen, damit Codex keinen Kontext aus früheren Nachrichten im Thread übersieht.
- **Posten im Workspace**: In einigen Unternehmens-Workspaces ist das Posten abschließender Antworten eingeschränkt. Öffne in diesen Fällen den Chat-Link, um Fortschritt und Ergebnisse anzuzeigen.
- **Weitere Hilfe**: Besuche das [OpenAI-Hilfecenter](https://help.openai.com/).
