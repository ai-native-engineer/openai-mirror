<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/qa-your-app-with-computer-use -->

## 简介

计算机使用非常适合开展 QA 测试，因为它可以查看界面、逐步操作各个流程、在字段中输入内容，并记录出错环节。因此，它有助于在贴近实际的用户操作路径中发现功能缺陷和 UI 问题。

关键在于告诉 Codex 要测试哪个环境、哪些流程最重要，以及您希望它返回哪种报告。

## 如何使用

1. 安装 [计算机使用插件](/zh-Hans/codex/computer-use)。
2. 告诉 Codex 要测试哪个应用、构建版本或环境。
3. 列出您最关心的流程或核心使用场景。
4. 要求 Codex 提供结构化报告，使输出结果便于分类处理或转交他人。

您可以只提出宽泛的要求：

- `@Computer Test my app. Find any major issues and give me a report.`

也可以提出更明确的要求：

- `@Computer Test my app in staging. Cover signup, invite a teammate, and upgrade billing. Log every bug with repro steps, expected result, actual result, and severity.`

如果您已在代码仓库中维护测试计划文件，请将其附加到聊天中，或向 Codex 指明该文件的位置，以便本轮 QA 测试遵循您已有的流程。

## 实用技巧

### 明确说明测试设置

如果账户状态、测试数据、功能开关或环境选择会影响流程，请一开始就说明这些信息。当 Codex 知道测试应在本地环境、预发布环境还是类生产环境中进行时，测试结果会好得多。

### 列出您关注的问题类型

请说明您希望 Codex 重点关注功能故障、布局问题、难以理解的文案、视觉回归，还是上述所有问题。

### 决定是停止还是继续

如果出现任何一个阻塞性问题就应结束本轮测试，请明确说明。否则，请让 Codex 继续完成其余流程，并在总结前收集所有非阻塞性问题。

## 后续操作建议

完成本轮 QA 测试后，请继续使用同一聊天，让 Codex 修复它发现的某个缺陷、将发现的问题整理成适合提交到 Linear 或 GitHub 的草稿，或者让下一轮测试仅聚焦某个出现故障的具体流程。

## 建议的提示

**执行一轮结构化 QA 测试**
