<!-- source: https://learn.chatgpt.com/fr-FR/docs/agent-configuration/agents-md -->

Codex lit les fichiers `AGENTS.md` avant de commencer toute tâche. En superposant des consignes globales et des instructions prioritaires propres au projet, vous pouvez démarrer chaque tâche avec des attentes cohérentes, quel que soit le dépôt que vous ouvrez.

## Comment Codex détecte les instructions

Au démarrage, Codex crée une chaîne d’instructions (une fois par exécution ; dans la TUI, cela correspond généralement à une fois par session lancée). La détection respecte l’ordre de priorité suivant :

1. **Portée globale :** Dans le répertoire d’accueil de Codex (`~/.codex` par défaut, sauf si vous définissez `CODEX_HOME`), Codex lit `AGENTS.override.md` s’il existe. Sinon, Codex lit `AGENTS.md`. Codex ne prend en compte que le premier fichier non vide à ce niveau.
2. **Portée du projet :** À partir de la racine du projet (généralement la racine Git), Codex descend dans l’arborescence jusqu’à votre répertoire de travail actuel. Si Codex ne trouve pas de racine de projet, il vérifie uniquement le répertoire actuel. Dans chaque répertoire du chemin, il recherche `AGENTS.override.md`, puis `AGENTS.md`, puis les éventuels noms alternatifs définis dans `project_doc_fallback_filenames`. Codex inclut au maximum un fichier par répertoire.
3. **Ordre de fusion :** Codex concatène les fichiers de la racine vers le bas de l’arborescence en les séparant par des lignes vides. Les fichiers les plus proches de votre répertoire actuel prennent le pas sur les consignes précédentes, car ils apparaissent plus tard dans le prompt fusionné.

Codex ignore les fichiers vides et cesse d’en ajouter dès que leur taille cumulée atteint la limite définie par `project_doc_max_bytes` (32 KiB par défaut). Pour en savoir plus sur ces paramètres, consultez [Détection des instructions de projet](/fr-FR/codex/config-file/config-advanced#project-instructions-discovery). Augmentez la limite ou répartissez les instructions entre plusieurs répertoires imbriqués lorsque vous l’atteignez.

## Créez des consignes globales

Définissez des valeurs par défaut persistantes dans le répertoire d’accueil de Codex afin que chaque dépôt hérite de vos conventions de travail.

1. Vérifiez que le répertoire existe :

   ```bash
   mkdir -p ~/.codex

2. Créez `~/.codex/AGENTS.md` et ajoutez-y des préférences réutilisables :

   ```md
   # ~/.codex/AGENTS.md

   ## Working agreements

   - Always run `npm test` after modifying JavaScript files.
   - Prefer `pnpm` when installing dependencies.
   - Ask for confirmation before adding new production dependencies.

3. Exécutez Codex depuis n’importe quel répertoire pour vérifier qu’il charge le fichier :

   ```bash
   codex --ask-for-approval never "Summarize the current instructions."

   Résultat attendu : Codex cite les éléments de `~/.codex/AGENTS.md` avant de proposer des modifications.

Utilisez `~/.codex/AGENTS.override.md` pour appliquer temporairement un remplacement global sans supprimer le fichier de base. Supprimez le fichier de remplacement pour rétablir les consignes partagées.

## Ajoutez une couche d’instructions propres au projet

Les fichiers placés au niveau du dépôt permettent à Codex de tenir compte des conventions du projet tout en héritant de vos valeurs par défaut globales.

1. À la racine de votre dépôt, ajoutez un fichier `AGENTS.md` qui décrit la configuration de base :

   ```md
   # AGENTS.md

   ## Repository expectations

   - Run `npm run lint` before opening a pull request.
   - Document public utilities in `docs/` when you change behavior.

2. Ajoutez des fichiers de remplacement dans les répertoires imbriqués lorsque certaines équipes ont besoin de règles différentes. Par exemple, dans `services/payments/`, créez `AGENTS.override.md` :

   ```md
   # services/payments/AGENTS.override.md

   ## Payments service rules

   - Use `make test-payments` instead of `npm test`.
   - Never rotate API keys without notifying the security channel.

3. Démarrez Codex depuis le répertoire des paiements :

   ```bash
   codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."

   Résultat attendu : Codex indique d’abord le fichier global, puis le fichier `AGENTS.md` à la racine du dépôt, et enfin le fichier de remplacement propre au service de paiement.

Codex cesse sa recherche lorsqu’il atteint votre répertoire actuel. Placez donc chaque fichier de remplacement au plus près des tâches spécialisées auxquelles il s’applique.

Voici un exemple de dépôt après l’ajout d’un fichier global et d’un fichier de remplacement propre au service de paiement :

## Ajoutez des règles de revue de code

Pour la [revue de code par Codex dans GitHub](/fr-FR/codex/third-party/github#customize-what-codex-reviews),
ajoutez une section `## Code Review Rules` au fichier `AGENTS.md` le plus proche du code auquel les
règles s’appliquent. Placez à la racine les contrôles portant sur l’ensemble du dépôt et, dans un fichier imbriqué, les
contrôles propres à un service.

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

Rédigez des règles concises, décrivez le comportement à signaler ainsi que toute solution sûre ou
exception, et réservez les contrôles de formatage et de lint à la CI. Consultez [Personnaliser ce que
Codex examine](/fr-FR/codex/third-party/github#customize-what-codex-reviews) pour
savoir comment configurer et rédiger les règles.

## Personnalisez les noms de fichiers alternatifs

Si votre dépôt utilise déjà un autre nom de fichier (par exemple `TEAM_GUIDE.md`), ajoutez-le à la liste des noms alternatifs afin que Codex le traite comme un fichier d’instructions.

1. Modifiez la configuration de Codex :

   ```toml
   # ~/.codex/config.toml
   project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
   project_doc_max_bytes = 65536

2. Redémarrez Codex ou exécutez une nouvelle commande afin que la configuration mise à jour soit chargée.

Codex recherche désormais les fichiers dans chaque répertoire dans l’ordre suivant : `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`. Les noms de fichiers absents de cette liste sont ignorés lors de la détection des instructions. La limite en octets plus élevée permet de combiner davantage de consignes avant qu’elles ne soient tronquées.

Une fois la liste des noms alternatifs configurée, Codex traite les fichiers alternatifs comme des fichiers d’instructions :

Définissez la variable d’environnement `CODEX_HOME` lorsque vous souhaitez utiliser un autre profil, par exemple pour un utilisateur d’automatisation propre à un projet :

```bash
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"

Résultat attendu : la sortie répertorie les fichiers avec des chemins relatifs au répertoire `.codex` personnalisé.

## Vérifiez votre configuration

- Exécutez `codex --ask-for-approval never "Summarize the current instructions."` depuis la racine d’un dépôt. Codex doit afficher les consignes des fichiers globaux et des fichiers de projet dans l’ordre de priorité.
- Utilisez `codex --cd subdir --ask-for-approval never "Show which instruction files are active."` pour vérifier que les remplacements imbriqués remplacent les règles plus générales.
- Pour vérifier quels fichiers d’instructions Codex a chargés, activez un journal TUI en texte brut avec `codex -c log_dir=./.codex-log` et consultez `./.codex-log/codex-tui.log`, ou examinez le fichier `session-*.jsonl` le plus récent si vous avez activé la journalisation des sessions.
- Si les instructions semblent obsolètes, redémarrez Codex dans le répertoire cible. Codex reconstruit la chaîne d’instructions à chaque exécution (et au début de chaque session TUI) ; aucun cache ne doit donc être vidé manuellement.

## Résolvez les problèmes de détection des instructions

- **Rien ne se charge :** Vérifiez que vous vous trouvez dans le dépôt voulu et que `codex status` indique la racine de l’espace de travail attendue. Assurez-vous que les fichiers d’instructions ne sont pas vides ; Codex ignore les fichiers vides.
- **Des consignes incorrectes s’affichent :** Recherchez un fichier `AGENTS.override.md` plus haut dans l’arborescence ou dans le répertoire d’accueil de Codex. Renommez ou supprimez ce fichier de remplacement pour revenir au fichier standard.
- **Codex ignore les noms de fichiers alternatifs :** Vérifiez que vous avez indiqué les noms dans `project_doc_fallback_filenames` sans faute de frappe, puis redémarrez Codex afin que la configuration mise à jour prenne effet.
- **Instructions tronquées :** Augmentez la valeur de `project_doc_max_bytes` ou répartissez le contenu des fichiers volumineux entre des répertoires imbriqués pour que les consignes essentielles restent intactes.
- **Confusion entre les profils :** Exécutez `echo $CODEX_HOME` avant de lancer Codex. Si la valeur n’est pas celle par défaut, Codex utilise un autre répertoire d’accueil que celui que vous avez modifié.

## Étapes suivantes

- Pour plus d’informations, consultez le site officiel [AGENTS.md](https://agents.md).
- Consultez [Conception de prompts pour Codex](/fr-FR/codex/prompting) pour découvrir des modes de dialogue adaptés aux consignes persistantes.
