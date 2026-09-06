<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/managed-configuration -->

La configuration gérée contrôle les comportements d’exécution locale pris en charge pour les fonctionnalités concernées dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE. Les exigences prises en charge peuvent varier selon le client et sa version. La configuration gérée n’accorde pas l’accès à l’espace de travail ChatGPT, n’attribue pas de licences et ne remplace pas le contrôle d’accès basé sur les rôles (RBAC) de l’espace de travail. Consultez [Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions) pour l’accès aux fonctionnalités de l’espace de travail, et cette page pour la politique d’exécution locale.

Les administrateurs d’entreprise peuvent contrôler de deux manières le comportement des clients locaux pris en charge :

- **Exigences** : contraintes imposées par les administrateurs, auxquelles les utilisateurs ne peuvent pas déroger.
- **Valeurs par défaut gérées** : valeurs initiales appliquées au lancement d’un client pris en charge. Les utilisateurs peuvent toujours modifier les paramètres pendant une exécution ; le client réapplique les valeurs par défaut gérées au démarrage suivant.

## Exigences imposées par les administrateurs (requirements.toml)

Les exigences limitent les paramètres sensibles sur le plan de la sécurité (politique d’approbation, responsable de la révision des approbations, politique de révision automatique, mode de bac à sable, profils d’autorisation, mode de recherche web, hooks gérés, serveurs MCP que les utilisateurs peuvent activer et sources de Marketplace de plugins configurées par les utilisateurs qu’ils peuvent ajouter, utiliser pour installer des plugins ou actualiser). Lors de la résolution de la configuration, par exemple à partir de `config.toml`, de [fichiers de profil](/fr-FR/codex/config-file/config-advanced#profiles) ou de surcharges de configuration de la CLI, si une valeur contrevient à une règle imposée, le client local utilise une valeur compatible et en informe l’utilisateur. Si vous configurez une liste d’autorisation `mcp_servers`, le client n’active un serveur MCP que si son nom et son identité correspondent tous deux à une entrée approuvée ; sinon, il le désactive.

Les exigences peuvent également restreindre les [indicateurs de fonctionnalité](/fr-FR/codex/config-file/config-basic/#feature-flags) via la table `[features]` de `requirements.toml`. Les fonctionnalités ne sont pas toujours sensibles sur le plan de la sécurité, mais les entreprises peuvent en figer les valeurs si elles le souhaitent. Les clés omises restent sans restriction.

À partir de Codex 0.138.0, privilégiez les [profils d’autorisation](/fr-FR/codex/permissions)
avec `allowed_permission_profiles` et le paramètre géré `default_permissions`. N’utilisez
`allowed_sandbox_modes` que pour les anciens déploiements qui configurent encore
`sandbox_mode`.

Pour consulter la liste exacte des clés, reportez-vous à la [section `requirements.toml` de la Référence de configuration](/fr-FR/codex/config-file/config-reference#requirementstoml).

### Emplacements et ordre de priorité

Chaque client local pris en charge combine les exigences par ordre de priorité croissant :

1. Fichier système `requirements.toml` (`/etc/codex/requirements.toml` sur les systèmes Unix,
   notamment Linux et macOS, ou `%ProgramData%\OpenAI\Codex\requirements.toml`
   sur Windows).
2. Exigences gérées par l’entreprise fournies dans le bundle de configuration cloud.
3. Champs hérités de `managed_config.toml` que le client local réinterprète comme des exigences.
4. Préférences gérées de macOS (MDM) transmises via
`com.openai.codex:requirements_toml_base64`.

Les couches de priorité supérieure remplacent les valeurs scalaires ordinaires et les listes des couches
inférieures. Les tables fusionnent par clé, tandis que les exigences relatives aux règles, aux hooks et
aux restrictions du système de fichiers suivent des règles de combinaison propres à chaque champ. Consultez la
[référence de `requirements.toml`](/fr-FR/codex/config-file/config-reference#requirementstoml)
pour connaître le schéma actuel, plutôt que de supposer que tous les champs fusionnent de la même
manière.

Pour assurer la rétrocompatibilité, les clients locaux pris en charge réinterprètent les champs hérités
`approval_policy`, `approvals_reviewer` et `sandbox_mode` comme des
exigences. Cette conversion ajoute si nécessaire des options de compatibilité ; utilisez
`requirements.toml` pour définir des listes d’autorisation explicites.

### Exigences gérées dans le cloud

Lorsqu’un utilisateur se connecte avec ChatGPT dans le cadre d’une offre prise en charge, les clients locaux pris en charge
peuvent recevoir des exigences imposées par les administrateurs et associées à l’espace de travail. Il s’agit
d’un canal de distribution pour une politique compatible avec `requirements.toml`. Ce canal n’accorde pas
l’accès à l’espace de travail et ne remplace pas son contrôle d’accès basé sur les rôles (RBAC).

Ouvrez [Configuration gérée](https://chatgpt.com/codex/settings/managed-configs)
pour créer et attribuer des exigences gérées dans le cloud. Par exemple, cette politique limite
les choix d’approbation et de bac à sable, et demande une confirmation avant l’exécution d’un point d’entrée shell
pris en charge :

```toml
allowed_approval_policies = ["on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[rules]
prefix_rules = [
  { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entry points" },
]

Vérifiez que chaque version de client géré prend en charge les clés sélectionnées et
testez la politique auprès d’un petit groupe avant de l’attribuer à toute l’organisation. Consultez
la référence de configuration pour obtenir le schéma actuel et l’interface
d’administration pour connaître les modalités actuelles d’attribution.

Le service sélectionne les couches d’exigences gérées par l’entreprise qui s’appliquent à
l’identité de l’utilisateur connecté. Le client local évalue ces couches avec les autres
sources d’exigences décrites dans [Emplacements et ordre de priorité](#locations-and-precedence).
Utilisez l’interface d’administration actuelle pour créer et
attribuer les exigences côté espace de travail. Ne vous fiez pas à une copie de l’algorithme de mise en correspondance des groupes ; le service
d’administration gère ce comportement et peut le modifier indépendamment du format des
exigences locales.

Pour connaître les clés prises en charge et consulter des exemples, reportez-vous à
[Exemple de requirements.toml](#example-requirementstoml) et à la
[référence de `requirements.toml`](/fr-FR/codex/config-file/config-reference#requirementstoml).

#### Comment les clients locaux appliquent les exigences gérées dans le cloud

Lorsqu’un utilisateur lance un client local pris en charge et se connecte avec ChatGPT dans le cadre d’une
offre prise en charge, le client recherche d’abord une entrée de cache valide correspondant à son identité.
Si aucune entrée valide n’est disponible, le client récupère le bundle applicable, avec de nouvelles tentatives
si nécessaire, et écrit une entrée de cache signée en cas de réussite. Si la requête échoue ou
expire et qu’aucun cache valide n’est disponible, le chargement du bundle de configuration cloud renvoie
une erreur au lieu de démarrer silencieusement sans la couche d’exigences gérées dans le
cloud.

Après la résolution du cache, le client combine les exigences gérées dans le cloud avec les
autres couches d’exigences décrites ci-dessus. Une actualisation en arrière-plan peut mettre à jour le
cache pour un démarrage ultérieur ; elle ne remplace pas les exigences déjà chargées
dans le processus en cours.

### Vérifiez l’expérience des administrateurs et des collaborateurs

Désignez une personne responsable de chaque politique gérée, consignez les utilisateurs ou groupes
auxquels elle doit s’appliquer et documentez la justification métier de toute restriction liée au système de fichiers,
au réseau, aux approbations ou aux profils d’autorisation.

Avant d’étendre le déploiement, testez auprès d’un utilisateur représentatif un workflow approuvé et un workflow
volontairement interdit. Vérifiez les paramètres effectivement appliqués dans le client pris en charge,
sans supposer qu’un rôle ou un groupe de l’espace de travail suffit à imposer
la restriction locale.

### Exemple de requirements.toml

Cet exemple bloque `--ask-for-approval never` et `--sandbox danger-full-access` (y compris `--yolo`) :

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

### Désactivez les captures d’application

Pour désactiver les captures d’application pour les utilisateurs gérés, définissez l’exigence `allow_appshots` de premier niveau :

```toml
allow_appshots = false

Lorsque les captures d’application sont disponibles, `allow_appshots = false` les désactive. Si vous
omettez la clé, les exigences n’imposent aucune restriction aux captures d’application et les vérifications habituelles de
disponibilité du produit s’appliquent. Les clients App Server qui lisent les exigences effectives
via `configRequirements/read` reçoivent la même restriction sous la forme de
`allowAppshots` ; une valeur omise ou égale à `null` pour `allowAppshots` ne désactive pas
les captures d’application.

### Désactivez le contrôle à distance de l’appareil

Pour désactiver le [contrôle à distance de l’appareil](/fr-FR/codex/remote-connections#pick-up-work-from-another-device)
pour les utilisateurs gérés, définissez l’exigence `allow_remote_control` de premier niveau :

```toml
allow_remote_control = false

Lorsque le contrôle à distance de l’appareil est pris en charge, `allow_remote_control = false`
le désactive. Si vous omettez la clé, les exigences n’imposent aucune restriction au contrôle à distance
de l’appareil et les vérifications habituelles de disponibilité du produit s’appliquent. Cette exigence ne
désactive pas les connexions SSH distantes.

### Contrôlez les profils d’autorisation disponibles

Utilisez `allowed_permission_profiles` pour contrôler les
[profils d’autorisation](/fr-FR/codex/permissions) intégrés et personnalisés que les utilisateurs peuvent sélectionner. Il s’agit de
l’équivalent de `allowed_sandbox_modes` pour les profils d’autorisation ; utilisez la liste d’autorisation qui
correspond à la manière dont vos utilisateurs sélectionnent leurs autorisations.

Les listes d’autorisation de profils nécessitent Codex 0.138.0 ou une version ultérieure. Codex 0.137.0 et
les versions antérieures ignorent `allowed_permission_profiles` ainsi que le paramètre géré
`default_permissions`.

N’utilisez les exemples de profils d’autorisation ci-dessous que lorsque tous les clients gérés exécutent une
version compatible. Ne déployez pas de profils personnalisés gérés tant que la mise à niveau du parc
n’est pas terminée.

Lorsqu’elle est présente, la table constitue la liste complète des profils autorisés. Elle autorise
les profils définis sur `true` et refuse ceux qui sont omis ou définis sur `false`, y compris
les profils intégrés ajoutés dans de futures versions de Codex.

#### Autorisez les profils standard

Cette politique autorise l’accès en lecture seule et l’accès à l’espace de travail, mais pas l’accès complet :

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

#### Ajoutez un profil par défaut géré respectant le principe du moindre privilège

Les administrateurs peuvent définir un profil personnalisé dans la même source d’exigences. Utilisez
des noms de profils propres à l’organisation qui ne risquent pas d’entrer en conflit avec ceux de la configuration
chargée pour les utilisateurs. Les noms personnalisés ne peuvent pas commencer par `:`
ni utiliser le nom réservé `filesystem`.

Ne déployez pas de profils personnalisés gérés sur des clients exécutant Codex 0.137.0 ou une
version antérieure. Ces clients reconnaissent la table des profils, mais pas la valeur par défaut gérée
qui sélectionne le profil.

Par exemple :

```toml
default_permissions = "acme_review_only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
acme_review_only = true
# ":danger-full-access" is intentionally omitted, so it is denied.

[permissions.acme_review_only]
description = "Review code without modifying the workspace."
extends = ":read-only"

#### Autorisez uniquement les profils définis par l’entreprise

Omettez tous les profils intégrés lorsque les utilisateurs ne doivent pouvoir sélectionner que ceux définis par les administrateurs :

```toml
default_permissions = "acme_workspace"

[allowed_permission_profiles]
acme_workspace = true

[permissions.acme_workspace]
description = "Workspace access with sensitive files denied."
extends = ":workspace"

[permissions.acme_workspace.filesystem]
glob_scan_max_depth = 3

[permissions.acme_workspace.filesystem.":workspace_roots"]
"**/*.env" = "deny"

Le profil personnalisé peut étendre `:workspace`, même si les utilisateurs ne peuvent pas sélectionner directement le
profil intégré `:workspace`.

#### Désactivez un profil autorisé par une autre source

Les listes d’autorisation se combinent par nom de profil. Comme les exigences gérées dans le cloud sont
prioritaires sur les exigences système, elles peuvent utiliser `false`
pour désactiver un profil autorisé par le fichier système.

Exigences gérées dans le cloud :

```toml
default_permissions = ":read-only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = false

Exigences système :

```toml
[allowed_permission_profiles]
":read-only" = true
":workspace" = true  # Not honored because cloud requirements set this to false.

Définissez explicitement `default_permissions` avec le nom d’un profil autorisé. Si ce paramètre est omis,
l’environnement d’exécution local adopte `:workspace` par défaut uniquement si `:workspace` et
`:read-only` sont tous deux explicitement autorisés. En l’absence de `allowed_permission_profiles`,
les exigences gérées ne limitent pas les noms de profils que les utilisateurs peuvent
sélectionner. Chaque entrée doit désigner un profil intégré ou un profil personnalisé défini dans
une source de configuration ou d’exigences chargée. Définissez les profils personnalisés dans les
exigences gérées afin de contrôler leur comportement de façon centralisée.

### Redéfinissez les exigences de bac à sable selon l’hôte

Utilisez `[[remote_sandbox_config]]` lorsqu’une même politique gérée doit appliquer des exigences de
bac à sable différentes selon les hôtes. Par exemple, vous pouvez conserver une configuration par défaut plus
stricte pour les ordinateurs portables, tout en autorisant l’écriture dans l’espace de travail sur les machines de développement ou les
runners CI correspondants. Actuellement, les entrées propres à un hôte ne redéfinissent que `allowed_sandbox_modes` :

```toml
allowed_sandbox_modes = ["read-only"]

[[remote_sandbox_config]]
hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

L’environnement d’exécution local compare chaque entrée `hostname_patterns` au
nom d’hôte qu’il parvient à résoudre. Il privilégie le nom de domaine complet lorsqu’il est
disponible et utilise à défaut le nom d’hôte local. La correspondance ne tient pas compte de la casse ;
`*` correspond à n’importe quelle suite de caractères, et `?` à un seul caractère.

La première entrée `[[remote_sandbox_config]]` correspondante l’emporte au sein d’une même
source d’exigences. Si aucune entrée ne correspond, l’environnement d’exécution local conserve la valeur
`allowed_sandbox_modes` de premier niveau. La correspondance du nom d’hôte sert uniquement à sélectionner la politique ; ne la
considérez pas comme une preuve authentifiée de l’identité de l’appareil.

Vous pouvez également restreindre le mode de recherche web :

```toml
allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed

`allowed_web_search_modes = []` n’autorise que `"disabled"`.
Par exemple, `allowed_web_search_modes = ["cached"]` empêche la recherche web en direct, même dans les sessions `danger-full-access`.

### Configurez les exigences d’accès réseau

  `[experimental_network]` est expérimental et susceptible d’évoluer. N’activez pas ces
  exigences à grande échelle dans un déploiement d’entreprise sans les avoir validées
  sur les versions des clients locaux et les systèmes d’exploitation de vos utilisateurs. La prise en charge de Windows
  reste limitée ; évitez d’appliquer cette stratégie aux utilisateurs de Windows tant que
  vous ne l’avez pas testée dans votre environnement.

Utilisez `[experimental_network]` dans `requirements.toml` lorsque les administrateurs doivent
définir les exigences d’accès réseau de manière centralisée. Ces exigences sont distinctes
du paramètre utilisateur `features.network_proxy` : elles permettent de configurer le réseau du bac à sable
sans cet indicateur de fonctionnalité, mais n’accordent pas d’accès réseau aux commandes
lorsque le bac à sable actif désactive le réseau. Définissez
`experimental_network.enabled = true` pour activer le proxy géré ; les règles de domaine
ne suffisent pas à elles seules à activer le proxy.

```toml
[experimental_network]
enabled = true
managed_allowed_domains_only = true

[experimental_network.domains]
"api.openai.com" = "allow"
"**.example.com" = "allow"
"blocked.example.com" = "deny"
"**.exfil.example.com" = "deny"

Utilisez `experimental_network.managed_allowed_domains_only = true` uniquement si vous
définissez également des entrées `"allow"` contrôlées par les administrateurs dans
`[experimental_network.domains]` et souhaitez que ces règles soient exclusives. Si ce paramètre vaut
`true` sans règles d’autorisation gérées, les règles d’autorisation de domaines ajoutées par les utilisateurs cessent
de s’appliquer. Ne combinez pas la table de correspondance canonique `domains` avec les anciennes listes
`allowed_domains` ou `denied_domains`.

`*.example.com` correspond uniquement aux sous-domaines. `**.example.com` correspond au domaine racine
et à ses sous-domaines. Une règle de refus correspondante l’emporte sur une règle d’autorisation.

La syntaxe des domaines, les règles relatives aux destinations locales ou privées, la priorité des refus sur les autorisations
et les limites liées au rebinding DNS sont les mêmes que pour le fonctionnement réseau du bac à sable
décrit dans [Autorisations de l’agent et sécurité](/fr-FR/codex/agent-approvals-security#network-isolation).

Le proxy achemine le trafic des commandes locales exécutées dans le bac à sable. Les outils de navigation
vérifient également les interdictions réseau gérées et les listes d’autorisation exclusives avant d’accéder
à une origine ; il s’agit d’une vérification distincte de la stratégie, et non d’un acheminement du trafic du navigateur via
le proxy des commandes. Celui-ci ne filtre pas la recherche web, les applications et connecteurs, les serveurs MCP,
le trafic des applications natives, les requêtes adressées au service Codex ni le trafic de Codex Cloud.
Utilisez les contrôles propres à chaque fonctionnalité :

- Utilisez `allowed_web_search_modes` pour restreindre la recherche web.
- Utilisez `features.apps = false` pour désactiver les intégrations d’applications et de connecteurs, et
`features.plugins = false` pour désactiver les plugins lorsqu’ils sont pris en charge.
- Utilisez la liste gérée `mcp_servers` des serveurs approuvés pour restreindre les serveurs MCP.
- Utilisez des exigences relatives aux fonctionnalités, telles que `browser_use`, `in_app_browser` et
`computer_use`, pour limiter les capacités liées au navigateur et à l’utilisation de l’ordinateur.
- Configurez l’accès réseau de Codex Cloud dans les paramètres de son environnement cloud.

Une liste des domaines autorisés pour les commandes ne remplace pas ces contrôles
propres à chaque fonctionnalité.

### Contrôlez le navigateur et l’Utilisation de l’ordinateur

Utilisez les tables `[browser_use]` et `[computer_use]` dans `requirements.toml` pour
restreindre les clients de bureau pris en charge. Validez la stratégie sur les versions des clients
et les systèmes d’exploitation de votre déploiement. Une règle d’autorisation configurée
n’installe aucun plugin, n’accorde aucune autorisation du système d’exploitation et n’approuve aucune action
qui nécessite encore une révision.

Pour l’accès au navigateur, configurez une stratégie d’origine. Une origine comprend le schéma,
l’hôte et un port facultatif, par exemple `https://example.com` ou
`https://*.example.com:8443`. N’incluez ni chemin, ni chaîne de requête, ni fragment. Contrairement
aux règles de domaine pour le réseau des commandes, les règles d’origine du navigateur distinguent HTTP de HTTPS
et tiennent compte du port.

Cet exemple limite l’accès du navigateur à un site approuvé et y interdit les envois de fichiers
ainsi que l’accès complet au protocole Chrome DevTools Protocol (CDP) :

```toml
[browser_use]
allow_history_access = false
allow_global_persistent_approval = false

[browser_use.default_origin_policy]
access = "deny"

[browser_use.origins."https://example.com"]
access = "allow"
uploads = "deny"
downloads = "allow"
full_cdp_access = "deny"
persistent_approval = false
access_approval_lifetime = "turn"

Les règles d’origine correspondantes sont évaluées champ par champ. Un refus correspondant l’emporte ; sinon,
la stratégie d’origine par défaut fournit les valeurs des champs que les règles correspondantes ne précisent pas.
La configuration locale peut ajouter des restrictions, mais ne peut pas assouplir un refus géré.
Les interdictions réseau et les listes d’autorisation réseau gérées exclusives continuent de s’appliquer.

Définissez `browser_use.disable_auto_review = true` pour désactiver la révision automatique des demandes d’approbation
pour les actions du navigateur, ou définissez `auto_review = "deny"` dans une stratégie d’origine
pour la désactiver pour cette origine. Ce paramètre contrôle la gestion des approbations ; il ne
désactive pas la surveillance de sécurité du modèle.

Pour les applications natives, définissez une stratégie d’accès par défaut et identifiez les applications autorisées. Par
exemple, cette stratégie macOS autorise Calculator et empêche l’enregistrement des approbations :

```toml
[computer_use]
default_app_access = "deny"
allow_persistent_approval = false

[computer_use.macos.bundle_ids]
"com.apple.calculator" = "allow"

Les stratégies Windows peuvent identifier les applications empaquetées à l’aide de
`computer_use.windows.aumids` ou les exécutables à l’aide de
`computer_use.windows.exes`. Les règles relatives aux exécutables exigent `publisher_name`,
`product_name` et `access` ; `binary_name` est facultatif. Utilisez l’identité vérifiée
de l’application plutôt que son seul nom d’affichage.

Consultez la [référence de configuration](/fr-FR/codex/config-file/config-reference#requirementstoml)
pour connaître tous les champs, ainsi que les [restrictions d’utilisation après verrouillage](#restrict-locked-computer-use)
pour les appareils macOS gérés.

### Fixez les indicateurs de fonctionnalités

Vous pouvez également fixer les [indicateurs de fonctionnalités](/fr-FR/codex/config-file/config-basic/#feature-flags) pour les utilisateurs
qui reçoivent un fichier `requirements.toml` géré :

```toml
[features]
personality = true
unified_exec = false

# Disable surface-specific features when needed.
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
in_app_updates = false
computer_use = false

Utilisez les clés de fonctionnalité canoniques de la table `[features]` de `config.toml` pour les
fonctionnalités d’exécution. L’environnement d’exécution local normalise les fonctionnalités reconnues pour respecter ces
valeurs imposées et refuse toute écriture incompatible dans `config.toml` ou dans les paramètres
de fonctionnalités des fichiers de profil.

<a id="disable-codex-feature-surfaces"></a>

- `in_app_browser = false` désactive le volet du navigateur intégré.
- `in_app_updates = false` désactive le programme de mise à jour propre à l’application de bureau ChatGPT au
  redémarrage, lorsque cette fonctionnalité est prise en charge. Cela n’affecte pas le déploiement externe de paquets et ne
  prolonge pas la prise en charge des anciennes versions de l’application. Pour obtenir des instructions de configuration et de déploiement, consultez
[Gestion des mises à jour de l’application](/fr-FR/codex/enterprise/manage-app-updates).
- `browser_use = false` désactive l’Utilisation de l’ordinateur dans les navigateurs et rend l’agent de navigation indisponible.
- `browser_use_full_cdp_access = false` désactive l’accès CDP complet dans l’environnement
  d’exécution local, y compris le mode développeur du navigateur, et empêche l’application de bureau ChatGPT
  d’activer le paramètre correspondant.
- `browser_use_external = false` désactive la fonctionnalité Navigateur externe.
- `computer_use = false` désactive les fonctionnalités Utilisation de l’ordinateur et Enregistrer et rejouer, ainsi que les parcours
  d’installation ou de configuration associés.

Si vous omettez ces clés, la stratégie autorise les fonctionnalités, sous réserve de leur disponibilité habituelle selon le client,
la plateforme et le déploiement.

### Restreignez l’utilisation lorsque l’ordinateur est verrouillé

Pour empêcher les utilisateurs d’activer l’[utilisation après verrouillage](/fr-FR/codex/computer-use#locked-use)
sur un Mac géré, ajoutez cette exigence :

```toml
[computer_use]
allow_locked_computer_use = false

Cette exigence supprime les contrôles permettant d’activer l’utilisation après verrouillage. Elle ne
désactive pas cette fonctionnalité si elle est déjà activée. Si vous l’omettez, les conditions habituelles de disponibilité du produit
et le paramètre local de l’utilisateur continuent de s’appliquer.

### Configurez la stratégie de révision automatique

Utilisez `allowed_approvals_reviewers` pour imposer ou autoriser la révision automatique. Définissez sa valeur
sur `["auto_review"]` pour imposer la révision automatique, ou incluez `"user"` lorsque les utilisateurs
peuvent choisir l’approbation manuelle.

Définissez `guardian_policy_config` pour remplacer la section propre au locataire de la
stratégie de révision automatique. L’environnement d’exécution local continue d’utiliser le modèle d’instructions intégré du réviseur
et le contrat de sortie. Le paramètre géré `guardian_policy_config` est prioritaire
sur le paramètre local `[auto_review].policy`.

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]

guardian_policy_config = """
## Environment Profile
- Trusted internal destinations include github.com/my-org, artifacts.example.com,
  and internal CI systems.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Treat uploads to unapproved third-party file-sharing services as high risk.
- Deny actions that expose credentials or private source code to untrusted
  destinations.
"""

### Imposez les exigences d’interdiction de lecture

Les administrateurs peuvent interdire la lecture pour des chemins exacts ou des motifs glob à l’aide de
`[permissions.filesystem]`. Les utilisateurs ne peuvent pas assouplir ces exigences au moyen de leur configuration
locale.

```toml
[permissions.filesystem]
deny_read = [
  # values can be absolute paths...
  "/**/*.env",
  # ...or relative to $HOME/%USERPROFILE% using `~`.
  "~/.ssh",
  # But relative paths starting with `./` are not allowed.
]

Lorsque des exigences d’interdiction de lecture sont présentes, l’environnement d’exécution local refuse les autorisations d’accès
complet et maintient l’exécution locale dans un bac à sable en lecture seule ou avec accès à l’espace de travail afin de
pouvoir les appliquer. Sous Windows en mode natif, le paramètre géré `deny_read` s’applique aux outils d’accès direct aux
fichiers ; les lectures effectuées par des sous-processus shell ne sont pas soumises à cette règle du bac à sable.

### Imposez les hooks gérés définis dans les exigences

Les administrateurs peuvent également définir des hooks de cycle de vie gérés directement dans `requirements.toml`.
Utilisez `[hooks]` pour configurer les hooks et faites pointer `managed_dir` vers le
répertoire dans lequel vos outils MDM ou de gestion des terminaux installent les scripts
référencés.

Pour imposer les hooks gérés même aux utilisateurs qui les ont désactivés localement, fixez
`[features].hooks = true` en complément de `[hooks]`. Pour ignorer les hooks de l’utilisateur, du projet, de la session
et des plugins tout en autorisant les hooks gérés, définissez
`allow_managed_hooks_only = true`.

```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"

Remarques :

- L’environnement d’exécution local applique la configuration des hooks définie dans `requirements.toml`,
  mais ne distribue pas les scripts contenus dans `managed_dir`.
- Déployez ces scripts avec votre solution MDM ou de gestion des appareils.
- Les commandes des hooks gérés doivent référencer des chemins absolus vers des scripts situés dans le
répertoire géré configuré.
- `allow_managed_hooks_only = true` ignore les hooks provenant de l’utilisateur, du projet, de la session et des
  plugins, mais continue de charger ceux de `requirements.toml` et des autres
  couches de configuration gérée.

### Imposez les règles de commande définies dans les exigences

Les administrateurs peuvent également imposer des règles de commande restrictives définies dans `requirements.toml`
à l’aide d’une table `[rules]`. Ces règles sont fusionnées avec celles des fichiers `.rules` ordinaires, et la
décision la plus restrictive l’emporte toujours.

Contrairement aux fichiers `.rules`, les règles définies dans les exigences doivent spécifier `decision`. Cette décision
doit être `"prompt"` ou `"forbidden"` (et non `"allow"`).

```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
]

Pour limiter les serveurs MCP qu’un client local peut activer, ajoutez une liste `mcp_servers`
de serveurs approuvés. Pour les serveurs stdio, utilisez `command` comme critère de correspondance ; pour les serveurs HTTP
avec diffusion en continu, utilisez `url` :

```toml
[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }

La forme textuelle de `identity.command` ne compare que la valeur `command` configurée. Elle
n’examine pas `args`, `cwd`, `env` ni `env_vars`.

Pour contraindre une invocation stdio complète, faites correspondre l’exécutable et chacun des
arguments positionnels :

```toml
[mcp_servers.internal.identity]
command = { executable = "/usr/local/bin/codex-mcp", args = [
  { match = "exact", value = "serve" },
  { match = "prefix", value = "--workspace=" },
] }

L’exécutable, le nombre d’arguments et leur ordre doivent correspondre. Les règles relatives aux arguments et aux URL
prennent en charge les correspondances `exact` et `prefix`, ainsi que les correspondances `regex` portant sur l’intégralité de la valeur. Les règles
structurées relatives aux commandes n’examinent toujours pas `cwd`, `env` ni `env_vars`. Les serveurs MCP intégrés aux
plugins utilisent les mêmes structures d’identité sous
`plugins.<plugin>.mcp_servers.<server>`.

Si `mcp_servers` est présent mais vide, le client local désactive tous les serveurs MCP.

### Contrôlez la disponibilité des plugins

Pour désactiver les plugins dans les clients locaux pris en charge, définissez `features.plugins` sur
`false` dans `requirements.toml` :

```toml
features.plugins = false

Ce paramètre s’applique également lorsque les utilisateurs se connectent à Codex avec une clé API. Consultez
[la référence de
`features.plugins`](/fr-FR/codex/config-file/config-reference#requirementstoml) pour connaître la
configuration prise en charge.

### Restreignez les sources de la Marketplace des plugins

Pour restreindre les opérations sur les sources de Marketplace configurées par les utilisateurs, définissez
`restrict_to_allowed_sources = true` et configurez une ou plusieurs règles de source :

```toml
[marketplaces]
restrict_to_allowed_sources = true

[marketplaces.allowed_sources.company_plugins]
source = "git"
url = "https://github.com/example/company-plugins.git"
ref = "main"

[marketplaces.allowed_sources.internal_git]
source = "host_pattern"
host_pattern = '^git\.example\.com$'

[marketplaces.allowed_sources.local_plugins]
source = "local"
path = "/opt/company/codex-plugins"

Les règles Git correspondent à l’URL normalisée du dépôt et, le cas échéant, à la valeur exacte de
`ref`. Les motifs d’hôte sont des expressions régulières comparées au nom d’hôte Git
en minuscules ; utilisez `^` et `$` pour faire correspondre l’intégralité du nom d’hôte. Les règles locales exigent un chemin absolu
et normalisé. Consultez la [référence de `requirements.toml`](/fr-FR/codex/config-file/config-reference#requirementstoml)
pour connaître le schéma complet et le comportement de fusion.

Ces exigences bloquent, pour les sources configurées par les utilisateurs, les opérations d’ajout de Marketplaces,
d’installation de plugins et d’actualisation de Marketplaces Git configurées lorsqu’elles ne correspondent à aucune règle.
Les Marketplaces OpenAI gérées par Codex restent disponibles lorsque leur source et leur nom réservé
correspondent aux valeurs attendues. Ces exigences ne filtrent pas les Marketplaces utilisateur déjà configurées ni leurs plugins
lors de l’exécution.

Ces restrictions sur les sources s’appliquent uniquement aux clients locaux qui prennent en charge les opérations sur les marketplaces de plugins : ChatGPT et Codex dans l’application de bureau, ainsi que Codex CLI.
Elles ne régissent pas l’utilisation des plugins dans ChatGPT sur le web ou sur mobile et n’ajoutent pas de plugins à l’extension IDE.

## Valeurs par défaut gérées (`managed_config.toml`)

Les valeurs par défaut gérées définissent la configuration initiale d’un client local pris en charge. Au
démarrage, elles priment sur le fichier `config.toml` local de l’utilisateur et sur toute surcharge `--config`
de la CLI. Les utilisateurs peuvent toujours modifier ces paramètres pendant l’exécution en cours, et les
valeurs par défaut s’appliquent de nouveau au prochain démarrage du client.

Si une valeur par défaut gérée, un profil MDM macOS ou une configuration enregistrée fixe le modèle à `gpt-5.4`
ou `gpt-5.4-mini` pour les utilisateurs connectés avec ChatGPT, mettez cette configuration à jour avant le 31 août 2026. Remplacez `gpt-5.4` par `gpt-5.6-terra` et `gpt-5.4-mini` par
`gpt-5.6-luna`. L’API OpenAI et Codex authentifié avec votre propre clé API
ne sont pas concernés. Consultez la [disponibilité des modèles
dans l’espace de travail](/fr-FR/codex/enterprise/workspace-model-availability#prepare-for-the-gpt-54-retirement).

Vérifiez que vos valeurs par défaut gérées respectent vos exigences ; l’environnement d’exécution local
rejette les valeurs non autorisées.

### Priorité et superposition des couches

L’environnement d’exécution local compose la configuration effective selon l’ordre suivant (les couches du haut
priment sur celles du bas) :

- Préférences gérées (MDM macOS ; priorité la plus élevée)
- `managed_config.toml` (fichier système/géré)
- `config.toml` (configuration de base de l’utilisateur)

Les surcharges `--config key=value` de la CLI s’appliquent à la configuration de base, mais les couches gérées sont prioritaires. Chaque exécution démarre donc avec les valeurs par défaut gérées, même si vous fournissez des options locales.

Les exigences gérées dans le cloud s’appliquent à la couche des exigences, et non aux valeurs par défaut gérées. Pour connaître leur ordre de priorité, consultez la section « Exigences imposées par les administrateurs » ci-dessus.

### Emplacements

- Linux/macOS (Unix) : `/etc/codex/managed_config.toml`
- Windows/non-Unix : `~/.codex/managed_config.toml`

Si le fichier est absent, l’environnement d’exécution local ignore la couche gérée.

### Préférences gérées de macOS (MDM)

Sur macOS, les administrateurs peuvent déployer un profil d’appareil contenant des charges utiles TOML encodées en base64 aux emplacements suivants :

- Domaine de préférences : `com.openai.codex`
- Clés :
  - `config_toml_base64` (valeurs par défaut gérées)
  - `requirements_toml_base64` (exigences)

L’environnement d’exécution local analyse ces charges utiles de « préférences gérées » au format TOML. Pour
les valeurs par défaut gérées (`config_toml_base64`), les préférences gérées ont la priorité
la plus élevée. Pour les exigences (`requirements_toml_base64`), l’ordre de priorité suit
celui des exigences gérées dans le cloud décrit ci-dessus. La même
table `[features]` dédiée aux exigences fonctionne dans `requirements_toml_base64` ; utilisez-y
également les clés canoniques des fonctionnalités.

### Workflow de configuration MDM

L’environnement d’exécution local prend en charge les charges utiles MDM standard de macOS. Vous pouvez ainsi distribuer
les paramètres à l’aide d’outils tels que `Jamf Pro`, `Fleet` ou `Kandji`. Un déploiement
simple se déroule comme suit :

1. Créez la charge utile TOML gérée, puis encodez-la avec `base64` (sans retour à la ligne).
2. Insérez la chaîne dans votre profil MDM, sous le domaine `com.openai.codex`, à la clé `config_toml_base64` (valeurs par défaut gérées) ou `requirements_toml_base64` (exigences).
3. Déployez le profil, puis demandez aux utilisateurs de redémarrer le client local pris en charge et
de vérifier que le résumé de la configuration au démarrage reflète les valeurs gérées.
4. Lorsque vous révoquez ou modifiez une politique, mettez à jour la charge utile gérée ; le client
lira la préférence actualisée à son prochain lancement.

Évitez d’intégrer des secrets ou des valeurs dynamiques fréquemment modifiées dans la charge utile. Traitez le TOML géré comme tout autre paramètre MDM soumis au contrôle des modifications.

### Exemple de managed\_config.toml

```toml
# Set conservative defaults
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false             # keep network disabled unless explicitly allowed

[otel]
environment = "prod"
exporter = "otlp-http"            # point at your collector
log_user_prompt = false            # keep prompts redacted
# exporter details live under exporter tables; see Monitoring and telemetry above

### Mesures de protection recommandées

- Pour la plupart des utilisateurs, privilégiez `workspace-write` avec des approbations ; réservez l’accès complet aux conteneurs contrôlés.
- Conservez `network_access = false`, sauf si votre révision de sécurité autorise un collecteur ou des domaines nécessaires à vos workflows.
- Utilisez la configuration gérée pour fixer les paramètres OTel (exportateur, environnement), mais conservez `log_user_prompt = false`, sauf si votre politique autorise explicitement le stockage du contenu des prompts.
- Contrôlez régulièrement les différences entre le fichier `config.toml` local et la politique gérée afin de détecter toute dérive ; les couches gérées doivent avoir la priorité sur les options et fichiers locaux.
