<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/scan-code-changes-for-security -->

## Examinez la modification plutôt que l’ensemble du dépôt

Utilisez une analyse de sécurité du diff lorsqu’une pull request, un commit, une branche ou un patch local
modifie un chemin de code sensible. Le Plugin Codex Security s’appuie sur le contexte du dépôt
pour comprendre la modification, puis concentre la détection et la validation des problèmes de sécurité
sur le diff et le code dont celui-ci dépend directement.

Ce flux de travail complète la revue de code habituelle. Utilisez-le lorsque vous avez besoin d’éléments probants
sur des régressions de sécurité, et non d’une revue générale du style du code ou des tests.

## Effectuez une analyse ciblée

1. Ouvrez le dépôt, puis effectuez le checkout de l’ensemble exact de modifications Git à examiner, ou décrivez-le.
2. Terminez le [Démarrage rapide du Plugin Codex Security](/fr-FR/codex/security/plugin) et précisez dans le prompt de démarrage la pull request, le commit, le diff de branche ou le patch de l’arbre de travail.
3. Précisez les surfaces à haut risque concernées par la modification, comme l’authentification, les analyseurs syntaxiques, les chemins de fichiers, les requêtes réseau ou la gestion des informations d’identification.
4. Exécutez le prompt sans demander de correctif, afin que le premier résultat reste un artefact de revue.
5. Vérifiez chaque ligne signalée comme concernée, chaque résultat de validation et chaque manque de preuves mentionné avant de décider s’il faut apporter une correction.

## Donnez suite à un constat

Un rapport utile distingue un constat de sécurité étayé par des preuves et associé à un chemin d’attaque viable d’un
soupçon qui reste à confirmer. Il peut aussi inclure des commentaires de code en ligne
sur les lignes concernées. Pour disposer d’un résultat exploitable, ouvrez une nouvelle tâche de correction bien délimitée
en indiquant l’identifiant du constat ou la section pertinente du rapport.
Consultez [Corriger un backlog de vulnérabilités](/fr-FR/codex/use-cases/remediate-vulnerability-backlog)
pour connaître le cycle de correction et de validation.

Pour les sélecteurs de modifications, le périmètre du diff et l’examen des résultats, consultez [Examiner les modifications de code
sous l’angle de la sécurité](/fr-FR/codex/security/plugin/code-changes).
