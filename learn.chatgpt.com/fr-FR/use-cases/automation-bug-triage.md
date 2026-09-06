<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/automation-bug-triage -->

## Utilisation

Demandez à Codex de vérifier les sources où les bugs sont déjà signalés : alertes Sentry, tickets Linear, issues GitHub, vérifications de PR, journaux de déploiement, tickets d’assistance et fils Slack. Commencez par un passage en revue manuel, ajustez le rapport dans la discussion, puis planifiez son exécution.

Utilisez une seule discussion Codex pour l’ensemble du cycle de triage :

1. Effectuez un passage en revue à la demande et obtenez une liste provisoire.
2. Examinez la liste et faites vos retours dans cette même discussion.
3. Depuis cette discussion, planifiez une tâche de triage.
4. Facultatif : demandez à Codex de rédiger des tickets Linear, des mises à jour Slack, des commentaires GitHub ou des notes de relais lorsque le rapport vous paraît fiable.

Avant de commencer, installez les [plugins](/fr-FR/codex/plugins) dont Codex a besoin, par exemple Sentry, Slack, Linear ou GitHub. Dans le prompt de départ, remplacez la liste de plugins entre crochets par de véritables mentions `@` de plugins. Remplacez ensuite chaque source entre crochets par l’emplacement précis à rechercher : un projet ou une URL d’alerte Sentry, un canal ou un fil Slack, une équipe, une vue ou une requête Linear, un dépôt, une requête d’issues ou une vérification de PR GitHub, un lien de déploiement, un fichier journal, une file d’assistance ou un tableau de bord.

## Phase 1 : effectuer le passage en revue

Lancez Codex depuis le dépôt concerné par les bugs lorsque le contexte local est utile : tests, outils du dépôt, vérifications de build ou échecs de CI. Vous pouvez également effectuer le passage en revue depuis n’importe quel dépôt si vos sources de bugs sont accessibles via des plugins, des connecteurs, des serveurs MCP, des liens, des exportations, des journaux collés ou des pièces jointes.

Commencez par exécuter le prompt de départ ci-dessus. Ne conservez que les plugins et les sources qui font partie de votre passage en revue.

Par exemple, un prompt complété peut nommer les plugins ainsi que les files d’attente, canaux ou dépôts précis à inclure dans le passage en revue.

<div class="not-prose mb-12 rounded-xl bg-[url('/images/codex/codex-wallpaper-1.webp')] bg-cover bg-center p-4 md:p-8">
  
</div>

## Phase 2 : rendre le rapport exploitable

Avant d’automatiser le processus, assurez-vous que le rapport sera utile au quotidien.

Une première exécution exploitable comprend :

- Des bugs pertinents classés de P0 à P3.
- Les signalements en double sont regroupés sous un même bug.
- Chaque bug comporte des liens vers les éléments probants ou de courtes citations.
- Les suppositions sont séparées des faits observés.
- Chaque bug est assorti d’une brève recommandation sur la prochaine action à mener.

Ajustez le rapport dans la même discussion avant d’en planifier l’exécution. Vous pouvez demander à Codex de :

- Consulter une source supplémentaire avant de classer la liste.
- Écarter les alertes parasites que l’équipe connaît déjà.
- Ne renvoyer que les bugs P0 et P1.
- Regrouper les signalements Slack, les alertes Sentry et les échecs GitHub lorsqu’ils correspondent au même bug.
- Afficher uniquement le meilleur lien pour chaque bug.
- Ajouter suffisamment d’éléments probants pour qu’une autre personne puisse reproduire le problème ou le transmettre à la bonne équipe.

## Phase 3 : automatiser le triage

Lorsque le rapport généré à la demande est exploitable, restez dans la même discussion et [planifiez depuis celle-ci une tâche de triage](/fr-FR/codex/automations#schedule-a-task-inside-a-chat). Codex peut s’appuyer sur vos ajustements dans la discussion pour rédiger le prompt récurrent.

**Planifier la tâche de triage**

## Phase 4 : orienter les actions de suivi

Une fois le rapport planifié exploitable, décidez de la suite à donner. Codex peut rédiger une mise à jour Slack pour un canal d’équipe, préparer des issues Linear pour les bugs que vous souhaitez suivre, rédiger des commentaires GitHub sur une PR dont les vérifications échouent ou préparer une note de passation pour la personne d’astreinte.
