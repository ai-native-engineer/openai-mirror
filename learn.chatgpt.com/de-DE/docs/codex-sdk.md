<!-- source: https://learn.chatgpt.com/de-DE/docs/codex-sdk -->

Wenn du Codex über Codex CLI, die IDE-Erweiterung oder Codex Cloud verwendest, kannst du Codex auch programmgesteuert steuern.

Verwende das SDK für Folgendes:

- Codex als Teil deiner CI/CD-Pipeline steuern
- Einen eigenen Agenten erstellen, der mit Codex zusammenarbeiten kann, um komplexe Entwicklungsaufgaben auszuführen
- Codex in deine eigenen internen Tools und Arbeitsabläufe integrieren
- Codex in deine eigene Anwendung integrieren

Verwende das Codex SDK, um Programmieraufgaben zu automatisieren, einschließlich CI-Jobs. Verwende den [Codex App Server](/de-DE/codex/app-server), um eigene Clients zu entwickeln, die Authentifizierung, Gesprächsverläufe und Genehmigungen verwalten sowie Agentenereignisse als Stream verarbeiten.

`codex mcp-server` ist veraltet. Die [Anleitung zum MCP-Server](/de-DE/codex/mcp-server) bleibt für bestehende Integrationen verfügbar.

Wenn du Betazugriff hast und Scans von Repositorys oder Änderungen mit strukturierten
Sicherheitsbefunden und Angaben zur Abdeckung benötigst, verwende das [TypeScript-SDK für
Codex Security](/de-DE/codex/security/sdk).

## TypeScript-Bibliothek

Mit der TypeScript-Bibliothek kann deine Anwendung lokale Codex-Threads starten, fortsetzen und wiederaufnehmen.

Verwende die Bibliothek serverseitig. Sie erfordert Node.js 18 oder höher.

### Installation

Installiere zunächst das Codex SDK mit `npm`:

```bash
npm install @openai/codex-sdk

### Verwendung

Starte einen Thread mit Codex und führe ihn mit deinem Prompt aus.

```ts

const codex = new Codex();
const thread = codex.startThread();
const result = await thread.run(
  "Make a plan to diagnose and fix the CI failures"
);

console.log(result.finalResponse);

Rufe `run()` erneut auf, um denselben Thread fortzusetzen, oder nimm einen früheren Thread wieder auf, indem du eine Thread-ID angibst.

```ts
// running the same thread
const result = await thread.run("Implement the plan");

console.log(result.finalResponse);

// resuming past thread

const threadId = "<thread-id>";
const thread2 = codex.resumeThread(threadId);
const result2 = await thread2.run("Pick up where you left off");

console.log(result2.finalResponse);

Weitere Informationen findest du im [TypeScript-Repository](https://github.com/openai/codex/tree/main/sdk/typescript).

## Python-Bibliothek

Das Python-SDK steuert den lokalen Codex App Server über JSON-RPC. Es erfordert Python 3.10 oder höher. Veröffentlichte SDK-Builds enthalten eine festgelegte Version von Codex CLI als Laufzeitabhängigkeit.

### Installation

Führe zur Installation des SDK folgenden Befehl aus:

```bash
pip install openai-codex

Veröffentlichte SDK-Builds verwenden automatisch die für sie festgelegte Laufzeitversion. Übergib `CodexConfig(codex_bin=...)` nur, wenn du gezielt eine bestimmte lokale ausführbare Codex-Datei verwenden möchtest.

Das Python-SDK ist als stabile Version verfügbar. `pip install openai-codex`
installiert die neueste stabile Version. Verwende `pip install --pre openai-codex`, wenn du stattdessen
neuere Vorab-Builds installieren möchtest.

### Verwendung

Starte Codex, erstelle einen Thread und führe einen Prompt aus:

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(
        model="gpt-5.6-terra",
        sandbox=Sandbox.workspace_write,
    )
    result = thread.run("Make a plan to diagnose and fix the CI failures")
    print(result.final_response)

Verwende `AsyncCodex`, wenn deine Anwendung bereits asynchron arbeitet:

```python

from openai_codex import AsyncCodex

async def main() -> None:
    async with AsyncCodex() as codex:
        thread = await codex.thread_start(model="gpt-5.6-terra")
        result = await thread.run("Implement the plan")
        print(result.final_response)

asyncio.run(main())

### Sandbox-Voreinstellungen

Verwende dieselben `Sandbox`-Voreinstellungen, wenn du einen Thread erstellst oder seinen Dateisystemzugriff
für einen späteren Turn änderst:

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(sandbox=Sandbox.workspace_write)
    thread.run("Make the requested change.")
    review = thread.run("Review the diff only.", sandbox=Sandbox.read_only)

Verfügbare Voreinstellungen:

- `Sandbox.read_only`: Dateien ohne Schreibzugriff lesen.
- `Sandbox.workspace_write`: Dateien lesen und im Workspace sowie in den konfigurierten beschreibbaren Stammverzeichnissen schreiben.
- `Sandbox.full_access`: Ohne Einschränkungen beim Dateisystemzugriff ausführen.

Wenn du `sandbox=` weglässt, verwendet der App Server die konfigurierte Standardeinstellung. Eine Sandbox,
die du an `run(...)` oder `turn(...)` übergibst, gilt für diesen Turn und alle späteren Turns
im Thread.

Weitere Informationen findest du im [Python-Repository](https://github.com/openai/codex/tree/main/sdk/python).
