<!-- source: https://learn.chatgpt.com/fr-FR/docs/notifications -->

Les notifications vous avertissent lorsqu’une tâche requiert votre attention. Leurs réglages et
leurs canaux de diffusion varient selon l’interface.

## Configurer les notifications de bureau

Ouvrez [**Paramètres**](codex://settings) pour choisir quand les alertes de fin de tour
s’affichent : jamais, uniquement lorsque ChatGPT est en arrière-plan ou toujours. Des
réglages distincts permettent d’activer ou de désactiver les notifications relatives aux demandes d’autorisation et aux questions. Votre
système d’exploitation peut vous demander d’autoriser l’application de bureau
ChatGPT à envoyer des notifications.

### Suivre les discussions dans la vue Activité

Lorsque **Activité** est disponible, sélectionnez l’icône en forme de cloche dans la barre latérale pour afficher les discussions
non lues, en cours ou en attente de votre réponse. Vous pouvez également ouvrir ou
fermer la vue Activité avec <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>U</kbd> sous macOS
ou <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>U</kbd> sous Windows.

Utilisez les options de la vue pour choisir les discussions qui s’affichent. Selon l’interface
utilisée, les options peuvent inclure **Work**, **Discussion**, **Épinglées** et
**Planifiées**. Vous pouvez également sélectionner **Tout marquer comme lu** pour marquer comme lus tous les éléments non lus.

<a id="follow-task-activity-with-a-pet"></a>

### Suivre l’activité des discussions avec un compagnon

Dans l’application de bureau ChatGPT, un compagnon flottant vous permet aussi de suivre l’activité
des discussions pendant que vous travaillez dans d’autres applications. Il peut indiquer qu’une discussion est **En cours**,
**En attente d’une réponse**, **Prête** ou **Bloquée**.

Consultez [Compagnons](/fr-FR/codex/pets?surface=app) pour choisir un compagnon, comprendre son statut ou
créer le vôtre.

## Configurer les notifications web

Ouvrez **Paramètres \> Notifications** pour gérer les catégories et
les canaux de notification disponibles pour votre compte. En fonction de la catégorie et du compte,
les canaux peuvent inclure les notifications push, les e-mails ou les SMS. Sélectionnez **Gérer les tâches** dans les paramètres de notification
des tâches pour ouvrir **Planifiées**.

## Configurer les notifications de la CLI

Pour les notifications dans le terminal et les notifications externes, consultez
[Notifications](/fr-FR/codex/config-file/config-advanced#notifications) dans le
guide de configuration avancée. Vous pouvez choisir quand la TUI émet une notification
et si Codex exécute un programme externe lorsqu’un tour se termine.

<a id="follow-task-activity-in-the-ide"></a>

## Suivre l’activité des discussions dans l’IDE

L’extension IDE ne propose pas de réglages de notification distincts. Laissez la
discussion ouverte pour suivre son activité. Pour exécuter un programme externe lorsqu’un tour
se termine, configurez `notify` sur l’hôte Codex connecté. Consultez
[Notifications](/fr-FR/codex/config-file/config-advanced#notifications) dans le
guide de configuration avancée.

## Documentation associée

- [Tâches de longue durée](/fr-FR/codex/long-running-work)
- [Tâches planifiées](/fr-FR/codex/automations)
- [Compagnons](/fr-FR/codex/pets)
