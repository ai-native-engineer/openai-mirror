<!-- source: https://developers.openai.com/api/reference/typescript/resources/skills/methods/delete/ -->

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

# Delete a skill by its ID.

client.skills.delete(stringskillID, RequestOptionsoptions?): [DeletedSkill](/api/reference/typescript/resources/skills#(resource)%20skills%20%3E%20(model)%20deleted_skill%20%3E%20(schema)) { id, deleted, object }

DELETE/skills/{skill\_id}

Delete a skill by its ID.

##### ParametersExpand Collapse

skillID: string

##### ReturnsExpand Collapse

DeletedSkill { id, deleted, object }

id: string

deleted: boolean

object: "skill.deleted"

### Delete a skill by its ID.

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

const deletedSkill = await client.skills.delete('skill_123');

console.log(deletedSkill.id);

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"
