<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/cli/ci/gitlab -->

在 GitLab CI/CD 中執行 Codex Security，掃描已提交的變更與受保護的分支，
將檢出項目發布至 GitLab Security，並可選擇透過合併請求草稿
提出已驗證的修正。

此工作流程將掃描憑證與程式碼庫寫入權限分開。
產生的變更一律須經人工審查才能合併。

請先從僅掃描並回報結果開始。確認專案的執行器、檢出項目與憑證權限範圍後，
再啟用修復功能。

## 開始之前

你需要：

- 一個 GitLab 專案，具備可信任的執行器，
且該執行器支援 Codex 沙盒的使用者命名空間。
- 在 GitLab 專案中擁有維護者或擁有者角色，以便設定
[專案 CI/CD 變數](https://docs.gitlab.com/ci/variables/)與受保護的
  資源。
- 具備 Codex Security 存取權的 OpenAI API 金鑰。使用 Platform API 金鑰的組織
  可[申請
  Trusted Access for Cyber](https://openai.com/form/enterprise-trusted-access-for-cyber/)。
  使用 ChatGPT 身分驗證的個人可使用[個人 Trusted Access
  流程](https://chatgpt.com/cyber)。部分帳戶或程式碼庫需要具備此
  存取權，才能掃描整個程式碼庫。
- GitLab Ultimate 19.2 或更新版本，以支援[匯入
  SARIF 2.1.0](https://docs.gitlab.com/user/application_security/detect/sarif/)。
- 完整的 Git 歷史紀錄，以便合併請求作業計算合併基底。

管線映像檔會安裝 Node.js 26、Python 3、Git、`rg`，以及固定版本的
Codex Security CLI。自動修復還需要既有的
回歸測試，以及能在不持有受保護憑證的情況下
執行由程式碼庫控制的指令的執行器。

## 從僅執行掃描的管線開始

建立已遮罩、隱藏且受保護的 GitLab CI/CD 變數，名稱為
`CODEX_SECURITY_API_KEY`。使用具備 Codex Security
存取權的 OpenAI Platform API 金鑰，並將此變數的環境範圍設為 `codex-security/openai`。請參閱
[限定環境範圍的 CI/CD 變數](https://docs.gitlab.com/ci/environments/#limit-the-environment-scope-of-a-cicd-variable)。

請先將這個精簡管線加入測試專案。它會掃描符合資格且受保護的合併請求中已提交的變更，
透過成功完成的報告作業發布 SARIF，
再於獨立關卡中還原掃描器的結果：

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

  

執行含有機密的作業前，請先審查 `.gitlab-ci.yml` 的每項變更。
這個精簡範例刻意省略完整掃描與修復功能。

## 採用正式環境管線

1. [下載完整的 GitLab 管線](/codex/security/cli/ci/gitlab.yml)，
   並將它存為程式碼庫根目錄中的 `.gitlab-ci.yml`。如果程式碼庫
   已有管線，請將範例中的階段、隱藏範本和
   作業合併至現有檔案。
2. 保留既有的建置、測試和部署階段。若專案使用
`workflow: rules`，請確認它允許你要掃描的
   管線事件。

此範例會新增 `security_scan`、`security_remediation`、`security_publish`，
以及 `security_gate` 階段。只進行掃描與回報時，僅需
`CODEX_SECURITY_API_KEY`。

預設情況下，掃描作業只會針對同一專案中
受保護分支之間的合併請求執行。設定 `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH=true`，即可掃描
受保護預設分支的推送與手動執行的管線。設定
`CODEX_SECURITY_SCHEDULED_DEEP_SCAN=true`，並明確設定時間與費用
預算，即可在受保護的預設分支上啟用排程深度掃描。

合併請求管線必須符合以下條件，才能存取受保護的變數與執行器：

- 來源與目標分支位於同一專案，且皆已設為受保護分支。
- 專案[允許合併請求管線存取受保護的變數與
  執行器](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners)。
- 啟動管線的使用者可以推送至目標分支，或將變更合併至該分支。

分支程式碼庫的管線與未受保護的合併請求不會收到掃描
憑證。執行含有機密的作業前，請先審查 `.gitlab-ci.yml` 的每項變更。
將變數設為遮罩及隱藏，並不會讓不受信任的 CI 程式碼
變得安全。

## 執行掃描並審查檢出項目

建立符合資格且受保護的合併請求，或在受保護的預設分支上執行管線。
執行付費的全程式碼庫掃描前，
請先從小範圍的差異開始。

開啟 `codex-security` 作業，並確認其產物包含：

- `scan-manifest.json`
- `findings.json`
- `coverage.json`
- `results.sarif`
- `scan-exit-code.txt`

接著開啟管線的 **安全性** 分頁，檢查匯入警告，並確認
檢出項目的識別碼、嚴重性等級與原始碼位置。預設分支掃描
也會建立專案弱點紀錄。合併請求的檢出項目會顯示在
管線的安全性分頁或合併請求的安全性小工具中，但不會建立
全專案範圍的弱點紀錄。

請限制產物的存取權限，因為掃描結果可能包含有弱點的原始碼片段、
證據與修復細節。

## 選擇掃描設定檔

管線會根據觸發事件選擇設定檔：

| 觸發事件                                        | 目標          | 模式       | 投入程度  |
| ---------------------------------------------- | --------------- | ---------- | ------- |
| 同一專案內受保護的合併請求           | 已提交的差異  | `standard` | `low`   |
| 受保護預設分支的推送或手動觸發（需主動啟用） | 整個程式碼庫 | `standard` | `high`  |
| 受保護預設分支上的排程觸發（需主動啟用）    | 整個程式碼庫 | `deep`     | `xhigh` |

合併請求掃描會針對已提交的變更提供回饋。
預設分支掃描會審查整合後的程式碼庫。排程深度掃描會定期提供更廣的涵蓋範圍。
完成的差異掃描僅適用於該次變更，
並不代表整個程式碼庫都沒有問題。

工作流程會將 CLI 安裝在程式碼庫之外，並以絕對路徑執行。
其模擬執行預檢會使用僅供該處理程序使用的 API 金鑰，
但不會啟動付費掃描，也不會檢查 API 身分驗證、Codex Security 存取權、配額或模型
可用性。

工作流程會將掃描狀態與結果寫入工作樹以外的位置，並將
`OPENAI_API_KEY` 的使用範圍限制在掃描處理程序內。CLI 只會收到一組精簡且明確指定的
環境變數，而不會繼承所有 GitLab 變數。執行差異掃描時，
工作流程會計算合併基底，並將掃描綁定至已審查的基底與
頂端修訂版本。

範例將 `@openai/codex-security` 固定在 `0.1.20` 版本。變更固定版本前，請重新測試身分驗證、
產物、SARIF 匯入與政策關卡。

## 將結果回報與政策強制執行分開

GitLab 會從成功完成的報告作業匯入 SARIF。管線會先發布
報告，再於獨立的
`codex-security-gate` 作業中還原掃描器的結束狀態。

報告作業會接受結束代碼為 `0` 或 `1` 時的檢出項目。對於結束
代碼 `2`，只有在掃描資訊清單證明掃描已完成、涵蓋範圍
明確標示為 `partial`，且存在內容非空的 SARIF 報告時才會接受。其他執行階段、
組態或匯出失敗仍會阻擋流程。

最後的關卡會保留以下掃描器結束代碼：

| 結束代碼 | 意義                                                                     |
| ---- | --------------------------------------------------------------------------- |
| `0`  | 掃描已完成，涵蓋範圍完整，且通過政策檢查。            |
| `1`  | 掃描已完成，並發現達到或超過設定門檻的問題。 |
| `2`  | 掃描涵蓋範圍不完整，或發生輸入或執行階段錯誤。              |

在您針對涵蓋範圍不完整的情況進行調整時，此範例暫時允許結束代碼 `2`。
若涵蓋範圍不完整時必須阻擋管線，請移除此允許設定。

修復與發布會在最終政策關卡前執行。即使關卡稍後判定管線失敗，符合條件的問題仍可產生經過驗證的草稿合併請求。

## 啟用經過驗證的修復

自動修復是選用功能，僅會在受保護的預設分支管線中執行。Codex 修復程序及由程式碼庫控制的驗證指令，不會收到 GitLab 專案存取 Token 或執行器注入的憑證。

此安全性契約包含三部分：由程式碼庫控制的指令絕不會收到 OpenAI 或 GitLab 憑證；只有發布作業會取得程式碼庫寫入權限；所有產生的變更都會維持草稿狀態，直到有人審查並合併為止。

此工作流程會：

1. 要求掃描涵蓋範圍完整，且發現嚴重性為 `high` 或 `critical` 的
   問題。
2. 確認設定的迴歸測試在套用修補內容前會失敗。
3. 產生針對問題的修補內容，並拒絕變更 CI 檔案、憑證檔案、二進位檔或其他受保護檔案。
4. 執行迴歸測試時，不提供 OpenAI、GitLab、登錄庫、部署或作業 Token 憑證。
5. 使用 `verify-fix` 傳回 `fixed`、`still_vulnerable` 或 `inconclusive`。
   只有在 `verify-fix` 傳回 `fixed`，且
   驗證程序未變更修補內容時，作業才會發布修補內容。

設定下列受保護變數以啟用修復功能：

- 將 `CODEX_SECURITY_ENABLE_REMEDIATION` 設為 `true`。
- 將 `CODEX_SECURITY_VERIFICATION_COMMAND` 設為現有的迴歸測試，
  該測試須在修復前傳回結束代碼 `1`，修復後傳回 `0`。
- 您也可以將 `CODEX_SECURITY_SETUP_COMMAND` 設為非互動式的相依套件
  設定指令。

選擇能驗證核心安全性不變條件的迴歸測試，而非針對特定實作的測試。對產生的測試與原始碼變更，都應同樣嚴格審查。

<details>
  <summary>進階：隔離程式碼庫指令</summary>

`validate`、`patch` 和 `verify-fix` 指令會收到僅限各自程序使用的
`CODEX_API_KEY`。由程式碼庫控制的設定與測試指令，會以
另一個無特權使用者的身分，在已追蹤原始碼檔案的可寫入副本中執行。
此副本刻意排除 Git 中繼資料、子模組內容，以及
已下載的產物。需要 `.git` 或
子模組的設定與測試指令，必須在另外設計、不含憑證的作業中執行。

只有由 root 擁有的 Codex 步驟，才能存取標準簽出目錄或 GitLab 的
相鄰檔案變數目錄。此副本的乾淨環境僅包含
`PATH`、`HOME`、`LANG`、`CI` 和 `CI_PROJECT_DIR`。若指令需要其他
非機密值，請先審查指令，再將該值加入允許清單。若您的
執行器無法切換使用者，請先將驗證移至獨立且不含憑證的
作業，再啟用修復功能。

</details>

## 發布草稿合併請求

建立一個 [GitLab 專案存取
Token](https://docs.gitlab.com/user/project/settings/project_access_tokens/#create-a-project-access-token)，
並授予開發者角色及 `api` 和 `write_repository` 範圍。將其儲存為
受保護、已遮罩且隱藏的 `GITLAB_REMEDIATION_TOKEN`，並將作用範圍限制在
`codex-security/publish` 環境。

設定 `CODEX_SECURITY_CREATE_MR=true` 以啟用發布功能。另將非機密變數
`CODEX_SECURITY_MR_TEST_COMMAND` 設為專案專用的安全性迴歸測試，
每個產生的修復分支都必須通過此測試。請讓此變數維持
未受保護狀態，讓產生的未受保護合併請求能讀取該指令。
發布工作流程會：

- 收到具有程式碼庫寫入權限的 Token，但不會收到 OpenAI 憑證。
- 建立 `codex-security/fix-<finding-hash>` 分支。
- 建立草稿合併請求；若已有開啟狀態的草稿，則會沿用，不會重複建立。
- 在只含已追蹤檔案的副本中，以無特權使用者身分執行未受保護修復分支的迴歸測試，且不提供受保護的憑證。
- 絕不自動合併產生的變更。

請勿以 `CI_JOB_TOKEN` 取代專案存取 Token，因為它無法執行
所需的合併請求建立作業。合併前，請審查提出的修補內容、
驗證證據及發現的問題。

## 設定選用變數

只需設定您所啟用功能需要的變數：

| 變數                                  | 需要時機                       | 預設值或用途                                          |
| ----------------------------------------- | --------------------------------- | ----------------------------------------------------------- |
| `CODEX_SECURITY_API_KEY`                  | 每次掃描                        | 受保護、已遮罩且隱藏；作用範圍限於 `codex-security/openai` |
| `CODEX_SECURITY_VERSION`                  | CLI 升級                       | 已釘選至 `0.1.20`；變更前請重新測試                  |
| `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` | 預設分支的完整掃描         | 須明確選擇啟用；預設關閉                             |
| `CODEX_SECURITY_SCHEDULED_DEEP_SCAN`      | 已排程的深度掃描              | 須明確選擇啟用；預設關閉                             |
| `CODEX_SECURITY_DEEP_MAX_TIME_HOURS`      | 已排程的深度掃描              | 必須設定時間預算，且須大於 `0` 並小於 `8`     |
| `CODEX_SECURITY_DEEP_MAX_COST`            | 已排程的深度掃描              | 必須設定預估成本防護門檻（美元），且須大於 `0`      |
| `CODEX_SECURITY_ENABLE_REMEDIATION`       | 產生修補內容                  | 須透過受保護變數選擇啟用；預設關閉                            |
| `CODEX_SECURITY_VERIFICATION_COMMAND`     | 產生修補內容                  | 受保護的迴歸測試                                   |
| `CODEX_SECURITY_SETUP_COMMAND`            | 選用的修復設定        | 受保護的相依套件安裝                           |
| `CODEX_SECURITY_REMEDIATION_EFFORT`       | 選用的修復調整       | `high`                                                      |
| `CODEX_SECURITY_MAX_CHANGED_FILES`        | 選用的修補內容大小限制         | `8`；允許範圍為 `1` 至 `20`                         |
| `CODEX_SECURITY_CREATE_MR`                | 建立草稿合併請求      | 須透過受保護變數選擇啟用；預設關閉                            |
| `GITLAB_REMEDIATION_TOKEN`                | 建立草稿合併請求      | 具開發者角色的專案 Token，作用範圍限於 `codex-security/publish`  |
| `CODEX_SECURITY_GITLAB_INTERNAL_URL`      | 選用的自架環境發布   | 執行器可連線的 GitLab 來源位址                     |
| `CODEX_SECURITY_MR_TEST_COMMAND`          | 發布合併請求草稿    | 必要的專案專用迴歸測試，不含機密資訊       |
| `CODEX_SECURITY_MR_SETUP_COMMAND`         | 選用的修復分支設定 | 不含機密資訊的相依套件設定                                 |

GitLab 提供 `CI_*` 變數。管線負責管理
`CODEX_SECURITY_BIN`、`CODEX_SECURITY_EFFORT`、`CODEX_SECURITY_MODE`、
`CODEX_SECURITY_STATE_DIR` 和 `CODEX_SECURITY_TARGET`；請勿將這些變數
設為專案變數。進行差異掃描時，CLI 會根據正規化後的基底與頂端修訂版本，
推導出標準目標識別資訊。

## 調整政策執行方式與成本

針對合併請求使用聚焦於變更的差異掃描來提供回饋，針對預設分支使用標準程式碼庫掃描，
並以排程深度掃描擴大涵蓋範圍。這兩種掃描整個程式碼庫的
設定檔預設皆停用。排程深度掃描還需要設定
`CODEX_SECURITY_DEEP_MAX_TIME_HOURS` 和 `CODEX_SECURITY_DEEP_MAX_COST`；
CLI 的時間預算必須低於作業的八小時逾時限制。請先量測具代表性的執行結果，
再設定預算。請將 `--max-cost` 視為預估成本的控管機制，而非
不可超過的計費上限。

請先從僅產生報告的掃描開始。待團隊
審查過具代表性的掃描結果、涵蓋範圍、成本與執行時間後，再加入 `--fail-on-severity`。請參閱[在 CI 中
執行 Codex Security](/zh-Hant/codex/security/cli/ci)，瞭解嚴重程度政策與結束代碼的
詳細資訊。

作業失敗時：

- 缺少掃描產物表示組態或執行器有問題。
- 若已有產物但涵蓋範圍不完整，請審查 `coverage.json`。
- 若 GitLab 未顯示掃描結果，請檢查 SARIF 報告作業是否成功，
以及 GitLab 是否已接受報告。
- 若修復作業被略過，請檢查受保護分支、掃描涵蓋範圍是否完整、
發現問題的嚴重程度、驗證指令，以及用於明確啟用功能的變數。
- 若發布時發生錯誤，請檢查專案 Token 的角色、權限範圍，
以及環境限制。

如需各項指令、旗標與產物的資訊，請參閱 [Codex Security CLI
參考資料](/zh-Hant/codex/security/cli/reference)。
