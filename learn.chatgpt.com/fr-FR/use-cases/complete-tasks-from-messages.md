<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/complete-tasks-from-messages -->

## Introduction

De nombreux fils de discussion recèlent des tâches à accomplir : réserver une table, planifier un suivi, rechercher des options, transmettre un reçu ou rassembler les informations nécessaires à une réponse. La fonctionnalité Utilisation de l’ordinateur peut lire le fil, identifier la tâche et la mener à bien dans les applications concernées.

Cette approche convient lorsque le message contient une demande concrète et que vous souhaitez que ChatGPT s’occupe de la suite, au lieu de simplement résumer le fil de discussion.

## Comment l’utiliser

1. Installez le [plugin Utilisation de l’ordinateur](/fr-FR/codex/computer-use).
2. Demandez à ChatGPT d’examiner un fil de discussion précis ou les messages d’un expéditeur donné.
3. Indiquez-lui quelle action effectuer et s’il doit s’arrêter avant de la finaliser.
4. Précisez s’il doit préparer un brouillon de réponse dans le fil de discussion d’origine.

Par exemple :

- `@Computer Look at my messages from [person]. Check my availability, find 2 dinner options in Hayes Valley, and draft a reply in the same thread. Check in with me before completing booking.`

## Conseils pratiques

### Demandez à ChatGPT de s’arrêter avant toute action irréversible

Si la tâche peut impliquer l’envoi d’argent, le passage d’une commande, la confirmation d’une réservation ou la validation d’un planning, demandez à ChatGPT de s’arrêter et de vous consulter avant d’effectuer cette dernière étape.

### Vérifiez que les applications nécessaires sont prêtes

Cette méthode fonctionne mieux si les applications associées sont disponibles et qu’une session y est déjà ouverte. Si la tâche nécessite Plans, Calendrier, Notes, un site de réservation ou une session de navigateur, préparez à l’avance les éléments concernés.

### Attendez-vous à ce que le fil soit marqué comme lu

Lorsque ChatGPT ouvre le fil dans Messages, il se comporte comme n’importe quel utilisateur qui consulte la conversation. Considérez donc le fil comme lu.

## Pour aller plus loin

Cette même méthode peut aussi fonctionner dans d’autres interfaces de type boîte de réception, comme Slack ou la messagerie électronique, lorsqu’une tâche part d’un message et se termine ailleurs. Si ce workflow revient souvent, ajoutez une préférence ou une instruction réutilisable via la [personnalisation](/fr-FR/codex/customization/overview), afin que ChatGPT traite ces demandes de la même manière à chaque fois.

### Prompt suggéré

**Mener à bien une tâche à partir d’un fil de discussion**
