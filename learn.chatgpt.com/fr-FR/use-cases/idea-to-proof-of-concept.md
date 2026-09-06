<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/idea-to-proof-of-concept -->

## Commencez par définir une orientation visuelle

GPT Image 2 excelle dans la génération de maquettes d’interface de haute qualité. Pour explorer de nouvelles idées sans partir de zéro, vous pouvez vous appuyer sur la génération d’images pour définir une orientation visuelle.

Vous pouvez procéder de deux façons :

- Affinez l’orientation visuelle à l’aide du skill ImageGen. Une fois que l’interface proposée vous convient, vous pouvez demander à Codex de créer un prototype qui reprend ce rendu visuel. Dans ce cas, sélectionnez Codex, démarrez une nouvelle discussion et joignez l’image finale que vous souhaitez implémenter au lieu de poursuivre directement la discussion dans ChatGPT. Codex obtient de meilleurs résultats lorsqu’il peut s’appuyer sur une pièce jointe fournie par l’utilisateur.
- Utilisez un plugin et décrivez simplement votre idée : il générera l’orientation visuelle et prendra en charge la suite.

## Appuyez-vous sur un plugin

Si vous n’avez pas besoin d’affiner l’orientation visuelle avant de commencer l’implémentation, vous pouvez utiliser un plugin et décrire votre idée.

Utilisez le [plugin Build Web Apps](https://github.com/openai/plugins/tree/main/plugins/build-web-apps)
pour les applications web, les tableaux de bord, les sites web créatifs et les outils à forte composante frontend. Son
workflow amène Codex à générer d’abord un design, à le reproduire dans le code, puis à utiliser le
navigateur pour comparer le résultat au concept.

Utilisez le [plugin Game Studio](https://github.com/openai/plugins/tree/main/plugins/game-studio)
lorsque la preuve de concept est un jeu sur navigateur. Ce parcours devrait définir les
verbes du joueur, la première boucle de jeu jouable, le moteur, le workflow de création des ressources, le HUD, les commandes et le test
dans le navigateur avant d’enrichir le jeu.

## Workflow d’itération

Une bonne preuve de concept se limite à un MVP qui peut être implémenté rapidement et validé avec l’équipe.
Si vous souhaitez vous assurer que le MVP fonctionne comme prévu, vous pouvez utiliser Playwright interactive pour que Codex vérifie son propre travail.

Une fois la première version opérationnelle, vous pouvez la faire évoluer en demandant des modifications ciblées dans la même discussion :
