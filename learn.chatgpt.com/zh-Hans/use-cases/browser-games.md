<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/browser-games -->

## 简介

游戏开发是最能体现 Codex 的作用不止于代码生成的场景之一。一款真正的游戏通常需要书面创意方案、渲染层、前端应用外壳开发、后端状态管理、资产制作，以及持续的视觉调优

在此用例中，最好先让 Codex 明确写下游戏应具备的具体功能，然后使用 Playwright interactive 在实际浏览器中测试游戏并反复迭代。

## 先制定游戏计划

在 Codex 开始搭建项目框架之前，请先让它创建 `PLAN.md` 文件，用具体条目定义游戏：

- 玩家目标
- 核心循环
- 输入与操控
- 胜利与失败状态
- 游戏进度或难度
- 视觉设计方向
- 技术栈与托管方面的假设
- 里程碑顺序

这份计划之所以重要，是因为“构建一款游戏”本身过于笼统。Codex 需要了解游戏各部分应如何实现，并且在构建过程中往往还要参考这些实现细节。

您可以使用 `/plan` 斜杠命令启用计划模式。
将输出保存到 `PLAN.md` 文件中。

## 使用 AGENTS.md 指导 Codex 的行为

为确保 Codex 遵循计划、验证其工作成果并使用正确的工具，请创建一个内容如下的 `AGENTS.md` 文件：

```text
# Game name

Tech Stack:

- NextJS for frontend (hosted on Vercel)
- <insert technology> for rendering
- Fastify for backend, websockets (hosted on <hosting platform>)
- Postgres for database (hosted on <hosting platform>)
- Redis for caching and pub/sub (hosted on <hosting platform>)
- OpenAI for generative AI features

Tips:

- Use build and test commands to verify your work as soon as you complete a feature or task
- Use the PLAN.md file to guide your work when building new features
- Log your work under .logs (create new log files as you see fit) to record your thought process and decisions, and reference them when iterating on features
- Use playwright to test the visual output of your work, and iterate if it doesn't look right or fit the vibe
- Use imagegen to generate visual assets for your work, and every time you generate a collection of assets, save the prompts you used to be able to continue generating more of the same assets later (create files in .prompts)
- Use Context7 MCP to fetch <rendering framework> docs

这样，Codex 就可以长时间独立运行，并根据需要使用相关技能。

## 使用技能

添加 AGENTS.md 文件中提到的技能：

- Imagegen，让 Codex 能够按需为游戏生成视觉资产
- Playwright interactive，让 Codex 能够在实际浏览器中测试游戏
- OpenAI 文档，让 Codex 能够获取最新的 OpenAI API 文档
- 您也可以选择添加 Context7 MCP 服务器，以获取渲染框架的最新文档

如需进一步了解如何添加技能，请参阅 [技能文档](/zh-Hans/codex/build-skills)。

  **提示**：请让 Codex 将图像生成提示词保存在文件中，以确保
  所有视觉资产保持一致。请说明您
  希望生成的资产风格，并让 Codex 编写详细且可复用的提示词。

## 让 Codex 开始工作并持续迭代

Codex 会根据初始计划生成游戏的第一个版本。

如果需要生成大量图像资产，第一个版本可能需要较长时间，有时甚至长达数小时。由于 Codex 能够测试自己的工作成果，并在实际浏览器中试玩游戏，因此无需您提供任何输入，也能长时间持续工作。

计划越明确，首次迭代完成后的输出结果就越好。

在测试过程中，您可以根据需要提供屏幕截图，要求调整玩法或更新视觉资产，并不断迭代，直到对结果满意为止。
