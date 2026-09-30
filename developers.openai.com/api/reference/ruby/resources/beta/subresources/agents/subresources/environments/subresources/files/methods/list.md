<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/list/ -->

## List agent environment files

`beta.agents.environments.files.list(environment_id, **kwargs) -> TokenPage<EnvironmentFile>`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

- `environment_id: String`

- `limit: Integer`

  The maximum number of files to return, between 1 and 100.

- `order: :asc | :desc`

  Sort by case-sensitive path components. Defaults to descending.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

- `page: String`

  The opaque token from the previous page. Keep the same path, order, and limit.

- `path: String`

  Restrict the listing to this absolute workspace directory.

- `class EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: String`

    The ID of the environment containing this file.

  - `object: :"agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `:"agent.environment.file"`

  - `path: String`

    The absolute file path inside the environment's workspace.

  - `size_bytes: Integer`

    The file size in bytes.

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.environments.files.list("environment_id")

puts(page)

  "data": [
      "environment_id": "environment_id",
      "object": "agent.environment.file",
      "path": "path",
      "size_bytes": 0
  "has_more": true,
  "next": "next",
  "object": "page"
