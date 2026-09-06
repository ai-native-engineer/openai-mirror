<!-- source: https://learn.chatgpt.com/de-DE/docs/security/setup -->

Diese Seite führt dich vom ersten Zugriff über die Prüfung der Befunde bis zu Pull Requests zur Behebung in Codex Security Cloud.

  Vergewissere dich zunächst, dass du Codex Cloud eingerichtet hast. Falls nicht, findest du unter [Codex
  Cloud](/de-DE/codex/cloud) die ersten Schritte.

## 1. Zugriff und Umgebung

Codex Security Cloud scannt GitHub-Repositorys, die über
[Codex Cloud](/de-DE/codex/cloud) verbunden sind.

- Vergewissere dich, dass dein Workspace auf Codex Security Cloud zugreifen kann.
- Vergewissere dich, dass das Repository, das du scannen möchtest, in Codex Cloud verfügbar ist.

Öffne [Codex-Umgebungen](https://chatgpt.com/codex/settings/environments) und prüfe, ob für das Repository bereits eine Umgebung vorhanden ist. Falls nicht, erstelle dort eine, bevor du fortfährst.

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 2. Neuer Sicherheitsscan

Sobald die Umgebung vorhanden ist, öffne [Sicherheitsscan erstellen](https://chatgpt.com/codex/security/scans/new) und wähle das gerade verbundene Repository aus.

Codex Security scannt Repositorys zunächst von den neuesten Commits aus rückwärts. So erstellt und aktualisiert es den Scan-Kontext, wenn neue Commits hinzukommen.

So konfigurierst du ein Repository:

1. Wähle die GitHub-Organisation aus.
2. Wähle das Repository aus.
3. Wähle den Branch aus, den du scannen möchtest.
4. Wähle die Umgebung aus.
5. Wähle ein **Verlaufsfenster** aus. Längere Verlaufsfenster liefern mehr Kontext, doch der Backfill dauert entsprechend länger.
6. Klicke auf **Erstellen**.

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 3. Erste Scans können eine Weile dauern

Beim Erstellen des Scans führt Codex Security zunächst im ausgewählten Verlaufsfenster eine Sicherheitsprüfung auf Commit-Ebene durch.
Der anfängliche Backfill kann einige Stunden dauern, besonders bei größeren Repositorys oder längeren Verlaufsfenstern.
Wenn nicht sofort Befunde angezeigt werden, ist das normal. Warte, bis der erste Scan abgeschlossen ist, bevor du ein Ticket öffnest oder mit der Fehlerbehebung beginnst.

  Die Ersteinrichtung des Scans erfolgt automatisch und umfassend. Das kann einige Stunden dauern. Sei nicht beunruhigt, wenn die ersten Befunde mit Verzögerung angezeigt werden.

## 4. Scans überprüfen und das Bedrohungsmodell verbessern

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

Öffne nach Abschluss des ersten Scans den Scan und überprüfe das generierte Bedrohungsmodell.
Sobald die ersten Befunde vorliegen, aktualisiere das Bedrohungsmodell, damit es deine Architektur, Vertrauensgrenzen und deinen Geschäftskontext korrekt abbildet.
So kann Codex Security die Probleme für dein Team priorisieren.

  Wenn du die Scan-Ergebnisse verändern möchtest, passe das Bedrohungsmodell an deinen aktualisierten Geltungsbereich, deine Prioritäten und deine Annahmen an.

Wenn die ersten Befunde vorliegen, prüfe das Modell erneut, damit sich der Scan weiterhin an den aktuellen Prioritäten orientiert.
Halte das Modell auf dem neuesten Stand, damit Codex Security bessere Vorschläge machen kann.

Ausführlichere Informationen zu Bedrohungsmodellen und ihren Auswirkungen auf Kritikalität und Triage findest du unter [Bedrohungsmodell verbessern](/de-DE/codex/security/threat-model).

## 5. Befunde überprüfen und beheben

Überprüfe nach Abschluss des ersten Backfills die Befunde in der Ansicht **Befunde** .

Du kannst zwei Ansichten verwenden:

- **Empfohlene Befunde**: eine laufend aktualisierte Top-10-Liste der kritischsten Probleme im Repository
- **Alle Befunde**: eine sortier- und filterbare Tabelle mit Befunden aus dem gesamten Repository

  
    
  

Klicke auf einen Befund, um die zugehörige Detailseite mit folgenden Informationen zu öffnen:

- eine kurze Beschreibung des Problems
- wichtige Metadaten wie Commit-Details und Dateipfade
- eine kontextbezogene Einschätzung der Auswirkungen
- relevante Codeausschnitte
- Kontext zum Aufrufpfad oder Datenfluss, sofern verfügbar
- Validierungsschritte und -ausgaben

Du kannst jeden Befund überprüfen und direkt auf seiner Detailseite einen PR erstellen.

## Weitere Dokumentation

- [Codex Security](/de-DE/codex/security) bietet einen Überblick über das Produkt.
- [Codex Security Cloud-FAQ](/de-DE/codex/security/faq) behandelt häufige Fragen zur Cloud.
- [Bedrohungsmodell verbessern](/de-DE/codex/security/threat-model) erklärt, wie du den Scan-Kontext und die Priorisierung von Befunden optimierst.
