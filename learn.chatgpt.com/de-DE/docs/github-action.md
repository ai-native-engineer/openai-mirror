<!-- source: https://learn.chatgpt.com/de-DE/docs/github-action -->

Verwende die Codex GitHub Action (`openai/codex-action@v1`), um Codex in CI/CD-Jobs auszuführen, Patches anzuwenden oder Reviews aus einem Workflow von GitHub Actions zu veröffentlichen.
Die Action installiert die Codex CLI, startet den Proxy für die Responses API, wenn du einen API-Schlüssel angibst, und führt `codex exec` mit den von dir festgelegten Berechtigungen aus.

Verwende die Action für folgende Aufgaben:

- Codex-Feedback zu Pull Requests oder Versionen automatisieren, ohne die CLI selbst verwalten zu müssen.
- Änderungen in deiner CI-Pipeline nur zulassen, wenn sie Codex-gestützte Qualitätsprüfungen bestehen.
- Reproduzierbare Codex-Aufgaben (Codeprüfung, Vorbereitung von Versionen und Migrationen) aus einer Workflow-Datei ausführen.

Ein CI-Beispiel findest du unter [Nicht interaktiver Modus](/de-DE/codex/non-interactive-mode). Den Quellcode kannst du im [Repository openai/codex-action](https://github.com/openai/codex-action) ansehen.

## Voraussetzungen

- Speichere deinen OpenAI-Schlüssel als GitHub-Secret (zum Beispiel `OPENAI_API_KEY`) und verweise im Workflow darauf.
- Führe den Job auf einem Linux- oder macOS-Runner aus. Lege für Windows `safety-strategy: unsafe` fest.
- Checke deinen Code aus, bevor du die Action aufrufst, damit Codex den Inhalt des Repositorys lesen kann.
- Lege fest, welche Prompts du ausführen möchtest. Du kannst Inline-Text über `prompt` bereitstellen oder mit `prompt-file` auf eine in das Repository eingecheckte Datei verweisen.

## Beispiel-Workflow

Der folgende Beispiel-Workflow prüft neue Pull Requests, erfasst die Antwort von Codex und veröffentlicht sie anschließend im PR.

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge
          fetch-depth: 0
          persist-credentials: false

      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    permissions:
      issues: write
      pull-requests: write
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}

Ersetze `.github/codex/prompts/review.md` durch deine eigene Prompt-Datei oder verwende die Eingabe `prompt` für Inline-Text. Das Beispiel schreibt außerdem die letzte Codex-Nachricht in `codex-output.md`, damit du sie später prüfen oder als Artefakt hochladen kannst.

## `codex exec` konfigurieren

Passe die Ausführung von Codex an, indem du die Action-Eingaben für die entsprechenden Optionen von `codex exec` festlegst:

- `prompt` oder `prompt-file` (wähle eine Option): Inline-Anweisungen oder ein Pfad im Repository zu einer Markdown- oder Textdatei mit deiner Aufgabe. Es empfiehlt sich, Prompts unter `.github/codex/prompts/` zu speichern.
- `codex-args`: Zusätzliche CLI-Flags. Gib ein JSON-Array (zum Beispiel `["--ephemeral"]`) oder einen Shell-String (`--profile ci`) an, um Sitzungen, Profile oder MCP-Einstellungen zu konfigurieren.
- `model` und `effort`: Wähle die gewünschte Konfiguration des Codex-Agenten aus. Lass die Felder leer, um die Standardwerte zu verwenden.
- `sandbox`: Stimme den Sandbox-Modus (`workspace-write`, `read-only`, `danger-full-access`) auf die Berechtigungen ab, die Codex während der Ausführung benötigt.
- `output-file`: Speichere die letzte Codex-Nachricht lokal, damit nachfolgende Schritte sie hochladen oder einen Diff davon erstellen können.
- `codex-version`: Lege eine bestimmte CLI-Version fest. Lass das Feld leer, um die neueste veröffentlichte Version zu verwenden.
- `codex-home`: Gib ein gemeinsames Codex-Home-Verzeichnis an, wenn du Konfigurationsdateien oder MCP-Setups in mehreren Schritten wiederverwenden möchtest.

## Berechtigungen verwalten

Codex hat auf von GitHub gehosteten Runnern umfassenden Zugriff, sofern du ihn nicht einschränkst. Nutze die folgenden Eingaben, um den Zugriff zu steuern:

- `safety-strategy` (Standard: `drop-sudo`) entfernt `sudo`, bevor Codex ausgeführt wird. Das lässt sich innerhalb des Jobs nicht rückgängig machen und schützt Secrets im Arbeitsspeicher. Unter Windows musst du `safety-strategy: unsafe` festlegen.
- `unprivileged-user` kombiniert `safety-strategy: unprivileged-user` mit `codex-user`, damit Codex unter einem bestimmten Konto ausgeführt wird. Stelle sicher, dass das Konto Lese- und Schreibzugriff auf den Repository-Checkout hat. Wie du die Besitzrechte korrigierst, erfährst du im [Beispiel für `unprivileged-user`](https://github.com/openai/codex-action/blob/main/examples/unprivileged-user.yml).
- `read-only` verhindert, dass Codex Dateien ändert oder das Netzwerk nutzt. Codex wird dabei jedoch weiterhin mit erhöhten Berechtigungen ausgeführt. Verlasse dich zum Schutz von Secrets nicht allein auf `read-only`.
- `sandbox` schränkt den Datei- und Netzwerkzugriff innerhalb von Codex selbst ein. Wähle die restriktivste Option, mit der Codex die Aufgabe noch abschließen kann.
- `allow-users` und `allow-bots` legen fest, wer den Workflow auslösen darf. Standardmäßig können nur Konten mit Schreibzugriff die Action ausführen. Gib weitere vertrauenswürdige Konten ausdrücklich an oder lass das Feld leer, um das Standardverhalten beizubehalten.

## Ausgaben erfassen

Die Action stellt die letzte Codex-Nachricht über die Ausgabe `final-message` bereit. Ordne sie einer Job-Ausgabe zu (wie oben gezeigt) oder verarbeite sie direkt in späteren Schritten. Kombiniere `output-file` mit der Funktion zum Hochladen von Artefakten, wenn du stattdessen das vollständige Transkript vom Runner sichern möchtest. Wenn du strukturierte Daten benötigst, übergib `--output-schema` über `codex-args`, um eine JSON-Struktur zu erzwingen.

## Sicherheitscheckliste

- Beschränke, wer den Workflow starten darf. Nutze bevorzugt vertrauenswürdige Ereignisse oder ausdrückliche Genehmigungen, statt allen zu erlauben, Codex für dein Repository auszuführen.
- Bereinige Prompt-Eingaben aus Pull Requests, Commit-Nachrichten oder Issue-Beschreibungen, um Prompt Injection zu vermeiden. Prüfe HTML-Kommentare oder verborgenen Text, bevor du diese Inhalte an Codex übergibst.
- Schütze deinen `OPENAI_API_KEY`, indem du `safety-strategy` auf `drop-sudo` eingestellt lässt oder Codex unter einem Konto ohne erhöhte Berechtigungen ausführst. Lass die Action auf Multi-Tenant-Runnern niemals im Modus `unsafe`.
- Führe Codex als letzten Schritt eines Jobs aus, damit keine nachfolgenden Schritte unerwartete Zustandsänderungen übernehmen.
- Wechsle Schlüssel sofort aus, wenn du vermutest, dass Proxy-Protokolle oder die Ausgabe der Action vertrauliche Daten offengelegt haben.

## Fehlerbehebung

- **Du hast sowohl prompt als auch prompt-file festgelegt**: Entferne die doppelte Eingabe, sodass du genau eine Quelle angibst.
- **responses-api-proxy hat keine Serverinformationen geschrieben**: Prüfe, ob der API-Schlüssel vorhanden und gültig ist. Der Proxy startet nur, wenn du `openai-api-key` angibst.
- **Das Entfernen von `sudo` war vorgesehen, aber `sudo` wurde erfolgreich ausgeführt**: Stelle sicher, dass kein vorheriger Schritt `sudo` wiederhergestellt hat und dass das Betriebssystem des Runners Linux oder macOS ist. Wiederhole die Ausführung mit einem neuen Job.
- **Berechtigungsfehler nach `drop-sudo`**: Gewähre Schreibzugriff, bevor die Action ausgeführt wird (zum Beispiel mit `chmod -R g+rwX "$GITHUB_WORKSPACE"` oder indem du das Muster unprivileged-user verwendest).
- **Nicht autorisierter Workflow-Start wurde blockiert**: Passe die Eingaben `allow-users` oder `allow-bots` an, wenn du neben den standardmäßig zugelassenen Mitwirkenden mit Schreibzugriff weitere Dienstkonten zulassen möchtest.
