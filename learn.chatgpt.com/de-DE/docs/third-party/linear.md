<!-- source: https://learn.chatgpt.com/de-DE/docs/third-party/linear -->

Nutze Codex in Linear, um Arbeit direkt aus Issues zu delegieren. Weise Codex ein Issue zu oder erwähne `@Codex` in einem Kommentar. Codex erstellt daraufhin einen Cloud-Chat und informiert dich über Fortschritte und Ergebnisse.

Codex in Linear ist für kostenpflichtige Tarife verfügbar (siehe [Preise](/de-DE/codex/pricing)).

Wenn du einen Enterprise-Tarif nutzt, bitte die Administration deines ChatGPT-Workspace, Codex-Cloud-Chats in den [Workspace-Einstellungen](https://chatgpt.com/admin/settings) und **Codex for Linear** in den [Konnektor-Einstellungen](https://chatgpt.com/admin/ca) zu aktivieren.

## Linear-Integration einrichten

1. Richte [Codex-Cloud-Chats](/de-DE/codex/cloud) ein, indem du GitHub in [Codex](https://chatgpt.com/codex) verbindest und eine [Umgebung](/de-DE/codex/environments/cloud-environment) für das Repository erstellst, in dem Codex arbeiten soll.
2. Öffne die [Codex-Einstellungen](https://chatgpt.com/codex/settings/connectors) und installiere **Codex for Linear** für deinen Workspace.
3. Verknüpfe dein Linear-Konto, indem du `@Codex` in einem Kommentarthread zu einem Linear-Issue erwähnst.

## Arbeit an Codex delegieren

Du kannst Arbeit auf zwei Arten delegieren:

### Codex ein Issue zuweisen

Nach der Installation der Integration kannst du Codex genauso Issues zuweisen wie deinen Teammitgliedern. Codex beginnt mit der Arbeit und veröffentlicht Fortschrittsmeldungen im Issue.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

### `@Codex` in Kommentaren erwähnen

Du kannst `@Codex` auch in Kommentarthreads erwähnen, um Arbeit zu delegieren oder Fragen zu stellen. Sobald Codex geantwortet hat, kannst du denselben Chat durch eine Antwort im Thread fortsetzen.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

Sobald Codex mit der Bearbeitung eines Issues beginnt, [wählt es eine Umgebung und ein Repository aus](#how-codex-chooses-an-environment-and-repo).
Um ein bestimmtes Repository vorzugeben, nenne es in deinem Kommentar, zum Beispiel: `@Codex fix this in openai/codex`.

So verfolgst du den Fortschritt:

- Öffne im Issue **Aktivität** , um Fortschrittsmeldungen zu sehen.
- Öffne den Chat-Link, um den Fortschritt genauer zu verfolgen.

Sobald Codex fertig ist, veröffentlicht es eine Zusammenfassung und einen Link zum abgeschlossenen Chat, damit du einen Pull Request erstellen kannst.

### So wählt Codex eine Umgebung und ein Repository aus

- Linear schlägt anhand des Issue-Kontexts ein Repository vor. Codex wählt die Umgebung aus, die am besten zu diesem Vorschlag passt. Ist die Anfrage nicht eindeutig, verwendet Codex die zuletzt von dir genutzte Umgebung.
- Der Chat wird auf dem Standard-Branch des ersten Repositorys ausgeführt, das in der Repository-Zuordnung dieser Umgebung aufgeführt ist. Aktualisiere die Repository-Zuordnung in Codex, wenn du ein anderes Standard-Repository oder weitere Repositorys benötigst.
- Wenn keine geeignete Umgebung oder kein geeignetes Repository verfügbar ist, erklärt Codex in einer Antwort in Linear, wie du das Problem vor einem erneuten Versuch behebst.

## Issues automatisch Codex zuweisen

Mit Triage-Regeln kannst du Issues automatisch Codex zuweisen:

1. Öffne in Linear die **Einstellungen**.
2. Wähle unter **Deine Teams** dein Team aus.
3. Öffne in den Workflow-Einstellungen **Triage** und aktiviere die Funktion.
4. Erstelle unter **Triage-Regeln** eine Regel und wähle **Delegieren** \> **Codex** sowie gegebenenfalls weitere Eigenschaften aus.

Linear weist neue Issues, die in die Triage aufgenommen werden, automatisch Codex zu.
Wenn du Triage-Regeln verwendest, führt Codex Chats mit dem Konto der Person aus, die das Issue erstellt hat.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

## Datennutzung, Datenschutz und Sicherheit

Wenn du `@Codex` erwähnst oder Codex ein Issue zuweist, erhält Codex dessen Inhalt, um deine Anfrage zu verstehen und einen Chat zu erstellen.
Für die Datenverarbeitung gelten die [Datenschutzrichtlinie](https://openai.com/privacy), die [Nutzungsbedingungen](https://openai.com/terms/) und weitere geltende [Richtlinien](https://openai.com/policies) von OpenAI.
Weitere Informationen zur Sicherheit findest du in der [Dokumentation zur Sicherheit von Codex](/de-DE/codex/agent-approvals-security).

Codex verwendet große Sprachmodelle, die Fehler machen können. Überprüfe Antworten und Diffs daher immer.

## Tipps und Fehlerbehebung

- **Fehlende Verbindungen**: Wenn Codex deine Verbindung mit Linear nicht bestätigen kann, antwortet es im Issue mit einem Link, über den du dein Konto verbinden kannst.
- **Unerwartete Auswahl der Umgebung**: Nenne in deiner Antwort im Thread die gewünschte Umgebung (zum Beispiel `@Codex please run this in openai/codex`).
- **Falscher Codeabschnitt**: Ergänze im Issue weiteren Kontext oder gib in deinem Kommentar mit `@Codex` konkrete Anweisungen.
- **Weitere Hilfe**: Besuche das [OpenAI-Hilfecenter](https://help.openai.com/).

<a id="connect-linear-for-local-tasks-mcp"></a>

## Linear für die lokale Arbeit verbinden (MCP)

Wenn du die ChatGPT-Desktop-App, Codex CLI oder die IDE-Erweiterung verwendest und lokal auf Linear-Issues zugreifen möchtest, konfiguriere den MCP-Server (Model Context Protocol) von Linear.

Weitere Informationen findest du in der [Linear-MCP-Dokumentation](https://linear.app/integrations/codex-mcp).

Da die IDE-Erweiterung und die CLI dieselbe Konfiguration verwenden, sind die Schritte zum Einrichten des MCP-Servers in beiden Fällen identisch.

### CLI verwenden (empfohlen)

Wenn du die CLI installiert hast, führe Folgendes aus:

```bash
codex mcp add linear --url https://mcp.linear.app/mcp

Du wirst aufgefordert, dich mit deinem Linear-Konto anzumelden und es mit Codex zu verbinden.

### Manuell konfigurieren

1. Öffne `~/.codex/config.toml` in deinem Editor.
2. Füge Folgendes hinzu:

```toml
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"

3. Führe `codex mcp login linear` aus, um dich anzumelden.
