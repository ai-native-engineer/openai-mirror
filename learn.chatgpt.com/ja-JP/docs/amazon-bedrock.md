<!-- source: https://learn.chatgpt.com/ja-JP/docs/amazon-bedrock -->

ローカル環境の ChatGPT Work と Codex で、Amazon Bedrock 経由で利用できる OpenAI モデルを使用するように構成します。この構成では、ローカルクライアントが AWS の管理する認証とアクセス制御を使用して、モデルリクエストを Bedrock に送信します。

## 動作の仕組み

ローカル環境の ChatGPT Work または Codex で Amazon Bedrock をモデルプロバイダーとして構成すると、OpenAI がホストする Responses API はリクエスト経路に含まれません。ローカルクライアントはモデルリクエストを Amazon Bedrock に送信し、Bedrock はサポート対象の OpenAI モデル向けに OpenAI 互換の Responses API 実装を提供します。

  認証には AWS ネイティブの仕組みを使用します。ユーザーは Bedrock API キーまたは AWS
  IAM 認証情報で認証します。このプロバイダーでは、ChatGPT へのサインインや `OPENAI_API_KEY`
  を使用しません。

## 開始前の準備

以下の項目を確認してください。

- Amazon Bedrock でサポート対象の OpenAI モデルにアクセスできること
- 選択したモデルを利用できる AWS リージョン
- AWS アカウントで Amazon Bedrock Mantle パスの認証が構成されていること

## プロバイダーの構成

Amazon Bedrock Mantle パス用のモデルプロバイダー `amazon-bedrock` を
`~/.codex/config.toml` に追加します。ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能、
SDK
は同じローカル構成レイヤーを読み込みます。モデルの指定は任意です。必要に応じて、サポート対象のモデルを明示的に選択してください。

```toml
model_provider = "amazon-bedrock"

  このガイドでは、サポート対象の商用 AWS リージョンにおける Amazon Bedrock Mantle パスを扱います。ローカル環境の ChatGPT Work と Codex は、AWS GovCloud リージョンの Bedrock Mantle エンドポイントには対応していません。

## 認証オプション

ローカル環境の ChatGPT Work と Codex は、2 つの Bedrock 認証方式に対応しています。次の順序で確認します。

1. Bedrock API キー
2. AWS SDK 認証情報チェーン

### オプション 1：Bedrock API キー

ローカルクライアントが参照する環境に Bedrock API キーを設定します。API キー認証を使用する場合は、リージョンを指定する必要があります。

```shell

### オプション 2：AWS SDK 認証情報

組織が AWS SDK 認証情報チェーンを通じて Bedrock へのアクセスを管理している場合は、この方式を使用します。ローカルクライアントでは、次の標準的な AWS SDK 認証情報ソースを使用できます。

#### AWS の共有構成ファイル

AWS の共有 `config` ファイルと `credentials` ファイルを構成します。

```shell
aws configure

#### 環境変数

AWS SDK の標準的な認証情報環境変数を設定します。

```shell

#### AWS Management Console の認証情報

AWS Management Console の認証情報でログインします。

```shell
aws login

#### AWS SSO または名前付きプロファイル

AWS SSO でログインし、名前付きプロファイルを選択します。

```shell
aws sso login --profile codex-bedrock

#### フェデレーティッドアイデンティティ

企業の SSO または OIDC
フェデレーションでは、ローカルクライアントの外部で `credential_process` を使用してフェデレーティッドアイデンティティを構成し、AWS SDK
が認証情報を解決できるようにします。ブラウザでのログイン、トークン交換、キャッシュ、更新は、
AWS プロファイルの `credential_process` ヘルパーで処理するようにします。

## デスクトップアプリと IDE 拡張機能

デスクトップアプリや IDE
拡張機能は、シェルから環境変数を継承しない場合があります。必要な値を `~/.codex/.env`
に設定してから、アプリまたは拡張機能を再起動します。

```shell

## セットアップの確認

- Codex CLI で `/status` を開き、Codex がモデルプロバイダーとして
`amazon-bedrock` を使用していることを確認します。
- ChatGPT デスクトップアプリを再起動した後、Work または Codex を選択して新しいタスクを開始します。
- IDE 拡張機能を再起動した後、新しいセッションを開始します。
- 選択したモデルが構成済みの AWS リージョンで利用可能であり、AWS アイデンティティにそのモデルへのアクセス権があることを確認します。

## サポート対象のモデル

正確なモデル ID を使用してください。

```text
openai.gpt-5.6-sol
openai.gpt-5.6-terra
openai.gpt-5.6-luna
openai.gpt-5.5
openai.gpt-5.4

モデルの提供状況は AWS リージョンによって異なります。モデルを選択する前に、[モデルの
AWS
リージョン別対応状況](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html)を確認してください。

## 機能の提供状況

この構成では、ローカル環境の ChatGPT Work と Codex のワークフローを利用できます。Web 上でホストされる ChatGPT Work、Codex Cloud、および OpenAI がホストするクラウドサービス、ホスト型ツール、クラウド管理型のディスカバリーに依存する機能は、現在利用できません。

  Amazon Bedrock では Fast モードを利用できません。Fast モードは優先処理を使用しますが、Amazon Bedrock の初期提供ではオンデマンド推論のみがサポートされます。

  

  <div
    id="codex-plan-region-limits"
    className="not-prose mt-3 text-sm text-secondary"
  >
    <sup>\*</sup> 現在、この機能は特定の地域でのみ利用できます。
    地域制限の詳細は、各機能のドキュメントをご確認ください。
  </div>
  <div
    id="codex-plan-plugin-limits"
    className="not-prose mt-1 text-sm text-secondary"
  >
    <sup>†</sup> ローカルプラグインバンドルや OpenAI が選定したプラグインのうち、
    ChatGPT 認証を必要としないものは、Codex Security を含めて利用できます。
    ChatGPT 認証やコネクタ、
    クラウドホスト型の共有機能を必要とするプラグインは利用できません。
  </div>

## トラブルシューティング

セットアップに失敗した場合は、次の点を確認してください。

- モデル ID がサポート対象モデルの ID と完全に一致していること
- モデルを利用できる AWS リージョンが指定されていること
- Bedrock API キーまたは AWS 認証情報が有効で、期限切れでないこと
- AWS アイデンティティに、選択した Bedrock モデルへのアクセス権があること
- `AWS_BEARER_TOKEN_BEDROCK` に、期限切れまたは意図しないキーが設定されていないこと
- デスクトップアプリまたは IDE 拡張機能を使用する場合は、
  必要な環境変数が `~/.codex/.env` に設定されていること

## サポート範囲

OpenAI サポートでは、ChatGPT Work および Codex クライアントのセットアップと構成、ローカル CLI の動作、デスクトップアプリの動作、IDE 拡張機能の動作、ローカル環境での製品利用についてサポートします。

AWS 認証情報、IAM 権限、Bedrock モデルへのアクセス、クォータ、請求、リージョンごとの提供状況、Bedrock リクエストの失敗、AWS サービスログ、Bedrock サービスの動作については、お客様の AWS 管理者または AWS サポートにお問い合わせください。
