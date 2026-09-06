<!-- source: https://learn.chatgpt.com/de-DE/docs/environments/git-worktrees -->

Mit Worktrees kann Codex mehrere unabhängige Chats im selben Projekt ausführen, ohne dass sie sich gegenseitig beeinträchtigen. Das Repository, der Worktree und die Befehle verbleiben auf dem Computer oder in der Remote-Entwicklungsumgebung des Projekts. Du kannst direkt in der ChatGPT-Desktop-App arbeiten oder in der mobilen ChatGPT-App [Remote](/de-DE/codex/remote) verwenden, um Worktree-Chats auf einem verbundenen Computer zu starten, zu steuern, zu genehmigen und zu überprüfen.

In Git-Repositories können [geplante Aufgaben](/de-DE/codex/automations) in eigenen Worktrees im Hintergrund ausgeführt werden, damit sie deine laufende Arbeit nicht beeinträchtigen. In Projekten ohne Versionsverwaltung werden geplante Aufgaben direkt im Projektverzeichnis ausgeführt. Du kannst Chats außerdem manuell in einem Worktree starten und sie mithilfe der Übergabe zwischen Lokal und Worktree verschieben.

  Worktrees werden nicht lokal auf deinem Smartphone ausgeführt. Mit Remote steuert die mobile App Codex auf deinem verbundenen Computer, auf dem das Repository und der Worktree verbleiben, oder in der Remote-Entwicklungsumgebung, die dieser Computer verwendet. Die folgenden Anweisungen für die Desktop-App beziehen sich auf den verbundenen Computer.

## Was ist ein Worktree?

Worktrees funktionieren nur in Projekten, die Teil eines Git-Repositorys sind, weil intern [Git-Worktrees](https://git-scm.com/docs/git-worktree) zum Einsatz kommen. Mit einem Worktree kannst du eine zweite Kopie („Checkout“) deines Repositorys erstellen. Jeder Worktree enthält eine eigene Kopie aller Dateien im Repository. Alle Worktrees greifen jedoch auf dieselben Metadaten im Ordner `.git` zu, darunter Informationen zu Commits, Branches usw. So kannst du mehrere Branches parallel auschecken und bearbeiten.

## Terminologie

- **Lokaler Checkout**: Das von dir erstellte Repository. In der ChatGPT-Desktop-App wird es manchmal einfach als **Lokal** bezeichnet.
- **Worktree**: Ein [Git-Worktree](https://git-scm.com/docs/git-worktree), der in der ChatGPT-Desktop-App aus deinem lokalen Checkout erstellt wurde.
- **Übergabe**: Der Ablauf, über den ein Chat zwischen Lokal und Worktree verschoben wird. Codex übernimmt die erforderlichen Git-Vorgänge, um deine Arbeit sicher zwischen beiden zu verschieben.

## Warum einen Worktree verwenden?

1. Arbeite parallel mit Codex, ohne dein aktuelles Setup in Lokal zu beeinträchtigen.
2. Plane Aufgaben für den Hintergrund ein und konzentriere dich weiter auf die Arbeit im Vordergrund.
3. Verschiebe einen Chat später nach Lokal, wenn du die Änderungen überprüfen oder testen oder direkter mit anderen zusammenarbeiten möchtest.

## Erste Schritte

Worktrees setzen ein Git-Repository voraus. Achte darauf, dass das ausgewählte Projekt Teil eines Git-Repositorys ist.

1.  „Worktree“ auswählen

    Wähle in der Ansicht für einen neuen Chat unterhalb des Editors **Worktree** aus.
    Optional kannst du eine [lokale Umgebung](/de-DE/codex/environments/local-environment) auswählen, um Setup-Skripts für den Worktree auszuführen.

2.  Ausgangs-Branch auswählen

    Wähle unterhalb des Editors den Git-Branch aus, auf dem der Worktree basieren soll. Das kann dein Branch `main` / `master`, ein Feature-Branch oder dein aktueller Branch mit lokalen Änderungen sein, die noch nicht für einen Commit vorgemerkt wurden.

3.  Prompt absenden

    Sende deinen Prompt ab. Codex erstellt daraufhin einen Git-Worktree auf Basis des ausgewählten Branches. Standardmäßig arbeitet Codex mit einem [„detached HEAD“](https://git-scm.com/docs/git-checkout#_detached_head).

4.  Ort für die weitere Arbeit auswählen

    Wenn du so weit bist, kannst du entweder direkt im Worktree weiterarbeiten oder den Chat an deinen lokalen Checkout übergeben. Bei der Übergabe zwischen Lokal und einem Worktree werden sowohl dein Chat _als auch_ dein Code verschoben, sodass du im jeweils anderen Checkout weiterarbeiten kannst.

## Zwischen Lokal und Worktree arbeiten

Worktrees ähneln deinem lokalen Checkout in Bedienung und Verhalten. Der Unterschied liegt darin, wie sie sich in deinen Arbeitsablauf einfügen. Betrachte Lokal als Vordergrund und Worktree als Hintergrund. Mit der Übergabe kannst du einen Chat zwischen beiden verschieben.

Im Hintergrund übernimmt die Übergabe die erforderlichen Git-Vorgänge, um Arbeit sicher zwischen zwei Checkouts zu verschieben. Das ist wichtig, denn **Git erlaubt das Auschecken eines Branches immer nur an einem Ort**. Wenn du einen Branch in einem Worktree auscheckst, kannst du ihn **nicht** gleichzeitig in deinem lokalen Checkout auschecken und umgekehrt.

In der Praxis gibt es dafür zwei gängige Vorgehensweisen:

1. [Ausschließlich im Worktree arbeiten](#option-1-working-on-the-worktree). Diese Vorgehensweise eignet sich am besten, wenn du Änderungen direkt im Worktree überprüfen kannst, etwa weil du Abhängigkeiten und Tools mithilfe eines [Setup-Skripts für die lokale Umgebung](/de-DE/codex/environments/local-environment) installiert hast.
2. [Den Chat an Lokal übergeben](#option-2-handing-a-chat-off-to-local). Nutze diese Möglichkeit, wenn du den Chat in den Vordergrund holen möchtest, zum Beispiel um Änderungen in deiner gewohnten IDE zu überprüfen oder weil du nur eine Instanz deiner App ausführen kannst.

### Option 1: Im Worktree arbeiten

<div class="feature-grid">

<div>

Wenn du mit deinen Änderungen ausschließlich im Worktree bleiben möchtest, wandle deinen Worktree über die Schaltfläche **Branch hier erstellen** im Chat-Header in einen Branch um.

Anschließend kannst du deine Änderungen committen, deinen Branch in dein Remote-Repository pushen und auf GitHub einen Pull Request öffnen.

Über die Schaltfläche „Öffnen“ in der Kopfzeile kannst du den Worktree in deiner IDE öffnen, das integrierte Terminal nutzen oder alle anderen erforderlichen Aufgaben direkt im Worktree-Verzeichnis erledigen.

</div>

  
    
  

</div>

Beachte: Wenn du in einem Worktree einen Branch erstellst, kannst du ihn in keinem anderen Worktree auschecken, auch nicht in deinem lokalen Checkout.

<a id="option-2-handing-a-thread-off-to-local"></a>
<a id="option-2-handing-a-chat-off-to-local"></a>
<a id="option-2-handing-a-task-off-to-local"></a>

### Option 2: Einen Chat an Lokal übergeben

<div class="feature-grid">

<div>

Wenn du einen Chat in den Vordergrund holen möchtest, wähle im Chat-Header **Übergeben** aus und verschiebe ihn nach **Lokal**.

Diese Vorgehensweise eignet sich, wenn du die Änderungen in deinem gewohnten IDE-Fenster durchsehen, deinen vorhandenen Entwicklungsserver ausführen oder die Arbeit in derselben Umgebung überprüfen möchtest, die du bereits täglich nutzt.

Codex übernimmt die erforderlichen Git-Schritte, um den Chat sicher zwischen dem Worktree und deinem lokalen Checkout zu verschieben.

Jedem Chat bleibt dauerhaft derselbe Worktree zugeordnet. Wenn du den Chat später wieder an einen Worktree übergibst, bringt Codex ihn in dieselbe Hintergrundumgebung zurück, damit du dort weitermachen kannst, wo du aufgehört hast.

</div>

  
    
  

</div>

Du kannst auch in die andere Richtung vorgehen. Wenn du bereits in Lokal arbeitest und den Vordergrund freigeben möchtest, verschiebe den Chat mit **Übergeben** in einen Worktree. Das ist praktisch, wenn Codex im Hintergrund weiterarbeiten soll, während du dich lokal wieder einer anderen Aufgabe widmest.

Da die Übergabe Git-Vorgänge nutzt, werden Dateien, die in `.gitignore` aufgeführt sind, nicht zusammen mit dem Chat verschoben, es sei denn, Codex kopiert sie mithilfe von `.worktreeinclude` in einen lokal verwalteten Worktree.

## Details für Fortgeschrittene

### Von Codex verwaltete und dauerhafte Worktrees

Standardmäßig verwenden Chats einen von Codex verwalteten Worktree. Diese Worktrees sind für eine unkomplizierte, vorübergehende Nutzung gedacht. Ein von Codex verwalteter Worktree ist in der Regel genau einem Chat zugeordnet. Wenn du den Chat später wieder an diesen Worktree übergibst, bringt Codex ihn dorthin zurück.

Wenn du eine dauerhafte Umgebung benötigst, erstelle über das Dreipunktmenü eines Projekts in der Seitenleiste einen dauerhaften Worktree. Dadurch entsteht ein neuer dauerhafter Worktree als eigenständiges Projekt. Dauerhafte Worktrees werden nicht automatisch gelöscht, und du kannst im selben Worktree mehrere Chats starten.

### So verwaltet Codex Worktrees für dich

Codex legt Worktrees in `$CODEX_HOME/worktrees` an. Der Ausgangs-Commit entspricht dem `HEAD`-Commit des Branches, den du beim Start des Chats ausgewählt hast. Wenn du einen Branch mit lokalen Änderungen ausgewählt hast, übernimmt Codex auch die noch nicht committeten Änderungen in den Worktree. Der Worktree ist nicht als Branch ausgecheckt, sondern befindet sich im Zustand [detached HEAD](https://git-scm.com/docs/git-checkout#_detached_head). So kann Codex mehrere Worktrees erstellen, ohne deine Branches unübersichtlich zu machen.

### Ignorierte lokale Dateien in verwaltete Worktrees kopieren

Von Codex verwaltete lokale Worktrees basieren auf einem Git-Checkout, daher sind von Git verfolgte Dateien bereits vorhanden. Wenn dein Repository lokale Setup-Dateien ignoriert, die ein neuer Worktree benötigt, lege im Stammverzeichnis des Repositorys eine Datei namens `.worktreeinclude` an. Trage darin die ignorierten Pfade oder Muster im Stil von `.gitignore` ein, damit Codex die entsprechenden Dateien beim Erstellen eines verwalteten Worktrees kopiert.

Nutze diese Möglichkeit für Dateien, die Git absichtlich ignoriert, etwa `.env`, `.env.local` oder `config/secrets.json`. Codex kopiert nur ignorierte Dateien, die den Einträgen in `.worktreeinclude` entsprechen. Andere lokale Dateien, die Git nicht verfolgt, kopiert Codex nicht. Führe keine von Git verfolgten Dateien auf.

Codex kopiert eine ignorierte Datei `AGENTS.override.md` automatisch in lokal verwaltete Worktrees. Du musst sie daher nicht in `.worktreeinclude` aufführen.

```text
# .worktreeinclude
.env
.env.local
config/secrets.json

Codex überspringt symbolische Links in der Quelle und überschreibt keine Dateien, die im neuen Checkout bereits vorhanden sind. Dieses Verhalten gilt für lokale Worktrees, die von der ChatGPT-Desktop-App verwaltet werden, nicht für Remote-Worktrees oder Git-Worktrees, die du selbst über die Kommandozeile erstellst.

### Einschränkungen für Branches

Angenommen, Codex schließt seine Arbeit in einem Worktree ab und du erstellst dort einen Branch namens `feature/a` über die Schaltfläche **Branch hier erstellen**. Nun möchtest du ihn in deinem lokalen Checkout ausprobieren. Beim Versuch, diesen Branch auszuchecken, würdest du folgende Fehlermeldung erhalten:

fatal: 'feature/a' is already used by worktree at '<WORKTREE_PATH>'

Um das Problem zu beheben, müsstest du im Worktree statt `feature/a` einen anderen Branch auschecken.

Wenn du den Branch lokal auschecken möchtest, verschiebe den Chat per Übergabe nach Lokal, statt zu versuchen, denselben Branch an beiden Orten gleichzeitig auszuchecken.

Git verhindert, dass derselbe Branch gleichzeitig in mehreren Worktrees ausgecheckt wird, weil ein Branch für genau eine veränderliche Referenz (`refs/heads/<name>`) steht. Diese Referenz beschreibt „den aktuell ausgecheckten Zustand“ eines Arbeitsverzeichnisses.

Wenn ein Branch ausgecheckt ist, betrachtet Git dessen HEAD als dem jeweiligen Worktree zugeordnet und erwartet, dass Vorgänge wie Commits, Resets, Rebases und Merges diese Referenz in einer klar definierten Reihenfolge fortschreiben. Könnten mehrere Worktrees denselben Branch gleichzeitig auschecken, entstünden Unklarheiten und Wettlaufsituationen darüber, welcher Worktree die Branch-Referenz aktualisiert. Dies könnte zu verlorenen Commits, inkonsistenten Indizes oder einer unklaren Konfliktauflösung führen.

Durch die Regel, dass ein Branch jeweils nur in einem Worktree ausgecheckt sein darf, stellt Git sicher, dass jeder Branch genau eine verbindliche Arbeitskopie hat. Andere Worktrees können weiterhin sicher über detached HEADs oder separate Branches auf dieselben Commits verweisen.

### Worktrees bereinigen

Worktrees können viel Speicherplatz belegen. Jeder Worktree verfügt über eigene Repository-Dateien, Abhängigkeiten, Build-Caches und weitere Daten. Deshalb versucht die ChatGPT-Desktop-App, die Anzahl der Worktrees auf ein sinnvolles Maß zu begrenzen.

Standardmäßig behält Codex deine 15 neuesten von Codex verwalteten Worktrees. Du kannst dieses Limit in den Einstellungen ändern oder die automatische Löschung deaktivieren, wenn du die Speicherplatznutzung lieber selbst verwalten möchtest.

Codex versucht, weiterhin benötigte Worktrees nicht zu löschen. Von Codex verwaltete Worktrees werden in folgenden Fällen nicht automatisch gelöscht:

- Ein angepinnter Chat ist mit dem Worktree verknüpft
- Der Chat läuft noch
- Es handelt sich um einen dauerhaften Worktree

Von Codex verwaltete Worktrees werden in folgenden Fällen automatisch gelöscht:

- Du archivierst den zugehörigen Chat
- Codex muss ältere Worktrees löschen, um dein konfiguriertes Limit einzuhalten

Vor dem Löschen eines von Codex verwalteten Worktrees speichert Codex einen Snapshot des aktuellen Arbeitsstands. Wenn du einen Chat öffnest, nachdem dessen Worktree gelöscht wurde, wird dir die Option angezeigt, den Worktree wiederherzustellen.

## Häufig gestellte Fragen

  Ja. Standardmäßig erstellt Codex verwaltete Worktrees unter `$CODEX_HOME/worktrees`.
  Um einen anderen Speicherort auszuwählen, öffne **Einstellungen \> Worktrees** 
und ändere **Worktree-Stammverzeichnis**.

<a id="can-i-move-a-chat-between-local-and-worktree"></a>

  Ja. Wähle in der Kopfzeile des Chats **Übergeben** , um ihn zwischen deinem lokalen
  Checkout und einem Worktree zu verschieben. Codex übernimmt die Git-Vorgänge, die für einen sicheren Wechsel
  des Chats zwischen den Umgebungen erforderlich sind. Wenn du den Chat später wieder an einen Worktree übergibst,
  verschiebt Codex ihn zurück in denselben zugeordneten Worktree.

<a id="what-happens-to-chats-if-a-worktree-is-deleted"></a>

  Chats können in deinem Verlauf erhalten bleiben, auch wenn das zugehörige Worktree-Verzeichnis
gelöscht wurde. Bei von Codex verwalteten Worktrees speichert Codex vor dem Löschen
einen Snapshot des Worktrees. Wenn du den zugehörigen Chat erneut öffnest, bietet Codex an,
den Worktree wiederherzustellen. Dauerhafte Worktrees werden nicht automatisch gelöscht,
wenn du die zugehörigen Chats archivierst.
