<!-- source: https://learn.chatgpt.com/ja-JP/use-cases/ios-liquid-glass -->

## iOS 26 を基準とする移行

まず、Liquid Glass を iOS 26 と Xcode 26 への移行プロジェクトとして扱います。iOS 26 SDK でアプリを再ビルドし、標準の SwiftUI コントロールから自動的に得られる外観を確認します。その後で初めて、平坦すぎる、重すぎる、またはシステム UI との一体感に欠けるカスタム部分だけを再設計するよう Codex に依頼します。

アプリが以前の iOS バージョンもサポートしている場合は、その制約を最初から明示してください。[Build iOS Apps プラグイン](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) の SwiftUI Liquid Glass スキルでは、Liquid Glass 専用の新しい API を `#available(iOS 26, *)` でガードし、旧バージョンのデバイスでも読みやすさを保てるフォールバックを維持する必要があります。

## iOS プラグインの活用

[Build iOS Apps プラグイン](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) を使用すると、Codex で SwiftUI の UI 変更とシミュレータによる検証を組み合わせられます。Liquid Glass への移行では、Codex に 1 つのフローを監査させ、少数の UI 領域を移行し、iOS 26 シミュレータで結果を起動して、対象範囲を広げる前にスクリーンショットを取得させるのが効果的です。

このプラグインには SwiftUI Liquid Glass スキルが含まれており、次の基本方針をプロンプトに盛り込むと効果的です：

- カスタムのぼかしビューよりも、ネイティブの `glassEffect`、`GlassEffectContainer`、Glass ボタンスタイル、`glassEffectID` による遷移を優先します。
- マテリアルが目的の最終形状に沿って適用されるよう、レイアウトと外観のモディファイアの後に `.glassEffect(...)` を適用します。
- 複数の UI 領域を同時に表示する場合は、関連する Glass 要素を `GlassEffectContainer` で囲みます。
- 実際にタッチに反応するボタン、チップ、コントロールにのみ `.interactive()` を使用します。
- 個別の Glass 表現を混在させず、機能全体で角の形状、ティント、間隔に一貫性を持たせます。
- iOS 26 より前のターゲット向けに、Liquid Glass を使用しないフォールバックを維持します。

プラグインとスキルのインストールについて詳しくは、[プラグイン](/ja-JP/codex/plugins) と [スキル](/ja-JP/codex/build-skills) のドキュメントをご覧ください。

## WWDC セッションの視聴

Codex に実際の本番フローをリファクタリングさせる前に、次の WWDC25 セッションを参照するとよいでしょう：

- [Liquid Glass の紹介](https://developer.apple.com/videos/play/wwdc2025/219/)
- [新しいデザインシステムを知る](https://developer.apple.com/videos/play/wwdc2025/356/)
- [新しいデザインで SwiftUI アプリを構築](https://developer.apple.com/videos/play/wwdc2025/323/)
- [新しいデザインで UIKit アプリを構築](https://developer.apple.com/videos/play/wwdc2025/284/)
- [SwiftUI の新機能](https://developer.apple.com/videos/play/wwdc2025/256/)

## 移行計画の依頼から部分実装へ

Liquid Glass への移行は、Codex が「Liquid Glass をどこに適用すべきか？」と「今すぐすべてのコードを書く」を分けて扱うことで、より円滑に進みます。まず簡単な監査を依頼し、その後、エージェントに独立して完結する 1 つの範囲をシミュレータで検証しながら実装させてください。

## 実践的なヒント

### Liquid Glass の全面適用を回避

Liquid Glass は、すべてのカードを光るパネルに変えるのではなく、コンテンツの上に明確なコントロールレイヤーを作るためのものです。システムマテリアルと競合する装飾的な背景は Codex に削除させ、可読性が最も重要な箇所では装飾のないコンテンツを維持し、ティントは意味上の強調や主要アクションに限定してください。

### 利用頻度の高い 1 つのフローから開始

最初の移行対象には、アプリ全体を一括で移行するよりも、タブのルート画面、詳細画面、シート、検索 UI、オンボーディングフローのいずれかが適しています。これによりレビューしやすくなり、Liquid Glass に関するどの判断を再利用可能なコンポーネントパターンとして採用すべきかが明確になります。

### フォールバック動作の入念なレビュー

デプロイターゲットが iOS 26 未満の場合は、Liquid Glass 版と並べてフォールバック実装を表示するよう Codex に依頼してください。このレビューステップにより、API の可用性に関する意図しないリグレッションを検出し、最新のシミュレータでしか動作しない移行内容のリリースを避けられます。
