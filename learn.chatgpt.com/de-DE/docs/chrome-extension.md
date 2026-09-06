<!-- source: https://learn.chatgpt.com/de-DE/docs/chrome-extension -->

Mit der ChatGPT-Browsererweiterung kannst du von der ChatGPT-Desktop-App aus in Google Chrome, Microsoft Edge, Brave, Opera oder Vivaldi arbeiten. ChatGPT kann Inhalte auf Websites lesen oder dort Aktionen ausführen, wenn du bereits angemeldet bist, etwa bei LinkedIn, Salesforce, Gmail oder internen Tools.

Alle fünf Browser unterstützen Tab-Erwähnungen und die Browsersteuerung über die
Desktop-App. Chrome, Edge, Brave und Vivaldi unterstützen auch den seitlichen Chat. **Opera unterstützt
keinen seitlichen Chat**. Starte Aufgaben für Opera stattdessen in der Desktop-App.

Aktualisiere die ChatGPT-Desktop-App, bevor du einen weiteren Browser einrichtest. Welche Browser verfügbar sind, kann vom Rollout und deinen Workspace-Einstellungen abhängen.

Wenn ChatGPT stattdessen seinen integrierten Browser steuern soll, verwende `@Browser`. Der
[integrierte Browser](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app)
unterstützt Anmeldungen und ermöglicht Browseraufgaben innerhalb von ChatGPT, ohne dein
übliches Browserprofil zu verwenden.

Je nach Aufgabe kann ChatGPT auch zwischen Tools wechseln: Es nutzt Plug-ins, wenn eine spezielle Integration verfügbar ist, deinen Browser, wenn es den Kontext einer angemeldeten Browsersitzung benötigt, und den integrierten Browser für localhost.

<div className="not-prose my-4">
  
</div>

<a id="use-chatgpt-from-chrome"></a>

## Seitlichen Chat im Browser verwenden

Der seitliche Chat ist in Chrome, Edge, Brave und Vivaldi verfügbar.

Öffne ChatGPT neben der gerade angezeigten Seite, um Fragen dazu zu stellen oder anschließend Aufgaben zu bearbeiten, die den Seitenkontext zusammen mit lokalen Dateien und verbundenen Apps nutzen können. ChatGPT kann den Kontext deiner geöffneten Tabs verwenden, wenn eine Aufgabe ihn erfordert.

1. Öffne die Seite, mit der du arbeiten möchtest.
2. Wähle ChatGPT in der Symbolleiste des Browsers oder im Menü **Erweiterungen** aus. Unter macOS
   kannst du auch <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd> drücken.
3. Stelle eine Frage zur Seite oder gib ChatGPT eine Aufgabe.

Die Seitenleiste bleibt dem Tab zugeordnet, in dem du sie geöffnet hast. Chats, die du im seitlichen Chat startest, sind auch in der ChatGPT-App verfügbar. Du kannst außerdem kürzlich verwendete ChatGPT-Chats im seitlichen Chat öffnen und so an beiden Orten weiterarbeiten.

  

## Tabs und ausgewählten Text in einen Chat übernehmen

Erwähne in der Desktop-App einen geöffneten Browser-Tab, wenn ChatGPT die Seite als Kontext verwenden soll. In Browsern mit seitlichem Chat kannst du Tabs auch dort erwähnen. Du kannst außerdem Text auf einer Seite markieren und die Auswahl in deinen Chat übernehmen, um nach einer bestimmten Passage zu fragen, ohne die gesamte Seite zu kopieren.

In Browsern mit seitlichem Chat kannst du auch mit der rechten Maustaste auf die Seite klicken und
**ChatGPT fragen** auswählen. Der seitliche Chat öffnet sich mit dem relevanten Seitenkontext, sodass du
die Anfrage im Browser fortsetzen kannst.

### Eine Frage zu einem YouTube-Video stellen

Öffne ein YouTube-Video und stelle dann im seitlichen Chat eines unterstützten Browsers eine Frage dazu. Wenn Untertitel verfügbar sind, kann ChatGPT das mit Zeitstempeln versehene Transkript des Videos verwenden, um den Inhalt zu erklären, zusammenzufassen oder Fragen dazu zu beantworten.

Behandle Inhalte von Webseiten, ausgewählten Text und Videotranskripte als nicht vertrauenswürdigen Kontext. Prüfe die Seite und alle angeforderten Berechtigungen, bevor du ChatGPT bittest, diese Informationen zu verwenden oder auf ihrer Grundlage zu handeln.

<a id="set-up-the-chrome-extension"></a>

## Deinen Browser einrichten

Installiere den Browser auf deinem Computer und öffne dann **Einstellungen \> Computernutzung** in der
ChatGPT-Desktop-App. Klappe **Weitere Browser** auf, wenn dein Browser
nicht in der Hauptliste angezeigt wird.

1. Wähle deinen Browser aus und folge den angezeigten Aufforderungen, um das erforderliche Plug-in zu installieren.
2. Wähle neben dem Browser **Installieren** aus, um die Seite der Erweiterung im jeweiligen Store zu öffnen.
   Installiere die ChatGPT-Erweiterung und prüfe die Berechtigungsanfragen des Browsers.
3. Kehre zu **Computernutzung** zurück und vergewissere dich, dass neben dem Browser **Verwalten** angezeigt wird.
4. Starte einen Chat in ChatGPT Work oder Codex und wähle deinen Browser über eine
`@`-Erwähnung aus. Verwende das Browserprofil, in dem du die Erweiterung installiert hast.

Mit dem Schalter für deinen Browser unter **Computernutzung** legst du fest, ob er im Menü für
`@`-Erwähnungen erscheint. Um stattdessen Website-Berechtigungen zu ändern, wähle **Verwalten** aus.

  

<a id="start-a-chrome-task-from-chatgpt"></a>

## Eine Browseraufgabe über ChatGPT starten

Starte nach dem Setup einen neuen Chat in ChatGPT Work oder Codex. Wähle **Chrome**, **Edge**,
**Brave Browser**, **Opera** oder **Vivaldi** im Menü für `@`-Erwähnungen aus, um festzulegen,
welchen Browser ChatGPT verwendet. Zum Beispiel:

```text
@Edge open Salesforce and update the account from these call notes.

Du kannst auch einen geöffneten Tab erwähnen, um ChatGPT den Kontext dieser Seite bereitzustellen. Opera unterstützt diese Arbeitsabläufe in der Desktop-App, obwohl es keinen seitlichen Chat bietet.

## Website-Zugriff steuern

Standardmäßig fragt ChatGPT nach, bevor es mit einer neuen Website interagiert. Die Anfrage richtet
sich nach dem Host der Website, zum Beispiel `example.com`.

Wenn ChatGPT um Erlaubnis bittet, eine Website zu verwenden, kannst du die Option wählen, die zur Aufgabe und deiner Risikotoleranz passt:

- Mit **Einmal zulassen** darf ChatGPT die Website einmal verwenden.
- Mit **Für diese Website zulassen** kann ChatGPT die Website erneut verwenden, ohne nachzufragen.
- Mit **Für alle Websites zulassen** kann ChatGPT Websites verwenden, ohne nachzufragen.
- Mit **Ablehnen** verhinderst du, dass ChatGPT die Website verwendet.

### Zugelassene und blockierte Websites verwalten

Öffne in der ChatGPT-Desktop-App **Einstellungen** \> **Computernutzung** und wähle dann
**Verwalten** neben deinem Browser aus, um eine Zulassungsliste und eine Sperrliste für
Domains zu verwalten. Die Zulassungsliste enthält Domains, die ChatGPT ohne erneute Nachfrage verwenden kann.
Die Sperrliste enthält Domains, die ChatGPT nicht verwenden soll. Diese Website-Berechtigungen gelten
für alle unterstützten Browser.

Wenn du eine Domain aus der Zulassungsliste entfernst, fragt ChatGPT vor der Verwendung erneut nach. Wenn du eine Domain aus der Sperrliste entfernst, kann ChatGPT wieder nachfragen, anstatt die Domain als blockiert zu behandeln.

#### Für alle Websites zulassen 

Wenn du **Für alle Websites zulassen** auswählst, fragt ChatGPT nicht mehr nach einer Bestätigung,
bevor es Websites verwendet. Wähle diese Option nur, wenn du ChatGPT bei der Nutzung beliebiger
im Browser geöffneter Websites vertraust.

#### Browserverlauf 

Der Browserverlauf kann sensible Telemetriedaten, interne URLs, Suchbegriffe und Aktivitäten aus Browsersitzungen auf Geräten enthalten, auf denen du angemeldet bist. Wenn du ChatGPT den Zugriff auf den Browserverlauf erlaubst, können relevante Verlaufseinträge Teil des Kontexts werden, den ChatGPT für die Aufgabe verwendet. Bösartige oder irreführende Seiteninhalte können das Risiko erhöhen, dass ChatGPT diese Daten an eine nicht vorgesehene Stelle kopiert.

ChatGPT fragt nach, wenn es den Browserverlauf verwenden möchte. ChatGPT beschränkt den Zugriff auf die jeweilige Anfrage. Für den Verlauf gibt es keine Option zur dauerhaften Zulassung.

## Daten und Sicherheit

<a id="chrome-extension-permissions"></a>

### Berechtigungen der Browsererweiterung

Bei der Installation der Erweiterung fordert dich dein Browser auf, Berechtigungen zu erteilen. Der Berechtigungsdialog von Chrome kann zum Beispiel Folgendes enthalten:

- Auf den Seiten-Debugger zugreifen
- Alle deine Daten auf allen Websites lesen und ändern
- Deinen Browserverlauf auf allen Geräten lesen und ändern, auf denen du angemeldet bist
- Benachrichtigungen anzeigen
- Deine Lesezeichen lesen und ändern
- Deine Downloads verwalten
- Mit kooperierenden nativen Anwendungen kommunizieren
- Deine Tabgruppen ansehen und verwalten

Mit diesen Berechtigungen kann die Erweiterung Arbeitsabläufe im Browser ausführen. ChatGPT nutzt weiterhin seine eigenen Bestätigungsabfragen, Einstellungen, Zulassungs- und Sperrlisten, bevor es während einer Aufgabe auf Websites oder den Browserverlauf zugreift.

### Erinnerungen

Für die Computernutzung gilt deine Einstellung für Erinnerungen. Wenn Erinnerungen aktiviert sind, kann ChatGPT relevante gespeicherte Erinnerungen nutzen, während es in deinem Browser arbeitet. Wenn Erinnerungen deaktiviert sind, werden bei der Browsersteuerung keine Erinnerungen verwendet.

### Welche Browserdaten OpenAI speichert

OpenAI speichert kein separates vollständiges Protokoll deiner über die Erweiterung ausgeführten Browseraktionen. OpenAI speichert Browseraktivitäten nur, wenn sie Teil des ChatGPT-Kontexts werden. Dazu gehören etwa Texte, die ChatGPT von einer Seite liest, Screenshots, Tool-Aufrufe, Zusammenfassungen, Nachrichten oder andere im Chat enthaltene Inhalte.

Deine ChatGPT-Datenkontrollen gelten für Inhalte, die im Kontext verarbeitet werden. Vermeide es, über Browseraufgaben Geheimnisse oder hochsensible Daten zu übermitteln, es sei denn, sie sind erforderlich und du bist anwesend, um jeden Prompt zu prüfen.

## Fehlerbehebung

Wenn ChatGPT keine Verbindung zu deinem Browser herstellen kann, prüfe zuerst, ob die Website, auf die ChatGPT zugreifen möchte, in den Einstellungen auf der Sperrliste steht. Wenn die Website nicht gesperrt ist, gehe die folgenden Prüfschritte durch:

1. Aktualisiere die ChatGPT-Desktop-App. Wenn du mehrere Desktop-Apps von ChatGPT oder Codex installiert hast, aktualisiere alle oder entferne Kopien, die du nicht mehr verwendest.
2. Starte deinen Browser neu. Öffne ChatGPT in Chrome, Edge, Brave oder Vivaldi erneut über
   die Symbolleiste oder das Menü **Erweiterungen** und prüfe, ob der seitliche Chat geladen wird. Opera
   hat keinen seitlichen Chat. Prüfe die Verbindung über die Desktop-App.
3. Prüfe unter **Einstellungen \> Computernutzung**, ob dein Browser aufgeführt ist und
**Verwalten** angezeigt wird. Falls weiterhin **Installieren** angezeigt wird, führe das Setup erneut durch.
   Wenn der Browser im Menü für `@`-Erwähnungen fehlt, aktiviere seinen Schalter.
4. Vergewissere dich, dass du das Browserprofil verwendest, in dem die Erweiterung installiert ist. Wenn du mehrere Profile verwendest, installiere und aktiviere die Erweiterung im aktiven Profil.
5. Starte einen neuen Chat in ChatGPT Work oder Codex und versuche die Browseraufgabe erneut. Dadurch kann der chatbezogene Verbindungsstatus zurückgesetzt werden.
6. Starte die ChatGPT-Desktop-App neu und versuche es noch einmal. Wenn die Erweiterung weiterhin
   keine Verbindung herstellt, installiere sie über **Einstellungen \> Computernutzung** neu.
7. Wenn ChatGPT den Browser weiterhin nicht verwenden kann, führe `/feedback`
   in der App aus und gib die Chat-ID an, wenn du den Support kontaktierst.

### Dateien hochladen

Wenn für eine Chrome-Aufgabe eine Datei von deinem Computer hochgeladen werden muss, erlaube der Chrome-Erweiterung in Chrome den Zugriff auf Datei-URLs:

1. Klicke in Chrome auf das Erweiterungssymbol in der Symbolleiste und dann auf **Erweiterungen
   verwalten**.
2. Klicke auf der Karte der Erweiterung auf **Details**.
3. Aktiviere **Zugriff auf Datei-URLs zulassen**.

Starte die Chrome-Aufgabe erneut, nachdem du die Einstellung geändert hast.
