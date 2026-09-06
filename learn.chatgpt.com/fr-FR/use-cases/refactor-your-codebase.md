<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/refactor-your-codebase -->

## Introduction

Lorsque votre base de code a accumulé du code inutilisé, de la logique dupliquée, des abstractions obsolètes, des fichiers volumineux ou des patterns hérités qui rendent chaque modification plus coûteuse qu’elle ne devrait l’être, vous devriez envisager de réduire cette dette technique par une refactorisation. La refactorisation vise à améliorer la structure du système existant sans pour autant en faire une migration de stack.

Codex est utile dans ce cas, car il peut d’abord cartographier la zone problématique, puis effectuer le nettoyage par petites étapes faciles à examiner : supprimer les chemins inutilisés, restructurer les modules volumineux, factoriser les chemins dupliqués, moderniser les anciens patterns de framework et renforcer les contrôles de validation associés à chaque étape.

L’objectif est d’améliorer directement la base de code existante :

1. Supprimez le code inutilisé, les fonctions utilitaires obsolètes, les anciens flags et les couches de compatibilité qui ne sont plus nécessaires.
2. Allégez les modules surchargés en extrayant des fonctions utilitaires, en scindant des composants ou en déplaçant les effets de bord vers des limites plus clairement définies.
3. Remplacez les patterns hérités par les conventions actuelles du dépôt : primitives plus récentes du framework, types plus clairs, flux d’état plus simple ou utilitaires de la bibliothèque standard.
4. Préservez la stabilité du comportement public tout en réduisant le coût de la prochaine modification.

## Utilisation

1. Demandez à Codex de cartographier la zone avant toute modification : les modules surchargés, la logique dupliquée, le code inutilisé, les tests, les contrats publics et tous les anciens patterns qui ne sont plus adaptés au dépôt.
2. Choisissez un seul axe de nettoyage à la fois : suppression du code inutilisé, simplification du flux de contrôle, modernisation d’un pattern obsolète ou scission d’un fichier volumineux en parties plus petites dont la responsabilité est clairement attribuée.
3. Avant que Codex n’apporte des modifications aux fichiers, demandez-lui d’indiquer le comportement actuel, l’amélioration structurelle envisagée et le contrôle minimal qui permettra de vérifier que le comportement est resté stable.
4. Après chaque étape, passez les modifications en revue et exécutez le contrôle minimal pertinent, plutôt que de regrouper tout le nettoyage dans un seul diff.
5. Traitez les changements de stack, les migrations de dépendances et les évolutions d’architecture comme des tâches distinctes, sauf s’ils sont nécessaires pour terminer le nettoyage.

  Vous pouvez utiliser le Mode plan pour créer un plan de refactorisation avant de commencer le
travail.

## Tirez parti des ExecPlans

Le [guide pratique de modernisation du code](/cookbook/examples/codex/code_modernization) présente les ExecPlans : des documents qui permettent à Codex de conserver une vue d’ensemble du nettoyage, de décrire précisément l’état final visé et de consigner les résultats de validation après chaque étape.
Ils sont utiles lorsque la refactorisation s’étend à plusieurs modules ou nécessite plusieurs sessions. Utilisez-les pour consigner les suppressions, les mises à jour de patterns, les contrats qui devaient rester stables et les éléments encore reportés.

## Utilisez les Skills pour les pratiques récurrentes

Les [Skills](/fr-FR/codex/build-skills) sont utiles lorsque les mêmes règles de nettoyage s’appliquent à plusieurs dépôts, services ou équipes. Utilisez des Skills spécifiques au framework lorsqu’ils sont disponibles, associez des Skills de sécurité et de CI aux nettoyages risqués et créez un Skill d’équipe lorsque vous disposez d’une liste de contrôle éprouvée pour la suppression du code inutilisé, l’extraction de modules ou la modernisation de patterns hérités.
Si vous en venez à appliquer la même étape de modernisation à plusieurs bases de code, Codex peut vous aider à transformer la première étape menée à bien en Skill réutilisable.
