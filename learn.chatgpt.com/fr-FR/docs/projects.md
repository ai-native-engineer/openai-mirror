<!-- source: https://learn.chatgpt.com/fr-FR/docs/projects -->

Utilisez un projet pour organiser les discussions associées et fournir à ChatGPT le contexte dont il a besoin.
La vue **Projets** de l’application de bureau ChatGPT comprend des projets ChatGPT et
des projets locaux associés à des dossiers sur votre ordinateur.

## Choisissez un projet ou démarrez sans projet

Créez un projet lorsque le travail doit se poursuivre dans le temps, produire plusieurs
résultats ou dépendre des mêmes fichiers et sources. Démarrez une discussion sans projet
lorsque le travail est autonome et ne nécessite pas le contexte partagé d’un projet.

Utilisez un projet pour regrouper les discussions, fichiers, instructions et sources associés.
Un même projet peut contenir des discussions démarrées avec Discussion ou ChatGPT Work.

## Choisissez un projet ou discutez sans projet

Créez un projet lorsque le travail doit se poursuivre dans le temps, produire plusieurs
résultats ou dépendre des mêmes fichiers et sources. Démarrez une discussion sans projet
lorsque le travail est autonome et ne nécessite pas le contexte partagé d’un projet.

Chaque projet comprend une section **Discussions** , qui répertorie ses discussions, et une section **Sources**
pour les fichiers importés et le contexte provenant de sources connectées. Les instructions du projet s’appliquent
à toutes ses discussions. Un projet ChatGPT ne donne pas directement accès à un dossier de
votre ordinateur : importez ou connectez donc les sources que ChatGPT doit utiliser.

Dans les deux cas, démarrez une nouvelle discussion depuis le projet pour utiliser ses fichiers et
ses instructions partagés, puis retrouvez-la dans **Discussions**.

Codex CLI considère le répertoire depuis lequel vous le lancez comme le projet de la discussion.
Exécutez `codex` depuis le répertoire dans lequel Codex doit travailler, ou utilisez
`--cd <directory>` (`-C`) pour le définir explicitement. La CLI ne donne pas accès à la
vue Projets de ChatGPT.

L’extension IDE considère le dossier ou l’espace de travail ouvert dans votre IDE comme le projet
local. Dans un espace de travail multiracine, sélectionnez la racine de l’espace de travail pour la discussion.
L’extension ne donne pas accès à la vue Projets de ChatGPT proposée sur le Web ou dans l’application de bureau.

<a id="work-in-a-project"></a>

## Travaillez dans un projet

La vue **Projets** réunit les projets ChatGPT et les projets locaux au même endroit.
Les projets ChatGPT rendent les fichiers et le contexte du projet accessibles dans les discussions associées. Un
projet local donne aux discussions accès à un ou plusieurs dossiers sur votre ordinateur, comme
un ensemble de fichiers source ou une base de code.

Démarrez une discussion distincte pour chaque résultat afin que ses messages et résultats restent
ciblés, tandis que le projet organise les travaux associés.

  
    
  

## Travaillez dans un projet

Un projet ChatGPT donne à ses discussions accès aux mêmes fichiers importés, aux instructions du
projet et aux sources connectées. Utilisez Discussion pour un échange rapide ou
ChatGPT Work pour un livrable plus conséquent ; les deux apparaissent comme des discussions dans la section
**Discussions** du projet. Démarrez une discussion distincte pour chaque résultat afin que ses
messages et résultats restent ciblés, tandis que le projet conserve le contexte partagé.

## Travaillez dans un répertoire de projet

Lancez Codex depuis le répertoire dont les fichiers doivent fournir le contexte de la discussion. Utilisez
`/new` pour démarrer une discussion distincte pour chaque résultat. Utilisez `/resume` lorsque
Codex est ouvert ou exécutez `codex resume` pour reprendre une discussion enregistrée.

La discussion conserve son historique et son répertoire de travail enregistré, tandis que Codex lit
les fichiers dans l’arbre de travail actuel. Conservez les consignes pérennes du projet dans
`AGENTS.md` ou dans la documentation versionnée afin qu’elles soient accessibles lors de futures discussions.

## Travaillez dans un espace de travail

Ouvrez le dossier ou l’espace de travail dont les fichiers doivent fournir le contexte de la discussion. Démarrez
une nouvelle discussion pour chaque résultat distinct, puis sélectionnez-la dans **Discussions récentes** pour
la reprendre. Les discussions d’un même projet peuvent utiliser les mêmes fichiers, mais chacune
conserve son propre historique.

La sélection actuelle et les fichiers ouverts fournissent le contexte de l’interaction en cours. Conservez
les consignes pérennes du projet dans `AGENTS.md` ou dans la documentation versionnée afin qu’elles
restent accessibles lors de futures discussions.

<a id="manage-project-threads"></a>
<a id="organize-projects-and-chats"></a>

<a id="organize-projects-and-tasks"></a>

## Organisez les projets et les discussions

Laissez les travaux en cours visibles et mettez de côté ceux qui sont terminés :

- **Épinglez un projet** pour qu’il reste en haut de la barre latérale. Vous pouvez également l’épingler
  depuis la vue Projets.
- **Épinglez une discussion** si vous y revenez souvent, même si des discussions plus récentes apparaissent dans le
  projet.
- **Renommez une discussion** avec un titre court qui décrit son résultat, par exemple « Note de lancement
  du T3 » ou « Revue de l’accessibilité du parcours de paiement ».
- **Recherchez des projets** depuis la vue Projets. Ouvrez **Rechercher des discussions** depuis la
  barre latérale pour retrouver une ancienne discussion lorsque vous vous souvenez d’une expression ou d’un nom de
  branche, mais pas de son titre. Cette fonction n’a pas de raccourci par défaut, mais vous pouvez en attribuer
  un dans **Paramètres \> Raccourcis clavier**.
- **Archivez une discussion** une fois le travail terminé. Dans le menu d’un projet, sélectionnez
**Archiver les discussions** pour archiver toutes ses discussions.

L’épinglage n’ajoute aucun contexte et ne modifie pas les éléments auxquels ChatGPT peut accéder. Il change uniquement
l’emplacement du projet ou de la discussion dans la barre latérale.

Restaurez les discussions archivées depuis **Paramètres \> Discussions archivées**.

<a id="organize-projects-and-tasks-1"></a>

## Organisez les projets et les discussions

Laissez les travaux en cours visibles et mettez de côté ceux qui sont terminés :

- **Épinglez un projet** pour qu’il reste en haut de la barre latérale. Vous pouvez également l’épingler
  depuis la vue Projets.
- **Épinglez une discussion** si vous y revenez souvent, même si des discussions plus récentes apparaissent dans le
  projet.
- **Renommez une discussion** avec un titre court qui décrit son résultat, par exemple « Note de lancement
  du T3 » ou « Revue de l’accessibilité du parcours de paiement ».
- **Recherchez des projets** depuis la vue Projets. Utilisez
<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>K</kbd> pour retrouver d’anciennes discussions lorsque vous vous souvenez d’une expression ou d’un
  nom de branche, mais pas du titre.
- **Archivez une discussion** une fois le travail terminé.

L’épinglage n’ajoute aucun contexte et ne modifie pas les éléments auxquels ChatGPT peut accéder. Il change uniquement
l’emplacement du projet ou de la discussion dans la barre latérale.

Restaurez les discussions archivées depuis **Paramètres \> Contrôles des données \> Discussions archivées**.

<a id="use-local-projects-for-folders-and-codebases"></a>

## Utilisez les projets locaux pour vos dossiers et votre code source

Ajoutez un projet local lorsque ChatGPT doit lire ou modifier des fichiers sur votre ordinateur.
Un projet n’a pas besoin de dossier, mais vous pouvez lui en associer selon vos besoins.

Pour ajouter ou changer des dossiers, ouvrez le menu du projet et sélectionnez **Modifier le projet**.
Sélectionnez **Ajouter un dossier** pour associer plusieurs dossiers. ChatGPT peut lire et modifier les fichiers
de chaque dossier associé. Pour changer le répertoire de travail par défaut,
survolez un dossier et sélectionnez **Définir comme principal**.

Les nouvelles discussions démarrent dans le dossier principal. Codex utilise également ce dossier
par défaut pour les opérations Git et la détection automatique de `AGENTS.md`, des skills et de
`config.toml`. Les dossiers secondaires restent disponibles pour rechercher, lire et
modifier des fichiers, mais Codex ne détecte pas automatiquement ces fichiers de projet dans
les dossiers secondaires.

Utilisez plusieurs dossiers lorsque des éléments liés se trouvent à différents endroits, par exemple une application et
sa documentation ou un site web et son backend. Créez des projets distincts pour
les travaux sans rapport ou lorsque chaque discussion ne doit accéder qu’à une partie d’un dépôt.
Le contexte de travail reste ainsi ciblé. Les projets distants ne prennent actuellement en charge qu’un seul
dossier.

Utilisez les [environnements locaux](/fr-FR/codex/environments/local-environment) pour définir les actions de configuration
et les commandes courantes d’un projet. Le [volet de
révision](/fr-FR/codex/code-review?surface=app) peut afficher les modifications apportées aux dépôts
associés au même projet. Les actions de pull request et
d’[arbre de travail](/fr-FR/codex/environments/git-worktrees) ciblent le dépôt
principal. Lorsque vous démarrez une discussion dans un arbre de travail, les autres dossiers restent
associés.

Les projets et les arbres de travail permettent d’organiser le travail, mais le [bac à sable](/fr-FR/codex/sandboxing)
contrôle ce que les commandes locales peuvent lire ou modifier, ainsi que leur accès au réseau.

<a id="start-without-a-project"></a>

<a id="start-a-task-without-a-project"></a>

## Démarrez une discussion sans projet

Sélectionnez **Nouvelle discussion** lorsque le travail est autonome et ne nécessite pas de fichiers
de projet partagés, d’instructions communes ni d’accès à des dossiers. Créez d’abord un projet lorsque
plusieurs discussions dépendent du même contexte.

<a id="start-a-task-without-a-project-1"></a>

## Démarrez une discussion sans projet

Démarrez une discussion depuis l’accueil de ChatGPT lorsqu’elle ne nécessite aucun fichier,
aucune instruction ni aucune source partagés au sein d’un projet. Vous pouvez utiliser Discussion ou ChatGPT Work ; sur le Web,
les deux permettent de créer des discussions.

Si le travail prend de l’ampleur, intégrez-le à un projet et donnez à chaque discussion un nom clair correspondant à son
résultat. Un projet peut contenir des discussions parallèles pour la recherche, la rédaction, la révision et le
suivi, sans mélanger tous les messages dans un même contexte.

<a id="start-a-chat"></a>
<a id="start-a-standalone-chat"></a>

<a id="use-quick-chat-for-a-quick-conversation"></a>

## Utilisez Chat rapide pour poser une question ponctuelle

Chat rapide ouvre une discussion ChatGPT classique. Les discussions ChatGPT n’apparaissent pas dans la
barre latérale de Codex, qui contient vos discussions et projets Codex.

Survolez **Nouvelle discussion**, puis sélectionnez l’icône **Chat rapide** à sa droite. Vous pouvez
également appuyer sur

<kbd>Cmd+Option+N</kbd> sur macOS ou <kbd>Ctrl+Alt+N</kbd> sur Windows et Linux.
Depuis **Nouvelle discussion**, vous pouvez ouvrir une discussion ChatGPT existante et l’ajouter à une discussion
Codex.

## Intégrez d’autres outils et du contexte

- Joignez des fichiers ou des [images en entrée](/fr-FR/codex/image-inputs) directement à une discussion
  lorsqu’ils ne concernent que cette requête.
- Installez des [plugins](/fr-FR/codex/plugins) pour intégrer du contexte et des actions provenant d’autres
  services.
- Configurez des serveurs [MCP](/fr-FR/codex/extend/mcp) lorsque votre organisation ou votre configuration de développement
  met des outils à disposition via Model Context Protocol.
- Utilisez les [mémoires](/fr-FR/codex/customization/memories), lorsqu’elles sont disponibles, pour réutiliser dans vos futures discussions
  le contexte utile issu de travaux antérieurs.

- Ajoutez des [images en entrée](/fr-FR/codex/image-inputs) à une discussion lorsque le contexte visuel concerne
  uniquement cette demande.
- Installez des [plugins](/fr-FR/codex/plugins) pour intégrer du contexte et des actions provenant d’autres
  services.
- Configurez des serveurs [MCP](/fr-FR/codex/extend/mcp) si votre organisation ou votre environnement de développement
  met des outils à disposition via le Model Context Protocol.
- Utilisez les [Mémoires](/fr-FR/codex/customization/memories), lorsqu’elles sont disponibles, pour réutiliser dans de futures discussions le contexte utile issu
  de travaux antérieurs.

- Référencez des fichiers ouverts ou sélectionnez du code dans l’éditeur pour fournir du contexte à
l’échange en cours.
- Configurez des serveurs [MCP](/fr-FR/codex/extend/mcp) si votre organisation ou votre environnement de développement
  met des outils à disposition via le Model Context Protocol.
- Utilisez les [Mémoires](/fr-FR/codex/customization/memories) de l’hôte Codex connecté, si elles sont
  disponibles, pour réutiliser du contexte utile dans de futures discussions.

- Ajoutez des fichiers et des sources connectées à la section **Sources** du projet s’ils
  doivent être disponibles dans toutes ses discussions.
- Joignez des fichiers ou des [images en entrée](/fr-FR/codex/image-inputs) directement à une discussion s’ils
  ne concernent que celle-ci.
- Dans ChatGPT Work, installez des [plugins](/fr-FR/codex/plugins) pour intégrer du contexte et
  des actions provenant d’autres services.
- Utilisez les [Mémoires](/fr-FR/codex/customization/memories), lorsqu’elles sont disponibles, pour réutiliser dans de futures discussions le contexte utile issu
  de travaux antérieurs.

## Étapes suivantes

- [Apprenez à rédiger et à affiner des prompts](/fr-FR/codex/prompting)
- [Apprenez à utiliser ChatGPT](/fr-FR/codex/use-chatgpt)
- [Poursuivez les tâches de longue durée](/fr-FR/codex/long-running-work)
