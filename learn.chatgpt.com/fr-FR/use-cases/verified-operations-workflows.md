<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/verified-operations-workflows -->

## Exécutez des opérations auditables

Si vous devez exécuter régulièrement des opérations reproductibles, comme accorder un accès à un utilisateur, appliquer une mise à jour par lots ou appeler un script avec différents paramètres, vous pouvez utiliser ChatGPT pour les automatiser et obtenir un résultat auditable.

Utilisez ce flux de travail lorsque ChatGPT doit exécuter une opération reproductible et vous montrer ce qui s’est passé en produisant un artefact faisant office de preuve.

## Décrivez la tâche et les entrées

1. Fournissez à ChatGPT les éléments sur lesquels il doit exécuter le processus par lots, qu’il s’agisse d’un tableau d’entrées, de fichiers, de tickets ou d’une autre liste.
2. Le cas échéant, indiquez-lui la source de l’approbation ou la politique qui définit le périmètre autorisé.
3. Indiquez à ChatGPT le script, l’API, le skill, la CLI ou le flux de travail d’une application à utiliser pour effectuer l’opération.
4. Si le flux de travail le permet, demandez au besoin une exécution à blanc.
5. Demandez à ChatGPT d’exécuter l’opération par lots et de consigner, pour chaque élément, une ligne indiquant la réussite ou l’échec.

Limitez le périmètre et demandez à ChatGPT de n’exécuter l’opération que lorsqu’il dispose de toutes les entrées requises.
Si un champ obligatoire manque dans une ligne, ChatGPT doit signaler cette ligne plutôt que de deviner.

Connectez les outils que vous utilisez pour exécuter l’opération au moyen de [plugins](/fr-FR/codex/plugins), par exemple votre système de gestion des tickets ou la feuille de calcul contenant la liste des éléments.

## Exigez une preuve permettant de vérifier le résultat

Pour être utile, l’exécution d’une opération doit fournir un résultat que vous ou un membre de votre équipe pouvez examiner, par exemple un fichier CSV, un fichier journal, un lien vers un tableau de bord, une capture d’écran, une vérification de PR ou toute autre preuve que l’opération a réussi. Après l’exécution, vous pouvez [ouvrir et examiner les fichiers générés](/fr-FR/codex/artifacts-viewer) dans l’application de bureau ChatGPT afin de vérifier le résultat.

## Transformez l’exécution en un flux de travail réutilisable

Après la première exécution réussie, demandez à ChatGPT de consigner les éléments reproductibles. Pour les flux de travail courants, ces éléments peuvent servir à créer un [skill](/fr-FR/codex/build-skills) ou une [tâche planifiée](/fr-FR/codex/automations).

Pour les opérations planifiées, ne créez une tâche planifiée qu’après avoir obtenu un résultat fiable lors d’une exécution manuelle. Maintenez à l’état de brouillon les actions sensibles susceptibles de modifier durablement les accès ou les données, sauf si vous souhaitez explicitement que ChatGPT les exécute.
