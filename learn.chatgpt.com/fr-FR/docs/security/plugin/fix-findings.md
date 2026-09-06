<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/plugin/fix-findings -->

Utilisez Codex Security pour transformer un constat de sécurité accepté en correctif ciblé
et vérifié. Vous pouvez travailler dans l’espace de travail de sécurité ou exécuter le workflow de remédiation
via un prompt, la ligne de commande ou CI/CD. Codex valide le problème
et, lorsque les tests sont sans risque et réalisables, ajoute un test de non-régression ciblé qui
échoue avant la correction et réussit après celle-ci. Il vérifie également que le comportement légitime
est préservé. Si un test de non-régression présente des risques ou n’est pas réalisable, Codex
consigne les éléments de preuve manquants et fournit à la place l’artefact de validation reproductible
le plus probant.

Commencez par un seul constat accepté, puis examinez le correctif proposé et les preuves de vérification
associées. Si le workflow répond à vos critères, traitez les autres constats acceptés
un par un, chacun dans une tâche Codex ou un job CI/CD distinct. En limitant le périmètre de chaque tâche,
vous facilitez la revue des modifications de code et des preuves associées.

## Corrigez un constat dans l’interface

Ouvrez un constat accepté depuis **Constats** ou depuis une analyse terminée dans **Analyses**.
Examinez ses éléments de preuve, puis utilisez **Correctif** pour générer, examiner, appliquer et vérifier
une correction ciblée.

1. Générez un correctif ciblé

   Ouvrez le constat, sélectionnez l’onglet **Correctif**, puis **Générer le correctif**.
   Lorsque c’est possible, Codex valide ou reproduit le problème et génère le correctif
   sous forme d’artefact sans modifier la copie de travail sélectionnée.

2. Examinez le diff proposé

   Examinez chaque fichier source modifié, chaque test de non-régression et chaque artefact de validation. Refusez
les refactorisations de grande ampleur, les nettoyages sans rapport ou les modifications qui affaiblissent un autre contrôle
de sécurité.

3. Appliquez le correctif en local

   Sélectionnez **Appliquer le correctif** uniquement lorsque le diff est acceptable. Codex applique
   le correctif généré tel quel à l’arbre de travail et consigne cet état. Examinez
   le diff de l’arbre de travail avant de continuer.

4. Vérifiez la correction

   Sélectionnez **Vérifier la correction**. Codex exécute à nouveau le cas de reproduction d’origine ou le test d’exploitation le plus probant
   disponible. Si un test de non-régression est sans risque et réalisable, Codex
   vérifie qu’il échoue avant la correction et réussit après celle-ci. Si le test
   présente des risques ou n’est pas réalisable, Codex consigne les éléments de preuve manquants et fournit
   à la place l’artefact de validation reproductible le plus probant. Il vérifie également
   le comportement légitime, les contournements similaires et les tests pertinents du dépôt.

5. Clôturez le constat en connaissance de cause

   La vérification ne clôture pas automatiquement un constat. Examinez les commandes,
les résultats et les éléments de preuve encore manquants, puis clôturez le constat en indiquant un motif
précis, ou laissez-le ouvert pour poursuivre le travail.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Examinez la correction de sécurité générée avant de l’appliquer à votre copie de travail.
  </figcaption>
</figure>

## Corrigez un constat depuis la CLI

Utilisez la CLI Codex pour un constat accepté provenant d’une analyse, d’un ticket, d’un avis de sécurité,
d’un signalement, d’une évaluation de sécurité ou d’une revue interne.

Installez Codex Security dans le `CODEX_HOME` utilisé par `codex exec` avant d’exécuter
ces commandes. Un runner CI vierge n’inclut pas les plugins du Marketplace par
défaut.

```text
Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.

Fournissez les éléments connus : la source, le puits, l’entrée contrôlée par l’attaquant, l’impact, l’invariant attendu,
le cas de reproduction, les fichiers concernés et la commande de validation. Codex peut inspecter le
dépôt pour retrouver les détails techniques manquants. Il doit demander confirmation plutôt que de supposer
quelle est la politique du produit ou l’invariant de sécurité visé.

Pour une exécution automatisée, récupérez le code, mettez le rapport du constat à disposition,
puis installez le plugin dans le `CODEX_HOME` du runner. Activez ensuite l’accès en écriture à l’espace de travail
et transmettez le prompt à `codex exec` :

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

## Analysez et corrigez les constats en CI/CD

Installez Codex Security dans le `CODEX_HOME` du runner avant d’appeler l’un ou l’autre
skill. Les commandes ci-dessous utilisent le plugin installé ; elles ne l’installent pas.

En CI/CD, séparez l’analyse des modifications de la remédiation et exigez que l’analyse
ne modifie pas la copie de travail. Conservez le répertoire de l’analyse terminée comme artefact
de job, examinez les constats et lancez une tâche ou un job Codex distinct pour chaque
constat dont la remédiation a été acceptée.

Par défaut, `codex exec` utilise un bac à sable en lecture seule. Exécutez l’analyse des modifications et la
remédiation avec `--sandbox workspace-write`. L’analyse a besoin de cette autorisation
pour enregistrer des artefacts temporaires, mais son prompt doit toujours contenir l’instruction `Do not modify
the checkout`. La remédiation a besoin de la même autorisation pour écrire le correctif
ciblé et les preuves de vérification. Consultez [Autorisations et
sécurité](/fr-FR/codex/non-interactive-mode#permissions-and-safety).

Pour chaque analyse et chaque constat accepté :

1. Déterminez les révisions de base et de tête de la modification.
2. Exécutez `$codex-security:security-diff-scan` sur ce diff sans modifier
   la copie de travail.
3. Conservez l’intégralité du répertoire de l’analyse et sélectionnez les constats à corriger.
4. Appelez `$codex-security:fix-finding` une fois pour chaque constat accepté, en lui transmettant
   l’ID du constat et le répertoire de l’analyse terminée.
5. Générez un seul correctif ciblé et ajoutez un test de non-régression qui échoue avant la
correction et réussit après celle-ci. Si ce test présente des risques ou n’est pas réalisable, consignez les
éléments de preuve manquants et utilisez à la place l’artefact de validation reproductible le plus probant.
6. Vérifiez le problème d’origine et le comportement légitime. Fournissez séparément chaque correctif, test
ou artefact de validation de substitution, ainsi que la commande de vérification et tout élément de preuve
manquant.

Commencez par analyser la modification sans modifier la copie de travail :

```bash
codex exec --sandbox workspace-write 'Use $codex-security:security-diff-scan to review changes from <base-revision> to <head-revision> for security regressions. Do not modify the checkout.'

Corrigez ensuite un constat accepté issu de l’analyse terminée :

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <completed-scan-directory>. Validate the finding, generate one minimal patch, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

Répétez la deuxième commande dans une tâche ou un job indépendant pour chaque autre
constat accepté. Après vérification, fusionnez chaque correctif en suivant votre processus habituel de
revue de code et de publication. Pour transmettre les constats à une autre équipe avant leur
remédiation, consultez [Exporter ou suivre
les constats](/fr-FR/codex/security/plugin/export-findings).
