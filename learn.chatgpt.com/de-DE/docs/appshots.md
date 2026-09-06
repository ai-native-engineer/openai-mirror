<!-- source: https://learn.chatgpt.com/de-DE/docs/appshots -->

Mit Appshots kannst du das App-Fenster im Vordergrund zu einem Chat in ChatGPT hinzufügen. Verwende sie, wenn
du gerade in einer anderen App auf deinem Computer arbeitest und
ChatGPT deinen aktuellen Kontext geben möchtest, damit es dich bei der Aufgabe unterstützen kann.

  Appshots sind in der ChatGPT-Desktop-App unter macOS verfügbar. Drücke beide Befehlstasten
oder deine eigene Appshots-Tastenkombination, um einen Appshot aufzunehmen.

## Was Appshots erfassen

Ein Appshot erfasst nur das Fenster im Vordergrund. Er kann Folgendes enthalten:

- Ein Bild des sichtbaren Fensters.
- Verfügbarer Text aus diesem Fenster, darunter sichtbarer Text und Text, den die App
außerhalb des sichtbaren Scrollbereichs zur Verfügung stellt.

Nachdem du einen Appshot zu einem Chat hinzugefügt hast, wird er wie ein Anhang behandelt. ChatGPT
speichert Appshots lokal in der Sitzungsdatei, ebenso wie Dateien oder Bilder, die du manuell
anhängst.

## Wann du Appshots verwenden solltest

Verwende Appshots, wenn ChatGPT Kontext aus einer Mac-App benötigt, bevor es eine Aktion ausführen kann.

Beispiele:

- Teile eine Seite der API-Referenz und bitte ChatGPT, ein Skript zu schreiben, das die API verwendet.
- Teile eine E-Mail- oder Kalenderansicht und bitte ChatGPT, den nächsten Schritt auszuarbeiten.
- Teile einen Bildeditor, ein Design oder ein Vorschaufenster und bitte ChatGPT, die
zugehörigen Assets oder den Code zu überarbeiten.
- Teile einen Fehler, ein Einstellungsfenster oder einen App-Zustand, wenn sich das leichter zeigen als
beschreiben lässt.

## Appshot aufnehmen

1. Bringe das App-Fenster, das du teilen möchtest, in den Vordergrund.
2. Drücke beide Befehlstasten oder die Tastenkombination, die du in ChatGPT
unter „Einstellungen“ konfiguriert hast.
3. Erteile die macOS-Berechtigungen, wenn ChatGPT dich dazu auffordert.
4. Bitte ChatGPT, mithilfe des Appshots eine Aufgabe auszuführen.

  

Standardmäßig startet ChatGPT für den Appshot einen neuen Chat. Wenn du in den letzten 60 Sekunden in einem
Chat aktiv warst, fügt ChatGPT den Appshot stattdessen diesem zuletzt verwendeten
Chat hinzu. Wenn du mehrere Appshots nacheinander aufnimmst, werden sie demselben Chat hinzugefügt.

Du kannst die Appshots-Tastenkombination in den Einstellungen der App ändern.

## Berechtigungen und Sicherheit

ChatGPT fragt möglicherweise nach Berechtigungen, bevor es Appshots aufnehmen kann:

- Mit **Bildschirm- & Systemaudioaufnahme** kann ChatGPT ein Bild des
  Fensters im Vordergrund aufnehmen.
- Mit **Bedienungshilfen** kann ChatGPT den verfügbaren Text aus dem Fenster im Vordergrund lesen.

Wenn du einen Appshot aufnimmst, teilst du das erfasste Bild und den verfügbaren Text mit ChatGPT.
Nimm keine Appshots mit sensiblen Inhalten auf, es sei denn, die Aufgabe erfordert diese
Inhalte.

Prüfe bei Appshots genauso sorgfältig wie bei Screenshots und Dokumenten,
ob du sie mit ChatGPT teilen möchtest.

## Einschränkungen und Fehlerbehebung

Appshots sind in der ChatGPT-Desktop-App unter macOS verfügbar. Wenn du einen Chat
in der CLI fortsetzt, der bereits einen Appshot enthält, bleibt der Anhang Teil des
Chatverlaufs, aber die CLI kann keinen neuen Appshot erstellen.

Bei einigen Apps und Websites, darunter Google Docs, Gmail, Google Sheets und
Google Slides, erhält ChatGPT unter Umständen nur den sichtbaren Screenshot und nicht
den vollständigen Dokumentinhalt oder Text außerhalb des sichtbaren Bereichs. In ChatGPT Work oder Codex kann ChatGPT ein
passendes installiertes Plug-in verwenden, um auf die relevanten Inhalte der App zuzugreifen und dich bei deiner
Anfrage zu unterstützen.

Wenn Appshots nicht funktionieren:

1. Öffne **Systemeinstellungen \> Datenschutz & Sicherheit**.
2. Prüfe unter **Bildschirm- & Systemaudioaufnahme** und **Bedienungshilfen** die Berechtigungen für Codex
   bei der Computernutzung.
3. Starte die App neu und versuche es noch einmal.
