<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/slack-action-triage -->

## Repérez les tâches cachées dans Slack

Une demande naît souvent dans Slack, alors que l’ensemble de son contexte se trouve ailleurs. Un membre de l’équipe peut demander une réponse dans un message direct, préciser l’action attendue dans un fil de discussion, partager le lien vers un document dans un canal, puis résoudre le problème plus tard sans vous mentionner à nouveau.

Utilisez ce workflow pour demander à ChatGPT d’analyser le contexte dans Slack, de vérifier si la demande est toujours d’actualité et de ne retenir que les quelques éléments qui nécessitent réellement votre attention. L’objectif est d’obtenir une liste d’actions classées par priorité : les éléments qui nécessitent une réponse, une décision, la prise de contact avec une personne, une mise à jour de la documentation ou un passage de relais.

## Lancez le triage

1. Indiquez à ChatGPT une période, un domaine d’activité, une personne, un canal ou un sujet.
2. Demandez-lui de rechercher dans les messages directs, les messages directs de groupe, les mentions dans les canaux et les réponses pertinentes des fils de discussion.
3. Demandez à ChatGPT de lire les derniers messages du fil avant de considérer un élément comme non résolu.
4. Demandez une liste d’actions classées par urgence et par impact.
5. Demandez à ChatGPT de préparer la réponse, le passage de relais ou la tâche de suivi.

Après avoir essayé ce workflow et l’avoir adapté à vos besoins, vous pouvez [planifier une tâche correspondant à cette activité depuis la discussion](/fr-FR/codex/automations#schedule-a-task-inside-a-chat) en demandant à ChatGPT d’effectuer la même opération à intervalles réguliers.

## Précisez le résultat attendu

Un résultat de triage utile doit expliquer pourquoi chaque élément est toujours d’actualité. Il doit aussi ignorer les anciennes demandes auxquelles quelqu’un a répondu plus tard dans le fil.

Vous devriez obtenir un résultat de ce type :

  <p>
    <strong>Action prioritaire :</strong> Priya demande des exemples concrets de clients,
    pas simplement d’autres idées.
  </p>
  <p>
    <strong>Pourquoi c’est important :</strong> le point sur le lancement doit citer de vraies personnes que
    l’équipe peut contacter cette semaine.
  </p>
  <p>
    <strong>Élément probant :</strong> le message initial dans le canal demandait des cas d’utilisation,
    mais un message ultérieur du fil précise : « envoyez-moi un message direct si vous avez des contacts ».
  </p>
  <p>
    <strong>Prochaine étape :</strong> répondez en donnant le nom de deux contacts, ou indiquez que vous pouvez être
    vous-même l’exemple si cela est plus utile.
  </p>

Un bon résultat établit clairement ces distinctions : une idée n’est pas un contact potentiel, une demande toujours d’actualité n’est pas un simple message d’information, et une demande à laquelle vous avez déjà répondu ne doit pas rester dans la liste.

Si vous obtenez trop de résultats non pertinents ou pas assez d’éléments exploitables, ajustez le prompt et, si nécessaire, indiquez les canaux Slack auxquels ChatGPT doit accorder une attention particulière.

## Rédigez le message de suivi

Une fois la liste au point, poursuivez le travail dans la même discussion. Demandez à ChatGPT de préparer une réponse ou un passage de relais à partir des éléments probants déjà recueillis :
