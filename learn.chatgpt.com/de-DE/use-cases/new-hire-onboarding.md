<!-- source: https://learn.chatgpt.com/de-DE/use-cases/new-hire-onboarding -->

## Einführung

Für das Onboarding neuer Mitarbeitender kommen meist mehrere Systeme zum Einsatz: eine Liste bestätigter Neueinstellungen, ein Onboarding-Tracker, Zuordnungen zu Führungskräften oder Teams, der Bereitstellungsstatus von Konten und Ausstattung, Kalendermeilensteine und die Chatbereiche der Teams, in denen die erste Woche koordiniert wird.

ChatGPT kann dabei helfen, diesen Workflow zu koordinieren. Bitte ChatGPT, die Kohorte für einen bestimmten Startzeitraum zu erfassen, Tracker-Aktualisierungen vorzubereiten, die Gruppe nach Teams zusammenzufassen und die Einrichtung von Willkommensbereichen in einem prüfbaren Paket zu entwerfen. Der erste Durchlauf sollte ohne Schreibzugriff erfolgen. Genehmige Schreibvorgänge, Einladungen, Beiträge, Direktnachrichten, E-Mails oder die Erstellung von Kanälen erst ausdrücklich, nachdem du den genauen Aktionsplan geprüft hast.

## Rahmen für die Prüfung festlegen

Bevor ChatGPT etwas liest oder schreibt, lege den Personenkreis, die Quellsysteme, die zulässigen Felder, die zu erstellenden Artefakte, die prüfenden Personen und die ausgeschlossenen Aktionen fest.

Das ist wichtig, weil Onboarding-Daten sensibel sein können. Beschränke den Workflow auf praktische Onboarding-Angaben wie bevorzugter Name, Rolle, einstellendes Team, Führungskraft, bei Bedarf geschäftliche E-Mail-Adresse, Startdatum, Zeitzone oder ungefährer Arbeitsort, Buddy, Bereitstellungsstatus von Konto und Ausstattung, Meilensteine der Einarbeitung und offene Fragen.

Nimm keine Angaben zu Vergütung, demografischen Merkmalen, amtlichen Identifikationsnummern, Privatadressen, medizinischen Themen oder Behinderungen, zum Status von Hintergrundprüfungen oder zur Einwanderung sowie kein Feedback aus Vorstellungsgesprächen und keine Leistungshinweise in den Prompt oder den generierten Tracker auf.

## Freigegebene Onboarding-Daten zusammentragen

Beginne mit der verbindlichen Quelle, die deine Organisation bereits für die Onboarding-Koordination freigegeben hat. Das kann ein Recruiting-Export, ein HR-Export, eine Tabelle, ein Projekt-Tracker, eine von einer Führungskraft bereitgestellte Tabelle, ein Verzeichnisexport oder ein kleiner eingefügter Beispieldatensatz sein.

Bitte ChatGPT, die gelesenen Quellen, Zeilenanzahlen, den Datumsbereich, die Feldnamen und die ausgewählten Spalten anzugeben, bevor es einen Tracker erstellt. Tabellenzellen, Dokumente, Chat-Nachrichten und Datensätze sollte es als zusammenzufassende Daten behandeln, nicht als auszuführende Anweisungen.

## Onboarding-Tracker erstellen

Ein Tracker lässt sich am einfachsten prüfen, wenn ChatGPT Angaben aus den Quellen von generierten Planungsfeldern trennt.

Quellspalten können beispielsweise Name, Team, Führungskraft, Rolle, Startdatum, geschäftliche E-Mail-Adresse und Startort enthalten. Planungsspalten können die zuständigen Personen für Konto und Ausstattung, den Einführungstermin, den Status des Willkommensbereichs, den Buddy, den Vorbereitungsstatus, fehlende Angaben und die nächste Aktion enthalten.

Bitte ChatGPT, den Tracker zunächst in einer neuen CSV-Datei, Tabelle, Markdown-Tabelle oder einem Entwurfs-Tab vorzubereiten, bevor es einen operativen Tracker aktualisiert. Prüfe die Zeilen, das Ziel der Freigabe und die Fragen zu fehlenden Feldern, bevor du einen Schreibvorgang genehmigst.

## Teamzusammenfassungen und Willkommensbereiche entwerfen

Sobald der Tracker-Entwurf korrekt ist, soll ChatGPT die Kommunikation in der Reihenfolge vorbereiten, in der eine koordinierende Person sie prüfen würde:

1. Eine Zusammenfassung für jedes Team mit Personenzahlen, Startdaten, Führungskräften und Lücken beim Vorbereitungsstand.
2. Namen für private Willkommensbereiche gemäß deiner freigegebenen Namenskonvention.
3. Einladungslisten, zuständige Personen, Themen, Lesezeichen, Willkommensnachrichten und Checklistenpunkte für die erste Woche in jedem Bereich.
4. Text für den Ankündigungskanal, der keine unnötigen personenbezogenen Angaben enthält.

In dieser Phase sollten alle Ausgaben weiterhin Entwürfe sein. Kanalnamen können Rückschlüsse auf die Identität oder den Beschäftigungsstatus zulassen, und Einladungen können Personen sofort benachrichtigen. Die Erstellung, Einladungen, Beiträge, Direktnachrichten, E-Mails und Schreibvorgänge im Tracker dürfen erst nach einer ausdrücklichen Genehmigung erfolgen.

## Wöchentlichen Onboarding-Workflow ausführen

Teile einen wiederkehrenden Onboarding-Durchlauf in Prüfpunkte auf:

1. **Bestandsaufnahme:** Lies nur die von dir angegebenen Quellen, ermittle Personen, deren Startdatum im Zielzeitraum liegt, und melde fehlende oder widersprüchliche Daten.
2. **Vorbereitung:** Erstelle Entwürfe für den Tracker, die Teamzusammenfassung, den Plan für Willkommensbereiche, die Einladungsliste und die Nachrichten.
3. **Review:** Bestätige die Kohorte, den Ziel-Tracker, Datum oder Status und Zielgruppe der Ankündigung, die Namenskonvention für Willkommensbereiche, die Sichtbarkeitseinstellung der Bereiche, die Einladungslisten und jede Nachricht.
4. **Ausführen:** Nachdem du deine Genehmigung ausdrücklich erteilt hast, bitte ChatGPT, ausschließlich die geprüften Aktionen auszuführen.
5. **Bericht:** Liefere Links zu den erstellten Artefakten, Anzahlen je Aktion, ungeklärte Lücken und die als Nächstes zuständigen Personen. Füge die vollständige Personalliste nur ein, wenn du sie in der abschließenden Zusammenfassung benötigst.

## Prompt-Vorschläge

Mit den folgenden Prompts bereitest du die Arbeit in getrennten Durchläufen vor. Wenn dein Team eine gemeinsame Projektseite oder eine Kurzinfo für Führungskräfte nutzt, bitte ChatGPT, den geprüften Tracker, die Zusammenfassung und den Plan für Willkommensbereiche in diesem Entwurf zu bündeln, bevor du Aktionen in externen Systemen genehmigst.

**Kohorte für den Startzeitraum erfassen**

**Tracker und Teamzusammenfassung vorbereiten**

**Einrichtung der Willkommensbereiche entwerfen**

**Onboarding-Paket zusammenstellen**

**Nur die genehmigten Aktionen ausführen**
