<!-- source: https://learn.chatgpt.com/zh-Hans/docs/build-plugins -->

如需构建或提交插件，请参阅
[developers.openai.com 上的完整插件构建文档](/plugins)。

<div className="not-prose my-6">
  
    构建并提交插件
  
</div>

本页提供简要介绍。插件是一种可安装的软件包，可以包含技能、MCP 服务器，也可以同时包含两者。MCP 服务器还可以返回可选的用户界面。

ChatGPT 和 Codex 共用一个通用插件目录。公开插件只需发布一次，用户便可在两款产品受支持的界面中找到同一个插件条目。开发期间，请先通过本地市场测试软件包，再将其提交到通用目录。

如需通过 GitHub 在工作空间内分发插件，请参阅
[插件管理](/zh-Hans/codex/enterprise/plugin-management)。

如果您仍在迭代某个个人工作流程，请先从技能入手。如果您希望共享该工作流程、打包相关技能、连接外部服务或向团队分发稳定的能力，请构建插件。

## 使用 `@plugin-creator` 创建插件

如需以最快的方式完成设置，请在 ChatGPT Work 模式中使用内置的 `@plugin-creator` 技能，
或在 Codex 中使用 `$plugin-creator`。

  
    
  

请说明您希望实现的结果、要包含的技能或 MCP 服务器，以及是否需要用于测试的本地市场条目。例如：

```text
@plugin-creator Create a plugin named meeting-follow-up.
Include a skill that turns meeting notes into decisions, owners, and next steps.
Add it to a personal marketplace so I can test it locally.

该技能会创建所需的 `.codex-plugin/plugin.json` 清单，
整理插件文件夹，还可以将插件添加到本地市场。

  
    
  

该技能运行完成后：

1. 审查 `.codex-plugin/plugin.json`。
2. 检查 `skills/` 目录下的每项随附技能。
3. 刷新 ChatGPT 或 Codex，然后从该插件对应的本地市场源进行安装。
4. 在新对话中使用具有代表性的请求测试该插件。

如果插件包含 MCP 服务器，请先构建并测试该服务器，然后
向 `@plugin-creator` 提供已注册连接的详细信息。请遵循完整的
[MCP 服务器工作流程](https://developers.openai.com/plugins/build/mcp-server)
中有关工具、身份验证、部署和测试的说明。

## 手动创建仅包含技能的插件

最简插件包含一份清单和至少一项技能：

```text
meeting-follow-up/
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── meeting-follow-up/
        └── SKILL.md

创建 `.codex-plugin/plugin.json`：

```json
{
  "name": "meeting-follow-up",
  "version": "1.0.0",
  "description": "Turn meeting notes into decisions and next steps",
  "skills": "./skills/"
}

然后添加 `skills/meeting-follow-up/SKILL.md`：

```md
---
name: meeting-follow-up
description: Extract decisions, owners, and next steps from meeting notes.
---

Review the meeting notes. Return:

1. Decisions
2. Action items with owners
3. Open questions

插件名称应保持稳定，并采用小写单词以连字符分隔的格式。技能描述应足够具体，以便 ChatGPT 和 Codex 判断该工作流程的适用场景。

使用 `@plugin-creator` 将文件夹添加到本地市场，然后安装并
测试该插件，再进行共享。

## 继续阅读插件构建文档

如需查阅完整的插件构建文档，请参阅
[插件文档](https://developers.openai.com/plugins/)。其中涵盖以下内容：

- [插件架构](https://developers.openai.com/plugins/concepts/plugins)
- [构建技能](https://developers.openai.com/plugins/build/skills)
- [构建 MCP 服务器](https://developers.openai.com/plugins/build/mcp-server)
- [添加可选的用户界面](https://developers.openai.com/plugins/build/chatgpt-ui)
- [打包插件](https://developers.openai.com/plugins/build/plugins)
- [测试插件](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [提交和发布](https://developers.openai.com/plugins/deploy/submission)

如需浏览、安装、启用或移除插件，请参阅[使用
插件](/zh-Hans/codex/plugins)。
