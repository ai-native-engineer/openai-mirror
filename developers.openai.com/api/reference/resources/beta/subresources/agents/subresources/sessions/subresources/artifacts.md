<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

# Artifacts

##### [Retrieve agent session artifact content](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/content)

GET/agents/sessions/{session\_id}/artifacts/{artifact\_id}/content

##### [Delete an agent session artifact](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/delete)

DELETE/agents/sessions/{session\_id}/artifacts/{artifact\_id}

##### [List agent session artifacts](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/list)

GET/agents/sessions/{session\_id}/artifacts

##### [Retrieve an agent session artifact](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/retrieve)

GET/agents/sessions/{session\_id}/artifacts/{artifact\_id}

##### ModelsExpand Collapse

SessionArtifact object { id, created\_at, environment\_id, 5 more }

An immutable file published by a completed hosted session turn.

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

SessionArtifactDeleted object { id, deleted, object }

Confirmation that an immutable session artifact was deleted.

The ID of the deleted session artifact.

deleted: boolean

Whether the session artifact was deleted. Always `true`.

object: "agent.session.artifact.deleted"

The object type. Always `agent.session.artifact.deleted`.
