<!-- source: https://learn.chatgpt.com/fr-FR/docs/config-file/config-reference -->

Utilisez cette page comme référence pour rechercher des informations sur les fichiers de configuration de Codex. Pour comprendre les concepts et consulter des exemples, commencez par les pages [Principes de configuration](/fr-FR/codex/config-file/config-basic) et [Configuration avancée](/fr-FR/codex/config-file/config-advanced).

## `config.toml`

La configuration utilisateur se trouve dans `~/.codex/config.toml`. Vous pouvez également redéfinir certains paramètres pour un projet dans des fichiers `.codex/config.toml`. Codex ne charge les fichiers de configuration propres au projet que si vous faites confiance au projet.

La configuration propre au projet ne peut pas redéfinir les clés locales à la machine relatives au fournisseur, à l’authentification,
aux métadonnées de requêtes d’applications gérées par l’hôte, aux notifications, à la sélection du profil de configuration
ou au routage de la télémétrie. Codex ignore `openai_base_url`,
`chatgpt_base_url`, `apps_mcp_product_sku`, `model_provider`,
`model_providers`, `notify`, `profile`, `profiles`,
`experimental_realtime_ws_base_url` et `otel` lorsqu’elles figurent dans un fichier
`.codex/config.toml` propre au projet ; définissez plutôt les clés de fournisseur, de notification et de télémétrie
dans la configuration utilisateur. Les [fichiers de profil](/fr-FR/codex/config-file/config-advanced#profiles) de configuration se trouvent à côté de
`config.toml` sous la forme `$CODEX_HOME/profile-name.config.toml` ; sélectionnez-en un avec
`--profile profile-name`.

Pour les clés relatives au bac à sable et aux approbations (`approval_policy`, `sandbox_mode` et `sandbox_workspace_write.*`), consultez également [Bac à sable et approbations](/fr-FR/codex/agent-approvals-security#sandbox-and-approvals), [Chemins protégés dans les racines accessibles en écriture](/fr-FR/codex/agent-approvals-security#protected-paths-in-writable-roots) et [Accès réseau](/fr-FR/codex/agent-approvals-security#network-access). Pour les profils d’autorisations en version bêta, consultez [Autorisations](/fr-FR/codex/permissions).

<ConfigTable
  options={[
    {
      key: "model",
      type: "string",
      description: "Modèle à utiliser (par exemple, `gpt-5.5`).",
    },
    {
      key: "review_model",
      type: "string",
      description:
        "Modèle de remplacement facultatif utilisé par `/review` (par défaut, le modèle de la session en cours).",
    },
    {
      key: "model_provider",
      type: "string",
      description: "Identifiant du fournisseur défini dans `model_providers` (valeur par défaut : `openai`).",
    },
    {
      key: "openai_base_url",
      type: "string",
      description:
        "URL de base personnalisée pour le fournisseur de modèles `openai` intégré.",
    },
    {
      key: "model_context_window",
      type: "number",
      description: "Nombre de tokens disponibles dans la fenêtre de contexte du modèle actif.",
    },
    {
      key: "model_auto_compact_token_limit",
      type: "number",
      description:
        "Seuil de tokens qui déclenche le compactage automatique de l’historique (s’il n’est pas défini, les valeurs par défaut du modèle sont utilisées).",
    },
    {
      key: "model_auto_compact_token_limit_scope",
      type: "total | body_after_prefix",
      description:
        "Détermine si le seuil de compactage automatique comptabilise tout le contexte actif (`total`, valeur par défaut) ou uniquement l’augmentation du contexte après le préfixe conservé de la fenêtre de compactage (`body_after_prefix`).",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description:
        "Chemin facultatif vers un catalogue de modèles au format JSON chargé au démarrage. Le fichier de profil sélectionné `$CODEX_HOME/profile-name.config.toml` peut redéfinir cette valeur pour le profil concerné.",
    },
    {
      key: "oss_provider",
      type: "lmstudio | ollama",
      description:
        "Fournisseur local par défaut utilisé lors de l’exécution avec `--oss` (s’il n’est pas défini, Codex vous demande de le choisir).",
    },
    {
      key: "approval_policy",
      type: "untrusted | on-request | never | { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }",
      description:
        "Détermine quand Codex se met en pause pour demander une approbation avant d’exécuter des commandes. Vous pouvez également utiliser `approval_policy = { granular = { ... } }` pour autoriser l’affichage de certaines catégories de demandes ou les rejeter automatiquement, tout en gardant les autres demandes interactives. `on-failure` est obsolète ; utilisez `on-request` pour les exécutions interactives ou `never` pour les exécutions non interactives.",
    },
    {
      key: "approval_policy.granular.sandbox_approval",
      type: "boolean",
      description:
        "Lorsque la valeur est `true`, les demandes d’approbation liées à l’élévation des autorisations du bac à sable peuvent s’afficher.",
    },
    {
      key: "approval_policy.granular.rules",
      type: "boolean",
      description:
        "Lorsque la valeur est `true`, les demandes d’approbation déclenchées par les règles `prompt` d’execpolicy peuvent s’afficher.",
    },
    {
      key: "approval_policy.granular.mcp_elicitations",
      type: "boolean",
      description:
        "Lorsque la valeur est `true`, les demandes d’élicitation MCP peuvent s’afficher au lieu d’être rejetées automatiquement.",
    },
    {
      key: "approval_policy.granular.request_permissions",
      type: "boolean",
      description:
        "Lorsque la valeur est `true`, les demandes de l’outil `request_permissions` peuvent s’afficher.",
    },
    {
      key: "approval_policy.granular.skill_approval",
      type: "boolean",
      description:
        "Lorsque la valeur est `true`, les demandes d’approbation des scripts de skill peuvent s’afficher.",
    },
    {
      key: "approvals_reviewer",
      type: "user | auto_review",
      description:
        "Détermine qui examine les demandes d’approbation admissibles dans le cadre des stratégies `on-request` ou des stratégies d’approbation granulaires. Valeur par défaut : `user` ; `auto_review` utilise le sous-agent de révision. Ce paramètre ne modifie pas le fonctionnement du bac à sable et ne soumet pas à révision les actions qui y sont déjà autorisées.",
    },
    {
      key: "auto_review.policy",
      type: "string",
      description:
        "Instructions locales en Markdown définissant les règles de révision automatique. Le paramètre géré `guardian_policy_config` est prioritaire. Les valeurs vides sont ignorées.",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description:
        "Autorisez les outils reposant sur un shell à utiliser la sémantique des shells de connexion. Valeur par défaut : `true` ; avec `false`, les requêtes `login = true` sont rejetées et, si `login` est omis, les shells utilisés par défaut ne sont pas des shells de connexion.",
    },
    {
      key: "sandbox_mode",
      type: "read-only | workspace-write | danger-full-access",
      description:
        "Stratégie du bac à sable pour l’accès au système de fichiers et au réseau lors de l’exécution des commandes.",
    },
    {
      key: "sandbox_workspace_write.writable_roots",
      type: "array<string>",
      description:
        "Racines supplémentaires accessibles en écriture lorsque `sandbox_mode = \"workspace-write\"`.",
    },
    {
      key: "sandbox_workspace_write.network_access",
      type: "boolean",
      description:
        "Autorisez l’accès réseau sortant dans le bac à sable workspace-write.",
    },
    {
      key: "sandbox_workspace_write.exclude_tmpdir_env_var",
      type: "boolean",
      description:
        "Excluez `$TMPDIR` des racines accessibles en écriture en mode workspace-write.",
    },
    {
      key: "sandbox_workspace_write.exclude_slash_tmp",
      type: "boolean",
      description:
        "Excluez `/tmp` des racines accessibles en écriture en mode workspace-write.",
    },
    {
      key: "windows.sandbox",
      type: "unelevated | elevated",
      description:
        "Mode de bac à sable natif réservé à Windows lorsque Codex s’exécute nativement sur Windows.",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "Lors d’une exécution native sur Windows, exécutez par défaut le processus enfant final placé en bac à sable sur un bureau privé. Définissez `false` uniquement pour assurer la compatibilité avec l’ancien comportement `Winsta0\\\\Default`.",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "Définissez la valeur sur `false` pour restreindre l’accès à l’historique de navigation. Les exigences gérées peuvent imposer cette restriction.",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "Restrictions par défaut pour les origines du navigateur. Prend en charge `access`, `uploads`, `downloads` et `full_cdp_access`, chacun défini sur `allow` ou `deny`.",
    },
    {
      key: "browser_use.origins.<origin>",
      type: "table",
      description:
        "Restrictions du navigateur par origine, avec les mêmes champs que `browser_use.default_origin_policy`. Incluez un schéma HTTP ou HTTPS et, éventuellement, un port ; omettez les chemins, les paramètres de requête et les fragments. Les valeurs locales ne peuvent pas assouplir les interdictions gérées.",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "Stratégie d’accès par défaut aux applications natives pour la fonctionnalité Utilisation de l’ordinateur. Les entrées propres à chaque application peuvent définir une stratégie ; la configuration locale ne peut pas assouplir les restrictions gérées.",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description: "Accès aux applications natives macOS, avec l’identifiant de bundle comme clé.",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "Accès aux applications Windows empaquetées, avec l’Application User Model ID (AUMID) comme clé.",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Règles d’accès aux exécutables Windows. Chaque règle exige `publisher_name`, `product_name` et `access` (`allow` ou `deny`) ; `binary_name` est facultatif.",
    },
    {
      key: "computer_use.windows.always_allowed_app_ids",
      type: "array<string>",
      description:
        "Identifiants des applications Windows que la fonctionnalité Utilisation de l’ordinateur peut ouvrir sans demander d’approbation. Les applications absentes de cette liste nécessitent une approbation ; supprimez les entrées enregistrées dans les paramètres de la fonctionnalité Utilisation de l’ordinateur de l’application de bureau ChatGPT.",
    },
    {
      key: "notify",
      type: "array<string>",
      description:
        "Commande exécutée pour les notifications ; elle reçoit une charge utile JSON de Codex.",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description:
        "Recherchez les mises à jour de Codex au démarrage (utilisez la valeur false uniquement si les mises à jour sont gérées de manière centralisée).",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "Activez l’envoi de commentaires via `/feedback` dans tous les clients locaux (valeur par défaut : true).",
    },
    {
      key: "analytics.enabled",
      type: "boolean",
      description:
        "Activez ou désactivez la collecte de données analytiques pour cette machine ou ce profil. Si ce paramètre n’est pas défini, la valeur par défaut du client s’applique.",
    },
    {
      key: "instructions",
      type: "string",
      description:
        "Réservé à un usage futur ; utilisez plutôt `model_instructions_file` ou `AGENTS.md`.",
    },
    {
      key: "developer_instructions",
      type: "string",
      description:
        "Instructions de développeur supplémentaires injectées dans la session (facultatives).",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description:
        "Répertoire dans lequel Codex écrit les fichiers journaux ; par défaut, `$CODEX_HOME/log`. Définir explicitement ce paramètre active également le journal TUI facultatif en texte brut `codex-tui.log` dans ce répertoire.",
    },
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Répertoire dans lequel Codex stocke la base de données d’état SQLite utilisée pour les tâches d’agents et les autres états d’exécution permettant une reprise.",
    },
    {
      key: "compact_prompt",
      type: "string",
      description: "Prompt de remplacement pour le compactage de l’historique, défini directement dans la configuration.",
    },
    {
      key: "model_instructions_file",
      type: "string (path)",
      description:
        "Instructions qui remplacent les instructions intégrées, à utiliser à la place de `AGENTS.md`.",
    },
    {
      key: "personality",
      type: "none | friendly | pragmatic",
      description:
        "Style de communication par défaut des modèles qui déclarent la capacité `supportsPersonality` ; peut être redéfini pour chaque fil de discussion ou tour, ou via `/personality`.",
    },
    {
      key: "service_tier",
      type: "string",
      description:
        "Offre privilégiée pour les nouveaux tours. Utilisez `fast` ou une autre offre déclarée par le modèle actif ; `fast` correspond à la valeur de requête `priority`.",
    },
    {
      key: "experimental_compact_prompt_file",
      type: "string (path)",
      description:
        "Chargez le prompt de remplacement pour le compactage depuis un fichier (expérimental).",
    },
    {
      key: "skills.max_context_tokens",
      type: "integer (positive)",
      description:
        "Budget de tokens pour le catalogue des skills disponibles. Par défaut, 2 % de la fenêtre de contexte du modèle. Les valeurs définies explicitement sont plafonnées à `10000` tokens.",
    },
    {
      key: "skills.config",
      type: "array<object>",
      description: "Paramètres d’activation redéfinis pour chaque skill, stockés dans config.toml.",
    },
    {
      key: "skills.config.<index>.path",
      type: "string (path)",
      description: "Chemin vers un dossier de skill contenant `SKILL.md`.",
    },
    {
      key: "skills.config.<index>.enabled",
      type: "boolean",
      description: "Activez ou désactivez le skill référencé.",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "Activez ou désactivez une application ou un connecteur spécifique selon son identifiant (valeur par défaut : true).",
    },
    {
      key: "apps._default.enabled",
      type: "boolean",
      description:
        "État d’activation par défaut de toutes les applications, sauf si une autre valeur est définie pour une application.",
    },
    {
      key: "apps._default.destructive_enabled",
      type: "boolean",
      description:
        "Règle d’autorisation ou de refus appliquée par défaut aux outils d’application avec `destructive_hint = true`.",
    },
    {
      key: "apps._default.open_world_enabled",
      type: "boolean",
      description:
        "Règle d’autorisation ou de refus appliquée par défaut aux outils d’application avec `open_world_hint = true`.",
    },
    {
      key: "apps._default.approvals_reviewer",
      type: "user | auto_review",
      description:
        "Responsable par défaut de l’examen des demandes d’approbation des outils d’application, sauf si une autre valeur est définie pour l’application. Si ce paramètre est omis, les applications héritent de la valeur `approvals_reviewer` de premier niveau.",
    },
    {
      key: "apps._default.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportement d’approbation par défaut des outils d’application en l’absence de valeurs de remplacement propres à l’application ou à l’outil.",
    },
    {
      key: "apps.<id>.destructive_enabled",
      type: "boolean",
      description:
        "Autorisez ou bloquez les outils de cette application qui déclarent `destructive_hint = true`.",
    },
    {
      key: "apps.<id>.open_world_enabled",
      type: "boolean",
      description:
        "Autorisez ou bloquez les outils de cette application qui déclarent `open_world_hint = true`.",
    },
    {
      key: "apps.<id>.default_tools_enabled",
      type: "boolean",
      description:
        "État d’activation par défaut des outils de cette application, sauf si un outil dispose d’un paramètre spécifique.",
    },
    {
      key: "apps.<id>.approvals_reviewer",
      type: "user | auto_review",
      description:
        "Responsable de la révision des demandes d’approbation des outils de cette application. Remplace `apps._default.approvals_reviewer`.",
    },
    {
      key: "apps.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportement d’approbation par défaut des outils de cette application, sauf si un outil dispose d’un paramètre spécifique.",
    },
    {
      key: "apps.<id>.tools.<tool>.enabled",
      type: "boolean",
      description:
        "Paramètre d’activation spécifique à un outil de l’application (par exemple `repos/list`).",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "Comportement d’approbation spécifique à un outil de l’application.",
    },
    {
      key: "tool_suggest.discoverables",
      type: "array<table>",
      description:
        "Autorisez les suggestions d’outils pour des connecteurs ou plugins supplémentaires pouvant être découverts. Chaque entrée utilise `type = \"connector\"` ou `\"plugin\"` et un `id`.",
    },
    {
      key: "tool_suggest.disabled_tools",
      type: "array<table>",
      description:
        "Désactivez les suggestions pour certains connecteurs ou plugins pouvant être découverts. Chaque entrée utilise `type = \"connector\"` ou `\"plugin\"` et un `id`.",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "Activez les intégrations d’applications (connecteurs) (stables ; activées par défaut). Le trafic des applications et des connecteurs n’est pas contrôlé par le proxy réseau des commandes exécutées dans le bac à sable ni par sa liste de domaines autorisés.",
    },
    {
      key: "features.hooks",
      type: "boolean",
      description:
        "Activez les hooks de cycle de vie chargés depuis `hooks.json` ou configurés directement dans `[hooks]`. `features.codex_hooks` est un alias obsolète.",
    },
    {
      key: "features.code_mode.enabled",
      type: "boolean",
      description:
        "Activez la configuration du mode code. Cette fonctionnalité est en cours de développement et désactivée par défaut.",
    },
    {
      key: "features.code_mode.excluded_tool_namespaces",
      type: "array<string>",
      description:
        "Espaces de noms d’outils que le mode code exclut des consignes relatives aux appels d’outils imbriqués et ne rend pas accessibles à l’exécuteur.",
    },
    {
      key: "features.code_mode.direct_only_tool_namespaces",
      type: "array<string>",
      description:
        "Espaces de noms d’outils que le mode code peut utiliser uniquement au moyen d’appels directs à ces outils.",
    },
    {
      key: "features.context_management.experimental_mode",
      type: "boolean",
      description:
        "Activez la gestion expérimentale du contexte (désactivée par défaut). Au lieu de compresser à répétition le contexte en un seul résumé, elle utilise des notes et un historique consultable par recherche pour préserver les détails accumulés. Nécessite une connexion à ChatGPT avec un abonnement Plus, Pro ou Pro Lite.",
    },
    {
      key: "features.rollout_budget.enabled",
      type: "boolean",
      description:
        "Activez le suivi du budget d’exécution. Cette fonctionnalité est en cours de développement et désactivée par défaut. Lorsqu’elle est activée, `features.rollout_budget.limit_tokens` est obligatoire.",
    },
    {
      key: "features.rollout_budget.limit_tokens",
      type: "integer",
      description:
        "Limite strictement positive de tokens pour le suivi du budget d’exécution. Obligatoire lorsque le budget d’exécution est activé.",
    },
    {
      key: "features.rollout_budget.reminder_interval_tokens",
      type: "integer",
      description:
        "Intervalle strictement positif, exprimé en tokens, entre les rappels du budget d’exécution. Par défaut, il correspond à 10 % de `limit_tokens`, avec un minimum de 1 token.",
    },
    {
      key: "features.rollout_budget.sampling_token_weight",
      type: "number",
      description:
        "Multiplicateur fini, positif ou nul, appliqué aux tokens échantillonnés lors de la comptabilisation du budget d’exécution. Valeur par défaut : `1.0`.",
    },
    {
      key: "features.rollout_budget.prefill_token_weight",
      type: "number",
      description:
        "Multiplicateur fini, positif ou nul, appliqué aux tokens de préremplissage lors de la comptabilisation du budget d’exécution. Valeur par défaut : `1.0`.",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "Hooks de cycle de vie configurés directement dans `config.toml`. Ils utilisent le même schéma d’événements que `hooks.json` ; consultez le guide Hooks pour voir des exemples et les événements pris en charge.",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "Groupes de critères de correspondance pour les événements de hook tels que `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `UserPromptSubmit`, `Stop` ou `Interrupt`.",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "Gestionnaires de hooks pour un groupe de critères de correspondance. Les hooks de commande et d’outil MCP sont pris en charge, tandis que les gestionnaires de hooks de prompt et d’agent sont analysés, mais ne sont pas exécutés.",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "Exécutez un hook de commande en arrière-plan sans retarder l’opération qui le déclenche. Valeur par défaut : `false` ; `SessionEnd` s’exécute toujours de façon synchrone. Consultez [Exécutez les hooks en arrière-plan](/codex/hooks#run-hooks-in-the-background).",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "Seuil approximatif de tokens par gestionnaire au-delà duquel une valeur `additionalContext` trop volumineuse est enregistrée sur disque et un aperçu plus court est présenté au modèle. Valeur par défaut : `2500` ; `0` transmet directement le contexte complet au modèle. Consultez [Sorties volumineuses des hooks](/codex/hooks#large-hook-output).",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "Commande de remplacement propre à Windows pour les hooks de commande. L’alias TOML `command_windows` est également accepté.",
    },
    {
      key: "features.memories",
      type: "boolean",
      description:
        "Activez les [Mémoires](/codex/customization/memories) (désactivées par défaut).",
    },
    {
      key: "mcp_optional_startup_grace_ms",
      type: "integer (milliseconds)",
      description:
        "Délai d’attente commun aux serveurs MCP facultatifs lors de la constitution du catalogue initial d’outils. Valeur par défaut : `1000`. Définissez-le sur `0` pour utiliser à la place le délai `startup_timeout_sec` de chaque serveur.",
    },
    {
      key: "mcp_servers.<id>.command",
      type: "string",
      description: "Commande de lancement d’un serveur MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.args",
      type: "array<string>",
      description: "Arguments transmis à la commande du serveur MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.env",
      type: "map<string,string>",
      description: "Variables d’environnement transmises au serveur MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.env_vars",
      type: 'array<string | { name = string, source = "local" | "remote" }>',
      description:
        "Variables d’environnement supplémentaires à ajouter à la liste d’autorisation d’un serveur MCP stdio. Les entrées sous forme de chaîne utilisent par défaut `source = \"local\"` ; utilisez `source = \"remote\"` uniquement avec un serveur stdio distant pris en charge par un exécuteur.",
    },
    {
      key: "mcp_servers.<id>.cwd",
      type: "string",
      description: "Répertoire de travail du processus du serveur MCP stdio.",
    },
    {
      key: "mcp_servers.<id>.url",
      type: "string",
      description: "Point de terminaison d’un serveur MCP utilisant le transport streamable HTTP.",
    },
    {
      key: "mcp_servers.<id>.auth",
      type: "oauth | chatgpt",
      description:
        "Méthode d’authentification de secours pour un serveur MCP HTTP, utilisée après les tokens bearer et les en-têtes d’autorisation configurés. `oauth` (par défaut) utilise les identifiants OAuth MCP enregistrés lorsqu’ils sont disponibles. `chatgpt` utilise la session ChatGPT actuelle pour l’origine officielle de confiance de ChatGPT, puis se rabat sur les identifiants OAuth enregistrés. Les deux modes permettent de se connecter sans authentification si aucune source ne fournit d’identifiants.",
    },
    {
      key: "mcp_servers.<id>.oauth.client_id",
      type: "string",
      description:
        "Identifiant client OAuth préenregistré utilisé pour l’autorisation et l’échange de tokens avec ce serveur MCP.",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_url",
      type: "string",
      description:
        "URL de rappel OAuth propre au serveur. Les clients préenregistrés la réutilisent lorsque l’identification de l’émetteur est prise en charge ou que l’URL se termine déjà par l’identifiant de rappel propre au serveur. Sinon, Codex utilise l’URL de rappel globale ou par défaut en y ajoutant cet identifiant. Les clients sans identifiant préenregistré utilisent cette URL de rappel lors de leur enregistrement.",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_port",
      type: "integer",
      description:
        "Port d’écoute fixe pour le rappel OAuth de ce serveur MCP. Remplace `mcp_oauth_callback_port`. Pour un rappel direct sur l’interface de bouclage dont l’URL contient un port explicite, configurez le même port d’écoute.",
    },
    {
      key: "mcp_servers.<id>.bearer_token_env_var",
      type: "string",
      description:
        "Variable d’environnement qui fournit le token bearer d’un serveur MCP HTTP.",
    },
    {
      key: "mcp_servers.<id>.http_headers",
      type: "map<string,string>",
      description: "En-têtes HTTP statiques inclus dans chaque requête MCP HTTP.",
    },
    {
      key: "mcp_servers.<id>.http_headers_helper",
      type: "string (command)",
      description:
        "Commande locale qui affiche un objet JSON contenant les noms et les valeurs des en-têtes HTTP. Prise en charge uniquement pour les serveurs MCP HTTP connectés localement. Les tokens bearer explicites et les identifiants OAuth ont priorité sur les en-têtes Authorization fournis par la commande auxiliaire.",
    },
    {
      key: "mcp_servers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "En-têtes HTTP renseignés à partir de variables d’environnement pour un serveur MCP HTTP.",
    },
    {
      key: "mcp_servers.<id>.enabled",
      type: "boolean",
      description: "Désactivez un serveur MCP sans supprimer sa configuration.",
    },
    {
      key: "mcp_servers.<id>.required",
      type: "boolean",
      description:
        "Lorsque la valeur est true, le démarrage ou la reprise échoue si ce serveur MCP activé ne parvient pas à s’initialiser.",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_sec",
      type: "number",
      description:
        "Redéfinissez le délai d’expiration par défaut de 10 s au démarrage d’un serveur MCP.",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_ms",
      type: "number",
      description: "Alias de `startup_timeout_sec` exprimé en millisecondes.",
    },
    {
      key: "mcp_servers.<id>.tool_timeout_sec",
      type: "number",
      description:
        "Redéfinissez le délai d’expiration par défaut de 60 s applicable à chaque outil d’un serveur MCP.",
    },
    {
      key: "mcp_servers.<id>.enabled_tools",
      type: "array<string>",
      description: "Liste d’autorisation des noms d’outils exposés par le serveur MCP.",
    },
    {
      key: "mcp_servers.<id>.disabled_tools",
      type: "array<string>",
      description:
        "Liste de refus appliquée après `enabled_tools` pour le serveur MCP.",
    },
    {
      key: "mcp_servers.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportement d’approbation par défaut des outils MCP de ce serveur, sauf si un outil dispose d’un paramètre spécifique.",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportement d’approbation spécifique à un outil MCP de ce serveur.",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.output_token_limit",
      type: "integer (positive)",
      description:
        "Budget de tokens pour la sortie d’un outil MCP, avant la marge standard de 20 % prévue pour la sérialisation. Remplace, pour cet outil, le budget de troncature des sorties défini par défaut pour le modèle.",
    },
    {
      key: "mcp_servers.<id>.scopes",
      type: "array<string>",
      description:
        "Portées OAuth à demander lors de l’authentification auprès de ce serveur MCP.",
    },
    {
      key: "mcp_servers.<id>.oauth_resource",
      type: "string",
      description:
        "Paramètre de ressource OAuth facultatif, défini par la RFC 8707, à inclure lors de la connexion MCP.",
    },
    {
      key: "mcp_servers.<id>.experimental_environment",
      type: "local | remote",
      description:
        "Emplacement d’exécution expérimental d’un serveur MCP. `remote` démarre les serveurs stdio via un environnement d’exécution distant ; le placement distant des serveurs utilisant le transport streamable HTTP n’est pas implémenté.",
    },
    {
      key: "agents",
      type: "table",
      description:
        "Paramètres multi-agents et déclarations de rôles personnalisés. Les noms de paramètres scalaires sont réservés et ne peuvent pas servir de noms de rôles personnalisés.",
    },
    {
      key: "agents.enabled",
      type: "boolean",
      description: "Activez ou désactivez les outils multi-agents (valeur par défaut : true).",
    },
    {
      key: "agents.max_concurrent_threads_per_session",
      type: "number",
      description:
        "Nombre maximal de fils de discussion d’agents lancés pouvant être ouverts simultanément, sans compter le fil principal. Si ce paramètre n’est pas défini, Codex choisit la valeur par défaut.",
    },
    {
      key: "agents.max_threads",
      type: "number",
      description:
        "Ancien alias de `agents.max_concurrent_threads_per_session`.",
    },
    {
      key: "agents.default_subagent_model",
      type: "string",
      description:
        "Modèle par défaut des agents lancés. Un modèle spécifié explicitement au lancement est prioritaire.",
    },
    {
      key: "agents.default_subagent_reasoning_effort",
      type: "string",
      description:
        "Effort de raisonnement par défaut des agents lancés. Un effort spécifié explicitement au lancement est prioritaire.",
    },
    {
      key: "agents.interrupt_message",
      type: "boolean",
      description:
        "Enregistrez un message visible par le modèle lorsqu’un tour d’agent est interrompu (valeur par défaut : true).",
    },
    {
      key: "agents.<name>.description",
      type: "string",
      description:
        "Consignes relatives au rôle présentées à Codex lorsqu’il choisit et lance ce type d’agent.",
    },
    {
      key: "agents.<name>.config_file",
      type: "string (path)",
      description:
        "Chemin d’une couche de configuration TOML pour ce rôle ; les chemins relatifs sont résolus par rapport au fichier de configuration qui déclare le rôle.",
    },
    {
      key: "memories.generate_memories",
      type: "boolean",
      description:
        "Lorsque la valeur est `false`, les fils de discussion nouvellement créés ne sont pas conservés comme données d’entrée pour la génération de mémoires. Valeur par défaut : `true`.",
    },
    {
      key: "memories.use_memories",
      type: "boolean",
      description:
        "Lorsque la valeur est `false`, Codex n’injecte pas les mémoires existantes dans les sessions futures. Valeur par défaut : `true`.",
    },
    {
      key: "memories.disable_on_external_context",
      type: "boolean",
      description:
        "Lorsque cette option vaut `true`, les fils qui utilisent du contexte externe, comme des appels d’outils MCP, la recherche web ou la recherche d’outils, sont exclus de la génération de mémoires. Valeur par défaut : `false`. Ancien alias : `memories.no_memories_if_mcp_or_web_search`.",
    },
    {
      key: "memories.max_raw_memories_for_consolidation",
      type: "number",
      description:
        "Nombre maximal de mémoires brutes récentes conservées pour la consolidation globale. Valeur par défaut : `256`, plafonnée à `4096`.",
    },
    {
      key: "memories.max_unused_days",
      type: "number",
      description:
        "Nombre maximal de jours depuis la dernière utilisation d’une mémoire au-delà duquel elle n’est plus admissible à la consolidation. Valeur par défaut : `30`, bornée entre `0` et `365`.",
    },
    {
      key: "memories.max_rollout_age_days",
      type: "number",
      description:
        "Ancienneté maximale des fils pris en compte pour la génération de mémoires. Valeur par défaut : `30`, bornée entre `0` et `90`.",
    },
    {
      key: "memories.max_rollouts_per_startup",
      type: "number",
      description:
        "Nombre maximal de trajectoires candidates traitées à chaque passe de démarrage. Valeur par défaut : `16`, plafonnée à `128`.",
    },
    {
      key: "memories.min_rollout_idle_hours",
      type: "number",
      description:
        "Durée minimale d’inactivité avant qu’un fil soit pris en compte pour la génération de mémoires. Valeur par défaut : `6`, bornée entre `1` et `48`.",
    },
    {
      key: "memories.min_rate_limit_remaining_percent",
      type: "number",
      description:
        "Pourcentage minimal de quota restant requis dans les fenêtres de limite de débit de Codex avant le démarrage de la génération de mémoires. Valeur par défaut : `25`, bornée entre `0` et `100`.",
    },
    {
      key: "memories.extract_model",
      type: "string",
      description: "Modèle de remplacement facultatif pour l’extraction des mémoires de chaque fil.",
    },
    {
      key: "memories.consolidation_model",
      type: "string",
      description: "Modèle de remplacement facultatif pour la consolidation globale des mémoires.",
    },
    {
      key: "features.unified_exec",
      type: "boolean",
      description:
        "Utilisez l’outil exec unifié reposant sur un PTY (fonctionnalité stable ; activée par défaut sauf sur Windows).",
    },
    {
      key: "features.shell_snapshot",
      type: "boolean",
      description:
        "Enregistrez un instantané de l’environnement du shell pour accélérer les commandes répétées (fonctionnalité stable ; activée par défaut).",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description:
        "Activez les outils de collaboration multi-agent (`spawn_agent`, `send_input`, `resume_agent`, `wait_agent` et `close_agent`) (fonctionnalité stable ; activée par défaut).",
    },
    {
      key: "features.goals",
      type: "boolean",
      description:
        "Activez la persistance des objectifs et la poursuite automatique (fonctionnalité stable ; activée par défaut).",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description: "Activez le catalogue distant de plugins (fonctionnalité stable ; activée par défaut).",
    },
    {
      key: "features.personality",
      type: "boolean",
      description:
        "Activez les options de sélection de la personnalité (fonctionnalité stable ; activée par défaut).",
    },
    {
      key: "features.network_proxy",
      type: "boolean | table",
      description:
        "Démarrez le proxy réseau des commandes exécutées dans le bac à sable (fonctionnalité expérimentale ; désactivée par défaut). Cette option est nécessaire pour appliquer les règles de domaine des profils d’autorisations, sauf si des exigences `experimental_network` activées et gérées par un administrateur démarrent le proxy. Utilisez une table pour définir des options de stratégie propres à cette fonctionnalité, telles que `domains`. Ce proxy ne filtre pas la recherche web, les applications, MCP ni les autres outils hébergés.",
    },
    {
      key: "features.network_proxy.enabled",
      type: "boolean",
      description:
        "Démarrez le proxy réseau des commandes exécutées dans le bac à sable lorsque leur accès réseau est activé. Valeur par défaut : `false` ; les règles de domaine des profils d’autorisations ne sont pas appliquées lorsque le proxy est désactivé.",
    },
    {
      key: "features.network_proxy.domains",
      type: "map<string, allow | deny>",
      description:
        "Stratégie relative aux domaines pour l’accès réseau dans le bac à sable. Par défaut, aucune valeur n’est définie ; aucune destination externe n’est donc autorisée tant que vous n’ajoutez pas de règles `allow`. La stratégie accepte les noms d’hôte exacts, `*.example.com` uniquement pour les sous-domaines, `**.example.com` pour le domaine racine et ses sous-domaines, ainsi que les règles d’autorisation globales `*` ; privilégiez les règles ciblées, car `*` ouvre largement l’accès sortant au réseau public. Ajoutez des règles `deny` pour bloquer certaines destinations ; en cas de conflit, `deny` l’emporte.",
    },
    {
      key: "features.network_proxy.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "Stratégie relative aux sockets Unix pour l’accès réseau dans le bac à sable. Par défaut, aucune valeur n’est définie ; ajoutez des entrées `allow` pour les sockets autorisés.",
    },
    {
      key: "features.network_proxy.allow_local_binding",
      type: "boolean",
      description:
        "Autorisez un accès plus étendu aux réseaux locaux et privés. Valeur par défaut : `false` ; des règles d’autorisation ciblant exactement une adresse IP locale littérale ou `localhost` peuvent néanmoins autoriser des cibles locales précises.",
    },
    {
      key: "features.network_proxy.enable_socks5",
      type: "boolean",
      description: "Activez la prise en charge de SOCKS5. Valeur par défaut : `true`.",
    },
    {
      key: "features.network_proxy.enable_socks5_udp",
      type: "boolean",
      description: "Autorisez UDP via SOCKS5. Valeur par défaut : `true`.",
    },
    {
      key: "features.network_proxy.allow_upstream_proxy",
      type: "boolean",
      description:
        "Autorisez le chaînage avec un proxy en amont défini dans l’environnement. Valeur par défaut : `true`.",
    },
    {
      key: "features.network_proxy.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Autorisez les adresses d’écoute autres que celles de la boucle locale. Valeur par défaut : `false` ; l’activation de cette option peut rendre les points d’écoute du proxy accessibles au-delà de localhost.",
    },
    {
      key: "features.network_proxy.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Autorisez n’importe quelle destination de socket Unix au lieu de limiter l’accès à la liste d’autorisation. Valeur par défaut : `false` ; utilisez cette option uniquement dans des environnements strictement contrôlés.",
    },
    {
      key: "features.network_proxy.proxy_url",
      type: "string",
      description:
        "URL d’écoute HTTP pour l’accès réseau dans le bac à sable. Valeur par défaut : `\"http://127.0.0.1:3128\"`.",
    },
    {
      key: "features.network_proxy.socks_url",
      type: "string",
      description:
        "URL d’écoute SOCKS5. Valeur par défaut : `\"http://127.0.0.1:8081\"`.",
    },
    {
      key: "features.web_search",
      type: "boolean",
      description:
        "Ancienne option désormais obsolète ; préférez le paramètre de premier niveau `web_search`.",
    },
    {
      key: "features.web_search_cached",
      type: "boolean",
      description:
        "Ancienne option désormais obsolète. Lorsque `web_search` n’est pas défini, true équivaut à `web_search = \"cached\"`.",
    },
    {
      key: "features.web_search_request",
      type: "boolean",
      description:
        "Ancienne option désormais obsolète. Lorsque `web_search` n’est pas défini, true équivaut à `web_search = \"live\"`.",
    },
    {
      key: "features.shell_tool",
      type: "boolean",
      description:
        "Activez l’outil `shell` fourni par défaut pour exécuter des commandes (fonctionnalité stable ; activée par défaut).",
    },
    {
      key: "features.enable_request_compression",
      type: "boolean",
      description:
        "Compressez avec zstd les corps des requêtes en streaming lorsque cette compression est prise en charge (fonctionnalité stable ; activée par défaut).",
    },
    {
      key: "features.skill_mcp_dependency_install",
      type: "boolean",
      description:
        "Autorisez Codex à proposer l’installation des dépendances MCP manquantes pour les Skills et à les installer (fonctionnalité stable ; activée par défaut).",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "Activez dans la TUI la sélection d’une offre du catalogue de modèles, y compris les commandes de l’offre Rapide lorsque le modèle actif indique qu’il les prend en charge (fonctionnalité stable ; activée par défaut).",
    },
    {
      key: "features.prevent_idle_sleep",
      type: "boolean",
      description:
        "Empêchez la machine de se mettre en veille pendant l’exécution d’un tour (fonctionnalité expérimentale ; désactivée par défaut).",
    },
    {
      key: "suppress_unstable_features_warning",
      type: "boolean",
      description:
        "Masquez l’avertissement qui s’affiche lorsque des indicateurs de fonctionnalités en cours de développement sont activés.",
    },
    {
      key: "model_providers.<id>",
      type: "table",
      description:
        "Définition d’un fournisseur personnalisé. Les identifiants des fournisseurs intégrés (`openai`, `ollama` et `lmstudio`) sont réservés et ne peuvent pas être redéfinis.",
    },
    {
      key: "model_providers.<id>.name",
      type: "string",
      description: "Nom d’affichage d’un fournisseur de modèles personnalisé.",
    },
    {
      key: "model_providers.<id>.base_url",
      type: "string",
      description: "URL de base de l’API du fournisseur de modèles.",
    },
    {
      key: "model_providers.<id>.env_key",
      type: "string",
      description: "Variable d’environnement fournissant la clé API du fournisseur.",
    },
    {
      key: "model_providers.<id>.env_key_instructions",
      type: "string",
      description: "Instructions facultatives pour configurer la clé API du fournisseur.",
    },
    {
      key: "model_providers.<id>.experimental_bearer_token",
      type: "string",
      description:
        "Token bearer du fournisseur défini directement (déconseillé ; utilisez `env_key`).",
    },
    {
      key: "model_providers.<id>.requires_openai_auth",
      type: "boolean",
      description:
        "Le fournisseur utilise l’authentification OpenAI (valeur par défaut : false).",
    },
    {
      key: "model_providers.<id>.wire_api",
      type: "responses",
      description:
        "Protocole utilisé par le fournisseur. `responses` est la seule valeur prise en charge et constitue la valeur par défaut lorsque ce paramètre est omis.",
    },
    {
      key: "model_providers.<id>.query_params",
      type: "map<string,string>",
      description: "Paramètres de requête supplémentaires ajoutés aux requêtes envoyées au fournisseur.",
    },
    {
      key: "model_providers.<id>.http_headers",
      type: "map<string,string>",
      description: "En-têtes HTTP statiques ajoutés aux requêtes envoyées au fournisseur.",
    },
    {
      key: "model_providers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "En-têtes HTTP renseignés à partir des variables d’environnement lorsqu’elles sont présentes.",
    },
    {
      key: "model_providers.<id>.request_max_retries",
      type: "number",
      description:
        "Nombre de nouvelles tentatives pour les requêtes HTTP envoyées au fournisseur (valeur par défaut : 4).",
    },
    {
      key: "model_providers.<id>.stream_max_retries",
      type: "number",
      description: "Nombre de tentatives de reprise des flux SSE après une interruption (valeur par défaut : 5).",
    },
    {
      key: "model_providers.<id>.stream_idle_timeout_ms",
      type: "number",
      description:
        "Délai maximal d’inactivité des flux SSE en millisecondes (valeur par défaut : 300000).",
    },
    {
      key: "model_providers.<id>.supports_websockets",
      type: "boolean",
      description:
        "Indique si ce fournisseur prend en charge le transport WebSocket de la Responses API.",
    },
    {
      key: "model_providers.<id>.supports_standalone_web_search",
      type: "boolean",
      description:
        "Déclarez la prise en charge d’un point de terminaison compatible pour la recherche web autonome (valeur par défaut : false). La recherche autonome reste en cours de développement et désactivée par défaut ; la compatibilité du fournisseur ne suffit pas à l’activer.",
    },
    {
      key: "model_providers.<id>.auth",
      type: "table",
      description:
        "Configuration d’un token bearer fourni par une commande pour un fournisseur personnalisé. Ne la combinez pas avec `env_key`, `experimental_bearer_token` ou `requires_openai_auth`.",
    },
    {
      key: "model_providers.<id>.auth.command",
      type: "string",
      description:
        "Commande à exécuter lorsque Codex a besoin d’un token bearer. La commande doit écrire le token sur stdout.",
    },
    {
      key: "model_providers.<id>.auth.args",
      type: "array<string>",
      description: "Arguments transmis à la commande de récupération du token.",
    },
    {
      key: "model_providers.<id>.auth.timeout_ms",
      type: "number",
      description:
        "Durée d’exécution maximale de la commande de récupération du token, en millisecondes (valeur par défaut : 5000).",
    },
    {
      key: "model_providers.<id>.auth.refresh_interval_ms",
      type: "number",
      description:
        "Intervalle entre les actualisations proactives du token par Codex, en millisecondes (valeur par défaut : 300000). Définissez cette valeur sur `0` pour n’actualiser le token qu’après une nouvelle tentative d’authentification.",
    },
    {
      key: "model_providers.<id>.auth.cwd",
      type: "string (path)",
      description: "Répertoire de travail de la commande de récupération du token.",
    },
    {
      key: "model_providers.amazon-bedrock.aws.profile",
      type: "string",
      description:
        "Nom du profil AWS utilisé par le fournisseur intégré `amazon-bedrock`.",
    },
    {
      key: "model_providers.amazon-bedrock.aws.region",
      type: "string",
      description: "Région AWS utilisée par le fournisseur intégré `amazon-bedrock`.",
    },
    {
      key: "model_reasoning_effort",
      type: "minimal | low | medium | high | xhigh",
      description:
        "Ajustez l’effort de raisonnement pour les modèles pris en charge (Responses API uniquement ; `xhigh` dépend du modèle).",
    },
    {
      key: "plan_mode_reasoning_effort",
      type: "none | minimal | low | medium | high | xhigh",
      description:
        "Valeur de remplacement de l’effort de raisonnement propre au mode plan. En l’absence de valeur, le mode plan utilise la valeur par défaut de son préréglage intégré.",
    },
    {
      key: "model_reasoning_summary",
      type: "auto | concise | detailed | none",
      description:
        "Sélectionnez le niveau de détail du résumé du raisonnement ou désactivez entièrement les résumés.",
    },
    {
      key: "model_verbosity",
      type: "low | medium | high",
      description:
        "Valeur de remplacement facultative du niveau de verbosité de la Responses API pour GPT-5 ; si elle n’est pas définie, la valeur par défaut du modèle ou du préréglage sélectionné est utilisée.",
    },
    {
      key: "model_supports_reasoning_summaries",
      type: "boolean",
      description: "Forcez Codex à envoyer ou à ne pas envoyer les métadonnées de raisonnement.",
    },
    {
      key: "shell_environment_policy.inherit",
      type: "all | core | none",
      description:
        "Règles de base pour l’héritage de l’environnement lors du lancement de sous-processus.",
    },
    {
      key: "shell_environment_policy.ignore_default_excludes",
      type: "boolean",
      description:
        "Conservez les variables contenant KEY, SECRET ou TOKEN avant l’application des autres filtres (par défaut : true). Définissez ce paramètre sur false pour appliquer les exclusions automatiques fondées sur les noms de secrets.",
    },
    {
      key: "shell_environment_policy.filters",
      type: "map<string, include | exclude>",
      description:
        "Filtres canoniques par motifs de noms de variables d’environnement, insensibles à la casse. Les entrées d’inclusion créent une liste d’autorisation et ne peuvent pas rétablir les valeurs exclues. Les valeurs `set` explicites s’appliquent après les exclusions. Ne combinez pas ces filtres avec les anciens tableaux `exclude` ou `include_only` dans une même couche.",
    },
    {
      key: "shell_environment_policy.exclude",
      type: "array<string>",
      description:
        "Anciens motifs d’exclusion de variables d’environnement. Utilisez `shell_environment_policy.filters` pour toute nouvelle configuration ; ne combinez pas les deux formes dans une même couche.",
    },
    {
      key: "shell_environment_policy.include_only",
      type: "array<string>",
      description:
        "Ancienne liste d’autorisation par motifs de noms de variables d’environnement. Utilisez `shell_environment_policy.filters` pour toute nouvelle configuration ; ne combinez pas les deux formes dans une même couche.",
    },
    {
      key: "shell_environment_policy.set",
      type: "map<string,string>",
      description:
        "Valeurs d’environnement explicites injectées après les exclusions ; les filtres d’inclusion peuvent encore les supprimer.",
    },
    {
      key: "shell_environment_policy.experimental_use_profile",
      type: "boolean",
      description: "Utilisez le profil shell de l’utilisateur lors du lancement de sous-processus.",
    },
    {
      key: "project_root_markers",
      type: "array<string>",
      description:
        "Liste des noms de fichiers servant à repérer la racine du projet lors de la recherche dans les répertoires parents.",
    },
    {
      key: "project_doc_max_bytes",
      type: "number",
      description:
        "Nombre maximal d’octets lus dans `AGENTS.md` lors de la préparation des instructions du projet.",
    },
    {
      key: "project_doc_fallback_filenames",
      type: "array<string>",
      description: "Noms de fichiers supplémentaires à essayer lorsque `AGENTS.md` est absent.",
    },
    {
      key: "history.persistence",
      type: "save-all | none",
      description:
        "Indiquez si Codex enregistre les transcriptions des sessions dans history.jsonl.",
    },
    {
      key: "tool_output_token_limit",
      type: "number",
      description:
        "Budget de tokens pour stocker chaque sortie d’outil ou de fonction dans l’historique.",
    },
    {
      key: "background_terminal_max_timeout",
      type: "number",
      description:
        "Durée maximale d’attente en millisecondes pour les appels à vide à `write_stdin` (interrogation du terminal en arrière-plan). Valeur par défaut : `300000` (5 minutes). Remplace l’ancienne clé `background_terminal_timeout`.",
    },
    {
      key: "history.max_bytes",
      type: "number",
      description:
        "Si ce paramètre est défini, il plafonne la taille du fichier d’historique en octets en supprimant les entrées les plus anciennes.",
    },
    {
      key: "file_opener",
      type: "vscode | vscode-insiders | windsurf | cursor | none",
      description:
        "Schéma d’URI utilisé pour ouvrir les citations figurant dans la sortie de Codex (par défaut : `vscode`).",
    },
    {
      key: "otel.environment",
      type: "string",
      description:
        "Étiquette d’environnement appliquée aux événements OpenTelemetry émis (par défaut : `dev`).",
    },
    {
      key: "otel.exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "Sélectionnez l’exportateur OpenTelemetry et fournissez les éventuelles métadonnées du point de terminaison.",
    },
    {
      key: "otel.trace_exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "Sélectionnez l’exportateur de traces OpenTelemetry et fournissez les éventuelles métadonnées du point de terminaison.",
    },
    {
      key: "otel.metrics_exporter",
      type: "none | statsig | otlp-http | otlp-grpc",
      description:
        "Sélectionnez l’exportateur de métriques OpenTelemetry (par défaut : `statsig`).",
    },
    {
      key: "otel.log_user_prompt",
      type: "boolean",
      description:
        "Activez l’exportation des prompts utilisateur bruts avec les journaux OpenTelemetry.",
    },
    {
      key: "otel.exporter.<id>.endpoint",
      type: "string",
      description: "Point de terminaison de l’exportateur pour les journaux OTEL.",
    },
    {
      key: "otel.exporter.<id>.protocol",
      type: "binary | json",
      description: "Protocole utilisé par l’exportateur OTLP/HTTP.",
    },
    {
      key: "otel.exporter.<id>.headers",
      type: "map<string,string>",
      description: "En-têtes statiques inclus dans les requêtes de l’exportateur OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.endpoint",
      type: "string",
      description: "Point de terminaison de l’exportateur de traces pour les journaux OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.protocol",
      type: "binary | json",
      description: "Protocole utilisé par l’exportateur de traces OTLP/HTTP.",
    },
    {
      key: "otel.trace_exporter.<id>.headers",
      type: "map<string,string>",
      description: "En-têtes statiques inclus dans les requêtes de l’exportateur de traces OTEL.",
    },
    {
      key: "otel.exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "Chemin d’accès au certificat de l’autorité de certification (CA) pour la connexion TLS de l’exportateur OTEL.",
    },
    {
      key: "otel.exporter.<id>.tls.client-certificate",
      type: "string",
      description: "Chemin d’accès au certificat client pour la connexion TLS de l’exportateur OTEL.",
    },
    {
      key: "otel.exporter.<id>.tls.client-private-key",
      type: "string",
      description: "Chemin d’accès à la clé privée du client pour la connexion TLS de l’exportateur OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "Chemin d’accès au certificat de l’autorité de certification (CA) pour la connexion TLS de l’exportateur de traces OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-certificate",
      type: "string",
      description: "Chemin d’accès au certificat client pour la connexion TLS de l’exportateur de traces OTEL.",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-private-key",
      type: "string",
      description: "Chemin d’accès à la clé privée du client pour la connexion TLS de l’exportateur de traces OTEL.",
    },
    {
      key: "desktop.custom_file_handlers.<id>",
      type: "table",
      description:
        "Au niveau utilisateur uniquement. Définit une cible **Ouvrir dans** supplémentaire pour l’application de bureau ChatGPT. Consultez [Ajouter des gestionnaires de fichiers personnalisés](/codex/config-file/config-advanced#add-custom-file-handlers) pour obtenir des exemples et connaître les contraintes relatives aux identifiants des gestionnaires.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.label",
      type: "string",
      description: "Nom d’affichage indiqué dans les menus **Ouvrir dans**. Obligatoire.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.icon",
      type: "string",
      description:
        "Chemin d’une ressource intégrée, URL `data:image/...` encodée en Base64, URI de fichier ou chemin local absolu pour l’icône du gestionnaire. Obligatoire ; l’icône VS Code par défaut est utilisée si la source n’est pas prise en charge.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.command",
      type: "string",
      description:
        "Chemin de l’exécutable ou nom de la commande à détecter et à lancer. Obligatoire.",
    },
    {
      key: "desktop.custom_file_handlers.<id>.args",
      type: "array<string>",
      description:
        "Arguments insérés entre la commande et le fichier fourni en entrée (par défaut : `[]`).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.input",
      type: "path | json_argument | json_stdin",
      description:
        "Méthode utilisée par l’application pour transmettre le fichier au gestionnaire (par défaut : `path`).",
    },
    {
      key: "desktop.custom_file_handlers.<id>.supports_ssh",
      type: "boolean",
      description:
        "Proposez le gestionnaire pour les fichiers situés dans des espaces de travail SSH (par défaut : `false`).",
    },
    {
      key: "tui",
      type: "table",
      description:
        "Options propres à la TUI, comme l’activation des notifications de bureau intégrées.",
    },
    {
      key: "tui.notifications",
      type: "boolean | array<string>",
      description:
        "Activez les notifications de la TUI et, si nécessaire, limitez-les à certains types d’événements.",
    },
    {
      key: "tui.notification_method",
      type: "auto | osc9 | bel",
      description:
        "Méthode utilisée pour les notifications du terminal (par défaut : auto).",
    },
    {
      key: "tui.notification_condition",
      type: "unfocused | always",
      description:
        "Indiquez si les notifications de la TUI se déclenchent uniquement lorsque le terminal n’a pas le focus ou indépendamment du focus. Valeur par défaut : `unfocused`.",
    },
    {
      key: "tui.animations",
      type: "boolean",
      description:
        "Activez les animations du terminal (écran d’accueil, effet de scintillement et indicateur de chargement rotatif) (par défaut : true).",
    },
    {
      key: "tui.alternate_screen",
      type: "auto | always | never",
      description:
        "Contrôlez l’utilisation de l’écran alternatif par la TUI (par défaut : auto ; en mode auto, il n’est pas utilisé dans Zellij afin de préserver l’historique de défilement).",
    },
    {
      key: "tui.resume_cwd",
      type: "current | session",
      description:
        "Répertoire de travail à utiliser lorsque vous reprenez ou forkez une session. S’il n’est pas défini, Codex vous demande de choisir un répertoire si votre répertoire actuel diffère du répertoire enregistré pour la session.",
    },
    {
      key: "tui.vim_mode_default",
      type: "boolean",
      description:
        "Démarrez la zone de saisie en mode normal de Vim plutôt qu’en mode insertion (par défaut : false). Vous pouvez toujours modifier ce réglage pour chaque session avec `/vim`.",
    },
    {
      key: "tui.raw_output_mode",
      type: "boolean",
      description:
        "Démarrez la TUI en mode d’historique de défilement brut pour faciliter la sélection et la copie dans le terminal (par défaut : false). Vous pouvez activer ou désactiver ce mode avec `/raw` ou le raccourci clavier `alt-r` par défaut.",
    },
    {
      key: "tui.show_tooltips",
      type: "boolean",
      description:
        "Affichez les info-bulles de prise en main sur l’écran d’accueil de la TUI (par défaut : true).",
    },
    {
      key: "tui.status_line",
      type: "array<string> | null",
      description:
        "Liste ordonnée des identifiants des éléments de la ligne d’état au bas de la TUI. `null` désactive la ligne d’état.",
    },
    {
      key: "tui.terminal_title",
      type: "array<string> | null",
      description:
        "Liste ordonnée des identifiants des éléments du titre de la fenêtre ou de l’onglet du terminal. Valeur par défaut : `[\"spinner\", \"project\"]` ; `null` désactive les mises à jour du titre.",
    },
    {
      key: "tui.theme",
      type: "string",
      description:
        "Thème de coloration syntaxique à utiliser en remplacement (nom du thème en kebab-case).",
    },
    {
      key: "tui.keymap.<context>.<action>",
      type: "string | array<string>",
      description:
        "Association d’un raccourci clavier à une action de la TUI. Les contextes pris en charge incluent `global`, `chat`, `composer`, `editor`, `vim_normal`, `vim_operator`, `vim_text_object`, `pager`, `list` et `approval`. Pour certaines actions de la zone de saisie, les associations correspondantes de `tui.keymap.global` s’appliquent à défaut ; les associations propres au contexte sont prioritaires lorsqu’elles sont prises en charge.",
    },
    {
      key: "tui.keymap.<context>.<action> = []",
      type: "empty array",
      description:
        "Supprimez le raccourci associé à cette action dans ce contexte de mappage clavier. Les noms de touches utilisent des chaînes normalisées comme `ctrl-a`, `shift-enter`, `page-down` ou `minus`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled",
      type: "boolean",
      description:
        "Activez ou désactivez un serveur MCP fourni avec un plugin installé sans modifier le manifeste du plugin.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportement d’approbation par défaut pour les outils d’un serveur MCP fourni par un plugin.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled_tools",
      type: "array<string>",
      description:
        "Liste d’autorisation des outils exposés par un serveur MCP fourni par un plugin.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.disabled_tools",
      type: "array<string>",
      description:
        "Liste de refus appliquée après `enabled_tools` pour un serveur MCP fourni par un plugin.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "Comportement d’approbation de remplacement pour un outil MCP fourni par un plugin.",
    },
    {
      key: "tui.model_availability_nux.<model>",
      type: "integer",
      description: "État interne de l’info-bulle de démarrage, indexé par le slug du modèle.",
    },
    {
      key: "hide_agent_reasoning",
      type: "boolean",
      description:
        "Masquez les événements de raisonnement dans la TUI comme dans la sortie de `codex exec`.",
    },
    {
      key: "show_raw_agent_reasoning",
      type: "boolean",
      description:
        "Affichez le contenu brut du raisonnement lorsque le modèle actif en produit.",
    },
    {
      key: "disable_paste_burst",
      type: "boolean",
      description: "Désactivez la détection des collages en rafale dans la TUI.",
    },
    {
      key: "windows_wsl_setup_acknowledged",
      type: "boolean",
      description: "Enregistrez la confirmation du parcours de prise en main de Windows (Windows uniquement).",
    },
    {
      key: "chatgpt_base_url",
      type: "string",
      description: "Remplacez l’URL de base utilisée lors de la connexion à ChatGPT.",
    },
    {
      key: "cli_auth_credentials_store",
      type: "file | keyring | auto",
      description:
        "Définissez où la CLI stocke les identifiants mis en cache (fichier auth.json ou trousseau du système d’exploitation).",
    },
    {
      key: "mcp_oauth_credentials_store",
      type: "auto | file | keyring",
      description: "Emplacement de stockage privilégié pour les identifiants OAuth MCP.",
    },
    {
      key: "mcp_oauth_callback_port",
      type: "integer",
      description:
        "Port fixe global facultatif pour le serveur HTTP local de rappel utilisé lors de la connexion OAuth MCP. Le paramètre `oauth.callback_port` propre à un serveur est prioritaire. Si aucun des deux n’est défini, Codex utilise un port éphémère choisi par le système d’exploitation.",
    },
    {
      key: "mcp_oauth_callback_url",
      type: "string",
      description:
        "URL de base de rappel facultative pour la connexion OAuth MCP, par exemple l’URL d’entrée d’une devbox. Les clients préenregistrés nouvellement ajoutés utilisent cette URL telle quelle lorsque le serveur d’autorisation prend en charge l’identification de l’émetteur ; les clients existants sans URL de rappel enregistrée y ajoutent un identifiant de rappel propre au serveur. Sans prise en charge de l’identification de l’émetteur, tout serveur MCP préenregistré dont l’URL de rappel configurée ne contient pas l’identifiant requis utilise cette URL en y ajoutant l’identifiant. Les ports figurant dans les URL de rappel ne déterminent pas le port d’écoute.",
    },
    {
      key: "experimental_use_unified_exec_tool",
      type: "boolean",
      description:
        "Ancien nom permettant d’activer l’exécution unifiée ; privilégiez `[features].unified_exec` ou `codex --enable unified_exec`.",
    },
    {
      key: "tools.web_search",
      type: 'boolean | { context_size = "low|medium|high", allowed_domains = [string], location = { country, region, city, timezone } }',
      description:
        "Configuration facultative de l’outil de recherche web. La forme objet permet de définir la taille du contexte de recherche, les domaines autorisés pour la recherche et la localisation approximative de l’utilisateur. Ces filtres de domaines de recherche sont distincts des règles de domaines réseau applicables aux commandes exécutées dans le bac à sable et ne limitent ni les connecteurs ni les serveurs MCP.",
    },
    {
      key: "tools.view_image",
      type: "boolean",
      description: "Activez l’outil `view_image` permettant de joindre des images locales.",
    },
    {
      key: "web_search",
      type: "disabled | cached | indexed | live",
      description:
        "Mode de recherche web (par défaut : `\"cached\"` ; le mode cached utilise un index maintenu par OpenAI sans accès au web externe ; le mode indexed permet un accès externe uniquement si l’index de recherche l’autorise ; si vous utilisez `--yolo` ou un autre paramètre de bac à sable accordant un accès complet, la valeur par défaut est `\"live\"`). Utilisez `\"live\"` pour récupérer du contenu en direct sans restriction, ou `\"disabled\"` pour supprimer l’outil.",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "Nom du profil d’autorisations par défaut à appliquer aux appels d’outils exécutés dans le bac à sable. Les profils intégrés sont `:read-only`, `:workspace` et `:danger-full-access` ; les noms de profils personnalisés nécessitent des tables `[permissions.<name>]` correspondantes. Ne combinez pas ce paramètre avec `sandbox_mode` ou `[sandbox_workspace_write]`.",
    },
    {
      key: "permissions.<name>.description",
      type: "string",
      description:
        "Description en langage naturel de ce profil nommé. Un profil n’hérite pas de la description de son parent via `extends`.",
    },
    {
      key: "permissions.<name>.extends",
      type: "string",
      description:
        "Profil parent facultatif appliqué avant ce profil nommé. Indiquez un autre profil nommé, `:read-only` ou `:workspace` ; `:danger-full-access`, les parents non définis et les cycles sont rejetés.",
    },
    {
      key: "permissions.<name>.workspace_roots",
      type: "table",
      description:
        "Racines d’espace de travail définies par le profil, auxquelles s’appliquent les règles de système de fichiers `:workspace_roots`, au même titre que les racines d’espace de travail de la session définies à l’exécution.",
    },
    {
      key: "permissions.<name>.workspace_roots.<path>",
      type: "boolean",
      description:
        "Incluez un chemin dans l’ensemble des racines d’espace de travail du profil en définissant cette option sur `true`. Les entrées désactivées restent inactives.",
    },
    {
      key: "permissions.<name>.filesystem",
      type: "table",
      description:
        "Profil d’autorisations nommé pour le système de fichiers. Chaque clé est un chemin absolu ou un token spécial tel que `:minimal` ou `:workspace_roots`.",
    },
    {
      key: "permissions.<name>.filesystem.glob_scan_max_depth",
      type: "number",
      description:
        "Profondeur maximale d’expansion des motifs glob d’interdiction de lecture sur les plateformes qui prennent un instantané des correspondances avant le démarrage du bac à sable. Si elle est définie, elle doit être au moins égale à `1`.",
    },
    {
      key: "permissions.<name>.filesystem.<path-or-glob>",
      type: '"read" | "write" | "deny" | table',
      description:
        "Accordez un accès direct à un chemin, à un motif glob ou à un token spécial, ou définissez la portée des entrées imbriquées sous cette racine. Utilisez `\"deny\"` pour interdire la lecture des chemins correspondants.",
    },
    {
      key: 'permissions.<name>.filesystem.":workspace_roots".<subpath-or-glob>',
      type: '"read" | "write" | "deny"',
      description:
        "Accès au système de fichiers dont la portée est définie par rapport à chaque racine effective de l’espace de travail. Utilisez `\".\"` pour la racine elle-même ; des sous-chemins avec motif glob tels que `\"**/*.env\"` peuvent interdire la lecture avec `\"deny\"`.",
    },
    {
      key: "permissions.<name>.network.enabled",
      type: "boolean",
      description:
        "Activez l’accès réseau pour les commandes de ce profil d’autorisations. Cela ne démarre pas le proxy réseau. Si `features.network_proxy` n’est pas activé et qu’aucune exigence réseau gérée par un administrateur n’est activée, l’accès réseau des commandes est direct et les règles de domaine du profil ne sont pas appliquées.",
    },
    {
      key: "permissions.<name>.network.proxy_url",
      type: "string",
      description:
        "URL d’écoute HTTP utilisée lorsque ce profil d’autorisations active l’accès réseau dans le bac à sable.",
    },
    {
      key: "permissions.<name>.network.enable_socks5",
      type: "boolean",
      description:
        "Activez la prise en charge de SOCKS5 lorsque ce profil d’autorisations active l’accès réseau dans le bac à sable.",
    },
    {
      key: "permissions.<name>.network.socks_url",
      type: "string",
      description: "Point de terminaison du proxy SOCKS5 utilisé par ce profil d’autorisations.",
    },
    {
      key: "permissions.<name>.network.enable_socks5_udp",
      type: "boolean",
      description: "Autorisez le protocole UDP via l’écouteur SOCKS5 lorsque celui-ci est activé.",
    },
    {
      key: "permissions.<name>.network.allow_upstream_proxy",
      type: "boolean",
      description:
        "Autorisez le trafic réseau du bac à sable à passer par un autre proxy en amont.",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Autorisez les écouteurs réseau du bac à sable à utiliser des adresses autres que celles de bouclage. L’activation de cette option peut rendre les écouteurs accessibles au-delà de localhost.",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Autorisez des destinations de sockets Unix arbitraires au lieu de l’ensemble restreint par défaut. Utilisez cette option uniquement dans des environnements étroitement contrôlés.",
    },
    {
      key: "permissions.<name>.network.mode",
      type: "limited | full",
      description: "Mode du proxy réseau utilisé pour le trafic des sous-processus.",
    },
    {
      key: "permissions.<name>.network.domains",
      type: "table",
      description:
        "Règles de domaine applicables aux commandes exécutées dans le bac à sable. Elles ne sont appliquées que lorsque `features.network_proxy` ou des exigences réseau actives gérées par un administrateur activent le proxy. Les noms d’hôtes exacts, `*.example.com`, `**.example.com` et les règles d’autorisation globales `*` sont pris en charge ; `deny` prévaut. Ces règles ne limitent ni la recherche web, ni les applications, ni les serveurs MCP.",
    },
    {
      key: "permissions.<name>.network.domains.<pattern>",
      type: "allow | deny",
      description:
        "Autorisez ou refusez un hôte par son nom exact ou par un motif à caractères génériques à portée définie, tel que `*.example.com` ou `**.example.com`.",
    },
    {
      key: "permissions.<name>.network.unix_sockets",
      type: "table",
      description:
        "Règles de remplacement de la liste d’autorisation des sockets Unix pour l’accès réseau dans le bac à sable. Utilisez les chemins de socket comme clés ; `allow` ajoute un chemin et `deny` le refuse.",
    },
    {
      key: "permissions.<name>.network.unix_sockets.<path>",
      type: "allow | deny",
      description:
        "Ajoutez un chemin absolu de socket Unix à la liste d’autorisation effective avec `allow`, ou refusez-le avec `deny`. Les entrées refusées sont exclues de la liste d’autorisation effective.",
    },
    {
      key: "permissions.<name>.network.allow_local_binding",
      type: "boolean",
      description:
        "Autorisez, depuis le bac à sable, un accès plus étendu aux réseaux locaux ou privés. Même si cette option reste définie sur `false`, des règles d’autorisation visant une adresse IP locale littérale exacte ou `localhost` peuvent toujours autoriser des cibles locales précises.",
    },
    {
      key: "projects.<path>.trust_level",
      type: "string",
      description:
        "Définissez un projet ou un arbre de travail comme fiable ou non fiable (`\"trusted\"` | `\"untrusted\"`). Pour les projets non fiables, les couches `.codex/` propres au projet sont ignorées, notamment la configuration, les hooks et les règles du projet.",
    },
    {
      key: "notice.hide_full_access_warning",
      type: "boolean",
      description: "Enregistrez la confirmation du message d’avertissement relatif à l’accès complet.",
    },
    {
      key: "notice.hide_world_writable_warning",
      type: "boolean",
      description:
        "Enregistrez la confirmation de l’avertissement concernant les répertoires accessibles en écriture à tous sous Windows.",
    },
    {
      key: "notice.hide_rate_limit_model_nudge",
      type: "boolean",
      description: "Enregistrez la désactivation du rappel de changement de modèle lié à la limite de débit.",
    },
    {
      key: "notice.hide_gpt5_1_migration_prompt",
      type: "boolean",
      description: "Enregistrez la confirmation du message de migration vers GPT-5.1.",
    },
    {
      key: "notice.hide_gpt-5.1-codex-max_migration_prompt",
      type: "boolean",
      description:
        "Enregistrez la confirmation du message de migration vers gpt-5.1-codex-max.",
    },
    {
      key: "notice.model_migrations",
      type: "map<string,string>",
      description: "Enregistrez les migrations de modèles confirmées sous forme de correspondances ancien->nouveau.",
    },
    {
      key: "forced_login_method",
      type: "chatgpt | api",
      description: "Restreignez Codex à une méthode d’authentification spécifique.",
    },
    {
      key: "forced_chatgpt_workspace_id",
      type: "string (uuid)",
      description: "Limitez les connexions à ChatGPT à un identifiant d’espace de travail spécifique.",
    },
  ]}
  client:load
/>

Le dernier schéma JSON de `config.toml` est disponible [ici](/codex/config-schema.json).

Pour bénéficier de l’autocomplétion et des diagnostics lors de la modification de `config.toml` dans VS Code ou Cursor, vous pouvez installer l’extension [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) et ajouter cette ligne au début de votre fichier `config.toml` :

```toml
#:schema https://developers.openai.com/codex/config-schema.json

Remarque : renommez `experimental_instructions_file` en `model_instructions_file`. Codex marque l’ancienne clé comme obsolète ; mettez à jour les configurations existantes afin d’utiliser le nouveau nom.

## `requirements.toml`

`requirements.toml` est un fichier de configuration imposé par l’administrateur qui encadre les paramètres sensibles pour la sécurité, sans que les utilisateurs puissent déroger à ces contraintes. Consultez [Exigences imposées par l’administrateur](/fr-FR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml) pour connaître les emplacements du fichier et obtenir des explications et des exemples.

Pour les utilisateurs de ChatGPT Business et ChatGPT Enterprise, Codex peut aussi appliquer des exigences
récupérées depuis le cloud. Consultez la page sur la sécurité pour connaître les règles de priorité.

Utilisez `[features]` dans `requirements.toml` pour fixer les indicateurs de fonctionnalités de l’environnement d’exécution à l’aide des mêmes
clés canoniques que dans `config.toml`. Les exigences peuvent aussi inclure des clés documentées
propres à l’application et qui ne doivent pas figurer dans `config.toml`. Les clés omises restent
sans contrainte.

Certaines exigences gérées imposent une valeur de configuration exacte plutôt qu’une
liste d’autorisation. Les utilisateurs ne peuvent pas remplacer les valeurs imposées pour un chemin, une préférence de mise à jour, une politique de shell de connexion,
un paramètre d’envoi de commentaires ou un paramètre de bureau privé sous Windows.

Les listes d’autorisation gérées pour les profils d’autorisations nécessitent Codex 0.138.0 ou une version ultérieure. Codex
0.137.0 et les versions antérieures ignorent `allowed_permission_profiles` et le paramètre géré
`default_permissions`.

Utilisez `allowed_sandbox_modes` avec `sandbox_mode`. Pour les déploiements utilisant des profils
d’autorisations, utilisez `allowed_permission_profiles` avec le paramètre géré
`default_permissions`.

La table `[models.new_thread]` fournit des valeurs par défaut gérées, sans les imposer.
Les choix explicites au lancement effectués avec des options CLI dédiées ou des valeurs de remplacement via `--config` sont
prioritaires. Un remplacement explicite du modèle ou de l’effort de raisonnement empêche l’application des deux champs gérés
relatifs au modèle ; `service_tier` est indépendant.

Les exigences relatives au navigateur couvrent trois interfaces distinctes. `in_app_browser`
contrôle le volet du navigateur qu’une personne ouvre et utilise directement. `browser_use`
contrôle les actions effectuées par l’agent dans un navigateur. `computer_use` contrôle les actions effectuées par l’agent
dans les applications de bureau natives.

Les valeurs imbriquées des politiques Navigateur et Utilisation de l’ordinateur n’accordent pas d’accès à elles seules.
Une valeur `allow` propre à une origine ou à une application peut remplacer la valeur de repli
de la même source de politique, mais les vérifications habituelles des fonctionnalités, des approbations et des autres politiques
continuent de s’appliquer. Lorsque les exigences gérées et `config.toml` s’appliquent toutes deux, une valeur `deny`
provenant de l’une ou de l’autre prévaut.

<ConfigTable
  options={[
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Imposez le répertoire où Codex stocke l’état d’exécution dans SQLite.",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description: "Imposez le répertoire dans lequel Codex écrit les fichiers journaux locaux.",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description: "Imposez le catalogue de modèles au format JSON que Codex utilise au démarrage.",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description: "Imposez l’activation ou la désactivation de la recherche de mises à jour au démarrage de Codex.",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description: "Imposez l’autorisation ou l’interdiction, pour les outils shell, de démarrer un shell de connexion.",
    },
    {
      key: "feedback",
      type: "table",
      description: "Paramètres d’envoi de commentaires gérés par l’administrateur.",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "Imposez le choix d’autoriser ou non les utilisateurs à envoyer des commentaires depuis les différents clients Codex.",
    },
    {
      key: "allowed_approval_policies",
      type: "array<string>",
      description:
        "Valeurs autorisées pour `approval_policy` (par exemple `untrusted`, `on-request`, `never` et `granular`).",
    },
    {
      key: "allowed_approvals_reviewers",
      type: "array<string>",
      description:
        "Valeurs autorisées pour `approvals_reviewer`, telles que `user` et `auto_review`.",
    },
    {
      key: "guardian_policy_config",
      type: "string",
      description:
        "Instructions gérées au format Markdown pour la politique de révision automatique. Elles prévalent sur la politique locale `[auto_review].policy`. Les valeurs vides sont ignorées.",
    },
    {
      key: "allowed_permission_profiles",
      type: "table<boolean>",
      description:
        "Liste complète des profils d’autorisations autorisés. Les profils définis sur `true` sont autorisés. Les profils omis ou définis sur `false` sont interdits, y compris ceux ajoutés dans de futures versions. Lorsque des sources d’exigences sont combinées, les entrées sont mises en correspondance par nom de profil.",
    },
    {
      key: "allowed_permission_profiles.<name>",
      type: "boolean",
      description:
        "Autorisez ou interdisez un profil d’autorisations intégré ou personnalisé défini dans une source de configuration ou d’exigences chargée. Une source d’exigences ultérieure et prioritaire peut utiliser `false` pour désactiver un profil autorisé par une source antérieure de priorité inférieure.",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "Profil d’autorisations par défaut géré par l’administrateur. Le profil doit être autorisé par `allowed_permission_profiles`. Définissez-le explicitement pour obtenir un comportement prévisible ; s’il est omis, Codex utilise `:workspace` par défaut uniquement lorsque `:workspace` et `:read-only` sont tous deux explicitement autorisés.",
    },
    {
      key: "enforce_residency",
      type: "string",
      description:
        "Exigez que le trafic du service Codex respecte une résidence des données prise en charge. Accepte actuellement `us`.",
    },
    {
      key: "models",
      type: "table",
      description:
        "Valeurs de modèle par défaut gérées par l’administrateur pour les nouveaux fils de discussion. Ces valeurs priment sur les valeurs par défaut de l’utilisateur et du projet, mais une sélection explicite pour le nouveau fil peut les remplacer.",
    },
    {
      key: "models.new_thread",
      type: "table",
      description:
        "Valeurs par défaut à appliquer au démarrage d’un nouveau fil de discussion local. Chaque paramètre du modèle est facultatif.",
    },
    {
      key: "models.new_thread.model",
      type: "string",
      description:
        "Modèle par défaut pour les nouveaux fils de discussion. Un remplacement explicite via `--model` ou via `--config` pour le modèle ou le raisonnement est prioritaire.",
    },
    {
      key: "models.new_thread.model_reasoning_effort",
      type: "string",
      description:
        "Effort de raisonnement par défaut pour les nouveaux fils de discussion. Un remplacement explicite du modèle ou de l’effort de raisonnement fait ignorer les deux champs de modèle gérés par l’administrateur.",
    },
    {
      key: "models.new_thread.service_tier",
      type: "string",
      description:
        "Offre par défaut pour les nouveaux fils de discussion. Un remplacement explicite de l’offre est prioritaire, indépendamment des champs de modèle.",
    },
    {
      key: "permissions",
      type: "table",
      description:
        "Profils d’autorisations définis par l’administrateur, avec le nom du profil comme clé. Ils utilisent les mêmes champs de profil que `config.toml`.",
    },
    {
      key: "permissions.<name>",
      type: "table",
      description:
        "Profil d’autorisations défini par l’administrateur. Son nom ne peut ni commencer par `:`, ni être le nom réservé `filesystem`, ni reprendre le nom d’un profil d’une configuration chargée. Il utilise les mêmes champs de profil que `config.toml` ; consultez le guide Autorisations pour connaître le schéma complet des profils.",
    },
    {
      key: "allowed_sandbox_modes",
      type: "array<string>",
      description: "Valeurs autorisées pour `sandbox_mode`.",
    },
    {
      key: "windows",
      type: "table",
      description: "Exigences relatives au bac à sable natif Windows.",
    },
    {
      key: "windows.allowed_sandbox_implementations",
      type: "array<string>",
      description:
        "Implémentations du bac à sable natif Windows autorisées pour `windows.sandbox` (`elevated` et `unelevated`). La liste ne doit pas être vide. Lorsque les deux sont autorisées et qu’aucun mode n’est sélectionné, Codex privilégie `elevated`.",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "Imposez l’utilisation ou non d’un bureau privé pour lancer le processus enfant du bac à sable natif Windows.",
    },
    {
      key: "remote_sandbox_config",
      type: "array<table>",
      description:
        "Exigences de bac à sable propres à chaque hôte. La première entrée dont les motifs `hostname_patterns` correspondent au nom d’hôte résolu remplace la valeur `allowed_sandbox_modes` de niveau supérieur pour cette source d’exigences. Actuellement, les entrées propres à un hôte ne remplacent que les modes de bac à sable.",
    },
    {
      key: "remote_sandbox_config[].hostname_patterns",
      type: "array<string>",
      description:
        "Motifs de noms d’hôte insensibles à la casse. Ils prennent en charge `*` pour une séquence quelconque de caractères et `?` pour un seul caractère.",
    },
    {
      key: "remote_sandbox_config[].allowed_sandbox_modes",
      type: "array<string>",
      description:
        "Modes de bac à sable autorisés à appliquer lorsque cette entrée propre à l’hôte correspond.",
    },
    {
      key: "allowed_web_search_modes",
      type: "array<string>",
      description:
        "Valeurs autorisées pour `web_search` (`disabled`, `cached`, `indexed`, `live`). `disabled` est toujours autorisé ; une liste vide n’autorise donc que `disabled`.",
    },
    {
      key: "allow_managed_hooks_only",
      type: "boolean",
      description:
        "Lorsque la valeur est `true`, Codex ignore les hooks utilisateur, de projet, de session et de plugin, tout en autorisant les hooks gérés provenant de `requirements.toml` et d’autres couches de configuration gérées.",
    },
    {
      key: "allow_appshots",
      type: "boolean",
      description:
        "Définissez cette option sur `false` pour désactiver les Captures d’application pour les utilisateurs gérés. Si cette option est omise, les exigences ne restreignent pas les Captures d’application et les règles normales de disponibilité du produit s’appliquent.",
    },
    {
      key: "allow_remote_control",
      type: "boolean",
      description:
        "Définissez cette option sur `false` pour désactiver le contrôle à distance des appareils pour les utilisateurs gérés. Si cette option est omise, les exigences ne restreignent pas le contrôle à distance des appareils, qui reste soumis aux règles normales de disponibilité du produit.",
    },
    {
      key: "allow_browser_and_computer_use",
      type: "boolean",
      description:
        "Définissez cette option sur `false` pour bloquer à la fois la fonctionnalité Navigateur pilotée par l’agent et la fonctionnalité Utilisation de l’ordinateur dans les applications natives. Définir cette option sur `true` ou l’omettre n’active aucune des deux fonctionnalités ; les autres vérifications relatives aux fonctionnalités, aux politiques et aux approbations continuent de s’appliquer.",
    },
    {
      key: "features.plugin_sharing",
      type: "boolean",
      description:
        "Définissez cette option sur `false` dans le fichier `requirements.toml` géré dans le cloud pour désactiver le partage des plugins créés localement au sein de l’espace de travail.",
    },
    {
      key: "features",
      type: "table",
      description:
        "Valeurs imposées aux fonctionnalités. Utilisez les noms canoniques de `config.toml` pour les fonctionnalités de l’environnement d’exécution ; les clés d’exigences documentées propres à l’application sont également prises en charge ici.",
    },
    {
      key: "features.<name>",
      type: "boolean",
      description:
        "Exigez qu’une fonctionnalité documentée de l’environnement d’exécution ou de l’application reste activée ou désactivée.",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "Imposez la disponibilité ou l’indisponibilité de l’intégration des Applications pour les utilisateurs gérés.",
    },
    {
      key: "features.in_app_updates",
      type: "boolean",
      description:
        "Définissez cette option sur `false` dans `requirements.toml` pour désactiver les mises à jour intégrées à l’application. Si cette exigence est omise, les mises à jour restent activées par défaut.",
    },
    {
      key: "features.in_app_browser",
      type: "boolean",
      description:
        "Définissez cette option sur `false` dans `requirements.toml` pour désactiver le volet du navigateur intégré que les utilisateurs ouvrent et contrôlent directement.",
    },
    {
      key: "features.browser_use",
      type: "boolean",
      description:
        "Définissez cette option sur `false` dans `requirements.toml` pour désactiver la fonctionnalité Navigateur pilotée par l’agent.",
    },
    {
      key: "features.browser_use_external",
      type: "boolean",
      description:
        "Définissez cette option sur `false` dans `requirements.toml` pour empêcher Codex de contrôler les navigateurs pris en charge via l’extension de navigateur ChatGPT, y compris les onglets existants et les sessions connectées.",
    },
    {
      key: "features.browser_use_full_cdp_access",
      type: "boolean",
      description:
        "Définissez cette option sur `false` dans `requirements.toml` pour désactiver l’accès complet à Chrome DevTools Protocol dans l’environnement d’exécution local, y compris le mode développeur du navigateur, et empêcher l’application de bureau ChatGPT d’activer le paramètre correspondant. Si cette option est omise, les règles normales de disponibilité du produit s’appliquent.",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "Imposez l’activation ou la désactivation de la fonctionnalité canonique `fast_mode` pour les utilisateurs gérés.",
    },
    {
      key: "features.guardian_approval",
      type: "boolean",
      description:
        "Imposez la disponibilité ou l’indisponibilité de l’approbation Guardian pour les utilisateurs gérés.",
    },
    {
      key: "features.memories",
      type: "boolean",
      description: "Imposez la disponibilité ou l’indisponibilité des Mémoires pour les utilisateurs gérés.",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description: "Imposez la disponibilité ou l’indisponibilité de la fonctionnalité multi-agent pour les utilisateurs gérés.",
    },
    {
      key: "features.plugins",
      type: "boolean",
      description: "Imposez la disponibilité ou l’indisponibilité des plugins pour les utilisateurs gérés.",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description:
        "Imposez la disponibilité ou l’indisponibilité du catalogue distant de plugins pour les utilisateurs gérés.",
    },
    {
      key: "features.computer_use",
      type: "boolean",
      description:
        "Définissez cette option sur `false` dans `requirements.toml` pour désactiver les fonctionnalités Utilisation de l’ordinateur et Enregistrer et rejouer, ainsi que les parcours d’installation ou d’activation associés.",
    },
    {
      key: "features.workspace_dependencies",
      type: "boolean",
      description:
        "Imposez la disponibilité ou l’indisponibilité de l’environnement d’exécution intégré pour les dépendances de l’espace de travail pour les utilisateurs gérés.",
    },
    {
      key: "in_app_browser",
      type: "table",
      description:
        "Exigences relatives au volet du navigateur intégré. Ces paramètres ne contrôlent pas la fonctionnalité Navigateur pilotée par l’agent.",
    },
    {
      key: "in_app_browser.allow_external_browser_settings_import",
      type: "boolean",
      description:
        "Définissez cette option sur `false` pour empêcher les utilisateurs d’importer des paramètres ou des données de navigation d’un navigateur externe dans le navigateur intégré. Définir cette option sur `true` ou l’omettre laisse l’importation disponible lorsque les autres vérifications du produit l’autorisent. Ce paramètre est réservé à la configuration gérée et ne peut pas être remplacé dans `config.toml`.",
    },
    {
      key: "browser_use",
      type: "table",
      description: "Exigences gérées pour la fonctionnalité Navigateur pilotée par l’agent.",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "Définissez cette option sur `false` pour empêcher la fonctionnalité Navigateur de lire l’historique de navigation. Définir cette option sur `true` ou l’omettre maintient les paramètres habituels de l’historique et les vérifications normales de disponibilité.",
    },
    {
      key: "browser_use.disable_auto_review",
      type: "boolean",
      description:
        "Définissez cette option sur `true` pour ignorer la révision automatique de la fonctionnalité Navigateur et demander à la place l’approbation de l’utilisateur. Définir cette option sur `false` ou l’omettre laisse la révision automatique disponible lorsque les autres paramètres l’autorisent.",
    },
    {
      key: "browser_use.allow_global_persistent_approval",
      type: "boolean",
      description:
        "Définissez cette option sur `false` pour empêcher la fonctionnalité Navigateur de créer ou de prendre en compte des approbations `Always allow` couvrant tous les sites, comme l’autorisation de télécharger depuis n’importe quel site. Les approbations déjà enregistrées sont ignorées, sans être supprimées. Définir cette option sur `true` ou l’omettre ne crée pas d’approbation.",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "Valeur de repli pour chaque paramètre de la fonctionnalité Navigateur lorsqu’aucune entrée correspondante dans `browser_use.origins` ne le définit. Une règle d’origine correspondante remplace la valeur de repli pour cette source. Codex applique ensuite le résultat le plus restrictif entre les exigences gérées et la configuration utilisateur.",
    },
    {
      key: "browser_use.default_origin_policy.access",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour bloquer la fonctionnalité Navigateur sur les origines auxquelles s’applique la valeur de repli. Le refus d’accès à une origine y bloque également les envois, les téléchargements, l’accès complet au débogage du navigateur et la révision automatique. `allow` permet uniquement de poursuivre les vérifications normales d’approbation et de politique.",
    },
    {
      key: "browser_use.default_origin_policy.downloads",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour bloquer les téléchargements de la fonctionnalité Navigateur sur les origines auxquelles s’applique la valeur de repli. `allow` permet uniquement de poursuivre les vérifications normales d’approbation et de politique.",
    },
    {
      key: "browser_use.default_origin_policy.uploads",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour bloquer les envois de la fonctionnalité Navigateur sur les origines auxquelles s’applique la valeur de repli. `allow` permet uniquement de poursuivre les vérifications normales d’approbation et de politique.",
    },
    {
      key: "browser_use.default_origin_policy.full_cdp_access",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour bloquer l’accès complet à Chrome DevTools Protocol (CDP) sur les origines auxquelles s’applique la valeur de repli. `allow` permet uniquement de poursuivre les vérifications normales d’activation volontaire et d’approbation.",
    },
    {
      key: "browser_use.default_origin_policy.auto_review",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour ignorer la révision automatique sur les origines auxquelles s’applique la valeur de repli et demander à la place l’approbation de l’utilisateur. `allow` laisse la révision automatique disponible lorsque les autres paramètres l’autorisent.",
    },
    {
      key: "browser_use.default_origin_policy.persistent_approval",
      type: "boolean",
      description:
        "Définissez cette option sur `false` pour empêcher la fonctionnalité Navigateur d’enregistrer ou de prendre en compte une approbation `Always allow` sur les origines auxquelles s’applique la valeur de repli. Les approbations pour le tour ou le fil de discussion en cours peuvent toujours s’appliquer. `true` rend l’option `Always allow` disponible lorsqu’elle est par ailleurs autorisée, mais ne crée pas d’approbation.",
    },
    {
      key: "browser_use.default_origin_policy.access_approval_lifetime",
      type: "turn | thread",
      description:
        "Définissez la durée de validité d’une approbation non persistante d’accès à un site : `turn` la limite au tour en cours, tandis que `thread` la conserve jusqu’à la fin du fil de discussion en cours. `persistent_approval` contrôle séparément la disponibilité de l’option `Always allow`. La valeur par défaut du produit est `thread`.",
    },
    {
      key: "browser_use.origins",
      type: "map<string, table>",
      description:
        "Politiques de la fonctionnalité Navigateur propres à chaque origine. Les clés utilisent le format `<scheme>://<host-pattern>[:<port>]` avec `http` ou `https`. Utilisez un hôte exact, `*.example.com` pour les sous-domaines uniquement ou `**.example.com` pour le domaine racine et ses sous-domaines. Les autres caractères génériques `*` peuvent couvrir des points : `region*.example.com` correspond donc aussi à `region.api.example.com` ; un hôte défini sur `*` correspond à tous les hôtes pour ce schéma. Les schémas et les ports non standard sont pris en compte ; les ports par défaut indiqués explicitement sont supprimés lors de la normalisation. Les chemins, les chaînes de requête, les noms d’utilisateur ou mots de passe intégrés, ainsi que les schémas ou ports contenant des caractères génériques, ne sont pas valides. Placez le motif entre guillemets en TOML, par exemple `[browser_use.origins.\"https://**.example.com\"]`.",
    },
    {
      key: "browser_use.origins.<pattern>",
      type: "table",
      description:
        "Politique applicable aux origines correspondant à ce motif. Si plusieurs motifs correspondent, Codex utilise la valeur la plus restrictive pour chaque capacité : `deny` prévaut sur `allow`, `false` sur `true` et `turn` sur `thread`.",
    },
    {
      key: "browser_use.origins.<pattern>.access",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour bloquer la fonctionnalité Navigateur sur les origines correspondantes. Le refus y bloque également les envois, les téléchargements, l’accès complet au débogage du navigateur et la révision automatique. `allow` permet uniquement de poursuivre les vérifications normales d’approbation et de politique.",
    },
    {
      key: "browser_use.origins.<pattern>.downloads",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour bloquer les téléchargements de la fonctionnalité Navigateur sur les origines correspondantes. `allow` permet uniquement de poursuivre les vérifications normales d’approbation et de politique.",
    },
    {
      key: "browser_use.origins.<pattern>.uploads",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour bloquer les envois de la fonctionnalité Navigateur sur les origines correspondantes. `allow` permet uniquement de poursuivre les vérifications normales d’approbation et de politique.",
    },
    {
      key: "browser_use.origins.<pattern>.full_cdp_access",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour bloquer l’accès complet à Chrome DevTools Protocol (CDP) sur les origines correspondantes. `allow` permet uniquement de poursuivre les vérifications normales d’activation volontaire et d’approbation.",
    },
    {
      key: "browser_use.origins.<pattern>.auto_review",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour ignorer la révision automatique sur les origines correspondantes et demander à la place l’approbation de l’utilisateur. `allow` laisse la révision automatique disponible lorsque les autres paramètres l’autorisent.",
    },
    {
      key: "browser_use.origins.<pattern>.persistent_approval",
      type: "boolean",
      description:
        "Définissez cette option sur `false` pour empêcher la fonctionnalité Navigateur d’enregistrer ou de prendre en compte une approbation `Always allow` sur les origines correspondantes. Les approbations pour le tour ou le fil de discussion en cours peuvent toujours s’appliquer. `true` rend l’option `Always allow` disponible lorsqu’elle est par ailleurs autorisée, mais ne crée pas d’approbation.",
    },
    {
      key: "browser_use.origins.<pattern>.access_approval_lifetime",
      type: "turn | thread",
      description:
        "Définissez la durée de validité d’une approbation non persistante d’accès à un site pour les origines correspondantes : `turn` la limite au tour en cours, tandis que `thread` la conserve jusqu’à la fin du fil de discussion en cours. `persistent_approval` contrôle séparément la disponibilité de l’option `Always allow`.",
    },
    {
      key: "computer_use",
      type: "table",
      description:
        "Exigences gérées pour les actions effectuées par l’agent dans les applications de bureau natives. Les règles d’application gérées et celles de `config.toml` sont toutes appliquées ; chaque source de politique doit autoriser l’application.",
    },
    {
      key: "computer_use.allow_locked_computer_use",
      type: "boolean",
      description:
        "Définissez cette option sur `false` pour empêcher les utilisateurs d’activer l’utilisation en mode verrouillé sur un appareil macOS géré. Cette exigence supprime les commandes d’activation, mais ne désactive pas l’utilisation en mode verrouillé si elle est déjà activée. Si cette option est omise, la disponibilité habituelle du produit s’applique.",
    },
    {
      key: "computer_use.allow_persistent_approval",
      type: "boolean",
      description:
        "Définissez cette option sur `false` pour supprimer la possibilité de conserver les approbations d’applications d’une session à l’autre. Les approbations pour la session en cours restent disponibles. Définir cette option sur `true` ou l’omettre n’approuve aucune application.",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "Accès par défaut pour les applications natives qui ne correspondent à aucune règle propre à leur plateforme. `deny` bloque l’accès. `allow` permet uniquement de poursuivre les vérifications habituelles d’approbation et de conformité aux politiques. La valeur par défaut du produit est `allow`.",
    },
    {
      key: "computer_use.macos",
      type: "table",
      description: "Règles d’applications pour la fonctionnalité Utilisation de l’ordinateur sur macOS.",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description:
        "Associez les identifiants de bundle macOS exacts à `allow` ou `deny`. Une règle correspondante remplace `computer_use.default_app_access` au sein de la même source de politique. Un refus provenant des exigences gérées ou de la configuration utilisateur bloque toujours l’accès.",
    },
    {
      key: "computer_use.macos.bundle_ids.<bundle-id>",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour bloquer l’identifiant de bundle exact. `allow` remplace uniquement la valeur par défaut de cette source de politique ; toute autre source de politique et le processus habituel d’approbation doivent également autoriser l’application.",
    },
    {
      key: "computer_use.windows",
      type: "table",
      description:
        "Règles d’applications pour la fonctionnalité Utilisation de l’ordinateur sur Windows, pour les applications empaquetées et non empaquetées.",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "Associez les identifiants Application User Model ID (AUMID) exacts et enregistrés des applications empaquetées signées à `allow` ou `deny`. Une règle correspondante remplace `computer_use.default_app_access` au sein de la même source de politique.",
    },
    {
      key: "computer_use.windows.aumids.<aumid>",
      type: "allow | deny",
      description:
        "Utilisez `deny` pour bloquer l’identité exacte de l’application empaquetée. `allow` remplace uniquement la valeur par défaut de cette source de politique ; toute autre source de politique et le processus habituel d’approbation doivent également autoriser l’application.",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Règles pour les exécutables Windows signés et non empaquetés. La correspondance s’effectue sur l’éditeur vérifié et les informations de version signées de l’exécutable, et non sur son chemin ou son nom de fichier actuel. Une règle de refus correspondante l’emporte sur les règles d’autorisation correspondantes. Les exécutables non signés utilisent `computer_use.default_app_access` ; les exécutables dont l’identité signée ne peut pas être vérifiée sans ambiguïté sont bloqués.",
    },
    {
      key: "computer_use.windows.exes[].publisher_name",
      type: "string",
      description:
        "Nom exact de l’éditeur provenant du certificat de signature de confiance de l’exécutable, au format de nom distinctif X.500 de Windows. Obligatoire.",
    },
    {
      key: "computer_use.windows.exes[].product_name",
      type: "string",
      description:
        "Valeur exacte de `ProductName` provenant des informations de version signées de l’exécutable. Obligatoire.",
    },
    {
      key: "computer_use.windows.exes[].binary_name",
      type: "string",
      description:
        "Valeur facultative de `OriginalFilename` provenant des informations de version signées de l’exécutable. La correspondance ne tient pas compte de la casse. Si une règle correspondant à l’éditeur et au produit exige cette valeur, mais que l’exécutable ne la fournit pas, la fonctionnalité Utilisation de l’ordinateur bloque l’exécutable.",
    },
    {
      key: "computer_use.windows.exes[].access",
      type: "allow | deny",
      description:
        "Décision d’accès obligatoire pour les exécutables correspondants. `deny` bloque l’accès. `allow` remplace uniquement la valeur par défaut de cette source de politique ; toute autre source de politique et le processus habituel d’approbation doivent également autoriser l’application.",
    },
    {
      key: "experimental_network",
      type: "table",
      description:
        "Exigences réseau gérées par l’administrateur pour les commandes locales exécutées dans le bac à sable, imposées depuis `requirements.toml`. Lorsqu’elles sont activées, ces exigences peuvent démarrer le proxy réseau des commandes sans `features.network_proxy`. Les outils de navigation vérifient séparément les refus réseau gérés et les listes d’autorisation exclusives. Ces exigences ne font pas transiter le trafic du navigateur par le proxy et ne contrôlent ni la recherche web, ni les applications, ni les serveurs MCP, ni le trafic des applications natives, ni les accès réseau de Codex Cloud.",
    },
    {
      key: "experimental_network.enabled",
      type: "boolean",
      description:
        "Activez les exigences réseau du bac à sable. Cela n’accorde pas d’accès réseau lorsque le bac à sable actif maintient les accès réseau des commandes désactivés.",
    },
    {
      key: "experimental_network.http_port",
      type: "integer",
      description:
        "Port d’écoute HTTP sur l’interface de bouclage à utiliser pour les exigences `[experimental_network]`.",
    },
    {
      key: "experimental_network.socks_port",
      type: "integer",
      description:
        "Port d’écoute SOCKS5 sur l’interface de bouclage à utiliser pour les exigences `[experimental_network]`.",
    },
    {
      key: "experimental_network.allow_upstream_proxy",
      type: "boolean",
      description:
        "Autorisez les connexions réseau du bac à sable à passer par un proxy en amont défini dans l’environnement.",
    },
    {
      key: "experimental_network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "Autorisez les adresses d’écoute hors de l’interface de bouclage pour les exigences `[experimental_network]`. L’activation de cette option peut rendre les services d’écoute accessibles au-delà de localhost.",
    },
    {
      key: "experimental_network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Autorisez n’importe quelle destination de socket Unix au lieu de limiter l’accès à la liste d’autorisation. Utilisez cette option uniquement dans des environnements strictement contrôlés.",
    },
    {
      key: "experimental_network.domains",
      type: "map<string, allow | deny>",
      description:
        "Politique de domaines définie par l’administrateur sous forme de table pour les accès réseau du bac à sable. Prend en charge les hôtes exacts, `*.example.com` pour les sous-domaines uniquement, `**.example.com` pour le domaine racine et ses sous-domaines, ainsi que les règles d’autorisation globales `*` ; privilégiez les règles ciblées, car `*` ouvre largement les accès sortants vers le réseau public. `deny` l’emporte en cas de conflit. Ne combinez pas cette option avec `experimental_network.allowed_domains` ou `experimental_network.denied_domains`.",
    },
    {
      key: "experimental_network.allowed_domains",
      type: "array<string>",
      description:
        "Règles d’autorisation définies par l’administrateur pour les accès réseau des commandes exécutées dans le bac à sable lorsque le proxy réseau géré est activé. Ces règles ne s’appliquent pas à la recherche web, aux applications ni aux serveurs MCP. Ne combinez pas cette option avec `experimental_network.domains`.",
    },
    {
      key: "experimental_network.denied_domains",
      type: "array<string>",
      description:
        "Règles de refus définies par l’administrateur sous forme de liste pour les accès réseau du bac à sable. Ne combinez pas cette option avec `experimental_network.domains`.",
    },
    {
      key: "experimental_network.managed_allowed_domains_only",
      type: "boolean",
      description:
        "Lorsque la valeur est `true`, seules les règles d’autorisation gérées par l’administrateur restent effectives tant que les exigences réseau du bac à sable sont actives ; les ajouts de l’utilisateur à la liste d’autorisation sont ignorés. En l’absence de règles d’autorisation gérées, les règles d’autorisation de domaines ajoutées par l’utilisateur ne restent pas effectives.",
    },
    {
      key: "experimental_network.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "Politique de sockets Unix gérée par l’administrateur pour les accès réseau du bac à sable.",
    },
    {
      key: "experimental_network.allow_local_binding",
      type: "boolean",
      description:
        "Autorisez un accès plus large au réseau local ou privé depuis le bac à sable. Les règles d’autorisation visant une adresse IP locale littérale exacte ou `localhost` peuvent toujours autoriser des destinations locales précises lorsque cette option reste définie sur `false`.",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "Hooks de cycle de vie gérés et imposés par l’administrateur. Nécessitent un répertoire de hooks gérés et utilisent le même schéma d’événements que la section `[hooks]` définie directement dans `config.toml`.",
    },
    {
      key: "hooks.managed_dir",
      type: "string (absolute path)",
      description:
        "Répertoire contenant les scripts de hooks gérés sur macOS et Linux. Codex vérifie que son chemin est absolu et que le répertoire existe avant de charger les hooks gérés.",
    },
    {
      key: "hooks.windows_managed_dir",
      type: "string (absolute path)",
      description:
        "Répertoire contenant les scripts de hooks gérés sur Windows. Codex vérifie que son chemin est absolu et que le répertoire existe avant de charger les hooks gérés.",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "Groupes de règles de correspondance pour un événement de hook tel que `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `SubagentStart`, `SubagentStop`, `UserPromptSubmit` ou `Stop`.",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "Gestionnaires de hooks pour un groupe de règles de correspondance. Les hooks de commande et d’outil MCP sont pris en charge, tandis que les gestionnaires de hooks de prompt et d’agent sont analysés, mais ne sont pas exécutés.",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "Exécutez un hook de commande en arrière-plan sans retarder l’opération qui le déclenche. La valeur par défaut est `false` ; `SessionEnd` s’exécute toujours de manière synchrone. Consultez [Exécution des hooks en arrière-plan](/codex/hooks#run-hooks-in-the-background).",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "Seuil approximatif en tokens, par gestionnaire, au-delà duquel un contenu `additionalContext` trop volumineux est enregistré sur disque et un aperçu plus court est présenté au modèle. La valeur par défaut est `2500` ; `0` transmet directement le contexte complet au modèle. Consultez [Sorties de hooks volumineuses](/codex/hooks#large-hook-output).",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "Commande de remplacement propre à Windows pour les hooks de commande. L’alias TOML `command_windows` est également accepté.",
    },
    {
      key: "permissions.filesystem.deny_read",
      type: "array<string>",
      description:
        "Interdictions de lecture du système de fichiers imposées par l’administrateur. Les entrées peuvent être des chemins ou des motifs glob, et les utilisateurs ne peuvent pas les assouplir avec une configuration locale.",
    },
    {
      key: "mcp_servers",
      type: "table",
      description:
        "Liste des serveurs MCP pouvant être activés. Le nom du serveur (`<id>`) et son identité doivent tous deux correspondre pour que le serveur MCP puisse être activé. Tout serveur MCP configuré qui ne figure pas dans la liste d’autorisation ou dont l’identité ne correspond pas est désactivé.",
    },
    {
      key: "mcp_servers.<id>.identity",
      type: "table",
      description:
        "Règle d’identité pour un serveur MCP. Définissez soit `command` (stdio), soit `url` (streamable HTTP).",
    },
    {
      key: "mcp_servers.<id>.identity.command",
      type: "string | table",
      description:
        "Autorisez un serveur MCP stdio en indiquant la chaîne exacte de sa commande, ou utilisez une table de correspondance pour imposer un exécutable précis et des règles de correspondance ordonnées pour les arguments. La forme chaîne ne vérifie ni les arguments, ni `cwd`, ni `env`, ni `env_vars`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.executable",
      type: "string",
      description:
        "Exécutable auquel la valeur `command` configurée pour le serveur stdio doit correspondre exactement.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args",
      type: "array<table>",
      description:
        "Règles de correspondance ordonnées pour les arguments d’un serveur stdio. La liste d’arguments configurée doit avoir la même longueur, et chaque argument doit satisfaire la règle à sa position. Les règles de correspondance de commande ne vérifient ni `cwd`, ni `env`, ni `env_vars`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "Opération de correspondance pour l’argument à cette position.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].value",
      type: "string",
      description: "Valeur utilisée par une règle de correspondance d’argument `exact` ou `prefix`.",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].expression",
      type: "string",
      description:
        "Expression régulière utilisée par une règle de correspondance d’argument `regex`. L’expression doit être valide et correspondre à l’intégralité de la valeur de l’argument.",
    },
    {
      key: "mcp_servers.<id>.identity.url",
      type: "string | table",
      description:
        "Autorisez un serveur MCP utilisant le transport streamable HTTP en indiquant la chaîne exacte de son URL, ou utilisez une table définissant une règle de correspondance de valeur de type `exact`, `prefix` ou `regex`.",
    },
    {
      key: "mcp_servers.<id>.identity.url.match",
      type: "exact | prefix | regex",
      description: "Opération de correspondance pour l’URL configurée du serveur MCP.",
    },
    {
      key: "mcp_servers.<id>.identity.url.value",
      type: "string",
      description: "Valeur utilisée par une règle de correspondance d’URL `exact` ou `prefix`.",
    },
    {
      key: "mcp_servers.<id>.identity.url.expression",
      type: "string",
      description:
        "Expression régulière utilisée par une règle de correspondance d’URL `regex`. L’expression doit être valide et correspondre à l’intégralité de la valeur de l’URL.",
    },
    {
      key: "plugins",
      type: "table",
      description:
        "Listes de serveurs MCP autorisés propres à chaque plugin, indexées par identifiant de plugin. Lorsque cette table est présente, les serveurs fournis avec un plugin sont désactivés si aucune entrée ne correspond au plugin et au serveur.",
    },
    {
      key: "plugins.<plugin>.mcp_servers",
      type: "table",
      description:
        "Liste des serveurs MCP autorisés pour un plugin. Les exigences relatives aux serveurs des plugins utilisent les mêmes formats pour les identités exactes et les règles de correspondance que les exigences `mcp_servers` de premier niveau.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity",
      type: "table",
      description:
        "Règle d’identité pour un serveur MCP fourni avec un plugin. Définissez soit `command` (stdio), soit `url` (streamable HTTP).",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command",
      type: "string | table",
      description:
        "Autorisez le serveur MCP stdio d’un plugin en indiquant la chaîne exacte de sa commande, ou utilisez une table de correspondance pour imposer un exécutable précis et des règles de correspondance ordonnées pour les arguments.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.executable",
      type: "string",
      description:
        "Exécutable auquel la commande configurée du serveur stdio fourni avec le plugin doit correspondre exactement.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args",
      type: "array<table>",
      description:
        "Règles de correspondance ordonnées pour les arguments d’un serveur stdio fourni avec un plugin. La liste d’arguments configurée doit avoir la même longueur, et chaque argument doit satisfaire la règle à sa position.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "Opération de correspondance pour l’argument à cette position.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].value",
      type: "string",
      description: "Valeur utilisée par une règle de correspondance d’argument `exact` ou `prefix`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].expression",
      type: "string",
      description:
        "Expression régulière utilisée par une règle de correspondance d’argument `regex`. L’expression doit correspondre à l’intégralité de la valeur de l’argument.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url",
      type: "string | table",
      description:
        "Autorisez le serveur MCP utilisant le transport streamable HTTP d’un plugin en indiquant la chaîne exacte de son URL, ou utilisez une table définissant une règle de correspondance de valeur de type `exact`, `prefix` ou `regex`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.match",
      type: "exact | prefix | regex",
      description: "Opération de correspondance pour l’URL du serveur MCP fourni avec le plugin.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.value",
      type: "string",
      description: "Valeur utilisée par une règle de correspondance d’URL `exact` ou `prefix`.",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.expression",
      type: "string",
      description:
        "Expression régulière utilisée par une règle de correspondance d’URL `regex`. L’expression doit correspondre à l’intégralité de la valeur de l’URL.",
    },
    {
      key: "marketplaces",
      type: "table",
      description:
        "Exigences définies par l’administrateur pour les sources des Marketplace de plugins. Ces règles s’appliquent lorsque `restrict_to_allowed_sources` est défini sur `true`.",
    },
    {
      key: "marketplaces.restrict_to_allowed_sources",
      type: "boolean",
      description:
        "Lorsque la valeur est `true`, les sources de Marketplace configurées par l’utilisateur doivent correspondre à `allowed_sources` lors de l’ajout d’une Marketplace, de l’installation d’un plugin ou de l’actualisation d’une Marketplace Git configurée. Les Marketplace OpenAI gérées par Codex restent autorisées si elles utilisent la source et le nom qui leur sont réservés. Ce paramètre ne filtre pas à l’exécution les Marketplace déjà configurées par l’utilisateur.",
    },
    {
      key: "marketplaces.allowed_sources",
      type: "table",
      description:
        "Sources de Marketplace autorisées, indexées par le nom de règle choisi par l’administrateur. Les noms distincts se cumulent d’une couche d’exigences à l’autre ; les champs associés à un même nom suivent l’ordre de priorité habituel des couches.",
    },
    {
      key: "marketplaces.allowed_sources.<name>",
      type: "table",
      description:
        "Règle définissant une source autorisée. La valeur finale de `source` après la fusion des exigences détermine les champs de même niveau que Codex interprète.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.source",
      type: "git | host_pattern | local",
      description:
        "Type de correspondance pour la source de la Marketplace. Utilisez `git` pour un dépôt, `host_pattern` pour des hôtes Git correspondant à une expression régulière, ou `local` pour un répertoire.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.url",
      type: "string",
      description:
        "URL du dépôt Git, obligatoire lorsque `source = \"git\"`. Codex normalise les URL configurées et autorisées, puis exige une correspondance exacte du dépôt.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.ref",
      type: "string",
      description:
        "Référence Git exacte facultative pour une règle `git`. Si elle est omise, la règle autorise toute référence du dépôt correspondant.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.host_pattern",
      type: "string",
      description:
        "Expression régulière obligatoire lorsque `source = \"host_pattern\"`. Codex l’applique au nom d’hôte en minuscules extrait d’une source Git HTTPS, SSH ou au format SCP. Utilisez `^` et `$` pour exiger une correspondance sur l’intégralité du nom d’hôte.",
    },
    {
      key: "marketplaces.allowed_sources.<name>.path",
      type: "string (absolute path)",
      description:
        "Répertoire local de la Marketplace, obligatoire lorsque `source = \"local\"`. Codex exige un chemin absolu et compare les chemins après normalisation.",
    },
    {
      key: "apps",
      type: "table",
      description:
        "Exigences gérées pour les applications, indexées par identifiant d’application. Elles peuvent désactiver une application ou restreindre le comportement d’approbation de chaque outil.",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "Définissez la valeur sur `false` pour désactiver une application. Une exigence de désactivation reste restrictive lors de la fusion de plusieurs sources d’exigences.",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "Définissez le mode d’approbation géré pour un outil d’application.",
    },
    {
      key: "rules",
      type: "table",
      description:
        "Règles de commande imposées par l’administrateur et fusionnées avec les fichiers `.rules`. Les règles définies dans les exigences doivent être restrictives.",
    },
    {
      key: "rules.prefix_rules",
      type: "array<table>",
      description:
        "Liste des règles de préfixe imposées. Chaque règle doit inclure `pattern` et `decision`.",
    },
    {
      key: "rules.prefix_rules[].pattern",
      type: "array<table>",
      description:
        "Préfixe de commande exprimé sous forme de tokens de motif. Chaque token définit soit `token`, soit `any_of`.",
    },
    {
      key: "rules.prefix_rules[].pattern[].token",
      type: "string",
      description: "Un seul token littéral à cette position.",
    },
    {
      key: "rules.prefix_rules[].pattern[].any_of",
      type: "array<string>",
      description: "Liste des tokens alternatifs autorisés à cette position.",
    },
    {
      key: "rules.prefix_rules[].decision",
      type: "prompt | forbidden",
      description:
        "Obligatoire. Les règles définies dans les exigences peuvent uniquement demander une approbation ou interdire, jamais autoriser.",
    },
    {
      key: "rules.prefix_rules[].justification",
      type: "string",
      description:
        "Justification facultative, non vide si elle est fournie, affichée dans les demandes d’approbation ou les messages de refus.",
    },
  ]}
  client:load
/>
