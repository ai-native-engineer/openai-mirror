<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/plugin -->

Codex Security 会扫描您的代码以查找漏洞，并对疑似漏洞进行验证。对于每个可报告的问题，它都会提供审查结果所需的证据和修复指导。请仅扫描您拥有或获准评估的代码。

按照本快速入门安装插件，并在 Codex 中对本地代码仓库运行标准的只读扫描。

  本页介绍桌面应用或 Codex CLI 中的 Codex Security 插件。若要
  在 Codex 云端扫描已连接的 GitHub 代码仓库，请参阅[Codex Security 云服务
  设置](/zh-Hans/codex/security/setup)。

## 安装插件

1. 打开[ChatGPT 桌面应用中的 Codex](/zh-Hans/codex/app)。
2. 打开 **插件**，搜索 **Codex Security**，或使用下方按钮：

   <div className="not-prose my-6">
     
       安装 Codex Security 插件
     
   </div>

3. 确认插件已启用，然后在侧边栏中打开 **安全** 。

1. 在终端中，进入您要评估的代码仓库并启动 Codex：

   ```bash
   codex

2. 输入 `/plugins`，搜索 **Codex Security**，然后选择 **安装
   插件**。
3. 输入 `/new`，为该代码仓库开始新对话。

若要为本地代码仓库安装 Codex Security，请使用 ChatGPT 桌面应用或 Codex CLI。

  在依赖某项功能或开始长时间运行的扫描前，请先查看[插件更新日志](/zh-Hans/codex/security/plugin/changelog)。
  如果桌面应用的侧边栏中未显示 **安全** ，
  请更新应用和插件，
  并确认插件已启用。

## 运行首次扫描

为获得最佳扫描质量，请使用 <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>，
并将推理强度设为 `xhigh`。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    开始扫描前，请选择代码仓库并配置新的安全扫描。
  </figcaption>
</figure>

1. 打开扫描设置

   在侧边栏中选择 **安全** ，打开 **扫描**，然后选择 **+ 扫描**。

2. 选择代码库和扫描范围

   选择现有代码仓库，或使用其他文件夹。选择 **代码库**，
   保持 **深度扫描** 关闭，然后选择整个代码仓库或单个文件夹。
   确认分支和修订版本对应您要扫描的代码。

3. 添加相关上下文

   选择模型和推理强度。仅在需要说明以下内容以指导审查时，才打开 **补充上下文** ：
   特定攻击向量、安全敏感区域或
   代码仓库详情。

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       启用补充上下文，以说明攻击向量、重点区域和相关安全指导。
     </figcaption>
   </figure>

4. 开始扫描

   选择 **开始扫描** ，并在安全工作台中跟踪扫描的各个阶段。
   选择 **查看活动** ，查看执行扫描的 Codex 任务。

5. 审查结果

   打开已完成的扫描，查看发现项、覆盖范围以及可用的报告文件。
   使用 **发现项** 审查各次扫描中的问题，或使用 **代码仓库**
   查看代码仓库的扫描历史记录。

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       在安全工作台中审查扫描结果、发现项和覆盖范围。
     </figcaption>
   </figure>

1. 请求标准扫描

   在新对话中发送以下提示：

   ```text
   Run a Codex Security scan on this repository.

2. 等待扫描完成

   Codex 会在终端中运行扫描，不会打开设置工作空间。请保持任务运行，直到 Codex 报告扫描已完成。如果 Codex 发现配置方面的限制，请在批准配置更新前，先审查该限制以及提议的具体更改。

3. 审查结果

   先在终端中审查摘要，然后打开生成的 `report.md`，
   查看完整结果。

请在 ChatGPT 桌面应用或 Codex CLI 中运行此本地插件工作流程。

## 扫描生成的内容

已完成的扫描仍可在 **扫描**中查看。
您可以在安全工作台中审查其发现项和覆盖范围，也可以
在 **发现项** 和 **代码仓库**中查看相关发现项及代码仓库历史记录。
扫描还会生成以下文件。

每次扫描完成后，都会在终端中显示摘要并生成以下文件。

请在 ChatGPT 桌面应用或 Codex CLI 中运行此本地插件工作流程。

- `report.md`：阅读扫描结果的主要入口。
- `findings/<slug>/`：在有详细漏洞报告及配套的
  概念验证文件时生成。
- `hardening/`：在有结构层面的加固指导以及配套方案或
  图示时生成。
- 用于自动化和集成的结构化扫描数据保存在 `scan-manifest.json`、`findings.json` 和
`coverage.json` 中。
  您无需打开这些文件即可审查扫描结果。

共享或归档结果时，请一并保留完整的扫描目录，
以确保 `report.md` 中的链接继续有效。

## 选择后续工作流程

- [使用安全工作台](/zh-Hans/codex/security/plugin/workbench)，在桌面应用中管理
  已保存的扫描、发现项、代码仓库和扫描活动。
- 如果您拥有 Beta 版访问权限，并且需要可重复执行、能生成结构化结果的终端工作流程，
  请[从 CLI 运行扫描](/zh-Hans/codex/security/cli)。
- [运行标准扫描或限定范围扫描](/zh-Hans/codex/security/plugin/scans)，使用默认工作流程审查
  代码仓库或单个文件夹。
- [评估首次扫描](/zh-Hans/codex/security/plugin/scans#assess-a-first-scan)，
  对照已知问题检查结果，并决定何时再次扫描。
- 如果您可以接受较长的运行时间，
  请[运行深度扫描](/zh-Hans/codex/security/plugin/deep-scans)，进行更全面的扫描。
- [审查代码更改](/zh-Hans/codex/security/plugin/code-changes)，以评估 Pull Request、
  提交、分支范围或工作树补丁。
- [研判积压项](/zh-Hans/codex/security/plugin/triage-backlog)，以审查现有的
  安全发现项。
- 在您接受某个发现项并决定修复后，
  [修复并验证该发现项](/zh-Hans/codex/security/plugin/fix-findings)。
- [导出或跟踪发现项](/zh-Hans/codex/security/plugin/export-findings)，以创建
  JSON、CSV、SARIF 格式的文件、需经审批的 Linear、GitHub 或 Jira 议题，或
  GitHub 安全公告的私有草稿。
- [编写漏洞报告](/zh-Hans/codex/security/plugin/vulnerability-reports)，
  将提供的发现项、披露说明、源代码和 PoCs 整理为
  独立完整的报告。
- [提出安全加固方案](/zh-Hans/codex/security/plugin/security-hardening)，根据扫描结果或其他
  安全证据，考虑结构或
  架构层面的方案。
