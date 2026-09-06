<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/native-macos-apps -->

## Crie a estrutura inicial do aplicativo e o ciclo de compilação

Para um novo aplicativo para Mac, peça primeiro ao Codex que escolha o modelo de cena adequado: `WindowGroup`, `Window`, `Settings`, `MenuBarExtra` ou `DocumentGroup`. Assim, o aplicativo será nativo para desktop desde a primeira iteração, em vez de evoluir a partir de uma `ContentView` no estilo do iOS.

Mantenha o ciclo de execução com foco no shell. Em projetos do Xcode, use `xcodebuild`. Em aplicativos baseados em pacotes, use `swift build` e o script local ao projeto `script/build_and_run.sh`, que encerra o processo antigo, compila o aplicativo, inicia o novo artefato e pode, opcionalmente, expor logs ou telemetria.

Se um aplicativo SwiftPM puro tiver uma GUI, empacote-o e inicie-o como um `.app`, em vez de executar diretamente o executável não empacotado. Isso evita problemas com a ausência do aplicativo no Dock, a ativação e a identidade do bundle durante a validação local.

## Aproveite as Habilidades

Adicione o [plug-in Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) quando o trabalho passar a envolver mais aspectos específicos do desktop. Ele abrange ciclos de compilação e depuração com foco no shell, empacotamento de aplicativos SwiftPM, padrões nativos de cenas e janelas no SwiftUI, interoperabilidade com AppKit, logs unificados, triagem de testes e fluxos de trabalho de assinatura e notarização.

Para saber mais sobre como instalar e usar Plug-ins e Habilidades, consulte a [documentação de Plug-ins](/pt-BR/codex/plugins) e a [documentação de Habilidades](/pt-BR/codex/build-skills).

## Crie uma interface nativa para desktop

Prefira as convenções do Mac aos padrões de navegação do iOS. Use `NavigationSplitView` em layouts de barra lateral/detalhes, cenas `Settings` explícitas para preferências, barras de ferramentas e comandos para ações fáceis de encontrar e itens extras da barra de menus para utilitários leves e sempre disponíveis.

Comece usando materiais do sistema, cores semânticas e controles padrão. Só adicione estilos de janela personalizados, regiões para arrastar ou superfícies Liquid Glass quando o produto precisar de uma aparência própria no desktop.

Se o SwiftUI chegar perto, mas não oferecer tudo de que você precisa, adicione a menor ponte possível com AppKit. Bons exemplos incluem painéis de abrir/salvar, controle do primeiro respondente, validação de menus, casos extremos de arrastar e soltar e uma `NSView` encapsulada para um controle especializado.

## Depure, teste e prepare para distribuir

Para analisar o comportamento em tempo de execução, peça ao Codex que adicione alguns eventos de `Logger` em pontos como a abertura de janelas, a seleção na barra lateral, a execução de comandos de menu ou a sincronização em segundo plano. Depois, verifique esses eventos com `log stream` após iniciar o aplicativo.

Para testes com falha, peça ao Codex que execute primeiro o menor escopo útil de `xcodebuild test` ou `swift test` e classifique se o problema é de compilação, uma falha de asserção, um crash, uma falha intermitente ou um problema de ambiente ou configuração.

Quando o trabalho passar da iteração local para a distribuição, peça ao Codex que prepare tanto um fluxo de arquivamento manual no Xcode quanto um fluxo de arquivamento e notarização via script, para que a distribuição seja reproduzível. Peça que ele inspecione o bundle do aplicativo, os entitlements e o runtime reforçado com `codesign` e `plutil`, e use a [App Store Connect CLI](https://asccli.sh/) quando você também quiser fazer os envios pelo terminal.

## Exemplo de prompt

## Dicas práticas

### Mantenha as cenas explícitas

Modele a janela principal, a janela de configurações, as janelas utilitárias e os itens extras da barra de menus como cenas raiz separadas, em vez de ocultar o aplicativo inteiro em uma única visualização enorme.

### Deixe a interface padrão do sistema fazer mais do trabalho

Antes de criar barras laterais, barras de ferramentas ou materiais personalizados, verifique se as APIs padrão de cenas e janelas do SwiftUI já oferecem o comportamento de Mac que você deseja.

### Mantenha a integração com AppKit bem delimitada

Use `NSViewRepresentable`, `NSViewControllerRepresentable` ou um componente auxiliar específico para `NSWindow` a fim de suprir um único recurso de desktop ausente, mas mantenha o SwiftUI como fonte da verdade para a seleção e o estado do aplicativo.

### Valide assinatura e notarização independentemente do sucesso da compilação local

Uma inicialização local bem-sucedida não comprova que o aplicativo esteja assinado nem pronto para notarização. Mantenha um fluxo manual de arquivamento no Xcode para verificações pontuais de lançamento, adicione um fluxo de arquivamento e notarização via script para uma distribuição reproduzível e execute verificações com `codesign` e `plutil` quando a tarefa envolver distribuição, não apenas iteração local.
