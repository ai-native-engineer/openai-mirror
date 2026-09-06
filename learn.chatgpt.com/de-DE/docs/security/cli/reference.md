<!-- source: https://learn.chatgpt.com/de-DE/docs/security/cli/reference -->

Mit dieser Referenz kannst du die von `codex-security` unterstützten Befehle, Flags,
Ausgabeformate und das Verhalten beim Beenden prüfen. Eine Anleitung für deinen ersten Scan findest du im
[CLI-Schnellstart](/de-DE/codex/security/cli).

  Das Paket `@openai/codex-security` ist öffentlich verfügbar. Für Scans benötigst du Zugriff auf
  Codex Security. Scans verwenden deine lokalen Berechtigungen und halten nicht an, um eine
  Genehmigung einzuholen. Lies vor dem Start den Abschnitt [Lokale
  Scanberechtigungen](#local-scan-permissions).

Führe die CLI mit `npx @openai/codex-security` aus.

## Befehlsübersicht

```text
usage: codex-security [--version] <command> [options]

Die CLI bietet folgende Befehle:

| Befehl                       | Zweck                                               |
| ----------------------------- | ----------------------------------------------------- |
| `codex-security scan`         | Einen Scan mit Codex Security ausführen.                            |
| `codex-security install-hook` | Einen Git-Pre-Commit-Sicherheitsscan installieren.               |
| `codex-security bulk-scan`    | Repositories ermitteln und fortsetzbare Massenscans ausführen.   |
| `codex-security scans`        | Gespeicherte Scanprotokolle auflisten, prüfen, vergleichen und abrufen. |
| `codex-security findings`     | Gespeicherte Sicherheitsbefunde prüfen und aktualisieren.            |
| `codex-security export`       | Abgeschlossene Befunde als CSV, JSON oder SARIF exportieren.     |
| `codex-security publish`      | Abgeschlossene Scanbefunde in Linear veröffentlichen.            |
| `codex-security validate`     | Einen oder mehrere potenzielle Sicherheitsbefunde prüfen.        |
| `codex-security patch`        | Ein oder mehrere Sicherheitsprobleme beheben.                    |
| `codex-security login`        | Anmelden, Anmeldedaten speichern oder den Anmeldestatus prüfen.  |
| `codex-security logout`       | Die gespeicherte Anmeldung entfernen.                            |
| `codex-security info`         | Metadaten zum SDK und zum mitgelieferten Plug-in ohne Schreibzugriff anzeigen.       |

Die CLI bietet außerdem folgende Integrationsbefehle:

| Befehl                      | Zweck                               |
| ---------------------------- | ------------------------------------- |
| `codex-security completions` | Skripte zur Shell-Vervollständigung erstellen.    |
| `codex-security mcp`         | Die CLI als MCP-Server registrieren.    |
| `codex-security skills`      | Skills von Codex Security mit Agenten synchronisieren. |

Alle verfügbaren Befehle auflisten:

```bash
npx @openai/codex-security --help

Füge `--help` zu einem Befehl hinzu, um dessen Argumente und Optionen anzuzeigen:

```bash
npx @openai/codex-security scan --help

`codex-security --version` gibt die installierte Version aus und wird anschließend beendet.
`codex-security info --json` gibt die Versionen des SDK und des mitgelieferten Plug-ins aus.
Keiner der beiden Befehle erfordert Python.

### Befehle ermitteln und Agenten anbinden

Gib das für Agenten lesbare Befehlsmanifest aus:

```bash
npx @openai/codex-security --llms

Zeige das Schema der Scan-Argumente als JSON an:

```bash
npx @openai/codex-security scan --schema --format json

Erstelle Shell-Vervollständigungen für Bash:

```bash
npx @openai/codex-security completions bash

Ersetze für die jeweilige Shell `bash` durch `zsh` oder `fish`.

Scanergebnisse unterstützen `--format toon|json|yaml|jsonl` und `--full-output`. Die Option
`--format` auf Framework-Ebene ist unabhängig von `--export-format`. Diese Option legt
das Format eines Artefakts fest, das aus einem abgeschlossenen Scan exportiert wird. Die globale Befehlshilfe
führt auch `md` auf, Scanergebnisse unterstützen jedoch keine Markdown-Ausgabe.

Registriere die CLI als MCP-Server:

```bash
npx @openai/codex-security mcp add

Synchronisiere Skills von Codex Security mit deinen Agenten:

```bash
npx @openai/codex-security skills add

Über MCP ist nur der Metadatenbefehl `info` ohne Schreibzugriff verfügbar. Scans, Exporte,
Authentifizierung, Validierung und das Erstellen von Patches bleiben der CLI vorbehalten.

## `codex-security scan`

Führe einen Scan für ein Repository, ausgewählte Pfade, committete Änderungen oder den
Arbeitsbaum aus.

```text
usage: codex-security scan [-h] [--auth {auto,chatgpt,api-key}]
                           [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                           [--path PATH | --diff BASE | --working-tree]
                           [--head HEAD] [--base BASE]
                           [--knowledge-base PATH] [--scan-prompt-file FILE]
                           [--post-scan-prompt-file FILE]
                           [--mode {standard,deep}] [--workers N]
                           [--subagents N] [--stop-after-no-new N]
                           [--max-discovery-runs N] [--max-time-hours HOURS]
                           [--model MODEL]
                           [--effort {minimal,low,medium,high,xhigh,max}]
                           [--output-dir DIR]
                           [--archive-existing]
                           [--plugin-path PATH] [--python PATH]
                           [--codex KEY=VALUE] [--fail-on-severity LEVEL]
                           [--patch] [--patch-severity {critical,high,medium,low}]
                           [--create-pr]
                           [--max-cost USD] [--dry-run] [--headless] [--verbose]
                           [--json] [--format {toon,json,yaml,jsonl}]
                           [--full-output] [repository]

Für `repository` wird standardmäßig das aktuelle Verzeichnis verwendet.

### Authentifizierung für Scans auswählen

Mit `--auth auto`, der Standardeinstellung, werden Anmeldedaten automatisch ausgewählt. Wenn
eine ChatGPT-Anmeldung und entweder `OPENAI_API_KEY` oder `CODEX_API_KEY` verfügbar sind,
fragen interaktive Scans mit Textausgabe, welche Anmeldedaten verwendet werden sollen. CI-Scans,
JSON- und JSONL-Scans sowie andere Scans ohne interaktives Terminal verwenden den API-Schlüssel
aus der Umgebung. Testläufe fragen keine Anmeldedaten ab und laden auch keine.

Übergib `--auth chatgpt`, um deine gespeicherten Anmeldedaten zu verwenden:

```bash
npx @openai/codex-security scan . --auth chatgpt

Übergib `--auth api-key`, um einen API-Schlüssel aus der Umgebung zu verwenden:

```bash
npx @openai/codex-security scan . --auth api-key

Um gespeicherte Anmeldedaten als Standard für die automatische Auswahl festzulegen, führe
`unset OPENAI_API_KEY CODEX_API_KEY` aus.

### OpenRouter oder Fireworks verwenden

Wähle OpenRouter mit dem zugehörigen API-Schlüssel und einem explizit angegebenen Modell aus:

```bash

npx @openai/codex-security scan . \
  --provider openrouter \
  --model anthropic/claude-sonnet-4.5

Wähle Fireworks mit dem zugehörigen API-Schlüssel und einem explizit angegebenen Modell aus:

```bash

npx @openai/codex-security scan . \
  --provider fireworks \
  --model accounts/fireworks/models/qwen3-235b-a22b

Beide Anbieter unterstützen auch `bulk-scan`.

### Amazon Bedrock verwenden

Wähle Amazon Bedrock mit `--provider amazon-bedrock` aus und gib ein bestimmtes
Bedrock-Modell mit `--model` an:

```bash
npx @openai/codex-security scan . \
  --provider amazon-bedrock \
  --model openai.gpt-5.6-sol

Setze `AWS_REGION` und authentifiziere dich mit `AWS_BEARER_TOKEN_BEDROCK`, regulären
AWS-Zugriffsschlüsseln, einem AWS-Profil, einer Webidentität, Container-Anmeldedaten oder der
standardmäßigen AWS-Anmeldedatenkette. Bedrock-Scans verwenden AWS-Anmeldedaten anstelle von
`--auth`, einer ChatGPT-Anmeldung oder einem OpenAI-API-Schlüssel. Sowohl `scan` als auch `bulk-scan`
unterstützen `--provider`.

### Scanziel auswählen

Wähle für jeden Scan einen Zieltyp aus.

| Argument                 | Beschreibung                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| `--path PATH`            | Scanne einen Pfad relativ zum Repository. Verwende das Flag mehrfach, um weitere Pfade zu scannen.         |
| `--diff BASE`            | Scanne committete Änderungen von `BASE` bis `--head`. Die Head-Revision ist standardmäßig `HEAD`.    |
| `--head HEAD`            | Lege die Head-Revision für `--diff` fest.                                             |
| `--working-tree`         | Scanne zum Commit vorgemerkte und nicht vorgemerkte Änderungen gegenüber `--base`. Die Basisrevision ist standardmäßig `HEAD`. |
| `--base BASE`            | Lege die Basisrevision für `--working-tree` fest.                                     |
| `--mode {standard,deep}` | Wähle den Scanmodus aus. Standardmäßig wird `standard` verwendet.                                |

`--path`, `--diff` und `--working-tree` schließen sich gegenseitig aus. `--head`
erfordert `--diff` und `--base` erfordert `--working-tree`. Der Deep-Modus unterstützt
Repositories und Pfade als Ziele.

Bei Diff- und Working-Tree-Scans muss das Repository-Argument auf das Stammverzeichnis des
Git-Worktrees verweisen. Die ausgewählten Refs müssen in diesem Checkout vorhanden sein.

Scanne das gesamte Repository:

```bash
npx @openai/codex-security scan .

Scanne ausgewählte Pfade:

```bash
npx @openai/codex-security scan . --path src --path tests

Scanne committete Änderungen:

```bash
npx @openai/codex-security scan . --diff origin/main --head HEAD

Scanne gestagte und nicht gestagte Änderungen:

```bash
npx @openai/codex-security scan . --working-tree --base HEAD

Führe eine gründlichere Überprüfung des Repositorys durch:

```bash
npx @openai/codex-security scan . --mode deep

### Tiefenscans konfigurieren

Verwende diese Optionen mit `--mode deep`, um die Parallelität und Laufzeit der Worker zu steuern:

| Argument                 | Beschreibung                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `--workers N`            | Maximale Anzahl parallel ausgeführter unabhängiger Worker für Standardscans. Standardwert: `4`.                |
| `--subagents N`          | Pro Worker verfügbare Subagenten. Standardwert: `3`.                                   |
| `--stop-after-no-new N`  | Beenden, wenn `N` aufeinanderfolgende abgeschlossene Worker-Scans keine neuen Probleme finden. Standardwert: `4`. |
| `--max-discovery-runs N` | Maximale Gesamtzahl unabhängiger Durchläufe von Standardscans. Standardwert: `40`.                       |
| `--max-time-hours HOURS` | Zeitlimit für die Ausführung von Workern in Stunden. Standardwert: `96`; auch Dezimalwerte sind zulässig.             |

`--subagents` akzeptiert null oder eine positive ganze Zahl. `--max-time-hours` akzeptiert eine
positive Zahl, die höchstens `96` beträgt. Für die übrigen Optionen ist eine positive
ganze Zahl erforderlich. Diese Optionen stehen für Standardscans nicht zur Verfügung.

Verwende beispielsweise zwei Worker, lasse bis zu zehn Durchläufe zu und beende die Ausführung
der Worker nach 1,5 Stunden:

```bash
npx @openai/codex-security scan . \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

Nach Ablauf des Zeitlimits beendet der Scan noch aktive Worker, bewahrt die abgeschlossenen
Scan-Ergebnisse auf und fasst sie im Abschlussbericht zusammen. Schließt kein Worker die
Überprüfung des Quellcodes ab, erfasst der Scan eine teilweise Abdeckung und gibt den Exit-Code `2` zurück.

Lege dauerhafte Standardwerte in `~/.codex/codex-security/config.toml` fest oder in
`$CODEX_HOME/codex-security/config.toml`, wenn du `CODEX_HOME` festlegst:

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

Kommandozeilenoptionen überschreiben diese Standardwerte. `scan --workers` steuert
unabhängige Worker für Standardscans innerhalb eines Tiefenscans; `bulk-scan --workers`
steuert parallel ausgeführte Repository-Scans. Lege `stop_after_consecutive_errors` ausschließlich
in der TOML-Datei fest; der Standardwert ist `3`.

### Sicherheitskontext hinzufügen

Verwende `--knowledge-base PATH`, um Architekturdokumente, Bedrohungsmodelle
oder Sicherheitsrichtlinien bereitzustellen. Wiederhole die Option für weitere Dateien oder Verzeichnisse:

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Unterstützt werden Dateien mit den Endungen `.md`, `.markdown`, `.txt`, `.pdf` und `.docx`.
Die CLI durchsucht Verzeichnisse rekursiv, lehnt verknüpfte Eingabepfade ab,
überspringt verknüpfte Verzeichniseinträge und übernimmt extrahierte Dokumentinhalte
nicht in die gespeicherten Scan-Ergebnisse.

### Scan-Anweisungen hinzufügen

Um Scan-Anweisungen hinzuzufügen, gib mit
`--scan-prompt-file` eine Text- oder Markdown-Datei an. Verwende `--post-scan-prompt-file`, um Folgeanweisungen
nach erfolgreichen Scans sowie nach Scans mit unvollständiger Abdeckung oder Fehlern
in derselben authentifizierten Sitzung auszuführen:

```bash
npx @openai/codex-security scan . \
  --scan-prompt-file security-focus.md \
  --post-scan-prompt-file follow-up.md

Nutze den Scan-Prompt beispielsweise, um den Fokus auf Autorisierungsgrenzen zu legen, und fordere
mit der Folgeanweisung dazu auf, eine neue `post-scan-summary.md` im Scan-Verzeichnis zu erstellen.
Schlägt die Folgeanweisung fehl, gibt die CLI eine Warnung aus und behält den abgeschlossenen Scan.
Nach einem Abbruch oder wenn der Scan sein Kostenlimit
erreicht, wird die Folgeanweisung nicht ausgeführt.

### Ausgabe- und Richtlinienoptionen festlegen

Verwende diese Optionen, um Artefakte aufzubewahren, frühere Ergebnisse zu sichern oder ein
maschinenlesbares Ergebnis zu erstellen.

| Argument                   | Beschreibung                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `--output-dir DIR`         | Scan-Artefakte in ein privates Verzeichnis außerhalb des übergeordneten Git-Worktrees schreiben. Standardmäßig wird der dauerhafte Statusspeicher von Codex Security verwendet. |
| `--archive-existing`       | Vorhandene Ergebnisse nach `DIR.previous-<timestamp>-<id>` verschieben und mit einem leeren Ausgabeverzeichnis beginnen. Erfordert `--output-dir`.  |
| `--fail-on-severity LEVEL` | Exit-Code `1` zurückgeben, wenn ein abgeschlossener Scan einen Befund mit mindestens dem Schweregrad `critical`, `high`, `medium` oder `low` meldet.                  |
| `--patch`                  | Ausgewählte Befunde nach einem vollständigen Scan beheben und überprüfen.                                                                      |
| `--patch-severity LEVEL`   | Befunde ab dem Schweregrad `critical`, `high`, `medium` oder `low` per Patch beheben. Standardwert: `low`.                                        |
| `--create-pr`              | Verifizierte Patch-Dateien committen und einen Pull Request auf GitHub erstellen. Erfordert `--patch`.                                              |
| `--max-cost USD`           | Einen Scan beenden, wenn seine geschätzten Modellkosten den angegebenen Betrag in USD überschreiten.                                                  |
| `--dry-run`                | Repository, Ziel, Wissensdatenbank, Ausgabeverzeichnis und Codex-Konfiguration prüfen, ohne einen Scan zu starten.             |
| `--headless`               | Fortschritt als Klartext statt im interaktiven Scan-Dashboard anzeigen.                                                          |
| `--verbose`                | Diagnoseinformationen zu Lebenszyklus, Authentifizierung, Fortschritt und Kosten mit ausgeblendeten sensiblen Daten auf stderr ausgeben.                                          |
| `--json`                   | Manifest, Befunde, Abdeckung, Pfade und Turn-Metadaten als einzelnes JSON-Dokument ausgeben.                                           |
| `--format FORMAT`          | Das vollständige Scan-Ergebnis als `toon`, `json`, `yaml` oder `jsonl` ausgeben.                                                        |
| `--full-output`            | Das vollständige Ergebnis im standardmäßigen strukturierten Ausgabeformat ausgeben.                                                        |

Das Kostenlimit ist ein Schätzwert und keine feste Ausgabenobergrenze. Bereits laufende
Anfragen können das Limit bei ihrem Abschluss geringfügig überschreiten. Erreicht ein Tiefenscan das Limit,
nachdem Codex Security die Ergebnisse abgeschlossener Worker zusammengeführt hat, versiegelt die CLI die
verfügbaren Ergebnisse, kennzeichnet die Abdeckung als `partial` und gibt den Exit-Code `2` zurück.
Andernfalls gibt sie `2` zurück und belässt gegebenenfalls vorhandene Teilergebnisse auf dem Datenträger.

Wenn du `--output-dir` weglässt, bleiben die Ergebnisse unter
`$CODEX_HOME/state/plugins/codex-security/scans/<repository>` dauerhaft gespeichert. Für `CODEX_HOME`
gilt standardmäßig `~/.codex`. Lege `CODEX_SECURITY_STATE_DIR` fest, um die Ergebnisse stattdessen unter
`$CODEX_SECURITY_STATE_DIR/scans/<repository>` zu speichern. Diese Verzeichnisse können
Quelltextauszüge und Details zu Schwachstellen enthalten. Verwalte deshalb ihre Berechtigungen
und Aufbewahrung entsprechend.

Die Workbench speichert den Scan-Verlauf in
`$CODEX_HOME/state/plugins/codex-security/workbench.sqlite3`. Wenn du
`CODEX_SECURITY_STATE_DIR` festlegst, wird auch die Workbench-Datenbank verschoben.

Das Ausgabeverzeichnis muss außerhalb des gescannten Verzeichnisses und jedes übergeordneten
Git-Worktrees liegen. Mit
`--archive-existing` kann ein Scan ein vorhandenes Ergebnisverzeichnis ersetzen.

So bewahrst du frühere Ergebnisse auf, bevor du ein Ausgabeverzeichnis erneut verwendest:

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --archive-existing

Scans dienen standardmäßig nur der Berichterstellung. Füge `--fail-on-severity` hinzu, um in CI eine
Richtlinie für Schweregrade auszuwerten:

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --json \
  --fail-on-severity high \
  > /path/outside/repository/codex-security.json

Ein Testlauf prüft lokale Eingaben einschließlich der Dokumente aus der Wissensdatenbank, ohne
Anmeldedaten zu laden, Codex zu starten oder den Python-Interpreter des Plug-ins
zu prüfen:

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --dry-run

### Laufzeit konfigurieren

Verwende Laufzeitoptionen, wenn du ein Modell, einen Interpreter, ein Plug-in oder
einen Codex-Konfigurationswert explizit angeben musst.

| Argument                                                  | Beschreibung                                                                                              |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `--auth {auto,chatgpt,api-key}`                           | Anmeldedaten für den Scan auswählen. Standardwert: `auto`.                                                      |
| `--provider {openai,openrouter,fireworks,amazon-bedrock}` | Inferenzanbieter auswählen. Standardwert: `openai`.                                                  |
| `--model MODEL`                                           | Modell auswählen. Standardwert: `gpt-5.6-sol`. Erforderlich für OpenRouter, Fireworks und Amazon Bedrock.  |
| `--effort {minimal,low,medium,high,xhigh,max}`            | Reasoning-Aufwand des Modells auswählen. Standardwert: `xhigh`.                                             |
| `--plugin-path PATH`                                      | Ein Codex-Security-Plugin aus einem Verzeichnis oder einer ZIP-Datei anstelle des mitgelieferten Plug-ins verwenden.                             |
| `--python PATH`                                           | Den Python-Interpreter für die Laufzeitumgebung des Plug-ins auswählen.                                                    |
| `--codex KEY=VALUE`                                       | Einen Wert in der isolierten Codex-Konfiguration überschreiben. Werte werden in TOML-Syntax angegeben. Wiederhole das Flag für weitere Werte. |

So wählst du ein anderes Modell und einen anderen Reasoning-Aufwand aus, ohne TOML zu schreiben:

```bash
npx @openai/codex-security scan . --model gpt-5.6-terra --effort high

Setze über `--codex` übergebene String-Werte in Anführungszeichen, damit der TOML-Parser einen
String erhält:

```bash
npx @openai/codex-security scan . --codex 'model="gpt-5.6-terra"'

## `codex-security install-hook`

Installiere eine Git-Pre-Commit-Sicherheitsprüfung für das aktuelle Repository:

```bash
npx @openai/codex-security install-hook

Die Prüfung scannt vor jedem Commit vorgemerkte und nicht vorgemerkte Änderungen und blockiert
Commits bei Befunden mit hohem Schweregrad oder Scan-Fehlern. Sie berücksichtigt `core.hooksPath` und ersetzt
kein vorhandenes Pre-Commit-Skript. Bei Bedarf kannst du einen anderen
Schwellenwert für den Schweregrad festlegen:

```bash
npx @openai/codex-security install-hook . --fail-on-severity medium

## `codex-security bulk-scan`

Finde GitHub-Repositorys und scanne sie oder führe anhand einer CSV-Datei mit
Repositorys einen fortsetzbaren Scan aus:

Eine vollständige Anleitung zur Suche nach GitHub-Repositorys, zu CSV-Inventarlisten,
Kampagnenergebnissen und containerisierten Scans findest du unter [Massenscans zur Sicherheitsprüfung
durchführen](/de-DE/codex/security/cli/bulk-scans).

```text
usage: codex-security bulk-scan [input] [--output-dir DIR]
                                [--workers N] [--mode {standard,deep}]
                                [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                                [--model MODEL]
                                [--effort {minimal,low,medium,high,xhigh,max}]
                                [--knowledge-base PATH]
                                [--scan-prompt-file FILE]
                                [--post-scan-prompt-file FILE]
                                [--max-attempts N] [--plugin-path PATH]
                                [--python PATH] [--codex KEY=VALUE]

Führe `npx @openai/codex-security bulk-scan` ohne Argumente aus, um
Repositorys interaktiv auszuwählen. Dafür musst du bei der GitHub CLI angemeldet sein.

So wählst du bei der interaktiven Suche ein Modell und den Reasoning-Aufwand aus:

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

Gib für eine vorbereitete Repository-Liste eine CSV-Datei und `--output-dir` an:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Die CSV-Datei muss die Spalten `id`, `repository` und `revision` enthalten. Revisionen müssen
vollständige Commit-Hashes sein. Mit den optionalen Spalten `scope`, `mode` und `prompt` lassen sich
einzelne Repositorys konfigurieren:

```csv
id,repository,revision,scope,mode,prompt
service,https://github.com/example/service.git,0123456789abcdef0123456789abcdef01234567,src,standard,Review authorization boundaries.

Mit `--knowledge-base PATH` stellst du Sicherheitsdokumente für alle
Repositorys bereit. Mit `--scan-prompt-file FILE` ergänzt du gemeinsame Scan-Anweisungen. Die
CSV-Spalte `prompt` fügt nach diesem gemeinsamen
Prompt zusätzliche Anweisungen für das jeweilige Repository hinzu. `--post-scan-prompt-file FILE` führt nach jedem
Scan Folgeanweisungen aus, auch bei unvollständiger Abdeckung oder Scan-Fehlern. Nach einem
Abbruch oder wenn ein Scan sein Kostenlimit erreicht, werden sie nicht ausgeführt.

`--workers` begrenzt die Anzahl gleichzeitiger Repository-Scans und ist standardmäßig auf `4` festgelegt. Für `--mode`
gilt standardmäßig `standard`, für `--max-attempts` gilt `1`. Lege
`--max-attempts` fest, um bei Repository- oder Scan-Fehlern erneute Versuche zuzulassen. Abgeschlossene Scans mit
unvollständiger Abdeckung werden nicht wiederholt. Ihre Ergebnisse bleiben verfügbar und der
Befehl gibt den Exit-Code `2` zurück.

Führe denselben Befehl erneut aus, um mit einem vorhandenen Ausgabeverzeichnis fortzufahren. Die CLI
überspringt abgeschlossene Scans, einschließlich Scans mit unvollständiger Abdeckung.

Informationen zu containerisierten Kampagnen findest du unter [Massenscans in
Docker durchführen](/de-DE/codex/security/cli/bulk-scans#run-bulk-scans-in-docker).

## `codex-security scans`

### Gespeicherte Scans finden

Gespeicherte Scans für das aktuelle Verzeichnis auflisten:

```bash
npx @openai/codex-security scans

Scans für ein anderes Repository auflisten:

```bash
npx @openai/codex-security scans list /path/to/repository

Scans finden, die in einem bestimmten Ausgabeverzeichnis gespeichert sind:

```bash
npx @openai/codex-security scans list --scan-root /path/outside/repository/results

### Scan untersuchen oder wiederholen

Ergebnisse und Konfiguration eines gespeicherten Scans anzeigen:

```bash
npx @openai/codex-security scans show SCAN_ID

Füge `--show-linked-findings` hinzu, um Links zu Befunden aus früheren Scans einzubeziehen.

Den Scan mit seiner ursprünglichen Konfiguration für den aktuellen Checkout erneut ausführen:

```bash
npx @openai/codex-security scans rerun SCAN_ID

Die erneute Ausführung erfordert die beim ursprünglichen Scan protokollierte Plug-in-Version.
Weicht die installierte Version davon ab, bricht der Befehl ab, statt den Scan mit einem
anderen Plug-in auszuführen.

### Gespeicherte Scan-Protokolle untersuchen

Lies alle gespeicherten Sitzungsereignisse eines Scans und seiner Worker. Diese Protokolle
sind nicht geschwärzt und können Quellcode oder Anmeldedaten enthalten. Prüfe sie daher,
bevor du sie weitergibst:

```bash
npx @openai/codex-security scans logs SCAN_ID

Füge `--json` hinzu, um ein maschinenlesbares Ergebnis mit sämtlichen Informationen zu erhalten.

### Befunde abgleichen und vergleichen

Vergleiche zwei Scans, um neue, fortbestehende, erneut geöffnete, behobene und unbekannte
Befunde zu ermitteln:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

Beim Vergleich werden Befunde mit derselben Grundursache automatisch abgeglichen
und gespeicherte Zuordnungen wiederverwendet. Um Zuordnungen explizit zu speichern, verwende `scans match`:

```bash
npx @openai/codex-security scans match PREVIOUS_SCAN_ID CURRENT_SCAN_ID

Ein Befund gilt als unbekannt, wenn der spätere Scan eine unvollständige Abdeckung aufweist oder
die ursprüngliche Position des Befunds nicht abdeckt. Füge `--force` zu `match` hinzu, wenn du
eine vorhandene Zuordnung neu berechnen musst.

So gleichst du alle abgeschlossenen Scans des aktuellen Repositorys ab, einschließlich Scans aus
anderen Checkouts:

```bash
npx @openai/codex-security scans match --all

Auch bei erneuter Ausführung mit derselben Konfiguration können Scan-Ergebnisse variieren. Abgleich und
Vergleich machen Änderungen nachvollziehbar. Sie sorgen weder für deterministische Ergebnisse noch belegen sie,
dass eine Schwachstelle nicht mehr besteht. Verwende `validate`, um einen sicherheitskritischen
Befund anhand des aktuellen Codes erneut zu prüfen.

## `codex-security findings`

Offene Befunde aus den Scans des aktuellen Repositorys auflisten:

```bash
npx @openai/codex-security findings list

Übergib einen Repository-Pfad, um einen anderen Checkout zu untersuchen:

```bash
npx @openai/codex-security findings list /path/to/repository

Füge `--json` hinzu, um eine strukturierte Ausgabe zu erhalten. Die Liste zeigt Befunde aus dem
neuesten Scan sowie frühere Befunde, die in diesem Scan nicht bestätigt wurden.

Beachte, dass frühere Befunde offen bleiben, bis sie behoben oder verworfen werden
(fehlen sie im neuesten Scan, gilt das nicht als Nachweis, dass sie behoben wurden).

So erfasst du einen überprüften Befund als falsch positiv:

```text
usage: codex-security findings false-positive OCCURRENCE_ID
                       --reason REASON

Untersuche den gespeicherten Scan, um das Vorkommen des Befunds zu ermitteln:

```bash
npx @openai/codex-security scans show SCAN_ID

Dokumentiere konkret, warum es sich um einen falsch positiven Befund handelt:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

Die Begründung darf nicht leer sein. Codex Security speichert die Entscheidung für das
Repository und stellt sie künftigen Scans als Kontext bereit. Jeder Scan überprüft unabhängig
den aktuellen Quellcode, die Sicherheitskontrollen und die Erreichbarkeit erneut. Eine frühere Entscheidung
unterdrückt keine Regel, keinen Pfad und keine Schwachstellenklasse.

## `codex-security export`

Exportiere CSV, JSON oder SARIF aus einem abgeschlossenen, versiegelten Scan. Beim Export werden die
Scan-Artefakte vor dem Schreiben der Ausgabe validiert. Die Codex-Laufzeitumgebung und
Anmeldedaten bleiben unverändert.

```text
usage: codex-security export [--export-format {csv,json,sarif}]
                             [--output FILE|-] [--source-root PATH]
                             [--python PATH] scan_dir

`scan_dir` ist das Verzeichnis des abgeschlossenen Scans.

| Argument                           | Beschreibung                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| `--export-format {csv,json,sarif}` | Wählt das Exportformat aus. Der Standardwert ist `sarif`.                                           |
| `--output FILE\|-`                 | Schreibt das ausgewählte Format in eine Datei oder auf stdout. Standardmäßig wird eine Datei im aktuellen Verzeichnis erstellt. |
| `--source-root PATH`               | Fügt SARIF mithilfe eines Repository-Checkouts Fingerabdrücke von Quellcodezeilen hinzu.                          |
| `--python PATH`                    | Wählt den Python-Interpreter für den mitgelieferten Exporter aus.                                     |

`--source-root` funktioniert nur mit `--export-format sarif`. JSON übernimmt
das versiegelte Befunddokument unverändert. CSV enthält übertragbare Spalten mit Befunddaten und
keinen lokalen Triage-Status der Workbench.

Ohne `--output` schreibt die CLI im aktuellen Arbeitsverzeichnis SARIF in `results.sarif`, JSON in
`findings.json` und CSV in `findings.csv`.
Exporte können Quellcodeauszüge und Details zu Schwachstellen enthalten. Führe den Befehl
außerhalb des Repositorys aus oder übergib `--output` mit einem privaten Pfad außerhalb des
gescannten Checkouts.

SARIF in eine Datei schreiben:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root /path/to/repository \
  --output /path/outside/repository/exports/results.sarif

SARIF auf stdout schreiben:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root . \
  --output -

Befunde als JSON exportieren:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format json \
  --output /path/outside/repository/exports/findings.json

Befunde als CSV exportieren:

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format csv \
  --output /path/outside/repository/exports/findings.csv

## `codex-security publish scan`

Alle Befunde eines abgeschlossenen Scans in Linear veröffentlichen:

```text
usage: codex-security publish scan [SCAN_DIR] --to linear
                                   [--linear-team TEAM_ID]
                                   [--project PROJECT_ID]
                                   [--linear-api-key KEY]
                                   [--linear-assignee EMAIL_OR_USER_ID]
                                   [--dry-run] [--json]

`SCAN_DIR` muss einen abgeschlossenen, versiegelten Scan enthalten. Lasse die Angabe in einem interaktiven
Terminal weg, um einen abgeschlossenen Scan aus dem lokalen Scan-Verlauf auszuwählen. Zum Erstellen von Issues
müssen sowohl der Scan als auch seine Befunde im lokalen Scan-Verlauf vorhanden sein. Ein
Probelauf validiert die versiegelten Artefakte ohne diese Persistenzprüfung.

| Argument                             | Beschreibung                                                                                                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--to linear`                        | Veröffentlicht in Linear. Dieses Argument ist erforderlich.                                                                                                                    |
| `--linear-team TEAM_ID`              | Wählt das Linear-Team aus. Fehlt die Angabe, wird `CODEX_SECURITY_LINEAR_TEAM` verwendet. Eine der beiden Angaben ist erforderlich.                                                                 |
| `--project PROJECT_ID`               | Wählt ein Linear-Projekt aus. Fehlt die Angabe, wird `CODEX_SECURITY_LINEAR_PROJECT` verwendet. Ist keine der beiden Angaben festgelegt, werden Issues direkt im Team erstellt.                          |
| `--linear-api-key KEY`               | Verwendet für die direkte Veröffentlichung einen persönlichen API-Schlüssel von Linear. Fehlt die Angabe, wird `CODEX_SECURITY_LINEAR_API_KEY` verwendet.                                                         |
| `--linear-assignee EMAIL_OR_USER_ID` | Weist erstellte Issues anhand einer E-Mail-Adresse oder Linear-Benutzer-ID zu. Erfordert `--linear-api-key` oder `CODEX_SECURITY_LINEAR_API_KEY`. Ohne Angabe bleiben Issues unzugewiesen. |
| `--dry-run`                          | Bereitet Issue-Payloads vor, ohne Codex zu starten, Linear zu kontaktieren, Issues zu erstellen oder den Veröffentlichungsstatus zu speichern.                                                 |
| `--json`                             | Schreibt strukturierte Veröffentlichungsergebnisse auf stdout. Der Fortschritt wird weiterhin auf stderr ausgegeben.                                                                                      |

  Beschreibungen von Linear-Issues und Ausgaben eines Probelaufs können Quellcodeausschnitte
und Details zu Schwachstellen enthalten. Veröffentliche Inhalte nur in einem autorisierten Linear-Team oder
Linear-Projekt und behandle gespeicherte Ausgaben als vertraulich.

Bei jedem Aufruf außerhalb eines Probelaufs wird versucht, für jeden Befund ein neues Issue zu erstellen.
Vorhandene Issues werden bei einer erneuten Veröffentlichung desselben Scans weder abgeglichen noch aktualisiert oder wiederverwendet.
Schlägt die Veröffentlichung einzelner Befunde fehl, bleiben erfolgreich erstellte Issues erhalten und der Befehl
gibt den Exit-Code `2` zurück.
Wenn du `--json` verwendest, überprüfe vor einem erneuten Versuch die Ergebnisse `created` und `failed`,
um Duplikate zu vermeiden.

Sieh dir die Issue-Payloads vor der Veröffentlichung an:

```bash
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --dry-run \
  --json

### Über die verbundene Linear-App veröffentlichen

Ohne einen Linear-API-Schlüssel startet der Befehl Codex mit deiner vorhandenen
Konfiguration und der verbundenen Linear-App. Melde dich vor der Veröffentlichung an
und verbinde Linear mit deinem Codex-Konto:

```bash
npx @openai/codex-security login
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --project PROJECT_ID

### Mit einem Linear-API-Schlüssel veröffentlichen

Wenn du `--linear-api-key` oder `CODEX_SECURITY_LINEAR_API_KEY` angibst, erfolgt die Veröffentlichung
direkt über die Linear-API, ohne Codex zu starten. Bei der direkten Veröffentlichung
bleiben Issues unzugewiesen, sofern du keine zuständige Person auswählst:

```bash

npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --linear-assignee teammate@example.com

Werte aus der Befehlszeile überschreiben die entsprechenden Umgebungsvariablen.
Verwende für API-Schlüssel vorzugsweise `CODEX_SECURITY_LINEAR_API_KEY` statt `--linear-api-key`, da
Befehlszeilenargumente im Shell-Verlauf und in Prozesslisten erscheinen können.

## `codex-security validate` und `codex-security patch`

Prüfe, ob ein potenzieller Befund zutrifft:

```bash
npx @openai/codex-security validate findings.json \
  "Possible SQL injection in src/query.ts:42"

Erstelle mit dem mitgelieferten Skill zur Problembehebung eine Korrektur:

```bash
npx @openai/codex-security patch findings.json \
  "Missing authorization check in src/routes.ts:18"

Jedes Positionsargument akzeptiert direkt eingegebenen Text oder einen Dateipfad. Diese Eingaben beziehen sich auf
das aktuelle Verzeichnis. Verwende `validate`, um einen Befund nach einer Korrektur oder dann erneut
zu prüfen, wenn er bei einem späteren Scan nicht mehr gemeldet wird. Der bloße Vergleich von Scans
belegt nicht, dass die Korrektur erfolgreich war.

Mit `--effort` kannst du für jeden der beiden Befehle den Reasoning-Aufwand festlegen:

```bash
npx @openai/codex-security validate "Possible SQL injection" --effort high

### Befunde nach einem Scan beheben

Verwende `scan --patch`, um Befunde nach einem vollständigen Scan zu beheben. Dafür ist
`@openai/codex-security` ab Version 0.1.15 erforderlich. Als Schwellenwert für den Schweregrad gilt standardmäßig
`low`. Dieser Befehl wählt Befunde mit hohem und kritischem Schweregrad aus:

```bash
npx @openai/codex-security scan . --patch --patch-severity high --json

Verifizierte und bereits behobene Befunde lösen `--fail-on-severity` nicht aus.

### Gespeicherte Befunde beheben

Übergib die ID eines Befunds oder eines Vorkommens, um den Befund in seinem ursprünglichen Repository zu beheben,
oder wähle Befunde aus einem gespeicherten Scan aus:

```bash
npx @openai/codex-security patch OCCURRENCE_ID
npx @openai/codex-security patch --scan SCAN_ID --severity high --json
npx @openai/codex-security patch --scan latest --severity medium

`--scan latest` wählt den zuletzt abgeschlossenen Scan für das aktuelle Repository aus.
Befehle für gespeicherte Befunde unterstützen `--json`; bei direkt eingegebenem Text und Dateien ist dies nicht möglich.

Füge `--create-pr` hinzu, um nur verifizierte Patch-Dateien zu committen und mit der GitHub CLI
einen Pull Request zu öffnen:

```bash
npx @openai/codex-security patch --scan SCAN_ID --severity high --create-pr

Wenn der Push oder Pull Request fehlschlägt, führe den ausgegebenen Befehl `patch --resume-pr BRANCH`
im selben Repository aus, um es erneut zu versuchen.

### Linear-Issues beheben

Setze für einen persönlichen API-Schlüssel `CODEX_SECURITY_LINEAR_API_KEY` oder `LINEAR_API_KEY`
beziehungsweise für ein OAuth-Token `LINEAR_ACCESS_TOKEN`. Verwende bevorzugt eine Umgebungsvariable anstelle von
`--linear-api-key KEY`, damit der Schlüssel nicht im Shell-Verlauf erscheint.

Importiere ein Issue anhand seiner ID oder URL. Wiederhole `--linear-issue`, um mehrere
Issues auszuwählen:

```bash
npx @openai/codex-security patch --linear-issue SEC-123 --linear-issue SEC-124

Verwende `--linear-project`, um die offenen Issues eines Projekts auszuwählen. Ergänze `--linear-filter`,
um die Auswahl einzugrenzen:

```bash
npx @openai/codex-security patch --linear-project "Security backlog" \
  --linear-filter '{"labels":{"name":{"eq":"security"}}}'

Die CLI schließt abgeschlossene und abgebrochene Issues aus, sofern im Filter `state` nicht festgelegt ist.
Sie ändert die Linear-Issues nicht.

## `codex-security login`, `logout` und `info`

Melde dich interaktiv an:

```bash
npx @openai/codex-security login

Verwende die Geräteauthentifizierung auf einem Remote-System oder einem System ohne grafische Oberfläche:

```bash
npx @openai/codex-security login --device-auth

Überprüfe die aktuelle Anmeldung:

```bash
npx @openai/codex-security login status

Entferne die gespeicherte Anmeldung:

```bash
npx @openai/codex-security logout

Speichere einen API-Schlüssel, indem du ihn über stdin übergibst:

```bash
printenv OPENAI_API_KEY | npx @openai/codex-security login --with-api-key

Speichere ein Zugriffstoken für Unternehmen:

```bash
printenv CODEX_ACCESS_TOKEN | npx @openai/codex-security login --with-access-token

Sieh dir ohne Schreibzugriff die Metadaten des SDK und des mitgelieferten Plug-ins an:

```bash
npx @openai/codex-security info --json

Wenn du die CLI als MCP-Server bereitstellst, ist `info` der einzige verfügbare Befehl.
Scans, Exporte, Veröffentlichungen, Anmeldungen, Validierungen und das Einspielen von Patches sind weiterhin nur über die CLI möglich.

## Scan-Ausgabe lesen

Standardmäßig geben Scans Fortschrittsmeldungen, Abschlusszusammenfassungen und Fehler auf stderr aus,
ohne das vollständige Scan-Ergebnis auf stdout zu schreiben. Verwende `--json`,
`--format` oder `--full-output`, um strukturierte Scan-Ergebnisse auf stdout auszugeben.

Interaktive Terminals zeigen ein Live-Dashboard mit der aktuellen Scan-Phase,
den überprüften Dateien, Aktivitäten, der Token-Nutzung und den geschätzten Kosten. In CI und bei umgeleiteter
Ausgabe wird der Fortschritt als Klartext angezeigt. Füge `--headless` hinzu, um den Fortschritt auch in
einem interaktiven Terminal als Klartext auszugeben:

```bash
npx @openai/codex-security scan . --headless

Das Dashboard zeigt außerdem aktuelle Sitzungsdetails. Sie werden nicht bereinigt und können
Quellcode oder Anmeldedaten enthalten. Prüfe sie, bevor du sie weitergibst.

### Ausführliche Diagnoseausgaben

Füge `--verbose` hinzu, um bereinigte Diagnosedaten zu Lebenszyklus, Authentifizierung, Fortschritt und Kosten
auf stderr auszugeben:

```bash
npx @openai/codex-security scan . --verbose

Setze `CODEX_SECURITY_LOG_LEVEL=debug`, um dieselben Diagnoseausgaben ohne das
Flag zu aktivieren. `LOG_LEVEL=debug` aktiviert Diagnoseausgaben ebenfalls, wenn
`CODEX_SECURITY_LOG_LEVEL` nicht gesetzt ist.

### Zusammenfassung nach Abschluss

Ein abgeschlossener Scan gibt die Anzahl offener Befunde im Repository, die Aufschlüsselung nach Schweregrad,
die Abdeckung, die verstrichene Zeit, den Berichtspfad und das Ergebnisverzeichnis auf stderr aus.
Sofern verfügbar, werden auch die Token-Nutzung und die geschätzten Kosten angegeben:

```text
  REPORT    /path/to/scan/report.md

  FINDINGS  4 (3 confirmed this scan; 1 previously found; 1 critical, 2 high, 1 informational)
  COVERAGE  complete
  ELAPSED   1s
  TOKENS    1,250 input, 200 cached, 30 output
  RESULTS   /path/to/scan

Informative Befunde zählen zur Gesamtzahl in der Zusammenfassung. Schweregradrichtlinien
berücksichtigen ausschließlich Befunde der Stufen `critical`, `high`, `medium` und `low` aus dem aktuellen
Scan, nicht frühere Befunde, die in der Gesamtzahl für das Repository enthalten sind.

### JSON-Ausgabe

`scan --json` gibt ein vollständiges JSON-Dokument auf stdout aus. Seine oberste
Ebene ist wie folgt aufgebaut:

```text
manifest
repositoryFindings
findings
coverage
scanDir
threadId
reportPath
artifactsDir
sarifPath
cost
turn
  id
  status
  durationMs
  finalResponse
  usage

Beim [Patchen](#patch-findings-after-a-scan) enthält die JSON-Ausgabe zusätzlich die Patch-Ergebnisse
und einen gegebenenfalls erstellten Pull Request.

Fortschritt, Abschlusszusammenfassungen, Archivierungshinweise und Fehler werden weiterhin auf stderr ausgegeben.
Ein abgeschlossener Scan gibt das vollständige JSON-Ergebnis auch aus, wenn eine Schweregradrichtlinie
zum Exitcode `1` oder eine unvollständige Abdeckung zum Exitcode `2` führt.

  `codex-security scan --json` gibt ein JSON-Dokument aus. `codex exec --json`
  gibt einen Ereignisstrom im Format JSON Lines aus. Verwende das Ausgabeformat, das zum
  ausgeführten Befehl passt.

## Scan-Artefakte

Ein abgeschlossener Scan speichert den lesbaren Bericht und die strukturierten Artefakte zusammen:

```text
<scan-directory>/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

Die strukturierten Dateien erfüllen unterschiedliche Zwecke:

| Datei                    | Inhalt                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `scan-manifest.json`    | Scan-Identität, Status, Ziel, Umfang, erzeugende Instanz und Datensätze zu versiegelten Artefakten.                                                    |
| `findings.json`         | Befundkennungen, Schweregrad, Konfidenz, Taxonomie, Fundstellen, Belege, Validierung, Datenfluss, Erreichbarkeit und Behebung. |
| `coverage.json`         | Überprüfte Bereiche, Ausschlüsse, zurückgestellte Arbeiten, offene Fragen und Vollständigkeit der Abdeckung.                                        |
| `report.md`             | Lesbarer Scan-Bericht.                                                                                                           |
| `artifacts/`            | Begleitende Scan-Artefakte.                                                                                                      |
| `exports/results.sarif` | Beim Scan generiertes SARIF, sofern vorhanden.                                                                                  |

Für die Vollständigkeit der Abdeckung gibt es drei Werte:

- `complete`: Der Scan dokumentiert eine vollständige Abdeckung des ausgewählten Prüfbereichs.
- `partial`: Der Scan dokumentiert zurückgestellte Arbeiten oder andere Einschränkungen der Abdeckung.
- `unknown`: Der Scan meldet, dass die Vollständigkeit der Abdeckung unbekannt ist.

Prüfe zurückgestellte Bereiche, explizite Ausschlüsse und offene Fragen, bevor du die
Abdeckung als Nachweis für eine Sicherheitsentscheidung heranziehst.

## Exit-Codes und Signale

Die CLI verwendet folgende Exit-Codes:

| Exit-Code  | Bedingung                                                                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`   | Ein Scan wurde mit vollständiger Abdeckung abgeschlossen und erfüllte die Richtlinie für den Schweregrad, ein Sammelscan oder eine Veröffentlichung wurde fehlerfrei abgeschlossen oder ein anderer Befehl wurde erfolgreich ausgeführt.                  |
| `1`   | Ein abgeschlossener Scan meldet einen Befund mit dem konfigurierten oder einem höheren Schweregrad.                                                                                                       |
| `2`   | Die CLI hat einen Eingabe-, Laufzeit- oder Exportfehler erkannt, ein Scan weist eine unvollständige Abdeckung auf, ein Sammelscan enthält Repositorys mit Fehlern oder bei einer Veröffentlichung konnte mindestens ein Befund nicht veröffentlicht werden. |
| `130` | Ctrl-C hat einen Scan oder eine Veröffentlichung unterbrochen.                                                                                                                                     |
| `143` | SIGTERM hat einen Scan oder eine Veröffentlichung beendet.                                                                                                                                     |

Jeder Scan mit dem Abdeckungsstatus `partial` oder `unknown` gibt `2` zurück, auch ohne
Richtlinie für den Schweregrad. Wenn du eine strukturierte Ausgabe anforderst, schreiben abgeschlossene Scans und
teilweise abgeschlossene Veröffentlichungen die verfügbaren Ergebnisse weiterhin nach stdout. Nach einer
Unterbrechung oder einem Laufzeitfehler gibt die CLI den Speicherort einer eventuell vorhandenen
Teilausgabe aus.

## Lokale Berechtigungen für Scans

CLI- und SDK-Scans werden mit deinen lokalen Betriebssystemberechtigungen ausgeführt. Jeder Scan
verwendet das Dateisystemprofil `codex_security_scan` und setzt `approvalPolicy` auf
`"never"`. Das Profil erlaubt Lesezugriff auf das lokale Dateisystem sowie Schreibzugriff auf
Workspace-Stammverzeichnisse und das ausgewählte Verzeichnis für den Scanstatus. Scans halten nicht an, um
eine interaktive Genehmigung anzufordern.

Einstellungen, die über die CLI mit `--codex` oder das SDK mit `codexOverrides` übergeben werden, einschließlich
`approval_policy`, `sandbox_mode` und Dateisystemberechtigungen, können diese Scanvorgaben weder ersetzen
noch einschränken. Host- und Netzwerkbeschränkungen gelten weiterhin.

Scan- und Workbench-Prozesse können deine Umgebung erben, einschließlich
API-Token und Cloud-Anmeldedaten ohne Bezug zum Scan. Scanne nur Repositorys, denen du vertraust
und die du überprüfen darfst. Stelle nur die Anmeldedaten bereit, die für den Scan erforderlich sind.

## Authentifizierung und Voraussetzungen

Lege `OPENAI_API_KEY` oder `CODEX_API_KEY` fest, melde dich mit
`npx @openai/codex-security login` an oder verwende eine vorhandene dateibasierte
Codex-Anmeldung. Lege für OpenRouter oder Fireworks den API-Schlüssel des jeweiligen Anbieters fest und wähle ein
Modell aus. Verwende für Amazon Bedrock stattdessen einen Bedrock-API-Schlüssel oder die standardmäßige
AWS-Anmeldedatenkette.

Informationen zur Auswahl der Anmeldedaten findest du unter [Authentifizierung für
Scans auswählen](#select-scan-authentication).

Beschränke den API-Schlüssel in CI auf den Scan-Schritt und verwende einen vertrauenswürdigen Ablauf.

Die CLI erfordert Node.js 22 (22.13.0 oder höher), 24 oder 26. Für Scans, Sammelscans,
Exporte, den Scanverlauf und gespeicherte Befunde ist außerdem Python 3.10 oder höher erforderlich.
Python 3.10 erfordert zusätzlich `tomli`. Verwende `--python` mit `scan`, `bulk-scan` oder
`export`. Alternativ kannst du `PYTHON` für Python-basierte Befehle festlegen.

Weitere Informationen findest du im [CLI-Schnellstart](/de-DE/codex/security/cli), im [Leitfaden zu
Sammelscans](/de-DE/codex/security/cli/bulk-scans), in den [CLI-FAQ](/de-DE/codex/security/cli/faq), im [Leitfaden zu
CI](/de-DE/codex/security/cli/ci) oder im [Leitfaden zum TypeScript SDK](/de-DE/codex/security/sdk).
