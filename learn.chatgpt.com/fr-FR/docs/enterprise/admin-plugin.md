<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/admin-plugin -->

Ce guide vous aide à comprendre comment le plugin Admin facilite les tâches d’administration courantes, à préparer une tâche et à essayer des prompts pour les principaux cas d’utilisation, avec les approbations et le contexte nécessaires.

## 1. Découvrez à quoi sert le plugin Admin

Le plugin Admin est conçu pour vous aider à gérer les paramètres, les autorisations et les contrôles directement dans ChatGPT Work. Vous décrivez l’objectif en langage courant, et le plugin rassemble les informations nécessaires, consulte l’état actuel, explique ses observations et vous guide vers la prochaine étape prise en charge.

### Les objectifs du plugin Admin

- Transformer une demande d’administration en workflow clair sans que vous ayez à rédiger une requête API.
- Examiner l’état actuel de l’espace de travail avant de prendre une décision ou d’approuver une modification.
- Indiquer les sources et les champs autorisés sur lesquels repose la réponse, ainsi que les éléments que le plugin n’a pas pu vérifier.
- Marquer une pause pour permettre une révision avant une modification prise en charge, puis consulter à nouveau l’enregistrement pour confirmer le résultat.

En arrière-plan, le plugin utilise certaines API d’administration et des sources de données connectées approuvées. Il ne regroupe pas tous les systèmes d’administration, n’élargit pas vos autorisations et ne rend pas toutes les actions des API disponibles dans ChatGPT. Le système qui détient les données continue de contrôler ce que le plugin peut lire ou modifier.

### Les objectifs des API d’administration

Une API d’administration permet à un logiciel de demander des données ou une action prise en charge de manière structurée. Les organisations peuvent utiliser ces API pour créer des processus internes ou des outils externes. Les exemples courants comprennent les rapports planifiés, les opérations répétées sur de nombreux enregistrements et les connexions à des systèmes approuvés. Ces flux de travail nécessitent généralement une révision par les équipes d’ingénierie, de sécurité et de gouvernance.

Vous n’avez pas besoin de créer un workflow utilisant une API pour suivre ce guide. La suite du guide porte sur le plugin Admin. L’administration de l’espace de travail ChatGPT et celle de la Plateforme API restent également distinctes, chacune ayant ses propres autorisations et exigences d’authentification.

### Gardez vos informations d’authentification confidentielles

Utilisez uniquement les connexions et les systèmes de stockage des secrets approuvés par votre organisation. Ne collez jamais de véritable clé d’API d’administration dans ChatGPT, Codex, un document ou un fichier source.

## 2. Préparez-vous à utiliser le plugin Admin

Utilisez le plugin Admin pour une tâche ponctuelle prise en charge lorsque vous souhaitez traiter la demande en langage courant. Décrivez l’objectif et fournissez les identifiants stables ou le contexte de reporting approuvé. Le plugin présente ce qu’il a trouvé ou ce qu’il prévoit de modifier avant que vous décidiez de poursuivre ou non.

Le plugin utilise uniquement les sources, les informations d’authentification et les actions autorisées pour cette tâche. Il ne regroupe pas tous les systèmes d’administration et ne vous accorde pas d’autorisations plus étendues. Le système d’origine reste la source de référence.

### Avant de commencer

1. Repérez l’espace d’administration où se trouvent les enregistrements.
2. Rassemblez les informations nécessaires et obtenez l’approbation requise.
3. Commencez par une demande en lecture seule.
4. Demandez au plugin quelles sources et quels champs il a utilisés, et ce qu’il n’a pas pu vérifier.
5. Pour une modification prise en charge, examinez le plan avant de l’approuver. Demandez ensuite au plugin de consulter à nouveau l’enregistrement et de confirmer le résultat.

Vérifiez que le plugin est disponible dans votre espace de travail et que vous disposez des autorisations requises. Les cas d’utilisation ci-dessous concernant les rôles et les accès correspondent au périmètre actuellement documenté du plugin. Le plugin peut examiner les rôles, les autorisations d’accès aux fonctionnalités et les attributions aux utilisateurs ou aux groupes. Après votre confirmation, il peut également attribuer un rôle existant à un groupe existant.

Le plugin ne peut pas créer de rôles, modifier les autorisations d’un rôle ni confirmer l’accès à un connecteur spécifique.

Les cas d’utilisation liés à l’analyse nécessitent un accès à des sources de données connectées et approuvées. L’analyse du ROI nécessite aussi des résultats métier ou d’ingénierie approuvés ; les seuls relevés d’utilisation ne suffisent pas.

## 3. Explorez les principaux cas d’utilisation du plugin Admin

Choisissez un cas d’utilisation, remplacez chaque espace réservé par une valeur issue de votre demande approuvée et suivez les étapes dans l’ordre. Commencez par une demande en lecture seule, sauf si la tâche consiste en une modification prise en charge qui a déjà été approuvée.

### Listez les rôles de l’espace de travail

**Prompt à essayer**

```text
List the roles in workspace {workspace_id}. Separate built-in and custom roles. For each role, explain which features it can use and show the users or groups assigned to it. Don’t make changes.

**Étapes**

1. **Préparation :** Confirmez l’identifiant de l’espace de travail et vérifiez que vous êtes autorisé à consulter ces informations.
2. **Exécution :** Demandez la liste des rôles en lecture seule.
3. **Révision :** Vérifiez les types de rôles, les accès aux fonctionnalités et les attributions.
4. **Vérification :** Examinez tout élément inattendu sans effectuer de modification.

### Examinez un rôle

**Prompt à essayer**

```text
Review role {role_id}. Explain its permissions in plain language, show who has it, and flag anything that looks broader than expected. Don’t edit the role.

**Étapes**

1. **Préparation :** Confirmez l’identifiant du rôle et l’espace de travail.
2. **Exécution :** Demandez une révision du rôle en lecture seule.
3. **Révision :** Vérifiez que les autorisations et les attributions correspondent à la fonction prévue du rôle.
4. **Vérification :** Notez les questions à poser au responsable du rôle. N’oubliez pas que le plugin ne peut ni créer le rôle ni modifier ses autorisations.

### Comprenez les droits d’accès d’un utilisateur ou d’un groupe

**Prompt à essayer**

```text
Help me understand the access for user {user_id} or group {group_id}. Show their assigned roles, explain what access those roles provide, and point out overlaps or gaps. Clearly say what you can’t verify.

**Étapes**

1. **Préparation :** Utilisez l’identifiant stable de l’utilisateur ou du groupe.
2. **Exécution :** Demandez au plugin d’expliquer les droits d’accès.
3. **Révision :** Vérifiez les rôles attribués et les accès qu’ils accordent. Notez les éventuels chevauchements ou lacunes.
4. **Vérification :** Si le plugin ne peut pas consulter une information, indiquez qu’elle est inconnue plutôt que de faire des suppositions.

### Attribuez un rôle existant à un groupe

**Prompt à essayer**

```text
Before making a change, show the current roles for group {group_id} and explain what role {role_id} would add. Confirm the recorded approver and wait for my explicit approval. After the assignment, verify the group’s updated roles.

**Étapes**

1. **Préparation :** Confirmez les identifiants du groupe et du rôle. Vérifiez la demande approuvée et l’identité consignée de l’approbateur.
2. **Exécution :** Demandez au plugin de présenter les rôles actuels et ce qui changerait.
3. **Révision :** N’approuvez le plan que s’il correspond à la demande approuvée.
4. **Vérification :** Après l’attribution, vérifiez à nouveau le groupe pour confirmer que le rôle existant a été ajouté conformément à ce qui a été approuvé.

### Vérifiez l’autorisation générale pour les connecteurs

**Prompt à essayer**

```text
Check whether user {user_id} has general connector access through their assigned roles. Ask the plugin to show which permissions support its answer. If it can’t verify access to a specific connector, have it say so clearly.

**Étapes**

1. **Préparation :** Confirmez l’identifiant de l’utilisateur et vérifiez que vous êtes autorisé à examiner ses droits d’accès.
2. **Exécution :** Demandez la vérification de l’autorisation générale.
3. **Révision :** Vérifiez le rôle attribué et l’autorisation sur laquelle repose la réponse.
4. **Vérification :** Utilisez ce résultat uniquement pour une vérification générale. Il ne prouve pas l’accès à un connecteur donné ni à un élément connecté donné.

### Résolvez les problèmes liés à une modification approuvée

**Prompt à essayer**

```text
Review approved change {change_record_id}. Compare the requested result with the current workspace. If it failed, check the workspace and role first. Then confirm who owns the record, explain the issue, and suggest the safest next step.

**Étapes**

1. **Préparation :** Confirmez l’enregistrement correspondant à la modification approuvée et le résultat attendu.
2. **Exécution :** Demandez au plugin de comparer la demande à l’état actuel de l’espace de travail.
3. **Révision :** Vérifiez l’espace de travail et le rôle. Vérifiez ensuite le propriétaire de l’enregistrement.
4. **Vérification :** Prenez l’état actuel de l’espace de travail comme référence avant de choisir la prochaine étape.

### Optimisez les coûts et la combinaison de modèles utilisés

**Prompt à essayer**

```text
For {date_range} in workspace {workspace_id}, group verified token use and cost by use case. Compare models and reasoning modes using the speed and quality information available. Flag costly workflows when the data shows little evidence of value. Recommend where spending could be reduced or redirected toward work with stronger productivity or cost results. Include any approved revenue or quality signals. Estimate possible savings, explain tradeoffs, and separate verified observations from assumptions or missing inputs. Keep this read-only.

**Étapes**

1. **Préparation :** Confirmez l’espace de travail et la plage de dates, et assurez-vous que les données de coûts couvrent toute la période. Vérifiez quels champs approuvés relatifs aux performances ou aux résultats sont disponibles.
2. **Exécution :** Demandez la comparaison des coûts et des modèles.
3. **Révision :** Distinguez ce que montrent les données des hypothèses, des informations manquantes et des compromis.
4. **Vérification :** Vérifiez les économies possibles avec l’équipe Finance et les responsables des workflows avant d’agir.

### Explorez l’utilisation et l’adoption

**Prompt à essayer**

```text
Analyze workspace {workspace_id} during {date_range}. Show tasks and token use by team and business function. Group cost by use case. Summarize what teams use ChatGPT and Codex to accomplish. Include examples from Legal, Marketing, and Sales. Compare available use of skills and plugins. Only report tool calls, connected apps, and multi-tool workflows if those fields are available. Show where teams use more advanced workflows and where there may be room to expand. Rank the top {5_or_10} use cases and show whether a small group of highly active users accounts for most usage. Don’t guess about activity that is not in the data.

**Étapes**

1. **Préparation :** Vérifiez l’espace de travail, la plage de dates et les correspondances des équipes. Assurez-vous que les rapports par utilisateur sont approuvés.
2. **Exécution :** Demandez l’analyse de l’utilisation et de l’adoption.
3. **Révision :** Vérifiez quels champs demandés sont disponibles. Laissez de côté les activités pour lesquelles les données manquent plutôt que de faire des suppositions.
4. **Vérification :** Un volume d’utilisation élevé ne prouve ni un usage avancé, ni une valeur pour l’entreprise, ni les performances individuelles.

### Mesurez la valeur pour l’entreprise et le retour sur investissement

**Prompt à essayer**

```text
For workspace {workspace_id} in {date_range}, combine verified usage and cost with approved outcomes. Estimate value by team and use case. Include approved Sales measures for productivity, revenue, and quality. Compare teams and models, as well as workflows and user segments. Rank returns against cost. Show the sources and formula. Clearly state assumptions, limits, and missing inputs. Don’t claim ChatGPT caused the outcomes. Keep this read-only.

**Étapes**

1. **Préparation :** Vérifiez l’espace de travail et la plage de dates, puis confirmez les résultats approuvés. Examinez la formule et les règles de confidentialité.
2. **Exécution :** Demandez l’analyse du retour sur investissement.
3. **Révision :** Vérifiez chaque source et chaque hypothèse. Notez chaque limite ou information manquante.
4. **Vérification :** L’utilisation seule ne permet de démontrer ni un retour sur investissement ni un lien de causalité. Examinez le résultat avec l’équipe Finance et les responsables métier.

### Évaluez le retour sur investissement de Codex

**Prompt à essayer**

```text
For workspace {workspace_id}, combine verified Codex usage and cost from {date_range} with approved engineering outcomes. Estimate ROI by team, repository, and workflow. Compare productivity and delivery speed with code quality and engineering cost. Identify workflows that show high value or use many resources. Recommend changes to the model, reasoning mode, or workflow. Explain the tradeoffs and uncertainty. Present the findings as patterns in the available data, not proof that Codex caused the outcome. Return findings only; do not make changes.

**Étapes**

1. **Préparation :** Confirmez l’espace de travail et la période couverte par le rapport. Examinez les correspondances des équipes et des dépôts ainsi que les données de référence approuvées.
2. **Exécution :** Demandez l’analyse du retour sur investissement de Codex.
3. **Révision :** Distinguez les tendances observées des hypothèses. Protégez les données des utilisateurs et des dépôts.
4. **Vérification :** Examinez les recommandations et les valeurs de référence des résultats avec l’équipe Ingénierie.

## 4. Quand un workflow reposant sur une API peut être pertinent

Certaines organisations utilisent les API pour créer leurs propres processus d’administration ou des outils externes. Cette approche peut prendre en charge des tâches planifiées ou exécutées en continu. Elle peut aussi être utile lorsqu’un processus porte sur de nombreux enregistrements ou doit se connecter à un système interne approuvé. Elle est distincte de l’expérience guidée du plugin Admin.

Commencez par une tâche d’administration bien définie : identifiez les données d’entrée et les autorisations nécessaires, les étapes de révision, le résultat attendu et la manière dont il sera consigné. Si votre organisation automatise cette tâche, faites appel aux équipes d’ingénierie, de sécurité et de gouvernance concernées, conservez les identifiants dans un système de stockage des secrets approuvé et testez le workflow avant le déploiement.

### Ressources connexes

- [Référence de l’API d’administration de l’espace de travail ChatGPT](https://chatgpt.com/public/admin/api-reference)
- [Limites de l’administration](/fr-FR/codex/enterprise/roles-and-workspace-permissions#understand-the-control-boundaries)
- [Analytics API de l’espace de travail ChatGPT](/fr-FR/codex/enterprise/analytics-api)
- [API de conformité de l’espace de travail ChatGPT](/fr-FR/codex/enterprise/compliance-api)
