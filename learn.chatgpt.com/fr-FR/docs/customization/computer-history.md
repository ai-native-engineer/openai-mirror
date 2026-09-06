<!-- source: https://learn.chatgpt.com/fr-FR/docs/customization/computer-history -->

L’Historique de l’ordinateur est **désactivé par défaut** pour les utilisateurs de ChatGPT Pro, Business et
  Entreprise dans l’application de bureau ChatGPT sur macOS. Les utilisateurs Pro peuvent choisir de
  l’activer. Pour les espaces de travail Business et Entreprise, un administrateur doit
  explicitement accorder l’accès avant que chaque membre puisse choisir de l’activer.
  L’Historique de l’ordinateur nécessite également les [Mémoires](/fr-FR/codex/customization/memories) et n’est pas
  disponible avec une clé API ni avec Amazon Bedrock. Cette fonctionnalité est disponible dans les régions prises
  en charge, notamment dans l’Espace économique européen (EEE), en Suisse et au
  Royaume-Uni.

L’Historique de l’ordinateur transforme votre activité sur les applications et les sites web en mémoires et
en une chronologie consultables par ChatGPT et Codex. Vous pouvez poser des questions en langage naturel
sur votre travail récent, reprendre là où vous en étiez, comprendre vos habitudes de
travail et transformer vos workflows récurrents en skills ou en automatisations.

Votre historique ne démarre que si vous choisissez de l’activer. Vous contrôlez quelles applications
et quels sites web y contribuent, pouvez consulter et suspendre la collecte depuis la barre des menus de macOS,
et pouvez examiner ou supprimer votre historique à tout moment.

L’Historique de l’ordinateur remplace l’ancienne préversion de recherche Chronicle, mais il s’agit d’un
système reconstruit, et non d’un simple changement de nom. Il utilise des événements
d’interaction, ainsi que du texte et d’autres éléments de contexte accessibles grâce aux fonctionnalités
d’accessibilité de macOS, pour créer des résumés que vous pouvez consulter et supprimer. Il n’inclut
aucune capture d’écran dans votre historique, n’enregistre pas d’audio et ne prend jamais en compte
votre activité de navigation web en mode privé.

  

## À quoi sert l’Historique de l’ordinateur

L’Historique de l’ordinateur apporte du contexte grâce à votre activité récente. Si un fichier, une conversation
Slack, un document Google Docs ou une autre source convient mieux à la tâche, ChatGPT et
Codex peuvent utiliser l’historique pour identifier cette source, puis la consulter directement.

<section class="feature-grid mt-4">

<div>

### Reprenez là où vous en étiez

Demandez ce que vous faisiez avant une pause sans avoir à retrouver chaque application ouverte,
chaque document consulté et chaque étape à venir.

</div>

</section>

<section class="feature-grid inverse">

<div>

### Retrouvez vos travaux récents

Décrivez un document, une conversation ou une tâche comme vous vous en souvenez.
L’Historique de l’ordinateur peut utiliser la chronologie de votre activité pour identifier la source concernée.

</div>

</section>

<section class="feature-grid">

<div>

### Réutilisez vos workflows

Lorsque l’Historique de l’ordinateur repère une tâche répétitive, une entrée de la chronologie peut suggérer une
skill ou une automatisation. Examinez la suggestion, puis demandez à Codex de la créer à partir
du workflow enregistré.

</div>

</section>

## Fonctionnement de l’Historique de l’ordinateur

L’Historique de l’ordinateur crée un flux d’événements d’interaction à partir des applications et
sites web autorisés. Ces événements peuvent inclure les clics, la saisie de texte, les raccourcis clavier, les changements d’application
et les informations contextuelles fournies par le système d’accessibilité de macOS. L’Historique de l’ordinateur
transforme régulièrement ces événements en résumés textuels et en fichiers mémoire locaux.

L’Historique de l’ordinateur n’inclut aucune capture d’écran dans votre historique et n’enregistre
ni le son capté par le microphone ni celui du système. L’activité de navigation web en mode privé n’est jamais
incluse.

Dans **Paramètres \> Historique de l’ordinateur \> Historique**, la chronologie regroupe les résumés par
jour et par heure. Chaque élément peut afficher :

- Un titre et un résumé textuel de l’activité.
- Les applications ayant contribué au résumé.
- Une skill ou une automatisation suggérée lorsque ChatGPT repère des tâches répétitives.
- Des actions permettant d’afficher le fichier mémoire dans le Finder ou de supprimer l’élément.

Sélectionnez **Poser une question sur votre historique** pour démarrer une discussion avec l’Historique de l’ordinateur, ou utilisez
des prompts tels que :

- « Sur quoi travaillais-je avant ma dernière pause ? »
- « Où puis-je trouver le document de proposition que je cherchais plus tôt aujourd’hui ? »
- « Donne-moi la liste des tâches sur lesquelles j’ai travaillé aujourd’hui et leur état d’avancement. »
- « Prépare un résumé de ce que j’ai fait hier pour le stand-up. »

## Autorisations et accès

L’Historique de l’ordinateur utilise des paramètres distincts pour l’accès à l’espace de travail, l’activation individuelle,
les mémoires, ainsi que les applications et sites web inclus dans votre historique :

- **Accès à l’espace de travail :** l’Historique de l’ordinateur est désactivé par défaut dans les espaces de travail Business et
  Enterprise. Il reste inaccessible tant qu’un administrateur n’en a pas
  explicitement autorisé l’accès. Les administrateurs Enterprise peuvent utiliser l’option **Activer l’Historique
  de l’ordinateur** dans [**Paramètres de l’espace de travail \> Autorisations et rôles**](https://chatgpt.com/admin/settings)
  pour accorder cet accès aux rôles appropriés de l’espace de travail.
- **Activation individuelle :** accorder l’accès au niveau de l’espace de travail permet seulement à un membre de choisir
  d’activer l’Historique de l’ordinateur. Cet accès n’active la fonctionnalité pour personne. Chaque
  utilisateur doit l’activer individuellement, y compris les utilisateurs de ChatGPT Pro.
- **Mémoires :** l’Historique de l’ordinateur nécessite également les [Mémoires](/fr-FR/codex/customization/memories).
  Utilisez `/memories` pour déterminer si une discussion donnée peut utiliser des mémoires locales
  ou contribuer aux mémoires futures.
- **Applications et sites web :** les autorisations accordées à vos applications et sites web déterminent les
  sources qui peuvent fournir des événements d’interaction. Vous pouvez n’autoriser que certaines
  sources ou exclure les applications et les URL de sites web que vous ne souhaitez pas inclure.

Si votre rôle dans l’espace de travail ne dispose pas de l’accès requis, modifier les paramètres locaux ne permet pas
d’activer l’Historique de l’ordinateur.

## Activer l’Historique de l’ordinateur

L’Historique de l’ordinateur est désactivé par défaut. Si vous utilisez un espace de travail Business ou Enterprise,
demandez à votre administrateur de vous accorder l’accès avant de l’activer.
L’approbation de l’administrateur ne l’active pas pour vous.

1. Ouvrez l’application de bureau ChatGPT sur macOS.
2. Dans Paramètres, sous **Intégrations**, sélectionnez **Historique de l’ordinateur**.
3. Sélectionnez **Activer** , puis consultez les informations sur la confidentialité, les autorisations et
   le stockage local.
4. Si vous y êtes invité, activez **Mémoires**. L’Historique de l’ordinateur nécessite la fonctionnalité Mémoires pour
   utiliser le contexte de votre activité dans différentes discussions et tâches.
5. Choisissez les applications et sites web qui peuvent alimenter votre historique, puis répondez
aux éventuelles demandes d’autorisation de macOS.

L’Historique de l’ordinateur ne nécessite pas l’autorisation Enregistrement de l’écran. Si ce paramètre
n’apparaît pas, vérifiez que votre abonnement permet d’utiliser l’Historique de l’ordinateur et, le cas échéant,
que l’administrateur de votre espace de travail l’a activé.

## Gérer les éléments inclus

Vous choisissez les applications et sites web qui alimentent votre historique à venir et décidez
si l’Historique de l’ordinateur collecte activement des événements d’interaction.

### Choisir les applications et les sites web

Dans **Paramètres \> Historique de l’ordinateur \> Autorisations**, choisissez les applications et les
sites web que l’Historique de l’ordinateur peut inclure :

- Les options **Exclure ces applications** et **Exclure ces sites web** bloquent les applications ou les URL
  indiquées, tout en autorisant les autres sources compatibles.
- Les options **Inclure uniquement ces applications** et **Inclure uniquement ces sites web** n’autorisent que les
  sources que vous choisissez explicitement.

Vous pouvez également sélectionner l’icône d’une application dans un élément de la chronologie de l’historique
pour exclure cette application de votre historique futur. Vous pourrez l’inclure de nouveau ultérieurement.

L’activité de navigation web en mode privé n’est jamais incluse. La modification des autorisations
accordées aux applications ou aux sites web ne concerne que l’historique futur. Pour retirer les éléments
existants, supprimez-les individuellement ou effacez l’historique.

### Suspendre, reprendre ou arrêter la collecte

Utilisez les paramètres de l’Historique de l’ordinateur ou la barre des menus de macOS pour contrôler quand
la fonctionnalité collecte votre activité :

- Sélectionnez l’icône ChatGPT dans la barre des menus de macOS, puis développez le menu Historique de l’ordinateur
pour consulter l’activité collectée et accéder à ses commandes.
- Sélectionnez **Suspendre** pour arrêter la collecte de nouveaux événements d’interaction, ou sélectionnez
**Reprendre** lorsque vous souhaitez recommencer.
- Désactivez l’Historique de l’ordinateur pour arrêter toute collecte d’activité future.

L’Historique de l’ordinateur peut inclure des événements d’interaction provenant d’applications
et de sites web de communication. Désactivez-le lorsque vous échangez avec d’autres personnes, sauf si elles
vous ont donné leur consentement préalable et explicite. Envisagez de le suspendre ou d’exclure les applications
qui contiennent des informations médicales, financières ou personnelles sensibles.

## Consulter et effacer l’historique

Ouvrez **Paramètres \> Historique de l’ordinateur \> Historique** pour consulter les résumés créés par l’Historique
de l’ordinateur. Vous pouvez afficher le fichier mémoire local associé à un résumé dans le Finder, supprimer
un élément de la chronologie ou effacer les 10 dernières minutes, la dernière heure, la dernière journée
ou l’intégralité de l’historique. La barre des menus de macOS permet également d’effacer la dernière session d’une
application récemment utilisée.

Effacer l’historique supprime les événements d’interaction correspondants ainsi que les mémoires
créées à partir de ces événements. Cette opération est irréversible.

## Confidentialité et stockage local

L’Historique de l’ordinateur stocke temporairement le flux d’événements d’interaction sur votre Mac afin que
ChatGPT et Codex puissent générer des mémoires et élaborer des suggestions de workflows. Ce flux
peut inclure des activités comme les clics et la saisie de texte, ainsi que du texte et d’autres informations
contextuelles accessibles grâce aux fonctionnalités d’accessibilité de macOS. L’Historique de l’ordinateur
n’inclut aucune capture d’écran dans votre historique et n’enregistre ni le son capté par le microphone
ni celui du système. L’activité de navigation web en mode privé n’est jamais incluse.

Les fichiers d’événements temporaires sont conservés pendant 48 heures au maximum. Les fichiers mémoire générés
restent dans votre système de fichiers jusqu’à leur suppression ou à l’effacement de l’historique, et vous pouvez afficher
ces fichiers depuis la chronologie Historique.

### Où l’Historique de l’ordinateur stocke-t-il mes données ?

L’Historique de l’ordinateur enregistre temporairement les événements d’interaction sur votre Mac. Les fichiers
d’événements sont isolés dans
l’[App Group](https://developer.apple.com/documentation/xcode/protecting-local-app-data-using-containers) de ChatGPT,
ce qui empêche les autres applications d’y accéder sans autorisation explicite.
ChatGPT et Codex suppriment ces fichiers d’événements au bout de 48 heures.

L’Historique de l’ordinateur génère le même type de mémoires locales que Codex : des fichiers Markdown en texte
brut que vous pouvez lire et modifier. Ces fichiers sont stockés
dans `$CODEX_HOME/memories/extensions/skysight/`, qui correspond généralement à
`~/.codex/memories/extensions/skysight/`.

<div className="not-prose my-4">
  
</div>

### Quelles données sont partagées avec OpenAI ?

L’Historique de l’ordinateur collecte localement les événements d’interaction, puis démarre périodiquement
une session Codex éphémère qui a accès au flux d’événements d’interaction pour
résumer votre activité sous forme de mémoires.

OpenAI traite les fichiers d’événements temporaires sur ses serveurs pour générer des mémoires,
qui sont ensuite stockées localement sur votre Mac. OpenAI ne conserve pas ces fichiers d’événements
après leur traitement, sauf si la loi l’exige, et ne les utilise pas pour
l’entraînement.

Lorsque ChatGPT ou Codex utilise une mémoire dans une discussion ultérieure, les contenus pertinents de cette mémoire
et les événements d’interaction peuvent être inclus dans le contexte. Le contenu de cette discussion peut être
utilisé pour améliorer les modèles OpenAI si vos
[paramètres de gestion des données de ChatGPT](https://help.openai.com/en/articles/7730893-data-controls-faq) l’autorisent.
Les mémoires sont également soumises aux mêmes
[paramètres propres à chaque discussion que les autres mémoires Codex](/fr-FR/codex/customization/memories#control-memories-per-chat).

### Risque d’attaque par injection de prompt

L’Historique de l’ordinateur augmente le risque d’attaque par injection de prompt lié au contenu des applications
et des sites web. Par exemple, si vous consultez un site web contenant des instructions malveillantes,
ChatGPT ou Codex pourrait les suivre.

## Utilisation des tokens

L’Historique de l’ordinateur utilise des tokens lorsqu’il résume l’activité et crée des mémoires.

## Dépannage

Si l’Historique de l’ordinateur est disponible mais ne démarre pas :

1. Vérifiez que la fonctionnalité **Mémoires** est activée.
2. Ouvrez **Paramètres \> Historique de l’ordinateur** , puis sélectionnez **Terminer la configuration**, **Reprendre**
   ou **Réessayer**, selon l’état affiché.
3. Quittez et rouvrez l’application de bureau ChatGPT si le paramètre reste indisponible.
