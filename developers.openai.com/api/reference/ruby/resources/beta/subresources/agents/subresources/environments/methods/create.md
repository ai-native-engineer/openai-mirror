<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/environments/methods/create/ -->

## Create an agent environment

`beta.agents.environments.create(**kwargs) -> EnvironmentInfo`

**post** `/agents/environments`

Creates an OpenAI-hosted environment before creating a session. Requires access to the prewarming beta.

- `environment: Environment{ type, capability_directories, desktop, 8 more}`

  The required hosting type and its configuration.

  - `type: :openai_hosted`

    The type of the object. Always `openai_hosted`.

    - `:openai_hosted`

  - `capability_directories: Array[String]`

    Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    `minItems: 0`, `maxItems: 16384`

  - `desktop: Desktop{ enabled}`

    Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

    - `enabled: bool`

      Whether to provision the desktop and its browser proxy.

  - `env: Hash[Symbol, String]`

    Environment variables made available to the agent.

  - `environment_template_id: String`

    A reusable hosted template applied before inline configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    `minLength: 0`, `maxLength: 64`

  - `files: Array[HostedEnvironmentFileParam]`

    Files available before the agent starts. Defaults to an empty list.

    `minItems: 0`, `maxItems: 50`

    - `class FileID`

      A file previously uploaded through the OpenAI Files API.

      - `file_id: String`

        The ID of the uploaded file.

        `minLength: 1`, `maxLength: 256`

      - `path: String`

        The absolute destination path inside `/workspace`.

        `minLength: 1`, `maxLength: 4096`

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      A file supplied directly as standard-base64 data.

      - `data: String`

        The standard-base64-encoded file contents.

        `minLength: 0`, `maxLength: 6990508`

      - `path: String`

        The absolute destination path inside `/workspace`.

        `minLength: 1`, `maxLength: 4096`

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `network: Network{ access, allowed_domains, blocked_domains}`

    Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

    - `access: :enabled | :disabled | :restricted`

      The environment's network access mode.

      - `:enabled`

        Allows unrestricted network access.

      - `:disabled`

        Disables network access.

      - `:restricted`

        Applies the configured domain restrictions.

    - `allowed_domains: Array[String]`

      Domains the environment may access when network access is restricted.

      `minItems: 0`, `maxItems: 16384`

    - `blocked_domains: Array[String]`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

      `minItems: 0`, `maxItems: 100`

  - `packages: Packages{ npm, python, system_}`

    Packages to install in the environment. Defaults to empty package lists.

    - `npm: Array[String]`

      npm packages to install globally. Defaults to an empty list.

      `minItems: 0`, `maxItems: 16384`

    - `python: Array[String]`

      Python packages to install. Defaults to an empty list.

      `minItems: 0`, `maxItems: 16384`

    - `system_: Array[String]`

      System packages to install. Defaults to an empty list.

      `minItems: 0`, `maxItems: 16384`

  - `plugins: Array[HostedPluginParam]`

    Plugins provided as inline ZIP archives. Defaults to an empty list.

    `minItems: 0`, `maxItems: 32`

    - `description: String`

      The plugin description declared in `.codex-plugin/plugin.json`.

      `minLength: 0`, `maxLength: 1048576`

    - `name: String`

      The plugin name declared in `.codex-plugin/plugin.json`.

      `minLength: 1`, `maxLength: 64`

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

      - `data: String`

        Standard-base64 encoded ZIP archive bytes.

        `minLength: 1`, `maxLength: 70254592`

      - `media_type: :"application/zip"`

        The archive media type, always `application/zip`.

        - `:"application/zip"`

      - `type: :base64`

        The type of the object. Always `base64`.

        - `:base64`

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `setup_commands: Array[SetupCommandParam]`

    Ordered, confidential setup commands. Command bodies are never returned.

    `minItems: 0`, `maxItems: 16`

    - `command: String`

      The shell command to execute.

      `minLength: 0`, `maxLength: 65536`

    - `cwd: String`

      The absolute working directory. Defaults to `/workspace`.

      `minLength: 0`, `maxLength: 4096`

  - `skills: Array[HostedSkillParam]`

    Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

    `minItems: 0`, `maxItems: 200`

    - `class SkillReference`

      References a skill uploaded through the Skills API.

      - `skill_id: String`

        The ID of the skill created through `/v1/skills`.

        `minLength: 1`, `maxLength: 64`

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The skill version, a positive integer or `latest`; omission selects the default.

        `minLength: 0`, `maxLength: 1048576`

    - `class Inline`

      Supplies a skill ZIP directly in the session request.

      - `description: String`

        The skill description declared in `SKILL.md`.

        `minLength: 0`, `maxLength: 1048576`

      - `name: String`

        The skill name declared in `SKILL.md`.

        `minLength: 1`, `maxLength: 64`

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

- `vault_ids: Array[String]`

  The IDs of up to 10 vaults made available to an OpenAI-hosted environment.

  `minItems: 0`, `maxItems: 10`

- `idempotency_key: String`

  `minLength: 1`, `maxLength: 256`

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

environment_info = openai.beta.agents.environments.create(environment: {type: :openai_hosted})

puts(environment_info)

#### 201 — Example

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
