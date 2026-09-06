<!-- source: https://learn.chatgpt.com/de-DE/use-cases/deep-security-scan -->

## Umfassende Repository-Prüfung auswählen

Verwende einen umfassenden Scan, wenn du ein Repository oder einen ausdrücklich angegebenen
Ordner gründlicher auf Schwachstellen prüfen musst und eine längere Laufzeit einplanen kannst.
Das Codex-Security-Plugin sucht in mehreren Durchläufen nach Schwachstellen, bevor es Befunde
validiert und priorisiert. Dieser Ablauf erfordert daher mehr Zeit und Ressourcen als ein gewöhnlicher Scan.

Ein umfassender Scan kann ein gesamtes Repository oder ein ausdrücklich angegebenes Paket oder
Verzeichnis prüfen. Wenn du einen Pull Request, einen Commit, einen Branch-Diff oder einen Working-Tree-Patch prüfen möchtest,
verwende
[$codex-security:security-diff-scan](/de-DE/codex/use-cases/scan-code-changes-for-security).

## Autorisierten Scan vorbereiten

1. Öffne das Repository in Codex und schließe den [Schnellstart für das Codex-Security-Plugin](/de-DE/codex/security/plugin) ab.
2. Vergewissere dich, dass dir das Repository gehört oder dass du berechtigt bist, es zu prüfen.
3. Hinterlege Vorgaben zu Architektur, Vertrauensgrenzen, Sicherheitsinvarianten, Befundkriterien,
   Ausschlüssen und Schweregraden in `SECURITY.md`. Verwende `SECURITY.md`-Dateien in Unterverzeichnissen
   für verzeichnisspezifische Richtlinien.
4. Dokumentiere unterstützte Build-, Test- und Validierungsbefehle sowie weitere Anweisungen für das Repository
   in `AGENTS.md`.
5. Führe den Einstiegs-Prompt aus und lasse den Scan alle Phasen vollständig durchlaufen:
wiederholte Suche, Validierung, Analyse der Angriffspfade und abschließende Berichterstellung.
6. Prüfe den Workspace mit den Befunden, den Bericht und mögliche Nachweislücken. Fordere bei
Bedarf detaillierte Schwachstellenberichte oder Empfehlungen zur strukturellen Härtung an.

## Nachweise vor der Behebung prüfen

Das Endergebnis sollte die betroffenen Stellen benennen und erläutern, warum das Verhalten
erreichbar ist, welche Validierung Codex durchgeführt hat und welche Nachweislücken verbleiben.
Außerdem sollte es einen klar abgegrenzten Ansatz zur Behebung aufzeigen. Unterscheide Befunde
ohne Validierungsnachweise von validierten Befunden.

Beginne nur mit der Behebung eines Befunds, den du ausgewählt und geprüft hast. Nutze
[Schwachstellen-Backlog abarbeiten](/de-DE/codex/use-cases/remediate-vulnerability-backlog),
um Befunde nacheinander mit gezielter Regressionsvalidierung zu beheben.

Informationen zum Setup, zur Vorabprüfung, zu abgegrenzten Scan-Zielen und zur erwarteten Laufzeit findest du unter [Umfassenden
Sicherheitsscan ausführen](/de-DE/codex/security/plugin/deep-scans).
