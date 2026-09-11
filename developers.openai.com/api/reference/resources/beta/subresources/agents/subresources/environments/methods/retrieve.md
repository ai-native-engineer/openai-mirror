<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/environments/methods/retrieve/ -->

[Environments](/api/reference/resources/beta/subresources/agents/subresources/environments)

# Retrieve an agent environment

GET/agents/environments/{environment\_id}

Retrieves an execution environment’s connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

environment\_id: string

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

### Retrieve an agent environment

curl https://api.openai.com/v1/agents/environments/$ENVIRONMENT_ID \

  "files": [
      "file_id": "file_id",
      "path": "path",
      "size_bytes": 0,
      "type": "file_id"
  ],
  "object": "agent.environment",
  "plugins": [
      "description": "description",
      "name": "name",
      "type": "inline"
  ],
  "skills": [
      "description": "description",
      "name": "name",
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
  ],
  "status": "pending",
  "type": "openai_hosted"

  "files": [
      "file_id": "file_id",
      "path": "path",
      "size_bytes": 0,
      "type": "file_id"
  ],
  "object": "agent.environment",
  "plugins": [
      "description": "description",
      "name": "name",
      "type": "inline"
  ],
  "skills": [
      "description": "description",
      "name": "name",
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
  ],
  "status": "pending",
  "type": "openai_hosted"
