<!-- source: https://learn.chatgpt.com/de-DE/use-cases/github-code-reviews -->

## So verwendest du Codex

Füge Codex Code Review zunächst deiner GitHub-Organisation oder deinem Repository hinzu.
Weitere Informationen findest du unter [Codex Code Review in GitHub](/de-DE/codex/third-party/github).

Du kannst Codex so einrichten, dass jeder Pull Request automatisch überprüft wird. Alternativ kannst du mit `@codex review` in einem Kommentar zum Pull Request ein Review anfordern.

Wenn Codex eine Regression oder ein potenzielles Problem meldet, kannst du Codex in einem Kommentar zum Pull Request bitten, das Problem zu beheben. Verwende dazu einen Folge-Prompt wie `@codex fix it`.

Dadurch startet ein neuer Cloud-Chat, der das Problem behebt und den Pull Request aktualisiert.

## Vorgaben für Reviews festlegen

Um festzulegen, was Codex überprüft, füge den Abschnitt `## Code Review Rules` der
`AGENTS.md` hinzu, die dem Code am nächsten liegt, auf den sich die Regeln beziehen. Beispiel:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Lege Regeln für das gesamte Repository in der `AGENTS.md` im Stammverzeichnis und Regeln für einzelne Services
in einer Datei in einem Unterverzeichnis ab. Formuliere die Regeln knapp. Beschreibe das zu meldende Verhalten und jede
sichere Vorgehensweise oder Ausnahme. Überlasse Formatierungs- und Lint-Prüfungen der CI. Unter
[Anpassen, was Codex überprüft](/de-DE/codex/third-party/github#customize-what-codex-reviews)
findest du Hinweise zum Setup und zum Formulieren von Regeln.
