<!-- source: https://developers.openai.com/api/reference/resources/audio/subresources/voice_consents/methods/list/ -->

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

# List voice consents

GET/audio/voice\_consents

Returns a list of voice consent recordings.

##### Query ParametersExpand Collapse

after: optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

##### ReturnsExpand Collapse

data: array of object { id, created\_at, language, 2 more }

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

has\_more: boolean

object: "list"

first\_id: optional string

last\_id: optional string

### List voice consents

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/audio/voice_consents?limit=20 \
  -H "Authorization: Bearer $OPENAI_API_KEY"

200 example

  "data": [
      "id": "cons_1234",
      "created_at": 0,
      "language": "language",
      "name": "name",
      "object": "audio.voice_consent"
  ],
  "has_more": true,
  "object": "list",
  "first_id": "first_id",
  "last_id": "last_id"

##### Returns Examples

200 example

  "data": [
      "id": "cons_1234",
      "created_at": 0,
      "language": "language",
      "name": "name",
      "object": "audio.voice_consent"
  ],
  "has_more": true,
  "object": "list",
  "first_id": "first_id",
  "last_id": "last_id"
