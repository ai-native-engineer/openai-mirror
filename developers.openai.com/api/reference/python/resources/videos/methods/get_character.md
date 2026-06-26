<!-- source: https://developers.openai.com/api/reference/python/resources/videos/methods/get_character/ -->

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

# Fetch a character.

videos.get\_character(strcharacter\_id)  -> [VideoGetCharacterResponse](/api/reference/python/resources/videos#(resource)%20videos%20%3E%20(model)%20video_get_character_response%20%3E%20(schema))

GET/videos/characters/{character\_id}

Fetch a character.

##### ParametersExpand Collapse

character\_id: str

##### ReturnsExpand Collapse

class VideoGetCharacterResponse: …

id: Optional[str]

Identifier for the character creation cameo.

created\_at: int

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: Optional[str]

Display name for the character.

### Fetch a character.

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
response = client.videos.get_character(
    "char_123",
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
