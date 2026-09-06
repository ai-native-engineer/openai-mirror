<!-- source: https://learn.chatgpt.com/fr-FR/docs/plugins -->

## Vue d’ensemble

Les plugins regroupent des fonctionnalités dans des workflows réutilisables au sein de ChatGPT et Codex. Ils
peuvent inclure des Skills, des connecteurs ou les deux. Les deux produits partagent un répertoire universel de plugins,
ce qui permet de découvrir les mêmes plugins publics depuis leurs interfaces
compatibles.

Les plugins fonctionnent dans Discussion et Work sur les versions web, de bureau et mobile de ChatGPT,
ainsi que dans Codex au sein de l’application de bureau ChatGPT. Codex CLI propose également un navigateur de plugins
pour les environnements Codex. L’extension IDE ne prend pas en charge les plugins.

Sur mobile, vous pouvez utiliser les plugins disponibles pour votre compte dans Discussion ou Work.

Ouvrez l’onglet **Plugins** pour parcourir et installer des plugins. Après l’installation, vous
pouvez utiliser les plugins dans Discussion ou Work dans ChatGPT, ou dans Codex. Les plugins installés peuvent
ajouter des Skills, des connecteurs et des outils MCP aux nouvelles discussions.

Ouvrez l’onglet **Plugins** pour parcourir et installer des plugins. Après l’installation, vous
pouvez utiliser les plugins dans Discussion ou Work. Un plugin peut vous inviter à connecter un service
externe avant que ses outils ne deviennent disponibles.

Dans Codex CLI, saisissez `/plugins` pour ouvrir le navigateur de plugins. Installez un plugin depuis
une marketplace configurée, puis démarrez une nouvelle session avant d’utiliser les
Skills ou les outils qu’il contient.

<a id="plugin-directory-in-the-ide-extension"></a>

### Utilisez les plugins depuis une interface compatible

Les plugins ne sont pas disponibles dans l’extension IDE. Pour parcourir et installer des plugins
pour Codex, utilisez l’application de bureau ChatGPT ou Codex CLI.

Étendez les capacités de ChatGPT et Codex, par exemple :

- Installez le plugin Codex Security pour analyser le code que vous êtes autorisé à examiner et confirmer
les signalements plausibles de vulnérabilités.
- Installez le plugin Gmail pour travailler avec Gmail.
- Installez le plugin Google Drive pour travailler dans Drive, Docs, Sheets et
Slides.
- Installez le plugin Slack pour résumer des canaux ou rédiger des brouillons de réponse.

Un plugin peut contenir un ou plusieurs des éléments suivants :

- **Skills :** instructions réutilisables pour des types de tâches précis. ChatGPT et
  Codex peuvent les charger au besoin pour suivre les étapes appropriées et utiliser les
  références ou les scripts auxiliaires adaptés à la tâche.
- **Connecteurs :** connexions à des outils comme GitHub, Slack ou Google Drive, qui permettent à
  ChatGPT et Codex de lire les informations qu’ils contiennent et d’y effectuer des
  actions. Les connecteurs mettent des outils à disposition et peuvent aussi inclure une interface utilisateur personnalisée.
- **Serveurs MCP :** services qui donnent à ChatGPT et Codex accès à davantage d’outils ou à
  des informations partagées, provenant souvent de systèmes extérieurs à votre projet local. Ces services
  sont également à la base des connecteurs. Ils définissent les outils, imposent l’authentification, renvoient
  des données structurées et effectuent des actions sur des systèmes externes.
- **Extensions de navigateur :** fonctionnalités du navigateur dont un plugin a besoin pour son
  workflow.
- **Hooks :** commandes exécutées aux étapes configurées du cycle de vie. Examinez les hooks
  du plugin et assurez-vous de pouvoir leur faire confiance avant de les activer.
- **Modèles de tâches planifiées :** points de départ réutilisables pour les tâches récurrentes
  là où les tâches planifiées sont disponibles.

Vous pouvez partager des plugins en les publiant par l’intermédiaire d’une source de marketplace, comme une
marketplace hébergée dans un dépôt pour un projet ou une équipe. Consultez [Créer des plugins](https://developers.openai.com/plugins/build/plugins)
pour obtenir des conseils sur la configuration de la marketplace, la création de packages et la distribution.

Si vous développez une intégration, commencez par
[Créer un serveur MCP](https://developers.openai.com/plugins/build/mcp-server).
Si le plugin nécessite une interface utilisateur personnalisée, consultez le
[guide sur l’ajout facultatif d’une interface utilisateur](https://developers.openai.com/plugins/build/chatgpt-ui).

## Utilisez et installez des plugins

<a id="plugin-directory-in-the-codex-app"></a>

### Répertoire universel de plugins

ChatGPT et Codex utilisent le même catalogue public de plugins. Sur le web ou dans
l’application de bureau ChatGPT, ouvrez l’onglet **Plugins** pour parcourir et installer des plugins.

  
    
  

Le répertoire de plugins classe les plugins dans les onglets suivants :

- **OpenAI :** plugins créés par OpenAI.
- **Nom de votre espace de travail :** plugins fournis par votre espace de travail.
- **Personnel :** plugins de la marketplace personnelle, avec les sections **Créés par moi** et
**Partagés avec moi** lorsque ces plugins sont disponibles.

Consultez la ligne distincte **Installés** pour voir les plugins que vous avez déjà installés.

Les administrateurs d’espace de travail peuvent importer et synchroniser une marketplace GitHub pour leur équipe. Consultez
[Gestion des plugins](/fr-FR/codex/enterprise/plugin-management) pour connaître les prérequis de configuration
et d’accès.

### Installez et utilisez un plugin

Une fois le répertoire de plugins ouvert :

1. Recherchez un plugin ou parcourez le répertoire, puis ouvrez sa fiche.
2. Sélectionnez le bouton plus pour installer le plugin.
3. Si le plugin nécessite un connecteur, connectez-le lorsque vous y êtes invité. Certains plugins
vous demandent de vous authentifier pendant l’installation. D’autres ne le demandent que lors de leur première
utilisation.
4. Après l’installation, démarrez une nouvelle discussion et demandez à ChatGPT ou Codex d’utiliser le
plugin.

### Connectez les services partenaires compatibles avec l’option « Se connecter avec ChatGPT »

L’option **Se connecter avec ChatGPT** est en cours de déploiement en version bêta pour les plugins et
les sites partenaires compatibles, notamment Airtable, GitLab, HubSpot, Notion, Supabase et
Vercel. Lorsque cette option est disponible, sélectionnez **Se connecter avec ChatGPT** lors de
la connexion du plugin pour créer un compte auprès de ce service ou y associer votre compte existant.

La connexion ne transmet au partenaire que votre nom, votre adresse e-mail et votre photo de profil, si elle est
disponible. Elle ne donne pas au plugin accès à vos données et
n’approuve aucune action automatiquement. Examinez et approuvez les autorisations demandées
par le plugin lors d’une étape distincte avant d’utiliser la connexion.

Après avoir installé un plugin, vous pouvez l’utiliser directement dans la zone de saisie :

  
    
  

<div class="not-prose mt-4 grid gap-4 md:grid-cols-2">
  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">Décrivez directement la tâche</p>
    <p class="mt-2 text-sm text-secondary">
      Demandez le résultat souhaité, par exemple « Résumez les fils de discussion Gmail non lus
d’aujourd’hui » ou « Récupérez les dernières notes de lancement depuis Google Drive ».
    </p>
    <p class="mt-3 text-sm text-secondary">
      Utilisez cette méthode si vous souhaitez que ChatGPT choisisse les outils installés adaptés à la
tâche.
    </p>
  </div>

  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">Choisissez un plugin précis</p>
    <p class="mt-2 text-sm text-secondary">
      Saisissez <code>@</code> pour appeler explicitement le plugin ou l’un des Skills
      qu’il contient.
    </p>
    <p class="mt-3 text-sm text-secondary">
      Utilisez cette méthode lorsque vous souhaitez préciser le plugin ou le Skill que ChatGPT
      doit utiliser. Consultez <a href="/codex/skills-and-plugins">Skills et plugins</a>.
    </p>
  </div>
</div>

### Utilisez Apple Messages depuis Codex

Le plugin Apple Messages est disponible avec toutes les offres dans l’application de bureau ChatGPT
pour macOS. Dans Codex et ChatGPT Work, il peut lire les discussions iMessage, SMS et
RCS sur votre Mac, y effectuer des recherches et envoyer des messages en votre nom via l’application Messages.
Il ne permet pas d’interagir à distance avec ChatGPT par Messages et
ne fonctionne pas dans les discussions ChatGPT ordinaires.

Pour cette version, le plugin Messages est inclus uniquement dans la version Apple Silicon
(arm64) de l’application de bureau ChatGPT.

1. Ouvrez **Plugins**, recherchez le plugin Apple Messages et installez-le.
2. Démarrez une nouvelle discussion avec Codex ou ChatGPT Work, puis demandez-lui de rechercher, de résumer, de rédiger
ou d’envoyer un message.
3. Accordez les autorisations macOS demandées avant que ChatGPT ne lise les discussions dans Messages.
4. Vérifiez le message et ses destinataires avant d’autoriser son envoi.

Par défaut, ChatGPT n’envoie un message qu’une fois que vous avez approuvé celui-ci et ses
destinataires. Choisissez **Autoriser une fois** pour approuver uniquement cet envoi. Si vous sélectionnez
**Toujours autoriser l’envoi dans cette discussion**, ChatGPT pourra envoyer d’autres messages dans cette
discussion Messages sans nouvelle approbation d’envoi.

Conservez l’approbation à chaque envoi pour les discussions susceptibles de contenir des instructions non fiables ou
trompeuses. L’approbation permanente vous prive de votre dernière occasion de vérifier un message
avant que ChatGPT ne l’envoie en votre nom. Ne l’utilisez que si vous acceptez ce risque.

Pour rétablir l’approbation à chaque envoi, ouvrez **Paramètres** \> **Utilisation de l’ordinateur** et sélectionnez
**Gérer** à côté de **Messages**. Sous **Envois toujours autorisés**, sélectionnez l’icône
de corbeille à côté de la discussion, puis confirmez en sélectionnant **Supprimer**. ChatGPT vous demandera à nouveau votre approbation
avant d’envoyer un message dans cette discussion.

**Problème connu :** si votre tâche est réglée sur **Accès complet** ou si les demandes
d’approbation y sont désactivées d’une autre manière, Apple Messages peut ne pas pouvoir afficher la confirmation nécessaire
à l’envoi. Passez à **Demander l’approbation** ou **Approuver pour moi** , puis réessayez.

Apple Messages fonctionne sur votre Mac. Il n’est pas directement disponible dans ChatGPT sur le
web ou sur mobile, dans Codex CLI ni dans l’extension IDE.

Dans les espaces de travail gérés, les administrateurs peuvent désactiver Apple Messages à l’aide du
paramètre existant Utilisation de l’ordinateur.

<a id="plugin-directory-in-codex-cli"></a>

### Navigateur de plugins dans Codex CLI

Dans Codex CLI, exécutez la commande suivante pour ouvrir le navigateur de plugins :

```text
codex
/plugins

  
    
  

Le navigateur de plugins de la CLI regroupe les plugins par Marketplace. Utilisez les onglets Marketplace
pour changer de source, ouvrez un plugin pour consulter ses détails, installez ou désinstallez des plugins
de la Marketplace, puis appuyez sur <kbd>Espace</kbd> pour activer
ou désactiver un plugin installé.

<a id="api-key-availability"></a>

### Disponibilité avec une clé API

Si vous [vous connectez à Codex avec une clé API
OpenAI](/fr-FR/codex/auth#sign-in-with-an-api-key), vous pouvez parcourir, installer et gérer
les plugins pris en charge et sélectionnés par OpenAI dans Codex CLI et dans Codex au sein de l’application
de bureau ChatGPT. Certains plugins ne sont pas disponibles avec l’authentification par clé API, car leurs
parcours de connexion nécessitent des fonctionnalités OAuth non prises en charge. Consultez l’utilisation des plugins
sur la [page d’utilisation de la plateforme](https://platform.openai.com/usage).

### Fonctionnement des autorisations et du partage de données

Dans ChatGPT sur le web, Discussion et Work utilisent les autorisations de l’espace de travail et les outils
disponibles dans cette discussion. Les connecteurs nécessitent toujours leur propre authentification et leurs propres droits d’accès.

Lorsqu’une fonctionnalité de plugin s’exécute via un hôte Codex, le [bac à sable et la politique
d’approbation](/fr-FR/codex/agent-approvals-security) de cet hôte s’appliquent.
Les connexions à des services externes utilisent les mécanismes d’authentification et les contrôles
d’accès propres à chaque service.

- Les Skills inclus deviennent disponibles lorsque vous démarrez une nouvelle discussion ou une nouvelle session CLI
après l’installation.
- Si un plugin inclut des connecteurs, le produit utilisé peut vous demander de les installer
ou de vous y connecter lors de la configuration ou de leur première utilisation.
- Si un plugin inclut des serveurs MCP, une configuration ou une authentification supplémentaire
peut être nécessaire avant que vous puissiez les utiliser.
- Lorsque ChatGPT transmet des données via un connecteur inclus, les conditions d’utilisation et la politique de
confidentialité de ce service s’appliquent.

### Supprimer un plugin

Pour supprimer un plugin, ouvrez-le dans un navigateur de plugins pris en charge, puis sélectionnez
**Désinstaller le plugin** lorsque cette action est disponible. Les plugins installés au niveau de l’espace de travail ou
fournis par défaut peuvent ne pas proposer cette action ; ils sont alors gérés par l’administrateur de votre espace
de travail.

La désinstallation d’un plugin supprime son package de l’environnement ChatGPT ou Codex
concerné, mais les connecteurs inclus restent connectés tant que vous n’intervenez pas sur leurs connexions dans
ChatGPT.

## Créer votre propre plugin

Si vous souhaitez créer, tester ou distribuer votre propre plugin, consultez
[Créer des plugins](https://developers.openai.com/plugins/build/plugins). Cette page présente la génération d’une structure de projet en local,
la configuration manuelle d’une Marketplace, le partage dans l’espace de travail, les manifestes de plugins et les recommandations
pour créer le package.

Si votre plugin inclut des fonctionnalités reposant sur un serveur, consultez
[Créer un serveur MCP](https://developers.openai.com/plugins/build/mcp-server).
Les outils MCP peuvent fonctionner sans interface utilisateur personnalisée ou renvoyer une interface lorsqu’un affichage visuel facilite
le workflow.

Lorsque votre plugin est prêt pour la révision, consultez
[Soumettre des plugins](https://developers.openai.com/plugins/deploy/submission) pour connaître le processus de soumission sur la plateforme OpenAI,
les autorisations requises, les éléments à fournir pour la révision, les vérifications MCP et les exigences relatives aux cas
de test.

## Guides sur les plugins

- [Enregistrer et rejouer](/fr-FR/codex/extend/record-and-replay) : montrez à ChatGPT un workflow
  une seule fois, puis transformez-le en skill réutilisable.
- [Plugin Codex Security](/fr-FR/codex/security/plugin) : analysez le code que vous êtes autorisé à examiner,
  confirmez les résultats et préparez des correctifs ayant fait l’objet d’une révision.
