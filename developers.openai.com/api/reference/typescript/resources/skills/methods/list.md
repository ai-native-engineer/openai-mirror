<!-- source: https://developers.openai.com/api/reference/typescript/resources/skills/methods/list/ -->

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

# List all skills for the current project.

client.skills.list(SkillListParams { after, limit, order } query?, RequestOptionsoptions?): CursorPage<[Skill](/api/reference/typescript/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more } >

GET/skills

List all skills for the current project.

##### ParametersExpand Collapse

query: SkillListParams { after, limit, order }

after?: string

Identifier for the last item from the previous pagination request

limit?: number

Number of items to retrieve

minimum0

maximum100

order?: "asc" | "desc"

Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

One of the following:

"asc"

"desc"

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

### List all skills for the current project.

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

// Automatically fetches more pages as needed.
for await (const skill of client.skills.list()) {
  console.log(skill.id);

200 example

  "data": [
      "id": "id",
      "created_at": 0,
      "default_version": "default_version",
      "description": "description",
      "latest_version": "latest_version",
      "name": "name",
      "object": "skill"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

##### Returns Examples

200 example

  "data": [
      "id": "id",
      "created_at": 0,
      "default_version": "default_version",
      "description": "description",
      "latest_version": "latest_version",
      "name": "name",
      "object": "skill"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
