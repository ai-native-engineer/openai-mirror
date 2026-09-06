<!-- source: https://learn.chatgpt.com/de-DE/docs/security/cli/ci -->

Führe die Codex Security CLI in CI aus, um exakt die Änderungen in einem Pull Request
oder Merge Request zu überprüfen, Befunde und Abdeckungsdaten zu sichern und die Prüfung optional ab
einem gewählten Schweregrad fehlschlagen zu lassen. Beginne mit rein informativen Ergebnissen, überprüfe die Qualität und
Laufzeit der Scans und ergänze anschließend eine Richtlinie für Schweregrade, die zu deinem Repository passt.

  Installiere das öffentliche Paket `@openai/codex-security`. Für Scans ist weiterhin
  Zugriff auf Codex Security erforderlich.

Dieser Leitfaden enthält Beispiele für GitHub Actions und GitLab CI/CD. Dieselben Befehle zum Scannen
und Exportieren funktionieren auch in anderen CI-Systemen.

## Ablauf vorbereiten

Hinterlege einen OpenAI-API-Schlüssel als
`CODEX_SECURITY_API_KEY` im Secrets-Speicher deines CI-Anbieters.

Ordne dieses Secret direkt der Umgebungsvariablen `OPENAI_API_KEY` des Scan-Schritts zu.
Stelle die Zugangsdaten nur dem Scan-Prozess zur Verfügung und verwende
`--auth api-key`, um sie explizit auszuwählen.

Führe den Ablauf nur für Repositorys und Pull Requests aus, denen du vertraust. Scans verwenden
die lokalen Berechtigungen des Runners und warten nicht auf eine Genehmigung. Scan-Prozesse
können die Job-Umgebung erben. Halte deshalb nicht zum Scan gehörende Token und Cloud-Zugangsdaten
aus dieser Umgebung fern.

Der Runner benötigt:

- Node.js 22 (Version 22.13.0 oder neuer), 24 oder 26.
- Python 3.10 oder neuer.
- Das veröffentlichte Paket `@openai/codex-security`, das außerhalb des
  ausgecheckten Repositorys installiert ist.
- Den Verlauf von Head und Basis des Pull Requests oder Merge Requests, damit Git
die Merge-Basis berechnen kann.

## Ablauf für GitHub Actions hinzufügen

Aktiviere für private oder interne Repositorys
[GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github),
bevor du SARIF hochlädst.

Erstelle `.github/workflows/codex-security.yml`. Bevor du den Pull Request auscheckst,
installiere `@openai/codex-security` unter
`$RUNNER_TEMP/codex-security`, damit die vertrauenswürdige ausführbare Datei unter
`$RUNNER_TEMP/codex-security/node_modules/.bin/codex-security` verfügbar ist:

```yaml
name: Codex Security scan

on:
  pull_request:

jobs:
  codex-security:
    if: github.event.pull_request.head.repo.full_name == github.repository && github.actor != 'dependabot[bot]'
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    steps:
      - name: Set up Node.js
        uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7
        with:
          node-version: "26"

      - name: Set up Python
        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7
        with:
          python-version: "3.14"

      - name: Install Codex Security
        run: |
          set -euo pipefail
          npm install \
            --prefix "$RUNNER_TEMP/codex-security" \
            --ignore-scripts \
            --no-audit \
            --no-fund \
            @openai/codex-security

      - name: Verify Codex Security
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
        run: |
          set -euo pipefail
          test -x "$CODEX_SECURITY_BIN"
          "$CODEX_SECURITY_BIN" --version

      - name: Check out the pull request
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Scan the pull request
        env:
          OPENAI_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          CODEX_SECURITY_STATE_DIR: ${{ runner.temp }}/codex-security-state
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
        run: |
          set -euo pipefail
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          "$CODEX_SECURITY_BIN" scan . \
            --diff "$BASE_REVISION" \
            --head "$HEAD_SHA" \
            --auth api-key \
            --output-dir "$SCAN_DIR" \
            --json > "$RUNNER_TEMP/codex-security.json"

      - name: Export SARIF
        id: export-sarif
        if: always()
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
          SARIF_FILE: ${{ runner.temp }}/codex-security.sarif
        run: |
          set -euo pipefail
          if test -f "$SCAN_DIR/scan-manifest.json"; then
            "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
              --export-format sarif \
              --source-root "$GITHUB_WORKSPACE" \
              --output "$SARIF_FILE"
            echo "available=true" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload SARIF
        if: always() && steps.export-sarif.outputs.available == 'true'
        uses: github/codeql-action/upload-sarif@e4fba868fa4b1b91e1fdab776edc8cfbe6e9fb81 # v4
        with:
          sarif_file: ${{ runner.temp }}/codex-security.sarif
          ref: refs/pull/${{ github.event.pull_request.number }}/head
          sha: ${{ github.event.pull_request.head.sha }}
          category: codex-security

      - name: Preserve scan results
        if: always()
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7
        with:
          name: codex-security-results
          path: |
            ${{ runner.temp }}/codex-security-results
            ${{ runner.temp }}/codex-security.json
          if-no-files-found: warn
          retention-days: 7

Der Ablauf checkt den Head des Pull Requests aus, berechnet dessen Merge-Basis und
scannt die per Commit gespeicherten Änderungen zwischen diesen Revisionen. Der vollständige Verlauf stellt sicher,
dass genau die vorgesehenen Änderungen gescannt werden. `persist-credentials: false` verhindert, dass das Repository-Token in
der Git-Konfiguration des ausgecheckten Repositorys gespeichert wird. Wenn die CLI vor dem Checkout installiert und
über ihren absoluten Pfad ausgeführt wird, erhalten vom Repository kontrollierte ausführbare Dateien keinen Zugriff auf
die Zugangsdaten für den Scan. `--auth api-key` wählt explizit den auf den Scan-Prozess beschränkten API-Schlüssel aus.
Der Scan speichert seinen Verlauf in einem beschreibbaren Zustandsverzeichnis außerhalb des
Repositorys.

`--json` schreibt ein vollständiges JSON-Dokument nach stdout, sodass der Ablauf es
direkt speichern kann. Fortschrittsmeldungen, Abschlusszusammenfassungen und Fehler werden weiterhin über stderr ausgegeben.
Im Gegensatz dazu gibt `codex exec --json` einen Ereignisstream im Format JSON Lines aus.

Der Exportschritt liest einen abgeschlossenen, versiegelten Scan und schreibt SARIF. Die
Codex-Laufzeit und die Zugangsdaten bleiben unverändert. Scan-Artefakte können Quellcodeausschnitte mit Schwachstellen,
Belege und Details zur Behebung enthalten. Wähle für dein Repository geeignete Zugriffskontrollen und eine
kurze Aufbewahrungsfrist.

## Pipeline für GitLab CI/CD hinzufügen

Für einen Ablauf im Produktivbetrieb mit geschützten Scans des Standard-Branches, geplanten vertieften Scans nach ausdrücklicher Aktivierung,
einer separaten SARIF-Prüfung zur Durchsetzung der Richtlinie und optionalen verifizierten Merge Requests im Entwurfsstatus
folge der Anleitung [Codex Security in GitLab
CI/CD ausführen](/de-DE/codex/security/cli/ci/gitlab).

GitLab kann ab GitLab Ultimate 19.2
[Berichte im Format SARIF 2.1.0](https://docs.gitlab.com/ci/yaml/artifacts_reports/#artifactsreportssarif)
einlesen. Füge vor dem Ausführen der Pipeline eine maskierte und ausgeblendete
CI/CD-Variable namens `CODEX_SECURITY_API_KEY` hinzu.

Das folgende Minimalbeispiel fügt einen `security`-Job, der ausschließlich scannt, zur Datei
`.gitlab-ci.yml` im Stammverzeichnis hinzu. Behalte alle vorhandenen Stages und Jobs in der Datei bei. Der Job scannt standardmäßig
Änderungen aus Merge Requests. Setze `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH`
auf `"true"`, um zusätzlich den gesamten Standard-Branch zu scannen:

```yaml
variables:
  CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH: "false"

stages:
  - test
  - security

codex-security:
  stage: security
  image: node:26-bookworm-slim
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "diff"
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH && $CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH == "true"'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "full"
  variables:
    GIT_DEPTH: "0"
    CODEX_SECURITY_CLI_DIR: "/tmp/codex-security-cli"
  before_script:
    - |
      set -eu
      apt-get update -qq
      apt-get install -y -qq --no-install-recommends \
        ca-certificates \
        git \
        python3 \
        ripgrep
      npm install \
        --prefix "$CODEX_SECURITY_CLI_DIR" \
        --ignore-scripts \
        --no-audit \
        --no-fund \
        @openai/codex-security@0.1.20

      test -x "$CODEX_SECURITY_BIN"
      "$CODEX_SECURITY_BIN" --version
  script:
    - |
      set -eu
      if test -z "${CODEX_SECURITY_API_KEY:-}"; then
        echo "Set the CODEX_SECURITY_API_KEY CI/CD variable." >&2
        exit 2
      fi

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      case "${CODEX_SECURITY_SCAN_SCOPE:-}" in
        diff)
          BASE_SHA="$CI_MERGE_REQUEST_DIFF_BASE_SHA"
          HEAD_SHA="$CI_COMMIT_SHA"
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          set -- --diff "$BASE_REVISION" --head "$HEAD_SHA"
          echo "Scanning committed changes from $BASE_REVISION to $HEAD_SHA."
          ;;
        full)
          set -- --mode standard
          echo "Scanning the complete default branch at $CI_COMMIT_SHA."
          ;;
        *)
          echo "Unsupported Codex Security scan scope: ${CODEX_SECURITY_SCAN_SCOPE:-unset}" >&2
          exit 2
          ;;
      esac

      SCAN_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      JSON_FILE="/tmp/codex-security-$CI_JOB_ID.json"
      SARIF_FILE="/tmp/codex-security-$CI_JOB_ID.sarif"

      install -d -m 700 "$CODEX_SECURITY_STATE_DIR" "$SCAN_DIR"

      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          "$@" \
          --auth api-key \
          --output-dir "$SCAN_DIR" \
          --json > "$JSON_FILE"
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      install -d -m 700 codex-security-artifacts/results
      cp -R "$SCAN_DIR"/. codex-security-artifacts/results/
      if test -s "$JSON_FILE"; then
        cp "$JSON_FILE" codex-security-artifacts/codex-security.json
      fi
      printf '%s\n' "$scan_exit" > codex-security-artifacts/scan-exit-code.txt

      export_exit=0
      if test -f "$SCAN_DIR/scan-manifest.json"; then
        set +e
        "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
          --export-format sarif \
          --source-root "$CI_PROJECT_DIR" \
          --output "$SARIF_FILE"
        export_exit="$?"
        set -e
        if test -s "$SARIF_FILE"; then
          cp "$SARIF_FILE" codex-security-artifacts/codex-security.sarif
        fi
      fi

      if test "$scan_exit" -ne 0; then
        exit "$scan_exit"
      fi
      exit "$export_exit"
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/codex-security.sarif

Standardmäßig wird der Job nur für Merge Requests aus Branches desselben
Projekts ausgeführt, sodass Fork-Pipelines die Zugangsdaten für den Scan nicht erhalten. Setze
`CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` auf `"true"`, und zwar auf Gruppen-, Projekt- oder
Pipelineebene, um zusätzlich einen regulären vollständigen Scan des Standard-Branches auszuführen.
Vollständige Scans dauern länger und kosten mehr als Diff-Scans.

`GIT_DEPTH: "0"` stellt den für Merge-Request-Scans erforderlichen Verlauf bereit. Damit lässt sich die Merge-Basis anhand von
`CI_MERGE_REQUEST_DIFF_BASE_SHA` und `CI_COMMIT_SHA` berechnen.

Der Job installiert die CLI unter `/tmp`, führt sie über ihren absoluten Pfad aus und macht
den API-Schlüssel ausschließlich für den Scan-Prozess verfügbar. Mit `artifacts: when: always` bleibt der SARIF-Bericht
erhalten, wenn der Scan fehlschlägt, während `artifacts:access: maintainer` den Zugriff
auf detaillierte Scan-Ergebnisse beschränkt.

Änderungen an `.gitlab-ci.yml` können CI/CD-Variablen offenlegen. Überprüfe deshalb Änderungen an der Pipeline,
bevor du den Job ausführst. Wenn du
[`CODEX_SECURITY_API_KEY` schützt](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners),
stellt GitLab die Variable nur für Merge Requests desselben Projekts zwischen
geschützten Branches bereit und nur dann, wenn die betreffende Person auf den Ziel-Branch zugreifen kann.

Der separate GitLab-Leitfaden erweitert diesen minimalen Job zum Ablauf für den Produktivbetrieb,
der am Anfang dieses Abschnitts verlinkt ist.

## Richtlinie für Schweregrade festlegen

Beide Beispiele erstellen nur Berichte, da sie `--fail-on-severity` nicht enthalten. Sobald
Befunde das Ergebnis der Prüfung beeinflussen sollen, füge einen Schwellenwert
zum Scan-Befehl hinzu:

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --fail-on-severity high

Die unterstützten Schwellenwerte sind `critical`, `high`, `medium` und `low`.
Ein Schwellenwert berücksichtigt Befunde des aktuellen Scans mit diesem oder einem höheren Schweregrad.
Frühere offene Befunde in der Repository-Zusammenfassung wirken sich nicht auf die Richtlinie aus.

Der Scan-Schritt verwendet folgende Exit-Codes:

| Exit-Code  | Bedeutung                                                                                 |
| ----- | --------------------------------------------------------------------------------------- |
| `0`   | Der Scan wurde mit vollständiger Abdeckung abgeschlossen und jede konfigurierte Richtlinie wurde eingehalten.            |
| `1`   | Der abgeschlossene Scan enthält einen Befund, dessen Schweregrad mindestens dem Schwellenwert entspricht.                        |
| `2`   | Die CLI hat einen Eingabe- oder Laufzeitfehler erkannt oder der abgeschlossene Scan weist eine unvollständige Abdeckung auf. |
| `130` | Ctrl-C hat den Scan unterbrochen.                                                            |
| `143` | SIGTERM hat den Scan beendet.                                                            |

Ein Scan mit dem Abdeckungsstatus `partial` oder `unknown` gibt `2` zurück, auch ohne Richtlinie für Schweregrade.
Die CLI schreibt dennoch die verfügbaren Befunde und Abdeckungsdaten. Überprüfe die
zurückgestellten Bereiche in `coverage.json`, bevor du das Prüfergebnis als abschließend betrachtest.

## Scan mit einem vorhandenen Ergebnisverzeichnis wiederholen

Verwende für jeden CI-Job ein neues Runner-Verzeichnis. Sichere bei einem persistenten oder selbst gehosteten
Runner ein früheres Ergebnis mit `--archive-existing`:

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --archive-existing

Der Befehl archiviert die vorherigen Ergebnisse und startet mit einem leeren Scan-Verzeichnis.

## Probleme mit einem CI-Scan beheben

- **Unbekannte Git-Referenz oder unerwarteter Diff:** Rufe den Verlauf von Basis und Head ab,
  berechne die Merge-Basis und übergib beide Revisionen explizit.
- **Geschütztes oder nicht leeres Ausgabeverzeichnis:** Wähle ein privates Verzeichnis
  außerhalb des übergeordneten Git-Worktrees. Verwende `--archive-existing`, wenn das
  Verzeichnis bereits Ergebnisse enthält.
- **Fehlende Zugangsdaten:** Stelle sicher, dass `CODEX_SECURITY_API_KEY` für
  den vertrauenswürdigen Ablauf oder die vertrauenswürdige Pipeline verfügbar ist und direkt der
Umgebungsvariablen `OPENAI_API_KEY` des Scan-Prozesses zugeordnet wird.
- **Fehler im Scan-Verlauf:** Setze `CODEX_SECURITY_STATE_DIR` auf ein beschreibbares
  Verzeichnis außerhalb des Repositorys.
- **Fehler beim Python-Setup:** Stelle sicher, dass der Runner Python 3.10 oder neuer verwendet.
- **Unvollständige Abdeckung:** Überprüfe `coverage.json` einschließlich zurückgestellter Bereiche
  und offener Fragen. Führe den Scan anschließend mit einem geeigneten Ziel oder einer geeigneten Umgebung erneut aus.
- **Fehler beim SARIF-Export:** Stelle sicher, dass der Scan abgeschlossen wurde und das vollständige
  Scan-Verzeichnis verfügbar ist. Beim Export werden die versiegelten Artefakte validiert, bevor
  SARIF geschrieben wird.
- **Fehler beim SARIF-Upload:** Stelle für GitHub Actions sicher, dass deine Organisation
  GitHub Code Security für das Repository aktiviert hat und der Ablauf die Berechtigungen
`actions: read`, `contents: read` und `security-events: write` erteilt.
  Stelle für GitLab CI/CD sicher, dass das Projekt GitLab Ultimate 19.2 oder neuer verwendet und
  der Job über `artifacts:reports:sarif` eine SARIF-2.1.0-Datei hochlädt.

Details zu allen Befehlen, Flags, Artefakten und Ausgabefeldern findest du in der [Referenz zur
CLI](/de-DE/codex/security/cli/reference). Informationen zu einer interaktiven CI-Überprüfung mit einem Plug-in findest du unter
[Codeänderungen auf Sicherheitsprobleme überprüfen](/de-DE/codex/security/plugin/code-changes#automate-reviews-in-cicd).
