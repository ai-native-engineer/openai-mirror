<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/ios-swiftui-view-refactor -->

## Refactoriser un écran sans modifier son comportement

Ce cas d’usage s’applique lorsqu’un fichier SwiftUI a fini par contenir un écran gigantesque et que chaque petite modification paraît risquée. L’objectif n’est ni de repenser la fonctionnalité ni d’inventer une nouvelle architecture. Demandez à Codex de préserver le comportement et la mise en page, puis de découper l’écran en petites sous-vues dont le flux de données est explicite afin de faciliter la révision de la prochaine modification.

Utilisez le [plugin Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) pour ce type de nettoyage. Son skill de refactorisation de vues SwiftUI adopte des partis pris utiles : privilégier MV plutôt que MVVM, conserver la logique métier dans les services ou les modèles, commencer par utiliser l’état local des vues et les dépendances d’environnement, et ne garder un modèle de vue que si la fonctionnalité en a clairement besoin.

## Ce qu’il faut demander à Codex

Commencez par indiquer précisément le nom d’un fichier d’écran et demandez à Codex d’en préserver le comportement tout en améliorant sa structure. Voici les règles de refactorisation à inclure directement dans votre prompt :

- Réorganisez le fichier afin de pouvoir parcourir facilement, de haut en bas, les dépendances d’environnement, les propriétés stockées, les propriétés d’état calculées qui ne produisent pas de vue, `init`, `body`, les propriétés de vue auxiliaires et les méthodes auxiliaires.
- Extrayez les sections pertinentes dans des types `View` dédiés avec quelques entrées explicites, des propriétés `@Binding` et des callbacks.
- N’utilisez que rarement de petites propriétés auxiliaires calculées de type `some View`. Ne recréez pas un écran gigantesque sous la forme d’une longue liste de fragments de vue privés et calculés.
- Déplacez hors de `body` les actions de bouton non triviales et les effets de bord, et transférez la véritable logique métier vers des services ou des modèles.
- Conservez une arborescence stable pour la vue racine. Privilégiez des conditions ciblées dans les sections ou les modificateurs plutôt que des branches `if/else` de premier niveau qui remplacent l’intégralité de l’écran.
- Corrigez au passage la gestion du cycle de vie avec Observation. Pour les modèles racines `@Observable` sous iOS 17+, la vue propriétaire doit les stocker dans `@State` ; n’utilisez les anciens wrappers observables que si votre cible de déploiement l’exige.

## Demandez une boucle de validation légère

Une refactorisation qui préserve le comportement doit s’accompagner de vérifications. Demandez à Codex d’effectuer, après chaque extraction significative, la vérification la plus légère possible de l’écran au moyen d’une compilation, d’un aperçu, d’un test ou du simulateur, puis de résumer ce qui a changé dans la structure et ce qui est volontairement resté identique.

## Conseils pratiques

### Découpez d’abord, débattez ensuite de l’architecture

Si un écran est trop grand, demandez à Codex d’en extraire les vues de section avant d’introduire une nouvelle couche d’abstraction. Une arborescence de vues plus courte et plus explicite suffit souvent à ne plus ressentir le besoin d’ajouter un modèle de vue.

### Transmettez à chaque sous-vue l’interface la plus réduite possible

Privilégiez les valeurs déclarées avec `let`, les propriétés `@Binding` et les callbacks à responsabilité unique plutôt que de transmettre l’intégralité du modèle parent à chaque vue enfant. Vous pourrez ainsi prévisualiser plus facilement chaque section extraite, avec moins de risque de la recoupler accidentellement à l’ensemble de l’écran.

### Demandez à Codex de signaler les éléments volontairement inchangés

Pour sécuriser une refactorisation, il est utile que Codex indique explicitement ce qu’il n’a pas modifié : les règles métier, le comportement de la navigation, la persistance, la sémantique des données d’analyse et la mise en page visible par l’utilisateur. Cela accélère nettement la révision.
