<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/ios-app-intents -->

## Rendez visibles au système les éléments pertinents de votre app

Les App Intents sont l’un des moyens les plus directs de rendre une app iOS plus utile en dehors de sa propre interface. Au lieu de considérer votre app comme un environnement fermé, qui ne fonctionne qu’après son lancement et quelques interactions, utilisez Codex pour exposer les actions et les objets qui doivent être accessibles à Raccourcis, Siri, Spotlight, aux widgets, aux commandes et aux expériences système plus récentes pilotées par des assistants.

C’est utile dès aujourd’hui pour la découverte et l’automatisation, et cela prépare solidement votre app à un avenir davantage piloté par des assistants. Si votre app permet déjà de créer, d’ouvrir, de filtrer, d’acheminer ou de résumer un contenu utile, les App Intents offrent au système un moyen structuré de solliciter cette capacité.

## Commencez par les actions et les entités, pas par tous les écrans

Pour une première implémentation d’App Intents, la meilleure approche ne consiste généralement pas à « reproduire toute l’app ». Demandez à Codex d’identifier :

- les quelques actions qu’un utilisateur souhaiterait déclencher sans parcourir toute l’interface
- les objets de l’app que le système doit comprendre pour acheminer correctement ces actions
- les flux de travail qui doivent ouvrir l’app dans un état précis, par opposition à ceux qui doivent s’exécuter entièrement depuis une interface système

Les recommandations d’Apple sur App Intents constituent ici un bon cadre : définissez l’action, puis le périmètre d’entités nécessaire au système, avant de rendre ces actions détectables et réutilisables dans les différentes expériences système. Les références les plus utiles sont [Rendre les actions et le contenu détectables et largement disponibles](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-and-widely-available), [Créer votre premier intent d’app](https://developer.apple.com/documentation/appintents/creating-your-first-app-intent) et l’exemple d’expérience système [Adopter App Intents pour prendre en charge les expériences système](https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences).

## Raisonnez en termes d’interfaces système, pas seulement de raccourcis

Les possibilités ne se limitent pas à « ajouter un raccourci ». Un ensemble d’App Intents bien conçu peut rendre votre app utile à plusieurs endroits :

- Raccourcis, où les utilisateurs peuvent exécuter directement des actions ou les combiner dans des automatisations plus larges
- Siri, où l’app peut exposer des verbes pertinents et des liens profonds au lieu de simplement s’ouvrir sans destination précise
- Spotlight, où les entités d’app et les raccourcis d’app deviennent des points d’entrée système faciles à découvrir
- les widgets, les Activités en direct, les commandes et les autres interfaces utilisateur pilotées par des intents
- les expériences plus récentes destinées aux assistants, dans lesquelles le système comprend bien plus facilement des actions et des entités structurées que des parcours arbitraires dans l’interface

## Suivez un modèle d’architecture concret

Cette approche fonctionne généralement mieux lorsque l’app adopte une structure de ce type :

- une cible App Intents dédiée, plutôt que des types d’intent dispersés dans des fichiers de l’app sans rapport entre eux
- des entrées `AppShortcutsProvider` pour des actions utilisateur importantes, comme rédiger une publication ou ouvrir l’app sur un onglet précis
- de petits types `AppEntity` pour les éléments sur lesquels le système doit raisonner, comme les comptes, les listes et les filtres de fil d’actualité
- une gestion des intents qui redirige proprement vers la scène principale de l’app, de sorte qu’un intent invoqué puisse ouvrir le bon parcours de rédaction ou faire basculer l’app sur le bon onglet

C’est le modèle que je demanderais à Codex de suivre pour la plupart des apps : commencez par une petite couche d’actions exposée au système, limitez le périmètre des entités et mettez en place un transfert prévisible vers l’app à l’exécution lorsqu’un intent nécessite l’interface principale.

## Demandez à Codex de concevoir le premier ensemble d’intents à exposer

Le prompt le plus efficace décrit à Codex les objets fondamentaux de votre app et les principales actions utilisateur, puis lui demande de choisir le plus petit ensemble initial d’App Intents qui soit utile, plutôt que de tout exposer aveuglément.

## Conseils pratiques

### Exposez les verbes dont les utilisateurs ont réellement besoin hors de l’app

Pour commencer, les intents les plus adaptés sont généralement des actions comme rédiger, ouvrir, rechercher, filtrer, démarrer, continuer ou inspecter. Si une action n’est utile qu’après un long parcours de configuration dans l’app, elle n’a peut-être pas sa place dans la première implémentation d’App Intents.

### Définissez des entités plus restreintes que votre couche de modèles

Le système n’a généralement pas besoin de votre modèle de persistance complet. Demandez à Codex de définir le plus petit ensemble d’entités d’app qui fournisse néanmoins à Siri, Raccourcis et Spotlight suffisamment de contexte pour acheminer et afficher correctement l’action.

### Considérez cette approche comme une infrastructure pour les assistants, pas seulement comme une fonctionnalité de raccourcis

Même si votre première version n’apporte d’amélioration visible qu’à Shortcuts ou Siri, l’avantage le plus important est que votre application commence à exprimer ses fonctionnalités sous forme d’actions et d’entités structurées. Elle pourra ainsi s’intégrer plus facilement aux futurs points d’entrée du système et à ceux pilotés par l’IA qu’une application dont les fonctionnalités ne sont définies que par des interactions tactiles et des hiérarchies de vues.
