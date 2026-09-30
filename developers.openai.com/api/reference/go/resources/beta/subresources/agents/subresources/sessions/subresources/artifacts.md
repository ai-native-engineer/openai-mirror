<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/ -->

# Artifacts

## Retrieve agent session artifact content

`client.Beta.Agents.Sessions.Artifacts.Content(ctx, sessionID, artifactID) (*Response, error)`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `sessionID string`

- `artifactID string`

### Returns

- `type BetaAgentSessionArtifactContentResponse interface{…}`

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
  response, err := client.Beta.Agents.Sessions.Artifacts.Content(
    context.TODO(),
    "session_id",
    "artifact_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response)
}
```

## Delete an agent session artifact

`client.Beta.Agents.Sessions.Artifacts.Delete(ctx, sessionID, artifactID) (*SessionArtifactDeleted, error)`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `sessionID string`

- `artifactID string`

### Returns

- `type SessionArtifactDeleted struct{…}`

  Confirmation that an immutable session artifact was deleted.

  - `ID string`

    The ID of the deleted session artifact.

  - `Deleted bool`

    Whether the session artifact was deleted. Always `true`.

  - `Object AgentSessionArtifactDeleted`

    The object type. Always `agent.session.artifact.deleted`.

    - `const AgentSessionArtifactDeletedAgentSessionArtifactDeleted AgentSessionArtifactDeleted = "agent.session.artifact.deleted"`

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
  sessionArtifactDeleted, err := client.Beta.Agents.Sessions.Artifacts.Delete(
    context.TODO(),
    "session_id",
    "artifact_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", sessionArtifactDeleted.ID)
}
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.session.artifact.deleted"
}
```

## List agent session artifacts

`client.Beta.Agents.Sessions.Artifacts.List(ctx, sessionID, query) (*CursorPage[SessionArtifact], error)`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `sessionID string`

- `query BetaAgentSessionArtifactListParams`

  - `After param.Field[string]`

    Return artifacts after this immutable artifact ID.

  - `EnvironmentID param.Field[string]`

    Restrict the listing to artifacts produced by this environment.

  - `Limit param.Field[int64]`

    The maximum number of artifacts to return, between 1 and 100.

  - `Order param.Field[BetaAgentSessionArtifactListParamsOrder]`

    Sort by creation time and ID. Defaults to descending.

    - `const BetaAgentSessionArtifactListParamsOrderAsc BetaAgentSessionArtifactListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionArtifactListParamsOrderDesc BetaAgentSessionArtifactListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type SessionArtifact struct{…}`

  An immutable file published by a completed hosted session turn.

  - `ID string`

    The immutable artifact ID.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the artifact was published.

  - `EnvironmentID string`

    The ID of the environment that produced the artifact.

  - `Object AgentSessionArtifact`

    The object type. Always `agent.session.artifact`.

    - `const AgentSessionArtifactAgentSessionArtifact AgentSessionArtifact = "agent.session.artifact"`

  - `Path string`

    The original absolute file path in the execution environment.

  - `SessionID string`

    The ID of the session that owns the artifact.

  - `SizeBytes int64`

    The immutable artifact size in bytes.

  - `TurnID string`

    The ID of the completed turn that published the artifact.

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
  page, err := client.Beta.Agents.Sessions.Artifacts.List(
    context.TODO(),
    "session_id",
    openai.BetaAgentSessionArtifactListParams{

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
      "id": "id",
      "created_at": 0,
      "environment_id": "environment_id",
      "object": "agent.session.artifact",
      "path": "path",
      "session_id": "session_id",
      "size_bytes": 0,
      "turn_id": "turn_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent session artifact

`client.Beta.Agents.Sessions.Artifacts.Get(ctx, sessionID, artifactID) (*SessionArtifact, error)`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `sessionID string`

- `artifactID string`

### Returns

- `type SessionArtifact struct{…}`

  An immutable file published by a completed hosted session turn.

  - `ID string`

    The immutable artifact ID.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the artifact was published.

  - `EnvironmentID string`

    The ID of the environment that produced the artifact.

  - `Object AgentSessionArtifact`

    The object type. Always `agent.session.artifact`.

    - `const AgentSessionArtifactAgentSessionArtifact AgentSessionArtifact = "agent.session.artifact"`

  - `Path string`

    The original absolute file path in the execution environment.

  - `SessionID string`

    The ID of the session that owns the artifact.

  - `SizeBytes int64`

    The immutable artifact size in bytes.

  - `TurnID string`

    The ID of the completed turn that published the artifact.

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
  sessionArtifact, err := client.Beta.Agents.Sessions.Artifacts.Get(
    context.TODO(),
    "session_id",
    "artifact_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", sessionArtifact.ID)
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "environment_id": "environment_id",
  "object": "agent.session.artifact",
  "path": "path",
  "session_id": "session_id",
  "size_bytes": 0,
  "turn_id": "turn_id"
}
```

## Domain Types

### Session Artifact

- `type SessionArtifact struct{…}`

  An immutable file published by a completed hosted session turn.

  - `ID string`

    The immutable artifact ID.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the artifact was published.

  - `EnvironmentID string`

    The ID of the environment that produced the artifact.

  - `Object AgentSessionArtifact`

    The object type. Always `agent.session.artifact`.

    - `const AgentSessionArtifactAgentSessionArtifact AgentSessionArtifact = "agent.session.artifact"`

  - `Path string`

    The original absolute file path in the execution environment.

  - `SessionID string`

    The ID of the session that owns the artifact.

  - `SizeBytes int64`

    The immutable artifact size in bytes.

  - `TurnID string`

    The ID of the completed turn that published the artifact.

### Session Artifact Deleted

- `type SessionArtifactDeleted struct{…}`

  Confirmation that an immutable session artifact was deleted.

  - `ID string`

    The ID of the deleted session artifact.

  - `Deleted bool`

    Whether the session artifact was deleted. Always `true`.

  - `Object AgentSessionArtifactDeleted`

    The object type. Always `agent.session.artifact.deleted`.

    - `const AgentSessionArtifactDeletedAgentSessionArtifactDeleted AgentSessionArtifactDeleted = "agent.session.artifact.deleted"`
