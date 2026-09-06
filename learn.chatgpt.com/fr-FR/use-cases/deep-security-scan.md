<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/deep-security-scan -->

## Choisissez une revue approfondie du dépôt

Utilisez une analyse approfondie lorsque vous avez besoin d’une revue plus complète des vulnérabilités dans
un dépôt ou un dossier explicitement défini et que vous pouvez prévoir une exécution plus longue. Le plugin Codex
Security effectue plusieurs passes de détection avant de valider et de hiérarchiser les
constats. Ce workflow exige donc plus de temps et de ressources qu’une analyse standard.

Une analyse approfondie peut porter sur l’intégralité d’un dépôt ou sur un package ou un
répertoire explicitement désigné. Pour examiner une pull request, un commit, un diff de branche ou un patch de l’arbre de travail,
utilisez
[$codex-security:security-diff-scan](/fr-FR/codex/use-cases/scan-code-changes-for-security).

## Préparez une analyse autorisée

1. Ouvrez le dépôt dans Codex et suivez le [Démarrage rapide du plugin Codex Security](/fr-FR/codex/security/plugin).
2. Vérifiez que le dépôt vous appartient ou que vous avez l’autorisation de l’évaluer.
3. Ajoutez des consignes sur l’architecture, les frontières de confiance, les invariants de sécurité, les critères de signalement,
   les exclusions et les niveaux de gravité dans `SECURITY.md`. Utilisez des fichiers `SECURITY.md`
   imbriqués pour définir des règles propres à chaque répertoire.
4. Conservez les commandes prises en charge pour la compilation, les tests et la validation, ainsi que les autres
   instructions du dépôt, dans `AGENTS.md`.
5. Lancez le prompt de démarrage et laissez l’analyse mener à bien ses passes répétées de détection,
ses étapes de validation et d’analyse des chemins d’attaque, puis la production du rapport final.
6. Examinez l’espace de travail des constats, le rapport et les éventuelles lacunes dans les preuves. Demandez des rapports détaillés
sur les vulnérabilités ou des recommandations de durcissement structurel lorsque vous en avez besoin.

## Examinez les preuves avant toute correction

Le résultat final doit indiquer les emplacements concernés, expliquer pourquoi ce comportement peut être
déclenché, préciser les validations effectuées par Codex, signaler les lacunes qui subsistent dans les preuves et proposer une
piste de correction bien circonscrite. Distinguez les constats dépourvus de preuves de validation
des constats validés.

N’entamez la correction d’un constat qu’après l’avoir sélectionné et examiné. Utilisez
[Corriger un backlog de vulnérabilités](/fr-FR/codex/use-cases/remediate-vulnerability-backlog)
pour corriger les constats un par un en vérifiant de façon ciblée l’absence de régression.

Pour la configuration, les contrôles préalables, la définition du périmètre des cibles et ce à quoi vous attendre pendant l’exécution, consultez [Effectuer une analyse de
sécurité approfondie](/fr-FR/codex/security/plugin/deep-scans).
