<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/ios-simulator-bug-debugging -->

## Confiez à Codex l’ensemble du cycle dans le simulateur

Ce cas d’usage est particulièrement efficace lorsque Codex prend en charge l’ensemble du cycle : choisir la bonne cible de l’application, lancer celle-ci dans le simulateur, inspecter l’écran actuel, exécuter les étapes de reproduction, recueillir les journaux et les captures d’écran, examiner une trace de pile si nécessaire, appliquer un correctif au code, puis reproduire le même parcours afin de vérifier que le bug a disparu.

Utilisez le [plugin Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) lorsque vous souhaitez que ce cycle reste agentique. Son flux de travail de débogage iOS repose sur XcodeBuildMCP, ce qui permet à Codex d’interagir avec un simulateur déjà démarré et de recueillir les mêmes éléments qu’une personne collecterait normalement à la main.

Lorsque XcodeBuildMCP est configuré avec des flux de travail pour l’automatisation du simulateur et de l’interface, le débogage et la journalisation, Codex peut prendre en charge tout le cycle de reproduction, débogage et vérification. Si Codex n’a pas encore choisi de projet, de schéma et de simulateur, demandez-lui de déterminer d’abord ces trois éléments, puis de réutiliser cette configuration pendant le reste de la session.

## Tirez parti des possibilités de XcodeBuildMCP

Dans la pratique, demandez à Codex d’utiliser les groupes de fonctionnalités suivants :

- Identification du projet et du simulateur : vérifiez si Codex connaît déjà la cible de l’application et le simulateur à utiliser, identifiez le projet ou l’espace de travail Xcode, recensez les schémas, trouvez ou démarrez un simulateur et conservez cette configuration pour les prochaines étapes de compilation et d’exécution.
- Contrôle de la compilation et du lancement : compilez la cible active de l’application, installez et lancez la version compilée dans le simulateur, relancez-la en capturant les journaux si nécessaire et déterminez l’identifiant du bundle de l’application si Codex doit inspecter ses journaux d’exécution spécifiques.
- Inspection de l’interface et interactions : lisez la hiérarchie d’accessibilité affichée à l’écran, prenez des captures d’écran, touchez les éléments de contrôle, saisissez du texte dans les champs, faites défiler les listes et effectuez des balayages depuis le bord ou d’autres gestes dans le simulateur.
- Journaux et état du débogueur : consultez en continu les journaux du simulateur, attachez LLDB à l’application en cours d’exécution, définissez des points d’arrêt, inspectez les frames de pile et les variables locales, puis exécutez des commandes du débogueur lorsqu’un plantage ou un blocage exige une analyse plus approfondie.

L’habitude essentielle consiste à demander à Codex d’inspecter l’arborescence des vues avant qu’il ne touche un élément. XcodeBuildMCP expose la hiérarchie d’accessibilité ainsi que les coordonnées, ce qui permet à Codex de privilégier des libellés stables ou des identifiants d’élément plutôt que de deviner des positions brutes à l’écran.

## Transformez un bug imprécis en script reproductible

Le skill de débogage iOS est particulièrement efficace lorsque votre prompt présente un bug précis et un résultat attendu, puis laisse Codex piloter l’application et recueillir des éléments de diagnostic de manière autonome. Si une authentification, un deep link ou une fixture de test est nécessaire, indiquez-le une seule fois et demandez à Codex de ne s’interrompre que lorsque cet élément manquant bloque sa progression.

## Conseils pratiques

### Demandez des preuves, pas seulement un correctif

Demandez le simulateur et le schéma exacts, ainsi que les captures d’écran, les extraits de journaux et les détails de la pile que Codex a utilisés pour expliquer le bug. Le patch final sera ainsi beaucoup plus facile à réviser qu’avec une simple affirmation comme « Je pense que cela devrait corriger le problème. »

### Privilégiez les libellés d’accessibilité aux coordonnées

Si Codex doit toucher un élément à partir de ses coordonnées parce qu’un contrôle ne possède aucun libellé stable ni identifiant d’accessibilité, demandez-lui de le signaler. Cela indique souvent que le correctif du bug devrait également apporter une petite amélioration à la testabilité de l’interface.

### Traitez un seul bug par exécution

Une boucle de débogage pilotée dans le simulateur est puissante, mais il est plus facile de lui faire confiance lorsque chaque prompt cible un seul mode de défaillance. Demandez à Codex de terminer un cycle de reproduction, correction et vérification avant d’étendre l’analyse aux problèmes connexes.
