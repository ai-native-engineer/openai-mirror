<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/roles-and-workspace-permissions -->

不同设置分别管理您所在组织使用 ChatGPT 的不同方面。在某个方面向用户授予访问权限，并不会自动使其获得其他方面的访问权限。请通过本页了解六个控制边界如何协同运作，然后参阅所附链接中的指南，查看当前的设置步骤。

在工作空间设置中， **Codex 和 Work 本地** 将本地 Codex 和 Work 的
访问权限合并到 **允许成员在本地使用 Codex 和 Work**下。另一些工作空间
则将 **Codex 本地** 和 **Work 本地** 分为独立的部分。在这种
布局中， **允许成员在本地使用 Codex** 授予本地 Codex 访问权限，
**在本地使用 Work** 授予本地 Work 访问权限。启用其中一项不会授予
另一项的访问权限。这些标签表示工作空间权限，而非独立的
产品或客户端。令牌权限和凭证有效期限制会出现在
 **访问令牌** 部分或本地访问权限部分，具体取决于
工作空间。托管配置是独立的控制层，用于约束
这些客户端中适用功能所支持的运行时行为。功能
和实际生效的要求可能因客户端和版本而异。

## 了解控制边界

| 边界          | 控制的内容                                                                                                                                                                                      | 不控制的内容                                                                          | 当前参考来源                                                                                                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT 工作空间 | 成员资格、席位、内置管理角色，以及按角色授予的受支持工作空间功能访问权限                                                                                               | 本地智能体权限、平台 API 组织访问权限，或已连接服务中的权限 | [ChatGPT 工作空间访问权限](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)和 [RBAC](https://help.openai.com/en/articles/11750701-rbac) |
| 本地客户端     | ChatGPT 桌面应用、Codex CLI 和 IDE 扩展中适用功能的运行时行为，包括审批、文件系统和网络访问、权限配置方案，以及允许使用的集成 | ChatGPT 席位、功能或模型使用资格，或外部数据访问权限                         | [托管配置](/zh-Hans/codex/enterprise/managed-configuration)和[权限](/zh-Hans/codex/permissions)                                                                                                   |
| Codex 云端       | 使用托管式 Codex 工作流和向用户开放的云端环境的资格                                                                                                       | 本地运行时策略，或源系统授予的代码仓库权限                    | [云端环境](/zh-Hans/codex/environments/cloud-environment)                                                                                                                                              |
| 平台 API      | 通过 API 身份验证开展工作时的组织和项目成员资格、API 密钥、模型访问权限、用量和计费                                                                                            | ChatGPT 工作空间成员资格、本地客户端访问权限或 Codex 云端访问权限                         | [OpenAI API 平台](https://platform.openai.com/docs/overview)                                                                                                                                         |
| 插件           | 插件的可用性和安装、随附技能、连接器访问权限，以及受支持的连接器操作                                                                                               | 已连接服务中的授权，或更广泛的本地和云端运行时权限            | [插件控制](/zh-Hans/codex/enterprise/apps-and-connectors)                                                                                                                                                 |
| 已连接的系统 | 通过身份验证的账户在源系统中可以访问哪些代码仓库、文件和消息，以及可以执行哪些操作                                                                                            | ChatGPT 工作空间、插件、Codex 云端或平台 API 的使用资格                              | 已连接服务的管理和访问控制                                                                                                                                               |

请求必须通过所有适用的控制边界。例如，工作空间访问权限可以使插件可用，但已连接服务仍决定已登录账户可以读取哪些数据。本地权限配置方案可以限制受支持本地客户端中的运行行为，但不能授予工作空间功能或模型的使用资格。

## 分配工作空间访问权限

ChatGPT 工作空间管理将产品访问权限与管理权限区分开来。

### 了解席位、管理角色和自定义角色之间的区别

席位决定成员可以访问哪些产品界面。根据工作空间的订阅方案，可用席位类型可能包括 ChatGPT 席位和 Codex 席位。

内置工作空间角色决定管理权限。 **所有者** 角色
管理整个工作空间的设置； **管理员** 角色管理受支持的操作
和群组； **成员** 角色没有管理权限；
**分析查看者** 角色可以访问工作空间分析。

自定义角色决定成员可以使用哪些受支持的功能，但不能替代席位或订阅方案的使用资格、授予已连接系统中的权限，或更改本地运行时要求。

<div class="not-prose my-4 aspect-video overflow-hidden rounded-md bg-gray-900">
  <iframe
    src="https://player.vimeo.com/video/1215495812"
    title="基于角色的访问控制操作演示"
    loading="lazy"
    allow="autoplay; fullscreen; picture-in-picture"
    allowFullScreen
    referrerPolicy="strict-origin-when-cross-origin"
    class="h-full w-full border-0"
  ></iframe>
</div>

### 先设置工作空间默认配置，再创建有针对性的自定义角色

只有工作空间所有者才能配置基于角色的访问控制（RBAC）并创建自定义角色。工作空间设置为适用的权限设定基准。工作空间所有者可以通过群组分配自定义角色；在受支持的情况下，也可以直接将角色分配给个别成员。群组可以手动管理或通过 SCIM 同步，一名成员可以获分配多个自定义角色。

对于适用的权限， **默认** 表示沿用工作空间设置， **开启**
表示授予访问权限， **关闭** 表示明确拒绝访问。只要任一适用角色明确设为 **关闭** ，
即使其他角色授予访问权限，也会阻止访问。可用的
权限状态可能因功能而异。

### 审查 Work 本地和 Work 云端权限

如果您的工作空间提供 **Work 本地** 和 **Work 云端**，请同时检查
工作空间默认设置和每个适用的自定义角色。Work 仅向
符合条件的工作空间开放；可用的控制项可能因订阅方案、工作空间
配置和上线进度而异。角色不能扩大成员席位允许的
访问范围。

**Work 云端** 控制受支持的云端 ChatGPT Work 任务。当这些
控制项相互独立时，拥有 **Work 本地** 但没有 **Work 云端** 权限，允许成员在
ChatGPT 桌面应用中开展本地工作，但不允许成员启动云任务。
本地 Codex 访问权限由 **允许成员在本地使用 Codex** 控制，此设置位于 **Codex
本地**中。更改 **在本地使用 Work** 不会改变本地 Codex 访问权限，也不能
替代本地运行时要求。

有些工作空间则显示合并后的 **Codex 和 Work 本地** 部分。在
这种布局中， **允许成员在本地使用 Codex 和 Work** 控制这两款
产品。

有关当前的使用资格和设置，请参阅
[ChatGPT Work 与 Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)。

由于可用席位、角色和权限会随着产品和订阅方案的更新而变化，请前往帮助中心查看当前的权限列表和设置流程：

- [管理成员、席位类型、角色和访问权限](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [配置基于角色的访问控制](https://help.openai.com/en/articles/11750701-rbac)
- [管理群组](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)

### 控制计算机使用记录的访问权限

[计算机使用记录](/zh-Hans/codex/customization/computer-history)在
Business 和企业工作空间中默认关闭。只有工作空间
所有者明确授予访问权限后，成员才能启用该功能。企业工作空间所有者可以
按角色授予访问权限：

1. 打开[**工作空间设置 \> 权限与角色**](https://chatgpt.com/admin/settings)。
2. 找到 **计算机使用记录** ，并选择应拥有
   访问权限的工作空间角色。
3. 为该角色开启 **启用计算机使用记录** 。

该权限仅允许获分配权限的成员开启计算机使用记录，不会替他们启用该功能。每位成员都必须在 macOS 上的 ChatGPT 桌面应用中主动启用，并可以选择将哪些应用和网站纳入记录。未获得所需工作空间权限的成员无法通过本地设置启用该功能。

## 应用本地运行时策略

本地运行时策略会约束 ChatGPT 桌面应用、Codex CLI 和 IDE 扩展中适用的功能。云端托管要求还取决于是否使用受支持的 ChatGPT 登录方式，以及是否具备相应订阅方案资格。权限配置方案和托管要求可以限制命令、文件系统访问、网络访问、审批，以及其他本地运行时行为。它们不会更改用户的席位、工作空间角色、模型使用资格或外部系统中的权限。

在本地策略允许的情况下，
用户可以选择内置或自定义权限配置方案。管理员可以通过
受支持的托管配置渠道分发默认设置和要求。请参阅[权限](/zh-Hans/codex/permissions)
了解配置方案的行为，并参阅[托管配置](/zh-Hans/codex/enterprise/managed-configuration)
了解相关要求、分发方式和优先级。

## 相关文档

- [管理员上线指南](/zh-Hans/codex/enterprise/admin-setup)
- [群组与预配](/zh-Hans/codex/enterprise/groups-and-provisioning)
- [用户生命周期管理](/zh-Hans/codex/enterprise/user-lifecycle)
- [工作空间模型可用性](/zh-Hans/codex/enterprise/workspace-model-availability)
- [访问令牌](/zh-Hans/codex/enterprise/access-tokens)
- [托管配置](/zh-Hans/codex/enterprise/managed-configuration)
- [身份验证](/zh-Hans/codex/auth)
