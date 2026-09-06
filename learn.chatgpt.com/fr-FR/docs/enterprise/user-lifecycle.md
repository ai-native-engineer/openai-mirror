<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/user-lifecycle -->

Utilisez ce guide pour accorder aux employés les accès appropriés à l’espace de travail ChatGPT à leur arrivée, les mettre à jour lorsque leurs responsabilités changent et les supprimer à leur départ. Ce processus couvre également les licences de l’espace de travail, les rôles attribués aux groupes, les jetons d’accès Codex et les systèmes connectés disposant de leurs propres contrôles d’accès.

L’authentification unique (SSO) vérifie l’identité d’un employé. Le provisionnement ajoute l’employé à un espace de travail. Aucune de ces actions ne détermine à elle seule sa licence, ses autorisations d’accès aux fonctionnalités, sa politique d’exécution locale ou son accès à un système externe.

Gérez les accès des employés à trois étapes de leur cycle de vie :

- **Arrivée :** Provisionnez l’accès à l’espace de travail, les groupes, les rôles et la licence appropriée.
- **Mobilité :** Mettez à jour les groupes de l’employé et supprimez uniquement les rôles directs devenus inutiles.
- **Départ :** Supprimez l’accès à l’espace de travail, révoquez les jetons et examinez les systèmes connectés.

## Vérifiez les prérequis et désignez les responsables

Avant d’intégrer les employés, identifiez qui gère chaque partie du cycle de vie :

| Responsable                     | Responsabilité                                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| Propriétaire de l’espace de travail           | Activez la synchronisation de l’annuaire, attribuez les rôles dans l’espace de travail, approuvez les types de licences et examinez les accès aux données d’audit |
| Administrateur des identités    | Configurez le fournisseur d’identité, les affectations aux applications, les groupes de provisionnement et l’état de la synchronisation        |
| Administrateur de l’espace de travail   | Examinez les membres de l’espace de travail, les appartenances aux groupes et les paramètres d’administration pris en charge                     |
| Responsable de la sécurité ou du service | Examinez les jetons Codex, les systèmes connectés, les automatisations partagées et les justificatifs d’audit requis                |

Confirmez l’espace de travail cible, vérifiez le domaine de messagerie de l’organisation si nécessaire et identifiez un propriétaire de l’espace de travail capable d’activer la synchronisation de l’annuaire. Vérifiez ensuite les contrôles pris en charge par l’offre de l’espace de travail :

| Fonctionnalité                                 | Offres d’espace de travail compatibles                                                                                    |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Synchronisation de l’annuaire via SCIM     | ChatGPT Enterprise, Edu et Healthcare                                                                      |
| Rôles personnalisés et contrôle d’accès basé sur les rôles | ChatGPT Enterprise, Edu, Healthcare et Teachers                                                            |
| Jetons d’accès Codex                        | ChatGPT Business et Enterprise                                                                              |
| Licences Codex uniquement                           | Espaces de travail Enterprise éligibles et espaces de travail Business existants remplissant les conditions requises ; indisponible pour Edu, Teachers ou Healthcare |

SCIM signifie System for Cross-domain Identity Management. Un espace de travail Business peut prendre en charge les jetons d’accès Codex sans SCIM, tandis qu’un espace de travail Edu peut prendre en charge SCIM sans jetons d’accès Codex ni licences Codex uniquement. Appliquez uniquement les contrôles disponibles dans votre espace de travail.

Un espace de travail Business ne peut conserver et ajouter des licences Codex uniquement que s’il disposait d’une licence
Codex avant le 24 juin 2026 ou d’une invitation en attente à cette date pour une licence Codex
remplissant les conditions requises. Les nouveaux espaces de travail Business et ceux qui ne disposent ni d’une licence ni
d’une invitation remplissant ces conditions ne peuvent pas ajouter leur première licence Codex uniquement. Consultez
[Gérer le cycle de vie et la migration des espaces de travail dans ChatGPT Business](https://help.openai.com/en/articles/8801890-managing-workspace-lifecycle-and-migration-in-chatgpt-business).

Si l’espace de travail prend en charge plusieurs types de licences, vérifiez le type par défaut dans
**Paramètres de l’espace de travail \> Identité et accès** avant d’activer le provisionnement
automatisé. Les utilisateurs provisionnés via SCIM héritent de ce type par défaut, et leur licence détermine
les interfaces produit disponibles. Un rôle personnalisé ne peut pas accorder un accès
qui n’est pas inclus dans la licence.

Utilisez **Autorisations et rôles** pour examiner les contrôles relatifs à l’accès local, aux jetons d’accès,
à la durée de validité des identifiants et aux appareils distants. Certains espaces de travail regroupent l’accès
local dans **Codex et Work Local**, avec le contrôle **Autoriser les membres à utiliser Codex et
Work en local** . D’autres séparent **Codex Local**, avec **Autoriser les membres
à utiliser Codex en local**, de **Work Local**, avec **Utiliser Work en local**.
Les contrôles distincts de Codex et de Work n’accordent pas l’accès à l’autre produit. Les contrôles des jetons
figurent soit dans la section d’accès local, soit dans une section **Jetons
d’accès** distincte. Ces paramètres sont indépendants de l’appartenance aux groupes et
des types de licences attribués.

L’exemple suivant présente les contrôles regroupés de **Codex et Work Local** et une
section **Jetons d’accès** distincte :

  

Pour connaître les prérequis actuels et les configurations d’identité prises en charge, consultez
[Identité et provisionnement](https://help.openai.com/en/articles/9672121)
et [Gérer les membres, les types de licences, les rôles et les accès](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise).

## Choisissez comment les employés rejoignent l’espace de travail

Choisissez une méthode de provisionnement principale pour chaque population d’utilisateurs :

| Méthode                     | Comment l’accès est accordé                                                       | Où supprimer l’accès                                  |
| -------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------- |
| Invitation manuelle          | Un propriétaire ou un administrateur de l’espace de travail invite un employé                          | Administration des membres de l’espace de travail                         |
| Création automatique de comptes | Un employé dont l’adresse e-mail utilise un domaine éligible se connecte                      | Administration de l’espace de travail et processus de gestion des identités concerné |
| Synchronisation de l’annuaire avec SCIM   | Un administrateur des identités affecte l’employé dans le fournisseur d’identité | Application ou groupe de provisionnement dans le fournisseur d’identité |

Utilisez les invitations manuelles pour un projet pilote restreint ou un groupe qui n’est pas géré par la synchronisation de l’annuaire. Utilisez SCIM lorsque l’appartenance à l’espace de travail doit suivre les changements du fournisseur d’identité à l’arrivée des employés, lors de leurs changements d’équipe ou à leur départ.

N’activez pas simultanément la création automatique de comptes et SCIM. Les utilisateurs ajoutés par
la création automatique de comptes peuvent ne pas être gérés par SCIM. Leur retrait
d’un groupe du fournisseur d’identité risque donc de ne pas supprimer leur accès à l’espace de travail. Consultez la
[FAQ sur l’intégration SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
pour connaître les recommandations actuelles.

SCIM peut connecter un seul espace de travail ChatGPT ou le tenant d’une organisation, selon la configuration d’identité approuvée. Définissez explicitement chaque affectation à un espace de travail et à un produit. Une connexion partagée à l’annuaire n’accorde ni ne supprime automatiquement l’accès à tous les espaces de travail ou à toutes les organisations de la Plateforme API.

## Connectez un groupe de provisionnement au bon espace de travail

Configurez la connexion avant d’ajouter le premier employé du groupe pilote. Le propriétaire de l’espace de travail et l’administrateur des identités ont des responsabilités distinctes :

1. Demandez au propriétaire de l’espace de travail de sélectionner l’espace de travail ChatGPT prévu et d’examiner
**Paramètres de l’espace de travail \> Groupes**. Consignez les noms des groupes existants, leurs membres,
   les rôles personnalisés attribués et les partages de projets ou de GPT concernés.
2. Demandez à l’administrateur des identités d’identifier précisément le groupe du fournisseur d’identité à synchroniser. Comparez son nom et ses membres à ceux de chaque groupe existant dans l’espace de travail.
3. Si un groupe synchronisé porte le même nom qu’un groupe existant dans l’espace de travail, harmonisez les groupes concernés ou renommez le groupe en conflit avant d’activer la synchronisation. Demandez au propriétaire de l’espace de travail d’approuver les membres, les rôles hérités et les partages qui en résultent. Un groupe existant portant le même nom devient géré par SCIM, et la gestion de ses membres passe sous le contrôle du fournisseur d’identité.
4. Sélectionnez un groupe pilote au périmètre restreint et consignez l’espace de travail approuvé, les employés attendus et les rôles attribués aux groupes.
5. Demandez au propriétaire de l’espace de travail d’ouvrir **Paramètres de l’espace de travail \> Identité et accès**
   et de sélectionner **Activer la synchronisation de l’annuaire**. Si un choix vous est proposé, choisissez **Utiliser SCIM uniquement
   pour cet espace de travail** pour un provisionnement au niveau de l’espace de travail, ou **Conserver la possibilité
   d’étendre à d’autres produits** pour un provisionnement approuvé au niveau du tenant. Si
   SCIM est déjà actif au niveau du tenant, gérez cette connexion existante
   au lieu de créer une seconde connexion pour l’espace de travail.
6. Demandez à l’administrateur des identités de finaliser la connexion au fournisseur d’identité, de sélectionner l’application ChatGPT et d’y affecter le groupe approuvé afin de provisionner les membres dans l’espace de travail prévu.
7. Dans **Paramètres de l’espace de travail \> Groupes**, confirmez que le groupe sélectionné affiche
   son badge SCIM. Vérifiez le nom du groupe, les membres synchronisés et l’espace de travail
   cible avant d’utiliser ce groupe pour accorder des accès.
8. Demandez au propriétaire de l’espace de travail d’ouvrir **Autorisations et rôles \> Rôles personnalisés**,
   de créer ou de sélectionner le rôle approuvé, puis de l’attribuer au groupe synchronisé.
   La configuration des rôles est disponible sur le Web et nécessite les droits
   de propriétaire de l’espace de travail.
9. Examinez les autorisations effectives du groupe et le type de licence par défaut de l’espace de travail
avant d’ajouter un employé représentatif pour le pilote.

L’administrateur du fournisseur d’identité gère les affectations aux applications et l’appartenance aux groupes ;
le propriétaire de l’espace de travail gère la synchronisation de l’annuaire et l’attribution des rôles
dans l’espace de travail. Consultez la [FAQ sur l’intégration SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
et la page [Configurez le contrôle d’accès basé sur les rôles](https://help.openai.com/en/articles/11750701-rbac)
pour connaître les étapes et les disponibilités actuelles propres à chaque fournisseur.

## Provisionnez l’accès d’un nouvel employé

Pour un employé géré via SCIM :

1. Confirmez l’espace de travail prévu, l’adresse e-mail vérifiée, le type de licence par défaut
et le groupe du fournisseur d’identité.
2. Affectez l’employé à l’application ChatGPT ou au groupe qui accorde l’accès
chez le fournisseur d’identité.
3. Attendez la fin de la synchronisation de l’annuaire. Vérifiez l’état actuel
chez le fournisseur d’identité si l’employé n’apparaît pas.
4. Dans **Paramètres de l’espace de travail \> Membres**, vérifiez l’adresse e-mail de l’employé,
   son appartenance à l’espace de travail ou son invitation en attente, son type de licence et son badge SCIM.
5. Dans **Paramètres de l’espace de travail \> Groupes**, confirmez que l’employé appartient au
   groupe synchronisé prévu. Demandez au propriétaire de l’espace de travail de vérifier le rôle personnalisé
   attribué à ce groupe.
6. Demandez à un employé représentatif de se connecter au bon espace de travail et de vérifier
les interfaces du produit, les fonctionnalités et les systèmes connectés dont il a besoin.
7. Consignez le responsable des accès et le résultat positif de la vérification selon
la procédure approuvée par votre organisation.

Si vous ajoutez un employé manuellement, envoyez l’invitation depuis l’interface d’administration des membres de l’espace de travail,
puis effectuez les mêmes vérifications de licence, de groupe, de rôle et de connexion.

Un groupe permet d’organiser les membres, mais n’accorde pas à lui seul l’accès à toutes les fonctionnalités.
Pour connaître la procédure actuelle d’attribution des rôles, consultez
[Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions)
et [Configurez le contrôle d’accès basé sur les rôles](https://help.openai.com/en/articles/11750701-rbac).

## Mettez à jour les accès lorsqu’un employé change d’équipe

Un employé qui change d’équipe peut conserver les accès accordés par ses précédents groupes ou rôles.
Mettez à jour le système qui gère son appartenance avant de vérifier
son nouveau niveau d’accès :

1. Identifiez la nouvelle équipe de l’employé, l’espace de travail et la licence nécessaires,
les autorisations de fonctionnalités approuvées et le groupe de destination.
2. Ajoutez l’employé au groupe de destination approuvé avant de le retirer
de son ancien groupe s’il doit rester dans l’espace de travail pendant toute
la transition. Mettez à jour l’appartenance gérée par SCIM chez le fournisseur d’identité ; mettez à jour
l’appartenance gérée manuellement depuis l’interface d’administration de l’espace de travail.
3. Confirmez que le rôle approuvé est déjà attribué au groupe de destination.
Conservez les attributions de rôles existantes sur les groupes partagés afin que les autres membres
gardent leurs accès approuvés.
4. Demandez à un propriétaire de l’espace de travail de modifier l’attribution d’un rôle à un groupe uniquement après
avoir approuvé un changement de politique distinct pour l’ensemble du groupe et examiné ses effets
sur chacun de ses membres.
5. Demandez à un propriétaire de l’espace de travail d’ouvrir le profil de l’employé, d’examiner les **Rôles directs**,
   puis de retirer les rôles obsolètes attribués directement à cette personne. Les rôles personnalisés utilisent les valeurs **Par défaut**,
**Activé** et **Désactivé**. La valeur explicite **Désactivé** dans un rôle attribué prévaut sur
**Activé** dans un autre rôle.
6. Examinez les autorisations effectives de l’employé sur l’ensemble des rôles attribués directement
ou par l’intermédiaire de groupes avant d’approuver le changement d’équipe.
7. Si l’espace de travail prend en charge plusieurs types de licences, demandez à un propriétaire de l’espace de travail d’ouvrir
**Paramètres de l’espace de travail \> Membres \> Modifier le type de licence** et d’examiner
   les accès aux produits prévus pour l’employé.
8. Avant de convertir une licence ChatGPT en licence réservée à Codex, confirmez que
l’employé doit perdre l’accès aux discussions, aux mémoires, aux projets et aux autres
fonctionnalités de ChatGPT. Les données sous-jacentes ne sont pas supprimées et redeviennent accessibles
si l’employé repasse à une licence ChatGPT.
9. Une fois la synchronisation et les mises à jour des autorisations terminées, vérifiez à la fois
les nouvelles actions autorisées et celles qui ne doivent plus être disponibles.

Si l’employé est propriétaire d’un workflow d’automatisation, examinez si le token Codex de ce workflow,
son entrée dans le gestionnaire de secrets ou son autorisation auprès d’un service connecté doivent être transférés à un autre
propriétaire approuvé. Retirer à l’employé l’autorisation d’utiliser Codex en local suspend ses
tokens Codex sans les révoquer. Rétablir cette autorisation
réactive ces tokens ; révoquez donc les identifiants qui doivent perdre définitivement leur accès.

## Retirez un employé sur le départ

Commencez par le système qui gère l’appartenance de l’employé à l’espace de travail :

1. Déterminez si l’employé est géré par SCIM ou si un administrateur l’a ajouté
manuellement.
2. Pour un employé géré par SCIM, supprimez son affectation à l’application ChatGPT
et retirez-le de tous les groupes de provisionnement qui lui accordent un accès
chez le fournisseur d’identité. Ne supprimez pas les groupes partagés eux-mêmes.
3. Pour un employé qui n’est pas géré via SCIM, demandez à un propriétaire ou à un administrateur
   de l’espace de travail de retirer le membre depuis **Paramètres de l’espace de travail \> Membres**.
4. Confirmez que le membre n’est plus présent dans l’espace de travail prévu.
Pour les accès gérés par SCIM, vérifiez que la synchronisation est terminée et qu’aucune
autre affectation chez le fournisseur d’identité ne peut rétablir son appartenance.
5. Consignez le retrait effectué et désignez un responsable pour examiner les tokens,
les systèmes connectés et les données conservées.

Ne vous contentez pas d’un retrait dans l’espace de travail si le fournisseur d’identité affecte encore
l’employé à un groupe géré par SCIM. Une synchronisation ultérieure peut le réintégrer
dans l’espace de travail.

### Révoquez les jetons d’accès Codex et transférez les automatisations

Retirer une personne de l’espace de travail ne remplace pas un examen explicite des
identifiants utilisés par les automatisations de confiance. Appliquez cette procédure uniquement si
l’espace de travail prend en charge les jetons d’accès Codex et que ceux-ci sont activés.

Retirer l’autorisation d’utiliser Codex en local suspend les tokens existants sans les révoquer.
Ces tokens peuvent fonctionner à nouveau si un propriétaire de l’espace de travail rétablit l’autorisation ;
révoquez donc explicitement les identifiants qui doivent perdre définitivement leur accès.

La page **Jetons d’accès** indique le créateur et l’état de chaque token. Utilisez
**Révoquer** pour supprimer l’accès des tokens actifs :

  

1. Demandez à un propriétaire ou à un administrateur de l’espace de travail d’ouvrir
[Jetons d’accès](https://chatgpt.com/admin/access-tokens).
2. Identifiez les tokens créés par l’employé sur le départ et les workflows qui
les utilisent.
3. Choisissez l’identité de remplacement. Pour un workflow pérenne exécuté par une identité non humaine avec une
   offre éligible facturée à l’usage, utilisez un [compte de
   service](/fr-FR/codex/enterprise/service-accounts) dédié et approuvé. Sinon, identifiez un
   propriétaire de workflow actif et approuvé. Demandez à un propriétaire de l’espace de travail d’accorder à cette personne
   l’autorisation de créer des jetons d’accès si nécessaire, et confirmez qu’elle dispose
   de l’autorisation d’utiliser Codex en local.
4. Créez le token de remplacement. Un opérateur de compte de service disposant des autorisations nécessaires peut
   créer un token depuis la page de détails du compte de service. Pour un remplacement par un token personnel,
   demandez au nouveau propriétaire du workflow de créer un token pour sa propre identité
   dans l’espace de travail ChatGPT. Si la boîte de dialogue affiche **Portées**, sélectionnez
**Codex**. Ne sélectionnez d’autres portées que si le workflow en a besoin. Une
   boîte de dialogue sans **Portées** crée un token réservé à Codex. Un administrateur ne peut pas
   créer de token personnel au nom d’un autre utilisateur.
5. Mettez à jour le secret stocké pour le workflow, puis vérifiez que celui-ci s’exécute correctement
avec le token de remplacement.
6. Demandez au propriétaire ou à l’administrateur de l’espace de travail de révoquer les tokens de l’employé sur le départ
ainsi que tous les identifiants remplacés.
7. Confirmez que les tokens révoqués ne permettent plus de lancer de nouvelles exécutions authentifiées.

Lorsqu’un propriétaire remplaçant approuvé crée un token, utilisez un nom descriptif pour le workflow
et choisissez la durée de validité des identifiants la plus courte autorisée par la politique
de votre organisation. Si **Portées** apparaît, sélectionnez **Codex** et évitez les autorisations dont le
workflow n’a pas besoin. L’exemple suivant présente l’interface avec sélection des portées :

  

Les propriétaires et administrateurs d’un espace de travail peuvent révoquer tous les tokens de cet espace. Un membre
disposant de l’autorisation relative aux jetons d’accès ne peut révoquer que les tokens qu’il a créés. Pour connaître
les autorisations actuelles relatives aux tokens et les étapes de rotation, consultez
[Jetons d’accès](/fr-FR/codex/enterprise/access-tokens#rotate-or-revoke-a-token).

### Examinez les systèmes connectés et les données conservées

Le provisionnement de l’espace de travail ne couvre pas tous les périmètres d’autorisation. Demandez au
responsable du service concerné d’examiner les accès aux éléments suivants :

- Les dépôts de code source et les comptes GitHub connectés.
- Google Drive, Slack et les autres applications connectées.
- Les plugins installés, les skills incluses et les capacités fournies par les connecteurs.
- Les environnements Codex hébergés, les automatisations partagées et les secrets stockés.
- Les appareils gérés, les identifiants stockés localement et les sessions à distance prises en charge.
- Les organisations, projets et clés API distincts de la Plateforme API.

Appliquez les contrôles propres à chaque système au lieu de supposer qu’une modification d’un groupe de l’espace de travail
ou de SCIM met à jour les autorisations partout. Consultez
[Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions)
pour connaître le modèle complet des périmètres d’autorisation, et [Contrôles des plugins](/fr-FR/codex/enterprise/apps-and-connectors)
pour la disponibilité des plugins, les skills incluses et les autorisations des applications connectées.

Retirer l’accès à l’espace de travail ne revient pas à supprimer du contenu. Lorsqu’un membre
quitte l’espace de travail, celui-ci transfère automatiquement la propriété de ses projets et de ses
GPT personnalisés à un propriétaire de l’espace de travail. Ces éléments ne sont pas marqués pour suppression.
Si le membre revient, il en redevient propriétaire.

Dans les espaces de travail Entreprise et Edu, les discussions, les fichiers et les documents canvas suivent
la politique de conservation configurée pour l’espace de travail. Les espaces de travail Business conservent les discussions,
les fichiers et les documents canvas indéfiniment. Les espaces de travail Healthcare proposent également
des contrôles de conservation des données ; examinez la configuration applicable à l’espace de travail et
les [consignes de ChatGPT for Healthcare](https://help.openai.com/en/articles/20001046-chatgpt-for-healthcare).

Réattribuer un projet ou un GPT ne transfère pas les conversations ou les fichiers privés
de l’ancien membre, et le propriétaire de l’espace de travail ne peut pas consulter ce contenu privé
du fait du changement de propriétaire. Consultez
[Retrait de membres de l’espace de travail et conservation des données](https://help.openai.com/en/articles/8266418)
pour connaître le comportement actuel propre à chaque offre.

Si la sécurité ou la conformité exige des preuves du changement, consignez dans le système approuvé
l’espace de travail concerné, l’employé, l’affectation dans le fournisseur d’identité, l’heure de réalisation,
le responsable de l’approbation et la vérification de la révocation des tokens.
Vérifiez les enregistrements disponibles, les autorisations des administrateurs et les règles de conservation dans la
[Référence de l’API d’administration](https://chatgpt.com/admin/api-reference), accessible après authentification.
Les périmètres d’accès sensibles liés à la conformité peuvent nécessiter l’intervention d’un propriétaire de l’espace de travail. Pour une présentation
du produit, consultez [API de conformité et événements d’audit](/fr-FR/codex/enterprise/compliance-api).
Ne déduisez pas de ce guide les événements couverts, les champs disponibles ou les durées de conservation.

## Résolvez les problèmes d’accès manquant ou inattendu

| Symptôme                                               | Points à vérifier                                                                             | Action corrective                                                                                                       |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Un employé peut se connecter, mais ne trouve pas l’espace de travail  | L’espace de travail cible, l’invitation, l’affectation dans le fournisseur d’identité et l’adresse e-mail         | Corrigez l’affectation ou la correspondance de l’adresse e-mail, puis vérifiez l’appartenance à l’espace de travail                                               |
| Un employé synchronisé reçoit une licence de type incorrect       | Le type de licence par défaut de l’espace de travail et la fiche actuelle du membre                     | Demandez à un propriétaire de l’espace de travail de vérifier le type de licence par défaut et les options de licence disponibles pour l’employé                                     |
| Un changement d’équipe ne retire pas l’accès à une fonctionnalité                | Les appartenances à d’autres groupes, les **Rôles directs** et les autorisations cumulées de l’employé        | Retirez l’employé des groupes auxquels il ne doit plus appartenir, puis demandez à un propriétaire de l’espace de travail de révoquer uniquement les rôles directs devenus inutiles pour cet employé |
| Un groupe géré manuellement passe sous gestion SCIM sans approbation  | Les noms de groupe identiques, les membres dans le fournisseur d’identité, les rôles hérités et les partages existants    | Alignez les appartenances aux groupes dans le fournisseur d’identité sur celles qui ont été approuvées, puis examinez les accès concernés                                 |
| D’autres employés perdent leur accès après un changement d’équipe       | Les modifications récentes des rôles attribués aux groupes partagés et les accès approuvés pour l’ancienne équipe     | Demandez à un propriétaire de l’espace de travail de rétablir le rôle approuvé du groupe partagé, puis mettez à jour uniquement l’appartenance de l’employé qui change d’équipe        |
| Un token d’automatisation cesse de fonctionner après un changement d’équipe | L’autorisation du propriétaire du workflow d’utiliser Codex en local et l’état actuel du token                      | Demandez à un propriétaire de l’espace de travail de rétablir l’accès approuvé à Codex en local, ou remplacez puis révoquez le token concerné                     |
| Un changement d’accès n’apparaît pas immédiatement           | L’état de synchronisation du fournisseur d’identité, le délai de synchronisation prévu et les mises à jour récentes des rôles          | Demandez à l’administrateur des identités de vérifier la synchronisation avant de contacter l’assistance OpenAI                                        |
| Un employé retiré réapparaît dans l’espace de travail           | L’affectation à l’application dans le fournisseur d’identité et tous les groupes de provisionnement qui accordent l’accès | Retirez l’employé dans le fournisseur d’identité, plutôt que seulement dans les paramètres de l’espace de travail                                      |
| Un employé sur le départ possède encore un token dans la liste         | Le créateur du token, le propriétaire du workflow et les autorisations de gestion des tokens de l’administrateur de l’espace de travail        | Renouvelez les informations d’authentification nécessaires à l’automatisation, puis révoquez le token de l’employé sur le départ                                   |
| Une application connectée autorise toujours l’accès           | Le compte dans le système source, la disponibilité du plugin et l’autorisation accordée à l’application                   | Demandez au responsable du service concerné de retirer l’accès à l’aide des contrôles pris en charge par ce système                                  |

La plupart des fournisseurs d’identité se synchronisent toutes les 30 à 40 minutes, mais certains
appliquent les mises à jour immédiatement. Les modifications des rôles personnalisés peuvent mettre environ cinq minutes à
apparaître. Vous ne pouvez pas forcer une synchronisation SCIM : ne supprimez donc pas un membre de l’espace de travail pour le recréer
et contourner ainsi un retard de mise à jour.

Si un retrait d’accès ou une mise à jour de groupe n’est toujours pas terminé une fois le délai prévu
pour le fournisseur écoulé, demandez à l’administrateur des identités de recueillir les éléments suivants :

- L’espace de travail concerné et l’adresse e-mail de l’employé.
- Le fournisseur d’identité, l’affectation à l’application et le groupe de provisionnement.
- Le changement tenté, son horodatage et le dernier état de synchronisation.
- Les rôles directs, les rôles de groupe ou les tokens qui restent à examiner.

Contactez l’[assistance OpenAI](https://help.openai.com/) en fournissant ces informations via
le centre d’aide. Traitez le maintien de l’accès d’un employé ayant quitté l’organisation comme une anomalie de sécurité
et suivez la procédure d’escalade des incidents de votre organisation.

Pour connaître la configuration et le comportement de synchronisation propres à chaque fournisseur, consultez la version actuelle de la
[FAQ sur l’intégration SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq).
Pour les erreurs de connexion et d’identité, consultez
[Dépannage de l’authentification](https://help.openai.com/en/articles/10489721-login-and-authentication-faq-s-and-troubleshooting-sso-scim-and-domain-verification).

## Vérifiez l’ensemble du cycle de vie de l’employé

Vérifiez les trois transitions avec un employé test représentatif avant un
déploiement plus large :

| Étape du cycle de vie | Responsable principal                 | Résultat attendu                                                                                                            |
| --------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Arrivée          | Administrateur des identités        | L’employé rejoint le bon espace de travail avec la licence, le groupe et l’accès aux fonctionnalités prévus                                    |
| Changement d’équipe           | Responsables des identités et propriétaires de l’espace de travail | Les administrateurs mettent à jour l’appartenance aux groupes, et les propriétaires de l’espace de travail retirent les rôles directs devenus inutiles tout en préservant les rôles des groupes partagés |
| Départ          | Responsables des identités et de la sécurité  | Les administrateurs retirent l’accès à l’espace de travail, examinent les tokens pris en charge et révoquent ou réattribuent les accès externes                       |

Consignez qui a approuvé chaque changement, ce que vous avez vérifié et qui est
responsable de résoudre les exceptions d’accès restantes. Planifiez des examens réguliers
des accès conformément aux politiques de gestion des identités et de sécurité de votre organisation.

## Documentation associée

- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
- [Groupes et provisionnement](/fr-FR/codex/enterprise/groups-and-provisioning)
- [Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions)
- [Contrôles des plugins](/fr-FR/codex/enterprise/apps-and-connectors)
- [Jetons d’accès](/fr-FR/codex/enterprise/access-tokens)
- [Comptes de service](/fr-FR/codex/enterprise/service-accounts)
- [Authentification](/fr-FR/codex/auth)
- [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration)
- [API de conformité et événements d’audit](/fr-FR/codex/enterprise/compliance-api)
