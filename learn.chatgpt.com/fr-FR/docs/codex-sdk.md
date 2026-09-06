<!-- source: https://learn.chatgpt.com/fr-FR/docs/codex-sdk -->

Si vous utilisez Codex via Codex CLI, l’extension IDE ou Codex Cloud, vous pouvez également le contrôler par programmation.

Utilisez le SDK lorsque vous devez :

- Piloter Codex dans le cadre de votre pipeline CI/CD
- Créer votre propre agent capable d’interagir avec Codex pour effectuer des tâches d’ingénierie complexes
- Intégrer Codex à vos propres outils internes et flux de travail
- Intégrer Codex à votre propre application

Utilisez le SDK Codex pour automatiser des tâches de programmation, y compris des jobs de CI. Utilisez l’[App Server de Codex](/fr-FR/codex/app-server) pour créer des clients personnalisés qui gèrent l’authentification, l’historique des conversations, les approbations et les événements d’agent diffusés en continu.

`codex mcp-server` est déprécié. Le [guide du serveur MCP](/fr-FR/codex/mcp-server) reste disponible pour les intégrations existantes.

Si vous disposez d’un accès à la version bêta et avez besoin d’analyses de dépôts ou de modifications fournissant des constats de sécurité structurés
et des données de couverture, utilisez le [SDK TypeScript
de Codex Security](/fr-FR/codex/security/sdk).

## Bibliothèque TypeScript

La bibliothèque TypeScript permet à votre application de démarrer, de poursuivre et de reprendre des threads Codex locaux.

Utilisez la bibliothèque côté serveur ; elle nécessite Node.js 18 ou une version ultérieure.

### Installation

Pour commencer, installez le SDK Codex avec `npm` :

```bash
npm install @openai/codex-sdk

### Utilisation

Démarrez un thread avec Codex et exécutez-y votre prompt.

```ts

const codex = new Codex();
const thread = codex.startThread();
const result = await thread.run(
  "Make a plan to diagnose and fix the CI failures"
);

console.log(result.finalResponse);

Appelez à nouveau `run()` pour poursuivre le même thread, ou reprenez un thread précédent en fournissant son ID.

```ts
// running the same thread
const result = await thread.run("Implement the plan");

console.log(result.finalResponse);

// resuming past thread

const threadId = "<thread-id>";
const thread2 = codex.resumeThread(threadId);
const result2 = await thread2.run("Pick up where you left off");

console.log(result2.finalResponse);

Pour en savoir plus, consultez le [dépôt TypeScript](https://github.com/openai/codex/tree/main/sdk/typescript).

## Bibliothèque Python

Le SDK Python contrôle l’app-server Codex local via JSON-RPC. Il nécessite Python 3.10 ou une version ultérieure. Les distributions publiées du SDK incluent une version épinglée de Codex CLI comme dépendance d’exécution.

### Installation

Pour installer le SDK, exécutez :

```bash
pip install openai-codex

Les distributions publiées du SDK utilisent automatiquement l’environnement d’exécution dont la version est épinglée. Fournissez `CodexConfig(codex_bin=...)` uniquement si vous souhaitez délibérément utiliser un exécutable Codex local précis.

Le SDK Python est disponible en version stable. La commande `pip install openai-codex`
installe la dernière version stable. Utilisez `pip install --pre openai-codex` pour installer
des préversions plus récentes.

### Utilisation

Lancez Codex, créez un thread et exécutez un prompt :

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(
        model="gpt-5.6-terra",
        sandbox=Sandbox.workspace_write,
    )
    result = thread.run("Make a plan to diagnose and fix the CI failures")
    print(result.final_response)

Utilisez `AsyncCodex` si votre application est déjà asynchrone :

```python

from openai_codex import AsyncCodex

async def main() -> None:
    async with AsyncCodex() as codex:
        thread = await codex.thread_start(model="gpt-5.6-terra")
        result = await thread.run("Implement the plan")
        print(result.final_response)

asyncio.run(main())

### Préréglages du bac à sable

Utilisez les mêmes préréglages `Sandbox` lorsque vous créez un thread ou modifiez son accès au système de fichiers
pour un tour ultérieur :

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(sandbox=Sandbox.workspace_write)
    thread.run("Make the requested change.")
    review = thread.run("Review the diff only.", sandbox=Sandbox.read_only)

Préréglages disponibles :

- `Sandbox.read_only` : Permet de lire des fichiers sans autoriser les opérations d’écriture.
- `Sandbox.workspace_write` : Permet de lire des fichiers et d’écrire dans l’espace de travail et les répertoires racines configurés comme accessibles en écriture.
- `Sandbox.full_access` : Permet une exécution sans restriction d’accès au système de fichiers.

Lorsque vous omettez `sandbox=`, app-server utilise la valeur par défaut de sa configuration. Un bac à sable
transmis à `run(...)` ou `turn(...)` s’applique à ce tour et aux tours suivants
du thread.

Pour en savoir plus, consultez le [dépôt Python](https://github.com/openai/codex/tree/main/sdk/python).
