<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/cli/bulk-scans -->

Utilisez `npx @openai/codex-security bulk-scan` pour examiner des dépôts au cours d’une même
campagne. Découvrez les dépôts de votre compte GitHub personnel ou d’une
organisation, ou fournissez un fichier CSV qui associe chaque dépôt à une
révision Git précise.

  Le package `@openai/codex-security` est public. L’exécution des analyses nécessite un accès
  à Codex Security. Suivez le [guide de démarrage rapide de la CLI](/fr-FR/codex/security/cli) pour installer
  la CLI et vous connecter.

## Choisissez une source de dépôts

| Source           | Quand l’utiliser                                                                          |
| ---------------- | --------------------------------------------------------------------------------------- |
| Découverte de dépôts GitHub | Sélectionnez de manière interactive des dépôts depuis votre compte GitHub personnel ou une organisation. |
| Inventaire CSV    | Exécutez une campagne automatisée et reproductible sur des révisions précises de dépôts.                |

Les deux workflows enregistrent votre progression, conservent les résultats de chaque dépôt et vous permettent de
reprendre une campagne après une interruption.

## Découvrez des dépôts GitHub

Connectez-vous à l’aide de GitHub CLI :

```bash
gh auth login

Lancez une analyse en masse interactive :

```bash
npx @openai/codex-security bulk-scan

La CLI vous guide au fil des étapes suivantes :

1. Choisissez votre compte GitHub personnel ou une organisation.
2. Passez en revue les dépôts actifs au cours des 90 derniers jours.
3. Effectuez une recherche dans la liste des dépôts et sélectionnez ceux à analyser.
4. Choisissez un répertoire pour les résultats d’analyse.
5. Passez en revue les dépôts sélectionnés et confirmez la campagne.

La découverte exclut les dépôts archivés et les forks. La CLI consigne le commit exact
de la branche par défaut de chaque dépôt sélectionné dans
`<output-directory>/repositories.csv`. Aucune analyse ne démarre tant que vous n’avez pas confirmé
la sélection.

Pour utiliser GitHub Enterprise Server, commencez par vous connecter à votre hôte GitHub :

```bash
gh auth login --hostname github.example.com

Définissez `GH_HOST` lorsque vous lancez la découverte des dépôts :

```bash
GH_HOST=github.example.com npx @openai/codex-security bulk-scan

La découverte interactive nécessite un terminal. Pour la CI, les conteneurs ou une liste
de dépôts déjà préparée, utilisez plutôt un inventaire CSV.

## Créez un fichier CSV de dépôts

Créez un fichier CSV comportant une ligne par dépôt, avec sa révision figée :

```csv
id,repository,revision,scope,mode,prompt
payments,https://github.com/example/payments.git,0123456789abcdef0123456789abcdef01234567,services/api,standard,Review payment authorization and refunds.
identity,https://github.com/example/identity.git,fedcba9876543210fedcba9876543210fedcba98,,deep,Review session and identity boundaries.

Le fichier CSV prend en charge les colonnes suivantes :

| Colonne       | Obligatoire | Description                                                                                                |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------------- |
| `id`         | Oui      | Identifiant unique du dépôt. Utilisez des lettres, des chiffres, des points, des traits d’union ou des tirets bas.                      |
| `repository` | Oui      | URL HTTPS, URL SSH ou chemin d’accès à un dépôt local. Les chemins relatifs sont interprétés par rapport au répertoire du fichier CSV.               |
| `revision`   | Oui      | SHA complet d’un commit Git, comportant 40 ou 64 caractères. Les noms de branches, les tags et les hachages de commit abrégés ne sont pas pris en charge. |
| `scope`      | Non       | Répertoire à analyser, indiqué par un chemin relatif au dépôt. Omettez la valeur pour analyser l’intégralité du dépôt.                       |
| `mode`       | Non       | `standard` ou `deep`. Omettez la valeur pour utiliser le mode sélectionné par la commande.                                   |
| `prompt`     | Non       | Instructions d’analyse spécifiques à ce dépôt.                                                             |

Pour obtenir le SHA complet du commit d’un dépôt local, exécutez :

```bash
git -C /path/to/repository rev-parse HEAD

## Exécutez une campagne à partir d’un fichier CSV

Indiquez le fichier CSV et un répertoire de sortie privé situé en dehors des dépôts :

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

`--workers` contrôle le nombre d’analyses de dépôts exécutées simultanément et vaut `4` par défaut. Cette option ne
définit pas le nombre de workers indépendants effectuant des analyses standard au sein de chaque analyse approfondie ;
configurez ces limites avec
[`[deep_scan]`](/fr-FR/codex/security/cli/reference#configure-deep-scans). Utilisez `--mode
deep` pour sélectionner l’analyse approfondie pour les lignes sans `mode` propre. Chaque ligne du fichier CSV
peut néanmoins définir son propre mode d’analyse et le périmètre du dépôt.

Définissez `[deep_scan].max_time_hours` pour limiter l’exécution des workers lors de chaque analyse approfondie de
la campagne. L’option `--max-time-hours` fonctionne avec `scan`, mais pas avec `bulk-scan`.

La CLI extrait chaque révision figée, analyse la cible sélectionnée, enregistre le
résultat et supprime la copie de travail temporaire du dépôt. Un dépôt n’est marqué comme
terminé que si la couverture de son analyse est complète et que tous les artefacts de
résultat requis existent.

## Partagez le contexte de sécurité et les instructions

Ajoutez à chaque analyse des documents d’architecture, des modèles de menaces ou des politiques de sécurité
avec `--knowledge-base`. Répétez cette option pour ajouter d’autres fichiers ou répertoires :

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Pour ajouter des instructions d’analyse communes ou exécuter un suivi après chaque analyse,
fournissez des fichiers de prompts :

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --scan-prompt-file scan-instructions.md \
  --post-scan-prompt-file follow-up.md

La CLI ajoute le `prompt` défini dans le fichier CSV pour chaque dépôt après les instructions d’analyse
communes. Les instructions de suivi s’exécutent dans la même session authentifiée
après les analyses réussies et celles dont la couverture est incomplète ou qui présentent des erreurs,
mais pas après une annulation ni après une analyse ayant atteint sa limite de coût. Les chemins des fichiers de prompts
sont interprétés par rapport à votre répertoire courant.

## Choisissez un modèle et un niveau d’effort de raisonnement

Par défaut, les analyses en masse utilisent `gpt-5.6-sol` avec le niveau d’effort de raisonnement `xhigh`. Pour
choisir un autre modèle et un autre niveau d’effort pour une campagne CSV :

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --model gpt-5.6-terra \
  --effort high

Les mêmes options s’appliquent aussi lors de la découverte interactive de dépôts :

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

Les niveaux d’effort pris en charge sont `minimal`, `low`, `medium`, `high` et `xhigh`.

Pour utiliser OpenRouter ou Fireworks, définissez respectivement `OPENROUTER_API_KEY` ou `FIREWORKS_API_KEY`,
puis indiquez `--provider` et `--model`. Pour en savoir plus sur les identifiants et consulter des
exemples, reportez-vous à la [configuration d’OpenRouter ou de
Fireworks](/fr-FR/codex/security/cli/reference#use-openrouter-or-fireworks) ou à la [configuration
d’Amazon Bedrock](/fr-FR/codex/security/cli/reference#use-amazon-bedrock).

## Examinez les résultats de la campagne

Le répertoire de sortie contient la campagne figée, un registre des résultats auquel on peut uniquement ajouter des entrées,
ainsi que des artefacts distincts pour chaque dépôt et chaque tentative :

```text
security-scans/
├── manifest.json
├── results.jsonl
├── checkouts/
└── artifacts/
    ├── payments/
    │   └── attempt-1/
    │       ├── scan-manifest.json
    │       ├── findings.json
    │       ├── coverage.json
    │       └── report.md
    └── identity/
        └── attempt-1/
            ├── scan-manifest.json
            ├── findings.json
            ├── coverage.json
            └── report.md

- `manifest.json` consigne les dépôts, les révisions figées, les périmètres, les modes
  d’analyse et les instructions de la campagne, qu’elles soient communes ou propres à un dépôt.
- `results.jsonl` consigne chaque tentative pour un dépôt, son état, son répertoire
  d’artefacts et les informations disponibles sur les coûts ou les erreurs.
- `report.md` fournit un rapport lisible sur une tentative d’analyse d’un dépôt.
- `findings.json` et `coverage.json` consignent les constats de cette tentative et le périmètre
  examiné.

Exportez l’analyse terminée d’un dépôt lorsque vous avez besoin d’un résultat portable :

```bash
npx @openai/codex-security export \
  /path/outside/repositories/security-scans/artifacts/payments/attempt-1 \
  --export-format sarif \
  --output /path/outside/repositories/payments.sarif

Les résultats peuvent contenir des extraits de code source et des détails sur les vulnérabilités. Conservez le
répertoire de sortie dans un emplacement privé, en dehors des dépôts analysés, et appliquez-lui une
politique de conservation appropriée.

## Reprise d’une campagne

Exécutez à nouveau la commande d’origine avec le même fichier CSV et le même répertoire de sortie :

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

La CLI reprend les analyses de dépôts inachevées et ignore celles qui sont terminées. Les analyses
dont la couverture est incomplète ne sont pas relancées. Leurs résultats restent disponibles et
la commande renvoie le code de sortie `2`.

Pour un répertoire de sortie existant, ne modifiez pas l’inventaire des dépôts ni les
instructions d’analyse et de suivi. La CLI vérifie le manifeste épinglé et rejette toute
campagne différente. Utilisez un nouveau répertoire de sortie lorsque vous modifiez les dépôts,
les révisions, les périmètres, les modes d’analyse ou les instructions communes ou propres à un dépôt.

## Nouvelle tentative après une erreur sur un dépôt

Utilisez `--max-attempts` pour relancer le traitement d’un dépôt après une erreur temporaire de checkout ou
d’analyse :

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

Par défaut, chaque dépôt ne fait l’objet que d’une tentative. Chaque tentative dispose de son propre
reçu et de son propre répertoire d’artefacts. Les nouvelles tentatives s’appliquent aux erreurs de checkout, aux échecs d’analyse
et aux artefacts requis manquants. Les analyses terminées dont la couverture est incomplète
ne sont pas relancées.

Les analyses en masse renvoient les codes de sortie suivants :

| Code de sortie | Signification                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| `0`       | Le traitement de tous les dépôts s’est terminé avec succès.                                                                              |
| `2`       | Le traitement d’un dépôt n’a pas pu aboutir, la couverture d’une analyse était incomplète ou la commande a rencontré une erreur d’entrée ou d’exécution. |
| `130`     | Ctrl-C a interrompu la campagne.                                                                                      |
| `143`     | SIGTERM a mis fin à la campagne.                                                                                      |

## Lancez des analyses en masse dans Docker

Le [dépôt
Codex Security](https://github.com/openai/codex-security) inclut une configuration
Compose renforcée pour les campagnes CSV automatisées sur un hôte Docker sous Linux. Cet
hôte doit permettre à des utilisateurs non privilégiés de créer des espaces de noms utilisateur.

Conservez le fichier CSV des dépôts, les résultats d’analyse et l’état de connexion montés dans des répertoires
persistants. Fournissez les identifiants OpenAI par l’environnement ou par un gestionnaire de
secrets. Pour les dépôts GitHub privés, fournissez `GH_TOKEN` ou `GITHUB_TOKEN`
de la même manière.

Exécutez l’image avec le fichier CSV et le répertoire de sortie montés :

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

Utilisez le même fichier CSV et le même répertoire de sortie montés pour reprendre la campagne. Pour
GitHub Enterprise Server, attribuez à `CODEX_SECURITY_GIT_HOST` la valeur de votre hôte GitHub.

Pour connaître toutes les options disponibles, consultez la [référence de la commande
bulk-scan](/fr-FR/codex/security/cli/reference#codex-security-bulk-scan). Pour obtenir des réponses aux questions
courantes sur la couverture et les résultats des analyses, consultez la [FAQ de la
CLI](/fr-FR/codex/security/cli/faq).
