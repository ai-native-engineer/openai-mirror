<!-- source: https://learn.chatgpt.com/fr-FR/docs/extend/record-and-replay -->

La fonctionnalité Enregistrer et rejouer est disponible sur macOS. La fonctionnalité Utilisation de l’ordinateur doit également être disponible et activée.

La fonctionnalité Enregistrer et rejouer vous permet de montrer un workflow sur votre
Mac et d’en faire un skill réutilisable. Utilisez-la si le workflow est répétitif,
dépend de vos préférences ou est plus facile à montrer qu’à décrire dans un prompt.

Vous pouvez par exemple enregistrer la manière dont vous déclarez une note de frais, réservez une place de stationnement,
créez un ticket correctement configuré, publiez une vidéo ou téléchargez un
rapport récurrent. ChatGPT ou Codex peut transformer cette procédure en skill que vous pourrez réutiliser
avec la fonctionnalité Utilisation de l’ordinateur, des actions dans le navigateur, des plugins connectés ou une combinaison
de ces outils.

## Avant de commencer

Choisissez un workflow que vous savez déjà exécuter. La fonctionnalité Enregistrer et rejouer fonctionne
mieux lorsque les étapes sont stables et que les critères de réussite sont clairs.

## Démarrer un enregistrement

1. Dans l’application de bureau ChatGPT, sélectionnez ChatGPT, puis activez le mode Work dans le sélecteur, ou sélectionnez Codex. Ouvrez ensuite **Plugins**.
2. Ouvrez le menu **+** .
3. Sélectionnez **Enregistrer un skill**.
4. Vérifiez le prompt suggéré, ajoutez tout contexte utile, puis envoyez-le.
5. Lorsque la discussion vous demande l’autorisation d’enregistrer vos actions, approuvez la
demande dès que vous pouvez commencer à montrer le workflow.
6. Exécutez le workflow sur votre Mac.
7. Une fois le workflow terminé, arrêtez l’enregistrement depuis la barre des menus ou l’interface superposée, ou indiquez dans la
discussion que vous avez terminé.

Pendant l’enregistrement, ChatGPT ou Codex observe les actions et le contenu des fenêtres
nécessaires à l’apprentissage du workflow. L’enregistrement continue jusqu’à ce que vous l’arrêtiez. Veillez à ce que
l’enregistrement reste centré sur la tâche que le skill doit permettre d’exécuter.

Après l’arrêt de l’enregistrement, ChatGPT ou Codex analyse le workflow capturé et
génère une première version du skill. Le skill indique quand utiliser le workflow, quelles entrées sont
nécessaires, quelles étapes suivre et comment vérifier le résultat. Vous pouvez également demander
d’autres améliorations.

## Rejouer le workflow

Démarrez une nouvelle discussion dans ChatGPT ou Codex et demandez-lui d’utiliser le skill généré. Précisez
les valeurs qui diffèrent cette fois-ci, comme le fichier à charger, le
ticket à créer ou la plage de dates du rapport.

Le produit utilise le skill comme contexte réutilisable pour la tâche. Il peut ensuite
exécuter le workflow avec les outils disponibles dans l’environnement actuel,
notamment la fonctionnalité Utilisation de l’ordinateur, les actions dans le navigateur et les plugins installés.

## Conseils pour réussir vos enregistrements

- Veillez à ce que la démonstration soit courte et complète.
- Avant de commencer l’enregistrement, indiquez votre objectif et les entrées spécifiques susceptibles de varier d’une
utilisation du skill à l’autre.
- Utilisez des entrées réalistes, mais évitez les secrets et les données sensibles.
- Après l’enregistrement, affinez le skill afin d’expliciter les préférences implicites importantes,
comme les conventions de nommage, les valeurs par défaut des champs ou les points de décision.
- Arrêtez l’enregistrement une fois le workflow terminé, plutôt que de poursuivre avec des tâches de
nettoyage sans rapport avec celui-ci.

## Quand créer un autre plugin

La fonctionnalité Enregistrer et rejouer permet de créer rapidement un skill à partir d’un workflow dont vous faites la démonstration.
Si vous souhaitez distribuer un package distinct et stable à toute une équipe, regrouper
plusieurs skills, inclure des connecteurs, ajouter des serveurs MCP ou gérer les
métadonnées d’installation, créez un plugin dédié à ce workflow. Consultez
[Créer des plugins](https://developers.openai.com/plugins/build/plugins).

## Dépannage

### Je ne vois pas Enregistrer et rejouer

Si votre organisation gère Codex avec `requirements.toml`, l’exigence
`[features].computer_use` détermine également la disponibilité de la fonctionnalité Enregistrer et rejouer. Définir
`computer_use = false` rend les deux fonctionnalités indisponibles.
