<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/plugin/code-changes -->

Lancez une révision de sécurité pour détecter les régressions dans un seul ensemble de modifications suivi par Git.
Codex examine chaque fichier modifié de type code source ainsi que le code qui le prend directement en charge.
Cette révision ne s’étend pas à un audit complet du dépôt.

Pour analyser un dépôt entier plutôt qu’une modification précise, consultez [Lancer une analyse
de sécurité](/fr-FR/codex/security/plugin/scans).

## Effectuez une révision manuelle

Dans l’application de bureau, ouvrez **Sécurité**, sélectionnez **Analyses**, puis **+ Analyse**.
Choisissez le dépôt, puis sélectionnez **Modifications**. Examinez les modifications non validées,
un seul commit ou une révision de base et une révision de tête. L’option **Analyse approfondie** n’est pas disponible pour une
analyse des modifications.

Vous pouvez également demander à Codex d’examiner les modifications non validées dans une discussion :

```text
Use $codex-security:security-diff-scan to review my current uncommitted changes for security regressions.

Pour une plage de commits ou de branches, indiquez les deux révisions si nécessaire :

```text
Use $codex-security:security-diff-scan to review the changes from origin/main to HEAD for security regressions. Focus on authentication, authorization, input handling, filesystem access, network requests, and secrets.

Vous pouvez également indiquer une pull request lorsque ses révisions de base et de tête sont disponibles
dans la copie de travail locale.

## Confirmez la modification dans la configuration

1. Sélectionnez **Modifications**.
2. Vérifiez le dépôt extrait, la branche actuelle et le dernier commit.
3. Sous **Modifications à réviser**, choisissez :
   - `Uncommitted changes` pour l’arbre de travail actuel.
   - Le dernier commit pour une révision portant sur un seul commit.
   - Une révision de base et une révision de tête pour une plage correspondant à une branche ou à une pull request.
4. Vérifiez que le résumé décrit bien la modification que vous souhaitiez examiner.
5. Sélectionnez **Lancer l’analyse**.

Codex ne bascule pas sur une autre branche et ne change pas l’arbre de travail sélectionné. Si
une révision demandée n’est pas disponible localement, récupérez-la avant la révision ou
indiquez des révisions de base et de tête disponibles localement.

## Traitez les constats

Après avoir examiné les résultats, [corrigez et vérifiez un constat
accepté](/fr-FR/codex/security/plugin/fix-findings) ou [exportez et suivez
les constats](/fr-FR/codex/security/plugin/export-findings).

## Automatisez les révisions en CI/CD

Si vous avez accès à la CLI autonome en version bêta, consultez [Exécuter Codex Security en
CI](/fr-FR/codex/security/cli/ci) pour obtenir des données JSON structurées, une politique de niveaux de gravité et le téléversement
SARIF. Poursuivez avec cette section pour appeler la skill du plugin installé
via `codex exec`.

Exécutez `$codex-security:security-diff-scan` en CI lorsque le runner peut appeler
Codex CLI sans interaction. Commencez par installer la CLI sans exposer l’identifiant utilisé pour
l’analyse :

```bash
npm install --global @openai/codex

Installez le Plugin Codex Security dans la CLI :

```bash
codex plugin add codex-security@openai-curated

La commande d’installation utilise la Marketplace publique des plugins Codex CLI. Consultez le
[journal des modifications du plugin](/fr-FR/codex/security/plugin/changelog) avant de vous appuyer sur une
version ou une fonctionnalité précise du plugin en CI.

Ensuite, placez une clé API OpenAI provenant du stockage de secrets de votre CI dans la variable
`CODEX_SECURITY_API_KEY`. N’exposez cet identifiant que pendant l’analyse :

```bash
CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
  --sandbox workspace-write \
  "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

Le bac à sable accessible en écriture permet à l’analyse de créer des artefacts temporaires. Le prompt
exige toujours que Codex laisse la copie de travail du code source inchangée.

L’analyse enregistre sa sortie dans
`$TMPDIR/codex-security-scans/<repository>/<scan-id>/` :

| Fichier                 | Contenu                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `report.md`          | Point d’entrée principal lisible vers le répertoire complet de l’analyse.                                                                                              |
| `findings/<slug>/`   | Rapports détaillés sur les vulnérabilités et fichiers de preuve de concept associés, sur demande.                                                                     |
| `hardening/`         | Recommandations de renforcement structurel et propositions associées, sur demande.                                                                                   |
| `findings.json`      | Constats comportant des identifiants stables, un niveau de gravité, un niveau de confiance, des emplacements dans le code source et des mesures correctives. Alimentez des flux de travail de sécurité internes approuvés ou des outils en aval. |
| `scan-manifest.json` | Reçu d’analyse scellé comprenant la cible examinée, les révisions et les hachages des artefacts.                                                                             |
| `coverage.json`      | Surfaces examinées et reportées, exclusions et exhaustivité de la couverture.                                                                                    |

Le [schéma `findings.json`](https://github.com/openai/plugins/blob/main/plugins/codex-security/schemas/findings.schema.json)
définit la structure complète. Il comprend les champs suivants :

| Champ                     | Type   | Description                                                            |
| ------------------------- | ------ | ---------------------------------------------------------------------- |
| `documentType`            | Chaîne | Identifie le document comme `codex-security.findings`.                  |
| `schemaVersion`           | Chaîne | Identifie la version du schéma des constats.                                |
| `scanId`                  | Chaîne | Identifie l’analyse qui a produit les constats.                        |
| `findings`                | Tableau  | Contient zéro ou plusieurs objets représentant des constats.                                 |
| `findings[].findingId`    | Chaîne | Identifiant stable d’un constat, dérivé de son empreinte.        |
| `findings[].occurrenceId` | Chaîne | Identifie cette occurrence du constat dans une analyse donnée.          |
| `findings[].ruleId`       | Chaîne | Identifie la famille de vulnérabilités.                                   |
| `findings[].identity`     | Objet | Contient l’ancre sémantique et l’identifiant facultatif de l’instance sœur. |
| `findings[].fingerprints` | Objet | Contient l’algorithme d’empreinte et l’empreinte principale.            |
| `findings[].title`        | Chaîne | Indique le titre court du constat.                                      |
| `findings[].summary`      | Chaîne | Résume la vulnérabilité et son impact.                           |
| `findings[].severity`     | Objet | Contient le niveau de gravité et des informations facultatives sur le score.              |
| `findings[].confidence`   | Objet | Contient le niveau de confiance et sa justification.                           |
| `findings[].taxonomy`     | Objet | Contient la catégorie de vulnérabilité et les identifiants CWE.               |
| `findings[].locations`    | Tableau  | Répertorie les fichiers concernés, les numéros de ligne et le rôle de chaque emplacement.                |
| `findings[].remediation`  | Chaîne | Décrit le correctif recommandé.                                         |
| `findings[].provenance`   | Objet | Identifie la source du constat.                                  |

Par exemple, cette commande affiche, pour chaque constat, une ligne dont les champs sont séparés par des tabulations :

```bash
jq -r '
  .findings[] |
  [.findingId, .severity.level, .confidence.level, .locations[0].path, .locations[0].startLine, .title] |
  @tsv
' findings.json

Ces exemples supposent l’utilisation d’un runner Linux de confiance disposant de Node.js et de `npm`, de Git, de Python
3, de `jq` et des outils en ligne de commande du fournisseur. Le préfixe global des packages `npm`
doit être accessible en écriture.

Choisissez l’exemple correspondant à votre fournisseur de CI :

Les résultats de l’analyse peuvent inclure des informations sensibles sur les vulnérabilités. Gardez les artefacts
confidentiels et ne publiez les constats qu’après avoir vérifié les destinataires, le contenu et
les approbations requises.

  <div slot="github">

```yaml
name: Codex Security review

on:
  pull_request:

jobs:
  security-review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Install Codex Security
        env:
          CODEX_HOME: ${{ runner.temp }}/codex-home
        run: |
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated

      - name: Review code changes
        env:
          CODEX_SECURITY_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_HOME: ${{ runner.temp }}/codex-home
          TMPDIR: ${{ runner.temp }}/codex-security
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_REVISION: ${{ github.event.pull_request.head.sha }}
        run: |
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_REVISION")"
          CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
            --sandbox workspace-write \
            "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: codex-security-review
          path: ${{ runner.temp }}/codex-security/codex-security-scans

  </div>

  <div slot="gitlab">

Créez une variable CI/CD `CODEX_SECURITY_API_KEY` masquée et examinez les artefacts de l’analyse
en privé avant de partager les constats.

```yaml
codex-security-review:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
  variables:
    GIT_DEPTH: "0"
  script:
    - |
      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
      CODEX_API_KEY="$codex_security_api_key" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
  after_script:
    - |
      unset CODEX_SECURITY_API_KEY
      scan_root="/tmp/codex-security-$CI_JOB_ID/codex-security-scans"
      if [ -d "$scan_root" ]; then
        tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
      fi
  artifacts:
    when: always
    paths:
      - codex-security-artifacts.tar.gz

  </div>

  <div slot="azure">

```yaml
trigger: none

pool:
  vmImage: ubuntu-latest

steps:
  - checkout: self
    fetchDepth: 0

  - bash: |
      set -euo pipefail

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
    displayName: Install Codex Security

  - bash: |
      set -euo pipefail

      CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
    displayName: Review code changes
    condition: and(succeeded(), ne(variables['System.PullRequest.IsFork'], 'True'))
    env:
      CODEX_SECURITY_API_KEY: $(CODEX_SECURITY_API_KEY)

  - publish: $(Agent.TempDirectory)/codex-security/codex-security-scans
    artifact: codex-security-review
    condition: always()

Pour Azure Repos, configurez une stratégie de branche **Validation de build** afin d’exécuter le
pipeline sur les pull requests.

  </div>

  <div slot="jenkins">

```groovy
pipeline {
  agent { label 'linux' }
  stages {
    stage('Codex Security review') {
      when {
        allOf {
          changeRequest()
          expression { !env.CHANGE_FORK?.trim() }
        }
      }
      steps {
        sh '''#!/usr/bin/env bash
          set -euo pipefail

          mkdir -p "$TMPDIR"
          git fetch --no-tags origin "$CHANGE_TARGET"
          target="$(git rev-parse FETCH_HEAD)"
          git fetch --no-tags origin "$CHANGE_BRANCH"
          git rev-parse FETCH_HEAD > "$TMPDIR/head"
          git merge-base "$target" "$(cat "$TMPDIR/head")" > "$TMPDIR/base"
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated
        '''
        withCredentials([string(credentialsId: 'codex-security-api-key', variable: 'CODEX_SECURITY_API_KEY')]) {
          sh '''#!/usr/bin/env bash
            set +x
            set -euo pipefail

            CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
              --sandbox workspace-write \
              "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
          '''
        }
      }
      post {
        always {
          sh '''#!/usr/bin/env bash
            set -euo pipefail
            scan_root="/tmp/codex-security-$BUILD_TAG/codex-security-scans"
            if [ -d "$scan_root" ]; then
              tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
            fi
          '''
          archiveArtifacts artifacts: 'codex-security-artifacts.tar.gz', allowEmptyArchive: true
        }
      }
    }
  }
}

  </div>

Les exemples ignorent les pull requests provenant de forks. N’exécutez les jobs nécessitant des identifiants qu’à partir d’une
définition de pipeline protégée et uniquement pour des contributeurs de confiance autorisés à utiliser l’identifiant
de l’analyse. Archivez `codex-security-scans` afin de conserver ensemble les constats structurés,
le manifeste, la couverture et `report.md`, ainsi que les éventuelles sorties demandées
`findings/` ou `hardening/`. Commencez par utiliser les résultats à titre indicatif et vérifiez
la couverture et la durée d’exécution avant de faire de ce job une vérification obligatoire.

Pour la gestion des clés API et les contrôles du bac à sable, consultez [Mode
non interactif](/fr-FR/codex/non-interactive-mode). Si votre organisation autorise la [Codex
GitHub Action](/fr-FR/codex/github-action), celle-ci peut installer la CLI au moment de l’exécution, mais
vous devez tout de même commencer par installer le plugin et faire pointer l’entrée `codex-home`
de l’action vers le même `CODEX_HOME`.
