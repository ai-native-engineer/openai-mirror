<!-- source: https://learn.chatgpt.com/de-DE/docs/environments/cloud-environment -->

Mit Umgebungen steuerst du, was Codex während Cloud-Chats installiert und ausführt. Du kannst beispielsweise Abhängigkeiten hinzufügen, Tools wie Linter und Formatierer installieren und Umgebungsvariablen festlegen.

Konfiguriere Umgebungen in den [Codex-Einstellungen](https://chatgpt.com/codex/settings/environments).

<a id="how-codex-cloud-tasks-run"></a>

## So laufen Codex-Cloud-Chats ab

Wenn du einen Prompt sendest, geschieht Folgendes:

1. Codex erstellt einen Container und checkt in deinem Repository den ausgewählten Branch oder die ausgewählte Commit-SHA aus.
2. Codex führt dein Setup-Skript aus. Wird ein zwischengespeicherter Container reaktiviert, führt Codex außerdem ein optionales Wartungsskript aus.
3. Codex wendet deine Einstellungen für den Internetzugang an. Setup-Skripte werden mit Internetzugang ausgeführt. Der Internetzugang für Agenten ist standardmäßig deaktiviert. Bei Bedarf kannst du jedoch eingeschränkten oder uneingeschränkten Zugriff aktivieren. Weitere Informationen findest du unter [Internetzugang für Agenten](/de-DE/codex/cloud/internet-access).
4. Der Agent führt Terminalbefehle in einer Schleife aus. Er bearbeitet Code, führt Prüfungen durch und versucht, seine Arbeit zu validieren. Wenn dein Repository `AGENTS.md` enthält, nutzt der Agent die Datei, um projektspezifische Lint- und Testbefehle zu finden.
5. Wenn der Agent fertig ist, zeigt er seine Antwort und ein Diff der Dateien an, die er geändert hat. Du kannst einen Pull Request öffnen oder Folgefragen stellen.

## Standard-Image „universal“

Der Codex-Agent wird in einem Standard-Container-Image namens `universal` ausgeführt, in dem gängige Sprachen, Pakete und Tools vorinstalliert sind.

Wähle in den Umgebungseinstellungen **Paketversionen festlegen** aus, um die Versionen von Python, Node.js und anderen Laufzeitumgebungen zu fixieren.

  Einzelheiten zu den installierten Komponenten findest du unter
[openai/codex-universal](https://github.com/openai/codex-universal). Dort stehen ein
  Dockerfile als Referenz sowie ein Image bereit, das du lokal herunterladen und testen kannst.

In `codex-universal` sind gängige Sprachen bereits vorinstalliert, damit sie schnell und bequem verfügbar sind. Über [Setup-Skripte](#manual-setup) kannst du jedoch weitere Pakete im Container installieren.

## Umgebungsvariablen und Secrets

**Umgebungsvariablen** werden für die gesamte Dauer des Chats festgelegt (einschließlich der Setup-Skripte und der Agentenphase).

Für **Secrets** gilt weitgehend dasselbe wie für Umgebungsvariablen, allerdings mit folgenden Ausnahmen:

- Sie werden mit einer zusätzlichen Verschlüsselungsschicht gespeichert und erst zur Ausführung der Aufgabe entschlüsselt.
- Sie sind nur für Setup-Skripte verfügbar. Aus Sicherheitsgründen werden Secrets entfernt, bevor die Agentenphase beginnt.

## Automatisches Setup

Bei Projekten mit gängigen Paketmanagern (`npm`, `yarn`, `pnpm`, `pip`, `pipenv` und `poetry`) kann Codex Abhängigkeiten und Tools automatisch installieren.

## Manuelles Setup

Wenn dein Entwicklungs-Setup komplexer ist, kannst du auch ein eigenes Setup-Skript bereitstellen. Beispiel:

```bash
# Install type checker
pip install pyright

# Install dependencies
poetry install --with test
pnpm install

  Setup-Skripte werden in einer vom Agenten getrennten Bash-Sitzung ausgeführt. Befehle wie
`export` wirken daher nicht bis in die Agentenphase fort. Wenn Umgebungsvariablen
  dauerhaft verfügbar bleiben sollen, füge sie der Datei `~/.bashrc` hinzu oder konfiguriere sie in den Umgebungseinstellungen.

## Container-Caching

Codex speichert den Containerzustand bis zu 12 Stunden im Cache, um neue Chats und Folgeanfragen zu beschleunigen.

Wenn eine Umgebung im Cache gespeichert wird:

- Codex klont das Repository und checkt den Standard-Branch aus.
- Codex führt das Setup-Skript aus und speichert den daraus resultierenden Containerzustand im Cache.

Wenn ein zwischengespeicherter Container reaktiviert wird:

- Codex checkt den für den Chat angegebenen Branch aus.
- Codex führt das optionale Wartungsskript aus. Das ist nützlich, wenn das Setup-Skript für einen älteren Commit ausgeführt wurde und die Abhängigkeiten aktualisiert werden müssen.

Codex macht den Cache automatisch ungültig, wenn du das Setup-Skript, das Wartungsskript, Umgebungsvariablen oder Secrets änderst. Wenn Änderungen an deinem Repository den zwischengespeicherten Zustand inkompatibel machen, wähle auf der Seite der Umgebung **Cache zurücksetzen** aus.

  Bei Business- und Unternehmenskonten werden Caches von allen Personen gemeinsam genutzt, die
Zugriff auf die Umgebung haben. Wenn der Cache ungültig gemacht wird, betrifft das alle, die
die Umgebung in deinem Workspace nutzen.

## Internetzugang und Netzwerkproxy

Während der Setup-Skriptphase steht Internetzugang zur Verfügung, um Abhängigkeiten zu installieren. Während der Agentenphase ist der Internetzugang standardmäßig deaktiviert. Du kannst jedoch eingeschränkten oder uneingeschränkten Zugriff konfigurieren. Weitere Informationen findest du unter [Internetzugang für Agenten](/de-DE/codex/cloud/internet-access).

Umgebungen werden aus Sicherheitsgründen und zum Schutz vor Missbrauch hinter einem HTTP/HTTPS-Netzwerkproxy betrieben. Der gesamte ausgehende Internetverkehr wird über diesen Proxy geleitet.
