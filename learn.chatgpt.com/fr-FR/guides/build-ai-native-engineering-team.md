<!-- source: https://learn.chatgpt.com/fr-FR/guides/build-ai-native-engineering-team -->

## Introduction

Les modèles d’IA élargissent rapidement l’éventail des tâches qu’ils peuvent accomplir, avec des conséquences importantes pour l’ingénierie. Les systèmes de pointe sont désormais capables de maintenir un raisonnement pendant plusieurs heures : en août 2025, METR a constaté que les meilleurs modèles pouvaient effectuer **2 heures et 17 minutes** de travail continu avec environ **50 % de confiance** quant à l’exactitude de leur réponse.

Cette capacité progresse rapidement : la durée des tâches que les modèles peuvent accomplir double environ tous les sept mois. Il y a quelques années à peine, les modèles ne pouvaient mener qu’environ 30 secondes de raisonnement, juste assez pour de petites suggestions de code. Aujourd’hui, comme ils peuvent maintenir des chaînes de raisonnement plus longues, l’IA peut potentiellement intervenir dans l’ensemble du cycle de vie du développement logiciel : les agents de programmation peuvent contribuer efficacement à la planification, à la conception, au développement, aux tests, aux revues de code et au déploiement.

![][image1]Dans ce guide, nous présenterons des exemples concrets illustrant la contribution des agents d’IA au cycle de vie du développement logiciel, ainsi que des conseils pratiques sur les mesures que les responsables de l’ingénierie peuvent prendre dès aujourd’hui pour commencer à mettre en place des équipes et des processus conçus autour de l’IA.

## Programmation assistée par l’IA : de l’autocomplétion aux agents

Les outils de programmation assistée par l’IA ont largement dépassé leur rôle initial d’assistants d’autocomplétion. Les premiers outils exécutaient des tâches rapides, comme suggérer la ligne de code suivante ou compléter des squelettes de fonctions. À mesure que les capacités de raisonnement des modèles se sont renforcées, les développeurs ont commencé à interagir avec des agents dans les interfaces de discussion des IDE pour programmer en binôme et explorer le code.

Les agents de programmation actuels peuvent générer des fichiers entiers, créer l’ossature de nouveaux projets et transformer des maquettes en code. Ils peuvent raisonner sur des problèmes en plusieurs étapes, tels que le débogage ou la refactorisation, tandis que leur exécution migre désormais de la machine d’un développeur vers des environnements cloud multi-agents. Cette évolution transforme le travail des développeurs : ils passent moins de temps à générer du code avec l’agent dans l’IDE et davantage à lui déléguer des workflows entiers.

| Capacité                         | Ce qu’elle permet                                                                                                                                                        |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Contexte unifié entre les systèmes** | Un même modèle peut lire le code, la configuration et les données de télémétrie, ce qui lui permet de raisonner de manière cohérente à travers les différentes couches qui nécessitaient auparavant des outils distincts.                    |
| **Exécution structurée d’outils**      | Les modèles peuvent désormais appeler directement des compilateurs, des outils d’exécution de tests et des outils d’analyse, et ainsi produire des résultats vérifiables plutôt que des suggestions statiques.                                       |
| **Mémoire persistante du projet**      | Grâce aux longues fenêtres de contexte et à des techniques comme le compactage, les modèles peuvent suivre une fonctionnalité depuis sa proposition jusqu’à son déploiement, tout en mémorisant les choix de conception et les contraintes définis précédemment. |
| **Boucles d’évaluation**               | Les sorties des modèles peuvent être testées automatiquement par rapport à des critères de référence — tests unitaires, objectifs de latence ou guides de style — afin que les améliorations reposent sur une qualité mesurable.          |

Chez OpenAI, nous en avons fait directement l’expérience. Les cycles de développement se sont accélérés : des travaux qui demandaient auparavant des semaines sont désormais livrés en quelques jours. Les équipes passent plus facilement d’un domaine à l’autre, prennent plus vite en main les projets qu’elles ne connaissent pas et gagnent en agilité et en autonomie dans toute l’organisation. De nombreuses tâches courantes et chronophages — documenter le nouveau code, identifier les tests pertinents, gérer les dépendances et nettoyer les feature flags — sont maintenant entièrement déléguées à Codex.

Cependant, certains aspects de l’ingénierie restent inchangés. La responsabilité finale du code — en particulier pour les problèmes nouveaux ou ambigus — incombe toujours aux ingénieurs, et certains défis dépassent les capacités des modèles actuels. Mais grâce à des agents de programmation comme Codex, les ingénieurs peuvent désormais consacrer davantage de temps aux défis complexes et inédits, et se concentrer sur la conception, l’architecture et le raisonnement à l’échelle du système plutôt que sur le débogage ou les tâches d’implémentation répétitives.

Dans les sections suivantes, nous détaillons la façon dont les agents de programmation transforment chaque phase du SDLC et présentons les mesures concrètes que votre équipe peut prendre pour commencer à fonctionner comme une organisation d’ingénierie conçue autour de l’IA.

## 1. Planification

Les équipes de toute l’organisation comptent souvent sur les ingénieurs pour déterminer si une fonctionnalité est réalisable, combien de temps son développement prendra et quels systèmes ou quelles équipes seront impliqués. Bien que tout le monde puisse rédiger une spécification, l’élaboration d’un plan fiable nécessite généralement une connaissance approfondie du code source et plusieurs cycles d’échanges avec les équipes d’ingénierie pour cerner les besoins, clarifier les cas limites et s’accorder sur ce qui est techniquement réaliste.

### Comment les agents de programmation peuvent aider

Les agents de programmation basés sur l’IA fournissent immédiatement aux équipes des analyses fondées sur le code pendant la planification et le cadrage. Par exemple, les équipes peuvent créer des workflows qui relient ces agents à leurs systèmes de suivi des tickets afin de lire la spécification d’une fonctionnalité, de la confronter au code source, puis de signaler les ambiguïtés, de diviser le travail en sous-composants ou d’en estimer la difficulté.

Les agents de programmation peuvent également retracer instantanément les chemins d’exécution du code afin d’indiquer quels services interviennent dans une fonctionnalité, une tâche qui nécessitait auparavant des heures, voire des jours, d’exploration manuelle d’un vaste code source.

### Sur quoi les ingénieurs se concentrent désormais

Les équipes consacrent davantage de temps au travail de fond sur les fonctionnalités, car les agents font ressortir les informations contextuelles qui nécessitaient auparavant des réunions d’alignement sur le produit et de cadrage. Les principaux détails d’implémentation, dépendances et cas limites sont identifiés en amont, ce qui permet de décider plus vite avec moins de réunions.

| Délégation                                                                                                                                                                                                              | Révision                                                                                                                                                                                                                                       | Responsabilité                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Les agents d’IA peuvent effectuer une première analyse de la faisabilité et de l’architecture. Ils lisent une spécification, la mettent en regard du code source, identifient les dépendances et font ressortir les ambiguïtés ou les cas limites à clarifier. | Les équipes examinent les conclusions de l’agent pour en vérifier l’exactitude et l’exhaustivité, et s’assurer que les estimations tiennent compte des véritables contraintes techniques. L’attribution des story points, l’estimation de l’effort et l’identification des risques difficiles à déceler nécessitent toujours un jugement humain. | Les décisions stratégiques — comme la hiérarchisation des priorités, l’orientation à long terme, l’ordre des étapes et les compromis — restent sous contrôle humain. Les équipes peuvent demander à l’agent de proposer des options ou les étapes suivantes, mais la responsabilité finale de la planification et de l’orientation du produit incombe à l’organisation. |

### Checklist pour bien démarrer

- Identifiez les processus courants qui nécessitent d’aligner les fonctionnalités et le code source. Il s’agit souvent du cadrage des fonctionnalités et de la création de tickets.
- Commencez par mettre en place des workflows simples, par exemple pour étiqueter et dédupliquer les tickets ou les demandes de fonctionnalités.
- Envisagez des workflows plus avancés, comme l’ajout de sous-tâches à un ticket à partir de la description initiale d’une fonctionnalité. Vous pouvez aussi lancer l’exécution d’un agent lorsqu’un ticket atteint une étape donnée, afin de compléter sa description par des informations supplémentaires.

<br />

## 2. Conception

La phase de conception est souvent ralentie par la mise en place des fondations techniques. Les équipes passent beaucoup de temps à écrire le code standard, à intégrer des systèmes de design et à affiner des composants ou des parcours d’interface utilisateur. Les écarts entre les maquettes et l’implémentation peuvent entraîner des reprises et de longs cycles de retours. Par ailleurs, le peu de temps disponible pour explorer d’autres solutions ou s’adapter à l’évolution des besoins retarde la validation de la conception.

### Comment les agents de programmation peuvent aider

Les outils de programmation assistée par l’IA accélèrent considérablement le prototypage en générant du code standard, en créant la structure des projets et en appliquant instantanément les tokens de design ou les guides de style. Les ingénieurs peuvent décrire en langage naturel les fonctionnalités ou les agencements d’interface utilisateur souhaités et obtenir du code de prototype ou des squelettes de composants conformes aux conventions de l’équipe.

Ils peuvent convertir directement les maquettes en code, suggérer des améliorations d’accessibilité et même analyser le code source pour repérer les parcours utilisateur ou les cas limites. Il devient ainsi possible d’itérer sur plusieurs prototypes en quelques heures au lieu de plusieurs jours et de créer très tôt des prototypes haute fidélité. Les équipes disposent donc d’éléments plus clairs pour prendre leurs décisions et peuvent effectuer des tests auprès des clients bien plus tôt dans le processus.

### Sur quoi les ingénieurs se concentrent désormais

Une fois les tâches courantes de configuration et de transposition confiées aux agents, les équipes peuvent consacrer leur attention à des travaux à plus fort impact. Les ingénieurs se concentrent sur l’amélioration de la logique principale, la définition de patterns architecturaux évolutifs et le respect des normes de qualité et de fiabilité par les composants. Les designers peuvent consacrer davantage de temps à évaluer les parcours utilisateur et à explorer d’autres concepts. Le travail collaboratif ne porte plus sur les contraintes de mise en œuvre, mais sur l’amélioration de l’expérience offerte par le produit.

| Délégation                                                                                                                                                                             | Révision                                                                                                                                                                       | Responsabilité                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Les agents prennent en charge la première phase de l’implémentation : ils créent l’ossature des projets, génèrent du code standard, transforment les maquettes en composants et appliquent les tokens de design ou les guides de style. | L’équipe examine la sortie de l’agent pour s’assurer que les composants respectent les conventions de design, satisfont aux normes de qualité et d’accessibilité, et s’intègrent correctement aux systèmes existants. | L’équipe reste responsable du système de design global, des patterns UX, des décisions architecturales et de l’orientation finale de l’expérience utilisateur. |

### Checklist pour bien démarrer

- Utilisez un agent de programmation multimodal acceptant à la fois du texte et des images en entrée
- Intégrez des outils de design aux agents de programmation via MCP
- Exposez les bibliothèques de composants par programmation avec MCP, puis intégrez-les à votre modèle de programmation
- Créez des workflows qui établissent la correspondance suivante : maquettes → composants → implémentation des composants
- Utilisez des langages typés (par exemple, Typescript) pour définir les props et sous-composants valides pour l’agent
  <br />

## 3. Développement

C’est pendant la phase de développement que les équipes rencontrent le plus de difficultés et que l’impact des agents de programmation est le plus net. Les ingénieurs consacrent beaucoup de temps à transposer les spécifications en structures de code, à connecter les services, à reproduire les mêmes patterns dans le code source et à ajouter du code standard ; même de petites fonctionnalités peuvent exiger des heures de travail fastidieux.

À mesure que les systèmes se développent, ces difficultés s’accumulent. Les grands monorepos accumulent des patterns, des conventions et des particularités historiques qui ralentissent les contributeurs. Les ingénieurs peuvent passer autant de temps à redécouvrir la « bonne manière » de procéder qu’à implémenter la fonctionnalité elle-même. Les changements constants de contexte entre les spécifications, la recherche dans le code, les erreurs de build, les échecs de tests et la gestion des dépendances augmentent la charge cognitive. De plus, les interruptions pendant les tâches de longue durée brisent le rythme et retardent encore la livraison.

### Comment les agents de programmation peuvent aider

Les agents de programmation exécutés dans l’IDE et la CLI accélèrent la phase de développement en prenant en charge des tâches d’implémentation plus vastes et en plusieurs étapes. Au lieu de produire uniquement la fonction ou le fichier suivant, ils peuvent créer des fonctionnalités complètes de bout en bout — modèles de données, API, composants d’interface utilisateur, tests et documentation — en une seule exécution coordonnée. Grâce à leur capacité à poursuivre leur raisonnement à l’échelle de l’ensemble du code source, ils prennent en charge des décisions qui exigeaient auparavant que les ingénieurs retracent manuellement les chemins d’exécution du code.

Pour les tâches de longue durée, les agents peuvent :

- Ébaucher l’implémentation complète de fonctionnalités à partir d’une spécification écrite.
- Rechercher et modifier du code dans des dizaines de fichiers tout en maintenant sa cohérence.
- Générer du code standard conforme aux conventions : gestion des erreurs, télémétrie, wrappers de sécurité ou conventions de style.
- Corriger les erreurs de build dès leur apparition au lieu d’attendre une intervention humaine.
- Écrire les tests en même temps que l’implémentation, au sein d’un même workflow.
- Produire des jeux de modifications directement exploitables sous forme de diff, conformes aux consignes internes et accompagnés de messages de PR.

En pratique, une grande partie des tâches mécaniques de développement passe ainsi des ingénieurs aux agents. L’agent effectue la première implémentation ; l’ingénieur en assure la revue et les modifications, et fixe la direction à suivre.

### Ce que font désormais les ingénieurs

Lorsque les agents peuvent exécuter de manière fiable des tâches de développement en plusieurs étapes, les ingénieurs se consacrent à des tâches nécessitant davantage de recul :

- Clarifier le comportement du produit, les cas limites et les spécifications avant l’implémentation.
- Examiner les implications architecturales du code généré par l’IA plutôt que d’effectuer des tâches de câblage répétitives.
- Affiner la logique métier et les chemins critiques pour les performances qui nécessitent une connaissance approfondie du domaine.
- Concevoir les patterns, les garde-fous et les conventions qui encadrent le code généré par les agents.
- Collaborer avec les responsables produit et les designers pour préciser l’objectif des fonctionnalités plutôt que de travailler sur le code standard.

Au lieu de « traduire » les spécifications d’une fonctionnalité en code, les ingénieurs se concentrent sur l’exactitude, la cohérence, la maintenabilité et la qualité à long terme, des aspects pour lesquels le contexte humain reste primordial.

| Délégation                                                                                                                                                                                                                                           | Révision                                                                                                                                                                                                                              | Responsabilité                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Les agents rédigent une première implémentation des fonctionnalités bien spécifiées : structure initiale, logique CRUD, câblage, refactorisations et tests. À mesure que leur capacité à raisonner sur de longues périodes s’améliore, ils prennent de plus en plus en charge des implémentations complètes de bout en bout plutôt que des extraits isolés. | Les ingénieurs évaluent les choix de conception, les performances, la sécurité, le risque lié aux migrations et l’adéquation avec le domaine, tout en corrigeant les problèmes subtils que l’agent peut ne pas détecter. Ils façonnent et affinent le code généré par l’IA au lieu d’effectuer les tâches mécaniques. | Les ingénieurs restent responsables des travaux qui nécessitent une compréhension approfondie du système : nouvelles abstractions, changements architecturaux transversaux, exigences produit ambiguës et compromis de maintenabilité à long terme. À mesure que les agents prennent en charge des tâches plus longues, le travail des ingénieurs passe d’une implémentation ligne par ligne à une supervision itérative. |

Exemple :

Les ingénieurs, responsables produit, designers et opérateurs de Cloudwalk utilisent Codex au quotidien pour transformer des spécifications en code fonctionnel, qu’il leur faille un script, une nouvelle règle antifraude ou un microservice complet livré en quelques minutes. Codex les décharge des tâches fastidieuses de la phase de développement et permet à chaque employé de concrétiser des idées à une vitesse remarquable.

### Liste de contrôle pour bien démarrer

- Commencez par des tâches définies avec précision
- Demandez à l’agent d’utiliser un outil de planification via MCP ou de créer un fichier PLAN.md et de le commiter dans le dépôt
- Vérifiez que les commandes que l’agent tente d’exécuter s’exécutent correctement
- Améliorez progressivement un fichier AGENTS.md afin de permettre des boucles agentiques, par exemple l’exécution de tests et de linters pour obtenir des retours
  <br />

## 4. Tests

Les développeurs ont souvent du mal à garantir une couverture de tests suffisante, car l’écriture et la maintenance de tests exhaustifs prennent du temps, imposent de changer de contexte et exigent une compréhension approfondie des cas limites. Les équipes doivent fréquemment arbitrer entre rapidité et exhaustivité des tests. À l’approche des échéances, la couverture de tests est souvent la première sacrifiée.

Même lorsque des tests existent, leur mise à jour au fil de l’évolution du code reste une source constante de difficultés. Ils peuvent devenir fragiles, échouer sans raison claire et nécessiter eux-mêmes d’importantes refactorisations lorsque le produit sous-jacent évolue. Des tests de qualité permettent aux équipes de livrer plus rapidement et avec davantage de confiance.

### Comment les agents de programmation peuvent aider

Les outils de programmation basés sur l’IA offrent aux développeurs plusieurs moyens efficaces d’écrire de meilleurs tests. Ils peuvent d’abord suggérer des cas de test en analysant un document d’exigences et la logique du code de la fonctionnalité. Les modèles peuvent se révéler étonnamment efficaces pour proposer des cas limites et des modes de défaillance qu’un développeur pourrait facilement négliger, surtout lorsqu’il s’est beaucoup concentré sur la fonctionnalité et qu’un second avis lui serait utile.

De plus, les modèles peuvent aider à maintenir les tests à jour à mesure que le code évolue, ce qui réduit les difficultés liées aux refactorisations et évite que des tests obsolètes ne deviennent instables. En prenant en charge les détails élémentaires de l’implémentation des tests et en faisant ressortir les cas limites, les agents de programmation accélèrent le développement des tests.

### Ce que font désormais les ingénieurs

L’écriture de tests avec des outils d’IA ne dispense pas les développeurs de réfléchir aux tests. Au contraire, à mesure que les agents lèvent les obstacles à la génération de code, les tests jouent un rôle toujours plus important de source de vérité sur le fonctionnement de l’application. Comme les agents peuvent exécuter la suite de tests et itérer en fonction des résultats, définir des tests de qualité constitue souvent la première étape pour permettre à un agent de développer une fonctionnalité.

Les développeurs se concentrent plutôt sur les grandes tendances de la couverture de tests, en approfondissant et en remettant en question les cas de test identifiés par le modèle. Accélérer l’écriture des tests leur permet de livrer des fonctionnalités plus rapidement, mais aussi de s’attaquer à des fonctionnalités plus ambitieuses.

| Délégation                                                                                                                                                                                                                                                                          | Révision                                                                                                                                                                                                                                                                                                                                           | Responsabilité                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Les ingénieurs délégueront une première génération des cas de test à partir des spécifications de la fonctionnalité. Ils utiliseront également le modèle pour produire une première version des tests. Il peut être utile de demander au modèle de générer les tests dans une session distincte de celle consacrée à l’implémentation de la fonctionnalité. | Les ingénieurs doivent néanmoins examiner minutieusement les tests générés par le modèle pour s’assurer qu’il n’a pas pris de raccourcis ni implémenté de tests réduits à de simples stubs. Ils veillent également à ce que leurs agents puissent exécuter les tests, disposent des autorisations nécessaires et connaissent le contexte des différentes suites de tests qu’ils peuvent exécuter. | Il incombe aux ingénieurs d’aligner la couverture de tests sur les spécifications des fonctionnalités et les attentes en matière d’expérience utilisateur. La réflexion adversariale, la créativité dans l’identification des cas limites et l’attention portée à l’objectif des tests restent des compétences essentielles. |

### Liste de contrôle pour bien démarrer

- Demandez au modèle d’implémenter les tests lors d’une étape distincte et vérifiez que les nouveaux tests échouent avant de passer à l’implémentation de la fonctionnalité.
- Définissez des consignes de couverture de tests dans votre fichier AGENTS.md
- Fournissez à l’agent des exemples précis d’outils de couverture du code qu’il peut appeler pour évaluer la couverture des tests
  <br />

## 5. Révision

En moyenne, les développeurs consacrent 2 à 5 heures par semaine aux revues de code. Les équipes doivent souvent choisir entre consacrer beaucoup de temps à une revue approfondie et effectuer une revue rapide, jugée « suffisante », pour des changements qui semblent mineurs. Une mauvaise appréciation de ces priorités laisse des bugs passer en production, ce qui pose des problèmes aux utilisateurs et entraîne un important travail de reprise.

### Comment les agents de programmation peuvent aider

Les agents de programmation permettent de généraliser la revue de code afin que chaque PR bénéficie d’un niveau d’attention minimal et constant. Contrairement aux outils d’analyse statique traditionnels, qui reposent sur la reconnaissance de motifs et des contrôles fondés sur des règles, les systèmes de revue par l’IA peuvent réellement exécuter certaines parties du code, interpréter son comportement à l’exécution et suivre la logique entre les fichiers et les services. Pour être efficaces, les modèles doivent toutefois être entraînés spécifiquement à détecter les bugs de niveaux P0 et P1, et ajustés pour fournir des retours concis et pertinents ; les réponses excessivement détaillées sont ignorées aussi facilement que les avertissements de linting peu pertinents.

### Ce que font désormais les ingénieurs

Chez OpenAI, nous constatons que la revue de code par l’IA donne aux ingénieurs davantage l’assurance de ne pas mettre en production de bugs majeurs. Elle détecte souvent des problèmes que le contributeur peut corriger avant de solliciter l’intervention d’un autre ingénieur. La revue de code n’accélère pas nécessairement le traitement des pull requests, surtout lorsqu’elle détecte des bugs importants — mais elle évite des défauts et des interruptions de service.

### Délégation, révision et responsabilité

Même avec la revue de code par l’IA, les ingénieurs restent chargés de s’assurer que le code est prêt à être déployé. Concrètement, ils doivent examiner la modification et en comprendre les implications. Ils délèguent la revue de code initiale à un agent, mais restent responsables de la revue finale et de la fusion.

| Délégation                                                                                                                                                    | Révision                                                                                                                                                                                                                       | Responsabilité                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Les ingénieurs délèguent la première revue de code aux agents. Cela peut se répéter plusieurs fois avant que la pull request ne soit marquée comme prête à être révisée par un collègue. | Les ingénieurs continuent de réviser les pull requests, mais mettent davantage l’accent sur l’alignement architectural. Ils vérifient notamment que les patterns implémentés sont composables, que les conventions appropriées sont appliquées et que la fonctionnalité répond aux exigences. | Les ingénieurs restent en définitive responsables du code déployé en production ; ils doivent s’assurer qu’il fonctionne de manière fiable et répond aux exigences définies. |

Exemple :

Sansan utilise la revue de code de Codex pour détecter les conditions de concurrence et les relations dans les bases de données, des problèmes que les humains négligent souvent. Codex a également pu repérer des cas de codage en dur inapproprié et même anticiper de futurs problèmes de montée en charge.

### Liste de contrôle pour bien démarrer

- Constituez un corpus de PRs de référence menées par des ingénieurs, comprenant à la fois les modifications de code et les commentaires laissés. Conservez cet ensemble comme jeu d’évaluation pour évaluer différents outils.
- Choisissez un produit doté d’un modèle spécifiquement entraîné à la revue de code. Nous avons constaté que les modèles généralistes s’attardent souvent sur des détails insignifiants et présentent un faible rapport signal/bruit.
- Définissez comment votre équipe mesurera la qualité des revues de code. Nous recommandons de suivre les réactions aux commentaires des PRs : c’est un moyen simple de distinguer les bonnes revues des mauvaises.
- Commencez à petite échelle, puis passez rapidement à un déploiement plus large dès que les résultats des revues de code vous inspirent confiance.
  <br />

## 6. Documentation

La plupart des équipes d’ingénierie savent que leur documentation accuse du retard, mais que le rattraper coûte cher. Les connaissances essentielles sont souvent concentrées chez quelques personnes au lieu d’être consignées dans des bases de connaissances interrogeables, et la documentation existante devient vite obsolète, car sa mise à jour détourne les ingénieurs du développement du produit. Même lorsque les équipes organisent des sprints de documentation, cet effort reste généralement ponctuel et son résultat se dégrade dès que le système évolue.

### Comment les agents de programmation peuvent aider

Les agents de programmation savent très bien résumer les fonctionnalités d’un système après en avoir analysé la base de code. En plus d’expliquer le fonctionnement de différentes parties de la base de code, ils peuvent générer des diagrammes système dans des syntaxes comme mermaid. Lorsque les développeurs créent des fonctionnalités avec des agents, il leur suffit de le demander au modèle pour mettre également la documentation à jour. AGENTS.md permet d’inclure automatiquement dans chaque prompt des instructions pour mettre à jour la documentation si nécessaire, afin d’assurer une meilleure cohérence.

Comme les agents de programmation peuvent être exécutés par programmation via des SDKs, ils peuvent aussi être intégrés aux workflows de publication. Par exemple, nous pouvons demander à un agent de programmation d’examiner les commits inclus dans la version à publier et de résumer les principales modifications. Résultat : la documentation fait partie intégrante du pipeline de livraison, devient plus rapide à produire et plus facile à tenir à jour, et ne dépend plus de quelqu’un qui « trouve le temps » de s’en charger.

### Ce que font désormais les ingénieurs

Les ingénieurs passent de la rédaction manuelle de chaque document au pilotage et à la supervision du système. Ils définissent l’organisation des documents, expliquent les raisons importantes qui sous-tendent les décisions, fixent des normes et des modèles clairs à suivre par les agents, puis relisent les contenus critiques ou destinés aux clients. Leur rôle consiste désormais à garantir que la documentation est structurée, exacte et intégrée au processus de livraison, au lieu de tout rédiger eux-mêmes.

| Délégation                                                                                                                                                                                                   | Révision                                                                                                                                                                              | Responsabilité                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Confiez entièrement à Codex les tâches répétitives à faible risque, comme les résumés préliminaires de fichiers et de modules, les descriptions simples des entrées et sorties, les listes de dépendances et les brefs résumés des modifications apportées aux pull requests. | Avant toute publication, les ingénieurs relisent et modifient les documents importants rédigés par Codex, notamment les présentations générales des services principaux, la documentation des API publiques et des SDK, les procédures d’exploitation et les pages d’architecture. | Les ingénieurs restent responsables de la stratégie et de la structure globales de la documentation, des normes et des modèles suivis par l’agent, ainsi que de toute documentation destinée à un public externe ou critique pour la sécurité qui comporte des risques juridiques, réglementaires ou pour l’image de marque. |

### Liste de vérification pour bien démarrer

- Expérimentez la génération de documentation en soumettant des prompts à l’agent de programmation
- Intégrez les consignes relatives à la documentation dans votre fichier AGENTS.md
- Identifiez les workflows (par exemple, les cycles de publication) dans lesquels la documentation peut être générée automatiquement
- Vérifiez que le contenu généré est de qualité, exact et bien ciblé
  <br />

## 7. Déploiement et maintenance

Bien comprendre la journalisation d’une application est essentiel pour assurer la fiabilité des logiciels. Lors d’un incident, les ingénieurs logiciels consultent les outils de journalisation, les déploiements de code et les modifications d’infrastructure afin d’identifier la cause profonde. Ce processus reste souvent étonnamment manuel et oblige les développeurs à passer sans cesse d’un système à l’autre, ce qui leur fait perdre de précieuses minutes dans des situations sous haute pression telles que les incidents.

### Comment les agents de programmation peuvent aider

Avec les outils de programmation basés sur l’IA, vous pouvez fournir le contexte de votre base de code, mais aussi donner accès à vos outils de journalisation via des serveurs MCP. Les développeurs disposent ainsi d’un workflow unique dans lequel ils peuvent demander au modèle d’examiner les erreurs d’un point de terminaison donné. Le modèle peut ensuite s’appuyer sur ce contexte pour parcourir la base de code et trouver les bugs ou les problèmes de performances pertinents. Comme ils peuvent aussi utiliser des outils en ligne de commande, les agents de programmation peuvent examiner l’historique git afin d’identifier les modifications précises susceptibles d’être à l’origine des problèmes visibles dans les traces de journalisation.

### Ce que font désormais les ingénieurs

En automatisant les aspects fastidieux de l’analyse des journaux et du triage des incidents, l’IA permet aux ingénieurs de se concentrer sur la résolution de problèmes plus complexes et l’amélioration des systèmes. Au lieu de rapprocher manuellement les journaux, les commits et les modifications d’infrastructure, les ingénieurs peuvent valider les causes profondes identifiées par l’IA, concevoir des correctifs robustes et élaborer des mesures préventives. Ce changement réduit le temps consacré à la gestion réactive des urgences et permet aux équipes d’investir davantage dans l’ingénierie proactive de la fiabilité et les améliorations architecturales.

| Délégation                                                                                                                                                      | Révision                                                                                                                                                                      | Responsabilité                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| De nombreuses tâches d’exploitation peuvent être déléguées aux agents : analyser les journaux, faire remonter les métriques anormales, identifier les modifications de code suspectes et même proposer des correctifs urgents. | Les ingénieurs vérifient et affinent les diagnostics générés par l’IA, en confirment l’exactitude et approuvent les mesures correctives. Ils veillent à ce que les correctifs respectent les normes de fiabilité, de sécurité et de conformité. | Les décisions critiques restent du ressort des ingénieurs, surtout lors d’incidents inédits, de modifications sensibles en production ou lorsque le modèle affiche un faible degré de confiance. Les humains restent responsables de l’appréciation et de la validation finale. |

Exemple :

Virgin Atlantic utilise Codex pour renforcer les pratiques de ses équipes en matière de déploiement et de maintenance des systèmes. Avec Codex VS Code Extension, les ingénieurs disposent d’un espace unique pour examiner les journaux, retracer l’origine des problèmes dans le code et les données, et vérifier les modifications via Azure DevOps MCP et Databricks Managed MCPs. En centralisant ce contexte d’exploitation dans l’IDE, Codex accélère l’identification des causes profondes, réduit le triage manuel et aide les équipes à se concentrer sur la validation des correctifs et l’amélioration de la fiabilité des systèmes.

### Liste de vérification pour bien démarrer

- Connectez les outils d’IA aux systèmes de journalisation et de déploiement : intégrez Codex CLI ou un outil similaire à vos serveurs MCP et à vos agrégateurs de journaux.
- Définissez les périmètres d’accès et les autorisations : assurez-vous que les agents peuvent accéder aux journaux pertinents, aux dépôts de code et aux historiques de déploiement, tout en respectant les bonnes pratiques de sécurité.
- Configurez des modèles de prompts : créez des prompts réutilisables pour les requêtes opérationnelles courantes, par exemple « Analysez les erreurs du point de terminaison X » ou « Analysez les pics d’activité dans les journaux après le déploiement. »
- Testez le workflow : simulez des incidents pour vérifier que l’IA présente le contexte pertinent, retrace précisément le cheminement dans le code et propose des diagnostics exploitables.
- Améliorez le workflow par itérations : recueillez les retours tirés d’incidents réels, affinez vos stratégies de prompts et étendez les capacités des agents à mesure que vos systèmes et processus évoluent.
  <br />

## Conclusion

Les agents de programmation transforment le cycle de vie du développement logiciel en prenant en charge les tâches d’exécution en plusieurs étapes qui ralentissaient traditionnellement les équipes d’ingénierie. Grâce à un raisonnement prolongé, à un contexte unifié à l’échelle de la base de code et à la capacité d’exécuter de vrais outils, ces agents prennent désormais en charge des tâches allant du cadrage et du prototypage à l’implémentation, aux tests, à la revue de code et même au triage opérationnel. Les ingénieurs gardent pleinement la maîtrise de l’architecture, des objectifs produit et de la qualité, mais les agents de programmation réalisent de plus en plus la première passe d’implémentation et les accompagnent en continu à chaque phase du SDLC.

Cette évolution n’exige aucune refonte radicale ; de petits workflows ciblés produisent rapidement des effets cumulatifs à mesure que les agents de programmation gagnent en capacité et en fiabilité. Les équipes qui commencent par des tâches bien délimitées, mettent en place des garde-fous et élargissent progressivement les responsabilités des agents obtiennent des gains notables en rapidité et en cohérence, tout en permettant à leurs développeurs de mieux se concentrer.

Si vous étudiez comment les agents de programmation peuvent accélérer le travail de votre organisation ou si vous préparez votre premier déploiement, contactez OpenAI. Nous sommes là pour vous aider à en faire un véritable levier : nous concevons des workflows de bout en bout couvrant la planification, la conception, le développement, les tests, la revue de code et les opérations, et aidons votre équipe à adopter des pratiques adaptées à la production qui concrétisent une ingénierie pensée dès l’origine autour de l’IA.

[image1]: /images/codex/guides/build-ai-native-engineering-team.png
