<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/turns/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

# Turns

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
