<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/macos-telemetry-logs -->

## Ajoutez un Logger là où le débogage manque de clarté

Ce cas d’usage concerne les flux d’applications Mac pour lesquels « quelque chose s’est produit » est une indication trop vague pour déboguer uniquement à partir d’une revue de code. Demandez à Codex d’ajouter quelques événements de journalisation unifiée à forte valeur informative autour d’un comportement, de lancer l’application, de déclencher ce comportement et de vérifier dans Console ou avec `log stream` que les événements attendus ont bien été émis.

Utilisez le [plugin Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) pour cette boucle. Le skill de télémétrie macOS qu’il fournit est volontairement léger : utilisez le `Logger` d’Apple, choisissez une paire sous-système/catégorie claire, journalisez les étapes clés des actions et les transitions d’état, évitez les données sensibles et vérifiez l’événement après une compilation et une exécution locales, plutôt que de supposer que l’instrumentation est correctement intégrée.

## Pourquoi la télémétrie est utile pour l’ingénierie agentique

De bons journaux offrent à Codex une boucle de rétroaction reproductible après chaque patch. Au lieu de vous demander d’inspecter manuellement chaque fenêtre, action de menu ou transition de synchronisation, l’agent peut exécuter l’application, parcourir le flux, examiner les journaux filtrés et déterminer la prochaine modification à apporter au code à partir d’éléments concrets.

C’est particulièrement utile pour trois boucles agentiques :

- **Boucle de débogage autonome :** Codex instrumente un flux suspect, lance l’application, clique dans la barre latérale ou déclenche une commande, lit la séquence d’événements journalisés, corrige le chemin de mise à jour de l’état, puis réexécute le même flux jusqu’à ce que les journaux concordent avec le comportement de l’interface.
- **Boucle de collecte de session d’application :** Codex ajoute un événement pour chacun des cas suivants : lancement de l’application, ouverture d’une fenêtre, sélection dans la barre latérale, début d’une importation, fin d’une importation et échec d’une importation. Il exécute ensuite une session locale et résume la chronologie obtenue afin que les transitions manquantes ou dans le désordre deviennent évidentes.
- **Boucle de capture pilotée par l’utilisateur :** Codex lance l’application avec la journalisation activée, maintient actif un flux de journaux ciblé pendant que vous testez manuellement un parcours complexe, puis examine la session capturée et propose le prochain patch à partir de cette trace.

## Conservez une instrumentation légère et filtrable

Demandez à Codex de créer un logger pour chaque domaine fonctionnel, plutôt qu’une ligne de journal permanente pour chaque modification d’état. Des catégories fonctionnelles telles que `Windowing`, `Commands`, `MenuBar`, `Sidebar`, `Sync` ou `Import` facilitent considérablement le filtrage des journaux lors de la prochaine session de débogage.

```swift

private let logger = Logger(
  subsystem: Bundle.main.bundleIdentifier ?? "SampleApp",
  category: "Sidebar"
)

@MainActor
func selectItem(_ item: SidebarItem) {
  logger.info("Selected sidebar item: \(item.id, privacy: .public)")
  selection = item.id
}

Utilisez `info` pour consigner les événements concis liés aux actions et au cycle de vie qui doivent rester utiles dans la durée, et `debug` pour les détails plus verbeux sur l’état local, susceptibles d’être supprimés ou journalisés à un niveau inférieur avant la fin de la tâche. N’ajoutez de marqueurs d’intervalle que pour mesurer une durée, et non par défaut.

## Demandez à Codex de confirmer l’événement dans les journaux

L’intérêt ne réside pas uniquement dans l’ajout d’appels à `Logger`. Demandez à Codex d’exécuter l’application, de déclencher le flux instrumenté, puis de vous fournir le filtre Console exact ou le prédicat `log stream` utilisé, ainsi qu’une ou deux lignes de journal représentatives.

```bash
log stream --style compact --predicate 'subsystem == "com.example.app" && category == "Sidebar"'

Si un événement attendu n’apparaît pas, demandez à Codex de rapprocher le point de journalisation du chemin de contrôle suspecté, de réexécuter le même flux et de poursuivre les itérations jusqu’à ce que les journaux expliquent ce qui s’est passé. Si la tâche se transforme en analyse de plantage ou de trace d’appels, passez au workflow de débogage avec compilation/exécution du plugin et concentrez la télémétrie sur les étapes clés des actions.

## Enregistrez une trace de session pour une prochaine exécution de Codex

Pour les bugs qui nécessitent des sessions plus longues ou qui surviennent par intermittence, demandez à Codex d’enregistrer un flux de journaux ciblé dans un petit fichier de trace local, de résumer la chronologie et de laisser cet artefact dans l’espace de travail. Une exécution ultérieure de Codex pourra ainsi examiner les mêmes éléments sans avoir à reconstituer toute la session de mémoire. Le débogage en plusieurs passes devient plus simple lorsqu’une exécution de l’agent collecte une trace et qu’une autre compare le comportement avant et après un patch.

Cette méthode est également adaptée lorsque vous devez piloter une partie de la session. Demandez à Codex de lancer l’application dans une boucle de débogage facilitant la journalisation, de démarrer une capture filtrée, d’attendre pendant que vous reproduisez manuellement le problème, puis de lire le fichier de trace enregistré une fois que vous avez terminé.

## Conseils pratiques

### Instrumentez une fonctionnalité à la fois

Commencez par un seul flux lié à une barre latérale, une fenêtre, une commande ou une synchronisation, afin que la séquence de journaux reste facile à examiner. Une fois ce flux fiable, Codex peut appliquer le même modèle aux flux voisins.

### Intégrez la confidentialité au prompt

Demandez à Codex d’expliquer chaque identifiant journalisé et d’éviter d’écrire des secrets, des données personnelles ou du contenu brut dans les journaux unifiés. Un vocabulaire d’événements très restreint suffit généralement au débogage local.

### Incluez un exemple de sortie dans le résumé final

Des lignes de journal représentatives permettent de se fier à la modification bien plus facilement que la simple affirmation « la télémétrie a été ajoutée ». Demandez à Codex d’inclure le prédicat de filtrage et une courte chronologie des actions afin que la prochaine exécution de l’agent puisse réutiliser la même boucle de vérification.
