<!-- source: https://learn.chatgpt.com/fr-FR/docs/permission-modes -->

{/* vale Microsoft.FirstPerson = NO */}

## Modes d’autorisation

Les autorisations déterminent comment ChatGPT (dans son application de bureau) et Codex (dans la CLI ou l’IDE) gèrent les actions locales, comme modifier des fichiers, exécuter des commandes et utiliser Internet. Le mode choisi délimite
ce que ChatGPT peut faire de manière autonome et ce qui doit faire l’objet d’une révision.

Pour la plupart des tâches, commencez par le mode **Demander l’approbation**. ChatGPT peut ainsi agir dans l’espace de travail
actuel et s’interrompt avant d’en franchir les limites.

Sélectionnez les différents modes ci-dessous pour comprendre le fonctionnement de chacun.

## Activation des modes

Lors de votre première utilisation de l’application de bureau ChatGPT, vous devez activer les modes dans les paramètres de l’application.

**Demander l’approbation** est toujours disponible. Pour ajouter **Approuver à ma place** (appelé
**Révision automatique** dans les paramètres) ou **Accès complet** au menu des autorisations, ouvrez
**Paramètres \> Général** dans l’application de bureau ChatGPT, puis activez le mode souhaité dans la section
**Autorisations**. L’activation d’un mode le rend disponible dans le menu ; elle ne
sélectionne pas ce mode et ne modifie aucune discussion existante.

  

  Les modes disponibles peuvent dépendre de votre configuration locale et des exigences de votre
organisation. Un mode non autorisé apparaît désactivé.

## Fonctionnement des autorisations

Deux mécanismes agissent conjointement :

- Le **bac à sable** détermine à quels fichiers et ressources réseau ChatGPT peut accéder.
- Les **approbations** déterminent dans quels cas ChatGPT s’interrompt avant d’effectuer une action ou soumet la
  demande à la révision automatique.

Changer la personne ou le système qui révise une demande n’étend pas le périmètre du bac à sable. Par exemple,
le mode **Approuver à ma place** conserve la même limite d’accès à l’espace de travail que le mode **Demander l’approbation** ;
il soumet à la révision automatique les demandes visant à franchir cette limite.

Utilisez le contrôle des autorisations situé sous la zone de saisie dans l’application de bureau ChatGPT ou
l’extension IDE.

Dans la CLI, saisissez `/permissions`. Pour plus de détails techniques, consultez la documentation sur
[le bac à sable](/fr-FR/codex/sandboxing), [la révision automatique](/fr-FR/codex/sandboxing/auto-review) ou
[les profils d’autorisation](/fr-FR/codex/permissions).
