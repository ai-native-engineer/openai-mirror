<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/plugin/triage-backlog -->

Utilisez `$codex-security:triage-finding` pour examiner les constats de sécurité existants
au regard du dépôt actuel. Ce workflow effectue une analyse statique
en lecture seule : Codex considère chaque constat comme une allégation non prouvée et examine les éléments de preuve du dépôt
sans exécuter le code.

Exécutez ce workflow depuis un projet Codex associé au dépôt que vous souhaitez
évaluer. Codex doit pouvoir lire le code source du dépôt. Les connecteurs Jira et Linear
peuvent fournir les données des constats, tandis que les constats GitHub nécessitent un accès
authentifié à l’API REST GitHub. Aucun de ces moyens ne remplace l’accès au code source.

En interne, Codex part du code cité ou des informations de version indiquées. Il
retrace la source supposément contrôlée par l’attaquant, les mesures de sécurité pertinentes,
le puits dangereux et le chemin accessible. Il vérifie aussi la surface du produit et la frontière
de confiance, recherche les éléments de preuve contradictoires et consigne les lacunes dans les preuves. Codex renvoie ensuite
un verdict pour chaque constat et classe les constats qui nécessitent une intervention ou un examen
approfondi.

Ce workflow diffère de `$codex-security:validation`, qui peut compiler ou exécuter du code,
créer un test ciblé ou une preuve de concept, ou interagir avec une interface réelle pour
reproduire ou réfuter un constat. Utilisez le triage pour classer et hiérarchiser un
backlog existant. Utilisez la validation lorsque les éléments observés à l’exécution pourraient lever l’incertitude sur
un constat que les éléments statiques laissent incertain.

  Le triage du backlog part de constats existants. Pour rechercher de nouvelles
  vulnérabilités dans le dépôt, [exécutez une analyse de sécurité](/fr-FR/codex/security/plugin/scans). Le triage
  ne modifie pas le dépôt et n’applique aucun correctif.

## Choisissez les constats à trier

Vous pouvez fournir un constat seul ou un ensemble issu des sources suivantes :

| Source                   | Éléments à fournir                                                                                                                                                                                                                                                                                                                                                                                                                                        | Prérequis                                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Constats fournis par copier-coller ou en local | Des résultats SARIF, une CVE ou une GHSA, un avis de sécurité, un ticket issu d’un scanner, un rapport de bug bounty, un artefact correspondant à un constat Codex Security ou une allégation de vulnérabilité en langage naturel.                                                                                                                                                                                                                                                                                          | Aucun connecteur requis.                                                                                                                                                                           |
| Jira ou Linear           | Les URL ou identifiants exacts de tickets de sécurité ou de vulnérabilité, une requête JQL Jira, ou une équipe, un projet ou une expression de recherche Linear. Codex récupère le contenu des tickets sélectionnés avant le triage.                                                                                                                                                                                                                                                                            | [Jira via Atlassian Rovo](codex://plugins/plugin_connector_692de805e3ec8191834719067174a384) ou [Linear](codex://plugins/plugin_asdk_app_69a089a326dc8191b32a3f2553f5be2c) avec un accès en lecture. |
| GitHub                   | Un dépôt et une source de constats : l’analyse du code, les vulnérabilités et logiciels malveillants signalés par `Dependabot`, les avis de sécurité et rapports privés de vulnérabilité, ou toutes les sources. Si vous n’indiquez pas de dépôt, Codex utilise, lorsqu’il est disponible, le dépôt GitHub associé au projet Codex actuel. Les issues GitHub ne sont pas incluses dans les sources GitHub par défaut ; fournissez une issue précise ou demandez explicitement les issues GitHub si vous souhaitez les trier. | Un accès authentifié à l’API REST GitHub, par exemple via `gh auth token`, `GH_TOKEN` ou `GITHUB_TOKEN`, avec l’autorisation de lire le dépôt et le type de constat sélectionnés.                                      |

Codex conserve un résultat pour chaque constat fourni, dans l’ordre d’entrée, afin que
chaque constat d’origine reste traçable. Il ne fusionne ni ne supprime les constats qui semblent
être des doublons.

## Exécutez le triage en lecture seule

Pour les constats fournis par copier-coller ou les artefacts locaux, envoyez un prompt de ce type :

```text
Use $codex-security:triage-finding to triage these existing security findings against this repository:

[Paste the findings or provide the artifact path.]

Pour les tickets Jira ou Linear, indiquez l’ensemble de tickets concerné et laissez le système source
en lecture seule :

```text
Use $codex-security:triage-finding to import and triage the security findings from [Jira or Linear issue URLs, identifiers, or query] against this repository.
Do not change the source issues.

Pour les constats GitHub, indiquez le dépôt et la source :

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from [owner/repository] against this repository.

Pour utiliser le dépôt GitHub associé au projet Codex actuel, indiquez
uniquement la source des constats :

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from GitHub against this repository. Use the GitHub repository attached to the current Codex project.

Le workflow se déroule dans l’ordre suivant :

1. Collectez et organisez les constats

   Codex récupère tout contenu demandé provenant d’un ticket ou de GitHub, conserve les
identifiants et références de la source, et crée un élément de triage par entrée. Il établit
la liste complète des éléments avant d’attribuer les verdicts.

2. Confirmez le contexte du dépôt

   Codex détermine le dépôt et la révision actuels lorsqu’ils sont disponibles. Il consulte
`SECURITY.md`, s’il est présent, afin de tenir compte des versions prises en charge, des entrées
   de confiance, des limites du produit et des surfaces hors périmètre dans l’évaluation.

3. Examinez les éléments de preuve statiques

   Pour chaque constat, Codex retrace la source supposément contrôlée par l’attaquant,
la mesure de sécurité pertinente, le puits vulnérable, le chemin accessible et le
périmètre de sécurité pris en charge. Il consigne les éléments qui étayent
l’allégation, ceux qui la contredisent et les lacunes dans les preuves.

4. Attribuez les verdicts et les rangs

   Codex attribue un verdict et un niveau de confiance à chaque constat. Il classe
les constats `confirmed` et `needs_review` selon leur exploitabilité, dans des files distinctes.

## Examinez les résultats

| Verdict          | Signification                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `confirmed`      | Les éléments de preuve du dépôt montrent que le chemin vulnérable est accessible selon les préconditions indiquées et qu’il franchit un périmètre de sécurité pris en charge.                     |
| `not_actionable` | Les éléments de preuve du dépôt réfutent l’allégation, par exemple en révélant une version non affectée, un chemin inaccessible, une mesure de protection efficace ou une surface absente du produit distribué.                 |
| `needs_review`   | Les éléments de preuve du dépôt ne permettent pas de trancher, car des informations requises sont manquantes ou ambiguës, ou dépendent de l’exécution, de l’environnement ou d’une politique. |

  Les rangs d’exploitabilité sont des entiers positifs commençant à `1`, attribués indépendamment
  dans chaque file de verdict. Les priorités de remédiation restent ainsi distinctes des
  travaux de révision encore en attente. Le rang `1` correspond au constat `confirmed` le plus exploitable
  ou au constat `needs_review` le plus prioritaire dans cet ensemble de résultats. Le rang
  n’est pas un score de gravité attribué par un scanner, et les constats `not_actionable` ne sont pas classés.

Pour chaque constat, examinez :

- la justification du verdict et du rang
- les éléments de preuve qui étayent l’allégation et ceux qui la contredisent
- les questions en suspens et les lacunes restantes dans les preuves
- l’emplacement concerné et le composant affecté
- la surface du produit et le niveau de confiance de la source
- la prochaine étape recommandée
- le transfert vers [`$codex-security:fix-finding`](/fr-FR/codex/security/plugin/fix-findings)
  à effectuer lorsque le constat est `confirmed`

Le triage est terminé lorsque chaque constat fourni possède un résultat, que Codex conserve
son identifiant source et que toute incertitude est explicite. Les enregistrements du backlog
dans Jira, Linear et les autres systèmes restent inchangés, sauf si vous demandez à Codex d’y répercuter les résultats du triage après
les avoir examinés.

## Étapes suivantes

- `confirmed` : Après validation du constat par une personne en vue de sa correction, utilisez
[`$codex-security:fix-finding`](/fr-FR/codex/security/plugin/fix-findings) pour le corriger, puis
  vérifier la correction. Le triage prépare un transfert directement utilisable dans un prompt, mais n’invoque pas la Skill
  automatiquement.
- `needs_review` : Si l’exécution du code peut combler la lacune dans les preuves, utilisez
`$codex-security:validation` pour effectuer une validation dynamique encadrée. À partir du résultat du triage, transmettez
  l’allégation associée au constat, les emplacements affectés, les préconditions, les éléments de preuve statiques et les
  lacunes dans les preuves :

  ```text
  Use $codex-security:validation to dynamically validate finding [triage item ID or source ID] from the backlog triage result. Use the strongest realistic, bounded method, record exactly what was tested, and preserve any remaining proof gaps.

  Contrairement au triage, la validation peut compiler ou exécuter du code, créer un test ciblé ou
  une preuve de concept, ou interagir avec une interface réelle. Examinez les commandes proposées
  avant de les approuver et maintenez [les politiques d’approbation et de sécurité
  de Codex](/fr-FR/codex/agent-approvals-security) en vigueur.

- `needs_review` : Si le constat dépend de la politique du produit ou du contexte de déploiement,
  répondez aux questions en suspens répertoriées avant de modifier le code.
- `not_actionable` : Conservez les éléments de preuve avec votre dossier de triage. Codex ne ferme pas le ticket d’origine et ne le met pas à jour
  automatiquement.
- Pour rechercher des vulnérabilités au-delà du backlog fourni, [exécutez une analyse de
  sécurité](/fr-FR/codex/security/plugin/scans).
