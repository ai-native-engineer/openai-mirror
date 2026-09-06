<!-- source: https://learn.chatgpt.com/fr-FR/docs/sites -->

Sites est en bêta publique et disponible avec les offres ChatGPT Plus, Pro, Business,
Enterprise et Edu. Des limites d’utilisation propres à chaque offre s’appliquent à l’ensemble des sites
pendant la bêta. ChatGPT affiche les limites en vigueur et vous avertit lorsque vous approchez
de l’une d’elles. Atteindre une limite peut vous empêcher de créer un site, d’ajouter du
stockage ou de maintenir un site très utilisé en accès public, mais vous pouvez toujours modifier et
gérer les sites existants.

Sites permet à ChatGPT de créer, d’héberger, d’améliorer et de partager des sites web, des applications web et des jeux.
Utilisez Sites pour transformer un prompt ou un projet existant compatible en une
expérience hébergée, sans mettre en place de workflow de déploiement distinct.

Ouvrez **Sites** dans l’application de bureau ChatGPT. Vous pouvez créer un site à partir d’un prompt ou
d’un projet local compatible, puis revenir à la vue Sites pour le gérer.

Utilisez Sites dans ChatGPT sur le web pour créer et gérer des sites hébergés. Sélectionnez
**Plus** \> **Sites**, ou accédez directement à
[chatgpt.com/sites](https://chatgpt.com/sites) pour retrouver les sites que vous avez créés.

Sites ne propose pas de vue de gestion dédiée dans Codex CLI. Utilisez ChatGPT sur le web ou
l’application de bureau pour créer, enregistrer, déployer et gérer un projet Sites. Vous pouvez
toujours utiliser Codex CLI pour modifier et tester un projet local avant de le publier.

Sites ne propose pas de vue de gestion dédiée dans l’extension IDE. Utilisez ChatGPT sur le web
ou l’application de bureau pour les opérations liées à Sites, et l’extension IDE pour modifier et
tester le projet source local.

  Chaque URL de déploiement de Sites correspond à un déploiement en production. Si vous souhaitez examiner un
build avant sa mise en ligne, demandez à ChatGPT d’enregistrer une version sans la
déployer.

## Bien démarrer avec Sites

Dans ChatGPT, incluez le mot « website » dans votre prompt ou mentionnez `@Sites` pour
lancer explicitement le workflow Sites.

1. Décrivez le site

   Décrivez le public visé, l’objectif, le comportement attendu et les informations que le site
doit utiliser.

2. Examinez le site

   Examinez le contenu généré et le fonctionnement du site. Vérifiez que le site utilise les
informations prévues et traite les données comme attendu.

3. Améliorez le site

   Décrivez les modifications souhaitées. Ajoutez des fichiers pertinents ou du contexte visuel si
cela peut aider ChatGPT à effectuer la modification.

4. Gérez et partagez le site

   Revenez dans **Sites** pour rouvrir ou améliorer le site. Lorsqu’il est prêt, choisissez qui
   peut y accéder, puis partagez le lien obtenu.

Dans l’aperçu, sélectionnez **Modifier**. Sous **Décrivez les modifications du site web**, décrivez les
modifications souhaitées. Utilisez **Capture d’écran** ou **Ajouter des fichiers et plus encore** si davantage de
contexte peut être utile.

## Prompts pour confier des tâches courantes à Sites

Pour un nouveau site web, tableau de bord ou outil interne, indiquez le public visé, l’expérience
principale et les informations nécessaires :

```text
Build a project request dashboard for my operations team. Let team members
submit requests, see who owns each one, update the status, and filter the list.
Require people to sign in with their workspace account, and keep the request
data saved between visits.

Pour un projet existant, demandez à Sites de préparer et de publier l’application actuelle :

```text
Deploy this project with Sites. Check whether it is compatible, make any
required changes, and give me the deployment URL.

Lorsqu’un site nécessite des données applicatives persistantes ou des fichiers importés, précisez-le dans la
demande :

```text
Add player scores and avatar uploads to this game. Keep the scores and uploaded
avatars between visits.

  Parcourez la [vitrine Sites](/showcase) pour découvrir des applications internes déployées et les
  prompts complets qui ont servi à les créer.

## Consultez les analyses d’un site

Sites enregistre automatiquement le trafic, ce qui vous permet de voir comment les visiteurs utilisent un site déployé
sans ajouter de SDK d’analyse. La vue Analyses affiche le nombre total de visiteurs uniques
et de pages vues, ainsi que l’évolution de ces deux indicateurs dans le temps. Modifiez la plage de dates ou
la granularité pour examiner une autre période.

Ouvrez **Sites**, repérez le site, puis sélectionnez **Plus d’actions** \> **Analyses**.

Accédez à [chatgpt.com/sites](https://chatgpt.com/sites), repérez le site, puis sélectionnez
**Plus d’actions** \> **Analyses**.

Sites ne propose pas de vue d’analyse dédiée dans la CLI ni dans l’extension IDE. Ouvrez
le site dans ChatGPT sur le web ou dans l’application de bureau pour consulter ses analyses.

  

  Les analyses sont actuellement disponibles pour les sites qui n’appartiennent pas à un espace de travail
Entreprise.

## Ajoutez la connexion avec ChatGPT

Les sites publics peuvent rester accessibles à tous tout en proposant une connexion facultative avec
ChatGPT pour les fonctionnalités qui s’appuient sur l’identité du visiteur, telles que la progression enregistrée, les vues personnalisées
ou les enregistrements associés à une personne précise. Les sites dont l’accès est limité à l’espace de travail utilisent déjà
l’identité ChatGPT pour appliquer leurs paramètres de partage.

Demandez à Sites d’ajouter le parcours de connexion :

```text
Add Sign in with ChatGPT to this public Site. Keep the Site available to signed-out visitors. Show a Sign in with ChatGPT action when someone is signed out. After they sign in, greet them with their full name when available, or their email address otherwise. Add a Sign out action, and keep authorization decisions in server-side code.

Sites gère les parcours de connexion et de déconnexion via des chemins fournis par la plateforme,
puis redirige le visiteur vers votre site :

```html
<a href="/signin-with-chatgpt">Sign in with ChatGPT</a>
<a href="/signout-with-chatgpt">Sign out</a>

Une fois qu’un visiteur s’est connecté, Sites transmet son identité au serveur via
les en-têtes de requête suivants :

- `oai-authenticated-user-email` contient l’adresse e-mail authentifiée.
- `oai-authenticated-user-full-name` peut contenir un nom de profil non vide. Considérez
  ce nom comme facultatif et utilisez l’adresse e-mail à défaut.

Prenez les décisions d’autorisation dans le code côté serveur et ne vous appuyez pas sur
des en-têtes qui séparent les différentes parties du nom.

## Comprendre les projets, les versions et les déploiements

Un site est une création hébergée de manière persistante que vous pouvez rouvrir, améliorer, configurer
et partager depuis **Sites** dans ChatGPT.

Un projet Sites relie un projet source local à un hébergement géré dans Sites.
Sites enregistre cette association et les noms des éventuelles liaisons de stockage dans
`.openai/hosting.json`. Un nouveau projet de démarrage local peut être créé sans
`project_id` ; Sites en ajoute un après avoir provisionné le projet hébergé.

Par exemple, un site provisionné qui utilise une liaison à une base de données relationnelle, mais pas de
stockage de fichiers, peut contenir :

```json
{
  "project_id": "<project-id>",
  "d1": "DB",
  "r2": null
}

Un site reste visible dans votre liste Sites même après la fin de la discussion ChatGPT Work qui l’a créé.
Vous n’avez besoin ni d’un projet local ni d’un manifeste pour créer un site sur le web. Un site est
distinct d’un Projet ChatGPT.

La publication avec Sites se déroule en deux étapes distinctes :

1. **Enregistrez une version.** ChatGPT génère une version déployable. Pour un projet source
   local, ChatGPT associe la version au commit Git utilisé pour le
   build. Utilisez cette étape pour obtenir une version candidate au déploiement que vous pourrez examiner.
2. **Déployez une version.** ChatGPT publie une version enregistrée et indique
   l’URL de production lorsque le déploiement réussit. Utilisez cette étape uniquement si vous souhaitez que
   le public sélectionné puisse accéder au site.

Demandez à ChatGPT de répertorier ou d’examiner les versions enregistrées lorsque vous devez retrouver une
version antérieure candidate au déploiement.

## Choisissez une architecture de site prise en charge

Pour les nouveaux projets, le workflow Sites peut partir du modèle de démarrage de site
recommandé. Pour un projet existant, demandez à ChatGPT de confirmer que le projet peut
produire des artefacts de déploiement compatibles avant de demander un déploiement.

Indiquez à ChatGPT le fonctionnement attendu du produit afin qu’il puisse sélectionner l’architecture
de site appropriée :

| Besoin du site                                                      | Ce qu’il faut demander à Sites                                                         |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Site web axé sur le contenu ou page de destination                            | Un site sans état applicatif persistant, sauf si l’expérience l’exige |
| Enregistrements sauvegardés, progression des utilisateurs ou scores de jeu                   | D1, une base de données relationnelle pour les données structurées persistantes                         |
| Images, documents, fichiers audio ou vidéo, ou autres fichiers importés              | R2, un stockage d’objets pour les fichiers                                                  |
| Fichiers importés avec des métadonnées permettant la recherche                        | D1 pour les métadonnées et R2 pour le contenu des fichiers                                      |
| Site interne qui nécessite l’identité de l’utilisateur actuel de l’espace de travail | Identité de l’utilisateur authentifié dans l’espace de travail                                         |
| Connexion publique ou fournisseur d’identité externe                | Un site avec authentification activée                                                |

Ne demandez pas de stockage durable pour un état d’affichage temporaire, comme le choix d’un thème ou la fermeture d’une bannière. Demandez-en pour les données de l’application que les utilisateurs s’attendent à voir conservées par le site hébergé.

## Gérez les accès et les secrets

Un nouveau site est accessible uniquement à son propriétaire et aux administrateurs de l’espace de travail tant que vous n’en modifiez pas l’accès. Gardez l’accès restreint pendant que vous vérifiez le contenu, le traitement des données et le public visé.

Selon les paramètres de votre compte et de votre espace de travail, les options de partage peuvent inclure :

- **Propriétaire et administrateurs de l’espace de travail**
- **Utilisateurs actifs ou groupes sélectionnés**, si cette option est disponible
- **Visiteurs externes invités**, lorsque les invitations externes sont disponibles
- **Toute personne de l’espace de travail**, si cette option est disponible
- **Toute personne sur Internet**, uniquement si la publication publique est activée

L’accès visiteur permet de consulter le site, mais ne donne pas le droit de le modifier. Dans les espaces de travail Entreprise, la publication publique est désactivée par défaut et doit être activée par un administrateur.

En cas de partage restreint, les visiteurs invités doivent se connecter avec le compte auquel l’accès a été accordé. Un site public est accessible sans accès à un espace de travail ChatGPT. Le paramètre définissant le public d’un site et toute fonctionnalité de connexion intégrée au site sont des contrôles distincts.

Par exemple :

```text
Change this Site's access to everyone in my workspace after showing me the
current Site and confirming its URL.

### Invitez des personnes extérieures à votre espace de travail

Les invitations externes permettent de donner accès à un site à des personnes précises sans le rendre public. Vous pouvez inviter des visiteurs extérieurs à votre espace de travail ou partager un site privé depuis un compte personnel. Cette fonctionnalité est en cours de déploiement auprès des utilisateurs de Sites disposant d’un forfait Plus, Pro, Business ou Entreprise.

1. Ouvrez un site dont vous êtes propriétaire et sélectionnez **Partager**.
2. Pour que le site reste privé, définissez **Qui a accès** sur **Uniquement les personnes invitées**.
3. Saisissez l’adresse e-mail du visiteur sous **Rechercher des personnes ou des groupes**, ou
**Saisir une adresse e-mail** pour un site personnel, puis sélectionnez le destinataire.
4. Vérifiez le public et les droits d’accès **Visiteur** du destinataire, puis sélectionnez
**Inviter**.
5. Vérifiez que le visiteur apparaît dans la liste enregistrée des personnes ayant accès au site. Partagez le lien du site et demandez-lui de se connecter avec le compte auquel l’accès a été accordé.

Les visiteurs externes peuvent ouvrir et utiliser le site. Ils ne deviennent ni membres de l’espace de travail ni éditeurs du site, et ne peuvent ni le modifier ni le publier. L’invitation donne accès à ce site ; vérifiez son contenu et les données auxquelles il est connecté avant de le partager.

Dans Entreprise, les administrateurs gèrent l’option **Autoriser les membres à inviter des visiteurs externes sur
des sites** sous **Paramètres de l’espace de travail \> Autorisations et rôles**. Cette autorisation
est distincte de celle permettant de publier des sites publiquement.
Les espaces de travail Business n’ont pas d’option distincte pour autoriser
les invitations externes ; Sites doit être activé et la fonctionnalité doit être disponible pour le compte.
Si l’option d’invitation n’apparaît pas, vérifiez le compte sélectionné, le propriétaire
du site, les autorisations de l’espace de travail et la disponibilité de la fonctionnalité à ce stade du déploiement.

Pour retirer un visiteur, ouvrez les paramètres de partage du site et supprimez son accès. Vérifiez également les autres paramètres définissant le public : supprimer une invitation ne retire pas l’accès dont la personne dispose grâce au partage public, avec l’espace de travail ou avec un groupe.

### Collaborez sur un site

La collaboration sur un site nécessite un espace de travail. Lorsque cette fonctionnalité est disponible, le propriétaire d’un site peut inviter des membres actifs du même espace de travail en tant qu’éditeurs.

Les éditeurs peuvent consulter les données de production contenues dans la base de données du site. N’invitez que des personnes à qui vous faites confiance pour accéder au code et aux données du site.

1. Ouvrez le site et sélectionnez **Partager**.
2. Sous **Ajouter des personnes ou des groupes**, recherchez et sélectionnez un membre de l’espace de travail. Cette personne
   est ajoutée en tant que visiteur.
3. Ouvrez le menu **Peut consulter** à côté de cette personne, puis choisissez **Peut modifier**. Les droits d’accès sont enregistrés
   automatiquement. Le site apparaît sous **Partagés avec vous** dans la vue
   Sites du membre.
4. L’éditeur peut ouvrir le site, apporter des modifications, enregistrer des versions et publier des mises à jour une fois que le propriétaire a publié le site pour la première fois.

Le propriétaire du site gère les droits des éditeurs et peut attribuer le rôle d’éditeur à un visiteur existant,
faire passer les droits d’un éditeur à **Peut consulter** ou lui retirer l’accès. La coédition
n’ajoute pas d’option d’autorisation distincte au niveau de l’espace de travail.

Les éditeurs ne peuvent pas modifier le public du site, inviter ou retirer d’autres personnes, gérer les paramètres ou les données d’analyse, restaurer une version antérieure ni transférer la propriété. Ils ne peuvent pas non plus effectuer la première publication du site : le propriétaire doit publier le site avant que les éditeurs puissent publier des mises à jour ultérieures.

Les droits de modification sont distincts des droits de consultation. Les étapes ci-dessus ajoutent d’abord la personne en tant que visiteur, puis lui accordent les droits de modification. Attribuer le rôle d’éditeur à un visiteur ne modifie pas le paramètre définissant le public du site.

### Configurez les valeurs de l’environnement d’exécution

Ouvrez **Sites**, puis les paramètres du site pour ajouter, mettre à jour ou supprimer
des variables d’environnement et des secrets dans l’environnement hébergé. N’incluez aucune valeur secrète dans les prompts, les fichiers
joints ou le contenu du site.

Accédez à [chatgpt.com/sites](https://chatgpt.com/sites), recherchez le site, puis sélectionnez
**Plus d’actions** \> **Paramètres**.

Ne stockez pas ces valeurs dans `.openai/hosting.json`. Gardez les fichiers locaux `.env` et
`.env.example` à jour avec les clés nécessaires au développement local, et
n’incluez aucune valeur secrète dans vos commits.

Lorsque vous ajoutez, mettez à jour ou supprimez des valeurs de l’environnement hébergé, demandez à ChatGPT de redéployer la version enregistrée et approuvée afin que le prochain déploiement utilise la configuration mise à jour.

## Modifiez l’URL d’un site

Lorsque la modification de l’URL est disponible, les propriétaires peuvent modifier l’URL hébergée par ChatGPT associée à un site existant sans créer de nouveau déploiement.

1. Ouvrez **Sites**, recherchez le site, puis ouvrez ses paramètres.
2. Repérez l’URL du site, puis sélectionnez **Modifier l’URL**.
3. Saisissez un nom disponible. Il doit comporter au moins cinq caractères, commencer par une lettre minuscule et ne contenir que des lettres minuscules, des chiffres et des tirets simples. Il ne peut ni se terminer par un tiret ni contenir de tirets consécutifs.
4. Confirmez la modification, puis patientez pendant que Sites met l’adresse à jour.

La modification de l’URL ne crée pas de nouveau déploiement. L’ancienne adresse redirige vers la nouvelle, en conservant les routes et les paramètres de requête.

La modification de l’URL hébergée par ChatGPT n’ajoute, ne supprime et ne modifie aucun domaine personnalisé. Les domaines personnalisés sont une fonctionnalité distincte qui existe déjà ; utilisez les paramètres des domaines personnalisés lorsque cette fonctionnalité est disponible.

## Connectez un domaine personnalisé

Lorsque les domaines personnalisés sont disponibles, vous pouvez connecter un domaine racine ou un sous-domaine que vous possédez déjà. Sites n’enregistre pas les domaines à votre place ; vous devez donc pouvoir modifier les enregistrements DNS du domaine. Au lancement, les domaines personnalisés ne sont pas disponibles dans les espaces de travail Entreprise.

Pour connecter un domaine :

1. Ouvrez les paramètres du site et sélectionnez **Ajouter un domaine**.
2. Saisissez le domaine racine ou le sous-domaine que vous souhaitez utiliser.
3. Copiez les enregistrements DNS et les valeurs fournis par Sites, puis ajoutez-les dans l’interface de votre fournisseur de domaine.
4. Patientez quelques minutes, revenez aux paramètres du site, puis actualisez l’état du domaine.

Vous pouvez également demander à ChatGPT de vous aider à faire pointer le domaine vers votre site. Si la navigation ou l’utilisation de l’ordinateur est activée, ChatGPT peut vous guider dans l’interface de votre fournisseur de domaine après votre connexion.

## Vérifiez le site avant de le partager

Avant de partager un site :

- Vérifiez son contenu, les textes et images générés, les liens, les fichiers importés, les formulaires et le fonctionnement des éléments interactifs.
- Vérifiez qu’il n’expose aucune information confidentielle ou sensible, aucune valeur secrète ni aucun contenu tiers que vous n’êtes pas autorisé à partager.
- Testez le site comme le ferait le public visé, notamment ses mécanismes d’accès et de connexion.
- Vérifiez les fonctionnalités qui collectent des informations personnelles ou d’autres contenus fournis par les visiteurs. Décidez si le site doit collecter, partager ou publier ces informations.
- Si le site utilise la connexion avec ChatGPT, expliquez quelles informations sur les visiteurs il reçoit et comment il les utilise.
- Si le site collecte ou traite des données personnelles, respectez
[les lois applicables en matière de respect de la vie privée et de protection des données](https://help.openai.com/en/articles/20001340).
- Choisissez l’option de partage la plus restrictive qui convient au public visé.
- Ouvrez le Site partagé et vérifiez que le public visé peut y accéder.

Pour un Site créé à partir d’un projet local, examinez également les modifications du code source et les éventuelles
migrations de base de données dans le [volet de révision](/fr-FR/codex/code-review?surface=app) de Codex.

## Retirer l’accès à un Site ou le supprimer

Pour retirer l’accès à un Site sans le supprimer, ouvrez ses paramètres de partage et limitez
l’accès à vous-même ou à certaines personnes. Vérifiez que le public qui y avait accès auparavant ne peut
plus l’ouvrir.

Pour supprimer définitivement un Site :

1. Ouvrez **Sites** et repérez le Site.
2. Sélectionnez **Supprimer le site** et suivez les instructions de la boîte de dialogue.
3. Saisissez le slug du Site, puis sélectionnez **Supprimer définitivement**.

La suppression d’un Site est définitive. Vous ne pouvez pas restaurer un Site supprimé.

## Comprendre les limites et les usages non pris en charge

Sites héberge des expériences web qui s’exécutent dans l’environnement d’exécution pris en charge par Sites. Certains
frameworks, réseaux privés, bases de données, services en arrière-plan et modes d’hébergement
ne sont pas pris en charge.

HTTP, HTTPS et WebSockets sont pris en charge. Les connexions TCP brutes entrantes et sortantes
ne le sont pas.

Chaque Site est soumis aux limites de stockage suivantes :

| Ressource            | Limite                  |
| ------------------- | ---------------------- |
| Stockage de la base de données D1 | 10 Go                  |
| Stockage d’objets R2   | Aucune limite de stockage fixe |

À son lancement, Sites ne prend pas en charge la résidence des données ni celle de l’inférence. Cela
concerne les Sites déployés, leur code, le stockage des données et des fichiers dans D1 et R2, les artefacts générés
et les journaux.

N’utilisez pas Sites pour traiter des informations de santé protégées ou des données de cartes de paiement ;
cibler des enfants de moins de 13 ans ou n’ayant pas atteint l’âge du consentement numérique applicable ; permettre
des transactions financières ; diffuser des logiciels malveillants ; faciliter l’hameçonnage ; usurper l’identité de personnes
ou d’organisations ; ou enfreindre de toute autre manière les politiques d’OpenAI. Consultez
[Créer et gérer des Sites ChatGPT](https://help.openai.com/en/articles/20001339)
pour connaître les limites actuelles et obtenir les liens vers les politiques applicables.

## Documentation associée

- La page [Application de bureau ChatGPT](/fr-FR/codex/app) présente la navigation dans l’application, les projets et les discussions.
- La page [Réviser et publier les modifications](/fr-FR/codex/code-review?surface=app) explique comment examiner les modifications du code source
  avant de les publier.

- La page [Projets et discussions](/fr-FR/codex/projects) explique comment le contexte des dossiers et de l’espace de travail
  est conservé d’une discussion à l’autre.
- La page [Réviser et publier les modifications](/fr-FR/codex/code-review) explique le workflow de révision pour
  chaque client Codex.
- La page [Bac à sable](/fr-FR/codex/sandboxing) explique le périmètre de l’exécution locale.

- [Ouvrez Sites dans ChatGPT](https://chatgpt.com/sites) pour retrouver les Sites que vous avez
  créés.
- La page [Projets et discussions](/fr-FR/codex/projects?surface=web) explique comment regrouper
  les discussions et les fichiers sources associés.
- La page [Travailler avec des fichiers](/fr-FR/codex/artifacts-viewer?surface=web) explique comment examiner
  les fichiers générés dans ChatGPT sur le Web.
