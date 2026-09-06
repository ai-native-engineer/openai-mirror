<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/native-ios-apps -->

## Estruture o aplicativo e configure o ciclo de build

Para projetos do zero, comece apenas com prompts. Peça ao Codex para criar a estrutura inicial de um aplicativo iOS em SwiftUI e escrever um pequeno script de build e inicialização que você possa vincular a uma ação `Build` em um [ambiente local](/pt-BR/codex/environments/local-environment).

Priorize a CLI no ciclo. A ferramenta `xcodebuild` da Apple pode listar esquemas e executar pelo terminal ações de compilação, teste, arquivamento, `build-for-testing` e `test-without-building`, permitindo que o Codex permaneça em um ciclo agêntico em vez de alternar para a interface gráfica do Xcode.

Se você quiser um gerador de projetos mais organizado e se sentir à vontade com ferramentas de terceiros, o [Tuist](https://tuist.dev/) é um bom próximo passo. Ele gera e compila projetos do Xcode sem precisar da interface gráfica e ainda permite que o Codex compile e inicie o aplicativo pelo terminal.

Use o [XcodeBuildMCP](https://www.xcodebuildmcp.com/) quando estiver trabalhando em um projeto completo do Xcode e precisar de automação mais avançada. É nesse ponto que esquemas, targets, controle do simulador, capturas de tela, logs e interação com a UI passam a ser relevantes o bastante para que simples comandos do shell já não resolvam tudo.

## Aproveite as habilidades

Na primeira etapa, muitas vezes você não precisa de uma habilidade nem de um servidor MCP. Adicione habilidades quando o trabalho ficar mais especializado ou quando quiser aplicar convenções mais rigorosas de SwiftUI durante a execução.

- [SwiftUI expert](https://github.com/AvdLee/SwiftUI-Agent-Skill) é uma habilidade versátil e sólida para SwiftUI, que já incorpora muitas práticas recomendadas.
- [SwiftUI Pro](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/main/swiftui-pro/SKILL.md) é uma habilidade abrangente de revisão de SwiftUI para APIs modernas, manutenção, acessibilidade e desempenho.

- [Liquid Glass expert](https://github.com/Dimillian/Skills/blob/main/swiftui-liquid-glass/SKILL.md) ajuda o Codex a adotar as novas APIs do Liquid Glass no iOS 26 e ajustar componentes personalizados para que se alinhem ao design mais recente do sistema.
- [SwiftUI performance](https://github.com/Dimillian/Skills/blob/main/swiftui-performance-audit/SKILL.md) é útil quando uma funcionalidade parece lenta ou o caminho de atualização de uma view SwiftUI parece suspeito. Essa habilidade procura erros comuns de SwiftUI e gera um relatório priorizado com o que corrigir e onde obter os maiores ganhos.
- [Swift concurrency expert](https://github.com/Dimillian/Skills/blob/main/swift-concurrency-expert/SKILL.md) é útil quando erros enigmáticos e avisos do compilador começam a atrapalhar a alteração que você quer fazer. No GPT-5.6 Terra, talvez você precise dessa habilidade com menos frequência, mas ela continua útil quando os diagnósticos de concorrência em Swift ficam ruidosos.
- [SwiftUI view refactor](https://github.com/Dimillian/Skills/blob/main/swiftui-view-refactor/SKILL.md) ajuda a manter os arquivos menores e a deixar o código SwiftUI mais consistente em todo o repositório.
- [SwiftUI patterns](https://github.com/Dimillian/Skills/blob/main/swiftui-ui-patterns/SKILL.md) ajuda a adotar padrões previsíveis de arquitetura com `@Observable` e `@Environment` à medida que o aplicativo cresce.

Para saber mais sobre como instalar e usar habilidades, consulte nossa [documentação sobre habilidades](/pt-BR/codex/build-skills).

## Itere

Quando tiver uma primeira versão funcionando, ou se estiver começando com um projeto existente, você poderá iniciar as iterações na UI ou no comportamento.

Nessa etapa, especifique o que você quer alterar e como.

Deixe isso explícito no prompt: informe ao Codex se ele está trabalhando em um repositório novo ou em um projeto existente do Xcode, quais dispositivos iOS ou destinos de implantação devem continuar funcionando e qual ciclo de validação você espera.

### Exemplo de prompt

Por exemplo, se quiser adicionar uma funcionalidade a um aplicativo existente, você pode pedir ao Codex uma alteração como esta:

## Dicas práticas

### Comece pelo básico

Para projetos do zero, comece apenas com prompts. Peça ao Codex para criar a estrutura inicial de um aplicativo SwiftUI e escrever um pequeno script de build e inicialização que você possa vincular a uma ação `Build` em um [ambiente local](/pt-BR/codex/environments/local-environment). Nessa primeira etapa, muitas vezes você não precisa de nenhuma habilidade nem de um servidor MCP.

### Use um ciclo de validação pequeno e confiável

Após cada alteração, peça ao Codex que execute o comando mais específico que realmente comprove o contrato afetado. Depois, amplie para builds mais abrangentes. Assim, o Codex continua rápido, sem tratar um build completo do aplicativo como requisito para toda edição.

### Priorize a CLI no ciclo de desenvolvimento

Priorize a CLI no ciclo de desenvolvimento. A ferramenta `xcodebuild` da Apple pode listar esquemas e executar pelo terminal as ações build, test, archive, `build-for-testing` e `test-without-building`, permitindo que o Codex permaneça em um ciclo agêntico em vez de precisar alternar para a interface gráfica do Xcode.

### Aproveite o XcodeBuildMCP

Use o XcodeBuildMCP assim que estiver trabalhando em um projeto completo do Xcode e precisar de automação mais avançada. É nesse ponto que esquemas, targets, controle do simulador, capturas de tela, logs e interação com a interface passam a ser importantes o suficiente para que simples comandos de shell já não deem conta de tudo.
