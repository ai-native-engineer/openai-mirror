<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/list/ -->

## List session subagents

`client.Beta.Agents.Sessions.Subagents.List(ctx, sessionID, query) (*CursorPage[Subagent], error)`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

- `sessionID string`

- `query BetaAgentSessionSubagentListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentSessionSubagentListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionSubagentListParamsOrderAsc BetaAgentSessionSubagentListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionSubagentListParamsOrderDesc BetaAgentSessionSubagentListParamsOrder = "desc"`

      Returns resources in descending order.

- `type Subagent struct{…}`

  A subagent created within a session.

  - `ID string`

    The ID of the subagent.

  - `ClosedAt int64`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `Instructions []AgentContentUnion`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `type OutputText struct{…}`

      A text content part produced by the agent.

      - `Text string`

        The text produced by the agent.

      - `Type OutputText`

        The content type. Always `output_text`.

        - `const OutputTextOutputText OutputText = "output_text"`

    - `type AgentContentEncryptedContent struct{…}`

      Encrypted content exchanged between agents.

      - `EncryptedContent string`

        The encrypted content payload.

      - `Type EncryptedContent`

        The content type. Always `encrypted_content`.

        - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

  - `Name string`

    The runner-assigned nickname, or null when unavailable.

  - `Object SubagentObject`

    The object type. Always `agent.session.subagent`.

    - `const SubagentObjectAgentSessionSubagent SubagentObject = "agent.session.subagent"`

  - `OpenedAt int64`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `ParentAgentID string`

    The ID of the agent that created this subagent.

  - `SessionID string`

    The ID of the session that owns the subagent.

  - `Status SubagentStatus`

    The current status of the subagent.

    - `const SubagentStatusActive SubagentStatus = "active"`

      The subagent remains available, including while idle between turns.

    - `const SubagentStatusClosed SubagentStatus = "closed"`

      The subagent is closed.

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
  page, err := client.Beta.Agents.Sessions.Subagents.List(
    context.TODO(),
    "session_id",
    openai.BetaAgentSessionSubagentListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
      "closed_at": 0,
      "instructions": [
          "text": "text",
          "type": "output_text"
      "object": "agent.session.subagent",
      "opened_at": 0,
      "parent_agent_id": "parent_agent_id",
      "session_id": "session_id",
      "status": "active"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
