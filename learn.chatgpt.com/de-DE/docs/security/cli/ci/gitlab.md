<!-- source: https://learn.chatgpt.com/de-DE/docs/security/cli/ci/gitlab -->

Führe Codex Security in GitLab CI/CD aus, um committete Änderungen und geschützte
Branches zu scannen, Befunde in GitLab Security zu veröffentlichen und optional verifizierte
Korrekturen in Merge-Request-Entwürfen vorzuschlagen.

Der Ablauf hält Zugangsdaten für Scans vom Schreibzugriff auf das Repository getrennt.
Generierte Änderungen müssen vor dem Merge immer von einem Menschen überprüft werden.

Beginne mit Scans, die nur Berichte erstellen. Aktiviere die Behebung von Schwachstellen erst, nachdem du den
Runner, die Befunde und die Zugriffsgrenzen für die Zugangsdaten in deinem Projekt geprüft hast.

## Bevor du beginnst

Du brauchst:

- Ein GitLab-Projekt mit einem vertrauenswürdigen Runner, der den
Benutzernamensraum der Codex-Sandbox unterstützt.
- Die Rolle Maintainer oder Owner im GitLab-Projekt, damit du
[CI/CD-Variablen des Projekts](https://docs.gitlab.com/ci/variables/) und geschützte
  Ressourcen konfigurieren kannst.
- Einen OpenAI-API-Schlüssel mit Zugriff auf Codex Security. Organisationen, die API-Schlüssel der Plattform verwenden,
  können [Trusted Access for Cyber
  beantragen](https://openai.com/form/enterprise-trusted-access-for-cyber/).
  Einzelpersonen, die sich über ChatGPT authentifizieren, können den [Ablauf für den persönlichen
  Trusted Access](https://chatgpt.com/cyber) nutzen. Für einige Konten oder Repositorys ist dieser Zugriff
  für Scans des gesamten Repositorys erforderlich.
- GitLab Ultimate 19.2 oder neuer für [den Import von
  SARIF 2.1.0](https://docs.gitlab.com/user/application_security/detect/sarif/).
- Den vollständigen Git-Verlauf, damit Merge-Request-Jobs die Merge-Basis berechnen können.

Das Pipeline-Image installiert Node.js 26, Python 3, Git, `rg` und die festgelegte Version
der Codex Security CLI. Die automatisierte Behebung von Schwachstellen erfordert außerdem einen vorhandenen
Regressionstest und einen Runner, der vom Repository vorgegebene Befehle
ohne geschützte Zugangsdaten ausführen kann.

## Mit einer reinen Scan-Pipeline beginnen

Erstelle eine maskierte, verborgene und geschützte GitLab-CI/CD-Variable namens
`CODEX_SECURITY_API_KEY`. Verwende einen API-Schlüssel der OpenAI-Plattform mit Zugriff auf Codex Security
und lege für die Variable den Umgebungsbereich `codex-security/openai` fest. Siehe
[auf Umgebungen beschränkte CI/CD-Variablen](https://docs.gitlab.com/ci/environments/#limit-the-environment-scope-of-a-cicd-variable).

Füge diese minimale Pipeline zunächst einem Testprojekt hinzu. Sie scannt committete Änderungen
in geschützten Merge Requests, die die Voraussetzungen erfüllen, veröffentlicht SARIF über einen erfolgreich abgeschlossenen Berichtsjob
und stellt das Scannergebnis in einer separaten Prüfstufe wieder her:

```yaml
stages:
  - security_scan
  - security_gate

.codex-security-merge-request:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID && $CI_MERGE_REQUEST_SOURCE_BRANCH_PROTECTED == "true" && $CI_MERGE_REQUEST_TARGET_BRANCH_PROTECTED == "true"'

codex-security:
  extends: .codex-security-merge-request
  stage: security_scan
  image: node:26-bookworm-slim
  environment:
    name: codex-security/openai
    action: access
  variables:
    GIT_DEPTH: "0"
  before_script:
    - npm install --prefix /tmp/codex-security-cli --ignore-scripts --no-audit --no-fund @openai/codex-security@0.1.20
  script:
    - |
      set -eu
      test -n "${CODEX_SECURITY_API_KEY:-}"

      CODEX_SECURITY_BIN="/tmp/codex-security-cli/node_modules/.bin/codex-security"
      RESULTS_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      ARTIFACT_DIR="codex-security-artifacts"
      BASE_REVISION="$(git merge-base \
        "$CI_MERGE_REQUEST_DIFF_BASE_SHA" "$CI_COMMIT_SHA")"
      install -d -m 700 "$RESULTS_DIR" "$ARTIFACT_DIR/results"

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY
      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          --diff "$BASE_REVISION" \
          --head "$CI_COMMIT_SHA" \
          --auth api-key \
          --output-dir "$RESULTS_DIR" \
          --json
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      case "$scan_exit" in
        0|1|2) ;;
        *) exit "$scan_exit" ;;
      esac

      "$CODEX_SECURITY_BIN" export "$RESULTS_DIR" \
        --export-format sarif \
        --source-root "$CI_PROJECT_DIR" \
        --output "$ARTIFACT_DIR/results.sarif"
      test -s "$ARTIFACT_DIR/results.sarif"
      cp -R "$RESULTS_DIR"/. "$ARTIFACT_DIR/results/"
      printf '%s\n' "$scan_exit" > "$ARTIFACT_DIR/scan-exit-code.txt"
      exit 0
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/results.sarif

codex-security-gate:
  extends: .codex-security-merge-request
  stage: security_gate
  image: alpine:3.20
  needs:
    - job: codex-security
      artifacts: true
  script:
    - exit "$(cat codex-security-artifacts/scan-exit-code.txt)"

  

Überprüfe jede Änderung an `.gitlab-ci.yml`, bevor du einen Job mit Zugriff auf Secrets ausführst.
Das Minimalbeispiel verzichtet bewusst auf vollständige Scans und die Behebung von Schwachstellen.

## Pipeline für den Produktivbetrieb übernehmen

1. [Lade die vollständige GitLab-Pipeline herunter](/codex/security/cli/ci/gitlab.yml)
   und speichere sie als `.gitlab-ci.yml` im Stammverzeichnis des Repositorys. Wenn dein Repository
   bereits eine Pipeline hat, übernimm die Phasen, versteckten Vorlagen und
   Jobs aus dem Beispiel in die vorhandene Datei.
2. Behalte vorhandene Build-, Test- und Deployment-Phasen bei. Wenn das Projekt
`workflow: rules` verwendet, stelle sicher, dass diese Regeln die Pipeline-Ereignisse zulassen, die du
   scannen möchtest.

Das Beispiel fügt die Phasen `security_scan`, `security_remediation`, `security_publish`
und `security_gate` hinzu. Für reine Scan-Berichte brauchst du nur
`CODEX_SECURITY_API_KEY`.

Standardmäßig läuft der Scan-Job nur für Merge Requests zwischen
geschützten Branches desselben Projekts. Setze `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH=true`, um Scans
bei Pushes auf den geschützten Standardbranch und in manuell gestarteten Pipelines auszuführen. Setze
`CODEX_SECURITY_SCHEDULED_DEEP_SCAN=true` und lege explizite Zeit- und Kostenbudgets fest,
um geplante Tiefenscans auf dem geschützten Standardbranch zu aktivieren.

Eine Merge-Request-Pipeline kann nur dann auf geschützte Variablen und Runner zugreifen, wenn folgende Bedingungen erfüllt sind:

- Du schützt den Quell- und den Zielbranch im selben Projekt.
- Das Projekt [erlaubt Merge-Request-Pipelines den Zugriff auf geschützte Variablen und
  Runner](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners).
- Die Person, die die Pipeline startet, darf in den Zielbranch pushen oder mergen.

Pipelines in Forks und ungeschützte Merge Requests erhalten keine Zugangsdaten
für den Scan. Überprüfe jede Änderung an `.gitlab-ci.yml`, bevor du einen
Job mit Zugriff auf Secrets ausführst. Das Maskieren und Verbergen einer Variablen macht nicht vertrauenswürdigen CI-Code
nicht sicher.

## Scan ausführen und Befunde überprüfen

Erstelle einen geschützten Merge Request, der die Voraussetzungen erfüllt, oder führe die Pipeline auf dem
geschützten Standardbranch aus. Beginne mit einem kleinen Diff, bevor du einen kostenpflichtigen
Scan des gesamten Repositorys ausführst.

Öffne den Job `codex-security` und stelle sicher, dass seine Artefakte Folgendes enthalten:

- `scan-manifest.json`
- `findings.json`
- `coverage.json`
- `results.sarif`
- `scan-exit-code.txt`

Öffne dann in der Pipeline den Tab **Sicherheit** , prüfe Warnungen zum Import und kontrolliere
die Kennungen, Schweregrade und Quellcodepositionen der Befunde. Scans des Standardbranches
erstellen außerdem Schwachstelleneinträge für das Projekt. Befunde aus Merge Requests erscheinen
im Tab Sicherheit der Pipeline oder im Sicherheits-Widget des Merge Requests. Daraus entstehen jedoch keine
projektweiten Schwachstelleneinträge.

Beschränke den Zugriff auf Artefakte, da Scannergebnisse Quellcodeausschnitte mit Schwachstellen,
Belege und Details zur Behebung enthalten können.

## Scan-Profil auswählen

Die Pipeline wählt das Profil anhand des auslösenden Ereignisses aus:

| Auslöser                                        | Ziel          | Modus       | Aufwand  |
| ---------------------------------------------- | --------------- | ---------- | ------- |
| Geschützter Merge Request innerhalb desselben Projekts           | Committeter Diff  | `standard` | `low`   |
| Push auf den geschützten Standardbranch oder manueller Start, jeweils nach ausdrücklicher Aktivierung | Gesamtes Repository | `standard` | `high`  |
| Geplante Ausführung auf dem geschützten Standardbranch nach ausdrücklicher Aktivierung    | Gesamtes Repository | `deep`     | `xhigh` |

Scans von Merge Requests liefern Rückmeldungen gezielt zur committeten Änderung.
Scans des Standardbranches prüfen das Repository mit den integrierten Änderungen. Geplante Tiefenscans
sorgen regelmäßig für eine umfassendere Abdeckung. Ein abgeschlossener Diff-Scan gilt nur für die betreffende
Änderung und belegt nicht, dass das gesamte Repository frei von Schwachstellen ist.

Im Ablauf wird die CLI außerhalb des Repositorys installiert und über einen absoluten
Pfad ausgeführt. Die Vorabprüfung im Probelauf verwendet den auf den Prozess beschränkten API-Schlüssel, startet aber keinen
kostenpflichtigen Scan. Sie prüft weder die API-Authentifizierung noch den Zugriff auf Codex Security, das Kontingent oder die
Modellverfügbarkeit.

Der Ablauf speichert Scan-Status und Ergebnisse außerhalb des Worktrees und beschränkt
`OPENAI_API_KEY` auf den Scan-Prozess. Die CLI erhält eine kleine, explizit definierte
Prozessumgebung, statt sämtliche GitLab-Variablen zu erben. Für Diff-Scans berechnet der
Ablauf die Merge-Basis und bindet den Scan an die überprüften Basis- und
Head-Revisionen.

Das Beispiel legt `@openai/codex-security` auf Version `0.1.20` fest. Teste Authentifizierung,
Artefakte, SARIF-Import und Richtlinienprüfung erneut, bevor du die festgelegte Version änderst.

## Berichterstellung und Durchsetzung von Richtlinien trennen

GitLab importiert SARIF aus einem erfolgreich abgeschlossenen Berichtsjob. Die Pipeline veröffentlicht zuerst den
Bericht und stellt den Exit-Status des Scanners in einem separaten
Job namens `codex-security-gate` wieder her.

Der Berichtsjob akzeptiert Befunde bei den Exitcodes `0` und `1`. Den Exitcode
`2` akzeptiert er nur, wenn das Scan-Manifest belegt, dass der Scan abgeschlossen ist, die Abdeckung
explizit als `partial` ausgewiesen ist und ein nicht leerer SARIF-Bericht vorliegt. Andere Laufzeit-,
Konfigurations- oder Exportfehler blockieren weiterhin die Pipeline.

Die abschließende Prüfstufe behält diese Exitcodes des Scanners bei:

| Exitcode | Bedeutung                                                                     |
| ---- | --------------------------------------------------------------------------- |
| `0`  | Der Scan wurde mit vollständiger Abdeckung abgeschlossen und hat die Richtlinienprüfung bestanden.            |
| `1`  | Der Scan wurde abgeschlossen und hat ein Problem gefunden, das den konfigurierten Schwellenwert erreicht oder überschreitet. |
| `2`  | Die Abdeckung des Scans war unvollständig, oder es trat ein Eingabe- oder Laufzeitfehler auf.              |

Im Beispiel ist der Exit-Code `2` vorübergehend zulässig, während du den Umgang mit teilweiser Abdeckung abstimmst.
Entferne diese Ausnahme, wenn eine unvollständige Abdeckung die Pipeline blockieren muss.

Behebung und Veröffentlichung erfolgen vor der abschließenden Richtlinienprüfung. Aus einem geeigneten Befund kann ein verifizierter Merge Request im Entwurfsstatus entstehen, selbst wenn die Prüfung die Pipeline später fehlschlagen lässt.

## Verifizierte Behebung aktivieren

Die automatisierte Behebung ist optional und wird nur in Pipelines für den geschützten Standard-Branch ausgeführt. Der Codex-Prozess zur Behebung und die vom Repository gesteuerten Verifizierungsbefehle erhalten weder das GitLab-Projektzugriffstoken noch vom Runner bereitgestellte Zugangsdaten.

Die Sicherheitsvorgaben bestehen aus drei Teilen: Vom Repository gesteuerte Befehle erhalten niemals Zugangsdaten für OpenAI oder GitLab, nur der Veröffentlichungsjob erhält Schreibzugriff auf das Repository, und jede generierte Änderung bleibt ein Entwurf, bis ein Mensch sie überprüft und zusammenführt.

Der Ablauf:

1. Erfordert vollständige Scanabdeckung und einen Befund
   mit dem Schweregrad `high` oder `critical`.
2. Bestätigt, dass der konfigurierte Regressionstest vor dem Anwenden des Patches fehlschlägt.
3. Erstellt einen gezielten Patch und lehnt Änderungen an CI-Dateien, Dateien mit Zugangsdaten, Binärdateien oder anderen geschützten Dateien ab.
4. Führt den Regressionstest ohne Zugangsdaten für OpenAI, GitLab, Registrys oder Deployments und ohne Job-Token aus.
5. Verwendet `verify-fix`, um `fixed`, `still_vulnerable` oder `inconclusive` zurückzugeben.
   Der Job veröffentlicht einen Patch nur, wenn `verify-fix` den Wert `fixed` zurückgibt und
   der Verifizierungsprozess den Patch unverändert lässt.

Setze diese geschützten Variablen, um die Behebung zu aktivieren:

- Setze `CODEX_SECURITY_ENABLE_REMEDIATION` auf `true`.
- Setze `CODEX_SECURITY_VERIFICATION_COMMAND` auf einen vorhandenen Regressionstest, der
  vor der Korrektur mit dem Exit-Code `1` und danach mit `0` endet.
- Optional kannst du `CODEX_SECURITY_SETUP_COMMAND` auf einen nicht interaktiven Befehl
  zum Einrichten der Abhängigkeiten setzen.

Wähle einen Regressionstest, der die zugrunde liegende Sicherheitsinvariante prüft, nicht eine bestimmte Implementierung. Prüfe generierte Änderungen an Tests und Quellcode mit derselben Sorgfalt.

<details>
  <summary>Fortgeschritten: Repository-Befehle isolieren</summary>

Die Befehle `validate`, `patch` und `verify-fix` erhalten einen auf ihren jeweiligen Prozess beschränkten
`CODEX_API_KEY`. Vom Repository gesteuerte Setup- und Testbefehle werden unter einem
separaten, unprivilegierten Benutzerkonto in einer beschreibbaren Kopie der versionierten Quelldateien ausgeführt.
Die Kopie enthält absichtlich keine Git-Metadaten, Submodulinhalte oder
heruntergeladenen Artefakte. Setup- und Testbefehle, die `.git` oder
Submodule benötigen, müssen in einem gesondert konzipierten Job ohne Zugangsdaten ausgeführt werden.

Nur die Codex-Schritte im Besitz von root können auf den kanonischen Checkout oder das
danebenliegende GitLab-Verzeichnis für Dateivariablen zugreifen. Die bereinigte Umgebung der Kopie enthält nur
`PATH`, `HOME`, `LANG`, `CI` und `CI_PROJECT_DIR`. Wenn ein Befehl einen weiteren
nicht geheimen Wert benötigt, nimm ihn nach Prüfung des Befehls in die Zulassungsliste auf. Wenn dein
Runner das Benutzerkonto nicht wechseln kann, verlagere die Verifizierung in einen separaten Job
ohne Zugangsdaten, bevor du die Behebung aktivierst.

</details>

## Merge Request als Entwurf veröffentlichen

Erstelle ein [Projektzugriffstoken
für GitLab](https://docs.gitlab.com/user/project/settings/project_access_tokens/#create-a-project-access-token)
mit der Rolle Developer und den Scopes `api` und `write_repository`. Speichere es als
geschützte, maskierte und ausgeblendete Variable `GITLAB_REMEDIATION_TOKEN`, deren Geltungsbereich auf
die Umgebung `codex-security/publish` beschränkt ist.

Setze `CODEX_SECURITY_CREATE_MR=true`, um die Veröffentlichung zu aktivieren. Setze außerdem die nicht geheime Variable
`CODEX_SECURITY_MR_TEST_COMMAND` auf den projektspezifischen Sicherheitsregressionstest,
den jeder generierte Branch zur Behebung bestehen muss. Lass diese Variable
ungeschützt, damit der generierte ungeschützte Merge Request den Befehl lesen kann.
Der Ablauf zur Veröffentlichung:

- Erhält das Token mit Schreibzugriff auf das Repository, aber keine OpenAI-Zugangsdaten.
- Erstellt einen Branch namens `codex-security/fix-<finding-hash>`.
- Öffnet einen Merge Request als Entwurf und verwendet einen bereits offenen Entwurf erneut, statt ein Duplikat zu erstellen.
- Führt den Regressionstest des ungeschützten Branches zur Behebung unter einem unprivilegierten Benutzerkonto und ohne geschützte Zugangsdaten in einer Kopie aus, die nur versionierte Dateien enthält.
- Führt die generierte Änderung niemals automatisch zusammen.

Ersetze das Projektzugriffstoken nicht durch `CI_JOB_TOKEN`. Dieses Token unterstützt die erforderliche
Operation zum Erstellen eines Merge Requests nicht. Prüfe den vorgeschlagenen Patch,
die Verifizierungsnachweise und den Befund, bevor du die Änderung zusammenführst.

## Optionale Variablen konfigurieren

Konfiguriere nur die Variablen, die du für die Funktionen benötigst, die du aktivierst:

| Variable                                  | Wann erforderlich                       | Standardwert oder Zweck                                          |
| ----------------------------------------- | --------------------------------- | ----------------------------------------------------------- |
| `CODEX_SECURITY_API_KEY`                  | Bei jedem Scan                        | Geschützt, maskiert, ausgeblendet; auf `codex-security/openai` beschränken |
| `CODEX_SECURITY_VERSION`                  | CLI-Upgrade                       | Auf `0.1.20` angepinnt; vor einer Änderung erneut testen                  |
| `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` | Vollständige Scans des Standard-Branches         | Explizite Aktivierung erforderlich; standardmäßig deaktiviert                             |
| `CODEX_SECURITY_SCHEDULED_DEEP_SCAN`      | Geplante Tiefenscans              | Explizite Aktivierung erforderlich; standardmäßig deaktiviert                             |
| `CODEX_SECURITY_DEEP_MAX_TIME_HOURS`      | Geplante Tiefenscans              | Erforderliches Zeitbudget: größer als `0` und kleiner als `8`     |
| `CODEX_SECURITY_DEEP_MAX_COST`            | Geplante Tiefenscans              | Erforderliche Obergrenze für die geschätzten Kosten in USD: größer als `0`      |
| `CODEX_SECURITY_ENABLE_REMEDIATION`       | Patch-Erstellung                  | Aktivierung über eine geschützte Variable; standardmäßig deaktiviert                            |
| `CODEX_SECURITY_VERIFICATION_COMMAND`     | Patch-Erstellung                  | Geschützter Regressionstest                                   |
| `CODEX_SECURITY_SETUP_COMMAND`            | Optionales Setup für die Behebung        | Geschützte Installation von Abhängigkeiten                           |
| `CODEX_SECURITY_REMEDIATION_EFFORT`       | Optionale Feinabstimmung der Behebung       | `high`                                                      |
| `CODEX_SECURITY_MAX_CHANGED_FILES`        | Optionale Begrenzung der Patch-Größe         | `8`; zulässiger Bereich: `1` bis `20`                         |
| `CODEX_SECURITY_CREATE_MR`                | Erstellung von Merge Requests als Entwurf      | Aktivierung über eine geschützte Variable; standardmäßig deaktiviert                            |
| `GITLAB_REMEDIATION_TOKEN`                | Erstellung von Merge Requests als Entwurf      | Projekttoken mit der Rolle Developer, beschränkt auf `codex-security/publish`  |
| `CODEX_SECURITY_GITLAB_INTERNAL_URL`      | Optionale Veröffentlichung auf einer selbst gehosteten Instanz   | Vom Runner aus erreichbare GitLab-Ursprungsadresse                     |
| `CODEX_SECURITY_MR_TEST_COMMAND`          | Merge Requests als Entwurf veröffentlichen    | Erforderlicher projektspezifischer Regressionstest (nicht geheim)       |
| `CODEX_SECURITY_MR_SETUP_COMMAND`         | Optionales Setup für den Branch zur Schwachstellenbehebung | Setup der Abhängigkeiten (nicht geheim)                                 |

GitLab stellt die Variablen `CI_*` bereit. Die Pipeline verwaltet
`CODEX_SECURITY_BIN`, `CODEX_SECURITY_EFFORT`, `CODEX_SECURITY_MODE`,
`CODEX_SECURITY_STATE_DIR` und `CODEX_SECURITY_TARGET`. Konfiguriere sie nicht
als Projektvariablen. Bei Diff-Scans leitet die CLI die kanonische Identität des Ziels
aus den normalisierten Basis- und Head-Revisionen ab.

## Richtliniendurchsetzung und Kosten anpassen

Verwende gezielte Diff-Scans für Feedback zu Merge Requests, Standardscans des Repositorys
für den Standard-Branch und geplante Tiefenscans für eine umfassendere Abdeckung. Beide
Profile für das gesamte Repository sind standardmäßig deaktiviert. Ein geplanter Tiefenscan erfordert außerdem
`CODEX_SECURITY_DEEP_MAX_TIME_HOURS` und `CODEX_SECURITY_DEEP_MAX_COST`. Halte das
Zeitbudget der CLI unter dem achtstündigen Timeout des Jobs. Miss repräsentative Durchläufe,
bevor du ein Budget festlegst. Betrachte `--max-cost` als Grenze für die geschätzten Kosten, nicht
als feste Abrechnungsobergrenze.

Beginne mit Scans, die nur Berichte erstellen. Füge `--fail-on-severity` erst hinzu, nachdem dein Team
repräsentative Befunde, Abdeckung, Kosten und Laufzeit geprüft hat. Unter [Codex Security
in CI ausführen](/de-DE/codex/security/cli/ci) findest du Richtlinien zu Schweregraden und Details
zu Exit-Codes.

Wenn ein Job fehlschlägt:

- Fehlende Scan-Artefakte deuten auf ein Problem mit der Konfiguration oder dem Runner hin.
- Wenn Artefakte vorhanden sind, aber die Abdeckung unvollständig ist, prüfe `coverage.json`.
- Wenn in GitLab Befunde fehlen, prüfe, ob der Job für den SARIF-Bericht
erfolgreich war und ob GitLab den Bericht akzeptiert hat.
- Wenn die Schwachstellenbehebung übersprungen wurde, prüfe den geschützten Branch, die Vollständigkeit der
Abdeckung, den Schweregrad des Befunds, den Verifizierungsbefehl und die Variablen zur Aktivierung.
- Wenn die Veröffentlichung fehlschlägt, prüfe die Rolle, die Berechtigungsbereiche und
die Umgebungsbeschränkung des Projekt-Tokens.

Informationen zu allen Befehlen, Flags und Artefakten findest du in der [Referenz zur
Codex Security CLI](/de-DE/codex/security/cli/reference).
