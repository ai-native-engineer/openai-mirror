<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/governance -->

Codex 活动的治理涵盖交互式分析、程序化报告、相关的 ChatGPT 用量控制和审计记录。请选择与问题相匹配的入口；分析数据和合规数据各有不同的用途。

<a id="governance-and-observability"></a>
<a id="ways-to-track-codex-usage"></a>

| 如果您需要                                          | 首先使用                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------- |
| 了解 ChatGPT 的整体采用情况                      | [工作空间分析](/zh-Hans/codex/enterprise/workspace-analytics)              |
| 以交互方式查看 Codex 的采用情况和活动        | [Codex 分析](#analytics-dashboard)                                   |
| 将汇总的 Codex 报告数据加载到另一个系统     | [分析 API](/zh-Hans/codex/enterprise/analytics-api)                          |
| 导出记录以供审计或调查               | [合规 API](/zh-Hans/codex/enterprise/compliance-api)                        |
| 查看因套餐而异的 ChatGPT 工作空间额度控制 | [ChatGPT 用量限制和支出控制](/zh-Hans/codex/enterprise/usage-limits) |

## 打开管理入口

- 打开[工作空间分析](https://chatgpt.com/admin/usage)，
  以交互方式查看工作空间报告。[工作空间分析指南](https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu)
  介绍了当前的角色和视图。
- 如果您需要按计划以编程方式生成报告，
  请打开[Codex 分析 API 参考](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)。
- 打开[管理 API 参考](https://chatgpt.com/public/admin/api-reference)
  和[合规平台指南](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)，
  以便为审计和调查工作进行集成。

例如，使用工作空间分析快速查看采用情况，使用分析 API 将汇总的 Codex 报告数据加载到商业智能系统，并使用合规 API 将可供审计的记录发送到 SIEM 或电子证据开示工作流。

## 分析仪表板

<a id="dashboard-views"></a>
<a id="data-export"></a>

ChatGPT 提供覆盖整个工作空间的分析，用于了解整体采用情况和参与度。Codex 分析侧重于 Codex 活动。两者都是交互式报告界面，并非原始审计日志。

参阅[工作空间分析](/zh-Hans/codex/enterprise/workspace-analytics)，
比较这两种分析体验，并查找由各自负责人维护的现行参考资料。您也可以
直接打开[工作空间分析](https://chatgpt.com/admin/usage)。请勿
将仪表板标签或下载报告中的字段
作为长期稳定的报告规范；这些内容可能会随产品演进而变化。

## 相关 ChatGPT 用量控制

ChatGPT 工作空间用量控制与分析相互独立，也不用于配置功能使用权限。根据套餐的不同，符合条件的 Codex 活动可能会消耗 ChatGPT 工作空间额度；达到用量上限时，对符合条件的功能的访问可能会暂停。这些控制不会为 Codex 设置统一限额，也不管理平台 API 的计费。

请参阅[ChatGPT 用量限制和支出控制](/zh-Hans/codex/enterprise/usage-limits)，
了解长期适用的范围划分及当前的帮助中心参考资料。

## 分析 API

<a id="what-it-measures"></a>
<a id="endpoints"></a>
<a id="usage"></a>
<a id="code-review-activity"></a>
<a id="user-engagement-with-code-review"></a>
<a id="how-it-works"></a>
<a id="common-use-cases"></a>

使用分析 API，以编程方式获取汇总的 Codex 报告数据。该 API 适用于数据仓库、商业智能系统，以及不应依赖交互式仪表板的内部报告。

API 参考是访问要求、路由、模式、
字段、报告时间窗口和分页信息的权威来源。请参阅
[分析 API](/zh-Hans/codex/enterprise/analytics-api)，了解概念层面的集成边界，
并获取权威参考链接。

## 合规 API

<a id="what-it-measures-1"></a>
<a id="what-you-can-export"></a>
<a id="activity-logs"></a>
<a id="metadata-for-audit-and-investigation"></a>
<a id="common-use-cases-1"></a>
<a id="what-it-does-not-provide"></a>

对于需要可供审计的记录的安全、法律和治理工作流，请使用合规 API。它不是用于查看采用情况或生产力的仪表板。

API 参考是事件覆盖范围、模式、权限、
筛选条件、保留期限和请求行为的权威来源。请参阅
[合规 API](/zh-Hans/codex/enterprise/compliance-api)，了解概念层面的集成边界，
并获取权威参考链接。

<a id="recommended-pattern"></a>

如需了解这些入口的上线顺序和验证方法，请参阅
[管理员上线指南](/zh-Hans/codex/enterprise/admin-setup)。

## 相关文档

- [管理员上线指南](/zh-Hans/codex/enterprise/admin-setup)
- [工作空间分析](/zh-Hans/codex/enterprise/workspace-analytics)
- [分析 API](/zh-Hans/codex/enterprise/analytics-api)
- [合规 API](/zh-Hans/codex/enterprise/compliance-api)
