<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/refactor-your-codebase -->

## Introdução

Quando sua base de código acumula código não utilizado, lógica duplicada, abstrações obsoletas, arquivos grandes ou padrões legados que tornam cada alteração mais cara do que deveria, considere reduzir a dívida de engenharia por meio de uma refatoração. Refatorar consiste em aprimorar a estrutura do sistema existente sem transformar esse trabalho em uma migração de stack.

O Codex é útil nesse caso porque pode primeiro mapear a área problemática e depois realizar a limpeza em pequenas etapas fáceis de revisar: excluir caminhos de código não utilizados, reorganizar módulos grandes, consolidar caminhos duplicados, modernizar padrões antigos de framework e reforçar a validação de cada etapa.

O objetivo é aprimorar a base de código existente, sem migrá-la:

1. Remova código não utilizado, funções auxiliares obsoletas, flags antigas e camadas de compatibilidade que não são mais necessárias.
2. Reduza módulos sobrecarregados extraindo funções auxiliares, dividindo componentes ou movendo efeitos colaterais para limites mais bem definidos.
3. Substitua padrões legados pelas convenções atuais do repositório: primitivas mais recentes do framework, tipos mais claros, fluxo de estado mais simples ou utilitários da biblioteca padrão.
4. Mantenha o comportamento público estável e reduza o custo da próxima alteração.

## Como usar

1. Peça ao Codex que mapeie a área antes de fazer alterações: módulos sobrecarregados, lógica duplicada, código não utilizado, testes, contratos públicos e padrões antigos que já não atendem às necessidades do repositório.
2. Escolha um tipo de limpeza por vez: remover código não utilizado, simplificar o fluxo de controle, modernizar um padrão desatualizado ou dividir um arquivo grande em partes menores com responsáveis bem definidos.
3. Antes de o Codex modificar os arquivos, peça que ele descreva o comportamento atual, a melhoria estrutural que pretende implementar e a verificação mínima que deve comprovar que o comportamento permaneceu estável.
4. Após cada etapa, revise as alterações e execute a menor verificação útil, em vez de agrupar toda a limpeza em um único diff.
5. Mantenha mudanças de stack, migrações de dependências e mudanças de arquitetura como tarefas separadas, a menos que sejam necessárias para concluir a limpeza.

  Você pode usar o Modo planejamento para criar um plano de refatoração antes de começar o
trabalho.

## Use os ExecPlans

O [guia prático de modernização de código](/cookbook/examples/codex/code_modernization) apresenta os ExecPlans: documentos que permitem que o Codex mantenha uma visão geral da limpeza, explicite o estado final pretendido e registre a validação após cada etapa.
Esses documentos são úteis quando a refatoração abrange mais de um módulo ou exige mais de uma sessão. Use-os para registrar exclusões, atualizações de padrões, contratos que precisaram permanecer estáveis e o que ainda ficou para depois.

## Use habilidades para padrões recorrentes

[Habilidades](/pt-BR/codex/build-skills) são úteis quando as mesmas regras de limpeza se repetem em diferentes repositórios, serviços ou equipes. Quando disponíveis, use habilidades específicas de cada framework, inclua habilidades de segurança e CI em limpezas arriscadas e crie uma habilidade para a equipe quando tiver uma lista de verificação que já se mostrou eficaz para remover código não utilizado, extrair módulos ou modernizar padrões legados.
Se você acabar executando a mesma etapa de modernização em mais de uma base de código, o Codex pode ajudar a transformar a primeira etapa bem-sucedida em uma habilidade reutilizável.
