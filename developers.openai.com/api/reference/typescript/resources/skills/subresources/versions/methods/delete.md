<!-- source: https://developers.openai.com/api/reference/typescript/resources/skills/subresources/versions/methods/delete/ -->

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

# Delete a skill version.

client.skills.versions.delete(stringversion, VersionDeleteParams { skill\_id } params, RequestOptionsoptions?): [DeletedSkillVersion](/api/reference/typescript/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20deleted_skill_version%20%3E%20(schema)) { id, deleted, object, version }

DELETE/skills/{skill\_id}/versions/{version}

Delete a skill version.

##### ParametersExpand Collapse

version: string

The skill version number.

params: VersionDeleteParams { skill\_id }

skill\_id: string

The identifier of the skill.

##### ReturnsExpand Collapse

DeletedSkillVersion { id, deleted, object, version }

id: string

deleted: boolean

object: "skill.version.deleted"

version: string

The deleted skill version.

### Delete a skill version.

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

const deletedSkillVersion = await client.skills.versions.delete('version', {
  skill_id: 'skill_123',

console.log(deletedSkillVersion.id);

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.version.deleted",
  "version": "version"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.version.deleted",
  "version": "version"
