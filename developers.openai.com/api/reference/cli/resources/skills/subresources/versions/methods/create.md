<!-- source: https://developers.openai.com/api/reference/cli/resources/skills/subresources/versions/methods/create/ -->

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

# Create a new immutable skill version.

$ openai skills:versions create

POST/skills/{skill\_id}/versions

Create a new immutable skill version.

##### ParametersExpand Collapse

--skill-id: string

The identifier of the skill to version.

--default: optional boolean

Whether to set this version as the default.

--files: optional array of string or string

Skill files to upload (directory upload) or a single zip file.

##### ReturnsExpand Collapse

skill\_version: object { id, created\_at, description, 4 more }

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

### Create a new immutable skill version.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai skills:versions create \
  --api-key 'My API Key' \
  --skill-id skill_123

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
