<!-- source: https://developers.openai.com/api/reference/cli/resources/realtime/subresources/calls/methods/accept/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Realtime](/api/reference/cli/resources/realtime)

[Calls](/api/reference/cli/resources/realtime/subresources/calls)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Accept call

$ openai realtime:calls accept

POST/realtime/calls/{call\_id}/accept

Accept an incoming SIP call and configure the realtime session that will
handle it.

##### ParametersExpand Collapse

--call-id: string

The identifier for the call provided in the
[`realtime.call.incoming`](https://platform.openai.com/docs/api-reference/webhook-events/realtime/call/incoming)
webhook.

--type: "realtime"

The type of session to create. Always `realtime` for the Realtime API.

--audio: optional object { input, output }

Configuration for input and output audio.

--include: optional array of "item.input\_audio\_transcription.logprobs"

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

--instructions: optional string

The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. “be extremely succinct”, “act friendly”, “here are examples of good responses”) and on audio behavior (e.g. “talk quickly”, “inject emotion into your voice”, “laugh frequently”). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

--max-output-tokens: optional number or "inf"

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

--model: optional string or "gpt-realtime" or "gpt-realtime-1.5" or "gpt-realtime-2" or 14 more

The Realtime model used for this session.

--output-modality: optional array of "text" or "audio"

The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

--parallel-tool-calls: optional boolean

Whether the model may call multiple tools in parallel. Only supported by
reasoning Realtime models such as `gpt-realtime-2`.

--prompt: optional object { id, variables, version }

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

--reasoning: optional object { effort }

Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.

--tool-choice: optional [ToolChoiceOptions](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) or [ToolChoiceFunction](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_function%20%3E%20(schema)) { name, type }  or [ToolChoiceMcp](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_mcp%20%3E%20(schema)) { server\_label, type, name }

How the model chooses tools. Provide one of the string modes or force a specific
function/MCP tool.

--tool: optional array of [RealtimeToolsConfigUnion](/api/reference/cli/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_tools_config_union%20%3E%20(schema))

Tools available to the model.

--tracing: optional "auto" or object { group\_id, metadata, workflow\_name }

Realtime API can write session traces to the [Traces Dashboard](https://platform.openai.com/logs?api=traces). Set to null to disable tracing. Once
tracing is enabled for a session, the configuration cannot be modified.

`auto` will create a trace for the session with default values for the
workflow name, group id, and metadata.

--truncation: optional "auto" or "disabled" or [RealtimeTruncationRetentionRatio](/api/reference/cli/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_truncation_retention_ratio%20%3E%20(schema)) { retention\_ratio, type, token\_limits }

When the number of tokens in a conversation exceeds the model’s input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model’s context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.

Clients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.

Truncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.

Truncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model’s input token limit.

### Accept call

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai realtime:calls accept \
  --api-key 'My API Key' \
  --call-id call_id \
  --type realtime

##### Returns Examples
