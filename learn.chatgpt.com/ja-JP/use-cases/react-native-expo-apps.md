<!-- source: https://learn.chatgpt.com/ja-JP/use-cases/react-native-expo-apps -->

## まずは Expo Go

Codex でモバイルアプリのアイデアを
テスト済みの React Native アプリに仕上げたい場合は、Expo が有力な第一候補です。まず `expo start` を実行し、次に Expo Go
を実機で使います。その後は、アプリに必要なのが
カスタムネイティブコード、ストア配布、または Expo Go では実行できない機能である場合に限り、開発クライアントまたは EAS ビルドに移行します。

この進め方なら、Codex は初回からアプリのワークフローに集中でき、
ネイティブ IDE やシミュレーターのセットアップ、プロビジョニング、ビルド構成に時間を費やさずに済みます。

## Expo プラグインの利用

Expo は [Expo プラグイン](https://docs.expo.dev/skills/) を公開しました。このプラグインは、Expo Router、ネイティブ UI、フォーム、
ナビゲーション、アニメーション、データ取得、NativeWind のセットアップ、Expo モジュール、開発
クライアント、デプロイ、アップグレード、Codex Run アクションの連携設定について、Expo に即したガイダンスを Codex に提供します。

このプラグインは、Codex による新しい Expo 画面の作成、パッケージの追加、API
呼び出しの組み込み、開発クライアントの準備、または TestFlight、App
Store、Play Store、EAS Hosting 向けのアプリの準備に使用します。

タスクで最新の
Expo ドキュメントの検索、互換性のあるパッケージのインストール、EAS のビルドおよび
ワークフロー操作、スクリーンショットの取得、シミュレーターの操作、React Native DevTools、
TestFlight データが必要な場合は、必要に応じて [Expo MCP サーバー](https://docs.expo.dev/eas/ai/mcp/) を追加します。

## イテレーションの流れ

1. リポジトリを調べ、新規の Expo アプリか
既存の Expo プロジェクトかを確認するよう、Codex に依頼します。
2. Expo Router と Expo Go から始め、`npx expo install` を使用して
   Expo パッケージを追加します。
3. Codex に、ネイティブアプリらしいナビゲーション、
読み込み状態、空の状態、エラー状態を備えた 1 つの完全なワークフローを構築するよう依頼します。
4. 実機上の Expo Go や
シミュレーターなど、利用できる最速の方法で検証し、必要な場合にのみ開発クライアントまたは EAS に移行します。

## おすすめのフォローアッププロンプト
