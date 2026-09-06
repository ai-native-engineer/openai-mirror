<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/chatgpt-apps -->

## Ce que vous allez créer

Chaque plugin reposant sur MCP comporte trois parties :

- Un serveur MCP qui définit les outils, renvoie les données, impose l’authentification et indique à ChatGPT où trouver les éventuelles ressources d’interface utilisateur.
- Un composant web facultatif qui s’affiche dans une iframe au sein de ChatGPT. Vous pouvez le créer avec React ou avec du HTML, du CSS et du JavaScript sans framework.
- Un modèle qui décide quand appeler les outils du plugin en fonction des métadonnées que vous fournissez.

Codex est particulièrement utile lorsqu’il prend en charge les tâches d’ingénierie répétitives liées à ces éléments :

- Planification de l’ensemble des outils et de leurs métadonnées.
- Génération de la structure initiale du serveur et du widget.
- Configuration des scripts d’exécution locale.
- Ajout, par passes ciblées, de l’authentification et des adaptations nécessaires au déploiement.
- Mise en place de la boucle de vérification qui confirme le bon fonctionnement du plugin dans ChatGPT.

## Pourquoi Codex est particulièrement adapté

- Les plugins reposant sur MCP se structurent clairement autour d’un serveur, d’une interface utilisateur facultative et d’appels d’outils
pilotés par le modèle.
- La conception de prompts pour Codex fonctionne mieux lorsque la tâche est explicite, bien délimitée et
facile à vérifier, ce qui correspond parfaitement au travail de création d’un plugin.
- Les Skills et `AGENTS.md` fournissent à Codex les instructions réutilisables et les règles du projet dont il a besoin pour rester ancré dans le contexte.

Pour en savoir plus sur l’installation et l’utilisation des Skills, consultez notre [documentation sur les Skills](/fr-FR/codex/build-skills).

## Utilisation

## Prérequis

- Concentrez-vous d’abord sur un seul objectif utilisateur central plutôt que de tenter de transposer un produit entier dans une conversation.
- Choisissez d’emblée la stack technique : TypeScript ou Python pour le serveur, et React ou du HTML, du CSS et du JavaScript sans framework pour le widget.
- Déterminez la solution d’accès HTTPS que vous utiliserez pendant le développement, par exemple `ngrok` ou Cloudflare Tunnel.
- Certains paramètres emploient encore d’anciens termes pour désigner une connexion à un serveur MCP. Pendant
les tests locaux, considérez que ces libellés font référence au serveur enregistré.

1. Commencez par un seul objectif précis pour le plugin et demandez à Codex de proposer entre trois et cinq outils dont les noms, les descriptions, les entrées et les sorties sont explicites.
2. Déterminez si la v1 peut se limiter aux données ou si elle nécessite un widget, puis générez la structure du serveur MCP et du widget facultatif en suivant les conventions existantes du dépôt avant d’ajouter des dépendances.
3. Exécutez le serveur MCP en local via HTTPS, connectez-le à ChatGPT en mode développeur, puis testez-le avec un petit jeu de prompts directs, indirects et négatifs.
4. Affinez les métadonnées, la gestion de l’état, `structuredContent` et les charges utiles `_meta` jusqu’à ce que le flux de lecture principal fonctionne de manière fiable dans ChatGPT.
5. N’ajoutez OAuth 2.1 que lorsque des données propres à l’utilisateur ou des actions d’écriture l’exigent, sans compliquer les flux anonymes ou en lecture seule.
6. Préparez une prévisualisation hébergée avec un point de terminaison `/mcp` stable, vérifiez le streaming et l’hébergement des ressources de l’interface utilisateur, puis passez en revue la liste de contrôle du lancement avant de partager ou de soumettre le plugin.

## Prompts suggérés

Les prompts efficaces pour ce workflow reposent sur les mêmes éléments :

- Un objectif clair : indiquez ce que le plugin doit aider l’utilisateur à accomplir dans ChatGPT.
- Une stack concrète : précisez si vous souhaitez utiliser TypeScript ou Python sur le serveur, et si le widget doit utiliser React ou rester léger.
- Des limites explicites pour les outils : demandez à Codex de proposer ou de créer un petit ensemble d’outils, chacun consacré à une seule tâche.
- Les attentes en matière d’authentification : précisez si la première version peut être anonyme ou si elle nécessite des comptes associés et des actions d’écriture.
- Un parcours de développement local : indiquez le tunnel ou le mode d’hébergement que vous prévoyez d’utiliser pour les tests HTTPS dans ChatGPT.
- Des étapes de vérification : indiquez à Codex les commandes à exécuter, les prompts à tester et les éléments de preuve à fournir.

Évitez un prompt monolithique qui regroupe en une seule passe la planification, l’implémentation, l’authentification, le déploiement, la soumission et le peaufinage. Décomposez plutôt le travail en jalons plus petits.

**Planifiez le plugin avant d’en générer la structure**

**Générez la structure de la première version fonctionnelle**

**N’ajoutez l’authentification qu’une fois le flux principal opérationnel**

**Préparez le plugin pour son déploiement et sa révision**

## Préparation au lancement

- Le plugin répond à un seul objectif, clairement délimité et compréhensible par les utilisateurs.
- L’ensemble d’outils reste limité et ses métadonnées, entrées et sorties sont explicites.
- Le serveur MCP fonctionne de bout en bout, renvoie un champ `structuredContent` concis et réserve à `_meta` les données destinées uniquement au widget.
- Le widget, s’il est nécessaire, s’affiche correctement dans ChatGPT.
- La boucle locale de tests HTTPS fonctionne via le mode développeur de ChatGPT.
- Un petit jeu de prompts directs, indirects et négatifs passe les tests en produisant le flux de conversation attendu et les charges utiles attendues pour les outils.
- L’authentification n’est ajoutée que lorsqu’elle est requise par des données propres à l’utilisateur ou des actions d’écriture.
- Un plan de déploiement et une révision de l’état de préparation au lancement couvrent les métadonnées, les indications sur les outils, la confidentialité et les prompts de test avant que le plugin ne soit partagé ou soumis.

## Pièges courants

- Demander à Codex de porter tout le produit dans ChatGPT. Meilleure approche : demandez-lui de se limiter à un objectif utilisateur principal, trois à cinq outils et un seul widget au périmètre restreint.
- Commencer par un énorme prompt d’implémentation. Meilleure approche : divisez le travail en phases distinctes de planification, de création de l’ossature, d’authentification, de déploiement et de révision.
- Développer l’interface utilisateur avant d’avoir clairement défini le contrat des outils. Meilleure approche : définissez d’abord les outils exposés et le schéma de réponse, puis créez le widget.
- Ne pas s’appuyer sur la documentation officielle. Meilleure approche : associez `$chatgpt-apps` à `$openai-docs` afin que l’ossature respecte les recommandations actuelles relatives aux plugins.
- Ne s’occuper des métadonnées qu’après coup. Meilleure approche : rédigez tôt les descriptions des outils et la documentation des paramètres, puis rejouez un jeu de prompts pour les valider.
- Ajouter l’authentification avant d’avoir validé le parcours anonyme ou en lecture seule. Meilleure approche : faites d’abord fonctionner le flux principal des outils, puis ajoutez OAuth aux outils qui en ont réellement besoin.
- Considérer le plugin comme terminé avant de l’avoir testé dans ChatGPT. Meilleure approche : connectez
le serveur MCP en mode développeur, inspectez les charges utiles des outils et vérifiez le véritable
flux de conversation.
