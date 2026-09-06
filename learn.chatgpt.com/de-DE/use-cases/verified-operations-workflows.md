<!-- source: https://learn.chatgpt.com/de-DE/use-cases/verified-operations-workflows -->

## Nachvollziehbare Vorgänge ausführen

Wenn du regelmäßig wiederholbare Vorgänge ausführen musst, etwa um einer Person Zugriff zu gewähren, ein Batch-Update anzuwenden oder ein Skript mit unterschiedlichen Parametern aufzurufen, kannst du sie mit ChatGPT automatisieren und erhältst eine nachvollziehbare Ausgabe.

Nutze diesen Arbeitsablauf, wenn ChatGPT einen wiederholbaren Vorgang ausführen und dir anhand eines Artefakts nachweisen soll, was dabei geschehen ist.

## Aufgabe und Eingaben beschreiben

1. Stelle ChatGPT die Eingabetabelle, Dateien, Tickets oder eine andere Liste bereit, für deren Einträge es den Prozess als Batch ausführen soll.
2. Verweise gegebenenfalls auf die Quelle der Genehmigung oder auf die Richtlinie, die den zulässigen Umfang festlegt.
3. Teile ChatGPT mit, welches Skript, welche API, welcher Skill, welche CLI oder welcher App-Arbeitsablauf die Aufgabe ausführen soll.
4. Fordere optional einen Testlauf an, sofern der Arbeitsablauf dies unterstützt.
5. Bitte ChatGPT, den Batch-Vorgang auszuführen und für jedes Element eine Zeile mit Erfolg oder Fehler zu erfassen.

Grenze den Umfang eng ein und weise ChatGPT an, den Vorgang nur auszuführen, wenn alle erforderlichen Eingaben vorliegen.
Fehlt in einer Zeile ein Pflichtfeld, soll ChatGPT diese Zeile kennzeichnen, statt eine Angabe zu erraten.

Verbinde die Tools, mit denen du den Vorgang ausführst, über [Plug-ins](/de-DE/codex/plugins), etwa dein Ticketsystem oder deine Tabelle mit den Listeneinträgen.

## Nachweis zur Überprüfung des Ergebnisses anfordern

Zu einer sinnvollen Ausführung gehört ein Ergebnis, das sich von dir oder anderen im Team prüfen lässt, etwa eine CSV-Datei, eine Protokolldatei, ein Dashboard-Link, ein Screenshot, ein PR-Check oder ein anderer Nachweis für die erfolgreiche Ausführung. In der ChatGPT-Desktop-App kannst du nach der Ausführung [generierte Dateien öffnen und prüfen](/de-DE/codex/artifacts-viewer), um das Ergebnis zu verifizieren.

## Aus der Ausführung einen wiederverwendbaren Arbeitsablauf erstellen

Bitte ChatGPT nach der ersten erfolgreichen Ausführung darum, die wiederholbaren Bestandteile festzuhalten. Bei gängigen Arbeitsabläufen kann daraus ein [Skill](/de-DE/codex/build-skills) oder eine [geplante Aufgabe](/de-DE/codex/automations) werden.

Erstelle für geplante Vorgänge erst dann eine geplante Aufgabe, wenn die manuelle Ausführung zuverlässige Ergebnisse liefert. Belasse sensible Aktionen, die Zugriffsrechte oder Daten dauerhaft verändern könnten, ausschließlich im Entwurfsstatus, sofern du nicht ausdrücklich möchtest, dass ChatGPT sie ausführt.
