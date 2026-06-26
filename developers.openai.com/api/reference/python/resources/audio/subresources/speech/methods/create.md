<!-- source: https://developers.openai.com/api/reference/python/resources/audio/subresources/speech/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Audio](/api/reference/python/resources/audio)

[Speech](/api/reference/python/resources/audio/subresources/speech)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create speech

audio.speech.create(SpeechCreateParams\*\*kwargs)  -> BinaryResponseContent

POST/audio/speech

Generates audio from the input text.

Returns the audio file content, or a stream of audio events.

##### ParametersExpand Collapse

input: str

The text to generate audio for. The maximum length is 4096 characters.

maxLength4096

model: Union[str, [SpeechModel](/api/reference/python/resources/audio#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema))]

One of the available [TTS models](https://platform.openai.com/docs/models#tts): `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

One of the following:

str

Literal["tts-1", "tts-1-hd", "gpt-4o-mini-tts", "gpt-4o-mini-tts-2025-12-15"]

One of the following:

"tts-1"

"tts-1-hd"

"gpt-4o-mini-tts"

"gpt-4o-mini-tts-2025-12-15"

voice: [Voice](/api/reference/python/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20voice%20%3E%20(schema))

The voice to use when generating the audio. Supported built-in voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. You may also provide a custom voice object with an `id`, for example `{ "id": "voice_1234" }`. Previews of the voices are available in the [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).

One of the following:

str

Literal["alloy", "ash", "ballad", 7 more]

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

class VoiceID: …

Custom voice reference.

id: str

The custom voice ID, e.g. `voice_1234`.

instructions: Optional[str]

Control the voice of your generated audio with additional instructions. Does not work with `tts-1` or `tts-1-hd`.

maxLength4096

response\_format: Optional[Literal["mp3", "opus", "aac", 3 more]]

The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

One of the following:

"mp3"

"opus"

"aac"

"flac"

"wav"

"pcm"

speed: Optional[float]

The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

minimum0.25

maximum4

stream\_format: Optional[Literal["sse", "audio"]]

The format to stream the audio in. Supported formats are `sse` and `audio`. `sse` is not supported for `tts-1` or `tts-1-hd`.

One of the following:

"sse"

"audio"

##### ReturnsExpand Collapse

BinaryResponseContent

### Create speech

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from pathlib import Path
import openai

speech_file_path = Path(__file__).parent / "speech.mp3"
with openai.audio.speech.with_streaming_response.create(
  model="gpt-4o-mini-tts",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
) as response:
  response.stream_to_file(speech_file_path)

##### Returns Examples
