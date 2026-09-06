<!-- source: https://learn.chatgpt.com/de-DE/docs/image-generation -->

Bitte ChatGPT, Bilder zu generieren oder zu bearbeiten. Nutze die Bildgenerierung für UI-Assets,
Banner, Hintergründe, Illustrationen, Sprite-Sheets und Platzhalter, die du
zusammen mit Code oder in einem ChatGPT-Chat erstellen möchtest.

Fordere im Editor der App ein Bild an. Füge ein Referenzbild hinzu, wenn
ChatGPT ein vorhandenes Asset umgestalten oder als visuelle Orientierung verwenden soll.

### Generierte Bilder prüfen und bearbeiten

Wähle ein generiertes Bild aus, um die erweiterte Bildansicht zu öffnen. Wechsle zwischen
der **Fokusansicht**, um ein einzelnes Bild zu prüfen, und der **Canvas-Ansicht**, um die
im selben Chat generierten Bilder zu sehen.

Verwende in der **Canvas-Ansicht** die Option **Kommentieren**, um präzises Feedback zu einem oder mehreren
Bildern zu geben. Wähle **Mehrfachauswahl**, um die gewünschten Bilder auszuwählen, und
sende dann deine Kommentare und weitere Bearbeitungsanweisungen im selben Chat.
Beschreibe, was sich ändern und was unverändert bleiben soll.

Fordere in einem Chat in der Webversion von ChatGPT ein Bild an. Füge im
Editor ein Referenzbild hinzu, wenn ChatGPT es bearbeiten oder als visuelle Orientierung verwenden soll.

Beschreibe das Bild in einer interaktiven Sitzung oder füge `$imagegen` ein, um
den Skill zur Bildgenerierung explizit aufzurufen. Hänge mit `-i` oder
`--image` ein vorhandenes Bild an, wenn es als Orientierung für das Ergebnis dienen soll.

Fordere im Chat der Erweiterung ein Bild an. Ziehe ein Referenzbild in
den Editor und halte dabei <kbd>Shift</kbd> gedrückt, wenn Codex ein vorhandenes Asset bearbeiten
oder darauf aufbauen soll.

## Ein Bild generieren oder bearbeiten

Beschreibe das Bild in natürlicher Sprache. Füge ein Referenzbild hinzu, wenn
ChatGPT ein vorhandenes Asset umgestalten oder erweitern soll.

Füge `$imagegen` in deinen Prompt ein, um den Skill zur Bildgenerierung
explizit aufzurufen.

Die integrierte Bildgenerierung verwendet `gpt-image-2` und wird auf deine allgemeinen
Codex-Nutzungslimits angerechnet. Bildgenerierungen verbrauchen das enthaltene Nutzungskontingent
je nach Bildqualität und -größe im Durchschnitt 3- bis 5-mal schneller als vergleichbare Interaktionen
ohne Bildgenerierung. Lege für größere Mengen `OPENAI_API_KEY` in deiner Umgebung fest und bitte
ChatGPT, Bilder über die API zu generieren. Dann gelten die API-Preise.

Ob die Bildgenerierung in der Webversion von ChatGPT verfügbar ist und welche Nutzungslimits gelten, hängt von deinem Tarif und den
Workspace-Einstellungen ab. Verwende für die programmatische Bildgenerierung die [API zur
Bildgenerierung](/api/docs/guides/image-generation).

## Effektive Bild-Prompts schreiben

Ein guter Bild-Prompt besteht oft nur aus ein bis drei klaren Sätzen. Beschreibe die
Details, auf die es für ein gelungenes Ergebnis ankommt:

- Beschreibe den Zweck des Bildes oder nenne die Zielgruppe.
- Nenne das Hauptmotiv und beschreibe, was geschieht.
- Beschreibe die Szenerie, die Komposition und den visuellen Stil.
- Gib bei Bedarf Bildausschnitt, Abmessungen, Beleuchtung, Farben oder Materialien an.
- Gib Einschränkungen an und nenne alles, was das Bild nicht enthalten darf.

Verwende konkrete visuelle Beschreibungen statt allgemeiner Wertungen. Beschreibe zum Beispiel,
woher das Licht kommt, anstatt um „schöne Beleuchtung“ zu bitten. Wiederhole jede
Anforderung, die unverändert bleiben muss.

## Ergebnis verfeinern

Beginne mit der Grundidee und nimm dann kleine, gezielte Anpassungen vor. Ändere jeweils nur
ein Element, damit sich die Komposition und andere wichtige Details nicht ungewollt verändern.
Du kannst außerdem einen bestimmten Bereich eines Bildes auswählen und die gewünschte Änderung für diesen
Bereich beschreiben.

Beschreibe beim Bearbeiten eines vorhandenen Bildes genau, was sich ändern und was
unverändert bleiben soll.

Formuliere das Feedback bei umfassenderen Überarbeitungen direkt und konkret: Mache das Bild
heller, reduziere die Farbsättigung, vereinfache den Hintergrund oder behalte die
Komposition bei und ändere dabei den Stil.

## Mehrere Referenzbilder verwenden

Verwende eine kleine Auswahl an Referenzbildern, wenn ein Bild den Inhalt und
ein anderes den Stil, das Layout oder eine andere visuelle Ausrichtung vorgibt. Bezeichne die einzelnen
Bilder anhand ihrer Reihenfolge und erkläre, wie sie zusammenhängen. Verwende beim Kombinieren von Elementen räumliche Angaben wie
Vordergrund, Hintergrund, links und rechts.

## Text zu einem Bild hinzufügen

Halte Text im Bild kurz und gib ihn genau vor. Setze den exakten Wortlaut in
Anführungszeichen, behalte die gewünschte Groß- und Kleinschreibung bei und beschreibe Schriftstil,
Schriftgröße, Farbe und Platzierung. Buchstabiere ungewöhnliche Namen,
wenn es auf Genauigkeit ankommt. Gib an, ob weiterer Text erlaubt ist.

## Infografiken und inhaltsreiche Layouts erstellen

Die Bildgenerierung kann dir bei Entwürfen für Erklärgrafiken, Poster, beschriftete Diagramme,
Zeitleisten und andere informationsreiche Visualisierungen helfen. Beschreibe die
Informationshierarchie und das Layout, halte Beschriftungen knapp und fordere eine gestochen scharfe Textdarstellung an.
Prüfe bei umfangreichen Texten oder produktionskritischer Typografie jedes Wort und stelle
das Asset bei Bedarf in einem Design-Tool fertig.

## Weitere Hinweise

- **Gehe mit Darstellungen realer Personen sorgsam um.** Wenn du eine reale Person abbildest, füge gegebenenfalls ein
  Referenzfoto hinzu und vergewissere dich, dass du die Erlaubnis hast,
  ihr Abbild zu verwenden.
- **Bitte um eine eigenständige Umsetzung.** Fordere ein generisches oder eigenständiges Design an,
  statt eine bestimmte Marke, ein Produkt, den Stil bestimmter Kunstschaffender oder ein Kunstwerk zu imitieren.
- **Die Nennung von OpenAI ist optional.** Bei generierten Bildern musst du OpenAI nicht nennen,
  kannst aber erläutern, wie ein Asset erstellt wurde, wenn dieser Kontext hilfreich ist.
- **Halte dich an geltende Richtlinien.** Verwende Bilder gemäß den Richtlinien deiner
  Organisation sowie den [Nutzungsrichtlinien
  von OpenAI](https://openai.com/policies/usage-policies/).

## Weiterführende Dokumentation

- [Preise für Codex](/de-DE/codex/pricing#image-generation-usage-limits)
- [Bildeingaben](/de-DE/codex/image-inputs)
- [API-Leitfaden zur Bildgenerierung](/api/docs/guides/image-generation)
- [Mit Dateien arbeiten](/de-DE/codex/artifacts-viewer)
- [Bilder mit ChatGPT erstellen](https://openai.com/academy/image-generation/)

  
    <span slot="icon">
      
    </span>
    Entdecke weitere Prompts und Ergebnisse zur Bildgenerierung.
  

- [Bildeingaben](/de-DE/codex/image-inputs)
- [API-Leitfaden zur Bildgenerierung](/api/docs/guides/image-generation)
- [Mit Dateien arbeiten](/de-DE/codex/artifacts-viewer)
- [Bilder mit ChatGPT erstellen](https://openai.com/academy/image-generation/)

  
    <span slot="icon">
      
    </span>
    Entdecke weitere Prompts und Ergebnisse zur Bildgenerierung.
  

- [Preise für Codex](/de-DE/codex/pricing#image-generation-usage-limits)
- [Bildeingaben](/de-DE/codex/image-inputs)
- [API-Leitfaden zur Bildgenerierung](/api/docs/guides/image-generation)
- [Mit Dateien arbeiten](/de-DE/codex/artifacts-viewer)

  
    <span slot="icon">
      
    </span>
    Entdecke weitere Prompts und Ergebnisse zur Bildgenerierung.
