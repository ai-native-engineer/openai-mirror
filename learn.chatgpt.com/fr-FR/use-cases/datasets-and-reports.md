<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/datasets-and-reports -->

## Introduction

L’analyse de données sert avant tout à éclairer les décisions. Il ne s’agit pas d’analyser pour analyser, mais de produire un livrable qui aide quelqu’un à agir : un graphique pour la direction, les résultats d’une expérimentation pour une équipe produit, une évaluation de modèle pour des chercheurs ou un tableau de bord qui guide les opérations quotidiennes.

Un cadre utile, popularisé par _R for Data Science_, repose sur une boucle : importez et structurez les données, puis alternez transformation, visualisation et modélisation pour approfondir votre compréhension avant de communiquer les résultats.

ChatGPT Work s’intègre bien à ce workflow. Il vous aide à nettoyer les données, à explorer des hypothèses, à générer des analyses et à produire des livrables reproductibles. L’objectif n’est pas de créer un notebook ponctuel, mais une analyse que d’autres personnes peuvent examiner, juger fiable et réexécuter.

## Définissez votre cas d’usage

Choisissez une question concrète à laquelle vous souhaitez répondre à partir de vos données. Plus elle est précise, plus il est facile de déterminer les bonnes données d’entrée, les bons contrôles et le résultat adéquat.

### Exemple fil rouge : valeur des biens immobiliers à proximité de l’autoroute

À titre d’exemple, nous étudierons la question suivante :

> Dans quelle mesure les maisons proches de l’autoroute ont-elles une valeur immobilière plus faible ?

Supposons qu’un jeu de données contienne les valeurs immobilières ou les prix de vente, et qu’un autre contienne des informations sur la localisation, les parcelles ou la proximité de l’autoroute. Le travail ne consiste pas seulement à exécuter un modèle. Il faut aussi fiabiliser les données d’entrée, documenter les jointures, tester la robustesse du résultat et aboutir à un livrable utilisable par quelqu’un d’autre.

Vous pouvez joindre des fichiers CSV ou des classeurs Excel, indiquer une feuille de calcul Google Sheets approuvée avec `@google-drive`, ou utiliser l’application de bureau si vos données sont stockées sur votre ordinateur.

<div data-use-case-export-only>

### Exemple de résultat

Dans un échantillon fictif, ChatGPT associe 11 ventes immobilières au fichier des distances à l’autoroute et signale une vente sans distance correspondante. La valeur moyenne des maisons situées à moins d’un mile de l’autoroute est de **$500,000**, contre **$600,000** pour celles situées entre deux et cinq miles.

Après exclusion du bien éloigné le plus cher, l’écart reste de **$94,000**. Le rapport et le graphique précisent que l’échantillon est de petite taille, que la vente sans correspondance est exclue, que la comparaison n’établit aucun lien de causalité et qu’elle ne tient compte ni du quartier, ni de la date de vente, ni de la circulation, ni du bruit.

</div>

## Importez les données

Commencez par joindre les fichiers et demandez à ChatGPT de les examiner. Vous pourrez ainsi répondre à des questions élémentaires mais importantes :

- Quels formats de fichiers sont présents ?
- Que semble représenter chaque jeu de données ?
- Quelles colonnes pourraient correspondre à des cibles, des identifiants, des dates, des localisations ou des mesures ?
- Quels sont les problèmes de qualité manifestes ?

Ne demandez pas encore de conclusions. Commencez par demander un état des lieux et des explications.

## Nettoyez et fusionnez les données d’entrée

C’est généralement ici que commence le véritable travail. Vous disposez de deux jeux de données ou plus, la clé primaire n’est pas clairement identifiée et une fusion naïve pourrait entraîner une perte de données ou créer des doublons.

Avant d’effectuer la fusion, demandez à ChatGPT d’en établir le profil :

- Vérifiez l’unicité des clés candidates.
- Mesurez les taux de valeurs nulles et les différences de formatage.
- Normalisez les problèmes de formatage évidents, comme la casse, les espaces ou le format des adresses.
- Testez plusieurs jointures et indiquez leurs taux de correspondance.
- Avant qu’il ne crée le fichier fusionné final, demandez-lui de recommander la stratégie de fusion la plus sûre.

Si vous devez déterminer la meilleure clé, par exemple une adresse normalisée, un identifiant de parcelle construit à partir de plusieurs colonnes ou une jointure géographique, demandez à ChatGPT d’expliquer les compromis et les cas limites avant de valider la fusion.

## Explorez les données à l’aide de graphiques

Utilisez des graphiques pour comprendre les données avant de choisir un modèle. Dans l’exemple fil rouge, comparez les maisons proches de l’autoroute à celles qui en sont plus éloignées, étudiez les valeurs aberrantes, examinez la répartition des valeurs manquantes et vérifiez si l’effet apparent s’explique par la composition des quartiers, la surface des maisons ou un autre facteur.

Veillez à ce que chaque graphique reste lié à la question initiale. Enregistrez les comparaisons utiles afin qu’une autre personne puisse examiner l’analyse.

## Modélisez la problématique

Une analyse ne nécessite pas toujours un modèle complexe. Commencez par un modèle de référence interprétable.

Pour répondre à la question sur l’autoroute, une première approche raisonnable consiste à utiliser une régression ou un autre modèle transparent afin d’estimer la relation entre la proximité de l’autoroute et la valeur immobilière, tout en tenant compte de facteurs pertinents tels que la superficie, l’ancienneté et l’emplacement des logements.

Demandez à ChatGPT de préciser clairement les éléments suivants :

- La définition de la variable cible et des caractéristiques.
- Les variables de contrôle à inclure et les raisons de ce choix.
- Les risques de fuite de données et les exclusions.
- La manière dont il a choisi le partitionnement des données, la méthode d’évaluation ou l’estimation de l’incertitude.
- La signification du résultat, formulée en termes simples.

Si le premier modèle est peu performant, cela reste utile. Vous saurez ainsi si le problème vient du modèle, des caractéristiques, de la qualité de la jointure ou de la question elle-même.

## Présentez les résultats

L’analyse n’est utile que si quelqu’un d’autre peut l’exploiter. Demandez à ChatGPT de produire le livrable dont le public visé a besoin :

- Une note au format Markdown pour les collaborateurs techniques.
- Une feuille de calcul ou un fichier CSV pour les opérations en aval.
- Un document mis en forme ou un PDF pour les décideurs.
- Un notebook, un tableau de bord ou un rapport statique pour que l’analyse soit réutilisable.

Demandez-lui d’inclure les réserves nécessaires. Si la qualité de la jointure est imparfaite, s’il existe un biais d’échantillonnage ou si les hypothèses du modèle sont fragiles, le livrable doit le signaler clairement.

## Facultatif : configurez un environnement Python

Si le projet nécessite des scripts réutilisables ou un notebook, demandez à ChatGPT d’utiliser l’environnement Python existant ou d’en configurer un qui soit léger et reproductible. Conservez les fichiers sources en l’état et enregistrez séparément l’analyse, les graphiques et le rapport final. Vous n’avez pas besoin de configurer Python avant d’analyser des fichiers joints dans ChatGPT Work.

## Prompts suggérés

**Chargez les jeux de données et expliquez-les**

**Vérifiez la fusion avant de joindre les données**

**Construisez un premier modèle interprétable**

**Préparez les résultats pour les parties prenantes**
