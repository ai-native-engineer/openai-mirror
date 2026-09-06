<!-- source: https://learn.chatgpt.com/de-DE/docs/reference/troubleshooting -->

## Häufig gestellte Fragen

### Im Seitenbereich erscheinen Dateien, die Codex nicht bearbeitet hat

Wenn sich dein Projekt in einem Git-Repository befindet, zeigt der Review-Bereich automatisch
Änderungen anhand des Git-Status deines Projekts an. Dazu gehören auch Änderungen, die Codex
nicht vorgenommen hat.

Im Review-Bereich kannst du zwischen bereitgestellten und noch nicht
bereitgestellten Änderungen wechseln und deinen Branch mit main vergleichen.

Wenn du nur die Änderungen deines letzten Codex-Durchlaufs sehen möchtest, stelle den Diff-Bereich
auf die Ansicht **Letzter Durchlauf** um.

[Weitere Informationen zur Verwendung des Review-Bereichs](/de-DE/codex/code-review?surface=app).

### Projekt aus der Seitenleiste entfernen

Um ein Projekt aus der Seitenleiste zu entfernen, bewege den Mauszeiger über den Projektnamen, klicke
auf die drei Punkte und wähle „Entfernen“ aus. Um es wiederherzustellen, füge das
Projekt über die Schaltfläche **Neues Projekt hinzufügen** neben **Chats** oder mit

<kbd>Cmd</kbd>+<kbd>O</kbd>.

<a id="find-archived-threads"></a>
<a id="find-archived-tasks"></a>

### Archivierte Chats finden

Archivierte Chats findest du unter [Einstellungen](codex://settings). Wenn du die Archivierung eines Chats aufhebst,
erscheint er wieder an seiner ursprünglichen Position in der Seitenleiste.

<a id="only-some-threads-appear-in-the-sidebar"></a>
<a id="only-some-tasks-appear-in-the-sidebar"></a>

### In der Seitenleiste werden nur einige Chats angezeigt

Über die Seitenleiste kannst du Chats nach dem Status eines Projekts filtern. Wenn dir
Chats fehlen, wähle das Filtersymbol neben **Chats** und dann
**Chronologisch** aus. Wenn der Chat weiterhin nicht angezeigt wird, öffne
[Einstellungen](codex://settings) und sieh unter **Archivierte Chats** nach.

### Code lässt sich in einem Worktree nicht ausführen

Worktrees werden in einem anderen Verzeichnis erstellt und übernehmen standardmäßig die in
Git versionierten Dateien. Je nachdem, wie du Abhängigkeiten und Tools für dein
Projekt verwaltest, musst du möglicherweise Setup-Skripte für deinen Worktree in einer
[lokalen Umgebung](/de-DE/codex/environments/local-environment) ausführen oder ignorierte Setup-Dateien
mit [`.worktreeinclude`](/de-DE/codex/environments/git-worktrees#copy-ignored-local-files-into-managed-worktrees) kopieren.
Alternativ kannst du die Änderungen in deinem regulären lokalen Projekt auschecken. Weitere Informationen findest du
in der [Dokumentation zu Worktrees](/de-DE/codex/environments/git-worktrees).

### Die App erkennt die freigegebene lokale Umgebung eines Teammitglieds nicht

Die Konfiguration der lokalen Umgebung muss sich im Ordner `.codex` im
Stammverzeichnis deines Projekts befinden. Wenn du in einem Monorepo mit mehreren
Projekten arbeitest, öffne das Projekt im Verzeichnis, das den
Ordner `.codex` enthält.

### Codex fordert Zugriff auf Apple Music an

Je nach Aufgabe muss Codex möglicherweise im Dateisystem navigieren. Für bestimmte
Verzeichnisse unter macOS, darunter Musik, Downloads oder Schreibtisch, ist eine
zusätzliche Genehmigung erforderlich. Wenn Codex dein Benutzerverzeichnis lesen muss,
fordert macOS dich auf, den Zugriff auf diese Ordner zu genehmigen.

<a id="automations-create-many-worktrees"></a>

### Durch geplante Aufgaben entstehen viele Worktrees

Häufig ausgeführte geplante Aufgaben können mit der Zeit viele Worktrees erzeugen. Archiviere geplante
Ausführungen, die du nicht mehr benötigst, und hefte Ausführungen nur an, wenn du ihre
Worktrees behalten möchtest.

### Prompt nach Auswahl des falschen Ziels wiederherstellen

Wenn du versehentlich einen Chat mit dem falschen Ziel (**Lokal**, **Worktree** oder **Cloud**) gestartet hast, kannst du die aktuelle Ausführung abbrechen und deinen vorherigen Prompt wiederherstellen, indem du im Editor die Pfeiltaste nach oben drückst.

### Eine Funktion funktioniert in der Codex CLI, aber nicht in der ChatGPT-Desktop-App

Die ChatGPT-Desktop-App und die Codex CLI können unterschiedliche Codex-Versionen enthalten. Deshalb
sind Funktionen möglicherweise auf einer der beiden Oberflächen früher verfügbar als auf der anderen. Experimentelle Funktionen sind
unter Umständen ebenfalls zuerst in der Codex CLI verfügbar.

Führe den folgenden Befehl aus, um die Version der Codex CLI auf deinem System zu ermitteln:

```bash
codex --version

Um die mit deiner ChatGPT-Desktop-App gebündelte Codex-Version zu ermitteln, verwende den
weiterhin vorhandenen Pfad zum Kompatibilitäts-Bundle `Codex.app`:

```bash
/Applications/Codex.app/Contents/Resources/codex --version

## Feedback und Logs

Gib <kbd>/</kbd> in das Texteingabefeld ein, um dem Team Feedback zu geben. Wenn
du die Feedback-Funktion in einem bestehenden Chat aufrufst, kannst du auswählen, ob du die
bestehende Sitzung zusammen mit deinem Feedback teilen möchtest. Nach dem Senden deines Feedbacks
erhältst du eine Sitzungs-ID, die du dem Team mitteilen kannst.

So meldest du ein Problem:

1. Suche im Codex-Repository auf GitHub nach [vorhandenen GitHub-Issues](https://github.com/openai/codex/issues).
2. [Neues GitHub-Issue öffnen](https://github.com/openai/codex/issues/new?template=2-bug-report.yml&steps=Uploaded%20thread%3A%20019c0d37-d2b6-74c0-918f-0e64af9b6e14)

Weitere Logs findest du an folgenden Speicherorten:

- App-Logs (macOS): `~/Library/Logs/com.openai.codex/YYYY/MM/DD`
- Sitzungstranskripte: `$CODEX_HOME/sessions` (Standard: `~/.codex/sessions`)
- Archivierte Sitzungen: `$CODEX_HOME/archived_sessions` (Standard: `~/.codex/archived_sessions`)

Wenn du Logs teilst, prüfe sie zuerst, um sicherzustellen, dass sie keine sensiblen
Informationen enthalten.

## Blockierte Zustände und Lösungswege

Wenn ein Chat zu hängen scheint:

1. Prüfe, ob Codex auf eine Genehmigung wartet.
2. Öffne das Terminal und führe einen einfachen Befehl wie `git status` aus.
3. Starte einen neuen Chat mit einem kürzeren, klarer eingegrenzten Prompt.

Wenn du die Erstellung eines Worktrees versehentlich abbrichst und deinen Prompt verlierst, drücke im Editor die
Pfeiltaste nach oben, um ihn wiederherzustellen.

## Terminalprobleme

**Terminal scheint zu hängen**

1. Schließe den Terminalbereich.
2. Öffne ihn mit <kbd>Ctrl</kbd>+<kbd>\`</kbd> erneut.
3. Führe einen einfachen Befehl wie `pwd` oder `git status` erneut aus.

Wenn sich Befehle anders als erwartet verhalten, prüfe zuerst das aktuelle Verzeichnis und den
Branch im Terminal.

Wenn das Terminal weiterhin hängt, warte, bis deine aktiven Chats abgeschlossen sind, und starte die App neu.

**Schriftarten werden nicht korrekt dargestellt**

Codex verwendet dieselbe Schriftart im Review-Bereich, im integrierten Terminal und für sämtlichen anderen Code, der in der App angezeigt wird. Du kannst die Schriftart im Bereich [Einstellungen](codex://settings) unter **Code-Schriftart** konfigurieren.
