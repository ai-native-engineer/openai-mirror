<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/plugin/triage-backlog -->

使用 `$codex-security:triage-finding` 研判现有安全发现项，
并对照当前代码仓库进行核查。此工作流执行只读静态
分析：Codex 将每个发现项视为未经证实的论断，并在不执行代码的情况下检查代码仓库中的
证据。

请从范围限定于您要
评估的代码仓库的 Codex 项目中运行此工作流。Codex 必须能够读取该代码仓库的源代码。Jira 和 Linear
连接器可以提供发现项数据，而 GitHub 发现项需要经过身份验证的
GitHub REST 访问权限。这些方式都不能替代对源代码的访问权限。

具体而言，Codex 会从引用的代码或版本信息开始。它
会追踪声称受攻击者控制的源、相关安全控制措施、
危险汇点和可达路径。它还会检查产品功能面和信任
边界，查找与论断相矛盾的证据，并记录证据缺口。随后，Codex 会为
每个发现项返回一项判定，并对需要采取行动或进一步
审查的发现项进行排名。

这与 `$codex-security:validation` 不同，后者可以构建或运行代码、
创建针对性测试或概念验证，或对真实接口执行操作来
复现发现项所述问题或推翻该发现项。使用研判工作流对现有
积压项进行分类和排序。如果某个发现项仍无法通过静态证据确定，
而运行时证据可能消除其不确定性，请使用验证工作流。

  积压项研判以现有发现项为起点。要在代码仓库中搜索新的
  漏洞，请执行以下操作：[运行安全扫描](/zh-Hans/codex/security/plugin/scans)。研判
  不会修改代码仓库，也不会实施修复。

## 选择要研判的发现项

您可以提供来自以下来源的单个发现项或发现项集合：

| 来源                   | 需提供的内容                                                                                                                                                                                                                                                                                                                                                                                                                                        | 要求                                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 粘贴的发现项或本地发现项 | SARIF 结果、CVE 或 GHSA、安全公告、扫描器工单、漏洞赏金报告、Codex Security 发现项产物，或以自然语言描述的漏洞论断。                                                                                                                                                                                                                                                                                          | 无需连接器。                                                                                                                                                                           |
| Jira 或 Linear           | 安全问题或漏洞问题的确切 URL 或标识符、Jira JQL，或 Linear 团队、项目或搜索短语。Codex 会在研判前检索所选问题的内容。                                                                                                                                                                                                                                                                            | 具备以下任一连接器的读取权限：[通过 Atlassian Rovo 访问 Jira](codex://plugins/plugin_connector_692de805e3ec8191834719067174a384) 或 [Linear](codex://plugins/plugin_asdk_app_69a089a326dc8191b32a3f2553f5be2c)。 |
| GitHub                   | 一个代码仓库和一个发现项来源：代码扫描、`Dependabot` 漏洞和恶意软件、安全公告和私密漏洞报告，或所有来源。如果未指定代码仓库，Codex 会在当前 Codex 项目已关联 GitHub 代码仓库时使用该仓库。默认的 GitHub 来源不包括 GitHub 议题；如需研判 GitHub 议题，请提供具体议题，或明确要求研判 GitHub 议题。 | 经过身份验证的 GitHub REST 访问权限，例如 `gh auth token`、`GH_TOKEN` 或 `GITHUB_TOKEN`，且具备所选代码仓库和发现项类型的读取权限。                                      |

Codex 会按输入顺序为提供的每个发现项保留一项结果，确保每个
来源发现项都可追溯。它不会合并或丢弃看起来
重复的发现项。

## 运行只读研判

对于粘贴的发现项或本地产物，请发送类似以下内容的提示：

```text
Use $codex-security:triage-finding to triage these existing security findings against this repository:

[Paste the findings or provide the artifact path.]

对于 Jira 或 Linear 问题，请指定问题集合，并使源系统保持
只读状态：

```text
Use $codex-security:triage-finding to import and triage the security findings from [Jira or Linear issue URLs, identifiers, or query] against this repository.
Do not change the source issues.

对于 GitHub 发现项，请指定代码仓库和来源：

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from [owner/repository] against this repository.

要使用当前 Codex 项目关联的 GitHub 代码仓库，只需指定
发现项来源：

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from GitHub against this repository. Use the GitHub repository attached to the current Codex project.

此工作流按以下顺序进行：

1. 收集并整理发现项

   Codex 会检索请求的所有问题或 GitHub 内容，保留来源
标识符和引用信息，并为每项输入创建一个研判项。它会先构建
完整的研判项列表，再给出判定。

2. 确认代码仓库上下文

   Codex 会解析当前代码仓库，并在可用时确定其修订版本。它会读取
`SECURITY.md`（如果存在），以便在评估中考虑受支持的版本、可信输入、产品
   边界和范围外的功能面。

3. 检查静态证据

   对于每个发现项，Codex 会追踪声称受攻击者控制的源、
相关安全控制措施、易受攻击的汇点、可达路径和受支持的
安全边界。它会记录支持该论断的证据、反驳该
论断的证据以及证据缺口。

4. 给出判定和排名

   Codex 会为每个发现项给出判定和置信度。它会在各自独立的队列中，按可利用性对
`confirmed` 和 `needs_review` 发现项进行排名。

## 审查结果

| 判定          | 含义                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `confirmed`      | 代码仓库中的证据表明，该漏洞路径在所述前提条件下可达，并且跨越受支持的安全边界。                     |
| `not_actionable` | 代码仓库中的证据排除了该论断，例如证明版本不受影响、路径不可达、防护措施有效，或相关功能面未随产品发布。                 |
| `needs_review`   | 代码仓库中的证据不足以做出判定，因为所需信息缺失或存在歧义，或者判定取决于运行时、环境或策略。 |

  可利用性排名使用从 `1` 开始的正整数，并在
  每个判定队列中独立编号。这样可将修复优先级与
  尚待解决的审查工作分开。在该结果集中，排名 `1` 表示可利用性最高的 `confirmed` 发现项，
  或优先级最高的 `needs_review` 发现项。该排名
  并非扫描器严重性评分，且不对 `not_actionable` 发现项进行排名。

对于每个发现项，请审查：

- 判定和排名的依据
- 支持该论断的证据和反驳该论断的证据
- 待解决的问题和剩余证据缺口
- 受影响的位置和组件
- 产品功能面和来源信任级别
- 建议的后续步骤
- 交由 [`$codex-security:fix-finding`](/zh-Hans/codex/security/plugin/fix-findings)
  处理（当发现项为 `confirmed` 时）

当每个提供的发现项都有一项结果、Codex 保留
其来源标识符且所有不确定性均已明确标出时，研判即告完成。Jira、Linear 和其他
积压项记录会保持不变，除非您要求 Codex 在
审查研判结果后写回。

## 后续步骤

- `confirmed`：在人员接受该发现项并决定修复后，使用
[`$codex-security:fix-finding`](/zh-Hans/codex/security/plugin/fix-findings) 修复并
  验证该发现项。研判会准备好可直接用作提示的移交内容，但不会
  自动调用该技能。
- `needs_review`：如果运行代码可以消除证据缺口，请使用
`$codex-security:validation` 执行范围受限的动态验证。请传入
  研判结果中的发现项论断、受影响的位置、前提条件、静态证据和
  证据缺口：

  ```text
  Use $codex-security:validation to dynamically validate finding [triage item ID or source ID] from the backlog triage result. Use the strongest realistic, bounded method, record exactly what was tested, and preserve any remaining proof gaps.

  与研判不同，验证可能会构建或运行代码、创建针对性测试或
  概念验证，或对真实接口执行操作。请先审查拟执行的命令，再予以审批，
  并确保 [Codex 审批策略和安全
  策略](/zh-Hans/codex/agent-approvals-security) 保持生效。

- `needs_review`：如果发现项取决于产品策略或部署
  上下文，请先回答列出的待解决问题，再更改代码。
- `not_actionable`：将证据与研判记录一并保留。Codex 不会
  自动关闭或更新来源工单。
- 要查找超出所提供积压项范围的漏洞，请执行以下操作：[运行安全
  扫描](/zh-Hans/codex/security/plugin/scans)。
