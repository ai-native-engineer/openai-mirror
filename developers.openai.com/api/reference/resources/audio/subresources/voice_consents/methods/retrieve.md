<!-- source: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Audio](/api/reference/resources/audio)

[Voice Consents](/api/reference/resources/audio/subresources/voice_consents)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve voice consent

GET/audio/voice\_consents/{consent\_id}

Retrieves a voice consent recording.

##### Path ParametersExpand Collapse

consent\_id: string

##### ReturnsExpand Collapse

id: string

The consent recording identifier.

created\_at: number

The Unix timestamp (in seconds) for when the consent recording was created.

formatunixtime

language: string

The BCP 47 language tag for the consent phrase (for example, `en-US`).

name: string

The label provided when the consent recording was uploaded.

object: "audio.voice\_consent"

The object type, which is always `audio.voice_consent`.

### Retrieve voice consent

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/audio/voice_consents/cons_1234 \
  -H "Authorization: Bearer $OPENAI_API_KEY"

200 example

  "id": "cons_1234",
  "created_at": 0,
  "language": "language",
  "name": "name",
  "object": "audio.voice_consent"

##### Returns Examples

200 example

  "id": "cons_1234",
  "created_at": 0,
  "language": "language",
  "name": "name",
  "object": "audio.voice_consent"
