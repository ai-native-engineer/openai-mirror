<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/plugin/export-findings -->

可将已完成的 Codex Security 扫描用于以下任一种交接方式：

- **导出** 会创建可移植的 JSON、CSV 或 SARIF 文件。
- **跟踪发现项** 会将选定的发现项整理为 Linear 问题、GitHub 议题或 Jira
  问题，也可以整理为一份私有 GitHub 安全公告草稿。Codex 会检查
  重复项，并在写入前等待您的审批。

这两种工作流都不会更改已封存的扫描包。

  可用的工件链接和导出格式取决于您使用的 Codex 界面和
  已安装的插件版本。请先查看 [插件
  更新日志](/zh-Hans/codex/security/plugin/changelog)，再将某种格式用于
  自动化。

## 导出可移植工件

在桌面 App 中，从 **安全** \> **扫描** 打开已完成的扫描。使用其
可用的工件链接查看 `report.md`、`findings.json`、
`scan-manifest.json`、`coverage.json` 或 SARIF 报告（如有）。

若要创建其他受支持的格式，请让 Codex 在不修改已封存扫描包的情况下，
从已完成的扫描中导出发现项：

```text
Export the findings from [completed scan directory] as [JSON, CSV, or SARIF]. Do not modify the sealed scan bundle or upload its contents.

选择适合目标位置的格式：

| 格式 | 用途                                                        |
| ------ | ----------------------------------------------------------------- |
| JSON   | 保留已封存的结构化发现项，供工具和脚本使用。    |
| CSV    | 在电子表格中审查发现项以及当前的本地分类处置状态。  |
| SARIF  | 将发现项发送至支持 SARIF 交换格式的工具。 |

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    从已完成的扫描中打开覆盖范围、发现项、扫描清单、Markdown 报告或 SARIF
工件。
  </figcaption>
</figure>

选择 **Markdown 报告** 以打开 `report.md`，系统将使用您配置的外部
编辑器。具体使用哪个编辑器取决于您的系统设置；以下示例显示了
生成的报告内容。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    在生成的 Markdown 报告中，审查扫描范围、威胁模型、经过验证的发现项和详细报告
链接。
  </figcaption>
</figure>

使用返回的工件路径。如果其他工具需要完整的扫描
上下文，请一并保留原始 `scan-manifest.json`、`findings.json` 和
`coverage.json`。导出操作不会将发现项上传到代码扫描
服务。

## 跟踪选定的发现项

运行 `$codex-security:track-findings`，并指定一项经过验证的发现项，或
从同一个已封存扫描中明确选定的一批发现项（最多 25 项）。每次
运行仅使用一个提供商和一个目标位置。私有 GitHub 安全公告
草稿仅接受一项发现项。

要准备 Linear 问题，请发送：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for the Linear team [team] and project [project, if
any]. Check for duplicates and show me the exact issue title, body, metadata,
and destination. Do not create or update anything until I approve that payload.

要准备 GitHub 议题，请发送：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for GitHub repository [owner/repository]. Check open
and closed issues for duplicates and show me the exact issue title, body,
metadata, repository visibility, and authenticated transport. Do not create or
update anything until I approve that payload.

要准备 Jira 问题，请发送：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for Jira project [project key] as [issue type].
Check for duplicates and show me the exact issue summary, description,
metadata, and destination. Do not create or update anything until I approve
that payload.

在 Codex 中跟踪 Jira 问题需要 Atlassian Rovo 插件。复用现有问题
需要读取权限；创建或更新问题需要读取和写入权限。

要准备私有 GitHub 安全公告草稿，请发送：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] as a private draft GitHub Security Advisory in
[owner/repository]. Verify the sealed source revision, repository, affected
paths, package metadata, and duplicate state. Show me the exact advisory
payload, authenticated GitHub CLI identity, and disclosure warnings. Do not
create anything until I approve that payload.

  创建安全公告草稿需要一项来自已封存的 `git_revision` 扫描的发现项、
  经验证的公开权威源代码仓库，以及管理员访问权限。此
  工作流不支持批量操作，也不会更新、发布或关闭安全公告。如果源代码仓库不符合这些要求，请使用已获批准的
  私有问题目标位置。

## 审查拟写入内容

1. 确认发现项 ID 和指纹来自您预期的已封存扫描。
2. 确认提供商、确切的 Linear 团队、GitHub 代码仓库、Jira 项目或
安全公告代码仓库，并确认目标位置当前的可见性。
3. 审查重复项检查结果： `create`、`reuse`、`update` 或 `blocked`。
4. 完整阅读拟写入的标题、正文、源代码位置和提供商
元数据。移除不应在目标位置公开的漏洞利用细节或
内部证据。
5. 只批准这份确切的写入内容。若目标位置、可见性、发现项
集合或正文有任何变化，都需要重新预览。

敏感发现项应发送到私有目标位置。在内部或公开的
GitHub 代码仓库中创建议题时，必须明确提示其可见性
并对完整内容进行审批。应将安全公告草稿的描述视为
最终会公开的内容，并在批准前移除凭据、私有证据和不必要的
漏洞利用细节。

在 Codex 对话中审查并批准外部操作。审批
不会在安全工作台中创建单独的问题或安全公告界面。

## 验证跟踪项

您批准拟写入内容后，Codex 会重新检查已封存源、
目标位置、访问权限和重复项状态。对于批量操作，它会逐项处理发现项，
并在遇到第一个无法确定的结果时停止。只有 Codex 回读确切的问题并验证其
绑定标识符和内容后，创建、更新或
复用才算完成。

将返回的问题或安全公告的规范 URL 与您的分类处置记录一并保存。
继续执行 [修复并验证发现项](/zh-Hans/codex/security/plugin/fix-findings)，前提是
负责人已接受该项并安排修复。
