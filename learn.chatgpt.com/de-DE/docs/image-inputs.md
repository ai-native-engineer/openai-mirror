<!-- source: https://learn.chatgpt.com/de-DE/docs/image-inputs -->

Füge einem Prompt Bilder hinzu, wenn die Aufgabe visuellen Kontext erfordert, etwa einen
Fehler-Screenshot, ein Oberflächendesign, ein Architekturdiagramm oder ein vorhandenes Asset. Erkläre,
was ChatGPT untersuchen soll und welches Ergebnis du erwartest. Verlasse dich nicht allein auf das Bild,
um die Aufgabe zu vermitteln.

Halte <kbd>Shift</kbd> gedrückt und ziehe ein Bild in den Prompt-Editor, um es
als Kontext hinzuzufügen. Du kannst ChatGPT auch bitten, ein Bild auf deinem System zu untersuchen, oder
ein Screenshot-Tool verwenden, um deine Arbeit in einer anderen App zu überprüfen.

Hänge im ChatGPT Web-Editor ein Bild an, füge es ein oder ziehe es hinein. Teile ChatGPT im Prompt mit,
was es untersuchen und welches Ergebnis es anhand des Bildes liefern soll.

Füge ein Bild in den interaktiven Editor ein oder übergib eine oder mehrere Dateien über die
Befehlszeile:

```bash
codex -i screenshot.png "Explain this error and suggest the smallest fix"
codex --image before.png,after.png "Compare these states and list the regressions"

Trenne bei mehreren Bildern die Pfade durch Kommas oder gib `--image` mehrfach an. Codex
akzeptiert gängige Bildformate wie PNG und JPEG.

Halte <kbd>Shift</kbd> gedrückt und ziehe ein Bild in den Prompt-Editor, damit die
Erweiterung das Bild übernimmt, statt es an den Editor weiterzugeben.

## Formuliere den Prompt passend zum Bild

Beschreibe, was das Bild zeigt, weise auf den relevanten Bereich hin und gib die gewünschte Ausgabe
sowie die geltenden Vorgaben an. Wenn du mehr als ein Bild anhängst, kennzeichne jedes Bild eindeutig und erkläre,
wie ChatGPT sie vergleichen soll.

Zum Beispiel:

```text
Compare this checkout screen with the design. Fix spacing and typography only;
do not change behavior. Verify the result with a new screenshot.

## Verwende die passende Bildfunktion

Verwende eine Bildeingabe, wenn ChatGPT eine visuelle Referenz untersuchen soll. Verwende
[Bildgenerierung](/de-DE/codex/image-generation), wenn ChatGPT ein Bild
erstellen oder bearbeiten soll.
