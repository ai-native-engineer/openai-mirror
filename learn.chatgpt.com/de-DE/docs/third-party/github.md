<!-- source: https://learn.chatgpt.com/de-DE/docs/third-party/github -->

Nutze Codex Code Review für einen weiteren, besonders aussagekräftigen Review-Durchgang bei Pull Requests auf GitHub. Codex überprüft den Diff des Pull Requests, befolgt die Vorgaben deines Repositorys und veröffentlicht auf GitHub ein reguläres Code Review, das sich auf schwerwiegende Probleme konzentriert. Das Sicherheits-Review ist als Forschungsvorschau verfügbar und untersucht potenzielle Sicherheitsprobleme in einem Pull Request ausführlicher.

<br />

## Bevor du beginnst

Stelle Folgendes sicher:

- [Codex Cloud](/de-DE/codex/cloud) ist für das Repository eingerichtet, das du überprüfen möchtest.
- Du hast Zugriff auf die [Einstellungen für Codex Code Review](https://chatgpt.com/codex/settings/code-review).
- Eine Datei namens `AGENTS.md` ist vorhanden, falls Codex Repository-spezifische Review-Vorgaben befolgen soll.

## Codex Code Review einrichten

Um automatische Reviews zu konfigurieren, brauchst du ein verbundenes GitHub-Repository sowie Push- oder Adminrechte auf GitHub für dessen Einstellungen.

1. Richte [Codex Cloud](/de-DE/codex/cloud) ein.
2. Öffne die [Codex-Einstellungen](https://chatgpt.com/codex/settings/code-review).
3. Aktiviere **Code Review** für dein Repository.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## Ein Review von Codex anfordern

1. Erwähne `@codex review` in einem Kommentar zu einem Pull Request.
2. Warte, bis Codex reagiert (👀) und ein Review veröffentlicht.

<div class="not-prose max-w-xl mr-auto">
  
    
      
    
  
</div>
<br />

Codex veröffentlicht ein Review zum Pull Request, genau wie ein Teammitglied. Auf GitHub meldet Codex ausschließlich Probleme der Prioritätsstufen P0 und P1, damit sich die Review-Kommentare auf Risiken mit hoher Priorität konzentrieren.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## Automatische Reviews aktivieren

Wenn Codex jeden Pull Request automatisch überprüfen soll, aktiviere
**Automatische Reviews** in den [Codex-Einstellungen](https://chatgpt.com/codex/settings/code-review).
Codex veröffentlicht ein Review, sobald jemand einen neuen Pull Request zur Überprüfung eröffnet,
ohne dass ein Kommentar mit `@codex review` erforderlich ist.

## Festlegen, was Codex überprüft

Codex durchsucht dein Repository nach Dateien namens `AGENTS.md` und befolgt die geltenden
Code-Review-Regeln. Füge einen Abschnitt namens `## Code Review Rules` in die Datei ein, die dem
betreffenden Code am nächsten liegt. Verwende Überschriften mit `###`, um zusammengehörige Prüfungen bei
Bedarf zu gruppieren.

Ein Dienst zur Berichterstellung über Experimente kann beispielsweise verhindern, dass das Verhalten nach der Exposition eine Vergleichskohorte verändert:

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Lege Regeln für das gesamte Repository in der Datei `AGENTS.md` im Stammverzeichnis und dienstspezifische Regeln
in einer Datei in einem Unterverzeichnis ab, etwa `services/experiment_reporting/AGENTS.md`. Codex
wendet auf jede geänderte Datei sowohl die Vorgaben aus dem Stammverzeichnis als auch die jeweils spezifischeren Vorgaben an,
sodass Änderungen in anderen Bereichen keinen dienstspezifischen Kontext benötigen.

Beginne mit zwei oder drei prägnanten Regeln für Prüfungen, die in Reviews häufig erläutert werden. Nützliche Regeln:

- **Konzentriere dich auf Repository-spezifisches Verhalten mit erheblichen Auswirkungen.** Beschreibe die
  Kompatibilitätseinschränkung, Datengrenze oder riskante Nebenwirkung, die Codex melden soll,
  und erkläre, warum sie relevant ist.
- **Nenne die sichere Vorgehensweise oder den Ausnahmefall.** Gib Codex genügend Kontext, um echte Probleme
  von erwartetem Verhalten zu unterscheiden.
- **Halte Regeln klar abgegrenzt und dauerhaft anwendbar.** Beschreibe bevorzugt Ergebnisse statt Funktionsnamen, die
  sich ändern können, und platziere die Vorgaben nahe am betreffenden Code.
- **Überlasse mechanische Prüfungen der CI.** Nimm Formatierung, Linting und andere
  deterministische Prüfungen nicht in die Review-Regeln auf.

Öffne einen repräsentativen Pull Request und fordere mit `@codex review` ein Review an.
Verfeinere die Regeln anhand der Ergebnisse und Rückmeldungen. Grenze Vorgaben, die unnötige Meldungen erzeugen, ein oder
entferne sie.

Code-Review-Regeln geben Codex Orientierung; sie ersetzen weder Tests noch Branch-Schutzregeln noch erforderliche Genehmigungen.

Wenn du einmalig einen bestimmten Schwerpunkt setzen möchtest, füge ihn deinem Kommentar zum Pull Request hinzu:

`@codex review for issues in the database migration`

## Sicherheits-Review

Das Sicherheits-Review ist ein zusätzliches Review für Kundinnen und Kunden, die Sicherheitsproblemen in Pull Requests besondere Aufmerksamkeit widmen möchten. Es untersucht sicherheitsspezifische Risiken gründlicher als Code Review. Dazu analysiert es den Diff des Pull Requests, den zugehörigen Kontext aus dem Repository sowie konfigurierte Bedrohungsmodelle oder Sicherheitsvorgaben.

Auch Code Review kann bei der allgemeinen Überprüfung sicherheitsrelevante Probleme erkennen. Daher können sich die Ergebnisse von Code Review und Sicherheits-Review gelegentlich überschneiden.

### Sicherheits-Review einrichten

Ausführlichere Anleitungen zum Setup und Informationen zu den Konfigurationsoptionen findest du in der Dokumentation [zum
Sicherheits-Review](/de-DE/codex/security/security-review).

1. Richte [Codex Cloud](/de-DE/codex/cloud) ein.
2. Öffne die [Codex-Einstellungen](https://chatgpt.com/codex/settings/code-review).
3. Unter **Repository-Einstellungen** legst du fest, für welche Pull Requests das Sicherheits-Review
   ausgeführt wird und wann. Wähle **Immer, wenn Code Review ausgeführt wird** aus, damit das Sicherheits-Review
   zusammen mit Code Review ausgeführt wird.

### Ein Sicherheits-Review anfordern

Um ein Sicherheits-Review manuell anzufordern, füge einem Pull Request diesen Kommentar hinzu:

`@codex security review`

Codex reagiert, während das Review ausgeführt wird, und veröffentlicht die Sicherheitsbefunde anschließend direkt
im Pull Request. Öffne die zugehörige Codex-Aufgabe und wähle den Tab **Bericht zur
Sicherheit** aus, um den vollständigen Bericht anzuzeigen.

## Auf Review-Ergebnisse reagieren

Nachdem Codex ein Review veröffentlicht hat, kannst du Codex in einem weiteren Kommentar bitten, Probleme im selben Pull Request zu beheben:

```md
@codex fix the P1 issue

Codex startet einen Cloud-Chat mit dem Pull Request als Kontext und kann eine Korrektur zurück in den Branch pushen, sofern die erforderliche Berechtigung vorliegt.

## Codex weitere Aufgaben zuweisen

Wenn du `@codex` in einem Kommentar mit einer anderen Anweisung als `review` erwähnst, startet Codex einen [Cloud-Chat](/de-DE/codex/cloud) mit deinem Pull Request als Kontext.

```md
@codex fix the CI failures

## Probleme mit Code Review beheben

Wenn Codex nicht reagiert oder kein Review veröffentlicht:

- Prüfe, ob du **Code Review** für das Repository in den [Codex-Einstellungen](https://chatgpt.com/codex/settings/code-review) aktiviert hast.
- Prüfe, ob der Pull Request zu einem Repository gehört, für das [Codex Cloud](/de-DE/codex/cloud) eingerichtet ist.
- Verwende in einem Kommentar zu einem Pull Request exakt den Auslöser `@codex review`.
- Prüfe bei automatischen Reviews, ob du **Automatische Reviews** aktiviert hast und ob
  das Ereignis des Pull Requests deinen Einstellungen für den Review-Auslöser entspricht.
