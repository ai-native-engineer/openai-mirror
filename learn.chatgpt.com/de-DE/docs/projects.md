<!-- source: https://learn.chatgpt.com/de-DE/docs/projects -->

Organisiere zusammengehörige Chats in einem Projekt und stelle ChatGPT so den nötigen Kontext bereit.
Die Ansicht **Projekte** in der ChatGPT-Desktop-App enthält ChatGPT-Projekte und
lokale Projekte, die mit Ordnern auf deinem Computer verknüpft sind.

## Ein Projekt auswählen oder ohne Projekt starten

Erstelle ein Projekt, wenn sich die Arbeit über einen längeren Zeitraum erstreckt, mehr als ein
Ergebnis liefert oder von denselben Dateien und Quellen abhängt. Starte einen Chat ohne Projekt,
wenn die Aufgabe in sich abgeschlossen ist und keinen gemeinsamen Projektkontext benötigt.

Nutze ein Projekt, um zusammengehörige Chats, Dateien, Anweisungen und Quellen an einem Ort zu organisieren.
Dasselbe Projekt kann Chats enthalten, die mit Chat oder ChatGPT Work gestartet wurden.

## Ein Projekt auswählen oder einen Chat ohne Projekt starten

Erstelle ein Projekt, wenn sich die Arbeit über einen längeren Zeitraum erstreckt, mehr als ein
Ergebnis liefert oder von denselben Dateien und Quellen abhängt. Starte einen Chat ohne Projekt,
wenn die Aufgabe in sich abgeschlossen ist und keinen gemeinsamen Projektkontext benötigt.

Jedes Projekt umfasst einen Bereich **Chats** für die Projekt-Chats und einen Bereich **Quellen**
für hochgeladene Dateien und verknüpften Kontext. Projektanweisungen gelten
für alle Chats des Projekts. Ein ChatGPT-Projekt ermöglicht keinen direkten Zugriff auf einen Ordner
auf deinem Computer. Lade die Quellen, die ChatGPT verwenden soll, hoch oder verbinde sie.

Starte in beiden Fällen im Projekt einen neuen Chat, damit er die gemeinsamen Dateien und
Anweisungen verwendet. Du findest ihn anschließend unter **Chats** wieder.

Codex CLI verwendet das Verzeichnis, in dem du Codex startest, als Projekt für den Chat.
Führe `codex` in dem Verzeichnis aus, in dem Codex arbeiten soll, oder übergib
`--cd <directory>` (`-C`), um das Verzeichnis explizit festzulegen. Die CLI bietet die
ChatGPT-Ansicht „Projekte“ nicht an.

Die IDE-Erweiterung verwendet den in deiner IDE geöffneten Ordner oder Workspace als lokales
Projekt. Wähle in einem Multi-Root-Workspace den Workspace-Stammordner für den Chat aus. Die
Erweiterung zeigt die ChatGPT-Ansicht „Projekte“ aus dem Web oder der Desktop-App nicht an.

<a id="work-in-a-project"></a>

## In einem Projekt arbeiten

Die Ansicht **Projekte** führt ChatGPT-Projekte und lokale Projekte an einem Ort zusammen.
Bei ChatGPT-Projekten stehen Projektdateien und Kontext in zusammengehörigen Chats zur Verfügung. Ein lokales
Projekt gibt Chats Zugriff auf einen oder mehrere Ordner auf deinem Computer, zum Beispiel auf eine
Sammlung von Quelldateien oder eine Codebasis.

Starte für jedes eigenständige Ergebnis einen eigenen Chat, damit Nachrichten und Ergebnisse
auf das jeweilige Ziel ausgerichtet bleiben und das Projekt zusammengehörige Arbeit übersichtlich bündelt.

  
    
  

## In einem Projekt arbeiten

Ein ChatGPT-Projekt ermöglicht allen zugehörigen Chats den Zugriff auf dieselben hochgeladenen Dateien,
Projektanweisungen und verbundenen Quellen. Nutze Chat für eine kurze Unterhaltung oder
ChatGPT Work für ein umfangreicheres Arbeitsergebnis. Beide erscheinen im Projekt unter
**Chats** . Starte für jedes eigenständige Ergebnis einen eigenen Chat, damit
Nachrichten und Ergebnisse auf das jeweilige Ziel ausgerichtet bleiben und der gemeinsame Projektkontext erhalten bleibt.

## In einem Projektverzeichnis arbeiten

Starte Codex in dem Verzeichnis, das den Dateikontext für den Chat bereitstellen soll. Verwende
`/new`, um für jedes eigenständige Ergebnis einen eigenen Chat zu starten. Verwende `/resume`, solange
Codex geöffnet ist, oder führe `codex resume` aus, um einen gespeicherten Chat fortzusetzen.

Der Chat behält sein Protokoll und das erfasste Arbeitsverzeichnis bei. Codex liest
die Dateien hingegen aus dem aktuellen Arbeitsbaum. Halte dauerhafte Projektvorgaben in
`AGENTS.md` oder eingecheckter Dokumentation fest, damit sie in künftigen Chats verfügbar sind.

## In einem Workspace arbeiten

Öffne den Ordner oder Workspace, der den Dateikontext für den Chat bereitstellen soll. Starte
für jedes eigenständige Ergebnis einen neuen Chat und wähle ihn anschließend unter **Letzte Chats** aus,
um ihn fortzusetzen. Chats im selben Projekt können mit denselben Dateien arbeiten, aber jeder
Chat behält sein eigenes Protokoll.

Die aktuelle Auswahl und die geöffneten Dateien liefern den Kontext für die aktuelle Anfrage. Halte
dauerhafte Projektvorgaben in `AGENTS.md` oder eingecheckter Dokumentation fest, damit sie
in künftigen Chats verfügbar sind.

<a id="manage-project-threads"></a>
<a id="organize-projects-and-chats"></a>

<a id="organize-projects-and-tasks"></a>

## Projekte und Chats organisieren

Behalte laufende Aufgaben im Blick und räume abgeschlossene aus dem Weg:

- **Hefte ein Projekt an** , damit es weit oben in der Seitenleiste bleibt. Du kannst es auch
  in der Ansicht „Projekte“ anheften.
- **Hefte einen Chat an** , wenn du häufig zu ihm zurückkehrst, auch wenn im
  Projekt neuere Chats erscheinen.
- **Benenne einen Chat um** und gib ihm einen kurzen Titel, der das Ergebnis beschreibt, zum Beispiel „Briefing für den
  Q3-Launch“ oder „Barrierefreiheitsprüfung des Checkouts“.
- **Suche nach Projekten** in der Ansicht „Projekte“. Öffne **Chats durchsuchen** in der
  Seitenleiste, um einen früheren Chat zu finden, wenn du dich an eine Formulierung oder einen Branch-Namen,
  aber nicht an den Titel erinnerst. Für „Chats durchsuchen“ ist standardmäßig kein Tastenkürzel
  festgelegt. Du kannst aber unter **Einstellungen \> Tastenkürzel** eines zuweisen.
- **Archiviere einen Chat** , wenn du die Arbeit abgeschlossen hast. Wähle im Projektmenü
**Chats archivieren** aus, um alle zugehörigen Chats gemeinsam zu archivieren.

Das Anheften fügt keinen Kontext hinzu und ändert nicht, worauf ChatGPT zugreifen kann. Es bestimmt nur,
wo das Projekt oder der Chat in der Seitenleiste erscheint.

Stelle archivierte Chats unter **Einstellungen \> Archivierte Chats** wieder her.

<a id="organize-projects-and-tasks-1"></a>

## Projekte und Chats organisieren

Behalte laufende Aufgaben im Blick und räume abgeschlossene aus dem Weg:

- **Hefte ein Projekt an** , damit es weit oben in der Seitenleiste bleibt. Du kannst es auch
  in der Ansicht „Projekte“ anheften.
- **Hefte einen Chat an** , wenn du häufig zu ihm zurückkehrst, auch wenn im
  Projekt neuere Chats erscheinen.
- **Benenne einen Chat um** und gib ihm einen kurzen Titel, der das Ergebnis beschreibt, zum Beispiel „Briefing für den
  Q3-Launch“ oder „Barrierefreiheitsprüfung des Checkouts“.
- **Suche nach Projekten** in der Ansicht „Projekte“. Durchsuche frühere Chats mit
<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>K</kbd>, wenn du dich an eine Formulierung oder einen
  Branch-Namen erinnerst, aber nicht an den Titel.
- **Archiviere einen Chat** , wenn du die Arbeit abgeschlossen hast.

Das Anheften fügt keinen Kontext hinzu und ändert nicht, worauf ChatGPT zugreifen kann. Es bestimmt nur,
wo das Projekt oder der Chat in der Seitenleiste erscheint.

Stelle archivierte Chats unter **Einstellungen \> Datenkontrollen \> Archivierte Chats** wieder her.

<a id="use-local-projects-for-folders-and-codebases"></a>

## Lokale Projekte für Ordner und Codebasen verwenden

Füge ein lokales Projekt hinzu, wenn ChatGPT Dateien auf deinem Computer lesen oder ändern soll.
Projekte benötigen keinen Ordner. Du kannst ihnen aber bei Bedarf Ordner hinzufügen.

Öffne zum Hinzufügen oder Ändern von Ordnern das Projektmenü und wähle **Projekt bearbeiten** aus.
Wähle **Ordner hinzufügen** aus, um mehrere Ordner hinzuzufügen. ChatGPT kann Dateien
in jedem hinzugefügten Ordner lesen und ändern. Um das standardmäßige Arbeitsverzeichnis zu ändern, bewege den Mauszeiger auf einen
Ordner und wähle **Als primär festlegen** aus.

Neue Chats beginnen im primären Ordner. Codex verwendet diesen Ordner außerdem als
Standard für Git-Vorgänge und die automatische Erkennung von `AGENTS.md`, Skills und
`config.toml`. Sekundäre Ordner bleiben für die Dateisuche sowie zum Lesen und
Bearbeiten verfügbar. Codex erkennt diese Projektdateien in
sekundären Ordnern jedoch nicht automatisch.

Verwende mehrere Ordner, wenn zusammengehörige Inhalte an verschiedenen Orten liegen, etwa eine App und
ihre Dokumentation oder eine Website und ihr Backend. Erstelle separate Projekte für
nicht zusammenhängende Arbeiten oder wenn jeder Chat nur auf einen Teil eines Repositorys zugreifen soll.
So bleibt der Arbeitskontext klar abgegrenzt. Remote-Projekte unterstützen derzeit nur einen
Ordner.

Mit [lokalen Umgebungen](/de-DE/codex/environments/local-environment) kannst du Setup-Aktionen
und häufig verwendete Befehle für ein Projekt festlegen. Der [Bereich für
Reviews](/de-DE/codex/code-review?surface=app) kann Änderungen in mehreren Repositorys anzeigen,
die mit demselben Projekt verknüpft sind. Aktionen für Pull Requests und
[Worktrees](/de-DE/codex/environments/git-worktrees) beziehen sich auf das primäre
Repository. Wenn du einen Chat in einem Worktree startest, bleiben die anderen Ordner
verknüpft.

Projekte und Worktrees organisieren die Arbeit, doch die [Sandbox](/de-DE/codex/sandboxing)
legt verbindlich fest, was lokale Befehle lesen oder ändern dürfen und worauf sie über das Netzwerk zugreifen können.

<a id="start-without-a-project"></a>

<a id="start-a-task-without-a-project"></a>

## Einen Chat ohne Projekt starten

Wähle **Neuer Chat** aus, wenn die Aufgabe in sich abgeschlossen ist und du keine gemeinsamen
Projektdateien oder Anweisungen und keinen Zugriff auf Ordner benötigst. Erstelle zuerst ein Projekt, wenn
mehrere Chats denselben Kontext benötigen.

<a id="start-a-task-without-a-project-1"></a>

## Einen Chat ohne Projekt starten

Starte einen Chat über die ChatGPT-Startseite, wenn der Chat keine gemeinsamen Projektdateien,
Anweisungen oder Quellen benötigt. Du kannst Chat oder ChatGPT Work verwenden. Im Web
wird in beiden Fällen ein Chat erstellt.

Wenn die Arbeit umfangreicher wird, verschiebe sie in ein Projekt und verwende für jedes
Ergebnis aussagekräftige Chatnamen. Ein Projekt kann parallele Chats für Recherche, Entwürfe, Reviews und
Nachbereitung enthalten, ohne alle Nachrichten in einem einzigen Kontext zu vermischen.

<a id="start-a-chat"></a>
<a id="start-a-standalone-chat"></a>

<a id="use-quick-chat-for-a-quick-conversation"></a>

## Schnellchat für eine kurze Frage verwenden

Der Schnellchat öffnet einen normalen ChatGPT-Chat. ChatGPT-Chats erscheinen nicht in der
Codex-Seitenleiste, in der deine Codex-Chats und -Projekte angezeigt werden.

Bewege den Mauszeiger auf **Neuer Chat** und wähle rechts daneben das Symbol **Schnellchat** aus. Alternativ
drückst du

<kbd>Cmd+Option+N</kbd> unter macOS oder <kbd>Ctrl+Alt+N</kbd> unter Windows und Linux.
Über **Neuer Chat** kannst du einen vorhandenen ChatGPT-Chat öffnen und ihn einem Codex-Chat
hinzufügen.

## Weitere Tools und Kontext einbinden

- Füge Dateien oder [Bildeingaben](/de-DE/codex/image-inputs) direkt einem Chat hinzu,
  wenn sie nur für diese Anfrage relevant sind.
- Installiere [Plug-ins](/de-DE/codex/plugins), um Kontext und Aktionen aus anderen
  Diensten einzubinden.
- Konfiguriere [MCP](/de-DE/codex/extend/mcp)-Server, wenn deine Organisation oder dein Entwicklungs-Setup
  Tools über das Model Context Protocol bereitstellt.
- Nutze [Erinnerungen](/de-DE/codex/customization/memories), sofern verfügbar, um nützlichen Kontext aus
  früheren Arbeiten in künftige Chats zu übernehmen.

- Übergib [Bildeingaben](/de-DE/codex/image-inputs) an einen Chat, wenn der visuelle Kontext
  nur für diese Anfrage relevant ist.
- Installiere [Plug-ins](/de-DE/codex/plugins), um Kontext und Aktionen aus anderen
  Diensten einzubinden.
- Konfiguriere [MCP](/de-DE/codex/extend/mcp)-Server, wenn deine Organisation oder dein Entwicklungs-Setup
  Tools über das Model Context Protocol bereitstellt.
- Nutze [Erinnerungen](/de-DE/codex/customization/memories), sofern verfügbar, um nützlichen Kontext aus
  früheren Arbeiten in künftige Chats zu übernehmen.

- Verweise auf geöffnete Dateien oder wähle Code im Editor aus, um Kontext für die
aktuelle Anfrage hinzuzufügen.
- Konfiguriere [MCP](/de-DE/codex/extend/mcp)-Server, wenn deine Organisation oder dein Entwicklungs-Setup
  Tools über das Model Context Protocol bereitstellt.
- Nutze [Erinnerungen](/de-DE/codex/customization/memories) vom verbundenen Codex-Host, sofern
  verfügbar, um nützlichen Kontext in künftige Chats zu übernehmen.

- Füge dem Bereich **Quellen** des Projekts Dateien und verbundene Quellen hinzu,
  wenn sie in allen zugehörigen Chats verfügbar sein sollen.
- Hänge Dateien oder [Bildeingaben](/de-DE/codex/image-inputs) direkt an einen Chat an, wenn
  sie nur für diesen Chat relevant sind.
- Installiere in ChatGPT Work [Plug-ins](/de-DE/codex/plugins), um Kontext und
  Aktionen aus anderen Diensten einzubinden.
- Nutze [Erinnerungen](/de-DE/codex/customization/memories), sofern verfügbar, um nützlichen Kontext aus
  früheren Arbeiten in künftige Chats zu übernehmen.

## Nächste Schritte

- [Erfahre, wie du Prompts schreibst und optimierst](/de-DE/codex/prompting)
- [Erfahre, wie du ChatGPT verwendest](/de-DE/codex/use-chatgpt)
- [Lang laufende Aufgaben fortsetzen](/de-DE/codex/long-running-work)
