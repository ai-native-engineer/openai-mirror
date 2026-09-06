<!-- source: https://learn.chatgpt.com/de-DE/docs/plugins -->

## Übersicht

Plug-ins bündeln Funktionen zu wiederverwendbaren Arbeitsabläufen in ChatGPT und Codex. Sie
können Skills, Konnektoren oder beides enthalten. Beide Produkte nutzen ein gemeinsames
Plug-in-Verzeichnis. So findest du auf den unterstützten Oberflächen beider Produkte
dieselben öffentlichen Plug-ins.

Plug-ins funktionieren in Chat und Work in ChatGPT im Web, auf dem Desktop und auf Mobilgeräten
sowie in Codex in der ChatGPT-Desktop-App. Codex CLI bietet außerdem einen Plug-in-Browser
für Codex-Umgebungen. Die IDE-Erweiterung unterstützt keine Plug-ins.

Auf Mobilgeräten kannst du in Chat oder Work die für dein Konto verfügbaren Plug-ins verwenden.

Öffne den Tab **Plug-ins** , um Plug-ins zu entdecken und zu installieren. Nach der Installation
kannst du sie in Chat oder Work in ChatGPT oder in Codex verwenden. Installierte Plug-ins können
neue Chats um Skills, Konnektoren und MCP-Tools erweitern.

Öffne den Tab **Plug-ins** , um Plug-ins zu entdecken und zu installieren. Nach der Installation
kannst du sie in Chat oder Work verwenden. Ein Plug-in kann dich auffordern,
eine Verbindung zu einem externen Dienst herzustellen, bevor seine Tools verfügbar werden.

Gib in Codex CLI `/plugins` ein, um den Plug-in-Browser zu öffnen. Installiere ein Plug-in aus
einem konfigurierten Marketplace und starte anschließend eine neue Sitzung, bevor du die enthaltenen
Skills oder Tools verwendest.

<a id="plugin-directory-in-the-ide-extension"></a>

### Plug-ins auf einer unterstützten Oberfläche verwenden

Plug-ins sind in der IDE-Erweiterung nicht verfügbar. Verwende die ChatGPT-Desktop-App
oder Codex CLI, um Plug-ins für Codex zu entdecken und zu installieren.

Erweitere die Funktionen von ChatGPT und Codex, zum Beispiel so:

- Installiere das Codex-Security-Plugin, um Code, den du prüfen darfst, zu scannen und
plausible Hinweise auf Schwachstellen zu bestätigen.
- Installiere das Plug-in für Gmail, um mit Gmail zu arbeiten.
- Installiere das Plug-in für Google Drive, um mit Drive, Docs, Sheets und
Slides zu arbeiten.
- Installiere das Plug-in für Slack, um Kanäle zusammenzufassen oder Antworten zu entwerfen.

Ein Plug-in kann einen oder mehrere dieser Bestandteile enthalten:

- **Skills:** wiederverwendbare Anweisungen für bestimmte Aufgabenarten. ChatGPT und
  Codex können sie bei Bedarf laden, um die richtigen Schritte auszuführen und die
  passenden Referenzen oder Hilfsskripte für eine Aufgabe zu verwenden.
- **Konnektoren:** Verbindungen zu Tools wie GitHub, Slack oder Google Drive, über die
  ChatGPT und Codex Informationen aus diesen Tools lesen und darin Aktionen ausführen
  können. Konnektoren stellen Tools bereit und können optional eine eigene Benutzeroberfläche enthalten.
- **MCP-Server:** Dienste, die ChatGPT und Codex Zugriff auf weitere Tools oder
  gemeinsam genutzte Informationen ermöglichen, oft aus Systemen außerhalb deines lokalen Projekts.
  Auch Konnektoren basieren auf diesen Diensten. Sie definieren Tools, erzwingen die Authentifizierung, geben
  strukturierte Daten zurück und führen Aktionen in externen Systemen aus.
- **Browsererweiterungen:** Browserfunktionen, die ein Plug-in für seinen
  Ablauf benötigt.
- **Hooks:** Befehle, die an konfigurierten Punkten im Lebenszyklus ausgeführt werden. Prüfe
  die Hooks eines Plug-ins und aktiviere sie nur, wenn du ihnen vertraust.
- **Vorlagen für geplante Aufgaben:** wiederverwendbare Ausgangspunkte für wiederkehrende Aufgaben,
  sofern geplante Aufgaben verfügbar sind.

Du kannst Plug-ins teilen, indem du sie über eine Marketplace-Quelle veröffentlichst, etwa über einen
Marketplace in einem Repository für ein Projekt oder Team. Unter [Plug-ins erstellen](https://developers.openai.com/plugins/build/plugins)
findest du Hinweise zum Marketplace-Setup sowie zur Paketierung und Verteilung.

Wenn du eine Integration entwickelst, beginne mit dem Leitfaden
[MCP-Server erstellen](https://developers.openai.com/plugins/build/mcp-server).
Wenn das Plug-in eine eigene Benutzeroberfläche benötigt, verwende den
[optionalen Leitfaden zur Benutzeroberfläche](https://developers.openai.com/plugins/build/chatgpt-ui).

## Plug-ins verwenden und installieren

<a id="plugin-directory-in-the-codex-app"></a>

### Gemeinsames Plug-in-Verzeichnis

ChatGPT und Codex verwenden denselben öffentlichen Plug-in-Katalog. Öffne im Web oder in der
ChatGPT-Desktop-App den Tab **Plug-ins** , um Plug-ins zu entdecken und zu installieren.

  
    
  

Im Plug-in-Verzeichnis sind die Plug-ins in Tabs gegliedert:

- **OpenAI:** von OpenAI entwickelte Plug-ins.
- **Name deines Workspaces:** von deinem Workspace bereitgestellte Plug-ins.
- **Persönlich:** persönliche Marketplace-Plug-ins, einschließlich der Bereiche **Von mir erstellt** und
**Mit mir geteilt** , sofern diese Plug-ins verfügbar sind.

In der separaten Zeile **Installiert** kannst du dir deine bereits installierten Plug-ins ansehen.

Mit Adminrechten im Workspace kannst du für dein Team einen GitHub-Marketplace importieren und synchronisieren. Unter
[Plug-in-Verwaltung](/de-DE/codex/enterprise/plugin-management) findest du Hinweise zum Setup und
zu den Zugriffsvoraussetzungen.

### Plug-in installieren und verwenden

Nachdem du das Plug-in-Verzeichnis geöffnet hast:

1. Suche nach einem Plug-in oder durchstöbere das Verzeichnis. Öffne anschließend die Details des Plug-ins.
2. Wähle die Schaltfläche mit dem Pluszeichen aus, um das Plug-in zu installieren.
3. Wenn das Plug-in einen Konnektor benötigt, stelle die Verbindung her, sobald du dazu aufgefordert wirst.
Einige Plug-ins fordern dich bereits während der Installation zur Authentifizierung auf.
Bei anderen geschieht das erst bei der ersten Verwendung.
4. Starte nach der Installation einen neuen Chat und bitte ChatGPT oder Codex, das
Plug-in zu verwenden.

### Unterstützte Partner über „Mit ChatGPT anmelden“ verbinden

**Mit ChatGPT anmelden** wird schrittweise als Betaversion für unterstützte Plug-ins und
Partner-Websites eingeführt, darunter Airtable, GitLab, HubSpot, Notion, Supabase und
Vercel. Wenn die Option verfügbar ist, wähle beim Verbinden des Plug-ins **Mit ChatGPT anmelden** aus,
um dein Konto bei diesem Dienst zu erstellen oder zu verknüpfen.

Bei der Anmeldung werden nur dein Name, deine E-Mail-Adresse und, falls vorhanden, dein Profilbild
an den Partner übermittelt. Das Plug-in erhält dadurch keinen Zugriff auf deine Daten.
Auch Aktionen werden nicht automatisch genehmigt. Prüfe die vom Plug-in angeforderten Berechtigungen
und genehmige sie in einem separaten Schritt, bevor du die Verbindung nutzt.

Nach der Installation kannst du ein Plug-in direkt im Prompt-Fenster verwenden:

  
    
  

<div class="not-prose mt-4 grid gap-4 md:grid-cols-2">
  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">Aufgabe direkt beschreiben</p>
    <p class="mt-2 text-sm text-secondary">
      Gib das gewünschte Ergebnis an, zum Beispiel: „Fasse die ungelesenen Gmail-Threads
von heute zusammen“ oder „Rufe die neuesten Notizen zum Launch aus Google Drive ab.“
    </p>
    <p class="mt-3 text-sm text-secondary">
      Nutze diese Möglichkeit, wenn ChatGPT die passenden installierten Tools für die
Aufgabe auswählen soll.
    </p>
  </div>

  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">Bestimmtes Plug-in auswählen</p>
    <p class="mt-2 text-sm text-secondary">
      Gib <code>@</code> ein, um das Plug-in oder einen der enthaltenen Skills
      gezielt aufzurufen.
    </p>
    <p class="mt-3 text-sm text-secondary">
      Nutze diese Möglichkeit, wenn du genau festlegen möchtest, welches Plug-in oder welchen Skill ChatGPT
      verwenden soll. Weitere Informationen findest du unter <a href="/codex/skills-and-plugins">Skills und Plug-ins</a>.
    </p>
  </div>
</div>

### Apple Messages aus Codex heraus verwenden

Das Plug-in für Apple Messages ist in der ChatGPT-Desktop-App für macOS in allen Tarifen
verfügbar. In Codex und ChatGPT Work kann es iMessage-, SMS- und RCS-Chats auf deinem Mac
lesen und durchsuchen sowie in deinem Namen Nachrichten über die Messages-App senden.
Du kannst damit nicht über Messages aus der Ferne mit ChatGPT interagieren.
In regulären ChatGPT-Chats funktioniert es ebenfalls nicht.

In dieser Version ist das Messages-Plug-in nur im Build der ChatGPT-Desktop-App
für Apple Silicon (arm64) enthalten.

1. Öffne **Plug-ins**, suche nach dem Plug-in für Apple Messages und installiere es.
2. Starte einen neuen Chat in Codex oder ChatGPT Work und bitte darum, eine Nachricht zu finden,
zusammenzufassen, zu entwerfen oder zu senden.
3. Erteile die angeforderten macOS-Berechtigungen, bevor ChatGPT Nachrichten aus Messages liest.
4. Prüfe die Nachricht und die Empfängerliste, bevor du den Versand erlaubst.

ChatGPT sendet Nachrichten standardmäßig erst, nachdem du die Nachricht und ihre
Empfängerliste genehmigt hast. Wähle **Einmal erlauben** , um nur diesen Versand zu genehmigen. Wenn du
**Senden an diesen Chat immer erlauben** auswählst, kann ChatGPT künftig Nachrichten an diesen
Messages-Chat senden, ohne erneut eine Genehmigung für den Versand anzufordern.

Behalte für Chats, die nicht vertrauenswürdige oder irreführende Anweisungen enthalten können,
die Genehmigung für jeden einzelnen Versand bei. Bei einer dauerhaften Genehmigung entfällt deine letzte Möglichkeit,
eine Nachricht zu prüfen, bevor ChatGPT sie in deinem Namen sendet. Erteile eine dauerhafte Genehmigung nur, wenn du dieses Risiko akzeptierst.

Um die Genehmigung für jeden Versand wieder zu aktivieren, öffne **Einstellungen** \> **Computernutzung** und wähle
**Verwalten** neben **Messages** aus. Wähle unter **Senden immer erlaubt** das
Papierkorbsymbol neben dem Chat aus und bestätige mit **Entfernen**. ChatGPT fragt künftig wieder nach,
bevor es eine Nachricht an diesen Chat sendet.

**Bekanntes Problem:** Wenn deine Aufgabe auf **Vollzugriff** eingestellt ist oder Genehmigungsabfragen
anderweitig deaktiviert sind, kann Apple Messages möglicherweise die zum Senden erforderliche Bestätigung
nicht anzeigen. Wechsle zu **Genehmigung anfordern** oder **Für mich genehmigen** und versuche es erneut.

Apple Messages läuft auf deinem Mac. Es ist nicht direkt in ChatGPT im Web oder auf
Mobilgeräten, in Codex CLI oder in der IDE-Erweiterung verfügbar.

In verwalteten Workspaces können Administrierende Apple Messages über die bestehende
Einstellung für die Computernutzung deaktivieren.

<a id="plugin-directory-in-codex-cli"></a>

### Plug-in-Browser in Codex CLI

Führe in Codex CLI den folgenden Befehl aus, um den Plug-in-Browser zu öffnen:

```text
codex
/plugins

  
    
  

Der Plug-in-Browser der CLI gruppiert Plug-ins nach Marketplace. Über die Marketplace-Tabs
wechselst du zwischen Quellen. Öffne ein Plug-in, um Details anzusehen, installiere oder deinstalliere
Marketplace-Einträge und drücke bei einem installierten Plug-in die <kbd>Leertaste</kbd>, um es
zu aktivieren oder zu deaktivieren.

<a id="api-key-availability"></a>

### Verfügbarkeit mit API-Schlüssel

Wenn du [dich mit einem OpenAI-API-Schlüssel
bei Codex anmeldest](/de-DE/codex/auth#sign-in-with-an-api-key), kannst du unterstützte, von OpenAI kuratierte Plug-ins
in Codex CLI und in Codex in der ChatGPT-Desktop-App durchsuchen, installieren und
verwalten. Einige Plug-ins sind bei der Authentifizierung mit einem API-Schlüssel nicht verfügbar,
weil für ihren Verbindungsaufbau nicht unterstützte OAuth-Funktionen erforderlich sind. Überprüfe die Plug-in-Nutzung
auf der [Seite zur Plattformnutzung](https://platform.openai.com/usage).

### So funktionieren Berechtigungen und Datenweitergabe

In ChatGPT im Web nutzen Chat und Work die Workspace-Berechtigungen und Tools,
die für den jeweiligen Chat verfügbar sind. Konnektoren erfordern weiterhin eine separate Anmeldung und eigene Zugriffsberechtigungen.

Wenn eine Plug-in-Funktion über einen Codex-Host ausgeführt wird, gelten dessen [Sandbox und
Genehmigungsrichtlinie](/de-DE/codex/agent-approvals-security).
Verbindungen zu externen Diensten nutzen deren eigene Authentifizierungsverfahren und
Zugriffskontrollen.

- Die enthaltenen Skills stehen dir zur Verfügung, sobald du nach der Installation einen neuen Chat oder
eine neue CLI-Sitzung startest.
- Wenn ein Plug-in Konnektoren enthält, kann dich das verwendete Produkt beim Setup oder bei der ersten
Nutzung dazu auffordern, diese Konnektoren zu installieren oder dich bei ihnen anzumelden.
- Wenn ein Plug-in MCP-Server enthält, musst du diese möglicherweise zusätzlich einrichten oder dich
authentifizieren, bevor du sie verwenden kannst.
- Wenn ChatGPT Daten über einen enthaltenen Konnektor sendet, gelten die Nutzungsbedingungen und die
Datenschutzrichtlinie des jeweiligen Dienstes.

### Plug-in entfernen

Um ein Plug-in zu entfernen, öffne es in einem unterstützten Plug-in-Browser und wähle
**Plug-in deinstallieren** aus, sofern diese Option verfügbar ist. Bei über den Workspace installierten oder
standardmäßig bereitgestellten Plug-ins ist diese Option möglicherweise nicht verfügbar. Stattdessen
verwaltet deine Workspace-Administration diese Plug-ins.

Wenn du ein Plug-in deinstallierst, wird das Plug-in-Paket aus der jeweiligen ChatGPT- oder Codex-Umgebung
entfernt. Die enthaltenen Konnektoren bleiben jedoch verbunden, bis du ihre Verbindungen in
ChatGPT verwaltest.

## Eigenes Plug-in erstellen

Wenn du dein eigenes Plug-in erstellen, testen oder verteilen möchtest, findest du weitere Informationen unter
[Plug-ins erstellen](https://developers.openai.com/plugins/build/plugins). Dort erfährst du, wie du lokal ein Grundgerüst erstellst,
einen Marketplace manuell einrichtest und Plug-ins im Workspace teilst. Außerdem findest du Hinweise zu Plug-in-Manifesten
und zur Paketierung.

Wenn dein Plug-in servergestützte Funktionen enthält, findest du weitere Informationen unter
[MCP-Server erstellen](https://developers.openai.com/plugins/build/mcp-server).
MCP-Tools können ohne eigene Benutzeroberfläche arbeiten oder eine Benutzeroberfläche zurückgeben,
wenn diese den Ablauf erleichtert.

Wenn dein Plug-in zur Überprüfung bereit ist, findest du unter
[Plug-ins einreichen](https://developers.openai.com/plugins/deploy/submission) Informationen zum Einreichungsprozess auf der OpenAI Platform,
zu den erforderlichen Berechtigungen, den Unterlagen für die Überprüfung, MCP-Prüfungen und den Anforderungen an
Testfälle.

## Leitfäden für Plug-ins

- [Aufzeichnen und Wiedergeben](/de-DE/codex/extend/record-and-replay): Zeige ChatGPT einmal einen Ablauf
  und verwandle ihn in einen wiederverwendbaren Skill.
- [Codex-Security-Plugin](/de-DE/codex/security/plugin): Scanne Code, zu dessen Analyse du berechtigt bist,
  bestätige Befunde und bereite geprüfte Korrekturen vor.
