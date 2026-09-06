<!-- source: https://learn.chatgpt.com/fr-FR/docs/custom-prompts -->

Les prompts personnalisés sont obsolètes. Utilisez les [Skills](/fr-FR/codex/build-skills) pour créer des
  instructions réutilisables que Codex peut invoquer explicitement ou implicitement.

Les prompts personnalisés (obsolètes) vous permettent de transformer des fichiers Markdown en prompts réutilisables que vous pouvez invoquer sous forme de commandes slash dans la CLI Codex comme dans l’Extension IDE Codex.

Les prompts personnalisés doivent être invoqués explicitement et sont stockés dans le répertoire d’accueil local de Codex (par exemple, `~/.codex`) ; ils ne sont donc pas partagés via votre dépôt. Si vous souhaitez partager un prompt (ou permettre à Codex de l’invoquer implicitement), [utilisez les Skills](/fr-FR/codex/build-skills).

1. Créez le répertoire des prompts :

   ```bash
   mkdir -p ~/.codex/prompts

2. Créez `~/.codex/prompts/draftpr.md` et ajoutez-y des instructions réutilisables :

   ```markdown
   ---
   description: Prep a branch, commit, and open a draft PR
   argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
   ---

   Create a branch named `dev/<feature_name>` for this work.
   If files are specified, stage them first: $FILES.
   Commit the staged changes with a clear message.
   Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.

3. Redémarrez Codex pour qu’il charge le nouveau prompt (redémarrez votre session CLI et rechargez l’Extension IDE si vous l’utilisez).

Résultat attendu : lorsque vous saisissez `/prompts:draftpr` dans le menu des commandes slash, votre commande personnalisée s’affiche, accompagnée de la description définie dans l’en-tête et d’indications précisant que les fichiers et le titre de la PR sont facultatifs.

## Ajoutez des métadonnées et des arguments

Codex lit les métadonnées du prompt et résout les espaces réservés lors du prochain démarrage de la session.

- **Description :** Elle s’affiche sous le nom de la commande dans la fenêtre contextuelle. Définissez-la dans l’en-tête YAML avec `description:`.
- **Indication sur les arguments :** Décrivez les paramètres attendus à l’aide de `argument-hint: KEY=<value>`.
- **Espaces réservés positionnels :** `$1` à `$9` sont remplacés par les arguments, séparés par des espaces, que vous fournissez après la commande. `$ARGUMENTS` les regroupe tous.
- **Espaces réservés nommés :** Utilisez des noms en majuscules comme `$FILE` ou `$TICKET_ID` et fournissez les valeurs sous la forme `KEY=value`. Mettez entre guillemets les valeurs contenant des espaces (par exemple, `FOCUS="loading state"`).
- **Signes dollar littéraux :** Écrivez `$$` pour insérer un seul signe `$` dans le prompt après substitution.

Après avoir modifié les fichiers de prompts, redémarrez Codex ou ouvrez une nouvelle discussion pour que les mises à jour soient chargées. Codex ignore les fichiers non Markdown du répertoire des prompts.

## Invoquez et gérez les commandes personnalisées

1. Dans Codex (CLI ou Extension IDE), saisissez `/` pour ouvrir le menu des commandes slash.
2. Saisissez `prompts:` ou le nom du prompt, par exemple `/prompts:draftpr`.
3. Fournissez les arguments requis :

   ```text
   /prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"

4. Appuyez sur Entrée pour envoyer les instructions après substitution (omettez les arguments dont vous n’avez pas besoin).

Résultat attendu : Codex remplace, dans le contenu de `draftpr.md`, les espaces réservés par les arguments que vous avez fournis, puis envoie le résultat sous forme de message.

Gérez les prompts en modifiant ou en supprimant les fichiers situés dans `~/.codex/prompts/`. Codex n’analyse que les fichiers Markdown situés à la racine de ce dossier ; placez donc chaque prompt personnalisé directement dans `~/.codex/prompts/`, et non dans des sous-répertoires.
