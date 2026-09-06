<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/chatgpt-work-local-security -->

ChatGPT Work peut utiliser les fichiers, applications et sessions de navigateur approuvés sur l’ordinateur d’un utilisateur pour exécuter des tâches locales. L’accès dépend des autorisations de l’espace de travail, des droits d’accès dont dispose déjà l’utilisateur avec son compte, des autorisations du système d’exploitation, des approbations des applications et des politiques de gestion des appareils prises en charge.

Les fonctionnalités locales dépendent de l’application de bureau prise en charge, du système d’exploitation, des droits accordés à l’espace de travail, des autorisations des rôles, de la politique de gestion de l’appareil et du déploiement du produit.

## La sécurité en bref

- Les tâches locales s’exécutent via l’application de bureau ChatGPT. Ouvrir une tâche hébergée dans le cloud dans cette même application ne la transforme pas en tâche locale.

- Les contrôles disponibles pour Work en local et en environnement hébergé dépendent de la configuration de l’espace de travail et du déploiement.

- L’accès aux fichiers, l’Utilisation de l’ordinateur, les navigateurs et les applications connectées reposent sur des autorisations et des approbations distinctes.

- Un navigateur ou une application déjà connecté à un système de l’entreprise peut permettre d’agir avec les autorisations de ce compte.

- Les politiques prises en charge sur les appareils gérés peuvent restreindre les fonctionnalités locales sans remplacer les contrôles d’accès de l’espace de travail.

- Les données des espaces de travail Business, Enterprise et Edu traitées par les services OpenAI couverts sont chiffrées en transit et au repos et ne servent pas, par défaut, à entraîner les modèles OpenAI.

- Les fichiers locaux, le contexte des tâches, les données des navigateurs, les enregistrements des systèmes connectés et les événements d’audit peuvent suivre des règles de stockage et de conservation différentes.

## Lieu d’exécution des tâches locales

Work Local accède aux ressources approuvées via l’application de bureau sur l’ordinateur de l’utilisateur. Work Cloud s’exécute sur une infrastructure gérée par OpenAI, même lorsqu’il est ouvert depuis la même application de bureau.

Les fichiers locaux peuvent rester sur l’appareil, mais les extraits de fichiers, prompts, captures d’écran, contenus de navigateur ou résultats d’outils pertinents peuvent être envoyés aux services OpenAI pour accomplir une tâche. L’exécution locale ne signifie pas que l’inférence du modèle se fait hors ligne ou exclusivement sur l’appareil.

## Accès aux fichiers et à l’appareil

Une tâche locale peut exploiter les informations fournies ou mises à disposition par l’utilisateur, notamment les fichiers pris en charge, le contenu des applications, les sessions de navigateur et les systèmes connectés autorisés. L’accès dépend des privilèges existants de l’utilisateur et des contrôles qui régissent la fonctionnalité concernée.

Accorder l’accès à Work en local n’approuve pas automatiquement toutes les applications, n’accorde pas de droits d’administrateur et ne permet pas de contourner les autorisations du compte utilisé pour accéder à un autre système. Une connexion partagée approuvée peut disposer de privilèges différents de ceux du compte personnel de l’utilisateur.

## Utilisation de l’ordinateur et approbations des applications

La fonctionnalité [Utilisation de l’ordinateur](/fr-FR/codex/computer-use) ne peut interagir avec les applications de bureau prises en charge que si elle est disponible, si les autorisations requises du système d’exploitation ont été accordées et si l’utilisateur autorise l’application. Selon les options disponibles, l’approbation peut s’appliquer à la session en cours ou aux tâches futures.

Sur macOS, l’autorisation Enregistrement de l’écran permet à la fonctionnalité Utilisation de l’ordinateur de voir le contenu des applications, et l’autorisation Accessibilité lui permet de cliquer, de saisir du texte et de naviguer. Les tâches macOS prises en charge peuvent s’exécuter en arrière-plan. Sur Windows, la fonctionnalité Utilisation de l’ordinateur agit sur le bureau actif et visible et ne peut pas s’exécuter en arrière-plan pendant que l’utilisateur continue d’utiliser cette même session.

Les utilisateurs peuvent arrêter une tâche à tout moment. La fonctionnalité Utilisation de l’ordinateur ne peut pas approuver les demandes de sécurité du système d’exploitation, s’authentifier en tant qu’administrateur, ni automatiser les applications de terminal ou ChatGPT lui-même.

### Appareils verrouillés

Les configurations macOS prises en charge peuvent proposer une option permettant à une tâche approuvée utilisant la fonctionnalité Utilisation de l’ordinateur de se poursuivre lorsque le Mac est verrouillé. La disponibilité dépend de la version de l’application, du déploiement de la fonctionnalité, des exigences applicables et de l’éligibilité au contrôle à distance.

Les administrateurs peuvent désactiver le fonctionnement sur un appareil verrouillé au moyen d’une configuration gérée prise en charge. Sur Windows, la fonctionnalité Utilisation de l’ordinateur nécessite un bureau actif et déverrouillé ; le fonctionnement sur un appareil macOS verrouillé n’implique pas une prise en charge équivalente sur Windows.

## Sessions de navigateur et comptes déjà connectés

Work Local n’a pas automatiquement accès à tous les navigateurs ni à tous les comptes de l’entreprise. L’accès dépend du navigateur utilisé, du compte connecté et des approbations requises pour cette interface de navigation.

| Mode d’accès au navigateur                                | Session et périmètre de sécurité                                                                                                                                                                                                 |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Navigateur intégré à l’application de bureau](/fr-FR/codex/browser)    | Utilise un profil de navigateur distinct de celui du navigateur habituel de l’utilisateur. L’utilisateur peut se connecter dans ce profil, et l’accès aux sites web pris en charge peut nécessiter une approbation. Le navigateur intégré ne peut pas automatiser l’envoi de fichiers.              |
| [Extension Chrome](/fr-FR/codex/chrome-extension) | Peut interagir avec les onglets et les comptes existants du navigateur lorsque l’extension et l’accès aux sites web sont approuvés. Les utilisateurs peuvent approuver un site pour une seule utilisation ou autoriser les accès futurs ; l’accès à l’historique de navigation et aux fichiers locaux nécessite un examen distinct. |
| Pilotage d’un navigateur avec la fonctionnalité Utilisation de l’ordinateur            | Utilise un navigateur approuvé en tant qu’application de bureau, avec les comptes qui y sont déjà connectés. Les autorisations du système d’exploitation, l’approbation de l’application et les autorisations du compte existant restent applicables.               |

Les options d’approbation des sites web et les confirmations d’actions sensibles varient selon l’interface de navigation. Autoriser tous les sites réduit le nombre de demandes d’approbation ultérieures ; les utilisateurs devraient donc examiner ce choix avant d’activer cette option.

Un navigateur hébergé dans le cloud est distinct des navigateurs locaux de l’utilisateur et n’hérite pas automatiquement de leurs connexions existantes. Les workflows cloud pris en charge peuvent demander une connexion distincte, autorisée par l’utilisateur.

## Applications, plugins et comptes connectés

Une application connectée peut donner accès à des informations ou à des actions dans un autre système. Un plugin peut utiliser une application comme outil sous-jacent. La mise à disposition d’un plugin n’active pas automatiquement l’application requise, n’autorise pas un compte et ne permet pas toutes les actions.

La disponibilité des plugins et des applications dépend de l’offre et de la configuration de l’espace de travail. La [vue d’ensemble de ChatGPT Work](/fr-FR/codex/enterprise/chatgpt-work-overview) indique que les plugins et leurs applications sous-jacentes sont désactivés par défaut pour les espaces de travail Enterprise et Edu, et activés par défaut pour les espaces de travail Business. Vérifiez les paramètres effectifs pour l’espace de travail et l’interface du produit concernés.

Avant qu’une tâche n’utilise un système connecté, vérifiez que l’espace de travail autorise l’application et tout plugin requis, que la connexion est autorisée et que le compte connecté peut accéder aux informations demandées ou effectuer l’action souhaitée. Les paramètres d’accès en lecture seule, les actions autorisées et les exigences de confirmation varient selon l’intégration.

Les plugins réservés à l’application de bureau, les outils locaux et les autres fonctionnalités fournies localement peuvent suivre des procédures d’installation ou d’approbation différentes. Ne supposez pas que tous les outils locaux suivent la même procédure d’approbation par l’administrateur.

### Connexions personnelles et partagées

Une connexion personnelle utilise les autorisations de l’utilisateur connecté dans le système source. Une connexion partagée ou appartenant à un agent utilise les autorisations du compte connecté, qui peuvent être plus étendues que les droits d’accès de l’utilisateur lui-même.

Limitez les comptes partagés aux données et aux actions nécessaires, restreignez leur utilisation aux personnes autorisées et appliquez les contrôles d’action ou de confirmation pris en charge. Les enregistrements du système connecté restent soumis aux autorisations et aux politiques de conservation de ce système.

## Accès administrateur et politiques applicables aux appareils gérés

Examinez les contrôles de Work disponibles dans **Paramètres de l’espace de travail** \> **Autorisations et rôles**. L’affichage d’autorisations distinctes pour Work en local et en environnement hébergé dépend de la configuration de l’espace de travail et du déploiement. Pour en savoir plus, consultez la [FAQ Work pour les administrateurs](/fr-FR/codex/enterprise/work-admin-faq).

N’activez que les environnements d’exécution approuvés pour chaque utilisateur ou groupe, puis vérifiez les droits d’accès effectifs après les modifications.

Les autorisations de l’espace de travail déterminent qui peut utiliser Work. Les administrateurs peuvent également restreindre les fonctionnalités de bureau prises en charge au moyen d’exigences imposées définies dans `requirements.toml`. Selon le déploiement, ces exigences peuvent être distribuées via une configuration gérée par l’espace de travail, un fichier de configuration au niveau du système ou des outils de gestion des appareils mobiles macOS pris en charge.

Les utilisateurs ne peuvent pas déroger aux exigences imposées. En revanche, les valeurs par défaut gérées définissent des paramètres initiaux que les utilisateurs peuvent éventuellement modifier. Ni les unes ni les autres ne remplacent les rôles de l’espace de travail ou les autorisations du système d’exploitation.

| Paramètre géré                                       | Objectif de sécurité                                                             |
| ----------------------------------------------------- | ---------------------------------------------------------------------------- |
| `features.computer_use = false`                       | Désactivez les capacités prises en charge de la fonctionnalité Utilisation de l’ordinateur.                                 |
| `allow_appshots = false`                              | Empêchez les captures Appshot prises en charge.                                           |
| `features.in_app_browser = false`                     | Désactivez le navigateur intégré de l’application de bureau.                                  |
| `features.browser_use = false`                        | Désactivez l’automatisation du navigateur prise en charge ; examinez séparément les autres modes d’accès au navigateur. |
| `features.apps = false` ou `features.plugins = false` | Restreignez les applications connectées ou les plugins pris en charge.                        |
| `computer_use.allow_locked_computer_use = false`      | Bloquez les fonctions prises en charge d’Utilisation de l’ordinateur lorsqu’un Mac est verrouillé.                        |

Les paramètres et les modes de distribution disponibles dépendent du client, du système d’exploitation, de l’espace de travail et de la configuration du déploiement. Validez les restrictions sur un appareil géré représentatif. Pour connaître les paramètres de politique pris en charge, voir des exemples de configuration et obtenir les instructions de configuration MDM, consultez la section [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration).

## Réseau local et ressources privées

Une tâche peut accéder aux informations de l’entreprise par différents moyens, notamment le navigateur d’un appareil, une application de bureau approuvée ou une application connectée. Les contrôles existants au niveau de l’appareil, du proxy, du VPN, du système source et du point de terminaison peuvent s’appliquer différemment à chacun de ces modes d’accès.

L’accès à un VPN d’entreprise n’autorise pas automatiquement chaque outil à utiliser toutes les ressources internes. De même, un navigateur Work dans le cloud ou un contrôle réseau dans le cloud n’impose pas de restriction universelle aux connexions réseau locales de l’appareil. Examinez la connexion, l’identité, la destination et l’action effectivement requises par le workflow.

## Traitement et conservation des données

Appliquez à l’appareil et au workflow concernés les contrôles de votre organisation relatifs aux points de terminaison, à l’accès aux fichiers, aux proxys et à la prévention de la perte de données. Vérifiez si ces contrôles peuvent empêcher l’introduction d’informations sensibles dans la tâche avant leur traitement. Les journaux d’audit et les exports de conformité facilitent la surveillance et les investigations, mais ne bloquent pas à eux seuls le traitement.

Le stockage et la conservation dépendent de la catégorie d’informations et de l’endroit où elles sont enregistrées.

| Catégorie d’informations                            | Points à vérifier                                                                                                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Enregistrements locaux des conversations                      | La façon dont l’application de bureau stocke, supprime, sauvegarde ou partage les enregistrements locaux. Ne supposez pas que les paramètres de conservation des conversations hébergées s’appliquent à tous les éléments stockés localement. |
| Fichiers locaux et résultats générés               | Le stockage sur l’appareil, la politique applicable aux points de terminaison, les téléversements autorisés par l’utilisateur, le partage externe et toute copie enregistrée séparément.                                                       |
| Prompts, extraits de fichiers et contexte des applications | Le contenu fourni à un modèle ou à un service, les conditions applicables à l’espace de travail et le flux réel de données du workflow.                                                           |
| Voix et Appshots                              | Les données captées par le microphone, les captures d’écran de la fenêtre au premier plan, le texte accessible des applications, le stockage local des sessions et tout contenu envoyé comme contexte de la tâche.                          |
| Données du navigateur                                    | Le profil de navigateur utilisé, les sessions déjà ouvertes, l’historique de navigation, les téléchargements, les approbations de sites web et tout contenu de tâche stocké séparément.                           |
| Enregistrements des systèmes connectés                        | Les autorisations et les règles de conservation du système source, l’identité du compte connecté et toute information enregistrée séparément dans la conversation ou ailleurs.              |
| Enregistrements de conformité et d’activité                 | Les événements Work Local disponibles pour l’espace de travail, l’intégration prise en charge et la politique de conservation du système destinataire.                                   |

Pour les espaces de travail Business, Entreprise et Edu pris en charge, les données professionnelles traitées par les services OpenAI couverts sont chiffrées en transit et au repos et ne sont pas utilisées par défaut pour entraîner ou améliorer les modèles OpenAI. Ces protections ne signifient pas qu’OpenAI régit tous les fichiers présents sur l’appareil, les applications tierces, les profils de navigateur ou les enregistrements des systèmes sources.

N’appliquez pas aux enregistrements locaux une durée de conservation prévue pour les conversations hébergées, les téléversements temporaires ou les journaux de conformité sans avoir confirmé qu’elle s’applique à la catégorie de données concernée.

## Visibilité en matière d’audit et de conformité

Les rapports disponibles dépendent de l’offre de l’espace de travail, de l’expérience produit, de l’événement, de l’application connectée et de la configuration déployée. Vérifiez ce qui est couvert pour Work Local avant de vous appuyer sur un export de l’espace de travail pour répondre à un incident ou effectuer un contrôle réglementaire.

Vérifiez si les systèmes concernés enregistrent l’identité de la tâche, les prompts et réponses pris en charge, les appels aux applications connectées, les approbations liées au navigateur, les actions dans les applications, l’activité sur les fichiers locaux ou les événements des points de terminaison. Les enregistrements des systèmes sources et des appareils peuvent offrir une visibilité différente de celle des enregistrements de l’espace de travail ChatGPT.

OpenAI ne conserve pas d’historique distinct et complet des actions effectuées dans Chrome via l’extension. Ne supposez pas que chaque opération sur un fichier local, capture d’écran, action dans le navigateur, approbation ou mise à jour externe figure dans l’API de conformité.

## Commencez par une tâche approuvée

Commencez avec un petit groupe utilisant des appareils gérés et choisissez une tâche approuvée, par exemple comparer une sélection de classeurs financiers. Vérifiez l’accès à Work de chaque utilisateur et ne fournissez que les fichiers, applications, sessions de navigateur ou comptes connectés nécessaires à la tâche.

Vérifiez que les actions approuvées fonctionnent, que les actions restreintes sont bloquées et que les enregistrements disponibles répondent à vos besoins de surveillance. Faites vérifier les résultats et toute modification externe par un utilisateur avant d’élargir l’accès.
