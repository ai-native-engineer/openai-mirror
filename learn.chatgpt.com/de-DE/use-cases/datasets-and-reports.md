<!-- source: https://learn.chatgpt.com/de-DE/use-cases/datasets-and-reports -->

## Einführung

Im Kern geht es bei der Datenanalyse darum, mit Daten fundierte Entscheidungen zu treffen. Die Analyse ist kein Selbstzweck. Sie soll ein Arbeitsergebnis hervorbringen, das konkretes Handeln ermöglicht: ein Diagramm für die Führungsebene, die Auswertung eines Experiments für ein Produktteam, eine Modellbewertung für Forschende oder ein Dashboard, das die tägliche Arbeit unterstützt.

Ein nützlicher Ansatz, der durch _R for Data Science_ bekannt wurde, ist ein Kreislauf: Zuerst importierst und bereitest du die Daten auf. Dann wechselst du wiederholt zwischen Transformation, Visualisierung und Modellierung, um die Daten besser zu verstehen, bevor du die Ergebnisse vermittelst.

ChatGPT Work fügt sich gut in diesen Workflow ein. Es hilft dir, Daten zu bereinigen, Hypothesen zu untersuchen, Analysen zu erstellen und reproduzierbare Arbeitsergebnisse zu erzeugen. Ziel ist kein Notebook für den einmaligen Gebrauch, sondern eine Analyse, die andere prüfen, der sie vertrauen und die sie erneut ausführen können.

## Anwendungsfall definieren

Wähle eine konkrete Frage aus, die du mit deinen Daten beantworten möchtest. Je konkreter die Frage, desto leichter lassen sich die passenden Eingabedaten, Prüfungen und das gewünschte Ergebnis bestimmen.

### Durchgängiges Beispiel: Immobilienwerte in Autobahnnähe

Als Beispiel untersuchen wir die folgende Frage:

> In welchem Ausmaß werden Häuser in Autobahnnähe niedriger bewertet?

Angenommen, ein Datensatz enthält Immobilienwerte oder Verkaufspreise, ein anderer Angaben zu Lage, Flurstück oder Entfernung zur Autobahn. Die Aufgabe besteht nicht nur darin, ein Modell auszuführen. Du musst auch verlässliche Eingabedaten schaffen, die Joins dokumentieren und die Belastbarkeit des Ergebnisses kritisch prüfen. Am Ende soll ein Arbeitsergebnis stehen, das andere nutzen können.

Du kannst CSV-Dateien oder Excel-Arbeitsmappen anhängen, mit `@google-drive` eine freigegebene Google-Tabelle angeben oder die Desktop-App verwenden, wenn die Daten auf deinem Computer gespeichert sind.

<div data-use-case-export-only>

### Beispielergebnis

In einem fiktiven Beispiel gleicht ChatGPT 11 Immobilienverkäufe mit der Datei zu Autobahnentfernungen ab und kennzeichnet einen Verkauf ohne passende Entfernungsangabe. Häuser im Umkreis von einer Meile um die Autobahn haben einen Durchschnittswert von **500.000 USD**. Bei Häusern in zwei bis fünf Meilen Entfernung sind es **600.000 USD**.

Nachdem die teuerste weiter entfernte Immobilie ausgeschlossen wurde, beträgt der Unterschied weiterhin **94.000 USD**. Bericht und Diagramm machen deutlich, dass die Stichprobe klein ist, der Verkauf ohne zugehörige Entfernungsangabe ausgeschlossen wurde und der Vergleich weder einen Kausalzusammenhang belegt noch Faktoren wie Wohnviertel, Verkaufszeitpunkt, Verkehr oder Lärm berücksichtigt.

</div>

## Daten importieren

Hänge zunächst die Dateien an und bitte ChatGPT, sie zu prüfen. So lassen sich grundlegende, aber wichtige Fragen beantworten:

- Welche Dateiformate sind vorhanden?
- Was scheint der jeweilige Datensatz abzubilden?
- Welche Spalten kommen als Zielvariablen, Kennungen, Datums- oder Ortsangaben beziehungsweise Messgrößen infrage?
- Wo liegen eindeutige Qualitätsprobleme vor?

Frage noch nicht nach Schlussfolgerungen. Bitte zuerst um eine Bestandsaufnahme und Erläuterungen.

## Eingabedaten aufbereiten und zusammenführen

Hier beginnt meist die eigentliche Arbeit. Du hast zwei oder mehr Datensätze, der Primärschlüssel ist unklar und beim naiven Zusammenführen könnten Daten verloren gehen oder Duplikate entstehen.

Bitte ChatGPT, die geplante Zusammenführung vorab zu analysieren:

- Prüfe Schlüsselkandidaten auf Eindeutigkeit.
- Ermittle die Anteile von Nullwerten und Unterschiede in der Formatierung.
- Vereinheitliche offensichtliche Formatierungsunterschiede, etwa bei der Groß- und Kleinschreibung, bei Leerzeichen oder bei Adressen.
- Führe testweise Joins durch und gib die Übereinstimmungsquoten an.
- Empfiehl die sicherste Strategie für die Zusammenführung, bevor du die endgültige zusammengeführte Datei erstellst.

Wenn du den am besten geeigneten Schlüssel ableiten musst, beispielsweise eine normalisierte Adresse, eine aus mehreren Spalten gebildete Flurstückskennung oder eine räumliche Verknüpfung, bitte ChatGPT, die Abwägungen und Ausnahmefälle zu erläutern, bevor du die Zusammenführung akzeptierst.

## Daten mit Diagrammen untersuchen

Nutze Diagramme, um die Daten zu verstehen, bevor du dich für ein Modell entscheidest. Vergleiche im durchgängigen Beispiel Häuser in Autobahnnähe mit weiter entfernten Häusern, untersuche Ausreißer und Muster fehlender Werte und prüfe, ob der scheinbare Effekt auf die Zusammensetzung der Wohnviertel, die Wohnfläche oder einen anderen Faktor zurückgeht.

Stelle bei jedem Diagramm den Bezug zur ursprünglichen Frage her. Speichere die aussagekräftigen Vergleiche, damit andere die Analyse prüfen können.

## Die Fragestellung mit einem Modell untersuchen

Nicht jede Analyse braucht ein komplexes Modell. Beginne mit einem interpretierbaren Basismodell.

Für die Frage zur Autobahnnähe ist als erster Schritt eine Regression oder ein anderes transparentes Modell sinnvoll. Damit lässt sich der Zusammenhang zwischen der Nähe zur Autobahn und dem Immobilienwert schätzen, wobei relevante Faktoren wie Größe und Alter der Immobilie sowie ihre Lage berücksichtigt werden.

Bitte ChatGPT, folgende Punkte genau darzulegen:

- Die Definitionen der Zielvariablen und der Merkmale.
- Welche Kontrollvariablen berücksichtigt werden sollten und warum.
- Risiken durch Datenlecks sowie Ausschlüsse.
- Nach welchen Kriterien es die Datenaufteilung, die Evaluierungsmethode oder die Unsicherheitsschätzung ausgewählt hat.
- Was das Ergebnis in einfachen Worten bedeutet.

Wenn das erste Modell nur schwache Ergebnisse liefert, ist auch das nützlich. Das zeigt dir, ob das Problem am Modell, an den Merkmalen, an der Qualität der Datenverknüpfung oder an der Fragestellung selbst liegt.

## Das Ergebnis vermitteln

Die Analyse ist nur dann nützlich, wenn andere sie verwenden können. Lass ChatGPT das Artefakt erstellen, das die Zielgruppe benötigt:

- Ein Markdown-Memo für technische Mitwirkende.
- Eine Tabellenkalkulations- oder CSV-Datei zur Weiterverarbeitung.
- Ein formatiertes Dokument oder eine PDF-Datei für Entscheidungstragende.
- Ein Notebook, ein Dashboard oder ein statischer Bericht für eine wiederverwendbare Analyse.

Bitte ChatGPT, auch auf Einschränkungen hinzuweisen. Wenn die Qualität der Datenverknüpfung nicht optimal ist, eine Stichprobenverzerrung vorliegt oder die Modellannahmen wenig robust sind, sollte das Ergebnis dies klar benennen.

## Optional: eine Python-Umgebung einrichten

Wenn für das Projekt wiederverwendbare Skripte oder ein Notebook nötig sind, bitte ChatGPT, die vorhandene Python-Umgebung zu verwenden oder eine kleine, reproduzierbare Umgebung einzurichten. Lass die Quelldateien unverändert und speichere die Analyse, die Diagramme und den Abschlussbericht getrennt voneinander. Du musst Python nicht vorab einrichten, um angehängte Dateien in ChatGPT Work zu analysieren.

## Vorgeschlagene Prompts

**Datensätze laden und erläutern**

**Verknüpfung vorab prüfen**

**Ein erstes interpretierbares Modell erstellen**

**Ergebnisse für Stakeholder aufbereiten**
