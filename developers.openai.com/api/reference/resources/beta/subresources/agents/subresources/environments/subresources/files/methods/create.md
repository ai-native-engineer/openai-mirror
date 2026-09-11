<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/create/ -->

[Environments](/api/reference/resources/beta/subresources/agents/subresources/environments)

[Files](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/files)

# Create an agent environment file

POST/agents/environments/{environment\_id}/files

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

environment\_id: string

##### Body ParametersJSONExpand Collapse

hosted\_environment\_file\_param: [HostedEnvironmentFileParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_environment_file_param%20%3E%20(schema))

A file materialized in an OpenAI-hosted execution environment.

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

### Create an agent environment file

curl https://api.openai.com/v1/agents/environments/$ENVIRONMENT_ID/files \
    -X POST \

  "environment_id": "environment_id",
  "object": "agent.environment.file",
  "path": "path",
  "size_bytes": 0

  "environment_id": "environment_id",
  "object": "agent.environment.file",
  "path": "path",
  "size_bytes": 0
