<!-- source: https://learn.chatgpt.com/de-DE/use-cases/figma-designs-to-code -->

## Einführung

Wenn dir eine genaue Figma-Auswahl vorliegt, kann Codex daraus eine ausgereifte UI erstellen, ohne die bereits in deinem Projekt etablierten Muster außer Acht zu lassen.

Mit dem Figma-Skill kann Codex über den Figma-MCP-Server strukturierten Designkontext, Variablen, Assets und die genaue Variante abrufen, die umgesetzt werden soll.

Mit dem interaktiven Playwright-Skill kann Codex die App in einem echten Browser öffnen, die Implementierung mit der Figma-Referenz vergleichen und Layout oder Verhalten iterativ anpassen, bis das Ergebnis der Vorlage näherkommt.

## Bereite dein Figma-Projekt vor

Je übersichtlicher deine Figma-Datei ist, desto besser wird die erste Implementierung. So verbesserst du die Übergabe:

- Verwende nach Möglichkeit Variablen oder Design-Tokens, insbesondere für Farben, Typografie und Abstände
- Erstelle Komponenten für wiederverwendbare UI-Elemente, statt nicht verknüpfte Ebenen zu duplizieren
- Nutze möglichst Auto-Layout statt manueller Positionierung
- Benenne Frames und Ebenen so eindeutig, dass Hauptansicht, Zustand und Varianten sofort erkennbar sind
- Belasse echte Icons und Bilder nach Möglichkeit in der Datei, damit Codex nicht raten muss

So erhält Codex eine bessere Struktur, die sich in eine robuste, produktionsreife UI umsetzen lässt.

## Sei konkret

Je konkreter du die erwarteten Interaktionsmuster und deinen gewünschten Stil beschreibst, desto besser wird das Ergebnis.

Wenn ein Zustand, ein Breakpoint oder eine Interaktion wichtig ist, weise ausdrücklich darauf hin. Enthält die Datei mehrere ähnliche Varianten, teile Codex mit, welche davon als maßgebliche Vorlage dienen soll.

Je eindeutiger du festlegst, was exakt übereinstimmen muss und wo die Konventionen des Repositorys Vorrang haben sollen, desto leichter kann Codex die richtigen Abwägungen treffen.

## Bereite das Designsystem vor

Codex arbeitet am besten, wenn das Ziel-Repository bereits eine klar strukturierte Komponentenebene hat. Codex kann deine vorhandenen Komponenten und dein Designsystem automatisch verwenden, statt sie von Grund auf neu zu erstellen.

Wenn du es für nötig hältst, gib Codex an, welche Primitives wiederverwendet werden sollen, wo deine Tokens definiert sind und was im Repository bei Buttons, Eingabefeldern, Karten, Typografie und Icons als Standard gilt.

Betrachte die Figma-MCP-Ausgabe, die häufig wie React und Tailwind aussieht, als strukturelle Referenz und nicht als Vorgabe für den endgültigen Codestil. Bitte Codex, die Ausgabe auf die im Projekt tatsächlich verwendeten Utilities, Komponenten-Wrapper, das Farbsystem, die Typografieskala und die Abstands-Tokens sowie auf die dortigen Muster für Routing, Zustandsverwaltung und Datenabrufe zu übertragen.

## Ablauf

### Beginne mit einer Figma-Auswahl

Kopiere den Link zu genau dem Figma-Frame, der Komponente oder der Variante, die du umsetzen möchtest. Der Figma-MCP-Ablauf basiert auf Links. Deshalb muss der Link auf den gewünschten Node selbst verweisen und nicht auf einen übergeordneten Frame in dessen Nähe.

### Fordere Codex auf, Figma zu verwenden

Figma sollte als Grundlage für den ersten Durchlauf dienen. Weise Codex an, vor Beginn der Implementierung den Figma-MCP-Ablauf zu befolgen.

Dein Prompt sollte Folgendes enthalten:

Sobald die erste Implementierung steht, überprüft Codex die UI mit Playwright in einem echten Browser und korrigiert verbleibende Abweichungen bei Darstellung oder Interaktion.
