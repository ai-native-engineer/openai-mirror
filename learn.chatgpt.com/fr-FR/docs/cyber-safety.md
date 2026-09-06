<!-- source: https://learn.chatgpt.com/fr-FR/docs/cyber-safety -->

OpenAI Daybreak aide les utilisateurs dont l’accès a été approuvé à mener des activités autorisées de cybersécurité défensive. Daybreak Blue donne accès à des modèles phares, avec moins de refus pour les workflows défensifs autorisés. Daybreak Red donne accès, sous réserve d’une approbation distincte, à des modèles spécialisés en cybersécurité pour des recherches en sécurité plus avancées.

Utilisez votre modèle approuvé dans un environnement contrôlé, avec des limites claires pour les systèmes et actions autorisés, des autorisations fondées sur le principe du moindre privilège et une révision automatique avant l’exécution d’actions sensibles. N’utilisez le modèle qu’avec l’identité approuvée, dans l’espace de travail approuvé ou dans l’organisation API et le projet approuvés, et via l’interface produit approuvée.

## Choisissez le modèle adapté

Pour la plupart des activités défensives autorisées, commencez par **GPT-Daybreak-Blue** . Ce modèle donne accès à des capacités avancées, avec moins de refus pour les workflows de sécurité défensive, notamment :

- Découverte et triage des vulnérabilités.
- Revue de code axée sur la sécurité et modélisation des menaces.
- Ingénierie de la détection et réponse aux incidents.
- Analyse de logiciels malveillants dans un environnement contrôlé.
- Remédiation et validation des correctifs.

**GPT-Daybreak-Red** est un modèle spécialisé en cybersécurité destiné aux workflows qui font l’objet d’une approbation distincte et d’une autorisation explicite, comme la reproduction contrôlée de vulnérabilités, la validation de preuves de concept ou d’exploits, les tests d’intrusion, le red teaming et l’analyse de systèmes complexes. Ce n’est pas le choix par défaut pour les tâches courantes de sécurité. L’accès n’est pas accordé automatiquement et n’est pas disponible dans toutes les interfaces.

Sans autorisation claire, ces workflows avancés peuvent s’apparenter à des activités malveillantes. N’utilisez le modèle et l’interface approuvés que sur les systèmes qui vous appartiennent ou que vous avez explicitement l’autorisation d’évaluer, et maintenez une supervision humaine adaptée.

Par exemple :

- **GPT-Daybreak-Blue :** Examinez le dépôt approuvé du laboratoire pour repérer les faiblesses d’authentification, classez les constats en fonction des preuves disponibles et de leur impact, puis proposez des correctifs sans accéder à des systèmes externes.
- **GPT-Daybreak-Red :** Dans le laboratoire approuvé et pendant la fenêtre de test autorisée, reproduisez la faille d’authentification documentée, validez une preuve de concept minimale et arrêtez-vous avant tout accès à des données d’authentification, toute mise en place d’un mécanisme de persistance ou toute modification en production.

## Trusted Access for Cyber

Demandez **l’accès à Daybreak** par l’intermédiaire de [Trusted Access for Cyber](https://help.openai.com/en/articles/20001258-trusted-access-for-cyber). L’accès est soumis à une approbation et à un provisionnement spécifiques à votre identité ou à votre service, à votre espace de travail ChatGPT ou à votre organisation API et à votre projet, à l’offre et au modèle autorisés, ainsi qu’à l’interface produit autorisée.

- Les particuliers peuvent demander l’accès au moyen du [formulaire de demande Trusted Access pour les particuliers](https://chatgpt.com/cyber).
- Les organisations peuvent soumettre le [formulaire de demande Trusted Access pour les entreprises](https://openai.com/form/enterprise-trusted-access-for-cyber/) et coordonner la démarche avec leur représentant OpenAI.

Déposer une demande ou mener à bien la vérification d’identité ne garantit pas l’approbation.

  Déposer une demande, faire vérifier votre identité ou obtenir l’approbation pour Daybreak Blue
ne donne pas accès à Daybreak Red ni à GPT-Daybreak-Red. L’offre spécialisée
nécessite une approbation et un provisionnement distincts.

Pour l’accès en entreprise, utilisez l’espace de travail, l’organisation API ou le projet approuvés uniquement pour les activités internes autorisées de votre organisation. N’étendez pas cet accès aux utilisateurs externes, aux clients tiers, aux services proposés à l’extérieur de l’organisation, aux fonctionnalités de produits en aval ni aux systèmes hors du périmètre des activités approuvées. Si vous avez un doute sur l’identité, l’espace de travail, l’organisation API, le projet, le modèle ou l’interface approuvés, arrêtez-vous et demandez confirmation à votre représentant OpenAI.

Trusted Access ne permet pas automatiquement de bénéficier de la [politique de non-conservation des données](/api/docs/guides/your-data#data-retention-controls-for-abuse-monitoring). Avant de commencer, vérifiez quels contrôles de conservation des données ont fait l’objet d’une approbation distincte pour l’organisation API concernée et le point de terminaison applicable.

## Faux positifs

Une activité légitime de cybersécurité, ou une activité sans rapport avec celle-ci, peut tout de même déclencher un mécanisme de protection. Si un tel mécanisme bloque, réachemine ou limite une requête, examinez le message disponible côté client et les journaux de requêtes. Consultez [Problèmes courants et dépannage](https://help.openai.com/en/articles/20001259) pour connaître les informations à recueillir et la marche à suivre. Signalez les faux positifs présumés de Codex via `/feedback`, lorsque cette option est disponible. Pour les restrictions d’accès à l’API et les recours, suivez les [consignes relatives aux contrôles de cybersécurité de l’API](/api/docs/guides/safety-checks/cybersecurity#appeals).

Tous les utilisateurs restent soumis aux [politiques d’utilisation](https://openai.com/policies/usage-policies/) et aux [conditions d’utilisation](https://openai.com/policies/row-terms-of-use/).

## Configurez votre workflow de sécurité

Trusted Access encadre les accès approuvés aux modèles, mais ne configure pas votre environnement, ne fait pas respecter les limites définies pour les systèmes et actions autorisés et n’examine pas les actions proposées.

- [Utilisez la configuration recommandée](/fr-FR/codex/cyber-safety/recommended-configuration) pour isoler l’environnement, appliquer le principe du moindre privilège aux autorisations, définir clairement les limites et mettre en place des garde-fous pour les actions sensibles.
