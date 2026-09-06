<!-- source: https://learn.chatgpt.com/fr-FR/docs/sandboxing/auto-review -->

La Révision automatique remplace l’approbation manuelle à la limite du bac à sable par un
agent de révision distinct. L’agent Codex principal s’exécute toujours dans le même bac à sable, avec
la même politique d’approbation et les mêmes limites réseau et de système de fichiers. La
seule différence tient à l’agent qui examine les demandes d’élévation admissibles.

  La Révision automatique ne s’applique que si les approbations sont interactives. En pratique, cela
  signifie utiliser `approval_policy = "on-request"` ou une politique d’approbation granulaire qui
  affiche toujours la catégorie de prompt concernée. Avec `approval_policy = "never"`,
  il n’y a rien à réviser.

Dans l’application de bureau ChatGPT, sélectionner un modèle Daybreak approuvé
fait automatiquement passer le contrôle des autorisations à **Approuver pour moi** lorsque ce
mode est disponible pour votre compte et autorisé par la politique de l’organisation. Cette règle
s’applique aussi lorsque vous utilisez la commande `/model` de l’application de bureau. Si ce mode
n’est pas disponible, le mode d’autorisation actuel reste inchangé. Le choix du modèle
ne supplante jamais les exigences gérées de l’organisation.

Avant d’activer **Accès complet** pour un modèle de sécurité approuvé, l’application
de bureau ChatGPT affiche un avertissement propre au modèle concernant les actions dangereuses. Cet
avertissement recommande plutôt **Approuver pour moi** et renvoie vers la
[configuration de la politique de révision](#configuration). L’avertissement ne rétablit pas
la limite du bac à sable et ne prévaut pas sur la politique de l’organisation.

## Fonctionnement de la Révision automatique

Dans les grandes lignes, le flux est le suivant :

1. L’agent principal travaille dans `read-only` ou `workspace-write`.
2. Lorsqu’il doit franchir la limite du bac à sable, il demande une approbation.
3. Si `approvals_reviewer = "auto_review"`, Codex transmet cette demande d’approbation
   à un agent de révision distinct au lieu d’interrompre l’exécution pour solliciter l’intervention d’une personne.
4. L’agent de révision détermine si l’action doit être exécutée et fournit une justification.
5. Si l’action est approuvée, l’exécution se poursuit. Si elle est refusée, l’agent
principal reçoit pour instruction de trouver une solution nettement plus sûre ou de s’arrêter et de demander
à l’utilisateur.

La Révision automatique change l’agent chargé de la révision ; elle n’accorde pas d’autorisation. Elle n’étend pas
`writable_roots`, n’active pas l’accès au réseau et n’assouplit pas la protection des chemins. Elle
modifie uniquement la façon dont Codex traite les actions qui nécessitent déjà une approbation.

## Quand elle se déclenche

La Révision automatique évalue les demandes d’approbation qui, autrement, suspendraient l’exécution dans l’attente d’une intervention humaine.
Les cas concernés sont notamment les suivants :

- Les appels d’outils shell ou exec qui demandent des autorisations élevées dans le bac à sable.
- Les requêtes réseau bloquées par le bac à sable ou la politique en vigueur.
- Les modifications de fichiers en dehors des racines autorisées en écriture.
- Les appels d’outils MCP ou d’application qui nécessitent une approbation en fonction de leurs annotations d’outil
ou du mode d’approbation configuré.
- L’accès à un nouveau site web ou domaine via la fonctionnalité Utilisation de l’ordinateur.

La Révision automatique ne s’exécute pas pour les actions courantes déjà autorisées dans le
bac à sable. Si une commande peut s’exécuter avec le `sandbox_mode` actif, ou si un appel d’outil
reste conforme à la politique autorisée, l’agent principal poursuit sans révision.

L’Utilisation de l’ordinateur constitue un cas distinct. Les approbations de l’App relatives à l’Utilisation de l’ordinateur sont toujours présentées
directement à l’utilisateur ; la Révision automatique ne remplace donc pas ces prompts au niveau de l’App.

## Ce que bloque la Révision automatique

Dans les grandes lignes, la Révision automatique vise à bloquer des actions telles que :

- l’envoi de données privées, de secrets ou d’identifiants vers des destinations non fiables
- la recherche d’identifiants, de tokens, de cookies ou de données de session
- un affaiblissement généralisé ou persistant de la sécurité
- des actions destructrices présentant un risque important de dommages irréversibles

La politique exacte se trouve dans le dépôt Codex open source :
[policy\_template.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy_template.md)
et
[policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).
Cette politique peut être personnalisée par entreprise avec `guardian_policy_config` ou
par utilisateur avec le paramètre local [`[auto_review].policy`](/fr-FR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes).

## Ce que voit l’agent de révision

L’agent de révision est lui-même un agent Codex, mais sa mission est plus restreinte que celle de l’agent principal :
déterminer si une action précise franchissant une limite doit être exécutée.

L’agent de révision voit une transcription concise ainsi que la demande d’approbation exacte. Cet ensemble
comprend généralement les messages de l’utilisateur, les mises à jour visibles de l’assistant, les appels d’outils pertinents
et leurs sorties, ainsi que l’action dont l’approbation est proposée. L’agent peut
également effectuer des vérifications en lecture seule pour obtenir le contexte manquant, mais il le fait rarement.

Le raisonnement masqué de l’assistant n’est pas inclus. La Révision automatique accède aux éléments conservés de la
conversation et aux données fournies par les outils, mais pas au raisonnement détaillé privé (« chain-of-thought »).

## Refus et comportement en cas d’échec

Un refus explicite n’est pas traité comme une erreur ordinaire du bac à sable. Codex renvoie
la justification de la révision à l’agent principal et ajoute une instruction plus stricte :

- Ne cherchez pas à obtenir le même résultat par une solution détournée, une exécution indirecte ou un
contournement de la politique.
- Ne continuez qu’avec une solution nettement plus sûre.
- Sinon, arrêtez-vous et demandez à l’utilisateur.

Codex applique également un coupe-circuit en cas de refus à chaque tour. Dans l’implémentation
open source actuelle, la Révision automatique interrompt le tour après `3`
refus consécutifs ou `10` refus dans une fenêtre glissante couvrant les `50`
dernières révisions du même tour.

Tout résultat autre qu’un refus réinitialise le compteur de refus consécutifs. Lorsque le coupe-circuit se déclenche,
Codex émet un avertissement et abandonne le tour en cours en déclenchant une interruption, au lieu
de laisser l’agent boucler sur de nouvelles tentatives d’élévation.

Les expirations de délai sont signalées séparément des refus explicites, et l’agent principal est
informé qu’une expiration de délai ne prouve pas à elle seule que l’action est dangereuse.

Il existe aussi une procédure explicite pour passer outre un refus. Dans l’interface TUI
open source actuelle, exécutez `/approve` pour ouvrir le sélecteur **Refus de la Révision automatique**, puis
sélectionnez une action récemment refusée afin d’autoriser une seule nouvelle tentative. Codex consigne jusqu’à 10
refus récents par tâche. Cette approbation a une portée limitée : elle s’applique exactement à
l’action refusée, et non aux actions similaires à venir ; elle est enregistrée pour une nouvelle tentative unique dans le
même contexte ; et cette tentative passe quand même par la Révision automatique. En interne,
Codex injecte un marqueur d’approbation limité au contexte développeur pour cette action précise.
L’agent de révision voit alors cette dérogation explicite de l’utilisateur dans le contexte, mais continue de respecter
la politique et peut à nouveau refuser l’action si celle-ci indique que l’utilisateur ne peut pas passer outre cette catégorie de
refus.

## Configuration

Pour en savoir plus sur la configuration, consultez
[Configuration gérée](/fr-FR/codex/enterprise/managed-configuration#configure-automatic-review-policy).

La politique par défaut de l’agent de révision se trouve dans le dépôt Codex open source :
[core/src/guardian/policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md).
Les entreprises peuvent remplacer sa section propre au locataire par
`guardian_policy_config` dans les exigences gérées. Les utilisateurs individuels peuvent aussi définir
une politique locale
[`[auto_review].policy`](/fr-FR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
dans leur `config.toml`, mais les exigences gérées sont prioritaires :

```toml
[auto_review]
policy = """
YOUR POLICY GOES HERE
"""

Pour personnaliser la politique, commencez par copier l’intégralité du texte de la politique par défaut, puis
adaptez-la progressivement à votre propre profil de risque.

## Configurez une mission de cybersécurité autorisée

Pour les activités de sécurité autorisées, associez la Révision automatique à un périmètre
d’intervention formalisé par écrit et à un [profil d’autorisations](/fr-FR/codex/permissions) appliquant le principe du moindre privilège.
Utilisez une cible de laboratoire approuvée, documentez les actions et la fenêtre d’intervention, et
excluez du périmètre les systèmes de production, les hôtes sans rapport, les identifiants et les modifications persistantes,
sauf autorisation explicite.

`[auto_review].policy` et `guardian_policy_config` remplacent tous deux votre politique actuelle
de l’agent de révision. Ils ne sont pas fusionnés avec les politiques fournies avec votre modèle ou
gérées par votre organisation. Les instructions de révision et le format de réponse
intégrés continuent de s’appliquer. Avant d’utiliser l’un de ces exemples, copiez l’intégralité de la politique
actuelle, conservez toutes les règles existantes et ajoutez celles qui correspondent à vos activités approuvées.
Remplacez l’espace réservé en majuscules par cette politique complète. Si vous ne pouvez pas
accéder à la politique actuelle, ne la redéfinissez pas.

Le modèle de fichier `config.toml` local suivant active la révision et ajoute des conditions de portée limitée
à la suite de la politique existante de l’agent de révision :

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = ":workspace"

[auto_review]
policy = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.
- Approved actions: inspect the target, reproduce authorized vulnerabilities,
  and validate fixes within the documented engagement window.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only actions against the approved target that match the documented
  engagement scope and approved actions.
- Deny out-of-scope or unknown hosts, production access, credential theft,
  persistence, data exfiltration, destructive operations, and policy bypass.
- Deny ambiguous actions and high-impact changes until a human explicitly
  approves the exact target, action, and side effects.
"""

Remplacez la cible et les actions autorisées de l’exemple par le périmètre réellement approuvé.
Appliquez les restrictions de cible au moyen de règles indépendantes pour le système de fichiers et le réseau ;
les instructions de l’agent de révision ne remplacent pas ces limites.

Les organisations peuvent appliquer les mêmes conditions dans la configuration `requirements.toml` gérée :

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
default_permissions = ":workspace"

guardian_policy_config = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only approved actions against the documented engagement target.
- Deny out-of-scope hosts, production access, credential theft, persistence,
  data exfiltration, destructive operations, and attempts to bypass policy.
- Deny ambiguous or high-impact actions until a human explicitly approves the
  exact target, action, and side effects.
"""

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

`allowed_permission_profiles` contrôle les profils d’autorisations actuels.
`allowed_sandbox_modes` empêche également l’accès complet dans les déploiements qui utilisent encore
l’ancien `sandbox_mode`.

Le paramètre `guardian_policy_config` géré est prioritaire sur le paramètre local de l’utilisateur
`[auto_review].policy`. Conservez `approval_policy = "on-request"` ou une autre
politique d’approbation interactive admissible, ainsi qu’une limite effective du bac à sable.
Avec `approval_policy = "never"`, `:danger-full-access` ou `--yolo`, une action
peut ne pas générer la demande d’approbation liée au franchissement de la limite dont la révision a besoin.

Une destination réseau figurant sur la liste d’autorisation ne déclenche pas à elle seule une révision. Ajoutez
des [règles de commande](/fr-FR/codex/agent-configuration/rules) explicites avec
`decision = "prompt"`, ou configurez les outils MCP sensibles pour qu’ils exigent une approbation,
lorsque les actions effectuées dans le bac à sable doivent malgré tout être soumises à l’agent de révision.

Consultez [Modèles et accès de confiance](/fr-FR/codex/cyber-safety) et la [configuration
recommandée](/fr-FR/codex/cyber-safety/recommended-configuration) pour l’accès aux modèles,
la configuration de la mission et les workflows d’agents personnalisés. Consultez [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration#configure-automatic-review-policy)
pour connaître l’ordre de priorité en entreprise et les versions clientes prises en charge. Pour les harnais personnalisés reposant sur une API ou
sur Agents SDK, utilisez [Garde-fous et révision humaine](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution).

## Réduisez le volume de révisions sans affaiblir la sécurité

La Révision automatique fonctionne mieux lorsque le bac à sable couvre déjà vos workflows sûrs
les plus courants. Si trop d’actions banales nécessitent une révision, corrigez d’abord la limite
plutôt que d’apprendre à l’agent de révision à approuver indéfiniment des demandes d’élévation superflues.

En pratique, les changements les plus efficaces sont les suivants :

- Ajoutez des
[`writable_roots`](/fr-FR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
  de portée restreinte pour les répertoires temporaires ou les dépôts voisins que vous utilisez volontairement.
- Ajoutez des [règles de préfixe](/fr-FR/codex/agent-configuration/rules) de portée restreinte. Préférez des préfixes de
  commande précis comme `["cargo", "test"]` ou `["pnpm", "run", "lint"]` à des
  motifs généraux comme `["python"]` ou `["curl"]`. Les règles trop générales font souvent disparaître précisément la
  limite que la Révision automatique est censée protéger.

Les transcriptions des sessions de Révision automatique sont conservées sous `~/.codex/sessions` par
défaut ; vous pouvez donc demander à Codex d’y analyser les activités passées avant de modifier
la politique ou les autorisations.

## Limites

La Révision automatique améliore le compromis par défaut pour les tâches agentiques de longue durée,
mais elle n’offre pas de garantie de sécurité déterministe.

- Elle évalue uniquement les actions qui demandent à franchir une limite.
- Elle peut néanmoins commettre des erreurs, en particulier dans des contextes hostiles ou inhabituels.
- Elle doit compléter, et non remplacer, une bonne conception du bac à sable, une surveillance efficace et
une politique propre à l’organisation.

Pour connaître les fondements de cette recherche et les résultats d’évaluation publiés, consultez le
[billet d’Alignment Research sur la Révision automatique](https://alignment.openai.com/auto-review/).
