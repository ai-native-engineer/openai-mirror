<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/access-tokens -->

Les jetons d’accès Codex sont des identifiants d’espace de travail ChatGPT dont la portée est limitée aux autorisations Codex. Ils authentifient les workflows locaux de confiance et non interactifs, notamment les automatisations utilisant Codex CLI ou App Server, avec une identité d’espace de travail ChatGPT. Utilisez-les lorsqu’un script, une tâche planifiée ou un exécuteur CI a besoin d’un accès local reproductible.

  Les jetons d’accès Codex sont actuellement pris en charge dans les espaces de travail ChatGPT Business et
ChatGPT Enterprise.

Créez des jetons d’accès personnels dans la console d’administration ChatGPT, sur la page [Jetons d’accès](https://chatgpt.com/admin/access-tokens). Chaque jeton appartient à son créateur et à l’espace de travail ChatGPT de cet utilisateur. Les jetons servent d’identités d’agent pour les workflows locaux programmatiques. Pour les jetons créés depuis la page de détails d’une identité non humaine dédiée de l’espace de travail, consultez [Comptes de service](/fr-FR/codex/enterprise/service-accounts).

  Si une clé API de la plateforme convient à votre automatisation, continuez à utiliser l’authentification par clé API. Utilisez
les jetons d’accès Codex lorsqu’un workflow local de confiance nécessite spécifiquement un accès à l’espace de travail ChatGPT,
des droits gérés par l’espace de travail ou des contrôles d’entreprise.

  Vous devez déclencher depuis votre propre système un agent publié dans un espace de travail ChatGPT ? Ce
  workflow nécessite l’accès **Agents de l’espace de travail** . Un jeton limité à Codex ne peut pas
  authentifier les appels qui déclenchent un agent d’espace de travail. Si la boîte de dialogue de création du jeton propose
**Portées**, sélectionnez **Agents de l’espace de travail** pour déclencher un agent et **Codex** pour
  une automatisation Codex. N’accordez plusieurs portées que si le workflow a besoin de chacune
  d’elles. Consultez [Authentifiez-vous avec des jetons d’accès
  aux agents de l’espace de travail](/workspace-agents/authentication).

## Fonctionnement des jetons d’accès

Utilisez un jeton d’accès lorsque Codex CLI ou un client App Server doit fonctionner sans qu’un utilisateur ait à se connecter via un navigateur. Le jeton représente l’utilisateur de l’espace de travail ChatGPT qui l’a créé ; les exécutions peuvent ainsi utiliser les droits d’accès de cet utilisateur et figurer dans les données de gouvernance de l’espace de travail.

Au démarrage d’une exécution, le client vérifie le jeton et associe l’exécution à cette identité dans l’espace de travail. Traitez le jeton comme tout autre secret d’automatisation : stockez-le dans un gestionnaire de secrets, veillez à ce qu’il n’apparaisse pas dans les journaux et renouvelez-le conformément à la politique de votre organisation.

Utilisez les jetons d’accès pour :

- Des tâches `codex exec` exécutées par une automatisation de confiance.
- Des scripts locaux nécessitant des exécutions reproductibles et non interactives de Codex CLI.
- Des automatisations de confiance basées sur App Server.
- Des workflows d’entreprise qui associent l’utilisation à un utilisateur d’espace de travail ChatGPT plutôt qu’à une clé API d’organisation.

Principaux risques à éviter :

- **Fuite de secrets :** toute personne disposant du jeton peut lancer des exécutions locales via Codex CLI ou un client App Server sous l’identité du créateur du jeton. Stockez les jetons dans un gestionnaire de secrets, veillez à ce qu’ils n’apparaissent pas dans les journaux et renouvelez-les conformément à la politique de votre organisation.
- **Confiance accordée aux exécuteurs :** des environnements CI publics, des pull requests issues de forks ou des machines partagées peuvent exposer les jetons à des personnes extérieures à votre espace de travail. N’utilisez les jetons d’accès que sur des exécuteurs de confiance.
- **Identités partagées :** la réutilisation du jeton d’une personne par des équipes sans rapport entre elles complique l’identification des responsables et l’interprétation des pistes d’audit. Créez des jetons associés à un responsable de workflow précis.
- **Identifiants obsolètes :** les jetons à longue durée de vie peuvent rester actifs après la modification du workflow. Privilégiez les jetons à durée limitée et révoquez ceux qui ne sont plus utilisés.
- **Portée ou type d’identifiant inadapté :** l’automatisation Codex nécessite l’accès Codex,
  le déclenchement d’agents d’espace de travail nécessite l’accès Agents de l’espace de travail, et les appels généraux à l’API OpenAI
  nécessitent des clés API de la plateforme. Si **Portées** apparaît, accordez uniquement les
  autorisations nécessaires au workflow.

## Activez la création de jetons d’accès

Dans les paramètres de l’espace de travail, utilisez l’autorisation relative aux jetons d’accès pour permettre aux membres autorisés de créer des jetons d’accès.

L’autorisation relative aux jetons d’accès contrôle leur création. Elle ne donne accès ni à
l’application de bureau ChatGPT, ni à Codex CLI, ni à l’extension IDE, et ne modifie ni le
type de licence d’un membre, ni son rôle prédéfini dans l’espace de travail, ni son profil d’autorisations
d’exécution locale. Les workflows Codex CLI et App Server authentifiés par jeton nécessitent également
que l’utilisateur dispose de l’autorisation d’utiliser Codex en local.

Pour comprendre les relations entre ces contrôles, consultez
[Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions).

  
    
  

1. Demandez à un propriétaire de l’espace de travail d’ouvrir
[Paramètres de l’espace de travail \> Autorisations et rôles](https://chatgpt.com/admin/permissions).
2. Si la section **Jetons d’accès** apparaît, activez **Autoriser les utilisateurs à créer des
   jetons d’accès personnels**. Si cette section n’est pas disponible, activez **Autoriser
   les membres à utiliser les jetons d’accès Codex** dans **Codex et Work Local** ou
**Codex Local**.
3. Activez l’autorisation d’utilisation locale de Codex correspondant au responsable du workflow :
**Autoriser les membres à utiliser Codex et Work en local** dans **Codex et Work Local**,
   ou **Autoriser les membres à utiliser Codex en local** dans **Codex Local**. Lorsque **Work
   Local** dispose de sa propre section, **Utiliser Work en local** contrôle l’accès à Work et n’est pas
   nécessaire pour les jetons Codex.

Réservez la création de jetons d’accès aux personnes ou aux responsables de service qui connaissent l’emplacement de stockage du jeton, l’automatisation à laquelle il est destiné et son calendrier de renouvellement.

La désactivation de l’autorisation d’utiliser Codex en local suspend les jetons Codex actifs des membres
concernés ; elle ne les révoque pas. Le rétablissement de l’accès local à Codex réactive ces
jetons. Révoquez les jetons lorsque leur accès doit prendre fin définitivement.

## Définissez une durée de validité maximale pour les jetons d’accès

Un propriétaire de l’espace de travail peut définir la durée de validité maximale que les membres peuvent choisir
pour les nouveaux jetons d’accès. Ouvrez
[Paramètres de l’espace de travail \> Autorisations et rôles](https://chatgpt.com/admin/permissions).
Si la section **Jetons d’accès** apparaît, définissez-y la **Durée de validité maximale des jetons d’accès**.
Sinon, recherchez ce paramètre dans **Codex et Work Local** ou
**Codex Local**.

  
    
  

La limite s’applique aux nouveaux jetons d’accès. Les jetons existants conservent leur durée de validité actuelle.

## Créez un jeton d’accès

Utilisez la page Jetons d’accès pour nommer le jeton, examiner les éventuelles portées disponibles par produit
et choisir une durée de validité adaptée.

1. Accédez à [Jetons d’accès](https://chatgpt.com/admin/access-tokens).
2. Sélectionnez **Créer**.

  
    
  

3. Saisissez un nom descriptif, comme `release-ci` ou `nightly-docs-check`.

  
    
  

4. Si la boîte de dialogue affiche **Portées**, sélectionnez **Codex**. Sélectionnez **Agents
   de l’espace de travail** uniquement si le même workflow doit aussi déclencher un agent d’espace de travail.
   Si la boîte de dialogue ne comporte pas de sélecteur de portée, elle crée un jeton limité à Codex.
5. Choisissez une durée de validité limitée, par exemple 7, 30, 60 ou 90 jours. Les jetons d’accès personnels
   à portée définie doivent expirer. Une ancienne version de la boîte de dialogue réservée à Codex
   peut proposer **Aucune expiration** ; évitez cette option, sauf si votre organisation
   l’approuve et renouvelle le jeton selon un calendrier défini.
6. Sélectionnez **Créer**.
7. Copiez immédiatement le jeton d’accès généré. Vous ne pourrez plus le consulter après
avoir fermé la boîte de dialogue.
8. Stockez le jeton dans votre gestionnaire de secrets ou dans le stockage de secrets de votre CI.

La durée de validité personnalisée minimale est d’un jour. Vous ne pouvez pas utiliser de jetons révoqués ou expirés pour lancer de nouvelles exécutions authentifiées.

## Utilisez un jeton d’accès avec Codex CLI

Si la boîte de dialogue de création du jeton indique une version requise de Codex CLI, mettez à jour la CLI
vers cette version ou une version ultérieure avant d’utiliser le jeton.

Pour une automatisation éphémère, stockez le jeton dans `CODEX_ACCESS_TOKEN` et exécutez Codex CLI normalement :

```bash

codex exec --json "review this repository and summarize the top risks"

Pour une connexion locale persistante, transmettez le jeton à `codex login --with-access-token` via un pipe :

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "summarize the last release diff"

`codex login --with-access-token` enregistre un identifiant associé à une identité d’agent dans le stockage d’authentification de Codex CLI. Si vous préférez ne pas conserver d’identifiants sur la machine, utilisez plutôt la variable d’environnement `CODEX_ACCESS_TOKEN`.

`codex app-server` peut utiliser le même identifiant via `CODEX_ACCESS_TOKEN` ou
une connexion créée avec `codex login --with-access-token` pour authentifier ses requêtes
OpenAI. Cet identifiant est distinct de celui utilisé pour l’authentification du transport
entre le client et App Server. Pour une connexion WebSocket distante, configurez un
jeton distinct de type bearer ou de capacité, comme décrit dans
[App Server](/fr-FR/codex/app-server) ; ne réutilisez pas le jeton d’accès Codex comme
jeton de transport. Consultez
[Variables d’environnement d’authentification et de réseau](/fr-FR/codex/config-file/environment-variables#authentication-and-network).

## Renouvelez ou révoquez un jeton

Renouvelez les jetons d’accès de la même manière que les autres secrets d’automatisation :

1. Créez un jeton de remplacement.
2. Mettez à jour le secret dans l’exécuteur, le planificateur ou le gestionnaire de secrets.
3. Effectuez un test de bon fonctionnement avec le nouveau jeton.
4. Révoquez l’ancien jeton depuis [Jetons d’accès](https://chatgpt.com/admin/access-tokens).

Depuis la page Jetons d’accès, les propriétaires et administrateurs de l’espace de travail peuvent révoquer n’importe quel jeton de l’espace de travail. Les membres disposant de l’autorisation relative aux jetons d’accès peuvent uniquement révoquer les jetons qu’ils ont créés.

## Modèle d’autorisations

L’autorisation relative aux jetons d’accès de l’espace de travail contrôle la création de jetons. Selon
l’organisation de l’espace de travail, le paramètre **Autoriser les membres à utiliser Codex et Work en local** dans la section
**Codex et Work en local**, ou **Autoriser les membres à utiliser Codex en local** dans la section **Codex
en local**, contrôle l’accès à Codex en local. Si **Work en local** dispose de sa propre section,
le paramètre **Utiliser Work en local** contrôle l’accès à Work et n’accorde pas l’accès à Codex. Un membre
doit disposer à la fois de l’accès à Codex en local et de l’autorisation relative aux jetons d’accès pour les workflows Codex
authentifiés par jeton. Un membre peut avoir accès à Codex en local sans être autorisé à
créer des jetons d’accès.

| Fonctionnalité                                                    | Propriétaires et administrateurs de l’espace de travail                      | Membre disposant de l’autorisation relative aux jetons d’accès           | Membre ne disposant pas de l’autorisation relative aux jetons d’accès |
| ------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------- | -------------------------------------- |
| Ouvrir [Jetons d’accès](https://chatgpt.com/admin/access-tokens) | Oui                                              | Oui                                           | Non                                     |
| Créer des jetons d’accès                                          | Oui, pour leur propre identité dans l’espace de travail ChatGPT    | Oui, pour leur propre identité dans l’espace de travail ChatGPT | Non                                     |
| Consulter la liste des jetons d’accès                                            | Liste des jetons de l’espace de travail, indiquant qui a créé chaque jeton | Uniquement les jetons créés par ce membre                      | Non                                     |
| Révoquer des jetons d’accès depuis la page Jetons d’accès              | N’importe quel jeton de l’espace de travail                       | Uniquement les jetons créés par ce membre                      | Aucun accès à la page                         |
| Accorder ou retirer l’autorisation relative aux jetons d’accès                       | Propriétaire de l’espace de travail uniquement                             | Non                                            | Non                                     |
| Gérer les autres paramètres des clients locaux ou de Codex Cloud             | Oui, en fonction des autorisations d’administration de l’espace de travail        | Non, sauf si un propriétaire accorde l’accès             | Non                                     |

En bref : les propriétaires et administrateurs de l’espace de travail gèrent les accès au niveau de l’espace de travail.
Les membres doivent disposer de l’autorisation relative aux jetons d’accès pour créer et gérer leurs propres jetons,
mais cette autorisation ne leur accorde ni droits d’administration ni accès
aux jetons des autres membres.

## Dépannage

### La page Jetons d’accès renvoie une erreur 404 ou un refus d’accès

Demandez à un propriétaire de l’espace de travail de vérifier que votre rôle comprend l’autorisation **Autoriser les utilisateurs à
créer des jetons d’accès personnels** ou **Autoriser les membres à utiliser les jetons d’accès
Codex**, selon l’interface disponible. Pour un workflow Codex authentifié
par jeton, vérifiez également que le paramètre **Autoriser les membres à utiliser Codex et Work
en local** ou **Autoriser les membres à utiliser Codex en local** est activé.

### Échec de `codex login --with-access-token`

Vérifiez que vous avez copié le jeton d’accès généré, et non un jeton de session du navigateur
ou une clé API de la plateforme. Vérifiez également que le jeton est actif, qu’il n’a pas expiré
et qu’il appartient à un utilisateur disposant de l’autorisation requise pour utiliser Codex en local.

## Documentation associée

- [Authentification](/fr-FR/codex/auth)
- [Comptes de service](/fr-FR/codex/enterprise/service-accounts)
- [Mode non interactif](/fr-FR/codex/non-interactive-mode)
- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
- [Groupes et provisionnement](/fr-FR/codex/enterprise/groups-and-provisioning)
- [Gestion du cycle de vie des utilisateurs](/fr-FR/codex/enterprise/user-lifecycle)
- [Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions)
- [Gouvernance](/fr-FR/codex/enterprise/governance)
