<!-- source: https://developers.openai.com/api/reference/resources/audio/subresources/translations/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Translations](/api/reference/resources/audio/subresources/translations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create translation

POST/audio/translations

Translates audio into English.

##### Body ParametersForm DataExpand Collapse

file: file

The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

model: string or [AudioModel](/api/reference/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema))

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

One of the following:

string

AudioModel = "whisper-1" or "gpt-4o-transcribe" or "gpt-4o-mini-transcribe" or 2 more

One of the following:

"whisper-1"

"gpt-4o-transcribe"

"gpt-4o-mini-transcribe"

"gpt-4o-mini-transcribe-2025-12-15"

"gpt-4o-transcribe-diarize"

prompt: optional string

An optional text to guide the model’s style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text#prompting) should be in English.

response\_format: optional "json" or "text" or "srt" or 2 more

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

One of the following:

"json"

"text"

"srt"

"verbose\_json"

"vtt"

temperature: optional number

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

##### ReturnsExpand Collapse

Translation object { text }

text: string

TranslationVerbose object { duration, language, text, segments }

duration: number

The duration of the input audio.

formatdouble

language: string

The language of the output translation (always `english`).

text: string

The translated text.

segments: optional array of [TranscriptionSegment](/api/reference/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more }

Segments of the translated text and their corresponding details.

id: number

Unique identifier of the segment.

avg\_logprob: number

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

formatfloat

compression\_ratio: number

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

formatfloat

end: number

End time of the segment in seconds.

formatdouble

no\_speech\_prob: number

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

formatfloat

seek: number

Seek offset of the segment.

start: number

Start time of the segment in seconds.

formatdouble

temperature: number

Temperature parameter used for generating the segment.

formatfloat

text: string

Text content of the segment.

tokens: array of number

Array of token IDs for the text content.

### Create translation

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/audio/translations \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@/path/to/file/german.m4a" \
  -F model="whisper-1"

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"

##### Returns Examples

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
