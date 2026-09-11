<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/list/ -->

[Environments](/api/reference/resources/beta/subresources/agents/subresources/environments)

[Templates](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates)

# List agent environment templates

GET/agents/environments/templates

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

##### Query ParametersExpand Collapse

after: optional string

Return resources after this resource ID in the selected order.

limit: optional number

The maximum number of resources to return, between 1 and 100. Defaults to 20.

minimum1

maximum100

order: optional "asc" or "desc"

The order in which resources are returned. Defaults to `desc`.

"asc"

Returns resources in ascending order.

"desc"

Returns resources in descending order.

data: array of [EnvironmentTemplate](/api/reference/resources/beta#(resource)%20beta.agents.environments.templates%20%3E%20(model)%20environment_template%20%3E%20(schema)) { id, capability\_directories, created\_at, 8 more }

The resources returned in this page, in the requested sort order.

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

first\_id: string or null

The ID of the first resource in `data`, or `null` if the page is empty.

has\_more: boolean

Whether there are more resources to retrieve after this page.

last\_id: string or null

The ID of the last resource in `data`, or `null` if the page is empty. Pass this as `after` with the same order and filters.

object: "list"

The object type, which is always `list`.

### List agent environment templates

curl https://api.openai.com/v1/agents/environments/templates \

  "data": [
      "capability_directories": [
        "string"
      ],
      "created_at": 0,
      "files": [
          "file_id": "file_id",
          "path": "path",
          "type": "file_id"
      ],
      "name": "name",
      "network": {
        "access": "enabled",
        "allowed_domains": [
          "string"
        ]
      },
      "object": "agent.environment.template",
      "packages": {
        "npm": [
          "string"
        ],
        "python": [
          "string"
        ],
        "system": [
          "string"
        ]
      },
      "plugins": [
          "description": "description",
          "name": "name",
          "type": "inline"
      ],
      "skills": [
          "skill_id": "skill_id",
          "type": "skill_reference",
          "version": "version"
      ],
      "updated_at": 0
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

  "data": [
      "capability_directories": [
        "string"
      ],
      "created_at": 0,
      "files": [
          "file_id": "file_id",
          "path": "path",
          "type": "file_id"
      ],
      "name": "name",
      "network": {
        "access": "enabled",
        "allowed_domains": [
          "string"
        ]
      },
      "object": "agent.environment.template",
      "packages": {
        "npm": [
          "string"
        ],
        "python": [
          "string"
        ],
        "system": [
          "string"
        ]
      },
      "plugins": [
          "description": "description",
          "name": "name",
          "type": "inline"
      ],
      "skills": [
          "skill_id": "skill_id",
          "type": "skill_reference",
          "version": "version"
      ],
      "updated_at": 0
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
