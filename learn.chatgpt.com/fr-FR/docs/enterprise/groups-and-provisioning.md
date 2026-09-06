<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/groups-and-provisioning -->

Les groupes rassemblent les utilisateurs d’un espace de travail ChatGPT et peuvent se voir attribuer des rôles personnalisés. L’appartenance à un groupe ne remplace pas l’attribution de licences, n’accorde pas à elle seule d’autorisations relatives aux fonctionnalités de l’espace de travail, ne prime pas sur la politique d’exécution locale et ne donne accès ni à la Plateforme API ni aux systèmes connectés.

Pour une présentation complète du modèle de contrôle, consultez
[Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions).

## Comparez les sources de gestion des membres

Utilisez les groupes pour les personnes qui ont un même besoin d’accès, comme les participants à un programme pilote, les opérateurs de l’espace de travail ou les membres qui ont besoin d’une même fonctionnalité prise en charge.

### Créez un groupe pour répondre à un besoin d’accès commun

Les propriétaires et les administrateurs de l’espace de travail peuvent créer et gérer des groupes. Créez un groupe géré manuellement pour un ensemble d’utilisateurs restreint ou temporaire, ou synchronisez un groupe existant depuis votre fournisseur d’identité lorsque la liste des membres doit correspondre à votre annuaire.

Chaque groupe possède une seule source de référence pour la gestion de ses membres :

| Type de groupe                | Source de gestion des membres                   | Cas d’application                                                                  |
| ------------------------- | ----------------------------------- | -------------------------------------------------------------------------------- |
| Géré manuellement          | Administration de l’espace de travail ChatGPT    | Le groupe est de petite taille, temporaire ou n’est pas géré par synchronisation avec un annuaire             |
| Géré par un fournisseur d’identité | Votre fournisseur d’identité via SCIM | La liste des membres doit correspondre à l’annuaire de l’organisation et être mise à jour conformément à son processus de suppression des membres |

Les groupes gérés manuellement et ceux gérés par un fournisseur d’identité peuvent coexister. Pour les groupes synchronisés, le fournisseur d’identité est la source de référence pour la gestion des membres ; des mises à jour de provisionnement ultérieures peuvent écraser les modifications effectuées dans l’espace de travail. Le centre d’aide fait autorité concernant le fonctionnement actuel de SCIM, les attributs pris en charge et les étapes de configuration.

## Comprenez les limites d’accès

L’appartenance à un groupe n’accorde pas, à elle seule, d’autorisation relative aux fonctionnalités de l’espace de travail.

### Associez un groupe aux autorisations appropriées

Les propriétaires de l’espace de travail peuvent attribuer des rôles personnalisés aux groupes ou, lorsque cette possibilité est disponible, directement
aux membres. Vérifiez tous les rôles applicables : une valeur **Désactivé** définie explicitement dans n’importe quel rôle
refuse l’autorisation correspondante, même si un autre rôle l’accorde. Le type de licence du membre
et son éligibilité au produit continuent de s’appliquer.

SCIM assure le provisionnement des membres de l’espace de travail et leur affectation aux groupes. Il n’accorde pas d’autorisations dans GitHub, Google Drive, Slack ou tout autre système connecté. Il ne remplace pas non plus les exigences d’exécution locale ni l’accès à une organisation de la Plateforme API.

Le RBAC de l’espace de travail et les exigences d’exécution locale sont deux systèmes de contrôle distincts. Un
groupe peut être pris en compte dans les deux systèmes, mais ne déduisez pas de l’ordre des groupes dans l’espace de travail une règle de mise en correspondance
ou de priorité applicable aux exigences gérées. Consultez
[Configuration gérée](/fr-FR/codex/enterprise/managed-configuration) pour connaître les règles
documentées de distribution et de priorité locale.

## Utilisez les procédures de configuration à jour

Les modalités d’administration de l’espace de travail peuvent évoluer. Consultez ces sources pour connaître les étapes à jour dans l’interface, la disponibilité et les limites :

- [Gestion des membres, des types de licences, des rôles et des accès](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Gestion des groupes](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)
- [FAQ sur l’intégration SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
- [Gestion des paramètres de l’espace de travail](https://help.openai.com/en/articles/8411955)

### Vérifiez les arrivées, les mobilités internes et les départs

- **Arrivées :** Confirmez que le membre accepte toute invitation en attente à l’espace de travail et
  se voit attribuer la licence prévue, rejoint les groupes prévus et dispose des autorisations
  et des fonctionnalités prises en charge attendues.
- **Mobilités internes :** Mettez à jour la source de référence pour la gestion des membres et vérifiez
  les autorisations effectives du membre en tenant compte de tous les rôles applicables.
- **Départs :** Révoquez, via le fournisseur
  d’identité, l’accès d’un membre géré par SCIM et vérifiez qu’il ne peut plus accéder à l’espace de travail. Si
  vous supprimez le membre uniquement de l’espace de travail, une synchronisation ultérieure peut rétablir
  son accès.

## Documentation connexe

- [Gestion du cycle de vie des utilisateurs](/fr-FR/codex/enterprise/user-lifecycle)
- [Authentification](/fr-FR/codex/auth)
- [Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions)
- [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration)
- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
