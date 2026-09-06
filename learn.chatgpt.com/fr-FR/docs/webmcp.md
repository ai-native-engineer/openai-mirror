<!-- source: https://learn.chatgpt.com/fr-FR/docs/webmcp -->

Les outils du site mettent en œuvre dans ChatGPT la proposition de
[norme WebMCP](https://webmachinelearning.github.io/webmcp/). Avec WebMCP,
un site web peut proposer des actions utiles directement à un agent d’IA, en complément de
l’interface que vous utilisez déjà. Vous et l’agent pouvez travailler sur la même page en temps réel
et dans la même session authentifiée.

Dans le [navigateur intégré](/fr-FR/codex/browser) de l’application de bureau ChatGPT,
ChatGPT Work et Codex peuvent découvrir et utiliser ces outils lorsqu’ils sont disponibles.

  Utilisez GPT-5.6 Sol ou GPT-5.6 Terra pour les outils du site. WebMCP est actuellement
désactivé pour GPT-5.6 Luna. Mettez l’application de bureau ChatGPT à jour vers la dernière version. Les outils
du site ne sont pas disponibles dans les espaces de travail Entreprise ou Edu. Leur disponibilité dépend aussi
du déploiement et des outils fournis par la page en cours.

## Comparaison entre WebMCP et MCP

Le [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/learn/architecture)
connecte une application d’IA à un serveur local ou distant. Ses outils peuvent fonctionner
indépendamment d’une page web ouverte, par exemple pour effectuer des recherches dans un service ou gérer
des enregistrements via une API.

Grâce à [WebMCP](https://github.com/webmachinelearning/webmcp), un site web peut mettre ses
fonctionnalités à la disposition d’un agent sous la forme d’un ensemble d’outils prédéfinis. L’agent peut
les découvrir lorsqu’il visite le site. Les utilisateurs n’ont donc pas besoin d’installer un serveur MCP
distinct ni de configurer une autre connexion pour utiliser ces fonctionnalités.

Cette approche est utile lorsque vous et l’agent devez voir la même chose, par exemple
pour modifier un canvas ou explorer un tableau de bord. Un
[plugin doté d’un serveur MCP](/fr-FR/codex/build-plugins) peut fournir une intégration
qui fonctionne indépendamment d’une page ouverte. Un site web peut prendre en charge les deux.

## Fonctionnement dans le navigateur

Ouvrez un site web dans le navigateur intégré et demandez à ChatGPT Work ou à Codex de vous aider
à accomplir une tâche. Si la page propose des outils du site, l’agent peut découvrir et utiliser les
actions pertinentes sur le site que vous consultez. Par exemple, un éditeur de documents
peut permettre à l’agent de trouver une section ou de laisser un commentaire que vous pourrez examiner.

Sélectionnez **Outils du site** dans la barre d’adresse du navigateur pour voir ce que le site
propose. Choisissez **Outils du site disponibles** pour examiner chaque outil. Le
navigateur vérifie chaque requête avant que le site ne l’exécute, et l’agent
peut examiner la page pour voir ce qui a changé. Lorsqu’une activité récente est disponible,
choisissez **Récemment utilisés** pour ouvrir **Sources** et examiner ces appels.

Dans cet exemple, développez **Outils du site disponibles** pour examiner les outils fournis
par [Margin](https://margin-local-docs.openai.chatgpt.site).

  

Les outils sont liés à la page qui les fournit. Si vous fermez une page ou la quittez pour en consulter
une autre, ses outils peuvent devenir indisponibles. Si aucun outil adapté n’est disponible,
l’agent peut tout de même être en mesure d’utiliser ses fonctionnalités habituelles de navigation.

## Exemple : explorez la documentation OpenAI

ChatGPT Learn et OpenAI Developers proposent des outils du site pour rechercher et lire de la
documentation. Sélectionnez **Ouvrir dans ChatGPT** dans la zone de saisie pour ouvrir Apprendre dans le
navigateur de l’application de bureau, à côté d’une nouvelle discussion où ce prompt est prêt à être envoyé.

L’agent peut utiliser ces outils pour rechercher, lire et ouvrir la page pertinente :

| Outil                    | Fonction                                                             |
| ----------------------- | ------------------------------------------------------------------------ |
| `search_openai_docs`    | Effectue une recherche dans la documentation OpenAI.                                           |
| `lookup_page`           | Lit une page de documentation à partir de son chemin ou de son URL.                               |
| `lookup_context`        | Lit la route de documentation actuelle et le texte sélectionné.                          |
| `navigate_to_page`      | Ouvre une page correspondante sur le site de documentation consulté.                 |
| `generate_custom_guide` | Lance la génération d’un guide personnalisé de développement ou d’apprentissage et renvoie son état et son lien. |

L’Agent de documentation génère un guide personnalisé de manière asynchrone. Recevoir son lien ne
signifie pas que la génération est terminée.

## Sécurité et contrôle par l’utilisateur

Les définitions et les résultats d’outils fournis par les sites web sont des contenus non fiables. Le nom d’un outil
ou l’affirmation selon laquelle il ne fait que lire des données ne prouvent pas ce qu’il fait réellement. Les instructions
d’un site web n’autorisent pas l’agent à partager des informations sans rapport avec la tâche ni
à effectuer des actions sensibles.

Dans le navigateur intégré, chaque appel d’outil fait l’objet d’une vérification de sécurité avant
son exécution. Les règles habituelles d’accès aux sites web et de confirmation continuent de s’appliquer, y compris
aux actions ayant des conséquences, comme l’envoi de messages, les achats, la suppression
de données ou la modification des autorisations. Le navigateur associe chaque appel à sa
page d’origine et à l’enregistrement de l’outil. Ces vérifications réduisent les risques ; elles ne
rendent pas un site web ni ses résultats dignes de confiance.

Vous pouvez désactiver l’option **Activer les outils du site** dans **Paramètres \> Navigateur \> Autorisations**.
Examinez le site, l’action demandée et le résultat avant de partager des informations sensibles
ou de vous fier à une modification.

Signalez les vulnérabilités de sécurité via le
[programme Bug Bounty consacré aux vulnérabilités de sécurité](https://bugcrowd.com/engagements/openai) d’OpenAI. Pour les risques liés à la sécurité
de l’IA, consultez le
[programme Bug Bounty pour la sécurité de l’IA](https://openai.com/index/safety-bug-bounty/). Respectez
le périmètre de chaque programme et ses consignes de soumission.

## Limites

Le navigateur intégré de ChatGPT ne prend actuellement en charge qu’une partie des API WebMCP.
Les fonctionnalités suivantes ne sont pas prises en charge :

- **API déclarative :** Les outils définis au moyen d’attributs de formulaires HTML ne sont pas
  disponibles en tant qu’outils du site.
- **Outils dans les iframes :** Le navigateur ne découvre pas les outils enregistrés dans les
  iframes, qu’elles soient de même origine ou d’origine différente.

Utilisez JavaScript pour enregistrer les outils dans la page de premier niveau, comme indiqué dans la
[section suivante](#add-webmcp-to-your-website). ChatGPT Work et Codex peuvent tout de même
interagir avec les formulaires à l’aide des fonctionnalités habituelles du navigateur, mais ces interactions
ne sont pas des appels d’outils WebMCP.

La spécification WebMCP et le guide de Chrome destiné aux développeurs couvrent un ensemble plus large
d’API, y compris des fonctionnalités que le navigateur intégré ne prend pas actuellement en charge.

## Ajoutez WebMCP à votre site web

Vous pouvez demander à Codex d’ajouter la prise en charge de WebMCP à l’application web ou au
[Site](/fr-FR/codex/sites) sur lesquels vous travaillez. Décrivez ce qu’un agent doit pouvoir
faire et demandez à Codex de réutiliser la logique et les autorisations existantes de l’application.

Commencez par une opération déjà prise en charge par votre application. Par exemple :

- Un tableau de bord qui permet à l’agent de définir une plage de dates et d’examiner les données sous-jacentes
à un graphique.
- Un éditeur de documents qui permet à l’agent de trouver une section, de suggérer une modification ou
de laisser un commentaire que vous pourrez examiner.
- Un outil de planification de voyages qui permet à l’agent de comparer les options et de mettre à jour un itinéraire
pendant que vous consultez la carte.

Vous pouvez aussi écrire le code vous-même. Dans le module JavaScript de votre page, vérifiez
que le navigateur prend en charge WebMCP et enregistrez un outil. Cet exemple en lecture seule renvoie le
titre de la page actuelle :

```javascript
if (typeof document.modelContext?.registerTool === "function") {
  await document.modelContext.registerTool({
    name: "get_page_title",
    description: "Read the title of the current page.",
    inputSchema: {
      type: "object",
      properties: {},
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true },
    execute: async () => ({ title: document.title }),
  });
}

Un agent compatible peut découvrir `get_page_title` et recevoir le titre actuel
de la page. Pour un outil qui accepte des arguments, décrivez-les dans le schéma
d’entrée et utilisez-les dans le gestionnaire `execute` pour appeler la logique
existante de votre application.

Limitez la portée des entrées, décrivez les effets de bord et renvoyez suffisamment d’informations pour
vérifier le résultat. Utilisez les mécanismes d’authentification,
d’autorisation et de validation des entrées déjà présents dans votre application. Conservez l’interface habituelle pour les utilisateurs,
ainsi que pour les navigateurs qui ne prennent pas en charge WebMCP.

Pour en savoir plus sur l’API et consulter des exemples, reportez-vous à la
[spécification WebMCP](https://webmachinelearning.github.io/webmcp/) et au
[guide de Chrome destiné aux développeurs](https://developer.chrome.com/docs/ai/webmcp).
