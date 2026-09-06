<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/cli -->

Codex Security aide les équipes de sécurité et d’ingénierie à détecter, confirmer et corriger
les vulnérabilités. Utilisez son interface en ligne de commande (CLI) pour analyser
les dépôts qui vous appartiennent ou que vous avez l’autorisation d’évaluer, suivre les constats au fil du temps
et vérifier les modifications avant leur intégration.

  Le package `@openai/codex-security` est public. L’exécution d’analyses nécessite un accès à Codex
  Security. Pour effectuer une analyse interactive dans Codex, commencez par le [guide de démarrage rapide du plugin Codex
  Security](/fr-FR/codex/security/plugin). Pour les dépôts GitHub connectés,
  consultez la [configuration de Codex Security dans le cloud](/fr-FR/codex/security/setup).

## Vérifiez les prérequis

La CLI nécessite Node.js 22 (22.13.0 ou version ultérieure), 24 ou 26. Les analyses, les analyses par lots,
les exportations, l’historique des analyses et les constats enregistrés nécessitent également Python 3.10 ou une version ultérieure.
Pour en savoir plus, consultez [Authentification et
prérequis](/fr-FR/codex/security/cli/reference#authentication-and-prerequisites).

## Configurez et vérifiez la CLI

Exécutez la CLI avec `npx` et vérifiez sa version :

```bash
npx @openai/codex-security --version

Pour afficher à la fois la version du package et celle du plugin qu’il intègre, exécutez :

```bash
npx @openai/codex-security info --json

Consultez les [versions de la CLI et du SDK](https://github.com/openai/codex-security/releases)
pour connaître les modifications apportées au package.

Répertoriez les commandes disponibles :

```bash
npx @openai/codex-security --help

Consultez également la [référence de la CLI](/fr-FR/codex/security/cli/reference).

## Connectez-vous

Pour une utilisation locale, connectez-vous avec votre compte ChatGPT :

```bash
npx @openai/codex-security login

Sur une machine distante ou sans interface graphique, utilisez l’authentification par appareil :

```bash
npx @openai/codex-security login --device-auth

Pour la CI et les autres workflows automatisés, définissez une clé API OpenAI :

```bash

Pour les identifiants AWS, consultez la [configuration
d’Amazon Bedrock](/fr-FR/codex/security/cli/reference#use-amazon-bedrock). Pour [OpenRouter ou
Fireworks](/fr-FR/codex/security/cli/reference#use-openrouter-or-fireworks), définissez la
clé API du fournisseur et sélectionnez un modèle avec `--provider` et `--model`.

Pour utiliser votre connexion ChatGPT lorsqu’une clé API est également définie, sélectionnez-la explicitement :

```bash
npx @openai/codex-security scan . --auth chatgpt

Pour imposer l’utilisation de la clé API de l’environnement, sélectionnez l’authentification par clé API :

```bash
npx @openai/codex-security scan . --auth api-key

Selon votre compte et votre dépôt, les analyses portant sur l’intégralité du dépôt peuvent également
nécessiter [Trusted Access for Cyber](https://chatgpt.com/cyber).

## Préparez une analyse

Choisissez un dépôt auquel vous faites confiance et que vous avez l’autorisation d’évaluer. Les analyses utilisent les autorisations de votre
système d’exploitation local et ne s’interrompent pas pour demander une approbation. Les processus
d’analyse peuvent hériter de votre environnement ; supprimez donc les identifiants sans rapport avec l’analyse avant
de commencer. Consultez [Autorisations des analyses
locales](/fr-FR/codex/security/cli/reference#local-scan-permissions).

Choisissez un répertoire situé en dehors du dépôt pour les résultats de l’analyse :

```bash
REPOSITORY=/path/to/repository
SCAN_DIR=/path/outside/repository/codex-security-results

Si vous omettez `--output-dir`, Codex Security enregistre les résultats dans son propre répertoire d’état
persistant. Les résultats peuvent contenir des extraits de code source et des détails sur les vulnérabilités ;
choisissez donc un emplacement privé et une politique de conservation appropriée.

Si le répertoire d’état par défaut n’est pas accessible en écriture, sélectionnez un répertoire accessible en écriture
situé en dehors du dépôt analysé :

```bash

Vérifiez le dépôt, la cible et le répertoire de sortie avant de lancer une analyse :

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --dry-run

La simulation vérifie les entrées locales, notamment les éventuels chemins indiqués avec `--knowledge-base`,
sans démarrer Codex, charger des identifiants ni sonder l’interpréteur Python
du plugin.

## Exécutez votre première analyse

Exécutez une analyse standard et conservez ses résultats dans le répertoire sélectionné :

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR"

Les terminaux interactifs affichent un tableau de bord d’analyse en temps réel. Ajoutez `--headless` pour afficher
à la place de simples lignes de progression. La CI et les terminaux sans session interactive
affichent automatiquement la progression sous cette forme.

Le tableau de bord affiche également les détails de la session en temps réel. Ceux-ci peuvent contenir du code source
ou des identifiants ; examinez-les avant de les partager.

Par défaut, la CLI écrit la progression de l’analyse et son récapitulatif final sur stderr.
Elle n’affiche pas le résultat complet de l’analyse sur stdout. Une analyse terminée affiche un
récapitulatif semblable à celui-ci :

```text
  REPORT    /path/outside/repository/codex-security-results/report.md

  FINDINGS  2 (2 confirmed this scan; 0 previously found; 1 high, 1 medium)
  COVERAGE  complete
  ELAPSED   42s
  RESULTS   /path/outside/repository/codex-security-results

La consommation de tokens et le coût estimé s’affichent lorsqu’ils sont disponibles. Pour afficher le résultat
complet au format JSON lisible par machine, demandez explicitement une sortie structurée :

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --json

Par défaut, les analyses génèrent uniquement un rapport ; les constats restent donc disponibles pour un examen
local. Vous pouvez ajouter un seuil de gravité lorsque vous souhaitez [exécuter des analyses dans la
CI](/fr-FR/codex/security/cli/ci).

## Choisissez un modèle et un niveau d’effort de raisonnement

Les analyses utilisent par défaut `gpt-5.6-sol` avec un effort de raisonnement de niveau `xhigh`. Sélectionnez un
autre modèle et un autre niveau d’effort lorsque la tâche l’exige :

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --model gpt-5.6-terra \
  --effort high

Les niveaux d’effort pris en charge sont `minimal`, `low`, `medium`, `high`, `xhigh` et
`max`.

## Examinez les résultats

Ouvrez `report.md` pour consulter une version lisible du résultat. Le répertoire de l’analyse contient également les
fichiers structurés utilisés pour l’automatisation :

```text
codex-security-results/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

- `scan-manifest.json` consigne la cible, le périmètre, le producteur et les artefacts
  scellés.
- `findings.json` consigne la gravité, le niveau de confiance, les emplacements, les preuves et les
  mesures correctives de chaque constat.
- `coverage.json` consigne les surfaces examinées, les exclusions, les travaux reportés, les questions
  en suspens et l’exhaustivité de la couverture.

La couverture peut être `complete`, `partial` ou `unknown`. Consultez les zones dont l’examen a été reporté ou
les questions en suspens avant de considérer l’analyse comme la preuve d’une revue.
La [référence de la CLI](/fr-FR/codex/security/cli/reference#scan-artifacts) décrit
le contrat complet relatif aux artefacts et aux sorties.

## Examinez et corrigez les constats

Après une analyse interactive complète ayant produit des constats, la CLI propose un navigateur de
constats. Examinez les preuves et choisissez les constats à corriger. Vous pouvez retrouver
les tâches enregistrées dans l’application de bureau Codex.

Pour corriger les constats de gravité élevée ou critique sans utiliser le navigateur :

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --patch --patch-severity high --json

Ajoutez `--create-pr` pour créer un commit contenant les correctifs vérifiés et ouvrir une pull request GitHub.

Vous pouvez également corriger des constats enregistrés ou importer des tickets Linear. Consultez la
[référence de `validate` et `patch`](/fr-FR/codex/security/cli/reference#codex-security-validate-and-codex-security-patch).

## Choisissez l’analyse suivante

Utilisez une analyse ciblée sur un chemin lorsqu’un dépôt contient des services ou des packages distincts :

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --path services/billing \
  --path packages/auth

Examinez les modifications incluses dans les commits entre la révision de base et `HEAD` :

```bash
npx @openai/codex-security scan "$REPOSITORY" --diff origin/main --head HEAD

Examinez les modifications indexées et non indexées par rapport à `HEAD` :

```bash
npx @openai/codex-security scan "$REPOSITORY" --working-tree --base HEAD

Les analyses de diff et d’arbre de travail exigent que l’argument du dépôt corresponde à la racine de l’arbre de travail
Git. Récupérez les révisions sélectionnées avant de lancer une analyse de diff.

Utilisez le mode approfondi lorsqu’un dépôt ou un chemin nécessite un examen plus étendu :

```bash
npx @openai/codex-security scan "$REPOSITORY" --mode deep

Pour contrôler les workers, les sous-agents et le moment où l’analyse s’arrête :

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

Ces options nécessitent le mode approfondi, qui prend en charge les cibles de type dépôt ou chemin,
mais pas les analyses de diff ou d’arbre de travail. Ici, `--workers` contrôle les workers indépendants
d’analyse standard au sein d’une même analyse ; `bulk-scan --workers` contrôle les analyses simultanées
de dépôts. `--max-time-hours` accepte une valeur positive allant jusqu’à `96`,
y compris des fractions d’heure. Lorsque cette limite est atteinte, l’analyse arrête les workers qui n’ont pas terminé,
conserve les résultats des analyses terminées et les regroupe dans le rapport final.

## Ajoutez un contexte d’architecture et de sécurité

Fournissez des documents d’architecture, des modèles de menaces ou des politiques de sécurité comme
contexte d’analyse. Codex Security peut ainsi évaluer les constats à partir du fonctionnement réel de votre
système :

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

## Ajoutez des instructions d’analyse personnalisées

Ajoutez des instructions pour orienter l’analyse vers vos priorités de sécurité. Utilisez un
second fichier pour les instructions de suivi :

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --scan-prompt-file /path/to/scan.md \
  --post-scan-prompt-file /path/to/follow-up.md

Le suivi s’exécute dans la même session authentifiée après les analyses réussies
et après celles dont la couverture est incomplète ou qui présentent des erreurs. Si le suivi échoue, la CLI
émet un avertissement et conserve l’analyse terminée. Il ne s’exécute pas après
une annulation ni après une analyse ayant atteint sa limite de coût. Les deux options fonctionnent également
avec `bulk-scan` ; une colonne `prompt` du fichier CSV ajoute des instructions propres à chaque dépôt.

## Définissez un budget d’analyse

Utilisez `--max-cost` pour arrêter une analyse lorsque le coût estimé du modèle dépasse une limite
exprimée en USD :

```bash
npx @openai/codex-security scan "$REPOSITORY" --max-cost 5

Les requêtes déjà en cours peuvent se terminer en dépassant légèrement la limite. Si une analyse
approfondie atteint cette limite après que Codex Security a regroupé les résultats des workers
ayant terminé, la CLI enregistre le rapport finalisé, indique que sa couverture est `partial`,
et renvoie le code de sortie `2`. Si l’analyse ne peut pas produire de rapport finalisé, toute
sortie partielle disponible reste sur le disque.

## Analysez les modifications avant chaque commit

Installez un contrôle de sécurité Git pre-commit pour votre dépôt :

```bash
npx @openai/codex-security install-hook

Le contrôle analyse les modifications indexées et non indexées avant chaque commit. Il bloque les commits en cas de signalements de gravité élevée ou d’erreurs d’analyse,
sans remplacer un script pre-commit existant.

## Analysez des dépôts en masse

Connectez-vous à GitHub avant de découvrir des dépôts :

```bash
gh auth login

Découvrez et sélectionnez des dépôts de votre compte ou de votre organisation GitHub :

```bash
npx @openai/codex-security bulk-scan

Le parcours interactif exclut les dépôts archivés et les forks. Il vous demande de
confirmer les dépôts sélectionnés avant de lancer l’analyse.

Pour analyser une liste de dépôts préparée, fournissez un fichier CSV et un répertoire de sortie :

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Relancez la même commande pour reprendre une analyse en masse existante. Codex Security
ignore les dépôts déjà traités. Ajoutez `--max-attempts 3` pour réessayer en cas
d’erreurs temporaires liées aux dépôts ou aux analyses.

Pour la découverte de dépôts GitHub, la préparation des fichiers CSV, les résultats des campagnes et la configuration de Docker, consultez
[Lancez des analyses de sécurité en masse](/fr-FR/codex/security/cli/bulk-scans).

## Lancez des analyses en masse dans Docker

Si votre accès inclut l’image Docker de Codex Security, utilisez la configuration
Compose renforcée et le profil de sécurité fournis sur un hôte Docker Linux.
L’hôte doit permettre à des utilisateurs non privilégiés de créer des espaces de noms utilisateur. Fournissez un fichier
CSV de dépôts, conservez les résultats et l’état de connexion dans des répertoires montés persistants, et
fournissez les identifiants via votre environnement ou un gestionnaire de secrets :

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

Le conteneur lance des analyses en masse sans invite interactive. Utilisez la CLI en dehors de
Docker pour découvrir des dépôts de manière interactive. Pour les dépôts
privés, fournissez `GH_TOKEN` ou `GITHUB_TOKEN` via votre environnement ou un
gestionnaire de secrets. Les [conditions de connexion](#sign-in), notamment l’accès au compte et au
dépôt, s’appliquent également aux analyses exécutées dans un conteneur.

## Consultez à nouveau une analyse enregistrée

Affichez les analyses enregistrées pour votre dépôt :

```bash
npx @openai/codex-security scans list "$REPOSITORY"

Copiez un identifiant d’analyse dans les résultats pour examiner ses signalements et sa configuration :

```bash
npx @openai/codex-security scans show SCAN_ID

Pour examiner les événements enregistrés d’une analyse et de ses workers :

```bash
npx @openai/codex-security scans logs SCAN_ID

Les journaux enregistrés ne sont pas expurgés et peuvent contenir du code source ou des identifiants.
Vérifiez-les avant de les partager.

Affichez les signalements ouverts dans l’ensemble des analyses du dépôt :

```bash
npx @openai/codex-security findings list "$REPOSITORY"

Un signalement antérieur reste ouvert lorsque la dernière analyse ne le confirme pas.

Pour marquer un signalement examiné comme faux positif, expliquez pourquoi il ne
s’applique pas :

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The route already checks permissions"

Les analyses ultérieures tiennent compte de cette explication, mais vérifient de nouveau le code actuel.

Lancez la même analyse sur la version actuellement extraite, avec sa configuration d’origine :

```bash
npx @openai/codex-security scans rerun SCAN_ID

Comparez deux analyses pour identifier les signalements nouveaux, persistants, rouverts, résolus ou de statut
inconnu :

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

La comparaison associe automatiquement les signalements selon leur cause racine et réutilise les correspondances
enregistrées.

Pour connaître le format CSV des analyses en masse, les filtres de l’historique des analyses et les options des commandes, consultez
la [référence de la CLI](/fr-FR/codex/security/cli/reference).

Poursuivez avec le workflow adapté à votre objectif :

- [Lancez des analyses de sécurité en masse](/fr-FR/codex/security/cli/bulk-scans) pour découvrir des dépôts GitHub
  ou analyser un inventaire CSV épinglé.
- [Consultez la FAQ de la CLI](/fr-FR/codex/security/cli/faq) pour obtenir des réponses sur l’historique des analyses,
  les retours sur les faux positifs, la couverture et la vérification des correctifs.
- [Lancez des analyses en CI](/fr-FR/codex/security/cli/ci) pour examiner les pull requests, conserver
  les résultats et définir une politique de gravité.
- [Consultez la référence de la CLI](/fr-FR/codex/security/cli/reference) pour vérifier chaque option,
  format de sortie, artefact et code de sortie.
- [Intégrez le SDK TypeScript](/fr-FR/codex/security/sdk) pour lancer des analyses depuis une
  application ou un outil de développement.
