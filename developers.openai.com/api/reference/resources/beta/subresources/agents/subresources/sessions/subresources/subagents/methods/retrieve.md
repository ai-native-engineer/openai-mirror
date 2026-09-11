<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/methods/retrieve/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

[Subagents](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/subagents)

# Retrieve a session subagent

GET/agents/sessions/{session\_id}/subagents/{subagent\_id}

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

session\_id: string

subagent\_id: string

Subagent object { id, closed\_at, instructions, 6 more }

A subagent created within a session.

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

### Retrieve a session subagent

curl https://api.openai.com/v1/agents/sessions/$SESSION_ID/subagents/$SUBAGENT_ID \

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
