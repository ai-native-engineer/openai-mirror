<!-- source: https://learn.chatgpt.com/de-DE/use-cases/learn-a-new-concept -->

## Einführung

Ein neues Konzept anhand einer anspruchsvollen Forschungsarbeit oder eines Kurses zu verstehen, erfordert mehr als eine bloße Zusammenfassung. Ziel ist ein tragfähiges mentales Modell. Dazu musst du verstehen, welches Problem behandelt wird, was die Methode tatsächlich leistet, welche Belege sie stützen, auf welchen Annahmen sie beruht und welche Aspekte du noch untersuchen musst.

ChatGPT ist hier hilfreich, weil es automatisch Kontext zusammentragen und komplizierte Konzepte mit hilfreichen Diagrammen oder Illustrationen verständlich machen kann. Dieser Anwendungsfall eignet sich außerdem gut für [Subagenten](/de-DE/codex/agent-configuration/subagents): Ein Thread kann die Struktur der Forschungsarbeit erfassen, ein weiterer das erforderliche Vorwissen zusammentragen und ein dritter Abbildungen und Notation untersuchen. Der Haupt-Thread kann die Ergebnisse anschließend abgleichen und in einem Bericht zusammenführen, den du später prüfen kannst.

Für diesen Anwendungsfall sollte das Endergebnis leicht zu prüfen sein: eine Markdown-Datei wie `notes/concept-report.md` oder ein Dokument in einem anderen Format. Es sollte eine Zusammenfassung, ein Glossar, eine schrittweise Erläuterung, Diagramme, eine Evidenztabelle, Einschränkungen und offene Fragen enthalten und nicht bei einer flüchtigen Chat-Antwort bleiben.

## Lernziel festlegen

Benenne zunächst das Konzept und das gewünschte Ergebnis. Eine eng gefasste Frage macht den Bericht hilfreicher als eine allgemeine Zusammenfassung.

Zum Beispiel:

> Ich möchte verstehen, worin die zentrale Idee dieser Forschungsarbeit besteht, wie die Methode funktioniert, warum die Experimente die Aussage stützen oder nicht und was ich als Nächstes lesen sollte.

Dieser Rahmen gibt ChatGPT eine konkrete Aufgabe. Es soll dir das Konzept erklären, zugleich aber Unsicherheiten kenntlich machen, die Herkunft von Aussagen belegen und die Aussagen der Forschungsarbeit von ChatGPTs eigener Interpretation trennen.

## Fortlaufendes Beispiel: Analyse einer Forschungsarbeit

Angenommen, du möchtest dich anhand einer Forschungsarbeit mit einer dir unbekannten Modellarchitektur vertraut machen. Du möchtest einen Bericht, mit dem du das Konzept auf einen Blick erfassen kannst, ohne die gesamte Forschungsarbeit lesen zu müssen.

Ein gutes Ergebnis könnte so aussehen:

- `notes/paper-report.md` mit der zentralen Erläuterung.
- `notes/figures/method-flow.mmd` oder ein direkt eingebettetes Mermaid-Diagramm zur Methode.
- `notes/figures/concept-map.mmd` oder eine kleine SVG-Datei, die zeigt, wie die erforderlichen Grundlagen zusammenhängen.
- Eine Evidenztabelle, die Aussagen den entsprechenden Abschnitten, Seiten, Abbildungen oder Tabellen der Forschungsarbeit zuordnet.
- Eine Liste mit weiterführender Literatur und ungeklärten Fragen.

Ziel ist es, den Lernprozess systematischer zu gestalten und ein dauerhaft nutzbares Ergebnis zu schaffen.

## Arbeit auf Subagenten aufteilen

Subagenten arbeiten am besten, wenn sie jeweils eine klar abgegrenzte Aufgabe und ein eindeutiges Rückgabeformat haben. Fordere ChatGPT ausdrücklich auf, sie zu starten. ChatGPT muss nicht für jede Leseaufgabe Subagenten verwenden, doch bei langen oder konzeptionell anspruchsvollen Forschungsarbeiten hilft eine parallele Bearbeitung.

Für eine Forschungsarbeit ist folgende Aufteilung sinnvoll:

- **Übersicht der Forschungsarbeit:** Erfasse die Problemstellung, den Beitrag, die Methode, die Experimente und die Einschränkungen sowie die Ergebnisse, die der Forschungsarbeit zufolge erzielt wurden.
- **Erforderliches Vorwissen:** Erkläre Hintergrundbegriffe, verwandte Konzepte und frühere Arbeiten, deren Kenntnis die Forschungsarbeit voraussetzt.
- **Notation und Abbildungen:** Gehe Gleichungen, Algorithmen, Diagramme, Abbildungen und Tabellen Schritt für Schritt durch.
- **Kritische Prüfung:** Prüfe, ob die Belege die Aussagen stützen, nenne Vorbehalte und ermittle fehlende Baselines oder unklare Annahmen.

Der Hauptagent sollte auf diese Subagenten warten, ihre Antworten vergleichen und Widersprüche auflösen. Anschließend führt ChatGPT die Ergebnisse zu einem schlüssigen Bericht zusammen.

## Zusätzlichen Kontext gezielt zusammentragen

Wenn die Forschungsarbeit Wissen voraussetzt, das dir fehlt, bitte ChatGPT, Kontext aus freigegebenen Quellen zusammenzutragen. Dafür kommen lokale Notizen, ein Ordner mit Literaturangaben, verlinkte Forschungsarbeiten, die Websuche (sofern aktiviert) oder eine angebundene Wissensdatenbank infrage.

Wenn du dich in ein internes Konzept einarbeitest, kannst du mit [Plug-ins](/de-DE/codex/plugins) mehrere Quellen zu einer Wissensdatenbank verbinden.

Grenze diesen Schritt klar ein. Teile ChatGPT mit, was als verlässliche Quelle gilt und wie der fertige Bericht mit externem Kontext umgehen soll:

- Definiere die vorausgesetzten Begriffe in einem Glossar.
- Füge einen kurzen Abschnitt „Nötiges Vorwissen“ hinzu.
- Verlinke weiterführende Literatur getrennt von den Aussagen der Forschungsarbeit.
- Kennzeichne Aussagen, die aus Quellen außerhalb der Forschungsarbeit stammen.

## Diagramme für den Bericht erstellen

An Diagrammen erkennst du oft am schnellsten, ob du ein Konzept wirklich verstanden hast. Bitte ChatGPT für einen Markdown-Bericht um Diagramme, die sich eng am Quellenmaterial orientieren und leicht überarbeiten lassen.

Bewährt haben sich:

- Eine Konzeptübersicht, die erforderliche Grundlagen und ihre Zusammenhänge zeigt.
- Ein Ablaufdiagramm der Methode, das Eingaben, Transformationen, Modellkomponenten und Ausgaben nachzeichnet.
- Eine Übersicht der Experimente, die Datensätze, Metriken, Baselines und die in der Forschungsarbeit formulierten Aussagen miteinander verknüpft.
- Ein Diagramm zu den Einschränkungen, das Annahmen, Fehlermodi und offene Fragen voneinander abgrenzt.

Bitte ChatGPT für Berichte mit Markdown als primärem Format um Mermaid-Diagramme, wenn das Zielsystem sie unterstützt, andernfalls um eine kleine, ins Repository eingecheckte SVG- oder PNG-Datei. Der System-Skill imagegen ist standardmäßig in ChatGPT enthalten. Bitte ChatGPT nur dann, ihn zu verwenden, wenn du eine anschauliche, nicht detailgetreue Grafik benötigst oder sich etwas nicht in einem nativen Markdown-Diagramm darstellen lässt.

## Markdown-Bericht verfassen

Bitte ChatGPT, den Bericht so in sich geschlossen zu verfassen, dass du später wieder darauf zurückgreifen kannst. Eine sinnvolle Struktur ist:

1. Kurzfassung.
2. Was du vor dem Lesen wissen solltest.
3. Schlüsselbegriffe und Notation.
4. Schrittweise Erläuterung der Forschungsarbeit.
5. Methodendiagramm.
6. Evidenztabelle.
7. Was die Forschungsarbeit nicht belegt.
8. Offene Fragen und weiterführende Literatur.

Der Bericht sollte, wo immer möglich, Quellenangaben enthalten. Bitte ChatGPT bei einer PDF-Datei um Verweise auf Seiten, Abschnitte, Abbildungen oder Tabellen. Wenn ChatGPT keine genauen Seitenangaben extrahieren kann, sollte es darauf hinweisen und stattdessen auf Abschnitte oder Überschriften verweisen.

## Nutze den Bericht für iteratives Lernen

Der erste Bericht ist nur ein Ausgangspunkt. Stelle nach dem Lesen Anschlussfragen und lass ChatGPT den Bericht überarbeiten.

Sinnvolle Anschlussfragen sind:

- Welchen Teil dieser Methode sollte ich zuerst verstehen?
- Was ist das einfachste Beispiel, das die Kernidee veranschaulicht?
- Welche Abbildung ist für die Argumentation der Forschungsarbeit am wichtigsten?
- Welche Aussage ist am schwächsten oder am wenigsten belegt?
- Was sollte ich als Nächstes lesen, wenn ich das implementieren möchte?

Wenn das Konzept Experimente erfordert, bitte ChatGPT, ein kleines Notebook oder Skript hinzuzufügen, das die Idee anhand eines vereinfachten Beispiels nachbildet. Verlinke das Notebook oder Skript im Markdown-Bericht, damit Erklärung und Experiment zusammenbleiben.

Beispiel-Prompt:

## Geeignete Skills

Verwende Skills nur, wenn sie zum gewünschten Artefakt passen:

- `$jupyter-notebook` für vereinfachte Beispiele, Diagramme oder einfache Reproduktionen, die ausführbar sein sollen.
- `$imagegen` für illustrative Grafiken, die keine exakten technischen Diagramme sein müssen.
- `$slides` für die Umwandlung des Berichts in eine Präsentation nach Abschluss der Lernphase.

Für die meisten Berichte zur Analyse von Forschungsarbeiten solltest du standardmäßig Markdown-native Diagramme oder einfache SVG-Dateien statt einer generierten Bitmap verwenden. Sie lassen sich leichter vergleichen, prüfen und aktualisieren, wenn sich dein Verständnis weiterentwickelt.

## Prompt-Vorschläge

**Zuerst die Berichtsgliederung erstellen**

**Diagramme zum Konzept erstellen**

**Aus dem Bericht einen Lernplan erstellen**
