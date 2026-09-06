<!-- source: https://learn.chatgpt.com/de-DE/docs/environments/local-environment -->

Mit lokalen Umgebungen kannst du Setup-Schritte für Worktrees sowie häufig verwendete Aktionen für ein Projekt konfigurieren.

  Lokale Umgebungen sind nur in Codex innerhalb der ChatGPT-Desktop-App verfügbar.
  Wähle **Codex** aus, bevor du eine lokale Umgebung konfigurierst oder verwendest.

Du konfigurierst deine lokalen Umgebungen im Bereich [Einstellungen der ChatGPT-Desktop-App](codex://settings). Du kannst die erstellte Datei in das Git-Repository deines Projekts einchecken, um sie mit anderen zu teilen.

Codex speichert diese Konfiguration im Ordner `.codex` im Stammverzeichnis deines
Projekts. Wenn dein Repository mehr als ein Projekt enthält, öffne das
Projektverzeichnis mit dem gemeinsamen Ordner `.codex`.

## Setup-Skripte

Da Worktrees andere Verzeichnisse als deine lokalen Chats verwenden, ist dein Projekt möglicherweise nicht vollständig eingerichtet. Eventuell fehlen Abhängigkeiten oder Dateien, die nicht in dein Repository eingecheckt wurden. Setup-Skripte werden automatisch ausgeführt, wenn Codex zu Beginn eines neuen Chats einen neuen Worktree erstellt.

Mit diesem Skript kannst du alle Befehle ausführen, die zum Konfigurieren deiner Umgebung erforderlich sind, etwa zum Installieren von Abhängigkeiten oder zum Ausführen eines Build-Prozesses.

Für ein TypeScript-Projekt kannst du beispielsweise ein Setup-Skript verwenden, um die Abhängigkeiten zu installieren und einen ersten Build auszuführen:

```bash
npm install
npm run build

Wenn dein Setup plattformspezifisch ist, definiere Setup-Skripte für macOS, Windows oder Linux, um das Standardskript zu überschreiben.

## Aktionen

<section class="feature-grid">

<div>
Mit Aktionen kannst du häufig verwendete Aufgaben definieren, zum Beispiel das Starten des Entwicklungsservers deiner App oder das Ausführen deiner Testsuite. Diese Aktionen werden für den schnellen Zugriff in der oberen Leiste der ChatGPT-Desktop-App angezeigt. Sie werden im [integrierten Terminal](/de-DE/codex/integrated-terminal) der App ausgeführt.

Aktionen ersparen dir, häufig verwendete Befehle immer wieder einzugeben, etwa um einen Build für dein Projekt auszulösen oder einen Entwicklungsserver zu starten. Wenn du nur einmal kurz debuggen möchtest, kannst du das integrierte Terminal direkt verwenden.

</div>

  
    
  

</section>

Für ein Node.js-Projekt könntest du beispielsweise eine Aktion namens „Ausführen“ mit dem folgenden Skript erstellen:

```bash
npm start

Wenn die Befehle deiner Aktion plattformspezifisch sind, definiere plattformspezifische Skripte für macOS, Windows und Linux.

Wähle für jede Aktion ein passendes Symbol aus, damit du sie leichter unterscheiden kannst.

## Integrierte Git-Tools verwenden

<div class="my-8 grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-center">

<div>

In Codex stellt die ChatGPT-Desktop-App neben jedem lokalen Projekt und Worktree
gängige Git-Bedienelemente bereit. Der Diff-Bereich zeigt Änderungen im aktuellen Checkout
und ermöglicht es dir, Inline-Kommentare hinzuzufügen, die Codex bearbeiten soll. Du kannst einzelne
Änderungsblöcke oder ganze Dateien stagen oder zurücksetzen, Änderungen committen, einen Branch pushen und
einen Pull Request erstellen, ohne die App zu verlassen.

Verwende das [integrierte Terminal](/de-DE/codex/integrated-terminal) für Git-Operationen,
die in der App nicht verfügbar sind. Um parallele Änderungen von deinem
lokalen Checkout getrennt zu halten, starte die Aufgabe in einem [Worktree](/de-DE/codex/environments/git-worktrees).

</div>

  

</div>
