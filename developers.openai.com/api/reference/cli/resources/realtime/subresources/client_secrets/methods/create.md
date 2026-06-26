<!-- source: https://developers.openai.com/api/reference/cli/resources/realtime/subresources/client_secrets/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Realtime](/api/reference/cli/resources/realtime)

[Client Secrets](/api/reference/cli/resources/realtime/subresources/client_secrets)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create client secret

$ openai realtime:client-secrets create

POST/realtime/client\_secrets

Create a Realtime client secret with an associated session configuration.

Client secrets are short-lived tokens that can be passed to a client app,
such as a web frontend or mobile client, which grants access to the Realtime API without
leaking your main API key. You can configure a custom TTL for each client secret.

You can also attach session configuration options to the client secret, which will be
applied to any sessions created using that client secret, but these can also be overridden
by the client connection.

[Learn more about authentication with client secrets over WebRTC](https://platform.openai.com/docs/guides/realtime-webrtc).

Returns the created client secret and the effective session object. The client secret is a string that looks like `ek_1234`.

##### ParametersExpand Collapse

--expires-after: optional object { anchor, seconds }

Configuration for the client secret expiration. Expiration refers to the time after which
a client secret will no longer be valid for creating sessions. The session itself may
continue after that time once started. A secret can be used to create multiple sessions
until it expires.

--session: optional [RealtimeSessionCreateRequest](/api/reference/cli/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)) { type, audio, include, 11 more }  or [RealtimeTranscriptionSessionCreateRequest](/api/reference/cli/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_create_request%20%3E%20(schema)) { type, audio, include }

Session configuration to use for the client secret. Choose either a realtime
session or a transcription session.

##### ReturnsExpand Collapse

ClientSecretNewResponse: object { expires\_at, session, value }

Response from creating a session and client secret for the Realtime API.

expires\_at: number

Expiration timestamp for the client secret, in seconds since epoch.

session: [RealtimeSessionCreateResponse](/api/reference/cli/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20realtime_session_create_response%20%3E%20(schema)) { id, object, type, 13 more }  or [RealtimeTranscriptionSessionCreateResponse](/api/reference/cli/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20realtime_transcription_session_create_response%20%3E%20(schema)) { id, object, type, 3 more }

The session configuration for either a realtime or transcription session.

realtime\_session\_create\_response: object { id, object, type, 13 more }

A Realtime session configuration object.

id: string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

object: "realtime.session"

The object type. Always `realtime.session`.

type: "realtime"

The type of session to create. Always `realtime` for the Realtime API.

audio: optional object { input, output }

Configuration for input and output audio.

input: optional object { format, noise\_reduction, transcription, turn\_detection }

format: optional object { rate, type }  or object { type }  or object { type }

The format of the input audio.

audio/pcm: object { rate, type }

The PCM audio format. Only a 24kHz sample rate is supported.

rate: optional 24000

The sample rate of the audio. Always `24000`.

24000

type: optional "audio/pcm"

The audio format. Always `audio/pcm`.

"audio/pcm"

audio/pcmu: object { type }

The G.711 μ-law format.

type: optional "audio/pcmu"

The audio format. Always `audio/pcmu`.

"audio/pcmu"

audio/pcma: object { type }

The G.711 A-law format.

type: optional "audio/pcma"

The audio format. Always `audio/pcma`.

"audio/pcma"

noise\_reduction: optional object { type }

Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

type: optional "near\_field" or "far\_field"

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

"near\_field"

"far\_field"

transcription: optional object { delay, language, model, prompt }

delay: optional "minimal" or "low" or "medium" or 2 more

Controls how long the model waits before emitting transcription text.
Higher values can improve transcription accuracy at the cost of latency.
Only supported with `gpt-realtime-whisper` in GA Realtime sessions.

"minimal"

"low"

"medium"

"high"

"xhigh"

language: optional string

The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

model: optional string or "whisper-1" or "gpt-4o-mini-transcribe" or "gpt-4o-mini-transcribe-2025-12-15" or 3 more

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

"whisper-1"

"gpt-4o-mini-transcribe"

"gpt-4o-mini-transcribe-2025-12-15"

"gpt-4o-transcribe"

"gpt-4o-transcribe-diarize"

"gpt-realtime-whisper"

prompt: optional string

An optional text to guide the model’s style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://platform.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example “expect words related to technology”.
Prompt is not supported with `gpt-realtime-whisper` in GA Realtime sessions.

turn\_detection: optional object { type, create\_response, idle\_timeout\_ms, 4 more }  or object { type, create\_response, eagerness, interrupt\_response }

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with “uhhm”, the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

For `gpt-realtime-whisper` transcription sessions, turn detection must be
set to `null`; VAD is not supported.

server\_vad: object { type, create\_response, idle\_timeout\_ms, 4 more }

Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.

type: "server\_vad"

Type of turn detection, `server_vad` to turn on simple Server VAD.

create\_response: optional boolean

Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

idle\_timeout\_ms: optional number

Optional timeout after which a model response will be triggered automatically. This is
useful for situations in which a long pause from the user is unexpected, such as a phone
call. The model will effectively prompt the user to continue the conversation based
on the current context.

The timeout value will be applied after the last model response’s audio has finished playing,
i.e. it’s set to the `response.done` time plus audio playback duration.

An `input_audio_buffer.timeout_triggered` event (plus events
associated with the Response) will be emitted when the timeout is reached.
Idle timeout is currently only supported for `server_vad` mode.

interrupt\_response: optional boolean

Whether or not to automatically interrupt (cancel) any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

prefix\_padding\_ms: optional number

Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

silence\_duration\_ms: optional number

Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

threshold: optional number

Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

semantic\_vad: object { type, create\_response, eagerness, interrupt\_response }

Server-side semantic turn detection which uses a model to determine when the user has finished speaking.

type: "semantic\_vad"

Type of turn detection, `semantic_vad` to turn on Semantic VAD.

create\_response: optional boolean

Whether or not to automatically generate a response when a VAD stop event occurs.

eagerness: optional "low" or "medium" or "high" or "auto"

Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.

"low"

"medium"

"high"

"auto"

interrupt\_response: optional boolean

Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

output: optional object { format, speed, voice }

format: optional object { rate, type }  or object { type }  or object { type }

The format of the output audio.

audio/pcm: object { rate, type }

The PCM audio format. Only a 24kHz sample rate is supported.

rate: optional 24000

The sample rate of the audio. Always `24000`.

24000

type: optional "audio/pcm"

The audio format. Always `audio/pcm`.

"audio/pcm"

audio/pcmu: object { type }

The G.711 μ-law format.

type: optional "audio/pcmu"

The audio format. Always `audio/pcmu`.

"audio/pcmu"

audio/pcma: object { type }

The G.711 A-law format.

type: optional "audio/pcma"

The audio format. Always `audio/pcma`.

"audio/pcma"

speed: optional number

The speed of the model’s spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it’s
also possible to prompt the model to speak faster or slower.

voice: optional string or "alloy" or "ash" or "ballad" or 7 more

The voice the model uses to respond. Voice cannot be changed during the
session once the model has responded with audio at least once. Current
voice options are `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`,
`shimmer`, `verse`, `marin`, and `cedar`. We recommend `marin` and `cedar` for
best quality.

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

expires\_at: optional number

Expiration timestamp for the session, in seconds since epoch.

include: optional array of "item.input\_audio\_transcription.logprobs"

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

"item.input\_audio\_transcription.logprobs"

instructions: optional string

The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. “be extremely succinct”, “act friendly”, “here are examples of good responses”) and on audio behavior (e.g. “talk quickly”, “inject emotion into your voice”, “laugh frequently”). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

max\_output\_tokens: optional number or "inf"

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

union\_member\_0: number

union\_member\_1: "inf"

model: optional string or "gpt-realtime" or "gpt-realtime-1.5" or "gpt-realtime-2" or 14 more

The Realtime model used for this session.

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

output\_modalities: optional array of "text" or "audio"

The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

"text"

"audio"

prompt: optional object { id, variables, version }

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

id: string

The unique identifier of the prompt template to use.

variables: optional map[string or [ResponseInputText](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  or [ResponseInputImage](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, image\_url }  or [ResponseInputFile](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 3 more } ]

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

union\_member\_0: string

response\_input\_text: object { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

response\_input\_image: object { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" or "high" or "auto" or "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string

The ID of the file to be sent to the model.

image\_url: optional string

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

response\_input\_file: object { type, detail, file\_data, 3 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail: optional "low" or "high"

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

"low"

"high"

file\_data: optional string

The content of the file to be sent to the model.

file\_id: optional string

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

filename: optional string

The name of the file to be sent to the model.

version: optional string

Optional version of the prompt template.

reasoning: optional object { effort }

Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.

effort: optional "minimal" or "low" or "medium" or 2 more

Constrains effort on reasoning for reasoning-capable Realtime models such as
`gpt-realtime-2`.

"minimal"

"low"

"medium"

"high"

"xhigh"

tool\_choice: optional [ToolChoiceOptions](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) or [ToolChoiceFunction](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_function%20%3E%20(schema)) { name, type }  or [ToolChoiceMcp](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_mcp%20%3E%20(schema)) { server\_label, type, name }

How the model chooses tools. Provide one of the string modes or force a specific
function/MCP tool.

tool\_choice\_options: "none" or "auto" or "required"

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

"none"

"auto"

"required"

tool\_choice\_function: object { name, type }

Use this option to force the model to call a specific function.

name: string

The name of the function to call.

type: "function"

For function calling, the type is always `function`.

tool\_choice\_mcp: object { server\_label, type, name }

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: string

The label of the MCP server to use.

type: "mcp"

For MCP tools, the type is always `mcp`.

name: optional string

The name of the tool to call on the server.

tools: optional array of [RealtimeFunctionTool](/api/reference/cli/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_function_tool%20%3E%20(schema)) { description, name, parameters, type }  or object { server\_label, type, allowed\_tools, 8 more }

Tools available to the model.

realtime\_function\_tool: object { description, name, parameters, type }

description: optional string

The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

name: optional string

The name of the function.

parameters: optional unknown

Parameters of the function in JSON Schema.

type: optional "function"

The type of the tool, i.e. `function`.

"function"

MCP tool: object { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools: optional array of string or object { read\_only, tool\_names }

List of allowed tool names or a filter object.

MCP allowed tools: array of string

A string array of allowed tool names

MCP tool filter: object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

authorization: optional string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

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

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: optional boolean

Whether this MCP tool is deferred and discovered via tool search.

headers: optional map[string]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never"

Specify which of the MCP server’s tools require approval.

MCP tool approval filter: object { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: optional object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

never: optional object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

MCP tool approval setting: "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

Optional description of the MCP server, used to provide more context.

server\_url: optional string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

tunnel\_id: optional string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

tracing: optional "auto" or object { group\_id, metadata, workflow\_name }

Realtime API can write session traces to the [Traces Dashboard](https://platform.openai.com/logs?api=traces). Set to null to disable tracing. Once
tracing is enabled for a session, the configuration cannot be modified.

`auto` will create a trace for the session with default values for the
workflow name, group id, and metadata.

auto: "auto"

Enables tracing and sets default values for tracing configuration options. Always `auto`.

Tracing Configuration: object { group\_id, metadata, workflow\_name }

Granular configuration for tracing.

group\_id: optional string

The group id to attach to this trace to enable filtering and
grouping in the Traces Dashboard.

metadata: optional unknown

The arbitrary metadata to attach to this trace to enable
filtering in the Traces Dashboard.

workflow\_name: optional string

The name of the workflow to attach to this trace. This is used to
name the trace in the Traces Dashboard.

truncation: optional "auto" or "disabled" or [RealtimeTruncationRetentionRatio](/api/reference/cli/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_truncation_retention_ratio%20%3E%20(schema)) { retention\_ratio, type, token\_limits }

When the number of tokens in a conversation exceeds the model’s input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model’s context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.

Clients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.

Truncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.

Truncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model’s input token limit.

RealtimeTruncationStrategy: "auto" or "disabled"

The truncation strategy to use for the session. `auto` is the default truncation strategy. `disabled` will disable truncation and emit errors when the conversation exceeds the input token limit.

"auto"

"disabled"

realtime\_truncation\_retention\_ratio: object { retention\_ratio, type, token\_limits }

Retain a fraction of the conversation tokens when the conversation exceeds the input token limit. This allows you to amortize truncations across multiple turns, which can help improve cached token usage.

retention\_ratio: number

Fraction of post-instruction conversation tokens to retain (`0.0` - `1.0`) when the conversation exceeds the input token limit. Setting this to `0.8` means that messages will be dropped until 80% of the maximum allowed tokens are used. This helps reduce the frequency of truncations and improve cache rates.

type: "retention\_ratio"

Use retention ratio truncation.

token\_limits: optional object { post\_instructions }

Optional custom token limits for this truncation strategy. If not provided, the model’s default token limits will be used.

post\_instructions: optional number

Maximum tokens allowed in the conversation after instructions (which including tool definitions). For example, setting this to 5,000 would mean that truncation would occur when the conversation exceeds 5,000 tokens after instructions. This cannot be higher than the model’s context window size minus the maximum output tokens.

realtime\_transcription\_session\_create\_response: object { id, object, type, 3 more }

A Realtime transcription session configuration object.

id: string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

object: string

The object type. Always `realtime.transcription_session`.

type: "transcription"

The type of session. Always `transcription` for transcription sessions.

audio: optional object { input }

Configuration for input audio for the session.

input: optional object { format, noise\_reduction, transcription, turn\_detection }

format: optional object { rate, type }  or object { type }  or object { type }

The PCM audio format. Only a 24kHz sample rate is supported.

audio/pcm: object { rate, type }

The PCM audio format. Only a 24kHz sample rate is supported.

rate: optional 24000

The sample rate of the audio. Always `24000`.

24000

type: optional "audio/pcm"

The audio format. Always `audio/pcm`.

"audio/pcm"

audio/pcmu: object { type }

The G.711 μ-law format.

type: optional "audio/pcmu"

The audio format. Always `audio/pcmu`.

"audio/pcmu"

audio/pcma: object { type }

The G.711 A-law format.

type: optional "audio/pcma"

The audio format. Always `audio/pcma`.

"audio/pcma"

noise\_reduction: optional object { type }

Configuration for input audio noise reduction.

type: optional "near\_field" or "far\_field"

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

"near\_field"

"far\_field"

transcription: optional object { delay, language, model, prompt }

delay: optional "minimal" or "low" or "medium" or 2 more

Controls how long the model waits before emitting transcription text.
Higher values can improve transcription accuracy at the cost of latency.
Only supported with `gpt-realtime-whisper` in GA Realtime sessions.

"minimal"

"low"

"medium"

"high"

"xhigh"

language: optional string

The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

model: optional string or "whisper-1" or "gpt-4o-mini-transcribe" or "gpt-4o-mini-transcribe-2025-12-15" or 3 more

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

"whisper-1"

"gpt-4o-mini-transcribe"

"gpt-4o-mini-transcribe-2025-12-15"

"gpt-4o-transcribe"

"gpt-4o-transcribe-diarize"

"gpt-realtime-whisper"

prompt: optional string

An optional text to guide the model’s style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://platform.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example “expect words related to technology”.
Prompt is not supported with `gpt-realtime-whisper` in GA Realtime sessions.

turn\_detection: optional object { prefix\_padding\_ms, silence\_duration\_ms, threshold, type }

Configuration for turn detection. Can be set to `null` to turn off. Server
VAD means that the model will detect the start and end of speech based on
audio volume and respond at the end of user speech. For `gpt-realtime-whisper`, this must be `null`; VAD is not supported.

prefix\_padding\_ms: optional number

Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

silence\_duration\_ms: optional number

Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

threshold: optional number

Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

type: optional string

Type of turn detection, only `server_vad` is currently supported.

expires\_at: optional number

Expiration timestamp for the session, in seconds since epoch.

include: optional array of "item.input\_audio\_transcription.logprobs"

Additional fields to include in server outputs.

* `item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

"item.input\_audio\_transcription.logprobs"

value: string

The generated client secret value.

### Create client secret

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai realtime:client-secrets create \
  --api-key 'My API Key'

  "value": "ek_68af296e8e408191a1120ab6383263c2",
  "expires_at": 1756310470,
  "session": {
    "type": "realtime",
    "object": "realtime.session",
    "id": "sess_C9CiUVUzUzYIssh3ELY1d",
    "model": "gpt-realtime",
    "output_modalities": [
      "audio"
    ],
    "instructions": "You are a friendly assistant.",
    "tools": [],
    "tool_choice": "auto",
    "max_output_tokens": "inf",
    "tracing": null,
    "truncation": "auto",
    "prompt": null,
    "expires_at": 0,
    "audio": {
      "input": {
        "format": {
          "type": "audio/pcm",
          "rate": 24000
        "transcription": null,
        "noise_reduction": null,
        "turn_detection": {
          "type": "server_vad",
      "output": {
        "format": {
          "type": "audio/pcm",
          "rate": 24000
        "voice": "alloy",
        "speed": 1.0
    "include": null

##### Returns Examples

  "value": "ek_68af296e8e408191a1120ab6383263c2",
  "expires_at": 1756310470,
  "session": {
    "type": "realtime",
    "object": "realtime.session",
    "id": "sess_C9CiUVUzUzYIssh3ELY1d",
    "model": "gpt-realtime",
    "output_modalities": [
      "audio"
    ],
    "instructions": "You are a friendly assistant.",
    "tools": [],
    "tool_choice": "auto",
    "max_output_tokens": "inf",
    "tracing": null,
    "truncation": "auto",
    "prompt": null,
    "expires_at": 0,
    "audio": {
      "input": {
        "format": {
          "type": "audio/pcm",
          "rate": 24000
        "transcription": null,
        "noise_reduction": null,
        "turn_detection": {
          "type": "server_vad",
      "output": {
        "format": {
          "type": "audio/pcm",
          "rate": 24000
        "voice": "alloy",
        "speed": 1.0
    "include": null
