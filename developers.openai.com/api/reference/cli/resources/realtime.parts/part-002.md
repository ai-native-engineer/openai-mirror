<!-- source: https://developers.openai.com/api/reference/cli/resources/realtime/ -->
<!-- part of: https://developers.openai.com/api/reference/cli/resources/realtime/ -->

<!-- chunk-start -->

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

realtime\_transcription\_session\_turn\_detection: object { prefix\_padding\_ms, silence\_duration\_ms, threshold, type }

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

#### RealtimeCalls

##### [Accept call](/api/reference/cli/resources/realtime/subresources/calls/methods/accept)

$ openai realtime:calls accept

POST/realtime/calls/{call\_id}/accept

##### [Hang up call](/api/reference/cli/resources/realtime/subresources/calls/methods/hangup)

$ openai realtime:calls hangup

POST/realtime/calls/{call\_id}/hangup

##### [Refer call](/api/reference/cli/resources/realtime/subresources/calls/methods/refer)

$ openai realtime:calls refer

POST/realtime/calls/{call\_id}/refer

##### [Reject call](/api/reference/cli/resources/realtime/subresources/calls/methods/reject)

$ openai realtime:calls reject

POST/realtime/calls/{call\_id}/reject

#### RealtimeTranslations

#### RealtimeTranslationsClient Secrets

#### RealtimeSessions

#### RealtimeTranscription Sessions
