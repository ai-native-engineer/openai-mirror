<!-- source: https://developers.openai.com/api/reference/typescript/resources/videos/methods/create_character/ -->

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

# Create a character from an uploaded video.

client.videos.createCharacter(VideoCreateCharacterParams { name, video } body, RequestOptionsoptions?): [VideoCreateCharacterResponse](/api/reference/typescript/resources/videos#(resource)%20videos%20%3E%20(model)%20video_create_character_response%20%3E%20(schema)) { id, created\_at, name }

POST/videos/characters

Create a character from an uploaded video.

##### ParametersExpand Collapse

body: VideoCreateCharacterParams { name, video }

name: string

Display name for this API character.

maxLength80

minLength1

video: [Uploadable](/api/reference/typescript/resources/videos/methods/create_character#(resource)%20videos%20%3E%20(method)%20create_character%20%3E%20(params)%20default%20%3E%20(param)%20video%20%3E%20(schema))

Video file used to create a character.

##### ReturnsExpand Collapse

VideoCreateCharacterResponse { id, created\_at, name }

id: string | null

Identifier for the character creation cameo.

created\_at: number

Unix timestamp (in seconds) when the character was created.

formatunixtime

name: string | null

Display name for the character.

### Create a character from an uploaded video.

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import fs from 'fs';
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted

const response = await client.videos.createCharacter({
  name: 'x',
  video: fs.createReadStream('path/to/file'),

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
