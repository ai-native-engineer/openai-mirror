<!-- source: https://developers.openai.com/api/reference/ruby/resources/videos/methods/get_character/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Videos](/api/reference/ruby/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Fetch a character.

videos.get\_character(character\_id) -> [VideoGetCharacterResponse](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_get_character_response%20%3E%20(schema)) { id, created\_at, name }

GET/videos/characters/{character\_id}

Fetch a character.

##### ParametersExpand Collapse

character\_id: String

##### ReturnsExpand Collapse

class VideoGetCharacterResponse { id, created\_at, name }

id: String

Identifier for the character creation cameo.

created\_at: Integer

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: String

Display name for the character.

### Fetch a character.

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.videos.get_character("char_123")

puts(response)

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"
