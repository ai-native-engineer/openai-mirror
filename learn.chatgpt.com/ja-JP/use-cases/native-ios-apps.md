<!-- source: https://learn.chatgpt.com/ja-JP/use-cases/native-ios-apps -->

## アプリとビルドループのひな形作成

新規開発では、まず通常のプロンプトから始めます。Codex に、スターター iOS SwiftUI アプリのひな形と、その環境の `Build` アクションに接続できる簡単なビルド・起動スクリプトを作成するよう依頼します（対象環境：[ローカル環境](/ja-JP/codex/environments/local-environment)）。

ビルドループは CLI 中心に保ちます。Apple の `xcodebuild` では、ターミナルからスキームを一覧表示し、build、test、archive、`build-for-testing`、`test-without-building` の各アクションを実行できます。そのため Codex は Xcode GUI を行き来せず、エージェント主導のループ内で作業を続けられます。

よりすっきりしたプロジェクトジェネレーターを求めていて、サードパーティ製ツールの使用に抵抗がなければ、[Tuist](https://tuist.dev/) が次の選択肢です。GUI を使わずに Xcode プロジェクトを生成してビルドでき、Codex は引き続きターミナルからアプリをビルドして起動できます。

一式そろった Xcode プロジェクトで、より高度な自動化が必要になったら、[XcodeBuildMCP](https://www.xcodebuildmcp.com/) を使用します。スキーム、ターゲット、シミュレーター制御、スクリーンショット、ログ、UI 操作が重要になり、通常のシェルコマンドだけでは十分でなくなる段階です。

## スキルの活用

最初の段階では、多くの場合、スキルも MCP サーバーも必要ありません。作業が専門的になったときや、より厳格な SwiftUI の規約を Codex の実行に組み込みたいときに、スキルを追加します。

- [SwiftUI expert](https://github.com/AvdLee/SwiftUI-Agent-Skill) は汎用性に優れた SwiftUI スキルで、多くのベストプラクティスがあらかじめ組み込まれています。
- [SwiftUI Pro](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/main/swiftui-pro/SKILL.md) は、最新 API、保守性、アクセシビリティ、パフォーマンスを幅広く確認できる SwiftUI レビュースキルです。

- [Liquid Glass expert](https://github.com/Dimillian/Skills/blob/main/swiftui-liquid-glass/SKILL.md) は、Codex が新しい iOS 26 Liquid Glass API を採用し、最新のシステムデザインに合うようカスタムコンポーネントを調整するのに役立ちます。
- [SwiftUI performance](https://github.com/Dimillian/Skills/blob/main/swiftui-performance-audit/SKILL.md) は、機能の動作が遅く感じられたり、SwiftUI のビュー更新経路に問題がありそうだったりする場合に役立ちます。SwiftUI でよくあるミスをスキャンし、修正箇所と最も効果の大きい改善点に優先順位を付けたレポートを生成します。
- [Swift concurrency expert](https://github.com/Dimillian/Skills/blob/main/swift-concurrency-expert/SKILL.md) は、不可解なエラーやコンパイラ警告が意図した変更の妨げになる場合に役立ちます。GPT-5.6 Terra では必要になる場面が少ないかもしれませんが、Swift の並行処理に関する診断メッセージが大量に出る場合には、引き続き有用です。
- [SwiftUI view refactor](https://github.com/Dimillian/Skills/blob/main/swiftui-view-refactor/SKILL.md) は、ファイルを小さく保ち、リポジトリ全体で SwiftUI コードの一貫性を高めるのに役立ちます。
- [SwiftUI patterns](https://github.com/Dimillian/Skills/blob/main/swiftui-ui-patterns/SKILL.md) は、アプリの成長に合わせて、予測しやすい `@Observable` と `@Environment` のアーキテクチャパターンを採用するのに役立ちます。

スキルのインストール方法と使い方について詳しくは、次のページを参照してください（[スキルのドキュメント](/ja-JP/codex/build-skills)）。

## 反復改善

ひとまず動くものができたら、または既存プロジェクトから始める場合は、UI や動作を反復的に改善できます。

この段階では、何をどのように変更したいのかを具体的に示してください。

プロンプトで前提を明確にし、対象が新規開発用リポジトリか既存の Xcode プロジェクトか、動作を維持すべき iOS デバイスやデプロイターゲットはどれか、どのような検証ループを期待するかを Codex に伝えてください。

### プロンプト例

たとえば、既存のアプリに機能を追加する場合は、Codex に次のような変更を依頼できます：

## 実践的なヒント

### 基本から開始

新規開発では、まず通常のプロンプトから始めます。Codex に、スターター SwiftUI アプリのひな形と、その環境の `Build` アクションに接続できる簡単なビルド・起動スクリプトを作成するよう依頼します（対象環境：[ローカル環境](/ja-JP/codex/environments/local-environment)）。最初の段階では、多くの場合、スキルも MCP サーバーも必要ありません。

### 小さく信頼できる検証ループの活用

変更のたびに、変更対象の仕様を実際に検証できる最も範囲の狭いコマンドを Codex に実行させます。その後、より広範なビルドへ拡大します。これにより、編集のたびにアプリ全体のビルドが必要だと決めつけることなく、Codex の速度を保てます。

### CLI ファーストのループを維持

ループでは CLI を優先します。Apple の `xcodebuild` ツールを使えば、ターミナルからスキームを一覧表示し、ビルド、テスト、アーカイブ、`build-for-testing`、`test-without-building` の各アクションを実行できます。これにより、Xcode の GUI に切り替えることなく、Codex はエージェント型のループ内で作業を続けられます。

### XcodeBuildMCP の活用

本格的な Xcode プロジェクトで作業し、より高度な自動化が必要になったら、すぐに XcodeBuildMCP を使います。スキーム、ターゲット、シミュレーターの制御、スクリーンショット、ログ、UI 操作が重要になり、単純なシェルコマンドだけでは済まなくなる段階です。
