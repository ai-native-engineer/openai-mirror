<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/workspace-model-availability -->

Les modèles accessibles à un utilisateur dépendent de l’interface du produit et de son
mode de connexion. Un paramètre de modèle de votre espace de travail ChatGPT ne s’applique pas automatiquement
à Codex dans l’application de bureau ChatGPT, à Codex CLI, à l’extension IDE,
à Codex Cloud ni à l’API OpenAI.

Pour une présentation complète du modèle d’administration, consultez
[Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions).

## Identifiez le périmètre d’accès aux modèles

| Périmètre du produit ou de l’authentification                                                         | L’accès aux modèles dépend de                                                                                  | Source à jour                                                                                                                |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Espace de travail ChatGPT                                                                          | L’offre de l’espace de travail, les droits d’accès des membres, les paramètres de l’espace de travail et les autorisations prises en charge pour les rôles                 | [Modèles et limites de ChatGPT Enterprise et ChatGPT Edu](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits) |
| Codex dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE avec connexion via ChatGPT        | Les modèles pris en charge par le client concerné et les droits d’accès associés à l’identité ChatGPT connectée    | [Modèles Codex](/fr-FR/codex/models) et recommandations en vigueur pour l’espace de travail                                                                  |
| Codex Cloud                                                                                | Les modèles pris en charge par les workflows Codex hébergés et les droits d’accès associés à l’identité ChatGPT connectée | [Modèles Codex](/fr-FR/codex/models) et [Codex Cloud](/fr-FR/codex/cloud)                                                                 |
| Codex dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE avec authentification par clé API | L’organisation et le projet de l’API OpenAI associés à la clé                                       | [Authentification](/fr-FR/codex/auth) et la [Plateforme API](https://platform.openai.com/docs/overview)                        |

Consultez la source à jour correspondant à l’interface réellement utilisée par l’utilisateur. Ne recopiez pas
un catalogue de modèles et ne supposez pas qu’un paramètre du sélecteur de modèles ChatGPT produit le même
effet pour Codex dans l’application de bureau ChatGPT, Codex CLI, l’extension IDE,
Codex Cloud et la Plateforme API.

## Définissez une expérience de démarrage claire pour les employés

Examinez les [paramètres des modèles](https://help.openai.com/en/articles/8411955) de votre
espace de travail avant d’inviter un groupe pilote. Les propriétaires et les administrateurs de l’espace de travail peuvent
configurer des paramètres de démarrage par défaut distincts pour Discussion, d’une part, et pour Work et Codex, d’autre part. Lorsque ces options sont
prises en charge, choisissez le modèle initial, le niveau de raisonnement, la vitesse et le comportement à l’ouverture de nouvelles
discussions pour Discussion, Work et les interfaces locales de Codex.

Considérez ces choix comme des paramètres par défaut, et non comme des autorisations. Les modèles disponibles
dépendent toujours de la licence attribuée au membre, de son rôle, de son identité liée à l’espace de travail ou à l’API,
des exigences imposées par l’espace de travail et de l’interface qu’il utilise. Les paramètres de démarrage par défaut
ne donnent pas accès à des modèles indisponibles et ne permettent pas de contourner ces exigences. Codex Cloud
ne permet pas de modifier son modèle par défaut.

La disponibilité du mode Rapide dépend de l’espace de travail, de l’interface du produit et de tout
paramètre `features.fast_mode` imposé dans
[`requirements.toml`](/fr-FR/codex/config-file/config-reference#requirementstoml).
Ce paramètre peut imposer l’activation ou la désactivation du mode Rapide pour les clients Codex locaux gérés ; il
ne constitue pas un paramètre de démarrage par défaut et ne peut pas modifier la disponibilité définie par l’espace de travail ou le produit.

## GPT-6 Astra dans l’offre Enterprise

Pendant le déploiement initial, votre organisation doit disposer d’un accès à Daybreak avant
qu’un administrateur puisse activer Astra. Astra est désactivé par défaut dans ChatGPT Enterprise
pendant les deux premières semaines suivant le lancement. Les administrateurs des espaces de travail éligibles
peuvent activer Astra pour des utilisateurs ou des groupes
dans Discussion, Work et Codex. Les critères d’éligibilité existants du produit restent applicables. Examinez les
[paramètres des modèles de votre espace de travail](https://help.openai.com/en/articles/8411955) et
vérifiez la disponibilité sur chaque client utilisé par votre groupe pilote.

Activer l’accès et choisir un modèle initial sont deux décisions distinctes. Vérifiez
la licence, le rôle et les modalités de facturation applicables avant de définir Astra comme modèle par défaut.
Consultez la page [Tarifs](/fr-FR/codex/pricing) pour connaître les quotas d’utilisation et les modalités
de facturation, et la section [surveillance de la sécurité](/fr-FR/codex/agent-approvals-security#safety-monitoring-and-paused-tasks)
pour les tâches mises en pause en vue d’une révision.

Pour une connexion par clé API, l’accès à Astra dépend de l’organisation et du projet de l’API
associés à la clé. Activer Astra dans un espace de travail ChatGPT ne donne pas
accès à l’API. L’accès anticipé avec une clé API nécessite également une configuration du client ;
demandez les instructions de configuration à l’équipe OpenAI chargée de votre compte. Sélectionner un
modèle ou modifier la configuration locale ne suffit pas à obtenir l’accès.

## Préparez le retrait de GPT-5.4

Le 31 août 2026, GPT-5.4 et GPT-5.4 mini seront retirés de Codex pour les utilisateurs connectés
via ChatGPT. Avant cette date, mettez à jour les paramètres par défaut concernés de l’espace de travail,
les paramètres de modèle enregistrés, les configurations gérées, les agents personnalisés et les tâches planifiées :

- Remplacez `gpt-5.4` par `gpt-5.6-terra` (GPT-5.6 Terra).
- Remplacez `gpt-5.4-mini` par `gpt-5.6-luna` (GPT-5.6 Luna).

L’API OpenAI et Codex avec authentification par votre propre clé API ne sont pas concernés.
Consultez les pages [Modèles Codex](/fr-FR/codex/models#deprecated-codex-models) et
[Configuration gérée](/fr-FR/codex/enterprise/managed-configuration)
pour connaître les détails de la migration.

## Distinguez l’accès aux modèles des autorisations appliquées à l’exécution

L’accès aux modèles détermine si un modèle est disponible pour l’utilisateur authentifié
sur une interface prise en charge. Les profils d’autorisations locaux et les exigences de la configuration gérée
déterminent ce qu’un agent peut faire après le démarrage d’une exécution locale, notamment les fichiers qu’il
peut modifier ou les destinations réseau auxquelles il peut accéder.

Un profil d’autorisations ne peut pas donner accès à un modèle. L’accès aux modèles ne peut pas non plus affaiblir
les protections du bac à sable, la politique d’approbation, les contrôles réseau ou les autorisations du système source
applicables à une exécution.

## Résolvez les problèmes d’accès aux modèles

Si un utilisateur ne parvient pas à sélectionner un modèle qui devrait être disponible :

- Vérifiez l’interface du produit utilisée et la méthode de connexion.
- Vérifiez l’espace de travail ChatGPT ou l’organisation et le projet de la Plateforme API.
- Examinez les contrôles d’accès en vigueur pour ce périmètre d’authentification.
- Vérifiez si le client local sélectionné ou Codex Cloud prend en charge le modèle.

## Sources à jour

- [Modèles et limites de ChatGPT Enterprise et ChatGPT Edu](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits)
- [Gérez les paramètres de l’espace de travail](https://help.openai.com/en/articles/8411955)
- [Contrôle d’accès basé sur les rôles](https://help.openai.com/en/articles/11750701-rbac)
- [Modèles Codex](/fr-FR/codex/models)
- [Disponibilité des fonctionnalités Codex selon l’offre](/fr-FR/codex/pricing#feature-availability)
- [Authentification](/fr-FR/codex/auth)

## Documentation associée

- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
- [Groupes et provisionnement](/fr-FR/codex/enterprise/groups-and-provisioning)
- [Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions)
- [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration)
