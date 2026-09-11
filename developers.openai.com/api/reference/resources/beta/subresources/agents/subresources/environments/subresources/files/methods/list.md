<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/list/ -->

[Environments](/api/reference/resources/beta/subresources/agents/subresources/environments)

[Files](/api/reference/resources/beta/subresources/agents/subresources/environments/subresources/files)

# List agent environment files

GET/agents/environments/{environment\_id}/files

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

environment\_id: string

##### Query ParametersExpand Collapse

limit: optional number or null

The maximum number of files to return, between 1 and 100.

minimum1

maximum100

order: optional "asc" or "desc"

Sort by case-sensitive path components. Defaults to descending.

"asc"

Returns resources in ascending order.

"desc"

Returns resources in descending order.

page: optional string

The opaque token from the previous page. Keep the same path, order, and limit.

path: optional string or null

Restrict the listing to this absolute workspace directory.

data: array of [EnvironmentFile](/api/reference/resources/beta#(resource)%20beta.agents.environments.files%20%3E%20(model)%20environment_file%20%3E%20(schema)) { environment\_id, object, path, size\_bytes }

Files available on the current page.

environment\_id: string

The ID of the environment containing this file.

object: "agent.environment.file"

The object type. Always `agent.environment.file`.

path: string

The absolute file path inside the environment’s workspace.

size\_bytes: number

The file size in bytes.

minimum0

has\_more: boolean

Whether more files follow this page.

next: string or null

The opaque cursor to use when requesting the next page, if any.

object: "page"

The object type. Always `page`.

### List agent environment files

curl https://api.openai.com/v1/agents/environments/$ENVIRONMENT_ID/files \

  "data": [
      "environment_id": "environment_id",
      "object": "agent.environment.file",
      "path": "path",
      "size_bytes": 0
  ],
  "has_more": true,
  "next": "next",
  "object": "page"

  "data": [
      "environment_id": "environment_id",
      "object": "agent.environment.file",
      "path": "path",
      "size_bytes": 0
  ],
  "has_more": true,
  "next": "next",
  "object": "page"
