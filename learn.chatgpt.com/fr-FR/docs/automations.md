<!-- source: https://learn.chatgpt.com/fr-FR/docs/automations -->

Planifiez l’exécution en arrière-plan de tâches récurrentes. Dans ChatGPT sur le web et sur mobile,
les offres éligibles permettent aussi d’exécuter des tâches en réponse à des événements d’applications pris en charge. Consultez les tâches actives,
en pause et terminées, ainsi que les exécutions récentes, dans **Planifiées**. Vous pouvez associer
les tâches planifiées à des [Skills](/fr-FR/codex/build-skills) pour des travaux plus complexes.

Dans l’application de bureau ChatGPT, les tâches planifiées peuvent travailler sur des projets locaux et
s’exécuter dans le répertoire du projet ou dans un arbre de travail isolé. Laissez l’ordinateur allumé et
l’application en cours d’exécution lorsqu’une tâche planifiée a besoin de fichiers locaux.

Lorsque les tâches planifiées sont activées pour votre espace de travail, créez-les depuis Discussion ou
ChatGPT Work sur le web et gérez leurs exécutions dans **Planifiées**. Les tâches exécutées sur le web
peuvent utiliser le contexte importé et les outils connectés, mais elles ne peuvent pas travailler directement dans
un dossier de votre ordinateur.

Codex CLI ne propose pas l’interface de gestion « Planifiées ». Utilisez ChatGPT sur le web
ou l’application de bureau pour créer et gérer des tâches planifiées. La CLI peut vous aider à
préparer et tester au préalable un prompt, un Skill ou un script.

L’extension IDE ne propose pas l’interface de gestion « Planifiées ». Utilisez
ChatGPT sur le web ou l’application de bureau pour créer et gérer des tâches planifiées. L’extension IDE
peut vous aider à préparer et tester au préalable un prompt, un Skill ou une modification
de l’espace de travail.

<a id="managing-tasks"></a>
<a id="ask-codex-to-create-or-update-automations"></a>
<a id="ask-chatgpt-to-create-or-update-scheduled-tasks"></a>
<a id="thread-automations"></a>
<a id="scheduled-tasks-in-threads"></a>
<a id="scheduled-tasks-in-chats"></a>
<a id="schedule-work-from-a-task"></a>
<a id="schedule-a-task-inside-a-chat"></a>
<a id="test-automations"></a>
<a id="test-scheduled-tasks"></a>
<a id="worktree-cleanup-for-automations"></a>
<a id="worktree-cleanup-for-scheduled-tasks"></a>
<a id="permissions-and-security-model"></a>
<a id="examples"></a>
<a id="automatically-create-new-skills"></a>
<a id="stay-up-to-date-with-your-project"></a>
<a id="combining-automations-with-skills-to-fix-your-own-bugs"></a>
<a id="combining-scheduled-tasks-with-skills-to-fix-your-own-bugs"></a>

## Gérez les tâches planifiées sur le web

Ouvrez **Planifiées** pour consulter l’état des tâches et les exécutions récentes. Utilisez une tâche planifiée autonome
lorsque chaque exécution doit partir du prompt enregistré. Utilisez une tâche planifiée dans une
discussion si vous souhaitez que ChatGPT reprenne cette même discussion avec son
contexte existant.

Les tâches planifiées sur le web peuvent utiliser les fichiers importés, les outils connectés, les Skills et les
Plugins disponibles dans cette discussion. Elles ne gardent pas de dossier local ni
d’arbre de travail à disposition entre les exécutions. Placez les instructions à réutiliser dans le prompt de la tâche
ou dans un Skill joint, et conservez les sources nécessaires dans un projet accessible,
un fichier importé ou un service connecté.

Avant de planifier une tâche, testez son prompt dans une discussion classique sur le web.
Examinez les premières exécutions, puis ajustez le prompt, les outils ou la fréquence si les
résultats sont trop généraux ou nécessitent davantage de contexte.

## Déclenchez des tâches à partir d’événements d’applications

Avec les offres éligibles, les tâches planifiées peuvent s’exécuter lorsqu’un événement pris en charge survient dans Gmail, Slack ou
GitHub. Les tâches déclenchées par un événement sont disponibles dans ChatGPT sur le web
et sur mobile. Elles ne sont pas disponibles dans l’application de bureau ChatGPT, dans Codex CLI ni dans
l’extension IDE.

Demandez à ChatGPT de créer la tâche, puis décrivez l’événement à surveiller et ce
qu’il faut faire lorsqu’il se produit. Le déclencheur détermine quand la tâche s’exécute ; le prompt
enregistré détermine les actions effectuées à chaque exécution. Une tâche peut utiliser plusieurs déclencheurs d’événements,
mais elle ne peut pas les combiner avec une planification à horaires définis.

Les déclencheurs d’événements pris en charge incluent :

- **Gmail :** Nouveaux messages reçus, avec un filtrage facultatif par expéditeur ou par objet.
- **Slack :** Nouveaux messages dans les canaux sélectionnés, avec un filtrage facultatif par auteur
  et la possibilité d’inclure ou non les réponses dans les fils de discussion. Les réactions, les modifications, les suppressions et
  les messages directs ne sont pas pris en charge.
- **GitHub :** Activité des Pull requests dans un dépôt. Filtrez par pull request,
  auteur, titre ou étiquette, et choisissez si les revues, les commentaires, les mises à jour des commits
  ou uniquement les fusions doivent déclencher la tâche.

Connectez l’application et accordez-lui les autorisations nécessaires avant de créer la tâche. Pour Slack, ajoutez
`@ChatGPT` à chaque canal surveillé par la tâche. Pour GitHub, l’application connectée
doit avoir accès au dépôt.

Lorsque plusieurs événements correspondant aux critères surviennent à peu d’intervalle, ChatGPT peut les regrouper
dans une seule exécution. Ouvrez **Planifiées** pour consulter les événements en attente ou choisissez **Exécuter maintenant**
pour les traiter.

La disponibilité dépend de votre offre et des paramètres de votre espace de travail. Dans les espaces de travail
gérés, les administrateurs peuvent contrôler l’accès avec l’autorisation **Autoriser les tâches planifiées
déclenchées par des événements** .

Par exemple, planifiez une tâche pour analyser les erreurs de télémétrie et soumettre des correctifs,
ou pour créer des rapports sur les modifications récentes du code source. Pour un travail en cours qui
doit conserver le même contexte, [planifiez une tâche dans une discussion existante](#schedule-a-task-inside-a-chat).

Pour les tâches planifiées rattachées à un projet, laissez la machine allumée et l’application de bureau ChatGPT
en cours d’exécution. Le projet sélectionné doit toujours être disponible sur le disque au moment où
la tâche doit s’exécuter.

Dans les dépôts Git, vous pouvez choisir d’exécuter une tâche planifiée dans votre
projet local ou dans un nouvel [arbre de travail](/fr-FR/codex/environments/git-worktrees). Dans les deux cas, l’exécution se fait en
arrière-plan. Les arbres de travail isolent les modifications apportées par les tâches planifiées du travail local
non terminé, tandis qu’une exécution dans votre projet local peut modifier des fichiers sur lesquels vous
travaillez encore. Dans les projets sans gestion de versions, les tâches planifiées s’exécutent directement dans le
répertoire du projet.

Vous pouvez aussi conserver le modèle et le niveau d’effort de raisonnement par défaut, ou
les choisir explicitement pour mieux contrôler l’exécution de la tâche planifiée.

Si une tâche planifiée utilise `gpt-5.4` ou `gpt-5.4-mini` avec l’authentification ChatGPT,
mettez-la à jour avant le retrait de ces modèles le 31 août 2026. Remplacez `gpt-5.4` par
`gpt-5.6-terra` et `gpt-5.4-mini` par `gpt-5.6-luna`.

  

Les tâches planifiées s’exécutent sans supervision avec vos paramètres de bac à sable par défaut. Commencez par le niveau d’accès
le plus restreint permettant à la tâche de réussir, et n’accordez l’accès au réseau ou un accès plus étendu aux fichiers
que si nécessaire. [Découvrez le fonctionnement du bac à sable](/fr-FR/codex/sandboxing).

## Gérez les tâches planifiées

Retrouvez toutes les tâches planifiées et leurs exécutions sous **Planifiées** , dans la barre latérale
de l’application de bureau ChatGPT.

La vue **Planifiées** sert de boîte de réception. Les exécutions de tâches planifiées qui ont des résultats à signaler
y apparaissent, et un indicateur de contenu non lu signale qu’une exécution nécessite votre attention.

  

Les tâches planifiées autonomes démarrent une nouvelle discussion à chaque exécution planifiée et affichent les
résultats dans **Planifiées**. Utilisez-les lorsque chaque exécution doit être indépendante ou lorsqu’une même
tâche planifiée doit s’exécuter sur un ou plusieurs projets. Si vous avez besoin d’une fréquence
personnalisée, utilisez les options de planification personnalisée. Pour une planification avancée, modifiez sa
règle de récurrence RFC 5545 (RRULE), par exemple
`RRULE:FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0`.

Pour les dépôts Git, chaque tâche planifiée peut s’exécuter dans votre projet local ou
dans un [arbre de travail](/fr-FR/codex/environments/git-worktrees) dédié aux exécutions en arrière-plan. Utilisez les
arbres de travail pour isoler les modifications des tâches planifiées du travail local
non terminé. Utilisez le mode local pour que la tâche planifiée travaille directement dans votre copie de travail
principale, en gardant à l’esprit qu’elle peut modifier les fichiers que vous êtes en train d’éditer.
Dans les projets sans gestion de versions, les tâches planifiées s’exécutent directement dans le
répertoire du projet. Une même tâche planifiée peut s’exécuter sur plusieurs projets.

Les tâches planifiées créées avec ChatGPT Work sur le web, ou avec ChatGPT Work ou
Codex dans l’application de bureau, peuvent utiliser des Plugins. Elles peuvent aussi utiliser des Skills.
Pour faciliter la maintenance et le partage des tâches planifiées entre les équipes, utilisez des
[Skills](/fr-FR/codex/build-skills) pour définir l’action et fournir les outils et le contexte.
Sélectionnez ou invoquez un Skill précis dans le prompt de la tâche lorsque le workflow ne doit pas
dépendre de la sélection automatique des outils.

## Demandez à ChatGPT de créer ou de mettre à jour des tâches planifiées

Vous pouvez créer et mettre à jour des tâches planifiées depuis une discussion ChatGPT ou Codex.
Décrivez le travail à effectuer, indiquez quand l’exécuter et précisez si chaque exécution doit revenir dans la
discussion actuelle ou en démarrer une nouvelle. ChatGPT peut rédiger le prompt, choisir la
bonne destination et mettre à jour la tâche lorsque son périmètre ou sa fréquence
change.

Par exemple, demandez à ChatGPT de planifier un suivi depuis la discussion actuelle en attendant la fin d’un
déploiement, ou de créer une tâche planifiée autonome qui vérifie
régulièrement un projet.

Les Skills peuvent aussi créer ou mettre à jour des tâches planifiées. Par exemple, un Skill chargé de
surveiller une pull request pourrait configurer une tâche planifiée qui vérifie le
statut de la PR avec le Plugin GitHub et apporte des corrections en fonction des nouveaux retours de revue.

## Planifiez une tâche dans une discussion

Planifiez une tâche dans une discussion existante si vous souhaitez que ChatGPT y revienne
aux moments prévus. La tâche planifiée utilise le contexte existant de la discussion au lieu de
repartir d’un nouveau prompt à chaque fois.

Les tâches planifiées dans une discussion peuvent utiliser des intervalles exprimés en minutes pour les boucles de suivi
actives, ou s’exécuter selon un calendrier quotidien ou hebdomadaire si vous avez besoin de faire le point à une heure
précise.

Planifiez une tâche dans une discussion pour :

- suivre une opération de longue durée jusqu’à son achèvement
- consulter une source connectée à intervalles réguliers lorsque vous avez besoin d’un état des lieux
périodique plutôt que d’une réponse à un événement d’application pris en charge
- rappeler à ChatGPT de poursuivre une boucle de revue à fréquence fixe
- exécuter un workflow piloté par un Skill et utilisant des Plugins, par exemple pour vérifier le statut d’une PR
et traiter les nouveaux retours
- poursuivre une discussion de recherche ou de triage en cours sans perdre son contexte

Utilisez une tâche planifiée autonome lorsque chaque exécution doit être indépendante ou lorsque
les résultats doivent apparaître sous forme d’exécutions distinctes dans **Planifiées**.

Lorsque vous planifiez une tâche dans une discussion, rédigez un prompt qui reste valable d’une exécution à l’autre. Il doit décrire
ce que ChatGPT doit faire à chaque exécution planifiée, comment déterminer s’il y a
un élément important à signaler, et quand s’arrêter ou vous solliciter.

## Testez les tâches planifiées

Avant de planifier une tâche, testez d’abord son prompt manuellement dans une discussion
classique. Vous pourrez ainsi vérifier les points suivants :

- Le prompt est clair et son périmètre est correctement défini.
- Le modèle, le niveau d’effort de raisonnement et les outils, qu’ils soient sélectionnés ou utilisés par défaut, se comportent comme prévu.
- Le résultat obtenu peut être examiné.

Lorsque vous commencez à planifier des exécutions, examinez les premiers résultats et ajustez le
prompt ou la fréquence selon les besoins.

Dans l’application de bureau ChatGPT, vous pouvez déclencher explicitement un Skill dans le prompt d’une tâche
planifiée en utilisant `$skill-name`.

## Nettoyage des arbres de travail associés aux tâches planifiées

Si vous choisissez des arbres de travail pour les dépôts Git, une fréquence d’exécution élevée peut créer
un grand nombre d’arbres de travail au fil du temps. Archivez les exécutions planifiées dont vous n’avez plus besoin et évitez
d’épingler des exécutions, sauf si vous souhaitez conserver leurs arbres de travail.

## Autorisations et modèle de sécurité

Les tâches planifiées s’exécutent sans supervision et utilisent vos paramètres de bac à sable par défaut.

Pour une explication simple de ces limites, consultez la
[vue d’ensemble du bac à sable](/fr-FR/codex/sandboxing). Pour connaître les règles relatives au système de fichiers et au réseau,
consultez [Autorisations](/fr-FR/codex/permissions).

- Si votre bac à sable est **en lecture seule**, les appels d’outils échouent s’ils nécessitent
  de modifier des fichiers, d’accéder au réseau ou d’utiliser des applications sur votre ordinateur.
  Envisagez de modifier les paramètres du bac à sable pour passer au mode Écriture dans l’espace de travail.
- Si votre bac à sable est en mode **workspace-write**, les appels d’outils échouent s’ils nécessitent
  de modifier des fichiers hors de l’espace de travail, d’accéder au réseau ou d’utiliser des applications
  sur votre ordinateur. Vous pouvez autoriser certaines commandes à s’exécuter hors du
  bac à sable à l’aide de [règles](/fr-FR/codex/agent-configuration/rules).
- Si votre bac à sable est en mode **accès complet**, les tâches planifiées en arrière-plan présentent
  un risque élevé, car ChatGPT peut modifier des fichiers, exécuter des commandes et accéder au réseau
  sans demander votre approbation. Envisagez de modifier les paramètres du bac à sable pour passer au mode Écriture dans l’espace de travail et
  d’utiliser des [règles](/fr-FR/codex/agent-configuration/rules) pour définir quelles commandes l’agent
  peut exécuter avec un accès complet.

Dans un environnement géré, les administrateurs peuvent imposer des exigences
pour limiter ces comportements. Par exemple, ils peuvent interdire `approval_policy =
"never"` ou restreindre les modes de bac à sable autorisés. Consultez
[Exigences imposées par les administrateurs (`requirements.toml`)](/fr-FR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

Les tâches planifiées utilisent `approval_policy = "never"` lorsque la politique de votre organisation
le permet. Si les exigences des administrateurs interdisent `approval_policy = "never"`,
les tâches planifiées adoptent alors le comportement d’approbation du mode d’autorisation
que vous avez sélectionné.

## Exemples

### Créez automatiquement de nouveaux Skills

```markdown
Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.

If there’s anything we’ve been doing often and struggle with that we should save as a skill to speed up future work, let’s do it.

Definitely don't feel like you need to update any- only if there's a good reason!

Let me know if you make any.

### Suivez l’évolution de votre projet

```markdown
Look at the latest remote origin/master or origin/main . Then produce an exec briefing for the last 24 hours of commits that touch 

Formatting + structure:

- Use rich Markdown (H1 workstream sections, italics for the subtitle, horizontal rules as needed).
- Preamble can read something like “Here’s the last 24h brief for <directory>:”
- Subtitle should read: “Narrative walkthrough with owners; grouped by workstream.”
- Group by workstream rather than listing each commit. Workstream titles should be H1.
- Write a short narrative per workstream that explains the changes in plain language.
- Use bullet points and bolding when it makes things more readable
- Feel free to make bullets per person, but bold their name

Content requirements:

- Include PR links inline (e.g., [#123](...)) without a “PRs:” label.
- Do NOT include commit hashes or a “Key commits” section.
- It’s fine if multiple PRs appear under one workstream, but avoid per‑commit bullet lists.

Scope rules:

- Only include changes within the current cwd (or main checkout equivalent)
- Only include the last 24h of commits.
- Use `gh` to fetch PR titles and descriptions if it helps.
  Also feel free to pull PR reviews and comments

### Combinez les tâches planifiées et les Skills pour corriger vos propres bugs

Créez un nouveau Skill `$recent-code-bugfix` qui tente de corriger un bug introduit par vos propres commits, puis [enregistrez-le dans vos Skills personnels](/fr-FR/codex/build-skills#where-to-save-skills).

```markdown
---
name: recent-code-bugfix
description: Find and fix a bug introduced by the current author within the last week in the current working directory. Use when a user wants a proactive bugfix from their recent changes, when the prompt is empty, or when asked to triage/fix issues caused by their recent commits. Root cause must map directly to the author’s own changes.
---

# Recent Code Bugfix

## Overview

Find a bug introduced by the current author in the last week, implement a fix, and verify it when possible. Operate in the current working directory, assume the code is local, and ensure the root cause is tied directly to the author’s own edits.

## Workflow

### 1) Establish the recent-change scope

Use Git to identify the author and changed files from the last week.

- Determine the author from `git config user.name`/`user.email`. If unavailable, use the current user’s name from the environment or ask once.
- Use `git log --since=1.week --author=<author>` to list recent commits and files. Focus on files touched by those commits.
- If the user’s prompt is empty, proceed directly with this default scope.

### 2) Find a concrete failure tied to recent changes

Prioritize defects that are directly attributable to the author’s edits.

- Look for recent failures (tests, lint, runtime errors) if logs or CI outputs are available locally.
- If no failures are provided, run the smallest relevant verification (single test, file-level lint, or targeted repro) that touches the edited files.
- Confirm the root cause is directly connected to the author’s changes, not unrelated legacy issues. If only unrelated failures are found, stop and report that no qualifying bug was detected.

### 3) Implement the fix

Make a minimal fix that aligns with project conventions.

- Update only the files needed to resolve the issue.
- Avoid adding extra defensive checks or unrelated refactors.
- Keep changes consistent with local style and tests.

### 4) Verify

Attempt verification when possible.

- Prefer the smallest validation step (targeted test, focused lint, or direct repro command).
- If verification cannot be run, state what would be run and why it wasn’t executed.

### 5) Report

Summarize the root cause, the fix, and the verification performed. Make it explicit how the root cause ties to the author’s recent changes.

Ensuite, créez une nouvelle tâche planifiée :

```markdown
Check my commits from the last 24h and submit a $recent-code-bugfix.
