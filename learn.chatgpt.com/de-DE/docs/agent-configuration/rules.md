<!-- source: https://learn.chatgpt.com/de-DE/docs/agent-configuration/rules -->

Mit Regeln legst du fest, welche Befehle Codex außerhalb der Sandbox ausführen darf.

Regeln sind experimentell und können sich ändern.

## Regeldatei erstellen

1. Erstelle eine Datei mit der Endung `.rules` im Ordner `rules/` neben einer aktiven Konfigurationsebene (zum Beispiel `~/.codex/rules/default.rules`).
2. Füge eine Regel hinzu. In diesem Beispiel fragt Codex nach, bevor `gh pr view` außerhalb der Sandbox ausgeführt werden darf.

   ```python
   # Prompt before running commands with the prefix `gh pr view` outside the sandbox.
   prefix_rule(
       # The prefix to match.
       pattern = ["gh", "pr", "view"],

       # The action to take when Codex requests to run a matching command.
       decision = "prompt",

       # Optional rationale for why this rule exists.
       justification = "Viewing PRs is allowed with approval",

       # `match` and `not_match` are optional "inline unit tests" where you can
       # provide examples of commands that should (or should not) match this rule.
       match = [
           "gh pr view 7888",
           "gh pr view --repo openai/codex",
           "gh pr view 7888 --json title,body,comments",
       ],
       not_match = [
           # Does not match because the `pattern` must be an exact prefix.
           "gh pr --repo openai/codex view 7888",
       ],
   )

3. Starte Codex neu.

Beim Start durchsucht Codex in jeder aktiven Konfigurationsebene den Ordner `rules/`, einschließlich der Speicherorte für die [Teamkonfiguration](/de-DE/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config) und der Benutzerebene unter `~/.codex/rules/`. Projektlokale Regeln unter `<repo>/.codex/rules/` werden nur geladen, wenn die Projektebene `.codex/` als vertrauenswürdig gilt.

Wenn du in der TUI einen Befehl zur Zulassungsliste hinzufügst, speichert Codex die Regel in der Benutzerebene unter `~/.codex/rules/default.rules`, damit bei künftigen Ausführungen keine Abfrage mehr nötig ist.

Wenn intelligente Genehmigungen aktiviert sind (Standardeinstellung), kann Codex dir bei Eskalationsanfragen eine
`prefix_rule` vorschlagen. Prüfe das vorgeschlagene Präfix
sorgfältig, bevor du es akzeptierst.

Personen mit Adminrechten können auch restriktive Einträge für `prefix_rule` aus
[`requirements.toml`](/de-DE/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml) erzwingen.

## Regelfelder verstehen

`prefix_rule()` unterstützt folgende Felder:

- `pattern` **(erforderlich)**: Eine nicht leere Liste, die das Befehlspräfix für den Abgleich festlegt. Jedes Element hat eine der folgenden Formen:
  - Eine literale Zeichenfolge (zum Beispiel `"pr"`).
  - Eine Vereinigung aus Literalen (zum Beispiel `["view", "list"]`), mit der Alternativen an dieser Argumentposition abgeglichen werden.
- `decision` **(standardmäßig `"allow"`)**: Die Aktion, die bei Übereinstimmung der Regel ausgeführt wird. Bei mehreren übereinstimmenden Regeln wendet Codex die restriktivste Entscheidung an (`forbidden` \> `prompt` \> `allow`).
  - `allow`: Der Befehl wird ohne Rückfrage außerhalb der Sandbox ausgeführt.
  - `prompt`: Vor jedem übereinstimmenden Aufruf wird nachgefragt.
  - `forbidden`: Die Anfrage wird ohne Rückfrage blockiert.
- `justification` **(optional)**: Eine nicht leere, verständliche Begründung für die Regel. Codex kann sie in Genehmigungsabfragen oder Ablehnungsmeldungen anzeigen. Wenn du `forbidden` verwendest, gib in der Begründung nach Möglichkeit eine empfohlene Alternative an (zum Beispiel `"Use \`rg\` anstelle von \`grep\`."\`).
- `match` und `not_match` **(standardmäßig `[]`)**: Beispiele, die Codex beim Laden deiner Regeln validiert. Damit kannst du Fehler erkennen, bevor eine Regel wirksam wird.

Vor einer möglichen Ausführung vergleicht Codex die Argumentliste des Befehls mit `pattern`. Intern behandelt Codex den Befehl als Argumentliste, wie sie auch `execvp(3)` erhält.

## Shell-Wrapper und zusammengesetzte Befehle

Einige Tools fassen mehrere Shell-Befehle zu einem einzigen Aufruf zusammen, zum Beispiel:

```text
["bash", "-lc", "git add . && rm -rf /"]

Da solche Befehle mehrere Aktionen in einer einzigen Zeichenfolge verbergen können, behandelt Codex `bash -lc`, `bash -c` sowie die entsprechenden Varianten für `zsh` / `sh` gesondert.

### Wenn Codex das Skript sicher aufteilen kann

Wenn das Shell-Skript eine lineare Befehlskette ist und nur folgende Konstrukte verwendet:

- einfache Wörter (ohne Variablenexpansion und ohne `VAR=...`, `$FOO`, `*` usw.)
- Verknüpfungen mit sicheren Operatoren (`&&`, `||`, `;` oder `|`)

parst Codex das Skript dann mithilfe von tree-sitter und teilt es in einzelne Befehle auf, bevor es deine Regeln anwendet.

Das obige Skript wird als zwei separate Befehle behandelt:

- `["git", "add", "."]`
- `["rm", "-rf", "/"]`

Anschließend wertet Codex jeden Befehl anhand deiner Regeln aus. Dabei hat das restriktivste Ergebnis Vorrang.

Selbst wenn du `pattern=["git", "add"]` zulässt, lässt Codex `git add . && rm -rf /` nicht automatisch zu, da der Teil `rm -rf /` separat ausgewertet wird und die automatische Zulassung des gesamten Aufrufs verhindert.

So wird verhindert, dass gefährliche Befehle zusammen mit sicheren eingeschleust werden.

### Wenn Codex das Skript nicht aufteilt

Wenn das Skript erweiterte Shell-Funktionen verwendet, zum Beispiel:

- Umleitungen (`>`, `>>`, `<`)
- Substitutionen (`$(...)`, `...`)
- Umgebungsvariablen (`FOO=bar`)
- Platzhaltermuster (`*`, `?`)
- Kontrollfluss (`if`, `for`, `&&` mit Zuweisungen usw.)

versucht Codex nicht, das Skript zu interpretieren oder aufzuteilen.

In diesen Fällen wird der gesamte Aufruf wie folgt behandelt:

```text
["bash", "-lc", "<full script>"]

und deine Regeln werden auf diesen **einzelnen** Aufruf angewendet.

Bei dieser Vorgehensweise wertet Codex jeden Befehl einzeln aus, wenn das sicher möglich ist, und verhält sich andernfalls konservativ.

## Regeldatei testen

Mit `codex execpolicy check` kannst du testen, wie deine Regeln auf einen Befehl angewendet werden:

```shell
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888 --json title,body,comments

Der Befehl gibt JSON mit der restriktivsten Entscheidung und allen übereinstimmenden Regeln aus, einschließlich aller Werte für `justification` aus den betreffenden Regeln. Verwende `--rules` mehrmals, um Dateien zu kombinieren, und füge `--pretty` hinzu, um die Ausgabe zu formatieren.

## Regelsprache verstehen

Für Dateien im Format `.rules` wird `Starlark` verwendet (siehe die [Sprachspezifikation](https://github.com/bazelbuild/starlark/blob/master/spec.md)). Die Syntax ähnelt Python, ist aber auf eine sichere Ausführung ausgelegt: Die Regel-Engine kann sie ohne Nebeneffekte ausführen (zum Beispiel ohne Änderungen am Dateisystem vorzunehmen).
