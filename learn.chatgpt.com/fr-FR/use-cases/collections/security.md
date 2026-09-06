<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/collections/security -->

# Sécurité

Codex peut aider les équipes d’ingénierie et de sécurité à évaluer le code qu’elles sont autorisées à analyser, à recueillir
des éléments probants et à transformer les constats révisés en correctifs ciblés. Ces cas d’utilisation couvrent
l’analyse des dépôts, la révision des modifications, les incidents liés aux dépendances et la correction
des vulnérabilités.

## Évaluer un dépôt

Utilisez le Plugin Codex Security pour effectuer une analyse complète d’un dépôt pour lequel vous disposez de l’autorisation requise,
réviser les constats jugés plausibles et produire des rapports qui facilitent le tri
manuel de ces constats. Les analyses complètes prennent plus de temps, car plusieurs
processus indépendants exécutent chacun la phase de découverte.

## Réviser les modifications avant leur fusion

Demandez à Codex d’inspecter une pull request, une branche, un commit ou le diff de l’arbre de travail pour y détecter
des régressions de sécurité et fournir des éléments probants liés au code modifié.

## Auditer les incidents liés aux dépendances

À partir d’un avis public relatif à un package ou à la chaîne d’approvisionnement, réalisez un audit en lecture seule d’un dépôt
portant sur les manifestes, les fichiers de verrouillage, les scripts, les flux de travail et les chemins d’exposition.

## Remédier aux constats révisés

Fournissez à Codex un constat approuvé issu d’un rapport de sécurité, d’un avis ou d’un ticket,
puis demandez-lui d’appliquer un correctif minimal et de vérifier que le comportement vulnérable n’est
plus reproductible.

- [Effectuez une analyse de sécurité approfondie](/fr-FR/use-cases/deep-security-scan)

- [Analyser les modifications de code pour détecter les problèmes de sécurité](/fr-FR/use-cases/scan-code-changes-for-security)

- [Auditer les incidents liés aux dépendances](/fr-FR/use-cases/dependency-incident-audits)

- [Résorber un backlog de vulnérabilités](/fr-FR/use-cases/remediate-vulnerability-backlog)
