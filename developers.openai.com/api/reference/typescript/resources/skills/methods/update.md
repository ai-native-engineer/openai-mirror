<!-- source: https://developers.openai.com/api/reference/typescript/resources/skills/methods/update/ -->

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

# Update the default version pointer for a skill.

client.skills.update(stringskillID, SkillUpdateParams { default\_version } body, RequestOptionsoptions?): [Skill](/api/reference/typescript/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

POST/skills/{skill\_id}

Update the default version pointer for a skill.

##### ParametersExpand Collapse

skillID: string

body: SkillUpdateParams { default\_version }

default\_version: string

The skill version number to set as default.

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

### Update the default version pointer for a skill.

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

const skill = await client.skills.update('skill_123', { default_version: 'default_version' });

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
