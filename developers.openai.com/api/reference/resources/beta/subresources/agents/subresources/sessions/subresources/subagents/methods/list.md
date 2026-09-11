<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/list/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

[Subagents](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/subagents)

# List session subagents

GET/agents/sessions/{session\_id}/subagents

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

session\_id: string

##### Query ParametersExpand Collapse

after: optional string

Return resources after this resource ID in the selected order.

limit: optional number

The maximum number of resources to return, between 1 and 100. Defaults to 20.

minimum1

maximum100

order: optional "asc" or "desc"

The order in which resources are returned. Defaults to `desc`.

"asc"

Returns resources in ascending order.

"desc"

Returns resources in descending order.

data: array of [Subagent](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20subagent%20%3E%20(schema)) { id, closed\_at, instructions, 6 more }

The resources returned in this page, in the requested sort order.

The ID of the subagent.

closed\_at: number or null

The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

instructions: array of [AgentContent](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_content%20%3E%20(schema)) or null

Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

OutputText object { text, type }

A text content part produced by the agent.

text: string

The text produced by the agent.

type: "output\_text"

The content type. Always `output_text`.

EncryptedContent object { encrypted\_content, type }

Encrypted content exchanged between agents.

encrypted\_content: string

The encrypted content payload.

type: "encrypted\_content"

The content type. Always `encrypted_content`.

name: string or null

The runner-assigned nickname, or null when unavailable.

object: "agent.session.subagent"

The object type. Always `agent.session.subagent`.

opened\_at: number

The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

parent\_agent\_id: string

The ID of the agent that created this subagent.

session\_id: string

The ID of the session that owns the subagent.

status: "active" or "closed"

The current status of the subagent.

"active"

The subagent remains available, including while idle between turns.

"closed"

The subagent is closed.

first\_id: string or null

The ID of the first resource in `data`, or `null` if the page is empty.

has\_more: boolean

Whether there are more resources to retrieve after this page.

last\_id: string or null

The ID of the last resource in `data`, or `null` if the page is empty. Pass this as `after` with the same order and filters.

object: "list"

The object type, which is always `list`.

### List session subagents

curl https://api.openai.com/v1/agents/sessions/$SESSION_ID/subagents \

  "data": [
      "closed_at": 0,
      "instructions": [
          "text": "text",
          "type": "output_text"
      ],
      "name": "name",
      "object": "agent.session.subagent",
      "opened_at": 0,
      "parent_agent_id": "parent_agent_id",
      "session_id": "session_id",
      "status": "active"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

  "data": [
      "closed_at": 0,
      "instructions": [
          "text": "text",
          "type": "output_text"
      ],
      "name": "name",
      "object": "agent.session.subagent",
      "opened_at": 0,
      "parent_agent_id": "parent_agent_id",
      "session_id": "session_id",
      "status": "active"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
