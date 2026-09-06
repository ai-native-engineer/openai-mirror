<!-- source: https://learn.chatgpt.com/fr-FR/docs/hooks -->

Les hooks sont un mécanisme d’extension de Codex. Ils permettent d’exécuter des scripts ou des outils MCP
pendant la boucle agentique, notamment pour :

- Envoyer la discussion à un moteur personnalisé de journalisation ou d’analyse
- Analyser les prompts de votre équipe pour bloquer le collage accidentel de clés API
- Résumer les discussions pour créer automatiquement des mémoires persistantes
- Exécuter un contrôle de validation personnalisé à l’arrêt d’un tour de discussion pour faire respecter les normes
- Personnaliser la conception de prompts dans un répertoire donné

Points à retenir sur le comportement à l’exécution :

- Tous les hooks correspondants s’exécutent, même s’ils proviennent de plusieurs fichiers.
- Les hooks de commande correspondant au même événement sont lancés simultanément,
si bien qu’un hook ne peut pas empêcher le démarrage d’un autre hook correspondant.
- Les hooks non gérés doivent être examinés et déclarés fiables avant de pouvoir s’exécuter.

Les hooks s’exécutent à différents moments d’une conversation :

| Moment                              | Hooks                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Pendant un tour                     | `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `UserPromptSubmit`, `SubagentStop`, `Stop` |
| Lorsque vous interrompez un tour en cours | `Interrupt` (ne s’exécute pas pour les sous-agents)                                                                                   |
| Au démarrage d’une session ou d’un sous-agent | `SessionStart`, `SubagentStart`                                                                                           |
| À la fin du fil de discussion principal         | `SessionEnd` (ne s’exécute pas pour les sous-agents)                                                                                  |

## Où Codex recherche les hooks

Codex recherche les hooks au niveau des couches de configuration actives, sous l’une des formes suivantes :

- `hooks.json`
- tables `[hooks]` directement dans `config.toml`

Les plugins installés peuvent aussi inclure la configuration du cycle de vie dans leur manifeste
ou dans un fichier `hooks/hooks.json` par défaut. Consultez [Création de
plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) pour connaître les
règles de packaging des plugins.

En pratique, les quatre emplacements les plus utiles sont :

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

S’il existe plusieurs sources de hooks, Codex charge tous les hooks correspondants.
Les couches de configuration prioritaires ne remplacent pas les hooks des couches moins prioritaires.
Si une même couche contient à la fois `hooks.json` et des tables `[hooks]` intégrées, Codex
les fusionne et affiche un avertissement au démarrage. Utilisez de préférence une seule représentation par couche.

Codex peut aussi détecter les hooks fournis avec les plugins activés. Ces hooks
se chargent avec ceux des autres sources et suivent la même procédure d’examen et de déclaration de fiabilité
que les autres hooks non gérés.

Les hooks locaux au projet ne sont chargés que si la couche `.codex/` du projet est déclarée fiable. Dans
les projets non fiables, Codex charge tout de même les hooks utilisateur et système depuis leurs propres
couches de configuration actives.

## Examinez les hooks et déclarez-les fiables

Codex répertorie les hooks configurés avant de déterminer lesquels peuvent s’exécuter. Avant qu’un
hook non géré puisse s’exécuter, Codex exige que vous examiniez sa définition exacte et la déclariez fiable.
Codex associe ce statut de confiance au hachage actuel du hook : les hooks nouveaux ou modifiés
sont donc signalés comme devant être examinés et ignorés tant qu’ils ne sont pas déclarés fiables.

Utilisez `/hooks` dans la CLI pour inspecter les sources des hooks, examiner les hooks nouveaux ou modifiés,
les déclarer fiables ou désactiver individuellement des hooks non gérés. Si des hooks doivent être examinés au
démarrage, Codex affiche un avertissement qui vous invite à ouvrir `/hooks`.

Les hooks gérés provenant du système, d’une solution MDM, du cloud ou de `requirements.toml` sont signalés
comme gérés et déclarés fiables par la politique applicable. Ils ne peuvent pas être désactivés depuis l’interface utilisateur de gestion des hooks.

Pour une automatisation ponctuelle qui vérifie déjà les sources des hooks en dehors de Codex, passez
`--dangerously-bypass-hook-trust` pour exécuter les hooks activés sans exiger
de statut de confiance enregistré pour cette invocation.

## Structure de la configuration

Les hooks sont organisés en trois niveaux :

- Un événement de hook tel que `PreToolUse`, `PostToolUse`, `PreCompact`,
`SubagentStart` ou `Stop`
- Un groupe de critères de correspondance qui détermine dans quels cas cet événement est retenu
- Un ou plusieurs gestionnaires de hooks qui s’exécutent lorsque les critères du groupe sont satisfaits

```json
{
  "description": "Optional lifecycle hooks for this workspace.",
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes",
            "additionalContextLimit": 5000
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_end.py",
            "timeout": 3
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/permission_request.py\"",
            "statusMessage": "Checking approval request"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
            "statusMessage": "Reviewing Bash output"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit_data_flywheel.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}

Remarques :

- `description` est une métadonnée facultative à la racine d’un fichier `hooks.json`. Elle
  ne change pas les hooks qui s’exécutent.
- La valeur de `timeout` est exprimée en secondes.
- Si `timeout` est omis, Codex utilise un délai de `600` secondes pour la plupart des hooks.
  - `SessionEnd` et `Interrupt` utilisent par défaut un délai de `1` seconde et acceptent jusqu’à `3` secondes.
- `statusMessage` est facultatif.
- `additionalContextLimit` définit la quantité de texte dans `additionalContext` qu’un hook de commande peut
  envoyer au modèle avant que Codex enregistre le texte intégral sur le disque et envoie à la place un aperçu
  plus court. Consultez [Sortie volumineuse des hooks](#large-hook-output).
- Le paramètre facultatif `commandWindows` permet de remplacer la commande uniquement sur Windows. En TOML, utilisez
`command_windows` ou `commandWindows`.
- Définissez `async` sur `true` pour [exécuter un hook de commande en
  arrière-plan](#run-hooks-in-the-background).
- Les gestionnaires `command` et `mcp_tool` sont pris en charge. Les gestionnaires `prompt` et `agent`
  sont analysés, mais ignorés.
- Les commandes s’exécutent avec le `cwd` de la session comme répertoire de travail.
- Pour les hooks locaux au dépôt, résolvez de préférence les chemins à partir de la racine Git plutôt que d’utiliser un
  chemin relatif tel que `.codex/hooks/...`. Codex peut être lancé depuis un
  sous-répertoire ; un chemin basé sur la racine Git garantit un emplacement stable pour le hook.

Configuration TOML équivalente directement dans `config.toml` :

```toml
[[hooks.SessionStart]]
matcher = "^compact$"

[[hooks.SessionStart.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/session_start.py"'
additionalContextLimit = 5000

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
timeout = 30
statusMessage = "Reviewing Bash output"

## Hooks d’outils MCP

Un hook d’outil MCP permet à un événement du cycle de vie d’appeler un outil sur un serveur MCP déjà connecté.
Il envoie des arguments structurés directement à l’outil. La procédure d’examen et de déclaration de fiabilité
ainsi que le contrat de sortie sont les mêmes que pour un hook de commande.

### Configurez un hook d’outil MCP

Ce hook demande au serveur MCP `scanner` d’analyser chaque patch après que Codex a écrit ou
modifié des fichiers :

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "mcp_tool",
            "server": "scanner",
            "tool": "scan_patch",
            "input": { "patch": "${tool_input.command}" },
            "timeout": 30,
            "statusMessage": "Scanning edited files"
          }
        ]
      }
    ]
  }
}

| Champ           | Signification                                                          |
| --------------- | ---------------------------------------------------------------- |
| `type`          | La valeur doit être `mcp_tool`.                                              |
| `server`        | Nom obligatoire d’un serveur MCP déjà connecté.                |
| `tool`          | Nom obligatoire d’un outil exposé par ce serveur.                  |
| `input`         | Objet JSON facultatif contenant les modèles d’arguments. Valeur par défaut : `{}`.    |
| `timeout`       | Durée maximale d’exécution active en secondes, facultative. Valeur par défaut : `600`. |
| `statusMessage` | Message facultatif affiché pendant l’exécution du hook.                      |

### Expansion des arguments à partir de l’événement du hook

Utilisez `${field.nested}` pour lire un champ de l’événement du hook avec la notation pointée. Un paramètre de substitution
qui occupe toute une valeur conserve son type JSON. À l’intérieur d’une chaîne plus longue,
il est converti en texte. Codex effectue ces substitutions de manière récursive dans les objets et les tableaux.

Pour un événement contenant `{"tool_input":{"file_path":"src/main.rs","count":3}}`,
ce modèle d’arguments :

```json
{
  "path": "${tool_input.file_path}",
  "count": "${tool_input.count}",
  "message": "Scanning ${tool_input.file_path}"
}

devient :

```json
{
  "path": "src/main.rs",
  "count": 3,
  "message": "Scanning src/main.rs"
}

### Exécution et cycle de vie

- Les hooks utilisent une connexion MCP existante. Ils ne démarrent pas de serveur et ne rétablissent pas de connexion à un serveur.
- Un hook peut bloquer une opération lorsque l’outil renvoie une décision de blocage.
Les erreurs, les serveurs manquants et les outils indisponibles ne bloquent pas l’opération.
- Les hooks d’outils MCP s’exécutent de manière synchrone. Ils ne demandent pas d’approbation pour l’outil et ne déclenchent
pas d’autres hooks.
- Le délai d’expiration applicable est le plus court de ceux du hook et du serveur. Le temps passé à attendre une réponse à une
élicitation MCP n’entre pas dans le calcul de ce délai.
- Les hooks `SessionStart` peuvent s’exécuter avant qu’un serveur MCP soit prêt. Dans ce cas,
  ils ne bloquent pas la session.
- `SessionEnd` ne prend pas en charge les hooks d’outils MCP.

## Désactivez les hooks

Les hooks sont activés par défaut. Pour les désactiver dans `config.toml`, utilisez la configuration suivante :

```toml
[features]
hooks = false

Utilisez `hooks` comme clé de référence pour cette fonctionnalité. `codex_hooks` fonctionne encore en tant
qu’alias obsolète. Les administrateurs peuvent imposer la désactivation des hooks de la même manière dans
`requirements.toml`, avec `[features].hooks = false`.

## Hooks gérés définis dans `requirements.toml`

Les exigences gérées par l’entreprise peuvent aussi définir des hooks directement dans `[hooks]`.
Cela permet aux administrateurs d’imposer la configuration des hooks tout en
distribuant les scripts via MDM ou un autre système de gestion des appareils.
Pour imposer les hooks gérés même aux utilisateurs qui ont désactivé les hooks localement, fixez
`[features].hooks = true` dans `requirements.toml`, en plus de `[hooks]`. Pour ignorer les hooks
utilisateur, de projet, de session et de plugin tout en autorisant les hooks gérés par les
administrateurs, définissez `allow_managed_hooks_only = true`.

```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"

Remarques sur les hooks gérés :

- `managed_dir` est utilisé sur macOS et Linux.
- `windows_managed_dir` est utilisé sur Windows.
- Codex ne distribue pas les scripts de `managed_dir` ; les outils de votre entreprise
  doivent les installer et les mettre à jour séparément.
- Les commandes des hooks gérés devraient utiliser des chemins absolus vers des scripts situés dans le
répertoire géré défini dans la configuration.
- Avec `allow_managed_hooks_only = true`, Codex ignore les hooks utilisateur, de projet, de session et
  de plugin, mais charge toujours les hooks gérés définis dans `requirements.toml` et
  les autres couches de configuration gérées.

## Hooks fournis avec les plugins

Lorsqu’un plugin est activé, Codex peut charger ses hooks de cycle de vie
en plus des hooks utilisateur, de projet et gérés.

Par défaut, Codex recherche `hooks/hooks.json` dans le répertoire racine du plugin. Le manifeste d’un plugin
peut redéfinir ce comportement par défaut avec une entrée `hooks` dans
`.codex-plugin/plugin.json`. Cette entrée peut être un chemin préfixé par `./`, un
tableau de chemins préfixés par `./`, un objet de hooks défini directement dans le manifeste ou un tableau
de tels objets.

```json
{
  "name": "repo-policy",
  "hooks": "./hooks/hooks.json"
}

Les chemins des hooks indiqués dans le manifeste sont résolus par rapport à la racine du plugin et doivent rester
à l’intérieur de celle-ci. Si un manifeste définit `hooks`, Codex utilise ces entrées
à la place du fichier par défaut `hooks/hooks.json`.

Les commandes des hooks de plugin reçoivent les variables d’environnement suivantes :

- `PLUGIN_ROOT` est une extension propre à Codex qui pointe vers le répertoire racine
  du plugin installé.
- `PLUGIN_DATA` est une extension propre à Codex qui pointe vers le
  répertoire de données accessible en écriture du plugin.
- Codex définit aussi `CLAUDE_PLUGIN_ROOT` et `CLAUDE_PLUGIN_DATA` pour
  assurer la compatibilité avec les hooks de plugin existants.

Les hooks de plugin utilisent le même schéma d’événement que les autres hooks. L’installation ou l’activation d’un
plugin ne marque pas automatiquement ses hooks comme fiables ; Codex ignore les hooks fournis avec le plugin
jusqu’à ce que vous ayez examiné leur définition actuelle et l’ayez déclarée fiable.

## Motifs de correspondance

Le champ `matcher` est une chaîne contenant une expression régulière qui détermine quand les hooks se déclenchent. Utilisez `"*"`,
`""` ou omettez entièrement `matcher` pour sélectionner chaque occurrence d’un événement
pris en charge.

Seuls certains événements actuels de Codex prennent en compte `matcher` :

| Événement               | Ce que filtre `matcher` | Remarques                                                        |
| ------------------- | ---------------------- | ------------------------------------------------------------ |
| `PermissionRequest` | nom de l’outil              | Sont notamment pris en charge : `Bash`, `apply_patch`\* et les noms d’outils MCP |
| `PostToolUse`       | nom de l’outil              | Consultez la section [Prise en charge des outils](#tool-coverage)                          |
| `PostCompact`       | déclencheur du compactage     | Les valeurs possibles sont `manual` ou `auto`                                |
| `PreCompact`        | déclencheur du compactage     | Les valeurs possibles sont `manual` ou `auto`                                |
| `PreToolUse`        | nom de l’outil              | Consultez la section [Prise en charge des outils](#tool-coverage)                          |
| `SessionEnd`        | motif de fin             | Pour l’instant, uniquement `other`                                       |
| `SessionStart`      | origine du démarrage           | Les valeurs possibles sont `startup`, `resume`, `clear` et `compact`       |
| `SubagentStart`     | type de sous-agent          | Les valeurs dépendent du sous-agent qui démarre                    |
| `SubagentStop`      | type de sous-agent          | Les valeurs dépendent du sous-agent qui s’arrête                     |
| `UserPromptSubmit`  | non pris en charge          | Toute valeur configurée pour `matcher` est ignorée pour cet événement           |
| `Stop`              | non pris en charge          | Toute valeur configurée pour `matcher` est ignorée pour cet événement           |
| `Interrupt`         | non pris en charge          | Toute valeur configurée pour `matcher` est ignorée pour cet événement           |

\*Pour `apply_patch`, `matcher` peut également prendre les valeurs `Edit` ou `Write`.

Exemples :

- `Bash`
- `^apply_patch$`
- `Edit|Write`
- `mcp__filesystem__read_file`
- `mcp__filesystem__.*`
- `startup|resume|clear|compact`
- `manual|auto`

### Outils pris en charge

`PreToolUse` et `PostToolUse` ne se limitent pas à observer les appels shell et MCP. La plupart des
outils de type fonction locaux utilisent le même chemin d’exécution des hooks. Vous pouvez donc filtrer sur leur nom,
examiner leurs arguments JSON et, avec `PreToolUse`, bloquer ou réécrire l’appel.

| Chemin d’exécution de l’outil                         | `PreToolUse` | `PostToolUse` | Remarques                                                                                                                    |
| --------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Commandes shell                    | Oui          | Oui           | Filtrez sur `Bash`.                                                                                                         |
| Exécution unifiée (`exec_command`)     | Oui          | Oui           | Filtrez sur `Bash`. Une interrogation ultérieure via `write_stdin` peut transmettre l’événement `PostToolUse` de la commande initiale lorsque celle-ci se termine. |
| `apply_patch`                     | Oui          | Oui           | Filtrez sur `apply_patch`, `Edit` ou `Write`.                                                                              |
| Outils MCP                         | Oui          | Oui           | Filtrez sur le nom de l’outil MCP, par exemple `mcp__filesystem__read_file`.                                                           |
| Autres outils de type fonction locaux        | Oui          | Oui           | Filtrez sur le nom de l’outil de type fonction, par exemple `update_plan`. `spawn_agent` correspond aussi à `Agent`.                                 |
| Outils hébergés, comme `WebSearch` | Non           | Non            | Ces outils n’utilisent pas le chemin d’exécution des hooks des outils de type fonction locaux.                                                                       |

`write_stdin` assure le transport pour une session unified-exec existante. Il ne réexécute pas
`PreToolUse` lorsqu’il envoie des données d’entrée ou interroge une commande déjà passée par
`PreToolUse`.

Certains chemins d’exécution d’outils spécialisés peuvent ne pas utiliser le chemin d’exécution des hooks par défaut. Considérez les
hooks d’outils comme un garde-fou utile, et non comme un mécanisme de contrôle exhaustif.

## Champs d’entrée communs

Chaque hook de commande reçoit un objet JSON sur `stdin`.

Voici les champs communs que vous utiliserez généralement :

| Champ             | Type             | Signification                                                             |
| ----------------- | ---------------- | ------------------------------------------------------------------- |
| `session_id`      | `string`         | Identifiant de la session Codex actuelle. Les hooks de sous-agents utilisent l’identifiant de la session parente. |
| `transcript_path` | `string \| null` | Chemin du fichier de transcription de la session, le cas échéant                         |
| `cwd`             | `string`         | Répertoire de travail de la session                                   |
| `hook_event_name` | `string`         | Nom de l’événement de hook en cours                                             |
| `model`           | `string`         | Extension propre à Codex. Slug du modèle actif                         |

Les hooks associés à un tour indiquent `turn_id` comme extension propre à Codex dans leurs
tableaux spécifiques à chaque événement.

`SessionStart`, `PreToolUse`, `PermissionRequest`, `PostToolUse`,
`UserPromptSubmit`, `SubagentStart`, `SubagentStop`, `Stop` et `Interrupt` incluent également
`permission_mode`, qui indique le mode d’autorisation actuel : `default`,
`acceptEdits`, `plan`, `dontAsk` ou `bypassPermissions`.

`transcript_path` facilite l’accès à une transcription de la discussion, mais le
format de cette transcription n’est pas une interface stable pour les hooks et peut évoluer au fil du temps.

Si vous avez besoin du format d’échange complet, consultez la section [Schémas](#schemas).

## Champs de sortie communs

`SessionStart`, `PreCompact`, `PostCompact`, `UserPromptSubmit`,
`SubagentStop` et `Stop` prennent en charge ces champs JSON communs. `SubagentStart`
accepte la même structure pour `systemMessage` et le contexte propre au hook, mais
`continue: false` n’arrête pas le sous-agent :

```json
{
  "continue": true,
  "stopReason": "optional",
  "systemMessage": "optional",
  "suppressOutput": false
}

| Champ            | Effet                                          |
| ---------------- | ----------------------------------------------- |
| `continue`       | Si la valeur est `false`, marque l’exécution de ce hook comme arrêtée      |
| `stopReason`     | Enregistré comme motif de l’arrêt             |
| `systemMessage`  | Affiché comme avertissement dans l’interface utilisateur ou le flux d’événements |
| `suppressOutput` | Reconnu par l’analyseur, mais pas encore implémenté            |

Une fin d’exécution avec le code `0` sans aucune sortie est considérée comme une réussite, et Codex continue.

`PreToolUse` et `PermissionRequest` prennent en charge `systemMessage`, mais `continue`,
`stopReason` et `suppressOutput` ne sont actuellement pas pris en charge pour ces événements.
Si un hook `PreToolUse` renvoie l’un de ces champs non pris en charge, Codex marque
l’exécution de ce hook comme ayant échoué, signale l’erreur et poursuit l’appel d’outil.

`PostToolUse` prend en charge `systemMessage`, `continue: false` et `stopReason`.
`suppressOutput` est reconnu par l’analyseur, mais n’est actuellement pas pris en charge pour cet événement.

### Sorties volumineuses des hooks

Par défaut, Codex limite chaque message de sortie d’un hook visible par le modèle à environ
2 500 tokens. Si un hook en renvoie davantage, Codex enregistre le texte intégral à l’emplacement
`<temp_dir>/hook_outputs/<session_id>/<uuid>.txt` et fournit au modèle un
aperçu comprenant le début et la fin du texte, avec le chemin du fichier enregistré. Ce comportement est appelé
**déport sur disque** : Codex stocke les sorties trop volumineuses sur disque et les remplace par un
aperçu plus court visible par le modèle. Si l’écriture du fichier échoue, le modèle
reçoit tout de même un aperçu tronqué.

  Veillez à ce que le contexte des hooks et des plugins reste concis. Le contexte de plusieurs hooks et plugins
  s’accumule et peut dégrader les performances du modèle. Augmenter `additionalContextLimit`
  accroît ce risque. Évitez de fixer la limite à `0`, sauf si le hook impose un
  plafond de sortie strict ; sinon, un seul hook peut occuper toute la fenêtre de
  contexte.

Pour tout hook de commande qui renvoie `additionalContext`, définissez
`additionalContextLimit` dans le gestionnaire afin de personnaliser le seuil approximatif
en tokens :

```json
{
  "type": "command",
  "command": "python3 ~/.codex/hooks/session_start.py",
  "additionalContextLimit": 5000
}

Omettez `additionalContextLimit` pour utiliser le seuil par défaut de `2500` tokens. Utilisez un
entier strictement positif pour choisir un autre seuil, ou `0` pour transmettre directement au modèle
l’intégralité du contexte supplémentaire du gestionnaire. Codex évalue indépendamment chaque
gestionnaire correspondant. Pour les événements qui ne peuvent pas produire de
contexte supplémentaire, Codex ignore `additionalContextLimit` et émet un
avertissement de configuration.

Ce paramètre s’applique uniquement à `additionalContext`. Les retours des outils et les prompts de
continuation conservent la limite par défaut.

Les sorties trop volumineuses pouvant être écrites sur disque, évitez de renvoyer des secrets ou
d’autres données sensibles dans les sorties des hooks.

## Exécutez les hooks en arrière-plan

Par défaut, Codex attend la fin d’un hook de commande avant de poursuivre
l’opération qui l’a déclenché. Définissez `async` sur `true` pour exécuter un hook de commande
en arrière-plan pendant que Codex poursuit son travail.

### Configurez un hook en arrière-plan

Ajoutez `"async": true` à un gestionnaire de commande dans `hooks.json` :

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/post_tool_use.py",
            "async": true,
            "timeout": 120
          }
        ]
      }
    ]
  }
}

Pour un hook défini directement dans `config.toml`, définissez `async = true` :

```toml
[[hooks.PostToolUse]]
matcher = "Bash"

[[hooks.PostToolUse.hooks]]
type = "command"
command = "python3 ~/.codex/hooks/post_tool_use.py"
async = true
timeout = 120

Les hooks en arrière-plan utilisent les mêmes entrées, critères de correspondance, procédures de révision et de validation de confiance, délais d’expiration et
[mécanismes de gestion des sorties volumineuses](#large-hook-output) que les hooks de commande synchrones. Comme
pour les autres hooks de commande, `timeout` s’exprime en secondes et vaut par défaut
`600`. Les hooks `Interrupt` ont un délai d’expiration d’une seconde par défaut et de trois secondes au maximum,
y compris lorsqu’ils s’exécutent en arrière-plan.

### Fonctionnement des hooks en arrière-plan

Lorsqu’un hook en arrière-plan se termine, Codex transmet les sorties informatives prises en charge
au prochain moment où la conversation le permet sans risque :

- Si un tour est en cours, Codex attend la fin de la requête au modèle et des appels d’outils en cours,
puis rend la sortie disponible pour la requête suivante au modèle dans ce même
tour.
- Si aucun tour n’est en cours, Codex attend le prochain tour utilisateur. La fin d’un
hook en arrière-plan ne déclenche pas de nouveau tour.

Utilisez la même sortie JSON propre à l’événement que pour un hook synchrone. Codex ajoute
`additionalContext` au contexte du modèle et présente `systemMessage` sous forme
d’avertissement.

  Les hooks en arrière-plan ne peuvent pas bloquer, approuver, réécrire ou autrement contrôler
l’opération qui les a déclenchés. Utilisez des hooks synchrones pour les politiques relatives aux outils,
les décisions d’autorisation, le rejet des prompts ou la poursuite d’un tour.

### Limites

- Codex exécute jusqu’à huit hooks en arrière-plan simultanément par session. Les hooks supplémentaires
attendent qu’un hook en cours d’exécution se termine.
- Chaque invocation correspondant aux critères s’exécute indépendamment, et les hooks en arrière-plan peuvent se terminer
dans un ordre différent de celui dans lequel ils ont démarré.
- À la fin de la session, Codex annule les hooks en arrière-plan qui ne sont pas terminés et supprime
les sorties qui n’ont pas été transmises.
- Les hooks `SessionEnd` s’exécutent toujours de façon synchrone.

## Hooks

### SessionStart

`matcher` s’applique à `source` pour cet événement.

Champs qui s’ajoutent aux [champs d’entrée communs](#common-input-fields) :

| Champ    | Type     | Signification                                                             |
| -------- | -------- | ------------------------------------------------------------------- |
| `source` | `string` | Mode de démarrage de la session : `startup`, `resume`, `clear` ou `compact` |

Le texte brut envoyé sur `stdout` est ajouté en tant que contexte développeur supplémentaire.

Le JSON envoyé sur `stdout` prend en charge les [champs de sortie communs](#common-output-fields) et la structure
suivante, propre à ce hook :

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Load the workspace conventions before editing."
  }
}

Le texte de `additionalContext` est ajouté en tant que contexte développeur supplémentaire.

Après le compactage d’une session racine par Codex, les hooks `SessionStart` qui correspondent à
`source: "compact"` s’exécutent avant la requête suivante au modèle. Cela s’applique aussi lorsqu’un
compactage automatique se produit au milieu d’un tour : Codex fournit le contexte
supplémentaire du hook à la reprise immédiate au lieu d’attendre
un tour utilisateur ultérieur. Si le hook renvoie `continue: false`, Codex met fin au tour
sans envoyer d’autre requête au modèle.

### SessionEnd

`SessionEnd` permet d’exécuter une commande à la fin d’une session, par exemple pour enregistrer les
notes finales ou nettoyer des fichiers. Il s’exécute pour le fil principal lorsque vous archivez ou
supprimez une conversation encore ouverte, lorsque Codex se ferme normalement, ou lorsqu’une
conversation est inactive et n’est ouverte dans aucun client connecté depuis 30
minutes. Il ne s’exécute pas pour les sous-agents.

Quitter l’affichage d’une conversation ou appeler `thread/unsubscribe` ne met pas
immédiatement fin à la session et ne déclenche donc pas tout de suite `SessionEnd`. Votre hook peut
toujours lire la transcription de la session pendant son exécution.

`matcher` filtre `reason` pour cet événement. Pour l’instant, `reason` vaut toujours `other`.
Vous pouvez omettre `matcher` ou utiliser `other` pour exécuter le hook à chaque événement `SessionEnd`.

Champs qui s’ajoutent aux [champs d’entrée communs](#common-input-fields) :

| Champ    | Type     | Signification                        |
| -------- | -------- | ------------------------------ |
| `reason` | `string` | Raison de la fin de la session : `other` |

Par exemple, une commande `SessionEnd` reçoit :

```json
{
  "session_id": "thr_123",
  "transcript_path": "/workspace/.codex/rollout.jsonl",
  "cwd": "/workspace",
  "hook_event_name": "SessionEnd",
  "reason": "other"
}

Les hooks `SessionEnd` s’exécutent toujours de façon synchrone, même si `async` vaut `true`. Ils
sont consultatifs : leur sortie n’oriente pas Codex et ne maintient pas le fil ouvert. Si une
commande dépasse le délai imparti ou se termine par une erreur, Codex le signale comme un échec du hook.

### SubagentStart

`matcher` s’applique à `agent_type` pour cet événement.

Champs qui s’ajoutent aux [champs d’entrée communs](#common-input-fields) :

| Champ             | Type     | Signification                                        |
| ----------------- | -------- | ---------------------------------------------- |
| `turn_id`         | `string` | Extension propre à Codex. Identifiant du tour Codex actif |
| `agent_id`        | `string` | Identifiant du sous-agent                    |
| `agent_type`      | `string` | Type ou profil du sous-agent                       |
| `permission_mode` | `string` | Mode d’autorisation actuel                        |

Le texte brut envoyé sur `stdout` est ajouté en tant que contexte développeur supplémentaire pour le sous-agent.

Le JSON envoyé sur `stdout` prend en charge `systemMessage` et la structure suivante, propre à ce hook :

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Review the repository test conventions first."
  }
}

Le texte de `additionalContext` est ajouté en tant que contexte développeur supplémentaire pour le
sous-agent. `continue: false` est analysé à des fins de compatibilité, mais n’empêche pas le
sous-agent de démarrer.

### PreToolUse

`PreToolUse` peut intercepter Bash, les modifications de fichiers effectuées via `apply_patch`,
les appels d’outils MCP et les autres outils de fonction locaux. Consultez la section [Couverture des
outils](#tool-coverage) pour connaître les chemins d’exécution pris en charge et les exceptions.

`matcher` s’applique à `tool_name` et aux alias utilisés pour la correspondance. Pour les modifications de fichiers via
`apply_patch`, les valeurs de `matcher` peuvent être `apply_patch`, `Edit` ou `Write` ; l’entrée du hook
indique toujours `tool_name: "apply_patch"`.

Champs qui s’ajoutent aux [champs d’entrée communs](#common-input-fields) :

| Champ         | Type         | Signification                                                                                                                          |
| ------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`     | `string`     | Extension propre à Codex. Identifiant du tour Codex actif                                                                                   |
| `tool_name`   | `string`     | Nom canonique de l’outil dans le hook, par exemple `Bash`, `apply_patch` ou un nom MCP comme `mcp__fs__read`                                     |
| `tool_use_id` | `string`     | Identifiant de l’appel d’outil pour cette invocation                                                                                                 |
| `tool_input`  | `JSON value` | Entrée propre à l’outil. `Bash` et `apply_patch` utilisent `tool_input.command`. Les outils MCP et les autres outils de fonction locaux envoient leurs arguments. |

Le texte brut envoyé sur `stdout` est ignoré.

Le JSON écrit sur `stdout` peut utiliser `systemMessage`. Pour refuser un appel d’outil pris en charge, renvoyez
cette structure propre au hook :

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook."
  }
}

Codex accepte également cette ancienne structure de blocage :

```json
{
  "decision": "block",
  "reason": "Destructive command blocked by hook."
}

Vous pouvez également utiliser le code de sortie `2` et écrire le motif du blocage sur `stderr`.

Pour ajouter du contexte visible par le modèle sans bloquer l’appel, renvoyez
`hookSpecificOutput.additionalContext` :

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "The pending command touches generated files."
  }
}

Pour réécrire un appel d’outil pris en charge sans le bloquer, renvoyez
`permissionDecision: "allow"` avec `updatedInput` :

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "echo rewritten"
    }
  }
}

Pour les commandes Bash et `apply_patch`, `updatedInput` doit inclure un champ
`command` de type chaîne de caractères. Pour MCP et les autres outils locaux de type fonction, `updatedInput` est
l’objet d’arguments de remplacement. Renvoyez `updatedInput` uniquement avec
`permissionDecision: "allow"` ; toute autre structure de `updatedInput` est signalée comme
une erreur.

`permissionDecision: "ask"`, l’ancienne forme `decision: "approve"`, `continue: false`,
`stopReason` et `suppressOutput` sont analysés, mais ne sont pas encore pris en charge. Codex marque
l’exécution du hook comme ayant échoué, signale l’erreur et poursuit l’appel de l’outil.

### PermissionRequest

`PermissionRequest` s’exécute lorsque Codex s’apprête à demander une approbation, par exemple pour une
élévation des permissions du shell ou un accès au réseau géré. Il peut autoriser la demande, la refuser
ou ne pas se prononcer et laisser l’invite d’approbation habituelle s’afficher.
Il ne s’exécute pas pour les commandes qui ne nécessitent pas d’approbation.

Le champ `matcher` s’applique à `tool_name` et aux alias de correspondance. Les valeurs canoniques actuelles
comprennent `Bash`, `apply_patch` et les noms d’outils MCP tels que
`mcp__server__tool` ; `apply_patch` correspond aussi à `Edit` et `Write`.

Champs en complément des [champs d’entrée communs](#common-input-fields) :

| Champ                    | Type             | Signification                                                                                                        |
| ------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------- |
| `turn_id`                | `string`         | Extension propre à Codex. Identifiant du tour Codex actif                                                                 |
| `tool_name`              | `string`         | Nom canonique de l’outil pour le hook, par exemple `Bash`, `apply_patch` ou un nom MCP tel que `mcp__fs__read`                   |
| `tool_input`             | `JSON value`     | Données d’entrée propres à l’outil. `Bash` et `apply_patch` utilisent `tool_input.command`, tandis que les outils MCP transmettent tous les arguments. |
| `tool_input.description` | `string \| null` | Motif de la demande d’approbation en langage naturel, si Codex en dispose                                                             |

Le texte brut écrit sur `stdout` est ignoré.

Les données d’entrée de certains outils peuvent inclure une description en langage naturel, mais ne comptez pas sur la présence d’un champ
`tool_input.description` pour chaque outil.

Pour approuver la demande, renvoyez :

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow"
    }
  }
}

Pour refuser la demande, renvoyez :

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "deny",
      "message": "Blocked by repository policy."
    }
  }
}

Si plusieurs hooks correspondants renvoient des décisions, toute décision `deny` prévaut. Sinon,
`allow` permet à la demande de suivre son cours sans afficher l’invite d’approbation. Si aucun
hook correspondant ne se prononce, Codex suit le processus d’approbation habituel.

Ne renvoyez pas `updatedInput`, `updatedPermissions` ou `interrupt` pour
`PermissionRequest` ; ces champs sont réservés à de futurs comportements et entraînent
actuellement un refus par défaut.

### PostToolUse

`PostToolUse` s’exécute après que les outils pris en charge ont produit une sortie, notamment Bash,
`apply_patch`, les appels d’outils MCP et les autres outils locaux de type fonction. Pour Bash, il
s’exécute aussi après les commandes qui se terminent avec un code de sortie non nul. Il ne peut pas annuler les effets
de bord d’un outil déjà exécuté. Consultez [Outils pris en charge](#tool-coverage) pour connaître
les chemins d’exécution pris en charge et les exceptions.

Le champ `matcher` s’applique à `tool_name` et aux alias de correspondance. Pour les modifications de fichiers effectuées avec
`apply_patch`, les valeurs de `matcher` peuvent être `apply_patch`, `Edit` ou `Write` ; les données d’entrée du hook
indiquent toujours `tool_name: "apply_patch"`.

Champs en complément des [champs d’entrée communs](#common-input-fields) :

| Champ           | Type         | Signification                                                                                                                          |
| --------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`       | `string`     | Extension propre à Codex. Identifiant du tour Codex actif                                                                                   |
| `tool_name`     | `string`     | Nom canonique de l’outil pour le hook, par exemple `Bash`, `apply_patch` ou un nom MCP tel que `mcp__fs__read`                                     |
| `tool_use_id`   | `string`     | Identifiant de l’appel d’outil pour cette invocation                                                                                                 |
| `tool_input`    | `JSON value` | Données d’entrée propres à l’outil. `Bash` et `apply_patch` utilisent `tool_input.command`. Les outils MCP et les autres outils locaux de type fonction transmettent leurs arguments. |
| `tool_response` | `JSON value` | Données de sortie propres à l’outil. Les outils MCP transmettent le résultat de l’appel MCP. Les autres outils locaux de type fonction transmettent normalement leur sortie destinée au modèle.    |

Le texte brut écrit sur `stdout` est ignoré.

Le JSON écrit sur `stdout` peut utiliser `systemMessage` ainsi que cette structure propre au hook :

```json
{
  "decision": "block",
  "reason": "The Bash output needs review before continuing.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command updated generated files."
  }
}

Le texte de `additionalContext` est ajouté en tant que contexte développeur supplémentaire.

Pour cet événement, `decision: "block"` n’annule pas la commande Bash déjà exécutée.
Codex enregistre plutôt le retour, remplace le résultat de l’outil par ce
retour et poursuit l’exécution du modèle à partir du message fourni par le hook.

Vous pouvez également utiliser le code de sortie `2` et écrire le motif du retour sur `stderr`.

Pour arrêter le traitement normal du résultat initial de l’outil une fois la commande
exécutée, renvoyez `continue: false`. Codex remplacera le résultat de l’outil par
votre retour ou votre message d’arrêt, puis reprendra à partir de là.

`updatedMCPToolOutput` et `suppressOutput` sont analysés, mais ne sont pas encore pris en charge.
Codex marque l’exécution du hook comme ayant échoué, signale l’erreur et poursuit le traitement normal
du résultat de l’outil.

#### Appels d’outils en mode code

Lorsqu’un modèle utilise le mode code pour appeler un outil depuis JavaScript, les décisions des hooks s’appliquent
à cet appel imbriqué. `PreToolUse` peut empêcher l’exécution de l’outil ou réécrire
ses données d’entrée. Un hook `PostToolUse` bloquant ne peut pas annuler les effets de bord de l’outil, mais il
peut empêcher le résultat initial de parvenir au script en cours d’exécution.

| Résultat du hook                                                      | Résultat visible en mode code                                                                                    |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Blocage par `PreToolUse`                                              | La promesse de l’outil est rejetée avant l’exécution de l’outil.                                                         |
| `PreToolUse` renvoie `updatedInput`                              | L’outil s’exécute avec les données d’entrée réécrites et la promesse se résout avec ce résultat.                      |
| `PostToolUse` renvoie `decision: "block"` ou se termine avec le code de sortie `2` | L’outil s’exécute, puis la promesse est rejetée avec le motif fourni par le hook.                                          |
| `PostToolUse` renvoie `continue: false`                          | Codex utilise le retour du hook comme résultat visible par le modèle, mais ne rejette pas la promesse de l’appel d’outil imbriqué. |

### PreCompact

`PreCompact` s’exécute avant que Codex ne compacte la discussion. Le champ `matcher` s’applique
à `trigger`, dont les valeurs sont `manual` et `auto`.

Champs en complément des [champs d’entrée communs](#common-input-fields) :

| Champ     | Type     | Signification                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Extension propre à Codex. Identifiant du tour Codex actif |
| `trigger` | `string` | Déclencheur du compactage : `manual` ou `auto`  |

Le texte brut écrit sur `stdout` est ignoré.

Le JSON écrit sur `stdout` prend en charge les [champs de sortie communs](#common-output-fields). Si un
hook `PreCompact` correspondant renvoie `continue: false`, Codex s’arrête avant
le compactage.

### PostCompact

`PostCompact` s’exécute après que Codex a compacté la discussion. `matcher` s’applique
à `trigger`, dont les valeurs sont `manual` et `auto`.

Champs qui s’ajoutent aux [champs d’entrée communs](#common-input-fields) :

| Champ     | Type     | Signification                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Extension propre à Codex. Identifiant du tour actif de Codex |
| `trigger` | `string` | Déclencheur du compactage : `manual` ou `auto`  |

Le texte brut écrit sur `stdout` est ignoré.

Le JSON écrit sur `stdout` prend en charge les [champs de sortie communs](#common-output-fields). Si un
hook `PostCompact` correspondant renvoie `continue: false`, Codex s’arrête après
le compactage.

### UserPromptSubmit

`matcher` n’est actuellement pas utilisé pour cet événement.

Champs qui s’ajoutent aux [champs d’entrée communs](#common-input-fields) :

| Champ     | Type     | Signification                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Extension propre à Codex. Identifiant du tour actif de Codex |
| `prompt`  | `string` | Prompt utilisateur sur le point d’être envoyé            |

Le texte brut écrit sur `stdout` est ajouté en tant que contexte développeur supplémentaire.

Le JSON écrit sur `stdout` prend en charge les [champs de sortie communs](#common-output-fields) et
cette structure propre au hook :

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Ask for a clearer reproduction before editing files."
  }
}

Le texte de `additionalContext` est ajouté en tant que contexte développeur supplémentaire.

Pour bloquer le prompt, renvoyez :

```json
{
  "decision": "block",
  "reason": "Ask for confirmation before doing that."
}

Vous pouvez également utiliser le code de sortie `2` et écrire le motif du blocage sur `stderr`.

### SubagentStop

`matcher` s’applique à `agent_type` pour cet événement.

Champs qui s’ajoutent aux [champs d’entrée communs](#common-input-fields) :

| Champ                    | Type             | Signification                                         |
| ------------------------ | ---------------- | ----------------------------------------------- |
| `turn_id`                | `string`         | Extension propre à Codex. Identifiant du tour actif de Codex  |
| `agent_id`               | `string`         | Identifiant du sous-agent                     |
| `agent_type`             | `string`         | Type ou profil du sous-agent                        |
| `agent_transcript_path`  | `string \| null` | Chemin du fichier de transcription du sous-agent, s’il existe    |
| `stop_hook_active`       | `boolean`        | Indique si l’exécution de ce sous-agent a déjà été poursuivie     |
| `last_assistant_message` | `string \| null` | Dernier message du sous-agent en tant qu’assistant, s’il est disponible |

`SubagentStop` attend du JSON sur `stdout` lorsque le code de sortie est `0`. Une sortie en texte brut est
invalide pour cet événement.

Le JSON écrit sur `stdout` prend en charge les [champs de sortie communs](#common-output-fields). Pour demander à
Codex de poursuivre l’exécution du sous-agent, renvoyez :

```json
{
  "decision": "block",
  "reason": "Run one more focused pass inside the subagent."
}

Vous pouvez également utiliser le code de sortie `2` et écrire la raison de poursuivre l’exécution sur `stderr`.

Si au moins un hook `SubagentStop` correspondant renvoie `continue: false`, ce résultat
prévaut sur les décisions de poursuivre l’exécution prises par les autres hooks `SubagentStop`
correspondants.

### Stop

`matcher` n’est actuellement pas utilisé pour cet événement.

Champs qui s’ajoutent aux [champs d’entrée communs](#common-input-fields) :

| Champ                    | Type             | Signification                                           |
| ------------------------ | ---------------- | ------------------------------------------------- |
| `turn_id`                | `string`         | Extension propre à Codex. Identifiant du tour actif de Codex    |
| `stop_hook_active`       | `boolean`        | Indique si ce tour a déjà été poursuivi par `Stop` |
| `last_assistant_message` | `string \| null` | Texte du dernier message de l’assistant, s’il est disponible       |

`Stop` attend du JSON sur `stdout` lorsque le code de sortie est `0`. Une sortie en texte brut est invalide
pour cet événement.

Le JSON écrit sur `stdout` prend en charge les [champs de sortie communs](#common-output-fields). Pour permettre à
Codex de continuer, renvoyez :

```json
{
  "decision": "block",
  "reason": "Run one more pass over the failing tests."
}

Vous pouvez également utiliser le code de sortie `2` et écrire la raison de poursuivre l’exécution sur `stderr`.

Pour cet événement, `decision: "block"` ne rejette pas le tour. Ce résultat demande plutôt à
Codex de continuer et crée automatiquement un nouveau prompt de continuation qui fait office
de nouveau prompt utilisateur, avec la valeur de `reason` comme texte.

Si au moins un hook `Stop` correspondant renvoie `continue: false`, ce résultat prévaut
sur les décisions de poursuivre l’exécution prises par les autres hooks `Stop` correspondants.

### Interrupt

`Interrupt` s’exécute lorsque vous interrompez un tour actif dans le fil principal. Utilisez-le
pour consigner l’interruption ou effectuer le nettoyage lié au travail lancé par un hook. Il ne s’exécute pas
pour les fils inactifs ni pour les sous-agents, et tout `matcher` configuré est ignoré.

En plus des [champs d’entrée communs](#common-input-fields), l’événement inclut
`turn_id`, l’identifiant du tour interrompu, et `permission_mode`.

Les hooks de commande ont un délai d’expiration d’une seconde par défaut. Les délais configurés doivent être compris
entre une et trois secondes. La sortie d’un hook ne peut ni empêcher
l’interruption ni redémarrer le tour. Terminez avec le code `0` sans sortie, ou renvoyez du JSON avec
un champ facultatif `systemMessage` pour afficher un avertissement. Une sortie en texte brut est invalide
pour cet événement.

```json
{ "systemMessage": "Saved the interrupted turn to the local audit log." }

## Schémas

  Les schémas de la branche `main` accessibles via les liens peuvent inclure des champs de hooks absents de la
  version actuelle. Référez-vous à cette page pour connaître le comportement de la version publiée.

Si vous avez besoin du format d’échange exact de la version actuelle, consultez les schémas générés dans le
[dépôt GitHub de Codex](https://github.com/openai/codex/tree/main/codex-rs/hooks/schema/generated).
