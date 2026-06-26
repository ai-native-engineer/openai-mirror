<!-- source: https://developers.openai.com/api/reference/resources/realtime/translation-client-events/ -->

[Skip to content](#_top)

Send this event to update the translation session configuration. Translation
sessions support updates to `audio.output.language`, `audio.input.transcription`,
and `audio.input.noise_reduction`.

session: [RealtimeTranslationSessionUpdateRequest](/api/reference/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_translation_session_update_request%20%3E%20(schema)) { audio }

Translation session fields to update. The session `type` and `model` are set
at creation and cannot be changed with `session.update`.

audio: optional object { input, output }

Configuration for translation input and output audio.

input: optional object { noise\_reduction, transcription }

noise\_reduction: optional object { type }

Optional input noise reduction. Set to `null` to disable it.

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

The transcription model to use for source transcript deltas.

output: optional object { language }

language: optional string

Target language for translated output audio and transcript deltas.

type: "session.update"

The event type, must be `session.update`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

OBJECT

### session.update

  "type": "session.update",
  "session": {
    "audio": {
      "input": {
        "transcription": {
          "model": "gpt-realtime-whisper"
        "noise_reduction": null
      "output": {
        "language": "es"

Send this event to append audio bytes to the translation session input audio buffer.

WebSocket translation sessions accept base64-encoded 24 kHz PCM16 mono
little-endian raw audio bytes. Unsupported websocket audio formats return a
validation error because lower-quality audio materially degrades translation
quality.

Translation consumes 200 ms engine frames. For best realtime behavior, append
audio in 200 ms chunks. If a chunk is shorter, the server buffers it until it
has enough audio for one frame. If a chunk is longer, the server splits it into
200 ms frames and enqueues them back-to-back.

Keep appending silence while the session is active. If a client stops sending
audio and later resumes, model time treats the resumed audio as contiguous with
the previous audio rather than as a real-world pause.

audio: string

Base64-encoded 24 kHz PCM16 mono audio bytes.

type: "session.input\_audio\_buffer.append"

The event type, must be `session.input_audio_buffer.append`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

OBJECT

### session.input\_audio\_buffer.append

  "event_id": "event_456",
  "type": "session.input_audio_buffer.append",
  "audio": "Base64EncodedAudioData"

Gracefully close the realtime translation session. The server flushes pending
input audio and emits any remaining translated output before closing the
session.

type: "session.close"

The event type, must be `session.close`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

OBJECT

### session.close

  "event_id": "event_789",
  "type": "session.close"
