<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/roles-and-workspace-permissions -->

Différents paramètres régissent les différents aspects de l’expérience ChatGPT au sein de votre organisation. Accorder à quelqu’un un accès dans un domaine ne lui donne pas automatiquement accès à un autre. Consultez cette page pour comprendre comment les six périmètres de contrôle fonctionnent ensemble, puis suivez les guides indiqués pour connaître les étapes de configuration à jour.

Dans les paramètres de l’espace de travail, la section **Codex et Work Local** regroupe l’accès local à Codex et à Work
sous l’autorisation **Autoriser les membres à utiliser Codex et Work en local**. D’autres espaces de travail
présentent **Codex Local** et **Work Local** dans des sections indépendantes. Dans cette
présentation, **Autoriser les membres à utiliser Codex en local** accorde l’accès local à Codex, et
**Utiliser Work en local** accorde l’accès local à Work. Activer l’un n’accorde pas
l’accès à l’autre. Ces libellés correspondent à des autorisations de l’espace de travail, et non à des produits
ou à des clients distincts. Les autorisations liées aux jetons et les limites de durée de validité des identifiants apparaissent
soit dans une section **Jetons d’accès** , soit dans la section consacrée à l’accès local, selon
l’espace de travail. La configuration gérée constitue une couche distincte qui encadre
les comportements à l’exécution pris en charge pour les capacités concernées dans ces clients. Les fonctionnalités
et les exigences applicables peuvent varier selon le client et sa version.

## Comprenez les périmètres de contrôle

| Périmètre          | Ce qu’il contrôle                                                                                                                                                                                      | Ce qu’il ne contrôle pas                                                                          | Source à jour                                                                                                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Espace de travail ChatGPT | Appartenance à l’espace de travail, licences, rôles d’administration intégrés et accès selon les rôles aux fonctionnalités prises en charge dans l’espace de travail                                                                                               | Autorisations de l’agent local, accès à une organisation de la Plateforme API ou autorisations dans un service connecté | [Accès à l’espace de travail ChatGPT](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise) et [RBAC](https://help.openai.com/en/articles/11750701-rbac) |
| Clients locaux     | Comportement à l’exécution des capacités concernées dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE, notamment les approbations, l’accès au système de fichiers et au réseau, les profils d’autorisation et les intégrations autorisées | Une licence ChatGPT, un droit d’accès à une fonctionnalité ou à un modèle, ou un accès à des données externes                         | [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration) et [Autorisations](/fr-FR/codex/permissions)                                                                                                   |
| Codex Cloud       | Éligibilité à l’utilisation des workflows Codex hébergés et des environnements cloud mis à la disposition de l’utilisateur                                                                                                       | Politique d’exécution locale ou autorisations d’accès aux dépôts accordées par un système source                    | [Environnements cloud](/fr-FR/codex/environments/cloud-environment)                                                                                                                                              |
| Plateforme API      | Appartenance à une organisation et à un projet, clés API, accès aux modèles, utilisation et facturation des activités authentifiées via l’API                                                                                            | Appartenance à l’espace de travail ChatGPT, accès aux clients locaux ou à Codex Cloud                         | [Plateforme API](https://platform.openai.com/docs/overview)                                                                                                                                         |
| Plugins           | Disponibilité et installation des plugins, Skills incluses, accès aux connecteurs et actions prises en charge par les connecteurs                                                                                               | Autorisation dans le service connecté ou autorisations d’exécution plus étendues en local et dans le cloud            | [Contrôles des plugins](/fr-FR/codex/enterprise/apps-and-connectors)                                                                                                                                                 |
| Systèmes connectés | Dépôts, fichiers, messages et actions accessibles au compte authentifié dans le système source                                                                                            | Droits d’accès à l’espace de travail ChatGPT, aux plugins, à Codex Cloud ou à la Plateforme API                              | Contrôles d’administration et d’accès du service connecté                                                                                                                                               |

Une requête doit satisfaire aux contrôles de chaque périmètre qui lui est applicable. Par exemple, l’accès à l’espace de travail peut rendre un plugin disponible, mais le service connecté détermine toujours quelles données le compte connecté peut lire. Un profil d’autorisation local peut restreindre une exécution dans un client local pris en charge, mais il ne peut pas donner accès à une fonctionnalité de l’espace de travail ni à un modèle.

## Attribuez les accès à l’espace de travail

L’administration de l’espace de travail ChatGPT distingue l’accès au produit des droits d’administration.

### Comprenez la différence entre une licence, un rôle d’administration et un rôle personnalisé

Une licence détermine les interfaces du produit auxquelles un membre peut accéder. Selon l’offre de l’espace de travail, les types de licences disponibles peuvent inclure des licences ChatGPT et Codex.

Les rôles intégrés à l’espace de travail définissent les droits d’administration. Le rôle **Propriétaire** 
gère les paramètres de l’ensemble de l’espace de travail, le rôle **Administrateur** gère les opérations prises en charge
et les groupes, le rôle **Membre** ne dispose d’aucun droit d’administration et le rôle
**Lecteur des analyses** permet d’accéder aux analyses de l’espace de travail.

Les rôles personnalisés définissent les fonctionnalités prises en charge qu’un membre peut utiliser. Ils ne remplacent pas les conditions d’éligibilité liées à la licence ou à l’offre, n’accordent pas d’autorisations dans un système connecté et ne modifient pas les exigences d’exécution locale.

<div class="not-prose my-4 aspect-video overflow-hidden rounded-md bg-gray-900">
  <iframe
    src="https://player.vimeo.com/video/1215495812"
    title="Présentation du contrôle d’accès basé sur les rôles"
    loading="lazy"
    allow="autoplay; fullscreen; picture-in-picture"
    allowFullScreen
    referrerPolicy="strict-origin-when-cross-origin"
    class="h-full w-full border-0"
  ></iframe>
</div>

### Définissez le paramètre par défaut de l’espace de travail, puis créez des rôles personnalisés ciblés

Seuls les propriétaires de l’espace de travail peuvent configurer le contrôle d’accès basé sur les rôles (RBAC) et créer des rôles personnalisés. Les paramètres de l’espace de travail définissent les valeurs de référence pour les autorisations concernées. Les propriétaires de l’espace de travail peuvent attribuer des rôles personnalisés par l’intermédiaire de groupes ou directement à des membres, lorsque cette option est prise en charge. Les groupes peuvent être gérés manuellement ou synchronisés via SCIM, et un membre peut recevoir plusieurs rôles personnalisés.

Pour les autorisations concernées, **Par défaut** reprend le paramètre de l’espace de travail, **Activé**
accorde l’accès et **Désactivé** le refuse explicitement. Un réglage explicite sur **Désactivé** dans n’importe quel rôle
applicable bloque l’accès, même si un autre rôle l’accorde. Les états d’autorisation
disponibles peuvent varier selon la fonctionnalité.

### Vérifiez les autorisations Work Local et Work Cloud

Lorsque votre espace de travail propose **Work Local** et **Work Cloud**, vérifiez à la fois
le paramètre par défaut de l’espace de travail et chaque rôle personnalisé applicable. Work est réservé
aux espaces de travail éligibles, et les contrôles disponibles peuvent varier selon l’offre, la configuration
de l’espace de travail et le déploiement. Un rôle ne peut pas étendre les droits d’accès accordés
par la licence d’un membre.

**Work Cloud** régit les tâches ChatGPT Work prises en charge dans le cloud. Lorsque les
contrôles sont indépendants, **Work Local** sans **Work Cloud** permet de travailler
localement dans l’application de bureau ChatGPT, mais n’autorise pas les membres à lancer des tâches dans le cloud.
L’accès local à Codex repose sur **Autoriser les membres à utiliser Codex en local** dans **Codex
Local**. Modifier **Utiliser Work en local** ne modifie pas l’accès local à Codex et
ne remplace pas les exigences d’exécution locale.

Certains espaces de travail affichent plutôt une section commune **Codex et Work Local** . Dans
cette présentation, **Autoriser les membres à utiliser Codex et Work en local** contrôle l’accès aux deux
produits.

Pour connaître les conditions d’éligibilité et les paramètres actuels, consultez
[ChatGPT Work et Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Comme les licences, les rôles et les autorisations disponibles évoluent avec les mises à jour du produit et de l’offre, consultez le centre d’aide pour connaître la liste actuelle des autorisations et la procédure de configuration :

- [Gérez les membres, les types de licences, les rôles et les accès](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Configurez le contrôle d’accès basé sur les rôles](https://help.openai.com/en/articles/11750701-rbac)
- [Gérez les groupes](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)

### Contrôlez l’accès à l’historique de l’ordinateur

La fonctionnalité [Historique de l’ordinateur](/fr-FR/codex/customization/computer-history) est désactivée par défaut dans les espaces de travail
Business et Enterprise. Les membres ne peuvent pas l’activer tant qu’un propriétaire de l’espace de travail
ne leur a pas explicitement accordé l’accès. Les propriétaires d’espaces de travail Enterprise peuvent accorder l’accès
par rôle :

1. Ouvrez [**Paramètres de l’espace de travail \> Autorisations et rôles**](https://chatgpt.com/admin/settings).
2. Recherchez **Historique de l’ordinateur** et choisissez le rôle de l’espace de travail qui doit
   y avoir accès.
3. Activez l’option **Activer l’historique de l’ordinateur** pour ce rôle.

Cette autorisation permet uniquement aux membres auxquels elle est attribuée d’activer l’historique de l’ordinateur ; elle n’active pas la fonctionnalité à leur place. Chaque membre doit choisir de l’activer depuis l’application de bureau ChatGPT sur macOS et peut sélectionner les applications et les sites web qui y contribuent. Les membres qui ne disposent pas de l’autorisation requise dans l’espace de travail ne peuvent pas activer cette fonctionnalité depuis les paramètres locaux.

## Appliquez la politique d’exécution locale

La politique d’exécution locale encadre les capacités concernées dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE. Les exigences gérées dans le cloud dépendent également d’une méthode de connexion à ChatGPT prise en charge et de l’éligibilité de l’offre. Les profils d’autorisation et les exigences gérées peuvent limiter les commandes, l’accès au système de fichiers, l’accès au réseau, les approbations et d’autres comportements à l’exécution locale. Ils ne modifient pas la licence de l’utilisateur, son rôle dans l’espace de travail, son droit d’accès aux modèles ni ses autorisations dans un système externe.

Les utilisateurs peuvent sélectionner un profil d’autorisation intégré ou personnalisé lorsque la politique locale
le permet. Les administrateurs peuvent diffuser des paramètres par défaut et des exigences via les
canaux de configuration gérée pris en charge. Consultez la page [Autorisations](/fr-FR/codex/permissions)
pour comprendre le fonctionnement des profils et la page [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration)
pour en savoir plus sur les exigences, leur diffusion et leur ordre de priorité.

## Documentation associée

- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
- [Groupes et provisionnement](/fr-FR/codex/enterprise/groups-and-provisioning)
- [Gestion du cycle de vie des utilisateurs](/fr-FR/codex/enterprise/user-lifecycle)
- [Disponibilité des modèles dans l’espace de travail](/fr-FR/codex/enterprise/workspace-model-availability)
- [Jetons d’accès](/fr-FR/codex/enterprise/access-tokens)
- [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration)
- [Authentification](/fr-FR/codex/auth)
