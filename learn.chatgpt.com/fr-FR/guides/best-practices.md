<!-- source: https://learn.chatgpt.com/fr-FR/guides/best-practices -->

Si vous découvrez Codex ou les agents de programmation en général, ce guide vous aidera à obtenir plus rapidement de meilleurs résultats. Il présente les habitudes essentielles qui rendent Codex plus efficace dans [la CLI](/fr-FR/codex/cli), [l’extension IDE](/fr-FR/codex/ide) et [l’application de bureau ChatGPT](/fr-FR/codex/app), de la conception de prompts et de la planification à la validation, en passant par MCP, les Skills et les tâches planifiées.

Codex donne de meilleurs résultats si vous le considérez moins comme un assistant ponctuel que comme un coéquipier que vous configurez et améliorez au fil du temps.

Une approche utile consiste à commencer par fournir le contexte adapté à la tâche, à utiliser `AGENTS.md` pour consigner des instructions durables, à configurer Codex en fonction de votre workflow, à connecter les systèmes externes avec MCP, à transformer les tâches répétitives en Skills et à automatiser les workflows stables.

## Pour bien commencer : contexte et prompts

Codex est déjà suffisamment performant pour être utile même si votre prompt n’est pas parfait. Vous pouvez souvent lui confier un problème difficile avec une configuration minimale et tout de même obtenir un très bon résultat. Une [conception de prompts](/fr-FR/codex/prompting) claire n’est pas indispensable pour en tirer parti, mais elle rend les résultats plus fiables, en particulier dans les bases de code volumineuses ou pour les tâches à forts enjeux.

Si vous travaillez dans un dépôt volumineux ou complexe, le principal levier consiste à fournir à Codex le contexte adapté à la tâche et une description clairement structurée du travail attendu.

En règle générale, incluez quatre éléments dans votre prompt :

- **Objectif :** Que cherchez-vous à modifier ou à créer ?
- **Contexte :** Quels fichiers, dossiers, documents, exemples ou messages d’erreur sont pertinents pour cette tâche ? Vous pouvez utiliser @ pour mentionner certains fichiers et les ajouter au contexte.
- **Contraintes :** Quelles normes, conventions et exigences en matière d’architecture ou de sécurité Codex doit-il respecter ?
- **Critères d’achèvement :** Quelles conditions doivent être remplies avant que la tâche soit considérée comme terminée, par exemple la réussite des tests, la modification du comportement ou l’impossibilité de reproduire le bug ?

Cela aide Codex à rester dans le périmètre, à faire moins d’hypothèses et à produire un travail plus facile à passer en revue.

Choisissez un niveau de raisonnement adapté à la difficulté de la tâche et testez ce qui convient le mieux à votre workflow. Les réglages optimaux varient selon les utilisateurs et les tâches.

- Faible pour les tâches rapides et bien délimitées
- Médium ou Élevé pour les modifications plus complexes ou le débogage
- Très élevé pour les tâches agentiques longues qui exigent beaucoup de raisonnement

  Pour fournir plus rapidement le contexte, essayez d’utiliser la dictée vocale dans l’application de bureau ChatGPT
pour dicter vos instructions à Codex plutôt que de les saisir au clavier.

## Planifiez d’abord les tâches difficiles

Si la tâche est complexe, ambiguë ou difficile à décrire précisément, demandez à Codex d’établir un plan avant de commencer à coder.

Plusieurs approches sont efficaces :

**Utilisez le mode plan :** Pour la plupart des utilisateurs, il s’agit de l’option la plus simple et la plus efficace. Le mode plan permet à Codex de recueillir le contexte nécessaire, de poser des questions de clarification et d’établir un plan plus solide avant l’implémentation. Activez-le avec `/plan` ou <kbd>Maj</kbd>+<kbd>Tab</kbd>.

**Demandez à Codex de vous interroger :** Si vous avez une idée générale de ce que vous voulez, mais ne savez pas exactement comment l’exprimer, demandez d’abord à Codex de vous poser des questions. Dites-lui de remettre en question vos hypothèses et de transformer cette idée encore floue en projet concret avant d’écrire du code.

**Utilisez un modèle PLANS.md :** Pour les workflows plus avancés, vous pouvez configurer Codex afin qu’il suive un modèle `PLANS.md` ou de plan d’exécution pour les tâches de longue durée ou à plusieurs étapes. Pour en savoir plus, consultez le [guide des plans d’exécution](/cookbook/articles/codex_exec_plans).

## Rendez les consignes réutilisables avec `AGENTS.md`

Lorsqu’une structure de prompt donne de bons résultats, l’étape suivante consiste à ne plus la reproduire manuellement. C’est là qu’intervient [AGENTS.md](/fr-FR/codex/agent-configuration/agents-md).

Considérez `AGENTS.md` comme un README au format libre destiné aux agents. Il est automatiquement chargé dans le contexte et constitue le meilleur endroit pour définir la manière dont vous et votre équipe souhaitez que Codex travaille dans un dépôt.

Un bon fichier `AGENTS.md` couvre les points suivants :

- la structure du dépôt et les répertoires importants
- Comment exécuter le projet
- Les commandes de build, de test et de lint
- Les conventions d’ingénierie et les attentes relatives aux PRs
- Les contraintes et les interdictions
- Les critères d’achèvement et la procédure de vérification du travail

La commande slash `/init` de la CLI permet de générer rapidement un fichier `AGENTS.md` initial dans le répertoire actuel. C’est un excellent point de départ, mais modifiez le résultat pour l’adapter aux pratiques réelles de votre équipe en matière de build, de tests, de revues de code et de livraison du code.

Vous pouvez créer des fichiers `AGENTS.md` à différents niveaux : un fichier `AGENTS.md` global, situé dans `~/.codex`, pour vos paramètres personnels par défaut ; un fichier au niveau du dépôt pour les normes communes ; et des fichiers plus spécifiques dans les sous-répertoires pour les règles locales. Si un fichier plus spécifique se trouve plus près de votre répertoire actuel, ses consignes prévalent.

Restez pragmatique. Un fichier `AGENTS.md` court et précis est plus utile qu’un long fichier rempli de règles vagues. Commencez par l’essentiel, puis n’ajoutez de nouvelles règles qu’après avoir constaté des erreurs récurrentes.

Si `AGENTS.md` devient trop volumineux, gardez le fichier principal concis et faites référence à des fichiers Markdown propres à chaque type de tâche, par exemple pour la planification, la revue de code ou l’architecture.

  Lorsque Codex commet deux fois la même erreur, demandez-lui d’effectuer une rétrospective et mettez à jour
`AGENTS.md`. Les consignes restent ainsi pragmatiques et fondées sur des difficultés réelles.

## Configurez Codex pour plus de cohérence

La configuration est l’un des principaux moyens de rendre le comportement de Codex plus cohérent entre les sessions et dans les différentes interfaces. Vous pouvez, par exemple, définir les valeurs par défaut pour le choix du modèle, l’effort de raisonnement, le mode bac à sable, la politique d’approbation, les profils et la configuration MCP.

Pour commencer, vous pouvez procéder ainsi :

- Conservez vos paramètres personnels par défaut dans `~/.codex/config.toml` (**Paramètres \> Configuration \> Ouvrir config.toml** dans l’application de bureau ChatGPT)
- Conservez la configuration propre au dépôt dans `.codex/config.toml`
- Utilisez les surcharges en ligne de commande uniquement pour les situations ponctuelles (si vous utilisez la CLI)

[`config.toml`](/fr-FR/codex/config-file/config-basic) vous permet de définir des préférences durables, comme les serveurs MCP, la configuration multi-agent et les indicateurs de fonctionnalités. Les surcharges propres à chaque profil sont placées dans des fichiers `$CODEX_HOME/profile-name.config.toml` distincts.

Codex intègre un bac à sable au niveau du système d’exploitation et propose deux réglages clés. Le mode d’approbation détermine quand Codex vous demande l’autorisation d’exécuter une commande, tandis que le mode bac à sable détermine si Codex peut lire ou écrire dans le répertoire et à quels fichiers l’agent peut accéder.

Si vous découvrez les agents de programmation, commencez par les autorisations par défaut. Conservez par défaut des paramètres d’approbation et de bac à sable stricts, puis n’assouplissez les autorisations que pour les dépôts de confiance ou certains workflows, une fois le besoin clairement établi.

Notez que la CLI, l’extension IDE et l’application de bureau ChatGPT partagent toutes les mêmes couches de configuration. Pour en savoir plus, consultez la page [Exemple de configuration](/fr-FR/codex/config-file/config-sample).

  Configurez Codex dès le début en fonction de votre environnement réel. De nombreux problèmes de qualité sont
en réalité des problèmes de configuration, comme un mauvais répertoire de travail, l’absence d’accès en écriture,
un modèle par défaut inadéquat ou des outils et connecteurs manquants.

## Améliorez la fiabilité grâce aux tests et à la revue de code

Ne vous contentez pas de demander à Codex d’effectuer une modification. Demandez-lui aussi de créer des tests si nécessaire, d’exécuter les contrôles pertinents, de confirmer le résultat et de passer le travail en revue avant de l’accepter.

Codex peut effectuer cette boucle pour vous, mais seulement s’il sait à quoi ressemble un bon résultat. Ces consignes peuvent provenir du prompt ou de `AGENTS.md`.

Cela peut inclure :

- Écrire ou mettre à jour les tests correspondant à la modification
- Exécuter les suites de tests appropriées
- Effectuer les contrôles de lint, de formatage ou de types
- Confirmer que le comportement final correspond à la demande
- Examiner le diff pour détecter les bugs, les régressions ou les pratiques à risque

  Basculez l’affichage du panneau de diff dans l’application de bureau ChatGPT pour [examiner directement
  les modifications](/fr-FR/codex/code-review?surface=app) en local. Cliquez sur une ligne précise pour
  fournir un commentaire qui sera ajouté au contexte de l’échange suivant avec Codex.

Une option utile ici est la commande slash `/review`, qui permet d’effectuer une revue de code de plusieurs façons :

- Revue par rapport à une branche de base, comme pour une PR
- Revue des modifications non validées
- Révisez un commit
- Utilisez des instructions de revue personnalisées

Si votre équipe et vous utilisez un fichier `code_review.md` référencé depuis `AGENTS.md`, Codex peut également suivre ces consignes pendant la revue. C’est une méthode efficace pour les équipes qui souhaitent conserver des pratiques de revue cohérentes d’un dépôt et d’un contributeur à l’autre.

Codex ne devrait pas se contenter de générer du code. Avec les bonnes instructions, il peut aussi vous aider à **le tester, le vérifier et en faire la revue**.

Si vous utilisez GitHub Cloud, vous pouvez configurer Codex pour qu’il effectue des [revues de code pour vos PRs](/fr-FR/codex/third-party/github). Chez OpenAI, Codex passe en revue 100 % des PRs. Vous pouvez activer les revues automatiques ou faire en sorte que Codex lance une revue lorsque vous mentionnez @Codex.

## Utilisez le protocole MCP pour le contexte externe

Utilisez le protocole MCP lorsque le contexte dont Codex a besoin se trouve en dehors du dépôt. Il permet à Codex de se connecter aux outils et systèmes que vous utilisez déjà, ce qui vous évite de copier-coller constamment des informations à jour dans les prompts.

Le [Model Context Protocol](/fr-FR/codex/extend/mcp), ou MCP, est une norme ouverte permettant de connecter Codex à des outils et systèmes externes.

Utilisez le protocole MCP dans les cas suivants :

- Le contexte requis se trouve en dehors du dépôt
- Les données changent fréquemment
- Vous souhaitez que Codex utilise un outil plutôt que de s’appuyer sur des instructions copiées-collées
- Vous avez besoin d’une intégration reproductible pour plusieurs utilisateurs ou projets

Codex prend en charge les serveurs STDIO et Streamable HTTP avec OAuth.

Dans l’application de bureau ChatGPT, accédez à **Paramètres \> Serveurs MCP** pour afficher les serveurs personnalisés et recommandés. Codex peut souvent vous aider à installer les serveurs nécessaires : il suffit de le lui demander. Vous pouvez aussi utiliser la commande `codex mcp add` dans la CLI pour ajouter vos serveurs personnalisés avec un nom, une URL et d’autres informations.

  N’ajoutez des outils que s’ils permettent de mettre en place un workflow concret. Ne commencez pas par connecter
tous les outils que vous utilisez. Commencez par un ou deux outils qui éliminent clairement une étape
manuelle que vous effectuez déjà souvent, puis développez l’intégration.

## Créez des skills pour les tâches répétitives

Lorsqu’un workflow devient reproductible, cessez de vous appuyer sur de longs prompts ou des échanges répétés. Utilisez un [skill](/fr-FR/codex/build-skills) pour regrouper dans un fichier `SKILL.md` les instructions, le contexte et la logique complémentaire que Codex doit appliquer de manière cohérente. Les Skills fonctionnent dans la CLI, l’extension IDE et l’application de bureau ChatGPT.

Consacrez chaque skill à une seule tâche. Commencez par 2 ou 3 cas d’utilisation concrets, définissez clairement les entrées et les sorties, puis rédigez une description qui précise ce que fait le skill et quand l’utiliser. Ajoutez des exemples de formulations qu’un utilisateur emploierait réellement pour le déclencher.

N’essayez pas de prévoir tous les cas limites dès le départ. Commencez par une tâche représentative, faites en sorte qu’elle fonctionne correctement, puis transformez ce workflow en skill et améliorez-le progressivement. N’ajoutez des scripts ou des ressources supplémentaires que s’ils améliorent la fiabilité.

Règle pratique : si vous réutilisez régulièrement le même prompt ou corrigez sans cesse le même workflow, il est sans doute temps d’en faire un skill.

Les Skills sont particulièrement utiles pour les tâches récurrentes telles que :

- Triage des logs
- Rédaction de notes de version
- Revue de PR selon une liste de contrôle
- Planification des migrations
- Synthèses de télémétrie ou d’incidents
- Workflows standard de débogage

Le skill `$skill-creator` est le meilleur point de départ pour générer la structure de la première version d’un skill. Conservez cette première version en local pendant vos itérations. Lorsqu’elle est prête à être diffusée plus largement, distribuez-la sous la forme d’un [plugin](https://developers.openai.com/plugins/build/plugins). La description est l’un des éléments les plus importants d’un skill. Elle doit indiquer ce que fait le skill et quand l’utiliser.

  Les skills personnels sont stockés dans `$HOME/.agents/skills`, et les skills partagés au sein de l’équipe
  peuvent être versionnés dans `.agents/skills` au sein d’un dépôt. Cette organisation est particulièrement
  utile pour l’intégration de nouveaux membres dans l’équipe.

## Utilisez les tâches planifiées pour les opérations récurrentes

Une fois un workflow stabilisé, vous pouvez planifier son exécution en arrière-plan avec Codex. Dans l’application de bureau ChatGPT, les [tâches planifiées](/fr-FR/codex/automations) vous permettent de choisir le projet, le prompt, la fréquence et l’environnement d’exécution des tâches récurrentes.

Créez une tâche planifiée depuis la page **Planifiées**. Choisissez le projet, le prompt,
la fréquence et indiquez si la tâche doit s’exécuter dans un arbre de travail Git dédié ou dans votre environnement
local. Le prompt peut invoquer des skills. En savoir plus sur les
[arbres de travail Git](/fr-FR/codex/environments/git-worktrees).

Les tâches suivantes s’y prêtent bien :

- Résumé des commits récents
- Détection de bugs potentiels
- Rédaction de notes de version
- Vérification des échecs de CI
- Production de synthèses de stand-up
- Exécution planifiée de workflows d’analyse reproductibles

Une règle utile consiste à confier la méthode aux skills et le calendrier d’exécution aux tâches planifiées. Si un workflow nécessite encore beaucoup d’interventions, transformez-le d’abord en skill. Une fois qu’il est prévisible, sa planification peut vous faire gagner du temps.

  Utilisez les tâches planifiées pour faire le point et assurer la maintenance, pas seulement pour exécuter des tâches. Passez en revue
les discussions récentes, synthétisez les points de friction récurrents et améliorez progressivement les prompts, les instructions
ou la configuration du workflow.

<a id="organize-long-running-tasks"></a>

## Organisez les discussions au long cours

Au fil du temps, les discussions accumulent du contexte, des décisions et des actions. Bien les gérer a donc une incidence majeure sur la qualité.

L’application de bureau ChatGPT vous permet d’épingler des discussions et de créer des arbres de travail. Si vous utilisez la
CLI, les [commandes slash](/codex/developer-commands?surface=cli) suivantes sont particulièrement utiles :

- `/experimental` pour activer ou désactiver les fonctionnalités expérimentales et les ajouter à votre `config.toml`
- `/resume` pour reprendre une discussion enregistrée
- `/fork` pour créer une discussion tout en conservant la transcription d’origine
- `/compact` lorsque la discussion s’allonge et que vous souhaitez obtenir une synthèse du contexte précédent. Codex compacte aussi automatiquement les discussions
- `/agent` lorsque vous exécutez des agents en parallèle et souhaitez passer d’un fil d’agent actif à un autre
- `/theme` pour choisir un thème de coloration syntaxique
- `/apps` pour utiliser les applications ChatGPT directement dans Codex
- `/status` pour consulter l’état de la session en cours

Gardez une discussion par unité de travail cohérente. Si le travail concerne toujours le même
problème, mieux vaut souvent rester dans la même discussion, car cela préserve le fil du
raisonnement. Ne forkez que lorsque le travail se ramifie réellement.

  Utilisez les workflows de Codex basés sur des [sous-agents](/fr-FR/codex/agent-configuration/subagents) pour
  décharger le fil principal des tâches bien délimitées. Gardez l’agent principal concentré sur le
  problème central et confiez aux sous-agents l’exploration, les tests ou le triage.

## Erreurs courantes

Voici quelques erreurs courantes à éviter lors de vos premières utilisations de Codex :

- Surcharger le prompt de règles pérennes au lieu de les placer dans `AGENTS.md` ou dans un skill
- Priver l’agent de visibilité sur son travail en n’indiquant pas précisément comment exécuter au mieux les commandes de build et de test
- Se passer de planification pour les tâches complexes en plusieurs étapes
- Accorder à Codex un accès complet à votre ordinateur avant d’avoir compris le workflow
- Exécuter plusieurs tâches en parallèle sur les mêmes fichiers sans utiliser d’arbres de travail Git
- Planifier une tâche récurrente avant que son exécution manuelle soit fiable
- Considérer Codex comme un outil qu’il faut surveiller étape par étape, au lieu de l’utiliser en parallèle de votre propre travail
- Utiliser une seule discussion pour un projet entier, au lieu d’une discussion par résultat cohérent. Au fil du temps, le contexte devient trop volumineux et les résultats se dégradent
