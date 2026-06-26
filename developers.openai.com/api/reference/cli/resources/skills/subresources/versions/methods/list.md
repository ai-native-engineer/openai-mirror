<!-- source: https://developers.openai.com/api/reference/cli/resources/skills/subresources/versions/methods/list/ -->

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

# List skill versions for a skill.

$ openai skills:versions list

GET/skills/{skill\_id}/versions

List skill versions for a skill.

##### ParametersExpand Collapse

--skill-id: string

The identifier of the skill.

--after: optional string

The skill version ID to start after.

--limit: optional number

Number of versions to retrieve.

--order: optional "asc" or "desc"

Sort order of results by version number.

##### ReturnsExpand Collapse

skill\_version\_list: object { data, first\_id, has\_more, 2 more }

data: array of [SkillVersion](/api/reference/cli/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more }

A list of items

id: string

Unique identifier for the skill version.

created\_at: number

Unix timestamp (seconds) for when the version was created.

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

first\_id: string

The ID of the first item in the list.

has\_more: boolean

Whether there are more items available.

last\_id: string

The ID of the last item in the list.

object: "list"

The type of object returned, must be `list`.

### List skill versions for a skill.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai skills:versions list \
  --api-key 'My API Key' \
  --skill-id skill_123

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
