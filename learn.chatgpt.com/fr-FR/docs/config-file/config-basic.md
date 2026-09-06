<!-- source: https://learn.chatgpt.com/fr-FR/docs/config-file/config-basic -->

Codex lit les informations de configuration à plusieurs emplacements. Vos paramètres personnels par défaut sont stockés dans `~/.codex/config.toml`, et vous pouvez les remplacer au niveau d’un projet à l’aide de fichiers `.codex/config.toml`. Par mesure de sécurité, Codex ne charge les couches `.codex/` propres à un projet que si vous avez déclaré ce projet fiable.

## Fichier de configuration de Codex

Codex stocke la configuration utilisateur dans `~/.codex/config.toml`. Pour limiter certains paramètres à un projet ou à un sous-dossier spécifique, ajoutez un fichier `.codex/config.toml` dans votre dépôt.

Pour ouvrir le fichier de configuration depuis l’extension IDE Codex, sélectionnez l’icône d’engrenage en haut à droite, puis **Paramètres Codex \> Ouvrir config.toml**.

La CLI et l’extension IDE partagent les mêmes couches de configuration. Utilisez-les pour les opérations suivantes :

- Définissez le modèle et le fournisseur par défaut.
- Configurez [les politiques d’approbation et les paramètres du bac à sable](/fr-FR/codex/agent-approvals-security#sandbox-and-approvals).
- Configurez [les serveurs MCP](/fr-FR/codex/extend/mcp).

## Ordre de priorité de la configuration

Codex détermine les valeurs dans l’ordre suivant (de la priorité la plus élevée à la plus faible) :

1. Options de la CLI et remplacements via `--config`
2. Fichiers de configuration du projet : `.codex/config.toml`, appliqués dans l’ordre de la racine du projet jusqu’au répertoire de travail actuel (le plus proche prévaut ; projets déclarés fiables uniquement)
3. Fichiers de [profil](/fr-FR/codex/config-file/config-advanced#profiles) sélectionnés avec `--profile profile-name` (`~/.codex/profile-name.config.toml`)
4. Configuration utilisateur : `~/.codex/config.toml`
5. Configuration système (si elle existe) : `/etc/codex/config.toml` sous Unix
6. Valeurs par défaut intégrées

Utilisez cet ordre de priorité pour définir les valeurs par défaut communes dans `config.toml` et réservez les [fichiers de profil](/fr-FR/codex/config-file/config-advanced#profiles) aux valeurs qui diffèrent.

Si vous marquez un projet comme non fiable, Codex ignore les couches `.codex/` propres à ce projet, notamment sa configuration locale, ses hooks et ses règles. Les configurations utilisateur et système sont tout de même chargées, y compris les hooks et les règles définis au niveau utilisateur ou global.

Pour les remplacements ponctuels via `-c`/`--config` (y compris les règles d’utilisation des guillemets en TOML), consultez [Configuration avancée](/fr-FR/codex/config-file/config-advanced#one-off-overrides-from-the-cli).

  Sur les machines gérées, votre organisation peut également imposer des contraintes via
`requirements.toml` (par exemple, interdire `approval_policy = "never"` ou
`sandbox_mode = "danger-full-access"`). Consultez [Configuration
  gérée](/fr-FR/codex/enterprise/managed-configuration) et [Exigences imposées
  par l’administrateur](/fr-FR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

## Options de configuration courantes

Voici quelques-unes des options les plus souvent modifiées :

#### Modèle par défaut

Choisissez le modèle que Codex utilise par défaut dans la CLI et l’IDE.

#### Demandes d’approbation

Déterminez quand Codex doit s’interrompre pour demander votre approbation avant d’exécuter les commandes générées.

```toml
approval_policy = "on-request"

Pour connaître les différences de comportement entre `untrusted`, `on-request` et `never`, consultez [Exécution sans demande d’approbation](/fr-FR/codex/agent-approvals-security#run-without-approval-prompts) et [Combinaisons courantes de bac à sable et d’approbation](/fr-FR/codex/agent-approvals-security#common-sandbox-and-approval-combinations).

#### Niveau du bac à sable

Définissez le niveau d’accès de Codex au système de fichiers et au réseau pendant l’exécution des commandes.

```toml
sandbox_mode = "workspace-write"

Pour connaître le comportement propre à chaque mode (notamment les chemins `.git`/`.codex` protégés et les paramètres réseau par défaut), consultez [Bac à sable et approbations](/fr-FR/codex/agent-approvals-security#sandbox-and-approvals), [Chemins protégés dans les racines accessibles en écriture](/fr-FR/codex/agent-approvals-security#protected-paths-in-writable-roots) et [Accès réseau](/fr-FR/codex/agent-approvals-security#network-access).

#### Profils d’autorisation

Codex prend également en charge des profils d’autorisation nommés qui permettent de réutiliser les politiques d’accès au système de fichiers et
au réseau. Les profils intégrés sont `:read-only`, `:workspace` et
`:danger-full-access`. Les profils personnalisés utilisent des tables `[permissions.<name>]` et une
valeur `default_permissions` correspondante. Consultez [Autorisations](/fr-FR/codex/permissions).

#### Mode du bac à sable Windows

Lorsque vous exécutez Codex de façon native sur Windows, définissez le mode natif du bac à sable sur `elevated` dans la table `windows`. N’utilisez `unelevated` que si vous ne disposez pas des droits d’administrateur ou si la configuration avec élévation de privilèges échoue.

```toml
[windows]
sandbox = "elevated"   # Recommended
# sandbox = "unelevated" # Fallback if admin permissions/setup are unavailable

#### Mode de recherche web

Codex active la recherche web par défaut pour les discussions locales et fournit des résultats issus d’un cache de recherche web. Ce cache est un index de résultats web géré par OpenAI. Le mode avec cache renvoie donc des résultats préindexés au lieu de récupérer les pages en direct. Cela réduit l’exposition aux attaques par injection de prompt provenant de contenus quelconques récupérés en direct, mais vous devez tout de même considérer les résultats web comme non fiables. Si vous utilisez `--yolo` ou un autre [paramètre de bac à sable avec accès complet](/fr-FR/codex/agent-approvals-security#common-sandbox-and-approval-combinations), la recherche web renvoie par défaut des résultats en direct. Choisissez un mode avec `web_search` :

- `"cached"` (par défaut) renvoie les résultats du cache de recherche web.
- `"indexed"` n’autorise l’accès web externe que lorsque l’index de recherche valide la requête.
- `"live"` récupère les données les plus récentes sur le web (comme `--search`).
- `"disabled"` désactive l’outil de recherche web.

```toml
web_search = "cached"  # default; serves results from the web search cache
# web_search = "indexed" # gate external web access through the search index
# web_search = "live"  # fetch the most recent data from the web (same as --search)
# web_search = "disabled"

#### Effort de raisonnement

Réglez l’effort que le modèle consacre au raisonnement lorsque cette option est prise en charge.

```toml
model_reasoning_effort = "high"

#### Style de communication

Définissez un style de communication par défaut pour les modèles compatibles.

```toml
personality = "friendly" # or "pragmatic" or "none"

Vous pouvez ensuite modifier ce paramètre dans une session active avec `/personality`, ou pour chaque fil de discussion ou tour de conversation lorsque vous utilisez les API App Server.

#### Raccourcis clavier de la TUI

Personnalisez les raccourcis clavier du terminal dans `tui.keymap`. Pour certaines actions de la zone de saisie, les raccourcis correspondants définis dans `tui.keymap.global` sont utilisés à défaut ; les raccourcis propres au contexte sont prioritaires lorsqu’ils sont pris en charge. Une liste vide supprime les raccourcis associés à l’action.

```toml
[tui.keymap.global]
open_transcript = "ctrl-t"

[tui.keymap.composer]
submit = ["enter", "ctrl-m"]

[tui.keymap.chat]
interrupt_turn = "f12"

#### Environnement des commandes

Contrôlez les variables d’environnement que Codex transmet aux commandes qu’il lance. Utilisez
des filtres par clé pour ne conserver que les variables dont vous avez besoin :

```toml
[shell_environment_policy]
ignore_default_excludes = false

[shell_environment_policy.filters]
"PATH" = "include"
"HOME" = "include"

`ignore_default_excludes` vaut `true` par défaut, ce qui désactive le filtrage automatique
des noms de variables contenant `KEY`, `SECRET` ou `TOKEN`. Définissez cette option sur `false`
pour activer ce filtrage automatique. Pour les règles d’exclusion, l’ordre de priorité et
l’ancien format de configuration, consultez [Politique d’environnement
du shell](/fr-FR/codex/config-file/config-advanced#shell-environment-policy).

#### Répertoire des journaux

Modifiez le répertoire dans lequel Codex écrit ses fichiers journaux locaux. Définir explicitement `log_dir`
active également le journal TUI facultatif en texte brut, `codex-tui.log`, dans ce répertoire.

```toml
log_dir = "/absolute/path/to/codex-logs"

Pour les exécutions ponctuelles, vous pouvez également le définir depuis la CLI :

```bash
codex -c log_dir=./.codex-log

## Indicateurs de fonctionnalité

Utilisez la table `[features]` dans `config.toml` pour activer ou désactiver les fonctionnalités facultatives et expérimentales.

### Indicateurs de fonctionnalité courants

| Clé                  |        Valeur par défaut        | Maturité     | Description                                                                              |
| -------------------- | :-------------------: | ------------ | ---------------------------------------------------------------------------------------- |
| `apps`               |         true          | Stable       | Activez les intégrations d’applications (connecteurs)                                                      |
| `goals`              |         true          | Stable       | Activez la persistance des objectifs et la poursuite automatique                                        |
| `hooks`              |         true          | Stable       | Activez les hooks de cycle de vie à partir de `hooks.json` ou directement dans `[hooks]`. Consultez [Hooks](/fr-FR/codex/hooks). |
| `fast_mode`          |         true          | Stable       | Activez la sélection du mode Rapide et l’utilisation de `service_tier = "fast"`                          |
| `memories`           |         false         | Expérimental | Activez les [Mémoires](/fr-FR/codex/customization/memories)                                         |
| `multi_agent`        |         true          | Stable       | Activez les outils de collaboration entre sous-agents                                                      |
| `personality`        |         true          | Stable       | Activez les commandes de sélection de la personnalité                                                    |
| `remote_plugin`      |         true          | Stable       | Activez le catalogue distant de plugins                                                         |
| `shell_snapshot`     |         true          | Stable       | Créez un instantané de votre environnement shell pour accélérer l’exécution des commandes répétées                            |
| `shell_tool`         |         true          | Stable       | Activez l’outil `shell` par défaut                                                          |
| `unified_exec`       | `true`, sauf sur Windows | Stable       | Utilisez l’outil exec unifié reposant sur un PTY                                                     |
| `web_search`         |         true          | Obsolète   | Ancienne option d’activation ; privilégiez le paramètre `web_search` de premier niveau                                 |
| `web_search_cached`  |         false         | Obsolète   | Ancienne option d’activation correspondant à `web_search = "cached"` lorsque ce paramètre n’est pas défini                            |
| `web_search_request` |         false         | Obsolète   | Ancienne option d’activation correspondant à `web_search = "live"` lorsque ce paramètre n’est pas défini                              |

  Ce tableau présente les options courantes destinées aux utilisateurs, et non l’ensemble des fonctionnalités internes ou
  en cours de développement. La colonne Maturité utilise des libellés tels que
  Expérimental, Bêta et Stable. Consultez [Maturité des
  fonctionnalités](/fr-FR/codex/feature-maturity) pour savoir comment interpréter ces libellés.

Omettez les clés des fonctionnalités pour conserver leurs valeurs par défaut.

Pour configurer les hooks de cycle de vie, consultez [Hooks](/fr-FR/codex/hooks).

### Activation des fonctionnalités

- Dans `config.toml`, ajoutez `feature_name = true` à la section `[features]`.
- Depuis la CLI, exécutez `codex --enable feature_name`.
- Pour activer plusieurs fonctionnalités, exécutez `codex --enable feature_a --enable feature_b`.
- Pour désactiver une fonctionnalité, attribuez la valeur `false` à sa clé dans `config.toml`.
