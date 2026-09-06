<!-- source: https://learn.chatgpt.com/pt-BR/docs/reference/troubleshooting -->

## Perguntas frequentes

### Arquivos que o Codex não editou aparecem no painel lateral

Se o seu projeto estiver em um repositório Git, o painel de revisão exibirá automaticamente
as alterações com base no estado do Git do projeto, inclusive aquelas que o Codex
não fez.

No painel de revisão, você pode alternar entre alterações em stage e alterações que ainda não estão
em stage, além de comparar sua branch com a main.

Se quiser ver apenas as alterações do último turno do Codex, mude o painel de diff
para a visualização **Último turno**.

[Saiba mais sobre como usar o painel de revisão](/pt-BR/codex/code-review?surface=app).

### Remover um projeto da barra lateral

Para remover um projeto da barra lateral, passe o cursor sobre o nome do projeto, clique
nos três pontos e escolha "Remover." Para restaurá-lo, adicione novamente o
projeto usando o botão **Adicionar novo projeto** ao lado de **Chats** ou usando

<kbd>Cmd</kbd>+<kbd>O</kbd>.

<a id="find-archived-threads"></a>
<a id="find-archived-tasks"></a>

### Encontrar chats arquivados

Os chats arquivados ficam em [Configurações](codex://settings). Ao desarquivar
um chat, ele reaparece no local original da barra lateral.

<a id="only-some-threads-appear-in-the-sidebar"></a>
<a id="only-some-tasks-appear-in-the-sidebar"></a>

### Apenas alguns chats aparecem na barra lateral

A barra lateral permite filtrar os chats com base no estado de um projeto. Se algum
chat não aparecer, selecione o ícone de filtro ao lado de **Chats** e depois
**Cronológico**. Se ainda assim o chat não aparecer, abra
[Configurações](codex://settings) e consulte **Chats arquivados**.

### O código não é executado em uma árvore de trabalho

As árvores de trabalho são criadas em outro diretório e, por padrão, herdam os arquivos
versionados no Git. Dependendo de como você gerencia as dependências e ferramentas do
projeto, talvez seja necessário executar scripts de configuração na árvore de trabalho usando um
[ambiente local](/pt-BR/codex/environments/local-environment) ou copiar arquivos de configuração ignorados
com [`.worktreeinclude`](/pt-BR/codex/environments/git-worktrees#copy-ignored-local-files-into-managed-worktrees).
Como alternativa, você pode fazer checkout das alterações no seu projeto local habitual. Consulte
a [documentação sobre árvores de trabalho](/pt-BR/codex/environments/git-worktrees) para saber mais.

### O App não detecta o ambiente local compartilhado por um colega de equipe

A configuração do ambiente local deve ficar na pasta `.codex`, na
raiz do projeto. Se você estiver trabalhando em um monorepo com mais de um
projeto, certifique-se de abrir o projeto no diretório que contém a
pasta `.codex`.

### Codex solicita acesso ao Apple Music

Dependendo da tarefa, o Codex talvez precise navegar pelo sistema de arquivos. Alguns
diretórios do macOS, como Música, Downloads ou Mesa, exigem
aprovação adicional do usuário. Se o Codex precisar ler seu diretório inicial, o
macOS solicitará que você aprove o acesso a essas pastas.

<a id="automations-create-many-worktrees"></a>

### Tarefas agendadas criam muitas árvores de trabalho

A execução frequente de tarefas agendadas pode criar muitas árvores de trabalho com o tempo. Arquive as
execuções agendadas que não são mais necessárias e evite fixá-las, a menos que pretenda manter as
árvores de trabalho correspondentes.

### Recuperar um prompt após selecionar o destino errado

Se você iniciou um chat por engano com o destino errado (**Local**, **Árvore de trabalho** ou **Nuvem**), pode cancelar a execução atual e recuperar o prompt anterior pressionando a tecla de seta para cima no editor.

### Um recurso funciona na CLI do Codex, mas não no aplicativo ChatGPT para desktop

O aplicativo ChatGPT para desktop e a CLI do Codex podem incluir versões diferentes do Codex; por isso,
os recursos podem ficar disponíveis em uma interface antes da outra. Os recursos experimentais também podem
chegar primeiro à CLI do Codex.

Para conferir a versão da CLI do Codex instalada no sistema, execute:

```bash
codex --version

Para conferir a versão do Codex incluída no aplicativo ChatGPT para desktop, use o
caminho preservado do pacote de compatibilidade `Codex.app`:

```bash
/Applications/Codex.app/Contents/Resources/codex --version

## Feedback e logs

Digite <kbd>/</kbd> no campo de mensagem para enviar feedback à equipe. Se
você iniciar o envio de feedback em um chat existente, poderá optar por compartilhar a
sessão existente junto com o feedback. Depois de enviá-lo,
você receberá um ID de sessão que poderá compartilhar com a equipe.

Para relatar um issue:

1. Procure [issues existentes](https://github.com/openai/codex/issues) no repositório do Codex no GitHub.
2. [Abrir um novo issue do GitHub](https://github.com/openai/codex/issues/new?template=2-bug-report.yml&steps=Uploaded%20thread%3A%20019c0d37-d2b6-74c0-918f-0e64af9b6e14)

Mais logs estão disponíveis nos seguintes locais:

- Logs do App (macOS): `~/Library/Logs/com.openai.codex/YYYY/MM/DD`
- Transcrições de sessões: `$CODEX_HOME/sessions` (padrão: `~/.codex/sessions`)
- Sessões arquivadas: `$CODEX_HOME/archived_sessions` (padrão: `~/.codex/archived_sessions`)

Se você compartilhar os logs, revise-os antes para confirmar que não contêm informações
sensíveis.

## Situações de travamento e formas de recuperação

Se um chat parecer travado:

1. Verifique se o Codex está aguardando uma aprovação.
2. Abra o terminal e execute um comando básico, como `git status`.
3. Inicie um novo chat com um prompt menor e mais específico.

Se você cancelar por engano a criação da árvore de trabalho e perder o prompt, pressione a tecla de
seta para cima no editor para recuperá-lo.

## Problemas no terminal

**O terminal parece travado**

1. Feche o painel do terminal.
2. Reabra-o com <kbd>Ctrl</kbd>+<kbd>\`</kbd>.
3. Execute novamente um comando básico, como `pwd` ou `git status`.

Se os comandos se comportarem de maneira diferente do esperado, confira primeiro o diretório e a
branch atuais no terminal.

Se o terminal continuar travado, aguarde o término dos chats ativos e reinicie o aplicativo.

**As fontes não são renderizadas corretamente**

O Codex usa a mesma fonte no painel de revisão, no terminal integrado e em todos os outros trechos de código exibidos no aplicativo. Você pode configurar a fonte no painel [Configurações](codex://settings), em **Fonte do código**.
