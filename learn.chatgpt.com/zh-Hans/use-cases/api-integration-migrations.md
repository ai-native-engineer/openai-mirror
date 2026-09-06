<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/api-integration-migrations -->

## 简介

随着我们发布新模型和 API 功能，建议您升级集成，以便享受最新改进。
从一个模型切换到另一个模型，通常并非只需更新模型名称那么简单。

API 可能会发生变化。例如，针对 GPT-5.4 模型，我们为助手消息新增了 `phase` 参数，集成时应注意包含该参数。更重要的是，模型行为可能有所不同，需要您修改现有提示词。

迁移到新模型时，您不仅应完成必要的代码修改，还应评估迁移对工作流的影响。

## 使用 OpenAI 文档技能

[模型指南](/api/docs/guides/latest-model)页面汇集了针对各代模型的 API 功能、模型行为、迁移和提示词指南。

OpenAI 文档技能还提供了[具体指导](https://github.com/openai/codex/blob/6323f0104d17d211029faab149231ba787f7da37/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-5p4.md)，可作为迁移的具体参考。有关当前的升级目标，请参阅[模型指南](/api/docs/guides/latest-model)页面。

Codex 现已默认内置 OpenAI 文档技能，因此，使用 OpenAI API 进行开发时，请务必在提示词中提及该技能，以获取所有最新文档和指南。

## 构建稳健的评测流水线

Codex 可根据最新的提示词指南自动更新您的提示词，但您还应建立自动验证机制，确认集成是否按预期运行。

请务必构建一条评测流水线，以便每次修改集成时都能运行，验证行为未发生回归。

这篇[Cookbook 指南](/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel)详细介绍了如何使用我们的 [Evals API](/api/docs/guides/evals) 实现这一点。
