<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/environments/methods/create/ -->

## Create an agent environment

`client.beta.agents.environments.create(EnvironmentCreateParamsparams, RequestOptionsoptions?): EnvironmentInfo`

**post** `/agents/environments`

Creates an OpenAI-hosted environment before creating a session. Requires access to the prewarming beta.

- `params: EnvironmentCreateParams`

  - `environment: Environment`

    Body param: The required hosting type and its configuration.

    - `type: "openai_hosted"`

      The type of the object. Always `openai_hosted`.

      - `"openai_hosted"`

    - `capability_directories?: Array<string> | null`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

      `minItems: 0`, `maxItems: 16384`

    - `desktop?: Desktop | null`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `enabled: boolean`

        Whether to provision the desktop and its browser proxy.

    - `env?: Record<string, string> | null`

      Environment variables made available to the agent.

    - `environment_template_id?: string`

      A reusable hosted template applied before inline configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

      `minLength: 0`, `maxLength: 64`

    - `files?: Array<HostedEnvironmentFileParam> | null`

      Files available before the agent starts. Defaults to an empty list.

      `minItems: 0`, `maxItems: 50`

      - `HostedEnvironmentFileParamFileID`

        A file previously uploaded through the OpenAI Files API.

        - `file_id: string`

          The ID of the uploaded file.

          `minLength: 1`, `maxLength: 256`

        - `path: string`

          The absolute destination path inside `/workspace`.

          `minLength: 1`, `maxLength: 4096`

        - `type: "file_id"`

          The type of the object. Always `file_id`.

          - `"file_id"`

      - `HostedEnvironmentFileParamInline`

        A file supplied directly as standard-base64 data.

        - `data: string`

          The standard-base64-encoded file contents.

          `minLength: 0`, `maxLength: 6990508`

        - `path: string`

          The absolute destination path inside `/workspace`.

          `minLength: 1`, `maxLength: 4096`

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

    - `network?: Network | null`

      Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

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

        `minItems: 0`, `maxItems: 16384`

      - `blocked_domains?: Array<string> | null`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

        `minItems: 0`, `maxItems: 100`

    - `packages?: Packages | null`

      Packages to install in the environment. Defaults to empty package lists.

      - `npm?: Array<string> | null`

        npm packages to install globally. Defaults to an empty list.

        `minItems: 0`, `maxItems: 16384`

      - `python?: Array<string> | null`

        Python packages to install. Defaults to an empty list.

        `minItems: 0`, `maxItems: 16384`

      - `system?: Array<string> | null`

        System packages to install. Defaults to an empty list.

        `minItems: 0`, `maxItems: 16384`

    - `plugins?: Array<HostedPluginParam> | null`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      `minItems: 0`, `maxItems: 32`

      - `description: string`

        The plugin description declared in `.codex-plugin/plugin.json`.

        `minLength: 0`, `maxLength: 1048576`

      - `name: string`

        The plugin name declared in `.codex-plugin/plugin.json`.

        `minLength: 1`, `maxLength: 64`

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

        - `data: string`

          Standard-base64 encoded ZIP archive bytes.

          `minLength: 1`, `maxLength: 70254592`

        - `media_type: "application/zip"`

          The archive media type, always `application/zip`.

          - `"application/zip"`

        - `type: "base64"`

          The type of the object. Always `base64`.

          - `"base64"`

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

    - `setup_commands?: Array<SetupCommandParam> | null`

      Ordered, confidential setup commands. Command bodies are never returned.

      `minItems: 0`, `maxItems: 16`

      - `command: string`

        The shell command to execute.

        `minLength: 0`, `maxLength: 65536`

      - `cwd?: string | null`

        The absolute working directory. Defaults to `/workspace`.

        `minLength: 0`, `maxLength: 4096`

    - `skills?: Array<HostedSkillParam> | null`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      `minItems: 0`, `maxItems: 200`

      - `HostedSkillParamSkillReference`

        References a skill uploaded through the Skills API.

        - `skill_id: string`

          The ID of the skill created through `/v1/skills`.

          `minLength: 1`, `maxLength: 64`

        - `type: "skill_reference"`

          The type of the object. Always `skill_reference`.

          - `"skill_reference"`

        - `version?: string | null`

          The skill version, a positive integer or `latest`; omission selects the default.

          `minLength: 0`, `maxLength: 1048576`

      - `HostedSkillParamInline`

        Supplies a skill ZIP directly in the session request.

        - `description: string`

          The skill description declared in `SKILL.md`.

          `minLength: 0`, `maxLength: 1048576`

        - `name: string`

          The skill name declared in `SKILL.md`.

          `minLength: 1`, `maxLength: 64`

        - `source: InlineCapabilitySourceParam`

          Provides ZIP bytes encoded with standard base64.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

  - `vault_ids?: Array<string> | null`

    Body param: The IDs of up to 10 vaults made available to an OpenAI-hosted environment.

    `minItems: 0`, `maxItems: 10`

  - `idempotencyKey?: string`

    Header param: Deduplicates creation for 24 hours within the authenticated organization, project, and creator. Retry the same JSON parameters with the same key to retrieve the original environment in its current state. Different parameters or an incomplete hosted creation return 409. Deleted environments are not recreated. After retention expires, the key may create a new environment. Without this header, each request creates a new environment.

    `minLength: 1`, `maxLength: 256`

- `EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: string`

    The ID of the environment.

    `minLength: 0`

  - `files: Array<HostedEnvironmentFile>`

    Files installed in the environment, without their contents.

    `minItems: 0`, `maxItems: 2000`

    - `HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `file_id: string`

        The ID of the uploaded file.

        `minLength: 0`

      - `path: string`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `size_bytes: number`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedEnvironmentFileResourceInline`

      A file supplied inline when the session was created.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `path: string`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `size_bytes: number`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: "agent.environment"`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: Array<HostedPlugin>`

    Plugins installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `description: string`

      The installed plugin description.

      `minLength: 0`

    - `name: string`

      The installed plugin name.

      `minLength: 0`

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedSkill>`

    Skills installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `HostedSkillReference`

      A skill installed from the Skills API.

      - `description: string`

        The installed skill description.

        `minLength: 0`

      - `name: string`

        The installed skill name.

        `minLength: 0`

      - `skill_id: string`

        The referenced skill ID.

        `minLength: 0`

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string`

        The concrete skill version installed for this session.

        `minLength: 0`

    - `HostedSkillResourceInline`

      A skill installed from an inline ZIP archive.

      - `description: string`

        The installed skill description.

        `minLength: 0`

      - `name: string`

        The installed skill name.

        `minLength: 0`

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: "pending" | "ready" | "connected" | 4 more`

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

  - `type: "openai_hosted" | "self_hosted"`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentInfo = await client.beta.agents.environments.create({
  environment: { type: 'openai_hosted' },
});

console.log(environmentInfo.id);

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
