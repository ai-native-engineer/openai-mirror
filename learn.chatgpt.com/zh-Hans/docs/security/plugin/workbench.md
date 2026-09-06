<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/plugin/workbench -->

安全工作台会在 Codex 桌面应用中集中展示您的扫描、发现项和代码仓库。
Codex 会通过常规任务执行扫描分析，工作台则会保留扫描及其结果，
方便您返回后继续查看。

在 ChatGPT 桌面应用中，打开 ChatGPT 下拉菜单，选择 **Codex**。
安装并启用 [Codex Security 插件](/zh-Hans/codex/security/plugin)，然后
在侧边栏中选择 **安全** 。

  如果未显示 **安全** ，请确认已选择 **Codex** ，
  且插件已安装并启用。如有需要，请更新桌面应用和插件，
  并检查您的工作空间管理员是否允许使用该插件。

## 开始扫描

为获得最佳扫描质量，请使用 <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>，
并将推理强度设置为 `xhigh`。

1. 打开 **扫描** ，然后选择 **+ 扫描**。
2. 选择现有的代码仓库，或选择其他文件夹。
3. 选择 **代码库** 以扫描代码仓库，或选择 **更改** ，
   以审查基于 Git 的更改。
4. 对于标准代码库扫描，请选择整个代码仓库或一个文件夹。
5. 要执行深度扫描，请先选择代码仓库或文件夹作为代码库，
   然后开启 **深度扫描**。深度扫描会审查整个选定代码库。
6. 要扫描更改，请选择未提交的更改、某次提交或一个修订版本范围。
   更改扫描不支持 **深度扫描** 。
7. 选择模型及推理强度。打开 **其他上下文** ，
   描述相关攻击向量、重点关注领域或其他安全上下文。
8. 选择 **开始扫描**。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    在安全工作台中选择代码仓库并配置扫描。
  </figcaption>
</figure>

请参阅[运行安全扫描](/zh-Hans/codex/security/plugin/scans)、[运行深度安全
扫描](/zh-Hans/codex/security/plugin/deep-scans)或[审查代码更改的
安全性](/zh-Hans/codex/security/plugin/code-changes)，
了解各类扫描的详细信息。

## 跟踪扫描进度

扫描页面会显示当前阶段以及插件报告的扫描进度。
对于标准扫描，这些阶段包括威胁建模、发现、验证、
影响与路径分析、生成报告和收尾。

选择 **查看活动** ，打开执行扫描的 Codex 任务。您可以
离开工作台后再返回 **扫描** ，已保存的扫描不会丢失。
如需主动停止扫描，请打开该扫描并选择 **停止扫描**。

扫描完成后，打开结果，审查扫描目标、修订版本、
发现项、覆盖范围和可用的报告产物。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    扫描完成后，
审查发现项、严重程度、扫描覆盖范围和产物。
  </figcaption>
</figure>

## 审查不同扫描中的发现项

打开 **发现项** ，查看不同代码仓库和扫描中已保存的发现项。
搜索或筛选列表，然后选择一个发现项，审查其摘要、源代码证据、
验证结果和影响。

使用 **摘要** 查看发现项详情；使用 **补丁** 生成、
审查、应用或验证针对性修复。有关修复工作流程，请参阅[修复并验证安全
发现项](/zh-Hans/codex/security/plugin/fix-findings)。

  **发现项** 标签页会显示已保存的 Codex Security 扫描中的发现项。
  导入的工单和其他现有安全问题仍属于独立的
[积压问题分类处理工作流程](/zh-Hans/codex/security/plugin/triage-backlog)。

## 查看代码仓库历史记录

打开 **代码仓库** ，浏览可用的代码仓库和文件夹。选择一个
代码仓库，查看其扫描历史记录、最近扫描的修订版本，以及尚未解决的
发现项。您可以在代码仓库详情中打开以往的扫描，或查看与该代码仓库
相关的发现项。

如果代码仓库没有扫描记录，请从其详情页面开始扫描，或在工作台中选择 **+ 扫描**
开始扫描。

## 从对话中开始扫描

您也可以在常规对话中要求 Codex 运行已安装的 Codex Security 插件。
使用共享插件工作台的扫描会显示在 **扫描**中，
因此您可以通过安全工作台返回查看扫描进度和结果。

有关基于终端的扫描和自动化，请参阅 [Codex Security CLI
快速入门](/zh-Hans/codex/security/cli)。
