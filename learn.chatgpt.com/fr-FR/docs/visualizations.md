<!-- source: https://learn.chatgpt.com/fr-FR/docs/visualizations -->

Les visualisations transforment les questions, les idées et les informations en graphiques, cartes,
diagrammes, calculateurs, simulations et explications interactives que vous pouvez explorer
dans une discussion ChatGPT. Utilisez-en une lorsque le fait d’ajuster les données d’entrée ou d’observer une
relation permet de mieux comprendre ou comparer une réponse, de s’exercer ou
de passer à l’action.

  La version préliminaire de Visualisations est en cours de déploiement. Sa disponibilité peut dépendre de votre
forfait, de votre plateforme, de votre compte et des paramètres de votre espace de travail.

La version préliminaire de Visualisations est en cours de déploiement dans l’application de bureau ChatGPT. Lorsque
**Visualiser** est disponible, saisissez `@` dans la zone de saisie, commencez à saisir
`Visualize`, puis sélectionnez **Visualiser** sous **Plugins**. La zone de saisie ajoute une
balise **Visualiser** avant votre demande.

Si **Visualiser** n’apparaît pas, utilisez ChatGPT sur le Web ou réessayez lorsque la
version préliminaire sera disponible pour votre compte.

Dans une discussion compatible de type Discussion ou ChatGPT Work, saisissez `@` dans la zone de saisie,
commencez à saisir `Visualize`, puis sélectionnez **Visualiser** sous **Plugins**. Sa
description est **Créez des visualisations et des outils interactifs**. La zone de saisie
ajoute une balise **Visualiser** avant votre demande.

Vous pouvez également saisir `@Visualize` et sélectionner la suggestion correspondante.

Codex CLI n’affiche pas les visualisations. Ouvrez le même contenu source dans
ChatGPT sur le Web ou dans l’application de bureau ChatGPT, puis ajoutez-y la balise `@Visualize`.

L’extension IDE de Codex n’affiche pas les visualisations. Utilisez ChatGPT sur le Web
ou dans l’application de bureau ChatGPT pour ce workflow.

## Vérifiez la disponibilité

| Interface                     | Disponibilité actuelle                                                          |
| --------------------------- | ----------------------------------------------------------------------------- |
| ChatGPT sur le Web          | Disponible pour les comptes compatibles dans Discussion et ChatGPT Work                      |
| Application de bureau ChatGPT         | Déploiement en cours en version préliminaire                                                        |
| Applications mobiles ChatGPT         | Déploiement en cours pour les comptes éligibles ; les commandes de la zone de saisie peuvent varier selon la version de l’application |
| Codex CLI et extension IDE | Le rendu des visualisations n’est pas pris en charge                                       |

La suggestion **Visualiser** indique de manière fiable que la version préliminaire est activée
pour votre compte. Pendant le déploiement, la disponibilité peut varier selon les comptes,
les espaces de travail et les versions de l’application, même pour un même forfait.

## Déterminez quand une visualisation est utile

ChatGPT peut choisir un format visuel lorsqu’il améliore sensiblement la réponse. Vous
pouvez également utiliser `@Visualize` si vous souhaitez expressément un résultat interactif.

Demandez le format le plus simple qui convient au besoin :

- Utilisez un diagramme pour représenter des relations accompagnées de libellés ou un processus.
- Utilisez un graphique ou un tracé pour représenter et comparer des données numériques clairement identifiées.
- Utilisez une carte pour les informations géographiques.
- Utilisez une visualisation interactive lorsque les données d’entrée, le temps, le mouvement ou les relations
spatiales doivent varier.
- Utilisez un [Site](/fr-FR/codex/sites) si vous avez besoin d’une application hébergée et pérenne, avec une
  URL partageable, des autorisations ou des données persistantes.

## Indiquez le résultat attendu et les éléments de contrôle dans le prompt

Une demande bien formulée précise le résultat attendu, le contenu source, la question et les interactions
utiles. Essayez cet exemple :

Indiquez à ChatGPT quelles informations utiliser, telles que le contenu déjà présent dans la
discussion, les données collées, un fichier joint ou une source connectée disponible.
Pour les demandes complexes, choisissez un niveau de raisonnement plus élevé lorsqu’il est disponible.

## Explorez des exemples interactifs

Ces exemples reproduisent trois visualisations de la page de lancement de GPT-5.6.
Utilisez leurs éléments de contrôle pour voir comment un prompt ciblé peut devenir une explication
interactive, un laboratoire ou un outil pédagogique.

  

## Affinez et poursuivez

Poursuivez dans la même discussion et décrivez la modification souhaitée. Voici quelques
relances utiles :

- Ajoutez ou supprimez un élément de contrôle, un filtre, une comparaison ou une annotation.
- Corrigez les données sources, les unités, les libellés ou les hypothèses.
- Simplifiez un résultat lent en agrégeant les données, en les regroupant en classes ou en les échantillonnant.
- Ajoutez un résumé textuel concis et un tableau de données.
- Rendez chaque élément de contrôle accessible au clavier et ajoutez des états de focus visibles.
- Utilisez des libellés ou des motifs en plus de la couleur, et supprimez les animations en boucle.
- Transformez le résultat en Site s’il doit être hébergé et consulté de nouveau.

Une relance peut créer une nouvelle visualisation au lieu de modifier le
résultat d’origine sur place. Vérifiez la nouvelle version avant de vous y fier.

## Partagez ou réutilisez un résultat

Utilisez l’action standard **Partager** de la discussion lorsqu’elle est disponible. Vérifiez
d’abord l’intégralité de la discussion partagée, y compris ses données sources et les
messages précédents. Une visualisation est généralement un instantané des informations disponibles
au moment où ChatGPT l’a créée, et non un tableau de bord en direct qui reste synchronisé avec une
source connectée.

Les options de téléchargement générées et les formats d’exportation peuvent varier selon le résultat. Si une exportation
ne fonctionne pas, demandez à ChatGPT les données sous-jacentes dans un format plus simple ou demandez-lui
de transformer la visualisation en Site.

## Améliorez l’accessibilité

Les visualisations générées cherchent à proposer des éléments de contrôle sémantiques, un focus visible, un contraste
suffisant et des animations limitées, mais le résultat peut varier. Vérifiez la visualisation
avant de la partager. Demandez à ChatGPT d’ajouter un résumé textuel et un tableau de données, de libeller les axes
et les unités, de ne pas s’appuyer uniquement sur la couleur et de rendre les éléments de contrôle utilisables au clavier.

## Résoudre un échec de génération

La génération des visualisations peut prendre une minute ou plus. Si le résultat est vide
ou absent, attendez la fin de la réponse, rechargez la discussion une fois, puis
réessayez. Si le problème persiste :

- Demandez une visualisation plus petite ou plus simple.
- Agrégez ou regroupez les données par classes, échantillonnez moins de points ou réduisez la précision d’un grand jeu de données.
- Supprimez un contrôle généré ou une bibliothèque générée qui ne fonctionne pas.
- Vérifiez les valeurs importantes, les limites géographiques et les hypothèses liées aux sources.
- Demandez plutôt un graphique, un diagramme, un tableau ou un Site.

Appliquez au traitement des données les mêmes règles de prudence que pour toute discussion ChatGPT. N’incluez
d’informations sensibles que si votre organisation l’autorise, et relisez
l’intégralité de la discussion avant de la partager.

## Documentation associée

- [Sites](/fr-FR/codex/sites)
- [Projets et discussions](/fr-FR/codex/projects)
- [Travailler avec des fichiers](/fr-FR/codex/artifacts-viewer)
- [Génération d’images](/fr-FR/codex/image-generation)
