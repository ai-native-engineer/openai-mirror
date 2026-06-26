<!-- source: https://developers.openai.com/api/reference/java/resources/skills/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Skills

##### [Create a new skill.](/api/reference/java/resources/skills/methods/create)

[Skill](/api/reference/java/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) skills().create(SkillCreateParamsparams = SkillCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/skills

##### [List all skills for the current project.](/api/reference/java/resources/skills/methods/list)

SkillListPage skills().list(SkillListParamsparams = SkillListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/skills

##### [Get a skill by its ID.](/api/reference/java/resources/skills/methods/retrieve)

[Skill](/api/reference/java/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) skills().retrieve(SkillRetrieveParamsparams = SkillRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/skills/{skill\_id}

##### [Update the default version pointer for a skill.](/api/reference/java/resources/skills/methods/update)

[Skill](/api/reference/java/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema)) skills().update(SkillUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/skills/{skill\_id}

##### [Delete a skill by its ID.](/api/reference/java/resources/skills/methods/delete)

[DeletedSkill](/api/reference/java/resources/skills#(resource)%20skills%20%3E%20(model)%20deleted_skill%20%3E%20(schema)) skills().delete(SkillDeleteParamsparams = SkillDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/skills/{skill\_id}

##### ModelsExpand Collapse

class DeletedSkill:

String id

boolean deleted

JsonValue; object\_ "skill.deleted"constant"skill.deleted"constant

class Skill:

String id

Unique identifier for the skill.

long createdAt

Unix timestamp (seconds) for when the skill was created.

formatunixtime

String defaultVersion

Default version for the skill.

String description

Description of the skill.

String latestVersion

Latest version for the skill.

String name

Name of the skill.

JsonValue; object\_ "skill"constant"skill"constant

The object type, which is `skill`.

class SkillList:

List<[Skill](/api/reference/java/resources/skills#(resource)%20skills%20%3E%20(model)%20skill%20%3E%20(schema))> data

A list of items

String id

Unique identifier for the skill.

long createdAt

Unix timestamp (seconds) for when the skill was created.

formatunixtime

String defaultVersion

Default version for the skill.

String description

Description of the skill.

String latestVersion

Latest version for the skill.

String name

Name of the skill.

JsonValue; object\_ "skill"constant"skill"constant

The object type, which is `skill`.

Optional<String> firstId

The ID of the first item in the list.

boolean hasMore

Whether there are more items available.

Optional<String> lastId

The ID of the last item in the list.

JsonValue; object\_ "list"constant"list"constant

The type of object returned, must be `list`.

#### SkillsContent

##### [Download a skill zip bundle by its ID.](/api/reference/java/resources/skills/subresources/content/methods/retrieve)

HttpResponse skills().content().retrieve(ContentRetrieveParamsparams = ContentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/skills/{skill\_id}/content

#### SkillsVersions

##### [Create a new immutable skill version.](/api/reference/java/resources/skills/subresources/versions/methods/create)

[SkillVersion](/api/reference/java/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) skills().versions().create(VersionCreateParamsparams = VersionCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/skills/{skill\_id}/versions

##### [List skill versions for a skill.](/api/reference/java/resources/skills/subresources/versions/methods/list)

VersionListPage skills().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/skills/{skill\_id}/versions

##### [Get a specific skill version.](/api/reference/java/resources/skills/subresources/versions/methods/retrieve)

[SkillVersion](/api/reference/java/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema)) skills().versions().retrieve(VersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/skills/{skill\_id}/versions/{version}

##### [Delete a skill version.](/api/reference/java/resources/skills/subresources/versions/methods/delete)

[DeletedSkillVersion](/api/reference/java/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20deleted_skill_version%20%3E%20(schema)) skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse

class DeletedSkillVersion:

String id

boolean deleted

JsonValue; object\_ "skill.version.deleted"constant"skill.version.deleted"constant

String version

The deleted skill version.

class SkillVersion:

String id

Unique identifier for the skill version.

long createdAt

Unix timestamp (seconds) for when the version was created.

formatunixtime

String description

Description of the skill version.

String name

Name of the skill version.

JsonValue; object\_ "skill.version"constant"skill.version"constant

The object type, which is `skill.version`.

String skillId

Identifier of the skill for this version.

String version

Version number for this skill.

class SkillVersionList:

List<[SkillVersion](/api/reference/java/resources/skills#(resource)%20skills.versions%20%3E%20(model)%20skill_version%20%3E%20(schema))> data

A list of items

String id

Unique identifier for the skill version.

long createdAt

Unix timestamp (seconds) for when the version was created.

formatunixtime

String description

Description of the skill version.

String name

Name of the skill version.

JsonValue; object\_ "skill.version"constant"skill.version"constant

The object type, which is `skill.version`.

String skillId

Identifier of the skill for this version.

String version

Version number for this skill.

Optional<String> firstId

The ID of the first item in the list.

boolean hasMore

Whether there are more items available.

Optional<String> lastId

The ID of the last item in the list.

JsonValue; object\_ "list"constant"list"constant

The type of object returned, must be `list`.

#### SkillsVersionsContent

##### [Download a skill version zip bundle.](/api/reference/java/resources/skills/subresources/versions/subresources/content/methods/retrieve)

HttpResponse skills().versions().content().retrieve(ContentRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/skills/{skill\_id}/versions/{version}/content
