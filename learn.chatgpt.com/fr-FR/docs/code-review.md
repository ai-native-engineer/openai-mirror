<!-- source: https://learn.chatgpt.com/fr-FR/docs/code-review -->

Utilisez ChatGPT ou Codex pour examiner les modifications du code avant de les valider dans un commit ou de les pousser.

## Démarrez une révision

Dans ChatGPT Work, importez le code à faire réviser ou rendez-le accessible via
un [plugin](/fr-FR/codex/plugins) de code source installé. Dans votre prompt, indiquez la pull
request, la branche, le commit, les fichiers et les critères de révision.

### Révision dans l’application

Ouvrez le volet de révision pour comprendre les modifications, commenter des lignes précises,
et décider des modifications à indexer, à annuler, à valider dans un commit ou à pousser.

Pour demander à Codex de réviser les modifications, saisissez `/review` dans la zone de saisie. Choisissez
**Réviser par rapport à une branche de base** ou **Réviser les modifications non validées**. Codex présente
des constats classés par ordre de priorité sans modifier votre arbre de travail.

Le volet de révision nécessite un projet situé dans un dépôt Git. Si votre projet
n’est pas encore un dépôt Git, l’application vous invite à en créer un.

Saisissez `/review` pour ouvrir les préréglages de révision de la CLI. Codex lance un réviseur dédié
qui lit le diff sélectionné et présente des constats exploitables classés par ordre de priorité,
sans modifier votre arbre de travail.

Saisissez `/review` dans la zone de saisie de l’extension IDE. Choisissez **Réviser par rapport à une
branche de base** ou **Réviser les modifications non validées**. Codex présente des constats classés par ordre de priorité
sans modifier votre arbre de travail.

La commande `/review` n’apparaît que lorsque le projet ouvert se trouve dans un dépôt
Git.

## Choisissez la portée de la révision

Précisez dans votre prompt la pull request, la branche, le commit ou les fichiers à examiner. Pour
réviser des fichiers locaux qui ne sont pas accessibles via un plugin de code source installé,
importez-les dans la discussion.

### Modifications affichées

Le volet de révision reflète l’état de votre dépôt Git, et pas seulement ce que Codex
a modifié. Il inclut les modifications apportées par Codex, celles que vous avez effectuées et toutes
les autres modifications non validées du dépôt.

Par défaut, le volet de révision affiche les modifications **Non indexées** . Utilisez **Indexées** pour l’index
Git, **Commit** pour un commit sélectionné, **Branche** pour le diff par rapport à votre
branche de base, ou **Dernier tour** pour la dernière intervention de l’assistant.

### Révisez plusieurs dépôts

Lorsqu’un [projet local comprend plusieurs dossiers](/fr-FR/codex/projects#use-local-projects-for-folders-and-codebases)
associés à différents dépôts Git, le volet de révision peut afficher les modifications de chaque
dépôt. Ouvrez le sélecteur de dépôt dans l’en-tête du volet de révision pour examiner
un autre dépôt et voir les lignes ajoutées ou supprimées sans quitter le
volet de révision actuel.

Choisissez **Dernier tour** pour voir les dernières modifications de l’assistant dans l’ensemble des
dépôts associés. Le sélecteur de dépôt affiche **Tous les dépôts** pour cette vue. Les autres
portées de révision, telles que **Non indexées**, **Indexées** et **Branche**, s’appliquent au
dépôt sélectionné.

Choisissez l’une des portées suivantes pour `/review` :

- **Réviser par rapport à une branche de base** identifie la base de fusion et examine le diff de votre branche.
- **Réviser les modifications non validées** inclut les fichiers indexés, non indexés et non suivis.
- **Réviser un commit** examine l’ensemble exact des modifications d’un commit sélectionné.
- **Instructions de révision personnalisées** : la révision se concentre sur les critères que vous indiquez.

Choisissez l’une des portées suivantes pour `/review` :

- **Réviser par rapport à une branche de base** compare votre branche actuelle à une branche que vous sélectionnez.
- **Réviser les modifications non validées** examine les modifications de votre arbre de travail.

## Exploitez les résultats de la révision

Les constats de la révision apparaissent dans la discussion sur le Web. Demandez des preuves, sollicitez une
révision de suivi plus ciblée ou demandez à ChatGPT de préparer des fichiers corrigés.

### Résultats de la revue de code

Les constats de la révision apparaissent sous forme de commentaires en ligne dans le volet de révision.

Par défaut, les révisions s’exécutent dans la discussion en cours. Dans **Paramètres** \> **Général** \>
**Revue de code**, choisissez **Détachée** pour démarrer une discussion de révision distincte. Consultez
les [paramètres de développement](/codex/developer-settings?surface=app#app-code-review).

  
    
  

La révision apparaît comme une intervention dans la transcription. Définissez `review_model` dans
`config.toml` pour que les révisions utilisent un modèle différent de celui de la
session actuelle.

Par défaut, la révision s’exécute dans la discussion en cours. Attribuez à `chatgpt.reviewDelivery` la valeur
`detached` si vous souhaitez que `/review` démarre une discussion de révision distincte. Consultez la
[référence des paramètres de l’extension IDE](/codex/developer-settings?surface=ide#ide-editor-settings-reference).

Si vous demandez à ChatGPT de préparer des fichiers corrigés, les outils et les autorisations de l’espace de travail
accessibles dans la discussion continuent de s’appliquer.

Si vous demandez à Codex d’appliquer les correctifs qu’il trouve, vos [paramètres du bac à sable et
d’approbation](/fr-FR/codex/sandboxing) habituels s’appliquent.

## Navigation dans le volet de révision

- Lorsque vous cliquez sur le nom d’un fichier, celui-ci s’ouvre généralement dans l’éditeur de votre choix. Vous
  pouvez choisir l’éditeur par défaut dans les [paramètres de développement](/codex/developer-settings?surface=app#app-project-and-terminal-behavior).
- Lorsque vous cliquez sur l’arrière-plan du nom du fichier, le diff se développe ou se réduit.
- Lorsque vous cliquez sur une ligne tout en maintenant la touche <kbd>Cmd</kbd> enfoncée, cette ligne s’ouvre dans l’éditeur de votre choix.
- Si une modification vous convient, vous pouvez [l’indexer ou annuler les modifications](#staging-and-reverting-files) dont vous ne voulez pas.

## Commentaires en ligne pour vos retours

Les commentaires en ligne permettent d’associer vos retours directement à des lignes précises du diff.
C’est souvent le moyen le plus rapide d’orienter Codex vers le bon correctif.

Pour laisser un commentaire en ligne :

1. Ouvrez le volet de révision.
2. Survolez la ligne que vous souhaitez commenter.
3. Sélectionnez le bouton **+** qui apparaît.
4. Rédigez votre commentaire et envoyez-le.
5. Une fois vos commentaires ajoutés, envoyez un message dans la discussion.

Comme les commentaires portent sur des lignes précises, Codex peut répondre plus précisément qu’avec
une instruction générale.

Codex considère les commentaires en ligne comme des consignes de révision. Après avoir ajouté vos commentaires, envoyez un
message de suivi qui indique clairement votre intention, par exemple : « Traitez les
commentaires en ligne et limitez les modifications au strict nécessaire. »

## Révisions de Pull requests

Lorsque Codex dispose d’un accès GitHub à votre dépôt et que le projet actuel se trouve sur
la branche de la pull request, l’application de bureau ChatGPT peut vous aider à traiter les retours
de la pull request sans quitter l’application. La barre latérale affiche le contexte de la pull request
et les retours des réviseurs, tandis que le volet de révision présente les commentaires à côté
du diff afin que vous puissiez demander à Codex de résoudre les problèmes dans la même discussion.

Installez GitHub CLI (`gh`) et authentifiez-la à l’aide de `gh auth login` afin que Codex
puisse charger le contexte de la pull request, les commentaires de révision et les fichiers modifiés. Si `gh` est
absent ou n’est pas authentifié, les détails de la pull request peuvent ne pas apparaître dans la barre latérale
ou dans le volet de révision.

Suivez cette procédure si vous souhaitez effectuer l’intégralité du cycle de correction au même endroit :

1. Ouvrez le volet de révision sur la branche de la pull request.
2. Examinez le contexte de la pull request, les commentaires et les fichiers modifiés.
3. Demandez à Codex de traiter les commentaires précis auxquels vous souhaitez donner suite.
4. Examinez le diff obtenu dans le volet de révision.
5. Lorsque vous êtes prêt, indexez les modifications, validez-les dans un commit, puis poussez-les vers la branche de la pull request.

Pour les révisions déclenchées par GitHub, consultez [Utiliser Codex dans GitHub](/fr-FR/codex/third-party/github).

## Indexation des fichiers et annulation des modifications

Le volet de revue comprend des actions Git qui vous permettent d’ajuster le diff avant de
créer un commit.

Vous pouvez ajouter des modifications à l’index, les en retirer ou les annuler à chacun des niveaux suivants :

- **Diff complet** : utilisez les boutons d’action de l’en-tête du volet de revue, tels que **Tout indexer** ou **Tout annuler**.
- **Par fichier** : ajoutez un fichier à l’index, retirez-le de l’index ou annulez ses modifications.
- **Par bloc de modifications** : ajoutez un bloc à l’index, retirez-le de l’index ou annulez ses modifications.

Ajoutez des modifications à l’index pour accepter une partie du travail, et annulez celles que vous souhaitez
abandonner.

### Modifications indexées et non indexées

Avec Git, un même fichier peut contenir à la fois des modifications indexées et non indexées. Lorsque cela
se produit, le volet peut afficher le même fichier dans les deux vues. C’est normal : Git
fonctionne ainsi.
