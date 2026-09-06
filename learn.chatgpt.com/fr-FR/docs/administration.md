<!-- source: https://learn.chatgpt.com/fr-FR/docs/administration -->

# Administration

Définissez les périmètres d’accès et les règles applicables à ChatGPT, aux outils de développement Codex, aux API, aux plugins et aux systèmes connectés

Définissez les périmètres d’accès et les règles applicables à ChatGPT, aux outils de développement Codex, aux API, aux plugins et aux systèmes connectés.

L’administration couvre six périmètres liés entre eux : l’accès à l’espace de travail ChatGPT ; la stratégie d’exécution locale applicable aux fonctionnalités concernées dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE ; les conditions d’accès à Codex Cloud ; l’accès à l’API de la plateforme ; la disponibilité des plugins et les autorisations des connecteurs ; et les autorisations dans les systèmes connectés. Commencez par la gestion des identités et des accès à l’espace de travail, puis appliquez les contrôles requis pour chaque déploiement à l’environnement d’exécution et aux systèmes sources.

Explorer l’authentification

Membres et groupes de l’espace de travail ChatGPT, jetons d’accès et contrôles associés aux rôles

Bien démarrer

Commencez par le guide de déploiement, puis consultez les pages de référence propres à chaque périmètre de contrôle.

Guide de déploiement pour les administrateurs

Planifiez les accès, désignez les responsables, configurez les contrôles et vérifiez le déploiement.

ChatGPT Work

Consultez la vue d’ensemble de ChatGPT Work et la documentation de référence pour l’administration.

Vue d’ensemble de ChatGPT Work

Découvrez l’exécution en environnement hébergé, les contrôles réseau, les limites applicables aux données et les informations disponibles pour l’audit.

Sécurité de ChatGPT Work dans le cloud

Examinez l’exécution en environnement hébergé, les comptes connectés, les contrôles d’accès, la conservation des données et les informations disponibles pour l’audit.

Sécurité de ChatGPT Work en local

Examinez l’exécution locale, l’accès aux appareils et au navigateur, les stratégies gérées, le traitement des données et les limites en matière d’audit.

FAQ d’administration de ChatGPT Work

Examinez les contrôles de ChatGPT Work concernant les accès, les données, la gouvernance, l’utilisation et les incidents.

ChatGPT Work : utilisation et coût

Découvrez les crédits partagés, l’impact sur la facturation, les contrôles des dépenses et la planification de l’adoption.

Identité et authentification

Choisissez le mode de connexion des utilisateurs et délivrez des identifiants d’authentification pour les workflows programmatiques.

Vue d’ensemble de l’authentification

Comparez les méthodes de connexion, le stockage des identifiants d’authentification et les mécanismes d’application des règles.

Identité de charge de travail

Permettez aux charges de travail de confiance d’utiliser Codex sans identifiants d’authentification à longue durée de vie.

Jetons d’accès personnels

Créez et gérez des tokens pour l’accès programmatique.

Comptes de service

Créez et gérez des identités dans l’espace de travail pour les workflows automatisés.

Accès à l’espace de travail, stratégies et modèles

Attribuez l’accès à l’espace de travail ChatGPT et gérez-le séparément de la stratégie d’exécution locale, de l’accès à Codex Cloud et de l’accès à l’API de la plateforme.

Groupes et provisionnement

Gérez les groupes administrés manuellement ou via SCIM, le provisionnement et les cohortes de déploiement.

Gestion du cycle de vie des utilisateurs

Provisionnez les comptes des employés, mettez à jour les accès des groupes et révoquez les identifiants d’authentification des utilisateurs qui quittent l’organisation.

Rôles et autorisations de l’espace de travail

Utilisez la cartographie de référence des contrôles relatifs à l’espace de travail, à l’environnement d’exécution, aux API, aux plugins et aux systèmes sources.

GPT et partage

Gérez le partage et la propriété des GPT, les applications connectées et les actions tierces dans l’ensemble de votre espace de travail.

Configuration gérée

Distribuez les paramètres gérés là où ils sont pris en charge et faites respecter les exigences d’exécution applicables aux fonctionnalités concernées dans l’application de bureau ChatGPT, Codex CLI et l’extension IDE.

Prisma AIRS

Appliquez aux prompts Codex des stratégies de sécurité à l’échelle de l’espace de travail.

Configuration HIPAA

Configurez des mesures de protection pour l’exécution locale des workflows susceptibles de traiter des informations de santé protégées.

Disponibilité des modèles dans l’espace de travail

Gérez séparément l’accès aux modèles pour ChatGPT, Codex dans l’application de bureau ChatGPT, Codex CLI, l’extension IDE, Codex Cloud et l’API de la plateforme.

Contrôles des plugins et des connecteurs

Contrôlez l’installation des plugins, les Skills incluses, les fonctionnalités reposant sur des connecteurs et l’accès aux services connectés.

Contrôles des plugins

Gérez la disponibilité des plugins, l’accès aux connecteurs et leurs actions, ainsi que les autorisations dans les systèmes sources.

Gestion des plugins

Importez et synchronisez les plugins de l’espace de travail depuis GitHub.

Contrôles des Skills

Comparez les contrôles des Skills dans l’espace de travail ChatGPT, le système de fichiers local et les plugins.

Utilisation, gouvernance et conformité

Mesurez l’adoption et acheminez les données destinées aux rapports ou aux audits vers le système qui les gère.

Gouvernance

Choisissez l’interface d’analyse, de suivi des dépenses ou d’audit adaptée à chaque question.

Plugin d’administration

Utilisez le plugin d’administration pour les autorisations, les approbations et les workflows administratifs pris en charge.

Analyses de l’espace de travail

Examinez l’adoption de ChatGPT et l’utilisation de Codex à l’échelle de l’espace de travail.

API d’analyse

Automatisez la production de rapports sur l’activité des développeurs et les revues de code avec l’API d’analyse de Codex.

API de conformité et événements d’audit

Exportez les enregistrements d’activité pour les workflows d’audit et d’investigation.

Déploiement et fournisseurs de modèles

Déployez et mettez à jour des applications de bureau, connectez des hôtes gérés ou configurez un fournisseur externe de modèles pris en charge.

Gestion des mises à jour de l’application

Contrôlez les mises à jour des applications de bureau et déployez les versions approuvées via votre plateforme de gestion des appareils.

Déploiement de l’application Windows

Choisissez une méthode d’installation et de mise à jour pour les appareils Windows gérés.

Connexions distantes

Lancez et contrôlez des tâches sur les ordinateurs connectés.

Amazon Bedrock

Configurez les clients locaux pris en charge pour utiliser les modèles disponibles via Bedrock.
