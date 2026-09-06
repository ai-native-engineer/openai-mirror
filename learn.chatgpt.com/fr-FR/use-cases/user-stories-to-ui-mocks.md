<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/user-stories-to-ui-mocks -->

## Introduction

Les équipes produit recueillent souvent des retours provenant de différentes sources, comme des fils de discussion Slack, des tickets Linear, des documents ou feuilles de calcul Google Drive, ou encore des notes prises lors d’appels avec des clients. Elles disposent parfois de user stories claires illustrant un problème à résoudre ; dans d’autres cas, le contexte se trouve dans ces sources.

ChatGPT peut rassembler ce contexte et en tirer une maquette d’interface pour une fonctionnalité qui résoudrait le problème. Une fois cette orientation validée, Codex peut implémenter la fonctionnalité dans le produit.

## Générez une référence visuelle

Si vous disposez d’une user story claire, commencez par celle-ci. Sinon, échangez d’abord avec ChatGPT pour recueillir le contexte dans différentes sources, puis synthétisez-le sous forme de user story.

Demandez ensuite à ChatGPT d’utiliser la génération d’images pour créer plusieurs pistes visuelles sous forme de maquettes. Les maquettes doivent respecter l’architecture de l’information du produit et les contraintes de son système de design.

Si cela peut vous aider, fournissez comme référence des captures d’écran de l’interface actuelle ou un fichier Figma.

Procédez ainsi jusqu’à ce que la maquette vous convienne. Plus les modifications sont ciblées, plus Codex a de chances de générer une maquette directement implémentable.

## Passez de la maquette au prototype

Utilisez l’image de la maquette finale que vous souhaitez faire implémenter par Codex. Sélectionnez Codex, démarrez une nouvelle discussion et joignez à nouveau l’image, au lieu de poursuivre directement la discussion dans ChatGPT. Demandez ensuite à Codex d’implémenter la maquette pour en faire un prototype fonctionnel, en utilisant éventuellement le [plugin Build Web Apps](https://github.com/openai/plugins/tree/main/plugins/build-web-apps) si vous développez une application web :
