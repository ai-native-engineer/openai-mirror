<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/skills -->

技能是由指令和辅助资源构成的可复用工作流。
ChatGPT 工作空间技能、供 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展中
本文涵盖的本地功能使用的文件系统技能，以及将技能打包的插件，各有独立的
生命周期和访问控制。

有关完整的管理模型，请参阅
[角色和工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)。

<a id="distinguish-the-distribution-models"></a>

## 技能分发与管理

| 分发模式      | 适用场景                                                                                           | 管理边界                                                                       |
| ----------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| ChatGPT 工作空间技能 | 通过 ChatGPT 工作空间中受支持的功能共享或安装已批准的工作流              | ChatGPT 工作空间技能的权限和生命周期控制                                    |
| 本地文件系统技能  | 从代码仓库级、用户级、管理员级或系统内置位置加载已安装的工作流     | 文件系统分发、本地客户端配置和运行时权限                  |
| 插件                  | 将一项或多项技能与可选的连接器、MCP 服务器、钩子和展示元数据一起打包 | 插件的可用性和安装，以及每项捆绑功能各自的控制机制 |

ChatGPT 工作空间技能分发、本地文件系统技能安装，以及
针对特定使用界面的插件安装各自采用独立的路径。迁移技能不会
转移 ChatGPT 工作空间所有权、共享设置、角色分配、插件
安装状态或连接器授权。

插件可用于 ChatGPT 网页版、桌面版和移动版中的聊天和 Work，
也可用于 ChatGPT 桌面应用中的 Codex，还可通过 Codex CLI 插件浏览器使用。
IDE 扩展中不提供插件。
这些受支持的界面从一个通用目录获取公开插件，该目录
由 ChatGPT 和 Codex 共享。

## 控制归属

请参阅 [构建技能](/zh-Hans/codex/build-skills)，了解文件系统位置和编写方法；
[ChatGPT 中的技能](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
介绍当前适用的工作空间操作流程；请参阅 [构建插件](https://developers.openai.com/plugins/build/plugins)，了解
插件打包方法。

ChatGPT 工作空间控制机制不会安装本地文件系统技能或插件。
文件系统分发不会分配 ChatGPT 工作空间的所有权或角色。
安装插件不会授予对连接器、MCP 服务器或
已连接服务的访问权限。请在各项功能所属的控制界面中
逐项进行配置。

## 相关文档

- [技能和插件](/zh-Hans/codex/skills-and-plugins)
- [插件](/zh-Hans/codex/plugins)
- [构建技能](/zh-Hans/codex/build-skills)
- [构建插件](https://developers.openai.com/plugins/build/plugins)
- [管理员部署指南](/zh-Hans/codex/enterprise/admin-setup)
- [插件控制](/zh-Hans/codex/enterprise/apps-and-connectors)
