<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/environments/methods/create/ -->

## Create an agent environment

`beta.agents.environments.create(EnvironmentCreateParams**kwargs)  -> EnvironmentInfo`

**post** `/agents/environments`

Creates an OpenAI-hosted environment before creating a session. Requires access to the prewarming beta.

- `environment: Environment`

  The required hosting type and its configuration.

  - `type: Literal["openai_hosted"]`

    The type of the object. Always `openai_hosted`.

    - `"openai_hosted"`

  - `capability_directories: Optional[Sequence[str]]`

    Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    `minItems: 0`, `maxItems: 16384`

  - `desktop: Optional[EnvironmentDesktop]`

    Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

    - `enabled: bool`

      Whether to provision the desktop and its browser proxy.

  - `env: Optional[Dict[str, str]]`

    Environment variables made available to the agent.

  - `environment_template_id: Optional[str]`

    A reusable hosted template applied before inline configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    `minLength: 0`, `maxLength: 64`

  - `files: Optional[Iterable[HostedEnvironmentFileParam]]`

    Files available before the agent starts. Defaults to an empty list.

    `minItems: 0`, `maxItems: 50`

    - `class HostedEnvironmentFileParamFileID: …`

      A file previously uploaded through the OpenAI Files API.

      - `file_id: str`

        The ID of the uploaded file.

        `minLength: 1`, `maxLength: 256`

      - `path: str`

        The absolute destination path inside `/workspace`.

        `minLength: 1`, `maxLength: 4096`

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class HostedEnvironmentFileParamInline: …`

      A file supplied directly as standard-base64 data.

      - `data: str`

        The standard-base64-encoded file contents.

        `minLength: 0`, `maxLength: 6990508`

      - `path: str`

        The absolute destination path inside `/workspace`.

        `minLength: 1`, `maxLength: 4096`

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `network: Optional[EnvironmentNetwork]`

    Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

    - `access: Literal["enabled", "disabled", "restricted"]`

      The environment's network access mode.

      - `enabled` - Allows unrestricted network access.
      - `disabled` - Disables network access.
      - `restricted` - Applies the configured domain restrictions.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: Optional[Sequence[str]]`

      Domains the environment may access when network access is restricted.

      `minItems: 0`, `maxItems: 16384`

    - `blocked_domains: Optional[Sequence[str]]`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

      `minItems: 0`, `maxItems: 100`

  - `packages: Optional[EnvironmentPackages]`

    Packages to install in the environment. Defaults to empty package lists.

    - `npm: Optional[Sequence[str]]`

      npm packages to install globally. Defaults to an empty list.

      `minItems: 0`, `maxItems: 16384`

    - `python: Optional[Sequence[str]]`

      Python packages to install. Defaults to an empty list.

      `minItems: 0`, `maxItems: 16384`

    - `system: Optional[Sequence[str]]`

      System packages to install. Defaults to an empty list.

      `minItems: 0`, `maxItems: 16384`

  - `plugins: Optional[Iterable[HostedPluginParam]]`

    Plugins provided as inline ZIP archives. Defaults to an empty list.

    `minItems: 0`, `maxItems: 32`

    - `description: str`

      The plugin description declared in `.codex-plugin/plugin.json`.

      `minLength: 0`, `maxLength: 1048576`

    - `name: str`

      The plugin name declared in `.codex-plugin/plugin.json`.

      `minLength: 1`, `maxLength: 64`

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

      - `data: str`

        Standard-base64 encoded ZIP archive bytes.

        `minLength: 1`, `maxLength: 70254592`

      - `media_type: Literal["application/zip"]`

        The archive media type, always `application/zip`.

        - `"application/zip"`

      - `type: Literal["base64"]`

        The type of the object. Always `base64`.

        - `"base64"`

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `setup_commands: Optional[Iterable[SetupCommandParam]]`

    Ordered, confidential setup commands. Command bodies are never returned.

    `minItems: 0`, `maxItems: 16`

    - `command: str`

      The shell command to execute.

      `minLength: 0`, `maxLength: 65536`

    - `cwd: Optional[str]`

      The absolute working directory. Defaults to `/workspace`.

      `minLength: 0`, `maxLength: 4096`

  - `skills: Optional[Iterable[HostedSkillParam]]`

    Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

    `minItems: 0`, `maxItems: 200`

    - `class HostedSkillParamSkillReference: …`

      References a skill uploaded through the Skills API.

      - `skill_id: str`

        The ID of the skill created through `/v1/skills`.

        `minLength: 1`, `maxLength: 64`

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: Optional[str]`

        The skill version, a positive integer or `latest`; omission selects the default.

        `minLength: 0`, `maxLength: 1048576`

    - `class HostedSkillParamInline: …`

      Supplies a skill ZIP directly in the session request.

      - `description: str`

        The skill description declared in `SKILL.md`.

        `minLength: 0`, `maxLength: 1048576`

      - `name: str`

        The skill name declared in `SKILL.md`.

        `minLength: 1`, `maxLength: 64`

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

- `vault_ids: Optional[Sequence[str]]`

  The IDs of up to 10 vaults made available to an OpenAI-hosted environment.

  `minItems: 0`, `maxItems: 10`

- `idempotency_key: Optional[str]`

  `minLength: 1`, `maxLength: 256`

- `class EnvironmentInfo: …`

  Safe metadata for a first-class execution environment.

  - `id: str`

    The ID of the environment.

    `minLength: 0`

  - `files: List[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    `minItems: 0`, `maxItems: 2000`

    - `class HostedEnvironmentFileID: …`

      A file copied from the OpenAI Files API.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `file_id: str`

        The ID of the uploaded file.

        `minLength: 0`

      - `path: str`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `size_bytes: int`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class HostedEnvironmentFileResourceInline: …`

      A file supplied inline when the session was created.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `path: str`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `size_bytes: int`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: Literal["agent.environment"]`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: List[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `description: str`

      The installed plugin description.

      `minLength: 0`

    - `name: str`

      The installed plugin name.

      `minLength: 0`

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `class HostedSkillReference: …`

      A skill installed from the Skills API.

      - `description: str`

        The installed skill description.

        `minLength: 0`

      - `name: str`

        The installed skill name.

        `minLength: 0`

      - `skill_id: str`

        The referenced skill ID.

        `minLength: 0`

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: str`

        The concrete skill version installed for this session.

        `minLength: 0`

    - `class HostedSkillResourceInline: …`

      A skill installed from an inline ZIP archive.

      - `description: str`

        The installed skill description.

        `minLength: 0`

      - `name: str`

        The installed skill name.

        `minLength: 0`

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: Literal["pending", "ready", "connected", 4 more]`

    The current environment connection status.

    - `"pending"`

    - `"ready"`

      Provisioning succeeded and the environment is available for attachment or use.

    - `"connected"`

    - `"disconnected"`

    - `"suspended"`

      The sandbox is stopped and can be resumed from its private checkpoint.

    - `"expired"`

    - `"failed"`

  - `type: Literal["openai_hosted", "self_hosted"]`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
environment_info = client.beta.agents.environments.create(
    environment={
        "type": "openai_hosted"
print(environment_info.id)

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
