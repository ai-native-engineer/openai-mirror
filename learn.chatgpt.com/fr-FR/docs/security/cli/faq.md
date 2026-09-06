<!-- source: https://learn.chatgpt.com/fr-FR/docs/security/cli/faq -->

Trouvez les réponses aux questions fréquentes sur l’analyse des dépôts et la gestion
des problèmes de sécurité détectés depuis le terminal. Pour l’installation et une première analyse, commencez
par le [démarrage rapide de la CLI](/fr-FR/codex/security/cli).

## Analyses de dépôts

### Qui peut utiliser la CLI

Le package `@openai/codex-security` est public.

L’exécution d’analyses nécessite un accès à Codex Security. Pour obtenir les meilleurs résultats, utilisez un compte
vérifié pour [Trusted Access for Cyber](https://chatgpt.com/cyber).

### Pourquoi une analyse utilise-t-elle une clé API après la connexion

Lorsque votre environnement contient `OPENAI_API_KEY` ou `CODEX_API_KEY`, les analyses
sans terminal interactif et celles aux formats JSON et JSONL utilisent par défaut la clé API
de l’environnement, même après une connexion réussie avec ChatGPT ou un token d’accès.
Les analyses interactives avec sortie texte vous demandent de choisir lorsqu’une connexion ChatGPT est
également disponible. Les exécutions à blanc ne demandent aucune saisie et ne chargent aucun identifiant.

Pour utiliser vos identifiants enregistrés lors d’une analyse, sélectionnez-les explicitement :

```bash
npx @openai/codex-security scan . --auth chatgpt

Pour imposer l’utilisation d’une clé API définie dans `OPENAI_API_KEY` ou `CODEX_API_KEY` :

```bash
npx @openai/codex-security scan . --auth api-key

Pour que vos identifiants enregistrés soient automatiquement utilisés par défaut, exécutez
`unset OPENAI_API_KEY CODEX_API_KEY`. Pour connaître tous les modes d’authentification pris en charge,
consultez la [référence de la CLI](/fr-FR/codex/security/cli/reference#select-scan-authentication).

### Comment fonctionne l’analyse groupée de dépôts

Connectez-vous à l’aide de la CLI GitHub :

```bash
gh auth login

Recherchez et sélectionnez des dépôts d’un compte ou d’une organisation GitHub :

```bash
npx @openai/codex-security bulk-scan

Pour utiliser une liste préparée, fournissez un fichier CSV de dépôts et un répertoire de sortie :

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

Consultez [Lancez des analyses de sécurité groupées](/fr-FR/codex/security/cli/bulk-scans) pour découvrir comment rechercher des dépôts GitHub,
utiliser le format CSV et consulter les résultats des campagnes et les options disponibles.

### Une analyse groupée interrompue peut-elle reprendre

Oui. Exécutez la même commande d’analyse groupée avec le fichier CSV et le répertoire de sortie d’origine.
Codex Security ignore les dépôts dont l’analyse est déjà terminée.

Ajoutez `--max-attempts 3` pour réessayer en cas d’erreur temporaire liée au dépôt ou à l’analyse :

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

Une analyse terminée dont la couverture est `partial` ou `unknown` conserve ses résultats et
entraîne la fin de la campagne avec le code de sortie `2`. Elle ne fait l’objet d’aucune nouvelle tentative, même avec
`--max-attempts`.

### Comment une analyse peut-elle prendre en compte l’architecture et les politiques de sécurité

Fournissez des documents d’architecture, des modèles de menaces ou des politiques de sécurité avec
`--knowledge-base` :

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Codex Security utilise ces documents comme contexte pour l’analyse en cours. Pour connaître
les types de fichiers pris en charge et le fonctionnement avec les répertoires, consultez [Ajouter un contexte
de sécurité](/fr-FR/codex/security/cli/reference#add-security-context).

## Problèmes détectés et couverture

### Où les équipes peuvent-elles trouver les résultats des analyses précédentes

Affichez la liste des analyses enregistrées pour votre dépôt :

```bash
npx @openai/codex-security scans list /path/to/repository

Utilisez l’ID d’une analyse fourni dans les résultats pour examiner les problèmes détectés :

```bash
npx @openai/codex-security scans show SCAN_ID

Chaque analyse terminée regroupe son rapport, les problèmes détectés, la couverture et les
artefacts associés. Consultez [Artefacts
d’analyse](/fr-FR/codex/security/cli/reference#scan-artifacts) pour connaître leur organisation complète.

Pour examiner les événements enregistrés concernant les analyses et les workers, exécutez `scans logs SCAN_ID`. Ces journaux
ne sont pas expurgés et peuvent contenir du code source ou des identifiants.

### Que faire si la CLI ne peut pas enregistrer l’historique des analyses

Codex Security conserve l’historique des analyses dans une base de données du workbench. Si le répertoire
par défaut des données d’état n’est pas accessible en écriture, choisissez un répertoire privé en dehors du
dépôt :

```bash

### Comment les analyses distinguent-elles les problèmes nouveaux et connus

Affichez la liste des problèmes non résolus issus de toutes les analyses d’un dépôt :

```bash
npx @openai/codex-security findings list /path/to/repository

La liste indique les problèmes confirmés par la dernière analyse et les problèmes antérieurs non
résolus que cette analyse n’a pas confirmés.

Comparez les problèmes détectés par les deux analyses :

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

La comparaison associe automatiquement les problèmes selon leur cause racine, réutilise les correspondances
enregistrées et identifie les problèmes nouveaux, persistants, rouverts, résolus ou d’état
inconnu. Un problème n’est considéré comme résolu que si l’analyse ultérieure couvre sa
cible d’origine et le chemin concerné sans lacune de couverture.

### Comment fonctionne le retour d’information sur les faux positifs

Examinez l’analyse enregistrée pour trouver l’ID d’occurrence :

```bash
npx @openai/codex-security scans show SCAN_ID

Consignez la raison pour laquelle ce problème ne s’applique pas :

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

Les analyses ultérieures du même dépôt utilisent cette explication comme contexte. Elles
continuent toutefois de vérifier indépendamment le code source actuel, les contrôles et l’atteignabilité. Le
rejet d’un problème ne supprime aucune règle, aucun chemin ni aucune catégorie de vulnérabilité.

Pour en savoir plus sur les commandes, consultez la [référence des problèmes
détectés](/fr-FR/codex/security/cli/reference#codex-security-findings).

### Pourquoi des analyses successives peuvent-elles détecter des problèmes différents

Les analyses assistées par l’IA peuvent varier, même avec la même configuration d’analyse. Commencez par
relancer votre analyse de référence :

```bash
npx @openai/codex-security scans rerun BASELINE_SCAN_ID

La nouvelle exécution conserve la configuration initiale de l’analyse et nécessite la même version du
plugin. Si le plugin installé a changé, la commande s’arrête.

Comparez l’analyse de référence à la nouvelle analyse :

```bash
npx @openai/codex-security scans compare BASELINE_SCAN_ID REPEAT_SCAN_ID

Fournissez des consignes communes sur l’architecture et la sécurité lorsqu’un manque de contexte peut
contribuer aux variations. La mise en correspondance peut reconnaître le même problème sous-jacent
d’une exécution à l’autre, mais elle ne rend pas les analyses déterministes. Revérifiez directement tout
problème important qui disparaît.

### Comment une équipe peut-elle confirmer l’efficacité d’un correctif

Après avoir appliqué un correctif, relancez l’analyse initiale :

```bash
npx @openai/codex-security scans rerun BEFORE_SCAN_ID

Comparez les problèmes détectés initialement avec la nouvelle analyse :

```bash
npx @openai/codex-security scans compare BEFORE_SCAN_ID AFTER_SCAN_ID

Vérifiez que la nouvelle analyse couvre la cible d’origine et le chemin concerné sans
lacune de couverture. Revérifiez ensuite directement le problème initial dans la copie de travail
actuelle :

```bash
npx @openai/codex-security validate /path/to/original/findings.json \
  "Recheck the SQL injection in src/orders.ts:42 against the current code"

Ni la disparition d’un problème détecté ni une simple comparaison des analyses ne suffisent à prouver l’efficacité d’un correctif.

### Que signifie une couverture incomplète

La couverture peut avoir la valeur `complete`, `partial` ou `unknown`. Examinez `coverage.json`
pour repérer les chemins exclus, les surfaces dont l’analyse est différée et les questions en suspens avant de considérer qu’une
analyse atteste qu’une révision a été effectuée.

Les analyses dont la couverture est partielle ou inconnue renvoient le code de sortie `2`, même sans
politique relative au niveau de gravité. Elles conservent néanmoins les problèmes détectés et les données de couverture disponibles. Une analyse ultérieure
ne peut pas établir qu’un problème antérieur n’existe plus si elle ne couvre pas
le chemin d’origine de ce problème.

## Automatisation et coût

### Comment fonctionnent les limites de durée des analyses approfondies

Définissez une échéance pour les workers lorsque vous lancez une analyse approfondie :

```bash
npx @openai/codex-security scan . --mode deep --max-time-hours 1.5

La durée par défaut est de `96` heures. Utilisez toute valeur positive inférieure ou égale à `96`, y compris
une valeur fractionnaire. À l’échéance, Codex Security arrête les workers qui n’ont pas terminé, conserve
les résultats des analyses standard terminées et les regroupe dans le rapport final. Si aucun worker
n’achève la revue du code source, le rapport indique une couverture partielle et la
CLI renvoie le code de sortie `2`.

Pour les paramètres persistants ou les campagnes groupées, définissez `max_time_hours` dans la section
`[deep_scan]` de la [configuration des analyses
approfondies](/fr-FR/codex/security/cli/reference#configure-deep-scans).

### Comment fonctionnent les limites de coût des analyses

Définissez une limite de coût estimée en USD avant de lancer l’analyse :

```bash
npx @openai/codex-security scan . --max-cost 5

La limite constitue une estimation et non un plafond de dépenses strict. Les requêtes déjà en
cours peuvent se terminer au-delà de cette limite. Si une analyse approfondie l’atteint après que
Codex Security a regroupé les résultats des workers terminés, la CLI enregistre le
rapport finalisé avec une couverture partielle et se termine avec le code `2`. Dans le cas contraire, elle conserve
toute sortie partielle disponible.

### Les analyses peuvent-elles vérifier les commits et les pull requests

Installez un contrôle de sécurité pre-commit pour les modifications indexées et non indexées :

```bash
npx @openai/codex-security install-hook

Pour vérifier les pull requests, analysez les modifications enregistrées dans un commit et définissez un seuil de
gravité :

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --fail-on-severity high

Une analyse complète renvoie le code de sortie `1` lorsqu’elle détecte un problème dont la gravité atteint ou dépasse le niveau
sélectionné. Consultez [Lancez des analyses en CI](/fr-FR/codex/security/cli/ci) pour découvrir le
workflow GitHub Actions complet, la gestion des artefacts et l’export au format SARIF.

### Une autre application peut-elle lancer directement des analyses

Oui. Utilisez le [SDK TypeScript](/fr-FR/codex/security/sdk) pour lancer des analyses, sélectionner des
cibles, examiner les problèmes détectés et la couverture, suivre l’avancement et contrôler les coûts
depuis une application ou un outil de développement.
