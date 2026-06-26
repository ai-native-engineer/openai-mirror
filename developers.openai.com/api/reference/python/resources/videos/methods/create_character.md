<!-- source: https://developers.openai.com/api/reference/python/resources/videos/methods/create_character/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Videos](/api/reference/python/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create a character from an uploaded video.

videos.create\_character(VideoCreateCharacterParams\*\*kwargs)  -> [VideoCreateCharacterResponse](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_character_response%20%3E%20(schema))

POST/videos/characters

Create a character from an uploaded video.

##### ParametersExpand Collapse

name: str

Display name for this API character.

maxLength80

minLength1

video: [FileTypes](/api/reference/python/resources/videos/methods/create_character#(resource)%20videos%20%3E%20(method)%20create_character%20%3E%20(params)%20default%20%3E%20(param)%20video%20%3E%20(schema))

Video file used to create a character.

##### ReturnsExpand Collapse

class VideoCreateCharacterResponse: …

id: Optional[str]

Identifier for the character creation cameo.

created\_at: int

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: Optional[str]

Display name for the character.

### Create a character from an uploaded video.

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
response = client.videos.create_character(
    name="x",
    video=b"Example data",
print(response.id)

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"
