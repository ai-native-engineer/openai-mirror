<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/environments/ -->

# Environments

## Retrieve an agent environment

`client.Beta.Agents.Environments.Get(ctx, environmentID) (*EnvironmentInfo, error)`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

### Parameters

- `environmentID string`

### Returns

- `type EnvironmentInfo struct{…}`

  Safe metadata for a first-class execution environment.

  - `ID string`

    The ID of the environment.

  - `Files []HostedEnvironmentFileUnion`

    Files installed in the environment, without their contents.

    - `type HostedEnvironmentFileID struct{…}`

      A file copied from the OpenAI Files API.

      - `ID string`

        The session-scoped ID of the file in the execution environment.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded file size in bytes.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type HostedEnvironmentFileInline struct{…}`

      A file supplied inline when the session was created.

      - `ID string`

        The session-scoped ID of the file in the execution environment.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded file size in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Object AgentEnvironment`

    The object type. Always `agent.environment`.

    - `const AgentEnvironmentAgentEnvironment AgentEnvironment = "agent.environment"`

  - `Plugins []HostedPlugin`

    Plugins installed in the environment, without their archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []HostedSkillUnion`

    Skills installed in the environment, without their archive contents.

    - `type HostedSkillReference struct{…}`

      A skill installed from the Skills API.

      - `Description string`

        The installed skill description.

      - `Name string`

        The installed skill name.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The concrete skill version installed for this session.

    - `type HostedSkillInline struct{…}`

      A skill installed from an inline ZIP archive.

      - `Description string`

        The installed skill description.

      - `Name string`

        The installed skill name.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Status EnvironmentInfoStatus`

    The current environment connection status.

    - `const EnvironmentInfoStatusPending EnvironmentInfoStatus = "pending"`

    - `const EnvironmentInfoStatusConnected EnvironmentInfoStatus = "connected"`

    - `const EnvironmentInfoStatusDisconnected EnvironmentInfoStatus = "disconnected"`

    - `const EnvironmentInfoStatusExpired EnvironmentInfoStatus = "expired"`

    - `const EnvironmentInfoStatusFailed EnvironmentInfoStatus = "failed"`

  - `Type EnvironmentInfoType`

    Whether the environment is hosted by OpenAI or by the application.

    - `const EnvironmentInfoTypeOpenAIHosted EnvironmentInfoType = "openai_hosted"`

    - `const EnvironmentInfoTypeSelfHosted EnvironmentInfoType = "self_hosted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentInfo, err := client.Beta.Agents.Environments.Get(context.TODO(), "environment_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentInfo.ID)
}
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

- `type EnvironmentInfo struct{…}`

  Safe metadata for a first-class execution environment.

  - `ID string`

    The ID of the environment.

  - `Files []HostedEnvironmentFileUnion`

    Files installed in the environment, without their contents.

    - `type HostedEnvironmentFileID struct{…}`

      A file copied from the OpenAI Files API.

      - `ID string`

        The session-scoped ID of the file in the execution environment.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded file size in bytes.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type HostedEnvironmentFileInline struct{…}`

      A file supplied inline when the session was created.

      - `ID string`

        The session-scoped ID of the file in the execution environment.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded file size in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Object AgentEnvironment`

    The object type. Always `agent.environment`.

    - `const AgentEnvironmentAgentEnvironment AgentEnvironment = "agent.environment"`

  - `Plugins []HostedPlugin`

    Plugins installed in the environment, without their archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []HostedSkillUnion`

    Skills installed in the environment, without their archive contents.

    - `type HostedSkillReference struct{…}`

      A skill installed from the Skills API.

      - `Description string`

        The installed skill description.

      - `Name string`

        The installed skill name.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The concrete skill version installed for this session.

    - `type HostedSkillInline struct{…}`

      A skill installed from an inline ZIP archive.

      - `Description string`

        The installed skill description.

      - `Name string`

        The installed skill name.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Status EnvironmentInfoStatus`

    The current environment connection status.

    - `const EnvironmentInfoStatusPending EnvironmentInfoStatus = "pending"`

    - `const EnvironmentInfoStatusConnected EnvironmentInfoStatus = "connected"`

    - `const EnvironmentInfoStatusDisconnected EnvironmentInfoStatus = "disconnected"`

    - `const EnvironmentInfoStatusExpired EnvironmentInfoStatus = "expired"`

    - `const EnvironmentInfoStatusFailed EnvironmentInfoStatus = "failed"`

  - `Type EnvironmentInfoType`

    Whether the environment is hosted by OpenAI or by the application.

    - `const EnvironmentInfoTypeOpenAIHosted EnvironmentInfoType = "openai_hosted"`

    - `const EnvironmentInfoTypeSelfHosted EnvironmentInfoType = "self_hosted"`

# Files

## Create an agent environment file

`client.Beta.Agents.Environments.Files.New(ctx, environmentID, body) (*EnvironmentFile, error)`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environmentID string`

- `body BetaAgentEnvironmentFileNewParams`

  - `FileID param.Field[string]`

    The ID of the uploaded file.

  - `Path param.Field[string]`

    The absolute destination path inside `/workspace`.

  - `Type param.Field[FileID]`

    The type of the object. Always `file_id`.

    - `const FileIDFileID FileID = "file_id"`

### Returns

- `type EnvironmentFile struct{…}`

  A live file in an execution environment.

  - `EnvironmentID string`

    The ID of the environment containing this file.

  - `Object AgentEnvironmentFile`

    The object type. Always `agent.environment.file`.

    - `const AgentEnvironmentFileAgentEnvironmentFile AgentEnvironmentFile = "agent.environment.file"`

  - `Path string`

    The absolute file path inside the environment's workspace.

  - `SizeBytes int64`

    The file size in bytes.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentFile, err := client.Beta.Agents.Environments.Files.New(
    context.TODO(),
    "environment_id",
    openai.BetaAgentEnvironmentFileNewParams{
      HostedEnvironmentFileParamUnionResp: map[string]any{},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentFile.EnvironmentID)
}
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

`client.Beta.Agents.Environments.Files.List(ctx, environmentID, query) (*TokenPage[EnvironmentFile], error)`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environmentID string`

- `query BetaAgentEnvironmentFileListParams`

  - `Limit param.Field[int64]`

    The maximum number of files to return, between 1 and 100.

  - `Order param.Field[BetaAgentEnvironmentFileListParamsOrder]`

    Sort by case-sensitive path components. Defaults to descending.

    - `const BetaAgentEnvironmentFileListParamsOrderAsc BetaAgentEnvironmentFileListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentEnvironmentFileListParamsOrderDesc BetaAgentEnvironmentFileListParamsOrder = "desc"`

      Returns resources in descending order.

  - `Page param.Field[string]`

    The opaque token from the previous page. Keep the same path, order, and limit.

  - `Path param.Field[string]`

    Restrict the listing to this absolute workspace directory.

### Returns

- `type EnvironmentFile struct{…}`

  A live file in an execution environment.

  - `EnvironmentID string`

    The ID of the environment containing this file.

  - `Object AgentEnvironmentFile`

    The object type. Always `agent.environment.file`.

    - `const AgentEnvironmentFileAgentEnvironmentFile AgentEnvironmentFile = "agent.environment.file"`

  - `Path string`

    The absolute file path inside the environment's workspace.

  - `SizeBytes int64`

    The file size in bytes.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Agents.Environments.Files.List(
    context.TODO(),
    "environment_id",
    openai.BetaAgentEnvironmentFileListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

- `type EnvironmentFile struct{…}`

  A live file in an execution environment.

  - `EnvironmentID string`

    The ID of the environment containing this file.

  - `Object AgentEnvironmentFile`

    The object type. Always `agent.environment.file`.

    - `const AgentEnvironmentFileAgentEnvironmentFile AgentEnvironmentFile = "agent.environment.file"`

  - `Path string`

    The absolute file path inside the environment's workspace.

  - `SizeBytes int64`

    The file size in bytes.

# Templates

## Create an agent environment template

`client.Beta.Agents.Environments.Templates.New(ctx, body) (*EnvironmentTemplate, error)`

**post** `/agents/environments/templates`

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `body BetaAgentEnvironmentTemplateNewParams`

  - `CapabilityDirectories param.Field[[]string]`

    Directories that contain capabilities exposed to the agent. Defaults to an empty list.

  - `Desktop param.Field[BetaAgentEnvironmentTemplateNewParamsDesktop]`

    Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

    - `Enabled bool`

      Whether to provision the desktop and its browser proxy.

  - `Env param.Field[map[string, string]]`

    Environment variables made available to the agent.

  - `Files param.Field[[]HostedEnvironmentFileParamUnionResp]`

    Files available before the agent starts. Defaults to an empty list.

    - `HostedEnvironmentFileParamFileIDResp`

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The absolute destination path inside `/workspace`.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `HostedEnvironmentFileParamInlineResp`

      - `Data string`

        The standard-base64-encoded file contents.

      - `Path string`

        The absolute destination path inside `/workspace`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name param.Field[string]`

    An optional human-readable display name for the template.

  - `Network param.Field[BetaAgentEnvironmentTemplateNewParamsNetwork]`

    Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

    - `Access string`

      The environment's network access mode.

      - `const BetaAgentEnvironmentTemplateNewParamsNetworkAccessEnabled BetaAgentEnvironmentTemplateNewParamsNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const BetaAgentEnvironmentTemplateNewParamsNetworkAccessDisabled BetaAgentEnvironmentTemplateNewParamsNetworkAccess = "disabled"`

        Disables network access.

      - `const BetaAgentEnvironmentTemplateNewParamsNetworkAccessRestricted BetaAgentEnvironmentTemplateNewParamsNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

    - `BlockedDomains []string`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `Packages param.Field[BetaAgentEnvironmentTemplateNewParamsPackages]`

    Packages to install in the environment. Defaults to empty package lists.

    - `Npm []string`

      npm packages to install globally. Defaults to an empty list.

    - `Python []string`

      Python packages to install. Defaults to an empty list.

    - `System []string`

      System packages to install. Defaults to an empty list.

  - `Plugins param.Field[[]HostedPluginParamResp]`

    Plugins provided as inline ZIP archives. Defaults to an empty list.

    - `Description string`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `Name string`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `Source InlineCapabilitySourceParamResp`

      Provides ZIP bytes encoded with standard base64.

      - `Data string`

        Standard-base64 encoded ZIP archive bytes.

      - `MediaType ApplicationZip`

        The archive media type, always `application/zip`.

        - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

          A ZIP archive.

      - `Type Base64`

        The type of the object. Always `base64`.

        - `const Base64Base64 Base64 = "base64"`

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `SetupCommands param.Field[[]SetupCommandParamResp]`

    Ordered, confidential setup commands. Command bodies are never returned.

    - `Command string`

      The shell command to execute.

    - `Cwd string`

      The absolute working directory. Defaults to `/workspace`.

  - `Skills param.Field[[]HostedSkillParamUnionResp]`

    Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

    - `HostedSkillParamSkillReferenceResp`

      - `SkillID string`

        The ID of the skill created through `/v1/skills`.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `HostedSkillParamInlineResp`

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Source InlineCapabilitySourceParamResp`

        Provides ZIP bytes encoded with standard base64.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

### Returns

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentTemplate, err := client.Beta.Agents.Environments.Templates.New(context.TODO(), openai.BetaAgentEnvironmentTemplateNewParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentTemplate.ID)
}
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

`client.Beta.Agents.Environments.Templates.Delete(ctx, environmentTemplateID) (*EnvironmentTemplateDeleted, error)`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID string`

### Returns

- `type EnvironmentTemplateDeleted struct{…}`

  A deleted reusable environment template.

  - `ID string`

    The ID of the deleted environment template.

  - `Deleted bool`

    Whether the environment template was deleted. Always `true`.

  - `Object AgentEnvironmentTemplateDeleted`

    The object type. Always `agent.environment.template.deleted`.

    - `const AgentEnvironmentTemplateDeletedAgentEnvironmentTemplateDeleted AgentEnvironmentTemplateDeleted = "agent.environment.template.deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentTemplateDeleted, err := client.Beta.Agents.Environments.Templates.Delete(context.TODO(), "environment_template_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentTemplateDeleted.ID)
}
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

`client.Beta.Agents.Environments.Templates.List(ctx, query) (*CursorPage[EnvironmentTemplate], error)`

**get** `/agents/environments/templates`

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `query BetaAgentEnvironmentTemplateListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentEnvironmentTemplateListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentEnvironmentTemplateListParamsOrderAsc BetaAgentEnvironmentTemplateListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentEnvironmentTemplateListParamsOrderDesc BetaAgentEnvironmentTemplateListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Agents.Environments.Templates.List(context.TODO(), openai.BetaAgentEnvironmentTemplateListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Agents.Environments.Templates.Get(ctx, environmentTemplateID) (*EnvironmentTemplate, error)`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID string`

### Returns

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentTemplate, err := client.Beta.Agents.Environments.Templates.Get(context.TODO(), "environment_template_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentTemplate.ID)
}
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

`client.Beta.Agents.Environments.Templates.Update(ctx, environmentTemplateID, body) (*EnvironmentTemplate, error)`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID string`

- `body BetaAgentEnvironmentTemplateUpdateParams`

  - `CapabilityDirectories param.Field[[]string]`

    Directories that expose capabilities to the agent.

  - `Desktop param.Field[BetaAgentEnvironmentTemplateUpdateParamsDesktop]`

    Replacement desktop configuration, or null to disable the desktop.

    - `Enabled bool`

      Whether to provision the desktop and its browser proxy.

  - `Env param.Field[map[string, string]]`

    Replacement confidential environment values.

  - `Files param.Field[[]HostedEnvironmentFileParamUnionResp]`

    Replacement file configuration materialized for each new session.

    - `HostedEnvironmentFileParamFileIDResp`

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The absolute destination path inside `/workspace`.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `HostedEnvironmentFileParamInlineResp`

      - `Data string`

        The standard-base64-encoded file contents.

      - `Path string`

        The absolute destination path inside `/workspace`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name param.Field[string]`

    A replacement human-readable display name, or `null` to clear the name.

  - `Network param.Field[BetaAgentEnvironmentTemplateUpdateParamsNetwork]`

    Network access available after setup completes. Omit to preserve the current policy, or pass `null` to reset to disabled for GA requests or enabled for beta requests.

    - `Access string`

      The environment's network access mode.

      - `const BetaAgentEnvironmentTemplateUpdateParamsNetworkAccessEnabled BetaAgentEnvironmentTemplateUpdateParamsNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const BetaAgentEnvironmentTemplateUpdateParamsNetworkAccessDisabled BetaAgentEnvironmentTemplateUpdateParamsNetworkAccess = "disabled"`

        Disables network access.

      - `const BetaAgentEnvironmentTemplateUpdateParamsNetworkAccessRestricted BetaAgentEnvironmentTemplateUpdateParamsNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

    - `BlockedDomains []string`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `Packages param.Field[BetaAgentEnvironmentTemplateUpdateParamsPackages]`

    Packages installed before the runtime network policy applies.

    - `Npm []string`

      npm packages to install globally. Defaults to an empty list.

    - `Python []string`

      Python packages to install. Defaults to an empty list.

    - `System []string`

      System packages to install. Defaults to an empty list.

  - `Plugins param.Field[[]HostedPluginParamResp]`

    Replacement plugin configuration installed for each new session.

    - `Description string`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `Name string`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `Source InlineCapabilitySourceParamResp`

      Provides ZIP bytes encoded with standard base64.

      - `Data string`

        Standard-base64 encoded ZIP archive bytes.

      - `MediaType ApplicationZip`

        The archive media type, always `application/zip`.

        - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

          A ZIP archive.

      - `Type Base64`

        The type of the object. Always `base64`.

        - `const Base64Base64 Base64 = "base64"`

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `SetupCommands param.Field[[]SetupCommandParamResp]`

    Replacement confidential setup commands, never included in returned resources.

    - `Command string`

      The shell command to execute.

    - `Cwd string`

      The absolute working directory. Defaults to `/workspace`.

  - `Skills param.Field[[]HostedSkillParamUnionResp]`

    Replacement skill configuration installed for each new session.

    - `HostedSkillParamSkillReferenceResp`

      - `SkillID string`

        The ID of the skill created through `/v1/skills`.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `HostedSkillParamInlineResp`

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Source InlineCapabilitySourceParamResp`

        Provides ZIP bytes encoded with standard base64.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

### Returns

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentTemplate, err := client.Beta.Agents.Environments.Templates.Update(
    context.TODO(),
    "environment_template_id",
    openai.BetaAgentEnvironmentTemplateUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentTemplate.ID)
}
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

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

### Environment Template Deleted

- `type EnvironmentTemplateDeleted struct{…}`

  A deleted reusable environment template.

  - `ID string`

    The ID of the deleted environment template.

  - `Deleted bool`

    Whether the environment template was deleted. Always `true`.

  - `Object AgentEnvironmentTemplateDeleted`

    The object type. Always `agent.environment.template.deleted`.

    - `const AgentEnvironmentTemplateDeletedAgentEnvironmentTemplateDeleted AgentEnvironmentTemplateDeleted = "agent.environment.template.deleted"`
