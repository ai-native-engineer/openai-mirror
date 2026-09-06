<!-- source: https://learn.chatgpt.com/fr-FR/docs/third-party/gitlab -->

Utilisez la revue de code Codex pour soumettre vos merge requests GitLab à un examen
supplémentaire ciblé et pertinent. Codex analyse le diff de la merge request, suit les consignes
de votre dépôt et publie une revue de code GitLab standard axée sur les problèmes graves.

La prise en charge de GitLab est en version bêta et disponible avec toutes les offres ChatGPT. L’intégration
Codex s’exécute dans Codex Cloud. Les fonctionnalités de gestion des dépôts de type GitHub dans
l’application de bureau, telles que **Créer une pull request**, ne sont pas incluses dans cette version bêta.

## Avant de commencer

Assurez-vous de disposer des éléments suivants :

- Un compte GitLab connecté. GitLab.com nécessite le
[parcours de connexion standard](https://help.openai.com/articles/20001486) ;
  les instances GitLab autogérées ou GitLab Dedicated nécessitent
[la configuration d’un modèle par un administrateur de l’espace de travail](https://help.openai.com/articles/20001487).
- Un fichier `AGENTS.md` si vous souhaitez que Codex respecte les consignes de revue
  propres au dépôt.

## Configurez la revue de code Codex

### Configurez la connexion GitLab et l’identité de revue de Codex

Pour GitLab.com, connectez votre compte GitLab dans Codex une fois que vous avez
[connecté GitLab dans ChatGPT](https://help.openai.com/articles/20001486).
Pour GitLab autogéré ou GitLab Dedicated, chaque relecteur doit se connecter une fois que le
[modèle de l’administrateur de l’espace de travail](https://help.openai.com/articles/20001487) a été
publié.

Pour GitLab autogéré ou GitLab Dedicated, ouvrez **Codex Cloud** → **Paramètres** →
[**Connecteurs**](https://chatgpt.com/codex/cloud/settings/connectors). Un
administrateur de l’espace de travail peut laisser Codex créer un compte de service ou enregistrer
le jeton d’accès personnel d’un compte de service existant.

#### Laissez Codex créer le compte

Dans **Codex Cloud** → **Paramètres** → **Connecteurs**, sélectionnez l’application correspondant à votre hôte GitLab
autogéré ou GitLab Dedicated → sélectionnez **Configurer le compte de service** →
**Créer un compte de service**. L’administrateur de l’espace de travail qui effectue la configuration doit disposer
d’un accès administrateur à l’instance GitLab. Choisissez **Groupes sélectionnés**
ou **Projets sélectionnés uniquement**, puis sélectionnez les groupes ou projets où Codex doit intervenir et créez
le compte. L’option de groupe accorde un accès Developer à chaque groupe sélectionné,
accès dont héritent ses projets et sous-groupes ; l’option de projet accorde un accès Developer
uniquement aux projets individuels que vous choisissez. Codex crée le compte de service d’instance ChatGPT
Codex Connector, doté d’un jeton d’accès personnel disposant de la portée
`api`.

#### Utilisez un compte existant

Dans GitLab, créez ou choisissez un compte de service et accordez-lui un accès Developer
uniquement aux groupes ou projets dans lesquels Codex doit intervenir. Sur la page **Comptes
de service** , sélectionnez le compte → **Gérer les jetons d’accès** → **Ajouter un nouveau
jeton** pour
[créer un jeton d’accès personnel](https://docs.gitlab.com/user/profile/service_accounts/#create-a-personal-access-token-for-a-service-account)
avec la portée `api` et une expiration prévue dans 30 jours au minimum. De retour dans
Codex, choisissez **Utiliser un compte de service existant**, collez le jeton, puis sélectionnez
**Enregistrer le jeton**. Le jeton est chiffré lors de son enregistrement et ne s’affiche plus jamais.

#### Gérez le jeton du compte de service

Les administrateurs de l’espace de travail peuvent gérer le compte de service dans **Codex Cloud** →
**Paramètres** → **Connecteurs**. Pour un compte créé par Codex, ils peuvent révoquer
le jeton actuel et en générer un nouveau. Pour un compte existant, ils peuvent
remplacer ou supprimer le jeton enregistré dans Codex et, si nécessaire, le révoquer séparément dans
GitLab. Codex ne peut pas répondre à l’activité GitLab tant qu’un jeton valide n’est pas
configuré.

### Choisissez comment l’activité GitLab est transmise à Codex

#### Créez un environnement de projet pour les tâches de programmation ou une configuration propre au projet

Dans **Codex Cloud** → **Paramètres** → **Environnements**, choisissez le projet GitLab
et créez un environnement de projet lorsque vous souhaitez que Codex écrive ou exécute du code
pour celui-ci — par exemple, pour modifier des fichiers, effectuer des commits ou pousser des mises à jour vers
une branche de merge request — ou lorsqu’une revue nécessite des secrets propres au projet,
un accès réseau ou des commandes de configuration.

Pour GitLab.com, un environnement de projet est également nécessaire pour activer les revues Codex.

Lors de la création de l’environnement, activez **Activer l’activité Codex depuis GitLab**
afin d’installer le webhook de projet qui transmet à Codex les événements liés aux merge requests, aux commentaires
et aux issues. La création du webhook de projet nécessite un accès Maintainer ou Owner,
un accès administrateur ou un rôle personnalisé autorisé à administrer les
webhooks du projet. Les webhooks de projet et de groupe signés nécessitent GitLab 19.0 ou une version ultérieure. Sur
GitLab 19.0 autogéré, vérifiez que l’indicateur de fonctionnalité `webhook_signing_token` est
activé ; il l’est par défaut et a été supprimé dans GitLab 19.1.

#### Activez l’activité pour les revues Codex sur l’ensemble des projets d’un groupe GitLab

Pour GitLab autogéré ou GitLab Dedicated, les administrateurs de l’espace de travail peuvent ouvrir **Environnements**
→ **Activité GitLab** → **Gérer les groupes** pour activer les revues Codex dans un groupe
et ses sous-groupes. Codex installe un webhook de groupe qui couvre les projets
de l’ensemble de ce groupe. L’utilisateur GitLab connecté doit être Owner du groupe, et les
webhooks de groupe nécessitent GitLab Premium ou Ultimate ainsi que GitLab 19.0 ou une version ultérieure.

L’activité d’un groupe permet les revues de code, mais ne crée pas d’environnements de projet.
Pour exécuter des tâches de programmation déclenchées depuis GitLab, comme modifier des fichiers,
exécuter des commandes, effectuer des commits ou pousser des mises à jour dans une merge request,
créez un environnement de projet.

### Configurez les politiques de revue de code

Configurez les politiques de revue de code dans les
[paramètres de revue Codex](https://chatgpt.com/codex/cloud/settings/code-review?provider=gitlab).
Choisissez la politique du dépôt : `Review my MRs`, `Review team MRs`,
`Review all MRs` ou `Follow personal`. Choisissez ensuite le moment où les revues sont exécutées : **À l’ouverture d’une MR**,
**À chaque push** ou **Déclenchement intelligent (expérimental)**. Les paramètres du dépôt peuvent
prévaloir sur les paramètres personnels par défaut.

## Demandez une revue Codex

1. Dans un commentaire sur une merge request, mentionnez `@codex review`.
2. Attendez que Codex réagisse (👀) et publie une revue.

Codex publie des discussions et des notes GitLab sur la merge request, comme le ferait
un membre de votre équipe. Par défaut, les revues demandées manuellement peuvent signaler des problèmes P0, P1 et
P2, tandis que les revues automatiques se concentrent sur les problèmes P0 et P1.

## Activez les revues automatiques

Pour examiner automatiquement les merge requests éligibles, activez **Revues
automatiques** dans les paramètres Codex, choisissez la politique du dépôt GitLab, puis sélectionnez un
déclencheur : **À l’ouverture d’une MR**, **À chaque push** ou **Déclenchement intelligent (expérimental)**.
Codex s’exécute sans commentaire `@codex review` lorsque l’événement lié à la merge request
correspond à cette politique et à ce déclencheur.

L’activité GitLab doit être activée au moyen du webhook d’un projet ou d’un groupe parent.
Pour GitLab autogéré ou GitLab Dedicated, le compte de service configuré doit également
disposer de droits d’écriture sur le projet. Codex utilise un environnement de projet configuré
lorsqu’il en existe un. Si l’activité est déjà activée pour un groupe parent,
les projets descendants en héritent.

## Personnalisez ce que Codex examine

Codex recherche les fichiers `AGENTS.md` dans votre dépôt et applique les règles de revue de code
pertinentes. Ajoutez une section `## Code Review Rules` au fichier le plus proche
du code auquel ces règles s’appliquent. Utilisez des titres `###` pour regrouper les contrôles associés lorsque
cela est utile.

Par exemple, un service de génération de rapports sur les expérimentations peut empêcher que les comportements postérieurs à l’exposition
modifient une cohorte de comparaison :

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Placez les règles applicables à l’ensemble du dépôt dans le fichier `AGENTS.md` situé à la racine et les règles propres à un service dans
un fichier imbriqué, par exemple `services/experiment_reporting/AGENTS.md`. Codex applique
les consignes définies à la racine et les consignes plus spécifiques qui concernent chaque fichier modifié ; ainsi, les changements sans rapport
n’ont pas à inclure un contexte propre à un service.

Commencez par deux ou trois règles concises qui formalisent des vérifications que les relecteurs
expliquent fréquemment. Voici quelques règles utiles :

- **Concentrez-vous sur les comportements à fort impact propres au dépôt.** Décrivez la
  contrainte de compatibilité, le périmètre des données ou l’effet de bord dangereux à signaler,
  et expliquez son importance.
- **Précisez l’approche sûre ou l’exception.** Donnez à Codex suffisamment de contexte pour distinguer
  un véritable problème d’un comportement attendu.
- **Définissez des règles ciblées et durables.** Privilégiez les résultats aux noms de fonctions
  susceptibles de changer et placez les consignes près du code concerné.
- **Réservez les vérifications mécaniques à la CI.** Excluez la mise en forme, le lint et les autres
  vérifications déterministes des règles de revue.

Ouvrez une merge request représentative et demandez une revue à l’aide de `@codex review`.
Affinez les règles en fonction des problèmes détectés et des retours obtenus, puis limitez ou
supprimez les consignes qui génèrent des signalements inutiles.

Les règles de revue de code guident Codex ; elles ne remplacent ni les tests, ni les protections des branches,
ni les approbations requises.

Pour cibler ponctuellement un aspect particulier, précisez-le dans votre commentaire sur la merge request :

`@codex review for issues in the database migration`

## Traitez les problèmes détectés lors de la revue

Pour corriger les problèmes détectés, vous devez disposer d’un **environnement de projet configuré** ; l’activité de groupe
permet les revues, mais ne permet pas, à elle seule, d’exécuter des tâches de programmation. Si le projet dispose
d’un environnement, demandez à Codex de corriger un problème dans la même merge request en ajoutant
un autre commentaire :

```md
@codex fix the P1 issue

Codex démarre une [discussion dans le cloud](/fr-FR/codex/cloud) en utilisant la merge request comme contexte et
peut pousser un correctif vers la branche lorsqu’il dispose des autorisations nécessaires.

## Confiez d’autres tâches à Codex

Les autres tâches de programmation nécessitent également un **environnement de projet configuré** ; l’activité de groupe
ne permet à elle seule que les revues. Si vous mentionnez `@codex` dans un commentaire contenant
autre chose que `review`, Codex démarre une [discussion dans le cloud](/fr-FR/codex/cloud) en utilisant
votre merge request comme contexte.

```md
@codex fix the CI failures

## Résolvez les problèmes de revue de code

Si Codex ne réagit pas ou ne publie pas de revue :

- Vérifiez que la bonne application GitLab est sélectionnée ; si vous utilisez une configuration propre
au projet, vérifiez que celui-ci dispose de l’environnement Codex Cloud prévu.
- Vérifiez que l’activité est activée pour le projet ou pour un groupe parent. Dans GitLab, consultez
**Webhooks** →
[**Événements récents**](https://docs.gitlab.com/user/project/integrations/webhooks/)
  et vérifiez que les événements de merge request et de note sont transmis correctement.
- Pour GitLab autogéré ou GitLab Dedicated, vérifiez que le webhook du projet ou du groupe est
  signé, que la vérification SSL est activée et que l’instance utilise GitLab 19.0 ou une version
  ultérieure. Sur GitLab 19.0 autogéré, vérifiez que l’indicateur de fonctionnalité `webhook_signing_token` est
  activé ; réparez les hooks automatiquement désactivés à la suite d’échecs.
- Pour GitLab autogéré ou GitLab Dedicated, vérifiez que le jeton d’accès personnel d’un compte de service existant
  est actif et possède la portée `api`. Si Codex a créé le
  compte de service, vérifiez qu’il est correctement configuré dans les
[paramètres des connecteurs Codex](https://chatgpt.com/codex/cloud/settings/connectors)
  et que le projet ou le groupe est activé.
- Pour GitLab autogéré ou GitLab Dedicated, vérifiez que le compte de service de l’espace de travail,
et pas uniquement l’utilisateur GitLab connecté, dispose d’un accès Developer au projet
ou à un groupe parent afin que Codex puisse publier des revues et des réactions. L’appartenance aux groupes est
héritée ; l’activité et l’accès du compte de service sont indépendants.
- Vérifiez que l’option **Revue de code** ou **Revues automatiques** est activée et que la MR correspond
  à la politique du dépôt et au déclencheur.
- Utilisez `@codex review`.
