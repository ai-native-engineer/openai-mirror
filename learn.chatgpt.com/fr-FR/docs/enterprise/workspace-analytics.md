<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/workspace-analytics -->

Utilisez les analyses de l’espace de travail ChatGPT pour suivre l’adoption dans l’ensemble de l’espace de travail. Utilisez les analyses Codex
pour obtenir des rapports centrés sur Codex. Utilisez Analytics API pour accéder par programmation
à des données agrégées et l’API de conformité pour obtenir des enregistrements pouvant être audités.

Ces solutions de reporting n’accordent pas l’accès au produit et ne définissent pas la politique d’exécution. Consultez
[Rôles et autorisations de l’espace de travail](/fr-FR/codex/enterprise/roles-and-workspace-permissions)
pour connaître les limites en matière d’administration.

## Choisissez une solution de reporting

| Solution                     | Utilisation                                                    | Référence faisant foi                                                                                                         |
| --------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Analyses de l’espace de travail ChatGPT | Rapports interactifs sur l’adoption et l’engagement dans l’ensemble de l’espace de travail | [Guide du centre d’aide sur les analyses de l’espace de travail](https://help.openai.com/en/articles/10875114)                               |
| Analyses Codex             | Rapports interactifs centrés sur l’adoption et l’activité de Codex  | Le [tableau de bord des analyses Codex](https://admin.openai.com/analytics/codex) accessible après authentification                                |
| Analytics API               | Production par programmation de rapports agrégés sur Codex                      | La [documentation de référence de Codex Analytics API](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics) |
| API de conformité              | Enregistrements d’audit, de sécurité, juridiques et d’enquête             | La [documentation de référence d’Admin API](https://chatgpt.com/public/admin/api-reference)                                              |

## Consultez les analyses de l’espace de travail ChatGPT

Les analyses de l’espace de travail ChatGPT offrent une vue interactive de l’adoption et de
l’engagement pour l’ensemble des fonctionnalités prises en charge dans l’espace de travail. La disponibilité, les rôles, les sections du tableau de bord,
la fraîcheur des données, les modalités de protection de la vie privée et les formats d’exportation peuvent évoluer. Consultez
[Analyses de l’espace de travail pour ChatGPT Enterprise et Edu](https://help.openai.com/en/articles/10875114)
pour connaître le périmètre couvert et les procédures à jour.

Traitez les rapports téléchargés comme des données identifiables de l’organisation.
Appliquez la politique de l’organisation en matière d’accès, de stockage et de conservation plutôt que de
supposer qu’un export présente les mêmes caractéristiques de confidentialité qu’un tableau de bord
présentant des données agrégées.

## Consultez les analyses Codex

Accessible après authentification, le [tableau de bord des analyses Codex](https://admin.openai.com/analytics/codex)
est consacré aux rapports sur Codex. Utilisez-le pour explorer les données de manière interactive, pas comme une garantie de stabilité
du schéma. Les catégories, les champs, les filtres et les formats d’exportation du tableau de bord peuvent
évoluer indépendamment de cette page.

Pour automatiser la production de rapports, utilisez [Analytics API](/fr-FR/codex/enterprise/analytics-api)
et suivez sa documentation de référence. Pour obtenir des enregistrements pouvant être audités, utilisez
l’[API de conformité](/fr-FR/codex/enterprise/compliance-api).

## Interprétez les données de reporting

Gardez à l’esprit les distinctions suivantes :

- Les analyses de l’espace de travail ChatGPT et les analyses Codex couvrent des périmètres fonctionnels
différents.
- Les analyses agrégées et les enregistrements d’audit répondent à des objectifs différents et relèvent de
contrats distincts.
- Les analyses décrivent l’activité ; elles n’accordent aucun accès et ne modifient pas les autorisations
d’exécution.
- Les [limites d’utilisation et les contrôles des dépenses de ChatGPT](/fr-FR/codex/enterprise/usage-limits) définissent
  un cadre distinct pour l’espace de travail, qui dépend de l’offre.
