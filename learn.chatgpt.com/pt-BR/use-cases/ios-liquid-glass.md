<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/ios-liquid-glass -->

## Comece com o iOS 26 como base

Primeiro, trate a adoção do Liquid Glass como um projeto de migração para iOS 26 e Xcode 26. Compile novamente o aplicativo com o SDK do iOS 26, verifique o que os controles padrão do SwiftUI fornecem automaticamente e só então peça ao Codex que reformule as partes personalizadas que ainda pareçam planas demais, carregadas demais ou desconectadas demais dos elementos da interface do sistema.

Se o aplicativo ainda oferecer suporte a versões anteriores do iOS, deixe essa restrição explícita desde o início. A habilidade de Liquid Glass no SwiftUI do [plug-in Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) deve usar `#available(iOS 26, *)` para condicionar o uso das novas APIs exclusivas do Liquid Glass e manter um caminho de fallback que continue legível em dispositivos mais antigos.

## Aproveite o plug-in para iOS

Use o [plug-in Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) quando quiser que o Codex combine alterações na UI do SwiftUI com validação no simulador. Para trabalhar com o Liquid Glass, peça ao Codex que audite um fluxo, migre um pequeno conjunto de superfícies, execute o resultado em um simulador do iOS 26 e capture telas antes de ampliar o escopo.

Esse plug-in inclui uma habilidade de Liquid Glass no SwiftUI com algumas diretrizes padrão simples que vale a pena incluir no prompt:

- Prefira APIs nativas como `glassEffect` e `GlassEffectContainer`, além de estilos de botão com efeito de vidro e transições com `glassEffectID`, a views personalizadas com desfoque.
- Aplique `.glassEffect(...)` depois dos modificadores de layout e visuais, para que o material envolva a forma final desejada.
- Agrupe os elementos de vidro relacionados em `GlassEffectContainer` quando várias superfícies aparecerem juntas.
- Use `.interactive()` apenas em botões, chips e controles que realmente respondem ao toque.
- Mantenha os formatos dos cantos, as cores e o espaçamento consistentes em toda a funcionalidade, em vez de misturar aplicações pontuais do efeito de vidro.
- Preserve um fallback sem efeito de vidro para destinos de implantação anteriores ao iOS 26.

Para saber mais sobre a instalação de plug-ins e habilidades, consulte nossa documentação sobre [plug-ins](/pt-BR/codex/plugins) e [habilidades](/pt-BR/codex/build-skills).

## Assista às sessões da WWDC

Estas sessões da WWDC25 são boas referências antes de você pedir ao Codex que refatore um fluxo real de produção:

- [Conheça o Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/)
- [Conheça o novo sistema de design](https://developer.apple.com/videos/play/wwdc2025/356/)
- [Crie um aplicativo SwiftUI com o novo design](https://developer.apple.com/videos/play/wwdc2025/323/)
- [Crie um aplicativo UIKit com o novo design](https://developer.apple.com/videos/play/wwdc2025/284/)
- [Novidades no SwiftUI](https://developer.apple.com/videos/play/wwdc2025/256/)

## Peça primeiro um plano de migração e depois uma etapa

As migrações para o Liquid Glass funcionam melhor quando o Codex trata separadamente "onde o efeito de vidro deve aparecer?" e "escreva todo o código agora". Primeiro, peça uma auditoria rápida; depois, deixe o agente implementar uma etapa autocontida com validação no simulador.

## Dicas práticas

### Não aplique o efeito de vidro a tudo

O Liquid Glass deve criar uma camada de controles bem definida sobre o conteúdo, não transformar cada cartão em um painel brilhante. Peça ao Codex que remova planos de fundo decorativos que entram em conflito com os materiais do sistema, preserve o conteúdo simples onde a legibilidade é mais importante e reserve as tonalidades para dar ênfase semântica ou destacar ações principais.

### Comece por um fluxo muito acessado

Uma tela raiz de aba, uma tela de detalhes, uma sheet, uma tela de pesquisa ou um fluxo de onboarding costuma ser um alvo inicial de migração melhor do que uma reformulação completa de todo o aplicativo. Isso facilita a revisão e deixa claro quais decisões do Liquid Glass devem se tornar padrões de componentes reutilizáveis.

### Revise cuidadosamente o comportamento de fallback

Se o destino de implantação for anterior ao iOS 26, peça ao Codex que mostre a implementação de fallback ao lado da versão com Liquid Glass. Essa etapa de revisão detecta regressões acidentais relacionadas à disponibilidade de APIs e evita lançar uma migração que só funciona no simulador mais recente.
