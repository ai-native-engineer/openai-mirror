<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/setup -->

本页将引导您完成 Codex Security 云服务的整个流程：从获取初始访问权限，到审查发现项并创建修复
Pull Request。

  请先确认您已完成 Codex 云端的设置。若尚未设置，请参阅 [Codex
  云端](/zh-Hans/codex/cloud)，了解如何开始使用。

## 1. 访问权限与环境

Codex Security 云服务会扫描通过
[Codex 云端](/zh-Hans/codex/cloud)连接的 GitHub 代码仓库。

- 确认您的工作空间有权访问 Codex Security 云服务。
- 确认您要扫描的代码仓库在 Codex 云端中可用。

前往 [Codex 环境](https://chatgpt.com/codex/settings/environments)，检查该代码仓库是否已有环境。如果没有，请先在那里创建一个环境，然后再继续。

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 2. 新建安全扫描

环境创建后，请前往[创建安全扫描](https://chatgpt.com/codex/security/scans/new)，然后选择您刚刚连接的代码仓库。

Codex Security 会先从最新提交开始，按时间倒序扫描代码仓库。它会据此构建扫描上下文，并在有新提交时更新上下文。

配置代码仓库的步骤如下：

1. 选择 GitHub 组织。
2. 选择代码仓库。
3. 选择您要扫描的分支。
4. 选择环境。
5. 选择 **历史记录时间范围**。时间范围越长，提供的上下文越多，但回填所需时间也越长。
6. 点击 **创建**。

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 3. 初始扫描可能需要一段时间

创建扫描时，Codex Security 会先在选定的历史记录时间范围内执行一轮提交级安全检查。
初始回填可能需要数小时，对于规模较大的代码仓库或较长的时间范围尤其如此。
如果未立即看到发现项，这是正常现象。在提交工单或排查问题之前，请等待初始扫描完成。

  初始扫描的设置过程自动而全面。这可能需要数小时。如果第一批发现项延迟出现，
请不必担心。

## 4. 审查扫描并改进威胁模型

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

初始扫描完成后，请打开该扫描并审查生成的威胁模型。
初始发现项出现后，请更新威胁模型，使其与您的架构、信任边界和业务上下文保持一致。
这有助于 Codex Security 为您的团队确定问题的优先级。

  如果您希望扫描结果发生变化，可以根据更新后的范围、优先事项和假设
编辑威胁模型。

初始发现项出现后，请重新审视模型，使扫描指引与当前优先事项保持一致。
及时更新模型有助于 Codex Security 提供更好的建议。

如需深入了解威胁模型及其对严重程度和分类处置的影响，请参阅[改进威胁模型](/zh-Hans/codex/security/threat-model)。

## 5. 审查发现项并修复问题

初始回填完成后，请在 **发现项** 视图中审查发现项。

您可以使用以下两种视图：

- **推荐发现项**：动态更新的列表，列出代码仓库中最严重的 10 个问题
- **所有发现项**：涵盖整个代码仓库且可排序、可筛选的发现项表格

  
    
  

点击某个发现项即可打开其详情页面，其中包括：

- 问题的简要说明
- 提交详情和文件路径等关键元数据
- 结合上下文对影响进行的推理分析
- 相关代码摘录
- 可用时提供的调用路径或数据流上下文
- 验证步骤和验证输出

您可以审查每个发现项，并直接从发现项详情页面创建 PR。

## 相关文档

- [Codex Security](/zh-Hans/codex/security) 提供产品概览。
- [Codex Security 云服务常见问题](/zh-Hans/codex/security/faq)涵盖云服务相关的常见问题。
- [改进威胁模型](/zh-Hans/codex/security/threat-model)介绍如何改进扫描上下文和发现项的优先级排序。
