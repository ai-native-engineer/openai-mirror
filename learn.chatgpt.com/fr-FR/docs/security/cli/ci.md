<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/cli/ci -->

Exécutez la CLI Codex Security en CI pour examiner précisément les modifications d’une pull request
ou d’une merge request, conserver les résultats et les informations de couverture, et éventuellement faire échouer la vérification
à partir d’un niveau de sévérité choisi. Commencez par des résultats informatifs, évaluez la qualité et la durée
d’exécution de l’analyse, puis ajoutez une politique de sévérité adaptée à votre dépôt.

  Installez le package public `@openai/codex-security`. L’exécution des analyses nécessite toujours
  un accès à Codex Security.

Ce guide contient des exemples pour GitHub Actions et GitLab CI/CD. Les mêmes commandes d’analyse
et d’exportation fonctionnent dans d’autres systèmes CI.

## Préparez le workflow

Enregistrez une clé d’API OpenAI dans le gestionnaire de secrets de votre fournisseur CI sous le nom
`CODEX_SECURITY_API_KEY`.

Associez directement ce secret à la variable d’environnement `OPENAI_API_KEY` de l’étape
d’analyse. Limitez l’accès à cet identifiant au processus d’analyse et utilisez
`--auth api-key` pour le sélectionner explicitement.

N’exécutez le workflow que pour les dépôts et les pull requests auxquels vous faites confiance. Les analyses utilisent
les autorisations locales du runner et ne s’interrompent pas pour demander une approbation. Les processus d’analyse
peuvent hériter de l’environnement du job : n’y incluez donc aucun token ni identifiant d’accès cloud
sans rapport avec l’analyse.

Le runner doit disposer des éléments suivants :

- Node.js 22 (22.13.0 ou une version ultérieure), 24 ou 26.
- Python 3.10 ou une version ultérieure.
- Le package publié `@openai/codex-security`, installé hors du répertoire
  dans lequel le dépôt est extrait.
- L’historique des révisions de tête et de base de la pull request ou de la merge request, afin que Git puisse calculer
la base de fusion.

## Ajoutez le workflow GitHub Actions

Pour les dépôts privés ou internes, activez
[GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)
avant de charger le rapport SARIF.

Créez `.github/workflows/codex-security.yml`. Avant d’extraire le contenu de la pull request,
installez `@openai/codex-security` dans
`$RUNNER_TEMP/codex-security`, afin que l’exécutable de confiance soit disponible à l’emplacement
`$RUNNER_TEMP/codex-security/node_modules/.bin/codex-security` :

```yaml
name: Codex Security scan

on:
  pull_request:

jobs:
  codex-security:
    if: github.event.pull_request.head.repo.full_name == github.repository && github.actor != 'dependabot[bot]'
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    steps:
      - name: Set up Node.js
        uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7
        with:
          node-version: "26"

      - name: Set up Python
        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7
        with:
          python-version: "3.14"

      - name: Install Codex Security
        run: |
          set -euo pipefail
          npm install \
            --prefix "$RUNNER_TEMP/codex-security" \
            --ignore-scripts \
            --no-audit \
            --no-fund \
            @openai/codex-security

      - name: Verify Codex Security
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
        run: |
          set -euo pipefail
          test -x "$CODEX_SECURITY_BIN"
          "$CODEX_SECURITY_BIN" --version

      - name: Check out the pull request
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Scan the pull request
        env:
          OPENAI_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          CODEX_SECURITY_STATE_DIR: ${{ runner.temp }}/codex-security-state
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
        run: |
          set -euo pipefail
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          "$CODEX_SECURITY_BIN" scan . \
            --diff "$BASE_REVISION" \
            --head "$HEAD_SHA" \
            --auth api-key \
            --output-dir "$SCAN_DIR" \
            --json > "$RUNNER_TEMP/codex-security.json"

      - name: Export SARIF
        id: export-sarif
        if: always()
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
          SARIF_FILE: ${{ runner.temp }}/codex-security.sarif
        run: |
          set -euo pipefail
          if test -f "$SCAN_DIR/scan-manifest.json"; then
            "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
              --export-format sarif \
              --source-root "$GITHUB_WORKSPACE" \
              --output "$SARIF_FILE"
            echo "available=true" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload SARIF
        if: always() && steps.export-sarif.outputs.available == 'true'
        uses: github/codeql-action/upload-sarif@e4fba868fa4b1b91e1fdab776edc8cfbe6e9fb81 # v4
        with:
          sarif_file: ${{ runner.temp }}/codex-security.sarif
          ref: refs/pull/${{ github.event.pull_request.number }}/head
          sha: ${{ github.event.pull_request.head.sha }}
          category: codex-security

      - name: Preserve scan results
        if: always()
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7
        with:
          name: codex-security-results
          path: |
            ${{ runner.temp }}/codex-security-results
            ${{ runner.temp }}/codex-security.json
          if-no-files-found: warn
          retention-days: 7

Le workflow extrait la révision de tête de la pull request, calcule sa base de fusion et
analyse les modifications enregistrées dans les commits entre ces révisions. L’historique complet garantit
un ciblage précis. `persist-credentials: false` empêche l’enregistrement du token du dépôt dans
la configuration Git de la copie de travail. Installer la CLI avant l’extraction et
l’exécuter au moyen de son chemin absolu empêche les exécutables contrôlés par le dépôt d’accéder
à l’identifiant d’accès de l’analyse. `--auth api-key` sélectionne explicitement la clé d’API réservée à l’analyse.
L’analyse enregistre son historique dans un répertoire d’état accessible en écriture, situé hors du
dépôt.

`--json` écrit un document JSON complet sur stdout, ce qui permet au workflow de l’enregistrer
directement. La progression, les récapitulatifs de fin d’exécution et les erreurs restent sur stderr. Ce comportement
diffère de celui de `codex exec --json`, qui émet un flux d’événements JSON Lines.

L’étape d’exportation lit une analyse terminée et scellée, puis génère un rapport SARIF. Elle ne modifie ni
l’environnement d’exécution de Codex ni les identifiants d’accès. Les artefacts d’analyse peuvent contenir des extraits de code source
vulnérable, des éléments de preuve et des détails sur les corrections à apporter. Choisissez des contrôles d’accès et une
courte durée de conservation adaptés à votre dépôt.

## Ajoutez le pipeline GitLab CI/CD

Pour un workflow de production avec des analyses protégées de la branche par défaut, des analyses approfondies planifiées
à activer explicitement, un contrôle distinct de la politique SARIF et, en option, des merge requests vérifiées
à l’état de brouillon, suivez le guide [Exécutez Codex Security dans GitLab
CI/CD](/fr-FR/codex/security/cli/ci/gitlab).

GitLab peut importer
[des rapports SARIF 2.1.0](https://docs.gitlab.com/ci/yaml/artifacts_reports/#artifactsreportssarif)
avec GitLab Ultimate 19.2 ou une version ultérieure. Avant d’exécuter le pipeline, ajoutez une variable CI/CD masquée et cachée nommée
`CODEX_SECURITY_API_KEY`.

L’exemple minimal suivant ajoute un job `security` consacré uniquement à l’analyse au fichier
`.gitlab-ci.yml` situé à la racine. Conservez les stages et les jobs déjà présents dans le fichier. Par défaut, il analyse
les modifications des merge requests. Définissez `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH`
sur `"true"` pour analyser également l’intégralité de la branche par défaut :

```yaml
variables:
  CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH: "false"

stages:
  - test
  - security

codex-security:
  stage: security
  image: node:26-bookworm-slim
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "diff"
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH && $CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH == "true"'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "full"
  variables:
    GIT_DEPTH: "0"
    CODEX_SECURITY_CLI_DIR: "/tmp/codex-security-cli"
  before_script:
    - |
      set -eu
      apt-get update -qq
      apt-get install -y -qq --no-install-recommends \
        ca-certificates \
        git \
        python3 \
        ripgrep
      npm install \
        --prefix "$CODEX_SECURITY_CLI_DIR" \
        --ignore-scripts \
        --no-audit \
        --no-fund \
        @openai/codex-security@0.1.20

      test -x "$CODEX_SECURITY_BIN"
      "$CODEX_SECURITY_BIN" --version
  script:
    - |
      set -eu
      if test -z "${CODEX_SECURITY_API_KEY:-}"; then
        echo "Set the CODEX_SECURITY_API_KEY CI/CD variable." >&2
        exit 2
      fi

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      case "${CODEX_SECURITY_SCAN_SCOPE:-}" in
        diff)
          BASE_SHA="$CI_MERGE_REQUEST_DIFF_BASE_SHA"
          HEAD_SHA="$CI_COMMIT_SHA"
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          set -- --diff "$BASE_REVISION" --head "$HEAD_SHA"
          echo "Scanning committed changes from $BASE_REVISION to $HEAD_SHA."
          ;;
        full)
          set -- --mode standard
          echo "Scanning the complete default branch at $CI_COMMIT_SHA."
          ;;
        *)
          echo "Unsupported Codex Security scan scope: ${CODEX_SECURITY_SCAN_SCOPE:-unset}" >&2
          exit 2
          ;;
      esac

      SCAN_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      JSON_FILE="/tmp/codex-security-$CI_JOB_ID.json"
      SARIF_FILE="/tmp/codex-security-$CI_JOB_ID.sarif"

      install -d -m 700 "$CODEX_SECURITY_STATE_DIR" "$SCAN_DIR"

      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          "$@" \
          --auth api-key \
          --output-dir "$SCAN_DIR" \
          --json > "$JSON_FILE"
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      install -d -m 700 codex-security-artifacts/results
      cp -R "$SCAN_DIR"/. codex-security-artifacts/results/
      if test -s "$JSON_FILE"; then
        cp "$JSON_FILE" codex-security-artifacts/codex-security.json
      fi
      printf '%s\n' "$scan_exit" > codex-security-artifacts/scan-exit-code.txt

      export_exit=0
      if test -f "$SCAN_DIR/scan-manifest.json"; then
        set +e
        "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
          --export-format sarif \
          --source-root "$CI_PROJECT_DIR" \
          --output "$SARIF_FILE"
        export_exit="$?"
        set -e
        if test -s "$SARIF_FILE"; then
          cp "$SARIF_FILE" codex-security-artifacts/codex-security.sarif
        fi
      fi

      if test "$scan_exit" -ne 0; then
        exit "$scan_exit"
      fi
      exit "$export_exit"
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/codex-security.sarif

Par défaut, le job ne s’exécute que pour les merge requests provenant de branches du même
projet. Ainsi, les pipelines des forks ne reçoivent pas l’identifiant d’accès de l’analyse. Définissez
`CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` sur `"true"` au niveau du groupe, du projet ou du
pipeline pour exécuter également une analyse complète standard de la branche par défaut. Les analyses
complètes prennent plus de temps et coûtent plus cher que les analyses différentielles.

`GIT_DEPTH: "0"` fournit l’historique nécessaire pour calculer la base de fusion à partir de
`CI_MERGE_REQUEST_DIFF_BASE_SHA` et `CI_COMMIT_SHA` lors des analyses de merge requests.

Le job installe la CLI dans `/tmp`, l’exécute au moyen de son chemin absolu et n’expose la
clé d’API qu’au processus d’analyse. `artifacts: when: always` conserve le rapport SARIF
en cas d’échec de l’analyse, tandis que `artifacts:access: maintainer` limite l’accès
aux résultats détaillés de l’analyse.

Les modifications apportées à `.gitlab-ci.yml` peuvent exposer des variables CI/CD. Examinez donc les modifications du pipeline
avant d’exécuter le job. Si vous
[protégez `CODEX_SECURITY_API_KEY`](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners),
GitLab ne rend cette variable disponible que pour les merge requests entre des branches
protégées d’un même projet, et uniquement si l’utilisateur peut accéder à la branche cible.

Le guide consacré à GitLab part de ce job minimal pour construire le workflow de production
dont le lien figure au début de cette section.

## Choisissez une politique de sévérité

Les deux exemples se limitent à produire un rapport, car ils omettent `--fail-on-severity`. Lorsque vous
souhaitez que les résultats déterminent l’issue de la vérification, ajoutez un seuil à la commande
d’analyse :

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --fail-on-severity high

Les seuils pris en charge sont `critical`, `high`, `medium` et `low`. Un
seuil inclut les résultats de l’analyse actuelle dont le niveau de sévérité est égal ou supérieur à ce seuil.
Les résultats antérieurs non résolus figurant dans le résumé du dépôt n’ont aucune incidence sur cette politique.

L’étape d’analyse utilise les codes de sortie suivants :

| Code de sortie  | Signification                                                                                 |
| ----- | --------------------------------------------------------------------------------------- |
| `0`   | L’analyse s’est terminée avec une couverture complète et, le cas échéant, la politique configurée a été respectée.            |
| `1`   | L’analyse terminée contient un résultat d’un niveau de sévérité égal ou supérieur au seuil.                        |
| `2`   | La CLI a détecté une erreur d’entrée ou d’exécution, ou l’analyse terminée présente une couverture incomplète. |
| `130` | Ctrl-C a interrompu l’analyse.                                                            |
| `143` | SIGTERM a mis fin à l’analyse.                                                            |

Une analyse dont la couverture est `partial` ou `unknown` renvoie `2`, même sans politique de
sévérité. La CLI enregistre tout de même les résultats disponibles et les informations de couverture. Examinez les
zones dont l’analyse a été reportée dans `coverage.json` avant de considérer la vérification comme concluante.

## Réessayez avec un répertoire de résultats existant

Utilisez un nouveau répertoire sur le runner pour chaque job CI. Si le runner est persistant ou auto-hébergé,
conservez un résultat antérieur avec `--archive-existing` :

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --archive-existing

La commande archive les résultats précédents et démarre avec un répertoire d’analyse vide.

## Résolvez les problèmes d’une analyse CI

- **Référence Git inconnue ou diff inattendu :** Récupérez l’historique des révisions de base et de tête,
  calculez la base de fusion et indiquez explicitement les deux révisions.
- **Répertoire de sortie protégé ou non vide :** Choisissez un répertoire privé
  hors de l’arbre de travail Git parent. Utilisez `--archive-existing` si le
  répertoire contient déjà des résultats.
- **Identifiants d’accès manquants :** Vérifiez que `CODEX_SECURITY_API_KEY` est disponible pour
  le workflow ou le pipeline de confiance et directement associé à la variable d’environnement
`OPENAI_API_KEY` du processus d’analyse.
- **Erreur d’historique de l’analyse :** Définissez `CODEX_SECURITY_STATE_DIR` sur un répertoire accessible en écriture
  situé hors du dépôt.
- **Erreur de configuration de Python :** Vérifiez que le runner utilise Python 3.10 ou une version ultérieure.
- **Couverture incomplète :** Examinez `coverage.json`, notamment les surfaces dont l’analyse a été reportée
  et les questions en suspens, puis relancez l’analyse avec une cible ou un environnement approprié.
- **Erreur d’exportation SARIF :** Vérifiez que l’analyse s’est terminée et que l’intégralité du répertoire
  d’analyse est disponible. L’exportation valide les artefacts scellés avant d’écrire
  le fichier SARIF.
- **Erreur de chargement SARIF :** Pour GitHub Actions, vérifiez que votre organisation
  a activé GitHub Code Security pour le dépôt et que le workflow accorde les autorisations
`actions: read`, `contents: read` et `security-events: write`. Pour GitLab
  CI/CD, vérifiez que le projet utilise GitLab Ultimate 19.2 ou une version ultérieure et que
  le job charge un fichier SARIF 2.1.0 au moyen de `artifacts:reports:sarif`.

Pour chaque commande, option, artefact et champ de sortie, consultez la [référence
de la CLI](/fr-FR/codex/security/cli/reference). Pour une revue interactive en CI
à l’aide d’un plugin, consultez [Examinez les modifications du code pour en vérifier la sécurité](/fr-FR/codex/security/plugin/code-changes#automate-reviews-in-cicd).
