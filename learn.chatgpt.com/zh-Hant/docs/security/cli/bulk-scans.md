<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/cli/bulk-scans -->

使用 `npx @openai/codex-security bulk-scan`，在單次
掃描活動中審查程式碼庫。從個人 GitHub 帳戶或
組織探索程式碼庫，或提供 CSV，將每個程式碼庫鎖定至確切的 Git
修訂版本。

  `@openai/codex-security` 套件是公開的。執行掃描需要
  Codex Security 存取權。請按照 [CLI 快速入門](/zh-Hant/codex/security/cli) 的說明安裝
  CLI 並登入。

## 選擇程式碼庫來源

| 來源           | 適用時機                                                                          |
| ---------------- | --------------------------------------------------------------------------------------- |
| GitHub 程式碼庫探索 | 以互動方式從個人 GitHub 帳戶或組織選擇程式碼庫。 |
| CSV 清單    | 針對程式碼庫的確切修訂版本，執行可重複的自動化掃描活動。                |

這兩種工作流程都會儲存進度、保留各程式碼庫的結果，並讓你
在中斷後繼續執行掃描活動。

## 探索 GitHub 程式碼庫

使用 GitHub CLI 登入：

```bash
gh auth login

啟動互動式批次掃描：

```bash
npx @openai/codex-security bulk-scan

CLI 會引導你完成下列步驟：

1. 選擇個人 GitHub 帳戶或組織。
2. 審查過去 90 天內曾有活動的程式碼庫。
3. 搜尋程式碼庫清單，然後選擇要掃描的程式碼庫。
4. 選擇掃描結果的目錄。
5. 審查所選的程式碼庫並確認掃描活動。

探索時會排除已封存的程式碼庫和分支程式碼庫。CLI 會將每個所選程式碼庫預設分支的確切
提交記錄至
`<output-directory>/repositories.csv`。在你確認
選取項目之前，不會開始任何掃描。

若要使用 GitHub Enterprise Server，請先登入你的 GitHub 主機：

```bash
gh auth login --hostname github.example.com

開始探索程式碼庫時，請設定 `GH_HOST`：

```bash
GH_HOST=github.example.com npx @openai/codex-security bulk-scan

互動式探索需要終端。若使用 CI、容器或已準備好的
程式碼庫清單，請改用 CSV 清單。

## 建立程式碼庫 CSV

建立 CSV，其中每個程式碼庫及其鎖定的修訂版本各佔一列：

```csv
id,repository,revision,scope,mode,prompt
payments,https://github.com/example/payments.git,0123456789abcdef0123456789abcdef01234567,services/api,standard,Review payment authorization and refunds.
identity,https://github.com/example/identity.git,fedcba9876543210fedcba9876543210fedcba98,,deep,Review session and identity boundaries.

CSV 支援下列欄位：

| 欄位       | 必填 | 說明                                                                                                |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------------- |
| `id`         | 是      | 程式碼庫的唯一識別碼。請使用字母、數字、句點、連字號或底線。                      |
| `repository` | 是      | HTTPS URL、SSH URL 或本機程式碼庫路徑。相對路徑會以 CSV 所在目錄為基準解析。               |
| `revision`   | 是      | 長度為 40 或 64 個字元的完整 Git 提交 SHA。不支援分支名稱、標籤或縮短的提交雜湊值。 |
| `scope`      | 否       | 要掃描的目錄，使用相對於程式碼庫的路徑。省略此值即可掃描整個程式碼庫。                       |
| `mode`       | 否       | `standard` 或 `deep`。省略此值即可使用指令所選的模式。                                   |
| `prompt`     | 否       | 此程式碼庫專用的掃描指示。                                                             |

若要找出本機程式碼庫的完整提交 SHA，請執行：

```bash
git -C /path/to/repository rev-parse HEAD

## 從 CSV 執行掃描活動

傳入 CSV 以及位於程式碼庫外部的私密輸出目錄：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

`--workers` 控制同時進行的程式碼庫掃描數量，預設值為 `4`。此設定
不會決定每次深度掃描中獨立標準掃描工作程序的數量；
請透過
[`[deep_scan]`](/zh-Hant/codex/security/cli/reference#configure-deep-scans) 設定這些限制。使用 `--mode
deep`，即可為未自行設定 `mode` 的資料列選擇深度掃描。每個 CSV 資料列
仍可自行選擇掃描模式和程式碼庫範圍。

設定 `[deep_scan].max_time_hours`，即可限制掃描活動中
每次深度掃描的工作程序執行。`--max-time-hours` 旗標適用於 `scan`，不適用於 `bulk-scan`。

CLI 會簽出每個鎖定的修訂版本、掃描所選目標並記錄
結果，接著移除暫時簽出的程式碼庫。只有掃描涵蓋範圍
完整，且所有必要的結果產出檔案都存在，程式碼庫
才算完成。

## 共用安全性上下文與指示

若要在每次掃描中加入架構文件、威脅模型或安全性政策，
請使用 `--knowledge-base`。若要加入更多檔案或目錄，請重複指定此旗標：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

若要加入共用掃描指示，或在每次掃描後執行後續指示，
請提供提示詞檔案：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --scan-prompt-file scan-instructions.md \
  --post-scan-prompt-file follow-up.md

CLI 會將每個程式碼庫在 CSV 中的 `prompt` 附加至共用掃描
指示之後。掃描成功、涵蓋範圍不完整或發生錯誤後，後續指示都會在同一個已通過身分驗證的工作階段
中執行；但掃描遭到取消或達到成本上限時，則
不會執行。提示詞檔案的路徑會以
目前目錄為基準解析。

## 選擇模型與推理強度

批次掃描預設使用 `gpt-5.6-sol` 模型，推理強度為 `xhigh`。若要
為 CSV 掃描活動選擇其他模型和推理強度：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --model gpt-5.6-terra \
  --effort high

互動式程式碼庫探索也能使用相同的選項：

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

支援的推理強度等級為 `minimal`、`low`、`medium`、`high` 和 `xhigh`。

若要使用 OpenRouter 或 Fireworks，請分別設定 `OPENROUTER_API_KEY` 或 `FIREWORKS_API_KEY`，
並指定 `--provider` 和 `--model`。如需憑證和
範例，請參閱 [OpenRouter 或 Fireworks
設定](/zh-Hant/codex/security/cli/reference#use-openrouter-or-fireworks) 或 [Amazon Bedrock
設定](/zh-Hant/codex/security/cli/reference#use-amazon-bedrock)。

## 審查掃描活動結果

輸出目錄包含已鎖定的掃描活動、僅可附加的結果
紀錄簿，以及每個程式碼庫和每次嘗試各自的產出檔案：

```text
security-scans/
├── manifest.json
├── results.jsonl
├── checkouts/
└── artifacts/
    ├── payments/
    │   └── attempt-1/
    │       ├── scan-manifest.json
    │       ├── findings.json
    │       ├── coverage.json
    │       └── report.md
    └── identity/
        └── attempt-1/
            ├── scan-manifest.json
            ├── findings.json
            ├── coverage.json
            └── report.md

- `manifest.json` 會記錄掃描活動中的程式碼庫、鎖定的修訂版本、範圍、掃描
  模式，以及共用或程式碼庫專屬的指示。
- `results.jsonl` 會記錄每次程式碼庫掃描嘗試、其狀態、產出檔案
  目錄，以及任何可用的成本或錯誤詳細資料。
- `report.md` 會針對單次程式碼庫掃描嘗試，提供易於閱讀的報告。
- `findings.json` 和 `coverage.json` 會記錄該次嘗試的發現項目和
  已審查範圍。

如需可攜式結果，請匯出一項已完成的程式碼庫掃描：

```bash
npx @openai/codex-security export \
  /path/outside/repositories/security-scans/artifacts/payments/attempt-1 \
  --export-format sarif \
  --output /path/outside/repositories/payments.sarif

掃描結果可能包含原始碼摘錄和漏洞詳細資料。請確保
輸出目錄不對外公開，置於受掃描的程式碼庫之外，並遵循
適當的保留政策。

## 繼續執行掃描作業

使用相同的 CSV 和輸出目錄，再次執行原始指令：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

CLI 會繼續執行未完成的程式碼庫掃描，並略過已完成的掃描。涵蓋範圍
不完整的掃描不會重試。其結果仍可使用，且
指令會以代碼 `2` 結束。

請勿變更現有輸出目錄所對應的程式碼庫清單，或掃描與後續指示。
CLI 會檢查已釘選的資訊清單，並拒絕執行其他掃描作業。
變更程式碼庫、修訂版本、範圍、掃描模式，
或共用或程式碼庫專屬的指示時，請使用新的輸出目錄。

## 重試發生錯誤的程式碼庫

使用 `--max-attempts`，在程式碼庫發生暫時性的簽出或掃描
錯誤後重試：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

每個程式碼庫預設只會嘗試一次。每次嘗試都有各自的
回執與產出物目錄。可重試的情況包括簽出錯誤、掃描失敗，
以及缺少必要產出物。已完成但涵蓋範圍不完整的掃描
不會重試。

批次掃描使用以下結束代碼：

| 結束代碼 | 說明                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| `0`       | 所有程式碼庫均已成功完成掃描。                                                                              |
| `2`       | 有程式碼庫未能完成掃描、某次掃描的涵蓋範圍不完整，或指令遇到輸入或執行階段錯誤。 |
| `130`     | Ctrl-C 中斷了掃描作業。                                                                                      |
| `143`     | SIGTERM 終止了掃描作業。                                                                                      |

## 在 Docker 中執行批次掃描

[Codex Security
程式碼庫](https://github.com/openai/codex-security)提供經過安全性強化的
Compose 組態，可在 Linux Docker 主機上執行自動化 CSV 掃描作業。
該主機必須支援建立非特權使用者命名空間。

請將程式碼庫 CSV、掃描結果和登入狀態掛載至持久性
目錄。透過環境或機密
管理工具提供 OpenAI 憑證。私人 GitHub 程式碼庫所需的 `GH_TOKEN` 或 `GITHUB_TOKEN`
也請以相同方式提供。

使用已掛載的 CSV 和輸出目錄執行映像檔：

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

使用相同的已掛載 CSV 和輸出目錄，繼續執行掃描作業。
若使用 GitHub Enterprise Server，請將 `CODEX_SECURITY_GIT_HOST` 設為您的 GitHub 主機。

如需查看所有可用旗標，請參閱 [bulk-scan 指令
參考資料](/zh-Hant/codex/security/cli/reference#codex-security-bulk-scan)。如需瞭解掃描涵蓋範圍和發現項目的常見
問題，請參閱 [CLI
常見問題](/zh-Hant/codex/security/cli/faq)。
