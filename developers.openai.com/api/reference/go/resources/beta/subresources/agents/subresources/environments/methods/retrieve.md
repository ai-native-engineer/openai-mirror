<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/environments/methods/retrieve/ -->

## Retrieve an agent environment

`client.Beta.Agents.Environments.Get(ctx, environmentID) (*EnvironmentInfo, error)`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

- `environmentID string`

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
  environmentInfo, err := client.Beta.Agents.Environments.Get(context.TODO(), "environment_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", environmentInfo.ID)

  "files": [
      "file_id": "file_id",
      "path": "path",
      "size_bytes": 0,
      "type": "file_id"
  "object": "agent.environment",
  "plugins": [
      "description": "description",
      "type": "inline"
  "skills": [
      "description": "description",
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
  "status": "pending",
  "type": "openai_hosted"
