<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/skills -->

Les Skills sont des flux de travail réutilisables composés d’instructions et de ressources complémentaires.
Les Skills de l’espace de travail ChatGPT, les Skills du système de fichiers utilisés par les fonctionnalités locales concernées
dans l’application de bureau ChatGPT, dans Codex CLI ou dans l’extension IDE, ainsi que les plugins qui
regroupent des Skills disposent de contrôles distincts pour leur cycle de vie et la gestion de leurs accès.

Pour consulter le modèle d’administration complet, reportez-vous à
[Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions).

<a id="distinguish-the-distribution-models"></a>

## Distribution et administration des Skills

| Modèle de distribution      | Cas d’utilisation                                                                                           | Périmètre d’administration                                                                       |
| ----------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Skill de l’espace de travail ChatGPT | Partage ou installation d’un flux de travail approuvé via les fonctionnalités prises en charge dans l’espace de travail ChatGPT              | Autorisations des Skills de l’espace de travail ChatGPT et contrôles de leur cycle de vie                                    |
| Skill du système de fichiers local  | Chargement d’un flux de travail installé depuis un emplacement associé à un dépôt, à un utilisateur ou à un administrateur, ou depuis un emplacement système intégré     | Distribution via le système de fichiers, configuration du client local et autorisations au moment de l’exécution                  |
| Plugin                  | Regroupement d’un ou plusieurs Skills avec, en option, des connecteurs, des serveurs MCP, des hooks et des métadonnées de présentation | Disponibilité et installation du plugin, ainsi que les contrôles propres à chaque fonctionnalité incluse |

La distribution des Skills de l’espace de travail ChatGPT, l’installation des Skills sur le système de fichiers local et
l’installation des plugins selon l’interface suivent des processus distincts. Déplacer un Skill ne
transfère ni sa propriété dans l’espace de travail ChatGPT, ni ses paramètres de partage, ni les rôles qui lui sont attribués, ni l’état
d’installation du plugin, ni l’autorisation du connecteur.

Les plugins fonctionnent dans Discussion et Work sur les versions web, de bureau et mobiles de ChatGPT,
dans Codex au sein de l’application de bureau ChatGPT et via le navigateur de plugins de Codex CLI.
Ils ne sont pas disponibles dans l’extension IDE.
Ces interfaces prises en charge récupèrent les plugins publics depuis un seul répertoire universel partagé
par ChatGPT et Codex.

## Contrôles de gestion

Consultez [Créer des Skills](/fr-FR/codex/build-skills) pour savoir où stocker les Skills dans le système de fichiers et comment les créer,
[Skills dans ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
pour connaître les procédures en vigueur dans l’espace de travail, et [Créer des plugins](https://developers.openai.com/plugins/build/plugins) pour
savoir comment préparer des packages de plugins.

Les contrôles de l’espace de travail ChatGPT n’installent ni les Skills du système de fichiers local ni les plugins.
La distribution via le système de fichiers n’attribue aucun statut de propriétaire ni aucun rôle dans l’espace de travail ChatGPT.
L’installation d’un plugin n’accorde pas l’accès à un connecteur, à un serveur MCP ou à un
service connecté. Configurez chaque fonctionnalité depuis l’interface de contrôle qui
en assure la gestion.

## Documentation associée

- [Skills et plugins](/fr-FR/codex/skills-and-plugins)
- [Plugins](/fr-FR/codex/plugins)
- [Créer des Skills](/fr-FR/codex/build-skills)
- [Créer des plugins](https://developers.openai.com/plugins/build/plugins)
- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
- [Contrôles des plugins](/fr-FR/codex/enterprise/apps-and-connectors)
