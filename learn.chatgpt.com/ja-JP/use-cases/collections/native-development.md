<!-- source: https://learn.chatgpt.com/ja-JP/use-cases/collections/native-development -->

# ネイティブ開発

各回の作業に、ビルド、実行、シミュレーターのいずれかを使った反復検証を組み込むと、Codex は Apple プラットフォーム向けプロジェクトで高い効果を発揮します。
これらのユースケースは、新規または既存の iOS および macOS アプリを開発する際に、UI を反復的に改善し、問題をデバッグする必要がある場合に役立ちます。

## アプリの基本構造の構築

Codex に、繰り返し実行できるビルドループを備えた iOS および macOS アプリのひな形を作成させます。Mac アプリの基本構造に関するユースケースでは、サイドバー、詳細ビュー、インスペクターで構成されるレイアウト、コマンド、設定など、デスクトップアプリ固有の構造をさらに詳しく扱います。

## iOS の SwiftUI 画面のリファクタリング

Codex を使って、動作を変えずに大規模な SwiftUI ビューを分割し、アプリの準備が整った段階で、対象の iOS フローを Liquid Glass に移行します。

## iOS アクションのシステムへの公開

Codex を活用して、アプリが App Intents を通じて公開すべきアクションとエンティティを特定し、ユーザーがシステムの各種 UI からアプリの機能を呼び出せるようにします。

## アプリのデバッグ

Codex に Simulator でバグを再現させるか、macOS アプリにテレメトリを追加させて、問題のデバッグと修正に役立てます。

- [iOS 向けアプリの開発](/ja-JP/use-cases/native-ios-apps)

- [macOS 向け開発](/ja-JP/use-cases/native-macos-apps)

- [Mac アプリシェルの構築](/ja-JP/use-cases/macos-sidebar-detail-inspector)

- [SwiftUI 画面のリファクタリング](/ja-JP/use-cases/ios-swiftui-view-refactor)

- [Liquid Glass の導入](/ja-JP/use-cases/ios-liquid-glass)

- [iOS アプリに App Intents を追加](/ja-JP/use-cases/ios-app-intents)

- [iOS シミュレータでのデバッグ](/ja-JP/use-cases/ios-simulator-bug-debugging)

- [Mac テレメトリの追加](/ja-JP/use-cases/macos-telemetry-logs)
