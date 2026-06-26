<!-- source: https://developers.openai.com/api/reference/resources/audio/subresources/speech/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Speech](/api/reference/resources/audio/subresources/speech)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create speech

POST/audio/speech

Generates audio from the input text.

Returns the audio file content, or a stream of audio events.

##### Body ParametersJSONExpand Collapse

input: string

The text to generate audio for. The maximum length is 4096 characters.

maxLength4096

model: string or [SpeechModel](/api/reference/resources/audio#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema))

One of the available [TTS models](/docs/models#tts): `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

One of the following:

string

SpeechModel = "tts-1" or "tts-1-hd" or "gpt-4o-mini-tts" or "gpt-4o-mini-tts-2025-12-15"

One of the following:

"tts-1"

"tts-1-hd"

"gpt-4o-mini-tts"

"gpt-4o-mini-tts-2025-12-15"

voice: string or "alloy" or "ash" or "ballad" or 7 more or object { id }

The voice to use when generating the audio. Supported built-in voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. You may also provide a custom voice object with an `id`, for example `{ "id": "voice_1234" }`. Previews of the voices are available in the [Text to speech guide](/docs/guides/text-to-speech#voice-options).

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

ID object { id }

Custom voice reference.

id: string

The custom voice ID, e.g. `voice_1234`.

instructions: optional string

Control the voice of your generated audio with additional instructions. Does not work with `tts-1` or `tts-1-hd`.

maxLength4096

response\_format: optional "mp3" or "opus" or "aac" or 3 more

The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

One of the following:

"mp3"

"opus"

"aac"

"flac"

"wav"

"pcm"

speed: optional number

The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

minimum0.25

maximum4

stream\_format: optional "sse" or "audio"

The format to stream the audio in. Supported formats are `sse` and `audio`. `sse` is not supported for `tts-1` or `tts-1-hd`.

One of the following:

"sse"

"audio"

DefaultSSE Stream Format

### Create speech

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini-tts",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "alloy"
  }' \
  --output speech.mp3

### Create speech

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini-tts",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "alloy",
    "stream_format": "sse"
  }'

##### Returns Examples
