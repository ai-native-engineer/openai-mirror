<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/plugin/code-changes -->

對由 Git 追蹤的單一變更集執行安全性變更審查，以找出安全性迴歸問題。
Codex 會審查每個已變更、具原始碼性質的檔案，以及直接支援該檔案的程式碼。
審查範圍不會擴大為整個程式碼庫的完整稽核。

若要掃描整個程式碼庫而非特定變更，請參閱[執行安全性
掃描](/zh-Hant/codex/security/plugin/scans)。

## 執行手動審查

在桌面 App 中，開啟 **安全性**，選取 **掃描**，再選取 **+ 掃描**。
選擇程式碼庫，然後選取 **變更**。可審查未提交的變更、
單一提交，或基準與頂端修訂版本。 **深度掃描** 無法用於
變更掃描。

您也可以在對話中要求 Codex 審查未提交的變更：

```text
Use $codex-security:security-diff-scan to review my current uncommitted changes for security regressions.

針對提交或分支範圍，請視需要指定兩個修訂版本：

```text
Use $codex-security:security-diff-scan to review the changes from origin/main to HEAD for security regressions. Focus on authentication, authorization, input handling, filesystem access, network requests, and secrets.

如果 Pull Request 的基準與頂端修訂版本可在本機簽出內容中使用，
也可以直接指定該 Pull Request。

## 在設定中確認變更

1. 選取 **變更**。
2. 確認已簽出的程式碼庫、目前分支和最新提交。
3. 在 **要審查的變更**下方，選擇：
   - `Uncommitted changes`，用於目前的工作樹。
   - 最新提交，用於單一提交審查。
   - 分支或 Pull Request 範圍的基準與頂端修訂版本。
4. 確認摘要描述的是您要審查的變更。
5. 選取 **開始掃描**。

Codex 不會簽出其他分支，也不會切換所選的工作樹。如果
要求的修訂版本無法在本機使用，請在審查前擷取該版本，或
提供可在本機使用的基準與頂端修訂版本。

## 處理發現項目

審查結果後，[修正並驗證已接受的
發現項目](/zh-Hant/codex/security/plugin/fix-findings)，或[匯出並追蹤
發現項目](/zh-Hant/codex/security/plugin/export-findings)。

## 在 CI/CD 中自動執行審查

如果您可以使用 Beta 版獨立 CLI，請參閱[在 CI 中執行
Codex Security](/zh-Hant/codex/security/cli/ci)，瞭解結構化 JSON、嚴重性政策和 SARIF
上傳。如需透過已安裝的外掛程式技能執行，請繼續閱讀本節，
並使用 `codex exec` 叫用。

如果要在 CI 中執行 `$codex-security:security-diff-scan`，執行器必須能以非互動方式叫用
Codex CLI。首先，安裝 CLI，並避免暴露掃描
憑證：

```bash
npm install --global @openai/codex

在 CLI 中安裝 Codex Security 外掛程式：

```bash
codex plugin add codex-security@openai-curated

安裝指令使用公開的 Codex CLI 外掛程式市集。請先查看
[外掛程式更新日誌](/zh-Hant/codex/security/plugin/changelog)，再於 CI 中依賴
特定外掛程式版本或功能。

接著，將 CI 祕密儲存區中的 OpenAI API 金鑰提供為
`CODEX_SECURITY_API_KEY`。僅在掃描時提供這項憑證：

```bash
CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
  --sandbox workspace-write \
  "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

可寫入的沙盒可讓掃描建立暫存成品。提示詞
仍要求 Codex 保持原始碼簽出內容不變。

掃描會將輸出寫入
`$TMPDIR/codex-security-scans/<repository>/<scan-id>/`：

| 檔案                 | 內容                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `report.md`          | 用來查閱完整掃描目錄的主要入口。                                                                                              |
| `findings/<slug>/`   | 如有要求，提供詳細漏洞報告及佐證用的概念驗證檔案。                                                                     |
| `hardening/`         | 如有要求，提供結構性強化指引及相關提案。                                                                                   |
| `findings.json`      | 包含穩定識別碼、嚴重性、可信度、原始碼位置及修復措施的發現項目。將其提供給經核准的內部安全性工作流程或下游工具。 |
| `scan-manifest.json` | 經密封的掃描收據，包含審查目標、修訂版本及成品雜湊值。                                                                             |
| `coverage.json`      | 已審查及延後處理的範圍、排除項目，以及涵蓋範圍的完整度。                                                                                    |

[`findings.json` 結構描述](https://github.com/openai/plugins/blob/main/plugins/codex-security/schemas/findings.schema.json)
定義完整結構。此結構描述包含以下欄位：

| 欄位                     | 類型   | 描述                                                            |
| ------------------------- | ------ | ---------------------------------------------------------------------- |
| `documentType`            | 字串 | 將文件識別為 `codex-security.findings`。                  |
| `schemaVersion`           | 字串 | 識別發現項目結構描述的版本。                                |
| `scanId`                  | 字串 | 識別產生這些發現項目的掃描。                        |
| `findings`                | 陣列  | 包含零個或多個發現項目物件。                                 |
| `findings[].findingId`    | 字串 | 由發現項目指紋衍生的穩定發現項目識別碼。        |
| `findings[].occurrenceId` | 字串 | 識別發現項目在特定掃描中出現的個別實例。          |
| `findings[].ruleId`       | 字串 | 識別漏洞系列。                                   |
| `findings[].identity`     | 物件 | 包含語意錨點及選用的同層執行個體識別碼。 |
| `findings[].fingerprints` | 物件 | 包含指紋演算法和主要指紋。            |
| `findings[].title`        | 字串 | 提供發現項目的簡短標題。                                      |
| `findings[].summary`      | 字串 | 概述漏洞及其影響。                           |
| `findings[].severity`     | 物件 | 包含嚴重性等級和選用的評分詳細資料。              |
| `findings[].confidence`   | 物件 | 包含可信度等級及其判定依據。                           |
| `findings[].taxonomy`     | 物件 | 包含漏洞類別和 CWE 識別碼。               |
| `findings[].locations`    | 陣列  | 列出受影響的檔案、行號和位置角色。                |
| `findings[].remediation`  | 字串 | 說明建議的修正方式。                                         |
| `findings[].provenance`   | 物件 | 識別發現項目的來源。                                  |

例如，此指令會針對每個發現項目列印一列以 Tab 分隔的資料：

```bash
jq -r '
  .findings[] |
  [.findingId, .severity.level, .confidence.level, .locations[0].path, .locations[0].startLine, .title] |
  @tsv
' findings.json

這些範例假設受信任的 Linux 執行器已安裝 Node.js 與 `npm`、Git、Python
3、`jq`，以及供應商的指令列工具。`npm` 的全域套件前綴
必須可寫入。

依您使用的 CI 供應商選擇對應範例：

掃描結果可能包含敏感的漏洞詳細資料。請將成品
設為私密，並且只有在審查分享對象、內容和
所需的核准後，才發布發現項目。

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

建立已遮罩的 `CODEX_SECURITY_API_KEY` CI/CD 變數，並在分享發現項目前以非公開方式審查掃描
成品。

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

在 Azure Repos 中，設定一項 **建置驗證** 分支原則，以便在 Pull Request 上執行
管線。

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

這些範例會略過來自分支程式碼庫的 Pull Request。使用憑證的作業只能從
受保護的管線定義執行，且僅限受信任且可使用掃描
憑證的貢獻者。請封存 `codex-security-scans`，將結構化的發現項目、
資訊清單、涵蓋範圍和 `report.md`，以及任何要求提供的
`findings/` 或 `hardening/` 輸出一併保存。初期請讓結果僅供參考，並先審查
涵蓋範圍和執行時間，再將作業設為必要檢查。

如需 API 金鑰處理與沙盒控制的相關資訊，請參閱 [非互動
模式](/zh-Hant/codex/non-interactive-mode)。若您的組織允許使用 [Codex
GitHub Action](/zh-Hant/codex/github-action)，該 GitHub Action 可在執行階段安裝 CLI，但
您仍須先安裝外掛程式，並將該 GitHub Action 的 `codex-home`
輸入指向同一個 `CODEX_HOME`。
