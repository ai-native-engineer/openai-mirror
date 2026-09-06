<!-- source: https://learn.chatgpt.com/pt-BR/docs/projects -->

Use um projeto para organizar chats relacionados e dar ao ChatGPT o contexto necessário.
A visualização **Projetos** no aplicativo do ChatGPT para desktop inclui projetos do ChatGPT e
projetos locais vinculados a pastas no seu computador.

## Escolha um projeto ou comece sem projeto

Crie um projeto quando o trabalho continuar ao longo do tempo, gerar mais de um
resultado ou depender dos mesmos arquivos e fontes. Inicie um chat sem um projeto
quando o trabalho for independente e não precisar do contexto compartilhado do projeto.

Use um projeto para reunir chats, arquivos, instruções e fontes relacionados.
O mesmo projeto pode conter chats iniciados com Chat ou ChatGPT Work.

## Escolha um projeto ou inicie um chat sem projeto

Crie um projeto quando o trabalho continuar ao longo do tempo, gerar mais de um
resultado ou depender dos mesmos arquivos e fontes. Inicie um chat sem um projeto
quando o trabalho for independente e não precisar do contexto compartilhado do projeto.

Cada projeto tem uma seção **Chats** , que lista os chats do projeto, e uma seção **Fontes**
para arquivos enviados e contexto conectado. As instruções do projeto se aplicam
a todos os seus chats. Um projeto do ChatGPT não oferece acesso direto a uma pasta no
seu computador; portanto, envie ou conecte as fontes que você quer que o ChatGPT use.

Com qualquer uma das opções, inicie um novo chat pelo projeto para usar os arquivos e as
instruções compartilhados. Depois, acesse-o novamente em **Chats**.

O Codex CLI considera o diretório em que você o inicia como o projeto do chat.
Execute `codex` no diretório em que você quer que o Codex trabalhe ou informe
`--cd <directory>` (`-C`) para defini-lo explicitamente. A CLI não disponibiliza a visualização
Projetos do ChatGPT.

A extensão para IDE considera a pasta ou o workspace aberto na IDE como o projeto
local. Em um workspace com várias raízes, selecione a raiz do workspace para o chat. A
extensão não disponibiliza a visualização Projetos do ChatGPT presente na Web ou no aplicativo para desktop.

<a id="work-in-a-project"></a>

## Trabalhar em um projeto

A visualização **Projetos** reúne os projetos do ChatGPT e os projetos locais em um só lugar.
Os projetos do ChatGPT mantêm arquivos e contexto disponíveis em chats relacionados. Um
projeto local permite que os chats acessem uma ou mais pastas no seu computador, como uma
coleção de arquivos de origem ou uma base de código.

Inicie um chat separado para cada resultado distinto, para que as mensagens e os resultados permaneçam
focados enquanto o projeto mantém o trabalho relacionado organizado.

  
    
  

## Trabalhar em um projeto

Um projeto do ChatGPT dá aos seus chats acesso aos mesmos arquivos enviados, às instruções
do projeto e às fontes conectadas. Use o Chat para um chat rápido ou
o ChatGPT Work para uma entrega mais abrangente; ambos aparecem como chats na seção
**Chats** do projeto. Inicie um chat separado para cada resultado distinto, para que as
mensagens e os resultados permaneçam focados enquanto o projeto preserva o contexto compartilhado.

## Trabalhar em um diretório de projeto

Inicie o Codex no diretório que deve fornecer o contexto de arquivos do chat. Use
`/new` para iniciar um chat separado para cada resultado distinto. Use `/resume` enquanto o
Codex estiver aberto ou execute `codex resume` para continuar um chat salvo.

O chat mantém a transcrição e o diretório de trabalho registrado, enquanto o Codex lê
os arquivos da árvore de trabalho atual. Mantenha as orientações permanentes do projeto em
`AGENTS.md` ou na documentação versionada para que fiquem disponíveis em chats futuros.

## Trabalhar em um workspace

Abra a pasta ou o workspace que deve fornecer o contexto de arquivos do chat. Inicie
um novo chat para cada resultado distinto e selecione-o em **Chats recentes** para
retomá-lo. Os chats do mesmo projeto podem trabalhar com os mesmos arquivos, mas cada
chat mantém sua própria transcrição.

A seleção atual e os arquivos abertos fornecem contexto para a interação atual. Mantenha
as orientações permanentes do projeto em `AGENTS.md` ou na documentação versionada para que fiquem
disponíveis em chats futuros.

<a id="manage-project-threads"></a>
<a id="organize-projects-and-chats"></a>

<a id="organize-projects-and-tasks"></a>

## Organizar projetos e chats

Mantenha o trabalho ativo visível e tire do caminho o que já foi concluído:

- **Fixe um projeto** para mantê-lo perto do topo da barra lateral. Também é possível fixá-lo
  na visualização Projetos.
- **Fixe um chat** se você o acessa com frequência, mesmo que chats mais recentes apareçam no
  projeto.
- **Renomeie um chat** com um título curto que descreva o resultado, como “Briefing do
  lançamento do 3º trimestre” ou “Revisão da acessibilidade do checkout”.
- **Pesquise projetos** na visualização Projetos. Abra **Pesquisar chats** na
  barra lateral para encontrar um chat anterior quando você se lembrar de uma frase ou do nome da branch, mas não
  do título. Pesquisar chats não tem um atalho padrão, mas você pode atribuir
  um em **Configurações \> Atalhos de teclado**.
- **Arquive um chat** ao concluir o trabalho. No menu do projeto, selecione
**Arquivar chats** para arquivar os chats do projeto de uma só vez.

Fixar não adiciona contexto nem altera o que o ChatGPT pode acessar. Isso só muda
onde o projeto ou o chat aparece na barra lateral.

Restaure chats arquivados em **Configurações \> Chats arquivados**.

<a id="organize-projects-and-tasks-1"></a>

## Organizar projetos e chats

Mantenha o trabalho ativo visível e tire do caminho o que já foi concluído:

- **Fixe um projeto** para mantê-lo perto do topo da barra lateral. Também é possível fixá-lo
  na visualização Projetos.
- **Fixe um chat** se você o acessa com frequência, mesmo que chats mais recentes apareçam no
  projeto.
- **Renomeie um chat** com um título curto que descreva o resultado, como “Briefing do
  lançamento do 3º trimestre” ou “Revisão da acessibilidade do checkout”.
- **Pesquise projetos** na visualização Projetos. Pesquise chats anteriores com
<kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>K</kbd> quando você se lembrar de uma frase ou do
  nome da branch, mas não do título.
- **Arquive um chat** ao concluir o trabalho.

Fixar não adiciona contexto nem altera o que o ChatGPT pode acessar. Isso só muda
onde o projeto ou o chat aparece na barra lateral.

Restaure chats arquivados em **Configurações \> Controles de dados \> Chats arquivados**.

<a id="use-local-projects-for-folders-and-codebases"></a>

## Usar projetos locais para pastas e bases de código

Adicione um projeto local quando o ChatGPT precisar ler ou alterar arquivos no seu computador.
Os projetos não precisam ter uma pasta, mas você pode anexar pastas conforme necessário.

Para adicionar ou alterar pastas, abra o menu do projeto e selecione **Editar projeto**.
Selecione **Adicionar pasta** para anexar várias pastas. O ChatGPT pode ler e alterar arquivos
em todas as pastas anexadas. Para alterar o diretório de trabalho padrão, passe o cursor sobre uma
pasta e selecione **Definir como principal**.

Novos chats são iniciados na pasta principal. O Codex também usa essa pasta como padrão
para operações do Git e para a descoberta automática de `AGENTS.md`, habilidades e
`config.toml`. As pastas secundárias continuam disponíveis para pesquisa, leitura e
edição de arquivos, mas o Codex não descobre automaticamente esses arquivos de projeto nas
pastas secundárias.

Use várias pastas quando o trabalho relacionado estiver em locais diferentes, como um aplicativo e
sua documentação ou um site e seu backend. Crie projetos separados para trabalhos
não relacionados ou quando cada chat deva acessar apenas uma parte de um repositório.
Isso mantém o contexto de trabalho focado. No momento, projetos remotos oferecem suporte a uma
pasta.

Use [ambientes locais](/pt-BR/codex/environments/local-environment) para definir ações de configuração
e comandos comuns de um projeto. O [painel de
revisão](/pt-BR/codex/code-review?surface=app) pode mostrar alterações nos repositórios
anexados ao mesmo projeto. As ações de pull request e
[árvore de trabalho](/pt-BR/codex/environments/git-worktrees) têm como destino o repositório
principal. Quando você inicia um chat em uma árvore de trabalho, as outras pastas continuam
anexadas.

Projetos e árvores de trabalho organizam o trabalho, mas o [sandbox](/pt-BR/codex/sandboxing)
controla o que os comandos locais podem ler, alterar ou acessar pela rede.

<a id="start-without-a-project"></a>

<a id="start-a-task-without-a-project"></a>

## Iniciar um chat sem um projeto

Selecione **Novo chat** quando o trabalho for independente e não precisar de arquivos
nem instruções compartilhados do projeto ou de acesso a pastas. Crie um projeto primeiro quando
vários chats forem depender do mesmo contexto.

<a id="start-a-task-without-a-project-1"></a>

## Iniciar um chat sem um projeto

Inicie um chat pela tela Início do ChatGPT quando ele não precisar de arquivos, instruções
ou fontes compartilhados do projeto. Você pode usar o Chat ou o ChatGPT Work; na Web,
as duas opções criam chats.

Se o trabalho aumentar, transfira-o para um projeto e use nomes claros de chat para cada
resultado. Um projeto pode conter chats paralelos para pesquisa, redação, revisão e
acompanhamento sem misturar todas as mensagens em um único contexto.

<a id="start-a-chat"></a>
<a id="start-a-standalone-chat"></a>

<a id="use-quick-chat-for-a-quick-conversation"></a>

## Use o Chat rápido para uma pergunta rápida

O Chat rápido abre um chat comum do ChatGPT. Os chats do ChatGPT não aparecem na
barra lateral do Codex, que contém seus chats e projetos do Codex.

Passe o cursor sobre **Novo chat** e selecione o ícone de **Chat rápido** à direita. Você também
pode pressionar

<kbd>Cmd+Option+N</kbd> no macOS ou <kbd>Ctrl+Alt+N</kbd> no Windows e no Linux.
Em **Novo chat**, você pode abrir um chat existente do ChatGPT e adicioná-lo a um
chat do Codex.

## Adicionar outras ferramentas e contexto

- Anexe arquivos ou [entradas de imagem](/pt-BR/codex/image-inputs) diretamente a um chat
  quando forem relevantes apenas para essa solicitação.
- Instale [plug-ins](/pt-BR/codex/plugins) para adicionar contexto e ações de outros
  serviços.
- Configure os servidores [MCP](/pt-BR/codex/extend/mcp) quando sua organização ou configuração de desenvolvimento
  disponibilizar ferramentas por meio do Model Context Protocol.
- Use [memórias](/pt-BR/codex/customization/memories), quando disponíveis, para aproveitar em chats futuros o contexto útil de
  trabalhos anteriores.

- Envie [entradas de imagem](/pt-BR/codex/image-inputs) para uma conversa quando o contexto visual se aplicar
  apenas a essa solicitação.
- Instale [plug-ins](/pt-BR/codex/plugins) para incorporar contexto e ações de outros
  serviços.
- Configure os servidores [MCP](/pt-BR/codex/extend/mcp) quando sua organização ou seu ambiente de desenvolvimento
  disponibilizar ferramentas por meio do Model Context Protocol.
- Use [memórias](/pt-BR/codex/customization/memories), quando disponíveis, para reaproveitar em conversas futuras o contexto útil de
  trabalhos anteriores.

- Faça referência a arquivos abertos ou selecione código no editor para adicionar contexto à
interação atual.
- Configure os servidores [MCP](/pt-BR/codex/extend/mcp) quando sua organização ou seu ambiente de desenvolvimento
  disponibilizar ferramentas por meio do Model Context Protocol.
- Use as [memórias](/pt-BR/codex/customization/memories) do host Codex conectado, quando
  disponíveis, para aproveitar contexto útil em conversas futuras.

- Adicione arquivos e fontes conectadas à seção **Fontes** do projeto quando precisarem
  estar disponíveis em todas as conversas do projeto.
- Anexe arquivos ou [entradas de imagem](/pt-BR/codex/image-inputs) diretamente a uma conversa quando
  forem relevantes apenas para essa conversa.
- No ChatGPT Work, instale [plug-ins](/pt-BR/codex/plugins) para incorporar contexto e
  ações de outros serviços.
- Use [memórias](/pt-BR/codex/customization/memories), quando disponíveis, para reaproveitar em conversas futuras o contexto útil de
  trabalhos anteriores.

## Próximas etapas

- [Aprenda a escrever e aprimorar prompts](/pt-BR/codex/prompting)
- [Aprenda a usar o ChatGPT](/pt-BR/codex/use-chatgpt)
- [Dê continuidade a trabalhos de longa duração](/pt-BR/codex/long-running-work)
