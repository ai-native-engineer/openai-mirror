<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/plugin/deep-scans -->

当您需要更全面的审查，并且可以接受较长的运行时间时，
请运行深度扫描。深度扫描会更全面地搜索代码仓库，
并可减少多次运行之间的结果差异。

先运行[标准扫描](/zh-Hans/codex/security/plugin/scans)，检查扫描范围
和结果。需要更全面的评估时，再使用深度扫描。

## 选择标准扫描或深度扫描

|                         | 标准扫描                                      | 深度扫描                                             |
| ----------------------- | -------------------------------------------------- | ----------------------------------------------------- |
| 最适合                | 首次运行，以及对代码仓库或文件夹进行常规审查 | 标准扫描后进行更全面的审查           |
| 结果差异性             | 标准                                           | 较低                                               |
| 范围                   | 代码仓库或明确指定的文件夹                      | 代码仓库或明确指定的文件夹                         |
| 运行时间和资源用量   | 较低                                              | 较高                                                |
| Pull Request 和代码差异 | 使用变更审查工作流程                     | 不支持；请改用变更审查工作流程 |

## 配置深度扫描的运行参数

要控制深度扫描的并发度和持续时间，请创建或编辑
`~/.codex/codex-security/config.toml`。如果您设置了 `CODEX_HOME`，请改用
`$CODEX_HOME/codex-security/config.toml`。

例如，此配置方案会运行一次耗时较短、并发度受限的扫描：

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

| 设置                         | 默认值 | 说明                                                                                                        |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| `workers`                       | `4`     | 允许同时运行的独立标准扫描工作器数量。旧版取值 `"auto"` 也会被解析为 `4`。 |
| `subagents`                     | `3`     | 每个工作器可启动的子智能体数量。设置为 `0` 可禁用子智能体。                                                |
| `stop_after_no_new`             | `4`     | 若工作器连续完成指定次数的扫描且均未产生新的发现项，则停止扫描。                                   |
| `stop_after_consecutive_errors` | `3`     | 工作器连续出错达到指定次数时停止扫描。                                                                    |
| `max_discovery_runs`            | `40`    | 限制汇总前独立标准扫描的运行次数。                                             |
| `max_time_hours`                | `96`    | 将工作器的运行时长设为正数，且不得超过 `96` 小时；可按需使用小数。                          |

设置较低的值可以缩短扫描时间并减少 Token 用量，但可能遗漏发现项。
配置更改仅适用于新的深度扫描，不适用于正在进行的扫描。

达到时间限制后，Codex Security 会停止尚未完成的工作器，保留
已完成的扫描结果，并将其汇总到最终报告中。如果没有工作器
在截止时间前完成源代码审查，报告将记录部分
覆盖情况。

`max_time_hours` 设置要求插件版本为 `0.1.19` 或更高版本。有关发布详情，请参阅
[插件更新日志](/zh-Hans/codex/security/plugin/changelog)。

## 启动深度扫描

在桌面应用中，打开 **安全**，选择 **扫描**，再选择 **+ 扫描**。
选择代码仓库或其他文件夹，选择 **代码库**，然后开启
**深度扫描**。扫描会覆盖所选代码仓库或文件夹的全部内容。

您还可以通过 Codex 对话启动针对整个代码仓库的深度扫描：

```text
Use $codex-security:deep-security-scan to run a deep security scan of this repository.

若要扫描单体代码仓库中的某个组件，请明确指定文件夹：

```text
Use $codex-security:deep-security-scan to run a deep security scan of /absolute/path/to/repository/services/payments.

要在桌面应用中运行限定范围的深度扫描，请将相应文件夹选为代码库。
扫描会覆盖所选文件夹的全部内容。

## 确认设置并完成预检

为获得最佳扫描质量，请使用 <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>
并将推理强度设置为 `xhigh`。

1. 选择 **代码库** 并开启 **深度扫描**。
2. 确认代码仓库或所选文件夹正是您要
扫描的代码范围。
3. 选择模型和推理强度。
4. 打开 **其他上下文** ，补充具体的攻击向量、敏感
   应用区域，或代码无法体现的代码仓库上下文。
5. 选择 **开始扫描**。

深度扫描工作器会继承您选择的模型和推理设置。每个
工作器都会运行一次完整的标准扫描，Codex Security 会汇总
已完成的结果。在 **扫描**中跟踪已保存的扫描，或选择 **查看
活动** 来检查对应的 Codex 任务。请先查看[插件
更新日志](/zh-Hans/codex/security/plugin/changelog)，再更新插件或
启动长时间运行的扫描。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    跟踪正在进行的深度扫描阶段，并检查对应的 Codex 活动，
然后再审查已完成的结果。
  </figcaption>
</figure>

## 审查结果

深度扫描使用与
标准扫描相同的已保存扫描详情和完整扫描目录。在 **扫描** 中打开已完成的扫描，或在
**发现项**中审查其发现项。如果您请求相应输出，生成的 `report.md` 会链接到详细的漏洞报告
或结构加固指南。
共享或归档结果时，请将报告链接的 `findings/` 和 `hardening/` 目录
与报告一并保留。

审查发现项之前，请先审查覆盖范围摘要。即使是深度扫描也有局限，
因此在得出
结论之前，请检查延后处理的攻击面和剩余的证据缺口。对于您接受的发现项，请继续[修复并验证
发现项](/zh-Hans/codex/security/plugin/fix-findings)。

如需审查 Pull Request、提交、分支范围或本地补丁，请使用[审查代码
变更](/zh-Hans/codex/security/plugin/code-changes)。深度扫描不能替代
专注于代码差异的工作流程。
