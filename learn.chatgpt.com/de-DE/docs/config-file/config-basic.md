<!-- source: https://learn.chatgpt.com/de-DE/docs/config-file/config-basic -->

Codex liest die Konfiguration aus mehreren Quellen. Deine persönlichen Standardeinstellungen stehen in `~/.codex/config.toml`. Mit `.codex/config.toml`-Dateien kannst du sie für einzelne Projekte überschreiben. Aus Sicherheitsgründen lädt Codex projektspezifische Konfigurationsebenen unter `.codex/` nur, wenn du dem Projekt vertraust.

## Codex-Konfigurationsdatei

Codex speichert die Benutzerkonfiguration unter `~/.codex/config.toml`. Wenn Einstellungen nur für ein bestimmtes Projekt oder einen Unterordner gelten sollen, füge dort in deinem Repository eine `.codex/config.toml`-Datei hinzu.

Um die Konfigurationsdatei in der Codex IDE-Erweiterung zu öffnen, wähle oben rechts das Zahnradsymbol und dann **Codex-Einstellungen \> config.toml öffnen** aus.

CLI und IDE-Erweiterung verwenden dieselben Konfigurationsebenen. Damit kannst du:

- Das Standardmodell und den Anbieter festlegen.
- [Genehmigungsrichtlinien und Sandbox-Einstellungen](/de-DE/codex/agent-approvals-security#sandbox-and-approvals) konfigurieren.
- [MCP-Server](/de-DE/codex/extend/mcp) konfigurieren.

## Priorität der Konfiguration

Codex ermittelt Werte in dieser Reihenfolge (höchste Priorität zuerst):

1. CLI-Flags und Überschreibungen mit `--config`
2. Projektkonfigurationsdateien: `.codex/config.toml`, vom Projektstammverzeichnis bis zu deinem aktuellen Arbeitsverzeichnis (die nächstgelegene Datei hat Vorrang; nur bei vertrauenswürdigen Projekten)
3. Mit `--profile profile-name` ausgewählte [Profildateien](/de-DE/codex/config-file/config-advanced#profiles) (`~/.codex/profile-name.config.toml`)
4. Benutzerkonfiguration: `~/.codex/config.toml`
5. Systemkonfiguration (falls vorhanden): `/etc/codex/config.toml` unter Unix
6. Integrierte Standardeinstellungen

Nutze diese Rangfolge, um gemeinsame Standardeinstellungen in `config.toml` festzulegen und die [Profildateien](/de-DE/codex/config-file/config-advanced#profiles) auf abweichende Werte zu beschränken.

Wenn du ein Projekt als nicht vertrauenswürdig markierst, überspringt Codex die projektspezifischen Konfigurationsebenen unter `.codex/`, einschließlich der lokalen Projektkonfiguration sowie projektspezifischer Hooks und Regeln. Die Benutzer- und Systemkonfiguration werden weiterhin geladen, einschließlich benutzerspezifischer und globaler Hooks und Regeln.

Informationen zu einmaligen Überschreibungen über `-c`/`--config` (einschließlich der TOML-Regeln für Anführungszeichen) findest du unter [Erweiterte Konfiguration](/de-DE/codex/config-file/config-advanced#one-off-overrides-from-the-cli).

  Auf verwalteten Geräten kann deine Organisation außerdem über
`requirements.toml` Einschränkungen durchsetzen (etwa indem sie `approval_policy = "never"` oder
`sandbox_mode = "danger-full-access"` untersagt). Weitere Informationen findest du unter [Verwaltete
  Konfiguration](/de-DE/codex/enterprise/managed-configuration) und [Administrativ erzwungene
  Anforderungen](/de-DE/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

## Gängige Konfigurationsoptionen

Hier sind einige Optionen, die besonders häufig geändert werden:

#### Standardmodell

Wähle das Modell aus, das Codex standardmäßig in der CLI und der IDE verwendet.

#### Genehmigungsabfragen

Lege fest, wann Codex pausiert und vor dem Ausführen generierter Befehle eine Genehmigung anfordert.

```toml
approval_policy = "on-request"

Informationen zu den Verhaltensunterschieden zwischen `untrusted`, `on-request` und `never` findest du unter [Ohne Genehmigungsabfragen ausführen](/de-DE/codex/agent-approvals-security#run-without-approval-prompts) und [Gängige Kombinationen aus Sandbox und Genehmigung](/de-DE/codex/agent-approvals-security#common-sandbox-and-approval-combinations).

#### Sandbox-Stufe

Lege fest, in welchem Umfang Codex beim Ausführen von Befehlen auf das Dateisystem und das Netzwerk zugreifen kann.

```toml
sandbox_mode = "workspace-write"

Informationen zum Verhalten der einzelnen Modi (einschließlich der geschützten Pfade `.git`/`.codex` und der Standardeinstellungen für den Netzwerkzugriff) findest du unter [Sandbox und Genehmigungen](/de-DE/codex/agent-approvals-security#sandbox-and-approvals), [Geschützte Pfade in Stammverzeichnissen mit Schreibzugriff](/de-DE/codex/agent-approvals-security#protected-paths-in-writable-roots) und [Netzwerkzugriff](/de-DE/codex/agent-approvals-security#network-access).

#### Berechtigungsprofile

Codex unterstützt außerdem benannte Berechtigungsprofile für wiederverwendbare Richtlinien zum Dateisystem- und
Netzwerkzugriff. Die integrierten Profile sind `:read-only`, `:workspace` und
`:danger-full-access`. Benutzerdefinierte Profile verwenden Tabellen vom Typ `[permissions.<name>]` und einen
passenden Wert für `default_permissions`. Siehe [Berechtigungen](/de-DE/codex/permissions).

#### Windows-Sandbox-Modus

Wenn du Codex nativ unter Windows ausführst, setze den nativen Sandbox-Modus in der Tabelle `windows` auf `elevated`. Verwende `unelevated` nur, wenn du keine Administratorrechte hast oder das Setup mit erhöhten Rechten fehlschlägt.

```toml
[windows]
sandbox = "elevated"   # Recommended
# sandbox = "unelevated" # Fallback if admin permissions/setup are unavailable

#### Modus der Websuche

Codex aktiviert die Websuche standardmäßig für lokale Chats und liefert Ergebnisse aus einem Cache für die Websuche. Der Cache ist ein von OpenAI gepflegter Index von Webergebnissen. Der Cache-Modus liefert daher bereits indexierte Ergebnisse, statt Webseiten live abzurufen. Das verringert das Risiko von Prompt Injection durch beliebige Live-Inhalte. Du solltest Webergebnisse dennoch als nicht vertrauenswürdig behandeln. Wenn du `--yolo` oder eine andere [Sandbox-Einstellung mit Vollzugriff](/de-DE/codex/agent-approvals-security#common-sandbox-and-approval-combinations) verwendest, liefert die Websuche standardmäßig Live-Ergebnisse. Wähle über `web_search` einen Modus aus:

- `"cached"` (Standard) liefert Ergebnisse aus dem Cache der Websuche.
- `"indexed"` erlaubt externen Webzugriff nur, wenn der Suchindex die Anfrage freigibt.
- `"live"` ruft die neuesten Daten aus dem Web ab (entspricht `--search`).
- `"disabled"` deaktiviert das Tool für die Websuche.

```toml
web_search = "cached"  # default; serves results from the web search cache
# web_search = "indexed" # gate external web access through the search index
# web_search = "live"  # fetch the most recent data from the web (same as --search)
# web_search = "disabled"

#### Reasoning-Aufwand

Passe den Reasoning-Aufwand des Modells an, sofern es diese Einstellung unterstützt.

```toml
model_reasoning_effort = "high"

#### Kommunikationsstil

Lege für unterstützte Modelle den standardmäßigen Kommunikationsstil fest.

```toml
personality = "friendly" # or "pragmatic" or "none"

Diese Einstellung kannst du später in einer laufenden Sitzung mit `/personality` oder bei Verwendung der APIs des App Server pro Thread oder Turn überschreiben.

#### TUI-Tastenbelegung

Passe unter `tui.keymap` die Tastenkürzel im Terminal an. Bestimmte Aktionen im Editor greifen ersatzweise auf entsprechende Belegungen unter `tui.keymap.global` zurück. Kontextspezifische Belegungen haben Vorrang, sofern sie unterstützt werden. Eine leere Liste entfernt die Tastenbelegung der Aktion.

```toml
[tui.keymap.global]
open_transcript = "ctrl-t"

[tui.keymap.composer]
submit = ["enter", "ctrl-m"]

[tui.keymap.chat]
interrupt_turn = "f12"

#### Befehlsumgebung

Lege fest, welche Umgebungsvariablen Codex an gestartete Befehle weitergibt. Verwende
schlüsselbasierte Filter, um nur die benötigten Variablen beizubehalten:

```toml
[shell_environment_policy]
ignore_default_excludes = false

[shell_environment_policy.filters]
"PATH" = "include"
"HOME" = "include"

`ignore_default_excludes` ist standardmäßig auf `true` gesetzt. Dadurch entfällt die automatische Filterung
von Variablennamen, die `KEY`, `SECRET` oder `TOKEN` enthalten. Setze die Option auf `false`,
wenn du diese automatische Filterung verwenden möchtest. Weitere Informationen zu Ausschlussregeln, zur Priorität und
zur bisherigen Konfiguration findest du unter [Richtlinie für
die Shell-Umgebung](/de-DE/codex/config-file/config-advanced#shell-environment-policy).

#### Log-Verzeichnis

Ändere den Speicherort für lokale Log-Dateien von Codex. Wenn du `log_dir` ausdrücklich festlegst, wird außerdem
das optionale TUI-Log im Klartext, `codex-tui.log`, in diesem Verzeichnis aktiviert.

```toml
log_dir = "/absolute/path/to/codex-logs"

Für einzelne Ausführungen kannst du den Speicherort auch über die CLI festlegen:

```bash
codex -c log_dir=./.codex-log

## Feature-Flags

Verwende die Tabelle `[features]` in `config.toml`, um optionale und experimentelle Funktionen zu aktivieren oder zu deaktivieren.

### Gängige Feature-Flags

| Schlüssel                  |        Standard        | Reifegrad     | Beschreibung                                                                              |
| -------------------- | :-------------------: | ------------ | ---------------------------------------------------------------------------------------- |
| `apps`               |         true          | Stabil       | App-Integrationen (Konnektoren) aktivieren                                                      |
| `goals`              |         true          | Stabil       | Dauerhaft gespeicherte Ziele und automatische Fortsetzung aktivieren                                        |
| `hooks`              |         true          | Stabil       | Lifecycle-Hooks aus `hooks.json` oder aus dem Inline-Abschnitt `[hooks]` aktivieren. Siehe [Hooks](/de-DE/codex/hooks). |
| `fast_mode`          |         true          | Stabil       | Die Auswahl des Schnellmodus und den Codepfad für `service_tier = "fast"` aktivieren                          |
| `memories`           |         false         | Experimentell | [Erinnerungen](/de-DE/codex/customization/memories) aktivieren                                         |
| `multi_agent`        |         true          | Stabil       | Tools für die Zusammenarbeit von Subagenten aktivieren                                                      |
| `personality`        |         true          | Stabil       | Bedienelemente zur Auswahl der Persönlichkeit aktivieren                                                    |
| `remote_plugin`      |         true          | Stabil       | Den Remote-Katalog für Plug-ins aktivieren                                                         |
| `shell_snapshot`     |         true          | Stabil       | Eine Momentaufnahme deiner Shell-Umgebung erstellen, um wiederholt ausgeführte Befehle zu beschleunigen                            |
| `shell_tool`         |         true          | Stabil       | Das standardmäßig verwendete Tool `shell` aktivieren                                                          |
| `unified_exec`       | `true` außer unter Windows | Stabil       | Das vereinheitlichte, PTY-gestützte exec-Tool verwenden                                                     |
| `web_search`         |         true          | Veraltet   | Veralteter Schalter; verwende vorzugsweise die Einstellung `web_search` auf oberster Ebene                                 |
| `web_search_cached`  |         false         | Veraltet   | Veralteter Schalter, der auf `web_search = "cached"` abgebildet wird, wenn die Einstellung nicht festgelegt ist                            |
| `web_search_request` |         false         | Veraltet   | Veralteter Schalter, der auf `web_search = "live"` abgebildet wird, wenn die Einstellung nicht festgelegt ist                              |

  Diese Tabelle enthält gängige Flags für die Nutzung von Codex, aber nicht jede interne oder
  noch in Entwicklung befindliche Funktion. In der Spalte „Reifegrad“ stehen Bezeichnungen wie
  Experimentell, Beta und Stabil. Unter [Reifegrad von
  Funktionen](/de-DE/codex/feature-maturity) erfährst du, wie diese Bezeichnungen zu verstehen sind.

Lass Funktionsschlüssel weg, damit ihre Standardwerte gelten.

Informationen zur Konfiguration von Lifecycle-Hooks findest du unter [Hooks](/de-DE/codex/hooks).

### Funktionen aktivieren

- Füge in `config.toml` unter `[features]` den Eintrag `feature_name = true` hinzu.
- Führe in der CLI `codex --enable feature_name` aus.
- Führe `codex --enable feature_a --enable feature_b` aus, um mehrere Funktionen zu aktivieren.
- Um eine Funktion zu deaktivieren, setze den Schlüssel in `config.toml` auf `false`.
