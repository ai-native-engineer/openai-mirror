<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/figma-designs-to-code -->

## Introduction

Lorsque vous disposez d’une sélection Figma précise, Codex peut la transformer en une interface soignée tout en respectant les conventions déjà établies dans votre projet.

Avec le skill Figma, Codex peut utiliser le serveur MCP de Figma pour récupérer un contexte de design structuré, des variables, des ressources et la variante exacte à implémenter.

Grâce au skill interactif Playwright, Codex peut ouvrir l’application dans un navigateur réel, comparer l’implémentation à la référence Figma, puis ajuster la mise en page ou le comportement jusqu’à rapprocher le résultat de la cible.

## Configurez votre projet Figma

Plus votre fichier Figma est propre, meilleure sera la première implémentation. Pour faciliter le passage de relais :

- Utilisez des variables ou des tokens de design dès que possible, en particulier pour les couleurs, la typographie et l’espacement
- Créez des composants pour les éléments d’interface réutilisables au lieu de dupliquer des calques dissociés
- Utilisez autant que possible la mise en page automatique au lieu du positionnement manuel
- Nommez les frames et les calques assez clairement pour que l’écran principal, l’état et les variantes soient faciles à identifier
- Conservez si possible les icônes et images réelles dans le fichier pour que Codex n’ait pas à les deviner

Codex dispose ainsi d’une structure plus claire pour produire une interface robuste et prête pour la production.

## Soyez précis

Plus vous préciserez les modes d’interaction attendus et le style souhaité, meilleur sera le résultat.

Si un état, un point de rupture ou une interaction a de l’importance, indiquez-le. Si le fichier contient plusieurs variantes proches, indiquez à Codex laquelle doit servir de référence.

Plus vous préciserez clairement ce qui doit être reproduit à l’identique et les aspects pour lesquels les conventions du dépôt doivent primer, plus Codex pourra effectuer facilement les bons arbitrages.

## Préparez le système de design

Codex fonctionne mieux lorsque le dépôt cible dispose déjà d’une couche de composants clairement définie. Il peut automatiquement réutiliser vos composants et votre système de design existants au lieu de les recréer de zéro.

Si vous le jugez nécessaire, indiquez à Codex les primitives à réutiliser, l’emplacement de vos tokens et ce qui fait référence dans le dépôt pour les boutons, les champs de saisie, les cartes, la typographie et les icônes.

Considérez la sortie du MCP de Figma, qui ressemble souvent à du code React avec Tailwind, comme une référence structurelle plutôt que comme le style de code final. Demandez à Codex d’adapter cette sortie aux utilitaires réellement employés par le projet, aux wrappers de composants, au système de couleurs, à l’échelle typographique, aux tokens d’espacement ainsi qu’aux conventions de routage, de gestion de l’état et de récupération des données.

## Workflow

### Commencez par une sélection Figma

Copiez le lien vers la frame, le composant ou la variante Figma précise à implémenter. Comme le workflow MCP de Figma repose sur les liens, celui-ci doit pointer vers le nœud exact souhaité, et non vers une frame parente située à proximité.

### Demandez à Codex d’utiliser Figma

La première passe doit s’appuyer sur Figma. Demandez à Codex de suivre le workflow MCP de Figma avant de commencer l’implémentation.

Éléments à inclure dans votre prompt :

Une fois la première implémentation en place, Codex utilisera Playwright pour vérifier l’interface dans un navigateur réel et corriger les derniers écarts visuels ou d’interaction.
