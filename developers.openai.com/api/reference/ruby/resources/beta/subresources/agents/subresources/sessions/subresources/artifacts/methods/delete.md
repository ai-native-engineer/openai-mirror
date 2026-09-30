<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/delete/ -->

## Delete an agent session artifact

`beta.agents.sessions.artifacts.delete(artifact_id, **kwargs) -> SessionArtifactDeleted`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `session_id: String`

- `artifact_id: String`

- `class SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: String`

    The ID of the deleted session artifact.

  - `deleted: bool`

    Whether the session artifact was deleted. Always `true`.

  - `object: :"agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `:"agent.session.artifact.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

session_artifact_deleted = openai.beta.agents.sessions.artifacts.delete("artifact_id", session_id: "session_id")

puts(session_artifact_deleted)

  "deleted": true,
  "object": "agent.session.artifact.deleted"
