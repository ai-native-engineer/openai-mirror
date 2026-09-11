<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/create/ -->

[Environments](/api/reference/resources/beta/subresources/agents/subresources/environments)

[Templates](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/templates)

# Create an agent environment template

POST/agents/environments/templates

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

##### Body ParametersJSONExpand Collapse

capability\_directories: optional array of string or null

Directories that contain capabilities exposed to the agent. Defaults to an empty list.

env: optional map[string] or null

Environment variables made available to the agent.

files: optional array of [HostedEnvironmentFileParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_environment_file_param%20%3E%20(schema)) or null

Files available before the agent starts. Defaults to an empty list.

FileID object { file\_id, path, type }

A file previously uploaded through the OpenAI Files API.

file\_id: string

The ID of the uploaded file.

minLength1

maxLength256

path: string

The absolute destination path inside `/workspace`.

minLength1

maxLength4096

type: "file\_id"

The type of the object. Always `file_id`.

Inline object { data, path, type }

A file supplied directly as standard-base64 data.

data: string

The standard-base64-encoded file contents.

maxLength6990508

path: string

The absolute destination path inside `/workspace`.

minLength1

maxLength4096

type: "inline"

The type of the object. Always `inline`.

name: optional string or null

An optional human-readable display name for the template.

minLength1

maxLength256

network: optional object { access, allowed\_domains }  or null

Network access for an OpenAI-hosted environment.

access: "enabled" or "disabled" or "restricted"

The environment’s network access mode.

"enabled"

Allows unrestricted network access, matching an omitted network policy.

"disabled"

Disables network access.

"restricted"

Allows access only to configured domains.

allowed\_domains: optional array of string or null

Domains the environment may access when network access is restricted.

packages: optional object { npm, python, system }  or null

Packages to install in an OpenAI-hosted environment.

npm: optional array of string or null

npm packages to install globally. Defaults to an empty list.

python: optional array of string or null

Python packages to install. Defaults to an empty list.

system: optional array of string or null

System packages to install. Defaults to an empty list.

plugins: optional array of [HostedPluginParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_plugin_param%20%3E%20(schema)) { description, name, source, type }  or null

Plugins provided as inline ZIP archives. Defaults to an empty list.

description: string

The plugin description declared in `.codex-plugin/plugin.json`.

The plugin name declared in `.codex-plugin/plugin.json`.

minLength1

maxLength64

source: [InlineCapabilitySourceParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20inline_capability_source_param%20%3E%20(schema)) { data, media\_type, type }

Provides ZIP bytes encoded with standard base64.

data: string

Standard-base64 encoded ZIP archive bytes.

minLength1

maxLength70254592

media\_type: "application/zip"

The archive media type, always `application/zip`.

type: "base64"

The type of the object. Always `base64`.

type: "inline"

The type of the object. Always `inline`.

setup\_commands: optional array of [SetupCommandParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20setup_command_param%20%3E%20(schema)) { command, cwd }  or null

Ordered, confidential setup commands. Command bodies are never returned.

command: string

The shell command to execute.

maxLength65536

cwd: optional string or null

The absolute working directory. Defaults to `/workspace`.

maxLength4096

skills: optional array of [HostedSkillParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_skill_param%20%3E%20(schema)) or null

Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

SkillReference object { skill\_id, type, version }

References a skill uploaded through the Skills API.

skill\_id: string

The ID of the skill created through `/v1/skills`.

minLength1

maxLength64

type: "skill\_reference"

The type of the object. Always `skill_reference`.

version: optional string or null

The skill version, a positive integer or `latest`; omission selects the default.

Inline object { description, name, source, type }

Supplies a skill ZIP directly in the session request.

description: string

The skill description declared in `SKILL.md`.

The skill name declared in `SKILL.md`.

minLength1

maxLength64

source: [InlineCapabilitySourceParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20inline_capability_source_param%20%3E%20(schema)) { data, media\_type, type }

Provides ZIP bytes encoded with standard base64.

data: string

Standard-base64 encoded ZIP archive bytes.

minLength1

maxLength70254592

media\_type: "application/zip"

The archive media type, always `application/zip`.

type: "base64"

The type of the object. Always `base64`.

type: "inline"

The type of the object. Always `inline`.

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

### Create an agent environment template

curl https://api.openai.com/v1/agents/environments/templates \
    -X POST \

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
