<!-- source: https://learn.chatgpt.com/de-DE/docs/security/plugin/deep-scans -->

Führe einen Tiefenscan durch, wenn du eine gründlichere Überprüfung benötigst und eine längere
Laufzeit in Kauf nehmen kannst. Tiefenscans durchsuchen ein Repository umfassender und können die
Variabilität zwischen den Durchläufen verringern.

Beginne mit einem [Standardscan](/de-DE/codex/security/plugin/scans), um den Scanumfang
und die Ergebnisse zu prüfen. Verwende anschließend einen Tiefenscan, wenn du eine gründlichere Bewertung benötigst.

## Zwischen Standard- und Tiefenscans wählen

|                         | Standardscan                                      | Tiefenscan                                             |
| ----------------------- | -------------------------------------------------- | ----------------------------------------------------- |
| Am besten geeignet für                | Erste Durchläufe und routinemäßige Überprüfungen von Repositorys oder Ordnern | Gründlichere Überprüfungen nach einem Standardscan           |
| Variabilität             | Standard                                           | Reduziert                                               |
| Umfang                   | Repository oder ausdrücklich angegebener Ordner                      | Repository oder ausdrücklich angegebener Ordner                         |
| Laufzeit und Ressourcen   | Geringer                                              | Höher                                                |
| Pull Requests und Diffs | Ablauf zur Überprüfung von Änderungen verwenden                     | Nicht unterstützt; verwende stattdessen den Ablauf zur Überprüfung von Änderungen |

## Laufzeit für Tiefenscans konfigurieren

Um Parallelität und Dauer eines Tiefenscans zu steuern, erstelle oder bearbeite die Datei
`~/.codex/codex-security/config.toml`. Wenn du `CODEX_HOME` festgelegt hast, verwende stattdessen
`$CODEX_HOME/codex-security/config.toml`.

Dieses Profil führt beispielsweise einen kürzeren Scan mit begrenzter Parallelität durch:

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

| Einstellung                         | Standardwert | Beschreibung                                                                                                        |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| `workers`                       | `4`     | Anzahl der unabhängigen Standardscan-Worker, die gleichzeitig ausgeführt werden dürfen. Der ältere Wert `"auto"` entspricht ebenfalls `4`. |
| `subagents`                     | `3`     | Anzahl der Subagenten, die jeder Worker starten darf. Lege `0` fest, um sie zu deaktivieren.                                                |
| `stop_after_no_new`             | `4`     | Beende den Scan, sobald die angegebene Anzahl aufeinanderfolgender abgeschlossener Worker-Scans keine neuen Befunde liefert.                                   |
| `stop_after_consecutive_errors` | `3`     | Beende den Scan nach der angegebenen Anzahl aufeinanderfolgender Worker-Fehler.                                                                    |
| `max_discovery_runs`            | `40`    | Begrenze die Anzahl unabhängiger Standardscan-Durchläufe vor der Zusammenführung.                                             |
| `max_time_hours`                | `96`    | Begrenze die Ausführungsdauer der Worker auf eine positive Stundenzahl von höchstens `96`; gib bei Bedarf auch Bruchteile einer Stunde an.                          |

Niedrigere Werte können die Scandauer und den Token-Verbrauch reduzieren, aber dazu führen, dass Befunde übersehen werden.
Konfigurationsänderungen gelten für neue Tiefenscans, nicht für bereits laufende Scans.

Wenn das Zeitlimit abläuft, stoppt Codex Security noch laufende Worker, behält
die Ergebnisse abgeschlossener Scans bei und führt sie im Abschlussbericht zusammen. Wenn kein Worker
die Quellcodeprüfung vor Ablauf der Frist abschließt, vermerkt der Bericht eine nur teilweise
Abdeckung.

Die Einstellung `max_time_hours` setzt die Plug-in-Version `0.1.19` oder höher voraus. Einzelheiten zur Veröffentlichung findest du im
[Änderungsprotokoll des Plug-ins](/de-DE/codex/security/plugin/changelog).

## Tiefenscan starten

Öffne in der Desktop-App **Sicherheit**, wähle **Scans** und anschließend **+ Scan**.
Wähle ein Repository oder einen anderen Ordner aus, wähle **Codebasis** und aktiviere
**Tiefenscan**. Der Scan umfasst das gesamte ausgewählte Repository oder den gesamten ausgewählten Ordner.

Du kannst einen Tiefenscan für das gesamte Repository auch in einer Codex-Unterhaltung starten:

```text
Use $codex-security:deep-security-scan to run a deep security scan of this repository.

Gib für eine einzelne Komponente in einem Monorepo den Ordner ausdrücklich an:

```text
Use $codex-security:deep-security-scan to run a deep security scan of /absolute/path/to/repository/services/payments.

Wähle für einen gezielt eingegrenzten Tiefenscan in der Desktop-App den Ordner als Codebasis aus.
Der Scan umfasst den gesamten ausgewählten Ordner.

## Setup und Vorabprüfung bestätigen

Verwende für die beste Scanqualität <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
mit dem Reasoning-Aufwand `xhigh`.

1. Wähle **Codebasis** und aktiviere **Tiefenscan**.
2. Vergewissere dich, dass das Repository oder der ausgewählte Ordner den Code enthält, den du
scannen möchtest.
3. Wähle ein Modell und den Reasoning-Aufwand aus.
4. Öffne **Zusätzlicher Kontext** , um konkrete Angriffsvektoren, sensible
   Anwendungsbereiche oder Kontext zum Repository anzugeben, der nicht aus dem Code hervorgeht.
5. Wähle **Scan starten** aus.

Worker für Tiefenscans übernehmen das von dir ausgewählte Modell und deine Einstellungen für den Reasoning-Aufwand. Jeder
Worker führt einen vollständigen Standardscan durch, und Codex Security führt die
Ergebnisse abgeschlossener Scans zusammen. Verfolge den gespeicherten Scan unter **Scans** oder wähle **Aktivität
anzeigen** , um die zugehörige Codex-Aufgabe zu überprüfen. Lies das [Änderungsprotokoll
des Plug-ins](/de-DE/codex/security/plugin/changelog), bevor du das Plug-in aktualisierst oder
einen lang andauernden Scan startest.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Verfolge die aktive Phase des Tiefenscans und prüfe die zugehörige Codex-Aktivität, bevor du
das fertige Ergebnis überprüfst.
  </figcaption>
</figure>

## Ergebnis überprüfen

Tiefenscans verwenden dieselben gespeicherten Scandetails und dasselbe vollständige Scanverzeichnis wie
Standardscans. Öffne den abgeschlossenen Scan unter **Scans** oder überprüfe seine Befunde unter
**Befunde**. Die generierte Datei `report.md` verlinkt auf ausführliche Schwachstellenberichte
oder Hinweise zur strukturellen Härtung, wenn du diese Ausgaben anforderst.
Bewahre alle verknüpften Verzeichnisse `findings/` und `hardening/` zusammen mit dem Bericht auf, wenn du
das Ergebnis teilst oder archivierst.

Überprüfe zuerst die Zusammenfassung der Abdeckung und danach die Befunde. Auch ein Tiefenscan hat Grenzen.
Prüfe deshalb zurückgestellte Bereiche und verbleibende Nachweislücken, bevor du eine
Schlussfolgerung ziehst. Wenn du einen Befund akzeptierst, fahre mit [Befund beheben und
überprüfen](/de-DE/codex/security/plugin/fix-findings) fort.

Um einen Pull Request, einen Commit, einen Branch-Bereich oder einen lokalen Patch zu überprüfen, verwende [Codeänderungen
überprüfen](/de-DE/codex/security/plugin/code-changes). Ein Tiefenscan ersetzt niemals den
auf Diffs ausgerichteten Ablauf.
