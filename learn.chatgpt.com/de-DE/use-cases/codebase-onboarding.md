<!-- source: https://learn.chatgpt.com/de-DE/use-cases/codebase-onboarding -->

## Einführung

Wenn ein Repository für dich neu ist oder du dich in eine unbekannte Funktion einarbeiten musst, hilft dir Codex, dich zu orientieren, bevor du Code änderst. Es geht nicht nur um einen groben Überblick, sondern auch darum, den Anfrageablauf nachzuvollziehen, die Zuständigkeiten der einzelnen Module zu verstehen und die Dateien zu ermitteln, die du als Nächstes lesen solltest.

## So gehst du vor

Wenn du neu in einem Projekt bist, kannst du Codex zunächst einfach bitten, dir die gesamte Codebasis zu erklären:

Wenn du eine bestehende Codebasis um eine neue Funktion erweitern möchtest, kannst du Codex bitten, dir einen bestimmten Systembereich zu erklären. Je genauer du die Anfrage eingrenzt, desto konkreter wird die Erklärung:

1. Nenne Codex die relevanten Dateien, Verzeichnisse oder den Funktionsbereich, den du verstehen möchtest.
2. Bitte Codex, den Anfrageablauf nachzuverfolgen und zu erklären, welche Module für Geschäftslogik, Transport, Persistenz oder UI zuständig sind.
3. Frage vor jeder Änderung, wo validiert wird und wo Seiteneffekte oder Zustandsübergänge auftreten.
4. Frage abschließend, welche Dateien du als Nächstes lesen solltest und welche Stellen besondere Risiken bergen.

Eine hilfreiche Antwort zur Einarbeitung sollte dir eine konkrete Übersicht liefern und nicht nur eine Liste mit Dateinamen. Am Ende sollte Codex den zentralen Ablauf erklärt, auf riskante Stellen hingewiesen und dir gezeigt haben, welche Dateien du als Nächstes lesen solltest und welche Prüfungen vor den ersten Änderungen wichtig sind.

## Mögliche Anschlussfragen

Sobald Codex dir einen ersten Überblick gegeben hat, frage weiter, bis die Erklärung so konkret ist, dass du dir die erste Änderung zutraust. Gute Anschlussfragen sorgen in der Regel dafür, dass Codex Annahmen, versteckte Abhängigkeiten und die nach einer Änderung relevanten Prüfungen klar benennt.

- Welches Modul ist für die eigentliche Geschäftslogik zuständig und welches für die Transport- oder UI-Schicht?
- Wo findet die Validierung statt und welche Annahmen werden dort durchgesetzt?
- Welche zugehörigen Dateien oder Hintergrundjobs kann ich leicht übersehen, wenn ich diesen Ablauf ändere?
- Welche Tests oder Prüfungen sollte ich ausführen, nachdem ich diesen Bereich geändert habe?
