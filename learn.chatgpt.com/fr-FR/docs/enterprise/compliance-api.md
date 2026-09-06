<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/compliance-api -->

Utilisez l’API de conformité pour les workflows liés à la sécurité, aux questions juridiques, à la gouvernance et aux enquêtes
qui nécessitent des enregistrements auditables. Pour mesurer l’adoption et les tendances,
utilisez les données d’analyse, et non les enregistrements de conformité.

La [référence de l’API d’administration](https://chatgpt.com/public/admin/api-reference)
fait autorité pour les exigences d’accès actuelles, les événements couverts, les routes,
les schémas, les filtres, la conservation et le comportement des requêtes.

Pour une vue d’ensemble des interfaces de conformité disponibles et des modèles
d’intégration courants, consultez le [guide de la plateforme de conformité](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers).

## Quand utiliser l’API de conformité

L’API de conformité convient lorsque vous devez :

- Exporter les enregistrements pris en charge vers un système d’audit ou d’enquête.
- Appliquer les procédures de votre organisation en matière de conservation et de préservation à des fins juridiques.
- Corréler l’activité de Codex avec d’autres données de sécurité ou d’identité.
- Appuyer les enquêtes approuvées portant sur la sécurité, les questions juridiques ou la gouvernance.

Ce n’est pas un tableau de bord de productivité. Ne l’utilisez pas pour tirer des conclusions sur la qualité du code ou
les performances individuelles. Pour produire des rapports sur l’adoption, utilisez les [Analyses de l’espace de travail](/fr-FR/codex/enterprise/workspace-analytics)
ou l’[Analytics API](/fr-FR/codex/enterprise/analytics-api).

## Bien démarrer

1. Ouvrez la [référence de l’API d’administration](https://chatgpt.com/public/admin/api-reference) et
   vérifiez que votre rôle d’administrateur vous permet d’accéder aux ressources de conformité
   dont vous avez besoin.
2. Utilisez le flux de journaux de conformité, qui n’autorise que l’ajout d’entrées, pour assurer une collecte continue. Consultez la
référence de l’API pour connaître les ressources et les méthodes de récupération actuellement
prises en charge.
3. [Téléchargez les fichiers journaux](#download-logs) et testez leur ingestion, hors production, dans un système
   de gestion des informations et des événements de sécurité (SIEM) ou un lac de données.
4. Planifiez une collecte continue et appliquez aux enregistrements exportés les contrôles d’accès,
de conservation et de préservation à des fins juridiques de votre organisation. Ne partez pas du principe que la
durée de conservation à la source remplace la politique de conservation de votre organisation.

Par exemple, une équipe de sécurité peut transmettre en continu des événements de conformité immuables à son
SIEM à des fins d’enquête, ou les acheminer vers un workflow approuvé de recherche de preuves
électroniques. Consultez la référence de l’API pour connaître les routes et les schémas
actuels, plutôt que de copier un contrat de point de terminaison à partir de ce guide.

### Téléchargez les journaux

Téléchargez le [script Bash](/downloads/compliance-api/download_compliance_files.sh)
ou le [script PowerShell](/downloads/compliance-api/download_compliance_files.ps1).
Tous deux répertorient et téléchargent tous les fichiers journaux disponibles après un horodatage donné, parcourent
les pages de résultats et écrivent des données au format JSONL sur la sortie standard. Les erreurs sont envoyées sur la sortie d’erreur standard.

Attribuez à `COMPLIANCE_API_KEY` la valeur de votre clé de l’API de conformité Entreprise. Remplacez
`<workspace_or_org_id>` par l’identifiant de votre espace de travail ChatGPT ou de votre organisation
sur la Plateforme API, et `<after>` par un horodatage ISO 8601 incluant un fuseau
horaire. Cet exemple récupère les fichiers `AUTH_LOG` par lots de 100.

Sur macOS ou Linux, installez Bash, `curl` et `jq`, puis exécutez :

```bash
bash ./download_compliance_files.sh "<workspace_or_org_id>" AUTH_LOG 100 "<after>" > output.jsonl

Le script Windows est compatible avec PowerShell 5.1 ou une version ultérieure. Examinez le fichier téléchargé.
Si Windows le bloque et que la stratégie d’exécution de votre organisation l’autorise, exécutez
`Unblock-File -Path .\download_compliance_files.ps1`. Cet exemple utilise
PowerShell 7 pour enregistrer les données en UTF-8 sans marque d’ordre des octets :

```powershell
.\download_compliance_files.ps1 "<workspace_or_org_id>" AUTH_LOG 100 "<after>" |
  Set-Content -Encoding utf8NoBOM output.jsonl

## Vérifiez les périmètres d’administration

Le périmètre de conformité suit celui de l’espace de travail ChatGPT et des produits répertoriés
dans la référence actuelle de l’API. Les données de l’organisation sur la Plateforme API sont régies
par les contrôles propres à cette plateforme en matière de données d’API et d’administration.

La référence de l’API fait autorité pour les routes actuelles, les événements couverts, les schémas,
les filtres, les modalités de conservation, les permissions requises et le fonctionnement des requêtes.
Cette page ne reproduit pas ce contrat.

## Documentation connexe

- [Analyses de l’espace de travail](/fr-FR/codex/enterprise/workspace-analytics)
- [Guide de déploiement pour les administrateurs](/fr-FR/codex/enterprise/admin-setup)
- [Gouvernance](/fr-FR/codex/enterprise/governance)
- [Analytics API](/fr-FR/codex/enterprise/analytics-api)
