<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/update/ -->

## Update an agent environment template

`beta.agents.environments.templates.update(strenvironment_template_id, TemplateUpdateParams**kwargs)  -> EnvironmentTemplate`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `environment_template_id: str`

- `capability_directories: Optional[Sequence[str]]`

  Directories that expose capabilities to the agent.

- `desktop: Optional[Desktop]`

  Replacement desktop configuration, or null to disable the desktop.

  - `enabled: bool`

    Whether to provision the desktop and its browser proxy.

- `env: Optional[Dict[str, str]]`

  Replacement confidential environment values.

- `files: Optional[Iterable[HostedEnvironmentFileParam]]`

  Replacement file configuration materialized for each new session.

  - `class HostedEnvironmentFileParamFileID: …`

    A file previously uploaded through the OpenAI Files API.

    - `file_id: str`

      The ID of the uploaded file.

    - `path: str`

      The absolute destination path inside `/workspace`.

    - `type: Literal["file_id"]`

      The type of the object. Always `file_id`.

      - `"file_id"`

  - `class HostedEnvironmentFileParamInline: …`

    A file supplied directly as standard-base64 data.

    - `data: str`

      The standard-base64-encoded file contents.

    - `path: str`

      The absolute destination path inside `/workspace`.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

- `name: Optional[str]`

  A replacement human-readable display name, or `null` to clear the name.

- `network: Optional[Network]`

  Network access available after setup completes. Omit to preserve the current policy, or pass `null` to reset to disabled for GA requests or enabled for beta requests.

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

  - `blocked_domains: Optional[Sequence[str]]`

    Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

- `packages: Optional[Packages]`

  Packages installed before the runtime network policy applies.

  - `npm: Optional[Sequence[str]]`

    npm packages to install globally. Defaults to an empty list.

  - `python: Optional[Sequence[str]]`

    Python packages to install. Defaults to an empty list.

  - `system: Optional[Sequence[str]]`

    System packages to install. Defaults to an empty list.

- `plugins: Optional[Iterable[HostedPluginParam]]`

  Replacement plugin configuration installed for each new session.

  - `description: str`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `name: str`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `source: InlineCapabilitySourceParam`

    Provides ZIP bytes encoded with standard base64.

    - `data: str`

      Standard-base64 encoded ZIP archive bytes.

    - `media_type: Literal["application/zip"]`

      The archive media type, always `application/zip`.

      - `"application/zip"`

        A ZIP archive.

    - `type: Literal["base64"]`

      The type of the object. Always `base64`.

      - `"base64"`

  - `type: Literal["inline"]`

    The type of the object. Always `inline`.

    - `"inline"`

- `setup_commands: Optional[Iterable[SetupCommandParam]]`

  Replacement confidential setup commands, never included in returned resources.

  - `command: str`

    The shell command to execute.

  - `cwd: Optional[str]`

    The absolute working directory. Defaults to `/workspace`.

- `skills: Optional[Iterable[HostedSkillParam]]`

  Replacement skill configuration installed for each new session.

  - `class HostedSkillParamSkillReference: …`

    References a skill uploaded through the Skills API.

    - `skill_id: str`

      The ID of the skill created through `/v1/skills`.

    - `type: Literal["skill_reference"]`

      The type of the object. Always `skill_reference`.

      - `"skill_reference"`

    - `version: Optional[str]`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `class HostedSkillParamInline: …`

    Supplies a skill ZIP directly in the session request.

    - `description: str`

      The skill description declared in `SKILL.md`.

    - `name: str`

      The skill name declared in `SKILL.md`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

- `class EnvironmentTemplate: …`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: str`

    The ID of the reusable environment template.

  - `capability_directories: List[str]`

    Directories that expose capabilities to the agent.

  - `created_at: int`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: List[File]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileHostedTemplateFileResourceFileID: …`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class FileHostedTemplateFileResourceInline: …`

      Metadata for confidential inline file contents.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded size of the inline file in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: Optional[str]`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: Literal["enabled", "disabled", "restricted"]`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: List[str]`

      Domains the environment may access when network access is restricted.

  - `object: Literal["agent.environment.template"]`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: List[str]`

      npm packages installed globally in the environment.

    - `python: List[str]`

      Python packages installed in the environment.

    - `system: List[str]`

      System packages installed in the environment.

  - `plugins: List[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[Skill]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillHostedTemplateSkillResourceSkillReference: …`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: Optional[str]`

        The requested version selector, including `latest`.

    - `class SkillHostedTemplateSkillResourceInline: …`

      Safe metadata for an inline skill archive.

      - `description: str`

        The skill description declared in `SKILL.md`.

      - `name: str`

        The skill name declared in `SKILL.md`.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the template was last updated.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
environment_template = client.beta.agents.environments.templates.update(
    environment_template_id="environment_template_id",
print(environment_template.id)

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
