<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/service-accounts -->

Les comptes de service vous permettent d’exécuter et de déployer à grande échelle des workflows Codex sans interface graphique dans toute votre organisation, sans dépendre du compte d’un employé. Chaque runner d’intégration continue (CI), tâche planifiée ou intégration partagée dispose de sa propre identité dans l’espace de travail ChatGPT, avec les mêmes groupes, rôles, contrôles d’accès et possibilités d’audit que pour les utilisateurs.

Seuls les propriétaires et les administrateurs de l’espace de travail peuvent créer des comptes de service. Ils peuvent autoriser d’autres personnes ou groupes à gérer un compte, à configurer des plugins ou à créer des jetons d’accès.

Les comptes de service sont disponibles uniquement avec les offres de paiement à l’usage.

Un compte de service représente une identité non humaine au sein de l’espace de travail. Un [jeton d’accès personnel](/fr-FR/codex/enterprise/access-tokens) représente le membre de l’espace de travail qui le crée. Les comptes de service des projets de la Plateforme API et les clés API utilisent un accès aux projets et une facturation distincts.

## Créez et configurez un compte de service

Ce guide interactif prend GitHub comme exemple : créez un compte, configurez un plugin, créez un jeton, puis attribuez des groupes et des rôles.

1. Ouvrez [Comptes de service](https://chatgpt.com/admin/service-accounts) dans les paramètres de votre espace de travail.
2. Sélectionnez le bouton plus (**+**) et saisissez un nom explicite, par exemple `release-automation`.
3. Sélectionnez **Créer**.

## Connecter un plugin

Configurez les plugins directement pour le compte de service. Il n’hérite ni des plugins ni des applications connectées de la personne qui l’a créé.

1. Ouvrez la section **Plugins** du compte et sélectionnez **Ajouter un plugin**.
2. Choisissez un plugin et vérifiez qu’il s’affiche comme configuré ou activé.

Les rôles **Configuration** et **Gestionnaire** permettent de configurer des plugins. Le rôle **Utilisateur** ne le permet pas.

## Créer un jeton d’accès

Créez un jeton depuis la page de détails du compte de service. Ce jeton représente le compte de service, et non la personne qui le crée.

1. Ouvrez le compte et sélectionnez **Créer un jeton** dans **Jetons d’accès**.
2. Nommez le jeton, confirmez la portée **Codex** et choisissez une option d’expiration.
3. Sélectionnez **Créer** et enregistrez le jeton dans votre gestionnaire de secrets.

Le jeton complet ne s’affiche qu’une seule fois. Les politiques de l’espace de travail déterminent les options d’expiration disponibles.

## Attribuer des rôles et des groupes

Comme un membre humain, un compte de service peut recevoir des rôles dans l’espace de travail et rejoindre des groupes. Attribuez-lui directement ses accès : il n’hérite pas des autorisations de la personne qui l’a créé.

Pour permettre à des personnes ou à des groupes de gérer le compte, sélectionnez **Partager**, puis **Ajouter des personnes ou des groupes**, et attribuez un rôle :

| Rôle sur le compte partagé | Configurer le compte et ses plugins | Créer des jetons d’accès pour le compte de service |
| ------------------- | ------------------------------------- | ------------------------------------ |
| **Utilisateur**            | Non                                    | Oui                                  |
| **Configuration**       | Oui                                   | Non                                   |
| **Gestionnaire**         | Oui                                   | Oui                                  |

Ces rôles s’appliquent aux personnes qui gèrent le compte. Ils sont distincts des rôles de l’espace de travail et des groupes attribués au compte de service.

Les rôles **Configuration** et **Gestionnaire** permettent d’activer ou de désactiver le compte. Seuls les propriétaires et les administrateurs de l’espace de travail peuvent créer, supprimer ou partager des comptes. Les opérateurs gèrent les comptes partagés en étant connectés à leur propre compte ChatGPT.

Pour en savoir plus sur les autorisations de l’espace de travail, consultez [Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions).

## Exécuter Codex sans se connecter

Les jetons d’accès des comptes de service nécessitent la version `0.142.0` ou une version ultérieure de Codex CLI. Définissez `CODEX_ACCESS_TOKEN`, puis exécutez Codex sans ouvrir de navigateur :

```bash

codex exec --json "Inspect this repository and summarize its current state."

En CI, transmettez le jeton via un gestionnaire de secrets ou un secret du runner.

Pour enregistrer les identifiants de connexion sur une machine de confiance, transmettez le jeton via l’entrée standard :

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "Summarize the changes in the current branch."

Cette opération enregistre les informations d’authentification localement. Sur les runners partagés ou temporaires, utilisez `CODEX_ACCESS_TOKEN` sans enregistrer d’identifiants de connexion.

## Provisionner des comptes de service avec SCIM

Si votre espace de travail permet de provisionner des comptes de service via le protocole System for Cross-domain Identity Management (SCIM), définissez `userType` sur `ServiceAccount` dans votre fournisseur d’identité :

```json
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "userName": "svc-codex-release@company.example",
  "displayName": "Codex release automation",
  "active": true,
  "userType": "ServiceAccount"
}

Attribuez l’identité à l’espace de travail et aux groupes requis, puis synchronisez-la. Le fournisseur d’identité gère le nom du compte, son appartenance aux groupes et son cycle de vie. Les comptes gérés par SCIM ne peuvent être ni renommés ni supprimés dans ChatGPT. Consultez [Groupes et provisionnement](/fr-FR/codex/enterprise/groups-and-provisioning).

## Gestion des comptes de service avec l’API Admin

Si votre espace de travail y a accès, utilisez une clé de l’API Admin de ChatGPT pour gérer les comptes, les tokens et le partage. Les opérations de lecture nécessitent `chatgpt.enterprise.service_account.read` ; les modifications nécessitent `chatgpt.enterprise.service_account.write`. Un token de compte de service ne permet pas d’authentifier les requêtes adressées à l’API Admin.

Consultez la [référence de l’API Admin](https://chatgpt.com/public/admin/api-reference) pour connaître les opérations disponibles et les chemins actuels des requêtes.

### Comptes

| Opération                    | Méthode   | Description                               |
| ---------------------------- | -------- | ------------------------------------------ |
| Lister les comptes                | `GET`    | Renvoie les comptes de service de l’espace de travail         |
| Créer un compte            | `POST`   | Crée un compte de service avec un nom            |
| Récupérer un compte               | `GET`    | Renvoie un compte de service                |
| Activer ou désactiver un compte | `PATCH`  | Met à jour la valeur `enabled` du compte      |
| Supprimer un compte            | `DELETE` | Supprime le compte et révoque ses tokens |

Créez des comptes avec `POST /v1/manage/workspaces/{workspace_id}/service-accounts`. Les mises à jour du compte modifient uniquement `enabled`.

### Tokens

| Opération      | Méthode   | Description                         |
| -------------- | -------- | ------------------------------------ |
| Lister les tokens    | `GET`    | Renvoie les métadonnées des tokens du compte |
| Créer un token | `POST`   | Crée un jeton d’accès associé à un périmètre défini        |
| Révoquer un token | `DELETE` | Révoque définitivement un token        |

Par exemple, créez un token Codex qui expire après 30 jours :

```json
{
  "name": "production-release-runner",
  "ttl": 2592000,
  "scopes": ["chatgpt.workspace.feature.allow-codex-local-access.access"]
}

`ttl` indique la durée de validité du token en secondes. Une durée de validité limitée doit être inférieure à un an et respecter la politique d’expiration de votre espace de travail. La valeur complète de `access_token` est renvoyée uniquement à la création du token.

L’API Admin permet également de lister, d’ajouter, de modifier et de supprimer les accès aux comptes partagés. Les valeurs de rôle sont `manager`, `configurer` et `user` ; `configurer` apparaît sous le nom **Configurer** dans ChatGPT.

## Sécurisation et gestion des comptes de service

- N’accordez que les rôles, groupes, plugins et connexions nécessaires au workflow.
- Stockez les tokens dans un gestionnaire de secrets et utilisez des runners de confiance.
- N’incluez aucune information d’authentification dans les journaux, les messages de discussion ou le système de gestion de versions.
- Définissez des durées de validité limitées et vérifiez régulièrement les accès aux comptes ainsi que leur activité.
- Pour renouveler un token, créez un token de remplacement, mettez à jour le workflow, vérifiez l’accès, puis révoquez l’ancien token dans l’espace de travail ou via l’API Admin.
- Révoquez immédiatement les tokens exposés et examinez l’activité récente du compte.
- Désactivez ou supprimez les comptes inutilisés dans l’espace de travail ou via l’API Admin. Ces deux actions révoquent tous les tokens actifs. Les comptes désactivés peuvent être réactivés avec de nouveaux tokens ; la suppression est irréversible.

Les exécutions sont attribuées au compte de service. Les analyses de l’espace de travail et les journaux d’audit disponibles peuvent également indiquer qui a créé des tokens ou modifié les paramètres du compte. Vérifiez les événements couverts dans la [référence de l’API Admin](https://chatgpt.com/public/admin/api-reference).

## Documentation associée

- [Authentification](/fr-FR/codex/auth)
- [Jetons d’accès personnels](/fr-FR/codex/enterprise/access-tokens)
- [Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions)
- [Groupes et provisionnement](/fr-FR/codex/enterprise/groups-and-provisioning)
- [Gouvernance](/fr-FR/codex/enterprise/governance)
- [API de conformité et événements d’audit](/fr-FR/codex/enterprise/compliance-api)
- [Mode non interactif](/fr-FR/codex/non-interactive-mode)
