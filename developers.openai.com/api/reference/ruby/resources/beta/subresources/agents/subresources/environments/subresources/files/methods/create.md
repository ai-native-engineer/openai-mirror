<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/create/ -->

## Create an agent environment file

`beta.agents.environments.files.create(environment_id, **kwargs) -> EnvironmentFile`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

- `environment_id: String`

- `hosted_environment_file_param: HostedEnvironmentFileParam`

  A file materialized in an OpenAI-hosted execution environment.

  - `class FileID`

    A file previously uploaded through the OpenAI Files API.

    - `file_id: String`

      The ID of the uploaded file.

    - `path: String`

      The absolute destination path inside `/workspace`.

    - `type: :file_id`

      The type of the object. Always `file_id`.

      - `:file_id`

  - `class Inline`

    A file supplied directly as standard-base64 data.

    - `data: String`

      The standard-base64-encoded file contents.

    - `path: String`

      The absolute destination path inside `/workspace`.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

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

environment_file = openai.beta.agents.environments.files.create("environment_id")

puts(environment_file)

  "environment_id": "environment_id",
  "object": "agent.environment.file",
  "path": "path",
  "size_bytes": 0
