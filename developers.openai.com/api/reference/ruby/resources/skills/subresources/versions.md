<!-- source: https://developers.openai.com/api/reference/ruby/resources/skills/subresources/versions/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Skills](/api/reference/ruby/resources/skills)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Versions

##### [Create a new immutable skill version.](/api/reference/ruby/resources/skills/subresources/versions/methods/create)

skills.versions.create(skill\_id, \*\*kwargs) -> [SkillVersion](/api/reference/ruby/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more }

POST/skills/{skill\_id}/versions

##### [List skill versions for a skill.](/api/reference/ruby/resources/skills/subresources/versions/methods/list)

skills.versions.list(skill\_id, \*\*kwargs) -> CursorPage<[SkillVersion](/api/reference/ruby/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more } >

GET/skills/{skill\_id}/versions

##### [Get a specific skill version.](/api/reference/ruby/resources/skills/subresources/versions/methods/retrieve)

skills.versions.retrieve(version, \*\*kwargs) -> [SkillVersion](/api/reference/ruby/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more }

GET/skills/{skill\_id}/versions/{version}

##### [Delete a skill version.](/api/reference/ruby/resources/skills/subresources/versions/methods/delete)

skills.versions.delete(version, \*\*kwargs) -> [DeletedSkillVersion](/api/reference/ruby/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20deleted_skill_version%20%3E%20(schema)) { id, deleted, object, version }

DELETE/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse

class DeletedSkillVersion { id, deleted, object, version }

id: String

deleted: bool

object: :"skill.version.deleted"

version: String

The deleted skill version.

class SkillVersion { id, created\_at, description, 4 more }

id: String

Unique identifier for the skill version.

created\_at: Integer

Unix timestamp (seconds) for when the version was created.

formatunixtime

description: String

Description of the skill version.

name: String

Name of the skill version.

object: :"skill.version"

The object type, which is `skill.version`.

skill\_id: String

Identifier of the skill for this version.

version: String

Version number for this skill.

class SkillVersionList { data, first\_id, has\_more, 2 more }

data: Array[[SkillVersion](/api/reference/ruby/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) { id, created\_at, description, 4 more } ]

A list of items

id: String

Unique identifier for the skill version.

created\_at: Integer

Unix timestamp (seconds) for when the version was created.

formatunixtime

description: String

Description of the skill version.

name: String

Name of the skill version.

object: :"skill.version"

The object type, which is `skill.version`.

skill\_id: String

Identifier of the skill for this version.

version: String

Version number for this skill.

first\_id: String

The ID of the first item in the list.

has\_more: bool

Whether there are more items available.

last\_id: String

The ID of the last item in the list.

object: :list

The type of object returned, must be `list`.

#### VersionsContent

##### [Download a skill version zip bundle.](/api/reference/ruby/resources/skills/subresources/versions/subresources/content/methods/retrieve)

skills.versions.content.retrieve(version, \*\*kwargs) -> StringIO

GET/skills/{skill\_id}/versions/{version}/content
