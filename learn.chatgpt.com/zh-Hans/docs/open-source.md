<!-- source: https://learn.chatgpt.com/zh-Hans/docs/open-source -->

OpenAI 以开源方式开发 Codex 的关键部分。相关工作托管在 GitHub 上，您可以在此跟进进展、报告问题并贡献改进。

如果您维护着一个广泛使用的开源项目，或者想提名负责重要项目的维护者，还可以[申请 Codex for OSS 计划](/community/codex-for-oss)，以获得 API 额度、可使用 Codex 的 ChatGPT Pro，以及 Codex Security 的选择性访问权限。

## 开源组件

| 组件                     | 获取位置                                                                                             | 说明                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Codex CLI                     | [openai/codex](https://github.com/openai/codex)                                                           | Codex 开源开发的主要代码仓库      |
| Codex SDK                     | [openai/codex/codex-sdk](https://github.com/openai/codex/tree/main/sdk)                                   | SDK 的源代码位于 Codex 代码仓库中                      |
| Codex Security CLI            | [openai/codex-security](https://github.com/openai/codex-security)                                         | 用于发现和验证安全漏洞的 CLI |
| Codex Security TypeScript SDK | [openai/codex-security/sdk/typescript](https://github.com/openai/codex-security/tree/main/sdk/typescript) | 用于运行 Codex Security 扫描的 TypeScript SDK         |
| Codex App Server              | [openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)         | App Server 的源代码位于 Codex 代码仓库中               |
| 技能                        | [openai/skills](https://github.com/openai/skills)                                                         | 用于扩展 ChatGPT 和 Codex 的可复用技能           |
| 插件                       | [openai/plugins](https://github.com/openai/plugins)                                                       | 供 ChatGPT 和 Codex 使用的可复用插件                  |
| IDE 扩展                 | -                                                                                                         | 非开源                                         |
| Codex 云端                   | -                                                                                                         | 非开源                                         |
| 通用云端环境   | [openai/codex-universal](https://github.com/openai/codex-universal)                                       | Codex 云端使用的基础环境                    |

## 在哪里报告问题和提出功能请求

请使用相应的 GitHub 代码仓库提交错误报告和功能请求：

- Codex 的错误报告和功能请求：[openai/codex/issues](https://github.com/openai/codex/issues)
- Codex Security CLI 和 TypeScript SDK 的错误报告和功能请求：[openai/codex-security/issues](https://github.com/openai/codex-security/issues)
- 讨论论坛：[openai/codex/discussions](https://github.com/openai/codex/discussions)

提交问题时，请注明您使用的组件（CLI、SDK、IDE 扩展、Codex 云端或 Codex Security），并尽可能提供版本信息。
