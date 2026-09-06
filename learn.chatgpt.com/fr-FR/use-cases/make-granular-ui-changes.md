<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/make-granular-ui-changes -->

## Introduction

Si vous disposez déjà d’une application et souhaitez itérer rapidement sur son interface, vous pouvez utiliser `gpt-5.3-codex-spark` pour y apporter de petites modifications ciblées.
Codex-Spark est notre modèle le plus rapide, optimisé pour itérer sur le code en temps réel et de manière quasi instantanée.

Cette approche fonctionne particulièrement bien en boucle courte : une remarque sur l’aspect visuel, une modification ciblée, une vérification dans le navigateur, puis la remarque suivante.

  Vous pouvez utiliser le [modèle Codex Spark](/fr-FR/codex/models) pour cette tâche. Il est
  disponible avec les offres Pro.

## Choisissez votre modèle

Pour itérer rapidement sur l’interface, commencez par `gpt-5.3-codex-spark` si vous y avez accès. Ses capacités sont inférieures à celles de nos modèles généralistes, mais il est conçu pour l’itération de code en temps réel. Si vous n’y avez pas accès, utilisez <code>{RECOMMENDED_MODEL_REFERENCES.latestMainlineModel.slug}</code> avec un effort de raisonnement `medium` ou `low`.

Ce compromis est utile pour les modifications ciblées de l’interface. Vous n’avez généralement pas besoin du modèle au raisonnement le plus poussé pour déplacer un bouton, régler un breakpoint ou ajuster l’état d’un composant. Il vous faut un modèle qui répond rapidement, comprend le code local, modifie le bon fichier et peut répéter cette boucle sans alourdir les itérations.

## Workflow de développement

1. Ouvrez l’application existante et affichez la route ou le composant concerné.
2. Détachez la discussion Codex en cours pour l’ouvrir dans une [fenêtre flottante](/codex/reference/settings#keep-a-chat-near-your-work), puis gardez-la à proximité de votre navigateur, de votre éditeur ou de l’aperçu du design pendant que vous travaillez.
3. Demandez à Codex d’effectuer une seule modification précise de l’interface à la fois. Fournissez la route, le viewport, la capture d’écran actuelle, la capture cible ou la remarque produit exacte si vous en disposez.
4. Demandez à Codex d’examiner l’implémentation actuelle, d’apporter la modification minimale raisonnable et de préserver les composants, tokens, primitives de mise en page et flux de données déjà en place dans l’application.
5. Examinez le résultat, puis envoyez le petit ajustement suivant dans la même discussion.

## Rédigez des prompts courts

Les prompts destinés à des modifications ciblées de l’interface doivent être directs et précis. Un bon prompt indique la zone de l’interface concernée, la modification visée et la validation attendue.

Si le résultat est presque satisfaisant, formulez un message de suivi tout aussi précis :

## Quand ralentir

Ne continuez pas à utiliser la boucle rapide si la tâche ne porte plus sur un ajustement ciblé. Passez à un modèle plus puissant et à un prompt plus soigneusement élaboré lorsque la modification nécessite une refactorisation à grande échelle, une nouvelle primitive du système de design, un comportement d’accessibilité complexe ou une décision produit qui affecte plusieurs écrans.

Les itérations rapides sur l’interface sont particulièrement efficaces lorsque Codex ajuste une partie de l’interface déjà bien comprise, plutôt que de refondre entièrement l’application.
