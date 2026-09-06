<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/workspace-analytics -->

使用 ChatGPT 工作空间分析了解工作空间的整体采用情况。使用 Codex 分析查看专注于 Codex 的报告。使用分析 API 以编程方式获取汇总数据，并使用合规 API 获取可审计记录。

这些报告渠道不会授予产品访问权限，也不会设置运行时策略。有关管理边界，请参阅
[角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)
。

## 选择报告渠道

| 渠道                     | 用途                                                    | 契约定义来源                                                                                                         |
| --------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ChatGPT 工作空间分析 | 涵盖整个工作空间采用情况与参与度的交互式报告 | [帮助中心的工作空间分析指南](https://help.openai.com/en/articles/10875114)                               |
| Codex 分析             | 专注于 Codex 采用情况和活动的交互式报告  | 需身份验证的 [Codex 分析仪表板](https://admin.openai.com/analytics/codex)                                |
| 分析 API               | 以编程方式获取 Codex 汇总报告                      | [Codex 分析 API 参考](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics) |
| 合规 API              | 审计、安全、法务和调查记录             | [Admin API 参考](https://chatgpt.com/public/admin/api-reference)                                              |

## 审查 ChatGPT 工作空间分析

ChatGPT 工作空间分析提供交互式视图，展示受支持工作空间功能的采用情况和
参与度。可用性、角色、仪表板版块、
数据时效性、隐私处理方式和导出格式均可能变化。请参阅
[ChatGPT Enterprise 和 Edu 的工作空间分析](https://help.openai.com/en/articles/10875114)
，了解当前的涵盖范围和操作流程。

请将下载的报告作为可识别身份的组织数据处理。遵循组织的访问、存储和保留政策，不要假定导出数据与汇总仪表板具有相同的隐私特性。

## 审查 Codex 分析

需身份验证的 [Codex 分析仪表板](https://admin.openai.com/analytics/codex)
专注于 Codex 报告。请将其用于交互式探索，不要将其视为稳定的
模式契约。仪表板的类别、字段、筛选条件和导出格式可能会
发生变化，而本页面不一定同步更新。

如需自动生成报告，请使用[分析 API](/zh-Hans/codex/enterprise/analytics-api)
，并遵循其 API 参考文档。如需可审计记录，请使用
[合规 API](/zh-Hans/codex/enterprise/compliance-api)。

## 解读报告数据

请注意以下边界：

- ChatGPT 工作空间分析与 Codex 分析涵盖的产品范围不同。
- 汇总分析数据和审计记录用途不同，且各有独立的契约。
- 分析数据描述活动情况；它不会授予访问权限，也不会更改运行时权限。
- [ChatGPT 用量限制和支出控制](/zh-Hans/codex/enterprise/usage-limits)是
  一项独立的工作空间限制，具体取决于套餐。
