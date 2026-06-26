<!-- source: https://developers.openai.com/api/reference/typescript/resources/skills/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Skills

##### [Create a new skill.](/api/reference/typescript/resources/skills/methods/create)

client.skills.create(SkillCreateParams { files } body?, RequestOptionsoptions?): [Skill](/api/reference/typescript/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

POST/skills

##### [List all skills for the current project.](/api/reference/typescript/resources/skills/methods/list)

client.skills.list(SkillListParams { after, limit, order } query?, RequestOptionsoptions?): CursorPage<[Skill](/api/reference/typescript/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more } >

GET/skills

##### [Get a skill by its ID.](/api/reference/typescript/resources/skills/methods/retrieve)

client.skills.retrieve(stringskillID, RequestOptionsoptions?): [Skill](/api/reference/typescript/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

GET/skills/{skill\_id}

##### [Update the default version pointer for a skill.](/api/reference/typescript/resources/skills/methods/update)

client.skills.update(stringskillID, SkillUpdateParams { default\_version } body, RequestOptionsoptions?): [Skill](/api/reference/typescript/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

POST/skills/{skill\_id}

##### [Delete a skill by its ID.](/api/reference/typescript/resources/skills/methods/delete)

client.skills.delete(stringskillID, RequestOptionsoptions?): [DeletedSkill](/api/reference/typescript/resources/skills#(resource)%20skills%20%3E%20(model)%20deleted_skill%20%3E%20(schema)) { id, deleted, object }

DELETE/skills/{skill\_id}

##### ModelsExpand Collapse

DeletedSkill { id, deleted, object }

id: string

deleted: boolean

object: "skill.deleted"

Skill { id, created\_at, default\_version, 4 more }

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

SkillList { data, first\_id, has\_more, 2 more }

data: Array<[Skill](/api/reference/typescript/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more } >

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

first\_id: string | null

The ID of the first item in the list.

has\_more: boolean

Whether there are more items available.

last\_id: string | null

The ID of the last item in the list.

object: "list"

The type of object returned, must be `list`.

#### SkillsContent

##### [Download a skill zip bundle by its ID.](/api/reference/typescript/resources/skills/subresources/content/methods/retrieve)

client.skills.content.retrieve(stringskillID, RequestOptionsoptions?): Response

GET/skills/{skill\_id}/content

#### SkillsVersions

##### [Create a new immutable skill version.](/api/reference/typescript/resources/skills/subresources/versions/methods/create)

client.skills.versions.create(stringskillID, VersionCreateParams { \_default, files } body?, RequestOptionsoptions?): [SkillVersion](/api/reference/typescript/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more }

POST/skills/{skill\_id}/versions

##### [List skill versions for a skill.](/api/reference/typescript/resources/skills/subresources/versions/methods/list)

client.skills.versions.list(stringskillID, VersionListParams { after, limit, order } query?, RequestOptionsoptions?): CursorPage<[SkillVersion](/api/reference/typescript/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more } >

GET/skills/{skill\_id}/versions

##### [Get a specific skill version.](/api/reference/typescript/resources/skills/subresources/versions/methods/retrieve)

client.skills.versions.retrieve(stringversion, VersionRetrieveParams { skill\_id } params, RequestOptionsoptions?): [SkillVersion](/api/reference/typescript/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more }

GET/skills/{skill\_id}/versions/{version}

##### [Delete a skill version.](/api/reference/typescript/resources/skills/subresources/versions/methods/delete)

client.skills.versions.delete(stringversion, VersionDeleteParams { skill\_id } params, RequestOptionsoptions?): [DeletedSkillVersion](/api/reference/typescript/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20deleted_skill_version%20%3E%20(schema)) { id, deleted, object, version }

DELETE/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse

DeletedSkillVersion { id, deleted, object, version }

id: string

deleted: boolean

object: "skill.version.deleted"

version: string

The deleted skill version.

SkillVersion { id, created\_at, description, 4 more }

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

SkillVersionList { data, first\_id, has\_more, 2 more }

data: Array<[SkillVersion](/api/reference/typescript/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more } >

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

first\_id: string | null

The ID of the first item in the list.

has\_more: boolean

Whether there are more items available.

last\_id: string | null

The ID of the last item in the list.

object: "list"

The type of object returned, must be `list`.

#### SkillsVersionsContent

##### [Download a skill version zip bundle.](/api/reference/typescript/resources/skills/subresources/versions/subresources/content/methods/retrieve)

client.skills.versions.content.retrieve(stringversion, ContentRetrieveParams { skill\_id } params, RequestOptionsoptions?): Response

GET/skills/{skill\_id}/versions/{version}/content
