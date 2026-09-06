<!-- source: https://learn.chatgpt.com/de-DE/docs/security/plugin/code-changes -->

Führe ein Sicherheits-Review durch, um Regressionen in einem einzelnen mit Git verwalteten Änderungssatz zu finden.
Codex überprüft jede geänderte Datei mit Quellcodecharakter sowie den direkt dazugehörigen Code.
Codex weitet das Review nicht auf ein vollständiges Audit des Repositorys aus.

Wenn du statt einer bestimmten Änderung ein ganzes Repository scannen möchtest, lies [Sicherheitsscan
ausführen](/de-DE/codex/security/plugin/scans).

## Manuelles Review durchführen

Öffne in der Desktop-App **Sicherheit**, wähle **Scans** und dann **+ Scan** aus.
Wähle das Repository und anschließend **Änderungen** aus. Überprüfe nicht committete Änderungen, einen
einzelnen Commit oder eine Basis- und eine Head-Revision. **Tiefenscan** ist für einen
Änderungsscan nicht verfügbar.

Du kannst Codex auch in einem Chat bitten, nicht committete Änderungen zu überprüfen:

```text
Use $codex-security:security-diff-scan to review my current uncommitted changes for security regressions.

Gib für einen Commit- oder Branch-Bereich bei Bedarf beide Revisionen an:

```text
Use $codex-security:security-diff-scan to review the changes from origin/main to HEAD for security regressions. Focus on authentication, authorization, input handling, filesystem access, network requests, and secrets.

Du kannst auch einen Pull Request angeben, wenn dessen Basis- und Head-Revisionen
im lokalen Checkout verfügbar sind.

## Änderung im Setup bestätigen

1. Wähle **Änderungen** aus.
2. Bestätige das ausgecheckte Repository, den aktuellen Branch und den neuesten Commit.
3. Wähle unter **Zu überprüfende Änderungen** eine der folgenden Optionen aus:
   - `Uncommitted changes` für den aktuellen Arbeitsbaum.
   - Den neuesten Commit für die Überprüfung eines einzelnen Commits.
   - Eine Basis- und eine Head-Revision für den Revisionsbereich eines Branches oder Pull Requests.
4. Vergewissere dich, dass die Zusammenfassung die Änderung beschreibt, die du überprüfen wolltest.
5. Wähle **Scan starten** aus.

Codex checkt keinen anderen Branch aus und wechselt nicht den ausgewählten Arbeitsbaum. Wenn
eine angeforderte Revision lokal nicht verfügbar ist, rufe sie vor dem Review ab oder
gib lokal verfügbare Basis- und Head-Revisionen an.

## Auf Befunde reagieren

Nachdem du die Ergebnisse überprüft hast, kannst du [einen akzeptierten
Befund beheben und verifizieren](/de-DE/codex/security/plugin/fix-findings) oder [Befunde exportieren und
nachverfolgen](/de-DE/codex/security/plugin/export-findings).

## Reviews in CI/CD automatisieren

Wenn du Zugriff auf die Beta-Version der eigenständigen CLI hast, findest du unter [Codex Security in
CI ausführen](/de-DE/codex/security/cli/ci) Informationen zu strukturiertem JSON, einer Richtlinie für Schweregrade und dem
Upload im SARIF-Format. In diesem Abschnitt erfährst du, wie du den installierten Skill des Plug-ins
über `codex exec` aufrufst.

Führe `$codex-security:security-diff-scan` in CI aus, wenn der Runner die
Codex CLI ohne Interaktion aufrufen kann. Installiere zuerst die CLI, ohne die
Zugangsdaten für den Scan offenzulegen:

```bash
npm install --global @openai/codex

Installiere das Codex-Security-Plugin in der CLI:

```bash
codex plugin add codex-security@openai-curated

Der Installationsbefehl nutzt den öffentlichen Marketplace für Plug-ins der Codex CLI. Prüfe das
[Änderungsprotokoll des Plug-ins](/de-DE/codex/security/plugin/changelog), bevor du dich in CI auf eine
bestimmte Plug-in-Version oder -Funktion verlässt.

Stelle anschließend einen OpenAI-API-Schlüssel aus dem Secret Store deines CI-Systems als
`CODEX_SECURITY_API_KEY` bereit. Mache die Zugangsdaten ausschließlich für den Scan verfügbar:

```bash
CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
  --sandbox workspace-write \
  "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

In der Sandbox mit Schreibzugriff kann der Scan temporäre Artefakte erstellen. Der Prompt
verlangt weiterhin, dass Codex den ausgecheckten Quellcode nicht verändert.

Der Scan schreibt die Ausgabe in
`$TMPDIR/codex-security-scans/<repository>/<scan-id>/`:

| Datei                 | Inhalt                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `report.md`          | Primärer lesbarer Einstiegspunkt in das gesamte Scan-Verzeichnis.                                                                                              |
| `findings/<slug>/`   | Detaillierte Schwachstellenberichte und ergänzende Proof-of-Concept-Dateien, sofern angefordert.                                                                     |
| `hardening/`         | Empfehlungen zur strukturellen Härtung und ergänzende Vorschläge, sofern angefordert.                                                                                   |
| `findings.json`      | Befunde mit stabilen Kennungen sowie Angaben zu Schweregrad, Konfidenz, Fundstellen im Quellcode und Behebung. Speise sie in genehmigte interne Arbeitsabläufe im Sicherheitsbereich oder nachgelagerte Tools ein. |
| `scan-manifest.json` | Versiegelter Scan-Nachweis mit dem überprüften Ziel, den Revisionen und den Artefakt-Hashes.                                                                             |
| `coverage.json`      | Überprüfte und zurückgestellte Bereiche, Ausschlüsse sowie Vollständigkeit der Abdeckung.                                                                                    |

Das [Schema für `findings.json`](https://github.com/openai/plugins/blob/main/plugins/codex-security/schemas/findings.schema.json)
definiert die vollständige Struktur. Das Schema umfasst folgende Felder:

| Feld                     | Typ   | Beschreibung                                                            |
| ------------------------- | ------ | ---------------------------------------------------------------------- |
| `documentType`            | String | Kennzeichnet das Dokument als `codex-security.findings`.                  |
| `schemaVersion`           | String | Gibt die Version des Befundschemas an.                                |
| `scanId`                  | String | Kennzeichnet den Scan, der die Befunde erzeugt hat.                        |
| `findings`                | Array  | Enthält null oder mehr Befundobjekte.                                 |
| `findings[].findingId`    | String | Stabile Befundkennung, die aus dem Fingerabdruck des Befunds abgeleitet wird.        |
| `findings[].occurrenceId` | String | Kennzeichnet dieses Vorkommen des Befunds in einem bestimmten Scan.          |
| `findings[].ruleId`       | String | Gibt die Schwachstellenfamilie an.                                   |
| `findings[].identity`     | Objekt | Enthält den semantischen Anker und die optionale Kennung einer gleichgeordneten Instanz. |
| `findings[].fingerprints` | Objekt | Enthält den Fingerabdruckalgorithmus und den primären Fingerabdruck.            |
| `findings[].title`        | String | Gibt den Kurztitel des Befunds an.                                      |
| `findings[].summary`      | String | Fasst die Schwachstelle und ihre Auswirkungen zusammen.                           |
| `findings[].severity`     | Objekt | Enthält den Schweregrad und optionale Details zur Bewertung.              |
| `findings[].confidence`   | Objekt | Enthält das Konfidenzniveau und die zugehörige Begründung.                           |
| `findings[].taxonomy`     | Objekt | Enthält die Schwachstellenkategorie und CWE-Kennungen.               |
| `findings[].locations`    | Array  | Listet betroffene Dateien, Zeilennummern und die Rollen der Fundstellen auf.                |
| `findings[].remediation`  | Zeichenfolge | Beschreibt die empfohlene Behebung.                                         |
| `findings[].provenance`   | Objekt | Gibt die Quelle des Befunds an.                                  |

Dieser Befehl gibt beispielsweise für jeden Befund eine tabulatorgetrennte Zeile aus:

```bash
jq -r '
  .findings[] |
  [.findingId, .severity.level, .confidence.level, .locations[0].path, .locations[0].startLine, .title] |
  @tsv
' findings.json

Diese Beispiele setzen einen vertrauenswürdigen Linux-Runner mit Node.js und `npm`, Git, Python
3, `jq` sowie den Befehlszeilentools des jeweiligen Anbieters voraus. Das globale Paketpräfix von `npm`
muss beschreibbar sein.

Wähle das passende Beispiel für deinen CI-Anbieter aus:

Scanergebnisse können sensible Details zu Schwachstellen enthalten. Behandle Artefakte
vertraulich und veröffentliche Befunde erst, nachdem du Zielgruppe, Inhalt und
erforderliche Genehmigungen geprüft hast.

  <div slot="github">

```yaml
name: Codex Security review

on:
  pull_request:

jobs:
  security-review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Install Codex Security
        env:
          CODEX_HOME: ${{ runner.temp }}/codex-home
        run: |
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated

      - name: Review code changes
        env:
          CODEX_SECURITY_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_HOME: ${{ runner.temp }}/codex-home
          TMPDIR: ${{ runner.temp }}/codex-security
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_REVISION: ${{ github.event.pull_request.head.sha }}
        run: |
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_REVISION")"
          CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
            --sandbox workspace-write \
            "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: codex-security-review
          path: ${{ runner.temp }}/codex-security/codex-security-scans

  </div>

  <div slot="gitlab">

Erstelle eine maskierte CI/CD-Variable namens `CODEX_SECURITY_API_KEY` und prüfe die
Scanartefakte vertraulich, bevor du Befunde weitergibst.

```yaml
codex-security-review:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
  variables:
    GIT_DEPTH: "0"
  script:
    - |
      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
      CODEX_API_KEY="$codex_security_api_key" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
  after_script:
    - |
      unset CODEX_SECURITY_API_KEY
      scan_root="/tmp/codex-security-$CI_JOB_ID/codex-security-scans"
      if [ -d "$scan_root" ]; then
        tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
      fi
  artifacts:
    when: always
    paths:
      - codex-security-artifacts.tar.gz

  </div>

  <div slot="azure">

```yaml
trigger: none

pool:
  vmImage: ubuntu-latest

steps:
  - checkout: self
    fetchDepth: 0

  - bash: |
      set -euo pipefail

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
    displayName: Install Codex Security

  - bash: |
      set -euo pipefail

      CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
    displayName: Review code changes
    condition: and(succeeded(), ne(variables['System.PullRequest.IsFork'], 'True'))
    env:
      CODEX_SECURITY_API_KEY: $(CODEX_SECURITY_API_KEY)

  - publish: $(Agent.TempDirectory)/codex-security/codex-security-scans
    artifact: codex-security-review
    condition: always()

Konfiguriere für Azure Repos eine Branch-Richtlinie zur **Buildüberprüfung** , damit die
Pipeline bei Pull Requests ausgeführt wird.

  </div>

  <div slot="jenkins">

```groovy
pipeline {
  agent { label 'linux' }
  stages {
    stage('Codex Security review') {
      when {
        allOf {
          changeRequest()
          expression { !env.CHANGE_FORK?.trim() }
        }
      }
      steps {
        sh '''#!/usr/bin/env bash
          set -euo pipefail

          mkdir -p "$TMPDIR"
          git fetch --no-tags origin "$CHANGE_TARGET"
          target="$(git rev-parse FETCH_HEAD)"
          git fetch --no-tags origin "$CHANGE_BRANCH"
          git rev-parse FETCH_HEAD > "$TMPDIR/head"
          git merge-base "$target" "$(cat "$TMPDIR/head")" > "$TMPDIR/base"
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated
        '''
        withCredentials([string(credentialsId: 'codex-security-api-key', variable: 'CODEX_SECURITY_API_KEY')]) {
          sh '''#!/usr/bin/env bash
            set +x
            set -euo pipefail

            CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
              --sandbox workspace-write \
              "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
          '''
        }
      }
      post {
        always {
          sh '''#!/usr/bin/env bash
            set -euo pipefail
            scan_root="/tmp/codex-security-$BUILD_TAG/codex-security-scans"
            if [ -d "$scan_root" ]; then
              tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
            fi
          '''
          archiveArtifacts artifacts: 'codex-security-artifacts.tar.gz', allowEmptyArchive: true
        }
      }
    }
  }
}

  </div>

Die Beispiele überspringen Pull Requests aus Forks. Starte Jobs mit hinterlegten Zugangsdaten nur auf Grundlage einer
geschützten Pipeline-Definition und nur für Mitwirkende, denen du die Scan-Zugangsdaten
anvertrauen kannst. Archiviere `codex-security-scans`, um die strukturierten Befunde,
das Manifest, die Abdeckung und `report.md` gemeinsam mit allen angeforderten
Ausgaben aus `findings/` oder `hardening/` aufzubewahren. Beginne mit rein informativen Ergebnissen und prüfe
Abdeckung und Laufzeit, bevor du den Job als verpflichtende Prüfung festlegst.

Informationen zum Umgang mit API-Schlüsseln und zur Steuerung der Sandbox findest du unter [Nicht interaktiver
Modus](/de-DE/codex/non-interactive-mode). Wenn deine Organisation die [Codex
GitHub Action](/de-DE/codex/github-action) zulässt, kann diese die CLI zur Laufzeit installieren, doch
du musst trotzdem zuerst das Plug-in installieren und den Eingabeparameter `codex-home`
der Action auf dasselbe `CODEX_HOME` setzen.
