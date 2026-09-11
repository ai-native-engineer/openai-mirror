<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/environments/ -->

# Environments

##### [Retrieve an agent environment](/api/reference/resources/beta/subresources/agents/subresources/environments/methods/retrieve)

GET/agents/environments/{environment\_id}

##### ModelsExpand Collapse

EnvironmentInfo object { id, files, object, 4 more }

Safe metadata for a first-class execution environment.

The ID of the environment.

files: array of [HostedEnvironmentFile](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_environment_file%20%3E%20(schema))

Files installed in the environment, without their contents.

HostedEnvironmentFileID object { id, file\_id, path, 2 more }

A file copied from the OpenAI Files API.

The session-scoped ID of the file in the execution environment.

file\_id: string

The ID of the uploaded file.

path: string

The file’s absolute path inside the environment.

size\_bytes: number

The decoded file size in bytes.

minimum0

type: "file\_id"

The type of the object. Always `file_id`.

Inline object { id, path, size\_bytes, type }

A file supplied inline when the session was created.

The session-scoped ID of the file in the execution environment.

path: string

The file’s absolute path inside the environment.

size\_bytes: number

The decoded file size in bytes.

minimum0

type: "inline"

The type of the object. Always `inline`.

object: "agent.environment"

The object type. Always `agent.environment`.

plugins: array of [HostedPlugin](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_plugin%20%3E%20(schema)) { description, name, type }

Plugins installed in the environment, without their archive contents.

description: string

The installed plugin description.

The installed plugin name.

type: "inline"

The type of the object. Always `inline`.

skills: array of [HostedSkill](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_skill%20%3E%20(schema))

Skills installed in the environment, without their archive contents.

HostedSkillReference object { description, name, skill\_id, 2 more }

A skill installed from the Skills API.

description: string

The installed skill description.

The installed skill name.

skill\_id: string

The referenced skill ID.

type: "skill\_reference"

The type of the object. Always `skill_reference`.

version: string

The concrete skill version installed for this session.

Inline object { description, name, type }

A skill installed from an inline ZIP archive.

description: string

The installed skill description.

The installed skill name.

type: "inline"

The type of the object. Always `inline`.

status: "pending" or "connected" or "disconnected" or 2 more

The current environment connection status.

"pending"

"connected"

"disconnected"

"expired"

"failed"

type: "openai\_hosted" or "self\_hosted"

Whether the environment is hosted by OpenAI or by the application.

"openai\_hosted"

"self\_hosted"

#### EnvironmentsFiles

##### [Create an agent environment file](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/create)

POST/agents/environments/{environment\_id}/files

##### [List agent environment files](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/list)

GET/agents/environments/{environment\_id}/files

##### ModelsExpand Collapse

EnvironmentFile object { environment\_id, object, path, size\_bytes }

A live file in an execution environment.

environment\_id: string

The ID of the environment containing this file.

object: "agent.environment.file"

The object type. Always `agent.environment.file`.

path: string

The absolute file path inside the environment’s workspace.

size\_bytes: number

The file size in bytes.

minimum0

#### EnvironmentsTemplates

##### [Create an agent environment template](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/create)

POST/agents/environments/templates

##### [Delete an agent environment template](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/delete)

DELETE/agents/environments/templates/{environment\_template\_id}

##### [List agent environment templates](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/list)

GET/agents/environments/templates

##### [Retrieve an agent environment template](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/retrieve)

GET/agents/environments/templates/{environment\_template\_id}

##### [Update an agent environment template](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/update)

POST/agents/environments/templates/{environment\_template\_id}

##### ModelsExpand Collapse

EnvironmentTemplate object { id, capability\_directories, created\_at, 8 more }

Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

The ID of the reusable environment template.

capability\_directories: array of string

Directories that expose capabilities to the agent.

The Unix timestamp, in seconds, when the template was created.

files: array of object { file\_id, path, type }  or object { path, size\_bytes, type }

Safe file metadata, excluding contents and session-scoped file IDs.

FileID object { file\_id, path, type }

A project-scoped Files API reference resolved separately for each session.

file\_id: string

The ID of the uploaded file.

path: string

The file’s absolute path inside the environment.

type: "file\_id"

The type of the object. Always `file_id`.

Inline object { path, size\_bytes, type }

Metadata for confidential inline file contents.

path: string

The file’s absolute path inside the environment.

size\_bytes: number

The decoded size of the inline file in bytes.

minimum0

type: "inline"

The type of the object. Always `inline`.

name: string or null

An optional human-readable display name for the template.

network: object { access, allowed\_domains }

Runtime network access for each OpenAI-hosted environment.

access: "enabled" or "disabled" or "restricted"

The environment’s network access mode.

"enabled"

Allows unrestricted network access.

"disabled"

Disables network access.

"restricted"

Allows access only to configured domains.

allowed\_domains: array of string

Domains the environment may access when network access is restricted.

object: "agent.environment.template"

The object type. Always `agent.environment.template`.

packages: object { npm, python, system }

Packages installed in each fresh OpenAI-hosted environment.

npm: array of string

npm packages installed globally in the environment.

python: array of string

Python packages installed in the environment.

system: array of string

System packages installed in the environment.

plugins: array of [HostedPlugin](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_plugin%20%3E%20(schema)) { description, name, type }

Safe plugin metadata, excluding inline archive contents.

description: string

The installed plugin description.

The installed plugin name.

type: "inline"

The type of the object. Always `inline`.

skills: array of object { skill\_id, type, version }  or object { description, name, type }

Safe skill metadata, preserving unresolved version selectors.

SkillReference object { skill\_id, type, version }

A skill resolved afresh from the Skills API whenever a session starts.

skill\_id: string

The referenced skill ID.

type: "skill\_reference"

The type of the object. Always `skill_reference`.

version: string or null

The requested version selector, including `latest`.

Inline object { description, name, type }

Safe metadata for an inline skill archive.

description: string

The skill description declared in `SKILL.md`.

The skill name declared in `SKILL.md`.

type: "inline"

The type of the object. Always `inline`.

updated\_at: number

The Unix timestamp, in seconds, when the template was last updated.

EnvironmentTemplateDeleted object { id, deleted, object }

A deleted reusable environment template.

The ID of the deleted environment template.

deleted: boolean

Whether the environment template was deleted. Always `true`.

object: "agent.environment.template.deleted"

The object type. Always `agent.environment.template.deleted`.
