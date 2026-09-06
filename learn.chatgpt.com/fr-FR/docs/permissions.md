<!-- source: https://learn.chatgpt.com/fr-FR/docs/permissions -->

Bêta. Les profils d’autorisation sont en cours de développement et peuvent changer.

  Les profils d’autorisation ne peuvent pas être combinés avec les anciens paramètres du bac à sable. Configurez
  soit `default_permissions` et `[permissions]`, soit `sandbox_mode` /
`sandbox_workspace_write`, mais pas les deux à la fois. Si `sandbox_mode` figure dans un
  fichier de configuration chargé, si vous utilisez `--sandbox` ou si le profil de configuration sélectionné définit
`sandbox_mode`, Codex utilise ces anciens paramètres du bac à sable au lieu de
`default_permissions`.

Le paramètre géré `allowed_permission_profiles` fait exception : il oblige Codex à utiliser
les profils d’autorisation. Supprimez les anciens paramètres tels que
`sandbox_mode` et `[sandbox_workspace_write]` avant de déployer une liste gérée
de profils autorisés. Pour un déploiement en entreprise sur plusieurs versions, vous pouvez conserver
l’exigence gérée `allowed_sandbox_modes` comme contrainte temporaire de compatibilité
jusqu’à ce que tous les clients utilisent Codex 0.138.0 ou une version ultérieure.

Les profils d’autorisation permettent d’appliquer des limites fondées sur le principe du moindre privilège aux commandes locales
que Codex exécute pour votre compte. Un profil est une stratégie nommée qui combine des règles d’accès au système de fichiers,
qui définissent ce que les commandes peuvent lire ou écrire, avec des règles réseau, qui
définissent les destinations que les commandes peuvent atteindre.

  Dans un profil, `network.enabled = true` autorise les commandes à accéder au réseau, mais
  ne démarre pas le proxy réseau. Pour appliquer les règles de domaine du profil, définissez également
`features.network_proxy = true` dans `config.toml`, ou utilisez des exigences
  `[experimental_network]` activées et gérées par un administrateur. Sans proxy
  actif, les règles de domaine du profil ne limitent pas l’accès direct au réseau.

Utilisez des profils pour accorder à Codex l’accès nécessaire à la discussion en cours sans lui donner
un accès étendu à votre machine ou à votre réseau. Par exemple, un profil en lecture seule peut
permettre à Codex d’inspecter un projet sans le modifier, tandis qu’un profil autorisant l’écriture
peut limiter les modifications à certaines racines de l’espace de travail.

Les profils d’autorisation locaux sont pris en charge sur macOS, Linux, WSL et
Windows natif. Consultez [Portée et application](#scope-and-enforcement) pour connaître les détails
et les points d’attention propres à chaque plateforme.

Pour les paramètres réseau de Codex Cloud, consultez [Accès Internet](/fr-FR/codex/cloud/internet-access).

## Définition et sélection d’un profil

Codex propose trois profils d’autorisation intégrés :

- `:read-only` limite l’exécution des commandes locales à un accès en lecture seule.
- `:workspace` autorise l’écriture dans les racines actives de l’espace de travail et les répertoires temporaires du système.
- `:danger-full-access` supprime les restrictions du bac à sable local et ne doit être utilisé
  que si vous souhaitez délibérément cet accès étendu.

Créez un profil nommé dans `[permissions.<name>]`, puis attribuez à la clé de niveau supérieur
`default_permissions` le nom de ce profil ou celui de l’un des profils intégrés ci-dessus.
Dans cet exemple, `project-edit` est le nom d’un profil défini par l’utilisateur, et non une
valeur intégrée.

Les administrateurs d’entreprise peuvent définir des profils et limiter ceux que
les utilisateurs peuvent sélectionner via le fichier géré `requirements.toml`. Dès que
`allowed_permission_profiles` est présent, tout profil qui n’y figure pas est interdit,
y compris les profils intégrés qui n’y figurent pas et ceux ajoutés dans de futures versions de Codex. Consultez
[Contrôler les profils d’autorisation disponibles](/fr-FR/codex/enterprise/managed-configuration#control-available-permission-profiles)
pour connaître la configuration gérée recommandée.

Les profils personnalisés reposent sur deux concepts associés :

- `[permissions.<name>.workspace_roots]` ajoute des répertoires précis à considérer
  comme des racines de l’espace de travail pour ce profil.
- `[permissions.<name>.filesystem.":workspace_roots"]` définit les règles d’accès au système de fichiers
  que Codex applique dans chaque racine effective de l’espace de travail : les racines de l’espace de travail
  de la session actuelle définies à l’exécution, auxquelles s’ajoutent les racines définies ci-dessus par le profil.

Les profils suivent également le modèle habituel de couches de configuration. Les couches prioritaires peuvent
ajouter ou remplacer des entrées sous un même nom de profil sans avoir à redéfinir
l’intégralité du profil.

Par exemple, une configuration au niveau de l’organisation et une configuration au niveau de l’utilisateur peuvent étendre
le même profil indépendamment :

```toml
# /etc/codex/config.toml
[permissions.server.workspace_roots]
"~/code/server" = true

```toml
# ~/.codex/config.toml
[permissions.server.workspace_roots]
"~/code/mobile-app" = true

Lorsque `server` est actif, les deux racines de l’espace de travail font partie du
profil effectif.

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"
"objects.githubusercontent.com" = "allow"
"*.github.com" = "allow"
"tracking.example.com" = "deny"

Ce profil :

- Donne accès en lecture aux seuls chemins nécessaires à l’exécution des outils de développement courants.
- Applique les mêmes règles aux racines de l’espace de travail de la session actuelle et aux
racines définies par le profil.
- Maintient les paramètres connexes à l’IDE tels que `.devcontainer/` en lecture seule sous chaque
  racine.
- Interdit, au moyen d’une règle glob, l’accès aux fichiers d’environnement correspondants.
- N’autorise l’accès au réseau que par l’intermédiaire de la stratégie de domaine configurée.

Dans un profil actif, les règles d’interdiction plus précises restent en vigueur même lorsqu’un chemin
plus général est accessible en lecture ou en écriture. Par exemple, un profil peut rendre les racines de l’espace de travail
accessibles en écriture tout en attribuant à un chemin `.env` correspondant la valeur `deny`.

## Extension d’un profil

Utilisez `extends` lorsqu’un profil est très similaire à un profil intégré ou à un autre profil
nommé. Préférez étendre un profil intégré plutôt que d’en créer un de toutes pièces afin de
conserver les protections de base. Par exemple, l’extension de `:workspace` maintient
le répertoire `.codex` de la racine de l’espace de travail en lecture seule, sauf si vous
redéfinissez explicitement cette règle. Définissez le parent une seule fois, puis ajoutez ou redéfinissez uniquement les règles qui
diffèrent.

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
description = "Project editing with OpenAI API access."
extends = ":workspace"

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

Ce profil se fonde sur `:workspace`, maintient l’interdiction des fichiers correspondant à `.env` et
autorise les requêtes vers `api.openai.com`. Un profil peut étendre `:read-only`,
`:workspace` ou un autre profil nommé. Il ne peut pas étendre
`:danger-full-access` ; Codex refuse également les parents inconnus et les cycles
d’héritage.

## Spécification de la configuration

| Entrée                                                             | Type / valeurs              | Valeur par défaut                 | Détails                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default_permissions`                                             | Nom de profil (chaîne)        | Aucune                    | Indique le profil d’autorisation appliqué par défaut par Codex. Il doit correspondre à un profil sous `[permissions]` ou à un profil intégré tel que `:workspace`. Définissez-le explicitement pour garantir un comportement prévisible ; les exigences gérées ne peuvent omettre ce paramètre que si `:workspace` et `:read-only` sont tous deux explicitement autorisés. Codex utilise les anciens paramètres du bac à sable, sauf si le paramètre géré `allowed_permission_profiles` lui indique d’utiliser les profils d’autorisation dans cette configuration. |
| `[permissions.<name>]`                                            | Table                      | Aucune                    | Définit un profil nommé. `default_permissions` sélectionne un profil par défaut ; les autres paramètres liés aux profils d’autorisation utilisent également le nom du profil.                                                                                                                                                                                                                                                                               |
| `permissions.<name>.description`                                  | Chaîne                     | Aucune                    | Fournit une description du profil lisible par l’utilisateur. Un profil n’hérite pas de la description de son parent via `extends`.                                                                                                                                                                                                                                                                                                 |
| `permissions.<name>.extends`                                      | Nom de profil (chaîne)        | Aucune                    | Initialise ce profil à partir d’un autre profil nommé ou de l’un des profils intégrés `:read-only` ou `:workspace`. Codex refuse `:danger-full-access`, les parents inconnus et les cycles d’héritage.                                                                                                                                                                                                                                            |
| `[permissions.<name>.workspace_roots]`                            | Table                      | Aucune                    | Ajoute des racines de l’espace de travail définies par le profil, auxquelles les règles d’accès au système de fichiers `:workspace_roots` s’appliquent au même titre qu’aux racines de l’espace de travail de la session actuelle définies à l’exécution.                                                                                                                                                                                                                                                                                |
| `permissions.<name>.workspace_roots."<path>"`                     | Booléen                    | `false`                 | Ajoute le chemin à l’ensemble des racines de l’espace de travail du profil lorsque la valeur est `true`. Les entrées dont la valeur est `false` restent inactives.                                                                                                                                                                                                                                                                                                                        |
| `[permissions.<name>.filesystem]`                                 | Table                      | Aucune                    | Associe les chemins du système de fichiers à des valeurs d’accès ou à des tables de sous-chemins à portée limitée. En l’absence de table du système de fichiers, ou si celle-ci est vide, l’accès au système de fichiers reste restreint et un avertissement est émis au démarrage.                                                                                                                                                                                                                                                               |
| `permissions.<name>.filesystem.glob_scan_max_depth`               | Nombre                     | Aucune                    | Limite l’expansion des motifs glob d’interdiction de lecture sur Linux, WSL et Windows natif lorsque Codex prend un instantané des correspondances avant le démarrage du bac à sable. Des valeurs plus élevées peuvent accroître la charge d’analyse au démarrage. Utilisez une valeur d’au moins `1` lorsqu’un motif `**` non borné nécessite une pré-expansion bornée.                                                                                                                                                              |
| `[permissions.<name>.filesystem]."<path>"`                        | `read`, `write` ou `deny` | Aucune                    | Accorde un accès direct à un chemin pris en charge. `deny` refuse l’accès et prévaut sur les entrées `write` ou `read` de même spécificité. Codex refuse les règles d’écriture directe que l’environnement d’exécution actif ne peut pas appliquer.                                                                                                                                                                                                                            |
| `[permissions.<name>.filesystem."<path>"]."<subpath>"`            | `read`, `write` ou `deny` | Aucune                    | Accorde l’accès à un descendant de `<path>`. Utilisez `.` pour le chemin de base. Les autres sous-chemins doivent être des descendants relatifs et ne peuvent pas contenir de composants `.` ou `..`.                                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network]`                                    | Tableau                      | Aucune                    | Configure l’accès réseau des commandes et la politique appliquée par un proxy réseau actif. Activez `features.network_proxy`, sauf si le proxy est démarré par des exigences réseau définies par un administrateur.                                                                                                                                                                                                                                    |
| `permissions.<name>.network.enabled`                              | Booléen                    | `false`                 | Active l’accès réseau pour les commandes du profil. Cette option ne démarre pas le proxy réseau ; en l’absence de proxy actif, les commandes peuvent se connecter directement sans restriction de domaine.                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network.domains]`                            | Tableau                      | Aucune                    | Associe les motifs de noms d’hôte à `allow` ou à `deny`. Les règles s’appliquent uniquement lorsque le proxy réseau est actif. En l’absence d’entrées `allow`, le proxy actif bloque les requêtes vers des domaines, et les entrées de refus priment sur les entrées d’autorisation.                                                                                                                                                                                                                 |
| `permissions.<name>.network.domains."<pattern>"`                  | `allow` ou `deny`          | Aucune                    | Prend en charge les noms d’hôte exacts, `*.example.com` pour les sous-domaines, `**.example.com` pour le domaine racine et ses sous-domaines, et `*` comme caractère générique global réservé aux autorisations. Les motifs de noms d’hôte sont normalisés en supprimant les espaces en début et en fin, en les convertissant en minuscules et en retirant le point final, les ports simples ou les crochets.                                                                                                                                                           |
| `[permissions.<name>.network.unix_sockets]`                       | Tableau                      | Aucune                    | Définit les dérogations à la liste d’autorisation des sockets Unix. Utilisez-les uniquement pour les intégrations locales telles que Docker.                                                                                                                                                                                                                                                                                                                                         |
| `permissions.<name>.network.unix_sockets."<path>"`                | `allow` ou `deny`          | Aucune                    | Ajoute un chemin absolu de socket Unix à la liste d’autorisation effective avec `allow`, ou le rejette avec `deny`. Les entrées refusées sont omises de la liste d’autorisation effective.                                                                                                                                                                                                                                                                |
| `permissions.<name>.network.proxy_url`                            | Chaîne d’URL                 | `http://127.0.0.1:3128` | Point d’écoute du proxy HTTP utilisé pour `HTTP_PROXY`, `HTTPS_PROXY`, les variables de proxy WebSocket et les variables d’environnement de proxy connexes des outils.                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.enable_socks5`                        | Booléen                    | `true`                  | Active le point d’écoute SOCKS5 utilisé pour `ALL_PROXY` et les variables de proxy FTP.                                                                                                                                                                                                                                                                                                                                                     |
| `permissions.<name>.network.socks_url`                            | Chaîne d’URL                 | `http://127.0.0.1:8081` | Adresse du point d’écoute SOCKS5.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `permissions.<name>.network.enable_socks5_udp`                    | Booléen                    | `true`                  | Active la prise en charge d’UDP par SOCKS5 lorsque le point d’écoute SOCKS5 est activé.                                                                                                                                                                                                                                                                                                                                                               |
| `permissions.<name>.network.allow_upstream_proxy`                 | Booléen                    | `true`                  | Permet au proxy réseau du bac à sable de tenir compte des paramètres `HTTP(S)_PROXY` et `ALL_PROXY` définis en amont pour les requêtes sortantes.                                                                                                                                                                                                                                                                                                          |
| `permissions.<name>.network.allow_local_binding`                  | Booléen                    | `false`                 | Désactive la protection contre l’accès aux réseaux locaux ou privés lorsque la valeur est `true`. Lorsque la valeur est `false`, les cibles locales indiquées littéralement, comme `localhost` ou `127.0.0.1`, doivent être ajoutées explicitement à la liste d’autorisation, tandis que les noms d’hôte qui se résolvent en adresses IP locales ou privées restent bloqués.                                                                                                                                                                                                |
| `permissions.<name>.network.dangerously_allow_non_loopback_proxy` | Booléen                    | `false`                 | Autorise les points d’écoute du proxy à écouter sur des adresses autres que les adresses de bouclage. Ne définissez pas cette option pour le développement local standard.                                                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.dangerously_allow_all_unix_sockets`   | Booléen                    | `false`                 | Contourne la liste d’autorisation des sockets Unix lorsque le proxy de sockets Unix est pris en charge. Ce mécanisme de contournement local est très permissif.                                                                                                                                                                                                                                                                                                               |

## Autorisations du système de fichiers

Les entrées du système de fichiers utilisent `read`, `write` ou `deny` :

| Accès  | Signification                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `read`  | Autorise les commandes à lire les fichiers et à lister les répertoires sous ce chemin. Elles ne peuvent pas y créer, modifier, renommer ni supprimer de fichiers. |
| `write` | Autorise les commandes à lire et à modifier les fichiers sous ce chemin, notamment à en créer, en renommer et en supprimer lorsque le système d’exploitation le permet.  |
| `deny`  | Interdit la lecture comme l’écriture sous ce chemin. Utilisez cette valeur pour interdire un sous-chemin au sein d’une autorisation `read` ou `write` plus étendue.         |

Les entrées plus spécifiques priment sur les entrées plus générales. Lorsque deux entrées ciblent le
même chemin, `deny` est prioritaire sur `write`, et `write` est prioritaire
sur `read`.

Cet ordre de priorité permet à un profil de décrire d’abord une vaste zone de travail, puis d’en exclure
les fichiers ou répertoires qui doivent rester inaccessibles en lecture :

```toml
[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

Dans cet exemple, la racine de l’espace de travail reste accessible en écriture, `.devcontainer/` reste
accessible en lecture sans devenir accessible en écriture, et les fichiers d’environnement correspondants restent
inaccessibles aux commandes exécutées en bac à sable.

Un chemin plus spécifique peut également réautoriser l’accès à un sous-arbre plus restreint au sein d’une interdiction plus générale :

```toml
[permissions.project-edit.filesystem]
"~/Documents" = "deny"
"~/Documents/codex" = "write"

Formats de chemin pris en charge :

| Chemin               | Signification                                                                                     | Limitation aux sous-chemins |
| ------------------ | ------------------------------------------------------------------------------------------- | --------------- |
| `:root`            | La racine du système de fichiers                                                                         | `.` uniquement        |
| `:minimal`         | Chemins de la plateforme et de l’environnement d’exécution requis par les outils courants                                           | `.` uniquement        |
| `:workspace_roots` | Les racines de l’espace de travail de la session en cours et toutes les racines d’espace de travail définies par le profil qui sont activées      | Oui             |
| `:tmpdir`          | L’emplacement `$TMPDIR`, lorsqu’il est disponible                                               | `.` uniquement        |
| `:slash_tmp`       | Le dossier `/tmp`, s’il existe                                                             | `.` uniquement        |
| `/absolute/path`   | Un chemin absolu propre à la plateforme, tel que `/path` sur macOS/Linux/WSL ou `C:\path` sur une installation native de Windows | Oui             |
| `~/path`           | Un chemin dans le répertoire personnel de l’utilisateur courant                                              | Oui             |

Sous Windows natif, les chemins relatifs au répertoire personnel peuvent également utiliser des barres obliques inverses, comme
`~\work`.

Utilisez `:root` uniquement lorsqu’un profil doit délibérément bénéficier d’un accès étendu en lecture :

```toml
[permissions.audit.filesystem]
":root" = "read"

Utilisez des entrées imbriquées sous `:workspace_roots` pour limiter l’accès aux sous-chemins
relatifs à la racine de l’espace de travail :

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"          # each workspace root
"docs" = "read"        # each workspace-root docs directory
"generated" = "deny"   # each workspace-root generated directory

Les sous-chemins imbriqués doivent rester dans leur racine d’espace de travail. Toute remontée vers un répertoire parent, comme
`../other-repo`, est refusée.

### Interdire la lecture à l’aide de chemins exacts ou de motifs glob

Utilisez `deny` pour les fichiers ou sous-arborescences que Codex ne doit pas lire, même si une règle plus générale du profil
autorise l’accès à proximité. Les chemins exacts conviennent aux emplacements stables,
comme `~/.ssh`. Les motifs glob sont plus adaptés lorsqu’un profil doit couvrir un ensemble
de fichiers sensibles dont l’emplacement exact varie d’un dépôt à l’autre.

Lorsqu’un motif glob figure sous `:workspace_roots`, Codex l’interprète par rapport à chaque
racine d’espace de travail effective. Par exemple :

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

Cette règle interdit la lecture des fichiers `.env` correspondants situés sous chaque racine d’espace de travail définie à l’exécution ou
dans le profil. Utilisez-la pour préserver les écritures habituelles dans l’espace de travail
tout en empêchant la lecture des fichiers d’environnement, des secrets générés ou des fichiers similaires
contenant des données d’authentification.

Les motifs glob `deny` sont pris en charge comme règles d’interdiction de lecture. Les motifs glob `read` ou `write`
sont moins portables dans les bacs à sable Linux, WSL et Windows natif ; privilégiez donc les chemins
exacts ou les règles de sous-arborescence telles que `"docs/**" = "read"` lorsque c’est possible.

Sous Linux, WSL et Windows natif, un motif `**` non borné d’interdiction de lecture peut nécessiter
une pré-expansion à profondeur limitée avant le démarrage du bac à sable. Définissez `glob_scan_max_depth` lorsque
vous utilisez un motif non borné tel que `"**/*.env" = "deny"` :

```toml
[permissions.project-edit.filesystem]
glob_scan_max_depth = 3

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

La valeur de `glob_scan_max_depth` doit être au moins égale à `1`. Des valeurs plus élevées entraînent une analyse plus approfondie avant
le démarrage du bac à sable, ce qui peut augmenter la charge au démarrage sous Linux, WSL et Windows natif.
Si vous préférez éviter l’expansion à profondeur limitée, énumérez explicitement les niveaux, par exemple
`*.env`, `*/*.env` et `*/*/*.env`.

Ajoutez des racines d’espace de travail réutilisables au profil lorsque les mêmes règles doivent s’appliquer
au-delà de la racine de la session en cours :

```toml
[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

Lorsque ce profil est actif, Codex applique les règles `:workspace_roots` aux
racines d’espace de travail définies à l’exécution pour la session en cours, ainsi qu’à chaque racine
d’espace de travail définie et activée dans le profil.

Sous Windows natif, les chemins comportant une lettre de lecteur, tels que `D:\work`, et les chemins UNC, tels que
`\\server\share`, sont acceptés comme chemins absolus.

## Autorisations réseau

L’accès au réseau et le filtrage réseau sont deux paramètres distincts. Définissez
`permissions.<name>.network.enabled = true` pour permettre aux commandes d’accéder au réseau,
et activez `features.network_proxy` pour appliquer les règles de domaine du profil :

```toml
[features]
network_proxy = true

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"example.com" = "allow"      # exact host
"*.example.com" = "allow"    # subdomains only
"**.example.com" = "allow"   # apex and subdomains
"ads.example.com" = "deny"   # deny wins over allow

Le comportement obtenu dépend de ces deux paramètres :

- Réseau désactivé : les commandes ne peuvent pas accéder au réseau, quel que soit l’état
de la fonctionnalité de proxy.
- Réseau activé, proxy désactivé : les commandes disposent d’un accès direct et illimité
au réseau. Les règles de domaine du profil d’autorisations ne sont pas appliquées.
- Réseau activé, proxy activé : les commandes utilisent le proxy, qui applique les règles
de domaine du profil. Si le proxy actif n’autorise aucun domaine, il bloque les destinations
externes.

Ajouter `[permissions.<name>.network.domains]` ou définir
`permissions.<name>.network.enabled = true` n’active pas
`features.network_proxy`. Les administrateurs peuvent également activer le
proxy avec `[experimental_network]` dans `requirements.toml`. Consultez la section
[Configuration gérée](/fr-FR/codex/enterprise/managed-configuration#configure-network-access-requirements).

Lorsqu’il est actif, le proxy réseau du bac à sable se lie par défaut à des points d’écoute locaux :

```toml
[permissions.project-edit.network]
enabled = true
proxy_url = "http://127.0.0.1:3128"
enable_socks5 = true
socks_url = "http://127.0.0.1:8081"
enable_socks5_udp = true

Conservez les valeurs par défaut de ces paramètres d’écoute, sauf en cas d’intégration avec
un environnement d’exécution particulier. Les clés réseau `dangerously_*` sont des mécanismes de contournement destinés aux
environnements spécialisés et ne doivent pas être utilisées pour le développement local courant.

### Réseaux locaux et privés

Lorsque le proxy réseau est actif, Codex applique par défaut une protection des réseaux locaux et privés
contre le rebinding DNS et l’accès accidentel aux services locaux. Pour autoriser délibérément
une cible locale sous forme littérale, ajoutez le nom d’hôte exact ou l’adresse IP littérale
à la liste d’autorisation :

```toml
[permissions.project-edit.network.domains]
"localhost" = "allow"
"127.0.0.1" = "allow"

Définissez `allow_local_binding = true` uniquement lorsque le profil doit accéder à des noms d’hôte figurant dans la liste d’autorisation
et qui se résolvent en adresses locales ou privées :

```toml
[permissions.project-edit.network]
enabled = true
allow_local_binding = true

[permissions.project-edit.network.domains]
"localhost" = "allow"

### Sockets Unix

Le proxy des sockets Unix constitue un mécanisme de contournement local pour des outils comme Docker. Utilisez-le
avec parcimonie :

```toml
[permissions.project-edit.network.unix_sockets]
"/var/run/docker.sock" = "allow"
"/tmp/old.sock" = "deny"

Utilisez `deny` pour refuser un chemin de socket, y compris s’il bénéficie d’une autorisation héritée. Les chemins de socket refusés
sont omis de la liste d’autorisation effective.

Lorsque les sockets Unix sont activés, veillez à ce que les points d’écoute du proxy restent liés à des adresses de bouclage.

## Migration depuis les anciens paramètres du bac à sable

Les profils d’autorisations remplacent l’ancienne combinaison de `sandbox_mode` et de
`sandbox_workspace_write` lorsque vous souhaitez qu’un seul profil réutilisable définisse à la fois
le comportement du système de fichiers et celui du réseau. Pour chaque session, utilisez l’un ou l’autre système,
jamais les deux.

Points de départ suggérés :

- Pour un workflow en lecture seule, utilisez le profil intégré `:read-only` ou définissez un
  profil personnalisé qui n’autorise la lecture que là où elle est nécessaire.
- Pour modifier l’espace de travail, utilisez le profil intégré `:workspace` ou définissez un
  profil personnalisé qui autorise l’écriture via `:workspace_roots` et ajoute uniquement les chemins
  temporaires ou de cache supplémentaires dont le workflow a besoin.
- Pour une exécution locale sans restriction, n’utilisez `:danger-full-access` que si vous
  souhaitez délibérément adopter le modèle d’accès local le plus large.

Les profils définissent le niveau d’accès local par défaut d’une session. Les exigences gérées par l’organisation
peuvent néanmoins imposer des restrictions que la configuration utilisateur ne doit pas
assouplir. Consultez la section [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration)
pour connaître les contraintes relatives au système de fichiers et au réseau imposées par les administrateurs.

## Portée et application des règles

Les profils d’autorisations définissent les limites de l’exécution locale des commandes
dans le bac à sable. Utilisez-les avec les politiques d’approbation et les contrôles distincts
applicables à la recherche web, aux connecteurs, aux serveurs MCP, au navigateur intégré, à l’Utilisation de l’ordinateur
et à Codex Cloud.

### Ce que contrôlent les profils

- **Exécution locale des commandes :** Les profils d’autorisations régissent les commandes exécutées dans le bac à sable
  sur votre machine. Les connecteurs, les serveurs MCP, les interfaces de navigation ou
  d’utilisation de l’ordinateur, les paramètres des environnements Codex Cloud et les élévations
  approuvées disposent de leurs propres contrôles.
- **Écritures dans le système de fichiers :** Un profil autorisant l’écriture peut entraîner des modifications persistantes.
  Considérez comme sensibles les écritures dans les scripts, les étapes de build, les hooks des gestionnaires de paquets, les fichiers de démarrage
  du shell et les répertoires partagés, car d’autres outils ou utilisateurs peuvent ensuite
  exécuter ces fichiers en dehors du contexte initial du bac à sable.
- **Destinations des connexions sortantes :** Les règles de domaine réseau ne limitent les destinations du trafic généré par les commandes
  exécutées dans le bac à sable que lorsque le proxy réseau est actif. Elles ne permettent pas
  de déterminer si une destination autorisée est fiable, et les règles d’autorisation avec caractères génériques
  conservent une portée étendue.
- **Services locaux :** Lorsqu’il est actif, le proxy réseau bloque par défaut les cibles des réseaux locaux et privés.
  Ajouter `localhost`, des adresses IP privées ou des sockets Unix à la liste d’autorisation, ou définir
`allow_local_binding = true`, ouvre explicitement l’accès aux services locaux.

### Ce que le proxy réseau ne contrôle pas

Le proxy réseau filtre uniquement le trafic des commandes locales exécutées dans le
bac à sable. Il n’applique pas la liste d’autorisation de domaines du profil aux éléments suivants :

- **Recherche web :** L’outil de recherche hébergé utilise ses propres paramètres d’accès. Utilisez
`web_search` et, pour les clients gérés, `allowed_web_search_modes` pour le contrôler.
  `tools.web_search.allowed_domains` filtre les résultats de recherche, et non l’accès des commandes
  au réseau.
- **Applications et connecteurs :** Les outils reposant sur des connecteurs utilisent leurs propres connexions côté service,
  autorisations d’espace de travail et paramètres d’application ou d’outil.
- **Serveurs MCP :** Les serveurs MCP locaux et distants utilisent leur propre processus ou
  mode de transport. Contrôlez-les à l’aide de la configuration `mcp_servers` et des listes
  d’autorisation de serveurs gérées.
- **Navigateur et Utilisation de l’ordinateur :** La navigation dans le navigateur et les actions effectuées sur l’ordinateur
  sont soumises à leurs propres contrôles de fonctionnalité et d’approbation.
- **Trafic des services Codex :** Les requêtes liées aux modèles, à l’authentification et aux autres services du client
  utilisent des paramètres HTTP et de proxy système distincts, propres au client.
- **Codex Cloud :** Ces tâches utilisent les
[paramètres d’accès à Internet](/fr-FR/codex/cloud/internet-access) propres à leur environnement.

Pour restreindre ces surfaces, configurez directement chaque fonctionnalité. Une liste
d’autorisation réseau pour les commandes ne constitue pas une politique réseau globale applicable à toutes les actions que Codex peut effectuer.

### Mécanismes d’application des règles

- Sur macOS, Codex utilise les profils de bac à sable Seatbelt. Si le bac à sable de la plateforme ne peut pas
appliquer la politique sélectionnée, Codex refuse d’exécuter la commande plutôt que de l’exécuter
hors du bac à sable sans avertissement.
- Sous Linux et WSL, Codex utilise [bubblewrap](https://github.com/containers/bubblewrap)
  et [seccomp](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html),
  avec Landlock comme solution de repli pour assurer la compatibilité. Le mécanisme
  d’application le plus strict dépend des espaces de noms utilisateur et de la prise en charge du noyau ; les hôtes de conteneurs
  soumis à des restrictions peuvent imposer des modes de compatibilité, et les politiques de séparation des accès non prises en charge
  sont refusées.
- Sous Windows natif, le [bac à sable `elevated`](/fr-FR/codex/windows/windows-sandbox#windows-sandbox)
  offre la protection la plus élevée, car il peut utiliser des comptes utilisateur dédiés au bac à sable et dotés de privilèges réduits,
  des limites d’autorisations du système de fichiers et des règles de pare-feu. Le bac à sable `unelevated`
  constitue une solution de repli dont l’isolation réseau est moins stricte et qui ne permet pas d’appliquer
  toutes les exceptions distinguant les droits de lecture et d’écriture ; les politiques non prises en charge sont donc refusées. Utilisez WSL
  si vous avez besoin du modèle de bac à sable Linux.

### Recommandations opérationnelles

Choisissez le profil le plus restrictif permettant néanmoins d’accomplir la tâche, en particulier lorsque
vous autorisez l’écriture ou l’accès au réseau sortant. Adaptez la politique d’approbation, la gestion des secrets
et les règles d’autorisation à ce niveau d’accès.

## Profils courants

### Lecture seule avec liste d’autorisation réseau

```toml
default_permissions = "readonly-net"

[features]
network_proxy = true

[permissions.readonly-net.filesystem]
":minimal" = "read"

[permissions.readonly-net.filesystem.":workspace_roots"]
"." = "read"

[permissions.readonly-net.network]
enabled = true

[permissions.readonly-net.network.domains]
"api.openai.com" = "allow"

### Accès aux fichiers limité à l’espace de travail

Voici un exemple de profil d’autorisations qui permet à Codex d’écrire dans les dossiers de votre espace de travail tout en lui interdisant de lire le reste du système de fichiers (à quelques exceptions près, définies par `:minimal`).

```toml
default_permissions = "workspace-only"

[permissions.workspace-only]
# By extending the :workspace profile, you get Codex's safeguards to ensure
# subfolders such as .codex/ and .git/ within a workspace root are read-only
# while the rest of the folder is writable.
extends = ":workspace"

[permissions.workspace-only.filesystem]
# By default, deny read access to all files on disk.
":root" = "deny"

# Though in practice, a software agent needs to be able to read folders that
# contain common tools, such as `/usr/bin`, to get work done, so grant access
# to a "minimal" set of files and folders, as determined by Codex.
":minimal" = "read"

# By extending the :workspace profile, :tmpdir and :slash_tmp are "write" by
# default, though you can deny access to them altogether, if desired.
":tmpdir" = "deny"
":slash_tmp" = "deny"

### Écriture dans l’espace de travail sans accès réseau

```toml
default_permissions = "project-edit"

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"

[permissions.project-edit.network]
enabled = false

### Écriture dans l’espace de travail avec accès au Web public

```toml
default_permissions = "workspace-net"

[features]
network_proxy = true

[permissions.workspace-net.filesystem]
":minimal" = "read"

[permissions.workspace-net.filesystem.":workspace_roots"]
"." = "write"

[permissions.workspace-net.network]
enabled = true

[permissions.workspace-net.network.domains]
"*" = "allow"

N’utilisez la règle d’autorisation globale `"*"` que si vous souhaitez autoriser l’accès
au réseau public. Les règles de refus peuvent restreindre une liste d’autorisation étendue.
