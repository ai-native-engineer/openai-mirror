<!-- source: https://developers.openai.com/api/reference/resources/realtime/translation-server-events/ -->

[Skip to content](#_top)

Returned when an error occurs, which could be a client problem or a server
problem. Most errors are recoverable and the session will stay open, we
recommend to implementors to monitor and log error messages by default.

error: [RealtimeError](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_error%20%3E%20(schema)) { message, type, code, 2 more }

Details of the error.

message: string

A human-readable error message.

type: string

The type of error (e.g., "invalid\_request\_error", "server\_error").

code: optional string

Error code, if any.

event\_id: optional string

The event\_id of the client event that caused the error, if applicable.

param: optional string

Parameter related to the error, if any.

event\_id: string

The unique ID of the server event.

type: "error"

The event type, must be `error`.

OBJECT

### error

    "event_id": "event_890",
    "type": "error",
    "error": {
        "type": "invalid_request_error",
        "code": "invalid_event",
        "message": "The 'type' field is missing.",
        "param": null,
        "event_id": "event_567"

Returned when a translation session is created. Emitted automatically when a
new connection is established as the first server event. This event contains
the default translation session configuration.

event\_id: string

The unique ID of the server event.

session: [RealtimeTranslationSession](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_translation_session%20%3E%20(schema)) { id, audio, expires\_at, 2 more }

The translation session configuration.

id: string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

audio: object { input, output }

Configuration for translation input and output audio.

input: optional object { noise\_reduction, transcription }

noise\_reduction: optional object { type }

Optional input noise reduction.

type: [NoiseReductionType](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

One of the following:

"near\_field"

"far\_field"

transcription: optional object { model }

Optional source-language transcription. When configured, the server emits
`session.input_transcript.delta` events. Translation itself still runs from
the input audio stream.

model: string

The transcription model used for source transcript deltas.

output: optional object { language }

language: optional string

Target language for translated output audio and transcript deltas.

expires\_at: number

Expiration timestamp for the session, in seconds since epoch.

formatunixtime

model: string

The Realtime translation model used for this session. This field is set at
session creation and cannot be changed with `session.update`.

type: "translation"

The session type. Always `translation` for Realtime translation sessions.

type: "session.created"

The event type, must be `session.created`.

OBJECT

### session.created

  "type": "session.created",
  "event_id": "event_123",
  "session": {
    "id": "sess_123",
    "type": "translation",
    "model": "gpt-realtime-translate",
    "expires_at": 1714857600,
    "audio": {
      "input": {
        "transcription": {
          "model": "gpt-realtime-whisper",
          "language": "en"
        "noise_reduction": {
          "type": "near_field"
      "output": {
        "language": "fr"

Returned when a translation session is updated with a `session.update` event,
unless there is an error.

event\_id: string

The unique ID of the server event.

session: [RealtimeTranslationSession](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_translation_session%20%3E%20(schema)) { id, audio, expires\_at, 2 more }

The translation session configuration.

id: string

Unique identifier for the session that looks like `sess_1234567890abcdef`.

audio: object { input, output }

Configuration for translation input and output audio.

input: optional object { noise\_reduction, transcription }

noise\_reduction: optional object { type }

Optional input noise reduction.

type: [NoiseReductionType](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

One of the following:

"near\_field"

"far\_field"

transcription: optional object { model }

Optional source-language transcription. When configured, the server emits
`session.input_transcript.delta` events. Translation itself still runs from
the input audio stream.

model: string

The transcription model used for source transcript deltas.

output: optional object { language }

language: optional string

Target language for translated output audio and transcript deltas.

expires\_at: number

Expiration timestamp for the session, in seconds since epoch.

formatunixtime

model: string

The Realtime translation model used for this session. This field is set at
session creation and cannot be changed with `session.update`.

type: "translation"

The session type. Always `translation` for Realtime translation sessions.

type: "session.updated"

The event type, must be `session.updated`.

OBJECT

### session.updated

  "type": "session.updated",
  "event_id": "event_124",
  "session": {
    "id": "sess_123",
    "type": "translation",
    "model": "gpt-realtime-translate",
    "expires_at": 1714857600,
    "audio": {
      "input": {
        "transcription": {
          "model": "gpt-realtime-whisper",
          "language": "en"
        "noise_reduction": {
          "type": "near_field"
      "output": {
        "language": "es"

Returned when a realtime translation session is closed.

event\_id: string

The unique ID of the server event.

type: "session.closed"

The event type, must be `session.closed`.

OBJECT

### session.closed

  "event_id": "event_987",
  "type": "session.closed"

Returned when optional source-language transcript text is available. This event
is emitted only when `audio.input.transcription` is configured.

Transcript deltas are append-only text fragments. Clients should not insert
unconditional spaces between deltas.

delta: string

Append-only source-language transcript text.

event\_id: string

The unique ID of the server event.

type: "session.input\_transcript.delta"

The event type, must be `session.input_transcript.delta`.

elapsed\_ms: optional number

Timing metadata for stream alignment, derived from the translation frame
when available. It advances in 200 ms increments, but multiple transcript
deltas may share the same `elapsed_ms`. Treat it as alignment metadata,
not a unique transcript-delta identifier.

OBJECT

### session.input\_transcript.delta

  "event_id": "event_125",
  "type": "session.input_transcript.delta",
  "delta": " hear",
  "elapsed_ms": 1200

Returned when translated transcript text is available.

Transcript deltas are append-only text fragments. Clients should not insert
unconditional spaces between deltas.

delta: string

Append-only transcript text for the translated output audio.

event\_id: string

The unique ID of the server event.

type: "session.output\_transcript.delta"

The event type, must be `session.output_transcript.delta`.

elapsed\_ms: optional number

Timing metadata for stream alignment, derived from the translation frame
when available. It advances in 200 ms increments, but multiple transcript
deltas may share the same `elapsed_ms`. Treat it as alignment metadata,
not a unique transcript-delta identifier.

OBJECT

### session.output\_transcript.delta

  "event_id": "event_124",
  "type": "session.output_transcript.delta",
  "delta": " escuch",
  "elapsed_ms": 1200

Returned when translated output audio is available. Output audio deltas are
200 ms frames of PCM16 audio.

delta: string

Base64-encoded translated audio data.

event\_id: string

The unique ID of the server event.

type: "session.output\_audio.delta"

The event type, must be `session.output_audio.delta`.

channels: optional number

Number of audio channels.

elapsed\_ms: optional number

Timing metadata for stream alignment, derived from the translation frame
when available. Treat `elapsed_ms` as alignment metadata, not a unique
event identifier.

format: optional "pcm16"

Audio encoding for `delta`.

sample\_rate: optional number

Sample rate of the audio delta.

OBJECT

### session.output\_audio.delta

  "event_id": "event_123",
  "type": "session.output_audio.delta",
  "delta": "Base64EncodedAudioDelta",
  "sample_rate": 24000,
  "channels": 1,
  "format": "pcm16",
  "elapsed_ms": 1200
