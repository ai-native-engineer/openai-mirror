<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/frontend-designs -->

## Introduction

Lorsque vous disposez de captures d’écran, d’un court brief de design ou de quelques références dont vous inspirer, Codex peut les convertir en une interface responsive tout en respectant les conventions déjà établies dans votre projet.

Avec la skill Playwright, Codex peut ouvrir l’application dans un vrai navigateur, comparer l’implémentation à vos captures d’écran pour différentes tailles d’écran, puis ajuster la mise en page ou le comportement jusqu’à se rapprocher du résultat attendu.

## Partez de vos références

Fournissez à Codex les références les plus claires dont vous disposez pour l’interface souhaitée. Une seule capture d’écran peut suffire pour une tâche ciblée, mais la transmission des consignes est plus efficace si vous incluez plusieurs états, par exemple les mises en page pour ordinateur et mobile, les états de survol ou de sélection, ainsi que les vues vides ou de chargement pertinentes.

Les références n’ont pas besoin d’être des livrables de design parfaits. Elles doivent simplement donner une vision suffisamment concrète de la hiérarchie, de l’espacement et de la direction visuelle souhaités pour que Codex n’ait pas à faire de suppositions.

## Soyez précis

Plus vos indications sur les schémas d’interaction attendus et le style souhaité sont précises, meilleur sera le résultat.
Le modèle a tendance à privilégier les schémas et les styles les plus courants ; si vos références ne montrent pas clairement que vous souhaitez autre chose, l’interface risque donc de paraître générique.
Plus vous fournissez d’éléments, qu’il s’agisse de références supplémentaires ou d’instructions plus précises, plus l’interface obtenue pourra se démarquer.

## Préparez le système de design

Codex fonctionne mieux lorsque le dépôt cible dispose déjà d’une couche de composants clairement définie. Il peut alors utiliser automatiquement vos composants et votre système de design existants au lieu de les recréer de toutes pièces.

Si nécessaire, par exemple si vous n’utilisez pas une stack standard, indiquez à Codex quelles primitives réutiliser, où se trouvent vos tokens et quelles implémentations font référence dans le dépôt pour les boutons, les champs de saisie, les cartes, la typographie et les icônes.

Si vous partez d’une base de code existante, Codex comprendra probablement de lui-même comment utiliser vos composants et votre système de design. En revanche, si vous partez de zéro, mieux vaut être explicite.

Demandez à Codex d’utiliser les captures d’écran comme cible visuelle, tout en la transposant dans les utilitaires, les wrappers de composants, le système de couleurs, l’échelle typographique, les tokens d’espacement et les conventions de routage, de gestion de l’état et de récupération des données propres au projet.

## Tirez parti de Playwright

Playwright est un excellent outil pour aider Codex à affiner l’interface par itérations. Il permet à Codex d’ouvrir l’application dans un vrai navigateur, de comparer l’implémentation aux captures d’écran fournies, puis d’ajuster la mise en page ou le comportement.

Codex peut redimensionner la fenêtre du navigateur afin de vérifier la mise en page pour différentes tailles d’écran et à différents points de rupture.

Vérifiez que la skill interactive Playwright est activée dans Codex. Pour en savoir plus, consultez la [documentation sur les Skills](/fr-FR/docs/build-skills).

## Procédez par itérations

La première itération devrait déjà être globalement proche des captures d’écran. Pour les mises en page ou les interactions complexes, ainsi que pour les interfaces riches en animations, prévoyez quelques cycles d’ajustement.

Demandez à Codex de comparer l’implémentation aux captures d’écran, pas seulement de vérifier que la page se compile. En cas de conflit, il doit privilégier les tokens du système de design du dépôt et limiter les ajustements d’espacement ou de dimensions au strict nécessaire pour préserver l’apparence générale du design.

Utilisez des captures d’écran supplémentaires ou de courtes notes si cela permet de clarifier des états qui ne ressortent pas clairement d’une seule image.

### Suggestion de prompt de suivi
