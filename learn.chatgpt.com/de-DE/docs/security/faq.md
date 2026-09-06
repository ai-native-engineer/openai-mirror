<!-- source: https://learn.chatgpt.com/de-DE/docs/security/faq -->

Diese FAQ behandelt Codex Security Cloud. Informationen zu lokalen Scans und Arbeitsabläufen, die in
einer Codex-Aufgabe ausgeführt werden, findest du im [Schnellstart für das Codex-Security-Plugin](/de-DE/codex/security/plugin).

{/* vale Microsoft.Auto = NO */}
{/* vale Vale.Spelling = NO */}

## Erste Schritte

### Was ist Codex Security?

Softwaresicherheit zählt weiterhin zu den schwierigsten und wichtigsten Aufgaben in der Softwareentwicklung. Codex Security ist ein LLM-gestütztes Toolkit für Sicherheitsanalysen, das Quellcode prüft und strukturierte, priorisierte Befunde zu Schwachstellen mit vorgeschlagenen Patches liefert. Es hilft Entwicklungs- und Sicherheitsteams, Sicherheitsprobleme in großem Umfang zu erkennen und zu beheben.

### Warum ist das wichtig?

Software ist für moderne Industrie und Gesellschaft unverzichtbar, und Schwachstellen bergen systemische Risiken. Codex Security unterstützt einen auf die Verteidigung ausgerichteten Arbeitsablauf, indem es fortlaufend wahrscheinliche Probleme erkennt, sie nach Möglichkeit validiert und Korrekturen vorschlägt. So können Teams die Sicherheit verbessern, ohne die Entwicklung auszubremsen.

### Welches geschäftliche Problem löst Codex Security?

Codex Security verkürzt den Weg von einem vermuteten Problem zu einem bestätigten, reproduzierbaren Befund mit Belegen und einem vorgeschlagenen Patch. Dadurch sinkt der Triage-Aufwand, und es gibt weniger Fehlalarme als beim alleinigen Einsatz herkömmlicher Scanner.

### Wie funktioniert Codex Security?

Codex Security führt die Analyse in einem temporären, isolierten Container aus und klont das Ziel-Repository vorübergehend. Es analysiert den Code und liefert strukturierte Befunde mit Beschreibung, Datei und Position, Kritikalität, Ursache sowie einem Vorschlag zur Behebung.

Bei Befunden mit Verifizierungsschritten führt das System die vorgeschlagenen Befehle oder Tests in derselben Sandbox aus. Es zeichnet Erfolg oder Fehlschlag, Exitcodes, stdout, stderr, Testergebnisse sowie alle erzeugten Diffs oder Artefakte auf und fügt diese Ausgaben als Belege für die Prüfung hinzu.

### Ersetzt es SAST?

Nein. Codex Security ergänzt SAST. Es erweitert die Analyse um semantische Schlussfolgerungen auf LLM-Basis und automatische Validierung, während bestehende SAST-Tools weiterhin eine umfassende deterministische Abdeckung bieten.

## Funktionen

### Aus welchen Schritten besteht die Analysepipeline?

Codex Security arbeitet mit einer mehrstufigen Pipeline:

1. **Analyse** erstellt ein Bedrohungsmodell für das Repository.
2. **Commit-Scanning** prüft zusammengeführte Commits und den Repository-Verlauf auf wahrscheinliche Probleme.
3. **Validierung** versucht, wahrscheinliche Schwachstellen in einer Sandbox zu reproduzieren, um Fehlalarme zu reduzieren.
4. Die **Patch-Erstellung** nutzt die Integration mit Codex, um Patches vorzuschlagen, die Prüfende begutachten können, bevor sie einen PR öffnen.

Codex Security unterstützt Entwicklungsteams bei ihrer Arbeit in GitHub, Codex und gängigen Review-Arbeitsabläufen.

### Welche Sprachen werden unterstützt?

Codex Security ist nicht an eine bestimmte Sprache gebunden. In der Praxis hängt die Leistung davon ab, wie gut das Modell mit der im Repository verwendeten Sprache und dem Framework umgehen kann.

### Welche Ergebnisse erhalte ich nach Abschluss des Scans?

Du erhältst priorisierte Befunde mit Kritikalität, Validierungsstatus sowie einem vorgeschlagenen Patch, sofern verfügbar. Die Befunde können außerdem Absturzausgaben, Reproduktionsbelege, Kontext zum Aufrufpfad und zugehörige Annotationen enthalten.

### Wie wird Kundencode isoliert?

Jeder Analyse- und Validierungsvorgang läuft in einem temporären Codex-Container mit Tools, die auf die jeweilige Sitzung beschränkt sind. Artefakte werden zur Prüfung extrahiert, und nach Abschluss des Vorgangs wird der Container entfernt.

### Wendet Codex Security Patches automatisch an?

Nein. Der vorgeschlagene Patch ist eine empfohlene Maßnahme zur Behebung. Du kannst ihn über die Benutzeroberfläche für Befunde prüfen und von dort als PR auf GitHub pushen. Codex Security wendet Änderungen am Repository jedoch nicht automatisch an.

### Ist für den Scan ein Build des Projekts erforderlich?

Nein. Codex Security kann auch ohne Kompilierschritt anhand des Repository- und Commit-Kontexts Befunde erzeugen. Während der automatischen Validierung kann Codex Security versuchen, im Container einen Build des Projekts zu erstellen, wenn sich das Problem dadurch reproduzieren lässt. Weitere Informationen zum Einrichten der Umgebung findest du unter [Cloud-Umgebungen von Codex](/de-DE/codex/environments/cloud-environment).

### Wie reduziert Codex Security Fehlalarme und vermeidet fehlerhafte Patches?

Codex Security arbeitet in zwei Schritten. Zunächst priorisiert das Modell wahrscheinliche Probleme. Anschließend versucht die automatische Validierung, jedes Problem in einem sauberen Container zu reproduzieren. Befunde, die sich erfolgreich reproduzieren lassen, werden als validiert gekennzeichnet. Das trägt dazu bei, Fehlalarme vor der Prüfung durch Fachleute zu reduzieren.

### Wie lange dauert ein erster Scan und wie geht es danach weiter?

Die Dauer eines ersten Scans hängt von der Größe des Repositorys, der Dauer des Builds und davon ab, wie viele Befunde in die Validierung gelangen. Bei manchen Repositorys kann ein Scan mehrere Stunden dauern, bei größeren mehrere Tage. Spätere Scans sind meist schneller, weil sie sich auf neue Commits und inkrementelle Änderungen konzentrieren.

### Was ist ein Bedrohungsmodell?

Ein Bedrohungsmodell beschreibt den Sicherheitskontext eines Repositorys für den Scan. Es kombiniert eine knappe Projektübersicht mit Details zur Angriffsfläche, etwa Einstiegspunkten, Vertrauensgrenzen, Annahmen zur Authentifizierung und riskanten Komponenten. Weitere Informationen findest du unter [Bedrohungsmodell verbessern](/de-DE/codex/security/threat-model).

### Wie wird ein Bedrohungsmodell erstellt?

Codex Security weist das Modell an, die Repository-Architektur und sicherheitsrelevante Einstiegspunkte zusammenzufassen, den Repository-Typ zu klassifizieren, spezialisierte Extraktoren auszuführen und die Ergebnisse zu einem Artefakt zusammenzuführen, das während des gesamten Scans als Projektübersicht oder Bedrohungsmodell dient.

### Ersetzt es eine manuelle Sicherheitsprüfung?

Nein. Codex Security beschleunigt die Prüfung und hilft dabei, Befunde zu priorisieren. Es ersetzt jedoch weder die Validierung auf Codeebene noch Prüfungen der Ausnutzbarkeit oder die manuelle Bedrohungsbewertung.

### Kann ich das Bedrohungsmodell bearbeiten?

Ja. Codex Security erstellt zunächst ein Bedrohungsmodell. Du kannst es aktualisieren, wenn sich Architektur, Risiken und geschäftlicher Kontext ändern. Wie du es bearbeitest, erfährst du unter [Bedrohungsmodell verbessern](/de-DE/codex/security/threat-model).

### Muss ich vor der Bedrohungsmodellierung einen Scan konfigurieren?

Ja. Die Hinweise zum Bedrohungsmodell richten sich danach, wie und was du scannst. Deshalb musst du zuerst das Repository konfigurieren. Weitere Informationen findest du unter [Codex-Security-Setup](/de-DE/codex/security/setup).

### Was enthält der vorgeschlagene Patch?

Wenn für den Befund eine Korrektur erstellt werden kann, enthält der vorgeschlagene Patch einen minimalen, direkt umsetzbaren Diff mit Dateinamen und Zeilenkontext.

### Ändert der Patch meinen PR-Branch direkt?

Nein. Der Arbeitsablauf erzeugt einen Diff, eine Patch-Datei oder einen Änderungsvorschlag. Repository-Verantwortliche und Prüfende können das Ergebnis prüfen, bevor sie es anwenden.

## Validierung

### Was ist die automatische Validierung?

Die automatische Validierung ist die Phase, in der das System versucht, ein vermutetes Problem in einem isolierten Container zu reproduzieren. Es zeichnet auf, ob die Reproduktion erfolgreich war oder fehlgeschlagen ist, und erfasst Protokolle, Befehle und zugehörige Artefakte als Belege.

### Was passiert, wenn die Validierung fehlschlägt?

Der Befund bleibt unvalidiert. Protokolle und Berichte halten dennoch fest, was versucht wurde. So können Entwicklungsteams einen weiteren Reproduktionsversuch starten, das Problem genauer untersuchen oder die Reproduktionsschritte anpassen.

{/* vale Microsoft.Auto = YES */}
{/* vale Vale.Spelling = YES */}
