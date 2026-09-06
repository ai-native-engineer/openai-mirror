<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/code-migrations -->

## Introduction

Lorsque vous passez d’une stack à une autre, vous pouvez utiliser Codex pour cartographier et exécuter une migration maîtrisée : routage, modèles de données, configuration, authentification, tâches d’arrière-plan, outils de build, déploiement, tests, voire les conventions mêmes du langage et du framework.

Codex est particulièrement utile dans ce contexte : il peut dresser l’inventaire du système existant, faire correspondre les anciens concepts aux nouveaux et effectuer la transition par points de contrôle plutôt que de procéder à une réécriture massive. Cette approche est importante lorsque vous quittez un framework historique, portez le système vers un nouveau runtime ou remplacez progressivement une stack par une autre alors que le produit doit rester opérationnel.

## Utilisation

1. Commencez par recenser les éléments concernés par la migration : packages du système existant, conventions du framework, routage, accès aux données, authentification, configuration, outils de build, tests, hypothèses liées au déploiement et tout contrat externe qui doit rester valide après la migration.
2. Demandez à Codex d’établir la correspondance entre les concepts du système existant et la stack cible, et de signaler ceux qui n’ont pas d’équivalent direct.
3. Choisissez une stratégie progressive : couche de compatibilité, portage module par module, branch-by-abstraction ou remplacement selon le pattern de l’étrangleur, appliqué à une frontière à la fois.
4. Maintenez le comportement à l’identique jusqu’à ce que la migration elle-même impose un changement visible, et indiquez explicitement les exceptions.
5. Après chaque jalon, exécutez la validation minimale qui démontre la parité : lint, vérification des types, tests ciblés, tests de contrat, smoke tests ou comparaison côte à côte avec le parcours du système existant.
6. Après chaque point de contrôle, examinez le diff et les risques qui subsistent pour la transition au lieu d’attendre la fin de la réécriture complète.

## Utiliser les ExecPlans

Dans notre [guide pratique de modernisation du code](/cookbook/examples/codex/code_modernization), nous présentons les ExecPlans : des documents qui permettent à Codex de garder une vue d’ensemble des travaux de nettoyage, de décrire précisément l’état final visé et de consigner les validations effectuées après chaque passe.
Lorsque vous demandez à Codex de mener une migration complexe, demandez-lui de créer un ExecPlan pour chaque partie du système afin que chaque décision et chaque choix de stack technologique soient consignés et puissent être examinés ultérieurement.

## Combiner avec un objectif

Pour les phases de migration de longue durée, utilisez un [objectif](/fr-FR/codex/use-cases/follow-goals) pour guider Codex tout au long du processus. Définissez cet objectif en précisant clairement l’état final visé, les vérifications de parité, les modalités de retour arrière et la condition d’arrêt.
