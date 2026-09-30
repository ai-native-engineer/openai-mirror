<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/ -->

# Artifacts

## Retrieve agent session artifact content

`beta.agents.sessions.artifacts.content(artifact_id, **kwargs) -> StringIO`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `artifact_id: String`

### Returns

- `StringIO`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.beta.agents.sessions.artifacts.content("artifact_id", session_id: "session_id")

puts(response)
```

## Delete an agent session artifact

`beta.agents.sessions.artifacts.delete(artifact_id, **kwargs) -> SessionArtifactDeleted`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `artifact_id: String`

### Returns

- `class SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: String`

    The ID of the deleted session artifact.

  - `deleted: bool`

    Whether the session artifact was deleted. Always `true`.

  - `object: :"agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `:"agent.session.artifact.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

session_artifact_deleted = openai.beta.agents.sessions.artifacts.delete("artifact_id", session_id: "session_id")

puts(session_artifact_deleted)
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

`beta.agents.sessions.artifacts.list(session_id, **kwargs) -> CursorPage<SessionArtifact>`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `after: String`

  Return artifacts after this immutable artifact ID.

- `environment_id: String`

  Restrict the listing to artifacts produced by this environment.

- `limit: Integer`

  The maximum number of artifacts to return, between 1 and 100.

- `order: :asc | :desc`

  Sort by creation time and ID. Defaults to descending.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: String`

    The immutable artifact ID.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: String`

    The ID of the environment that produced the artifact.

  - `object: :"agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `:"agent.session.artifact"`

  - `path: String`

    The original absolute file path in the execution environment.

  - `session_id: String`

    The ID of the session that owns the artifact.

  - `size_bytes: Integer`

    The immutable artifact size in bytes.

  - `turn_id: String`

    The ID of the completed turn that published the artifact.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.artifacts.list("session_id")

puts(page)
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

`beta.agents.sessions.artifacts.retrieve(artifact_id, **kwargs) -> SessionArtifact`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `artifact_id: String`

### Returns

- `class SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: String`

    The immutable artifact ID.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: String`

    The ID of the environment that produced the artifact.

  - `object: :"agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `:"agent.session.artifact"`

  - `path: String`

    The original absolute file path in the execution environment.

  - `session_id: String`

    The ID of the session that owns the artifact.

  - `size_bytes: Integer`

    The immutable artifact size in bytes.

  - `turn_id: String`

    The ID of the completed turn that published the artifact.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

session_artifact = openai.beta.agents.sessions.artifacts.retrieve("artifact_id", session_id: "session_id")

puts(session_artifact)
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

- `class SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: String`

    The immutable artifact ID.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: String`

    The ID of the environment that produced the artifact.

  - `object: :"agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `:"agent.session.artifact"`

  - `path: String`

    The original absolute file path in the execution environment.

  - `session_id: String`

    The ID of the session that owns the artifact.

  - `size_bytes: Integer`

    The immutable artifact size in bytes.

  - `turn_id: String`

    The ID of the completed turn that published the artifact.

### Session Artifact Deleted

- `class SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: String`

    The ID of the deleted session artifact.

  - `deleted: bool`

    Whether the session artifact was deleted. Always `true`.

  - `object: :"agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `:"agent.session.artifact.deleted"`
