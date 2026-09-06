<!-- source: https://learn.chatgpt.com/de-DE/docs/security/plugin/scans -->

Beginne für eine erste Prüfung oder eine routinemäßige Bewertung eines
Repositorys oder einer Komponente mit einem Standardscan von Codex Security. Dieser führt den vollständigen Scan-Ablauf einmal aus.

Prüfe für eine gründlichere Bewertung zunächst die Ergebnisse und führe dann [einen
Tiefenscan](/de-DE/codex/security/plugin/deep-scans) aus. Tiefenscans dauern länger und suchen
umfassender.

## Scanbereich auswählen

Öffne in der Desktop-App **Sicherheit**, wähle **Scans** und dann **+ Scan** aus.
Wähle ein vorhandenes Repository oder einen anderen Ordner und anschließend **Codebasis** aus.

Scanne das gesamte Repository, wenn du eine umfassende Abdeckung benötigst und es eine
sinnvolle Prüfungseinheit darstellt. Wähle bei einem Monorepo einen Ordner aus, wenn für einen Dienst,
ein Paket oder eine Komponente die Zuständigkeit und die Sicherheitsgrenze klar definiert sind.

Du kannst einen Scan auch aus einer Unterhaltung mit Codex heraus starten:

```text
Use $codex-security:security-scan to scan this repository for security vulnerabilities.

Wenn sich die Unterhaltung auf einen bestimmten Ordner konzentrieren soll, gib die Komponente an:

```text
Use $codex-security:security-scan to scan this repository for security vulnerabilities, focusing on the services/billing component.

  Beginne bei einem großen Monorepo mit einem klar abgegrenzten Produkt- oder Dienstbereich.

## Scan konfigurieren

Verwende für die bestmögliche Scanqualität <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
mit dem Reasoning-Aufwand `xhigh`.

1. Wähle **Codebasis** aus und lasse **Tiefenscan** deaktiviert.
2. Bestätige das ausgewählte Repository, den aktuellen Branch und den neuesten Revisionsstand.
3. Lege für **Scanbereich** das gesamte Repository fest oder wähle einen Ordner aus.
4. Wähle ein Modell und den Reasoning-Aufwand aus.
5. Öffne **Zusätzlicher Kontext** nur, wenn dies die Prüfung beeinflusst. Hilfreicher Kontext
   benennt von Angreifenden kontrollierte Eingaben, Vertrauensgrenzen, sensible Aktionen oder einen
   bestimmten Bereich, der priorisiert werden soll.
6. Wähle **Scan starten** aus.

Füge `SECURITY.md` im Stammverzeichnis des Repositorys hinzu, um Sicherheitshinweise dauerhaft zu hinterlegen.
Beschreibe das Bedrohungsmodell, Sicherheitsinvarianten, Kriterien für zu meldende Befunde,
Ausschlüsse und den Kontext zur Bewertung des Schweregrads. Füge in Unterverzeichnissen weitere Dateien namens `SECURITY.md` hinzu,
um verzeichnisspezifische Hinweise zu geben. Wenn sich Richtlinien widersprechen, hat die Datei Vorrang, deren Verzeichnis dem
Code am nächsten liegt. Codex Security behandelt diese Dateien als Richtlinienkontext
und nicht als ausführbare Anweisungen.

Verwende `AGENTS.md` für unterstützte Build- und Validierungsbefehle sowie andere
Repository-spezifische Anweisungen.

## Abschluss aller Phasen abwarten

Ein Scan durchläuft diese Phasen in der folgenden Reihenfolge:

1. Die **Bedrohungsmodellierung** identifiziert Schutzgüter, Einstiegspunkte, Vertrauensgrenzen und
   Sicherheitsinvarianten.
2. Die **Befundsuche** prüft den angeforderten Code auf möglicherweise fehlerhafte
   Sicherheitskontrollen und Source-to-Sink-Pfade.
3. Die **Validierung** testet jeden potenziellen Befund oder prüft ihn auf andere Weise und erfasst Belege
   oder Nachweislücken.
4. Die **Auswirkungs- und Pfadanalyse** bewertet die realistischen Pfade jedes potenziellen Befunds,
   seine Auswirkungen und seinen Schweregrad.
5. Die **Berichterstellung** erfasst validierte Befunde, Abdeckung und Scan-Metadaten.
   Detaillierte Berichte zu einzelnen Befunden sind auf Anfrage verfügbar.
6. Die **strukturelle Härtung** analysiert auf Anfrage die Gesamtheit der Befunde und
   erstellt Empfehlungen für das Design.
7. Der **Abschluss** validiert den strukturierten Scan-Kontrakt und erstellt
`report.md`, einschließlich Links zu etwaigen detaillierten Berichten oder Empfehlungen zur Härtung.

Die Workbench zeigt die aktive Scan-Phase und den vom Plug-in gemeldeten Fortschritt an.
Wähle **Aktivität anzeigen** aus, um die Codex-Aufgabe zu prüfen. Warte auf das vollständige
Ergebnis, statt mögliche Befunde vorschnell zu beurteilen oder den Scan abzubrechen, nur weil eine Phase
länger dauert als eine andere.

## Abgeschlossenen Scan prüfen

Prüfe das Ergebnis in dieser Reihenfolge:

1. Bestätige das Ziel, die Revision und den Scanbereich.
2. Lies die Angaben zu den geprüften Bereichen sowie zu allen ausdrücklich zurückgestellten oder zur Nachverfolgung vorgesehenen Bereichen.
3. Prüfe für jeden Befund die zugrunde liegende Kontrolle oder Senke, die von Angreifenden kontrollierte
Eingabe, die Validierungsmethode, verbleibende Unsicherheiten, die realistische Erreichbarkeit,
die Begründung für den Schweregrad und die vorgeschlagene Behebung.
4. Verwirf Befunde, wenn die Belege den behaupteten Pfad oder die behauptete Auswirkung nicht stützen.
5. Wähle einen akzeptierten Befund aus, bevor du mit der Behebung beginnst.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Prüfe den Schweregrad, den Validierungsstatus, die Ursache und den
Angriffspfad des Befunds.
  </figcaption>
</figure>

## Ersten Scan bewerten

Wähle vor dem Scan zwei bis vier Bewertungskriterien aus, etwa die unabhängige
Erkennung, die Qualität der Belege, Fehlalarme oder die Qualität der Behebung. Wenn du
anhand eines bekannten Befunds testest, halte fest, ob du ihn Codex mitgeteilt oder
beim Scan zurückgehalten hast.

Halte Repository-Revision, Plug-in-Version, Modell und Reasoning-Aufwand fest.
Nutze diese Ausgangsbasis, um spätere Scans damit zu vergleichen, wenn sich der Code, die Sicherheitskontrollen oder
die Scan-Einstellungen geändert haben.

## Scanrhythmus festlegen

Lege den Scanrhythmus anhand des Risikos des Repositorys und der Kapazität deines Teams
zur Bearbeitung von Befunden fest. Führe zu folgenden Zeitpunkten Scans aus:

- **Ausgangsbasis:** Führe einen Standardscan aus, wenn du ein Repository neu einbindest, die
  Verantwortung für eine Komponente übernimmst oder einen Ausgangspunkt für ein neues Bedrohungsmodell benötigst.
- **Codeänderungen:** [Prüfe Änderungen
  am Code](/de-DE/codex/security/plugin/code-changes), wenn ein Pull Request oder Commit
  sicherheitsrelevanten Code oder eine externe Integration ändert.
- **Regelmäßige Prüfung:** Lege ein wiederkehrendes Prüfintervall danach fest, wie stark dein System
  Risiken ausgesetzt ist und wie oft sich der Code ändert. Passe es an die Kapazität deines Teams zur
  Bearbeitung von Befunden an.
- **Nach einer Korrektur:** [Behebe und überprüfe den
  Befund](/de-DE/codex/security/plugin/fix-findings). Vergewissere dich, dass sich das Problem nicht
  mehr reproduzieren lässt, und bewahre den ursprünglichen Scan zum Vergleich auf.

Aus diesen Scan-Anlässen entsteht kein automatisierter Zeitplan.

## Früheren Scan erneut öffnen

Öffne **Sicherheit** und wähle anschließend unter **Scans** einen gespeicherten Scan aus, um dessen
Befunde, Abdeckung und verfügbare Berichtsartefakte zu prüfen. Starte zur Bewertung des neuesten Codes
einen neuen Scan für dasselbe Repository. Der neue Scan ersetzt weder den
früheren Scan noch dessen Artefakte.

## Ergebnisse verwenden

Verwende die Sicherheits-Workbench, um Befunde, Abdeckung und nachzuverfolgende Bereiche zu prüfen,
ohne JSON-Rohdaten zu untersuchen. Öffne, sofern verfügbar, `report.md` als lesbaren
Einstieg in das vollständige Scan-Verzeichnis. Teile oder archiviere das Verzeichnis stets vollständig,
denn der Bericht verweist auf detaillierte Berichte in `findings/`
und auf Empfehlungen zur strukturellen Härtung in `hardening/`, sofern diese optionalen Artefakte
verfügbar sind.

Im Hintergrund des Workspace speichert jeder Scan `scan-manifest.json`, `findings.json`
und `coverage.json` für Automatisierungen und Integrationen. Normalerweise musst du
diese Dateien nicht selbst öffnen.

Informationen zu übertragbaren Artefakten oder zur externen Problemverfolgung findest du unter [Befunde exportieren oder
nachverfolgen](/de-DE/codex/security/plugin/export-findings).

## Nächster Schritt

Nachdem du einen Befund akzeptiert hast, verwende [Befund beheben und
überprüfen](/de-DE/codex/security/plugin/fix-findings), um einen klar abgegrenzten
Patch zu erstellen und zu prüfen. Bitte Codex nicht darum, alle Befunde eines Scans in einem einzigen Chat zu beheben.
