<!-- source: https://learn.chatgpt.com/de-DE/docs/webmcp -->

Website-Tools sind ChatGPTs Umsetzung des vorgeschlagenen
[WebMCP-Standards](https://webmachinelearning.github.io/webmcp/). Mit WebMCP kann eine Website
einem KI-Agenten nützliche Aktionen direkt anbieten, zusätzlich zu der
Oberfläche, die Menschen bereits nutzen. Du und der Agent können auf derselben aktuell geöffneten
Seite und in derselben angemeldeten Sitzung arbeiten.

Im [integrierten Browser](/de-DE/codex/browser) der ChatGPT-Desktop-App können ChatGPT Work und Codex
diese Tools erkennen und nutzen, sofern sie verfügbar sind.

  Verwende GPT-5.6 Sol oder GPT-5.6 Terra für Website-Tools. Bei GPT-5.6 Luna ist
WebMCP derzeit deaktiviert. Aktualisiere die ChatGPT-Desktop-App auf die neueste Version.
Website-Tools sind in Enterprise- oder Edu-Workspaces nicht verfügbar. Die Verfügbarkeit hängt außerdem
vom Rollout und den Tools ab, die die aktuelle Seite bereitstellt.

## WebMCP und MCP im Vergleich

Das [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/learn/architecture)
verbindet eine KI-Anwendung mit einem lokalen oder entfernten Server. Die zugehörigen Tools können
unabhängig von einer geöffneten Webseite arbeiten, etwa um einen Dienst zu durchsuchen oder
Datensätze über eine API zu verwalten.

Mit [WebMCP](https://github.com/webmachinelearning/webmcp) kann eine Website ihre Funktionen
einem Agenten als vordefinierte Tools zur Verfügung stellen. Der Agent kann sie
beim Besuch der Website erkennen. Du musst also keinen separaten MCP-Server
installieren und keine weitere Verbindung einrichten, um diese Funktionen zu nutzen.

Dieser Ansatz ist nützlich, wenn du und der Agent dasselbe sehen müssen, zum Beispiel
beim Bearbeiten eines Canvas oder beim Erkunden eines Dashboards. Ein
[Plug-in mit einem MCP-Server](/de-DE/codex/build-plugins) kann eine Integration bereitstellen,
die unabhängig von einer geöffneten Seite funktioniert. Eine Website kann beides unterstützen.

## So funktioniert es im Browser

Öffne eine Website im integrierten Browser und bitte ChatGPT Work oder Codex um Hilfe
bei einer Aufgabe. Wenn die Seite Website-Tools anbietet, kann der Agent die passenden Aktionen
auf der angezeigten Website erkennen und nutzen. Beispielsweise könnte ein Dokumenteditor
dem Agenten ermöglichen, einen Abschnitt zu finden oder einen Kommentar zu hinterlassen, den du überprüfen kannst.

Wähle in der Adressleiste des Browsers **Website-Tools** aus, um zu sehen, was die Website
bereitstellt. Wähle **Verfügbare Website-Tools** aus, um dir die einzelnen Tools anzusehen.
Der Browser prüft jede Anfrage, bevor die Website sie ausführt. Der Agent
kann die Seite prüfen, um festzustellen, was sich geändert hat. Sind aktuelle Aktivitäten verfügbar,
wähle **Zuletzt verwendet** aus, um **Quellen** zu öffnen und diese Aufrufe zu überprüfen.

Klappe in diesem Beispiel **Verfügbare Website-Tools** auf, um dir die Tools
von [Margin](https://margin-local-docs.openai.chatgpt.site) anzusehen.

  

Tools gehören zu der Seite, die sie bereitstellt. Wenn du eine Seite schließt oder verlässt,
sind ihre Tools möglicherweise nicht mehr verfügbar. Wenn kein geeignetes Tool verfügbar ist,
kann der Agent unter Umständen weiterhin seine regulären Browserfunktionen nutzen.

## Beispiel: Die OpenAI-Dokumentation erkunden

ChatGPT Learn und OpenAI Developers bieten Website-Tools zum Suchen und Lesen
von Dokumentation. Wähle im Editor **In ChatGPT öffnen** aus, um Learn im Browser der
Desktop-App zu öffnen. Daneben erscheint ein neuer Chat, in dem dieser Prompt zum Senden bereitsteht.

Mit diesen Tools kann der Agent die passende Seite suchen, lesen und öffnen:

| Tool                    | Funktion                                                             |
| ----------------------- | ------------------------------------------------------------------------ |
| `search_openai_docs`    | Durchsucht die OpenAI-Dokumentation.                                           |
| `lookup_page`           | Liest eine Dokumentationsseite anhand ihres Pfads oder ihrer URL.                               |
| `lookup_context`        | Liest die aktuelle Route der Dokumentation und den ausgewählten Text.                          |
| `navigate_to_page`      | Öffnet eine passende Seite auf der aktuellen Dokumentationswebsite.                 |
| `generate_custom_guide` | Startet die Erstellung einer individuellen Entwicklungs- oder Lernanleitung und gibt ihren Status und Link zurück. |

Der Docs-Agent erstellt asynchron eine individuelle Anleitung. Wenn du den Link erhältst, bedeutet das nicht, dass die Erstellung bereits abgeschlossen ist.

## Sicherheit und deine Kontrollmöglichkeiten

Tool-Definitionen und Ergebnisse, die eine Website bereitstellt, sind nicht vertrauenswürdige Inhalte. Der Name eines Tools oder die Behauptung, dass es nur Daten liest, belegt nicht, was es tatsächlich tut. Anweisungen einer Website erteilen dem Agenten keine Berechtigung, Informationen ohne Bezug zur Aufgabe weiterzugeben oder sensible Aktionen auszuführen.

Im integrierten Browser wird jeder Tool-Aufruf vor der Ausführung auf Sicherheit geprüft. Die üblichen Richtlinien für Website-Zugriffe und Bestätigungen gelten weiterhin, auch für folgenreiche Aktionen wie das Senden von Nachrichten, Käufe, das Löschen von Daten oder das Ändern von Berechtigungen. Der Browser bindet jeden Aufruf an seine Ursprungsseite und die zugehörige Tool-Registrierung. Diese Prüfungen verringern das Risiko, machen eine Website oder ihre Ausgaben aber nicht vertrauenswürdig.

Du kannst die Option **Website-Tools aktivieren** unter **Einstellungen \> Browser \> Berechtigungen** ausschalten.
Prüfe die Website, die angeforderte Aktion und das Ergebnis, bevor du sensible
Informationen weitergibst oder dich auf eine Änderung verlässt.

Melde Sicherheitslücken über das
[Security-Bug-Bounty-Programm](https://bugcrowd.com/engagements/openai) von OpenAI. Bei Risiken für die KI-Sicherheit
informiere dich über das
[Safety-Bug-Bounty-Programm](https://openai.com/index/safety-bug-bounty/). Beachte
den Geltungsbereich und die Vorgaben zur Einreichung des jeweiligen Programms.

## Einschränkungen

Der integrierte Browser von ChatGPT unterstützt derzeit einen Teil der WebMCP-APIs. Die folgenden Funktionen werden nicht unterstützt:

- **Deklarative API:** Tools, die über HTML-Formularattribute definiert werden, sind
  nicht als Website-Tools verfügbar.
- **Tools in iframes:** Der Browser findet keine Tools, die in
  iframes registriert sind. Das gilt sowohl für Same-Origin- als auch für Cross-Origin-iframes.

Registriere Tools mit JavaScript auf der obersten Seitenebene, wie im
[nächsten Abschnitt](#add-webmcp-to-your-website) gezeigt. ChatGPT Work und Codex können weiterhin
über die regulären Browserfunktionen mit Formularen interagieren. Diese Interaktionen
sind jedoch keine WebMCP-Tool-Aufrufe.

Die WebMCP-Spezifikation und der Entwicklungsleitfaden von Chrome beschreiben den umfassenderen Funktionsumfang der APIs. Dazu gehören auch Funktionen, die der integrierte Browser derzeit nicht unterstützt.

## WebMCP in deine Website integrieren

Du kannst Codex bitten, die Web-App oder
[Site](/de-DE/codex/sites), an der du arbeitest, um WebMCP-Unterstützung zu erweitern. Beschreibe, was ein Agent tun können soll,
und bitte Codex, auf die vorhandene Logik und die bestehenden Berechtigungen der Anwendung zurückzugreifen.

Beginne mit einer Aktion, die deine Anwendung bereits unterstützt. Zum Beispiel:

- Ein Dashboard, in dem der Agent einen Zeitraum festlegen und die Daten prüfen kann, auf denen ein Diagramm basiert.
- Ein Dokumenteditor, in dem der Agent einen Abschnitt finden, eine Änderung vorschlagen oder einen Kommentar hinterlassen kann, den du prüfen kannst.
- Ein Reiseplaner, in dem der Agent Optionen vergleichen und einen Reiseplan aktualisieren kann, während du dir die Karte ansiehst.

Du kannst den Code auch selbst schreiben. Prüfe im JavaScript-Modul deiner Seite, ob der Browser WebMCP unterstützt, und registriere ein Tool. Dieses Beispiel ohne Schreibzugriff gibt den Titel der aktuellen Seite zurück:

```javascript
if (typeof document.modelContext?.registerTool === "function") {
  await document.modelContext.registerTool({
    name: "get_page_title",
    description: "Read the title of the current page.",
    inputSchema: {
      type: "object",
      properties: {},
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true },
    execute: async () => ({ title: document.title }),
  });
}

Ein kompatibler Agent kann `get_page_title` finden und damit den aktuellen Titel
der Seite abrufen. Wenn ein Tool Argumente akzeptiert, beschreibe sie im Eingabeschema
und verwende sie im `execute`-Handler, um die vorhandene Logik
deiner Anwendung aufzurufen.

Grenze die zulässigen Eingaben eng ein, beschreibe Seiteneffekte und gib genügend Informationen zurück, um das Ergebnis überprüfen zu können. Nutze die vorhandene Authentifizierung, Autorisierung und Eingabevalidierung deiner Anwendung. Behalte die normale Oberfläche für Menschen und für Browser ohne WebMCP-Unterstützung bei.

API-Details und Beispiele findest du in der
[WebMCP-Spezifikation](https://webmachinelearning.github.io/webmcp/) und im
[Entwicklungsleitfaden von Chrome](https://developer.chrome.com/docs/ai/webmcp).
