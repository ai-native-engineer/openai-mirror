<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/discover-protein-folding-architectures -->

## Explorez une hypothèse d’architecture pour le repliement des protéines

Utilisez le mode Objectif de Codex quand une hypothèse sur le repliement des protéines exige plus
d’une passe d’implémentation. Fournissez à Codex une orientation scientifique bien délimitée, une
baseline fonctionnelle et un benchmark dont le score est calculé automatiquement. Codex peut implémenter
le fork d’architecture, suivre les expériences, diagnostiquer les échecs et poursuivre
les itérations pendant que vous examinez les éléments probants.

Cet exemple est parti d’une question précise : un modèle de type AlphaFold2 pourrait-il
apprendre plus efficacement les propriétés géométriques utiles des protéines si son tronc représentait non
seulement les résidus et les paires de résidus, mais aussi des objets topologiques explicites
d’ordre supérieur ?

## Définissez une expérience bien délimitée

AlphaFold2 utilise déjà un puissant raisonnement par paires et par triangles au sein de
l’Evoformer. Ses opérations triangulaires améliorent les représentations des arêtes, mais
réinjectent toujours leurs résultats dans un tenseur de paires. Le scientifique a proposé de tester si des représentations
apprises et persistantes des faces triangulaires et des cellules tétraédriques pouvaient
constituer un biais inductif utile avec peu de données.

Le dépôt public qui en résulte, [SimplexFold](https://github.com/ChrisHayduk/SimplexFold),
ajoute des états de faces parcimonieux `F_ijk` et des états tétraédriques `U_ijkl` en complément de la
représentation par paires classique `Z_ij`.

```text
MSA representation M
        <-> pair / edge tensor Z_ij
        <-> sparse face tensor F_ijk
        <-> sparse tetra tensor U_ijkl
        -> structure module
        -> recycled geometry
        loops back into the next pass

Commencez par le prompt de démarrage de cette page, une baseline minimale de type AlphaFold2,
et le benchmark public NanoFold. Ce benchmark fournit un support compact et soigneusement élaboré,
avec des données fixes et un score calculé automatiquement, pour mener des expériences de biologie
structurale. Veillez à ce que la première implémentation reste suffisamment réduite pour être testée avec
des tests unitaires ciblés et des microbenchmarks avant de lancer des entraînements
coûteux.

## Lancez la recherche avec le mode Objectif

1. Fournissez une hypothèse scientifique générale et réfutable, plutôt que de demander au modèle d’inventer de toutes pièces un programme de recherche complet.
2. Utilisez GPT-5.5 Pro dans ChatGPT pour transformer cette orientation en plan d’implémentation assorti de contraintes et d’ablations explicites.
3. Demandez à Codex d’implémenter une baseline [SimplexFold](https://github.com/ChrisHayduk/SimplexFold) exécutable aussi réduite que possible, puis vérifiez-la à l’aide de tests unitaires ciblés et de microbenchmarks.
4. Confiez le dépôt obtenu à Codex en mode Objectif et demandez-lui d’améliorer par ascension locale le score `lDDT-Cα` de validation sur le benchmark NanoFold, tout en conservant les journaux d’expériences, les plans et les références aux artefacts.
5. Laissez le mode Objectif s’exécuter en continu afin qu’il exploite les retours du benchmark pour faire évoluer l’architecture, le protocole d’entraînement et le harnais expérimental. Dans cet exemple, la boucle s’est exécutée pendant plus de 150 heures.

Utilisez `PLAN.md` pour consigner la stratégie actuelle et les prochaines étapes, `EXPERIMENTS.md` pour tenir un
journal structuré des résultats et `EXPERIMENT_NOTES.md` comme bloc-notes évolutif.
Ces artefacts permettent d’auditer une recherche de longue durée et vous offrent un espace stable
pour orienter l’itération suivante.

Le mode Objectif est utile ici, car la recherche exige des cycles répétés d’implémentation,
de test, de suivi des expériences, de diagnostic des échecs et d’itérations pilotées par le
benchmark. L’autorecherche non guidée dérivait souvent vers des modifications locales classiques,
comme les fonctions de perte, les optimiseurs et les hyperparamètres. Une hypothèse d’architecture concise fournie par le scientifique
a offert à Codex un espace de recherche plus pertinent, tout en lui laissant assez de latitude
pour tester, diagnostiquer et affiner l’implémentation.

Ce workflow est également utile aux équipes qui évaluent l’effet d’un pilotage avec un scientifique dans la boucle
sur la qualité de la recherche scientifique agentique.

## Exemple de résultat

Ce workflow a abouti à [SimplexFold](https://github.com/ChrisHayduk/SimplexFold),
une architecture expérimentale dotée d’états explicites de simplexes d’ordre supérieur. Examinez
conjointement la topologie et les journaux du benchmark pour vérifier que chaque itération continue
de tester l’idée scientifique initiale.

![Comparaison de la géométrie protéique en 1-, 2- et 3-simplexes.](/codex/use-cases/discover-protein-folding-architectures-simplex.webp)

L’enseignement à retenir n’est pas que Codex a résolu le repliement des protéines en toute autonomie.
Ce workflow montre que le mode Objectif peut servir de boucle persistante d’ingénierie
scientifique : un scientifique apporte l’idée conceptuelle, et Codex raccourcit le cycle
d’implémentation, d’expérimentation, de débogage et de recherche complémentaire.

Considérez les diagnostics prometteurs comme des indices que la voie d’implémentation fonctionne,
et non comme une preuve de généralisation. Examinez régulièrement la trajectoire de l’agent,
puis réorientez-le vers des questions d’architecture scientifiquement pertinentes si sa recherche
se réduit au réglage local des hyperparamètres. Ne formulez d’affirmations qu’après avoir effectué
des comparaisons appariées sur le jeu public de validation et des réplications appropriées.

## Ressources

- [Dépôt SimplexFold](https://github.com/ChrisHayduk/SimplexFold)
- [Plan du benchmark SimplexFold](https://github.com/ChrisHayduk/SimplexFold/blob/main/BENCHMARK_PLAN.md)
- [Concours NanoFold](https://github.com/ChrisHayduk/nanoFold-Competition)
- [Règles du concours NanoFold](https://github.com/ChrisHayduk/nanoFold-Competition/blob/main/docs/COMPETITION.md)
- [Exécution du mode Objectif pendant plus de 150 heures](https://x.com/ChrisHayduk/status/2055757345506877759?s=20)
- [Article sur le mode Objectif](https://x.com/ChrisHayduk/status/2053807198870880743?s=20)
