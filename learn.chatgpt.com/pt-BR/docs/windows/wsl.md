<!-- source: https://learn.chatgpt.com/pt-BR/docs/windows/wsl -->

Ao usar o WSL2, o Codex é executado no ambiente Linux, em vez de usar o
[sandbox nativo do Windows](/pt-BR/codex/windows/windows-sandbox). Escolha o WSL2 quando precisar de ferramentas nativas do
Linux, quando seus repositórios e seu fluxo de trabalho de desenvolvimento já estiverem no WSL2 ou quando
nenhum dos dois modos de sandbox nativos do Windows funcionar no seu ambiente.

O WSL1 teve suporte até o Codex `0.114`. A partir do Codex `0.115`, o sandbox
do Linux passou a usar `bubblewrap`; por isso, o WSL1 não tem mais suporte.

## Inicie o VS Code de dentro do WSL

Para ver instruções passo a passo, consulte o [tutorial oficial do VS Code para WSL](https://code.visualstudio.com/docs/remote/wsl-tutorial).

### Pré-requisitos

- Windows com o WSL instalado. Para instalar o WSL, abra o PowerShell como administrador e execute `wsl --install` (o Ubuntu é uma opção comum).
- VS Code com a [extensão WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) instalada.

### Abra o VS Code a partir de um terminal do WSL

```bash
# From your WSL shell
cd ~/code/your-project
code .

Isso abre uma janela remota do WSL, instala o VS Code Server, se necessário, e garante que os terminais integrados sejam executados no Linux.

### Confirme se você está conectado ao WSL

- Procure a barra de status verde que exibe `WSL: <distro>`.
- Os terminais integrados devem exibir caminhos do Linux (como `/home/...`) em vez de `C:\`.
- Você pode verificar com:

  ```bash
  echo $WSL_DISTRO_NAME

  Esse comando exibe o nome da sua distribuição.

  Se "WSL: ..." não aparecer na barra de status, pressione `Ctrl+Shift+P`, selecione
`WSL: Reopen Folder in WSL` e mantenha seu repositório em `/home/...` (não em
`C:\`) para obter o melhor desempenho.

  Se o aplicativo para Windows ou o seletor de projetos não mostrar seu repositório do WSL, digite
<code>\\wsl$</code> no seletor de arquivos ou no Explorer e navegue até o
  diretório pessoal da sua distribuição.

## Use a CLI do Codex com o WSL

Execute estes comandos em uma sessão do PowerShell ou do Windows Terminal com privilégios elevados:

```powershell
# Install default Linux distribution (like Ubuntu)
wsl --install

# Start a shell inside Windows Subsystem for Linux
wsl

Depois, execute estes comandos no shell do WSL:

```bash
# Install and run Codex in WSL
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex

## Trabalhe com o código dentro do WSL

- Trabalhar em caminhos montados do Windows, como <code>/mnt/c/...</code>, pode ser mais lento do que trabalhar em caminhos nativos do Windows. Mantenha seus repositórios no diretório pessoal do Linux (como <code>~/code/my-app</code>) para ter E/S mais rápida e menos problemas com links simbólicos e permissões:
  ```bash
  mkdir -p ~/code && cd ~/code
  git clone https://github.com/your/repo.git
  cd repo
- Se precisar acessar os arquivos pelo Windows, eles estarão em <code>\\wsl$\\Ubuntu\\home&lt;user\></code> no Explorer.

## Solução de problemas e perguntas frequentes

- Certifique-se de que não está trabalhando em <code>/mnt/c</code>. Mova o repositório para o WSL (por exemplo, <code>~/code/...</code>).
- Aumente a memória e a CPU alocadas ao WSL, se necessário; atualize o WSL para a versão mais recente:
  ```powershell
  wsl --update
  wsl --shutdown

Verifique se o binário existe e está no `PATH` dentro do WSL:

```bash
which codex || echo "codex not found"

Se o binário não for encontrado, siga as [instruções de configuração da CLI do Codex](#use-codex-cli-with-wsl).
