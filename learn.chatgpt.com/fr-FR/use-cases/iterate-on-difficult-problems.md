<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/iterate-on-difficult-problems -->

## Introduction

Certaines tâches se vérifient facilement en une seule étape : le build réussit, les tests passent et c’est terminé. Mais certains problèmes d’optimisation sont difficiles à résoudre et nécessitent de nombreuses itérations dans le cadre d’une boucle d’évaluation rigoureuse. Pour déterminer la marche à suivre, Codex doit examiner la sortie actuelle, lui attribuer un score, décider de la prochaine modification, puis répéter le processus jusqu’à obtenir un résultat réellement satisfaisant.

Ce type de cas d’usage se prête bien à une interface utilisateur personnalisée permettant de suivre visuellement la progression : Codex y consigne les sorties et les artefacts générés à chaque itération.
Vous pouvez observer Codex poursuivre son travail dans l’application tandis que l’artefact cible, la sortie du modèle ou la ressource générée continue de s’améliorer.
L’essentiel est de fournir à Codex les scripts nécessaires pour générer les métriques d’évaluation et les artefacts à examiner.

## Commencez par les évaluations

Avant le début de la tâche, définissez comment mesurer sa réussite. La meilleure configuration associe généralement :

- **Vérifications déterministes :** éléments que les scripts peuvent noter directement, comme les violations de contraintes ou les métriques déterministes calculées par le code
- **Vérifications par un LLM utilisé comme juge :** scores fondés sur une grille pour des qualités plus difficiles à formaliser précisément, comme la ressemblance, la lisibilité, l’utilité ou la qualité globale ; ces vérifications peuvent s’appuyer sur du texte ou des images en sortie

Si la dimension subjective compte, fournissez à Codex un script capable d’appeler un modèle, par exemple via la [Responses API](/api/reference/resources/responses/methods/create), puis de renvoyer des scores structurés. L’objectif n’est pas de remplacer les vérifications déterministes, mais de les compléter par un juge cohérent pour la partie que des humains évalueraient autrement à l’œil.

La boucle fonctionne au mieux lorsque la sortie de l’évaluation est exploitable par une machine, enregistrée après chaque exécution et facile à comparer dans le temps.

  **Conseil** : demandez à Codex de générer le script d’évaluation pour vous en décrivant les
  vérifications que vous souhaitez exécuter.

## Définissez une règle d’arrêt pour Codex

Les tâches difficiles dévient souvent de leur objectif parce que le prompt demande de « continuer à améliorer » sans indiquer quand s’arrêter. Formulez explicitement la règle d’arrêt.

Voici une approche pratique :

1. Définissez une cible pour le score global.
2. Définissez une cible distincte pour la moyenne des scores du LLM utilisé comme juge.
3. Demandez à Codex de continuer jusqu’à ce que ces deux valeurs dépassent le seuil, et non une seule.

Par exemple, si l’objectif est d’obtenir un artefact de grande qualité, demandez à Codex de poursuivre jusqu’à ce que le score global et la moyenne des scores du LLM utilisé comme juge dépassent tous deux 90 %. Cela clarifie la tâche : Codex peut déterminer si le résultat reste en deçà de la cible, mesurer l’écart et savoir si la dernière modification a été bénéfique.

## Tenez à jour un journal de la boucle

Le traitement des tâches de longue durée est bien plus fiable lorsque Codex tient un journal de la boucle au lieu de s’appuyer uniquement sur le contexte de la discussion.

Ce journal doit consigner :

- les meilleurs scores actuels
- les modifications apportées lors de la dernière itération
- ce qui s’est amélioré ou dégradé d’après l’évaluation
- ce que Codex prévoit d’essayer ensuite

C’est particulièrement important lorsque la tâche dure longtemps. Le journal sert de point de référence lorsque la tâche reprend, ainsi que de trace d’auto-évaluation pour l’exécution en cours.

## Examinez l’artefact, pas seulement les journaux

Pour certaines tâches difficiles, le diff de code et les résultats des métriques ne suffisent pas. Codex doit examiner l’artefact qu’il a produit.

Si la sortie est visuelle, comme une image générée, une mise en page ou un état rendu, laissez Codex examiner directement cet artefact et comparer le résultat actuel au meilleur résultat précédent ou à la grille d’évaluation prévue, par exemple lorsque la sortie est enregistrée sur le disque sous forme d’image.

Cela renforce la boucle :

- le script d’évaluation indique le score
- l’artefact révèle ce que le score n’a pas pris en compte
- la modification suivante tient compte des deux

Cette combinaison est bien plus efficace que de modifier le code à l’aveugle entre les exécutions.

## Formalisez chaque itération

Demandez à Codex de toujours suivre la même boucle :

1. Exécutez les évaluations sur la version de référence actuelle.
2. À partir des scores et des artefacts, identifiez le principal mode de défaillance.
3. Apportez une seule modification ciblée pour corriger ce facteur limitant.
4. Relancez les évaluations.
5. Consignez les nouveaux scores et précisez si la modification a apporté une amélioration.
6. Poursuivez jusqu’à ce que les seuils soient atteints.

Cette rigueur est essentielle. Si chaque itération modifie trop d’éléments à la fois, Codex ne peut pas déterminer quelle idée a amélioré le score. Si Codex ne tient pas de journal, il devient difficile de se fier au processus et de reprendre la tâche.
