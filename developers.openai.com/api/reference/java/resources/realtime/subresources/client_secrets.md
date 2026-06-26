<!-- source: https://developers.openai.com/api/reference/java/resources/realtime/subresources/client_secrets/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Realtime](/api/reference/java/resources/realtime)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Client Secrets

##### [Create client secret](/api/reference/java/resources/realtime/subresources/client_secrets/methods/create)

[ClientSecretCreateResponse](/api/reference/java/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20ClientSecretCreateResponse%20%3E%20(schema)) realtime().clientSecrets().create(ClientSecretCreateParamsparams = ClientSecretCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/realtime/client\_secrets

##### ModelsExpand Collapse

class RealtimeSessionCreateResponse:

A Realtime session configuration object.

String id

Unique identifier for the session that looks like `sess_1234567890abcdef`.

JsonValue; object\_ "realtime.session"constant"realtime.session"constant

The object type. Always `realtime.session`.

JsonValue; type "realtime"constant"realtime"constant

The type of session to create. Always `realtime` for the Realtime API.

Optional<Audio> audio

Configuration for input and output audio.

Optional<Input> input

Optional<[RealtimeAudioFormats](/api/reference/java/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))> format

The format of the input audio.

Optional<NoiseReduction> noiseReduction

Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

Optional<[NoiseReductionType](/api/reference/java/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))> type

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

Optional<[AudioTranscription](/api/reference/java/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema))> transcription

Optional<TurnDetection> turnDetection

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with “uhhm”, the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

For `gpt-realtime-whisper` transcription sessions, turn detection must be
set to `null`; VAD is not supported.

One of the following:

class ServerVad:

Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.

JsonValue; type "server\_vad"constant"server\_vad"constant

Type of turn detection, `server_vad` to turn on simple Server VAD.

Optional<Boolean> createResponse

Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

Optional<Long> idleTimeoutMs

Optional timeout after which a model response will be triggered automatically. This is
useful for situations in which a long pause from the user is unexpected, such as a phone
call. The model will effectively prompt the user to continue the conversation based
on the current context.

The timeout value will be applied after the last model response’s audio has finished playing,
i.e. it’s set to the `response.done` time plus audio playback duration.

An `input_audio_buffer.timeout_triggered` event (plus events
associated with the Response) will be emitted when the timeout is reached.
Idle timeout is currently only supported for `server_vad` mode.

minimum5000

maximum30000

Optional<Boolean> interruptResponse

Whether or not to automatically interrupt (cancel) any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

Optional<Long> prefixPaddingMs

Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

Optional<Long> silenceDurationMs

Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

Optional<Double> threshold

Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

class SemanticVad:

Server-side semantic turn detection which uses a model to determine when the user has finished speaking.

JsonValue; type "semantic\_vad"constant"semantic\_vad"constant

Type of turn detection, `semantic_vad` to turn on Semantic VAD.

Optional<Boolean> createResponse

Whether or not to automatically generate a response when a VAD stop event occurs.

Optional<Eagerness> eagerness

Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Boolean> interruptResponse

Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

Optional<Output> output

Optional<[RealtimeAudioFormats](/api/reference/java/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))> format

The format of the output audio.

Optional<Double> speed

The speed of the model’s spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it’s
also possible to prompt the model to speak faster or slower.

maximum1.5

minimum0.25

Optional<Voice> voice

The voice the model uses to respond. Voice cannot be changed during the
session once the model has responded with audio at least once. Current
voice options are `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`,
`shimmer`, `verse`, `marin`, and `cedar`. We recommend `marin` and `cedar` for
best quality.

One of the following:

ALLOY("alloy")

ASH("ash")

BALLAD("ballad")

CORAL("coral")

ECHO("echo")

SAGE("sage")

SHIMMER("shimmer")

VERSE("verse")

MARIN("marin")

CEDAR("cedar")

Optional<Long> expiresAt

Expiration timestamp for the session, in seconds since epoch.

formatunixtime

Optional<List<Include>> include

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

Optional<String> instructions

The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. “be extremely succinct”, “act friendly”, “here are examples of good responses”) and on audio behavior (e.g. “talk quickly”, “inject emotion into your voice”, “laugh frequently”). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

Optional<MaxOutputTokens> maxOutputTokens

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

One of the following:

long

JsonValue;

Optional<Model> model

The Realtime model used for this session.

One of the following:

GPT\_REALTIME("gpt-realtime")

GPT\_REALTIME\_1\_5("gpt-realtime-1.5")

GPT\_REALTIME\_2("gpt-realtime-2")

GPT\_REALTIME\_2025\_08\_28("gpt-realtime-2025-08-28")

GPT\_4O\_REALTIME\_PREVIEW("gpt-4o-realtime-preview")

GPT\_4O\_REALTIME\_PREVIEW\_2024\_10\_01("gpt-4o-realtime-preview-2024-10-01")

GPT\_4O\_REALTIME\_PREVIEW\_2024\_12\_17("gpt-4o-realtime-preview-2024-12-17")

GPT\_4O\_REALTIME\_PREVIEW\_2025\_06\_03("gpt-4o-realtime-preview-2025-06-03")

GPT\_4O\_MINI\_REALTIME\_PREVIEW("gpt-4o-mini-realtime-preview")

GPT\_4O\_MINI\_REALTIME\_PREVIEW\_2024\_12\_17("gpt-4o-mini-realtime-preview-2024-12-17")

GPT\_REALTIME\_MINI("gpt-realtime-mini")

GPT\_REALTIME\_MINI\_2025\_10\_06("gpt-realtime-mini-2025-10-06")

GPT\_REALTIME\_MINI\_2025\_12\_15("gpt-realtime-mini-2025-12-15")

GPT\_AUDIO\_1\_5("gpt-audio-1.5")

GPT\_AUDIO\_MINI("gpt-audio-mini")

GPT\_AUDIO\_MINI\_2025\_10\_06("gpt-audio-mini-2025-10-06")

GPT\_AUDIO\_MINI\_2025\_12\_15("gpt-audio-mini-2025-12-15")

Optional<List<OutputModality>> outputModalities

The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

One of the following:

TEXT("text")

AUDIO("audio")

Optional<[ResponsePrompt](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20response_prompt%20%3E%20(schema))> prompt

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

Optional<[RealtimeReasoning](/api/reference/java/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning%20%3E%20(schema))> reasoning

Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.

Optional<ToolChoice> toolChoice

How the model chooses tools. Provide one of the string modes or force a specific
function/MCP tool.

One of the following:

enum ToolChoiceOptions:

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

NONE("none")

AUTO("auto")

REQUIRED("required")

class ToolChoiceFunction:

Use this option to force the model to call a specific function.

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

For function calling, the type is always `function`.

class ToolChoiceMcp:

Use this option to force the model to call a specific tool on a remote MCP server.

String serverLabel

The label of the MCP server to use.

JsonValue; type "mcp"constant"mcp"constant

For MCP tools, the type is always `mcp`.

Optional<String> name

The name of the tool to call on the server.

Optional<List<Tool>> tools

Tools available to the model.

One of the following:

class RealtimeFunctionTool:

Optional<String> description

The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

Optional<String> name

The name of the function.

Optional<JsonValue> parameters

Parameters of the function in JSON Schema.

Optional<Type> type

The type of the tool, i.e. `function`.

class McpTool:

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

One of the following:

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

One of the following:

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

Optional<Tracing> tracing

Realtime API can write session traces to the [Traces Dashboard](https://platform.openai.com/logs?api=traces). Set to null to disable tracing. Once
tracing is enabled for a session, the configuration cannot be modified.

`auto` will create a trace for the session with default values for the
workflow name, group id, and metadata.

One of the following:

JsonValue;

class TracingConfiguration:

Granular configuration for tracing.

Optional<String> groupId

The group id to attach to this trace to enable filtering and
grouping in the Traces Dashboard.

Optional<JsonValue> metadata

The arbitrary metadata to attach to this trace to enable
filtering in the Traces Dashboard.

Optional<String> workflowName

The name of the workflow to attach to this trace. This is used to
name the trace in the Traces Dashboard.

Optional<[RealtimeTruncation](/api/reference/java/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_truncation%20%3E%20(schema))> truncation

When the number of tokens in a conversation exceeds the model’s input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model’s context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.

Clients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.

Truncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.

Truncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model’s input token limit.

class RealtimeTranscriptionSessionCreateResponse:

A Realtime transcription session configuration object.

String id

Unique identifier for the session that looks like `sess_1234567890abcdef`.

String object\_

The object type. Always `realtime.transcription_session`.

JsonValue; type "transcription"constant"transcription"constant

The type of session. Always `transcription` for transcription sessions.

Optional<Audio> audio

Configuration for input audio for the session.

Optional<Input> input

Optional<[RealtimeAudioFormats](/api/reference/java/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))> format

The PCM audio format. Only a 24kHz sample rate is supported.

Optional<NoiseReduction> noiseReduction

Configuration for input audio noise reduction.

Optional<[NoiseReductionType](/api/reference/java/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))> type

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

Optional<[AudioTranscription](/api/reference/java/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema))> transcription

Optional<[RealtimeTranscriptionSessionTurnDetection](/api/reference/java/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20realtime_transcription_session_turn_detection%20%3E%20(schema))> turnDetection

Configuration for turn detection. Can be set to `null` to turn off. Server
VAD means that the model will detect the start and end of speech based on
audio volume and respond at the end of user speech. For `gpt-realtime-whisper`, this must be `null`; VAD is not supported.

Optional<Long> expiresAt

Expiration timestamp for the session, in seconds since epoch.

formatunixtime

Optional<List<Include>> include

Additional fields to include in server outputs.

* `item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

class RealtimeTranscriptionSessionTurnDetection:

Configuration for turn detection. Can be set to `null` to turn off. Server
VAD means that the model will detect the start and end of speech based on
audio volume and respond at the end of user speech. For `gpt-realtime-whisper`, this must be `null`; VAD is not supported.

Optional<Long> prefixPaddingMs

Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

Optional<Long> silenceDurationMs

Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

Optional<Double> threshold

Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

Optional<String> type

Type of turn detection, only `server_vad` is currently supported.
