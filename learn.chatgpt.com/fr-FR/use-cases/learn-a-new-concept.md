<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/learn-a-new-concept -->

## Introduction

Comprendre un nouveau concept à partir d’un article de recherche dense ou d’un cours exige plus qu’un simple résumé. L’objectif est de construire un modèle mental opérationnel : quelle problématique il aborde, ce que fait réellement la méthode, quels éléments probants l’étayent, sur quelles hypothèses elle repose et quels aspects vous devez encore approfondir.

ChatGPT est utile dans ce contexte, car il peut automatiser la collecte d’informations contextuelles et transformer des concepts complexes en diagrammes ou illustrations utiles. Ce cas d’usage se prête aussi bien aux [sous-agents](/fr-FR/codex/agent-configuration/subagents) : un fil de travail peut analyser la structure de l’article, un autre rassembler les notions préalables, un troisième examiner les figures et la notation, tandis que le fil principal met les résultats en cohérence dans un rapport que vous pourrez relire ultérieurement.

Dans ce cas d’usage, le livrable final doit être facile à relire : un fichier Markdown tel que `notes/concept-report.md`, ou un document dans un autre format. Au lieu de se limiter à une réponse éphémère dans la discussion, il doit inclure une synthèse, un glossaire, une analyse pas à pas, des diagrammes, un tableau des éléments probants, les limites et les questions en suspens.

## Définissez l’objectif d’apprentissage

Commencez par préciser le concept et le livrable souhaité. Une question ciblée rend le rapport plus utile qu’une synthèse générale.

Par exemple :

> Je souhaite comprendre l’idée principale de cet article de recherche, le fonctionnement de la méthode, les raisons pour lesquelles les expériences étayent ou non l’affirmation, et ce que je devrais lire ensuite.

Ce périmètre confie à ChatGPT une tâche concrète. ChatGPT doit vous expliquer le concept, mais aussi rendre compte des incertitudes, citer l’origine des affirmations et distinguer les affirmations de l’article de sa propre interprétation.

## Exemple fil rouge : analyse d’un article de recherche

Supposons que vous souhaitiez étudier un article portant sur une architecture de modèle que vous ne connaissez pas. Vous voulez obtenir un rapport qui vous permette de comprendre le concept en un coup d’œil, sans avoir à lire l’intégralité de l’article.

Un bon résultat pourrait se présenter ainsi :

- `notes/paper-report.md` avec l’explication principale.
- `notes/figures/method-flow.mmd` ou un diagramme Mermaid intégré au Markdown pour expliquer la méthode.
- `notes/figures/concept-map.mmd` ou un petit fichier SVG montrant les relations entre les notions préalables.
- Un tableau des éléments probants qui associe chaque affirmation aux sections, pages, figures ou tableaux correspondants de l’article.
- Une liste de lectures complémentaires et de questions non résolues.

L’objectif est de systématiser le processus d’apprentissage et de produire un livrable durable.

## Répartissez le travail entre plusieurs sous-agents

Les sous-agents sont plus efficaces lorsque chacun se voit confier une tâche délimitée et un format de restitution clair. Demandez explicitement à ChatGPT de les lancer ; ChatGPT n’a pas besoin de recourir à des sous-agents pour chaque tâche de lecture, mais une exploration en parallèle est utile lorsque l’article est long ou complexe sur le plan conceptuel.

Pour un article de recherche, vous pouvez répartir le travail comme suit :

- **Cartographie de l’article :** Relevez la problématique, la contribution, la méthode, les expériences, les limites et les résultats annoncés.
- **Contexte préalable :** Expliquez les notions de base, les concepts connexes et les travaux antérieurs que l’article suppose connus.
- **Notation et figures :** Passez en revue les équations, les algorithmes, les diagrammes, les figures et les tableaux.
- **Relecteur critique :** Vérifiez si les éléments probants étayent les affirmations, dressez la liste des réserves et repérez les méthodes de référence manquantes ou les hypothèses peu claires.

L’agent principal doit attendre les réponses de ces sous-agents, les comparer et résoudre les contradictions. ChatGPT synthétisera ensuite les résultats dans un rapport cohérent.

## Complétez le contexte de manière ciblée

Lorsque l’article suppose des connaissances qui vous manquent, demandez à ChatGPT de réunir les informations contextuelles nécessaires à partir de sources approuvées. Il peut s’agir de notes locales, d’un dossier bibliographique, d’articles liés, de la Recherche web si elle est activée, ou d’une base de connaissances connectée.

Si vous étudiez un concept interne, vous pouvez relier plusieurs sources grâce aux [Plugins](/fr-FR/codex/plugins) pour créer une base de connaissances.

Délimitez clairement cette étape. Indiquez à ChatGPT quels critères définissent une source fiable et comment le rapport final doit intégrer le contexte externe :

- Définissez dans un glossaire les termes à connaître au préalable.
- Ajoutez une courte section « Notions à connaître au préalable ».
- Distinguez les liens vers les lectures complémentaires des affirmations propres à l’article.
- Signalez les affirmations provenant de sources extérieures à l’article.

## Générez des diagrammes pour le rapport

Les diagrammes sont souvent le moyen le plus rapide de vérifier que vous comprenez réellement un concept. Pour un rapport Markdown, demandez à ChatGPT de produire des diagrammes fidèles aux sources et faciles à modifier.

Voici de bons choix par défaut :

- Une carte conceptuelle présentant les notions préalables et leurs liens.
- Un diagramme de flux de la méthode retraçant les entrées, les transformations, les composants du modèle et les sorties.
- Une cartographie des expériences reliant les jeux de données, les métriques, les méthodes de référence et les affirmations présentées.
- Un diagramme des limites distinguant les hypothèses, les modes de défaillance et les questions en suspens.

Pour les rapports centrés sur Markdown, demandez un diagramme Mermaid si la destination le prend en charge, ou un petit fichier SVG/PNG ajouté au dépôt dans le cas contraire. Demandez à ChatGPT d’utiliser le skill système imagegen, inclus par défaut dans ChatGPT, uniquement si vous avez besoin d’un visuel d’illustration sans exigence d’exactitude, ou d’un élément qui se prête mal à un diagramme directement intégré au Markdown.

## Rédigez le rapport Markdown

Demandez à ChatGPT de rendre le rapport suffisamment autonome pour que vous puissiez y revenir plus tard. Voici une structure utile :

1. Synthèse.
2. À savoir avant la lecture.
3. Termes clés et notations.
4. Lecture guidée de l’article.
5. Schéma de la méthode.
6. Tableau des éléments de preuve.
7. Ce que l’article ne démontre pas.
8. Questions ouvertes et lectures complémentaires.

Le rapport doit inclure des références aux sources dans la mesure du possible. Pour un PDF, demandez des références aux pages, sections, figures ou tableaux. Si ChatGPT ne peut pas extraire les numéros de page exacts, il doit le signaler et fournir plutôt des références aux sections ou aux titres.

## Utilisez le rapport comme support d’un cycle d’étude

Le premier rapport n’est qu’un point de départ. Après l’avoir lu, posez des questions complémentaires et demandez à ChatGPT de réviser le document.

Voici quelques questions complémentaires utiles :

- Quelle partie de cette méthode dois-je comprendre en premier ?
- Quel est l’exemple jouet le plus simple qui illustre l’idée centrale ?
- Quelle figure joue le rôle le plus important dans l’argumentation de l’article ?
- Quelle affirmation est la plus fragile ou la moins bien étayée ?
- Que dois-je lire ensuite pour mettre cette méthode en œuvre ?

Lorsque le concept nécessite une expérimentation, demandez à ChatGPT d’ajouter un petit notebook ou script qui en reproduit une version simplifiée. Ajoutez dans le rapport Markdown un lien vers ce travail exploratoire afin de conserver ensemble l’explication et l’expérience.

Exemple de prompt :

## Skills à envisager

N’utilisez des Skills que s’ils correspondent au livrable souhaité :

- `$jupyter-notebook` pour les exemples jouets, les graphiques ou les reproductions légères, lorsque le résultat doit être exécutable.
- `$imagegen` pour les ressources visuelles à visée illustrative qui n’ont pas besoin d’être des schémas techniques exacts.
- `$slides` lorsque vous souhaitez transformer le rapport en présentation une fois la phase d’apprentissage terminée.

Pour la plupart des rapports d’analyse d’articles, les diagrammes intégrés à Markdown ou de simples fichiers SVG sont préférables par défaut à une image bitmap générée. Ils facilitent la comparaison des versions, la révision et la mise à jour à mesure que votre compréhension évolue.

## Suggestions de prompts

**Créez d’abord le plan du rapport**

**Créez des diagrammes pour mieux comprendre le concept**

**Transformez le rapport en plan d’étude**
