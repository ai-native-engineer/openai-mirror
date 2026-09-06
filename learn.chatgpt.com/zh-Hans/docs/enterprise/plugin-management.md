<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/plugin-management -->

## 开始之前

工作空间管理员可以从 GitHub 导入插件市场，并从代码仓库同步插件更新。市场是一个 JSON 格式的目录，其中列出了要导入的插件。

请使用能够读取市场代码仓库及其引用的其他所有代码仓库的 GitHub 账户。支持公开和私有 GitHub 代码仓库。导入前，请完成访问代码仓库所需的所有 GitHub 组织审批。

导入前，请审查代码仓库内容。新插件的初始安装策略为 **可用** ，并在安装时进行身份验证。新市场默认启用每日自动同步。导入会处理所有有效条目，后续同步会自动添加代码仓库中的所有新增插件。

## 配置市场同步

1. 打开 **管理** \> **插件** ，然后选择 **添加** \> **导入市场**。
2. 在 **来源**中输入代码仓库 URL，例如 `https://github.com/example/team-plugins`。仅使用代码仓库 URL，不要使用分支或文件夹的 URL。
3. 如果市场位于子目录中，请在 **路径**中输入该目录。例如，对于 `team-tools/.agents/plugins/marketplace.json`，请输入 `team-tools`。如果位于代码仓库根目录，请将 **路径** 留空。不要输入清单文件名。
4. 您可以选择输入 **分支、标签或提交**。留空则使用代码仓库的默认分支。指定分支可接收后续提交；指定固定提交则会停留在该版本。
5. 选择 **导入市场** ，并在出现提示时授权 GitHub 访问。对于规模很大的市场，首次导入可能需要长达一小时。后续每日同步通常需要几分钟。
6. 检查 **导入结果**，然后逐一打开已导入的插件，配置其安装策略和所需的应用。

如需请求更新而不等待每日同步，请在 **管理** \> **插件** \> **市场** 下打开该市场，然后选择 **立即同步**。

## 支持的格式

所选目录必须包含以下文件之一：

| 文件                               | 格式                                                               |
| ---------------------------------- | -------------------------------------------------------------------- |
| `.agents/plugins/marketplace.json` | 包含 `plugins` 数组的 Codex 市场。                          |
| `.claude-plugin/marketplace.json`  | 包含 `plugins` 数组的 Claude 兼容市场。              |
| `.claude-plugin/plugin.json`       | 独立的 Claude 插件，适用于不存在市场清单的情况。 |

市场中的条目可以引用带有 `.codex-plugin/plugin.json` 的原生插件、Claude 兼容插件、Agent Plugins 1.0 软件包或受支持的技能包。

在 Codex 市场中，对于同一代码仓库中的插件，请使用本地路径：

```json
{
  "name": "team-plugins",
  "interface": {
    "displayName": "Team plugins"
  },
  "plugins": [
    {
      "name": "team-tools",
      "source": {
        "source": "local",
        "path": "./plugins/team-tools"
      }
    }
  ]
}

该路径相对于所选市场的根目录，而不是 `.agents/plugins/`。

Claude 兼容市场可以为每个本地插件使用一个路径字符串：

```json
{
  "name": "team-plugins",
  "plugins": [
    {
      "name": "team-tools",
      "source": "./plugins/team-tools"
    }
  ]
}

Codex 市场条目还支持使用 `source: "url"` 引用位于 GitHub 代码仓库根目录的插件，以及使用 `source: "git-subdir"` 引用位于 GitHub 子目录中的插件。例如：

```json
{
  "name": "team-tools",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/example/team-tools.git",
    "path": "./plugins/team-tools",
    "ref": "main"
  }
}

Git 源可以指定 `ref` 或由 40 个字符组成的完整提交 `sha`。用于授权的 GitHub 账户必须能够读取所有被引用的代码仓库。工作空间导入目前仅支持 GitHub 代码仓库。

## 配置工作空间访问权限

GitHub 导入和同步不会应用代码仓库中的安装或身份验证策略，包括 `AVAILABLE`、`INSTALLED_BY_DEFAULT`、`NOT_AVAILABLE`、`ON_INSTALL` 和 `ON_USE`。这些设置由工作空间管理员为每个插件配置。同步更新或将现有插件改为通过 GitHub 管理时，会保留其工作空间策略。

在 **安装策略** 中，为每个符合条件的角色选择 **可用** 或 **已安装** 。所需的应用也必须启用，且成员必须有权访问所连接的服务。导入插件不会授予应用访问权限，也不会连接成员的账户。有关角色、应用和操作控制，请参阅[插件控制](/zh-Hans/codex/enterprise/apps-and-connectors)。

## 将现有插件改为通过 GitHub 管理

在现有插件的市场条目中添加 `pluginId`：

```json
{
  "name": "team-tools",
  "pluginId": "plugin_0123456789abcdef0123456789abcdef",
  "source": {
    "source": "local",
    "path": "./plugins/team-tools"
  }
}

从 **管理** \> **插件** 打开该插件，复制其 URL 中 `/admin/plugins/` 后面的 ID。在市场条目中，将 `pluginId` 与 `name` 和 `source` 放在同一级。现有插件必须位于同一工作空间中。

这样会将已上传或以其他方式存在但尚未受管理的工作空间插件改为通过 GitHub 管理。插件会保留其 ID、共享设置和工作空间策略。后续更新将来自 GitHub；无法再通过上传归档文件替换受管理的插件。已由其他 GitHub 源管理的插件无法通过这种方式接管。

## 仅限桌面端的插件

任何在 `mcp.json` 或 `.mcp.json` 中声明 MCP 服务器的已导入插件，都会被标记为 **仅限桌面端** ，且只能在 ChatGPT 桌面应用中使用。这也包括使用远程 HTTPS URL 的服务器。其他受支持的 MCP 配置形式（例如内联服务器声明）同样受此限制。

## 使用 `.app.json` 引用现有应用

在插件根目录中添加 `.app.json`。文件名必须以点开头；不支持不带点的 `app.json`。

```json
{
  "apps": {
    "team-tools": {
      "id": "asdk_app_example",
      "required": true
    }
  }
}

将 `asdk_app_example` 替换为现有应用的 ID。支持的应用 ID 以 `asdk_app_`、`connector_` 或 `templated_apps_` 开头。请使用应用 ID，而不是 `plugin_...` ID。例如，包含 `plugin_asdk_app_example` 的插件 URL 表示应用 `asdk_app_example`。

键 `team-tools` 是该引用在此文件中的名称。如果插件依赖该应用，请将 `required` 设为 `true`。您可以添加更多条目来引用其他现有应用。

对于原生插件，请在 `.codex-plugin/plugin.json` 中将 `apps` 设为 `./.app.json`。以下是此示例的完整清单：

```json
{
  "name": "team-tools",
  "version": "1.0.0",
  "description": "Use the team's approved tools.",
  "author": {
    "name": "Example team"
  },
  "apps": "./.app.json",
  "interface": {
    "displayName": "Team tools",
    "shortDescription": "Use approved team tools",
    "longDescription": "Connect to the team's existing app.",
    "developerName": "Example team",
    "category": "Productivity",
    "capabilities": ["Read"]
  }
}

请按以下目录结构放置文件：

```text
team-plugins/
├── .agents/plugins/marketplace.json
└── plugins/team-tools/
    ├── .codex-plugin/plugin.json
    └── .app.json

该引用不会创建应用或授予权限。管理员必须让目标角色可以使用该应用，成员也必须完成所需的身份验证。现有的应用权限、操作控制和服务访问规则仍然适用。

## 保持插件为最新版本

新市场每天检查更新。打开 **管理** \> **插件** \> **市场**，选中该市场，然后选择 **立即同步** ，即可请求更新，无需等待自动同步。

同步可以添加新的市场条目并更新现有插件。合并代码仓库变更之前，请先审查这些变更，因为自动同步会导入所有新增插件。

同步后，请检查状态和已保存的报告。 **已完成，N 个错误** 表示本轮同步已结束，但部分插件未能处理。如果现有插件的更新无效，会保留其最近一个可用版本。请在 GitHub 中修复报告中的问题，然后选择 **立即同步** 重试。

从代码仓库中移除条目不会删除已导入工作空间的副本。该副本会被标记为 **源中已不存在**。在 ChatGPT 中删除市场会删除从该市场导入的所有插件。

## 重新连接 GitHub 或更改访问授权

要 **重新建立 GitHub 访问连接**，请先确认用于导入的 GitHub 账户仍有权访问该代码仓库及其引用的所有代码仓库。随后，最初导入该市场的管理员应在 ChatGPT 中打开 GitHub 插件，重新连接自己的账户，因为市场同步使用的是该管理员的 GitHub 连接。

要 **转移给新所有者**，新的工作空间管理员应打开 **管理** \> **插件** \> **添加** \> **导入市场** ，使用相同的 **来源**、 **路径**和 **分支、标签或提交** 值导入同一个市场。后续同步将使用新管理员的 GitHub 连接。

不要仅为重新连接或更改所有者而删除市场，因为删除市场也会移除从中导入的插件。
