<!-- source: https://learn.chatgpt.com/zh-Hant/docs/open-source -->

OpenAI 採開源方式開發 Codex 的關鍵部分。相關工作託管於 GitHub，方便你追蹤進度、回報問題及貢獻改進內容。

如果你維護廣泛使用的開源專案，或想提名重要專案的維護者，也可以 [申請加入 Codex for OSS 計畫](/community/codex-for-oss)，以取得 API 點數、含 Codex 的 ChatGPT Pro，以及經遴選後使用 Codex Security 的資格。

## 開源元件

| 元件                     | 所在位置                                                                                             | 備註                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Codex CLI                     | [openai/codex](https://github.com/openai/codex)                                                           | Codex 開源開發的主要程式碼庫      |
| Codex SDK                     | [openai/codex/codex-sdk](https://github.com/openai/codex/tree/main/sdk)                                   | SDK 原始碼位於 Codex 程式碼庫中                      |
| Codex Security CLI            | [openai/codex-security](https://github.com/openai/codex-security)                                         | 用來找出及驗證安全性漏洞的 CLI |
| Codex Security TypeScript SDK | [openai/codex-security/sdk/typescript](https://github.com/openai/codex-security/tree/main/sdk/typescript) | 用來執行 Codex Security 掃描的 TypeScript SDK         |
| Codex App Server              | [openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)         | App Server 原始碼位於 Codex 程式碼庫中               |
| 技能                        | [openai/skills](https://github.com/openai/skills)                                                         | 可擴充 ChatGPT 與 Codex 功能的可重複使用技能           |
| 外掛程式                       | [openai/plugins](https://github.com/openai/plugins)                                                       | 適用於 ChatGPT 與 Codex 的可重複使用外掛程式                  |
| IDE 擴充功能                 | -                                                                                                         | 非開源                                         |
| Codex 雲端                   | -                                                                                                         | 非開源                                         |
| 通用雲端環境   | [openai/codex-universal](https://github.com/openai/codex-universal)                                       | Codex 雲端所使用的基礎環境                    |

## 問題回報與功能要求管道

請在對應的 GitHub 程式碼庫回報錯誤及提出功能要求：

- Codex 錯誤回報與功能要求：[openai/codex/issues](https://github.com/openai/codex/issues)
- Codex Security CLI 與 TypeScript SDK 的錯誤回報與功能要求：[openai/codex-security/issues](https://github.com/openai/codex-security/issues)
- 討論論壇：[openai/codex/discussions](https://github.com/openai/codex/discussions)

回報問題時，請註明你使用的元件（CLI、SDK、IDE 擴充功能、Codex 雲端或 Codex Security），並盡可能附上版本資訊。
