<!-- source: https://learn.chatgpt.com/de-DE/docs/security/cli/faq -->

Hier findest du Antworten auf häufige Fragen zum Scannen von Repositorys und zum Verwalten
von Sicherheitsbefunden über das Terminal. Beginne für die Installation und deinen ersten Scan
mit dem [CLI-Schnellstart](/de-DE/codex/security/cli).

## Repository-Scans

### Wer kann die CLI verwenden

Das Paket `@openai/codex-security` ist öffentlich verfügbar.

Zum Ausführen von Scans benötigst du Zugriff auf Codex Security. Verwende für optimale Ergebnisse ein Konto,
das für [Trusted Access for Cyber](https://chatgpt.com/cyber) verifiziert wurde.

### Warum verwendet ein Scan nach der Anmeldung einen API-Schlüssel

Wenn in deiner Umgebung `OPENAI_API_KEY` oder `CODEX_API_KEY` gesetzt ist, verwenden Scans
ohne interaktives Terminal sowie JSON- und JSONL-Scans standardmäßig den API-Schlüssel
aus der Umgebung, selbst nach einer erfolgreichen Anmeldung über ChatGPT oder ein Zugriffstoken.
Bei interaktiven Scans mit Textausgabe wirst du zur Auswahl aufgefordert, wenn zusätzlich
eine ChatGPT-Anmeldung verfügbar ist. Testläufe fordern keine Eingabe an und laden keine Anmeldedaten.

Um deine gespeicherten Anmeldedaten für einen Scan zu verwenden, wähle sie ausdrücklich aus:

```bash
npx @openai/codex-security scan . --auth chatgpt

So legst du fest, dass ein API-Schlüssel aus `OPENAI_API_KEY` oder `CODEX_API_KEY` erforderlich ist:

```bash
npx @openai/codex-security scan . --auth api-key

Damit deine gespeicherten Anmeldedaten automatisch verwendet werden, führe
`unset OPENAI_API_KEY CODEX_API_KEY` aus. Informationen zu allen unterstützten Authentifizierungsmethoden
findest du in der [CLI-Referenz](/de-DE/codex/security/cli/reference#select-scan-authentication).

### Wie funktionieren Scans mehrerer Repositorys

Melde dich mit der GitHub CLI an:

```bash
gh auth login

Suche Repositorys in einem GitHub-Konto oder einer GitHub-Organisation und wähle sie aus:

```bash
npx @openai/codex-security bulk-scan

Gib für eine vorbereitete Liste eine CSV-Datei mit Repositorys und ein Ausgabeverzeichnis an:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Unter [Sicherheitsscans für mehrere Repositorys ausführen](/de-DE/codex/security/cli/bulk-scans) findest du Informationen zur Suche nach Repositorys auf GitHub,
zum CSV-Format, zu Kampagnenergebnissen und zu verfügbaren Optionen.

### Kann ein unterbrochener Scan mehrerer Repositorys fortgesetzt werden

Ja. Führe denselben Befehl für den Scan mehrerer Repositorys mit der ursprünglichen CSV-Datei und dem ursprünglichen Ausgabeverzeichnis erneut aus.
Codex Security überspringt Repositorys, deren Scan bereits abgeschlossen ist.

Füge `--max-attempts 3` hinzu, um nach vorübergehenden Repository- oder Scanfehlern einen erneuten Versuch zu starten:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

Ein abgeschlossener Scan mit dem Abdeckungsstatus `partial` oder `unknown` behält seine Ergebnisse,
und die Kampagne endet mit dem Exitcode `2`. Der Scan wird auch mit
`--max-attempts` nicht wiederholt.

### Wie kann ein Scan Architektur und Sicherheitsrichtlinien berücksichtigen

Übergib Architekturdokumente, Bedrohungsmodelle oder Sicherheitsrichtlinien mit
`--knowledge-base`:

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Codex Security verwendet diese Dokumente als Kontext für den aktuellen Scan. Informationen zu
unterstützten Dateitypen und zur Verarbeitung von Verzeichnissen findest du unter [Sicherheitskontext
hinzufügen](/de-DE/codex/security/cli/reference#add-security-context).

## Befunde und Abdeckung

### Wo finden Teams frühere Scanergebnisse

Liste die gespeicherten Scans für dein Repository auf:

```bash
npx @openai/codex-security scans list /path/to/repository

Verwende eine Scan-ID aus den Ergebnissen, um die zugehörigen Befunde zu prüfen:

```bash
npx @openai/codex-security scans show SCAN_ID

Für jeden abgeschlossenen Scan werden Bericht, Befunde, Abdeckung und zugehörige
Artefakte gemeinsam gespeichert. Den vollständigen Aufbau findest du unter [Artefakte von
Scans](/de-DE/codex/security/cli/reference#scan-artifacts).

Führe `scans logs SCAN_ID` aus, um gespeicherte Scan- und Worker-Ereignisse zu prüfen. Diese Protokolle
sind nicht geschwärzt und können Quellcode oder Anmeldedaten enthalten.

### Was passiert, wenn die CLI den Scanverlauf nicht speichern kann

Codex Security speichert den Scanverlauf in einer Workbench-Datenbank. Wenn das standardmäßige
Statusverzeichnis nicht beschreibbar ist, wähle ein privates Verzeichnis außerhalb des
Repositorys:

```bash

### Wie unterscheiden Scans zwischen neuen und bekannten Befunden

Liste die offenen Befunde aus allen Scans eines Repositorys auf:

```bash
npx @openai/codex-security findings list /path/to/repository

Die Liste zeigt Befunde, die im letzten Scan bestätigt wurden, sowie frühere offene
Befunde, die der Scan nicht bestätigt hat.

Vergleiche die Befunde der beiden Scans:

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

Der Vergleich gleicht Befunde automatisch anhand ihrer zugrunde liegenden Ursache ab, nutzt gespeicherte
Zuordnungen erneut und erkennt neue, fortbestehende, wiedereröffnete, behobene sowie unbekannte
Befunde. Ein Befund gilt nur dann als behoben, wenn der spätere Scan sein
ursprüngliches Ziel und den betroffenen Pfad lückenlos abdeckt.

### Wie funktionieren Rückmeldungen zu Fehlalarmen

Prüfe den gespeicherten Scan, um die ID des Vorkommens zu finden:

```bash
npx @openai/codex-security scans show SCAN_ID

Dokumentiere, warum dieser Befund nicht zutrifft:

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

Künftige Scans desselben Repositorys erhalten diese Erklärung als Kontext. Dennoch
prüfen sie den aktuellen Quellcode, die Schutzmaßnahmen und die Erreichbarkeit unabhängig. Das
Verwerfen eines Befunds unterdrückt weder eine Regel noch einen Pfad oder eine Schwachstellenklasse.

Details zu den Befehlen findest du in der [Referenz zu
Befunden](/de-DE/codex/security/cli/reference#codex-security-findings).

### Warum können wiederholte Scans unterschiedliche Befunde liefern

KI-gestützte Scans können selbst bei derselben Scan-Konfiguration unterschiedlich ausfallen. Führe zunächst
deinen Ausgangsscan erneut aus:

```bash
npx @openai/codex-security scans rerun BASELINE_SCAN_ID

Beim erneuten Ausführen bleibt die ursprüngliche Scan-Konfiguration erhalten,
und dieselbe Plug-in-Version ist erforderlich. Hat sich das installierte Plug-in geändert, wird der Befehl abgebrochen.

Vergleiche den Ausgangsscan mit dem neuen Scan:

```bash
npx @openai/codex-security scans compare BASELINE_SCAN_ID REPEAT_SCAN_ID

Stelle einheitliche Architektur- und Sicherheitsvorgaben bereit, wenn fehlender Kontext
zu den Abweichungen beitragen könnte. Ein Abgleich kann denselben zugrunde liegenden Befund
über mehrere Scanläufe hinweg erkennen, macht die Scans aber nicht deterministisch. Prüfe jeden
wichtigen Befund, der nicht mehr angezeigt wird, direkt erneut.

### Wie kann ein Team prüfen, ob eine Korrektur wirksam war

Führe nach der Korrektur den ursprünglichen Scan erneut aus:

```bash
npx @openai/codex-security scans rerun BEFORE_SCAN_ID

Vergleiche die ursprünglichen Befunde mit dem neuen Scan:

```bash
npx @openai/codex-security scans compare BEFORE_SCAN_ID AFTER_SCAN_ID

Stelle sicher, dass der neue Scan das ursprüngliche Ziel und den betroffenen Pfad
lückenlos abdeckt. Prüfe den ursprünglichen Befund anschließend direkt anhand des aktuellen
Checkouts:

```bash
npx @openai/codex-security validate /path/to/original/findings.json \
  "Recheck the SQL injection in src/orders.ts:42 against the current code"

Ein fehlender Befund oder ein Scanvergleich allein belegt nicht, dass eine Korrektur wirksam war.

### Was bedeutet eine unvollständige Abdeckung

Der Abdeckungsstatus kann `complete`, `partial` oder `unknown` lauten. Prüfe `coverage.json`
auf ausgeschlossene Pfade, zurückgestellte Bereiche und offene Fragen, bevor du einen
Scan als Nachweis einer Überprüfung wertest.

Scans mit teilweiser oder unbekannter Abdeckung geben den Exitcode `2` zurück, auch ohne
Richtlinie für Schweregrade. Verfügbare Befunde und Abdeckungsinformationen bleiben erhalten. Ein späterer
Scan kann nicht belegen, dass ein früherer Befund nicht mehr besteht, wenn er
dessen ursprünglichen Pfad nicht abdeckt.

## Automatisierung und Kosten

### Wie funktionieren Zeitlimits für Tiefenscans

Lege beim Start eines Tiefenscans eine Frist für die Worker fest:

```bash
npx @openai/codex-security scan . --mode deep --max-time-hours 1.5

Der Standardwert beträgt `96` Stunden. Du kannst jeden positiven Wert bis einschließlich `96` festlegen,
auch Bruchteile. Nach Ablauf der Frist stoppt Codex Security noch nicht abgeschlossene Worker,
behält die Ergebnisse abgeschlossener Standardscans bei und fasst sie im Abschlussbericht zusammen.
Falls kein Worker die Überprüfung des Quellcodes abschließt, weist der Bericht eine teilweise Abdeckung aus
und die CLI gibt den Exitcode `2` zurück.

Lege für dauerhafte Einstellungen oder Kampagnen mit mehreren Repositorys `max_time_hours` unter
`[deep_scan]` in der [Konfiguration für
Tiefenscans](/de-DE/codex/security/cli/reference#configure-deep-scans) fest.

### Wie funktionieren Kostenlimits für Scans

Lege vor Beginn des Scans ein geschätztes Kostenlimit in USD fest:

```bash
npx @openai/codex-security scan . --max-cost 5

Das Limit ist eine Schätzung und keine feste Ausgabenobergrenze. Bereits laufende
Anfragen können abgeschlossen werden und dabei das Limit überschreiten. Erreicht ein Tiefenscan das Limit,
nachdem Codex Security die Ergebnisse abgeschlossener Worker zusammengeführt hat, speichert die CLI den fertiggestellten
Bericht mit teilweiser Abdeckung und beendet sich mit dem Exitcode `2`. Andernfalls bleiben
vorhandene Teilergebnisse erhalten.

### Können Scans Commits und Pull Requests prüfen

Installiere eine Pre-Commit-Sicherheitsprüfung für zum Commit vorgemerkte und nicht vorgemerkte Änderungen:

```bash
npx @openai/codex-security install-hook

Für die Prüfung von Pull Requests scanne die committeten Änderungen und lege einen
Schwellenwert für den Schweregrad fest:

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --fail-on-severity high

Ein vollständiger Scan gibt den Exit-Code `1` zurück, wenn er ein Problem findet, dessen Schweregrad
mindestens dem ausgewählten Wert entspricht. Unter [Scans in CI durchführen](/de-DE/codex/security/cli/ci) findest du den
vollständigen Ablauf für GitHub Actions sowie Informationen zur Verarbeitung von Artefakten und zum SARIF-Export.

### Kann eine andere Anwendung Scans direkt ausführen

Ja. Verwende das [TypeScript SDK](/de-DE/codex/security/sdk), um direkt aus einer Anwendung oder einem
Entwicklungstool Scans zu starten, Ziele auszuwählen, Befunde und Abdeckung
zu prüfen, den Fortschritt zu verfolgen und Kostenkontrollen anzuwenden.
