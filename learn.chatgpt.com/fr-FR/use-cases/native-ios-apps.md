<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/native-ios-apps -->

## Créez la structure de l’app et mettez en place la boucle de compilation

Pour un nouveau projet, commencez par formuler un prompt simple. Demandez à Codex de créer la structure d’une app iOS SwiftUI de départ et d’écrire un petit script de compilation et de lancement que vous pourrez associer à une action `Build` dans un [environnement local](/fr-FR/codex/environments/local-environment).

Maintenez une boucle axée sur la CLI. L’outil `xcodebuild` d’Apple peut répertorier les schémas et gérer depuis le terminal les opérations de compilation, de test et d’archivage ainsi que les actions `build-for-testing` et `test-without-building`. Codex peut ainsi rester dans une boucle agentique sans devoir basculer vers l’interface graphique de Xcode.

Si vous souhaitez une génération de projets plus propre et que les outils tiers ne vous posent pas problème, [Tuist](https://tuist.dev/) constitue une bonne étape suivante. Il peut générer et compiler des projets Xcode sans interface graphique, tout en permettant à Codex de compiler et de lancer l’app depuis le terminal.

Utilisez [XcodeBuildMCP](https://www.xcodebuildmcp.com/) lorsque vous travaillez dans un projet Xcode complet et avez besoin d’une automatisation plus poussée. À ce stade, les schémas, les cibles, le contrôle du simulateur, les captures d’écran, les journaux et les interactions avec l’interface deviennent suffisamment importants pour que de simples commandes shell ne suffisent plus à tout gérer.

## Tirez parti des Skills

Pour une première passe, vous n’avez souvent besoin ni d’un Skill ni d’un serveur MCP. Ajoutez des Skills lorsque la tâche devient plus spécialisée ou que vous souhaitez intégrer d’office des conventions SwiftUI plus rigoureuses à l’exécution.

- [SwiftUI expert](https://github.com/AvdLee/SwiftUI-Agent-Skill) est un Skill SwiftUI robuste et polyvalent qui intègre déjà de nombreuses bonnes pratiques.
- [SwiftUI Pro](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/main/swiftui-pro/SKILL.md) est un Skill complet d’audit SwiftUI portant sur les API modernes, la maintenabilité, l’accessibilité et les performances.

- [Liquid Glass expert](https://github.com/Dimillian/Skills/blob/main/swiftui-liquid-glass/SKILL.md) aide Codex à adopter les nouvelles API Liquid Glass d’iOS 26 et à ajuster les composants personnalisés pour les harmoniser avec le design le plus récent du système.
- [SwiftUI performance](https://github.com/Dimillian/Skills/blob/main/swiftui-performance-audit/SKILL.md) est utile lorsqu’une fonctionnalité semble lente ou que le chemin de mise à jour d’une vue SwiftUI paraît suspect. Il recherche les erreurs SwiftUI courantes et produit un rapport indiquant par ordre de priorité les corrections à apporter et les sources des gains les plus importants.
- [Swift concurrency expert](https://github.com/Dimillian/Skills/blob/main/swift-concurrency-expert/SKILL.md) est utile lorsque des erreurs obscures et des avertissements du compilateur font obstacle à la modification que vous souhaitez apporter. Vous en aurez peut-être moins souvent besoin avec GPT-5.6 Terra, mais il reste utile lorsque les diagnostics de concurrence Swift deviennent difficiles à démêler.
- [SwiftUI view refactor](https://github.com/Dimillian/Skills/blob/main/swiftui-view-refactor/SKILL.md) aide à réduire la taille des fichiers et à rendre le code SwiftUI plus cohérent dans tout le dépôt.
- [SwiftUI patterns](https://github.com/Dimillian/Skills/blob/main/swiftui-ui-patterns/SKILL.md) facilite l’adoption de modèles d’architecture prévisibles basés sur `@Observable` et `@Environment` à mesure que l’app évolue.

Pour en savoir plus sur l’installation et l’utilisation des Skills, consultez notre [documentation sur les Skills](/fr-FR/codex/build-skills).

## Itérez

Une fois la première version opérationnelle, ou si vous partez d’un projet existant, vous pouvez commencer à faire évoluer l’interface ou le comportement.

À ce stade, indiquez précisément ce que vous souhaitez modifier et comment.

Explicitez le contexte dans le prompt : indiquez à Codex s’il travaille dans un dépôt créé de zéro ou dans un projet Xcode existant, quels appareils iOS ou cibles de déploiement doivent continuer à fonctionner, et quelle boucle de validation vous attendez.

### Exemple de prompt

Par exemple, si vous souhaitez ajouter une fonctionnalité à une app existante, vous pouvez demander à Codex d’effectuer une modification comme celle-ci :

## Conseils pratiques

### Commencez par les bases

Pour un nouveau projet, commencez par formuler un prompt simple. Demandez à Codex de créer la structure d’une app SwiftUI de départ et d’écrire un petit script de compilation et de lancement que vous pourrez associer à une action `Build` dans un [environnement local](/fr-FR/codex/environments/local-environment). Pour cette première passe, vous n’avez souvent besoin ni d’un Skill ni d’un serveur MCP.

### Utilisez une boucle de validation courte et fiable

Après chaque modification, demandez à Codex d’exécuter la commande la plus ciblée qui valide réellement le contrat concerné. Passez ensuite à des compilations plus étendues. Codex reste ainsi rapide sans laisser croire qu’une compilation complète de l’app est nécessaire à chaque modification.

### Privilégiez la CLI pour le cycle de développement

Pour le cycle de développement, privilégiez la CLI. L’outil `xcodebuild` d’Apple peut répertorier les schémas et exécuter depuis le terminal les actions build, test, archive, `build-for-testing` et `test-without-building`. Codex peut ainsi rester dans un flux de travail agentique au lieu de devoir basculer vers l’interface graphique de Xcode.

### Tirez parti de XcodeBuildMCP

Utilisez XcodeBuildMCP dès que vous travaillez dans un projet Xcode complet et avez besoin d’une automatisation plus poussée. C’est alors que les schémas, les cibles, le pilotage du simulateur, les captures d’écran, les journaux et les interactions avec l’interface utilisateur prennent suffisamment d’importance pour que de simples commandes shell ne suffisent plus à elles seules.
