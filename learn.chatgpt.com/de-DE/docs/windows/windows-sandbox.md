<!-- source: https://learn.chatgpt.com/de-DE/docs/windows/windows-sandbox -->

Verwende Codex unter Windows mit der nativen [ChatGPT-Desktop-App](/de-DE/codex/windows/windows-app), der
[CLI](/de-DE/codex/cli) oder der [IDE-Erweiterung](/de-DE/codex/ide).

Die ChatGPT-Desktop-App unter Windows unterstützt zentrale Arbeitsabläufe wie parallele Chats,
Worktrees, geplante Aufgaben, Git-Funktionen, den integrierten Browser, Dateivorschauen,
Plug-ins und Skills.

Die App kann nativ in PowerShell mit einer Windows-Sandbox ausgeführt werden, ohne
dass WSL oder eine virtuelle Maschine erforderlich ist. So lässt sich Codex in Windows-nativen
Arbeitsabläufen nutzen, während der Zugriff auf Dateisystem und Netzwerk begrenzt bleibt.

  
    
  

<div class="mb-8">
  
</div>

Die native Windows-Sandbox bietet zwei Modi:

- nativ unter Windows mit der stärker abgesicherten Sandbox `elevated`,
- nativ unter Windows mit der als Ausweichlösung vorgesehenen Sandbox `unelevated`.

<span id="windows-sandbox"></span>

## Windows-Sandbox konfigurieren

Wenn du Codex nativ unter Windows ausführst, verwendet der Agentenmodus eine Windows-Sandbox, um
Schreibvorgänge im Dateisystem außerhalb des Arbeitsordners zu blockieren und den Netzwerkzugriff
ohne deine ausdrückliche Genehmigung zu verhindern.

Die native Windows-Sandbox unterstützt zwei Modi, die du in
`config.toml` konfigurieren kannst:

```toml
[windows]
sandbox = "elevated" # or "unelevated"

`elevated` ist die bevorzugte native Windows-Sandbox. Sie verwendet eigens eingerichtete
Sandbox-Benutzerkonten mit eingeschränkten Rechten, Berechtigungsgrenzen im Dateisystem,
Firewallregeln und lokale Richtlinienänderungen, die für die Ausführung von Befehlen in der Sandbox erforderlich sind.

`unelevated` ist die native Windows-Sandbox, die als Ausweichlösung dient. Sie führt Befehle mit einem
eingeschränkten Windows-Token aus, das von deinem aktuellen Benutzerkonto abgeleitet ist, wendet ACL-basierte
Dateisystemgrenzen an und nutzt Offline-Beschränkungen auf Umgebungsebene anstelle
der speziellen Firewallregel für Offline-Benutzerkonten. Sie ist schwächer abgesichert als `elevated`, aber
weiterhin nützlich, wenn ein von der Administration genehmigtes Setup durch lokale oder
Unternehmensrichtlinien blockiert wird.

Wenn beide Modi verfügbar sind, verwende `elevated`. Falls die standardmäßig verwendete native Sandbox
in deiner Umgebung nicht funktioniert, nutze `unelevated` als Ausweichlösung, während du
Fehler beim Setup behebst.

Die IT-Administration in Unternehmen kann festlegen, welche nativen Sandbox-Implementierungen
Codex verwenden darf. Dafür nutzt sie [`requirements.toml`](/de-DE/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml):

```toml
[windows]
allowed_sandbox_implementations = ["elevated"]

Dieses Beispiel setzt die Sandbox `elevated` voraus und verhindert, dass
auf `unelevated` ausgewichen wird. Um beide Implementierungen zuzulassen, gib beide Werte an.
Wenn kein Modus ausgewählt ist, bevorzugt Codex `elevated`. In der
[Referenz zu `requirements.toml`](/de-DE/codex/config-file/config-reference#requirementstoml) findest du die
unterstützten Werte.

Standardmäßig verwenden beide Sandbox-Modi außerdem einen privaten Desktop, um die Benutzeroberfläche stärker
zu isolieren. Setze `windows.sandbox_private_desktop = false` nur dann, wenn du aus
Kompatibilitätsgründen das ältere Verhalten von `Winsta0\\Default` benötigst.

### Sandbox-Berechtigungen

  Wird Codex im Modus „Vollzugriff“ ausgeführt, ist es nicht auf dein Projektverzeichnis
  beschränkt und kann versehentlich destruktive Aktionen ausführen, die zu
  Datenverlust führen können. Für eine sicherere Automatisierung behalte die Sandbox-Grenzen bei und verwende
[Regeln](/de-DE/codex/agent-configuration/rules) für konkrete Ausnahmen. Alternativ kannst du deine
[Genehmigungsrichtlinie auf
  never](/de-DE/codex/agent-approvals-security#run-without-approval-prompts) setzen. Dann versucht
  Codex, Probleme ohne Anforderung erhöhter Berechtigungen zu lösen,
  entsprechend deiner [Genehmigungs- und Sicherheitskonfiguration](/de-DE/codex/agent-approvals-security).

### Windows-Versionsmatrix

| Windows-Version                  | Supportstufe   | Hinweise                                                                                                                                                                                 |
| -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows 11                       | Empfohlen     | Beste Ausgangsbasis für Codex unter Windows. Verwende diese Version, wenn du eine unternehmensweite Bereitstellung standardisierst.                                                                                       |
| Aktuelle, vollständig aktualisierte Version von Windows 10 | Unterstützung nach Möglichkeit     | Kann funktionieren, ist jedoch weniger zuverlässig als Windows 11. Unter Windows 10 benötigt Codex moderne Konsolenunterstützung einschließlich ConPTY. In der Praxis ist Windows 10 ab Version 1809 erforderlich. |
| Ältere Builds von Windows 10          | Nicht empfohlen | Bei diesen Builds fehlen häufiger erforderliche Konsolenkomponenten wie ConPTY, und Setups in Unternehmen schlagen eher fehl.                                                                          |

Weitere Voraussetzungen für die Umgebung:

- `winget` sollte verfügbar sein. Falls nicht, aktualisiere Windows oder installiere
  den Windows Package Manager, bevor du Codex einrichtest.
- Die empfohlene native Sandbox setzt ein von der Administration genehmigtes Setup voraus.
- Einige von Unternehmen verwaltete Geräte blockieren die erforderlichen Setup-Schritte, obwohl die
Betriebssystemversion an sich geeignet ist.

### Lesezugriff für die Sandbox gewähren

Wenn ein Befehl fehlschlägt, weil die Windows-Sandbox ein Verzeichnis nicht lesen kann, verwende:

```text
/sandbox-add-read-dir C:\absolute\directory\path

Es muss sich um den absoluten Pfad eines vorhandenen Verzeichnisses handeln. Nach erfolgreicher Ausführung des Befehls können nachfolgende Befehle in der Sandbox dieses Verzeichnis während der aktuellen Sitzung lesen.

<span id="windows-subsystem-for-linux"></span>

Verwende standardmäßig die native Windows-Sandbox. Entscheide dich für [WSL](/de-DE/codex/windows/wsl),
wenn du Linux-native Tools benötigst, dein Arbeitsablauf bereits in WSL2 stattfindet oder
keiner der nativen Windows-Sandbox-Modi deine Anforderungen erfüllt.

## Fehlerbehebung und FAQ

Wenn du bei einem verwalteten Windows-Computer Fehler behebst, prüfe zunächst den nativen
Sandbox-Modus, die Windows-Version und alle von Codex angezeigten Richtlinienfehler. Die meisten Probleme beim nativen
Einsatz unter Windows betreffen das Sandbox-Setup, Anmelderechte oder
Dateisystemberechtigungen und nicht den Editor selbst.

Wenn Codex das Setup der Sandbox `elevated` nicht abschließen kann, sind die häufigsten
Ursachen:

- die Windows-UAC- oder Administratorabfrage wurde abgelehnt,
- das Gerät lässt das Erstellen lokaler Benutzerkonten oder Gruppen nicht zu,
- das Gerät lässt Änderungen an Firewallregeln nicht zu,
- das Gerät blockiert die Anmelderechte, die die Sandbox-Benutzerkonten benötigen,
- oder eine andere Unternehmensrichtlinie blockiert einen Teil des Setup-Ablaufs.

Das kannst du versuchen:

1. Versuche erneut, die Sandbox `elevated` einzurichten, und bestätige die Administratorabfrage,
   wenn deine Umgebung dies zulässt.
2. Wenn dein Firmenlaptop dies blockiert, frage dein IT-Team, ob das Gerät
ein von der Administration genehmigtes Setup für das Erstellen lokaler Benutzerkonten und Gruppen, die
Firewallkonfiguration und die erforderlichen Anmelderechte der Sandbox-Benutzerkonten zulässt.
3. Wenn das Standard-Setup weiterhin fehlschlägt, verwende die Sandbox `unelevated`, damit du
   weiterarbeiten kannst, während das Problem untersucht wird.

Das bedeutet, dass Codex das Setup der stärker abgesicherten Sandbox `elevated` auf deinem
Computer nicht abschließen konnte.

- Codex kann weiterhin in einem Sandbox-Modus ausgeführt werden.
- Die Sandbox wendet weiterhin ACL-basierte Dateisystemgrenzen an, nutzt jedoch nicht die
  separate Sicherheitsgrenze durch Sandbox-Benutzerkonten des Modus `elevated` und bietet eine schwächere
  Netzwerkisolierung.
- Dies ist eine nützliche Ausweichlösung, aber nicht die langfristig bevorzugte Konfiguration für
Unternehmen.

Wenn du einen verwalteten Firmenlaptop verwendest, besteht die beste langfristige Lösung meist darin,
die Sandbox `elevated` mit Unterstützung deines IT-Teams zum Laufen zu bringen.

Wenn Befehle in der Sandbox mit dem Fehler `1385` fehlschlagen, lässt Windows die Anmeldeart nicht zu,
die der Sandbox-Benutzer zum Starten des Befehls benötigt.

In der Praxis bedeutet das meist, dass Codex die Sandbox-Benutzer erfolgreich angelegt hat,
die Windows-Richtlinie diese Benutzer aber weiterhin daran hindert, Befehle in der Sandbox
auszuführen.

Das kannst du tun:

1. Frage dein IT-Team, ob die Geräterichtlinie den von Codex angelegten Sandbox-Benutzern
die erforderlichen Anmelderechte einräumt.
2. Prüfe Unterschiede bei Gruppenrichtlinien oder OUs, wenn das Problem nur einige
Computer oder Teams betrifft.
3. Wenn du sofort weiterarbeiten musst, verwende die `unelevated`-Sandbox, während
   das Richtlinienproblem untersucht wird.
4. Sende `CODEX_HOME/.sandbox/sandbox.log` zusammen mit deiner Windows-Version und einer
   kurzen Beschreibung des Fehlers.

Codex warnt möglicherweise, dass `Everyone` Schreibzugriff auf einige Ordner hat.

Wenn diese Warnung angezeigt wird, sind die Windows-Berechtigungen für diese Ordner so weit gefasst,
dass die Sandbox sie nicht vollständig schützen kann.

Das kannst du tun:

1. Überprüfe die Ordner, die Codex in der Warnung aufführt.
2. Entziehe `Everyone` den Schreibzugriff auf diese Ordner, sofern das in
   deiner Umgebung sinnvoll ist.
3. Starte Codex neu oder führe das Sandbox-Setup erneut aus, nachdem du diese Berechtigungen
korrigiert hast.

Wenn du nicht sicher bist, wie du diese Berechtigungen ändern kannst, bitte dein IT-Team um Hilfe.

Einige Codex-Chats werden absichtlich ohne ausgehenden Netzwerkzugriff ausgeführt,
je nachdem, welcher Berechtigungsmodus verwendet wird.

Wenn eine Aufgabe wegen fehlenden Netzwerkzugriffs fehlschlägt:

1. Prüfe, ob die Aufgabe ohne Netzwerkzugriff ausgeführt werden sollte.
2. Wenn du Netzwerkzugriff erwartet hast, starte Codex neu und versuche es noch einmal.
3. Wenn das Problem weiterhin auftritt, sichere das Sandbox-Protokoll, damit das Team prüfen kann,
ob die Sandbox auf dem Computer nur teilweise eingerichtet oder fehlerhaft ist.

Das kann nach Folgendem passieren:

- dem Verschieben eines Repositorys oder eines Workspaces,
- dem Ändern von Berechtigungen auf dem Computer,
- dem Ändern von Windows-Richtlinien,
- oder anderen Änderungen an der Systemkonfiguration.

Das kannst du versuchen:

1. Starte Codex neu.
2. Führe das Setup der `elevated`-Sandbox erneut aus.
3. Wenn das Problem dadurch nicht behoben wird, verwende die `unelevated`-Sandbox als vorübergehende
   Ausweichlösung.
4. Sichere das Sandbox-Protokoll zur Überprüfung.

Wenn du weiterhin Probleme hast, sende Folgendes:

- `CODEX_HOME/.sandbox/sandbox.log`

Folgende Angaben sind ebenfalls hilfreich:

- eine kurze Beschreibung dessen, was du vorhattest,
- ob die `elevated`-Sandbox fehlgeschlagen ist oder die `unelevated`-Sandbox verwendet wurde,
- jede in der App angezeigte Fehlermeldung,
- ob dir der Fehler `1385` oder ein anderer Windows- oder PowerShell-Fehler angezeigt wurde,
- und ob du Windows 11 oder Windows 10 verwendest.

Sende Folgendes nicht:

- den Inhalt von `CODEX_HOME/.sandbox-secrets/`

Auf deinem System fehlen möglicherweise C++-Entwicklungstools, die für einige native Abhängigkeiten erforderlich sind:

- Visual Studio Build Tools (C++-Workload)
- Microsoft Visual C++ Redistributable (x64)
- Führe mit `winget` den Befehl `winget install --id Microsoft.VisualStudio.2022.BuildTools -e` aus

Starte VS Code nach der Installation vollständig neu.
