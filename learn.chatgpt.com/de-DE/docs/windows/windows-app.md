<!-- source: https://learn.chatgpt.com/de-DE/docs/windows/windows-app -->

# ChatGPT-Desktop-App für Windows

Die [ChatGPT-Desktop-App für Windows](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) bietet dir eine zentrale Oberfläche, um
projektübergreifend zu arbeiten, parallele Chats auszuführen und Ergebnisse zu überprüfen.
Die Windows-App unterstützt zentrale Arbeitsabläufe wie Worktrees, geplante Aufgaben und Git-Funktionen
sowie den integrierten Browser, Dateivorschauen, Skills und Plug-ins.
Sie wird nativ unter Windows mit PowerShell und der
[Windows-Sandbox](/de-DE/codex/windows/windows-sandbox#windows-sandbox) ausgeführt. Alternativ kannst du sie so konfigurieren, dass sie
im [Windows Subsystem for Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl) ausgeführt wird.

  
    
  

## ChatGPT-Desktop-App herunterladen

Lade die [ChatGPT-Desktop-App](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) für Windows herunter.

Folge anschließend dem [Schnellstart](/de-DE/codex/quickstart?setup=app), um loszulegen.

Informationen zu Installations- und Updateoptionen für Unternehmen findest du unter
[Windows-App bereitstellen](/de-DE/codex/enterprise/windows-deployment).

Wenn du die Installation über die Kommandozeile bevorzugst, führe Folgendes aus:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

## Native Sandbox

Die ChatGPT-Desktop-App unter Windows unterstützt eine native [Windows-Sandbox](/de-DE/codex/windows/windows-sandbox#windows-sandbox), wenn der Agent in PowerShell ausgeführt wird. Wenn du den Agenten in [Windows Subsystem for Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl) ausführst, kommt Linux-Sandboxing zum Einsatz. Um den Sandbox-Schutz in beiden Modi anzuwenden, wähle unter dem Editor **Genehmigung anfordern** , bevor du Nachrichten an Codex sendest.

  Wenn Codex im Modus „Vollzugriff“ ausgeführt wird, ist Codex nicht auf dein Projektverzeichnis
  beschränkt und kann unbeabsichtigt destruktive Aktionen ausführen, die zu
  Datenverlust führen können. Behalte die Sandbox-Grenzen bei und nutze
[Regeln](/de-DE/codex/agent-configuration/rules) für gezielte Ausnahmen. Alternativ kannst du deine
[Genehmigungsrichtlinie auf
  never festlegen](/de-DE/codex/agent-approvals-security#run-without-approval-prompts), damit
  Codex versucht, Probleme zu lösen, ohne erhöhte Berechtigungen anzufordern.
  Maßgeblich ist dabei dein [Genehmigungs- und Sicherheits-Setup](/de-DE/codex/agent-approvals-security).

## An dein Entwicklungs-Setup anpassen

<section class="feature-grid">

<div>

### Bevorzugter Editor

Wähle für **Öffnen** eine Standard-App aus, etwa Visual Studio, VS Code oder einen anderen
Editor. Du kannst diese Auswahl für jedes Projekt überschreiben. Wenn du für ein Projekt bereits eine
andere App aus dem Menü **Öffnen** ausgewählt hast, hat diese projektspezifische
Auswahl Vorrang.

</div>

  
    
  

</section>

<section class="feature-grid inverse">

<div>

### Integriertes Terminal

Du kannst auch das standardmäßig verwendete integrierte Terminal auswählen. Je nachdem, was du
installiert hast, stehen folgende Optionen zur Verfügung:

- PowerShell
- Eingabeaufforderung
- Git Bash
- WSL

Diese Änderung gilt nur für neue Terminalsitzungen. Wenn du bereits ein
integriertes Terminal geöffnet hast, starte die App neu oder beginne einen neuen Chat,
damit das neue Standardterminal angezeigt wird.

</div>

  
    
  

</section>

## Windows Subsystem for Linux (WSL)

Standardmäßig verwendet die ChatGPT-Desktop-App den Windows-nativen Codex-Agenten. Das bedeutet, der Agent
führt Befehle in PowerShell aus. Die App kann auch mit Projekten arbeiten, die sich im
Windows Subsystem for Linux 2 (WSL2) befinden, indem sie bei Bedarf die `wsl`-CLI verwendet.

Wenn du ein Projekt aus dem WSL-Dateisystem hinzufügen möchtest, klicke auf **Neues Projekt hinzufügen**
oder drücke <kbd>Strg</kbd>+<kbd>O</kbd>. Gib dann `\\wsl$\` in das Fenster des
Datei-Explorers ein. Wähle dort deine Linux-Distribution und den Ordner aus, den du
öffnen möchtest.

Wenn du den Windows-nativen Agenten weiterverwenden möchtest, solltest du Projekte im
Windows-Dateisystem speichern und aus WSL über
`/mnt/<drive>/...` darauf zugreifen. Dieses Setup ist zuverlässiger, als Projekte
direkt aus dem WSL-Dateisystem zu öffnen.

Wenn der Agent selbst in WSL2 ausgeführt werden soll, öffne **[Einstellungen](codex://settings)**,
stelle ihn von Windows-nativ auf WSL um und **starte die App neu**. Die
Änderung wird erst nach dem Neustart wirksam. Deine Projekte sollten
danach weiterhin vorhanden sein.

WSL1 wurde bis einschließlich Codex `0.114` unterstützt. Ab Codex `0.115` basiert die Linux-Sandbox
auf `bubblewrap`. Daher wird WSL1 nicht mehr unterstützt.

  
    
  

Du konfigurierst das integrierte Terminal unabhängig vom Agenten. Unter
[An dein Entwicklungs-Setup anpassen](#customize-for-your-dev-setup) findest du die
Terminaloptionen. Du kannst den Agenten in WSL belassen und trotzdem PowerShell im
Terminal verwenden oder je nach Arbeitsablauf für beides WSL nutzen.

## Nützliche Entwicklungstools

Codex funktioniert am besten, wenn einige gängige Entwicklungstools bereits installiert sind:

- **Git**: Dient als Grundlage für den Review-Bereich in der ChatGPT-Desktop-App und ermöglicht es dir, Änderungen zu prüfen oder
  rückgängig zu machen.
- **Node.js**: Ein gängiges Tool, mit dem der Agent Aufgaben
  effizienter erledigt.
- **Python**: Ein gängiges Tool, mit dem der Agent Aufgaben
  effizienter erledigt.
- **.NET SDK**: Nützlich, wenn du native Windows-Apps entwickeln möchtest.
- **GitHub CLI**: Stellt GitHub-spezifische Funktionen in der ChatGPT-Desktop-App bereit.

Installiere sie mit dem standardmäßigen Windows-Paketmanager `winget`, indem du Folgendes
in das [integrierte Terminal](/de-DE/codex/integrated-terminal) einfügst oder
Codex bittest, die Tools zu installieren:

```powershell
winget install --id Git.Git
winget install --id OpenJS.NodeJS.LTS
winget install --id Python.Python.3.14
winget install --id Microsoft.DotNet.SDK.10
winget install --id GitHub.cli
```

Führe nach der Installation von GitHub CLI `gh auth login` aus,
um die GitHub-Funktionen in der App zu aktivieren.

Wenn du eine andere Python- oder .NET-Version benötigst, passe die Paket-IDs an die
gewünschte Version an.

## Fehlerbehebung und FAQ

### Befehle mit erhöhten Berechtigungen ausführen

Wenn Codex Befehle mit erhöhten Berechtigungen ausführen soll, starte
die ChatGPT-Desktop-App selbst mit Administratorrechten. Öffne nach der Installation das Startmenü,
suche die App und wähle **Als Administrator ausführen**. Der Codex-Agent übernimmt
diese Berechtigungsstufe.

### PowerShell-Ausführungsrichtlinie blockiert Befehle

Wenn du Tools wie Node.js oder `npm` noch nie zuvor in PowerShell verwendet hast, können
beim Codex-Agenten oder im integrierten Terminal Fehler aufgrund der Ausführungsrichtlinie auftreten.

Das kann auch passieren, wenn Codex PowerShell-Skripts für dich erstellt. In diesem Fall
benötigst du möglicherweise eine weniger restriktive Ausführungsrichtlinie, bevor PowerShell
die Skripts ausführen kann.

Eine Fehlermeldung kann etwa so aussehen:

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

Eine häufige Lösung besteht darin, die Ausführungsrichtlinie auf `RemoteSigned` festzulegen:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Informiere dich vor einer Änderung der Richtlinie im
[Microsoft-Leitfaden zu Ausführungsrichtlinien](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)
über Details und weitere Optionen.

### Skripts der lokalen Umgebung unter Windows

Wenn deine [lokale Umgebung](/de-DE/codex/environments/local-environment) plattformübergreifende
Befehle wie `npm`-Skripts nutzt, kannst du für alle Plattformen dasselbe Setup-Skript
oder dieselben Aktionen verwenden.

Wenn du Windows-spezifisches Verhalten benötigst, erstelle Windows-spezifische Setup-Skripts oder
Windows-spezifische Aktionen.

Aktionen werden in der Umgebung ausgeführt, die dein integriertes Terminal verwendet. Weitere Informationen findest du unter
[An dein Entwicklungs-Setup anpassen](#customize-for-your-dev-setup).

Lokale Setup-Skripts werden in der Agentenumgebung ausgeführt: in WSL, wenn der Agent WSL verwendet,
andernfalls in PowerShell.

### Konfiguration, Authentifizierung und Sitzungen mit WSL teilen

Die Windows-App verwendet dasselbe Codex-Home-Verzeichnis wie die native Codex-Version unter Windows:
`%USERPROFILE%\.codex`.

Wenn du die Codex CLI auch in WSL ausführst, verwendet die CLI standardmäßig das
Linux-Home-Verzeichnis. Daher teilt sie die Konfiguration, zwischengespeicherte
Authentifizierungsdaten und den Sitzungsverlauf nicht automatisch mit der Windows-App.

Nutze zum Teilen eine der folgenden Methoden:

- Synchronisiere `~/.codex` unter WSL mit `%USERPROFILE%\.codex` in deinem Dateisystem.
- Lege `CODEX_HOME` fest, damit WSL das Codex-Home-Verzeichnis unter Windows verwendet:

```bash

```

Damit diese Einstellung in jeder Shell gilt, füge sie deinem WSL-Shell-Profil hinzu,
zum Beispiel `~/.bashrc` oder `~/.zshrc`.

### Git-Funktionen sind nicht verfügbar

Wenn Git nicht nativ unter Windows installiert ist, kann die App einige
Funktionen nicht verwenden. Installiere Git mit `winget install Git.Git` über PowerShell oder `cmd.exe`.

### Git wird bei Projekten nicht erkannt, die über `\\wsl$` geöffnet wurden

Wenn du den nativen Windows-Agenten mit einem Projekt verwenden möchtest, auf das du auch
über WSL zugreifen kannst, ist die derzeit zuverlässigste Übergangslösung, das Projekt auf dem
nativen Windows-Laufwerk zu speichern und in WSL über `/mnt/<drive>/...` darauf zuzugreifen.

### `Cmder` wird im Dialog „Öffnen“ nicht aufgeführt

Wenn `Cmder` installiert ist, aber nicht im Dialog „Öffnen“ von Codex erscheint, füge es dem
Windows-Startmenü hinzu: Klicke mit der rechten Maustaste auf `Cmder` und wähle **An „Start“ anheften**. Starte
anschließend Codex oder den Computer neu.
