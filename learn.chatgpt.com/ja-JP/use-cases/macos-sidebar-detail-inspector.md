<!-- source: https://learn.chatgpt.com/ja-JP/use-cases/macos-sidebar-detail-inspector -->

## Mac のシーンモデルから開始

このユースケースでは、タッチ操作優先のスタックをそのまま引き延ばすのではなく、デスクトップ向けに設計されたと感じられる Mac アプリシェルへアプリのアイデアを発展させます。まず Codex にシーンモデルを選ばせ、次に、安定したサイドバー選択、詳細表示領域、補助的なコントロールやメタデータ用のインスペクタを中心にメインウィンドウを設計するよう依頼します。

![サイドバーで項目が選択され、詳細ペインにコンテンツが表示された Mac ネイティブのサイドバー／詳細アプリシェル](/images/codex/use-cases/macos-sidebar-detail-inspector.png)

Codex にこのデスクトップ構造を適用させ、ビルド／実行ループをシェル起点で進めたい場合は、[Build macOS Apps プラグイン](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) を使用します。同プラグインの macOS SwiftUI パターンスキルは、シーン設計、サイドバー、インスペクタ、コマンド、設定のほか、SwiftUI だけでは Mac 固有の動作を実現しきれない場合の小規模な AppKit ブリッジにも適しています。

## サイドバー、詳細ペイン、インスペクタの構築

永続的なナビゲーションと安定した選択項目が適している機能では、`NavigationSplitView` を優先します。サイドバーの行はネイティブかつ軽量に保ち、サイドバーにはシステム標準の背景を使用し、カスタムカードや密度の高いメタデータは詳細ペインまたはインスペクタに配置します。

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

アプリで分割ビューの特殊なサイズ調整、低レベルのウィンドウ連携、レスポンダーチェーンの独自動作が必要な場合は、SwiftUI シェルをそのまま維持し、その不足を補うために必要な最小限の AppKit ブリッジだけを追加するよう Codex に依頼します。

## デスクトップ層へのコマンド、ツールバー、ショートカットの配置

Mac ユーザーが重要なアクションをメニューバー、ツールバー、キーボードショートカットから見つけられるようにします。デスクトップユーザーがジェスチャーでしか使えないコントロールを探し回らずに済むよう、シーンレベルの `commands`、状況に応じたメニュー項目、ツールバーボタンのいずれからも同じアプリアクションを呼び出せるよう Codex に依頼します。

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

コマンドを現在の詳細項目に適用する必要がある場合は、`FocusedValue`、シーン状態、または明示的な選択状態を使用します。ショートカットが複数の場所で登録される場合は、アプリ内のコマンド経路を 1 つに明確化できるよう、管理主体を集約するよう Codex に依頼します。

## 環境設定は `Settings` で管理

アプリの環境設定には専用の `Settings` シーンを使用し、継続的に保持するユーザー設定は `@AppStorage` で永続化します。通常は、メインコンテンツウィンドウ内に設定画面をプッシュ表示するより、この方が Mac に適しています。

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

## アプリのコンセプトを提示してからシェルを検証

このページは、プロンプトにアプリのコンセプト、主要なコンテンツオブジェクト、主要なアクションを明記し、そのワークフローを軸にデスクトップシェルを先に構築するよう Codex に依頼すると、最も効果的です。エージェントには小規模なビルド／実行チェックを行わせ、シーン構造、コマンドの接続、状態の所有関係、AppKit で補完した箇所を要約させます。

## 実践的なヒント

### サイドバーをネイティブに維持

サイドバーの各行は、アイコン 1 つ、タイトル 1 行、短い補足行を多くても 1 行にします。情報量の多いカード、カウンター、メタデータは詳細ペインかインスペクタに移し、サイドバーのリストを見渡しやすく保ちます。

### メインスタック内への設定の埋め込みを回避

ユーザー設定がアプリ全体に影響する場合は、別の設定画面をプッシュ表示するのではなく、そのコントロールを `Settings` に配置して `@AppStorage` で永続化し、アプリメニューから開けるよう Codex に依頼します。

### デスクトップ固有の不足だけを AppKit で補完

機能に開く／保存パネル、ファーストレスポンダーの制御、カスタム `NSView` が必要な場合は、ウィンドウ全体を AppKit で書き直すのではなく、SwiftUI が所有する状態モデルの境界部分だけを補う小規模な手段として AppKit を使用します。
