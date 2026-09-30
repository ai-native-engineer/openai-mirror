<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/create/ -->

## Create an agent environment template

`client.beta.agents.environments.templates.create(TemplateCreateParamsbody?, RequestOptionsoptions?): EnvironmentTemplate`

**post** `/agents/environments/templates`

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `body: TemplateCreateParams`

  - `capability_directories?: Array<string> | null`

    Directories that contain capabilities exposed to the agent. Defaults to an empty list.

  - `desktop?: Desktop | null`

    Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

    - `enabled: boolean`

      Whether to provision the desktop and its browser proxy.

  - `env?: Record<string, string> | null`

    Environment variables made available to the agent.

  - `files?: Array<HostedEnvironmentFileParam> | null`

    Files available before the agent starts. Defaults to an empty list.

    - `HostedEnvironmentFileParamFileID`

      A file previously uploaded through the OpenAI Files API.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The absolute destination path inside `/workspace`.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedEnvironmentFileParamInline`

      A file supplied directly as standard-base64 data.

      - `data: string`

        The standard-base64-encoded file contents.

      - `path: string`

        The absolute destination path inside `/workspace`.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name?: string | null`

    An optional human-readable display name for the template.

  - `network?: Network | null`

    Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

    - `access: "enabled" | "disabled" | "restricted"`

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

    - `allowed_domains?: Array<string> | null`

      Domains the environment may access when network access is restricted.

    - `blocked_domains?: Array<string> | null`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `packages?: Packages | null`

    Packages to install in the environment. Defaults to empty package lists.

    - `npm?: Array<string> | null`

      npm packages to install globally. Defaults to an empty list.

    - `python?: Array<string> | null`

      Python packages to install. Defaults to an empty list.

    - `system?: Array<string> | null`

      System packages to install. Defaults to an empty list.

  - `plugins?: Array<HostedPluginParam> | null`

    Plugins provided as inline ZIP archives. Defaults to an empty list.

    - `description: string`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `name: string`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

      - `data: string`

        Standard-base64 encoded ZIP archive bytes.

      - `media_type: "application/zip"`

        The archive media type, always `application/zip`.

        - `"application/zip"`

          A ZIP archive.

      - `type: "base64"`

        The type of the object. Always `base64`.

        - `"base64"`

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `setup_commands?: Array<SetupCommandParam> | null`

    Ordered, confidential setup commands. Command bodies are never returned.

    - `command: string`

      The shell command to execute.

    - `cwd?: string | null`

      The absolute working directory. Defaults to `/workspace`.

  - `skills?: Array<HostedSkillParam> | null`

    Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

    - `HostedSkillParamSkillReference`

      References a skill uploaded through the Skills API.

      - `skill_id: string`

        The ID of the skill created through `/v1/skills`.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version?: string | null`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `HostedSkillParamInline`

      Supplies a skill ZIP directly in the session request.

      - `description: string`

        The skill description declared in `SKILL.md`.

      - `name: string`

        The skill name declared in `SKILL.md`.

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

- `EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: string`

    The ID of the reusable environment template.

  - `capability_directories: Array<string>`

    Directories that expose capabilities to the agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: boolean`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array<HostedTemplateFileResourceFileID | HostedTemplateFileResourceInline>`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `HostedTemplateFileResourceFileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedTemplateFileResourceInline`

      Metadata for confidential inline file contents.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded size of the inline file in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: string | null`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: "enabled" | "disabled" | "restricted"`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: Array<string>`

      Domains the environment may access when network access is restricted.

  - `object: "agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array<string>`

      npm packages installed globally in the environment.

    - `python: Array<string>`

      Python packages installed in the environment.

    - `system: Array<string>`

      System packages installed in the environment.

  - `plugins: Array<HostedPlugin>`

    Safe plugin metadata, excluding inline archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedTemplateSkillResourceSkillReference | HostedTemplateSkillResourceInline>`

    Safe skill metadata, preserving unresolved version selectors.

    - `HostedTemplateSkillResourceSkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string | null`

        The requested version selector, including `latest`.

    - `HostedTemplateSkillResourceInline`

      Safe metadata for an inline skill archive.

      - `description: string`

        The skill description declared in `SKILL.md`.

      - `name: string`

        The skill name declared in `SKILL.md`.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the template was last updated.

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplate = await client.beta.agents.environments.templates.create();

console.log(environmentTemplate.id);

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
