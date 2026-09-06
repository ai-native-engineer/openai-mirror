<!-- source: https://learn.chatgpt.com/fr-FR/docs/cyber-safety/recommended-configuration -->

Les contrôles de sécurité adaptés à un flux de travail de cybersécurité dépendent du modèle, des actions qu’il peut exécuter, des systèmes auxquels il peut accéder et de la sensibilité des données concernées.

Pour la plupart des flux de travail Daybreak Blue, les pratiques de sécurité déjà en place dans votre organisation, telles que les contrôles d’accès, la protection des identifiants et la révision des actions sensibles, peuvent suffire.

Les flux de travail Daybreak Red, les tests de sécurité autonomes et les activités impliquant des systèmes de production, des données sensibles ou des outils externes peuvent nécessiter des mesures de protection plus strictes. Les recommandations ci-dessous s’adressent principalement à ces scénarios à plus haut risque.

  Vous êtes responsable de l’évaluation des risques propres à votre flux de travail et
de la mise en œuvre des contrôles de sécurité appropriés. Les mesures de protection du modèle et
Trusted Access ne remplacent pas les pratiques de votre organisation en matière de sécurité, de surveillance et
de supervision.

Trusted Access régit l’accès approuvé aux modèles, mais ne configure pas votre environnement et ne fait pas respecter les limites applicables aux systèmes et actions approuvés. Votre équipe doit mettre en place des contrôles appropriés d’isolation, d’autorisation, de révision, de surveillance et de supervision humaine. Partez du principe que le modèle, ses outils et chaque système connecté peuvent être compromis, puis configurez l’environnement de sorte qu’ils ne puissent malgré tout ni accéder à des systèmes non autorisés, ni exposer des identifiants, ni désactiver les mesures de protection, ni persister après la fin du travail.

## Isolez l’environnement

Menez les travaux de sécurité offensive dans un laboratoire dédié ou un bac à sable. Commencez sans accès illimité à Internet ni accès aux systèmes de production sensibles, aux réseaux d’entreprise, aux charges de travail sans rapport avec la tâche ou aux interfaces de gestion de l’hôte. Gardez hors de portée les secrets, les identifiants, les accès persistants et les modifications durables du système, sauf si les travaux approuvés les exigent et les autorisent explicitement.

Pour les travaux à plus haut risque ou soumis à des mesures de protection réduites, utilisez un nouvel environnement fortement isolé à chaque tentative. Séparez les ressources de calcul et de stockage, le réseau et les identités, puis détruisez l’environnement au lieu de le réinitialiser ou de le réutiliser.

Testez les limites du système de fichiers et du réseau avant de commencer des travaux à plus haut risque. Incluez dans ces tests chaque hôte accessible, outil connecté, agent délégué et service en aval. Maintenez l’environnement hôte isolé même lorsque le modèle ou le réviseur approuve une action particulière.

## Définissez et faites respecter les limites approuvées

Avant de lancer le modèle, consignez les systèmes, les outils, les actions et les limites de durée approuvés pour vos travaux. Indiquez :

- Les systèmes, les hôtes et les environnements cibles approuvés.
- Les systèmes exclus, notamment les systèmes de production et l’infrastructure sans rapport avec la tâche.
- Les outils et services connectés approuvés.
- Les actions autorisées et interdites.
- Les horaires de début et de fin approuvés, ainsi que les exigences de traitement des données.
- La divulgation des vulnérabilités, l’approbation des correctifs et la coordination avec les mainteneurs.
- Les conditions d’arrêt et les actions qui nécessitent une approbation humaine explicite.

Fournissez ces limites approuvées à l’agent dans le contexte de la tâche. Les documenter ne suffit pas à les faire respecter : appliquez des contrôles indépendants au système de fichiers, au réseau, aux identités et aux outils afin de rendre les actions non autorisées impossibles chaque fois que possible.

Utilisez les [profils d’autorisation](/fr-FR/codex/permissions) de Codex pour définir un périmètre fondé sur le principe du moindre privilège. Choisissez `:read-only` lorsque la tâche ne nécessite aucune modification, ou étendez les autorisations avec `:workspace` lorsque le travail exige de modifier l’espace de travail. Par exemple :

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = "cyber-lab"

[features]
network_proxy = true

[permissions.cyber-lab]
description = "Limit security testing to the approved lab and workspace."
extends = ":workspace"

[permissions.cyber-lab.filesystem]
glob_scan_max_depth = 3

[permissions.cyber-lab.filesystem.":workspace_roots"]
"**/.env*" = "deny"
"**/*.pem" = "deny"

[permissions.cyber-lab.network]
enabled = true
# Uncomment only for an approved host that resolves to a private address.
# allow_local_binding = true

[permissions.cyber-lab.network.domains]
"lab.example.com" = "allow"

La fonctionnalité `network_proxy` impose le respect du domaine approuvé. Sans elle,
`network.enabled = true` autorise un accès direct au réseau et la liste d’autorisation du laboratoire
ne limite pas les destinations. La recherche web, les applications, les connecteurs, les serveurs MCP,
l’activité du navigateur et Codex Cloud disposent de contrôles distincts ; limitez ou désactivez
chaque interface qui n’est pas nécessaire au flux de travail approuvé.

Remplacez `lab.example.com` par une cible approuvée. L’analyse limitée du système de fichiers vise à éviter de parcourir l’intégralité de l’espace de travail sous Linux, WSL et Windows ; augmentez la profondeur d’analyse ou indiquez précisément les chemins à interdire si des fichiers sensibles se trouvent plus en profondeur. Ne combinez pas les profils d’autorisation avec les anciens paramètres `sandbox_mode` ; suivez les [instructions de configuration des profils d’autorisation](/fr-FR/codex/permissions#define-and-select-a-profile).

Si le nom de l’hôte de laboratoire approuvé est résolu en une adresse privée, Codex le bloque par défaut même s’il figure dans la liste d’autorisation. Définissez `allow_local_binding = true` uniquement pour des travaux sur réseau privé explicitement approuvés, limitez strictement la liste d’autorisation des destinations et consultez les [recommandations relatives aux réseaux locaux et privés](/fr-FR/codex/permissions#local-and-private-networks). Vous pouvez également ajouter à la liste d’autorisation l’adresse IP privée exacte approuvée.

Bloquez par défaut l’accès à l’Internet public et aux réseaux de production. Si un accès externe est nécessaire, faites-le transiter par une passerelle ou un proxy soumis à des contrôles indépendants, avec des listes d’autorisation restreintes, une inspection des requêtes et une journalisation. Appliquez les mêmes restrictions aux connexions indirectes via les gestionnaires de paquets, les webhooks, les services de récupération d’URL, les redirections, les API cloud et les outils connectés. Préchargez les dépendances avant l’exécution ou n’utilisez que celles qu’un administrateur a approuvées.

## Protégez les identifiants et les données sensibles

Ne placez aucune clé API réutilisable, aucun identifiant cloud, mot de passe ou token de compte de service dans les prompts, les dépôts, les variables d’environnement, les systèmes de fichiers partagés ou les journaux accessibles au modèle. Lorsqu’une authentification est requise, utilisez un service intermédiaire distinct ou une passerelle pour fournir des identifiants à courte durée de vie, limités à la cible exacte et à l’action autorisée, sans les exposer au modèle.

Fournissez uniquement les données nécessaires à la tâche approuvée. Supprimez les informations sensibles inutiles, bloquez l’accès aux métadonnées cloud et aux points de terminaison d’identifiants, et considérez les fichiers générés par le modèle comme non fiables.

Évitez `:danger-full-access` et `--yolo` pour les flux de travail de cybersécurité. Le mode Accès complet supprime le périmètre contraignant du bac à sable dont dépend la révision automatique. Les organisations gérées peuvent interdire `:danger-full-access` et `--yolo`, limiter les politiques d’approbation autorisées et imposer la révision automatique au moyen d’une [configuration gérée par l’entreprise](/fr-FR/codex/enterprise/managed-configuration#configure-automatic-review-policy).

Avant d’activer **Accès complet** pour un modèle de sécurité approuvé, l’application de bureau ChatGPT affiche un avertissement propre au modèle concernant les actions dangereuses. Cet avertissement recommande plutôt **Approuver pour moi** et renvoie vers la [configuration de la politique du réviseur](/fr-FR/codex/sandboxing/auto-review#configuration). Il ne rétablit pas les limites du bac à sable et ne prévaut pas sur la politique de l’organisation.

Les garde-fous soumettent un flux de travail de cybersécurité encadré à une révision selon des règles définies. Ils ne remplacent ni l’isolation de l’environnement, ni les autorisations fondées sur le principe du moindre privilège, ni des limites clairement définies, ni la surveillance, ni la supervision humaine.

## Révisez les actions sensibles de Codex

La [Révision automatique](/fr-FR/codex/sandboxing/auto-review) transmet les demandes d’approbation admissibles liées aux limites du bac à sable à un réviseur distinct avant l’exécution de l’action proposée. Le réviseur examine l’action proposée, le contexte délimité de la tâche et la politique applicable, puis accepte ou refuse la demande. Les organisations peuvent adapter cette politique en fonction de leurs cibles approuvées, des actions interdites et des cas dans lesquels une révision humaine est obligatoire.

Exigez une approbation humaine explicite pour les actions qui affectent la production, les systèmes externes, les données sensibles, l’élévation de privilèges, les accès persistants ou les modifications irréversibles. Considérez comme non fiables les instructions intégrées aux sites web, aux dépôts, aux documents et aux sorties d’outils ; elles ne peuvent ni élargir le périmètre autorisé ni contourner les contrôles d’accès.

Dans l’application de bureau ChatGPT, la sélection d’un modèle Daybreak approuvé fait automatiquement passer le réglage des autorisations à **Approuver pour moi** si ce mode est disponible pour votre compte et autorisé par la politique de l’organisation. Cela s’applique également lorsque vous utilisez la commande `/model` de l’application de bureau. Si ce mode n’est pas disponible, le mode d’autorisation actuel reste inchangé. Le choix du modèle ne permet jamais de déroger aux exigences d’une organisation gérée.

Pour permettre la révision automatique, maintenez ces trois contrôles en place :

1. Utilisez une politique d’approbation interactive telle que `approval_policy = "on-request"`.
2. Définissez `approvals_reviewer = "auto_review"`.
3. Maintenez un périmètre effectivement appliqué par un bac à sable ou un profil d’autorisation.

Les requêtes envoyées à une cible figurant dans la liste d’autorisation réseau restent à l’intérieur du périmètre réseau et ne déclenchent pas automatiquement la fonctionnalité Révision automatique. Pour réviser une commande sensible même lorsque sa destination figure dans la liste d’autorisation, créez une [règle de commande](/fr-FR/codex/agent-configuration/rules) explicite dans `~/.codex/rules/` :

```python
prefix_rule(
    pattern = ["curl"],
    decision = "prompt",
    justification = "Review requests to the approved cybersecurity target.",
)

Redémarrez Codex après avoir ajouté la règle. Avec `approvals_reviewer = "auto_review"`, les commandes qui correspondent à la règle sont envoyées au réviseur avant leur exécution. Ajoutez des règles de prompt correspondantes pour chaque commande sensible, ou utilisez `approval_mode = "prompt"` pour des [outils MCP](/fr-FR/codex/extend/mcp) particuliers. Les actions qui nécessitent une décision humaine doivent toujours faire l’objet d’une approbation humaine explicite.

La fonctionnalité Révision automatique n’inspecte pas les actions courantes déjà autorisées dans le bac à sable. Avec `approval_policy = "never"` ou Accès complet, une action sensible peut ne générer aucune demande d’approbation à réviser. La révision automatique peut se tromper et ne remplace ni l’isolation, ni des limites clairement définies, ni la surveillance, ni la supervision humaine explicite.

Pour définir une politique au périmètre précis et l’appliquer à l’échelle de l’organisation, consultez [Configurer un flux de travail de cybersécurité autorisé](/fr-FR/codex/sandboxing/auto-review#configure-an-authorized-cybersecurity-engagement).

## Surveillez de manière indépendante et bloquez par défaut en cas de défaillance

Journalisez les requêtes du modèle, les appels d’outils, l’activité réseau, l’utilisation des identifiants et les modifications pertinentes pour la sécurité. Conservez les journaux et les systèmes de surveillance en dehors de l’environnement contrôlé par le modèle. Déclenchez des alertes en cas de cibles non autorisées, de requêtes réseau inattendues, d’identifiants exposés, de modifications de politique, de journaux manquants ou de tentatives de contournement des mesures de protection.

Veillez à ce que l’application des politiques, les services intermédiaires de gestion des identifiants, les systèmes de révision et les mécanismes d’arrêt d’urgence restent indépendants de l’agent. Arrêtez le flux de travail en cas de défaillance d’un contrôle essentiel ou d’un système de surveillance.

## Ajoutez des garde-fous aux flux de travail personnalisés d’agents

Si vous développez avec la Responses API, l’Agents SDK ou un autre harnais, ajoutez une étape de révision au niveau de l’exécution des outils. Avant leur exécution, vérifiez que les actions sensibles proposées respectent les systèmes et actions approuvés ainsi que les limites de durée, transmettez les actions ambiguës ou à haut risque à une personne, appliquez des restrictions indépendantes au système de fichiers et au réseau, conservez des journaux d’audit et bloquez toute exécution si le réviseur ou la politique n’est pas disponible.

La fonctionnalité Révision automatique de Codex ne protège pas automatiquement les outils personnalisés ni les harnais externes. Pour une implémentation avec l’Agents SDK, utilisez [Garde-fous et révision humaine](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution) et prenez la [politique open source du réviseur](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md) comme référence.

Les mécanismes de bac à sable et de révision propres au produit Codex sont distincts des [contrôles de cybersécurité de l’API](/api/docs/guides/safety-checks/cybersecurity). Les mesures de protection de l’API peuvent renvoyer des erreurs `cyber_policy`, et les valeurs `safety_identifier` propres à chaque utilisateur peuvent aider à limiter l’impact d’une mesure de protection.

## Nettoyez et validez les résultats

Une fois les travaux terminés, révoquez les identifiants temporaires, arrêtez les processus en arrière-plan, supprimez les accès persistants et détruisez les environnements à plus haut risque. Vérifiez qu’il ne reste aucune connexion de rappel, aucun artefact exposé, aucun état partagé ni aucun accès d’une exécution à l’autre, et maintenez l’isolation entre les différents utilisateurs, sessions et évaluations.

Validez les constats avant d’agir, suivez les pratiques de divulgation coordonnée et veillez à ce que les personnes restent responsables des corrections et des modifications.

## Avant de commencer

Confirmez les systèmes et actions approuvés, le modèle adapté, l’environnement isolé, les autorisations fondées sur le principe du moindre privilège, l’accès réseau restreint, la protection des identifiants, la révision des actions, la surveillance indépendante, le mécanisme d’arrêt d’urgence et le plan de nettoyage. Les mesures de protection du modèle, l’isolation, les autorisations à portée limitée, la révision des actions, la surveillance et la supervision humaine sont complémentaires ; aucun de ces contrôles ne doit être utilisé seul.
