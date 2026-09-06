<!-- source: https://learn.chatgpt.com/zh-Hans/docs/pricing -->

<strong>ChatGPT Work 和 Codex 共享用量。</strong>在 ChatGPT 中使用
  ChatGPT Work 时，其定价、额度和用量上限与 Codex 相同。

<h2 class="sr-only">定价选项</h2>

  <div data-content-switcher-pane data-value="individual">
    <div class="codex-pricing-grid">
      
      
      
        - 可通过 Web、CLI、IDE 扩展和 iOS 使用 Codex
        - 自动代码审查和 Slack 集成等云端集成功能
        - GPT-5.6 模型系列，包括 Sol、Terra 和 Luna
        - 使用 GPT-5.6 Luna 处理较轻量或大批量工作负载时，可获得更高的用量上限
        - 使用 [ChatGPT 额度](#credits-overview)灵活扩展用量
        - Plus 套餐包含的其他
          [ChatGPT 功能](https://chatgpt.com/pricing)
      
      
        - 可使用 GPT-5.3-Codex-Spark（研究预览版），这是一款适用于日常编程任务的快速 Codex 模型
        - Codex 用量是 Plus 的 5 倍或 20 倍\*
        - 每月 $200 的档位可无限使用 ChatGPT 语音；任务仍会消耗您的 Codex 用量预算
        - Pro 套餐包含的其他
          [ChatGPT 功能](https://chatgpt.com/pricing)
      
      
        - 可在 CLI、SDK 或 IDE 扩展中使用 Codex
        - 不提供云端功能（如 GitHub 代码审查、Slack 等）
        - 可用模型取决于您的密钥能够访问哪些 API 模型
        - 根据 [API 定价](/api/docs/pricing)支付 Codex 使用费用
      
    </div>

  </div>

  <div data-content-switcher-pane data-value="business-enterprise" hidden>
    <div class="codex-pricing-grid">
      
        - 可在桌面和移动应用中使用 ChatGPT 和 Codex
        - 使用更大规格的虚拟机，加快云端聊天的运行速度
        - 使用 [ChatGPT 额度](#credits-overview)灵活扩展用量
        - 安全的专用工作空间，提供必要的管理控制功能、SAML SSO 和 MFA
        - 默认不使用您的业务数据进行训练。[了解
          更多](https://openai.com/business-data/)
        - Business 套餐包含的其他
          [ChatGPT 功能](https://chatgpt.com/pricing)
      
      
        - 优先处理请求
        - 企业级安全与控制功能，包括 SCIM、EKM、
          用户分析、域名验证和基于角色的访问控制
          （[RBAC](https://help.openai.com/en/articles/11750701-rbac)）
        - 通过[合规
          API](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Tasks)查看审计日志并监控使用情况
        - 数据保留和数据驻留控制
        - 企业方案包含的其他
          [ChatGPT 功能](https://chatgpt.com/pricing)
      
    </div>

    <div class="mt-8 mb-10 codex-pricing-grid">
      
        - 在 CLI、SDK 或 IDE 扩展中使用 Codex
        - 不提供云端功能（GitHub 代码审查、Slack 等）
        - 可用模型取决于您的密钥可访问的 API 模型
        - 按 [API 定价](/api/docs/pricing)支付 Codex 使用费用
      
    </div>

  </div>

## 邀请朋友和同事

符合条件的用户可以通过应用左下角的个人资料菜单发送 Codex 邀请。
如果您使用的是符合条件的个人方案，请选择 **邀请朋友** ；
如果您使用的是符合条件的 Business 工作空间，请选择 **邀请同事** 。
然后输入收件人的电子邮件地址并发送邀请。

邀请对话框会显示您所用方案或推广活动的当前奖励、受邀人资格要求、邀请上限及奖励到期时间。个人推荐计划和 Business 推荐计划采用各自的奖励和资格规则。ChatGPT Enterprise 目前不支持推荐。

2026 年 6 月 11 日至 6 月 24 日，符合条件的 Plus 和 Pro 用户最多可邀请
三位朋友。符合条件的受邀人发送第一条 Codex 消息后，双方
均会获得一次可留待以后使用的速率限制重置机会。该重置机会自发放之日起
30 天内有效。Business 推荐计划另行提供共享工作空间
额度奖励；请先查看
[现行条款](https://help.openai.com/en/articles/20001271)，再发送
邀请。

## 常见问题

### 站点的费用是多少？

公开测试期间，符合条件的 ChatGPT 方案均包含[站点](/zh-Hans/codex/sites)。
是否可用取决于您的方案、所在地区和工作空间设置。

### 我的方案有哪些使用限额？

您可以发送的消息数量取决于所用模型、任务的规模和复杂程度，以及任务是在本地还是云端运行。小型脚本或常规函数可能只会消耗一小部分使用配额，而较大的项目、长时间运行的任务，或需要智能体保留更多上下文的长时间会话，每条消息消耗的配额则会明显更多。

看似相似的任务可能会消耗不同数量的使用配额。模型选择、上下文、推理、工具使用、检索和缓存都会影响用量，因此仅凭提示长度无法可靠估算用量。

选择最适合您工作的 GPT-5.6 模型：

- **Sol** 专为最棘手的工作而设计，包括复杂推理、界定不清的问题、
  高级编程和事关重大的决策。
- **Terra** 是日常工作的主力模型，适用于生产环境任务、报告编制、
  文档分析、编程和需要良好判断力的工作。
- **Luna** 针对需要快速、大批量处理的工作进行了优化，例如路由、
  分类、提取、支持、后台自动化，
  以及目标明确的编程任务。

<div id="usage-limits">

以下估算值为每个五小时周期内可发送的本地消息数量。
ChatGPT 方案中的云端聊天使用 GPT-5.6 Sol，消耗的使用配额可能多于本地消息。
这些估算值并非固定的消息数量上限；请查看
[用量面板](#where-can-i-see-my-current-usage-limits)，了解当前限额
和重置时间。

</div>

  <thead class="whitespace-nowrap">
    <tr>
      <th scope="col">模型</th>
      <th scope="col" style="text-align:center">
        Plus
      </th>
      <th scope="col" style="text-align:center">
        Pro 5x
      </th>
      <th scope="col" style="text-align:center">
        Pro 20x
      </th>
      <th scope="col" style="text-align:center">
        标准 Business
      </th>
      <th scope="col" style="text-align:center">
        API 密钥
      </th>
    </tr>
  </thead>
  <tbody class="whitespace-nowrap">
    <tr>
      <td>GPT-6 Astra</td>
      <td style="text-align:center">5-45</td>
      <td style="text-align:center">25-225</td>
      <td style="text-align:center">100-900</td>
      <td style="text-align:center">5-45</td>
      <td style="text-align:center">
        [按用量计费](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.6 Sol</td>
      <td style="text-align:center">10-100</td>
      <td style="text-align:center">50-500</td>
      <td style="text-align:center">200-2,000</td>
      <td style="text-align:center">10-100</td>
      <td style="text-align:center">
        [按用量计费](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.6 Terra</td>
      <td style="text-align:center">25-200</td>
      <td style="text-align:center">125-1,000</td>
      <td style="text-align:center">500-4,000</td>
      <td style="text-align:center">25-200</td>
      <td style="text-align:center">
        [按用量计费](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.6 Luna</td>
      <td style="text-align:center">250-2,000</td>
      <td style="text-align:center">1,250-10,000</td>
      <td style="text-align:center">5,000-40,000</td>
      <td style="text-align:center">250-2,000</td>
      <td style="text-align:center">
        [按用量计费](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.5</td>
      <td style="text-align:center">15-80</td>
      <td style="text-align:center">75-400</td>
      <td style="text-align:center">300-1,600</td>
      <td style="text-align:center">15-80</td>
      <td style="text-align:center">
        [按用量计费](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.4</td>
      <td style="text-align:center">20-100</td>
      <td style="text-align:center">100-500</td>
      <td style="text-align:center">400-2,000</td>
      <td style="text-align:center">20-100</td>
      <td style="text-align:center">
        [按用量计费](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.4 mini</td>
      <td style="text-align:center">60-350</td>
      <td style="text-align:center">300-1,750</td>
      <td style="text-align:center">1,200-7,000</td>
      <td style="text-align:center">60-350</td>
      <td style="text-align:center">
        [按用量计费](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="6" style="text-align:center">
        本地消息和云端聊天共用您方案中的使用配额。此外还可能设有每周限额。
      </td>
    </tr>
    <tr>
      <td colspan="6" style="text-align:center">
        对于采用灵活定价的企业/Edu 方案用户，不设固定的速率限制；
        可用量随[额度](#credits-overview)增加。
      </td>
    </tr>
    <tr>
      <td colspan="6" style="text-align:center">
        不采用灵活定价的企业和 Edu 方案，其大多数功能的每席位使用限额与 Plus 相同。
      </td>
    </tr>
  </tfoot>

Business（$100）适用 Pro 5x 的估算值。

其他智能体功能的定价生效后，这些功能将共用使用限额。
目前包括 Plus 和 Pro 方案中的 [ChatGPT for
Excel](https://help.openai.com/articles/20001063)。

速度配置会增加所有适用模型的额度消耗，
因此也会更快地消耗方案内使用配额。对于支持快速模式的模型，快速模式会以更高的费率
消耗额度。有关支持的模型和费率，请参阅[速度](/zh-Hans/codex/agent-configuration/speed)。
图像生成消耗方案内使用配额的速度平均也约为通常的 3-5 倍，
具体取决于图像质量和尺寸。GPT-5.3-Codex-Spark 处于研究预览阶段，
仅向 ChatGPT Pro 用户开放，发布时尚不支持通过 API 使用。
由于它运行在专用的低延迟硬件上，因此设有单独的使用限额，
该限额可能根据需求调整。

### 桌面端的 ChatGPT 语音

桌面端的 ChatGPT 语音采用单独的使用配额，配额取决于您的方案，并按五小时滚动窗口计算。通过语音启动的任务会消耗您现有的 Codex 使用配额。当您达到其中任一限额时，ChatGPT 都会通知您。

GPT-Live 负责实时对话。当您在现有的 Codex 任务中使用语音时，
任务所选的模型会负责执行工作。有关可用性和设置方法，
请参阅 [ChatGPT 语音](/zh-Hans/codex/features/voice#start-talking)。

- **Plus：** 约 15–30 分钟
- **Pro 5x（$100/月）：** 约 1–2.5 小时
- **Pro 20x（$200/月）：** 不限量使用语音
- **Business：** 约 45 分钟
- **企业 / Edu（旧版）：** 约 45 分钟

不限量使用语音并不意味着 Codex 任务也不受限额约束。通过 ChatGPT 语音启动的任务仍会消耗您现有的 Codex 使用配额。

对于采用额度计费或按量付费的 Business、Edu 和企业工作空间，桌面端语音每分钟约消耗 6 额度。目前无法通过 API 密钥使用桌面端的 ChatGPT 语音。

### 达到使用限额后会怎样？

我们希望您能够完成已在进行的工作。如果您在某一轮任务执行期间达到使用限额，智能体仍可继续处理该轮任务，但须遵守公平使用限制。

ChatGPT Plus 和 Pro 用户达到使用限额后，可以购买额外额度来继续工作，无需升级现有方案。

采用[灵活
定价](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)的 Business、Edu 和企业方案
可以购买额外的工作空间额度以继续工作。

如果您即将达到用量限制，也可以切换到较小的模型，让剩余可用量用得更久。

所有用户也都可以使用 API 密钥进行额外的本地聊天，用量按
[标准 API 费率](https://platform.openai.com/docs/pricing)计费。

<a id="image-generation-usage-limits"></a>

### 图像生成如何计入用量限制？

图像生成与本地消息
和云端聊天共用总体用量限制。图像生成消耗方案所含用量的速度，
平均是不生成图像的类似轮次的 3-5 倍，具体取决于
图像质量和尺寸。达到方案所含用量限制后，图像生成
也会消耗[额度](#credits-overview)。

免费方案不提供图像生成功能。通过 API 密钥使用 Codex 时，图像生成按 API 定价计费，而不计入 ChatGPT 方案所含用量限制。

### 在哪里可以查看当前的用量限制？

您可以在[用量
仪表板](https://chatgpt.com/codex/settings/usage)中查看当前的用量限制。如果想在正在进行的
Codex CLI 会话中查看剩余可用量，可以使用 `/status`。

每一到两周查看一次仪表板，了解您的用量消耗速度和剩余可用量。如果用量高于预期，请考虑改用较小的模型或缩小任务范围，看看是否仍能获得有用的结果。

### Token 和额度是什么？

Token 是 ChatGPT 读取和写入的小块信息。您的提示、文件、聊天记录、工具结果以及 ChatGPT 的回复都会使用 Token。

额度是采用额度计费的方案用于支付符合条件用量的单位。达到方案所含用量限制后，您可以使用可用额度继续工作。额度的购买价格及适用折扣取决于您的方案或协议。

#### Token 费率

下方的 Token 费率以每百万输入 Token、缓存输入 Token
和输出 Token 所消耗的额度表示。[详细了解
Token](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)。

快速模式按 Astra 标准费率的 2.5 倍计费。

少数企业客户应继续使用旧版费率表，
直到我们为您切换到新的按 Token 计价方案。如需了解更多信息，
请[联系 OpenAI
销售团队](https://chatgpt.com/contact-sales?utm_internal_source=openai_developers_codex)。

<div id="credits-overview">
  <table>
    <thead>
      <tr>
        <th scope="col">每百万 Token 消耗的额度</th>
        <th scope="col" style="text-align:center">
          输入 Token
        </th>
        <th scope="col" style="text-align:center">
          缓存输入 Token
        </th>
        <th scope="col" style="text-align:center">
          输出 Token
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>GPT-6 Astra</td>
<td style="text-align:center">250 点额度</td>
<td style="text-align:center">25 点额度</td>
<td style="text-align:center">1,250 点额度</td>
      </tr>
      <tr>
        <td>GPT-5.6 Sol</td>
<td style="text-align:center">100 点额度</td>
<td style="text-align:center">10 点额度</td>
<td style="text-align:center">500 点额度</td>
      </tr>
      <tr>
        <td>Daybreak Blue</td>
<td style="text-align:center">100 点额度</td>
<td style="text-align:center">10 点额度</td>
<td style="text-align:center">500 点额度</td>
      </tr>
      <tr>
        <td>Daybreak Red</td>
<td style="text-align:center">312.5 点额度</td>
<td style="text-align:center">31.25 点额度</td>
<td style="text-align:center">1875 点额度</td>
      </tr>
      <tr>
        <td>GPT-5.6 Terra</td>
<td style="text-align:center">50 点额度</td>
<td style="text-align:center">5 点额度</td>
<td style="text-align:center">300 点额度</td>
      </tr>
      <tr>
        <td>GPT-5.6 Luna</td>
<td style="text-align:center">5 点额度</td>
<td style="text-align:center">0.5 点额度</td>
<td style="text-align:center">30 点额度</td>
      </tr>
      <tr>
        <td>GPT-5.5</td>
<td style="text-align:center">125 点额度</td>
<td style="text-align:center">12.50 点额度</td>
<td style="text-align:center">750 点额度</td>
      </tr>
      <tr>
        <td>GPT-5.4</td>
<td style="text-align:center">62.50 点额度</td>
<td style="text-align:center">6.250 点额度</td>
<td style="text-align:center">375 点额度</td>
      </tr>
      <tr>
        <td>GPT-5.4 mini</td>
<td style="text-align:center">18.75 点额度</td>
<td style="text-align:center">1.875 点额度</td>
<td style="text-align:center">113 点额度</td>
      </tr>
      <tr>
        <td>GPT-5.3-Codex-Spark</td>
        <td colspan="3" style="text-align:center">
          研究预览版
        </td>
      </tr>
      <tr>
        <td>GPT-Image-2（图像）</td>
<td style="text-align:center">200 点额度</td>
<td style="text-align:center">50 点额度</td>
<td style="text-align:center">750 点额度</td>
      </tr>
      <tr>
        <td>GPT-Image-2（文本）</td>
<td style="text-align:center">125 点额度</td>
<td style="text-align:center">31.25 点额度</td>
<td style="text-align:center">250 点额度</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="4" style="text-align:center">
          使用 GPT-5.6 时，每条消息平均消耗 5-30 点额度。
        </td>
      </tr>
      <tr>
        <td colspan="4" style="text-align:center">
          对于支持的模型，快速模式会以更高的费率消耗额度。具体费率请参阅
<a href="/codex/agent-configuration/speed">速度</a>。
        </td>
      </tr>
      <tr>
        <td colspan="4" style="text-align:center">
          使用 Daybreak 需通过 [Trusted Access for
          Cyber](/zh-Hans/codex/cyber-safety#trusted-access-for-cyber) 审批。
          Daybreak Blue 采用 GPT-5.6 Sol 的额度费率。Daybreak Red 需要
          单独审批和开通。
        </td>
      </tr>
    </tfoot>
  </table>
</div>

_GPT-5.6 Sol 的优惠定价至少持续至 2026 年 11 月 21 日。_

速度配置会增加所有适用模型的额度消耗。
对于支持的模型，快速模式会以更高的费率消耗额度。支持的模型及费率请参阅
[速度](/zh-Hans/codex/agent-configuration/speed)。

[详细了解 ChatGPT Plus 和
Pro 的额度。](https://help.openai.com/en/articles/12642688)

[详细了解 ChatGPT Business、ChatGPT Enterprise 和
ChatGPT Edu 的额度。](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)

对于 Business 和企业 / Edu 方案的额度计费，请使用<a href="https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing" target="_blank" rel="noopener noreferrer">额度计费费率表</a>。如果您的企业协议规定按用量以美元计费，请改用<a href="https://help.openai.com/en/articles/20001415-chatgpt-rate-card-enterprise-token-based-pricing" target="_blank" rel="noopener noreferrer">企业美元费率表</a>及您的协议。工作空间管理员还可以查看 [ChatGPT Work 的用量和费用](/codex/enterprise/chatgpt-work-usage-and-cost#understand-tokens-and-credits)。

### 哪些操作计入代码审查用量？

仅当 Codex 通过 GitHub 执行审查时，才会计入代码审查用量。例如，
在 Pull Request 中标记 `@Codex` 请求审查，或为代码仓库
启用自动审查。在本地或 GitHub 之外执行的审查会计入
您的总体用量限制。

### 如何让可用量用得更久？

上述用量限制和额度消耗均为平均值。您可以尝试以下方法，充分利用用量限额：

- **控制提示的长度。** 给智能体的指令要明确具体，
  同时删除不必要的上下文。
- **限制参考资料的范围。** 仅提供相关文件，并尽可能
  缩小资料来源或日期范围。
- **让输出符合需求。** 明确受众、格式和长度，
  并区分必需的工作和可选的改进。
- **精简 AGENTS.md 的内容。** 如果您在处理较大的项目，
  可以通过[在代码仓库的不同层级
  放置 AGENTS.md 文件](/zh-Hans/codex/agent-configuration/agents-md#layer-project-instructions)，控制这些文件引入的上下文量。
- **限制使用的 MCP 服务器数量。** 每个
[MCP](/zh-Hans/codex/extend/mcp) 服务器都会为消息添加更多上下文，并消耗
  更多可用量。不需要时，请禁用 MCP 服务器。
- **处理日常任务时，切换到较小的模型。** 使用 GPT-5.6 Terra 或
  GPT-5.6 Luna 可以让本地消息的可用量用得更久，具体取决于
  您原先使用的模型。

有关如何选择任务和界定任务范围的指导，请参阅[高效
使用 Work](/zh-Hans/codex/prompting#use-work-efficiently)。

## 功能可用性

<div
  id="codex-plan-region-limits"
  className="not-prose mt-3 text-sm text-secondary"
>
  <sup>\*</sup> 此功能目前仅在特定地区可用。请查阅
  各项功能的文档，了解地域限制的详情。
</div>
<div
  id="codex-plan-plugin-limits"
  className="not-prose mt-1 text-sm text-secondary"
>
  <sup>†</sup> 部分第一方插件不可用。
</div>
