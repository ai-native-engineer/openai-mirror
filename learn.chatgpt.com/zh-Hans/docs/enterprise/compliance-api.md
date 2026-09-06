<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/compliance-api -->

对于需要可审计记录的安全、法务、治理和调查工作流，请使用合规 API。
请使用分析数据而非合规记录来衡量采用情况和趋势。

[管理员 API 参考](https://chatgpt.com/public/admin/api-reference)
是当前访问要求、事件覆盖范围、路由、
模式、筛选器、保留机制和请求行为的权威依据。

如需了解可用的合规功能和常见的集成模式，
请参阅[合规平台指南](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)。

## 何时使用合规 API

如果您需要执行以下操作，适合使用合规 API：

- 将受支持的记录导出到审计或调查系统中。
- 执行组织的记录保留和法律保全流程。
- 将 Codex 活动与其他安全或身份数据关联起来。
- 支持经批准的安全、法务或治理调查。

它不是工作效率仪表板。请勿用它推断代码质量或
个人绩效。如需生成采用情况报告，请使用[工作空间分析](/zh-Hans/codex/enterprise/workspace-analytics)
或[分析 API](/zh-Hans/codex/enterprise/analytics-api)。

## 开始使用

1. 打开[管理员 API 参考](https://chatgpt.com/public/admin/api-reference)，
   并确认您的管理员角色有权访问
   所需的合规资源。
2. 使用仅追加的合规日志流进行持续采集。
请查阅 API 参考，了解当前支持的资源和检索方式。
3. [下载日志文件](#download-logs)，并测试将其导入非生产环境中的
   安全信息和事件管理（SIEM）系统或数据湖。
4. 安排持续采集，并对导出的记录实施您所在组织的访问、保留和法律保全控制。
不要认为源系统的保留期限可以取代您所在组织的保留政策。

例如，安全团队可以将不可变的合规事件流式传输到其 SIEM 中进行调查，也可以将这些事件路由到经批准的电子证据开示工作流。
请查阅 API 参考，了解当前的路由和模式，而不要从本指南复制端点规范。

### 下载日志

下载[Bash 脚本](/downloads/compliance-api/download_compliance_files.sh)
或[PowerShell 脚本](/downloads/compliance-api/download_compliance_files.ps1)。
两种脚本都会逐页列出并下载指定时间戳之后的所有可用日志文件，
并将 JSONL 写入标准输出。错误信息写入标准错误输出。

将 `COMPLIANCE_API_KEY` 设置为您的企业合规 API 密钥。
将 `<workspace_or_org_id>` 替换为您的 ChatGPT 工作空间 ID 或 API 平台组织 ID，
将 `<after>` 替换为包含时区的 ISO 8601 时间戳。
此示例检索 `AUTH_LOG` 文件，每次检索 100 个。

在 macOS 或 Linux 上，安装 Bash、`curl` 和 `jq`，然后运行：

```bash
bash ./download_compliance_files.sh "<workspace_or_org_id>" AUTH_LOG 100 "<after>" > output.jsonl

Windows 脚本支持 PowerShell 5.1 或更高版本。请审查已下载的文件。
如果 Windows 阻止其运行，且您所在组织的执行策略允许此操作，请运行
`Unblock-File -Path .\download_compliance_files.ps1`。此示例使用
PowerShell 7 将文件保存为不带字节顺序标记的 UTF-8 格式：

```powershell
.\download_compliance_files.ps1 "<workspace_or_org_id>" AUTH_LOG 100 "<after>" |
  Set-Content -Encoding utf8NoBOM output.jsonl

## 确认管理边界

合规覆盖范围以 ChatGPT 工作空间及当前 API 参考中列出的产品为准。
平台 API 的组织数据受其自身的 API 数据和管理控制措施约束。

当前的路由、事件覆盖范围、模式、筛选器、保留行为、权限要求和请求机制，均以 API 参考为准。
本页不重复列出这些规范。

## 相关文档

- [工作空间分析](/zh-Hans/codex/enterprise/workspace-analytics)
- [管理员上线指南](/zh-Hans/codex/enterprise/admin-setup)
- [治理](/zh-Hans/codex/enterprise/governance)
- [分析 API](/zh-Hans/codex/enterprise/analytics-api)
