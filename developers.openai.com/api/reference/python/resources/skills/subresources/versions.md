<!-- source: https://developers.openai.com/api/reference/python/resources/skills/subresources/versions/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Skills](/api/reference/python/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Versions

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

#### VersionsContent

##### [Download a skill version zip bundle.](/api/reference/python/resources/skills/subresources/versions/subresources/content/methods/retrieve)

skills.versions.content.retrieve(strversion, ContentRetrieveParams\*\*kwargs)  -> BinaryResponseContent

GET/skills/{skill\_id}/versions/{version}/content
