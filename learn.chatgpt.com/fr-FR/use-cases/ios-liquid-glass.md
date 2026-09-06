<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/ios-liquid-glass -->

## Prenez iOS 26 comme version de référence

Considérez d’abord l’adoption de Liquid Glass comme un projet de migration vers iOS 26 et Xcode 26. Recompilez l’application avec le SDK d’iOS 26, examinez ce que les contrôles SwiftUI standard fournissent automatiquement, puis demandez à Codex de repenser uniquement les parties personnalisées qui paraissent encore trop plates, trop lourdes ou trop déconnectées de l’interface du système.

Si l’application prend toujours en charge des versions antérieures d’iOS, explicitez cette contrainte dès le départ. Le Skill SwiftUI Liquid Glass du [plugin Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) doit utiliser `#available(iOS 26, *)` pour conditionner l’accès aux nouvelles API propres à Liquid Glass et conserver une solution de repli qui reste claire sur les appareils plus anciens.

## Tirez parti du plugin iOS

Utilisez le [plugin Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) lorsque vous voulez que Codex associe des modifications de l’interface SwiftUI à une validation dans le simulateur. Pour une migration vers Liquid Glass, demandez à Codex d’auditer un parcours, de migrer un petit ensemble de surfaces, de lancer le résultat dans un simulateur iOS 26 et de prendre des captures d’écran avant d’élargir le périmètre.

Ce plugin inclut un Skill SwiftUI Liquid Glass avec quelques choix par défaut utiles à reprendre dans votre prompt :

- Privilégiez les API natives `glassEffect` et `GlassEffectContainer`, les styles de boutons Liquid Glass et les transitions `glassEffectID`, plutôt que les vues de flou personnalisées.
- Appliquez `.glassEffect(...)` après les modificateurs de mise en page et d’apparence, afin que le matériau épouse la forme finale souhaitée.
- Regroupez les éléments Liquid Glass associés dans `GlassEffectContainer` lorsque plusieurs surfaces apparaissent ensemble.
- N’utilisez `.interactive()` que pour les boutons, les pastilles et les contrôles qui réagissent réellement au toucher.
- Harmonisez la forme des coins, les teintes et les espacements dans toute la fonctionnalité au lieu de multiplier les traitements Liquid Glass ponctuels.
- Conservez une solution de repli sans Liquid Glass pour les cibles de déploiement antérieures à iOS 26.

Pour en savoir plus sur l’installation des Plugins et des Skills, consultez notre documentation consacrée aux [Plugins](/fr-FR/codex/plugins) et aux [Skills](/fr-FR/codex/build-skills).

## Regardez les sessions de la WWDC

Ces sessions de la WWDC25 constituent un bon ensemble de références avant de demander à Codex de refactoriser un parcours réellement utilisé en production :

- [Découvrez Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/)
- [Familiarisez-vous avec le nouveau système de design](https://developer.apple.com/videos/play/wwdc2025/356/)
- [Créez une app SwiftUI avec le nouveau design](https://developer.apple.com/videos/play/wwdc2025/323/)
- [Créez une app UIKit avec le nouveau design](https://developer.apple.com/videos/play/wwdc2025/284/)
- [Nouveautés de SwiftUI](https://developer.apple.com/videos/play/wwdc2025/256/)

## Demandez d’abord un plan de migration, puis la migration d’une première partie

Les migrations vers Liquid Glass se déroulent mieux lorsque Codex sépare la question « Où Liquid Glass doit-il apparaître ? » de la consigne « Écrivez tout le code maintenant. » Demandez d’abord un audit rapide, puis laissez l’agent mettre en œuvre une partie autonome avec une validation dans le simulateur.

## Conseils pratiques

### N’appliquez pas Liquid Glass partout

Liquid Glass doit créer une couche de contrôles clairement distincte au-dessus du contenu, et non transformer chaque carte en panneau lumineux. Demandez à Codex de supprimer les arrière-plans décoratifs qui entrent en conflit avec les matériaux système, de conserver un contenu sans effet là où la lisibilité prime et de réserver les teintes à la mise en valeur sémantique ou aux actions principales.

### Commencez par un parcours très utilisé

Pour une première migration, mieux vaut généralement choisir la racine d’un onglet, un écran de détail, une feuille, une interface de recherche ou un parcours de prise en main plutôt que toute l’application. Cela simplifie la révision et permet d’identifier clairement quels choix relatifs à Liquid Glass doivent être déclinés en modèles de composants réutilisables.

### Vérifiez soigneusement le comportement de repli

Si votre cible de déploiement est antérieure à iOS 26, demandez à Codex d’afficher l’implémentation de repli à côté de l’implémentation Liquid Glass. Cette étape de révision permet de détecter toute régression involontaire dans la gestion de la disponibilité des API et d’éviter de livrer une migration qui ne fonctionne que dans le simulateur le plus récent.
