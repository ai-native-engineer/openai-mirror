<!-- source: https://learn.chatgpt.com/de-DE/docs/security/cli -->

Codex Security hilft Sicherheits- und Entwicklungsteams dabei, Schwachstellen zu finden,
zu bestätigen und zu beheben. Nutze die Kommandozeilenschnittstelle (CLI), um
Repositories zu scannen, die dir gehören oder die du überprüfen darfst, Befunde im Zeitverlauf
zu überprüfen und Änderungen vor ihrer Übernahme zu prüfen.

  Das Paket `@openai/codex-security` ist öffentlich verfügbar. Für Scans benötigst du Zugriff auf
  Codex Security. Einen interaktiven Scan in Codex startest du mit dem [Schnellstart für das
  Codex Security-Plug-in](/de-DE/codex/security/plugin). Informationen zu verbundenen Repositories auf GitHub findest du
  unter [Setup für Codex Security Cloud](/de-DE/codex/security/setup).

## Voraussetzungen prüfen

Für die CLI ist Node.js 22 (22.13.0 oder höher), 24 oder 26 erforderlich. Scans, Sammelscans,
Exporte, der Scanverlauf und gespeicherte Befunde setzen außerdem Python 3.10 oder höher voraus.
Weitere Informationen findest du unter [Authentifizierung und
Voraussetzungen](/de-DE/codex/security/cli/reference#authentication-and-prerequisites).

## CLI einrichten und überprüfen

Führe die CLI mit `npx` aus und prüfe ihre Version:

```bash
npx @openai/codex-security --version

Führe folgenden Befehl aus, um sowohl die Paketversion als auch die Version des mitgelieferten Plug-ins anzuzeigen:

```bash
npx @openai/codex-security info --json

Unter [CLI- und SDK-Versionen](https://github.com/openai/codex-security/releases)
findest du Informationen zu Änderungen am Paket.

Liste die verfügbaren Befehle auf:

```bash
npx @openai/codex-security --help

Siehe auch die [CLI-Referenz](/de-DE/codex/security/cli/reference).

## Anmelden

Melde dich für die lokale Nutzung mit deinem ChatGPT-Konto an:

```bash
npx @openai/codex-security login

Verwende auf einem Remote- oder Headless-System die Geräteauthentifizierung:

```bash
npx @openai/codex-security login --device-auth

Lege für CI und andere automatisierte Arbeitsabläufe einen OpenAI-API-Schlüssel fest:

```bash

Informationen zu AWS-Anmeldedaten findest du unter [Setup für
Amazon Bedrock](/de-DE/codex/security/cli/reference#use-amazon-bedrock). Lege für [OpenRouter oder
Fireworks](/de-DE/codex/security/cli/reference#use-openrouter-or-fireworks) den API-Schlüssel des Anbieters fest und
wähle mit `--provider` und `--model` ein Modell aus.

Wenn auch ein API-Schlüssel festgelegt ist, wähle ausdrücklich die Anmeldung mit deinem ChatGPT-Konto aus:

```bash
npx @openai/codex-security scan . --auth chatgpt

Um zwingend den in der Umgebung hinterlegten API-Schlüssel zu verwenden, wähle die API-Schlüssel-Authentifizierung aus:

```bash
npx @openai/codex-security scan . --auth api-key

Je nach Konto und Repository benötigen Scans des gesamten Repositorys möglicherweise zusätzlich
[Trusted Access for Cyber](https://chatgpt.com/cyber).

## Scan vorbereiten

Wähle ein Repository, dem du vertraust und das du überprüfen darfst. Scans verwenden deine
lokalen Betriebssystemberechtigungen und warten nicht auf eine Genehmigung. Scanprozesse
können deine Umgebung erben. Entferne daher vor dem Start
alle dafür nicht benötigten Anmeldedaten. Weitere Informationen findest du unter [Berechtigungen für lokale
Scans](/de-DE/codex/security/cli/reference#local-scan-permissions).

Wähle für die Scanergebnisse ein Verzeichnis außerhalb des Repositorys aus:

```bash
REPOSITORY=/path/to/repository
SCAN_DIR=/path/outside/repository/codex-security-results

Wenn du `--output-dir` weglässt, speichert Codex Security die Ergebnisse in einem eigenen persistenten
Zustandsverzeichnis. Die Ergebnisse können Quelltextauszüge und Details zu Schwachstellen enthalten.
Wähle daher einen privaten Speicherort und eine geeignete Aufbewahrungsrichtlinie.

Wenn das standardmäßige Zustandsverzeichnis nicht beschreibbar ist, wähle ein beschreibbares Verzeichnis
außerhalb des gescannten Repositorys aus:

```bash

Prüfe vor dem Start eines Scans das Repository, das Ziel und das Ausgabeverzeichnis:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --dry-run

Der Testlauf prüft lokale Eingaben, einschließlich aller über `--knowledge-base` angegebenen Pfade,
ohne Codex zu starten, Anmeldedaten zu laden oder den Python-Interpreter
des Plug-ins zu überprüfen.

## Ersten Scan ausführen

Führe einen Standardscan aus und speichere seine Ergebnisse im ausgewählten Verzeichnis:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR"

Interaktive Terminals zeigen ein Live-Dashboard für den Scan. Füge `--headless` hinzu, um stattdessen
einfache Fortschrittszeilen anzuzeigen. In CI und auf Terminals ohne interaktive Sitzung
erscheinen automatisch einfache Fortschrittszeilen.

Das Dashboard zeigt außerdem Sitzungsdetails in Echtzeit an. Diese können Quellcode
oder Anmeldedaten enthalten. Prüfe sie daher, bevor du sie weitergibst.

Standardmäßig gibt die CLI den Scanfortschritt und die Abschlusszusammenfassung über stderr aus.
Das vollständige Scanergebnis wird nicht über stdout ausgegeben. Nach einem abgeschlossenen Scan
erscheint eine Zusammenfassung wie diese:

```text
  REPORT    /path/outside/repository/codex-security-results/report.md

  FINDINGS  2 (2 confirmed this scan; 0 previously found; 1 high, 1 medium)
  COVERAGE  complete
  ELAPSED   42s
  RESULTS   /path/outside/repository/codex-security-results

Tokenverbrauch und geschätzte Kosten werden angezeigt, sofern verfügbar. Um das vollständige
Ergebnis als maschinenlesbares JSON auszugeben, fordere ausdrücklich eine strukturierte Ausgabe an:

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --json

Scans dienen standardmäßig nur der Berichterstellung, sodass Befunde für die lokale
Überprüfung verfügbar bleiben. Sobald du bereit bist, [Scans in
CI auszuführen](/de-DE/codex/security/cli/ci), kannst du einen Schwellenwert für den Schweregrad festlegen.

## Modell und Reasoning-Aufwand auswählen

Scans verwenden standardmäßig `gpt-5.6-sol` mit dem Reasoning-Aufwand `xhigh`. Wähle ein
anderes Modell und einen anderen Reasoning-Aufwand aus, wenn die Aufgabe dies erfordert:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --model gpt-5.6-terra \
  --effort high

Für den Reasoning-Aufwand werden die Stufen `minimal`, `low`, `medium`, `high`, `xhigh` und
`max` unterstützt.

## Ergebnisse prüfen

Öffne `report.md`, um das Ergebnis in lesbarer Form anzuzeigen. Das Scanverzeichnis enthält außerdem die
strukturierten Dateien, die für die Automatisierung verwendet werden:

```text
codex-security-results/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

- `scan-manifest.json` dokumentiert Ziel, Umfang, erzeugende Komponente und versiegelte
  Artefakte.
- `findings.json` dokumentiert für jeden Befund Schweregrad, Konfidenz, Fundstellen, Nachweise und
  Maßnahmen zur Behebung.
- `coverage.json` dokumentiert geprüfte Bereiche, Ausschlüsse, zurückgestellte Aufgaben, offene
  Fragen und die Vollständigkeit der Abdeckung.

Die Abdeckung kann den Status `complete`, `partial` oder `unknown` haben. Prüfe alle zurückgestellten Bereiche und
offenen Fragen, bevor du den Scan als Nachweis einer Überprüfung heranziehst.
Die [CLI-Referenz](/de-DE/codex/security/cli/reference#scan-artifacts) beschreibt
die vollständige Spezifikation für Artefakte und Ausgaben.

## Befunde prüfen und beheben

Nach einem vollständigen interaktiven Scan mit Befunden bietet die CLI einen
Browser für Befunde an. Prüfe die Nachweise und entscheide, welche Befunde du beheben
möchtest. Die gespeicherten Aufgaben findest du in der Codex-Desktop-App.

So behebst du Befunde mit hohem oder kritischem Schweregrad ohne den Browser:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --patch --patch-severity high --json

Füge `--create-pr` hinzu, um verifizierte Patches zu committen und einen Pull Request auf GitHub zu öffnen.

Du kannst auch gespeicherte Befunde beheben oder Linear-Issues importieren. Weitere Informationen findest du in der
[Referenz zu `validate` und `patch`](/de-DE/codex/security/cli/reference#codex-security-validate-and-codex-security-patch).

## Nächsten Scan auswählen

Verwende einen Pfadscan, wenn ein Repository separate Dienste oder Pakete enthält:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --path services/billing \
  --path packages/auth

Prüfe die zwischen der Basisrevision und `HEAD` committeten Änderungen:

```bash
npx @openai/codex-security scan "$REPOSITORY" --diff origin/main --head HEAD

Prüfe bereitgestellte und nicht bereitgestellte Änderungen gegenüber `HEAD`:

```bash
npx @openai/codex-security scan "$REPOSITORY" --working-tree --base HEAD

Bei Diff- und Worktree-Scans muss das Repository-Argument auf das Stammverzeichnis
des Git-Worktrees verweisen. Rufe die ausgewählten Revisionen ab, bevor du einen Diff-Scan startest.

Verwende den Modus für gründliche Scans, wenn ein Repository oder Pfad umfassender geprüft werden muss:

```bash
npx @openai/codex-security scan "$REPOSITORY" --mode deep

So steuerst du Worker, Subagenten und den Zeitpunkt, zu dem der Scan beendet wird:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

Diese Optionen erfordern den Modus für gründliche Scans. Er unterstützt Repository- und Pfadziele,
aber keine Diff- oder Worktree-Scans. Hier steuert `--workers` unabhängige
Worker für Standardscans innerhalb eines einzelnen Scans; `bulk-scan --workers` steuert parallele
Repository-Scans. `--max-time-hours` akzeptiert eine positive Zahl bis zu `96`,
einschließlich Stundenbruchteilen. Sobald das Limit erreicht ist, beendet der Scan noch laufende Worker,
bewahrt die Ergebnisse abgeschlossener Scans und fasst sie im Abschlussbericht zusammen.

## Architektur- und Sicherheitskontext hinzufügen

Stelle Architekturdokumente, Bedrohungsmodelle oder Sicherheitsrichtlinien als Kontext für den Scan
bereit. So kann Codex Security Befunde anhand der tatsächlichen Funktionsweise deines Systems
bewerten:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

## Benutzerdefinierte Scan-Anweisungen hinzufügen

Füge Anweisungen hinzu, die den Scan auf deine Sicherheitsprioritäten ausrichten. Verwende eine
zweite Datei für Folgeanweisungen:

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --scan-prompt-file /path/to/scan.md \
  --post-scan-prompt-file /path/to/follow-up.md

Die Folgeanweisungen werden nach erfolgreichen Scans sowie nach Scans mit unvollständiger Abdeckung
oder Fehlern in derselben authentifizierten Sitzung ausgeführt. Schlägt ihre Ausführung fehl,
gibt die CLI eine Warnung aus und behält den abgeschlossenen Scan bei. Nach einem
Abbruch oder einem Scan, der sein Kostenlimit erreicht, werden sie nicht ausgeführt.
Beide Optionen funktionieren auch mit `bulk-scan`; eine CSV-Spalte namens `prompt` ergänzt Repository-spezifische Anweisungen.

## Scanbudget festlegen

Mit `--max-cost` beendest du einen Scan, sobald die geschätzten Modellkosten einen Grenzwert
in USD überschreiten:

```bash
npx @openai/codex-security scan "$REPOSITORY" --max-cost 5

Bereits laufende Anfragen können das Limit bei ihrem Abschluss geringfügig überschreiten. Wenn ein gründlicher Scan
das Limit erreicht, nachdem Codex Security die Ergebnisse abgeschlossener Worker
zusammengeführt hat, speichert die CLI den fertigen Bericht, kennzeichnet dessen Abdeckung als `partial`
und gibt den Exit-Code `2` zurück. Wenn der Scan keinen fertigen Bericht erstellen kann,
bleiben alle verfügbaren Teilergebnisse auf dem Datenträger erhalten.

## Änderungen vor jedem Commit scannen

Installiere für dein Repository eine Git-Sicherheitsprüfung, die vor jedem Commit ausgeführt wird:

```bash
npx @openai/codex-security install-hook

Die Prüfung scannt vor jedem Commit gestagte und nicht gestagte Änderungen. Sie blockiert
Commits bei Befunden mit hohem Schweregrad und bei Scanfehlern, ohne ein vorhandenes
Pre-Commit-Skript zu ersetzen.

## Massenscans für Repositorys durchführen

Melde dich bei GitHub an, bevor du nach Repositorys suchst:

```bash
gh auth login

Suche nach Repositorys in deinem GitHub-Konto oder deiner Organisation und wähle sie aus:

```bash
npx @openai/codex-security bulk-scan

Der interaktive Ablauf schließt archivierte Repositorys und Forks aus. Vor dem Scannen wirst du aufgefordert,
die ausgewählten Repositorys zu bestätigen.

Um eine vorbereitete Liste von Repositorys zu scannen, gib eine CSV-Datei und ein Ausgabeverzeichnis an:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Führe denselben Befehl erneut aus, um einen bestehenden Massenscan fortzusetzen. Codex Security
überspringt bereits abgeschlossene Repositorys. Füge `--max-attempts 3` hinzu, um es bei vorübergehenden
Repository- oder Scanfehlern erneut zu versuchen.

Informationen zur Ermittlung von Repositorys auf GitHub, zur Vorbereitung von CSV-Dateien, zu Kampagnenergebnissen und zum Docker-Setup findest du unter
[Sicherheits-Massenscans durchführen](/de-DE/codex/security/cli/bulk-scans).

## Massenscans in Docker durchführen

Wenn dein Zugang das Docker-Image von Codex Security umfasst, verwende die bereitgestellte
gehärtete Compose-Konfiguration und das Sicherheitsprofil auf einem Linux-Docker-Host.
Der Host muss das Anlegen nicht privilegierter Benutzer-Namespaces unterstützen. Gib die Repositorys
in einer CSV-Datei an, speichere Ergebnisse und Anmeldestatus in dauerhaft eingebundenen Verzeichnissen und
stelle Anmeldedaten über deine Umgebung oder einen Secret Manager bereit:

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

Der Container führt Massenscans ohne interaktive Eingabeaufforderungen durch. Verwende die CLI außerhalb
von Docker, wenn du Repositorys interaktiv ermitteln möchtest. Stelle für private
Repositorys `GH_TOKEN` oder `GITHUB_TOKEN` über deine Umgebung oder
einen Secret Manager bereit. Die [Anmeldeanforderungen](#sign-in), einschließlich des Zugriffs auf das Konto und das
Repository, gelten auch für Scans in Containern.

## Gespeicherten Scan erneut aufrufen

Liste die gespeicherten Scans für dein Repository auf:

```bash
npx @openai/codex-security scans list "$REPOSITORY"

Kopiere eine Scan-ID aus den Ergebnissen, um die Befunde und die Konfiguration des Scans zu prüfen:

```bash
npx @openai/codex-security scans show SCAN_ID

So siehst du dir die gespeicherten Ereignisse eines Scans und seiner Worker an:

```bash
npx @openai/codex-security scans logs SCAN_ID

Gespeicherte Protokolle sind nicht geschwärzt und können Quellcode oder Anmeldedaten enthalten.
Prüfe sie, bevor du sie weitergibst.

Liste offene Befunde aus allen Scans des Repositorys auf:

```bash
npx @openai/codex-security findings list "$REPOSITORY"

Ein früherer Befund bleibt offen, wenn der neueste Scan ihn nicht bestätigt.

Um einen geprüften Befund als falsch positiv zu markieren, erkläre, warum er nicht
zutrifft:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The route already checks permissions"

Spätere Scans berücksichtigen diese Begründung, prüfen den aktuellen Code aber trotzdem erneut.

Führe denselben Scan mit seiner ursprünglichen Konfiguration für den aktuellen Checkout aus:

```bash
npx @openai/codex-security scans rerun SCAN_ID

Vergleiche zwei Scans, um neue, fortbestehende, erneut geöffnete, behobene oder unbekannte
Befunde zu ermitteln:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

Der Vergleich ordnet Befunde anhand ihrer zugrunde liegenden Ursache automatisch einander zu und
nutzt gespeicherte Zuordnungen erneut.

Informationen zum CSV-Format für Massenscans, zu Filtern für den Scanverlauf und zu Befehlsoptionen findest du
in der [CLI-Referenz](/de-DE/codex/security/cli/reference).

Fahre mit dem Ablauf fort, der zu deinem Ziel passt:

- [Sicherheits-Massenscans durchführen](/de-DE/codex/security/cli/bulk-scans), um Repositorys auf GitHub
  zu ermitteln oder eine angepinnte CSV-Bestandsliste zu scannen.
- [CLI-FAQ lesen](/de-DE/codex/security/cli/faq), um Antworten zum Scanverlauf,
  zu Rückmeldungen bei falsch positiven Befunden, zur Abdeckung und zur Überprüfung von Fehlerbehebungen zu finden.
- [Scans in CI durchführen](/de-DE/codex/security/cli/ci), um Pull Requests zu prüfen, Ergebnisse
  zu speichern und eine Richtlinie für Schweregrade festzulegen.
- [CLI-Referenz verwenden](/de-DE/codex/security/cli/reference), um jedes Flag,
  jedes Ausgabeformat, jedes Artefakt und jeden Exitcode zu überprüfen.
- [TypeScript SDK integrieren](/de-DE/codex/security/sdk), um Scans aus einer
  Anwendung oder einem Entwicklungstool auszuführen.
