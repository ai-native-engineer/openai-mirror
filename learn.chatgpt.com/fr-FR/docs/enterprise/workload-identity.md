<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/workload-identity -->

La fédération des identités de charge de travail permet aux automatisations de confiance d’utiliser Codex sans stocker
un token d’accès personnel ni aucune autre information d’identification OpenAI à longue durée de validité. Votre charge de travail
présente un token d’identité à courte durée de validité émis par un fournisseur que vous gérez déjà.
OpenAI vérifie ce token et renvoie un token d’accès à courte durée de validité associé à un utilisateur ou à un
compte de service de votre espace de travail ChatGPT géré.

Utilisez l’identité de charge de travail pour les processus Codex sans surveillance sur les plateformes cloud,
dans Kubernetes, les systèmes CI et les autres environnements capables d’émettre des tokens OIDC ou des
SPIFFE JWT-SVIDs. Pour en savoir plus sur le modèle de confiance partagé et le flux distinct de l’API OpenAI,
consultez la [vue d’ensemble de l’identité de charge de travail](/api/docs/guides/workload-identity-federation).

  La fédération des identités de charge de travail Codex est en version bêta et doit être activée pour votre
  espace de travail. Pour demander l’accès, contactez votre représentant OpenAI ou l’[assistance
  OpenAI](https://help.openai.com/en/articles/6614161-how-can-i-contact-support).

## Avant de commencer

Éléments requis :

- L’autorisation de gérer l’identité de charge de travail dans OpenAI Admin Portal.
- Un espace de travail ChatGPT géré.
- Un utilisateur ChatGPT ou un compte de service membre actif de cet espace de travail,
ou l’autorisation d’en créer un lors de la configuration.
- Un token OIDC ou un SPIFFE JWT-SVID dont vous connaissez l’émetteur, l’audience et les
revendications d’identification.
- Un environnement d’exécution capable de maintenir ce token à jour dans un fichier protégé accessible par un
chemin absolu.
- Codex 0.148.0 ou une version ultérieure.
- Une politique d’authentification Codex applicable qui autorise l’authentification ChatGPT
  et l’espace de travail sélectionné par la règle de fédération. Consultez [Imposer une méthode de
  connexion ou un espace de travail](/fr-FR/codex/auth#enforce-a-login-method-or-workspace).

OpenAI ne crée pas de principal et n’ajoute pas de membre à l’espace de travail lors de l’échange
de tokens. Un administrateur sélectionne ou crée le principal avant que la charge de travail
se connecte. La création d’un utilisateur humain utilise une place dans l’espace de travail et respecte
les règles d’appartenance à cet espace.

Sous Windows natif, utilisez le mode **élevé** du
[Bac à sable Windows](/fr-FR/codex/windows/windows-sandbox). Les autres modes du bac à sable Windows
ne peuvent pas protéger le fichier du token d’identité contre les commandes contrôlées par le modèle.

## Obtenez un token d’identité

L’environnement d’exécution de votre charge de travail obtient et renouvelle le token d’identité en amont. Codex
n’appelle pas les services de métadonnées cloud ni les bibliothèques clientes des fournisseurs d’identité
en votre nom.

| Environnement d’exécution                          | Source recommandée pour le fichier de token                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes, AKS, EKS ou GKE     | Montez un token projeté associé à un compte de service et configurez Codex pour utiliser ce fichier. La plateforme assure sa rotation.                                  |
| Identité managée Microsoft Entra | Exécutez un processus hôte ou un sidecar de confiance qui demande un token à Azure IMDS et remplace le fichier avant l’expiration du token.                |
| Fédération d’identités sortante AWS | Exécutez un processus hôte de confiance qui appelle l’opération `GetWebIdentityToken` du service STS régional et remplace le fichier avant l’expiration du token.                   |
| Google Cloud                     | Exécutez un processus hôte de confiance qui demande un token d’identité au serveur de métadonnées et remplace le fichier avant l’expiration du token.        |
| Oracle Cloud Infrastructure      | Exécutez un processus hôte de confiance qui utilise un principal d’instance pour demander un token d’accès IDCS et remplace le fichier avant l’expiration du token. |
| GitHub Actions                   | Demandez le token OIDC du job, enregistrez-le dans un fichier protégé et demandez un nouveau token avant tout échange ultérieur.                    |
| SPIFFE                           | Utilisez la SPIFFE Workload API ou un utilitaire approuvé pour écrire un JWT-SVID à jour dans le fichier.                                      |
| Fournisseur OIDC personnalisé             | Utilisez le flux de l’émetteur destiné aux charges de travail pour obtenir un JWT, puis mettez à jour le fichier protégé avant l’expiration du JWT.                            |

Suivez le guide de votre fournisseur pour configurer l’émission des tokens et examiner un
token d’exemple :

- [Microsoft Azure](/api/docs/guides/workload-identity-federation/microsoft-azure)
- [AWS](/api/docs/guides/workload-identity-federation/aws)
- [Google Cloud](/api/docs/guides/workload-identity-federation/google-cloud)
- [Oracle Cloud Infrastructure](/api/docs/guides/workload-identity-federation/oracle-cloud)
- [GitHub Actions](/api/docs/guides/workload-identity-federation/github-actions)
- [Kubernetes](/api/docs/guides/workload-identity-federation/kubernetes)
- [SPIFFE](/api/docs/guides/workload-identity-federation/spiffe)

Décodez localement un token d’exemple et notez ses valeurs `iss`, `aud` et `sub`, ainsi que toute autre
revendication à laquelle vous comptez faire confiance. Le décodage ne vérifie pas la signature. Ne collez pas de token
de production sur un site web et ne l’inscrivez pas dans des journaux.

## Connectez la charge de travail

Un administrateur crée le fournisseur et la règle de fédération avant de démarrer
Codex.

1. Ouvrez [Identité de charge de travail](https://admin.openai.com/workload-identity) dans
   OpenAI Admin Portal, puis sélectionnez **Connecter une charge de travail**.
2. Réutilisez un fournisseur configuré pour Codex ou créez-en un. Les préréglages des fournisseurs
préremplissent les paramètres courants pour GitHub Actions, Microsoft Entra ID, Google Cloud,
AWS, Kubernetes, SPIFFE et les fournisseurs OIDC personnalisés.
3. Sélectionnez **Codex** et l’espace de travail géré que la charge de travail est autorisée à utiliser.
4. Ajoutez les conditions les plus restrictives permettant d’identifier la charge de travail. Configurez une correspondance sur un sujet,
des revendications exactes, une condition CEL ou une combinaison de ces critères. Ajoutez des audiences acceptées pour
restreindre les tokens acceptés par la règle. Chaque critère de correspondance configuré doit être satisfait.
5. Associez la règle à un seul utilisateur ChatGPT ou compte de service existant, ou créez-en un
lors de la configuration.
6. Vérifiez le fournisseur, les conditions, l’espace de travail, le principal, les portées et la durée de validité du token
   d’accès. Sélectionnez **Connecter une charge de travail**, puis **Télécharger la configuration**.

Le fichier téléchargé contient un identifiant non secret de règle de fédération et le chemin à partir duquel
Codex lira le token d’identité. Il ne contient aucune information d’identification.

Pour automatiser la configuration, utilisez l’[Admin API dédiée aux identités de charge de
travail](/api/docs/guides/workload-identity-federation/admin-api). Pour comprendre le comportement des critères de correspondance et consulter des exemples,
reportez-vous à la [référence des règles de
fédération](/api/docs/guides/workload-identity-federation/federation-rules).

## Configurez le processus Codex

Le processus qui démarre Codex nécessite ces deux variables d’identité de charge de travail :

```bash

`OPENAI_FEDERATION_RULE_ID` n’est pas un secret. Le fichier de token, en revanche, est confidentiel. Utilisez un chemin
absolu dans un répertoire dédié, tel que `/var/run/secrets/openai.com`, appartenant au
compte de la charge de travail et configuré en mode `0700`. Seuls des processus hôtes de confiance doivent pouvoir
y écrire. Placez ce répertoire en dehors des dépôts et des autres chemins accessibles aux
outils Codex. N’inscrivez aucune information d’identification dans les journaux, l’historique du shell ou les artefacts de build.

### Ajoutez des informations d’attribution pour l’audit

Lorsque plusieurs instances d’exécution partagent une règle de fédération, vous pouvez identifier chaque instance
dans les événements d’audit relatifs à l’émission de tokens. Définissez la variable facultative
`OPENAI_WORKLOAD_IDENTITY_CONTEXT` sur un objet JSON encodé sous la forme d’une
chaîne de caractères :

```bash

  "instance_id": "runner-42",
  "display_name": "payments-prod",
  "labels": {
    "environment": "production",
    "region": "us-west-2"
  }
}'

L’objet doit contenir `instance_id`. Il peut également contenir `display_name` et jusqu’à
huit étiquettes. L’objet encodé ne peut pas dépasser 1 024 octets. `instance_id` et
`display_name` peuvent comporter jusqu’à 128 caractères. Les clés d’étiquette peuvent comporter jusqu’à 64
caractères et les valeurs d’étiquette jusqu’à 256 caractères.

Les identifiants doivent commencer par une lettre ASCII ou un chiffre. Les valeurs peuvent ensuite contenir
des lettres, des chiffres, `.`, `_`, `:`, `/`, `@` et `-`. Les clés d’étiquette acceptent les lettres,
les chiffres, `.`, `_` et `-`.

OpenAI considère ce contexte comme des informations d’attribution d’audit déclarées par le client, et non comme une identité de
charge de travail vérifiée. Il n’a aucune incidence sur l’authentification, l’autorisation, la correspondance des
règles, les portées, les limites de débit, la révocation, les contrôles d’activation des fonctionnalités ou les métriques.
N’y incluez pas d’identifiants, de secrets, de données personnelles, de prompts, de sorties du modèle ni d’autres
contenus client.

Pour un contexte valide, OpenAI calcule un identifiant d’attribution stable propre au locataire,
au fournisseur, à la règle de fédération et à `instance_id`. À des fins d’attribution, le jeton d’accès
contient cet identifiant, mais pas le contexte. L’événement d’audit associé à l’émission réussie du jeton
contient cet identifiant et le contexte normalisé. Si le contexte dépasse une limite ou
ne respecte pas ce schéma, l’échange échoue avec l’erreur `invalid_grant`.

Codex lit le contexte au démarrage du processus et ne le transmet pas, ni l’identifiant de la règle, ni le chemin du fichier de jeton, aux shells, aux hooks ou aux serveurs MCP contrôlés par le modèle. Redémarrez Codex après toute modification du contexte.

### Protégez le fichier de jeton et assurez sa rotation

Pour les déploiements gérés sur Linux, macOS et WSL, ajoutez l’intégralité du répertoire du jeton à
[`permissions.filesystem.deny_read`](/fr-FR/codex/enterprise/managed-configuration#enforce-deny-read-requirements)
dans les exigences gérées :

```toml
[permissions.filesystem]
deny_read = ["/var/run/secrets/openai.com"]

Cela empêche les commandes contrôlées par le modèle de lire le jeton actif ou un jeton de remplacement temporaire, tandis que le processus hôte Codex peut toujours utiliser le jeton pour l’échange. Pour les volumes de jetons projetés, interdisez l’accès à l’intégralité du point de montage du jeton, ainsi qu’à tout chemin cible sous-jacent ou résolu situé en dehors de celui-ci. Les modes d’accès aux fichiers et le nettoyage des variables d’environnement ne suffisent pas, à eux seuls, à protéger les identifiants d’authentification contre un autre processus exécuté sous le même utilisateur. Sous Windows natif, utilisez le bac à sable avec élévation de privilèges décrit ci-dessus.

Pour les sources de jetons qui ne projettent pas de fichier, confiez à un processus hôte de confiance l’écriture de chaque fichier de remplacement dans ce répertoire protégé, puis son renommage à l’emplacement définitif. Un renommage atomique empêche Codex de lire un jeton incomplet. Par exemple, adaptez ce script de renouvellement géré par l’hôte à la commande de récupération de jeton de votre fournisseur. Préparez le répertoire avant d’exécuter le script :

```bash
set -eu
TOKEN_DIR="/var/run/secrets/openai.com"
TOKEN_FILE="$TOKEN_DIR/identity-token"
umask 077
TOKEN_TEMP="$(mktemp "$TOKEN_DIR/.identity-token.XXXXXX")"
trap 'rm -f -- "$TOKEN_TEMP"' EXIT
trap 'exit 1' HUP INT TERM
your-identity-provider-command > "$TOKEN_TEMP"
test -s "$TOKEN_TEMP"
mv -f -- "$TOKEN_TEMP" "$TOKEN_FILE"

Exécutez le processus de renouvellement en dehors de tout shell ou outil que Codex peut contrôler. Maintenez
l’interdiction de lecture pendant le renouvellement et le nettoyage. Même si un arrêt forcé
laisse un fichier temporaire, celui-ci doit rester dans le répertoire
dont la lecture est interdite. Ne placez pas les paramètres d’identité de charge de travail dans `config.toml`.

## Vérifiez la connexion

Chargez l’environnement téléchargé et vérifiez la méthode d’authentification sélectionnée :

```bash
. ./workload-identity-idpm_example.env
codex login status

Dans PowerShell :

```powershell
$env:OPENAI_FEDERATION_RULE_ID = "idpm_..."
$env:OPENAI_IDENTITY_TOKEN_FILE = "C:\run\openai\identity-token"
codex login status

Si la vérification réussit, `Logged in using workload identity` s’affiche. Cela confirme
que Codex a échangé un jeton via la règle de fédération configurée. La commande
n’affiche ni l’espace de travail, ni le principal de sécurité, ni la règle identifiés. Vérifiez ces valeurs
dans le portail d’administration avant de démarrer la charge de travail. Si Codex indique une autre
méthode d’authentification, les deux variables WIF requises n’ont pas été transmises au processus.

Si le fournisseur utilise **Empêcher le rejeu des assertions** et que l’assertion contient une revendication `jti`,
cette vérification consomme ce `jti`. Écrivez une assertion nouvellement émise avec un nouveau
`jti` avant de démarrer un autre processus Codex.

Exécutez une requête simple dans le même environnement :

```bash
codex exec "Reply with only: workload identity is working"

Codex échange le jeton en amont et conserve le jeton d’accès OpenAI en mémoire.
Il ne stocke aucun des deux identifiants d’authentification dans `auth.json`, dans le trousseau système, ni dans
`config.toml`.

## Maintenez le jeton à jour

Renouvelez le fichier du jeton d’identité avant l’expiration du jeton en amont. Codex relit le fichier lorsqu’il a besoin d’un autre jeton d’accès OpenAI. Le jeton OpenAI expire dès que le jeton en amont expire ou que la durée de validité définie par la règle de fédération est atteinte, selon la première échéance. Il n’est jamais valide plus d’une heure.

Lorsqu’un administrateur active la protection contre le rejeu, chaque JWT en amont doit comporter un
`jti` unique. Écrivez une assertion nouvellement émise contenant un nouveau `jti` avant chaque
échange, y compris lors des renouvellements d’un processus de longue durée. Les assertions dépourvues de
`jti` ne bénéficient pas de la protection contre le rejeu.

Codex partage une seule session d’échange en mémoire au sein de chaque processus hôte. Les requêtes simultanées dans ce processus réutilisent un jeton d’accès OpenAI valide et partagent une unique opération de renouvellement à son expiration. Des processus distincts effectuent des échanges distincts ; ils ont donc besoin d’assertions que le fournisseur autorise chacun d’eux à utiliser.

## Priorité des identifiants d’authentification

Les deux variables d’identité de charge de travail requises sont prioritaires sur toutes les autres sources d’identifiants d’authentification :

1. Si l’une des variables `OPENAI_FEDERATION_RULE_ID` ou
`OPENAI_IDENTITY_TOKEN_FILE` est présente, Codex sélectionne l’identité de charge de travail.
2. Si une seule variable requise est présente, Codex renvoie une erreur. Il n’utilise pas de clé API, de jeton d’accès ni de connexion enregistrée comme solution de repli.
3. `OPENAI_WORKLOAD_IDENTITY_CONTEXT` seul ne permet pas de sélectionner l’identité de charge de travail.
4. En l’absence des deux variables WIF requises, Codex applique les règles habituelles
   d’authentification propres à l’interface concernée. Pour les interfaces qui autorisent
   l’authentification par clé API, `CODEX_API_KEY` est prioritaire pour `codex exec`,
`codex review`, le SDK TypeScript et `codex exec-server --remote`. Les autres
   interfaces peuvent utiliser `CODEX_ACCESS_TOKEN` ou une connexion enregistrée.

L’option `apiKey` du SDK est convertie en `CODEX_API_KEY`, mais WIF reste prioritaire
dès que l’une des variables WIF requises est présente. Lorsque vous utilisez WIF, omettez cette option afin que
la charge de travail ne contienne pas d’identifiant d’authentification de longue durée inutilisé.

Pour migrer une charge de travail existante sans interruption, configurez WIF tant que son identifiant d’authentification actuel est encore disponible. Démarrez un nouveau processus avec les deux variables WIF requises ; WIF est prioritaire même si l’ancien identifiant est toujours présent. Une fois que la charge de travail s’exécute correctement avec WIF, supprimez l’ancien identifiant de son environnement d’exécution et de son gestionnaire de secrets, puis révoquez-le. Avant sa révocation, vous pouvez revenir en arrière en supprimant les deux variables WIF requises et en démarrant un nouveau processus.

## Interfaces Codex prises en charge

Configurez l’identité de charge de travail sur la machine qui héberge le processus Codex.

| Interface                                         | Prise en charge et périmètre de l’hôte                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `codex`, `resume` et `fork` en mode interactif       | Pris en charge. Démarrez la CLI dans l’environnement configuré.                                                 |
| `codex exec`, `exec resume` et `codex review` | Pris en charge. La présence de l’une des deux variables WIF requises donne la priorité à WIF.                                      |
| SDK TypeScript                                  | Pris en charge. Le processus parent fournit les variables WIF requises et l’éventuel contexte d’attribution. |
| `codex app-server`                              | Pris en charge. Configurez WIF sur l’hôte app-server, et non sur un client distant.                                |
| `codex exec-server --remote`                    | Pris en charge pour l’authentification auprès du registre des environnements distants. Configurez WIF sur l’hôte exec-server. |
| Opérations locales du processus exec-server            | N’utilisez pas l’authentification WIF. Ces opérations passent par le protocole exec-server local.                         |
| `codex mcp-server`                              | Non pris en charge.                                                                                          |

Les clients app-server et exec-server distants n’envoient jamais le jeton d’identité en amont via leurs protocoles.

## Modifiez ou supprimez l’accès

Les modifications apportées aux sujets, aux audiences, aux revendications, à la condition CEL, aux portées ou à la durée de validité des jetons d’une règle s’appliquent aux nouveaux échanges. Un jeton émis avant la modification peut rester valide jusqu’à son expiration.

Désactivez un fournisseur ou une règle pour interrompre immédiatement l’accès. La désactivation bloque les nouveaux échanges et révoque les jetons d’accès OpenAI déjà émis via cette ressource. L’archivage a le même effet sur l’accès et ne peut pas être annulé. Toute modification de la relation de confiance avec le fournisseur révoque également les jetons émis avant que la nouvelle relation de confiance ne prenne effet.

## Auditez les modifications

La création, la mise à jour et l’archivage des fournisseurs et des règles de fédération génèrent des événements
d’audit. Consultez le [guide de l’API de conformité et des événements
d’audit](/fr-FR/codex/enterprise/compliance-api) pour exporter les événements que votre espace de travail
prend en charge. Rapprochez-les des journaux d’émission de votre fournisseur d’identité et
n’enregistrez ni les assertions en amont ni les jetons d’accès OpenAI dans aucun de ces deux systèmes.

Lorsque le processus fournit `OPENAI_WORKLOAD_IDENTITY_CONTEXT`, les événements d’audit associés à
l’émission réussie d’un jeton contiennent également l’identifiant d’attribution stable et le
contexte normalisé décrits ci-dessus.

## Dépannage

| Symptôme                                                               | Vérification                                                                                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Codex signale une configuration incomplète de l’identité de charge de travail              | Définissez les deux variables requises dans le même processus et utilisez un chemin absolu pour le fichier de jeton.                               |
| Codex indique que sa politique de connexion n’autorise pas l’identité de charge de travail | Autorisez l’authentification ChatGPT dans la politique effectivement appliquée et ajoutez l’espace de travail de la règle à la liste des espaces de travail autorisés. |
| Codex signale un autre identifiant d’authentification                                      | Chargez les deux variables WIF requises dans le processus Codex, puis démarrez un nouveau processus et exécutez à nouveau `codex login status`.  |
| OpenAI rejette le contexte de la charge de travail                                       | Vérifiez sa structure JSON, sa taille, les caractères autorisés et les limites des champs. Supprimez toute donnée sensible ou tout contenu client.            |
| OpenAI rejette le jeton                                              | Comparez `iss`, `aud`, la date d’expiration, la clé de signature et la durée de validité de l’assertion avec la configuration du fournisseur.               |
| La règle ne correspond pas                                               | Confirmez que le client utilise l’identifiant de règle attendu et que chaque vérification des sujets, des audiences, des revendications exactes et des conditions CEL réussit.  |
| OpenAI rejette le principal de sécurité                                          | Vérifiez que l’utilisateur ou le compte de service est actif et qu’il est membre actif de l’espace de travail sélectionné.                   |
| OpenAI rejette une assertion réutilisée                                   | Obtenez un nouveau JWT avec un nouveau `jti` ; ne réessayez pas avec la même assertion protégée contre le rejeu.                                  |
| Un processus de longue durée cesse d’effectuer les renouvellements                               | Vérifiez que le processus de renouvellement de l’hôte remplace toujours le fichier de token avant son expiration.                                  |

Pour plus d’informations sur la vérification du fournisseur, les limites et CEL, consultez la [référence des règles de
fédération](/api/docs/guides/workload-identity-federation/federation-rules).
