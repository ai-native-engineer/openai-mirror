<!-- source: https://learn.chatgpt.com/de-DE/use-cases/frontend-designs -->

## Einführung

Wenn du Screenshots, eine kurze Designvorgabe oder einige Referenzen als Inspiration hast, kann Codex daraus eine responsive UI erstellen und dabei die bereits in deinem Projekt etablierten Muster berücksichtigen.

Mit dem Playwright-Skill kann Codex die App in einem echten Browser öffnen, die Implementierung bei verschiedenen Bildschirmgrößen mit deinen Screenshots abgleichen und Layout oder Verhalten so lange anpassen, bis das Ergebnis dem gewünschten Ziel näherkommt.

## Mit Vorlagen beginnen

Stelle Codex möglichst aussagekräftige Vorlagen für die gewünschte UI bereit. Für eine eng umrissene Aufgabe kann ein einzelner Screenshot genügen. Die Übergabe gelingt aber besser, wenn du mehrere Zustände einbeziehst, etwa Layouts für Desktop- und Mobilgeräte, Hover- oder Auswahlzustände sowie relevante Leer- oder Ladeansichten.

Die Vorlagen müssen keine perfekten Designunterlagen sein. Sie müssen die gewünschte Hierarchie, die Abstände und die gestalterische Richtung nur so konkret vermitteln, dass Codex nicht raten muss.

## Sei konkret

Je genauer du die erwarteten Interaktionsmuster und den gewünschten Stil beschreibst, desto besser wird das Ergebnis.
Das Modell greift tendenziell auf häufig verwendete Muster und Stile zurück. Wenn aus deinen Vorlagen nicht klar hervorgeht, dass du etwas anderes möchtest, wirkt die UI daher möglicherweise generisch.
Je mehr Informationen du bereitstellst, sei es durch weitere Referenzen zur Inspiration oder durch genauere Anweisungen, desto eher entsteht eine UI, die sich abhebt.

## Designsystem vorbereiten

Codex funktioniert am besten, wenn das Ziel-Repository bereits eine klar definierte Komponentenebene hat. Codex kann deine vorhandenen Komponenten und dein Designsystem automatisch verwenden, statt sie von Grund auf neu zu erstellen.

Falls nötig, etwa wenn du keinen Standard-Stack verwendest, teile Codex mit, welche Basiskomponenten wiederverwendet werden sollen, wo deine Tokens definiert sind und was im Repository für Buttons, Eingabefelder, Karten, Typografie und Symbole als maßgeblich gilt.

Wenn du mit einer vorhandenen Codebasis beginnst, erkennt Codex sehr wahrscheinlich selbst, wie deine Komponenten und dein Designsystem verwendet werden sollen. Bei einem neuen Projekt solltest du diese Vorgaben dagegen ausdrücklich nennen.

Bitte Codex, die Screenshots als visuelle Zielvorgabe zu verwenden, sie aber mit den tatsächlich im Projekt genutzten Utilities, Komponenten-Wrappern, dem Farbsystem, der Typografieskala und den Abstands-Tokens sowie den vorhandenen Mustern für Routing, State-Management und Datenabruf umzusetzen.

## Playwright nutzen

Playwright ist ein hilfreiches Tool, mit dem Codex die UI schrittweise verbessern kann. Damit kann Codex die App in einem echten Browser öffnen, die Implementierung mit den von dir bereitgestellten Screenshots vergleichen und Layout oder Verhalten anpassen.

Codex kann das Browserfenster an verschiedene Bildschirmgrößen anpassen und das Layout an unterschiedlichen Breakpoints prüfen.

Stelle sicher, dass der interaktive Playwright-Skill in Codex aktiviert ist. Weitere Informationen findest du in der [Dokumentation zu Skills](/de-DE/docs/build-skills).

## Optimieren

Der erste Durchlauf sollte den Screenshots bereits in den wesentlichen Punkten nahekommen. Bei komplexen Layouts oder Interaktionen sowie bei einer UI mit vielen Animationen solltest du mit einigen Anpassungsrunden rechnen.

Bitte Codex, die Implementierung mit den Screenshots abzugleichen, statt lediglich zu prüfen, ob sich die Seite erfolgreich erstellen lässt. Bei Konflikten sollte Codex den im Repository definierten Tokens des Designsystems Vorrang geben und nur die minimal erforderlichen Anpassungen an Abständen oder Größen vornehmen, damit der Gesamteindruck des Designs erhalten bleibt.

Nutze zusätzliche Screenshots oder kurze Hinweise, wenn sie Zustände verdeutlichen, die aus einem einzelnen Bild nicht ersichtlich sind.

### Vorschlag für einen Folge-Prompt
