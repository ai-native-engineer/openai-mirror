<!-- source: https://learn.chatgpt.com/zh-Hans/docs/browser -->

Codex CLI 和 Codex IDE 扩展均不支持浏览器功能。请打开 ChatGPT 桌面应用，使用内置浏览器。

浏览器让 ChatGPT 能够打开网站、收集最新信息并执行操作，而您始终拥有控制权。您可以使用它比较选项、在网站上完成多步骤任务，或审查正在构建的页面。

网页版 ChatGPT 和 ChatGPT 桌面应用均提供浏览器功能。

[GPT-6 Astra](/zh-Hans/codex/models#gpt-6-astra) 提升了视觉判断能力，
适用于对照截图检查页面或完成跨网站工作流程等任务。
如果模型选择器中提供此模型，请选择它，并说明如何
验证最终结果。

在受管理的桌面环境中，管理员可以限制浏览器来源、
上传、下载以及开发者访问权限。请参阅
[受管理的浏览器控制措施](/zh-Hans/codex/enterprise/managed-configuration#control-browser-and-computer-use)。

请将页面内容视为不可信的上下文。在分享敏感信息或允许 ChatGPT 执行操作前，请先审查网站和拟执行的操作。

ChatGPT 桌面应用中的内置浏览器让您与 ChatGPT 能够在聊天中共同查看网站和本地 Web 应用。您可以使用它预览页面、提供视觉反馈，或让 ChatGPT 代您与网站交互。

内置浏览器使用独立的浏览器配置方案，
与您常用的浏览器分开。它不会自动共享您现有的标签页或浏览器会话。
任务需要账户时，您可以直接登录。打开 **设置 \>
浏览器** ，即可管理浏览器数据以及
您设备上可用的配置方案导入功能。

浏览器下载的文件默认保存在系统的“下载”文件夹中。在 **设置 \>
浏览器**中，您可以选择其他下载位置、将下载位置恢复为系统默认位置，
或开启 **询问下载文件的保存位置**。

当 ChatGPT 需要在现有的 Chrome、Edge、Brave、Opera 或 Vivaldi 标签页中操作，
或使用您常用的浏览器配置方案时，
请改用[浏览器扩展程序](/zh-Hans/codex/chrome-extension)。

您可以从工具栏打开内置浏览器，也可以点击 URL、手动导航，
或按 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>
（在 Windows 上为 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>）。

  
    
  

## 通过地址栏搜索

在内置浏览器的地址栏中输入内容，即可从其浏览历史记录中查找页面。选择匹配的页面即可重新打开；如果历史记录中没有匹配结果，可以输入搜索词，在 Google 上搜索。

内置浏览器保留自己的配置方案和浏览历史记录。搜索结果不会自动包含您常用的 Chrome 配置方案或其他浏览器中的页面。

## 管理浏览历史记录

打开 **设置 \> 浏览器** ，即可搜索内置浏览器的历史记录、
重新打开已访问的页面，或在您的组织允许时删除历史记录条目。
使用**清除浏览数据** ，选择时间范围以及
要删除的浏览数据类型。

如果该功能可用，ChatGPT 可以请求搜索您的浏览历史记录，以查找与当前任务相关的页面。允许访问前，请先审查请求。浏览历史记录可能包含内部 URL、搜索词和其他敏感信息，因此请仅在任务需要此类上下文时允许访问。

<a id="browser-use"></a>

## 浏览器中的计算机使用

在桌面应用中，计算机使用功能让 ChatGPT Work 或 Codex 能够直接操作内置浏览器。您选择的产品可以打开页面、点击、输入、检查渲染状态、截取屏幕截图，并在页面中验证操作结果。

浏览器随桌面应用提供，并会自动安装。
请让 ChatGPT 或 Codex 在任务中使用内置浏览器，
或通过 `@Browser` 直接引用它。

例如：

```text
Use the browser to open http://localhost:3000/settings, reproduce the layout
bug, and fix only the overflowing controls.

除非您已允许某个网站，否则 ChatGPT 在使用该网站前会先征求您的许可。
您可以在 **设置 \> 浏览器**中管理允许和屏蔽的网站。
ChatGPT 还会在提交信息、购买、
更改权限或删除数据等敏感操作前请求确认。
ChatGPT 无法在内置浏览器中自动上传文件。

  页面上的指令可能具有误导性或恶意。网站权限允许 ChatGPT 与该网站交互，但不代表网站内容可信，也不意味着所有操作都已获批。

## 预览页面

1. 在[集成终端](/zh-Hans/codex/integrated-terminal)中或通过[本地环境操作](/zh-Hans/codex/environments/local-environment#actions)启动您应用的开发服务器。
2. 点击 URL，或在浏览器中手动导航，打开本地路由、基于文件的页面或公开页面。
3. 对照代码差异审查页面的渲染状态。
4. 在需要修改的元素或区域上添加浏览器评论。
5. 让 ChatGPT 处理这些评论，并保持较小的任务范围。

例如：

```text
I left comments on the pricing page in the built-in browser. Address the mobile
layout issues and keep the card structure unchanged.

## 在页面上添加评论

如果某个错误只有在渲染后的页面中才可见，请使用浏览器评论向 ChatGPT 提供准确反馈。

1. 开启 **批注模式**。
2. 点击某个元素，或拖动以选择一个区域。
3. 撰写并保存您的评论。
4. 在聊天中发送消息，让 ChatGPT 处理这些评论。

在评论中明确说明问题和期望结果，效果最佳：

```text
This button overflows on mobile. Keep the label on one line if it fits,
otherwise wrap it without changing the card height.

```text
This tooltip covers the data point under the cursor. Reposition the tooltip so
it stays inside the chart bounds.

<section class="feature-grid">

<div>

### 样式反馈

为页面中的某个区域添加批注时，请选择文本输入框旁的 **调整** ，
向 ChatGPT 提供更细致的样式反馈。
您可以修改字体、文本、间距和颜色等属性，在页面上预览效果，
然后发送目标更明确的批注。

</div>

  
    
  

</section>

## 限定浏览器任务的范围

确保每项浏览器任务的范围足够小，以便一次完成审查。

- 明确指出页面、路由或 URL。
- 明确指出您关注的状态，例如加载中、空状态、错误或成功。
- 在需要修改的具体元素或区域上添加评论。
- ChatGPT 完成后，再次审查页面。
- 请让 ChatGPT 在打开本地页面前，先启动或检查开发服务器。

对于代码仓库中的变更，请使用[审查窗格](/zh-Hans/codex/code-review?surface=app)
检查这些变更并添加评论。

<section class="feature-grid">

<div>

## 开发者模式

开发者模式可以配合 Chrome 和内置浏览器中的计算机使用功能使用，让 ChatGPT 以受控方式访问 Chrome DevTools Protocol（CDP）。使用它可以分析 JavaScript 性能、检查控制台输出和网络流量、查看 DOM 及已应用的样式，或在运行中的浏览器里诊断问题。

要启用此功能，请打开[**设置 \> 浏览器**](codex://settings/browser-use)，
在 **开发者模式**下开启 **启用完整 CDP 访问权限**。
如果您的组织已禁用此设置，您就无法在本地启用它。
管理员可以在 [`requirements.toml`](/zh-Hans/codex/enterprise/managed-configuration#pin-feature-flags) 的 `[features]` 下
设置 `browser_use_full_cdp_access = false`，
以禁用完整 CDP 访问权限，并阻止用户
在 ChatGPT 桌面应用中启用相应设置。

完整 CDP 访问权限可能暴露浏览器内部的敏感信息。ChatGPT 在使用完整 CDP 检查网站前，会请求您的明确批准。批准前，请先审查网站、任务以及请求的访问权限。

使用 `@Browser` 调用内置浏览器。要在 Chrome 中使用开发者模式，
请[设置 Chrome 扩展程序](/zh-Hans/codex/chrome-extension)，并调用 `@Chrome`。

例如：

```text
This app is slow. Use @Browser to capture a performance trace and inspect
network traffic, then identify the bottleneck.

</div>

  
    
  

</section>

## 使用 ChatGPT Work 跨网站完成任务

ChatGPT Work 可以跨网站完成任务，包括需要您登录的网站。

Work 使用自己的浏览器，该浏览器运行在云端的一台独立计算机上，并非您手机或笔记本电脑上的浏览器。

在网页端或移动端的 ChatGPT Work 中开始任务后，即使您离开并合上电脑，ChatGPT 也能继续工作。Work 可以使用自己的计算机，通过阅读、点击网页和在网页中输入内容，完成各种互联网任务。根据您的请求，它可能会使用插件、浏览器，或同时使用两者。

例如，ChatGPT 可以帮助您：

- 查找并预约 DMV 办事时段。
- 登录您的公用事业服务账户并比较套餐。
- 查找并收藏符合您条件的公寓房源。
- 在社交媒体上研究竞争对手。
- 在您的会计软件中完成结账。

您可以决定 ChatGPT 能访问哪些网站。ChatGPT 经过训练，会在完成预订或付款等可能产生重大影响的操作前请求确认。如果 ChatGPT 因任何原因无法继续，您都可以在移动端或桌面端接管它的计算机并亲自操作。

Plus 和 Pro 方案用户可以在网页端和移动端使用 ChatGPT Work 访问需要身份验证的网站。

具体可用性取决于推出进度。企业或 Edu 工作空间不支持网站登录。

## ChatGPT Work 的计算机如何运作

当您的任务需要访问网站时，ChatGPT 会使用自己的浏览器浏览页面、收集信息并在线完成任务步骤。

默认情况下，ChatGPT 会在访问新网站前征求您的许可。您可以选择逐一批准请求，也可以调整设置，让 ChatGPT 自动批准访问与您任务相关的网站。ChatGPT Work 在执行可能产生重大影响的操作前始终会请求确认，例如提交您的信息以完成预约或完成付款。

## 登录网站

如果网站要求登录，ChatGPT Work 会请您登录。您完成身份验证后，它会继续在已登录的网站上执行任务。您的会话会保持有效，以供后续任务使用，因此您无需每次都登录。

### 使用安全登录表单

ChatGPT 无法看到您的用户名或密码，模型也绝不会看到这些信息，这些信息也不会用于模型训练。ChatGPT 不会存储您的用户名或密码。您可以随时前往 **设置** \> **云端浏览器** \> **浏览器数据**，删除所有网站或单个网站的浏览历史记录，这也会让您退出相应网站的登录状态。

当 ChatGPT 遇到登录界面时，它会暂停，并请您根据需要输入登录凭据和双重身份验证代码。在 iOS 上，您可以使用受支持的密码管理器便捷登录。

请使用 ChatGPT 提供的登录表单。不要在聊天中发送密码。

![iOS 上的 ChatGPT Work 暂停 DMV 任务并显示安全登录表单，表单中可见网站地址，密码则以掩码显示。](/images/codex/cloud-browser-auth/sign-in.webp)

### 在网页上登录

如果有此选项，请选择 **改为在网页上登录** ，直接在云端浏览器中登录。登录期间，任务会暂停。选择 **我已完成** ，将控制权交还给 ChatGPT；您也可以跳过或取消该请求。

<a id="start-a-browser-task"></a>
<a id="start-browser-work"></a>
<a id="web-start-browser-work"></a>

## 如何在 ChatGPT Work 中开始任务

1. 打开 ChatGPT 网页端或移动端，在 Work 中开始任务。
2. 描述您希望 ChatGPT 完成的工作。
3. 如收到提示，请批准网站访问请求。
4. 如果网站要求登录，请直接登录。
5. 在对话中查看任务进度。
6. 审查结果，并批准可能产生重大影响的操作。

您无需单独选择浏览器。ChatGPT 会根据您的请求决定何时使用它。

有些网站会阻止访问。如果遇到这种情况，ChatGPT 会告知您，并在可能的情况下尝试通过其他方式完成任务。

<a id="website-permissions-and-confirmations"></a>
<a id="web-website-permissions-and-confirmations"></a>

## 安全与用户控制

在 ChatGPT 设置中打开 **云端浏览器** ，管理网站权限。可用选项包括：

- **始终询问**：手动审查每个网站访问请求。
- **自动审批**：让 ChatGPT 在检查网站与您任务的相关性后自动批准访问。
- **始终允许**：无需上述额外审查步骤即可允许访问网站。我们提供此选项是为了尽量简化操作，但不建议使用。

![云端浏览器设置，显示“始终询问”“自动审批”和“始终允许”网站权限选项。](/images/codex/cloud-browser-auth/website-permissions.webp)

您还可以单独允许或阻止对特定网站的访问，以覆盖默认权限设置。

在 ChatGPT 请求您登录任何网站之前，另一个审查模型会检查登录请求及您将输入信息的位置，判断是否存在网络钓鱼或欺骗迹象。我们针对提示注入、网络钓鱼和非预期操作等风险测试该智能体。

为确保整个过程透明，您会看到网站地址和登录表单预览，也可以在继续之前查看实际网站。通过安全登录表单输入的凭据会直接发送到浏览器，模型无法看到这些凭据。

<a id="browser-data"></a>
<a id="web-browser-data"></a>

## 隐私与浏览器数据

ChatGPT Work 的计算机独立于您设备上的浏览器运行，并维护自己的 Cookie、浏览器数据和已登录会话。ChatGPT 在完成任务时使用的信息受您选择的 ChatGPT 数据控制设置约束。您可以在 ChatGPT 网页端和移动端的 **设置** \> **数据控制**中查看这些设置。

它不会使用您个人浏览器中已打开的标签页、浏览历史记录、保存的密码、Cookie、扩展程序或现有的已登录会话。

要清除浏览器数据，请前往 **设置** \> **云端浏览器** \> **浏览器数据** \> **全部清除**。这会让您退出 ChatGPT Work 浏览器中各网站的登录状态，因此执行后续任务时，您需要重新登录。

![云端浏览器设置，包含“浏览器数据”部分和“Cookie”控件，用于管理云端浏览器保存的 Cookie。](/images/codex/cloud-browser-auth/browser-data.webp)

## 限制

- 并非所有工作空间或推出阶段都支持网站登录。如果任务要求使用不受支持的登录方式，请自行完成该步骤，或使用其他可用工具。
- 有些网站会屏蔽自动化浏览器，或要求完成 CAPTCHA 验证。ChatGPT 可能无法在这些网站上完成任务。
- 云端浏览功能的可用性可能取决于您的方案、工作空间设置和推出进度。除免费版和 Go 外的付费方案均可在所有地区使用云端浏览功能。企业管理员必须为其工作空间启用云端浏览功能。

在推出期间，即使您的方案支持浏览器，它也可能不会立即显示。
