<!-- source: https://learn.chatgpt.com/de-DE/docs/hooks -->

Hooks sind ein Framework zur Erweiterung von Codex. Damit kannst du während der Agentenschleife Skripte oder MCP-Tools ausführen, etwa für folgende Aufgaben:

- Den Chat an ein eigenes System für Protokollierung oder Analyse senden
- Die Prompts deines Teams prüfen, um das versehentliche Einfügen von API-Schlüsseln zu verhindern
- Chats zusammenfassen, um automatisch dauerhafte Erinnerungen zu erstellen
- Eine eigene Validierungsprüfung ausführen, wenn eine Chat-Runde endet, um Standards durchzusetzen
- Die Formulierung von Prompts anpassen, wenn du in einem bestimmten Verzeichnis arbeitest

Beachte Folgendes zum Laufzeitverhalten:

- Alle passenden Hooks aus mehreren Dateien werden ausgeführt.
- Mehrere passende Befehls-Hooks für dasselbe Ereignis werden gleichzeitig gestartet. Daher kann kein Hook den Start eines anderen passenden Hooks verhindern.
- Nicht verwaltete Hooks müssen vor ihrer Ausführung überprüft und als vertrauenswürdig eingestuft werden.

Hooks werden zu verschiedenen Zeitpunkten einer Unterhaltung ausgeführt:

| Zeitpunkt                              | Hooks                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Während einer Runde                     | `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `UserPromptSubmit`, `SubagentStop`, `Stop` |
| Wenn du eine aktive Runde unterbrichst | `Interrupt` (wird für Subagenten nicht ausgeführt)                                                                                   |
| Beim Start einer Sitzung oder eines Subagenten | `SessionStart`, `SubagentStart`                                                                                           |
| Wenn der Haupt-Thread endet         | `SessionEnd` (wird für Subagenten nicht ausgeführt)                                                                                  |

## Wo Codex nach Hooks sucht

Codex sucht neben aktiven Konfigurationsebenen in einer der folgenden Formen nach Hooks:

- `hooks.json`
- direkt in `config.toml` definierte `[hooks]`-Tabellen

Installierte Plug-ins können auch die Konfiguration für den Lebenszyklus über ihr Plug-in-Manifest
oder die Standarddatei `hooks/hooks.json` mitliefern. Unter [Plug-ins
erstellen](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) findest du die
Regeln für die Paketierung von Plug-ins.

In der Praxis sind die folgenden vier Speicherorte am nützlichsten:

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

Wenn mehrere Hook-Quellen vorhanden sind, lädt Codex alle passenden Hooks.
Konfigurationsebenen mit höherer Priorität ersetzen keine Hooks aus Ebenen mit niedrigerer Priorität.
Wenn eine einzelne Ebene sowohl `hooks.json` als auch direkt eingebettete `[hooks]`-Tabellen enthält, führt Codex
beides zusammen und zeigt beim Start eine Warnung an. Verwende pro Ebene möglichst nur eine Darstellungsform.

Codex kann auch Hooks erkennen, die in aktivierten Plug-ins enthalten sind. Diese Hooks werden zusammen mit Hooks aus anderen Quellen geladen und durchlaufen dieselbe Vertrauensprüfung wie andere nicht verwaltete Hooks.

Projektlokale Hooks werden nur geladen, wenn die Projektebene `.codex/` als vertrauenswürdig gilt.
In nicht vertrauenswürdigen Projekten lädt Codex weiterhin Benutzer- und System-Hooks
aus den jeweils eigenen aktiven Konfigurationsebenen.

## Hooks überprüfen und als vertrauenswürdig einstufen

Codex listet die konfigurierten Hooks auf, bevor es entscheidet, welche ausgeführt werden dürfen. Bevor ein nicht verwalteter Hook ausgeführt werden kann, musst du seine genaue Definition überprüfen und als vertrauenswürdig einstufen. Codex bindet die Vertrauensentscheidung an den aktuellen Hash des Hooks. Neue oder geänderte Hooks werden deshalb zur Überprüfung markiert und übersprungen, bis du sie als vertrauenswürdig eingestuft hast.

Mit `/hooks` in der CLI kannst du Hook-Quellen einsehen, neue oder geänderte Hooks überprüfen,
Hooks als vertrauenswürdig einstufen oder einzelne nicht verwaltete Hooks deaktivieren. Wenn beim Start
Hooks überprüft werden müssen, gibt Codex eine Warnung aus, die dich auffordert, `/hooks` zu öffnen.

Verwaltete Hooks aus System-, MDM- oder Cloud-Quellen sowie aus `requirements.toml` werden als verwaltet gekennzeichnet.
Sie gelten aufgrund einer Richtlinie als vertrauenswürdig und können nicht über den benutzerseitigen Hook-Browser deaktiviert werden.

Für eine einmalige Automatisierung, die Hook-Quellen bereits außerhalb von Codex prüft, übergib
`--dangerously-bypass-hook-trust`. So führst du aktivierte Hooks bei diesem Aufruf aus, ohne dass dafür eine
dauerhaft gespeicherte Vertrauensentscheidung erforderlich ist.

## Struktur der Konfiguration

Hooks sind in drei Ebenen organisiert:

- Ein Hook-Ereignis wie `PreToolUse`, `PostToolUse`, `PreCompact`,
`SubagentStart` oder `Stop`
- Eine Matcher-Gruppe, die festlegt, wann sie für dieses Ereignis greift
- Ein oder mehrere Hook-Handler, die ausgeführt werden, wenn die Matcher-Gruppe greift

```json
{
  "description": "Optional lifecycle hooks for this workspace.",
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes",
            "additionalContextLimit": 5000
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_end.py",
            "timeout": 3
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/permission_request.py\"",
            "statusMessage": "Checking approval request"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
            "statusMessage": "Reviewing Bash output"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit_data_flywheel.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}

Hinweise:

- `description` ist ein optionales Metadatenfeld auf oberster Ebene einer `hooks.json`-Datei.
  Es beeinflusst nicht, welche Hooks ausgeführt werden.
- `timeout` wird in Sekunden angegeben.
- Wenn `timeout` fehlt, verwendet Codex für die meisten Hooks `600` Sekunden.
  - Für `SessionEnd` und `Interrupt` gilt standardmäßig `1` Sekunde; unterstützt werden bis zu `3` Sekunden.
- `statusMessage` ist optional.
- Mit `additionalContextLimit` legst du fest, wie viel Kontext ein Befehls-Hook über `additionalContext`
  an das Modell senden kann, bevor Codex den vollständigen Text auf dem Datenträger speichert
  und stattdessen eine kürzere Vorschau sendet. Siehe [Große Hook-Ausgaben](#large-hook-output).
- Mit `commandWindows` kannst du optional einen abweichenden Befehl festlegen, der nur unter Windows gilt. Verwende in TOML
`command_windows` oder `commandWindows`.
- Setze `async` auf `true`, um [einen Befehls-Hook im
  Hintergrund auszuführen](#run-hooks-in-the-background).
- Handler vom Typ `command` und `mcp_tool` werden unterstützt. Handler vom Typ `prompt` und `agent`
  werden geparst, aber übersprungen.
- Befehle verwenden das `cwd` der Sitzung als Arbeitsverzeichnis.
- Bei Hooks im Repository solltest du Pfade vom Git-Stammverzeichnis aus auflösen, statt einen
  relativen Pfad wie `.codex/hooks/...` zu verwenden. Codex kann aus einem Unterverzeichnis gestartet werden.
  Ein Pfad auf Basis des Git-Stammverzeichnisses verweist trotzdem auf denselben Speicherort des Hooks.

Die entsprechende Inline-TOML-Konfiguration in `config.toml`:

```toml
[[hooks.SessionStart]]
matcher = "^compact$"

[[hooks.SessionStart.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/session_start.py"'
additionalContextLimit = 5000

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
timeout = 30
statusMessage = "Reviewing Bash output"

## MCP-Tool-Hooks

Mit einem MCP-Tool-Hook kann ein Lebenszyklusereignis ein Tool auf einem bereits verbundenen MCP-Server aufrufen. Der Hook sendet strukturierte Argumente direkt an das Tool. Für ihn gelten dieselbe Vertrauensprüfung und dieselben Ausgabevorgaben wie für einen Befehls-Hook.

### Einen MCP-Tool-Hook konfigurieren

Dieser Hook fordert den MCP-Server `scanner` auf, jeden Patch zu scannen, nachdem Codex Dateien geschrieben
oder bearbeitet hat:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "mcp_tool",
            "server": "scanner",
            "tool": "scan_patch",
            "input": { "patch": "${tool_input.command}" },
            "timeout": 30,
            "statusMessage": "Scanning edited files"
          }
        ]
      }
    ]
  }
}

| Feld           | Bedeutung                                                          |
| --------------- | ---------------------------------------------------------------- |
| `type`          | Muss `mcp_tool` sein.                                              |
| `server`        | Erforderlicher Name eines bereits verbundenen MCP-Servers.                |
| `tool`          | Erforderlicher Name eines Tools, das dieser Server bereitstellt.                  |
| `input`         | Optionales JSON-Objekt mit Vorlagen für Argumente. Standardwert: `{}`.    |
| `timeout`       | Optionales Zeitlimit für die aktive Ausführung in Sekunden. Standardwert: `600`. |
| `statusMessage` | Optionale Nachricht, die während der Ausführung des Hooks angezeigt wird.                      |

### Argumente mit Daten aus dem Hook-Ereignis füllen

Verwende `${field.nested}`, um ein Feld im Hook-Ereignis über einen Pfad in Punktnotation auszulesen.
Ein Platzhalter, der den gesamten Wert bildet, behält seinen JSON-Typ. Ein Platzhalter innerhalb einer längeren
Zeichenfolge wird als Text ausgegeben. Codex löst Platzhalter in Objekten und Arrays rekursiv auf.

Bei einem Ereignis mit `{"tool_input":{"file_path":"src/main.rs","count":3}}`
und dieser Argumentvorlage:

```json
{
  "path": "${tool_input.file_path}",
  "count": "${tool_input.count}",
  "message": "Scanning ${tool_input.file_path}"
}

ergibt sich:

```json
{
  "path": "src/main.rs",
  "count": 3,
  "message": "Scanning src/main.rs"
}

### Ausführung und Lebenszyklus

- Hooks nutzen eine bestehende MCP-Verbindung. Sie starten keine Server und verbinden sich nicht erneut mit ihnen.
- Ein Hook kann einen Vorgang blockieren, wenn das Tool eine Entscheidung zum Blockieren zurückgibt.
Fehler, fehlende Server und nicht verfügbare Tools blockieren den Vorgang nicht.
- MCP-Tool-Hooks laufen synchron. Sie fordern keine Genehmigung für Tool-Aufrufe an und lösen
keine anderen Hooks aus.
- Es gilt das kürzere der beiden Zeitlimits für Hook und Server. Die Wartezeit auf eine Antwort auf eine MCP-Elizitation
wird nicht auf das Zeitlimit angerechnet.
- Hooks für `SessionStart` können ausgeführt werden, bevor ein MCP-Server bereit ist.
  In diesem Fall blockieren sie die Sitzung nicht.
- `SessionEnd` unterstützt keine MCP-Tool-Hooks.

## Hooks deaktivieren

Hooks sind standardmäßig aktiviert. Um sie in `config.toml` zu deaktivieren, lege Folgendes fest:

```toml
[features]
hooks = false

Verwende `hooks` als kanonischen Schlüssel für die Funktion. `codex_hooks` funktioniert weiterhin als
veralteter Alias. Admins können Hooks auf dieselbe Weise in
`requirements.toml` mit `[features].hooks = false` verbindlich deaktivieren.

## Verwaltete Hooks aus `requirements.toml`

Vom Unternehmen verwaltete Vorgaben können Hooks auch direkt unter `[hooks]` definieren.
Das ist nützlich, wenn Admins die Hook-Konfiguration verbindlich vorgeben und dabei
die eigentlichen Skripte über MDM oder ein anderes System zur Geräteverwaltung verteilen möchten.
Um verwaltete Hooks auch für Nutzende durchzusetzen, die Hooks lokal deaktiviert haben, lege
`[features].hooks = true` in `requirements.toml` zusätzlich zu `[hooks]` verbindlich fest. Um Hooks aus
Benutzer-, Projekt- und Sitzungsquellen sowie Plug-ins zu ignorieren, aber weiterhin von Admins
verwaltete Hooks zuzulassen, setze `allow_managed_hooks_only = true`.

```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"

Hinweise zu verwalteten Hooks:

- `managed_dir` wird unter macOS und Linux verwendet.
- `windows_managed_dir` wird unter Windows verwendet.
- Codex verteilt die Skripte in `managed_dir` nicht. Die Tools deines Unternehmens müssen sie
  separat installieren und aktualisieren.
- Befehle für verwaltete Hooks sollten absolute Pfade zu Skripten innerhalb des konfigurierten
verwalteten Verzeichnisses verwenden.
- Mit `allow_managed_hooks_only = true` überspringt Codex Hooks aus Benutzer-, Projekt- und Sitzungsquellen sowie
  Plug-ins, lädt aber weiterhin verwaltete Hooks aus `requirements.toml` und
  anderen verwalteten Konfigurationsebenen.

## In Plug-ins enthaltene Hooks

Wenn ein Plug-in aktiviert ist, kann Codex dessen Lebenszyklus-Hooks
zusammen mit benutzer- und projektspezifischen sowie verwalteten Hooks laden.

Standardmäßig sucht Codex im Stammverzeichnis des Plug-ins nach `hooks/hooks.json`.
Das Manifest des Plug-ins kann diese Voreinstellung mit einem `hooks`-Eintrag in
`.codex-plugin/plugin.json` überschreiben. Dieser Eintrag kann ein Pfad mit dem Präfix `./`, ein
Array aus Pfaden mit dem Präfix `./`, ein direkt eingebettetes Hooks-Objekt oder ein Array aus
direkt eingebetteten Hooks-Objekten sein.

```json
{
  "name": "repo-policy",
  "hooks": "./hooks/hooks.json"
}

Hook-Pfade im Manifest werden relativ zum Stammverzeichnis des Plug-ins aufgelöst und müssen
innerhalb dieses Verzeichnisses bleiben. Wenn ein Manifest `hooks` definiert, verwendet Codex diese
Manifest-Einträge anstelle der Standarddatei `hooks/hooks.json`.

Befehle von Plug-in-Hooks erhalten diese Umgebungsvariablen:

- `PLUGIN_ROOT` ist eine Codex-spezifische Erweiterung, die auf das Stammverzeichnis
  des installierten Plug-ins verweist.
- `PLUGIN_DATA` ist eine Codex-spezifische Erweiterung, die auf das
  beschreibbare Datenverzeichnis des Plug-ins verweist.
- Codex setzt außerdem `CLAUDE_PLUGIN_ROOT` und `CLAUDE_PLUGIN_DATA`, um
  die Kompatibilität mit bestehenden Plug-in-Hooks zu gewährleisten.

Plug-in-Hooks verwenden dasselbe Ereignisschema wie andere Hooks. Wenn du ein Plug-in
installierst oder aktivierst, gelten dessen Hooks nicht automatisch als vertrauenswürdig. Codex überspringt die im Plug-in enthaltenen Hooks,
bis du die aktuelle Hook-Definition geprüft und als vertrauenswürdig eingestuft hast.

## Matcher-Muster

Das Feld `matcher` enthält einen regulären Ausdruck als Zeichenfolge und legt fest, wann Hooks ausgelöst werden. Verwende `"*"`,
`""` oder lass `matcher` ganz weg, um jedes Auftreten eines unterstützten
Ereignisses zu erfassen.

Nur einige der aktuellen Codex-Ereignisse berücksichtigen `matcher`:

| Ereignis               | Was `matcher` filtert | Hinweise                                                        |
| ------------------- | ---------------------- | ------------------------------------------------------------ |
| `PermissionRequest` | Tool-Name              | Unterstützt werden unter anderem `Bash`, `apply_patch`\* und MCP-Tool-Namen |
| `PostToolUse`       | Tool-Name              | Siehe [Unterstützte Tools](#tool-coverage)                          |
| `PostCompact`       | Auslöser für Compaction (Kontextverdichtung)     | Die Werte sind `manual` oder `auto`                                |
| `PreCompact`        | Auslöser für Compaction (Kontextverdichtung)     | Die Werte sind `manual` oder `auto`                                |
| `PreToolUse`        | Tool-Name              | Siehe [Unterstützte Tools](#tool-coverage)                          |
| `SessionEnd`        | Beendigungsgrund             | Derzeit nur `other`                                       |
| `SessionStart`      | Auslöser des Starts           | Die Werte sind `startup`, `resume`, `clear` und `compact`       |
| `SubagentStart`     | Typ des Subagenten          | Die Werte richten sich nach dem Subagenten, der startet                    |
| `SubagentStop`      | Typ des Subagenten          | Die Werte richten sich nach dem Subagenten, der stoppt                     |
| `UserPromptSubmit`  | Nicht unterstützt          | Die Einstellung `matcher` wird bei diesem Ereignis immer ignoriert           |
| `Stop`              | Nicht unterstützt          | Die Einstellung `matcher` wird bei diesem Ereignis immer ignoriert           |
| `Interrupt`         | Nicht unterstützt          | Die Einstellung `matcher` wird bei diesem Ereignis immer ignoriert           |

\*Bei `apply_patch` kannst du für `matcher` auch `Edit` oder `Write` verwenden.

Beispiele:

- `Bash`
- `^apply_patch$`
- `Edit|Write`
- `mcp__filesystem__read_file`
- `mcp__filesystem__.*`
- `startup|resume|clear|compact`
- `manual|auto`

### Unterstützte Tools

`PreToolUse` und `PostToolUse` können nicht nur Shell- und MCP-Aufrufe erfassen. Die meisten
lokalen Funktionstools verwenden denselben Hook-Pfad. So kannst du ihren Tool-Namen abgleichen,
ihre JSON-Argumente prüfen und bei `PreToolUse` den Aufruf blockieren oder umschreiben.

| Tool-Pfad                         | `PreToolUse` | `PostToolUse` | Hinweise                                                                                                                    |
| --------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Shell-Befehle                    | Ja          | Ja           | Verwende `Bash` zum Abgleich.                                                                                                         |
| Einheitliche Befehlsausführung (`exec_command`)     | Ja          | Ja           | Verwende `Bash` zum Abgleich. Eine spätere Abfrage mit `write_stdin` kann das `PostToolUse`-Ereignis des ursprünglichen Befehls liefern, sobald dieser abgeschlossen ist. |
| `apply_patch`                     | Ja          | Ja           | Verwende `apply_patch`, `Edit` oder `Write` zum Abgleich.                                                                              |
| MCP-Tools                         | Ja          | Ja           | Verwende zum Abgleich den Namen des MCP-Tools, etwa `mcp__filesystem__read_file`.                                                           |
| Andere lokale Funktionstools        | Ja          | Ja           | Verwende zum Abgleich den Namen des Funktionstools, etwa `update_plan`. Für `spawn_agent` kannst du auch `Agent` zum Abgleich verwenden.                                 |
| Gehostete Tools, etwa `WebSearch` | Nein           | Nein            | Diese verwenden nicht den Hook-Pfad für lokale Funktionstools.                                                                       |

`write_stdin` überträgt Daten für eine bestehende Sitzung zur einheitlichen Befehlsausführung. Es führt
`PreToolUse` nicht erneut aus, wenn es Eingaben sendet oder einen Befehl abfragt, der
`PreToolUse` bereits durchlaufen hat.

Einige spezialisierte Tool-Pfade können den standardmäßigen Hook-Pfad überspringen.
Betrachte Tool-Hooks als nützliche Schutzmaßnahme, nicht als Garantie für eine lückenlose Durchsetzung von Regeln.

## Gemeinsame Eingabefelder

Jeder Befehls-Hook erhält ein JSON-Objekt über `stdin`.

Diese gemeinsamen Felder verwendest du in der Regel:

| Feld             | Typ             | Bedeutung                                                             |
| ----------------- | ---------------- | ------------------------------------------------------------------- |
| `session_id`      | `string`         | ID der aktuellen Codex-Sitzung. Hooks für Subagenten verwenden die ID der übergeordneten Sitzung. |
| `transcript_path` | `string \| null` | Pfad zur Transkriptdatei der Sitzung, sofern vorhanden                         |
| `cwd`             | `string`         | Arbeitsverzeichnis der Sitzung                                   |
| `hook_event_name` | `string`         | Name des aktuellen Hook-Ereignisses                                             |
| `model`           | `string`         | Codex-spezifische Erweiterung. Slug des aktiven Modells                         |

Hooks für einzelne Gesprächsrunden führen `turn_id` in ihren
ereignisspezifischen Tabellen als Codex-spezifische Erweiterung auf.

`SessionStart`, `PreToolUse`, `PermissionRequest`, `PostToolUse`,
`UserPromptSubmit`, `SubagentStart`, `SubagentStop`, `Stop` und `Interrupt` enthalten außerdem
`permission_mode`. Dieses Feld gibt den aktuellen Berechtigungsmodus als `default`,
`acceptEdits`, `plan`, `dontAsk` oder `bypassPermissions` an.

`transcript_path` verweist der Einfachheit halber auf ein Chat-Transkript. Das
Transkriptformat ist jedoch keine stabile Schnittstelle für Hooks und kann sich im Laufe der Zeit ändern.

Das vollständige Übertragungsformat findest du unter [Schemata](#schemas).

## Gemeinsame Ausgabefelder

`SessionStart`, `PreCompact`, `PostCompact`, `UserPromptSubmit`,
`SubagentStop` und `Stop` unterstützen diese gemeinsamen JSON-Felder. `SubagentStart`
akzeptiert dieselbe Struktur für `systemMessage` und Hook-spezifischen Kontext,
aber `continue: false` stoppt den Subagenten nicht:

```json
{
  "continue": true,
  "stopReason": "optional",
  "systemMessage": "optional",
  "suppressOutput": false
}

| Feld            | Wirkung                                          |
| ---------------- | ----------------------------------------------- |
| `continue`       | Bei `false` wird diese Hook-Ausführung als gestoppt markiert      |
| `stopReason`     | Wird als Grund für den Stopp erfasst             |
| `systemMessage`  | Wird in der Benutzeroberfläche oder im Ereignisstream als Warnung ausgegeben |
| `suppressOutput` | Wird bereits geparst, ist aber noch nicht implementiert            |

Ein Exit-Code von `0` ohne Ausgabe gilt als Erfolg und Codex fährt fort.

`PreToolUse` und `PermissionRequest` unterstützen `systemMessage`, aber `continue`,
`stopReason` und `suppressOutput` werden für diese Ereignisse derzeit nicht unterstützt.
Gibt ein Hook für `PreToolUse` eines dieser nicht unterstützten Felder zurück, markiert Codex
diese Hook-Ausführung als fehlgeschlagen, meldet den Fehler und setzt den Tool-Aufruf fort.

`PostToolUse` unterstützt `systemMessage`, `continue: false` und `stopReason`.
`suppressOutput` wird geparst, für dieses Ereignis derzeit aber nicht unterstützt.

### Umfangreiche Hook-Ausgaben

Standardmäßig begrenzt Codex jede für das Modell sichtbare Nachricht mit Hook-Ausgabe auf etwa
2.500 Token. Gibt ein Hook mehr zurück, speichert Codex den vollständigen Text unter
`<temp_dir>/hook_outputs/<session_id>/<uuid>.txt` und stellt dem Modell eine
Vorschau mit Anfang und Ende des Textes sowie dem Pfad zur gespeicherten Datei bereit. Dies wird als
**Auslagern** bezeichnet: Codex speichert zu umfangreiche Ausgaben auf dem Datenträger und ersetzt sie durch eine
kürzere, für das Modell sichtbare Vorschau. Kann die Datei nicht geschrieben werden, erhält das Modell trotzdem
eine gekürzte Vorschau.

  Halte den Kontext von Hooks und Plug-ins knapp. Der Kontext mehrerer Hooks und Plug-ins
  summiert sich und kann die Modellleistung beeinträchtigen. Ein höherer Wert für `additionalContextLimit`
  erhöht dieses Risiko. Setze den Grenzwert nur dann auf `0`, wenn der Hook eine
  strikte Obergrenze für die Ausgabe erzwingt. Andernfalls kann ein einzelner Hook das gesamte
  Kontextfenster belegen.

Wenn ein Befehls-Hook `additionalContext` zurückgibt, lege
`additionalContextLimit` im Handler fest, um den ungefähren
Token-Schwellenwert anzupassen:

```json
{
  "type": "command",
  "command": "python3 ~/.codex/hooks/session_start.py",
  "additionalContextLimit": 5000
}

Lass `additionalContextLimit` weg, um den Standardschwellenwert von `2500` Token zu verwenden. Verwende eine
positive Ganzzahl für einen anderen Schwellenwert oder `0`, um den gesamten zusätzlichen Kontext des Handlers
direkt an das Modell zu übergeben. Codex wertet jeden
passenden Handler unabhängig aus. Bei Ereignissen, die keinen zusätzlichen Kontext
erzeugen können, ignoriert Codex `additionalContextLimit` und gibt eine
Konfigurationswarnung aus.

Die Einstellung gilt nur für `additionalContext`. Für Tool-Feedback und
Prompts zur Fortsetzung gilt weiterhin der Standardgrenzwert.

Da zu umfangreiche Ausgaben auf dem Datenträger gespeichert werden können, solltest du in Hook-Ausgaben keine vertraulichen Informationen oder
anderen sensiblen Daten zurückgeben.

## Hooks im Hintergrund ausführen

Standardmäßig wartet Codex, bis ein Befehls-Hook abgeschlossen ist, bevor es den
Vorgang fortsetzt, der den Hook ausgelöst hat. Setze `async` auf `true`, um einen Befehls-Hook
im Hintergrund auszuführen, während Codex weiterarbeitet.

### Hintergrund-Hook konfigurieren

Füge einem Befehlshandler in `hooks.json` die Einstellung `"async": true` hinzu:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/post_tool_use.py",
            "async": true,
            "timeout": 120
          }
        ]
      }
    ]
  }
}

Verwende für einen Inline-Hook in `config.toml` die Einstellung `async = true`:

```toml
[[hooks.PostToolUse]]
matcher = "Bash"

[[hooks.PostToolUse.hooks]]
type = "command"
command = "python3 ~/.codex/hooks/post_tool_use.py"
async = true
timeout = 120

Bei Hintergrund-Hooks funktionieren Eingabe, Matcher, Vertrauensprüfung, Zeitlimit und
[Verarbeitung großer Ausgaben](#large-hook-output) genauso wie bei synchronen Befehls-Hooks.
Wie bei anderen Befehls-Hooks wird `timeout` in Sekunden angegeben und hat standardmäßig
den Wert `600`. Für Hooks vom Typ `Interrupt` gilt standardmäßig eine Sekunde und maximal drei Sekunden,
auch wenn sie im Hintergrund ausgeführt werden.

### So werden Hintergrund-Hooks ausgeführt

Sobald ein Hintergrund-Hook abgeschlossen ist, stellt Codex die unterstützten Informationsausgaben
zum nächsten sicheren Zeitpunkt in der Unterhaltung bereit:

- Wenn ein Durchlauf aktiv ist, wartet Codex, bis die aktuelle Modellanfrage und die Toolaufrufe
abgeschlossen sind. Anschließend stellt Codex die Ausgabe für die nächste Modellanfrage in diesem
Durchlauf bereit.
- Wenn kein Durchlauf aktiv ist, wartet Codex bis zum nächsten Durchlauf mit Nutzereingabe.
Der Abschluss eines Hintergrund-Hooks startet keinen neuen Durchlauf.

Verwende dieselbe ereignisspezifische JSON-Ausgabe wie bei einem synchronen Hook. Codex fügt
`additionalContext` zum Kontext des Modells hinzu und zeigt `systemMessage`
als Warnung an.

  Hintergrund-Hooks können den Vorgang, der sie ausgelöst hat, weder blockieren noch genehmigen,
ändern oder anderweitig steuern. Verwende synchrone Hooks für Tool-Richtlinien, Entscheidungen
über Berechtigungen, das Ablehnen von Prompts oder das Fortsetzen eines Durchlaufs.

### Einschränkungen

- Codex führt pro Sitzung bis zu acht Hintergrund-Hooks gleichzeitig aus.
Weitere Hooks warten, bis ein laufender Hook abgeschlossen ist.
- Jeder passende Aufruf wird unabhängig ausgeführt. Hintergrund-Hooks können
in einer anderen Reihenfolge enden, als sie gestartet wurden.
- Wenn die Sitzung endet, bricht Codex noch nicht abgeschlossene Hintergrund-Hooks ab
und verwirft Ausgaben, die noch nicht bereitgestellt wurden.
- Hooks vom Typ `SessionEnd` werden immer synchron ausgeführt.

## Hooks

### SessionStart

`matcher` wird bei diesem Ereignis auf `source` angewendet.

Felder zusätzlich zu den [allgemeinen Eingabefeldern](#common-input-fields):

| Feld    | Typ     | Bedeutung                                                             |
| -------- | -------- | ------------------------------------------------------------------- |
| `source` | `string` | Wie die Sitzung gestartet wurde: `startup`, `resume`, `clear` oder `compact` |

Klartext auf `stdout` wird als zusätzlicher Entwicklerkontext hinzugefügt.

JSON auf `stdout` unterstützt die [allgemeinen Ausgabefelder](#common-output-fields) und die folgende
Hook-spezifische Struktur:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Load the workspace conventions before editing."
  }
}

Der Text aus `additionalContext` wird als zusätzlicher Entwicklerkontext hinzugefügt.

Nachdem Codex den Kontext einer Root-Sitzung verdichtet hat, werden Hooks vom Typ `SessionStart`, die
der Bedingung `source: "compact"` entsprechen, vor der nächsten Modellanfrage ausgeführt. Das gilt auch, wenn
die automatische Compaction (Kontextverdichtung) mitten in einem Durchlauf stattfindet: Codex stellt den
zusätzlichen Kontext des Hooks für die unmittelbare Fortsetzung bereit, statt auf einen
späteren Durchlauf mit Nutzereingabe zu warten. Gibt der Hook `continue: false` zurück, beendet Codex den Durchlauf,
ohne eine weitere Modellanfrage zu senden.

### SessionEnd

Mit `SessionEnd` kannst du beim Ende einer Sitzung einen Befehl ausführen, etwa um abschließende
Notizen zu speichern oder Dateien zu bereinigen. Der Hook wird für den Haupt-Thread ausgeführt, wenn du eine noch offene Unterhaltung archivierst oder
löschst, wenn Codex regulär beendet wird oder wenn eine Unterhaltung seit 30 Minuten
inaktiv und in keinem verbundenen Client geöffnet ist.
Für Subagenten wird er nicht ausgeführt.

Wenn du eine Unterhaltung verlässt oder `thread/unsubscribe` aufrufst, wird
die Sitzung nicht sofort beendet. Deshalb wird `SessionEnd` nicht unmittelbar ausgeführt. Dein Hook kann
während seiner Ausführung weiterhin das Sitzungstranskript lesen.

Bei diesem Ereignis filtert `matcher` nach `reason`. Derzeit hat `reason` immer den Wert `other`.
Du kannst `matcher` weglassen oder `other` verwenden, damit der Hook bei jedem Ereignis vom Typ `SessionEnd` ausgeführt wird.

Felder zusätzlich zu den [allgemeinen Eingabefeldern](#common-input-fields):

| Feld    | Typ     | Bedeutung                        |
| -------- | -------- | ------------------------------ |
| `reason` | `string` | Grund für das Ende der Sitzung: `other` |

Ein Befehl für `SessionEnd` erhält beispielsweise:

```json
{
  "session_id": "thr_123",
  "transcript_path": "/workspace/.codex/rollout.jsonl",
  "cwd": "/workspace",
  "hook_event_name": "SessionEnd",
  "reason": "other"
}

Hooks vom Typ `SessionEnd` werden immer synchron ausgeführt, auch wenn `async` den Wert `true` hat. Ihre
Ausgaben dienen nur als Hinweis: Sie steuern Codex nicht und halten den Thread nicht offen. Wenn bei einem
Befehl eine Zeitüberschreitung auftritt oder er mit einem Fehler beendet wird, meldet Codex dies als Hook-Fehler.

### SubagentStart

`matcher` wird bei diesem Ereignis auf `agent_type` angewendet.

Felder zusätzlich zu den [allgemeinen Eingabefeldern](#common-input-fields):

| Feld             | Typ     | Bedeutung                                        |
| ----------------- | -------- | ---------------------------------------------- |
| `turn_id`         | `string` | Codex-spezifische Erweiterung. ID des aktiven Codex-Durchlaufs |
| `agent_id`        | `string` | Kennung des Subagenten                    |
| `agent_type`      | `string` | Typ oder Profil des Subagenten                       |
| `permission_mode` | `string` | Aktueller Berechtigungsmodus                        |

Klartext auf `stdout` wird dem Subagenten als zusätzlicher Entwicklerkontext hinzugefügt.

JSON auf `stdout` unterstützt `systemMessage` und die folgende Hook-spezifische Struktur:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Review the repository test conventions first."
  }
}

Der Text aus `additionalContext` wird dem Subagenten als zusätzlicher Entwicklerkontext
hinzugefügt. `continue: false` wird aus Kompatibilitätsgründen geparst, verhindert jedoch nicht,
dass der Subagent gestartet wird.

### PreToolUse

`PreToolUse` kann Bash, über `apply_patch` vorgenommene Dateibearbeitungen,
MCP-Toolaufrufe und andere lokale Funktionstools abfangen. Unter [Unterstützung für
Tools](#tool-coverage) findest du die unterstützten Ausführungspfade und Ausnahmen.

`matcher` wird auf `tool_name` und Matcher-Aliasse angewendet. Bei Dateibearbeitungen über
`apply_patch` kannst du für `matcher` die Werte `apply_patch`, `Edit` oder `Write` verwenden. Die Hook-Eingabe
gibt weiterhin `tool_name: "apply_patch"` an.

Felder zusätzlich zu den [allgemeinen Eingabefeldern](#common-input-fields):

| Feld         | Typ         | Bedeutung                                                                                                                          |
| ------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`     | `string`     | Codex-spezifische Erweiterung. ID des aktiven Codex-Durchlaufs                                                                                   |
| `tool_name`   | `string`     | Kanonischer Toolname für den Hook, etwa `Bash`, `apply_patch` oder ein MCP-Name wie `mcp__fs__read`                                     |
| `tool_use_id` | `string`     | ID des Toolaufrufs für diese Ausführung                                                                                                 |
| `tool_input`  | `JSON value` | Tool-spezifische Eingabe. `Bash` und `apply_patch` verwenden `tool_input.command`. MCP-Tools und andere lokale Funktionstools senden ihre Argumente. |

Klartext auf `stdout` wird ignoriert.

In JSON auf `stdout` kannst du `systemMessage` verwenden. Um einen unterstützten Tool-Aufruf abzulehnen, gib
die folgende Hook-spezifische Struktur zurück:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook."
  }
}

Codex akzeptiert auch diese ältere Struktur zum Blockieren:

```json
{
  "decision": "block",
  "reason": "Destructive command blocked by hook."
}

Du kannst auch den Exit-Code `2` verwenden und den Grund für die Blockierung auf `stderr` ausgeben.

Um für das Modell sichtbaren Kontext hinzuzufügen, ohne den Aufruf zu blockieren, gib
`hookSpecificOutput.additionalContext` zurück:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "The pending command touches generated files."
  }
}

Um einen unterstützten Tool-Aufruf umzuschreiben, ohne ihn zu blockieren, gib
`permissionDecision: "allow"` mit `updatedInput` zurück:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "echo rewritten"
    }
  }
}

Für Bash-Befehle und `apply_patch` muss `updatedInput` ein Feld
`command` vom Typ String enthalten. Bei MCP-Tools und anderen lokalen Funktionstools ist `updatedInput`
das Ersatzobjekt für die Argumente. Gib `updatedInput` nur zusammen mit
`permissionDecision: "allow"` zurück. Andere Strukturen für `updatedInput` werden als Fehler
gemeldet.

`permissionDecision: "ask"`, die ältere Form `decision: "approve"`, `continue: false`,
`stopReason` und `suppressOutput` werden geparst, aber noch nicht unterstützt. Codex markiert
die Hook-Ausführung als fehlgeschlagen, meldet den Fehler und setzt den Tool-Aufruf fort.

### PermissionRequest

`PermissionRequest` wird ausgeführt, wenn Codex eine Genehmigung anfordern will, etwa für
erweiterte Shell-Berechtigungen oder verwalteten Netzwerkzugriff. Der Hook kann die Anfrage genehmigen,
ablehnen oder keine Entscheidung treffen und die normale Genehmigungsabfrage fortsetzen lassen.
Bei Befehlen, die keine Genehmigung benötigen, wird er nicht ausgeführt.

`matcher` wird auf `tool_name` und Matcher-Aliase angewendet. Zu den aktuellen kanonischen
Werten gehören `Bash`, `apply_patch` und MCP-Toolnamen wie
`mcp__server__tool`. `apply_patch` lässt sich auch über `Edit` und `Write` abgleichen.

Zusätzliche Felder neben den [allgemeinen Eingabefeldern](#common-input-fields):

| Feld                    | Typ             | Bedeutung                                                                                                        |
| ------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------- |
| `turn_id`                | `string`         | Codex-spezifische Erweiterung. ID des aktiven Codex-Interaktionsschritts                                                                 |
| `tool_name`              | `string`         | Kanonischer Toolname für Hooks, zum Beispiel `Bash`, `apply_patch` oder ein MCP-Name wie `mcp__fs__read`                   |
| `tool_input`             | `JSON value`     | Toolspezifische Eingabe. `Bash` und `apply_patch` verwenden `tool_input.command`, während MCP-Tools alle Argumente senden. |
| `tool_input.description` | `string \| null` | Verständliche Begründung für die Genehmigungsanfrage, sofern Codex eine bereitstellt                                                             |

Nur-Text-Ausgabe auf `stdout` wird ignoriert.

Manche Tool-Eingaben können eine verständliche Beschreibung enthalten. Verlass dich aber nicht darauf,
dass jedes Tool ein Feld `tool_input.description` bereitstellt.

Um die Anfrage zu genehmigen, gib Folgendes zurück:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow"
    }
  }
}

Um die Anfrage abzulehnen, gib Folgendes zurück:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "deny",
      "message": "Blocked by repository policy."
    }
  }
}

Wenn mehrere passende Hooks Entscheidungen zurückgeben, hat `deny` immer Vorrang. Andernfalls
wird die Anfrage bei `allow` ohne Genehmigungsabfrage fortgesetzt. Wenn kein
passender Hook entscheidet, verwendet Codex den normalen Genehmigungsablauf.

Gib weder `updatedInput` noch `updatedPermissions` noch `interrupt` für
`PermissionRequest` zurück. Diese Felder sind für künftiges Verhalten reserviert und führen derzeit
zur Ablehnung der Anfrage.

### PostToolUse

`PostToolUse` wird ausgeführt, nachdem unterstützte Tools eine Ausgabe erzeugt haben. Dazu gehören Bash,
`apply_patch`, MCP-Tool-Aufrufe und andere lokale Funktionstools. Bei Bash wird der Hook
auch nach Befehlen ausgeführt, die mit einem Status ungleich null enden. Er kann die Seiteneffekte
eines bereits ausgeführten Tools nicht rückgängig machen. Unter [Unterstützte Tools](#tool-coverage) findest du
die unterstützten Ausführungspfade und Ausnahmen.

`matcher` wird auf `tool_name` und Matcher-Aliase angewendet. Für Dateiänderungen über
`apply_patch` kannst du für `matcher` die Werte `apply_patch`, `Edit` oder `Write` verwenden. Die Hook-Eingabe
enthält weiterhin `tool_name: "apply_patch"`.

Zusätzliche Felder neben den [allgemeinen Eingabefeldern](#common-input-fields):

| Feld           | Typ         | Bedeutung                                                                                                                          |
| --------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`       | `string`     | Codex-spezifische Erweiterung. ID des aktiven Codex-Interaktionsschritts                                                                                   |
| `tool_name`     | `string`     | Kanonischer Toolname für Hooks, zum Beispiel `Bash`, `apply_patch` oder ein MCP-Name wie `mcp__fs__read`                                     |
| `tool_use_id`   | `string`     | ID des Tool-Aufrufs für diese Ausführung                                                                                                 |
| `tool_input`    | `JSON value` | Toolspezifische Eingabe. `Bash` und `apply_patch` verwenden `tool_input.command`. MCP-Tools und andere lokale Funktionstools senden ihre Argumente. |
| `tool_response` | `JSON value` | Toolspezifische Ausgabe. MCP-Tools senden das Ergebnis des MCP-Aufrufs. Andere lokale Funktionstools senden in der Regel ihre für das Modell bestimmte Ausgabe.    |

Nur-Text-Ausgabe auf `stdout` wird ignoriert.

In JSON auf `stdout` kannst du `systemMessage` und die folgende Hook-spezifische Struktur verwenden:

```json
{
  "decision": "block",
  "reason": "The Bash output needs review before continuing.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command updated generated files."
  }
}

Der Text aus `additionalContext` wird als zusätzlicher Entwicklerkontext hinzugefügt.

Bei diesem Ereignis macht `decision: "block"` den bereits ausgeführten Bash-Befehl nicht rückgängig.
Stattdessen zeichnet Codex das Feedback auf, ersetzt das Tool-Ergebnis durch dieses
Feedback und setzt die Modellausführung mit der vom Hook bereitgestellten Nachricht fort.

Du kannst auch den Exit-Code `2` verwenden und die Begründung für das Feedback auf `stderr` ausgeben.

Um die normale Verarbeitung des ursprünglichen Tool-Ergebnisses zu stoppen, nachdem der Befehl
bereits ausgeführt wurde, gib `continue: false` zurück. Codex ersetzt das Tool-Ergebnis durch
dein Feedback oder deine Stoppmeldung und setzt die Verarbeitung damit fort.

`updatedMCPToolOutput` und `suppressOutput` werden geparst, aber noch nicht unterstützt.
Codex markiert die Hook-Ausführung als fehlgeschlagen, meldet den Fehler und setzt die normale
Verarbeitung des Tool-Ergebnisses fort.

#### Tool-Aufrufe im Codemodus

Wenn ein Modell im Codemodus über JavaScript ein Tool aufruft, gelten die Hook-Entscheidungen
für diesen verschachtelten Aufruf. `PreToolUse` kann die Ausführung des Tools verhindern oder
dessen Eingabe umschreiben. Ein blockierender `PostToolUse`-Hook kann die Seiteneffekte des Tools nicht rückgängig machen,
aber verhindern, dass das ursprüngliche Ergebnis das laufende Skript erreicht.

| Hook-Ergebnis                                                      | Was im Codemodus sichtbar ist                                                                                    |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `PreToolUse` blockiert                                              | Das Promise des Tools wird abgelehnt, bevor das Tool ausgeführt wird.                                                         |
| `PreToolUse` gibt `updatedInput` zurück                              | Das Tool wird mit der umgeschriebenen Eingabe ausgeführt, und das Promise wird mit diesem Ergebnis aufgelöst.                      |
| `PostToolUse` gibt `decision: "block"` zurück oder endet mit Exit-Code `2` | Das Tool wird ausgeführt. Anschließend wird das Promise mit der Begründung des Hooks abgelehnt.                                          |
| `PostToolUse` gibt `continue: false` zurück                          | Codex verwendet das Hook-Feedback als für das Modell sichtbares Ergebnis, lehnt das Promise des verschachtelten Tool-Aufrufs aber nicht ab. |

### PreCompact

`PreCompact` wird ausgeführt, bevor Codex den Chat verdichtet. `matcher` wird
auf `trigger` mit den möglichen Werten `manual` und `auto` angewendet.

Zusätzliche Felder neben den [allgemeinen Eingabefeldern](#common-input-fields):

| Feld     | Typ     | Bedeutung                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex-spezifische Erweiterung. ID des aktiven Codex-Interaktionsschritts |
| `trigger` | `string` | Auslöser der Compaction (Kontextverdichtung): `manual` oder `auto`  |

Nur-Text-Ausgabe auf `stdout` wird ignoriert.

JSON auf `stdout` unterstützt die [gemeinsamen Ausgabefelder](#common-output-fields). Wenn ein
passender `PreCompact`-Hook `continue: false` zurückgibt, stoppt Codex
vor der Compaction (Kontextverdichtung).

### PostCompact

`PostCompact` wird ausgeführt, nachdem Codex den Kontext des Chats verdichtet hat. `matcher` wird
auf `trigger` angewendet, dessen Werte `manual` und `auto` sind.

Zusätzliche Felder neben den [gemeinsamen Eingabefeldern](#common-input-fields):

| Feld     | Typ     | Bedeutung                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex-spezifische Erweiterung. ID des aktiven Codex-Turns |
| `trigger` | `string` | Auslöser der Compaction (Kontextverdichtung): `manual` oder `auto`  |

Reiner Text auf `stdout` wird ignoriert.

JSON auf `stdout` unterstützt die [gemeinsamen Ausgabefelder](#common-output-fields). Wenn ein
passender `PostCompact`-Hook `continue: false` zurückgibt, stoppt Codex
nach der Compaction (Kontextverdichtung).

### UserPromptSubmit

`matcher` wird derzeit für dieses Ereignis nicht verwendet.

Zusätzliche Felder neben den [gemeinsamen Eingabefeldern](#common-input-fields):

| Feld     | Typ     | Bedeutung                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex-spezifische Erweiterung. ID des aktiven Codex-Turns |
| `prompt`  | `string` | Der von dir eingegebene Prompt, der gleich gesendet wird            |

Reiner Text auf `stdout` wird als zusätzlicher Entwicklerkontext hinzugefügt.

JSON auf `stdout` unterstützt die [gemeinsamen Ausgabefelder](#common-output-fields) und
folgende Struktur für diesen Hook:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Ask for a clearer reproduction before editing files."
  }
}

Der Text in `additionalContext` wird als zusätzlicher Entwicklerkontext hinzugefügt.

Gib Folgendes zurück, um den Prompt zu blockieren:

```json
{
  "decision": "block",
  "reason": "Ask for confirmation before doing that."
}

Du kannst auch den Exit-Code `2` verwenden und den Grund für die Blockierung auf `stderr` ausgeben.

### SubagentStop

Bei diesem Ereignis wird `matcher` auf `agent_type` angewendet.

Zusätzliche Felder neben den [gemeinsamen Eingabefeldern](#common-input-fields):

| Feld                    | Typ             | Bedeutung                                         |
| ------------------------ | ---------------- | ----------------------------------------------- |
| `turn_id`                | `string`         | Codex-spezifische Erweiterung. ID des aktiven Codex-Turns  |
| `agent_id`               | `string`         | Kennung des Subagenten                     |
| `agent_type`             | `string`         | Typ oder Profil des Subagenten                        |
| `agent_transcript_path`  | `string \| null` | Pfad zur Transkriptdatei des Subagenten, falls vorhanden    |
| `stop_hook_active`       | `boolean`        | Ob die Ausführung dieses Subagenten bereits fortgesetzt wurde     |
| `last_assistant_message` | `string \| null` | Letzte Assistentennachricht des Subagenten, sofern verfügbar |

`SubagentStop` erwartet JSON auf `stdout`, wenn der Hook mit Exit-Code `0` endet. Eine reine Textausgabe ist
für dieses Ereignis ungültig.

JSON auf `stdout` unterstützt die [gemeinsamen Ausgabefelder](#common-output-fields). Gib Folgendes zurück, um
Codex aufzufordern, den Ablauf des Subagenten fortzusetzen:

```json
{
  "decision": "block",
  "reason": "Run one more focused pass inside the subagent."
}

Du kannst auch den Exit-Code `2` verwenden und den Grund für die Fortsetzung auf `stderr` ausgeben.

Wenn ein passender `SubagentStop`-Hook `continue: false` zurückgibt, hat das
Vorrang vor Entscheidungen anderer passender `SubagentStop`-Hooks
zur Fortsetzung.

### Stop

`matcher` wird derzeit für dieses Ereignis nicht verwendet.

Zusätzliche Felder neben den [gemeinsamen Eingabefeldern](#common-input-fields):

| Feld                    | Typ             | Bedeutung                                           |
| ------------------------ | ---------------- | ------------------------------------------------- |
| `turn_id`                | `string`         | Codex-spezifische Erweiterung. ID des aktiven Codex-Turns    |
| `stop_hook_active`       | `boolean`        | Ob dieser Turn bereits durch `Stop` fortgesetzt wurde |
| `last_assistant_message` | `string \| null` | Text der letzten Assistentennachricht, sofern verfügbar       |

`Stop` erwartet JSON auf `stdout`, wenn der Hook mit Exit-Code `0` endet. Eine reine Textausgabe ist
für dieses Ereignis ungültig.

JSON auf `stdout` unterstützt die [gemeinsamen Ausgabefelder](#common-output-fields). Gib Folgendes zurück, damit
Codex fortfährt:

```json
{
  "decision": "block",
  "reason": "Run one more pass over the failing tests."
}

Du kannst auch den Exit-Code `2` verwenden und den Grund für die Fortsetzung auf `stderr` ausgeben.

Bei diesem Ereignis lehnt `decision: "block"` den Turn nicht ab. Stattdessen wird Codex
angewiesen, fortzufahren, und automatisch ein neuer Prompt zur Fortsetzung erstellt. Dieser dient
als neuer Nutzer-Prompt, wobei der von dir in `reason` angegebene Grund als Prompttext verwendet wird.

Wenn ein passender `Stop`-Hook `continue: false` zurückgibt, hat das Vorrang
vor Entscheidungen anderer passender `Stop`-Hooks zur Fortsetzung.

### Interrupt

`Interrupt` wird ausgeführt, wenn du einen aktiven Turn im Haupt-Thread unterbrichst. Nutze ihn,
um die Unterbrechung zu protokollieren oder nach Arbeiten aufzuräumen, die ein Hook gestartet hat.
Er wird weder für inaktive Threads noch für Subagenten ausgeführt. Ein konfigurierter `matcher` wird ignoriert.

Zusätzlich zu den [gemeinsamen Eingabefeldern](#common-input-fields) enthält das Ereignis
`turn_id`, die ID des unterbrochenen Turns, und `permission_mode`.

Für Befehls-Hooks gilt standardmäßig ein Timeout von einer Sekunde. Konfigurierte Timeouts sind
auf eine bis drei Sekunden begrenzt. Die Hook-Ausgabe kann weder die
Unterbrechung verhindern noch den Turn neu starten. Beende den Hook ohne Ausgabe mit Exit-Code `0` oder gib JSON mit
einem optionalen `systemMessage`-Feld zurück, um eine Warnung anzuzeigen. Reine Textausgaben sind
für dieses Ereignis ungültig.

```json
{ "systemMessage": "Saved the interrupted turn to the local audit log." }

## Schemas

  Die verlinkten Schemas des Branches `main` können Hook-Felder enthalten, die nicht Teil der
  aktuellen Version sind. Nutze diese Seite als Referenz für das Verhalten der aktuellen Version.

Wenn du das genaue aktuelle Übertragungsformat benötigst, findest du es in den generierten Schemas im
[Codex-Repository auf GitHub](https://github.com/openai/codex/tree/main/codex-rs/hooks/schema/generated).
