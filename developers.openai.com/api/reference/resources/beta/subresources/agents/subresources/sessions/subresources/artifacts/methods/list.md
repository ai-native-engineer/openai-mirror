<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/list/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

[Artifacts](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts)

# List agent session artifacts

GET/agents/sessions/{session\_id}/artifacts

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

session\_id: string

##### Query ParametersExpand Collapse

after: optional string or null

Return artifacts after this immutable artifact ID.

environment\_id: optional string or null

Restrict the listing to artifacts produced by this environment.

limit: optional number or null

The maximum number of artifacts to return, between 1 and 100.

minimum1

maximum100

order: optional "asc" or "desc"

Sort by creation time and ID. Defaults to descending.

"asc"

Returns resources in ascending order.

"desc"

Returns resources in descending order.

data: array of [SessionArtifact](/api/reference/resources/beta#(resource)%20beta.agents.sessions.artifacts%20%3E%20(model)%20session_artifact%20%3E%20(schema)) { id, created\_at, environment\_id, 5 more }

The resources returned in this page, in the requested sort order.

The immutable artifact ID.

The Unix timestamp, in seconds, when the artifact was published.

environment\_id: string

The ID of the environment that produced the artifact.

object: "agent.session.artifact"

The object type. Always `agent.session.artifact`.

path: string

The original absolute file path in the execution environment.

session\_id: string

The ID of the session that owns the artifact.

size\_bytes: number

The immutable artifact size in bytes.

minimum0

turn\_id: string

The ID of the completed turn that published the artifact.

first\_id: string or null

The ID of the first resource in `data`, or `null` if the page is empty.

has\_more: boolean

Whether there are more resources to retrieve after this page.

last\_id: string or null

The ID of the last resource in `data`, or `null` if the page is empty. Pass this as `after` with the same order and filters.

object: "list"

The object type, which is always `list`.

### List agent session artifacts

curl https://api.openai.com/v1/agents/sessions/$SESSION_ID/artifacts \

  "data": [
      "created_at": 0,
      "environment_id": "environment_id",
      "object": "agent.session.artifact",
      "path": "path",
      "session_id": "session_id",
      "size_bytes": 0,
      "turn_id": "turn_id"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

  "data": [
      "created_at": 0,
      "environment_id": "environment_id",
      "object": "agent.session.artifact",
      "path": "path",
      "session_id": "session_id",
      "size_bytes": 0,
      "turn_id": "turn_id"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
