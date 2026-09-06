<!-- source: https://learn.chatgpt.com/fr-FR/docs/windows/wsl -->

Lorsque vous utilisez WSL2, Codex s’exécute dans l’environnement Linux au lieu d’utiliser le
[bac à sable Windows](/fr-FR/codex/windows/windows-sandbox) natif. Choisissez WSL2 si vous avez besoin d’outils
natifs de Linux, si vos dépôts et votre workflow de développement se trouvent déjà dans WSL2, ou si
aucun des deux modes de bac à sable natifs de Windows ne fonctionne dans votre environnement.

WSL1 était pris en charge jusqu’à la version `0.114` de Codex. À partir de la version `0.115` de Codex, le bac à sable
Linux utilise désormais `bubblewrap` ; WSL1 n’est donc plus pris en charge.

## Lancez VS Code depuis WSL

Pour obtenir des instructions détaillées, consultez le [tutoriel WSL officiel de VS Code](https://code.visualstudio.com/docs/remote/wsl-tutorial).

### Prérequis

- Un système Windows sur lequel WSL est installé. Pour installer WSL, ouvrez PowerShell en tant qu’administrateur, puis exécutez `wsl --install` (Ubuntu est un choix courant).
- VS Code avec [l’extension WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) installée.

### Ouvrez VS Code depuis un terminal WSL

```bash
# From your WSL shell
cd ~/code/your-project
code .

Cette opération ouvre une fenêtre distante WSL, installe VS Code Server si nécessaire et garantit que les terminaux intégrés s’exécutent sous Linux.

### Vérifiez que vous êtes connecté à WSL

- Repérez la barre d’état verte affichant `WSL: <distro>`.
- Les terminaux intégrés doivent afficher des chemins Linux (par exemple `/home/...`) plutôt que `C:\`.
- Vous pouvez le vérifier avec :

  ```bash
  echo $WSL_DISTRO_NAME

  Cette commande affiche le nom de votre distribution.

  Si « WSL: ... » n’apparaît pas dans la barre d’état, appuyez sur `Ctrl+Shift+P`, choisissez
`WSL: Reopen Folder in WSL` et conservez votre dépôt sous `/home/...` (et non sous
`C:\`) pour obtenir des performances optimales.

  Si l’application Windows ou le sélecteur de projets n’affiche pas votre dépôt WSL, saisissez
<code>\\wsl$</code> dans le sélecteur de fichiers ou l’Explorateur de fichiers, puis accédez au répertoire personnel de votre
  distribution.

## Utilisez Codex CLI avec WSL

Exécutez ces commandes dans une fenêtre PowerShell ou Windows Terminal ouverte avec des droits d’administrateur :

```powershell
# Install default Linux distribution (like Ubuntu)
wsl --install

# Start a shell inside Windows Subsystem for Linux
wsl

Exécutez ensuite ces commandes depuis votre shell WSL :

```bash
# Install and run Codex in WSL
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex

## Travaillez sur le code dans WSL

- Travailler dans des chemins montés depuis Windows, comme <code>/mnt/c/...</code>, peut être plus lent que dans des chemins natifs de Windows. Conservez vos dépôts dans votre répertoire personnel sous Linux (par exemple <code>~/code/my-app</code>) pour bénéficier d’entrées/sorties plus rapides et limiter les problèmes de liens symboliques et d’autorisations :
  ```bash
  mkdir -p ~/code && cd ~/code
  git clone https://github.com/your/repo.git
  cd repo
- Si vous devez accéder aux fichiers depuis Windows, vous les trouverez à l’emplacement <code>\\wsl$\\Ubuntu\\home&lt;user\></code> dans l’Explorateur de fichiers.

## Dépannage et FAQ

- Vérifiez que vous ne travaillez pas sous <code>/mnt/c</code>. Déplacez le dépôt dans WSL (par exemple, sous <code>~/code/...</code>).
- Augmentez si nécessaire la mémoire et les ressources processeur allouées à WSL ; mettez WSL à jour vers la dernière version :
  ```powershell
  wsl --update
  wsl --shutdown

Vérifiez que le binaire existe et se trouve dans le `PATH` sous WSL :

```bash
which codex || echo "codex not found"

Si le binaire est introuvable, suivez les [instructions de configuration de Codex CLI](#use-codex-cli-with-wsl).
