<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/environments/methods/list/ -->

## List agent environments

`client.Beta.Agents.Environments.List(ctx, query) (*CursorPage[EnvironmentInfo], error)`

**get** `/agents/environments`

Lists OpenAI-hosted environments owned by the authenticated principal. Requires access to the prewarming beta.

- `query BetaAgentEnvironmentListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

    `minLength: 0`, `maxLength: 1048576`

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `Order param.Field[BetaAgentEnvironmentListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentEnvironmentListParamsOrderAsc BetaAgentEnvironmentListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentEnvironmentListParamsOrderDesc BetaAgentEnvironmentListParamsOrder = "desc"`

      Returns resources in descending order.

  - `Type param.Field[BetaAgentEnvironmentListParamsType]`

    The hosting type to list. Defaults to `openai_hosted`.

    - `const BetaAgentEnvironmentListParamsTypeOpenAIHosted BetaAgentEnvironmentListParamsType = "openai_hosted"`

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
  page, err := client.Beta.Agents.Environments.List(context.TODO(), openai.BetaAgentEnvironmentListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
