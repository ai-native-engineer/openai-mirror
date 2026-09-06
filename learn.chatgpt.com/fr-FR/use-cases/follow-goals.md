<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/follow-goals -->

## Introduction

Utilisez `/goal` lorsque vous souhaitez que Codex poursuive un même objectif persistant au lieu de s’arrêter au terme d’un échange habituel. Cette commande est utile pour les tâches qui ont une cible claire, une boucle de validation et laissent à Codex une marge de manœuvre suffisante pour progresser sans vous demander d’intervenir à chaque étape. Avec `/goal`, Codex peut travailler de manière autonome pendant plusieurs heures sans intervention de votre part.

Définissez un objectif avec `/goal <objective>`, consultez l’objectif en cours avec `/goal`, puis utilisez `/goal pause`, `/goal resume` ou `/goal clear` lorsque vous devez contrôler l’exécution.

Si `/goal` ne figure pas dans la liste des commandes slash, activez `features.goals`
dans `config.toml` :

```toml
[features]
goals = true

Vous pouvez également exécuter `codex features enable goals` depuis la CLI ou demander à Codex de le faire.

## Choisissez les tâches adaptées

Un bon objectif dépasse le cadre d’un seul prompt, mais reste plus limité qu’un backlog sans périmètre défini. Il doit préciser ce que Codex doit accomplir, ce qu’il ne doit pas modifier, comment il doit valider sa progression et quand il doit s’arrêter.

Ce type d’objectif convient particulièrement aux cas suivants :

- une migration de code dont la pile cible, les vérifications de parité et les contraintes sont clairement définies
- des refactorisations d’envergure pour lesquelles Codex peut exécuter des tests après chaque point de contrôle
- des expériences, jeux ou prototypes où Codex peut continuer d’améliorer un livrable fonctionnel

Évitez d’utiliser un objectif pour une simple liste de tâches sans rapport entre elles.

## Mettez en place la boucle

1. Définissez un seul objectif et une seule condition d’arrêt.
2. Indiquez à Codex les fichiers, la documentation, le ticket, les journaux ou le plan qu’il doit consulter en premier.
3. Définissez les commandes ou les artefacts qui attestent de la progression.
4. Demandez à Codex de procéder par étapes et de tenir un bref journal d’avancement.
5. Utilisez `/goal` pour consulter l’état d’avancement pendant l’exécution.
6. Mettez l’objectif en pause, reprenez-le ou effacez-le lorsque l’exécution se termine, se bloque ou change de direction.

L’élément essentiel est le contrat. Avant de commencer, Codex doit savoir ce que signifie « terminé ». Si l’objectif est une migration, cela peut signifier que le nouveau chemin de code réussit les tests de contrat et qu’un retour arrière vers l’ancien reste possible. S’il s’agit d’un jeu ou d’un prototype, cela peut signifier que l’application se compile, se lance et correspond à la référence fournie en entrée ou au comportement attendu.

  Demandez de l’aide à Codex : commencez par échanger avec lui sur ce que vous souhaitez
créer, puis demandez-lui de définir directement un objectif et de commencer à travailler.

## Laissez Codex travailler de manière autonome

Pendant l’exécution d’un objectif, demandez des rapports de progression concis qui permettent de suivre l’exécution en toute confiance. Une mise à jour utile indique le point de contrôle en cours, ce qui a été vérifié, ce qu’il reste à faire et si Codex est bloqué.
Si l’état d’avancement manque de précision, précisez davantage l’objectif plutôt que d’ajouter des instructions ponctuelles. Indiquez précisément à Codex le prochain point de contrôle prioritaire, la commande qui permet de le valider et ce qui doit entraîner sa mise en pause.

Lorsqu’il poursuit un objectif, Codex peut travailler de manière autonome pendant de nombreuses heures sans que vous ayez à vérifier son avancement. Il s’arrête lorsqu’il est convaincu d’avoir atteint la condition d’arrêt ; considérez donc `/goal` comme une tâche en arrière-plan qu’il n’est pas nécessaire de surveiller.

## Exemples d’objectifs

### Migrations

Que vous migriez des jeux vers une nouvelle pile technologique, des applications mobiles vers une nouvelle plateforme ou une base de code vers un nouveau framework, vous pouvez utiliser `/goal` pour confier la migration à Codex :

### Création de prototypes

Que vous créiez de zéro une nouvelle application, un nouveau jeu ou une nouvelle fonctionnalité, vous pouvez utiliser `/goal` pour demander à Codex d’en réaliser une première version aboutie. Vous pouvez utiliser un fichier PLAN.md décrivant précisément ce que vous souhaitez créer pour guider la réalisation de cette première version.

### Optimisation des prompts

Si vous disposez d’une suite d’évaluations, vous pouvez utiliser `/goal` pour optimiser les prompts en fonction des résultats. Codex peut examiner les échecs, mettre à jour le prompt, relancer les évaluations et poursuivre les itérations jusqu’à ce que le score s’améliore ou que votre condition d’arrêt soit atteinte.
