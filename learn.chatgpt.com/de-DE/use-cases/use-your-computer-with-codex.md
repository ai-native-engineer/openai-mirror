<!-- source: https://learn.chatgpt.com/de-DE/use-cases/use-your-computer-with-codex -->

## Einführung

Nutze die [Computernutzung](/de-DE/docs/computer-use), wenn sich eine Aufgabe über Desktop-Apps, Fenster oder lokale Dateien erstreckt. ChatGPT kann in den von dir freigegebenen Apps klicken, Text eingeben und navigieren. Anschließend erhältst du das Ergebnis zur Überprüfung. Starte für eine Website oder eine angemeldete Browsersitzung eine separate Browseraufgabe mit `@Chrome`.

**Für die Computernutzung ist die ChatGPT-Desktop-App erforderlich.** In unterstützten Regionen ist die Computernutzung unter macOS und Windows in ChatGPT Work und Codex verfügbar. Cloud-Aufgaben in Work können im Web oder auf Mobilgeräten nicht direkt auf deine lokalen Apps, Dateien oder angemeldeten Desktop-Browsersitzungen zugreifen. Du kannst eine Desktop-Aufgabe über [Remote auf Mobilgeräten](/de-DE/codex/remote-connections) starten oder steuern, wenn du einen Mac- oder Windows-Host verbindest.

Du kannst beispielsweise Notizen in ein führendes System übertragen, vor dem Entwerfen einer Antwort den Kontext in mehreren Apps prüfen oder freigegebene Angaben zwischen Tools kopieren, für die es kein eigenes Plug-in gibt.

So kann es aussehen, wenn du eine Desktop-Aufgabe sicher übergibst und deine Pläne für ein Hüttenwochenende in „Nachrichten“ und „Notizen“ stehen:

<div data-use-case-export-only>

**Desktop-Aufgabe:** Ideen für ein Hüttenwochenende aus „Nachrichten“ und einer Hüttenauswahl in „Notizen“ zusammentragen, eine lokale Notiz erstellen und eine Antwort entwerfen.

**Ergebnis:** Pine Lodge ist stufenlos zugänglich, innerhalb von zwei Stunden erreichbar und kostet insgesamt 690 USD. Lake House kommt möglicherweise infrage, aber Fahrzeit und Barrierefreiheit müssen noch bestätigt werden. Cedar Ridge scheidet wegen der Treppen aus. Da die Gruppengröße noch unbekannt ist, steht der Preis pro Person unter Vorbehalt.

Die lokale Notiz und der Antwortentwurf können jetzt überprüft werden. Es wurde nichts gebucht oder gesendet.

</div>

## Verwendung

1. Öffne die ChatGPT-Desktop-App und installiere das [Plug-in für die Computernutzung](/de-DE/docs/computer-use).
2. Beginne deine Anfrage für Desktop-Apps mit `@Computer` oder für Browseraufgaben mit `@Chrome`.
3. Beschreibe die Aufgabe, die beteiligten Apps oder Dateien und das gewünschte Ergebnis.
4. Prüfe Zugriffsanfragen und halte vor Aktionen inne, bei denen wichtige Daten gesendet, übermittelt oder geändert werden.
5. Halte unter Windows die Ziel-App sichtbar, während die Computernutzung aktiv ist.

Wenn es für eine App ein Plug-in gibt, kann ChatGPT dieses für die strukturierte Aktion verwenden. Die Computernutzung eignet sich, wenn die Aufgabe von der App-Oberfläche abhängt oder kein Plug-in verfügbar ist.

## Ideen zum Ausprobieren

Beginne mit einem Tool: Verwende `@Computer` für Desktop-Apps und lokale Dateien oder `@Chrome` für deinen Browser. ChatGPT kann bei Bedarf weitere Tools auswählen.

**Nachrichten in einen Plan verwandeln**

**Unterkünfte finden**

**Den aktuellen Stand eines Projekts erfahren**

**Einen Tracker anhand von Besprechungsnotizen aktualisieren**

**Im Browser mit aktiver Anmeldung arbeiten**

**Eine Website testen**

**Lokale Dateien aufräumen**

**Zeige ChatGPT, was du gerade ansiehst**

Verwende unter macOS einen [Appshot](/de-DE/codex/appshots), um das App-Fenster im Vordergrund zu teilen. Appshots liefern visuellen Kontext. Wenn du es erlaubst, kann die Computernutzung die App anschließend öffnen, prüfen und bedienen.

## Praktische Tipps

### So läuft die Aufgabe auf jedem Computer ab

Unter macOS kann die Computernutzung im Hintergrund laufen, während du andere Apps verwendest. Eine Bild-in-Bild-Vorschau zeigt die aktive App. Öffne die Vorschau, um die Ausführung mitzuverfolgen, oder verschiebe sie, wenn sie im Weg ist. Wenn du einen Begleiter verwendest, kannst du die Vorschau dorthin verschieben.

Unter Windows läuft die Computernutzung auf dem aktiven Desktop und übernimmt die Bedienung im Vordergrund. Rechne damit, dass sich während der Aufgabe der Mauszeiger bewegt und Tastatureingaben erfolgen. Lass das Gerät entsperrt und verbunden. Wenn du deinen Haupt-Desktop weiter nutzen möchtest, führe die Desktop-App in einer virtuellen Windows-Maschine aus.

### Den richtigen Browser auswählen

Aufgaben im Browser gehören oft zur Computernutzung. Wähle den Browser, der über den benötigten Kontext verfügt:

- **[Chrome-Erweiterung](/de-DE/codex/chrome-extension):** Verwende `@Chrome` für Aufgaben im Browser, etwa für die Suche nach Angeboten, den Zugriff auf Websites oder die Nutzung deines bereits angemeldeten Chrome-Profils, deiner Tabs oder Erweiterungen.
- **[Integrierter Browser](/de-DE/codex/browser?surface=app):** Verwende ihn, wenn du für localhost oder öffentliche Websites eine separate Browsersitzung benötigst. Er verfügt über einen eigenen Browserzustand und kann warten, während du dich anmeldest.
- **Cloud-Browser in ChatGPT Work im Web oder auf Mobilgeräten:** Verwende ihn für unterstützte, öffentlich zugängliche Websites ohne Anmeldung. Er hat keinen Zugriff auf lokale Dateien, geöffnete Tabs, Erweiterungen oder gespeicherte Passwörter und kann sich weder bei Websites anmelden noch Zahlungen abschließen.

Nenne den Browser im Prompt, wenn es darauf ankommt, und lege wiederkehrende Desktop-Einstellungen unter [Anpassung](/de-DE/docs/customization/overview) fest.

### Parallele Ausführungen in derselben App vermeiden

Führe nicht zwei Aufgaben mit der Computernutzung gleichzeitig in derselben App aus. Konkurrierende Aktionen können das aktuelle Fenster oder den Zustand der App verändern und das Ergebnis unzuverlässig machen.

### Anmeldung bei Apps und Nutzung im gesperrten Zustand vorbereiten

Bevor du eine Desktop-Aufgabe startest, melde dich bei den benötigten Apps und Diensten an. Unter macOS kannst du die [Nutzung im gesperrten Zustand](/de-DE/docs/computer-use#locked-use) aktivieren, damit unterstützte Aufgaben auch nach dem Sperren des Mac weiterlaufen. Ohne diese Option endet die Computernutzung, sobald der Mac gesperrt wird. Unter Windows ist die Nutzung im gesperrten Zustand für die Computernutzung nicht verfügbar.
