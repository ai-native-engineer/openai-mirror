<!-- source: https://learn.chatgpt.com/fr-FR/docs/whats-new -->

Ce récapitulatif hebdomadaire présente les fonctionnalités de ChatGPT et de Codex qui peuvent changer votre
façon de travailler, avec des exemples et des liens pour en savoir plus. Pour consulter toutes les mises à jour de version, corrections de bugs
et améliorations mineures, reportez-vous au [journal des modifications de Codex](/codex/changelog).

## Du 31 août au 4 septembre 2026

### Accomplissez des tâches exigeantes avec GPT-6 Astra

[GPT-6 Astra](/fr-FR/codex/models#gpt-6-astra) associe un raisonnement avancé, l’utilisation de l’ordinateur
et un meilleur discernement pour réaliser des tâches complexes de programmation, d’utilisation d’applications et de recherche dans
Codex et ChatGPT Work. Utilisez-le pour exécuter un workflow, vérifier le résultat et
produire un document, une feuille de calcul ou une présentation adaptés à vos modèles de documents et
à votre tâche.

Une fois Astra disponible pour votre compte, choisissez-le dans le sélecteur de modèles.
Consultez les [informations sur l’utilisation et les tarifs](/fr-FR/codex/pricing) avant de lancer une tâche importante.
L’accès avec Enterprise nécessite à la fois d’être éligible au déploiement et
qu’un administrateur l’active.

## Du 24 au 28 août 2026

### Travaillez avec davantage de sites web

- **Utilisez votre navigateur :** Travaillez dans [Edge, Brave, Opera ou Vivaldi](/fr-FR/codex/chrome-extension)
  ainsi que dans Chrome depuis l’application de bureau ChatGPT. Intégrez un onglet ouvert à une
  discussion ChatGPT Work ou Codex et utilisez le site web auquel vous êtes déjà
  connecté. Opera prend en charge le contrôle du navigateur, mais pas la discussion latérale.

- **Utilisez les outils d’un site web :** Grâce aux [outils du site (WebMCP)](/fr-FR/codex/webmcp), ChatGPT Work
  et Codex peuvent utiliser les actions proposées par un site web dans le navigateur
  intégré de l’application de bureau. Par exemple, un éditeur de documents peut proposer des outils pour trouver
  une section ou ajouter un commentaire. Mettez à jour l’application de bureau et utilisez GPT-5.6 Sol ou
  GPT-5.6 Terra. Les outils du site ne sont pas disponibles avec GPT-5.6 Luna ni dans les espaces de travail Enterprise
  ou Edu.

- **Connectez-vous via le navigateur cloud :** Avec une offre éligible, poursuivez une tâche
  nécessitant un compte sur un site web dans ChatGPT Work sur le web, iOS ou Android.
  Suivez la [demande de connexion](/fr-FR/codex/browser?surface=web#web-sign-in-to-a-website)
  et saisissez vos identifiants dans le parcours de connexion, pas dans la discussion. Cela ne
  connecte pas le profil de votre navigateur local. La connexion aux sites web n’est pas disponible pour les
  espaces de travail Enterprise ou Edu.

La disponibilité dépend du déploiement et des paramètres de l’espace de travail.

[Consultez les notes de version du 25 août
sur le navigateur](/codex/changelog#codex-2026-08-25-browser).

### Déclenchez des tâches planifiées à partir d’événements dans les applications

Les [tâches planifiées](/fr-FR/codex/automations?surface=web#web-trigger-tasks-from-app-events) peuvent désormais
démarrer lorsqu’un événement pris en charge survient dans Gmail, Slack ou GitHub. Utilisez un déclencheur
d’événement pour trier les nouveaux e-mails, résumer l’activité d’un canal ou donner suite aux commentaires sur une pull request
sans effectuer de vérifications à intervalles réguliers.

Les tâches déclenchées par des événements sont disponibles dans ChatGPT sur le web et sur mobile avec les
offres éligibles. Connectez d’abord l’application concernée et approuvez les accès qu’elle demande. Dans les espaces de travail
gérés, les administrateurs peuvent contrôler l’accès.

<PromptComponent
  prompt={`Lorsque l’une de mes pull requests dans <owner>/<repository> reçoit de nouveaux commentaires de revue, résumez-les et préparez un plan de révision.`}
/>

[Consultez les notes de version
du 25 août](/codex/changelog#codex-2026-08-25-event-triggers).

## Du 17 au 21 août 2026

### Travaillez avec davantage de vos applications et de vos contenus

- **Apple Messages :** [Retrouvez des discussions, résumez les messages, préparez des réponses et envoyez-les avec Messages sur votre Mac](/fr-FR/codex/plugins?surface=app#app-use-apple-messages-from-codex). Ce plugin est disponible avec toutes les offres dans l’application de bureau ChatGPT pour macOS. Utilisez-le dans ChatGPT Work et Codex, et non dans les discussions ChatGPT classiques. Par défaut, ChatGPT envoie des messages uniquement après que vous avez approuvé le message et ses destinataires.

- **Coédition d’un Site :** Si cette fonctionnalité est disponible, [invitez des membres actifs de votre espace de travail comme éditeurs](/fr-FR/codex/sites#collaborate-on-a-site). Les éditeurs peuvent améliorer le Site et publier des mises à jour une fois que son propriétaire l’a publié pour la première fois. Les éditeurs invités peuvent consulter les données de la base de données en production du Site ; les propriétaires conservent le contrôle du partage et des paramètres.

- **URL modifiables des Sites :** Si cette fonctionnalité est disponible, [choisissez une nouvelle adresse hébergée par ChatGPT pour un Site existant](/fr-FR/codex/sites#change-a-site-url) sans le redéployer. L’ancienne adresse redirige vers la nouvelle.

- **Historique de l’ordinateur en Europe :** Utilisez l’[Historique de l’ordinateur](/fr-FR/codex/customization/computer-history) dans l’EEE, en Suisse et au Royaume-Uni. Il reste désactivé par défaut pour les utilisateurs de ChatGPT Pro, Business et Enterprise sur macOS. Les administrateurs Business et Enterprise doivent d’abord activer l’accès.

- **Instantanés partagés des fils de discussion :** [Partagez un instantané en lecture seule d’un fil de discussion Codex local](/fr-FR/codex/use-chatgpt#share-a-read-only-snapshot-of-a-codex-thread) depuis l’application de bureau ChatGPT pour macOS. Les liens associés à un compte personnel sont accessibles à toute personne qui dispose du lien ; ceux associés à un compte d’espace de travail sont limités à l’espace de travail d’origine. Codex masque les secrets correspondant à des motifs connus, mais examinez l’instantané avant de le partager, car des informations sensibles peuvent subsister.

- **Fils épinglés unifiés :** Gardez vos [discussions épinglées](/fr-FR/codex/projects?surface=app#app-organize-projects-and-chats) synchronisées entre l’application de bureau et iOS.

[Consultez les notes de version du 20 août](/codex/changelog#codex-2026-08-20-app).

### Travaillez sur des projets GitLab dans Codex Cloud

La [prise en charge de GitLab](/fr-FR/codex/third-party/gitlab) est disponible en version bêta avec toutes les offres
ChatGPT. Connectez un projet, créez un environnement cloud, lancez des tâches depuis des issues
ou des merge requests avec `@codex`, et demandez des revues ponctuelles ou
automatiques des merge requests.

L’intégration s’exécute dans Codex Cloud et l’administrateur d’un espace de travail géré peut la
désactiver. L’activité déclenchée par GitLab nécessite l’autorisation de configurer le webhook
correspondant. Les connexions GitLab Self-Managed et GitLab Dedicated doivent être configurées
par un administrateur de l’espace de travail ; l’activité des webhooks nécessite GitLab 19.0 ou une version ultérieure.

[Consultez les notes de version GitLab
du 19 août](/codex/changelog#codex-2026-08-19-gitlab).

### Exportez les métadonnées des plugins publics pour les examiner

Les propriétaires et administrateurs éligibles d’espaces de travail ChatGPT Enterprise peuvent télécharger un fichier CSV
répertoriant les plugins publics visibles dans leur espace de travail. Dans
[Administration \> Plugins](https://chatgpt.com/admin/plugins), sélectionnez **Public**, puis
sélectionnez l’icône de téléchargement (**Exporter en CSV**).

L’export répertorie les noms et descriptions des plugins, des applications et des Skills de Discussion, ainsi
que le développeur, la version, la date d’ajout en UTC et les métadonnées de vérification par OpenAI.
Il utilise un instantané du catalogue public pouvant dater de 48 heures au maximum et exclut les
plugins créés pour l’espace de travail. L’export n’est pas disponible dans les espaces de travail
FedRAMP.

[Consultez les notes de version du 17 août sur l’export
pour les administrateurs](/codex/changelog#codex-2026-08-17-admin-csv).

## Du 10 au 14 août 2026

### Retrouvez vos travaux antérieurs grâce à l’Historique de l’ordinateur

L’[Historique de l’ordinateur](/fr-FR/codex/customization/computer-history) transforme l’activité de vos
applications et sites web en une chronologie dans laquelle vous pouvez faire des recherches et en mémoires que ChatGPT
et Codex peuvent utiliser. Activez-le uniquement si vous souhaitez partager ce contexte, puis
choisissez les applications et sites web qui y contribuent. Vous pouvez suspendre la collecte et consulter ou
supprimer votre historique à tout moment.

L’Historique de l’ordinateur est disponible dans l’application de bureau ChatGPT sur macOS pour les clients ChatGPT
Pro, Business et Enterprise. Les administrateurs Business et Enterprise doivent d’abord
activer l’accès. La disponibilité initiale exclut l’Union européenne, la Suisse
et le Royaume-Uni.

### Utilisez l’application de bureau ChatGPT sur Linux

L’[application de bureau ChatGPT pour Linux](/fr-FR/codex/linux/linux-app) est désormais disponible en
préversion. Installez un paquet `.deb` sur les distributions Ubuntu ou Debian prises en charge,
ou un paquet `.rpm` sur Fedora. Ces paquets sont disponibles pour les processeurs x64 et
ARM64.

Connectez-vous à votre compte ChatGPT pour utiliser les projets, les fichiers locaux et
Codex. Certaines fonctionnalités, dont l’Utilisation de l’ordinateur, ne sont pas encore disponibles
dans la préversion Linux.

### Importez la configuration de votre agent et vos travaux existants

[Importez des instructions, des paramètres, des Skills, des plugins, des projets et des travaux
récents](/codex/import) depuis **Claude Code**, <strong>Claude Cowork</strong> ou
**Cursor** dans l’application de bureau ChatGPT. Activez les mises à jour automatiques dans
**Paramètres \> Importation** pour que vos travaux importés restent synchronisés.

Dans Codex CLI, utilisez `/import` pour importer la configuration prise en charge et les discussions récentes de
Claude Code ou de Cursor dans votre session locale.

[Consultez les notes de version du 11 août pour l’application de bureau
et la CLI](/codex/changelog#codex-2026-08-11-app).

### Choisissez l’accès adapté à vos activités de cybersécurité défensive

Daybreak propose désormais deux niveaux d’accès aux professionnels de la cybersécurité défensive ayant obtenu une approbation. **Daybreak Blue** prend en charge
les activités défensives courantes, comme la revue de code axée sur la sécurité, la réponse aux incidents et
la validation des correctifs. **Daybreak Red** nécessite une approbation distincte et donne
accès à des modèles entraînés spécifiquement pour les évaluations de sécurité autorisées.

L’accès nécessite [Trusted Access for
Cyber](/fr-FR/codex/cyber-safety#trusted-access-for-cyber) et se limite
à l’identité, à l’espace de travail ou à l’organisation, au modèle et à l’interface du produit approuvés.

[Consultez l’annonce Daybreak
du 10 août](/codex/changelog#codex-2026-08-10-daybreak).

## Du 3 au 7 août 2026

### Discutez de vos fichiers et projets avec ChatGPT Voix

[ChatGPT Voix](/fr-FR/codex/features/voice) prend désormais en charge les fichiers téléversés et
les [projets ChatGPT](/fr-FR/codex/projects). Posez des questions sur un document lors d’une
conversation vocale, ou poursuivez un projet en vous appuyant sur ses discussions récentes, ses sources et
ses instructions.

### Étudiez et enseignez avec des plugins dédiés à l’éducation

Trois nouveaux [plugins](/fr-FR/codex/plugins) proposent des workflows propres à l’enseignement dans
ChatGPT Work et Codex. **College Student** crée des guides de révision, des quiz
d’entraînement, des cartes mémoire et des explications interactives. **College Educator** aide à
élaborer des plans de cours, des supports et des évaluations. **K–12 Educator** facilite
la préparation des leçons et la création de ressources pour la classe et de supports adaptés aux différents
profils d’élèves.

Les plugins sont disponibles via ChatGPT Edu et les déploiements de ChatGPT for Teachers au sein des districts
scolaires. Les établissements déterminent les outils et les autorisations disponibles. Consultez
l’[annonce des plugins
éducatifs](https://openai.com/index/learn-teach-chatgpt-work-codex/).

### Réutilisez vos fichiers enregistrés et retrouvez plus vite vos travaux précédents

Sur le web, ajoutez à une conversation un fichier enregistré dans la Bibliothèque sans le téléverser
à nouveau, effectuez des recherches dans la Bibliothèque et collez du texte mis en forme sans perdre les titres,
les liens ni les listes. La recherche retrouve aussi les dossiers et les titres de conversation sur le
web, iOS et Android.

Les contenus collés de plus de 10 000 caractères deviennent désormais des pièces jointes avec toutes les offres ChatGPT,
y compris Enterprise et Edu. Sélectionnez **Afficher dans le champ de texte** si vous souhaitez
réintégrer le contenu dans votre message.

Consultez les [notes de version
de ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

### Consultez votre quota d’utilisation restant dans ChatGPT Work

Les utilisateurs éligibles disposant d’une offre personnelle ou de ChatGPT Business peuvent consulter leur quota
d’utilisation restant dans ChatGPT Work directement dans la barre latérale sur le web. Les options de crédits disponibles dépendent
de votre compte et des autorisations de votre espace de travail. ChatGPT Work et Codex continuent de
partager les mêmes [limites d’utilisation et crédits](/fr-FR/codex/pricing).

### Choisissez la façon dont GPT-5.6 répond dans ChatGPT

Les utilisateurs de ChatGPT Plus et Pro peuvent régler le niveau de réflexion que GPT-5.6 Sol consacre à une
réponse grâce à un nouveau curseur. Le modèle mis à jour fournit également des informations factuelles plus fiables
et des réponses plus ciblées. GPT-5.6 Luna devient le modèle par défaut de ChatGPT pour les offres Free
et Go.

Ces changements s’appliquent aux conversations ChatGPT. Ils ne modifient pas le comportement des modèles
dans ChatGPT Work ou Codex. Consultez les [notes de version
de ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).

### Organisez votre travail et changez d’agent dans Codex CLI 0.147.0

[Codex CLI 0.147.0](https://github.com/openai/codex/releases/tag/rust-v0.147.0)
ajoute des sections de discussion persistantes que vous pouvez ordonner manuellement et des Agent Plugins portables.
Effectuez des recherches dans les catalogues de plugins locaux, personnels, de l’espace de travail et distants, ou
[importez la configuration de Cursor et de Claude Code](/fr-FR/codex/import) sans dupliquer
les conversations synchronisées.

Utilisez `--approve-for-me` pour activer la [révision automatique
des demandes d’approbation](/fr-FR/codex/sandboxing/auto-review) éligibles, sans étendre
les autorisations d’accès au système de fichiers ou au réseau. Les sessions Amazon Bedrock bénéficient aussi de la recherche web avec mise en cache
et du compactage des conversations à distance.

### Suivez et reprenez des analyses de sécurité plus approfondies

Les versions `0.1.16` à `0.1.18` du plugin Codex Security hébergé ajoutent le suivi en direct de la
progression des analyses, la mesure de la consommation de tokens, des analyses approfondies pouvant être reprises et des
limites de découverte configurables. La dernière version prend aussi en charge l’authentification via Amazon Bedrock
pour les analyses de dépôts et leurs agents délégués.

Utilisez la [console Codex Security](/fr-FR/codex/security/plugin/workbench) pour examiner
la progression et les résultats des analyses, ou [configurez une analyse
approfondie](/fr-FR/codex/security/plugin/deep-scans) lorsque vous avez besoin d’une évaluation plus
complète. Consultez le [journal des modifications du plugin](/fr-FR/codex/security/plugin/changelog) pour
vérifier les fonctionnalités prises en charge par la version installée.

### Examinez les pull requests GitHub pour détecter les risques de sécurité

[Codex Security Review](/fr-FR/codex/security/security-review) analyse les modifications des pull requests
en tenant compte du contexte du dépôt, des modèles de menace et des consignes de sécurité.
Configurez des revues automatiques à l’ouverture d’une pull request ou à l’ajout de nouveaux
commits, ou demandez-en une directement avec `@codex security review`.

Cette fonctionnalité est disponible en préversion de recherche pour les clients éligibles de ChatGPT Enterprise,
Business, Edu et Pro. Elle n’est pas disponible avec Plus, et des limites d’utilisation
peuvent s’appliquer.

## Du 27 au 31 juillet 2026

### Utilisez GPT-5.6 Terra et Luna à des tarifs réduits

GPT-5.6 Terra coûte désormais 20 % de moins et GPT-5.6 Luna 80 % de moins. Les tarifs des entrées,
des entrées mises en cache et des sorties ont diminué dans les mêmes proportions. Les nouvelles
[limites d’utilisation et grilles tarifaires](/fr-FR/codex/pricing) rendent Terra encore mieux adapté au travail
quotidien et Luna particulièrement utile pour les tâches de programmation ciblées et les tâches à fort volume.

### Retrouvez du contexte utile dans votre navigateur et vos onglets ouverts

Dans l’application de bureau ChatGPT, le [navigateur intégré](/fr-FR/codex/browser) peut retrouver
des pages de votre historique de navigation ou effectuer une recherche Google directement depuis sa barre
d’adresse. ChatGPT peut aussi effectuer des recherches dans votre historique de navigation lorsqu’une tâche nécessite du contexte
antérieur.

L’[extension Chrome](/fr-FR/codex/chrome-extension) permet de mentionner des onglets ouverts,
d’ajouter le texte sélectionné sur une page à une discussion latérale, de poser des questions sur des vidéos YouTube
ou de sélectionner **Demander à ChatGPT** dans le menu contextuel d’une page. Examinez et approuvez
les demandes d’accès à l’historique de navigation avant que ChatGPT n’intègre ces informations dans une
tâche.

### Examinez les modifications dans plusieurs dépôts

Lorsqu’un [projet local contient plusieurs
dossiers](/fr-FR/codex/projects#use-local-projects-for-folders-and-codebases), l’application
de bureau affiche chaque dépôt et les lignes modifiées dans chacun. Sélectionnez
**Révision** pour examiner leurs diffs ensemble sans passer d’une vue de révision
à l’autre.

### Affinez les images générées dans votre conversation

Ouvrez une image générée dans la visionneuse agrandie, puis basculez entre
**Vue ciblée** et **Vue canvas**. Ajoutez des commentaires sur les différentes images, sélectionnez les
versions à conserver et demandez des modifications ciblées sans quitter la discussion.
Découvrez la [génération d’images](/fr-FR/codex/image-generation).

### Retrouvez les discussions qui nécessitent votre attention

La nouvelle **vue Activité** de l’application de bureau regroupe les discussions auxquelles vous avez récemment
participé et le travail qui nécessite votre attention. Sélectionnez la cloche dans la barre latérale
pour ouvrir cette vue.

[Consultez les notes de version du 30 juillet
pour l’application de bureau](/codex/changelog#codex-2026-07-30-app).

### Connectez des outils partenaires avec « Se connecter avec ChatGPT »

L’option **Se connecter avec ChatGPT** est en cours de déploiement en bêta pour les plugins et
sites partenaires compatibles, à commencer par Airtable, GitLab, HubSpot, Notion, Supabase et
Vercel. Utilisez-la pour créer ou associer un compte partenaire en moins d’étapes, puis commencez
à utiliser ce service dans ChatGPT ou Codex.

Les partenaires reçoivent uniquement votre nom, votre adresse e-mail et votre photo de profil lorsqu’elle est
disponible. Les accès demandés par chaque plugin nécessitent toujours un examen
et une approbation distincts. Consultez l’[annonce du 29 juillet sur la
connexion](/codex/changelog#codex-2026-07-29).

### Collaborez dans un espace de travail dédié à la recherche universitaire

[ChatGPT for Academic Researchers](https://openai.com/index/chatgpt-for-academic-researchers/)
offre aux enseignants-chercheurs et aux chercheurs postdoctoraux éligibles 12 mois d’accès gratuit
à un espace de travail ChatGPT dédié. Les équipes approuvées peuvent compter jusqu’à cinq
chercheurs vérifiés d’un même établissement et bénéficient de protections des données
professionnelles et de limites d’utilisation équivalentes à celles de ChatGPT Pro. Les participants peuvent utiliser GPT-5.6
dans ChatGPT, ChatGPT Work et Codex pour leurs workflows de recherche et de programmation.

Le programme couvre l’accès à ChatGPT, mais pas les crédits de l’API OpenAI. La participation nécessite
[une vérification de l’affiliation à un établissement et un article de recherche
répondant aux critères](https://help.openai.com/en/articles/20001406).

### Reprenez vos tâches Codex de façon plus fiable sur iOS

ChatGPT pour iOS 1.2026.202 se reconnecte aux tâches de façon plus fiable lorsque vous revenez dans
l’application ou déverrouillez votre appareil avec Face ID. Les conversations vocales utilisent la voix ChatGPT que vous avez choisie
et affichent des avertissements sur les limites d’utilisation. La zone de saisie suggère désormais les plugins installés
et leurs skills de la même manière que l’application de bureau.

Cette version améliore également les commandes de pause et de reprise des objectifs, les tableaux intégrés
et les thèmes visuels, les diffs volumineux de l’espace de travail, les références au texte sélectionné et la restauration
du modèle. Consultez les [notes de version du 27 juillet
pour iOS](/codex/changelog#codex-2026-07-27-mobile).

### Comparez les analyses de sécurité et gérez les problèmes détectés

Les versions `0.1.14` et `0.1.15` du plugin Codex Security hébergé ajoutent la comparaison des analyses,
le signalement des faux positifs, des politiques `SECURITY.md` à portée définie et des historiques plus clairs des dépôts
et des problèmes détectés. Vous pouvez sélectionner les problèmes à suivre dans Linear ou dans des issues GitHub.
Codex examine l’action proposée avant que vous ne l’approuviez.

Utilisez l’[interface d’analyse de
Codex Security](/fr-FR/codex/security/plugin/workbench) existante pour examiner les analyses enregistrées, les problèmes détectés,
l’historique du dépôt et les mesures correctives dans l’application de bureau. Le catalogue de plugins hébergés
propose la version `0.1.15`, tandis que la marketplace publique de plugins CLI
propose la version `0.1.11`. Consultez le [journal des modifications du plugin
Codex Security](/fr-FR/codex/security/plugin/changelog) avant de vous appuyer sur une nouvelle fonctionnalité.

### Lancez des analyses de sécurité depuis le terminal, la CI ou TypeScript

La CLI et le SDK TypeScript publics de `@openai/codex-security` sont passés à la version
`0.1.5`, avec une numérotation distincte de celle du plugin Codex Security. Utilisez le
package pour [lancer des analyses depuis la CLI](/fr-FR/codex/security/cli), examiner les modifications des pull requests
et téléverser les résultats SARIF dans la [CI](/fr-FR/codex/security/cli/ci), ou lancer
des [analyses en masse](/fr-FR/codex/security/cli/bulk-scans) pouvant être reprises sur des dépôts GitHub
ou à partir d’un inventaire CSV figé.

Le [SDK TypeScript de Codex Security](/fr-FR/codex/security/sdk) permet aussi d’intégrer
les analyses, le suivi de l’avancement, le contrôle des coûts et l’annulation dans vos propres
outils. Le package est public, mais l’exécution d’analyses nécessite toujours un accès
à Codex Security. Certaines analyses de dépôts entiers nécessitent également Trusted Access for Cyber.

### Organisez vos sessions et étendez les fonctionnalités de Codex CLI 0.146.0

[Codex CLI 0.146.0](https://github.com/openai/codex/releases/tag/rust-v0.146.0)
permet de nommer une nouvelle discussion avec `/new release prep` ou `/clear bug bash`, d’épingler
les fils importants et de passer d’une conversation secondaire à l’autre sans les fermer.
Il ajoute aussi la possibilité de forker temporairement des conversations, une recherche web autonome pour les fournisseurs
de modèles personnalisés compatibles, des skills fournis par l’exécuteur, ainsi que la prise en charge des manifestes Agent Plugins,
de la publication de plugins dans l’espace de travail et d’autres marketplaces de plugins.

Pour les clients personnalisés, [App Server](/fr-FR/codex/app-server) peut filtrer les fils
épinglés, les forker en mémoire, inspecter l’état des connecteurs installés et lire
leurs métadonnées. La prise en charge expérimentale de WebSocket permet aussi de connecter app-server à
des hôtes Code Mode distants. Consultez les
[exigences de sécurité d’app-server](/fr-FR/codex/app-server#connect-the-cli-terminal-ui)
avant d’exposer une connexion distante. Cette version améliore aussi la prise en charge des proxys,
la reconnexion MCP, la réactivité du terminal et la fiabilité du bac à sable Windows.

### Utilisez GPT-5.6 Sol pour vos tâches Codex hébergées

[GPT-5.6 Sol](/fr-FR/codex/models#recommended-models) assure désormais la revue de code
et l’assurance qualité dans Codex Cloud pour les clients éligibles. Sol est le modèle phare
de la famille GPT-5.6 pour les tâches complexes de programmation, de recherche, d’utilisation de l’ordinateur et de sécurité.
Codex Cloud sélectionne automatiquement son modèle ; Terra et Luna restent disponibles dans
les interfaces locales et web compatibles.

### Préparez-vous au retrait du modèle GPT-5.4

Le 31 août, GPT-5.4 et GPT-5.4 mini seront retirés de Codex pour les utilisateurs connectés
avec ChatGPT. Remplacez `gpt-5.4` par `gpt-5.6-terra` et `gpt-5.4-mini`
par `gpt-5.6-luna` dans les paramètres par défaut de l’espace de travail, les paramètres de modèle enregistrés, les configurations
gérées, les agents personnalisés et les tâches planifiées.

L’API OpenAI et les sessions Codex authentifiées avec une clé API ne sont pas
concernées. Consultez les [modèles Codex obsolètes](/fr-FR/codex/models#deprecated-codex-models)
et la [disponibilité des modèles dans l’espace
de travail](/fr-FR/codex/enterprise/workspace-model-availability) avant la date
limite.

## 20–24 juillet 2026

### Discutez de votre travail avec ChatGPT Voix

[ChatGPT Voix](/fr-FR/codex/features/voice), qui s’appuie sur GPT-Live, vous permet de discuter
de votre travail et de coordonner des tâches dans Discussion, Work et Codex au sein de l’application de bureau
ChatGPT. Démarrez une nouvelle discussion ou tâche en mode vocal, puis demandez à ChatGPT de lancer, de vérifier ou
d’orienter le travail dans d’autres fils.

Sur macOS, dites « Regardez ceci » pour partager une [capture d’application](/fr-FR/codex/appshots) de
votre fenêtre au premier plan lorsque le **Contexte de l’écran** est activé.

La fonctionnalité Voix est disponible avec les offres Plus, Pro, Business, Edu et Enterprise dans
l’application de bureau et via [À distance sur iOS](/fr-FR/codex/remote-connections#set-up-mobile-access).

### Travaillez dans plusieurs dossiers au sein d’un même projet local

Les projets locaux de l’application de bureau ChatGPT peuvent désormais inclure plusieurs dossiers
connexes. Choisissez un dossier principal pour les nouvelles discussions, les opérations Git et la détection automatique
de `AGENTS.md`, des skills et de `config.toml`. Les dossiers secondaires restent
accessibles pour rechercher, lire et modifier des fichiers.

Ouvrez **Modifier le projet** pour [ajouter des dossiers et choisir le dossier
principal](/fr-FR/codex/projects#use-local-projects-for-folders-and-codebases).

[Consultez les notes de version du 23 juillet](/codex/changelog#codex-2026-07-23-app).

## Du 13 au 17 juillet 2026

### Réunissez les conversations Work et les projets dans l’application de bureau

L’application de bureau ChatGPT réunit désormais les conversations de Discussion et de Work dans la
vue ChatGPT. Les conversations Work dans le cloud se synchronisent entre le web, le mobile et l’application de bureau ;
les conversations Work locales restent sur votre ordinateur. Les projets ChatGPT sont disponibles
dans l’application de bureau. Codex conserve sa vue dédiée et son historique distinct pour
les workflows de développement.

[Comparez ChatGPT Work et Codex dans l’application
de bureau](/fr-FR/codex/use-chatgpt#compare-chatgpt-work-and-codex-on-desktop) pour choisir la
vue adaptée à votre tâche.

### Pilotez les tâches Codex en parallèle avec Codex Micro

Le 15 juillet, OpenAI et Work Louder ont lancé
[Codex Micro](/fr-FR/codex/features/codex-micro), un contrôleur physique en série limitée
pour Codex dans l’application de bureau ChatGPT. Ses touches d’agent affichent l’état de
six discussions au maximum et permettent de passer de l’une à l’autre. Des touches de commande personnalisables, un joystick
analogique et une molette permettent de déclencher des actions courantes ou des skills, d’activer la fonction « appuyer pour parler » et
d’ajuster l’effort de raisonnement sans quitter le clavier.

### Utilisez GPT-5.6 via Amazon Bedrock

GPT-5.6 Sol, Terra et Luna sont désormais en disponibilité générale via Amazon Bedrock.
Les interfaces locales de ChatGPT Work et de Codex peuvent utiliser le
[fournisseur `amazon-bedrock`](/fr-FR/codex/amazon-bedrock) intégré avec une clé API Bedrock ou la
chaîne de résolution des identifiants du SDK AWS. Cela comprend Work et Codex dans l’application de bureau
ChatGPT, Codex CLI, l’extension IDE et le SDK Codex.

### Examinez les visualisations des tâches Codex sur iOS

ChatGPT pour iOS 1.2026.188 a ajouté des visualisations intégrées aux tâches Codex et
amélioré la création et la gestion des tâches depuis les conversations, notamment grâce à des liens
fiables vers les tâches nouvellement créées. Consultez les
[notes de version iOS du 13 juillet](/codex/changelog#codex-2026-07-13-mobile).

## Du 6 au 10 juillet 2026

<a id="take-on-ambitious-work-with-chatgpt-work"></a>

### Menez des projets ambitieux dans ChatGPT

Dans ChatGPT, [ChatGPT Work](/fr-FR/codex/get-started-with-work) peut recueillir du contexte à partir
de vos fichiers et de vos [plugins](/fr-FR/codex/plugins),
agir dans différents workflows et produire des documents, des présentations,
des feuilles de calcul, des Sites et d’autres livrables finalisés que vous pouvez examiner. Grâce à
[GPT-5.6](/fr-FR/codex/models), il peut décomposer un objectif en étapes et travailler pendant des heures tandis que
vous suivez sa progression, répondez aux questions, changez de direction et approuvez
les actions importantes.

Les [tâches planifiées](/fr-FR/codex/automations) peuvent faire avancer ce travail en votre absence
en s’exécutant une seule fois, selon un calendrier, en réponse à un événement ou en surveillant
les changements.

### Choisissez le modèle GPT-5.6 adapté

La [famille GPT-5.6](/fr-FR/codex/models#recommended-models) propose trois modèles recommandés
dans ChatGPT Work, l’application de bureau ChatGPT, Codex CLI et l’extension IDE
Codex. Sol est le modèle phare pour les tâches complexes de programmation, d’utilisation de l’ordinateur, de recherche et
de sécurité. Terra offre un équilibre entre capacités et coût pour le travail quotidien, tandis que Luna
est l’option la plus rapide et la moins chère. Le réglage **Puissance** par défaut utilise Sol avec
un niveau de raisonnement moyen.

### Utilisez Codex dans l’application de bureau ChatGPT

Le 9 juillet, l’application Codex a été intégrée à
l’[application de bureau ChatGPT](/fr-FR/codex/app) sur macOS et Windows. Codex conserve son
expérience dédiée à la programmation, aux côtés de Discussion et de Work dans ChatGPT. Cette expérience
comprend la modification directement dans les diffs, la revue de pull requests dans le panneau latéral, une fonctionnalité
[Utilisation de l’ordinateur](/fr-FR/codex/computer-use) plus rapide grâce à GPT-5.6, ainsi que des projets
regroupant plusieurs dépôts.

Les utilisateurs de l’application Codex peuvent effectuer la mise à jour comme d’habitude. Vous pouvez définir Codex comme vue par défaut,
utiliser le logo Codex comme icône de l’application et accéder aux projets Codex de votre ordinateur depuis
l’application mobile ChatGPT. L’application de bureau mise à jour est disponible dans le monde entier avec toutes
les offres ChatGPT, y compris Free.

## Du 15 au 19 juin 2026

### Transformez vos démonstrations de workflows en skills réutilisables

La fonctionnalité [Enregistrer et rejouer](/fr-FR/codex/extend/record-and-replay) vous permet de montrer à ChatGPT ou
à Codex un workflow sur macOS, puis de transformer cette démonstration en skill réutilisable. Utilisez-la
pour les tâches répétitives plus faciles à montrer qu’à décrire, puis affinez la
skill générée et rejouez-la avec de nouvelles données d’entrée. Elle nécessite la fonctionnalité Utilisation de l’ordinateur et n’est initialement pas disponible
dans l’EEE, au Royaume-Uni ni en Suisse.

<a id="continue-a-task-on-another-host"></a>

### Poursuivez une discussion sur un autre hôte

Le [transfert de discussion](/fr-FR/codex/remote-connections#hand-off-a-chat-between-hosts)
déplace une discussion et son état Git entre votre ordinateur local et un hôte
distant connecté. Codex peut créer ou réutiliser un arbre de travail sur l’hôte de destination, transférer
la discussion et la poursuivre dans le projet correspondant.

Cette même version de l’application de bureau ajoute des actions groupées à l’historique des exécutions planifiées :
vous pouvez ainsi marquer toutes les exécutions comme lues ou archiver ensemble celles qui peuvent l’être.

### Parcourez et examinez les espaces de travail depuis iOS

Dans l’application mobile ChatGPT sur iOS, **À distance** propose désormais un explorateur de fichiers de l’espace de travail, un
sélecteur de répertoire pour les nouvelles discussions, des commandes pour développer ou réduire les diffs et
des options d’approbation MCP propres à une discussion ou valables pour plusieurs discussions.

Le déploiement des fonctionnalités Utilisation de l’ordinateur, Extension Chrome, Mémoires et Chronicle a également commencé
dans l’EEE, au Royaume-Uni et en Suisse. Les Mémoires restent
désactivées par défaut dans ces régions, et Chronicle est une préversion de recherche à activer volontairement
pour les abonnés ChatGPT Pro sur macOS.

Consultez les notes de version du [15 juin pour iOS](/codex/changelog#codex-2026-06-15-mobile),
du [16 juin sur la disponibilité](/codex/changelog#codex-2026-06-16-app) et
du [18 juin pour l’application](/codex/changelog#codex-2026-06-18-app).

## Du 8 au 12 juin 2026

### Déboguez les applications web avec le mode Développeur du navigateur

Le [mode Développeur](/fr-FR/codex/browser?surface=app#app-developer-mode) donne à Codex un accès contrôlé
aux fonctionnalités du Chrome DevTools Protocol dans Chrome et le navigateur
intégré. Codex peut inspecter le trafic réseau, la sortie de la console, les erreurs d’exécution et
l’état de la page pendant qu’il analyse les performances de votre application ou la débogue. Dans la section **Mode Développeur** de
**Paramètres** \> **Navigateur**, activez **Activer l’accès complet à CDP**. Codex demande
une approbation explicite avant d’utiliser cet accès sur un site web.

L’utilisation du navigateur est également jusqu’à deux fois plus rapide, car les optimisations de CDP et des instantanés du DOM
réduisent les allers-retours avec le navigateur.

  
    
  

### Importez votre configuration dans Codex

De nouveaux parcours de migration permettent d’importer les éléments de configuration pris en charge depuis d’autres agents de programmation pendant
la configuration initiale. L’application Codex a également ajouté `/init` pour créer les instructions du projet,
et amélioré la gestion des plugins, le diagnostic du navigateur et les résumés des discussions
terminées.

<a id="set-up-codex-tasks-from-ios"></a>

### Configurez vos discussions Codex depuis iOS

Sur iOS, À distance permet désormais de choisir une branche, de créer un arbre de travail, d’exécuter un script de configuration
de l’environnement, de gérer des objectifs et d’ajouter des commentaires de revue intégrés.

Consultez les notes de version du [9 juin pour l’application](/codex/changelog#codex-2026-06-09-app),
du [9 juin pour iOS](/codex/changelog#codex-2026-06-09-mobile) et
du [11 juin pour l’application](/codex/changelog#codex-2026-06-11-app).

## Du 1er au 5 juin 2026

### Créez et déployez des sites web avec Sites

[Sites](/fr-FR/codex/sites) permet à ChatGPT de créer, d’enregistrer, de déployer et d’inspecter des sites web,
des tableaux de bord, des outils internes, des applications web et des jeux hébergés par OpenAI. Sites dispose d’un
point d’accès dédié dans ChatGPT sur le web et dans l’application de bureau. Vous pouvez y retrouver vos
projets et gérer les valeurs et les secrets de l’environnement hébergé sans mettre en place
une infrastructure de déploiement distincte.

### Utilisez Codex avec Amazon Bedrock

Vous pouvez [utiliser Codex avec Amazon Bedrock](/fr-FR/codex/amazon-bedrock) pour des workflows
locaux avec l’authentification, les contrôles de compte et la facturation gérés par AWS.
La fonctionnalité À distance sur iOS propose désormais aussi un verrouillage facultatif dans l’application, des paramètres de comportement des messages de suivi,
le retour à la ligne dans les diffs et des connexions SSH aux machines Windows. L’application de bureau
s’est enrichie d’options de positionnement du terminal et d’informations sur l’activité dans la vue
Profil.

[Consultez toutes les notes de version de juin 2026](/codex/changelog#month-2026-06).

## Du 25 au 29 mai 2026

### Utilisez les applications Windows et contrôlez Codex à distance

La fonctionnalité [Utilisation de l’ordinateur](/fr-FR/codex/computer-use#windows-foreground-use) permet désormais
de voir, de cliquer et de saisir du texte dans les applications de bureau Windows. Installez le plugin Utilisation de l’ordinateur
avant de commencer. Sur Windows, Codex utilise le bureau actif et prend
le contrôle au premier plan pendant l’exécution de la tâche. Les connexions distantes prennent également en charge
Windows. Dans l’application mobile ChatGPT, ouvrez **À distance** pour commencer à travailler sur un appareil Windows,
ou utilisez un Mac exécutant l’application de bureau ChatGPT et suivez la progression
depuis un autre endroit.

Sur iOS, À distance propose aussi des accès depuis Spotlight et Raccourcis, la consultation des discussions archivées,
`/side` et des options pour enregistrer ou copier les images rendues. L’application de bureau
permet désormais de coordonner les discussions des projets locaux et des arbres de travail, de rechercher des discussions passées par contenu ou
nom de branche, et d’identifier les sous-agents en arrière-plan grâce à des repères visuels
cohérents.

Consultez les notes de version [iOS du 25 mai](/codex/changelog#codex-2026-05-25-mobile) et celles
[de l’application du 29 mai](/codex/changelog#codex-2026-05-28-app).

## Du 18 au 22 mai 2026

### Fournissez à Codex du contexte depuis n’importe quelle application Mac avec les captures d’application

Les [captures d’application](/fr-FR/codex/appshots) transmettent à Codex la fenêtre de l’application au premier plan, avec une
capture d’écran et le texte disponible, lorsque vous appuyez sur les deux touches Commande. Codex obtient ainsi
le contexte de votre travail dans vos outils de design, tableaux de bord, documents et autres applications,
sans que vous ayez à copier, coller ou décrire ce qui s’affiche à l’écran.

### Suivez des objectifs de longue durée

Le [mode objectif](/fr-FR/codex/prompting#goal-mode) n’est plus expérimental et est
disponible dans Codex App, l’extension IDE et la CLI pour des objectifs pouvant nécessiter
des heures ou des jours. L’[utilisation après verrouillage](/fr-FR/codex/computer-use#locked-use) permet à Codex de
poursuivre les tâches approuvées d’utilisation de l’ordinateur après le verrouillage d’un Mac, y compris via
**À distance** dans l’application mobile ChatGPT. Les espaces de travail ChatGPT Business permettent aussi de
[partager des ensembles de plugins réutilisables avec les membres de l’espace de travail](https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace).

[Consultez les notes de lancement du 21 mai](/codex/changelog#codex-2026-05-21).

## Du 11 au 15 mai 2026

### Poursuivez sur mobile le travail commencé sur ordinateur

Dans l’application mobile ChatGPT, **À distance** se connecte à un Mac exécutant
l’application de bureau ChatGPT. Comme le travail s’exécute sur l’hôte connecté, vos projets, fichiers,
informations d’authentification, plugins, skills et configuration restent disponibles lorsque vous
poursuivez depuis votre téléphone. Consultez [Connexions distantes](/fr-FR/codex/remote-connections)
pour configurer un hôte et reprendre le travail depuis un autre appareil.

### Automatisez des workflows de confiance

Les hooks sont désormais en disponibilité générale et permettent d’exécuter des commandes personnalisées à des étapes clés
du cycle de vie de l’agent. Les administrateurs ChatGPT Enterprise peuvent aussi activer
les [jetons d’accès Codex](/fr-FR/codex/enterprise/access-tokens) pour les scripts,
les planificateurs et les runners CI privés de confiance. La documentation destinée aux entreprises couvre désormais
la configuration gérée et les contrôles de Codex.

[Consultez les notes de lancement du 14 mai](/codex/changelog#codex-2026-05-13-app).

## Du 4 au 8 mai 2026

### Travaillez dans plusieurs onglets avec l’extension Chrome

L’[extension Chrome](/fr-FR/codex/chrome-extension) peut travailler en
parallèle dans plusieurs onglets en arrière-plan, sans monopoliser votre navigateur. Vous
contrôlez les sites web que Codex peut utiliser et pouvez ainsi combiner recherche,
saisie de données et vérifications dans différentes applications web au sein d’une même tâche.

Codex App propose aussi la correction du texte dicté et un dictionnaire personnalisé pour les noms,
les chemins de fichiers et les symboles du code. Les propriétaires d’espaces de travail ChatGPT Enterprise peuvent autoriser
les membres à créer des [jetons d’accès Codex](/fr-FR/codex/enterprise/access-tokens) pour
des workflows locaux de confiance et non interactifs.

Consultez les notes de lancement [de l’application du 5 mai](/codex/changelog#codex-2026-05-05-app),
[des jetons d’accès du 5 mai](/codex/changelog#codex-2026-05-05) et
[de Codex pour Chrome](/codex/changelog#codex-2026-05-07).

## Du 20 au 24 avril 2026

### Utilisez GPT-5.5 pour les tâches complexes

À son arrivée dans Codex, [GPT-5.5](/fr-FR/codex/models) est devenu le modèle recommandé pour la plupart
des tâches, avec des atouts pour l’implémentation, le débogage, les tests, l’utilisation de l’ordinateur,
la recherche et la production de livrables aboutis pour les tâches intellectuelles.

### Laissez Codex utiliser le navigateur et examiner les demandes d’approbation

L’[utilisation de l’ordinateur dans le navigateur intégré](/fr-FR/codex/browser?surface=app#app-computer-use-in-the-browser)
permet à Codex de naviguer par clics sur des serveurs de développement locaux et des pages issues de fichiers pour
reproduire les problèmes et vérifier les correctifs. Les demandes d’approbation éligibles peuvent également passer
par une [révision automatique des demandes d’approbation](/fr-FR/codex/sandboxing/auto-review),
qui affiche l’état de la révision et le risque avant l’exécution de l’action.

[Consultez les notes de lancement du 23 avril](/codex/changelog#codex-2026-04-23).

## 13–17 avril 2026

### Prévisualisez votre travail et pilotez vos applications au même endroit

Le [navigateur intégré](/fr-FR/codex/browser?surface=app) s’est enrichi d’aperçus en direct et de commentaires sur les pages,
tandis que la fonction [Utilisation de l’ordinateur](/fr-FR/codex/computer-use) a permis à Codex de voir et de
piloter les applications macOS. Ensemble, ces fonctionnalités ont intégré le développement des éléments visuels et la vérification de bout en bout
à la même tâche que la modification du code.

  
    
  

<a id="start-with-a-task-and-keep-it-moving"></a>

### Commencez par une discussion et continuez à avancer

Les [discussions autonomes](/fr-FR/codex/projects#start-without-a-project) ont permis de
commencer sans choisir de dossier de projet. La même version a ajouté
des [tâches planifiées au sein d’une discussion](/fr-FR/codex/automations#schedule-a-task-inside-a-chat),
le contexte des pull requests, des aperçus de fichiers plus riches et les [Mémoires](/fr-FR/codex/customization/memories) pour
le travail qui se poursuit d’une discussion à l’autre.

[Consultez les notes de version de Codex App du 16 avril](/codex/changelog#codex-2026-04-16-app).

## 6–10 avril 2026

### Passez en revue et publiez des pull requests dans l’application

L’interface de revue s’est enrichie de commentaires repliables au fil du code, de modes de revue intégrés et séparés,
ainsi que d’informations plus claires sur Git et le code source. L’activité des pull requests,
les commentaires et les options de push ont ensuite rejoint l’application, aux côtés des onglets de fichiers de l’espace de travail,
pour vous permettre d’examiner une modification et d’y répondre sans changer d’outil.

Consultez les notes de version de Codex App du [9 avril](/codex/changelog#codex-2026-04-09-app) et du
[10 avril](/codex/changelog#codex-2026-04-10-app), ou
découvrez comment [passer en revue les modifications dans l’application](/fr-FR/codex/code-review?surface=app).

## 23–27 mars 2026

### Regroupez vos workflows dans des plugins

Les [plugins](/fr-FR/codex/plugins) ont été lancés sous forme de packages installables regroupant des skills,
des connecteurs et des serveurs MCP. Ils ont facilité la découverte,
l’installation et le partage de workflows complets. Les pages des plugins et des skills ont aussi été repensées pour présenter plus clairement leur contenu
et leur état. La recherche dans les discussions passées est également arrivée cette semaine-là.

Consultez les notes de version sur la [recherche de tâches](/codex/changelog#codex-2026-03-24-app),
le [lancement des plugins](/codex/changelog#codex-2026-03-25) et
[Codex App](/codex/changelog#codex-2026-03-25-app).

## 16–20 mars 2026

### Forkez une discussion à partir d’un message antérieur et choisissez vos outils dans la zone de saisie

Vous pouviez forker une discussion à partir d’un message antérieur, ce qui permettait d’essayer plus facilement une nouvelle
approche sans perdre le cheminement initial. Les commandes de sélection du modèle et du niveau de raisonnement sont devenues
accessibles pendant la rédaction, les skills activés sont apparus dans le menu `@`, et GPT-5.4
mini a apporté une option plus rapide pour les tâches légères et les sous-agents.

Consultez les notes de version sur [GPT-5.4 mini](/codex/changelog#codex-2026-03-17),
le [contrôle des discussions](/codex/changelog#codex-2026-03-18-app) et
le [menu des skills](/codex/changelog#codex-2026-03-19-app).

## 9–13 mars 2026

### Planifiez votre travail dans l’environnement adapté

Les [tâches planifiées](/fr-FR/codex/automations) pouvaient s’exécuter localement ou dans un arbre de travail
avec un modèle et un niveau de raisonnement définis explicitement. Des modèles réutilisables permettaient de configurer plus rapidement les tâches
courantes, et des thèmes personnalisés facilitaient la personnalisation
de l’espace de travail.

  
    
  

### Laissez Codex examiner la sortie du terminal

Codex a également appris à lire le [terminal intégré](/fr-FR/codex/integrated-terminal#run-and-validate-your-project)
de la discussion en cours. Il pouvait ainsi examiner directement la sortie d’un serveur de développement en cours d’exécution ou d’un build
sans vous demander de la coller.

Consultez les notes de version de Codex App du [11 mars](/codex/changelog#codex-2026-03-11-app) et
du [12 mars](/codex/changelog#codex-2026-03-12-app).

## 2–6 mars 2026

### Exécutez Codex nativement sur Windows

Codex App a été lancée sur [Windows](/fr-FR/codex/windows/windows-app) avec une prise en charge native de PowerShell
et du bac à sable, ainsi que des arbres de travail, des tâches planifiées et des skills. WSL restait
disponible pour les développeurs qui préféraient un environnement Linux.

  
    
  

<a id="move-tasks-between-local-and-worktree"></a>

### Déplacez des discussions entre Local et Worktree

[Le transfert entre Local et Worktree](/fr-FR/codex/environments/git-worktrees#working-between-local-and-worktree)
a permis de déplacer une discussion en cours tout en préservant son contexte. GPT-5.4
est également arrivé dans Codex cette semaine-là pour la programmation, l’utilisation de l’ordinateur et les workflows
nécessitant un contexte plus long.

Consultez les notes de version sur le [lancement sur Windows](/codex/changelog#codex-2026-03-04-app),
le [transfert entre Local et Worktree](/codex/changelog#codex-2026-03-03-app) et
[GPT-5.4](/codex/changelog#codex-2026-03-05).

## 9–13 février 2026

### Itérez en temps réel et forkez une discussion pour explorer une autre approche

GPT-5.3-Codex-Spark a été lancé en préversion de recherche comme modèle aux réponses quasi instantanées pour
itérer sur du code en temps réel. L’application a également intégré la possibilité de forker une discussion et une
fenêtre de discussion flottante, toujours au premier plan, pour explorer une autre approche ou
garder Codex à côté d’un éditeur ou d’un navigateur.

Consultez les notes de version de [Spark](/codex/changelog#codex-2026-02-12) et de
[Codex App](/codex/changelog#codex-2026-02-12-app), ou la
version actuelle du [guide des modèles](/fr-FR/codex/models).

## 2–6 février 2026

### Lancement de Codex App sur macOS

À son lancement, Codex App offrait un espace de travail sur ordinateur avec des discussions menées en parallèle dans les projets,
une fonction intégrée de révision Git, des arbres de travail, des skills, des tâches planifiées et la dictée vocale.
Ces fonctionnalités sont désormais disponibles dans Codex, au sein de l’[application de bureau ChatGPT](/fr-FR/codex/app).

  
    
  

### Réorientez le travail en cours et ajoutez des fichiers

Il est devenu possible de réorienter Codex sans interrompre sa
réponse en cours, et de joindre d’autres fichiers que des images. Ces possibilités
ont posé les bases de la [réorientation et de la mise en file d’attente](/fr-FR/codex/prompting#steering-and-queuing)
des demandes suivantes, avec le contexte nécessaire à Codex.

Consultez les [notes de lancement de Codex App](/codex/changelog#codex-2026-02-02) et
les [notes de version de l’application du 5 février](/codex/changelog#codex-2026-02-05-app).
