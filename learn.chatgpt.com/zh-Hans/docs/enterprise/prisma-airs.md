<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/prisma-airs -->

连接 Palo Alto Networks Prisma AIRS，以在
Codex 提示到达模型之前对其应用您的安全策略。工作空间管理员只需为所属工作空间配置一次
此集成。

Prisma AIRS 可应用安全配置文件中配置的保护措施，例如
数据丢失防护、提示注入检测和恶意 URL
检测。

## 开始之前

您需要：

- 一个已启用 Prisma AIRS 访问权限的 ChatGPT 工作空间。请联系您的 OpenAI
客户团队，申请访问权限。
- 工作空间管理员权限。
- Prisma AIRS API 密钥、已配置的安全配置文件，以及
部署所用的服务端点。

## 连接 Prisma AIRS

1. 打开 [Codex 数据控制](https://chatgpt.com/codex/cloud/settings/data)，并以
   工作空间管理员身份进行操作。
2. 在 **外部防护机制** 部分中找到 **Prisma AIRS**。如果此部分
   不可用，请联系您的 OpenAI 客户团队，申请为您的工作空间启用访问权限。
3. 输入您的 **API 密钥**、**安全配置文件** 名称或 ID，以及 **端点
   URL**。
4. 选择 **强制执行模式**，并设置 **AIRS 失败时** 对应的处理方式。
5. 选择 **保存连接**。Codex 会验证连接并加密您的
   API 密钥。
6. 选择 **测试连接**，以验证已保存的配置。
7. 打开 **启用 Prisma AIRS**，即可开始扫描整个
   工作空间中的提示。

仅保存连接不会启用扫描。您还必须打开 **启用
Prisma AIRS**。

## 选择端点

请使用您的 Prisma AIRS 部署所获批的端点：

| 区域        | 端点                                                 |
| ------------- | -------------------------------------------------------- |
| 美国 | `https://service.api.aisecurity.paloaltonetworks.com`    |
| 德国       | `https://service-de.api.aisecurity.paloaltonetworks.com` |
| 印度         | `https://service-in.api.aisecurity.paloaltonetworks.com` |
| 新加坡     | `https://service-sg.api.aisecurity.paloaltonetworks.com` |

Codex 默认使用美国端点。工作空间的数据驻留
要求可能会限制您可使用的端点。

## 选择提示处理方式

**强制执行模式** 决定 Prisma AIRS 标记某条提示后如何处理：

- **阻止**：在提示到达模型之前将其阻止。这是默认设置。
- **仅发出警报**：记录检测结果，并允许继续处理该提示。

**AIRS 失败时** 决定 Prisma AIRS 不可用或
未响应时如何处理：

- **允许提示**：扫描未完成也继续处理该提示。这是默认设置。
- **阻止提示**：暂停处理该提示，直到 Prisma AIRS 能够进行扫描。

请选择 **阻止提示**，以满足您的安全策略要求：每条适用的提示
都必须获得扫描判定结果。

## 了解扫描哪些内容

Codex 会将新提交的提示文本发送到已配置的 Prisma AIRS 端点
进行检查。此检查适用于此集成涵盖的 Codex 工作流，包括 App、CLI、
IDE 扩展和云端，前提是用户通过已配置的 ChatGPT
工作空间进行身份验证。使用平台 API 密钥进行身份验证的会话不在覆盖范围内。请参阅
[强制使用登录方式或工作空间](/zh-Hans/codex/auth#enforce-a-login-method-or-workspace)
以要求使用指定的登录方式和工作空间。

Prisma AIRS 不会通过此集成扫描助手回复、工具调用、工具结果、文件
或图像。您配置的安全配置文件决定 Prisma AIRS 会检测
哪些威胁和敏感数据。

Codex 会加密您的 API 密钥，保存后绝不会再次显示。请先查阅 Palo
Alto Networks 的数据处理、保留和驻留政策，再启用
提示检查。这些政策适用于发送到 Prisma AIRS 的提示。

## 管理连接

返回 [Codex 数据控制](https://chatgpt.com/codex/cloud/settings/data)
以管理此集成：

- 选择 **测试连接**，验证您保存的 API 密钥、安全配置文件
  和端点。
- 输入新密钥并选择 **轮换 API 密钥**，替换已保存的密钥
  而不更改其他设置。
- 关闭 **启用 Prisma AIRS** 可停止扫描，同时保留已保存的
  配置。
- 选择 **断开连接**，然后确认，即可停止扫描并删除已保存的
  连接和 API 密钥。

有关更全面的工作空间设置和策略管理，请参阅
[管理员部署指南](/zh-Hans/codex/enterprise/admin-setup)，以及
[托管配置](/zh-Hans/codex/enterprise/managed-configuration)。
