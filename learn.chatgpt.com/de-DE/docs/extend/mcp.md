<!-- source: https://learn.chatgpt.com/de-DE/docs/extend/mcp -->

Das Model Context Protocol (MCP) verbindet Modelle mit Tools und Kontext. Nutze es, damit ChatGPT oder Codex auf Dokumentation von Drittanbietern zugreifen oder mit Entwicklungstools wie deinem Browser oder Figma interagieren kann.

ChatGPT im Web kann Remote-Tools verwenden, die Plug-ins über MCP bereitstellen. Lokale Codex-Clients können sich auch direkt mit MCP-Servern verbinden und eine gemeinsame Konfiguration verwenden.

<a id="supported-mcp-features"></a>

Die ChatGPT-Desktop-App, Codex CLI und die IDE-Erweiterung unterstützen MCP-Server und verwenden für denselben Codex-Host eine gemeinsame MCP-Konfiguration.

Die folgenden Funktionen werden für MCP-Server unterstützt, die auf einem Codex-Host konfiguriert sind. Gehostete Plug-in-Tools können andere Funktionen bieten.

## Unterstützte MCP-Funktionen

- **STDIO-Server**: Server, die als lokaler Prozess ausgeführt werden (per Befehl gestartet).
  - Umgebungsvariablen
- **Streamable-HTTP-Server**: Server, auf die du über eine Adresse zugreifst.
  - Authentifizierung mit Bearer-Tokens
  - OAuth-Authentifizierung einschließlich Client ID Metadata Documents (CIMD) und Dynamic Client Registration (DCR)
  - Authentifizierung über die ChatGPT-Sitzung für vertrauenswürdige Server des Erstanbieters
- **Serveranweisungen**: Codex liest das bei der Initialisierung zurückgegebene MCP-Feld `instructions` und nutzt es neben den Tools des Servers als serverweit geltende Anleitung.

Wenn du einen MCP-Server für Codex entwickelst oder betreust, verwende `instructions` für toolübergreifende Arbeitsabläufe sowie für serverweit geltende Einschränkungen und Ratenlimits. Formuliere die ersten 512 Zeichen so, dass sie für sich allein verständlich sind. So stehen Codex die wichtigsten Anweisungen zur Verfügung, wenn es entscheidet, wie es den Server verwendet.

## Codex mit einem MCP-Server verbinden

Codex speichert die MCP-Konfiguration zusammen mit anderen Codex-Einstellungen in `config.toml`. Standardmäßig ist das `~/.codex/config.toml`. Mit `.codex/config.toml` kannst du MCP-Server auch projektbezogen konfigurieren (nur für vertrauenswürdige Projekte).

Die ChatGPT-Desktop-App, Codex CLI und die IDE-Erweiterung verwenden diese Konfiguration gemeinsam. Sobald du deine MCP-Server konfiguriert hast, kannst du zwischen diesen Clients wechseln, ohne das Setup zu wiederholen.

### In der ChatGPT-Desktop-App konfigurieren

1. Öffne die **Einstellungen** und wähle dann **MCP-Server** aus.
2. Wähle **Server hinzufügen** aus.
3. Gib einen Namen ein, wähle **STDIO** oder **Streamable HTTP** und gib
   den Befehl oder die URL des Servers an.
4. Speichere den Server und wähle dann **Neu starten** aus.

Die Serverliste zeigt, welche Server aktiviert sind und welche OAuth erfordern. Wähle
**Authentifizieren** aus, wenn für einen OAuth-Server eine Anmeldung erforderlich ist. Gib im Editor `/mcp`
ein, um verbundene Server anzuzeigen.

## MCP-gestützte Tools in ChatGPT im Web verwenden

Installiere in einem gehosteten Chat in ChatGPT Work ein [Plug-in](/de-DE/codex/plugins), um die
mitgelieferten Konnektoren und Remote-MCP-Tools zu verwenden. Nach der Installation können Chat und Work
diese Tools verwenden. Die Workspace-Administration kann festlegen, welche Plug-ins und Tools
verfügbar sind.

ChatGPT im Web liest keine lokalen Codex-Konfigurationsdateien und stellt das lokale
Codex-Befehlsmenü nicht bereit. Öffne den Tab **Plug-ins** , um verfügbare
Tools zu durchsuchen und zu verwalten.

### Mit der CLI konfigurieren

#### Einen MCP-Server hinzufügen

```bash
codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>

Um beispielsweise Context7, einen kostenlosen MCP-Server für Dokumentation zur Softwareentwicklung, hinzuzufügen, kannst du folgenden Befehl ausführen:

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp

#### Weitere CLI-Befehle

Führe `codex mcp list` aus, um die konfigurierten Server anzuzeigen. Um alle verfügbaren
MCP-Befehle anzuzeigen, führe `codex mcp --help` aus. Unterstützt ein Server OAuth, führe
`codex mcp login <server-name>` aus.

#### Terminal-Oberfläche (TUI)

Verwende in der TUI von `codex` den Befehl `/mcp`, um deine aktiven MCP-Server anzuzeigen.

### In der IDE-Erweiterung konfigurieren

1. Öffne das Menü über das Zahnradsymbol und wähle dann **MCP-Server** aus.
2. Wähle **Server hinzufügen** aus.
3. Gib einen Namen ein, wähle **STDIO** oder **Streamable HTTP** und gib
   den Befehl oder die URL des Servers an.
4. Speichere den Server und wähle dann **Erweiterung neu starten** aus.

Die MCP-Serverliste zeigt, welche Server aktiviert sind und welche OAuth erfordern.
Wähle **Authentifizieren** aus, wenn für einen OAuth-Server eine Anmeldung erforderlich ist.

### Mit config.toml konfigurieren

Um die Einstellungen genauer anzupassen, bearbeite `~/.codex/config.toml` oder die projektbezogene Datei
`.codex/config.toml`. Die [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference)
enthält eine durchsuchbare Liste aller unterstützten MCP-Optionen.

Konfiguriere jeden MCP-Server über eine Tabelle `[mcp_servers.<server-name>]` in der Konfigurationsdatei.

<a id="stdio-servers"></a>

#### STDIO-Server

- `command` (erforderlich): Der Befehl, mit dem der Server gestartet wird.
- `args` (optional): Argumente, die an den Server übergeben werden.
- `env` (optional): Umgebungsvariablen, die für den Server gesetzt werden.
- `env_vars` (optional): Umgebungsvariablen, die zugelassen und weitergeleitet werden.
- `cwd` (optional): Arbeitsverzeichnis, aus dem der Server gestartet wird.
- `experimental_environment` (optional): Setze den Wert auf `remote`, um den STDIO-Server
  über eine Remote-Ausführungsumgebung zu starten, sofern eine verfügbar ist.

`env_vars` kann einfache Variablennamen oder Objekte mit einer Quellenangabe enthalten:

```toml
env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]

Bei String-Einträgen und `source = "local"` stammen die Werte aus der lokalen Codex-Umgebung.
Mit `source = "remote"` werden Werte aus der Remote-Ausführungsumgebung gelesen; dafür ist
Remote-MCP über STDIO erforderlich.

<a id="streamable-http-servers"></a>

#### Streamable-HTTP-Server

- `url` (erforderlich): Die Serveradresse.
- `auth` (optional): Authentifizierungsmethode, die nach konfigurierten Bearer-Tokens und
  Autorisierungsheadern versucht wird. Verwende `oauth` (Standard) für gespeicherte
  MCP-OAuth-Anmeldedaten. Verwende `chatgpt`, um für die vertrauenswürdige
  ChatGPT-Origin des Erstanbieters die aktuelle ChatGPT-Sitzung zu nutzen; gespeicherte OAuth-Anmeldedaten dienen als Fallback.
- `bearer_token_env_var` (optional): Name der Umgebungsvariablen für ein Bearer-Token, das im Header `Authorization` gesendet wird.
- `http_headers` (optional): Zuordnung von Header-Namen zu statischen Werten.
- `env_http_headers` (optional): Zuordnung von Header-Namen zu Namen von Umgebungsvariablen (die Werte werden aus der Umgebung abgerufen).
- `http_headers_helper` (optional): Lokaler Befehl, der ein JSON-Objekt mit
  Header-Namen und String-Werten ausgibt, etwa `{"X-Auth": "temporary-token"}`.
  Wird für HTTP-MCP-Verbindungen unterstützt, die aus der lokalen Umgebung hergestellt werden, aber nicht für
  STDIO-Server oder Verbindungen über eine Remote-Ausführungsumgebung.

Codex speichert die vom Hilfsprogramm gelieferten Header für die Verbindung im Cache. Wenn eine POST-Anfrage an dieselbe Origin
`401` oder `403` zurückgibt, aktualisiert Codex die Header einmal und wiederholt die Anfrage nur, wenn das
Hilfsprogramm geänderte Werte liefert. Explizit angegebene Bearer-Tokens und OAuth-Anmeldedaten
haben Vorrang vor einem vom Hilfsprogramm gelieferten `Authorization`-Header.
Eine OAuth-Antwort mit Status `403`, die einen unzureichenden Berechtigungsumfang meldet,
löst keine Aktualisierung durch das Hilfsprogramm aus.

Wenn keine der Quellen Anmeldedaten liefert, kann Codex ohne
Authentifizierung eine Verbindung zum Server herstellen. Führe `codex mcp login <server-name>` separat aus, um eine
MCP-OAuth-Anmeldung zu starten.

#### Weitere Konfigurationsoptionen

- `startup_timeout_sec` (optional): Zeitlimit (in Sekunden) für den Start des Servers. Standard: `10`.
- `tool_timeout_sec` (optional): Zeitlimit (in Sekunden) für die Ausführung eines Tools durch den Server. Standard: `60`.
- `enabled` (optional): Setze den Wert auf `false`, um einen Server zu deaktivieren, ohne ihn zu löschen.
- `required` (optional): Setze den Wert auf `true`, damit der Start fehlschlägt, wenn dieser aktivierte Server nicht initialisiert werden kann.
- `enabled_tools` (optional): Liste zugelassener Tools.
- `disabled_tools` (optional): Liste gesperrter Tools (wird nach `enabled_tools` angewendet).
- `default_tools_approval_mode` (optional): Standardmäßiges Genehmigungsverhalten für
  Tools dieses Servers. Unterstützte Werte sind `auto`, `prompt`, `writes` und
`approve`. Im Modus `writes` wird für Tools, die nicht als „ohne Schreibzugriff“ gekennzeichnet sind, eine Genehmigung angefordert.
- `tools.<tool>.approval_mode` (optional): Legt für einzelne Tools ein abweichendes Genehmigungsverhalten fest.
- `tools.<tool>.output_token_limit` (optional): Positives Token-Budget für die Ausgabe eines
  Tools, vor dem üblichen Zuschlag von 20 % für die Serialisierung. Ersetzt
  das Standardbudget des Modells, bis zu dem die Ausgabe dieses Tools ungekürzt bleibt.

Die Einstellung `mcp_optional_startup_grace_ms` auf oberster Ebene legt fest, wie lange Codex
beim Erstellen des anfänglichen Tool-Katalogs auf optionale MCP-Server wartet.
Der Standardwert beträgt `1000` Millisekunden. Setze den Wert auf `0`, um stattdessen für jeden Server
die in `startup_timeout_sec` festgelegte Zeit zu warten. Für erforderliche Server gelten weiterhin
die jeweiligen Startzeitlimits.

#### Registrierung von OAuth-Clients und Callbacks

Wenn dein Autorisierungsserver einen vorab registrierten OAuth-Client erfordert, gib
beim Hinzufügen des MCP-Servers dessen Client-ID an:

```bash
codex mcp add example --url https://mcp.example.com --oauth-client-id my-client

Codex zeigt die vollständige Callback-URL an, die du bei deinem Anbieter registrieren musst:

```text
OAuth callback URL: http://127.0.0.1/callback

Codex speichert den Callback zusammen mit der Client-ID in `config.toml` für spätere
Anmeldungen:

```toml
[mcp_servers.example]
url = "https://mcp.example.com"

[mcp_servers.example.oauth]
client_id = "my-client"
callback_url = "http://127.0.0.1/callback"

Neu hinzugefügte, vorab registrierte Clients verwenden nur dann einen stabilen Callback, wenn der
Autorisierungsserver
`authorization_response_iss_parameter_supported: true` angibt und in seinen Metadaten einen
`issuer` bereitstellt. Gibt er keine Unterstützung für die Ausstelleridentifikation an, hängt Codex eine serverspezifische
Callback-ID an, zum Beispiel `http://127.0.0.1/callback/XuuuHAzzHOni`. Bestehende Clients
ohne gespeicherten Callback verwenden weiterhin ihre Weiterleitung mit der jeweiligen Callback-ID.

Bei der Anmeldung richtet sich die Auswahl des Callbacks nach der OAuth-Konfiguration und
den Metadaten des Autorisierungsservers:

| OAuth-Konfiguration                                                | Unterstützung für die Ausstelleridentifikation           | Verwendeter Callback                                                                                                                                      |
| ------------------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_url` ohne `client_id`                                 | Unterstützt                | Der konfigurierte Callback wird zur Clientregistrierung verwendet.                                                                                           |
| `callback_url` ohne `client_id`                                 | Nicht unterstützt              | Der konfigurierte Callback wird mit angehängter serverspezifischer Callback-ID zur Clientregistrierung verwendet.                                             |
| `client_id` und `callback_url`                                     | Unterstützt                | Der konfigurierte Callback wird wiederverwendet; die Autorisierungsantwort muss den passenden Wert für `iss` enthalten.                                                     |
| `client_id` und eine `callback_url`, die mit der korrekten Callback-ID endet | Nicht unterstützt              | Der konfigurierte Callback wird unverändert wiederverwendet.                                                                                                       |
| `client_id` und eine `callback_url` ohne die korrekte Callback-ID   | Nicht unterstützt              | Der konfigurierte Callback wird ignoriert. Codex verwendet `mcp_oauth_callback_url` oder, wenn diese Einstellung nicht gesetzt ist, `http://127.0.0.1/callback`, jeweils mit angehängter Callback-ID. |
| `client_id` ohne konfigurierte `callback_url`                    | Unterstützt oder nicht unterstützt | Codex verwendet den globalen Callback oder den Standard-Callback und hängt die serverspezifische Callback-ID an.                                                           |

Der Fallback ändert die gespeicherte Callback-URL nicht. Codex leitet die Callback-ID
aus der URL des MCP-Servers einschließlich Pfad und Abfragezeichenfolge ab. Für die automatische
und die explizite Anmeldung gelten dieselben Auswahlregeln.

Lege `mcp_oauth_callback_url` fest, wenn du einen benutzerdefinierten Callback-Pfad oder die
Ingress-URL einer Remote-Devbox benötigst. Neu hinzugefügte, vorab registrierte Clients verwenden diese URL unverändert,
wenn ihr Anbieter die Ausstelleridentifikation unterstützt. Andernfalls verwenden sie die
konfigurierte URL mit angehängter serverspezifischer Callback-ID. Registriere immer
genau den Callback, den `codex mcp add` anzeigt.

Bei Callbacks mit `http://127.0.0.1` ohne Portangabe lässt Codex den Listener-Port in
der angezeigten und gespeicherten URL weg und fügt während der
Autorisierung den aktiven Listener-Port ein. Diese Ersetzung gilt nicht für `localhost`, IPv6-Hosts,
HTTPS-URLs oder Callbacks, die bereits einen Port enthalten. Autorisierungsserver
müssen gemäß
[RFC 8252, Abschnitt 7.3](https://www.rfc-editor.org/rfc/rfc8252#section-7.3) variable Loopback-Ports akzeptieren.

Lege `mcp_oauth_callback_port` fest, um einen festen globalen Listener-Port zu wählen, oder lege
`mcp_servers.<server-name>.oauth.callback_port` fest, um ihn für einen einzelnen Server zu überschreiben.
Eine explizite Portangabe in der Callback-URL konfiguriert den Listener nicht. Verwende für
einen direkten Loopback-Callback `http://127.0.0.1` ohne Portangabe oder konfiguriere denselben
Port explizit sowohl für die Callback-URL als auch für den Listener. Bei einem Callback über einen Proxy kann
der externe URL-Port bewusst vom lokalen Listener-Port abweichen.
Bei lokalen Callback-URLs bindet Codex den Listener an die lokale Schnittstelle, bei nicht lokalen Callback-URLs
an `0.0.0.0`.

Codex validiert jeden zurückgegebenen Wert für `iss`, bevor es den Autorisierungscode einlöst. Ein
abweichender Wert für `iss` führt immer zur Ablehnung der Antwort. Wenn die Unterstützung für die Ausstelleridentifikation angegeben ist,
wird die Antwort auch bei fehlendem `iss` abgelehnt. In beiden Fehlerfällen wird weder der Code eingelöst
noch auf einen anderen Callback zurückgegriffen. Auch eine fehlerhafte Callback-URL oder eine angegebene Unterstützung für die Ausstelleridentifikation
ohne Ausstellerangabe in den Metadaten führt weiterhin zum Abbruch. Siehe
[Nutzende authentifizieren](/plugins/build/auth).

Wenn der MCP-Server `scopes_supported` angibt, bevorzugt Codex bei der OAuth-Anmeldung die
vom Server angegebenen Scopes. Andernfalls greift Codex auf die
in `config.toml` konfigurierten Scopes zurück.

#### Registrierung von OAuth-Clients

Codex unterstützt [OAuth Client ID Metadata Documents (CIMD)](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)
und Dynamic Client Registration (DCR). Standardmäßig wählt Codex automatisch
CIMD, wenn der Autorisierungsserver
`client_id_metadata_document_supported: true` angibt, `none` in
`token_endpoint_auth_methods_supported` aufführt und der Callback eine unterstützte
Loopback-URL verwendet. Andernfalls verwendet Codex DCR, sofern verfügbar. Eine konfigurierte OAuth-Client-ID
hat immer Vorrang; in diesem Fall wird die Clientregistrierung übersprungen.

Für CIMD verwendet Codex ein von ChatGPT gehostetes Metadatendokument für den jeweiligen
MCP-Server:

```text
https://chatgpt.com/oauth/codex/<callback_id>/client.json

Codex leitet `<callback_id>` aus der URL des MCP-Servers ab und fügt die ID in die
Loopback-Weiterleitungs-URI ein, zum Beispiel
`http://127.0.0.1:<port>/callback/<callback_id>`. Das Metadatendokument registriert
die zugehörige Loopback-URI ohne Port. Autorisierungsserver müssen den bei der
Anmeldung gewählten Port akzeptieren und dabei Host und Pfad exakt abgleichen, wie in
[RFC 8252](https://www.rfc-editor.org/rfc/rfc8252.html#section-7.3) vorgeschrieben. Benutzerdefinierte
Callback-Hosts, Pfade oder Abfrageparameter erfordern DCR oder eine konfigurierte
OAuth-Client-ID.

Die Unterstützung für ein stabiles, gemeinsam genutztes CIMD-Dokument wird derzeit entwickelt und ist bald verfügbar:

```text
https://chatgpt.com/oauth/codex/client.json

Codex wird das stabile Dokument mit dem gemeinsam genutzten Pfad `/callback` verwenden, wenn der
Autorisierungsserver
`authorization_response_iss_parameter_supported: true` angibt, in seinen Metadaten einen gültigen
`issuer` bereitstellt und in seinen Autorisierungsantworten einen passenden Wert für `iss`
angibt. Server, deren Antworten nicht an einen Aussteller gebunden sind, werden weiterhin das
für den jeweiligen Callback vorgesehene Dokument verwenden.

Um für eine einzelne CLI-Anmeldung eine Registrierungsmethode auszuwählen, verwende
`--oauth-client-registration`:

```bash
codex mcp login <server-name> --oauth-client-registration cimd
codex mcp login <server-name> --oauth-client-registration dcr

Der Standardwert ist `auto`. Die gewählte Registrierungsmethode gilt nur für die aktuelle Anmeldung und
wird nicht in `config.toml` gespeichert.

#### Beispiele für config.toml

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env_vars = ["LOCAL_TOKEN"]

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"

```toml
# Optional MCP OAuth callback overrides (used by `codex mcp login`)
mcp_oauth_callback_port = 5555
mcp_oauth_callback_url = "https://devbox.example.internal/callback"

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }

```toml
[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
enabled_tools = ["open", "screenshot"]
disabled_tools = ["screenshot"] # applied after enabled_tools
default_tools_approval_mode = "prompt"
startup_timeout_sec = 20
tool_timeout_sec = 45
enabled = true

[mcp_servers.chrome_devtools.tools.open]
approval_mode = "approve"
output_token_limit = 30000

### Von Plug-ins bereitgestellte MCP-Server

Installierte Plug-ins können MCP-Server in ihrem Plug-in-Manifest bündeln. Diese
Server werden über das Plug-in gestartet. Deshalb legt die Benutzerkonfiguration ihren
Transportbefehl nicht fest. Den Aktivierungsstatus und die Richtlinie für Tools kannst du in der Benutzerkonfiguration weiterhin
unter `plugins.<plugin>.mcp_servers.<server>` steuern.

```toml
[plugins."sample@test".mcp_servers.sample]
enabled = true
default_tools_approval_mode = "prompt"
enabled_tools = ["read", "search"]

[plugins."sample@test".mcp_servers.sample.tools.search]
approval_mode = "approve"

Von Plug-ins bereitgestellte HTTP-MCP-Server können auch OAuth-Einstellungen in `.mcp.json` deklarieren.
Plug-in-Manifeste verwenden die Feldnamen `clientId`, `callbackUrl` und
`callbackPort` in camelCase-Schreibweise:

```json
{
  "mcpServers": {
    "sample": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "clientId": "my-pre-registered-client",
        "callbackUrl": "http://127.0.0.1/callback/registered"
      }
    }
  }
}

Für von Plug-ins bereitgestellte MCP-Server gelten dieselben Regeln zur Callback-Auswahl wie für andere
MCP-Server. Wenn ein Plug-in eine `clientId` bereitstellt, sein Anbieter keine an den Aussteller gebundenen
Callbacks unterstützt und `callbackUrl` die serverspezifische Callback-ID
nicht enthält, ignoriert Codex diese URL bei der Anmeldung und verwendet `mcp_oauth_callback_url` oder,
falls diese Einstellung nicht gesetzt ist, `http://127.0.0.1/callback`, jeweils mit angehängter Callback-ID.
Die konfigurierte `callbackUrl` bleibt unverändert.

`oauth.callbackPort` eines Plug-ins überschreibt die globale Einstellung
`mcp_oauth_callback_port`. Ist keine der beiden Einstellungen gesetzt, wählt Codex einen dynamisch zugewiesenen Port.
Der in `callbackUrl` enthaltene Port legt den Listener-Port nicht fest. Konfiguriere für einen
direkten Loopback-Callback mit festem Port beide Werte so, dass sie übereinstimmen:

```json
{
  "callbackUrl": "http://127.0.0.1:4321/callback/registered",
  "callbackPort": 4321
}

Bei Remote-Ingress oder einem anderen Proxy können der Port der Callback-URL und der lokale Listener-Port
bewusst voneinander abweichen, wenn der Proxy an den konfigurierten
Listener weiterleitet.

## Beispiele für nützliche MCP-Server

Die Liste der MCP-Server wächst stetig. Hier sind einige gängige Beispiele:

- [OpenAI Docs MCP](/learn/docs-mcp): Die Entwicklerdokumentation von OpenAI durchsuchen und lesen.
- [Context7](https://github.com/upstash/context7): Eine Verbindung zu aktueller Entwicklerdokumentation herstellen.
- Figma [Lokal](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) und [Remote](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/): Auf deine Figma-Designs zugreifen.
- [Playwright](https://www.npmjs.com/package/@playwright/mcp): Einen Browser mit Playwright steuern und untersuchen.
- [Chrome Developer Tools](https://github.com/ChromeDevTools/chrome-devtools-mcp/): Chrome steuern und untersuchen.
- [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex): Auf Sentry-Protokolle zugreifen.
- [GitHub](https://github.com/github/github-mcp-server): Verwalte GitHub auch über den Funktionsumfang von `git` hinaus (zum Beispiel Pull Requests und Issues).
