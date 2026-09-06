<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/chatgpt-work-cloud-security -->

ChatGPT Work fait partie de votre espace de travail ChatGPT existant et respecte les politiques
de confidentialité, de sécurité et de traitement des données qui s’y appliquent. Pour les espaces de travail
Business, Enterprise et Edu, les protections existantes comprennent le chiffrement en transit
et au repos, et OpenAI n’utilise pas les données professionnelles pour entraîner ses modèles
par défaut.

Work Cloud ajoute également l’exécution hébergée de tâches et des outils facultatifs capables
d’accéder à des systèmes connectés ou d’effectuer des actions autorisées. Examinez les autorisations,
les paramètres de conservation et les enregistrements d’audit disponibles pour les capacités
que votre organisation active.

Les capacités et les contrôles dépendent de l’offre de l’espace de travail, du déploiement, de la configuration
et de l’intégration connectée. Pour une vue plus générale du modèle d’exécution, consultez la
[Vue d’ensemble de ChatGPT Work](/fr-FR/codex/enterprise/chatgpt-work-overview).

## Sécurité en bref

- Les tâches dans le cloud s’exécutent sur une infrastructure gérée par OpenAI, et non sur l’appareil
de l’utilisateur.
- Une tâche dans le cloud n’hérite pas de l’accès aux fichiers locaux, aux applications de bureau,
aux sessions de navigateur ni aux réseaux privés de cet appareil.
- Les applications connectées utilisent les autorisations du compte autorisé, qui peut être
un compte individuel, partagé ou appartenant à un agent.
- Les contrôles de l’espace de travail et ceux propres à chaque fonctionnalité régissent l’accès à Work, l’exécution
locale, la navigation dans le cloud, les applications connectées et l’accès réseau du code ou du shell.
- Les données des espaces de travail Business, Enterprise et Edu sont chiffrées en transit et au
repos et ne sont pas utilisées par défaut pour entraîner les modèles OpenAI.
- La conservation et les informations accessibles à des fins d’audit dépendent de la catégorie de données, de l’emplacement de stockage,
de l’événement et de la configuration du produit applicable.

## Où s’exécutent les tâches dans le cloud

Les utilisateurs peuvent lancer des tâches dans le cloud depuis les interfaces web, mobile ou de bureau
de ChatGPT qui les prennent en charge. Sur le web et sur mobile, Work s’exécute dans le cloud. L’application de bureau peut
exécuter des tâches dans le cloud ou en local lorsque les autorisations correspondantes sont disponibles et
activées.

L’appareil de l’utilisateur se trouve dans le périmètre de confiance géré par le service informatique
de l’organisation, en dehors des systèmes exploités par OpenAI. Lancer une tâche dans le cloud depuis
l’application de bureau ne lui donne pas un accès direct à l’ordinateur de l’utilisateur.
L’exécution reste dans l’environnement géré par OpenAI, quelle que soit l’interface
utilisée pour la lancer.

Work Cloud utilise le harnais d’exécution des tâches de Codex. Work et Codex partagent les principaux
mécanismes d’exécution et d’isolation, mais leurs outils disponibles, leurs autorisations et
leurs contrôles d’administration ne sont pas identiques. Le client contrôle l’accès à l’espace de travail,
les connexions approuvées et les informations fournies intentionnellement à une tâche ;
OpenAI gère l’environnement d’exécution hébergé.

Work Cloud s’exécute sur une infrastructure partagée, gérée par OpenAI. Dans le mode d’exécution
actuellement pris en charge, les tâches s’exécutent dans des bacs à sable reposant sur des machines virtuelles, avec un état d’exécution
associé à l’utilisateur du compte authentifié dans l’espace de travail. Work peut réutiliser
un environnement pour plusieurs tâches ou le remplacer tout en conservant les données d’état éligibles à la conservation. Cela
ne signifie pas que chaque tâche reçoit un nouveau conteneur ni que chaque client dispose
d’un hôte physique dédié. Les clients ne fournissent, n’hébergent et ne gèrent pas les conteneurs
Work Cloud.

## Ce à quoi une tâche dans le cloud peut accéder

Une tâche dans le cloud peut utiliser les informations mises à sa disposition par une voie d’accès autorisée :

- Les informations qu’une personne saisit dans une conversation.
- Les fichiers importés intentionnellement, joints depuis la Bibliothèque ou mis à disposition
via un projet.
- Les contenus récupérés via une application activée et une connexion autorisée
à un compte.
- Le contenu des sites web consultés via un navigateur cloud activé ou une autre
fonctionnalité web autorisée, sous réserve des contrôles d’accès applicables.

Une tâche dans le cloud n’hérite pas directement de l’accès aux fichiers locaux, aux applications
installées ni à la session de navigateur de l’utilisateur. L’accès d’un appareil à un VPN
d’entreprise, à un site web interne ou à un réseau privé ne confère pas cet accès à la tâche
dans le cloud.

Une connexion autorisée peut rendre accessibles des informations d’un système interne
par sa propre voie d’accès. Cette connexion ne donne pas à la tâche dans le cloud
un accès sans restriction à l’appareil ou au réseau de l’employé.

## Applications, plugins et comptes connectés

Une application peut donner à Work accès à des informations ou à des actions dans un autre système. Un
plugin peut utiliser une application comme l’un de ses outils sous-jacents. Rendre un plugin disponible
n’active pas automatiquement l’application sous-jacente, n’autorise pas un compte et
n’approuve pas toutes les actions que l’intégration peut effectuer.

Une tâche qui utilise une application connectée, directement ou via un plugin, ne peut se poursuivre
que si les conditions suivantes sont réunies :

- L’application et tout plugin qui en dépend sont activés dans l’espace de travail.
- La personne dispose des droits d’accès nécessaires dans l’espace de travail ou au titre de son rôle.
- La connexion utilise un compte autorisé, qui peut être individuel, partagé ou appartenir
à un agent.
- Le compte connecté, les périmètres d’autorisation approuvés et les paramètres disponibles pour les actions de l’application
permettent d’accéder aux informations demandées ou d’effectuer l’opération demandée.

Pour les applications qui prennent en charge le **Contrôle des actions**, les administrateurs peuvent autoriser des actions
en lecture seule, toutes les actions ou un ensemble personnalisé. Les **Autorisations des applications** déterminent quand
ChatGPT demande une confirmation pour utiliser une application. Selon l’application et
l’espace de travail, les options peuvent inclure **Toujours demander**, **Toute modification**, **Actions
importantes** et **Ne jamais demander**. Avec **Toute modification**, les opérations de lecture prises en charge peuvent se poursuivre
sans demande de confirmation, tandis que les modifications nécessitent une confirmation.

Une opération d’écriture autorisée peut s’exécuter sans demande de confirmation lorsque la politique configurée
le permet. Cela n’élargit ni les actions autorisées de l’application, ni l’accès à l’espace de travail, ni les
autorisations du compte connecté. ChatGPT peut toujours bloquer certaines actions à haut
risque.

Vérifiez que le plugin et chacune des applications sous-jacentes sont disponibles dans l’espace de travail.
Examinez séparément les décisions relatives aux droits d’accès liés aux rôles,
à l’autorisation du compte connecté et aux autorisations d’action. Consultez les
[Contrôles des plugins](/fr-FR/codex/enterprise/apps-and-connectors).

### Connexions personnelles et partagées

Une connexion personnelle utilise les autorisations du compte de l’employé dans le système
source. Une connexion partagée ou appartenant à un agent utilise quant à elle les autorisations de son
compte connecté. Ce compte peut avoir accès à des informations ou effectuer
des actions auxquelles la personne à l’origine de la demande n’aurait pas accès avec un compte personnel.

Avant d’activer une connexion partagée, limitez les autorisations et les périmètres d’autorisation
du compte, choisissez qui peut l’utiliser et examinez les actions qu’il peut effectuer. Consultez
[Connexions et autorisations des agents d’espace de travail](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business).

Le contenu récupéré depuis une application connectée n’est pas automatiquement enregistré sous forme de fichier dans la Bibliothèque.
Si ce contenu est ensuite enregistré dans une conversation, un projet, la Bibliothèque ou
un index synchronisé, cette copie suit les règles de son emplacement d’enregistrement.

## Navigateur cloud et accès réseau

Le navigateur cloud, la recherche web, les applications connectées et l’accès réseau du code ou du shell sont
des capacités distinctes. Restreindre l’une ne désactive pas automatiquement les
autres.

### Navigateur cloud

Le navigateur cloud est un outil hébergé qu’une tâche Work peut utiliser pour interagir avec
des sites web. Ouvrir ChatGPT dans un navigateur web ou dans l’application de bureau n’active pas la navigation
dans le cloud ; une tâche dans le cloud peut s’exécuter sans cette fonctionnalité.

Le navigateur hébergé n’hérite pas du profil du navigateur local de l’utilisateur, de ses onglets ouverts,
de ses sessions déjà authentifiées, de ses mots de passe enregistrés, de son gestionnaire de mots de passe ni de son historique de navigation.
Lorsque cette fonctionnalité est prise en charge, les utilisateurs peuvent se connecter séparément via un parcours de connexion
hébergé et sécurisé. Cela ne donne pas accès à leur session de navigateur locale.

Les interactions avec les sites web prises en charge peuvent inclure l’utilisation de formulaires publics et combiner
des informations provenant d’une application autorisée avec une tâche sur un site web. Lorsqu’elles sont disponibles,
les autorisations pour les sites web comprennent **Toujours demander**, **Approuver automatiquement** et **Toujours
autoriser**. L’option **Approuver automatiquement** applique des contrôles de risque automatisés ; l’option **Toujours autoriser**
supprime l’examen interactif de l’accès au site web. Ni l’une ni l’autre n’accorde de nouvelles autorisations aux applications
ni n’approuve toutes les actions sur un site web. Les actions ayant des conséquences importantes peuvent
toujours nécessiter une confirmation distincte.

Pour qu’une tâche Work puisse utiliser le navigateur cloud dans un espace de travail Enterprise,
les administrateurs doivent activer à la fois l’accès à Work et l’accès au navigateur cloud. Consultez
[Utilisation du navigateur cloud dans ChatGPT](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt).

### Accès réseau pour le code et le shell

L’accès à l’Internet public pour l’exécution de code ou de commandes shell suit sa propre politique
réseau. Lorsque cet accès est désactivé, les destinations réseau nécessaires à
ChatGPT Work peuvent rester accessibles via une liste gérée de destinations autorisées.

La liste d’autorisation régit les destinations réseau, pas les commandes shell. Désactiver
l’accès à l’Internet public pour l’exécution de code ou de commandes shell ne désactive pas, à lui seul,
le navigateur cloud, la recherche web ni les applications connectées. Les modifications du paramètre
réseau prennent effet après la fin de l’exécution du code ou de la commande shell en cours et
l’actualisation de l’environnement d’exécution.

Consultez [Bac à sable pour le code et le shell](/fr-FR/codex/sandboxing?surface=web).

## Traitement et conservation des données

Work Cloud applique les mesures de protection de la confidentialité et de la sécurité
applicables à l’espace de travail ChatGPT, décrites ci-dessus. Consultez
[Confidentialité en entreprise](https://openai.com/enterprise-privacy/).

Les informations associées à une tâche dans le cloud ne suivent pas toutes le même calendrier
de conservation :

| Catégorie de données                        | Règles de conservation et de suppression                                                                                                                                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conversations Work                   | Sont soumises aux paramètres de conservation des conversations de l’espace de travail. La suppression définitive des discussions supprimées est généralement prévue sous 30 jours, sous réserve des exceptions publiées en matière de sécurité, d’obligations légales et de désidentification.                                                                                |
| État d’exécution hébergé et instantanés | Suivent un cycle de vie distinct de celui des conversations et des fichiers. L’accès à l’état d’exécution est limité à l’utilisateur du compte, et le paramètre de conservation des conversations de l’espace de travail est pris en compte pour les instantanés stockés éligibles. Terminer une tâche ou supprimer une discussion n’efface pas immédiatement tous les artefacts associés. |
| Fichiers enregistrés dans la Bibliothèque               | Les fichiers importés ou générés suivent les règles de conservation applicables à la Bibliothèque et à l’espace de travail. Supprimer une conversation ne supprime pas un fichier enregistré dans la Bibliothèque.                                                                                                                                      |
| Fichiers de projet                        | Restent associés à leur projet jusqu’à leur retrait ou à la suppression du projet, sous réserve des règles de suppression applicables.                                                                                                                                                                       |
| Mémoires enregistrées, lorsque la fonctionnalité est activée         | Relèvent de paramètres propres à la mémoire. La suppression d’une conversation ne supprime pas nécessairement une mémoire déjà enregistrée.                                                                                                                                                                             |
| Téléversements temporaires                    | Les fichiers temporaires éligibles téléversés dans Enterprise hors de la Bibliothèque peuvent expirer au bout de 48 heures, sauf si un autre paramètre de conservation s’applique.                                                                                                                                                      |
| Contenu des applications connectées                | Les enregistrements du système source sont soumis aux politiques de ce système. Les copies enregistrées dans une conversation, un projet, la Bibliothèque ou un index synchronisé sont soumises aux règles de leur emplacement de stockage.                                                                                                                         |
| Données du navigateur cloud                   | Les données du navigateur hébergé sont distinctes de celles du navigateur local. Les utilisateurs peuvent supprimer les cookies enregistrés dans le navigateur cloud à l’aide des paramètres correspondants.                                                                                                                                                    |
| Enregistrements de conformité                   | Les enregistrements de la plateforme de journaux de conformité sont disponibles pendant 30 jours. Les copies exportées sont soumises à la politique de conservation du système destinataire.                                                                                                                                                               |

Supprimer une conversation, un fichier de la Bibliothèque ou une mémoire enregistrée,
déconnecter une application et effacer les données du navigateur hébergé sont des actions distinctes.
Vérifiez l’emplacement de stockage concerné au lieu de supposer qu’une seule action supprime
toutes les copies. Consultez les
[politiques de conservation des discussions et des fichiers](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt).

Conserver un contexte de conversation et d’exécution adapté peut aider Work à reprendre
les tâches interrompues, à se référer aux étapes précédentes et à produire des résultats plus cohérents.
Réduire la durée de conservation ou supprimer les données peut limiter cette continuité. Choisissez donc des paramètres
qui concilient les exigences de sécurité et l’utilité du workflow.

Les espaces de travail Enterprise et Edu éligibles peuvent utiliser Enterprise Key Management pour
les contenus stockés pris en charge, notamment les instantanés d’exécution hébergée pris en charge lorsqu’un
chiffrement géré par le client est requis. La couverture varie selon la catégorie de données et le
déploiement. La rotation d’une clé ne supprime pas les données existantes et ne bloque pas, à elle seule,
l’accès aux contenus chiffrés antérieurement. Révoquer ou désactiver l’accès à la clé est une
action distincte qui peut perturber les workflows pris en charge. Aucune de ces actions ne remplace une
politique de conservation ou de suppression.

La résidence des données et la résidence de l’inférence ne s’appliquent qu’aux contenus éligibles et aux
charges de travail prises en charge, selon le contrat, la région et la
configuration de l’organisation. Les applications connectées, les fournisseurs externes et certains traitements ou
index synchronisés peuvent être soumis à des règles de localisation distinctes. Vérifiez la prise en charge pour le
produit, l’intégration et la région concernés. Consultez
[Résidence des données et résidence de l’inférence](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt).

La [politique de non-conservation des données](/api/docs/guides/your-data#zero-data-retention) de l’API OpenAI
est un contrôle propre à l’API et ne définit pas les règles de conservation des données dans ChatGPT Work.

## Contrôles d’accès pour les administrateurs

Examinez les contrôles qui s’appliquent à chaque composante d’une tâche dans le cloud :

- **Work Cloud et Work Local :** Lorsque des paramètres indépendants sont disponibles,
  gérez séparément Work dans le cloud et Work en local dans **Paramètres de l’espace de travail** \>
**Autorisations et rôles**. Dans d’autres espaces de travail, Work en local peut partager un paramètre
  avec Codex Local.
- **Applications et plugins :** Choisissez les intégrations disponibles et les
  personnes ou les rôles qui peuvent les utiliser.
- **Actions des comptes connectés :** Examinez les autorisations des comptes, les périmètres d’accès
  des applications et les paramètres d’action ou de confirmation disponibles.
- **Navigateur et réseau :** Évaluez séparément l’accès au navigateur cloud et l’accès au réseau public
  pour l’exécution de code ou de commandes shell.

Activez **Work Cloud** uniquement pour les utilisateurs ou les groupes approuvés. Lorsque des paramètres distincts sont disponibles pour
**Work Cloud** et **Work Local** , activez **Work Cloud**
et désactivez **Work Local** pour le rôle concerné afin d’autoriser Work dans le cloud sans
exécution locale. Lorsque Work en local et Codex partagent un même paramètre, examinez l’effet
sur les deux avant de désactiver l’exécution locale. Ces paramètres n’empêchent pas une
personne autorisée de téléverser volontairement un fichier dans une tâche dans le cloud.

Pour les autorisations de rôle prises en charge qui proposent les états **Par défaut**, **Activé** et **Désactivé** ,
**Par défaut** hérite du paramètre de l’espace de travail, **Activé** accorde l’accès et **Désactivé**
supprime l’accès accordé par ce rôle. Si un utilisateur a plusieurs rôles personnalisés, un autre
rôle peut toujours lui accorder l’accès. Certains paramètres de Work et des plugins utilisent des contrôles différents,
à deux états. Vérifiez les droits d’accès effectifs en tenant compte de tous les rôles attribués. Consultez
[Contrôle d’accès basé sur les rôles](https://help.openai.com/en/articles/11750701-rbac).

Lorsqu’elle est disponible, l’autorisation **Work Cloud** s’applique aux interfaces web,
mobiles et de bureau prises en charge. Elle ne permet pas, à elle seule, de sélectionner les
interfaces qui peuvent exécuter des tâches dans le cloud. Envisagez d’utiliser la gestion des appareils ou d’autres contrôles
d’accès si un déploiement doit exclure une interface particulière.

## Visibilité pour l’audit et la conformité

Pour les espaces de travail Enterprise et Edu éligibles, la plateforme de journaux de conformité peut
inclure les prompts et les réponses de Work pris en charge. Les appels aux applications connectées font l’objet de journaux distincts,
et les enregistrements d’audit disponibles dans le système source varient selon l’intégration.
Les points de terminaison de conformité pris en charge peuvent donner accès aux fichiers éligibles de la Bibliothèque.

La couverture dépend de l’événement et du système dans lequel il se produit. Ne supposez pas
que chaque commande shell, interaction avec le navigateur, appel à une application, opération sur un fichier ou
approbation figure dans un export de conformité accessible au client.

La surveillance des points de terminaison permet d’observer le client ChatGPT ou le trafic réseau sur les appareils gérés,
mais pas d’inspecter les actions à l’intérieur de l’environnement d’exécution hébergé. Utilisez
plutôt les enregistrements pris en charge pour Work, la conformité et les systèmes connectés.

Examinez la couverture actuelle des événements de conformité ainsi que les rapports de l’espace de travail,
les journaux d’audit des systèmes connectés et les politiques de conservation des systèmes qui reçoivent
les enregistrements exportés. Consultez la
[plateforme de conformité OpenAI](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

## Commencez par un projet pilote à petite échelle

Choisissez une tâche concrète pour un petit groupe. Par exemple, une équipe de sécurité pourrait
comparer un bulletin approuvé d’un fournisseur à un inventaire auquel elle est autorisée à accéder, puis examiner une
ébauche d’évaluation de l’exposition avant de décider de la marche à suivre. Si la navigation dans le cloud ou
les applications connectées ne sont pas disponibles, fournissez directement le bulletin et un extrait approuvé
de l’inventaire.

N’activez que les accès nécessaires à la tâche. Vérifiez les autorisations des comptes connectés,
les paramètres de conservation, les enregistrements d’audit disponibles et les étapes auxquelles une personne
doit examiner le résultat avant d’élargir l’accès. Pour planifier le déploiement, consultez le
[Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup).
