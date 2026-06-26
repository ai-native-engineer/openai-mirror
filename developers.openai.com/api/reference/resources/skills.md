<!-- source: https://developers.openai.com/api/reference/resources/skills/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Skills

##### [Create a new skill.](/api/reference/resources/skills/methods/create)

POST/skills

##### [List all skills for the current project.](/api/reference/resources/skills/methods/list)

GET/skills

##### [Get a skill by its ID.](/api/reference/resources/skills/methods/retrieve)

GET/skills/{skill\_id}

##### [Update the default version pointer for a skill.](/api/reference/resources/skills/methods/update)

POST/skills/{skill\_id}

##### [Delete a skill by its ID.](/api/reference/resources/skills/methods/delete)

DELETE/skills/{skill\_id}

##### ModelsExpand Collapse

DeletedSkill object { id, deleted, object }

id: string

deleted: boolean

object: "skill.deleted"

Skill object { id, created\_at, default\_version, 4 more }

id: string

Unique identifier for the skill.

created\_at: number

Unix timestamp (seconds) for when the skill was created.

formatunixtime

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

SkillList object { data, first\_id, has\_more, 2 more }

data: array of [Skill](/api/reference/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

A list of items

id: string

Unique identifier for the skill.

created\_at: number

Unix timestamp (seconds) for when the skill was created.

formatunixtime

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

##### [Download a skill zip bundle by its ID.](/api/reference/resources/skills/subresources/content/methods/retrieve)

GET/skills/{skill\_id}/content

#### SkillsVersions

##### [Create a new immutable skill version.](/api/reference/resources/skills/subresources/versions/methods/create)

POST/skills/{skill\_id}/versions

##### [List skill versions for a skill.](/api/reference/resources/skills/subresources/versions/methods/list)

GET/skills/{skill\_id}/versions

##### [Get a specific skill version.](/api/reference/resources/skills/subresources/versions/methods/retrieve)

GET/skills/{skill\_id}/versions/{version}

##### [Delete a skill version.](/api/reference/resources/skills/subresources/versions/methods/delete)

DELETE/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse

DeletedSkillVersion object { id, deleted, object, version }

id: string

deleted: boolean

object: "skill.version.deleted"

version: string

The deleted skill version.

SkillVersion object { id, created\_at, description, 4 more }

id: string

Unique identifier for the skill version.

created\_at: number

Unix timestamp (seconds) for when the version was created.

formatunixtime

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

SkillVersionList object { data, first\_id, has\_more, 2 more }

data: array of [SkillVersion](/api/reference/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more }

A list of items

id: string

Unique identifier for the skill version.

created\_at: number

Unix timestamp (seconds) for when the version was created.

formatunixtime

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

##### [Download a skill version zip bundle.](/api/reference/resources/skills/subresources/versions/subresources/content/methods/retrieve)

GET/skills/{skill\_id}/versions/{version}/content
