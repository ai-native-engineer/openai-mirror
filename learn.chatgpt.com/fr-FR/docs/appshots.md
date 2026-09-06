<!-- source: https://learn.chatgpt.com/fr-FR/docs/appshots -->

Les Appshots vous permettent d’envoyer la fenêtre de l’application au premier plan dans une discussion ChatGPT. Utilisez-les lorsque
vous travaillez dans une autre application sur votre ordinateur et souhaitez fournir
à ChatGPT le contexte de votre travail afin qu’il puisse vous aider à accomplir la tâche.

  Les Appshots sont disponibles dans l’application de bureau ChatGPT sur macOS. Appuyez simultanément sur les deux touches Commande,
ou utilisez le raccourci clavier personnalisé des Appshots pour en prendre un.

## Contenu capturé par les appshots

Un appshot capture uniquement la fenêtre au premier plan. Il peut inclure :

- Une image de la fenêtre visible.
- Le texte disponible dans cette fenêtre, y compris le texte visible et celui que l’application rend
accessible en dehors de la zone de défilement visible.

Une fois ajouté à une discussion, un appshot se comporte comme une pièce jointe. ChatGPT
stocke les appshots localement dans le fichier de session, comme les fichiers ou les images que vous joignez
manuellement.

## Quand utiliser les appshots

Utilisez les appshots lorsque ChatGPT a besoin du contexte d’une application Mac avant de pouvoir agir.

Exemples :

- Partagez une page de référence d’API et demandez à ChatGPT d’écrire un script qui l’utilise.
- Partagez la vue d’un e-mail ou d’un calendrier et demandez à ChatGPT de préparer l’étape suivante.
- Partagez une fenêtre d’éditeur d’images, de design ou d’aperçu et demandez à ChatGPT de réviser les
ressources ou le code associés.
- Partagez une erreur, un panneau de paramètres ou un état d’application plus facile à montrer qu’à
décrire.

## Prendre un appshot

1. Placez au premier plan la fenêtre de l’application que vous souhaitez partager.
2. Appuyez sur les deux touches Commande ou sur le raccourci clavier personnalisé configuré
dans les paramètres de ChatGPT.
3. Accordez les autorisations macOS si ChatGPT vous le demande.
4. Demandez à ChatGPT d’effectuer une tâche à l’aide de l’appshot.

  

Par défaut, ChatGPT ouvre une nouvelle discussion pour l’appshot. Si vous avez interagi avec une
discussion au cours des 60 dernières secondes, ChatGPT ajoute plutôt l’appshot à cette discussion
récente. Si vous prenez plusieurs appshots à la suite, ils sont ajoutés à la même discussion.

Vous pouvez modifier le raccourci clavier des Appshots dans les paramètres de l’application.

## Autorisations et sécurité

ChatGPT peut demander des autorisations avant de pouvoir prendre des appshots :

- **Enregistrement de l’écran et de l’audio système** permet à ChatGPT de capturer une image de la
  fenêtre au premier plan.
- **Accessibilité** permet à ChatGPT de lire le texte disponible dans la fenêtre au premier plan.

Lorsque vous prenez un appshot, l’image capturée et le texte disponible sont transmis à ChatGPT.
Évitez de prendre des appshots de contenu sensible, sauf si la tâche nécessite ce
contenu.

Examinez les appshots comme vous le feriez pour des captures d’écran et des documents avant de les partager
avec ChatGPT.

## Limites et dépannage

Les Appshots sont disponibles dans l’application de bureau ChatGPT sur macOS. Si vous reprenez une discussion
dans la CLI alors qu’elle contient déjà un appshot, la pièce jointe fait partie de l’historique de la discussion,
mais la CLI ne peut pas créer de nouvel appshot.

Pour certaines applications et certains sites web, notamment Google Docs, Gmail, Google Sheets et
Google Slides, ChatGPT peut ne recevoir que la capture d’écran visible et ne pas recevoir
le document complet ni le texte hors écran. Dans ChatGPT Work ou Codex, ChatGPT peut utiliser un
plugin compatible déjà installé pour accéder au contenu pertinent de l’application et vous aider à traiter votre
demande.

Si les appshots ne fonctionnent pas :

1. Ouvrez **Réglages Système \> Confidentialité et sécurité**.
2. Vérifiez les autorisations **Enregistrement de l’écran et de l’audio système** et **Accessibilité** pour la fonctionnalité Utilisation de
   l’ordinateur de Codex.
3. Redémarrez l’application et réessayez.
