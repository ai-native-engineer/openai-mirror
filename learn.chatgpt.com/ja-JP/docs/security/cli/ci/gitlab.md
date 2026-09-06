<!-- source: https://learn.chatgpt.com/ja-JP/docs/security/cli/ci/gitlab -->

GitLab CI/CD で Codex Security を実行し、コミット済みの変更と保護ブランチをスキャンして、検出結果を GitLab Security に公開します。必要に応じて、検証済みの修正をドラフトのマージリクエストで提案することもできます。

このワークフローでは、スキャン用の認証情報とリポジトリへの書き込み権限を分離します。生成された変更をマージする前には、必ず人によるレビューが必要です。

まずはスキャン結果の報告のみを行う構成から始めてください。修復を有効にするのは、プロジェクトのランナー、検出結果、認証情報を利用できる範囲を確認してからにしてください。

## 事前準備

次のものが必要です。

- Codex サンドボックスのユーザー名前空間に対応した、信頼できるランナーを備えた GitLab プロジェクト
- GitLab プロジェクトの Maintainer または Owner ロール（
[プロジェクトの CI/CD 変数](https://docs.gitlab.com/ci/variables/)と
  保護されたリソースの設定に必要）
- Codex Security へのアクセス権がある OpenAI API キー。Platform の API キーを使用する組織は、
  [Trusted Access for Cyber
  を申請](https://openai.com/form/enterprise-trusted-access-for-cyber/)できます。
  ChatGPT 認証を使用する個人は、[個人向け Trusted Access
  の手続き](https://chatgpt.com/cyber)を利用できます。一部のアカウントやリポジトリでは、
  リポジトリ全体のスキャンにこのアクセス権が必要です。
- [SARIF 2.1.0
  の取り込み](https://docs.gitlab.com/user/application_security/detect/sarif/)に必要な GitLab Ultimate 19.2 以降
- マージリクエストのジョブでマージベースを計算するための、完全な Git 履歴

パイプラインイメージには、Node.js 26、Python 3、Git、`rg`、
バージョンを固定した Codex Security CLI がインストールされます。自動修復にはさらに、
既存の回帰テストと、保護された認証情報を使わずに
リポジトリ側で制御されるコマンドを実行できるランナーが必要です。

## スキャン専用パイプラインの導入

マスク、非表示、保護を有効にした GitLab CI/CD 変数として、
`CODEX_SECURITY_API_KEY` を作成します。Codex Security へのアクセス権がある OpenAI Platform API キーを使用し、
環境スコープを `codex-security/openai` に設定してください。
[環境スコープを指定した CI/CD 変数](https://docs.gitlab.com/ci/environments/#limit-the-environment-scope-of-a-cicd-variable)を参照してください。

まず、この最小構成のパイプラインをテスト用プロジェクトに追加してください。このパイプラインは、対象条件を満たす保護されたマージリクエスト内のコミット済みの変更をスキャンし、成功したレポートジョブから SARIF を公開して、別のゲートでスキャナーの結果を復元します。

```yaml
stages:
  - security_scan
  - security_gate

.codex-security-merge-request:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID && $CI_MERGE_REQUEST_SOURCE_BRANCH_PROTECTED == "true" && $CI_MERGE_REQUEST_TARGET_BRANCH_PROTECTED == "true"'

codex-security:
  extends: .codex-security-merge-request
  stage: security_scan
  image: node:26-bookworm-slim
  environment:
    name: codex-security/openai
    action: access
  variables:
    GIT_DEPTH: "0"
  before_script:
    - npm install --prefix /tmp/codex-security-cli --ignore-scripts --no-audit --no-fund @openai/codex-security@0.1.20
  script:
    - |
      set -eu
      test -n "${CODEX_SECURITY_API_KEY:-}"

      CODEX_SECURITY_BIN="/tmp/codex-security-cli/node_modules/.bin/codex-security"
      RESULTS_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      ARTIFACT_DIR="codex-security-artifacts"
      BASE_REVISION="$(git merge-base \
        "$CI_MERGE_REQUEST_DIFF_BASE_SHA" "$CI_COMMIT_SHA")"
      install -d -m 700 "$RESULTS_DIR" "$ARTIFACT_DIR/results"

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY
      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          --diff "$BASE_REVISION" \
          --head "$CI_COMMIT_SHA" \
          --auth api-key \
          --output-dir "$RESULTS_DIR" \
          --json
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      case "$scan_exit" in
        0|1|2) ;;
        *) exit "$scan_exit" ;;
      esac

      "$CODEX_SECURITY_BIN" export "$RESULTS_DIR" \
        --export-format sarif \
        --source-root "$CI_PROJECT_DIR" \
        --output "$ARTIFACT_DIR/results.sarif"
      test -s "$ARTIFACT_DIR/results.sarif"
      cp -R "$RESULTS_DIR"/. "$ARTIFACT_DIR/results/"
      printf '%s\n' "$scan_exit" > "$ARTIFACT_DIR/scan-exit-code.txt"
      exit 0
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/results.sarif

codex-security-gate:
  extends: .codex-security-merge-request
  stage: security_gate
  image: alpine:3.20
  needs:
    - job: codex-security
      artifacts: true
  script:
    - exit "$(cat codex-security-artifacts/scan-exit-code.txt)"

  

シークレットが渡されるジョブを実行する前に、`.gitlab-ci.yml` へのすべての変更をレビューしてください。
この最小構成の例では、意図的にフルスキャンと修復を省いています。

## 本番用パイプラインの導入

1. [GitLab パイプラインの完全版をダウンロード](/codex/security/cli/ci/gitlab.yml)し、
   リポジトリのルートに `.gitlab-ci.yml` として保存します。
   リポジトリに既存のパイプラインがある場合は、この例のステージ、非表示のテンプレート、
   ジョブを既存のファイルに統合してください。
2. 既存のビルド、テスト、デプロイの各ステージは維持してください。
プロジェクトで `workflow: rules` を使用している場合は、
   スキャン対象のパイプラインイベントが許可されていることを確認してください。

この例では、`security_scan`、`security_remediation`、`security_publish`、
`security_gate` の各ステージを追加します。スキャン結果の報告のみを行う場合に必要なのは、
`CODEX_SECURITY_API_KEY` だけです。

デフォルトでは、スキャンジョブは同一プロジェクト内の
保護ブランチ間のマージリクエストに対してのみ実行されます。`CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH=true` を設定すると、
保護されたデフォルトブランチへのプッシュと、手動実行のパイプラインをスキャンできます。
`CODEX_SECURITY_SCHEDULED_DEEP_SCAN=true` を設定し、時間とコストの予算を明示的に指定すると、
保護されたデフォルトブランチで詳細スキャンのスケジュール実行を有効にできます。

マージリクエストのパイプラインが保護された変数とランナーにアクセスできるのは、次の条件をすべて満たす場合だけです。

- 同じプロジェクト内のソースブランチとターゲットブランチを保護していること
- プロジェクトで、[マージリクエストのパイプラインから保護された変数と
  ランナーへのアクセスが許可されている](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners)こと
- パイプラインを開始するユーザーに、ターゲットブランチへのプッシュまたはマージ権限があること

フォークのパイプラインや保護されていないマージリクエストには、
スキャン用の認証情報は渡されません。`.gitlab-ci.yml` への変更はすべて、
シークレットが渡されるジョブを実行する前にレビューしてください。変数をマスクして非表示にしても、
信頼できない CI コードが安全になるわけではありません。

## スキャンの実行と検出結果のレビュー

対象条件を満たす保護されたマージリクエストを作成するか、保護されたデフォルトブランチでパイプラインを実行してください。リポジトリ全体を対象とする有料スキャンを実行する前に、まずは小さな差分から始めてください。

`codex-security` ジョブを開き、アーティファクトに次のものが含まれていることを確認します。

- `scan-manifest.json`
- `findings.json`
- `coverage.json`
- `results.sarif`
- `scan-exit-code.txt`

次に、パイプラインの **セキュリティ** タブを開き、取り込み時の警告を確認し、
検出結果の識別子、重大度レベル、ソース内の位置を確認します。デフォルトブランチのスキャンでは、
プロジェクトの脆弱性レコードも作成されます。マージリクエストの検出結果は、
パイプラインのセキュリティタブまたはマージリクエストのセキュリティウィジェットに表示されますが、
プロジェクト全体の脆弱性レコードは作成されません。

スキャン結果には、脆弱性のあるソースコードの断片、根拠となる情報、修復の詳細が含まれる場合があるため、アーティファクトへのアクセスを制限してください。

## スキャンプロファイルの選択

パイプラインは、トリガーに応じて次のプロファイルを選択します。

| トリガー                                        | 対象          | モード       | 推論強度  |
| ---------------------------------------------- | --------------- | ---------- | ------- |
| 同一プロジェクト内の保護されたマージリクエスト           | コミット済みの差分  | `standard` | `low`   |
| 保護されたデフォルトブランチへのプッシュまたは手動実行（明示的な有効化が必要） | リポジトリ全体 | `standard` | `high`  |
| 保護されたデフォルトブランチでのスケジュール実行（明示的な有効化が必要）    | リポジトリ全体 | `deep`     | `xhigh` |

マージリクエストのスキャンでは、コミット済みの変更に絞ってフィードバックを提供します。デフォルトブランチのスキャンでは、統合後のリポジトリをレビューします。スケジュール実行の詳細スキャンでは、より広い範囲を定期的にスキャンします。完了した差分スキャンの結果が当てはまるのはその変更だけであり、リポジトリ全体に問題がないことを示すものではありません。

このワークフローは、リポジトリの外に CLI をインストールし、絶対パスで実行します。ドライランによる事前チェックでは、対象プロセスにのみ渡される API キーを使用しますが、有料スキャンは開始せず、API 認証、Codex Security へのアクセス権、クォータ、モデルの利用可否も検証しません。

このワークフローはスキャンの状態と結果を Worktree の外に書き込み、
`OPENAI_API_KEY` をスキャンプロセスにのみ渡します。CLI に渡されるのは、
明示的に指定された少数の環境変数であり、すべての GitLab 変数を継承することはありません。差分スキャンでは、
ワークフローがマージベースを計算し、レビュー済みのベースと
ヘッドの各リビジョンにスキャンを紐付けます。

この例では、`@openai/codex-security` のバージョンを `0.1.20` に固定しています。固定するバージョンを変更する前に、
認証、アーティファクト、SARIF の取り込み、ポリシーゲートの動作を再テストしてください。

## 報告とポリシーの強制適用の分離

GitLab は、成功したレポートジョブから SARIF を取り込みます。
パイプラインはまずレポートを公開し、
別の `codex-security-gate` ジョブでスキャナーの終了ステータスを復元します。

レポートジョブは、終了コードが `0` または `1` の場合に検出結果を受け入れます。
終了コードが `2` の場合に受け入れるのは、スキャンの完了がスキャンマニフェストで証明され、
カバレッジが明示的に `partial` であり、空でない SARIF レポートが存在する場合に限られます。
それ以外の実行時エラー、構成エラー、エクスポートの失敗は引き続き処理をブロックします。

最後のゲートでは、次のスキャナーの終了コードをそのまま保持します。

| 終了コード | 意味                                                                     |
| ---- | --------------------------------------------------------------------------- |
| `0`  | 対象範囲全体のスキャンが完了し、ポリシーの基準を満たしました。            |
| `1`  | スキャンが完了し、設定されたしきい値以上の問題が見つかりました。 |
| `2`  | スキャンのカバレッジが不完全だったか、入力エラーまたは実行時エラーが発生しました。              |

この例では、部分的なカバレッジの扱いを調整する間、終了コード `2` を一時的に許容します。
カバレッジが不完全な場合にパイプラインをブロックする必要があるなら、この許容設定を削除してください。

修正と公開は、最後のポリシーゲートより先に実行されます。条件を満たす検出事項があれば、その後ゲートがパイプラインを失敗させた場合でも、検証済みのドラフトマージリクエストを作成できます。

## 検証付き修正の有効化

自動修正は任意の機能で、保護されたデフォルトブランチのパイプラインでのみ実行されます。Codex の修正プロセスとリポジトリで管理される検証コマンドには、GitLab プロジェクトアクセストークンやランナーが注入する認証情報は渡されません。

セキュリティ上の保証は 3 つあります。リポジトリで管理されるコマンドには OpenAI や GitLab の認証情報を一切渡しません。リポジトリへの書き込み権限は公開ジョブだけに付与します。生成されたすべての変更は、人がレビューしてマージするまでドラフトのまま維持します。

ワークフローでは、次の処理を行います。

1. 完全なスキャンカバレッジと、重大度が `high` または `critical` の
   検出事項を必須とします
2. パッチ適用前に、設定された回帰テストが失敗することを確認します
3. 変更範囲を絞ったパッチを生成し、CI 関連ファイル、認証情報ファイル、バイナリファイル、その他の保護対象ファイルへの変更を拒否します
4. OpenAI、GitLab、レジストリ、デプロイ、ジョブトークンの認証情報を渡さずに回帰テストを実行します
5. `verify-fix` を使用して、`fixed`、`still_vulnerable`、`inconclusive` のいずれかを返します。
   ジョブがパッチを公開するのは、`verify-fix` が `fixed` を返し、
   検証プロセスでパッチが変更されなかった場合だけです

修正を有効にするには、次の保護された変数を設定してください。

- `CODEX_SECURITY_ENABLE_REMEDIATION` を `true` に設定してください。
- `CODEX_SECURITY_VERIFICATION_COMMAND` に、修正前は終了コード `1`、修正後は終了コード `0` で終了する
  既存の回帰テストを設定してください。
- 必要に応じて、`CODEX_SECURITY_SETUP_COMMAND` に、対話操作を必要としない
  依存関係のセットアップコマンドを設定してください。

特定の実装ではなく、根底にあるセキュリティの不変条件を検証する回帰テストを選んでください。生成されたテストの変更とソースの変更も、同じ厳密さで精査してください。

<details>
  <summary>上級：リポジトリのコマンドの分離</summary>

`validate`、`patch`、`verify-fix` コマンドには、プロセススコープの
`CODEX_API_KEY` が渡されます。リポジトリで管理されるセットアップコマンドとテストコマンドは、
追跡対象のソースファイルの書き込み可能なコピー内で、別の非特権ユーザーとして実行されます。
このコピーには、Git メタデータ、サブモジュールの内容、
ダウンロードしたアーティファクトを意図的に含めていません。`.git` や
サブモジュールが必要なセットアップコマンドとテストコマンドは、別途設計した、認証情報を持たないジョブで実行する必要があります。

正本のチェックアウトや、それに隣接する GitLab のファイル変数ディレクトリにアクセスできるのは、
root 所有の Codex ステップだけです。コピーのクリーンな環境に含まれるのは、
`PATH`、`HOME`、`LANG`、`CI`、`CI_PROJECT_DIR` だけです。コマンドにそれ以外の機密ではない値が必要な場合は、
コマンドをレビューしてから、その値を許可リストに追加してください。
ランナーでユーザーを切り替えられない場合は、修正を有効にする前に、
認証情報を持たない別のジョブに検証を移してください。

</details>

## ドラフトマージリクエストの公開

[GitLab のプロジェクト
アクセストークン](https://docs.gitlab.com/user/project/settings/project_access_tokens/#create-a-project-access-token)を、
Developer ロールと `api` および `write_repository` スコープで作成してください。
保護、マスク、非表示を設定した `GITLAB_REMEDIATION_TOKEN` として保存し、スコープは
`codex-security/publish` 環境だけに限定してください。

`CODEX_SECURITY_CREATE_MR=true` を設定して公開を有効にしてください。さらに、機密情報ではない変数
`CODEX_SECURITY_MR_TEST_COMMAND` に、生成されるすべての修正ブランチが合格しなければならない、
プロジェクト固有のセキュリティ回帰テストを設定してください。
生成された保護されていないマージリクエストからコマンドを読み取れるように、この変数は保護しないでください。
公開ワークフローでは、次の処理を行います。

- リポジトリへの書き込み用トークンを受け取りますが、OpenAI の認証情報は受け取りません
- `codex-security/fix-<finding-hash>` ブランチを作成します
- ドラフトマージリクエストを作成します。既にオープンなドラフトがある場合は、重複して作成せずに再利用します
- 保護されていない修正ブランチの回帰テストを、追跡対象ファイルだけを含むコピー内で、保護された認証情報を渡さずに非特権ユーザーとして実行します
- 生成された変更を自動でマージすることはありません

プロジェクトアクセストークンの代わりに `CI_JOB_TOKEN` を使わないでください。
必要なマージリクエストの作成操作を実行できません。
マージする前に、提案されたパッチ、検証の証拠、検出事項をレビューしてください。

## 任意の変数の設定

有効にする機能に必要な変数だけを設定してください。

| 変数                                  | 必要な場面                       | デフォルト値または用途                                          |
| ----------------------------------------- | --------------------------------- | ----------------------------------------------------------- |
| `CODEX_SECURITY_API_KEY`                  | すべてのスキャン                        | 保護、マスク、非表示を設定し、スコープを `codex-security/openai` に限定 |
| `CODEX_SECURITY_VERSION`                  | CLI のアップグレード                       | `0.1.20` にピン留め済み、変更前に再テストが必要                  |
| `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` | デフォルトブランチのフルスキャン         | 明示的な有効化が必要、デフォルトでは無効                             |
| `CODEX_SECURITY_SCHEDULED_DEEP_SCAN`      | スケジュール済みのディープスキャン              | 明示的な有効化が必要、デフォルトでは無効                             |
| `CODEX_SECURITY_DEEP_MAX_TIME_HOURS`      | スケジュール済みのディープスキャン              | `0` を超え、`8` 未満の時間予算が必須     |
| `CODEX_SECURITY_DEEP_MAX_COST`            | スケジュール済みのディープスキャン              | 推定コスト（USD）のガードレールが必須（`0` より大きい値）      |
| `CODEX_SECURITY_ENABLE_REMEDIATION`       | パッチの生成                  | 保護された変数で明示的に有効化、デフォルトでは無効                            |
| `CODEX_SECURITY_VERIFICATION_COMMAND`     | パッチの生成                  | 保護された変数で指定する回帰テスト                                   |
| `CODEX_SECURITY_SETUP_COMMAND`            | 修正用のセットアップ（任意）        | 保護された変数で指定する依存関係のインストール                           |
| `CODEX_SECURITY_REMEDIATION_EFFORT`       | 修正の調整（任意）       | `high`                                                      |
| `CODEX_SECURITY_MAX_CHANGED_FILES`        | パッチサイズの制限（任意）         | `8`、許容範囲は `1` から `20`                         |
| `CODEX_SECURITY_CREATE_MR`                | ドラフトマージリクエストの作成      | 保護された変数で明示的に有効化、デフォルトでは無効                            |
| `GITLAB_REMEDIATION_TOKEN`                | ドラフトマージリクエストの作成      | スコープを `codex-security/publish` に限定した Developer ロールのプロジェクトトークン  |
| `CODEX_SECURITY_GITLAB_INTERNAL_URL`      | セルフホスト環境での公開（任意）   | ランナーからアクセス可能な GitLab のオリジン                     |
| `CODEX_SECURITY_MR_TEST_COMMAND`          | ドラフトマージリクエストの公開    | 機密情報を含まないプロジェクト固有の回帰テスト（必須）       |
| `CODEX_SECURITY_MR_SETUP_COMMAND`         | 修復ブランチのセットアップ（任意） | 機密情報を含まない依存関係のセットアップ                                 |

GitLab が `CI_*` 変数を提供します。パイプラインが
`CODEX_SECURITY_BIN`、`CODEX_SECURITY_EFFORT`、`CODEX_SECURITY_MODE`、
`CODEX_SECURITY_STATE_DIR`、`CODEX_SECURITY_TARGET` を管理するため、これらを
プロジェクト変数として設定しないでください。差分スキャンでは、CLI が正規化されたベースリビジョンとヘッドリビジョンから
正規のスキャン対象識別子を導出します。

## ポリシー適用とコストの調整

マージリクエストへのフィードバックには対象を絞った差分スキャンを、デフォルトブランチには標準のリポジトリスキャンを、
より広範囲のカバレッジが必要な場合はスケジュール済みの詳細スキャンを使用してください。リポジトリ全体を対象とする
2 つのプロファイルは、どちらもデフォルトでは無効です。スケジュール済みの詳細スキャンには、
`CODEX_SECURITY_DEEP_MAX_TIME_HOURS` と `CODEX_SECURITY_DEEP_MAX_COST` も必要です。
CLI に割り当てる時間は、ジョブのタイムアウトである 8 時間未満にしてください。予算を設定する前に、代表的な実行を
計測してください。`--max-cost` は、厳密な請求額の上限ではなく、
推定コストに基づくガードレールとして扱ってください。

まずはレポートのみを出力するスキャンから始めてください。`--fail-on-severity` は、
代表的な検出結果、カバレッジ、コスト、実行時間をチームでレビューしてから追加してください。重大度のポリシーと終了コードの詳細は、[CI での
Codex Security の実行](/ja-JP/codex/security/cli/ci)を
参照してください。

ジョブが失敗した場合は、次の点を確認してください。

- スキャンのアーティファクトがない場合は、構成またはランナーに問題があると考えられます。
- アーティファクトはあるもののカバレッジが不完全な場合は、`coverage.json` をレビューしてください。
- GitLab に検出結果が表示されない場合は、SARIF レポートジョブが成功したか、
GitLab がレポートを受け付けたかを確認してください。
- 修復がスキップされた場合は、保護されたブランチであること、カバレッジが完全であること、
検出結果の重大度、検証コマンド、有効化用の変数を確認してください。
- 公開時にエラーが発生する場合は、プロジェクトトークンのロール、スコープ、
環境の制限を確認してください。

すべてのコマンド、フラグ、アーティファクトについては、[Codex Security CLI
リファレンス](/ja-JP/codex/security/cli/reference)を参照してください。
