<!-- source: https://learn.chatgpt.com/pt-BR/docs/import -->

Use o fluxo de importação para trazer instruções, configurações, habilidades, plug-ins, projetos
e trabalhos recentes de outro agente para o aplicativo do ChatGPT para desktop ou para a Codex CLI.
O aplicativo para desktop pode importar do **Claude Code**, do <strong>Claude Cowork</strong>
ou do **Cursor**. A Codex CLI pode importar do **Claude Code** ou do **Cursor**.

O aplicativo para desktop importa diretamente os itens compatíveis e permite concluir a configuração de
plug-ins ou conexões importados que precisam de autorização. Você também pode manter os trabalhos
importados sincronizados com atualizações automáticas.

A importação não altera nem exclui a configuração atual do seu agente.

  

## Iniciar uma importação

### Importar no aplicativo para desktop

1. No aplicativo do ChatGPT para desktop, abra **Configurações \> Importar**. Se **Importar** ainda não
   estiver disponível como uma seção das configurações, abra **Geral** e localize **Importar configuração de outro
   agente**.
2. Selecione **Importar**.
3. Escolha de quais agentes deseja fazer a importação e selecione **Continuar**.
4. Em **Selecionar itens para importar**, escolha o que deseja importar e selecione **Continuar**.
5. Quando a importação terminar, abra um projeto ou chat importado para continuar trabalhando.

### Manter os trabalhos importados sincronizados

No aplicativo do ChatGPT para desktop, abra **Configurações \> Importar** e ative as atualizações
automáticas para manter os trabalhos importados sincronizados com o agente de origem. Você também pode
consultar o histórico de importação na mesma seção das configurações.

### Importar na Codex CLI

1. Inicie uma sessão local da Codex CLI e digite `/import`.
2. Escolha **Claude Code** ou **Cursor**.
3. Selecione a configuração compatível, os arquivos de projeto e os chats recentes que deseja
importar.
4. Revise a configuração importada e continue trabalhando no Codex.

A Codex CLI importa até 50 chats dos últimos 30 dias. O comando `/import`
não está disponível durante uma tarefa em execução, em uma sessão remota nem enquanto você estiver conectado
a um daemon local do app-server. Consulte [Comandos de barra
da CLI](/codex/developer-commands?surface=cli#cli-import-claude-code-or-cursor-setup-with-import).

  

## Como funciona a importação

O fluxo de importação verifica tanto sua configuração no nível do usuário quanto seus projetos existentes.
A configuração no nível do usuário vem de arquivos na sua máquina. A configuração no nível do projeto vem
de arquivos nos repositórios e nas pastas que você selecionar.

Ao fazer uma importação, o ChatGPT:

1. Detecta configurações compatíveis e trabalhos recentes.
2. Importa os itens selecionados.
3. Mantém inalterada a configuração atual do seu agente.
4. Verifica se os plug-ins ou as conexões importados ainda precisam de configuração.
5. Exibe um cartão de status quando você precisa concluir a configuração.

## O que o ChatGPT pode importar

| Item importado                     | Destino                                             |
| --------------------------------- | ------------------------------------------------------- |
| Arquivos de instruções                 | [`AGENTS.md`](/pt-BR/codex/agent-configuration/agents-md)     |
| `settings.json`                   | [`config.toml`](/pt-BR/codex/config-file/config-basic)        |
| Habilidades                            | [Habilidades](/pt-BR/codex/build-skills)                           |
| Plug-ins                           | Plug-ins                                                 |
| Pastas de projetos existentes          | Projetos que usam as mesmas pastas                         |
| Memórias de projetos do Claude Code | [Memórias](/pt-BR/codex/customization/memories)               |
| Chats dos últimos 30 dias       | Chats do ChatGPT                                           |
| Configuração de servidores MCP          | [Configuração de servidores MCP no Codex](/pt-BR/codex/extend/mcp)            |
| Hooks                             | [Hooks do Codex](/pt-BR/codex/hooks)                             |
| Comandos de barra                    | [Habilidades](/pt-BR/codex/build-skills)                           |
| Subagentes                         | [Subagentes do Codex](/pt-BR/codex/agent-configuration/subagents) |

## Concluir a configuração após a importação

Quando a importação é concluída, o aplicativo exibe um cartão de status no canto inferior esquerdo.
Se um plug-in ou uma conexão importados ainda precisarem de configuração, isso será indicado no cartão.

Quando o aplicativo sinalizar um item que requer atenção, selecione **Concluir** e siga as
instruções para concluir a configuração.

## O que revisar após a importação

Revise a configuração importada antes de confiar nela, especialmente:

- Restrições ou permissões de ferramentas nas habilidades e nos agentes importados.
- Configurações de servidores MCP que usam autenticação personalizada, cabeçalhos, variáveis de
ambiente ou transportes. Talvez seja necessário fazer login novamente.
- Hooks cujo comportamento pode ser diferente após a importação.
- Plug-ins, marketplaces ou outras configurações que exigem acompanhamento manual.
- Modelos de prompt ou prompts no estilo de comando que dependem de argumentos, interpolação no shell
ou placeholders de caminho de arquivo.

## Após a importação

Quando a importação terminar, abra um dos projetos importados e continue o trabalho
a partir daí. Consulte [Usar o ChatGPT](/pt-BR/codex/use-chatgpt) para saber como iniciar sua
próxima tarefa.
