<!-- source: https://learn.chatgpt.com/de-DE/docs/security/plugin/changelog -->

In diesem Änderungsprotokoll erfährst du, was sich am Codex-Security-Plugin geändert hat.

**Neueste Plug-in-Version:** `0.1.20`.

Prüfe die Plug-in-Version in deiner aktuellen Codex-Umgebung, bevor du eine Funktion aus einer neueren Version verwendest.

Die Einträge im Änderungsprotokoll richten sich nach der Plug-in-Version, nicht nach der Paketversion. Wenn du die CLI oder
das SDK verwendest, kannst du `npx @openai/codex-security info --json` ausführen, um die Versionen des Pakets
und des mitgelieferten Plug-ins gemeinsam zu prüfen.

## 0.1.20 (17. August 2026)

### Tiefenscans als vollständige, unabhängige Audits ausführen

- Führe mit jedem Worker für Tiefenscans dasselbe vollständige Audit wie bei Standardscans durch, einschließlich Bedrohungsmodellierung, Validierung, Angriffspfadanalyse und Berichterstellung zur Prüfabdeckung.
- Fasse abgeschlossene Worker-Berichte zu einem Scan zusammen. Dabei bleiben konfigurierte Zeitlimits, Angaben zur teilweisen Prüfabdeckung, die Wiederherstellung nach Neustarts und die Möglichkeit zum Abbrechen erhalten.
- Verwende standardmäßig vier parallele Worker, beende den Scan, wenn vier aufeinanderfolgende abgeschlossene
  Scans keine neuen Befunde ergeben, und begrenze einen Tiefenscan auf 40 Worker-Durchläufe. Für bestehende
Einstellungen mit `workers = "auto"` werden jetzt vier Worker verwendet. Siehe
[Laufzeit für Tiefenscans konfigurieren](/de-DE/codex/security/plugin/deep-scans#configure-deep-scan-runtime).
- Setze die Arbeit von Workern fort, die die Quellcodeprüfung abgeschlossen haben, deren endgültiger Entwurf aber verloren gegangen ist, statt das vollständige Audit zu wiederholen.

### Trusted Access for Cyber vor gehosteten Scans prüfen

- Prüfe auf Codex-Hosts, die die App Codex Security Access bereitstellen, vor dem Start von Standard-, Änderungs- und Tiefenscans den Status von Trusted Access.
- Du erhältst eine deutlich sichtbare Warnung, wenn geschützte Scan-Ausgaben möglicherweise nicht verfügbar sind, und einen Link zur Registrierung, wenn kein Zugriff gewährt wurde.
- Setze den Scan fort, wenn die Prüfung den Status von Trusted Access nicht bestätigen kann oder kein Zugriff gewährt wurde. Der Hinweis entscheidet nicht darüber, ob der Scan ausgeführt wird.
- Die öffentlichen CLI- und SDK-Pakete führen diese Prüfung in Version `0.1.20` nicht durch.

### Tiefenscans in weiteren Umgebungen ausführen

- Starte Worker für Tiefenscans aus installierten CLI- und SDK-Paketen, auch unter
  Windows ohne global verfügbare ausführbare Datei `codex`.
- Halte die Einstellungen für Tiefenscans eigenständiger CLI- und SDK-Installationen von anderen laufenden Scans getrennt.
- Behalte Einstellungen für nicht interaktive Genehmigungen in verschachtelten Workern für Tiefenscans bei.

### Scanergebnisse in weiteren Fehlerszenarien bewahren

- Behalte mehr gespeicherte Scans und abgeschlossene Worker-Ergebnisse bei der Wiederherstellung nach Neustarts, aus Archiven und nach Übergaben bei.
- Stelle gültige Befunde aus älteren oder unvollständigen Scandaten wieder her.
- Schließe Scans auch dann ab, wenn sich unabhängige Berichte zur Prüfabdeckung überschneiden.
- Berücksichtige zwischengespeicherte Eingaben korrekt in den Gesamtsummen der Token-Nutzung, sowohl bei aktuellen als auch bei älteren Antworten von Anbietern.

## 0.1.19 (13. August 2026)

### Zeitlimit für Tiefenscans festlegen

- Setze `[deep_scan].max_time_hours` auf eine Dauer von mehr als null und höchstens 96 Stunden.
  Auch Bruchteile von Stunden sind möglich.
- Behalte nach Ablauf des Zeitlimits die bereits ermittelten Ergebnisse der Schwachstellensuche bei und fahre dann mit der Validierung und Berichterstellung fort.
- Kennzeichne den Bericht als unvollständig, wenn vor Ablauf des Zeitlimits keine Quellcodeprüfung abgeschlossen wird.

### Zuverlässigkeit von Scans verbessern

- Behalte bereits abgeschlossene Schritte der Schwachstellensuche bei, wenn ein Worker stoppt oder ein Reducer einen neuen Versuch startet.
- Lies größere Quelldateien ein und erstelle Berichte ohne die bisherigen festen Größenbegrenzungen.
- Lies die per Commit gespeicherten Änderungen aus der ausgewählten Revision ein und behalte unter Windows Pfade relativ zum Repository bei.
- Gib Anmeldedaten für OpenRouter und Fireworks an Worker für Tiefenscans weiter.

## 0.1.18 (7. August 2026)

### Amazon Bedrock für Sicherheitsscans verwenden

- Führe Scans mit Bearer-Token für Amazon Bedrock und AWS-Profilen, Regionseinstellungen, Webidentität oder Container-Anmeldedaten aus.
- Stelle sicher, dass die AWS-Authentifizierung auch für delegierte Worker von Tiefenscans verfügbar bleibt.

### Standardscans mit geringerem Koordinationsaufwand ausführen

- Verwende einen einfacheren Ablauf für Standardscans von Repositorys und ausgewählten Pfaden.
- Behalte Vorgaben aus `SECURITY.md`-Dateien in Unterverzeichnissen, den genauen Scanumfang, Fortschrittsmeldungen
  und abschließende Scanberichte bei.

### Scans zuverlässiger starten und abschließen

- Gib per Prompt gestarteten Scans bis zu fünf Minuten Zeit, um große Repositorys zu initialisieren, statt sie nach 30 Sekunden wegen einer Zeitüberschreitung abzubrechen.
- Schließe Standard- und Tiefenscans auch dann ab, wenn ein Host die Länge von Tool-Namen begrenzt.

### Behebung nach Änderungen am Dateisystem weiterhin ermöglichen

- Behebe Befunde aus abgeschlossenen Scans auch dann, wenn sich die Gerätekennung des Dateisystems durch erneutes Einhängen geändert hat.
- Verlange weiterhin den ursprünglichen Checkout und die ursprüngliche Git-Revision, bevor du eine Korrektur anwendest.

## 0.1.17 (5. August 2026)

### Scanfortschritt in Echtzeit verfolgen

- Verfolge die aktuelle Scanphase, die verstrichene Zeit, aktive Worker, geprüfte Dateien und die Token-Nutzung in einer einzigen Fortschrittsansicht in Echtzeit.
- Verfolge den Fortschritt der Repository-Prüfung nach jeder abgeschlossenen Dateiprüfung, statt auf den Abschluss des Scans zu warten.

### Unterbrochene Tiefenscans fortsetzen

- Setze einen laufenden Tiefenscan nach einem Neustart des Koordinators fort, ohne bereits abgeschlossene Dateiprüfungen zu wiederholen.
- Behalte bereits ermittelte Ergebnisse der Schwachstellensuche, die Zuständigkeit für den Scan und ausstehende Aufgaben auch bei App-Updates oder unterbrochenen Scan-Sitzungen bei.

### Scans mit weniger Aufwand starten und abschließen

- Starte Standard-, Änderungs- und Tiefenscans direkt in nativen Arbeitsabläufen, ohne das ausgemusterte eingebettete Scan-Widget zu öffnen.
- Verwende Zusammenfassungen abgeschlossener Scans erneut, ohne jeden Befund neu zu laden, sofern du nicht die vollständigen strukturierten Ergebnisse anforderst.

## 0.1.16 (4. August 2026)

### Gemessenen Verbrauch bei Scans verfolgen

- Prüfe die Token-Nutzung des Hauptscans und seiner delegierten Worker insgesamt sowie aufgeschlüsselt nach Eingabe-Token, zwischengespeicherten Eingabe-Token und Ausgabe-Token.
- Unterscheide vollständige, teilweise verfügbare und nicht verfügbare Messungen, statt fehlende Nutzungsdaten als null anzuzeigen.

### Gründlichere Scans mit konsistenten Ergebnissen ausführen

- Verwende bei Standard- und Tiefenscans dieselben Phasen für Bedrohungsmodellierung, Erkennung, Validierung, Angriffspfadanalyse und Berichterstellung.
- Konfiguriere über die CLI oder das SDK die Worker für Tiefenscans, die Delegierung pro Worker, die Sättigung und die Grenzwerte für die Erkennung.
- Führe Tiefenscans mit der vom Modell unterstützten Worker-Laufzeitumgebung aus und stelle ältere Scan-Zustände wieder her, ohne den bestehenden Scan-Verlauf zu verlieren.
- Erstelle den Hauptbericht für Änderungs- und Tiefenscans, ohne dass separate Schwachstellenbeschreibungen oder Empfehlungen zur Härtung erforderlich sind.

### Korrekte Scan-Vorgaben und Repository-Ziele sicherstellen

- Aktualisiere die Sicherheitsvorgaben während eines laufenden Scans und gib sie an spätere Phasen und delegierte Worker für Tiefenscans weiter.
- Behalte Repository-URLs, Verweise auf Pull Requests und umfangreicheren Sicherheitskontext bei, ohne Netzwerkzugriff zuzulassen, den du nicht angefordert hast.
- Brich Scans mit einem Fehler ab, wenn sich das Repository oder das Scan-Ziel während der Ausführung ändert, damit Automatisierungen keine veralteten Befunde übernehmen.
- Berücksichtige in verwalteten Netzwerkumgebungen die Einstellungen für Unternehmensproxys und vertrauenswürdige Zertifikate.

### Verständlichere Schwachstellenberichte erstellen

- Erstelle durch Quellen belegte Schwachstellenberichte, die beobachtetes Verhalten von nicht verifizierten Hypothesen trennen.
- Beschreibe die Grenzen des Proof of Concept realistisch und nenne betroffene Versionen, Sicherheitsgrenzen sowie konkrete Hinweise zur Behebung.

## 0.1.15 (30. Juli 2026)

### Scan-Ergebnisse bei Änderungen am Repository erhalten

- Behalte die Zuordnung abgeschlossener Befunde und Berichte zur ursprünglichen Revision oder zum ursprünglichen Worktree-Snapshot bei, auch wenn sich Dateien oder die Repository-Revision während eines Scans ändern.
- Zeige beim Abschluss eine Warnung an, wenn sich der ausgewählte Code ändert oder das Ziel nicht mehr verfügbar ist, statt die Scan-Ergebnisse zu verwerfen.
- Archiviere einen bestehenden Scan, bevor du sein Ausgabeverzeichnis für einen anderen Scan wiederverwendest.

### Geprüftes Feedback zu Befunden übernehmen

- Halte eine Begründung fest, wenn du einen Befund als falsch positiv schließt.
- Übernimm geprüfte Einstufungen als falsch positiv in spätere Scans desselben Ziels, ohne sie auf einen anderen Checkout oder ein nicht zugehöriges Ziel anzuwenden.
- Unterdrücke einen wiederkehrenden Befund nur, wenn die frühere Begründung weiterhin auf den aktuellen Code und die Sicherheitsmaßnahmen zutrifft.

### Gültige Befunde wiederherstellen, ohne eine zu hohe Prüfabdeckung auszuweisen

- Behalte gültige Befunde bei, wenn ein anderer Befund, ein Bericht oder ein Härtungsartefakt fehlerhaft formatiert ist, und zeige eine Warnung zu den übersprungenen Daten an.
- Entferne doppelte Befunde und behalte den Befund bei, der nach Schweregrad, Konfidenz und stützenden Belegen am stärksten einzustufen ist.
- Kennzeichne die Prüfabdeckung als unvollständig, wenn Codex Befunde, Prüfnachweise oder Bereiche für Nachprüfungen nicht verifizieren kann.
- Nimm Warnungen zu unvollständiger Prüfabdeckung und aufgeschobenen Prüfungen in SARIF-Exporte auf.

### Scan-Einstellungen und Fortschritt sichtbar halten

- Speichere das ausgewählte Modell und den eingestellten Reasoning-Aufwand zusammen mit Standard- und Tiefenscans, damit Scan-Verlauf und Fortschritt auch nach dem Neuladen konsistent bleiben.
- Zeige die Anzahl laufender und abgeschlossener unabhängiger Prüfungen bei Tiefenscans an sowie den Zeitpunkt, an dem die Zusammenführung der Ergebnisse beginnt.
- Passe die Erkennungsphase von Standardscans an die verfügbare Worker-Kapazität an. Behalte dabei eine einzige Liste der Dateien im Prüfumfang und einen einzigen Prüfdurchlauf für Kandidaten bei.

### Weitere Repository- und Dateisystemstrukturen unterstützen

- Beziehe verschachtelte Git-Repositorys ein, wenn du einen Worktree-Snapshot erstellst.
- Behalte die genauen Dateipfade im Prüfumfang bei und berücksichtige Windows-Pfade ohne Unterscheidung zwischen Groß- und Kleinschreibung.
- Löse beim Preflight-Check des Scans einen konfigurierten `CODEX_HOME`-Pfad auf, der mit `~` beginnt.

## 0.1.14 (28. Juli 2026)

### Scan-Verlauf und wiederkehrende Befunde prüfen

- Filtere Repositorys, Befunde und den Scan-Verlauf mit einer begrenzten Anzahl an Ergebnissen pro Seite und klareren Statusdetails.
- Führe einen Scan mit seinen gespeicherten Einstellungen erneut aus und vergleiche abgeschlossene Scans, um neue, fortbestehende, behobene und nicht erneut gescannte Befunde zu unterscheiden.
- Gruppiere Worktrees aus demselben Repository und verwende in allen Ansichten stabile Identitäten für Repositorys und Befunde.

### Sicherheitsrichtlinie für das Repository definieren

- Verwende `$codex-security:define-security-policy`, um bereichsspezifische
Vorgaben in `SECURITY.md` zu Vertrauensgrenzen, Sicherheitsinvarianten, berichtenswerten Befunden,
  Schweregraden, Ausschlüssen und akzeptierten Risiken zu prüfen oder zu aktualisieren.
- Wende die nächstgelegene Richtliniendatei an, begrenze dabei ihre Größe und lehne symbolische Links ab, die aus dem Repository herausführen.

### Befunde vor der Nachverfolgung prüfen

- Wähle aus einem abgeschlossenen Scan bis zu 25 Befunde aus, um sie in Linear oder GitHub-Issues nachzuverfolgen.
- Gib die ausgewählten Befunde zur Prüfung und Genehmigung an Codex zurück, statt direkt im Workspace für Befunde Tickets zu erstellen.

### Standardscans mit einem einfacheren Ablauf ausführen

- Verwende für Standardscans von Repositorys und ausgewählten Pfaden eine einzige deterministisch erstellte Liste der Dateien im Prüfumfang und ein kompaktes Kandidatenprotokoll.
- Behalte die vorhandenen Ausgaben für Manifest, Befunde, Prüfabdeckung, Bericht und SARIF bei und reduziere zugleich wiederholte Scan-Phasen.

## 0.1.13 (25. Juli 2026)

### Befunde in weiteren Umgebungen prüfen

- Behalte tatsächliche Sicherheitsbefunde auch dann bei, wenn der betroffene Code lokal vorliegt, intern oder für Trainingszwecke verwendet wird oder nicht in einer Produktionsumgebung bereitgestellt ist.
- Berücksichtige den Kontext der Bereitstellung und Exposition, um Schweregrad und Konfidenz angemessen einzustufen, statt den Befund automatisch zu unterdrücken.

## 0.1.12 (23. Juli 2026)

### Tiefenscans mit klarerer Fortschrittsanzeige ausführen

- Führe Tiefenscans aus, die Worker über ein gesamtes Repository oder ein ausgewähltes Verzeichnis hinweg koordinieren.
- Übernimm deine Einstellungen für das Modell und den Reasoning-Aufwand in delegierte Scan-Aufgaben.
- Sieh dir vor und während eines Scans die Ergebnisse des Preflight-Checks, den Scan-Fortschritt, die verfügbare Worker-Kapazität und das Fallback-Verhalten an.

### Frühere Scans prüfen und erneut ausführen

- Öffne aktuelle und frühere Scans über die Liste der Sicherheitsscans.
- Öffne einen gespeicherten Scan erneut im Workspace für Befunde oder führe ihn erneut aus, um die Ergebnisse zu aktualisieren.
- Erhalte klarere Angaben zum Abschlussstatus sowie konsistentere Befunddetails und einen konsistenteren Scan-Verlauf.

### Scans mit weniger Unterbrechungen konfigurieren

- Starte Scans über den integrierten Setup-Ablauf, ohne deine aktuelle Aufgabe zu verlassen.
- Behalte das Scan-Setup im Seitenbereich, auch wenn Codex im Vollbildmodus ist.
- Blende das Setup aus, wenn du es nicht brauchst, und behalte diese Einstellung für spätere Scans bei.

### Validierte Befunde überprüfen und beheben

- Behalte validierte Befunde mit geringem Schweregrad in den Ergebnissen abgeschlossener Scans bei.
- Prüfe die konsistenteren Befunddetails in Scans, Berichten und Exporten.
- Versuche die Behebung erneut und übernimm den relevanten Scankontext in nachfolgende Korrekturen.

### Ergebnisse für bestehende Arbeitsabläufe im Sicherheitsbereich exportieren

- Exportiere Befunde aus abgeschlossenen Scans als JSON, CSV oder SARIF.
- Generiere SARIF-Ergebnisse lokal für Code-Scanning-Integrationen und die Anbindung von Sicherheitstools.
- Behalte konsistente Befunddetails in allen Exportformaten bei.

## 0.1.11 (10. Juli 2026)

### Detaillierte Berichte zu Befunden und Härtungsmaßnahmen erstellen

- Erstelle für jeden berichtsrelevanten Scanbefund einen durch Quellcode belegten Schwachstellenbericht. Ergänze unterstützende Proof-of-Concept-Dateien, sofern sie verfügbar sind.
- Prüfe ein Portfolio zur strukturellen Härtung, das sämtliche Befunde, Zielkonflikte im Engineering, Migrationsoptionen und unterstützende Diagramme analysiert.
- Nutze `report.md` als Einstiegspunkt zu diesen abgeleiteten Ausgaben unter `findings/`
  und `hardening/`. Halte beim Teilen oder Archivieren der Ergebnisse
  das gesamte Scanverzeichnis zusammen.

### Arbeitsabläufe zur Berichterstellung direkt ausführen

- Nutze `$codex-security:vulnerability-writeup`, um aus Offenlegungsdokumenten,
  vorläufigen Befunden, PoCs und Quellcode ausgearbeitete Berichte zu erstellen, ohne zuvor
  einen Scan mit Codex Security auszuführen.
- Nutze `$codex-security:propose-security-hardening`, um anhand von Scans, Befunden,
  Vorfall- oder Bewertungsdokumenten und Quellcode beleggestützte
  strukturelle oder architektonische Optionen zu entwickeln.

### Repository-Vorgaben konsequent anwenden und die Prüfabdeckung vereinheitlichen

- Definiere den Kontext des Bedrohungsmodells, Sicherheitsinvarianten, Kriterien für berichtsrelevante Befunde,
  Ausschlüsse und den Kontext für die Schweregradeinstufung in `SECURITY.md`-Dateien im Stammverzeichnis oder in Unterverzeichnissen.
  Die nächstgelegene zutreffende Datei hat Vorrang.
- Verbessere vor der Validierung die Abdeckung der Repository-Überprüfung. Halte dabei ausdrücklich zurückgestellte Bereiche und Nachweislücken weiterhin fest.
- Prüfe bei Änderungsscans gelöschte Quelldateien und erweitere vor der Validierung die standardmäßige Abdeckung der Repository-Überprüfung.
- Prüfe vor dem Start eines Tiefenscans die Skills für seine einzelnen Phasen, die delegierten Worker und die Worker-Kapazität.

## 0.1.10 (23. Juni 2026)

### Übernahme von Jira- und Linear-Tickets verbessern

- Frage vor dem Import von Linear-Unteraufgaben nach und behalte in den Ergebnissen die Beziehungen zwischen über- und untergeordneten Aufgaben bei.
- Unterscheide zwischen fehlenden Verbindungen, unzureichenden Berechtigungen, nicht zugänglichen Tickets und vorübergehenden Konnektorausfällen.
- Brich den Vorgang ab, statt eine Bewertung abzugeben, wenn der angeforderte Ticketinhalt nicht verfügbar ist.
- Vergib ab `1` eindeutige positive ganzzahlige Rangnummern in jeder Warteschlange für bestätigte
  oder noch zu überprüfende Befunde.

### Codeänderungen zuverlässiger überprüfen

- Vergleiche einen untersuchten Commit mit seinem tatsächlichen Vorgänger-Commit und behalte das Diff-Ziel im Workspace für Befunde bei.
- Melde, wenn der Patch-Status nicht verfügbar ist, statt eine andere Änderung zu überprüfen.
- Prüfe die konsistenteren Triage-Ergebnisse und Kontextinformationen zu Befunden.

## 0.1.9 (18. Juni 2026)

### Scans im Workspace für Befunde überprüfen

- Überprüfe abgeschlossene Scans in einem eigenen Workspace, der Befunde, Abdeckung, Schweregrad, Konfidenz und Scan-Artefakte zusammenführt.
- Filtere und sortiere Befunde, auch nach der höchsten Konfidenz. Der Zustand deines Workspaces bleibt bei Aktualisierungen erhalten.
- Öffne einen Befund, um Belege aus dem Quellcode, Validierungsdetails, Erreichbarkeit, Auswirkungen und Hinweise zur Behebung an einem Ort zu prüfen.

### Scans mit weniger Setup-Aufwand ausführen

- Führe Standardscans für Git-Repositorys, einzelne Ordner oder Codebasen ohne Git-Verlauf aus. Tiefenscans können ebenfalls einen bestimmten Ordner prüfen.
- Brich einen aktiven Scan explizit ab, setze einen unterbrochenen Scan ohne erneute Setup-Aufforderung fort und erhalte eine Warnung, bevor du mehrere Tiefenscans gleichzeitig startest.
- Verfolge Setup und Fortschritt anhand klarerer Statusangaben und kompakterer Fortschrittsübersichten. Fehler bleiben sichtbar, bis du sie behebst.

### Übertragbare und überprüfbare Ergebnisse exportieren

- Verwende für abgeschlossene Scans ein einheitliches Format mit einem Manifest, strukturierten Befunden, Abdeckungsdaten und einem Markdown-Bericht, der aus demselben kanonischen Ergebnis abgeleitet wird.
- Exportiere Befunde als JSON, CSV oder SARIF zur Analyse, Archivierung und Integration mit anderen Sicherheitstools.
- Schließe Scans zuverlässiger ab, auch wenn Windows-Pfade oder Scan-Sperren den Zugriff auf das Dateisystem beeinträchtigen.

### Vorhandene Befunde bewerten und nachverfolgen

- Bewerte vorhandene Befunde aus Scannern, Sicherheitshinweisen, Bug-Bounty-Berichten, GitHub, Jira, Linear oder Ergebnissen von Codex Security anhand der aktuellen Codebasis. Der Triage-Ablauf liefert eine beleggestützte Bewertung und eine priorisierte Maßnahmenliste.
- Verfolge ausgewählte validierte Befunde in Linear, Jira oder GitHub-Issues oder erstelle einen privaten Entwurf für ein GitHub Security Advisory, wenn das Repository die dafür geltenden Anforderungen erfüllt.
- Prüfe die Ergebnisse der Duplikatsuche, den Quellkontext, die Sichtbarkeit am Ziel und den genauen vorgeschlagenen Inhalt, bevor du einen Schreibvorgang genehmigst. Codex liest das Ergebnis nach der Erstellung oder Aktualisierung erneut ein, um es zu verifizieren.

## 0.1.7 (4. Juni 2026)

### Beleggestützte Sicherheits-Reviews durchführen

- Scanne ein zur Prüfung autorisiertes Repository oder einen ausgewählten Ordner auf Sicherheitslücken.
- Durchsuche ein gesamtes Repository wiederholt nach Schwachstellen, wenn du eine gründlichere Prüfabdeckung benötigst.
- Prüfe Pull Requests, Commits, Unterschiede zwischen Branches und lokale Patches auf Sicherheitsregressionen.
- Bearbeite jeden potenziellen Befund in den Phasen Bedrohungsmodellierung, Befundermittlung, Validierung und Auswirkungsanalyse, bevor du Scanberichte erstellst.
- Behebe einen akzeptierten Befund mit einem gezielten Patch. Ergänze Regressionstests und überprüfe das ursprüngliche Problem.
