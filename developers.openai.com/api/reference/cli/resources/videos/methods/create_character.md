<!-- source: https://developers.openai.com/api/reference/cli/resources/videos/methods/create_character/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Videos](/api/reference/cli/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create a character from an uploaded video.

$ openai videos create-character

POST/videos/characters

Create a character from an uploaded video.

##### ParametersExpand Collapse

--name: string

Display name for this API character.

--video: file path

Video file used to create a character.

##### ReturnsExpand Collapse

VideoNewCharacterResponse: object { id, created\_at, name }

id: string

Identifier for the character creation cameo.

created\_at: number

Unix timestamp (in seconds) when the character was created.

name: string

Display name for the character.

### Create a character from an uploaded video.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai videos create-character \
  --api-key 'My API Key' \
  --name x \
  --video 'Example data'

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"
