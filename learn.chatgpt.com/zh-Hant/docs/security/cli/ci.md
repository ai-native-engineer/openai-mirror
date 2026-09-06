<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/cli/ci -->

在 CI 中執行 Codex Security CLI，審查 Pull Request 或合併請求中的確切變更，
保留發現項目與涵蓋範圍，並可選擇在達到指定嚴重性時讓檢查失敗。
先使用僅供參考的結果，審查掃描品質與執行時間，
再加入適合您程式碼庫的嚴重性政策。

  安裝公開的 `@openai/codex-security` 套件。執行掃描仍
  需要 Codex Security 存取權。

本指南提供 GitHub Actions 與 GitLab CI/CD 的範例。相同的掃描
和匯出指令也適用於其他 CI 系統。

## 準備工作流程

在 CI 供應商的密鑰儲存區中，將 OpenAI API 金鑰儲存為
`CODEX_SECURITY_API_KEY`。

將此密鑰直接對應至掃描步驟的 `OPENAI_API_KEY` 環境變數。
請將憑證的使用範圍限制於掃描程序，並使用
`--auth api-key` 明確選取該憑證。

僅對您信任的程式碼庫和 Pull Request 執行工作流程。掃描會使用
執行器的本機權限，且不會暫停以要求核准。掃描程序
可能繼承工作的環境，因此請勿將無關的 Token 和雲端憑證
放入該環境。

執行器需要：

- Node.js 22（22.13.0 或更新版本）、24 或 26。
- Python 3.10 或更新版本。
- 已發布的 `@openai/codex-security` 套件，安裝位置應在
  程式碼庫簽出目錄之外。
- Pull Request 或合併請求的來源分支與基底分支歷程，讓 Git 能計算
合併基底。

## 新增 GitHub Actions 工作流程

若是私人或內部程式碼庫，請先啟用
[GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)，
再上傳 SARIF。

建立 `.github/workflows/codex-security.yml`。簽出 Pull Request 前，請先
將 `@openai/codex-security` 安裝到
`$RUNNER_TEMP/codex-security`，讓受信任的可執行檔位於
`$RUNNER_TEMP/codex-security/node_modules/.bin/codex-security`：

```yaml
name: Codex Security scan

on:
  pull_request:

jobs:
  codex-security:
    if: github.event.pull_request.head.repo.full_name == github.repository && github.actor != 'dependabot[bot]'
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    steps:
      - name: Set up Node.js
        uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7
        with:
          node-version: "26"

      - name: Set up Python
        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7
        with:
          python-version: "3.14"

      - name: Install Codex Security
        run: |
          set -euo pipefail
          npm install \
            --prefix "$RUNNER_TEMP/codex-security" \
            --ignore-scripts \
            --no-audit \
            --no-fund \
            @openai/codex-security

      - name: Verify Codex Security
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
        run: |
          set -euo pipefail
          test -x "$CODEX_SECURITY_BIN"
          "$CODEX_SECURITY_BIN" --version

      - name: Check out the pull request
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Scan the pull request
        env:
          OPENAI_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          CODEX_SECURITY_STATE_DIR: ${{ runner.temp }}/codex-security-state
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
        run: |
          set -euo pipefail
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          "$CODEX_SECURITY_BIN" scan . \
            --diff "$BASE_REVISION" \
            --head "$HEAD_SHA" \
            --auth api-key \
            --output-dir "$SCAN_DIR" \
            --json > "$RUNNER_TEMP/codex-security.json"

      - name: Export SARIF
        id: export-sarif
        if: always()
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
          SARIF_FILE: ${{ runner.temp }}/codex-security.sarif
        run: |
          set -euo pipefail
          if test -f "$SCAN_DIR/scan-manifest.json"; then
            "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
              --export-format sarif \
              --source-root "$GITHUB_WORKSPACE" \
              --output "$SARIF_FILE"
            echo "available=true" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload SARIF
        if: always() && steps.export-sarif.outputs.available == 'true'
        uses: github/codeql-action/upload-sarif@e4fba868fa4b1b91e1fdab776edc8cfbe6e9fb81 # v4
        with:
          sarif_file: ${{ runner.temp }}/codex-security.sarif
          ref: refs/pull/${{ github.event.pull_request.number }}/head
          sha: ${{ github.event.pull_request.head.sha }}
          category: codex-security

      - name: Preserve scan results
        if: always()
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7
        with:
          name: codex-security-results
          path: |
            ${{ runner.temp }}/codex-security-results
            ${{ runner.temp }}/codex-security.json
          if-no-files-found: warn
          retention-days: 7

工作流程會簽出 Pull Request 的最新提交、計算其合併基底，並
掃描這兩個修訂版本之間已提交的變更。完整的歷程可確保
掃描目標準確。`persist-credentials: false` 可避免將程式碼庫 Token 寫入
簽出後的 Git 組態。先安裝 CLI 再簽出程式碼庫，並
透過絕對路徑執行 CLI，可避免程式碼庫控制的可執行檔取得
掃描憑證。`--auth api-key` 會明確選取限定使用範圍的 API 金鑰。
掃描會將歷程儲存在程式碼庫之外、
可寫入的狀態目錄中。

`--json` 會將一份完整的 JSON 文件寫入 stdout，讓工作流程可以直接儲存。
進度、完成摘要和錯誤仍會寫入 stderr。
這與 `codex exec --json` 不同，後者會輸出 JSON Lines 事件串流。

匯出步驟會讀取已完成且已密封的掃描，並寫入 SARIF，且不會變更
Codex 執行環境或憑證。掃描成品可能包含有漏洞的原始碼片段、
證據和修復詳細資料。請依據您的程式碼庫，選擇適當的存取控制和
較短的保留期限。

## 新增 GitLab CI/CD 管線

如需適用於正式環境的工作流程，包含受保護的預設分支掃描、可選擇啟用的排程深度掃描、
獨立的 SARIF 政策檢查，以及可選用的已驗證合併請求草稿，
請參閱[在 GitLab CI/CD 中
執行 Codex Security](/zh-Hant/codex/security/cli/ci/gitlab)。

GitLab Ultimate 19.2 或更新版本可匯入
[SARIF 2.1.0 報告](https://docs.gitlab.com/ci/yaml/artifacts_reports/#artifactsreportssarif)。
執行管線前，請新增已遮罩且隱藏的
`CODEX_SECURITY_API_KEY` CI/CD 變數。

以下最精簡範例會將僅執行掃描的 `security` 工作加入根目錄的
`.gitlab-ci.yml`。請保留檔案中現有的所有階段和工作。此範例預設會掃描
合併請求的變更。將 `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH`
設為 `"true"`，即可一併掃描整個預設分支：

```yaml
variables:
  CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH: "false"

stages:
  - test
  - security

codex-security:
  stage: security
  image: node:26-bookworm-slim
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "diff"
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH && $CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH == "true"'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "full"
  variables:
    GIT_DEPTH: "0"
    CODEX_SECURITY_CLI_DIR: "/tmp/codex-security-cli"
  before_script:
    - |
      set -eu
      apt-get update -qq
      apt-get install -y -qq --no-install-recommends \
        ca-certificates \
        git \
        python3 \
        ripgrep
      npm install \
        --prefix "$CODEX_SECURITY_CLI_DIR" \
        --ignore-scripts \
        --no-audit \
        --no-fund \
        @openai/codex-security@0.1.20

      test -x "$CODEX_SECURITY_BIN"
      "$CODEX_SECURITY_BIN" --version
  script:
    - |
      set -eu
      if test -z "${CODEX_SECURITY_API_KEY:-}"; then
        echo "Set the CODEX_SECURITY_API_KEY CI/CD variable." >&2
        exit 2
      fi

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      case "${CODEX_SECURITY_SCAN_SCOPE:-}" in
        diff)
          BASE_SHA="$CI_MERGE_REQUEST_DIFF_BASE_SHA"
          HEAD_SHA="$CI_COMMIT_SHA"
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          set -- --diff "$BASE_REVISION" --head "$HEAD_SHA"
          echo "Scanning committed changes from $BASE_REVISION to $HEAD_SHA."
          ;;
        full)
          set -- --mode standard
          echo "Scanning the complete default branch at $CI_COMMIT_SHA."
          ;;
        *)
          echo "Unsupported Codex Security scan scope: ${CODEX_SECURITY_SCAN_SCOPE:-unset}" >&2
          exit 2
          ;;
      esac

      SCAN_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      JSON_FILE="/tmp/codex-security-$CI_JOB_ID.json"
      SARIF_FILE="/tmp/codex-security-$CI_JOB_ID.sarif"

      install -d -m 700 "$CODEX_SECURITY_STATE_DIR" "$SCAN_DIR"

      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          "$@" \
          --auth api-key \
          --output-dir "$SCAN_DIR" \
          --json > "$JSON_FILE"
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      install -d -m 700 codex-security-artifacts/results
      cp -R "$SCAN_DIR"/. codex-security-artifacts/results/
      if test -s "$JSON_FILE"; then
        cp "$JSON_FILE" codex-security-artifacts/codex-security.json
      fi
      printf '%s\n' "$scan_exit" > codex-security-artifacts/scan-exit-code.txt

      export_exit=0
      if test -f "$SCAN_DIR/scan-manifest.json"; then
        set +e
        "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
          --export-format sarif \
          --source-root "$CI_PROJECT_DIR" \
          --output "$SARIF_FILE"
        export_exit="$?"
        set -e
        if test -s "$SARIF_FILE"; then
          cp "$SARIF_FILE" codex-security-artifacts/codex-security.sarif
        fi
      fi

      if test "$scan_exit" -ne 0; then
        exit "$scan_exit"
      fi
      exit "$export_exit"
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/codex-security.sarif

依預設，此工作只會針對同一專案內各分支提出的合併請求執行，
因此分支專案的管線不會取得掃描憑證。在群組、專案或管線層級，將
`CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` 設為 `"true"`，
即可一併對預設分支執行標準完整掃描。
完整掃描比差異掃描更耗時，成本也更高。

`GIT_DEPTH: "0"` 會提供必要的歷程，讓合併請求掃描能依據
`CI_MERGE_REQUEST_DIFF_BASE_SHA` 和 `CI_COMMIT_SHA` 計算合併基底。

此工作會將 CLI 安裝在 `/tmp` 下，以絕對路徑執行，
且只向掃描程序提供 API 金鑰。`artifacts: when: always` 會在掃描失敗時保留 SARIF 報告，
而 `artifacts:access: maintainer` 則會限制
詳細掃描結果的存取權。

變更 `.gitlab-ci.yml` 可能會暴露 CI/CD 變數，
因此請在執行工作前審查管線變更。如果您
[將 `CODEX_SECURITY_API_KEY` 設為受保護](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners)，
GitLab 只會對同一專案內受保護分支之間的合併請求提供該變數，
且使用者必須有權存取目標分支。

本節開頭連結的 GitLab 專用指南會將這個最精簡工作擴充為
適用於正式環境的工作流程。

## 選擇嚴重性政策

兩個範例都未指定 `--fail-on-severity`，因此僅提供報告。
準備好讓發現項目影響檢查結果後，請在掃描指令中
加入門檻值：

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --fail-on-severity high

支援的門檻值為 `critical`、`high`、`medium` 和 `low`。
門檻值涵蓋本次掃描中嚴重性達到該層級或更高的發現項目。
程式碼庫摘要中顯示的先前尚未解決的發現項目，不會影響此政策的判定。

掃描步驟會使用以下結束代碼：

| 結束代碼  | 意義                                                                                 |
| ----- | --------------------------------------------------------------------------------------- |
| `0`   | 掃描已完成且涵蓋範圍完整，所有已設定的政策也都已通過。            |
| `1`   | 已完成的掃描包含嚴重性達到或超過門檻值的發現項目。                        |
| `2`   | CLI 發現輸入或執行階段錯誤，或已完成掃描的涵蓋範圍不完整。 |
| `130` | Ctrl-C 中斷了掃描。                                                            |
| `143` | SIGTERM 終止了掃描。                                                            |

涵蓋範圍為 `partial` 或 `unknown` 的掃描會傳回 `2`，即使未設定嚴重性政策也是如此。
CLI 仍會寫入目前可用的發現項目與涵蓋範圍資訊。
在將檢查結果視為定論前，請先審查 `coverage.json` 中延後掃描的區域。

## 使用現有結果目錄重試

每個 CI 工作都應使用全新的執行器目錄。
若使用常駐或自行託管的執行器，請使用 `--archive-existing` 保留先前的結果：

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --archive-existing

此指令會封存先前的結果，並從空的掃描目錄開始。

## CI 掃描疑難排解

- **不明的 Git 參照或非預期的差異：** 請擷取基底分支與來源分支的歷程，
  計算合併基底，並明確傳入這兩個修訂版本。
- **受保護或非空的輸出目錄：** 請在所屬 Git 工作樹之外
  選擇私人目錄。如果目錄已包含結果，
  請使用 `--archive-existing`。
- **缺少憑證：** 請確認 `CODEX_SECURITY_API_KEY` 可供
  受信任的工作流程或管線使用，且已直接對應至掃描程序的
`OPENAI_API_KEY` 環境變數。
- **掃描歷程錯誤：** 請將 `CODEX_SECURITY_STATE_DIR` 設為程式碼庫之外
  可寫入的目錄。
- **Python 設定錯誤：** 請確認執行器使用 Python 3.10 或更新版本。
- **涵蓋範圍不完整：** 請審查 `coverage.json`，包括延後掃描的範圍
  和尚待釐清的問題，然後使用適當的目標或環境重新執行。
- **SARIF 匯出錯誤：** 請確認掃描已完成，
  且完整的掃描目錄可供使用。匯出程序會先驗證已密封的成品，再寫入
  SARIF。
- **SARIF 上傳錯誤：** 若使用 GitHub Actions，請確認您的組織
  已為該程式碼庫啟用 GitHub Code Security，且工作流程授予
`actions: read`、`contents: read` 和 `security-events: write` 權限。
  若使用 GitLab CI/CD，請確認專案使用 GitLab Ultimate 19.2 或更新版本，
  且工作會透過 `artifacts:reports:sarif` 上傳 SARIF 2.1.0 檔案。

如需瞭解所有指令、旗標、成品和輸出欄位，請參閱 [CLI
參考資料](/zh-Hant/codex/security/cli/reference)。如需使用外掛程式進行互動式 CI 審查，
請參閱[審查程式碼變更的安全性](/zh-Hant/codex/security/plugin/code-changes#automate-reviews-in-cicd)。
