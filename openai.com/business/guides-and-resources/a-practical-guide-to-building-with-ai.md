<!-- source: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-with-ai/ -->

# A practical guide to building with GPT‑5

Proven startup strategies to migrate, prompt, and scale with OpenAI’s newest frontier model.

[Try ChatGPT(opens in a new window)](https://chat.openai.com/)[Contact sales](/contact-sales/)

## Meet GPT‑5: our most powerful, most steerable model yet.

Built for the full spectrum of coding and agentic tasks, GPT‑5 is faster, smarter, and more adaptable than anything we’ve released before. Its greatest strength is how responsive it is to your direction, making it easier than ever to shape behavior for your specific use case.

But here’s the catch: every new model ‘thinks’ a little differently. Prompts that worked with GPT‑4.1 or other models won’t always translate directly. To unlock GPT‑5’s full potential, you’ll need to refine your prompts and tailor them to its unique behaviors and personality.

Our newest flagship model represents a major leap forward in what startups can accomplish, both due to its state-of-the-art performance (74.9% on SWE-bench Verified) and the controls developers have to steer and shape behavior. GPT‑5 excels at agentic and multi-step reasoning tasks where reliability, depth, and control matter: parsing complex inputs, orchestrating tool use, or managing multi-stage workflows. Beyond agentic use cases, whether you’re refining natural language interfaces, powering developer tools, generating structured outputs, or automating complex business processes, GPT‑5 delivers higher accuracy, better consistency, and more predictable behavior than any previous model.

---

### What we’ll cover in this guide

In this guide, we’ll share proven techniques to get the most out of GPT‑5 based on our work with leading startups with technical resources and actionable steps to get started.

1. **Migrate:** Steps to migrate to the Responses API, designed for long-term scale, speed, and new reasoning capabilities.
2. **Optimize:** Techniques to develop strong prompting that help you move faster and reduce engineering overhead.
3. **Steer:** New controls let you guide how the model reasons and communicates to match effort and output based on task complexity.
4. **Troubleshoot:** Resources to avoid common pitfalls like overthinking or overly verbose answers.

By the end of this guide, you should understand how to leverage GPT‑5 to its full potential to unlock more consistent, predictable, and accurate behavior while optimizing costs.

---

## Step 01: Migrate to the Responses API

Your first step to unlocking GPT‑5’s full intelligence is to build on the infrastructure designed for it. Only the Responses API allows the model to persist its chains of thought (reasoning items) across turns and tool calls, either with OpenAI managing state or by passing back encrypted reasoning items.

This means every request to the model has access to its complete internal context, significantly boosting performance and improving caching to lower costs—capabilities the Chat Completions API simply doesn’t support.

##### Velocity

Smarter tool use and built-in state management reduce glue code and orchestration. You ship faster with fewer engineers and focus more time on your product and customers.

##### Scale without drag

Full-context reasoning plus faster performance and higher cache-hit rates lower infrastructure costs and latency as you grow. With zero-data retention (ZDR) compatibility, you’re not locked into today’s deployment pattern—you’re ready for the agentic workflows that will define tomorrow’s applications.

##### Future-proofing

The Responses API is the path forward for new reasoning capabilities. Building here keeps you off legacy APIs when the most powerful features ship and aligns your codebase with where OpenAI is investing most heavily, giving you long-term stability as the ecosystem evolves.

The Responses API is the unified surface for working with GPT‑5. To maximize performance and future-proof your startup, we highly recommend moving workflows to the Responses API today.

![Screenshot of a tweet by Greg Brockman (@gdb), verified, that says “try using Responses API with gpt-5:” and quotes a tweet from Shen Zhuoran (@CMS_Flash), verified, dated Aug 18. The quoted tweet reads: “Man it’s crazy how BIG a difference it makes for GPT-5 just by switching from Completions API to Responses API. We’re cooking @augmentcode.” The tweet shows a timestamp of 10:04 AM · Aug 19, 2025.](https://images.ctfassets.net/kftzwdyauwt9/DESfDyAgvsjMjmQBLKkaj/0148090e354cc9f5cb737f274a3b6ce7/Twitter.png?w=3840&q=90&fm=webp)

###### Getting started with Responses API

[### Responses API

Why we build the Responses API.

Learn more](https://developers.openai.com/blog/responses-api)

[### Reasoning Models on the Responses API

Instructions on passing reasoning tokens, caching, and unlocking more intelligence.

Learn more](https://cookbook.openai.com/examples/responses_api/reasoning_items)

[### Migration Guide

Step-by-step instructions to move from Completions to Responses.

Learn more](https://platform.openai.com/docs/guides/migrate-to-responses#page-top)

[### Codex CLI Toolkit

Open-sourced tools to automate and streamline migration.

Learn more](https://github.com/openai/completions-responses-migration-pack)

[### Build Hour Demo

See GPT-5 in action on the Responses API.

Learn more](https://www.youtube.com/watch?feature=shared&t=304&v=ITMouQ_EuXI&themeRefresh=1)

---

## Step 02: Optimize prompting

Moving to GPT‑5 isn’t just about adopting a new model – it’s about mastering how to optimize it. Startups that develop strong prompting practices move faster, spend less on engineering overhead, and create products that feel meaningfully better to users.

![Screenshot of a tweet by alex duffy (@alxai_), verified. The tweet says that good prompting is more important with GPT-5 because it is highly steerable: mediocre prompts give worse results, great prompts give better ones. It notes a performance gap for GPT-5 with minimal reasoning, with optimized prompts shown in red and baseline in gray. Below the text is a dark-themed box-and-whisker chart titled “Model Performance as France,” showing multiple model configurations along the x-axis and game score on the y-axis. Red (optimized) distributions generally appear higher than gray (baseline), highlighting performance differences, with some model groups outlined for emphasis.](https://images.ctfassets.net/kftzwdyauwt9/76Jw7jCUMiZ2dLaQGm70Nw/fb792962120058aaf1c5fed4d2292d6d/Twitter_Alex_Duffy.png?w=3840&q=90&fm=webp)

##### Start with evals

Begin by running your existing prompts as is against your evals to establish a baseline and see where outputs diverge from expectations.

##### Inspect the model’s reasoning

For specific failure cases, loop the eval again and stream reasoning summaries with GPT‑5 in the Responses API. Watching the model reason helps you pinpoint where it needs more steering.

##### Metaprompt and simplify

GPT‑5 is skilled at metaprompting—use the model to improve its own prompts as you iterate. Often, it requires less scaffolding than older models; shorter, clearer instructions can perform better.

##### Template and document

When prompts work reliably, lock them into reusable templates or a prompt library. Document what good vs. bad outputs look like so the team can build consistently, and revisit periodically as techniques evolve.

###### Getting started with prompt optimization

[### GPT-5 Prompting Guide

Best practices for crafting powerful prompts

Learn more](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide)

[### Building Hour Demo

Live example of GPT-5 in action

Learn more](https://www.youtube.com/watch?v=ITMouQ_EuXI&t=1528s)

[### Prompt Optimization Tool

Interactive playground to refine prompts

Learn more](https://platform.openai.com/chat/edit?models=gpt-5&optimize=true)

---

## Step 03: Steer GPT‑5 with reasoning, verbosity, and new capabilities

GPT‑5 introduces new controls that let you fine-tune how the model reasons and communicates. These capabilities help startups match model effort and output to the unique complexity of their products.

##### Reasoning effort

`reasoning_effort` controls how much the model thinks (and how readily it calls tools). The default is `medium;` options are `minimal`, `low`, `medium`, and `high`. Experiment to right-size effort to the complexity of your task and measure against your evals using the [prompting guide⁠(opens in a new window)](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide).

##### Verbosity

`verbosity` influences the length of the model’s output. Options are `low`, `medium`, and `high`. You can also add prompt instructions for scenarios where you want the model to override the default.

##### Experimentation guidance

GPT‑5 is highly steerable. These parameters give you more control over model behavior. There’s no single deterministic best configuration - systematically experiment and evaluate to identify what works best for your use case.

###### New & enhanced capabilities

[### GPT-5 Build Hour

Live coding session showcasing GPT-5 capabilities.

Learn more](https://youtu.be/ITMouQ_EuXI?feature=shared&t=151)

[### Using GPT-5

Quick guide to get started and build effectively.

Learn more](https://platform.openai.com/docs/guides/latest-model#page-top)

[### New parameters and tools

Overview of the latest features and settings.

Learn more](https://cookbook.openai.com/examples/gpt-5/gpt-5_new_params_and_tools)

[### Preambles

Tips for setting strong context in prompts.

Learn more](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide#tool-preambles)

[### Latency optimization

Techniques to speed up responses.

Learn more](https://platform.openai.com/docs/guides/latency-optimization#page-top)

[### Cost optimization

Strategies to reduce usage costs.

Learn more](https://platform.openai.com/docs/guides/cost-optimization#page-top)

---

## Step 04: Troubleshoot using common patterns

From working closely with hundreds of startups, we see recurring issues such as overthinking, underthinking, over-deference, overly verbose outputs, latency problems (see [Latency Optimization⁠(opens in a new window)](https://platform.openai.com/docs/guides/latency-optimization#page-top)), tool overuse, and malformed tool calls. Because GPT‑5 is highly steerable and eager to follow instructions, careful prompt tuning—paired with solid evals and metaprompting—resolves most of these quickly. For deeper guidance on diagnosing and correcting each pattern, explore the [GPT‑5 Troubleshooting Cookbook⁠(opens in a new window)](https://cookbook.openai.com/examples/gpt-5/gpt-5_troubleshooting_guide).

---

### About the authors

This guide was developed by [Hillary Bush⁠(opens in a new window)](https://www.linkedin.com/in/hillarybush/), Startups Account Director, and [Prashant Mital⁠(opens in a new window)](https://www.linkedin.com/in/pmital/), Startup Solutions Architect, based on their experience working with top startups leveraging GPT‑5.

They created this guide after helping dozens of early-stage and growth-stage startups adopt GPT‑5 in production, seeing consistent patterns in how the most successful teams migrated APIs, tuned prompts, and used new reasoning controls to ship faster and build stronger products.

The goal of the OpenAI Startups Team is to share these best practices broadly so any startup, whether pre-seed or scaling globally, can accelerate its journey from idea to impact with GPT‑5. We hope you found this guide useful – happy building!

## Interested in bringing AI to your business?

Learn how we help companies build scalable, responsible AI strategies.

[Try ChatGPT](https://chatgpt.com/)[Contact sales](/contact-sales/)

## Sources cited

* [Greg Brockman @gdb, X⁠(opens in a new window)](https://x.com/gdb/status/1957851156564042012)
* [Alex Duffy @alxai\_, X⁠(opens in a new window)](https://x.com/alxai_/status/1955082871426748638)

## Keep reading

![How agents are transforming work > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7hmtkjKv0DxS4Yt8mQZju2/c168bfa2010da64bcc9dd60d6b5491e8/Art_Card__1_.png?w=3840&q=90&fm=webp)

[How agents are transforming work

CompanyJun 25, 2026](/index/how-agents-are-transforming-work/)

![OpenAI and Broadcom Jalapeño inference chip card image](https://images.ctfassets.net/kftzwdyauwt9/21KcazqOHUF7Cq71Hpfcnc/81ad98a1978845b441ab14e008168c75/openai-broadcom-jalapeno-inference-chip-image-1_1.png?w=3840&q=90&fm=webp)

[OpenAI and Broadcom unveil LLM-optimized inference chip

CompanyJun 24, 2026](/index/openai-broadcom-jalapeno-inference-chip/)

![Helping build shared standards for advanced AI - card image](https://images.ctfassets.net/kftzwdyauwt9/3tqr0Vb3JnK38uBRBw7FAF/a3989888ee148ba286b834076aaa289b/helping-build-shared-standards-for-advanced-ai-1_1.png?w=3840&q=90&fm=webp)

[Helping build shared standards for advanced AI

Global AffairsJun 23, 2026](/index/helping-build-shared-standards-for-advanced-ai/)
