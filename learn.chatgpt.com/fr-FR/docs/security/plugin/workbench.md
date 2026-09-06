<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/plugin/workbench -->

L’atelier de Codex Security regroupe vos analyses, les problèmes qu’elles détectent et vos dépôts
dans l’application de bureau Codex. Codex effectue chaque analyse dans une tâche standard, tandis que
l’atelier conserve l’analyse et ses résultats pour que vous puissiez les retrouver à votre retour.

Dans l’application de bureau ChatGPT, ouvrez le menu déroulant ChatGPT et sélectionnez **Codex**.
Installez et activez le [Plugin Codex Security](/fr-FR/codex/security/plugin), puis
sélectionnez **Sécurité** dans la barre latérale.

  Si **Sécurité** ne s’affiche pas, vérifiez que **Codex** est sélectionné et que le
  plugin est installé et activé. Si nécessaire, mettez à jour l’application de bureau et le plugin,
  puis vérifiez que l’administrateur de votre espace de travail autorise ce plugin.

## Lancer une analyse

Pour obtenir la meilleure qualité d’analyse, utilisez <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
avec un effort de raisonnement `xhigh`.

1. Ouvrez **Analyses** et sélectionnez **+ Analyse**.
2. Sélectionnez un dépôt existant ou choisissez un autre dossier.
3. Choisissez **Base de code** pour analyser un dépôt ou **Modifications** pour examiner une
   modification versionnée avec Git.
4. Pour une analyse standard de la base de code, sélectionnez l’intégralité du dépôt ou un dossier.
5. Pour une analyse approfondie, commencez par sélectionner le dépôt ou le dossier en tant que base de code, puis
   activez **Analyse approfondie**. Les analyses approfondies examinent l’intégralité de la base de code sélectionnée.
6. Pour analyser des modifications, sélectionnez les modifications non commitées, un commit ou une plage de
   révisions. L’option **Analyse approfondie** n’est pas disponible pour les analyses de modifications.
7. Choisissez un modèle et un effort de raisonnement. Ouvrez **Contexte supplémentaire** pour décrire
   les vecteurs d’attaque pertinents, les points à cibler ou tout autre élément de contexte lié à la sécurité.
8. Sélectionnez **Lancer l’analyse**.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Choisissez un dépôt et configurez une analyse dans l’atelier de Codex Security.
  </figcaption>
</figure>

Consultez [Lancez une analyse de sécurité](/fr-FR/codex/security/plugin/scans), [Lancez une analyse de sécurité
approfondie](/fr-FR/codex/security/plugin/deep-scans) ou [Examinez les modifications du code pour détecter les problèmes de
sécurité](/fr-FR/codex/security/plugin/code-changes) pour en savoir plus sur chaque type
d’analyse.

## Suivre la progression d’une analyse

La page de l’analyse affiche la phase en cours et la progression signalée par le plugin.
Pour une analyse standard, les phases comprennent la modélisation des menaces, la découverte, la validation,
l’analyse de l’impact et des chemins d’attaque, la création du rapport et la finalisation.

Sélectionnez **Voir l’activité** pour ouvrir la tâche Codex qui exécute l’analyse. Vous pouvez
quitter l’atelier et revenir dans **Analyses** sans perdre une analyse enregistrée. Pour arrêter
volontairement l’analyse, ouvrez-la et sélectionnez **Arrêter l’analyse**.

Une fois l’analyse terminée, ouvrez ses résultats pour examiner la cible, la révision,
les problèmes détectés, la couverture et les artefacts de rapport disponibles.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Examinez les problèmes détectés, leur niveau de gravité, la couverture de l’analyse et ses artefacts une fois celle-ci
terminée.
  </figcaption>
</figure>

## Examiner les problèmes détectés dans plusieurs analyses

Ouvrez **Résultats** pour examiner les problèmes enregistrés dans différents dépôts et analyses.
Effectuez une recherche dans la liste ou filtrez-la, puis sélectionnez un problème pour examiner son résumé, les éléments de preuve
provenant du code source, sa validation et son impact.

Utilisez **Résumé** pour consulter les détails du problème et **Patch** lorsque vous souhaitez générer,
examiner, appliquer ou vérifier un correctif ciblé. Consultez [Corriger et vérifier les problèmes de
sécurité](/fr-FR/codex/security/plugin/fix-findings) pour découvrir le workflow de remédiation.

  L’onglet **Résultats** affiche les problèmes détectés lors des analyses Codex Security enregistrées. Les tickets importés
  et les autres problèmes de sécurité existants continuent d’être traités séparément dans le
[workflow de triage du backlog](/fr-FR/codex/security/plugin/triage-backlog).

## Consulter l’historique d’un dépôt

Ouvrez **Dépôts** pour parcourir les dépôts et dossiers disponibles. Sélectionnez un
dépôt pour consulter l’historique de ses analyses, la dernière révision analysée et les
problèmes détectés encore ouverts. Depuis la page de détails du dépôt, ouvrez une analyse précédente ou consultez les problèmes
détectés associés à ce dépôt.

Si un dépôt n’a encore fait l’objet d’aucune analyse, lancez-en une depuis sa page de détails ou sélectionnez **+ Analyse**
dans l’atelier.

## Lancer une analyse depuis une conversation

Vous pouvez également demander à Codex d’exécuter le Plugin Codex Security installé dans une
conversation classique. Les analyses qui utilisent l’atelier partagé du plugin apparaissent dans **Analyses**,
ce qui vous permet de consulter à nouveau leur progression et leurs résultats depuis l’atelier de Codex Security.

Pour les analyses depuis le terminal et l’automatisation, consultez le [Démarrage rapide de la CLI
Codex Security](/fr-FR/codex/security/cli).
