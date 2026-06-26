<!-- source: https://developers.openai.com/api/reference/typescript/resources/skills/subresources/versions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Skills](/api/reference/typescript/resources/skills)

[Versions](/api/reference/typescript/resources/skills/subresources/versions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create a new immutable skill version.

client.skills.versions.create(stringskillID, VersionCreateParams { \_default, files } body?, RequestOptionsoptions?): [SkillVersion](/api/reference/typescript/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more }

POST/skills/{skill\_id}/versions

Create a new immutable skill version.

##### ParametersExpand Collapse

skillID: string

body: VersionCreateParams { \_default, files }

\_default?: boolean

Whether to set this version as the default.

files?: Array<Uploadable> | Uploadable

Skill files to upload (directory upload) or a single zip file.

One of the following:

Array<Uploadable>

Uploadable

##### ReturnsExpand Collapse

SkillVersion { id, created\_at, description, 4 more }

id: string

Unique identifier for the skill version.

created\_at: number

Unix timestamp (seconds) for when the version was created.

formatunixtime

description: string

Description of the skill version.

name: string

Name of the skill version.

object: "skill.version"

The object type, which is `skill.version`.

skill\_id: string

Identifier of the skill for this version.

version: string

Version number for this skill.

### Create a new immutable skill version.

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

const skillVersion = await client.skills.versions.create('skill_123');

console.log(skillVersion.id);

200 example

  "id": "id",
  "created_at": 0,
  "description": "description",
  "name": "name",
  "object": "skill.version",
  "skill_id": "skill_id",
  "version": "version"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "description": "description",
  "name": "name",
  "object": "skill.version",
  "skill_id": "skill_id",
  "version": "version"
