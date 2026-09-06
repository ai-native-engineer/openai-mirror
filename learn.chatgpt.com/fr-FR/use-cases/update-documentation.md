<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/update-documentation -->

## Introduction

Il est plus facile de maintenir la documentation à jour en la modifiant en même temps que le code source, plutôt que plusieurs semaines plus tard. Codex peut examiner le code et les tests modifiés, les notes de version, les issues associées et le contexte des pull requests, puis rédiger une mise à jour ciblée de la documentation qui en respecte la structure existante.

Utilisez ce flux de travail pour la documentation destinée aux développeurs, les mises à jour de fichiers README, les brouillons du journal des modifications, les notes de migration, les guides d’exploitation ou tout autre contenu qui doit rester à jour à mesure que les comportements évoluent.

## Comment l’utiliser

1. Commencez par la modification à documenter.

   Partagez la branche, la pull request, le commit, l’issue ou les fichiers concernés. Si la documentation est publique, précisez explicitement que la feuille de route non publiée, les informations privées sur les clients et le contexte réservé à un usage interne ne doivent pas y figurer.

2. Demandez à Codex de recenser les pages de documentation concernées.

   Avant la rédaction, demandez-lui de rechercher dans la documentation existante les noms de fonctionnalités, les clés de configuration, les commandes, les exemples et les termes connexes.

3. Limitez les modifications de la documentation au strict nécessaire.

   Codex doit préserver la structure actuelle de la page, la terminologie, les liens croisés et le frontmatter. Il doit éviter de réécrire de larges portions lorsqu’une note ciblée, un exemple ou la mise à jour d’une section suffit.

4. Vérifiez les modifications.

   Demandez à Codex d’exécuter les vérifications de mise en forme et de documentation adaptées au dépôt, puis de résumer les éléments qui étayent chaque affirmation concernant le comportement visible par les utilisateurs.

## Ce qu’il faut fournir à Codex

| Source                               | Pourquoi c’est utile                                                               |
| ------------------------------------ | -------------------------------------------------------------------------- |
| Code et tests modifiés               | Permet à Codex d’analyser le comportement réel pour rédiger des mises à jour ciblées de la documentation. |
| Notes de version publiques ou documentation du produit | Aide Codex à refléter fidèlement la terminologie publique, la disponibilité et le statut de la fonctionnalité.    |
| Contexte de la pull request ou de l’issue        | Explique pourquoi la modification a été apportée et quel comportement visible par les utilisateurs doit être pris en compte.   |
| Vérifications locales de la documentation                    | Fournit à Codex des critères concrets pour déterminer si le travail est terminé avant de publier la documentation.   |

Fournir davantage de contexte, par exemple des notes de version publiques, aide Codex à éviter d’inclure des informations privées ou des mises à jour qui ne sont pas encore publiques.

## Rendez le flux de travail reproductible

Pour établir une convention à l’échelle du dépôt, ajoutez les exigences relatives à la documentation dans [AGENTS.md](/fr-FR/codex/agent-configuration/agents-md). Par exemple :

```md
## Documentation

- When user-facing behavior changes, check whether docs, examples, or changelogs need updates.
- Public docs must only include public information or behavior visible in this repo.
- Preserve existing terminology and frontmatter.
- Run the docs formatting and build checks before final handoff.

Si le processus comporte davantage d’étapes, transformez-le en [skill](/fr-FR/codex/build-skills) afin que les tâches Codex à venir puissent suivre le même cycle d’examen des sources, de rédaction et de vérification. Pour en savoir plus sur cette approche, consultez [Enregistrer des flux de travail sous forme de Skills](/fr-FR/codex/use-cases/reusable-codex-skills).

Vous pouvez aussi [planifier une tâche pour ce flux de travail depuis la discussion en cours](/fr-FR/codex/automations#schedule-a-task-inside-a-chat). Par exemple, demandez à Codex de récupérer les pull requests GitHub récentes et de maintenir la documentation à jour chaque semaine :
