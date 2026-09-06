<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/make-granular-ui-changes -->

## Introdução

Quando você já tem um aplicativo e quer iterar rapidamente na interface, pode usar `gpt-5.3-codex-spark` para fazer alterações pequenas e pontuais na interface.
O Codex-Spark é o nosso modelo mais rápido, otimizado para iterações de código quase instantâneas e em tempo real.

O melhor é manter um ciclo curto: uma observação visual, uma edição pontual, uma verificação no navegador e, depois, a próxima observação.

  Você pode usar o [modelo Codex Spark](/pt-BR/codex/models) para esta tarefa. Ele está
  disponível nos planos Pro.

## Escolha seu modelo

Para iterar rapidamente na interface, comece com `gpt-5.3-codex-spark`, se tiver acesso a ele. Ele é menos capaz do que nossos modelos de uso geral, mas foi projetado para iterações de código em tempo real. Se não tiver acesso a ele, use <code>{RECOMMENDED_MODEL_REFERENCES.latestMainlineModel.slug}</code> com o esforço de raciocínio definido como `medium` ou `low`.

Esse equilíbrio entre capacidade e velocidade é útil para alterações pontuais na interface. Em geral, você não precisa do modelo com o raciocínio mais profundo para mover um botão, ajustar um breakpoint ou alterar o estado de um componente. Você precisa de um modelo que responda rapidamente, entenda o código local, edite o arquivo certo e possa repetir o ciclo sem tornar cada iteração trabalhosa.

## Fluxo de desenvolvimento

1. Abra o aplicativo existente e exiba a rota ou o componente relevante.
2. Destaque o chat ativo do Codex em uma [janela flutuante](/codex/reference/settings#keep-a-chat-near-your-work) e mantenha-a perto do navegador, do editor ou da prévia do design enquanto trabalha.
3. Peça ao Codex uma alteração específica na interface por vez. Inclua a rota, o viewport, a captura de tela atual, a captura de tela desejada ou a observação exata sobre o produto, se houver.
4. Peça ao Codex que inspecione a implementação atual, faça a menor alteração justificável e preserve os componentes, tokens, primitivas de layout e fluxo de dados já existentes no aplicativo.
5. Revise o resultado e envie o próximo ajuste pontual no mesmo chat.

## Escreva prompts curtos

Os prompts para alterações pontuais na interface devem ser diretos e bem delimitados. Um bom prompt identifica a área da interface, a alteração desejada e a validação esperada.

Se o resultado estiver quase certo, mantenha o mesmo nível de especificidade no prompt de acompanhamento:

## Quando reduzir o ritmo

Não continue com o ciclo rápido se a tarefa deixar de ser pontual. Mude para um modelo mais potente e um prompt mais elaborado quando a alteração exigir uma refatoração ampla, uma nova primitiva do sistema de design, um comportamento de acessibilidade não trivial ou uma decisão de produto que afete mais de uma tela.

A iteração rápida na interface funciona melhor quando o Codex ajusta uma área que já conhece, em vez de reformular o aplicativo do zero.
