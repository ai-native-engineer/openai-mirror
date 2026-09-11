<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/files/ -->

[Environments](/api/reference/resources/beta/subresources/agents/subresources/environments)

# Files

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
