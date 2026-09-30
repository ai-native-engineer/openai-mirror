<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/environments/methods/retrieve/ -->

## Retrieve an agent environment

`beta.agents.environments.retrieve(environment_id) -> EnvironmentInfo`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

- `environment_id: String`

- `class EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: String`

    The ID of the environment.

  - `files: Array[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: String`

        The session-scoped ID of the file in the execution environment.

      - `file_id: String`

        The ID of the uploaded file.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded file size in bytes.

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      A file supplied inline when the session was created.

      - `id: String`

        The session-scoped ID of the file in the execution environment.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded file size in bytes.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `object: :"agent.environment"`

    The object type. Always `agent.environment`.

    - `:"agent.environment"`

  - `plugins: Array[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    - `description: String`

      The installed plugin description.

    - `name: String`

      The installed plugin name.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `skills: Array[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference`

      A skill installed from the Skills API.

      - `description: String`

        The installed skill description.

      - `name: String`

        The installed skill name.

      - `skill_id: String`

        The referenced skill ID.

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The concrete skill version installed for this session.

    - `class Inline`

      A skill installed from an inline ZIP archive.

      - `description: String`

        The installed skill description.

      - `name: String`

        The installed skill name.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `status: :pending | :connected | :disconnected | 2 more`

    The current environment connection status.

    - `:pending`

    - `:connected`

    - `:disconnected`

    - `:expired`

    - `:failed`

  - `type: :openai_hosted | :self_hosted`

    Whether the environment is hosted by OpenAI or by the application.

    - `:openai_hosted`

    - `:self_hosted`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

environment_info = openai.beta.agents.environments.retrieve("environment_id")

puts(environment_info)

  "files": [
      "file_id": "file_id",
      "path": "path",
      "size_bytes": 0,
      "type": "file_id"
  "object": "agent.environment",
  "plugins": [
      "description": "description",
      "type": "inline"
  "skills": [
      "description": "description",
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
  "status": "pending",
  "type": "openai_hosted"
