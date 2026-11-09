<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/environments/methods/list/ -->

## List agent environments

`beta.agents.environments.list(**kwargs) -> CursorPage<EnvironmentInfo>`

**get** `/agents/environments`

Lists OpenAI-hosted environments owned by the authenticated principal. Requires access to the prewarming beta.

- `after: String`

  Return resources after this resource ID in the selected order.

  `minLength: 0`, `maxLength: 1048576`

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

  `format: int64`, `minimum: 1`, `maximum: 100`

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

- `type: :openai_hosted`

  The hosting type to list. Defaults to `openai_hosted`.

  - `:openai_hosted`

- `class EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: String`

    The ID of the environment.

    `minLength: 0`

  - `files: Array[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    `minItems: 0`, `maxItems: 2000`

    - `class HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: String`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `file_id: String`

        The ID of the uploaded file.

        `minLength: 0`

      - `path: String`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `size_bytes: Integer`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      A file supplied inline when the session was created.

      - `id: String`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `path: String`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `size_bytes: Integer`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `object: :"agent.environment"`

    The object type. Always `agent.environment`.

    - `:"agent.environment"`

  - `plugins: Array[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `description: String`

      The installed plugin description.

      `minLength: 0`

    - `name: String`

      The installed plugin name.

      `minLength: 0`

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `skills: Array[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `class HostedSkillReference`

      A skill installed from the Skills API.

      - `description: String`

        The installed skill description.

        `minLength: 0`

      - `name: String`

        The installed skill name.

        `minLength: 0`

      - `skill_id: String`

        The referenced skill ID.

        `minLength: 0`

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The concrete skill version installed for this session.

        `minLength: 0`

    - `class Inline`

      A skill installed from an inline ZIP archive.

      - `description: String`

        The installed skill description.

        `minLength: 0`

      - `name: String`

        The installed skill name.

        `minLength: 0`

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `status: :pending | :ready | :connected | 4 more`

    The current environment connection status.

    - `:pending`

    - `:ready`

      Provisioning succeeded and the environment is available for attachment or use.

    - `:connected`

    - `:disconnected`

    - `:suspended`

      The sandbox is stopped and can be resumed from its private checkpoint.

    - `:expired`

    - `:failed`

  - `type: :openai_hosted | :self_hosted`

    Whether the environment is hosted by OpenAI or by the application.

    - `:openai_hosted`

    - `:self_hosted`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.environments.list

puts(page)

  "data": [
      "files": [
          "file_id": "file_id",
          "path": "path",
          "size_bytes": 0,
          "type": "file_id"
      "object": "agent.environment",
      "plugins": [
          "type": "inline"
      "skills": [
          "skill_id": "skill_id",
          "type": "skill_reference",
          "version": "version"
      "status": "pending",
      "type": "openai_hosted"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
