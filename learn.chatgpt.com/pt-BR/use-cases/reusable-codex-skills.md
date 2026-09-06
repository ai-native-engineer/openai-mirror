<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/reusable-codex-skills -->

## Crie uma habilidade que o Codex possa ter sempre à mão

Use habilidades para fornecer ao Codex instruções, recursos e scripts reutilizáveis para tarefas recorrentes. Uma [habilidade](/pt-BR/codex/build-skills) pode preservar a tarefa, o documento, o comando ou o exemplo que tornou o Codex útil na primeira vez.

Comece com um exemplo que funcione: um chat do Codex que fez cherry-pick de um PR, um checklist de lançamento do Notion, um conjunto de comentários úteis para PRs ou uma conversa do Slack que explique um processo de lançamento.

## Como usar

1. Adicione o contexto que você quer que o Codex use.

   Permaneça no chat do Codex que você quer preservar, cole a conversa do Slack ou o link da documentação e adicione a regra, o comando ou o exemplo que o Codex deve lembrar.

2. Execute o prompt inicial.

   O prompt define o nome da habilidade que você quer e, em seguida, passa para `$skill-creator` a tarefa, o documento, o PR, o comando ou o resultado a ser preservado.

3. Deixe o Codex criar e validar a habilidade.

   O resultado deve definir `$skill-name`, descrever quando a habilidade deve ser acionada e manter as instruções reutilizáveis no lugar certo.

   As habilidades em `~/.codex/skills` ficam disponíveis em qualquer repositório. As habilidades no repositório atual podem ser incluídas em um commit para que os colegas de equipe também possam usá-las.

4. Use a habilidade e depois atualize-a pelo chat.

   Invoque a nova `$skill-name` na próxima tarefa envolvendo um PR, alerta, revisão, nota de lançamento ou design. Se ela usar o comando de teste errado, ignorar uma regra de revisão, pular uma etapa do runbook ou escrever um rascunho que você não enviaria, peça ao Codex para adicionar essa correção à habilidade.

## Forneça o material de origem

Forneça a `$skill-creator` o material que explica como a habilidade deve funcionar.

| O que você tem                                              | O que adicionar                                                                                                                                                             |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Um fluxo de trabalho de um chat do Codex que você quer preservar** | Permaneça nesse chat e diga `use this chat`. O Codex pode usar o contexto, os comandos, as alterações e o feedback do chat como ponto de partida.                                         |
| **Documentação ou um runbook**                                      | Cole o checklist de lançamento, inclua o link do runbook de resposta a incidentes, anexe o PDF da API ou indique ao Codex o guia em Markdown no seu repositório.                                 |
| **Conversa da equipe**                                      | Cole a conversa do Slack em que alguém explicou um alerta, inclua o link da revisão do PR com regras de frontend ou anexe a conversa com o suporte que explica o problema do cliente. |
| **Scripts ou comandos que a habilidade deve reutilizar**             | Adicione o comando de teste, o comando de pré-visualização, o script de lançamento, o script para buscar logs ou o comando auxiliar local que você quer que o Codex execute em tarefas futuras.                                    |
| **Um bom resultado**                                          | Adicione como referência para tarefas futuras o PR mesclado, a entrada final do registro de alterações, a nota de lançamento aprovada, o ticket resolvido, a captura de tela de antes e depois ou a resposta final do Codex.         |

Se a fonte estiver no Slack, Linear, GitHub, Notion ou Sentry, conecte essa ferramenta ao Codex usando um [plug-in](/pt-BR/codex/plugins), mencione-a no prompt inicial ou cole a parte relevante no chat.

## O que o Codex cria

A maioria das habilidades começa como um arquivo `SKILL.md`. `$skill-creator` pode adicionar referências mais extensas, scripts ou recursos quando forem necessários ao fluxo de trabalho.

## Habilidades que você pode criar

Use o mesmo padrão quando as tarefas futuras precisarem consultar o mesmo runbook, executar a mesma CLI, seguir os mesmos critérios de revisão, redigir o mesmo tipo de atualização para a equipe ou fazer o QA do mesmo fluxo no navegador. Por exemplo:

- **`$buildkite-fix-ci`** baixa os logs dos jobs com falha, diagnostica o erro e propõe a menor correção de código possível.
- **`$fix-merge-conflicts`** faz checkout de um PR do GitHub, atualiza-o em relação à branch base, resolve conflitos e retorna o comando exato de push.
- **`$frontend-skill`** mantém o Codex alinhado às suas preferências de UI, aos componentes existentes, ao ciclo de QA com capturas de tela, às escolhas de recursos e à etapa de refinamento no navegador.
- **`$pr-review-comments`** transforma notas de revisão em comentários concisos nas linhas relevantes, com o tom certo e links do GitHub.
- **`$web-game-prototyper`** define o escopo do primeiro ciclo jogável, escolhe os recursos, ajusta a experiência de jogo, faz capturas de tela e refina o resultado no navegador.
