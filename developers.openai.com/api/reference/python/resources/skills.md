<!-- source: https://developers.openai.com/api/reference/python/resources/skills/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Skills

##### [Create a new skill.](/api/reference/python/resources/skills/methods/create)

skills.create(SkillCreateParams\*\*kwargs)  -> [Skill](/api/reference/python/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))

POST/skills

##### [List all skills for the current project.](/api/reference/python/resources/skills/methods/list)

skills.list(SkillListParams\*\*kwargs)  -> SyncCursorPage[[Skill](/api/reference/python/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))]

GET/skills

##### [Get a skill by its ID.](/api/reference/python/resources/skills/methods/retrieve)

skills.retrieve(strskill\_id)  -> [Skill](/api/reference/python/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))

GET/skills/{skill\_id}

##### [Update the default version pointer for a skill.](/api/reference/python/resources/skills/methods/update)

skills.update(strskill\_id, SkillUpdateParams\*\*kwargs)  -> [Skill](/api/reference/python/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))

POST/skills/{skill\_id}

##### [Delete a skill by its ID.](/api/reference/python/resources/skills/methods/delete)

skills.delete(strskill\_id)  -> [DeletedSkill](/api/reference/python/resources/skills#(resource)%20skills%20%3E%20(model)%20deleted_skill%20%3E%20(schema))

DELETE/skills/{skill\_id}

##### ModelsExpand Collapse

class DeletedSkill: …

id: str

deleted: bool

object: Literal["skill.deleted"]

class Skill: …

id: str

Unique identifier for the skill.

created\_at: int

Unix timestamp (seconds) for when the skill was created.

formatunixtime

default\_version: str

Default version for the skill.

description: str

Description of the skill.

latest\_version: str

Latest version for the skill.

name: str

Name of the skill.

object: Literal["skill"]

The object type, which is `skill`.

class SkillList: …

data: List[[Skill](/api/reference/python/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))]

A list of items

id: str

Unique identifier for the skill.

created\_at: int

Unix timestamp (seconds) for when the skill was created.

formatunixtime

default\_version: str

Default version for the skill.

description: str

Description of the skill.

latest\_version: str

Latest version for the skill.

name: str

Name of the skill.

object: Literal["skill"]

The object type, which is `skill`.

first\_id: Optional[str]

The ID of the first item in the list.

has\_more: bool

Whether there are more items available.

last\_id: Optional[str]

The ID of the last item in the list.

object: Literal["list"]

The type of object returned, must be `list`.

#### SkillsContent

##### [Download a skill zip bundle by its ID.](/api/reference/python/resources/skills/subresources/content/methods/retrieve)

skills.content.retrieve(strskill\_id)  -> BinaryResponseContent

GET/skills/{skill\_id}/content

#### SkillsVersions

##### [Create a new immutable skill version.](/api/reference/python/resources/skills/subresources/versions/methods/create)

skills.versions.create(strskill\_id, VersionCreateParams\*\*kwargs)  -> [SkillVersion](/api/reference/python/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema))

POST/skills/{skill\_id}/versions

##### [List skill versions for a skill.](/api/reference/python/resources/skills/subresources/versions/methods/list)

skills.versions.list(strskill\_id, VersionListParams\*\*kwargs)  -> SyncCursorPage[[SkillVersion](/api/reference/python/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema))]

GET/skills/{skill\_id}/versions

##### [Get a specific skill version.](/api/reference/python/resources/skills/subresources/versions/methods/retrieve)

skills.versions.retrieve(strversion, VersionRetrieveParams\*\*kwargs)  -> [SkillVersion](/api/reference/python/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema))

GET/skills/{skill\_id}/versions/{version}

##### [Delete a skill version.](/api/reference/python/resources/skills/subresources/versions/methods/delete)

skills.versions.delete(strversion, VersionDeleteParams\*\*kwargs)  -> [DeletedSkillVersion](/api/reference/python/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20deleted_skill_version%20%3E%20(schema))

DELETE/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse

class DeletedSkillVersion: …

id: str

deleted: bool

object: Literal["skill.version.deleted"]

version: str

The deleted skill version.

class SkillVersion: …

id: str

Unique identifier for the skill version.

created\_at: int

Unix timestamp (seconds) for when the version was created.

formatunixtime

description: str

Description of the skill version.

name: str

Name of the skill version.

object: Literal["skill.version"]

The object type, which is `skill.version`.

skill\_id: str

Identifier of the skill for this version.

version: str

Version number for this skill.

class SkillVersionList: …

data: List[[SkillVersion](/api/reference/python/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema))]

A list of items

id: str

Unique identifier for the skill version.

created\_at: int

Unix timestamp (seconds) for when the version was created.

formatunixtime

description: str

Description of the skill version.

name: str

Name of the skill version.

object: Literal["skill.version"]

The object type, which is `skill.version`.

skill\_id: str

Identifier of the skill for this version.

version: str

Version number for this skill.

first\_id: Optional[str]

The ID of the first item in the list.

has\_more: bool

Whether there are more items available.

last\_id: Optional[str]

The ID of the last item in the list.

object: Literal["list"]

The type of object returned, must be `list`.

#### SkillsVersionsContent

##### [Download a skill version zip bundle.](/api/reference/python/resources/skills/subresources/versions/subresources/content/methods/retrieve)

skills.versions.content.retrieve(strversion, ContentRetrieveParams\*\*kwargs)  -> BinaryResponseContent

GET/skills/{skill\_id}/versions/{version}/content
