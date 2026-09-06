<!-- source: https://learn.chatgpt.com/pt-BR/docs/cli-customization -->

A CLI do Codex oferece opções específicas do terminal para definir a aparência das sessões interativas
e como você insere comandos e prompts.

## Realce de sintaxe e temas

A interface de terminal (TUI) realça a sintaxe de blocos de código Markdown delimitados e de diffs de
arquivos. Execute `/theme` para abrir o seletor de temas, visualizar temas e salvar sua
seleção em `tui.theme`, no arquivo `$CODEX_HOME/config.toml`.

Para adicionar um tema personalizado, coloque um arquivo `.tmTheme` em `$CODEX_HOME/themes` e depois
selecione-o no seletor de temas.

## Preenchimento automático do shell

Gere um script de preenchimento automático para Bash, Z shell, Fish ou PowerShell:

```bash
codex completion zsh

Carregue o script pelo arquivo de configuração do shell. Para o Z shell, adicione:

```bash
eval "$(codex completion zsh)"

Se o Z shell exibir `command not found: compdef`, inicialize o sistema de preenchimento
automático antes de carregar as definições do Codex:

```bash
autoload -Uz compinit && compinit
eval "$(codex completion zsh)"

Reinicie o shell, digite `codex` e pressione <kbd>Tab</kbd> para verificar o preenchimento automático.

## Editor de prompts

Para prompts mais longos, pressione <kbd>Ctrl</kbd>+<kbd>G</kbd> no Editor para abrir
o editor configurado por `VISUAL` ou por `EDITOR` quando `VISUAL` não estiver definida. Salve
e feche o editor para devolver o texto ao Editor antes de enviá-lo.

Para ver os controles interativos do teclado e a lista completa de comandos e opções, consulte
[Comandos](/codex/developer-commands?surface=cli#cli-interactive-shortcuts).
