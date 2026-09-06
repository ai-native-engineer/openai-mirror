<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/plugin -->

Codex Security analyse votre code à la recherche de vulnérabilités et valide les
constats plausibles. Pour chaque problème à signaler, il fournit les preuves et les recommandations de correction
nécessaires pour examiner le résultat. Analysez uniquement le code qui vous appartient ou que vous avez
l’autorisation d’évaluer.

Suivez ce guide de démarrage rapide pour installer le plugin et lancer une analyse standard en lecture seule
d’un dépôt local dans Codex.

  Cette page présente le plugin Codex Security dans l’application de bureau ou Codex CLI. Pour
  analyser un dépôt GitHub connecté dans Codex Cloud, consultez [la configuration de Codex Security
  dans le cloud](/fr-FR/codex/security/setup).

## Installez le plugin

1. Ouvrez [Codex dans l’application de bureau ChatGPT](/fr-FR/codex/app).
2. Ouvrez **Plugins**, recherchez **Codex Security** ou utilisez le bouton ci-dessous :

   <div className="not-prose my-6">
     
       Installer le plugin Codex Security
     
   </div>

3. Vérifiez que le plugin est activé, puis ouvrez **Sécurité** dans la barre latérale.

1. Dans votre terminal, accédez au dépôt que vous souhaitez évaluer et lancez Codex :

   ```bash
   codex

2. Saisissez `/plugins`, recherchez **Codex Security**, puis sélectionnez **Installer le
   plugin**.
3. Saisissez `/new` pour démarrer une nouvelle discussion consacrée au dépôt.

Pour installer Codex Security pour un dépôt local, utilisez l’application de bureau ChatGPT
ou Codex CLI.

  Consultez le [journal des modifications du plugin](/fr-FR/codex/security/plugin/changelog) avant de vous appuyer
  sur une fonctionnalité ou de lancer une analyse de longue durée. Si **Sécurité** n’apparaît pas
  dans la barre latérale de l’application de bureau, mettez à jour l’application et le plugin, puis vérifiez que le plugin
  est activé.

## Lancez votre première analyse

Pour une qualité d’analyse optimale, utilisez <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
avec un niveau d’effort de raisonnement `xhigh`.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Choisissez un dépôt et configurez une nouvelle analyse de sécurité avant de la lancer.
  </figcaption>
</figure>

1. Ouvrez la configuration de l’analyse

   Sélectionnez **Sécurité** dans la barre latérale, ouvrez **Analyses**, puis sélectionnez **+ Analyse**.

2. Choisissez la base de code et le périmètre de l’analyse

   Sélectionnez un dépôt existant ou utilisez un autre dossier. Choisissez **Base de code**,
   laissez l’option **Analyse approfondie** désactivée, puis sélectionnez l’intégralité du dépôt ou un seul dossier.
   Vérifiez que la branche et la révision correspondent bien au code que vous souhaitez analyser.

3. Ajoutez du contexte pertinent

   Choisissez le modèle et le niveau d’effort de raisonnement. Ouvrez **Contexte supplémentaire** uniquement lorsque
   vous devez décrire un vecteur d’attaque précis, une zone sensible sur le plan de la sécurité ou
   un détail concernant le dépôt qui doit orienter l’examen.

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       Activez le contexte supplémentaire pour décrire les vecteurs d’attaque, les zones à examiner et
les recommandations de sécurité pertinentes.
     </figcaption>
   </figure>

4. Lancez l’analyse

   Sélectionnez **Lancer l’analyse** et suivez les phases de l’analyse dans l’atelier de sécurité.
   Sélectionnez **Afficher l’activité** pour examiner la tâche Codex qui effectue l’analyse.

5. Examinez le résultat

   Ouvrez l’analyse terminée pour examiner les constats, la couverture et les fichiers de rapport
   disponibles. Utilisez **Constats** pour examiner les problèmes détectés dans les différentes analyses ou **Dépôts**
   pour consulter l’historique des analyses d’un dépôt.

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       Examinez les résultats, les constats et la couverture de l’analyse dans l’atelier de sécurité.
     </figcaption>
   </figure>

1. Demandez une analyse standard

   Envoyez ce prompt dans la nouvelle discussion :

   ```text
   Run a Codex Security scan on this repository.

2. Laissez l’analyse se terminer

   Codex exécute l’analyse dans le terminal sans ouvrir d’espace de travail de configuration. Laissez
la tâche s’exécuter jusqu’à ce que Codex indique qu’elle est terminée. Si Codex détecte
une limitation de configuration, examinez cette limitation et la modification exacte proposée
avant d’approuver une mise à jour de la configuration.

3. Examinez le résultat

   Examinez le résumé dans le terminal, puis ouvrez le fichier `report.md` généré pour
   consulter le résultat complet.

Exécutez ce workflow local du plugin dans l’application de bureau ChatGPT ou Codex CLI.

## Ce que génère l’analyse

Les analyses terminées restent disponibles dans **Analyses**. Examinez leurs constats et leur
couverture dans l’atelier de sécurité, ou consultez les constats associés et l’historique des dépôts
dans **Constats** et **Dépôts**. L’analyse génère également les fichiers
ci-dessous.

Chaque analyse terminée affiche un résumé dans le terminal et crée les fichiers
ci-dessous.

Exécutez ce workflow local du plugin dans l’application de bureau ChatGPT ou Codex CLI.

- `report.md`, le fichier principal pour consulter les résultats de l’analyse.
- `findings/<slug>/`, lorsque des rapports de vulnérabilité détaillés et des fichiers de preuve de concept
  associés sont disponibles.
- `hardening/`, lorsque des recommandations de renforcement structurel de la sécurité et des propositions ou
  schémas associés sont disponibles.
- Données d’analyse structurées dans `scan-manifest.json`, `findings.json` et
`coverage.json` pour l’automatisation et les intégrations. Vous pouvez consulter les résultats de l’analyse
  sans ouvrir ces fichiers.

Conservez le répertoire d’analyse dans son intégralité lorsque vous partagez ou archivez les résultats, afin que les
liens de `report.md` continuent de fonctionner.

## Choisissez votre prochain workflow

- [Utilisez l’atelier de sécurité](/fr-FR/codex/security/plugin/workbench) pour gérer
  les analyses enregistrées, les constats, les dépôts et l’activité d’analyse dans l’application de bureau.
- [Lancez une analyse depuis la CLI](/fr-FR/codex/security/cli) si vous disposez d’un accès bêta et
  avez besoin d’un workflow reproductible dans le terminal avec des résultats structurés.
- [Lancez une analyse standard ou ciblée](/fr-FR/codex/security/plugin/scans) pour examiner un
  dépôt ou un dossier avec le workflow par défaut.
- [Évaluez une première analyse](/fr-FR/codex/security/plugin/scans#assess-a-first-scan)
  pour comparer les résultats aux problèmes connus et décider quand relancer une analyse.
- [Lancez une analyse approfondie](/fr-FR/codex/security/plugin/deep-scans) pour réaliser une analyse plus complète
  si vous pouvez prévoir une durée d’exécution plus longue.
- [Examinez les modifications du code](/fr-FR/codex/security/plugin/code-changes) pour évaluer une pull request,
  un commit, les différences entre branches ou un patch de l’arbre de travail.
- [Triez un backlog](/fr-FR/codex/security/plugin/triage-backlog) pour examiner les constats de
  sécurité existants.
- [Corrigez et vérifiez un constat](/fr-FR/codex/security/plugin/fix-findings) après avoir
  accepté de le corriger.
- [Exportez ou suivez les constats](/fr-FR/codex/security/plugin/export-findings) pour créer
  des fichiers JSON, CSV ou SARIF, une issue Linear, GitHub ou Jira dont la création est soumise à approbation, ou un brouillon privé
  de GitHub Security Advisory.
- [Rédigez des rapports de vulnérabilité](/fr-FR/codex/security/plugin/vulnerability-reports)
  pour transformer les constats, les notes de divulgation, le code source et les PoCs fournis en
  rapports autonomes.
- [Proposez un renforcement de la sécurité](/fr-FR/codex/security/plugin/security-hardening) pour
  envisager des options structurelles ou architecturales à partir des résultats d’analyse ou d’autres
  éléments probants liés à la sécurité.
