<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/cli/reference -->

Utilisez cette référence pour consulter les commandes et les options `codex-security` prises en charge,
les formats de sortie et le comportement en fin d’exécution. Pour une première analyse guidée, commencez par le
[démarrage rapide de la CLI](/fr-FR/codex/security/cli).

  Le package `@openai/codex-security` est public. L’exécution d’analyses nécessite un accès à Codex
  Security. Les analyses utilisent vos autorisations locales et ne s’interrompent pas pour demander une
  approbation. Avant de commencer, consultez la section [Autorisations des analyses
  locales](#local-scan-permissions).

Exécutez la CLI avec `npx @openai/codex-security`.

## Vue d’ensemble des commandes

```text
usage: codex-security [--version] <command> [options]

La CLI fournit les commandes suivantes :

| Commande                       | Fonction                                               |
| ----------------------------- | ----------------------------------------------------- |
| `codex-security scan`         | Exécutez une analyse Codex Security.                            |
| `codex-security install-hook` | Installez une analyse de sécurité Git pre-commit.               |
| `codex-security bulk-scan`    | Découvrez des dépôts et exécutez des analyses en masse pouvant être reprises.   |
| `codex-security scans`        | Répertoriez, examinez, comparez et récupérez les journaux d’analyse enregistrés. |
| `codex-security findings`     | Examinez et mettez à jour les constats de sécurité enregistrés.            |
| `codex-security export`       | Exportez les constats finalisés au format CSV, JSON ou SARIF.     |
| `codex-security publish`      | Publiez dans Linear les constats d’une analyse terminée.            |
| `codex-security validate`     | Vérifiez un ou plusieurs constats de sécurité potentiels.        |
| `codex-security patch`        | Corrigez un ou plusieurs problèmes de sécurité.                    |
| `codex-security login`        | Connectez-vous, enregistrez vos identifiants ou vérifiez l’état de la connexion.  |
| `codex-security logout`       | Supprimez la connexion enregistrée.                            |
| `codex-security info`         | Affichez les métadonnées en lecture seule du SDK et du plugin fourni.       |

La CLI fournit également les commandes d’intégration suivantes :

| Commande                      | Fonction                               |
| ---------------------------- | ------------------------------------- |
| `codex-security completions` | Générez des scripts de complétion shell.    |
| `codex-security mcp`         | Enregistrez la CLI en tant que serveur MCP.    |
| `codex-security skills`      | Synchronisez les Skills Codex Security avec les agents. |

Affichez toutes les commandes disponibles :

```bash
npx @openai/codex-security --help

Ajoutez `--help` à une commande pour consulter ses arguments et ses options :

```bash
npx @openai/codex-security scan --help

`codex-security --version` affiche la version installée, puis se termine.
`codex-security info --json` indique les versions du SDK et du plugin fourni.
Aucune de ces commandes ne nécessite Python.

### Découvrez les commandes et connectez des agents

Affichez le manifeste des commandes lisible par les agents :

```bash
npx @openai/codex-security --llms

Examinez le schéma des arguments d’analyse au format JSON :

```bash
npx @openai/codex-security scan --schema --format json

Générez les complétions shell pour Bash :

```bash
npx @openai/codex-security completions bash

Pour ces shells, remplacez `bash` par `zsh` ou `fish`.

Les résultats d’analyse prennent en charge `--format toon|json|yaml|jsonl` et `--full-output`. Cette option
`--format`, définie au niveau du framework, est distincte de `--export-format`, qui sélectionne
le format d’un artefact exporté à partir d’une analyse terminée. L’aide globale des commandes
répertorie également `md`, mais les résultats d’analyse ne prennent pas en charge les sorties Markdown.

Enregistrez la CLI en tant que serveur MCP :

```bash
npx @openai/codex-security mcp add

Synchronisez les Skills Codex Security avec vos agents :

```bash
npx @openai/codex-security skills add

MCP n’expose que la commande de métadonnées `info` en lecture seule. Les analyses, les exportations,
l’authentification, la validation et l’application de correctifs restent accessibles uniquement via la CLI.

## `codex-security scan`

Exécutez une analyse sur un dépôt, des chemins sélectionnés, des modifications commitées ou
l’arbre de travail.

```text
usage: codex-security scan [-h] [--auth {auto,chatgpt,api-key}]
                           [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                           [--path PATH | --diff BASE | --working-tree]
                           [--head HEAD] [--base BASE]
                           [--knowledge-base PATH] [--scan-prompt-file FILE]
                           [--post-scan-prompt-file FILE]
                           [--mode {standard,deep}] [--workers N]
                           [--subagents N] [--stop-after-no-new N]
                           [--max-discovery-runs N] [--max-time-hours HOURS]
                           [--model MODEL]
                           [--effort {minimal,low,medium,high,xhigh,max}]
                           [--output-dir DIR]
                           [--archive-existing]
                           [--plugin-path PATH] [--python PATH]
                           [--codex KEY=VALUE] [--fail-on-severity LEVEL]
                           [--patch] [--patch-severity {critical,high,medium,low}]
                           [--create-pr]
                           [--max-cost USD] [--dry-run] [--headless] [--verbose]
                           [--json] [--format {toon,json,yaml,jsonl}]
                           [--full-output] [repository]

`repository` utilise par défaut le répertoire courant.

### Sélectionnez l’authentification de l’analyse

Utilisez `--auth auto`, la valeur par défaut, pour sélectionner automatiquement les identifiants. Lorsque vous disposez à la fois
d’une connexion ChatGPT et de `OPENAI_API_KEY` ou `CODEX_API_KEY`,
les analyses interactives avec sortie texte vous demandent quels identifiants utiliser. Les analyses en CI, les analyses JSON et
JSONL, ainsi que les autres analyses sans terminal interactif, utilisent la
clé API de l’environnement. Les exécutions à blanc n’affichent aucune invite et ne chargent aucun identifiant.

Pour utiliser vos identifiants enregistrés, indiquez `--auth chatgpt` :

```bash
npx @openai/codex-security scan . --auth chatgpt

Pour utiliser une clé API définie dans l’environnement, indiquez `--auth api-key` :

```bash
npx @openai/codex-security scan . --auth api-key

Pour que les identifiants enregistrés soient utilisés automatiquement par défaut, exécutez
`unset OPENAI_API_KEY CODEX_API_KEY`.

### Utilisez OpenRouter ou Fireworks

Sélectionnez OpenRouter avec sa clé API et un modèle spécifié explicitement :

```bash

npx @openai/codex-security scan . \
  --provider openrouter \
  --model anthropic/claude-sonnet-4.5

Sélectionnez Fireworks avec sa clé API et un modèle spécifié explicitement :

```bash

npx @openai/codex-security scan . \
  --provider fireworks \
  --model accounts/fireworks/models/qwen3-235b-a22b

Les deux fournisseurs prennent également en charge `bulk-scan`.

### Utilisez Amazon Bedrock

Sélectionnez Amazon Bedrock avec `--provider amazon-bedrock` et spécifiez explicitement un modèle
Bedrock avec `--model` :

```bash
npx @openai/codex-security scan . \
  --provider amazon-bedrock \
  --model openai.gpt-5.6-sol

Définissez `AWS_REGION`, puis authentifiez-vous à l’aide de `AWS_BEARER_TOKEN_BEDROCK`, de clés d’accès AWS
standard, d’un profil AWS, d’une identité web, d’identifiants de conteneur ou de la
chaîne d’identifiants AWS par défaut. Les analyses Bedrock utilisent des identifiants AWS au lieu de
`--auth`, d’une connexion ChatGPT ou d’une clé API OpenAI. Les commandes `scan` et `bulk-scan`
prennent toutes deux en charge `--provider`.

### Sélectionnez la cible de l’analyse

Choisissez un seul type de cible pour chaque analyse.

| Argument                 | Description                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| `--path PATH`            | Analysez un chemin relatif au dépôt. Répétez l’option pour chaque chemin supplémentaire.         |
| `--diff BASE`            | Analysez les modifications commitées de `BASE` à `--head`. La révision de tête est `HEAD` par défaut.    |
| `--head HEAD`            | Définissez la révision de tête pour `--diff`.                                             |
| `--working-tree`         | Analysez les modifications indexées et non indexées par rapport à `--base`. La révision de base est `HEAD` par défaut. |
| `--base BASE`            | Définissez la révision de base pour `--working-tree`.                                     |
| `--mode {standard,deep}` | Sélectionnez le mode d’analyse. La valeur par défaut est `standard`.                                |

`--path`, `--diff` et `--working-tree` s’excluent mutuellement. `--head`
nécessite `--diff`, et `--base` nécessite `--working-tree`. Le mode approfondi prend en charge
les dépôts et les chemins comme cibles.

Les analyses de diff et de l’arbre de travail exigent que l’argument du dépôt corresponde à la racine de l’arbre de
travail Git. Les références sélectionnées doivent exister dans cette copie de travail.

Analysez l’ensemble du dépôt :

```bash
npx @openai/codex-security scan .

Analysez les chemins sélectionnés :

```bash
npx @openai/codex-security scan . --path src --path tests

Analysez les modifications commitées :

```bash
npx @openai/codex-security scan . --diff origin/main --head HEAD

Analysez les modifications indexées et non indexées :

```bash
npx @openai/codex-security scan . --working-tree --base HEAD

Effectuez une revue plus approfondie du dépôt :

```bash
npx @openai/codex-security scan . --mode deep

### Configurez les analyses approfondies

Utilisez ces options avec `--mode deep` pour contrôler le parallélisme des workers et leur durée d’exécution :

| Argument                 | Description                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `--workers N`            | Nombre maximal de workers d’analyse standard indépendants exécutés simultanément. La valeur par défaut est `4`.                |
| `--subagents N`          | Sous-agents disponibles pour chaque worker. La valeur par défaut est `3`.                                   |
| `--stop-after-no-new N`  | Arrêtez l’analyse après `N` analyses de workers consécutives, terminées sans détecter de nouveaux problèmes. La valeur par défaut est `4`. |
| `--max-discovery-runs N` | Nombre maximal total d’exécutions indépendantes d’analyses standard. La valeur par défaut est `40`.                       |
| `--max-time-hours HOURS` | Durée maximale d’exécution des workers, en heures. La valeur par défaut est `96` ; les valeurs fractionnaires sont acceptées.             |

`--subagents` accepte zéro ou un entier strictement positif. `--max-time-hours` accepte un nombre
strictement positif inférieur ou égal à `96`. Les autres options exigent un entier
strictement positif. Ces options ne sont pas disponibles pour les analyses standard.

Par exemple, utilisez deux workers, autorisez jusqu’à dix exécutions et arrêtez l’exécution des workers
après 1,5 heure :

```bash
npx @openai/codex-security scan . \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

À l’expiration de la limite de temps, l’analyse arrête les workers qui n’ont pas terminé, conserve les résultats des
analyses terminées et les agrège dans le rapport final. Si aucun worker ne termine la revue
du code source, l’analyse enregistre une couverture partielle et renvoie le code de sortie `2`.

Définissez les valeurs par défaut persistantes dans `~/.codex/codex-security/config.toml`, ou dans
`$CODEX_HOME/codex-security/config.toml` lorsque vous définissez `CODEX_HOME` :

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

Les options de ligne de commande remplacent ces valeurs par défaut. `scan --workers` contrôle les workers
indépendants chargés des analyses standard au sein d’une même analyse approfondie ; `bulk-scan --workers`
contrôle les analyses de dépôts exécutées simultanément. Définissez `stop_after_consecutive_errors` uniquement
dans le fichier TOML ; sa valeur par défaut est `3`.

### Ajoutez du contexte de sécurité

Utilisez `--knowledge-base PATH` pour fournir des documents d’architecture, des modèles de menaces
ou des politiques de sécurité. Répétez l’option pour ajouter d’autres fichiers ou répertoires :

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Les documents pris en charge incluent les fichiers `.md`, `.markdown`, `.txt`, `.pdf` et `.docx`.
La CLI parcourt les répertoires de manière récursive, refuse les chemins d’entrée qui sont des liens symboliques,
ignore les liens symboliques présents dans les répertoires et conserve le contenu extrait des documents
en dehors des résultats d’analyse enregistrés.

### Ajoutez des instructions d’analyse

Pour ajouter des instructions d’analyse, fournissez un fichier texte ou Markdown avec
`--scan-prompt-file`. Utilisez `--post-scan-prompt-file` pour exécuter des instructions de suivi
dans la même session authentifiée après les analyses réussies et les analyses
dont la couverture est incomplète ou qui comportent des erreurs :

```bash
npx @openai/codex-security scan . \
  --scan-prompt-file security-focus.md \
  --post-scan-prompt-file follow-up.md

Par exemple, utilisez le prompt d’analyse pour cibler les limites d’autorisation et demandez
à l’étape de suivi de créer un nouveau fichier `post-scan-summary.md` dans le répertoire d’analyse.
Si l’étape de suivi échoue, la CLI affiche un avertissement et conserve l’analyse terminée.
L’étape de suivi ne s’exécute pas après une annulation ni lorsque l’analyse atteint sa limite
de coût.

### Configurez les options de sortie et de politique

Utilisez ces options pour conserver les artefacts, préserver les résultats antérieurs ou créer un
résultat lisible par une machine.

| Argument                   | Description                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `--output-dir DIR`         | Écrivez les artefacts d’analyse dans un répertoire privé situé en dehors de l’arbre de travail Git parent. Par défaut, ils sont enregistrés dans l’état persistant de Codex Security. |
| `--archive-existing`       | Déplacez les résultats existants vers `DIR.previous-<timestamp>-<id>` et repartez avec un répertoire de sortie vide. Nécessite `--output-dir`.  |
| `--fail-on-severity LEVEL` | Renvoyez le code de sortie `1` lorsqu’une analyse terminée signale un constat dont la gravité atteint ou dépasse le seuil `critical`, `high`, `medium` ou `low`.                  |
| `--patch`                  | Corrigez et vérifiez les constats sélectionnés après une analyse complète.                                                                      |
| `--patch-severity LEVEL`   | Appliquez un correctif aux constats dont la gravité atteint ou dépasse `critical`, `high`, `medium` ou `low`. La valeur par défaut est `low`.                                        |
| `--create-pr`              | Créez un commit contenant les fichiers de correctifs vérifiés et ouvrez une pull request GitHub. Nécessite `--patch`.                                              |
| `--max-cost USD`           | Arrêtez une analyse lorsque le coût estimé du modèle dépasse le montant spécifié en USD.                                                  |
| `--dry-run`                | Vérifiez le dépôt, la cible, la base de connaissances, le répertoire de sortie et la configuration de Codex sans lancer d’analyse.             |
| `--headless`               | Affichez la progression en texte brut au lieu du tableau de bord interactif de l’analyse.                                                          |
| `--verbose`                | Affichez sur stderr les diagnostics expurgés concernant le cycle de vie, l’authentification, la progression et le coût.                                          |
| `--json`                   | Affichez le manifeste, les constats, la couverture, les chemins et les métadonnées des tours dans un document JSON unique.                                           |
| `--format FORMAT`          | Affichez le résultat complet de l’analyse au format `toon`, `json`, `yaml` ou `jsonl`.                                                        |
| `--full-output`            | Affichez le résultat complet dans le format de sortie structurée par défaut.                                                        |

La limite de coût est une estimation, et non un plafond de dépenses strict. Les requêtes déjà en
cours peuvent se terminer légèrement au-dessus de cette limite. Si une analyse approfondie atteint la limite
après que Codex Security a agrégé les résultats des workers ayant terminé, la CLI scelle les
résultats disponibles, marque la couverture comme `partial` et renvoie le code de sortie `2`.
Dans le cas contraire, elle renvoie `2` et laisse sur disque toute sortie partielle disponible.

Si vous omettez `--output-dir`, les résultats sont conservés dans
`$CODEX_HOME/state/plugins/codex-security/scans/<repository>`. Par défaut, `CODEX_HOME`
vaut `~/.codex`. Définissez `CODEX_SECURITY_STATE_DIR` afin de conserver plutôt les résultats dans
`$CODEX_SECURITY_STATE_DIR/scans/<repository>`. Ces répertoires peuvent
contenir des extraits de code source et des détails sur les vulnérabilités ; gérez donc leurs autorisations
et leur conservation en conséquence.

L’environnement de travail conserve l’historique des analyses dans
`$CODEX_HOME/state/plugins/codex-security/workbench.sqlite3`. Définir
`CODEX_SECURITY_STATE_DIR` déplace également la base de données de l’environnement de travail.

Le répertoire de sortie doit se trouver en dehors du répertoire analysé et de tout
arbre de travail Git parent. Une analyse peut remplacer un répertoire de résultats existant avec
`--archive-existing`.

Pour conserver les résultats antérieurs avant de réutiliser un répertoire de sortie :

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --archive-existing

Par défaut, les analyses produisent uniquement un rapport. Ajoutez `--fail-on-severity` pour évaluer une
politique de gravité dans la CI :

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --json \
  --fail-on-severity high \
  > /path/outside/repository/codex-security.json

Une exécution à blanc vérifie les entrées locales, notamment les documents de la base de connaissances, sans
charger les identifiants, lancer Codex ni vérifier l’interpréteur Python du
plugin :

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --dry-run

### Configurez l’environnement d’exécution

Utilisez les options d’exécution lorsque vous devez spécifier explicitement un modèle, un interpréteur, un plugin ou
une valeur de configuration de Codex.

| Argument                                                  | Description                                                                                              |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `--auth {auto,chatgpt,api-key}`                           | Sélectionnez les identifiants d’authentification utilisés pour l’analyse. La valeur par défaut est `auto`.                                                      |
| `--provider {openai,openrouter,fireworks,amazon-bedrock}` | Sélectionnez le fournisseur d’inférence. La valeur par défaut est `openai`.                                                  |
| `--model MODEL`                                           | Sélectionnez le modèle. La valeur par défaut est `gpt-5.6-sol`. Une sélection explicite est obligatoire pour OpenRouter, Fireworks et Amazon Bedrock.  |
| `--effort {minimal,low,medium,high,xhigh,max}`            | Sélectionnez le niveau d’effort de raisonnement du modèle. La valeur par défaut est `xhigh`.                                             |
| `--plugin-path PATH`                                      | Utilisez un répertoire ou une archive ZIP du Plugin Codex Security pour remplacer le plugin intégré.                             |
| `--python PATH`                                           | Sélectionnez l’interpréteur Python pour l’environnement d’exécution du plugin.                                                    |
| `--codex KEY=VALUE`                                       | Remplacez une valeur isolée de la configuration Codex. Ces valeurs suivent la syntaxe TOML. Répétez l’option pour ajouter d’autres valeurs. |

Pour sélectionner un autre modèle et un autre niveau d’effort de raisonnement sans écrire de TOML :

```bash
npx @openai/codex-security scan . --model gpt-5.6-terra --effort high

Placez entre guillemets les valeurs de type chaîne transmises via `--codex` afin que l’analyseur TOML reçoive une
chaîne :

```bash
npx @openai/codex-security scan . --codex 'model="gpt-5.6-terra"'

## `codex-security install-hook`

Installez un contrôle de sécurité Git pre-commit pour le dépôt actuel :

```bash
npx @openai/codex-security install-hook

Le contrôle analyse les modifications indexées et non indexées avant chaque commit et bloque
le commit en cas de constat de gravité élevée ou d’erreur d’analyse. Il respecte `core.hooksPath` et ne
remplace pas un script pre-commit existant. Définissez un autre seuil de gravité
si nécessaire :

```bash
npx @openai/codex-security install-hook . --fail-on-severity medium

## `codex-security bulk-scan`

Découvrez et analysez des dépôts GitHub, ou lancez une analyse pouvant être reprise à partir d’un
fichier CSV de dépôts :

Pour consulter un guide complet sur la découverte de dépôts GitHub, les inventaires CSV, les résultats de campagne
et les analyses conteneurisées, consultez [Lancez des analyses de sécurité
en masse](/fr-FR/codex/security/cli/bulk-scans).

```text
usage: codex-security bulk-scan [input] [--output-dir DIR]
                                [--workers N] [--mode {standard,deep}]
                                [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                                [--model MODEL]
                                [--effort {minimal,low,medium,high,xhigh,max}]
                                [--knowledge-base PATH]
                                [--scan-prompt-file FILE]
                                [--post-scan-prompt-file FILE]
                                [--max-attempts N] [--plugin-path PATH]
                                [--python PATH] [--codex KEY=VALUE]

Exécutez `npx @openai/codex-security bulk-scan` sans arguments pour sélectionner
des dépôts de manière interactive. Cette procédure nécessite une connexion à GitHub CLI.

Pour choisir un modèle et un effort de raisonnement lors de la découverte interactive :

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

Pour utiliser une liste de dépôts préparée, fournissez un fichier CSV et `--output-dir` :

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Le fichier CSV doit comporter les colonnes `id`, `repository` et `revision`. Les révisions doivent être
des hachages de commit complets. Les colonnes facultatives `scope`, `mode` et `prompt` permettent de configurer
chaque dépôt :

```csv
id,repository,revision,scope,mode,prompt
service,https://github.com/example/service.git,0123456789abcdef0123456789abcdef01234567,src,standard,Review authorization boundaries.

Utilisez `--knowledge-base PATH` pour partager des documents de sécurité entre tous les
dépôts. Utilisez `--scan-prompt-file FILE` pour ajouter des instructions d’analyse communes ; la
colonne `prompt` du fichier CSV ajoute des instructions propres à chaque dépôt après ce
prompt commun. `--post-scan-prompt-file FILE` exécute des instructions de suivi après chaque
analyse, y compris celles dont la couverture est incomplète ou qui comportent des erreurs. Ces instructions ne s’exécutent pas après
une annulation ni lorsqu’une analyse atteint sa limite de coût.

`--workers` limite le nombre d’analyses simultanées de dépôts et sa valeur par défaut est `4`. La valeur par défaut de `--mode`
est `standard`, et celle de `--max-attempts` est `1`. Définissez
`--max-attempts` pour relancer l’opération en cas d’erreur liée au dépôt ou à l’analyse. Les analyses terminées dont la
couverture est incomplète ne sont pas relancées. Leurs résultats restent disponibles et la
commande renvoie le code de sortie `2`.

Réexécutez la même commande pour reprendre à partir d’un répertoire de sortie existant. La CLI
ignore les analyses terminées, y compris celles dont la couverture est incomplète.

Pour les campagnes conteneurisées, consultez [Lancez des analyses en masse dans
Docker](/fr-FR/codex/security/cli/bulk-scans#run-bulk-scans-in-docker).

## `codex-security scans`

### Rechercher des analyses enregistrées

Répertoriez les analyses enregistrées pour le répertoire actuel :

```bash
npx @openai/codex-security scans

Répertoriez les analyses d’un autre dépôt :

```bash
npx @openai/codex-security scans list /path/to/repository

Recherchez les analyses stockées dans un répertoire de sortie spécifique :

```bash
npx @openai/codex-security scans list --scan-root /path/outside/repository/results

### Inspecter ou relancer une analyse

Affichez les résultats et la configuration d’une analyse enregistrée :

```bash
npx @openai/codex-security scans show SCAN_ID

Ajoutez `--show-linked-findings` pour inclure les liens vers les constats issus d’analyses antérieures.

Relancez l’analyse sur la copie de travail actuelle avec sa configuration d’origine :

```bash
npx @openai/codex-security scans rerun SCAN_ID

La relance nécessite la version du plugin enregistrée lors de l’analyse initiale. Si la
version installée diffère, la commande s’arrête au lieu de s’exécuter avec un
plugin différent.

### Inspecter les journaux d’analyse enregistrés

Consultez l’intégralité des événements de session enregistrés pour une analyse et ses processus de travail. Ces journaux
ne sont pas expurgés et peuvent contenir du code source ou des identifiants d’authentification ; examinez-les
avant de les partager :

```bash
npx @openai/codex-security scans logs SCAN_ID

Ajoutez `--json` pour obtenir un résultat lisible par une machine contenant l’ensemble des informations.

### Mettre en correspondance et comparer les constats

Comparez deux analyses pour identifier les constats nouveaux, persistants, rouverts, résolus ou de statut
inconnu :

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

La comparaison met automatiquement en correspondance les constats qui ont la même cause racine
et réutilise les correspondances enregistrées. Pour enregistrer explicitement les correspondances, utilisez `scans match` :

```bash
npx @openai/codex-security scans match PREVIOUS_SCAN_ID CURRENT_SCAN_ID

Un constat est de statut inconnu lorsque l’analyse ultérieure a une couverture incomplète ou ne
couvre pas l’emplacement d’origine du constat. Ajoutez `--force` à `match` si vous devez
recalculer une correspondance existante.

Pour mettre en correspondance toutes les analyses terminées du dépôt actuel, y compris celles provenant
d’autres copies de travail :

```bash
npx @openai/codex-security scans match --all

Les résultats d’analyse peuvent varier même lorsque vous réutilisez la même configuration. La mise en correspondance et
la comparaison permettent de suivre les changements ; elles ne rendent pas les résultats déterministes et ne prouvent pas qu’une
vulnérabilité a disparu. Utilisez `validate` pour revérifier un constat critique pour la sécurité
dans le code actuel.

## `codex-security findings`

Répertoriez les constats ouverts dans l’ensemble des analyses du dépôt actuel :

```bash
npx @openai/codex-security findings list

Indiquez le chemin d’un dépôt pour inspecter une autre copie de travail :

```bash
npx @openai/codex-security findings list /path/to/repository

Ajoutez `--json` pour obtenir une sortie structurée. La liste identifie les constats observés lors de la
dernière analyse et les constats antérieurs qui n’ont pas été confirmés par celle-ci.

Notez que les constats antérieurs restent ouverts tant qu’ils ne sont pas résolus ou écartés (leur absence
dans la dernière analyse ne prouve pas que le problème a été corrigé).

Pour enregistrer un constat examiné comme faux positif :

```text
usage: codex-security findings false-positive OCCURRENCE_ID
                       --reason REASON

Inspectez l’analyse enregistrée pour identifier l’occurrence du constat :

```bash
npx @openai/codex-security scans show SCAN_ID

Consignez une explication précise du faux positif :

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

Le motif ne doit pas être vide. Codex Security enregistre la décision pour le
dépôt et l’utilise comme contexte lors des analyses suivantes. Chaque analyse revérifie indépendamment
le code source actuel, les contrôles et l’accessibilité de la vulnérabilité. Une décision antérieure
ne désactive aucune règle, aucun chemin ni aucune classe de vulnérabilités.

## `codex-security export`

Exportez les résultats d’une analyse terminée et scellée au format CSV, JSON ou SARIF. L’exportation valide les
artefacts de l’analyse avant d’écrire la sortie, sans modifier l’environnement d’exécution Codex ni les
identifiants d’authentification.

```text
usage: codex-security export [--export-format {csv,json,sarif}]
                             [--output FILE|-] [--source-root PATH]
                             [--python PATH] scan_dir

`scan_dir` est le répertoire de l’analyse terminée.

| Argument                           | Description                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| `--export-format {csv,json,sarif}` | Sélectionnez le format d’exportation. La valeur par défaut est `sarif`.                                           |
| `--output FILE\|-`                 | Écrivez le contenu au format sélectionné dans un fichier ou sur stdout. Par défaut, il est écrit dans un fichier du répertoire actuel. |
| `--source-root PATH`               | Ajoutez à SARIF des empreintes de lignes de code source à l’aide d’une copie de travail du dépôt.                          |
| `--python PATH`                    | Sélectionnez l’interpréteur Python pour l’outil d’exportation fourni.                                     |

`--source-root` fonctionne uniquement avec `--export-format sarif`. JSON préserve
le document scellé contenant les constats. Le format CSV contient des colonnes portables décrivant les constats et
n’inclut pas l’état de triage de l’espace de travail local.

Sans `--output`, la CLI écrit SARIF dans `results.sarif`, JSON dans
`findings.json` et CSV dans `findings.csv`, dans le répertoire de travail actuel.
Les exportations peuvent contenir des extraits de code source et des détails sur les vulnérabilités. Exécutez la commande
hors du dépôt ou utilisez `--output` avec un chemin privé situé hors de la
copie de travail analysée.

Écrivez la sortie SARIF dans un fichier :

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root /path/to/repository \
  --output /path/outside/repository/exports/results.sarif

Écrivez la sortie SARIF sur stdout :

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root . \
  --output -

Exportez les constats au format JSON :

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format json \
  --output /path/outside/repository/exports/findings.json

Exportez les constats au format CSV :

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format csv \
  --output /path/outside/repository/exports/findings.csv

## `codex-security publish scan`

Publiez sur Linear tous les constats issus d’une analyse terminée :

```text
usage: codex-security publish scan [SCAN_DIR] --to linear
                                   [--linear-team TEAM_ID]
                                   [--project PROJECT_ID]
                                   [--linear-api-key KEY]
                                   [--linear-assignee EMAIL_OR_USER_ID]
                                   [--dry-run] [--json]

`SCAN_DIR` doit contenir une analyse terminée et scellée. Dans un terminal
interactif, omettez cet argument pour sélectionner une analyse terminée dans l’historique local des analyses. La création de tickets
nécessite également que l’analyse et ses constats figurent dans cet historique. Une exécution
à blanc valide les artefacts scellés sans effectuer cette vérification de persistance.

| Argument                             | Description                                                                                                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--to linear`                        | Publiez sur Linear. Cet argument est obligatoire.                                                                                                                    |
| `--linear-team TEAM_ID`              | Sélectionnez l’équipe Linear. Si cet argument est omis, la valeur de `CODEX_SECURITY_LINEAR_TEAM` est utilisée ; l’un des deux est obligatoire.                                                                 |
| `--project PROJECT_ID`               | Sélectionnez un projet Linear. Si cet argument est omis, la valeur de `CODEX_SECURITY_LINEAR_PROJECT` est utilisée. Si aucun des deux n’est défini, les tickets sont créés directement dans l’équipe.                          |
| `--linear-api-key KEY`               | Utilisez une clé API personnelle Linear pour publier directement. Si cet argument est omis, la valeur de `CODEX_SECURITY_LINEAR_API_KEY` est utilisée.                                                         |
| `--linear-assignee EMAIL_OR_USER_ID` | Attribuez les tickets créés à l’aide d’une adresse e-mail ou d’un identifiant d’utilisateur Linear. Cette option nécessite `--linear-api-key` ou `CODEX_SECURITY_LINEAR_API_KEY`. Si elle est omise, les tickets ne sont pas attribués. |
| `--dry-run`                          | Préparez les charges utiles des tickets sans démarrer Codex ni contacter Linear, sans créer de tickets et sans enregistrer l’état de publication.                                                 |
| `--json`                             | Écrivez les résultats structurés de publication sur stdout. La progression reste sur stderr.                                                                                      |

  Les descriptions des tickets Linear et la sortie d’une exécution à blanc peuvent contenir des extraits de code source
et des détails sur les vulnérabilités. Publiez uniquement dans des équipes ou des projets Linear
autorisés, et considérez les sorties enregistrées comme sensibles.

Chaque exécution qui n’est pas à blanc tente de créer un nouveau ticket pour chaque constat.
Une nouvelle publication de la même analyse ne recherche pas de correspondance avec les tickets existants, ne les met pas à jour et ne les réutilise pas.
Si la publication de certains constats échoue, la commande conserve les tickets créés avec succès et
renvoie le code de sortie `2`.
Avec `--json`, examinez les résultats `created` et `failed` avant toute nouvelle tentative afin
d’éviter les doublons.

Prévisualisez les charges utiles des tickets avant leur publication :

```bash
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --dry-run \
  --json

### Publication avec l’application Linear connectée

Sans clé API Linear, la commande démarre Codex en utilisant votre configuration
existante et l’application Linear connectée. Connectez-vous et associez Linear à votre
compte Codex avant de publier :

```bash
npx @openai/codex-security login
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --project PROJECT_ID

### Publication avec une clé API Linear

L’utilisation de `--linear-api-key` ou de `CODEX_SECURITY_LINEAR_API_KEY` permet de publier
directement via l’API Linear, sans démarrer Codex. Lors d’une publication directe,
les tickets ne sont pas attribués, sauf si vous désignez un responsable :

```bash

npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --linear-assignee teammate@example.com

Les valeurs passées en ligne de commande prévalent sur les variables d’environnement correspondantes. Pour les clés
API, privilégiez `CODEX_SECURITY_LINEAR_API_KEY` plutôt que `--linear-api-key`, car les
arguments de ligne de commande peuvent apparaître dans l’historique du shell et dans la liste des processus.

## `codex-security validate` et `codex-security patch`

Vérifiez si un constat potentiel est valide :

```bash
npx @openai/codex-security validate findings.json \
  "Possible SQL injection in src/query.ts:42"

Générez un correctif à l’aide du skill de remédiation intégré :

```bash
npx @openai/codex-security patch findings.json \
  "Missing authorization check in src/routes.ts:18"

Chaque argument positionnel accepte du texte littéral ou un chemin de fichier. Ces entrées utilisent
le répertoire courant. Utilisez `validate` pour revérifier un constat après l’application d’un correctif ou lorsqu’une
analyse ultérieure ne le signale plus. Comparer des analyses ne suffit pas à prouver qu’un correctif
a fonctionné.

Utilisez `--effort` pour sélectionner le niveau d’effort de raisonnement avec l’une ou l’autre commande :

```bash
npx @openai/codex-security validate "Possible SQL injection" --effort high

### Correction des constats après une analyse

Utilisez `scan --patch` pour corriger les constats après une analyse complète. Cette fonctionnalité nécessite
`@openai/codex-security` en version 0.1.15 ou ultérieure. Le seuil de gravité par défaut est
`low`. Cette commande sélectionne les constats de gravité élevée ou critique :

```bash
npx @openai/codex-security scan . --patch --patch-severity high --json

Les constats vérifiés ainsi que ceux qui sont déjà corrigés ne déclenchent pas `--fail-on-severity`.

### Correction des constats enregistrés

Indiquez l’identifiant d’un constat ou d’une occurrence pour appliquer un correctif dans son dépôt d’origine, ou sélectionnez
des constats issus d’une analyse enregistrée :

```bash
npx @openai/codex-security patch OCCURRENCE_ID
npx @openai/codex-security patch --scan SCAN_ID --severity high --json
npx @openai/codex-security patch --scan latest --severity medium

`--scan latest` sélectionne la dernière analyse terminée pour le dépôt courant.
Les commandes relatives aux constats enregistrés prennent en charge `--json` ; ce n’est pas le cas des entrées sous forme de texte littéral ou de fichier.

Ajoutez `--create-pr` pour créer un commit contenant uniquement les fichiers de correctif vérifiés et ouvrir une pull request
avec la CLI GitHub :

```bash
npx @openai/codex-security patch --scan SCAN_ID --severity high --create-pr

En cas d’échec du push ou de la pull request, exécutez la commande affichée `patch --resume-pr BRANCH`
depuis le même dépôt pour réessayer.

### Correction des tickets Linear

Définissez `CODEX_SECURITY_LINEAR_API_KEY` ou `LINEAR_API_KEY` pour utiliser une clé API personnelle,
ou `LINEAR_ACCESS_TOKEN` pour utiliser un token OAuth. Privilégiez une variable d’environnement plutôt que
`--linear-api-key KEY` afin d’éviter que la clé figure dans l’historique du shell.

Importez un ticket à l’aide de son identifiant ou de son URL. Répétez `--linear-issue` pour sélectionner plusieurs
tickets :

```bash
npx @openai/codex-security patch --linear-issue SEC-123 --linear-issue SEC-124

Utilisez `--linear-project` pour sélectionner les tickets ouverts d’un projet. Ajoutez `--linear-filter`
pour affiner la sélection :

```bash
npx @openai/codex-security patch --linear-project "Security backlog" \
  --linear-filter '{"labels":{"name":{"eq":"security"}}}'

La CLI exclut les tickets terminés et annulés, sauf si le filtre définit `state`.
Elle ne modifie pas les tickets Linear.

## `codex-security login`, `logout` et `info`

Connectez-vous en mode interactif :

```bash
npx @openai/codex-security login

Utilisez l’authentification par appareil sur une machine distante ou sans interface graphique :

```bash
npx @openai/codex-security login --device-auth

Vérifiez la connexion actuelle :

```bash
npx @openai/codex-security login status

Supprimez la connexion enregistrée :

```bash
npx @openai/codex-security logout

Enregistrez une clé API en la transmettant via stdin :

```bash
printenv OPENAI_API_KEY | npx @openai/codex-security login --with-api-key

Enregistrez un token d’accès d’entreprise :

```bash
printenv CODEX_ACCESS_TOKEN | npx @openai/codex-security login --with-access-token

Inspectez les métadonnées en lecture seule du SDK et du plugin intégré :

```bash
npx @openai/codex-security info --json

Lorsque vous exposez la CLI comme serveur MCP, `info` est la seule commande disponible.
Les analyses, les exportations, la publication, la connexion, la validation et l’application de correctifs restent accessibles uniquement via la CLI.

## Lecture de la sortie d’analyse

Par défaut, les analyses envoient la progression, les résumés de fin d’analyse et les erreurs sur stderr,
sans écrire le résultat complet de l’analyse sur stdout. Utilisez `--json`,
`--format` ou `--full-output` pour envoyer des résultats d’analyse structurés sur stdout.

Les terminaux interactifs affichent un tableau de bord en direct indiquant la phase d’analyse en cours,
les fichiers examinés, l’activité, la consommation de tokens et le coût estimé. En CI et lorsque la
sortie est redirigée, la progression s’affiche en texte brut. Ajoutez `--headless` pour afficher la progression en
texte brut dans un terminal interactif :

```bash
npx @openai/codex-security scan . --headless

Le tableau de bord affiche également en direct les détails de la session. Ces détails ne sont pas expurgés et peuvent
contenir du code source ou des identifiants. Examinez-les avant de les partager.

### Diagnostics détaillés

Ajoutez `--verbose` pour afficher sur stderr des diagnostics expurgés relatifs au cycle de vie, à l’authentification, à la progression et aux
coûts :

```bash
npx @openai/codex-security scan . --verbose

Définissez `CODEX_SECURITY_LOG_LEVEL=debug` pour activer les mêmes diagnostics sans utiliser
l’option. `LOG_LEVEL=debug` active également les diagnostics lorsque
`CODEX_SECURITY_LOG_LEVEL` n’est pas défini.

### Résumé de fin d’analyse

Une analyse terminée écrit sur stderr le nombre de constats ouverts dans le dépôt, leur répartition par gravité,
la couverture, le temps écoulé, le chemin du rapport et le répertoire des résultats. Elle indique également
la consommation de tokens et le coût estimé lorsque ces informations sont disponibles :

```text
  REPORT    /path/to/scan/report.md

  FINDINGS  4 (3 confirmed this scan; 1 previously found; 1 critical, 2 high, 1 informational)
  COVERAGE  complete
  ELAPSED   1s
  TOKENS    1,250 input, 200 cached, 30 output
  RESULTS   /path/to/scan

Les constats informatifs sont inclus dans le total du résumé. Les politiques de gravité
n’évaluent que les constats de niveau `critical`, `high`, `medium` et `low` issus de l’analyse
en cours, et non les constats antérieurs inclus dans le total du dépôt.

### Sortie JSON

`scan --json` écrit un unique document JSON complet sur stdout. Sa structure de premier niveau
est la suivante :

```text
manifest
repositoryFindings
findings
coverage
scanDir
threadId
reportPath
artifactsDir
sarifPath
cost
turn
  id
  status
  durationMs
  finalResponse
  usage

Lorsque vous [appliquez des correctifs](#patch-findings-after-a-scan), la sortie JSON inclut également les résultats des correctifs
et toute pull request créée.

La progression, les résumés de fin d’analyse, les avis d’archivage et les erreurs restent sur stderr.
Une analyse terminée affiche toujours le résultat JSON complet lorsqu’une politique de gravité
renvoie le code de sortie `1` ou qu’une couverture incomplète renvoie le code de sortie `2`.

  `codex-security scan --json` émet un document JSON unique. `codex exec --json`
  émet un flux d’événements JSON Lines. Utilisez le format de sortie adapté à la
  commande que vous exécutez.

## Artefacts d’analyse

Une analyse terminée regroupe son rapport lisible et ses artefacts structurés :

```text
<scan-directory>/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

Les fichiers structurés remplissent différentes fonctions :

| Fichier                    | Contenu                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `scan-manifest.json`    | Identité, état, cible, périmètre et producteur de l’analyse, ainsi que les enregistrements des artefacts scellés.                                                    |
| `findings.json`         | Identifiants des constats, gravité, niveau de confiance, taxonomie, emplacements, preuves, validation, flux de données, atteignabilité et remédiation. |
| `coverage.json`         | Surfaces examinées, exclusions, travaux reportés, questions en suspens et exhaustivité de la couverture.                                        |
| `report.md`             | Rapport d’analyse lisible.                                                                                                           |
| `artifacts/`            | Artefacts complémentaires de l’analyse.                                                                                                      |
| `exports/results.sarif` | Fichier SARIF généré pendant l’analyse, le cas échéant.                                                                                  |

L’exhaustivité de la couverture peut prendre trois valeurs :

- `complete` : l’analyse indique une couverture complète du périmètre sélectionné.
- `partial` : l’analyse indique que certains travaux sont reportés ou que la couverture présente d’autres limites.
- `unknown` : l’analyse indique que l’exhaustivité de la couverture est inconnue.

Examinez les surfaces dont l’examen a été reporté, les exclusions explicites et les questions en suspens avant d’utiliser
la couverture pour étayer une décision en matière de sécurité.

## Codes de sortie et signaux

La CLI utilise les codes de sortie suivants :

| Code de sortie  | Condition                                                                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`   | Une analyse s’est terminée avec une couverture complète et a respecté sa politique de gravité, une analyse groupée ou une publication s’est terminée sans échec, ou une autre commande a réussi.                  |
| `1`   | Une analyse terminée fait état d’un constat dont la gravité atteint ou dépasse le niveau configuré.                                                                                                       |
| `2`   | La CLI a détecté une erreur d’entrée, d’exécution ou d’exportation, une analyse présente une couverture incomplète, une analyse groupée comporte des dépôts en erreur, ou la publication d’un ou plusieurs constats a échoué. |
| `130` | Ctrl-C a interrompu une analyse ou une publication.                                                                                                                                     |
| `143` | SIGTERM a mis fin à une analyse ou à une publication.                                                                                                                                     |

Toute analyse dont la couverture est `partial` ou `unknown` renvoie `2`, même sans
politique de gravité. Lorsque vous demandez une sortie structurée, les analyses terminées et les
publications partielles écrivent tout de même les résultats disponibles sur stdout. La CLI
affiche l’emplacement de toute sortie partielle après une interruption ou une erreur
d’exécution.

## Autorisations des analyses locales

Les analyses effectuées avec la CLI et le SDK s’exécutent avec les autorisations de votre système d’exploitation local. Chaque analyse
utilise le profil de système de fichiers `codex_security_scan` et définit `approvalPolicy` sur
`"never"`. Ce profil autorise la lecture du système de fichiers local et l’écriture dans les
racines des espaces de travail ainsi que dans le répertoire d’état sélectionné pour l’analyse. Les analyses ne s’arrêtent pas pour
demander une approbation interactive.

Les paramètres fournis via l’option `--codex` de la CLI ou `codexOverrides` du SDK, notamment
`approval_policy`, `sandbox_mode` et les autorisations du système de fichiers, ne peuvent ni remplacer
ni restreindre ces contrôles d’analyse. Les restrictions liées à l’hôte et au réseau continuent de s’appliquer.

Les processus d’analyse et de l’interface de travail peuvent hériter de votre environnement, notamment des
tokens API sans rapport avec l’analyse et des identifiants cloud. Analysez uniquement les dépôts auxquels vous faites
confiance et que vous êtes autorisé à évaluer, et fournissez uniquement les identifiants nécessaires à l’analyse.

## Authentification et prérequis

Définissez `OPENAI_API_KEY` ou `CODEX_API_KEY`, connectez-vous avec
`npx @openai/codex-security login`, ou utilisez une connexion Codex existante stockée dans un
fichier. Pour OpenRouter ou Fireworks, définissez la clé API du fournisseur et sélectionnez un
modèle. Pour Amazon Bedrock, utilisez plutôt une clé API Bedrock ou la chaîne standard
d’identifiants AWS.

Pour choisir les identifiants, consultez [Sélection de l’authentification
de l’analyse](#select-scan-authentication).

En CI, limitez la portée de la clé API à l’étape d’analyse et utilisez un workflow de confiance.

La CLI nécessite Node.js 22 (22.13.0 ou version ultérieure), 24 ou 26. Les analyses, les analyses groupées,
les exportations, l’historique des analyses et les constats enregistrés nécessitent également Python 3.10 ou une version ultérieure.
Python 3.10 nécessite aussi `tomli`. Utilisez `--python` avec `scan`, `bulk-scan` ou
`export`, ou définissez `PYTHON` pour toute commande reposant sur Python.

Poursuivez avec le [guide de démarrage rapide de la CLI](/fr-FR/codex/security/cli), le [guide des analyses
groupées](/fr-FR/codex/security/cli/bulk-scans), la [FAQ de la CLI](/fr-FR/codex/security/cli/faq), le [guide de la
CI](/fr-FR/codex/security/cli/ci) ou le [guide du SDK TypeScript](/fr-FR/codex/security/sdk).
