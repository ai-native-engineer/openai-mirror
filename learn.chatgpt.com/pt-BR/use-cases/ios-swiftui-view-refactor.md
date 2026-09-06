<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/ios-swiftui-view-refactor -->

## Refatore uma tela sem alterar o que ela faz

Este caso de uso se aplica quando um arquivo SwiftUI cresceu até virar uma tela gigantesca e qualquer pequena edição parece arriscada. O objetivo não é reformular o recurso nem inventar uma nova arquitetura. Peça ao Codex que preserve o comportamento e o layout e divida a tela em pequenas subviews com um fluxo de dados explícito, para facilitar a revisão da próxima alteração.

Use o [plug-in Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) para esse tipo de organização. A habilidade de refatoração de views do SwiftUI incluída nele adota uma abordagem bem definida e útil: priorize MV em vez de MVVM, mantenha a lógica de negócios em serviços ou modelos, use primeiro o estado local da view e as dependências do ambiente e só mantenha um view model quando o recurso realmente precisar de um.

## O que pedir ao Codex

Comece indicando um arquivo de tela específico e pedindo ao Codex que preserve o comportamento enquanto melhora a estrutura. Vale a pena incluir estas regras de refatoração diretamente no prompt:

- Reorganize o arquivo para facilitar a leitura, de cima para baixo, das dependências do ambiente, das propriedades armazenadas, do estado computado que não representa views, de `init`, de `body`, das funções auxiliares de view e dos métodos auxiliares.
- Extraia seções relevantes para tipos `View` dedicados, com um pequeno conjunto de entradas explícitas, propriedades `@Binding` e callbacks.
- Use poucos auxiliares computados do tipo `some View` e mantenha-os pequenos. Não reconstrua uma tela gigantesca como uma longa lista de fragmentos de view privados e computados.
- Retire de `body` as ações de botão não triviais e os efeitos colaterais e transfira a lógica de negócios real para serviços ou modelos.
- Mantenha estável a árvore da view raiz. Prefira condicionais locais em seções ou modificadores a ramificações `if/else` no nível superior que substituem telas inteiras.
- Ajuste a responsabilidade pelo estado no Observation à medida que avança. Para modelos raiz `@Observable` no iOS 17 ou posterior, a view responsável deve armazená-los em `@State`; use wrappers observáveis legados somente quando o destino de implantação exigir isso.

## Peça um ciclo curto de validação

Refatorações que preservam o comportamento devem vir acompanhadas de comprovação. Peça ao Codex que execute a menor verificação possível de build, pré-visualização, teste ou simulador que exercite a tela após cada extração relevante. Depois, peça que resuma o que mudou na estrutura e o que foi mantido intencionalmente.

## Dicas práticas

### Primeiro divida; depois discuta a arquitetura

Se uma tela estiver grande demais, peça ao Codex que extraia as views de cada seção antes de introduzir uma nova camada de abstração. Uma árvore de views mais curta e explícita muitas vezes elimina por completo a necessidade de adicionar um view model.

### Passe a menor interface possível para cada subview

Prefira valores `let`, propriedades `@Binding` e callbacks com uma única finalidade em vez de passar o modelo completo da view pai para cada view filha. Isso facilita gerar uma pré-visualização de cada seção extraída e reduz o risco de voltar a acoplá-la acidentalmente à tela inteira.

### Peça ao Codex que destaque o que não foi alterado de propósito

Para uma refatoração segura, é útil que o Codex liste explicitamente o que não foi alterado: regras de negócios, comportamento da navegação, persistência, semântica de analytics e layout visível para o usuário. Isso agiliza muito a revisão.
