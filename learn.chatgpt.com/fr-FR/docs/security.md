<!-- source: https://learn.chatgpt.com/fr-FR/docs/security -->

Codex Security est un agent de sécurité applicative qui aide les équipes de sécurité et
d’ingénierie à détecter, confirmer et corriger les vulnérabilités. Utilisez-le dans
Codex, depuis votre terminal, via le SDK TypeScript ou avec des dépôts GitHub
connectés.

Pour une première analyse locale guidée, commencez par le guide [Démarrage rapide du plugin
Codex Security](/fr-FR/codex/security/plugin).

## Utilisez Codex Security dans l’application de bureau

Dans l’application de bureau ChatGPT, ouvrez le menu déroulant ChatGPT et sélectionnez **Codex**.
Installez et activez le plugin Codex Security pour ouvrir **Sécurité** dans la
barre latérale. L’atelier de sécurité regroupe vos analyses, vos résultats et vos dépôts en un
seul endroit pendant que Codex exécute chaque analyse dans une tâche.

- Utilisez **Analyses** pour lancer des analyses, suivre leur progression et consulter les résultats enregistrés.
- Utilisez **Résultats** pour examiner les problèmes et les preuves relevés dans les analyses terminées.
- Utilisez **Dépôts** pour consulter l’historique des dépôts et les résultats non résolus.

Consultez la page [Utilisez l’atelier de sécurité](/fr-FR/codex/security/plugin/workbench) pour découvrir le
workflow complet dans l’application de bureau.

### Explorez les cas d’utilisation du plugin

- [Lancez une analyse de sécurité](/fr-FR/codex/security/plugin/scans) sur un dépôt ou un seul dossier ciblé.
- [Lancez une analyse de sécurité approfondie](/fr-FR/codex/security/plugin/deep-scans) si vous avez besoin d’un examen plus complet et pouvez attendre plus longtemps la fin de l’analyse.
- [Examinez les modifications du code](/fr-FR/codex/security/plugin/code-changes) avant de fusionner une pull request ou une branche.
- [Triez un backlog](/fr-FR/codex/security/plugin/triage-backlog) lorsque vous disposez déjà de résultats de sécurité à examiner.
- [Corrigez et vérifiez les résultats](/fr-FR/codex/security/plugin/fix-findings) à l’aide de correctifs de portée limitée pour les résultats approuvés.
- [Exportez ou suivez les résultats](/fr-FR/codex/security/plugin/export-findings) sous forme d’artefacts portables ou vers des destinations de suivi soumises à approbation.
- [Rédigez des rapports de vulnérabilité](/fr-FR/codex/security/plugin/vulnerability-reports) à partir des résultats, des notes de divulgation, du code source et des PoCs fournis.
- [Proposez un renforcement de la sécurité](/fr-FR/codex/security/plugin/security-hardening) à partir des résultats d’analyse ou d’autres éléments probants liés à la sécurité.
- [Découvrez les nouveautés](/fr-FR/codex/security/plugin/changelog) du plugin Codex Security.

  L’atelier de sécurité de l’application de bureau et Codex CLI utilisent le plugin Codex Security.
  Codex Security dans le cloud analyse les dépôts GitHub connectés via Codex Cloud.
  Pour en savoir plus sur l’exécution en bac à sable, les approbations, les contrôles réseau et les paramètres d’administration de Codex, consultez
[Autorisations de l’agent et sécurité](/fr-FR/codex/agent-approvals-security).

## CLI et SDK de Codex Security

La CLI et le SDK TypeScript sont disponibles sous la forme du package public
[`@openai/codex-security`](https://github.com/openai/codex-security).
Exécutez la CLI avec `npx` :

```bash
npx @openai/codex-security --help

L’exécution d’analyses nécessite un accès à Codex Security. Pour obtenir les meilleurs résultats, utilisez un compte
vérifié pour [Trusted Access for Cyber](https://chatgpt.com/cyber).

Utilisez le même outil d’analyse que le plugin sur plusieurs dépôts et dans la durée. La CLI
recense les dépôts GitHub, reprend les analyses en lot, suit les résultats d’une analyse à l’autre
et enregistre les retours sur les faux positifs. Ajoutez votre architecture et vos politiques de sécurité,
définissez une limite de coût estimée ou exécutez des vérifications en CI et avant les commits.
Utilisez le SDK TypeScript pour intégrer les analyses, les rapports de progression et le contrôle des coûts
à une application ou à un outil de développement.

- [Commencez par le guide de démarrage rapide de la CLI](/fr-FR/codex/security/cli) pour configurer la CLI,
  effectuer les vérifications préalables d’un dépôt et lancer une analyse locale.
- [Lancez des analyses de sécurité en lot](/fr-FR/codex/security/cli/bulk-scans) pour recenser des dépôts
  GitHub ou lancer une campagne pouvant être reprise à partir d’un inventaire CSV.
- [Lancez des analyses en CI](/fr-FR/codex/security/cli/ci) pour examiner les modifications des pull requests,
  conserver les artefacts, téléverser des fichiers SARIF et définir une politique de gravité.
- [Consultez la FAQ de la CLI](/fr-FR/codex/security/cli/faq) pour obtenir des réponses sur l’historique des analyses,
  les retours sur les faux positifs, la couverture et la vérification des correctifs.
- [Consultez la référence de la CLI](/fr-FR/codex/security/cli/reference) pour vérifier la prise en charge des
  commandes, options, formats de sortie, artefacts et codes de sortie.
- [Intégrez le SDK TypeScript](/fr-FR/codex/security/sdk) pour sélectionner les cibles,
  examiner les résultats, suivre la progression et annuler les analyses depuis le code.

## Codex Security dans le cloud

Codex Security dans le cloud est actuellement disponible en préversion de recherche. Il analyse les dépôts GitHub
connectés pour repérer les problèmes de sécurité probables.

Il permet aux équipes de :

1. **Détecter les vulnérabilités probables** grâce à un modèle de menaces propre au dépôt et au contexte réel du code source.
2. **Réduire le bruit** en validant les résultats avant leur examen.
3. **Faciliter la correction des problèmes détectés** grâce à des résultats hiérarchisés, à des preuves et à des suggestions de correctifs.

## Fonctionnement de Codex Security dans le cloud

Codex Security analyse les dépôts connectés commit par commit.
Il construit le contexte d’analyse à partir de votre dépôt, évalue les vulnérabilités probables à la lumière de ce contexte et valide les problèmes présentant des indices solides dans un environnement isolé avant de les signaler.

Vous bénéficiez d’un workflow axé sur :

- un contexte propre au dépôt plutôt que des signatures génériques
- des preuves de validation qui contribuent à réduire les faux positifs
- des suggestions de correctifs que vous pouvez examiner sur GitHub

## Accès à Codex Security dans le cloud et prérequis

Codex Security dans le cloud fonctionne avec les dépôts GitHub connectés
via Codex Cloud. Si un dépôt n’est pas visible, vérifiez qu’il est disponible dans votre
espace de travail Codex Cloud ou contactez l’équipe OpenAI chargée de votre compte.

## Documentation associée

- Le [Démarrage rapide du plugin Codex Security](/fr-FR/codex/security/plugin) vous guide dans l’installation et la réalisation d’une première analyse locale.
- La page [Atelier de sécurité](/fr-FR/codex/security/plugin/workbench) présente les analyses enregistrées, les résultats, les dépôts et l’activité d’analyse dans l’application de bureau.
- Le [Démarrage rapide de la CLI Codex Security](/fr-FR/codex/security/cli) vous guide dans la configuration, les vérifications préalables et la réalisation d’une première analyse dans le terminal.
- La page [Lancez des analyses de sécurité en lot](/fr-FR/codex/security/cli/bulk-scans) présente le recensement des dépôts GitHub, les inventaires CSV, les résultats de campagne et le fonctionnement de la reprise.
- La [FAQ de la CLI Codex Security](/fr-FR/codex/security/cli/faq) répond aux questions fréquentes sur les analyses, les résultats, la couverture et les coûts.
- Le [SDK TypeScript de Codex Security](/fr-FR/codex/security/sdk) explique comment exécuter des analyses depuis une application ou un outil de développement.
- La page [Configuration de Codex Security dans le cloud](/fr-FR/codex/security/setup) détaille la configuration, les analyses et l’examen des résultats.
- La page [Révision de sécurité](/fr-FR/codex/security/security-review) explique comment effectuer des revues de sécurité approfondies des pull requests GitHub.
- La page [Améliorer le modèle de menaces](/fr-FR/codex/security/threat-model) explique comment ajuster le périmètre, les points d’entrée et les hypothèses de criticité.
- La [FAQ sur Codex Security dans le cloud](/fr-FR/codex/security/faq) répond aux questions fréquentes sur le produit cloud.
