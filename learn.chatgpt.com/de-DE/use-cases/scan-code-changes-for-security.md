<!-- source: https://learn.chatgpt.com/de-DE/use-cases/scan-code-changes-for-security -->

## Die Änderung statt des gesamten Repositorys prüfen

Führe eine gezielte Sicherheitsprüfung des Diffs durch, wenn ein Pull Request, Commit, Branch oder lokaler Patch
einen sensiblen Codepfad ändert. Das Codex-Security-Plugin nutzt den Kontext des Repositorys,
um die Änderung zu verstehen. Anschließend konzentriert es sich bei der Suche nach Befunden und deren Validierung
auf den Diff und den Code, der unmittelbar damit zusammenhängt.

Dieser Arbeitsablauf ergänzt die normale Codeüberprüfung. Nutze ihn, wenn du Belege
für Sicherheitsregressionen benötigst, nicht für eine allgemeine Stil- oder Testprüfung.

## Eine gezielte Prüfung durchführen

1. Öffne das Repository und checke den konkret zu prüfenden Git-basierten Änderungssatz aus oder beschreibe ihn.
2. Schließe den [Schnellstart für das Codex-Security-Plugin](/de-DE/codex/security/plugin) ab und gib im Starter-Prompt den Pull Request, Commit, Branch-Diff oder Working-Tree-Patch an.
3. Nenne sicherheitskritische Bereiche der Änderung, etwa Authentifizierung, Parser, Dateipfade, Netzwerkanfragen oder den Umgang mit Zugangsdaten.
4. Führe den Prompt aus, ohne zugleich eine Behebung anzufordern, damit das erste Ergebnis als Review-Artefakt erhalten bleibt.
5. Prüfe jede als betroffen gemeldete Zeile, jedes Validierungsergebnis und jede ausgewiesene Nachweislücke, bevor du über eine Behebung entscheidest.

## Einen Befund weiterverfolgen

Ein aussagekräftiger Bericht unterscheidet zwischen einem erreichbaren, belegten Sicherheitsbefund und einem
Verdacht, der noch bestätigt werden muss. Er kann zudem Inline-Kommentare im Code
für betroffene Zeilen enthalten. Für ein umsetzbares Ergebnis erstelle eine neue, klar abgegrenzte
Aufgabe zur Behebung mit der Befund-ID oder dem relevanten Berichtsabschnitt.
Öffne [Einen Schwachstellen-Backlog abarbeiten](/de-DE/codex/use-cases/remediate-vulnerability-backlog)
und informiere dich über den Zyklus aus Behebung und Validierung.

Informationen zur Änderungsauswahl, zum Diff-Umfang und zur Ergebnisprüfung findest du unter [Codeänderungen
auf Sicherheitsrisiken prüfen](/de-DE/codex/security/plugin/code-changes).
