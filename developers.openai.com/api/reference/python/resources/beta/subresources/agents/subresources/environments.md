<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/environments/ -->

# Environments

## Retrieve an agent environment

`beta.agents.environments.retrieve(strenvironment_id)  -> EnvironmentInfo`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

### Parameters

- `environment_id: str`

### Returns

- `class EnvironmentInfo: …`

  Safe metadata for a first-class execution environment.

  - `id: str`

    The ID of the environment.

  - `files: List[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileID: …`

      A file copied from the OpenAI Files API.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded file size in bytes.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class HostedEnvironmentFileResourceInline: …`

      A file supplied inline when the session was created.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded file size in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: Literal["agent.environment"]`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: List[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference: …`

      A skill installed from the Skills API.

      - `description: str`

        The installed skill description.

      - `name: str`

        The installed skill name.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: str`

        The concrete skill version installed for this session.

    - `class HostedSkillResourceInline: …`

      A skill installed from an inline ZIP archive.

      - `description: str`

        The installed skill description.

      - `name: str`

        The installed skill name.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: Literal["pending", "connected", "disconnected", 2 more]`

    The current environment connection status.

    - `"pending"`

    - `"connected"`

    - `"disconnected"`

    - `"expired"`

    - `"failed"`

  - `type: Literal["openai_hosted", "self_hosted"]`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_info = client.beta.agents.environments.retrieve(
    "environment_id",
)
print(environment_info.id)
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

- `class EnvironmentInfo: …`

  Safe metadata for a first-class execution environment.

  - `id: str`

    The ID of the environment.

  - `files: List[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileID: …`

      A file copied from the OpenAI Files API.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded file size in bytes.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class HostedEnvironmentFileResourceInline: …`

      A file supplied inline when the session was created.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded file size in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: Literal["agent.environment"]`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: List[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference: …`

      A skill installed from the Skills API.

      - `description: str`

        The installed skill description.

      - `name: str`

        The installed skill name.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: str`

        The concrete skill version installed for this session.

    - `class HostedSkillResourceInline: …`

      A skill installed from an inline ZIP archive.

      - `description: str`

        The installed skill description.

      - `name: str`

        The installed skill name.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: Literal["pending", "connected", "disconnected", 2 more]`

    The current environment connection status.

    - `"pending"`

    - `"connected"`

    - `"disconnected"`

    - `"expired"`

    - `"failed"`

  - `type: Literal["openai_hosted", "self_hosted"]`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

# Files

## Create an agent environment file

`beta.agents.environments.files.create(strenvironment_id, FileCreateParams**kwargs)  -> EnvironmentFile`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environment_id: str`

- `file_id: Optional[str]`

  The ID of the uploaded file.

- `path: Optional[str]`

  The absolute destination path inside `/workspace`.

- `type: Optional[Literal["file_id"]]`

  The type of the object. Always `file_id`.

  - `"file_id"`

### Returns

- `class EnvironmentFile: …`

  A live file in an execution environment.

  - `environment_id: str`

    The ID of the environment containing this file.

  - `object: Literal["agent.environment.file"]`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: str`

    The absolute file path inside the environment's workspace.

  - `size_bytes: int`

    The file size in bytes.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_file = client.beta.agents.environments.files.create(
    environment_id="environment_id",
)
print(environment_file.environment_id)
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

`beta.agents.environments.files.list(strenvironment_id, FileListParams**kwargs)  -> SyncTokenPage[EnvironmentFile]`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environment_id: str`

- `limit: Optional[int]`

  The maximum number of files to return, between 1 and 100.

- `order: Optional[Literal["asc", "desc"]]`

  Sort by case-sensitive path components. Defaults to descending.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

- `page: Optional[str]`

  The opaque token from the previous page. Keep the same path, order, and limit.

- `path: Optional[str]`

  Restrict the listing to this absolute workspace directory.

### Returns

- `class EnvironmentFile: …`

  A live file in an execution environment.

  - `environment_id: str`

    The ID of the environment containing this file.

  - `object: Literal["agent.environment.file"]`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: str`

    The absolute file path inside the environment's workspace.

  - `size_bytes: int`

    The file size in bytes.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.environments.files.list(
    environment_id="environment_id",
)
page = page.data[0]
print(page.environment_id)
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

- `class EnvironmentFile: …`

  A live file in an execution environment.

  - `environment_id: str`

    The ID of the environment containing this file.

  - `object: Literal["agent.environment.file"]`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: str`

    The absolute file path inside the environment's workspace.

  - `size_bytes: int`

    The file size in bytes.

# Templates

## Create an agent environment template

`beta.agents.environments.templates.create(TemplateCreateParams**kwargs)  -> EnvironmentTemplate`

**post** `/agents/environments/templates`

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `capability_directories: Optional[Sequence[str]]`

  Directories that contain capabilities exposed to the agent. Defaults to an empty list.

- `desktop: Optional[Desktop]`

  Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

  - `enabled: bool`

    Whether to provision the desktop and its browser proxy.

- `env: Optional[Dict[str, str]]`

  Environment variables made available to the agent.

- `files: Optional[Iterable[HostedEnvironmentFileParam]]`

  Files available before the agent starts. Defaults to an empty list.

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

  An optional human-readable display name for the template.

- `network: Optional[Network]`

  Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

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

  Packages to install in the environment. Defaults to empty package lists.

  - `npm: Optional[Sequence[str]]`

    npm packages to install globally. Defaults to an empty list.

  - `python: Optional[Sequence[str]]`

    Python packages to install. Defaults to an empty list.

  - `system: Optional[Sequence[str]]`

    System packages to install. Defaults to an empty list.

- `plugins: Optional[Iterable[HostedPluginParam]]`

  Plugins provided as inline ZIP archives. Defaults to an empty list.

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

  Ordered, confidential setup commands. Command bodies are never returned.

  - `command: str`

    The shell command to execute.

  - `cwd: Optional[str]`

    The absolute working directory. Defaults to `/workspace`.

- `skills: Optional[Iterable[HostedSkillParam]]`

  Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

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

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_template = client.beta.agents.environments.templates.create()
print(environment_template.id)
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

`beta.agents.environments.templates.delete(strenvironment_template_id)  -> EnvironmentTemplateDeleted`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environment_template_id: str`

### Returns

- `class EnvironmentTemplateDeleted: …`

  A deleted reusable environment template.

  - `id: str`

    The ID of the deleted environment template.

  - `deleted: bool`

    Whether the environment template was deleted. Always `true`.

  - `object: Literal["agent.environment.template.deleted"]`

    The object type. Always `agent.environment.template.deleted`.

    - `"agent.environment.template.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_template_deleted = client.beta.agents.environments.templates.delete(
    "environment_template_id",
)
print(environment_template_deleted.id)
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

`beta.agents.environments.templates.list(TemplateListParams**kwargs)  -> SyncCursorPage[EnvironmentTemplate]`

**get** `/agents/environments/templates`

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.environments.templates.list()
page = page.data[0]
print(page.id)
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

`beta.agents.environments.templates.retrieve(strenvironment_template_id)  -> EnvironmentTemplate`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environment_template_id: str`

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_template = client.beta.agents.environments.templates.retrieve(
    "environment_template_id",
)
print(environment_template.id)
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

`beta.agents.environments.templates.update(strenvironment_template_id, TemplateUpdateParams**kwargs)  -> EnvironmentTemplate`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

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

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_template = client.beta.agents.environments.templates.update(
    environment_template_id="environment_template_id",
)
print(environment_template.id)
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

### Environment Template Deleted

- `class EnvironmentTemplateDeleted: …`

  A deleted reusable environment template.

  - `id: str`

    The ID of the deleted environment template.

  - `deleted: bool`

    Whether the environment template was deleted. Always `true`.

  - `object: Literal["agent.environment.template.deleted"]`

    The object type. Always `agent.environment.template.deleted`.

    - `"agent.environment.template.deleted"`
