<!-- source: https://developers.openai.com/api/reference/cli/resources/skills/subresources/versions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Skills](/api/reference/cli/resources/skills)

[Versions](/api/reference/cli/resources/skills/subresources/versions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a skill version.

$ openai skills:versions delete

DELETE/skills/{skill\_id}/versions/{version}

Delete a skill version.

##### ParametersExpand Collapse

--skill-id: string

The identifier of the skill.

--version: string

The skill version number.

##### ReturnsExpand Collapse

deleted\_skill\_version: object { id, deleted, object, version }

id: string

deleted: boolean

object: "skill.version.deleted"

version: string

The deleted skill version.

### Delete a skill version.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai skills:versions delete \
  --api-key 'My API Key' \
  --skill-id skill_123 \
  --version version

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
