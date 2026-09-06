<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/native-macos-apps -->

## Générez l’ossature de l’app et la boucle de compilation

Pour une nouvelle app Mac, demandez d’abord à Codex de choisir le modèle de scène approprié : `WindowGroup`, `Window`, `Settings`, `MenuBarExtra` ou `DocumentGroup`. Cela permet à l’app de respecter les conventions des apps de bureau dès la première version, plutôt que d’évoluer à partir d’une `ContentView` conçue dans le style iOS.

Veillez à ce que la boucle d’exécution privilégie le shell. Pour les projets Xcode, utilisez `xcodebuild`. Pour les apps organisées autour de packages, utilisez `swift build` et un script d’encapsulation `script/build_and_run.sh` propre au projet, qui arrête l’ancien processus, compile l’app, lance le nouvel artefact et peut, si nécessaire, exposer les journaux ou la télémétrie.

Si une app SwiftPM pure est dotée d’une interface graphique, empaquetez-la et lancez-la sous forme de `.app` plutôt que d’exécuter directement le binaire brut. Vous éviterez ainsi, lors de la validation locale, les problèmes de présence dans le Dock, d’activation ou d’identité du bundle.

## Exploitez les Skills

Ajoutez le [plugin Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) dès que le travail devient plus spécifique aux apps de bureau. Il couvre les boucles de compilation et de débogage qui privilégient le shell, l’empaquetage d’apps SwiftPM, les modèles de scènes et de fenêtres SwiftUI conformes aux conventions Mac, l’interopérabilité avec AppKit, la journalisation unifiée, l’analyse des échecs de tests ainsi que les flux de travail de signature et de notarisation.

Pour en savoir plus sur l’installation et l’utilisation des Plugins et des Skills, consultez la [documentation sur les Plugins](/fr-FR/codex/plugins) et la [documentation sur les Skills](/fr-FR/codex/build-skills).

## Créez une interface native pour Mac

Préférez les conventions propres au Mac aux modèles de navigation d’iOS. Utilisez `NavigationSplitView` pour les interfaces avec barre latérale et panneau de détail, des scènes `Settings` explicites pour les préférences, des barres d’outils et des commandes pour rendre les actions faciles à trouver, ainsi que des éléments de la barre des menus pour les utilitaires légers toujours disponibles.

Utilisez d’abord les matériaux système, les couleurs sémantiques et les contrôles standard. N’ajoutez une apparence de fenêtre personnalisée, des zones de déplacement ou des surfaces Liquid Glass que si le produit a besoin d’une interface de bureau distinctive.

Si SwiftUI couvre presque votre besoin, ajoutez la plus petite passerelle AppKit possible. Les panneaux d’ouverture et d’enregistrement, le contrôle du premier répondant, la validation des menus, les cas limites du glisser-déposer et l’encapsulation d’un `NSView` pour un contrôle spécialisé s’y prêtent bien.

## Déboguez, testez et préparez la distribution

Pour observer le comportement à l’exécution, demandez à Codex d’ajouter quelques événements `Logger` liés à l’ouverture d’une fenêtre, à la sélection dans la barre latérale, à l’exécution de commandes de menu ou à la synchronisation en arrière-plan, puis de vérifier ces événements avec `log stream` après le lancement de l’app.

En cas d’échec de tests, demandez d’abord à Codex d’exécuter le plus petit périmètre de test utile avec `xcodebuild test` ou `swift test`, puis de déterminer si le problème relève de la compilation, de l’échec d’une assertion, d’un plantage, d’un test instable ou d’un problème d’environnement ou de configuration.

Lorsque vous passez des itérations locales à la distribution, demandez à Codex de préparer à la fois une procédure d’archivage manuel dans Xcode et une procédure par scripts pour l’archivage et la notarisation, afin de rendre la distribution reproductible. Demandez-lui d’inspecter le bundle de l’app, ses droits d’accès et l’environnement d’exécution renforcé avec `codesign` et `plutil`, et d’utiliser [App Store Connect CLI](https://asccli.sh/) si vous souhaitez que les envois s’effectuent eux aussi dans le terminal.

## Exemple de prompt

## Conseils pratiques

### Définissez explicitement les scènes

Modélisez la fenêtre principale, la fenêtre de paramètres, les fenêtres utilitaires et les éléments supplémentaires de la barre des menus comme des racines de scène distinctes, au lieu de dissimuler toute l’app dans une seule vue gigantesque.

### Appuyez-vous davantage sur les éléments d’interface système

Avant de créer des barres latérales, des barres d’outils ou des matériaux personnalisés, vérifiez si les API SwiftUI standard pour les scènes et les fenêtres offrent déjà le comportement Mac recherché.

### Limitez l’intégration d’AppKit au strict nécessaire

Utilisez `NSViewRepresentable`, `NSViewControllerRepresentable` ou un utilitaire `NSWindow` ciblé pour ajouter une fonctionnalité manquante propre aux apps de bureau, mais conservez SwiftUI comme source de vérité pour la sélection et l’état de l’app.

### Validez la signature et la notarisation indépendamment de la réussite de la compilation locale

Un lancement local réussi ne prouve ni que l’app est signée ni qu’elle est prête pour la notarisation. Conservez un flux de travail d’archivage manuel dans Xcode pour les vérifications ponctuelles avant publication, ajoutez un flux de travail scripté d’archivage et de notarisation pour assurer une distribution reproductible, et effectuez des vérifications avec `codesign` et `plutil` lorsque la tâche porte sur la distribution plutôt que sur les seules itérations locales.
