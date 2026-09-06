<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/plugin/export-findings -->

Utilisez une analyse Codex Security terminée pour l’un de ces deux usages :

- **L’exportation** crée un fichier portable au format JSON, CSV ou SARIF.
- **Le suivi des résultats** permet de préparer les résultats sélectionnés sous forme d’issues
  Linear, GitHub ou Jira, ou d’un unique GitHub Security Advisory privé à l’état de brouillon. Codex recherche les
  doublons et attend votre approbation avant toute écriture.

Aucun de ces workflows ne modifie le paquet scellé de l’analyse.

  Les liens vers les artefacts et les formats d’exportation disponibles dépendent de l’interface Codex utilisée et de la
  version du plugin installée. Consultez le [journal des
  modifications du plugin](/fr-FR/codex/security/plugin/changelog) avant d’utiliser un format dans une
  automatisation.

## Exportation d’un artefact portable

Dans l’application de bureau, ouvrez une analyse terminée via **Sécurité** \> **Analyses**. Utilisez les liens
disponibles vers les artefacts pour consulter `report.md`, `findings.json`,
`scan-manifest.json`, `coverage.json` ou un rapport SARIF, s’il est présent.

Pour créer un autre format pris en charge, demandez à Codex d’exporter les résultats de
l’analyse terminée sans modifier le paquet scellé de celle-ci :

```text
Export the findings from [completed scan directory] as [JSON, CSV, or SARIF]. Do not modify the sealed scan bundle or upload its contents.

Choisissez le format adapté à votre destination :

| Format | Utilisation                                                        |
| ------ | ----------------------------------------------------------------- |
| JSON   | Conservez les résultats structurés scellés pour les outils et les scripts.    |
| CSV    | Examinez les résultats et l’état actuel du triage local dans une feuille de calcul.  |
| SARIF  | Envoyez les résultats aux outils qui prennent en charge le format d’échange SARIF. |

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Dans une analyse terminée, ouvrez l’artefact de couverture, l’artefact des résultats, le manifeste d’analyse, le rapport Markdown ou l’artefact
SARIF.
  </figcaption>
</figure>

Sélectionnez **Rapport Markdown** pour ouvrir `report.md` dans l’éditeur externe
configuré sur votre système. L’éditeur dépend des paramètres de votre système ; l’exemple ci-dessous montre le
contenu du rapport généré.

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    Examinez le périmètre de l’analyse, le modèle de menace, les résultats validés et les liens vers les rapports
détaillés dans le rapport Markdown généré.
  </figcaption>
</figure>

Utilisez le chemin d’accès à l’artefact renvoyé. Si un autre outil a besoin du contexte
complet de l’analyse, conservez ensemble les fichiers d’origine `scan-manifest.json`, `findings.json` et
`coverage.json`. L’exportation ne transmet pas les résultats à un service
d’analyse de code.

## Suivi des résultats sélectionnés

Exécutez `$codex-security:track-findings` avec un résultat validé ou un
lot explicitement sélectionné de 25 résultats au maximum provenant de la même analyse scellée. Chaque
exécution utilise un seul fournisseur et une seule destination. Un GitHub Security Advisory privé à l’état de brouillon ne peut contenir
qu’un seul résultat.

Pour préparer une issue Linear, envoyez :

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for the Linear team [team] and project [project, if
any]. Check for duplicates and show me the exact issue title, body, metadata,
and destination. Do not create or update anything until I approve that payload.

Pour préparer une issue GitHub, envoyez :

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for GitHub repository [owner/repository]. Check open
and closed issues for duplicates and show me the exact issue title, body,
metadata, repository visibility, and authenticated transport. Do not create or
update anything until I approve that payload.

Pour préparer une issue Jira, envoyez :

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for Jira project [project key] as [issue type].
Check for duplicates and show me the exact issue summary, description,
metadata, and destination. Do not create or update anything until I approve
that payload.

Le suivi dans Jira nécessite le plugin Atlassian Rovo dans Codex. La réutilisation d’une issue
nécessite un accès en lecture ; sa création ou sa mise à jour nécessite un accès en lecture et en écriture.

Pour préparer un GitHub Security Advisory privé à l’état de brouillon, envoyez :

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] as a private draft GitHub Security Advisory in
[owner/repository]. Verify the sealed source revision, repository, affected
paths, package metadata, and duplicate state. Show me the exact advisory
payload, authenticated GitHub CLI identity, and disclosure warnings. Do not
create anything until I approve that payload.

  Pour créer un avis de sécurité à l’état de brouillon, il faut un résultat provenant d’une analyse `git_revision` scellée, le
  dépôt source canonique public vérifié et des droits d’administrateur. Le
  workflow ne permet pas de traiter les avis par lot, de les mettre à jour, de les publier ni de les clôturer. Utilisez une
  destination approuvée pour les issues privées lorsque la source ne remplit pas ces conditions.

## Vérification de l’action d’écriture proposée

1. Vérifiez que l’identifiant et l’empreinte du résultat proviennent bien de l’analyse scellée concernée.
2. Vérifiez le fournisseur, l’équipe Linear exacte, le dépôt GitHub, le projet Jira ou
le dépôt de l’avis, ainsi que la visibilité actuelle de la destination.
3. Vérifiez le résultat du contrôle des doublons : `create`, `reuse`, `update` ou `blocked`.
4. Lisez l’intégralité du titre, du corps, des emplacements dans le code source et des métadonnées du fournisseur
figurant dans la proposition. Supprimez les détails d’exploitation ou les preuves internes que la destination
ne doit pas exposer.
5. N’approuvez que cette charge utile exacte. Toute modification de la destination, de sa visibilité, de l’ensemble des résultats
ou du corps nécessite un nouvel aperçu.

Les résultats sensibles doivent être envoyés vers une destination privée. La création d’une issue dans un
dépôt GitHub interne ou public nécessite un avertissement explicite concernant sa visibilité
et l’approbation de l’intégralité du contenu. Considérez que la description d’un avis à l’état de brouillon
finira par être publique et supprimez les identifiants d’accès, les preuves confidentielles et les détails
d’exploitation superflus avant l’approbation.

Examinez et approuvez les actions externes dans la conversation Codex. L’approbation
ne crée pas d’écran distinct pour les issues ou les avis dans l’espace de travail Sécurité.

## Vérification de l’élément suivi

Après votre approbation de l’action d’écriture proposée, Codex vérifie de nouveau la source scellée,
la destination, les droits d’accès et l’état des doublons. Pour un lot, il traite les résultats
un par un et s’arrête au premier résultat incertain. La création, la mise à jour ou la
réutilisation n’est considérée comme terminée qu’après que Codex a relu l’issue correspondante et vérifié ses
identifiants d’association et son contenu.

Conservez l’URL canonique renvoyée de l’issue ou de l’avis avec votre dossier de triage.
Passez à [Corriger et vérifier un résultat](/fr-FR/codex/security/plugin/fix-findings)
lorsque son responsable accepte de le corriger.
