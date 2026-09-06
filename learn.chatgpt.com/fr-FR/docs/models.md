<!-- source: https://learn.chatgpt.com/fr-FR/docs/models -->

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Choisissez un modèle

Dans l’application de bureau ChatGPT, utilisez le sélecteur de modèle et d’effort de raisonnement situé sous la
zone de saisie pour choisir un modèle disponible et régler son effort de raisonnement.

Un effort de raisonnement plus élevé peut améliorer les résultats pour les tâches complexes, mais demande
plus de temps et consomme davantage de tokens. Commencez par l’effort par défaut et augmentez-le lorsque
la tâche nécessite une planification ou une analyse plus approfondie.

Le mode <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> ne se limite pas
à l’exécution par un seul agent. Il utilise des
[sous-agents](/codex/agent-configuration/subagents) pour accélérer les tâches complexes,
ce qui le rend utile pour les tâches de grande ampleur qui peuvent être réparties entre plusieurs sous-agents.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Choisissez un modèle

Ces recommandations s’appliquent à **ChatGPT Work** sur le Web. Utilisez le
sélecteur de modèle et d’effort de raisonnement situé sous la zone de saisie pour choisir un modèle disponible
et régler son effort de raisonnement.

Un effort de raisonnement plus élevé peut améliorer les résultats pour les tâches complexes, mais demande
plus de temps et consomme davantage de tokens. Commencez par l’effort par défaut et augmentez-le lorsque
la tâche nécessite une planification ou une analyse plus approfondie.

Le mode <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> ne se limite pas
à l’exécution par un seul agent. Il utilise des
[sous-agents](/codex/agent-configuration/subagents) pour accélérer les tâches complexes,
ce qui le rend utile pour les tâches de grande ampleur qui peuvent être réparties entre plusieurs sous-agents.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(22rem,25rem)] lg:items-start">
  <div class="min-w-0">

## Choisissez un modèle

Dans une session CLI interactive, utilisez `/model` pour changer de modèle ou ajuster
l’effort de raisonnement. Vous pouvez aussi choisir un modèle lorsque vous lancez Codex avec
`--model` ou son alias `-m` :

La même option fonctionne pour les exécutions non interactives. Par exemple :

Un effort de raisonnement plus élevé peut améliorer les résultats pour les tâches complexes, mais demande
plus de temps et consomme davantage de tokens. Commencez par le niveau d’effort par défaut et augmentez-le lorsque
la tâche nécessite une planification ou une analyse plus poussée.

Le mode <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> va au-delà
d’une exécution avec un seul agent. Il fait appel à des
[sous-agents](/codex/agent-configuration/subagents) pour accélérer les tâches complexes,
ce qui le rend utile pour les tâches de grande ampleur pouvant être réparties entre plusieurs sous-agents.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Choisissez un modèle

Utilisez le sélecteur de modèle sous la zone de saisie pour choisir un modèle disponible et
régler l’effort de raisonnement.

Un effort de raisonnement plus élevé peut améliorer les résultats pour les tâches complexes, mais demande
plus de temps et consomme davantage de tokens. Commencez par le niveau d’effort par défaut et augmentez-le lorsque
la tâche nécessite une planification ou une analyse plus poussée.

Le mode <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> va au-delà
d’une exécution avec un seul agent. Il fait appel à des
[sous-agents](/codex/agent-configuration/subagents) pour accélérer les tâches complexes,
ce qui le rend utile pour les tâches de grande ampleur pouvant être réparties entre plusieurs sous-agents.

  </div>
  
</div>

<a id="recommended-models"></a>
<a id="other-models"></a>
<a id="deprecated-codex-models"></a>
<a id="configure-your-default-local-model"></a>
<a id="choose-a-model-for-cloud-tasks"></a>
<a id="gpt-6-astra"></a>

## Modèles recommandés

<a id="app-compare-models"></a>

<div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
  

  

</div>

La disponibilité dépend du déploiement, de votre méthode de connexion et de votre client.
Consultez les [tarifs](/fr-FR/codex/pricing) pour connaître l’accès et l’utilisation inclus dans chaque offre, et la page
[Disponibilité des modèles dans l’espace de travail](/fr-FR/codex/enterprise/workspace-model-availability#gpt-6-astra-in-enterprise)
pour l’accès Entreprise.

  Commencez par le réglage Puissance proposé par défaut pour votre compte. Déplacez le curseur vers
**Plus intelligent** pour un raisonnement plus approfondi ou vers **Plus rapide** pour travailler plus vite et à moindre coût.
  Ouvrez **Avancé** pour choisir `gpt-5.6-luna` ou un modèle, un niveau de raisonnement
  ou une vitesse spécifiques.

Les illustrations du sélecteur montrent les commandes de GPT-5.6. Pour les comptes Pro, Business
(100 $) et Entreprise éligibles, le déploiement d’Astra remplace les options de Puissance
par Terra Léger, Sol Léger, Sol Médium, Astra Léger, Astra Médium et Astra
Très élevé. Les options peuvent varier selon l’offre et la phase du déploiement.

### Gestion expérimentale du contexte

Sur les clients Codex compatibles, les utilisateurs connectés avec ChatGPT Plus ou Pro peuvent activer
la gestion expérimentale du contexte. Astra conserve des notes d’une fenêtre de contexte
à l’autre et peut rechercher des messages et des résultats d’outils antérieurs de la même tâche.
Cette fonctionnalité expérimentale est désactivée par défaut et n’est pas disponible au lancement avec les offres Business ou Entreprise,
ni avec une connexion par clé API.

Pour l’activer, définissez `features.context_management.experimental_mode = true` dans votre fichier
`config.toml`, puis démarrez une nouvelle tâche. Consultez la [référence de configuration](/fr-FR/codex/config-file/config-reference)
pour en savoir plus sur ce paramètre et les [bases de la configuration](/fr-FR/codex/config-file/config-basic)
pour connaître l’emplacement du fichier. Les exigences de l’espace de travail restent applicables.

<a id="choosing-sol-terra-and-luna"></a>

## Choisissez entre Astra, Sol, Terra et Luna

Choisissez **Astra** lorsqu’une tâche exige les meilleures capacités au fil de plusieurs
étapes et avec différents outils. **Sol** offre des résultats approfondis et soignés, **Terra** convient au travail quotidien
et **Luna** aux tâches bien définies et répétables.

### Les points forts de chaque modèle

- **Astra, pour les tâches les plus difficiles à mener de bout en bout.** Choisissez Astra pour des workflows complets
  de programmation, d’utilisation d’applications et de recherche qui exigent un raisonnement et un discernement soutenus.
  Fournissez-lui les sources, les modèles de documents, les contraintes et les vérifications qui définissent un résultat
  utile. Astra pose des questions plus ciblées et intègre mieux vos
  indications tout en gardant à l’esprit l’objectif et les contraintes d’origine.
- **Sol, pour les tâches complexes et ouvertes.** Choisissez Sol pour les tâches ambiguës, difficiles ou
  à forte valeur ajoutée qui exigent davantage d’analyse, de discernement ou de finition, comme
  des modifications complexes du code, une recherche approfondie ou des documents soignés. Pour les tâches plus
  ciblées, définissez clairement le résultat attendu afin que le travail reste centré sur l’objectif.
- **Terra, le modèle polyvalent et pragmatique.** Choisissez Terra pour les tâches quotidiennes qui
  nécessitent de solides capacités de raisonnement et d’utilisation des outils, sans exiger toute la profondeur d’analyse de Sol. Terra
  est un bon point de départ pour les tâches que vous confiiez auparavant à GPT-5.5.
- **Luna, pour les tâches bien définies et répétables.** Choisissez Luna pour les tâches précises à traiter en grand volume
  lorsque vous savez ce qui constitue un bon résultat, par exemple l’extraction,
  la classification, la transformation et les résumés structurés.

### Choisissez un niveau de raisonnement

Utilisez le niveau de raisonnement le plus faible qui produit le résultat souhaité. Augmentez-le
pour les tâches qui nécessitent davantage de planification, d’analyse ou de vérification.

- Le niveau **Léger** dans l’application de bureau ChatGPT, ChatGPT Work sur le Web et l’extension IDE, ou **Faible** dans la
  CLI, convient aux tâches rapides et bien délimitées.
- Le niveau **Médium** concilie vitesse et profondeur pour les tâches qui nécessitent davantage de planification.
- Les niveaux **Élevé** et **Très élevé** conviennent aux tâches difficiles qui comportent plusieurs étapes, mobilisent plusieurs sources
  ou nécessitent des arbitrages.

Il n’existe pas de correspondance exacte entre les niveaux de raisonnement de GPT-5.5 et ceux de GPT-5.6. Essayez une
tâche familière à un niveau inférieur, puis ajustez-le en fonction du résultat.

### Quand utiliser Max ou Ultra

**Max** donne au modèle sélectionné davantage de temps pour raisonner sur une seule tâche. Utilisez-le
pour les problèmes les plus difficiles, lorsque la profondeur d’analyse compte davantage que la vitesse ou la consommation. Si
Max n’apparaît pas dans vos options, vous devrez l’activer dans les paramètres de l’application.

**Ultra** fait appel à des [sous-agents](/fr-FR/codex/agent-configuration/subagents) pour traiter
en parallèle différentes parties d’une tâche complexe. Choisissez ce mode lorsque vous pouvez diviser le
travail en parties cohérentes. La plupart des tâches ne nécessitent ni Max ni Ultra.

Si Ultra n’apparaît pas dans le curseur de sélection du modèle de l’application de bureau, accédez à
**Paramètres** \> **Configuration**, puis activez **Ultra dans le curseur de sélection du modèle**.

## Autres modèles

Lorsque vous vous connectez avec ChatGPT, Codex donne les meilleurs résultats avec les modèles recommandés ci-dessus.

  <strong>
    Les modèles GPT-5.4 et GPT-5.4 mini sont retirés de Codex le 31 août 2026.
  </strong>{" "}
  Si vous vous connectez avec ChatGPT, remplacez `gpt-5.4` par `gpt-5.6-terra` et
`gpt-5.4-mini` par `gpt-5.6-luna` dans les configurations enregistrées, les agents personnalisés et les
  tâches planifiées. L’API OpenAI et l’utilisation de Codex avec votre propre clé API
  ne sont pas concernées.

  <div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
    

    

    

  </div>

Vous pouvez aussi configurer Codex pour utiliser tout modèle et tout fournisseur compatibles avec l’[API Chat Completions](https://platform.openai.com/docs/api-reference/chat) ou l’[API Responses](https://platform.openai.com/docs/api-reference/responses), selon votre cas d’usage.

  La prise en charge de l’API Chat Completions est obsolète et sera supprimée dans
les prochaines versions de Codex.

## Modèles Codex obsolètes

Les modèles `gpt-5.4` et `gpt-5.4-mini` seront retirés de Codex pour les utilisateurs qui se connectent via ChatGPT
le 31 août 2026. Remplacez `gpt-5.4` par `gpt-5.6-terra` et
`gpt-5.4-mini` par `gpt-5.6-luna` dans les paramètres par défaut de l’espace de travail, les paramètres de modèle
enregistrés, les configurations gérées, les agents personnalisés et les tâches planifiées.

Les modèles `gpt-5.2` et `gpt-5.3-codex` sont déjà obsolètes dans Codex lorsque
vous vous connectez via ChatGPT. Mettez à jour les scripts, les fichiers de configuration et
les commandes `codex exec --model` qui font encore référence à ces modèles.

L’API OpenAI et Codex avec authentification par votre propre clé API ne sont pas concernés
par le retrait de GPT-5.4. Pour connaître les modèles actuellement disponibles via l’API, consultez la
[page des modèles de l’API](/api/docs/models).

## Configurez votre modèle local par défaut

L’application de bureau ChatGPT, Codex CLI et l’extension IDE utilisent le même
[fichier de configuration](/fr-FR/codex/config-file/config-basic) `config.toml`. Pour spécifier un modèle, ajoutez une entrée
`model` à votre fichier de configuration. Si vous ne spécifiez pas de modèle,
l’application de bureau ChatGPT, Codex CLI ou l’extension IDE utilise un modèle recommandé.

## Choisissez un modèle pour les discussions dans le cloud

Actuellement, vous ne pouvez pas changer le modèle par défaut des discussions dans Codex Cloud.
