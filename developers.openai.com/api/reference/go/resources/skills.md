<!-- source: https://developers.openai.com/api/reference/go/resources/skills/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Skills

##### [Create a new skill.](/api/reference/go/resources/skills/methods/create)

client.Skills.New(ctx, body) (\*[Skill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)), error)

POST/skills

##### [List all skills for the current project.](/api/reference/go/resources/skills/methods/list)

client.Skills.List(ctx, query) (\*CursorPage[[Skill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))], error)

GET/skills

##### [Get a skill by its ID.](/api/reference/go/resources/skills/methods/retrieve)

client.Skills.Get(ctx, skillID) (\*[Skill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)), error)

GET/skills/{skill\_id}

##### [Update the default version pointer for a skill.](/api/reference/go/resources/skills/methods/update)

client.Skills.Update(ctx, skillID, body) (\*[Skill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)), error)

POST/skills/{skill\_id}

##### [Delete a skill by its ID.](/api/reference/go/resources/skills/methods/delete)

client.Skills.Delete(ctx, skillID) (\*[DeletedSkill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20deleted_skill%20%3E%20(schema)), error)

DELETE/skills/{skill\_id}

##### ModelsExpand Collapse

type DeletedSkill struct{…}

ID string

Deleted bool

Object SkillDeleted

type Skill struct{…}

ID string

Unique identifier for the skill.

CreatedAt int64

Unix timestamp (seconds) for when the skill was created.

formatunixtime

DefaultVersion string

Default version for the skill.

Description string

Description of the skill.

LatestVersion string

Latest version for the skill.

Name string

Name of the skill.

Object Skill

The object type, which is `skill`.

type SkillList struct{…}

Data [][Skill](/api/reference/go/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))

A list of items

ID string

Unique identifier for the skill.

CreatedAt int64

Unix timestamp (seconds) for when the skill was created.

formatunixtime

DefaultVersion string

Default version for the skill.

Description string

Description of the skill.

LatestVersion string

Latest version for the skill.

Name string

Name of the skill.

Object Skill

The object type, which is `skill`.

FirstID string

The ID of the first item in the list.

HasMore bool

Whether there are more items available.

LastID string

The ID of the last item in the list.

Object List

The type of object returned, must be `list`.

#### SkillsContent

##### [Download a skill zip bundle by its ID.](/api/reference/go/resources/skills/subresources/content/methods/retrieve)

client.Skills.Content.Get(ctx, skillID) (\*Response, error)

GET/skills/{skill\_id}/content

#### SkillsVersions

##### [Create a new immutable skill version.](/api/reference/go/resources/skills/subresources/versions/methods/create)

client.Skills.Versions.New(ctx, skillID, body) (\*[SkillVersion](/api/reference/go/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)), error)

POST/skills/{skill\_id}/versions

##### [List skill versions for a skill.](/api/reference/go/resources/skills/subresources/versions/methods/list)

client.Skills.Versions.List(ctx, skillID, query) (\*CursorPage[[SkillVersion](/api/reference/go/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema))], error)

GET/skills/{skill\_id}/versions

##### [Get a specific skill version.](/api/reference/go/resources/skills/subresources/versions/methods/retrieve)

client.Skills.Versions.Get(ctx, skillID, version) (\*[SkillVersion](/api/reference/go/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)), error)

GET/skills/{skill\_id}/versions/{version}

##### [Delete a skill version.](/api/reference/go/resources/skills/subresources/versions/methods/delete)

client.Skills.Versions.Delete(ctx, skillID, version) (\*[DeletedSkillVersion](/api/reference/go/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20deleted_skill_version%20%3E%20(schema)), error)

DELETE/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse

type DeletedSkillVersion struct{…}

ID string

Deleted bool

Object SkillVersionDeleted

Version string

The deleted skill version.

type SkillVersion struct{…}

ID string

Unique identifier for the skill version.

CreatedAt int64

Unix timestamp (seconds) for when the version was created.

formatunixtime

Description string

Description of the skill version.

Name string

Name of the skill version.

Object SkillVersion

The object type, which is `skill.version`.

SkillID string

Identifier of the skill for this version.

Version string

Version number for this skill.

type SkillVersionList struct{…}

Data [][SkillVersion](/api/reference/go/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema))

A list of items

ID string

Unique identifier for the skill version.

CreatedAt int64

Unix timestamp (seconds) for when the version was created.

formatunixtime

Description string

Description of the skill version.

Name string

Name of the skill version.

Object SkillVersion

The object type, which is `skill.version`.

SkillID string

Identifier of the skill for this version.

Version string

Version number for this skill.

FirstID string

The ID of the first item in the list.

HasMore bool

Whether there are more items available.

LastID string

The ID of the last item in the list.

Object List

The type of object returned, must be `list`.

#### SkillsVersionsContent

##### [Download a skill version zip bundle.](/api/reference/go/resources/skills/subresources/versions/subresources/content/methods/retrieve)

client.Skills.Versions.Content.Get(ctx, skillID, version) (\*Response, error)

GET/skills/{skill\_id}/versions/{version}/content
