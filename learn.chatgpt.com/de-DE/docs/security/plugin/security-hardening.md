<!-- source: https://learn.chatgpt.com/de-DE/docs/security/plugin/security-hardening -->

Verwende `$codex-security:propose-security-hardening`, um aus einer Sammlung von
sicherheitsrelevanten Nachweisen strukturelle oder architektonische Härtungsmaßnahmen abzuleiten. Der
Ablauf kann einen abgeschlossenen Scan von Codex Security analysieren oder bereitgestellte
Befunde, Berichte über offengelegte Schwachstellen, Vorfallanalysen, Bewertungsunterlagen und
Quellcode als Ausgangspunkt verwenden.

Das Ergebnis ist ein Portfolio mit Designoptionen, kein Patch. Es belegt nicht, dass eine
Schwachstelle damit behoben wird. Codex ändert das Repository erst, wenn du eine Option auswählst und
die Änderung ausdrücklich anforderst.

## Nachweise vorbereiten

Stelle für den Ablauf Folgendes bereit:

- Ein Scanverzeichnis oder eine explizit zusammengestellte Sammlung von Befunden und Berichten.
- Den zu untersuchenden Quellbaum sowie, sofern verfügbar, die relevante Revision oder den relevanten Snapshot.
- PoCs, Traces, Nachweise zu Vorfällen oder Bewertungsunterlagen, die die
Befunde stützen.
- Vorgaben zu Leistung, Speicherbedarf, Kompatibilität, Zuverlässigkeit, Betrieb,
Umsetzungsdauer oder Änderungsumfang.

Der Ablauf nutzt die Nachweise, um wiederholt verletzte Invarianten, verstreute
Sicherheitskontrollen, Engstellen mit privilegiertem Zugriff, schwache Isolationsgrenzen und wiederkehrende
Behebungsmuster zu erkennen. Er kann auch zu dem Schluss kommen, dass lokale Korrekturen
verhältnismäßiger sind als eine Änderung der Architektur.

## Ablauf ausführen

Sende zum Beispiel folgenden Prompt:

```text
Use $codex-security:propose-security-hardening to analyze [scan directory or finding paths] against [source tree and revision]. Develop evidence-backed structural hardening options with engineering tradeoffs, before-and-after diagrams, a migration plan, and an implementation handoff. Do not modify the repository.

## Portfolio prüfen

Ein aussagekräftiges Portfolio sollte:

- Jede vorgeschlagene Änderung mit konkreten Befunden sowie Nachweisen aus dem Quellcode und
Bedrohungsmodell verknüpfen.
- Das aktuelle Design und die Sicherheitsinvarianten beschreiben, die das neue Design
bewahren soll.
- Unterschiedliche Optionen im Hinblick auf Restrisiko, Leistung,
Zuverlässigkeit, Betrieb, Kompatibilität und Migrationskosten vergleichen.
- Nur dann eine Option empfehlen, wenn die Nachweise sie stützen, und dabei
Annahmen und offene Fragen ausdrücklich benennen.
- Hinweise zu Rollout, Validierung, Rollback und Implementierung enthalten.
- Beobachtete Fakten, Schlussfolgerungen und vorgeschlagene Eigenschaften des Designs voneinander trennen.

Prüfe die Nachweise und wäge die Vor- und Nachteile ab, bevor du dich für eine Option entscheidest. Ein Architekturdiagramm
oder eine Designempfehlung ersetzt weder die Validierung der ursprünglichen
Befunde noch die der umgesetzten Korrektur.

## Härtungsempfehlungen aus einem Scan verwenden

Du kannst für einen Standard-, Tiefen- oder Änderungsscan mit
berichtswürdigen Befunden ein Portfolio mit Härtungsmaßnahmen anfordern. Codex speichert das Portfolio unter `hardening/hardening.md`,
die strukturierte Analyse unter `hardening/hardening.json` sowie ergänzende Vorschläge
oder Diagramme unter `hardening/`. Der Scan verlinkt das Portfolio in `report.md`.

Bewahre das vollständige Scanverzeichnis als Einheit auf, damit diese Links weiterhin funktionieren. Informationen zur Prüfung
der einzelnen Berichte, auf denen das Portfolio basiert, findest du unter [Schwachstellenberichte
erstellen](/de-DE/codex/security/plugin/vulnerability-reports).
