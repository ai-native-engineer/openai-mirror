<!-- source: https://learn.chatgpt.com/de-DE/docs/computer-use -->

In unterstützten Regionen ist die Computernutzung in der ChatGPT-Desktop-App unter macOS und Windows mit ChatGPT Work und Codex verfügbar. Installiere das Plug-in für die Computernutzung. Erteile unter macOS die Berechtigungen für Bildschirmaufnahme und Bedienungshilfen, wenn du dazu aufgefordert wirst.

Mit der Computernutzung kann ChatGPT grafische Benutzeroberflächen unter macOS oder Windows sehen und bedienen. Nutze sie für Aufgaben, bei denen Kommandozeilentools oder strukturierte Integrationen nicht ausreichen, etwa um eine Desktop-App zu überprüfen, einen Browser zu verwenden, App-Einstellungen zu ändern, mit einer Datenquelle zu arbeiten, für die kein Plug-in verfügbar ist, oder einen Fehler zu reproduzieren, der nur in einer grafischen Benutzeroberfläche auftritt.

Die Computernutzung kann den Zustand von Apps und des Systems auch außerhalb deines Projekt-Workspace beeinflussen. Nutze sie deshalb für klar begrenzte Aufgaben und prüfe Berechtigungsanfragen, bevor du fortfährst.

## Computernutzung einrichten

Wähle in der ChatGPT-Desktop-App ChatGPT aus und wechsle im Umschalter zu Work oder wähle
Codex aus. Öffne **Plug-ins \>
Computernutzung** und wähle **Plug-in installieren** aus, wenn du dazu aufgefordert wirst. Wenn die Option **„Aktivieren“** angezeigt wird,
wähle sie aus. Aktiviere die Schalter für den Server und den Skill der Computernutzung und wähle zum Starten **Jetzt
ausprobieren** aus.

  

Öffne dann **Einstellungen \> Computernutzung** , um den App-Zugriff zu prüfen. Die Bedienelemente für verbundene Browser
zeigen die Aktion **Verwalten** . Apps, die du für zukünftige Aufgaben genehmigst, erscheinen im
Abschnitt **Immer zugelassene Apps** .

  

Lass unter Windows die Ziel-App auf dem aktiven Desktop sichtbar, während die Aufgabe ausgeführt wird. Erteile unter macOS die Berechtigungen für Bildschirmaufnahme und Bedienungshilfen, wenn du dazu aufgefordert wirst, damit ChatGPT die Ziel-App sehen und mit ihr interagieren kann.

Erteile unter macOS folgende Berechtigungen:

- **Bildschirmaufnahme** , damit ChatGPT die Ziel-App sehen kann.
- **Bedienungshilfen** , damit ChatGPT klicken, Text eingeben und navigieren kann.

## Wann die Computernutzung sinnvoll ist

Wähle für schwierige Aufgaben, die Screenshots oder eine visuelle Beurteilung erfordern,
[GPT-6 Astra](/de-DE/codex/models#gpt-6-astra), sofern es in deiner Modellauswahl
verfügbar ist. Es gelten dasselbe Plug-in-Setup, dieselben Betriebssystemberechtigungen und dieselben
Kontrollen für den App-Zugriff.

Wähle die Computernutzung, wenn die Aufgabe eine grafische Benutzeroberfläche erfordert, die sich allein anhand von Dateien oder Befehlsausgaben nur schwer überprüfen lässt.

Geeignete Anwendungsfälle sind:

- Testen einer macOS-App, einer Windows-App, eines Ablaufs im iOS-Simulator oder einer anderen Desktop-App, die ChatGPT entwickelt.
- Ausführen einer Aufgabe, für die dein Webbrowser erforderlich ist.
- Reproduzieren eines Fehlers, der nur in einer grafischen Benutzeroberfläche auftritt.
- Ändern von App-Einstellungen, die sich nur über Klicks in einer Benutzeroberfläche anpassen lassen.
- Prüfen von Informationen in einer App oder Datenquelle, auf die nicht über ein Plug-in zugegriffen werden kann.
- Ausführen einer klar begrenzten Aufgabe unter macOS im Hintergrund, während du an anderer Stelle weiterarbeitest.
- Ausführen eines Ablaufs, der mehrere Apps umfasst.

Verwende für Web-Apps, die du lokal entwickelst, zuerst den
[integrierten Browser](/de-DE/codex/browser?surface=app).

### Nutzung im Vordergrund unter Windows

Unter Windows wird die Computernutzung auf dem aktiven Desktop ausgeführt. Sie kann nicht im Hintergrund arbeiten, während du dieselbe Windows-Sitzung weiterverwendest. Rechne daher damit, dass ChatGPT den Zeiger bewegt, Text eingibt und während der Aufgabe die Steuerung im Vordergrund übernimmt.

Wenn Windows-Aufgaben weiterlaufen sollen, während du nicht am Gerät bist, lass das
Windows-Gerät entsperrt und mit dem Internet verbunden. Nutze die
[Fernsteuerung](/de-DE/codex/remote-connections) auf deinem Smartphone, um den Fortschritt zu prüfen
oder weitere Anweisungen zu senden. Alternativ kannst du die ChatGPT-Desktop-App in einer virtuellen Windows-Maschine
ausführen, damit die Computernutzung die VM statt deines Haupt-Desktops übernimmt.

## Eine Aufgabe mit Computernutzung starten

Erwähne `@Computer` oder `@AppName` in deinem Prompt oder bitte ChatGPT, die Computernutzung
zu verwenden. Beschreibe genau, welche App oder welches Fenster ChatGPT bedienen oder welchen Ablauf es ausführen soll.

```text
Open the app with Computer Use, reproduce the onboarding bug, and fix the
smallest code path that causes it. After each change, run the same UI flow
again.

```text
Open @Chrome and verify the checkout page still works after the latest changes.

Wenn die Ziel-App ein eigenes Plug-in oder einen MCP-Server bereitstellt, verwende für den Datenzugriff und wiederholbare Vorgänge vorzugsweise diese strukturierte Integration. Wähle die Computernutzung, wenn ChatGPT die App visuell prüfen oder bedienen muss.

## Berechtigungen und Genehmigungen

Die Workspace-Administration kann einschränken, auf welche Apps die Computernutzung zugreifen kann und
ob Genehmigungen gespeichert werden dürfen. Siehe
[zentral verwaltete Kontrollen für Browser und Computernutzung](/de-DE/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Systemberechtigungen für die Computernutzung sind von App-Genehmigungen in ChatGPT getrennt. Unter macOS ermöglichen die Berechtigungen für Bildschirmaufnahme und Bedienungshilfen ChatGPT, Apps zu sehen und zu bedienen. App-Genehmigungen legen fest, welche Apps ChatGPT verwenden darf. Das Lesen und Bearbeiten von Dateien sowie das Ausführen von Shell-Befehlen unterliegen weiterhin den Sandbox- und Genehmigungseinstellungen der Aufgabe.

Mit der Computernutzung kann ChatGPT nur die von dir zugelassenen Apps sehen und darin Aktionen ausführen.
Während einer Aufgabe fragt ChatGPT nach deiner Genehmigung, bevor es eine App auf deinem Computer
verwenden kann. Du kannst **Immer zulassen** wählen, damit ChatGPT diese App künftig
ohne erneute Nachfrage verwenden kann. Du kannst Apps aus der Liste **Immer zulassen** entfernen. Du findest sie im
Abschnitt **Computernutzung** in den Einstellungen der ChatGPT-Desktop-App.

  
    
  

ChatGPT kann auch vor sensiblen oder störenden Aktionen eine Genehmigung anfordern.

Wenn ChatGPT eine App nicht sehen oder steuern kann, öffne unter macOS **Systemeinstellungen \> Datenschutz &
Sicherheit** und überprüfe die Berechtigungen **Bildschirmaufnahme** und **Bedienungshilfen** für **Codex
Computernutzung** . Stelle unter Windows sicher, dass die Ziel-App in der
aktiven Desktop-Sitzung sichtbar ist.

Unter Windows speichert die Computernutzung dauerhafte Entscheidungen zu Apps in
`$CODEX_HOME/config.toml`. Führe die Apps auf, die die Computernutzung ohne
Nachfrage öffnen darf:

```toml
[computer_use.windows]
always_allowed_app_ids = ["mspaint.exe"]

Verwende die App-Kennung, die die Computernutzung unter Windows meldet, etwa den Namen
der ausführbaren Datei einer Desktop-App oder eine App User Model ID für eine paketierte App. ChatGPT
fragt bei Apps nach, die nicht in der Liste stehen. Um eine gespeicherte Entscheidung zu widerrufen, entferne
die App unter **Einstellungen \> Computernutzung \> Immer zulassen**.

Diese Tabelle speichert lokale Entscheidungen zur Computernutzung. Sie ist von der
administrativ vorgegebenen Datei `requirements.toml` getrennt, in der die Administration die Computernutzung
mit `[features].computer_use = false` deaktivieren kann. Ältere Einträge der Zulassungsliste aus
`$CODEX_HOME/computer-use/config.toml` werden in die
aktuelle Einstellung migriert. Die Liste `denied` aus dieser älteren Datei ist nicht Teil des aktuellen Richtlinienschemas.

## Nutzung im Sperrzustand

  Die Nutzung im Sperrzustand ist für macOS vorgesehen. Unter Windows arbeitet die Computernutzung im Vordergrund.

Die Nutzung im Sperrzustand ermöglicht ChatGPT die Computernutzung auch nach dem Sperren deines Mac, allerdings erst, nachdem du sie aktiviert hast. Verwende sie, wenn eine ChatGPT-Aufgabe nach dem Sperren des Mac von einem verbundenen Gerät aus auf Desktop-Apps zugreifen muss.

Wenn du die Nutzung im Sperrzustand aktivierst, installiert ChatGPT ein von Apple vorgesehenes
[Autorisierungs-Plug-in](https://developer.apple.com/documentation/security/authorization-plug-ins),
das am Entsperrvorgang von macOS beteiligt ist.

Die Nutzung im Sperrzustand ist bewusst eng begrenzt. Sie ist keine allgemeine Möglichkeit, deinen Mac aus der Ferne zu entsperren, und erlaubt weder anderen Apps noch lokalen Prozessen, den Computer zu entsperren.

So verwendest du die Nutzung im Sperrzustand:

1. Öffne in der App **Einstellungen \> Computernutzung** .
2. Aktiviere die Nutzung im Sperrzustand.
3. Starte von einem verbundenen Gerät aus eine Aufgabe mit Computernutzung, nachdem der Bildschirm deines Mac gesperrt wurde.

Wenn eine ChatGPT-Aufgabe nach dem Sperren deines Mac über die Computernutzung auf eine App zugreift, entsperrt ChatGPT den Mac vorübergehend. Dabei blockiert ChatGPT die lokale Nutzung und erhält den Schutz des Sperrbildschirms aufrecht. Vor dem Entsperren prüft ChatGPT, ob der Entsperrversuch zu einem aktiven, vertrauenswürdigen Vorgang der Computernutzung gehört. Außerhalb dieses kurzen Zeitfensters verweigert ChatGPT das Entsperren und fordert dich bei Bedarf auf, den Mac manuell zu entsperren.

Die Nutzung im Sperrzustand umfasst folgende Schutzmaßnahmen:

- Die Autorisierung gilt nur für ein kurzes Zeitfenster und ist auf den aktuellen Entsperrversuch beschränkt.
- Die automatische Entsperrung ist nur für ChatGPT und nur während aktiver Vorgänge der Computernutzung verfügbar.
- Während der Desktop vorübergehend entsperrt ist, verdeckt ChatGPT alle Bildschirme.
- Wenn ChatGPT lokale Tastatur- oder Zeigereingaben erkennt, sperrt es den Mac erneut und setzt die automatische Entsperrung aus, bis du ihn manuell entsperrst.

## Sicherheitshinweise

Mit der Computernutzung kann ChatGPT Bildschirminhalte einsehen, Screenshots erstellen und in der Ziel-App Fenster und Menüs bedienen, Tastatureingaben vornehmen und auf die Zwischenablage zugreifen. Behandle sichtbare App-Inhalte, Browserseiten, Screenshots und in der Ziel-App geöffnete Dateien als Kontext, den ChatGPT während der Ausführung der Aufgabe verarbeiten kann.

Begrenze Aufgaben klar und bleibe bei sensiblen Abläufen anwesend:

- Gib ChatGPT jeweils genau eine App oder einen Ablauf als klares Ziel vor.
- Du kannst die Aufgabe jederzeit stoppen oder die Steuerung deines Computers übernehmen.
- Lass Apps mit sensiblen Inhalten geschlossen, sofern sie für die Aufgabe nicht erforderlich sind.
- Rechne unter Windows damit, dass ChatGPT während der Ausführung die Eingaben im Vordergrund übernimmt. Verwende ein zweites Gerät oder eine VM oder stoppe die Aufgabe, bevor du diesen Desktop selbst nutzt.
- Vermeide Aufgaben, die vertrauliche Daten erfordern, es sei denn, du bist dabei und kannst jeden Schritt genehmigen.
- Prüfe Berechtigungsanfragen für Apps, bevor du ChatGPT die Verwendung einer App erlaubst.
- Wähle **Immer erlauben** nur für Apps aus, die ChatGPT deiner Einschätzung nach bei
  künftigen Aufgaben bedenkenlos automatisch verwenden darf.
- Bleib dabei, wenn es um Einstellungen zu Konto, Sicherheit, Datenschutz, Netzwerk, Zahlungen oder Anmeldedaten geht.
- Brich die Aufgabe ab, wenn ChatGPT beginnt, mit dem falschen Fenster zu interagieren.

Wenn ChatGPT deinen Browser verwendet, kann es mit Seiten interagieren, auf denen du bereits angemeldet bist. Prüfe Aktionen auf Websites so, als würdest du sie selbst ausführen: Webseiten können schädliche oder irreführende Inhalte enthalten, und Websites können genehmigte Klicks, Formularübermittlungen und Aktionen im angemeldeten Zustand deinem Konto zuordnen. Damit du deinen Browser weiter nutzen kannst, während ChatGPT arbeitet, bitte ChatGPT, einen anderen Browser zu verwenden.

Die Funktion kann weder Terminal-Apps noch ChatGPT selbst automatisieren, da eine solche Automatisierung die Sicherheitsrichtlinien von ChatGPT umgehen könnte. Sie kann sich außerdem nicht mit Administratorrechten authentifizieren oder Berechtigungsanfragen für Sicherheit und Datenschutz auf deinem Computer genehmigen.

Dateiänderungen und Shell-Befehle unterliegen weiterhin den Genehmigungs- und Sandbox-Einstellungen von ChatGPT, soweit diese anwendbar sind. Änderungen über Desktop-Apps erscheinen im Review-Bereich möglicherweise erst, wenn sie auf dem Datenträger gespeichert und vom Projekt erfasst wurden. Deine Datenkontrollen in ChatGPT gelten für Inhalte, die über ChatGPT verarbeitet werden. Dazu gehören auch Screenshots, die bei der Computernutzung aufgenommen werden.
