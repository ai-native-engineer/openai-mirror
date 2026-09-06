<!-- source: https://learn.chatgpt.com/de-DE/docs/cli-customization -->

Die Codex CLI bietet terminalspezifische Optionen für die Darstellung interaktiver Sitzungen
und für die Eingabe von Befehlen und Prompts.

## Syntaxhervorhebung und Themes

Die Terminaloberfläche (TUI) hebt die Syntax in Markdown-Codeblöcken mit Code-Fences und in Datei-Diffs
hervor. Führe `/theme` aus, um die Theme-Auswahl zu öffnen, Themes in der Vorschau anzuzeigen und deine
Auswahl unter `tui.theme` in `$CODEX_HOME/config.toml` zu speichern.

Um ein eigenes Theme hinzuzufügen, lege eine Datei im Format `.tmTheme` unter `$CODEX_HOME/themes` ab und wähle das Theme dann
in der Theme-Auswahl aus.

## Shell-Vervollständigungen

Erstelle ein Vervollständigungsskript für Bash, die Z-Shell, Fish oder PowerShell:

```bash
codex completion zsh

Lade das Skript über deine Shell-Konfiguration. Füge für die Z-Shell Folgendes hinzu:

```bash
eval "$(codex completion zsh)"

Wenn die Z-Shell `command not found: compdef` meldet, initialisiere ihr Vervollständigungssystem,
bevor du die Codex-Vervollständigungen lädst:

```bash
autoload -Uz compinit && compinit
eval "$(codex completion zsh)"

Starte die Shell neu, gib `codex` ein und drücke <kbd>Tab</kbd>, um zu prüfen, ob die Vervollständigung funktioniert.

## Prompt-Editor

Drücke bei längeren Prompts im Editor <kbd>Strg</kbd>+<kbd>G</kbd>. So öffnest du
den über `VISUAL` festgelegten Texteditor. Stattdessen wird `EDITOR` verwendet, wenn `VISUAL` nicht gesetzt ist. Speichere den Text
und schließe den Texteditor, damit der Text vor dem Senden wieder in den Editor übernommen wird.

Informationen zur Tastatursteuerung in interaktiven Sitzungen sowie die vollständige Liste der Befehle und Optionen findest du auf der Seite
[Befehle](/codex/developer-commands?surface=cli#cli-interactive-shortcuts).
