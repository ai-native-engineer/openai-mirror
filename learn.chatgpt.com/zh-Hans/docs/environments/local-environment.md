<!-- source: https://learn.chatgpt.com/zh-Hans/docs/environments/local-environment -->

本地环境可让您为工作树配置设置步骤，并为项目配置常用操作。

  本地环境仅可在 ChatGPT 桌面应用的 Codex 中使用。
  配置或使用本地环境前，请先选择 **Codex** 。

您可以通过 [ChatGPT 桌面应用设置](codex://settings)窗格配置本地环境。您可以将生成的文件提交到项目的 Git 代码仓库，以便与他人共享。

Codex 会将此配置存储在项目根目录下的 `.codex` 文件夹中。
如果您的代码仓库包含多个项目，
请打开包含共享 `.codex` 文件夹的项目目录。

## 设置脚本

由于工作树与本地聊天在不同目录中运行，您的项目可能尚未完成设置，并且可能缺少依赖项或未提交到代码仓库的文件。每当 Codex 在新聊天开始时创建新的工作树，设置脚本都会自动运行。

请使用此脚本运行配置环境所需的任何命令，例如安装依赖项或执行构建流程。

例如，对于 TypeScript 项目，您可以使用设置脚本安装依赖项并执行初始构建：

```bash
npm install
npm run build

如果设置因平台而异，请为 macOS、Windows 或 Linux 定义相应的设置脚本，以覆盖默认脚本。

## 操作

<section class="feature-grid">

<div>
您可以使用操作定义常用任务，例如启动应用的开发服务器或运行测试套件。这些操作会显示在 ChatGPT 桌面应用的顶部栏中，方便快速访问。操作会在应用的[集成终端](/zh-Hans/codex/integrated-terminal)中运行。

通过这些操作，您无需再为触发项目构建或启动开发服务器等常见任务手动输入命令。对于一次性快速调试，您可以直接使用集成终端。

</div>

  
    
  

</section>

例如，对于 Node.js 项目，您可以创建一个名为“运行”的操作，其中包含以下脚本：

```bash
npm start

如果操作所用的命令因平台而异，请分别为 macOS、Windows 和 Linux 定义对应平台的脚本。

为便于识别各项操作，请为每项操作选择相应的图标。

## 使用内置 Git 工具

<div class="my-8 grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-center">

<div>

在 Codex 中，ChatGPT 桌面应用会在每个
本地项目和工作树旁提供常用的 Git 控件。差异窗格会显示当前签出内容中的更改，
并允许您添加行内评论，供 Codex 处理。您可以暂存或还原单个
变更块、暂存或还原整个文件、提交更改、推送分支，以及创建
Pull Request，整个过程都无需离开应用。

请使用[集成终端](/zh-Hans/codex/integrated-terminal)执行应用中未提供的 Git
操作。如需将并发更改与
您的本地签出内容隔离，请在[工作树](/zh-Hans/codex/environments/git-worktrees)中启动任务。

</div>

  

</div>
