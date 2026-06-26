<!-- source: https://developers.openai.com/api/reference/python/resources/audio/subresources/translations/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Audio](/api/reference/python/resources/audio)

[Translations](/api/reference/python/resources/audio/subresources/translations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create translation

audio.translations.create(TranslationCreateParams\*\*kwargs)  -> [TranslationCreateResponse](/api/reference/python/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_create_response%20%3E%20(schema))

POST/audio/translations

Translates audio into English.

##### ParametersExpand Collapse

file: [FileTypes](/api/reference/python/resources/audio/subresources/translations/methods/create#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20file%20%3E%20(schema))

The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

model: Union[str, [AudioModel](/api/reference/python/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema))]

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

One of the following:

str

Literal["whisper-1", "gpt-4o-transcribe", "gpt-4o-mini-transcribe", 2 more]

One of the following:

"whisper-1"

"gpt-4o-transcribe"

"gpt-4o-mini-transcribe"

"gpt-4o-mini-transcribe-2025-12-15"

"gpt-4o-transcribe-diarize"

prompt: Optional[str]

An optional text to guide the model’s style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should be in English.

response\_format: Optional[Literal["json", "text", "srt", 2 more]]

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

One of the following:

"json"

"text"

"srt"

"verbose\_json"

"vtt"

temperature: Optional[float]

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

##### ReturnsExpand Collapse

[TranslationCreateResponse](/api/reference/python/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_create_response%20%3E%20(schema))

One of the following:

class Translation: …

text: str

class TranslationVerbose: …

duration: float

The duration of the input audio.

formatdouble

language: str

The language of the output translation (always `english`).

text: str

The translated text.

segments: Optional[List[[TranscriptionSegment](/api/reference/python/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema))]]

Segments of the translated text and their corresponding details.

id: int

Unique identifier of the segment.

avg\_logprob: float

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: float

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end: float

End time of the segment in seconds.

formatdouble

no\_speech\_prob: float

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: int

Seek offset of the segment.

start: float

Start time of the segment in seconds.

formatdouble

temperature: float

Temperature parameter used for generating the segment.

formatfloat

text: str

Text content of the segment.

tokens: List[int]

Array of token IDs for the text content.

### Create translation

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

audio_file = open("speech.mp3", "rb")
transcript = client.audio.translations.create(
  model="whisper-1",
  file=audio_file

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"

##### Returns Examples

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
