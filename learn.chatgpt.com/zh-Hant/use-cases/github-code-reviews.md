<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/github-code-reviews -->

## 使用方式

首先，請將 Codex 程式碼審查新增至您的 GitHub 組織或程式碼庫。
如需詳細資訊，請參閱 [GitHub 中的 Codex 程式碼審查](/zh-Hant/codex/third-party/github)。

您可以設定 Codex 自動審查每個 Pull Request，也可以在 Pull Request 留言中使用 `@codex review` 要求審查。

如果 Codex 指出迴歸或潛在問題，您可以在 Pull Request 留言中加入如 `@codex fix it` 的後續提示詞，要求它修正問題。

這會啟動新的雲端對話來修正問題，並更新 Pull Request。

## 制定審查指引

若要自訂 Codex 的審查內容，請將 `## Code Review Rules` 區段新增至離規則所適用的程式碼最近的
`AGENTS.md`。例如：

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

請將適用整個程式碼庫的規則放在根目錄的 `AGENTS.md`，並將特定服務的規則
放在巢狀檔案中。規則應保持簡潔，並說明要標示的行為，以及任何
安全做法或例外情況；格式化與 lint 檢查則交由 CI 執行。請參閱
[自訂 Codex 的審查內容](/zh-Hant/codex/third-party/github#customize-what-codex-reviews)
以了解設定與規則撰寫指引。
