<!-- source: https://learn.chatgpt.com/fr-FR/docs/auth -->

## Authentification OpenAI

<a id="sign-in-with-chatgpt"></a>

Codex propose aux utilisateurs deux méthodes de connexion pour utiliser les modèles OpenAI :

- Connexion avec ChatGPT pour un accès par abonnement
- Connexion avec une clé API pour un accès facturé à l’usage

L’application de bureau ChatGPT, Codex CLI et l’extension IDE prennent en charge les deux méthodes de connexion
pour le travail local. Codex Cloud nécessite une connexion avec ChatGPT.

Votre méthode de connexion détermine également les contrôles administratifs et les politiques de traitement des données applicables.

- Lorsque vous vous connectez avec ChatGPT, l’utilisation de Codex respecte les autorisations de votre espace de travail ChatGPT,
le contrôle d’accès basé sur les rôles (RBAC), ainsi que les paramètres de conservation
et de résidence des données de ChatGPT Enterprise.
- Avec une clé API, l’utilisation respecte les paramètres de conservation et
de partage des données de votre organisation API.

Dans les espaces de travail gérés, l’authentification n’est qu’une composante du contrôle d’accès. L’appartenance à l’espace de travail et
le provisionnement déterminent qui peut se connecter, tandis que les licences et
les rôles dans l’espace de travail déterminent les interfaces et fonctionnalités accessibles.
Pour le travail local dans l’application de bureau ChatGPT, Codex CLI ou l’extension IDE,
les profils d’autorisation limitent les actions que l’agent peut effectuer sur l’appareil. Consultez
[Groupes et provisionnement](/fr-FR/codex/enterprise/groups-and-provisioning)
et [Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions)
pour planifier ces contrôles.

### Connectez-vous avec ChatGPT

Lorsque vous vous connectez avec ChatGPT depuis l’application de bureau ChatGPT, Codex CLI ou l’extension IDE, le processus de connexion ouvre une fenêtre de navigateur. Une fois la connexion établie, le navigateur transmet vos identifiants à Codex.

### ChatGPT sur le Web

Ouvrez [ChatGPT](https://chatgpt.com), connectez-vous et choisissez l’espace de travail dans lequel vous
souhaitez travailler. ChatGPT sur le Web conserve la session authentifiée dans votre navigateur.

#### Application de bureau ChatGPT

Sur l’écran de connexion, sélectionnez **Continuer pour se connecter**, puis terminez le
processus dans le navigateur.

#### Codex CLI

Exécutez `codex login`, puis terminez le processus dans le navigateur. Il s’agit de la méthode
d’authentification par défaut lorsqu’aucune session valide n’est disponible.

#### Extension IDE

Sur l’écran de connexion, sélectionnez **Se connecter avec ChatGPT**, puis terminez le
processus dans le navigateur.

<a id="sign-in-with-an-api-key"></a>

### Connectez-vous avec une clé API

Vous pouvez également utiliser une clé API pour vous connecter à l’application de bureau ChatGPT, à Codex CLI ou à l’extension IDE. Récupérez votre clé API dans le [tableau de bord OpenAI](https://platform.openai.com/api-keys).

#### Application de bureau ChatGPT

Sur l’écran de connexion, sélectionnez **Se connecter autrement**, saisissez votre clé, puis
sélectionnez **Continuer**.

#### Codex CLI

Transmettez la clé à `codex login` via stdin :

```shell
printenv OPENAI_API_KEY | codex login --with-api-key

#### Extension IDE

Sur l’écran de connexion, sélectionnez **Utiliser une clé API**, saisissez votre clé, puis sélectionnez
**OK**.

OpenAI facture l’utilisation de la clé API sur votre compte de la plateforme OpenAI, aux tarifs API standard. Consultez la [page des tarifs de l’API](https://openai.com/api/pricing/).

L’authentification par clé API prend en charge les workflows Codex locaux, mais certaines fonctionnalités qui
dépendent de l’accès à l’espace de travail ChatGPT ou de services cloud sont limitées ou indisponibles.
Comparez leur prise en charge selon l’offre dans la section
[Disponibilité des fonctionnalités](/fr-FR/codex/pricing#feature-availability).

Dans Codex CLI et Codex au sein de l’application de bureau ChatGPT, l’authentification par clé API
permet d’accéder aux plugins compatibles sélectionnés par OpenAI. Certains plugins ne sont pas
disponibles, car leur processus de connexion nécessite des fonctionnalités OAuth
non prises en charge. Consultez [Utilisez les plugins](/fr-FR/codex/plugins#api-key-availability).

Lorsque vous vous connectez avec une clé API, Codex applique les tarifs API standard au lieu des
crédits inclus dans l’offre ChatGPT.

Utilisez l’authentification par clé API pour les workflows programmatiques de Codex CLI, tels que les tâches CI/CD.
N’exposez pas l’exécution de Codex dans des environnements non fiables ou publics.

### Vérifiez l’authentification ou déconnectez-vous

Ouvrez le menu du profil pour vérifier le compte et l’espace de travail actifs. Pour mettre fin à la
session ChatGPT sur le Web dans ce navigateur, sélectionnez **Se déconnecter**.

Ouvrez le menu du profil pour afficher le compte actif ou l’état de la clé API. Sélectionnez
**Se déconnecter** pour effacer les identifiants actuels.

Exécutez `codex login status` pour afficher la méthode d’authentification active. Pour une authentification
enregistrée, exécutez `codex logout` afin d’effacer les identifiants actuels. Lorsque
le processus sélectionne l’identité de charge de travail, Codex refuse `codex login` et
`codex logout`, car l’environnement du processus contrôle l’authentification.

Ouvrez le menu du profil pour afficher le compte actif ou l’état de la clé API. Sélectionnez
**Se déconnecter** pour effacer les identifiants actuels.

### Utilisez les jetons d’accès Codex pour l’automatisation en entreprise

Dans les espaces de travail ChatGPT Enterprise, les administrateurs peuvent accorder l’autorisation de créer des jetons d’accès
pour permettre aux membres autorisés de générer des jetons d’accès Codex destinés à des workflows Codex locaux,
de confiance et non interactifs. Utilisez un jeton d’accès lorsqu’une automatisation nécessite l’accès
à un espace de travail ChatGPT, des droits d’accès à Codex gérés par ChatGPT ou les contrôles d’un espace de travail
d’entreprise, sans connexion dans un navigateur.

Les jetons d’accès sont destinés aux scripts de confiance, aux planificateurs et aux runners CI privés.
Pour les appels généraux à l’API OpenAI, continuez d’utiliser des clés API de la plateforme OpenAI.

Pour connaître les étapes de configuration et les recommandations concernant les autorisations, la rotation et la révocation, consultez
[Jetons d’accès](/fr-FR/codex/enterprise/access-tokens).

Si votre plateforme cloud, votre système CI ou votre cluster émet déjà des jetons de charge de travail
à durée de vie limitée, utilisez
la [fédération des identités de charge de travail](/fr-FR/codex/enterprise/workload-identity)
au lieu de stocker un identifiant OpenAI.

Si votre environnement fournit déjà un jeton d’accès Codex, transmettez-le à la CLI :

```shell
printenv CODEX_ACCESS_TOKEN | codex login --with-access-token

## Sécurisez votre compte Codex Cloud

Codex Cloud interagit directement avec votre code source ; il nécessite donc une sécurité renforcée par rapport à de nombreuses autres fonctionnalités de ChatGPT. Activez l’authentification multifacteur (MFA).

Si vous utilisez un fournisseur de connexion tiers (Google, Microsoft ou Apple), vous n’êtes pas tenu d’activer l’authentification multifacteur (MFA) sur votre compte ChatGPT, mais vous pouvez la configurer auprès de ce fournisseur.

Pour obtenir les instructions de configuration, consultez :

- [Google](https://support.google.com/accounts/answer/185839)
- [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661)
- [Apple](https://support.apple.com/en-us/102660)

Si vous accédez à ChatGPT via l’authentification unique (SSO), l’administrateur SSO de votre organisation devrait imposer l’authentification multifacteur (MFA) à tous les utilisateurs.

Si vous vous connectez avec une adresse e-mail et un mot de passe, vous devez configurer l’authentification multifacteur (MFA) sur votre compte avant d’accéder à Codex Cloud.

Si votre compte prend en charge plusieurs méthodes de connexion et que l’une d’elles utilise une adresse e-mail et un mot de passe, vous devez configurer l’authentification multifacteur (MFA) avant d’accéder à Codex, même si vous vous connectez autrement.

<a id="login-caching"></a>

## Mise en cache des informations de connexion

Lorsque vous vous connectez à l’application de bureau ChatGPT, à Codex CLI ou à l’extension IDE avec ChatGPT ou une clé API, vos informations de connexion sont mises en cache et réutilisées. La CLI et l’extension partagent les mêmes informations de connexion en cache. Si vous vous déconnectez de l’une ou de l’autre, vous devrez vous reconnecter au prochain démarrage de la CLI ou de l’extension.

Codex met en cache les informations de connexion localement, dans un fichier en texte brut à l’emplacement `~/.codex/auth.json` ou dans le gestionnaire d’identifiants propre à votre système d’exploitation.

Pour les sessions ouvertes avec ChatGPT, Codex actualise automatiquement les tokens en cours d’utilisation avant leur expiration. Les sessions actives se poursuivent donc généralement sans nécessiter une nouvelle connexion dans le navigateur.

<a id="credential-storage"></a>
<a id="enforce-a-login-method-or-workspace"></a>

## Stockage des identifiants

Utilisez `cli_auth_credentials_store` pour contrôler l’emplacement où Codex CLI stocke les identifiants mis en cache :

```toml
# file | keyring | auto
cli_auth_credentials_store = "keyring"

- `file` stocke les identifiants dans `auth.json`, sous `CODEX_HOME` (par défaut : `~/.codex`).
- `keyring` stocke les identifiants dans le gestionnaire d’identifiants de votre système d’exploitation.
- `auto` utilise le gestionnaire d’identifiants du système d’exploitation lorsqu’il est disponible ; sinon, il utilise `auth.json`.

Consultez la [référence de configuration](/fr-FR/codex/config-file/config-reference) pour connaître le schéma
complet de `config.toml`.

  Si vous utilisez le stockage dans un fichier, traitez `~/.codex/auth.json` comme un mot de passe : il
  contient des jetons d’accès. Ne l’ajoutez pas à un commit, ne le collez pas dans des tickets et ne le partagez pas dans une
  conversation.

## Imposez une méthode de connexion ou un espace de travail

Dans les environnements gérés, les administrateurs peuvent limiter les méthodes d’authentification autorisées pour les utilisateurs :

```toml
# Only allow ChatGPT login or only allow API key login.
forced_login_method = "chatgpt" # or "api"

# When using ChatGPT login, restrict users to a specific workspace.
forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"

Si les identifiants actifs ne respectent pas les restrictions configurées, Codex déconnecte l’utilisateur et s’arrête.

Ces paramètres sont généralement appliqués au moyen de la configuration gérée plutôt que via une configuration propre à chaque utilisateur. Consultez [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration).

## Diagnostics de connexion

Les exécutions directes de `codex login` créent un fichier `codex-login.log` dédié dans
votre répertoire de journaux configuré. Utilisez-le pour diagnostiquer les échecs de connexion via le navigateur ou
par code d’appareil, ou lorsque l’assistance vous demande des journaux spécifiques à la connexion.

## Ensembles de certificats d’AC personnalisés

Si votre réseau utilise un proxy TLS d’entreprise ou une autorité de certification (AC) racine privée, définissez
`CODEX_CA_CERTIFICATE` sur un ensemble de certificats PEM avant de vous connecter. Lorsque
`CODEX_CA_CERTIFICATE` n’est pas défini, Codex utilise `SSL_CERT_FILE` à la place. Les mêmes
paramètres d’AC personnalisés s’appliquent à la connexion, aux requêtes HTTPS normales et aux connexions WebSocket
sécurisées.

```shell

codex login

## Connexion sur des appareils sans interface graphique

Si vous vous connectez à ChatGPT avec Codex CLI, l’interface de connexion dans le navigateur peut ne pas fonctionner dans certaines situations :

- Vous exécutez la CLI dans un environnement distant ou sans interface graphique.
- Votre configuration réseau locale bloque le rappel localhost utilisé par Codex pour renvoyer le token OAuth à la CLI après votre connexion.

Dans ces situations, privilégiez l’authentification par code d’appareil (bêta). Dans l’interface de connexion interactive, choisissez **Se connecter avec un code d’appareil**, ou exécutez directement `codex login --device-auth`. Si l’authentification par code d’appareil ne fonctionne pas dans votre environnement, utilisez l’une des méthodes de secours.

### Méthode recommandée : authentification par code d’appareil (bêta)

1. Activez la connexion par code d’appareil dans les paramètres de sécurité de ChatGPT (compte personnel) ou dans les autorisations de l’espace de travail ChatGPT (administrateur de l’espace de travail).
2. Dans le terminal où vous exécutez Codex, choisissez l’une des options suivantes :
   - Dans l’interface de connexion interactive, sélectionnez **Se connecter avec un code d’appareil**.
   - Exécutez `codex login --device-auth`.
3. Ouvrez le lien dans votre navigateur, connectez-vous, puis saisissez le code à usage unique.

Si la connexion par code d’appareil n’est pas disponible dans votre environnement, utilisez l’une des
méthodes de secours ci-dessous.

### Méthode de secours : authentifiez-vous localement et copiez votre cache d’authentification

Si vous pouvez terminer le processus de connexion sur une machine dotée d’un navigateur, vous pouvez copier vos identifiants en cache sur la machine sans interface graphique.

1. Sur une machine où vous pouvez utiliser le processus de connexion via le navigateur, exécutez `codex login`.
2. Vérifiez que le cache de connexion existe à l’emplacement `~/.codex/auth.json`.
3. Copiez `~/.codex/auth.json` vers `~/.codex/auth.json` sur la machine sans interface graphique.

Traitez `~/.codex/auth.json` comme un mot de passe : il contient des jetons d’accès. Ne l’ajoutez pas à un commit, ne le collez pas dans des tickets et ne le partagez pas dans une conversation.

Si votre système d’exploitation stocke les identifiants dans un gestionnaire d’identifiants plutôt que dans `~/.codex/auth.json`, cette méthode peut ne pas s’appliquer. Consultez
[Stockage des identifiants](/fr-FR/codex/auth#credential-storage) pour savoir comment configurer le stockage dans un fichier.

Copiez le fichier sur une machine distante via SSH :

```shell
ssh user@remote 'mkdir -p ~/.codex'
scp ~/.codex/auth.json user@remote:~/.codex/auth.json

Vous pouvez aussi utiliser une commande en une ligne qui évite `scp` :

```shell
ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json

Copiez le fichier dans un conteneur Docker :

```shell
# Replace MY_CONTAINER with the name or ID of your container.
CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"

Pour une version plus avancée de cette même approche sur des runners CI/CD de confiance, consultez
[Maintenez l’authentification du compte Codex en CI/CD (avancé)](/codex/auth/ci-cd-auth).
Ce guide explique comment permettre à Codex d’actualiser `auth.json` pendant les exécutions normales, puis
de conserver le fichier actualisé pour la tâche suivante. Les clés API restent la solution recommandée
par défaut pour l’automatisation.

### Méthode de secours : redirigez le rappel localhost via SSH

Si vous pouvez rediriger des ports entre votre machine locale et l’hôte distant, vous pouvez utiliser le processus standard via le navigateur en établissant un tunnel vers le serveur de rappel local de Codex (par défaut : `localhost:1455`).

1. Depuis votre machine locale, démarrez la redirection de port :

```shell
ssh -L 1455:localhost:1455 user@remote

2. Dans cette session SSH, exécutez `codex login`, puis ouvrez l’adresse affichée sur votre machine locale.

## Autres fournisseurs de modèles

Lorsque vous définissez un [fournisseur de modèles personnalisé](/fr-FR/codex/config-file/config-advanced#custom-model-providers) dans votre fichier de configuration, vous pouvez choisir l’une des méthodes d’authentification suivantes :

- **Authentification OpenAI** : définissez `requires_openai_auth = true` pour utiliser l’authentification OpenAI. Vous pouvez ensuite vous connecter avec ChatGPT ou une clé API. Cette option est utile lorsque vous accédez aux modèles OpenAI via un serveur proxy LLM. Lorsque `requires_openai_auth = true`, Codex ignore `env_key`.
- **Authentification par variable d’environnement** : définissez `env_key = "<ENV_VARIABLE_NAME>"` pour utiliser une clé API propre au fournisseur issue de la variable d’environnement locale nommée `<ENV_VARIABLE_NAME>`.
- **Aucune authentification** : si vous ne définissez pas `requires_openai_auth` (ou si vous le définissez sur `false`) et que vous ne définissez pas `env_key`, Codex suppose que le fournisseur ne nécessite pas d’authentification. Cette option est utile pour les modèles locaux.
