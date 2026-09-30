<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/retrieve/ -->

## Retrieve a session subagent

`client.Beta.Agents.Sessions.Subagents.Get(ctx, sessionID, subagentID) (*Subagent, error)`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

- `sessionID string`

- `subagentID string`

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
  subagent, err := client.Beta.Agents.Sessions.Subagents.Get(
    context.TODO(),
    "session_id",
    "subagent_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", subagent.ID)

  "closed_at": 0,
  "instructions": [
      "text": "text",
      "type": "output_text"
  "object": "agent.session.subagent",
  "opened_at": 0,
  "parent_agent_id": "parent_agent_id",
  "session_id": "session_id",
  "status": "active"
