<!-- source: https://learn.chatgpt.com/de-DE/docs/security/threat-model -->

Erfahre, was ein Bedrohungsmodell ist und wie du durch seine Bearbeitung die Vorschläge von Codex Security verbesserst.

## Was ein Bedrohungsmodell ist

Ein Bedrohungsmodell fasst kurz zusammen, wie dein Repository aus Sicherheitssicht funktioniert. In Codex Security bearbeitest du es als `project overview`. Das System nutzt es als Kontext für künftige Scans sowie für die Priorisierung und Überprüfung der Ergebnisse.

Codex Security erstellt anhand des Codes einen ersten Entwurf. Wenn dir die Ergebnisse nicht stimmig erscheinen, bearbeite zuerst das Bedrohungsmodell.

Ein hilfreiches Bedrohungsmodell nennt:

- Einstiegspunkte und nicht vertrauenswürdige Eingaben
- Vertrauensgrenzen und Annahmen zur Authentifizierung
- sensible Datenpfade oder privilegierte Aktionen
- die Bereiche, die dein Team zuerst überprüfen möchte

Zum Beispiel:

> Öffentliche API für Änderungen an Konten. Akzeptiert JSON-Anfragen und Datei-Uploads. Nutzt einen internen Authentifizierungsdienst zur Identitätsprüfung und nimmt Änderungen an Abrechnungsdaten über einen internen Dienst vor. Schwerpunkte der Überprüfung sind Authentifizierungsprüfungen, die Verarbeitung von Uploads und Vertrauensgrenzen zwischen Diensten.

Damit erhält Codex Security einen besseren Ausgangspunkt für künftige Scans und die Priorisierung der Ergebnisse.

## Bedrohungsmodell verbessern und erneut prüfen

Wenn du die Ergebnisse verbessern möchtest, bearbeite zuerst das Bedrohungsmodell. Überarbeite es, wenn in den für dich wichtigen Bereichen Ergebnisse fehlen oder sie an unerwarteten Stellen auftauchen. Änderungen am Bedrohungsmodell wirken sich auf den Kontext künftiger Scans aus.

  Manche kopieren das aktuelle Bedrohungsmodell in Codex und verbessern es in einem Chat
mit Blick auf die Bereiche, die sie genauer überprüfen lassen möchten. Anschließend fügen sie die aktualisierte
Version wieder in die Web-Benutzeroberfläche ein.

### Wo du das Bedrohungsmodell bearbeiten kannst

Um das Bedrohungsmodell zu überprüfen oder zu aktualisieren, rufe [Codex Security-Scans](https://chatgpt.com/codex/security/scans) auf, öffne das Repository und klicke auf **Bearbeiten**.

## Weitere Dokumentation

- [Codex Security Cloud-Setup](/de-DE/codex/security/setup) behandelt das Repository-Setup und die Überprüfung der Ergebnisse.
- [Codex Security](/de-DE/codex/security) bietet eine Übersicht über das Produkt.
- [Codex Security Cloud-FAQ](/de-DE/codex/security/faq) behandelt häufige Fragen zur Cloud.
