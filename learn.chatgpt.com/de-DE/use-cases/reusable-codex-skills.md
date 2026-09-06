<!-- source: https://learn.chatgpt.com/de-DE/use-cases/reusable-codex-skills -->

## Einen Skill erstellen, auf den Codex jederzeit zurückgreifen kann

Mit Skills kannst du Codex wiederverwendbare Anweisungen, Ressourcen und Skripte für Aufgaben bereitstellen, die du regelmäßig ausführst. Ein [Skill](/de-DE/codex/build-skills) kann festhalten, was sich beim ersten Einsatz von Codex als nützlich erwiesen hat: die Aufgabe, die Dokumentation, den Befehl oder das Beispiel.

Beginne mit einem gelungenen Beispiel: einem Codex-Chat, in dem Codex einen PR per Cherry-Pick übernommen hat, einer Release-Checkliste aus Notion, einer Sammlung hilfreicher PR-Kommentare oder einem Slack-Thread, der einen Launch-Prozess erklärt.

## Verwendung

1. Füge den Kontext hinzu, den Codex verwenden soll.

   Bleibe in dem Codex-Chat, den du festhalten möchtest, und füge den Slack-Thread oder den Link zur Dokumentation ein. Ergänze außerdem, was Codex künftig berücksichtigen soll: eine Regel, einen Befehl oder ein Beispiel.

2. Führe den Starter-Prompt aus.

   Im Prompt benennst du den gewünschten Skill. Anschließend übergibst du `$skill-creator` die Aufgabe, die Dokumentation, den PR, den Befehl oder die Ausgabe, die festgehalten werden soll.

3. Lass Codex den Skill erstellen und validieren.

   Das Ergebnis sollte den `$skill-name` definieren, beschreiben, wann der Skill ausgelöst werden soll, und wiederverwendbare Anweisungen an der richtigen Stelle ablegen.

   Skills in `~/.codex/skills` stehen dir in jedem Repository zur Verfügung. Skills im aktuellen Repository kannst du committen, damit auch andere in deinem Team sie nutzen können.

4. Verwende den Skill und aktualisiere ihn anschließend direkt im Chat.

   Setze den neuen `$skill-name` bei der nächsten Aufgabe ein, etwa für einen PR, eine Warnmeldung, ein Review, einen Release-Hinweis oder eine Designaufgabe. Wenn er den falschen Testbefehl verwendet, eine Review-Regel übersieht, einen Runbook-Schritt auslässt oder einen Entwurf verfasst, den du nicht versenden würdest, bitte Codex, diese Korrektur in den Skill aufzunehmen.

## Quellmaterial bereitstellen

Stelle `$skill-creator` das Material bereit, aus dem hervorgeht, wie der Skill funktionieren soll.

| Was du hast                                              | Was du hinzufügen solltest                                                                                                                                                             |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ein Arbeitsablauf aus einem Codex-Chat, den du festhalten möchtest** | Bleibe in diesem Chat und sage `use this chat`. Codex kann den Chat-Kontext, die Befehle, Änderungen und Rückmeldungen als Ausgangspunkt verwenden.                                         |
| **Dokumentation oder ein Runbook**                                      | Füge die Release-Checkliste ein, verlinke das Runbook für die Reaktion auf Vorfälle, hänge das API-PDF an oder verweise Codex auf den Markdown-Leitfaden in deinem Repository.                                 |
| **Gespräch im Team**                                      | Füge den Slack-Thread ein, in dem jemand eine Warnmeldung erklärt hat, verlinke das PR-Review mit den Frontend-Regeln oder hänge das Support-Gespräch an, in dem das Problem auf Kundenseite erläutert wird. |
| **Skripte oder Befehle, die der Skill wiederverwenden soll**             | Gib die Befehle und Skripte an, die Codex bei künftigen Aufgaben ausführen soll: den Testbefehl, den Vorschaubefehl, das Release-Skript, das Skript zum Abrufen von Logs oder einen lokalen Hilfsbefehl.                                    |
| **Ein gutes Ergebnis**                                          | Füge als Vorlage für künftige Aufgaben den zusammengeführten PR, den endgültigen Eintrag im Änderungsprotokoll, den freigegebenen Launch-Hinweis, das gelöste Ticket, den Vorher-nachher-Screenshot oder die endgültige Codex-Antwort hinzu.         |

Wenn sich die Quelle in Slack, Linear, GitHub, Notion oder Sentry befindet, verbinde das jeweilige Tool über ein [Plug-in](/de-DE/codex/plugins) mit Codex, erwähne es im Starter-Prompt oder füge den relevanten Teil in den Chat ein.

## Was Codex erstellt

Die meisten Skills bestehen zunächst aus einer Datei namens `SKILL.md`. `$skill-creator` kann ausführlichere Referenzdokumente, Skripte oder Assets hinzufügen, wenn der Arbeitsablauf sie erfordert.

## Skills, die du erstellen könntest

Verwende dasselbe Muster, wenn Codex bei künftigen Aufgaben dasselbe Runbook lesen, dieselbe CLI ausführen, dieselben Review-Kriterien befolgen, dasselbe Team-Update verfassen oder denselben Browserablauf im Rahmen der Qualitätssicherung testen soll. Zum Beispiel:

- **`$buildkite-fix-ci`** lädt die Logs fehlgeschlagener Jobs herunter, diagnostiziert den Fehler und schlägt die kleinstmögliche Änderung am Code vor.
- **`$fix-merge-conflicts`** checkt einen GitHub-PR aus, bringt ihn mit dem Basis-Branch auf den neuesten Stand, löst Konflikte und gibt den genauen Push-Befehl zurück.
- **`$frontend-skill`** sorgt dafür, dass Codex deinen UI-Stil, deine vorhandenen Komponenten, deinen QA-Zyklus mit Screenshots, deine Asset-Auswahl und den Feinschliff im Browser berücksichtigt.
- **`$pr-review-comments`** macht aus Review-Notizen prägnante Inline-Kommentare im richtigen Ton und mit passenden GitHub-Links.
- **`$web-game-prototyper`** legt den Umfang des ersten spielbaren Loops fest, wählt Assets aus, optimiert das Spielgefühl, nimmt Screenshots auf und verleiht dem Spiel im Browser den letzten Schliff.
