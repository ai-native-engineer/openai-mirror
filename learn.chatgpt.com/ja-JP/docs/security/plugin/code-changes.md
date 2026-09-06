<!-- source: https://learn.chatgpt.com/ja-JP/docs/security/plugin/code-changes -->

Git で管理された 1 つの変更セットを対象にセキュリティレビューを実行し、リグレッションを検出します。
Codex は、変更されたソースコードに類する各ファイルと、それらを直接支えるコードをレビューします。
レビュー対象がリポジトリ全体の監査に拡大されることはありません。

特定の変更ではなくリポジトリ全体をスキャンするには、[セキュリティスキャンの
実行](/ja-JP/codex/security/plugin/scans)を参照してください。

## 手動レビューの実行

デスクトップアプリで **セキュリティ**を開き、 **スキャン**、 **+ スキャン**の順に選択します。
リポジトリを選択してから、 **変更**を選択します。未コミットの変更、
単一のコミット、またはベースとヘッドのリビジョンをレビューできます。 **詳細スキャン** は
変更のスキャンでは利用できません。

会話で Codex に未コミットの変更をレビューするよう依頼することもできます。

```text
Use $codex-security:security-diff-scan to review my current uncommitted changes for security regressions.

コミットまたはブランチの範囲を指定する場合は、必要に応じて両方のリビジョンを指定します。

```text
Use $codex-security:security-diff-scan to review the changes from origin/main to HEAD for security regressions. Focus on authentication, authorization, input handling, filesystem access, network requests, and secrets.

Pull Request のベースとヘッドのリビジョンをローカルのチェックアウトで利用できる場合は、
その Pull Request を指定することもできます。

## セットアップでの変更内容の確認

1. **変更**を選択します。
2. チェックアウトしているリポジトリ、現在のブランチ、最新のコミットを確認します。
3. **レビュー対象の変更**で、次のいずれかを選択します。
   - 現在の作業ツリーを対象とする `Uncommitted changes`
   - 単一コミットをレビューする場合は最新のコミット
   - ブランチまたは Pull Request の範囲をレビューする場合はベースとヘッドのリビジョン
4. 要約に、レビューしようとしている変更内容が記載されていることを確認します。
5. **スキャンを開始**を選択します。

Codex は別のブランチをチェックアウトしたり、選択した作業ツリーを切り替えたりしません。
指定したリビジョンがローカルにない場合は、レビュー前にフェッチするか、
ローカルで利用できるベースとヘッドを指定してください。

## 検出結果への対応

結果をレビューした後、[受け入れた検出結果の修正と
検証](/ja-JP/codex/security/plugin/fix-findings)、または[検出結果のエクスポートと
追跡](/ja-JP/codex/security/plugin/export-findings)を行います。

## CI/CD でのレビューの自動化

ベータ版のスタンドアロン CLI を利用できる場合は、[CI で Codex Security を
実行](/ja-JP/codex/security/cli/ci)を参照し、構造化 JSON、重大度ポリシー、SARIF の
アップロードについて確認してください。インストール済みのプラグインスキルを
`codex exec` で呼び出す場合は、このセクションを読み進めてください。

ランナーが
Codex CLI を非対話形式で呼び出せる場合は、CI で `$codex-security:security-diff-scan` を実行します。まず、スキャン用の
認証情報を公開せずに CLI をインストールします。

```bash
npm install --global @openai/codex

CLI に Codex Security プラグインをインストールします。

```bash
codex plugin add codex-security@openai-curated

インストールコマンドは、公開されている Codex CLI のプラグインマーケットプレイスを使用します。
[プラグインの変更履歴](/ja-JP/codex/security/plugin/changelog)は、CI で特定の
プラグインバージョンや機能に依存する前に確認してください。

次に、CI のシークレットストアにある OpenAI API キーを
`CODEX_SECURITY_API_KEY` として指定します。認証情報はスキャンの実行時にのみ渡してください。

```bash
CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
  --sandbox workspace-write \
  "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

書き込み可能なサンドボックスでは、スキャン時に一時アーティファクトを作成できます。
ただし、プロンプトでは Codex に、チェックアウトしたソースを変更しないよう求めています。

スキャン結果は
`$TMPDIR/codex-security-scans/<repository>/<scan-id>/` に書き込まれます。

| ファイル                 | 内容                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `report.md`          | スキャンディレクトリ全体を確認するための、人が読める主要なエントリーポイント。                                                                                              |
| `findings/<slug>/`   | 要求された場合に生成される、詳細な脆弱性レポートと裏付けとなる概念実証ファイル。                                                                     |
| `hardening/`         | 要求された場合に提供される、構造的なセキュリティ強化に関するガイダンスと関連する提案。                                                                                   |
| `findings.json`      | 安定した識別子、重大度、信頼度、ソース内の位置、修正方法を含む検出結果。承認済みの社内セキュリティワークフローまたは後続ツールに取り込みます。 |
| `scan-manifest.json` | レビュー対象、リビジョン、アーティファクトのハッシュを含む、封印済みのスキャンレシート。                                                                             |
| `coverage.json`      | レビュー済みおよび保留中の対象領域、除外事項、カバレッジの完全性。                                                                                    |

[`findings.json` のスキーマ](https://github.com/openai/plugins/blob/main/plugins/codex-security/schemas/findings.schema.json)に、
構造全体が定義されています。このスキーマには、次のフィールドが含まれます。

| フィールド                     | 型   | 説明                                                            |
| ------------------------- | ------ | ---------------------------------------------------------------------- |
| `documentType`            | 文字列 | ドキュメントを `codex-security.findings` として識別します。                  |
| `schemaVersion`           | 文字列 | 検出結果スキーマのバージョンを識別します。                                |
| `scanId`                  | 文字列 | 検出結果を生成したスキャンを識別します。                        |
| `findings`                | 配列  | 0 個以上の検出結果オブジェクトを格納します。                                 |
| `findings[].findingId`    | 文字列 | 検出結果のフィンガープリントから導出される、安定した検出結果識別子。        |
| `findings[].occurrenceId` | 文字列 | 特定のスキャンにおける、その検出結果の発生を識別します。          |
| `findings[].ruleId`       | 文字列 | 脆弱性のファミリーを識別します。                                   |
| `findings[].identity`     | オブジェクト | セマンティックアンカーと、省略可能な兄弟インスタンス識別子を格納します。 |
| `findings[].fingerprints` | オブジェクト | フィンガープリントアルゴリズムと主要なフィンガープリントを格納します。            |
| `findings[].title`        | 文字列 | 検出結果の短いタイトルを示します。                                      |
| `findings[].summary`      | 文字列 | 脆弱性とその影響の概要を示します。                           |
| `findings[].severity`     | オブジェクト | 重大度レベルと、省略可能なスコアの詳細が含まれます。              |
| `findings[].confidence`   | オブジェクト | 信頼度レベルとその根拠が含まれます。                           |
| `findings[].taxonomy`     | オブジェクト | 脆弱性のカテゴリと CWE 識別子が含まれます。               |
| `findings[].locations`    | 配列  | 影響を受けるファイル、行番号、該当箇所の役割を列挙します。                |
| `findings[].remediation`  | 文字列 | 推奨される修正方法を説明します。                                         |
| `findings[].provenance`   | オブジェクト | 検出結果の生成元を識別します。                                  |

たとえば、次のコマンドは検出結果ごとにタブ区切りのデータを 1 行出力します：

```bash
jq -r '
  .findings[] |
  [.findingId, .severity.level, .confidence.level, .locations[0].path, .locations[0].startLine, .title] |
  @tsv
' findings.json

これらの例では、Node.js と `npm`、Git、Python 3、
`jq`、プロバイダーのコマンドラインツールを備えた信頼できる Linux ランナーを前提としています。`npm` のグローバルパッケージのプレフィックスは、
書き込み可能である必要があります。

利用する CI プロバイダーに対応する例を選択してください：

スキャン結果には、機密性の高い脆弱性の詳細が含まれる場合があります。アーティファクトは非公開に保ち、公開対象者、内容、必要な承認を確認したうえでのみ、検出結果を公開してください。

  <div slot="github">

```yaml
name: Codex Security review

on:
  pull_request:

jobs:
  security-review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Install Codex Security
        env:
          CODEX_HOME: ${{ runner.temp }}/codex-home
        run: |
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated

      - name: Review code changes
        env:
          CODEX_SECURITY_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_HOME: ${{ runner.temp }}/codex-home
          TMPDIR: ${{ runner.temp }}/codex-security
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_REVISION: ${{ github.event.pull_request.head.sha }}
        run: |
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_REVISION")"
          CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
            --sandbox workspace-write \
            "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: codex-security-review
          path: ${{ runner.temp }}/codex-security/codex-security-scans

  </div>

  <div slot="gitlab">

マスクされた CI/CD 変数 `CODEX_SECURITY_API_KEY` を作成し、
検出結果を共有する前にスキャンアーティファクトを非公開でレビューしてください。

```yaml
codex-security-review:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
  variables:
    GIT_DEPTH: "0"
  script:
    - |
      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
      CODEX_API_KEY="$codex_security_api_key" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
  after_script:
    - |
      unset CODEX_SECURITY_API_KEY
      scan_root="/tmp/codex-security-$CI_JOB_ID/codex-security-scans"
      if [ -d "$scan_root" ]; then
        tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
      fi
  artifacts:
    when: always
    paths:
      - codex-security-artifacts.tar.gz

  </div>

  <div slot="azure">

```yaml
trigger: none

pool:
  vmImage: ubuntu-latest

steps:
  - checkout: self
    fetchDepth: 0

  - bash: |
      set -euo pipefail

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
    displayName: Install Codex Security

  - bash: |
      set -euo pipefail

      CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
    displayName: Review code changes
    condition: and(succeeded(), ne(variables['System.PullRequest.IsFork'], 'True'))
    env:
      CODEX_SECURITY_API_KEY: $(CODEX_SECURITY_API_KEY)

  - publish: $(Agent.TempDirectory)/codex-security/codex-security-scans
    artifact: codex-security-review
    condition: always()

Azure Repos では、 **ビルド検証** のブランチポリシーを設定し、
Pull Request に対してパイプラインが実行されるようにしてください。

  </div>

  <div slot="jenkins">

```groovy
pipeline {
  agent { label 'linux' }
  stages {
    stage('Codex Security review') {
      when {
        allOf {
          changeRequest()
          expression { !env.CHANGE_FORK?.trim() }
        }
      }
      steps {
        sh '''#!/usr/bin/env bash
          set -euo pipefail

          mkdir -p "$TMPDIR"
          git fetch --no-tags origin "$CHANGE_TARGET"
          target="$(git rev-parse FETCH_HEAD)"
          git fetch --no-tags origin "$CHANGE_BRANCH"
          git rev-parse FETCH_HEAD > "$TMPDIR/head"
          git merge-base "$target" "$(cat "$TMPDIR/head")" > "$TMPDIR/base"
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated
        '''
        withCredentials([string(credentialsId: 'codex-security-api-key', variable: 'CODEX_SECURITY_API_KEY')]) {
          sh '''#!/usr/bin/env bash
            set +x
            set -euo pipefail

            CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
              --sandbox workspace-write \
              "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
          '''
        }
      }
      post {
        always {
          sh '''#!/usr/bin/env bash
            set -euo pipefail
            scan_root="/tmp/codex-security-$BUILD_TAG/codex-security-scans"
            if [ -d "$scan_root" ]; then
              tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
            fi
          '''
          archiveArtifacts artifacts: 'codex-security-artifacts.tar.gz', allowEmptyArchive: true
        }
      }
    }
  }
}

  </div>

これらの例では、フォークリポジトリからの Pull Request をスキップします。
認証情報を使用するジョブは、保護されたパイプライン定義からのみ実行し、
スキャン用認証情報の取り扱いを信頼して任せられるコントリビューターのみを対象にしてください。`codex-security-scans` をアーカイブして、構造化された検出結果、
マニフェスト、カバレッジ、`report.md` をまとめて保管し、要求された場合は
`findings/` または `hardening/` の出力も含めてください。まずは結果を参考情報として扱い、
ジョブを必須チェックにする前に、カバレッジと実行時間を確認してください。

API キーの取り扱いとサンドボックスの制御については、[非対話
モード](/ja-JP/codex/non-interactive-mode)を参照してください。組織で [Codex
GitHub Action](/ja-JP/codex/github-action) の使用が許可されている場合は、このアクションで実行時に CLI をインストールできますが、
先にプラグインをインストールし、アクションの `codex-home`
入力に同じ `CODEX_HOME` を指定する必要があります。
