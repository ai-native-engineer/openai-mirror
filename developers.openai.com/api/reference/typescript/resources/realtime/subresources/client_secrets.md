<!-- source: https://developers.openai.com/api/reference/typescript/resources/realtime/subresources/client_secrets/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Realtime](/api/reference/typescript/resources/realtime)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Client Secrets

##### [Create client secret](/api/reference/typescript/resources/realtime/subresources/client_secrets/methods/create)

client.realtime.clientSecrets.create(ClientSecretCreateParams { expires\_after, session } body, RequestOptionsoptions?): [ClientSecretCreateResponse](/api/reference/typescript/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20client_secret_create_response%20%3E%20(schema)) { expires\_at, session, value }

POST/realtime/client\_secrets

##### ModelsExpand Collapse

RealtimeSessionCreateResponse { id, object, type, 13 more }

A Realtime session configuration object.

id: string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

object: "realtime.session"

The object type. Always `realtime.session`.

type: "realtime"

The type of session to create. Always `realtime` for the Realtime API.

audio?: Audio { input, output }

Configuration for input and output audio.

input?: Input { format, noise\_reduction, transcription, turn\_detection }

format?: [RealtimeAudioFormats](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the input audio.

noise\_reduction?: NoiseReduction { type }

Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

type?: [NoiseReductionType](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

transcription?: [AudioTranscription](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)) { delay, language, model, prompt }

turn\_detection?: ServerVad { type, create\_response, idle\_timeout\_ms, 4 more }  | SemanticVad { type, create\_response, eagerness, interrupt\_response }  | null

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with “uhhm”, the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

For `gpt-realtime-whisper` transcription sessions, turn detection must be
set to `null`; VAD is not supported.

One of the following:

ServerVad { type, create\_response, idle\_timeout\_ms, 4 more }

Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.

type: "server\_vad"

Type of turn detection, `server_vad` to turn on simple Server VAD.

create\_response?: boolean

Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

idle\_timeout\_ms?: number | null

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

interrupt\_response?: boolean

Whether or not to automatically interrupt (cancel) any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

prefix\_padding\_ms?: number

Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

silence\_duration\_ms?: number

Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

threshold?: number

Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

SemanticVad { type, create\_response, eagerness, interrupt\_response }

Server-side semantic turn detection which uses a model to determine when the user has finished speaking.

type: "semantic\_vad"

Type of turn detection, `semantic_vad` to turn on Semantic VAD.

create\_response?: boolean

Whether or not to automatically generate a response when a VAD stop event occurs.

eagerness?: "low" | "medium" | "high" | "auto"

Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.

One of the following:

"low"

"medium"

"high"

"auto"

interrupt\_response?: boolean

Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

output?: Output { format, speed, voice }

format?: [RealtimeAudioFormats](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the output audio.

speed?: number

The speed of the model’s spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it’s
also possible to prompt the model to speak faster or slower.

maximum1.5

minimum0.25

voice?: (string & {}) | "alloy" | "ash" | "ballad" | 7 more

The voice the model uses to respond. Voice cannot be changed during the
session once the model has responded with audio at least once. Current
voice options are `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`,
`shimmer`, `verse`, `marin`, and `cedar`. We recommend `marin` and `cedar` for
best quality.

One of the following:

(string & {})

"alloy" | "ash" | "ballad" | 7 more

"alloy"

"ash"

"ballad"

"coral"

"echo"

"sage"

"shimmer"

"verse"

"marin"

"cedar"

expires\_at?: number

Expiration timestamp for the session, in seconds since epoch.

formatunixtime

include?: Array<"item.input\_audio\_transcription.logprobs">

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

instructions?: string

The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. “be extremely succinct”, “act friendly”, “here are examples of good responses”) and on audio behavior (e.g. “talk quickly”, “inject emotion into your voice”, “laugh frequently”). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

max\_output\_tokens?: number | "inf"

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

One of the following:

number

"inf"

"inf"

model?: (string & {}) | "gpt-realtime" | "gpt-realtime-1.5" | "gpt-realtime-2" | 14 more

The Realtime model used for this session.

One of the following:

(string & {})

"gpt-realtime" | "gpt-realtime-1.5" | "gpt-realtime-2" | 14 more

"gpt-realtime"

"gpt-realtime-1.5"

"gpt-realtime-2"

"gpt-realtime-2025-08-28"

"gpt-4o-realtime-preview"

"gpt-4o-realtime-preview-2024-10-01"

"gpt-4o-realtime-preview-2024-12-17"

"gpt-4o-realtime-preview-2025-06-03"

"gpt-4o-mini-realtime-preview"

"gpt-4o-mini-realtime-preview-2024-12-17"

"gpt-realtime-mini"

"gpt-realtime-mini-2025-10-06"

"gpt-realtime-mini-2025-12-15"

"gpt-audio-1.5"

"gpt-audio-mini"

"gpt-audio-mini-2025-10-06"

"gpt-audio-mini-2025-12-15"

output\_modalities?: Array<"text" | "audio">

The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

One of the following:

"text"

"audio"

prompt?: [ResponsePrompt](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_prompt%20%3E%20(schema)) { id, variables, version }  | null

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

reasoning?: [RealtimeReasoning](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning%20%3E%20(schema)) { effort }

Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.

tool\_choice?: [ToolChoiceOptions](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) | [ToolChoiceFunction](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_function%20%3E%20(schema)) { name, type }  | [ToolChoiceMcp](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_mcp%20%3E%20(schema)) { server\_label, type, name }

How the model chooses tools. Provide one of the string modes or force a specific
function/MCP tool.

One of the following:

ToolChoiceOptions = "none" | "auto" | "required"

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

One of the following:

"none"

"auto"

"required"

ToolChoiceFunction { name, type }

Use this option to force the model to call a specific function.

name: string

The name of the function to call.

type: "function"

For function calling, the type is always `function`.

ToolChoiceMcp { server\_label, type, name }

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: string

The label of the MCP server to use.

type: "mcp"

For MCP tools, the type is always `mcp`.

name?: string | null

The name of the tool to call on the server.

tools?: Array<[RealtimeFunctionTool](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_function_tool%20%3E%20(schema)) { description, name, parameters, type }  | McpTool { server\_label, type, allowed\_tools, 8 more } >

Tools available to the model.

One of the following:

RealtimeFunctionTool { description, name, parameters, type }

description?: string

The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

name?: string

The name of the function.

parameters?: unknown

Parameters of the function in JSON Schema.

type?: "function"

The type of the tool, i.e. `function`.

McpTool { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

One of the following:

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

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

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

One of the following:

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

tracing?: "auto" | TracingConfiguration { group\_id, metadata, workflow\_name }  | null

Realtime API can write session traces to the [Traces Dashboard](https://platform.openai.com/logs?api=traces). Set to null to disable tracing. Once
tracing is enabled for a session, the configuration cannot be modified.

`auto` will create a trace for the session with default values for the
workflow name, group id, and metadata.

One of the following:

"auto"

"auto"

TracingConfiguration { group\_id, metadata, workflow\_name }

Granular configuration for tracing.

group\_id?: string

The group id to attach to this trace to enable filtering and
grouping in the Traces Dashboard.

metadata?: unknown

The arbitrary metadata to attach to this trace to enable
filtering in the Traces Dashboard.

workflow\_name?: string

The name of the workflow to attach to this trace. This is used to
name the trace in the Traces Dashboard.

truncation?: [RealtimeTruncation](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_truncation%20%3E%20(schema))

When the number of tokens in a conversation exceeds the model’s input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model’s context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.

Clients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.

Truncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.

Truncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model’s input token limit.

RealtimeTranscriptionSessionCreateResponse { id, object, type, 3 more }

A Realtime transcription session configuration object.

id: string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

object: string

The object type. Always `realtime.transcription_session`.

type: "transcription"

The type of session. Always `transcription` for transcription sessions.

audio?: Audio { input }

Configuration for input audio for the session.

input?: Input { format, noise\_reduction, transcription, turn\_detection }

format?: [RealtimeAudioFormats](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The PCM audio format. Only a 24kHz sample rate is supported.

noise\_reduction?: NoiseReduction { type }

Configuration for input audio noise reduction.

type?: [NoiseReductionType](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

transcription?: [AudioTranscription](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)) { delay, language, model, prompt }

turn\_detection?: [RealtimeTranscriptionSessionTurnDetection](/api/reference/typescript/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20realtime_transcription_session_turn_detection%20%3E%20(schema)) { prefix\_padding\_ms, silence\_duration\_ms, threshold, type }  | null

Configuration for turn detection. Can be set to `null` to turn off. Server
VAD means that the model will detect the start and end of speech based on
audio volume and respond at the end of user speech. For `gpt-realtime-whisper`, this must be `null`; VAD is not supported.

expires\_at?: number

Expiration timestamp for the session, in seconds since epoch.

formatunixtime

include?: Array<"item.input\_audio\_transcription.logprobs">

Additional fields to include in server outputs.

* `item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

RealtimeTranscriptionSessionTurnDetection { prefix\_padding\_ms, silence\_duration\_ms, threshold, type }

Configuration for turn detection. Can be set to `null` to turn off. Server
VAD means that the model will detect the start and end of speech based on
audio volume and respond at the end of user speech. For `gpt-realtime-whisper`, this must be `null`; VAD is not supported.

prefix\_padding\_ms?: number

Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

silence\_duration\_ms?: number

Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

threshold?: number

Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

type?: string

Type of turn detection, only `server_vad` is currently supported.

ClientSecretCreateResponse { expires\_at, session, value }

Response from creating a session and client secret for the Realtime API.

expires\_at: number

Expiration timestamp for the client secret, in seconds since epoch.

formatunixtime

session: [RealtimeSessionCreateResponse](/api/reference/typescript/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20realtime_session_create_response%20%3E%20(schema)) { id, object, type, 13 more }  | [RealtimeTranscriptionSessionCreateResponse](/api/reference/typescript/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20realtime_transcription_session_create_response%20%3E%20(schema)) { id, object, type, 3 more }

The session configuration for either a realtime or transcription session.

One of the following:

RealtimeSessionCreateResponse { id, object, type, 13 more }

A Realtime session configuration object.

id: string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

object: "realtime.session"

The object type. Always `realtime.session`.

type: "realtime"

The type of session to create. Always `realtime` for the Realtime API.

audio?: Audio { input, output }

Configuration for input and output audio.

input?: Input { format, noise\_reduction, transcription, turn\_detection }

format?: [RealtimeAudioFormats](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the input audio.

noise\_reduction?: NoiseReduction { type }

Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

type?: [NoiseReductionType](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

transcription?: [AudioTranscription](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)) { delay, language, model, prompt }

turn\_detection?: ServerVad { type, create\_response, idle\_timeout\_ms, 4 more }  | SemanticVad { type, create\_response, eagerness, interrupt\_response }  | null

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with “uhhm”, the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

For `gpt-realtime-whisper` transcription sessions, turn detection must be
set to `null`; VAD is not supported.

One of the following:

ServerVad { type, create\_response, idle\_timeout\_ms, 4 more }

Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.

type: "server\_vad"

Type of turn detection, `server_vad` to turn on simple Server VAD.

create\_response?: boolean

Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

idle\_timeout\_ms?: number | null

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

interrupt\_response?: boolean

Whether or not to automatically interrupt (cancel) any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

prefix\_padding\_ms?: number

Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

silence\_duration\_ms?: number

Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

threshold?: number

Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

SemanticVad { type, create\_response, eagerness, interrupt\_response }

Server-side semantic turn detection which uses a model to determine when the user has finished speaking.

type: "semantic\_vad"

Type of turn detection, `semantic_vad` to turn on Semantic VAD.

create\_response?: boolean

Whether or not to automatically generate a response when a VAD stop event occurs.

eagerness?: "low" | "medium" | "high" | "auto"

Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.

One of the following:

"low"

"medium"

"high"

"auto"

interrupt\_response?: boolean

Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

output?: Output { format, speed, voice }

format?: [RealtimeAudioFormats](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the output audio.

speed?: number

The speed of the model’s spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it’s
also possible to prompt the model to speak faster or slower.

maximum1.5

minimum0.25

voice?: (string & {}) | "alloy" | "ash" | "ballad" | 7 more

The voice the model uses to respond. Voice cannot be changed during the
session once the model has responded with audio at least once. Current
voice options are `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`,
`shimmer`, `verse`, `marin`, and `cedar`. We recommend `marin` and `cedar` for
best quality.

One of the following:

(string & {})

"alloy" | "ash" | "ballad" | 7 more

"alloy"

"ash"

"ballad"

"coral"

"echo"

"sage"

"shimmer"

"verse"

"marin"

"cedar"

expires\_at?: number

Expiration timestamp for the session, in seconds since epoch.

formatunixtime

include?: Array<"item.input\_audio\_transcription.logprobs">

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

instructions?: string

The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. “be extremely succinct”, “act friendly”, “here are examples of good responses”) and on audio behavior (e.g. “talk quickly”, “inject emotion into your voice”, “laugh frequently”). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

max\_output\_tokens?: number | "inf"

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

One of the following:

number

"inf"

"inf"

model?: (string & {}) | "gpt-realtime" | "gpt-realtime-1.5" | "gpt-realtime-2" | 14 more

The Realtime model used for this session.

One of the following:

(string & {})

"gpt-realtime" | "gpt-realtime-1.5" | "gpt-realtime-2" | 14 more

"gpt-realtime"

"gpt-realtime-1.5"

"gpt-realtime-2"

"gpt-realtime-2025-08-28"

"gpt-4o-realtime-preview"

"gpt-4o-realtime-preview-2024-10-01"

"gpt-4o-realtime-preview-2024-12-17"

"gpt-4o-realtime-preview-2025-06-03"

"gpt-4o-mini-realtime-preview"

"gpt-4o-mini-realtime-preview-2024-12-17"

"gpt-realtime-mini"

"gpt-realtime-mini-2025-10-06"

"gpt-realtime-mini-2025-12-15"

"gpt-audio-1.5"

"gpt-audio-mini"

"gpt-audio-mini-2025-10-06"

"gpt-audio-mini-2025-12-15"

output\_modalities?: Array<"text" | "audio">

The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

One of the following:

"text"

"audio"

prompt?: [ResponsePrompt](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_prompt%20%3E%20(schema)) { id, variables, version }  | null

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

reasoning?: [RealtimeReasoning](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning%20%3E%20(schema)) { effort }

Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.

tool\_choice?: [ToolChoiceOptions](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) | [ToolChoiceFunction](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_function%20%3E%20(schema)) { name, type }  | [ToolChoiceMcp](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_mcp%20%3E%20(schema)) { server\_label, type, name }

How the model chooses tools. Provide one of the string modes or force a specific
function/MCP tool.

One of the following:

ToolChoiceOptions = "none" | "auto" | "required"

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

One of the following:

"none"

"auto"

"required"

ToolChoiceFunction { name, type }

Use this option to force the model to call a specific function.

name: string

The name of the function to call.

type: "function"

For function calling, the type is always `function`.

ToolChoiceMcp { server\_label, type, name }

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: string

The label of the MCP server to use.

type: "mcp"

For MCP tools, the type is always `mcp`.

name?: string | null

The name of the tool to call on the server.

tools?: Array<[RealtimeFunctionTool](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_function_tool%20%3E%20(schema)) { description, name, parameters, type }  | McpTool { server\_label, type, allowed\_tools, 8 more } >

Tools available to the model.

One of the following:

RealtimeFunctionTool { description, name, parameters, type }

description?: string

The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

name?: string

The name of the function.

parameters?: unknown

Parameters of the function in JSON Schema.

type?: "function"

The type of the tool, i.e. `function`.

McpTool { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

One of the following:

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

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

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

One of the following:

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

tracing?: "auto" | TracingConfiguration { group\_id, metadata, workflow\_name }  | null

Realtime API can write session traces to the [Traces Dashboard](https://platform.openai.com/logs?api=traces). Set to null to disable tracing. Once
tracing is enabled for a session, the configuration cannot be modified.

`auto` will create a trace for the session with default values for the
workflow name, group id, and metadata.

One of the following:

"auto"

"auto"

TracingConfiguration { group\_id, metadata, workflow\_name }

Granular configuration for tracing.

group\_id?: string

The group id to attach to this trace to enable filtering and
grouping in the Traces Dashboard.

metadata?: unknown

The arbitrary metadata to attach to this trace to enable
filtering in the Traces Dashboard.

workflow\_name?: string

The name of the workflow to attach to this trace. This is used to
name the trace in the Traces Dashboard.

truncation?: [RealtimeTruncation](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_truncation%20%3E%20(schema))

When the number of tokens in a conversation exceeds the model’s input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model’s context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.

Clients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.

Truncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.

Truncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model’s input token limit.

RealtimeTranscriptionSessionCreateResponse { id, object, type, 3 more }

A Realtime transcription session configuration object.

id: string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

object: string

The object type. Always `realtime.transcription_session`.

type: "transcription"

The type of session. Always `transcription` for transcription sessions.

audio?: Audio { input }

Configuration for input audio for the session.

input?: Input { format, noise\_reduction, transcription, turn\_detection }

format?: [RealtimeAudioFormats](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The PCM audio format. Only a 24kHz sample rate is supported.

noise\_reduction?: NoiseReduction { type }

Configuration for input audio noise reduction.

type?: [NoiseReductionType](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

transcription?: [AudioTranscription](/api/reference/typescript/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)) { delay, language, model, prompt }

turn\_detection?: [RealtimeTranscriptionSessionTurnDetection](/api/reference/typescript/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20realtime_transcription_session_turn_detection%20%3E%20(schema)) { prefix\_padding\_ms, silence\_duration\_ms, threshold, type }  | null

Configuration for turn detection. Can be set to `null` to turn off. Server
VAD means that the model will detect the start and end of speech based on
audio volume and respond at the end of user speech. For `gpt-realtime-whisper`, this must be `null`; VAD is not supported.

expires\_at?: number

Expiration timestamp for the session, in seconds since epoch.

formatunixtime

include?: Array<"item.input\_audio\_transcription.logprobs">

Additional fields to include in server outputs.

* `item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

value: string

The generated client secret value.
