<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/cli/reference -->

使用本參考資料查看支援的 `codex-security` 指令、旗標、
輸出格式與結束行為。若要依指引進行首次掃描，請從
[CLI 快速入門](/zh-Hant/codex/security/cli)開始。

  `@openai/codex-security` 套件已公開。
  執行掃描需要 Codex Security 存取權。掃描會使用您的本機權限，且不會暫停
  等待核准。開始前，請先詳閱[本機掃描
  權限](#local-scan-permissions)。

請使用 `npx @openai/codex-security` 執行 CLI。

## 指令概覽

```text
usage: codex-security [--version] <command> [options]

CLI 提供以下指令：

| 指令                       | 用途                                               |
| ----------------------------- | ----------------------------------------------------- |
| `codex-security scan`         | 執行 Codex Security 掃描。                            |
| `codex-security install-hook` | 安裝 Git 提交前安全性掃描。               |
| `codex-security bulk-scan`    | 探索程式碼庫並執行可續行的大量掃描。   |
| `codex-security scans`        | 列出、檢查、比較及擷取已儲存的掃描記錄。 |
| `codex-security findings`     | 審查並更新已儲存的安全性發現項目。            |
| `codex-security export`       | 將已完成的發現項目匯出為 CSV、JSON 或 SARIF。     |
| `codex-security publish`      | 將已完成掃描的發現項目發布至 Linear。            |
| `codex-security validate`     | 檢查一或多個待確認的安全性發現項目。        |
| `codex-security patch`        | 修補一或多個安全性問題。                    |
| `codex-security login`        | 登入、儲存憑證，或查看登入狀態。  |
| `codex-security logout`       | 移除已儲存的登入資訊。                            |
| `codex-security info`         | 顯示 SDK 與隨附外掛程式的唯讀中繼資料。       |

CLI 也提供以下整合指令：

| 指令                      | 用途                               |
| ---------------------------- | ------------------------------------- |
| `codex-security completions` | 產生 Shell 自動完成指令碼。    |
| `codex-security mcp`         | 將 CLI 註冊為 MCP 伺服器。    |
| `codex-security skills`      | 將 Codex Security 技能同步至智慧體。 |

列出所有可用指令：

```bash
npx @openai/codex-security --help

在指令中加入 `--help`，以查看其引數和選項：

```bash
npx @openai/codex-security scan --help

`codex-security --version` 會顯示已安裝版本並結束。
`codex-security info --json` 會回報 SDK 和隨附外掛程式的版本。
這兩個指令都不需要 Python。

### 探索指令並連接智慧體

輸出智慧體可讀取的指令資訊清單：

```bash
npx @openai/codex-security --llms

以 JSON 格式查看掃描引數的結構描述：

```bash
npx @openai/codex-security scan --schema --format json

為 Bash 產生 Shell 自動完成指令碼：

```bash
npx @openai/codex-security completions bash

若使用其他 Shell，請將 `bash` 替換為 `zsh` 或 `fish`。

掃描結果支援 `--format toon|json|yaml|jsonl` 和 `--full-output`。這個
框架層級的 `--format` 不同於 `--export-format`，後者用於選擇
從已完成掃描匯出的成品格式。全域指令說明中
也列出 `md`，但掃描結果不支援 Markdown 輸出。

將 CLI 註冊為 MCP 伺服器：

```bash
npx @openai/codex-security mcp add

將 Codex Security 技能同步至您的智慧體：

```bash
npx @openai/codex-security skills add

MCP 僅提供唯讀的 `info` 中繼資料指令。掃描、匯出、
身分驗證、驗證和修補仍僅能透過 CLI 執行。

## `codex-security scan`

對程式碼庫、所選路徑、已提交的變更或
工作樹執行掃描。

```text
usage: codex-security scan [-h] [--auth {auto,chatgpt,api-key}]
                           [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                           [--path PATH | --diff BASE | --working-tree]
                           [--head HEAD] [--base BASE]
                           [--knowledge-base PATH] [--scan-prompt-file FILE]
                           [--post-scan-prompt-file FILE]
                           [--mode {standard,deep}] [--workers N]
                           [--subagents N] [--stop-after-no-new N]
                           [--max-discovery-runs N] [--max-time-hours HOURS]
                           [--model MODEL]
                           [--effort {minimal,low,medium,high,xhigh,max}]
                           [--output-dir DIR]
                           [--archive-existing]
                           [--plugin-path PATH] [--python PATH]
                           [--codex KEY=VALUE] [--fail-on-severity LEVEL]
                           [--patch] [--patch-severity {critical,high,medium,low}]
                           [--create-pr]
                           [--max-cost USD] [--dry-run] [--headless] [--verbose]
                           [--json] [--format {toon,json,yaml,jsonl}]
                           [--full-output] [repository]

`repository` 預設為目前目錄。

### 選擇掃描的身分驗證方式

使用預設的 `--auth auto` 自動選取憑證。當同時有
ChatGPT 登入資訊，以及 `OPENAI_API_KEY` 或 `CODEX_API_KEY` 可用時，
採用文字輸出的互動式掃描會詢問要使用哪個憑證。CI 掃描、JSON 和
JSONL 掃描，以及其他沒有互動式終端的掃描，會使用
環境中的 API 金鑰。試執行不會顯示提示，也不會載入憑證。

若要使用已儲存的憑證，請傳入 `--auth chatgpt`：

```bash
npx @openai/codex-security scan . --auth chatgpt

若要使用環境中的 API 金鑰，請傳入 `--auth api-key`：

```bash
npx @openai/codex-security scan . --auth api-key

若要讓系統預設自動使用已儲存的憑證，請執行
`unset OPENAI_API_KEY CODEX_API_KEY`。

### 使用 OpenRouter 或 Fireworks

若要選取 OpenRouter，請提供其 API 金鑰並明確指定模型：

```bash

npx @openai/codex-security scan . \
  --provider openrouter \
  --model anthropic/claude-sonnet-4.5

若要選取 Fireworks，請提供其 API 金鑰並明確指定模型：

```bash

npx @openai/codex-security scan . \
  --provider fireworks \
  --model accounts/fireworks/models/qwen3-235b-a22b

這兩個提供者也都支援 `bulk-scan`。

### 使用 Amazon Bedrock

使用 `--provider amazon-bedrock` 選取 Amazon Bedrock，並透過
`--model` 明確指定 Bedrock 模型：

```bash
npx @openai/codex-security scan . \
  --provider amazon-bedrock \
  --model openai.gpt-5.6-sol

設定 `AWS_REGION`，並使用 `AWS_BEARER_TOKEN_BEDROCK`、標準 AWS
存取金鑰、AWS 設定檔、Web 身分識別、容器憑證或
預設 AWS 憑證鏈進行身分驗證。Bedrock 掃描會使用 AWS 憑證，而非
`--auth`、ChatGPT 登入資訊或 OpenAI API 金鑰。`scan` 和 `bulk-scan`
都支援 `--provider`。

### 選擇掃描目標

每次掃描請選擇一種目標類型。

| 引數                 | 說明                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| `--path PATH`            | 掃描相對於程式碼庫的路徑。若要指定其他路徑，請重複使用此旗標。         |
| `--diff BASE`            | 掃描從 `BASE` 到 `--head` 的已提交變更。目標修訂版本預設為 `HEAD`。    |
| `--head HEAD`            | 設定 `--diff` 的目標修訂版本。                                             |
| `--working-tree`         | 以 `--base` 為基準，掃描已暫存與未暫存的變更。基準修訂版本預設為 `HEAD`。 |
| `--base BASE`            | 設定 `--working-tree` 的基準修訂版本。                                     |
| `--mode {standard,deep}` | 選擇掃描模式。預設為 `standard`。                                |

`--path`、`--diff` 和 `--working-tree` 彼此互斥。`--head`
必須搭配 `--diff`，而 `--base` 必須搭配 `--working-tree`。深度模式支援
程式碼庫和路徑目標。

差異掃描與工作樹掃描的程式碼庫引數必須指向 Git 工作樹的根目錄。
選取的參照必須存在於該簽出版本中。

掃描整個程式碼庫：

```bash
npx @openai/codex-security scan .

掃描選取的路徑：

```bash
npx @openai/codex-security scan . --path src --path tests

掃描已提交的變更：

```bash
npx @openai/codex-security scan . --diff origin/main --head HEAD

掃描已暫存和未暫存的變更：

```bash
npx @openai/codex-security scan . --working-tree --base HEAD

對程式碼庫進行更深入的審查：

```bash
npx @openai/codex-security scan . --mode deep

### 設定深度掃描

搭配 `--mode deep` 使用下列選項，以控制工作程序的並行數和執行時間：

| 引數                 | 說明                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `--workers N`            | 同時執行的獨立標準掃描工作程序數量上限。預設值為 `4`。                |
| `--subagents N`          | 每個工作程序可使用的子代理程式數量。預設值為 `3`。                                   |
| `--stop-after-no-new N`  | 當連續完成的 `N` 次工作程序掃描均未發現新問題時停止。預設值為 `4`。 |
| `--max-discovery-runs N` | 獨立標準掃描的執行總次數上限。預設值為 `40`。                       |
| `--max-time-hours HOURS` | 工作程序執行時間上限，以小時為單位。預設值為 `96`；可使用小數。             |

`--subagents` 可接受零或正整數。`--max-time-hours` 可接受
不大於 `96` 的正數。其餘選項必須為
正整數。這些選項不適用於標準掃描。

例如，使用兩個工作程序，最多執行十次，並在 1.5 小時後
停止工作程序的執行：

```bash
npx @openai/codex-security scan . \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

時間上限到期時，掃描會停止尚未完成的工作程序，保留已完成的
掃描結果，並將結果彙整至最終報告。若沒有任何工作程序完成
原始碼審查，掃描會記錄部分涵蓋範圍，並傳回結束代碼 `2`。

在 `~/.codex/codex-security/config.toml` 中設定永久預設值；或在
`$CODEX_HOME/codex-security/config.toml` 中設定，前提是已設定 `CODEX_HOME`：

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

指令列選項會覆寫這些預設值。`scan --workers` 控制
單次深度掃描中的獨立標準掃描工作程序；`bulk-scan --workers`
控制同時進行的程式碼庫掃描。`stop_after_consecutive_errors` 只能
在 TOML 檔案中設定；預設值為 `3`。

### 新增安全性上下文

使用 `--knowledge-base PATH` 提供架構文件、威脅模型
或安全性政策。若要加入更多檔案或目錄，請重複使用此選項：

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

支援的文件包括 `.md`、`.markdown`、`.txt`、`.pdf` 和 `.docx`
檔案。CLI 會遞迴搜尋目錄，拒絕符號連結形式的輸入路徑，
略過符號連結的目錄項目，並將擷取的文件內容
排除在已儲存的掃描結果之外。

### 新增掃描指示

若要新增掃描指示，請使用
`--scan-prompt-file` 提供文字或 Markdown 檔案。使用 `--post-scan-prompt-file`，即可
在掃描成功、掃描涵蓋範圍不完整或掃描發生錯誤後，
於同一個已通過身分驗證的工作階段中執行後續指示：

```bash
npx @openai/codex-security scan . \
  --scan-prompt-file security-focus.md \
  --post-scan-prompt-file follow-up.md

例如，使用掃描提示詞聚焦於授權邊界，並要求後續指示
在掃描目錄中寫入新的 `post-scan-summary.md`。
如果後續指示執行失敗，CLI 會回報警告並保留已完成的掃描。
若掃描遭取消，或掃描達到成本
上限，則不會執行後續指示。

### 設定輸出與政策選項

使用這些選項可保留產出物、保存先前的結果，或建立
機器可讀的結果。

| 引數                   | 說明                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `--output-dir DIR`         | 將掃描產出物寫入外層 Git 工作樹之外的私有目錄。預設會保存至 Codex Security 的永久狀態儲存空間。 |
| `--archive-existing`       | 將現有結果移至 `DIR.previous-<timestamp>-<id>`，並從空白的輸出目錄開始。需要 `--output-dir`。  |
| `--fail-on-severity LEVEL` | 當已完成的掃描回報發現項目的嚴重性達到指定門檻或更高時，傳回結束代碼 `1`。門檻可為 `critical`、`high`、`medium` 或 `low`。                  |
| `--patch`                  | 在完整掃描後修正並驗證選取的發現項目。                                                                      |
| `--patch-severity LEVEL`   | 修補嚴重性達到或高於 `critical`、`high`、`medium` 或 `low` 的發現項目。預設值為 `low`。                                        |
| `--create-pr`              | 提交已驗證的修補檔案，並建立 GitHub Pull Request。需要 `--patch`。                                              |
| `--max-cost USD`           | 當預估的模型成本超過指定的美元金額時停止掃描。                                                  |
| `--dry-run`                | 在不啟動掃描的情況下，檢查程式碼庫、目標、知識庫、輸出目錄和 Codex 組態。             |
| `--headless`               | 顯示純文字進度，而非互動式掃描儀表板。                                                          |
| `--verbose`                | 將經過遮蔽的生命週期、身分驗證、進度與成本診斷資訊列印至 stderr。                                          |
| `--json`                   | 將資訊清單、發現項目、涵蓋範圍、路徑與回合中繼資料列印為單一 JSON 文件。                                           |
| `--format FORMAT`          | 以 `toon`、`json`、`yaml` 或 `jsonl` 格式列印完整掃描結果。                                                        |
| `--full-output`            | 使用預設的結構化輸出格式列印完整結果。                                                        |

成本限制為估算值，並非硬性支出上限。已在
處理中的請求，完成時可能略微超出限制。若深度掃描在 Codex Security 彙整
已完成的工作程序結果後達到限制，CLI 會封存
可用結果，將涵蓋範圍標記為 `partial`，並傳回結束代碼 `2`。
否則，會傳回 `2`，並將任何可用的部分輸出保留在磁碟上。

若省略 `--output-dir`，結果會持續儲存在
`$CODEX_HOME/state/plugins/codex-security/scans/<repository>`。`CODEX_HOME`
的預設值為 `~/.codex`。設定 `CODEX_SECURITY_STATE_DIR`，即可改將結果保留在
`$CODEX_SECURITY_STATE_DIR/scans/<repository>`。這些目錄可能
包含原始碼摘錄和漏洞詳細資料，因此請妥善管理其權限
與保留方式。

工作台會將掃描記錄保存在
`$CODEX_HOME/state/plugins/codex-security/workbench.sqlite3`。設定
`CODEX_SECURITY_STATE_DIR` 也會移動工作台資料庫的位置。

輸出目錄必須位於掃描目錄及包含該目錄的任何
Git 工作樹之外。掃描可使用
`--archive-existing` 取代現有的結果目錄。

若要在重複使用輸出目錄前保存先前的結果：

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --archive-existing

掃描預設只產生報告。加入 `--fail-on-severity`，即可在 CI 中評估
嚴重性政策：

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --json \
  --fail-on-severity high \
  > /path/outside/repository/codex-security.json

試執行會檢查本機輸入，包括知識庫文件，但不會
載入憑證、啟動 Codex，也不會探查外掛程式的 Python
直譯器：

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --dry-run

### 設定執行階段

需要明確指定模型、直譯器、外掛程式或
Codex 組態值時，請使用執行階段選項。

| 引數                                                  | 說明                                                                                              |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `--auth {auto,chatgpt,api-key}`                           | 選取掃描憑證。預設值為 `auto`。                                                      |
| `--provider {openai,openrouter,fireworks,amazon-bedrock}` | 選取推論提供者。預設值為 `openai`。                                                  |
| `--model MODEL`                                           | 選取模型。預設值為 `gpt-5.6-sol`。使用 OpenRouter、Fireworks 或 Amazon Bedrock 時必須指定。  |
| `--effort {minimal,low,medium,high,xhigh,max}`            | 選取模型的推理強度。預設值為 `xhigh`。                                             |
| `--plugin-path PATH`                                      | 使用 Codex Security 外掛程式目錄或 ZIP 檔案，覆寫隨附的外掛程式。                             |
| `--python PATH`                                           | 選取外掛程式執行階段使用的 Python 直譯器。                                                    |
| `--codex KEY=VALUE`                                       | 覆寫隔離的 Codex 組態值。值使用 TOML 語法。若要指定更多值，請重複使用此旗標。 |

若不想編寫 TOML，可用以下方式選取不同的模型與推理強度：

```bash
npx @openai/codex-security scan . --model gpt-5.6-terra --effort high

將透過 `--codex` 傳入的字串值加上引號，讓 TOML 剖析器接收到
字串：

```bash
npx @openai/codex-security scan . --codex 'model="gpt-5.6-terra"'

## `codex-security install-hook`

為目前的程式碼庫安裝 Git pre-commit 安全性檢查：

```bash
npx @openai/codex-security install-hook

此檢查會在每次提交前掃描已暫存與未暫存的變更，並在出現
高嚴重性發現項目或掃描錯誤時阻止提交。它會遵循 `core.hooksPath`，且
不會取代現有的 pre-commit 指令碼。必要時，可設定不同的嚴重性
門檻：

```bash
npx @openai/codex-security install-hook . --fail-on-severity medium

## `codex-security bulk-scan`

探索並掃描 GitHub 程式碼庫，或根據程式碼庫 CSV 執行
可中斷後繼續的掃描：

如需 GitHub 探索、CSV 清單、掃描活動結果
和容器化掃描的完整指南，請參閱[執行批次安全性
掃描](/zh-Hant/codex/security/cli/bulk-scans)。

```text
usage: codex-security bulk-scan [input] [--output-dir DIR]
                                [--workers N] [--mode {standard,deep}]
                                [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                                [--model MODEL]
                                [--effort {minimal,low,medium,high,xhigh,max}]
                                [--knowledge-base PATH]
                                [--scan-prompt-file FILE]
                                [--post-scan-prompt-file FILE]
                                [--max-attempts N] [--plugin-path PATH]
                                [--python PATH] [--codex KEY=VALUE]

不加任何引數執行 `npx @openai/codex-security bulk-scan`，即可透過互動方式選擇
程式碼庫。此流程須先登入 GitHub CLI。

若要在互動式探索時選擇模型與推理強度：

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

若已備妥程式碼庫清單，請提供 CSV 檔案和 `--output-dir`：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

CSV 必須包含 `id`、`repository` 和 `revision` 欄位。修訂版本必須是
完整的提交雜湊值。選填的 `scope`、`mode` 和 `prompt` 欄位可用來設定
個別程式碼庫：

```csv
id,repository,revision,scope,mode,prompt
service,https://github.com/example/service.git,0123456789abcdef0123456789abcdef01234567,src,standard,Review authorization boundaries.

使用 `--knowledge-base PATH`，即可在所有
程式碼庫之間共用安全性文件。使用 `--scan-prompt-file FILE` 新增共用掃描指示；
CSV 的 `prompt` 欄位則會在共用提示詞之後，新增程式碼庫
專屬的指示。`--post-scan-prompt-file FILE` 會在每次
掃描後執行後續指示，包括涵蓋範圍不完整或發生錯誤的掃描。
但若掃描遭取消或達到成本上限，則不會執行後續指示。

`--workers` 限制同時掃描的程式碼庫數量，預設為 `4`。`--mode`
預設為 `standard`，而 `--max-attempts` 預設為 `1`。設定
`--max-attempts`，即可在程式碼庫或掃描發生錯誤時重試。已完成但
涵蓋範圍不完整的掃描不會重試；其結果仍可使用，而
指令會傳回結束代碼 `2`。

再次執行相同指令，即可從現有的輸出目錄繼續。
CLI 會略過已完成的掃描，包括涵蓋範圍不完整的掃描。

如需容器化掃描活動的相關資訊，請參閱[在 Docker 中執行
批次掃描](/zh-Hant/codex/security/cli/bulk-scans#run-bulk-scans-in-docker)。

## `codex-security scans`

### 尋找已儲存的掃描

列出目前目錄中已儲存的掃描：

```bash
npx @openai/codex-security scans

列出其他程式碼庫的掃描：

```bash
npx @openai/codex-security scans list /path/to/repository

尋找儲存於特定輸出目錄下的掃描：

```bash
npx @openai/codex-security scans list --scan-root /path/outside/repository/results

### 檢查或重新執行掃描

顯示已儲存掃描的結果與組態：

```bash
npx @openai/codex-security scans show SCAN_ID

加入 `--show-linked-findings`，即可納入先前掃描的發現項目連結。

使用原始組態，針對目前的簽出內容重新執行掃描：

```bash
npx @openai/codex-security scans rerun SCAN_ID

重新執行時，必須使用原始掃描記錄的外掛程式版本。若
已安裝的版本不同，指令會停止，而不會使用其他版本的
外掛程式執行。

### 檢查已儲存的掃描記錄

讀取掃描及其工作程序已儲存的完整工作階段事件。這些記錄
未經遮蔽處理，可能包含原始碼或憑證，因此請在分享前
先行審查：

```bash
npx @openai/codex-security scans logs SCAN_ID

加入 `--json`，即可取得包含完整資訊的機器可讀格式結果。

### 比對與比較發現項目

比較兩次掃描，找出新增、持續存在、重新開啟、已解決及狀態未知的
發現項目：

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

比較作業會自動比對根本原因相同的發現項目，
並重複使用已儲存的比對結果。若要明確儲存比對結果，請使用 `scans match`：

```bash
npx @openai/codex-security scans match PREVIOUS_SCAN_ID CURRENT_SCAN_ID

若後續掃描的涵蓋範圍不完整，或未
涵蓋發現項目的原始位置，該項目即會被標示為未知。將 `--force` 加入 `match`，即可在需要時
重新計算現有的比對結果。

若要比對目前程式碼庫的所有已完成掃描，包括來自
其他簽出內容的掃描：

```bash
npx @openai/codex-security scans match --all

即使使用相同組態重新執行，掃描結果仍可能不同。比對與
比較只能追蹤變更，無法讓結果具有確定性，也無法證明
漏洞已不存在。請使用 `validate`，針對目前程式碼重新檢查攸關安全性的
發現項目。

## `codex-security findings`

列出目前程式碼庫各次掃描中尚未結案的發現項目：

```bash
npx @openai/codex-security findings list

傳入程式碼庫路徑，以檢查其他簽出內容：

```bash
npx @openai/codex-security findings list /path/to/repository

加入 `--json`，即可取得結構化輸出。清單會標示最新掃描中
出現的發現項目，以及未在該次掃描中獲得確認的先前發現項目。

請注意，先前的發現項目在解決或駁回前，都會維持未結案狀態
（未出現在最新掃描中，並不能證明問題已修正）。

將已審查的發現項目記錄為誤報：

```text
usage: codex-security findings false-positive OCCURRENCE_ID
                       --reason REASON

檢查已儲存的掃描，以找出發現項目的出現記錄：

```bash
npx @openai/codex-security scans show SCAN_ID

記錄該誤報的具體說明：

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

原因不得為空。Codex Security 會為該程式碼庫儲存這項判定，
並將其作為上下文提供給後續掃描。每次掃描都會獨立重新檢查
目前的原始碼、控制措施與可達性。先前的判定
不會排除任何規則、路徑或漏洞類別。

## `codex-security export`

從已完成且已封存的掃描匯出 CSV、JSON 或 SARIF。匯出作業會先驗證
掃描成品，再寫入輸出，且不會變動 Codex 執行階段
或憑證。

```text
usage: codex-security export [--export-format {csv,json,sarif}]
                             [--output FILE|-] [--source-root PATH]
                             [--python PATH] scan_dir

`scan_dir` 是已完成的掃描目錄。

| 引數                           | 說明                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| `--export-format {csv,json,sarif}` | 選取匯出格式。預設為 `sarif`。                                           |
| `--output FILE\|-`                 | 將所選格式寫入檔案或 stdout。預設會寫入目前目錄中的檔案。 |
| `--source-root PATH`               | 使用程式碼庫簽出內容，將原始碼行指紋新增至 SARIF。                          |
| `--python PATH`                    | 選取隨附匯出器使用的 Python 解譯器。                                     |

`--source-root` 只能搭配 `--export-format sarif` 使用。JSON 會保留
已封存的發現項目文件。CSV 包含可攜式的發現項目欄位，
且不包含本機工作台的分流狀態。

若未指定 `--output`，CLI 會在目前工作目錄中將 SARIF 寫入 `results.sarif`、JSON 寫入
`findings.json`，並將 CSV 寫入 `findings.csv`。
匯出內容可能包含原始碼摘錄和漏洞詳細資料。請在程式碼庫
外執行此指令，或傳入 `--output`，並指定受掃描的
簽出內容以外的私有路徑。

將 SARIF 寫入檔案：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root /path/to/repository \
  --output /path/outside/repository/exports/results.sarif

將 SARIF 寫入 stdout：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root . \
  --output -

將發現項目匯出為 JSON：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format json \
  --output /path/outside/repository/exports/findings.json

將發現項目匯出為 CSV：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format csv \
  --output /path/outside/repository/exports/findings.csv

## `codex-security publish scan`

將已完成掃描中的每個發現項目發布至 Linear：

```text
usage: codex-security publish scan [SCAN_DIR] --to linear
                                   [--linear-team TEAM_ID]
                                   [--project PROJECT_ID]
                                   [--linear-api-key KEY]
                                   [--linear-assignee EMAIL_OR_USER_ID]
                                   [--dry-run] [--json]

`SCAN_DIR` 必須包含已完成且已封存的掃描。在互動式
終端中，可省略此引數，以從本機掃描歷史記錄選取已完成的掃描。建立議題
時，也要求該次掃描及其發現項目存在於本機掃描歷史記錄中。模擬
執行會驗證已封存的成品，但不執行這項持久化檢查。

| 引數                             | 說明                                                                                                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--to linear`                        | 發布至 Linear。必須提供此引數。                                                                                                                    |
| `--linear-team TEAM_ID`              | 選取 Linear 團隊。省略時會使用 `CODEX_SECURITY_LINEAR_TEAM`；兩者至少必須設定其中一項。                                                                 |
| `--project PROJECT_ID`               | 選取 Linear 專案。省略時會使用 `CODEX_SECURITY_LINEAR_PROJECT`。如果兩者都未設定，則會直接在團隊中建立議題。                          |
| `--linear-api-key KEY`               | 使用 Linear 個人 API 金鑰直接發布。省略時會使用 `CODEX_SECURITY_LINEAR_API_KEY`。                                                         |
| `--linear-assignee EMAIL_OR_USER_ID` | 透過電子郵件地址或 Linear 使用者 ID 指派已建立的議題。必須提供 `--linear-api-key` 或 `CODEX_SECURITY_LINEAR_API_KEY`。省略時，議題會維持未指派狀態。 |
| `--dry-run`                          | 準備議題資料，但不啟動 Codex、不連線至 Linear、不建立議題，也不寫入發布狀態。                                                 |
| `--json`                             | 將結構化發布結果寫入 stdout。進度資訊仍會輸出至 stderr。                                                                                      |

  Linear 議題說明與模擬執行的輸出可能包含原始碼片段
和漏洞詳細資料。請僅發布至經授權的 Linear 團隊或
專案，並將已儲存的輸出視為敏感資料。

每次實際執行發布時，都會嘗試為每個發現項目建立新議題。
再次發布相同的掃描時，不會比對、更新或重複使用現有議題。
如果部分發現項目發布失敗，指令會保留成功建立的議題，並
傳回結束代碼 `2`。
使用 `--json` 時，請在重試前審查 `created` 和 `failed` 結果，
以免重複建立議題。

發布前預覽議題酬載：

```bash
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --dry-run \
  --json

### 透過已連接的 Linear 應用程式發布

未提供 Linear API 金鑰時，指令會使用您現有的
組態與已連接的 Linear 應用程式啟動 Codex。發布前，請先登入並將 Linear
連接至您的 Codex 帳戶：

```bash
npx @openai/codex-security login
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --project PROJECT_ID

### 使用 Linear API 金鑰發布

提供 `--linear-api-key` 或 `CODEX_SECURITY_LINEAR_API_KEY` 後，系統會
直接透過 Linear API 發布，不會啟動 Codex。直接發布時，
除非您指定負責人，否則議題會維持未指派狀態：

```bash

npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --linear-assignee teammate@example.com

指令列值會覆寫對應的環境變數。對於 API
金鑰，建議優先使用 `CODEX_SECURITY_LINEAR_API_KEY`，而非 `--linear-api-key`，因為
指令列引數可能出現在 shell 歷史記錄和程序清單中。

## `codex-security validate` 與 `codex-security patch`

檢查候選發現項目是否有效：

```bash
npx @openai/codex-security validate findings.json \
  "Possible SQL injection in src/query.ts:42"

使用隨附的修復技能產生修正內容：

```bash
npx @openai/codex-security patch findings.json \
  "Missing authorization check in src/routes.ts:18"

每個位置引數都接受文字內容或檔案路徑，且皆以
目前目錄為基準。修正完成後，或後續掃描不再回報某個發現項目時，請使用 `validate`
重新檢查該項目。只比較掃描結果，並不能證明修正
確實有效。

使用 `--effort` 為任一指令選取推理強度：

```bash
npx @openai/codex-security validate "Possible SQL injection" --effort high

### 掃描後修正發現的問題

使用 `scan --patch` 在完整掃描結束後修正發現的問題。這需要
`@openai/codex-security` 0.1.15 或更新版本。預設的嚴重性門檻為
`low`。下列指令會選取嚴重性屬於「高」或「嚴重」的發現項目：

```bash
npx @openai/codex-security scan . --patch --patch-severity high --json

已驗證的發現項目，以及已修正的發現項目，都不會觸發 `--fail-on-severity`。

### 修正已儲存的發現項目

傳入發現項目 ID 或出現紀錄 ID，以修補其原始程式碼庫；也可以從已儲存的掃描中
選取發現項目：

```bash
npx @openai/codex-security patch OCCURRENCE_ID
npx @openai/codex-security patch --scan SCAN_ID --severity high --json
npx @openai/codex-security patch --scan latest --severity medium

`--scan latest` 會選取目前程式碼庫最近一次完成的掃描。
處理已儲存發現項目的指令支援 `--json`；文字內容和檔案輸入則不支援。

加入 `--create-pr`，即可只提交已驗證的修補檔案，並使用
GitHub CLI 建立 Pull Request：

```bash
npx @openai/codex-security patch --scan SCAN_ID --severity high --create-pr

如果推送或建立 Pull Request 失敗，請在同一個程式碼庫中執行顯示的 `patch --resume-pr BRANCH`
指令以重試。

### 修正 Linear 議題

若要使用個人 API 金鑰，請設定 `CODEX_SECURITY_LINEAR_API_KEY` 或 `LINEAR_API_KEY`；
若要使用 OAuth Token，則請設定 `LINEAR_ACCESS_TOKEN`。建議優先使用環境變數，
而非 `--linear-api-key KEY`，以免金鑰留在 shell 歷史記錄中。

透過 ID 或 URL 匯入議題。重複使用 `--linear-issue`，即可選取多個
議題：

```bash
npx @openai/codex-security patch --linear-issue SEC-123 --linear-issue SEC-124

使用 `--linear-project` 選取專案中尚未結案的議題。加入 `--linear-filter`
以縮小選取範圍：

```bash
npx @openai/codex-security patch --linear-project "Security backlog" \
  --linear-filter '{"labels":{"name":{"eq":"security"}}}'

除非篩選條件設定了 `state`，否則 CLI 會排除已完成與已取消的議題。
CLI 不會修改 Linear 議題。

## `codex-security login`、`logout` 與 `info`

以互動方式登入：

```bash
npx @openai/codex-security login

在遠端或無圖形介面的機器上使用裝置身分驗證：

```bash
npx @openai/codex-security login --device-auth

檢查目前的登入狀態：

```bash
npx @openai/codex-security login status

移除已儲存的登入資訊：

```bash
npx @openai/codex-security logout

透過 stdin 傳入 API 金鑰並儲存：

```bash
printenv OPENAI_API_KEY | npx @openai/codex-security login --with-api-key

儲存企業存取 Token：

```bash
printenv CODEX_ACCESS_TOKEN | npx @openai/codex-security login --with-access-token

檢視 SDK 和隨附外掛程式的唯讀中繼資料：

```bash
npx @openai/codex-security info --json

將 CLI 作為 MCP 伺服器提供時，`info` 是唯一可用的指令。
掃描、匯出、發布、登入、驗證與修補仍只能透過 CLI 執行。

## 讀取掃描輸出

依預設，掃描會將進度、完成摘要與錯誤傳送至 stderr，
而不會將完整掃描結果寫入 stdout。指定 `--json`、
`--format` 或 `--full-output`，即可將結構化掃描結果傳送至 stdout。

互動式終端會顯示即時儀表板，列出目前的掃描階段、
已審查檔案、活動、Token 用量與預估費用。CI 和重新導向的
輸出會以純文字顯示進度。加入 `--headless`，即可在
互動式終端中以純文字顯示進度：

```bash
npx @openai/codex-security scan . --headless

儀表板也會顯示即時工作階段詳細資訊。這些資訊未經遮蔽，可能包含
原始程式碼或憑證。分享前請先審查。

### 詳細診斷資訊

加入 `--verbose`，即可將已遮蔽敏感資訊的生命週期、身分驗證、進度及費用
診斷資訊輸出至 stderr：

```bash
npx @openai/codex-security scan . --verbose

設定 `CODEX_SECURITY_LOG_LEVEL=debug`，不必使用該
旗標，即可啟用相同的診斷資訊。`LOG_LEVEL=debug` 也會在
`CODEX_SECURITY_LOG_LEVEL` 未設定時啟用診斷資訊。

### 完成摘要

掃描完成後，會將程式碼庫中未結案發現項目的數量、嚴重性分布、
涵蓋範圍、經過時間、報告路徑與結果目錄寫入 stderr。若有相關資料，
也會列出 Token 用量與預估費用：

```text
  REPORT    /path/to/scan/report.md

  FINDINGS  4 (3 confirmed this scan; 1 previously found; 1 critical, 2 high, 1 informational)
  COVERAGE  complete
  ELAPSED   1s
  TOKENS    1,250 input, 200 cached, 30 output
  RESULTS   /path/to/scan

資訊性發現項目會計入摘要總數。嚴重性政策
只會評估本次掃描中嚴重性為 `critical`、`high`、`medium` 和 `low` 的發現項目，
不會評估程式碼庫總數中列出的先前發現項目。

### JSON 輸出

`scan --json` 會將一份完整的 JSON 文件寫入 stdout。其頂層結構
如下：

```text
manifest
repositoryFindings
findings
coverage
scanDir
threadId
reportPath
artifactsDir
sarifPath
cost
turn
  id
  status
  durationMs
  finalResponse
  usage

進行 [修補](#patch-findings-after-a-scan)時，JSON 輸出也會包含修補
結果，以及已建立的任何 Pull Request。

進度、完成摘要、封存通知與錯誤仍會輸出至 stderr。
即使嚴重性政策
傳回結束代碼 `1`，或因涵蓋不完整而傳回結束代碼 `2`，已完成的掃描仍會輸出完整的 JSON 結果。

  `codex-security scan --json` 會輸出一份 JSON 文件。`codex exec --json`
  會輸出 JSON Lines 事件串流。請使用與所執行
  指令相符的輸出格式。

## 掃描產物

掃描完成後，易讀報告與結構化產物會存放在一起：

```text
<scan-directory>/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

這些結構化檔案各有不同用途：

| 檔案                    | 內容                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `scan-manifest.json`    | 掃描識別資訊、狀態、目標、範圍、產生者，以及已封存的產物記錄。                                                    |
| `findings.json`         | 發現項目的識別碼、嚴重性、可信度、分類體系、位置、證據、驗證、資料流、可達性與修復方式。 |
| `coverage.json`         | 已審查的面向、排除項目、延後處理的工作、待釐清問題與涵蓋完整度。                                        |
| `report.md`             | 易讀的掃描報告。                                                                                                           |
| `artifacts/`            | 輔助性掃描產物。                                                                                                      |
| `exports/results.sarif` | 掃描期間產生的 SARIF（若有）。                                                                                  |

涵蓋完整度有三種值：

- `complete`：掃描記錄顯示，所選範圍已完整涵蓋。
- `partial`：掃描記錄了延後處理的工作或其他涵蓋限制。
- `unknown`：掃描將涵蓋完整度回報為未知。

請先審查延後處理的面向、明確排除的項目與待釐清問題，再將
涵蓋情形作為安全性決策的依據。

## 結束代碼與訊號

CLI 使用下列結束代碼：

| 結束代碼  | 條件                                                                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`   | 掃描已完成，涵蓋範圍完整且通過嚴重程度政策檢查；批次掃描或發布已完成，且未發生失敗；或其他指令執行成功。                  |
| `1`   | 已完成的掃描回報嚴重程度達到或超過設定層級的發現項目。                                                                                                       |
| `2`   | CLI 偵測到輸入、執行階段或匯出錯誤；掃描涵蓋範圍不完整；批次掃描中有程式碼庫發生錯誤；或發布作業中有一或多個發現項目發布失敗。 |
| `130` | Ctrl-C 中斷掃描或發布作業。                                                                                                                                     |
| `143` | SIGTERM 終止掃描或發布作業。                                                                                                                                     |

只要掃描涵蓋範圍為 `partial` 或 `unknown`，就會傳回 `2`，即使沒有
嚴重程度政策也一樣。要求結構化輸出時，已完成的掃描和
部分完成的發布作業仍會將可用結果寫入 stdout。CLI 會在作業中斷
或發生執行階段錯誤後，列印
部分輸出的位置。

## 本機掃描權限

CLI 和 SDK 掃描會以您的本機作業系統權限執行。每次掃描
都會使用 `codex_security_scan` 檔案系統設定檔，並將 `approvalPolicy` 設為
`"never"`。此設定檔允許讀取本機檔案系統，並寫入
工作區根目錄及所選的掃描狀態目錄。掃描不會暫停
以要求互動式核准。

透過 CLI `--codex` 或 SDK `codexOverrides` 提供的設定，包括
`approval_policy`、`sandbox_mode` 和檔案系統權限，無法取代
或限制這些掃描控制措施。主機和網路限制仍然適用。

掃描和工作台處理程序可能會繼承您的環境，包括不相關的
API Token 和雲端憑證。請只掃描您信任且有權評估的
程式碼庫，並且只提供掃描所需的憑證。

## 身分驗證與必要條件

設定 `OPENAI_API_KEY` 或 `CODEX_API_KEY`，使用
`npx @openai/codex-security login` 登入，或使用現有、儲存在檔案中的 Codex
登入資訊。如使用 OpenRouter 或 Fireworks，請設定供應商的 API 金鑰並選擇
模型。如使用 Amazon Bedrock，則改用 Bedrock API 金鑰或標準 AWS
憑證鏈。

如需了解如何選擇憑證，請參閱[選擇掃描
身分驗證方式](#select-scan-authentication)。

針對 CI，請將 API 金鑰的使用範圍限制於掃描步驟，並使用可信任的工作流程。

CLI 需要 Node.js 22（22.13.0 或更新版本）、24 或 26。掃描、批次掃描、
匯出、掃描記錄和已儲存的發現項目，也需要 Python 3.10 或更新版本。
Python 3.10 還需要 `tomli`。請將 `--python` 與 `scan`、`bulk-scan` 或
`export` 搭配使用；也可以為任何使用 Python 執行的指令設定 `PYTHON`。

請繼續參閱[CLI 快速入門](/zh-Hant/codex/security/cli)、[批次掃描
指南](/zh-Hant/codex/security/cli/bulk-scans)、[CLI 常見問題](/zh-Hant/codex/security/cli/faq)、[CI
指南](/zh-Hant/codex/security/cli/ci)，或[TypeScript SDK 指南](/zh-Hant/codex/security/sdk)。
