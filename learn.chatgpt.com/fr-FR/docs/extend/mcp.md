<!-- source: https://learn.chatgpt.com/fr-FR/docs/extend/mcp -->

Le Model Context Protocol (MCP) relie les modèles à des outils et à du contexte. Utilisez-le pour
donner à ChatGPT ou à Codex accès à de la documentation tierce, ou pour lui permettre
d’interagir avec des outils de développement comme votre navigateur ou Figma.

ChatGPT sur le Web peut utiliser des outils MCP distants fournis par des plugins. Les clients Codex
locaux peuvent également se connecter directement à des serveurs MCP et partager leur configuration.

<a id="supported-mcp-features"></a>

L’application de bureau ChatGPT, Codex CLI et l’extension IDE prennent en charge les serveurs MCP et
partagent la configuration MCP d’un même hôte Codex.

Les fonctionnalités prises en charge ci-dessous s’appliquent aux serveurs MCP configurés sur un hôte
Codex. Les outils hébergés fournis par des plugins peuvent avoir des capacités différentes.

## Fonctionnalités MCP prises en charge

- **Serveurs STDIO** : serveurs qui s’exécutent sous la forme d’un processus local (démarré par une commande).
  - Variables d’environnement
- **Serveurs Streamable HTTP** : serveurs accessibles à une adresse donnée.
  - Authentification par token Bearer
  - Authentification OAuth, y compris les documents de métadonnées d’identifiant client (CIMD) et
l’enregistrement dynamique des clients (DCR)
  - Authentification par session ChatGPT pour les serveurs de confiance fournis par l’éditeur
- **Instructions du serveur** : Codex lit le champ MCP `instructions` renvoyé lors de l’initialisation et utilise son contenu comme consignes applicables à l’ensemble du serveur, en complément des outils de celui-ci.

Si vous développez ou maintenez un serveur MCP pour Codex, utilisez `instructions` pour définir les workflows faisant intervenir plusieurs outils, les contraintes et les limites de débit qui s’appliquent à l’ensemble du serveur. Veillez à ce que les 512 premiers caractères soient compréhensibles à eux seuls, afin que les consignes essentielles soient disponibles lorsque Codex détermine comment utiliser le serveur.

## Connexion de Codex à un serveur MCP

Codex stocke la configuration MCP dans `config.toml`, avec ses autres paramètres de configuration. Par défaut, ce fichier se trouve à l’emplacement `~/.codex/config.toml`, mais vous pouvez également définir des serveurs MCP propres à un projet avec `.codex/config.toml` (projets de confiance uniquement).

L’application de bureau ChatGPT, Codex CLI et l’extension IDE partagent cette configuration.
Une fois vos serveurs MCP configurés, vous pouvez passer d’un client à l’autre sans
refaire la configuration.

### Configuration dans l’application de bureau ChatGPT

1. Ouvrez les **Paramètres**, puis sélectionnez **Serveurs MCP**.
2. Sélectionnez **Ajouter un serveur**.
3. Saisissez un nom, choisissez **STDIO** ou **Streamable HTTP**, puis indiquez la
   commande ou l’URL du serveur.
4. Enregistrez le serveur, puis sélectionnez **Redémarrer**.

La liste des serveurs indique ceux qui sont activés et ceux qui nécessitent OAuth. Sélectionnez
**S’authentifier** lorsqu’un serveur OAuth nécessite une connexion. Dans la zone de saisie, tapez `/mcp`
pour afficher les serveurs connectés.

## Utilisation des outils MCP dans ChatGPT sur le Web

Dans une discussion ChatGPT Work hébergée, installez un [plugin](/fr-FR/codex/plugins) pour utiliser ses
connecteurs et outils MCP distants. Après l’installation, Discussion et Work peuvent
utiliser ces outils. Les administrateurs de l’espace de travail peuvent contrôler les plugins et outils
disponibles.

ChatGPT sur le Web ne lit pas les fichiers de configuration locaux de Codex et n’affiche pas le menu local
des commandes Codex. Ouvrez l’onglet **Plugins** pour parcourir et gérer les outils
disponibles.

### Configuration avec la CLI

#### Ajout d’un serveur MCP

```bash
codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>

Par exemple, pour ajouter Context7 (un serveur MCP gratuit dédié à la documentation pour les développeurs), vous pouvez exécuter la commande suivante :

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp

#### Autres commandes de la CLI

Exécutez `codex mcp list` pour afficher les serveurs configurés. Pour afficher toutes les commandes MCP
disponibles, exécutez `codex mcp --help`. Pour un serveur qui prend en charge OAuth, exécutez
`codex mcp login <server-name>`.

#### Interface utilisateur en terminal (TUI)

Dans l’interface TUI de `codex`, utilisez `/mcp` pour afficher vos serveurs MCP actifs.

### Configuration dans l’extension IDE

1. Ouvrez le menu représenté par une icône d’engrenage, puis sélectionnez **Serveurs MCP**.
2. Sélectionnez **Ajouter un serveur**.
3. Saisissez un nom, choisissez **STDIO** ou **Streamable HTTP**, puis indiquez la
   commande ou l’URL du serveur.
4. Enregistrez le serveur, puis sélectionnez **Redémarrer l’extension**.

La liste des serveurs MCP indique ceux qui sont activés et ceux qui nécessitent OAuth.
Sélectionnez **S’authentifier** lorsqu’un serveur OAuth nécessite une connexion.

### Configuration avec config.toml

Pour un contrôle plus précis, modifiez `~/.codex/config.toml` ou le fichier
`.codex/config.toml` propre à un projet. Consultez la [référence de configuration](/fr-FR/codex/config-file/config-reference)
pour accéder à la liste de toutes les options MCP prises en charge et y effectuer des recherches.

Configurez chaque serveur MCP à l’aide d’une table `[mcp_servers.<server-name>]` dans le fichier de configuration.

<a id="stdio-servers"></a>

#### Serveurs STDIO

- `command` (obligatoire) : commande qui démarre le serveur.
- `args` (facultatif) : arguments à transmettre au serveur.
- `env` (facultatif) : variables d’environnement à définir pour le serveur.
- `env_vars` (facultatif) : variables d’environnement à autoriser et à transmettre.
- `cwd` (facultatif) : répertoire de travail à partir duquel démarrer le serveur.
- `experimental_environment` (facultatif) : définissez cette option sur `remote` pour démarrer le serveur stdio
  via l’environnement d’un exécuteur distant, lorsqu’un tel environnement est disponible.

`env_vars` peut contenir de simples noms de variables ou des objets associés à une source :

```toml
env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]

Pour les entrées sous forme de chaînes et celles qui spécifient `source = "local"`, les valeurs sont lues dans l’environnement local de Codex.
Avec `source = "remote"`, elles sont lues dans l’environnement de l’exécuteur distant, ce qui nécessite
l’exécution distante de serveurs MCP stdio.

<a id="streamable-http-servers"></a>

#### Serveurs Streamable HTTP

- `url` (obligatoire) : adresse du serveur.
- `auth` (facultatif) : méthode d’authentification à essayer après les tokens Bearer et les
  en-têtes d’autorisation configurés. Utilisez `oauth` (valeur par défaut) pour les identifiants OAuth MCP
  enregistrés. Utilisez `chatgpt` pour utiliser la session ChatGPT actuelle auprès de l’origine ChatGPT
  officielle de confiance, avec les identifiants OAuth enregistrés comme solution de repli.
- `bearer_token_env_var` (facultatif) : nom de la variable d’environnement contenant un token Bearer à envoyer dans `Authorization`.
- `http_headers` (facultatif) : association de noms d’en-têtes à des valeurs statiques.
- `env_http_headers` (facultatif) : association de noms d’en-têtes à des noms de variables d’environnement (valeurs extraites de l’environnement).
- `http_headers_helper` (facultatif) : commande locale qui affiche un objet JSON associant
  des noms d’en-têtes à des valeurs de type chaîne, par exemple `{"X-Auth": "temporary-token"}`.
  Prise en charge pour les connexions MCP HTTP établies depuis l’environnement local, mais pas pour
  les serveurs stdio ni les connexions établies via un environnement d’exécution distant.

Codex met en cache les en-têtes fournis par la commande auxiliaire pour la connexion. Lorsqu’une requête POST vers la même origine
renvoie `401` ou `403`, il actualise les en-têtes une fois et ne réessaie que si la
commande auxiliaire renvoie des valeurs différentes. Les tokens Bearer explicites et les identifiants OAuth
ont priorité sur un en-tête `Authorization` fourni par la commande auxiliaire.
Une réponse OAuth `403` signalant une portée d’autorisation insuffisante ne déclenche pas
d’actualisation par la commande auxiliaire.

Si aucune source ne fournit d’identifiants, Codex peut se connecter au serveur sans
authentification. Exécutez séparément `codex mcp login <server-name>` pour lancer une procédure de connexion MCP
avec OAuth.

#### Autres options de configuration

- `startup_timeout_sec` (facultatif) : délai d’attente, en secondes, pour le démarrage du serveur. Valeur par défaut : `10`.
- `tool_timeout_sec` (facultatif) : délai d’attente, en secondes, accordé au serveur pour exécuter un outil. Valeur par défaut : `60`.
- `enabled` (facultatif) : définissez ce paramètre sur `false` pour désactiver un serveur sans le supprimer.
- `required` (facultatif) : définissez ce paramètre sur `true` pour que le démarrage échoue si ce serveur est activé mais ne peut pas s’initialiser.
- `enabled_tools` (facultatif) : liste des outils autorisés.
- `disabled_tools` (facultatif) : liste des outils interdits (appliquée après `enabled_tools`).
- `default_tools_approval_mode` (facultatif) : comportement d’approbation par défaut pour les
  outils de ce serveur. Les valeurs prises en charge sont `auto`, `prompt`, `writes` et
`approve`. Le mode `writes` demande une approbation pour les outils qui ne sont pas marqués comme étant en lecture seule.
- `tools.<tool>.approval_mode` (facultatif) : remplace le comportement d’approbation par défaut pour l’outil concerné.
- `tools.<tool>.output_token_limit` (facultatif) : budget de tokens strictement positif pour la sortie d’un
  outil, avant l’ajout de la marge standard de 20 % pour la sérialisation. Remplace la
  limite de troncature de sortie par défaut du modèle pour cet outil.

Le paramètre de premier niveau `mcp_optional_startup_grace_ms` détermine combien de temps Codex
attend les serveurs MCP facultatifs lors de la création du catalogue initial d’outils. Sa
valeur par défaut est de `1000` millisecondes. Définissez-le sur `0` pour utiliser à la place le délai
`startup_timeout_sec` de chaque serveur. Les serveurs obligatoires continuent d’utiliser leurs délais
de démarrage.

#### Enregistrement des clients OAuth et URL de rappel

Lorsque votre serveur d’autorisation exige un client OAuth préenregistré, indiquez
son identifiant de client lors de l’ajout du serveur MCP :

```bash
codex mcp add example --url https://mcp.example.com --oauth-client-id my-client

Codex affiche l’URL de rappel complète à enregistrer auprès de votre fournisseur :

```text
OAuth callback URL: http://127.0.0.1/callback

Codex enregistre l’URL de rappel avec l’identifiant de client dans `config.toml` pour les connexions
ultérieures :

```toml
[mcp_servers.example]
url = "https://mcp.example.com"

[mcp_servers.example.oauth]
client_id = "my-client"
callback_url = "http://127.0.0.1/callback"

Les clients préenregistrés nouvellement ajoutés n’utilisent une URL de rappel stable que si le
serveur d’autorisation annonce
`authorization_response_iss_parameter_supported: true` et fournit la métadonnée
`issuer`. Si la prise en charge de l’identification de l’émetteur n’est pas annoncée, Codex ajoute un identifiant
de rappel propre au serveur, comme dans `http://127.0.0.1/callback/XuuuHAzzHOni`. Les clients existants
sans URL de rappel enregistrée continuent d’utiliser la redirection propre à leur identifiant de rappel.

Lors de la connexion, le choix de l’URL de rappel dépend de la configuration OAuth et des
métadonnées du serveur d’autorisation :

| Configuration OAuth                                                | Prise en charge de l’identification de l’émetteur           | URL de rappel utilisée                                                                                                                                      |
| ------------------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_url` sans `client_id`                                 | Oui                | L’URL de rappel configurée est utilisée pour l’enregistrement du client.                                                                                           |
| `callback_url` sans `client_id`                                 | Non              | L’URL de rappel configurée est utilisée pour l’enregistrement du client, avec l’identifiant de rappel propre au serveur ajouté à la fin.                                             |
| `client_id` et `callback_url`                                     | Oui                | L’URL de rappel configurée est réutilisée ; la réponse d’autorisation doit contenir la valeur `iss` correspondante.                                                     |
| `client_id` et une `callback_url` se terminant par l’identifiant de rappel correct | Non              | L’URL de rappel configurée est réutilisée telle quelle.                                                                                                       |
| `client_id` et une `callback_url` sans l’identifiant de rappel correct   | Non              | L’URL de rappel configurée est ignorée. Codex utilise `mcp_oauth_callback_url`, ou `http://127.0.0.1/callback` si ce paramètre n’est pas défini, avec l’identifiant de rappel ajouté à la fin. |
| `client_id` sans valeur définie pour `callback_url`                    | Oui ou non | Codex utilise l’URL de rappel globale ou celle par défaut et y ajoute l’identifiant de rappel propre au serveur.                                                           |

Ce mécanisme de repli ne modifie pas l’URL de rappel enregistrée. Codex déduit l’identifiant de rappel
de l’URL du serveur MCP, en incluant son chemin et sa chaîne de requête. Les mêmes
règles de sélection s’appliquent aux connexions automatiques et explicites.

Définissez `mcp_oauth_callback_url` si vous avez besoin d’un chemin de rappel personnalisé ou de l’URL d’entrée d’une
Devbox distante. Les clients préenregistrés nouvellement ajoutés utilisent cette URL telle quelle
si leur fournisseur prend en charge l’identification de l’émetteur. Sinon, ils utilisent
l’URL configurée en y ajoutant l’identifiant de rappel propre au serveur. Enregistrez toujours
l’URL de rappel exacte affichée par `codex mcp add`.

Pour les URL de rappel `http://127.0.0.1` sans port, Codex omet le port d’écoute dans
l’URL qu’il affiche et enregistre, puis insère le port d’écoute actif lors de
l’autorisation. Cette substitution ne s’applique ni à `localhost`, ni aux hôtes IPv6,
ni aux URL HTTPS, ni aux URL de rappel contenant déjà un port. Les serveurs d’autorisation
doivent accepter des ports de bouclage variables conformément à la
[RFC 8252, section 7.3](https://www.rfc-editor.org/rfc/rfc8252#section-7.3).

Définissez `mcp_oauth_callback_port` pour choisir un port d’écoute global fixe, ou définissez
`mcp_servers.<server-name>.oauth.callback_port` pour le remplacer pour un serveur donné.
Un port explicitement indiqué dans l’URL de rappel ne configure pas le port d’écoute. Pour un
rappel direct sur l’interface de bouclage, utilisez `http://127.0.0.1` sans port ou indiquez explicitement le même
port dans l’URL de rappel et dans la configuration du port d’écoute. Un rappel passant par un proxy peut
utiliser volontairement un port dans l’URL externe différent du port d’écoute
local. Avec une URL de rappel locale, Codex écoute sur l’interface locale ; avec une URL de rappel non locale,
il écoute sur `0.0.0.0`.

Codex valide toute valeur `iss` renvoyée avant d’échanger le code d’autorisation. Une
valeur `iss` qui ne correspond pas à celle attendue entraîne toujours le rejet de la réponse. Lorsque la prise en charge de l’identification de l’émetteur est annoncée,
l’absence de `iss` entraîne également son rejet. Dans ces deux cas, le code n’est pas échangé et aucun repli
vers une autre URL de rappel n’est effectué. Une URL de rappel mal formée ou une prise en charge de l’identification de l’émetteur annoncée
sans émetteur dans les métadonnées provoque également un échec bloquant. Consultez
[Authentifier les utilisateurs](/plugins/build/auth).

Si le serveur MCP annonce `scopes_supported`, Codex privilégie les
portées annoncées par ce serveur lors de la connexion OAuth. Sinon, Codex utilise les
portées configurées dans `config.toml`.

#### Enregistrement des clients OAuth

Codex prend en charge les [documents de métadonnées d’identifiant de client OAuth (CIMD)](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)
et l’enregistrement dynamique des clients (DCR). Par défaut, Codex choisit automatiquement
CIMD lorsque le serveur d’autorisation annonce
`client_id_metadata_document_supported: true`, inclut `none` dans
`token_endpoint_auth_methods_supported` et que le rappel utilise une URL de bouclage
prise en charge. Sinon, Codex utilise DCR lorsque cette méthode est disponible. Un identifiant de client OAuth
configuré est toujours prioritaire et évite l’étape d’enregistrement du client.

Pour CIMD, Codex utilise un document de métadonnées hébergé par ChatGPT et propre au
serveur MCP :

```text
https://chatgpt.com/oauth/codex/<callback_id>/client.json

Codex déduit `<callback_id>` de l’URL du serveur MCP et l’ajoute à l’URI de
redirection vers l’interface de bouclage, par exemple
`http://127.0.0.1:<port>/callback/<callback_id>`. Le document de métadonnées enregistre
l’URI de bouclage correspondante sans port. Les serveurs d’autorisation doivent accepter le
port choisi lors de la connexion, tout en vérifiant que l’hôte et le chemin correspondent exactement, conformément à la
[RFC 8252](https://www.rfc-editor.org/rfc/rfc8252.html#section-7.3). L’utilisation d’un hôte, d’un chemin ou de paramètres de requête
personnalisés pour le rappel nécessite DCR ou un identifiant de client OAuth
configuré.

La prise en charge d’un document CIMD stable et partagé est en cours de développement et sera bientôt disponible :

```text
https://chatgpt.com/oauth/codex/client.json

Codex utilisera le document stable avec le chemin partagé `/callback` lorsque le
serveur d’autorisation annoncera
`authorization_response_iss_parameter_supported: true`, fournira une valeur
`issuer` valide dans ses métadonnées et inclura une valeur `iss` correspondante dans les réponses
d’autorisation. Les serveurs dont les réponses ne sont pas liées à l’émetteur continueront d’utiliser le
document propre au rappel.

Pour choisir une méthode d’enregistrement pour une seule connexion via la CLI, utilisez
`--oauth-client-registration` :

```bash
codex mcp login <server-name> --oauth-client-registration cimd
codex mcp login <server-name> --oauth-client-registration dcr

La valeur par défaut est `auto`. Les choix d’enregistrement s’appliquent uniquement à la connexion en cours et
ne sont pas enregistrés dans `config.toml`.

#### Exemples de configuration dans config.toml

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env_vars = ["LOCAL_TOKEN"]

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"

```toml
# Optional MCP OAuth callback overrides (used by `codex mcp login`)
mcp_oauth_callback_port = 5555
mcp_oauth_callback_url = "https://devbox.example.internal/callback"

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }

```toml
[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
enabled_tools = ["open", "screenshot"]
disabled_tools = ["screenshot"] # applied after enabled_tools
default_tools_approval_mode = "prompt"
startup_timeout_sec = 20
tool_timeout_sec = 45
enabled = true

[mcp_servers.chrome_devtools.tools.open]
approval_mode = "approve"
output_token_limit = 30000

### Serveurs MCP fournis par des plugins

Les plugins installés peuvent inclure des serveurs MCP dans leur manifeste. Ces
serveurs sont lancés depuis le plugin ; la configuration utilisateur ne définit donc pas leur
commande de transport. Elle peut néanmoins contrôler leur état d’activation et la politique applicable aux outils
dans `plugins.<plugin>.mcp_servers.<server>`.

```toml
[plugins."sample@test".mcp_servers.sample]
enabled = true
default_tools_approval_mode = "prompt"
enabled_tools = ["read", "search"]

[plugins."sample@test".mcp_servers.sample.tools.search]
approval_mode = "approve"

Les serveurs MCP HTTP fournis par des plugins peuvent aussi déclarer des paramètres OAuth dans `.mcp.json`.
Les manifestes des plugins utilisent les noms de champs en camelCase `clientId`, `callbackUrl` et
`callbackPort` :

```json
{
  "mcpServers": {
    "sample": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "clientId": "my-pre-registered-client",
        "callbackUrl": "http://127.0.0.1/callback/registered"
      }
    }
  }
}

Les serveurs MCP fournis par des plugins suivent les mêmes règles de sélection de l’URL de rappel que les autres
serveurs MCP. Si un plugin fournit un `clientId`, que son fournisseur ne prend pas en charge les
rappels liés à l’émetteur et que `callbackUrl` ne contient pas l’identifiant de rappel propre
au serveur, Codex ignore cette URL pour la connexion et utilise `mcp_oauth_callback_url`, ou
`http://127.0.0.1/callback` si ce paramètre n’est pas défini, en y ajoutant l’identifiant de rappel. La
valeur configurée de `callbackUrl` reste inchangée.

Le paramètre `oauth.callbackPort` d’un plugin est prioritaire sur le paramètre global
`mcp_oauth_callback_port` ; si aucun des deux n’est défini, Codex choisit un port éphémère.
Le port indiqué dans `callbackUrl` ne détermine pas le port d’écoute. Pour un
rappel direct sur l’interface de bouclage avec un port fixe, configurez les deux valeurs de façon à utiliser le même port :

```json
{
  "callbackUrl": "http://127.0.0.1:4321/callback/registered",
  "callbackPort": 4321
}

Avec un point d’entrée distant ou un autre proxy, le port de l’URL de rappel et le port d’écoute
local peuvent volontairement être différents si le proxy relaie les requêtes vers le
processus d’écoute configuré.

## Exemples de serveurs MCP utiles

La liste des serveurs MCP ne cesse de s’allonger. En voici quelques exemples courants :

- [OpenAI Docs MCP](/learn/docs-mcp) : recherchez et consultez la documentation OpenAI pour les développeurs.
- [Context7](https://github.com/upstash/context7) : accédez à une documentation à jour destinée aux développeurs.
- Figma [Local](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) et [À distance](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) : accédez à vos designs Figma.
- [Playwright](https://www.npmjs.com/package/@playwright/mcp) : contrôlez et inspectez un navigateur à l’aide de Playwright.
- [Chrome Developer Tools](https://github.com/ChromeDevTools/chrome-devtools-mcp/) : contrôlez et inspectez Chrome.
- [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex) : accédez aux journaux Sentry.
- [GitHub](https://github.com/github/github-mcp-server) : Gérez les fonctionnalités de GitHub que `git` ne prend pas en charge (par exemple, les pull requests et les issues).
