<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/build-and-deploy-internal-apps -->

## Créer et déployer en une seule tâche

Sites est un service d’hébergement géré dans ChatGPT. Demandez à ChatGPT de créer une application : il peut développer le projet, l’exécuter pour le tester, le déployer et vous fournir une URL à partager.

Sites est disponible en bêta publique pour les offres payantes éligibles. Au lancement, il n’est pas disponible avec les offres Free ou Go, ni dans l’EEE, en Suisse ou au Royaume-Uni. Son déploiement progressif ou les paramètres de l’espace de travail peuvent également influer sur l’accès.

Le périmètre va des sites statiques aux applications web full-stack en JavaScript ou TypeScript. Sites convient donc bien aux outils internes ciblés : tableaux de bord d’accueil des nouveaux collaborateurs, centres de formation, bibliothèques de ressources avec fonction de recherche, applications de workflow légères et vues de reporting.

Consultez la [documentation de Sites](/fr-FR/codex/sites) pour obtenir des instructions sur la configuration, le stockage, le déploiement et l’accès.

Commencez par un seul workflow utile. Une première version clairement délimitée est plus facile à réviser, à déployer et à améliorer qu’une demande trop vaste visant à recréer tout un système interne.

## À quoi s’attendre

Voici un exemple fictif fondé sur un brief de lancement joint et cinq exemples de demandes. La première itération permet de créer et de vérifier un outil ciblé de suivi des demandes ; la suivante ajoute un filtre par responsable et permet de repérer plus facilement les demandes en retard.

<div data-use-case-export-only>

L’outil de suivi des demandes de lancement s’ouvre avec **cinq exemples de demandes**, dont une demande bloquée, deux en cours de révision et une en retard. L’équipe peut les parcourir par lancement et par statut, filtrer les demandes bloquées, ajouter une demande et mettre à jour son statut. Le parcours principal et l’enregistrement de l’état ont été vérifiés aux formats ordinateur et mobile.

Après une demande complémentaire, l’outil comporte un filtre par responsable et met en évidence les demandes en retard ; **les demandes bloquées restent en tête et une demande ne peut pas être marquée comme prête sans responsable**. L’aperçu reste privé ; aucun Site n’a été publié et l’accès n’a pas été modifié.

</div>

## Fournir à ChatGPT le contexte du workflow

Indiquez à ChatGPT à qui l’application est destinée, ce que les utilisateurs doivent y faire, quels documents sources il doit consulter et quelles informations doivent être conservées d’une session à l’autre. Précisez clairement le périmètre de partage prévu et demandez-lui de tester le parcours principal avant le déploiement.

Utilisez des [plugins](/fr-FR/codex/plugins) pour récupérer ou actualiser les données provenant de sources internes connectées. Dans Work sur le Web, ou dans Work ou Codex sur ordinateur, lancez une tâche Sites qui utilise des applications connectées ou des fichiers dans le cloud. Utilisez l’application de bureau pour un fichier local, le navigateur intégré pour un site auquel vous êtes connecté, ou l’extension Chrome Codex pour une session Chrome existante.

  Si vous devez récupérer des données en temps réel, vous pouvez vous connecter à un outil tiers à l’aide d’une
  clé API configurée dans les paramètres du Site. N’incluez aucune valeur secrète dans les prompts
  ni dans les fichiers. Si vous souhaitez utiliser les connexions de plugins, vous pouvez [planifier des opérations depuis
  la tâche actuelle](/fr-FR/codex/automations#schedule-work-from-a-task) afin de récupérer des données
  avec des plugins selon une fréquence définie, mettre à jour l’application et enregistrer une version à réviser.
  Ne déployez la version révisée qu’après son approbation.

## Choisir le stockage de l’application

De nombreuses applications internes doivent conserver leurs données d’une session à l’autre. Sites propose deux mécanismes de stockage :

- Utilisez D1, une base de données compatible avec SQLite, pour stocker des données structurées telles que l’état des listes de contrôle, les favoris, les filtres, les annotations, la configuration et les métadonnées de fichiers.
- Utilisez le stockage d’objets R2 pour les données binaires de fichiers, comme les documents importés, les images ou les autres ressources qui doivent être conservées.

Conservez les métadonnées structurées dans D1 et les objets de fichiers plus volumineux dans R2. Une page de ressources en lecture seule ou un petit site statique peut n’avoir besoin d’aucun des deux.

Sites ne prend en charge ni la résidence des données ni celle des inférences. Ne l’utilisez pas pour traiter des informations de santé protégées ou des données de cartes de paiement, ni pour permettre des transactions financières. Consultez les [restrictions de Sites relatives aux données et à l’utilisation](https://help.openai.com/en/articles/20001339-creating-and-managing-chatgpt-sites) avant de stocker des informations sensibles.

## Gérer et partager vos projets

Vous pouvez définir qui peut accéder à vos projets déployés.

Conservez tout nouveau projet en mode privé pendant que vous examinez son contenu, la façon dont il traite les données et le public auquel il est destiné.

Selon les paramètres de votre compte et de votre espace de travail, vous pouvez le partager avec :

- Les personnes que vous invitez.
- Tous les membres de votre espace de travail.
- Toute personne sur Internet.

Les personnes avec qui vous partagez le projet peuvent le consulter, mais pas le modifier. Pour modifier l’accès, ouvrez [Sites dans ChatGPT](https://chatgpt.com/sites) ou demandez-le directement à ChatGPT :

Le partage public convient également à un guide d’événement simple, à une page de ressources pour un club ou à tout autre site destiné à des personnes extérieures à un espace de travail. Dans les espaces de travail Entreprise, la publication publique est désactivée par défaut et doit être activée par un administrateur. Gardez les données internes privées, même lorsqu’un lien public est disponible.

## Exemples

La [galerie Sites](/showcase/sites) propose des exemples de Sites accompagnés de leurs prompts complets.

{/* vale Vale.Spelling = NO */}
{/* vale Vale.Terms = NO */}

- **[Onboarding Hub](/showcase/onboarding-hub)** combine une liste de contrôle pour la première semaine, des ressources, des notes et des documents importés. Il utilise D1 pour l’état de l’utilisateur et les métadonnées des fichiers, et R2 pour les données binaires des fichiers importés.
- **[Enablement Hub](/showcase/enablement-hub)** propose une bibliothèque de contenus de formation avec fonction de recherche, des filtres et des favoris enregistrés, le tout reposant sur D1.
- **[Pulse Dashboard](/showcase/pulse-dashboard)** présente des métriques, des tendances et des informations sur la traçabilité des données, tout en utilisant D1 pour la configuration et les instantanés en cache.
- **[Sparkboard](/showcase/idea-intake)** transforme la collecte des idées des collaborateurs en workflow, avec des soumissions authentifiées, des votes, des commentaires, des tableaux de suivi et un classement des contributeurs.
- **[Launch Cal](/showcase/launch-cal)** organise les prochains lancements de produits dans un calendrier mensuel comprenant des filtres, des indicateurs de risque, des listes de contrôle et des références aux sources connectées.
- **[Event Planning Hub](/showcase/event-planning-hub)** regroupe les demandes liées aux événements, les approbations, les modèles, les jalons, la préparation au respect des politiques et les ressources de planification connectées.

{/* vale Vale.Terms = YES */}
{/* vale Vale.Spelling = YES */}

Utilisez ces exemples comme points de départ, puis ciblez plus précisément le prompt sur le workflow et les sources de votre équipe.
