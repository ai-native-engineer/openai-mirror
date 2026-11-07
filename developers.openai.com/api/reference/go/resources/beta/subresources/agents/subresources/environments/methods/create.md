<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/environments/methods/create/ -->

## Create an agent environment

`client.Beta.Agents.Environments.New(ctx, params) (*EnvironmentInfo, error)`

**post** `/agents/environments`

Creates an OpenAI-hosted environment before creating a session. Requires access to the prewarming beta.

- `params BetaAgentEnvironmentNewParams`

  - `Environment param.Field[BetaAgentEnvironmentNewParamsEnvironment]`

    Body param: The required hosting type and its configuration.

    - `Type OpenAIHosted`

      The type of the object. Always `openai_hosted`.

      - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

    - `CapabilityDirectories []string`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

      `minItems: 0`, `maxItems: 16384`

    - `Desktop BetaAgentEnvironmentNewParamsEnvironmentDesktop`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `Enabled bool`

        Whether to provision the desktop and its browser proxy.

    - `Env map[string, string]`

      Environment variables made available to the agent.

    - `EnvironmentTemplateID string`

      A reusable hosted template applied before inline configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

      `minLength: 0`, `maxLength: 64`

    - `Files []HostedEnvironmentFileParamUnionResp`

      Files available before the agent starts. Defaults to an empty list.

      `minItems: 0`, `maxItems: 50`

      - `HostedEnvironmentFileParamFileIDResp`

        - `FileID string`

          The ID of the uploaded file.

          `minLength: 1`, `maxLength: 256`

        - `Path string`

          The absolute destination path inside `/workspace`.

          `minLength: 1`, `maxLength: 4096`

        - `Type FileID`

          The type of the object. Always `file_id`.

          - `const FileIDFileID FileID = "file_id"`

      - `HostedEnvironmentFileParamInlineResp`

        - `Data string`

          The standard-base64-encoded file contents.

          `minLength: 0`, `maxLength: 6990508`

        - `Path string`

          The absolute destination path inside `/workspace`.

          `minLength: 1`, `maxLength: 4096`

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

    - `Network BetaAgentEnvironmentNewParamsEnvironmentNetwork`

      Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

      - `Access string`

        The environment's network access mode.

        - `const BetaAgentEnvironmentNewParamsEnvironmentNetworkAccessEnabled BetaAgentEnvironmentNewParamsEnvironmentNetworkAccess = "enabled"`

          Allows unrestricted network access.

        - `const BetaAgentEnvironmentNewParamsEnvironmentNetworkAccessDisabled BetaAgentEnvironmentNewParamsEnvironmentNetworkAccess = "disabled"`

          Disables network access.

        - `const BetaAgentEnvironmentNewParamsEnvironmentNetworkAccessRestricted BetaAgentEnvironmentNewParamsEnvironmentNetworkAccess = "restricted"`

          Applies the configured domain restrictions.

      - `AllowedDomains []string`

        Domains the environment may access when network access is restricted.

        `minItems: 0`, `maxItems: 16384`

      - `BlockedDomains []string`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

        `minItems: 0`, `maxItems: 100`

    - `Packages BetaAgentEnvironmentNewParamsEnvironmentPackages`

      Packages to install in the environment. Defaults to empty package lists.

      - `Npm []string`

        npm packages to install globally. Defaults to an empty list.

        `minItems: 0`, `maxItems: 16384`

      - `Python []string`

        Python packages to install. Defaults to an empty list.

        `minItems: 0`, `maxItems: 16384`

      - `System []string`

        System packages to install. Defaults to an empty list.

        `minItems: 0`, `maxItems: 16384`

    - `Plugins []HostedPluginParamResp`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      `minItems: 0`, `maxItems: 32`

      - `Description string`

        The plugin description declared in `.codex-plugin/plugin.json`.

        `minLength: 0`, `maxLength: 1048576`

      - `Name string`

        The plugin name declared in `.codex-plugin/plugin.json`.

        `minLength: 1`, `maxLength: 64`

      - `Source InlineCapabilitySourceParamResp`

        Provides ZIP bytes encoded with standard base64.

        - `Data string`

          Standard-base64 encoded ZIP archive bytes.

          `minLength: 1`, `maxLength: 70254592`

        - `MediaType ApplicationZip`

          The archive media type, always `application/zip`.

          - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

        - `Type Base64`

          The type of the object. Always `base64`.

          - `const Base64Base64 Base64 = "base64"`

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

    - `SetupCommands []SetupCommandParamResp`

      Ordered, confidential setup commands. Command bodies are never returned.

      `minItems: 0`, `maxItems: 16`

      - `Command string`

        The shell command to execute.

        `minLength: 0`, `maxLength: 65536`

      - `Cwd string`

        The absolute working directory. Defaults to `/workspace`.

        `minLength: 0`, `maxLength: 4096`

    - `Skills []HostedSkillParamUnionResp`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      `minItems: 0`, `maxItems: 200`

      - `HostedSkillParamSkillReferenceResp`

        - `SkillID string`

          The ID of the skill created through `/v1/skills`.

          `minLength: 1`, `maxLength: 64`

        - `Type SkillReference`

          The type of the object. Always `skill_reference`.

          - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

        - `Version string`

          The skill version, a positive integer or `latest`; omission selects the default.

          `minLength: 0`, `maxLength: 1048576`

      - `HostedSkillParamInlineResp`

        - `Description string`

          The skill description declared in `SKILL.md`.

          `minLength: 0`, `maxLength: 1048576`

        - `Name string`

          The skill name declared in `SKILL.md`.

          `minLength: 1`, `maxLength: 64`

        - `Source InlineCapabilitySourceParamResp`

          Provides ZIP bytes encoded with standard base64.

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

  - `VaultIDs param.Field[[]string]`

    Body param: The IDs of up to 10 vaults made available to an OpenAI-hosted environment.

    `minItems: 0`, `maxItems: 10`

  - `IdempotencyKey param.Field[string]`

    Header param: Deduplicates creation for 24 hours within the authenticated organization, project, and creator. Retry the same JSON parameters with the same key to retrieve the original environment in its current state. Different parameters or an incomplete hosted creation return 409. Deleted environments are not recreated. After retention expires, the key may create a new environment. Without this header, each request creates a new environment.

    `minLength: 1`, `maxLength: 256`

- `type EnvironmentInfo struct{…}`

  Safe metadata for a first-class execution environment.

  - `ID string`

    The ID of the environment.

    `minLength: 0`

  - `Files []HostedEnvironmentFileUnion`

    Files installed in the environment, without their contents.

    `minItems: 0`, `maxItems: 2000`

    - `type HostedEnvironmentFileID struct{…}`

      A file copied from the OpenAI Files API.

      - `ID string`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `FileID string`

        The ID of the uploaded file.

        `minLength: 0`

      - `Path string`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `SizeBytes int64`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type HostedEnvironmentFileInline struct{…}`

      A file supplied inline when the session was created.

      - `ID string`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `Path string`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `SizeBytes int64`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Object AgentEnvironment`

    The object type. Always `agent.environment`.

    - `const AgentEnvironmentAgentEnvironment AgentEnvironment = "agent.environment"`

  - `Plugins []HostedPlugin`

    Plugins installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `Description string`

      The installed plugin description.

      `minLength: 0`

    - `Name string`

      The installed plugin name.

      `minLength: 0`

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []HostedSkillUnion`

    Skills installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `type HostedSkillReference struct{…}`

      A skill installed from the Skills API.

      - `Description string`

        The installed skill description.

        `minLength: 0`

      - `Name string`

        The installed skill name.

        `minLength: 0`

      - `SkillID string`

        The referenced skill ID.

        `minLength: 0`

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The concrete skill version installed for this session.

        `minLength: 0`

    - `type HostedSkillInline struct{…}`

      A skill installed from an inline ZIP archive.

      - `Description string`

        The installed skill description.

        `minLength: 0`

      - `Name string`

        The installed skill name.

        `minLength: 0`

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Status EnvironmentInfoStatus`

    The current environment connection status.

    - `const EnvironmentInfoStatusPending EnvironmentInfoStatus = "pending"`

    - `const EnvironmentInfoStatusReady EnvironmentInfoStatus = "ready"`

      Provisioning succeeded and the environment is available for attachment or use.

    - `const EnvironmentInfoStatusConnected EnvironmentInfoStatus = "connected"`

    - `const EnvironmentInfoStatusDisconnected EnvironmentInfoStatus = "disconnected"`

    - `const EnvironmentInfoStatusSuspended EnvironmentInfoStatus = "suspended"`

      The sandbox is stopped and can be resumed from its private checkpoint.

    - `const EnvironmentInfoStatusExpired EnvironmentInfoStatus = "expired"`

    - `const EnvironmentInfoStatusFailed EnvironmentInfoStatus = "failed"`

  - `Type EnvironmentInfoType`

    Whether the environment is hosted by OpenAI or by the application.

    - `const EnvironmentInfoTypeOpenAIHosted EnvironmentInfoType = "openai_hosted"`

    - `const EnvironmentInfoTypeSelfHosted EnvironmentInfoType = "self_hosted"`

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  environmentInfo, err := client.Beta.Agents.Environments.New(context.TODO(), openai.BetaAgentEnvironmentNewParams{
    Environment: openai.BetaAgentEnvironmentNewParamsEnvironment{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", environmentInfo.ID)

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
