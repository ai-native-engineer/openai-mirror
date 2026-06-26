<!-- source: https://developers.openai.com/api/reference/resources/realtime/subresources/transcription_sessions/ -->

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

# Transcription Sessions

##### [Create transcription session](/api/reference/resources/realtime/subresources/transcription_sessions/methods/create)

Deprecated

POST/realtime/transcription\_sessions

##### ModelsExpand Collapse

TranscriptionSessionCreateResponse object { client\_secret, input\_audio\_format, input\_audio\_transcription, 2 more }

A new Realtime transcription session configuration.

When a session is created on the server via REST API, the session object
also contains an ephemeral key. Default TTL for keys is 10 minutes. This
property is not present when a session is updated via the WebSocket API.

client\_secret: object { expires\_at, value }

Ephemeral key returned by the API. Only present when the session is
created on the server via REST API.

expires\_at: number

Timestamp for when the token expires. Currently, all tokens expire
after one minute.

formatunixtime

value: string

Ephemeral key usable in client environments to authenticate connections
to the Realtime API. Use this in client-side environments rather than
a standard API token, which should only be used server-side.

input\_audio\_format: optional string

The format of input audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`.

input\_audio\_transcription: optional object { language, model, prompt }

Configuration of the transcription model.

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

modalities: optional array of "text" or "audio"

The set of modalities the model can respond with. To disable audio,
set this to [“text”].

One of the following:

"text"

"audio"

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
