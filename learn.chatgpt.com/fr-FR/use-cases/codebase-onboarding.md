<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/codebase-onboarding -->

## Introduction

Lorsque vous découvrez un dépôt ou devez intervenir sur une fonctionnalité que vous ne connaissez pas, Codex peut vous aider à vous repérer avant de commencer à modifier le code. L’objectif n’est pas seulement d’obtenir une vue d’ensemble, mais de cartographier le flux de la requête, de comprendre les responsabilités de chaque module et d’identifier les fichiers à lire ensuite.

## Comment l’utiliser

Si vous découvrez un projet, vous pouvez simplement commencer par demander à Codex de vous expliquer toute la base de code :

Si vous devez développer une nouvelle fonctionnalité dans une base de code existante, vous pouvez demander à Codex de vous expliquer une partie précise du système. Plus votre demande est ciblée, plus l’explication sera concrète :

1. Fournissez à Codex les fichiers et répertoires pertinents, ou indiquez-lui le domaine fonctionnel que vous cherchez à comprendre.
2. Demandez-lui de retracer le flux de la requête et d’expliquer quels modules prennent en charge la logique métier, le transport, la persistance ou l’interface utilisateur.
3. Avant de modifier quoi que ce soit, demandez-lui où interviennent la validation, les effets de bord ou les transitions d’état.
4. Pour finir, demandez-lui quels fichiers lire ensuite et quels sont les points à risque.

Pour être utile, une réponse de prise en main doit vous fournir une cartographie concrète, et pas seulement une liste de noms de fichiers. À la fin, Codex devrait avoir expliqué le flux principal, signalé les parties à risque et indiqué les prochains fichiers à lire ou les vérifications importantes avant de commencer les modifications.

## Questions à poser ensuite

Après la première analyse de Codex, continuez à l’interroger jusqu’à ce que son explication soit suffisamment précise pour que vous puissiez effectuer votre première modification en toute confiance. De bonnes questions de suivi l’amènent généralement à expliciter ses hypothèses, les dépendances cachées et les vérifications importantes après une modification.

- Quel module prend en charge la logique métier proprement dite, par opposition à la couche de transport ou à celle de l’interface utilisateur ?
- Où s’effectue la validation, et quelles hypothèses fait-elle respecter ?
- Quels fichiers connexes ou quelles tâches en arrière-plan peuvent facilement m’échapper si je modifie ce flux ?
- Quels tests ou quelles vérifications dois-je effectuer après avoir modifié cette partie du code ?
