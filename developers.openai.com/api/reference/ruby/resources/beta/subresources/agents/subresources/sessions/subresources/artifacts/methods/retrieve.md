<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/retrieve/ -->

## Retrieve an agent session artifact

`beta.agents.sessions.artifacts.retrieve(artifact_id, **kwargs) -> SessionArtifact`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `session_id: String`

- `artifact_id: String`

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

session_artifact = openai.beta.agents.sessions.artifacts.retrieve("artifact_id", session_id: "session_id")

puts(session_artifact)

  "environment_id": "environment_id",
  "object": "agent.session.artifact",
  "path": "path",
  "session_id": "session_id",
  "size_bytes": 0,
  "turn_id": "turn_id"
