<!-- source: https://openai.com/index/better-prompt-caching-for-gpt-6/ -->

September 22, 2026

[Product](/news/product-releases/)

# Better prompt caching for GPT‑6

Higher cache hit rates and new tools to help persistent agents run faster and cost less.

Loading…

Share

GPT‑6 enables persistent agents to work for hours on complex tasks, from refactoring codebases to producing well-researched documents and presentations. The applications behind these agents make a series of API requests that build on one another, often carrying forward the same instructions, tool definitions, and context from earlier turns. OpenAI caches that shared context to reuse computation across requests, reducing response times and giving developers discounts of up to 90% on cached input tokens.

With the GPT‑6 family, we launched an improved prompt caching system that delivers higher cache hit rates by default. We now give cache discounts for eligible shared prefixes reused within a 30-minute window. We’re also introducing new tools to help developers monitor cache performance, diagnose misses, and choose how much of a prompt to cache.

> “OpenAI’s prompt caching plays a critical role in helping GitHub Copilot deliver fast, efficient experiences at scale. Over the past several months, we’ve reduced by more than 50% the share of prompt tokens requiring fresh processing across billions of requests to OpenAI models, relative to our previous baseline. The result is a more efficient inference stack and faster time to first response for developers.”

—Mario Rodriguez, Chief Product Officer

## Monitor caching and diagnose cache misses

The new [Prompt Caching Dashboard⁠(opens in a new window)](https://platform.openai.com/usage?usage_section=prompt-caching) shows how much of your application’s input is served from cache. Track hit rates over time and use the input composition chart to compare cached and uncached tokens. These views help you spot drops in cache hits and evaluate how changes to your application impact caching performance.

![Prompt caching dashboard showing cache hit rate, cache performance over time, and input token composition.](https://images.ctfassets.net/kftzwdyauwt9/29DVnNtIz2bkMRa1wWULXs/062723af9185edeb09c27071e68b589d/image__17_.png?w=3840&q=90&fm=webp)

When you see an unexpected cache miss, use the [prompt caching diagnostics tool⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching/diagnostics) to understand what happened. Compare a request with a recent response to identify changes to the model, tools, settings, or input that prevented reuse. The estimated number of affected tokens helps you assess the size of the impact and decide how you can optimize your integration to maximize cache hit rates.

```
{
  "prompt_cache_diagnostics": {
    "type": "cache_miss",
    "reason": "tools_changed",
    "comparison_reusable_tokens": 5629,
    "cache_missed_tokens": 5629
  }
}
```

## Optimize caching for your application

**Choose what to cache.** Explicit cache breakpoints let you choose which prompt prefixes to reuse. The refreshed [prompt caching guide⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching) explains how to use them, how long cached prefixes remain eligible, and how changes to tools and inputs affect reuse.

**Adjust reasoning effort without breaking cache.** On GPT‑6 models, you can now [change reasoning effort⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/reasoning?api-mode=responses#change-reasoning-mid-conversation) between responses without breaking cache. Raise effort for a harder task or lower it for a routine follow-up by appending a `configuration_update` while leaving request-level reasoning effort unchanged. This lets you adjust how much reasoning a task needs while preserving reusable context.

**Preserve cache as tools and instructions change.** As your agent’s tool use needs change, keep tool definitions, schemas, and ordering stable so earlier context stays reusable. Use `allowed_tools` to make only the relevant tools callable, or set tool\_choice to none when no tools are needed, instead of removing definitions. Use new developer messages to append new instructions towards the end of the context to override older ones. See our [guidance on managing tool changes⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching#manage-tools-with-append-only-updates).

**Prewarm the cache to reduce latency.** [Prewarming⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching#prewarm-the-cache) prepares known context ahead of time so the model can start responding sooner when a request arrives. For example, an application can prewarm shared instructions, tool definitions, or reference material during startup, before the user asks their first question. This moves processing out of the user’s wait time.

These optional controls build on the engine’s default performance, helping you tailor caching to your workload.

1 of 3

> “OpenAI’s prompt caching diagnostics and dashboard helped us improve cache hit rates by a few percentage points, reducing costs by 20%. We now get alerts when caching breaks unexpectedly and use Codex agents to diagnose the root cause. Explicit breakpoints also let us cache stable context while keeping frequently changing content at the end of the prompt. That’s made it economically viable to fork conversations for background tasks while reusing nearly all of the shared context.”

—Arian Hanifi, Chief Technology Officer

> “For long-running agents like Manus, reliable caching is fundamental to the economics. Working with OpenAI's engineering team, we refined cache breakpoint placement, combined explicit and automatic caching, and used real requests to pinpoint unexpected cache misses. In less than a week, our OpenAI model cache hit rate went from roughly 85% to consistently above 90%, further lowering inference costs in production. The progress came through a series of targeted improvements, with both teams validating the results along the way.”

—Bin Fan, Agent Team Lead

> “Working with OpenAI, we moved our session agents to explicit cache breakpoints. In under a week, cache hit rates on our evaluations rose from 83% to 91%. This meant fewer cache writes and lower inference costs with the same workload; the cache writes fell by roughly two-thirds, and inference costs by 36%.”

—Eugene Mikhantyev, AI Engineer

* Strawberry Browser
* Manus
* Wordsmith

* Strawberry Browser
* Manus
* Wordsmith

## Get started

* Monitor cache hit rates in the [Prompt Caching Dashboard⁠(opens in a new window)](https://platform.openai.com/usage?usage_section=prompt-caching).
* Investigate unexpected misses with the [diagnostics tool⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching/diagnostics).
* Follow the [prompt caching guide⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching) to improve your setup, or [use Codex⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching#how-to-optimize-prompt-caching) to review your code, apply improvements, and measure results.

* [API](/news/?tags=api)
* [2026](/news/?tags=2026)

## Author

## Keep reading

[View all](/news/)

![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c5675cb7525bcccbe8c5580/gpt-6-sol-luna-art.png?w=3840&q=90&fm=webp)

[Introducing GPT-6 Sol and Luna

ProductSep 22, 2026](/index/introducing-gpt-6-sol-and-luna/)

![Reimagining advertising with AI — Card cover](https://images.ctfassets.net/kftzwdyauwt9/fHwkKLVG8WFHvuUPqMXtz/1c49ba0859fe1e1e21f5d64f692490f5/reimagining-advertising-with-ai-cover.png?w=3840&q=90&fm=webp)

[Reimagining advertising with AI

ProductSep 16, 2026](/index/reimagining-advertising-with-ai/)

![How to connect AI usage to business value — art card](https://images.ctfassets.net/kftzwdyauwt9/36T42HPkipcJAs08yNirmR/f73d9408ef4f0b08b5cce3b839656843/cover-018.png?w=3840&q=90&fm=webp)

[How to connect AI usage to business value

ProductSep 16, 2026](/index/how-to-connect-ai-usage-to-business-value/)
