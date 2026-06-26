<!-- source: https://developers.openai.com/api/reference/cli/resources/skills/methods/retrieve/ -->

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

# Get a skill by its ID.

$ openai skills retrieve

GET/skills/{skill\_id}

Get a skill by its ID.

##### ParametersExpand Collapse

--skill-id: string

The identifier of the skill to retrieve.

##### ReturnsExpand Collapse

skill: object { id, created\_at, default\_version, 4 more }

id: string

Unique identifier for the skill.

created\_at: number

Unix timestamp (seconds) for when the skill was created.

default\_version: string

Default version for the skill.

description: string

Description of the skill.

latest\_version: string

Latest version for the skill.

name: string

Name of the skill.

object: "skill"

The object type, which is `skill`.

### Get a skill by its ID.

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai skills retrieve \
  --api-key 'My API Key' \
  --skill-id skill_123

200 example

  "id": "id",
  "created_at": 0,
  "default_version": "default_version",
  "description": "description",
  "latest_version": "latest_version",
  "name": "name",
  "object": "skill"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "default_version": "default_version",
  "description": "description",
  "latest_version": "latest_version",
  "name": "name",
  "object": "skill"
