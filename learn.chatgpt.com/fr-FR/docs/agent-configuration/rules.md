<!-- source: https://learn.chatgpt.com/fr-FR/docs/agent-configuration/rules -->

Utilisez des règles pour contrôler les commandes que Codex peut exécuter en dehors du bac à sable.

Les règles sont expérimentales et peuvent évoluer.

## Création d’un fichier de règles

1. Créez un fichier `.rules` dans un dossier `rules/` situé à côté d’une couche de configuration active (par exemple, `~/.codex/rules/default.rules`).
2. Ajoutez une règle. Dans cet exemple, Codex demande confirmation avant d’autoriser l’exécution de `gh pr view` en dehors du bac à sable.

   ```python
   # Prompt before running commands with the prefix `gh pr view` outside the sandbox.
   prefix_rule(
       # The prefix to match.
       pattern = ["gh", "pr", "view"],

       # The action to take when Codex requests to run a matching command.
       decision = "prompt",

       # Optional rationale for why this rule exists.
       justification = "Viewing PRs is allowed with approval",

       # `match` and `not_match` are optional "inline unit tests" where you can
       # provide examples of commands that should (or should not) match this rule.
       match = [
           "gh pr view 7888",
           "gh pr view --repo openai/codex",
           "gh pr view 7888 --json title,body,comments",
       ],
       not_match = [
           # Does not match because the `pattern` must be an exact prefix.
           "gh pr --repo openai/codex view 7888",
       ],
   )

3. Redémarrez Codex.

Au démarrage, Codex analyse le dossier `rules/` de chaque couche de configuration active, y compris les emplacements de la [configuration d’équipe](/fr-FR/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config) et la couche utilisateur située à `~/.codex/rules/`. Les règles propres au projet dans `<repo>/.codex/rules/` ne sont chargées que si la couche `.codex/` du projet est considérée comme fiable.

Lorsque vous ajoutez une commande à la liste d’autorisation dans l’interface TUI, Codex l’enregistre dans la couche utilisateur à l’emplacement `~/.codex/rules/default.rules`, afin de ne plus demander confirmation lors des exécutions suivantes.

Lorsque les approbations intelligentes sont activées (option par défaut), Codex peut vous proposer une règle
`prefix_rule` lors des demandes d’élévation. Examinez le préfixe proposé
avec attention avant de l’accepter.

Les administrateurs peuvent également imposer des entrées `prefix_rule` restrictives au moyen de
[`requirements.toml`](/fr-FR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

## Champs d’une règle

`prefix_rule()` accepte les champs suivants :

- `pattern` **(obligatoire)** : liste non vide qui définit le préfixe auquel la commande doit correspondre. Chaque élément peut être :
  - Une chaîne littérale (par exemple, `"pr"`).
  - Une union de valeurs littérales (par exemple, `["view", "list"]`) pour faire correspondre plusieurs possibilités à cette position d’argument.
- `decision` **(valeur par défaut : `"allow"`)** : action à effectuer lorsque la règle s’applique. Si plusieurs règles s’appliquent, Codex applique la décision la plus restrictive (`forbidden` \> `prompt` \> `allow`).
  - `allow` : exécute la commande en dehors du bac à sable sans demander confirmation.
  - `prompt` : demande confirmation avant chaque invocation correspondante.
  - `forbidden` : bloque la requête sans demander confirmation.
- `justification` **(facultatif)** : motif non vide et compréhensible qui explique la règle. Codex peut l’afficher dans les demandes d’approbation ou les messages de rejet. Lorsque vous utilisez `forbidden`, indiquez dans la justification une solution de remplacement recommandée lorsque cela est pertinent (par exemple, `"Use \`rg\` plutôt que \`grep\`."\`).
- `match` et `not_match` **(valeur par défaut : `[]`)** : exemples que Codex valide au chargement de vos règles. Utilisez-les pour détecter les erreurs avant qu’une règle ne prenne effet.

Lorsque Codex envisage d’exécuter une commande, il compare la liste des arguments de celle-ci à `pattern`. En interne, Codex traite la commande comme une liste d’arguments (comme celle que reçoit `execvp(3)`).

## Wrappers shell et commandes composées

Certains outils regroupent plusieurs commandes shell dans une seule invocation, par exemple :

```text
["bash", "-lc", "git add . && rm -rf /"]

Comme ce type de commande peut dissimuler plusieurs actions dans une même chaîne, Codex applique un traitement particulier à `bash -lc`, `bash -c` et à leurs équivalents pour `zsh` / `sh`.

### Cas où Codex peut scinder le script en toute sécurité

Si le script shell forme une chaîne linéaire de commandes qui répond aux critères suivants :

- elle se compose de mots simples (sans expansion de variables ni éléments tels que `VAR=...`, `$FOO`, `*`, etc.)
- ses éléments sont reliés par des opérateurs sûrs (`&&`, `||`, `;` ou `|`)

Codex l’analyse alors (à l’aide de tree-sitter) et le scinde en commandes distinctes avant d’appliquer vos règles.

Le script ci-dessus est traité comme deux commandes distinctes :

- `["git", "add", "."]`
- `["rm", "-rf", "/"]`

Codex évalue ensuite chaque commande selon vos règles et retient le résultat le plus restrictif.

Même si vous autorisez `pattern=["git", "add"]`, Codex n’autorise pas automatiquement `git add . && rm -rf /`, car la partie `rm -rf /` est évaluée séparément et empêche l’autorisation automatique de l’ensemble de l’invocation.

Cela empêche de dissimuler des commandes dangereuses parmi des commandes sûres.

### Cas où Codex ne scinde pas le script

Si le script utilise des fonctionnalités plus avancées du shell, telles que :

- les redirections (`>`, `>>`, `<`)
- les substitutions (`$(...)`, `...`)
- les variables d’environnement (`FOO=bar`)
- les motifs avec caractères génériques (`*`, `?`)
- les structures de contrôle (`if`, `for`, `&&` avec des affectations, etc.)

Codex n’essaie alors ni de l’interpréter ni de le scinder.

Dans ce cas, l’ensemble de l’invocation est traité comme suit :

```text
["bash", "-lc", "<full script>"]

et vos règles sont appliquées à cette **unique** invocation.

Ce traitement permet d’évaluer séparément chaque commande lorsqu’il est possible de le faire en toute sécurité, tout en adoptant une approche prudente dans le cas contraire.

## Test d’un fichier de règles

Utilisez `codex execpolicy check` pour tester l’application de vos règles à une commande :

```shell
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888 --json title,body,comments

La commande produit une sortie JSON indiquant la décision la plus restrictive et les éventuelles règles correspondantes, y compris les valeurs `justification` de celles-ci. Répétez l’option `--rules` pour combiner des fichiers et ajoutez `--pretty` pour mettre en forme la sortie.

## Langage des règles

Le format de fichier `.rules` utilise `Starlark` (consultez la [spécification du langage](https://github.com/bazelbuild/starlark/blob/master/spec.md)). Sa syntaxe ressemble à celle de Python, mais le langage est conçu pour une exécution sûre : le moteur de règles peut l’exécuter sans effets de bord (par exemple, sans toucher au système de fichiers).
