<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/service-accounts -->

服务账户让您无需依赖员工账户，即可在整个组织中运行和扩展无头 Codex 工作流。每个持续集成（CI）运行器、定时作业或共享集成都拥有独立的 ChatGPT 工作空间身份，并具备与人员账户相同的群组、角色、访问控制和审计能力。

只有工作空间所有者和管理员可以创建服务账户。他们可以授权其他个人或群组管理账户、配置插件或创建访问令牌。

服务账户仅适用于按用量付费套餐。

服务账户代表工作空间中的非人员身份。[个人访问令牌](/zh-Hans/codex/enterprise/access-tokens)代表创建该令牌的工作空间成员。API 平台的项目服务账户和 API 密钥使用独立的项目访问权限和计费方式。

## 创建并设置服务账户

本交互式演示以 GitHub 为例，介绍如何创建账户、配置插件、创建令牌以及分配群组和角色。

1. 在您的工作空间设置中打开[服务账户](https://chatgpt.com/admin/service-accounts)。
2. 选择加号（**+**）按钮，并输入一个能说明用途的名称，例如 `release-automation`。
3. 选择 **创建**。

## 连接插件

请为服务账户单独配置插件。服务账户不会继承创建者的插件或已连接的应用。

1. 打开该账户的 **插件** 部分，然后选择 **添加插件**。
2. 选择一个插件，并确认其显示为已配置或已启用。

**配置者** 和 **管理者** 角色可以配置插件， **用户** 角色则不可以。

## 创建访问令牌

在服务账户的详情页面创建令牌。该令牌代表服务账户，而非创建令牌的人员。

1. 打开该账户，在 **访问令牌**中选择 **创建令牌** 。
2. 为令牌命名，确认 **Codex** 权限范围，并选择有效期。
3. 选择 **创建** ，并将令牌保存到您的密钥管理器中。

完整令牌仅显示一次。可选择的有效期由工作空间策略决定。

## 分配角色和群组

服务账户与工作空间中的个人成员一样，可以获得工作空间角色并加入群组。请直接为其分配访问权限；它不会继承创建者的权限。

若要让人员或群组管理该账户，请选择 **共享**，然后选择 **添加人员或群组**，并分配角色：

| 共享账户角色 | 配置账户及其插件 | 创建服务账户访问令牌 |
| ------------------- | ------------------------------------- | ------------------------------------ |
| **用户**            | 否                                    | 是                                  |
| **配置者**       | 是                                   | 否                                   |
| **管理者**         | 是                                   | 是                                  |

这些角色适用于管理该账户的人员，与分配给服务账户的工作空间角色和群组相互独立。

**配置者** 和 **管理者** 可以启用或停用账户。只有工作空间所有者和管理员可以创建、删除或共享账户。操作人员使用自己的 ChatGPT 账户登录后管理共享账户。

有关工作空间权限的更多信息，请参阅[角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)。

## 无需登录即可运行 Codex

服务账户访问令牌需要 `0.142.0` 或更高版本的 Codex CLI。设置 `CODEX_ACCESS_TOKEN` 后，无需打开浏览器即可运行 Codex：

```bash

codex exec --json "Inspect this repository and summarize its current state."

在 CI 中，请通过密钥管理器或运行器密钥提供令牌。

如需在受信任的计算机上保存登录信息，请通过标准输入传入令牌：

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "Summarize the changes in the current branch."

此操作会将凭据保存在本地。在共享或临时运行器上，请使用 `CODEX_ACCESS_TOKEN`，不要保存登录信息。

## 使用 SCIM 预配服务账户

如果您的工作空间支持通过跨域身份管理系统（SCIM）协议预配服务账户，请在身份提供商中将 `userType` 设置为 `ServiceAccount`：

```json
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "userName": "svc-codex-release@company.example",
  "displayName": "Codex release automation",
  "active": true,
  "userType": "ServiceAccount"
}

将该身份分配给工作空间和所需群组，然后进行同步。身份提供商负责管理该账户的名称、所属群组和生命周期。由 SCIM 管理的账户无法在 ChatGPT 中重命名或删除。请参阅[群组与预配](/zh-Hans/codex/enterprise/groups-and-provisioning)。

## 使用 Admin API 管理服务账户

如果您的工作空间有访问权限，请使用 ChatGPT Admin API 密钥管理账户、令牌和共享权限。读取操作需要 `chatgpt.enterprise.service_account.read`；修改操作需要 `chatgpt.enterprise.service_account.write`。服务账户令牌不能用于对 Admin API 请求进行身份验证。

请查阅 [Admin API 参考](https://chatgpt.com/public/admin/api-reference)，了解可用操作和当前请求路径。

### 账户

| 操作                    | 方法   | 功能                               |
| ---------------------------- | -------- | ------------------------------------------ |
| 列出账户                | `GET`    | 返回工作空间的服务账户         |
| 创建账户            | `POST`   | 创建具有指定名称的服务账户            |
| 获取账户               | `GET`    | 返回一个服务账户                |
| 启用或停用账户 | `PATCH`  | 更新账户的 `enabled` 值      |
| 删除账户            | `DELETE` | 移除账户并撤销其令牌 |

使用 `POST /v1/manage/workspaces/{workspace_id}/service-accounts` 创建账户。更新账户时只能修改 `enabled`。

### 令牌

| 操作      | 方法   | 功能                         |
| -------------- | -------- | ------------------------------------ |
| 列出令牌    | `GET`    | 返回账户的令牌元数据 |
| 创建令牌 | `POST`   | 创建具有指定作用域的访问令牌        |
| 撤销令牌 | `DELETE` | 永久撤销一个令牌        |

例如，创建一个 30 天后过期的 Codex 令牌：

```json
{
  "name": "production-release-runner",
  "ttl": 2592000,
  "scopes": ["chatgpt.workspace.feature.allow-codex-local-access.access"]
}

`ttl` 表示令牌的有效期，单位为秒。若设置了有限的有效期，则必须少于一年，并符合您的工作空间的到期策略。完整的 `access_token` 仅在创建令牌时返回。

Admin API 还可以列出、添加、更新和移除共享账户的访问权限。其角色值为 `manager`、`configurer` 和 `user`；其中 `configurer` 在 ChatGPT 中显示为 **配置** 。

## 保护和管理服务账户

- 仅授予工作流程所需的角色、群组、插件和连接。
- 将令牌存储在密钥管理器中，并使用受信任的运行器。
- 切勿将凭证写入日志、聊天消息或源代码管理系统。
- 设置有限的有效期，并定期审查账户访问权限和活动。
- 轮换令牌时，请创建替代令牌、更新工作流程并验证访问权限，然后在工作空间中或通过 Admin API 撤销旧令牌。
- 立即撤销已泄露的令牌，并调查账户近期的活动。
- 在工作空间中或通过 Admin API 停用或删除不再使用的账户。这两项操作都会撤销所有有效令牌。已停用的账户可重新启用，但需使用新令牌；删除操作无法撤销。

运行活动均记在服务账户名下。可用的工作空间分析和审计记录还可用于确定是谁创建了令牌或更改了账户设置。请在 [Admin API 参考](https://chatgpt.com/public/admin/api-reference)中确认事件覆盖范围。

## 相关文档

- [身份验证](/zh-Hans/codex/auth)
- [个人访问令牌](/zh-Hans/codex/enterprise/access-tokens)
- [角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)
- [群组与预配](/zh-Hans/codex/enterprise/groups-and-provisioning)
- [治理](/zh-Hans/codex/enterprise/governance)
- [合规 API 和审计事件](/zh-Hans/codex/enterprise/compliance-api)
- [非交互模式](/zh-Hans/codex/non-interactive-mode)
