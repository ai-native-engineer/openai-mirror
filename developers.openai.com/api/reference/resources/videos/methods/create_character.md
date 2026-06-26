<!-- source: https://developers.openai.com/api/reference/resources/videos/methods/create_character/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Videos](/api/reference/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create a character from an uploaded video.

POST/videos/characters

Create a character from an uploaded video.

##### Body ParametersForm DataExpand Collapse

name: string

Display name for this API character.

maxLength80

minLength1

video: file

Video file used to create a character.

##### ReturnsExpand Collapse

id: string

Identifier for the character creation cameo.

created\_at: number

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: string

Display name for the character.

### Create a character from an uploaded video.

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/videos/characters \
    -H 'Content-Type: multipart/form-data' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -F name=x \
    -F 'video=@/path/to/video'

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"
