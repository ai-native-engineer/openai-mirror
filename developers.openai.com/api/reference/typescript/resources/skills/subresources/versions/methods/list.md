<!-- source: https://developers.openai.com/api/reference/typescript/resources/skills/subresources/versions/methods/list/ -->

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

# List skill versions for a skill.

client.skills.versions.list(stringskillID, VersionListParams { after, limit, order } query?, RequestOptionsoptions?): CursorPage<[SkillVersion](/api/reference/typescript/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more } >

GET/skills/{skill\_id}/versions

List skill versions for a skill.

##### ParametersExpand Collapse

skillID: string

query: VersionListParams { after, limit, order }

after?: string

The skill version ID to start after.

limit?: number

Number of versions to retrieve.

minimum0

maximum100

order?: "asc" | "desc"

Sort order of results by version number.

One of the following:

"asc"

"desc"

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

### List skill versions for a skill.

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
for await (const skillVersion of client.skills.versions.list('skill_123')) {
  console.log(skillVersion.id);

200 example

  "data": [
      "id": "id",
      "created_at": 0,
      "description": "description",
      "name": "name",
      "object": "skill.version",
      "skill_id": "skill_id",
      "version": "version"
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
      "description": "description",
      "name": "name",
      "object": "skill.version",
      "skill_id": "skill_id",
      "version": "version"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
