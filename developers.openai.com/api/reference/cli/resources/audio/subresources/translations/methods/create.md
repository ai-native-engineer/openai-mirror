<!-- source: https://developers.openai.com/api/reference/cli/resources/audio/subresources/translations/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Audio](/api/reference/cli/resources/audio)

[Translations](/api/reference/cli/resources/audio/subresources/translations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create translation

$ openai audio:translations create

POST/audio/translations

Translates audio into English.

##### ParametersExpand Collapse

--file: file path

The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

--model: string or [AudioModel](/api/reference/cli/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema))

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

--prompt: optional string

An optional text to guide the model’s style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should be in English.

--response-format: optional "json" or "text" or "srt" or 2 more

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

--temperature: optional number

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

##### ReturnsExpand Collapse

unnamed\_schema\_1: [Translation](/api/reference/cli/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation%20%3E%20(schema)) { text }  or [TranslationVerbose](/api/reference/cli/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation_verbose%20%3E%20(schema)) { duration, language, text, segments }

translation: object { text }

text: string

translation\_verbose: object { duration, language, text, segments }

duration: number

The duration of the input audio.

language: string

The language of the output translation (always `english`).

text: string

The translated text.

segments: optional array of [TranscriptionSegment](/api/reference/cli/resources/audio#(resource)%20audio.transcriptions%20%3E%20(model)%20transcription_segment%20%3E%20(schema)) { id, avg\_logprob, compression\_ratio, 7 more }

Segments of the translated text and their corresponding details.

id: number

Unique identifier of the segment.

avg\_logprob: number

Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

compression\_ratio: number

Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

end: number

End time of the segment in seconds.

no\_speech\_prob: number

Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

seek: number

Seek offset of the segment.

start: number

Start time of the segment in seconds.

temperature: number

Temperature parameter used for generating the segment.

text: string

Text content of the segment.

tokens: array of number

Array of token IDs for the text content.

### Create translation

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai audio:translations create \
  --api-key 'My API Key' \
  --file 'Example data' \
  --model whisper-1

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"

##### Returns Examples

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
