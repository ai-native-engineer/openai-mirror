<!-- source: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/delete/ -->

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

# Delete voice consent

DELETE/audio/voice\_consents/{consent\_id}

Deletes a voice consent recording.

##### Path ParametersExpand Collapse

consent\_id: string

##### ReturnsExpand Collapse

id: string

The consent recording identifier.

deleted: boolean

object: "audio.voice\_consent"

### Delete voice consent

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
  -X DELETE \
  -H "Authorization: Bearer $OPENAI_API_KEY"

200 example

  "id": "cons_1234",
  "deleted": true,
  "object": "audio.voice_consent"

##### Returns Examples

200 example

  "id": "cons_1234",
  "deleted": true,
  "object": "audio.voice_consent"
