<!-- source: https://learn.chatgpt.com/de-DE/docs/code-review -->

Nutze ChatGPT oder Codex, um Codeänderungen zu überprüfen, bevor du sie committest oder pushst.

## Ein Review starten

Lade in ChatGPT Work den Code hoch, den du überprüfen lassen möchtest, oder stelle ihn über
ein installiertes [Quellcode-Plug-in](/de-DE/codex/plugins) bereit. Gib in deinem Prompt den
zu prüfenden Pull Request, Branch und Commit sowie die Dateien und Review-Kriterien an.

### Review in der App

Öffne den Review-Bereich, um Änderungen nachzuvollziehen, Feedback zu einzelnen Zeilen zu geben
und zu entscheiden, welche Änderungen du stagen, verwerfen, committen oder pushen möchtest.

Gib `/review` in den Editor ein, um Codex mit der Überprüfung der Änderungen zu beauftragen. Wähle
**Mit einem Basis-Branch vergleichen** oder **Nicht committete Änderungen überprüfen**. Codex meldet
priorisierte Hinweise, ohne deinen Working Tree zu verändern.

Der Review-Bereich setzt ein Projekt in einem Git-Repository voraus. Falls dein Projekt
noch kein Git-Repository ist, fordert dich die App auf, eines zu erstellen.

Gib `/review` ein, um die Voreinstellungen für Reviews in der CLI zu öffnen. Codex startet einen eigenen Review-Agenten,
der den ausgewählten Diff liest und priorisierte, direkt umsetzbare Hinweise meldet,
ohne deinen Working Tree zu verändern.

Gib `/review` in den Editor der IDE-Erweiterung ein. Wähle **Mit einem
Basis-Branch vergleichen** oder **Nicht committete Änderungen überprüfen**. Codex meldet priorisierte Hinweise,
ohne deinen Working Tree zu verändern.

Der Befehl `/review` wird nur angezeigt, wenn das geöffnete Projekt
in einem Git-Repository liegt.

## Review-Umfang auswählen

Nenne in deinem Prompt den Pull Request, den Branch, den Commit oder die zu prüfenden Dateien. Um
lokale Dateien zu überprüfen, die nicht über ein installiertes Quellcode-Plug-in verfügbar sind,
lade sie in den Chat hoch.

### Angezeigte Änderungen

Der Review-Bereich zeigt den Zustand deines Git-Repositorys, nicht nur die Änderungen von Codex.
Er umfasst Änderungen von Codex, eigene Änderungen und alle weiteren
nicht committeten Änderungen im Repository.

Standardmäßig zeigt der Review-Bereich Änderungen unter **Nicht gestagt** . Verwende **Gestagt** für den
Git-Index, **Commit** für einen ausgewählten Commit, **Branch** für den Diff mit deinem
Basis-Branch oder **Letzte Antwort** für die jüngste Antwort des Assistenten.

### Mehrere Repositorys überprüfen

Wenn ein [lokales Projekt mehrere Ordner umfasst](/de-DE/codex/projects#use-local-projects-for-folders-and-codebases),
die zu unterschiedlichen Git-Repositorys gehören, kann der Review-Bereich Änderungen aus jedem
Repository anzeigen. Öffne die Repository-Auswahl in der Kopfzeile des Review-Bereichs, um
ein anderes Repository zu prüfen und hinzugefügte oder entfernte Zeilen anzuzeigen, ohne den
aktuellen Review-Bereich zu verlassen.

Wähle **Letzte Antwort** , um die neuesten Änderungen des Assistenten in allen verbundenen
Repositorys zu sehen. Für diese Ansicht zeigt die Repository-Auswahl **Alle Repositorys** an. Andere
Review-Umfänge wie **Nicht gestagt**, **Gestagt** und **Branch** gelten für das
ausgewählte Repository.

Wähle für `/review` eine dieser Optionen:

- Die Option **Mit einem Basis-Branch vergleichen** ermittelt die Merge-Basis und überprüft den Diff deines Branches.
- Die Option **Nicht committete Änderungen überprüfen** umfasst gestagte, nicht gestagte und nicht nachverfolgte Dateien.
- Mit der Option **Einen Commit überprüfen** prüft Codex genau die Änderungen eines ausgewählten Commits.
- Die Option **Eigene Review-Anweisungen** richtet das Review nach den von dir vorgegebenen Kriterien aus.

Wähle für `/review` eine dieser Optionen:

- Die Option **Mit einem Basis-Branch vergleichen** vergleicht deinen aktuellen Branch mit einem von dir ausgewählten Branch.
- Die Option **Nicht committete Änderungen überprüfen** prüft die Änderungen in deinem Working Tree.

## Mit Review-Ergebnissen arbeiten

Die Review-Ergebnisse werden im Web-Chat angezeigt. Bitte um Belege, fordere eine
gezieltere Folgeüberprüfung an oder bitte ChatGPT, überarbeitete Dateien vorzubereiten.

### Ergebnisse des Code Reviews

Review-Ergebnisse werden als Inline-Kommentare im Review-Bereich angezeigt.

Standardmäßig werden Reviews im aktuellen Chat ausgeführt. Wähle unter **Einstellungen** \> **Allgemein** \>
**Code Review** die Option **Separat** , um einen eigenen Review-Chat zu starten. Weitere Informationen findest du in den
[Entwicklungseinstellungen](/codex/developer-settings?surface=app#app-code-review).

  
    
  

Das Review erscheint als eigener Beitrag im Transkript. Lege `review_model` in
`config.toml` fest, wenn für Reviews ein anderes Modell als in der aktuellen
Sitzung verwendet werden soll.

Standardmäßig wird das Review im aktuellen Chat ausgeführt. Setze `chatgpt.reviewDelivery` auf
`detached`, wenn `/review` einen separaten Review-Chat starten soll. Weitere Informationen findest du in der
[Referenz zu den Einstellungen der IDE-Erweiterung](/codex/developer-settings?surface=ide#ide-editor-settings-reference).

Wenn du ChatGPT bittest, überarbeitete Dateien vorzubereiten, bleiben die für den Chat verfügbaren Tools und
Workspace-Berechtigungen unverändert.

Wenn du Codex bittest, die gefundenen Korrekturen anzuwenden, gelten deine üblichen [Einstellungen für Sandbox und
Genehmigungen](/de-DE/codex/sandboxing).

## Im Review-Bereich navigieren

- Ein Klick auf einen Dateinamen öffnet die Datei normalerweise im ausgewählten Editor. Den
  Standardeditor kannst du in den [Entwicklungseinstellungen](/codex/developer-settings?surface=app#app-project-and-terminal-behavior) auswählen.
- Ein Klick auf den Hintergrund des Dateinamens klappt den Diff auf oder zu.
- Wenn du <kbd>Cmd</kbd> gedrückt hältst und auf eine einzelne Zeile klickst, wird sie im ausgewählten Editor geöffnet.
- Wenn du mit einer Änderung zufrieden bist, kannst du sie [stagen oder unerwünschte Änderungen verwerfen](#staging-and-reverting-files).

## Feedback mit Inline-Kommentaren

Mit Inline-Kommentaren kannst du Feedback direkt an bestimmten Zeilen im Diff hinterlassen.
So kannst du Codex oft am schnellsten zur passenden Korrektur führen.

So hinterlässt du einen Inline-Kommentar:

1. Öffne den Review-Bereich.
2. Bewege den Mauszeiger über die Zeile, die du kommentieren möchtest.
3. Wähle die daraufhin angezeigte Schaltfläche **+** aus.
4. Gib dein Feedback ein und sende es ab.
5. Sobald du dein Feedback hinterlassen hast, sende eine Nachricht im Chat.

Da sich Kommentare auf konkrete Zeilen beziehen, kann Codex präziser reagieren als bei
einer allgemeinen Anweisung.

Codex versteht Inline-Kommentare als Hinweise für das Review. Sende danach eine
Folgenachricht, in der du dein Ziel klar formulierst, zum Beispiel: „Berücksichtige die
Inline-Kommentare und halte den Umfang der Änderungen so gering wie möglich.“

## Reviews von Pull Requests

Wenn Codex für dein Repository Zugriff auf GitHub hat und sich das aktuelle Projekt auf
dem Branch des Pull Requests befindet, kann dir die ChatGPT-Desktop-App helfen, das
Feedback zum Pull Request direkt in der App zu bearbeiten. Die Seitenleiste zeigt den Kontext zum Pull Request und
das Feedback der Reviewenden. Im Review-Bereich stehen die Kommentare
neben dem Diff, sodass du Codex im selben Chat mit der Behebung der Probleme beauftragen kannst.

Installiere die GitHub CLI (`gh`) und authentifiziere sie mit `gh auth login`, damit Codex
den Kontext zum Pull Request, Review-Kommentare und geänderte Dateien laden kann. Wenn `gh`
fehlt oder nicht authentifiziert ist, werden Details zum Pull Request möglicherweise weder in der Seitenleiste
noch im Review-Bereich angezeigt.

Nutze diesen Ablauf, wenn du den gesamten Korrekturprozess an einem Ort durchführen möchtest:

1. Öffne den Review-Bereich auf dem Branch des Pull Requests.
2. Prüfe den Kontext zum Pull Request sowie die Kommentare und geänderten Dateien.
3. Bitte Codex, die Probleme aus den von dir ausgewählten Kommentaren zu beheben.
4. Sieh dir den resultierenden Diff im Review-Bereich an.
5. Sobald du bereit bist, stage und committe die Änderungen und pushe sie in den Branch des Pull Requests.

Informationen zu von GitHub ausgelösten Reviews findest du unter [Codex in GitHub verwenden](/de-DE/codex/third-party/github).

## Dateien stagen und Änderungen verwerfen

Der Review-Bereich enthält Git-Aktionen, mit denen du den Diff anpassen kannst, bevor du einen Commit erstellst.

Du kannst Änderungen auf den folgenden Ebenen stagen, aus dem Staging-Bereich entfernen oder verwerfen:

- **Gesamter Diff**: Verwende die Aktionsschaltflächen in der Kopfzeile des Review-Bereichs, etwa **Alle Änderungen stagen** oder **Alle Änderungen verwerfen**.
- **Pro Datei**: Du kannst eine einzelne Datei stagen, aus dem Staging-Bereich entfernen oder ihre Änderungen verwerfen.
- **Pro Hunk**: Du kannst einen einzelnen Hunk stagen, aus dem Staging-Bereich entfernen oder verwerfen.

Nutze Staging, wenn du einen Teil der Änderungen übernehmen möchtest, und verwirf Änderungen, die du nicht behalten möchtest.

### Status gestagter und nicht gestagter Änderungen

Git kann in derselben Datei sowohl gestagte als auch nicht gestagte Änderungen abbilden. Ist das der Fall, kann der Bereich dieselbe Datei in beiden Ansichten anzeigen. Dieses Verhalten ist bei Git normal.
