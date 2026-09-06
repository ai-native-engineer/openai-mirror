<!-- source: https://learn.chatgpt.com/zh-Hant/docs/agent-configuration/rules -->

使用規則控制 Codex 可在沙盒外執行哪些指令。

規則目前仍屬實驗性質，可能會變更。

## 建立規則檔案

1. 建立一個 `.rules` 檔案，並將它放在作用中設定層旁的 `rules/` 資料夾下（例如 `~/.codex/rules/default.rules`）。
2. 新增規則。此範例會先顯示提示，再允許 `gh pr view` 在沙盒外執行。

   ```python
   # Prompt before running commands with the prefix `gh pr view` outside the sandbox.
   prefix_rule(
       # The prefix to match.
       pattern = ["gh", "pr", "view"],

       # The action to take when Codex requests to run a matching command.
       decision = "prompt",

       # Optional rationale for why this rule exists.
       justification = "Viewing PRs is allowed with approval",

       # `match` and `not_match` are optional "inline unit tests" where you can
       # provide examples of commands that should (or should not) match this rule.
       match = [
           "gh pr view 7888",
           "gh pr view --repo openai/codex",
           "gh pr view 7888 --json title,body,comments",
       ],
       not_match = [
           # Does not match because the `pattern` must be an exact prefix.
           "gh pr --repo openai/codex view 7888",
       ],
   )

3. 重新啟動 Codex。

Codex 啟動時，會掃描每個作用中設定層下的 `rules/`，包括 [團隊設定](/zh-Hant/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config) 的位置，以及位於 `~/.codex/rules/` 的使用者層。位於 `<repo>/.codex/rules/` 的專案本機規則，只有在專案的 `.codex/` 層受信任時才會載入。

當你在 TUI 中將指令加入允許清單時，Codex 會寫入位於 `~/.codex/rules/default.rules` 的使用者層，讓之後執行時可以略過提示。

智慧核准啟用時（預設為啟用），Codex 可能會在處理權限提升要求的過程中，為你建議一項
`prefix_rule`。接受前，請檢查建議的前綴，
並務必審慎確認。

管理員也可以強制套用限制性的 `prefix_rule` 項目；這些項目來自
[`requirements.toml`](/zh-Hant/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)。

## 瞭解規則欄位

`prefix_rule()` 支援下列欄位：

- `pattern` **（必填）**：用於定義所要比對之指令前綴的非空清單。每個元素可以是下列任一項：
  - 常值字串（例如 `"pr"`）。
  - 常值聯集（例如 `["view", "list"]`），用於比對該引數位置的不同選項。
- `decision` **（預設為 `"allow"`）**：規則相符時要採取的動作。如果有多個規則相符，Codex 會套用限制最嚴格的決策（`forbidden` \> `prompt` \> `allow`）。
  - `allow`：不顯示提示，直接在沙盒外執行指令。
  - `prompt`：每次符合規則的呼叫前都顯示提示。
  - `forbidden`：不顯示提示，直接封鎖要求。
- `justification` **（選填）**：非空且便於閱讀的規則理由。Codex 可能會在核准提示或拒絕訊息中顯示此理由。使用 `forbidden` 時，請視情況在理由中加入建議的替代方案（例如，`"Use \`rg\`，而不要使用 \`grep\`。"\`）。
- `match` 和 `not_match` **（預設為 `[]`）**：Codex 載入規則時會驗證的範例。請用這些範例在規則生效前找出錯誤。

Codex 考慮執行某個指令時，會將該指令的引數清單與 `pattern` 比對。在內部，Codex 會將指令視為引數清單（類似 `execvp(3)` 接收的內容）。

## Shell 包裝器與複合指令

有些工具會將多個 Shell 指令包裝成一次呼叫，例如：

```text
["bash", "-lc", "git add . && rm -rf /"]

由於這類指令可將多個動作隱藏在單一字串中，Codex 會特別處理 `bash -lc`、`bash -c`，以及兩者在 `zsh` / `sh` 中的對等形式。

### Codex 可安全分割指令碼的情況

如果 Shell 指令碼是只由下列項目組成的線性指令鏈：

- 一般字詞（不含變數展開，也不含 `VAR=...`、`$FOO`、`*` 等）
- 以安全運算子（`&&`、`||`、`;` 或 `|`）連接

Codex 就會使用 tree-sitter 解析指令碼，將它分割成個別指令，再套用你的規則。

上述指令碼會被視為兩個獨立指令：

- `["git", "add", "."]`
- `["rm", "-rf", "/"]`

接著，Codex 會根據你的規則評估每個指令，並採用限制最嚴格的結果。

即使你允許 `pattern=["git", "add"]`，Codex 也不會自動允許 `git add . && rm -rf /`，因為 `rm -rf /` 部分會單獨評估，導致整次呼叫無法獲得自動允許。

這可防止危險指令夾帶在安全指令中一起執行。

### Codex 不會分割指令碼的情況

如果指令碼使用較進階的 Shell 功能，例如：

- 重新導向（`>`、`>>`、`<`）
- 命令替換（`$(...)`、`...`）
- 環境變數（`FOO=bar`）
- 萬用字元模式（`*`、`?`）
- 控制流程（`if`、`for`、搭配指派的 `&&` 等）

Codex 就不會嘗試解譯或分割指令碼。

在這些情況下，整次呼叫會被視為：

```text
["bash", "-lc", "<full script>"]

而你的規則會套用到那個 **單一** 呼叫。

這種處理方式可兼顧安全性：在安全可行時逐一評估指令，否則採取保守做法。

## 測試規則檔案

使用 `codex execpolicy check` 測試規則如何套用至指令：

```shell
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888 --json title,body,comments

此指令會輸出 JSON，顯示限制最嚴格的決策及所有相符規則，包括相符規則中的任何 `justification` 值。若要合併檔案，請使用多個 `--rules` 旗標；若要格式化輸出，請加上 `--pretty`。

## 瞭解規則語言

`.rules` 檔案格式使用 `Starlark`（請參閱 [語言規格](https://github.com/bazelbuild/starlark/blob/master/spec.md)）。其語法類似 Python，但設計上可安全執行：規則引擎執行它時不會產生副作用（例如變更檔案系統）。
