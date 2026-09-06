<!-- source: https://learn.chatgpt.com/de-DE/docs/notifications -->

Benachrichtigungen informieren dich, wenn etwas deine Aufmerksamkeit erfordert. Welche Steuerelemente und
Zustellungskanäle verfügbar sind, hängt von der jeweiligen Oberfläche ab.

## Desktop-Benachrichtigungen konfigurieren

Öffne [**Einstellungen**](codex://settings), um festzulegen, wann Benachrichtigungen nach Abschluss eines Durchlaufs
angezeigt werden: nie, nur wenn ChatGPT im Hintergrund ausgeführt wird oder immer. Mit separaten
Steuerelementen kannst du Benachrichtigungen zu Berechtigungen und Fragen ein- oder ausschalten. Dein
Betriebssystem fordert dich möglicherweise auf, der Desktop-App von ChatGPT
die Berechtigung zum Senden von Benachrichtigungen zu erteilen.

### Chats in der Ansicht „Aktivität“ verfolgen

Wenn **Aktivität** verfügbar ist, wähle in der Seitenleiste das Glockensymbol aus, um Chats anzuzeigen,
die ungelesen sind, gerade ausgeführt werden oder auf deine Antwort warten. Du kannst die Ansicht „Aktivität“ außerdem öffnen oder
schließen: mit <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>U</kbd> unter macOS
oder mit <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>U</kbd> unter Windows.

Lege über die Optionen der Ansicht fest, welche Chats angezeigt werden. Je nach aktueller
Oberfläche können die Optionen **Work**, **Chat**, **Angeheftet** und
**Geplant** umfassen. Du kannst außerdem **Alle als gelesen markieren** auswählen, um ungelesene Einträge als gelesen zu markieren.

<a id="follow-task-activity-with-a-pet"></a>

### Chat-Aktivitäten mit einem Begleiter verfolgen

In der Desktop-App von ChatGPT kannst du Chat-Aktivitäten alternativ mit einem schwebenden Begleiter verfolgen,
während du in anderen Apps arbeitest. Er kann den Status eines Chats anzeigen: **Wird ausgeführt**,
**Eingabe erforderlich**, **Bereit** oder **Blockiert**.

Auf der Seite [Begleiter](/de-DE/codex/pets?surface=app) erfährst du, wie du einen Begleiter auswählst, seinen Status verstehst oder
einen eigenen erstellst.

## Web-Benachrichtigungen konfigurieren

Öffne **Einstellungen \> Benachrichtigungen**, um die für dein Konto verfügbaren Kategorien und
Kanäle für Benachrichtigungen zu verwalten. Je nach Kategorie und Konto
können Push-Benachrichtigungen, E-Mail oder SMS als Kanäle verfügbar sein. Wähle in den Einstellungen für Aufgabenbenachrichtigungen **Aufgaben verwalten** aus,
um **Geplant** zu öffnen.

## CLI-Benachrichtigungen konfigurieren

Informationen zu Benachrichtigungen im Terminal und über externe Programme findest du unter
[Benachrichtigungen](/de-DE/codex/config-file/config-advanced#notifications) im
Leitfaden zur erweiterten Konfiguration. Du kannst festlegen, wann die TUI eine Benachrichtigung sendet
und ob Codex nach Abschluss eines Durchlaufs ein externes Programm ausführt.

<a id="follow-task-activity-in-the-ide"></a>

## Chat-Aktivitäten in der IDE verfolgen

Die IDE-Erweiterung bietet keine separaten Einstellungen für Benachrichtigungen. Lass den
Chat geöffnet, um seine Aktivität zu verfolgen. Wenn nach Abschluss eines Durchlaufs ein externes Programm ausgeführt werden soll,
konfiguriere `notify` auf dem verbundenen Codex-Host. Weitere Informationen findest du unter
[Benachrichtigungen](/de-DE/codex/config-file/config-advanced#notifications) im
Leitfaden zur erweiterten Konfiguration.

## Weitere Dokumentation

- [Lang laufende Aufgaben](/de-DE/codex/long-running-work)
- [Geplante Aufgaben](/de-DE/codex/automations)
- [Begleiter](/de-DE/codex/pets)
