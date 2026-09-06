<!-- source: https://learn.chatgpt.com/pt-BR/docs/windows/windows-app -->

# Aplicativo do ChatGPT para desktop no Windows

O [aplicativo do ChatGPT para desktop no Windows](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) oferece uma única interface para
trabalhar em vários projetos, executar conversas em paralelo e revisar resultados.
O aplicativo para Windows oferece suporte a fluxos de trabalho essenciais, como árvores de trabalho, tarefas agendadas e recursos do Git,
além do navegador integrado, visualizações de arquivos, plug-ins e habilidades.
Ele é executado nativamente no Windows usando o PowerShell e o
[sandbox do Windows](/pt-BR/codex/windows/windows-sandbox#windows-sandbox), ou você pode configurá-lo para
ser executado no [Subsistema do Windows para Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl).

  
    
  

## Baixar o aplicativo do ChatGPT para desktop

Baixe o [aplicativo do ChatGPT para desktop](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) para Windows.

Depois, siga o [início rápido](/pt-BR/codex/quickstart?setup=app) para começar.

Para ver as opções de instalação e atualização para empresas, consulte
[Implantar o aplicativo para Windows](/pt-BR/codex/enterprise/windows-deployment).

Se preferir instalar pela linha de comando, execute:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

## Sandbox nativo

O aplicativo do ChatGPT para desktop no Windows oferece suporte a um [sandbox do Windows](/pt-BR/codex/windows/windows-sandbox#windows-sandbox) nativo quando o agente é executado no PowerShell e usa o ambiente isolado do Linux quando o agente é executado no [Subsistema do Windows para Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl). Para aplicar as proteções do sandbox em qualquer um dos modos, selecione **Pedir aprovação** abaixo do campo de mensagem antes de enviar mensagens ao Codex.

  Executar o Codex no modo Acesso completo significa que ele não fica restrito ao diretório
  do projeto e pode realizar ações destrutivas não intencionais, o que pode causar
  perda de dados. Mantenha os limites do sandbox e use
[regras](/pt-BR/codex/agent-configuration/rules) para exceções específicas ou defina a
[política de aprovação como
  never](/pt-BR/codex/agent-approvals-security#run-without-approval-prompts) para que o
  Codex tente resolver problemas sem pedir permissões elevadas,
  de acordo com sua [configuração de aprovação e segurança](/pt-BR/codex/agent-approvals-security).

## Personalize seu ambiente de desenvolvimento

<section class="feature-grid">

<div>

### Editor preferencial

Escolha um aplicativo padrão para **Abrir**, como o Visual Studio, o VS Code ou outro
editor. Você pode substituir essa escolha em cada projeto. Se já tiver escolhido outro
aplicativo no menu **Abrir** para um projeto, a escolha específica desse
projeto terá prioridade.

</div>

  
    
  

</section>

<section class="feature-grid inverse">

<div>

### Terminal integrado

Você também pode escolher o terminal integrado padrão. Dependendo do que estiver
instalado, as opções incluem:

- PowerShell
- Prompt de Comando
- Git Bash
- WSL

Essa alteração se aplica apenas a novas sessões de terminal. Se já houver um
terminal integrado aberto, reinicie o aplicativo ou inicie uma nova conversa para
que o novo terminal padrão seja exibido.

</div>

  
    
  

</section>

## Subsistema do Windows para Linux (WSL)

Por padrão, o aplicativo do ChatGPT para desktop usa o agente do Codex nativo para Windows. Isso significa que o agente
executa comandos no PowerShell. O aplicativo ainda pode trabalhar com projetos armazenados no
Subsistema do Windows para Linux 2 (WSL2) usando a CLI `wsl` quando necessário.

Para adicionar um projeto do sistema de arquivos do WSL, clique em **Adicionar novo projeto**
ou pressione <kbd>Ctrl</kbd>+<kbd>O</kbd>. Depois, digite `\\wsl$\` na janela do Explorador de
Arquivos. Nela, escolha sua distribuição Linux e a pasta que você
deseja abrir.

Se pretende continuar usando o agente nativo do Windows, prefira armazenar os projetos no
sistema de arquivos do Windows e acessá-los pelo WSL por meio de
`/mnt/<drive>/...`. Essa configuração é mais confiável do que abrir os projetos
diretamente do sistema de arquivos do WSL.

Se quiser que o próprio agente seja executado no WSL2, abra **[Configurações](codex://settings)**,
mude o agente de Windows nativo para WSL e **reinicie o aplicativo**. A
alteração só entra em vigor após reiniciar o aplicativo. Seus projetos devem continuar
disponíveis após o reinício.

O WSL1 teve suporte até o Codex `0.114`. A partir do Codex `0.115`, o sandbox do
Linux migrou para `bubblewrap`; por isso, o WSL1 não tem mais suporte.

  
    
  

O terminal integrado é configurado independentemente do agente. Consulte
[Personalize seu ambiente de desenvolvimento](#customize-for-your-dev-setup) para ver as
opções de terminal. Você pode manter o agente no WSL e usar o PowerShell no
terminal ou usar o WSL para os dois, de acordo com seu fluxo de trabalho.

## Ferramentas úteis para desenvolvimento

O Codex funciona melhor quando algumas ferramentas comuns de desenvolvimento já estão instaladas:

- **Git**: viabiliza o painel de revisão do aplicativo do ChatGPT para desktop e permite inspecionar ou
  reverter alterações.
- **Node.js**: uma ferramenta comum que o agente usa para realizar tarefas com mais
  eficiência.
- **Python**: uma ferramenta comum que o agente usa para realizar tarefas com mais
  eficiência.
- **.NET SDK**: útil para criar aplicativos nativos do Windows.
- **GitHub CLI**: viabiliza os recursos específicos do GitHub no aplicativo do ChatGPT para desktop.

Instale essas ferramentas com o gerenciador de pacotes padrão do Windows, o `winget`, colando isto
no [terminal integrado](/pt-BR/codex/integrated-terminal) ou
pedindo ao Codex que as instale:

```powershell
winget install --id Git.Git
winget install --id OpenJS.NodeJS.LTS
winget install --id Python.Python.3.14
winget install --id Microsoft.DotNet.SDK.10
winget install --id GitHub.cli
```

Depois de instalar a GitHub CLI, execute `gh auth login` para ativar os recursos do GitHub
no aplicativo.

Se você precisar de outra versão do Python ou do .NET, altere os IDs dos pacotes para a
versão desejada.

## Solução de problemas e perguntas frequentes

### Executar comandos com permissões elevadas

Se precisar que o Codex execute comandos com permissões elevadas, inicie o próprio aplicativo do ChatGPT
para desktop como administrador. Após a instalação, abra o menu Iniciar,
localize o aplicativo e escolha **Executar como administrador**. O agente do Codex herda esse
nível de permissão.

### A política de execução do PowerShell bloqueia comandos

Se você nunca tiver usado ferramentas como Node.js ou `npm` no PowerShell, o
agente do Codex ou o terminal integrado poderá encontrar erros de política de execução.

Isso também pode acontecer se o Codex criar scripts do PowerShell para você. Nesse caso,
talvez seja necessário usar uma política de execução menos restritiva para que o PowerShell possa
executá-los.

Um erro pode ter esta aparência:

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

Uma solução comum é definir a política de execução como `RemoteSigned`:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Para ver detalhes e outras opções, consulte o
[guia sobre políticas de execução](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)
da Microsoft antes de alterar a política.

### Scripts do ambiente local no Windows

Se o seu [ambiente local](/pt-BR/codex/environments/local-environment) usar comandos multiplataforma,
como scripts do `npm`, você pode manter um único script de configuração ou
conjunto de ações compartilhado entre todas as plataformas.

Se precisar de um comportamento específico do Windows, crie scripts de configuração específicos do Windows ou
ações específicas do Windows.

As ações são executadas no ambiente usado pelo terminal integrado. Consulte
[Personalize seu ambiente de desenvolvimento](#customize-for-your-dev-setup).

Os scripts de configuração local são executados no ambiente do agente: no WSL quando o agente usa o WSL
e, caso contrário, no PowerShell.

### Compartilhar configurações, autenticação e sessões com o WSL

O aplicativo para Windows e o Codex nativo no Windows usam o mesmo diretório inicial do Codex:
`%USERPROFILE%\.codex`.

Se você também executar a Codex CLI no WSL, a CLI usará o diretório inicial do Linux
por padrão e, por isso, não compartilhará automaticamente as configurações, a autenticação em cache
nem o histórico de sessões com o aplicativo para Windows.

Para compartilhá-los, use uma destas abordagens:

- Sincronize `~/.codex` do WSL com `%USERPROFILE%\.codex` no seu sistema de arquivos.
- Aponte o WSL para o diretório inicial do Codex no Windows definindo `CODEX_HOME`:

```bash

```

Para aplicar essa configuração a todos os shells, adicione-a ao perfil do shell do WSL,
como `~/.bashrc` ou `~/.zshrc`.

### Recursos do Git indisponíveis

Se o Git não estiver instalado nativamente no Windows, o aplicativo não poderá usar alguns
recursos. Instale-o com `winget install Git.Git` no PowerShell ou no `cmd.exe`.

### O Git não é detectado em projetos abertos a partir de `\\wsl$`

Por enquanto, se quiser usar o agente nativo do Windows com um projeto também
acessível pelo WSL, a solução alternativa mais confiável é armazenar o projeto
na unidade nativa do Windows e acessá-lo pelo WSL por meio de `/mnt/<drive>/...`.

### `Cmder` não aparece na caixa de diálogo Abrir

Se `Cmder` estiver instalado, mas não aparecer na caixa de diálogo Abrir do Codex, adicione-o ao
menu Iniciar do Windows: clique com o botão direito em `Cmder` e escolha **Fixar em Iniciar**. Depois,
reinicie o Codex ou o computador.
