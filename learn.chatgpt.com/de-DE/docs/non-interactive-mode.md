<!-- source: https://learn.chatgpt.com/de-DE/docs/non-interactive-mode -->

Im nicht interaktiven Modus kannst du Codex über Skripte ausführen, zum Beispiel in Jobs für Continuous Integration (CI), ohne die interaktive TUI zu öffnen.
Dazu verwendest du `codex exec`.

Details zu den einzelnen Flags findest du unter [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec).

## Wann du `codex exec` verwenden solltest

Mit `codex exec` kannst du:

- Codex als Teil einer Pipeline ausführen, etwa für CI, Prüfungen vor dem Merge oder geplante Jobs.
- Ausgaben erzeugen, die du per Pipe an andere Tools weitergeben kannst, zum Beispiel, um Versionshinweise oder Zusammenfassungen zu erstellen.
- Codex nahtlos in CLI-Arbeitsabläufe integrieren, in denen du Befehlsausgaben an Codex und Codex-Ausgaben an andere Tools weiterleitest.
- Codex mit explizit vorab festgelegten Einstellungen für Sandbox und Genehmigungen ausführen.

## Grundlegende Verwendung

Übergib einen Aufgaben-Prompt als einzelnes Argument:

```bash
codex exec "summarize the repository structure and list the top 5 risky areas"

Während `codex exec` ausgeführt wird, gibt Codex laufend Fortschrittsmeldungen über `stderr` und nur die abschließende Agentennachricht über `stdout` aus. So kannst du das Endergebnis einfach umleiten oder per Pipe weitergeben:

```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md

Verwende `--ephemeral`, wenn du die Rollout-Dateien einer Sitzung nicht dauerhaft auf dem Datenträger speichern möchtest:

```bash
codex exec --ephemeral "triage this repository and suggest next steps"

Wenn stdin per Pipe übergeben wird und du außerdem ein Prompt-Argument angibst, behandelt Codex den Prompt als Anweisung und den per Pipe übergebenen Inhalt als zusätzlichen Kontext.

So kannst du mit einem Befehl Eingaben erzeugen und direkt an Codex übergeben:

```bash
curl -s https://jsonplaceholder.typicode.com/comments \
  | codex exec "format the top 20 items into a markdown table" \
  > table.md

Weitere fortgeschrittene Muster für die stdin-Weiterleitung findest du unter [Fortgeschrittene stdin-Weiterleitung](#advanced-stdin-piping).

## Berechtigungen und Sicherheit

Standardmäßig wird `codex exec` in einer Sandbox ohne Schreibzugriff ausgeführt. Lege für Automatisierungen nur die Berechtigungen fest, die für den jeweiligen Ablauf unbedingt erforderlich sind:

- Bearbeitungen zulassen: `codex exec --sandbox workspace-write "<task>"`
- Umfassenderen Zugriff zulassen: `codex exec --sandbox danger-full-access "<task>"`

Verwende `danger-full-access` nur in einer kontrollierten Umgebung, zum Beispiel auf einem isolierten CI-Runner oder in einem Container.

Codex behält `codex exec --full-auto` als veraltetes Kompatibilitäts-Flag bei und gibt eine Warnung aus. Verwende in neuen Skripten stattdessen das explizite Flag `--sandbox workspace-write`.

Verwende `--ignore-user-config`, wenn `$CODEX_HOME/config.toml` bei einer Ausführung nicht geladen werden soll. Verwende `--ignore-rules`, wenn du in einer kontrollierten Automatisierungsumgebung execpolicy-Dateien mit der Endung `.rules` auf Benutzer- und Projektebene überspringen musst.

Wenn du einen aktivierten MCP-Server mit `required = true` konfigurierst und dessen Initialisierung fehlschlägt, bricht `codex exec` mit einem Fehler ab, anstatt ohne diesen Server fortzufahren.

## Ausgaben maschinenlesbar machen

Verwende Ausgaben im Format JSON Lines, um Codex-Ausgaben in Skripten zu verarbeiten:

```bash
codex exec --json "summarize the repo structure" | jq

Wenn du `--json` aktivierst, wird `stdout` zu einem Stream im Format JSON Lines (JSONL). So kannst du jedes Ereignis erfassen, das Codex während der Ausführung ausgibt. Zu den Ereignistypen gehören `thread.started`, `turn.started`, `turn.completed`, `turn.failed`, `item.*` und `error`.

Zu den Elementtypen zählen Agentennachrichten, Überlegungen, Befehlsausführungen, Dateiänderungen, MCP-Tool-Aufrufe, Websuchen und Planaktualisierungen.

Beispiel für einen JSON-Stream, bei dem jede Zeile ein JSON-Objekt ist:

```jsonl
{"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122,"reasoning_output_tokens":0}}

Wenn du nur die abschließende Nachricht benötigst, schreibe sie mit `-o <path>`/`--output-last-message <path>` in eine Datei. Dadurch wird die abschließende Nachricht in die Datei geschrieben und weiterhin über `stdout` ausgegeben. Details findest du unter [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec).

## Strukturierte Ausgaben mit einem Schema erstellen

Wenn du für nachgelagerte Schritte strukturierte Daten benötigst, fordere mit `--output-schema` eine abschließende Antwort an, die einem JSON-Schema entspricht.
Das ist bei automatisierten Arbeitsabläufen hilfreich, die fest definierte Felder benötigen, zum Beispiel für Job-Zusammenfassungen, Risikoberichte oder Release-Metadaten.

`schema.json`

```json
{
  "type": "object",
  "properties": {
    "project_name": { "type": "string" },
    "programming_languages": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["project_name", "programming_languages"],
  "additionalProperties": false
}

Führe Codex mit dem Schema aus und speichere die abschließende JSON-Antwort auf dem Datenträger:

```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json

Beispiel für die abschließende Ausgabe (stdout):

```json
{
  "project_name": "Codex CLI",
  "programming_languages": ["Rust", "TypeScript", "Shell"]
}

## Authentifizierung in Automatisierungen

`codex exec` greift standardmäßig auf die gespeicherte CLI-Authentifizierung zurück. In CI werden Anmeldedaten üblicherweise explizit bereitgestellt:

Wenn deine vertrauenswürdige Cloud- oder CI-Laufzeitumgebung bereits kurzlebige
Workload-Token erhält, nutze
[Identitätsföderation für Workloads](/de-DE/codex/enterprise/workload-identity),
statt OpenAI-Anmeldedaten zu speichern.

### Authentifizierung per API-Schlüssel verwenden

Verwende für GitHub Actions die [Codex GitHub Action](/de-DE/codex/github-action), statt die CLI selbst zu installieren und zu authentifizieren. Die Action verringert das Risiko einer Offenlegung von API-Schlüsseln, indem sie Codex installiert, einen Proxy für die Responses API startet und Codex mit einer konfigurierbaren Sicherheitsstrategie ausführt.

Setze in Arbeitsabläufen, die Code aus dem Repository auschecken oder ausführen, weder `OPENAI_API_KEY` noch `CODEX_API_KEY` als Umgebungsvariable auf Jobebene. Build-Skripte, Tests, Lifecycle-Hooks von Abhängigkeiten oder eine kompromittierte Action im selben Job können diese Umgebungsvariablen auslesen.

Setze `CODEX_API_KEY` in anderen Automatisierungsumgebungen nur für den Codex-Aufruf,
der diesen Schlüssel benötigt. Stelle sicher, dass in derselben Prozessumgebung
kein nicht vertrauenswürdiger Code ausgeführt wird.

Wenn du für eine einzelne Ausführung einen anderen API-Schlüssel verwenden möchtest, setze `CODEX_API_KEY` direkt im Aufruf:

```bash
CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"

`CODEX_API_KEY` kannst du mit `codex exec`, `codex review`,
dem TypeScript-SDK und `codex exec-server --remote` verwenden.

Lies diesen Abschnitt, wenn du CI/CD-Jobs mit einem Codex-Benutzerkonto statt mit einem
API-Schlüssel ausführen musst. Das ist zum Beispiel der Fall, wenn Teams in Unternehmen auf vertrauenswürdigen
Runnern den von ChatGPT verwalteten Codex-Zugriff verwenden oder wenn du statt eines API-Schlüssels die Ratenlimits von ChatGPT/Codex benötigst.

API-Schlüssel sind für Automatisierungen die richtige Standardwahl, da sie sich einfacher
bereitstellen und rotieren lassen. Verwende diesen Ansatz nur, wenn du Codex ausdrücklich über
dein Codex-Konto ausführen musst.

Behandle `~/.codex/auth.json` wie ein Passwort: Die Datei enthält Zugriffstoken. Nimm sie nicht
in einen Commit auf, füge sie nicht in Tickets ein und teile sie nicht im Chat.

Verwende diesen Ablauf nicht für öffentliche Repositorys oder Open-Source-Repositorys. Wenn `codex login`
auf dem Runner nicht möglich ist, stelle `auth.json` über einen sicheren Speicher bereit. Führe
Codex auf dem Runner aus, damit Codex die Datei direkt aktualisiert, und bewahre die aktualisierte Datei
zwischen den Ausführungen auf.

Siehe [Authentifizierung des Codex-Kontos in CI/CD aufrechterhalten (fortgeschritten)](/codex/auth/ci-cd-auth).

## Nicht interaktive Sitzung fortsetzen

Wenn du eine vorherige Ausführung fortsetzen musst, zum Beispiel in einer zweistufigen Pipeline, verwende den Unterbefehl `resume`:

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"

Mit `codex exec resume <SESSION_ID>` kannst du auch eine bestimmte Sitzungs-ID angeben.

## Git-Repository erforderlich

Um destruktive Änderungen zu verhindern, lässt Codex die Ausführung von Befehlen nur innerhalb eines Git-Repositorys zu. Wenn du sicher bist, dass die Umgebung unbedenklich ist, kannst du diese Prüfung mit `codex exec --skip-git-repo-check` überspringen.

## Gängige Automatisierungsmuster

### Beispiel: CI-Fehler in GitHub Actions automatisch beheben

Verwende für Arbeitsabläufe in GitHub Actions [`openai/codex-action`](https://github.com/openai/codex-action), statt Codex zu installieren und den API-Schlüssel an einen Shell-Schritt zu übergeben. Die Action startet einen sicheren Proxy für den OpenAI-API-Schlüssel.

Codex kann automatisch Korrekturen vorschlagen, wenn ein CI-Ablauf fehlschlägt. Gehe dabei wie folgt vor:

1. Löse einen Folgeablauf aus, wenn dein primärer CI-Ablauf mit einem Fehler endet.
2. Checke den Commit aus, bei dem der Fehler aufgetreten ist, und verwende dabei ausschließlich Leseberechtigungen für das Repository.
3. Führe die Setup-Befehle vor Codex aus, ohne deinen OpenAI-API-Schlüssel für diese Schritte offenzulegen.
4. Führe die Codex GitHub Action aus.
5. Speichere die lokalen Änderungen von Codex als Patch-Artefakt.
6. Wende in einem separaten Job den Patch an und öffne einen Pull Request.

Der folgende Codex-Job verfügt nur über `contents: read`. Nachdem Codex ausgeführt wurde, serialisiert der Job lediglich den Diff als Artefakt. Der Job `open_pr` erhält Schreibberechtigungen für das Repository, aber nicht `OPENAI_API_KEY`.

Das Beispiel setzt ein Node.js-Projekt voraus. Passe die Setup- und Testbefehle an deinen Stack an.

Eine ausführlichere Sicherheitscheckliste findest du im [Sicherheitsleitfaden zur Codex GitHub Action](https://github.com/openai/codex-action/blob/main/docs/security.md).

```yaml
name: Codex auto-fix on CI failure

on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

jobs:
  generate_fix:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      has_patch: ${{ steps.diff.outputs.has_patch }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0
          persist-credentials: false

      - uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install dependencies
        run: |
          if [ -f package-lock.json ]; then npm ci; fi

      - name: Run Codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt: |
            The CI workflow "${{ github.event.workflow_run.name }}" failed for commit
            ${{ github.event.workflow_run.head_sha }}.

            Run `npm test --silent` to reproduce the failure. Identify the minimal
            change needed to make the tests pass, implement only that change, and
            run `npm test --silent` again.

            Do not refactor unrelated files.

      - name: Create patch artifact
        id: diff
        run: |
          git add -N .
          git diff --binary HEAD > codex.patch
          if [ -s codex.patch ]; then
            echo "has_patch=true" >> "$GITHUB_OUTPUT"
          else
            echo "has_patch=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload patch artifact
        if: steps.diff.outputs.has_patch == 'true'
        uses: actions/upload-artifact@v4
        with:
          name: codex-fix-patch
          path: codex.patch
          if-no-files-found: error

  open_pr:
    runs-on: ubuntu-latest
    needs: generate_fix
    if: needs.generate_fix.outputs.has_patch == 'true'
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0

      - uses: actions/download-artifact@v4
        with:
          name: codex-fix-patch

      - name: Apply Codex patch
        run: git apply --index codex.patch

      - name: Open pull request
        env:
          GH_TOKEN: ${{ github.token }}
          FAILED_HEAD_BRANCH: ${{ github.event.workflow_run.head_branch }}
          FAILED_HEAD_SHA: ${{ github.event.workflow_run.head_sha }}
          RUN_ID: ${{ github.event.workflow_run.run_id }}
        run: |
          branch="codex/auto-fix-$RUN_ID"

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git switch -c "$branch"
          git commit -m "Auto-fix failing CI via Codex"
          git push origin "$branch"

          {
            echo "Codex generated this patch after CI failed for \`$FAILED_HEAD_SHA\`."
            echo
            echo "Review the changes before merging."
          } > pr-body.md

          gh pr create \
            --base "$FAILED_HEAD_BRANCH" \
            --head "$branch" \
            --title "Auto-fix failing CI via Codex" \
            --body-file pr-body.md

## stdin-Weiterleitung für Fortgeschrittene

Wenn ein anderer Befehl Eingaben für Codex erzeugt, wähle je nachdem, woher die Anweisung stammen soll, das passende stdin-Muster. Verwende Prompt-plus-stdin, wenn du die Anweisung bereits kennst und die per Pipe weitergeleitete Ausgabe als Kontext übergeben möchtest. Verwende `codex exec -`, wenn stdin den vollständigen Prompt bilden soll.

### Prompt-plus-stdin verwenden

Prompt-plus-stdin eignet sich, wenn ein anderer Befehl bereits die Daten erzeugt, die Codex untersuchen soll. In diesem Modus formulierst du die Anweisung selbst und leitest die Ausgabe per Pipe als Kontext weiter. Das passt gut zu CLI-Arbeitsabläufen, die auf Befehlsausgaben, Protokollen und generierten Daten basieren.

```bash
npm test 2>&1 \
  | codex exec "summarize the failing tests and propose the smallest likely fix" \
  | tee test-summary.md

### Protokolle zusammenfassen

```bash
tail -n 200 app.log \
  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
  > log-triage.md

### TLS- oder HTTP-Probleme untersuchen

```bash
curl -vv https://api.example.com/health 2>&1 \
  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
  > tls-debug.md

### Ein Update für Slack vorbereiten

```bash
gh run view 123456 --log \
  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
  | pbcopy

### Aus CI-Protokollen einen Kommentar für einen Pull Request entwerfen

```bash
gh run view 123456 --log \
  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
  | gh pr comment 789 --body-file -

### Verwende `codex exec -`, wenn stdin der Prompt ist

Wenn du das Prompt-Argument weglässt, liest Codex den Prompt von stdin ein. Verwende `codex exec -`, wenn du dieses Verhalten ausdrücklich erzwingen möchtest.

Der Marker `-` ist nützlich, wenn ein anderer Befehl oder ein Skript den gesamten Prompt dynamisch erzeugt. Das eignet sich, wenn du Prompts in Dateien speicherst, sie mit Shell-Skripten zusammensetzt oder aktuelle Befehlsausgaben mit Anweisungen kombinierst, bevor du den gesamten Prompt an Codex übergibst.

```bash
cat prompt.txt | codex exec -

```bash
printf "Summarize this error log in 3 bullets:\n\n%s\n" "$(tail -n 200 app.log)" \
  | codex exec -

```bash
generate_prompt.sh | codex exec - --json > result.jsonl
