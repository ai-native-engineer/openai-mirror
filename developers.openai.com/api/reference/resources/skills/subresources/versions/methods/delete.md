<!-- source: https://developers.openai.com/api/reference/resources/skills/subresources/versions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Skills](/api/reference/resources/skills)

[Versions](/api/reference/resources/skills/subresources/versions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a skill version.

DELETE/skills/{skill\_id}/versions/{version}

Delete a skill version.

##### Path ParametersExpand Collapse

skill\_id: string

version: string

The skill version number.

##### ReturnsExpand Collapse

DeletedSkillVersion object { id, deleted, object, version }

id: string

deleted: boolean

object: "skill.version.deleted"

version: string

The deleted skill version.

### Delete a skill version.

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/skills/$SKILL_ID/versions/$VERSION \
    -X DELETE \
    -H "Authorization: Bearer $OPENAI_API_KEY"

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
