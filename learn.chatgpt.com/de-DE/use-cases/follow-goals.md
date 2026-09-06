<!-- source: https://learn.chatgpt.com/de-DE/use-cases/follow-goals -->

## Einführung

Verwende `/goal`, wenn Codex nicht nach einer einzigen normalen Interaktion aufhören, sondern kontinuierlich auf ein dauerhaftes Ziel hinarbeiten soll. Das eignet sich für Aufgaben mit einem klaren Ziel, einer Validierungsschleife und genügend Spielraum, damit Codex Fortschritte erzielen kann, ohne dass du jeden Schritt vorgeben musst. Mit `/goal` kann Codex mehrere Stunden lang selbstständig arbeiten, ohne dass du eingreifen musst.

Lege mit `/goal <objective>` ein Ziel fest, prüfe mit `/goal` das aktuelle Ziel und verwende `/goal pause`, `/goal resume` oder `/goal clear`, um die Ausführung bei Bedarf zu steuern.

Wenn `/goal` nicht in der Liste der Slash-Befehle angezeigt wird, aktiviere `features.goals`
in `config.toml`:

```toml
[features]
goals = true

Du kannst auch `codex features enable goals` über die CLI ausführen oder Codex bitten, den Befehl auszuführen.

## Die passende Aufgabe auswählen

Ein gutes Ziel geht über einen einzelnen Prompt hinaus, ist aber überschaubarer als ein Backlog ohne klaren Abschluss. Es sollte festlegen, was Codex erreichen soll, was unverändert bleiben muss, wie der Fortschritt überprüft wird und wann Codex aufhören soll.

Dafür eignen sich:

- Code-Migrationen mit klar definiertem Ziel-Stack, eindeutigen Paritätsprüfungen und klaren Einschränkungen
- umfangreiche Refactorings, bei denen Codex nach jeder Etappe Tests ausführen kann
- Experimente, Spiele oder Prototypen, bei denen Codex ein funktionsfähiges Artefakt kontinuierlich verbessern kann

Verwende kein Ziel für eine lose Sammlung voneinander unabhängiger Aufgaben.

## Die Schleife einrichten

1. Benenne ein Ziel und eine Endbedingung.
2. Zeige Codex, welche Dateien, welche Dokumentation, welches Issue, welche Protokolle oder welchen Plan es zuerst lesen muss.
3. Lege die Befehle oder Artefakte fest, mit denen sich der Fortschritt nachweisen lässt.
4. Weise Codex an, in Etappen zu arbeiten und ein kurzes Fortschrittsprotokoll zu führen.
5. Prüfe mit `/goal` während der Ausführung den Status.
6. Pausiere das Ziel, setze es fort oder lösche es, wenn die Ausführung abgeschlossen oder blockiert ist oder sich die Richtung ändert.

Entscheidend ist die klare Zielvereinbarung. Codex sollte vor Beginn wissen, was „fertig“ bedeutet. Bei einer Migration kann „fertig“ bedeuten, dass der neue Pfad die Contract-Tests besteht und für den bisherigen Pfad weiterhin ein Rollback möglich ist. Bei einem Spiel oder Prototyp kann „fertig“ bedeuten, dass sich die App erstellen und starten lässt und der bereitgestellten Referenz oder dem erwarteten Verhalten entspricht.

  Bitte Codex um Hilfe: Sprich zunächst darüber, was du
entwickeln möchtest, und bitte Codex dann, direkt ein Ziel festzulegen und mit der Arbeit zu beginnen.

## Codex selbstständig arbeiten lassen

Während Codex ein Ziel verfolgt, bitte um kompakte Fortschrittsberichte, die die Ausführung leichter nachvollziehbar machen. Eine hilfreiche Statusmeldung nennt die aktuelle Etappe, was überprüft wurde, was noch aussteht und ob Codex blockiert ist.
Wenn der Status unklar wird, grenze das Ziel enger ein, statt weitere einmalige Anweisungen hinzuzufügen. Teile Codex genau mit, welche Etappe als Nächstes wichtig ist, welcher Befehl ihren Abschluss nachweist und wann Codex pausieren soll.

Wenn Codex ein Ziel verfolgt, kann es viele Stunden lang selbstständig arbeiten, ohne dass du nachsehen musst. Codex beendet die Ausführung, sobald es sicher ist, die Endbedingung erreicht zu haben. Betrachte `/goal` daher als Hintergrundaufgabe, die du nicht überwachen musst.

## Beispielziele

### Migrationen

Mit `/goal` kannst du Codex die Migration durchführen lassen, egal ob du Spiele auf einen neuen Stack, mobile Apps auf eine neue Plattform oder eine Codebasis auf ein neues Framework migrierst:

### Prototypen erstellen

Ganz gleich, ob du von Grund auf eine neue App, ein neues Spiel oder eine neue Funktion entwickelst: Mit `/goal` kannst du Codex eine ausgereifte erste Version fertigstellen lassen. Mithilfe einer PLAN.md-Datei kannst du genau beschreiben, was du entwickeln möchtest, und so die Erstellung der ersten Version anleiten.

### Prompt-Optimierung

Wenn du über eine Eval-Suite verfügst, kannst du mit `/goal` Prompts anhand der Eval-Ergebnisse optimieren. Codex kann fehlgeschlagene Fälle untersuchen, den Prompt aktualisieren, die Evals erneut ausführen und die Optimierung fortsetzen, bis sich der Score verbessert oder deine Endbedingung erreicht ist.
