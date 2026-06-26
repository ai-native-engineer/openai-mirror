<!-- source: https://developers.openai.com/api/reference/go/resources/realtime/subresources/client_secrets/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Realtime](/api/reference/go/resources/realtime)

[Client Secrets](/api/reference/go/resources/realtime/subresources/client_secrets)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create client secret

client.Realtime.ClientSecrets.New(ctx, body) (\*[ClientSecretNewResponse](/api/reference/go/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20ClientSecretNewResponse%20%3E%20(schema)), error)

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

body ClientSecretNewParams

ExpiresAfter param.Field[[ClientSecretNewParamsExpiresAfter](/api/reference/go/resources/realtime/subresources/client_secrets/methods/create#(resource)%20realtime.client_secrets%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20expires_after%20%3E%20(schema))]Optional

Configuration for the client secret expiration. Expiration refers to the time after which
a client secret will no longer be valid for creating sessions. The session itself may
continue after that time once started. A secret can be used to create multiple sessions
until it expires.

Anchor stringOptional

The anchor point for the client secret expiration, meaning that `seconds` will be added to the `created_at` time of the client secret to produce an expiration timestamp. Only `created_at` is currently supported.

Seconds int64Optional

The number of seconds from the anchor point to the expiration. Select a value between `10` and `7200` (2 hours). This default to 600 seconds (10 minutes) if not specified.

formatint64

minimum10

maximum7200

Session param.Field[[ClientSecretNewParamsSessionUnion](/api/reference/go/resources/realtime/subresources/client_secrets/methods/create#(resource)%20realtime.client_secrets%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20session%20%3E%20(schema))]Optional

Session configuration to use for the client secret. Choose either a realtime
session or a transcription session.

type RealtimeSessionCreateRequest struct{…}

Realtime session object configuration.

Type Realtime

The type of session to create. Always `realtime` for the Realtime API.

Audio [RealtimeAudioConfig](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config%20%3E%20(schema))Optional

Configuration for input and output audio.

Input [RealtimeAudioConfigInput](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_input%20%3E%20(schema))Optional

Format [RealtimeAudioFormatsUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))Optional

The format of the input audio.

One of the following:

type RealtimeAudioFormatsAudioPCM struct{…}

The PCM audio format. Only a 24kHz sample rate is supported.

Rate int64Optional

The sample rate of the audio. Always `24000`.

Type stringOptional

The audio format. Always `audio/pcm`.

type RealtimeAudioFormatsAudioPCMU struct{…}

The G.711 μ-law format.

Type stringOptional

The audio format. Always `audio/pcmu`.

type RealtimeAudioFormatsAudioPCMA struct{…}

The G.711 A-law format.

Type stringOptional

The audio format. Always `audio/pcma`.

NoiseReduction RealtimeAudioConfigInputNoiseReductionOptional

Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

Type [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))Optional

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

One of the following:

const NoiseReductionTypeNearField [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema)) = "near\_field"

const NoiseReductionTypeFarField [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema)) = "far\_field"

Transcription [AudioTranscription](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema))Optional

Configuration for input audio transcription, defaults to off and can be set to `null` to turn off once on. Input audio transcription is not native to the model, since the model consumes audio directly. Transcription runs asynchronously through [the /audio/transcriptions endpoint](https://platform.openai.com/docs/api-reference/audio/createTranscription) and should be treated as guidance of input audio content rather than precisely what the model heard. The client can optionally set the language and prompt for transcription, these offer additional guidance to the transcription service.

Delay AudioTranscriptionDelayOptional

Controls how long the model waits before emitting transcription text.
Higher values can improve transcription accuracy at the cost of latency.
Only supported with `gpt-realtime-whisper` in GA Realtime sessions.

One of the following:

const AudioTranscriptionDelayMinimal AudioTranscriptionDelay = "minimal"

const AudioTranscriptionDelayLow AudioTranscriptionDelay = "low"

const AudioTranscriptionDelayMedium AudioTranscriptionDelay = "medium"

const AudioTranscriptionDelayHigh AudioTranscriptionDelay = "high"

const AudioTranscriptionDelayXhigh AudioTranscriptionDelay = "xhigh"

Language stringOptional

The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

Model AudioTranscriptionModelOptional

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

One of the following:

string

type AudioTranscriptionModel string

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

One of the following:

const AudioTranscriptionModelWhisper1 AudioTranscriptionModel = "whisper-1"

const AudioTranscriptionModelGPT4oMiniTranscribe AudioTranscriptionModel = "gpt-4o-mini-transcribe"

const AudioTranscriptionModelGPT4oMiniTranscribe2025\_12\_15 AudioTranscriptionModel = "gpt-4o-mini-transcribe-2025-12-15"

const AudioTranscriptionModelGPT4oTranscribe AudioTranscriptionModel = "gpt-4o-transcribe"

const AudioTranscriptionModelGPT4oTranscribeDiarize AudioTranscriptionModel = "gpt-4o-transcribe-diarize"

const AudioTranscriptionModelGPTRealtimeWhisper AudioTranscriptionModel = "gpt-realtime-whisper"

Prompt stringOptional

An optional text to guide the model’s style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://platform.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example “expect words related to technology”.
Prompt is not supported with `gpt-realtime-whisper` in GA Realtime sessions.

TurnDetection [RealtimeAudioInputTurnDetectionUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema))Optional

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with “uhhm”, the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

For `gpt-realtime-whisper` transcription sessions, turn detection must be
set to `null`; VAD is not supported.

One of the following:

RealtimeAudioInputTurnDetectionServerVad

Type ServerVad

Type of turn detection, `server_vad` to turn on simple Server VAD.

CreateResponse boolOptional

Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

IdleTimeoutMs int64Optional

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

InterruptResponse boolOptional

Whether or not to automatically interrupt (cancel) any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

PrefixPaddingMs int64Optional

Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

SilenceDurationMs int64Optional

Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

Threshold float64Optional

Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

RealtimeAudioInputTurnDetectionSemanticVad

Type SemanticVad

Type of turn detection, `semantic_vad` to turn on Semantic VAD.

CreateResponse boolOptional

Whether or not to automatically generate a response when a VAD stop event occurs.

Eagerness stringOptional

Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.

One of the following:

const RealtimeAudioInputTurnDetectionSemanticVadEagernessLow RealtimeAudioInputTurnDetectionSemanticVadEagerness = "low"

const RealtimeAudioInputTurnDetectionSemanticVadEagernessMedium RealtimeAudioInputTurnDetectionSemanticVadEagerness = "medium"

const RealtimeAudioInputTurnDetectionSemanticVadEagernessHigh RealtimeAudioInputTurnDetectionSemanticVadEagerness = "high"

const RealtimeAudioInputTurnDetectionSemanticVadEagernessAuto RealtimeAudioInputTurnDetectionSemanticVadEagerness = "auto"

InterruptResponse boolOptional

Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

Output [RealtimeAudioConfigOutput](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema))Optional

Format [RealtimeAudioFormatsUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))Optional

The format of the output audio.

One of the following:

type RealtimeAudioFormatsAudioPCM struct{…}

The PCM audio format. Only a 24kHz sample rate is supported.

Rate int64Optional

The sample rate of the audio. Always `24000`.

Type stringOptional

The audio format. Always `audio/pcm`.

type RealtimeAudioFormatsAudioPCMU struct{…}

The G.711 μ-law format.

Type stringOptional

The audio format. Always `audio/pcmu`.

type RealtimeAudioFormatsAudioPCMA struct{…}

The G.711 A-law format.

Type stringOptional

The audio format. Always `audio/pcma`.

Speed float64Optional

The speed of the model’s spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it’s
also possible to prompt the model to speak faster or slower.

maximum1.5

minimum0.25

Voice RealtimeAudioConfigOutputVoiceUnionOptional

The voice the model uses to respond. Supported built-in voices are
`alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`,
`marin`, and `cedar`. You may also provide a custom voice object with
an `id`, for example `{ "id": "voice_1234" }`. Voice cannot be changed
during the session once the model has responded with audio at least once.
We recommend `marin` and `cedar` for best quality.

One of the following:

string

string

One of the following:

const RealtimeAudioConfigOutputVoiceString2Alloy RealtimeAudioConfigOutputVoiceString2 = "alloy"

const RealtimeAudioConfigOutputVoiceString2Ash RealtimeAudioConfigOutputVoiceString2 = "ash"

const RealtimeAudioConfigOutputVoiceString2Ballad RealtimeAudioConfigOutputVoiceString2 = "ballad"

const RealtimeAudioConfigOutputVoiceString2Coral RealtimeAudioConfigOutputVoiceString2 = "coral"

const RealtimeAudioConfigOutputVoiceString2Echo RealtimeAudioConfigOutputVoiceString2 = "echo"

const RealtimeAudioConfigOutputVoiceString2Sage RealtimeAudioConfigOutputVoiceString2 = "sage"

const RealtimeAudioConfigOutputVoiceString2Shimmer RealtimeAudioConfigOutputVoiceString2 = "shimmer"

const RealtimeAudioConfigOutputVoiceString2Verse RealtimeAudioConfigOutputVoiceString2 = "verse"

const RealtimeAudioConfigOutputVoiceString2Marin RealtimeAudioConfigOutputVoiceString2 = "marin"

const RealtimeAudioConfigOutputVoiceString2Cedar RealtimeAudioConfigOutputVoiceString2 = "cedar"

RealtimeAudioConfigOutputVoiceID

ID string

The custom voice ID, e.g. `voice_1234`.

Include []stringOptional

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

Instructions stringOptional

The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. “be extremely succinct”, “act friendly”, “here are examples of good responses”) and on audio behavior (e.g. “talk quickly”, “inject emotion into your voice”, “laugh frequently”). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

MaxOutputTokens RealtimeSessionCreateRequestMaxOutputTokensUnionOptional

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

One of the following:

int64

Inf

Model RealtimeSessionCreateRequestModelOptional

The Realtime model used for this session.

One of the following:

string

RealtimeSessionCreateRequestModel

One of the following:

const RealtimeSessionCreateRequestModelGPTRealtime RealtimeSessionCreateRequestModel = "gpt-realtime"

const RealtimeSessionCreateRequestModelGPTRealtime1\_5 RealtimeSessionCreateRequestModel = "gpt-realtime-1.5"

const RealtimeSessionCreateRequestModelGPTRealtime2 RealtimeSessionCreateRequestModel = "gpt-realtime-2"

const RealtimeSessionCreateRequestModelGPTRealtime2025\_08\_28 RealtimeSessionCreateRequestModel = "gpt-realtime-2025-08-28"

const RealtimeSessionCreateRequestModelGPT4oRealtimePreview RealtimeSessionCreateRequestModel = "gpt-4o-realtime-preview"

const RealtimeSessionCreateRequestModelGPT4oRealtimePreview2024\_10\_01 RealtimeSessionCreateRequestModel = "gpt-4o-realtime-preview-2024-10-01"

const RealtimeSessionCreateRequestModelGPT4oRealtimePreview2024\_12\_17 RealtimeSessionCreateRequestModel = "gpt-4o-realtime-preview-2024-12-17"

const RealtimeSessionCreateRequestModelGPT4oRealtimePreview2025\_06\_03 RealtimeSessionCreateRequestModel = "gpt-4o-realtime-preview-2025-06-03"

const RealtimeSessionCreateRequestModelGPT4oMiniRealtimePreview RealtimeSessionCreateRequestModel = "gpt-4o-mini-realtime-preview"

const RealtimeSessionCreateRequestModelGPT4oMiniRealtimePreview2024\_12\_17 RealtimeSessionCreateRequestModel = "gpt-4o-mini-realtime-preview-2024-12-17"

const RealtimeSessionCreateRequestModelGPTRealtimeMini RealtimeSessionCreateRequestModel = "gpt-realtime-mini"

const RealtimeSessionCreateRequestModelGPTRealtimeMini2025\_10\_06 RealtimeSessionCreateRequestModel = "gpt-realtime-mini-2025-10-06"

const RealtimeSessionCreateRequestModelGPTRealtimeMini2025\_12\_15 RealtimeSessionCreateRequestModel = "gpt-realtime-mini-2025-12-15"

const RealtimeSessionCreateRequestModelGPTAudio1\_5 RealtimeSessionCreateRequestModel = "gpt-audio-1.5"

const RealtimeSessionCreateRequestModelGPTAudioMini RealtimeSessionCreateRequestModel = "gpt-audio-mini"

const RealtimeSessionCreateRequestModelGPTAudioMini2025\_10\_06 RealtimeSessionCreateRequestModel = "gpt-audio-mini-2025-10-06"

const RealtimeSessionCreateRequestModelGPTAudioMini2025\_12\_15 RealtimeSessionCreateRequestModel = "gpt-audio-mini-2025-12-15"

OutputModalities []stringOptional

The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

One of the following:

const RealtimeSessionCreateRequestOutputModalityText RealtimeSessionCreateRequestOutputModality = "text"

const RealtimeSessionCreateRequestOutputModalityAudio RealtimeSessionCreateRequestOutputModality = "audio"

ParallelToolCalls boolOptional

Whether the model may call multiple tools in parallel. Only supported by
reasoning Realtime models such as `gpt-realtime-2`.

Prompt [ResponsePrompt](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_prompt%20%3E%20(schema))Optional

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

ID string

The unique identifier of the prompt template to use.

Variables map[string, ResponsePromptVariableUnion]Optional

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

One of the following:

string

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type ResponseInputImage struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail ResponseInputImageDetail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

const ResponseInputImageDetailLow ResponseInputImageDetail = "low"

const ResponseInputImageDetailHigh ResponseInputImageDetail = "high"

const ResponseInputImageDetailAuto ResponseInputImageDetail = "auto"

const ResponseInputImageDetailOriginal ResponseInputImageDetail = "original"

Type InputImage

The type of the input item. Always `input_image`.

FileID stringOptional

The ID of the file to be sent to the model.

ImageURL stringOptional

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

type ResponseInputFile struct{…}

A file input to the model.

Type InputFile

The type of the input item. Always `input_file`.

Detail ResponseInputFileDetailOptional

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

const ResponseInputFileDetailLow ResponseInputFileDetail = "low"

const ResponseInputFileDetailHigh ResponseInputFileDetail = "high"

FileData stringOptional

The content of the file to be sent to the model.

FileID stringOptional

The ID of the file to be sent to the model.

FileURL stringOptional

The URL of the file to be sent to the model.

formaturi

Filename stringOptional

The name of the file to be sent to the model.

Version stringOptional

Optional version of the prompt template.

Reasoning [RealtimeReasoning](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning%20%3E%20(schema))Optional

Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.

Effort [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema))Optional

Constrains effort on reasoning for reasoning-capable Realtime models such as
`gpt-realtime-2`.

One of the following:

const RealtimeReasoningEffortMinimal [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)) = "minimal"

const RealtimeReasoningEffortLow [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)) = "low"

const RealtimeReasoningEffortMedium [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)) = "medium"

const RealtimeReasoningEffortHigh [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)) = "high"

const RealtimeReasoningEffortXhigh [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)) = "xhigh"

ToolChoice [RealtimeToolChoiceConfigUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_tool_choice_config%20%3E%20(schema))Optional

How the model chooses tools. Provide one of the string modes or force a specific
function/MCP tool.

One of the following:

type ToolChoiceOptions string

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

One of the following:

const ToolChoiceOptionsNone [ToolChoiceOptions](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) = "none"

const ToolChoiceOptionsAuto [ToolChoiceOptions](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) = "auto"

const ToolChoiceOptionsRequired [ToolChoiceOptions](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) = "required"

type ToolChoiceFunction struct{…}

Use this option to force the model to call a specific function.

Name string

The name of the function to call.

Type Function

For function calling, the type is always `function`.

type ToolChoiceMcp struct{…}

Use this option to force the model to call a specific tool on a remote MCP server.

ServerLabel string

The label of the MCP server to use.

Type Mcp

For MCP tools, the type is always `mcp`.

Name stringOptional

The name of the tool to call on the server.

Tools [RealtimeToolsConfig](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_tools_config%20%3E%20(schema))Optional

Tools available to the model.

One of the following:

type RealtimeFunctionTool struct{…}

Description stringOptional

The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

Name stringOptional

The name of the function.

Parameters anyOptional

Parameters of the function in JSON Schema.

Type RealtimeFunctionToolTypeOptional

The type of the tool, i.e. `function`.

RealtimeToolsConfigUnionMcp

ServerLabel string

A label for this MCP server, used to identify it in tool calls.

Type Mcp

The type of the MCP tool. Always `mcp`.

AllowedTools RealtimeToolsConfigUnionMcpAllowedToolsOptional

List of allowed tool names or a filter object.

One of the following:

[]string

RealtimeToolsConfigUnionMcpAllowedToolsMcpToolFilter

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Authorization stringOptional

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

ConnectorID stringOptional

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

const RealtimeToolsConfigUnionMcpConnectorIDConnectorDropbox RealtimeToolsConfigUnionMcpConnectorID = "connector\_dropbox"

const RealtimeToolsConfigUnionMcpConnectorIDConnectorGmail RealtimeToolsConfigUnionMcpConnectorID = "connector\_gmail"

const RealtimeToolsConfigUnionMcpConnectorIDConnectorGooglecalendar RealtimeToolsConfigUnionMcpConnectorID = "connector\_googlecalendar"

const RealtimeToolsConfigUnionMcpConnectorIDConnectorGoogledrive RealtimeToolsConfigUnionMcpConnectorID = "connector\_googledrive"

const RealtimeToolsConfigUnionMcpConnectorIDConnectorMicrosoftteams RealtimeToolsConfigUnionMcpConnectorID = "connector\_microsoftteams"

const RealtimeToolsConfigUnionMcpConnectorIDConnectorOutlookcalendar RealtimeToolsConfigUnionMcpConnectorID = "connector\_outlookcalendar"

const RealtimeToolsConfigUnionMcpConnectorIDConnectorOutlookemail RealtimeToolsConfigUnionMcpConnectorID = "connector\_outlookemail"

const RealtimeToolsConfigUnionMcpConnectorIDConnectorSharepoint RealtimeToolsConfigUnionMcpConnectorID = "connector\_sharepoint"

DeferLoading boolOptional

Whether this MCP tool is deferred and discovered via tool search.

Headers map[string, string]Optional

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

RequireApproval RealtimeToolsConfigUnionMcpRequireApprovalOptional

Specify which of the MCP server’s tools require approval.

One of the following:

RealtimeToolsConfigUnionMcpRequireApprovalMcpToolApprovalFilter

Always RealtimeToolsConfigUnionMcpRequireApprovalMcpToolApprovalFilterAlwaysOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Never RealtimeToolsConfigUnionMcpRequireApprovalMcpToolApprovalFilterNeverOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

string

One of the following:

const RealtimeToolsConfigUnionMcpRequireApprovalMcpToolApprovalSettingAlways RealtimeToolsConfigUnionMcpRequireApprovalMcpToolApprovalSetting = "always"

const RealtimeToolsConfigUnionMcpRequireApprovalMcpToolApprovalSettingNever RealtimeToolsConfigUnionMcpRequireApprovalMcpToolApprovalSetting = "never"

ServerDescription stringOptional

Optional description of the MCP server, used to provide more context.

ServerURL stringOptional

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

TunnelID stringOptional

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

Tracing [RealtimeTracingConfigUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_tracing_config%20%3E%20(schema))Optional

Realtime API can write session traces to the [Traces Dashboard](https://platform.openai.com/logs?api=traces). Set to null to disable tracing. Once
tracing is enabled for a session, the configuration cannot be modified.

`auto` will create a trace for the session with default values for the
workflow name, group id, and metadata.

One of the following:

Auto

RealtimeTracingConfigTracingConfiguration

GroupID stringOptional

The group id to attach to this trace to enable filtering and
grouping in the Traces Dashboard.

Metadata anyOptional

The arbitrary metadata to attach to this trace to enable
filtering in the Traces Dashboard.

WorkflowName stringOptional

The name of the workflow to attach to this trace. This is used to
name the trace in the Traces Dashboard.

Truncation [RealtimeTruncationUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_truncation%20%3E%20(schema))Optional

When the number of tokens in a conversation exceeds the model’s input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model’s context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.

Clients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.

Truncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.

Truncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model’s input token limit.

One of the following:

type RealtimeTruncationRealtimeTruncationStrategy string

The truncation strategy to use for the session. `auto` is the default truncation strategy. `disabled` will disable truncation and emit errors when the conversation exceeds the input token limit.

One of the following:

const RealtimeTruncationRealtimeTruncationStrategyAuto RealtimeTruncationRealtimeTruncationStrategy = "auto"

const RealtimeTruncationRealtimeTruncationStrategyDisabled RealtimeTruncationRealtimeTruncationStrategy = "disabled"

type RealtimeTruncationRetentionRatio struct{…}

Retain a fraction of the conversation tokens when the conversation exceeds the input token limit. This allows you to amortize truncations across multiple turns, which can help improve cached token usage.

RetentionRatio float64

Fraction of post-instruction conversation tokens to retain (`0.0` - `1.0`) when the conversation exceeds the input token limit. Setting this to `0.8` means that messages will be dropped until 80% of the maximum allowed tokens are used. This helps reduce the frequency of truncations and improve cache rates.

minimum0

maximum1

Type RetentionRatio

Use retention ratio truncation.

TokenLimits RealtimeTruncationRetentionRatioTokenLimitsOptional

Optional custom token limits for this truncation strategy. If not provided, the model’s default token limits will be used.

PostInstructions int64Optional

Maximum tokens allowed in the conversation after instructions (which including tool definitions). For example, setting this to 5,000 would mean that truncation would occur when the conversation exceeds 5,000 tokens after instructions. This cannot be higher than the model’s context window size minus the maximum output tokens.

minimum0

type RealtimeTranscriptionSessionCreateRequest struct{…}

Realtime transcription session object configuration.

Type Transcription

The type of session to create. Always `transcription` for transcription sessions.

Audio [RealtimeTranscriptionSessionAudio](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_audio%20%3E%20(schema))Optional

Configuration for input and output audio.

Input [RealtimeTranscriptionSessionAudioInput](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_audio_input%20%3E%20(schema))Optional

Format [RealtimeAudioFormatsUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))Optional

The PCM audio format. Only a 24kHz sample rate is supported.

One of the following:

type RealtimeAudioFormatsAudioPCM struct{…}

The PCM audio format. Only a 24kHz sample rate is supported.

Rate int64Optional

The sample rate of the audio. Always `24000`.

Type stringOptional

The audio format. Always `audio/pcm`.

type RealtimeAudioFormatsAudioPCMU struct{…}

The G.711 μ-law format.

Type stringOptional

The audio format. Always `audio/pcmu`.

type RealtimeAudioFormatsAudioPCMA struct{…}

The G.711 A-law format.

Type stringOptional

The audio format. Always `audio/pcma`.

NoiseReduction RealtimeTranscriptionSessionAudioInputNoiseReductionOptional

Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

Type [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))Optional

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

One of the following:

const NoiseReductionTypeNearField [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema)) = "near\_field"

const NoiseReductionTypeFarField [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema)) = "far\_field"

Transcription [AudioTranscription](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema))Optional

Configuration for input audio transcription, defaults to off and can be set to `null` to turn off once on. Input audio transcription is not native to the model, since the model consumes audio directly. Transcription runs asynchronously through [the /audio/transcriptions endpoint](https://platform.openai.com/docs/api-reference/audio/createTranscription) and should be treated as guidance of input audio content rather than precisely what the model heard. The client can optionally set the language and prompt for transcription, these offer additional guidance to the transcription service.

Delay AudioTranscriptionDelayOptional

Controls how long the model waits before emitting transcription text.
Higher values can improve transcription accuracy at the cost of latency.
Only supported with `gpt-realtime-whisper` in GA Realtime sessions.

One of the following:

const AudioTranscriptionDelayMinimal AudioTranscriptionDelay = "minimal"

const AudioTranscriptionDelayLow AudioTranscriptionDelay = "low"

const AudioTranscriptionDelayMedium AudioTranscriptionDelay = "medium"

const AudioTranscriptionDelayHigh AudioTranscriptionDelay = "high"

const AudioTranscriptionDelayXhigh AudioTranscriptionDelay = "xhigh"

Language stringOptional

The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

Model AudioTranscriptionModelOptional

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

One of the following:

string

type AudioTranscriptionModel string

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

One of the following:

const AudioTranscriptionModelWhisper1 AudioTranscriptionModel = "whisper-1"

const AudioTranscriptionModelGPT4oMiniTranscribe AudioTranscriptionModel = "gpt-4o-mini-transcribe"

const AudioTranscriptionModelGPT4oMiniTranscribe2025\_12\_15 AudioTranscriptionModel = "gpt-4o-mini-transcribe-2025-12-15"

const AudioTranscriptionModelGPT4oTranscribe AudioTranscriptionModel = "gpt-4o-transcribe"

const AudioTranscriptionModelGPT4oTranscribeDiarize AudioTranscriptionModel = "gpt-4o-transcribe-diarize"

const AudioTranscriptionModelGPTRealtimeWhisper AudioTranscriptionModel = "gpt-realtime-whisper"

Prompt stringOptional

An optional text to guide the model’s style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://platform.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example “expect words related to technology”.
Prompt is not supported with `gpt-realtime-whisper` in GA Realtime sessions.

TurnDetection [RealtimeTranscriptionSessionAudioInputTurnDetectionUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_audio_input_turn_detection%20%3E%20(schema))Optional

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with “uhhm”, the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

For `gpt-realtime-whisper` transcription sessions, turn detection must be
set to `null`; VAD is not supported.

One of the following:

RealtimeTranscriptionSessionAudioInputTurnDetectionServerVad

Type ServerVad

Type of turn detection, `server_vad` to turn on simple Server VAD.

CreateResponse boolOptional

Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

IdleTimeoutMs int64Optional

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

InterruptResponse boolOptional

Whether or not to automatically interrupt (cancel) any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

PrefixPaddingMs int64Optional

Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

SilenceDurationMs int64Optional

Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

Threshold float64Optional

Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

RealtimeTranscriptionSessionAudioInputTurnDetectionSemanticVad

Type SemanticVad

Type of turn detection, `semantic_vad` to turn on Semantic VAD.

CreateResponse boolOptional

Whether or not to automatically generate a response when a VAD stop event occurs.

Eagerness stringOptional

Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.

One of the following:

const RealtimeTranscriptionSessionAudioInputTurnDetectionSemanticVadEagernessLow RealtimeTranscriptionSessionAudioInputTurnDetectionSemanticVadEagerness = "low"

const RealtimeTranscriptionSessionAudioInputTurnDetectionSemanticVadEagernessMedium RealtimeTranscriptionSessionAudioInputTurnDetectionSemanticVadEagerness = "medium"

const RealtimeTranscriptionSessionAudioInputTurnDetectionSemanticVadEagernessHigh RealtimeTranscriptionSessionAudioInputTurnDetectionSemanticVadEagerness = "high"

const RealtimeTranscriptionSessionAudioInputTurnDetectionSemanticVadEagernessAuto RealtimeTranscriptionSessionAudioInputTurnDetectionSemanticVadEagerness = "auto"

InterruptResponse boolOptional

Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

Include []stringOptional

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

##### ReturnsExpand Collapse

type ClientSecretNewResponse struct{…}

Response from creating a session and client secret for the Realtime API.

ExpiresAt int64

Expiration timestamp for the client secret, in seconds since epoch.

formatunixtime

Session ClientSecretNewResponseSessionUnion

The session configuration for either a realtime or transcription session.

One of the following:

type RealtimeSessionCreateResponse struct{…}

A Realtime session configuration object.

ID string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

Object RealtimeSession

The object type. Always `realtime.session`.

Type Realtime

The type of session to create. Always `realtime` for the Realtime API.

Audio RealtimeSessionCreateResponseAudioOptional

Configuration for input and output audio.

Input RealtimeSessionCreateResponseAudioInputOptional

Format [RealtimeAudioFormatsUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))Optional

The format of the input audio.

One of the following:

type RealtimeAudioFormatsAudioPCM struct{…}

The PCM audio format. Only a 24kHz sample rate is supported.

Rate int64Optional

The sample rate of the audio. Always `24000`.

Type stringOptional

The audio format. Always `audio/pcm`.

type RealtimeAudioFormatsAudioPCMU struct{…}

The G.711 μ-law format.

Type stringOptional

The audio format. Always `audio/pcmu`.

type RealtimeAudioFormatsAudioPCMA struct{…}

The G.711 A-law format.

Type stringOptional

The audio format. Always `audio/pcma`.

NoiseReduction RealtimeSessionCreateResponseAudioInputNoiseReductionOptional

Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

Type [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))Optional

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

One of the following:

const NoiseReductionTypeNearField [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema)) = "near\_field"

const NoiseReductionTypeFarField [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema)) = "far\_field"

Transcription [AudioTranscription](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema))Optional

Delay AudioTranscriptionDelayOptional

Controls how long the model waits before emitting transcription text.
Higher values can improve transcription accuracy at the cost of latency.
Only supported with `gpt-realtime-whisper` in GA Realtime sessions.

One of the following:

const AudioTranscriptionDelayMinimal AudioTranscriptionDelay = "minimal"

const AudioTranscriptionDelayLow AudioTranscriptionDelay = "low"

const AudioTranscriptionDelayMedium AudioTranscriptionDelay = "medium"

const AudioTranscriptionDelayHigh AudioTranscriptionDelay = "high"

const AudioTranscriptionDelayXhigh AudioTranscriptionDelay = "xhigh"

Language stringOptional

The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

Model AudioTranscriptionModelOptional

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

One of the following:

string

type AudioTranscriptionModel string

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

One of the following:

const AudioTranscriptionModelWhisper1 AudioTranscriptionModel = "whisper-1"

const AudioTranscriptionModelGPT4oMiniTranscribe AudioTranscriptionModel = "gpt-4o-mini-transcribe"

const AudioTranscriptionModelGPT4oMiniTranscribe2025\_12\_15 AudioTranscriptionModel = "gpt-4o-mini-transcribe-2025-12-15"

const AudioTranscriptionModelGPT4oTranscribe AudioTranscriptionModel = "gpt-4o-transcribe"

const AudioTranscriptionModelGPT4oTranscribeDiarize AudioTranscriptionModel = "gpt-4o-transcribe-diarize"

const AudioTranscriptionModelGPTRealtimeWhisper AudioTranscriptionModel = "gpt-realtime-whisper"

Prompt stringOptional

An optional text to guide the model’s style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://platform.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example “expect words related to technology”.
Prompt is not supported with `gpt-realtime-whisper` in GA Realtime sessions.

TurnDetection RealtimeSessionCreateResponseAudioInputTurnDetectionUnionOptional

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with “uhhm”, the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

For `gpt-realtime-whisper` transcription sessions, turn detection must be
set to `null`; VAD is not supported.

One of the following:

type RealtimeSessionCreateResponseAudioInputTurnDetectionServerVad struct{…}

Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.

Type ServerVad

Type of turn detection, `server_vad` to turn on simple Server VAD.

CreateResponse boolOptional

Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

IdleTimeoutMs int64Optional

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

InterruptResponse boolOptional

Whether or not to automatically interrupt (cancel) any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

PrefixPaddingMs int64Optional

Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

SilenceDurationMs int64Optional

Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

Threshold float64Optional

Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

type RealtimeSessionCreateResponseAudioInputTurnDetectionSemanticVad struct{…}

Server-side semantic turn detection which uses a model to determine when the user has finished speaking.

Type SemanticVad

Type of turn detection, `semantic_vad` to turn on Semantic VAD.

CreateResponse boolOptional

Whether or not to automatically generate a response when a VAD stop event occurs.

Eagerness stringOptional

Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.

One of the following:

const RealtimeSessionCreateResponseAudioInputTurnDetectionSemanticVadEagernessLow RealtimeSessionCreateResponseAudioInputTurnDetectionSemanticVadEagerness = "low"

const RealtimeSessionCreateResponseAudioInputTurnDetectionSemanticVadEagernessMedium RealtimeSessionCreateResponseAudioInputTurnDetectionSemanticVadEagerness = "medium"

const RealtimeSessionCreateResponseAudioInputTurnDetectionSemanticVadEagernessHigh RealtimeSessionCreateResponseAudioInputTurnDetectionSemanticVadEagerness = "high"

const RealtimeSessionCreateResponseAudioInputTurnDetectionSemanticVadEagernessAuto RealtimeSessionCreateResponseAudioInputTurnDetectionSemanticVadEagerness = "auto"

InterruptResponse boolOptional

Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

Output RealtimeSessionCreateResponseAudioOutputOptional

Format [RealtimeAudioFormatsUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))Optional

The format of the output audio.

One of the following:

type RealtimeAudioFormatsAudioPCM struct{…}

The PCM audio format. Only a 24kHz sample rate is supported.

Rate int64Optional

The sample rate of the audio. Always `24000`.

Type stringOptional

The audio format. Always `audio/pcm`.

type RealtimeAudioFormatsAudioPCMU struct{…}

The G.711 μ-law format.

Type stringOptional

The audio format. Always `audio/pcmu`.

type RealtimeAudioFormatsAudioPCMA struct{…}

The G.711 A-law format.

Type stringOptional

The audio format. Always `audio/pcma`.

Speed float64Optional

The speed of the model’s spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it’s
also possible to prompt the model to speak faster or slower.

maximum1.5

minimum0.25

Voice stringOptional

The voice the model uses to respond. Voice cannot be changed during the
session once the model has responded with audio at least once. Current
voice options are `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`,
`shimmer`, `verse`, `marin`, and `cedar`. We recommend `marin` and `cedar` for
best quality.

One of the following:

string

string

One of the following:

const RealtimeSessionCreateResponseAudioOutputVoiceAlloy RealtimeSessionCreateResponseAudioOutputVoice = "alloy"

const RealtimeSessionCreateResponseAudioOutputVoiceAsh RealtimeSessionCreateResponseAudioOutputVoice = "ash"

const RealtimeSessionCreateResponseAudioOutputVoiceBallad RealtimeSessionCreateResponseAudioOutputVoice = "ballad"

const RealtimeSessionCreateResponseAudioOutputVoiceCoral RealtimeSessionCreateResponseAudioOutputVoice = "coral"

const RealtimeSessionCreateResponseAudioOutputVoiceEcho RealtimeSessionCreateResponseAudioOutputVoice = "echo"

const RealtimeSessionCreateResponseAudioOutputVoiceSage RealtimeSessionCreateResponseAudioOutputVoice = "sage"

const RealtimeSessionCreateResponseAudioOutputVoiceShimmer RealtimeSessionCreateResponseAudioOutputVoice = "shimmer"

const RealtimeSessionCreateResponseAudioOutputVoiceVerse RealtimeSessionCreateResponseAudioOutputVoice = "verse"

const RealtimeSessionCreateResponseAudioOutputVoiceMarin RealtimeSessionCreateResponseAudioOutputVoice = "marin"

const RealtimeSessionCreateResponseAudioOutputVoiceCedar RealtimeSessionCreateResponseAudioOutputVoice = "cedar"

ExpiresAt int64Optional

Expiration timestamp for the session, in seconds since epoch.

formatunixtime

Include []stringOptional

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

Instructions stringOptional

The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. “be extremely succinct”, “act friendly”, “here are examples of good responses”) and on audio behavior (e.g. “talk quickly”, “inject emotion into your voice”, “laugh frequently”). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

MaxOutputTokens RealtimeSessionCreateResponseMaxOutputTokensUnionOptional

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

One of the following:

int64

type Inf string

Model RealtimeSessionCreateResponseModelOptional

The Realtime model used for this session.

One of the following:

string

type RealtimeSessionCreateResponseModel string

The Realtime model used for this session.

One of the following:

const RealtimeSessionCreateResponseModelGPTRealtime RealtimeSessionCreateResponseModel = "gpt-realtime"

const RealtimeSessionCreateResponseModelGPTRealtime1\_5 RealtimeSessionCreateResponseModel = "gpt-realtime-1.5"

const RealtimeSessionCreateResponseModelGPTRealtime2 RealtimeSessionCreateResponseModel = "gpt-realtime-2"

const RealtimeSessionCreateResponseModelGPTRealtime2025\_08\_28 RealtimeSessionCreateResponseModel = "gpt-realtime-2025-08-28"

const RealtimeSessionCreateResponseModelGPT4oRealtimePreview RealtimeSessionCreateResponseModel = "gpt-4o-realtime-preview"

const RealtimeSessionCreateResponseModelGPT4oRealtimePreview2024\_10\_01 RealtimeSessionCreateResponseModel = "gpt-4o-realtime-preview-2024-10-01"

const RealtimeSessionCreateResponseModelGPT4oRealtimePreview2024\_12\_17 RealtimeSessionCreateResponseModel = "gpt-4o-realtime-preview-2024-12-17"

const RealtimeSessionCreateResponseModelGPT4oRealtimePreview2025\_06\_03 RealtimeSessionCreateResponseModel = "gpt-4o-realtime-preview-2025-06-03"

const RealtimeSessionCreateResponseModelGPT4oMiniRealtimePreview RealtimeSessionCreateResponseModel = "gpt-4o-mini-realtime-preview"

const RealtimeSessionCreateResponseModelGPT4oMiniRealtimePreview2024\_12\_17 RealtimeSessionCreateResponseModel = "gpt-4o-mini-realtime-preview-2024-12-17"

const RealtimeSessionCreateResponseModelGPTRealtimeMini RealtimeSessionCreateResponseModel = "gpt-realtime-mini"

const RealtimeSessionCreateResponseModelGPTRealtimeMini2025\_10\_06 RealtimeSessionCreateResponseModel = "gpt-realtime-mini-2025-10-06"

const RealtimeSessionCreateResponseModelGPTRealtimeMini2025\_12\_15 RealtimeSessionCreateResponseModel = "gpt-realtime-mini-2025-12-15"

const RealtimeSessionCreateResponseModelGPTAudio1\_5 RealtimeSessionCreateResponseModel = "gpt-audio-1.5"

const RealtimeSessionCreateResponseModelGPTAudioMini RealtimeSessionCreateResponseModel = "gpt-audio-mini"

const RealtimeSessionCreateResponseModelGPTAudioMini2025\_10\_06 RealtimeSessionCreateResponseModel = "gpt-audio-mini-2025-10-06"

const RealtimeSessionCreateResponseModelGPTAudioMini2025\_12\_15 RealtimeSessionCreateResponseModel = "gpt-audio-mini-2025-12-15"

OutputModalities []stringOptional

The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

One of the following:

const RealtimeSessionCreateResponseOutputModalityText RealtimeSessionCreateResponseOutputModality = "text"

const RealtimeSessionCreateResponseOutputModalityAudio RealtimeSessionCreateResponseOutputModality = "audio"

Prompt [ResponsePrompt](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_prompt%20%3E%20(schema))Optional

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

ID string

The unique identifier of the prompt template to use.

Variables map[string, ResponsePromptVariableUnion]Optional

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

One of the following:

string

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type ResponseInputImage struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail ResponseInputImageDetail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

const ResponseInputImageDetailLow ResponseInputImageDetail = "low"

const ResponseInputImageDetailHigh ResponseInputImageDetail = "high"

const ResponseInputImageDetailAuto ResponseInputImageDetail = "auto"

const ResponseInputImageDetailOriginal ResponseInputImageDetail = "original"

Type InputImage

The type of the input item. Always `input_image`.

FileID stringOptional

The ID of the file to be sent to the model.

ImageURL stringOptional

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

type ResponseInputFile struct{…}

A file input to the model.

Type InputFile

The type of the input item. Always `input_file`.

Detail ResponseInputFileDetailOptional

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

const ResponseInputFileDetailLow ResponseInputFileDetail = "low"

const ResponseInputFileDetailHigh ResponseInputFileDetail = "high"

FileData stringOptional

The content of the file to be sent to the model.

FileID stringOptional

The ID of the file to be sent to the model.

FileURL stringOptional

The URL of the file to be sent to the model.

formaturi

Filename stringOptional

The name of the file to be sent to the model.

Version stringOptional

Optional version of the prompt template.

Reasoning [RealtimeReasoning](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning%20%3E%20(schema))Optional

Configuration for reasoning-capable Realtime models such as `gpt-realtime-2`.

Effort [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema))Optional

Constrains effort on reasoning for reasoning-capable Realtime models such as
`gpt-realtime-2`.

One of the following:

const RealtimeReasoningEffortMinimal [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)) = "minimal"

const RealtimeReasoningEffortLow [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)) = "low"

const RealtimeReasoningEffortMedium [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)) = "medium"

const RealtimeReasoningEffortHigh [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)) = "high"

const RealtimeReasoningEffortXhigh [RealtimeReasoningEffort](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_reasoning_effort%20%3E%20(schema)) = "xhigh"

ToolChoice RealtimeSessionCreateResponseToolChoiceUnionOptional

How the model chooses tools. Provide one of the string modes or force a specific
function/MCP tool.

One of the following:

type ToolChoiceOptions string

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

One of the following:

const ToolChoiceOptionsNone [ToolChoiceOptions](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) = "none"

const ToolChoiceOptionsAuto [ToolChoiceOptions](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) = "auto"

const ToolChoiceOptionsRequired [ToolChoiceOptions](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) = "required"

type ToolChoiceFunction struct{…}

Use this option to force the model to call a specific function.

Name string

The name of the function to call.

Type Function

For function calling, the type is always `function`.

type ToolChoiceMcp struct{…}

Use this option to force the model to call a specific tool on a remote MCP server.

ServerLabel string

The label of the MCP server to use.

Type Mcp

For MCP tools, the type is always `mcp`.

Name stringOptional

The name of the tool to call on the server.

Tools []RealtimeSessionCreateResponseToolUnionOptional

Tools available to the model.

One of the following:

type RealtimeFunctionTool struct{…}

Description stringOptional

The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

Name stringOptional

The name of the function.

Parameters anyOptional

Parameters of the function in JSON Schema.

Type RealtimeFunctionToolTypeOptional

The type of the tool, i.e. `function`.

type RealtimeSessionCreateResponseToolMcpTool struct{…}

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

ServerLabel string

A label for this MCP server, used to identify it in tool calls.

Type Mcp

The type of the MCP tool. Always `mcp`.

AllowedTools RealtimeSessionCreateResponseToolMcpToolAllowedToolsUnionOptional

List of allowed tool names or a filter object.

One of the following:

type RealtimeSessionCreateResponseToolMcpToolAllowedToolsMcpAllowedTools []string

A string array of allowed tool names

type RealtimeSessionCreateResponseToolMcpToolAllowedToolsMcpToolFilter struct{…}

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Authorization stringOptional

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

ConnectorID stringOptional

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

const RealtimeSessionCreateResponseToolMcpToolConnectorIDConnectorDropbox RealtimeSessionCreateResponseToolMcpToolConnectorID = "connector\_dropbox"

const RealtimeSessionCreateResponseToolMcpToolConnectorIDConnectorGmail RealtimeSessionCreateResponseToolMcpToolConnectorID = "connector\_gmail"

const RealtimeSessionCreateResponseToolMcpToolConnectorIDConnectorGooglecalendar RealtimeSessionCreateResponseToolMcpToolConnectorID = "connector\_googlecalendar"

const RealtimeSessionCreateResponseToolMcpToolConnectorIDConnectorGoogledrive RealtimeSessionCreateResponseToolMcpToolConnectorID = "connector\_googledrive"

const RealtimeSessionCreateResponseToolMcpToolConnectorIDConnectorMicrosoftteams RealtimeSessionCreateResponseToolMcpToolConnectorID = "connector\_microsoftteams"

const RealtimeSessionCreateResponseToolMcpToolConnectorIDConnectorOutlookcalendar RealtimeSessionCreateResponseToolMcpToolConnectorID = "connector\_outlookcalendar"

const RealtimeSessionCreateResponseToolMcpToolConnectorIDConnectorOutlookemail RealtimeSessionCreateResponseToolMcpToolConnectorID = "connector\_outlookemail"

const RealtimeSessionCreateResponseToolMcpToolConnectorIDConnectorSharepoint RealtimeSessionCreateResponseToolMcpToolConnectorID = "connector\_sharepoint"

DeferLoading boolOptional

Whether this MCP tool is deferred and discovered via tool search.

Headers map[string, string]Optional

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

RequireApproval RealtimeSessionCreateResponseToolMcpToolRequireApprovalUnionOptional

Specify which of the MCP server’s tools require approval.

One of the following:

type RealtimeSessionCreateResponseToolMcpToolRequireApprovalMcpToolApprovalFilter struct{…}

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Always RealtimeSessionCreateResponseToolMcpToolRequireApprovalMcpToolApprovalFilterAlwaysOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Never RealtimeSessionCreateResponseToolMcpToolRequireApprovalMcpToolApprovalFilterNeverOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

type RealtimeSessionCreateResponseToolMcpToolRequireApprovalMcpToolApprovalSetting string

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

const RealtimeSessionCreateResponseToolMcpToolRequireApprovalMcpToolApprovalSettingAlways RealtimeSessionCreateResponseToolMcpToolRequireApprovalMcpToolApprovalSetting = "always"

const RealtimeSessionCreateResponseToolMcpToolRequireApprovalMcpToolApprovalSettingNever RealtimeSessionCreateResponseToolMcpToolRequireApprovalMcpToolApprovalSetting = "never"

ServerDescription stringOptional

Optional description of the MCP server, used to provide more context.

ServerURL stringOptional

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

TunnelID stringOptional

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

Tracing RealtimeSessionCreateResponseTracingUnionOptional

Realtime API can write session traces to the [Traces Dashboard](https://platform.openai.com/logs?api=traces). Set to null to disable tracing. Once
tracing is enabled for a session, the configuration cannot be modified.

`auto` will create a trace for the session with default values for the
workflow name, group id, and metadata.

One of the following:

type Auto string

Enables tracing and sets default values for tracing configuration options. Always `auto`.

type RealtimeSessionCreateResponseTracingTracingConfiguration struct{…}

Granular configuration for tracing.

GroupID stringOptional

The group id to attach to this trace to enable filtering and
grouping in the Traces Dashboard.

Metadata anyOptional

The arbitrary metadata to attach to this trace to enable
filtering in the Traces Dashboard.

WorkflowName stringOptional

The name of the workflow to attach to this trace. This is used to
name the trace in the Traces Dashboard.

Truncation [RealtimeTruncationUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_truncation%20%3E%20(schema))Optional

When the number of tokens in a conversation exceeds the model’s input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model’s context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.

Clients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.

Truncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.

Truncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model’s input token limit.

One of the following:

type RealtimeTruncationRealtimeTruncationStrategy string

The truncation strategy to use for the session. `auto` is the default truncation strategy. `disabled` will disable truncation and emit errors when the conversation exceeds the input token limit.

One of the following:

const RealtimeTruncationRealtimeTruncationStrategyAuto RealtimeTruncationRealtimeTruncationStrategy = "auto"

const RealtimeTruncationRealtimeTruncationStrategyDisabled RealtimeTruncationRealtimeTruncationStrategy = "disabled"

type RealtimeTruncationRetentionRatio struct{…}

Retain a fraction of the conversation tokens when the conversation exceeds the input token limit. This allows you to amortize truncations across multiple turns, which can help improve cached token usage.

RetentionRatio float64

Fraction of post-instruction conversation tokens to retain (`0.0` - `1.0`) when the conversation exceeds the input token limit. Setting this to `0.8` means that messages will be dropped until 80% of the maximum allowed tokens are used. This helps reduce the frequency of truncations and improve cache rates.

minimum0

maximum1

Type RetentionRatio

Use retention ratio truncation.

TokenLimits RealtimeTruncationRetentionRatioTokenLimitsOptional

Optional custom token limits for this truncation strategy. If not provided, the model’s default token limits will be used.

PostInstructions int64Optional

Maximum tokens allowed in the conversation after instructions (which including tool definitions). For example, setting this to 5,000 would mean that truncation would occur when the conversation exceeds 5,000 tokens after instructions. This cannot be higher than the model’s context window size minus the maximum output tokens.

minimum0

type RealtimeTranscriptionSessionCreateResponse struct{…}

A Realtime transcription session configuration object.

ID string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

Object string

The object type. Always `realtime.transcription_session`.

Type Transcription

The type of session. Always `transcription` for transcription sessions.

Audio RealtimeTranscriptionSessionCreateResponseAudioOptional

Configuration for input audio for the session.

Input RealtimeTranscriptionSessionCreateResponseAudioInputOptional

Format [RealtimeAudioFormatsUnion](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))Optional

The PCM audio format. Only a 24kHz sample rate is supported.

One of the following:

type RealtimeAudioFormatsAudioPCM struct{…}

The PCM audio format. Only a 24kHz sample rate is supported.

Rate int64Optional

The sample rate of the audio. Always `24000`.

Type stringOptional

The audio format. Always `audio/pcm`.

type RealtimeAudioFormatsAudioPCMU struct{…}

The G.711 μ-law format.

Type stringOptional

The audio format. Always `audio/pcmu`.

type RealtimeAudioFormatsAudioPCMA struct{…}

The G.711 A-law format.

Type stringOptional

The audio format. Always `audio/pcma`.

NoiseReduction RealtimeTranscriptionSessionCreateResponseAudioInputNoiseReductionOptional

Configuration for input audio noise reduction.

Type [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))Optional

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

One of the following:

const NoiseReductionTypeNearField [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema)) = "near\_field"

const NoiseReductionTypeFarField [NoiseReductionType](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema)) = "far\_field"

Transcription [AudioTranscription](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema))Optional

Delay AudioTranscriptionDelayOptional

Controls how long the model waits before emitting transcription text.
Higher values can improve transcription accuracy at the cost of latency.
Only supported with `gpt-realtime-whisper` in GA Realtime sessions.

One of the following:

const AudioTranscriptionDelayMinimal AudioTranscriptionDelay = "minimal"

const AudioTranscriptionDelayLow AudioTranscriptionDelay = "low"

const AudioTranscriptionDelayMedium AudioTranscriptionDelay = "medium"

const AudioTranscriptionDelayHigh AudioTranscriptionDelay = "high"

const AudioTranscriptionDelayXhigh AudioTranscriptionDelay = "xhigh"

Language stringOptional

The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

Model AudioTranscriptionModelOptional

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

One of the following:

string

type AudioTranscriptionModel string

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

One of the following:

const AudioTranscriptionModelWhisper1 AudioTranscriptionModel = "whisper-1"

const AudioTranscriptionModelGPT4oMiniTranscribe AudioTranscriptionModel = "gpt-4o-mini-transcribe"

const AudioTranscriptionModelGPT4oMiniTranscribe2025\_12\_15 AudioTranscriptionModel = "gpt-4o-mini-transcribe-2025-12-15"

const AudioTranscriptionModelGPT4oTranscribe AudioTranscriptionModel = "gpt-4o-transcribe"

const AudioTranscriptionModelGPT4oTranscribeDiarize AudioTranscriptionModel = "gpt-4o-transcribe-diarize"

const AudioTranscriptionModelGPTRealtimeWhisper AudioTranscriptionModel = "gpt-realtime-whisper"

Prompt stringOptional

An optional text to guide the model’s style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://platform.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example “expect words related to technology”.
Prompt is not supported with `gpt-realtime-whisper` in GA Realtime sessions.

TurnDetection [RealtimeTranscriptionSessionTurnDetection](/api/reference/go/resources/realtime#(resource)%20realtime.client_secrets%20%3E%20(model)%20realtime_transcription_session_turn_detection%20%3E%20(schema))Optional

Configuration for turn detection. Can be set to `null` to turn off. Server
VAD means that the model will detect the start and end of speech based on
audio volume and respond at the end of user speech. For `gpt-realtime-whisper`, this must be `null`; VAD is not supported.

PrefixPaddingMs int64Optional

Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

SilenceDurationMs int64Optional

Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

Threshold float64Optional

Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

Type stringOptional

Type of turn detection, only `server_vad` is currently supported.

ExpiresAt int64Optional

Expiration timestamp for the session, in seconds since epoch.

formatunixtime

Include []stringOptional

Additional fields to include in server outputs.

* `item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

Value string

The generated client secret value.

### Create client secret

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
  "github.com/openai/openai-go/realtime"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  clientSecret, err := client.Realtime.ClientSecrets.New(context.TODO(), realtime.ClientSecretNewParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", clientSecret.ExpiresAt)

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
