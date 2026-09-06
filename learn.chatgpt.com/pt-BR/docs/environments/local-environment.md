<!-- source: https://learn.chatgpt.com/pt-BR/docs/environments/local-environment -->

Os ambientes locais permitem definir etapas de configuração para árvores de trabalho e ações comuns para um projeto.

  Os ambientes locais estão disponíveis somente no Codex do aplicativo do ChatGPT para desktop.
  Selecione **Codex** antes de configurar ou usar um ambiente local.

Configure seus ambientes locais no painel de [configurações do aplicativo do ChatGPT para desktop](codex://settings). Você pode versionar o arquivo gerado no repositório Git do projeto para compartilhá-lo com outras pessoas.

O Codex armazena essa configuração na pasta `.codex`, na raiz do seu
projeto. Se o repositório contiver mais de um projeto, abra o diretório do
projeto que contém a pasta `.codex` compartilhada.

## Scripts de configuração

Como as árvores de trabalho ficam em diretórios diferentes dos usados pelos chats locais, talvez seu projeto não esteja totalmente configurado e faltem dependências ou arquivos que não estejam versionados no repositório. Os scripts de configuração são executados automaticamente quando o Codex cria uma nova árvore de trabalho no início de um novo chat.

Use este script para executar qualquer comando necessário para configurar seu ambiente, como instalar dependências ou executar um processo de build.

Em um projeto TypeScript, por exemplo, você pode usar um script de configuração para instalar as dependências e executar um build inicial:

```bash
npm install
npm run build

Se a configuração for específica da plataforma, defina scripts de configuração para macOS, Windows ou Linux a fim de substituir o script padrão.

## Ações

<section class="feature-grid">

<div>
Use ações para definir tarefas comuns, como iniciar o servidor de desenvolvimento do seu aplicativo ou executar a suíte de testes. Essas ações aparecem na barra superior do aplicativo do ChatGPT para desktop para acesso rápido. Elas são executadas no [terminal integrado](/pt-BR/codex/integrated-terminal) do aplicativo.

Com as ações, você evita digitar comandos para tarefas frequentes, como executar um build do projeto ou iniciar um servidor de desenvolvimento. Para uma depuração rápida e pontual, use diretamente o terminal integrado.

</div>

  
    
  

</section>

Por exemplo, em um projeto Node.js, você pode criar uma ação "Executar" com o seguinte script:

```bash
npm start

Se os comandos da ação forem específicos de cada plataforma, defina scripts específicos para macOS, Windows e Linux.

Para identificar suas ações, escolha um ícone associado a cada uma.

## Use as ferramentas integradas do Git

<div class="my-8 grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-center">

<div>

No Codex, o aplicativo do ChatGPT para desktop oferece controles comuns do Git para cada
projeto local e árvore de trabalho. O painel de diff mostra as alterações no checkout atual
e permite adicionar comentários inline para o Codex resolver. Você pode adicionar trechos individuais
ao stage ou revertê-los, adicionar arquivos inteiros ao stage ou revertê-los, fazer commit das alterações,
fazer push de uma branch e criar uma pull request sem sair do aplicativo.

Use o [terminal integrado](/pt-BR/codex/integrated-terminal) para realizar operações do Git
que não estão disponíveis no aplicativo. Para isolar as alterações simultâneas do
seu checkout local, inicie a tarefa em uma [árvore de trabalho](/pt-BR/codex/environments/git-worktrees).

</div>

  

</div>
