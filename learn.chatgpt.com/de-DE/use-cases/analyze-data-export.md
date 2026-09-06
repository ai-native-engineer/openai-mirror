<!-- source: https://learn.chatgpt.com/de-DE/use-cases/analyze-data-export -->

## Bevor du beginnst

Hänge eine CSV-Datei oder Tabelle an oder verbinde Google Drive und füge die exakte URL von Google Drive oder Google Sheets in den Chat ein. Sites kann aus diesen Quellen ein privates, interaktives Dashboard erstellen, ohne es zu veröffentlichen oder deine Daten öffentlich zugänglich zu machen.

Du kannst das Dashboard in ChatGPT Work im Browser oder in der Desktop-App erstellen. Damit eine geplante Prüfung auch bei ausgeschaltetem Laptop weiterläuft, musst du die Aufgabe im Browser starten. Für eine Aufgabe über die Desktop-App muss dein Computer eingeschaltet sein und die Desktop-App muss laufen.

## Das erwartet dich

ChatGPT prüft die Quelldaten, erstellt ein Dashboard und zeigt die den Diagrammen zugrunde liegenden Zahlen. Dieses Beispiel verwendet fiktive Vertriebsexporte pro Quartal, eine Zuordnung der Kundensegmente und eine beispielhafte Dashboard-Vorschau. Es unterscheidet zwischen der größten absoluten Veränderung in USD und der größten prozentualen Veränderung und weist auf eine Bestellung hin, die keinem Kundensegment zugeordnet werden kann.

<div data-use-case-export-only>

### Beispiel-Dashboard

| Kundensegment | Q1-Umsatz | Q2-Umsatz |         Veränderung |
| ---------------- | ---------: | ---------: | -------------: |
| Unternehmen       |     3.000 USD |     2.450 USD | -550 USD (-18,3 %) |
| Mittelstand       |     1.000 USD |     1.170 USD |   +170 USD (+17 %) |
| KMU              |       400 USD |       520 USD |   +120 USD (+30 %) |

Im Segment Unternehmen war die absolute Veränderung in USD am größten, bei KMU die prozentuale Veränderung. Eine Bestellung aus Q2 im Wert von 160 USD konnte keinem Kundensegment zugeordnet werden und wurde aus den Summen der Segmente ausgeschlossen. Das private Dashboard enthält ein Vergleichsdiagramm, Filter für Segment und Datum, Angaben zur Aktualität der Quelle sowie die zugrunde liegenden Berechnungen.

Wenn ChatGPT die Quelle jeden Werktagmorgen prüfen soll, aktualisiert es das Dashboard, sobald sich die freigegebenen Daten ändern, und weist auf wesentliche Änderungen oder fehlende Datensätze hin. Ohne Genehmigung veröffentlicht oder teilt es das Dashboard nicht.

</div>

## So funktioniert es

- **Quelle verbinden:** Hänge einen Vertriebsexport oder eine Tabelle an oder füge den exakten Link zu einem freigegebenen Google Sheet oder einer freigegebenen Datei in Google Drive ein. ChatGPT prüft die Spalten, Datumsangaben und Kundendatensätze, bevor es Schlussfolgerungen zieht.
- **Dashboard erstellen:** Sites wandelt die Ergebnisse in ein privates, interaktives Dashboard mit Diagrammen, Filtern, Angaben zur Aktualität der Quelle und den zugehörigen Berechnungen um.
- **Aktuell halten:** Eine geplante Aufgabe in ChatGPT Work prüft die freigegebene Quelle an jedem Werktag und aktualisiert das Dashboard, wenn sich die Daten ändern. Die Site selbst führt den Zeitplan nicht aus.
- **Nur auf Wichtiges hinweisen:** Bitte ChatGPT, auf ungewöhnliche Änderungen, fehlende Datensätze oder Entscheidungen hinzuweisen, die überprüft werden müssen. Wenn sich nichts Wichtiges ändert, soll es keine Meldung senden.
- **Vor dem Teilen überprüfen:** Prüfe zuerst das Dashboard. Bitte ChatGPT erst dann, es mit bestimmten Personen zu teilen, wenn du die Änderung der Zugriffsrechte genehmigt hast.

## Dashboard teilen

Nachdem du das Dashboard überprüft hast, bitte ChatGPT, es mit bestimmten Personen zu teilen oder für deinen Workspace verfügbar zu machen. Du kannst den Zugriff auch direkt in [Sites](https://chatgpt.com/sites) verwalten. Bitte ChatGPT, die aktuellen Freigabeeinstellungen anzuzeigen und auf deine Genehmigung zu warten, bevor es Personen einlädt, das Dashboard veröffentlicht oder seine Sichtbarkeit ändert.

Informationen zu Freigabeoptionen und Workspace-Zugriff findest du in der [Sites-Dokumentation](/de-DE/codex/sites).

## Weitere Möglichkeiten

**Ändere, was das Dashboard erfasst**

**Eine gezieltere Benachrichtigung einrichten**

**Ein wöchentliches Update vorbereiten**
