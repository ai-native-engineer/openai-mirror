<!-- source: https://learn.chatgpt.com/fr-FR/docs/github-action -->

Utilisez la GitHub Action Codex (`openai/codex-action@v1`) pour exécuter Codex dans des jobs CI/CD, appliquer des patchs ou publier des revues de code depuis un workflow GitHub Actions.
L’action installe la CLI Codex, démarre le proxy de la Responses API lorsque vous fournissez une clé API et exécute `codex exec` avec les autorisations que vous spécifiez.

Utilisez cette action pour :

- Automatiser les retours de Codex sur les pull requests ou les versions sans avoir à gérer vous-même la CLI.
- Conditionner l’intégration des modifications à la réussite des contrôles qualité pilotés par Codex dans votre pipeline CI.
- Exécuter depuis un fichier de workflow des tâches Codex reproductibles (revue de code, préparation des versions, migrations).

Pour consulter un exemple de CI, consultez la page [Mode non interactif](/fr-FR/codex/non-interactive-mode) et explorez le code source dans le [dépôt openai/codex-action](https://github.com/openai/codex-action).

## Prérequis

- Stockez votre clé OpenAI en tant que secret GitHub (par exemple `OPENAI_API_KEY`), puis référencez ce secret dans le workflow.
- Exécutez le job sur un runner Linux ou macOS. Sous Windows, définissez `safety-strategy: unsafe`.
- Récupérez votre code avant d’appeler l’action afin que Codex puisse lire le contenu du dépôt.
- Choisissez les prompts à exécuter. Vous pouvez fournir directement du texte avec `prompt` ou, avec `prompt-file`, indiquer le chemin d’un fichier versionné dans le dépôt.

## Exemple de workflow

L’exemple de workflow ci-dessous effectue une revue des nouvelles pull requests, récupère la réponse de Codex et la publie sur la PR.

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge
          fetch-depth: 0
          persist-credentials: false

      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    permissions:
      issues: write
      pull-requests: write
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}

Remplacez `.github/codex/prompts/review.md` par votre propre fichier de prompt ou utilisez l’entrée `prompt` pour fournir directement du texte. L’exemple écrit également le message final de Codex dans `codex-output.md` afin de pouvoir l’examiner ou le charger ultérieurement comme artefact.

## Configuration de `codex exec`

Ajustez l’exécution de Codex en définissant les entrées de l’action qui correspondent aux options de `codex exec` :

- `prompt` ou `prompt-file` (choisissez une seule option) : fournissez directement les instructions ou indiquez le chemin, dans le dépôt, d’un fichier Markdown ou d’un fichier texte contenant votre tâche. Envisagez de stocker les prompts dans `.github/codex/prompts/`.
- `codex-args` : options CLI supplémentaires. Fournissez un tableau JSON (par exemple `["--ephemeral"]`) ou une chaîne shell (`--profile ci`) pour configurer les sessions, les profils ou les paramètres MCP.
- `model` et `effort` : choisissez la configuration souhaitée pour l’agent Codex ; laissez ces champs vides pour utiliser les valeurs par défaut.
- `sandbox` : adaptez le mode de bac à sable (`workspace-write`, `read-only`, `danger-full-access`) aux autorisations nécessaires à Codex pendant l’exécution.
- `output-file` : enregistrez sur disque le message final de Codex pour que les étapes suivantes puissent le charger ou en générer un diff.
- `codex-version` : fixez une version précise de la CLI. Laissez ce champ vide pour utiliser la dernière version publiée.
- `codex-home` : indiquez un répertoire d’accueil partagé de Codex si vous souhaitez réutiliser des fichiers de configuration ou des configurations MCP d’une étape à l’autre.

## Gestion des privilèges

Codex dispose d’un accès étendu sur les runners hébergés par GitHub, sauf si vous le restreignez. Utilisez ces entrées pour contrôler le niveau d’exposition :

- `safety-strategy` (`drop-sudo` par défaut) supprime `sudo` avant d’exécuter Codex. Cette opération est irréversible pour ce job et protège les secrets en mémoire. Sous Windows, vous devez définir `safety-strategy: unsafe`.
- `unprivileged-user` associe `safety-strategy: unprivileged-user` à `codex-user` pour exécuter Codex sous un compte donné. Vérifiez que l’utilisateur dispose d’un accès en lecture et en écriture à la copie locale du dépôt (consultez [l’exemple `unprivileged-user`](https://github.com/openai/codex-action/blob/main/examples/unprivileged-user.yml) pour corriger la propriété des fichiers).
- `read-only` empêche Codex de modifier des fichiers ou d’utiliser le réseau, mais il continue de s’exécuter avec des privilèges élevés. Ne comptez pas uniquement sur `read-only` pour protéger les secrets.
- `sandbox` limite l’accès au système de fichiers et au réseau au sein même de Codex. Choisissez l’option la plus restrictive qui permet tout de même d’accomplir la tâche.
- `allow-users` et `allow-bots` restreignent les comptes autorisés à déclencher le workflow. Par défaut, seuls les utilisateurs disposant d’un accès en écriture peuvent exécuter l’action ; indiquez explicitement tout compte de confiance supplémentaire ou laissez le champ vide pour conserver le comportement par défaut.

## Capture des sorties

L’action expose le dernier message de Codex via la sortie `final-message`. Déclarez-la comme sortie du job (comme indiqué ci-dessus) ou traitez-la directement au cours d’étapes ultérieures. Associez `output-file` au chargement d’artefacts si vous préférez récupérer la transcription complète depuis le runner. Lorsque vous avez besoin de données structurées, transmettez `--output-schema` à l’aide de `codex-args` pour imposer une structure JSON.

## Liste de contrôle de sécurité

- Limitez les comptes autorisés à démarrer le workflow. Privilégiez les événements provenant de sources fiables ou les approbations explicites plutôt que d’autoriser tout le monde à exécuter Codex sur votre dépôt.
- Assainissez les entrées de prompt provenant des pull requests, des messages de commit ou du contenu des issues afin d’éviter les attaques par injection de prompt. Examinez les commentaires HTML ou le texte masqué avant de transmettre ces éléments à Codex.
- Protégez votre `OPENAI_API_KEY` en laissant `safety-strategy` défini sur `drop-sudo` ou en exécutant Codex avec un utilisateur non privilégié. Ne laissez jamais l’action en mode `unsafe` sur des runners mutualisés.
- Exécutez Codex comme dernière étape d’un job afin que les éventuelles étapes suivantes n’héritent d’aucun changement d’état inattendu.
- Renouvelez immédiatement les clés si vous soupçonnez que les journaux du proxy ou la sortie de l’action ont exposé des données secrètes.

## Dépannage

- **Vous avez défini à la fois prompt et prompt-file** : supprimez l’entrée en double afin de ne fournir qu’une seule source.
- **responses-api-proxy n’a pas écrit les informations sur le serveur** : vérifiez que la clé API est présente et valide ; le proxy ne démarre que lorsque vous fournissez `openai-api-key`.
- **La suppression de `sudo` était attendue, mais `sudo` a fonctionné** : vérifiez qu’aucune étape précédente n’a rétabli `sudo` et que le système d’exploitation du runner est Linux ou macOS. Relancez l’opération dans un nouveau job.
- **Erreurs d’autorisation après `drop-sudo`** : accordez l’accès en écriture avant l’exécution de l’action (par exemple avec `chmod -R g+rwX "$GITHUB_WORKSPACE"` ou en utilisant le modèle unprivileged-user).
- **Déclenchement non autorisé bloqué** : ajustez les paramètres d’entrée `allow-users` ou `allow-bots` si vous devez autoriser des comptes de service en plus des collaborateurs autorisés par défaut grâce à leur accès en écriture.
