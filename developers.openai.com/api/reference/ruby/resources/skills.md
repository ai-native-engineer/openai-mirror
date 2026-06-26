<!-- source: https://developers.openai.com/api/reference/ruby/resources/skills/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Skills

##### [Create a new skill.](/api/reference/ruby/resources/skills/methods/create)

skills.create(\*\*kwargs) -> [Skill](/api/reference/ruby/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

POST/skills

##### [List all skills for the current project.](/api/reference/ruby/resources/skills/methods/list)

skills.list(\*\*kwargs) -> CursorPage<[Skill](/api/reference/ruby/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more } >

GET/skills

##### [Get a skill by its ID.](/api/reference/ruby/resources/skills/methods/retrieve)

skills.retrieve(skill\_id) -> [Skill](/api/reference/ruby/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

GET/skills/{skill\_id}

##### [Update the default version pointer for a skill.](/api/reference/ruby/resources/skills/methods/update)

skills.update(skill\_id, \*\*kwargs) -> [Skill](/api/reference/ruby/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more }

POST/skills/{skill\_id}

##### [Delete a skill by its ID.](/api/reference/ruby/resources/skills/methods/delete)

skills.delete(skill\_id) -> [DeletedSkill](/api/reference/ruby/resources/skills#(resource)%20skills%20%3E%20(model)%20deleted_skill%20%3E%20(schema)) { id, deleted, object }

DELETE/skills/{skill\_id}

##### ModelsExpand Collapse

class DeletedSkill { id, deleted, object }

id: String

deleted: bool

object: :"skill.deleted"

class Skill { id, created\_at, default\_version, 4 more }

id: String

Unique identifier for the skill.

created\_at: Integer

Unix timestamp (seconds) for when the skill was created.

formatunixtime

default\_version: String

Default version for the skill.

description: String

Description of the skill.

latest\_version: String

Latest version for the skill.

name: String

Name of the skill.

object: :skill

The object type, which is `skill`.

class SkillList { data, first\_id, has\_more, 2 more }

data: Array[[Skill](/api/reference/ruby/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) { id, created\_at, default\_version, 4 more } ]

A list of items

id: String

Unique identifier for the skill.

created\_at: Integer

Unix timestamp (seconds) for when the skill was created.

formatunixtime

default\_version: String

Default version for the skill.

description: String

Description of the skill.

latest\_version: String

Latest version for the skill.

name: String

Name of the skill.

object: :skill

The object type, which is `skill`.

first\_id: String

The ID of the first item in the list.

has\_more: bool

Whether there are more items available.

last\_id: String

The ID of the last item in the list.

object: :list

The type of object returned, must be `list`.

#### SkillsContent

##### [Download a skill zip bundle by its ID.](/api/reference/ruby/resources/skills/subresources/content/methods/retrieve)

skills.content.retrieve(skill\_id) -> StringIO

GET/skills/{skill\_id}/content

#### SkillsVersions

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

#### SkillsVersionsContent

##### [Download a skill version zip bundle.](/api/reference/ruby/resources/skills/subresources/versions/subresources/content/methods/retrieve)

skills.versions.content.retrieve(version, \*\*kwargs) -> StringIO

GET/skills/{skill\_id}/versions/{version}/content
