<!-- source: https://learn.chatgpt.com/fr-FR/docs/enterprise/plugin-management -->

## Avant de commencer

Les administrateurs de l’espace de travail peuvent importer une marketplace de plugins depuis GitHub et maintenir ses plugins à jour à partir du dépôt. Une marketplace est un catalogue JSON qui répertorie les plugins à importer.

Utilisez un compte GitHub disposant d’un accès en lecture au dépôt de la marketplace et à tous les autres dépôts référencés. Les dépôts GitHub publics et privés sont pris en charge. Avant l’importation, obtenez toutes les approbations de l’organisation GitHub requises pour accéder au dépôt.

Examinez le contenu du dépôt avant l’importation. Pour les nouveaux plugins, la politique d’installation est définie sur **Disponible** et l’authentification est demandée à l’installation. La synchronisation automatique quotidienne est activée pour les nouvelles marketplaces. L’importation traite toutes les entrées valides, et les synchronisations ultérieures ajoutent automatiquement tous les nouveaux plugins du dépôt.

## Configurez la synchronisation d’une marketplace

1. Ouvrez **Administration** \> **Plugins** et sélectionnez **Ajouter** \> **Importer une marketplace**.
2. Dans **Source**, saisissez l’URL du dépôt, par exemple `https://github.com/example/team-plugins`. Utilisez uniquement l’URL du dépôt, et non celle d’une branche ou d’un dossier.
3. Si la marketplace se trouve dans un sous-répertoire, saisissez ce répertoire dans **Chemin**. Par exemple, utilisez `team-tools` pour `team-tools/.agents/plugins/marketplace.json`. Laissez **Chemin** vide pour utiliser la racine du dépôt. Ne saisissez pas le nom du fichier manifeste.
4. Vous pouvez renseigner le champ **Branche, tag ou commit**. Laissez-le vide pour utiliser la branche par défaut du dépôt. Utilisez une branche pour recevoir les futurs commits ; si vous indiquez un commit précis, la révision reste figée.
5. Sélectionnez **Importer une marketplace** et autorisez l’accès à GitHub lorsque vous y êtes invité. L’importation initiale peut prendre jusqu’à une heure pour les très grandes marketplaces. Les synchronisations quotidiennes suivantes prennent généralement quelques minutes.
6. Consultez les **Résultats de l’importation**, puis ouvrez chaque plugin importé pour configurer sa politique d’installation et les éventuelles applications requises.

Pour demander une mise à jour sans attendre la synchronisation quotidienne, ouvrez la marketplace dans **Administration** \> **Plugins** \> **Marketplaces** et sélectionnez **Synchroniser maintenant**.

## Formats pris en charge

Le répertoire sélectionné doit contenir l’un de ces fichiers :

| Fichier                               | Format                                                               |
| ---------------------------------- | -------------------------------------------------------------------- |
| `.agents/plugins/marketplace.json` | Une marketplace Codex avec un tableau `plugins`.                          |
| `.claude-plugin/marketplace.json`  | Une marketplace compatible avec Claude avec un tableau `plugins`.              |
| `.claude-plugin/plugin.json`       | Un plugin Claude autonome, en l’absence de manifeste de marketplace. |

Dans une marketplace, les entrées peuvent référencer des plugins natifs avec `.codex-plugin/plugin.json`, des plugins compatibles avec Claude, des packages Agent Plugins 1.0 ou des packages de skills pris en charge.

Pour une marketplace Codex, utilisez des chemins locaux pour les plugins situés dans le même dépôt :

```json
{
  "name": "team-plugins",
  "interface": {
    "displayName": "Team plugins"
  },
  "plugins": [
    {
      "name": "team-tools",
      "source": {
        "source": "local",
        "path": "./plugins/team-tools"
      }
    }
  ]
}

Le chemin est relatif à la racine de la marketplace sélectionnée, et non à `.agents/plugins/`.

Une marketplace compatible avec Claude peut utiliser une chaîne de caractères indiquant le chemin de chaque plugin local :

```json
{
  "name": "team-plugins",
  "plugins": [
    {
      "name": "team-tools",
      "source": "./plugins/team-tools"
    }
  ]
}

Les entrées d’une marketplace Codex prennent également en charge `source: "url"` pour un plugin à la racine d’un dépôt GitHub et `source: "git-subdir"` pour un plugin dans un sous-répertoire GitHub. Par exemple :

```json
{
  "name": "team-tools",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/example/team-tools.git",
    "path": "./plugins/team-tools",
    "ref": "main"
  }
}

Les sources Git permettent de sélectionner une `ref` ou le `sha` complet d’un commit, composé de 40 caractères. Le compte GitHub qui autorise l’accès doit disposer d’un accès en lecture à chaque dépôt référencé. L’importation dans l’espace de travail ne prend actuellement en charge que les dépôts GitHub.

## Configurez l’accès dans l’espace de travail

L’importation et la synchronisation depuis GitHub n’appliquent pas les politiques d’installation ou d’authentification du dépôt, notamment `AVAILABLE`, `INSTALLED_BY_DEFAULT`, `NOT_AVAILABLE`, `ON_INSTALL` et `ON_USE`. Les administrateurs de l’espace de travail configurent ces paramètres pour chaque plugin. La synchronisation d’une mise à jour ou le passage d’un plugin existant à une gestion via GitHub conserve les politiques qui lui sont appliquées dans l’espace de travail.

Dans **Politique d’installation** , choisissez **Disponible** ou **Installé** pour chaque rôle éligible. Les applications requises doivent également être activées, et les membres doivent avoir accès au service connecté. L’importation d’un plugin n’accorde pas l’accès aux applications et ne connecte pas les comptes des membres. Consultez [Contrôles des plugins](/fr-FR/codex/enterprise/apps-and-connectors) pour connaître les contrôles des rôles, des applications et des actions.

## Passez à la gestion via GitHub pour un plugin existant

Ajoutez `pluginId` à l’entrée du plugin existant dans la marketplace :

```json
{
  "name": "team-tools",
  "pluginId": "plugin_0123456789abcdef0123456789abcdef",
  "source": {
    "source": "local",
    "path": "./plugins/team-tools"
  }
}

Ouvrez le plugin depuis **Administration** \> **Plugins** et copiez l’identifiant situé après `/admin/plugins/` dans son URL. Placez `pluginId` à côté de `name` et de `source` dans l’entrée de la marketplace. Le plugin existant doit se trouver dans le même espace de travail.

Cette opération fait passer à une gestion via GitHub un plugin de l’espace de travail qui a été téléversé ou qui n’était pas encore géré. Le plugin conserve son identifiant, ses paramètres de partage et ses politiques dans l’espace de travail. Les futures mises à jour proviennent de GitHub ; le téléversement d’archives ne permet plus de remplacer le plugin géré. Cette méthode ne permet pas de reprendre la gestion d’un plugin déjà géré par une autre source GitHub.

## Plugins réservés à l’application de bureau

Tout plugin importé qui déclare des serveurs MCP dans `mcp.json` ou `.mcp.json` porte la mention **Application de bureau uniquement** et ne fonctionne que dans l’application de bureau ChatGPT. Cela inclut les serveurs qui utilisent une URL HTTPS distante. La même restriction s’applique aux autres formes de configuration MCP prises en charge, telles que les déclarations de serveurs intégrées.

## Référencez une application existante avec `.app.json`

Ajoutez `.app.json` à la racine du plugin. Le nom du fichier commence par un point ; `app.json`, sans le point, n’est pas pris en charge.

```json
{
  "apps": {
    "team-tools": {
      "id": "asdk_app_example",
      "required": true
    }
  }
}

Remplacez `asdk_app_example` par l’identifiant de l’application existante. Les identifiants d’application pris en charge commencent par `asdk_app_`, `connector_` ou `templated_apps_`. Utilisez l’identifiant de l’application, et non un identifiant `plugin_...`. Par exemple, une URL de plugin contenant `plugin_asdk_app_example` correspond à l’application `asdk_app_example`.

La clé `team-tools` donne un nom à la référence dans ce fichier. Définissez `required` sur `true` lorsque le plugin dépend de l’application. Vous pouvez ajouter d’autres entrées pour référencer d’autres applications existantes.

Pour un plugin natif, définissez `apps` sur `./.app.json` dans `.codex-plugin/plugin.json`. Voici un manifeste complet pour cet exemple :

```json
{
  "name": "team-tools",
  "version": "1.0.0",
  "description": "Use the team's approved tools.",
  "author": {
    "name": "Example team"
  },
  "apps": "./.app.json",
  "interface": {
    "displayName": "Team tools",
    "shortDescription": "Use approved team tools",
    "longDescription": "Connect to the team's existing app.",
    "developerName": "Example team",
    "category": "Productivity",
    "capabilities": ["Read"]
  }
}

Respectez cette arborescence de fichiers :

```text
team-plugins/
├── .agents/plugins/marketplace.json
└── plugins/team-tools/
    ├── .codex-plugin/plugin.json
    └── .app.json

Cette référence ne crée pas d’application et n’accorde aucune autorisation. Les administrateurs doivent rendre l’application disponible pour les rôles visés, et les membres doivent effectuer toute authentification requise. Les autorisations existantes de l’application, les contrôles des actions et les conditions d’accès au service continuent de s’appliquer.

## Maintenez les plugins à jour

Les nouvelles marketplaces recherchent les mises à jour quotidiennement. Ouvrez **Administration** \> **Plugins** \> **Marketplaces**, sélectionnez la marketplace, puis choisissez **Synchroniser maintenant** pour demander une mise à jour sans attendre la synchronisation automatique.

La synchronisation peut ajouter de nouvelles entrées de marketplace et mettre à jour les plugins existants. Examinez les modifications du dépôt avant de les fusionner, car la synchronisation automatique importera tous les nouveaux plugins.

Après une synchronisation, consultez son état et le rapport enregistré. **Terminé — N erreurs** signifie que le traitement est terminé, mais que certains plugins n’ont pas pu être traités. Si la mise à jour d’un plugin existant n’est pas valide, sa dernière version fonctionnelle est conservée. Corrigez le problème signalé dans GitHub, puis sélectionnez **Synchroniser maintenant** pour réessayer.

La suppression d’une entrée du dépôt ne supprime pas sa copie importée dans l’espace de travail. Elle porte alors la mention **N’est plus dans la source**. La suppression de la marketplace dans ChatGPT supprime tous les plugins importés depuis celle-ci.

## Rétablissez ou modifiez l’accès à GitHub

Pour **rétablir l’accès à GitHub**, vérifiez d’abord que le compte GitHub utilisé pour l’importation a toujours accès au dépôt et à tous les dépôts référencés. L’administrateur qui a initialement importé la marketplace devrait ensuite ouvrir le plugin GitHub dans ChatGPT et reconnecter son compte, car la synchronisation de la marketplace utilise sa connexion GitHub.

Pour **transférer la marketplace à un nouveau propriétaire**, le nouvel administrateur de l’espace de travail devrait ouvrir **Administration** \> **Plugins** \> **Ajouter** \> **Importer une marketplace** et importer la même marketplace en utilisant les mêmes valeurs pour **Source**, **Chemin** et **Branche, tag ou commit** . Les futures synchronisations utiliseront sa connexion GitHub.

Ne supprimez pas la marketplace dans le seul but de la reconnecter ou d’en changer le propriétaire : cette opération supprime également les plugins importés depuis celle-ci.
