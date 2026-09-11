<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/ -->

# Sessions

##### [Create an agent session](/api/reference/resources/beta/subresources/agents/subresources/sessions/methods/create)

POST/agents/sessions

##### [Delete an agent session](/api/reference/resources/beta/subresources/agents/subresources/sessions/methods/delete)

DELETE/agents/sessions/{session\_id}

##### [List agent sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions/methods/list)

GET/agents/sessions

##### [Retrieve an agent session](/api/reference/resources/beta/subresources/agents/subresources/sessions/methods/retrieve)

GET/agents/sessions/{session\_id}

##### [Update an agent session](/api/reference/resources/beta/subresources/agents/subresources/sessions/methods/update)

POST/agents/sessions/{session\_id}

#### SessionsArtifacts

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

#### SessionsEvents

##### [Create agent session input events](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/create)

POST/agents/sessions/{session\_id}/events

##### [Stream agent session events](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/stream)

GET/agents/sessions/{session\_id}/events

#### SessionsItems

##### [List agent session items](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/items/methods/list)

GET/agents/sessions/{session\_id}/items

#### SessionsSubagents

##### [List session subagents](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/list)

GET/agents/sessions/{session\_id}/subagents

##### [Retrieve a session subagent](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/retrieve)

GET/agents/sessions/{session\_id}/subagents/{subagent\_id}

#### SessionsSubagentsItems

##### [List subagent items](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/subresources/items/methods/list)

GET/agents/sessions/{session\_id}/subagents/{subagent\_id}/items

#### SessionsSubagentsTurns

##### [List subagent turns](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/subresources/turns/methods/list)

GET/agents/sessions/{session\_id}/subagents/{subagent\_id}/turns

##### [Retrieve a subagent turn](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/subresources/turns/methods/retrieve)

GET/agents/sessions/{session\_id}/subagents/{subagent\_id}/turns/{turn\_id}

#### SessionsSubagentsTurnsItems

##### [List subagent turn items](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/subresources/turns/subresources/items/methods/list)

GET/agents/sessions/{session\_id}/subagents/{subagent\_id}/turns/{turn\_id}/items

#### SessionsTurns

##### [List agent session turns](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/turns/methods/list)

GET/agents/sessions/{session\_id}/turns

##### [Retrieve an agent session turn](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/turns/methods/retrieve)

GET/agents/sessions/{session\_id}/turns/{turn\_id}

##### ModelsExpand Collapse

Turn object { id, agent\_id, completed\_at, 8 more }

The canonical public representation of a session turn.

The ID of the turn.

agent\_id: string

The ID of the agent that ran the turn.

completed\_at: number or null

The Unix timestamp, in seconds, when the turn reached a terminal state.

The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

error: [SessionTurnError](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20session_turn_error%20%3E%20(schema)) { code, message }  or null

A customer-safe error describing why a session request failed.

object: "agent.session.turn"

The object type. Always `agent.session.turn`.

session\_id: string

The ID of the session that owns the turn.

started\_at: number or null

The Unix timestamp, in seconds, when the turn started.

status: "queued" or "in\_progress" or "waiting" or 3 more

The current status of the turn.

"queued"

The turn is waiting to start.

"in\_progress"

The turn is in progress.

"waiting"

The turn is waiting for external input.

"completed"

The turn completed successfully.

"failed"

The turn failed.

"cancelled"

The turn was cancelled.

subagent\_id: string or null

The ID of the subagent that ran the turn, if applicable.

usage: [TokenUsage](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20token_usage%20%3E%20(schema)) { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }  or null

Recorded token usage for a session or turn. Usage is best effort and may change.
