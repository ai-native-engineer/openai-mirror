<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/chatgpt-work-overview -->

ChatGPT Work et Codex partagent les mêmes mécanismes fondamentaux d’exécution, d’isolation et de gestion des autorisations, et relèvent du même périmètre de sécurité prévu par votre contrat ChatGPT Business ou Enterprise. Les fonctionnalités et les contrôles disponibles dans chaque expérience dépendent de l’exécution de la tâche en local ou dans le cloud, des outils dont elle dispose et des politiques applicables à l’espace de travail.

ChatGPT Work peut accomplir des tâches comportant plusieurs étapes en utilisant les informations, les fichiers, les applications et les outils accessibles à un membre autorisé de l’espace de travail. Sur le web, ces tâches s’exécutent dans le cloud et non sur l’appareil du membre.

Cette vue d’ensemble explique le périmètre d’exécution, les contrôles réseau et applicatifs, le traitement des données et l’exécution sécurisée des tâches avec ChatGPT Work sur le web. La disponibilité et les contrôles d’administration dépendent de votre offre et de la configuration de votre espace de travail.

Pour des précisions sur l’exécution hébergée, les autorisations des comptes connectés,
les paramètres du navigateur et du réseau, la conservation des données et les informations disponibles pour les audits, consultez
[Sécurité de ChatGPT Work dans le cloud](/fr-FR/codex/enterprise/chatgpt-work-cloud-security).

Pour en savoir plus sur l’accès à l’appareil, les sessions de navigation locales, les politiques gérées et le traitement
des données locales, consultez
[Sécurité de ChatGPT Work en local](/fr-FR/codex/enterprise/chatgpt-work-local-security).

## Isolation de l’exécution, fichiers et accès à l’appareil

Les fichiers et les outils accessibles à ChatGPT Work dépendent de l’emplacement où Work s’exécute, des autorisations de l’utilisateur et de la configuration définie par les administrateurs.

### Work en local

Work en local exécute les tâches sur l’appareil de l’utilisateur via l’application de bureau ChatGPT. Il peut accéder aux fichiers locaux, aux applications et aux autres ressources mises à sa disposition, sous réserve des autorisations de l’utilisateur, des contrôles applicables à l’espace de travail et des politiques de sécurité de l’appareil. Contrairement à Work sur le Web, Work en local peut utiliser des ressources qui restent sur votre ordinateur, sans vous obliger à importer des fichiers dans une conversation dans le cloud.

### Work dans le cloud

Work dans le cloud est disponible sur les interfaces web, mobiles et de bureau compatibles. Il exécute le harnais Codex dans un environnement isolé sur une infrastructure gérée par OpenAI. Les conversations dans le cloud peuvent se synchroniser entre ces interfaces, et les tâches prises en charge peuvent se poursuivre lorsque l’utilisateur s’absente de la conversation.

Work sur le web ne peut pas accéder directement aux fichiers, aux applications ni aux onglets de navigateur ouverts sur l’ordinateur de l’utilisateur. Celui-ci peut fournir des fichiers en les important, en les ajoutant à un projet compatible ou en utilisant une application connectée autorisée. L’application de bureau contrôle l’accès aux fichiers et aux applications locaux au moyen de ses propres autorisations.

Lorsque
la [Bibliothèque](https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt)
est disponible, les fichiers importés ou générés éligibles peuvent y être enregistrés.
Les administrateurs peuvent définir si ChatGPT se réfère automatiquement aux fichiers enregistrés
dans la Bibliothèque. La désactivation des références automatiques n’empêche pas les utilisateurs
d’accéder explicitement aux fichiers qu’ils sont autorisés à utiliser ou de les joindre.

Consultez [Bac à sable pour le code et le shell](/fr-FR/codex/sandboxing?surface=web),
[Création et modification de documents, de feuilles de calcul et de présentations](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work),
ainsi que
[Stockage de fichiers et Bibliothèque dans ChatGPT](https://help.openai.com/en/articles/20001052-library-for-chatgpt).

## Accès réseau et destinations externes

Pour accomplir des tâches, Work utilise des outils tels que l’exécution de code ou de commandes shell et le navigateur cloud. Les autorisations de chacun de ces outils sont configurables.

- **Code et commandes shell** : l’accès à l’Internet public dépend de la politique
  applicable à l’espace de travail et du paramètre réseau individuel de Work. Lorsque l’accès
  à l’Internet public n’est pas autorisé, les commandes peuvent toujours atteindre les destinations approuvées par OpenAI
  nécessaires au fonctionnement de Work. Ce paramètre contrôle les destinations réseau,
  et non les commandes qui peuvent être exécutées.
- **Recherche web** : la recherche dispose de contrôles distincts du paramètre d’accès réseau
  pour le code et le shell dans Work.

Lorsqu’il est disponible, le paramètre individuel d’accès réseau pour le code et le shell se trouve dans
**Paramètres** \> **Contrôles des données** \> **Accès réseau de Work**. Activer **Autoriser l’accès
à l’Internet public** ne permet pas de contourner une restriction imposée par un
administrateur. Désactiver ce paramètre limite l’accès du code et des commandes shell aux
destinations requises de la liste d’autorisation gérée ; cela ne désactive ni les applications
connectées, ni la recherche web, ni le navigateur cloud.

Les modifications du paramètre d’accès réseau pour le code et le shell prennent effet une fois l’exécution en cours
terminée et après que Work a actualisé son environnement d’exécution. Consultez
[Bac à sable pour le code et le shell](/fr-FR/codex/sandboxing?surface=web) et
[Contrôles d’accès à Work](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Les contrôles des interactions sortantes sont distincts des
[restrictions d’accès IP de l’espace de travail](https://help.openai.com/en/articles/12111596-ip-allowlisting-for-chatgpt),
qui limitent l’accès entrant à l’espace de travail ChatGPT ou à l’API de conformité.

## Navigateur cloud et accès aux sites web

Le
[Navigateur cloud](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
est l’un des outils que ChatGPT Work peut utiliser et se distingue du
[Navigateur intégré](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app).
Il fonctionne à distance et utilise une session de navigation distincte de celle du navigateur
local de l’utilisateur. Il ne peut accéder ni aux onglets locaux, ni aux extensions, ni à l’historique de navigation,
ni aux mots de passe enregistrés, ni aux sessions locales authentifiées.

Le navigateur cloud peut parcourir des sites web publics, saisir des informations dans les formulaires publics pris en charge et s’appuyer sur les informations pertinentes d’une application approuvée pour réaliser une tâche sur un site web. L’authentification sur les sites web via le navigateur cloud n’est pas disponible dans les espaces de travail Enterprise ou Edu. La disponibilité du navigateur dépend de votre offre, de votre région, de son déploiement et des autorisations de l’espace de travail. Pour les espaces de travail Enterprise, un administrateur doit activer l’accès au navigateur cloud en plus de l’accès à Work.

L’accès aux sites web et les actions réalisées sur ceux-ci font l’objet de contrôles distincts :

- Par défaut, ChatGPT demande une autorisation avant de visiter un nouveau site web. Lorsque ces
  options sont disponibles, les utilisateurs peuvent sélectionner **Toujours demander**, **Approbation automatique** ou **Toujours autoriser**, et autoriser ou
  bloquer chaque site web individuellement. L’option **Approbation automatique** applique des contrôles automatisés des risques.
L’option **Toujours autoriser** supprime la révision interactive de l’accès aux sites web. Les administrateurs
  peuvent également limiter les paramètres d’approbation des utilisateurs (par exemple,
  désactiver **Toujours autoriser** pour l’ensemble de l’espace de travail).
- Autoriser un site web n’équivaut pas à approuver toutes les actions effectuées sur ce site. ChatGPT peut demander une confirmation distincte avant des actions susceptibles d’entraîner un engagement financier, juridique, lié à un compte ou ayant d’autres conséquences importantes.

Dans une conversation Work, les utilisateurs peuvent consulter les captures d’écran des pages et revoir la session de navigation, lorsque ces éléments sont disponibles. Ces éléments visibles par l’utilisateur ne signifient pas qu’ils sont exportés via l’API de conformité, ni qu’un historique d’exécution complet est accessible aux administrateurs.

Consultez
[Utilisation du navigateur cloud dans ChatGPT](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
et [Navigateur](/fr-FR/codex/browser?surface=web).

## Applications connectées, identifiants et autorisations

Une application connectée ou un Plugin ne permet à Work d’accéder aux ressources que par l’intermédiaire de l’intégration autorisée par votre espace de travail et dans la limite des autorisations accordées pour cette connexion. Depuis le tableau de bord d’administration, les administrateurs peuvent contrôler la disponibilité des Plugins et des applications, l’accès associé aux rôles de l’espace de travail, l’autorisation externe, les paramètres des actions et les autorisations du système source.

Dans les espaces de travail Enterprise et Edu, les plugins et leurs applications sous-jacentes sont désactivés par défaut. Dans les espaces de travail Business, les plugins et les applications sont activés par défaut. Rendre un plugin disponible n’active pas automatiquement l’application dont il dépend et n’accorde pas d’accès à un compte. La connexion requise doit être autorisée pour un compte individuel, partagé ou appartenant à un agent avant que ChatGPT Work puisse y accéder. Une connexion partagée ou appartenant à un agent utilise les autorisations du compte connecté dans le système source, qui peuvent différer de celles de l’utilisateur à l’origine de la demande.

Lorsque cette fonctionnalité est prise en charge, les administrateurs peuvent limiter une application à des actions en lecture seule ou à un ensemble d’actions approuvées. Les paramètres d’autorisation de l’application peuvent aussi déterminer si ChatGPT demande une confirmation avant d’utiliser une application, d’apporter des modifications ou d’effectuer des actions importantes. Toutes les applications ne proposent pas les mêmes contrôles d’action, et toutes les actions n’exigent pas une confirmation humaine individuelle.

Avec les applications synchronisées, les modifications du contenu source ou des autorisations peuvent prendre un certain temps avant d’apparaître. Déconnecter une application ne supprime pas automatiquement les informations déjà enregistrées dans une conversation, un fichier généré ou un enregistrement régi par sa propre politique de conservation.

Consultez
[Contrôles d’administration, sécurité et conformité pour les plugins et les applications](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business),
[Contrôles des plugins](/fr-FR/codex/enterprise/apps-and-connectors),
[Configuration de Google Workspace gérée par les administrateurs](https://help.openai.com/en/articles/10929079-google-workspace-admin-managed-setup),
ainsi que [Applications ChatGPT avec synchronisation](https://help.openai.com/en/articles/10847137-chatgpt-apps-with-sync).

## Confidentialité et traitement des données

ChatGPT Work respecte les politiques de confidentialité, de sécurité et de traitement des données applicables à votre espace de travail ChatGPT. Les conversations, les fichiers importés ou générés, les applications connectées et les données du navigateur peuvent être soumis à des règles de conservation et de suppression différentes.

Pour en savoir plus, consultez [Confidentialité en entreprise](https://openai.com/enterprise-privacy/),
[Politiques de conservation des discussions et des fichiers](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt),
[Résidence des données et de l’inférence](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt),
ainsi que la [FAQ d’administration de ChatGPT Work](/fr-FR/codex/enterprise/work-admin-faq).

### La conservation dépend du type de données

- **Conversations Work :** elles sont soumises aux paramètres de conservation et de suppression
  des conversations applicables à l’espace de travail ChatGPT.
- **Fichiers enregistrés dans la Bibliothèque :** ils sont soumis aux règles de conservation
  applicables aux fichiers et à l’espace de travail. Supprimer une conversation ne supprime pas les fichiers stockés
  dans la Bibliothèque.
- **Fichiers de projet :** ils restent associés au projet jusqu’à sa suppression, sous réserve
  des règles et des exceptions applicables en matière de suppression.
- **Fichiers importés temporairement hors de la Bibliothèque :** pour Enterprise, ces fichiers peuvent
  expirer après 48 heures, sauf si un autre paramètre de conservation s’applique.
- **Mémoires enregistrées, lorsqu’elles sont activées :** elles sont soumises à des contrôles de mémoire distincts.
- **Cookies du navigateur cloud :** ils restent distincts des données du navigateur local. Les utilisateurs peuvent
  les effacer depuis les paramètres du navigateur cloud.
- **Enregistrements de la plateforme de journaux de conformité :** ils restent disponibles
  sur la plateforme pendant 30 jours. Les copies exportées suivent la politique de conservation du système destinataire.
- **Données des applications connectées :** les enregistrements sources sont soumis aux politiques
  de l’application connectée. Les copies enregistrées dans une discussion, un fichier ou un index synchronisé sont également soumises
  aux règles de stockage et de conservation applicables d’OpenAI.

Supprimer une conversation, mettre fin à une tâche Work, effacer les cookies du navigateur et conserver les enregistrements de conformité sont des opérations distinctes. Lorsqu’une discussion est supprimée, elle disparaît de l’interface et sa suppression définitive est programmée dans un délai de 30 jours, sous réserve des exceptions publiées concernant la sécurité, les obligations légales et la désidentification.

Consultez
[Politiques de conservation des discussions et des fichiers](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt),
[Mémoire dans ChatGPT](https://help.openai.com/en/articles/8590148-memory-in-chatgpt-faq),
ainsi que la
[plateforme de conformité OpenAI](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).
