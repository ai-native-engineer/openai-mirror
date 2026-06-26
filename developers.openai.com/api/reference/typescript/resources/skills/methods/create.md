<!-- source: https://developers.openai.com/api/reference/typescript/resources/skills/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Skills](/api/reference/typescript/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create a new skill.

client.skills.create(SkillCreateParams { files } body?, RequestOptionsoptions?): [Skill](/api/reference/typescript/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

POST/skills

Create a new skill.

##### ParametersExpand Collapse

body: SkillCreateParams { files }

files?: Array<Uploadable> | Uploadable

Skill files to upload (directory upload) or a single zip file.

One of the following:

Array<Uploadable>

Uploadable

##### ReturnsExpand Collapse

Skill { id, created\_at, default\_version, 4 more }

id: string

Unique identifier for the skill.

created\_at: number

Unix timestamp (seconds) for when the skill was created.

formatunixtime

default\_version: string

Default version for the skill.

description: string

Description of the skill.

latest\_version: string

Latest version for the skill.

name: string

Name of the skill.

object: "skill"

The object type, which is `skill`.

### Create a new skill.

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

const skill = await client.skills.create();

console.log(skill.id);

200 example

  "id": "id",
  "created_at": 0,
  "default_version": "default_version",
  "description": "description",
  "latest_version": "latest_version",
  "name": "name",
  "object": "skill"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "default_version": "default_version",
  "description": "description",
  "latest_version": "latest_version",
  "name": "name",
  "object": "skill"
