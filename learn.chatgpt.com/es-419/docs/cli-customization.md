<!-- source: https://learn.chatgpt.com/es-419/docs/cli-customization -->

La CLI de Codex ofrece opciones específicas de la terminal para configurar la apariencia de las sesiones interactivas
y la forma de ingresar comandos y prompts.

## Resaltado de sintaxis y temas

La interfaz de usuario de la terminal (TUI) aplica resaltado de sintaxis a los bloques de código delimitados en Markdown y a las
diferencias entre archivos. Ejecuta `/theme` para abrir el selector de temas, previsualizarlos y guardar tu
selección en `tui.theme` del archivo `$CODEX_HOME/config.toml`.

Para agregar un tema personalizado, coloca un archivo `.tmTheme` en `$CODEX_HOME/themes` y luego
selecciónalo en el selector de temas.

## Autocompletado del shell

Genera un script de autocompletado para Bash, el shell Z, Fish o PowerShell:

```bash
codex completion zsh

Carga el script desde la configuración de tu shell. Para el shell Z, agrega:

```bash
eval "$(codex completion zsh)"

Si el shell Z muestra `command not found: compdef`, inicializa su sistema de autocompletado
antes de cargar las definiciones de autocompletado de Codex:

```bash
autoload -Uz compinit && compinit
eval "$(codex completion zsh)"

Reinicia el shell, escribe `codex` y presiona <kbd>Tab</kbd> para comprobar que el autocompletado funcione.

## Editor de prompts

Para prompts más largos, presiona <kbd>Ctrl</kbd>+<kbd>G</kbd> en el Editor para abrir
el editor indicado por `VISUAL` o por `EDITOR` si la variable `VISUAL` no está definida. Guarda
y cierra el editor para que el texto vuelva al Editor antes de enviarlo.

Para conocer los controles interactivos del teclado y consultar la lista completa de comandos y opciones, consulta
[Comandos](/codex/developer-commands?surface=cli#cli-interactive-shortcuts).
