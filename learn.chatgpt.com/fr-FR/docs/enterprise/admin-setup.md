<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/admin-setup -->

Utilisez ce guide pour planifier le déploiement de ChatGPT Enterprise dans les périmètres
d’administration suivants :

- Accès à l’espace de travail.
- Politique d’exécution locale pour les fonctionnalités concernées dans l’application de bureau ChatGPT,
Codex CLI et l’extension IDE.
- Codex Cloud.
- Accès à la Plateforme API.
- Accès aux plugins et aux connecteurs.
- Autorisations dans les systèmes connectés.

Pour un nouveau déploiement, suivez les étapes dans l’ordre ou consultez les pages indiquées pour modifier
un seul périmètre.

Dans les paramètres de l’espace de travail, **Codex et Work en local** regroupe les accès locaux à Codex et à Work
sous **Autoriser les membres à utiliser Codex et Work en local**. Certains espaces de travail
proposent plutôt deux sections indépendantes, **Codex en local** et **Work en local** . Dans
cette présentation, **Autoriser les membres à utiliser Codex en local** contrôle Codex, et **Utiliser
Work en local** contrôle Work. Activer l’un n’active pas l’autre.
Ces libellés correspondent à des autorisations de l’espace de travail, et non à des produits ou à des clients distincts.
Les autorisations des tokens et les limites de durée de validité des identifiants d’authentification figurent dans une section **Tokens
d’accès** ou dans la section consacrée à l’accès local, selon l’espace de travail.
La configuration gérée est une couche de règles distincte qui peut encadrer les comportements d’exécution pris en charge
pour les fonctionnalités concernées dans ces clients. Ce guide précise
l’interface concernée lorsque le comportement ou la disponibilité diffère.

Commencez par la vue d’ensemble de référence dans
[Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions).
Consultez les instructions du centre d’aide pour connaître les procédures actuelles de l’espace de travail ChatGPT et la
documentation pour les développeurs indiquée en lien pour comprendre le comportement d’exécution en local et dans les environnements hébergés.

<a id="enterprise-grade-security-and-privacy"></a>

Pour la sécurité, la confidentialité et les protections à l’exécution en entreprise, consultez
[Approbations et sécurité des agents](/fr-FR/codex/agent-approvals-security) et le
[livre blanc sur la sécurité de Codex](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).

<a id="pre-requisites-determine-owners-and-rollout-strategy"></a>

## Étape 1 : désignez les responsables et choisissez une approche de déploiement

Désignez un responsable pour chaque volet du déploiement :

- **Accès à l’espace de travail :** gestion des membres, licences, rôles et fonctionnalités
  prises en charge dans l’espace de travail.
- **Politique d’exécution locale :** approbations, profils d’autorisation, accès au système de fichiers et
  au réseau, et autres exigences applicables aux clients locaux pris en charge.
- **Codex Cloud :** environnements hébergés, connexions aux dépôts et politique
  d’exécution dans le cloud.
- **Systèmes connectés :** installation d’applications côté fournisseur, comptes et
  autorisations.
- **Rapports et conformité :** accès aux analyses, exportations d’audit et
  traitement des données en aval.

Déterminez si chaque public a besoin des fonctionnalités locales concernées dans l’application de bureau ChatGPT,
Codex CLI, l’extension IDE, Codex Cloud ou une combinaison de ces interfaces. Traitez
l’accès à la Plateforme API comme un périmètre distinct au niveau de l’organisation et du projet lorsqu’un
workflow utilise une authentification par clé API.

## Étape 2 : configurez l’accès à l’espace de travail et l’identité

Utilisez la gestion des membres, les licences, les groupes et les autorisations RBAC prises en charge dans l’espace de travail ChatGPT
pour donner aux publics visés accès aux fonctionnalités prises en charge de l’espace de travail. Vérifiez l’accès aux
clients locaux et à Codex Cloud en vous référant à la documentation actuelle de l’espace de travail, plutôt
que de supposer que le même rôle régit toutes les interfaces. Réservez les rôles
d’administration intégrés aux personnes qui administrent l’espace de travail.

Les contrôles et les libellés de l’espace de travail évoluent au fil du temps. Consultez ces sources pour connaître les
procédures à jour :

- [Gérez les membres, les types de licence, les rôles et les accès](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [Configurez le contrôle d’accès basé sur les rôles](https://help.openai.com/en/articles/11750701-rbac)
- [Gérez les paramètres de l’espace de travail](https://help.openai.com/en/articles/8411955)
- [Groupes et provisionnement](/fr-FR/codex/enterprise/groups-and-provisioning)
- [Gestion du cycle de vie des utilisateurs](/fr-FR/codex/enterprise/user-lifecycle)
- [Authentification](/fr-FR/codex/auth)

Testez la connexion et l’accès aux fonctionnalités avec un membre représentatif avant d’étendre
le déploiement. L’accès à l’espace de travail ne donne pas accès aux dépôts, aux fichiers ni aux actions
d’un service connecté.

## Étape 3 : configurez les exigences d’exécution locale

Les exigences locales encadrent le comportement à l’exécution lorsqu’un utilisateur lance une
exécution locale prise en charge dans l’application de bureau ChatGPT, Codex CLI ou l’extension IDE. Distribuez
`requirements.toml` par un canal pris en charge dans le cloud, sur l’appareil ou au niveau du système. Gérez
cette politique séparément des rôles et des groupes de l’espace de travail ChatGPT.

Utilisez des profils d’autorisation pour les clients locaux pris en charge, plutôt que de concevoir de nouveaux
déploiements fondés sur les anciennes restrictions du mode bac à sable. Par exemple :

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true

Pour désactiver la fonctionnalité Utilisation de l’ordinateur dans les interfaces de navigateur et de bureau
prises en charge, appliquez des contraintes à chaque clé publique de fonctionnalité qui intervient dans cette expérience :

```toml
[features]
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
computer_use = false

Pour obtenir la liste de référence des clés, le mode de distribution, l’ordre de priorité et d’autres
exemples, consultez
[Configuration gérée](/fr-FR/codex/enterprise/managed-configuration) et la
[référence de `requirements.toml`](/fr-FR/codex/config-file/config-reference#requirementstoml).

<a id="team-config"></a>
<a id="step-4-standardize-local-configuration-with-team-config"></a>

## Étape 4 : standardisez la configuration du dépôt

Utilisez une configuration propre au dépôt pour partager les paramètres par défaut du projet, les règles et les
skills sans dupliquer la configuration pour chaque utilisateur. Versionnez la configuration dans
`.codex` ou `.agents`, selon l’emplacement indiqué dans la documentation de la fonctionnalité :

| Type          | Source                                           | Utilisation                                                  |
| ------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| Configuration | [Principes de configuration](/fr-FR/codex/config-file/config-basic) | Définissez les paramètres par défaut du dépôt pour les clients locaux pris en charge        |
| Règles         | [Règles](/fr-FR/codex/agent-configuration/rules)        | Contrôlez les commandes qui nécessitent une approbation hors du bac à sable |
| Skills        | [Créer des skills](/fr-FR/codex/build-skills)              | Mettez les workflows du dépôt à la disposition des clients pris en charge   |

La configuration du dépôt peut fournir des paramètres par défaut et des workflows réutilisables. Elle ne peut pas
accorder l’accès à l’espace de travail, aux modèles, à la Plateforme API ni aux systèmes connectés.

## Étape 5 : configurez Codex Cloud

Codex Cloud s’appuie sur des environnements hébergés et des dépôts de code source connectés. Planifiez
chaque périmètre :

1. Accordez au public visé l’accès à Codex Cloud via les contrôles de l’espace de travail
pris en charge.
2. Installez et configurez l’intégration prise en charge avec le système source.
3. Dans le système source, limitez l’accès aux dépôts à ceux dont chaque public
a besoin.
4. Configurez les environnements cloud, les secrets et l’accès Internet pour ces
dépôts.
5. Configurez les workflows hébergés facultatifs, tels que la revue de code.
6. Effectuez un test avec un utilisateur représentatif qui dispose des autorisations prévues pour l’espace de travail et
les dépôts.

Codex Cloud respecte les autorisations et les protections des dépôts fournies par le
système source connecté. L’accès à l’espace de travail ne contourne pas ces contrôles. Consultez
[Environnements cloud](/fr-FR/codex/environments/cloud-environment),
[Intégration GitHub](/fr-FR/codex/third-party/github) et
[Approbations et sécurité des agents](/fr-FR/codex/agent-approvals-security) pour obtenir des instructions sur la configuration
et le comportement à l’exécution de Codex Cloud.

## Étape 6 : configurez les plugins et les fonctionnalités connectées

Évaluez séparément l’installation des plugins, les skills inclus, les fonctionnalités reposant sur des connecteurs,
les actions des connecteurs et les autorisations dans le système source.
La désactivation d’une fonctionnalité reposant sur un connecteur n’entraîne pas nécessairement la désinstallation du
plugin ni des skills qu’il inclut.

Avant d’inclure un plugin ou un skill dans le déploiement :

1. Vérifiez sa provenance, la personne qui en est responsable, le public visé et la date de révision.
2. Passez en revue les Skills inclus, les connecteurs, les serveurs MCP, les hooks, ainsi que les données et
les actions nécessaires à chaque fonctionnalité.
3. Testez-le avec des données non sensibles et les droits d’accès strictement nécessaires.
4. Consignez les responsables de sa réévaluation et de son retrait.

Les plugins fonctionnent dans Discussion et Work de ChatGPT sur le web, sur ordinateur et sur mobile,
dans Codex au sein de l’application de bureau ChatGPT, ainsi que via le navigateur de plugins de Codex CLI.
Ils ne sont pas disponibles dans l’extension IDE.
ChatGPT et Codex partagent un même annuaire public universel de plugins ; les contrôles de l’espace de travail
déterminent les plugins auxquels les membres peuvent accéder.

Consultez les pages [Contrôles des plugins](/fr-FR/codex/enterprise/apps-and-connectors) et
[Contrôles des Skills](/fr-FR/codex/enterprise/skills) pour une description complète du modèle.

## Étape 7 : Mettez en place la gouvernance et l’observabilité

Choisissez l’outil de reporting adapté à la question posée :

<a id="analytics-api-setup-steps"></a>
<a id="compliance-api-setup-steps"></a>

- Utilisez les [Analyses de l’espace de travail](/fr-FR/codex/enterprise/workspace-analytics) pour
  consulter de manière interactive les analyses de l’espace de travail ChatGPT et celles de Codex.
- Utilisez l’[API d’analyse](/fr-FR/codex/enterprise/analytics-api) pour générer par programmation
  des rapports agrégés via l’API d’analyse Codex.
- Utilisez l’[API de conformité](/fr-FR/codex/enterprise/compliance-api) pour les enregistrements d’audit et
  d’enquête.
- Utilisez les [Limites d’utilisation de ChatGPT et contrôles des dépenses](/fr-FR/codex/enterprise/usage-limits)
  lorsque, selon l’offre, l’activité Codex consomme des crédits éligibles de l’espace de travail
  ChatGPT.

Consultez les références d’API accessibles après authentification pour obtenir des informations à jour sur les exigences d’accès, les schémas,
les champs, la conservation des données et le comportement des requêtes. Ne développez pas d’intégration à partir d’un
contrat copié dans ce guide.

Protégez le périmètre d’intégration :

- Stockez les clés API et les autres identifiants d’authentification des intégrations dans le système de gestion des secrets
de l’organisation.
- Limitez l’accès aux systèmes en aval et aux données conservées aux seules personnes
autorisées.
- Protégez les enregistrements exportés via l’API de conformité en fonction de leur sensibilité et
de la politique de conservation de l’organisation, et vérifiez par des tests que les workflows de collecte et de suppression
respectent le contrat en vigueur.

## Étape 8 : Vérifiez le déploiement et assurez-en le suivi

Vérifiez chaque périmètre concerné à l’aide d’identités représentatives :

- Appartenance à l’espace de travail ChatGPT, licence attribuée et autorisations de rôle prises en charge.
- Fonctionnalités locales concernées dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE,
y compris la connexion et les exigences d’exécution effectivement appliquées.
- Accès à Codex Cloud, configuration de l’environnement et autorisations d’accès aux dépôts.
- Accès à l’organisation et au projet de la Plateforme API pour les workflows utilisant des clés API.
- Installation des plugins, Skills inclus, accès aux connecteurs et actions prises en charge.
- Autorisations dans les systèmes connectés et accès aux données.
- Accès aux analyses et aux outils de conformité pour les administrateurs responsables.

Consignez, pour chaque contrôle, son responsable et la source de référence des procédures en vigueur. Ce registre
permet aux administrateurs de mettre à jour les procédures lorsque l’interface utilisateur ou la politique change, sans
modifier le modèle d’administration.

Après le déploiement initial, passez en revue les accès, les fonctionnalités connectées, l’utilisation des crédits,
les retours du support et les workflows réellement utilisés par les équipes. Adaptez le périmètre du déploiement
et les instructions destinées aux administrateurs lorsque ces indicateurs évoluent.
