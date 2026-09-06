<!-- source: https://learn.chatgpt.com/de-DE/use-cases/ios-app-intents -->

## Die richtigen Teile deiner App für das System sichtbar machen

App Intents gehören zu den naheliegendsten Möglichkeiten, eine iOS-App auch außerhalb ihrer eigenen Benutzeroberfläche nützlicher zu machen. Behandle deine App nicht wie ein in sich geschlossenes System, das erst funktioniert, nachdem jemand sie gestartet und durch mehrere Ansichten navigiert hat. Nutze Codex stattdessen, um die Aktionen und Objekte für Kurzbefehle, Siri, Spotlight, Widgets, Steuerelemente und neuere assistenzgestützte Systemfunktionen verfügbar zu machen.

Das verbessert schon heute die Auffindbarkeit und Automatisierung und bereitet die App zugleich auf eine Zukunft vor, in der Assistenten eine größere Rolle spielen. Wenn deine App bereits nützliche Funktionen zum Verfassen, Öffnen, Filtern, Weiterleiten oder Zusammenfassen bietet, ermöglichen App Intents dem System, diese Funktionen strukturiert anzufordern.

## Beginne mit Aktionen und Entitäten, nicht mit jedem Bildschirm

Beim ersten Durchgang mit App Intents ist es meist keine gute Idee, „die gesamte App nachzubilden“. Bitte Codex, Folgendes zu ermitteln:

- die wenigen Aktionen, die Nutzende auslösen möchten, ohne durch die gesamte Benutzeroberfläche zu navigieren
- die App-Objekte, die das System verstehen muss, um diese Aktionen korrekt weiterzuleiten
- die Arbeitsabläufe, bei denen sich die App in einem bestimmten Zustand öffnen soll, im Gegensatz zu denen, die direkt in einem Systembereich abgeschlossen werden sollen

Die Hinweise von Apple zu App Intents bieten dafür einen guten Rahmen: Definiere die Aktion und die vom System benötigte Entitätsebene. Sorge anschließend dafür, dass diese Aktionen in verschiedenen Systemfunktionen auffindbar und wiederverwendbar sind. Besonders hilfreich sind die Referenzen [Aktionen und Inhalte auffindbar und allgemein verfügbar machen](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-and-widely-available), [Deinen ersten App Intent erstellen](https://developer.apple.com/documentation/appintents/creating-your-first-app-intent) und das Beispiel für Systemfunktionen [App Intents zur Unterstützung von Systemfunktionen einsetzen](https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences).

## Denke in Systembereichen, nicht nur in Kurzbefehlen

Die Möglichkeiten gehen über „einen Kurzbefehl hinzufügen“ hinaus. Eine gut gestaltete Schnittstelle für App Intents kann deine App an mehreren Stellen nützlich machen:

- Kurzbefehle, mit denen Nutzende Aktionen direkt ausführen oder zu größeren Automatisierungen kombinieren können
- Siri, wo die App aussagekräftige Verben und Deep Links bereitstellen kann, statt sich nur ohne bestimmtes Ziel öffnen zu lassen
- Spotlight, wo App-Entitäten und App-Kurzbefehle zu auffindbaren Einstiegspunkten ins System werden
- Widgets, Live-Aktivitäten, Steuerelemente und andere Intent-gesteuerte Benutzeroberflächen
- neuere, auf Assistenten ausgelegte Funktionen, bei denen strukturierte Aktionen und Entitäten für das System wesentlich leichter verständlich sind als beliebige Abläufe in der Benutzeroberfläche

## Nutze ein praxistaugliches App-Muster

Das funktioniert meist am besten, wenn die App etwa so strukturiert ist:

- ein eigenes Target für App Intents, statt Intent-Typen über nicht zusammengehörige App-Dateien zu verteilen
- Einträge in `AppShortcutsProvider` für besonders nützliche Aktionen wie das Verfassen eines Beitrags oder das Öffnen der App auf einem bestimmten Tab
- kleine, auf `AppEntity` basierende Typen für Objekte, die das System verstehen muss, etwa Konten, Listen und Timeline-Filter
- eine Intent-Verarbeitung mit sauberer Weiterleitung zurück in die Hauptszene der App, damit ein aufgerufener Intent den richtigen Erstellungsablauf öffnen oder zum richtigen Tab wechseln kann

Dieses Muster würde ich Codex für die meisten Apps vorgeben: Beginne mit einer kleinen, auf das System ausgerichteten Aktionsebene, halte die Entitätsebene schlank und richte eine vorhersehbare Übergabe zur Laufzeit zurück an die App ein, wenn der Intent die Hauptbenutzeroberfläche benötigt.

## Bitte Codex, die erste Intent-Schnittstelle zu entwerfen

Ein besonders guter Prompt nennt Codex die zentralen Objekte und wichtigsten Aktionen deiner App. Anschließend fordert er Codex auf, die kleinste sinnvolle erste Schnittstelle für App Intents auszuwählen, statt blind alles verfügbar zu machen.

## Praktische Tipps

### Mache die Aktionen verfügbar, die Nutzende außerhalb der App wirklich ausführen möchten

Gute erste Intents sind meist Aktionen wie Verfassen, Öffnen, Suchen, Filtern, Starten, Fortsetzen oder Prüfen. Wenn eine Aktion erst nach einem langen Einrichtungsablauf innerhalb der App nützlich ist, gehört sie möglicherweise nicht in den ersten Durchgang mit App Intents.

### Halte Entitäten schlanker als deine Modellschicht

Das System benötigt in der Regel nicht dein vollständiges Persistenzmodell. Bitte Codex, die kleinstmögliche App-Entitätsebene zu definieren, die Siri, Kurzbefehle und Spotlight dennoch genug Kontext bietet, um die Aktion korrekt weiterzuleiten und darzustellen.

### Betrachte dies als Infrastruktur für Assistenten, nicht nur als Funktion für Kurzbefehle

Auch wenn mit deiner ersten Version zunächst nur Verbesserungen in Shortcuts oder Siri sichtbar werden, liegt der größere Vorteil darin, dass deine App ihre Funktionen nun über strukturierte Aktionen und Entitäten ausdrückt. Dadurch kann sie künftig leichter über systemseitige und KI-gesteuerte Einstiegspunkte genutzt werden als eine App, deren Funktionen nur in Tippinteraktionen und Ansichtshierarchien abgebildet sind.
