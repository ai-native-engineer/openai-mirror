<!-- source: https://learn.chatgpt.com/fr-FR/docs/config-file/environment-variables -->

Codex utilise `config.toml` pour les paramètres persistants. Utilisez les variables d’environnement pour
surcharger des paramètres à l’échelle du shell, fournir des secrets d’automatisation, contrôler le comportement du programme d’installation ou effectuer des diagnostics.

Cette page répertorie les variables d’environnement publiques stables que Codex lit directement.
Elle ne répertorie pas les variables de développement internes, les variables de test ni
les noms de secrets propres à un fournisseur que vous choisissez vous-même avec
[`env_key`](/fr-FR/codex/config-file/config-advanced#custom-model-providers).

## Emplacements principaux

| Variable            | Utilisée par                                    | Valeur par défaut      | Description                                                                                                                                                      |
| ------------------- | ------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_HOME`        | CLI, extension IDE, app-server et programmes d’installation | `~/.codex`   | Définit le répertoire racine des données d’état de Codex, notamment la configuration, l’authentification, les journaux, les sessions, les Skills et les métadonnées du package autonome. Si vous définissez cette variable, le répertoire doit déjà exister. |
| `CODEX_SQLITE_HOME` | Données d’état de la CLI et d’app-server                   | `CODEX_HOME` | Définit l’emplacement de stockage des données d’état gérées par SQLite. L’option de configuration `sqlite_home` est prioritaire. Les chemins relatifs sont résolus à partir du répertoire de travail courant.           |

Pour en savoir plus sur les fichiers stockés sous `CODEX_HOME`, consultez
[Emplacements de la configuration et des données d’état](/fr-FR/codex/config-file/config-advanced#config-and-state-locations).

## Variables du programme d’installation

Ces variables s’appliquent aux scripts d’installation autonomes disponibles aux adresses
`https://chatgpt.com/codex/install.sh` et
`https://chatgpt.com/codex/install.ps1`.

| Variable                | Valeur par défaut                                                                              | Description                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_NON_INTERACTIVE` | `false`                                                                              | Définissez la variable sur `1`, `true` ou `yes` pour ignorer les invites du programme d’installation. La réponse par défaut est alors utilisée pour chaque invite ; réservez donc ce réglage aux installations et mises à jour effectuées par script, et non à la configuration lors de la première exécution. |
| `CODEX_INSTALL_DIR`     | `~/.local/bin` sur macOS/Linux ; `%LOCALAPPDATA%\Programs\OpenAI\Codex\bin` sur Windows | Modifie l’emplacement d’installation de la commande `codex` disponible pour l’utilisateur. Le cache du package autonome reste stocké sous `CODEX_HOME/packages/standalone`.                        |

Pour les installations sans intervention, définissez `CODEX_NON_INTERACTIVE=1` dans le shell qui exécute
le programme d’installation téléchargé :

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh

```powershell
$env:CODEX_NON_INTERACTIVE=1; irm https://chatgpt.com/codex/install.ps1 | iex

## Authentification et réseau

| Variable                           | Utilisée par                                          | Description                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_API_KEY`                    | Exec, review, SDK TypeScript et exec-server distant | Fournit une clé API à un processus Codex non interactif. Définissez-la directement sur la ligne de commande plutôt que pour l’ensemble de la tâche lorsque vous exécutez du code contrôlé par le dépôt.             |
| `CODEX_ACCESS_TOKEN`               | CLI, app-server et automatisations de confiance              | Fournit un jeton d’accès ChatGPT ou Codex pour les automatisations de confiance. Pour une connexion persistante, transmettez-le à `codex login --with-access-token` via un pipe.             |
| `OPENAI_FEDERATION_RULE_ID`        | Identité de charge de travail                                | Sélectionne la règle de fédération configurée pour la charge de travail.                                                                                        |
| `OPENAI_IDENTITY_TOKEN_FILE`       | Identité de charge de travail                                | Indique le chemin absolu du fichier contenant le token OIDC actuel ou le SPIFFE JWT-SVID.                                                |
| `OPENAI_WORKLOAD_IDENTITY_CONTEXT` | Identité de charge de travail                                | Fournit éventuellement des identifiants JSON de taille limitée pour renseigner, à des fins d’audit, les informations d’attribution déclarées par le client. Cela n’a aucune incidence sur l’authentification ni sur l’autorisation.         |
| `CODEX_CA_CERTIFICATE`             | Clients HTTPS, de connexion et WebSocket              | Indique le chemin d’un bundle d’autorités de certification au format PEM pour les environnements utilisant une interception TLS d’entreprise ou des certificats racines privés. Cette variable est prioritaire sur `SSL_CERT_FILE`. |
| `SSL_CERT_FILE`                    | Clients HTTPS, de connexion et WebSocket              | Chemin de repli vers un bundle d’autorités de certification au format PEM lorsque `CODEX_CA_CERTIFICATE` n’est pas défini.                                                                               |

Pour les clés API des fournisseurs, définissez
[`env_key`](/fr-FR/codex/config-file/config-advanced#custom-model-providers) dans la configuration du fournisseur de
modèles. Codex lit la variable désignée par ce paramètre ; le nom de cette variable
n’est donc pas celui d’une variable d’environnement Codex prédéfinie.

Pour la gestion des secrets d’automatisation, consultez
[Utiliser l’authentification par clé API](/fr-FR/codex/non-interactive-mode#use-api-key-auth).
Pour configurer les jetons d’accès, consultez [Jetons d’accès](/fr-FR/codex/enterprise/access-tokens).
Pour configurer l’identité de charge de travail, consultez
[Fédération d’identité de charge de travail](/fr-FR/codex/enterprise/workload-identity).

## Diagnostics

| Variable   | Utilisée par            | Description                                                                                                             |
| ---------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `RUST_LOG` | CLI et app-server | Contrôle le filtrage et la verbosité des journaux Rust. Par défaut, `codex exec` produit uniquement une sortie de niveau `error`, sauf si vous définissez une valeur plus verbeuse. |

`RUST_LOG` accepte des valeurs telles que `error`, `warn`, `info`, `debug` et
`trace`. Il accepte également des filtres de journalisation Rust plus ciblés, comme
`codex_core=debug,codex_tui=debug`.

La CLI interactive enregistre par défaut les diagnostics dans des espaces de stockage locaux de taille limitée, mais
la création du fichier en texte brut `codex-tui.log` doit être activée explicitement. Définissez `log_dir` explicitement lorsque vous
avez besoin d’un journal en texte brut pour le dépannage :

```bash
RUST_LOG=debug codex -c log_dir=./.codex-log
tail -F ./.codex-log/codex-tui.log

En mode non interactif, `codex exec` affiche les messages directement au lieu de les écrire
dans un fichier journal TUI distinct.
