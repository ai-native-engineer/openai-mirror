<!-- source: https://learn.chatgpt.com/de-DE/docs/app-server -->

Codex app-server ist die Schnittstelle, auf der funktionsreiche Codex-Clients wie die Codex-Erweiterung für VS Code basieren. Nutze sie, wenn du Codex umfassend in dein eigenes Produkt integrieren möchtest: mit Authentifizierung, Unterhaltungsverlauf, Genehmigungen und gestreamten Agentenereignissen. Die app-server-Implementierung ist als Open Source im Codex-Repository auf GitHub verfügbar ([openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)). Eine vollständige Liste der Open-Source-Komponenten von Codex findest du auf der Seite [Open Source](/de-DE/codex/open-source).

  Wenn du Jobs automatisierst oder Codex in CI ausführst, verwende stattdessen das
<a href="/codex/codex-sdk">Codex SDK</a>.

## CLI-Terminaloberfläche verbinden

Im Remote-Modus der Terminaloberfläche kannst du app-server auf einem Computer ausführen und die
Terminaloberfläche der Codex CLI von einem anderen Computer aus damit verbinden. Starte einen WebSocket-Listener:

```bash
codex app-server --listen ws://127.0.0.1:4500

Verbinde dann die Terminaloberfläche:

```bash
codex --remote ws://127.0.0.1:4500

Konfiguriere für eine nicht lokale Verbindung die WebSocket-Authentifizierung und sichere die
Verbindung mit TLS ab. Speichere das Bearer-Token in einer Umgebungsvariablen und
übergib deren Namen, statt das Token in die Befehlszeile einzugeben:

```bash

codex --remote wss://remote-host:4500 \
  --remote-auth-token-env CODEX_REMOTE_TOKEN

Die Option `--remote` akzeptiert die Endpunkte `ws://`, `wss://`, `unix://` und
`unix://PATH`. Verwende unverschlüsselte WebSockets nur für localhost oder eine Verbindung über
eine SSH-Portweiterleitung.

## Remote-Host für den Code-Modus verbinden

Standardmäßig startet app-server einen lokalen Host für den Code-Modus. Um stattdessen einen Remote-Host
zu verwenden, übergib dessen sichere WebSocket-URL:

```bash
codex app-server --code-mode-host wss://code-mode.example.com/host

`--code-mode-host` steuert die ausgehende Verbindung von app-server
zu seinem Host für den Code-Modus. Die Option `--listen` bleibt davon unberührt; sie steuert,
wie sich Clients mit app-server verbinden. Alle Threads im selben app-server-Prozess teilen sich
die ausgewählte Verbindung zum Host für den Code-Modus.

Verwende für einen Remote-Host `wss://`. Verwende `ws://` nur für localhost oder
eine Verbindung mit SSH-Portweiterleitung. Der app-server-Befehl und der WebSocket-Transport sind
experimentell und werden für Produktions-Workloads nicht unterstützt.

## Protokoll

Wie [MCP](https://modelcontextprotocol.io/) unterstützt `codex app-server` die bidirektionale Kommunikation über Nachrichten im Format JSON-RPC 2.0, wobei der Header `"jsonrpc":"2.0"` bei der Übertragung entfällt.

Unterstützte Transportarten:

- `stdio` (`--listen stdio://`, Standard): durch Zeilenumbrüche getrenntes JSON (JSONL).
- `websocket` (`--listen ws://IP:PORT`, experimentell und nicht unterstützt): eine
  JSON-RPC-Nachricht pro WebSocket-Textframe.
- Unix-Socket (`--listen unix://` oder `--listen unix://PATH`): WebSocket-Verbindungen über den
  standardmäßigen app-server-Steuersocket von Codex oder einen benutzerdefinierten
  Unix-Socket-Pfad mit dem standardmäßigen HTTP-Upgrade-Handshake.
- `off` (`--listen off`): keinen lokalen Transport bereitstellen.

Wenn du `--listen ws://IP:PORT` verwendest, stellt derselbe Listener außerdem einfache
HTTP-Health-Checks bereit:

- `GET /readyz` gibt `200 OK` zurück, sobald der Listener neue Verbindungen annimmt.
- `GET /healthz` gibt `200 OK` zurück, wenn die Anfrage keinen `Origin`-Header
  enthält.
- Anfragen mit einem `Origin`-Header werden mit `403 Forbidden` abgelehnt.

Der WebSocket-Transport ist experimentell und wird nicht unterstützt. Lokale Listener wie
`ws://127.0.0.1:PORT` eignen sich für localhost und Arbeitsabläufe mit
SSH-Portweiterleitung. WebSocket-Listener, die nicht an eine Loopback-Adresse gebunden sind, lassen während des Rollouts derzeit standardmäßig
Verbindungen ohne Authentifizierung zu. Konfiguriere daher die WebSocket-Authentifizierung,
bevor du einen solchen Listener remote erreichbar machst.

Unterstützte Flags für die WebSocket-Authentifizierung:

- `--ws-auth capability-token --ws-token-file /absolute/path`
- `--ws-auth capability-token --ws-token-sha256 HEX`
- `--ws-auth signed-bearer-token --ws-shared-secret-file /absolute/path`

Für signierte Bearer-Tokens kannst du außerdem `--ws-issuer`, `--ws-audience` und
`--ws-max-clock-skew-seconds` festlegen. Clients übermitteln die Zugangsdaten beim WebSocket-Handshake als
`Authorization: Bearer <token>`. app-server erzwingt die Authentifizierung
vor dem JSON-RPC-Aufruf `initialize`.

Verwende vorzugsweise `--ws-token-file`, statt Bearer-Tokens im Klartext über die Befehlszeile zu übergeben. Verwende
`--ws-token-sha256` nur, wenn der Client das ursprüngliche Token mit hoher Entropie in einem
separaten lokalen Speicher für Zugangsdaten aufbewahrt. Der Hash dient lediglich zur Verifizierung; Clients benötigen weiterhin
das ursprüngliche Token.

Im WebSocket-Modus verwendet app-server Warteschlangen mit begrenzter Kapazität. Wenn die Warteschlange für eingehende Anfragen voll ist,
lehnt der Server neue Anfragen mit dem JSON-RPC-Fehlercode `-32001` und der Meldung
`"Server overloaded; retry later."` ab. Clients sollten es mit exponentiell
zunehmender Verzögerung und Jitter erneut versuchen.

## Nachrichtenschema

Anfragen enthalten `method`, `params` und `id`:

```json
{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.6-terra" } }

Antworten geben dieselbe `id` zusammen mit entweder `result` oder `error` zurück:

```json
{ "id": 10, "result": { "thread": { "id": "thr_123" } } }

```json
{ "id": 10, "error": { "code": 123, "message": "Something went wrong" } }

Benachrichtigungen lassen `id` weg und verwenden nur `method` und `params`:

```json
{ "method": "turn/started", "params": { "turn": { "id": "turn_456" } } }

Du kannst über die CLI ein TypeScript-Schema oder ein JSON-Schema-Bundle generieren. Jede Ausgabe ist an die ausgeführte Codex-Version gebunden, sodass die generierten Artefakte dieser Version exakt entsprechen:

```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas

## Erste Schritte

1. Starte den Server mit `codex app-server` (standardmäßiger stdio-Transport),
`codex app-server --listen ws://127.0.0.1:4500` (TCP-WebSocket) oder
`codex app-server --listen unix://` (standardmäßiger Unix-Socket).
2. Verbinde einen Client über die ausgewählte Transportart. Sende dann `initialize`, gefolgt von der Benachrichtigung `initialized`.
3. Starte einen Thread und einen Turn und lies danach fortlaufend Benachrichtigungen aus dem aktiven Stream der Transportverbindung.

Beispiel (Node.js / TypeScript):

```ts

const proc = spawn("codex", ["app-server"], {
  stdio: ["pipe", "pipe", "inherit"],
});
const rl = readline.createInterface({ input: proc.stdout });

const send = (message: unknown) => {
  proc.stdin.write(`${JSON.stringify(message)}\n`);
};

let threadId: string | null = null;

rl.on("line", (line) => {
  const msg = JSON.parse(line) as any;
  console.log("server:", msg);

  if (msg.id === 1 && msg.result?.thread?.id && !threadId) {
    threadId = msg.result.thread.id;
    send({
      method: "turn/start",
      id: 2,
      params: {
        threadId,
        input: [{ type: "text", text: "Summarize this repo." }],
      },
    });
  }
});

send({
  method: "initialize",
  id: 0,
  params: {
    clientInfo: {
      name: "my_product",
      title: "My Product",
      version: "0.1.0",
    },
  },
});
send({ method: "initialized", params: {} });
send({ method: "thread/start", id: 1, params: { model: "gpt-5.6-terra" } });

## Grundlegende Konzepte

- **Thread**: Eine Unterhaltung zwischen einer nutzenden Person und dem Codex-Agenten. Threads enthalten Turns.
- **Turn**: Eine einzelne Anfrage einer nutzenden Person und die Arbeit, die der Agent daraufhin ausführt. Turns enthalten Items und stellen inkrementelle Aktualisierungen als Stream bereit.
- **Item**: Eine Ein- oder Ausgabeeinheit (Nachricht von Nutzenden, Agentennachricht, Befehlsausführung, Dateiänderung, Toolaufruf und mehr).

Mit den Thread-APIs kannst du Unterhaltungen erstellen, auflisten oder archivieren. Steuere eine Unterhaltung mit den Turn-APIs und übertrage Fortschrittsmeldungen als Stream über Turn-Benachrichtigungen.

## Lebenszyklus im Überblick

- **Einmal pro Verbindung initialisieren**: Sende unmittelbar nach dem Öffnen einer Transportverbindung eine `initialize`-Anfrage mit den Metadaten deines Clients und anschließend `initialized`. Der Server lehnt alle Anfragen über diese Verbindung ab, die vor diesem Handshake eingehen.
- **Thread starten (oder fortsetzen)**: Rufe `thread/start` auf, um eine neue Unterhaltung zu beginnen, `thread/resume`, um eine bestehende fortzusetzen, oder `thread/fork`, um den Verlauf in einen neuen Thread mit eigener ID zu verzweigen.
- **Turn beginnen**: Rufe `turn/start` mit der `threadId` des Ziel-Threads und der Eingabe der nutzenden Person auf. Optionale Felder überschreiben die Einstellungen für Modell, Persönlichkeit, `cwd`, Sandbox-Richtlinie und weitere Optionen.
- **Aktiven Turn steuern**: Rufe `turn/steer` auf, um dem derzeit laufenden Turn weitere Eingaben der nutzenden Person hinzuzufügen, ohne einen neuen Turn zu erstellen.
- **Ereignisse streamen**: Lies nach `turn/start` die Benachrichtigungen auf stdout fortlaufend weiter: `thread/archived`, `thread/unarchived`, `item/started`, `item/completed`, `item/agentMessage/delta`, Fortschrittsmeldungen von Tools und weitere Aktualisierungen.
- **Turn abschließen**: Der Server sendet `turn/completed` mit dem endgültigen Status, wenn das Modell seine Arbeit beendet oder der Turn über `turn/interrupt` abgebrochen wurde.

## Initialisierung

Clients müssen pro Transportverbindung genau eine `initialize`-Anfrage senden, bevor sie über diese Verbindung eine andere Methode aufrufen, und die Initialisierung anschließend mit einer `initialized`-Benachrichtigung bestätigen. Für Anfragen vor der Initialisierung wird der Fehler `Not initialized` zurückgegeben; wiederholte Aufrufe von `initialize` über dieselbe Verbindung geben `Already initialized` zurück.

Der Server gibt den User-Agent-String zurück, den er an vorgelagerte Dienste übermittelt, sowie Werte für `platformFamily` und `platformOs`, die die Laufzeitplattform beschreiben. Lege `clientInfo` fest, um deine Integration zu identifizieren.

`initialize.params.capabilities` unterstützt außerdem folgende Clientfunktionen:

- `optOutNotificationMethods`: exakte Namen der Benachrichtigungsmethoden, die für
  diese Verbindung unterdrückt werden sollen. Der Abgleich erfolgt exakt, ohne Wildcards oder Präfixe.
  Unbekannte Namen werden akzeptiert und ignoriert.
- `requestAttestation`: lässt die vom Server initiierte Anfrage `attestation/generate` zu.
  Desktop-Hosts, die eine Attestierung gegenüber vorgelagerten Diensten bereitstellen, antworten mit einem
  opaken Wert im Format `{ "token": "..." }`.
- `mcpServerOpenaiFormElicitation`: erlaubt nachgelagerten MCP-Servern, die
  erweiterte OpenAI-Formularvariante von `mcpServer/elicitation/request` zu senden.

**Wichtig**: Verwende `clientInfo.name`, um deinen Client für die Plattform für Compliance-Protokolle von OpenAI zu identifizieren. Wenn du eine neue Codex-Integration für den Einsatz in Unternehmen entwickelst, wende dich bitte an OpenAI, damit dein Client in die Liste bekannter Clients aufgenommen wird. Weitere Informationen findest du in der [Referenz zu Codex-Protokollen](https://chatgpt.com/public/admin/api-reference#tag/Codex).

Beispiel (aus der Codex-Erweiterung für VS Code):

```json
{
  "method": "initialize",
  "id": 0,
  "params": {
    "clientInfo": {
      "name": "codex_vscode",
      "title": "Codex VS Code Extension",
      "version": "0.1.0"
    }
  }
}

Beispiel für das Unterdrücken von Benachrichtigungen:

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true,
      "optOutNotificationMethods": ["thread/started", "item/agentMessage/delta"]
    }
  }
}

## Experimentelle API aktivieren

Einige app-server-Methoden und -Felder sind bewusst nur verfügbar, wenn die Clientfunktion `experimentalApi` aktiviert ist.

- Lass `capabilities` weg (oder setze `experimentalApi` auf `false`), damit du nur die stabile API verwendest. Der Server lehnt dann experimentelle Methoden und Felder ab.
- Setze `capabilities.experimentalApi` auf `true`, um experimentelle Methoden und Felder zu aktivieren.

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true
    }
  }
}

Wenn ein Client eine experimentelle Methode oder ein experimentelles Feld sendet, ohne die experimentelle API zuvor aktiviert zu haben, lehnt app-server die Anfrage wie folgt ab:

`<descriptor> requires experimentalApi capability`

## API-Übersicht

- `thread/start`: Erstellt einen neuen Thread, sendet `thread/started` und abonniert für dich automatisch die Turn- und Item-Ereignisse dieses Threads.
- `thread/resume`: Öffnet einen vorhandenen Thread anhand seiner ID erneut, sodass spätere Aufrufe von `turn/start` den Thread ergänzen.
- `thread/fork`: Forkt einen Thread unter einer neuen Thread-ID, indem der gespeicherte Verlauf kopiert wird. Übergib `lastTurnId`, um den Verlauf bis einschließlich dieses Turns zu kopieren und spätere Turns auszulassen, oder `ephemeral: true`, um einen Fork im Arbeitsspeicher zu erstellen. Sendet `thread/started` für den neuen Thread; zurückgegebene Threads enthalten, sofern verfügbar, `forkedFromId`.
- `thread/read`: Liest einen gespeicherten Thread anhand seiner ID, ohne ihn fortzusetzen. Setze `includeTurns`, um den vollständigen Turn-Verlauf zu erhalten. Zurückgegebene Objekte vom Typ `thread` enthalten den Laufzeitstatus im Feld `status`.
- `thread/list`: Listet gespeicherte Thread-Protokolle seitenweise auf. Unterstützt cursorbasierte Paginierung sowie die Filter `modelProviders`, `sourceKinds`, `archived`, `isPinned`, `cwd`, `useStateDbOnly`, `searchTerm` und die experimentellen Filter `parentThreadId` oder `ancestorThreadId`. Zurückgegebene Objekte vom Typ `thread` enthalten den Laufzeitstatus im Feld `status`.
- `thread/turns/list`: Experimentell; liest den Turn-Verlauf eines gespeicherten Threads seitenweise aus, ohne den Thread fortzusetzen. `itemsView` steuert, ob Turn-Items ausgelassen, zusammengefasst oder vollständig geladen werden.
- `thread/items/list`: Experimentell; liest dauerhaft gespeicherte Thread-Items seitenweise aus, optional beschränkt auf eine bestimmte `turnId`. Der aktive Thread-Speicher muss die Paginierung von Items unterstützen.
- `thread/loaded/list`: Listet die IDs der derzeit im Arbeitsspeicher geladenen Threads auf.
- `thread/name/set`: Legt für einen geladenen Thread oder einen dauerhaft gespeicherten Rollout den angezeigten Thread-Namen fest oder aktualisiert ihn; sendet `thread/name/updated`.
- `thread/goal/set`: Legt das Ziel eines Threads fest; sendet `thread/goal/updated`.
- `thread/goal/get`: Liest das aktuelle Ziel eines Threads aus.
- `thread/goal/clear`: Löscht das Ziel eines Threads; sendet `thread/goal/cleared`.
- `thread/metadata/update`: Aktualisiert gezielt die in SQLite gespeicherten Thread-Metadaten, einschließlich der dauerhaft gespeicherten Felder `gitInfo` und `isPinned`.
- `thread/archive`: Verschiebt die Protokolldatei eines Threads in das Archivverzeichnis und versucht, die noch nicht archivierten Protokolldateien der von ihm erzeugten nachgeordneten Threads zu archivieren. Gibt bei Erfolg `{}` zurück und sendet für jeden archivierten Thread `thread/archived`.
- `thread/delete`: Löscht einen dauerhaft gespeicherten aktiven oder archivierten Thread und alle von ihm erzeugten nachgeordneten Threads endgültig. Gibt bei Erfolg `{}` zurück und sendet für jeden gelöschten Thread `thread/deleted`.
- `thread/unsubscribe`: Beendet für diese Verbindung das Abonnement der Turn- und Item-Ereignisse des Threads. Wenn dies die letzte abonnierte Verbindung war, entfernt der Server den Thread nach einer Inaktivitätsfrist ohne abonnierte Verbindungen aus dem Arbeitsspeicher und sendet `thread/closed`.
- `thread/unarchive`: Stellt einen archivierten Thread-Rollout im Verzeichnis der aktiven Sitzungen wieder her. Gibt das wiederhergestellte `thread`-Objekt zurück und sendet `thread/unarchived`.
- `thread/status/changed`: Benachrichtigung, die gesendet wird, wenn sich der Laufzeitstatus im Feld `status` eines geladenen Threads ändert.
- `thread/compact/start`: Löst die Compaction (Kontextverdichtung) des Gesprächsverlaufs für einen Thread aus. Gibt sofort `{}` zurück, während der Fortschritt über Benachrichtigungen vom Typ `turn/*` und `item/*` gestreamt wird.
- `thread/shellCommand`: Führt einen von Nutzenden angestoßenen Shell-Befehl für einen Thread aus. Dieser wird außerhalb der Sandbox mit Vollzugriff ausgeführt und übernimmt nicht die Sandbox-Richtlinie des Threads.
- `thread/backgroundTerminals/clean`: Stoppt alle laufenden Hintergrundterminals eines Threads (experimentell; erfordert `capabilities.experimentalApi`).
- `thread/backgroundTerminals/list`: Listet die laufenden Hintergrundterminals eines geladenen Threads auf (experimentell; erfordert `capabilities.experimentalApi`).
- `thread/backgroundTerminals/terminate`: Beendet ein laufendes Hintergrundterminal anhand der app-server-Kennung `processId` (experimentell; erfordert `capabilities.experimentalApi`).
- `thread/rollback`: Veraltet; entfernt die letzten N Turns aus dem Kontext im Arbeitsspeicher und speichert eine Rollback-Markierung dauerhaft. Gibt das aktualisierte `thread`-Objekt zurück.
- `turn/start`: Fügt einem Thread Benutzereingaben oder eigenständige Tool-Ausgaben hinzu und startet die Generierung durch Codex. Antwortet mit dem initialen `turn`-Objekt und streamt Ereignisse. Für `collaborationMode` bedeutet `settings.developer_instructions: null`: „Verwende die integrierten Anweisungen für den ausgewählten Modus.“
- `thread/inject_items`: Fügt dem für das Modell sichtbaren Verlauf eines geladenen Threads unverarbeitete Items der Responses API hinzu, ohne einen Turn mit Benutzereingabe zu starten.
- `turn/steer`: Fügt dem aktuell laufenden Turn eines Threads weitere Benutzereingaben hinzu; gibt die akzeptierte `turnId` zurück.
- `turn/interrupt`: Fordert den Abbruch eines laufenden Turns an. Bei Erfolg wird `{}` zurückgegeben und der Turn endet mit `status: "interrupted"`.
- `review/start`: Startet den Codex-Reviewer für einen Thread; sendet Items vom Typ `enteredReviewMode` und `exitedReviewMode`.
- `command/exec`: Führt einen einzelnen Befehl in der Sandbox des Servers aus, ohne einen Thread oder Turn zu starten.
- `command/exec/write`: Schreibt Bytes in `stdin` einer laufenden Sitzung von `command/exec` oder schließt `stdin`.
- `command/exec/resize`: Ändert die Größe einer laufenden, PTY-gestützten Sitzung von `command/exec`.
- `command/exec/terminate`: Beendet eine laufende Sitzung von `command/exec`.
- `command/exec/outputDelta` (Benachrichtigung): Wird für Base64-codierte stdout/stderr-Datenblöcke gesendet, die aus einer Sitzung von `command/exec` gestreamt werden.
- `process/spawn`: Startet eine explizite Prozesssitzung außerhalb der Codex-Sandbox (experimentell; erfordert `capabilities.experimentalApi`).
- `process/writeStdin`: Schreibt Bytes in stdin einer laufenden Sitzung von `process/spawn` oder schließt stdin (experimentell).
- `process/resizePty`: Ändert die Größe einer laufenden, PTY-gestützten Prozesssitzung (experimentell).
- `process/kill`: Beendet eine laufende Prozesssitzung (experimentell).
- `process/outputDelta` und `process/exited` (Benachrichtigungen): Werden für gestreamte Prozessausgaben und den Exit-Status des Prozesses gesendet (experimentell).
- `model/list`: Listet verfügbare Modelle auf (setze `includeHidden: true`, um Einträge mit `hidden: true` einzuschließen). Enthalten sind Optionen für den Reasoning-Aufwand, optional `upgrade` sowie `inputModalities`.
- `modelProvider/capabilities/read`: Liest für Kombinationen aus Modell und Anbieter die Grenzen der vom Anbieter unterstützten Funktionen aus.
- `experimentalFeature/list`: Listet Feature-Flags mit Metadaten zur Lebenszyklusphase und cursorbasierter Paginierung auf.
- `experimentalFeature/enablement/set`: Aktualisiert gezielt die Laufzeiteinstellungen im Arbeitsspeicher für unterstützte Funktionsschlüssel wie `apps` und `plugins`.
- `environment/info`: Experimentell; stellt eine Verbindung zu einer konfigurierten Ausführungsumgebung her und gibt deren Shell sowie das standardmäßige Arbeitsverzeichnis zurück.
- `permissionProfile/list`: Listet mit cursorbasierter Paginierung Beta-Berechtigungsprofile auf und gibt an, ob die geltenden Anforderungen sie zulassen.
- `collaborationMode/list`: Listet Voreinstellungen für den Modus zur Zusammenarbeit auf (experimentell, ohne Paginierung).
- `skills/list`: Listet Skills für einen oder mehrere Werte von `cwd` auf (unterstützt `forceReload` und optional `perCwdExtraUserRoots`).
- `skills/extraRoots/set`: Ersetzt die zusätzlichen Stammverzeichnisse auf Prozessebene, die zur Suche nach eigenständigen Skills dienen. Die Stammverzeichnisse werden dabei nicht dauerhaft gespeichert.
- `skills/changed` (Benachrichtigung): Wird gesendet, wenn sich überwachte lokale Skill-Dateien ändern.
- `hooks/list`: Listet erkannte Lebenszyklus-Hooks für einen oder mehrere Werte von `cwd` auf.
- `marketplace/add`: Fügt einen Remote-Marketplace für Plug-ins hinzu und speichert ihn dauerhaft in der benutzerspezifischen Marketplace-Konfiguration.
- `marketplace/remove`: Entfernt einen konfigurierten Marketplace und, sofern vorhanden, dessen installiertes Stammverzeichnis.
- `marketplace/upgrade`: Aktualisiert einen konfigurierten Git-Marketplace oder alle konfigurierten Git-Marketplaces, wenn du den Marketplace-Namen weglässt.
- `plugin/list`: In Entwicklung; listet erkannte Plug-in-Marketplaces und den Status von Plug-ins auf, einschließlich Metadaten zu Installations- und Authentifizierungsrichtlinien, Fehlern beim Laden von Marketplaces, IDs hervorgehobener Plug-ins sowie Metadaten zu Plug-in-Quellen (lokal, Git, Paketregistry oder Remote). Zusammenfassungen können die Remote-Version `version`, die lokale Version `localVersion`, strukturierte Symbole für helle und dunkle Darstellungen sowie `installPolicySource` enthalten. Letzteres kann bei aktuellen Remote-Einträgen `null`, `WORKSPACE_SETTING` oder `IMPLICIT_CANONICAL_APP` sein. Rufe diese Methode in Produktions-Clients noch nicht auf.
- `plugin/read`: In Entwicklung; liest ein Plug-in anhand des Marketplace-Pfads oder des Namens des Remote-Marketplaces sowie des Plug-in-Namens aus. Enthalten sind gebündelte Skills, Apps, MCP-Servernamen und das Feld `shareUrl` für ein Remote-Plug-in, sofern der Remote-Katalog einen entsprechenden Wert bereitstellt. Rufe diese Methode in Produktions-Clients noch nicht auf.
- `plugin/install`: In Entwicklung; installiert ein Plug-in über einen Marketplace-Pfad oder den Namen eines Remote-Marketplaces. Rufe diese Methode in Produktions-Clients noch nicht auf.
- `plugin/uninstall`: In Entwicklung; deinstalliert ein installiertes Plug-in. Rufe diese Methode in Produktions-Clients noch nicht auf.
- `plugin/skill/read`: Liest bei Bedarf den Markdown-Inhalt eines Skills aus einem Remote-Plug-in anhand des Remote-Marketplaces, der Plug-in-ID und des Skill-Namens aus.
- `app/installed`: Liest den Laufzeitzustand installierter Apps aus, einschließlich des jeweils wirksamen Aktivierungsstatus und der Aufrufbarkeit.
- `app/list`: Listet verfügbare Apps (Konnektoren) mit Paginierung sowie Metadaten zum Zugriffs- und Aktivierungsstatus auf.
- `app/read`: Ruft Metadaten und optionale, ausschließlich zur Anzeige bestimmte Tool-Zusammenfassungen für bestimmte App-IDs ab.
- `skills/config/write`: aktiviert oder deaktiviert Skills anhand ihres Pfads.
- `mcpServer/oauth/login`: startet eine OAuth-Anmeldung für einen konfigurierten MCP-Server, gibt eine Autorisierungs-URL zurück und sendet nach Abschluss `mcpServer/oauthLogin/completed`.
- `tool/requestUserInput`: stellt Nutzenden für einen Tool-Aufruf 1 bis 3 kurze Fragen (experimentell); für eine Freitextoption lässt sich in den Fragen `isOther` festlegen.
- `mcpServer/elicitation/request` (Serveranfrage): fordert vom Client strukturierte Formulareingaben oder die Bestätigung eines von einem MCP-Server angeforderten URL-basierten Ablaufs an.
- `item/permissions/requestApproval` (Serveranfrage): fordert den Client auf, eine Teilmenge der vom integrierten Tool `request_permissions` angeforderten Netzwerk- oder Dateisystemberechtigungen zu gewähren.
- `config/mcpServer/reload`: lädt die MCP-Server-Konfiguration vom Datenträger neu und stellt eine Aktualisierung für geladene Threads in die Warteschlange.
- `mcpServerStatus/list`: listet MCP-Server, Tools, Ressourcen und den Authentifizierungsstatus auf (Paginierung mit Cursor und Limit). Verwende `detail: "full"` für vollständige Daten oder `detail: "toolsAndAuthOnly"`, um Ressourcen auszulassen.
- `mcpServer/resource/read`: liest über einen initialisierten MCP-Server eine einzelne MCP-Ressource.
- `mcpServer/tool/call`: ruft auf dem konfigurierten MCP-Server eines Threads ein Tool auf.
- `mcpServer/startupStatus/updated` (Benachrichtigung): wird gesendet, wenn sich der Startstatus eines konfigurierten MCP-Servers für einen geladenen Thread ändert.
- `windowsSandbox/setupStart`: startet das Setup der Windows-Sandbox für den Modus `elevated` oder `unelevated`, antwortet zügig und sendet später `windowsSandbox/setupCompleted`.
- `feedback/upload`: sendet einen Feedbackbericht (Klassifizierung, optionaler Grund/optionale Protokolle, Konversations-ID sowie optionale Anhänge in `extraLogFiles`).
- `config/read`: ruft nach dem Zusammenführen der Konfigurationsebenen die effektive Konfiguration vom Datenträger ab.
- `externalAgentConfig/detect`: erkennt mit `includeHome` und optional `cwds` migrierbare Artefakte externer Agenten; jedes erkannte Element enthält `cwd` (`null` für das Home-Verzeichnis).
- `externalAgentConfig/import`: wendet ausgewählte Migrationseinträge externer Agenten an, indem du `migrationItems` explizit mit `cwd` übergibst (`null` für das Home-Verzeichnis). Unterstützte Elementtypen sind Konfiguration, Skills, `AGENTS.md`, Plug-ins, MCP-Server-Konfiguration, Subagenten, Hooks, Befehle und Sitzungen. Bei nicht leeren Importen werden mit dem Abschluss der jeweiligen Verarbeitungsschritte `externalAgentConfig/import/progress` und `externalAgentConfig/import/completed` gesendet. Der Import von Plug-ins und Sitzungen kann asynchron abgeschlossen werden.
- `config/value/write`: schreibt einen einzelnen Konfigurationsschlüssel samt Wert in die benutzerspezifische Datei `config.toml` auf dem Datenträger.
- `config/batchWrite`: übernimmt Konfigurationsänderungen atomar in die benutzerspezifische Datei `config.toml` auf dem Datenträger.
- `configRequirements/read`: ruft Anforderungen aus `requirements.toml` und/oder MDM ab, darunter die exakte verwaltete Konfiguration, Zulassungslisten, fest vorgegebene `featureRequirements` und Netzwerkanforderungen (oder `null`, falls du keine eingerichtet hast).
- `fs/readFile`, `fs/writeFile`, `fs/createDirectory`, `fs/getMetadata`, `fs/readDirectory`, `fs/remove`, `fs/copy`, `fs/watch`, `fs/unwatch` und `fs/changed` (Benachrichtigung): führen über die Dateisystem-API v2 von app-server Operationen auf absoluten Dateisystempfaden aus.

Plug-in-Zusammenfassungen enthalten einen Union-Typ `source`. Lokale Plug-ins geben
`{ "type": "local", "path": ... }` zurück, Git-basierte Marketplace-Einträge geben
`{ "type": "git", "url": ..., "path": ..., "refName": ..., "sha": ... }` zurück,
Einträge aus Paketregistern geben
`{ "type": "npm", "package": ..., "version": ..., "registry": ... }` zurück und
Remote-Katalogeinträge geben `{ "type": "remote" }` zurück. Bei ausschließlich remote verfügbaren
Katalogeinträgen kann `PluginMarketplaceEntry.path` den Wert `null` haben. Übergib
`remoteMarketplaceName` statt `marketplacePath`, wenn du diese Plug-ins liest oder
installierst.

## Modelle

### Modelle auflisten (`model/list`)

Rufe `model/list` auf, um verfügbare Modelle und ihre Funktionen zu ermitteln, bevor du Auswahlmenüs für Modelle oder Persönlichkeiten anzeigst.

```json
{ "method": "model/list", "id": 6, "params": { "limit": 20, "includeHidden": false } }
{ "id": 6, "result": {
  "data": [{
    "id": "gpt-5.6-sol",
    "model": "gpt-5.6-sol",
    "displayName": "GPT-5.6-Sol",
    "hidden": false,
    "defaultReasoningEffort": "low",
    "supportedReasoningEfforts": [{
      "reasoningEffort": "low",
      "description": "Fast responses with lighter reasoning"
    }],
    "inputModalities": ["text", "image"],
    "supportsPersonality": true,
    "isDefault": true
  }],
  "nextCursor": null
} }

Jeder Modelleintrag kann Folgendes enthalten:

- `supportedReasoningEfforts`: vom Modell unterstützte Optionen für den Reasoning-Aufwand.
- `defaultReasoningEffort`: vorgeschlagener Standardwert für den Reasoning-Aufwand in Clients.
- `upgrade`: optionale ID des als Upgrade empfohlenen Modells für Migrations-Prompts in Clients.
- `upgradeInfo`: optionale Upgrade-Metadaten für Migrations-Prompts in Clients.
- `hidden`: gibt an, ob das Modell in der standardmäßigen Auswahlliste ausgeblendet ist.
- `inputModalities`: vom Modell unterstützte Eingabetypen (zum Beispiel `text`, `image`).
- `supportsPersonality`: gibt an, ob das Modell persönlichkeitsspezifische Anweisungen wie `/personality` unterstützt.
- `isDefault`: gibt an, ob das Modell als Standard empfohlen wird.

Standardmäßig gibt `model/list` nur Modelle zurück, die in der Auswahlliste sichtbar sind. Lege `includeHidden: true` fest, wenn du die vollständige Liste benötigst und clientseitig anhand von `hidden` filtern möchtest.

Wenn `inputModalities` fehlt (bei älteren Modellkatalogen), verwende zur Abwärtskompatibilität `["text", "image"]` als Ersatzwert.

### Experimentelle Funktionen auflisten (`experimentalFeature/list`)

Über diesen Endpunkt kannst du Feature-Flags mit Metadaten und Lebenszyklusphase ermitteln:

```json
{ "method": "experimentalFeature/list", "id": 7, "params": { "limit": 20 } }
{ "id": 7, "result": {
  "data": [{
    "name": "unified_exec",
    "stage": "beta",
    "displayName": "Unified exec",
    "description": "Use the unified PTY-backed execution tool.",
    "announcement": "Beta rollout for improved command execution reliability.",
    "enabled": false,
    "defaultEnabled": false
  }],
  "nextCursor": null
} }

`stage` kann `beta`, `underDevelopment`, `stable`, `deprecated` oder `removed` sein. Bei Flags außerhalb der Betaphase können `displayName`, `description` und `announcement` den Wert `null` haben.

### Ausführungsumgebung prüfen (experimentell)

Verwende `environment/info`, um eine konfigurierte Remote-Umgebung zu prüfen, bevor du
dort mit der Arbeit beginnst. Die Methode erfordert `capabilities.experimentalApi = true`.

```json
{ "method": "environment/info", "id": 8, "params": { "environmentId": "devbox" } }
{ "id": 8, "result": {
  "shell": { "name": "zsh", "path": "/bin/zsh" },
  "cwd": "file:///workspace/project"
} }

`cwd` kann `null` sein. Wenn ein Wert vorhanden ist, handelt es sich um einen kanonischen URI des Typs `file:`, der die
native Pfadsyntax der Umgebung verwendet. Unbekannte Umgebungs-IDs sowie Verbindungs- oder
Protokollfehler führen zu Anfragefehlern.

## Threads

- `thread/read` liest einen gespeicherten Thread, ohne ihn zu abonnieren. Lege `includeTurns` fest, um Turns einzuschließen.
- `thread/turns/list` ist experimentell und ruft den Turn-Verlauf eines gespeicherten Threads seitenweise ab, ohne
  ihn fortzusetzen. Lege mit `itemsView` fest, ob Turn-Elemente ausgelassen,
  zusammengefasst oder vollständig geladen werden.
- `thread/items/list` ist experimentell und ruft persistierte Thread-Elemente seitenweise ab, optional auf einen Turn beschränkt.
- `thread/list` unterstützt Cursor-Paginierung sowie Filter nach `modelProviders`, `sourceKinds`, `archived`, `isPinned`, `cwd`, `useStateDbOnly`, `searchTerm` und experimentell nach `parentThreadId` oder `ancestorThreadId`.
- `thread/loaded/list` gibt die IDs der derzeit im Arbeitsspeicher geladenen Threads zurück.
- `thread/archive` verschiebt das persistierte JSONL-Protokoll des Threads in das Archivverzeichnis und versucht, auch die Protokolle der aus ihm hervorgegangenen Threads zu archivieren, sofern sie noch nicht archiviert sind.
- `thread/delete` löscht einen persistierten aktiven oder archivierten Thread sowie die aus ihm hervorgegangenen Threads dauerhaft.
- `thread/metadata/update` aktualisiert gezielt gespeicherte Thread-Metadaten, einschließlich der persistierten Felder `gitInfo` und `isPinned`.
- `thread/unsubscribe` beendet für die aktuelle Verbindung das Abonnement eines geladenen Threads und kann nach Ablauf einer Inaktivitätsfrist `thread/closed` auslösen.
- `thread/unarchive` stellt den Rollout eines archivierten Threads im Verzeichnis für aktive Sitzungen wieder her.
- `thread/compact/start` löst eine Compaction (Kontextverdichtung) aus und gibt sofort `{}` zurück.
- `thread/rollback` ist veraltet. Die Methode entfernt die letzten N Turns aus dem Kontext im Arbeitsspeicher und schreibt eine Rollback-Markierung in das persistierte JSONL-Protokoll des Threads.
- `thread/inject_items` fügt unverarbeitete Elemente der Responses API an den für das Modell sichtbaren Verlauf eines geladenen Threads an, ohne einen Turn für eine Nutzereingabe zu starten.

### Thread starten oder fortsetzen

Starte einen neuen Thread, wenn du eine neue Codex-Konversation benötigst.

```json
{ "method": "thread/start", "id": 10, "params": {
  "model": "gpt-5.6-terra",
  "cwd": "/Users/me/project",
  "approvalPolicy": "never",
  "sandbox": "workspaceWrite",
  "personality": "friendly",
  "serviceName": "my_app_server_client"
} }
{ "id": 10, "result": {
  "thread": {
    "id": "thr_123",
    "sessionId": "thr_123",
    "preview": "",
    "ephemeral": false,
    "modelProvider": "openai",
    "createdAt": 1730910000
  }
} }
{ "method": "thread/started", "params": { "thread": { "id": "thr_123" } } }

`serviceName` ist optional. Gib einen Wert an, wenn app-server Metriken auf Thread-Ebene mit dem Dienstnamen deiner Integration kennzeichnen soll.

`thread/start`, `thread/resume` und `thread/fork` geben
`instructionSources` zurück, ein Array mit den Pfaden geladener Anweisungsdateien. Jeder Pfad verwendet
die native Syntax seiner Quellumgebung für absolute Pfade. Das gilt auch
für Remote-Umgebungen.

Experimentelle Clients können `historyMode` für `thread/start` auf `"legacy"`
(Standard) oder `"paginated"` setzen. Das Erstellen paginierter Threads wird noch nicht unterstützt
und führt zum JSON-RPC-Fehler `-32601`. App-server kann Zusammenfassungen vorhandener
paginierter Datensätze auflisten und lesen. Abfragen des vollständigen Verlaufs, die Turn-Paginierung und das Fortsetzen
werden jedoch sicherheitshalber abgelehnt, bis paginierte Verläufe unterstützt werden.

Beta-Clients, die `capabilities.experimentalApi` aktivieren, können die ID eines benannten
Berechtigungsprofils im Feld `permissions` übergeben, statt das bisherige Feld `sandbox` zu verwenden.
Sende `permissions` und `sandbox` nicht zusammen. Verwende
`permissionProfile/list` mit dem `cwd` des Projekts, um verfügbare Profile zu ermitteln
und zu prüfen, ob die verwalteten Anforderungen jedes einzelne zulassen.

`thread.sessionId` kennzeichnet die Wurzel des derzeit aktiven Sitzungsbaums. Root-Threads
verwenden ihre eigene Thread-ID als Sitzungs-ID; geforkte Threads behalten die Sitzungs-ID
der Wurzel, von der sie abstammen. Clients sollten die Sitzungs-ID aus
`thread.sessionId` lesen, statt sie aus der Thread-ID abzuleiten.

Um eine gespeicherte Sitzung fortzusetzen, rufe `thread/resume` mit der zuvor gespeicherten `thread.id` auf. Die Antwort hat dieselbe Struktur wie bei `thread/start`. Du kannst auch dieselben abweichenden Konfigurationseinstellungen übergeben, die `thread/start` unterstützt, zum Beispiel `personality`:

```json
{ "method": "thread/resume", "id": 11, "params": {
  "threadId": "thr_123",
  "personality": "friendly"
} }
{ "id": 11, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false } } }

Allein durch das Fortsetzen eines Threads werden weder `thread.updatedAt` noch der Änderungszeitpunkt der Rollout-Datei aktualisiert. Der Zeitstempel wird aktualisiert, wenn du einen Turn startest.

Wenn du einen aktivierten MCP-Server in der Konfiguration als `required` kennzeichnest und seine Initialisierung fehlschlägt, schlagen `thread/start` und `thread/resume` fehl, anstatt ohne ihn fortzufahren.

`dynamicTools` in `thread/start` ist ein experimentelles Feld (erfordert `capabilities.experimentalApi = true`). Codex speichert diese dynamischen Tools in den Rollout-Metadaten des Threads und stellt sie bei `thread/resume` wieder her, wenn du keine neuen dynamischen Tools angibst.

Wenn du einen Thread mit einem anderen Modell fortsetzt als dem im Rollout gespeicherten, gibt Codex eine Warnung aus und wendet beim nächsten Turn einmalig eine Anweisung zum Modellwechsel an.

### Ziel eines Threads verwalten

Verwende `thread/goal/set`, `thread/goal/get` und `thread/goal/clear`, um
denselben gespeicherten Zustand des Ziels zu verwalten, der auch über `/goal` in der TUI verfügbar ist.

```json
{ "method": "thread/goal/set", "id": 13, "params": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000
} }
{ "id": 13, "result": { "goal": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000,
  "tokensUsed": 0,
  "timeUsedSeconds": 0
} } }
{ "method": "thread/goal/updated", "params": {
  "threadId": "thr_123",
  "goal": {
    "threadId": "thr_123",
    "objective": "Finish the migration and keep tests green",
    "status": "active",
    "tokenBudget": 40000,
    "tokensUsed": 0,
    "timeUsedSeconds": 0
  }
} }

Zielvorgaben dürfen nicht leer sein und höchstens 4.000 Zeichen enthalten. Eine neue
Zielvorgabe ersetzt das Ziel und setzt die Nutzungserfassung zurück. Gibst du die aktuelle Zielvorgabe eines Ziels ohne Endstatus an
oder lässt du `objective` weg, werden der Status oder das Token-Budget aktualisiert,
während der Nutzungsverlauf erhalten bleibt.

Um von einer gespeicherten Sitzung abzuzweigen, rufe `thread/fork` mit `thread.id` auf. Dadurch wird eine neue Thread-ID erstellt und dafür eine Benachrichtigung vom Typ `thread/started` ausgegeben. Übergib
`lastTurnId`, um den Verlauf bis einschließlich dieses Turns zu kopieren und spätere
Turns auszulassen:

```json
{ "method": "thread/fork", "id": 12, "params": { "threadId": "thr_123", "lastTurnId": "turn_456" } }
{ "id": 12, "result": { "thread": { "id": "thr_456", "sessionId": "thr_123", "forkedFromId": "thr_123" } } }
{ "method": "thread/started", "params": { "thread": { "id": "thr_456" } } }

App Server lehnt `lastTurnId` ab, wenn der zugehörige Turn noch läuft. Lässt du das Feld weg, während im
Quell-Thread gerade ein Turn läuft, wird beim Forken eine Unterbrechungsmarkierung aufgezeichnet, statt
einen nicht gekennzeichneten unvollständigen Turn beizubehalten.

Übergib `ephemeral: true`, um einen Fork im Arbeitsspeicher zu erstellen, ohne ihn in Listen
gespeicherter Threads aufzunehmen:

```json
{
  "method": "thread/fork",
  "id": 13,
  "params": {
    "threadId": "thr_123",
    "ephemeral": true
  }
}
{
  "id": 13,
  "result": {
    "thread": {
      "id": "thr_789",
      "sessionId": "thr_789",
      "forkedFromId": "thr_123",
      "ephemeral": true
    }
  }
}

Für temporäre Forks von Threads mit Paginierung ist außerdem `excludeTurns: true` erforderlich.
Dieses Feld ist experimentell und erfordert `capabilities.experimentalApi = true`.

Wenn ein in der Benutzeroberfläche sichtbarer Thread-Titel festgelegt wurde, befüllt App Server das Feld `thread.name` in Antworten auf `thread/list`, `thread/read`, `thread/resume`, `thread/unarchive` und `thread/rollback`. In Antworten auf `thread/start` und `thread/fork` kann `name` fehlen oder `null` zurückgegeben werden, bis später ein Titel festgelegt wird.

### Gespeicherten Thread lesen (ohne ihn fortzusetzen)

Verwende `thread/read`, wenn du gespeicherte Thread-Daten benötigst, den Thread aber weder fortsetzen noch seine Ereignisse abonnieren möchtest.

- `includeTurns`: Bei `true` enthält die Antwort die Turns des Threads. Bei `false` oder wenn das Feld fehlt, erhältst du nur die Thread-Zusammenfassung.
- Zurückgegebene Objekte vom Typ `thread` enthalten im Feld `status` den Laufzeitstatus (`notLoaded`, `idle`, `systemError` oder `active` mit `activeFlags`).

```json
{ "method": "thread/read", "id": 19, "params": { "threadId": "thr_123", "includeTurns": true } }
{ "id": 19, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false, "status": { "type": "notLoaded" }, "turns": [] } } }

Anders als `thread/resume` lädt `thread/read` den Thread nicht in den Arbeitsspeicher und gibt keine Benachrichtigung vom Typ `thread/started` aus.

### Turns eines Threads auflisten

`thread/turns/list` ist experimentell. Verwende die Methode, um den Turn-Verlauf eines gespeicherten Threads seitenweise abzurufen, ohne ihn fortzusetzen. Standardmäßig werden die neuesten Ergebnisse zuerst zurückgegeben, sodass Clients mit `nextCursor` ältere Turns abrufen können. Die Antwort enthält außerdem `backwardsCursor`. Übergib diesen Wert als `cursor` zusammen mit `sortDirection: "asc"`, um Turns abzurufen, die neuer sind als das erste Element der zuvor abgerufenen Seite.

`itemsView` steuert, in welchem Umfang die Antwort Daten zu den Elementen eines Turns enthält:

- `notLoaded` lässt die Elemente weg.
- `summary` gibt zusammengefasste Elementdaten zurück und ist der Standardwert, wenn das Feld fehlt.
- `full` gibt vollständige Elementdaten zurück.

```json
{ "method": "thread/turns/list", "id": 20, "params": {
  "threadId": "thr_123",
  "limit": 50,
  "sortDirection": "desc",
  "itemsView": "summary"
} }
{ "id": 20, "result": {
  "data": [],
  "nextCursor": "older-turns-cursor-or-null",
  "backwardsCursor": "newer-turns-cursor-or-null"
} }

`thread/items/list` ist ebenfalls experimentell. Damit kannst du gespeicherte Elemente seitenweise abrufen, ohne
den Thread fortzusetzen. Übergib `turnId`, um die Ergebnisse auf einen Turn zu beschränken, oder lass das Feld weg,
um Elemente aus dem gesamten Thread seitenweise abzurufen. Der aktive Thread-Speicher muss die
Paginierung von Elementen unterstützen. Andernfalls gibt der Server einen Fehler wegen einer nicht unterstützten Methode zurück.

### Threads auflisten (mit Paginierung und Filtern)

Mit `thread/list` kannst du eine Verlaufsansicht darstellen. Standardmäßig werden die Ergebnisse nach `createdAt` sortiert, wobei die neuesten zuerst stehen. Filter werden vor der Paginierung angewendet. Übergib eine beliebige Kombination der folgenden Felder:

- `cursor`: opake Zeichenfolge aus einer vorherigen Antwort. Lass das Feld für die erste Seite weg.
- `limit`: Wenn das Feld nicht gesetzt ist, verwendet der Server standardmäßig eine angemessene Seitengröße.
- `sortKey`: `created_at` (Standard), `updated_at` oder `recency_at`.
- `sortDirection`: `desc` (Standard) oder `asc`.
- `modelProviders`: Beschränkt die Ergebnisse auf bestimmte Anbieter. Ist der Wert nicht gesetzt, null oder ein leeres Array, werden alle Anbieter berücksichtigt.
- `sourceKinds`: Beschränkt die Ergebnisse auf bestimmte Thread-Quellen. Wenn das Feld fehlt oder auf `[]` gesetzt wird, berücksichtigt der Server standardmäßig nur interaktive Quellen: `cli` und `vscode`.
- `archived`: Bei `true` werden nur archivierte Threads aufgelistet. Bei `false` oder wenn das Feld fehlt, werden nicht archivierte Threads aufgelistet (Standard).
- `isPinned`: Wenn angegeben, werden nur Threads mit dem entsprechenden gespeicherten Pin-Status zurückgegeben. Lass das Feld weg, um angepinnte und nicht angepinnte Threads zurückzugeben.
- `cwd`: Beschränkt die Ergebnisse auf Threads, deren Sitzung aktuell genau diesen Pfad oder einen der Pfade in einem Array als Arbeitsverzeichnis verwendet. Relative Pfade werden ausgehend vom Arbeitsverzeichnis des App Server-Prozesses aufgelöst.
- `useStateDbOnly`: Gibt bei `true` Ergebnisse aus der Zustandsdatenbank zurück, ohne die JSONL-Protokolle der Threads zur Reparatur von Metadaten zu durchsuchen. Lass das Feld weg oder übergib `false`, damit wie üblich die Protokolle durchsucht und die Metadaten repariert werden.
- `searchTerm`: Beschränkt die Ergebnisse auf Threads, deren extrahierter Titel dieses Textfragment unter Beachtung der Groß- und Kleinschreibung enthält.
- `parentThreadId`: Beschränkt die Ergebnisse auf die direkt untergeordneten Threads des angegebenen übergeordneten Threads. Dieser Filter ist experimentell und erfordert `capabilities.experimentalApi = true`.
- `ancestorThreadId`: Beschränkt die Ergebnisse auf untergeordnete Threads, die direkt oder indirekt vom angegebenen Thread erzeugt wurden, unabhängig von ihrer Tiefe in der Hierarchie. Dieser Filter ist experimentell und erfordert `capabilities.experimentalApi = true`. Kombiniere ihn nicht mit `parentThreadId`.

`sourceKinds` akzeptiert folgende Werte:

- `cli`
- `vscode`
- `exec`
- `appServer`
- `subAgent`
- `subAgentReview`
- `subAgentCompact`
- `subAgentThreadSpawn`
- `subAgentOther`
- `unknown`

Beispiel:

```json
{ "method": "thread/list", "id": 20, "params": {
  "cursor": null,
  "limit": 25,
  "sortKey": "created_at"
} }
{ "id": 20, "result": {
  "data": [
    { "id": "thr_a", "preview": "Create a TUI", "ephemeral": false, "isPinned": true, "modelProvider": "openai", "createdAt": 1730831111, "updatedAt": 1730831111, "name": "TUI prototype", "status": { "type": "notLoaded" } },
    { "id": "thr_b", "preview": "Fix tests", "ephemeral": false, "isPinned": false, "modelProvider": "openai", "createdAt": 1730750000, "updatedAt": 1730750000, "status": { "type": "notLoaded" } }
  ],
  "nextCursor": "opaque-token-or-null"
} }

Wenn `nextCursor` den Wert `null` hat, hast du die letzte Seite erreicht.

### Metadaten eines gespeicherten Threads aktualisieren

Verwende `thread/metadata/update`, um gespeicherte Thread-Metadaten zu aktualisieren, ohne den
Thread fortzusetzen. Setze `isPinned`, um den Thread anzupinnen oder den Pin zu entfernen, oder aktualisiere `gitInfo`, um
gespeicherte Git-Metadaten zu ändern. Nicht angegebene Felder bleiben unverändert. Ein explizites `null` löscht einen
gespeicherten Git-Metadatenwert.

```json
{ "method": "thread/metadata/update", "id": 21, "params": {
  "threadId": "thr_123",
  "isPinned": true,
  "gitInfo": { "branch": "feature/sidebar-pr" }
} }
{ "id": 21, "result": {
  "thread": {
    "id": "thr_123",
    "isPinned": true,
    "gitInfo": { "sha": null, "branch": "feature/sidebar-pr", "originUrl": null }
  }
} }

### Statusänderungen eines Threads verfolgen

`thread/status/changed` wird immer dann ausgegeben, wenn sich der Laufzeitstatus eines geladenen Threads ändert. Die Nutzlast enthält `threadId` und den neuen Wert für `status`.

```json
{
  "method": "thread/status/changed",
  "params": {
    "threadId": "thr_123",
    "status": { "type": "active", "activeFlags": ["waitingOnApproval"] }
  }
}

### Geladene Threads auflisten

`thread/loaded/list` gibt die IDs der aktuell im Arbeitsspeicher geladenen Threads zurück.

```json
{ "method": "thread/loaded/list", "id": 21 }
{ "id": 21, "result": { "data": ["thr_123", "thr_456"] } }

### Abonnement eines geladenen Threads beenden

`thread/unsubscribe` hebt für die aktuelle Verbindung das Abonnement eines Threads auf. Die Antwort enthält einen der folgenden Statuswerte:

- `unsubscribed`, wenn die Verbindung den Thread abonniert hatte und dieses Abonnement nun entfernt wurde.
- `notSubscribed`, wenn die Verbindung diesen Thread nicht abonniert hatte.
- `notLoaded`, wenn der Thread nicht geladen ist.

Wenn dies die letzte abonnierende Verbindung war, hält der Server den Thread im Arbeitsspeicher, bis 30 Minuten lang weder ein Abonnement besteht noch Aktivitäten im Thread stattfinden. Nach Ablauf dieser Frist entfernt App Server den Thread aus dem Arbeitsspeicher und sendet eine Benachrichtigung vom Typ `thread/status/changed` für den Übergang zu `notLoaded` sowie eine vom Typ `thread/closed`.

```json
{ "method": "thread/unsubscribe", "id": 22, "params": { "threadId": "thr_123" } }
{ "id": 22, "result": { "status": "unsubscribed" } }

Wenn später die Frist für den Thread abläuft:

```json
{ "method": "thread/status/changed", "params": {
    "threadId": "thr_123",
    "status": { "type": "notLoaded" }
} }
{ "method": "thread/closed", "params": { "threadId": "thr_123" } }

### Thread archivieren

Verwende `thread/archive`, um das gespeicherte Thread-Protokoll (als JSONL-Datei auf dem Datenträger gespeichert) in das Verzeichnis archivierter Sitzungen zu verschieben. Beim Archivieren eines Threads wird außerdem versucht, die von diesem Thread direkt oder indirekt erzeugten untergeordneten Threads zu archivieren, sofern sie noch nicht archiviert sind.

```json
{ "method": "thread/archive", "id": 22, "params": { "threadId": "thr_b" } }
{ "id": 22, "result": {} }
{ "method": "thread/archived", "params": { "threadId": "thr_b" } }
{ "method": "thread/archived", "params": { "threadId": "thr_child" } }

Archivierte Threads erscheinen bei künftigen Aufrufen von `thread/list` nur, wenn du `archived: true` übergibst. Der Server gibt für jeden tatsächlich archivierten Thread eine Benachrichtigung vom Typ `thread/archived` aus. Wenn einer der erzeugten untergeordneten Threads nicht archiviert werden kann, kann die Anfrage dennoch erfolgreich sein, ohne dass für diesen Thread eine Archivierungsbenachrichtigung ausgegeben wird.

### Thread löschen

Verwende `thread/delete`, um einen gespeicherten aktiven oder archivierten Thread
und die von ihm direkt oder indirekt erzeugten untergeordneten Threads dauerhaft zu löschen. Der Server entfernt vorhandene Rollout-Dateien und
zugehörige Metadaten, bevor er Erfolg meldet. Fehlende Rollout-Dateien gelten
als bereits gelöscht. Temporäre Root-Threads können nicht gelöscht werden.

```json
{ "method": "thread/delete", "id": 23, "params": { "threadId": "thr_b" } }
{ "id": 23, "result": {} }
{ "method": "thread/deleted", "params": { "threadId": "thr_b" } }
{ "method": "thread/deleted", "params": { "threadId": "thr_child" } }

### Thread aus dem Archiv wiederherstellen

Verwende `thread/unarchive`, um den Rollout eines archivierten Threads zurück in das Verzeichnis der aktiven Sitzungen zu verschieben.

```json
{ "method": "thread/unarchive", "id": 24, "params": { "threadId": "thr_b" } }
{ "id": 24, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes" } } }
{ "method": "thread/unarchived", "params": { "threadId": "thr_b" } }

### Compaction (Kontextverdichtung) eines Threads auslösen

Verwende `thread/compact/start`, um für einen Thread manuell eine Compaction (Kontextverdichtung) des Verlaufs auszulösen. Die Anfrage gibt sofort `{}` zurück.

App Server meldet den Fortschritt über die üblichen Benachrichtigungen vom Typ `turn/*` und `item/*` für dieselbe `threadId`. Dazu gehören die Ereignisse im Lebenszyklus eines `contextCompaction`-Elements (`item/started`, dann `item/completed`).

```json
{ "method": "thread/compact/start", "id": 25, "params": { "threadId": "thr_b" } }
{ "id": 25, "result": {} }

### Shell-Befehl für einen Thread ausführen

Verwende `thread/shellCommand` für von Nutzenden gestartete Shell-Befehle, die zu einem Thread gehören. Die Anfrage gibt sofort `{}` zurück, während der Fortschritt über die standardmäßigen Benachrichtigungen `turn/*` und `item/*` gestreamt wird.

Diese API wird außerhalb der Sandbox mit Vollzugriff ausgeführt und übernimmt die Sandbox-Richtlinie des Threads nicht. Clients sollten sie nur für Befehle bereitstellen, die ausdrücklich von Nutzenden gestartet wurden.

Wenn der Thread bereits einen aktiven Turn hat, wird der Befehl als zusätzliche Aktion in diesem Turn ausgeführt und seine formatierte Ausgabe in dessen Nachrichtenstream eingespeist. Ist der Thread inaktiv, startet app-server einen eigenständigen Turn für den Shell-Befehl.

Setze `timeoutMs`, um die Ausführungszeit in Millisekunden zu begrenzen. Lässt du den Wert weg oder übergibst
`null`, gilt der Standardwert von einer Stunde. `0` fordert einen sofortigen Timeout an; negative
Werte werden abgelehnt. Der Timeout verzögert die sofortige RPC-Bestätigung nicht.

```json
{ "method": "thread/shellCommand", "id": 26, "params": { "threadId": "thr_b", "command": "git status --short", "timeoutMs": 10000 } }
{ "id": 26, "result": {} }

### Hintergrundterminals bereinigen

Verwende `thread/backgroundTerminals/clean`, um alle laufenden Hintergrundterminals eines Threads zu beenden. Diese Methode ist experimentell und erfordert `capabilities.experimentalApi = true`.

```json
{ "method": "thread/backgroundTerminals/clean", "id": 27, "params": { "threadId": "thr_b" } }
{ "id": 27, "result": {} }

Verwende `thread/backgroundTerminals/list`, um laufende Hintergrundterminals
eines geladenen Threads zu prüfen. Die Anfrage unterstützt die standardmäßige Paginierung mit `cursor` und `limit`.
Der zurückgegebene Wert `processId` ist die Prozess-ID von app-server. Diese
Methode ist experimentell und erfordert `capabilities.experimentalApi = true`:

```json
{ "method": "thread/backgroundTerminals/list", "id": 28, "params": { "threadId": "thr_b" } }
{ "id": 28, "result": { "data": [
  {
    "itemId": "item_456",
    "processId": "42",
    "command": "python3 -m http.server",
    "cwd": "/workspace",
    "osPid": null,
    "cpuPercent": null,
    "rssKb": null
  }
], "nextCursor": null } }

Rufe `thread/backgroundTerminals/terminate` mit der entsprechenden `processId` auf, um ein
Hintergrundterminal zu beenden. Diese Methode ist experimentell und erfordert
`capabilities.experimentalApi = true`:

```json
{ "method": "thread/backgroundTerminals/terminate", "id": 29, "params": { "threadId": "thr_b", "processId": "42" } }
{ "id": 29, "result": { "terminated": true } }

### Letzte Turns rückgängig machen

`thread/rollback` ist veraltet und wird entfernt. Die Methode entfernt die letzten
`numTurns` Einträge aus dem Kontext im Arbeitsspeicher und speichert eine Rollback-Markierung im
Rollout-Protokoll. Das zurückgegebene `thread`-Objekt enthält in `turns` den Stand nach dem
Rollback.

```json
{ "method": "thread/rollback", "id": 30, "params": { "threadId": "thr_b", "numTurns": 1 } }
{ "id": 30, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }

## Turns

Das Feld `input` akzeptiert eine Liste von Elementen:

- `{ "type": "text", "text": "Explain this diff" }`
- `{ "type": "image", "url": "https://.../design.png" }`
- `{ "type": "localImage", "path": "/tmp/screenshot.png" }`

Du kannst die Konfiguration für jeden Turn überschreiben (Modell, Reasoning-Aufwand, Persönlichkeit, `cwd`, Sandbox-Richtlinie, Zusammenfassung). Wenn du diese Einstellungen angibst, werden sie zu den Standardwerten für spätere Turns desselben Threads. `outputSchema` gilt nur für den aktuellen Turn. Setze für `sandboxPolicy.type = "externalSandbox"` den Wert `networkAccess` auf `restricted` oder `enabled`; bei `workspaceWrite` bleibt `networkAccess` ein boolescher Wert.

Bei `turn/start.collaborationMode` bedeutet `settings.developer_instructions: null` „integrierte Anweisungen für den ausgewählten Modus verwenden“, statt die Anweisungen für den Modus zu löschen.

### Lesezugriff in der Sandbox (`ReadOnlyAccess`)

`sandboxPolicy` unterstützt eine explizite Steuerung des Lesezugriffs:

- `readOnly`: optionales Feld `access` (standardmäßig `{ "type": "fullAccess" }`; alternativ auf bestimmte Stammverzeichnisse beschränkt).
- `workspaceWrite`: optionales Feld `readOnlyAccess` (standardmäßig `{ "type": "fullAccess" }`; alternativ auf bestimmte Stammverzeichnisse beschränkt).

Struktur für eingeschränkten Lesezugriff:

```json
{
  "type": "restricted",
  "includePlatformDefaults": true,
  "readableRoots": ["/Users/me/shared-read-only"]
}

Unter macOS fügt `includePlatformDefaults: true` eine ausgewählte plattformspezifische Seatbelt-Standardrichtlinie für Sitzungen mit eingeschränktem Lesezugriff hinzu. Das verbessert die Kompatibilität mit Tools, ohne den Zugriff auf das gesamte Verzeichnis `/System` pauschal freizugeben.

Beispiele:

```json
{ "type": "readOnly", "access": { "type": "fullAccess" } }

```json
{
  "type": "workspaceWrite",
  "writableRoots": ["/Users/me/project"],
  "readOnlyAccess": {
    "type": "restricted",
    "includePlatformDefaults": true,
    "readableRoots": ["/Users/me/shared-read-only"]
  },
  "networkAccess": false
}

### Turn starten

```json
{ "method": "turn/start", "id": 30, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Run tests" } ],
  "cwd": "/Users/me/project",
  "approvalPolicy": "unlessTrusted",
  "sandboxPolicy": {
    "type": "workspaceWrite",
    "writableRoots": ["/Users/me/project"],
    "networkAccess": true
  },
  "model": "gpt-5.6-terra",
  "effort": "medium",
  "summary": "concise",
  "personality": "friendly",
  "outputSchema": {
    "type": "object",
    "properties": { "answer": { "type": "string" } },
    "required": ["answer"],
    "additionalProperties": false
  }
} }
{ "id": 30, "result": { "turn": { "id": "turn_456", "status": "inProgress", "items": [], "error": null } } }

Um einen Turn mit der Ausgabe eines Tools zu starten, das dein Client ausgeführt hat, übergib `toolOutput`
mit einem nicht leeren Wert für `name`, optional einem Wert für `namespace` und `output` als Zeichenfolge oder
Array von Inhaltselementen. Setze `input` auf ein leeres Array; du kannst
`toolOutput` nicht mit nicht leeren Nutzereingaben kombinieren.

```json
{
  "method": "turn/start",
  "id": 31,
  "params": {
    "threadId": "thr_123",
    "input": [],
    "toolOutput": {
      "name": "run_tests",
      "namespace": null,
      "output": "All 42 tests passed."
    }
  }
}

Die Ausgabe bleibt im Gespräch als Tool-Ausgabe erhalten und erscheint in Benachrichtigungen und im gespeicherten Verlauf als Element vom Typ
`functionCallOutput`. Wenn bereits ein regulärer
Turn aktiv ist, stellt Codex die Ausgabe für diesen Turn in die Warteschlange.

### Elemente in einen Thread einfügen

Verwende `thread/inject_items`, um vorgefertigte Elemente der Responses API an den Prompt-Verlauf eines geladenen Threads anzuhängen, ohne einen Turn für eine Nutzereingabe zu starten. Diese Elemente werden dauerhaft im Rollout gespeichert und in nachfolgende Modellanfragen aufgenommen.

```json
{ "method": "thread/inject_items", "id": 31, "params": {
  "threadId": "thr_123",
  "items": [
    {
      "type": "message",
      "role": "assistant",
      "content": [{ "type": "output_text", "text": "Previously computed context." }]
    }
  ]
} }
{ "id": 31, "result": {} }

### Aktiven Turn steuern

Verwende `turn/steer`, um weitere Nutzereingaben an den aktuell laufenden Turn anzuhängen.

- Gib `expectedTurnId` an; der Wert muss mit der ID des aktiven Turns übereinstimmen.
- Die Anfrage schlägt fehl, wenn im Thread kein aktiver Turn vorhanden ist.
- `turn/steer` sendet keine neue Benachrichtigung vom Typ `turn/started`.
- `turn/steer` akzeptiert keine Überschreibungen auf Turn-Ebene (`model`, `cwd`, `sandboxPolicy` oder `outputSchema`).

```json
{ "method": "turn/steer", "id": 32, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Actually focus on failing tests first." } ],
  "expectedTurnId": "turn_456"
} }
{ "id": 32, "result": { "turnId": "turn_456" } }

### Turn starten (Skill aufrufen)

Rufe einen Skill explizit auf, indem du `$<skill-name>` in die Texteingabe einfügst und zusätzlich ein Eingabeelement vom Typ `skill` hinzufügst.

```json
{ "method": "turn/start", "id": 33, "params": {
  "threadId": "thr_123",
  "input": [
    { "type": "text", "text": "$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage." },
    { "type": "skill", "name": "skill-creator", "path": "/Users/me/.codex/skills/skill-creator/SKILL.md" }
  ]
} }
{ "id": 33, "result": { "turn": { "id": "turn_457", "status": "inProgress", "items": [], "error": null } } }

### Turn unterbrechen

```json
{ "method": "turn/interrupt", "id": 31, "params": { "threadId": "thr_123", "turnId": "turn_456" } }
{ "id": 31, "result": {} }

Bei Erfolg endet der Turn mit `status: "interrupted"`.

## Review

`review/start` startet den Codex-Reviewer für einen Thread und streamt Review-Elemente. Mögliche Ziele sind:

- `uncommittedChanges`
- `baseBranch` (Diff gegenüber einem Branch)
- `commit` (einen bestimmten Commit überprüfen)
- `custom` (frei formulierte Anweisungen)

Verwende `delivery: "inline"` (Standard), um das Review im vorhandenen Thread auszuführen, oder `delivery: "detached"`, um einen neuen Review-Thread zu forken.

Beispiel für Anfrage und Antwort:

```json
{ "method": "review/start", "id": 40, "params": {
  "threadId": "thr_123",
  "delivery": "inline",
  "target": { "type": "commit", "sha": "1234567deadbeef", "title": "Polish tui colors" }
} }
{ "id": 40, "result": {
  "turn": {
    "id": "turn_900",
    "status": "inProgress",
    "items": [
      { "type": "userMessage", "id": "turn_900", "content": [ { "type": "text", "text": "Review commit 1234567: Polish tui colors" } ] }
    ],
    "error": null
  },
  "reviewThreadId": "thr_123"
} }

Verwende für ein separates Review `"delivery": "detached"`. Die Antwort hat dieselbe Struktur, allerdings enthält `reviewThreadId` die ID des neuen Review-Threads und unterscheidet sich damit von der ursprünglichen `threadId`. Der Server sendet außerdem eine Benachrichtigung vom Typ `thread/started` für den neuen Thread, bevor er den Review-Turn streamt.

Codex streamt zunächst die übliche Benachrichtigung vom Typ `turn/started` und anschließend eine Benachrichtigung vom Typ `item/started` mit einem Element vom Typ `enteredReviewMode`:

```json
{
  "method": "item/started",
  "params": {
    "item": {
      "type": "enteredReviewMode",
      "id": "turn_900",
      "review": "current changes"
    }
  }
}

Sobald der Reviewer fertig ist, sendet der Server die Benachrichtigungen `item/started` und `item/completed`, die ein Element vom Typ `exitedReviewMode` mit dem endgültigen Review-Text enthalten:

```json
{
  "method": "item/completed",
  "params": {
    "item": {
      "type": "exitedReviewMode",
      "id": "turn_900",
      "review": "Looks solid overall..."
    }
  }
}

Verwende diese Benachrichtigung, um die Ausgabe des Reviewers in deinem Client darzustellen.

## Prozessausführung

`process/*` ist eine experimentelle API zur expliziten Prozesssteuerung. Sie erfordert
`capabilities.experimentalApi = true` und wird außerhalb der Sandbox von Codex ausgeführt. Verwende sie
nur, wenn dein Client bewusst eine lokale Prozesssteuerung ohne
Sandbox bereitstellt.

Starte mit `process/spawn` einen Prozess und gib einen Wert für `processHandle` an. Verwende
dieses Handle anschließend in Anfragen, um Eingaben an stdin zu senden, die Größe zu ändern oder den Prozess zu beenden. Die Ausgabe wird über Benachrichtigungen vom Typ
`process/outputDelta` gestreamt; der Abschluss wird über
`process/exited` gemeldet.

```json
{ "method": "process/spawn", "id": 48, "params": {
  "command": ["python3", "-m", "pytest", "-q"],
  "processHandle": "pytest-1",
  "cwd": "/Users/me/project",
  "tty": true
} }
{ "id": 48, "result": {} }
{ "method": "process/outputDelta", "params": {
  "processHandle": "pytest-1",
  "stream": "stdout",
  "deltaBase64": "Li4u"
} }
{ "method": "process/exited", "params": {
  "processHandle": "pytest-1",
  "exitCode": 0
} }

Verwende `process/writeStdin` mit `deltaBase64`, `closeStdin` oder beiden, um
Eingaben zu senden. Verwende `process/resizePty` für Ereignisse zur Änderung der PTY-Größe und `process/kill`, um
einen laufenden Prozess zu beenden.

## Befehlsausführung

`command/exec` führt innerhalb der Server-Sandbox einen einzelnen Befehl (`argv`-Array) aus, ohne einen Thread zu erstellen.

```json
{ "method": "command/exec", "id": 50, "params": {
  "command": ["ls", "-la"],
  "cwd": "/Users/me/project",
  "sandboxPolicy": { "type": "workspaceWrite" },
  "timeoutMs": 10000
} }
{ "id": 50, "result": { "exitCode": 0, "stdout": "...", "stderr": "" } }

Verwende `sandboxPolicy.type = "externalSandbox"`, wenn du den Serverprozess bereits in einer Sandbox ausführst und Codex seine eigenen Sandbox-Regeln nicht zusätzlich durchsetzen soll. Setze im externen Sandbox-Modus `networkAccess` auf `restricted` (Standard) oder `enabled`. Verwende für `readOnly` und `workspaceWrite` dieselbe oben gezeigte optionale Struktur mit `access` beziehungsweise `readOnlyAccess`.

Hinweise:

- Der Server lehnt leere `command`-Arrays ab.
- `sandboxPolicy` akzeptiert dieselbe Struktur wie `turn/start` (zum Beispiel `dangerFullAccess`, `readOnly`, `workspaceWrite`, `externalSandbox`).
- Wird `timeoutMs` nicht angegeben, gilt der Standardwert des Servers.
- Setze `tty: true` für PTY-basierte Sitzungen. Verwende `processId`, wenn du anschließend `command/exec/write`, `command/exec/resize` oder `command/exec/terminate` aufrufen möchtest.
- Setze `streamStdoutStderr: true`, um während der Befehlsausführung Benachrichtigungen vom Typ `command/exec/outputDelta` zu erhalten.

### Admin-Anforderungen auslesen (`configRequirements/read`)

Verwende `configRequirements/read`, um die wirksamen Admin-Anforderungen zu prüfen, die aus `requirements.toml` und/oder MDM geladen wurden.

```json
{ "method": "configRequirements/read", "id": 52, "params": {} }
{ "id": 52, "result": {
  "requirements": {
    "allowedApprovalPolicies": ["onRequest", "unlessTrusted"],
    "allowedSandboxModes": ["readOnly", "workspaceWrite"],
    "featureRequirements": {
      "personality": true,
      "unified_exec": false
    },
    "network": {
      "enabled": true,
      "allowedDomains": ["api.openai.com"],
      "allowUnixSockets": ["/tmp/example.sock"],
      "dangerouslyAllowAllUnixSockets": false
    }
  }
} }

`result.requirements` ist `null`, wenn keine Anforderungen konfiguriert sind. Details zu unterstützten Schlüsseln und Werten findest du in der Dokumentation zu [`requirements.toml`](/de-DE/codex/config-file/config-reference#requirementstoml).

### Windows-Sandbox-Setup (`windowsSandbox/setupStart`)

Eigene Windows-Clients können das Setup der Sandbox asynchron starten, statt auf den Abschluss der Prüfungen beim Start zu warten.

```json
{ "method": "windowsSandbox/setupStart", "id": 53, "params": { "mode": "elevated" } }
{ "id": 53, "result": { "started": true } }

Der App Server startet das Setup im Hintergrund und gibt später eine Benachrichtigung über den Abschluss aus:

```json
{
  "method": "windowsSandbox/setupCompleted",
  "params": { "mode": "elevated", "success": true, "error": null }
}

Modi:

- `elevated`: den Setup-Ablauf für die Windows-Sandbox mit erhöhten Rechten ausführen.
- `unelevated`: den bisherigen Ablauf für Setup und Vorabprüfung ausführen.

## Dateisystem

Die v2-Dateisystem-APIs arbeiten mit absoluten Pfaden. Verwende `fs/watch`, wenn ein Client nach Änderungen an einer Datei oder einem Verzeichnis seinen UI-Zustand als ungültig markieren muss.

```json
{ "method": "fs/watch", "id": 54, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "path": "/Users/me/project/.git/HEAD"
} }
{ "id": 54, "result": { "path": "/Users/me/project/.git/HEAD" } }
{ "method": "fs/changed", "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "changedPaths": ["/Users/me/project/.git/HEAD"]
} }
{ "method": "fs/unwatch", "id": 55, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1"
} }
{ "id": 55, "result": {} }

Beim Überwachen einer Datei wird für ihren Pfad `fs/changed` ausgegeben, auch bei Aktualisierungen durch Ersetzen oder Umbenennen.

## Ereignisse

Ereignisbenachrichtigungen bilden den vom Server initiierten Stream für die Lebenszyklen von Threads und Turns sowie die darin enthaltenen Items. Lies nach dem Starten oder Fortsetzen eines Threads den aktiven Transportstream weiter aus, um Benachrichtigungen für `thread/started`, `thread/archived`, `thread/unarchived`, `thread/closed`, `thread/status/changed`, `turn/*`, `item/*` und `serverRequest/resolved` zu empfangen.

### Benachrichtigungen unterdrücken

Clients können pro Verbindung bestimmte Benachrichtigungen unterdrücken, indem sie in `initialize.params.capabilities.optOutNotificationMethods` die exakten Methodennamen senden.

- Nur exakte Übereinstimmungen: `item/agentMessage/delta` unterdrückt ausschließlich diese Methode.
- Unbekannte Methodennamen werden ignoriert.
- Gilt für die aktuellen Benachrichtigungen `thread/*`, `turn/*` und `item/*` sowie für verwandte v2-Benachrichtigungen.
- Gilt nicht für Anfragen, Antworten oder Fehler.

### Ereignisse der unscharfen Dateisuche (experimentell)

Die Sitzungs-API der unscharfen Dateisuche gibt für jede Abfrage Benachrichtigungen aus:

- `fuzzyFileSearch/sessionUpdated`: `{ sessionId, query, files }` mit den aktuellen Treffern für die aktive Abfrage.
- `fuzzyFileSearch/sessionCompleted`: `{ sessionId }`, sobald die Indizierung und der Abgleich für diese Abfrage abgeschlossen sind.

### Warnereignisse

- `configWarning`: `{ summary, details?, path?, range? }` bei behebbaren
  Konfigurations- oder Initialisierungsproblemen.
- `warning`: `{ threadId?, message }` bei Laufzeitwarnungen, die nicht zum Abbruch führen.

### Setup-Ereignisse der Windows-Sandbox

- `windowsSandbox/setupCompleted`: `{ mode, success, error }` wird ausgegeben, sobald eine Anfrage mit `windowsSandbox/setupStart` abgeschlossen ist.

### Turn-Ereignisse

- `turn/started`: `{ turn }` mit der Turn-ID, einem leeren `items`-Array und `status: "inProgress"`.
- `turn/completed`: `{ turn }`, wobei `turn.status` den Wert `completed`, `interrupted` oder `failed` hat. Bei Fehlern ist `{ error: { message, codexErrorInfo?, additionalDetails? } }` enthalten.
- `turn/diff/updated`: `{ threadId, turnId, diff }` mit dem neuesten zusammengefassten Diff im Unified-Format für alle Dateiänderungen im Turn.
- `turn/plan/updated`: `{ turnId, explanation?, plan }`, sobald der Agent seinen Plan mitteilt oder ändert. Jeder Eintrag in `plan` hat die Form `{ step, status }`, wobei `status` den Wert `pending`, `inProgress` oder `completed` hat.
- `hook/started` und `hook/completed`: `{ threadId, turnId?, run }` beim Start eines synchronen Lebenszyklus-Hooks und sobald die abschließende Zusammenfassung seiner Ausführung vorliegt. Für asynchrone Hooks werden diese Benachrichtigungen nicht ausgegeben.
- `model/safetyBuffering/updated`: `{ threadId, turnId, model, useCases, reasons, showBufferingUi, fasterModel }`, wenn eine Antwort vorübergehend aus Sicherheitsgründen gepuffert wird.
- `model/rerouted`: `{ threadId, turnId, fromModel, toModel, reason }`, wenn der Dienst eine Anfrage an ein anderes Modell weiterleitet.
- `model/verification`: `{ threadId, turnId, verifications }`, wenn der Dienst eine zusätzliche Verifizierung des Kontos verlangt.
- `thread/tokenUsage/updated`: aktualisierte Nutzungsdaten für den aktiven Thread.

`turn/diff/updated` und `turn/plan/updated` enthalten derzeit leere `items`-Arrays, selbst wenn Item-Ereignisse gestreamt werden. Verwende Benachrichtigungen vom Typ `item/*` als maßgebliche Quelle für die Items eines Turns.

### Items

`ThreadItem` ist der diskriminierte Union-Typ, der in Turn-Antworten und Benachrichtigungen vom Typ `item/*` enthalten ist. Zu den gängigen Item-Typen gehören:

- `userMessage`: `{id, content}`, wobei `content` eine Liste mit Nutzereingaben (`text`, `image` oder `localImage`) ist.
- `functionCallOutput`: `{id, name, namespace, output}` für eigenständige Tool-Ausgaben, die über `turn/start.toolOutput` bereitgestellt werden. `namespace` kann `null` sein.
- `agentMessage`: `{id, text, phase?}` enthält die bislang zusammengeführte Antwort des Agenten. Sofern vorhanden, verwendet `phase` die Werte des Übertragungsformats der Responses API (`commentary`, `final_answer`).
- `plan`: `{id, text}` enthält den im Planmodus vorgeschlagenen Plantext. Betrachte das abschließende Item vom Typ `plan` aus `item/completed` als maßgeblich.
- `reasoning`: `{id, summary, content}`. `summary` enthält gestreamte Zusammenfassungen der Modellüberlegungen und `content` die unverarbeiteten Blöcke dieser Überlegungen.
- `commandExecution`: `{id, command, cwd, status, commandActions, aggregatedOutput?, exitCode?, durationMs?}`.
- `fileChange`: `{id, changes, status}` beschreibt vorgeschlagene Änderungen; `changes` listet Einträge der Form `{path, kind, diff}` auf.
- `mcpToolCall`: `{id, server, tool, status, arguments, appContext?, pluginId?, result?, error?}`. Bei vertrauenswürdigen MCP-Apps kann `appContext` die Felder `connectorId`, `linkId`, `resourceUri`, `appName`, `templateId` und den stabilen Wert `actionName` des Konnektors enthalten. Bei älteren gespeicherten Items können neuere Metadaten fehlen. Verwende `appContext.resourceUri` anstelle des veralteten Felds `mcpAppResourceUri` auf oberster Ebene.
- `dynamicToolCall`: `{id, tool, arguments, status, contentItems?, success?, durationMs?}` für dynamische Tool-Aufrufe, die der Client ausführt.
- `collabToolCall`: `{id, tool, status, senderThreadId, receiverThreadId?, newThreadId?, prompt?, agentStatus?}`.
- `webSearch`: `{id, query, action?}` für vom Agenten initiierte Anfragen an die Websuche.
- `imageView`: `{id, path}` wird ausgegeben, wenn der Agent das Tool zur Bildanzeige aufruft.
- `enteredReviewMode`: `{id, review}` wird gesendet, wenn der Review-Agent startet.
- `exitedReviewMode`: `{id, review}` wird ausgegeben, wenn der Review-Agent seine Arbeit abschließt.
- `contextCompaction`: `{id}` wird ausgegeben, wenn Codex den Gesprächsverlauf verdichtet.

Bei `webSearch.action` kann das Feld `type` der Aktion den Wert `search` (`query?`, `queries?`), `openPage` (`url?`) oder `findInPage` (`url?`, `pattern?`) haben.

Der App Server kennzeichnet die bisherige Benachrichtigung `thread/compacted` als veraltet. Verwende stattdessen das Item `contextCompaction`.

Alle Items geben dieselben zwei Lebenszyklusereignisse aus:

- `item/started`: gibt zu Beginn einer neuen Arbeitseinheit das vollständige `item` aus. Der Wert von `item.id` entspricht dem in Deltas verwendeten Wert von `itemId`.
- `item/completed`: sendet nach Abschluss der Arbeit das endgültige `item`. Betrachte es als maßgeblichen Zustand.

### Item-Deltas

- `item/agentMessage/delta`: hängt gestreamten Text an die Agentennachricht an.
- `item/plan/delta`: streamt vorgeschlagenen Plantext. Das endgültige Item vom Typ `plan` entspricht möglicherweise nicht exakt den verketteten Deltas.
- `item/reasoning/summaryTextDelta`: streamt lesbare Zusammenfassungen der Modellüberlegungen. `summaryIndex` wird erhöht, sobald ein neuer Abschnitt der Zusammenfassung beginnt.
- `item/reasoning/summaryPartAdded`: markiert den Übergang zwischen Abschnitten der Zusammenfassung der Modellüberlegungen.
- `item/reasoning/textDelta`: streamt den unverarbeiteten Text der Modellüberlegungen (sofern das Modell dies unterstützt).
- `item/commandExecution/outputDelta`: streamt stdout/stderr für einen Befehl. Hänge die Deltas der Reihe nach an.
- `item/fileChange/outputDelta`: veraltete Kompatibilitätsbenachrichtigung für die frühere Textausgabe von `apply_patch`. Aktuelle Versionen des App Server geben sie nicht mehr aus. Verwende stattdessen Elemente vom Typ `fileChange` und `turn/diff/updated`.

## Fehler

Wenn ein Turn fehlschlägt, gibt der Server ein Ereignis vom Typ `error` mit `{ error: { message, codexErrorInfo?, additionalDetails? } }` aus und beendet den Turn anschließend mit `status: "failed"`. Wenn ein HTTP-Status des Upstream-Dienstes verfügbar ist, steht er in `codexErrorInfo.httpStatusCode`.

Gängige Werte für `codexErrorInfo` sind:

- `ContextWindowExceeded`
- `UsageLimitExceeded`
- `HttpConnectionFailed` (4xx-/5xx-Fehler des Upstream-Dienstes)
- `ResponseStreamConnectionFailed`
- `ResponseStreamDisconnected`
- `ResponseTooManyFailedAttempts`
- `BadRequest`, `Unauthorized`, `SandboxError`, `InternalServerError`, `Other`

Wenn ein HTTP-Status des Upstream-Dienstes verfügbar ist, leitet der Server ihn im Feld `httpStatusCode` der entsprechenden Variante von `codexErrorInfo` weiter.

## Genehmigungen

Je nach Codex-Einstellungen können die Ausführung von Befehlen und Änderungen an Dateien eine Genehmigung erfordern. Der App Server sendet dazu von sich aus eine JSON-RPC-Anfrage an den Client. Der Client antwortet mit einer Payload, die die Entscheidung enthält.

- Mögliche Entscheidungen für die Befehlsausführung: `accept`, `acceptForSession`, `decline`, `cancel` oder `{ "acceptWithExecpolicyAmendment": { "execpolicy_amendment": ["cmd", "..."] } }`.
- Mögliche Entscheidungen für Dateiänderungen: `accept`, `acceptForSession`, `decline`, `cancel`.

- Anfragen enthalten `threadId` und `turnId`. Verwende sie, um den UI-Zustand auf die aktive Unterhaltung zu beschränken.
- Der Server setzt den Vorgang fort oder lehnt ihn ab und beendet das Element mit `item/completed`.

### Genehmigungen für die Befehlsausführung

Reihenfolge der Nachrichten:

1. `item/started` zeigt das ausstehende Element vom Typ `commandExecution` mit `command`, `cwd` und weiteren Feldern.
2. `item/commandExecution/requestApproval` enthält `itemId`, `threadId`, `turnId` sowie die optionalen Felder `reason`, `command`, `cwd`, `commandActions`, `proposedExecpolicyAmendment`, `networkApprovalContext` und `availableDecisions`. Wenn `initialize.params.capabilities.experimentalApi = true` gilt, kann die Payload zusätzlich das experimentelle Feld `additionalPermissions` enthalten, das den angeforderten Sandbox-Zugriff pro Befehl beschreibt. Alle Dateisystempfade in `additionalPermissions` werden als absolute Pfade übertragen.
3. Der Client antwortet mit einer der oben genannten Entscheidungen zur Genehmigung der Befehlsausführung.
4. `serverRequest/resolved` bestätigt, dass die ausstehende Anfrage beantwortet oder entfernt wurde.
5. `item/completed` gibt das endgültige Element vom Typ `commandExecution` mit `status: completed | failed | declined` zurück.

Wenn `networkApprovalContext` vorhanden ist, bezieht sich der Prompt auf verwalteten Netzwerkzugriff und nicht auf eine allgemeine Genehmigung für Shell-Befehle. Das aktuelle v2-Schema enthält für das Ziel die Felder `host` und `protocol`. Clients sollten einen netzwerkspezifischen Prompt anzeigen und nicht voraussetzen, dass `command` eine für Nutzende aussagekräftige Vorschau eines Shell-Befehls enthält.

Codex gruppiert gleichzeitige Prompts zur Genehmigung von Netzwerkzugriffen nach ihrem Ziel (`host`, Protokoll und Port). Daher kann der App Server einen einzigen Prompt senden, der mehrere Anfragen in der Warteschlange für dasselbe Ziel freigibt. Unterschiedliche Ports desselben Hosts werden getrennt behandelt.

### Genehmigungen für Dateiänderungen

Reihenfolge der Nachrichten:

1. `item/started` gibt ein Element vom Typ `fileChange` mit den vorgeschlagenen Änderungen in `changes` und `status: "inProgress"` aus.
2. `item/fileChange/requestApproval` enthält `itemId`, `threadId`, `turnId` sowie die optionalen Felder `reason` und `grantRoot`.
3. Der Client antwortet mit einer der oben genannten Entscheidungen zur Genehmigung von Dateiänderungen.
4. `serverRequest/resolved` bestätigt, dass die ausstehende Anfrage beantwortet oder entfernt wurde.
5. `item/completed` gibt das endgültige Element vom Typ `fileChange` mit `status: completed | failed | declined` zurück.

### `tool/requestUserInput`

Wenn der Client auf `item/tool/requestUserInput` antwortet, gibt der App Server `serverRequest/resolved` mit `{ threadId, requestId }` aus. Wird die ausstehende Anfrage durch den Start, Abschluss oder die Unterbrechung eines Turns entfernt, bevor der Client antwortet, gibt der Server für diese Bereinigung dieselbe Benachrichtigung aus.

Die Anfrageparameter enthalten `autoResolutionMs` als ganzzahliges Zeitlimit in Millisekunden oder
`null`. Ist ein Zeitlimit angegeben, können Host-Clients den Prompt nach Ablauf dieses
Intervalls automatisch abschließen, falls Nutzende nicht antworten.

### Berechtigungsanfragen

Das integrierte Tool `request_permissions` sendet
`item/permissions/requestApproval` mit `threadId`, `turnId`, `itemId`,
`environmentId`, `cwd`, optional `reason` sowie den angeforderten
Netzwerk- oder Dateisystemberechtigungen. Antworte mit `permissions`, das nur die gewährte Teilmenge enthält.
Setze `scope` auf `"session"`, um diese Berechtigungen für spätere Turns derselben
Sitzung zu speichern. Lasse das Feld weg oder verwende `"turn"`, wenn die Berechtigungen nur für einen Turn gelten sollen. Berechtigungen, die
nicht angefordert wurden, werden ignoriert.

### Elizitationsanfragen von MCP-Servern

Ein MCP-Server kann einen Turn mit `mcpServer/elicitation/request` unterbrechen. Die
Anfrage enthält `threadId`, optional `turnId`, `serverName` und eine der
folgenden Anfragestrukturen:

- `mode: "form"` oder `mode: "openai/form"`, jeweils mit `message` und
`requestedSchema`.
- `mode: "url"` mit `message`, `url` und `elicitationId`.

Antworte mit `action: "accept"` und den angeforderten Daten in `content` oder mit
`action: "decline"` beziehungsweise `"cancel"` und `content: null`. Anschließend gibt der App Server
`serverRequest/resolved` aus. Um die Variante `openai/form` zu erhalten, aktiviere sie mit
`initialize.params.capabilities.mcpServerOpenaiFormElicitation`.

### Dynamische Tool-Aufrufe (experimentell)

`dynamicTools` in `thread/start` und der zugehörige Anfrage- oder Antwortablauf über `item/tool/call` sind experimentelle APIs.

Die Namen dynamischer Tools und Namespaces müssen den Benennungsvorgaben der Responses API
entsprechen. Vermeide reservierte Namespace-Namen, die von integrierten Codex-Tools verwendet werden.

Wenn während eines Turns ein dynamisches Tool aufgerufen wird, gibt der App Server Folgendes aus:

1. `item/started` mit `item.type = "dynamicToolCall"`, `status = "inProgress"` sowie `tool` und `arguments`.
2. `item/tool/call` als Serveranfrage an den Client.
3. Die Antwort-Payload des Clients mit den zurückgegebenen Inhaltselementen.
4. `item/completed` mit `item.type = "dynamicToolCall"`, dem endgültigen Wert von `status` und gegebenenfalls zurückgegebenen Werten für `contentItems` oder `success`.

### Genehmigungen für MCP-Tool-Aufrufe (Apps)

Auch Tool-Aufrufe von Apps (Konnektoren) können eine Genehmigung erfordern. Wenn ein App-Tool-Aufruf Nebenwirkungen hat, kann der Server über `tool/requestUserInput` eine Genehmigung mit Optionen wie **Akzeptieren**, **Ablehnen** und **Abbrechen** anfordern. Tool-Annotationen, die auf destruktive Aktionen hinweisen, lösen immer eine Genehmigungsanfrage aus, auch wenn das Tool zusätzlich Hinweise auf geringere Berechtigungsanforderungen angibt. Wenn Nutzende die Anfrage ablehnen oder abbrechen, wird das zugehörige Element vom Typ `mcpToolCall` mit einem Fehler abgeschlossen, statt das Tool auszuführen.

## Skills

Rufe einen Skill auf, indem du `$<skill-name>` in die Texteingabe der nutzenden Person einfügst. Füge außerdem ein Eingabeelement vom Typ `skill` hinzu (empfohlen), damit der Server die vollständigen Skill-Anweisungen einfügt, statt die Auflösung des Namens dem Modell zu überlassen.

```json
{
  "method": "turn/start",
  "id": 101,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$skill-creator Add a new skill for triaging flaky CI."
      },
      {
        "type": "skill",
        "name": "skill-creator",
        "path": "/Users/me/.codex/skills/skill-creator/SKILL.md"
      }
    ]
  }
}

Wenn du das Element vom Typ `skill` weglässt, analysiert das Modell trotzdem die Markierung `$<skill-name>` und versucht, den Skill zu finden. Das kann die Latenz erhöhen.

Beispiel:

$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage.

Verwende `skills/list`, um verfügbare Skills abzurufen (optional auf `cwds` beschränkt, mit `forceReload`). Du kannst außerdem `perCwdExtraUserRoots` angeben, um zusätzliche absolute Pfade im Geltungsbereich `user` für bestimmte Werte von `cwd` zu durchsuchen. Der App Server ignoriert Einträge, deren `cwd` nicht in `cwds` enthalten ist. `skills/list` kann pro `cwd` ein zwischengespeichertes Ergebnis wiederverwenden. Setze `forceReload: true`, um die Daten neu vom Datenträger einzulesen. Falls vorhanden, liest der Server `interface` und `dependencies` aus `SKILL.json`.

```json
{ "method": "skills/list", "id": 25, "params": {
  "cwds": ["/Users/me/project", "/Users/me/other-project"],
  "forceReload": true,
  "perCwdExtraUserRoots": [
    {
      "cwd": "/Users/me/project",
      "extraUserRoots": ["/Users/me/shared-skills"]
    }
  ]
} }
{ "id": 25, "result": {
  "data": [{
    "cwd": "/Users/me/project",
    "skills": [
      {
        "name": "skill-creator",
        "description": "Create or update a Codex skill",
        "enabled": true,
        "interface": {
          "displayName": "Skill Creator",
          "shortDescription": "Create or update a Codex skill"
        },
        "dependencies": {
          "tools": [
            {
              "type": "env_var",
              "value": "GITHUB_TOKEN",
              "description": "GitHub API token"
            },
            {
              "type": "mcp",
              "value": "github",
              "transport": "streamable_http",
              "url": "https://example.com/mcp"
            }
          ]
        }
      }
    ],
    "errors": []
  }]
} }

Der Server gibt außerdem Benachrichtigungen vom Typ `skills/changed` aus, wenn sich überwachte lokale Skill-Dateien ändern. Behandle dies als Signal, dass die bisherigen Daten nicht mehr aktuell sind, und rufe `skills/list` bei Bedarf mit deinen aktuellen Parametern erneut auf.

So aktivierst oder deaktivierst du einen Skill anhand seines Pfads:

```json
{
  "method": "skills/config/write",
  "id": 26,
  "params": {
    "path": "/Users/me/.codex/skills/skill-creator/SKILL.md",
    "enabled": false
  }
}

## Apps (Konnektoren)

Verwende `app/installed`, um den zuletzt festgeschriebenen Snapshot des Laufzeitstatus installierter Apps abzurufen.
Jedes Ergebnis enthält für die App die Felder `id`, `runtimeName` (oder `null`), den effektiven
Status von `enabled` und den Status von `callable`. Aufrufbar ist eine App nur, wenn die effektive
Konfiguration sie aktiviert und mindestens ein für das Modell sichtbares Tool die
Richtlinien für Apps und Tools erfüllt.

```json
{
  "method": "app/installed",
  "id": 49,
  "params": {
    "threadId": "thread-1",
    "forceRefresh": false
  }
}
{
  "id": 49,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "runtimeName": "Demo App",
        "enabled": true,
        "callable": true
      }
    ]
  }
}

Lasse `threadId` weg, um statt der Konfiguration eines geladenen Threads die globale
Konfiguration zu verwenden. Setze `forceRefresh: true`, um den Laufzeit-Snapshot des Konnektors vor dem
Lesen zu aktualisieren. Wenn globale oder Workspace-Richtlinien den Zugriff auf Apps blockieren,
kann eine erfasste App dennoch angezeigt werden, wobei `enabled` und `callable` auf `false` gesetzt sind.

Verwende `app/list`, um verfügbare Apps abzurufen. In der CLI/TUI dient `/apps` als App-Auswahl für Nutzende. In eigenen Clients rufst du `app/list` direkt auf. Jeder Eintrag enthält sowohl `isAccessible` (für Nutzende verfügbar) als auch `isEnabled` (in `config.toml` aktiviert), damit Clients zwischen dem Installations- beziehungsweise Zugriffsstatus und dem lokalen Aktivierungsstatus unterscheiden können. App-Einträge können außerdem die optionalen Felder `branding`, `appMetadata` und `labels` enthalten.

```json
{ "method": "app/list", "id": 50, "params": {
  "cursor": null,
  "limit": 50,
  "threadId": "thread-1",
  "forceRefetch": false
} }
{ "id": 50, "result": {
  "data": [
    {
      "id": "demo-app",
      "name": "Demo App",
      "description": "Example connector for documentation.",
      "logoUrl": "https://example.com/demo-app.png",
      "logoUrlDark": null,
      "distributionChannel": null,
      "branding": null,
      "appMetadata": null,
      "labels": null,
      "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
      "isAccessible": true,
      "isEnabled": true
    }
  ],
  "nextCursor": null
} }

Wenn du `threadId` angibst, verwendet die Funktionsfreigabe für Apps (`features.apps`) den Konfigurations-Snapshot dieses Threads. Ohne das Feld verwendet der App Server die aktuelle globale Konfiguration.

`app/list` gibt erst dann ein Ergebnis zurück, wenn sowohl die zugänglichen Apps als auch die Apps aus dem Verzeichnis geladen wurden. Setze `forceRefetch: true`, um App-Caches zu umgehen und aktuelle Daten abzurufen. Cache-Einträge werden nur ersetzt, wenn die Aktualisierung erfolgreich ist.

Der Server gibt außerdem Benachrichtigungen vom Typ `app/list/updated` aus, sobald eine der beiden Quellen (zugängliche Apps oder Apps aus dem Verzeichnis) vollständig geladen ist. Jede Benachrichtigung enthält die aktuelle zusammengeführte App-Liste.

```json
{
  "method": "app/list/updated",
  "params": {
    "data": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "logoUrl": "https://example.com/demo-app.png",
        "logoUrlDark": null,
        "distributionChannel": null,
        "branding": null,
        "appMetadata": null,
        "labels": null,
        "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
        "isAccessible": true,
        "isEnabled": true
      }
    ]
  }
}

Verwende `app/read`, wenn du die App-IDs bereits kennst und App-Metadaten statt
des Laufzeitstatus installierter Apps benötigst. Übergib höchstens 100 `appIds`. Der Server berücksichtigt bei wiederholten IDs nur
deren erstes Vorkommen und behält diese Reihenfolge sowohl in
`apps` als auch in `missingAppIds` bei. Unbekannte oder nicht zugängliche Apps werden in
`missingAppIds` zurückgegeben, ohne dass die gesamte Anfrage fehlschlägt.

```json
{
  "method": "app/read",
  "id": 52,
  "params": {
    "appIds": ["demo-app", "missing-app"],
    "includeTools": true
  }
}
{
  "id": 52,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "iconUrl": null,
        "iconUrlDark": null,
        "distributionChannel": null,
        "installUrl": null,
        "pluginDisplayNames": [],
        "toolSummaries": [
          {
            "name": "search",
            "title": "Search",
            "description": "Search the app.",
            "isEnabled": true,
            "disabledReason": null,
            "isReadOnly": true
          }
        ]
      }
    ],
    "missingAppIds": ["missing-app"]
  }
}

Setze `includeTools: true`, um öffentliche Tool-Zusammenfassungen ausschließlich zur Anzeige anzufordern. Die
Metadatenantwort enthält weder den Laufzeitstatus installierter Apps noch autorisiert sie
einen Tool-Aufruf. Prüfe mit `app/installed` die tatsächlich geltenden
Werte für `enabled` und `callable`.

Rufe eine App auf, indem du `$<app-slug>` in die Texteingabe einfügst und ein Eingabeelement vom Typ `mention` mit dem Pfad `app://<id>` hinzufügst (empfohlen).

```json
{
  "method": "turn/start",
  "id": 51,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$demo-app Pull the latest updates from the team."
      },
      {
        "type": "mention",
        "name": "Demo App",
        "path": "app://demo-app"
      }
    ]
  }
}

### Beispiele für Konfigurations-RPCs für App-Einstellungen

Verwende `config/read`, `config/value/write` und `config/batchWrite`, um App-Einstellungen in `config.toml` einzusehen oder zu aktualisieren.

Lies die Struktur der wirksamen App-Konfiguration aus (einschließlich `_default` und Überschreibungen für einzelne Tools):

```json
{ "method": "config/read", "id": 60, "params": { "includeLayers": false } }
{ "id": 60, "result": {
  "config": {
    "apps": {
      "_default": {
        "enabled": true,
        "destructive_enabled": true,
        "open_world_enabled": true,
        "approvals_reviewer": "user",
        "default_tools_approval_mode": "auto"
      },
      "google_drive": {
        "enabled": true,
        "destructive_enabled": false,
        "approvals_reviewer": "auto_review",
        "default_tools_approval_mode": "prompt",
        "tools": {
          "files/delete": { "enabled": false, "approval_mode": "approve" }
        }
      }
    }
  }
} }

`apps._default.approvals_reviewer` legt den Reviewer für alle Apps fest, sofern kein
Wert für die jeweilige App diese Einstellung überschreibt. Fehlen beide Werte, übernimmt die App den
Wert von `approvals_reviewer` auf oberster Ebene. `apps._default.default_tools_approval_mode`
legt den ersatzweise verwendeten Genehmigungsmodus für Tools fest, für die weder auf App-Ebene
noch auf Tool-Ebene eine Überschreibung vorliegt. Verwaltete Vorgaben zum Genehmigungsmodus haben Vorrang
vor den entsprechenden Tool-Einstellungen.

Aktualisiere eine einzelne App-Einstellung:

```json
{
  "method": "config/value/write",
  "id": 61,
  "params": {
    "keyPath": "apps.google_drive.default_tools_approval_mode",
    "value": "prompt",
    "mergeStrategy": "replace"
  }
}

Wende mehrere App-Änderungen atomar an:

```json
{
  "method": "config/batchWrite",
  "id": 62,
  "params": {
    "edits": [
      {
        "keyPath": "apps._default.destructive_enabled",
        "value": false,
        "mergeStrategy": "upsert"
      },
      {
        "keyPath": "apps.google_drive.tools.files/delete.approval_mode",
        "value": "approve",
        "mergeStrategy": "upsert"
      }
    ]
  }
}

### Konfiguration externer Agenten erkennen und importieren

Verwende `externalAgentConfig/detect`, um migrierbare Artefakte externer Agenten zu erkennen, und übergib die ausgewählten Einträge anschließend an `externalAgentConfig/import`.

Beispiel für die Erkennung:

```json
{ "method": "externalAgentConfig/detect", "id": 63, "params": {
  "includeHome": true,
  "cwds": ["/Users/me/project"]
} }
{ "id": 63, "result": {
  "items": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    },
    {
      "itemType": "SKILLS",
      "description": "Copy skill folders from /Users/me/.claude/skills to /Users/me/.agents/skills.",
      "cwd": null
    }
  ]
} }

Importbeispiel:

```json
{ "method": "externalAgentConfig/import", "id": 64, "params": {
  "migrationItems": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    }
  ],
  "source": "claude-code"
} }
{ "id": 64, "result": { "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868" } }

Der optionale Importparameter `source` auf oberster Ebene kennzeichnet das Produkt,
das die ausgewählten Migrationselemente erstellt hat.

Der Server gibt `externalAgentConfig/import/progress` aus, sobald einzelne Elementtypen vollständig importiert wurden,
und `externalAgentConfig/import/completed`, nachdem alle synchronen und im Hintergrund ausgeführten
Importe abgeschlossen sind. Diese Benachrichtigungen enthalten dieselbe `importId` wie die
Antwort sowie `itemTypeResults` mit `successes` und `failures` für jeden Typ.
Die Abschlussbenachrichtigung kann unmittelbar nach der Antwort oder erst nach Abschluss der
im Hintergrund ausgeführten Remote-Importe eintreffen.

```json
{ "method": "externalAgentConfig/import/progress", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }
{ "method": "externalAgentConfig/import/completed", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }

Lies bereits abgeschlossene Importe aus:

```json
{ "method": "externalAgentConfig/import/readHistories", "id": 65 }
{ "id": 65, "result": { "data": [
  {
    "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
    "completedAtMs": 1781784000000,
    "successes": [
      { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
    ],
    "failures": []
  }
] } }

Unterstützte Werte für `itemType` sind `AGENTS_MD`, `CONFIG`, `SKILLS`, `PLUGINS`,
`MCP_SERVER_CONFIG`, `SUBAGENTS`, `HOOKS`, `COMMANDS` und `SESSIONS`. Für
Elemente vom Typ `PLUGINS` listet `details.plugins` jeweils `marketplaceName` und die
`pluginNames` auf, deren Migration Codex versuchen kann. Die Erkennung gibt nur Elemente zurück, bei denen
noch Arbeit aussteht. Codex überspringt beispielsweise die AGENTS-Migration, wenn `AGENTS.md`
bereits vorhanden und nicht leer ist. Skill-Importe überschreiben keine vorhandenen
Skill-Verzeichnisse.

Bei der Erkennung von Plug-ins anhand von `.claude/settings.json` liest Codex die konfigurierten
Marketplace-Quellen aus `extraKnownMarketplaces`. Wenn `enabledPlugins`
Plug-ins aus `claude-plugins-official` enthält, die Marketplace-Quelle aber fehlt,
nimmt Codex `anthropics/claude-plugins-official` als Quelle an.

## Authentifizierungsendpunkte

Die JSON-RPC-Schnittstelle für Authentifizierung und Konten stellt Methoden für Anfragen und Antworten sowie vom Server initiierte Benachrichtigungen bereit (ohne `id`). Verwende sie, um den Authentifizierungsstatus zu ermitteln, Anmeldungen zu starten oder abzubrechen, dich abzumelden, ChatGPT-Ratenlimits einzusehen und Personen mit Inhaberrolle im Workspace über aufgebrauchte Credits oder Nutzungslimits zu benachrichtigen.

### Authentifizierungsmodi

Codex unterstützt die folgenden Authentifizierungsmodi. `account/updated.authMode` zeigt den aktiven Modus an und enthält, sofern verfügbar, unter `planType` den aktuellen ChatGPT-Tarif. `account/read` gibt außerdem Informationen zum Konto und zum Tarif zurück.

- **API-Schlüssel (`apikey`)** : Der aufrufende Client übergibt mit `type: "apiKey"` einen OpenAI-API-Schlüssel, den Codex für API-Anfragen speichert.
- **Verwaltete ChatGPT-Authentifizierung (`chatgpt`)** : Codex übernimmt den OAuth-Ablauf für ChatGPT, speichert Token dauerhaft und aktualisiert sie automatisch. Starte den Anmeldeablauf im Browser mit `type: "chatgpt"` oder den Ablauf per Gerätecode mit `type: "chatgptDeviceCode"`.
- **Extern verwaltete ChatGPT-Token (`chatgptAuthTokens`)** : Dieser experimentelle Modus ist für Host-Apps vorgesehen, die die ChatGPT-Authentifizierung ihrer Nutzenden bereits vollständig selbst verwalten. Die Host-App stellt `accessToken`, `chatgptAccountId` und optional `chatgptPlanType` direkt bereit und muss das Token auf Anforderung aktualisieren.
- **Amazon Bedrock** : `account/read` gibt Bedrock-Konten als `type: "amazonBedrock"` zurück und zeigt an, ob die Anmeldedaten von einem durch Codex verwalteten Bedrock-API-Schlüssel (`credentialSource: "codexManaged"`) oder aus der externen AWS-Anmeldedatenkette (`credentialSource: "awsManaged"`) stammen. `account/updated.authMode` verwendet `bedrockApiKey` für von Codex verwaltete Bedrock-API-Schlüssel.

### API-Übersicht

- `account/read`: Aktuelle Kontoinformationen abrufen und optional Token aktualisieren.
- `account/login/start`: Anmeldung starten (`apiKey`, `chatgpt`, `chatgptDeviceCode` oder experimentell `chatgptAuthTokens`).
- `account/login/completed` (Benachrichtigung): Wird nach Abschluss eines Anmeldeversuchs ausgegeben (Erfolg oder Fehler).
- `account/login/cancel`: Eine ausstehende verwaltete ChatGPT-Anmeldung anhand von `loginId` abbrechen.
- `account/logout`: Abmelden; löst `account/updated` aus.
- `account/updated` (Benachrichtigung): Wird bei jeder Änderung des Authentifizierungsmodus ausgegeben (`authMode`: `apikey`, `chatgpt`, `chatgptAuthTokens`, `agentIdentity`, `personalAccessToken`, `bedrockApiKey` oder `null`) und enthält, sofern verfügbar, `planType`.
- `account/chatgptAuthTokens/refresh` (Serveranfrage): Nach einem Autorisierungsfehler neue extern verwaltete ChatGPT-Token anfordern.
- `account/rateLimits/read`: ChatGPT-Ratenlimits abrufen.
- `account/rateLimits/updated` (Benachrichtigung): Wird ausgegeben, wenn sich die ChatGPT-Ratenlimits einer Person ändern.
- `account/sendAddCreditsNudgeEmail`: ChatGPT auffordern, eine Person mit Inhaberrolle im Workspace per E-Mail über aufgebrauchte Credits oder ein erreichtes Nutzungslimit zu informieren.
- `account/rateLimitResetCredit/consume`: Eine erworbene Zurücksetzung des Ratenlimits mit einem beim Aufruf übergebenen Wert für `idempotencyKey` einlösen.
- `account/usage/read`: Zusammenfassungen der Token-Aktivität des ChatGPT-Kontos und nach Tagen gruppierte Daten abrufen.
- `account/workspaceMessages/read`: Aktive Workspace-Nachrichten abrufen, einschließlich der Überschriften von Benachrichtigungen, sofern verfügbar.
- `mcpServer/oauthLogin/completed` (Benachrichtigung): Wird nach Abschluss eines Ablaufs vom Typ `mcpServer/oauth/login` ausgegeben; die Nutzlast enthält `{ name, threadId, success, error? }`. Bei OAuth-Abläufen auf App-Ebene oder für Plug-ins kann `threadId` den Wert `null` haben.
- `mcpServer/startupStatus/updated` (Benachrichtigung): Wird ausgegeben, wenn sich der Startstatus eines konfigurierten MCP-Servers ändert; die Nutzlast enthält `{ threadId, name, status, error, failureReason }`. Bei einem Start auf App-Ebene hat `threadId` den Wert `null`. Wenn der Start fehlschlägt, bedeutet `failureReason: "reauthenticationRequired"`, dass die gespeicherten OAuth-Anmeldedaten abgelaufen sind und nicht aktualisiert werden konnten. Der Client sollte daher anbieten, die Verbindung zum Server wiederherzustellen.

### 1) Authentifizierungsstatus prüfen

Anfrage:

```json
{ "method": "account/read", "id": 1, "params": { "refreshToken": false } }

Antwortbeispiele:

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": false } }

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": true } }

```json
{
  "id": 1,
  "result": { "account": { "type": "apiKey" }, "requiresOpenaiAuth": true }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "codexManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "awsManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "chatgpt",
      "email": "user@example.com",
      "planType": "pro"
    },
    "requiresOpenaiAuth": true
  }
}

Hinweise zu den Feldern:

- `refreshToken` (boolescher Wert): Setze den Wert auf `true`, um im Modus mit verwalteter ChatGPT-Authentifizierung eine Aktualisierung des Tokens zu erzwingen. Im Modus mit extern verwalteten Token (`chatgptAuthTokens`) ignoriert app-server dieses Flag.
- `email` hat den Wert `null`, wenn dem ChatGPT-Konto keine E-Mail-Adresse zugeordnet ist.
- `requiresOpenaiAuth` richtet sich nach dem aktiven Anbieter. Bei `false` kann Codex ohne OpenAI-Anmeldedaten ausgeführt werden.
- Amazon Bedrock meldet `credentialSource: "codexManaged"`, wenn es einen
  von Codex verwalteten Bedrock-API-Schlüssel verwendet. Für den Bezug externer AWS-Anmeldedaten meldet es `credentialSource: "awsManaged"`.
  Damit wird die ausgewählte Quelle der Anmeldedaten angegeben.
  Es wird nicht geprüft, ob die AWS-Anmeldedatenkette
  Anmeldedaten ermitteln kann.

### 2) Mit einem API-Schlüssel anmelden

1. Senden:

   ```json
   {
     "method": "account/login/start",
     "id": 2,
     "params": { "type": "apiKey", "apiKey": "sk-..." }
   }

2. Erwartete Antwort:

   ```json
   { "id": 2, "result": { "type": "apiKey" } }

3. Benachrichtigungen:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "apikey", "planType": null }
   }

### 3) Mit ChatGPT anmelden (Ablauf im Browser)

1. Starten:

   ```json
   {
     "method": "account/login/start",
     "id": 3,
     "params": {
       "type": "chatgpt",
       "useHostedLoginSuccessPage": true,
       "appBrand": "chatgpt"
     }
   }

   Standardmäßig leitet ein erfolgreicher Browser-Callback auf eine lokale Erfolgsseite weiter.
   Setze `useHostedLoginSuccessPage: true`, um die gehostete Erfolgsseite zu verwenden, wenn
   keine Organisation eingerichtet werden muss. Wenn die gehostete Erfolgsseite aktiviert ist, kann `appBrand`
   den Wert `"codex"` oder `"chatgpt"` haben. Fehlt der Wert oder ist er `null`,
gilt standardmäßig `"codex"`.

   ```json
   {
     "id": 3,
     "result": {
       "type": "chatgpt",
       "loginId": "<uuid>",
       "authUrl": "https://chatgpt.com/...&redirect_uri=http%3A%2F%2Flocalhost%3A<port>%2Fauth%2Fcallback"
     }
   }

2. Öffne `authUrl` in einem Browser; app-server stellt den lokalen Callback bereit.
3. Warte auf Benachrichtigungen:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3b) Mit ChatGPT anmelden (Ablauf per Gerätecode)

Verwende diesen Ablauf, wenn dein Client den Anmeldevorgang selbst übernimmt oder ein Browser-Callback störanfällig ist.

1. Starten:

   ```json
   {
     "method": "account/login/start",
     "id": 4,
     "params": { "type": "chatgptDeviceCode" }
   }

   ```json
   {
     "id": 4,
     "result": {
       "type": "chatgptDeviceCode",
       "loginId": "<uuid>",
       "verificationUrl": "https://auth.openai.com/codex/device",
       "userCode": "ABCD-1234"
     }
   }

2. Zeige den Nutzenden `verificationUrl` und `userCode` an. Das Frontend ist für die Benutzerführung verantwortlich.
3. Warte auf Benachrichtigungen:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3c) Mit extern verwalteten ChatGPT-Token anmelden (`chatgptAuthTokens`)

Verwende diesen experimentellen Modus nur, wenn eine Host-Anwendung den gesamten Ablauf der ChatGPT-Authentifizierung für die nutzende Person verwaltet und Token direkt bereitstellt. Clients müssen `capabilities.experimentalApi = true` beim Aufruf von `initialize` setzen, bevor sie diesen Anmeldetyp verwenden.

1. Senden:

   ```json
   {
     "method": "account/login/start",
     "id": 7,
     "params": {
       "type": "chatgptAuthTokens",
       "accessToken": "<jwt>",
       "chatgptAccountId": "org-123",
       "chatgptPlanType": "business"
     }
   }

2. Erwartetes Ergebnis:

   ```json
   { "id": 7, "result": { "type": "chatgptAuthTokens" } }

3. Benachrichtigungen:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgptAuthTokens", "planType": "business" }
   }

Wenn der Server eine Antwort mit `401 Unauthorized` erhält, kann er aktualisierte Token von der Host-App anfordern:

```json
{
  "method": "account/chatgptAuthTokens/refresh",
  "id": 8,
  "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
}
{ "id": 8, "result": { "accessToken": "<jwt>", "chatgptAccountId": "org-123", "chatgptPlanType": "business" } }

Nach einer erfolgreichen Antwort auf die Aktualisierungsanfrage wiederholt der Server die ursprüngliche Anfrage. Für Anfragen gilt ein Timeout von etwa 10 Sekunden.

### 4) ChatGPT-Anmeldung abbrechen

```json
{ "method": "account/login/cancel", "id": 4, "params": { "loginId": "<uuid>" } }
{ "method": "account/login/completed", "params": { "loginId": "<uuid>", "success": false, "error": "..." } }

### 5) Abmelden

```json
{ "method": "account/logout", "id": 5 }
{ "id": 5, "result": {} }
{ "method": "account/updated", "params": { "authMode": null, "planType": null } }

### 6) Ratenlimits (ChatGPT)

```json
{ "method": "account/rateLimits/read", "id": 6 }
{ "id": 6, "result": {
  "rateLimits": {
    "limitId": "codex",
    "limitName": null,
    "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
    "secondary": null,
    "rateLimitReachedType": null
  },
  "rateLimitsByLimitId": {
    "codex": {
      "limitId": "codex",
      "limitName": null,
      "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
      "secondary": null,
      "rateLimitReachedType": null
    },
    "codex_other": {
      "limitId": "codex_other",
      "limitName": "codex_other",
      "primary": { "usedPercent": 42, "windowDurationMins": 60, "resetsAt": 1730950800 },
      "secondary": null,
      "rateLimitReachedType": null
    }
  },
  "rateLimitResetCredits": {
    "availableCount": 2,
    "credits": [{
      "id": "RateLimitResetCredit_1",
      "resetType": "codexRateLimits",
      "status": "available",
      "grantedAt": 1781654400,
      "expiresAt": 1784246400,
      "title": "Rate-limit reset",
      "description": "Reset an eligible Codex rate-limit window."
    }]
  }
} }
{ "method": "account/rateLimits/updated", "params": {
  "rateLimits": {
    "limitId": "codex",
    "primary": { "usedPercent": 31, "windowDurationMins": 15, "resetsAt": 1730948100 }
  }
} }

Hinweise zu den Feldern:

- `rateLimits` ist die abwärtskompatible Ansicht für einen einzelnen Bucket.
- `rateLimitsByLimitId` ist, sofern vorhanden, die Ansicht für mehrere Buckets mit der jeweiligen `limit_id` für die Nutzungsmessung als Schlüssel (zum Beispiel `codex`).
- `limitId` ist die Kennung des Buckets für die Nutzungsmessung.
- `limitName` ist eine optionale Bezeichnung des Buckets für die Benutzeroberfläche.
- `usedPercent` gibt die aktuelle Nutzung innerhalb des Kontingentzeitraums an.
- `windowDurationMins` gibt die Länge des Kontingentzeitraums an.
- `resetsAt` ist ein Unix-Zeitstempel in Sekunden für den Zeitpunkt der nächsten Zurücksetzung.
- `planType` ist enthalten, wenn der Server den dem Bucket zugeordneten ChatGPT-Tarif zurückgibt.
- `credits` ist enthalten, wenn der Server Details zu den verbleibenden Credits des Workspaces zurückgibt.
- `rateLimitReachedType` kennzeichnet den vom Server klassifizierten Limitstatus, wenn ein Limit erreicht wurde.
- `rateLimitResetCredits` gibt an, wie viele verdiente Zurücksetzungen verfügbar sind, sofern der Dienst diese Angabe bereitstellt. Andernfalls ist der Wert `null`.
- `rateLimitResetCredits.credits` ist `null`, wenn nur die Anzahl bekannt ist. Ein leeres Array bedeutet, dass der Dienst Details abgerufen und keine verfügbaren Credits zurückgegeben hat. Da der Dienst die Anzahl der Detailzeilen begrenzen kann, ist `availableCount` maßgeblich.
- Jede Detailzeile enthält eine opake `id`, `resetType`, `status`, `grantedAt`, `expiresAt` (kann `null` sein), `title` (kann `null` sein) und `description` (kann `null` sein).
- Rufe nach dem Einlösen einer Zurücksetzung `account/rateLimits/read` auf.

### 7) Token-Nutzung (ChatGPT)

Rufe mit `account/usage/read` die Felder mit einer Zusammenfassung der Token-Aktivität in ChatGPT und
optional die täglichen Buckets ab.

```json
{ "method": "account/usage/read", "id": 7 }
{ "id": 7, "result": {
  "summary": {
    "lifetimeTokens": 1234567,
    "peakDailyTokens": 45678,
    "longestRunningTurnSec": 540,
    "currentStreakDays": 8,
    "longestStreakDays": 14
  },
  "dailyUsageBuckets": [
    { "startDate": "2026-06-18", "tokens": 12345 }
  ]
} }

Hinweise zu den Feldern:

- Die Werte in `summary` können `null` sein, wenn der Dienst die entsprechende Metrik nicht zurückgegeben hat.
- `dailyUsageBuckets` kann `null` sein. Wenn Buckets vorhanden sind, enthält jeder davon `startDate` und `tokens`.
- Der Endpunkt erfordert eine Authentifizierung über Codex-Dienste. Unterstützt werden die Authentifizierung über ChatGPT,
mit externen ChatGPT-Token, mit einer Agentenidentität und mit einem persönlichen Zugriffstoken.
Eine reine API-Schlüssel-Authentifizierung und die Authentifizierung über Bedrock werden nicht unterstützt.

### 8) Verdiente Zurücksetzungen von Ratenlimits (ChatGPT)

Verwende `account/rateLimitResetCredit/consume`, um eine verdiente Zurücksetzung einzulösen.

```json
{ "method": "account/rateLimitResetCredit/consume", "id": 8, "params": { "idempotencyKey": "8ae96ff3-3425-4f4c-8772-b6fd61502868", "creditId": "RateLimitResetCredit_1" } }
{ "id": 8, "result": { "outcome": "reset" } }

Hinweise zu den Feldern:

- `idempotencyKey` darf nicht leer sein. Verwende für jeden logischen Einlöseversuch eine UUID und bei Wiederholungen desselben Versuchs denselben Wert.
- `creditId` ist optional. Wenn du das Feld angibst, muss es eine nicht leere opake ID aus `account/rateLimits/read` enthalten. Lässt du es weg, wählt der Dienst den nächsten verfügbaren Credit aus.
- `reset` bedeutet, dass ein Credit eingelöst wurde.
- `alreadyRedeemed` bedeutet, dass dieselbe Einlösung bereits abgeschlossen wurde. Behandle dies als idempotenten Erfolg und aktualisiere die Kontolimits.
- `nothingToReset` bedeutet, dass kein Ratenlimit-Zeitfenster für eine Zurücksetzung infrage kommt.
- `noCredit` bedeutet, dass für das Konto keine verdienten Credits für Zurücksetzungen verfügbar sind.
- Rufe nach dem Einlösen einer Zurücksetzung `account/rateLimits/read` auf, statt die aktualisierten Ratenlimit-Zeitfenster aus dieser Antwort abzuleiten.

### 9) Person mit Workspace-Inhaberrechten über ein Limit benachrichtigen

Fordere ChatGPT mit `account/sendAddCreditsNudgeEmail` auf, eine Person mit Workspace-Inhaberrechten per E-Mail zu benachrichtigen, wenn die Credits aufgebraucht sind oder ein Nutzungslimit erreicht wurde.

```json
{ "method": "account/sendAddCreditsNudgeEmail", "id": 9, "params": { "creditType": "credits" } }
{ "id": 9, "result": { "status": "sent" } }

Verwende `creditType: "credits"`, wenn die Credits des Workspaces aufgebraucht sind, oder `creditType: "usage_limit"`, wenn das Nutzungslimit des Workspaces erreicht wurde. Wurde die Person mit Inhaberrechten bereits vor Kurzem benachrichtigt, lautet der Antwortstatus `cooldown_active`.

### 10) Workspace-Nachrichten (ChatGPT)

Rufe mit `account/workspaceMessages/read` die aktiven Nachrichten für den aktuellen
Workspace ab, einschließlich der Überschriften von Benachrichtigungen, sofern verfügbar.

```json
{ "method": "account/workspaceMessages/read", "id": 10 }
{ "id": 10, "result": { "featureEnabled": true, "messages": [
  { "messageId": "msg_123", "messageType": "headline", "messageBody": "Workspace maintenance starts at 5pm.", "createdAt": 1781395200, "archivedAt": null }
] } }
