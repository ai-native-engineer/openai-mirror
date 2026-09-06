<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/plugin/deep-scans -->

Lancez une analyse approfondie lorsqu’un examen plus poussé est nécessaire et que vous pouvez accepter une durée
d’exécution plus longue. Les analyses approfondies explorent un dépôt plus en profondeur et peuvent réduire
la variabilité entre les exécutions.

Commencez par une [analyse standard](/fr-FR/codex/security/plugin/scans) pour vérifier votre périmètre
et vos résultats. Utilisez ensuite une analyse approfondie lorsqu’une évaluation plus poussée est nécessaire.

## Choisissez entre l’analyse standard et l’analyse approfondie

|                         | Analyse standard                                      | Analyse approfondie                                             |
| ----------------------- | -------------------------------------------------- | ----------------------------------------------------- |
| Idéal pour                | Premières exécutions et examen régulier d’un dépôt ou d’un dossier | Examens plus approfondis après une analyse standard           |
| Variabilité             | Standard                                           | Réduite                                               |
| Périmètre                   | Dépôt ou dossier explicitement indiqué                      | Dépôt ou dossier explicitement indiqué                         |
| Besoins en temps et en ressources   | Plus faibles                                              | Plus élevés                                                |
| Pull requests et diffs | Utilisez le workflow de revue des modifications                     | Non pris en charge ; utilisez plutôt le workflow de revue des modifications |

## Configurez les paramètres d’exécution des analyses approfondies

Pour contrôler le parallélisme et la durée d’une analyse approfondie, créez ou modifiez
`~/.codex/codex-security/config.toml`. Si vous définissez `CODEX_HOME`, utilisez plutôt
`$CODEX_HOME/codex-security/config.toml`.

Par exemple, ce profil exécute une analyse plus courte avec un parallélisme limité :

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

| Paramètre                         | Valeur par défaut | Description                                                                                                        |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| `workers`                       | `4`     | Nombre de workers d’analyse standard indépendants pouvant s’exécuter simultanément. L’ancienne valeur `"auto"` correspond également à `4`. |
| `subagents`                     | `3`     | Nombre de sous-agents que chaque worker peut lancer. Définissez ce paramètre sur `0` pour les désactiver.                                                |
| `stop_after_no_new`             | `4`     | Arrêtez l’analyse après ce nombre d’analyses consécutives menées à terme par les workers sans nouveau constat.                                   |
| `stop_after_consecutive_errors` | `3`     | Arrêtez l’analyse après ce nombre d’erreurs consécutives des workers.                                                                    |
| `max_discovery_runs`            | `40`    | Limitez le nombre d’exécutions indépendantes d’analyses standard avant l’agrégation.                                             |
| `max_time_hours`                | `96`    | Limitez l’exécution des workers à un nombre d’heures strictement positif ne dépassant pas `96` ; utilisez des fractions si nécessaire.                          |

Des valeurs plus faibles peuvent réduire la durée de l’analyse et la consommation de tokens, mais certains constats peuvent passer inaperçus.
Les modifications de configuration s’appliquent aux nouvelles analyses approfondies, et non à celles déjà en cours.

Lorsque la durée limite est atteinte, Codex Security interrompt les workers encore en cours, conserve
les résultats des analyses terminées et les agrège dans le rapport final. Si aucun worker
ne termine l’examen du code source avant l’échéance, le rapport indique une couverture
partielle.

Le paramètre `max_time_hours` nécessite la version `0.1.19` ou une version ultérieure du plugin. Consultez le
[journal des modifications du plugin](/fr-FR/codex/security/plugin/changelog) pour connaître les détails de la version.

## Lancez l’analyse approfondie

Dans l’application de bureau, ouvrez **Sécurité**, sélectionnez **Analyses**, puis sélectionnez **+ Analyse**.
Choisissez un dépôt ou un autre dossier, sélectionnez **Code source**, puis activez
**Analyse approfondie**. L’analyse porte sur l’intégralité du dépôt ou du dossier sélectionné.

Vous pouvez également lancer une analyse approfondie de l’ensemble d’un dépôt depuis une conversation Codex :

```text
Use $codex-security:deep-security-scan to run a deep security scan of this repository.

Pour un seul composant d’un monorepo, indiquez explicitement le dossier :

```text
Use $codex-security:deep-security-scan to run a deep security scan of /absolute/path/to/repository/services/payments.

Pour limiter le périmètre d’une analyse approfondie dans l’application de bureau, sélectionnez le dossier comme code source.
L’analyse porte sur l’intégralité du dossier sélectionné.

## Vérifiez la configuration et effectuez les contrôles préalables

Pour une qualité d’analyse optimale, utilisez <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
avec un effort de raisonnement de niveau `xhigh`.

1. Sélectionnez **Code source** et activez **Analyse approfondie**.
2. Vérifiez que le dépôt ou le dossier sélectionné contient bien le code que vous souhaitiez
analyser.
3. Choisissez un modèle et un niveau d’effort de raisonnement.
4. Ouvrez **Contexte supplémentaire** pour indiquer des vecteurs d’attaque concrets, les zones sensibles
   de l’application ou des éléments de contexte sur le dépôt que le code seul ne peut pas révéler.
5. Sélectionnez **Démarrer l’analyse**.

Les workers d’analyse approfondie héritent du modèle et des paramètres de raisonnement que vous avez sélectionnés. Chaque
worker exécute une analyse standard complète, et Codex Security agrège les
résultats des analyses terminées. Suivez l’analyse enregistrée dans **Analyses** ou sélectionnez **Afficher
l’activité** pour examiner la tâche Codex correspondante. Consultez le [journal des modifications
du plugin](/fr-FR/codex/security/plugin/changelog) avant de mettre à jour le plugin ou de
lancer une analyse de longue durée.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Suivez la phase en cours de l’analyse approfondie et inspectez son activité Codex avant
d’examiner le résultat final.
  </figcaption>
</figure>

## Examinez le résultat

Les analyses approfondies utilisent les mêmes informations d’analyse enregistrées et le même répertoire d’analyse complet que les analyses
standard. Ouvrez l’analyse terminée dans **Analyses** ou examinez ses constats dans
**Constats**. Le fichier `report.md` généré renvoie vers des rapports détaillés sur les vulnérabilités
ou des recommandations de renforcement structurel lorsque vous demandez ces résultats.
Conservez avec le rapport tous les répertoires `findings/` et `hardening/` associés lorsque vous
partagez ou archivez le résultat.

Consultez le résumé de la couverture avant d’examiner les constats. Même une analyse approfondie a ses limites ;
vérifiez donc les surfaces dont l’examen a été reporté et les preuves encore manquantes avant de tirer une
conclusion. Si vous acceptez un constat, reportez-vous à [Corrigez et vérifiez un
constat](/fr-FR/codex/security/plugin/fix-findings).

Pour examiner une pull request, un commit, une plage de branches ou un patch local, utilisez [la revue des modifications
du code](/fr-FR/codex/security/plugin/code-changes). Une analyse approfondie ne remplace jamais
le workflow centré sur les diffs.
