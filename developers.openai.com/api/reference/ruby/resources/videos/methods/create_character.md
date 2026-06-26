<!-- source: https://developers.openai.com/api/reference/ruby/resources/videos/methods/create_character/ -->

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

# Create a character from an uploaded video.

videos.create\_character(\*\*kwargs) -> [VideoCreateCharacterResponse](/api/reference/ruby/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_character_response%20%3E%20(schema)) { id, created\_at, name }

POST/videos/characters

Create a character from an uploaded video.

##### ParametersExpand Collapse

name: String

Display name for this API character.

maxLength80

minLength1

video: FileInput

Video file used to create a character.

##### ReturnsExpand Collapse

class VideoCreateCharacterResponse { id, created\_at, name }

id: String

Identifier for the character creation cameo.

created\_at: Integer

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: String

Display name for the character.

### Create a character from an uploaded video.

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

response = openai.videos.create_character(name: "x", video: StringIO.new("Example data"))

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
