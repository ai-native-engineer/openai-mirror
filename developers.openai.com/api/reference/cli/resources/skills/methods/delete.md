<!-- source: https://developers.openai.com/api/reference/cli/resources/skills/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Skills](/api/reference/cli/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a skill by its ID.

$ openai skills delete

DELETE/skills/{skill\_id}

Delete a skill by its ID.

##### ParametersExpand Collapse

--skill-id: string

The identifier of the skill to delete.

##### ReturnsExpand Collapse

deleted\_skill: object { id, deleted, object }

id: string

deleted: boolean

object: "skill.deleted"

### Delete a skill by its ID.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai skills delete \
  --api-key 'My API Key' \
  --skill-id skill_123

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"
