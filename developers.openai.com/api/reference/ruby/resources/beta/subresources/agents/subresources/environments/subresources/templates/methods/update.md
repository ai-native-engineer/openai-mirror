<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/update/ -->

## Update an agent environment template

`beta.agents.environments.templates.update(environment_template_id, **kwargs) -> EnvironmentTemplate`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `environment_template_id: String`

- `capability_directories: Array[String]`

  Directories that expose capabilities to the agent.

- `desktop: Desktop{ enabled}`

  Replacement desktop configuration, or null to disable the desktop.

  - `enabled: bool`

    Whether to provision the desktop and its browser proxy.

- `env: Hash[Symbol, String]`

  Replacement confidential environment values.

- `files: Array[HostedEnvironmentFileParam]`

  Replacement file configuration materialized for each new session.

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

- `name: String`

  A replacement human-readable display name, or `null` to clear the name.

- `network: Network{ access, allowed_domains, blocked_domains}`

  Network access available after setup completes. Omit to preserve the current policy, or pass `null` to reset to disabled for GA requests or enabled for beta requests.

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

  - `blocked_domains: Array[String]`

    Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

- `packages: Packages{ npm, python, system_}`

  Packages installed before the runtime network policy applies.

  - `npm: Array[String]`

    npm packages to install globally. Defaults to an empty list.

  - `python: Array[String]`

    Python packages to install. Defaults to an empty list.

  - `system_: Array[String]`

    System packages to install. Defaults to an empty list.

- `plugins: Array[HostedPluginParam]`

  Replacement plugin configuration installed for each new session.

  - `description: String`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `name: String`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `source: InlineCapabilitySourceParam`

    Provides ZIP bytes encoded with standard base64.

    - `data: String`

      Standard-base64 encoded ZIP archive bytes.

    - `media_type: :"application/zip"`

      The archive media type, always `application/zip`.

      - `:"application/zip"`

        A ZIP archive.

    - `type: :base64`

      The type of the object. Always `base64`.

      - `:base64`

  - `type: :inline`

    The type of the object. Always `inline`.

    - `:inline`

- `setup_commands: Array[SetupCommandParam]`

  Replacement confidential setup commands, never included in returned resources.

  - `command: String`

    The shell command to execute.

  - `cwd: String`

    The absolute working directory. Defaults to `/workspace`.

- `skills: Array[HostedSkillParam]`

  Replacement skill configuration installed for each new session.

  - `class SkillReference`

    References a skill uploaded through the Skills API.

    - `skill_id: String`

      The ID of the skill created through `/v1/skills`.

    - `type: :skill_reference`

      The type of the object. Always `skill_reference`.

      - `:skill_reference`

    - `version: String`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `class Inline`

    Supplies a skill ZIP directly in the session request.

    - `description: String`

      The skill description declared in `SKILL.md`.

    - `name: String`

      The skill name declared in `SKILL.md`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

- `class EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: String`

    The ID of the reusable environment template.

  - `capability_directories: Array[String]`

    Directories that expose capabilities to the agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop{ enabled}`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: String`

        The ID of the uploaded file.

      - `path: String`

        The file's absolute path inside the environment.

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      Metadata for confidential inline file contents.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded size of the inline file in bytes.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `name: String`

    An optional human-readable display name for the template.

  - `network: Network{ access, allowed_domains}`

    Runtime network access for each OpenAI-hosted environment.

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

  - `object: :"agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `:"agent.environment.template"`

  - `packages: Packages{ npm, python, system_}`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array[String]`

      npm packages installed globally in the environment.

    - `python: Array[String]`

      Python packages installed in the environment.

    - `system_: Array[String]`

      System packages installed in the environment.

  - `plugins: Array[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: String`

      The installed plugin description.

    - `name: String`

      The installed plugin name.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: String`

        The referenced skill ID.

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The requested version selector, including `latest`.

    - `class Inline`

      Safe metadata for an inline skill archive.

      - `description: String`

        The skill description declared in `SKILL.md`.

      - `name: String`

        The skill name declared in `SKILL.md`.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the template was last updated.

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

environment_template = openai.beta.agents.environments.templates.update("environment_template_id")

puts(environment_template)

  "capability_directories": [
    "string"
  "desktop": {
    "enabled": true
  "files": [
      "file_id": "file_id",
      "path": "path",
      "type": "file_id"
  "network": {
    "access": "enabled",
    "allowed_domains": [
      "string"
    ]
  "object": "agent.environment.template",
  "packages": {
    "npm": [
      "string"
    "python": [
      "string"
    "system": [
      "string"
    ]
  "plugins": [
      "description": "description",
      "type": "inline"
  "skills": [
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
  "updated_at": 0
