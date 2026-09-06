<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/ai-app-evals -->

## Introduction

Lorsque vous développez une application d’IA ou modifiez une application existante, vous devez vous assurer qu’elle se comporte comme prévu. Les évaluations permettent de tester systématiquement un ensemble de scénarios et de détecter les régressions avant leur déploiement.

Vous pouvez utiliser Promptfoo pour exécuter des évaluations sur votre application d’IA et Codex pour vous aider à les créer et à les maintenir.

## Utilisation

Utilisez Codex avec la skill `$promptfoo-evals` du plugin Promptfoo pour transformer un comportement d’application d’IA en suite d’évaluation reproductible. Si l’application ne dispose pas encore d’une cible Promptfoo fonctionnelle, `$promptfoo-provider-setup` permet de relier la suite au parcours de l’application que vous souhaitez tester.

Codex peut examiner l’application, proposer des cas de test particulièrement pertinents, ajouter la configuration Promptfoo et les données de test, exécuter la suite en local et vous fournir une commande à réutiliser.

Ce cas d’usage est particulièrement adapté aux comportements concrets : qualité des réponses d’assistance, ancrage dans les données récupérées, étiquettes produites par un classificateur, appels d’outils, structure JSON, règles métier ou confiance dans les migrations de prompts et de modèles.

Une première version solide doit se composer de code et de données de test faciles à relire : un fichier `promptfooconfig.yaml` ou une configuration équivalente, un petit répertoire `evals/`, des cas de test, tout adaptateur cible nécessaire pour appeler l’application et une commande locale telle que `npm run evals`.

## Choisissez ce que vous souhaitez évaluer

Commencez par une seule promesse faite aux utilisateurs. Évitez de demander à Codex d’évaluer l’ensemble du système d’IA en une seule passe. Une suite plus restreinte inspire davantage confiance, se relit plus facilement et s’exécute plus aisément dans la durée.

Voici quelques bonnes cibles pour commencer :

- **Exactitude :** classification, extraction, résumé, routage ou transformation.
- **Ancrage :** réponses qui doivent rester ancrées dans les documents récupérés ou les sources citées.
- **Utilisation des outils :** choix de l’outil approprié, transmission d’arguments valides et gestion des erreurs renvoyées par les outils.
- **Format ou règles métier :** schémas JSON, noms de champs, limites définies par les règles métier ou contrats portant sur les textes affichés dans l’interface.
- **Migration de prompt ou de modèle :** vérification qu’un nouveau prompt, modèle, message système ou paramètre de récupération ne fait pas échouer des cas importants.

Partez des exigences produit, des rapports de bug, des signalements remontés par le support ou d’exemples débarrassés de toute donnée sensible que votre équipe accepte de versionner dans le dépôt.

## Demandez un plan d’évaluation

Codex doit examiner l’application avant de la modifier. Demandez-lui un plan qui précise le parcours cible, les fixtures, les assertions, l’adaptateur et les commandes. Vous pourrez ainsi repérer une mauvaise cible ou des cas de test peu pertinents avant l’ajout des fichiers.

Examinez le plan avant l’implémentation. Il doit préciser le parcours de l’application ou le point de terminaison que Promptfoo appellera, les cas initiaux, les assertions, les fichiers que Codex créera, la commande locale, ainsi que les éventuels secrets ou services nécessaires. Si le plan teste directement le modèle plutôt que le parcours de l’application emprunté par les utilisateurs, demandez à Codex si ce choix est intentionnel.

## Implémentez, exécutez, puis itérez

Lorsque le plan est correct, demandez à Codex de l’implémenter. La première implémentation doit rester simple : configuration, cas de test, fixtures, adaptateur cible si nécessaire, commande et preuve de l’exécution de cette commande.

Une petite suite qui s’appuie sur l’application pourrait se présenter ainsi :

```text
evals/
  promptfooconfig.yaml
  tests/
    cases.yaml
  providers/
    provider.js  # only if the built-in provider cannot call the app directly

Exécutez la suite avant de modifier le comportement. Cette exécution de référence vous indique si l’application échoue déjà sur certains cas, si les assertions doivent être ajustées ou si l’adaptateur cible est incorrect. Ajustez les assertions lorsqu’elles sont trop fragiles ou trop vagues, mais laissez visibles les véritables défaillances du produit.

Après la première exécution, utilisez la suite pour comparer les modifications apportées à l’application avant leur mise en production. Ajoutez de nouveaux cas chaque fois qu’un bug, une exigence de lancement ou une revue produit révèle un comportement que vous souhaitez maintenir stable. Lorsque la commande locale est stable, demandez à Codex de l’ajouter à la CI ou à votre liste de contrôle de mise en production.
