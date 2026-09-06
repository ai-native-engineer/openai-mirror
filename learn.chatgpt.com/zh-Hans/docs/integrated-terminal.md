<!-- source: https://learn.chatgpt.com/zh-Hans/docs/integrated-terminal -->

ChatGPT 桌面应用中的每个聊天会话都配有一个终端，其作用域限定为当前项目或
工作树。您可以点击应用右上角的终端图标打开它，或
按 <kbd>Ctrl</kbd>+<kbd>\`</kbd>。

  
    
  

## 运行并验证您的项目

使用终端验证更改、运行脚本和执行 Git 操作，
无需切换应用。ChatGPT 可以读取当前终端输出，
因此在与您协作时，能够检查正在运行的开发服务器，
或查看失败的构建情况。

常用命令包括：

- `git status`
- `git pull --rebase`
- `pnpm test` 或 `npm test`
- `pnpm run lint` 或其他项目专用的检查命令

## 创建可复用操作

如果您经常运行某个命令，请在[本地环境](/zh-Hans/codex/environments/local-environment#actions)中定义一个操作。
操作会在 ChatGPT 桌面应用中显示为快捷方式，并在集成
终端中运行。

<kbd>Cmd</kbd>+<kbd>K</kbd> 会打开应用的命令面板，但不会清空
终端。要清空终端，请按 <kbd>Ctrl</kbd>+<kbd>L</kbd>。
