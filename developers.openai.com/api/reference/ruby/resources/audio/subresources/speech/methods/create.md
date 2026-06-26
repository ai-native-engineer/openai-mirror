<!-- source: https://developers.openai.com/api/reference/ruby/resources/audio/subresources/speech/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Audio](/api/reference/ruby/resources/audio)

[Speech](/api/reference/ruby/resources/audio/subresources/speech)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create speech

audio.speech.create(\*\*kwargs) -> StringIO

POST/audio/speech

Generates audio from the input text.

Returns the audio file content, or a stream of audio events.

##### ParametersExpand Collapse

input: String

The text to generate audio for. The maximum length is 4096 characters.

maxLength4096

model: String | [SpeechModel](/api/reference/ruby/resources/audio#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema))

One of the available [TTS models](https://platform.openai.com/docs/models#tts): `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

One of the following:

String = String

SpeechModel = :"tts-1" | :"tts-1-hd" | :"gpt-4o-mini-tts" | :"gpt-4o-mini-tts-2025-12-15"

One of the following:

:"tts-1"

:"tts-1-hd"

:"gpt-4o-mini-tts"

:"gpt-4o-mini-tts-2025-12-15"

voice: String | :alloy | :ash | :ballad | 7 more | ID{ id}

The voice to use when generating the audio. Supported built-in voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. You may also provide a custom voice object with an `id`, for example `{ "id": "voice_1234" }`. Previews of the voices are available in the [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).

One of the following:

String = String

Voice = :alloy | :ash | :ballad | 7 more

One of the following:

:alloy

:ash

:ballad

:coral

:echo

:sage

:shimmer

:verse

:marin

:cedar

class ID { id }

Custom voice reference.

id: String

The custom voice ID, e.g. `voice_1234`.

instructions: String

Control the voice of your generated audio with additional instructions. Does not work with `tts-1` or `tts-1-hd`.

maxLength4096

response\_format: :mp3 | :opus | :aac | 3 more

The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

One of the following:

:mp3

:opus

:aac

:flac

:wav

:pcm

speed: Float

The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

minimum0.25

maximum4

stream\_format: :sse | :audio

The format to stream the audio in. Supported formats are `sse` and `audio`. `sse` is not supported for `tts-1` or `tts-1-hd`.

One of the following:

:sse

:audio

##### ReturnsExpand Collapse

StringIO

### Create speech

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

speech = openai.audio.speech.create(input: "input", model: :"tts-1", voice: :alloy)

puts(speech)

##### Returns Examples
