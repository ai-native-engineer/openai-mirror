<!-- source: https://learn.chatgpt.com/pt-BR/docs/environments/git-worktrees -->

As árvores de trabalho permitem que o Codex execute vários chats independentes no mesmo projeto sem que interfiram uns nos outros. O repositório, a árvore de trabalho e os comandos permanecem no computador ou no ambiente de desenvolvimento remoto que contém o projeto. Você pode trabalhar diretamente no aplicativo do ChatGPT para desktop ou usar o [Remoto](/pt-BR/codex/remote) no aplicativo do ChatGPT para dispositivos móveis para iniciar, orientar, aprovar e revisar chats em árvores de trabalho em um computador conectado.

Em repositórios Git, as [tarefas agendadas](/pt-BR/codex/automations) podem ser executadas em árvores de trabalho dedicadas em segundo plano para não entrarem em conflito com seu trabalho em andamento. Em projetos sem controle de versão, as tarefas agendadas são executadas diretamente no diretório do projeto. Você também pode iniciar chats manualmente em uma árvore de trabalho e usar a Transferência para mover um chat entre Local e Árvore de trabalho.

  As árvores de trabalho não são executadas localmente no seu celular. Com o Remoto, o aplicativo
para dispositivos móveis controla o Codex no computador conectado, onde o repositório e a árvore de trabalho
permanecem, ou no ambiente de desenvolvimento remoto usado por esse computador. As instruções
específicas para desktop apresentadas a seguir se aplicam ao computador conectado.

## O que é uma árvore de trabalho

As árvores de trabalho só funcionam em projetos que fazem parte de um repositório Git, pois usam [árvores de trabalho do Git](https://git-scm.com/docs/git-worktree) nos bastidores. Uma árvore de trabalho permite criar uma segunda cópia ("checkout") do repositório. Cada árvore de trabalho tem sua própria cópia de todos os arquivos do repositório, mas todas compartilham os mesmos metadados (pasta `.git`) sobre commits, branches etc. Isso permite fazer checkout de várias branches e trabalhar nelas em paralelo.

## Terminologia

- **Checkout local**: o repositório que você criou. No aplicativo do ChatGPT para desktop, às vezes ele é chamado apenas de **Local** .
- **Árvore de trabalho**: uma [árvore de trabalho do Git](https://git-scm.com/docs/git-worktree) criada a partir do seu checkout local no aplicativo do ChatGPT para desktop.
- **Transferência**: o fluxo que move um chat entre Local e Árvore de trabalho. O Codex executa as operações do Git necessárias para mover seu trabalho com segurança entre os dois.

## Por que usar uma árvore de trabalho

1. Trabalhe em paralelo com o Codex sem afetar sua configuração atual em Local.
2. Enfileire trabalhos em segundo plano enquanto mantém o foco no primeiro plano.
3. Transfira um chat para Local mais tarde, quando estiver pronto para inspecionar, testar ou colaborar de forma mais direta.

## Primeiros passos

As árvores de trabalho exigem um repositório Git. Verifique se o projeto selecionado faz parte de um.

1.  Selecione "Árvore de trabalho"

    Na tela de novo chat, selecione **Árvore de trabalho** abaixo do Editor.
    Se quiser, escolha um [ambiente local](/pt-BR/codex/environments/local-environment) para executar scripts de configuração da árvore de trabalho.

2.  Selecione a branch inicial

    Abaixo do Editor, escolha a branch do Git que servirá de base para a árvore de trabalho. Pode ser sua branch `main` / `master`, uma branch de feature ou sua branch atual com alterações locais ainda não adicionadas ao stage.

3.  Envie seu prompt

    Envie seu prompt, e o Codex criará uma árvore de trabalho do Git com base na branch selecionada. Por padrão, o Codex trabalha no estado de ["HEAD desanexado"](https://git-scm.com/docs/git-checkout#_detached_head).

4.  Escolha onde continuar trabalhando

    Quando estiver pronto, você pode continuar trabalhando diretamente na árvore de trabalho ou transferir o chat para o checkout local. A transferência de ou para Local move o chat _e_ o código, permitindo que você continue no outro checkout.

## Trabalhar entre Local e Árvore de trabalho

As árvores de trabalho têm aparência e funcionamento muito parecidos com os do checkout local. A diferença está em como elas se encaixam no seu fluxo. Pense em Local como o primeiro plano e em Árvore de trabalho como o segundo plano. A Transferência permite mover um chat entre os dois.

Nos bastidores, a Transferência executa as operações do Git necessárias para mover o trabalho com segurança entre dois checkouts. Isso é importante porque **o Git só permite fazer checkout de uma branch em um lugar por vez**. Se você fizer checkout de uma branch em uma árvore de trabalho, **não poderá** fazer checkout dela no checkout local ao mesmo tempo, e vice-versa.

Na prática, há dois caminhos comuns:

1. [Trabalhar exclusivamente na árvore de trabalho](#option-1-working-on-the-worktree). Esse caminho funciona melhor quando você pode verificar as alterações diretamente nela, por exemplo, porque instalou dependências e ferramentas usando um [script de configuração do ambiente local](/pt-BR/codex/environments/local-environment).
2. [Transferir o chat para Local](#option-2-handing-a-chat-off-to-local). Use esse caminho quando quiser trazer o chat para o primeiro plano, por exemplo, para inspecionar as alterações na IDE que você costuma usar ou porque só pode executar uma instância do seu aplicativo.

### Opção 1: trabalhar na árvore de trabalho

<div class="feature-grid">

<div>

Se quiser manter as alterações exclusivamente na árvore de trabalho, transforme-a em uma branch usando o botão **Criar branch aqui** no cabeçalho do chat.

A partir daí, você pode fazer commit das alterações, fazer push da sua branch para o repositório remoto e abrir uma pull request no GitHub.

Você pode abrir a árvore de trabalho na sua IDE usando o botão "Abrir" no cabeçalho, usar o terminal integrado ou fazer qualquer outra operação necessária no diretório da árvore de trabalho.

</div>

  
    
  

</div>

Lembre-se: se você criar uma branch em uma árvore de trabalho, não poderá fazer checkout dela em nenhuma outra árvore de trabalho, inclusive no checkout local.

<a id="option-2-handing-a-thread-off-to-local"></a>
<a id="option-2-handing-a-chat-off-to-local"></a>
<a id="option-2-handing-a-task-off-to-local"></a>

### Opção 2: transferir um chat para Local

<div class="feature-grid">

<div>

Se quiser trazer um chat para o primeiro plano, selecione **Transferir** no cabeçalho do chat e mova-o para **Local**.

Esse caminho funciona bem quando você quer ver as alterações na janela da IDE que costuma usar, executar seu servidor de desenvolvimento existente ou validar o trabalho no mesmo ambiente que já usa no dia a dia.

O Codex executa as etapas do Git necessárias para mover o chat com segurança entre a árvore de trabalho e o checkout local.

Cada chat permanece associado à mesma árvore de trabalho ao longo do tempo. Se depois você o transferir de volta para uma árvore de trabalho, o Codex o devolve ao mesmo ambiente em segundo plano para que você retome de onde parou.

</div>

  
    
  

</div>

Você também pode fazer o caminho inverso. Se já estiver trabalhando em Local e quiser deixar o primeiro plano livre, use **Transferir** para mover o chat para uma árvore de trabalho. Isso é útil quando você quer que o Codex continue trabalhando em segundo plano enquanto volta sua atenção para outra tarefa local.

Como a Transferência usa operações do Git, os arquivos incluídos no arquivo `.gitignore` não serão movidos com o chat, a menos que o Codex os copie para uma árvore de trabalho local gerenciada usando `.worktreeinclude`.

## Detalhes avançados

### Árvores de trabalho gerenciadas pelo Codex e permanentes

Por padrão, os chats usam uma árvore de trabalho gerenciada pelo Codex. A ideia é que essas árvores sejam leves e descartáveis. Geralmente, uma árvore de trabalho gerenciada pelo Codex é dedicada a um único chat, e o Codex devolve esse chat à mesma árvore de trabalho se você o transferir de volta para lá mais tarde.

Se quiser um ambiente de longa duração, crie uma árvore de trabalho permanente pelo menu de três pontos de um projeto na barra lateral. Isso cria uma nova árvore de trabalho permanente que funciona como um projeto separado. As árvores de trabalho permanentes não são excluídas automaticamente, e você pode iniciar vários chats a partir da mesma árvore de trabalho.

### Como o Codex gerencia as árvores de trabalho para você

O Codex cria árvores de trabalho em `$CODEX_HOME/worktrees`. O commit inicial é o commit `HEAD` da branch selecionada ao iniciar o chat. Se você escolheu uma branch com alterações locais, o Codex também aplica as alterações sem commit à árvore de trabalho. Não é feito checkout de nenhuma branch na árvore de trabalho. Ela fica no estado de [HEAD desanexado](https://git-scm.com/docs/git-checkout#_detached_head). Assim, o Codex pode criar várias árvores de trabalho sem poluir suas branches.

### Copiar arquivos locais ignorados para árvores de trabalho gerenciadas

As árvores de trabalho locais gerenciadas pelo Codex partem de um checkout do Git, portanto os arquivos rastreados já estão presentes. Se o repositório ignorar arquivos de configuração local necessários para uma nova árvore de trabalho, adicione um arquivo `.worktreeinclude` à raiz do repositório e liste os caminhos ignorados ou os padrões no estilo de `.gitignore` que definem o que copiar quando o Codex criar uma árvore de trabalho gerenciada.

Use isso para arquivos que o Git ignora intencionalmente, como `.env`, `.env.local` ou `config/secrets.json`. O Codex copia apenas arquivos ignorados que correspondem ao que está definido em `.worktreeinclude`; ele não copia outros arquivos locais que o Git não rastreia. Não liste arquivos rastreados.

O Codex copia automaticamente um arquivo `AGENTS.override.md` ignorado para árvores de trabalho locais gerenciadas, portanto não é necessário listá-lo em `.worktreeinclude`.

```text
# .worktreeinclude
.env
.env.local
config/secrets.json

O Codex ignora links simbólicos na origem e não sobrescreve arquivos que já existam no novo checkout. Esse comportamento se aplica às árvores de trabalho locais gerenciadas pelo aplicativo do ChatGPT para desktop, não às árvores de trabalho remotas nem às árvores de trabalho do Git que você mesmo cria pela linha de comando.

### Limitações das branches

Suponha que o Codex conclua um trabalho em uma árvore de trabalho e você decida criar nela uma branch `feature/a` usando **Criar branch aqui**. Agora, você quer testá-la no checkout local. Se tentasse fazer checkout da branch, receberia o seguinte erro:

fatal: 'feature/a' is already used by worktree at '<WORKTREE_PATH>'

Para resolver isso, você precisaria fazer checkout de outra branch, em vez de `feature/a`, na árvore de trabalho.

Se pretende fazer checkout da branch localmente, use a Transferência para mover o chat para Local, em vez de tentar manter o checkout da mesma branch nos dois lugares ao mesmo tempo.

O Git impede que se faça checkout da mesma branch em mais de uma árvore de trabalho ao mesmo tempo, porque uma branch representa uma única referência mutável (`refs/heads/<name>`), cujo significado é “o estado atual do checkout” de uma árvore de trabalho.

Quando uma branch está em checkout, o Git considera que seu HEAD pertence àquela árvore de trabalho e espera que operações como commits, resets, rebases e merges avancem essa referência de maneira bem definida e sequencial. Permitir que várias árvores de trabalho façam checkout da mesma branch simultaneamente criaria ambiguidades e condições de corrida sobre qual árvore de trabalho atualizaria a referência da branch por meio de suas operações, podendo causar perda de commits, índices inconsistentes ou uma resolução de conflitos pouco clara.

Ao impor a regra de uma branch por árvore de trabalho, o Git garante que cada branch tenha uma única cópia de trabalho de referência, ao mesmo tempo que permite que outras árvores de trabalho referenciem com segurança os mesmos commits por meio de HEADs desanexados ou branches distintas.

### Limpeza de árvores de trabalho

As árvores de trabalho podem ocupar muito espaço em disco. Cada uma tem seu próprio conjunto de arquivos do repositório, dependências, caches de build etc. Por isso, o aplicativo do ChatGPT para desktop tenta manter o número de árvores de trabalho dentro de um limite razoável.

Por padrão, o Codex mantém as 15 árvores de trabalho gerenciadas pelo Codex mais recentes. Você pode alterar esse limite ou desativar a exclusão automática nas configurações se preferir gerenciar o uso do espaço em disco por conta própria.

O Codex tenta evitar a exclusão de árvores de trabalho que ainda são importantes. As árvores de trabalho gerenciadas pelo Codex não são excluídas automaticamente se:

- Houver um chat fixado associado à árvore de trabalho
- O chat ainda estiver em andamento
- A árvore de trabalho for permanente

As árvores de trabalho gerenciadas pelo Codex são excluídas automaticamente quando:

- Você arquiva o chat associado
- O Codex precisa excluir árvores de trabalho mais antigas para respeitar o limite configurado

Antes de excluir uma árvore de trabalho gerenciada pelo Codex, o Codex salva um snapshot do trabalho feito nela. Se você abrir um chat depois que a árvore de trabalho tiver sido excluída, verá a opção de restaurá-la.

## Perguntas frequentes

  Sim. O Codex cria árvores de trabalho gerenciadas em `$CODEX_HOME/worktrees` por
  padrão. Para escolher outro local, abra **Configurações \> Árvores de trabalho** e altere
**Raiz da árvore de trabalho**.

<a id="can-i-move-a-chat-between-local-and-worktree"></a>

  Sim. Use **Transferir** no cabeçalho do chat para mover um chat entre seu checkout
  local e uma árvore de trabalho. O Codex cuida das operações do Git necessárias para mover o
  chat com segurança entre os ambientes. Se você transferir o chat de volta para uma árvore de trabalho mais tarde,
  o Codex o devolverá à mesma árvore de trabalho associada.

<a id="what-happens-to-chats-if-a-worktree-is-deleted"></a>

  Os chats podem permanecer no seu histórico mesmo que o diretório da árvore de trabalho seja
excluído. No caso das árvores de trabalho gerenciadas pelo Codex, o Codex salva um snapshot antes de excluir
a árvore de trabalho e oferece a opção de restaurá-la se você reabrir o chat associado.
As árvores de trabalho permanentes não são excluídas automaticamente quando você arquiva os
chats associados a elas.
