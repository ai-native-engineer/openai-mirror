<!-- source: https://learn.chatgpt.com/de-DE/docs/security/plugin/workbench -->

Die Security-Workbench bündelt deine Scans, Befunde und Repositorys
in der Codex-Desktop-App. Codex analysiert den Scan im Rahmen einer regulären Aufgabe. Die Workbench
hält den Scan und seine Ergebnisse bereit, wenn du zurückkehrst.

Öffne in der ChatGPT-Desktop-App das ChatGPT-Dropdown-Menü und wähle **Codex** aus.
Installiere und aktiviere das [Codex-Security-Plugin](/de-DE/codex/security/plugin) und wähle anschließend
 **Sicherheit** in der Seitenleiste aus.

  Wenn **Sicherheit** nicht angezeigt wird, prüfe, ob **Codex** ausgewählt und das
  Plug-in installiert und aktiviert ist. Aktualisiere bei Bedarf die Desktop-App und das Plug-in
  und prüfe, ob deine Workspace-Administration das Plug-in zulässt.

## Einen Scan starten

Verwende für die beste Scanqualität <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
mit dem Reasoning-Aufwand `xhigh`.

1. Öffne **Scans** und wähle **+ Scan** aus.
2. Wähle ein vorhandenes Repository oder einen anderen Ordner aus.
3. Wähle **Codebasis** , um ein Repository zu scannen, oder **Änderungen** , um eine
   Git-basierte Änderung zu überprüfen.
4. Wähle für einen Standardscan das gesamte Repository oder einen Ordner als Codebasis aus.
5. Wähle für einen Tiefenscan zunächst das Repository oder den Ordner als Codebasis aus und
   aktiviere dann **Tiefenscan**. Tiefenscans überprüfen die gesamte ausgewählte Codebasis.
6. Wähle für einen Scan von Änderungen noch nicht committete Änderungen, einen Commit oder einen
   Revisionsbereich aus. **Tiefenscan** ist bei Scans von Änderungen nicht verfügbar.
7. Wähle ein Modell und einen Reasoning-Aufwand aus. Öffne den Bereich **Zusätzlicher Kontext** , um
   relevante Angriffsvektoren, Schwerpunkte oder weiteren sicherheitsrelevanten Kontext zu beschreiben.
8. Wähle **Scan starten** aus.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Wähle ein Repository aus und konfiguriere einen Scan in der Security-Workbench.
  </figcaption>
</figure>

Unter [Sicherheitsscan durchführen](/de-DE/codex/security/plugin/scans), [Umfassenden Sicherheitsscan
durchführen](/de-DE/codex/security/plugin/deep-scans) oder [Codeänderungen auf
Sicherheitsprobleme überprüfen](/de-DE/codex/security/plugin/code-changes) findest du Details zu den einzelnen
Scanarten.

## Scanfortschritt verfolgen

Auf der Scanseite siehst du die aktuelle Phase und den vom Plug-in gemeldeten Fortschritt.
Die Phasen eines Standardscans umfassen Bedrohungsmodellierung, Erkundung, Validierung,
Auswirkungs- und Pfadanalyse, Berichterstellung sowie Abschluss.

Wähle **Aktivität anzeigen** , um die Codex-Aufgabe zu öffnen, die den Scan ausführt. Du kannst
die Workbench verlassen und zu **Scans** zurückkehren, ohne einen gespeicherten Scan zu verlieren. Wenn du die
Ausführung gezielt stoppen möchtest, öffne den Scan und wähle **Scan stoppen** aus.

Öffne nach Abschluss des Scans die Ergebnisse, um Ziel, Revision,
Befunde, Abdeckung und verfügbare Berichtsartefakte zu prüfen.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Prüfe Befunde, Schweregrade, Scanabdeckung und Artefakte, sobald ein Scan
abgeschlossen ist.
  </figcaption>
</figure>

## Befunde scanübergreifend überprüfen

Öffne **Befunde** , um gespeicherte Befunde aus verschiedenen Repositorys und Scans zu prüfen.
Durchsuche oder filtere die Liste und wähle dann einen Befund aus, um dessen Zusammenfassung, Belege aus dem
Quellcode, Validierung und Auswirkungen zu prüfen.

Unter **Zusammenfassung** findest du Details zum Befund. Verwende **Patch** , um eine gezielte Korrektur zu erstellen,
zu prüfen, anzuwenden oder zu verifizieren. Den Ablauf zur Behebung findest du unter [Sicherheitsbefunde beheben und
verifizieren](/de-DE/codex/security/plugin/fix-findings).

  Der Tab **Befunde** zeigt Befunde aus gespeicherten Scans von Codex Security. Importierte
  Tickets und andere bestehende Sicherheitsprobleme gehören weiterhin zum separaten
[Ablauf zur Backlog-Triage](/de-DE/codex/security/plugin/triage-backlog).

## Repository-Verlauf einsehen

Öffne **Repositorys** , um die verfügbaren Repositorys und Ordner zu durchsuchen. Wähle ein
Repository aus, um seinen Scanverlauf, die zuletzt gescannte Revision und offene
Befunde zu prüfen. In den Repository-Details kannst du einen früheren Scan öffnen oder die
diesem Repository zugeordneten Befunde anzeigen.

Wenn für ein Repository noch keine Scans vorliegen, starte in den Repository-Details einen Scan oder wähle **+ Scan**
in der Workbench aus.

## Einen Scan aus einem Chat starten

Du kannst Codex auch in einem normalen
Chat bitten, das installierte Codex-Security-Plugin auszuführen. Scans, die die gemeinsame Plug-in-Workbench nutzen, werden unter **Scans** angezeigt.
So kannst du ihren Fortschritt und ihre Ergebnisse später wieder in der Security-Workbench aufrufen.

Informationen zu Scans im Terminal und zur Automatisierung findest du im [Schnellstart für die
Codex Security CLI](/de-DE/codex/security/cli).
