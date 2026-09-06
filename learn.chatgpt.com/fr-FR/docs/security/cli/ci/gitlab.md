<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/cli/ci/gitlab -->

Exécutez Codex Security dans GitLab CI/CD pour analyser les modifications enregistrées dans les commits et les branches
protégées, publier les résultats dans GitLab Security et, si vous le souhaitez, proposer des correctifs
vérifiés dans des brouillons de merge requests.

Le workflow sépare les identifiants utilisés pour l’analyse de l’accès en écriture au dépôt.
Les modifications générées nécessitent toujours une révision humaine avant leur fusion.

Commencez par produire uniquement des rapports d’analyse. N’activez la remédiation qu’après avoir vérifié le
runner, les résultats et le cloisonnement des identifiants de votre projet.

## Avant de commencer

Vous avez besoin des éléments suivants :

- Un projet GitLab avec un runner de confiance qui prend en charge l’espace de noms
utilisateur du bac à sable Codex.
- Le rôle Maintainer ou Owner dans le projet GitLab pour pouvoir configurer
[les variables CI/CD du projet](https://docs.gitlab.com/ci/variables/) et les ressources
  protégées.
- Une clé API OpenAI donnant accès à Codex Security. Les organisations utilisant des clés API de la plateforme
  peuvent [demander Trusted Access for
  Cyber](https://openai.com/form/enterprise-trusted-access-for-cyber/).
  Les particuliers qui s’authentifient avec ChatGPT peuvent suivre la [procédure Trusted Access
  pour les particuliers](https://chatgpt.com/cyber). Certains comptes ou dépôts nécessitent cet
  accès pour les analyses du dépôt entier.
- GitLab Ultimate 19.2 ou version ultérieure pour [l’ingestion de rapports
  SARIF 2.1.0](https://docs.gitlab.com/user/application_security/detect/sarif/).
- L’historique Git complet pour que les jobs de merge request puissent calculer la base de fusion.

L’image du pipeline installe Node.js 26, Python 3, Git, `rg` et la version fixée de la
CLI Codex Security. La remédiation automatisée nécessite également un test de non-régression
existant et un runner capable d’exécuter les commandes définies dans le dépôt
sans identifiants protégés.

## Commencez par un pipeline d’analyse uniquement

Créez une variable CI/CD GitLab masquée, cachée et protégée nommée
`CODEX_SECURITY_API_KEY`. Utilisez une clé API de la plateforme OpenAI donnant accès à Codex Security
et limitez sa portée à l’environnement `codex-security/openai`. Consultez
[les variables CI/CD limitées à un environnement](https://docs.gitlab.com/ci/environments/#limit-the-environment-scope-of-a-cicd-variable).

Ajoutez d’abord ce pipeline minimal à un projet de test. Il analyse les modifications enregistrées dans les commits
des merge requests protégées admissibles, publie le rapport SARIF depuis un job de rapport terminé avec succès
et rétablit le résultat de l’analyse dans une étape de contrôle distincte :

```yaml
stages:
  - security_scan
  - security_gate

.codex-security-merge-request:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID && $CI_MERGE_REQUEST_SOURCE_BRANCH_PROTECTED == "true" && $CI_MERGE_REQUEST_TARGET_BRANCH_PROTECTED == "true"'

codex-security:
  extends: .codex-security-merge-request
  stage: security_scan
  image: node:26-bookworm-slim
  environment:
    name: codex-security/openai
    action: access
  variables:
    GIT_DEPTH: "0"
  before_script:
    - npm install --prefix /tmp/codex-security-cli --ignore-scripts --no-audit --no-fund @openai/codex-security@0.1.20
  script:
    - |
      set -eu
      test -n "${CODEX_SECURITY_API_KEY:-}"

      CODEX_SECURITY_BIN="/tmp/codex-security-cli/node_modules/.bin/codex-security"
      RESULTS_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      ARTIFACT_DIR="codex-security-artifacts"
      BASE_REVISION="$(git merge-base \
        "$CI_MERGE_REQUEST_DIFF_BASE_SHA" "$CI_COMMIT_SHA")"
      install -d -m 700 "$RESULTS_DIR" "$ARTIFACT_DIR/results"

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY
      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          --diff "$BASE_REVISION" \
          --head "$CI_COMMIT_SHA" \
          --auth api-key \
          --output-dir "$RESULTS_DIR" \
          --json
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      case "$scan_exit" in
        0|1|2) ;;
        *) exit "$scan_exit" ;;
      esac

      "$CODEX_SECURITY_BIN" export "$RESULTS_DIR" \
        --export-format sarif \
        --source-root "$CI_PROJECT_DIR" \
        --output "$ARTIFACT_DIR/results.sarif"
      test -s "$ARTIFACT_DIR/results.sarif"
      cp -R "$RESULTS_DIR"/. "$ARTIFACT_DIR/results/"
      printf '%s\n' "$scan_exit" > "$ARTIFACT_DIR/scan-exit-code.txt"
      exit 0
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/results.sarif

codex-security-gate:
  extends: .codex-security-merge-request
  stage: security_gate
  image: alpine:3.20
  needs:
    - job: codex-security
      artifacts: true
  script:
    - exit "$(cat codex-security-artifacts/scan-exit-code.txt)"

  

Examinez chaque modification de `.gitlab-ci.yml` avant d’exécuter un job ayant accès à des secrets.
L’exemple minimal omet volontairement les analyses complètes et la remédiation.

## Adoptez le pipeline de production

1. [Téléchargez le pipeline GitLab complet](/codex/security/cli/ci/gitlab.yml)
   et enregistrez-le sous le nom `.gitlab-ci.yml` à la racine du dépôt. Si votre dépôt
   dispose déjà d’un pipeline, intégrez les étapes, les modèles cachés et
   les jobs de l’exemple au fichier existant.
2. Conservez les étapes existantes de build, de test et de déploiement. Si le projet utilise
`workflow: rules`, vérifiez que cette configuration autorise les événements de pipeline pour lesquels vous souhaitez
   lancer une analyse.

L’exemple ajoute les étapes `security_scan`, `security_remediation`, `security_publish`
et `security_gate`. La production de rapports d’analyse uniquement ne nécessite que
`CODEX_SECURITY_API_KEY`.

Par défaut, le job d’analyse s’exécute uniquement pour les merge requests entre branches
protégées d’un même projet. Définissez `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH=true` pour lancer des analyses
lors des pushs sur la branche par défaut protégée et dans les pipelines manuels. Définissez
`CODEX_SECURITY_SCHEDULED_DEEP_SCAN=true` et configurez des budgets explicites de temps et de coût
pour activer les analyses approfondies planifiées sur la branche par défaut protégée.

Un pipeline de merge request ne peut accéder aux variables et aux runners protégés que si les conditions suivantes sont réunies :

- Vous avez protégé les branches source et cible au sein du même projet.
- Le projet [autorise les pipelines de merge request à accéder aux variables et
  aux runners protégés](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners).
- L’utilisateur qui lance le pipeline peut pousser des commits dans la branche cible ou y fusionner des modifications.

Les pipelines des dépôts forkés et les merge requests non protégées ne reçoivent pas l’identifiant
d’authentification utilisé pour l’analyse. Examinez chaque modification de `.gitlab-ci.yml` avant d’exécuter un
job ayant accès à des secrets. Masquer et cacher une variable ne rend pas sûr
un code CI non fiable.

## Lancez une analyse et examinez les résultats

Créez une merge request protégée admissible ou lancez le pipeline sur la
branche par défaut protégée. Commencez par un petit diff avant de lancer une analyse payante
du dépôt entier.

Ouvrez le job `codex-security` et vérifiez que ses artefacts comprennent :

- `scan-manifest.json`
- `findings.json`
- `coverage.json`
- `results.sarif`
- `scan-exit-code.txt`

Ouvrez ensuite l’onglet **Sécurité** du pipeline, examinez les avertissements d’ingestion et vérifiez
les identifiants des résultats, les niveaux de gravité et les emplacements dans le code source. Les analyses de la branche par défaut
créent également des fiches de vulnérabilité dans le projet. Les résultats des merge requests apparaissent dans
l’onglet Sécurité du pipeline ou dans le widget de sécurité de la merge request, mais ne créent pas
de fiches de vulnérabilité à l’échelle du projet.

Restreignez l’accès aux artefacts, car les résultats d’analyse peuvent contenir des extraits de code source
vulnérable, des éléments de preuve et des détails de remédiation.

## Choisissez un profil d’analyse

Le pipeline sélectionne un profil en fonction du déclencheur :

| Déclencheur                                        | Cible          | Mode       | Effort  |
| ---------------------------------------------- | --------------- | ---------- | ------- |
| Merge request protégée au sein du même projet           | Diff entre commits  | `standard` | `low`   |
| Push ou exécution manuelle sur la branche par défaut protégée, après activation explicite | Dépôt entier | `standard` | `high`  |
| Exécution planifiée sur la branche par défaut protégée, après activation explicite    | Dépôt entier | `deep`     | `xhigh` |

Les analyses de merge requests concentrent les retours sur la modification enregistrée dans les commits.
Les analyses de la branche par défaut examinent le dépôt après intégration des modifications. Les analyses approfondies planifiées
assurent une couverture périodique plus large. Une analyse de diff terminée ne porte que sur la
modification concernée et ne prouve pas que le dépôt entier est exempt de problèmes.

Le workflow installe la CLI en dehors du dépôt et l’exécute à l’aide d’un chemin
absolu. Sa vérification préalable en mode simulation utilise la clé API limitée au processus, mais ne lance pas
d’analyse payante et ne vérifie ni l’authentification à l’API, ni l’accès à Codex Security, ni le quota, ni la disponibilité
des modèles.

Le workflow écrit l’état et les résultats de l’analyse en dehors de l’arbre de travail et limite
`OPENAI_API_KEY` au processus d’analyse. La CLI reçoit un environnement minimal, explicitement
défini, au lieu d’hériter de toutes les variables GitLab. Pour les analyses de diff, le
workflow calcule la base de fusion et lie l’analyse aux révisions de base et
de tête qui ont été examinées.

L’exemple fixe `@openai/codex-security` à la version `0.1.20`. Testez à nouveau l’authentification,
les artefacts, l’ingestion SARIF et le contrôle de la politique avant de modifier cette version.

## Séparez la publication des rapports de l’application de la politique

GitLab ingère le rapport SARIF d’un job de rapport terminé avec succès. Le pipeline publie d’abord le
rapport, puis rétablit le code de sortie de l’analyseur dans un job distinct
nommé `codex-security-gate`.

Le job de rapport accepte les résultats associés aux codes de sortie `0` et `1`. Il n’accepte le code de sortie
`2` que si le manifeste d’analyse prouve que l’analyse est terminée, si la couverture est
explicitement indiquée comme `partial` et si un rapport SARIF non vide existe. Les autres échecs d’exécution,
de configuration ou d’export restent bloquants.

L’étape de contrôle finale conserve les codes de sortie suivants de l’analyseur :

| Code de sortie | Signification                                                                     |
| ---- | --------------------------------------------------------------------------- |
| `0`  | L’analyse s’est terminée avec une couverture complète et son résultat respecte la politique définie.            |
| `1`  | L’analyse s’est terminée et a détecté un problème dont la gravité atteint ou dépasse le seuil configuré. |
| `2`  | La couverture de l’analyse était incomplète, ou une erreur d’entrée ou d’exécution s’est produite.              |

L’exemple autorise temporairement le code de sortie `2` pendant que vous ajustez la gestion de la couverture partielle.
Supprimez cette exception lorsque toute couverture incomplète doit bloquer le pipeline.

La correction et la publication s’exécutent avant le contrôle final de conformité à la politique. Un problème détecté répondant aux critères
peut donner lieu à une merge request en brouillon avec un correctif vérifié, même si ce contrôle fait ensuite
échouer le pipeline.

## Activez les corrections vérifiées

La correction automatique est facultative et ne s’exécute que dans les pipelines de la branche par défaut protégée.
Le processus de correction de Codex et les commandes de vérification contrôlées par le dépôt
ne reçoivent ni le token d’accès au projet GitLab ni les identifiants
injectés par le runner.

Le contrat de sécurité comporte trois volets : les commandes contrôlées par le dépôt ne reçoivent jamais
d’identifiants OpenAI ou GitLab, seul le job de publication reçoit
un accès en écriture au dépôt, et chaque modification générée reste à l’état de brouillon jusqu’à ce
qu’une personne l’examine et la fusionne.

Le workflow :

1. Exige une couverture complète de l’analyse et un problème détecté
   de gravité `high` ou `critical`.
2. Confirme que le test de non-régression configuré échoue avant l’application du correctif.
3. Génère un correctif ciblé et rejette les modifications des fichiers de CI, des fichiers d’identifiants, des fichiers binaires ou
d’autres fichiers protégés.
4. Exécute le test de non-régression sans identifiants OpenAI, GitLab, de registre ou de déploiement,
ni token de job.
5. Utilise `verify-fix` pour renvoyer `fixed`, `still_vulnerable` ou `inconclusive`.
   Le job ne publie un correctif que si `verify-fix` renvoie `fixed` et que le
   processus de vérification laisse le correctif inchangé.

Définissez ces variables protégées pour activer la correction :

- Définissez `CODEX_SECURITY_ENABLE_REMEDIATION` sur `true`.
- Définissez `CODEX_SECURITY_VERIFICATION_COMMAND` sur un test de non-régression existant qui
  se termine avec le code `1` avant la correction et `0` après.
- Si vous le souhaitez, définissez `CODEX_SECURITY_SETUP_COMMAND` sur une commande non interactive
  de configuration des dépendances.

Choisissez un test de non-régression qui vérifie l’invariant de sécurité sous-jacent, et non
une implémentation particulière. Examinez avec la même rigueur les modifications générées dans les tests et
le code source.

<details>
  <summary>Avancé : isolation des commandes du dépôt</summary>

Les commandes `validate`, `patch` et `verify-fix` reçoivent une clé
`CODEX_API_KEY` dont la portée est limitée au processus. Les commandes de configuration et de test contrôlées par le dépôt s’exécutent sous
un utilisateur distinct sans privilèges, dans une copie accessible en écriture des fichiers source suivis.
Cette copie exclut volontairement les métadonnées Git, le contenu des sous-modules et
les artefacts téléchargés. Les commandes de configuration et de test qui nécessitent `.git` ou
des sous-modules doivent s’exécuter dans un job conçu séparément et dépourvu d’identifiants.

Seules les étapes Codex appartenant à root peuvent accéder à la copie de travail de référence ou au
répertoire adjacent des variables de type fichier de GitLab. L’environnement épuré de la copie ne contient que
`PATH`, `HOME`, `LANG`, `CI` et `CI_PROJECT_DIR`. Si une commande nécessite une autre
valeur non secrète, ajoutez-la à la liste d’autorisation après avoir examiné la commande. Si votre
runner ne peut pas changer d’utilisateur, déplacez la vérification dans un job distinct dépourvu
d’identifiants avant d’activer la correction.

</details>

## Publiez une merge request en brouillon

Créez un [token d’accès à un projet
GitLab](https://docs.gitlab.com/user/project/settings/project_access_tokens/#create-a-project-access-token)
avec le rôle Développeur et les portées `api` et `write_repository`. Enregistrez-le dans
une variable `GITLAB_REMEDIATION_TOKEN` protégée, masquée et cachée, dont la portée est limitée à
l’environnement `codex-security/publish`.

Définissez `CODEX_SECURITY_CREATE_MR=true` pour activer la publication. Définissez également la variable non secrète
`CODEX_SECURITY_MR_TEST_COMMAND` sur le test de non-régression de sécurité propre au projet
que chaque branche de correction générée doit réussir. Laissez cette variable
non protégée afin que la merge request non protégée générée puisse lire la commande.
Le workflow de publication :

- Reçoit le token d’écriture dans le dépôt, mais aucun identifiant OpenAI.
- Crée une branche `codex-security/fix-<finding-hash>`.
- Ouvre une merge request en brouillon et réutilise un brouillon déjà ouvert au lieu de
créer un doublon.
- Exécute le test de non-régression de la branche de correction non protégée sous un utilisateur sans privilèges,
dans une copie contenant uniquement les fichiers suivis, sans identifiants protégés.
- Ne fusionne jamais automatiquement la modification générée.

N’utilisez pas `CI_JOB_TOKEN` à la place du token d’accès au projet. Il ne permet pas d’effectuer
l’opération de création de merge request requise. Examinez le correctif proposé,
les preuves de vérification et le problème détecté avant de fusionner.

## Configurez les variables facultatives

Configurez uniquement les variables nécessaires aux fonctionnalités que vous activez :

| Variable                                  | Nécessaire pour                       | Valeur par défaut ou usage                                          |
| ----------------------------------------- | --------------------------------- | ----------------------------------------------------------- |
| `CODEX_SECURITY_API_KEY`                  | Chaque analyse                        | Protégée, masquée et cachée ; limitez sa portée à `codex-security/openai` |
| `CODEX_SECURITY_VERSION`                  | Mise à niveau de la CLI                       | Version épinglée à `0.1.20` ; refaites les tests avant de la modifier                  |
| `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` | Analyses complètes de la branche par défaut         | Activation explicite requise ; désactivée par défaut                             |
| `CODEX_SECURITY_SCHEDULED_DEEP_SCAN`      | Analyses approfondies planifiées              | Activation explicite requise ; désactivée par défaut                             |
| `CODEX_SECURITY_DEEP_MAX_TIME_HOURS`      | Analyses approfondies planifiées              | Budget de temps obligatoire, supérieur à `0` et inférieur à `8`     |
| `CODEX_SECURITY_DEEP_MAX_COST`            | Analyses approfondies planifiées              | Limite obligatoire du coût estimé en USD, supérieure à `0`      |
| `CODEX_SECURITY_ENABLE_REMEDIATION`       | Génération de correctifs                  | Activation explicite par variable protégée ; désactivée par défaut                            |
| `CODEX_SECURITY_VERIFICATION_COMMAND`     | Génération de correctifs                  | Test de non-régression protégé                                   |
| `CODEX_SECURITY_SETUP_COMMAND`            | Configuration facultative pour la correction        | Installation protégée des dépendances                           |
| `CODEX_SECURITY_REMEDIATION_EFFORT`       | Réglages facultatifs de la correction       | `high`                                                      |
| `CODEX_SECURITY_MAX_CHANGED_FILES`        | Limite facultative de la taille des correctifs         | `8` ; plage autorisée de `1` à `20`                         |
| `CODEX_SECURITY_CREATE_MR`                | Création de merge requests en brouillon      | Activation explicite par variable protégée ; désactivée par défaut                            |
| `GITLAB_REMEDIATION_TOKEN`                | Création de merge requests en brouillon      | Token de projet avec le rôle Développeur, dont la portée est limitée à `codex-security/publish`  |
| `CODEX_SECURITY_GITLAB_INTERNAL_URL`      | Publication facultative sur une instance autohébergée   | Origine GitLab accessible depuis le runner                     |
| `CODEX_SECURITY_MR_TEST_COMMAND`          | Publication de merge requests en brouillon    | Test de non-régression obligatoire, non secret et propre au projet       |
| `CODEX_SECURITY_MR_SETUP_COMMAND`         | Configuration facultative de la branche de correction | Configuration des dépendances sans secret                                 |

GitLab fournit les variables `CI_*`. Le pipeline gère
`CODEX_SECURITY_BIN`, `CODEX_SECURITY_EFFORT`, `CODEX_SECURITY_MODE`,
`CODEX_SECURITY_STATE_DIR` et `CODEX_SECURITY_TARGET` ; ne les configurez pas
comme variables de projet. Pour les analyses de diff, la CLI déduit l’identité canonique de la cible
à partir des révisions de base et de tête normalisées.

## Ajustez les règles de blocage et les coûts

Utilisez des analyses ciblées de diff pour obtenir des retours sur les merge requests, des analyses standard du dépôt
pour la branche par défaut, et des analyses approfondies planifiées pour étendre la couverture. Les deux
profils d’analyse du dépôt complet sont désactivés par défaut. Une analyse approfondie planifiée nécessite aussi
`CODEX_SECURITY_DEEP_MAX_TIME_HOURS` et `CODEX_SECURITY_DEEP_MAX_COST` ; maintenez le
temps alloué à la CLI en dessous du délai d’expiration de huit heures du job. Mesurez des exécutions représentatives
avant de fixer un budget. Considérez `--max-cost` comme un garde-fou fondé sur une estimation du coût, et non
comme un plafond de facturation strict.

Commencez par des analyses qui produisent uniquement un rapport. Ajoutez `--fail-on-severity` une fois que votre équipe a
examiné des résultats représentatifs, la couverture, le coût et le temps d’exécution. Consultez [Exécutez Codex Security
en CI](/fr-FR/codex/security/cli/ci) pour en savoir plus sur les règles de gravité et les codes
de sortie.

Lorsqu’un job échoue :

- L’absence d’artefacts d’analyse indique un problème de configuration ou de runner.
- Si des artefacts sont présents mais que la couverture est partielle, examinez `coverage.json`.
- Si les résultats n’apparaissent pas dans GitLab, vérifiez que le job de rapport SARIF
s’est terminé avec succès et que GitLab a accepté le rapport.
- Si la correction n’est pas exécutée, vérifiez la protection de la branche, l’exhaustivité de la couverture,
la gravité des problèmes détectés, la commande de vérification et les variables d’activation.
- En cas d’erreur de publication, vérifiez le rôle du token de projet, ses portées
et sa restriction à un environnement.

Pour connaître toutes les commandes, options et tous les artefacts, consultez la [référence de la
CLI Codex Security](/fr-FR/codex/security/cli/reference).
