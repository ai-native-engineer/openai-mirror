<!-- source: https://learn.chatgpt.com/de-DE/docs/security/plugin -->

Codex Security prüft deinen Code auf Schwachstellen und validiert plausible
Befunde. Zu jedem meldewürdigen Problem erhältst du die nötigen Nachweise und
Hinweise zur Behebung, um das Ergebnis zu prüfen. Scanne nur Code, der dir
gehört oder den du prüfen darfst.

In diesem Schnellstart installierst du das Plug-in und führst in Codex einen
Standardscan ohne Schreibzugriff für ein lokales Repository aus.

  Diese Seite behandelt das Codex-Security-Plugin in der Desktop-App oder in Codex CLI.
  Wie du ein verbundenes GitHub-Repository in Codex Cloud scannst, erfährst du unter [Setup
  für Codex Security Cloud](/de-DE/codex/security/setup).

## Plug-in installieren

1. Öffne [Codex in der ChatGPT-Desktop-App](/de-DE/codex/app).
2. Öffne **Plug-ins**, suche nach **Codex Security** oder verwende die Schaltfläche unten:

   <div className="not-prose my-6">
     
       Codex-Security-Plugin installieren
     
   </div>

3. Stelle sicher, dass das Plug-in aktiviert ist, und öffne anschließend **Sicherheit** in der Seitenleiste.

1. Wechsle im Terminal in das Repository, das du prüfen möchtest, und starte Codex:

   ```bash
   codex

2. Gib `/plugins` ein, suche nach **Codex Security** und wähle **Plug-in
   installieren** aus.
3. Gib `/new` ein, um einen neuen Chat für das Repository zu starten.

Verwende die ChatGPT-Desktop-App oder Codex CLI, um Codex Security für ein lokales
Repository zu installieren.

  Prüfe das [Änderungsprotokoll des Plug-ins](/de-DE/codex/security/plugin/changelog), bevor du dich auf eine Funktion
  verlässt oder einen lang andauernden Scan startest. Wenn **Sicherheit** in der
  Seitenleiste der Desktop-App nicht angezeigt wird, aktualisiere die App und das Plug-in
  und vergewissere dich, dass das Plug-in aktiviert ist.

## Ersten Scan durchführen

Verwende für die bestmögliche Scanqualität <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
mit dem Reasoning-Aufwand `xhigh`.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Wähle ein Repository aus und konfiguriere einen neuen Sicherheitsscan, bevor du ihn startest.
  </figcaption>
</figure>

1. Scan-Setup öffnen

   Wähle in der Seitenleiste **Sicherheit** aus, öffne **Scans** und wähle **+ Scan** aus.

2. Codebasis und Scanbereich auswählen

   Wähle ein vorhandenes Repository oder einen anderen Ordner aus. Wähle **Codebasis** aus,
   lass **Tiefenscan** deaktiviert und wähle das gesamte Repository oder einen einzelnen Ordner aus.
   Stelle sicher, dass Branch und Revision auf den Code verweisen, den du scannen möchtest.

3. Relevanten Kontext hinzufügen

   Wähle das Modell und den Reasoning-Aufwand aus. Öffne **Zusätzlicher Kontext** nur, wenn
   du einen bestimmten Angriffsvektor, einen sicherheitskritischen Bereich oder ein Detail zum
   Repository beschreiben musst, um die Überprüfung gezielt auszurichten.

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       Aktiviere zusätzlichen Kontext, um Angriffsvektoren, Schwerpunktbereiche und
relevante Sicherheitshinweise zu beschreiben.
     </figcaption>
   </figure>

4. Scan starten

   Wähle **Scan starten** aus und verfolge die Scanphasen in der Sicherheits-Workbench.
   Wähle **Aktivität anzeigen** aus, um die Codex-Aufgabe einzusehen, die den Scan ausführt.

5. Ergebnis prüfen

   Öffne den abgeschlossenen Scan, um Befunde, Abdeckung und verfügbare Berichtsartefakte
   zu prüfen. Nutze **Befunde** , um Probleme scanübergreifend zu prüfen, oder **Repositories**,
   um den Scanverlauf eines Repositorys einzusehen.

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       Prüfe Scanergebnisse, Befunde und Abdeckung in der Sicherheits-Workbench.
     </figcaption>
   </figure>

1. Standardscan anfordern

   Sende diesen Prompt im neuen Chat:

   ```text
   Run a Codex Security scan on this repository.

2. Scan zu Ende laufen lassen

   Codex führt den Scan im Terminal aus, ohne einen Workspace für das Setup zu öffnen.
Lass die Aufgabe weiterlaufen, bis Codex meldet, dass sie abgeschlossen ist. Wenn Codex
eine Einschränkung der Konfiguration erkennt, prüfe diese und die konkret vorgeschlagene
Änderung, bevor du eine Aktualisierung der Konfiguration genehmigst.

3. Ergebnis prüfen

   Prüfe die Zusammenfassung im Terminal und öffne anschließend die erstellte Datei `report.md`, um
   das vollständige Ergebnis einzusehen.

Führe diesen lokalen Plug-in-Ablauf in der ChatGPT-Desktop-App oder in Codex CLI aus.

## Was der Scan erstellt

Abgeschlossene Scans bleiben unter **Scans** verfügbar. Prüfe ihre Befunde und
Abdeckung in der Sicherheits-Workbench oder sieh dir zugehörige Befunde und den
Repository-Verlauf unter **Befunde** und **Repositories** an. Der Scan erstellt außerdem
die folgenden Dateien.

Jeder abgeschlossene Scan gibt im Terminal eine Zusammenfassung aus und erstellt
die folgenden Dateien.

Führe diesen lokalen Plug-in-Ablauf in der ChatGPT-Desktop-App oder in Codex CLI aus.

- `report.md`, die zentrale Datei zum Lesen der Scanergebnisse.
- `findings/<slug>/`, wenn detaillierte Schwachstellenberichte und ergänzende
  Proof-of-Concept-Dateien verfügbar sind.
- `hardening/`, wenn Hinweise zur strukturellen Sicherheitshärtung sowie ergänzende Vorschläge oder
  Diagramme verfügbar sind.
- Strukturierte Scandaten in `scan-manifest.json`, `findings.json` und
`coverage.json` für Automatisierung und Integrationen. Du kannst die Scanergebnisse prüfen,
  ohne diese Dateien zu öffnen.

Halte beim Teilen oder Archivieren von Ergebnissen das gesamte Scanverzeichnis zusammen, damit die
Links in `report.md` weiterhin funktionieren.

## Nächsten Ablauf auswählen

- [Sicherheits-Workbench verwenden](/de-DE/codex/security/plugin/workbench), um
  gespeicherte Scans, Befunde, Repositories und Scanaktivitäten in der Desktop-App zu verwalten.
- [Scan über die CLI ausführen](/de-DE/codex/security/cli), wenn du Betazugriff hast und
  einen wiederholbaren Terminal-Ablauf mit strukturierten Ergebnissen benötigst.
- [Standardscan oder eingegrenzten Scan durchführen](/de-DE/codex/security/plugin/scans), um ein
  Repository oder einen einzelnen Ordner mit dem Standardablauf zu prüfen.
- [Ersten Scan auswerten](/de-DE/codex/security/plugin/scans#assess-a-first-scan),
  um die Ergebnisse mit bekannten Problemen abzugleichen und zu entscheiden, wann du erneut scannst.
- [Tiefenscan durchführen](/de-DE/codex/security/plugin/deep-scans), um gründlicher zu scannen,
  wenn du eine längere Laufzeit einplanen kannst.
- [Codeänderungen überprüfen](/de-DE/codex/security/plugin/code-changes), um einen Pull Request,
  einen Commit, einen Branch-Bereich oder einen Working-Tree-Patch zu bewerten.
- [Backlog prüfen und priorisieren](/de-DE/codex/security/plugin/triage-backlog), um vorhandene
  Sicherheitsbefunde zu überprüfen.
- [Befund beheben und verifizieren](/de-DE/codex/security/plugin/fix-findings), nachdem du
  einen Befund zur Behebung akzeptiert hast.
- [Befunde exportieren oder nachverfolgen](/de-DE/codex/security/plugin/export-findings), um
  JSON, CSV, SARIF, ein genehmigungspflichtiges Issue in Linear, GitHub oder Jira oder einen
  privaten Entwurf eines GitHub Security Advisory zu erstellen.
- [Schwachstellenberichte erstellen](/de-DE/codex/security/plugin/vulnerability-reports),
  um bereitgestellte Befunde, Hinweise zur Offenlegung, Quellcode und PoCs zu
  in sich geschlossenen Berichten zusammenzufassen.
- [Maßnahmen zur Sicherheitshärtung vorschlagen](/de-DE/codex/security/plugin/security-hardening), um
  anhand von Scanergebnissen oder anderen Sicherheitsnachweisen strukturelle oder
  architektonische Optionen abzuwägen.
