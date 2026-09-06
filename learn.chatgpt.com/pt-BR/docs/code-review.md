<!-- source: https://learn.chatgpt.com/pt-BR/docs/code-review -->

Use o ChatGPT ou o Codex para inspecionar alterações no código antes de fazer commit ou push.

## Iniciar uma revisão

No ChatGPT Work, envie o código que deseja revisar ou disponibilize-o por meio
de um [plug-in](/pt-BR/codex/plugins) de código-fonte instalado. No prompt, identifique a pull
request, a branch, o commit, os arquivos e os critérios de revisão.

### Revisar no aplicativo

Abra o painel de revisão para entender o que mudou, dar feedback sobre linhas específicas
e decidir o que preparar, reverter, incluir em um commit ou enviar por push.

Para pedir ao Codex que revise as alterações, digite `/review` no editor. Escolha
**Revisar em relação a uma branch base** ou **Revisar alterações sem commit**. O Codex apresenta
apontamentos priorizados sem alterar sua árvore de trabalho.

O painel de revisão requer um projeto em um repositório Git. Se o projeto
ainda não for um repositório Git, o aplicativo solicitará que você crie um.

Digite `/review` para abrir as predefinições de revisão da CLI. O Codex inicia um revisor dedicado
que lê o diff selecionado e apresenta apontamentos priorizados e acionáveis
sem alterar sua árvore de trabalho.

Digite `/review` no editor da extensão para IDE. Escolha **Revisar em relação a uma branch
base** ou **Revisar alterações sem commit**. O Codex apresenta apontamentos priorizados
sem alterar sua árvore de trabalho.

O comando `/review` só aparece quando o projeto aberto está em um
repositório Git.

## Escolher o escopo da revisão

Indique no prompt a pull request, a branch, o commit ou os arquivos a inspecionar. Para
revisar arquivos locais que não estão disponíveis por meio de um plug-in de código-fonte instalado,
envie-os para o chat.

### Quais alterações são exibidas

O painel de revisão reflete o estado do seu repositório Git, não apenas o que o Codex
editou. Ele inclui alterações feitas pelo Codex, alterações que você mesmo fez e quaisquer
outras alterações sem commit no repositório.

Por padrão, o painel de revisão mostra alterações **Não preparadas** . Use **Preparadas** para ver o
índice do Git, **Commit** para um commit selecionado, **Branch** para o diff em relação à sua
branch base ou **Último turno** para o turno mais recente do assistente.

### Revisar vários repositórios

Quando um [projeto local inclui várias pastas](/pt-BR/codex/projects#use-local-projects-for-folders-and-codebases)
associadas a diferentes repositórios Git, o painel de revisão pode mostrar as alterações de cada
repositório. Abra o seletor de repositórios no cabeçalho da revisão para inspecionar
outro repositório e ver as linhas adicionadas ou removidas sem sair do
painel de revisão atual.

Escolha **Último turno** para ver as alterações mais recentes feitas pelo assistente nos
repositórios vinculados. O seletor de repositórios mostra **Todos os repositórios** nessa visualização. Outros
escopos de revisão, como **Não preparadas**, **Preparadas** e **Branch**, aplicam-se ao
repositório selecionado.

Escolha um destes escopos do comando `/review`:

- **Revisar em relação a uma branch base** encontra a base de merge e revisa o diff da sua branch.
- **Revisar alterações sem commit** inclui arquivos preparados, não preparados e não rastreados.
- **Revisar um commit** analisa o conjunto exato de alterações de um commit selecionado.
- **Instruções de revisão personalizadas** concentram a revisão nos critérios que você fornece.

Escolha um destes escopos do comando `/review`:

- **Revisar em relação a uma branch base** compara sua branch atual com uma branch selecionada.
- **Revisar alterações sem commit** revisa as alterações na sua árvore de trabalho.

## Trabalhar com os resultados da revisão

Os apontamentos da revisão aparecem no chat na Web. Peça evidências, solicite uma
revisão complementar mais restrita ou peça ao ChatGPT que prepare arquivos revisados.

### Resultados da revisão de código

Os apontamentos da revisão aparecem como comentários em linha no painel de revisão.

Por padrão, as revisões são executadas no chat atual. Em **Configurações** \> **Geral** \>
**Revisão de código**, escolha **Separado** para iniciar um chat de revisão separado. Consulte as
[configurações para desenvolvedores](/codex/developer-settings?surface=app#app-code-review).

  
    
  

A revisão aparece como um turno na transcrição. Defina `review_model` em
`config.toml` quando quiser que as revisões usem um modelo diferente daquele usado na
sessão atual.

Por padrão, a revisão é executada no chat atual. Defina `chatgpt.reviewDelivery` como
`detached` quando quiser que `/review` inicie um chat de revisão separado. Consulte a
[referência das configurações da extensão para IDE](/codex/developer-settings?surface=ide#ide-editor-settings-reference).

Se você pedir ao ChatGPT que prepare arquivos revisados, as ferramentas e as permissões do workspace
disponíveis para o chat continuam valendo.

Se você pedir ao Codex que aplique as correções encontradas, suas [configurações habituais de sandbox e
aprovação](/pt-BR/codex/sandboxing) continuam valendo.

## Navegar pelo painel de revisão

- Clicar no nome de um arquivo normalmente abre esse arquivo no editor escolhido. Você
  pode escolher o editor padrão nas [configurações para desenvolvedores](/codex/developer-settings?surface=app#app-project-and-terminal-behavior).
- Clicar no plano de fundo do nome do arquivo expande ou recolhe o diff.
- Clicar em uma linha com a tecla <kbd>Cmd</kbd> pressionada abre essa linha no editor escolhido.
- Se estiver satisfeito com uma alteração, você pode [prepará-la ou reverter as alterações](#staging-and-reverting-files) que não quiser.

## Comentários em linha para feedback

Os comentários em linha permitem associar feedback diretamente a linhas específicas do diff.
Essa costuma ser a maneira mais rápida de direcionar o Codex à correção certa.

Para adicionar um comentário em linha:

1. Abra o painel de revisão.
2. Passe o cursor sobre a linha que deseja comentar.
3. Selecione o botão **+** que aparecer.
4. Escreva seu feedback e envie-o.
5. Ao terminar de registrar seu feedback, volte ao chat e envie uma mensagem.

Como os comentários se referem a linhas específicas, o Codex pode responder com mais precisão do que com
uma instrução geral.

O Codex considera os comentários em linha como orientações para a revisão. Depois de comentar, envie uma
mensagem de acompanhamento que explicite sua intenção, por exemplo: “Trate dos
comentários em linha e mantenha o escopo mínimo.”

## Revisões de pull request

Quando o Codex tem acesso ao seu repositório no GitHub e o projeto atual está na
branch da pull request, o aplicativo do ChatGPT para desktop pode ajudar você a tratar o feedback da pull
request sem sair do aplicativo. A barra lateral mostra o contexto da pull request
e o feedback dos revisores, enquanto o painel de revisão mostra os comentários
ao lado do diff para que você possa pedir ao Codex que resolva os problemas no mesmo chat.

Instale a GitHub CLI (`gh`) e autentique-a com `gh auth login` para que o Codex
possa carregar o contexto da pull request, os comentários da revisão e os arquivos alterados. Se `gh` não estiver
instalado ou autenticado, talvez os detalhes da pull request não apareçam na barra lateral
nem no painel de revisão.

Use este fluxo quando quiser manter todo o ciclo de correções em um só lugar:

1. Abra o painel de revisão na branch da pull request.
2. Revise o contexto da pull request, os comentários e os arquivos alterados.
3. Peça ao Codex que faça as correções indicadas nos comentários específicos que você deseja atender.
4. Inspecione o diff resultante no painel de revisão.
5. Quando estiver tudo pronto, prepare as alterações e faça commit e push delas para a branch da pull request.

Para revisões acionadas pelo GitHub, consulte [Usar o Codex no GitHub](/pt-BR/codex/third-party/github).

## Preparação e reversão de arquivos

O painel de revisão inclui ações do Git para que você possa ajustar o diff antes de fazer commit.

Você pode preparar, remover da preparação ou reverter alterações nestes níveis:

- **Diff completo**: use os botões de ação no cabeçalho da revisão, como **Preparar tudo** ou **Reverter tudo**.
- **Por arquivo**: prepare, remova da preparação ou reverta um arquivo específico.
- **Por bloco**: prepare, remova da preparação ou reverta um único bloco de alterações.

Prepare as alterações quando quiser aceitar parte do trabalho e reverta-as quando quiser descartá-las.

### Alterações preparadas e não preparadas

O Git pode representar alterações preparadas e não preparadas no mesmo arquivo. Quando isso acontece, o painel pode mostrar o mesmo arquivo nas duas visualizações. Esse é um comportamento normal do Git.
