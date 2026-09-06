<!-- source: https://learn.chatgpt.com/ja-JP/docs/build-plugins -->

プラグインの作成や提出については、
[developers.openai.com の開発者向けドキュメント](/plugins)で詳しい手順を確認してください。

<div className="not-prose my-6">
  
    プラグインの作成と提出
  
</div>

このページでは概要を簡単に説明します。プラグインはインストール可能なパッケージで、スキル、MCP サーバー、またはその両方を含められます。MCP サーバーは、必要に応じて UI を返すこともできます。

ChatGPT と Codex は 1 つの共通プラグインディレクトリを共有しています。プラグインを一度一般公開すれば、両製品の対応画面から同じ掲載情報を見つけられるようになります。開発中は、ローカルマーケットプレイスでパッケージをテストしてから、共通ディレクトリに提出してください。

GitHub を通じたワークスペースへの配布については、
[プラグインの管理](/ja-JP/codex/enterprise/plugin-management)を参照してください。

個人用のワークフローを 1 つ試行錯誤している段階では、まずスキルから始めてください。そのワークフローの共有、関連スキルのパッケージ化、外部サービスへの接続、安定した機能のチームへの配布を行いたい場合は、プラグインを作成してください。

## `@plugin-creator` を使ったプラグインの作成

最短でセットアップするには、ChatGPT Work モードに組み込まれた `@plugin-creator` スキル、
または Codex の `$plugin-creator` を使用します。

  
    
  

実現したい結果、含めるスキルや MCP サーバー、テスト用にローカルマーケットプレイスへの登録を希望するかどうかを説明してください。例：

```text
@plugin-creator Create a plugin named meeting-follow-up.
Include a skill that turns meeting notes into decisions, owners, and next steps.
Add it to a personal marketplace so I can test it locally.

このスキルは、必須のマニフェスト `.codex-plugin/plugin.json` を作成し、プラグインフォルダーを整理します。
プラグインをローカルマーケットプレイスに追加することもできます。

  
    
  

完了したら、次の手順を実行します：

1. `.codex-plugin/plugin.json` をレビューします。
2. `skills/` 配下に同梱された各スキルを確認します。
3. ChatGPT または Codex を再読み込みし、登録先のローカルマーケットプレイスからプラグインをインストールします。
4. 代表的なリクエストを使って、新しい会話でプラグインをテストします。

プラグインに MCP サーバーが含まれる場合は、まずそのサーバーを構築してテストし、
登録済みの接続情報を `@plugin-creator` に渡します。ツール、認証、デプロイ、テストについては、
[MCP サーバーのワークフロー](https://developers.openai.com/plugins/build/mcp-server)に従って、
一連の手順を進めてください。

## スキルのみを含むプラグインの手動作成

最小構成のプラグインには、マニフェストと少なくとも 1 つのスキルが含まれます：

```text
meeting-follow-up/
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── meeting-follow-up/
        └── SKILL.md

`.codex-plugin/plugin.json` を作成します：

```json
{
  "name": "meeting-follow-up",
  "version": "1.0.0",
  "description": "Turn meeting notes into decisions and next steps",
  "skills": "./skills/"
}

次に、`skills/meeting-follow-up/SKILL.md` を追加します：

```md
---
name: meeting-follow-up
description: Extract decisions, owners, and next steps from meeting notes.
---

Review the meeting notes. Return:

1. Decisions
2. Action items with owners
3. Open questions

プラグイン名には、継続して使えるケバブケースの名前を選んでください。スキルの説明は、ChatGPT と Codex がそのワークフローを適用すべき場面を判断できるよう、具体的に記述してください。

`@plugin-creator` を使ってフォルダーをローカルマーケットプレイスに追加し、
共有する前にインストールしてテストします。

## 開発者向けドキュメントでの次のステップ

プラグイン開発の詳しい手順は、
[プラグインのドキュメント](https://developers.openai.com/plugins/)を参照してください。次の内容を扱っています：

- [プラグインのアーキテクチャ](https://developers.openai.com/plugins/concepts/plugins)
- [スキルの作成](https://developers.openai.com/plugins/build/skills)
- [MCP サーバーの構築](https://developers.openai.com/plugins/build/mcp-server)
- [UI の追加（任意）](https://developers.openai.com/plugins/build/chatgpt-ui)
- [プラグインのパッケージ化](https://developers.openai.com/plugins/build/plugins)
- [プラグインのテスト](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [提出と公開](https://developers.openai.com/plugins/deploy/submission)

プラグインの閲覧、インストール、有効化、削除については、[プラグインの
使用](/ja-JP/codex/plugins)を参照してください。
