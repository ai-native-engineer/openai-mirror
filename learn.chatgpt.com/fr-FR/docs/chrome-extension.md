<!-- source: https://learn.chatgpt.com/fr-FR/docs/chrome-extension -->

Utilisez l’extension de navigateur ChatGPT pour travailler dans Google Chrome, Microsoft Edge,
Brave, Opera ou Vivaldi depuis l’application de bureau ChatGPT. ChatGPT peut lire du contenu ou effectuer des actions
sur les sites auxquels vous êtes déjà connecté, comme LinkedIn, Salesforce, Gmail
ou des outils internes.

Les cinq navigateurs permettent de mentionner des onglets et de contrôler le navigateur depuis l’application
de bureau. Chrome, Edge, Brave et Vivaldi prennent également en charge la discussion latérale. **Opera ne prend pas en charge
la discussion latérale** ; démarrez ses tâches dans l’application de bureau.

Mettez à jour l’application de bureau ChatGPT avant de configurer un autre navigateur. La disponibilité des navigateurs
peut dépendre du déploiement et des paramètres de votre espace de travail.

Pour que ChatGPT contrôle plutôt son navigateur intégré, utilisez `@Browser`. Le
[navigateur intégré](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app)
permet de vous connecter et de garder votre activité de navigation dans ChatGPT sans utiliser votre
profil de navigateur habituel.

ChatGPT peut aussi passer d’un outil à l’autre selon les besoins de la tâche, en utilisant des plugins lorsqu’une
intégration dédiée est disponible, votre navigateur lorsqu’il a besoin du contexte des sites auxquels vous êtes
connecté, et le navigateur intégré pour localhost.

<div className="not-prose my-4">
  
</div>

<a id="use-chatgpt-from-chrome"></a>

## Utilisez la discussion latérale dans votre navigateur

La discussion latérale est disponible dans Chrome, Edge, Brave et Vivaldi.

Ouvrez ChatGPT à côté de la page que vous consultez pour poser des questions à son sujet ou passer
à des tâches qui peuvent utiliser son contexte avec vos fichiers locaux et vos applications connectées.
ChatGPT peut utiliser le contexte de vos onglets ouverts lorsqu’une tâche en a besoin.

1. Ouvrez la page avec laquelle vous souhaitez travailler.
2. Sélectionnez ChatGPT dans la barre d’outils du navigateur ou le menu **Extensions** . Sur macOS, vous
   pouvez également appuyer sur <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd>.
3. Posez une question sur la page ou confiez une tâche à ChatGPT.

Le panneau reste associé à l’onglet dans lequel vous l’avez ouvert. Les discussions démarrées dans la discussion latérale
sont disponibles dans l’application ChatGPT, et vous pouvez ouvrir vos discussions ChatGPT récentes dans
la discussion latérale. Vous pouvez ainsi poursuivre votre travail dans l’une ou l’autre interface.

  

## Ajoutez des onglets et du texte sélectionné à une discussion

Mentionnez un onglet de navigateur ouvert dans l’application de bureau lorsque vous souhaitez que ChatGPT utilise
cette page comme contexte. Dans les navigateurs proposant la discussion latérale, vous pouvez aussi y mentionner des onglets,
ou sélectionner du texte sur une page et l’ajouter à votre discussion pour
poser une question sur un passage précis sans copier toute la page.

Dans les navigateurs proposant la discussion latérale, vous pouvez aussi faire un clic droit sur la page et sélectionner
**Demander à ChatGPT**. La discussion latérale s’ouvre avec le contexte pertinent de la page pour vous permettre de
poursuivre votre demande dans le navigateur.

### Posez des questions sur une vidéo YouTube

Ouvrez une vidéo YouTube, puis posez une question à son sujet dans la discussion latérale d’un navigateur compatible.
Lorsque des sous-titres sont disponibles, ChatGPT peut utiliser la transcription horodatée de la vidéo
pour expliquer ou résumer son contenu, ou répondre à des questions à son sujet.

Considérez le contenu des pages web, le texte sélectionné et les transcriptions vidéo comme un contexte
non fiable. Vérifiez la page et toutes les autorisations demandées avant de demander à ChatGPT
d’utiliser ces informations ou d’agir en fonction de celles-ci.

<a id="set-up-the-chrome-extension"></a>

## Configurez votre navigateur

Installez le navigateur sur votre ordinateur, puis ouvrez **Paramètres \> Utilisation de l’ordinateur** dans
l’application de bureau ChatGPT. Développez **Autres navigateurs** si votre navigateur ne figure pas
dans la liste principale.

1. Sélectionnez votre navigateur et suivez les instructions à l’écran pour installer le plugin requis.
2. Sélectionnez **Installer** à côté du navigateur pour ouvrir la page de l’extension dans la boutique du navigateur.
   Installez l’extension ChatGPT et examinez les demandes d’autorisation du navigateur.
3. Revenez à **Utilisation de l’ordinateur** et vérifiez que le navigateur affiche **Gérer**.
4. Démarrez une discussion ChatGPT Work ou Codex et sélectionnez votre navigateur à l’aide d’une
mention `@`. Utilisez le profil de navigateur dans lequel vous avez installé l’extension.

Le bouton d’activation du navigateur dans **Utilisation de l’ordinateur** détermine s’il apparaît dans le
menu des mentions `@`. Pour modifier les autorisations des sites web, sélectionnez plutôt **Gérer** .

  

<a id="start-a-chrome-task-from-chatgpt"></a>

## Démarrez une tâche de navigateur depuis ChatGPT

Une fois la configuration terminée, démarrez une nouvelle discussion ChatGPT Work ou Codex. Sélectionnez **Chrome**, **Edge**,
**Brave Browser**, **Opera** ou **Vivaldi** dans le menu des mentions `@` pour choisir
le navigateur que ChatGPT utilise. Par exemple :

```text
@Edge open Salesforce and update the account from these call notes.

Vous pouvez aussi mentionner un onglet ouvert pour fournir à ChatGPT le contexte de cette page.
Opera prend en charge ces flux de travail depuis l’application de bureau, même s’il ne propose pas de discussion latérale.

## Contrôlez l’accès aux sites web

Par défaut, ChatGPT demande votre autorisation avant d’interagir avec chaque nouveau site web. ChatGPT formule
la demande en fonction de l’hôte du site web, par exemple `example.com`.

Lorsque ChatGPT demande à utiliser un site web, vous pouvez choisir l’option adaptée à la
tâche et à votre tolérance au risque :

- **Autoriser une fois** pour permettre à ChatGPT d’utiliser le site web une seule fois.
- **Autoriser pour ce site** pour permettre à ChatGPT de réutiliser le site web sans redemander d’autorisation.
- **Autoriser pour tous les sites** pour permettre à ChatGPT d’utiliser des sites web sans demander d’autorisation.
- **Refuser** pour empêcher ChatGPT d’utiliser le site web.

### Gérez les sites web autorisés et bloqués

Dans l’application de bureau ChatGPT, accédez à **Paramètres** \> **Utilisation de l’ordinateur**, puis sélectionnez
**Gérer** à côté de votre navigateur pour gérer une liste d’autorisation et une liste de blocage des
domaines. La liste d’autorisation contient les domaines que ChatGPT peut utiliser sans redemander d’autorisation.
La liste de blocage contient les domaines que ChatGPT ne doit pas utiliser. Les navigateurs pris en charge
partagent ces autorisations d’accès aux sites web.

Si vous retirez un domaine de la liste d’autorisation, ChatGPT redemande une autorisation avant de l’utiliser.
Si vous retirez un domaine de la liste de blocage, ChatGPT peut redemander une autorisation au lieu de
considérer le domaine comme bloqué.

#### Autoriser pour tous les sites 

Si vous sélectionnez **Autoriser pour tous les sites**, ChatGPT ne demande plus de confirmation
avant d’utiliser des sites web. Ne choisissez cette option que si vous faites confiance à ChatGPT pour utiliser n’importe quel
site web ouvert dans le navigateur.

#### Historique de navigation 

L’historique de navigation peut inclure des données de télémétrie sensibles, des URL internes, des termes de recherche,
ainsi que l’activité des sessions de navigation sur les appareils connectés à votre compte. Si vous autorisez ChatGPT à
accéder à l’historique de navigation, les entrées pertinentes de cet historique peuvent être intégrées au contexte que
ChatGPT utilise pour la tâche. Le contenu malveillant ou trompeur d’une page peut accroître le
risque que ChatGPT copie ces données vers un emplacement non prévu.

ChatGPT demande votre autorisation lorsqu’il souhaite utiliser l’historique de navigation. Il limite cet accès à
la demande en cours, et aucune option permettant de toujours l’autoriser n’est disponible.

## Données et sécurité

<a id="chrome-extension-permissions"></a>

### Autorisations de l’extension de navigateur

Votre navigateur vous demande d’accorder des autorisations lors de l’installation de l’extension.
Par exemple, la demande d’autorisation de Chrome peut inclure :

- Accéder au débogueur de page
- Lire et modifier toutes vos données sur tous les sites web
- Lire et modifier votre historique de navigation sur tous vos appareils connectés à votre compte
- Afficher des notifications
- Lire et modifier vos favoris
- Gérer vos téléchargements
- Communiquer avec les applications natives associées
- Afficher et gérer vos groupes d’onglets

Ces autorisations permettent à l’extension d’exécuter des flux de travail dans le
navigateur. ChatGPT s’appuie toujours sur ses propres confirmations, paramètres, listes d’autorisation et
listes de blocage avant d’utiliser des sites web ou l’historique de navigation au cours d’une tâche.

### Mémoires

La fonctionnalité Utilisation de l’ordinateur respecte le réglage choisi pour les Mémoires. Si les Mémoires sont activées, ChatGPT peut
utiliser les mémoires enregistrées pertinentes lorsqu’il travaille dans votre navigateur. Si elles sont désactivées,
le contrôle du navigateur n’utilise pas de mémoires.

### Données de navigation conservées par OpenAI

OpenAI ne conserve pas de journal complet distinct de vos actions de navigation via
l’extension. OpenAI ne conserve l’activité du navigateur que lorsqu’elle fait partie du contexte de ChatGPT,
par exemple le texte que ChatGPT lit sur une page, les captures d’écran, les appels d’outils,
les résumés, les messages ou tout autre contenu inclus dans la discussion.

Vos paramètres de contrôle des données dans ChatGPT s’appliquent au contenu traité dans le contexte.
Évitez d’envoyer des secrets ou des données hautement sensibles dans le cadre de tâches effectuées dans le navigateur, sauf
s’ils sont nécessaires et que vous êtes présent pour examiner chaque prompt.

## Dépannage

Si ChatGPT ne parvient pas à se connecter à votre navigateur, vérifiez d’abord que le site web auquel ChatGPT tente
d’accéder ne figure pas dans la liste de blocage dans les Paramètres. Si le site n’est pas bloqué, effectuez
les vérifications suivantes :

1. Mettez à jour l’application de bureau ChatGPT. Si plusieurs applications de bureau ChatGPT ou Codex sont installées,
mettez-les toutes à jour ou supprimez celles que vous n’utilisez plus.
2. Redémarrez votre navigateur. Dans Chrome, Edge, Brave ou Vivaldi, rouvrez ChatGPT depuis
   la barre d’outils ou le menu **Extensions** et vérifiez que la discussion latérale se charge. Opera
   ne propose pas de discussion latérale ; vérifiez sa connexion depuis l’application de bureau.
3. Dans **Paramètres \> Utilisation de l’ordinateur**, vérifiez que votre navigateur apparaît et affiche
**Gérer**. S’il affiche toujours **Installer**, suivez à nouveau la procédure de configuration.
   Activez son bouton bascule si le navigateur n’apparaît pas dans le menu des mentions `@`.
4. Vérifiez que vous utilisez bien le profil du navigateur dans lequel l’extension est
installée. Si vous utilisez plusieurs profils, installez et activez
l’extension dans le profil actif.
5. Démarrez une nouvelle discussion ChatGPT Work ou Codex et réessayez d’exécuter la tâche dans le navigateur. Cela peut
réinitialiser l’état de connexion propre à la discussion.
6. Redémarrez l’application de bureau ChatGPT, puis réessayez. Si l’extension ne parvient toujours pas
   à se connecter, réinstallez-la depuis **Paramètres \> Utilisation de l’ordinateur**.
7. Si ChatGPT ne peut toujours pas utiliser le navigateur, exécutez `/feedback`
   dans l’application et indiquez l’ID de la discussion lorsque vous contactez l’assistance.

### Importer des fichiers

Si une tâche Chrome doit importer un fichier depuis votre ordinateur, autorisez l’extension Chrome
à accéder aux URL de fichiers dans Chrome :

1. Dans Chrome, cliquez sur l’icône des extensions dans la barre d’outils, puis sur **Gérer les
   extensions**.
2. Sur la fiche de l’extension, cliquez sur **Détails**.
3. Activez **Autoriser l’accès aux URL de fichier**.

Une fois le paramètre modifié, relancez la tâche Chrome.
