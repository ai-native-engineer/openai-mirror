<!-- source: https://learn.chatgpt.com/fr-FR/docs/web-search -->

ChatGPT intègre son propre outil de recherche web. Considérez tous les résultats web comme
des données non fiables.

Dans l’application de bureau ChatGPT, demandez des informations à jour dans une discussion. ChatGPT consigne
l’activité de recherche avec les autres appels d’outils dans la transcription.

Dans ChatGPT sur le Web, demandez des informations à jour ou des sources. Les résultats de recherche et
les citations apparaissent dans la discussion lorsque ChatGPT utilise la recherche web. Les paramètres de l’espace de travail
peuvent limiter la disponibilité de la recherche.

Dans la CLI, utilisez `--search` pour récupérer des résultats en direct pour une seule exécution :

```bash
codex --search "Summarize the latest release notes for this dependency"

Les recherches apparaissent sous forme d’éléments `web_search` dans la transcription interactive et dans
la sortie de `codex exec --json`.

Dans l’extension IDE, demandez à Codex d’effectuer une recherche pendant que vous travaillez dans l’éditeur. Cette
extension utilise le mode de recherche de l’hôte Codex connecté. L’activité de recherche apparaît
dans la transcription de la discussion.

## Configuration de la recherche web locale

Dans les discussions Codex en local, Codex active par défaut la recherche en cache. Ce mode utilise
un index tenu à jour par OpenAI au lieu de récupérer en direct des pages web quelconques, ce qui
réduit le risque d’attaque par injection de prompt sans toutefois l’éliminer.

La recherche web est un outil hébergé, indépendant de l’accès réseau des commandes locales exécutées dans un bac à sable.
Elle n’utilise ni le proxy réseau ni la liste des domaines autorisés du profil d’autorisations, et
peut rester disponible lorsque l’accès réseau des commandes est désactivé. Configurez
la recherche, selon vos besoins, avec `web_search`, `tools.web_search.allowed_domains` et le paramètre géré
`allowed_web_search_modes`. Les filtres de domaines de recherche ne limitent pas
le trafic des commandes locales, des applications, des connecteurs ni des serveurs MCP.

Utilisez la recherche en direct lorsque votre tâche dépend des informations les plus récentes. Définissez
`web_search = "live"` dans `config.toml`. Définissez `web_search = "disabled"` pour
désactiver l’outil. Le mode `"indexed"` n’autorise l’accès au web externe que lorsque
l’index de recherche contrôle la requête. Lorsque Codex s’exécute avec un accès complet, la recherche web
utilise par défaut les résultats en direct. Consultez [Principes de configuration](/fr-FR/codex/config-file/config-basic)
pour connaître l’emplacement des fichiers de configuration et leur ordre de priorité.

### Recherche avec un fournisseur de modèles personnalisé

Un fournisseur de modèles personnalisé peut opter pour la recherche web autonome s’il prend en charge
un point de terminaison de recherche compatible :

```toml
model_provider = "custom"
web_search = "live"

[model_providers.custom]
name = "Custom Responses provider"
base_url = "https://example.com/v1"
env_key = "CUSTOM_RESPONSES_API_KEY"
supports_standalone_web_search = true

Par défaut, les fournisseurs personnalisés utilisent `supports_standalone_web_search = false`.
La recherche web autonome est encore en cours de développement et est désactivée par défaut.
Configurer cette capacité du fournisseur n’active pas la fonctionnalité : le fournisseur,
le modèle sélectionné et l’environnement d’exécution doivent également prendre en charge la recherche autonome. Les restrictions de recherche propres à l’espace de travail et
celles gérées de façon centralisée continuent de s’appliquer.

Pour connaître les limites réseau applicables aux environnements cloud Codex, consultez [Accès à
Internet](/fr-FR/codex/cloud/internet-access).
