<!-- source: https://learn.chatgpt.com/fr-FR/docs/customization/overview -->

La personnalisation vous permet d’adapter Codex aux méthodes de travail de votre équipe.

Dans Codex, la personnalisation repose sur plusieurs couches complémentaires :

- **Consignes de projet (`AGENTS.md`)** pour définir des instructions persistantes
- **[Mémoires](/fr-FR/codex/customization/memories)** pour conserver le contexte utile acquis lors de travaux précédents
- **Skills** pour les flux de travail réutilisables et l’expertise métier
- **[MCP](/fr-FR/codex/extend/mcp)** pour accéder à des outils externes et à des systèmes partagés
- **[Sous-agents](/fr-FR/codex/agent-configuration/subagents)** pour déléguer des tâches à des sous-agents spécialisés

Ces éléments sont complémentaires et non concurrents. `AGENTS.md` façonne le comportement, les mémoires
conservent le contexte local pour la suite, les skills regroupent des processus reproductibles et
[MCP](/fr-FR/codex/extend/mcp) relie Codex à des systèmes extérieurs à l’espace de travail local.

## Consignes AGENTS

Le fichier `AGENTS.md` fournit à Codex des consignes de projet persistantes qui accompagnent votre dépôt et s’appliquent avant que l’agent commence à travailler. Gardez-le concis.

Utilisez-le pour définir les règles que Codex doit systématiquement suivre dans un dépôt, par exemple :

- Commandes de compilation et de test
- Critères de revue
- Conventions propres au dépôt
- Instructions propres aux répertoires

Lorsque l’agent émet des hypothèses erronées sur votre code source, corrigez-les dans `AGENTS.md` et demandez-lui de mettre à jour `AGENTS.md` afin de pérenniser la correction. Faites de ce processus une boucle de rétroaction.

**Mise à jour de `AGENTS.md` :** Commencez par les seules instructions essentielles. Formalisez les retours de revue récurrents, placez les consignes dans le répertoire le plus proche de l’endroit où elles s’appliquent et demandez à l’agent de mettre à jour `AGENTS.md` lorsque vous corrigez un point, afin que la correction s’applique aux sessions suivantes.

### Quand mettre à jour `AGENTS.md`

- **Erreurs répétées** : si l’agent répète la même erreur, ajoutez une règle.
- **Lecture excessive** : s’il trouve les bons fichiers mais consulte trop de documents, ajoutez des consignes d’orientation (répertoires ou fichiers à privilégier).
- **Retours récurrents sur les PRs** : si vous formulez plusieurs fois le même retour, formalisez-le.
- **Dans GitHub** : dans un commentaire de pull request, mentionnez `@codex` en lui adressant une demande (par exemple, `@codex add this to AGENTS.md`) afin de déléguer la mise à jour à une discussion dans le cloud.
- **Automatisez la détection des écarts** : utilisez les [Tâches planifiées](/fr-FR/codex/automations) pour effectuer des contrôles récurrents (par exemple, chaque jour) qui repèrent les lacunes dans les consignes et suggèrent les éléments à ajouter à `AGENTS.md`.

Associez `AGENTS.md` à une infrastructure qui fait respecter ces règles : les hooks pre-commit, les linters et les vérificateurs de types détectent les problèmes avant même que vous ne les voyiez, ce qui permet au système de mieux prévenir les erreurs récurrentes.

Codex peut charger des consignes depuis plusieurs emplacements : un fichier global dans le répertoire d’accueil de Codex (pour vous en tant que développeur) et des fichiers propres au dépôt que les équipes peuvent versionner. Les fichiers les plus proches du répertoire de travail sont prioritaires.
Utilisez le fichier global pour définir la manière dont Codex communique avec vous (par exemple, le style de revue, le niveau de détail et les valeurs par défaut) et réservez les fichiers du dépôt aux règles propres à l’équipe et au code source.

[Instructions personnalisées avec AGENTS.md](/fr-FR/codex/agent-configuration/agents-md)

## Skills

Les skills dotent Codex de capacités réutilisables pour des flux de travail reproductibles.
Les skills sont souvent le meilleur choix pour ces flux de travail, car ils permettent d’utiliser des instructions plus détaillées, des scripts et des références, tout en restant réutilisables d’une tâche à l’autre.
Les skills sont chargés et accessibles à l’agent (au moins leurs métadonnées), afin que Codex puisse les découvrir et les sélectionner implicitement. Les flux de travail complets restent ainsi disponibles sans alourdir le contexte dès le départ.

Utilisez des dossiers de skills pour concevoir et améliorer vos flux de travail en local. S’il existe déjà un plugin
pour ce flux de travail, installez-le d’abord afin de réutiliser une configuration éprouvée. Lorsque
vous souhaitez diffuser votre propre flux de travail auprès de plusieurs équipes ou le regrouper avec des
connecteurs, distribuez-le sous forme de [plugin](/fr-FR/codex/build-plugins). Les skills restent le
format de création ; les plugins sont l’unité de distribution installable.

Un skill se compose généralement d’un fichier `SKILL.md`, auquel peuvent s’ajouter des scripts, des références et des ressources.

Le répertoire du skill peut inclure un dossier `scripts/` contenant des scripts CLI que Codex appelle dans le cadre du flux de travail (par exemple, pour initialiser des données ou exécuter des validations). Si le flux de travail nécessite des systèmes externes (outils de suivi des tickets, outils de design ou serveurs de documentation), associez le skill à [MCP](/fr-FR/codex/extend/mcp).

Exemple de fichier `SKILL.md` :

```md
---
name: commit
description: Stage and commit changes in semantic groups. Use when the user wants to commit, organize commits, or clean up a branch before pushing.
---

1. Do not run `git add .`. Stage files in logical groups by purpose.
2. Group into separate commits: feat → test → docs → refactor → chore.
3. Write concise commit messages that match the change scope.
4. Keep each commit focused and reviewable.

Utilisez les skills pour :

- Flux de travail reproductibles (étapes de publication, routines de revue, mises à jour de la documentation)
- Expertise propre à l’équipe
- Procédures nécessitant des exemples, des références ou des scripts utilitaires

Les skills peuvent être globaux (dans votre répertoire utilisateur, pour vous en tant que développeur) ou propres au dépôt (versionnés dans `.agents/skills`, pour votre équipe). Placez les skills du dépôt dans `.agents/skills` lorsque le flux de travail concerne ce projet ; utilisez votre répertoire utilisateur pour les skills à employer dans tous vos dépôts.

| Couche  | Global               | Dépôt                                           |
| :----- | :------------------- | :--------------------------------------------- |
| AGENTS | `~/.codex/AGENTS.md` | `AGENTS.md` à la racine du dépôt ou dans des sous-répertoires |
| Skills | `~/.agents/skills`   | `.agents/skills` dans le dépôt                       |

Codex charge progressivement les skills :

- Il commence par les métadonnées (`name`, `description`) pour identifier les skills
- Il ne charge `SKILL.md` qu’une fois un skill sélectionné
- Il consulte les références ou exécute les scripts uniquement en cas de besoin

Les skills peuvent être invoqués explicitement, et Codex peut aussi les sélectionner implicitement lorsque la tâche correspond à leur description. Des descriptions claires améliorent la fiabilité de leur déclenchement.

[Créer des skills](/fr-FR/codex/build-skills)

## MCP

MCP (Model Context Protocol) est le moyen standard de connecter Codex à des outils externes et à des fournisseurs de contexte.
Il est particulièrement utile pour les systèmes hébergés à distance, tels que Figma, Linear, GitHub ou les services internes de gestion des connaissances dont dépend votre équipe.

Utilisez MCP lorsque Codex a besoin de fonctionnalités accessibles hors du dépôt local, comme des outils de suivi des tickets, des outils de design, des navigateurs ou des systèmes de documentation partagée.

Vous pouvez le voir ainsi :

- **Hôte** : Codex
- **Client** : la connexion MCP dans Codex
- **Serveur** : l’outil externe ou le fournisseur de contexte

Les serveurs MCP peuvent exposer :

- **Outils** (actions)
- **Ressources** (données consultables)
- **Prompts** (modèles de prompts réutilisables)

Cette séparation permet de mieux cerner les limites en matière de confiance et de capacités. Certains serveurs fournissent principalement du contexte, tandis que d’autres donnent accès à des actions puissantes.

En pratique, MCP est souvent particulièrement utile en association avec des Skills :

- Un skill définit le flux de travail et indique les outils MCP à utiliser

[Model Context Protocol](/fr-FR/codex/extend/mcp)

## Sous-agents

Vous pouvez créer plusieurs agents, leur attribuer des rôles différents et leur demander d’utiliser les outils de différentes façons. Par exemple, un agent peut utiliser des commandes et des configurations de test spécifiques, tandis qu’un autre dispose de serveurs MCP qui récupèrent les journaux de production à des fins de débogage. Chaque sous-agent reste concentré sur sa tâche et utilise les outils adaptés à son rôle.

[Sous-agents](/fr-FR/codex/agent-configuration/subagents)

## Association des Skills et de MCP

C’est en associant les Skills à MCP que tout se met en place : les Skills définissent des flux de travail reproductibles, et MCP les relie à des outils et des systèmes externes.
Si un skill dépend de MCP, déclarez cette dépendance dans `agents/openai.yaml` pour que Codex puisse l’installer et l’intégrer automatiquement (voir [Créer des Skills](/fr-FR/codex/build-skills)).

## Étape suivante

Procédez dans cet ordre :

1. [Instructions personnalisées avec AGENTS.md](/fr-FR/codex/agent-configuration/agents-md) pour que Codex respecte les conventions de votre dépôt. Ajoutez des hooks pre-commit et des linters pour faire respecter ces règles.
2. Installez un [plugin](/fr-FR/codex/plugins) lorsqu’un flux de travail réutilisable existe déjà. Sinon, créez un [skill](/fr-FR/codex/build-skills), puis distribuez-le sous forme de plugin lorsque vous souhaitez le partager.
3. Utilisez [MCP](/fr-FR/codex/extend/mcp) lorsque les flux de travail nécessitent l’accès à des systèmes externes (Linear, GitHub, serveurs de documentation, outils de design).
4. Faites appel aux [Sous-agents](/fr-FR/codex/agent-configuration/subagents) lorsque vous êtes prêt à leur déléguer des tâches générant beaucoup de bruit ou des tâches spécialisées.
