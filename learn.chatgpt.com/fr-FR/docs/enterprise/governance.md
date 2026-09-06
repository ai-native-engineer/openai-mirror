<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/governance -->

La gouvernance de l’activité de Codex couvre les analyses interactives, les rapports générés par programmation,
les contrôles associés à l’utilisation de ChatGPT et les enregistrements d’audit. Choisissez
l’interface adaptée à la question posée ; les données d’analyse et de conformité répondent
à des objectifs différents.

<a id="governance-and-observability"></a>
<a id="ways-to-track-codex-usage"></a>

| Si vous souhaitez                                          | Commencez par                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------- |
| Comprendre l’adoption à l’échelle de ChatGPT                      | [Analyses de l’espace de travail](/fr-FR/codex/enterprise/workspace-analytics)              |
| Examiner de manière interactive l’adoption et l’activité de Codex        | [Analyses Codex](#analytics-dashboard)                                   |
| Charger les rapports Codex agrégés dans un autre système     | [Analytics API](/fr-FR/codex/enterprise/analytics-api)                          |
| Exporter des enregistrements à des fins d’audit ou d’enquête               | [API de conformité](/fr-FR/codex/enterprise/compliance-api)                        |
| Examiner les contrôles des crédits de l’espace de travail ChatGPT qui dépendent de l’offre | [Limites d’utilisation et contrôles des dépenses de ChatGPT](/fr-FR/codex/enterprise/usage-limits) |

## Ouvrez les interfaces d’administration

- Ouvrez [Analyses de l’espace de travail](https://chatgpt.com/admin/usage) pour consulter les rapports interactifs
  de l’espace de travail. Le [guide des analyses de l’espace de travail](https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu)
  décrit les rôles et les vues actuels.
- Ouvrez la [référence de l’Analytics API de Codex](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)
  lorsque vous devez générer des rapports planifiés par programmation.
- Ouvrez la [référence de l’API d’administration](https://chatgpt.com/public/admin/api-reference)
  et le [guide de la plateforme de conformité](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)
  pour les intégrations d’audit et d’enquête.

Par exemple, utilisez les analyses de l’espace de travail pour vérifier rapidement l’adoption, l’Analytics API
pour charger les rapports Codex agrégés dans un système d’informatique décisionnelle,
et l’API de conformité pour envoyer des enregistrements auditables à un SIEM ou à un workflow
d’eDiscovery.

## Tableau de bord d’analyse

<a id="dashboard-views"></a>
<a id="data-export"></a>

ChatGPT fournit des analyses à l’échelle de l’espace de travail pour mesurer globalement l’adoption et l’engagement.
Les analyses Codex portent sur l’activité de Codex. Dans les deux cas, il s’agit d’interfaces de consultation interactive des rapports,
et non de journaux d’audit bruts.

Consultez [Analyses de l’espace de travail](/fr-FR/codex/enterprise/workspace-analytics) pour comparer les
deux expériences et trouver leurs sources actuelles, tenues à jour par leurs responsables. Vous pouvez aussi
ouvrir directement [Analyses de l’espace de travail](https://chatgpt.com/admin/usage). Ne
fondez pas un contrat de reporting pérenne sur les libellés du tableau de bord ni sur les champs des rapports
téléchargés ; ces éléments peuvent changer à mesure que le produit évolue.

## Contrôles associés à l’utilisation de ChatGPT

Les contrôles d’utilisation de l’espace de travail ChatGPT sont distincts des analyses et ne
configurent pas les droits d’accès aux fonctionnalités. Selon l’offre, les activités Codex éligibles
peuvent consommer des crédits de l’espace de travail ChatGPT. Lorsque les limites sont atteintes, l’accès aux
fonctionnalités éligibles peut être suspendu. Ces contrôles ne fixent pas de limite universelle pour Codex et ne régissent pas
la facturation de la Plateforme API.

Consultez [Limites d’utilisation et contrôles des dépenses de ChatGPT](/fr-FR/codex/enterprise/usage-limits)
pour connaître le périmètre stable de ces contrôles et accéder aux sources actuelles du centre d’aide.

## Analytics API

<a id="what-it-measures"></a>
<a id="endpoints"></a>
<a id="usage"></a>
<a id="code-review-activity"></a>
<a id="user-engagement-with-code-review"></a>
<a id="how-it-works"></a>
<a id="common-use-cases"></a>

Utilisez l’Analytics API pour obtenir par programmation des rapports Codex agrégés. Elle
convient pour alimenter des entrepôts de données et des systèmes d’informatique décisionnelle, ainsi que pour produire des rapports
internes qui ne doivent pas dépendre d’un tableau de bord interactif.

La documentation de référence de l’API fait autorité pour les conditions d’accès, les routes, les schémas,
les champs, les périodes couvertes par les rapports et la pagination. Consultez
[Analytics API](/fr-FR/codex/enterprise/analytics-api) pour connaître le périmètre conceptuel de l’intégration
et accéder au lien vers la référence canonique.

## API de conformité

<a id="what-it-measures-1"></a>
<a id="what-you-can-export"></a>
<a id="activity-logs"></a>
<a id="metadata-for-audit-and-investigation"></a>
<a id="common-use-cases-1"></a>
<a id="what-it-does-not-provide"></a>

Utilisez l’API de conformité pour les workflows liés à la sécurité, aux questions juridiques et à la gouvernance qui nécessitent
des enregistrements auditables. Il ne s’agit pas d’un tableau de bord d’adoption ou de productivité.

La documentation de référence de l’API fait autorité pour la couverture des événements, les schémas, les autorisations,
les filtres, la conservation et le comportement des requêtes. Consultez
[API de conformité](/fr-FR/codex/enterprise/compliance-api) pour connaître le périmètre conceptuel
de l’intégration et accéder au lien vers la référence canonique.

<a id="recommended-pattern"></a>

Pour planifier les étapes du déploiement et effectuer les vérifications dans ces différentes interfaces, utilisez le
[guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup).

## Documentation associée

- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
- [Analyses de l’espace de travail](/fr-FR/codex/enterprise/workspace-analytics)
- [Analytics API](/fr-FR/codex/enterprise/analytics-api)
- [API de conformité](/fr-FR/codex/enterprise/compliance-api)
