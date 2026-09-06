<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/macos-sidebar-detail-inspector -->

## Comece pelo modelo de cena para Mac

Este caso de uso mostra como transformar a ideia de um aplicativo em uma estrutura para Mac que pareça criada para desktop, não apenas ampliada a partir de uma pilha voltada primeiro ao toque. Peça ao Codex que escolha primeiro o modelo de cena e depois projete a janela principal em torno de uma seleção estável na barra lateral, uma área de detalhes e um inspetor para controles ou metadados secundários.

![Uma estrutura de aplicativo nativa para Mac, com um item selecionado na barra lateral e conteúdo no painel de detalhes](/images/codex/use-cases/macos-sidebar-detail-inspector.png)

Use o [plug-in Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) quando quiser que o Codex aplique essa estrutura de desktop e mantenha o ciclo de compilação/execução priorizando o shell. A habilidade de padrões do SwiftUI para macOS desse plug-in é uma boa opção para projetar cenas, barras laterais, inspetores, comandos e configurações, além de pequenas pontes com AppKit quando o SwiftUI não cobre por completo algum comportamento específico do Mac.

## Crie uma barra lateral, um painel de detalhes e um inspetor

Prefira `NavigationSplitView` quando o recurso se beneficiar de navegação persistente e de um item selecionado estável. Mantenha os itens da barra lateral nativos e simples, use nela os planos de fundo do sistema e reserve cartões personalizados ou metadados densos para o painel de detalhes ou o inspetor.

```swift
struct LibraryRootView: View {
  @SceneStorage("LibraryRootView.selection") private var selection: Item.ID?
  @SceneStorage("LibraryRootView.showInspector") private var showInspector = true

  var body: some View {
    NavigationSplitView {
      List(selection: $selection) {
        ForEach(items) { item in
          Label(item.title, systemImage: item.systemImage)
            .tag(item.id)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Library")
    } detail: {
      ItemDetailView(selection: selection)
        .inspector(isPresented: $showInspector) {
          ItemInspectorView(selection: selection)
        }
    }
  }
}

Se o aplicativo precisar de dimensionamento incomum dos painéis, coordenação de janelas em baixo nível ou comportamento personalizado na cadeia de resposta, peça ao Codex que mantenha intacta a estrutura do SwiftUI e adicione apenas a menor ponte de AppKit necessária para suprir essa lacuna específica.

## Coloque comandos, barras de ferramentas e atalhos na camada de desktop

Os usuários de Mac devem conseguir encontrar ações importantes na barra de menus, na barra de ferramentas e nos atalhos de teclado. Peça ao Codex que associe `commands` no nível da cena, itens de menu sensíveis ao contexto e botões da barra de ferramentas às mesmas ações do aplicativo, para que os usuários de desktop não precisem procurar controles disponíveis apenas por gestos.

```swift
@main
struct LibraryApp: App {
  var body: some Scene {
    WindowGroup {
      LibraryRootView()
    }
    .commands {
      CommandMenu("Library") {
        Button("New Item") {
          // Create a new item.
        }
        .keyboardShortcut("n")

        Button("Toggle Inspector") {
          // Route this command to the focused window or selected item state.
        }
        .keyboardShortcut("i", modifiers: [.command, .option])
      }
    }

    Settings {
      LibrarySettingsView()
    }
  }
}

Use `FocusedValue`, o estado da cena ou um estado de seleção explícito quando um comando precisar ser aplicado ao item de detalhes atual. Se um atalho puder ser registrado em vários lugares, peça ao Codex que centralize a responsabilidade por ele para que o aplicativo tenha um único fluxo claro para comandos.

## Mantenha as preferências em `Settings`

Para as preferências do aplicativo, use uma cena `Settings` dedicada e mantenha as escolhas do usuário de forma persistente com `@AppStorage`. Em geral, isso é mais adequado para Mac do que empilhar uma tela de configurações dentro da janela principal de conteúdo.

```swift
struct LibrarySettingsView: View {
  @AppStorage("showItemMetadata") private var showItemMetadata = true

  var body: some View {
    TabView {
      Form {
        Toggle("Show Item Metadata", isOn: $showItemMetadata)
      }
      .tabItem { Label("General", systemImage: "gearshape") }
    }
    .frame(width: 460, height: 260)
    .scenePadding()
  }
}

## Descreva o conceito do aplicativo no prompt e depois valide a estrutura

Esta página funciona melhor quando seu prompt descreve o conceito do aplicativo, os principais objetos de conteúdo e as ações primárias e, em seguida, pede ao Codex que primeiro crie a estrutura de desktop em torno desse fluxo de trabalho. Peça ao agente para executar uma verificação simples de compilação/execução e resumir a estrutura das cenas, a configuração dos comandos, a responsabilidade pelo estado e qualquer lacuna que tenha precisado contornar por meio de uma ponte de AppKit.

## Dicas práticas

### Mantenha a barra lateral nativa

Use um ícone, uma linha de título e, no máximo, uma linha secundária curta em cada item da barra lateral. Transfira cartões mais elaborados, contadores e metadados para o painel de detalhes ou o inspetor, para que a lista da barra lateral continue fácil de examinar.

### Não esconda as configurações na pilha principal

Se uma preferência do usuário afetar todo o aplicativo, peça ao Codex que coloque esse controle em `Settings` com `@AppStorage` e disponibilize um ponto de entrada no menu do aplicativo, em vez de criar outra tela de configurações empilhada.

### Reserve o AppKit para lacunas pontuais do desktop

Se o recurso exigir painéis de abrir/salvar, controle do first responder ou uma `NSView` personalizada, use AppKit apenas para uma pequena integração em torno de um modelo de estado controlado pelo SwiftUI, em vez de reescrever toda a janela em AppKit.
