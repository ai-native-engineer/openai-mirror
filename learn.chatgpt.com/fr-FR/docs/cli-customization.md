<!-- source: https://learn.chatgpt.com/fr-FR/docs/cli-customization -->

La CLI Codex propose des options propres au terminal pour personnaliser l’apparence des sessions interactives
et la façon dont vous saisissez les commandes et les prompts.

## Coloration syntaxique et thèmes

L’interface utilisateur du terminal (TUI) applique la coloration syntaxique aux blocs de code Markdown délimités et aux diffs
de fichiers. Exécutez `/theme` pour ouvrir le sélecteur de thème, prévisualiser les thèmes et enregistrer votre
sélection dans l’option `tui.theme` du fichier `$CODEX_HOME/config.toml`.

Pour ajouter un thème personnalisé, placez un fichier `.tmTheme` dans `$CODEX_HOME/themes`, puis
sélectionnez-le dans le sélecteur de thème.

## Complétion du shell

Générez un script de complétion pour Bash, le Z shell, Fish ou PowerShell :

```bash
codex completion zsh

Chargez le script depuis la configuration de votre shell. Pour le Z shell, ajoutez :

```bash
eval "$(codex completion zsh)"

Si le Z shell affiche `command not found: compdef`, initialisez son système de complétion
avant de charger les complétions de Codex :

```bash
autoload -Uz compinit && compinit
eval "$(codex completion zsh)"

Redémarrez le shell, saisissez `codex`, puis appuyez sur <kbd>Tab</kbd> pour vérifier que la complétion fonctionne.

## Éditeur de prompts

Pour les prompts plus longs, appuyez sur <kbd>Ctrl</kbd>+<kbd>G</kbd> dans la zone de saisie pour ouvrir
l’éditeur défini dans la variable `VISUAL`, ou dans `EDITOR` si `VISUAL` n’est pas définie. Enregistrez vos modifications
et fermez l’éditeur pour retrouver le texte dans la zone de saisie avant de l’envoyer.

Pour consulter les commandes au clavier disponibles en mode interactif ainsi que la liste complète des commandes et options, reportez-vous à la page
[Commandes](/codex/developer-commands?surface=cli#cli-interactive-shortcuts).
