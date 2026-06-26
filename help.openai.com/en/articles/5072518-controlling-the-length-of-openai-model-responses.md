<!-- source: https://help.openai.com/en/articles/5072518-controlling-the-length-of-openai-model-responses -->

# Controlling the length of OpenAI model responses

Learn how to set output limits for OpenAI models using token settings, clear prompts, examples, and stop sequences.

Updated: 2 days ago

# Overview

Controlling the length of a model’s response is useful for several reasons: it helps manage cost (since you pay per token), improves latency/performance (shorter responses are returned faster), and ensures relevance by avoiding overly long or verbose outputs.  
  
You can achieve this using token caps, reasoning and verbosity settings, clear instructions, examples, and stop sequences. For the most current and complete details, always refer to the [official API reference on platform.openai.com.](https://platform.openai.com/docs/overview)

# Set a maximum output length

## Responses API

Used for GPT-5 models and most o-series models: use `max_output_tokens` to cap the number of tokens the model will generate. For `compaction_trigger` requests, either omit `max_output_tokens` or set it to at least `20000`; smaller values are rejected. The Responses API does not support multiple completions (`n`).

## Chat Completions API

Used for legacy GPT-3.5, GPT-4o, and sometimes o-series.

* For reasoning models like o3 and o4-mini, use `max_completion_tokens` (alias of `max_tokens`)
* For earlier/non-reasoning models, `max_tokens` still works
* Supports `stop` and `n` (multiple completions).

***Note:*** *There is no “minimum tokens” setting. If you need a minimum length, specify it in your prompt.*

## Token limits by model group

For up-to-date token limits, context sizes, and output caps, please reference the [specific model documentation](https://platform.openai.com/docs/models/).

## Quick examples

**Responses API**

```
{ "model": "gpt-5", "input": "Summarize the findings in ~80 words.", "max_output_tokens": 120 }
```

**Chat Completions (reasoning model)**

```
{ "model": "o3-mini", "messages": [{"role": "user", "content": "Write five one-line options."}], "max_completion_tokens": 100 }
```

# GPT-5 models specific controls: `verbosity` and `reasoning.effort`

These controls are **only available on GPT-5 models** (gpt-5.2, gpt-5.2-chat-latest, gpt-5.2 pro, etc. O-series and legacy models do not support them.

**`verbosity`** accepts `"low"`, `"medium"` (default), or `"high"`. It influences detail level but not hard limits.

```
{ "model": "gpt-5", "input": "Explain PageRank at a high level.", "text": { "verbosity": "low" }, "max_output_tokens": 200 }
```

**`reasoning.effort`** controls how many reasoning tokens are generated before producing an answer. GPT-5.2 supports `none,low`, `medium`, `high,and xhigh`. gpt-5.2-pro only supports `medium`, `high,and xhigh`. Earlier reasoning models support only `low`, `medium`, and `high`.

```
{ "model": "gpt-5", "input": "How much gold would it take to coat the Statue of Liberty in a 1mm layer?", "reasoning": { "effort": "minimal" } }
```

You can set **`reasoning.effort`** to `none` to make the model behave like a non-reasoning model for latency-sensitive use cases.

# Provide specific instructions

Ask for the exact length or shape you want. Examples:

* “List **exactly five** options.”
* “Write a **50-word** summary.”
* “No more than **100 tokens**. If you need more, say ‘Need more room.’”

# Use examples with consistent length

Few-shot examples that match your desired length help the model continue the pattern.

# Apply strategic stop sequences

Use `stop` to halt generation when the model reaches a delimiter or a numbered list boundary.

```
{ "stop": ["\n###", "6."] }
```

# Multiple candidates

* **Chat Completions:** `n` returns multiple completions in one call.
* **Responses API:** `n` is not supported; make multiple calls if you need more than one output.
