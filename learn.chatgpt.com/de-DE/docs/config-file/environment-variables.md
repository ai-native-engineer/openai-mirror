<!-- source: https://learn.chatgpt.com/de-DE/docs/config-file/environment-variables -->

Codex verwendet `config.toml` für dauerhafte Einstellungen. Verwende Umgebungsvariablen für
auf die Shell beschränkte Überschreibungen, Secrets für Automatisierungen, das Verhalten des Installationsprogramms oder Diagnosezwecke.

Diese Seite führt stabile öffentliche Umgebungsvariablen auf, die Codex direkt ausliest.
Nicht aufgeführt sind interne Entwicklungsvariablen, Testvariablen oder
anbieterspezifische Namen für Secrets, die du über
[`env_key`](/de-DE/codex/config-file/config-advanced#custom-model-providers) selbst festlegst.

## Zentrale Speicherorte

| Variable            | Verwendet von                                    | Standardwert      | Beschreibung                                                                                                                                                      |
| ------------------- | ------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_HOME`        | CLI, IDE-Erweiterung, app-server, Installationsprogramme | `~/.codex`   | Legt das Stammverzeichnis für die Zustandsdaten von Codex fest. Dazu gehören Konfiguration, Authentifizierungsdaten, Protokolle, Sitzungen, Skills und Metadaten eigenständiger Pakete. Wenn du die Variable festlegst, muss das Verzeichnis bereits vorhanden sein. |
| `CODEX_SQLITE_HOME` | Zustandsdaten von CLI und app-server                   | `CODEX_HOME` | Legt fest, wo SQLite-basierte Zustandsdaten gespeichert werden. Die Konfigurationsoption `sqlite_home` hat Vorrang. Relative Pfade werden ausgehend vom aktuellen Arbeitsverzeichnis aufgelöst.           |

Weitere Informationen zu den unter `CODEX_HOME` gespeicherten Dateien findest du unter
[Speicherorte für Konfiguration und Zustandsdaten](/de-DE/codex/config-file/config-advanced#config-and-state-locations).

## Installationsvariablen

Diese Variablen gelten für die eigenständigen Installationsskripte, die unter
`https://chatgpt.com/codex/install.sh` und
`https://chatgpt.com/codex/install.ps1` bereitgestellt werden.

| Variable                | Standardwert                                                                              | Beschreibung                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_NON_INTERACTIVE` | `false`                                                                              | Setze die Variable auf `1`, `true` oder `yes`, um die Eingabeaufforderungen des Installationsprogramms zu überspringen. Dabei wird jeweils die Standardantwort verwendet. Nutze diese Einstellung daher für skriptgesteuerte Installationen und Updates, nicht für das Setup beim ersten Start. |
| `CODEX_INSTALL_DIR`     | `~/.local/bin` unter macOS/Linux; `%LOCALAPPDATA%\Programs\OpenAI\Codex\bin` unter Windows | Ändert den Installationsort des aufrufbaren Befehls `codex`. Der Cache für eigenständige Pakete befindet sich weiterhin unter `CODEX_HOME/packages/standalone`.                        |

Lege für unbeaufsichtigte Installationen `CODEX_NON_INTERACTIVE=1` in der Shell fest, in der
das heruntergeladene Installationsprogramm ausgeführt wird:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh

```powershell
$env:CODEX_NON_INTERACTIVE=1; irm https://chatgpt.com/codex/install.ps1 | iex

## Authentifizierung und Netzwerk

| Variable                           | Verwendet von                                          | Beschreibung                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_API_KEY`                    | Exec, review, TypeScript SDK, entfernter exec-server | Stellt einem nicht interaktiven Codex-Prozess einen API-Schlüssel bereit. Wenn du Code ausführst, der vom Repository vorgegeben wird, lege den Schlüssel direkt beim Aufruf und nicht für den gesamten Job fest.             |
| `CODEX_ACCESS_TOKEN`               | CLI, app-server, vertrauenswürdige Automatisierung              | Stellt für vertrauenswürdige Automatisierung ein Zugriffstoken für ChatGPT oder Codex bereit. Leite es für eine dauerhafte Anmeldung per Pipe an `codex login --with-access-token` weiter.             |
| `OPENAI_FEDERATION_RULE_ID`        | Workload-Identität                                | Wählt die für die Workload konfigurierte Föderationsregel aus.                                                                                        |
| `OPENAI_IDENTITY_TOKEN_FILE`       | Workload-Identität                                | Verweist auf den absoluten Pfad der Datei, die das aktuelle OIDC-Token oder SPIFFE JWT-SVID enthält.                                                |
| `OPENAI_WORKLOAD_IDENTITY_CONTEXT` | Workload-Identität                                | Stellt optional begrenzte JSON-Kennungen für die vom Client gemeldete Audit-Zuordnung bereit. Dies hat keine Auswirkungen auf die Authentifizierung oder Autorisierung.         |
| `CODEX_CA_CERTIFICATE`             | HTTPS-, Login- und WebSocket-Clients              | Verweist auf ein PEM-CA-Bundle für Umgebungen mit TLS-Interception im Unternehmensnetzwerk oder privaten Stammzertifikaten. Diese Einstellung hat Vorrang vor `SSL_CERT_FILE`. |
| `SSL_CERT_FILE`                    | HTTPS-, Login- und WebSocket-Clients              | Ersatzpfad für ein PEM-CA-Bundle, wenn `CODEX_CA_CERTIFICATE` nicht gesetzt ist.                                                                               |

Lege für API-Schlüssel von Anbietern
[`env_key`](/de-DE/codex/config-file/config-advanced#custom-model-providers) in der Konfiguration des Modellanbieters
fest. Codex liest die Variable aus, deren Name in dieser Konfiguration angegeben ist. Daher ist
der Variablenname selbst keine fest vorgegebene Codex-Umgebungsvariable.

Informationen zum Umgang mit Secrets für Automatisierungen findest du unter
[API-Schlüssel zur Authentifizierung verwenden](/de-DE/codex/non-interactive-mode#use-api-key-auth).
Informationen zum Einrichten von Zugriffstoken findest du unter [Zugriffstoken](/de-DE/codex/enterprise/access-tokens).
Informationen zum Einrichten von Workload-Identitäten findest du unter
[Föderation von Workload-Identitäten](/de-DE/codex/enterprise/workload-identity).

## Diagnose

| Variable   | Verwendet von            | Beschreibung                                                                                                             |
| ---------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `RUST_LOG` | CLI und app-server | Steuert Filter und Ausführlichkeit der Rust-Protokollierung. Bei `codex exec` ist die Ausgabe standardmäßig auf `error` beschränkt, sofern du keinen ausführlicheren Wert festlegst. |

`RUST_LOG` akzeptiert Werte wie `error`, `warn`, `info`, `debug` und
`trace`. Auch gezieltere Filter für die Rust-Protokollierung sind möglich, etwa
`codex_core=debug,codex_tui=debug`.

Die interaktive CLI speichert Diagnosedaten standardmäßig in lokalen Datenspeichern mit Größenlimit, aber
die Klartextdatei `codex-tui.log` wird nur nach expliziter Aktivierung erstellt. Lege `log_dir` explizit fest, wenn du
für die Fehlerbehebung ein Klartextprotokoll benötigst:

```bash
RUST_LOG=debug codex -c log_dir=./.codex-log
tail -F ./.codex-log/codex-tui.log

Im nicht interaktiven Modus gibt `codex exec` Meldungen direkt aus, anstatt sie
in eine separate TUI-Protokolldatei zu schreiben.
