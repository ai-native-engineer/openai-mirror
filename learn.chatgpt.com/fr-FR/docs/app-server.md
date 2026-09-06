<!-- source: https://learn.chatgpt.com/fr-FR/docs/app-server -->

Codex app-server est l’interface qu’utilise Codex pour faire fonctionner des clients riches (par exemple, l’extension Codex pour VS Code). Utilisez-la pour intégrer Codex en profondeur à votre propre produit : authentification, historique des conversations, approbations et événements de l’agent diffusés en continu. L’implémentation d’app-server est disponible en open source dans le dépôt GitHub de Codex ([openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)). Consultez la page [Open source](/fr-FR/codex/open-source) pour obtenir la liste complète des composants open source de Codex.

  Si vous automatisez des tâches ou exécutez Codex en CI, utilisez plutôt le
<a href="/codex/codex-sdk">SDK Codex</a>.

## Connectez l’interface terminal de la CLI

Le mode d’interface terminal à distance vous permet d’exécuter app-server sur une machine et de connecter
l’interface terminal de Codex CLI depuis une autre. Démarrez un écouteur WebSocket :

```bash
codex app-server --listen ws://127.0.0.1:4500

Connectez ensuite l’interface terminal :

```bash
codex --remote ws://127.0.0.1:4500

Pour une connexion non locale, configurez l’authentification WebSocket et protégez la
connexion avec TLS. Stockez le token au porteur dans une variable d’environnement et
transmettez son nom au lieu de placer le token sur la ligne de commande :

```bash

codex --remote wss://remote-host:4500 \
  --remote-auth-token-env CODEX_REMOTE_TOKEN

L’option `--remote` accepte les points de terminaison `ws://`, `wss://`, `unix://` et
`unix://PATH`. N’utilisez des connexions WebSocket non chiffrées que pour localhost ou une connexion
avec redirection de port SSH.

## Connectez un hôte Code Mode distant

Par défaut, app-server démarre un hôte Code Mode local. Pour utiliser un hôte distant
à la place, transmettez son URL WebSocket sécurisée :

```bash
codex app-server --code-mode-host wss://code-mode.example.com/host

`--code-mode-host` contrôle la connexion sortante d’app-server à son hôte
Code Mode. Cette option ne modifie pas `--listen`, qui détermine comment les clients se connectent à
app-server. Tous les fils d’un même processus app-server partagent la connexion sélectionnée à l’hôte
Code Mode.

Utilisez `wss://` pour un hôte distant. N’utilisez `ws://` que pour une connexion à localhost ou
avec redirection de port SSH. La commande app-server et le transport WebSocket sont
expérimentaux et ne sont pas pris en charge pour les charges de travail en production.

## Protocole

Comme [MCP](https://modelcontextprotocol.io/), `codex app-server` prend en charge les communications bidirectionnelles au moyen de messages JSON-RPC 2.0 (l’en-tête `"jsonrpc":"2.0"` est omis lors de la transmission).

Transports pris en charge :

- `stdio` (`--listen stdio://`, par défaut) : JSON délimité par des sauts de ligne (JSONL).
- `websocket` (`--listen ws://IP:PORT`, expérimental et non pris en charge) : un
  message JSON-RPC par trame de texte WebSocket.
- Socket Unix (`--listen unix://` ou `--listen unix://PATH`) : connexions WebSocket
  via le socket de contrôle app-server par défaut de Codex ou un chemin de socket Unix
  personnalisé, au moyen de la négociation HTTP Upgrade standard.
- `off` (`--listen off`) : n’expose aucun transport local.

Lorsque vous utilisez `--listen ws://IP:PORT`, le même écouteur répond également à des sondes de santé
HTTP simples :

- `GET /readyz` renvoie `200 OK` dès que l’écouteur accepte de nouvelles connexions.
- `GET /healthz` renvoie `200 OK` lorsque la requête ne contient pas
  d’en-tête `Origin`.
- Les requêtes comportant un en-tête `Origin` sont rejetées avec `403 Forbidden`.

Le transport WebSocket est expérimental et non pris en charge. Les écouteurs locaux tels que
`ws://127.0.0.1:PORT` conviennent aux workflows sur localhost et à ceux utilisant une redirection
de port SSH. Pendant le déploiement progressif, les écouteurs WebSocket non limités à l’interface de bouclage autorisent actuellement
les connexions non authentifiées par défaut. Configurez donc l’authentification WebSocket avant
d’en exposer un à distance.

Options d’authentification WebSocket prises en charge :

- `--ws-auth capability-token --ws-token-file /absolute/path`
- `--ws-auth capability-token --ws-token-sha256 HEX`
- `--ws-auth signed-bearer-token --ws-shared-secret-file /absolute/path`

Pour les tokens au porteur signés, vous pouvez également définir `--ws-issuer`, `--ws-audience` et
`--ws-max-clock-skew-seconds`. Les clients présentent les informations d’authentification sous la forme
`Authorization: Bearer <token>` pendant la négociation WebSocket, et app-server
impose l’authentification avant l’appel JSON-RPC `initialize`.

Préférez `--ws-token-file` à la transmission de tokens au porteur bruts sur la ligne de commande. N’utilisez
`--ws-token-sha256` que lorsque le client conserve le token brut à forte entropie dans un magasin
local de secrets distinct ; l’empreinte ne sert qu’à la vérification et les clients ont toujours besoin
du token d’origine.

En mode WebSocket, app-server utilise des files d’attente de capacité limitée. Lorsque la file de réception des requêtes est pleine,
le serveur rejette les nouvelles requêtes avec le code d’erreur JSON-RPC `-32001` et le message
`"Server overloaded; retry later."` Les clients devraient réessayer avec un délai
qui augmente de façon exponentielle, assorti d’une variation aléatoire.

## Schéma des messages

Les requêtes contiennent `method`, `params` et `id` :

```json
{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.6-terra" } }

Les réponses renvoient le même `id` avec soit `result`, soit `error` :

```json
{ "id": 10, "result": { "thread": { "id": "thr_123" } } }

```json
{ "id": 10, "error": { "code": 123, "message": "Something went wrong" } }

Les notifications omettent `id` et utilisent uniquement `method` et `params` :

```json
{ "method": "turn/started", "params": { "turn": { "id": "turn_456" } } }

Vous pouvez générer un schéma TypeScript ou un bundle JSON Schema depuis la CLI. Chaque sortie est propre à la version de Codex exécutée ; les artefacts générés correspondent donc exactement à cette version :

```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas

## Bien démarrer

1. Démarrez le serveur avec `codex app-server` (transport stdio par défaut),
`codex app-server --listen ws://127.0.0.1:4500` (WebSocket sur TCP) ou
`codex app-server --listen unix://` (socket Unix par défaut).
2. Connectez un client via le transport sélectionné, puis envoyez `initialize`, suivi de la notification `initialized`.
3. Créez un fil et démarrez un tour, puis continuez à lire les notifications dans le flux de transport actif.

Exemple (Node.js / TypeScript) :

```ts

const proc = spawn("codex", ["app-server"], {
  stdio: ["pipe", "pipe", "inherit"],
});
const rl = readline.createInterface({ input: proc.stdout });

const send = (message: unknown) => {
  proc.stdin.write(`${JSON.stringify(message)}\n`);
};

let threadId: string | null = null;

rl.on("line", (line) => {
  const msg = JSON.parse(line) as any;
  console.log("server:", msg);

  if (msg.id === 1 && msg.result?.thread?.id && !threadId) {
    threadId = msg.result.thread.id;
    send({
      method: "turn/start",
      id: 2,
      params: {
        threadId,
        input: [{ type: "text", text: "Summarize this repo." }],
      },
    });
  }
});

send({
  method: "initialize",
  id: 0,
  params: {
    clientInfo: {
      name: "my_product",
      title: "My Product",
      version: "0.1.0",
    },
  },
});
send({ method: "initialized", params: {} });
send({ method: "thread/start", id: 1, params: { model: "gpt-5.6-terra" } });

## Primitives fondamentales

- **Fil** : une conversation entre un utilisateur et l’agent Codex. Les fils contiennent des tours.
- **Tour** : une seule demande de l’utilisateur et le travail de l’agent qui suit. Les tours contiennent des éléments et transmettent des mises à jour incrémentielles en continu.
- **Élément** : une unité d’entrée ou de sortie (message de l’utilisateur, message de l’agent, exécution de commande, modification de fichier, appel d’outil, etc.).

Utilisez les API des fils pour créer, lister ou archiver des conversations. Pilotez une conversation avec les API des tours et suivez sa progression en continu grâce aux notifications de tour.

## Vue d’ensemble du cycle de vie

- **Initialisez une seule fois par connexion** : immédiatement après l’ouverture d’une connexion de transport, envoyez une requête `initialize` avec les métadonnées de votre client, puis émettez `initialized`. Le serveur rejette toute requête sur cette connexion avant cet échange initial.
- **Démarrez ou reprenez un fil** : appelez `thread/start` pour créer une conversation, `thread/resume` pour en reprendre une existante ou `thread/fork` pour créer un nouveau fil à partir de l’historique, avec un nouvel identifiant.
- **Commencez un tour** : appelez `turn/start` avec le `threadId` cible et l’entrée utilisateur. Les champs facultatifs permettent de remplacer le modèle, la personnalité, `cwd`, la politique de bac à sable, etc.
- **Orientez un tour actif** : appelez `turn/steer` pour ajouter une entrée utilisateur au tour en cours sans en créer un nouveau.
- **Recevez les événements en continu** : après `turn/start`, continuez à lire les notifications sur stdout : `thread/archived`, `thread/unarchived`, `item/started`, `item/completed`, `item/agentMessage/delta`, la progression des outils et d’autres mises à jour.
- **Terminez le tour** : le serveur émet `turn/completed` avec l’état final lorsque le modèle termine son travail ou après une annulation via `turn/interrupt`.

## Initialisation

Les clients doivent envoyer une seule requête `initialize` par connexion de transport avant d’appeler toute autre méthode sur cette connexion, puis envoyer une notification `initialized` en guise d’accusé de réception. Les requêtes envoyées avant l’initialisation reçoivent une erreur `Not initialized`, et les appels répétés à `initialize` sur la même connexion renvoient `Already initialized`.

Le serveur renvoie la chaîne d’agent utilisateur qu’il présentera aux services en amont, ainsi que les valeurs `platformFamily` et `platformOs` qui décrivent la cible d’exécution. Définissez `clientInfo` pour identifier votre intégration.

`initialize.params.capabilities` prend également en charge les capacités client suivantes :

- `optOutNotificationMethods` - noms exacts des méthodes de notification à désactiver pour
  cette connexion. La correspondance est exacte, sans caractères génériques ni préfixes ; les noms inconnus
  sont acceptés et ignorés.
- `requestAttestation` - active la réception de la requête `attestation/generate`
  initiée par le serveur. Les hôtes de bureau qui fournissent une attestation aux services en amont répondent par une
  valeur opaque `{ "token": "..." }`.
- `mcpServerOpenaiFormElicitation` - autorise les serveurs MCP en aval à envoyer la
  variante à formulaire étendu de `mcpServer/elicitation/request` proposée par OpenAI.

**Important** : utilisez `clientInfo.name` pour identifier votre client auprès de la plateforme de journaux de conformité. Si vous développez une nouvelle intégration Codex destinée à un usage en entreprise, contactez OpenAI pour qu’elle soit ajoutée à une liste de clients connus. Pour en savoir plus, consultez la [documentation de référence sur les journaux Codex](https://chatgpt.com/public/admin/api-reference#tag/Codex).

Exemple (tiré de l’extension Codex pour VS Code) :

```json
{
  "method": "initialize",
  "id": 0,
  "params": {
    "clientInfo": {
      "name": "codex_vscode",
      "title": "Codex VS Code Extension",
      "version": "0.1.0"
    }
  }
}

Exemple avec désactivation des notifications :

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true,
      "optOutNotificationMethods": ["thread/started", "item/agentMessage/delta"]
    }
  }
}

## Activation de l’API expérimentale

Certaines méthodes et certains champs d’app-server ne sont volontairement accessibles qu’avec la capacité `experimentalApi`.

- Omettez `capabilities` (ou définissez `experimentalApi` sur `false`) pour vous limiter à l’API stable ; le serveur rejette alors les méthodes et les champs expérimentaux.
- Définissez `capabilities.experimentalApi` sur `true` pour activer les méthodes et champs expérimentaux.

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true
    }
  }
}

Si un client envoie une méthode ou un champ expérimental sans avoir activé cette option, app-server le rejette avec le message suivant :

`<descriptor> requires experimentalApi capability`

## Vue d’ensemble de l’API

- `thread/start` - crée un nouveau fil ; émet `thread/started` et vous abonne automatiquement aux événements liés aux tours et aux éléments de ce fil.
- `thread/resume` - rouvre un fil existant à partir de son identifiant pour que les appels ultérieurs à `turn/start` y ajoutent des tours.
- `thread/fork` - forke un fil sous un nouvel identifiant en copiant l’historique stocké. Transmettez `lastTurnId` pour copier l’historique jusqu’à ce tour inclus en omettant les suivants, ou `ephemeral: true` pour forker le fil en mémoire. Émet `thread/started` pour le nouveau fil ; les fils renvoyés incluent `forkedFromId` lorsqu’il est disponible.
- `thread/read` - lit un fil stocké à partir de son identifiant sans le reprendre ; définissez `includeTurns` pour obtenir l’historique complet des tours. Les objets `thread` renvoyés incluent leur état d’exécution (`status`).
- `thread/list` - parcourt page par page les journaux stockés des fils ; prend en charge la pagination par curseur ainsi que les filtres `modelProviders`, `sourceKinds`, `archived`, `isPinned`, `cwd`, `useStateDbOnly`, `searchTerm` et les filtres expérimentaux `parentThreadId` ou `ancestorThreadId`. Les objets `thread` renvoyés incluent leur état d’exécution (`status`).
- `thread/turns/list` - méthode expérimentale ; parcourt page par page l’historique des tours d’un fil stocké sans le reprendre. `itemsView` détermine si les éléments des tours sont omis, résumés ou entièrement chargés.
- `thread/items/list` - méthode expérimentale ; parcourt page par page les éléments enregistrés d’un fil, avec possibilité de limiter les résultats à un seul `turnId`. Le système de stockage actif des fils doit prendre en charge la pagination des éléments.
- `thread/loaded/list` - répertorie les identifiants des fils actuellement chargés en mémoire.
- `thread/name/set` - définit ou met à jour le nom du fil affiché à l’utilisateur, pour un fil chargé ou un journal d’exécution enregistré ; émet `thread/name/updated`.
- `thread/goal/set` - définit l’objectif d’un fil ; émet `thread/goal/updated`.
- `thread/goal/get` - lit l’objectif actuel d’un fil.
- `thread/goal/clear` - efface l’objectif d’un fil ; émet `thread/goal/cleared`.
- `thread/metadata/update` - modifie les métadonnées du fil stockées dans SQLite, notamment les valeurs enregistrées de `gitInfo` et `isPinned`.
- `thread/archive` - déplace le fichier journal d’un fil dans le répertoire d’archivage et tente d’archiver les journaux des fils descendants créés qui ne sont pas déjà archivés ; renvoie `{}` en cas de réussite et émet `thread/archived` pour chaque fil archivé.
- `thread/delete` - supprime définitivement un fil enregistré, actif ou archivé, ainsi que tous ses fils descendants créés ; renvoie `{}` en cas de réussite et émet `thread/deleted` pour chaque fil supprimé.
- `thread/unsubscribe` - désabonne cette connexion des événements liés aux tours et aux éléments du fil. S’il s’agissait du dernier abonné, le serveur retire le fil de la mémoire après un délai de grâce sans activité ni abonné et émet `thread/closed`.
- `thread/unarchive` - restaure le journal d’exécution d’un fil archivé dans le répertoire des sessions actives ; renvoie l’objet `thread` restauré et émet `thread/unarchived`.
- `thread/status/changed` - notification émise lorsque l’état d’exécution (`status`) d’un fil chargé change.
- `thread/compact/start` - déclenche le compactage de l’historique de conversation d’un fil ; renvoie immédiatement `{}` tandis que la progression est diffusée via les notifications `turn/*` et `item/*`.
- `thread/shellCommand` - exécute une commande shell à l’initiative de l’utilisateur dans le cadre d’un fil. La commande s’exécute hors du bac à sable avec un accès complet et n’hérite pas de la politique de bac à sable du fil.
- `thread/backgroundTerminals/clean` - arrête tous les terminaux en arrière-plan en cours d’exécution pour un fil (expérimental ; nécessite `capabilities.experimentalApi`).
- `thread/backgroundTerminals/list` - répertorie les terminaux en arrière-plan en cours d’exécution pour un fil chargé (expérimental ; nécessite `capabilities.experimentalApi`).
- `thread/backgroundTerminals/terminate` - arrête un terminal en arrière-plan en cours d’exécution à partir de son `processId` dans app-server (expérimental ; nécessite `capabilities.experimentalApi`).
- `thread/rollback` - méthode obsolète ; retire les N derniers tours du contexte en mémoire et enregistre durablement un marqueur de retour arrière ; renvoie l’objet `thread` mis à jour.
- `turn/start` - ajoute à un fil une entrée utilisateur ou une sortie d’outil fournie séparément et lance la génération par Codex ; renvoie l’objet `turn` initial et diffuse les événements en continu. Pour `collaborationMode`, `settings.developer_instructions: null` signifie « utiliser les instructions intégrées du mode sélectionné ».
- `thread/inject_items` - ajoute des éléments bruts de l’API Responses à l’historique visible par le modèle d’un fil chargé, sans démarrer de tour utilisateur.
- `turn/steer` - ajoute une entrée utilisateur au tour actif en cours d’un fil ; renvoie le `turnId` accepté.
- `turn/interrupt` - demande l’annulation d’un tour en cours ; la réussite est indiquée par `{}` et le tour se termine avec `status: "interrupted"`.
- `review/start` - lance l’agent de revue de Codex pour un fil ; émet des éléments `enteredReviewMode` et `exitedReviewMode`.
- `command/exec` - exécute une seule commande dans le bac à sable du serveur sans démarrer de fil ni de tour.
- `command/exec/write` - écrit des octets sur `stdin` dans une session `command/exec` en cours d’exécution, ou ferme `stdin`.
- `command/exec/resize` - redimensionne une session `command/exec` en cours d’exécution utilisant un PTY.
- `command/exec/terminate` - arrête une session `command/exec` en cours d’exécution.
- `command/exec/outputDelta` (notification) - émise pour les fragments stdout/stderr encodés en base64 provenant d’une session `command/exec` avec diffusion en continu.
- `process/spawn` - démarre explicitement une session de processus hors du bac à sable de Codex (expérimental ; nécessite `capabilities.experimentalApi`).
- `process/writeStdin` - écrit des octets sur stdin dans une session `process/spawn` en cours d’exécution, ou ferme stdin (expérimental).
- `process/resizePty` - redimensionne une session de processus en cours d’exécution utilisant un PTY (expérimental).
- `process/kill` - arrête une session de processus en cours d’exécution (expérimental).
- `process/outputDelta` et `process/exited` (notifications) - émises pour la sortie du processus diffusée en continu et son statut de sortie (expérimental).
- `model/list` - répertorie les modèles disponibles (définissez `includeHidden: true` pour inclure les entrées avec `hidden: true`), avec leurs options d’effort, le champ facultatif `upgrade` et le champ `inputModalities`.
- `modelProvider/capabilities/read` - lit les limites des capacités du fournisseur pour les combinaisons modèle/fournisseur.
- `experimentalFeature/list` - répertorie les indicateurs de fonctionnalités avec les métadonnées de leur stade du cycle de vie et une pagination par curseur.
- `experimentalFeature/enablement/set` - modifie les paramètres d’exécution en mémoire pour les clés de fonctionnalités prises en charge, telles que `apps` et `plugins`.
- `environment/info` - méthode expérimentale ; se connecte à un environnement d’exécution configuré et renvoie son shell ainsi que son répertoire de travail par défaut.
- `permissionProfile/list` - répertorie les profils de permissions en bêta et indique si les exigences en vigueur les autorisent, avec une pagination par curseur.
- `collaborationMode/list` - répertorie les préréglages des modes de collaboration (expérimental, sans pagination).
- `skills/list` - répertorie les Skills pour une ou plusieurs valeurs de `cwd` (prend en charge `forceReload` et, facultativement, `perCwdExtraUserRoots`).
- `skills/extraRoots/set` - remplace les répertoires racines supplémentaires définis au niveau du processus et utilisés pour découvrir les Skills autonomes, sans enregistrer ces répertoires de manière persistante.
- `skills/changed` (notification) - émise lorsque les fichiers locaux de Skills surveillés sont modifiés.
- `hooks/list` - répertorie les Hooks de cycle de vie détectés pour une ou plusieurs valeurs de `cwd`.
- `marketplace/add` - ajoute une Marketplace distante de plugins et l’enregistre dans la configuration Marketplace de l’utilisateur.
- `marketplace/remove` - supprime une Marketplace configurée ainsi que son répertoire racine installé, le cas échéant.
- `marketplace/upgrade` - actualise une Marketplace Git configurée, ou toutes les Marketplaces Git configurées si vous omettez le nom de la Marketplace.
- `plugin/list` - en cours de développement ; répertorie les Marketplaces de plugins détectées et l’état des plugins, notamment les métadonnées des politiques d’installation et d’authentification, les erreurs de chargement des Marketplaces, les identifiants des plugins mis en avant et les métadonnées de leurs sources locales, Git, issues d’un registre de paquets ou distantes. Les résumés peuvent inclure la valeur distante `version`, la valeur locale `localVersion`, des icônes structurées pour les thèmes clair et sombre, ainsi que `installPolicySource`, qui peut valoir `null`, `WORKSPACE_SETTING` ou `IMPLICIT_CANONICAL_APP` pour les entrées distantes actuelles. N’appelez pas encore cette méthode depuis des clients en production.
- `plugin/read` - en cours de développement ; lit un plugin à partir de son nom et du chemin de la Marketplace ou du nom de la Marketplace distante, avec les Skills et applications fournis, les noms des serveurs MCP et une valeur `shareUrl` pour le plugin distant lorsque le catalogue distant en fournit une. N’appelez pas encore cette méthode depuis des clients en production.
- `plugin/install` - en cours de développement ; installe un plugin à partir d’un chemin de Marketplace ou du nom d’une Marketplace distante. N’appelez pas encore cette méthode depuis des clients en production.
- `plugin/uninstall` - en cours de développement ; désinstalle un plugin installé. N’appelez pas encore cette méthode depuis des clients en production.
- `plugin/skill/read` - lit à la demande le contenu Markdown d’un Skill de plugin distant à partir de la Marketplace distante, de l’identifiant du plugin et du nom du Skill.
- `app/installed` - lit l’état d’exécution des applications installées, notamment, pour chacune, si elle est effectivement activée et peut être appelée.
- `app/list` - répertorie les applications disponibles (connecteurs), avec une pagination et des métadonnées indiquant si elles sont accessibles et activées.
- `app/read` - récupère les métadonnées et, en option, des résumés d’outils destinés uniquement à l’affichage pour des identifiants d’applications donnés.
- `skills/config/write` - active ou désactive les skills à partir de leur chemin.
- `mcpServer/oauth/login` - démarre une connexion OAuth pour un serveur MCP configuré ; renvoie une URL d’autorisation et émet `mcpServer/oauthLogin/completed` une fois l’opération terminée.
- `tool/requestUserInput` - pose à l’utilisateur 1 à 3 questions courtes pour un appel d’outil (expérimental) ; les questions peuvent définir `isOther` pour proposer une option de réponse libre.
- `mcpServer/elicitation/request` (requête du serveur) - demande au client des données de formulaire structurées ou la confirmation d’un parcours via URL demandé par un serveur MCP.
- `item/permissions/requestApproval` (requête du serveur) - demande au client d’accorder un sous-ensemble des autorisations réseau ou d’accès au système de fichiers demandées par l’outil intégré `request_permissions`.
- `config/mcpServer/reload` - recharge depuis le disque la configuration des serveurs MCP et met en file d’attente une actualisation des fils de discussion chargés.
- `mcpServerStatus/list` - répertorie les serveurs MCP, les outils, les ressources et l’état de l’authentification (pagination par curseur avec limite). Utilisez `detail: "full"` pour obtenir toutes les données ou `detail: "toolsAndAuthOnly"` pour omettre les ressources.
- `mcpServer/resource/read` - lit une seule ressource MCP via un serveur MCP initialisé.
- `mcpServer/tool/call` - appelle un outil sur le serveur MCP configuré pour un fil de discussion.
- `mcpServer/startupStatus/updated` (notification) - est émise lorsque l’état de démarrage d’un serveur MCP configuré change pour un fil de discussion chargé.
- `windowsSandbox/setupStart` - lance la configuration du bac à sable Windows en mode `elevated` ou `unelevated` ; renvoie rapidement une réponse, puis émet `windowsSandbox/setupCompleted`.
- `feedback/upload` - envoie un rapport de retour d’expérience (classification + motif/journaux facultatifs + identifiant de conversation, ainsi que des pièces jointes `extraLogFiles` facultatives).
- `config/read` - récupère la configuration effective sur le disque après résolution des différentes couches de configuration.
- `externalAgentConfig/detect` - détecte les artefacts d’agents externes pouvant être migrés, à l’aide de `includeHome` et du paramètre facultatif `cwds` ; chaque élément détecté inclut `cwd` (`null` pour le répertoire personnel).
- `externalAgentConfig/import` - applique les éléments de migration d’agents externes sélectionnés en transmettant explicitement `migrationItems` avec `cwd` (`null` pour le répertoire personnel). Les types d’éléments pris en charge incluent la configuration, les skills, `AGENTS.md`, les plugins, la configuration des serveurs MCP, les sous-agents, les hooks, les commandes et les sessions ; les importations non vides émettent `externalAgentConfig/import/progress` et `externalAgentConfig/import/completed` à mesure que les opérations se terminent. Les importations de plugins et de sessions peuvent se terminer de manière asynchrone.
- `config/value/write` - écrit une seule paire clé/valeur de configuration dans le fichier `config.toml` de l’utilisateur sur le disque.
- `config/batchWrite` - applique de façon atomique les modifications de configuration au fichier `config.toml` de l’utilisateur sur le disque.
- `configRequirements/read` - récupère les exigences depuis `requirements.toml` et/ou MDM, notamment les valeurs exactes de la configuration gérée, les listes d’autorisation, les valeurs épinglées de `featureRequirements` et les exigences réseau (ou `null` si vous n’en avez configuré aucune).
- `fs/readFile`, `fs/writeFile`, `fs/createDirectory`, `fs/getMetadata`, `fs/readDirectory`, `fs/remove`, `fs/copy`, `fs/watch`, `fs/unwatch` et `fs/changed` (notification) - effectuent des opérations sur des chemins absolus du système de fichiers via l’API de système de fichiers v2 d’app-server.

Les résumés de plugins incluent un champ `source` de type union. Les plugins locaux renvoient
`{ "type": "local", "path": ... }`, les entrées de marketplace basées sur Git renvoient
`{ "type": "git", "url": ..., "path": ..., "refName": ..., "sha": ... }`,
les entrées de registre de paquets renvoient
`{ "type": "npm", "package": ..., "version": ..., "registry": ... }`, et
les entrées du catalogue distant renvoient `{ "type": "remote" }`. Pour les entrées de catalogue
disponibles uniquement à distance, `PluginMarketplaceEntry.path` peut valoir `null` ; transmettez
`remoteMarketplaceName` au lieu de `marketplacePath` lors de la lecture ou de l’installation
de ces plugins.

## Modèles

### Répertoriez les modèles (`model/list`)

Appelez `model/list` pour découvrir les modèles disponibles et leurs capacités avant d’afficher les sélecteurs de modèle ou de personnalité.

```json
{ "method": "model/list", "id": 6, "params": { "limit": 20, "includeHidden": false } }
{ "id": 6, "result": {
  "data": [{
    "id": "gpt-5.6-sol",
    "model": "gpt-5.6-sol",
    "displayName": "GPT-5.6-Sol",
    "hidden": false,
    "defaultReasoningEffort": "low",
    "supportedReasoningEfforts": [{
      "reasoningEffort": "low",
      "description": "Fast responses with lighter reasoning"
    }],
    "inputModalities": ["text", "image"],
    "supportsPersonality": true,
    "isDefault": true
  }],
  "nextCursor": null
} }

Chaque entrée de modèle peut inclure :

- `supportedReasoningEfforts` - options d’effort de raisonnement prises en charge par le modèle.
- `defaultReasoningEffort` - niveau d’effort de raisonnement par défaut suggéré aux clients.
- `upgrade` - identifiant facultatif du modèle recommandé pour la mise à niveau, utilisé dans les prompts de migration des clients.
- `upgradeInfo` - métadonnées facultatives de mise à niveau pour les prompts de migration des clients.
- `hidden` - indique si le modèle est masqué dans la liste par défaut du sélecteur.
- `inputModalities` - types d’entrée pris en charge par le modèle (par exemple `text`, `image`).
- `supportsPersonality` - indique si le modèle prend en charge les instructions propres à une personnalité, telles que `/personality`.
- `isDefault` - indique si le modèle est celui recommandé par défaut.

Par défaut, `model/list` renvoie uniquement les modèles visibles dans le sélecteur. Définissez `includeHidden: true` si vous avez besoin de la liste complète et souhaitez la filtrer côté client à l’aide de `hidden`.

Lorsque `inputModalities` est absent (anciens catalogues de modèles), considérez que sa valeur est `["text", "image"]` afin de préserver la rétrocompatibilité.

### Répertoriez les fonctionnalités expérimentales (`experimentalFeature/list`)

Utilisez ce point de terminaison pour découvrir les indicateurs de fonctionnalités, leurs métadonnées et leur stade dans le cycle de vie :

```json
{ "method": "experimentalFeature/list", "id": 7, "params": { "limit": 20 } }
{ "id": 7, "result": {
  "data": [{
    "name": "unified_exec",
    "stage": "beta",
    "displayName": "Unified exec",
    "description": "Use the unified PTY-backed execution tool.",
    "announcement": "Beta rollout for improved command execution reliability.",
    "enabled": false,
    "defaultEnabled": false
  }],
  "nextCursor": null
} }

`stage` peut valoir `beta`, `underDevelopment`, `stable`, `deprecated` ou `removed`. Pour les indicateurs qui ne sont pas en bêta, `displayName`, `description` et `announcement` peuvent valoir `null`.

### Inspectez un environnement d’exécution (expérimental)

Utilisez `environment/info` pour inspecter un environnement distant configuré avant
de commencer à y travailler. Cette méthode nécessite `capabilities.experimentalApi = true`.

```json
{ "method": "environment/info", "id": 8, "params": { "environmentId": "devbox" } }
{ "id": 8, "result": {
  "shell": { "name": "zsh", "path": "/bin/zsh" },
  "cwd": "file:///workspace/project"
} }

`cwd` peut valoir `null`. Lorsqu’il est renseigné, il s’agit d’un URI `file:` canonique qui utilise la
syntaxe de chemin native de l’environnement. Les identifiants d’environnement inconnus et les échecs de connexion ou
de protocole entraînent des erreurs de requête.

## Fils de discussion

- `thread/read` lit un fil de discussion enregistré sans s’y abonner ; définissez `includeTurns` pour inclure les tours.
- `thread/turns/list` est expérimental et parcourt page par page l’historique des tours d’un fil de discussion enregistré sans
  le reprendre. Utilisez `itemsView` pour choisir si les éléments des tours doivent être omis,
  résumés ou chargés intégralement.
- `thread/items/list` est expérimental et parcourt page par page les éléments enregistrés d’un fil de discussion, avec la possibilité de limiter les résultats à un seul tour.
- `thread/list` prend en charge la pagination par curseur, ainsi que les filtres `modelProviders`, `sourceKinds`, `archived`, `isPinned`, `cwd`, `useStateDbOnly`, `searchTerm` et les filtres expérimentaux `parentThreadId` ou `ancestorThreadId`.
- `thread/loaded/list` renvoie les identifiants des fils de discussion actuellement en mémoire.
- `thread/archive` déplace le journal JSONL enregistré du fil de discussion vers le répertoire d’archives et tente d’archiver les journaux encore non archivés des fils de discussion descendants créés à partir de ce fil.
- `thread/delete` supprime définitivement un fil de discussion enregistré, actif ou archivé, ainsi que les fils de discussion descendants créés à partir de ce fil.
- `thread/metadata/update` met à jour partiellement les métadonnées stockées du fil de discussion, notamment les valeurs enregistrées de `gitInfo` et `isPinned`.
- `thread/unsubscribe` met fin à l’abonnement de la connexion actuelle à un fil de discussion chargé et peut déclencher `thread/closed` après un délai de tolérance sans activité.
- `thread/unarchive` restaure le journal d’exécution d’un fil de discussion archivé dans le répertoire des sessions actives.
- `thread/compact/start` déclenche le compactage et renvoie immédiatement `{}`.
- La méthode `thread/rollback` est obsolète. Elle supprime les N derniers tours du contexte en mémoire et inscrit un marqueur de retour arrière dans le journal JSONL enregistré du fil de discussion.
- `thread/inject_items` ajoute des éléments bruts de l’API Responses à l’historique visible par le modèle d’un fil de discussion chargé, sans démarrer de tour utilisateur.

### Démarrez ou reprenez un fil de discussion

Démarrez un nouveau fil de discussion lorsque vous avez besoin d’une nouvelle conversation Codex.

```json
{ "method": "thread/start", "id": 10, "params": {
  "model": "gpt-5.6-terra",
  "cwd": "/Users/me/project",
  "approvalPolicy": "never",
  "sandbox": "workspaceWrite",
  "personality": "friendly",
  "serviceName": "my_app_server_client"
} }
{ "id": 10, "result": {
  "thread": {
    "id": "thr_123",
    "sessionId": "thr_123",
    "preview": "",
    "ephemeral": false,
    "modelProvider": "openai",
    "createdAt": 1730910000
  }
} }
{ "method": "thread/started", "params": { "thread": { "id": "thr_123" } } }

`serviceName` est facultatif. Définissez-le si vous souhaitez qu’app-server associe le nom du service de votre intégration aux métriques du fil de discussion.

`thread/start`, `thread/resume` et `thread/fork` renvoient
`instructionSources`, un tableau contenant les chemins des fichiers d’instructions chargés. Chaque chemin utilise
la syntaxe de chemin absolu native de son environnement source, y compris pour les environnements
distants.

Les clients expérimentaux peuvent attribuer à `historyMode` dans `thread/start` la valeur `"legacy"`
(par défaut) ou `"paginated"`. La création de fils de discussion avec pagination n’est pas encore prise en charge
et renvoie l’erreur JSON-RPC `-32601`. App-server peut répertorier et lire des résumés pour
les enregistrements paginés existants, mais la lecture de l’historique complet, la pagination des tours et la reprise
sont refusées par sécurité tant que l’historique paginé n’est pas pris en charge.

Les clients bêta qui activent `capabilities.experimentalApi` peuvent transmettre l’identifiant d’un profil d’autorisations nommé
dans `permissions`, à la place de l’ancien champ `sandbox`.
N’envoyez pas `permissions` et `sandbox` ensemble. Utilisez
`permissionProfile/list` avec le `cwd` du projet pour découvrir les profils disponibles
et vérifier si les exigences gérées autorisent chacun d’eux.

`thread.sessionId` identifie la racine de l’arborescence de la session actuellement active. Les fils de discussion racines
utilisent leur propre identifiant de fil comme identifiant de session ; les fils forkés conservent l’identifiant de session
de leur racine d’origine. Les clients devraient lire l’identifiant de session dans
`thread.sessionId` au lieu de le déduire de l’identifiant du fil.

Pour poursuivre une session enregistrée, appelez `thread/resume` avec le `thread.id` que vous avez enregistré précédemment. La structure de la réponse est identique à celle de `thread/start`. Vous pouvez également transmettre les mêmes paramètres de remplacement de configuration que ceux pris en charge par `thread/start`, comme `personality` :

```json
{ "method": "thread/resume", "id": 11, "params": {
  "threadId": "thr_123",
  "personality": "friendly"
} }
{ "id": 11, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false } } }

La simple reprise d’un fil de discussion ne met pas à jour `thread.updatedAt` (ni l’horodatage de modification du fichier du journal d’exécution). L’horodatage est mis à jour lorsque vous démarrez un tour.

Si, dans la configuration, vous marquez un serveur MCP activé comme `required` et que son initialisation échoue, `thread/start` et `thread/resume` échouent au lieu de poursuivre sans ce serveur.

Le champ `dynamicTools` de `thread/start` est expérimental (nécessite `capabilities.experimentalApi = true`). Codex conserve ces outils dynamiques dans les métadonnées du journal du fil et les restaure lors de `thread/resume` si vous ne fournissez pas de nouveaux outils dynamiques.

Si vous reprenez un fil avec un modèle différent de celui enregistré dans le journal, Codex émet un avertissement et applique une instruction ponctuelle de changement de modèle au tour suivant.

### Gérez l’objectif d’un fil

Utilisez `thread/goal/set`, `thread/goal/get` et `thread/goal/clear` pour gérer l’état persistant
de l’objectif, également accessible via `/goal` dans la TUI.

```json
{ "method": "thread/goal/set", "id": 13, "params": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000
} }
{ "id": 13, "result": { "goal": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000,
  "tokensUsed": 0,
  "timeUsedSeconds": 0
} } }
{ "method": "thread/goal/updated", "params": {
  "threadId": "thr_123",
  "goal": {
    "threadId": "thr_123",
    "objective": "Finish the migration and keep tests green",
    "status": "active",
    "tokenBudget": 40000,
    "tokensUsed": 0,
    "timeUsedSeconds": 0
  }
} }

Le texte de l’objectif ne doit pas être vide et doit comporter au maximum 4 000 caractères. Fournir un nouvel
objectif remplace l’objectif existant et réinitialise la comptabilisation de l’utilisation. Si vous fournissez l’objectif actuel
dont l’état n’est pas terminal, ou omettez `objective`, vous mettez à jour l’état ou le budget de tokens
tout en conservant l’historique d’utilisation.

Pour forker une session stockée, appelez `thread/fork` avec `thread.id`. Cela crée un nouvel identifiant de fil et émet une notification `thread/started` pour celui-ci. Transmettez
`lastTurnId` pour copier l’historique jusqu’à ce tour inclus et omettre les tours
ultérieurs :

```json
{ "method": "thread/fork", "id": 12, "params": { "threadId": "thr_123", "lastTurnId": "turn_456" } }
{ "id": 12, "result": { "thread": { "id": "thr_456", "sessionId": "thr_123", "forkedFromId": "thr_123" } } }
{ "method": "thread/started", "params": { "thread": { "id": "thr_456" } } }

App-server rejette `lastTurnId` s’il correspond à un tour en cours. Si vous omettez ce champ alors que le
fil source est au milieu d’un tour, le fil forké enregistre un marqueur d’interruption au lieu de
conserver un tour partiel sans marqueur.

Transmettez `ephemeral: true` pour créer un fil forké en mémoire sans l’ajouter aux listes de
fils stockés :

```json
{
  "method": "thread/fork",
  "id": 13,
  "params": {
    "threadId": "thr_123",
    "ephemeral": true
  }
}
{
  "id": 13,
  "result": {
    "thread": {
      "id": "thr_789",
      "sessionId": "thr_789",
      "forkedFromId": "thr_123",
      "ephemeral": true
    }
  }
}

Pour créer des fils forkés éphémères à partir de fils paginés, fournissez également `excludeTurns: true`. Ce
champ est expérimental et nécessite `capabilities.experimentalApi = true`.

Lorsqu’un titre de fil visible par l’utilisateur est défini, app-server renseigne `thread.name` dans les réponses de `thread/list`, `thread/read`, `thread/resume`, `thread/unarchive` et `thread/rollback`. Les réponses de `thread/start` et `thread/fork` peuvent omettre `name` (ou renvoyer `null`) jusqu’à ce qu’un titre soit défini ultérieurement.

### Lisez un fil stocké (sans le reprendre)

Utilisez `thread/read` pour obtenir les données stockées d’un fil sans le reprendre ni vous abonner à ses événements.

- `includeTurns` : s’il vaut `true`, la réponse inclut les tours du fil ; s’il vaut `false` ou est omis, vous obtenez uniquement le résumé du fil.
- Les objets `thread` renvoyés incluent l’état d’exécution `status` (`notLoaded`, `idle`, `systemError` ou `active` avec `activeFlags`).

```json
{ "method": "thread/read", "id": 19, "params": { "threadId": "thr_123", "includeTurns": true } }
{ "id": 19, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false, "status": { "type": "notLoaded" }, "turns": [] } } }

Contrairement à `thread/resume`, `thread/read` ne charge pas le fil en mémoire et n’émet pas `thread/started`.

### Listez les tours d’un fil

`thread/turns/list` est expérimental. Utilisez cette méthode pour parcourir par pages l’historique des tours d’un fil stocké sans le reprendre. Par défaut, les résultats sont classés du plus récent au plus ancien afin que les clients puissent récupérer les tours antérieurs avec `nextCursor`. La réponse inclut également `backwardsCursor` ; transmettez cette valeur comme `cursor`, avec `sortDirection: "asc"`, pour récupérer les tours plus récents que le premier élément de la page précédente.

`itemsView` détermine le niveau de détail des données incluses dans la réponse sur les éléments des tours :

- `notLoaded` omet les éléments.
- `summary` renvoie des données résumées sur les éléments et constitue la valeur par défaut lorsque le champ est omis.
- `full` renvoie les données complètes des éléments.

```json
{ "method": "thread/turns/list", "id": 20, "params": {
  "threadId": "thr_123",
  "limit": 50,
  "sortDirection": "desc",
  "itemsView": "summary"
} }
{ "id": 20, "result": {
  "data": [],
  "nextCursor": "older-turns-cursor-or-null",
  "backwardsCursor": "newer-turns-cursor-or-null"
} }

`thread/items/list` est également expérimental. Il permet de parcourir par pages les éléments enregistrés sans
reprendre le fil. Transmettez `turnId` pour limiter les résultats à un seul tour, ou omettez-le
pour parcourir les éléments de tout le fil. Le système de stockage des fils actuellement utilisé doit prendre en charge la
pagination des éléments ; sinon, le serveur renvoie une erreur indiquant que la méthode n’est pas prise en charge.

### Listez les fils (avec pagination et filtres)

`thread/list` permet d’afficher une interface d’historique. Par défaut, les résultats sont triés par `createdAt`, du plus récent au plus ancien. Les filtres s’appliquent avant la pagination. Transmettez les paramètres suivants dans n’importe quelle combinaison :

- `cursor` : chaîne opaque issue d’une réponse précédente ; omettez ce paramètre pour la première page.
- `limit` : si vous ne le définissez pas, le serveur utilise par défaut une taille de page raisonnable.
- `sortKey` : `created_at` (par défaut), `updated_at` ou `recency_at`.
- `sortDirection` : `desc` (par défaut) ou `asc`.
- `modelProviders` : limite les résultats à certains fournisseurs ; si ce paramètre n’est pas défini, vaut null ou correspond à un tableau vide, tous les fournisseurs sont inclus.
- `sourceKinds` : limite les résultats à certaines sources de fils. Si ce paramètre est omis ou vaut `[]`, le serveur ne retient par défaut que les sources interactives : `cli` et `vscode`.
- `archived` : s’il vaut `true`, renvoie uniquement les fils archivés. S’il vaut `false` ou est omis, renvoie les fils non archivés (comportement par défaut).
- `isPinned` : lorsqu’il est fourni, renvoie uniquement les fils dont l’état d’épinglage enregistré correspond à la valeur fournie. Omettez-le pour renvoyer les fils épinglés et non épinglés.
- `cwd` : limite les résultats aux fils dont le répertoire de travail courant de la session correspond exactement à ce chemin ou à l’un des chemins d’un tableau. Les chemins relatifs sont résolus à partir du répertoire de travail du processus app-server.
- `useStateDbOnly` : s’il vaut `true`, renvoie les résultats de la base de données d’état sans analyser les journaux JSONL des fils pour réparer les métadonnées. Omettez ce paramètre ou transmettez `false` pour appliquer le comportement par défaut d’analyse et de réparation.
- `searchTerm` : limite les résultats aux fils dont le titre extrait contient ce fragment de texte en respectant la casse.
- `parentThreadId` : limite les résultats aux fils enfants directs du fil parent indiqué. Ce filtre est expérimental et nécessite `capabilities.experimentalApi = true`.
- `ancestorThreadId` : limite les résultats aux fils descendants créés à partir du fil indiqué, quelle que soit leur profondeur. Ce filtre est expérimental et nécessite `capabilities.experimentalApi = true` ; ne l’associez pas à `parentThreadId`.

`sourceKinds` accepte les valeurs suivantes :

- `cli`
- `vscode`
- `exec`
- `appServer`
- `subAgent`
- `subAgentReview`
- `subAgentCompact`
- `subAgentThreadSpawn`
- `subAgentOther`
- `unknown`

Exemple :

```json
{ "method": "thread/list", "id": 20, "params": {
  "cursor": null,
  "limit": 25,
  "sortKey": "created_at"
} }
{ "id": 20, "result": {
  "data": [
    { "id": "thr_a", "preview": "Create a TUI", "ephemeral": false, "isPinned": true, "modelProvider": "openai", "createdAt": 1730831111, "updatedAt": 1730831111, "name": "TUI prototype", "status": { "type": "notLoaded" } },
    { "id": "thr_b", "preview": "Fix tests", "ephemeral": false, "isPinned": false, "modelProvider": "openai", "createdAt": 1730750000, "updatedAt": 1730750000, "status": { "type": "notLoaded" } }
  ],
  "nextCursor": "opaque-token-or-null"
} }

Lorsque `nextCursor` vaut `null`, vous avez atteint la dernière page.

### Mettez à jour les métadonnées stockées d’un fil

Utilisez `thread/metadata/update` pour modifier les métadonnées stockées d’un fil sans
le reprendre. Définissez `isPinned` pour épingler ou désépingler le fil, ou mettez à jour `gitInfo` pour modifier les
métadonnées Git enregistrées. Les champs omis restent inchangés ; une valeur `null` explicite efface la
valeur enregistrée d’une métadonnée Git.

```json
{ "method": "thread/metadata/update", "id": 21, "params": {
  "threadId": "thr_123",
  "isPinned": true,
  "gitInfo": { "branch": "feature/sidebar-pr" }
} }
{ "id": 21, "result": {
  "thread": {
    "id": "thr_123",
    "isPinned": true,
    "gitInfo": { "sha": null, "branch": "feature/sidebar-pr", "originUrl": null }
  }
} }

### Suivez les changements d’état d’un fil

`thread/status/changed` est émis chaque fois que l’état d’exécution d’un fil chargé change. La charge utile inclut `threadId` et la nouvelle valeur de `status`.

```json
{
  "method": "thread/status/changed",
  "params": {
    "threadId": "thr_123",
    "status": { "type": "active", "activeFlags": ["waitingOnApproval"] }
  }
}

### Listez les fils chargés

`thread/loaded/list` renvoie les identifiants des fils actuellement chargés en mémoire.

```json
{ "method": "thread/loaded/list", "id": 21 }
{ "id": 21, "result": { "data": ["thr_123", "thr_456"] } }

### Désabonnez-vous d’un fil chargé

`thread/unsubscribe` supprime l’abonnement de la connexion actuelle à un fil. Le statut de la réponse prend l’une des valeurs suivantes :

- `unsubscribed` lorsque la connexion était abonnée et que son abonnement est désormais supprimé.
- `notSubscribed` lorsque la connexion n’était pas abonnée à ce fil.
- `notLoaded` lorsque le fil n’est pas chargé.

S’il s’agissait du dernier abonné, le serveur conserve le fil en mémoire jusqu’à ce que celui-ci soit resté 30 minutes sans abonné ni activité. À l’expiration de ce délai de grâce, app-server décharge le fil et émet une notification `thread/status/changed` signalant le passage à `notLoaded`, ainsi que `thread/closed`.

```json
{ "method": "thread/unsubscribe", "id": 22, "params": { "threadId": "thr_123" } }
{ "id": 22, "result": { "status": "unsubscribed" } }

Si le fil expire par la suite :

```json
{ "method": "thread/status/changed", "params": {
    "threadId": "thr_123",
    "status": { "type": "notLoaded" }
} }
{ "method": "thread/closed", "params": { "threadId": "thr_123" } }

### Archivez un fil

Utilisez `thread/archive` pour déplacer le journal persistant du fil (stocké sur disque sous forme de fichier JSONL) dans le répertoire des sessions archivées. Lors de l’archivage, le serveur tente aussi d’archiver les fils descendants créés à partir de ce fil et qui ne sont pas déjà archivés.

```json
{ "method": "thread/archive", "id": 22, "params": { "threadId": "thr_b" } }
{ "id": 22, "result": {} }
{ "method": "thread/archived", "params": { "threadId": "thr_b" } }
{ "method": "thread/archived", "params": { "threadId": "thr_child" } }

Les fils archivés n’apparaîtront pas dans les appels ultérieurs à `thread/list`, sauf si vous transmettez `archived: true`. Le serveur émet une notification `thread/archived` pour chaque fil qu’il archive effectivement ; si un fil descendant créé à partir de celui-ci ne peut pas être archivé, la requête peut tout de même aboutir sans notification d’archivage pour ce descendant.

### Supprimez un fil

Utilisez `thread/delete` pour supprimer définitivement un fil persistant actif ou archivé
ainsi que les fils descendants créés à partir de celui-ci. Le serveur supprime les fichiers de journal existants et
les métadonnées associées avant de renvoyer une réponse de réussite ; les fichiers de journal manquants sont considérés
comme déjà supprimés. Les fils racines éphémères ne peuvent pas être supprimés.

```json
{ "method": "thread/delete", "id": 23, "params": { "threadId": "thr_b" } }
{ "id": 23, "result": {} }
{ "method": "thread/deleted", "params": { "threadId": "thr_b" } }
{ "method": "thread/deleted", "params": { "threadId": "thr_child" } }

### Désarchivez un fil

Utilisez `thread/unarchive` pour replacer le journal d’un fil archivé dans le répertoire des sessions actives.

```json
{ "method": "thread/unarchive", "id": 24, "params": { "threadId": "thr_b" } }
{ "id": 24, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes" } } }
{ "method": "thread/unarchived", "params": { "threadId": "thr_b" } }

### Déclenchez le compactage d’un fil

Utilisez `thread/compact/start` pour déclencher le compactage manuel de l’historique d’un fil. La requête renvoie immédiatement `{}`.

App-server émet des informations de progression sous forme de notifications standard `turn/*` et `item/*` pour le même `threadId`, notamment le cycle de vie d’un élément `contextCompaction` (`item/started`, puis `item/completed`).

```json
{ "method": "thread/compact/start", "id": 25, "params": { "threadId": "thr_b" } }
{ "id": 25, "result": {} }

### Exécutez une commande shell dans un fil

Utilisez `thread/shellCommand` pour les commandes shell lancées par l’utilisateur et associées à un fil. La requête renvoie immédiatement `{}`, tandis que la progression est diffusée via les notifications standard `turn/*` et `item/*`.

Cette API s’exécute hors du bac à sable avec un accès complet et n’hérite pas de la politique du bac à sable du fil. Les clients ne devraient l’exposer que pour les commandes explicitement lancées par l’utilisateur.

Si le fil comporte déjà un tour actif, la commande s’exécute comme une action auxiliaire de ce tour et sa sortie mise en forme est injectée dans le flux de messages du tour. Si le fil est inactif, app-server démarre un tour autonome pour la commande shell.

Définissez `timeoutMs` pour limiter la durée d’exécution en millisecondes. Si vous l’omettez ou passez
`null`, la valeur par défaut d’une heure s’applique. `0` demande une expiration immédiate du délai ; les valeurs négatives
sont rejetées. Ce délai ne retarde pas l’accusé de réception RPC, qui est immédiat.

```json
{ "method": "thread/shellCommand", "id": 26, "params": { "threadId": "thr_b", "command": "git status --short", "timeoutMs": 10000 } }
{ "id": 26, "result": {} }

### Arrêtez les terminaux en arrière-plan

Utilisez `thread/backgroundTerminals/clean` pour arrêter tous les terminaux en arrière-plan en cours d’exécution associés à un fil. Cette méthode est expérimentale et nécessite `capabilities.experimentalApi = true`.

```json
{ "method": "thread/backgroundTerminals/clean", "id": 27, "params": { "threadId": "thr_b" } }
{ "id": 27, "result": {} }

Utilisez `thread/backgroundTerminals/list` pour examiner les terminaux en arrière-plan en cours d’exécution
d’un fil chargé. La requête prend en charge la pagination standard avec `cursor` et `limit`,
et la valeur `processId` renvoyée correspond à l’identifiant de processus d’app-server. Cette
méthode est expérimentale et nécessite `capabilities.experimentalApi = true` :

```json
{ "method": "thread/backgroundTerminals/list", "id": 28, "params": { "threadId": "thr_b" } }
{ "id": 28, "result": { "data": [
  {
    "itemId": "item_456",
    "processId": "42",
    "command": "python3 -m http.server",
    "cwd": "/workspace",
    "osPid": null,
    "cpuPercent": null,
    "rssKb": null
  }
], "nextCursor": null } }

Utilisez `thread/backgroundTerminals/terminate` avec cette valeur de `processId` pour arrêter un
terminal en arrière-plan. Cette méthode est expérimentale et nécessite
`capabilities.experimentalApi = true` :

```json
{ "method": "thread/backgroundTerminals/terminate", "id": 29, "params": { "threadId": "thr_b", "processId": "42" } }
{ "id": 29, "result": { "terminated": true } }

### Annulez les tours récents

La méthode `thread/rollback` est obsolète et sera supprimée. Elle retire les
`numTurns` dernières entrées du contexte en mémoire et enregistre un marqueur de retour arrière dans
le journal de déroulement. L’objet `thread` renvoyé contient le champ `turns` renseigné après le
retour arrière.

```json
{ "method": "thread/rollback", "id": 30, "params": { "threadId": "thr_b", "numTurns": 1 } }
{ "id": 30, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }

## Tours de conversation

Le champ `input` accepte une liste d’éléments :

- `{ "type": "text", "text": "Explain this diff" }`
- `{ "type": "image", "url": "https://.../design.png" }`
- `{ "type": "localImage", "path": "/tmp/screenshot.png" }`

Vous pouvez redéfinir les paramètres de configuration pour chaque tour (modèle, niveau d’effort, personnalité, `cwd`, politique du bac à sable, résumé). Lorsqu’ils sont spécifiés, ces paramètres deviennent les valeurs par défaut pour les tours suivants du même fil. `outputSchema` s’applique uniquement au tour en cours. Pour `sandboxPolicy.type = "externalSandbox"`, définissez `networkAccess` sur `restricted` ou `enabled` ; pour `workspaceWrite`, `networkAccess` reste une valeur booléenne.

Pour `turn/start.collaborationMode`, `settings.developer_instructions: null` signifie « utiliser les instructions intégrées du mode sélectionné », et non effacer les instructions du mode.

### Accès en lecture dans le bac à sable (`ReadOnlyAccess`)

`sandboxPolicy` prend en charge des contrôles explicites de l’accès en lecture :

- `readOnly` : champ `access` facultatif (`{ "type": "fullAccess" }` par défaut, ou accès limité à certains répertoires racines).
- `workspaceWrite` : champ `readOnlyAccess` facultatif (`{ "type": "fullAccess" }` par défaut, ou accès limité à certains répertoires racines).

Structure de l’accès en lecture restreint :

```json
{
  "type": "restricted",
  "includePlatformDefaults": true,
  "readableRoots": ["/Users/me/shared-read-only"]
}

Sur macOS, `includePlatformDefaults: true` ajoute aux sessions à accès en lecture restreint une politique Seatbelt par défaut soigneusement sélectionnée pour la plateforme. Cela améliore la compatibilité des outils sans autoriser un accès général à l’ensemble de `/System`.

Exemples :

```json
{ "type": "readOnly", "access": { "type": "fullAccess" } }

```json
{
  "type": "workspaceWrite",
  "writableRoots": ["/Users/me/project"],
  "readOnlyAccess": {
    "type": "restricted",
    "includePlatformDefaults": true,
    "readableRoots": ["/Users/me/shared-read-only"]
  },
  "networkAccess": false
}

### Démarrez un tour

```json
{ "method": "turn/start", "id": 30, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Run tests" } ],
  "cwd": "/Users/me/project",
  "approvalPolicy": "unlessTrusted",
  "sandboxPolicy": {
    "type": "workspaceWrite",
    "writableRoots": ["/Users/me/project"],
    "networkAccess": true
  },
  "model": "gpt-5.6-terra",
  "effort": "medium",
  "summary": "concise",
  "personality": "friendly",
  "outputSchema": {
    "type": "object",
    "properties": { "answer": { "type": "string" } },
    "required": ["answer"],
    "additionalProperties": false
  }
} }
{ "id": 30, "result": { "turn": { "id": "turn_456", "status": "inProgress", "items": [], "error": null } } }

Pour démarrer un tour avec la sortie d’un outil exécuté par votre client, passez `toolOutput`
avec un champ `name` non vide, un champ `namespace` facultatif et un champ `output` contenant une chaîne ou
un tableau d’éléments de contenu. Définissez `input` sur un tableau vide ; vous ne pouvez pas combiner
`toolOutput` avec une entrée utilisateur non vide.

```json
{
  "method": "turn/start",
  "id": 31,
  "params": {
    "threadId": "thr_123",
    "input": [],
    "toolOutput": {
      "name": "run_tests",
      "namespace": null,
      "output": "All 42 tests passed."
    }
  }
}

La sortie conserve son statut de sortie d’outil dans la conversation et apparaît sous la forme d’un élément
`functionCallOutput` dans les notifications et l’historique enregistré. Si un tour standard
est déjà actif, Codex met la sortie en file d’attente pour ce tour.

### Injectez des éléments dans un fil

Utilisez `thread/inject_items` pour ajouter des éléments préconstruits de l’API Responses à l’historique des prompts d’un fil chargé sans démarrer de tour utilisateur. Ces éléments sont enregistrés dans le journal de déroulement et inclus dans les requêtes suivantes envoyées au modèle.

```json
{ "method": "thread/inject_items", "id": 31, "params": {
  "threadId": "thr_123",
  "items": [
    {
      "type": "message",
      "role": "assistant",
      "content": [{ "type": "output_text", "text": "Previously computed context." }]
    }
  ]
} }
{ "id": 31, "result": {} }

### Orientez un tour actif

Utilisez `turn/steer` pour ajouter des entrées utilisateur supplémentaires au tour actif en cours d’exécution.

- Incluez `expectedTurnId` ; sa valeur doit correspondre à l’identifiant du tour actif.
- La requête échoue si le fil ne comporte aucun tour actif.
- `turn/steer` n’émet pas de nouvelle notification `turn/started`.
- `turn/steer` n’accepte pas de paramètres de remplacement au niveau du tour (`model`, `cwd`, `sandboxPolicy` ou `outputSchema`).

```json
{ "method": "turn/steer", "id": 32, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Actually focus on failing tests first." } ],
  "expectedTurnId": "turn_456"
} }
{ "id": 32, "result": { "turnId": "turn_456" } }

### Démarrez un tour (invoquez une skill)

Invoquez explicitement une skill en incluant `$<skill-name>` dans l’entrée textuelle et en ajoutant également un élément d’entrée `skill`.

```json
{ "method": "turn/start", "id": 33, "params": {
  "threadId": "thr_123",
  "input": [
    { "type": "text", "text": "$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage." },
    { "type": "skill", "name": "skill-creator", "path": "/Users/me/.codex/skills/skill-creator/SKILL.md" }
  ]
} }
{ "id": 33, "result": { "turn": { "id": "turn_457", "status": "inProgress", "items": [], "error": null } } }

### Interrompez un tour

```json
{ "method": "turn/interrupt", "id": 31, "params": { "threadId": "thr_123", "turnId": "turn_456" } }
{ "id": 31, "result": {} }

En cas de réussite, le tour se termine avec `status: "interrupted"`.

## Révision

`review/start` exécute l’outil de révision de Codex pour un fil et diffuse les éléments de révision. Les cibles possibles sont notamment :

- `uncommittedChanges`
- `baseBranch` (diff par rapport à une branche)
- `commit` (révision d’un commit précis)
- `custom` (instructions libres)

Utilisez `delivery: "inline"` (valeur par défaut) pour exécuter la révision dans le fil existant, ou `delivery: "detached"` pour forker un nouveau fil de révision.

Exemple de requête/réponse :

```json
{ "method": "review/start", "id": 40, "params": {
  "threadId": "thr_123",
  "delivery": "inline",
  "target": { "type": "commit", "sha": "1234567deadbeef", "title": "Polish tui colors" }
} }
{ "id": 40, "result": {
  "turn": {
    "id": "turn_900",
    "status": "inProgress",
    "items": [
      { "type": "userMessage", "id": "turn_900", "content": [ { "type": "text", "text": "Review commit 1234567: Polish tui colors" } ] }
    ],
    "error": null
  },
  "reviewThreadId": "thr_123"
} }

Pour une révision détachée, utilisez `"delivery": "detached"`. La réponse a la même structure, mais `reviewThreadId` correspond à l’identifiant du nouveau fil de révision (différent du `threadId` d’origine). Le serveur émet également une notification `thread/started` pour ce nouveau fil avant de diffuser le tour de révision.

Codex diffuse la notification `turn/started` habituelle, suivie d’une notification `item/started` contenant un élément `enteredReviewMode` :

```json
{
  "method": "item/started",
  "params": {
    "item": {
      "type": "enteredReviewMode",
      "id": "turn_900",
      "review": "current changes"
    }
  }
}

Lorsque l’outil de révision termine son travail, le serveur émet les notifications `item/started` et `item/completed`, qui contiennent un élément `exitedReviewMode` avec le texte final de la révision :

```json
{
  "method": "item/completed",
  "params": {
    "item": {
      "type": "exitedReviewMode",
      "id": "turn_900",
      "review": "Looks solid overall..."
    }
  }
}

Utilisez cette notification pour afficher le résultat de l’outil de révision dans votre client.

## Exécution de processus

`process/*` est une API expérimentale de contrôle explicite des processus. Elle nécessite
`capabilities.experimentalApi = true` et s’exécute hors du bac à sable de Codex. Utilisez-la
uniquement si votre client expose intentionnellement le contrôle des processus locaux sans
bac à sable.

Démarrez un processus avec `process/spawn` et fournissez un `processHandle`, puis utilisez
ce descripteur pour les requêtes stdin, de redimensionnement et d’arrêt. La sortie est diffusée via les
notifications `process/outputDelta`, et la fin du processus est signalée par
`process/exited`.

```json
{ "method": "process/spawn", "id": 48, "params": {
  "command": ["python3", "-m", "pytest", "-q"],
  "processHandle": "pytest-1",
  "cwd": "/Users/me/project",
  "tty": true
} }
{ "id": 48, "result": {} }
{ "method": "process/outputDelta", "params": {
  "processHandle": "pytest-1",
  "stream": "stdout",
  "deltaBase64": "Li4u"
} }
{ "method": "process/exited", "params": {
  "processHandle": "pytest-1",
  "exitCode": 0
} }

Utilisez `process/writeStdin` avec `deltaBase64`, `closeStdin` ou les deux pour envoyer
des données en entrée. Utilisez `process/resizePty` pour les événements de redimensionnement du PTY et `process/kill` pour
terminer un processus en cours d’exécution.

## Exécution de commandes

`command/exec` exécute une seule commande (tableau `argv`) dans le bac à sable du serveur sans créer de fil.

```json
{ "method": "command/exec", "id": 50, "params": {
  "command": ["ls", "-la"],
  "cwd": "/Users/me/project",
  "sandboxPolicy": { "type": "workspaceWrite" },
  "timeoutMs": 10000
} }
{ "id": 50, "result": { "exitCode": 0, "stdout": "...", "stderr": "" } }

Utilisez `sandboxPolicy.type = "externalSandbox"` si vous avez déjà placé le processus serveur dans un bac à sable et souhaitez que Codex n’applique pas ses propres règles de bac à sable. En mode bac à sable externe, définissez `networkAccess` sur `restricted` (par défaut) ou `enabled`. Pour `readOnly` et `workspaceWrite`, utilisez la même structure facultative `access` / `readOnlyAccess` présentée ci-dessus.

Remarques :

- Le serveur rejette les tableaux `command` vides.
- `sandboxPolicy` accepte la même structure que celle utilisée par `turn/start` (par exemple, `dangerFullAccess`, `readOnly`, `workspaceWrite`, `externalSandbox`).
- Lorsque `timeoutMs` est omis, la valeur par défaut du serveur s’applique.
- Définissez `tty: true` pour les sessions reposant sur un PTY, et utilisez `processId` si vous prévoyez ensuite d’appeler `command/exec/write`, `command/exec/resize` ou `command/exec/terminate`.
- Définissez `streamStdoutStderr: true` pour recevoir des notifications `command/exec/outputDelta` pendant l’exécution de la commande.

### Consultez les exigences de l’administrateur (`configRequirements/read`)

Utilisez `configRequirements/read` pour consulter les exigences de l’administrateur en vigueur, chargées depuis `requirements.toml` et/ou via MDM.

```json
{ "method": "configRequirements/read", "id": 52, "params": {} }
{ "id": 52, "result": {
  "requirements": {
    "allowedApprovalPolicies": ["onRequest", "unlessTrusted"],
    "allowedSandboxModes": ["readOnly", "workspaceWrite"],
    "featureRequirements": {
      "personality": true,
      "unified_exec": false
    },
    "network": {
      "enabled": true,
      "allowedDomains": ["api.openai.com"],
      "allowUnixSockets": ["/tmp/example.sock"],
      "dangerouslyAllowAllUnixSockets": false
    }
  }
} }

`result.requirements` vaut `null` lorsqu’aucune exigence n’est configurée. Consultez la documentation sur [`requirements.toml`](/fr-FR/codex/config-file/config-reference#requirementstoml) pour en savoir plus sur les clés et valeurs prises en charge.

### Configuration du bac à sable Windows (`windowsSandbox/setupStart`)

Les clients Windows personnalisés peuvent déclencher la configuration du bac à sable de manière asynchrone, sans rester bloqués sur les vérifications au démarrage.

```json
{ "method": "windowsSandbox/setupStart", "id": 53, "params": { "mode": "elevated" } }
{ "id": 53, "result": { "started": true } }

App-server lance la configuration en arrière-plan, puis émet une notification lorsqu’elle est terminée :

```json
{
  "method": "windowsSandbox/setupCompleted",
  "params": { "mode": "elevated", "success": true, "error": null }
}

Modes :

- `elevated` - exécutez la procédure de configuration du bac à sable Windows avec élévation de privilèges.
- `unelevated` - exécutez l’ancienne procédure de configuration et de vérification préalable.

## Système de fichiers

Les API v2 du système de fichiers utilisent des chemins absolus. Utilisez `fs/watch` lorsqu’un client doit invalider l’état de l’interface utilisateur après la modification d’un fichier ou d’un répertoire.

```json
{ "method": "fs/watch", "id": 54, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "path": "/Users/me/project/.git/HEAD"
} }
{ "id": 54, "result": { "path": "/Users/me/project/.git/HEAD" } }
{ "method": "fs/changed", "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "changedPaths": ["/Users/me/project/.git/HEAD"]
} }
{ "method": "fs/unwatch", "id": 55, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1"
} }
{ "id": 55, "result": {} }

La surveillance d’un fichier émet `fs/changed` pour le chemin de ce fichier, y compris pour les mises à jour effectuées par des opérations de remplacement ou de renommage.

## Événements

Les notifications d’événements forment un flux envoyé par le serveur pour suivre les cycles de vie des fils de discussion et des tours, ainsi que les éléments qu’ils contiennent. Après avoir démarré ou repris un fil de discussion, continuez à lire le flux du transport actif pour recevoir les notifications `thread/started`, `thread/archived`, `thread/unarchived`, `thread/closed`, `thread/status/changed`, `turn/*`, `item/*` et `serverRequest/resolved`.

### Désactivation sélective des notifications

Les clients peuvent désactiver certaines notifications pour chaque connexion en transmettant les noms exacts des méthodes dans `initialize.params.capabilities.optOutNotificationMethods`.

- Correspondance exacte uniquement : `item/agentMessage/delta` ne désactive que les notifications de cette méthode.
- Les noms de méthodes inconnus sont ignorés.
- S’applique aux notifications actuelles `thread/*`, `turn/*` et `item/*`, ainsi qu’aux notifications v2 associées.
- Ne s’applique pas aux requêtes, aux réponses ni aux erreurs.

### Événements de recherche approximative de fichiers (expérimental)

L’API de session de recherche approximative de fichiers émet des notifications pour chaque requête :

- `fuzzyFileSearch/sessionUpdated` - `{ sessionId, query, files }` avec les correspondances actuelles pour la requête active.
- `fuzzyFileSearch/sessionCompleted` - `{ sessionId }` une fois l’indexation et la recherche de correspondances terminées pour cette requête.

### Événements d’avertissement

- `configWarning` - `{ summary, details?, path?, range? }` pour les problèmes de configuration ou d’initialisation
  dont le système peut se remettre.
- `warning` - `{ threadId?, message }` pour les avertissements d’exécution non fatals.

### Événements de configuration du bac à sable Windows

- `windowsSandbox/setupCompleted` - `{ mode, success, error }` émis une fois le traitement d’une requête `windowsSandbox/setupStart` terminé.

### Événements de tour

- `turn/started` - `{ turn }` avec l’identifiant du tour, un tableau `items` vide et `status: "inProgress"`.
- `turn/completed` - `{ turn }` où `turn.status` vaut `completed`, `interrupted` ou `failed` ; en cas d’échec, `{ error: { message, codexErrorInfo?, additionalDetails? } }` est inclus.
- `turn/diff/updated` - `{ threadId, turnId, diff }` avec le dernier diff unifié regroupant toutes les modifications de fichiers du tour.
- `turn/plan/updated` - `{ turnId, explanation?, plan }` chaque fois que l’agent partage ou modifie son plan ; chaque entrée de `plan` est de la forme `{ step, status }`, où `status` vaut `pending`, `inProgress` ou `completed`.
- `hook/started` et `hook/completed` - `{ threadId, turnId?, run }` lorsqu’un hook de cycle de vie synchrone démarre et lorsque le résumé final de son exécution est disponible. Ces notifications ne sont pas émises pour les hooks asynchrones.
- `model/safetyBuffering/updated` - `{ threadId, turnId, model, useCases, reasons, showBufferingUi, fasterModel }` lorsqu’une réponse est temporairement mise en mémoire tampon pour des raisons de sécurité.
- `model/rerouted` - `{ threadId, turnId, fromModel, toModel, reason }` lorsque le service achemine une requête vers un autre modèle.
- `model/verification` - `{ threadId, turnId, verifications }` lorsque le service exige une vérification supplémentaire du compte.
- `thread/tokenUsage/updated` - mises à jour des données d’utilisation du fil de discussion actif.

`turn/diff/updated` et `turn/plan/updated` contiennent actuellement des tableaux `items` vides, même lorsque des événements relatifs aux éléments sont diffusés en continu. Utilisez les notifications `item/*` comme source de référence pour les éléments du tour.

### Éléments

`ThreadItem` est l’union discriminée transmise dans les réponses de tour et les notifications `item/*`. Les types d’éléments courants sont les suivants :

- `userMessage` - `{id, content}` où `content` est une liste d’entrées de l’utilisateur (`text`, `image` ou `localImage`).
- `functionCallOutput` - `{id, name, namespace, output}` pour une sortie d’outil fournie séparément via `turn/start.toolOutput`. `namespace` peut valoir `null`.
- `agentMessage` - `{id, text, phase?}` contenant la réponse cumulée de l’agent. Lorsqu’il est présent, `phase` utilise les valeurs du format d’échange de l’API Responses (`commentary`, `final_answer`).
- `plan` - `{id, text}` contenant le texte du plan proposé en mode plan. Considérez l’élément `plan` final transmis par `item/completed` comme la référence.
- `reasoning` - `{id, summary, content}` où `summary` contient les résumés de raisonnement diffusés en continu et `content` les blocs de raisonnement bruts.
- `commandExecution` - `{id, command, cwd, status, commandActions, aggregatedOutput?, exitCode?, durationMs?}`.
- `fileChange` - `{id, changes, status}` décrivant les modifications proposées ; `changes` est une liste d’objets `{path, kind, diff}`.
- `mcpToolCall` - `{id, server, tool, status, arguments, appContext?, pluginId?, result?, error?}`. Pour les applications MCP de confiance, `appContext` peut inclure `connectorId`, `linkId`, `resourceUri`, `appName`, `templateId` et le champ stable `actionName` du connecteur. Les anciens éléments persistés peuvent ne pas inclure les métadonnées plus récentes. Utilisez `appContext.resourceUri` plutôt que le champ de niveau supérieur obsolète `mcpAppResourceUri`.
- `dynamicToolCall` - `{id, tool, arguments, status, contentItems?, success?, durationMs?}` pour les appels d’outils dynamiques exécutés par le client.
- `collabToolCall` - `{id, tool, status, senderThreadId, receiverThreadId?, newThreadId?, prompt?, agentStatus?}`.
- `webSearch` - `{id, query, action?}` pour les requêtes de recherche web émises par l’agent.
- `imageView` - `{id, path}` émis lorsque l’agent appelle l’outil de visualisation d’images.
- `enteredReviewMode` - `{id, review}` envoyé au démarrage du réviseur.
- `exitedReviewMode` - `{id, review}` émis lorsque le réviseur a terminé.
- `contextCompaction` - `{id}` émis lorsque Codex compacte l’historique de la conversation.

Pour `webSearch.action`, le champ `type` de l’action peut valoir `search` (`query?`, `queries?`), `openPage` (`url?`) ou `findInPage` (`url?`, `pattern?`).

Dans App Server, l’ancienne notification `thread/compacted` est obsolète ; utilisez plutôt l’élément `contextCompaction`.

Tous les éléments émettent deux événements de cycle de vie communs :

- `item/started` - émet l’objet `item` complet lorsqu’une nouvelle unité de travail commence ; la valeur de `item.id` correspond à celle de `itemId` utilisée par les deltas.
- `item/completed` - envoie l’objet `item` final une fois le travail terminé ; considérez-le comme l’état de référence.

### Deltas des éléments

- `item/agentMessage/delta` - ajoute au message de l’agent le texte diffusé en continu.
- `item/plan/delta` - diffuse en continu le texte du plan proposé. L’élément `plan` final peut ne pas correspondre exactement à la concaténation des deltas.
- `item/reasoning/summaryTextDelta` - diffuse en continu des résumés lisibles du raisonnement ; `summaryIndex` est incrémenté à l’ouverture de chaque nouvelle section de résumé.
- `item/reasoning/summaryPartAdded` - marque une séparation entre les sections du résumé du raisonnement.
- `item/reasoning/textDelta` - diffuse en continu le texte brut du raisonnement (lorsque le modèle le prend en charge).
- `item/commandExecution/outputDelta` - diffuse stdout/stderr d’une commande en continu ; ajoutez les deltas dans l’ordre.
- `item/fileChange/outputDelta` - notification de compatibilité obsolète pour l’ancienne sortie textuelle de `apply_patch`. Les versions actuelles d’app-server ne l’émettent plus ; utilisez les éléments `fileChange` et `turn/diff/updated` à la place.

## Erreurs

Si un tour échoue, le serveur émet un événement `error` avec `{ error: { message, codexErrorInfo?, additionalDetails? } }`, puis termine le tour avec `status: "failed"`. Lorsqu’un code d’état HTTP en amont est disponible, il figure dans `codexErrorInfo.httpStatusCode`.

Les valeurs courantes de `codexErrorInfo` sont notamment :

- `ContextWindowExceeded`
- `UsageLimitExceeded`
- `HttpConnectionFailed` (erreurs 4xx/5xx en amont)
- `ResponseStreamConnectionFailed`
- `ResponseStreamDisconnected`
- `ResponseTooManyFailedAttempts`
- `BadRequest`, `Unauthorized`, `SandboxError`, `InternalServerError`, `Other`

Lorsqu’un code d’état HTTP en amont est disponible, le serveur le transmet dans `httpStatusCode` pour la variante `codexErrorInfo` correspondante.

## Approbations

Selon les paramètres Codex de l’utilisateur, l’exécution de commandes et les modifications de fichiers peuvent nécessiter une approbation. App-server envoie au client une requête JSON-RPC à l’initiative du serveur, et le client répond avec une charge utile contenant sa décision.

- Décisions relatives à l’exécution de commandes : `accept`, `acceptForSession`, `decline`, `cancel` ou `{ "acceptWithExecpolicyAmendment": { "execpolicy_amendment": ["cmd", "..."] } }`.
- Décisions relatives aux modifications de fichiers : `accept`, `acceptForSession`, `decline`, `cancel`.

- Les requêtes incluent `threadId` et `turnId` : utilisez-les pour rattacher l’état de l’interface à la conversation active.
- Le serveur reprend ou refuse le traitement et termine l’élément avec `item/completed`.

### Approbations pour l’exécution de commandes

Ordre des messages :

1. `item/started` présente l’élément `commandExecution` en attente, avec `command`, `cwd` et d’autres champs.
2. `item/commandExecution/requestApproval` inclut `itemId`, `threadId`, `turnId`, ainsi que les champs facultatifs `reason`, `command`, `cwd`, `commandActions`, `proposedExecpolicyAmendment`, `networkApprovalContext` et `availableDecisions`. Lorsque `initialize.params.capabilities.experimentalApi = true`, la charge utile peut également inclure le champ expérimental `additionalPermissions`, qui décrit les accès demandés dans le bac à sable pour chaque commande. Dans les données transmises, tous les chemins du système de fichiers figurant dans `additionalPermissions` sont absolus.
3. Le client répond avec l’une des décisions d’approbation de l’exécution de commandes indiquées ci-dessus.
4. `serverRequest/resolved` confirme que la requête en attente a reçu une réponse ou a été supprimée.
5. `item/completed` renvoie l’élément `commandExecution` final avec `status: completed | failed | declined`.

Lorsque `networkApprovalContext` est présent, le prompt concerne un accès réseau géré (et non une approbation générale de commande shell). Le schéma v2 actuel expose les champs `host` et `protocol` de la cible ; les clients devraient afficher un prompt propre à l’accès réseau et ne pas supposer que `command` fournit un aperçu de commande shell compréhensible pour l’utilisateur.

Codex regroupe les prompts d’approbation réseau simultanés par destination (`host`, protocole et port). App-server peut donc envoyer un seul prompt qui débloque plusieurs requêtes en file d’attente vers la même destination, tandis que les différents ports d’un même hôte sont traités séparément.

### Approbations des modifications de fichiers

Ordre des messages :

1. `item/started` émet un élément `fileChange` avec les modifications proposées dans `changes`, ainsi que `status: "inProgress"`.
2. `item/fileChange/requestApproval` inclut `itemId`, `threadId`, `turnId`, ainsi que les champs facultatifs `reason` et `grantRoot`.
3. Le client répond avec l’une des décisions d’approbation des modifications de fichiers indiquées ci-dessus.
4. `serverRequest/resolved` confirme que la requête en attente a reçu une réponse ou a été supprimée.
5. `item/completed` renvoie l’élément `fileChange` final avec `status: completed | failed | declined`.

### `tool/requestUserInput`

Lorsque le client répond à `item/tool/requestUserInput`, app-server émet `serverRequest/resolved` avec `{ threadId, requestId }`. Si la requête en attente est supprimée au démarrage, à la fin ou à l’interruption d’un tour avant que le client ne réponde, le serveur émet la même notification pour signaler cette suppression.

Les paramètres de la requête incluent `autoResolutionMs`, dont la valeur est soit un délai d’expiration en millisecondes exprimé par un entier, soit
`null`. Lorsqu’un délai est défini, les clients hôtes peuvent traiter automatiquement le prompt à l’expiration de ce
délai si l’utilisateur ne répond pas.

### Demandes d’autorisations

L’outil intégré `request_permissions` envoie
`item/permissions/requestApproval` avec `threadId`, `turnId`, `itemId`,
`environmentId`, `cwd`, le champ facultatif `reason`, ainsi que les autorisations d’accès au réseau ou au système de fichiers
demandées. Répondez avec `permissions` en indiquant uniquement le sous-ensemble accordé.
Définissez `scope` sur `"session"` pour conserver les autorisations accordées lors des tours suivants de la même
session ; omettez ce champ ou utilisez `"turn"` pour limiter les autorisations au tour en cours. Les autorisations qui
n’ont pas été demandées sont ignorées.

### Demandes d’élicitation des serveurs MCP

Un serveur MCP peut interrompre un tour avec `mcpServer/elicitation/request`. La
requête inclut `threadId`, le champ facultatif `turnId`, `serverName` et l’une des
structures de requête suivantes :

- `mode: "form"` ou `mode: "openai/form"`, avec `message` et
`requestedSchema`.
- `mode: "url"`, avec `message`, `url` et `elicitationId`.

Répondez avec `action: "accept"` et les données demandées dans `content`, ou avec
`action: "decline"` ou `"cancel"`, ainsi que `content: null`. App-server émet ensuite
`serverRequest/resolved`. Pour recevoir la variante `openai/form`, activez cette fonctionnalité avec
`initialize.params.capabilities.mcpServerOpenaiFormElicitation`.

### Appels d’outils dynamiques (expérimentaux)

Le champ `dynamicTools` dans `thread/start` et le flux de requête ou de réponse `item/tool/call` correspondant constituent des API expérimentales.

Les noms des outils dynamiques et des espaces de noms doivent respecter les contraintes de nommage
imposées par l’API Responses. Évitez les noms d’espaces de noms réservés aux outils intégrés de Codex.

Lorsqu’un outil dynamique est appelé pendant un tour, app-server émet :

1. `item/started` avec `item.type = "dynamicToolCall"`, `status = "inProgress"`, ainsi que `tool` et `arguments`.
2. `item/tool/call` sous forme de requête du serveur au client.
3. La charge utile de la réponse du client, avec les éléments de contenu renvoyés.
4. `item/completed` avec `item.type = "dynamicToolCall"`, la valeur finale de `status`, ainsi que toute valeur renvoyée dans `contentItems` ou `success`.

### Approbations des appels d’outils MCP (applications)

Les appels d’outils d’une App (connecteur) peuvent également nécessiter une approbation. Lorsqu’un appel à un outil d’application entraîne des effets de bord, le serveur peut demander une approbation avec `tool/requestUserInput` et proposer des options telles que **Accepter**, **Refuser** et **Annuler**. Les annotations indiquant qu’un outil est destructif déclenchent toujours une demande d’approbation, même si l’outil fournit également des indications suggérant des privilèges moindres. Si l’utilisateur refuse ou annule, l’élément `mcpToolCall` associé se termine par une erreur et l’outil n’est pas exécuté.

## Skills

Appelez un skill en incluant `$<skill-name>` dans le texte saisi par l’utilisateur. Ajoutez un élément d’entrée `skill` (recommandé) afin que le serveur injecte les instructions complètes du skill au lieu de laisser le modèle l’identifier à partir de son nom.

```json
{
  "method": "turn/start",
  "id": 101,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$skill-creator Add a new skill for triaging flaky CI."
      },
      {
        "type": "skill",
        "name": "skill-creator",
        "path": "/Users/me/.codex/skills/skill-creator/SKILL.md"
      }
    ]
  }
}

Si vous omettez l’élément `skill`, le modèle analyse tout de même le marqueur `$<skill-name>` et tente de trouver le skill, ce qui peut augmenter la latence.

Exemple :

$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage.

Utilisez `skills/list` pour récupérer les skills disponibles (éventuellement filtrés par `cwds`, avec `forceReload`). Vous pouvez également inclure `perCwdExtraUserRoots` pour parcourir des chemins absolus supplémentaires dans la portée `user` pour des valeurs précises de `cwd`. App-server ignore les entrées dont la valeur `cwd` ne figure pas dans `cwds`. `skills/list` peut réutiliser un résultat mis en cache pour chaque `cwd` ; définissez `forceReload: true` pour actualiser les données depuis le disque. S’ils sont présents, le serveur lit `interface` et `dependencies` dans `SKILL.json`.

```json
{ "method": "skills/list", "id": 25, "params": {
  "cwds": ["/Users/me/project", "/Users/me/other-project"],
  "forceReload": true,
  "perCwdExtraUserRoots": [
    {
      "cwd": "/Users/me/project",
      "extraUserRoots": ["/Users/me/shared-skills"]
    }
  ]
} }
{ "id": 25, "result": {
  "data": [{
    "cwd": "/Users/me/project",
    "skills": [
      {
        "name": "skill-creator",
        "description": "Create or update a Codex skill",
        "enabled": true,
        "interface": {
          "displayName": "Skill Creator",
          "shortDescription": "Create or update a Codex skill"
        },
        "dependencies": {
          "tools": [
            {
              "type": "env_var",
              "value": "GITHUB_TOKEN",
              "description": "GitHub API token"
            },
            {
              "type": "mcp",
              "value": "github",
              "transport": "streamable_http",
              "url": "https://example.com/mcp"
            }
          ]
        }
      }
    ],
    "errors": []
  }]
} }

Le serveur émet également des notifications `skills/changed` lorsque les fichiers locaux de skills sous surveillance changent. Considérez-les comme un signal d’invalidation et relancez `skills/list` avec vos paramètres actuels si nécessaire.

Pour activer ou désactiver un skill à partir de son chemin :

```json
{
  "method": "skills/config/write",
  "id": 26,
  "params": {
    "path": "/Users/me/.codex/skills/skill-creator/SKILL.md",
    "enabled": false
  }
}

## Applications (connecteurs)

Utilisez `app/installed` pour lire le dernier instantané validé de l’état d’exécution des applications installées.
Chaque résultat comprend l’identifiant `id` de l’application, `runtimeName` (ou `null`), l’état effectif
`enabled` et l’état `callable`. Une application ne peut être appelée que si la configuration
effective l’active et qu’au moins un outil visible par le modèle respecte les politiques
de l’application et des outils.

```json
{
  "method": "app/installed",
  "id": 49,
  "params": {
    "threadId": "thread-1",
    "forceRefresh": false
  }
}
{
  "id": 49,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "runtimeName": "Demo App",
        "enabled": true,
        "callable": true
      }
    ]
  }
}

Omettez `threadId` pour utiliser la configuration globale plutôt que celle d’un fil de discussion
chargé. Définissez `forceRefresh: true` pour actualiser l’instantané de l’état d’exécution du connecteur
avant de le lire. Lorsque la politique globale ou celle de l’espace de travail bloque l’accès aux applications,
une application observée peut tout de même apparaître avec `enabled` et `callable` définis sur `false`.

Utilisez `app/list` pour récupérer les applications disponibles. Dans la CLI/TUI, `/apps` est le sélecteur présenté à l’utilisateur ; dans les clients personnalisés, appelez directement `app/list`. Chaque entrée inclut à la fois `isAccessible` (disponible pour l’utilisateur) et `isEnabled` (activé dans `config.toml`), afin que les clients puissent distinguer l’installation ou l’accès de l’état d’activation local. Les entrées d’application peuvent également inclure les champs facultatifs `branding`, `appMetadata` et `labels`.

```json
{ "method": "app/list", "id": 50, "params": {
  "cursor": null,
  "limit": 50,
  "threadId": "thread-1",
  "forceRefetch": false
} }
{ "id": 50, "result": {
  "data": [
    {
      "id": "demo-app",
      "name": "Demo App",
      "description": "Example connector for documentation.",
      "logoUrl": "https://example.com/demo-app.png",
      "logoUrlDark": null,
      "distributionChannel": null,
      "branding": null,
      "appMetadata": null,
      "labels": null,
      "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
      "isAccessible": true,
      "isEnabled": true
    }
  ],
  "nextCursor": null
} }

Si vous fournissez `threadId`, le contrôle d’activation des applications (`features.apps`) utilise l’instantané de configuration de ce fil de discussion. Si vous l’omettez, app-server utilise la dernière configuration globale.

`app/list` renvoie sa réponse une fois le chargement des applications accessibles et des applications de l’annuaire terminé. Définissez `forceRefetch: true` pour ignorer les caches d’applications et récupérer des données à jour. Les entrées du cache ne sont remplacées que si l’actualisation réussit.

Le serveur émet également des notifications `app/list/updated` chaque fois que l’une des deux sources (applications accessibles ou applications de l’annuaire) termine son chargement. Chaque notification contient la dernière liste fusionnée des applications.

```json
{
  "method": "app/list/updated",
  "params": {
    "data": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "logoUrl": "https://example.com/demo-app.png",
        "logoUrlDark": null,
        "distributionChannel": null,
        "branding": null,
        "appMetadata": null,
        "labels": null,
        "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
        "isAccessible": true,
        "isEnabled": true
      }
    ]
  }
}

Utilisez `app/read` lorsque vous connaissez déjà les identifiants des applications et avez besoin de leurs métadonnées plutôt
que de l’état d’exécution des applications installées. Transmettez au maximum 100 identifiants dans `appIds`. Le serveur ne conserve que
la première occurrence de chaque identifiant répété et préserve cet ordre à la fois dans
`apps` et dans `missingAppIds`. Les applications inconnues ou inaccessibles sont renvoyées dans
`missingAppIds`, sans faire échouer l’ensemble de la requête.

```json
{
  "method": "app/read",
  "id": 52,
  "params": {
    "appIds": ["demo-app", "missing-app"],
    "includeTools": true
  }
}
{
  "id": 52,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "iconUrl": null,
        "iconUrlDark": null,
        "distributionChannel": null,
        "installUrl": null,
        "pluginDisplayNames": [],
        "toolSummaries": [
          {
            "name": "search",
            "title": "Search",
            "description": "Search the app.",
            "isEnabled": true,
            "disabledReason": null,
            "isReadOnly": true
          }
        ]
      }
    ],
    "missingAppIds": ["missing-app"]
  }
}

Définissez `includeTools: true` pour demander des résumés publics des outils destinés uniquement à l’affichage. La
réponse contenant les métadonnées n’inclut pas l’état d’exécution des applications installées et n’autorise aucun
appel d’outil ; utilisez `app/installed` pour vérifier les états effectifs
`enabled` et `callable`.

Invoquez une application en insérant `$<app-slug>` dans le texte saisi et en ajoutant un élément d’entrée `mention` avec le chemin `app://<id>` (recommandé).

```json
{
  "method": "turn/start",
  "id": 51,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$demo-app Pull the latest updates from the team."
      },
      {
        "type": "mention",
        "name": "Demo App",
        "path": "app://demo-app"
      }
    ]
  }
}

### Exemples de RPC de configuration pour les paramètres des applications

Utilisez `config/read`, `config/value/write` et `config/batchWrite` pour consulter ou modifier les paramètres des applications dans `config.toml`.

Consultez la structure de la configuration effective des applications (y compris `_default` et les valeurs de remplacement propres à chaque outil) :

```json
{ "method": "config/read", "id": 60, "params": { "includeLayers": false } }
{ "id": 60, "result": {
  "config": {
    "apps": {
      "_default": {
        "enabled": true,
        "destructive_enabled": true,
        "open_world_enabled": true,
        "approvals_reviewer": "user",
        "default_tools_approval_mode": "auto"
      },
      "google_drive": {
        "enabled": true,
        "destructive_enabled": false,
        "approvals_reviewer": "auto_review",
        "default_tools_approval_mode": "prompt",
        "tools": {
          "files/delete": { "enabled": false, "approval_mode": "approve" }
        }
      }
    }
  }
} }

`apps._default.approvals_reviewer` définit le réviseur pour toutes les applications, sauf si une
valeur propre à une application le remplace. Si ces deux valeurs sont omises, l’application hérite de la
valeur `approvals_reviewer` définie au niveau supérieur. `apps._default.default_tools_approval_mode`
définit le mode d’approbation de repli pour les outils sans valeur de remplacement propre à l’application
ou à l’outil. Les exigences gérées relatives au mode d’approbation prévalent sur les paramètres de mode d’approbation
des outils.

Mettez à jour un seul paramètre d’application :

```json
{
  "method": "config/value/write",
  "id": 61,
  "params": {
    "keyPath": "apps.google_drive.default_tools_approval_mode",
    "value": "prompt",
    "mergeStrategy": "replace"
  }
}

Appliquez plusieurs modifications de configuration d’applications de manière atomique :

```json
{
  "method": "config/batchWrite",
  "id": 62,
  "params": {
    "edits": [
      {
        "keyPath": "apps._default.destructive_enabled",
        "value": false,
        "mergeStrategy": "upsert"
      },
      {
        "keyPath": "apps.google_drive.tools.files/delete.approval_mode",
        "value": "approve",
        "mergeStrategy": "upsert"
      }
    ]
  }
}

### Détectez et importez la configuration d’agents externes

Utilisez `externalAgentConfig/detect` pour détecter les artefacts d’agents externes pouvant être migrés, puis transmettez les entrées sélectionnées à `externalAgentConfig/import`.

Exemple de détection :

```json
{ "method": "externalAgentConfig/detect", "id": 63, "params": {
  "includeHome": true,
  "cwds": ["/Users/me/project"]
} }
{ "id": 63, "result": {
  "items": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    },
    {
      "itemType": "SKILLS",
      "description": "Copy skill folders from /Users/me/.claude/skills to /Users/me/.agents/skills.",
      "cwd": null
    }
  ]
} }

Exemple d’importation :

```json
{ "method": "externalAgentConfig/import", "id": 64, "params": {
  "migrationItems": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    }
  ],
  "source": "claude-code"
} }
{ "id": 64, "result": { "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868" } }

Le paramètre d’importation facultatif `source`, au niveau supérieur, indique le produit qui a
généré les éléments sélectionnés pour la migration.

Le serveur émet `externalAgentConfig/import/progress` à mesure que l’importation de chaque type d’élément se termine,
puis `externalAgentConfig/import/completed` une fois toutes les importations synchrones et en arrière-plan
terminées. Ces notifications incluent le même `importId` que dans la
réponse, ainsi que `itemTypeResults`, qui contient `successes` et `failures` pour chaque type.
La notification de fin peut arriver immédiatement après la réponse ou une fois les importations distantes
en arrière-plan terminées.

```json
{ "method": "externalAgentConfig/import/progress", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }
{ "method": "externalAgentConfig/import/completed", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }

Consultez les importations déjà terminées :

```json
{ "method": "externalAgentConfig/import/readHistories", "id": 65 }
{ "id": 65, "result": { "data": [
  {
    "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
    "completedAtMs": 1781784000000,
    "successes": [
      { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
    ],
    "failures": []
  }
] } }

Les valeurs de `itemType` prises en charge sont `AGENTS_MD`, `CONFIG`, `SKILLS`, `PLUGINS`,
`MCP_SERVER_CONFIG`, `SUBAGENTS`, `HOOKS`, `COMMANDS` et `SESSIONS`. Pour les éléments
`PLUGINS`, `details.plugins` répertorie chaque `marketplaceName` ainsi que les
`pluginNames` que Codex peut tenter de migrer. La détection ne renvoie que les éléments qui nécessitent encore
un traitement. Par exemple, Codex ignore la migration d’AGENTS lorsque `AGENTS.md`
existe déjà et n’est pas vide, et les importations de skills n’écrasent pas les répertoires de skills
existants.

Lors de la détection de plugins à partir de `.claude/settings.json`, Codex lit les sources de Marketplace configurées
dans `extraKnownMarketplaces`. Si `enabledPlugins` contient
des plugins provenant de `claude-plugins-official`, mais que la source de Marketplace correspondante est absente,
Codex déduit que `anthropics/claude-plugins-official` est la source.

## Points de terminaison d’authentification

L’interface JSON-RPC d’authentification et de gestion du compte expose des méthodes de requête et de réponse ainsi que des notifications émises à l’initiative du serveur (sans `id`). Utilisez-les pour déterminer l’état d’authentification, lancer ou annuler des procédures de connexion, déconnecter l’utilisateur, consulter les limites de débit de ChatGPT et informer les propriétaires d’espaces de travail de l’épuisement des crédits ou des limites d’utilisation.

### Modes d’authentification

Codex prend en charge les modes d’authentification suivants. `account/updated.authMode` indique le mode actif et inclut la valeur actuelle de `planType` pour ChatGPT lorsqu’elle est disponible. `account/read` fournit également les détails relatifs au compte et à l’offre.

- **Clé API (`apikey`)** - l’appelant fournit une clé API OpenAI avec `type: "apiKey"`, et Codex la stocke pour les requêtes API.
- **Authentification ChatGPT gérée (`chatgpt`)** - Codex gère le flux OAuth ChatGPT, conserve les tokens et les actualise automatiquement. Démarrez avec `type: "chatgpt"` pour le flux par navigateur ou `type: "chatgptDeviceCode"` pour le flux par code d’appareil.
- **Tokens ChatGPT externes (`chatgptAuthTokens`)** - ce mode expérimental est destiné aux applications hôtes qui gèrent déjà le cycle d’authentification ChatGPT de l’utilisateur. L’application hôte fournit directement un `accessToken`, un `chatgptAccountId` et, facultativement, un `chatgptPlanType`, et doit actualiser le token sur demande.
- **Amazon Bedrock** - `account/read` présente les comptes Bedrock sous la forme `type: "amazonBedrock"` et indique si les identifiants proviennent d’une clé API Bedrock gérée par Codex (`credentialSource: "codexManaged"`) ou de la chaîne externe de résolution des identifiants AWS (`credentialSource: "awsManaged"`). `account/updated.authMode` utilise `bedrockApiKey` pour les clés API Bedrock gérées par Codex.

### Vue d’ensemble de l’API

- `account/read` - récupère les informations du compte actuel et permet, en option, d’actualiser les tokens.
- `account/login/start` - démarre une procédure de connexion (`apiKey`, `chatgpt`, `chatgptDeviceCode` ou, à titre expérimental, `chatgptAuthTokens`).
- `account/login/completed` (notification) - émise à la fin d’une tentative de connexion (réussite ou erreur).
- `account/login/cancel` - annule une procédure de connexion ChatGPT gérée en attente, identifiée par `loginId`.
- `account/logout` - déconnecte l’utilisateur et déclenche `account/updated`.
- `account/updated` (notification) - émise à chaque changement du mode d’authentification (`authMode` : `apikey`, `chatgpt`, `chatgptAuthTokens`, `agentIdentity`, `personalAccessToken`, `bedrockApiKey` ou `null`) et inclut `planType` lorsqu’il est disponible.
- `account/chatgptAuthTokens/refresh` (requête du serveur) - demande de nouveaux tokens ChatGPT gérés en externe à la suite d’une erreur d’autorisation.
- `account/rateLimits/read` - récupère les limites de débit de ChatGPT.
- `account/rateLimits/updated` (notification) - émise à chaque changement des limites de débit ChatGPT d’un utilisateur.
- `account/sendAddCreditsNudgeEmail` - demande à ChatGPT d’informer par e-mail un propriétaire d’espace de travail de l’épuisement des crédits ou de l’atteinte d’une limite d’utilisation.
- `account/rateLimitResetCredit/consume` - consomme une réinitialisation acquise de la limite de débit à l’aide d’une valeur `idempotencyKey` fournie par l’appelant.
- `account/usage/read` - récupère les récapitulatifs d’utilisation des tokens du compte ChatGPT et les agrégats quotidiens.
- `account/workspaceMessages/read` - récupère les messages actifs de l’espace de travail, y compris les titres des notifications lorsqu’ils sont disponibles.
- `mcpServer/oauthLogin/completed` (notification) - émise à la fin d’un flux `mcpServer/oauth/login` ; la charge utile inclut `{ name, threadId, success, error? }`. `threadId` peut valoir `null` pour les flux OAuth propres à une application ou à un plugin.
- `mcpServer/startupStatus/updated` (notification) - émise lorsque l’état de démarrage d’un serveur MCP configuré change ; la charge utile inclut `{ threadId, name, status, error, failureReason }`. `threadId` vaut `null` pour un démarrage au niveau de l’application. En cas d’échec du démarrage, `failureReason: "reauthenticationRequired"` signifie que les identifiants OAuth stockés ont expiré et n’ont pas pu être actualisés ; le client devrait donc proposer de reconnecter le serveur.

### 1) Vérifiez l’état d’authentification

Requête :

```json
{ "method": "account/read", "id": 1, "params": { "refreshToken": false } }

Exemples de réponses :

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": false } }

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": true } }

```json
{
  "id": 1,
  "result": { "account": { "type": "apiKey" }, "requiresOpenaiAuth": true }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "codexManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "awsManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "chatgpt",
      "email": "user@example.com",
      "planType": "pro"
    },
    "requiresOpenaiAuth": true
  }
}

Remarques sur les champs :

- `refreshToken` (booléen) : définissez-le sur `true` pour forcer l’actualisation du token en mode d’authentification ChatGPT gérée. En mode de tokens externes (`chatgptAuthTokens`), app-server ignore ce paramètre.
- `email` vaut `null` lorsque le compte ChatGPT n’a pas d’adresse e-mail.
- `requiresOpenaiAuth` reflète le fournisseur actif ; lorsqu’il vaut `false`, Codex peut fonctionner sans identifiants OpenAI.
- Amazon Bedrock indique `credentialSource: "codexManaged"` lorsqu’il utilise une
  clé API Bedrock gérée par Codex. Il indique `credentialSource: "awsManaged"`
  pour la résolution externe des identifiants AWS. Cela identifie la source d’identifiants
  sélectionnée, sans vérifier que la chaîne de résolution des identifiants AWS peut
  obtenir des identifiants.

### 2) Connectez-vous avec une clé API

1. Envoyez :

   ```json
   {
     "method": "account/login/start",
     "id": 2,
     "params": { "type": "apiKey", "apiKey": "sk-..." }
   }

2. Résultat attendu :

   ```json
   { "id": 2, "result": { "type": "apiKey" } }

3. Notifications :

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "apikey", "planType": null }
   }

### 3) Connectez-vous avec ChatGPT (flux par navigateur)

1. Démarrez :

   ```json
   {
     "method": "account/login/start",
     "id": 3,
     "params": {
       "type": "chatgpt",
       "useHostedLoginSuccessPage": true,
       "appBrand": "chatgpt"
     }
   }

   Par défaut, lorsqu’un callback du navigateur aboutit, il redirige vers une page locale de confirmation.
   Définissez `useHostedLoginSuccessPage: true` pour utiliser la page de confirmation hébergée lorsque
   la configuration de l’organisation n’est pas requise. Lorsque cette page hébergée est activée, `appBrand`
   peut valoir `"codex"` ou `"chatgpt"` ; si la valeur est omise ou vaut `null`, la valeur par défaut est
`"codex"`.

   ```json
   {
     "id": 3,
     "result": {
       "type": "chatgpt",
       "loginId": "<uuid>",
       "authUrl": "https://chatgpt.com/...&redirect_uri=http%3A%2F%2Flocalhost%3A<port>%2Fauth%2Fcallback"
     }
   }

2. Ouvrez `authUrl` dans un navigateur ; app-server héberge le callback local.
3. Attendez les notifications :

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3b) Connectez-vous avec ChatGPT (flux par code d’appareil)

Utilisez ce flux lorsque votre client gère lui-même la procédure de connexion ou lorsqu’un callback du navigateur est peu fiable.

1. Démarrez :

   ```json
   {
     "method": "account/login/start",
     "id": 4,
     "params": { "type": "chatgptDeviceCode" }
   }

   ```json
   {
     "id": 4,
     "result": {
       "type": "chatgptDeviceCode",
       "loginId": "<uuid>",
       "verificationUrl": "https://auth.openai.com/codex/device",
       "userCode": "ABCD-1234"
     }
   }

2. Affichez `verificationUrl` et `userCode` à l’utilisateur ; le frontend prend en charge l’expérience utilisateur.
3. Attendez les notifications :

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3c) Connectez-vous avec des tokens ChatGPT gérés en externe (`chatgptAuthTokens`)

Utilisez ce mode expérimental uniquement lorsqu’une application hôte gère le cycle de vie de l’authentification ChatGPT de l’utilisateur et fournit directement les tokens. Les clients doivent définir `capabilities.experimentalApi = true` lors de `initialize` avant d’utiliser ce type de connexion.

1. Envoyez :

   ```json
   {
     "method": "account/login/start",
     "id": 7,
     "params": {
       "type": "chatgptAuthTokens",
       "accessToken": "<jwt>",
       "chatgptAccountId": "org-123",
       "chatgptPlanType": "business"
     }
   }

2. Réponse attendue :

   ```json
   { "id": 7, "result": { "type": "chatgptAuthTokens" } }

3. Notifications :

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgptAuthTokens", "planType": "business" }
   }

Lorsque le serveur reçoit une réponse `401 Unauthorized`, il peut demander à l’application hôte des tokens renouvelés :

```json
{
  "method": "account/chatgptAuthTokens/refresh",
  "id": 8,
  "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
}
{ "id": 8, "result": { "accessToken": "<jwt>", "chatgptAccountId": "org-123", "chatgptPlanType": "business" } }

Après une réponse confirmant le renouvellement, le serveur réessaie la requête initiale. Les requêtes expirent au bout d’environ 10 secondes.

### 4) Annulez une tentative de connexion à ChatGPT

```json
{ "method": "account/login/cancel", "id": 4, "params": { "loginId": "<uuid>" } }
{ "method": "account/login/completed", "params": { "loginId": "<uuid>", "success": false, "error": "..." } }

### 5) Déconnectez-vous

```json
{ "method": "account/logout", "id": 5 }
{ "id": 5, "result": {} }
{ "method": "account/updated", "params": { "authMode": null, "planType": null } }

### 6) Limites de débit (ChatGPT)

```json
{ "method": "account/rateLimits/read", "id": 6 }
{ "id": 6, "result": {
  "rateLimits": {
    "limitId": "codex",
    "limitName": null,
    "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
    "secondary": null,
    "rateLimitReachedType": null
  },
  "rateLimitsByLimitId": {
    "codex": {
      "limitId": "codex",
      "limitName": null,
      "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
      "secondary": null,
      "rateLimitReachedType": null
    },
    "codex_other": {
      "limitId": "codex_other",
      "limitName": "codex_other",
      "primary": { "usedPercent": 42, "windowDurationMins": 60, "resetsAt": 1730950800 },
      "secondary": null,
      "rateLimitReachedType": null
    }
  },
  "rateLimitResetCredits": {
    "availableCount": 2,
    "credits": [{
      "id": "RateLimitResetCredit_1",
      "resetType": "codexRateLimits",
      "status": "available",
      "grantedAt": 1781654400,
      "expiresAt": 1784246400,
      "title": "Rate-limit reset",
      "description": "Reset an eligible Codex rate-limit window."
    }]
  }
} }
{ "method": "account/rateLimits/updated", "params": {
  "rateLimits": {
    "limitId": "codex",
    "primary": { "usedPercent": 31, "windowDurationMins": 15, "resetsAt": 1730948100 }
  }
} }

Remarques sur les champs :

- `rateLimits` est la vue rétrocompatible à un seul compartiment.
- `rateLimitsByLimitId`, lorsqu’il est présent, est la vue à plusieurs compartiments, indexée par le `limit_id` utilisé pour le suivi de l’utilisation (par exemple `codex`).
- `limitId` est l’identifiant du compartiment de suivi de l’utilisation.
- `limitName` est un libellé facultatif du compartiment, destiné à l’utilisateur.
- `usedPercent` indique l’utilisation actuelle dans la fenêtre de quota.
- `windowDurationMins` est la durée de la fenêtre de quota.
- `resetsAt` est l’horodatage Unix (en secondes) de la prochaine réinitialisation.
- `planType` est inclus lorsque le serveur renvoie l’offre ChatGPT associée à un compartiment.
- `credits` est inclus lorsque le serveur renvoie les détails sur les crédits restants de l’espace de travail.
- `rateLimitReachedType` indique, selon la classification du serveur, l’état de la limite lorsqu’elle est atteinte.
- `rateLimitResetCredits` contient le nombre de réinitialisations acquises et disponibles lorsque le service le fournit ; sinon, sa valeur est `null`.
- `rateLimitResetCredits.credits` vaut `null` lorsque seul le nombre est connu. Un tableau vide signifie que le service a récupéré les détails et n’a renvoyé aucun crédit disponible. Le service peut limiter le nombre de lignes de détail ; c’est donc `availableCount` qui fait foi.
- Chaque ligne de détail comprend un `id` opaque, `resetType`, `status`, `grantedAt`, `expiresAt` (qui peut valoir `null`), `title` (qui peut valoir `null`) et `description` (qui peut valoir `null`).
- Appelez `account/rateLimits/read` après avoir consommé un crédit de réinitialisation.

### 7) Utilisation des tokens (ChatGPT)

Utilisez `account/usage/read` pour récupérer les champs récapitulatifs de l’utilisation des tokens ChatGPT ainsi que,
facultativement, les données regroupées par jour.

```json
{ "method": "account/usage/read", "id": 7 }
{ "id": 7, "result": {
  "summary": {
    "lifetimeTokens": 1234567,
    "peakDailyTokens": 45678,
    "longestRunningTurnSec": 540,
    "currentStreakDays": 8,
    "longestStreakDays": 14
  },
  "dailyUsageBuckets": [
    { "startDate": "2026-06-18", "tokens": 12345 }
  ]
} }

Remarques sur les champs :

- Les valeurs de `summary` peuvent être `null` lorsque le service n’a pas renvoyé la métrique correspondante.
- `dailyUsageBuckets` peut valoir `null` ; lorsque ce champ est renseigné, chaque groupe de données comprend `startDate` et `tokens`.
- Le point de terminaison nécessite une authentification reposant sur les services Codex. L’authentification via ChatGPT,
via des tokens ChatGPT externes, par identité d’agent ou par token d’accès personnel fonctionne ;
l’authentification par clé API seule ou via Bedrock ne fonctionne pas.

### 8) Réinitialisations acquises des limites de débit (ChatGPT)

Utilisez `account/rateLimitResetCredit/consume` pour consommer un crédit de réinitialisation acquis.

```json
{ "method": "account/rateLimitResetCredit/consume", "id": 8, "params": { "idempotencyKey": "8ae96ff3-3425-4f4c-8772-b6fd61502868", "creditId": "RateLimitResetCredit_1" } }
{ "id": 8, "result": { "outcome": "reset" } }

Remarques sur les champs :

- `idempotencyKey` ne doit pas être vide. Utilisez un UUID pour chaque tentative logique d’utilisation d’un crédit et réutilisez la même valeur si vous relancez cette tentative.
- `creditId` est facultatif. Lorsque vous le fournissez, il doit s’agir d’un identifiant opaque non vide provenant de `account/rateLimits/read`. Si vous l’omettez, le service sélectionne le prochain crédit disponible.
- `reset` indique qu’un crédit a été consommé.
- `alreadyRedeemed` indique que la même opération d’utilisation du crédit a déjà abouti. Traitez ce résultat comme un succès idempotent et actualisez les limites du compte.
- `nothingToReset` indique qu’aucune fenêtre de limite de débit n’est éligible à une réinitialisation.
- `noCredit` indique qu’aucun crédit de réinitialisation acquis n’est disponible pour ce compte.
- Après avoir consommé un crédit de réinitialisation, appelez `account/rateLimits/read` au lieu de déduire de cette réponse les fenêtres actualisées.

### 9) Informez un propriétaire de l’espace de travail d’une limite

Utilisez `account/sendAddCreditsNudgeEmail` pour demander à ChatGPT d’envoyer un e-mail à un propriétaire de l’espace de travail lorsque les crédits sont épuisés ou qu’une limite d’utilisation a été atteinte.

```json
{ "method": "account/sendAddCreditsNudgeEmail", "id": 9, "params": { "creditType": "credits" } }
{ "id": 9, "result": { "status": "sent" } }

Utilisez `creditType: "credits"` lorsque les crédits de l’espace de travail sont épuisés, ou `creditType: "usage_limit"` lorsque la limite d’utilisation de l’espace de travail a été atteinte. Si le propriétaire a déjà été averti récemment, le statut de la réponse est `cooldown_active`.

### 10) Messages de l’espace de travail (ChatGPT)

Utilisez `account/workspaceMessages/read` pour récupérer les messages actifs de l’espace de travail actuel,
y compris les titres des notifications lorsqu’ils sont disponibles.

```json
{ "method": "account/workspaceMessages/read", "id": 10 }
{ "id": 10, "result": { "featureEnabled": true, "messages": [
  { "messageId": "msg_123", "messageType": "headline", "messageBody": "Workspace maintenance starts at 5pm.", "createdAt": 1781395200, "archivedAt": null }
] } }
