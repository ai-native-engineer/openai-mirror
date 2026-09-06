<!-- source: https://learn.chatgpt.com/fr-FR/docs/non-interactive-mode -->

Le mode non interactif vous permet d’exécuter Codex à partir de scripts (par exemple, des tâches d’intégration continue (CI)) sans ouvrir l’interface TUI interactive.
Pour le lancer, utilisez `codex exec`.

Pour plus de détails sur les options, consultez [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec).

## Quand utiliser `codex exec`

Utilisez `codex exec` lorsque vous souhaitez que Codex :

- S’exécute dans le cadre d’un pipeline (CI, vérifications préalables à la fusion, tâches planifiées).
- Produise une sortie que vous pouvez rediriger vers d’autres outils (par exemple, pour générer des notes de version ou des résumés).
- S’intègre naturellement aux flux de travail CLI qui transmettent à Codex la sortie de commandes, puis la sortie de Codex à d’autres outils.
- S’exécute avec des paramètres explicites et prédéfinis pour le bac à sable et l’approbation.

## Utilisation de base

Transmettez un prompt de tâche sous la forme d’un seul argument :

```bash
codex exec "summarize the repository structure and list the top 5 risky areas"

Pendant l’exécution de `codex exec`, Codex diffuse sa progression dans `stderr` et n’écrit que le message final de l’agent dans `stdout`. Vous pouvez ainsi facilement rediriger le résultat final ou le transmettre via un tube :

```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md

Utilisez `--ephemeral` si vous ne souhaitez pas enregistrer les fichiers de déroulement de session sur le disque :

```bash
codex exec --ephemeral "triage this repository and suggest next steps"

Si une entrée est redirigée vers stdin et que vous fournissez également un prompt en argument, Codex considère le prompt comme l’instruction et le contenu redirigé comme du contexte supplémentaire.

Vous pouvez ainsi générer une entrée avec une commande et la transmettre directement à Codex :

```bash
curl -s https://jsonplaceholder.typicode.com/comments \
  | codex exec "format the top 20 items into a markdown table" \
  > table.md

Pour des méthodes plus avancées de redirection de stdin, consultez [Redirection avancée de stdin](#advanced-stdin-piping).

## Autorisations et sécurité

Par défaut, `codex exec` s’exécute dans un bac à sable en lecture seule. Pour l’automatisation, définissez les autorisations minimales requises par le flux de travail :

- Autorisez les modifications : `codex exec --sandbox workspace-write "<task>"`
- Autorisez un accès plus étendu : `codex exec --sandbox danger-full-access "<task>"`

N’utilisez `danger-full-access` que dans un environnement contrôlé (par exemple, un runner CI isolé ou un conteneur).

Codex conserve `codex exec --full-auto` comme option de compatibilité obsolète et affiche un avertissement. Dans les nouveaux scripts, privilégiez l’option explicite `--sandbox workspace-write`.

Utilisez `--ignore-user-config` pour exécuter Codex sans charger `$CODEX_HOME/config.toml`, et `--ignore-rules` pour ignorer les fichiers `.rules` d’execpolicy de l’utilisateur et du projet dans un environnement d’automatisation contrôlé.

Si vous configurez un serveur MCP activé avec `required = true` et que son initialisation échoue, `codex exec` se termine avec une erreur au lieu de continuer sans ce serveur.

## Rendre la sortie exploitable par une machine

Pour exploiter la sortie de Codex dans des scripts, utilisez une sortie au format JSON Lines :

```bash
codex exec --json "summarize the repo structure" | jq

Lorsque vous activez `--json`, `stdout` devient un flux JSON Lines (JSONL), ce qui vous permet de capturer chaque événement émis par Codex pendant son exécution. Les types d’événements incluent `thread.started`, `turn.started`, `turn.completed`, `turn.failed`, `item.*` et `error`.

Les types d’éléments incluent les messages de l’agent, le raisonnement, l’exécution de commandes, les modifications de fichiers, les appels d’outils MCP, les recherches web et les mises à jour du plan.

Exemple de flux JSON (chaque ligne est un objet JSON) :

```jsonl
{"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122,"reasoning_output_tokens":0}}

Si vous n’avez besoin que du message final, écrivez-le dans un fichier avec `-o <path>`/`--output-last-message <path>`. Cette option écrit le message final dans le fichier et l’affiche également dans `stdout` (consultez [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec) pour plus de détails).

## Créer des sorties structurées à l’aide d’un schéma

Si les étapes suivantes nécessitent des données structurées, utilisez `--output-schema` pour demander une réponse finale conforme à un schéma JSON.
Cette option est utile pour les flux de travail automatisés qui nécessitent des champs stables (par exemple, des résumés de tâches, des rapports sur les risques ou des métadonnées de version).

`schema.json`

```json
{
  "type": "object",
  "properties": {
    "project_name": { "type": "string" },
    "programming_languages": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["project_name", "programming_languages"],
  "additionalProperties": false
}

Exécutez Codex avec le schéma et écrivez la réponse JSON finale sur le disque :

```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json

Exemple de sortie finale (stdout) :

```json
{
  "project_name": "Codex CLI",
  "programming_languages": ["Rust", "TypeScript", "Shell"]
}

## Authentification pour l’automatisation

`codex exec` réutilise par défaut l’authentification CLI enregistrée. En CI, il est courant de fournir explicitement les identifiants :

Si votre environnement d’exécution cloud ou CI de confiance reçoit déjà des tokens de charge de travail
de courte durée, utilisez
[la fédération d’identités de charge de travail](/fr-FR/codex/enterprise/workload-identity)
au lieu de stocker un identifiant OpenAI.

### Authentification par clé API

Pour GitHub Actions, utilisez la [GitHub Action Codex](/fr-FR/codex/github-action) plutôt que d’installer vous-même la CLI et de vous y authentifier. Cette action est conçue pour réduire l’exposition de la clé API en installant Codex, en démarrant un proxy de la Responses API et en exécutant Codex avec une stratégie de sécurité configurable.

Ne définissez pas `OPENAI_API_KEY` ou `CODEX_API_KEY` comme variable d’environnement au niveau du job dans les flux de travail qui récupèrent ou exécutent du code contrôlé par le dépôt. Les scripts de build, les tests, les hooks du cycle de vie des dépendances ou une action compromise dans le même job peuvent lire ces variables d’environnement.

Pour les autres environnements d’automatisation, définissez `CODEX_API_KEY` uniquement pour l’invocation de Codex
qui en a besoin et assurez-vous qu’aucun code non fiable ne s’exécute dans l’environnement du même
processus.

Pour utiliser une autre clé API lors d’une seule exécution, définissez `CODEX_API_KEY` directement dans la commande :

```bash
CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"

Vous pouvez utiliser `CODEX_API_KEY` avec `codex exec`, `codex review`, le SDK
TypeScript et `codex exec-server --remote`.

Consultez cette section si vous devez exécuter des jobs CI/CD avec un compte utilisateur Codex plutôt qu’une
clé API, par exemple pour les équipes d’entreprise qui utilisent l’accès Codex géré par ChatGPT sur des runners de confiance
ou pour les utilisateurs qui ont besoin des limites de débit de ChatGPT/Codex plutôt que d’utiliser une clé API.

Pour l’automatisation, privilégiez par défaut les clés API, car elles sont plus simples à
provisionner et à renouveler. N’utilisez cette méthode que si vous avez spécifiquement besoin d’exécuter Codex avec
votre compte Codex.

Traitez `~/.codex/auth.json` comme un mot de passe : ce fichier contient des jetons d’accès. Ne le
commitez pas, ne collez pas son contenu dans des tickets et ne le partagez pas dans une discussion.

N’utilisez pas ce flux de travail pour les dépôts publics ou open source. Si `codex login`
n’est pas possible sur le runner, fournissez `auth.json` via un stockage sécurisé, exécutez
Codex sur le runner afin qu’il mette le fichier à jour sur place, puis conservez le fichier mis à jour
d’une exécution à l’autre.

Consultez [Maintenir l’authentification du compte Codex en CI/CD (avancé)](/codex/auth/ci-cd-auth).

## Reprendre une session non interactive

Pour poursuivre une exécution précédente (par exemple, dans un pipeline en deux étapes), utilisez la sous-commande `resume` :

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"

Vous pouvez également cibler un identifiant de session précis avec `codex exec resume <SESSION_ID>`.

## Dépôt Git requis

Pour éviter les modifications destructrices, Codex exige que les commandes soient exécutées dans un dépôt Git. Si vous êtes certain que l’environnement est sûr, contournez cette vérification avec `codex exec --skip-git-repo-check`.

## Scénarios d’automatisation courants

### Exemple : correction automatique des échecs de CI dans GitHub Actions

Pour les flux de travail GitHub Actions, utilisez [`openai/codex-action`](https://github.com/openai/codex-action) au lieu d’installer Codex et de transmettre la clé API à une étape shell. L’action démarre un proxy sécurisé pour la clé API OpenAI.

Vous pouvez utiliser Codex pour proposer automatiquement des correctifs lorsqu’un flux de travail CI échoue. Procédez comme suit :

1. Déclenchez un flux de travail de suivi lorsque votre flux de travail CI principal se termine par une erreur.
2. Récupérez le commit concerné par l’échec avec uniquement des autorisations de lecture sur le dépôt.
3. Exécutez les commandes de configuration avant de lancer Codex, sans exposer votre clé API OpenAI à ces étapes.
4. Exécutez la GitHub Action Codex.
5. Enregistrez les modifications locales de Codex dans un artefact contenant un patch.
6. Dans un job distinct, appliquez le patch et ouvrez une pull request.

Le job Codex ci-dessous dispose uniquement de l’autorisation `contents: read`. Une fois l’exécution de Codex terminée, ce job ne sérialise que le diff sous forme d’artefact. Le job `open_pr` reçoit les autorisations d’écriture sur le dépôt, mais pas `OPENAI_API_KEY`.

Cet exemple suppose un projet Node.js. Adaptez les commandes de configuration et de test à votre stack technique.

Pour une liste de contrôle de sécurité plus complète, consultez les [consignes de sécurité relatives à Codex GitHub Action](https://github.com/openai/codex-action/blob/main/docs/security.md).

```yaml
name: Codex auto-fix on CI failure

on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

jobs:
  generate_fix:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      has_patch: ${{ steps.diff.outputs.has_patch }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0
          persist-credentials: false

      - uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install dependencies
        run: |
          if [ -f package-lock.json ]; then npm ci; fi

      - name: Run Codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt: |
            The CI workflow "${{ github.event.workflow_run.name }}" failed for commit
            ${{ github.event.workflow_run.head_sha }}.

            Run `npm test --silent` to reproduce the failure. Identify the minimal
            change needed to make the tests pass, implement only that change, and
            run `npm test --silent` again.

            Do not refactor unrelated files.

      - name: Create patch artifact
        id: diff
        run: |
          git add -N .
          git diff --binary HEAD > codex.patch
          if [ -s codex.patch ]; then
            echo "has_patch=true" >> "$GITHUB_OUTPUT"
          else
            echo "has_patch=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload patch artifact
        if: steps.diff.outputs.has_patch == 'true'
        uses: actions/upload-artifact@v4
        with:
          name: codex-fix-patch
          path: codex.patch
          if-no-files-found: error

  open_pr:
    runs-on: ubuntu-latest
    needs: generate_fix
    if: needs.generate_fix.outputs.has_patch == 'true'
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0

      - uses: actions/download-artifact@v4
        with:
          name: codex-fix-patch

      - name: Apply Codex patch
        run: git apply --index codex.patch

      - name: Open pull request
        env:
          GH_TOKEN: ${{ github.token }}
          FAILED_HEAD_BRANCH: ${{ github.event.workflow_run.head_branch }}
          FAILED_HEAD_SHA: ${{ github.event.workflow_run.head_sha }}
          RUN_ID: ${{ github.event.workflow_run.run_id }}
        run: |
          branch="codex/auto-fix-$RUN_ID"

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git switch -c "$branch"
          git commit -m "Auto-fix failing CI via Codex"
          git push origin "$branch"

          {
            echo "Codex generated this patch after CI failed for \`$FAILED_HEAD_SHA\`."
            echo
            echo "Review the changes before merging."
          } > pr-body.md

          gh pr create \
            --base "$FAILED_HEAD_BRANCH" \
            --head "$branch" \
            --title "Auto-fix failing CI via Codex" \
            --body-file pr-body.md

## Redirection avancée vers stdin

Lorsqu’une autre commande génère des données d’entrée pour Codex, choisissez comment utiliser stdin selon la provenance souhaitée de l’instruction. Utilisez un prompt avec stdin si vous connaissez déjà l’instruction et souhaitez rediriger la sortie vers stdin pour fournir du contexte. Utilisez `codex exec -` lorsque stdin doit fournir l’intégralité du prompt.

### Utilisez un prompt avec stdin

L’utilisation d’un prompt avec stdin est utile lorsqu’une autre commande produit déjà les données que vous souhaitez demander à Codex d’analyser. Dans ce mode, vous rédigez vous-même l’instruction et redirigez la sortie vers stdin afin qu’elle serve de contexte. Cette méthode s’intègre naturellement aux flux de travail CLI fondés sur les sorties de commandes, les journaux et les données générées.

```bash
npm test 2>&1 \
  | codex exec "summarize the failing tests and propose the smallest likely fix" \
  | tee test-summary.md

### Résumez les journaux

```bash
tail -n 200 app.log \
  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
  > log-triage.md

### Analysez les problèmes TLS ou HTTP

```bash
curl -vv https://api.example.com/health 2>&1 \
  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
  > tls-debug.md

### Préparez une mise à jour à publier sur Slack

```bash
gh run view 123456 --log \
  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
  | pbcopy

### Rédigez un commentaire de pull request à partir des journaux de CI

```bash
gh run view 123456 --log \
  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
  | gh pr comment 789 --body-file -

### Utilisez `codex exec -` lorsque le prompt provient de stdin

Si vous omettez l’argument du prompt, Codex lit le prompt depuis stdin. Utilisez `codex exec -` pour imposer explicitement ce comportement.

La valeur sentinelle `-` est utile lorsqu’une autre commande ou un autre script génère dynamiquement l’intégralité du prompt. Cette approche convient bien lorsque vous stockez des prompts dans des fichiers, les assemblez à l’aide de scripts shell ou combinez la sortie en temps réel d’une commande avec des instructions avant de transmettre le prompt complet à Codex.

```bash
cat prompt.txt | codex exec -

```bash
printf "Summarize this error log in 3 bullets:\n\n%s\n" "$(tail -n 200 app.log)" \
  | codex exec -

```bash
generate_prompt.sh | codex exec - --json > result.jsonl
