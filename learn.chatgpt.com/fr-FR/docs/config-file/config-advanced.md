<!-- source: https://learn.chatgpt.com/fr-FR/docs/config-file/config-advanced -->

Utilisez ces options lorsque vous avez besoin d’un contrôle accru sur les fournisseurs, les politiques et les intégrations. Pour démarrer rapidement, consultez [Principes de configuration](/fr-FR/codex/config-file/config-basic).

Pour en savoir plus sur les consignes de projet, les capacités réutilisables, les commandes slash personnalisées, les flux de travail de sous-agents et les intégrations, consultez [Personnalisation](/fr-FR/codex/customization/overview). Pour les clés de configuration, consultez [Référence de configuration](/fr-FR/codex/config-file/config-reference).

## Profils

Les profils permettent d’enregistrer des couches de configuration nommées et de passer de l’une à l’autre depuis
la CLI. Lorsque vous utilisez `--profile profile-name`, Codex charge
`~/.codex/config.toml`, puis lui superpose `~/.codex/profile-name.config.toml`.
Les noms de profils peuvent contenir des lettres, des chiffres, des traits d’union et des traits de soulignement.

Créez un fichier TOML distinct pour chaque profil. Utilisez des clés de configuration de premier niveau dans le
fichier de profil ; ne les imbriquez pas sous `[profiles.profile-name]`.

```toml
# ~/.codex/deep-review.config.toml
model = "gpt-5.5"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
model_catalog_json = "/Users/me/.codex/model-catalogs/deep-review.json"

```shell
codex --profile deep-review
codex exec --profile deep-review "review this change"

Comme le fichier de profil est une couche située au-dessus de votre configuration utilisateur de base, mais en dessous
des configurations de projet et de la CLI, il lui suffit de contenir les valeurs qui diffèrent de votre
configuration de base. Les fichiers de profil peuvent également redéfinir `model_catalog_json` ; Codex utilise
la valeur du profil lorsque ce paramètre est défini dans les deux fichiers.

Dans Codex 0.134.0 et les versions ultérieures, `--profile` ne lit plus `[profiles.profile-name]`
dans `config.toml`, et le sélecteur de premier niveau `profile = "profile-name"` n’est
plus pris en charge. Déplacez les anciens paramètres de profil vers
`~/.codex/profile-name.config.toml`, puis supprimez la table correspondante
`[profiles.profile-name]` et le sélecteur `profile = "profile-name"` de
`config.toml`.

## Remplacements ponctuels via la CLI

En plus de modifier `~/.codex/config.toml`, vous pouvez remplacer la configuration pour une seule exécution depuis la CLI :

- Privilégiez les options dédiées lorsqu’elles existent (par exemple, `--model`).
- Utilisez `-c` / `--config` pour remplacer n’importe quelle clé.

Exemples :

```shell
# Dedicated flag
codex --model gpt-5.6-terra

# Generic key/value override (value is TOML, not JSON)
codex --config model='"gpt-5.6-terra"'
codex --config sandbox_workspace_write.network_access=true
codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'

Remarques :

- Les clés peuvent utiliser la notation pointée pour définir des valeurs imbriquées (par exemple, `mcp_servers.context7.enabled=false`).
- Les valeurs de `--config` sont analysées au format TOML. En cas de doute, placez la valeur entre guillemets pour éviter que votre shell ne la découpe au niveau des espaces.
- Si la valeur ne peut pas être analysée au format TOML, Codex la traite comme une chaîne de caractères.

## Emplacements de la configuration et des données d’état

Codex stocke son état local dans `CODEX_HOME` (`~/.codex` par défaut).

Fichiers courants que vous pouvez y trouver :

- `config.toml` (votre configuration locale)
- `auth.json` (si vous stockez les identifiants dans un fichier) ou le trousseau de clés de votre système d’exploitation
- `history.jsonl` (si la persistance de l’historique est activée)
- Autres données d’état propres à l’utilisateur, comme les journaux et les caches

Pour en savoir plus sur l’authentification (y compris les modes de stockage des identifiants), consultez [Authentification](/fr-FR/codex/auth). Pour la liste complète des clés de configuration, consultez [Référence de configuration](/fr-FR/codex/config-file/config-reference).

Pour les valeurs par défaut partagées, les règles et les Skills stockés dans des dépôts ou des chemins système, consultez [Configuration d’équipe](/fr-FR/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config).

Si vous souhaitez simplement faire pointer le fournisseur OpenAI intégré vers un proxy LLM, un routeur ou un projet où la résidence des données est activée, définissez `openai_base_url` dans `config.toml` au lieu de définir un nouveau fournisseur. Cela modifie l’URL de base du fournisseur `openai` intégré sans nécessiter d’entrée `model_providers.<id>` distincte.

```toml
openai_base_url = "https://us.api.openai.com/v1"

## Fichiers de configuration du projet (`.codex/config.toml`)

En plus de votre configuration utilisateur, Codex lit les remplacements propres au projet à partir des fichiers `.codex/config.toml` de votre dépôt. Codex parcourt l’arborescence depuis la racine du projet jusqu’à votre répertoire de travail actuel et charge chaque fichier `.codex/config.toml` trouvé. Si plusieurs fichiers définissent la même clé, celui qui se trouve le plus près de votre répertoire de travail l’emporte.

Par sécurité, Codex ne charge les fichiers de configuration propres au projet que lorsque celui-ci est considéré comme fiable. Si le projet n’est pas considéré comme fiable, Codex ignore ses couches `.codex/`, notamment `.codex/config.toml`, les hooks propres au projet et les règles propres au projet. Les couches utilisateur et système restent distinctes et sont tout de même chargées.

Les chemins relatifs dans une configuration de projet (par exemple, `model_instructions_file`) sont résolus par rapport au dossier `.codex/` qui contient le fichier `config.toml`.

Les fichiers de configuration de projet ne peuvent pas remplacer les paramètres qui redirigent les identifiants, modifient
les métadonnées contrôlées par l’hôte dans les requêtes de l’application, changent l’authentification du fournisseur, sélectionnent des profils de configuration
ou exécutent des commandes de notification ou de télémétrie locales à la machine. Codex ignore les
clés suivantes dans le fichier `.codex/config.toml` propre au projet et affiche un avertissement au démarrage
lorsqu’il les rencontre : `openai_base_url`, `chatgpt_base_url`,
`apps_mcp_product_sku`, `model_provider`, `model_providers`, `notify`,
`profile`, `profiles`, `experimental_realtime_ws_base_url` et `otel`. Définissez
les clés de fournisseur, de notification et de télémétrie dans votre fichier utilisateur
`~/.codex/config.toml` ; sélectionnez les profils de configuration avec `--profile profile-name`
et `~/.codex/profile-name.config.toml`.

## Hooks

Codex peut également charger des hooks de cycle de vie depuis des fichiers `hooks.json` ou des tables intégrées
`[hooks]` dans des fichiers `config.toml` situés à côté des couches de configuration actives.

En pratique, les quatre emplacements les plus utiles sont :

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

Les hooks propres au projet ne sont chargés que si la couche `.codex/` du projet est considérée comme fiable.
Les hooks de niveau utilisateur ne dépendent pas de la confiance accordée au projet.

Les hooks TOML intégrés utilisent la même structure d’événements que `hooks.json` :

```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

Si une même couche contient à la fois `hooks.json` et une table `[hooks]` intégrée, Codex charge
les deux et affiche un avertissement. Privilégiez une seule représentation par couche.

Pour connaître la liste actuelle des événements, les champs d’entrée, le comportement des sorties et les limitations, consultez
[Hooks](/fr-FR/codex/hooks).

## Rôles des agents (`[agents]` dans `config.toml`)

Pour configurer les rôles des sous-agents (`[agents]` dans `config.toml`), consultez [Sous-agents](/fr-FR/codex/agent-configuration/subagents).

## Détection de la racine du projet

Codex détecte la configuration du projet (par exemple, les couches `.codex/` et `AGENTS.md`) en remontant l’arborescence depuis le répertoire de travail jusqu’à atteindre la racine d’un projet.

Par défaut, Codex considère qu’un répertoire contenant `.git` est la racine du projet. Pour personnaliser ce comportement, définissez `project_root_markers` dans `config.toml` :

```toml
# Treat a directory as the project root when it contains any of these markers.
project_root_markers = [".git", ".hg", ".sl"]

Définissez `project_root_markers = []` pour ignorer la recherche dans les répertoires parents et considérer le répertoire de travail actuel comme la racine du projet.

## Fournisseurs de modèles personnalisés

Un fournisseur de modèles définit la manière dont Codex se connecte à un modèle (URL de base, API de communication, authentification et en-têtes HTTP facultatifs). Les fournisseurs personnalisés ne peuvent pas réutiliser les identifiants réservés des fournisseurs intégrés : `openai`, `ollama` et `lmstudio`.

Définissez des fournisseurs supplémentaires et faites pointer `model_provider` vers eux :

```toml
model = "gpt-5.6-terra"
model_provider = "proxy"

[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "http://proxy.example.com"
env_key = "OPENAI_API_KEY"

[model_providers.local_ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"

[model_providers.mistral]
name = "Mistral"
base_url = "https://api.mistral.ai/v1"
env_key = "MISTRAL_API_KEY"

Si un fournisseur personnalisé prend en charge le point de terminaison de recherche web autonome, déclarez
cette capacité dans sa configuration :

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
env_key = "OPENAI_API_KEY"
supports_standalone_web_search = true

Pour les fournisseurs personnalisés, ce paramètre vaut `false` par défaut. La recherche web autonome est
en cours de développement et désactivée par défaut. Définir la capacité du fournisseur sur `true`
ne l’active pas : le fournisseur doit prendre en charge un point de terminaison compatible,
et le modèle ainsi que l’environnement d’exécution sélectionnés doivent prendre en charge la recherche autonome. Le
[mode `web_search`](/fr-FR/codex/web-search) configuré et les
restrictions de recherche gérées s’appliquent toujours.

Ajoutez des en-têtes de requête si nécessaire :

```toml
[model_providers.example]
http_headers = { "X-Example-Header" = "example-value" }
env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }

Utilisez une authentification par commande lorsqu’un fournisseur exige que Codex récupère des tokens Bearer auprès d’un utilitaire externe de gestion des identifiants :

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
wire_api = "responses"

[model_providers.proxy.auth]
command = "/usr/local/bin/fetch-codex-token"
args = ["--audience", "codex"]
timeout_ms = 5000
refresh_interval_ms = 300000

La commande d’authentification ne reçoit aucune donnée via `stdin` et doit écrire le token sur stdout. Codex supprime les espaces blancs en début et en fin, considère un token vide comme une erreur et le renouvelle de manière proactive selon `refresh_interval_ms` ; définissez `refresh_interval_ms = 0` pour ne le renouveler qu’après une nouvelle tentative d’authentification. Ne combinez pas `[model_providers.<id>.auth]` avec `env_key`, `experimental_bearer_token` ou `requires_openai_auth`.

### Fournisseur Amazon Bedrock

Codex inclut un fournisseur de modèles `amazon-bedrock` intégré. Affectez-le directement à
`model_provider` ; contrairement aux fournisseurs personnalisés, ce fournisseur intégré ne prend en charge que
les remplacements imbriqués du profil et de la région AWS.

```toml
model_provider = "amazon-bedrock"
model = "<bedrock-model-id>"

[model_providers.amazon-bedrock.aws]
profile = "default"
region = "eu-central-1"

Si vous omettez `profile`, Codex utilise la chaîne standard d’identifiants AWS. Définissez
`region` sur la région Bedrock prise en charge qui doit traiter les requêtes.

Pour connaître la procédure complète de configuration, les options d’authentification, les modèles pris en charge et la disponibilité
des fonctionnalités, consultez [Utiliser ChatGPT Work et Codex avec Amazon
Bedrock](/fr-FR/codex/amazon-bedrock).

## Mode OSS (fournisseurs locaux)

Codex peut fonctionner avec un fournisseur local « open source » tel qu’Ollama ou LM
Studio lorsque vous utilisez `--oss`. Choisissez-en un pour une seule exécution avec
`--local-provider`, ou définissez `oss_provider` comme valeur par défaut. Si aucun des deux n’est défini, la
CLI interactive vous invite à en choisir un ; `codex exec` se termine par une erreur.

```toml
# Default local provider used with `--oss`
oss_provider = "ollama" # or "lmstudio"

## Fournisseur Azure et réglages propres à chaque fournisseur

```toml
[model_providers.azure]
name = "Azure"
base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
env_key = "AZURE_OPENAI_API_KEY"
query_params = { api-version = "2025-04-01-preview" }
wire_api = "responses"
request_max_retries = 4
stream_max_retries = 10
stream_idle_timeout_ms = 300000

Pour modifier l’URL de base du fournisseur OpenAI intégré, utilisez `openai_base_url` ; ne créez pas `[model_providers.openai]`, car vous ne pouvez pas remplacer les identifiants des fournisseurs intégrés.

## Organisations API utilisant la résidence des données

Pour les projets créés avec la [résidence des données](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt) activée, vous pouvez créer un fournisseur de modèles afin de mettre à jour `base_url` avec le [préfixe approprié](/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency). Pour les espaces de travail ChatGPT avec résidence des données, aucun fournisseur personnalisé n’est nécessaire ; Codex respecte les paramètres de résidence de l’espace de travail lorsque vous vous connectez avec ChatGPT.

```toml
model_provider = "openaidr"
[model_providers.openaidr]
name = "OpenAI Data Residency"
base_url = "https://us.api.openai.com/v1" # Replace 'us' with domain prefix

## Raisonnement, niveau de détail et limites du modèle

```toml
model_reasoning_summary = "none"          # Disable summaries
model_verbosity = "low"                   # Shorten responses
model_supports_reasoning_summaries = true # Force reasoning
model_context_window = 128000             # Context window size

`model_verbosity` s’applique uniquement aux fournisseurs qui utilisent la Responses API. Les fournisseurs Chat Completions ignorent ce paramètre.

## Politiques d’approbation et modes de bac à sable

Choisissez le niveau d’exigence des approbations (qui détermine quand Codex se met en pause) et le niveau du bac à sable (qui détermine l’accès aux fichiers et au réseau).

Pour connaître les aspects opérationnels à prendre en compte lorsque vous modifiez `config.toml`, consultez [Combinaisons courantes de bac à sable et d’approbation](/fr-FR/codex/agent-approvals-security#common-sandbox-and-approval-combinations), [Chemins protégés dans les racines accessibles en écriture](/fr-FR/codex/agent-approvals-security#protected-paths-in-writable-roots) et [Accès réseau](/fr-FR/codex/agent-approvals-security#network-access).

Pour en savoir plus sur les profils d’autorisations en version bêta qui configurent conjointement l’accès au système de fichiers et au réseau, consultez [Autorisations](/fr-FR/codex/permissions).

Vous pouvez également utiliser une politique d’approbation granulaire (`approval_policy = { granular = { ... } }`) pour autoriser ou rejeter automatiquement certaines catégories de prompts. Cette option est utile si vous souhaitez conserver les approbations interactives habituelles dans certains cas, mais refuser automatiquement les autres par mesure de sécurité, notamment `request_permissions` ou les prompts liés aux scripts de Skills.

Définissez `approvals_reviewer = "auto_review"` pour soumettre les demandes d’approbation
interactives admissibles à la révision automatique. Cela change le réviseur, mais pas la
limite du bac à sable.

Utilisez `[auto_review].policy` pour définir les instructions locales relatives à la politique de révision. Le paramètre géré
`guardian_policy_config` est prioritaire.

```toml
approval_policy = "untrusted"   # Other options: on-request, never, or { granular = { ... } }
approvals_reviewer = "user"     # Or "auto_review" for automatic review
sandbox_mode = "workspace-write"
allow_login_shell = false       # Optional hardening: disallow login shells for shell tools

# Example granular approval policy:
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

[sandbox_workspace_write]
exclude_tmpdir_env_var = false  # Allow $TMPDIR
exclude_slash_tmp = false       # Allow /tmp
writable_roots = ["/Users/YOU/.pyenv/shims"]
network_access = false          # Opt in to outbound network

[auto_review]
policy = """
Use your organization's automatic review policy.
"""

### Profils d’autorisations nommés

Pour en savoir plus sur les profils intégrés, la syntaxe des profils personnalisés et le modèle complet de configuration du système de fichiers et
du réseau, consultez [Autorisations](/fr-FR/codex/permissions).

Pour obtenir la liste complète des clés et les contraintes imposées par les exigences, consultez
[Référence de configuration](/fr-FR/codex/config-file/config-reference) et
[Configuration gérée](/fr-FR/codex/enterprise/managed-configuration).

  En mode workspace-write, certains environnements maintiennent `.git/` et `.codex/`
  en lecture seule, même si le reste de l’espace de travail est accessible en écriture. C’est pourquoi
  des commandes comme `git commit` peuvent encore nécessiter une approbation pour s’exécuter hors du
  bac à sable. Si vous souhaitez empêcher Codex d’exécuter certaines commandes, par exemple bloquer `git
  commit` hors du bac à sable, utilisez les
<a href="/codex/agent-configuration/rules">règles</a>.

Désactivez entièrement le bac à sable (uniquement si votre environnement isole déjà les processus) :

```toml
sandbox_mode = "danger-full-access"

## Politique d’environnement du shell

`shell_environment_policy` détermine quelles variables d’environnement Codex transmet aux
commandes lancées. Partez d’un environnement vide avec `inherit = "none"`, ou
héritez d’un ensemble restreint avec `inherit = "core"`. Ajoutez des valeurs explicites et des
filtres définis par clé pour éviter de transmettre inutilement des secrets aux commandes lancées.

```toml
[shell_environment_policy]
inherit = "core"
set = { MY_FLAG = "1" }
ignore_default_excludes = false

[shell_environment_policy.filters]
"AWS_*" = "exclude"
"AZURE_*" = "exclude"

Les motifs de filtrage ne tiennent pas compte de la casse et prennent en charge `*` et `?`. Utilisez `"exclude"`
pour supprimer les variables correspondantes. Dès qu’un motif utilise `"include"`, Codex ne conserve
que les variables correspondant à un motif d’inclusion. Les inclusions ne rétablissent pas les variables
déjà exclues. Les clés des filtres sont fusionnées sans tenir compte de la casse entre les
couches de configuration.

`ignore_default_excludes` vaut `true` par défaut. Codex ne supprime donc pas automatiquement
les variables dont le nom contient `KEY`, `SECRET` ou `TOKEN`. Définissez-le sur `false`
pour appliquer ces exclusions automatiques avant vos filtres explicites.

Codex applique d’abord les exclusions automatiques, puis les exclusions personnalisées, les valeurs de
`set` et enfin la liste d’autorisation fondée sur les motifs d’inclusion. Comme `set` est appliqué après
les exclusions, il peut rétablir une variable exclue. Une liste d’autorisation fondée sur les motifs d’inclusion
peut néanmoins supprimer cette valeur rétablie.

Les anciens tableaux `exclude` et `include_only` restent pris en charge pour les
configurations existantes. N’associez aucun de ces tableaux à
`[shell_environment_policy.filters]` dans une même couche de configuration : Codex
rejette cette combinaison.

## Serveurs MCP

Consultez la [documentation consacrée à MCP](/fr-FR/codex/extend/mcp) pour en savoir plus sur la configuration.

## Observabilité et télémétrie

Activez l’exportation des journaux OpenTelemetry (OTel) pour suivre les exécutions de Codex (requêtes API, événements SSE, prompts, approbations et résultats des outils). Elle est désactivée par défaut ; activez-la via `[otel]` :

```toml
[otel]
environment = "staging"   # defaults to "dev"
exporter = "none"         # set to otlp-http or otlp-grpc to send events
log_user_prompt = false   # redact user prompts unless explicitly enabled

Choisissez un exportateur :

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}

Avec `exporter = "none"`, Codex enregistre les événements, mais n’envoie rien. Les exportateurs traitent les données par lots de façon asynchrone et vident leur tampon à l’arrêt. Les métadonnées des événements comprennent le nom du service, la version de la CLI, l’étiquette d’environnement, l’identifiant de conversation, le modèle, les paramètres de bac à sable et d’approbation, ainsi que les champs propres à chaque événement (voir [Référence de configuration](/fr-FR/codex/config-file/config-reference)).

### Événements émis

Codex émet des événements de journalisation structurés concernant les exécutions et l’utilisation des outils. Voici quelques types d’événements représentatifs :

- `codex.conversation_starts` (modèle, paramètres de raisonnement, politique de bac à sable et d’approbation)
- `codex.api_request` (tentative, statut/réussite, durée et détails de l’erreur)
- `codex.sse_event` (type d’événement de flux, réussite/échec, durée et nombre de tokens pour `response.completed`)
- `codex.websocket_request` et `codex.websocket_event` (durée de la requête et type/réussite/erreur pour chaque message)
- `codex.user_prompt` (longueur ; contenu masqué sauf activation explicite)
- `codex.tool_decision` (approbation/refus et origine de la décision : configuration ou utilisateur)
- `codex.tool_result` (durée, réussite, extrait de sortie)

### Métriques OTel émises

Lorsque le pipeline de métriques OTel est activé, Codex émet des compteurs et des histogrammes de durée pour l’activité liée à l’API, aux flux et aux outils.

Chaque métrique ci-dessous inclut également les étiquettes de métadonnées par défaut suivantes : `auth_mode`, `originator`, `session_source`, `model` et `app.version`.

| Métrique                                | Type      | Champs              | Description                                                       |
| ------------------------------------- | --------- | ------------------- | ----------------------------------------------------------------- |
| `codex.api_request`                   | compteur   | `status`, `success` | Nombre de requêtes API par statut HTTP et résultat (réussite ou échec).             |
| `codex.api_request.duration_ms`       | histogramme | `status`, `success` | Durée des requêtes API en millisecondes.                             |
| `codex.sse_event`                     | compteur   | `kind`, `success`   | Nombre d’événements SSE par type d’événement et résultat (réussite ou échec).                |
| `codex.sse_event.duration_ms`         | histogramme | `kind`, `success`   | Durée de traitement des événements SSE en millisecondes.                    |
| `codex.websocket.request`             | compteur   | `success`           | Nombre de requêtes WebSocket par résultat (réussite ou échec).                       |
| `codex.websocket.request.duration_ms` | histogramme | `success`           | Durée des requêtes WebSocket en millisecondes.                       |
| `codex.websocket.event`               | compteur   | `kind`, `success`   | Nombre de messages/événements WebSocket par type et résultat (réussite ou échec).        |
| `codex.websocket.event.duration_ms`   | histogramme | `kind`, `success`   | Durée de traitement des messages/événements WebSocket en millisecondes.      |
| `codex.tool.call`                     | compteur   | `tool`, `success`   | Nombre d’appels d’outil par nom d’outil et par résultat (réussite ou échec).           |
| `codex.tool.call.duration_ms`         | histogramme | `tool`, `success`   | Durée d’exécution des outils en millisecondes, par nom d’outil et par résultat. |

Pour en savoir plus sur la sécurité et la confidentialité liées à la télémétrie, consultez [Sécurité](/fr-FR/codex/agent-approvals-security#monitoring-and-telemetry).

### Métriques

Par défaut, Codex envoie périodiquement à OpenAI une petite quantité de données anonymes sur l’utilisation et l’état de fonctionnement. Ces données permettent de détecter les dysfonctionnements de Codex et de savoir quelles fonctionnalités et options de configuration sont utilisées, afin que l’équipe Codex puisse se concentrer sur ce qui importe le plus. Ces métriques ne contiennent aucune information permettant d’identifier une personne (PII). La collecte de métriques est indépendante de l’exportation de journaux et de traces via OTel.

Pour désactiver complètement, sur une machine, la collecte de métriques dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE, définissez le paramètre d’analyse dans votre configuration :

```toml
[analytics]
enabled = false

Chaque métrique comprend ses propres champs, auxquels s’ajoutent les champs de contexte par défaut ci-dessous.

#### Champs de contexte par défaut (applicables à chaque événement/métrique)

- `auth_mode` : `swic` \| `api` \| `unknown`.
- `model` : nom du modèle utilisé.
- `app.version` : version de Codex.

#### Catalogue des métriques

Chaque métrique comprend les champs requis ainsi que les champs de contexte par défaut ci-dessus. Les noms de métriques ci-dessous ne comportent pas le préfixe `codex.`.
La plupart des noms de métriques sont centralisés dans `codex-rs/otel/src/metrics/names.rs` ; les métriques propres à certaines fonctionnalités et émises en dehors de ce fichier figurent également ici.
Si une métrique comprend le champ `tool`, celui-ci indique l’outil interne utilisé (par exemple, `apply_patch` ou `shell`) et ne contient ni la commande shell réelle ni le patch que `codex` tente d’appliquer.

#### Exécution et transport du modèle

| Métrique                                          | Type      | Champs               | Description                                                  |
| ----------------------------------------------- | --------- | -------------------- | ------------------------------------------------------------ |
| `api_request`                                   | compteur   | `status`, `success`  | Nombre de requêtes API par statut HTTP et par résultat (réussite ou échec).        |
| `api_request.duration_ms`                       | histogramme | `status`, `success`  | Durée des requêtes API en millisecondes.                        |
| `sse_event`                                     | compteur   | `kind`, `success`    | Nombre d’événements SSE par type d’événement et par résultat (réussite ou échec).           |
| `sse_event.duration_ms`                         | histogramme | `kind`, `success`    | Durée de traitement des événements SSE en millisecondes.               |
| `websocket.request`                             | compteur   | `success`            | Nombre de requêtes WebSocket par résultat (réussite ou échec).                  |
| `websocket.request.duration_ms`                 | histogramme | `success`            | Durée des requêtes WebSocket en millisecondes.                  |
| `websocket.event`                               | compteur   | `kind`, `success`    | Nombre de messages/événements WebSocket par type et par résultat (réussite ou échec).   |
| `websocket.event.duration_ms`                   | histogramme | `kind`, `success`    | Durée de traitement des messages/événements WebSocket en millisecondes. |
| `responses_api_overhead.duration_ms`            | histogramme |                      | Mesure du surcoût temporel de Responses API à partir des réponses WebSocket.      |
| `responses_api_inference_time.duration_ms`      | histogramme |                      | Mesure du temps d’inférence de Responses API à partir des réponses WebSocket.     |
| `responses_api_engine_iapi_ttft.duration_ms`    | histogramme |                      | Mesure du délai avant le premier token côté IAPI du moteur Responses API.        |
| `responses_api_engine_service_ttft.duration_ms` | histogramme |                      | Mesure du délai avant le premier token côté service du moteur Responses API.     |
| `responses_api_engine_iapi_tbt.duration_ms`     | histogramme |                      | Mesure du délai entre les tokens côté IAPI du moteur Responses API.         |
| `responses_api_engine_service_tbt.duration_ms`  | histogramme |                      | Mesure du délai entre les tokens côté service du moteur Responses API.      |
| `transport.fallback_to_http`                    | compteur   | `from_wire_api`      | Nombre de basculements de WebSocket vers HTTP.                            |
| `remote_models.fetch_update.duration_ms`        | histogramme |                      | Durée de récupération des définitions des modèles distants.                      |
| `remote_models.load_cache.duration_ms`          | histogramme |                      | Durée de chargement du cache des modèles distants.                         |
| `startup_prewarm.duration_ms`                   | histogramme | `status`             | Durée du préchauffage au démarrage selon le résultat.                         |
| `startup_prewarm.age_at_first_turn_ms`          | histogramme | `status`             | Âge du préchauffage au démarrage lors de sa résolution par le premier tour réel.    |
| `cloud_requirements.fetch.duration_ms`          | histogramme |                      | Durée de récupération des exigences cloud gérées par l’espace de travail.         |
| `cloud_requirements.fetch_attempt`              | compteur   | Voir la note             | Tentatives de récupération des exigences cloud gérées par l’espace de travail.         |
| `cloud_requirements.fetch_final`                | compteur   | Voir la note             | Résultat final de la récupération des exigences cloud gérées par l’espace de travail.    |
| `cloud_requirements.load`                       | compteur   | `trigger`, `outcome` | Résultat du chargement des exigences cloud gérées par l’espace de travail.           |

La métrique `cloud_requirements.fetch_attempt` comprend les champs `trigger`, `attempt`, `outcome` et `status_code`. La métrique `cloud_requirements.fetch_final` comprend les champs `trigger`, `outcome`, `reason`, `attempt_count` et `status_code`.

#### Activité des tours et des outils

| Métrique                                 | Type      | Champs                                                                    | Description                                                                                                      |
| -------------------------------------- | --------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `turn.e2e_duration_ms`                 | histogramme |                                                                           | Durée de bout en bout d’un tour complet.                                                                                 |
| `turn.ttft.duration_ms`                | histogramme |                                                                           | Délai avant le premier token d’un tour.                                                                                  |
| `turn.ttfm.duration_ms`                | histogramme |                                                                           | Délai avant le premier élément de sortie du modèle pour un tour.                                                                      |
| `turn.network_proxy`                   | compteur   | `active`, `tmp_mem_enabled`                                               | Indique si le proxy réseau géré était actif pendant le tour.                                                       |
| `turn.memory`                          | compteur   | `read_allowed`, `feature_enabled`, `config_use_memories`, `has_citations` | Disponibilité de la lecture de la mémoire et utilisation des citations issues de la mémoire pour chaque tour.                                                     |
| `turn.tool.call`                       | histogramme | `tmp_mem_enabled`                                                         | Nombre d’appels d’outils pendant le tour.                                                                                |
| `turn.token_usage`                     | histogramme | `token_type`, `tmp_mem_enabled`                                           | Utilisation des tokens pour chaque tour, par type de token (`total`, `input`, `cached_input`, `output` ou `reasoning_output`).          |
| `tool.call`                            | compteur   | `tool`, `success`                                                         | Nombre d’invocations d’outils par nom d’outil et selon leur réussite ou leur échec.                                                          |
| `tool.call.duration_ms`                | histogramme | `tool`, `success`                                                         | Durée d’exécution des outils en millisecondes, par nom d’outil et par résultat.                                                |
| `tool.unified_exec`                    | compteur   | `tty`                                                                     | Appels de l’outil exec unifié par mode TTY.                                                                             |
| `approval.requested`                   | compteur   | `tool`, `approved`                                                        | Résultat d’une demande d’approbation d’outil (`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`). |
| `mcp.call`                             | compteur   | Voir la note                                                                  | Résultat de l’invocation d’un outil MCP.                                                                                      |
| `mcp.call.duration_ms`                 | histogramme | Voir la note                                                                  | Durée d’invocation d’un outil MCP.                                                                                    |
| `mcp.tools.list.duration_ms`           | histogramme | `cache`                                                                   | Durée d’obtention de la liste des outils MCP, y compris l’état de présence ou d’absence dans le cache.                                                          |
| `mcp.tools.fetch_uncached.duration_ms` | histogramme |                                                                           | Durée des récupérations d’outils MCP absents du cache.                                                                |
| `mcp.tools.cache_write.duration_ms`    | histogramme |                                                                           | Durée des écritures dans le cache des outils MCP des Applications Codex.                                                                    |
| `hooks.run`                            | compteur   | `hook_name`, `source`, `status`                                           | Nombre d’exécutions de hooks par nom de hook, source et statut.                                                                 |
| `hooks.run.duration_ms`                | histogramme | `hook_name`, `source`, `status`                                           | Durée d’exécution du hook en millisecondes.                                                                               |

Les métriques `mcp.call` et `mcp.call.duration_ms` incluent `status` ; les événements normalement émis pour les appels d’outil incluent également `tool`, ainsi que `connector_id` et `connector_name` lorsqu’ils sont disponibles. Les appels MCP bloqués des applications Codex peuvent émettre `mcp.call` avec uniquement `status`.

#### Fils, tâches et fonctionnalités

| Métrique                            | Type      | Champs                | Description                                                                      |
| --------------------------------- | --------- | --------------------- | -------------------------------------------------------------------------------- |
| `feature.state`                   | compteur   | `feature`, `value`    | Valeurs des fonctionnalités qui diffèrent des valeurs par défaut (une ligne émise pour chaque valeur différente).         |
| `status_line`                     | compteur   |                       | Session démarrée avec une ligne d’état configurée.                                   |
| `model_warning`                   | compteur   |                       | Avertissement envoyé au modèle.                                                       |
| `thread.started`                  | compteur   | `is_git`              | Nouveau fil créé, avec une étiquette indiquant si le répertoire de travail se trouve dans un dépôt Git.    |
| `conversation.turn.count`         | compteur   |                       | Tours utilisateur/assistant par fil, enregistrés à la fin du fil.              |
| `thread.fork`                     | compteur   | `source`              | Nouveau fil créé en forkant un fil existant.                                |
| `thread.rename`                   | compteur   |                       | Fil renommé.                                                                  |
| `thread.side`                     | compteur   | `source`              | Conversation parallèle créée.                                                       |
| `thread.skills.enabled_total`     | histogramme |                       | Nombre de Skills activés pour un nouveau fil.                                       |
| `thread.skills.kept_total`        | histogramme |                       | Nombre de Skills activés conservés après le rendu du prompt.                            |
| `thread.skills.truncated`         | histogramme |                       | Indique si le rendu des Skills a tronqué la liste des Skills activés (`1` ou `0`).          |
| `task.compact`                    | compteur   | `type`                | Nombre de compactages par type (`remote` ou `local`), manuels et automatiques compris. |
| `task.review`                     | compteur   |                       | Nombre de révisions déclenchées.                                                     |
| `task.undo`                       | compteur   |                       | Nombre d’actions d’annulation déclenchées.                                                |
| `task.user_shell`                 | compteur   |                       | Nombre d’actions de l’utilisateur dans le shell (`!` dans la TUI, par exemple).                       |
| `shell_snapshot`                  | compteur   | Voir la note              | Indique si la création d’un instantané du shell a réussi.                                       |
| `shell_snapshot.duration_ms`      | histogramme | `success`             | Temps nécessaire pour créer un instantané du shell.                                                   |
| `skill.injected`                  | compteur   | `status`, `skill`     | Résultats de l’injection de Skills, par Skill.                                               |
| `plugins.startup_sync`            | compteur   | `transport`, `status` | Tentatives de synchronisation au démarrage des plugins sélectionnés.                                            |
| `plugins.startup_sync.final`      | compteur   | `transport`, `status` | Résultat final de la synchronisation au démarrage des plugins sélectionnés.                                       |
| `multi_agent.spawn`               | compteur   | `role`                | Créations d’agents par rôle.                                                            |
| `multi_agent.resume`              | compteur   |                       | Reprises de l’exécution d’agents.                                                                   |
| `multi_agent.nickname_pool_reset` | compteur   |                       | Réinitialisations du pool de surnoms d’agents.                                                      |

La métrique `shell_snapshot` inclut `success` et, en cas d’échec, `failure_reason`.

#### Mémoire et état local

| Métrique                         | Type      | Champs                    | Description                                               |
| ------------------------------ | --------- | ------------------------- | --------------------------------------------------------- |
| `memory.phase1`                | compteur   | `status`                  | Nombre de tâches de la phase 1 de la mémoire selon le statut.                      |
| `memory.phase1.e2e_ms`         | histogramme |                           | Durée de bout en bout de la phase 1 de la mémoire.                   |
| `memory.phase1.output`         | compteur   |                           | Sorties écrites lors de la phase 1 de la mémoire.                           |
| `memory.phase1.token_usage`    | histogramme | `token_type`              | Utilisation des tokens lors de la phase 1 de la mémoire selon le type de token.                 |
| `memory.phase2`                | compteur   | `status`                  | Nombre de tâches de la phase 2 de la mémoire selon le statut.                      |
| `memory.phase2.e2e_ms`         | histogramme |                           | Durée de bout en bout de la phase 2 de la mémoire.                   |
| `memory.phase2.input`          | compteur   |                           | Nombre d’entrées de la phase 2 de la mémoire.                               |
| `memory.phase2.token_usage`    | histogramme | `token_type`              | Utilisation des tokens lors de la phase 2 de la mémoire selon le type de token.                 |
| `memories.usage`               | compteur   | `kind`, `tool`, `success` | Utilisation de la mémoire selon le type, l’outil et le résultat (réussite ou échec).          |
| `external_agent_config.detect` | compteur   | Voir la note                  | Configurations d’agents externes détectées par type d’élément de migration.  |
| `external_agent_config.import` | compteur   | Voir la note                  | Configurations d’agents externes importées par type d’élément de migration.     |
| `db.backfill`                  | compteur   | `status`                  | Résultats du remplissage initial de la base de données d’état (`upserted`, `failed`). |
| `db.backfill.duration_ms`      | histogramme | `status`                  | Durée du remplissage initial de la base de données d’état.                |
| `db.error`                     | compteur   | `stage`                   | Erreurs lors des opérations sur la base de données d’état.                        |

Les métriques `external_agent_config.detect` et `external_agent_config.import` incluent `migration_type` ; les migrations de Skills incluent également `skills_count`.

#### Bac à sable Windows

| Métrique                                           | Type      | Champs                                    | Description                                           |
| ------------------------------------------------ | --------- | ----------------------------------------- | ----------------------------------------------------- |
| `windows_sandbox.setup_success`                  | compteur   | `originator`, `mode`                      | Configurations réussies du bac à sable Windows.                      |
| `windows_sandbox.setup_failure`                  | compteur   | `originator`, `mode`                      | Échecs de configuration du bac à sable Windows.                       |
| `windows_sandbox.setup_duration_ms`              | histogramme | `result`, `originator`, `mode`            | Durée de configuration du bac à sable Windows.                       |
| `windows_sandbox.elevated_setup_success`         | compteur   |                                           | Configurations réussies du bac à sable Windows avec privilèges élevés.             |
| `windows_sandbox.elevated_setup_failure`         | compteur   | Voir la note                                  | Échecs de configuration du bac à sable Windows avec privilèges élevés.              |
| `windows_sandbox.elevated_setup_canceled`        | compteur   | Voir la note                                  | Tentatives annulées de configuration du bac à sable Windows avec privilèges élevés.     |
| `windows_sandbox.elevated_setup_duration_ms`     | histogramme | `result`                                  | Durée de configuration du bac à sable Windows avec privilèges élevés.              |
| `windows_sandbox.elevated_prompt_shown`          | compteur   |                                           | Invite de configuration du bac à sable avec privilèges élevés affichée.                  |
| `windows_sandbox.elevated_prompt_accept`         | compteur   |                                           | Invite de configuration du bac à sable avec privilèges élevés acceptée.               |
| `windows_sandbox.elevated_prompt_use_legacy`     | compteur   |                                           | L’utilisateur a choisi l’ancien bac à sable dans l’invite de configuration avec privilèges élevés.   |
| `windows_sandbox.elevated_prompt_quit`           | compteur   |                                           | L’utilisateur a quitté depuis l’invite de configuration avec privilèges élevés.                   |
| `windows_sandbox.fallback_prompt_shown`          | compteur   |                                           | Invite de repli du bac à sable affichée.                        |
| `windows_sandbox.fallback_retry_elevated`        | compteur   |                                           | L’utilisateur a relancé la configuration avec élévation des privilèges depuis l’invite de repli. |
| `windows_sandbox.fallback_use_legacy`            | compteur   |                                           | L’utilisateur a choisi l’ancien bac à sable depuis l’invite de repli.   |
| `windows_sandbox.fallback_prompt_quit`           | compteur   |                                           | L’utilisateur a choisi de quitter depuis l’invite de repli.                   |
| `windows_sandbox.legacy_setup_preflight_failed`  | compteur   | Voir la note                                  | Échec de la vérification préalable à la configuration de l’ancien bac à sable Windows.       |
| `windows_sandbox.setup_elevated_sandbox_command` | compteur   |                                           | Commande de configuration du bac à sable avec élévation des privilèges appelée.               |
| `windows_sandbox.createprocessasuserw_failed`    | compteur   | `error_code`, `path_kind`, `exe`, `level` | Échecs de `CreateProcessAsUserW` sous Windows.              |

Les métriques d’échec de la configuration avec élévation des privilèges incluent `code` et `message` lorsque les détails des échecs de configuration sous Windows sont disponibles, et peuvent inclure `originator` lorsqu’elles sont émises depuis le chemin de configuration partagé. La métrique `windows_sandbox.legacy_setup_preflight_failed` inclut `originator` lorsqu’elle est émise depuis le chemin de configuration partagé, mais les échecs de vérification préalable issus de l’invite de repli peuvent ne comporter aucun champ.

### Gestion des commentaires

Par défaut, les clients locaux permettent aux utilisateurs d’envoyer des commentaires depuis `/feedback`. Pour désactiver la collecte des commentaires dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE sur une machine, mettez à jour votre configuration :

```toml
[feedback]
enabled = false

Lorsque la collecte est désactivée, `/feedback` affiche un message indiquant que la fonctionnalité est désactivée et Codex rejette l’envoi de commentaires.

### Masquer ou afficher les événements de raisonnement

Pour réduire les sorties de « raisonnement » parasites, par exemple dans les journaux de CI, vous pouvez les masquer :

```toml
hide_agent_reasoning = true

Pour afficher le contenu brut du raisonnement lorsqu’un modèle en émet :

```toml
show_raw_agent_reasoning = true

N’activez l’affichage du raisonnement brut que s’il convient à votre workflow. Certains modèles ou fournisseurs, comme `gpt-oss`, n’émettent pas de raisonnement brut ; dans ce cas, ce paramètre n’a aucun effet visible.

## Notifications

Utilisez `notify` pour déclencher un programme externe chaque fois que Codex émet un événement pris en charge (actuellement, uniquement `agent-turn-complete`). Cette option est pratique pour les notifications de bureau, les webhooks de messagerie, les mises à jour de CI ou toute alerte par canal secondaire non couverte par les notifications intégrées de la TUI.

```toml
notify = ["python3", "/path/to/notify.py"]

Exemple de `notify.py` (tronqué) qui réagit à `agent-turn-complete` :

```python
#!/usr/bin/env python3

def main() -> int:
    notification = json.loads(sys.argv[1])
    if notification.get("type") != "agent-turn-complete":
        return 0
    title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
    message = " ".join(notification.get("input-messages", []))
    subprocess.check_output([
        "terminal-notifier",
        "-title", title,
        "-message", message,
        "-group", "codex-" + notification.get("thread-id", ""),
        "-activate", "com.googlecode.iterm2",
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())

Le script reçoit un seul argument JSON. Les champs courants sont notamment :

- `type` (actuellement `agent-turn-complete`)
- `thread-id` (identifiant de session)
- `turn-id` (identifiant du tour)
- `cwd` (répertoire de travail)
- `input-messages` (messages de l’utilisateur à l’origine du tour)
- `last-assistant-message` (texte du dernier message de l’assistant)

Placez le script à l’emplacement de votre choix sur le disque et faites pointer `notify` vers celui-ci.

#### `notify` ou `tui.notifications`

- `notify` exécute un programme externe (adapté aux webhooks, aux outils de notification de bureau et aux hooks de CI).
- `tui.notifications` est intégré à la TUI et peut éventuellement filtrer selon le type d’événement (par exemple, `agent-turn-complete` et `approval-requested`).
- `tui.notification_method` détermine comment la TUI émet les notifications du terminal (`auto`, `osc9` ou `bel`).
- `tui.notification_condition` détermine si les notifications de la TUI se déclenchent uniquement lorsque
  le terminal n’a pas le focus (`unfocused`) ou systématiquement (`always`).

En mode `auto`, Codex privilégie les notifications OSC 9 (une séquence d’échappement de terminal que certains terminaux interprètent comme une notification de bureau) et utilise BEL (`\x07`) à défaut.

Pour connaître les clés exactes, consultez la [Référence de configuration](/fr-FR/codex/config-file/config-reference).

## Persistance de l’historique

Par défaut, Codex enregistre les transcriptions locales des sessions sous `CODEX_HOME` (par exemple, `~/.codex/history.jsonl`). Pour désactiver la persistance locale de l’historique :

```toml
[history]
persistence = "none"

Pour limiter la taille du fichier d’historique, définissez `history.max_bytes`. Lorsque le fichier dépasse cette limite, Codex supprime les entrées les plus anciennes et compacte le fichier tout en conservant les enregistrements les plus récents.

```toml
[history]
max_bytes = 104857600 # 100 MiB

## Références cliquables

Si vous utilisez une intégration au terminal ou à l’éditeur compatible, Codex peut afficher les références aux fichiers sous forme de liens cliquables. Configurez `file_opener` pour choisir le schéma d’URI utilisé par Codex :

```toml
file_opener = "vscode" # or cursor, windsurf, vscode-insiders, none

Exemple : une référence telle que `/home/user/project/main.py:42` peut être convertie en lien `vscode://file/...:42` cliquable.

## Détection des instructions du projet

Codex lit `AGENTS.md` (et les fichiers associés) et inclut une quantité limitée de consignes propres au projet dans le premier tour d’une session. Deux paramètres contrôlent ce fonctionnement :

- `project_doc_max_bytes` : quantité de contenu à lire dans chaque fichier `AGENTS.md`
- `project_doc_fallback_filenames` : noms de fichiers supplémentaires à rechercher lorsqu’un répertoire ne contient pas de fichier `AGENTS.md`

Pour une procédure détaillée, consultez [Instructions personnalisées avec AGENTS.md](/fr-FR/codex/agent-configuration/agents-md).

## Application de bureau

Les options de cette section s’appliquent uniquement à l’application de bureau ChatGPT.

### Ajoutez des gestionnaires de fichiers personnalisés

Dans votre fichier de configuration utilisateur `~/.codex/config.toml`, ajoutez des entrées sous
`desktop.custom_file_handlers` afin d’ouvrir des fichiers dans des éditeurs ou des lanceurs internes
que l’application de bureau ChatGPT ne prend pas en charge par défaut. Chaque entrée ajoute une
cible d’éditeur aux menus **Ouvrir dans** de l’application. L’application affiche la cible lorsque
la valeur de `command` est un chemin absolu existant ou peut être résolue à l’aide de la variable `PATH` de l’application.

L’exemple suivant présente trois façons de transmettre un fichier à un gestionnaire :

```toml
# Append the opened path directly after the command.
[desktop.custom_file_handlers.vscodium]
label = "VSCodium"
icon = "/Users/you/.codex/icons/vscodium.png"
command = "codium"

# Place fixed arguments before the opened path.
[desktop.custom_file_handlers.textedit]
label = "TextEdit"
icon = "/Users/you/.codex/icons/textedit.png"
command = "/usr/bin/open"
args = ["-a", "TextEdit"]

# Append one JSON argument with the path and editor context.
[desktop.custom_file_handlers.company_editor]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"
input = "json_argument"

Enregistrez `config.toml`, puis redémarrez l’application de bureau ChatGPT.

L’identifiant du gestionnaire est le dernier segment de l’en-tête de table TOML. Il doit contenir
de 1 à 64 caractères, commencer par une lettre ou un chiffre ASCII et ne contenir par ailleurs
que des lettres et des chiffres ASCII, des points, des tirets bas ou des traits d’union. L’application ajoute
le préfixe `custom:` à l’identifiant ; par exemple, `company_editor` devient
`custom:company_editor`. Mettez entre guillemets tout identifiant contenant un point pour éviter que TOML ne
l’interprète comme une table imbriquée. Par exemple :

```toml
[desktop.custom_file_handlers."company.editor"]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"

Chaque gestionnaire prend en charge les champs suivants :

| Champ          | Obligatoire | Description                                                                                                                                                              |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `label`        | Oui      | Nom d’affichage dans l’application.                                                                                                                                                 |
| `icon`         | Oui      | Icône d’application intégrée telle que `apps/vscode.png`, URL `data:image/...` en base64, URI `file:` ou chemin absolu vers une image locale. Si la source n’est pas prise en charge, l’icône VS Code par défaut est utilisée. |
| `command`      | Oui      | Chemin de l’exécutable ou nom de la commande à détecter et à lancer.                                                                                                                    |
| `args`         | Non       | Tableau de chaînes de caractères inséré entre `command` et le fichier fourni en entrée. Valeur par défaut : `[]`.                                                                                            |
| `input`        | Non       | Mode de transmission du fichier par l’application : `path`, `json_argument` ou `json_stdin`. Valeur par défaut : `path`.                                                                              |
| `supports_ssh` | Non       | Indique si le gestionnaire doit être proposé pour les fichiers des espaces de travail SSH. Valeur par défaut : `false`. Utilisez `json_stdin` lorsque le gestionnaire a besoin d’informations sur l’hôte distant et le chemin.                     |

La valeur `input` détermine ce qui suit `args` :

- `path` ajoute le chemin comme dernier argument de la commande.
- `json_argument` ajoute un objet JSON contenant `target`, `path`, `appPath` et
`location`. La valeur `location` est soit un objet contenant les valeurs `line` et
`column` indexées à partir de 1, soit `null`.
- `json_stdin` écrit l’objet JSON sur l’entrée standard au lieu d’ajouter un
  argument. Cet objet contient également `hostConfig`, `remoteWorkspaceRoot` et
`remotePath` ; ces champs valent `null` lorsqu’ils ne s’appliquent pas.

Par exemple, `company_editor` peut recevoir cet argument lorsque l’utilisateur ouvre un
emplacement précis dans le code source :

```json
{
  "target": "custom:company_editor",
  "path": "/repo/src/index.ts",
  "appPath": null,
  "location": { "line": 12, "column": 3 }
}

Le choix d’un gestionnaire personnalisé comme éditeur préféré est conservé de la même
manière que celui d’un éditeur intégré, y compris dans les préférences propres à chaque projet.

## Options de la TUI

L’exécution de `codex` sans sous-commande lance l’interface utilisateur interactive du terminal (TUI). Codex propose plusieurs options de configuration propres à la TUI sous `[tui]`, notamment :

- `tui.notifications` : activez ou désactivez les notifications (ou limitez-les à certains types)
- `tui.notification_method` : choisissez `auto`, `osc9` ou `bel` pour les notifications du terminal
- `tui.notification_condition` : choisissez `unfocused` ou `always` pour déterminer quand
  les notifications se déclenchent
- `tui.animations` : activez ou désactivez les animations ASCII et les effets de scintillement
- `tui.alternate_screen` : contrôlez l’utilisation de l’écran alternatif (utilisez `never` pour conserver l’historique de défilement du terminal)
- `tui.show_tooltips` : affichez ou masquez les infobulles de prise en main sur l’écran d’accueil

`tui.notification_method` a pour valeur par défaut `auto`. En mode `auto`, Codex privilégie les notifications OSC 9 (une séquence d’échappement interprétée par certains terminaux comme une notification de bureau) lorsque le terminal semble les prendre en charge ; sinon, il utilise BEL (`\x07`).

Consultez la [Référence de configuration](/fr-FR/codex/config-file/config-reference) pour obtenir la liste complète des clés.
