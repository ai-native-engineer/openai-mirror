<!-- source: https://learn.chatgpt.com/fr-FR/docs/environments/local-environment -->

Les environnements locaux permettent de définir les étapes de configuration des arbres de travail ainsi que les actions courantes d’un projet.

  Les environnements locaux ne sont disponibles que dans Codex, dans l’application de bureau ChatGPT.
  Sélectionnez **Codex** avant de configurer ou d’utiliser un environnement local.

Configurez vos environnements locaux dans le volet des [paramètres de l’application de bureau ChatGPT](codex://settings). Vous pouvez versionner le fichier généré dans le dépôt Git de votre projet afin de le partager avec d’autres personnes.

Codex enregistre cette configuration dans le dossier `.codex` situé à la racine de votre
projet. Si votre dépôt contient plusieurs projets, ouvrez le répertoire du projet
qui contient le dossier partagé `.codex`.

## Scripts de configuration

Comme les arbres de travail utilisent des répertoires différents de ceux de vos discussions locales, votre projet peut ne pas être entièrement configuré et certaines dépendances ou certains fichiers non versionnés dans votre dépôt peuvent manquer. Les scripts de configuration s’exécutent automatiquement lorsque Codex crée un nouvel arbre de travail au début d’une nouvelle discussion.

Utilisez ce script pour exécuter toute commande nécessaire à la configuration de votre environnement, par exemple pour installer des dépendances ou lancer un build.

Par exemple, pour un projet TypeScript, vous pouvez utiliser un script de configuration afin d’installer les dépendances et d’effectuer un premier build :

```bash
npm install
npm run build

Si votre configuration dépend de la plateforme, définissez des scripts de configuration pour macOS, Windows ou Linux afin de remplacer le script par défaut.

## Actions

<section class="feature-grid">

<div>
Utilisez les actions pour définir des tâches courantes, comme démarrer le serveur de développement de votre application ou exécuter votre suite de tests. Ces actions s’affichent dans la barre supérieure de l’application de bureau ChatGPT pour vous permettre d’y accéder rapidement. Elles s’exécutent dans le [terminal intégré](/fr-FR/codex/integrated-terminal) de l’application.

Les actions vous évitent de saisir manuellement des commandes courantes, par exemple pour lancer un build de votre projet ou démarrer un serveur de développement. Pour un débogage rapide et ponctuel, vous pouvez utiliser directement le terminal intégré.

</div>

  
    
  

</section>

Par exemple, pour un projet Node.js, vous pouvez créer une action « Exécuter » contenant le script suivant :

```bash
npm start

Si les commandes de votre action dépendent de la plateforme, définissez des scripts propres à chaque plateforme pour macOS, Windows et Linux.

Pour identifier vos actions, choisissez une icône pour chacune d’elles.

## Utilisez les outils Git intégrés

<div class="my-8 grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-center">

<div>

Dans Codex, l’application de bureau ChatGPT propose des commandes Git courantes pour chaque
projet local et chaque arbre de travail. Le volet des différences affiche les modifications de la version actuellement extraite
et vous permet d’ajouter des commentaires en ligne que Codex pourra prendre en compte. Vous pouvez indexer ou annuler des blocs
de modifications, indexer ou rétablir des fichiers entiers, créer un commit avec vos modifications, pousser une branche et créer
une pull request sans quitter l’application.

Utilisez le [terminal intégré](/fr-FR/codex/integrated-terminal) pour les opérations Git
qui ne sont pas proposées dans l’application. Pour isoler les modifications simultanées de
votre copie de travail locale, démarrez la tâche dans un [arbre de travail](/fr-FR/codex/environments/git-worktrees).

</div>

  

</div>
