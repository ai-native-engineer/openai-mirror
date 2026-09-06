<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/code-migrations -->

## Introdução

Ao migrar de uma pilha tecnológica para outra, você pode usar o Codex para mapear e executar uma migração controlada: roteamento, modelos de dados, configuração, autenticação, tarefas em segundo plano, ferramentas de build, implantação, testes ou até mesmo as próprias convenções da linguagem e do framework.

O Codex é útil nesse processo porque pode fazer um inventário do sistema legado, mapear conceitos antigos para novos e implementar a mudança em etapas, em vez de realizar uma enorme reescrita de uma só vez. Isso é importante ao deixar de usar um framework legado, migrar para um novo ambiente de execução ou substituir gradualmente uma pilha tecnológica por outra enquanto o produto precisa continuar funcionando.

## Como usar

1. Comece fazendo um inventário de tudo o que será afetado pela migração: pacotes legados, convenções do framework, roteamento, acesso a dados, autenticação, configuração, ferramentas de build, testes, premissas de implantação e todos os contratos externos que precisam ser preservados durante a migração.
2. Peça ao Codex para mapear os conceitos legados para a pilha tecnológica de destino e destacar o que não tiver equivalente direto.
3. Escolha uma estratégia incremental: camada de compatibilidade, migração módulo a módulo, ramificação por abstração ou substituição pelo padrão estrangulador, um limite por vez.
4. Mantenha o comportamento estável até que a própria migração imponha uma mudança visível e identifique explicitamente essas exceções.
5. Após cada etapa, execute a validação mínima capaz de comprovar a paridade: lint, verificação de tipos, testes direcionados, testes de contrato, testes de fumaça ou uma comparação lado a lado com o fluxo legado.
6. Após cada ponto de controle, analise o diff e os riscos de transição ainda existentes, em vez de aguardar a reescrita completa.

## Use os ExecPlans

Em nosso [guia prático de modernização de código](/cookbook/examples/codex/code_modernization), apresentamos os ExecPlans: documentos que permitem ao Codex acompanhar a limpeza como um todo, detalhar o estado final pretendido e registrar a validação após cada iteração.
Quando você pedir ao Codex para executar uma migração complexa, peça que ele crie um ExecPlan para cada parte do sistema, a fim de garantir que todas as decisões e escolhas de pilha tecnológica sejam registradas e possam ser revisadas depois.

## Combine com uma meta

Em etapas de migração que levam mais tempo, use uma [meta](/pt-BR/codex/use-cases/follow-goals) para orientar o Codex durante o trabalho. Defina a meta com um estado final claro, verificações de paridade, expectativas de reversão e uma condição de parada.
