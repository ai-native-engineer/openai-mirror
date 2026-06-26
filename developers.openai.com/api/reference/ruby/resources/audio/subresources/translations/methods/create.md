<!-- source: https://developers.openai.com/api/reference/ruby/resources/audio/subresources/translations/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Audio](/api/reference/ruby/resources/audio)

[Translations](/api/reference/ruby/resources/audio/subresources/translations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create translation

audio.translations.create(\*\*kwargs) -> [TranslationCreateResponse](/api/reference/ruby/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_create_response%20%3E%20(schema))

POST/audio/translations

Translates audio into English.

##### ParametersExpand Collapse

file: FileInput

The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

model: String | [AudioModel](/api/reference/ruby/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema))

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

One of the following:

String = String

AudioModel = :"whisper-1" | :"gpt-4o-transcribe" | :"gpt-4o-mini-transcribe" | 2 more

One of the following:

:"whisper-1"

:"gpt-4o-transcribe"

:"gpt-4o-mini-transcribe"

:"gpt-4o-mini-transcribe-2025-12-15"

:"gpt-4o-transcribe-diarize"

prompt: String

An optional text to guide the model’s style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should be in English.

response\_format: :json | :text | :srt | 2 more

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

One of the following:

:json

:text

:srt

:verbose\_json

:vtt

temperature: Float

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

##### ReturnsExpand Collapse

TranslationCreateResponse = [Translation](/api/reference/ruby/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation%20%3E%20(schema)) { text }  | [TranslationVerbose](/api/reference/ruby/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_verbose%20%3E%20(schema)) { duration, language, text, segments }

One of the following:

class Translation { text }

text: String

class TranslationVerbose { duration, language, text, segments }

duration: Float

The duration of the input audio.

formatdouble

language: String

The language of the output translation (always `english`).

text: String

The translated text.

segments: Array[[TranscriptionSegment](/api/reference/ruby/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more } ]

Segments of the translated text and their corresponding details.

id: Integer

Unique identifier of the segment.

avg\_logprob: Float

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: Float

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end\_: Float

End time of the segment in seconds.

formatdouble

no\_speech\_prob: Float

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: Integer

Seek offset of the segment.

start: Float

Start time of the segment in seconds.

formatdouble

temperature: Float

Temperature parameter used for generating the segment.

formatfloat

text: String

Text content of the segment.

tokens: Array[Integer]

Array of token IDs for the text content.

### Create translation

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

translation = openai.audio.translations.create(file: StringIO.new("Example data"), model: :"whisper-1")

puts(translation)

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"

##### Returns Examples

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
