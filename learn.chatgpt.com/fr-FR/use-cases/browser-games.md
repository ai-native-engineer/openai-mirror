<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/browser-games -->

## Introduction

La création d’un jeu illustre particulièrement bien que Codex ne se limite pas à générer du code. Un véritable jeu nécessite généralement un concept formalisé, une couche de rendu, la mise en place d’une structure frontend, la gestion de l’état côté backend, la production de ressources et des ajustements visuels constants

Pour ce cas d’usage, les meilleurs résultats s’obtiennent lorsque Codex commence par décrire précisément ce que le jeu doit faire, puis procède par itérations avec Playwright interactive pour le tester directement dans un navigateur.

## Commencez par le plan du jeu

Avant que Codex ne mette en place la moindre structure, demandez-lui de créer un `PLAN.md` qui définit concrètement le jeu :

- l’objectif du joueur
- la boucle de jeu principale
- les entrées et les commandes
- les conditions de victoire et d’échec
- la progression ou la difficulté
- la direction artistique
- les hypothèses concernant la stack et l’hébergement
- l’ordre des étapes clés

Ce plan est important, car « créer un jeu » est en soi trop vague. Codex doit savoir comment implémenter chaque partie du jeu et, souvent, se reporter aux détails d’implémentation au fil du développement.

Vous pouvez activer le Mode plan avec la commande slash `/plan`.
Enregistrez ensuite le résultat dans un fichier `PLAN.md`.

## Définissez le comportement de Codex avec AGENTS.md

Pour que Codex suive le plan, vérifie son travail et utilise les bons outils, définissez un fichier `AGENTS.md` comme dans l’exemple suivant :

```text
# Game name

Tech Stack:

- NextJS for frontend (hosted on Vercel)
- <insert technology> for rendering
- Fastify for backend, websockets (hosted on <hosting platform>)
- Postgres for database (hosted on <hosting platform>)
- Redis for caching and pub/sub (hosted on <hosting platform>)
- OpenAI for generative AI features

Tips:

- Use build and test commands to verify your work as soon as you complete a feature or task
- Use the PLAN.md file to guide your work when building new features
- Log your work under .logs (create new log files as you see fit) to record your thought process and decisions, and reference them when iterating on features
- Use playwright to test the visual output of your work, and iterate if it doesn't look right or fit the vibe
- Use imagegen to generate visual assets for your work, and every time you generate a collection of assets, save the prompts you used to be able to continue generating more of the same assets later (create files in .prompts)
- Use Context7 MCP to fetch <rendering framework> docs

Codex peut ainsi travailler longtemps en autonomie et utiliser les Skills nécessaires selon les besoins.

## Exploitez les Skills

Ajoutez les Skills que mentionne le fichier AGENTS.md :

- Imagegen, afin que Codex puisse générer les ressources visuelles du jeu selon les besoins
- Playwright interactive, afin que Codex puisse tester le jeu directement dans un navigateur
- Documentation OpenAI, afin que Codex puisse récupérer la documentation la plus récente de l’API OpenAI
- Vous pouvez également ajouter le serveur MCP Context7 pour récupérer la documentation la plus récente du framework de rendu

Pour en savoir plus sur l’ajout de Skills, consultez la [documentation sur les Skills](/fr-FR/codex/build-skills).

  **Conseil** : demandez à Codex d’enregistrer dans un fichier les prompts de génération d’images afin que
  toutes les ressources visuelles soient cohérentes. Décrivez le style des ressources que vous
  souhaitez générer, puis laissez Codex élaborer des prompts détaillés et réutilisables.

## Laissez Codex travailler par itérations

Codex générera une première version du jeu à partir du plan initial.

Si vous devez générer un grand nombre de ressources visuelles, la création de cette première version peut prendre du temps, parfois plusieurs heures. Comme Codex peut tester son travail et essayer le jeu directement dans un navigateur, il peut poursuivre son travail longtemps sans aucune intervention de votre part.

Plus le plan est précis, meilleur sera le résultat final après la première itération.

Au fil de vos tests, affinez le jeu selon vos besoins en fournissant des captures d’écran et en demandant des modifications du gameplay ou des mises à jour des ressources visuelles, jusqu’à ce que le résultat vous convienne.
