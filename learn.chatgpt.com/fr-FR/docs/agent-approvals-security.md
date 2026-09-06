<!-- source: https://learn.chatgpt.com/fr-FR/docs/agent-approvals-security -->

Codex contribue à protéger votre code et vos données et réduit le risque d’utilisation abusive.

  Cette page explique comment utiliser Codex en toute sécurité, notamment en ce qui concerne le bac à sable, les approbations
  et l’accès au réseau. Si vous recherchez Codex Security, le produit qui permet
  d’analyser les dépôts GitHub connectés, consultez [Codex Security](/fr-FR/codex/security).

Par défaut, l’agent s’exécute sans accès au réseau. En local, Codex utilise un bac à sable imposé par le système d’exploitation, qui limite ses accès, généralement à l’espace de travail actuel. Une politique d’approbation détermine également quand il doit s’arrêter et vous demander votre accord avant d’agir.

Pour une présentation générale du fonctionnement du bac à sable dans l’application de bureau ChatGPT,
Codex CLI et l’extension IDE, consultez la page [Bac à sable](/fr-FR/codex/sandboxing).
Pour une vue d’ensemble plus large de la sécurité en entreprise, consultez le [livre blanc sur la sécurité de Codex](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).

## Bac à sable et approbations

Les contrôles de sécurité de Codex reposent sur deux couches complémentaires :

- **Mode bac à sable** : ce que Codex peut techniquement faire lorsqu’il exécute des commandes générées par le modèle, notamment où il peut écrire et s’il peut accéder au réseau.
- **Politique d’approbation** : les situations dans lesquelles Codex doit demander votre approbation avant d’exécuter une action, comme quitter le bac à sable, utiliser le réseau ou exécuter des commandes qui ne figurent pas dans un ensemble de confiance.

Codex utilise différents modes de bac à sable selon l’environnement dans lequel vous l’exécutez :

- **Codex Cloud** : s’exécute dans des conteneurs isolés gérés par OpenAI, ce qui empêche l’accès à votre système hôte ou à des données sans rapport avec la tâche. Son modèle d’exécution comporte deux phases : la phase de configuration précède celle de l’agent et peut accéder au réseau pour installer les dépendances indiquées ; ensuite, la phase de l’agent s’exécute hors ligne par défaut, sauf si vous activez l’accès Internet pour cet environnement. Les secrets configurés pour les environnements cloud sont accessibles uniquement pendant la configuration et sont supprimés avant le début de la phase de l’agent.
- **Codex CLI / extension IDE** : des mécanismes du système d’exploitation appliquent les politiques du bac à sable. Par défaut, l’accès au réseau est désactivé et les autorisations d’écriture sont limitées à l’espace de travail actif. Vous pouvez configurer le bac à sable, la politique d’approbation et les paramètres réseau selon votre tolérance au risque.

Avec le préréglage `Auto` (par exemple, `--sandbox workspace-write --ask-for-approval on-request`), Codex peut automatiquement lire des fichiers, les modifier et exécuter des commandes dans le répertoire de travail.

Codex demande votre approbation pour modifier des fichiers hors de l’espace de travail ou exécuter des commandes nécessitant un accès au réseau. Si vous souhaitez discuter ou planifier sans apporter de modifications, passez au mode `read-only` avec la commande `/permissions`.

Codex peut également solliciter une approbation pour les appels d’outils d’application (connecteur) qui déclarent des effets de bord, même si l’action n’est ni une commande shell ni une modification de fichier. Les appels destructifs aux outils d’application ou MCP nécessitent toujours une approbation lorsque l’outil déclare une annotation destructive, sauf s’il déclare une annotation de lecture, qui est prioritaire.

## Surveillance de la sécurité et tâches en pause

GPT-6 Astra intègre une surveillance de la sécurité dans Codex et ChatGPT Work. Cette surveillance
s’exécute de manière asynchrone et peut mettre une tâche en pause si elle détecte un comportement potentiellement dangereux du modèle.
La mise en pause peut intervenir après l’activité qui l’a déclenchée ; la surveillance
ne remplace ni le bac à sable, ni les autorisations, ni la révision du résultat.

Si une tâche se met en pause, lisez le message et examinez les constats lorsqu’ils sont disponibles. Reprenez
uniquement après avoir vérifié que la tâche peut se poursuivre en toute sécurité. Si le message indique que
la tâche est terminée ou ne propose pas de reprise, vous ne pouvez pas la reprendre depuis cette
interface.

| Interface et contrôles des données                                                                               | Constats et reprise                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Clients Codex et ChatGPT Work proposant la consultation des constats et la reprise, sans les contrôles des données indiqués ici | Examinez les constats avant de reprendre.                      |
| Codex CLI et Codex mobile                                                                                    | Les constats complets et la reprise ne sont pas disponibles. La tâche se termine. |
| Politique de non-conservation des données, surveillance modifiée des abus ou résidence des données stockées hors des États-Unis                        | Les constats complets et la reprise ne sont pas disponibles. La tâche se termine. |

La surveillance de la sécurité évalue le comportement du modèle pendant une tâche.
La [révision automatique des demandes d’approbation](/fr-FR/codex/sandboxing/auto-review) évalue chaque action qui
nécessite déjà une approbation, avant son exécution. Une action approuvée par
la révision automatique peut tout de même faire partie d’une tâche que la surveillance met ensuite en pause.

## Accès au réseau 

Pour Codex Cloud, consultez la page sur [l’accès Internet de l’agent](/fr-FR/codex/cloud/internet-access) afin d’activer un accès Internet complet ou une liste de domaines autorisés.

Pour l’application de bureau ChatGPT, Codex CLI ou l’extension IDE, le mode de bac à sable `workspace-write` par défaut maintient l’accès au réseau désactivé, sauf si vous l’activez dans votre configuration :

```toml
[sandbox_workspace_write]
network_access = true

### Isolement réseau

L’accès au réseau est contrôlé par des règles de destination qui s’appliquent aux scripts,
aux programmes et aux sous-processus lancés par les commandes. Lorsque l’accès au réseau des commandes est
déjà activé, activez la fonctionnalité `network_proxy` pour soumettre ce trafic
à la politique réseau que vous configurez. L’ajout de règles de domaine ne suffit pas à activer
le proxy.

```toml
[features.network_proxy]
enabled = true
domains = { "api.openai.com" = "allow", "example.com" = "deny" }

Pour une session CLI ponctuelle, utilisez la forme booléenne abrégée si vous devez simplement activer ou désactiver
la fonctionnalité, et la forme table si vous définissez aussi des options de politique :

```bash
codex \
  -c 'features.network_proxy=true' \
  -c 'sandbox_workspace_write.network_access=true'

codex \
  -c 'features.network_proxy.enabled=true' \
  -c 'features.network_proxy.domains={ "api.openai.com" = "allow", "example.com" = "deny" }' \
  -c 'sandbox_workspace_write.network_access=true'

La fonctionnalité modifie la manière dont l’accès au réseau est contrôlé lorsqu’il est activé ; elle n’accorde pas
à elle seule l’accès au réseau. Utilisez `sandbox_workspace_write.network_access` avec
la configuration `workspace-write` pour déterminer si les commandes disposent d’un accès au réseau :

- Réseau désactivé + `network_proxy` activé : le réseau reste désactivé et la fonctionnalité n’a aucun effet.
- Réseau activé + `network_proxy` désactivé : le réseau reste activé avec un accès sortant direct
  sans restriction.
- Réseau activé + `network_proxy` activé : le réseau reste activé et le trafic sortant est
  limité par la politique réseau configurée.

La fonctionnalité de proxy s’applique également aux [profils d’autorisations](/fr-FR/codex/permissions#network-permissions).
Dans un profil, `network.enabled = true` autorise les commandes à accéder au réseau, tandis que
`features.network_proxy = true` active l’application des règles de domaine
de ce profil :

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
extends = ":workspace"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

Si vous omettez la fonctionnalité de proxy dans cet exemple, les commandes disposent d’un accès direct
au réseau et la règle d’autorisation `api.openai.com` ne limite pas leurs destinations.

Les exigences `experimental_network` gérées par les administrateurs sont distinctes de l’activation
de la fonctionnalité par l’utilisateur. Elles permettent de configurer et de démarrer le réseau en bac à sable sans
`features.network_proxy`, mais n’activent pas l’accès au réseau lorsque le
bac à sable actif le maintient désactivé. Consultez [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration#configure-network-access-requirements)
pour connaître la structure de `requirements.toml` côté administrateur.

#### Politique réseau

Les règles de domaine reposent d’abord sur une liste d’autorisation :

- Un nom d’hôte exact ne correspond qu’à cet hôte.
- `*.example.com` correspond aux sous-domaines tels que `api.example.com`, mais pas à
`example.com`.
- `**.example.com` correspond à la fois au domaine racine et aux sous-domaines.
- Une règle d’autorisation globale `*` correspond à tout hôte public qui n’est pas bloqué. Considérez `*`
  comme un accès réseau étendu et privilégiez des règles ciblées lorsque c’est possible.
- `deny` l’emporte toujours sur `allow`, et le caractère générique global `*` n’est valide que pour les règles d’autorisation.

#### Destinations locales et privées

Par défaut, `allow_local_binding = false` bloque les destinations de bouclage, de liaison locale et
privées :

- Exceptions ciblées : ajoutez une règle autorisant une adresse IP locale littérale exacte ou `localhost`
  lorsqu’une commande doit accéder à une cible locale.
- Accès plus large : définissez `allow_local_binding = true` uniquement si vous souhaitez délibérément
  étendre l’accès aux destinations locales ou privées.
- Caractères génériques : les règles utilisant des caractères génériques ne constituent pas des exceptions locales explicites.
- Adresses résolues : les noms d’hôte dont la résolution aboutit à des adresses IP locales ou privées restent bloqués,
même s’ils correspondent à une règle de la liste d’autorisation.

#### Protections contre le rebinding DNS

Avant d’autoriser un nom d’hôte, Codex vérifie, dans la mesure du possible, la résolution DNS et la classification
des adresses IP :

- Les requêtes de résolution qui échouent ou dépassent le délai imparti sont bloquées.
- Les noms d’hôte qui se résolvent en adresses non publiques sont bloqués.
- Cette vérification réduit le risque de rebinding DNS, sans l’éliminer. Pour empêcher totalement
le rebinding, il faudrait maintenir les adresses IP résolues fixes jusque dans la couche
de transport.

Si votre modèle de menace inclut un DNS hostile, appliquez également des contrôles du trafic sortant à une couche inférieure.

#### Paramètres dangereux

Deux paramètres élargissent délibérément le périmètre de confiance :

- `dangerously_allow_non_loopback_proxy = true` peut exposer les points d’écoute du proxy au-delà de l’interface
  de bouclage.
- `dangerously_allow_all_unix_sockets = true` contourne la liste d’autorisation des sockets Unix.

Utilisez ces paramètres uniquement dans des environnements strictement contrôlés. Lorsque le proxy de sockets Unix est
activé, les points d’écoute restent limités à la boucle locale, même si une liaison à une autre interface a été demandée.
Le réseau du bac à sable ne devient donc pas une passerelle permettant d’accéder à distance aux démons locaux.

`network_proxy` est désactivé par défaut. Lorsque vous l’activez :

| Paramètre                                | Valeur par défaut | Comportement                                                                                                                                                                              |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                              | `false` | Démarre le réseau du bac à sable uniquement lorsque l’accès au réseau des commandes est déjà activé.                                                                                                           |
| `domains`                              | non défini   | Fonctionne avec une liste d’autorisation : aucune destination externe n’est autorisée tant que vous n’ajoutez pas de règles `allow`. Prend en charge les hôtes exacts, les caractères génériques à portée limitée et les règles d’autorisation globales `*` ; `deny` est toujours prioritaire. |
| `unix_sockets`                         | non défini   | Aucune destination de socket Unix n’est autorisée tant que vous n’ajoutez pas de règles `allow` explicites.                                                                                                         |
| `allow_local_binding`                  | `false` | Bloque les destinations locales et celles des réseaux privés, sauf si vous ajoutez une règle autorisant une adresse IP locale exacte saisie littéralement ou `localhost`, ou si vous activez explicitement un accès plus large aux destinations locales et privées.                |
| `enable_socks5`                        | `true`  | Rend SOCKS5 disponible lorsque la politique l’autorise.                                                                                                                                         |
| `enable_socks5_udp`                    | `true`  | Autorise UDP via SOCKS5 lorsque SOCKS5 est disponible.                                                                                                                                      |
| `allow_upstream_proxy`                 | `true`  | Permet au réseau du bac à sable d’utiliser un proxy en amont défini dans l’environnement.                                                                                                               |
| `dangerously_allow_non_loopback_proxy` | `false` | Maintient les points de terminaison d’écoute sur la boucle locale, sauf si vous les exposez délibérément au-delà de localhost.                                                                                            |
| `dangerously_allow_all_unix_sockets`   | `false` | Maintient l’accès aux sockets Unix fondé sur une liste d’autorisation, sauf si vous contournez délibérément cette protection.                                                                                              |

### Trafic hors du proxy réseau des commandes

Le proxy réseau filtre les scripts, les programmes et les processus enfants exécutés
dans le bac à sable local des commandes. Il ne filtre pas la recherche web, les appels aux outils des applications ou
des connecteurs, les connexions aux serveurs MCP, l’activité du navigateur ou de la fonctionnalité Utilisation de l’ordinateur,
les tâches Codex Cloud, ni les requêtes du client relatives aux modèles et à l’authentification. Ces
fonctionnalités utilisent des connexions de service, des paramètres de fonctionnalités, des politiques
d’espace de travail ou des contrôles d’environnement distincts.

Les outils du navigateur vérifient séparément les interdictions réseau gérées et les listes d’autorisation exclusives
avant d’accéder à une origine. Les politiques du navigateur par origine peuvent restreindre davantage l’accès aux sites,
les téléversements, les téléchargements et les outils de développement. Consultez
[les contrôles gérés du navigateur](/fr-FR/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Pour les utilisateurs gérés, combinez la politique réseau des commandes avec des contrôles tels que
`allowed_web_search_modes`, les `mcp_servers` approuvés et les exigences relatives aux fonctionnalités
des applications, des plugins, des navigateurs ou de l’Utilisation de l’ordinateur. Consultez
[Configuration gérée](/fr-FR/codex/enterprise/managed-configuration).

Vous pouvez également contrôler [l’outil de recherche web](https://platform.openai.com/docs/guides/tools-web-search) sans accorder un accès complet au réseau aux commandes lancées. Par défaut, Codex utilise un cache de recherche web pour accéder aux résultats. Ce cache est un index de résultats web géré par OpenAI. Le mode mis en cache renvoie donc des résultats préindexés au lieu de récupérer des pages en direct. Cela réduit l’exposition aux attaques par injection de prompt provenant de contenus quelconques récupérés en direct, mais vous devez tout de même considérer les résultats web comme non fiables. Si vous utilisez `--yolo` ou un autre [paramètre de bac à sable en accès complet](#common-sandbox-and-approval-combinations), la recherche web renvoie par défaut des résultats en direct. Utilisez `--search` ou définissez `web_search = "live"` pour autoriser la navigation en direct, ou définissez la valeur sur `"disabled"` pour désactiver l’outil :

```toml
web_search = "cached"  # default
# web_search = "disabled"
# web_search = "live"  # same as --search

Définissez `web_search = "indexed"` lorsque l’accès au web externe doit être contrôlé par
l’index de recherche. Faites preuve de prudence lorsque vous activez l’accès au réseau ou la recherche web dans Codex.
Une attaque par injection de prompt peut amener l’agent à récupérer et à suivre des instructions non fiables.

## Valeurs par défaut et recommandations

- Au démarrage, Codex détecte si le dossier est sous gestion de versions et recommande :
  - Dossiers sous gestion de versions : `Auto` (écriture dans l’espace de travail + approbations sur demande)
  - Dossiers sans gestion de versions : `read-only`
- Selon votre configuration, Codex peut également démarrer en mode `read-only` tant que vous n’avez pas indiqué explicitement que le répertoire de travail est fiable (par exemple, au moyen d’une invite de configuration initiale ou de `/permissions`).
- L’espace de travail comprend le répertoire courant et les répertoires temporaires tels que `/tmp`. Utilisez la commande `/status` pour connaître les répertoires inclus dans l’espace de travail.
- Pour accepter les valeurs par défaut, exécutez `codex`.
- Vous pouvez définir ces paramètres explicitement :
  - `codex --sandbox workspace-write --ask-for-approval on-request`
  - `codex --sandbox read-only --ask-for-approval on-request`

### Chemins protégés dans les racines accessibles en écriture

Dans la politique de bac à sable `workspace-write` par défaut, les racines accessibles en écriture contiennent tout de même des chemins protégés :

- `<writable_root>/.git` est protégé en lecture seule, qu’il se présente sous la forme d’un répertoire ou d’un fichier.
- Si `<writable_root>/.git` est un fichier pointeur (`gitdir: ...`), le chemin résolu du répertoire Git est également protégé en lecture seule.
- `<writable_root>/.agents` est protégé en lecture seule lorsqu’il existe sous forme de répertoire.
- `<writable_root>/.codex` est protégé en lecture seule lorsqu’il existe sous forme de répertoire.
- La protection est récursive : tout ce qui se trouve sous ces chemins est en lecture seule.

### Exécution sans demandes d’approbation

Vous pouvez désactiver les demandes d’approbation avec `--ask-for-approval never` ou `-a never` (forme abrégée).

Cette option fonctionne avec tous les modes `--sandbox`, ce qui vous permet de continuer à contrôler le degré d’autonomie de Codex. Codex fait de son mieux dans les limites que vous définissez.

Si Codex doit lire et modifier des fichiers, ainsi qu’exécuter des commandes avec un accès au réseau sans demander d’approbation, utilisez `--sandbox danger-full-access` (ou l’option `--dangerously-bypass-approvals-and-sandbox`). Faites preuve de prudence avant de procéder.

Comme solution intermédiaire, `approval_policy = { granular = { ... } }` permet de conserver un traitement interactif pour certaines catégories de demandes d’approbation tout en refusant automatiquement les autres. La politique granulaire couvre les approbations liées au bac à sable, les demandes liées aux règles execpolicy, les demandes MCP, les demandes `request_permissions` et les approbations de scripts de skills.

### Révisions automatiques des demandes d’approbation

Par défaut, les demandes d’approbation vous sont adressées :

```toml
approvals_reviewer = "user"

Les révisions automatiques des demandes d’approbation s’appliquent lorsque les approbations sont interactives, par exemple avec
`approval_policy = "on-request"` ou une politique d’approbation granulaire. Définissez
`approvals_reviewer = "auto_review"` pour transmettre les demandes d’approbation admissibles
à un agent de révision avant que Codex n’exécute l’action demandée :

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"

Pour connaître le cycle de vie complet de l’agent de révision, les conditions de déclenchement, l’ordre de priorité des configurations
et le comportement en cas d’échec, consultez
[Révision automatique](/fr-FR/codex/sandboxing/auto-review).

L’agent de révision évalue uniquement les actions qui nécessitent déjà une approbation, telles que les demandes
d’élévation liées au bac à sable, les requêtes réseau bloquées, les demandes `request_permissions` ou
les appels d’outils d’applications et MCP ayant des effets secondaires. Les actions qui restent dans le bac à sable
se poursuivent sans étape de révision supplémentaire.

La politique de révision vérifie les risques d’exfiltration de données, de recherche d’identifiants,
d’affaiblissement durable de la sécurité et d’actions destructrices. Les actions à risque faible ou moyen
peuvent être exécutées lorsque la politique les autorise. La politique refuse les actions à risque critique.
Les actions à risque élevé exigent une autorisation suffisante de l’utilisateur et l’absence de règle de refus applicable.
Tout échec de création du prompt, de session de révision ou d’analyse entraîne un refus par défaut. Les dépassements de délai sont
signalés séparément, mais l’action n’est pas exécutée pour autant.

La [politique de révision par défaut](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)
se trouve dans le dépôt open source de Codex. Les entreprises peuvent remplacer sa
section propre au locataire à l’aide de `guardian_policy_config` dans les exigences gérées.
Le texte local défini dans `[auto_review].policy` est également pris en charge, mais les exigences gérées
sont prioritaires. Pour en savoir plus sur la configuration, consultez
[Configuration gérée](/fr-FR/codex/enterprise/managed-configuration#configure-automatic-review-policy).

Dans l’application de bureau ChatGPT, ces révisions apparaissent comme des éléments de révision automatique avec un état
tel que En cours de révision, Approuvé, Refusé, Interrompu ou Délai dépassé. Elles peuvent également
inclure un niveau de risque et une évaluation de l’autorisation accordée par l’utilisateur pour la demande
examinée.

La révision automatique effectue des appels supplémentaires au modèle, ce qui peut augmenter l’utilisation de Codex. Les administrateurs
peuvent la limiter avec `allowed_approvals_reviewers`.

### Combinaisons courantes de bac à sable et d’approbation

| Objectif                                                            | Options / configuration                                                                                                                      | Effet                                                                                                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Auto (préréglage)                                                     | _aucune option requise_ ou `--sandbox workspace-write --ask-for-approval on-request`                                                      | Codex peut lire et modifier des fichiers, ainsi qu’exécuter des commandes dans l’espace de travail. Une approbation est nécessaire pour apporter des modifications hors de l’espace de travail ou accéder au réseau. |
| Consultation sécurisée en lecture seule                                           | `--sandbox read-only --ask-for-approval on-request`                                                                                 | Codex peut lire des fichiers et répondre à des questions. Une approbation est nécessaire pour apporter des modifications, exécuter des commandes ou accéder au réseau.                               |
| Lecture seule non interactive (CI)                                    | `--sandbox read-only --ask-for-approval never`                                                                                      | Codex peut uniquement lire des fichiers et ne demande jamais d’approbation.                                                                                              |
| Modification automatique avec demande d’approbation pour les commandes non fiables | `--sandbox workspace-write --ask-for-approval untrusted`                                                                            | Codex peut lire et modifier des fichiers, mais demande une approbation avant d’exécuter des commandes non fiables.                                                           |
| Mode de révision automatique                                                  | `--sandbox workspace-write --ask-for-approval on-request -c approvals_reviewer=auto_review` ou `approvals_reviewer = "auto_review"` | Le périmètre du bac à sable reste identique à celui du mode standard d’approbation à la demande, mais les demandes d’approbation admissibles sont examinées par la Révision automatique au lieu d’être présentées à l’utilisateur.  |
| Accès complet dangereux                                             | `--dangerously-bypass-approvals-and-sandbox` (alias : `--yolo`)                                                                      |  Aucun bac à sable ; aucune approbation _(déconseillé)_                                                                               |

Pour les exécutions non interactives, utilisez `codex exec --sandbox workspace-write` ; Codex conserve les anciennes invocations `codex exec --full-auto` à des fins de compatibilité, mais elles sont obsolètes et déclenchent un avertissement.

Avec `--ask-for-approval untrusted`, Codex n’exécute automatiquement que les opérations de lecture reconnues comme sûres. Les commandes susceptibles de modifier l’état ou de déclencher une exécution externe (par exemple, les opérations Git destructrices ou les options Git de sortie ou de remplacement de configuration) nécessitent une approbation.

#### Configuration dans `config.toml`

Pour une présentation plus générale du workflow de configuration, consultez les [Principes de configuration](/fr-FR/codex/config-file/config-basic), la [Configuration avancée](/fr-FR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes) et la [Référence de configuration](/fr-FR/codex/config-file/config-reference).

```toml
# Always ask for approval mode
approval_policy = "untrusted"
sandbox_mode    = "read-only"
allow_login_shell = false # optional hardening: disallow login shells for shell-based tools

# Optional: Allow network in workspace-write mode
[sandbox_workspace_write]
network_access = true

# Optional: granular approval policy
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

Vous pouvez également enregistrer des préréglages sous forme de [fichiers de profil](/fr-FR/codex/config-file/config-advanced#profiles), puis les sélectionner avec `codex --profile profile-name` :

```toml
# ~/.codex/full_auto.config.toml
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

```toml
# ~/.codex/readonly_quiet.config.toml
approval_policy = "never"
sandbox_mode    = "read-only"

### Testez le bac à sable localement

Pour voir ce qui se passe lorsqu’une commande s’exécute dans le bac à sable de Codex, utilisez les commandes Codex CLI suivantes :

```bash
# macOS
codex sandbox macos [--permissions-profile <name>] [--log-denials] [COMMAND]...
# Linux
codex sandbox linux [--permissions-profile <name>] [COMMAND]...
# Windows
codex sandbox windows [--permissions-profile <name>] [COMMAND]...

La commande `sandbox` est également disponible sous la forme `codex debug`, et les utilitaires propres à chaque plateforme disposent d’alias (par exemple, `codex sandbox seatbelt` et `codex sandbox landlock`).

## Bac à sable au niveau du système d’exploitation

Codex met en œuvre le bac à sable différemment selon votre système d’exploitation :

- **macOS** utilise des politiques Seatbelt et exécute les commandes avec `sandbox-exec`, en utilisant un profil (`-p`) correspondant au mode `--sandbox` sélectionné. Lorsque l’accès restreint en lecture active les paramètres par défaut de la plateforme, Codex ajoute une politique macOS aux règles soigneusement sélectionnées, au lieu d’autoriser largement l’accès à `/System`, afin de préserver la compatibilité avec les outils courants.
- **Linux** utilise par défaut `bwrap` et `seccomp`.
- **Windows** utilise l’implémentation Linux du bac à sable lorsque Codex s’exécute dans [Windows Subsystem for Linux 2 (WSL2)](/fr-FR/codex/windows/wsl). WSL1 était pris en charge jusqu’à Codex `0.114` ; à partir de `0.115`, le bac à sable Linux est passé à `bwrap`, et WSL1 n’est donc plus pris en charge. Lorsque Codex s’exécute nativement sur Windows, il utilise une implémentation du [bac à sable Windows](/fr-FR/codex/windows/windows-sandbox#windows-sandbox).

Si vous utilisez l’extension IDE Codex sur Windows, elle prend directement en charge WSL2. Définissez le paramètre suivant dans VS Code afin de maintenir l’agent dans WSL2 chaque fois que cet environnement est disponible :

```json
{
  "chatgpt.runCodexInWindowsSubsystemForLinux": true
}

Ainsi, l’extension IDE reprend le fonctionnement du bac à sable Linux pour les commandes, les approbations et l’accès au système de fichiers, même lorsque le système d’exploitation hôte est Windows. Pour en savoir plus, consultez le [guide WSL](/fr-FR/codex/windows/wsl).

Lors d’une exécution native sur Windows, configurez le mode de bac à sable natif dans `config.toml` :

```toml
[windows]
sandbox = "unelevated" # or "elevated"
# sandbox_private_desktop = true  # default; set false only for compatibility

Pour plus de détails, consultez le [guide de configuration pour Windows](/fr-FR/codex/windows/windows-sandbox#windows-sandbox).

Lorsque vous exécutez Linux dans un environnement conteneurisé tel que Docker, le bac à sable peut ne pas fonctionner si la configuration de l’hôte ou du conteneur bloque les opérations sur les espaces de noms, l’exécution setuid de `bwrap` ou les opérations `seccomp` nécessaires à Codex.

Dans ce cas, configurez votre conteneur Docker afin qu’il fournisse l’isolation nécessaire, puis exécutez `codex` avec `--sandbox danger-full-access` (ou l’option `--dangerously-bypass-approvals-and-sandbox`) dans le conteneur.

### Exécutez Codex dans des Dev Containers

Si votre hôte ne peut pas exécuter directement le bac à sable Linux, ou si votre organisation a déjà adopté le développement conteneurisé comme standard, exécutez Codex avec Dev Containers et laissez Docker assurer l’isolation externe. Cette solution fonctionne avec Visual Studio Code Dev Containers et les outils compatibles.

Utilisez [l’exemple de devcontainer sécurisé de Codex](https://github.com/openai/codex/tree/main/.devcontainer) comme implémentation de référence. Cet exemple installe Codex, des outils de développement courants, `bubblewrap` et des mécanismes de contrôle du trafic sortant fondés sur un pare-feu.

  Les devcontainers offrent une protection importante, mais n’empêchent pas toutes les
  attaques. Si vous exécutez Codex avec `--sandbox danger-full-access` ou
`--dangerously-bypass-approvals-and-sandbox` dans le conteneur, un projet malveillant
  peut exfiltrer tout ce qui est accessible dans le devcontainer, y compris
  les identifiants Codex. N’utilisez cette configuration qu’avec des dépôts de confiance et
  surveillez l’activité de Codex comme dans tout autre environnement à privilèges élevés.

L’implémentation de référence comprend :

- une image de base Ubuntu 24.04 avec Codex et des outils de développement courants préinstallés ;
- un profil de pare-feu fondé sur une liste d’autorisation pour l’accès sortant ;
- des paramètres VS Code et des recommandations d’extensions pour rouvrir l’espace de travail dans un conteneur ;
- des montages persistants pour l’historique des commandes et la configuration de Codex ;
- `bubblewrap`, afin que Codex puisse continuer à utiliser son bac à sable Linux lorsque le conteneur accorde les capacités nécessaires.

Pour l’essayer :

1. Installez Visual Studio Code et [l’extension Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2. Copiez la configuration `.devcontainer` de l’exemple Codex dans votre dépôt, ou partez directement du dépôt Codex.
3. Dans VS Code, exécutez **Dev Containers: Open Folder in Container...** et sélectionnez `.devcontainer/devcontainer.secure.json`.
4. Une fois le conteneur démarré, ouvrez un terminal et exécutez `codex`.

Vous pouvez également démarrer le conteneur depuis la CLI :

```bash
devcontainer up --workspace-folder . --config .devcontainer/devcontainer.secure.json

L’exemple comporte trois éléments principaux :

- `.devcontainer/devcontainer.secure.json` contrôle les paramètres, les capacités, les montages et les variables d’environnement du conteneur, ainsi que les extensions VS Code.
- `.devcontainer/Dockerfile.secure` définit l’image basée sur Ubuntu et les outils installés.
- `.devcontainer/init-firewall.sh` applique la politique de contrôle du trafic réseau sortant.

Le pare-feu de référence constitue volontairement un point de départ. Si votre isolation repose sur une liste de domaines autorisés, mettez en place des protections contre le rebinding DNS et les risques liés à l’actualisation DNS adaptées à votre environnement, par exemple des actualisations tenant compte du TTL ou un pare-feu prenant en compte le DNS.

Dans le conteneur, choisissez l’un des modes suivants :

- Maintenez le bac à sable Linux de Codex activé si le profil Dev Container accorde les capacités dont `bwrap` a besoin pour créer le bac à sable interne.
- Si le conteneur constitue le périmètre de sécurité souhaité, exécutez Codex avec `--sandbox danger-full-access` dans le conteneur afin qu’il ne tente pas de créer une seconde couche de bac à sable.

## Gestion des versions

Codex fonctionne mieux avec un workflow de gestion des versions :

- Travaillez sur une branche de fonctionnalité et veillez à ce que `git status` n’indique aucune modification avant de déléguer une tâche. Les patchs de Codex seront ainsi plus faciles à isoler et à annuler.
- Privilégiez les workflows fondés sur des patchs (par exemple, `git diff`/`git apply`) plutôt que de modifier directement les fichiers suivis. Effectuez fréquemment des commits afin de pouvoir revenir en arrière par petites étapes.
- Traitez les suggestions de Codex comme toute autre PR : exécutez des vérifications ciblées, examinez les diffs et consignez les décisions dans les messages de commit à des fins d’audit.

## Supervision et télémétrie

Codex prend en charge une supervision facultative via OpenTelemetry (OTel) pour aider les équipes à auditer l’utilisation, à analyser les problèmes et à respecter les exigences de conformité sans affaiblir les paramètres de sécurité locaux par défaut. La télémétrie est désactivée par défaut ; activez-la explicitement dans votre configuration.

### Vue d’ensemble

- Par défaut, Codex désactive l’export OTel afin que les exécutions locales restent autonomes.
- Lorsque cette option est activée, Codex émet des événements de journalisation structurés concernant les discussions, les requêtes API, l’activité des flux SSE/WebSocket, les prompts des utilisateurs (masqués par défaut), les décisions d’approbation des outils et les résultats des outils.
- Codex associe aux événements exportés `service.name` (émetteur), la version de la CLI et un libellé d’environnement afin de distinguer le trafic de développement, de préproduction et de production.

### Activez OTel (facultatif)

Ajoutez un bloc `[otel]` à votre configuration Codex (généralement `~/.codex/config.toml`), puis choisissez un exportateur et indiquez si le texte des prompts doit être journalisé.

```toml
[otel]
environment = "staging"   # dev | staging | prod
exporter = "none"          # none | otlp-http | otlp-grpc
log_user_prompt = false     # redact prompt text unless policy allows

- `exporter = "none"` maintient l’instrumentation active, mais n’envoie aucune donnée.
- Pour envoyer les événements à votre propre collecteur, choisissez l’une des options suivantes :

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}

Codex regroupe les événements par lots et envoie ceux en attente à l’arrêt. Codex exporte uniquement les données de télémétrie produites par son module OTel.

### Catégories d’événements

Voici quelques types d’événements représentatifs :

- `codex.conversation_starts` (modèle, paramètres de raisonnement, politique de bac à sable et d’approbation)
- `codex.api_request` (tentative, statut/réussite, durée et détails de l’erreur)
- `codex.sse_event` (type d’événement du flux, réussite/échec, durée et nombre de tokens lors de `response.completed`)
- `codex.websocket_request` et `codex.websocket_event` (durée de la requête et type/réussite/erreur pour chaque message)
- `codex.user_prompt` (longueur ; contenu masqué sauf si sa journalisation est explicitement activée)
- `codex.tool_decision` (approbation/refus, origine : configuration ou utilisateur)
- `codex.tool_result` (durée, réussite, extrait de la sortie)

Les métriques OTel associées (paires composées d’un compteur et d’un histogramme de durée) comprennent `codex.api_request`, `codex.sse_event`, `codex.websocket.request`, `codex.websocket.event` et `codex.tool.call` (avec les instruments `.duration_ms` correspondants).

Pour consulter le catalogue complet des événements et la référence de configuration, consultez la [documentation de configuration de Codex sur GitHub](https://github.com/openai/codex/blob/main/docs/config.md#otel).

### Recommandations de sécurité et de confidentialité

- Conservez `log_user_prompt = false`, sauf si votre politique autorise explicitement le stockage du contenu des prompts. Les prompts peuvent contenir du code source et des données sensibles.
- Acheminez les données de télémétrie uniquement vers des collecteurs que vous contrôlez ; appliquez des limites de conservation et des contrôles d’accès adaptés à vos exigences de conformité.
- Traitez les arguments et les sorties des outils comme des données sensibles. Lorsque c’est possible, privilégiez le masquage au niveau du collecteur ou du SIEM.
- Vérifiez les paramètres de conservation des données locales (par exemple, `history.persistence` / `history.max_bytes`) si vous ne souhaitez pas que Codex enregistre les transcriptions des sessions dans `CODEX_HOME`. Consultez les sections [Configuration avancée](/fr-FR/codex/config-file/config-advanced#history-persistence) et [Référence de configuration](/fr-FR/codex/config-file/config-reference).
- Si vous exécutez la CLI sans accès au réseau, l’exportation OTel ne peut pas atteindre votre collecteur. Pour exporter les données, autorisez l’accès au réseau en mode `workspace-write` pour le point de terminaison OTel, ou exportez-les depuis Codex Cloud avec le domaine du collecteur dans votre liste de domaines autorisés.
- Examinez régulièrement les événements pour détecter les modifications apportées aux approbations ou au bac à sable, ainsi que les exécutions d’outils inattendues.

OTel est facultatif et conçu pour compléter, sans les remplacer, les protections liées au bac à sable et aux approbations décrites ci-dessus.

## Configuration gérée

Les administrateurs d’entreprise peuvent configurer les paramètres de sécurité de Codex pour leur espace de travail dans [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration). Consultez cette page pour en savoir plus sur la configuration et les politiques.
