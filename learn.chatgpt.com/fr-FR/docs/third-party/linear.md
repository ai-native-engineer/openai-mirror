<!-- source: https://learn.chatgpt.com/fr-FR/docs/third-party/linear -->

Utilisez Codex dans Linear pour déléguer des tâches à partir de tickets. Attribuez un ticket à Codex ou mentionnez `@Codex` dans un commentaire : Codex crée alors une discussion dans le cloud et vous informe de sa progression et de ses résultats.

Codex dans Linear est disponible avec les offres payantes (consultez [Tarifs](/fr-FR/codex/pricing)).

Si vous disposez d’une offre Entreprise, demandez à l’administrateur de votre espace de travail ChatGPT d’activer les discussions Codex dans le cloud dans [les paramètres de l’espace de travail](https://chatgpt.com/admin/settings), ainsi que **Codex pour Linear** dans [les paramètres des connecteurs](https://chatgpt.com/admin/ca).

## Configurer l’intégration Linear

1. Configurez [les discussions Codex dans le cloud](/fr-FR/codex/cloud) en connectant GitHub à [Codex](https://chatgpt.com/codex) et en créant un [environnement](/fr-FR/codex/environments/cloud-environment) pour le dépôt sur lequel vous souhaitez que Codex travaille.
2. Accédez aux [paramètres de Codex](https://chatgpt.com/codex/settings/connectors) et installez **Codex pour Linear** dans votre espace de travail.
3. Associez votre compte Linear en mentionnant `@Codex` dans un fil de commentaires d’un ticket Linear.

## Déléguer des tâches à Codex

Vous pouvez déléguer des tâches de deux façons :

### Attribuer un ticket à Codex

Après avoir installé l’intégration, vous pouvez attribuer des tickets à Codex comme vous le feriez pour vos collègues. Codex commence son travail et publie des mises à jour dans le ticket.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

### Mentionner `@Codex` dans les commentaires

Vous pouvez également mentionner `@Codex` dans des fils de commentaires pour déléguer des tâches ou poser des questions. Une fois que Codex a répondu, poursuivez l’échange dans le fil pour continuer la même discussion.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

Lorsque Codex commence à traiter un ticket, il [choisit un environnement et un dépôt](#how-codex-chooses-an-environment-and-repo) dans lesquels travailler.
Pour spécifier un dépôt précis, indiquez-le dans votre commentaire, par exemple : `@Codex fix this in openai/codex`.

Pour suivre la progression :

- Ouvrez **Activité** dans le ticket pour consulter les mises à jour sur la progression.
- Ouvrez le lien vers la discussion pour suivre son déroulement plus en détail.

Une fois son travail terminé, Codex publie un résumé et un lien vers la discussion terminée afin que vous puissiez créer une pull request.

### Comment Codex choisit un environnement et un dépôt

- Linear suggère un dépôt en fonction du contexte du ticket. Codex sélectionne l’environnement qui correspond le mieux à cette suggestion. Si la demande est ambiguë, il utilise l’environnement dont vous vous êtes servi le plus récemment.
- La discussion s’exécute sur la branche par défaut du premier dépôt répertorié dans le mappage des dépôts de cet environnement. Modifiez ce mappage dans Codex si vous souhaitez changer le dépôt par défaut ou ajouter d’autres dépôts.
- Si aucun environnement ou dépôt adapté n’est disponible, Codex répond dans Linear en expliquant comment corriger le problème avant de réessayer.

## Attribuer automatiquement des tickets à Codex

Vous pouvez attribuer automatiquement des tickets à Codex à l’aide de règles de triage :

1. Dans Linear, accédez aux **Paramètres**.
2. Sous **Vos équipes**, sélectionnez votre équipe.
3. Dans les paramètres du workflow, ouvrez **Triage** et activez-le.
4. Dans **Règles de triage**, créez une règle, puis choisissez **Déléguer** \> **Codex** (ainsi que toute autre propriété que vous souhaitez définir).

Linear attribue automatiquement à Codex les nouveaux tickets qui entrent en triage.
Lorsque vous utilisez des règles de triage, Codex lance les discussions avec le compte de la personne qui a créé le ticket.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

## Utilisation des données, confidentialité et sécurité

Lorsque vous mentionnez `@Codex` ou que vous lui attribuez un ticket, Codex reçoit le contenu de votre ticket afin de comprendre votre demande et de créer une discussion.
Le traitement des données respecte la [politique de confidentialité](https://openai.com/privacy) et les [conditions d’utilisation](https://openai.com/terms/) d’OpenAI, ainsi que les autres [politiques](https://openai.com/policies) applicables.
Pour en savoir plus sur la sécurité, consultez la [documentation de Codex sur la sécurité](/fr-FR/codex/agent-approvals-security).

Codex utilise de grands modèles de langage qui peuvent commettre des erreurs. Vérifiez toujours les réponses et les diffs.

## Conseils et dépannage

- **Connexions manquantes** : si Codex ne parvient pas à confirmer votre connexion à Linear, il répond dans le ticket en fournissant un lien permettant de connecter votre compte.
- **Choix inattendu de l’environnement** : répondez dans le fil en indiquant l’environnement souhaité (par exemple, `@Codex please run this in openai/codex`).
- **Partie du code mal ciblée** : ajoutez davantage de contexte au ticket ou donnez des instructions explicites dans votre commentaire mentionnant `@Codex`.
- **Aide supplémentaire** : consultez le [centre d’aide OpenAI](https://help.openai.com/).

<a id="connect-linear-for-local-tasks-mcp"></a>

## Connecter Linear pour travailler en local (MCP)

Si vous utilisez l’application de bureau ChatGPT, Codex CLI ou l’extension IDE et souhaitez que Codex accède localement aux tickets Linear, configurez le serveur MCP (Model Context Protocol) de Linear.

Pour en savoir plus, [consultez la documentation MCP de Linear](https://linear.app/integrations/codex-mcp).

Les étapes de configuration du serveur MCP sont identiques, que vous utilisiez l’extension IDE ou la CLI, puisque les deux partagent la même configuration.

### Utiliser la CLI (recommandé)

Si vous avez installé la CLI, exécutez :

```bash
codex mcp add linear --url https://mcp.linear.app/mcp

Cette commande vous invite à vous connecter avec votre compte Linear et à l’associer à Codex.

### Configurer manuellement

1. Ouvrez `~/.codex/config.toml` dans votre éditeur.
2. Ajoutez ce qui suit :

```toml
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"

3. Exécutez `codex mcp login linear` pour vous connecter.
