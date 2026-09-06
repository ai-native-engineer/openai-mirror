<!-- source: https://learn.chatgpt.com/es-419/docs/integrated-terminal -->

Cada chat de la aplicación de escritorio de ChatGPT incluye una terminal vinculada a su proyecto o
worktree actual. Ábrela desde el ícono de terminal en la esquina superior derecha de la app o
presiona <kbd>Ctrl</kbd>+<kbd>\`</kbd>.

  
    
  

## Ejecuta y valida tu proyecto

Usa la terminal para validar cambios, ejecutar scripts y realizar operaciones de Git
sin cambiar de app. ChatGPT puede leer la salida actual de la terminal, por lo que puede
revisar un servidor de desarrollo en ejecución o hacer referencia a una compilación fallida mientras trabaja
contigo.

Estos son algunos comandos comunes:

- `git status`
- `git pull --rebase`
- `pnpm test` o `npm test`
- `pnpm run lint` u otra comprobación específica del proyecto

## Crea acciones reutilizables

Si ejecutas un comando con frecuencia, define una acción en tu [entorno local](/es-419/codex/environments/local-environment#actions).
Las acciones aparecen como accesos directos en la aplicación de escritorio de ChatGPT y se ejecutan en la terminal
integrada.

<kbd>Cmd</kbd>+<kbd>K</kbd> abre la paleta de comandos de la app; no limpia la
terminal. Para limpiar la terminal, presiona <kbd>Ctrl</kbd>+<kbd>L</kbd>.
