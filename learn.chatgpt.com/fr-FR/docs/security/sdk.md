<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/sdk -->

Utilisez le SDK TypeScript de Codex Security pour analyser la sécurité des dépôts et des
modifications de code depuis votre application ou votre outil de développement. Le SDK renvoie des constats
typés, des informations sur la couverture et les chemins des artefacts d’analyse. Pour les analyses plus longues,
il prend en charge les vérifications préalables, les limites de coût, les callbacks de progression et l’annulation.

Le SDK utilise les modules ECMAScript (ESM) et s’exécute côté serveur avec Node.js 22
(22.13.0 ou une version ultérieure), 24 ou 26. Les analyses nécessitent également Python 3.10 ou une version ultérieure.
Python 3.10 nécessite aussi le package `tomli`.

  Le SDK Codex Security est [accessible publiquement sur
  GitHub](https://github.com/openai/codex-security). L’exécution d’analyses nécessite
  un accès à Codex Security. Pour les agents de programmation généralistes, consultez le [guide du SDK
  Codex](/fr-FR/codex/codex-sdk). Pour les workflows dans le terminal et en CI, consultez le [guide de démarrage rapide de la CLI Codex
  Security](/fr-FR/codex/security/cli).

## Configurez le SDK

Installez le SDK :

```bash
npm install @openai/codex-security

Avant de lancer une analyse, définissez `OPENAI_API_KEY` ou `CODEX_API_KEY`, utilisez une
connexion Codex existante stockée dans un fichier, ou [configurez un autre
fournisseur](#configure-the-runtime-and-credentials). Amazon Bedrock utilise des identifiants
AWS ; OpenRouter et Fireworks utilisent des clés API et une
configuration propres à chaque fournisseur.

Pour obtenir les meilleurs résultats, utilisez un compte vérifié pour [Trusted Access for
Cyber](https://chatgpt.com/cyber). Se connecter ou fournir une clé API ne donne pas
accès à Trusted Access.

## Exécutez une analyse

Analysez uniquement les dépôts auxquels vous faites confiance et que vous avez l’autorisation d’évaluer. Le SDK s’exécute
avec les autorisations de votre système d’exploitation local et ne s’interrompt jamais pour demander une approbation.
Les processus d’analyse peuvent hériter de votre environnement : supprimez donc les identifiants non pertinents
avant de commencer. Consultez la section [Autorisations des analyses
locales](/fr-FR/codex/security/cli/reference#local-scan-permissions).

Créez un seul client `CodexSecurity`, exécutez une analyse standard du dépôt, puis fermez
le client une fois l’opération terminée. Transmettez `outputDir` pour choisir un répertoire privé
de résultats situé hors de l’arbre de travail Git englobant.

Si vous omettez `outputDir`, Codex Security enregistre les résultats dans son propre répertoire
d’état persistant. Les résultats peuvent contenir des extraits de code source et des informations
sur les vulnérabilités : choisissez donc des autorisations et des politiques de conservation adaptées.

```ts

const security = new CodexSecurity();

try {
  const result = await security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
  });

  console.log(result.reportPath);
  console.log(result.coverage.completeness);
  console.log(result.findings.findings.length);
} finally {
  await security.close();
}

`run` lance l’analyse, attend qu’elle se termine, valide les artefacts scellés,
puis renvoie un `ScanResult`. `close` libère l’environnement d’exécution isolé et accepte
les appels répétés.

## Vérifiez les entrées avec preflight

Utilisez `preflight` pour vérifier un dépôt, une cible, un mode, les documents de la base de connaissances,
l’emplacement de sortie et la configuration Codex avant de lancer une analyse :

```ts
const plan = await security.preflight("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
  knowledgeBasePaths: ["/path/to/architecture.md"],
  outputDir: "/path/outside/repository/results",
});

console.log(plan.repository);
console.log(plan.target.kind);
console.log(plan.mode);
console.log(plan.outputDir);

La vérification préalable ne modifie ni l’environnement d’exécution Codex ni les identifiants. Elle laisse également
à l’analyse elle-même la détection du plugin et de Python. Elle permet ainsi
de vérifier les entrées utilisateur avant une opération de longue durée ou nécessitant des identifiants.

Pour prévisualiser l’archivage d’un répertoire de résultats existant, définissez
`archiveExisting: true` :

```ts
const plan = await security.preflight("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
});

console.log(plan.archiveDir);

La valeur `archiveDir` renvoyée donne un aperçu du nom de l’archive. Le chemin final peut
différer, car `run` génère sa propre destination unique. Récupérez le chemin réel
de l’archive avec `onOutputArchived` :

```ts
await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
  onOutputArchived(archiveDir) {
    console.log("Archived results:", archiveDir);
  },
});

L’analyse archive les résultats précédents et démarre avec un répertoire de sortie
vide.

## Choisissez une cible d’analyse

Le SDK prend en charge les cibles de type dépôt, chemin, diff entre commits et arbre de travail.
Par défaut, la cible est l’intégralité du dépôt.

### Analysez les chemins sélectionnés

Transmettez un tableau de chemins situés dans le dépôt :

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
});

Les chemins peuvent désigner des fichiers ou des répertoires. Le SDK résout chaque chemin au sein du
dépôt et supprime les doublons.

### Analysez les modifications enregistrées dans des commits

Utilisez `DiffTarget.refs` pour analyser les modifications enregistrées dans des commits entre deux révisions
Git disponibles localement :

```ts

const target = DiffTarget.refs({
  base: "origin/main",
  head: "HEAD",
});

const result = await security.run("/path/to/repository", { target });

La révision de tête est `HEAD` par défaut. Pour les cibles de diff, l’argument du dépôt doit
correspondre à la racine de l’arbre de travail Git.

### Analysez l’arbre de travail

Utilisez `DiffTarget.workingTree` pour analyser les modifications indexées et non indexées par rapport à une
révision de base :

```ts
const target = DiffTarget.workingTree({ base: "HEAD" });
const result = await security.run("/path/to/repository", { target });

La révision de base est `HEAD` par défaut. Récupérez les révisions sélectionnées avant de lancer une analyse
de diff ou d’arbre de travail.

### Sélectionnez le mode approfondi

Définissez `mode: "deep"` pour analyser un dépôt ou un chemin nécessitant un examen plus étendu :

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing"],
  mode: "deep",
  workers: 2,
  subagents: 0,
  stopAfterNoNew: 3,
  maxDiscoveryRuns: 10,
  maxTimeHours: 1.5,
});

Le mode approfondi prend en charge les cibles de type dépôt et chemin. Utilisez le mode standard pour les analyses de diff et
d’arbre de travail. Les paramètres facultatifs définissent le nombre de workers indépendants exécutant simultanément
des analyses standard, le nombre de sous-agents par worker, le nombre d’analyses de workers terminées consécutivement
sans nouveaux constats, ainsi que le nombre total et la durée des exécutions des workers. Ces paramètres
nécessitent `mode: "deep"`.

`maxTimeHours` vaut `96` par défaut et accepte tout nombre positif inférieur ou égal à `96`,
y compris les fractions d’heure. À l’échéance, Codex Security arrête les workers qui n’ont pas terminé,
conserve les résultats des analyses terminées et les agrège dans le rapport
final. Vérifiez `result.coverage.completeness` avant de considérer une analyse limitée
dans le temps comme la preuve d’une couverture complète.

### Ajoutez une base de connaissances sur la sécurité

Transmettez des documents d’architecture, des modèles de menaces ou des politiques de sécurité via
`knowledgeBasePaths` :

```ts
const result = await security.run("/path/to/repository", {
  knowledgeBasePaths: [
    "/path/to/architecture.md",
    "/path/to/security-policies",
  ],
});

Le SDK accepte des fichiers ou des répertoires et parcourt ces derniers de manière récursive.
Les formats de document pris en charge sont `.md`, `.markdown`, `.txt`, `.pdf` et `.docx`.
Le SDK refuse les chemins d’entrée correspondant à des liens, ignore les liens présents dans les répertoires et conserve
le contenu extrait des documents en dehors des résultats d’analyse enregistrés.

### Ajoutez des instructions d’analyse et de suivi

Utilisez `scanPrompt` pour cibler l’analyse et `postScanPrompt` pour demander un suivi :

```ts
const result = await security.run("/path/to/repository", {
  scanPrompt: "Focus on tenant isolation and authorization checks.",
  postScanPrompt: "Write confirmed findings to post-scan-summary.md.",
});

Si le suivi échoue, le SDK conserve l’analyse terminée et signale l’erreur
via `onWarning`. Il restaure tous les artefacts de l’analyse terminée que le
suivi a modifiés.

### Définissez un budget d’analyse

Définissez `maxCostUsd` pour arrêter une analyse lorsque son coût estimé d’utilisation du modèle dépasse une limite.
Utilisez `onCost` pour suivre ce coût pendant l’analyse :

```ts
const result = await security.run("/path/to/repository", {
  maxCostUsd: 5,
  onCost(cost) {
    console.log(cost.estimatedUsd);
  },
});

console.log(result.cost?.estimatedUsd);

Cette limite correspond à une estimation des dépenses, mais ne constitue pas un plafond strict : les requêtes déjà
en cours peuvent donc se terminer en la dépassant légèrement. Si une analyse approfondie atteint cette limite après que
Codex Security a agrégé les résultats des workers ayant terminé leur analyse, `run` renvoie un résultat
dans lequel `coverage.completeness` est défini sur `"partial"`, puis signale l’avertissement budgétaire
via `onWarning`.

Si l’analyse ne peut pas produire de résultat partiel finalisé, `run` lève
l’exception `ScanCostLimitExceededError` et conserve toutes les données de sortie disponibles.

## Exploitez les résultats d’analyse

`ScanResult` donne accès aux documents structurés, aux métadonnées d’analyse et aux chemins
des artefacts :

| Propriété             | Contenu                                                                           |
| -------------------- | ---------------------------------------------------------------------------------- |
| `manifest`           | Le manifeste scellé de l’analyse, comprenant la cible, le périmètre, le producteur et les enregistrements des artefacts. |
| `findings`           | Constats issus de l’analyse actuelle. Lisez les objets de constat dans `findings.findings`.     |
| `repositoryFindings` | Constats non résolus dans les différentes analyses du dépôt, lorsque l’historique des analyses est disponible.             |
| `coverage`           | Surfaces examinées, exclusions, tâches reportées, questions en suspens et exhaustivité.    |
| `scanDir`            | Le répertoire de l’analyse.                                                                |
| `threadId`           | L’identifiant du thread Codex pour l’analyse.                                          |
| `turnResult`         | État du tour, réponse et métadonnées d’utilisation disponibles.                               |
| `cost`               | Coût estimé lié au modèle et aux tokens, ou `null` si cette estimation n’est pas disponible.                        |
| `reportPath`         | Le chemin vers `report.md`.                                                           |
| `manifestPath`       | Le chemin vers `scan-manifest.json`.                                                  |
| `findingsPath`       | Le chemin vers `findings.json`.                                                       |
| `coveragePath`       | Le chemin vers `coverage.json`.                                                       |
| `artifactsDir`       | Le répertoire des artefacts complémentaires.                                                |
| `sarifPath`          | Le chemin SARIF généré, ou `null` en l’absence de fichier SARIF.                          |
| `pluginVersion`      | La version enregistrée par le producteur de l’analyse.                                         |

Pour exiger le même plugin lors d’une analyse ultérieure, transmettez
`expectedPluginVersion: result.pluginVersion`. Le SDK refuse l’analyse si
la version du plugin installé diffère.

Utilisez directement les constats structurés et les données de couverture :

```ts
for (const finding of result.findings.findings) {
  const location = finding.locations[0];
  if (location === undefined) continue;

  console.log(
    finding.severity.level,
    `${location.path}:${location.startLine}`,
    finding.title
  );
}

for (const deferred of result.coverage.deferred) {
  console.log(deferred.id, deferred.reason);
}

Les constats peuvent inclure les champs facultatifs `codeEvidence`, `rootCause`, `validation`,
`attackPath`, `remediationTests` et `preventiveControls`.

Pour les constats portant sur l’ensemble du dépôt, `confirmedInLatestScan` distingue ceux
identifiés lors de la dernière analyse des constats antérieurs encore ouverts :

```ts
for (const finding of result.repositoryFindings ?? []) {
  console.log(finding.title, finding.confirmedInLatestScan);
}

L’exhaustivité de la couverture peut être `complete`, `partial` ou `unknown`. Examinez les surfaces dont l’évaluation a été reportée,
les exclusions et les questions en suspens avant de vous appuyer sur une analyse pour prendre une
décision de sécurité.

`result.toJSON()` renvoie le manifeste, les constats du dépôt et de l’analyse en cours,
la couverture, les identifiants de l’analyse et du thread, `reportPath`, `artifactsDir`,
`sarifPath`, le coût et les métadonnées du tour dans un même objet prêt à être sérialisé en JSON.

## Suivi et annulation d’une analyse

Transmettez les fonctions de rappel de `ScanOptions` pour signaler le démarrage de l’analyse, la progression des workers et
les tentatives de reconnexion :

```ts
const result = await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  onScanStarted() {
    console.log("Scan started");
  },
  onProgress(progress) {
    console.log(progress.phase, progress.filesCompleted, progress.filesTotal);
  },
  onWorkerStatus(status) {
    console.log(status.kind, status);
  },
  onSessionEvent(session) {
    console.log(session.threadId, session.worker, session.event["type"]);
  },
  onReconnect(attempt, maxAttempts) {
    console.log(`Reconnect attempt ${attempt} of ${maxAttempts}`);
  },
  onObserverError(observer, error) {
    console.error(`${observer} failed`, error);
  },
});

console.log(result.reportPath);

Transmettez un `AbortSignal` lorsque l’annulation provient d’une requête, d’un contrôleur de tâches
ou d’un délai d’expiration :

```ts

const controller = new AbortController();

try {
  const scan = security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
    signal: controller.signal,
  });

  controller.abort();
  await scan;
} catch (error) {
  if (error instanceof ScanInterruptedError) {
    console.error(error.scanDir);
  } else {
    throw error;
  }
}

Une analyse interrompue peut laisser une sortie partielle dans `scanDir`. Conservez ce
répertoire si le résultat doit être examiné.

Les applications qui affichent la progression de la configuration de l’analyse peuvent également utiliser les fonctions de rappel de `ScanOptions`
pour suivre le cycle de vie :

| Fonction de rappel                            | Appelée lorsque                                          |
| ----------------------------------- | ---------------------------------------------------- |
| `onAuthentication(authentication)`  | L’analyse sélectionne sa méthode d’authentification.          |
| `onOutputArchived(archiveDir)`      | Les résultats existants sont déplacés vers le répertoire d’archivage.      |
| `onOutputDirReady(scanDir)`         | Le répertoire privé de l’analyse est prêt.                 |
| `onScanStarted()`                   | La configuration de l’analyse est terminée et l’exécution commence.           |
| `onTrustedAccessStatus(status)`     | Le statut de Trusted Access devient disponible.             |
| `onReconnect(attempt, maxAttempts)` | Le SDK retente la connexion au flux d’analyse après une déconnexion.          |
| `onActivity(activity)`              | Une commande, un outil, une étape de raisonnement ou un message est mis à jour. |
| `onProgress(progress)`              | La phase de l’analyse ou le nombre de fichiers examinés change.       |
| `onWorkerStatus(status)`            | Le statut du contrôle préalable ou de l’affectation d’un worker change.         |
| `onSessionEvent(session)`           | Une session d’analyse ou de worker émet un événement.             |
| `onCost(cost)`                      | Une estimation actualisée du coût de l’analyse est disponible.         |
| `onWarning(warning)`                | L’analyse signale un avertissement.                          |
| `onObserverError(observer, error)`  | Une autre fonction de rappel liée au cycle de vie de l’analyse lève une erreur.     |

Le statut de Trusted Access est `granted`, `not_granted` ou `unknown`. Un accès absent ou
inconnu déclenche également `onWarning`.

`onSessionEvent` reçoit des événements non expurgés pouvant contenir du code
source ou des identifiants. Filtrez-les avant de les envoyer à des journaux partagés ou à d’autres
services.

## Configuration de l’environnement d’exécution et des identifiants

Transmettez une configuration de l’environnement d’exécution lorsque vous avez besoin d’un plugin, d’un interpréteur ou
d’un paramètre Codex spécifique :

```ts
const security = new CodexSecurity({
  pluginPath: "/path/to/codex-security-plugin",
  pythonPath: "/path/to/python",
  codexOverrides: {
    model: "gpt-5.6-terra",
    model_reasoning_effort: "high",
  },
});

`pluginPath` accepte un répertoire de plugin ou une archive ZIP. `pythonPath` sélectionne
l’interpréteur du plugin. `codexOverrides` fusionne les valeurs prises en charge dans la configuration
Codex isolée. Les analyses utilisent `gpt-5.6-sol` avec un effort de raisonnement très élevé
par défaut. Définissez `model` et `model_reasoning_effort` dans `codexOverrides` pour utiliser
un autre modèle ou un autre effort de raisonnement. Pour utiliser [Amazon
Bedrock](/fr-FR/codex/security/cli/reference#use-amazon-bedrock), définissez
`model_provider` et `model` dans `codexOverrides`.

`codexOverrides` ne peut ni restreindre l’accès de l’analyse au système de fichiers ni modifier sa
politique d’approbation. Consultez les [autorisations des analyses
locales](/fr-FR/codex/security/cli/reference#local-scan-permissions).

Pour OpenRouter ou Fireworks, fournissez également la clé API correspondante et une configuration complète
du fournisseur dans `codexOverrides`. Par exemple, définissez
`OPENROUTER_API_KEY` et configurez OpenRouter :

```ts
const security = new CodexSecurity({
  codexOverrides: {
    model: "anthropic/claude-sonnet-4.5",
    model_provider: "openrouter",
    model_providers: {
      openrouter: {
        name: "OpenRouter",
        base_url: "https://openrouter.ai/api/v1",
        env_key: "OPENROUTER_API_KEY",
        wire_api: "responses",
      },
    },
  },
});

Pour Fireworks, remplacez les deux clés `openrouter` par `fireworks`, définissez `name` sur
`Fireworks AI`, définissez `env_key` sur `FIREWORKS_API_KEY`, utilisez
`https://api.fireworks.ai/inference/v1` comme valeur de `base_url`, puis sélectionnez un modèle
Fireworks.

Le client expose également les méthodes d’authentification prises en charge :

| Méthode                     | Fonction                                                     |
| -------------------------- | ----------------------------------------------------------- |
| `loginApiKey(apiKey)`      | Authentifier l’environnement d’exécution isolé à l’aide d’une clé API.          |
| `loginChatGPT()`           | Démarrer un flux de connexion dans le navigateur et renvoyer un objet de connexion.     |
| `loginChatGPTDeviceCode()` | Démarrer un flux de connexion par code d’appareil et renvoyer un objet de connexion. |
| `account()`                | Renvoyer l’état d’authentification actuel.                    |
| `logout()`                 | Effacer l’authentification de l’environnement isolé.                              |

Un objet de connexion fournit `waitForInstructions`, `authUrl`, `verificationUrl`,
`userCode`, `wait` et `cancel` afin qu’une application puisse présenter et mener à terme le
flux de connexion sélectionné. Le SDK peut réutiliser une connexion Codex enregistrée dans un fichier. Les clés API
conviennent bien à la CI et à l’automatisation côté serveur.

Lorsqu’une clé API et une connexion enregistrée sont toutes deux disponibles, le SDK utilise la clé API
par défaut. Pour utiliser plutôt votre connexion ChatGPT, sélectionnez-la pour l’analyse :

```ts
const result = await security.run("/path/to/repository", {
  auth: "chatgpt",
});

Définissez `auth: "api-key"` pour exiger qu’une clé API soit définie dans l’environnement. `preflight` accepte
la même option `auth`.

## Gestion des erreurs d’analyse

Interceptez la classe d’erreur exportée qui correspond à l’action que votre application peut
entreprendre :

| Erreur                            | Signification                                                            |
| -------------------------------- | ------------------------------------------------------------------ |
| `AuthenticationRequiredError`    | Une analyse nécessite un moyen d’authentification pris en charge.                               |
| `ConfigurationError`             | La configuration Codex ou une surcharge ne convient pas.                  |
| `InvalidTargetError`             | Le dépôt, le chemin, le mode ou la cible Git ne convient pas.           |
| `OutputDirectoryError`           | L’emplacement de sortie ou les autorisations associées ne conviennent pas.             |
| `OutputInsideProtectedRootError` | Le répertoire de sortie se trouve dans le dépôt ou l’arbre de travail analysé. |
| `PluginPythonUnavailableError`   | Aucun interpréteur Python utilisable n’est disponible.                        |
| `PluginBootstrapError`           | L’environnement d’exécution du plugin n’a pas pu démarrer.                                |
| `ScanCostLimitExceededError`     | L’analyse a dépassé la limite fixée pour son coût estimé.                        |
| `IncompleteScanError`            | L’analyse s’est terminée avant de produire le résultat requis.               |
| `ContractValidationError`        | Une analyse terminée a renvoyé une erreur liée au contrat structuré.             |
| `ScanInterruptedError`           | Une interruption a arrêté l’analyse et peut avoir laissé une sortie partielle. |

Poursuivez avec le [démarrage rapide de la CLI](/fr-FR/codex/security/cli), le [guide de la
CI](/fr-FR/codex/security/cli/ci) ou la [référence de la
CLI](/fr-FR/codex/security/cli/reference).
