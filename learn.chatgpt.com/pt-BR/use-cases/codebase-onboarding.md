<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/codebase-onboarding -->

## Introdução

Quando você começa a trabalhar em um repositório ou se depara com um recurso que não conhece, o Codex pode ajudar você a se situar antes de começar a alterar o código. O objetivo não é apenas obter uma visão geral, mas mapear o fluxo da requisição, entender as responsabilidades de cada módulo e identificar os próximos arquivos que vale a pena ler.

## Como usar

Se você ainda não conhece um projeto, pode começar simplesmente pedindo ao Codex que explique toda a base de código:

Se você precisar implementar um novo recurso em uma base de código existente, pode pedir ao Codex que explique uma área específica do sistema. Quanto mais bem delimitado for o pedido, mais concreta será a explicação:

1. Forneça ao Codex os arquivos e diretórios relevantes ou indique a área funcional que você está tentando entender.
2. Peça que ele rastreie o fluxo da requisição e explique quais módulos são responsáveis pela lógica de negócios, pelo transporte, pela persistência ou pela interface.
3. Antes de editar qualquer coisa, pergunte onde ocorrem a validação, os efeitos colaterais ou as transições de estado.
4. Por fim, pergunte quais arquivos você deve ler em seguida e onde estão os pontos de risco.

Uma resposta útil para a ambientação deve fornecer um mapa concreto, não apenas uma lista de nomes de arquivos. Ao final, o Codex deve ter explicado o fluxo principal, destacado os pontos de risco e indicado quais arquivos consultar em seguida ou quais verificações são importantes antes de você começar a editar.

## Próximas perguntas

Depois que o Codex fornecer uma análise inicial, continue fazendo perguntas até que a explicação seja específica o suficiente para você se sentir seguro para fazer a primeira alteração. Boas perguntas complementares geralmente fazem com que ele explicite as premissas, as dependências ocultas e as verificações necessárias após uma alteração.

- Qual módulo é responsável pela lógica de negócios propriamente dita e qual é responsável pela camada de transporte ou pela interface?
- Onde ocorre a validação e quais premissas são impostas nesse ponto?
- Quais arquivos relacionados ou tarefas em segundo plano podem passar despercebidos se eu alterar esse fluxo?
- Quais testes ou verificações devo executar depois de editar essa área?
