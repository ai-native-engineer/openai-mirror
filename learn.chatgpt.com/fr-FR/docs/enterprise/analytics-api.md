<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/analytics-api -->

La Codex Analytics API fournit des métriques agrégées sur l’utilisation et l’activité de Codex pour
un espace de travail ChatGPT.

La [référence de la Codex Analytics API](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)
fait autorité sur les exigences d’accès en vigueur, les routes, les schémas de requête et de
réponse, les métriques, la sémantique temporelle et la pagination.

## Quand utiliser l’Analytics API

L’Analytics API convient lorsque vous devez :

- Automatiser la génération régulière de rapports sur Codex.
- Croiser les métriques agrégées de Codex avec les données internes de l’organisation.
- Créer une couche de reporting contrôlée pour les destinataires autorisés.
- Éviter de coupler une intégration à un tableau de bord interactif.

Il ne s’agit pas d’une interface d’accès aux journaux d’audit bruts. Utilisez
l’[API de conformité](/fr-FR/codex/enterprise/compliance-api) lorsque le workflow nécessite
des enregistrements d’activité pouvant faire l’objet d’un audit.

## Vérifiez les périmètres d’administration

Les résultats de l’Analytics API sont limités à un espace de travail ChatGPT, mais les requêtes
sont authentifiées à l’aide d’une clé API d’une organisation de la Plateforme. L’organisation à laquelle appartient la clé doit
correspondre à celle associée à l’espace de travail.

La référence de l’API fait autorité sur les modalités actuelles de provisionnement des clés, les portées requises,
les routes, les schémas, les champs, la sémantique temporelle et le fonctionnement de la pagination. Cette page
ne reproduit pas ce contrat.

## Documentation associée

- [Analyses de l’espace de travail](/fr-FR/codex/enterprise/workspace-analytics)
- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
- [Gouvernance](/fr-FR/codex/enterprise/governance)
- [API de conformité](/fr-FR/codex/enterprise/compliance-api)
