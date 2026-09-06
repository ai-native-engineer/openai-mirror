<!-- source: https://learn.chatgpt.com/de-DE/docs/windows/wsl -->

Wenn du WSL2 verwendest, läuft Codex in der Linux-Umgebung und nutzt nicht die
native [Windows-Sandbox](/de-DE/codex/windows/windows-sandbox). Wähle WSL2, wenn du native
Linux-Tools benötigst, deine Repositories und dein Entwicklungsworkflow bereits in WSL2 eingerichtet sind oder
keiner der beiden nativen Windows-Sandbox-Modi in deiner Umgebung funktioniert.

WSL1 wurde bis einschließlich Codex `0.114` unterstützt. Ab Codex `0.115` wurde die Sandbox für Linux
auf `bubblewrap` umgestellt, weshalb WSL1 nicht mehr unterstützt wird.

## VS Code aus WSL heraus starten

Eine Schritt-für-Schritt-Anleitung findest du im [offiziellen WSL-Tutorial für VS Code](https://code.visualstudio.com/docs/remote/wsl-tutorial).

### Voraussetzungen

- Windows mit installiertem WSL. Öffne zum Installieren von WSL PowerShell mit Administratorrechten und führe dann `wsl --install` aus (Ubuntu ist eine gängige Wahl).
- VS Code mit installierter [WSL-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl).

### VS Code über ein WSL-Terminal öffnen

```bash
# From your WSL shell
cd ~/code/your-project
code .

So öffnest du ein WSL-Remote-Fenster. Bei Bedarf wird der VS Code Server installiert und integrierte Terminals werden unter Linux ausgeführt.

### Verbindung mit WSL prüfen

- Achte auf die grüne Statusleiste mit der Anzeige `WSL: <distro>`.
- Integrierte Terminals sollten Linux-Pfade (z. B. `/home/...`) statt `C:\` anzeigen.
- Du kannst dies wie folgt überprüfen:

  ```bash
  echo $WSL_DISTRO_NAME

  Damit wird der Name deiner Distribution ausgegeben.

  Wenn du „WSL: ...“ nicht in der Statusleiste siehst, drücke `Ctrl+Shift+P`, wähle
`WSL: Reopen Folder in WSL` aus und lege dein Repository für optimale Leistung unter `/home/...` ab (nicht
unter `C:\`).

  Wenn die Windows-App oder die Projektauswahl dein WSL-Repository nicht anzeigt, gib
<code>\\wsl$</code> in der Dateiauswahl oder im Explorer ein und navigiere dann zum
  Home-Verzeichnis deiner Distribution.

## Codex CLI mit WSL verwenden

Führe diese Befehle in PowerShell oder Windows Terminal mit Administratorrechten aus:

```powershell
# Install default Linux distribution (like Ubuntu)
wsl --install

# Start a shell inside Windows Subsystem for Linux
wsl

Führe anschließend diese Befehle in deiner WSL-Shell aus:

```bash
# Install and run Codex in WSL
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex

## Code in WSL bearbeiten

- Das Arbeiten mit unter Windows eingebundenen Pfaden wie <code>/mnt/c/...</code> kann langsamer sein als mit nativen Windows-Pfaden. Lege deine Repositories für schnellere E/A-Vorgänge und weniger Probleme mit Symlinks und Berechtigungen in deinem Linux-Home-Verzeichnis ab, zum Beispiel unter <code>~/code/my-app</code>:
  ```bash
  mkdir -p ~/code && cd ~/code
  git clone https://github.com/your/repo.git
  cd repo
- Wenn du von Windows aus auf die Dateien zugreifen musst, findest du sie im Explorer unter <code>\\wsl$\\Ubuntu\\home&lt;user\></code>.

## Fehlerbehebung und FAQ

- Stelle sicher, dass du nicht unter <code>/mnt/c</code> arbeitest. Verschiebe das Repository nach WSL (zum Beispiel nach <code>~/code/...</code>).
- Weise WSL bei Bedarf mehr Arbeitsspeicher und CPU-Ressourcen zu; aktualisiere WSL auf die neueste Version:
  ```powershell
  wsl --update
  wsl --shutdown

Prüfe, ob die Binärdatei vorhanden und in WSL über `PATH` auffindbar ist:

```bash
which codex || echo "codex not found"

Wenn die Binärdatei nicht gefunden wird, befolge die [Setup-Anleitung für die Codex CLI](#use-codex-cli-with-wsl).
