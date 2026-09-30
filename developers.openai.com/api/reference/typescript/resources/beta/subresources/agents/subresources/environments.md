<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/environments/ -->

# Environments

## Retrieve an agent environment

`client.beta.agents.environments.retrieve(stringenvironmentID, RequestOptionsoptions?): EnvironmentInfo`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

### Parameters

- `environmentID: string`

### Returns

- `EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: string`

    The ID of the environment.

  - `files: Array<HostedEnvironmentFile>`

    Files installed in the environment, without their contents.

    - `HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded file size in bytes.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedEnvironmentFileResourceInline`

      A file supplied inline when the session was created.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded file size in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: "agent.environment"`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: Array<HostedPlugin>`

    Plugins installed in the environment, without their archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedSkill>`

    Skills installed in the environment, without their archive contents.

    - `HostedSkillReference`

      A skill installed from the Skills API.

      - `description: string`

        The installed skill description.

      - `name: string`

        The installed skill name.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string`

        The concrete skill version installed for this session.

    - `HostedSkillResourceInline`

      A skill installed from an inline ZIP archive.

      - `description: string`

        The installed skill description.

      - `name: string`

        The installed skill name.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: "pending" | "connected" | "disconnected" | 2 more`

    The current environment connection status.

    - `"pending"`

    - `"connected"`

    - `"disconnected"`

    - `"expired"`

    - `"failed"`

  - `type: "openai_hosted" | "self_hosted"`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentInfo = await client.beta.agents.environments.retrieve('environment_id');

console.log(environmentInfo.id);
```

#### Response

```json
{
  "id": "id",
  "files": [
    {
      "id": "id",
      "file_id": "file_id",
      "path": "path",
      "size_bytes": 0,
      "type": "file_id"
    }
  ],
  "object": "agent.environment",
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "description": "description",
      "name": "name",
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "status": "pending",
  "type": "openai_hosted"
}
```

## Domain Types

### Environment Info

- `EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: string`

    The ID of the environment.

  - `files: Array<HostedEnvironmentFile>`

    Files installed in the environment, without their contents.

    - `HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded file size in bytes.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedEnvironmentFileResourceInline`

      A file supplied inline when the session was created.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded file size in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: "agent.environment"`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: Array<HostedPlugin>`

    Plugins installed in the environment, without their archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedSkill>`

    Skills installed in the environment, without their archive contents.

    - `HostedSkillReference`

      A skill installed from the Skills API.

      - `description: string`

        The installed skill description.

      - `name: string`

        The installed skill name.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string`

        The concrete skill version installed for this session.

    - `HostedSkillResourceInline`

      A skill installed from an inline ZIP archive.

      - `description: string`

        The installed skill description.

      - `name: string`

        The installed skill name.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: "pending" | "connected" | "disconnected" | 2 more`

    The current environment connection status.

    - `"pending"`

    - `"connected"`

    - `"disconnected"`

    - `"expired"`

    - `"failed"`

  - `type: "openai_hosted" | "self_hosted"`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

# Files

## Create an agent environment file

`client.beta.agents.environments.files.create(stringenvironmentID, FileCreateParamsbody, RequestOptionsoptions?): EnvironmentFile`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environmentID: string`

- `FileCreateParams = HostedEnvironmentFileParamFileID | HostedEnvironmentFileParamInline`

  - `FileCreateParamsBase`

    - `file_id?: string`

      The ID of the uploaded file.

    - `path_?: string`

      The absolute destination path inside `/workspace`.

    - `type?: "file_id"`

      The type of the object. Always `file_id`.

      - `"file_id"`

  - `HostedEnvironmentFileParamFileID extends FileCreateParamsBase`

  - `HostedEnvironmentFileParamInline extends FileCreateParamsBase`

### Returns

- `EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: string`

    The ID of the environment containing this file.

  - `object: "agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: string`

    The absolute file path inside the environment's workspace.

  - `size_bytes: number`

    The file size in bytes.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentFile = await client.beta.agents.environments.files.create('environment_id');

console.log(environmentFile.environment_id);
```

#### Response

```json
{
  "environment_id": "environment_id",
  "object": "agent.environment.file",
  "path": "path",
  "size_bytes": 0
}
```

## List agent environment files

`client.beta.agents.environments.files.list(stringenvironmentID, FileListParamsquery?, RequestOptionsoptions?): TokenPage<EnvironmentFile>`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environmentID: string`

- `query: FileListParams`

  - `limit?: number | null`

    The maximum number of files to return, between 1 and 100.

  - `order?: "asc" | "desc"`

    Sort by case-sensitive path components. Defaults to descending.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

  - `page?: string`

    The opaque token from the previous page. Keep the same path, order, and limit.

  - `path_?: string | null`

    Restrict the listing to this absolute workspace directory.

### Returns

- `EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: string`

    The ID of the environment containing this file.

  - `object: "agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: string`

    The absolute file path inside the environment's workspace.

  - `size_bytes: number`

    The file size in bytes.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const environmentFile of client.beta.agents.environments.files.list('environment_id')) {
  console.log(environmentFile.environment_id);
}
```

#### Response

```json
{
  "data": [
    {
      "environment_id": "environment_id",
      "object": "agent.environment.file",
      "path": "path",
      "size_bytes": 0
    }
  ],
  "has_more": true,
  "next": "next",
  "object": "page"
}
```

## Domain Types

### Environment File

- `EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: string`

    The ID of the environment containing this file.

  - `object: "agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: string`

    The absolute file path inside the environment's workspace.

  - `size_bytes: number`

    The file size in bytes.

# Templates

## Create an agent environment template

`client.beta.agents.environments.templates.create(TemplateCreateParamsbody?, RequestOptionsoptions?): EnvironmentTemplate`

**post** `/agents/environments/templates`

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

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

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplate = await client.beta.agents.environments.templates.create();

console.log(environmentTemplate.id);
```

#### Response

```json
{
  "id": "id",
  "capability_directories": [
    "string"
  ],
  "created_at": 0,
  "desktop": {
    "enabled": true
  },
  "files": [
    {
      "file_id": "file_id",
      "path": "path",
      "type": "file_id"
    }
  ],
  "name": "name",
  "network": {
    "access": "enabled",
    "allowed_domains": [
      "string"
    ]
  },
  "object": "agent.environment.template",
  "packages": {
    "npm": [
      "string"
    ],
    "python": [
      "string"
    ],
    "system": [
      "string"
    ]
  },
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "updated_at": 0
}
```

## Delete an agent environment template

`client.beta.agents.environments.templates.delete(stringenvironmentTemplateID, RequestOptionsoptions?): EnvironmentTemplateDeleted`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID: string`

### Returns

- `EnvironmentTemplateDeleted`

  A deleted reusable environment template.

  - `id: string`

    The ID of the deleted environment template.

  - `deleted: boolean`

    Whether the environment template was deleted. Always `true`.

  - `object: "agent.environment.template.deleted"`

    The object type. Always `agent.environment.template.deleted`.

    - `"agent.environment.template.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplateDeleted = await client.beta.agents.environments.templates.delete(
  'environment_template_id',
);

console.log(environmentTemplateDeleted.id);
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.environment.template.deleted"
}
```

## List agent environment templates

`client.beta.agents.environments.templates.list(TemplateListParamsquery?, RequestOptionsoptions?): CursorPage<EnvironmentTemplate>`

**get** `/agents/environments/templates`

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `query: TemplateListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `limit?: number`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `order?: "asc" | "desc"`

    The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const environmentTemplate of client.beta.agents.environments.templates.list()) {
  console.log(environmentTemplate.id);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "capability_directories": [
        "string"
      ],
      "created_at": 0,
      "desktop": {
        "enabled": true
      },
      "files": [
        {
          "file_id": "file_id",
          "path": "path",
          "type": "file_id"
        }
      ],
      "name": "name",
      "network": {
        "access": "enabled",
        "allowed_domains": [
          "string"
        ]
      },
      "object": "agent.environment.template",
      "packages": {
        "npm": [
          "string"
        ],
        "python": [
          "string"
        ],
        "system": [
          "string"
        ]
      },
      "plugins": [
        {
          "description": "description",
          "name": "name",
          "type": "inline"
        }
      ],
      "skills": [
        {
          "skill_id": "skill_id",
          "type": "skill_reference",
          "version": "version"
        }
      ],
      "updated_at": 0
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent environment template

`client.beta.agents.environments.templates.retrieve(stringenvironmentTemplateID, RequestOptionsoptions?): EnvironmentTemplate`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID: string`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplate = await client.beta.agents.environments.templates.retrieve(
  'environment_template_id',
);

console.log(environmentTemplate.id);
```

#### Response

```json
{
  "id": "id",
  "capability_directories": [
    "string"
  ],
  "created_at": 0,
  "desktop": {
    "enabled": true
  },
  "files": [
    {
      "file_id": "file_id",
      "path": "path",
      "type": "file_id"
    }
  ],
  "name": "name",
  "network": {
    "access": "enabled",
    "allowed_domains": [
      "string"
    ]
  },
  "object": "agent.environment.template",
  "packages": {
    "npm": [
      "string"
    ],
    "python": [
      "string"
    ],
    "system": [
      "string"
    ]
  },
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "updated_at": 0
}
```

## Update an agent environment template

`client.beta.agents.environments.templates.update(stringenvironmentTemplateID, TemplateUpdateParamsbody?, RequestOptionsoptions?): EnvironmentTemplate`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID: string`

- `body: TemplateUpdateParams`

  - `capability_directories?: Array<string> | null`

    Directories that expose capabilities to the agent.

  - `desktop?: Desktop | null`

    Replacement desktop configuration, or null to disable the desktop.

    - `enabled: boolean`

      Whether to provision the desktop and its browser proxy.

  - `env?: Record<string, string> | null`

    Replacement confidential environment values.

  - `files?: Array<HostedEnvironmentFileParam> | null`

    Replacement file configuration materialized for each new session.

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

    A replacement human-readable display name, or `null` to clear the name.

  - `network?: Network | null`

    Network access available after setup completes. Omit to preserve the current policy, or pass `null` to reset to disabled for GA requests or enabled for beta requests.

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

    Packages installed before the runtime network policy applies.

    - `npm?: Array<string> | null`

      npm packages to install globally. Defaults to an empty list.

    - `python?: Array<string> | null`

      Python packages to install. Defaults to an empty list.

    - `system?: Array<string> | null`

      System packages to install. Defaults to an empty list.

  - `plugins?: Array<HostedPluginParam> | null`

    Replacement plugin configuration installed for each new session.

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

    Replacement confidential setup commands, never included in returned resources.

    - `command: string`

      The shell command to execute.

    - `cwd?: string | null`

      The absolute working directory. Defaults to `/workspace`.

  - `skills?: Array<HostedSkillParam> | null`

    Replacement skill configuration installed for each new session.

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

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplate = await client.beta.agents.environments.templates.update(
  'environment_template_id',
);

console.log(environmentTemplate.id);
```

#### Response

```json
{
  "id": "id",
  "capability_directories": [
    "string"
  ],
  "created_at": 0,
  "desktop": {
    "enabled": true
  },
  "files": [
    {
      "file_id": "file_id",
      "path": "path",
      "type": "file_id"
    }
  ],
  "name": "name",
  "network": {
    "access": "enabled",
    "allowed_domains": [
      "string"
    ]
  },
  "object": "agent.environment.template",
  "packages": {
    "npm": [
      "string"
    ],
    "python": [
      "string"
    ],
    "system": [
      "string"
    ]
  },
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "updated_at": 0
}
```

## Domain Types

### Environment Template

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

### Environment Template Deleted

- `EnvironmentTemplateDeleted`

  A deleted reusable environment template.

  - `id: string`

    The ID of the deleted environment template.

  - `deleted: boolean`

    Whether the environment template was deleted. Always `true`.

  - `object: "agent.environment.template.deleted"`

    The object type. Always `agent.environment.template.deleted`.

    - `"agent.environment.template.deleted"`
