<!-- source: https://developers.openai.com/api/reference/typescript/resources/videos/methods/get_character/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Videos](/api/reference/typescript/resources/videos)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Fetch a character.

client.videos.getCharacter(stringcharacterID, RequestOptionsoptions?): [VideoGetCharacterResponse](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_get_character_response%20%3E%20(schema)) { id, created\_at, name }

GET/videos/characters/{character\_id}

Fetch a character.

##### ParametersExpand Collapse

characterID: string

##### ReturnsExpand Collapse

VideoGetCharacterResponse { id, created\_at, name }

id: string | null

Identifier for the character creation cameo.

created\_at: number

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: string | null

Display name for the character.

### Fetch a character.

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

const response = await client.videos.getCharacter('char_123');

console.log(response.id);

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "name": "name"
