<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/work-admin-faq -->

ChatGPT Work intègre à ChatGPT la technologie de Codex pour accomplir des tâches plus longues,
comportant plusieurs étapes. Il peut recueillir des éléments de contexte dans les discussions, les fichiers,
les ressources de l’espace de travail et les systèmes connectés, utiliser des outils approuvés et produire des résultats
prêts à être révisés. L’accès, le contexte, les actions, le comportement réseau et la consommation de crédits varient
selon l’offre, les paramètres de l’espace de travail, les autorisations des sources et l’interface.

## Vue d’ensemble

ChatGPT Work permet aux utilisateurs de déléguer à ChatGPT des tâches plus longues, comportant plusieurs étapes. Il peut recueillir
des informations auprès de sources connectées, raisonner d’une étape à l’autre, créer des documents,
des présentations ou des analyses, puis soumettre les résultats à révision.

ChatGPT Work est disponible sur les interfaces web, mobiles et de bureau prises en charge pour les offres
et les espaces de travail éligibles. Lorsque cette fonctionnalité est disponible, les propriétaires d’espaces de travail ou les
administrateurs autorisés peuvent gérer Work Cloud, Work Local et Codex Local grâce à des autorisations
distinctes. Dans les espaces de travail Enterprise et Edu éligibles, le rôle par défaut de l’espace de travail
inclut Work, sauf si un administrateur autorisé le désactive. Les contrôles du navigateur et du
réseau restreignent également Work Cloud, dont la disponibilité dépend du rôle, de l’offre, de
l’espace de travail et de la région. Consultez
[ChatGPT Work et Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

Cette FAQ explique comment les administrateurs gèrent ChatGPT Work : contrôles des accès et des données,
conformité et visibilité, utilisation et dépenses, réponse aux incidents et pratiques de
déploiement. Pour connaître le modèle d’exécution hébergée et les limites de sécurité, consultez
[Vue d’ensemble de ChatGPT Work](/fr-FR/codex/enterprise/chatgpt-work-overview).

## Principaux contrôles d’administration

Les administrateurs encadrent l’utilisation de ChatGPT Work à l’aide des niveaux de contrôle suivants :

- **Accès à l’espace de travail de l’entreprise :** les contrôles d’identité et d’accès régissent
  l’authentification et l’accès à l’espace de travail. Selon l’offre et la
  configuration, les fonctionnalités de gestion des identités contrôlées par les administrateurs peuvent inclure le SSO,
  la vérification des domaines, le provisionnement SCIM, la gestion du cycle de vie des utilisateurs et la
  synchronisation des groupes d’identité. SCIM et les groupes d’identité synchronisés ne sont pas
  inclus dans ChatGPT Business. Les utilisateurs peuvent activer l’authentification multifacteur (MFA) OpenAI pour leur compte.
  ChatGPT ne permet pas d’imposer la MFA à l’ensemble de l’espace de travail ; les organisations qui
  l’exigent devraient imposer le SSO et la MFA par l’intermédiaire de leur fournisseur d’identité. Gérez
  le SSO et les paramètres d’identité associés dans la
[Console d’administration globale](https://help.openai.com/en/articles/12289294-admin-portal).
  Consultez [Authentification multifacteur](https://help.openai.com/en/articles/7967234-enabling-or-disabling-multi-factor-authentication-mfa).
- **Accès à ChatGPT Work dans l’espace de travail :** lorsqu’il est disponible, Work Cloud
  encadre l’utilisation hébergée de Work sur les interfaces web, mobiles et de bureau prises en charge.
  Work Local encadre l’utilisation locale de Work sur ordinateur, tandis que Codex Local contrôle l’accès local à
  Codex dans les clients de bureau, CLI et IDE pris en charge. Les paramètres du navigateur cloud et du réseau
  restreignent davantage Work Cloud. Le contrôle d’accès personnalisé basé sur les rôles (RBAC)
  et les autorisations disponibles dépendent de l’offre et de l’espace de travail.
- **Appartenance aux groupes :** avec les offres compatibles avec SCIM, synchronisez les groupes via
  un fournisseur d’identité afin que les accès soient mis à jour lorsque les employés rejoignent l’organisation,
  changent de rôle ou la quittent. Consultez
[Groupes et provisionnement](/fr-FR/codex/enterprise/groups-and-provisioning).
- **Rôles de l’espace de travail et des membres :** les rôles intégrés de l’offre Enterprise comprennent Propriétaire,
  Administrateur, Membre et Lecteur des analyses. Dans les offres compatibles, les rôles personnalisés et le
  RBAC des membres contrôlent l’accès à ChatGPT Work, aux plugins et aux autres fonctionnalités.
  Lorsque différents types de licences s’appliquent, les membres doivent également disposer d’une licence comprenant ChatGPT ; une
  licence réservée à Codex ne donne pas accès à Work. Consultez
[Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions).
- **Plugins et applications :** la politique relative aux plugins régit leur disponibilité et leur
  installation. L’accès aux applications, les contrôles des actions et les règles d’approbation sont
  configurés séparément. Lorsqu’ils sont disponibles, les agents d’espace de travail disposent de leurs propres
  contrôles. Consultez [Contrôles des plugins](/fr-FR/codex/enterprise/apps-and-connectors),
[Plugins](/fr-FR/codex/plugins) et le
[livre blanc sur la sécurité des applications](https://cdn.openai.com/business-guides-and-resources/app-security-whitepaper.pdf).
- **Autorisations des systèmes sources :** un utilisateur ne peut accéder qu’aux contenus et aux actions
  autorisés par le compte ou la connexion partagée dans l’application native. Consultez
[Contrôles d’administration, sécurité et conformité dans les applications](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business).
- **Restrictions relatives aux approbations et aux actions :** pour les applications compatibles avec le contrôle des actions,
  les administrateurs peuvent autoriser toutes les actions, uniquement celles en lecture seule ou un ensemble personnalisé, et décider
  du traitement des actions nouvellement ajoutées. Les autorisations des applications déterminent séparément
  dans quels cas ChatGPT demande confirmation avant d’utiliser une application.
- **Crédits :** ChatGPT Work et Codex partagent les mêmes tarifs, crédits et limites d’utilisation.
  Les administrateurs Enterprise et Edu éligibles peuvent définir des limites mensuelles par utilisateur grâce à une
  limite par défaut pour l’espace de travail, des limites par défaut pour les groupes et des dérogations individuelles. Les utilisateurs peuvent
  demander une augmentation si l’espace de travail l’autorise. L’offre Business suit un modèle distinct
  pour les crédits et le contrôle des dépenses. Consultez
[Limites d’utilisation et contrôle des dépenses de ChatGPT](/fr-FR/codex/enterprise/usage-limits).
- **Analyses et rapports :** la Console d’administration globale et les analyses de l’espace de travail
  permettent d’étudier l’adoption et l’utilisation des crédits. Utilisez l’API de conformité et les interfaces de rapports Codex
  en respectant leur couverture documentée des événements et des produits ; consultez les
  schémas en vigueur avant de garantir la couverture de prompts, fichiers,
  approbations, actions, erreurs ou appels d’outils particuliers. Consultez
[Gouvernance](/fr-FR/codex/enterprise/governance).

## Accès, données, systèmes et actions des utilisateurs

### Comment l’accès aux données et aux systèmes, ainsi que les actions des utilisateurs, sont-ils protégés ?

ChatGPT Work est soumis aux contrôles d’identité, d’accès et d’autorisation déjà
établis dans votre espace de travail ChatGPT. Les administrateurs utilisent la gestion des identités,
les rôles de l’espace de travail et, pour les offres éligibles, le
[RBAC](https://help.openai.com/en/articles/11750701-rbac) afin de déterminer qui peut
utiliser ChatGPT Work.

Lorsque cette fonctionnalité est prise en charge, les accès peuvent être synchronisés avec votre fournisseur d’identité via
[SCIM](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
et la synchronisation des groupes. Vous pouvez ainsi gérer les accès et les autorisations de manière centralisée
lorsque des employés rejoignent l’organisation, changent de rôle ou la quittent.

Les systèmes sources sous-jacents appliquent les autorisations du compte ou de la connexion
partagée approuvée utilisés pour l’opération. Une connexion individuelle utilise les droits d’accès de
la personne concernée au système source. Une connexion appartenant à un agent ou partagée peut
permettre aux utilisateurs autorisés de cet agent d’accéder, via le compte connecté, à des données ou à des
actions auxquelles leur propre compte n’a pas accès. Limitez les périmètres d’accès de la connexion,
les actions disponibles et le public de l’agent aux besoins professionnels visés. Consultez
[Connexions et autorisations des agents d’espace de travail](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business).

<a id="how-does-work-access-data-and-context"></a>
<a id="how-does-work-mode-access-data-and-context"></a>

### Comment ChatGPT Work accède-t-il aux données et au contexte ?

ChatGPT Work peut utiliser la discussion en cours, les fichiers importés, les ressources de l’espace de travail et les
systèmes connectés via des applications approuvées et, le cas échéant, des plugins.
Selon les fonctionnalités et les autorisations activées, cela peut inclure des documents,
des dépôts, des tickets, des canaux, des e-mails et des calendriers. Des fichiers antérieurs peuvent être
accessibles via la discussion en cours, les projets pris en charge, un accès autorisé à la Bibliothèque
ou les références automatiques à la Bibliothèque, lorsqu’elles sont activées. Les mémoires enregistrées obéissent à leurs
propres contrôles au niveau de l’espace de travail et de l’utilisateur.

Chaque source de contexte conserve ses propres contrôles : les utilisateurs fournissent le contexte de la discussion,
les administrateurs gèrent les ressources de l’espace de travail et les systèmes connectés appliquent les règles d’authentification
et les autorisations. ChatGPT Work ne peut accéder qu’aux informations autorisées pour l’utilisateur ou pour une
connexion partagée approuvée.

ChatGPT Work hérite des protections applicables de l’espace de travail ChatGPT. La résidence des données, leur conservation,
la journalisation et la disponibilité des fonctionnalités varient selon l’offre, la région, l’interface et le système
connecté. Vérifiez donc la couverture correspondant à votre configuration.

### Quelles actions à fort impact sont restreintes ou nécessitent une révision ?

Le risque varie selon l’action. La lecture ou la rédaction ont généralement moins d’impact que la modification
de données, le partage d’informations ou les actions dans des systèmes externes. Combinez les rôles, des autorisations
et des identifiants d’accès à portée restreinte, ainsi que les approbations prises en charge, afin de réserver les actions à fort
impact à des usages de confiance soumis à révision.

Les catégories d’actions courantes sont les suivantes :

- **Lecture :** accéder à des informations provenant de sources approuvées, les rechercher ou les résumer
  sans modifier les données sous-jacentes.
- **Rédaction :** préparer des documents, des e-mails, des rapports, du code ou d’autres contenus qu’une
  personne révisera avant utilisation.
- **Écriture :** créer, mettre à jour ou supprimer des enregistrements dans des systèmes connectés, tels que des
  documents, des tickets, des dépôts ou des outils de gestion de projet.
- **Partage :** envoyer ou publier des informations, ou les mettre autrement à la disposition d’un plus grand nombre
  de personnes, de systèmes ou de destinations externes.
- **Planification :** démarrer une tâche ultérieurement ou selon un calendrier récurrent
  sans qu’un utilisateur ait à lancer chaque exécution.
- **Exécution :** exécuter du code, des commandes shell, des automatisations du navigateur ou d’autres
  tâches réalisées au moyen d’outils qui interagissent directement avec des environnements externes.

Pour les actions à fort impact, utilisez une révision humaine, des identifiants d’accès restreints, des périmètres
limités et les approbations prises en charge. Les actions des plugins restent soumises aux
autorisations et aux contrôles de sécurité de chaque intégration.

## Conformité

<a id="how-does-work-support-enterprise-privacy-and-data-commitments"></a>
<a id="how-does-work-mode-support-enterprise-privacy-and-data-commitments"></a>

### Comment ChatGPT Work répond-il aux engagements envers les entreprises en matière de confidentialité et de données ?

ChatGPT Work applique les engagements en matière de confidentialité, de sécurité et de données associés à
l’espace de travail ChatGPT du client, selon l’offre, la configuration, l’interface, la fonctionnalité
et la région. Pour ChatGPT Enterprise, cela comprend
[l’absence, par défaut, d’entraînement sur les données professionnelles](https://help.openai.com/en/articles/8983130-what-if-i-want-to-keep-my-history-on-but-disable-model-training),
le chiffrement en transit et au repos, les contrôles d’accès au niveau de l’espace de travail et la
journalisation d’audit prise en charge.

La prise en charge de la résidence des données, de la résidence de l’inférence, de la conformité HIPAA ou d’un
Business Associate Agreement n’est pas systématique. Vérifiez les
[recommandations actuelles sur la résidence des données et de l’inférence](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)
ainsi que le contrat du client pour les fonctionnalités et les régions utilisées.

Les services connectés ont leurs propres exigences en matière de conservation, de journalisation, d’accès, de résidence et de
conformité. Lorsque ChatGPT Work utilise des plugins, des dépôts ou des systèmes
tiers, évaluez à la fois les contrôles de l’espace de travail ChatGPT et ceux du système
connecté.

Pour les activités Codex, les contrôles d’entreprise peuvent s’étendre aux environnements de développement,
aux dépôts, aux outils configurés et aux activités associées. Consultez le
[Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup) et la section
[Gouvernance](/fr-FR/codex/enterprise/governance) en complément des contrôles de l’espace de travail.

### Quelles données sont stockées, conservées ou supprimées ?

La conservation et la suppression des données dans ChatGPT Work dépendent de l’offre de l’espace de travail
ChatGPT, des paramètres d’administration et des fonctionnalités utilisées. Les règles de conservation peuvent varier
selon les informations auxquelles ChatGPT Work accède. Les conversations et les fichiers éligibles de la Bibliothèque
suivent les paramètres applicables de l’espace de travail. Les fichiers de projet, les fichiers
importés temporairement, les mémoires enregistrées, les événements de conformité, les données synchronisées des applications et les
enregistrements de tiers peuvent suivre des règles distinctes de conservation et de suppression. Consultez
[Politiques de conservation des discussions et des fichiers](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt).

ChatGPT Work peut créer du contenu de discussion, des fichiers importés ou générés, des artefacts
et des métadonnées d’exécution. Les discussions Codex peuvent également créer des métadonnées de dépôt ou d’environnement,
des sorties de commandes, des diffs et des journaux. Consultez la documentation actuelle du produit et de l’
[API de conformité](/fr-FR/codex/enterprise/compliance-api) pour connaître précisément les catégories
de données, les durées de conservation et les procédures de suppression.

Examinez les exigences de conservation applicables à l’espace de travail ChatGPT et aux systèmes d’entreprise
connectés afin que les politiques de votre organisation en matière de gouvernance des données, de conformité et de
conservation des enregistrements s’appliquent à chaque système.

## Observabilité

### Quelles données d’utilisation sont accessibles aux administrateurs ou aux propriétaires ?

Les administrateurs et les propriétaires peuvent utiliser les analyses produit et les journaux de conformité pour suivre différents
aspects de l’activité. La Console d’administration globale fournit les vues prises en charge sur l’adoption de ChatGPT et de
Codex et sur l’utilisation des crédits ; les répartitions disponibles par utilisateur, produit, agent et modèle
dépendent de l’interface d’analyse et de l’espace de travail. Pour les espaces de travail
éligibles, l’API de conformité fournit les enregistrements des conversations ChatGPT qui entrent dans son périmètre,
y compris les activités Work dans le cloud prises en charge. La couverture dépend du produit,
de l’interface, des autorisations, du point de terminaison disponible et du schéma d’événements documenté. Consultez
[Analyses de l’espace de travail](/fr-FR/codex/enterprise/workspace-analytics) ainsi que
[l’API de conformité](/fr-FR/codex/enterprise/compliance-api).

### Les prompts, les sorties, les fichiers, les actions ou les appels d’outils sont-ils journalisés ?

Dans les espaces de travail Enterprise et Edu éligibles, la plateforme de journaux de conformité
fournit les prompts des utilisateurs de Work et les réponses des agents.
[Les appels aux applications connectées sont journalisés séparément](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business),
et les espaces de travail éligibles peuvent accéder aux fichiers actifs de la Bibliothèque via les
[points de terminaison pris en charge de l’API de conformité dédiés à la Bibliothèque](https://help.openai.com/en/articles/20001052-library-for-chatgpt).
Ces enregistrements ne constituent pas une piste d’audit exhaustive couvrant chaque opération sur des fichiers en environnement hébergé,
commande shell, interaction avec le navigateur, appel d’outil ou approbation.
Vérifiez les événements et les produits actuellement couverts dans la documentation
de l’API de conformité accessible après authentification.

La plateforme de journaux de conformité conserve les données pendant 30 jours. Exportez les enregistrements
en continu vers un système approuvé de recherche de preuves électroniques, de prévention des pertes de données, de type SIEM
ou de lac de données lorsque votre organisation exige une conservation plus longue. Consultez le
[guide de la plateforme de conformité OpenAI](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

### Peut-on détecter rapidement les comportements inhabituels, les défaillances ou les pics d’utilisation ?

Les analyses de l’espace de travail, les journaux de conformité et les outils de surveillance connectés aident
les administrateurs à examiner l’utilisation et à enquêter sur les activités ChatGPT, Work et Codex
prises en charge. Selon l’interface de rapports sélectionnée, les signaux peuvent inclure
les utilisateurs actifs, les messages pris en charge, l’activité des applications, l’utilisation des agents, les événements
d’authentification ou d’administration et la consommation de crédits. Les journaux exportés peuvent faciliter
la recherche de preuves électroniques, la prévention des pertes de données, les opérations SIEM, les audits et les enquêtes.
La qualité de la détection dépend de l’offre, de la couverture des événements, de leur attribution, de la fraîcheur des données et
des règles configurées.

Les signaux pouvant justifier un examen comprennent une hausse inattendue de l’utilisation ou de la
consommation de crédits, une activité inhabituelle d’un utilisateur ou d’un agent, des erreurs opérationnelles récurrentes et
des événements d’authentification ou d’administration pertinents. Vérifiez précisément les signaux disponibles
dans les schémas applicables d’analyse, de conformité et de journaux d’audit.

Pour les activités Codex, les analyses Codex et l’Analytics API fournissent les indicateurs pris en charge
concernant l’adoption et l’activité. Les organisations utilisant des clients Codex locaux peuvent choisir
d’activer les exportations OpenTelemetry pour des événements tels que les requêtes API, les erreurs, les métadonnées de prompts,
les décisions d’approbation d’outils et les résultats des outils. Le contenu des prompts est
masqué, sauf si `otel.log_user_prompt = true` fait l’objet d’une activation
distincte et explicite. Consultez
[Surveillance et télémétrie](/fr-FR/codex/agent-approvals-security#monitoring-and-telemetry).
Cette télémétrie Codex locale ne fournit aucune exportation OpenTelemetry pour
ChatGPT Work sur le web.

## Gouvernance

### Comment les administrateurs peuvent-ils contrôler les accès, les autorisations et les politiques ?

La gouvernance comprend trois niveaux liés, mais distincts :

- **Les contrôles d’accès à ChatGPT Work** déterminent qui peut utiliser ChatGPT Work sur
  chaque interface.
- **Les contrôles des agents d’espace de travail** déterminent qui peut créer, publier, partager,
  planifier ou configurer des agents réutilisables et des connexions partagées, lorsque les
  agents d’espace de travail sont disponibles.
- **La configuration gérée de Codex** encadre les comportements pris en charge lors de l’exécution locale de Codex
  et ne configure pas ChatGPT Work hébergé.

La configuration gérée encadre les comportements d’exécution pris en charge. Elle n’accorde pas
l’accès à l’espace de travail, ne remplace pas le RBAC et ne révoque pas l’accès d’un utilisateur à cet espace. Ces
niveaux ne constituent pas une interface unique et uniforme de gestion des politiques de ChatGPT Work. Les analyses et les journaux de conformité
apportent une visibilité supplémentaire dans les limites de leur couverture documentée des produits et des
événements.

Pour les clients Codex locaux pris en charge, les administrateurs d’entreprise peuvent appliquer
une [configuration gérée](/fr-FR/codex/enterprise/managed-configuration) et des
[profils d’autorisation](/fr-FR/codex/permissions). Ces contrôles propres aux clients locaux n’accordent pas
l’accès à ChatGPT Work hébergé et ne remplacent pas les autorisations correspondantes de l’espace de travail.

### Peut-on limiter l’accès par groupe, rôle, espace de travail ou capacité ?

Oui. Dans les offres Entreprise et Edu éligibles qui prennent en charge le RBAC personnalisé pour les membres,
l’accès aux capacités de ChatGPT Work peut être limité selon les rôles de l’espace de travail, les groupes d’identité
et les autorisations définies par les administrateurs. ChatGPT Business applique les contrôles pertinents
au niveau de l’espace de travail, mais ne propose ni RBAC personnalisé pour les membres ni synchronisation
des groupes par SCIM. Attribuez les capacités prises en charge en fonction des besoins métier
et de la politique de l’organisation. Consultez le
[guide du RBAC](https://help.openai.com/en/articles/11750701-rbac) ainsi que cette
[présentation pas à pas du RBAC](https://vimeo.com/1207482321/d1286e4467?share=copy&fl=sv&fe=ci).

Lorsque le RBAC personnalisé est disponible, les organisations peuvent l’utiliser pour déterminer quels
utilisateurs peuvent accéder à ChatGPT Work, gérer les paramètres de l’espace de travail, configurer des plugins
approuvés ou utiliser les fonctionnalités d’agents de l’espace de travail prises en charge. Pour les espaces de travail Entreprise et
Edu éligibles, les limites d’utilisation mensuelles peuvent accompagner un déploiement progressif grâce à une
limite par défaut pour l’espace de travail, à des limites par défaut par groupe et à des exceptions par utilisateur.

L’accès aux systèmes connectés reste géré de manière indépendante. Limitez l’accès aux plugins, aux identifiants
partagés, aux dépôts et aux actions permettant l’écriture aux seules personnes qui en ont besoin,
à l’aide des autorisations de l’espace de travail, des paramètres des plugins et des contrôles du système
source. Pour les clients Codex locaux pris en charge, la configuration gérée peut restreindre davantage
les capacités d’exécution locales. Work hébergé obéit à ses propres contrôles, spécifiques à l’espace de travail
et au produit.

### Comment les périmètres d’exécution et de réseau sont-ils gérés ?

Les périmètres de sécurité de ChatGPT Work dépendent de la tâche. Une conversation standard dans Discussion, un
workflow connecté, une tâche planifiée et une discussion Codex peuvent s’exécuter dans différents
environnements, avec des autorisations, des outils et des accès réseau distincts.

Gérez chaque environnement d’exécution à l’aide des contrôles qui lui sont applicables. Work Cloud
régit Work hébergé sur les interfaces web, mobiles et de bureau prises en charge. Work Local
régit Work exécuté localement dans l’application de bureau, tandis que Codex Local contrôle l’accès local à
Codex dans les clients de bureau, CLI et IDE pris en charge. Les autorisations réseau du navigateur et du shell
restreignent davantage Work Cloud. La recherche, les applications, les plugins, les agents de l’espace de travail disponibles
et les autorisations des systèmes sources restent des contrôles distincts.
La configuration gérée applicable et les politiques d’exécution locale ne régissent que les usages locaux
qu’elles prennent en charge. Ces contrôles ne sont pas interchangeables.

Pour les activités Codex, les exécutions locales dans l’application de bureau ChatGPT, la CLI et l’IDE s’effectuent
sur la machine de l’utilisateur, avec les mécanismes de bac à sable du système d’exploitation et des politiques d’approbation.
Codex Cloud exécute les discussions dans des environnements isolés gérés par OpenAI. Pour les clients locaux
pris en charge, les administrateurs d’entreprise peuvent utiliser des exigences gérées pour
restreindre les profils d’autorisation, les approbations, l’accès au système de fichiers et au réseau, les serveurs MCP,
les hooks, les règles de commande et d’autres comportements d’exécution pris en charge.

## Utilisation et coûts

<a id="how-does-work-usage-translate-into-spend-over-time"></a>
<a id="how-does-work-mode-usage-translate-into-spend-over-time"></a>

### Comment l’utilisation de ChatGPT Work se traduit-elle en dépenses au fil du temps ?

[ChatGPT Work et Codex partagent les mêmes tarifs, crédits et limites d’utilisation](/fr-FR/codex/pricing).
Pour les contrats éligibles reposant sur des crédits, comparez l’utilisation cumulée de Discussion et de Work
par les employés à l’enveloppe de crédits partagée de l’espace de travail. La consommation varie selon
le modèle, les paramètres de raisonnement ou de vitesse applicables, les entrées et sorties traitées,
ainsi que les outils ou fonctionnalités éligibles.

L’utilisation des crédits prévus au contrat n’augmente pas automatiquement le montant de votre facture. Les frais réels
dépendent du solde de crédits restant, des tarifs contractuels, de l’éligibilité du compte
aux dépassements et de la limite de dépassement configurée pour l’espace de travail. Pour des exemples de planification,
les limites effectives par utilisateur, le périmètre des rapports et les détails de facturation,
consultez [ChatGPT Work : utilisation et coûts](/fr-FR/codex/enterprise/chatgpt-work-usage-and-cost).

Les coûts les plus variables concernent souvent les workflows qui s’exécutent fréquemment,
récupèrent ou traitent de grandes quantités d’informations, sollicitent plusieurs outils ou applications,
réessaient après un échec ou produisent des artefacts volumineux. Les usages à surveiller en matière de coûts
incluent les tâches planifiées ou récurrentes, les fichiers volumineux, la récupération étendue
d’informations dans les sources de l’entreprise, les appels répétés aux applications et les discussions Codex qui
traitent des dépôts, exécutent des commandes ou utilisent des environnements cloud. Lorsqu’ils sont disponibles, les déclencheurs de l’API
Workspace Agent peuvent également augmenter l’utilisation.

Utilisez les contrôles des dépenses, l’analyse de l’utilisation et les rapports pour surveiller ces usages
au fil du temps. Examinez l’utilisation selon les dimensions disponibles dans l’interface d’analyse actuelle
et ajustez les limites ou le périmètre du déploiement en fonction de la valeur métier. Ne considérez pas
les analyses agrégées comme une attribution exacte des coûts à chaque workflow.

Les analyses de l’espace de travail, les journaux de conformité et les outils de surveillance connectés peuvent aider
les administrateurs à examiner l’utilisation et à analyser les activités couvertes. La capacité à
détecter les comportements risqués ou inhabituels dépend de l’offre, de la couverture des journaux, de l’attribution,
de la fraîcheur des données et des règles configurées dans vos systèmes de surveillance.

### Quelles limites d’utilisation, alertes ou quels plafonds sont disponibles ?

Les espaces de travail Entreprise et Edu éligibles peuvent utiliser des limites mensuelles par utilisateur et
des contrôles des dépenses à l’échelle de l’espace de travail pour l’utilisation décomptée en crédits :

- **Surveillez la consommation de crédits :** consultez les rapports disponibles sur l’utilisation des crédits dans la
  console d’administration globale et dans les paramètres de l’espace de travail.
- **Définissez une limite mensuelle par défaut :** établissez une limite de crédits par défaut par utilisateur
  pour l’espace de travail.
- **Appliquez des limites propres à chaque groupe :** attribuez aux groupes des limites mensuelles par défaut par utilisateur qui
  reflètent leurs workflows, leurs responsabilités ou leur phase de déploiement.
- **Créez des exceptions par utilisateur :** attribuez une limite différente à un utilisateur précis sans
  modifier la valeur par défaut de l’ensemble du groupe.
- **Examinez les demandes d’augmentation :** si les demandes sont activées, les utilisateurs peuvent demander une
  limite mensuelle plus élevée. L’approbation crée une exception pour l’utilisateur.
- **Maîtrisez l’exposition financière globale de l’espace de travail :** configurez séparément les alertes liées aux crédits de l’espace de travail et
  la limite de dépassement dans la console d’administration globale. Les alertes préviennent
  leurs destinataires ; la limite de dépassement régit l’utilisation éligible une fois la réserve
  de crédits prévus au contrat épuisée.
- **Exportez les données d’utilisation :** les administrateurs Entreprise éligibles peuvent accéder
  aux données d’utilisation des crédits via la Cost API unifiée pour produire des rapports internes ou
  surveiller l’utilisation.

Les utilisateurs peuvent consulter leur propre utilisation et, si cette option est activée, demander davantage de crédits, mais ils
ne peuvent pas modifier les limites qui leur sont attribuées. Consultez la page
[Gérer les limites d’utilisation et les dépassements](https://help.openai.com/en/articles/20001001-manage-usage-limits-and-overages-in-chatgpt-enterprise-and-edu)
ainsi que la
[présentation pas à pas des contrôles des dépenses](https://vimeo.com/1207484127/0f2029dd01?share=copy&fl=sv&fe=ci).

## Contrôles en cas d’incident et de révocation

### Comment les administrateurs peuvent-ils interrompre l’accès ou l’activité ?

Lors de la suppression d’un utilisateur ou de l’examen d’un incident, les administrateurs peuvent devoir interrompre l’accès,
désactiver des applications, révoquer des identifiants partagés, suspendre des tâches planifiées ou révoquer des identifiants
Codex.

Les procédures de révocation comprennent notamment les actions suivantes :

- Supprimez l’accès d’un utilisateur à l’espace de travail ou à un groupe. Pour les utilisateurs gérés par SCIM, supprimez
cet accès auprès du fournisseur d’identité ; sinon, une synchronisation ultérieure peut
provisionner de nouveau l’utilisateur.
- Désactivez ou restreignez le plugin ou l’application concernés.
- Révoquez une connexion partagée, un bot ou un compte de service depuis l’interface qui en assure
la gestion. Les propriétaires et administrateurs de l’espace de travail peuvent révoquer séparément les jetons d’accès
Codex à l’espace de travail.
- Annulez la publication d’un agent de l’espace de travail ou supprimez-le par l’intermédiaire de son propriétaire
ou d’un administrateur de l’espace de travail.
- Désactivez la tâche planifiée concernée ou, lorsqu’il est disponible, le déclencheur de l’API
Workspace Agent.
- Pour l’accès à Codex, révoquez séparément le jeton d’accès, la connexion au dépôt
et l’accès à l’environnement cloud concernés. La configuration gérée n’est pas un
mécanisme de révocation d’accès.

## Ressources supplémentaires pour vos équipes

| Thème                    | À utiliser pour expliquer                                                      | Page de la rubrique Apprendre de ChatGPT                                               |
| ------------------------ | ----------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Vue d’ensemble de Work            | Fonctionnement de l’exécution dans le cloud, de l’accès au navigateur, de la politique réseau et des périmètres de données | [Vue d’ensemble de ChatGPT Work](/fr-FR/codex/enterprise/chatgpt-work-overview) |
| Configuration de l’espace de travail et RBAC | Qui peut utiliser et administrer Codex                                              | [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)             |
| Authentification           | Différences entre la connexion avec ChatGPT, la connexion avec une clé API et la politique de l’espace de travail             | [Authentification](/fr-FR/codex/auth)                                    |
| Approbations et bac à sable | Comment Codex contrôle les actions sur les fichiers, l’exécution de commandes, l’accès au réseau et les actions d’outils ayant des effets de bord    | [Approbations et sécurité des agents](/fr-FR/codex/agent-approvals-security)  |
| Politique gérée           | Comment les administrateurs imposent des paramètres Codex que les utilisateurs ne peuvent pas modifier                        | [Configuration gérée](/fr-FR/codex/enterprise/managed-configuration) |
| Environnements d’exécution     | Fonctionnement de la configuration de Codex Cloud, des secrets, des caches et des phases des tâches                  | [Environnements cloud](/fr-FR/codex/environments/cloud-environment)      |
| Accès Internet          | Fonctionnement des listes de domaines autorisés et des méthodes HTTP dans Codex Cloud                       | [Accès des agents à Internet](/fr-FR/codex/cloud/internet-access)            |
| Autorisations              | Fonctionnement des contrôles d’accès au système de fichiers et au réseau, ainsi que des interdictions de lecture                          | [Autorisations](/fr-FR/codex/permissions)                                |
| Observabilité            | Fonctionnement des analyses, des rapports et des exports de conformité                         | [Gouvernance](/fr-FR/codex/enterprise/governance)                       |
| Identifiants d’authentification pour l’automatisation   | Comment les jetons d’accès sont créés, limités, révoqués et audités                  | [Jetons d’accès](/fr-FR/codex/enterprise/access-tokens)                 |

## Actions recommandées aux administrateurs

- **Déterminez qui doit bénéficier d’un accès en priorité.** Décidez s’il faut restreindre l’accès à
  ChatGPT Work, mener un projet pilote ou le déployer à grande échelle. De nombreuses organisations commencent
  par les utilisateurs avancés, les ambassadeurs ou les équipes dont les cas d’utilisation sont clairement définis.
- **Passez en revue les rôles et les autorisations.** Dans **Autorisations et rôles**, vérifiez quels
  utilisateurs ou groupes peuvent accéder à ChatGPT Work. Accordez l’accès en fonction des besoins métier, du niveau de préparation
  et des attentes en matière de gouvernance.
- **Passez en revue les plugins et les sources de données.** ChatGPT Work est le plus utile lorsqu’il dispose d’un contexte
  métier approuvé, comme des fichiers, des e-mails, des calendriers, Slack ou un CRM. Vérifiez
  quels plugins sont activés, qui y a accès et si les politiques des applications correspondent toujours à la manière dont les utilisateurs
  doivent déléguer leur travail.
- **Précisez les cas d’utilisation à privilégier.** Présentez ChatGPT Work comme l’outil adapté aux tâches en plusieurs étapes
  et à plus forte valeur ajoutée, comme la recherche, la synthèse, l’analyse, la création de fichiers,
  la mise à jour de workflows et la production de livrables réutilisables. Utilisez Discussion pour les questions rapides,
  les reformulations légères ou le brainstorming.
- **Passez en revue les contrôles liés aux crédits et à l’utilisation.** Comme ChatGPT Work peut effectuer des tâches
  de longue durée, il peut consommer davantage de crédits qu’une conversation standard dans Discussion. Passez en revue
  les paramètres par défaut, ceux des groupes, les dérogations individuelles ainsi que les consignes internes visant à
  adapter l’effort à la valeur métier.
- **Identifiez vos premiers workflows à forte valeur ajoutée.** Commencez par des résultats clairs et vérifiables,
  comme des briefings clients, des rapports récurrents, des synthèses de recherche,
  des mises à jour d’outils de suivi ou des documents et des diapositives soignés.
- **Préparez les ambassadeurs et les équipes d’assistance.** Fournissez en priorité aux ambassadeurs, aux responsables de la formation
  et aux équipes d’assistance les ressources de déploiement afin qu’ils puissent répondre aux questions,
  recueillir les retours et montrer comment déléguer efficacement.
- **Précisez les attentes en matière de révision et d’approbation.** Rappelez aux utilisateurs que l’examen des résultats,
  la validation des affirmations importantes et l’approbation des actions à fort impact
  avant tout partage ou toute utilisation relèvent toujours de la responsabilité humaine.
- **Suivez l’adoption et adaptez votre approche.** Examinez l’utilisation, les retours, la consommation de crédits
  et les tâches déléguées après le déploiement. Appuyez-vous sur vos constats pour ajuster l’accès,
  les consignes, la formation et l’extension du déploiement.
