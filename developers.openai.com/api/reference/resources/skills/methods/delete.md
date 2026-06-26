<!-- source: https://developers.openai.com/api/reference/resources/skills/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Skills](/api/reference/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a skill by its ID.

DELETE/skills/{skill\_id}

Delete a skill by its ID.

##### Path ParametersExpand Collapse

skill\_id: string

##### ReturnsExpand Collapse

DeletedSkill object { id, deleted, object }

id: string

deleted: boolean

object: "skill.deleted"

### Delete a skill by its ID.

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/skills/$SKILL_ID \
    -X DELETE \
    -H "Authorization: Bearer $OPENAI_API_KEY"

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"

##### Returns Examples

200 example

  "id": "id",
  "deleted": true,
  "object": "skill.deleted"
