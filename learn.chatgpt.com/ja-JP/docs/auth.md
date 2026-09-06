<!-- source: https://learn.chatgpt.com/ja-JP/docs/auth -->

## OpenAI 認証

<a id="sign-in-with-chatgpt"></a>

OpenAI モデルを使用する場合、Codex では次の 2 つの方法でサインインできます：

- ChatGPT でサインインしてサブスクリプションを利用
- API キーでサインインして従量課金で利用

ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能は、ローカルでの作業で両方のサインイン方法に対応しています。
Codex Cloud を利用するには ChatGPT でのサインインが必要です。

適用される管理者向けの制御機能とデータ処理ポリシーも、サインイン方法によって決まります。

- ChatGPT でサインインすると、Codex の利用には、ChatGPT ワークスペースの権限、
ロールベースのアクセス制御（RBAC）、および ChatGPT Enterprise の
データ保持とデータレジデンシーに関する設定が適用されます。
- API キーを使用する場合は、代わりに API 組織のデータ保持と
データ共有に関する設定が適用されます。

管理対象のワークスペースでは、認証はアクセス制御の一要素にすぎません。
サインインできるユーザーはワークスペースのメンバーシップとプロビジョニングで決まり、
利用できるプロダクトの各画面や機能は、シートとワークスペースのロールによって決まります。
ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能でローカル作業を行う場合は、
権限プロファイルによって、エージェントがデバイス上で実行できる操作が制限されます。
これらの制御の計画については、「[グループとプロビジョニング](/ja-JP/codex/enterprise/groups-and-provisioning)」
および「[ロールとワークスペースの権限](/ja-JP/codex/enterprise/roles-and-workspace-permissions)」
を参照してください。

### ChatGPT でのサインイン

ChatGPT デスクトップアプリ、Codex CLI、または IDE 拡張機能から ChatGPT でサインインすると、ブラウザウィンドウが開きます。サインイン後、ブラウザから認証情報が Codex に返されます。

### ChatGPT Web

「[ChatGPT](https://chatgpt.com)」を開いてサインインし、作業するワークスペースを選択します。
ChatGPT Web の認証済みセッションはブラウザに保持されます。

#### ChatGPT デスクトップアプリ

サインアウト状態の画面で「 **サインインを続ける**」を選択し、
ブラウザでの手続きを完了します。

#### Codex CLI

`codex login` を実行し、ブラウザでの手続きを完了します。有効なセッションがない場合は、
これがデフォルトの認証手順となります。

#### IDE 拡張機能

サインアウト状態の画面で「 **ChatGPT でサインイン**」を選択し、
ブラウザでの手続きを完了します。

<a id="sign-in-with-an-api-key"></a>

### API キーでのサインイン

ChatGPT デスクトップアプリ、Codex CLI、または IDE 拡張機能には、API キーでもサインインできます。API キーは「[OpenAI ダッシュボード](https://platform.openai.com/api-keys)」から取得してください。

#### ChatGPT デスクトップアプリ

サインアウト状態の画面で「 **別の方法でサインイン**」を選択してキーを入力し、
「 **続ける**」を選択します。

#### Codex CLI

キーを stdin 経由で `codex login` にパイプします：

```shell
printenv OPENAI_API_KEY | codex login --with-api-key

#### IDE 拡張機能

サインアウト状態の画面で「 **API キーを使用**」を選択してキーを入力し、
「**OK**」を選択します。

OpenAI は、API キーの使用料金を標準の API 料金に基づき、OpenAI Platform アカウントを通じて請求します。詳しくは、「[API 料金ページ](https://openai.com/api/pricing/)」を参照してください。

API キー認証はローカルの Codex ワークフローに対応していますが、
ChatGPT ワークスペースへのアクセスやクラウドサービスに依存する一部の機能は、制限されるか利用できません。
プランごとの対応状況は、
「[機能の提供状況](/ja-JP/codex/pricing#feature-availability)」で比較できます。

Codex CLI および ChatGPT デスクトップアプリの Codex では、API キー認証でも
OpenAI が選定した対応プラグインを利用できます。一部のプラグインは、
接続フローで未対応の OAuth 機能を
必要とするため利用できません。詳しくは、「[プラグインの使用](/ja-JP/codex/plugins#api-key-availability)」を参照してください。

API キーでサインインすると、Codex には ChatGPT プランに含まれるクレジットではなく、
標準の API 料金が適用されます。

CI/CD ジョブなど、プログラムから実行する Codex CLI ワークフローでは API キー認証を使用してください。
信頼できない環境や公開環境に Codex の実行機能を公開しないでください。

### 認証状態の確認またはサインアウト

プロファイルメニューを開き、使用中のアカウントとワークスペースを確認します。
そのブラウザの ChatGPT Web セッションを終了するには、「 **ログアウト**」を選択します。

プロファイルメニューを開くと、使用中のアカウントまたは API キーの状態を確認できます。
現在の認証情報を消去するには、「**ログアウト** 」を選択します。

使用中の認証方法を確認するには、`codex login status` を実行します。保存された認証情報を
使用している場合は、現在の認証情報を消去するために `codex logout` を実行します。
プロセスでワークロード ID が選択されている場合、認証はプロセス環境によって制御されるため、Codex は `codex login` と
`codex logout` を拒否します。

プロファイルメニューを開くと、使用中のアカウントまたは API キーの状態を確認できます。
現在の認証情報を消去するには、「**ログアウト** 」を選択します。

### エンタープライズ自動化での Codex アクセストークンの使用

ChatGPT Enterprise ワークスペースでは、管理者がアクセストークンの権限を付与できます。
権限を付与されたメンバーは、信頼できる非対話型の Codex ローカルワークフローで使用する
Codex アクセストークンを作成できます。ブラウザでサインインせずに、ChatGPT ワークスペースへのアクセス、
ChatGPT で管理される Codex の利用資格、またはエンタープライズワークスペースの管理機能を
自動化で利用する必要がある場合は、アクセストークンを使用してください。

アクセストークンは、信頼できるスクリプト、スケジューラー、プライベート CI ランナーでの使用を目的としています。
一般的な OpenAI API の呼び出しには、引き続き Platform API キーを使用してください。

セットアップ手順、権限、ローテーション、失効に関するガイダンスについては、
「[アクセストークン](/ja-JP/codex/enterprise/access-tokens)」を参照してください。

クラウドプラットフォーム、CI システム、またはクラスターがすでに有効期間の短い
ワークロードトークンを発行している場合は、OpenAI の認証情報を保存する代わりに、
「[ワークロード ID フェデレーション](/ja-JP/codex/enterprise/workload-identity)」
を使用してください。

環境ですでに Codex アクセストークンが提供されている場合は、トークンを CLI にパイプします：

```shell
printenv CODEX_ACCESS_TOKEN | codex login --with-access-token

## Codex Cloud アカウントの保護

Codex Cloud はコードベースを直接操作するため、他の多くの ChatGPT 機能よりも強固なセキュリティが必要です。多要素認証（MFA）を有効にしてください。

ソーシャルログインプロバイダー（Google、Microsoft、Apple）を使用する場合、ChatGPT アカウントで MFA を有効にする必要はありませんが、ソーシャルログインプロバイダー側で設定できます。

セットアップ手順については、以下を参照してください：

- [Google](https://support.google.com/accounts/answer/185839)
- [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661)
- [Apple](https://support.apple.com/en-us/102660)

シングルサインオン（SSO）で ChatGPT にアクセスする場合は、組織の SSO 管理者がすべてのユーザーに MFA の利用を義務付けることが推奨されます。

メールアドレスとパスワードでログインする場合は、Codex Cloud にアクセスする前に、アカウントで MFA を設定する必要があります。

アカウントが複数のログイン方法に対応しており、その一つがメールアドレスとパスワードによるログインである場合は、別の方法でサインインするときでも、Codex にアクセスする前に MFA を設定する必要があります。

<a id="login-caching"></a>

## ログイン情報のキャッシュ

ChatGPT または API キーを使用して ChatGPT デスクトップアプリ、Codex CLI、または IDE 拡張機能にサインインすると、ログイン情報がキャッシュされ、再利用されます。CLI と拡張機能は同じログイン情報のキャッシュを共有します。どちらかでログアウトすると、次回 CLI または拡張機能を起動したときに、再度サインインする必要があります。

Codex は、ログイン情報をローカルの平文ファイル `~/.codex/auth.json` または OS 固有の認証情報ストアにキャッシュします。

ChatGPT でサインインしたセッションでは、Codex が使用中のトークンを期限切れになる前に自動更新するため、通常、アクティブなセッションはブラウザで再度ログインしなくても継続します。

<a id="credential-storage"></a>
<a id="enforce-a-login-method-or-workspace"></a>

## 認証情報の保存

`cli_auth_credentials_store` を使用して、Codex CLI がキャッシュした認証情報の保存先を制御します：

```toml
# file | keyring | auto
cli_auth_credentials_store = "keyring"

- `file` では、認証情報を `auth.json` に保存します。保存先は `CODEX_HOME` 配下です（デフォルトは `~/.codex`）。
- `keyring` では、オペレーティングシステムの認証情報ストアに認証情報を保存します。
- `auto` では、利用できる場合は OS の認証情報ストアを使用し、利用できない場合は `auth.json` にフォールバックします。

`config.toml` の完全なスキーマについては、
[構成リファレンス](/ja-JP/codex/config-file/config-reference)を参照してください。

  ファイルベースの保存を使用する場合、`~/.codex/auth.json` はアクセストークンを含むため、パスワードと同様に扱ってください。
  コミットしたりチケットに貼り付けたりせず、
  チャットでも共有しないでください。

## ログイン方法またはワークスペースの指定の必須化

管理対象の環境では、管理者がユーザーに許可する認証方法を制限できます：

```toml
# Only allow ChatGPT login or only allow API key login.
forced_login_method = "chatgpt" # or "api"

# When using ChatGPT login, restrict users to a specific workspace.
forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"

使用中の認証情報が設定済みの制限に一致しない場合、Codex はユーザーをログアウトさせて終了します。

これらの設定は、通常、ユーザーごとのセットアップではなく、管理対象の設定を通じて適用されます。「[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration)」を参照してください。

## ログイン診断

`codex login` を直接実行すると、設定済みのログディレクトリに専用の `codex-login.log` ファイルが作成されます。
ブラウザログインやデバイスコード認証の失敗をデバッグする場合、
またはサポートからログイン固有のログの提出を求められた場合に使用してください。

## カスタム CA バンドル

ネットワークで企業の TLS プロキシまたはプライベートルート CA を使用している場合は、
ログイン前に `CODEX_CA_CERTIFICATE` に PEM バンドルを設定してください。
`CODEX_CA_CERTIFICATE` が未設定の場合、Codex は `SSL_CERT_FILE` にフォールバックします。
同じカスタム CA 設定は、ログイン、通常の HTTPS リクエスト、
安全な WebSocket 接続に適用されます。

```shell

codex login

## ヘッドレスデバイスでのログイン

Codex CLI から ChatGPT にサインインする際、次のような状況ではブラウザベースのログイン UI が機能しないことがあります：

- CLI をリモート環境またはヘッドレス環境で実行している場合
- ローカルのネットワーク構成により、サインイン後に Codex が OAuth トークンを CLI に返すための localhost コールバックがブロックされている場合

このような場合は、デバイスコード認証（ベータ版）を優先してください。対話型ログイン UI で「 **デバイスコードでサインイン**」を選択するか、`codex login --device-auth` を直接実行します。使用中の環境でデバイスコード認証が機能しない場合は、いずれかの代替手段を使用してください。

### 推奨：デバイスコード認証（ベータ版）

1. ChatGPT のセキュリティ設定（個人アカウント）、または ChatGPT のワークスペース権限（ワークスペース管理者）で、デバイスコードログインを有効にしてください。
2. Codex を実行しているターミナルで、次のいずれかを選択します：
   - 対話型ログイン UI で「 **デバイスコードでサインイン**」を選択します。
   - `codex login --device-auth` を実行します。
3. ブラウザでリンクを開いてサインインし、ワンタイムコードを入力します。

使用中の環境でデバイスコードログインを利用できない場合は、以下のいずれかの代替手段を使用してください。

### 代替手段：ローカルでの認証と認証キャッシュのコピー

ブラウザを使用できるマシンでログイン手続きを完了できる場合は、キャッシュされた認証情報をヘッドレスマシンにコピーできます。

1. ブラウザベースのログイン手続きを使用できるマシンで、`codex login` を実行します。
2. ログインキャッシュが `~/.codex/auth.json` に存在することを確認します。
3. `~/.codex/auth.json` をヘッドレスマシンの `~/.codex/auth.json` にコピーします。

`~/.codex/auth.json` をパスワードと同様に扱ってください。このファイルにはアクセストークンが含まれています。コミットしたり、チケットに貼り付けたり、チャットで共有したりしないでください。

OS が認証情報を `~/.codex/auth.json` ではなく認証情報ストアに保存する場合、この方法を使用できないことがあります。
ファイルベースの保存を構成する方法については、「[認証情報の保存](/ja-JP/codex/auth#credential-storage)」を参照してください。

SSH 経由でリモートマシンにコピーします：

```shell
ssh user@remote 'mkdir -p ~/.codex'
scp ~/.codex/auth.json user@remote:~/.codex/auth.json

または、`scp` を使用しないワンライナーを実行します：

```shell
ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json

Docker コンテナにコピーします：

```shell
# Replace MY_CONTAINER with the name or ID of your container.
CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"

信頼できる CI/CD ランナーでこのパターンをさらに高度に利用する方法については、
「[CI/CD で Codex アカウントの認証を維持する（上級）](/codex/auth/ci-cd-auth)」を参照してください。
このガイドでは、通常の実行中に Codex が `auth.json` を更新できるようにし、
更新後のファイルを次のジョブ用に保持する方法を説明しています。
自動化では、引き続き API キーをデフォルトとして使用することを推奨します。

### 代替手段：SSH 経由での localhost コールバックの転送

ローカルマシンとリモートホストの間でポートを転送できる場合は、Codex のローカルコールバックサーバー（デフォルトは `localhost:1455`）をトンネリングすることで、標準のブラウザベースの手続きを使用できます。

1. ローカルマシンからポート転送を開始します：

```shell
ssh -L 1455:localhost:1455 user@remote

2. その SSH セッションで `codex login` を実行し、表示されたアドレスにローカルマシンからアクセスします。

## 代替モデルプロバイダー

構成ファイルで[カスタムモデルプロバイダー](/ja-JP/codex/config-file/config-advanced#custom-model-providers)を定義する場合は、次のいずれかの認証方法を選択できます：

- **OpenAI 認証**：OpenAI 認証を使用するには、`requires_openai_auth = true` を設定します。その後、ChatGPT または API キーでサインインできます。この方法は、LLM プロキシサーバー経由で OpenAI モデルにアクセスする場合に便利です。`requires_openai_auth = true` の場合、Codex は `env_key` を無視します。
- **環境変数による認証**：`env_key = "<ENV_VARIABLE_NAME>"` を設定すると、`<ENV_VARIABLE_NAME>` という名前のローカル環境変数に格納されたプロバイダー固有の API キーを使用します。
- **認証なし**：`requires_openai_auth` を設定せず（または `false` に設定し）、かつ `env_key` も設定しない場合、Codex はプロバイダーに認証が不要であると見なします。この方法はローカルモデルに便利です。
