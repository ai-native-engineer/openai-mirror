<!-- source: https://learn.chatgpt.com/fr-FR/docs/reference/troubleshooting -->

## Questions fréquentes

### Des fichiers que Codex n’a pas modifiés apparaissent dans le volet latéral

Si votre projet se trouve dans un dépôt Git, le volet de révision affiche automatiquement
les modifications selon l’état Git de votre projet, y compris celles que Codex
n’a pas effectuées.

Dans le volet de révision, vous pouvez alterner entre les modifications indexées et celles qui ne le sont pas encore,
et comparer votre branche à main.

Pour n’afficher que les modifications du dernier tour de Codex, basculez le volet des
différences vers la vue **Dernier tour**.

[En savoir plus sur l’utilisation du volet de révision](/fr-FR/codex/code-review?surface=app).

### Supprimer un projet de la barre latérale

Pour supprimer un projet de la barre latérale, survolez son nom, cliquez
sur les trois points et choisissez « Supprimer ». Pour le restaurer, ajoutez de nouveau
le projet à l’aide du bouton **Ajouter un projet** à côté de **Discussions** ou avec

<kbd>Cmd</kbd>+<kbd>O</kbd>.

<a id="find-archived-threads"></a>
<a id="find-archived-tasks"></a>

### Trouver les discussions archivées

Les discussions archivées se trouvent dans [Paramètres](codex://settings). Lorsque vous désarchivez
une discussion, elle réapparaît à son emplacement d’origine dans la barre latérale.

<a id="only-some-threads-appear-in-the-sidebar"></a>
<a id="only-some-tasks-appear-in-the-sidebar"></a>

### Seules certaines discussions apparaissent dans la barre latérale

La barre latérale vous permet de filtrer les discussions selon l’état d’un projet. Si certaines
discussions manquent, sélectionnez l’icône de filtre à côté de **Discussions**, puis choisissez
**Chronologique**. Si la discussion n’apparaît toujours pas, ouvrez
[Paramètres](codex://settings) et consultez **Discussions archivées**.

### Le code ne s’exécute pas dans un arbre de travail

Les arbres de travail sont créés dans un autre répertoire et héritent par défaut des fichiers versionnés dans
Git. Selon la façon dont vous gérez les dépendances et les outils de votre
projet, vous devrez peut-être exécuter des scripts de configuration dans votre arbre de travail à l’aide d’un
[environnement local](/fr-FR/codex/environments/local-environment) ou copier les fichiers de configuration ignorés
à l’aide de [`.worktreeinclude`](/fr-FR/codex/environments/git-worktrees#copy-ignored-local-files-into-managed-worktrees).
Vous pouvez également récupérer ces modifications dans votre projet local habituel. Consultez
la [documentation sur les arbres de travail](/fr-FR/codex/environments/git-worktrees) pour en savoir plus.

### L’App ne détecte pas l’environnement local partagé d’un membre de l’équipe

La configuration de l’environnement local doit se trouver dans le dossier `.codex`, à la
racine de votre projet. Si vous travaillez dans un monorepo comportant plusieurs
projets, veillez à ouvrir le projet à partir du répertoire qui contient le
dossier `.codex`.

### Codex demande l’accès à Apple Music

Selon votre tâche, Codex peut avoir besoin de parcourir le système de fichiers. Certains
répertoires de macOS, notamment Musique, Téléchargements ou Bureau, nécessitent une
approbation supplémentaire de votre part. Si Codex doit lire votre répertoire de départ,
macOS vous demande d’autoriser l’accès à ces dossiers.

<a id="automations-create-many-worktrees"></a>

### Les tâches planifiées créent de nombreux arbres de travail

Des tâches planifiées fréquentes peuvent créer de nombreux arbres de travail au fil du temps. Archivez les exécutions
planifiées dont vous n’avez plus besoin et évitez de les épingler, sauf si vous souhaitez conserver leurs
arbres de travail.

### Récupérer un prompt après avoir sélectionné la mauvaise cible

Si vous avez lancé par erreur une discussion avec la mauvaise cible (**Local**, **Worktree** ou **Cloud**), annulez l’exécution en cours et récupérez votre prompt précédent en appuyant sur la touche Flèche vers le haut dans la zone de saisie.

### Une fonctionnalité fonctionne dans la CLI Codex, mais pas dans l’application de bureau ChatGPT

L’application de bureau ChatGPT et la CLI Codex peuvent intégrer des versions différentes de Codex. Par conséquent,
les fonctionnalités peuvent être disponibles dans une interface avant l’autre. Les fonctionnalités expérimentales peuvent
également être proposées d’abord dans la CLI Codex.

Pour connaître la version de la CLI Codex installée sur votre système, exécutez :

```bash
codex --version

Pour connaître la version de Codex fournie avec votre application de bureau ChatGPT, utilisez le
chemin conservé vers le paquet de compatibilité `Codex.app` :

```bash
/Applications/Codex.app/Contents/Resources/codex --version

## Commentaires et journaux

Saisissez <kbd>/</kbd> dans la zone de saisie pour envoyer vos commentaires à l’équipe. Si
vous lancez cet envoi depuis une discussion existante, vous pouvez choisir de partager la
session existante avec vos commentaires. Une fois ceux-ci envoyés,
vous recevrez un ID de session que vous pourrez communiquer à l’équipe.

Pour signaler un problème :

1. Recherchez les [issues existantes](https://github.com/openai/codex/issues) dans le dépôt GitHub de Codex.
2. [Ouvrez une nouvelle issue GitHub](https://github.com/openai/codex/issues/new?template=2-bug-report.yml&steps=Uploaded%20thread%3A%20019c0d37-d2b6-74c0-918f-0e64af9b6e14)

D’autres journaux sont disponibles aux emplacements suivants :

- Journaux de l’App (macOS) : `~/Library/Logs/com.openai.codex/YYYY/MM/DD`
- Transcriptions des sessions : `$CODEX_HOME/sessions` (par défaut : `~/.codex/sessions`)
- Sessions archivées : `$CODEX_HOME/archived_sessions` (par défaut : `~/.codex/archived_sessions`)

Si vous partagez des journaux, examinez-les d’abord pour vérifier qu’ils ne contiennent pas d’informations
sensibles.

## Blocages et méthodes de récupération

Si une discussion semble bloquée :

1. Vérifiez si Codex attend une approbation.
2. Ouvrez le terminal et exécutez une commande simple, comme `git status`.
3. Démarrez une nouvelle discussion avec un prompt plus court et plus ciblé.

Si vous annulez par erreur la création d’un arbre de travail et perdez votre prompt, appuyez sur la touche Flèche vers le
haut dans la zone de saisie pour le récupérer.

## Problèmes liés au terminal

**Le terminal semble bloqué**

1. Fermez le panneau du terminal.
2. Rouvrez-le avec <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
3. Réexécutez une commande simple, comme `pwd` ou `git status`.

Si les commandes ne se comportent pas comme prévu, vérifiez d’abord le répertoire courant et
la branche active dans le terminal.

S’il reste bloqué, attendez la fin de vos discussions en cours, puis redémarrez l’application.

**Les polices ne s’affichent pas correctement**

Codex utilise la même police dans le volet de révision, le terminal intégré et pour tout autre code affiché dans l’application. Vous pouvez configurer cette police dans le volet [Paramètres](codex://settings), sous **Police du code**.
