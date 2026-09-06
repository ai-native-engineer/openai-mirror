<!-- source: https://learn.chatgpt.com/de-DE/docs/security/cli/bulk-scans -->

Verwende `npx @openai/codex-security bulk-scan`, um Repositories in einer
Kampagne zu überprüfen. Suche in deinem persönlichen GitHub-Konto oder einer
Organisation nach Repositories oder stelle eine CSV bereit, die für jedes Repository eine exakte
Git-Revision festlegt.

  Das Paket `@openai/codex-security` ist öffentlich verfügbar. Für die Scans benötigst du
  Zugriff auf Codex Security. Folge dem [CLI-Schnellstart](/de-DE/codex/security/cli), um die CLI zu installieren
  und dich anzumelden.

## Repository-Quelle auswählen

| Quelle           | Geeignet für                                                                          |
| ---------------- | --------------------------------------------------------------------------------------- |
| GitHub-Suche | Wähle interaktiv Repositories aus deinem persönlichen GitHub-Konto oder einer Organisation aus. |
| CSV-Bestandsliste    | Führe eine wiederholbare, automatisierte Kampagne für exakt festgelegte Repository-Revisionen aus.                |

Beide Arbeitsabläufe speichern den Fortschritt sowie die Ergebnisse der einzelnen Repositories, sodass du
eine Kampagne nach einer Unterbrechung fortsetzen kannst.

## GitHub-Repositories suchen

Melde dich mit der GitHub CLI an:

```bash
gh auth login

Starte einen interaktiven Scan mehrerer Repositories:

```bash
npx @openai/codex-security bulk-scan

Die CLI führt dich durch folgende Schritte:

1. Wähle dein persönliches GitHub-Konto oder eine Organisation aus.
2. Überprüfe Repositories, die in den letzten 90 Tagen aktiv waren.
3. Durchsuche die Repository-Liste und wähle die Repositories aus, die du scannen möchtest.
4. Wähle ein Verzeichnis für die Scanergebnisse aus.
5. Überprüfe die ausgewählten Repositories und bestätige die Kampagne.

Die Suche schließt archivierte Repositories und Forks aus. Für jedes ausgewählte
Repository speichert die CLI den exakten Commit des Standard-Branches in
`<output-directory>/repositories.csv`. Scans starten erst, nachdem du die
Auswahl bestätigt hast.

Um GitHub Enterprise Server zu verwenden, melde dich zunächst bei deinem GitHub-Host an:

```bash
gh auth login --hostname github.example.com

Lege `GH_HOST` beim Start der Repository-Suche fest:

```bash
GH_HOST=github.example.com npx @openai/codex-security bulk-scan

Für die interaktive Suche benötigst du ein Terminal. Verwende bei CI, Containern oder einer vorbereiteten
Repository-Liste stattdessen eine CSV-Bestandsliste.

## Repository-CSV erstellen

Erstelle eine CSV mit einer Zeile für jedes Repository und die jeweils festgelegte Revision:

```csv
id,repository,revision,scope,mode,prompt
payments,https://github.com/example/payments.git,0123456789abcdef0123456789abcdef01234567,services/api,standard,Review payment authorization and refunds.
identity,https://github.com/example/identity.git,fedcba9876543210fedcba9876543210fedcba98,,deep,Review session and identity boundaries.

Die CSV unterstützt folgende Spalten:

| Spalte       | Erforderlich | Beschreibung                                                                                                |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------------- |
| `id`         | Ja      | Eindeutige Repository-Kennung. Verwende Buchstaben, Ziffern, Punkte, Bindestriche oder Unterstriche.                      |
| `repository` | Ja      | HTTPS-URL, SSH-URL oder lokaler Repository-Pfad. Relative Pfade werden ausgehend vom CSV-Verzeichnis aufgelöst.               |
| `revision`   | Ja      | Vollständiger SHA-Wert eines Git-Commits mit 40 oder 64 Zeichen. Branch-Namen, Tags und gekürzte Commit-Hashes werden nicht unterstützt. |
| `scope`      | Nein       | Zu scannendes Verzeichnis, angegeben relativ zum Repository. Lass den Wert weg, um das gesamte Repository zu scannen.                       |
| `mode`       | Nein       | `standard` oder `deep`. Lass den Wert weg, um den beim Aufruf des Befehls ausgewählten Modus zu verwenden.                                   |
| `prompt`     | Nein       | Scan-Anweisungen für dieses Repository.                                                             |

Führe folgenden Befehl aus, um den vollständigen Commit-SHA eines lokalen Repositorys zu ermitteln:

```bash
git -C /path/to/repository rev-parse HEAD

## Kampagne anhand einer CSV ausführen

Übergib die CSV und ein privates Ausgabeverzeichnis außerhalb der Repositories:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

`--workers` steuert die Anzahl gleichzeitiger Repository-Scans. Der Standardwert ist `4`. Die Option legt
nicht die Anzahl unabhängiger Worker für Standard-Scans innerhalb jedes Deep-Scans fest.
Diese Grenzwerte konfigurierst du über
[`[deep_scan]`](/de-DE/codex/security/cli/reference#configure-deep-scans). Verwende `--mode
deep`, um für Zeilen ohne eigenen `mode` einen Deep-Scan auszuwählen. Jede CSV-Zeile
kann weiterhin ihren eigenen Scanmodus und den Scanbereich im Repository festlegen.

Lege `[deep_scan].max_time_hours` fest, um die Ausführung der Worker bei jedem Deep-Scan in der
Kampagne zu begrenzen. Das Flag `--max-time-hours` lässt sich mit `scan`, aber nicht mit `bulk-scan` verwenden.

Die CLI checkt jede festgelegte Revision aus, scannt das ausgewählte Ziel, speichert das
Ergebnis und entfernt den temporären Repository-Checkout. Ein Repository gilt nur dann als
abgeschlossen, wenn sein Scan den vorgesehenen Bereich vollständig abdeckt und alle erforderlichen
Ergebnisartefakte vorhanden sind.

## Sicherheitskontext und Anweisungen für alle Scans bereitstellen

Füge jedem Scan Architekturdokumente, Bedrohungsmodelle oder Sicherheitsrichtlinien
mit `--knowledge-base` hinzu. Gib das Flag für weitere Dateien oder Verzeichnisse erneut an:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Stelle Prompt-Dateien bereit, um gemeinsame Scan-Anweisungen hinzuzufügen oder nach jedem Scan
Folgeanweisungen auszuführen:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --scan-prompt-file scan-instructions.md \
  --post-scan-prompt-file follow-up.md

Die CLI hängt das CSV-Feld `prompt` jedes Repositorys an die gemeinsamen
Scan-Anweisungen an. Folgeanweisungen werden in derselben authentifizierten Sitzung
nach erfolgreichen Scans sowie nach Scans mit unvollständiger Abdeckung oder Fehlern ausgeführt,
jedoch nicht nach einem Abbruch oder einem Scan, der sein Kostenlimit erreicht. Pfade zu Prompt-Dateien werden
ausgehend von deinem aktuellen Verzeichnis aufgelöst.

## Modell und Reasoning-Aufwand auswählen

Scans mehrerer Repositories verwenden standardmäßig `gpt-5.6-sol` mit dem Reasoning-Aufwand `xhigh`. So
wählst du für eine CSV-Kampagne ein anderes Modell und einen anderen Reasoning-Aufwand aus:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --model gpt-5.6-terra \
  --effort high

Dieselben Optionen kannst du auch bei der interaktiven Repository-Suche verwenden:

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

Für den Reasoning-Aufwand werden die Stufen `minimal`, `low`, `medium`, `high` und `xhigh` unterstützt.

Für OpenRouter oder Fireworks legst du entsprechend `OPENROUTER_API_KEY` oder `FIREWORKS_API_KEY` fest
und gibst `--provider` sowie `--model` an. Informationen zu Zugangsdaten und
Beispiele findest du unter [Setup für OpenRouter oder
Fireworks](/de-DE/codex/security/cli/reference#use-openrouter-or-fireworks) oder [Setup für
Amazon Bedrock](/de-DE/codex/security/cli/reference#use-amazon-bedrock).

## Kampagnenergebnisse überprüfen

Das Ausgabeverzeichnis enthält die Kampagne mit festgelegten Revisionen, ein Ergebnisprotokoll, das nur ergänzt wird,
und separate Artefakte für jedes Repository und jeden Versuch:

```text
security-scans/
├── manifest.json
├── results.jsonl
├── checkouts/
└── artifacts/
    ├── payments/
    │   └── attempt-1/
    │       ├── scan-manifest.json
    │       ├── findings.json
    │       ├── coverage.json
    │       └── report.md
    └── identity/
        └── attempt-1/
            ├── scan-manifest.json
            ├── findings.json
            ├── coverage.json
            └── report.md

- `manifest.json` dokumentiert die Repositories, festgelegten Revisionen, Scanbereiche und
  Scanmodi sowie die gemeinsamen oder Repository-spezifischen Anweisungen der Kampagne.
- `results.jsonl` dokumentiert jeden Scanversuch für ein Repository, dessen Status und das Artefaktverzeichnis
  sowie alle verfügbaren Angaben zu Kosten oder Fehlern.
- `report.md` stellt einen lesbaren Bericht zu einem Scanversuch für ein Repository bereit.
- `findings.json` und `coverage.json` dokumentieren die Befunde des Versuchs und den
  überprüften Scanbereich.

Exportiere einen abgeschlossenen Repository-Scan, wenn du ein übertragbares Ergebnis benötigst:

```bash
npx @openai/codex-security export \
  /path/outside/repositories/security-scans/artifacts/payments/attempt-1 \
  --export-format sarif \
  --output /path/outside/repositories/payments.sarif

Ergebnisse können Auszüge aus dem Quellcode und Details zu Schwachstellen enthalten. Behandle das
Ausgabeverzeichnis vertraulich, speichere es außerhalb der gescannten Repositories und wende eine
angemessene Aufbewahrungsrichtlinie darauf an.

## Kampagne fortsetzen

Führe den ursprünglichen Befehl mit derselben CSV und demselben Ausgabeverzeichnis aus:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Die CLI setzt nicht abgeschlossene Repository-Scans fort und überspringt bereits abgeschlossene Scans.
Scans mit unvollständiger Abdeckung werden nicht erneut ausgeführt. Ihre Ergebnisse bleiben verfügbar,
und der Befehl endet mit dem Exit-Code `2`.

Ändere bei einem vorhandenen Ausgabeverzeichnis weder das Repository-Inventar noch die Scan- und Folgeanweisungen.
Die CLI überprüft das fixierte Manifest und lehnt eine abweichende Kampagne ab. Verwende ein neues
Ausgabeverzeichnis, wenn du Repositories, Revisionen, Scanbereiche, Scanmodi oder gemeinsame
beziehungsweise Repository-spezifische Anweisungen änderst.

## Repositories nach Fehlern erneut verarbeiten

Verwende `--max-attempts`, um ein Repository nach einem vorübergehenden Checkout- oder
Scanfehler erneut zu verarbeiten:

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

Standardmäßig ist ein Versuch pro Repository vorgesehen. Jeder Versuch erhält einen eigenen
Beleg und ein eigenes Artefaktverzeichnis. Erneute Versuche sind bei Checkout-Fehlern, fehlgeschlagenen Scans
und fehlenden erforderlichen Artefakten möglich. Abgeschlossene Scans mit unvollständiger Abdeckung
werden nicht erneut ausgeführt.

Massenscans verwenden folgende Exit-Codes:

| Exit-Code | Bedeutung                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| `0`       | Alle Repositories wurden erfolgreich verarbeitet.                                                                              |
| `2`       | Ein Repository konnte nicht vollständig verarbeitet werden, ein Scan hatte eine unvollständige Abdeckung oder beim Befehl trat ein Eingabe- oder Laufzeitfehler auf. |
| `130`     | Ctrl-C hat die Kampagne unterbrochen.                                                                                      |
| `143`     | SIGTERM hat die Kampagne beendet.                                                                                      |

## Massenscans in Docker ausführen

Das [Repository von
Codex Security](https://github.com/openai/codex-security) enthält eine gehärtete
Compose-Konfiguration für automatisierte CSV-Kampagnen auf einem Linux-Docker-Host. Der
Host muss das Erstellen von User-Namespaces ohne Root-Rechte unterstützen.

Binde die Repository-CSV, die Scanergebnisse und den Anmeldestatus aus persistenten
Verzeichnissen ein. Stelle OpenAI-Zugangsdaten über die Umgebung oder einen
Secret-Manager bereit. Stelle für private GitHub-Repositories `GH_TOKEN` oder `GITHUB_TOKEN`
auf dieselbe Weise bereit.

Führe das Image mit eingebundener CSV und eingebundenem Ausgabeverzeichnis aus:

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

Verwende dieselbe eingebundene CSV und dasselbe eingebundene Ausgabeverzeichnis, um die Kampagne fortzusetzen. Setze für
GitHub Enterprise Server `CODEX_SECURITY_GIT_HOST` auf deinen GitHub-Host.

Alle verfügbaren Flags findest du in der [Referenz zum
bulk-scan-Befehl](/de-DE/codex/security/cli/reference#codex-security-bulk-scan). Antworten auf häufige
Fragen zur Scanabdeckung und zu Befunden findest du in den [FAQ zur
CLI](/de-DE/codex/security/cli/faq).
