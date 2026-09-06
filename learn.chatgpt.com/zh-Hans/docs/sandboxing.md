<!-- source: https://learn.chatgpt.com/zh-Hans/docs/sandboxing -->

沙盒为智能体设定边界，使其能够自主执行操作，同时不会让它
不受限制地访问您的计算机。当本地聊天在
**ChatGPT 桌面应用**、 **Codex CLI** 或 **IDE 扩展**中运行命令时，这些命令会在
受限环境中运行，而非默认获得完全访问权限。

该环境规定智能体可自主执行哪些操作，例如可以修改哪些文件、
命令能否访问网络。只要任务未超出这些边界，智能体就能持续执行，
无需停下来请求确认；当任务需要超出边界时，
则进入审批流程。

  沙盒与审批是两种相互配合的控制机制。
沙盒负责设定技术边界；审批策略则决定智能体
何时必须在越过边界前暂停并请求审批。

## 沙盒的作用

沙盒不仅适用于内置文件
操作，也适用于启动的命令。如果智能体运行 `git`、软件包管理器或测试运行器，
这些命令也会受到相同的沙盒边界约束。

Codex 在每个操作系统上都采用平台原生的强制执行机制。macOS、
Linux、WSL2 和原生 Windows 的实现方式各不相同，但各个界面的
核心理念一致：为智能体提供边界明确的工作环境，让常规任务能够在
清晰的限制范围内自主运行。

## 为何重要

沙盒可以减少审批疲劳。智能体无需请求您确认每一条
低风险命令，即可在您已批准的边界内读取文件、编辑文件并运行
常规项目命令。

沙盒还为智能体执行任务提供了更清晰的信任模型。您不仅
信任智能体的意图，也确信它会在强制执行的限制范围内
运行。这让您能够更放心地让智能体独立工作，同时清楚
它会在何时暂停并请求帮助。

## 入门

默认权限模式会自动启用沙盒。

### 前提条件

在 **macOS** 上，沙盒使用系统内置的 Seatbelt
框架，无需额外配置即可使用。

在 **Windows** 上，如果在 PowerShell 中运行，Codex 会使用原生 [Windows
沙盒](/zh-Hans/codex/windows/windows-sandbox#windows-sandbox)；如果在 WSL2 中运行，则使用
Linux 沙盒实现。

在 **Linux 和 WSL2** 上，请先使用软件包管理器安装 `bubblewrap`：

  <div slot="ubuntu-debian">

```bash
sudo apt install bubblewrap

  </div>

  <div slot="fedora">

```bash
sudo dnf install bubblewrap

  </div>

Codex 使用找到的第一个 `bwrap` 可执行文件，查找范围为 `PATH`。如果没有可用的 `bwrap`
可执行文件，Codex 会改用随附的辅助程序，但该辅助程序
要求系统支持创建非特权用户命名空间。安装
提供 `bwrap` 的发行版软件包，可确保此配置稳定运行。

如果缺少 `bwrap`，或者辅助程序
无法创建所需的用户命名空间，Codex 会在启动时显示警告。对于通过此项
AppArmor 设置施加限制的发行版，建议优先加载 `bwrap` 的 AppArmor 配置文件，使 `bwrap`
能够继续运行，而无需在全局禁用该限制。

  **Ubuntu AppArmor 注意事项：** 在 Ubuntu 25.04 上，从 Ubuntu 软件包仓库安装 `bubblewrap` 后，
  应无需额外配置 AppArmor 即可正常使用。
`bwrap-userns-restrict` 配置文件包含在 `apparmor` 软件包中，位于
`/etc/apparmor.d/bwrap-userns-restrict`。

在 Ubuntu 24.04 上，即使已安装 `bubblewrap`，Codex 仍可能警告无法创建所需的用户
命名空间。请复制并加载额外的配置文件：

```bash
sudo apt update
sudo apt install apparmor-profiles apparmor-utils
sudo install -m 0644 \
  /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
  /etc/apparmor.d/bwrap-userns-restrict
sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict

`apparmor_parser -r` 可以将配置文件加载到内核中，无需重启系统。您
也可以重新加载所有 AppArmor 配置文件：

```bash
sudo systemctl reload apparmor.service

如果该配置文件不可用或未能解决问题，您可以使用以下命令禁用
AppArmor 对非特权用户命名空间的限制：

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

## 权限的工作原理

请使用当前界面的权限控件，调整 Codex 处理本地
操作的方式。

审批决定 Codex 何时在执行操作前暂停；沙盒则决定
命令可以访问哪些文件和网络资源。如果审批提供不同的授权范围，
例如仅批准一次或在整个会话期间有效，请选择能让任务继续进行的
最小授权范围。默认情况下应保持项目
边界；请使用单独的项目或工作树，而不要
将访问范围扩大到无关的代码仓库。

ChatGPT Work 在受管理的隔离环境中运行代码和 Shell 命令。
工作空间策略和各工具的专用控制设置决定哪些能力
可用。如果可以使用该设置，请通过 **设置 \> 数据控制 \> Work
网络访问** 管理代码和 Shell 命令的网络访问权限。开启
**允许访问公共互联网** 后，这些命令即可访问公共
互联网。关闭后，命令只能访问
受管理的允许列表中必需的主机名。

网页搜索、插件和远程浏览器分别有独立的控制设置。
更改会在当前代码或 Shell 命令运行结束，并且 Work
刷新执行环境后生效。ChatGPT 网页版不提供本地
Codex 沙盒或审批模式选择器。

在 ChatGPT 桌面应用中，请使用编辑器下方的权限控件。
根据您的配置，菜单可能包括 **请求审批**、
**替我审批** （适用于符合条件的审批请求）、 **完全访问权限**，以及已命名或
自定义的权限配置方案。

在 CLI 中，输入
[`/permissions`](/codex/developer-commands?surface=cli#cli-update-permissions-with-permissions)
即可打开权限选择器，并更改当前生效的权限配置方案。

在 IDE 扩展中，请使用编辑器下方的权限控件。
根据您的配置，菜单可能包括 **请求审批**、
**替我审批** （适用于符合条件的审批请求）、 **完全访问权限**，以及已命名或
自定义的权限配置方案。

<div class="not-prose my-8 max-w-[18rem] mr-auto">
  
    
      
    
  
</div>

<a id="configure-defaults"></a>

## 配置默认值

为确保每次启动时行为一致，请在 `config.toml` 中设置默认值。
[基础配置](/zh-Hans/codex/config-file/config-basic)介绍了其工作原理，
[配置参考资料](/zh-Hans/codex/config-file/config-reference)列出了以下确切的配置键：
`sandbox_mode`、`approval_policy`、`approvals_reviewer` 和
`sandbox_workspace_write.writable_roots`。通过这些设置，您可以决定智能体默认拥有多少
自主权、可以写入哪些目录、何时需要
暂停请求审批，以及由谁审查符合条件的审批请求。

常见的沙盒模式大致如下：

- `read-only`：智能体可以查看文件，但未经审批，不能编辑文件或运行
  命令。
- `workspace-write`：智能体可以读取文件、在工作空间内编辑文件，并在该边界内运行
  常规本地命令。这是可让本地
  工作更顺畅的默认模式。
- `danger-full-access`：智能体运行时不受沙盒限制，这会移除
  文件系统和网络边界。仅当您希望智能体拥有
  完全访问权限时，才应使用此模式。

常见的审批策略如下：

- `untrusted`：智能体在运行不属于其可信
  命令集的命令前，会先请求审批。
- `on-request`：智能体默认在沙盒内运行，并在
  需要超出该边界时请求审批。
- `never`：智能体不会因审批提示而暂停。

当审批需要交互时，您还可以通过
`approvals_reviewer` 指定由谁进行审查：

- `user`：审批提示会显示给用户。这是默认设置。
- `auto_review`：符合条件的审批提示会转交审查智能体处理（请参阅
[自动审查](/zh-Hans/codex/sandboxing/auto-review)）。

完全访问权限是指同时使用 `sandbox_mode = "danger-full-access"` 和
`approval_policy = "never"`。相比之下，风险较低的本地自动化
预设会同时使用 `sandbox_mode = "workspace-write"` 和
`approval_policy = "on-request"`，或使用对应的 CLI 标志
`--sandbox workspace-write --ask-for-approval on-request`。之后，您可以保留
`approvals_reviewer = "user"`，以进行手动审批；也可以设置
`approvals_reviewer = "auto_review"`，以自动审查审批请求。

如果需要智能体跨多个目录工作，您可以使用可写根目录
扩展其可修改的范围，而无需完全移除沙盒。如果
需要更宽或更窄的信任边界，请调整默认沙盒模式
和审批策略，而不要依赖一次性例外。

如果工作流程需要特定例外，请使用[规则](/zh-Hans/codex/agent-configuration/rules)。通过规则，您可以
对沙盒外的命令前缀设置允许、提示确认或禁止，这通常
比大范围扩大访问权限更合适。有关 IDE 专用设置的
入口，请参阅 [Codex IDE 扩展设置](/codex/developer-settings?surface=ide)。

自动审查功能可用时，也不会改变沙盒边界。它是
处理该边界处审批请求时可选的一种 `approvals_reviewer`，例如
沙盒权限提升、被阻止的网络访问，或产生副作用且
仍需审批的工具调用。沙盒内已获允许的操作会运行，
无需额外审查。有关审查者的生命周期、触发类型、拒绝
语义和配置详情，请参阅
[自动审查](/zh-Hans/codex/sandboxing/auto-review)。

各平台的详细信息请参阅对应的平台文档。有关原生 Windows 的设置、
运行行为和故障排除，请参阅 [Windows](/zh-Hans/codex/windows/windows-sandbox)。有关管理员
要求，以及组织层面对沙盒和审批的限制，请参阅
[智能体审批与安全](/zh-Hans/codex/agent-approvals-security)。
