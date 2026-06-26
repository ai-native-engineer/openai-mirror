<!-- source: https://developers.openai.com/api/reference/resources/videos/methods/get_character/ -->

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

# Fetch a character.

GET/videos/characters/{character\_id}

Fetch a character.

##### Path ParametersExpand Collapse

character\_id: string

##### ReturnsExpand Collapse

id: string

Identifier for the character creation cameo.

created\_at: number

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: string

Display name for the character.

### Fetch a character.

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/videos/characters/$CHARACTER_ID \
    -H "Authorization: Bearer $OPENAI_API_KEY"

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"
