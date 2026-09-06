<!-- source: https://learn.chatgpt.com/de-DE/docs/linux/linux-app -->

Die ChatGPT-Desktop-App für Linux ist als Vorschauversion verfügbar. Installiere das Paket für deine Linux-Distribution und Prozessorarchitektur und melde dich anschließend mit deinem ChatGPT-Konto an, um mit Projekten, lokalen Dateien und Codex zu arbeiten.

## Unterstützte Distributionen und Architekturen

Die Vorschauversion unterstützt die Desktop-Versionen folgender Linux-Distributionen:

- Ubuntu 24.04 LTS und 26.04 LTS
- Debian 13
- Fedora 43 und 44

Für jede unterstützte Distribution sind Pakete für x64- und ARM64-Prozessoren verfügbar. Führe folgenden Befehl aus, um deine Prozessorarchitektur zu prüfen:

```bash
uname -m

Die Ausgabe `x86_64` kennzeichnet einen x64-Prozessor. Die Ausgabe `aarch64` oder
`arm64` kennzeichnet einen ARM64-Prozessor.

## Das passende Paket herunterladen

Wähle `.deb` für Ubuntu oder Debian und `.rpm` für Fedora:

| Distribution     | Architektur | Download                                                                                                          |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Ubuntu oder Debian | x64          | [`.deb` für x64 herunterladen](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_amd64.deb)     |
| Ubuntu oder Debian | ARM64        | [`.deb` für ARM64 herunterladen](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_arm64.deb)   |
| Fedora           | x64          | [`.rpm` für x64 herunterladen](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.x86_64.rpm)    |
| Fedora           | ARM64        | [`.rpm` für ARM64 herunterladen](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.aarch64.rpm) |

## Unter Ubuntu oder Debian installieren

Lade das `.deb`-Paket für deine Prozessorarchitektur herunter. Öffne anschließend ein
Terminal, wechsle in das Verzeichnis mit dem Paket und installiere es mit
`apt`:

```bash
cd ~/Downloads
sudo apt install ./chatgpt_amd64.deb

Ersetze für ARM64 `chatgpt_amd64.deb` durch `chatgpt_arm64.deb`.

Öffne **ChatGPT** über das Anwendungsmenü oder führe `chatgpt` in einem Terminal aus.
Melde dich mit deinem ChatGPT-Konto an und folge dem
[Schnellstart für die Desktop-App](/de-DE/codex/quickstart?setup=app).

## Unter Fedora installieren

Lade das `.rpm`-Paket für deine Prozessorarchitektur herunter. Öffne anschließend ein
Terminal, wechsle in das Verzeichnis mit dem Paket und installiere es mit
`dnf`:

```bash
cd ~/Downloads
sudo dnf install ./chatgpt.x86_64.rpm

Ersetze für ARM64 `chatgpt.x86_64.rpm` durch `chatgpt.aarch64.rpm`.

Öffne **ChatGPT** über das Anwendungsmenü oder führe `chatgpt` in einem Terminal aus.
Melde dich mit deinem ChatGPT-Konto an und folge dem
[Schnellstart für die Desktop-App](/de-DE/codex/quickstart?setup=app).

## Die App aktualisieren

Bei der Installation konfiguriert das Paket das signierte Paket-Repository von OpenAI. Verwende die Paketverwaltung deiner Distribution, um spätere Updates zu installieren.

Führe unter Ubuntu oder Debian folgenden Befehl aus:

```bash
sudo apt update
sudo apt install --only-upgrade chatgpt

Führe unter Fedora folgenden Befehl aus:

```bash
sudo dnf upgrade --refresh chatgpt

## Kompatibilität und Einschränkungen

Die Vorschauversion unterstützt die unter
[Unterstützte Distributionen und Architekturen](#supported-distributions-and-architectures) aufgeführten Desktop-Distributionen.
Andere Linux-Distributionen funktionieren möglicherweise, werden aber nicht offiziell unterstützt.

Für einige Funktionen gelten gesonderte Anforderungen an die Plattform. So ist die
[Computernutzung](/de-DE/codex/computer-use) unter macOS und Windows verfügbar, in der Linux-Vorschauversion jedoch
noch nicht. Eine zukünftige Version wird Linux unterstützen.

## Wayland-Unterstützung

Die native Wayland-Unterstützung ist experimentell und wird laufend verbessert. In einer Wayland-Sitzung verwendet die App XWayland, sofern es verfügbar ist. Um Wayland gezielt nativ zu nutzen, beende die App vollständig und starte sie über ein Terminal:

```bash
chatgpt --ozone-platform=wayland

Solange die native Wayland-Unterstützung weiterentwickelt wird, funktionieren einige Funktionen wie schwebende Fenster, Fensterpositionierung, Fokussteuerung und Tastenkombinationen möglicherweise noch nicht vollständig.

## Nächste Schritte

- Folge dem [Schnellstart für die Desktop-App](/de-DE/codex/quickstart?setup=app).
- Richte die [Chrome-Erweiterung](/de-DE/codex/chrome-extension) für die Browserintegration ein.
- Überprüfe die [Berechtigungen](/de-DE/codex/permissions) für lokale Projekte und Befehle.
