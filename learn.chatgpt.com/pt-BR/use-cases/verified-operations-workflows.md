<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/verified-operations-workflows -->

## Execute operações que você possa auditar

Se você precisa executar regularmente operações repetíveis, como conceder acesso a um usuário, aplicar uma atualização em lote ou chamar um script com parâmetros diferentes, pode usar o ChatGPT para automatizá-las e obter uma saída auditável.

Use este fluxo de trabalho quando o ChatGPT precisar executar uma operação repetível e mostrar o que aconteceu por meio de um artefato que sirva como verificação.

## Descreva a tarefa e as entradas

1. Forneça ao ChatGPT a tabela de entrada, os arquivos, os tickets ou outra lista de itens aos quais o processo em lote deve ser aplicado.
2. Se aplicável, indique ao ChatGPT a fonte de aprovação ou a política que define o escopo permitido.
3. Informe ao ChatGPT qual script, API, habilidade, CLI ou fluxo de trabalho do aplicativo deve ser usado para executar a operação.
4. Opcionalmente, solicite uma simulação quando o fluxo de trabalho oferecer suporte a esse recurso.
5. Peça ao ChatGPT para executar a operação em lote e registrar uma linha de sucesso ou falha para cada item.

Mantenha o escopo delimitado e instrua o ChatGPT a executar a operação somente quando todas as entradas obrigatórias estiverem disponíveis.
Se uma linha não tiver um campo obrigatório, o ChatGPT deverá sinalizá-la em vez de tentar adivinhar.

Conecte as ferramentas que você usa para executar a operação por meio de [plug-ins](/pt-BR/codex/plugins), como seu sistema de tickets ou sua planilha com os itens da lista.

## Exija uma comprovação para verificar o resultado

Uma boa execução de uma operação inclui um resultado que você ou um colega de equipe possa inspecionar, como um arquivo CSV, um arquivo de log, um link para um painel, uma captura de tela, uma verificação de PR ou outra comprovação de que a operação foi bem-sucedida. No aplicativo do ChatGPT para desktop, você pode [abrir e inspecionar os arquivos gerados](/pt-BR/codex/artifacts-viewer) depois da execução para verificar o resultado.

## Transforme a execução em um fluxo de trabalho reutilizável

Após a primeira execução bem-sucedida, peça ao ChatGPT para documentar as partes repetíveis. No caso de fluxos de trabalho comuns, isso pode se tornar uma [habilidade](/pt-BR/codex/build-skills) ou uma [tarefa agendada](/pt-BR/codex/automations).

Para operações agendadas, só crie uma tarefa agendada depois que a execução manual produzir uma saída confiável. Mantenha somente como rascunho as ações sensíveis que possam afetar permanentemente o acesso ou os dados, a menos que você queira explicitamente que o ChatGPT as execute.
