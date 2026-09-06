<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/feedback-synthesis -->

## Avant de commencer

Les retours sur le produit peuvent se trouver dans Slack, des exports de questionnaires, des outils de suivi des tickets, des dossiers du support ou des notes de recherche. Fournissez à ChatGPT Work les sources, le périmètre produit et la période à examiner. Il peut regrouper les problèmes récurrents dans une feuille de calcul ou un document que l’équipe pourra examiner avant de décider des prochaines étapes.

Lancez ce workflow dans Work, sur le Web ou dans l’application de bureau, avec les applications connectées et les fichiers cloud. Si la source se trouve sur votre ordinateur, commencez par joindre un export local ou utilisez l’application de bureau.

## Résultats attendus

Voici un exemple qui utilise un export de questionnaire, des dossiers du support, un fil de retours et des notes de recherche pour une file de révision des demandes. La première analyse regroupe les problèmes récurrents ; la demande complémentaire décompose ensuite un thème général en deux décisions plus précises.

<div data-use-case-export-only>

La première analyse a fait ressortir trois problèmes récurrents à partir d’un questionnaire, de dossiers du support, d’un fil de retours et de notes de recherche :

- **Les conflits ne sont pas visibles dans la file :** huit mentions réparties entre quatre sources. Affichez le statut de conflit dans la liste et distinguez `Ready` de `Needs attention`.
- **L’approbation groupée peut inclure des demandes bloquées :** quatre mentions réparties entre quatre sources. Excluez par défaut les demandes bloquées ou affichez un avertissement avant l’approbation.
- **Les personnes chargées de la révision perdent le fil et ne peuvent pas isoler les éléments à traiter :** dix mentions réparties entre quatre sources. Conservez la recherche et les filtres, et proposez une vue `Needs attention`.

Après une demande complémentaire visant à scinder le dernier thème, le tableau distingue **la réinitialisation de la recherche et des filtres au retour** de **la difficulté à isoler les éléments bloqués et non examinés**. Pour chaque thème, le tableau conserve les utilisateurs concernés, les ID des éléments probants, le niveau de confiance, les implications pour le design, les questions ouvertes et les actions de suivi. Ces chiffres indiquent le nombre de mentions récurrentes dans un petit échantillon, et non des taux d’incidence à l’échelle du produit.

</div>

## Fonctionnement

1. Indiquez à Work les sources des retours, le périmètre produit et la période à examiner.
2. Demandez-lui de regrouper les retours récurrents en thèmes et de conserver, pour chaque thème, les liens ou ID qui l’étayent.
3. Créez un fichier Google Sheets ou Google Docs indiquant les utilisateurs concernés, le niveau de confiance, les questions ouvertes et la décision à prendre ou la suite à donner.
4. Examinez le résumé avant de transformer un thème en message Slack ou en brouillon de ticket.

Utilisez le prompt de départ de cette page pour la première analyse, puis affinez tout thème trop général, insuffisamment étayé ou qui mélange des problèmes distincts.

## Préparez le brouillon suivant à partir d’un thème examiné

Une fois le résumé créé, demandez à Work de scinder un thème général, d’ajouter les éléments probants manquants, de rédiger un message Slack ou de transformer un thème examiné en brouillon de ticket. Précisez le public visé et la décision à prendre pour clarifier l’étape suivante.

## Maintenez à jour un canal de retours

Pour un canal Slack ou une file de tickets qui continue de recevoir de nouveaux signalements, demandez à Work de [le vérifier à intervalles réguliers](/fr-FR/codex/automations#schedule-work-from-a-task). Conservez les mêmes règles de révision pour éviter que de nouveaux retours ne donnent lieu, sans approbation, à un message, un ticket ou une attribution.
