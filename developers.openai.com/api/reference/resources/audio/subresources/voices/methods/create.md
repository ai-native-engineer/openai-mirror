<!-- source: https://developers.openai.com/api/reference/resources/audio/subresources/voices/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Voices](/api/reference/resources/audio/subresources/voices)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create voice

POST/audio/voices

Creates a custom voice.

##### Body ParametersForm DataExpand Collapse

audio\_sample: file

The sample audio recording file. Maximum size is 10 MiB.

Supported MIME types:
`audio/mpeg`, `audio/wav`, `audio/x-wav`, `audio/ogg`, `audio/aac`, `audio/flac`, `audio/webm`, `audio/mp4`.

consent: string

The consent recording ID (for example, `cons_1234`).

name: string

The name of the new voice.

##### ReturnsExpand Collapse

id: string

The voice identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the voice was created.

formatunixtime

name: string

The name of the voice.

object: "audio.voice"

The object type, which is always `audio.voice`.

### Create voice

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/audio/voices \
  -X POST \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "name=My new voice" \
  -F "consent=cons_1234" \
  -F "audio_sample=@$HOME/audio_sample.wav;type=audio/x-wav"

200 example

  "id": "id",
  "created_at": 0,
  "name": "name",
  "object": "audio.voice"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name",
  "object": "audio.voice"
