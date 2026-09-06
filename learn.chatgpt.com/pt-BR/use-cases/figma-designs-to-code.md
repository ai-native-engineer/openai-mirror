<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/figma-designs-to-code -->

## Introdução

Quando você tem uma seleção exata no Figma, o Codex pode transformá-la em uma interface refinada sem desconsiderar os padrões já estabelecidos no projeto.

Com a habilidade do Figma, o Codex pode usar o servidor MCP do Figma para extrair o contexto estruturado do design, as variáveis, os recursos e a variante exata que deve implementar.

Com a habilidade interativa do Playwright, o Codex pode abrir o aplicativo em um navegador real, comparar a implementação com a referência do Figma e refinar o layout ou o comportamento até aproximar o resultado do objetivo.

## Configure seu projeto do Figma

Quanto mais organizado estiver seu arquivo do Figma, melhor será a primeira implementação. Para melhorar a transição do design para o desenvolvimento:

- Use variáveis ou tokens de design sempre que possível, sobretudo para cores, tipografia e espaçamento
- Crie componentes para elementos reutilizáveis da interface, em vez de repetir camadas desvinculadas
- Use o layout automático sempre que possível, em vez do posicionamento manual
- Dê nomes claros aos frames e às camadas para facilitar a identificação da tela principal, do estado e das variantes
- Mantenha no arquivo os ícones e as imagens reais sempre que possível, para que o Codex não precise adivinhar

Isso fornece ao Codex uma estrutura mais adequada para gerar uma interface robusta e pronta para produção.

## Seja específico

Quanto mais detalhes você fornecer sobre os padrões de interação esperados e o estilo desejado, melhor será o resultado.

Se um estado, breakpoint ou interação for importante, deixe isso claro. Se o arquivo contiver várias variantes parecidas, informe ao Codex qual delas deve ser considerada a referência principal.

Quanto mais claro você for sobre o que precisa corresponder exatamente e quando as convenções do repositório devem prevalecer, mais fácil será para o Codex equilibrar essas prioridades da forma certa.

## Prepare o sistema de design

O Codex funciona melhor quando o repositório de destino já tem uma camada de componentes bem definida. Ele pode usar automaticamente os componentes e o sistema de design existentes, em vez de recriá-los do zero.

Se considerar necessário, informe ao Codex quais primitivas devem ser reutilizadas, onde ficam seus tokens e quais são os padrões canônicos do repositório para botões, campos de entrada, cards, tipografia e ícones.

Considere a saída do MCP do Figma, que muitas vezes se parece com React usando Tailwind, uma referência estrutural, não o estilo final do código. Peça ao Codex que adapte essa saída aos utilitários, wrappers de componentes, sistema de cores, escala tipográfica, tokens de espaçamento, roteamento, gerenciamento de estado e padrões de obtenção de dados realmente usados no projeto.

## Fluxo de trabalho

### Comece com uma seleção do Figma

Copie o link do frame, componente ou variante exata do Figma que você quer implementar. O fluxo do MCP do Figma é baseado em links, por isso o link precisa apontar para o node exato, não para um frame pai próximo.

### Instrua o Codex a usar o Figma

O Figma deve orientar a implementação inicial. Peça ao Codex que siga o fluxo do MCP do Figma antes de começar a implementar.

Inclua estes itens no prompt:

Quando a implementação inicial estiver pronta, o Codex usará o Playwright para verificar a interface em um navegador real e corrigir eventuais divergências restantes na aparência ou na interação.
