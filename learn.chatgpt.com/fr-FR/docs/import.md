<!-- source: https://learn.chatgpt.com/fr-FR/docs/import -->

Utilisez le processus d’importation pour transférer les instructions, les paramètres, les Skills, les Plugins, les projets,
ainsi que les travaux récents d’un autre agent vers l’application de bureau ChatGPT ou Codex CLI.
L’application de bureau prend en charge les importations depuis **Claude Code**, <strong>Claude Cowork</strong>
ou **Cursor**. Codex CLI prend en charge les importations depuis **Claude Code** ou **Cursor**.

L’application de bureau importe directement les éléments pris en charge et vous permet de terminer la configuration des
Plugins ou des connexions importés qui nécessitent une autorisation. Vous pouvez également maintenir
le contenu importé synchronisé grâce aux mises à jour automatiques.

L’importation ne modifie ni ne supprime la configuration existante de votre agent.

  

## Démarrer une importation

### Importer dans l’application de bureau

1. Dans l’application de bureau ChatGPT, ouvrez **Paramètres \> Importer**. Si la section **Importer** n’est pas
   encore disponible dans les paramètres, ouvrez **Général** et recherchez **Importer la
   configuration d’un autre agent**.
2. Sélectionnez **Importer**.
3. Choisissez les agents dont vous souhaitez importer le contenu, puis sélectionnez **Continuer**.
4. Sur l’écran **Sélectionner les éléments à importer**, choisissez les éléments à transférer, puis sélectionnez **Continuer**.
5. Une fois l’importation terminée, ouvrez un projet importé ou une discussion importée pour poursuivre votre travail.

### Maintenir le contenu importé synchronisé

Dans l’application de bureau ChatGPT, ouvrez **Paramètres \> Importer** et activez les mises à jour
automatiques afin de maintenir le contenu importé synchronisé avec celui de l’agent d’origine. Vous pouvez aussi
consulter l’historique de vos importations dans cette même section des paramètres.

### Importer dans Codex CLI

1. Démarrez une session locale de Codex CLI et saisissez `/import`.
2. Choisissez **Claude Code** ou **Cursor**.
3. Sélectionnez les éléments de configuration pris en charge, les fichiers de projet et les discussions récentes que vous souhaitez
importer.
4. Vérifiez la configuration importée, puis poursuivez votre travail dans Codex.

Codex CLI importe jusqu’à 50 discussions datant des 30 derniers jours. La commande `/import`
n’est pas disponible pendant qu’une tâche est en cours, dans une session à distance, ni lors d’une connexion
à un démon app-server local. Consultez les [commandes slash de la
CLI](/codex/developer-commands?surface=cli#cli-import-claude-code-or-cursor-setup-with-import).

  

## Fonctionnement de l’importation

Le processus d’importation vérifie à la fois votre configuration utilisateur et vos projets existants.
La configuration utilisateur provient de fichiers stockés sur votre machine. La configuration de projet provient
des fichiers contenus dans les dépôts et dossiers que vous sélectionnez.

Lors d’une importation, ChatGPT :

1. Détecte les éléments de configuration pris en charge et les travaux récents.
2. Importe les éléments que vous sélectionnez.
3. Conserve telle quelle la configuration existante de votre agent.
4. Vérifie si des Plugins ou des connexions importés nécessitent encore une configuration.
5. Affiche une carte d’état lorsque vous devez terminer la configuration.

## Éléments que ChatGPT peut importer

| Élément importé                     | Destination                                             |
| --------------------------------- | ------------------------------------------------------- |
| Fichiers d’instructions                 | [`AGENTS.md`](/fr-FR/codex/agent-configuration/agents-md)     |
| `settings.json`                   | [`config.toml`](/fr-FR/codex/config-file/config-basic)        |
| Skills                            | [Skills](/fr-FR/codex/build-skills)                           |
| Plugins                           | Plugins                                                 |
| Dossiers de projet existants          | Projets utilisant les mêmes dossiers                         |
| Mémoires de projet provenant de Claude Code | [Mémoires](/fr-FR/codex/customization/memories)               |
| Discussions des 30 derniers jours       | Discussions ChatGPT                                           |
| Configuration du serveur MCP          | [Configuration MCP de Codex](/fr-FR/codex/extend/mcp)            |
| Hooks                             | [Hooks de Codex](/fr-FR/codex/hooks)                             |
| Commandes slash                    | [Skills](/fr-FR/codex/build-skills)                           |
| Sous-agents                         | [Sous-agents de Codex](/fr-FR/codex/agent-configuration/subagents) |

## Finaliser la configuration après l’importation

Une fois l’importation terminée, l’application affiche une carte d’état dans le coin inférieur gauche.
Si un Plugin importé ou une connexion importée nécessite encore une configuration, la carte le signale.

Lorsque l’application signale qu’un élément nécessite votre attention, sélectionnez **Terminer** , puis suivez les
instructions pour achever la configuration.

## Éléments à vérifier après l’importation

Avant de vous fier à la configuration importée, vérifiez en particulier les éléments suivants :

- Les restrictions ou autorisations relatives aux outils dans les Skills et les agents importés.
- Les paramètres du serveur MCP faisant appel à une authentification personnalisée, à des en-têtes, à des variables
d’environnement ou à des transports. Vous devrez peut-être vous reconnecter.
- Les Hooks dont le comportement peut différer après l’importation.
- Les Plugins, les marketplaces ou les autres éléments de configuration qui nécessitent une intervention manuelle.
- Modèles de prompts ou prompts de type commande qui dépendent d’arguments, de l’interpolation du shell
ou d’espaces réservés aux chemins de fichiers.

## Après l’importation

Une fois l’importation terminée, ouvrez l’un de vos projets importés et poursuivez votre travail à partir de
là. Consultez [Utiliser ChatGPT](/fr-FR/codex/use-chatgpt) pour savoir comment démarrer votre
prochaine tâche.
