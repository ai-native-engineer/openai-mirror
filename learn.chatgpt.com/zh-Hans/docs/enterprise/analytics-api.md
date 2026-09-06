<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/analytics-api -->

Codex 分析 API 为 ChatGPT 工作空间提供
汇总的 Codex 使用情况和活动指标。

[Codex 分析 API 参考](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)
是当前访问要求、路由、请求和响应模式、
指标、时间语义及分页的权威依据。

## 何时使用分析 API

当您需要执行以下操作时，适合使用分析 API：

- 实现 Codex 定期报告的自动化。
- 将汇总的 Codex 指标与组织内部数据关联起来。
- 为获准的受众构建受控的报告层。
- 避免将集成与交互式仪表板耦合。

它不是原始审计日志接口。
如果工作流程需要可审计的活动记录，
请使用 [合规 API](/zh-Hans/codex/enterprise/compliance-api)。

## 确认管理边界

分析 API 返回的结果仅涵盖一个 ChatGPT 工作空间，但请求需使用
平台组织的 API 密钥进行身份验证。该密钥所属的组织必须
与该工作空间关联的组织一致。

API 参考规定了当前的密钥发放方式、作用域要求、
路由、模式、字段、时间语义和分页行为。
本页面不重复说明这些接口约定。

## 相关文档

- [工作空间分析](/zh-Hans/codex/enterprise/workspace-analytics)
- [管理员上线指南](/zh-Hans/codex/enterprise/admin-setup)
- [治理](/zh-Hans/codex/enterprise/governance)
- [合规 API](/zh-Hans/codex/enterprise/compliance-api)
