<!-- source: https://learn.chatgpt.com/fr-FR/docs/long-running-work -->

Pour une tâche susceptible de nécessiter de nombreuses étapes, indiquez clairement à ChatGPT le résultat attendu, les contraintes
et les critères d’achèvement. Regroupez les tâches connexes dans la même discussion afin que
ChatGPT puisse s’appuyer sur le même contexte pour choisir l’étape suivante et déterminer quand
la tâche est terminée.

Dans l’application de bureau ChatGPT, saisissez `/goal` pour lancer le mode Objectif. La ligne de progression
vous permet de mettre l’objectif en pause, de le reprendre, de le modifier ou de l’effacer pendant que ChatGPT travaille.

Pour les tâches de longue durée hébergées dans la version web de ChatGPT, utilisez ChatGPT Work et indiquez directement dans votre
prompt le résultat attendu, les contraintes et les critères de révision.

Poursuivez dans la même discussion sur le web pour ajouter du contexte, modifier les contraintes ou
demander un point d’avancement. Utilisez des discussions distinctes lorsque des tâches indépendantes peuvent s’exécuter en
parallèle et évitez d’accorder à deux tâches un accès en écriture à la même source connectée.
Pour les tâches connexes, regroupez les discussions et les fichiers sources au sein d’un
[projet](/fr-FR/codex/projects).

Dans une session interactive de Codex CLI, saisissez `/goal` pour lancer le mode Objectif. Poursuivez
dans la même session pour guider la tâche ou demander un point d’avancement.

Dans la discussion de l’extension IDE, saisissez `/goal` pour lancer le mode Objectif dans l’espace de travail
ouvert. Poursuivez dans la même discussion pour guider la tâche pendant son exécution.

  
    
  

<a id="start-a-goal"></a>
<a id="define-what-done-means"></a>
<a id="steer-a-running-goal"></a>
<a id="run-goals-in-parallel"></a>
<a id="related-docs"></a>

## Lancer un objectif

Saisissez `/goal` dans l’application de bureau ChatGPT, Codex CLI ou l’extension IDE. Le
texte de l’objectif constitue à la fois le premier prompt et les critères d’achèvement de la
tâche.

Si le résultat attendu reste flou, commencez par `/plan`. Demandez à ChatGPT de vous interroger,
de cerner les contraintes et de transformer le résultat en objectif assorti de critères de réussite
mesurables. Lancez ensuite l’objectif ainsi précisé avec `/goal`.

## Définir les critères d’achèvement

Rédigez un objectif qui permet à ChatGPT de vérifier sa propre progression. Incluez les trois éléments suivants
lorsqu’ils sont pertinents :

| Élément de l’objectif     | Contenu à inclure                                                               |
| ---------------- | ----------------------------------------------------------------------------- |
| **Résultat attendu**      | Décrivez le résultat souhaité, pas seulement l’activité que ChatGPT doit effectuer.   |
| **Contraintes**  | Indiquez les outils requis, les limites à respecter, les exigences de compatibilité ou les approches à éviter. |
| **Vérification** | Ajoutez des tests, des mesures ou des critères de révision qui permettent de confirmer que la tâche est terminée.  |

Par exemple :

```text
Migrate this codebase from JavaScript to TypeScript. Preserve existing behavior,
compile in strict mode without explicit `any` types, and make the full test suite pass.

## Guider l’exécution d’un objectif

Dans l’application de bureau ChatGPT, la ligne de progression de l’objectif s’affiche au-dessus de la zone de saisie. Utilisez-la pour
mettre l’objectif en pause ou le reprendre, le modifier ou l’effacer. Vous pouvez également envoyer des messages de suivi
pendant l’exécution de l’objectif afin d’ajouter du contexte ou d’ajuster les contraintes.

Utilisez une discussion secondaire lorsque vous souhaitez obtenir un récapitulatif de l’avancement ou une explication sans
interrompre la discussion principale. Mettez l’objectif en pause si vous prévoyez de perdre
la connexion, puis reprenez-le lorsque vous souhaitez que ChatGPT poursuive.

<a id="steer-a-running-task"></a>

## Guider une tâche en cours

Poursuivez dans la même discussion pour ajouter du contexte, ajuster les contraintes ou demander
un récapitulatif de l’avancement. Ouvrez une discussion distincte lorsqu’une autre tâche peut s’exécuter
de manière indépendante.

## Guider l’exécution d’un objectif

Envoyez un message de suivi dans la même session interactive pour ajouter du contexte ou
ajuster les contraintes. Demandez un récapitulatif de l’avancement si vous souhaitez que Codex résume
la progression avant de poursuivre.

## Guider l’exécution d’un objectif

Poursuivez dans la même discussion de l’IDE pour ajouter du contexte, ajuster les contraintes ou demander un
récapitulatif de l’avancement. Maintenez l’espace de travail accessible pendant l’exécution de l’objectif.

Le lancement d’un objectif n’accorde pas à ChatGPT un accès plus étendu. ChatGPT conserve la même
[politique de bac à sable et d’approbation](/fr-FR/codex/sandboxing) et s’interrompt lorsqu’une
décision est requise. Avec les [révisions automatiques des demandes
d’approbation](/fr-FR/codex/sandboxing/auto-review), un réviseur distinct peut
évaluer les demandes admissibles sans étendre ces limites.

## Exécuter des objectifs en parallèle

Chaque discussion conserve son propre contexte, ses messages, ses résultats et son objectif. Utilisez plusieurs discussions
simultanément, mais évitez que deux discussions modifient les mêmes fichiers. Utilisez des
[arbres de travail](/fr-FR/codex/environments/git-worktrees) afin d’attribuer une copie de travail distincte à chaque discussion de programmation
parallèle.

Pour les tâches locales, activez **Empêcher la mise en veille pendant l’exécution** dans les paramètres afin que votre Mac
ne se mette pas en veille. Utilisez les [Compagnons](/fr-FR/codex/pets?surface=app) ou les [notifications
système](/fr-FR/codex/notifications?surface=app) pour savoir quand une discussion requiert votre intervention
ou est prête pour la révision.

## Documentation associée

- [Projets et discussions](/fr-FR/codex/projects)
- [Mode Objectif et conception de prompts](/fr-FR/codex/prompting#goal-mode)
- [Arbres de travail Git](/fr-FR/codex/environments/git-worktrees)

## Documentation associée

- [Projets et discussions](/fr-FR/codex/projects)
- [Tâches planifiées](/fr-FR/codex/automations)
- [Bac à sable et autorisations](/fr-FR/codex/sandboxing)
