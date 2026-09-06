<!-- source: https://learn.chatgpt.com/ja-JP/use-cases/browser-games -->

## はじめに

ゲーム開発は、Codex がコード生成以外にも役立つことを最も明確に示す例の 1 つです。実際のゲームには通常、文書化されたコンセプト、レンダリングレイヤー、フロントエンドの基盤構築、バックエンドの状態管理、アセット制作、継続的なビジュアル調整が必要です

このユースケースでは、まずゲームの仕様を Codex に正確に書き出させ、その後、Playwright interactive を使って実際のブラウザでゲームをテストしながら反復改善すると、最も効果的です。

## まずゲームプランを作成

Codex が実装の雛形を作り始める前に、ゲームの内容を具体的に定義する `PLAN.md` を作成するよう依頼します:

- プレイヤーの目標
- メインループ
- 入力と操作方法
- 勝利条件と失敗条件
- 進行システムまたは難易度
- ビジュアルの方向性
- 技術スタックとホスティングに関する前提
- マイルストーンの順序

このプランが重要なのは、「ゲームを作る」だけでは曖昧すぎるためです。Codex はゲームの各要素の実装方法を把握する必要があり、構築中にはその実装の詳細を参照することもよくあります。

スラッシュコマンド `/plan` でプランモードを有効にできます。
出力を `PLAN.md` ファイルに保存します。

## AGENTS.md で Codex の動作を指定

Codex がプランに従い、作業内容を検証し、適切なツールを使うようにするには、次のような `AGENTS.md` を定義します:

```text
# Game name

Tech Stack:

- NextJS for frontend (hosted on Vercel)
- <insert technology> for rendering
- Fastify for backend, websockets (hosted on <hosting platform>)
- Postgres for database (hosted on <hosting platform>)
- Redis for caching and pub/sub (hosted on <hosting platform>)
- OpenAI for generative AI features

Tips:

- Use build and test commands to verify your work as soon as you complete a feature or task
- Use the PLAN.md file to guide your work when building new features
- Log your work under .logs (create new log files as you see fit) to record your thought process and decisions, and reference them when iterating on features
- Use playwright to test the visual output of your work, and iterate if it doesn't look right or fit the vibe
- Use imagegen to generate visual assets for your work, and every time you generate a collection of assets, save the prompts you used to be able to continue generating more of the same assets later (create files in .prompts)
- Use Context7 MCP to fetch <rendering framework> docs

これにより、Codex は長時間自律的に動作し、必要に応じて関連するスキルを使用できます。

## スキルの活用

AGENTS.md ファイルに記載したスキルを追加します:

- Codex が必要に応じてゲーム用のビジュアルアセットを生成できるようにする Imagegen
- Codex が実際のブラウザでゲームをテストできるようにする Playwright interactive
- Codex が最新の OpenAI API ドキュメントを取得できるようにする OpenAI ドキュメント
- レンダリングフレームワークの最新ドキュメントを取得するために、Context7 MCP サーバーを追加することもできます

スキルを追加する方法について詳しくは、[スキルのドキュメント](/ja-JP/codex/build-skills)をご覧ください。

  **ヒント**: 画像生成用のプロンプトをファイルに保存するよう Codex に依頼し、
  すべてのビジュアルアセットに一貫性を持たせます。生成するアセットのスタイルを指定し、
  詳細かつ再利用可能なプロンプトを Codex に作成させます。

## Codex による実装と反復改善

Codex は最初のプランに基づいて、ゲームの最初のバージョンを生成します。

画像アセットを大量に生成する必要がある場合、最初のバージョンの作成には時間がかかり、ときには数時間に及ぶこともあります。Codex は自身の作業をテストし、実際のブラウザでゲームを試せるため、ユーザーからの入力がなくても長時間作業を続けられます。

プランが明確であるほど、最初の反復改善後に得られる成果物の品質が向上します。

ゲームをテストしながら、スクリーンショットを提供したり、ゲームプレイの変更やビジュアルアセットの更新を依頼したりして、満足できる結果になるまで必要に応じて改善を繰り返します。
