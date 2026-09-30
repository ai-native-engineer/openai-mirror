<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/list/ -->

## List agent session artifacts

`beta.agents.sessions.artifacts.list(session_id, **kwargs) -> CursorPage<SessionArtifact>`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

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

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.artifacts.list("session_id")

puts(page)

  "data": [
      "environment_id": "environment_id",
      "object": "agent.session.artifact",
      "path": "path",
      "session_id": "session_id",
      "size_bytes": 0,
      "turn_id": "turn_id"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
