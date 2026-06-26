<!-- source: https://developers.openai.com/api/reference/cli/resources/videos/methods/get_character/ -->

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

# Fetch a character.

$ openai videos get-character

GET/videos/characters/{character\_id}

Fetch a character.

##### ParametersExpand Collapse

--character-id: string

The identifier of the character to retrieve.

##### ReturnsExpand Collapse

VideoGetCharacterResponse: object { id, created\_at, name }

id: string

Identifier for the character creation cameo.

created\_at: number

Unix timestamp (in seconds) when the character was created.

name: string

Display name for the character.

### Fetch a character.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai videos get-character \
  --api-key 'My API Key' \
  --character-id char_123

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"
