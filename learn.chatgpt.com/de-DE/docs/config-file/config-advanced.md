<!-- source: https://learn.chatgpt.com/de-DE/docs/config-file/config-advanced -->

Verwende diese Optionen, wenn du mehr Kontrolle über Anbieter, Richtlinien und Integrationen benötigst. Einen schnellen Einstieg findest du unter [Grundlagen der Konfiguration](/de-DE/codex/config-file/config-basic).

Hintergrundinformationen zu Projektanweisungen, wiederverwendbaren Funktionen, benutzerdefinierten Slash-Befehlen, Arbeitsabläufen mit Subagenten und Integrationen findest du unter [Anpassung](/de-DE/codex/customization/overview). Die Konfigurationsschlüssel findest du in der [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference).

## Profile

Mit Profilen kannst du benannte Konfigurationsebenen speichern und über
die CLI zwischen ihnen wechseln. Übergibst du `--profile profile-name`, lädt Codex
zunächst `~/.codex/config.toml` und überlagert diese Konfiguration anschließend mit `~/.codex/profile-name.config.toml`.
Profilnamen können Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten.

Erstelle für jedes Profil eine separate TOML-Datei. Verwende in der
Profildatei Konfigurationsschlüssel auf oberster Ebene. Verschachtele sie nicht unter `[profiles.profile-name]`.

```toml
# ~/.codex/deep-review.config.toml
model = "gpt-5.5"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
model_catalog_json = "/Users/me/.codex/model-catalogs/deep-review.json"

```shell
codex --profile deep-review
codex exec --profile deep-review "review this change"

Die Profildatei ist eine Konfigurationsebene über deiner grundlegenden Benutzerkonfiguration und unter der
Projekt- und CLI-Konfiguration. Sie muss deshalb nur die Werte enthalten, die von deiner
Basiskonfiguration abweichen. Profildateien können auch `model_catalog_json` überschreiben. Wenn beide Dateien diesen Wert festlegen, verwendet Codex den
Wert aus der Profildatei.

Ab Codex 0.134.0 liest `--profile` `[profiles.profile-name]` nicht mehr
aus `config.toml`, und der Selektor `profile = "profile-name"` auf oberster Ebene wird nicht
mehr unterstützt. Verschiebe bisherige Profileinstellungen nach
`~/.codex/profile-name.config.toml`. Entferne anschließend die entsprechende Tabelle
`[profiles.profile-name]` sowie den Selektor `profile = "profile-name"` aus
`config.toml`.

## Einmalige Überschreibungen über die CLI

Neben der Bearbeitung von `~/.codex/config.toml` kannst du die Konfiguration für einen einzelnen Lauf über die CLI überschreiben:

- Verwende nach Möglichkeit dedizierte Flags, zum Beispiel `--model`.
- Verwende `-c` / `--config`, wenn du einen beliebigen Schlüssel überschreiben musst.

Beispiele:

```shell
# Dedicated flag
codex --model gpt-5.6-terra

# Generic key/value override (value is TOML, not JSON)
codex --config model='"gpt-5.6-terra"'
codex --config sandbox_workspace_write.network_access=true
codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'

Hinweise:

- Schlüssel können in Punktnotation angegeben werden, um verschachtelte Werte festzulegen, zum Beispiel `mcp_servers.context7.enabled=false`.
- Werte für `--config` werden als TOML geparst. Setze den Wert im Zweifelsfall in Anführungszeichen, damit deine Shell ihn nicht an Leerzeichen aufteilt.
- Wenn sich der Wert nicht als TOML parsen lässt, behandelt Codex ihn als Zeichenfolge.

## Speicherorte für Konfiguration und Statusdaten

Codex speichert seine lokalen Statusdaten unter `CODEX_HOME`, standardmäßig unter `~/.codex`.

Dort findest du häufig folgende Dateien:

- `config.toml` (deine lokale Konfiguration)
- `auth.json` (wenn du Anmeldedaten dateibasiert speicherst) oder der Schlüsselbund beziehungsweise Schlüsselring deines Betriebssystems
- `history.jsonl` (wenn die dauerhafte Speicherung des Verlaufs aktiviert ist)
- Weitere benutzerspezifische Statusdaten, etwa Protokolle und Caches

Details zur Authentifizierung, einschließlich der Modi zur Speicherung von Anmeldedaten, findest du unter [Authentifizierung](/de-DE/codex/auth). Die vollständige Liste der Konfigurationsschlüssel findest du in der [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference).

Informationen zu gemeinsam genutzten Standardwerten, Regeln und Skills, die in Repositorys oder Systempfaden hinterlegt sind, findest du unter [Teamkonfiguration](/de-DE/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config).

Wenn du den integrierten OpenAI-Anbieter lediglich auf einen LLM-Proxy, einen Router oder ein Projekt mit aktivierter Datenresidenz verweisen lassen möchtest, lege `openai_base_url` in `config.toml` fest, statt einen neuen Anbieter zu definieren. Dadurch änderst du die Basis-URL des integrierten Anbieters `openai`, ohne einen separaten Eintrag für `model_providers.<id>` erstellen zu müssen.

```toml
openai_base_url = "https://us.api.openai.com/v1"

## Projektkonfigurationsdateien (`.codex/config.toml`)

Zusätzlich zu deiner Benutzerkonfiguration liest Codex projektspezifische Überschreibungen aus `.codex/config.toml`-Dateien in deinem Repository. Codex durchsucht den Pfad vom Projektstammverzeichnis bis zu deinem aktuellen Arbeitsverzeichnis und lädt jede gefundene Datei `.codex/config.toml`. Wenn mehrere Dateien denselben Schlüssel definieren, hat die Datei Vorrang, die deinem Arbeitsverzeichnis am nächsten liegt.

Aus Sicherheitsgründen lädt Codex projektspezifische Konfigurationsdateien nur, wenn das Projekt als vertrauenswürdig eingestuft ist. Bei einem nicht vertrauenswürdigen Projekt ignoriert Codex die projektspezifischen Ebenen unter `.codex/`, einschließlich `.codex/config.toml`, projektlokaler Hooks und projektlokaler Regeln. Benutzer- und Systemebenen bleiben davon unabhängig und werden weiterhin geladen.

Relative Pfade in einer Projektkonfiguration, zum Beispiel `model_instructions_file`, werden relativ zum Ordner `.codex/` aufgelöst, in dem sich `config.toml` befindet.

Projektkonfigurationsdateien können keine Einstellungen überschreiben, die Anmeldedaten umleiten,
vom Host verwaltete Metadaten von App-Anfragen ändern, die Authentifizierung von Anbietern ändern,
Konfigurationsprofile auswählen oder auf dem Rechner Befehle für Benachrichtigungen oder Telemetrie ausführen. Codex ignoriert die
folgenden Schlüssel in der projektlokalen Datei `.codex/config.toml` und gibt beim Start eine
Warnung aus, wenn sie vorhanden sind: `openai_base_url`, `chatgpt_base_url`,
`apps_mcp_product_sku`, `model_provider`, `model_providers`, `notify`,
`profile`, `profiles`, `experimental_realtime_ws_base_url` und `otel`. Lege Schlüssel für
Anbieter, Benachrichtigungen und Telemetrie auf Benutzerebene in
`~/.codex/config.toml` fest. Wähle Konfigurationsprofile mit `--profile profile-name`
und `~/.codex/profile-name.config.toml` aus.

## Hooks

Codex kann Lifecycle-Hooks außerdem aus `hooks.json`-Dateien oder direkt aus
`[hooks]`-Tabellen in `config.toml`-Dateien laden, die neben aktiven Konfigurationsebenen liegen.

In der Praxis sind die folgenden vier Speicherorte am nützlichsten:

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

Projektlokale Hooks werden nur geladen, wenn die `.codex/`-Ebene des Projekts als vertrauenswürdig eingestuft ist.
Hooks auf Benutzerebene sind unabhängig vom Vertrauensstatus des Projekts.

Inline-TOML-Hooks verwenden dieselbe Ereignisstruktur wie `hooks.json`:

```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

Wenn eine einzelne Ebene sowohl `hooks.json` als auch die Inline-Tabelle `[hooks]` enthält, lädt Codex
beides und gibt eine Warnung aus. Verwende pro Ebene möglichst nur eine Darstellungsform.

Die aktuelle Ereignisliste sowie Informationen zu Eingabefeldern, Ausgabeverhalten und Einschränkungen findest du unter
[Hooks](/de-DE/codex/hooks).

## Agentenrollen (`[agents]` in `config.toml`)

Informationen zur Konfiguration von Rollen für Subagenten (`[agents]` in `config.toml`) findest du unter [Subagenten](/de-DE/codex/agent-configuration/subagents).

## Erkennung des Projektstammverzeichnisses

Codex ermittelt die Projektkonfiguration, beispielsweise Ebenen unter `.codex/` und `AGENTS.md`, indem es die Verzeichnishierarchie ausgehend vom Arbeitsverzeichnis nach oben durchsucht, bis es ein Projektstammverzeichnis erreicht.

Codex betrachtet standardmäßig ein Verzeichnis, das `.git` enthält, als Projektstammverzeichnis. Lege zum Anpassen dieses Verhaltens `project_root_markers` in `config.toml` fest:

```toml
# Treat a directory as the project root when it contains any of these markers.
project_root_markers = [".git", ".hg", ".sl"]

Lege `project_root_markers = []` fest, um die Suche in übergeordneten Verzeichnissen zu überspringen und das aktuelle Arbeitsverzeichnis als Projektstammverzeichnis zu verwenden.

## Benutzerdefinierte Modellanbieter

Ein Modellanbieter legt fest, wie Codex eine Verbindung zu einem Modell herstellt: über die Basis-URL, die Wire-API, die Authentifizierung und optionale HTTP-Header. Benutzerdefinierte Anbieter können die reservierten IDs integrierter Anbieter nicht wiederverwenden: `openai`, `ollama` und `lmstudio`.

Definiere zusätzliche Anbieter und lege mit `model_provider` fest, welcher verwendet wird:

```toml
model = "gpt-5.6-terra"
model_provider = "proxy"

[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "http://proxy.example.com"
env_key = "OPENAI_API_KEY"

[model_providers.local_ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"

[model_providers.mistral]
name = "Mistral"
base_url = "https://api.mistral.ai/v1"
env_key = "MISTRAL_API_KEY"

Wenn ein benutzerdefinierter Anbieter den eigenständigen Endpunkt für die Websuche unterstützt, gib
diese Funktion in seiner Anbieterkonfiguration an:

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
env_key = "OPENAI_API_KEY"
supports_standalone_web_search = true

Für benutzerdefinierte Anbieter ist die Einstellung standardmäßig `false`. Die eigenständige Websuche befindet sich
in Entwicklung und ist standardmäßig deaktiviert. Auch wenn du die Anbieterfunktion auf `true`
setzt, wird sie nicht aktiviert: Der Anbieter muss einen kompatiblen Endpunkt unterstützen,
und sowohl das ausgewählte Modell als auch die Laufzeit müssen die eigenständige Suche unterstützen. Der
konfigurierte [Modus für `web_search`](/de-DE/codex/web-search) und
verwaltete Suchbeschränkungen gelten weiterhin.

Füge bei Bedarf Anfrage-Header hinzu:

```toml
[model_providers.example]
http_headers = { "X-Example-Header" = "example-value" }
env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }

Verwende eine befehlsbasierte Authentifizierung, wenn Codex für einen Anbieter Bearer-Token über ein externes Hilfsprogramm für Anmeldedaten abrufen muss:

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
wire_api = "responses"

[model_providers.proxy.auth]
command = "/usr/local/bin/fetch-codex-token"
args = ["--audience", "codex"]
timeout_ms = 5000
refresh_interval_ms = 300000

Der Authentifizierungsbefehl erhält keine Eingabe über `stdin` und muss das Token über stdout ausgeben. Codex entfernt Leerraumzeichen am Anfang und Ende, behandelt ein leeres Token als Fehler und aktualisiert es proaktiv im Intervall `refresh_interval_ms`. Lege `refresh_interval_ms = 0` fest, damit die Aktualisierung erst nach einem erneuten Authentifizierungsversuch erfolgt. Kombiniere `[model_providers.<id>.auth]` nicht mit `env_key`, `experimental_bearer_token` oder `requires_openai_auth`.

### Anbieter für Amazon Bedrock

Codex enthält den integrierten Modellanbieter `amazon-bedrock`. Lege ihn direkt als Wert für
`model_provider` fest. Anders als benutzerdefinierte Anbieter unterstützt dieser integrierte Anbieter nur
verschachtelte Überschreibungen für das AWS-Profil und die AWS-Region.

```toml
model_provider = "amazon-bedrock"
model = "<bedrock-model-id>"

[model_providers.amazon-bedrock.aws]
profile = "default"
region = "eu-central-1"

Wenn du `profile` nicht angibst, verwendet Codex die Standardkette für AWS-Anmeldedaten. Setze
`region` auf die unterstützte Bedrock-Region, die Anfragen verarbeiten soll.

Informationen zum vollständigen Setup-Ablauf, zu Authentifizierungsoptionen, unterstützten Modellen und zur
Verfügbarkeit von Funktionen findest du unter [ChatGPT Work und Codex
mit Amazon Bedrock verwenden](/de-DE/codex/amazon-bedrock).

## OSS-Modus (lokale Anbieter)

Codex kann mit einem lokalen „Open Source“-Anbieter wie
Ollama oder LM Studio arbeiten, wenn du `--oss` übergibst. Wähle mit
`--local-provider` einen Anbieter für einen einzelnen Lauf aus oder lege `oss_provider` als Standard fest. Wenn keine der beiden Optionen festgelegt ist, fordert dich die
interaktive CLI zur Auswahl auf; `codex exec` wird mit einem Fehler beendet.

```toml
# Default local provider used with `--oss`
oss_provider = "ollama" # or "lmstudio"

## Azure-Anbieter und anbieterspezifische Einstellungen

```toml
[model_providers.azure]
name = "Azure"
base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
env_key = "AZURE_OPENAI_API_KEY"
query_params = { api-version = "2025-04-01-preview" }
wire_api = "responses"
request_max_retries = 4
stream_max_retries = 10
stream_idle_timeout_ms = 300000

Verwende `openai_base_url`, um die Basis-URL des integrierten OpenAI-Anbieters zu ändern. Erstelle nicht `[model_providers.openai]`, da sich die IDs integrierter Anbieter nicht überschreiben lassen.

## API-Organisationen mit Datenresidenz

Für Projekte, die mit aktivierter [Datenresidenz](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt) erstellt wurden, kannst du einen Modellanbieter erstellen, um `base_url` mit dem [richtigen Präfix](/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency) zu aktualisieren. Für ChatGPT-Workspaces mit Datenresidenz ist kein benutzerdefinierter Anbieter erforderlich: Wenn du dich mit ChatGPT anmeldest, berücksichtigt Codex die Einstellungen des Workspace zur Datenresidenz.

```toml
model_provider = "openaidr"
[model_providers.openaidr]
name = "OpenAI Data Residency"
base_url = "https://us.api.openai.com/v1" # Replace 'us' with domain prefix

## Reasoning-Aufwand, Ausführlichkeit und Grenzwerte des Modells

```toml
model_reasoning_summary = "none"          # Disable summaries
model_verbosity = "low"                   # Shorten responses
model_supports_reasoning_summaries = true # Force reasoning
model_context_window = 128000             # Context window size

`model_verbosity` gilt nur für Anbieter, die die Responses API verwenden. Anbieter für Chat Completions ignorieren diese Einstellung.

## Genehmigungsrichtlinien und Sandbox-Modi

Lege fest, wie streng Genehmigungen gehandhabt werden (das beeinflusst, wann Codex pausiert), und wähle die Sandbox-Stufe (sie beeinflusst den Datei- und Netzwerkzugriff).

Praktische Hinweise, die du beim Bearbeiten von `config.toml` beachten solltest, findest du unter [Gängige Kombinationen aus Sandbox und Genehmigung](/de-DE/codex/agent-approvals-security#common-sandbox-and-approval-combinations), [Geschützte Pfade in beschreibbaren Stammverzeichnissen](/de-DE/codex/agent-approvals-security#protected-paths-in-writable-roots) und [Netzwerkzugriff](/de-DE/codex/agent-approvals-security#network-access).

Informationen zu Beta-Berechtigungsprofilen, mit denen du den Dateisystem- und Netzwerkzugriff gemeinsam konfigurierst, findest du unter [Berechtigungen](/de-DE/codex/permissions).

Mit einer granularen Genehmigungsrichtlinie (`approval_policy = { granular = { ... } }`) kannst du außerdem einzelne Prompt-Kategorien zulassen oder automatisch ablehnen. Das ist hilfreich, wenn du in einigen Fällen wie gewohnt interaktive Genehmigungen verwenden möchtest, andere jedoch, etwa `request_permissions` oder Prompts für Skill-Skripte, automatisch nach dem Fail-Closed-Prinzip abgelehnt werden sollen.

Setze `approvals_reviewer = "auto_review"`, um geeignete interaktive
Genehmigungsanfragen an die automatische Überprüfung weiterzuleiten. Das ändert die Prüfinstanz, aber nicht die
Sandbox-Grenze.

Verwende `[auto_review].policy` für lokale Richtlinienanweisungen an die Prüfinstanz. Die verwaltete Konfiguration
`guardian_policy_config` hat Vorrang.

```toml
approval_policy = "untrusted"   # Other options: on-request, never, or { granular = { ... } }
approvals_reviewer = "user"     # Or "auto_review" for automatic review
sandbox_mode = "workspace-write"
allow_login_shell = false       # Optional hardening: disallow login shells for shell tools

# Example granular approval policy:
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

[sandbox_workspace_write]
exclude_tmpdir_env_var = false  # Allow $TMPDIR
exclude_slash_tmp = false       # Allow /tmp
writable_roots = ["/Users/YOU/.pyenv/shims"]
network_access = false          # Opt in to outbound network

[auto_review]
policy = """
Use your organization's automatic review policy.
"""

### Benannte Berechtigungsprofile

Informationen zu integrierten Profilen, zur Syntax benutzerdefinierter Profile und zum vollständigen Konfigurationsmodell für Dateisystem und
Netzwerk findest du unter [Berechtigungen](/de-DE/codex/permissions).

Die vollständige Liste der Schlüssel und die in den Anforderungen festgelegten Einschränkungen findest du unter
[Konfigurationsreferenz](/de-DE/codex/config-file/config-reference) und
[Verwaltete Konfiguration](/de-DE/codex/enterprise/managed-configuration).

  Im Modus workspace-write gewähren manche Umgebungen für `.git/` und `.codex/`
  keinen Schreibzugriff, obwohl der restliche Workspace beschreibbar ist. Deshalb
  kann für Befehle wie `git commit` weiterhin eine Genehmigung erforderlich sein, um sie außerhalb der
  Sandbox auszuführen. Wenn du möchtest, dass Codex bestimmte Befehle überspringt, etwa indem es `git
  commit` außerhalb der Sandbox blockiert, verwende
<a href="/codex/agent-configuration/rules">Regeln</a>.

Deaktiviere Sandboxing vollständig (nur, wenn deine Umgebung Prozesse bereits isoliert):

```toml
sandbox_mode = "danger-full-access"

## Richtlinie für die Shell-Umgebung

`shell_environment_policy` steuert, welche Umgebungsvariablen Codex an
gestartete Befehle übergibt. Verwende `inherit = "none"`, um mit einer leeren Umgebung zu starten, oder
übernimm mit `inherit = "core"` eine reduzierte Auswahl. Füge explizite Werte und schlüsselbasierte
Filter hinzu, damit sensible Daten nicht unnötig an gestartete Befehle weitergegeben werden.

```toml
[shell_environment_policy]
inherit = "core"
set = { MY_FLAG = "1" }
ignore_default_excludes = false

[shell_environment_policy.filters]
"AWS_*" = "exclude"
"AZURE_*" = "exclude"

Bei Filtermustern wird die Groß- und Kleinschreibung nicht berücksichtigt; sie unterstützen `*` und `?`. Verwende `"exclude"`,
um übereinstimmende Variablen zu entfernen. Sobald ein Muster `"include"` verwendet, behält Codex
nur Variablen bei, die einem Include-Muster entsprechen. Include-Muster nehmen bereits ausgeschlossene Variablen
nicht wieder auf. Filterschlüssel werden ohne Berücksichtigung der Groß- und Kleinschreibung über
Konfigurationsebenen hinweg zusammengeführt.

`ignore_default_excludes` ist standardmäßig auf `true` gesetzt. Daher entfernt Codex nicht automatisch
Variablennamen, die `KEY`, `SECRET` oder `TOKEN` enthalten. Setze die Option auf `false`,
damit diese automatischen Ausschlüsse angewendet werden, bevor deine expliziten Filter greifen.

Codex wendet zuerst automatische Ausschlüsse an, dann benutzerdefinierte Ausschlüsse, anschließend Werte aus
`set` und zuletzt die Zulassungsliste für Include-Muster. Da `set` nach
den Ausschlüssen angewendet wird, kann es eine ausgeschlossene Variable wiederherstellen. Die Zulassungsliste für Include-Muster
kann den wiederhergestellten Wert dennoch entfernen.

Die älteren Arrays `exclude` und `include_only` werden für bestehende
Konfigurationen weiterhin unterstützt. Kombiniere keines der Arrays in derselben Konfigurationsebene mit
`[shell_environment_policy.filters]`; Codex
lehnt diese Kombination ab.

## MCP-Server

Weitere Details zur Konfiguration findest du in der separaten [MCP-Dokumentation](/de-DE/codex/extend/mcp).

## Observability und Telemetrie

Aktiviere den Protokollexport mit OpenTelemetry (OTel), um Codex-Ausführungen zu verfolgen (API-Anfragen, SSE-Ereignisse, Prompts sowie Genehmigungen und Ergebnisse von Tools). Die Funktion ist standardmäßig deaktiviert. Aktiviere sie über `[otel]`:

```toml
[otel]
environment = "staging"   # defaults to "dev"
exporter = "none"         # set to otlp-http or otlp-grpc to send events
log_user_prompt = false   # redact user prompts unless explicitly enabled

Wähle einen Exporter aus:

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}

Mit `exporter = "none"` zeichnet Codex Ereignisse auf, sendet jedoch nichts. Exporter bündeln Daten asynchron und leeren beim Beenden ihre Puffer. Ereignismetadaten umfassen den Dienstnamen, die CLI-Version, das Umgebungs-Tag, die Konversations-ID, das Modell, Sandbox- und Genehmigungseinstellungen sowie ereignisspezifische Felder (siehe [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference)).

### Ausgegebene Ereignisse

Codex gibt strukturierte Protokollereignisse für Ausführungen und die Nutzung von Tools aus. Beispiele für Ereignistypen sind:

- `codex.conversation_starts` (Modell, Einstellungen für den Reasoning-Aufwand, Sandbox- und Genehmigungsrichtlinien)
- `codex.api_request` (Versuch, Status/Erfolg, Dauer und Fehlerdetails)
- `codex.sse_event` (Art des Stream-Ereignisses, Erfolg/Fehlschlag, Dauer sowie Token-Anzahlen bei `response.completed`)
- `codex.websocket_request` und `codex.websocket_event` (Anfragedauer sowie Art, Erfolg und Fehler je Nachricht)
- `codex.user_prompt` (Länge; Inhalt wird unkenntlich gemacht, sofern seine Erfassung nicht ausdrücklich aktiviert ist)
- `codex.tool_decision` (genehmigt/abgelehnt und ob die Entscheidung aus der Konfiguration oder von Nutzenden stammt)
- `codex.tool_result` (Dauer, Erfolg, Ausgabeausschnitt)

### Ausgegebene OTel-Metriken

Wenn die OTel-Pipeline für Metriken aktiviert ist, gibt Codex Zähler und Histogramme zur Dauer von API-, Stream- und Tool-Aktivitäten aus.

Jede der folgenden Metriken enthält außerdem diese Standard-Metadaten-Tags: `auth_mode`, `originator`, `session_source`, `model` und `app.version`.

| Metrik                                | Typ      | Felder              | Beschreibung                                                       |
| ------------------------------------- | --------- | ------------------- | ----------------------------------------------------------------- |
| `codex.api_request`                   | Zähler   | `status`, `success` | Anzahl der API-Anfragen nach HTTP-Status und Erfolg/Fehlschlag.             |
| `codex.api_request.duration_ms`       | Histogramm | `status`, `success` | Dauer von API-Anfragen in Millisekunden.                             |
| `codex.sse_event`                     | Zähler   | `kind`, `success`   | Anzahl der SSE-Ereignisse nach Ereignisart und Erfolg/Fehlschlag.                |
| `codex.sse_event.duration_ms`         | Histogramm | `kind`, `success`   | Verarbeitungsdauer von SSE-Ereignissen in Millisekunden.                    |
| `codex.websocket.request`             | Zähler   | `success`           | Anzahl der WebSocket-Anfragen nach Erfolg/Fehlschlag.                       |
| `codex.websocket.request.duration_ms` | Histogramm | `success`           | Dauer von WebSocket-Anfragen in Millisekunden.                       |
| `codex.websocket.event`               | Zähler   | `kind`, `success`   | Anzahl der WebSocket-Nachrichten und -Ereignisse nach Typ und Erfolg/Fehlschlag.        |
| `codex.websocket.event.duration_ms`   | Histogramm | `kind`, `success`   | Verarbeitungsdauer von WebSocket-Nachrichten und -Ereignissen in Millisekunden.      |
| `codex.tool.call`                     | Zähler   | `tool`, `success`   | Anzahl der Tool-Aufrufe, aufgeschlüsselt nach Tool-Name und Erfolg/Fehlschlag.           |
| `codex.tool.call.duration_ms`         | Histogramm | `tool`, `success`   | Ausführungsdauer von Tools in Millisekunden, aufgeschlüsselt nach Tool-Name und Ergebnis. |

Weitere Hinweise zu Sicherheit und Datenschutz bei der Telemetrie findest du unter [Sicherheit](/de-DE/codex/agent-approvals-security#monitoring-and-telemetry).

### Metriken

Standardmäßig sendet Codex regelmäßig eine geringe Menge an anonymen Nutzungs- und Zustandsdaten an OpenAI. Die Daten helfen dabei, Fehlfunktionen von Codex zu erkennen, und zeigen, welche Funktionen und Konfigurationsoptionen verwendet werden. So kann sich das Codex-Team auf die wichtigsten Bereiche konzentrieren. Diese Metriken enthalten keine personenbezogenen Daten (PII). Die Erfassung von Metriken erfolgt unabhängig vom OTel-Export von Logs und Traces.

Wenn du die Erfassung von Metriken in der ChatGPT-Desktop-App, der Codex CLI und der IDE-Erweiterung auf einem Computer vollständig deaktivieren möchtest, setze das Analytics-Flag in deiner Konfiguration:

```toml
[analytics]
enabled = false

Jede Metrik umfasst eigene Felder sowie die unten aufgeführten Standardkontextfelder.

#### Standardkontextfelder (für jedes Ereignis und jede Metrik)

- `auth_mode`: `swic` | `api` | `unknown`.
- `model`: Name des verwendeten Modells.
- `app.version`: Codex-Version.

#### Metrikkatalog

Jede Metrik enthält die erforderlichen Felder sowie die oben aufgeführten Standardkontextfelder. Die folgenden Metriknamen enthalten das Präfix `codex.` nicht.
Die meisten Metriknamen sind zentral in `codex-rs/otel/src/metrics/names.rs` definiert; auch funktionsspezifische Metriken, die außerhalb dieser Datei ausgegeben werden, sind hier aufgeführt.
Wenn eine Metrik das Feld `tool` enthält, gibt es das intern verwendete Tool an (zum Beispiel `apply_patch` oder `shell`). Das Feld enthält weder den tatsächlichen Shell-Befehl noch den Patch, den `codex` anzuwenden versucht.

#### Laufzeit und Modellkommunikation

| Metrik                                          | Typ      | Felder               | Beschreibung                                                  |
| ----------------------------------------------- | --------- | -------------------- | ------------------------------------------------------------ |
| `api_request`                                   | Zähler   | `status`, `success`  | Anzahl der API-Anfragen, aufgeschlüsselt nach HTTP-Status und Erfolg/Fehlschlag.        |
| `api_request.duration_ms`                       | Histogramm | `status`, `success`  | Dauer von API-Anfragen in Millisekunden.                        |
| `sse_event`                                     | Zähler   | `kind`, `success`    | Anzahl der SSE-Ereignisse, aufgeschlüsselt nach Ereignisart und Erfolg/Fehlschlag.           |
| `sse_event.duration_ms`                         | Histogramm | `kind`, `success`    | Verarbeitungsdauer von SSE-Ereignissen in Millisekunden.               |
| `websocket.request`                             | Zähler   | `success`            | Anzahl der WebSocket-Anfragen, aufgeschlüsselt nach Erfolg/Fehlschlag.                  |
| `websocket.request.duration_ms`                 | Histogramm | `success`            | Dauer von WebSocket-Anfragen in Millisekunden.                  |
| `websocket.event`                               | Zähler   | `kind`, `success`    | Anzahl der WebSocket-Nachrichten/-Ereignisse, aufgeschlüsselt nach Typ und Erfolg/Fehlschlag.   |
| `websocket.event.duration_ms`                   | Histogramm | `kind`, `success`    | Verarbeitungsdauer von WebSocket-Nachrichten/-Ereignissen in Millisekunden. |
| `responses_api_overhead.duration_ms`            | Histogramm |                      | Aus WebSocket-Antworten ermittelte Overhead-Dauer der Responses API.      |
| `responses_api_inference_time.duration_ms`      | Histogramm |                      | Aus WebSocket-Antworten ermittelte Inferenzdauer der Responses API.     |
| `responses_api_engine_iapi_ttft.duration_ms`    | Histogramm |                      | IAPI-Zeit bis zum ersten Token der Engine der Responses API.        |
| `responses_api_engine_service_ttft.duration_ms` | Histogramm |                      | Service-Zeit bis zum ersten Token der Engine der Responses API.     |
| `responses_api_engine_iapi_tbt.duration_ms`     | Histogramm |                      | IAPI-Zeit zwischen Tokens der Engine der Responses API.         |
| `responses_api_engine_service_tbt.duration_ms`  | Histogramm |                      | Service-Zeit zwischen Tokens der Engine der Responses API.      |
| `transport.fallback_to_http`                    | Zähler   | `from_wire_api`      | Anzahl der Fallbacks von WebSocket auf HTTP.                            |
| `remote_models.fetch_update.duration_ms`        | Histogramm |                      | Dauer des Abrufs von Remote-Modelldefinitionen.                      |
| `remote_models.load_cache.duration_ms`          | Histogramm |                      | Ladedauer des Remote-Modellcaches.                         |
| `startup_prewarm.duration_ms`                   | Histogramm | `status`             | Dauer der Vorwärmung beim Start, aufgeschlüsselt nach Ergebnis.                         |
| `startup_prewarm.age_at_first_turn_ms`          | Histogramm | `status`             | Zeit seit Beginn der Vorabinitialisierung beim Start, wenn der erste tatsächliche Turn sie abschließt.    |
| `cloud_requirements.fetch.duration_ms`          | Histogramm |                      | Dauer des Abrufs der vom Workspace verwalteten Cloud-Anforderungen.         |
| `cloud_requirements.fetch_attempt`              | Zähler   | Siehe Hinweis             | Abrufversuche für die vom Workspace verwalteten Cloud-Anforderungen.         |
| `cloud_requirements.fetch_final`                | Zähler   | Siehe Hinweis             | Endgültiges Ergebnis des Abrufs der vom Workspace verwalteten Cloud-Anforderungen.    |
| `cloud_requirements.load`                       | Zähler   | `trigger`, `outcome` | Ergebnis des Ladens der vom Workspace verwalteten Cloud-Anforderungen.           |

Die Metrik `cloud_requirements.fetch_attempt` enthält die Felder `trigger`, `attempt`, `outcome` und `status_code`. Die Metrik `cloud_requirements.fetch_final` enthält die Felder `trigger`, `outcome`, `reason`, `attempt_count` und `status_code`.

#### Turn- und Tool-Aktivität

| Metrik                                 | Typ      | Felder                                                                    | Beschreibung                                                                                                      |
| -------------------------------------- | --------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `turn.e2e_duration_ms`                 | Histogramm |                                                                           | Gesamtdauer eines vollständigen Turns.                                                                                 |
| `turn.ttft.duration_ms`                | Histogramm |                                                                           | Zeit bis zum ersten Token eines Turns.                                                                                  |
| `turn.ttfm.duration_ms`                | Histogramm |                                                                           | Zeit bis zum ersten Ausgabeelement des Modells in einem Turn.                                                                      |
| `turn.network_proxy`                   | Zähler   | `active`, `tmp_mem_enabled`                                               | Ob der verwaltete Netzwerkproxy für den Turn aktiv war.                                                       |
| `turn.memory`                          | Zähler   | `read_allowed`, `feature_enabled`, `config_use_memories`, `has_citations` | Verfügbarkeit des Lesezugriffs auf Erinnerungen und Nutzung von Verweisen auf Erinnerungen pro Turn.                                                     |
| `turn.tool.call`                       | Histogramm | `tmp_mem_enabled`                                                         | Anzahl der Tool-Aufrufe im Turn.                                                                                |
| `turn.token_usage`                     | Histogramm | `token_type`, `tmp_mem_enabled`                                           | Token-Nutzung pro Turn nach Token-Typ (`total`, `input`, `cached_input`, `output` oder `reasoning_output`).          |
| `tool.call`                            | Zähler   | `tool`, `success`                                                         | Anzahl der Tool-Aufrufe nach Tool-Name sowie Erfolg oder Fehlschlag.                                                          |
| `tool.call.duration_ms`                | Histogramm | `tool`, `success`                                                         | Ausführungsdauer des Tools in Millisekunden nach Tool-Name und Ergebnis.                                                |
| `tool.unified_exec`                    | Zähler   | `tty`                                                                     | Aufrufe des vereinheitlichten exec-Tools nach TTY-Modus.                                                                             |
| `approval.requested`                   | Zähler   | `tool`, `approved`                                                        | Ergebnis der Genehmigungsanfrage für ein Tool (`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`). |
| `mcp.call`                             | Zähler   | Siehe Hinweis                                                                  | Ergebnis des Aufrufs eines MCP-Tools.                                                                                      |
| `mcp.call.duration_ms`                 | Histogramm | Siehe Hinweis                                                                  | Dauer des Aufrufs eines MCP-Tools.                                                                                    |
| `mcp.tools.list.duration_ms`           | Histogramm | `cache`                                                                   | Dauer der Auflistung von MCP-Tools einschließlich des Status für Cache-Treffer oder -Fehlzugriffe.                                                          |
| `mcp.tools.fetch_uncached.duration_ms` | Histogramm |                                                                           | Dauer des Abrufs von MCP-Tools bei fehlendem Cache-Treffer.                                                                |
| `mcp.tools.cache_write.duration_ms`    | Histogramm |                                                                           | Dauer der Schreibvorgänge von Codex Apps in den MCP-Tool-Cache.                                                                    |
| `hooks.run`                            | Zähler   | `hook_name`, `source`, `status`                                           | Anzahl der Hook-Ausführungen nach Hook-Name, Quelle und Status.                                                                 |
| `hooks.run.duration_ms`                | Histogramm | `hook_name`, `source`, `status`                                           | Dauer der Hook-Ausführung in Millisekunden.                                                                               |

Die Metriken `mcp.call` und `mcp.call.duration_ms` enthalten `status`. Bei normalen Tool-Aufrufen enthalten die ausgegebenen Metriken außerdem `tool` sowie, sofern verfügbar, `connector_id` und `connector_name`. Bei blockierten MCP-Aufrufen von Codex Apps wird möglicherweise `mcp.call` nur mit `status` ausgegeben.

#### Threads, Aufgaben und Funktionen

| Metrik                            | Typ      | Felder                | Beschreibung                                                                      |
| --------------------------------- | --------- | --------------------- | -------------------------------------------------------------------------------- |
| `feature.state`                   | Zähler   | `feature`, `value`    | Werte für Funktionen, die von den Standardwerten abweichen (pro abweichendem Wert wird eine Zeile ausgegeben).         |
| `status_line`                     | Zähler   |                       | Sitzung mit konfigurierter Statuszeile gestartet.                                   |
| `model_warning`                   | Zähler   |                       | Warnung an das Modell gesendet.                                                       |
| `thread.started`                  | Zähler   | `is_git`              | Neuer Thread erstellt; erfasst wird, ob sich das Arbeitsverzeichnis in einem Git-Repository befindet.    |
| `conversation.turn.count`         | Zähler   |                       | Dialogbeiträge von Nutzenden und Assistent pro Thread, erfasst am Ende des Threads.              |
| `thread.fork`                     | Zähler   | `source`              | Neuer Thread durch Forken eines bestehenden Threads erstellt.                                |
| `thread.rename`                   | Zähler   |                       | Thread umbenannt.                                                                  |
| `thread.side`                     | Zähler   | `source`              | Nebenunterhaltung erstellt.                                                       |
| `thread.skills.enabled_total`     | Histogramm |                       | Anzahl der für einen neuen Thread aktivierten Skills.                                       |
| `thread.skills.kept_total`        | Histogramm |                       | Anzahl der aktivierten Skills, die nach dem Rendern des Prompts beibehalten wurden.                            |
| `thread.skills.truncated`         | Histogramm |                       | Ob beim Rendern der Skills die Liste der aktivierten Skills gekürzt wurde (`1` oder `0`).          |
| `task.compact`                    | Zähler   | `type`                | Anzahl manueller und automatischer Compactions (Kontextverdichtungen) je Typ (`remote` oder `local`). |
| `task.review`                     | Zähler   |                       | Anzahl der ausgelösten Reviews.                                                     |
| `task.undo`                       | Zähler   |                       | Anzahl der ausgelösten Aktionen zum Rückgängigmachen.                                                |
| `task.user_shell`                 | Zähler   |                       | Anzahl der Shell-Aktionen durch Nutzende (zum Beispiel `!` in der TUI).                       |
| `shell_snapshot`                  | Zähler   | Siehe Hinweis              | Ob ein Shell-Snapshot erfolgreich erstellt wurde.                                       |
| `shell_snapshot.duration_ms`      | Histogramm | `success`             | Dauer der Erstellung eines Shell-Snapshots.                                                   |
| `skill.injected`                  | Zähler   | `status`, `skill`     | Ergebnisse der Skill-Injektion nach Skill.                                               |
| `plugins.startup_sync`            | Zähler   | `transport`, `status` | Synchronisierungsversuche für kuratierte Plug-ins beim Start.                                            |
| `plugins.startup_sync.final`      | Zähler   | `transport`, `status` | Endergebnis der Synchronisierung kuratierter Plug-ins beim Start.                                       |
| `multi_agent.spawn`               | Zähler   | `role`                | Starts von Agenten nach Rolle.                                                            |
| `multi_agent.resume`              | Zähler   |                       | Wiederaufnahmen von Agenten.                                                                   |
| `multi_agent.nickname_pool_reset` | Zähler   |                       | Zurücksetzungen des Pools für Agenten-Spitznamen.                                                      |

Die Metrik `shell_snapshot` enthält `success` und bei Fehlern `failure_reason`.

#### Erinnerung und lokaler Zustand

| Metrik                         | Typ      | Felder                    | Beschreibung                                               |
| ------------------------------ | --------- | ------------------------- | --------------------------------------------------------- |
| `memory.phase1`                | Zähler   | `status`                  | Anzahl der Jobs in Erinnerungsphase 1 nach Status.                      |
| `memory.phase1.e2e_ms`         | Histogramm |                           | Gesamtdauer der Erinnerungsphase 1.                   |
| `memory.phase1.output`         | Zähler   |                           | In Erinnerungsphase 1 geschriebene Ausgaben.                           |
| `memory.phase1.token_usage`    | Histogramm | `token_type`              | Token-Nutzung in Erinnerungsphase 1 nach Token-Typ.                 |
| `memory.phase2`                | Zähler   | `status`                  | Anzahl der Jobs in Erinnerungsphase 2 nach Status.                      |
| `memory.phase2.e2e_ms`         | Histogramm |                           | Gesamtdauer der Erinnerungsphase 2.                   |
| `memory.phase2.input`          | Zähler   |                           | Anzahl der Eingaben für Erinnerungsphase 2.                               |
| `memory.phase2.token_usage`    | Histogramm | `token_type`              | Token-Nutzung in Erinnerungsphase 2 nach Token-Typ.                 |
| `memories.usage`               | Zähler   | `kind`, `tool`, `success` | Nutzung von Erinnerungen nach Art, Tool und Erfolg oder Fehlschlag.          |
| `external_agent_config.detect` | Zähler   | Siehe Hinweis                  | Erkannte externe Agentenkonfigurationen nach Typ des Migrationselements.  |
| `external_agent_config.import` | Zähler   | Siehe Hinweis                  | Importierte externe Agentenkonfigurationen nach Typ des Migrationselements.     |
| `db.backfill`                  | Zähler   | `status`                  | Ergebnisse der anfänglichen Nachbefüllung der Zustandsdatenbank (`upserted`, `failed`). |
| `db.backfill.duration_ms`      | Histogramm | `status`                  | Dauer der anfänglichen Nachbefüllung der Zustandsdatenbank.                |
| `db.error`                     | Zähler   | `stage`                   | Fehler bei Vorgängen in der Zustandsdatenbank.                        |

Die Metriken `external_agent_config.detect` und `external_agent_config.import` enthalten `migration_type`; Migrationen von Skills enthalten außerdem `skills_count`.

#### Windows-Sandbox

| Metrik                                           | Typ      | Felder                                    | Beschreibung                                           |
| ------------------------------------------------ | --------- | ----------------------------------------- | ----------------------------------------------------- |
| `windows_sandbox.setup_success`                  | Zähler   | `originator`, `mode`                      | Erfolgreiche Setups der Windows-Sandbox.                      |
| `windows_sandbox.setup_failure`                  | Zähler   | `originator`, `mode`                      | Fehlgeschlagene Setups der Windows-Sandbox.                       |
| `windows_sandbox.setup_duration_ms`              | Histogramm | `result`, `originator`, `mode`            | Dauer des Setups der Windows-Sandbox.                       |
| `windows_sandbox.elevated_setup_success`         | Zähler   |                                           | Erfolgreiche Setups der Windows-Sandbox mit erhöhten Rechten.             |
| `windows_sandbox.elevated_setup_failure`         | Zähler   | Siehe Hinweis                                  | Fehlgeschlagene Setups der Windows-Sandbox mit erhöhten Rechten.              |
| `windows_sandbox.elevated_setup_canceled`        | Zähler   | Siehe Hinweis                                  | Abgebrochene Versuche, die Windows-Sandbox mit erhöhten Rechten einzurichten.     |
| `windows_sandbox.elevated_setup_duration_ms`     | Histogramm | `result`                                  | Dauer des Setups der Windows-Sandbox mit erhöhten Rechten.              |
| `windows_sandbox.elevated_prompt_shown`          | Zähler   |                                           | Aufforderung zum Sandbox-Setup mit erhöhten Rechten wurde angezeigt.                  |
| `windows_sandbox.elevated_prompt_accept`         | Zähler   |                                           | Aufforderung zum Sandbox-Setup mit erhöhten Rechten wurde bestätigt.               |
| `windows_sandbox.elevated_prompt_use_legacy`     | Zähler   |                                           | In der Aufforderung zum Setup mit erhöhten Rechten wurde die Legacy-Sandbox ausgewählt.   |
| `windows_sandbox.elevated_prompt_quit`           | Zähler   |                                           | Der Vorgang wurde über die Aufforderung zum Setup mit erhöhten Rechten beendet.                   |
| `windows_sandbox.fallback_prompt_shown`          | Zähler   |                                           | Fallback-Dialog für die Sandbox angezeigt.                        |
| `windows_sandbox.fallback_retry_elevated`        | Zähler   |                                           | Setup mit erhöhten Rechten über den Fallback-Dialog erneut versucht. |
| `windows_sandbox.fallback_use_legacy`            | Zähler   |                                           | Legacy-Sandbox im Fallback-Dialog ausgewählt.   |
| `windows_sandbox.fallback_prompt_quit`           | Zähler   |                                           | Vorgang im Fallback-Dialog beendet.                   |
| `windows_sandbox.legacy_setup_preflight_failed`  | Zähler   | Siehe Hinweis                                  | Fehler bei der Vorabprüfung für das Setup der Legacy-Windows-Sandbox.       |
| `windows_sandbox.setup_elevated_sandbox_command` | Zähler   |                                           | Befehl für das Sandbox-Setup mit erhöhten Rechten aufgerufen.               |
| `windows_sandbox.createprocessasuserw_failed`    | Zähler   | `error_code`, `path_kind`, `exe`, `level` | Fehler bei `CreateProcessAsUserW` unter Windows.              |

Die Metriken zu Fehlern beim Setup mit erhöhten Rechten enthalten `code` und `message`, wenn Details zu Windows-Setup-Fehlern verfügbar sind. Wenn sie über den gemeinsamen Setup-Pfad ausgegeben werden, können sie außerdem `originator` enthalten. Die Metrik `windows_sandbox.legacy_setup_preflight_failed` enthält `originator`, wenn sie über den gemeinsamen Setup-Pfad ausgegeben wird. Bei Fehlern der Vorabprüfung im Fallback-Dialog sind jedoch möglicherweise keine Felder enthalten.

### Feedback-Einstellungen

In lokalen Clients kannst du standardmäßig über `/feedback` Feedback senden. Um die Feedbackerfassung in der ChatGPT-Desktop-App, der Codex CLI und der IDE-Erweiterung auf einem Computer zu deaktivieren, aktualisiere deine Konfiguration:

```toml
[feedback]
enabled = false

Wenn die Funktion deaktiviert ist, zeigt `/feedback` eine entsprechende Meldung an und Codex lehnt Feedbackübermittlungen ab.

### Reasoning-Ereignisse ausblenden oder anzeigen

Wenn du störende „Reasoning“-Ausgaben reduzieren möchtest (etwa in CI-Protokollen), kannst du sie unterdrücken:

```toml
hide_agent_reasoning = true

Wenn du Reasoning-Inhalte im Rohformat anzeigen möchtest, sobald ein Modell sie ausgibt:

```toml
show_raw_agent_reasoning = true

Aktiviere die Ausgabe von Reasoning-Inhalten im Rohformat nur, wenn das für deinen Ablauf vertretbar ist. Einige Modelle oder Anbieter (wie `gpt-oss`) geben keine Reasoning-Inhalte im Rohformat aus. In diesem Fall hat diese Einstellung keine sichtbare Wirkung.

## Benachrichtigungen

Mit `notify` kannst du ein externes Programm starten, wenn Codex ein unterstütztes Ereignis ausgibt (derzeit nur `agent-turn-complete`). Das eignet sich für Desktop-Benachrichtigungen, Chat-Webhooks, CI-Updates und andere Benachrichtigungen über separate Kanäle, die sich nicht mit den integrierten TUI-Benachrichtigungen umsetzen lassen.

```toml
notify = ["python3", "/path/to/notify.py"]

Beispiel für eine gekürzte Version von `notify.py`, die auf `agent-turn-complete` reagiert:

```python
#!/usr/bin/env python3

def main() -> int:
    notification = json.loads(sys.argv[1])
    if notification.get("type") != "agent-turn-complete":
        return 0
    title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
    message = " ".join(notification.get("input-messages", []))
    subprocess.check_output([
        "terminal-notifier",
        "-title", title,
        "-message", message,
        "-group", "codex-" + notification.get("thread-id", ""),
        "-activate", "com.googlecode.iterm2",
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())

Das Skript erhält ein einzelnes JSON-Argument. Häufig verwendete Felder sind:

- `type` (derzeit `agent-turn-complete`)
- `thread-id` (Sitzungskennung)
- `turn-id` (Interaktionskennung)
- `cwd` (Arbeitsverzeichnis)
- `input-messages` (Eingaben, die zu dieser Interaktion geführt haben)
- `last-assistant-message` (Text der letzten Assistentennachricht)

Speichere das Skript an einer beliebigen Stelle auf dem Datenträger und gib seinen Pfad in `notify` an.

#### `notify` und `tui.notifications` im Vergleich

- `notify` führt ein externes Programm aus (geeignet für Webhooks, Benachrichtigungsprogramme für den Desktop und CI-Hooks).
- `tui.notifications` ist in die TUI integriert und kann bei Bedarf nach Ereignistyp filtern (beispielsweise `agent-turn-complete` und `approval-requested`).
- Mit `tui.notification_method` legst du fest, wie die TUI Benachrichtigungen im Terminal ausgibt (`auto`, `osc9` oder `bel`).
- Mit `tui.notification_condition` legst du fest, ob TUI-Benachrichtigungen nur ausgelöst werden, wenn
  das Terminal nicht fokussiert ist (`unfocused`), oder immer (`always`).

Im Modus `auto` verwendet Codex bevorzugt OSC 9-Benachrichtigungen (eine Terminal-Escape-Sequenz, die einige Terminals als Desktop-Benachrichtigung interpretieren) und greift andernfalls auf BEL (`\x07`) zurück.

Die genauen Konfigurationsschlüssel findest du in der [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference).

## Verlaufsspeicherung

Standardmäßig speichert Codex lokale Sitzungsprotokolle unter `CODEX_HOME` (zum Beispiel `~/.codex/history.jsonl`). So deaktivierst du die lokale Verlaufsspeicherung:

```toml
[history]
persistence = "none"

Lege `history.max_bytes` fest, um die Größe der Verlaufsdatei zu begrenzen. Wenn die Datei den Grenzwert überschreitet, entfernt Codex die ältesten Einträge und kompaktiert die Datei, behält dabei aber die neuesten Einträge bei.

```toml
[history]
max_bytes = 104857600 # 100 MiB

## Anklickbare Dateiverweise

Wenn du eine Terminal- oder Editor-Integration verwendest, die dies unterstützt, kann Codex Dateiverweise als anklickbare Links darstellen. Konfiguriere `file_opener`, um das von Codex verwendete URI-Schema auszuwählen:

```toml
file_opener = "vscode" # or cursor, windsurf, vscode-insiders, none

Beispiel: Ein Verweis wie `/home/user/project/main.py:42` lässt sich in den anklickbaren Link `vscode://file/...:42` umwandeln.

## Projektanweisungen ermitteln

Codex liest `AGENTS.md` (und zugehörige Dateien) und berücksichtigt in der ersten Interaktion einer Sitzung nur einen begrenzten Teil der Projektanweisungen. Zwei Einstellungen steuern dieses Verhalten:

- `project_doc_max_bytes`: die maximale Datenmenge, die aus jeder Datei namens `AGENTS.md` gelesen wird
- `project_doc_fallback_filenames`: zusätzliche Dateinamen, nach denen gesucht wird, wenn `AGENTS.md` auf einer Verzeichnisebene fehlt

Eine ausführliche Anleitung findest du unter [Benutzerdefinierte Anweisungen mit AGENTS.md](/de-DE/codex/agent-configuration/agents-md).

## Desktop

Die Optionen in diesem Abschnitt gelten nur für die ChatGPT-Desktop-App.

### Benutzerdefinierte Datei-Handler hinzufügen

Füge in deiner benutzerspezifischen Konfigurationsdatei `~/.codex/config.toml` unter
`desktop.custom_file_handlers` Einträge hinzu, um Dateien in Editoren oder internen Startprogrammen zu öffnen,
die von der ChatGPT-Desktop-App standardmäßig nicht unterstützt werden. Jeder Eintrag fügt
den Menüs **Öffnen in** der App einen Editor hinzu. Die App zeigt das Ziel an, wenn
`command` ein vorhandener absoluter Pfad ist oder die App den Befehl über ihren `PATH` auflösen kann.

Das folgende Beispiel zeigt drei Möglichkeiten, eine Datei an einen Handler zu übergeben:

```toml
# Append the opened path directly after the command.
[desktop.custom_file_handlers.vscodium]
label = "VSCodium"
icon = "/Users/you/.codex/icons/vscodium.png"
command = "codium"

# Place fixed arguments before the opened path.
[desktop.custom_file_handlers.textedit]
label = "TextEdit"
icon = "/Users/you/.codex/icons/textedit.png"
command = "/usr/bin/open"
args = ["-a", "TextEdit"]

# Append one JSON argument with the path and editor context.
[desktop.custom_file_handlers.company_editor]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"
input = "json_argument"

Speichere `config.toml` und starte anschließend die ChatGPT-Desktop-App neu.

Die Handler-ID ist das letzte Segment der TOML-Tabellenüberschrift. Sie muss
1–64 Zeichen lang sein, mit einem ASCII-Buchstaben oder einer Ziffer beginnen und darf ansonsten
nur ASCII-Buchstaben, Ziffern, Punkte, Unterstriche oder Bindestriche enthalten. Die App stellt
die ID mit dem Präfix `custom:` bereit; beispielsweise wird `company_editor` zu
`custom:company_editor`. Setze eine ID, die einen Punkt enthält, in Anführungszeichen, damit TOML sie nicht
als verschachtelte Tabelle interpretiert. Beispiel:

```toml
[desktop.custom_file_handlers."company.editor"]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"

Jeder Handler unterstützt folgende Felder:

| Feld          | Erforderlich | Beschreibung                                                                                                                                                              |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `label`        | Ja      | Anzeigename in der App.                                                                                                                                                 |
| `icon`         | Ja      | Ein mitgeliefertes App-Symbol wie `apps/vscode.png`, eine Base64-URL im Format `data:image/...`, eine URI mit dem Schema `file:` oder ein absoluter lokaler Bildpfad. Bei einer nicht unterstützten Quelle wird das Standardsymbol von VS Code verwendet. |
| `command`      | Ja      | Pfad zur ausführbaren Datei oder Befehlsname zum Erkennen und Starten des Handlers.                                                                                                                    |
| `args`         | Nein       | String-Array, das zwischen `command` und der Dateieingabe eingefügt wird. Standardmäßig `[]`.                                                                                            |
| `input`        | Nein       | So übergibt die App die Dateieingabe: `path`, `json_argument` oder `json_stdin`. Standardmäßig `path`.                                                                              |
| `supports_ssh` | Nein       | Ob der Handler für Dateien in SSH-Workspaces angeboten wird. Standardmäßig `false`. Verwende `json_stdin`, wenn der Handler Angaben zu Remote-Host und Pfad benötigt.                     |

Der Wert von `input` legt fest, was nach `args` folgt:

- `path` hängt den Pfad als letztes Befehlsargument an.
- `json_argument` hängt ein JSON-Objekt mit `target`, `path`, `appPath` und
`location` an. Der Wert `location` ist entweder ein Objekt mit 1-basierten Werten für `line` und
`column` oder `null`.
- `json_stdin` schreibt das JSON-Objekt in die Standardeingabe, statt ein
  Argument hinzuzufügen. Das Objekt enthält außerdem `hostConfig`, `remoteWorkspaceRoot` und
`remotePath`; diese Felder haben den Wert `null`, wenn sie nicht relevant sind.

Zum Beispiel kann `company_editor` dieses Argument erhalten, wenn du eine
bestimmte Stelle im Quellcode öffnest:

```json
{
  "target": "custom:company_editor",
  "path": "/repo/src/index.ts",
  "appPath": null,
  "location": { "line": 12, "column": 3 }
}

Wenn du einen benutzerdefinierten Handler als bevorzugten Editor auswählst, wird diese Auswahl genauso
wie bei einem integrierten Editor gespeichert, einschließlich projektspezifischer Einstellungen.

## TUI-Optionen

Wenn du `codex` ohne Unterbefehl ausführst, wird die interaktive Terminal-Benutzeroberfläche (TUI) gestartet. Unter `[tui]` stellt Codex unter anderem folgende TUI-spezifische Konfigurationsoptionen bereit:

- `tui.notifications`: Benachrichtigungen aktivieren oder deaktivieren oder auf bestimmte Typen beschränken
- `tui.notification_method`: `auto`, `osc9` oder `bel` für Terminalbenachrichtigungen auswählen
- `tui.notification_condition`: Mit `unfocused` oder `always` festlegen, wann
  Benachrichtigungen ausgelöst werden
- `tui.animations`: ASCII-Animationen und Schimmereffekte aktivieren oder deaktivieren
- `tui.alternate_screen`: Nutzung des alternativen Bildschirms steuern (auf `never` setzen, damit der Scrollback des Terminals erhalten bleibt)
- `tui.show_tooltips`: Onboarding-Tooltips auf dem Begrüßungsbildschirm ein- oder ausblenden

`tui.notification_method` ist standardmäßig auf `auto` gesetzt. Im Modus `auto` bevorzugt Codex Benachrichtigungen über OSC 9 (eine Escape-Sequenz des Terminals, die manche Terminals als Desktopbenachrichtigung interpretieren), sofern das Terminal OSC 9 offenbar unterstützt. Andernfalls greift Codex auf BEL (`\x07`) zurück.

Die vollständige Liste der Konfigurationsschlüssel findest du in der [Konfigurationsreferenz](/de-DE/codex/config-file/config-reference).
