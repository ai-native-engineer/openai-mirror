<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/frontend-designs -->

## Introdução

Se você tem capturas de tela, um breve briefing de design ou algumas referências para se inspirar, o Codex pode transformar esse material em uma UI responsiva sem ignorar os padrões já estabelecidos no projeto.

Com a habilidade do Playwright, o Codex pode abrir o aplicativo em um navegador real, comparar a implementação com suas capturas de tela em diferentes tamanhos de tela e ajustar o layout ou o comportamento até que o resultado fique mais próximo do objetivo.

## Comece pelas referências

Forneça ao Codex as referências mais claras que você tiver para a UI desejada. Uma única captura de tela pode ser suficiente para uma tarefa de escopo limitado, mas o direcionamento fica mais claro quando você inclui vários estados, como layouts para desktop e dispositivos móveis, estados ao passar o cursor ou de seleção e telas vazias ou de carregamento relevantes.

As referências não precisam ser materiais de design perfeitos. Elas só precisam mostrar com clareza suficiente a hierarquia, o espaçamento e o direcionamento desejados, para que o Codex não precise fazer suposições.

## Seja específico

Quanto mais específico você for sobre os padrões de interação esperados e o estilo desejado, melhor será o resultado.
O modelo tende a adotar os padrões e estilos mais comuns. Por isso, se as referências não deixarem claro que você deseja algo diferente, a UI poderá parecer genérica.
Quanto mais informações você fornecer — seja com outras referências para inspiração, seja com instruções mais específicas —, maior será a chance de obter uma UI que se destaque.

## Prepare o sistema de design

O Codex funciona melhor quando o repositório de destino já tem uma camada de componentes bem definida. O Codex pode usar automaticamente os componentes e o sistema de design que você já tem, em vez de recriá-los do zero.

Se necessário, por exemplo, se você não estiver usando uma stack padrão, informe ao Codex quais primitivas reutilizar, onde ficam os tokens e quais são os padrões canônicos do repositório para botões, campos de entrada, cartões, tipografia e ícones.

Se você partir de uma base de código existente, o Codex provavelmente entenderá por conta própria como usar seus componentes e seu sistema de design. Se estiver começando do zero, porém, é recomendável explicitar essas informações.

Peça ao Codex que trate as capturas de tela como um objetivo visual, mas implemente esse objetivo com os utilitários, wrappers de componentes, sistema de cores, escala tipográfica, tokens de espaçamento, roteamento, gerenciamento de estado e padrões de busca de dados que o projeto realmente usa.

## Use o Playwright

O Playwright é uma ótima ferramenta para ajudar o Codex a refinar a UI. Com ele, o Codex pode abrir o aplicativo em um navegador real, comparar a implementação com as capturas de tela fornecidas e fazer ajustes no layout ou no comportamento.

Ele pode redimensionar a janela do navegador para diferentes tamanhos de tela e verificar o layout em diferentes breakpoints.

Verifique se a habilidade interativa do Playwright está ativada no Codex. Para saber mais, consulte a [documentação sobre Habilidades](/pt-BR/docs/build-skills).

## Itere

A primeira versão já deve seguir a direção geral das capturas de tela. Para layouts ou interações complexas, ou para uma UI com muitas animações, espere algumas rodadas de ajustes.

Peça ao Codex que compare a implementação com as capturas de tela, e não apenas que verifique se a página compila. Em caso de conflito, o Codex deve priorizar os tokens do sistema de design do repositório e fazer apenas os ajustes mínimos de espaçamento ou tamanho necessários para preservar a aparência geral do design.

Use capturas de tela adicionais ou observações breves se elas ajudarem a esclarecer estados que não ficam claros em uma única imagem.

### Sugestão de prompt de acompanhamento
