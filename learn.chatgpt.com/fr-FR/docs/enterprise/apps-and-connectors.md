<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/apps-and-connectors -->

Les plugins regroupent des workflows réutilisables et peuvent inclure des Skills et des applications qui se connectent
à d’autres outils. ChatGPT et Codex utilisent le même répertoire public de plugins sur
les interfaces prises en charge, tandis que les administrateurs décident quels plugins sont disponibles dans leur espace de travail.
Découvrez les [plugins](/fr-FR/codex/plugins),
les [Skills](/fr-FR/codex/skills-and-plugins) et
les [applications et connecteurs](https://help.openai.com/en/articles/11487775).

Un membre ne peut utiliser une capacité reposant sur un connecteur que si le plugin et l’application sont
disponibles pour son rôle et s’il a accès au service connecté.

Les plugins fonctionnent dans Discussion et Work sur les versions web, de bureau et mobile de ChatGPT,
dans Codex au sein de l’application de bureau ChatGPT et via le navigateur de plugins de Codex CLI.
Ils ne sont pas disponibles dans l’extension IDE.

Pour comprendre comment ces contrôles s’articulent avec les rôles et les autorisations de l’espace de travail, consultez
[Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions).

## Comprenez la chaîne de contrôle des capacités

Un plugin peut relever des niveaux de contrôle suivants :

| Niveau                   | Ce qu’il détermine                                                           | Où le gérer                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Disponibilité            | La disponibilité du package du plugin pour l’utilisateur                           | [Paramètres de l’espace de travail](https://chatgpt.com/admin/settings) pour les interfaces web et de bureau prises en charge ; navigateur de plugins pour la CLI |
| Skills incluses         | Les instructions réutilisables fournies par le plugin installé                 | Le package du plugin et les [Contrôles des Skills](/fr-FR/codex/enterprise/skills)                                                               |
| Accès aux applications              | L’accès des utilisateurs aux capacités reposant sur un connecteur                          | [Applications de l’espace de travail](https://chatgpt.com/admin/ca) et [Autorisations et rôles](https://chatgpt.com/admin/settings)                    |
| Actions et autorisations | Les actions que les utilisateurs peuvent exécuter et les situations où ChatGPT demande confirmation avant d’utiliser le connecteur | Le contrôle des actions du connecteur et les autorisations de l’application dans [Applications de l’espace de travail](https://chatgpt.com/admin/ca)                            |
| Autorisation d’accès au service   | Les données et actions externes auxquelles l’identité authentifiée peut accéder        | Le service connecté et son fournisseur d’identité                                                                                 |
| Autorisations d’exécution     | Ce qu’un agent peut faire après avoir reçu des données ou un outil                        | Les contrôles de l’environnement d’exécution, du bac à sable et des approbations pour l’interface active                                                              |

Appuyez-vous sur ces niveaux pour un déploiement en deux étapes : mettez d’abord les plugins appropriés à disposition,
puis configurez les capacités et les autorisations nécessaires à chaque workflow.

## Étape 1 : rendez les plugins disponibles

Sur les interfaces web et de bureau prises en charge, les contrôles des plugins de l’espace de travail déterminent
quels rôles peuvent utiliser ou installer un plugin. Codex CLI utilise son propre navigateur de plugins
pour l’installation. Consultez
[Créer des plugins](https://developers.openai.com/plugins/build/plugins) pour en savoir plus sur
la création et la distribution de packages.

Pour importer des plugins depuis GitHub dans votre espace de travail et les maintenir à jour, consultez
[Gestion des plugins](/fr-FR/codex/enterprise/plugin-management).

### Exportez le catalogue public pour l’examiner

Les propriétaires et administrateurs éligibles d’espaces de travail ChatGPT Enterprise peuvent télécharger un fichier CSV
répertoriant les plugins publics disponibles dans leur espace de travail. Utilisez cet export pour examiner
les métadonnées des plugins, des applications et des Skills avant de modifier la disponibilité des plugins.

1. Ouvrez [Admin \> Plugins](https://chatgpt.com/admin/plugins).
2. Sélectionnez **Public**.
3. Sélectionnez l’icône de téléchargement (**Exporter le CSV**) dans l’en-tête de la page.

Le fichier téléchargé porte le nom `public-plugins-security-review.csv` et contient :

- Métadonnées du plugin : `Plugin Name`, `Plugin Description`, `Date Added (UTC)`,
`OpenAI Verified`, `Developer Name` et `Version`.
- Métadonnées des applications : `App Name(s)` et `App Description(s)`.
- Métadonnées des Skills de Discussion : `Skill Name(s)` et `Skill Description(s)`.

Lorsqu’un plugin comprend plusieurs applications ou Skills, des points-virgules séparent les
valeurs correspondantes. L’export repose sur un instantané du catalogue public pouvant dater
de 48 heures au maximum,
comprend uniquement les plugins publics visibles dans l’espace de travail actuel et n’inclut pas
les plugins créés pour cet espace. Il n’est pas disponible dans les espaces de travail
FedRAMP.

## Étape 2 : gérez les capacités

  Rendre une application ou un plugin disponible dans ChatGPT ne donne pas accès aux fichiers,
aux enregistrements ni aux actions du service connecté. Avant de résoudre un problème ou
d’élargir l’accès, vérifiez le rôle du membre dans l’espace de travail et les paramètres des actions
approuvées. Vérifiez ensuite que le compte authentifié ou la connexion partagée dispose des
autorisations attendues dans le service connecté.

Les plugins de ChatGPT et de Codex peuvent inclure des connecteurs capables de rechercher, récupérer ou synchroniser des données,
ou d’agir sur des systèmes externes. La disponibilité des plugins et les droits d’accès et d’action
accordés à chaque connecteur relèvent de contrôles distincts.

Gérez les capacités reposant sur des connecteurs depuis
[Applications de l’espace de travail](https://chatgpt.com/admin/ca) et
[Autorisations et rôles](https://chatgpt.com/admin/settings). Les contrôles disponibles
permettent aux administrateurs d’effectuer les opérations suivantes :

- Activez les applications ou les connecteurs et attribuez les accès en fonction du rôle dans l’espace de travail.
- Pour les connecteurs qui prennent en charge le contrôle des actions, autorisez les actions en lecture seule ou un
ensemble personnalisé approuvé, et précisez comment l’espace de travail gère les actions nouvellement ajoutées.
- Définissez les autorisations des applications qui déterminent quand ChatGPT demande confirmation avant d’utiliser une application.
- Veillez à ce que l’accès respecte les portées et les autorisations accordées par chaque service connecté
et chaque utilisateur authentifié.

Pour connaître la disponibilité actuelle et les procédures à suivre, consultez
[Contrôles d’administration, sécurité et conformité dans les applications](https://help.openai.com/en/articles/11509118).

<a id="choose-a-starting-set-of-apps"></a>

## Commencez par une sélection ciblée

Commencez par les plugins qui répondent à un besoin métier clairement identifié. Décidez, pour chaque plugin, s’il doit être mis
à la disposition de tous, réservé à un rôle ou à un groupe pilote, ou soumis
à un examen complémentaire.

Pour chaque service connecté, consignez le responsable métier, les données autorisées, les actions
de lecture ou d’écriture approuvées, la méthode d’authentification et un contact pour l’assistance ou le retrait.

Avant d’activer des actions d’écriture ou de publier une nouvelle capacité connectée, vérifiez
son périmètre d’accès par rôle et testez-la avec un compte disposant uniquement des autorisations prévues
dans le service connecté.

Pour un déploiement à grande échelle, commencez par les catégories que les équipes utilisent chaque jour, comme la messagerie,
les calendriers et les systèmes de gestion de fichiers ou de documents. Consultez le
[Répertoire des plugins](https://chatgpt.com/apps) pour vérifier la disponibilité actuelle
et les capacités proposées dans les interfaces ChatGPT et Codex prises en charge.

Quelle que soit votre sélection initiale, commencez par les actions de lecture. Avant d’activer les actions
d’écriture, identifiez le responsable du plugin, examinez les portées du connecteur et les autorisations
du service, confirmez l’accès aux données et documentez les effets sur les systèmes externes ainsi qu’une procédure
de récupération.

## Comprenez les flux de données et la sécurité

Lorsque ChatGPT utilise une application ou un connecteur inclus dans un plugin, il envoie une requête
au service connecté et renvoie des données ou des résultats d’actions, dans la limite des autorisations
de l’utilisateur authentifié dans ce service.

ChatGPT traite les données des applications connectées de deux manières :

- **Sans synchronisation :** ChatGPT traite temporairement les données issues de Discussion et de la recherche approfondie
  sans les indexer.
- **Avec synchronisation :** ChatGPT indexe à l’avance les contenus sélectionnés provenant des services connectés. Vous pouvez vérifier
  sur la page du plugin si une application prend en charge la synchronisation.

Le mode utilisé modifie la manière dont ChatGPT indexe les contenus des services connectés ; il ne remplace pas
les contrôles habituels de conservation des conversations. Les conversations ChatGPT qui utilisent des applications restent
accessibles via l’API de conformité.

La documentation d’OpenAI sur les applications décrit le chiffrement en transit et au repos, les autorisations
par utilisateur, les contrôles des rôles et des actions, les restrictions d’accès réseau pour
les conversations qui utilisent des applications, ainsi que l’absence d’entraînement des modèles sur les informations consultées
via les applications pour les clients Business, Enterprise et Edu. Lorsqu’une requête parvient
à un service connecté, les périmètres d’autorisation de ce service, ses règles de conservation et de résidence des données,
ainsi que ses autres politiques s’appliquent également.

Consultez les rubriques [sécurité et conformité des applications](https://help.openai.com/en/articles/11509118)
et [applications avec synchronisation](https://help.openai.com/en/articles/10847137) pour connaître les modalités actuelles de
traitement des données. Pour les serveurs MCP configurés localement dans l’application de bureau
ChatGPT, Codex CLI ou l’extension IDE, consultez la
[configuration MCP de Codex](/fr-FR/codex/extend/mcp).

## Utilisez les procédures et références à jour

- [Contrôles d’administration, sécurité et conformité dans les applications](https://help.openai.com/en/articles/11509118)
- [Applications dans ChatGPT](https://help.openai.com/en/articles/11487775)
- [Applications avec synchronisation](https://help.openai.com/en/articles/10847137)
- [Gestion des paramètres de l’espace de travail](https://help.openai.com/en/articles/8411955)
- [Plugins](/fr-FR/codex/plugins)
- [Skills et plugins](/fr-FR/codex/skills-and-plugins)
- [Créer des plugins](https://developers.openai.com/plugins/build/plugins)
- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
