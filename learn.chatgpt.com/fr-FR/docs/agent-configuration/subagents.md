<!-- source: https://learn.chatgpt.com/fr-FR/docs/agent-configuration/subagents -->

ChatGPT Work et Codex peuvent exécuter des workflows avec des sous-agents en lançant des agents spécialisés en parallèle, puis en regroupant leurs résultats dans une seule réponse. Cette approche peut être particulièrement utile pour les tâches complexes qui se prêtent largement à une exécution en parallèle, comme l’exploration d’une base de code ou la mise en œuvre d’un plan de développement de fonctionnalité en plusieurs étapes.

Dans les clients Codex locaux, vous pouvez également définir des agents personnalisés avec des configurations de modèle et des instructions adaptées à différentes tâches.

## Disponibilité

ChatGPT Work permet aux comptes éligibles d’utiliser des workflows avec des sous-agents et de consulter leur activité.

<a id="custom-agents"></a>

Les versions actuelles de Codex activent par défaut les workflows avec des sous-agents. Leur activité apparaît dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE.

Comme chaque sous-agent effectue ses propres opérations avec le modèle et les outils, les workflows avec des sous-agents consomment plus de tokens que des exécutions comparables avec un seul agent.

Dans ChatGPT Work, demandez à ChatGPT de déléguer les tâches indépendantes à des sous-agents. Les agents s’exécutent dans l’environnement hébergé de ChatGPT, et la discussion affiche leur activité et leurs résultats. Pour la plupart des niveaux d’intelligence, demandez explicitement la délégation. Avec Ultra, ChatGPT peut déléguer de sa propre initiative lorsque des agents travaillant en parallèle permettraient d’améliorer sensiblement la vitesse ou la qualité.

Dans une discussion de l’application, demandez à Codex de déléguer les parties indépendantes du travail à
des sous-agents. Les versions locales actuelles de Codex délèguent lorsque vous le demandez directement ou lorsque
les instructions applicables d’un fichier `AGENTS.md` ou d’une skill le demandent. L’application affiche chaque
fil de sous-agent afin que vous puissiez examiner son travail et le résumé renvoyé à la
discussion principale.

Dans une session CLI interactive, demandez à Codex d’utiliser des sous-agents. Codex peut également suivre
les instructions applicables d’un fichier `AGENTS.md` ou d’une skill qui demandent une délégation. Utilisez
`/agent` pour examiner les fils d’agents et passer de l’un à l’autre pendant leur exécution. Le fil
principal regroupe les résultats des sous-agents dans sa réponse finale.

Dans une discussion de l’IDE, demandez à Codex de déléguer les parties indépendantes du travail à des sous-agents.
Codex peut également suivre les instructions applicables d’un fichier `AGENTS.md` ou d’une skill qui demandent une
délégation. Lorsque l’interface des agents en arrière-plan est disponible, les sous-agents actifs apparaissent
au-dessus de la zone de saisie. Développez le panneau pour consulter leur état, arrêter tous les
sous-agents actifs ou ouvrir le fil d’un sous-agent particulier.

## Pourquoi utiliser des workflows avec des sous-agents

Même avec de grandes fenêtres de contexte, les modèles ont leurs limites. Si vous surchargez la discussion principale (où vous définissez les exigences, les contraintes et les décisions) de sorties intermédiaires encombrantes telles que des notes d’exploration, des journaux de test, des traces de pile et des sorties de commande, la session peut perdre en fiabilité au fil du temps.

On parle souvent de :

- **Pollution du contexte** : les informations utiles sont noyées dans des sorties intermédiaires encombrantes.
- **Dégradation du contexte** : les performances diminuent à mesure que la discussion se remplit de détails moins pertinents.

Pour en savoir plus, consultez l’article de Chroma sur la [dégradation du contexte](https://research.trychroma.com/context-rot).

Les workflows avec des sous-agents aident à résoudre ce problème en déplaçant hors du fil principal les tâches qui génèrent beaucoup de sorties intermédiaires :

- Gardez l’ **agent principal** concentré sur les exigences, les décisions et les résultats finaux.
- Exécutez des **sous-agents** spécialisés en parallèle pour l’exploration, les tests ou l’analyse des journaux.
- Faites renvoyer aux sous-agents des **résumés** plutôt que des sorties intermédiaires brutes.

Ces workflows peuvent également faire gagner du temps lorsque les tâches peuvent s’exécuter indépendamment en parallèle. Ils facilitent aussi le traitement des tâches de grande ampleur en les décomposant en éléments bien délimités. Par exemple, Codex peut décomposer l’analyse d’un document de plusieurs millions de tokens en problèmes plus petits, puis renvoyer une synthèse des principaux enseignements au fil principal.

Pour commencer, utilisez des agents en parallèle pour les tâches qui nécessitent beaucoup de lecture, comme l’exploration, les tests, le triage et la synthèse. Faites preuve de davantage de prudence avec les workflows parallèles qui impliquent beaucoup d’écriture, car des agents qui modifient le code simultanément peuvent créer des conflits et alourdir la coordination.

## Termes essentiels

Codex emploie plusieurs termes associés dans les workflows avec des sous-agents :

- **Workflow avec des sous-agents** : workflow dans lequel Codex exécute des agents en parallèle et combine leurs résultats.
- **Sous-agent** : agent que Codex lance pour lui déléguer une tâche précise.
- **Fil d’agent** : fil dans lequel un sous-agent effectue son travail. Les clients compatibles vous permettent d’ouvrir ces fils pour examiner la progression ou les résultats.

## Déclenchement des workflows avec des sous-agents

Pour la plupart des niveaux d’intelligence, demandez directement l’utilisation de sous-agents ou le travail de plusieurs agents en parallèle. Ultra permet la délégation proactive : ChatGPT peut ainsi déléguer les tâches indépendantes qui s’y prêtent sans demande distincte.

Demandez directement l’utilisation de sous-agents ou le travail de plusieurs agents en parallèle. Codex peut également déléguer lorsque les instructions applicables d’un projet ou d’une skill le demandent.

En pratique, le déclenchement manuel consiste à utiliser des instructions directes telles que « Lancez deux agents », « Déléguez ce travail en parallèle » ou « Utilisez un agent par point ». Les workflows avec des sous-agents consomment plus de tokens que des exécutions comparables avec un seul agent, car chaque sous-agent effectue ses propres opérations avec le modèle et les outils.

Un bon prompt pour utiliser des sous-agents doit expliquer comment répartir le travail, indiquer si Codex doit attendre tous les agents avant de poursuivre et préciser le résumé ou le résultat à renvoyer.

```text
Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.

## Choix des modèles et du niveau de raisonnement

Les agents n’ont pas tous besoin des mêmes paramètres de modèle et de raisonnement.

Dans ChatGPT Work, choisissez un modèle et un niveau d’intelligence dans la zone de saisie.
Selon le modèle sélectionné, les niveaux d’intelligence disponibles peuvent inclure **Léger**, **Médium**, **Élevé**,
**Très élevé** et **Max**. **Ultra** est
réservé aux comptes éligibles et aux modèles compatibles. Il utilise un effort de
raisonnement maximal et permet à ChatGPT de déléguer de sa propre initiative les tâches appropriées à des sous-agents.

Aux autres niveaux d’intelligence, demandez explicitement des sous-agents lorsque vous souhaitez déléguer du travail en parallèle.

Si vous ne configurez ni le modèle d’un sous-agent ni `model_reasoning_effort`, le
sous-agent hérite du modèle et de l’effort de raisonnement de l’agent parent. Si une demande
explicite de lancement ou une valeur par défaut de `[agents]` sélectionne un modèle sans effort de
raisonnement explicitement indiqué ou configuré, le sous-agent utilise l’effort de raisonnement
par défaut de ce modèle. Pour équilibrer l’intelligence, la vitesse et le coût pour chaque tâche,
demandez un modèle ou un effort de raisonnement précis dans votre prompt,
configurez les valeurs par défaut de `[agents]` dans `config.toml`, ou définissez `model` et
`model_reasoning_effort` directement dans le fichier de l’agent personnalisé.
Par exemple, utilisez <code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> pour des analyses rapides ou une configuration de <code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code> avec un effort de raisonnement supérieur pour les raisonnements plus exigeants.

  Pour la plupart des tâches dans Codex, commencez par{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>. Utilisez{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> si vous recherchez
  une option plus rapide et moins coûteuse pour les tâches légères confiées à des sous-agents.

### Choix du modèle

- **<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>** : commencez par ce modèle pour les agents chargés de tâches exigeantes. C’est le plus performant pour les travaux ambigus en plusieurs étapes qui nécessitent de planifier, d’utiliser des outils, de valider les résultats et de mener le travail à son terme dans un contexte plus étendu.
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>** : utilisez ce modèle pour les agents qui privilégient la vitesse et l’efficacité plutôt que la profondeur, par exemple pour l’exploration, les analyses nécessitant beaucoup de lecture, la revue de fichiers volumineux ou le traitement de documents complémentaires. Il convient bien aux agents qui travaillent en parallèle et renvoient des résultats synthétisés à l’agent principal.
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestNanoModel.slug}</code>** : utilisez ce modèle pour les agents rapides au périmètre restreint qui traitent des tâches claires, reproductibles ou en grand volume.

### Effort de raisonnement (`model_reasoning_effort`)

- **`ultra`** : utilisez ce niveau pour le raisonnement le plus approfondi lorsque le modèle sélectionné
  le prend en charge.
- **`max`** et **`xhigh`** : utilisez ces niveaux pour les raisonnements particulièrement exigeants lorsque le
  modèle sélectionné les prend en charge.
- **`high`** : utilisez ce niveau lorsqu’un agent doit suivre une logique complexe, vérifier des hypothèses ou étudier des cas limites (par exemple, les agents chargés de la revue ou spécialisés dans la sécurité).
- **`medium`** : niveau par défaut équilibré pour la plupart des agents.
- **`low`** : utilisez ce niveau lorsque la tâche est simple et que la vitesse est prioritaire.

Un effort de raisonnement supérieur augmente le temps de réponse et la consommation de tokens, mais peut améliorer la qualité des résultats pour les tâches complexes. Pour en savoir plus, consultez [Modèles](/fr-FR/codex/models), [Principes de configuration](/fr-FR/codex/config-file/config-basic) et [Référence de configuration](/fr-FR/codex/config-file/config-reference).

## Orchestration et gestion des fils

ChatGPT ou Codex gère l’orchestration entre les agents, notamment le lancement de nouveaux sous-agents, la transmission des instructions de suivi, l’attente des résultats et la fermeture des fils d’agents.

Lorsque de nombreux agents sont en cours d’exécution, Codex attend que tous les résultats demandés soient disponibles, puis renvoie une réponse consolidée.

Pour la plupart des niveaux d’intelligence, ChatGPT lance des agents après une demande directe. Avec Ultra, ChatGPT peut également déléguer de sa propre initiative lorsque le travail en parallèle est utile.

Les versions locales actuelles de Codex lancent des agents après une demande directe ou en réponse à une instruction applicable d’un projet ou d’une skill.

Pour voir ce mécanisme en action, essayez le prompt suivant sur votre projet :

```text
I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race
5. Test flakiness
6. Maintainability of the code

## Gestion des sous-agents

Ouvrez **Sous-agents** pour consulter les listes en lecture seule **Actifs** et **Terminés** . Sélectionnez un
sous-agent ayant terminé pour examiner ses détails et son résultat. La barre latérale web affiche
l’activité des sous-agents ; elle ne propose pas de commandes pour arrêter ou orienter un sous-agent
particulier.

- Depuis l’activité affichée dans le fil principal, ouvrez le fil d’un sous-agent pour examiner son travail.
- Demandez directement à Codex d’orienter un sous-agent en cours d’exécution, de l’arrêter ou de fermer les fils des sous-agents ayant terminé.

  

  

- Utilisez `/agent` dans la CLI pour passer d’un fil d’agent actif à l’autre et examiner le fil en cours.
- Demandez directement à Codex d’orienter un sous-agent en cours d’exécution, de l’arrêter ou de fermer les fils des agents ayant terminé.

- Lorsque le panneau des agents en arrière-plan est disponible, développez-le pour consulter leur état,
arrêter les sous-agents actifs ou ouvrir le fil d’un sous-agent.
- Demandez directement à Codex d’orienter un sous-agent en cours d’exécution, de l’arrêter ou de fermer les fils
des sous-agents ayant terminé.

## Approbations et contrôles du bac à sable

Les sous-agents héritent de votre politique de bac à sable actuelle.

ChatGPT Work exécute les sous-agents dans son environnement hébergé et ne donne accès ni à un
bac à sable Codex local ni à un réglage du mode d’approbation. Les sous-agents utilisent les outils disponibles
dans la discussion parente. Les autorisations relatives aux sites web et aux connecteurs restent
propres à chaque outil.

Les sous-agents héritent du mode d’autorisation sélectionné sous la zone de saisie. Choisissez le
mode d’autorisation du tour parent avant de demander à Codex de déléguer le travail.

Dans les sessions CLI interactives, des demandes d’approbation peuvent provenir de fils d’agents
inactifs même lorsque vous consultez le fil principal. La fenêtre d’approbation
affiche le libellé du fil source ; vous pouvez appuyer sur `o` pour ouvrir ce fil avant
d’approuver ou de rejeter la demande, ou d’y répondre.

Dans les workflows non interactifs, ou lorsqu’une exécution ne peut pas présenter une nouvelle demande d’approbation,
toute action nécessitant une nouvelle approbation échoue et Codex transmet l’erreur au workflow
parent.

Codex réapplique également les modifications actives des paramètres d’exécution du tour parent lorsqu’il crée un
agent enfant. Cela inclut les choix de bac à sable et d’approbation définis de manière interactive pendant
la session, comme les modifications effectuées avec `/permissions` ou l’option `--yolo`, même si le fichier
d’agent personnalisé sélectionné définit d’autres valeurs par défaut.

Les sous-agents héritent du mode d’autorisation sélectionné sous la zone de saisie. Choisissez
le mode d’autorisation du tour parent avant de demander à Codex de déléguer le travail.

Vous pouvez également remplacer la configuration du bac à sable pour certains [agents personnalisés](#custom-agents), par exemple en indiquant explicitement qu’un agent doit fonctionner en lecture seule.

## Agents personnalisés

Codex inclut les agents intégrés suivants :

- `default` : agent de repli polyvalent.
- `worker` : agent axé sur l’exécution, pour l’implémentation et les correctifs.
- `explorer` : agent d’exploration du code source privilégiant la lecture.

Pour définir vos propres agents personnalisés, ajoutez des fichiers TOML autonomes dans
`~/.codex/agents/` pour les agents personnels ou dans `.codex/agents/` pour les agents propres au
projet.

Chaque fichier définit un agent personnalisé. Codex charge ces fichiers comme des couches de configuration
pour les sessions créées, ce qui permet aux agents personnalisés de remplacer les mêmes paramètres qu’une
configuration normale de session Codex. Cette approche peut sembler plus lourde qu’un manifeste
d’agent dédié, et le format peut évoluer à mesure que les fonctions de création et de partage gagnent en maturité.

Chaque fichier autonome d’agent personnalisé doit définir :

- `name`
- `description`
- `developer_instructions`

Si un fichier d’agent personnalisé définit `model` ou `model_reasoning_effort`, la valeur indiquée dans
ce fichier prévaut. Avant d’appliquer le fichier, Codex détermine chaque paramètre
à partir d’une valeur explicitement indiquée lors de la création, puis de la valeur par défaut correspondante de `[agents]`, puis
de la valeur de l’agent parent. Si une demande de création explicite ou une valeur par défaut de `[agents]`
sélectionne un modèle et qu’aucune des deux ne précise l’effort de raisonnement, Codex utilise
l’effort par défaut de ce modèle. Un fichier d’agent personnalisé qui définit uniquement `model`
conserve cet effort déterminé précédemment. Définissez également `model_reasoning_effort` dans le
fichier si le modèle sélectionné ne prend pas en charge cet effort ou si vous souhaitez en
utiliser un autre. Les autres paramètres de session, comme `sandbox_mode`, `mcp_servers`
et `skills.config`, sont hérités de l’agent parent lorsque le fichier d’agent personnalisé ne les
définit pas.

### Paramètres globaux

Les paramètres globaux des sous-agents se trouvent toujours dans la section `[agents]` de votre [configuration](/fr-FR/codex/config-file/config-basic#configuration-precedence).

| Champ                                       | Type    | Obligatoire | Objectif                                                             |
| ------------------------------------------- | ------- | :------: | ------------------------------------------------------------------- |
| `agents.enabled`                            | booléen |    Non    | Activez ou désactivez les outils multi-agents.                                |
| `agents.max_concurrent_threads_per_session` | nombre  |    Non    | Limitez le nombre de fils d’agents créés pouvant être ouverts simultanément, hors fil principal. |
| `agents.default_subagent_model`             | chaîne  |    Non    | Définissez le modèle par défaut des agents créés.                           |
| `agents.default_subagent_reasoning_effort`  | chaîne  |    Non    | Définissez l’effort de raisonnement par défaut des agents créés.                |
| `agents.interrupt_message`                  | booléen |    Non    | Consignez un message visible par le modèle lorsque le tour d’un agent est interrompu.   |

**Remarques :**

- La valeur par défaut de `agents.enabled` est `true`. Définissez ce paramètre sur `false` pour désactiver les outils multi-agents.
- Si vous ne définissez pas `agents.max_concurrent_threads_per_session`, Codex choisit la valeur par défaut. Les configurations existantes peuvent continuer à utiliser `agents.max_threads` comme alias historique.
- Les valeurs explicitement définies lors de la création remplacent `agents.default_subagent_model` et `agents.default_subagent_reasoning_effort`.
- La valeur par défaut de `agents.interrupt_message` est `true`. Définissez ce paramètre sur `false` pour omettre du contexte de l’agent le message d’interruption visible par le modèle.
- Si le nom d’un agent personnalisé correspond à celui d’un agent intégré tel que `explorer`, votre agent personnalisé prévaut.

### Schéma du fichier d’agent personnalisé

| Champ                    | Type   | Obligatoire | Objectif                                                         |
| ------------------------ | ------ | :------: | --------------------------------------------------------------- |
| `name`                   | chaîne |   Oui    | Nom que Codex utilise lorsqu’il crée cet agent ou y fait référence. |
| `description`            | chaîne |   Oui    | Indications destinées aux utilisateurs précisant dans quels cas Codex doit utiliser cet agent.     |
| `developer_instructions` | chaîne |   Oui    | Instructions principales qui définissent le comportement de l’agent.             |

Vous pouvez également inclure dans un fichier d’agent personnalisé d’autres clés de `config.toml` prises en charge, comme `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers` et `skills.config`.

Codex identifie l’agent personnalisé grâce à son champ `name`. La convention la plus simple consiste à donner au fichier
le même nom qu’à l’agent, mais c’est le champ `name` qui
fait foi.

### Exemples d’agents personnalisés

Les meilleurs agents personnalisés sont spécialisés et reposent sur des choix clairement définis. Attribuez à chacun une mission précise, un
ensemble d’outils adapté à cette mission et des instructions qui l’empêchent de
se disperser sur des tâches connexes.

#### Exemple 1 : revue de PR

Cette approche répartit la revue entre trois agents personnalisés spécialisés :

- `pr_explorer` cartographie le code source et rassemble des éléments probants.
- `reviewer` recherche les risques liés au bon fonctionnement, à la sécurité et aux tests.
- `docs_researcher` consulte la documentation du framework ou de l’API par l’intermédiaire d’un serveur MCP dédié.

Configuration du projet (`.codex/config.toml`) :

```toml
[agents]
max_concurrent_threads_per_session = 8

`.codex/agents/pr-explorer.toml` :

```toml
name = "pr_explorer"
description = "Read-only codebase explorer for gathering evidence before changes are proposed."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in exploration mode.
Trace the real execution path, cite files and symbols, and avoid proposing fixes unless the parent agent asks for them.
Prefer fast search and targeted file reads over broad scans.
"""

`.codex/agents/reviewer.toml` :

```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
Lead with concrete findings, include reproduction steps when possible, and avoid style-only comments unless they hide a real bug.
"""

`.codex/agents/docs-researcher.toml` :

```toml
name = "docs_researcher"
description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Use the docs MCP server to confirm APIs, options, and version-specific behavior.
Return concise answers with links or exact references when available.
Do not make code changes.
"""

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"

Cette configuration convient bien aux prompts tels que :

```text
Review this branch against main. Have pr_explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.

#### Exemple 2 : débogage de l’intégration frontend

Cette approche est utile en cas de régressions de l’interface utilisateur, de parcours de navigation instables ou de bugs d’intégration touchant à la fois le code de l’application et le produit en cours d’exécution.

Configuration du projet (`.codex/config.toml`) :

```toml
[agents]
max_concurrent_threads_per_session = 6

`.codex/agents/code-mapper.toml` :

```toml
name = "code_mapper"
description = "Read-only codebase explorer for locating the relevant frontend and backend code paths."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Map the code that owns the failing UI flow.
Identify entry points, state transitions, and likely files before the worker starts editing.
"""

`.codex/agents/browser-debugger.toml` :

```toml
name = "browser_debugger"
description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"
developer_instructions = """
Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
Use browser tooling for screenshots, console output, and network evidence.
Do not edit application code.
"""

[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
startup_timeout_sec = 20

`.codex/agents/ui-fixer.toml` :

```toml
name = "ui_fixer"
description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
developer_instructions = """
Own the fix once the issue is reproduced.
Make the smallest defensible change, keep unrelated files untouched, and validate only the behavior you changed.
"""

[[skills.config]]
path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
enabled = false

Cette configuration convient bien aux prompts tels que :

```text
Investigate why the settings modal fails to save. Have browser_debugger reproduce it, code_mapper trace the responsible code path, and ui_fixer implement the smallest fix once the failure mode is clear.
