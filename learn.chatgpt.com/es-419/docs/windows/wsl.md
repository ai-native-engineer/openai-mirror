<!-- source: https://learn.chatgpt.com/es-419/docs/windows/wsl -->

Cuando usas WSL2, Codex se ejecuta dentro del entorno de Linux en lugar de usar la
versión nativa del [sandbox de Windows](/es-419/codex/windows/windows-sandbox). Elige WSL2 si necesitas herramientas
nativas de Linux, si tus repositorios y tu flujo de trabajo de desarrollo ya están en WSL2 o si
ninguno de los dos modos del sandbox nativo de Windows funciona en tu entorno.

Codex ofreció soporte para WSL1 hasta la versión `0.114`. A partir de la versión `0.115` de Codex, el
sandbox de Linux pasó a usar `bubblewrap`, por lo que WSL1 dejó de tener soporte.

## Inicia VS Code desde WSL

Para obtener instrucciones paso a paso, consulta el [tutorial oficial de WSL para VS Code](https://code.visualstudio.com/docs/remote/wsl-tutorial).

### Requisitos previos

- Windows con WSL instalado. Para instalar WSL, abre PowerShell como administrador y luego ejecuta `wsl --install` (Ubuntu es una opción común).
- VS Code con la [extensión WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) instalada.

### Abre VS Code desde una terminal de WSL

```bash
# From your WSL shell
cd ~/code/your-project
code .

Esto abre una ventana remota de WSL, instala VS Code Server si es necesario y garantiza que las terminales integradas funcionen en Linux.

### Confirma que tienes conexión con WSL

- Busca la barra de estado verde que muestra `WSL: <distro>`.
- Las terminales integradas deben mostrar rutas de Linux (como `/home/...`) en lugar de `C:\`.
- Puedes verificarlo con:

  ```bash
  echo $WSL_DISTRO_NAME

  Esto muestra el nombre de tu distribución.

  Si no ves “WSL: ...” en la barra de estado, presiona `Ctrl+Shift+P`, selecciona
`WSL: Reopen Folder in WSL` y mantén tu repositorio en `/home/...` (no en
`C:\`) para obtener el mejor rendimiento.

  Si la App de Windows o el selector de proyectos no muestran tu repositorio de WSL, escribe
<code>\\wsl$</code> en el selector de archivos o en el Explorador de archivos y luego ve al
  directorio principal de tu distribución.

## Usa Codex CLI con WSL

Abre PowerShell o Windows Terminal como administrador y ejecuta estos comandos:

```powershell
# Install default Linux distribution (like Ubuntu)
wsl --install

# Start a shell inside Windows Subsystem for Linux
wsl

Luego, ejecuta estos comandos desde tu shell de WSL:

```bash
# Install and run Codex in WSL
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex

## Trabaja con código en WSL

- Trabajar en rutas montadas desde Windows, como <code>/mnt/c/...</code>, puede ser más lento que hacerlo en rutas nativas de Windows. Guarda tus repositorios en tu directorio principal de Linux (por ejemplo, <code>~/code/my-app</code>) para obtener operaciones de E/S más rápidas y reducir los problemas con enlaces simbólicos y permisos:
  ```bash
  mkdir -p ~/code && cd ~/code
  git clone https://github.com/your/repo.git
  cd repo
- Si necesitas acceder a los archivos desde Windows, los encontrarás en <code>\\wsl$\\Ubuntu\\home&lt;user\></code> mediante el Explorador de archivos.

## Solución de problemas y preguntas frecuentes

- Asegúrate de no trabajar en <code>/mnt/c</code>. Mueve el repositorio a WSL (por ejemplo, a <code>~/code/...</code>).
- Si es necesario, aumenta los recursos de memoria y CPU asignados a WSL; actualiza WSL a la versión más reciente:
  ```powershell
  wsl --update
  wsl --shutdown

Verifica que el binario exista y esté en `PATH` dentro de WSL:

```bash
which codex || echo "codex not found"

Si no se encuentra el binario, sigue las [instrucciones de configuración de Codex CLI](#use-codex-cli-with-wsl).
