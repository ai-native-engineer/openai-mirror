<!-- source: https://learn.chatgpt.com/fr-FR/docs/build-skills -->

Utilisez les skills d’agent pour doter ChatGPT et Codex de capacités adaptées à des tâches spécifiques. Un
skill regroupe des instructions, des ressources et, éventuellement, des scripts pour permettre à chaque produit
de suivre un workflow de manière fiable. Les skills reposent sur le
[standard ouvert des skills d’agent](https://agentskills.io).

Les skills sont le format de création des workflows réutilisables. Les plugins permettent de distribuer
des skills et des connecteurs réutilisables via le répertoire universel de plugins partagé
par ChatGPT et Codex. Les plugins fonctionnent dans Discussion et Work avec ChatGPT sur le web,
sur ordinateur et sur mobile, dans Codex au sein de l’application de bureau ChatGPT, et via Codex
CLI. Utilisez des skills pour concevoir le workflow lui-même, puis créez un
[plugin](https://developers.openai.com/plugins/build/plugins) si vous souhaitez que
d’autres personnes puissent l’installer.

Les skills autonomes sont disponibles dans l’application de bureau ChatGPT, Codex CLI et l’extension
IDE. Les skills inclus dans des plugins sont également disponibles dans Discussion et Work sur les versions
web, de bureau et mobile de ChatGPT.

Dans l’application de bureau ChatGPT, ouvrez **Skills** dans la barre latérale pour consulter et explorer les skills
créés dans l’ensemble de vos projets.

  
    
  

Les skills utilisent la **divulgation progressive** pour gérer efficacement le contexte. ChatGPT et
Codex commencent par le nom et la description de chaque skill, puis chargent l’intégralité des instructions du fichier
`SKILL.md` lorsqu’ils décident d’utiliser ce skill.

Dans Codex, la liste initiale indique également le chemin du fichier de chaque skill. Pour éviter
qu’elle n’empiète sur le reste du prompt, cette liste utilise au maximum 2 % de la fenêtre de
contexte du modèle, ou 8 000 caractères lorsque cette fenêtre est inconnue. Si de nombreux
skills sont installés, Codex raccourcit d’abord leur description. Lorsque les skills sont très
nombreux, Codex peut en omettre certains de la liste initiale et afficher un avertissement.

Ce budget s’applique uniquement à la liste initiale des skills. Lorsque Codex sélectionne un skill, il lit toujours l’intégralité des instructions du fichier SKILL.md de ce skill.

Un skill est un répertoire contenant un fichier `SKILL.md` et, éventuellement, des scripts et des références. Le fichier `SKILL.md` doit inclure `name` et `description`.

<a id="how-codex-uses-skills"></a>

## Comment ChatGPT et Codex utilisent les skills

ChatGPT et Codex peuvent activer des skills de deux façons :

1. **Invocation explicite :** Incluez directement le skill dans votre prompt. Dans
   ChatGPT, saisissez `@` pour sélectionner un skill. Dans Codex CLI ou l’extension IDE, exécutez
`/skills` ou saisissez `$` pour mentionner un skill.
2. **Invocation implicite :** ChatGPT ou Codex peut choisir un skill lorsque votre tâche
   correspond à sa `description`.

Comme la correspondance implicite dépend de `description`, rédigez des descriptions concises
qui définissent clairement leur périmètre et leurs limites. Placez le cas d’usage principal et les mots déclencheurs au début
afin qu’un hôte puisse identifier le skill même lorsque les descriptions sont raccourcies.

## Créer un skill

Si vous connaissez déjà le workflow et qu’il est plus facile à montrer qu’à décrire, utilisez
[Enregistrer et rejouer](/fr-FR/codex/extend/record-and-replay). L’outil d’enregistrement capture le
workflow, analyse ses étapes et prépare une ébauche de skill réutilisable à partir de la
démonstration.

Si vous préférez décrire le skill, utilisez l’outil de création intégré. Dans ChatGPT
Work, invoquez-le avec `@skill-creator`. Dans Codex, invoquez-le ainsi :

```text
$skill-creator

L’outil de création vous demande ce que fait le skill, quand il doit se déclencher et s’il doit contenir uniquement des instructions ou inclure des scripts. Par défaut, il ne contient que des instructions.

Vous pouvez également créer un skill manuellement en créant un dossier contenant un fichier `SKILL.md` :

```md
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for ChatGPT or Codex to follow.

Codex détecte automatiquement les modifications apportées aux skills. Si une mise à jour n’apparaît pas, redémarrez Codex.

<a id="where-to-save-skills"></a>

## Où Codex charge les skills locaux

Codex lit les skills aux emplacements propres au dépôt, à l’utilisateur, à l’administrateur et au système. Dans les dépôts, Codex recherche `.agents/skills` dans chaque répertoire, du répertoire de travail courant jusqu’à la racine du dépôt. Si deux skills ont le même `name`, Codex ne les fusionne pas ; tous deux peuvent apparaître dans les sélecteurs de skills.

| Portée du skill | Emplacement                                                                                                  | Utilisation suggérée                                                                                                                                                                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REPO`      | `$CWD/.agents/skills` <br /> Répertoire de travail courant : emplacement à partir duquel vous lancez Codex.                           | Si vous travaillez dans un dépôt ou un environnement de développement, les équipes peuvent versionner des skills adaptés à un dossier de travail, par exemple des skills propres à un microservice ou à un module.                              |
| `REPO`      | `$CWD/../.agents/skills` <br /> Un dossier situé au-dessus de CWD lorsque vous lancez Codex dans un dépôt Git.         | Si vous travaillez dans un dépôt comprenant des dossiers imbriqués, les organisations peuvent versionner, dans un dossier parent, des skills adaptés à un espace partagé.                                                                       |
| `REPO`      | `$REPO_ROOT/.agents/skills` <br /> Le dossier racine situé au plus haut niveau lorsque vous lancez Codex dans un dépôt Git. | Si vous travaillez dans un dépôt comprenant des dossiers imbriqués, les organisations peuvent versionner des skills utiles à toutes les personnes qui utilisent ce dépôt. Ces skills racine sont accessibles depuis tous les sous-dossiers du dépôt. |
| `USER`      | `$HOME/.agents/skills` <br /> Tous les skills versionnés dans le dossier personnel de l’utilisateur.                         | Utilisez cet emplacement pour constituer une sélection de skills propres à un utilisateur et applicables à tous les dépôts dans lesquels il peut travailler.                                                                                                           |
| `ADMIN`     | `/etc/codex/skills` <br /> Tous les skills versionnés à un emplacement système partagé sur la machine ou dans le conteneur. | Utilisez cet emplacement pour les scripts SDK, l’automatisation et le versionnage des skills d’administration par défaut accessibles à chaque utilisateur de la machine.                                                                                     |
| `SYSTEM`    | Inclus dans Codex par OpenAI.                                                                             | Des skills utiles à un large public, comme skill-creator et plan. Ils sont accessibles à tous dès le lancement de Codex.                                                                   |

Codex prend en charge les dossiers de skills accessibles par lien symbolique et suit la cible du lien lorsqu’il analyse ces emplacements.

Ces emplacements servent à créer et à découvrir des skills en local. Si vous souhaitez
distribuer des skills réutilisables au-delà d’un seul dépôt ou, éventuellement, les associer à des
connecteurs, utilisez des [plugins](https://developers.openai.com/plugins/build/plugins).

## Distribuer des skills avec des plugins

Les dossiers de skills conviennent surtout à la création locale et aux workflows propres à un dépôt. Si
vous souhaitez distribuer un skill réutilisable, regrouper au moins deux skills ou
fournir un skill avec un connecteur, regroupez-les dans un
[plugin](https://developers.openai.com/plugins/build/plugins).

Les plugins peuvent inclure un ou plusieurs skills. Ils peuvent aussi regrouper, de façon facultative,
des connexions enregistrées à des serveurs MCP, une configuration intégrée de serveurs MCP et
des ressources de présentation au sein d’un même package.

## Installer des skills sélectionnés pour un usage local

Pour ajouter des skills sélectionnés à votre configuration locale de Codex, en plus des skills intégrés, utilisez `$skill-installer`. Par exemple, pour installer le skill `$linear` :

```bash
$skill-installer linear

Vous pouvez également demander au programme d’installation de télécharger des skills depuis d’autres dépôts.
Codex détecte automatiquement les skills nouvellement installés ; si l’un d’eux n’apparaît pas,
redémarrez Codex.

Utilisez cette méthode pour la configuration locale et les expérimentations. Pour distribuer vos
propres skills sous une forme réutilisable, privilégiez les plugins.

## Activer ou désactiver les skills locaux de Codex

Utilisez les entrées `[[skills.config]]` dans `~/.codex/config.toml` pour désactiver un skill sans le supprimer :

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false

Redémarrez Codex après avoir modifié `~/.codex/config.toml`.

## Métadonnées facultatives

Ajoutez `agents/openai.yaml` pour configurer les métadonnées de l’interface utilisateur dans [l’application de bureau ChatGPT](/fr-FR/codex/app), définir la politique d’invocation et déclarer les dépendances aux outils afin de faciliter l’utilisation du skill.

```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
  brand_color: "#3B82F6"
  default_prompt: "Optional surrounding prompt to use the skill with"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"

`allow_implicit_invocation` (valeur par défaut : `true`) : lorsque cette valeur est `false`, Codex n’invoque pas implicitement le skill à partir du prompt de l’utilisateur ; l’invocation explicite via `$skill` reste possible.

## Bonnes pratiques

- Limitez chaque skill à une seule tâche.
- Privilégiez les instructions aux scripts, sauf si vous avez besoin d’un comportement déterministe ou d’outils externes.
- Rédigez les étapes à l’impératif en indiquant explicitement les entrées et les sorties.
- Testez des prompts par rapport à la description du skill afin de vérifier qu’il se déclenche correctement.

Pour d’autres exemples, consultez
[Réparation de la CI GitHub](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci),
[PDF](https://github.com/openai/skills/tree/main/skills/.curated/pdf),
[Linear](https://github.com/openai/skills/tree/main/skills/.curated/linear),
[openai/skills](https://github.com/openai/skills) et la
[spécification des skills d’agent](https://agentskills.io/specification). Pour
distribuer des skills que d’autres peuvent installer, privilégiez les [plugins](https://developers.openai.com/plugins/build/plugins).
