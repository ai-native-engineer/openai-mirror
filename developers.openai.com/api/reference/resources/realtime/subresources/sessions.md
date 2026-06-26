<!-- source: https://developers.openai.com/api/reference/resources/realtime/subresources/sessions/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Realtime](/api/reference/resources/realtime)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Sessions

##### [Create session](/api/reference/resources/realtime/subresources/sessions/methods/create)

Deprecated

POST/realtime/sessions

##### ModelsExpand Collapse

SessionCreateResponse object { id, audio, expires\_at, 10 more }

A Realtime session configuration object.

id: optional string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

audio: optional object { input, output }

Configuration for input and output audio for the session.

input: optional object { format, noise\_reduction, transcription, turn\_detection }

format: optional [RealtimeAudioFormats](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The PCM audio format. Only a 24kHz sample rate is supported.

noise\_reduction: optional object { type }

Configuration for input audio noise reduction.

type: optional [NoiseReductionType](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

transcription: optional object { language, model, prompt }

Configuration for input audio transcription.

language: optional string

The language of the input audio.

model: optional string or "whisper-1" or "gpt-4o-mini-transcribe" or "gpt-4o-mini-transcribe-2025-12-15" or 3 more

The model used for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`.

One of the following:

string

"whisper-1" or "gpt-4o-mini-transcribe" or "gpt-4o-mini-transcribe-2025-12-15" or 3 more

The model used for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`, and `gpt-realtime-whisper`.

One of the following:

"whisper-1"

"gpt-4o-mini-transcribe"

"gpt-4o-mini-transcribe-2025-12-15"

"gpt-4o-transcribe"

"gpt-4o-transcribe-diarize"

"gpt-realtime-whisper"

prompt: optional string

The prompt configured for input audio transcription, when present.

turn\_detection: optional object { prefix\_padding\_ms, silence\_duration\_ms, threshold, type }

Configuration for turn detection.

prefix\_padding\_ms: optional number

silence\_duration\_ms: optional number

threshold: optional number

type: optional string

Type of turn detection, only `server_vad` is currently supported.

output: optional object { format, speed, voice }

format: optional [RealtimeAudioFormats](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The PCM audio format. Only a 24kHz sample rate is supported.

speed: optional number

voice: optional string or "alloy" or "ash" or "ballad" or 7 more

One of the following:

string

"alloy" or "ash" or "ballad" or 7 more

One of the following:

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

formatunixtime

include: optional array of "item.input\_audio\_transcription.logprobs"

Additional fields to include in server outputs.

* `item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

instructions: optional string

The default system instructions (i.e. system message) prepended to model
calls. This field allows the client to guide the model on desired
responses. The model can be instructed on response content and format,
(e.g. “be extremely succinct”, “act friendly”, “here are examples of good
responses”) and on audio behavior (e.g. “talk quickly”, “inject emotion
into your voice”, “laugh frequently”). The instructions are not guaranteed
to be followed by the model, but they provide guidance to the model on the
desired behavior.

Note that the server sets default instructions which will be used if this
field is not set and are visible in the `session.created` event at the
start of the session.

max\_output\_tokens: optional number or "inf"

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

One of the following:

number

"inf"

model: optional string

The Realtime model used for this session.

object: optional string

The object type. Always `realtime.session`.

output\_modalities: optional array of "text" or "audio"

The set of modalities the model can respond with. To disable audio,
set this to [“text”].

One of the following:

"text"

"audio"

tool\_choice: optional string

How the model chooses tools. Options are `auto`, `none`, `required`, or
specify a function.

tools: optional array of [RealtimeFunctionTool](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_function_tool%20%3E%20(schema)) { description, name, parameters, type }

Tools (functions) available to the model.

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

tracing: optional "auto" or object { group\_id, metadata, workflow\_name }

Configuration options for tracing. Set to null to disable tracing. Once
tracing is enabled for a session, the configuration cannot be modified.

`auto` will create a trace for the session with default values for the
workflow name, group id, and metadata.

One of the following:

"auto"

Default tracing mode for the session.

TracingConfiguration object { group\_id, metadata, workflow\_name }

Granular configuration for tracing.

group\_id: optional string

The group id to attach to this trace to enable filtering and
grouping in the traces dashboard.

metadata: optional unknown

The arbitrary metadata to attach to this trace to enable
filtering in the traces dashboard.

workflow\_name: optional string

The name of the workflow to attach to this trace. This is used to
name the trace in the traces dashboard.

turn\_detection: optional object { prefix\_padding\_ms, silence\_duration\_ms, threshold, type }

Configuration for turn detection. Can be set to `null` to turn off. Server
VAD means that the model will detect the start and end of speech based on
audio volume and respond at the end of user speech.

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
