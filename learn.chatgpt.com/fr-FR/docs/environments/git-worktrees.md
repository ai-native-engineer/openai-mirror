<!-- source: https://learn.chatgpt.com/fr-FR/docs/environments/git-worktrees -->

Les arbres de travail permettent à Codex d’exécuter plusieurs discussions indépendantes dans un même projet sans qu’elles interfèrent entre elles. Le dépôt, l’arbre de travail et les commandes restent sur l’ordinateur ou dans l’environnement de développement distant qui contient le projet. Vous pouvez travailler directement dans l’application de bureau ChatGPT ou utiliser [À distance](/fr-FR/codex/remote) dans l’application mobile ChatGPT pour démarrer, piloter, approuver et examiner des discussions dans un arbre de travail sur un ordinateur connecté.

Dans les dépôts Git, les [tâches planifiées](/fr-FR/codex/automations) peuvent s’exécuter dans des arbres de travail dédiés en arrière-plan afin de ne pas entrer en conflit avec votre travail en cours. Dans les projets sans contrôle de version, les tâches planifiées s’exécutent directement dans le répertoire du projet. Vous pouvez également démarrer manuellement des discussions dans un arbre de travail et utiliser la fonction Transfert pour déplacer une discussion entre Local et Worktree.

  Les arbres de travail ne s’exécutent pas localement sur votre téléphone. Avec la fonctionnalité À distance, l’application mobile
contrôle Codex sur votre ordinateur connecté, où restent le dépôt et l’arbre de travail,
ou dans l’environnement de développement distant utilisé par cet ordinateur. Les
instructions ci-dessous propres à l’application de bureau s’appliquent à l’ordinateur connecté.

## Qu’est-ce qu’un arbre de travail ?

Les arbres de travail fonctionnent uniquement dans les projets qui font partie d’un dépôt Git, car ils s’appuient sur les [arbres de travail Git](https://git-scm.com/docs/git-worktree). Un arbre de travail vous permet de créer une seconde copie (« copie de travail ») de votre dépôt. Chaque arbre de travail possède sa propre copie de tous les fichiers du dépôt, mais tous partagent les mêmes métadonnées (dossier `.git`) relatives aux commits, aux branches, etc. Vous pouvez ainsi extraire plusieurs branches et travailler dessus en parallèle.

## Terminologie

- **Copie de travail locale** : le dépôt que vous avez créé. Elle est parfois simplement appelée **Local** dans l’application de bureau ChatGPT.
- **Worktree** : un [arbre de travail Git](https://git-scm.com/docs/git-worktree) créé à partir de votre copie de travail locale dans l’application de bureau ChatGPT.
- **Transfert** : le processus qui déplace une discussion entre Local et Worktree. Codex prend en charge les opérations Git nécessaires pour déplacer votre travail en toute sécurité de l’un à l’autre.

## Pourquoi utiliser un arbre de travail ?

1. Travaillez en parallèle avec Codex sans perturber votre configuration Local actuelle.
2. Mettez des tâches en file d’attente pour les exécuter en arrière-plan, tout en restant concentré sur votre travail au premier plan.
3. Transférez ensuite une discussion vers Local lorsque vous souhaitez examiner ou tester le travail, ou collaborer plus directement.

## Bien démarrer

Les arbres de travail nécessitent un dépôt Git. Vérifiez que le projet sélectionné se trouve dans un tel dépôt.

1.  Sélectionnez « Worktree »

    Dans la vue d’une nouvelle discussion, sélectionnez **Worktree** sous la zone de saisie.
    Si vous le souhaitez, choisissez un [environnement local](/fr-FR/codex/environments/local-environment) afin d’exécuter des scripts de configuration pour l’arbre de travail.

2.  Sélectionnez la branche de départ

    Sous la zone de saisie, choisissez la branche Git sur laquelle baser l’arbre de travail. Il peut s’agir de votre branche `main` / `master`, d’une branche de fonctionnalité ou de votre branche actuelle avec des modifications locales non indexées.

3.  Envoyez votre prompt

    Envoyez votre prompt : Codex crée alors un arbre de travail Git basé sur la branche sélectionnée. Par défaut, Codex travaille avec une [« HEAD détachée »](https://git-scm.com/docs/git-checkout#_detached_head).

4.  Choisissez où poursuivre votre travail

    Quand vous le souhaitez, vous pouvez continuer à travailler directement dans l’arbre de travail ou transférer la discussion vers votre copie de travail locale. Un transfert depuis ou vers Local déplace votre discussion _et_ votre code pour vous permettre de continuer dans l’autre copie de travail.

## Travailler entre Local et Worktree

Les arbres de travail ressemblent beaucoup à votre copie de travail locale et s’utilisent de façon similaire. La différence tient à leur place dans votre workflow. Vous pouvez considérer Local comme le premier plan et Worktree comme l’arrière-plan. La fonction Transfert vous permet de déplacer une discussion de l’un à l’autre.

En coulisses, la fonction Transfert prend en charge les opérations Git nécessaires pour déplacer votre travail en toute sécurité entre deux copies de travail. C’est important, car **Git ne permet d’extraire une branche qu’à un seul emplacement à la fois**. Si vous extrayez une branche dans un arbre de travail, vous **ne pouvez pas** l’extraire en même temps dans votre copie de travail locale, et inversement.

En pratique, deux approches sont courantes :

1. [Travaillez exclusivement dans l’arbre de travail](#option-1-working-on-the-worktree). Cette approche convient surtout lorsque vous pouvez vérifier les modifications directement dans l’arbre de travail, par exemple parce que vous avez installé les dépendances et les outils à l’aide d’un [script de configuration de l’environnement local](/fr-FR/codex/environments/local-environment).
2. [Transférez la discussion vers Local](#option-2-handing-a-chat-off-to-local). Choisissez cette approche pour ramener la discussion au premier plan, par exemple si vous souhaitez examiner les modifications dans votre IDE habituel ou ne pouvez exécuter qu’une seule instance de votre application.

### Option 1 : travailler dans l’arbre de travail

<div class="feature-grid">

<div>

Si vous souhaitez conserver vos modifications dans l’arbre de travail et y travailler exclusivement, créez-y une branche à l’aide du bouton **Créer une branche ici** dans l’en-tête de la discussion.

Vous pouvez ensuite effectuer un commit de vos modifications, pousser votre branche vers votre dépôt distant et ouvrir une pull request sur GitHub.

Vous pouvez ouvrir l’arbre de travail dans votre IDE à l’aide du bouton « Ouvrir » de l’en-tête, utiliser le terminal intégré ou effectuer toute autre opération nécessaire depuis le répertoire de l’arbre de travail.

</div>

  
    
  

</div>

N’oubliez pas que si vous créez une branche dans un arbre de travail, vous ne pouvez l’extraire dans aucun autre arbre de travail, y compris votre copie de travail locale.

<a id="option-2-handing-a-thread-off-to-local"></a>
<a id="option-2-handing-a-chat-off-to-local"></a>
<a id="option-2-handing-a-task-off-to-local"></a>

### Option 2 : transférer une discussion vers Local

<div class="feature-grid">

<div>

Pour ramener une discussion au premier plan, sélectionnez **Transférer** dans son en-tête, puis déplacez-la vers **Local**.

Cette approche est adaptée si vous souhaitez consulter les modifications dans la fenêtre habituelle de votre IDE, exécuter votre serveur de développement existant ou valider le travail dans l’environnement que vous utilisez déjà au quotidien.

Codex prend en charge les opérations Git nécessaires pour transférer en toute sécurité la discussion entre l’arbre de travail et votre copie de travail locale.

Chaque discussion reste associée au même arbre de travail au fil du temps. Si vous la retransférez ultérieurement vers un arbre de travail, Codex la replace dans ce même environnement en arrière-plan afin que vous puissiez reprendre là où vous en étiez.

</div>

  
    
  

</div>

L’inverse est également possible. Si vous travaillez déjà dans Local et souhaitez libérer le premier plan, utilisez **Transférer** pour déplacer la discussion vers un arbre de travail. Cette option est utile si vous voulez que Codex continue à travailler en arrière-plan pendant que vous vous recentrez sur une autre tâche en local.

Comme la fonction Transfert utilise des opérations Git, les fichiers répertoriés dans votre fichier `.gitignore` ne sont pas déplacés avec la discussion, sauf si Codex les copie dans un arbre de travail local géré à l’aide de `.worktreeinclude`.

## Détails avancés

### Arbres de travail gérés par Codex et arbres de travail permanents

Par défaut, les discussions utilisent un arbre de travail géré par Codex. Ces arbres sont conçus pour être légers et éphémères. Un arbre de travail géré par Codex est généralement consacré à une seule discussion, et Codex renvoie cette discussion vers le même arbre de travail si vous l’y retransférez ultérieurement.

Pour disposer d’un environnement durable, créez un arbre de travail permanent depuis le menu à trois points d’un projet dans la barre latérale. Cela crée un nouvel arbre de travail permanent qui constitue un projet distinct. Les arbres de travail permanents ne sont pas supprimés automatiquement et vous pouvez démarrer plusieurs discussions depuis le même arbre de travail.

### Comment Codex gère vos arbres de travail

Codex crée les arbres de travail dans `$CODEX_HOME/worktrees`. Le commit de départ correspond au commit `HEAD` de la branche sélectionnée au démarrage de votre discussion. Si vous avez choisi une branche comportant des modifications locales, Codex applique également les modifications non commitées à l’arbre de travail. L’arbre de travail n’est rattaché à aucune branche. Il se trouve dans un état de [HEAD détachée](https://git-scm.com/docs/git-checkout#_detached_head). Codex peut ainsi créer plusieurs arbres de travail sans encombrer vos branches.

### Copie des fichiers locaux ignorés dans les arbres de travail gérés

Les arbres de travail locaux gérés par Codex sont créés à partir d’une copie de travail Git ; les fichiers suivis sont donc déjà présents. Si votre dépôt ignore des fichiers de configuration locale nécessaires à un nouvel arbre de travail, ajoutez un fichier `.worktreeinclude` à la racine du dépôt et indiquez-y les chemins ignorés ou les motifs de type `.gitignore` à copier lorsque Codex crée un arbre de travail géré.

Utilisez cette méthode pour les fichiers intentionnellement ignorés par Git, tels que `.env`, `.env.local` ou `config/secrets.json`. Codex copie uniquement les fichiers ignorés qui correspondent aux règles de `.worktreeinclude` ; il ne copie pas les autres fichiers locaux non suivis par Git. Ne répertoriez pas les fichiers suivis.

Codex copie automatiquement un fichier `AGENTS.override.md` ignoré dans les arbres de travail locaux gérés ; vous n’avez donc pas besoin de le répertorier dans `.worktreeinclude`.

```text
# .worktreeinclude
.env
.env.local
config/secrets.json

Codex ignore les liens symboliques présents à la source et n’écrase pas les fichiers qui existent déjà dans la nouvelle copie de travail. Ce comportement s’applique aux arbres de travail locaux gérés par l’application de bureau ChatGPT, mais pas aux arbres de travail distants ni aux arbres de travail Git que vous créez vous-même depuis la ligne de commande.

### Limitations liées aux branches

Supposons que Codex ait terminé une tâche dans un arbre de travail et que vous choisissiez d’y créer une branche `feature/a` à l’aide de **Créer une branche ici**. Vous souhaitez maintenant la tester dans votre copie de travail locale. Si vous tentiez d’extraire cette branche, l’erreur suivante s’afficherait :

fatal: 'feature/a' is already used by worktree at '<WORKTREE_PATH>'

Pour résoudre ce problème, il faudrait extraire une autre branche à la place de `feature/a` dans l’arbre de travail.

Si vous prévoyez d’extraire la branche en local, utilisez la fonction Transfert pour déplacer la discussion vers Local plutôt que d’essayer d’extraire simultanément la même branche aux deux endroits.

Git empêche l’extraction simultanée de la même branche dans plusieurs arbres de travail, car une branche correspond à une référence mutable unique (`refs/heads/<name>`) qui représente « l’état actuellement extrait » d’un arbre de travail.

Lorsqu’une branche est extraite, Git considère que son HEAD appartient à cet arbre de travail et attend que les opérations comme les commits, les réinitialisations, les rebasages et les fusions fassent avancer cette référence de manière séquentielle et bien définie. Autoriser plusieurs arbres de travail à extraire simultanément la même branche créerait des ambiguïtés et des conditions de concurrence entre leurs opérations de mise à jour de la référence de cette branche, ce qui pourrait entraîner la perte de commits, des index incohérents ou une résolution incertaine des conflits.

En imposant la règle d’une seule branche par arbre de travail, Git garantit que chaque branche dispose d’une unique copie de travail faisant autorité, tout en permettant aux autres arbres de travail de référencer les mêmes commits en toute sécurité grâce à des HEAD détachés ou à des branches distinctes.

### Nettoyage des arbres de travail

Les arbres de travail peuvent occuper beaucoup d’espace disque. Chacun possède ses propres fichiers de dépôt, dépendances, caches de compilation, etc. L’application de bureau ChatGPT essaie donc de maintenir leur nombre dans une limite raisonnable.

Par défaut, Codex conserve vos 15 arbres de travail gérés par Codex les plus récents. Vous pouvez modifier cette limite ou désactiver la suppression automatique dans les paramètres si vous préférez gérer vous-même l’utilisation de l’espace disque.

Codex essaie de ne pas supprimer les arbres de travail encore importants. Les arbres de travail gérés par Codex ne sont pas supprimés automatiquement si :

- Une discussion épinglée y est associée
- La discussion est toujours en cours
- L’arbre de travail est permanent

Les arbres de travail gérés par Codex sont supprimés automatiquement lorsque :

- Vous archivez la discussion associée
- Codex doit supprimer d’anciens arbres de travail pour respecter la limite que vous avez configurée

Avant de supprimer un arbre de travail qu’il gère, Codex enregistre un instantané du travail effectué dans cet arbre. Si vous ouvrez une discussion après la suppression de son arbre de travail, vous verrez une option permettant de le restaurer.

## Questions fréquentes

  Oui. Codex crée par défaut les arbres de travail gérés dans `$CODEX_HOME/worktrees`.
  Pour choisir un autre emplacement, ouvrez **Paramètres \> Arbres de travail** , puis modifiez
**Racine de l’arbre de travail**.

<a id="can-i-move-a-chat-between-local-and-worktree"></a>

  Oui. Utilisez **Transférer** dans l’en-tête de la discussion pour la déplacer entre votre copie de travail
  locale et un arbre de travail. Codex effectue les opérations Git nécessaires pour déplacer la
  discussion en toute sécurité entre ces environnements. Si vous la retransférez ensuite vers un arbre de travail,
  Codex la replace dans l’arbre de travail auquel elle était associée.

<a id="what-happens-to-chats-if-a-worktree-is-deleted"></a>

  Les discussions peuvent rester dans votre historique même si le répertoire de l’arbre de travail correspondant est
supprimé. Pour les arbres de travail gérés par Codex, Codex enregistre un instantané avant de supprimer
l’arbre de travail et propose de le restaurer si vous rouvrez la discussion associée.
Les arbres de travail permanents ne sont pas supprimés automatiquement lorsque vous archivez les
discussions correspondantes.
