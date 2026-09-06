<!-- source: https://learn.chatgpt.com/fr-FR/docs/third-party/slack -->

Utilisez Codex dans Slack pour lancer des tâches de développement depuis des canaux et des fils de discussion. Mentionnez `@Codex` et ajoutez un prompt : Codex crée alors une discussion dans le cloud et répond avec les résultats.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>

<br />

## Configurez l’application Slack

1. Configurez les [discussions Codex dans le cloud](/fr-FR/codex/cloud). Vous devez disposer d’un abonnement Plus, Pro, Business, Entreprise ou Edu (voir les [tarifs de ChatGPT](https://chatgpt.com/pricing)), d’un compte GitHub connecté et d’au moins un [environnement](/fr-FR/codex/environments/cloud-environment).
2. Accédez aux [paramètres de Codex](https://chatgpt.com/codex/settings/connectors) et installez l’application Slack dans votre espace de travail. Selon les règles de votre espace de travail Slack, un administrateur devra peut-être approuver l’installation.
3. Ajoutez `@Codex` à un canal. Si ce n’est pas encore fait, Slack vous invite à l’ajouter lorsque vous le mentionnez.

<a id="start-a-task"></a>

## Démarrez une discussion

1. Dans un canal ou un fil de discussion, mentionnez `@Codex` et ajoutez votre prompt. Codex peut s’appuyer sur les messages précédents du fil, ce qui vous évite souvent de rappeler le contexte.
2. (Facultatif) Précisez un environnement ou un dépôt dans votre prompt, par exemple : `@Codex fix the above in openai/codex`.
3. Attendez que Codex réagisse (👀) et réponde avec un lien vers la discussion. Une fois la tâche terminée, Codex publie le résultat et, selon vos paramètres, une réponse dans le fil de discussion.

### Comment Codex choisit un environnement et un dépôt

- Codex examine les environnements auxquels vous avez accès et choisit celui qui correspond le mieux à votre demande. Si votre demande est ambiguë, il retient le dernier environnement que vous avez utilisé.
- La discussion s’exécute sur la branche par défaut du premier dépôt répertorié dans le mappage des dépôts de cet environnement. Mettez à jour ce mappage dans Codex si vous avez besoin d’un autre dépôt par défaut ou de dépôts supplémentaires.
- Si aucun environnement ou dépôt adapté n’est disponible, Codex répond dans Slack en vous indiquant comment résoudre le problème avant de réessayer.

### Contrôles des données pour l’offre Entreprise

Par défaut, Codex publie dans le fil de discussion une réponse susceptible de contenir des informations provenant de son environnement d’exécution.
Pour éviter cela, un administrateur de l’offre Entreprise peut décocher **Autoriser l’application Slack de Codex à publier des réponses à la fin d’une tâche** dans les [paramètres de l’espace de travail ChatGPT](https://chatgpt.com/admin/settings). Lorsqu’un administrateur désactive les réponses, Codex répond uniquement avec un lien vers la discussion.

### Utilisation des données, confidentialité et sécurité

Lorsque vous mentionnez `@Codex`, Codex reçoit votre message et l’historique du fil de discussion afin de comprendre votre demande et de créer une discussion.
Le traitement des données respecte la [politique de confidentialité](https://openai.com/privacy) d’OpenAI, ainsi que ses [conditions d’utilisation](https://openai.com/terms/) et ses autres [politiques](https://openai.com/policies) applicables.
Pour en savoir plus sur la sécurité, consultez la [documentation sur la sécurité](/fr-FR/codex/agent-approvals-security) de Codex.

Codex utilise de grands modèles de langage qui peuvent se tromper. Vérifiez toujours les réponses et les diffs.

### Conseils et dépannage

- **Connexions manquantes** : si Codex ne parvient pas à confirmer votre connexion à Slack ou à GitHub, il répond avec un lien pour vous reconnecter.
- **Choix inattendu de l’environnement** : répondez dans le fil de discussion en indiquant l’environnement souhaité (par exemple, `Please run this in openai/openai (applied)`), puis mentionnez à nouveau `@Codex`.
- **Fils de discussion longs ou complexes** : résumez les informations essentielles dans votre dernier message afin que Codex ne manque aucun élément de contexte mentionné plus tôt dans le fil.
- **Publication dans l’espace de travail** : certains espaces de travail Entreprise restreignent la publication des réponses finales. Dans ce cas, ouvrez le lien vers la discussion pour suivre l’avancement et consulter les résultats.
- **Aide supplémentaire** : consultez le [centre d’aide OpenAI](https://help.openai.com/).
