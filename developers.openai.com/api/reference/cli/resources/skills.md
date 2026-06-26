<!-- source: https://developers.openai.com/api/reference/cli/resources/skills/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Skills

##### [Create a new skill.](/api/reference/cli/resources/skills/methods/create)

$ openai skills create

POST/skills

##### [List all skills for the current project.](/api/reference/cli/resources/skills/methods/list)

$ openai skills list

GET/skills

##### [Get a skill by its ID.](/api/reference/cli/resources/skills/methods/retrieve)

$ openai skills retrieve

GET/skills/{skill\_id}

##### [Update the default version pointer for a skill.](/api/reference/cli/resources/skills/methods/update)

$ openai skills update

POST/skills/{skill\_id}

##### [Delete a skill by its ID.](/api/reference/cli/resources/skills/methods/delete)

$ openai skills delete

DELETE/skills/{skill\_id}

##### ModelsExpand Collapse

deleted\_skill: object { id, deleted, object }

id: string

deleted: boolean

object: "skill.deleted"

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

skill\_list: object { data, first\_id, has\_more, 2 more }

data: array of [Skill](/api/reference/cli/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

A list of items

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

first\_id: string

The ID of the first item in the list.

has\_more: boolean

Whether there are more items available.

last\_id: string

The ID of the last item in the list.

object: "list"

The type of object returned, must be `list`.

#### SkillsContent

##### [Download a skill zip bundle by its ID.](/api/reference/cli/resources/skills/subresources/content/methods/retrieve)

$ openai skills:content retrieve

GET/skills/{skill\_id}/content

#### SkillsVersions

##### [Create a new immutable skill version.](/api/reference/cli/resources/skills/subresources/versions/methods/create)

$ openai skills:versions create

POST/skills/{skill\_id}/versions

##### [List skill versions for a skill.](/api/reference/cli/resources/skills/subresources/versions/methods/list)

$ openai skills:versions list

GET/skills/{skill\_id}/versions

##### [Get a specific skill version.](/api/reference/cli/resources/skills/subresources/versions/methods/retrieve)

$ openai skills:versions retrieve

GET/skills/{skill\_id}/versions/{version}

##### [Delete a skill version.](/api/reference/cli/resources/skills/subresources/versions/methods/delete)

$ openai skills:versions delete

DELETE/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse

deleted\_skill\_version: object { id, deleted, object, version }

id: string

deleted: boolean

object: "skill.version.deleted"

version: string

The deleted skill version.

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

#### SkillsVersionsContent

##### [Download a skill version zip bundle.](/api/reference/cli/resources/skills/subresources/versions/subresources/content/methods/retrieve)

$ openai skills:versions:content retrieve

GET/skills/{skill\_id}/versions/{version}/content
